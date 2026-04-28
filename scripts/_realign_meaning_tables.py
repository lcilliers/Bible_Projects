"""
_realign_meaning_tables.py
──────────────────────────
One-off re-alignment of the meaning parse tables.

Uses the existing engine/meaning_parser.run_parser() — no STEP API needed.
The vocab dict is assembled entirely from wa_term_inventory columns.

Phases
──────
  Phase 1 — First-time parse
      Target: wa_term_inventory rows WHERE parsed_meaning_id IS NULL
              AND (meaning IS NOT NULL OR lsj_entry IS NOT NULL)
      Action: run run_parser() → writes wa_meaning_parsed, wa_meaning_sense,
              wa_meaning_stem (Hebrew), wa_lsj_parsed (Greek),
              sets parsed_meaning_id FK.

  Phase 2 — Fix language mismatch
      Target: wa_meaning_parsed rows WHERE language = 'Hebrew'
              but the joined wa_term_inventory.language = 'Greek'
              (currently 300 rows from the previous diagnostic)
      Action: run_parser() again (idempotent) — rebuilds the rows with the
              correct language and also adds the missing wa_lsj_parsed record
              for any row that has lsj_entry text.

  Phase 3 — Verify + anomaly report
      Read-only: print after-action counts and flag any residual anomalies
      for researcher review.

Usage
──────
  # Preview without writing anything:
  python scripts/_realign_meaning_tables.py --dry-run

  # Execute all phases:
  python scripts/_realign_meaning_tables.py

  # Execute a single phase:
  python scripts/_realign_meaning_tables.py --phase 1
  python scripts/_realign_meaning_tables.py --phase 2
"""

import argparse
import os
import sqlite3
import sys

# ── path setup ───────────────────────────────────────────────────────────────
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from engine.meaning_parser import run_parser  # noqa: E402

DB = os.path.join(ROOT, "database", "bible_research.db")


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def hr(label=""):
    width = 72
    if label:
        pad = (width - len(label) - 2) // 2
        right = width - len(label) - 2 - pad
        print(f"\n{'─' * pad} {label} {'─' * right}")
    else:
        print("─" * width)


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def build_vocab(row) -> dict:
    """Build the vocab dict that run_parser() expects from a wa_term_inventory row."""
    return {
        "strong_number": row["strongs_number"] or row["term_id"] or "",
        "language":      row["language"],
        "medium_def":    row["meaning"] or "",
        "lsj_entry":     row["lsj_entry"] or "",
    }


# ─────────────────────────────────────────────────────────────────────────────
# Phase 1 — First-time parse
# ─────────────────────────────────────────────────────────────────────────────

def phase1(conn, dry_run: bool) -> dict:
    section("Phase 1 — First-time parse (parsed_meaning_id IS NULL)")

    target = conn.execute("""
        SELECT ti.id, ti.language, ti.term_id, ti.strongs_number,
               ti.transliteration, ti.meaning, ti.lsj_entry
        FROM wa_term_inventory ti
        WHERE ti.parsed_meaning_id IS NULL
          AND (
              (ti.meaning IS NOT NULL AND TRIM(ti.meaning) != '')
              OR (ti.lsj_entry IS NOT NULL AND TRIM(ti.lsj_entry) != '')
          )
        ORDER BY ti.language, ti.id
    """).fetchall()

    skipped_no_content = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory
        WHERE parsed_meaning_id IS NULL
          AND (meaning IS NULL OR TRIM(meaning) = '')
          AND (lsj_entry IS NULL OR TRIM(lsj_entry) = '')
    """).fetchone()[0]

    print(f"  Target terms to parse:       {len(target)}")
    print(f"  Skipped (no content at all): {skipped_no_content}")

    if dry_run:
        print("  [DRY RUN — no changes written]")
        return {"parsed": 0, "errors": [], "skipped": skipped_no_content}

    parsed = 0
    errors = []
    for row in target:
        vocab = build_vocab(row)
        try:
            run_parser(conn, row["id"], vocab)
            parsed += 1
        except Exception as exc:
            errors.append(f"  ti.id={row['id']}  {row['strongs_number']}  {row['transliteration']}: {exc}")

    conn.commit()
    print(f"  Parsed:  {parsed}")
    print(f"  Errors:  {len(errors)}")
    for e in errors:
        print(e)
    return {"parsed": parsed, "errors": errors, "skipped": skipped_no_content}


# ─────────────────────────────────────────────────────────────────────────────
# Phase 2 — Fix language mismatch
# ─────────────────────────────────────────────────────────────────────────────

def phase2(conn, dry_run: bool) -> dict:
    section("Phase 2 — Fix language mismatch (wa_meaning_parsed.language wrong)")

    # find terms where the stored language in wa_meaning_parsed differs from
    # the authoritative wa_term_inventory.language
    target = conn.execute("""
        SELECT ti.id, ti.language AS correct_lang, ti.term_id,
               ti.strongs_number, ti.transliteration, ti.meaning, ti.lsj_entry,
               mp.language AS stored_lang, mp.id AS mp_id
        FROM wa_term_inventory ti
        JOIN wa_meaning_parsed mp ON mp.term_inv_id = ti.id
        WHERE mp.language != ti.language
        ORDER BY ti.language, ti.id
    """).fetchall()

    print(f"  Mismatched language rows:    {len(target)}")

    if not target:
        print("  Nothing to fix.")
        return {"reparsed": 0, "errors": []}

    # Show a language breakdown
    from collections import Counter
    counts = Counter((r["stored_lang"], r["correct_lang"]) for r in target)
    for (stored, correct), cnt in sorted(counts.items()):
        print(f"    stored='{stored}' -> correct='{correct}':  {cnt} rows")

    if dry_run:
        print("  [DRY RUN — no changes written]")
        return {"reparsed": 0, "errors": []}

    reparsed = 0
    errors = []
    for row in target:
        # Phase 2 row uses aliased column names — build vocab explicitly
        vocab = {
            "strong_number": row["strongs_number"] or row["term_id"] or "",
            "language":      row["correct_lang"],
            "medium_def":    row["meaning"] or "",
            "lsj_entry":     row["lsj_entry"] or "",
        }
        try:
            run_parser(conn, row["id"], vocab)
            reparsed += 1
        except Exception as exc:
            errors.append(f"  ti.id={row['id']}  {row['strongs_number']}  {row['transliteration']}: {exc}")

    conn.commit()
    print(f"  Re-parsed: {reparsed}")
    print(f"  Errors:    {len(errors)}")
    for e in errors:
        print(e)
    return {"reparsed": reparsed, "errors": errors}


# ─────────────────────────────────────────────────────────────────────────────
# Phase 3 — Verify + anomaly report
# ─────────────────────────────────────────────────────────────────────────────

def phase3(conn) -> None:
    section("Phase 3 — Verification and anomaly report")

    hr("wa_meaning_parsed coverage")
    total_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
    total_mp = conn.execute("SELECT COUNT(*) FROM wa_meaning_parsed").fetchone()[0]
    covered  = conn.execute(
        "SELECT COUNT(*) FROM wa_term_inventory WHERE parsed_meaning_id IS NOT NULL"
    ).fetchone()[0]
    uncovered = total_ti - covered
    print(f"  wa_term_inventory total:          {total_ti}")
    print(f"  wa_meaning_parsed total:          {total_mp}")
    print(f"  Terms with parsed_meaning_id set: {covered}  ({100*covered//total_ti}%)")
    print(f"  Still unparsed:                   {uncovered}")

    hr("language alignment (should be 0 mismatches)")
    rows = conn.execute("""
        SELECT mp.language AS mp_lang, ti.language AS ti_lang, COUNT(*) AS cnt,
               CASE WHEN mp.language = ti.language THEN 'OK' ELSE 'MISMATCH' END AS status
        FROM wa_meaning_parsed mp
        JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
        GROUP BY mp.language, ti.language
        ORDER BY status DESC, mp.language
    """).fetchall()
    for r in rows:
        print(f"  mp.language={r['mp_lang']:<8}  ti.language={r['ti_lang']:<8}  rows={r['cnt']:>4}  [{r['status']}]")

    hr("wa_meaning_sense")
    total_sense = conn.execute("SELECT COUNT(*) FROM wa_meaning_sense").fetchone()[0]
    parsed_no_sense = conn.execute("""
        SELECT COUNT(*) FROM wa_meaning_parsed mp
        WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_sense s WHERE s.parsed_meaning_id = mp.id)
    """).fetchone()[0]
    print(f"  Total wa_meaning_sense rows:          {total_sense}")
    print(f"  Parsed entries with no sense rows:    {parsed_no_sense}")

    hr("wa_meaning_stem (Hebrew only)")
    total_stem = conn.execute("SELECT COUNT(*) FROM wa_meaning_stem").fetchone()[0]
    heb_mp = conn.execute(
        "SELECT COUNT(*) FROM wa_meaning_parsed WHERE language = 'Hebrew'"
    ).fetchone()[0]
    heb_with_stems = conn.execute("""
        SELECT COUNT(DISTINCT parsed_meaning_id) FROM wa_meaning_stem
    """).fetchone()[0]
    print(f"  Total wa_meaning_stem rows:           {total_stem}")
    print(f"  Hebrew parsed entries:                {heb_mp}")
    print(f"  Hebrew entries with stem rows:        {heb_with_stems}")

    hr("wa_lsj_parsed (Greek only)")
    total_lsj   = conn.execute("SELECT COUNT(*) FROM wa_lsj_parsed").fetchone()[0]
    greek_ti    = conn.execute(
        "SELECT COUNT(*) FROM wa_term_inventory WHERE language = 'Greek'"
    ).fetchone()[0]
    greek_w_lsj = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
        WHERE ti.language = 'Greek'
          AND EXISTS (SELECT 1 FROM wa_lsj_parsed lsj WHERE lsj.term_inv_id = ti.id)
    """).fetchone()[0]
    greek_w_lsj_entry = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory
        WHERE language = 'Greek'
          AND lsj_entry IS NOT NULL AND TRIM(lsj_entry) != ''
    """).fetchone()[0]
    print(f"  Total wa_lsj_parsed rows:             {total_lsj}")
    print(f"  Greek terms in wa_term_inventory:     {greek_ti}")
    print(f"  Greek terms with lsj_entry text:      {greek_w_lsj_entry}")
    print(f"  Greek terms with wa_lsj_parsed row:   {greek_w_lsj}")
    lsj_still_missing = greek_w_lsj_entry - greek_w_lsj
    print(f"  lsj_entry present but no parse row:   {lsj_still_missing}")

    hr("orphan check (all should be 0)")
    orphan_mp = conn.execute("""
        SELECT COUNT(*) FROM wa_meaning_parsed mp
        WHERE NOT EXISTS (SELECT 1 FROM wa_term_inventory ti WHERE ti.id = mp.term_inv_id)
    """).fetchone()[0]
    orphan_s = conn.execute("""
        SELECT COUNT(*) FROM wa_meaning_sense s
        WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = s.parsed_meaning_id)
    """).fetchone()[0]
    orphan_st = conn.execute("""
        SELECT COUNT(*) FROM wa_meaning_stem st
        WHERE NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = st.parsed_meaning_id)
    """).fetchone()[0]
    orphan_lsj = conn.execute("""
        SELECT COUNT(*) FROM wa_lsj_parsed lsj
        WHERE NOT EXISTS (SELECT 1 FROM wa_term_inventory ti WHERE ti.id = lsj.term_inv_id)
    """).fetchone()[0]
    broken_fk = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory
        WHERE parsed_meaning_id IS NOT NULL
          AND NOT EXISTS (SELECT 1 FROM wa_meaning_parsed mp WHERE mp.id = parsed_meaning_id)
    """).fetchone()[0]
    for label, val in [
        ("orphan wa_meaning_parsed",           orphan_mp),
        ("orphan wa_meaning_sense",            orphan_s),
        ("orphan wa_meaning_stem",             orphan_st),
        ("orphan wa_lsj_parsed",               orphan_lsj),
        ("broken parsed_meaning_id FK",        broken_fk),
    ]:
        flag = "  OK" if val == 0 else "  !! PROBLEM"
        print(f"  {label:<40} {val:>4}{flag}")

    hr("anomalies for researcher review")

    # Terms still unparsed — breakdown by why
    no_content = conn.execute("""
        SELECT ti.id, fi.word, ti.language, ti.strongs_number, ti.transliteration
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE ti.parsed_meaning_id IS NULL
          AND (ti.meaning IS NULL OR TRIM(ti.meaning) = '')
          AND (ti.lsj_entry IS NULL OR TRIM(ti.lsj_entry) = '')
        ORDER BY fi.word, ti.id
    """).fetchall()
    print(f"\n  Terms with NO content to parse (parsed_meaning_id stays NULL): {len(no_content)}")
    for r in no_content[:20]:
        print(f"    ti.id={r['id']:>4}  [{r['language'][:3]}]  {r['word']:<16}  "
              f"{(r['strongs_number'] or '')::<10}  {r['transliteration']}")
    if len(no_content) > 20:
        print(f"    … and {len(no_content)-20} more")

    # Hebrew lsj_entry anomaly
    heb_lsj = conn.execute("""
        SELECT ti.id, fi.word, ti.strongs_number, ti.transliteration,
               SUBSTR(ti.lsj_entry, 1, 60) AS lsj_snippet
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE ti.language = 'Hebrew'
          AND ti.lsj_entry IS NOT NULL AND TRIM(ti.lsj_entry) != ''
    """).fetchall()
    print(f"\n  Hebrew terms with lsj_entry (anomaly): {len(heb_lsj)}")
    for r in heb_lsj:
        print(f"    ti.id={r['id']:>4}  {r['word']:<16}  {(r['strongs_number'] or '')::<10}  "
              f"{r['transliteration']}  lsj='{r['lsj_snippet']}…'")

    # parse_warnings summary
    hr("parse_warnings distribution")
    warn_rows = conn.execute("""
        SELECT parse_warnings, COUNT(*) AS cnt
        FROM wa_meaning_parsed
        WHERE parse_warnings IS NOT NULL AND TRIM(parse_warnings) != ''
        GROUP BY parse_warnings
        ORDER BY cnt DESC
        LIMIT 15
    """).fetchall()
    for r in warn_rows:
        print(f"  {r['parse_warnings']:<40}  {r['cnt']:>5}")
    if not warn_rows:
        print("  (none)")

    hr()
    print("  Phase 3 complete.")
    hr()


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Re-align meaning parse tables from wa_term_inventory source data."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview counts without writing anything to the database."
    )
    parser.add_argument(
        "--phase", type=int, choices=[1, 2, 3],
        help="Run only a specific phase (default: all phases)."
    )
    args = parser.parse_args()

    if args.dry_run:
        print("\n*** DRY RUN MODE — no database changes will be made ***")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")

    run_all = args.phase is None

    try:
        if run_all or args.phase == 1:
            result1 = phase1(conn, dry_run=args.dry_run)

        if run_all or args.phase == 2:
            result2 = phase2(conn, dry_run=args.dry_run)

        if run_all or args.phase == 3:
            if args.dry_run:
                print("\n  [Phase 3 skipped in dry-run mode — no data written yet]")
            else:
                phase3(conn)

    except Exception as exc:
        conn.rollback()
        print(f"\nFATAL ERROR — rolled back: {exc}", file=sys.stderr)
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
