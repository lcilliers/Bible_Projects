#!/usr/bin/env python
"""_probe_ve_lexical_per_book_census_v1_20260705.py — per-book ve_lexical extraction (read-only, DB only).

Per book, keyed span->verse->book via verse_span_index:
  records      = active ve_lexical rows
  spans        = distinct verse_span_id coded
  verses       = distinct verses touched
  passages     = distinct passage_id touched
  dims         = distinct dimensions (ve_nr) used in the book
  rec/span     = records per coded span
  dim/verse    = avg distinct dimensions per coded verse
  dim/passage  = avg distinct dimensions per coded passage
"""
import sqlite3, os
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()

# aggregate per book (span-keyed)
agg=cur.execute("""
  SELECT b.id bid, b.name,
    COUNT(*) records,
    COUNT(DISTINCT vl.verse_span_id) spans,
    COUNT(DISTINCT v.id) verses,
    COUNT(DISTINCT v.passage_id) passages,
    COUNT(DISTINCT vl.ve_nr) dims
  FROM ve_lexical vl
  JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id
  JOIN verse v ON v.id=vsi.verse_id
  JOIN books b ON b.id=v.book_id
  WHERE COALESCE(vl.delete_flagged,0)=0
  GROUP BY b.id ORDER BY b.id
""").fetchall()

# avg distinct dims per verse, per book
dpv={r['bid']: (r['s']/r['n'] if r['n'] else 0) for r in cur.execute("""
  SELECT bid, AVG(d) s, COUNT(*) n FROM (
    SELECT v.book_id bid, v.id vid, COUNT(DISTINCT vl.ve_nr) d
    FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
    WHERE COALESCE(vl.delete_flagged,0)=0 GROUP BY v.id
  ) GROUP BY bid
""").fetchall() for _ in [0]} if False else {}
rows=cur.execute("""
    SELECT v.book_id bid, COUNT(DISTINCT vl.ve_nr) d
    FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
    WHERE COALESCE(vl.delete_flagged,0)=0 GROUP BY v.id
""").fetchall()
from collections import defaultdict
sv=defaultdict(list)
for r in rows: sv[r['bid']].append(r['d'])
# per passage
rows2=cur.execute("""
    SELECT v.book_id bid, COUNT(DISTINCT vl.ve_nr) d
    FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
    WHERE COALESCE(vl.delete_flagged,0)=0 AND v.passage_id IS NOT NULL GROUP BY v.passage_id
""").fetchall()
sp=defaultdict(list)
for r in rows2: sp[r['bid']].append(r['d'])

print(f"{'Book':<16}{'records':>9}{'spans':>8}{'verses':>7}{'passages':>9}{'dims':>5}{'rec/span':>9}{'dim/vs':>7}{'dim/psg':>8}")
tr=ts=tv=0
for a in agg:
    dv=sum(sv[a['bid']])/len(sv[a['bid']]) if sv[a['bid']] else 0
    dp=sum(sp[a['bid']])/len(sp[a['bid']]) if sp[a['bid']] else 0
    rps=a['records']/a['spans'] if a['spans'] else 0
    tr+=a['records']; ts+=a['spans']; tv+=a['verses']
    print(f"{a['name']:<16}{a['records']:>9}{a['spans']:>8}{a['verses']:>7}{a['passages']:>9}{a['dims']:>5}{rps:>9.2f}{dv:>7.1f}{dp:>8.1f}")
print(f"{'TOTAL':<16}{tr:>9}{ts:>8}{tv:>7}")
