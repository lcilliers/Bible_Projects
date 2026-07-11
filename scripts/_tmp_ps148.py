#!/usr/bin/env python
"""Ps 148 - cosmic praise: all creation summoned. This psalm is overwhelmingly
the personified cosmos praising (sun, moon, stars, angels, sea creatures,
weather, mountains, trees, beasts) = standalone substrate. The genuine human-IB
chars are small and honest: (1) humans of every rank praising the exalted name;
(2) the saints/people near to God praising, the horn raised for them."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=148
r = Reading("Psa", 19, CH, note="Cosmic praise; human portion = every rank + the saints praising (rest = personified creation, standalone)")

r.ch(274394,"every human rank praises","affect","humankind","kings, peoples, princes, young and old, men and maidens - the whole human range summoned to praise the one exalted name","universal-human-praise","all-ranks-praise",IB,
     "v11-13: 'Kings... peoples... young men and maidens... Let them PRAISE the name of the LORD, for his name alone is exalted' - across every rank and age the human interior is called to the same act; the levelling of all persons before the one name.")
r.ch(274408,"the saints praise (horn raised)","affect","the saints","the people near to God praise him - he has raised a horn for his saints, the people close to his heart","near-praise","saints-horn-praise",IB,
     "v14: 'He has raised up a HORN for his people, PRAISE for all his SAINTS, for the people of Israel who are NEAR to him' - the psalm narrows from the cosmos to the covenant people whose nearness makes their praise intimate, not merely dutiful.")

for sid,sense,src,d in [
 (274442,"commanded and created",274394,"v5: 'For he COMMANDED and they were CREATED' - the creative act the ranks praise."),
 (274443,"created (bara)",274394,"v5: 'they were CREATED' - the ground of the summoned praise."),
 (274405,"raised up a horn",274408,"v14: 'He has RAISED UP a horn for his people' - God's exalting act the saints praise."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (personified creation: angels/sun/moon/stars/sea-creatures/weather/mountains/trees/beasts, or rank-label); standalone.")
r.write()
