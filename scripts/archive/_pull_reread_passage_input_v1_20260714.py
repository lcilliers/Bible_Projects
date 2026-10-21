#!/usr/bin/env python
"""Leaner re-read passage-input pull (v1, 2026-07-14).

Replaces the verbose per-cycle input dump (which showed EVERY token incl. pure function
words) with a filtered view: full verse text for context + only the spans that matter for
reading — char_candidate=1 OR role IS NOT NULL (characteristic / qualifier / standalone).
Pure role=None function words (the/and/of ...) are dropped as noise. READ-ONLY.
(Proverbs retrospective R9 — cuts input tokens, same coverage.)

Usage:
  python scripts/_pull_reread_passage_input_v1_20260714.py --book 20 --passages 4157,4158
  python scripts/_pull_reread_passage_input_v1_20260714.py --book 20 --from 4157 --to 4168
  python scripts/_pull_reread_passage_input_v1_20260714.py --book 20 --after 4300 --limit 12   # next N passages after an id
  python scripts/_pull_reread_passage_input_v1_20260714.py --book 20 --all-tokens            # include function words
"""
import sqlite3, os, argparse, sys

DB = os.path.join('database', 'bible_research.db')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', required=True)
    ap.add_argument('--passages')
    ap.add_argument('--from', dest='pfrom', type=int)
    ap.add_argument('--to', dest='pto', type=int)
    ap.add_argument('--after', type=int, help='pull the next --limit passages with id > this')
    ap.add_argument('--limit', type=int, default=12)
    ap.add_argument('--all-tokens', action='store_true', help='include pure function-word (role=None, non-candidate) spans')
    a = ap.parse_args()

    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    bid = int(a.book) if str(a.book).isdigit() else c.execute(
        "SELECT id FROM books WHERE LOWER(name) LIKE ?", (f"%{str(a.book).lower()}%",)).fetchone()[0]

    if a.passages:
        pids = [int(x) for x in a.passages.split(',') if x.strip()]
        rows = c.execute(f"SELECT id, ref FROM passage WHERE book_id=? AND id IN ({','.join('?'*len(pids))}) ORDER BY id", [bid] + pids).fetchall()
    elif a.after is not None:
        rows = c.execute("SELECT id, ref FROM passage WHERE book_id=? AND id>? ORDER BY id LIMIT ?", (bid, a.after, a.limit)).fetchall()
    elif a.pfrom is not None and a.pto is not None:
        rows = c.execute("SELECT id, ref FROM passage WHERE book_id=? AND id BETWEEN ? AND ? ORDER BY id", (bid, a.pfrom, a.pto)).fetchall()
    else:
        sys.exit("give --passages, --from/--to, or --after")

    if not rows:
        print("(no passages)"); return
    print(f"passages: {rows[0]['id']}..{rows[-1]['id']} ({len(rows)})  [book_id={bid}]"
          + ("" if a.all_tokens else "  — meaningful spans only (function words hidden; --all-tokens to show)"))
    span_filter = "" if a.all_tokens else " AND (si.char_candidate=1 OR si.role IS NOT NULL)"
    for p in rows:
        print(f"\n--- P{p['id']} {p['ref']} ---")
        for v in c.execute("SELECT id vid, reference, verse_text FROM verse WHERE passage_id=? ORDER BY id", (p['id'],)):
            print(f"  {v['reference']}: {v['verse_text']}")
            allspans = c.execute(
                """SELECT id sid, surface, strongs, role, role_provenance, char_candidate cc, characteristic ch
                   FROM verse_span_index si WHERE verse_id=? ORDER BY id""", (v['vid'],)).fetchall()
            hidden = []
            for s in allspans:
                meaningful = a.all_tokens or s['cc'] == 1 or s['role'] is not None
                if meaningful:
                    print(f"     {s['sid']:>7} [{(s['strongs'] or '-'):>7}] {(s['surface'] or '')[:20]:<20} "
                          f"role={s['role']}/{s['role_provenance']} cand={s['cc']} char={s['ch']}")
                else:
                    hidden.append(f"{s['surface']}({s['sid']})")
            # nothing is invisible: role=None non-candidate spans are listed compactly (surface+id),
            # so an emergent content word is still seen and can be inspected on request.
            if hidden:
                print(f"     [role=None, non-candidate — {len(hidden)}]: " + ", ".join(hidden))
    c.close()

if __name__ == '__main__':
    main()
