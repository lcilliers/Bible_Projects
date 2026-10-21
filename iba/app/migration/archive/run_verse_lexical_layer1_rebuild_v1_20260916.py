"""Run the Layer 1 (`verse_lexical`) corpus-wide rebuild — the actual bulk build, separate from
`rebuild_verse_lexical_layer1_v1_20260916.py` (which soft-deleted the old rows and dissolved the
old config) so the before/after counts of each step stay legible, per that script's own docstring.

Researcher, verbatim, 2026-09-15: "layer 1 will be processed in bulk to produce fresh results for
the entire corpus." Escalation #1706 Phase B item 8.

Runs `lib.lexical.build_for_verse_ids` (the readiness-checked, identity-stable write path) against
every live verse, in book-sized batches (commit per book) so a mid-run interruption loses at most
one book's worth of work, not the whole corpus, and progress is visible. Safe to re-run: Layer 1's
own write is identity-stable (escalation #1520) — a verse already correctly rebuilt is a true no-op.

Usage:
    python iba/app/migration/run_verse_lexical_layer1_rebuild_v1_20260916.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys
import time

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sys.path.insert(0, r"C:\Bible_study_projects")
    from iba.app.lib import lexical

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    unready = lexical.unready_codes_in_scope(
        conn, [r["id"] for r in conn.execute("SELECT id FROM verse WHERE deleted=0")])
    if unready:
        print(f"ABORT: {len(unready)} code(s) in the full corpus scope are not ready "
             f"(zero cluster_strong allocation): {unready[:20]}")
        conn.close()
        return 1

    books = [r["book"] for r in conn.execute(
        "SELECT book FROM cfg_book_order WHERE inactive=0 ORDER BY ordinal")]

    grand = {"verses": 0, "spans": 0, "codes": 0, "inserted": 0, "updated": 0, "unchanged": 0,
            "removed": 0, "removed_with_live_notes": 0}
    t0 = time.time()
    for book in books:
        verse_ids = [r["id"] for r in conn.execute(
            "SELECT id FROM verse WHERE deleted=0 AND osisId LIKE ? ORDER BY id",
            (f"{book}.%",))]
        if not verse_ids:
            continue
        totals = lexical.build_for_verse_ids(conn, verse_ids)
        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()
        for k in grand:
            grand[k] += totals.get(k, 0)
        print(f"{book}: {totals['verses']} verse(s), {totals['codes']} code(s) "
             f"({totals['inserted']} ins / {totals['updated']} upd / {totals['unchanged']} unch) "
             f"— running total {grand['verses']} verses, {grand['codes']} codes, "
             f"{time.time() - t0:.1f}s elapsed")

    print()
    print(f"DONE ({'DRY-RUN, all rolled back' if args.dry_run else 'COMMITTED per book'}): "
         f"{grand['verses']} verse(s), {grand['spans']} span(s), {grand['codes']} code(s) — "
         f"{grand['inserted']} inserted, {grand['updated']} updated, {grand['unchanged']} "
         f"unchanged, {grand['removed']} removed ({grand['removed_with_live_notes']} with live "
         f"notes now dangling) — {time.time() - t0:.1f}s total")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
