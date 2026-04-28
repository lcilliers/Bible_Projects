"""
_backfill_span_match.py
────────────────────────
Fix 2: For all wa_verse_records rows where span_strong_match IS NULL,
fetch verse HTML from the STEP API per term and apply the span filter.

Strategy:
  - Group NULL rows by strongs_number (1 API call per term, not per verse)
  - Match STEP results back to DB rows by reference string
  - Update span_strong_match + target_word in batches
  - Commit every term; resume-safe (only processes NULL rows)

Rows where STEP returns no HTML for a verse get span_strong_match = NULL preserved
(no update) so they can be retried later.
"""
import sqlite3
import sys
import os
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")

from analytics.step_client import StepClient
from engine.span_filter import apply_span_filter

DB = r"G:\My Drive\Bible_study_projects\database\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
client = StepClient()

# Get all distinct strongs_numbers that have NULL span rows
terms = conn.execute("""
    SELECT ti.strongs_number, COUNT(vr.id) as cnt
    FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
    WHERE vr.span_strong_match IS NULL
    GROUP BY ti.strongs_number
    ORDER BY ti.strongs_number
""").fetchall()

total_terms = len(terms)
print(f"Terms to process: {total_terms}")
print()

total_updated = 0
total_match1  = 0
total_match0  = 0
total_no_html = 0
total_errors  = 0

for i, term_row in enumerate(terms, 1):
    strongs = term_row["strongs_number"]
    cnt     = term_row["cnt"]
    print(f"[{i:3}/{total_terms}] {strongs} ({cnt} rows) ... ", end="", flush=True)

    try:
        raw_records, html_map = client.get_verse_records_with_html(strongs)
    except Exception as exc:
        print(f"ERROR: {exc}")
        total_errors += 1
        continue

    if not raw_records and not html_map:
        print("no STEP data")
        total_errors += 1
        continue

    # Build ref -> {span_strong_match, target_word} from STEP results
    ref_results = {}
    for rec in raw_records:
        ref  = rec.get("ref", "")
        osis = rec.get("osisId", "")
        html = html_map.get(osis, "")
        if html:
            result = apply_span_filter(html, strongs)
            ref_results[ref] = {
                "span_strong_match": 1 if result["match"] else 0,
                "target_word":       result["target_word"] or "",
            }
        else:
            # No HTML available for this verse — leave span_strong_match NULL
            ref_results[ref] = None

    # Fetch the NULL rows for this term from DB
    db_rows = conn.execute("""
        SELECT vr.id, vr.reference
        FROM wa_verse_records vr
        JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
        WHERE vr.span_strong_match IS NULL
          AND ti.strongs_number = ?
    """, (strongs,)).fetchall()

    updates_match1  = []
    updates_match0  = []
    no_html_count   = 0

    for row in db_rows:
        ref    = row["reference"]
        result = ref_results.get(ref)
        if result is None:
            no_html_count += 1
            continue
        if result["span_strong_match"] == 1:
            updates_match1.append((result["target_word"], row["id"]))
        else:
            updates_match0.append((result["target_word"], row["id"]))

    if updates_match1:
        conn.executemany(
            "UPDATE wa_verse_records SET span_strong_match=1, target_word=? WHERE id=?",
            updates_match1
        )
    if updates_match0:
        conn.executemany(
            "UPDATE wa_verse_records SET span_strong_match=0, target_word=? WHERE id=?",
            updates_match0
        )
    conn.commit()

    updated = len(updates_match1) + len(updates_match0)
    total_updated += updated
    total_match1  += len(updates_match1)
    total_match0  += len(updates_match0)
    total_no_html += no_html_count

    print(f"match=1: {len(updates_match1):3}  match=0: {len(updates_match0):3}  no_html: {no_html_count}")

print()
print("=" * 50)
print(f"Done.")
print(f"  Total rows updated:  {total_updated}")
print(f"  span_strong_match=1: {total_match1}")
print(f"  span_strong_match=0: {total_match0}")
print(f"  No HTML (skipped):   {total_no_html}")
print(f"  Term errors:         {total_errors}")
print()

# Final NULL count
remaining = conn.execute(
    "SELECT COUNT(*) FROM wa_verse_records WHERE span_strong_match IS NULL"
).fetchone()[0]
print(f"  Remaining NULL span_strong_match: {remaining}")

conn.close()
