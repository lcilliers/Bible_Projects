#!/usr/bin/env python
"""Ps 150 - the final doxology, pure praise. Thirteen 'praise' calls + instruments.
The instruments are the medium (standalone); the genuine IB movement is anchored
in three praise-operations: (1) praise God for himself (sanctuary/mighty heavens);
(2) praise proportioned to his mighty deeds and excellent greatness; (3) the
universal summons - every breathing thing praises. Movement-anchored to avoid
flattened reuse of the repeated 'praise'."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=150
r = Reading("Psa", 19, CH, note="Final doxology: praise-for-himself, praise-for-his-deeds, universal breath-praise (instruments = standalone)")

r.ch(274569,"praise God for himself","affect","the worshippers","praise directed to God in his sanctuary and mighty heavens - praise for who and where he is","adoration","praise-in-sanctuary",IB,
     "v1: 'PRAISE God in his sanctuary; praise him in his mighty heavens!' - the first movement praises God for his own holy presence and majesty, before any reason is given.")
r.ch(274578,"praise for his mighty deeds","affect","the worshippers","praise proportioned to God's mighty deeds and excellent greatness - praise measured to what he has done","proportioned-praise","praise-his-deeds",IB,
     "v2: 'PRAISE him for his MIGHTY DEEDS; praise him according to his EXCELLENT greatness!' - the second movement grounds praise in God's acts and grandeur; the measure of praise is the measure of his greatness.")
r.ch(274602,"every breath praises","affect","all that breathes","the universal summons: everything that has breath is called to praise - praise as the proper act of every living thing","universal-doxology","let-all-breath-praise",IB,
     "v6: 'Let everything that has BREATH PRAISE the LORD!' - the Psalter's closing note widens praise to the limit: to breathe is to owe praise; the final movement leaves no living thing outside the doxology.")

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (instrument/venue medium: trumpet/harp/lute/tambourine/strings/pipe/cymbals/sanctuary/heavens, or a medium-repetition of the praise-call); standalone.")
r.write()
