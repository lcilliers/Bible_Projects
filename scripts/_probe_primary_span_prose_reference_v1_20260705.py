#!/usr/bin/env python
"""_probe_primary_span_prose_reference_v1_20260705.py — per book: primary spans + how many are
referenced (by transliteration) in the actual prose. Read-only, DB only.

'primary span'   = distinct ve_lexical.verse_span_id with gate='1-primary' (Gate 1 = tagged term).
'referenced'     = the span's lexicon transliteration (dots/hyphens stripped, whole-word) appears in
                   the body of a prose reading that covers the span's verse. This is a LOWER BOUND:
                   if the translit is present the span was cited by lexical identity; absence does not
                   prove non-reference (poetic prose often cites the English gloss/concept instead).
                   There is NO structural link between ve_lexical and prose_section; this text match is
                   the only available signal.

Prose readings used: type 104 (poetic chapter) + 108 (narrative passage), active, latest version;
verse->prose map built from each reading's metadata verse list.
"""
import sqlite3, os, re, json
from collections import defaultdict
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()

def norm(s): return re.sub(r'[^a-z]', '', (s or '').lower())

# 1. verse-ref -> list of normalised prose bodies covering it
ref2bodies=defaultdict(list)
for r in cur.execute("SELECT body, metadata_json FROM prose_section WHERE section_type_id IN (104,108) AND COALESCE(delete_flagged,0)=0 AND superseded_by_id IS NULL").fetchall():
    body_norm=re.sub(r'[.\-]', '', r['body'].lower())  # de-dot so 'a.hev' or 'ahev' both hit
    try: meta=json.loads(r['metadata_json']) if r['metadata_json'] else {}
    except Exception: meta={}
    refs=meta.get('verses') or meta.get('verse_refs') or []
    for ref in refs:
        ref2bodies[ref].append(body_norm)

# 2. primary spans per book, with translit + verse ref
rows=cur.execute("""
  SELECT b.name book, vl.verse_span_id sid, v.reference ref, lx.transliteration tl
  FROM ve_lexical vl
  JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id
  JOIN verse v ON v.id=vsi.verse_id
  JOIN books b ON b.id=v.book_id
  LEFT JOIN lexicon lx ON lx.strong=vsi.primary_strong
  WHERE COALESCE(vl.delete_flagged,0)=0 AND vl.gate='1-primary'
  GROUP BY vl.verse_span_id
""").fetchall()

per=defaultdict(lambda:[0,0,0])  # book -> [primary_spans, has_prose_for_verse, translit_in_prose]
for r in rows:
    book=r['book']; per[book][0]+=1
    bodies=ref2bodies.get(r['ref'], [])
    if bodies: per[book][1]+=1
    tl=norm(r['tl'])
    if tl and any(re.search(r'\b'+re.escape(tl)+r'\b', bd) for bd in bodies):
        per[book][2]+=1

print(f"{'Book':<16}{'primarySpans':>13}{'verseHasProse':>14}{'translitInProse':>16}{'%ref':>7}")
tp=tv=tr=0
for book in sorted(per, key=lambda b: cur.execute('SELECT id FROM books WHERE name=?',(b,)).fetchone()[0]):
    p,hv,tir=per[book]; tp+=p; tv+=hv; tr+=tir
    pct=100*tir/p if p else 0
    print(f"{book:<16}{p:>13}{hv:>14}{tir:>16}{pct:>6.1f}%")
print(f"{'TOTAL':<16}{tp:>13}{tv:>14}{tr:>16}{(100*tr/tp if tp else 0):>6.1f}%")
