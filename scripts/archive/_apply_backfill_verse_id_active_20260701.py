"""
_apply_backfill_verse_id_active_20260701.py

Backfill wa_verse_records.verse_id (FK -> verse.id, the master verse index) for the
ACTIVE rows (delete_flagged=0) where it is currently NULL.

Cause of the nulls: rows onboarded via the fanout path after the M60 verse_id backfill
(2026-06-16) — the onboarding path does not set verse_id. ~66 active rows, carrying the
ve_lexical for the recent fanout verses (Exo 1:13 perek, etc.).

Match key: (book_id, chapter, verse_num) against `verse`. Verified pre-run that this key
and the reference-text key agree with zero conflicts. Rows whose verse is not yet in the
`verse` master index are left NULL and reported (blocked on verse ingestion).

Safe: backs up the DB first; only touches active NULL rows; single transaction; verifies.
Usage: python scripts/_apply_backfill_verse_id_active_20260701.py [--live]
Default is DRY-RUN (reports, no write).
"""
import sqlite3, sys, os, shutil
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')
LIVE = '--live' in sys.argv

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # master verse index lookup
    by_bcv = {}
    for v in cur.execute('SELECT id, book_id, chapter, verse_num FROM verse').fetchall():
        by_bcv.setdefault((v['book_id'], v['chapter'], v['verse_num']), v['id'])

    rows = cur.execute(
        'SELECT id, reference, book_id, chapter, verse_num '
        'FROM wa_verse_records WHERE verse_id IS NULL AND delete_flagged=0'
    ).fetchall()

    updates, blocked = [], []
    for r in rows:
        vid = by_bcv.get((r['book_id'], r['chapter'], r['verse_num']))
        if vid is not None:
            updates.append((vid, r['id']))
        else:
            blocked.append(r['reference'])

    print(f'Active NULL verse_id rows: {len(rows)}')
    print(f'  -> matchable (will backfill): {len(updates)}')
    print(f'  -> blocked (verse not in master index): {len(blocked)} {sorted(set(blocked))}')

    if not LIVE:
        print('\nDRY-RUN. Re-run with --live to apply.')
        return

    # backup
    os.makedirs('backups', exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    bak = os.path.join('backups', f'bible_research.pre-verseid-backfill.{stamp}.db')
    shutil.copy2(DB, bak)
    print(f'\nBackup: {bak}')

    cur.executemany('UPDATE wa_verse_records SET verse_id=? WHERE id=?', updates)
    conn.commit()

    remaining = cur.execute(
        'SELECT COUNT(*) FROM wa_verse_records WHERE verse_id IS NULL AND delete_flagged=0'
    ).fetchone()[0]
    orphans = cur.execute(
        'SELECT COUNT(*) FROM wa_verse_records w WHERE w.verse_id IS NOT NULL '
        'AND NOT EXISTS (SELECT 1 FROM verse v WHERE v.id=w.verse_id)'
    ).fetchone()[0]
    print(f'Applied {len(updates)} updates.')
    print(f'Active NULL verse_id remaining: {remaining} (expected {len(blocked)} = the blocked verses)')
    print(f'FK orphans (verse_id with no verse row): {orphans} (expected 0)')

if __name__ == '__main__':
    main()
