"""
Apply stem-extraction-patch-20260319-v1.json

Phase 1 — UPDATE wa_meaning_parsed for 643 rows listed in wa_meaning_parsed_create
           (these existed in our DB post-realignment; patch now supplies correct
           stem_count / has_causative_stem / top_sense_count / parse_version)
Phase 2 — UPDATE wa_meaning_parsed for 538 rows listed in wa_meaning_parsed_update
Phase 3 — INSERT 695 rows into wa_meaning_stem (empty table)
           parsed_meaning_id resolved via term_inv_id lookup in wa_meaning_parsed
Phase 4 — UPDATE wa_term_inventory.causative_form_present for causative_flag_corrections
           where recommended_value is 0 or 1 (skip 'REVIEW' entries)
"""

import sqlite3
import json
import os
import sys

DB_PATH   = os.path.join("database", "bible_research.db")
PATCH_PATH = os.path.join("Sessions", "Patches",
                          "stem-extraction-patch-20260319-v1.json")

def main():
    with open(PATCH_PATH, encoding="utf-8") as f:
        patch = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # ── build a term_inv_id → wa_meaning_parsed.id lookup ──────────────────
    cur.execute("SELECT id, term_inv_id FROM wa_meaning_parsed")
    parsed_lookup = {r["term_inv_id"]: r["id"] for r in cur.fetchall()}
    print(f"wa_meaning_parsed rows loaded into lookup: {len(parsed_lookup)}")

    # ══════════════════════════════════════════════════════════════════════
    # Phase 1 — UPDATE wa_meaning_parsed from wa_meaning_parsed_create list
    # ══════════════════════════════════════════════════════════════════════
    p1_updated = 0
    p1_skipped = 0
    for row in patch["wa_meaning_parsed_create"]:
        tid = row["term_inv_id"]
        if tid not in parsed_lookup:
            p1_skipped += 1
            continue
        cur.execute("""
            UPDATE wa_meaning_parsed
            SET top_sense_count    = ?,
                stem_count         = ?,
                has_causative_stem = ?,
                has_domain_tags    = ?,
                parsed_at          = ?,
                parse_version      = ?,
                parse_warnings     = ?
            WHERE term_inv_id = ?
        """, (
            row["top_sense_count"],
            row["stem_count"],
            row["has_causative_stem"],
            row["has_domain_tags"],
            row["parsed_at"],
            row["parse_version"],
            json.dumps(row["parse_warnings"]) if row["parse_warnings"] else None,
            tid,
        ))
        p1_updated += cur.rowcount

    print(f"\nPhase 1 — wa_meaning_parsed_create updates:")
    print(f"  Updated : {p1_updated}")
    print(f"  Skipped : {p1_skipped}  (term_inv_id not in DB)")

    # ══════════════════════════════════════════════════════════════════════
    # Phase 2 — UPDATE wa_meaning_parsed from wa_meaning_parsed_update list
    # ══════════════════════════════════════════════════════════════════════
    p2_updated = 0
    p2_skipped = 0
    for row in patch["wa_meaning_parsed_update"]:
        tid = row["term_inv_id"]
        if tid not in parsed_lookup:
            p2_skipped += 1
            continue
        cur.execute("""
            UPDATE wa_meaning_parsed
            SET stem_count         = ?,
                has_causative_stem = ?
            WHERE term_inv_id = ?
        """, (
            row["stem_count"],
            row["has_causative_stem"],
            tid,
        ))
        p2_updated += cur.rowcount

    print(f"\nPhase 2 — wa_meaning_parsed_update updates:")
    print(f"  Updated : {p2_updated}")
    print(f"  Skipped : {p2_skipped}  (term_inv_id not in DB)")

    # ══════════════════════════════════════════════════════════════════════
    # Phase 3 — INSERT wa_meaning_stem
    # ══════════════════════════════════════════════════════════════════════
    p3_inserted = 0
    p3_skipped  = 0
    p3_errors   = []
    for row in patch["wa_meaning_stem_insert"]:
        tid = row["term_inv_id"]
        parsed_id = parsed_lookup.get(tid)
        if parsed_id is None:
            p3_skipped += 1
            p3_errors.append(f"  term_inv_id={tid} ({row['strongs_number']}) not found in wa_meaning_parsed")
            continue
        cur.execute("""
            INSERT INTO wa_meaning_stem
                (parsed_meaning_id, stem_name, stem_type, sense_count, top_sense_text)
            VALUES (?, ?, ?, ?, ?)
        """, (
            parsed_id,
            row["stem_name"],
            row["stem_type"],
            row["sense_count"],
            row["top_sense_text"],
        ))
        p3_inserted += 1

    print(f"\nPhase 3 — wa_meaning_stem inserts:")
    print(f"  Inserted: {p3_inserted}")
    print(f"  Skipped : {p3_skipped}")
    if p3_errors:
        for e in p3_errors[:10]:
            print(e)
        if len(p3_errors) > 10:
            print(f"  ... and {len(p3_errors)-10} more")

    # ══════════════════════════════════════════════════════════════════════
    # Phase 4 — causative_form_present corrections (skip REVIEW entries)
    # ══════════════════════════════════════════════════════════════════════
    p4_updated  = 0
    p4_review   = 0
    p4_skipped  = 0
    for row in patch["causative_flag_corrections"]:
        rec_val = row["recommended_value"]
        if not isinstance(rec_val, int):
            p4_review += 1
            continue
        tid = row["term_inv_id"]
        cur.execute("""
            UPDATE wa_term_inventory
            SET causative_form_present = ?
            WHERE id = ?
        """, (rec_val, tid))
        if cur.rowcount:
            p4_updated += 1
        else:
            p4_skipped += 1

    print(f"\nPhase 4 — causative_form_present corrections:")
    print(f"  Updated : {p4_updated}")
    print(f"  Skipped (REVIEW) : {p4_review}")
    print(f"  Not found       : {p4_skipped}")

    # ══════════════════════════════════════════════════════════════════════
    # Verify
    # ══════════════════════════════════════════════════════════════════════
    cur.execute("SELECT COUNT(*) FROM wa_meaning_stem")
    stem_total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM wa_meaning_stem WHERE stem_type = 'piel_causative' OR stem_type LIKE '%causative%'")
    causative_stems = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE stem_count > 0")
    parsed_with_stems = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM wa_meaning_parsed WHERE has_causative_stem = 1")
    parsed_causative_flag = cur.fetchone()[0]

    print(f"\n── Verification ──")
    print(f"  wa_meaning_stem total rows   : {stem_total}")
    print(f"  Causative stem rows          : {causative_stems}")
    print(f"  wa_meaning_parsed stem_count>0: {parsed_with_stems}")
    print(f"  wa_meaning_parsed has_causative_stem=1: {parsed_causative_flag}")

    # Orphan check
    cur.execute("""
        SELECT COUNT(*) FROM wa_meaning_stem ms
        WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = ms.parsed_meaning_id)
    """)
    orphans = cur.fetchone()[0]
    print(f"  Orphaned wa_meaning_stem rows: {orphans}")

    conn.commit()
    print("\nPatch applied and committed.")

if __name__ == "__main__":
    main()
