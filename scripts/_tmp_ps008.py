#!/usr/bin/env python
"""Ps 8 (majesty + human dignity). Overwhelmingly God's majesty (name, heavens,
strength from infants) = standalone/qualifier. The human-IB core is the
meditation on the human creature: astonished that God is mindful of frail man;
the dignity of man crowned with glory and honour; the vocation of dominion."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=8
r = Reading("Psa", 19, CH, note="Majesty + human dignity; human portion = wonder at God's regard, the crowned dignity, the dominion-vocation")

r.ch(284919,"mindful of frail man","cognition","the psalmist","confronted with the vast heavens, the self marvels that God is mindful of and cares for so small a creature as man","humbled-wonder","why-mindful-of-man",IB,
     "v4: 'what is MAN that you are MINDFUL of him, and the son of man that you CARE for him?' - the interior weighs its own smallness against the star-filled sky and is astonished at being noticed at all.")
r.ch(284927,"crowned with glory and honour","state","mankind","the meditation on human dignity: man made a little lower than the heavenly beings and crowned with glory and honour - status reflected on","dignity","crowned-with-glory",IB,
     "v5: 'you have made him a little LOWER than the heavenly beings and CROWNED him with GLORY and honour' - the interior grasps a paradox: the frail creature of v4 is also a crowned one; smallness and dignity held together.")
r.ch(284931,"given dominion","state","mankind","the human vocation contemplated: man given dominion over the works of God's hands - responsibility as part of the dignity","vocation","given-dominion",IB,
     "v6: 'You have given him DOMINION over the works of your hands; you have put all things under his feet' - the interior reckons with a calling: the crowned creature is also a ruler, entrusted with the world.")

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (God's name/glory/heavens, strength-from-infants, foes-silenced imagery or label); standalone.")
r.write()
