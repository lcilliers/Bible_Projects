"""
_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py

Soft-delete stray ve_lexical rows that sit on INACTIVE (delete_flagged=1) verse_records.

Integrity rule: an active ve_lexical row should never hang off a delete_flagged
verse_record (an XREF / duplicate copy). Found 187 such rows across 106 verse_contexts
— all the `faculty` item (ve_nr 7), all from the run `faculty-verse-explicit-v1-20260626`,
which wrote faculty onto delete_flagged records that the main v2-engine sweep skips.

Action: set ve_lexical.delete_flagged=1 for these rows (reversible; preserves audit).
Safe: backs up the DB first; dry-run by default; single transaction; verifies.

Usage: python scripts/_apply_cleanup_stray_ve_lexical_on_deleted_records_20260701.py [--live]
"""
import sqlite3, sys, os, shutil
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')
LIVE = '--live' in sys.argv

TARGET = (
    "SELECT vl.id FROM ve_lexical vl "
    "JOIN verse_context vc ON vl.verse_context_id=vc.id "
    "JOIN wa_verse_records w ON vc.verse_record_id=w.id "
    "WHERE vl.delete_flagged=0 AND w.delete_flagged=1"
)

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    ids = [r['id'] for r in cur.execute(TARGET).fetchall()]
    # breakdown for the record
    brk = cur.execute(
        "SELECT vl.ve_label, vl.source_provenance, COUNT(*) n FROM ve_lexical vl "
        "JOIN verse_context vc ON vl.verse_context_id=vc.id "
        "JOIN wa_verse_records w ON vc.verse_record_id=w.id "
        "WHERE vl.delete_flagged=0 AND w.delete_flagged=1 "
        "GROUP BY vl.ve_label, vl.source_provenance"
    ).fetchall()
    print(f'Stray active ve_lexical rows on delete_flagged verse_records: {len(ids)}')
    for r in brk:
        print(f'  {r["ve_label"]} / {r["source_provenance"]}: {r["n"]}')

    if not LIVE:
        print('\nDRY-RUN. Re-run with --live to apply.')
        return

    os.makedirs('backups', exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    bak = os.path.join('backups', f'bible_research.pre-stray-lexical-cleanup.{stamp}.db')
    shutil.copy2(DB, bak)
    print(f'\nBackup: {bak}')

    cur.executemany('UPDATE ve_lexical SET delete_flagged=1 WHERE id=?', [(i,) for i in ids])
    conn.commit()

    remaining = cur.execute(f'SELECT COUNT(*) FROM ({TARGET})').fetchone()[0]
    print(f'Soft-deleted {len(ids)} rows.')
    print(f'Active ve_lexical still on delete_flagged verse_records: {remaining} (expected 0)')

if __name__ == '__main__':
    main()
