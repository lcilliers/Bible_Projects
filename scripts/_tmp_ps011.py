#!/usr/bin/env python
"""Ps 11 (refuge vs the counsel to flee). Mostly the theology of God's testing
(qualifier) + the wicked's fiery portion (standalone). The two human-IB chars:
(1) the interior that takes refuge and refuses the advice to flee like a bird;
(2) the upright who shall behold God's face."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=11
r = Reading("Psa", 19, CH, note="Refuge vs flee-counsel; God tests (qual), the wicked's fiery portion (standalone); upright behold his face")

r.ch(272228,"take refuge, refuse to flee","affect","the psalmist","in the LORD the self takes refuge and rejects the counsel to flee like a bird - trust that holds its ground","standing-trust","refuse-to-flee",IB,
     "v1: 'In the LORD I TAKE REFUGE; how can you say to my SOUL, FLEE like a bird to your mountain?' - the operation is a trust that stays put; against the advisers' panic, the interior refuses flight and shelters in God.")
r.ch(272288,"the upright shall behold his face","affect","the upright","the LORD is righteous and loves righteous deeds; the upright shall behold his face - the reward of an upright interior is to see God","hope-of-seeing-God","behold-his-face",IB,
     "v7: 'the LORD is righteous... the UPRIGHT shall BEHOLD his face' - the interior of the upright is oriented to a final vision of God; uprightness ends not in reward-things but in seeing him.")

for sid,sense,src,d in [
 (272261,"his eyes test",272228,"v4: 'his eyes see, his EYELIDS TEST the children of man' - God's scrutiny from his holy temple that steadies the one who stays."),
 (272265,"tests the righteous",272288,"v5: 'The LORD TESTS the righteous' - the divine assaying the upright endure and are proven by."),
 (272268,"his soul hates violence",272288,"v5: 'his soul HATES the wicked and the one who loves violence' - God's own aversion that vindicates the upright."),
 (272271,"he loves righteous deeds",272288,"v7: 'he LOVES righteous deeds' - God's love that draws the upright toward beholding him."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (bow/arrow, foundations, coals/fire/sulphur portion imagery, or label); standalone.")
r.write()
