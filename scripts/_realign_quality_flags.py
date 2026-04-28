"""
_realign_quality_flags.py
─────────────────────────
Full reset and recompute of wa_data_quality_flags.

Phase 1 — Clear everything
    DELETE all existing wa_data_quality_flags rows.

Phase 2 — Complete words: recompute all derivable DATA_COVERAGE flags
    For each file_id of a Complete word:
      - queued_span_conflicts: empty (term_fetch_log has 0 span_conflict rows)
      - run_flag_engine() → THIN_DATA, SMALL_VERSE_SAMPLE, NO_VERSES,
        NO_WORD_ANALYSIS, SPAN_RESOLUTION_CONFLICT
      - SPAN_FILTER_APPLIED: written separately for terms with any
        wa_verse_records where span_strong_match = 0

Phase 3 — Verify
    Before/after counts by flag code.

Note:
    IMPORT_STATUS, TERM_ANALYSIS, and NOTE groups are NOT re-inserted —
    removed permanently as they have no further value for phase 2 research.

    Excluded words: 0 have wa_file_index rows, so no REGISTRY_STATUS flags
    can be attached (the file_id FK is NOT NULL). Excluded words are simply
    left with no quality flag rows.

Usage:
    python scripts/_realign_quality_flags.py            # live run
    python scripts/_realign_quality_flags.py --dry-run  # preview only
"""

import argparse
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import sqlite3
from engine.flag_engine import run_flag_engine

DB = os.path.join(ROOT, "database", "bible_research.db")


def hr(label=""):
    width = 72
    if label:
        pad = (width - len(label) - 2) // 2
        right = width - len(label) - 2 - pad
        print("\n%s %s %s" % ("─" * pad, label, "─" * right))
    else:
        print("─" * width)


def section(title):
    print("\n%s\n  %s\n%s" % ("=" * 72, title, "=" * 72))


def flag_distribution(conn, label):
    """Print current flag counts by code."""
    print("\n  %s" % label)
    rows = conn.execute("""
        SELECT qft.flag_group, qft.flag_code, COUNT(*) AS cnt
        FROM wa_data_quality_flags dqf
        JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
        GROUP BY qft.flag_code
        ORDER BY qft.flag_group, cnt DESC
    """).fetchall()
    total = conn.execute("SELECT COUNT(*) FROM wa_data_quality_flags").fetchone()[0]
    if not rows:
        print("    (empty)")
    for r in rows:
        print("    %-18s  %-35s  %d" % (r["flag_group"], r["flag_code"], r["cnt"]))
    print("    TOTAL: %d rows" % total)


def get_span_filter_applied_id(conn):
    row = conn.execute(
        "SELECT id FROM wa_quality_flag_types WHERE flag_code = 'SPAN_FILTER_APPLIED'"
    ).fetchone()
    return row["id"] if row else None


def write_span_filter_applied(conn, file_id, span_fid):
    """Write SPAN_FILTER_APPLIED for each term in file_id that has filtered verses."""
    terms_with_filtered = conn.execute("""
        SELECT DISTINCT ti.id, ti.strongs_number, ti.term_id,
               COUNT(*) AS filtered_count
        FROM wa_term_inventory ti
        JOIN wa_verse_records vr ON vr.term_inv_id = ti.id
        WHERE ti.file_id = ? AND vr.span_strong_match = 0
        GROUP BY ti.id
    """, (file_id,)).fetchall()

    for t in terms_with_filtered:
        strongs = t["strongs_number"] or t["term_id"] or ""
        conn.execute(
            "INSERT INTO wa_data_quality_flags (file_id, term_id, flag_id, description)"
            " VALUES (?, ?, ?, ?)",
            (
                file_id, strongs, span_fid,
                "Span filter removed %d verse(s) for %s: span_strong_match=0 "
                "records exist in wa_verse_records." % (t["filtered_count"], strongs)
            )
        )
    return len(terms_with_filtered)


def main():
    parser = argparse.ArgumentParser(
        description="Reset and recompute wa_data_quality_flags from data."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview counts without writing.")
    args = parser.parse_args()

    if args.dry_run:
        print("\n*** DRY RUN — no changes will be written ***")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")

    # ── Before state ──────────────────────────────────────────────────────────
    section("Before state")
    flag_distribution(conn, "Current wa_data_quality_flags distribution:")

    if args.dry_run:
        # Just show what would happen
        section("Dry-run preview")
        complete_files = conn.execute("""
            SELECT fi.id, fi.word
            FROM wa_file_index fi
            JOIN word_registry wr ON wr.id = fi.word_registry_fk
            WHERE wr.phase1_status = 'Complete'
            ORDER BY fi.word, fi.id
        """).fetchall()
        print("  Complete word files to recompute:  %d" % len(complete_files))

        span_fid = get_span_filter_applied_id(conn)
        span_filter_terms = conn.execute("""
            SELECT COUNT(DISTINCT ti.id) FROM wa_term_inventory ti
            JOIN wa_verse_records vr ON vr.term_inv_id = ti.id
            JOIN wa_file_index fi ON fi.id = ti.file_id
            JOIN word_registry wr ON wr.id = fi.word_registry_fk
            WHERE wr.phase1_status = 'Complete' AND vr.span_strong_match = 0
        """).fetchone()[0]
        print("  Terms needing SPAN_FILTER_APPLIED: %d" % span_filter_terms)
        print("  [DRY RUN — no changes written]")
        conn.close()
        return

    # ── Phase 1: Clear everything ─────────────────────────────────────────────
    section("Phase 1 — Clear all existing flags")
    deleted = conn.execute("DELETE FROM wa_data_quality_flags").rowcount
    conn.commit()
    print("  Deleted: %d rows" % deleted)

    # ── Phase 2: Recompute for Complete words ─────────────────────────────────
    section("Phase 2 — Recompute DATA_COVERAGE flags for Complete words")

    span_fid = get_span_filter_applied_id(conn)
    if span_fid is None:
        print("  WARNING: SPAN_FILTER_APPLIED not found in wa_quality_flag_types — skipping")

    complete_files = conn.execute("""
        SELECT fi.id AS file_id, wr.id AS registry_id, fi.word
        FROM wa_file_index fi
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE wr.phase1_status = 'Complete'
        ORDER BY wr.id, fi.id
    """).fetchall()

    print("  Processing %d files..." % len(complete_files))

    total_flags = 0
    total_span_filter = 0
    errors = []

    # Span conflicts: term_fetch_log has 0 span_conflict=1 rows,
    # so queued_span_conflicts is always empty.
    # (Verified: SELECT COUNT(*) FROM term_fetch_log WHERE span_conflict=1 → 0)
    EMPTY_SPAN_CONFLICTS: set = set()

    for f in complete_files:
        file_id = f["file_id"]
        registry_id = f["registry_id"]
        try:
            result = run_flag_engine(conn, file_id, registry_id, EMPTY_SPAN_CONFLICTS)
            total_flags += result["flags_written"]
            errors.extend(result.get("errors", []))
        except Exception as exc:
            errors.append("file_id=%d (%s): run_flag_engine failed: %s" % (
                file_id, f["word"], exc))

        # SPAN_FILTER_APPLIED — not handled by run_flag_engine
        if span_fid:
            try:
                n = write_span_filter_applied(conn, file_id, span_fid)
                total_span_filter += n
                total_flags += n
            except Exception as exc:
                errors.append("file_id=%d (%s): SPAN_FILTER_APPLIED failed: %s" % (
                    file_id, f["word"], exc))

    conn.commit()
    print("  Flags written (derivable):   %d" % total_flags)
    print("  SPAN_FILTER_APPLIED written: %d terms across all files" % total_span_filter)
    print("  Errors:                      %d" % len(errors))
    for e in errors:
        print("    " + e)

    # ── Phase 3: Verify ───────────────────────────────────────────────────────
    section("Phase 3 — Verification")
    flag_distribution(conn, "After-state wa_data_quality_flags distribution:")

    hr("unused flag codes")
    unused = conn.execute("""
        SELECT flag_group, flag_code FROM wa_quality_flag_types
        WHERE id NOT IN (SELECT DISTINCT flag_id FROM wa_data_quality_flags)
        ORDER BY flag_group, flag_code
    """).fetchall()
    for r in unused:
        print("  %-18s  %s" % (r["flag_group"], r["flag_code"]))

    hr("orphan check")
    orphan_files = conn.execute("""
        SELECT COUNT(*) FROM wa_data_quality_flags
        WHERE file_id NOT IN (SELECT id FROM wa_file_index)
    """).fetchone()[0]
    orphan_types = conn.execute("""
        SELECT COUNT(*) FROM wa_data_quality_flags
        WHERE flag_id NOT IN (SELECT id FROM wa_quality_flag_types)
    """).fetchone()[0]
    print("  Orphan file_id refs:  %d  %s" % (orphan_files, "OK" if orphan_files == 0 else "!! PROBLEM"))
    print("  Orphan flag_id refs:  %d  %s" % (orphan_types, "OK" if orphan_types == 0 else "!! PROBLEM"))

    hr()
    print("  Done.")
    hr()
    conn.close()


if __name__ == "__main__":
    main()
