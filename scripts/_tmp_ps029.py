#!/usr/bin/env python
"""Ps 29 (the voice of the LORD - thunderstorm theophany). The seven-fold 'voice
of the LORD' over the waters (vv3-9) = standalone theophany. The human-IB portion
is small and honest: the summons to ascribe glory and worship in holiness; the
temple-cry 'Glory!'."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=29
r = Reading("Psa", 19, CH, note="Thunderstorm theophany (voice-of-the-LORD = standalone); human portion = ascribe-glory/worship + the temple-cry 'Glory!'")

r.ch(276413,"ascribe glory, worship in holiness","affect","the heavenly beings / worshippers","the summons to ascribe to the LORD glory and strength and to worship him in the splendour of holiness - the interior called to render God his due","ascription","ascribe-glory",IB,
     "v1-2: 'ASCRIBE to the LORD glory and strength; ascribe to the LORD the glory due his name; WORSHIP the LORD in the splendour of holiness' - the operation is the giving-back of glory: the interior is summoned to acknowledge God's weight and bow.")
r.ch(276489,"in his temple all cry 'Glory!'","affect","the worshippers","while the voice of the LORD shakes creation, in his temple all cry 'Glory!' - the worshippers' spontaneous exclamation","exclamation","cry-glory",IB,
     "v9: 'and in his temple all cry, GLORY!' - the operation is the involuntary response of the interior to the theophany: awe forced up into a single word of praise.")

for sid,sense,src,d in [
 (276432,"bless his people with peace",276413,"v11: 'May the LORD give strength to his people! May the LORD BLESS his people with PEACE!' - the benediction the ascription closes on."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (voice-of-the-LORD theophany: thunders/breaks-cedars/flashes/shakes-wilderness, or glory/name label); standalone.")
r.write()
