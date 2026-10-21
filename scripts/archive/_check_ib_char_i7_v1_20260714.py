#!/usr/bin/env python
"""Cheap I7 check (v1, 2026-07-14) — read-2026 characteristics with NO ib_char link.

Per cadence v2 (Proverbs retrospective): the ib_characteristic Phase-1 rebuild is O(book)
and was run 60x (once/cycle). Instead, run THIS cheap check each cycle; only run the full
`_apply_rebuild_ib_char_meaning_keyed_v3 --book <id> --live` when it reports > 0 (and at
book-close / every ~5 cycles regardless). READ-ONLY. Exit 0 if I7=0, 1 if I7>0.

Usage:  python scripts/_check_ib_char_i7_v1_20260714.py --book 20
"""
import sqlite3, os, sys

DB = os.path.join('database', 'bible_research.db')

def main():
    if '--book' not in sys.argv:
        print("usage: --book <id|name>"); sys.exit(2)
    b = sys.argv[sys.argv.index('--book') + 1]
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    if str(b).isdigit():
        row = c.execute("SELECT id,name FROM books WHERE id=?", (int(b),)).fetchone()
    else:
        row = c.execute("SELECT id,name FROM books WHERE LOWER(name) LIKE ?", (f"%{str(b).lower()}%",)).fetchone()
    if not row:
        print(f"book not found: {b}"); sys.exit(2)
    bid, name = row['id'], row['name']
    n = c.execute("""SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                     WHERE v.book_id=? AND si.role='characteristic' AND si.role_provenance='read-2026'
                       AND si.ib_char_id IS NULL""", (bid,)).fetchone()[0]
    c.close()
    if n == 0:
        print(f"[I7 OK] {name}({bid}): 0 read-2026 chars unlinked — full rebuild NOT needed this cycle")
        sys.exit(0)
    print(f"[I7 >0] {name}({bid}): {n} read-2026 chars with NULL ib_char_id — run the full rebuild "
          f"(_apply_rebuild_ib_char_meaning_keyed_v3 --book {bid} --live)")
    sys.exit(1)

if __name__ == '__main__':
    main()
