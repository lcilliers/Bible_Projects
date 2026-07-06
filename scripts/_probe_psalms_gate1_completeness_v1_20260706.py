#!/usr/bin/env python
"""_probe_psalms_gate1_completeness_v1_20260706.py — Step (d) diagnostic (read-only).

For every CHARACTERISTIC span in Psalms (ve_nr=115, value='characteristic', role-reassess-2026),
check Gate-1 completeness of the chain:
  (1) the term (base strong) is recorded in mti_terms
  (2) the verse occurrence is present in wa_verse_records (verse_id + term_id)
  (3) links intact (that verse-record carries verse_span_id + mti_term_id)
Reports the gap only; writes nothing.
"""
import sqlite3, os, re
from collections import defaultdict
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
def base(s): m=re.match(r'(H\d+)', s or ''); return m.group(1) if m else (s or '')
pb=cur.execute("SELECT id FROM books WHERE name='Psalms'").fetchone()['id']

# characteristic spans (verse, span, strong)
spans=cur.execute("""SELECT vsi.id sid, vsi.verse_id vid, v.chapter ch, v.verse_num vn,
    substr(vsi.primary_strong,1,5) s, vsi.surface
  FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
  WHERE v.book_id=? AND vl.ve_nr=115 AND vl.value='characteristic' AND vl.source_provenance='role-reassess-2026'
    AND COALESCE(vl.delete_flagged,0)=0""",(pb,)).fetchall()
print(f"Characteristic spans in Psalms: {len(spans)}")
char_strongs=set(base(sp['s']) for sp in spans)
print(f"Distinct characteristic strongs: {len(char_strongs)}")

# (1) mti_terms membership (strong may be zero-padded 4-digit in mti; normalise both)
def norm(s):  # H0157 -> H157 base compare set of forms
    b=base(s); return b
mti=set()
for r in cur.execute("SELECT DISTINCT strongs_number AS strongs FROM mti_terms WHERE COALESCE(status,'') NOT IN ('delete','excluded','candidate_delete')"):
    if r['strongs']:
        for part in re.split(r'[,\s;]+', r['strongs']):
            if part.strip(): mti.add(base(part.strip()))
# also try zero-pad variants
def in_mti(strong):
    b=base(strong)
    if b in mti: return True
    # try without leading zeros e.g. H0157 -> H157
    m=re.match(r'H0*(\d+)', b)
    if m and ('H'+m.group(1)) in mti: return True
    # try zero-padded 4
    m=re.match(r'H(\d+)', b)
    if m and ('H'+m.group(1).zfill(4)) in mti: return True
    return False
missing_terms=sorted(s for s in char_strongs if not in_mti(s))
print(f"\n(1) characteristic strongs NOT in mti_terms: {len(missing_terms)}")
if missing_terms: print("   ", missing_terms[:40])

# (2) verse-record presence: for each char span, is there a wa_verse_records row for (verse_id, this strong)?
# build wavr lookup keyed (verse_id, base strong)
wavr=defaultdict(list)
for r in cur.execute("SELECT id, verse_id, term_id, verse_span_id, mti_term_id FROM wa_verse_records WHERE book_id=? AND COALESCE(delete_flagged,0)=0",(pb,)):
    wavr[(r['verse_id'], base(r['term_id']))].append(r)
present=absent=0; absent_by_strong=defaultdict(int); link_missing=0
for sp in spans:
    key=(sp['vid'], base(sp['s'])); recs=wavr.get(key,[])
    if recs:
        present+=1
        if not any(r['verse_span_id'] and r['mti_term_id'] for r in recs): link_missing+=1
    else:
        absent+=1; absent_by_strong[base(sp['s'])]+=1
print(f"\n(2) characteristic spans WITH a verse-record: {present}")
print(f"    characteristic spans WITHOUT a verse-record (Gate-1 gap): {absent}")
print(f"(3) present but missing verse_span_id/mti_term_id link: {link_missing}")
print(f"\nDistinct strongs with any missing verse-record: {len(absent_by_strong)}")
top=sorted(absent_by_strong.items(), key=lambda x:-x[1])[:25]
# add gloss
for s,n in top:
    g=cur.execute("SELECT gloss FROM lexicon WHERE strong LIKE ? LIMIT 1",(s+'%',)).fetchone()
    print(f"    {s} x{n}  {(g['gloss'] if g else '')[:30]}")
