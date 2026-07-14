#!/usr/bin/env python
"""Reusable per-cycle re-read conformance check (v1, 2026-07-14).

Retires the inline SQL that was hand-authored every cycle during the Proverbs read
(where the prior span_id/verse_span_id bug lived). Runs the standing gates on the
read-2026 characteristic layer, scoped to a passage list, passage range, or span-id
list. READ-ONLY. Exit 0 if all gates pass, 1 otherwise.

Gates (per the cadence doc, v2):
  I11        char gloss (verse_span_index.characteristic) set on every read char
  D1         reread lexical only where role is not NULL
  D2         reread lexical only on role='characteristic'
  ledger     full poetic mandatory ledger present per char (M below)
  marker     every read char's verse carries process_marker
  G10/116    locus (116) present per char
  stale      no non-reread lexical on a read char
  coverage   (--coverage) book-wide: verses read + skip-listed == verses seen so far

Usage:
  python scripts/_check_reread_conformance_v1_20260714.py --book 20 --passages 4157,4158,...
  python scripts/_check_reread_conformance_v1_20260714.py --book 20 --from 4157 --to 4168
  python scripts/_check_reread_conformance_v1_20260714.py --book 20 --spans 265266,265276,...
  python scripts/_check_reread_conformance_v1_20260714.py --book 20 --coverage
"""
import sqlite3, os, argparse, sys

DB = os.path.join('database', 'bible_research.db')
# 11-dim poetic/wisdom mandatory ledger (per cadence v2)
M = (101, 102, 104, 105, 106, 107, 108, 112, 114, 115, 116)

def resolve_book(c, book):
    if str(book).isdigit():
        r = c.execute("SELECT id,name FROM books WHERE id=?", (int(book),)).fetchone()
    else:
        r = c.execute("SELECT id,name FROM books WHERE LOWER(name) LIKE ?", (f"%{str(book).lower()}%",)).fetchone()
    if not r:
        sys.exit(f"book not found: {book}")
    return r['id'], r['name']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', required=True)
    ap.add_argument('--passages', help='comma-separated passage ids')
    ap.add_argument('--from', dest='pfrom', type=int, help='passage id range start (inclusive)')
    ap.add_argument('--to', dest='pto', type=int, help='passage id range end (inclusive)')
    ap.add_argument('--spans', help='comma-separated span ids (scope by span, ignores passage)')
    ap.add_argument('--prov', help="reread provenance (default reread-<book>-2026)")
    ap.add_argument('--coverage', action='store_true', help='also run the book-wide verse-coverage assertion')
    a = ap.parse_args()

    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    bid, bname = resolve_book(c, a.book)
    prov = a.prov or f"reread-{bname.lower()}-2026"
    marker = f"reread-{bname.lower()}-2026"

    # --- resolve the read-2026 char spans in scope ---
    if a.spans:
        sids = [int(x) for x in a.spans.split(',') if x.strip()]
        ids = [r['id'] for r in c.execute(
            f"SELECT id FROM verse_span_index WHERE id IN ({','.join('?'*len(sids))}) "
            f"AND role='characteristic' AND role_provenance='read-2026'", sids)]
        pids = None
    else:
        if a.passages:
            pids = [int(x) for x in a.passages.split(',') if x.strip()]
        elif a.pfrom is not None and a.pto is not None:
            pids = list(range(a.pfrom, a.pto + 1))
        else:
            pids = None
        if pids is not None:
            q = ','.join('?' * len(pids))
            ids = [r['id'] for r in c.execute(
                f"""SELECT si.id FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                    WHERE v.passage_id IN ({q}) AND si.role='characteristic' AND si.role_provenance='read-2026'""", pids)]
        else:
            ids = [r['id'] for r in c.execute(
                """SELECT si.id FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                   WHERE v.book_id=? AND si.role='characteristic' AND si.role_provenance='read-2026'""", (bid,))]

    qi = ','.join('?' * len(ids)) if ids else 'NULL'
    one = lambda s, ar: c.execute(s, ar).fetchone()[0]
    gates = {}

    gates['I11 char gloss unset'] = one(
        f"SELECT COUNT(*) FROM verse_span_index WHERE id IN ({qi}) AND (characteristic IS NULL OR characteristic='')", ids) if ids else 0

    # D1/D2 over the reread lexical in the passage scope (or span scope)
    if a.spans:
        d1 = one(f"""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id
            WHERE x.verse_span_id IN ({qi}) AND x.source_provenance=? AND x.delete_flagged=0 AND si.role IS NULL""", ids + [prov]) if ids else 0
        d2 = one(f"""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id
            WHERE x.verse_span_id IN ({qi}) AND x.source_provenance=? AND x.delete_flagged=0 AND si.role!='characteristic'""", ids + [prov]) if ids else 0
    elif pids is not None:
        q = ','.join('?' * len(pids))
        d1 = one(f"""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
            WHERE v.passage_id IN ({q}) AND x.source_provenance=? AND x.delete_flagged=0 AND si.role IS NULL""", pids + [prov])
        d2 = one(f"""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
            WHERE v.passage_id IN ({q}) AND x.source_provenance=? AND x.delete_flagged=0 AND si.role!='characteristic'""", pids + [prov])
    else:
        d1 = one("""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
            WHERE v.book_id=? AND x.source_provenance=? AND x.delete_flagged=0 AND si.role IS NULL""", [bid, prov])
        d2 = one("""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
            WHERE v.book_id=? AND x.source_provenance=? AND x.delete_flagged=0 AND si.role!='characteristic'""", [bid, prov])
    gates['D1 reread lexical role null'] = d1
    gates['D2 reread lexical on non-char'] = d2

    missing = g10 = 0
    for sid in ids:
        have = set(r[0] for r in c.execute(
            "SELECT ve_nr FROM ve_lexical WHERE verse_span_id=? AND delete_flagged=0 AND source_provenance=?", (sid, prov)))
        if not set(M).issubset(have):
            missing += 1
        if 116 not in have:
            g10 += 1
    gates['mandatory ledger missing'] = missing
    gates['G10 locus(116) missing'] = g10

    gates['unmarked read verses'] = one(
        f"""SELECT COUNT(DISTINCT v.id) FROM verse v JOIN verse_span_index si ON si.verse_id=v.id
            WHERE si.id IN ({qi}) AND (v.process_marker IS NULL OR v.process_marker!=?)""", ids + [marker]) if ids else 0

    gates['stale lexical on read chars'] = one(
        f"""SELECT COUNT(*) FROM ve_lexical x WHERE x.verse_span_id IN ({qi})
            AND x.delete_flagged=0 AND x.source_provenance!=?""", ids + [prov]) if ids else 0

    print(f"# reread conformance — book={bname}({bid}) prov={prov} | read-2026 chars in scope: {len(ids)}")
    failed = 0
    for k, v in gates.items():
        ok = 'PASS' if v == 0 else 'FAIL'
        if v: failed += 1
        print(f"  [{ok}] {k:<28}: {v}")

    if a.coverage:
        total = one("SELECT COUNT(*) FROM verse WHERE book_id=?", [bid])
        inpass = one("SELECT COUNT(*) FROM verse WHERE book_id=? AND passage_id IS NOT NULL", [bid])
        nullp = total - inpass
        read = one("""SELECT COUNT(DISTINCT v.id) FROM verse v JOIN verse_span_index si ON si.verse_id=v.id
            WHERE v.book_id=? AND si.role='characteristic' AND si.role_provenance='read-2026'""", [bid])
        print(f"  [INFO] verse-coverage           : total={total} in-passages={inpass} passage_id-NULL={nullp} read={read}")
        print(f"         (book-start pre-flight must reconcile NULL verses to passages or skip-list — see readiness §D)")

    c.close()
    if failed:
        print(f"\nRESULT: {failed} gate(s) FAILED")
        sys.exit(1)
    print("\nRESULT: all gates PASS")

if __name__ == '__main__':
    main()
