#!/usr/bin/env python
"""Ps 14 (the fool; universal corruption). IB ops: the fool's practical atheism
('no God' in the heart); the rare seeking-after-God that the LORD looks down for;
the evildoers' ignorance and prayerlessness; the anticipated gladness of
restoration. God's look-down/refuge = qualifier; the corruption-verdict + terror
= standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=14
r = Reading("Psa", 19, CH, note="The fool's 'no God' vs the sought-for seeker; evildoers' ignorance; restoration-joy")

r.ch(274506,"the fool says 'no God'","cognition","the fool","the fool says in his heart there is no God - a moral-practical denial that issues in corrupt deeds","practical-atheism","no-God-in-heart",IB,
     "v1: 'The FOOL says in his HEART, There is no God' - the operation is an interior verdict (not a philosophy) that clears the way for abominable deeds; denial as licence.")
r.ch(274526,"any who seek after God","volition","the seeker","the LORD looks down to see if any understand and seek after God - the rare interior that reaches for him","God-seeking","seek-after-God",IB,
     "v2: 'to see if there are any who UNDERSTAND, who SEEK after God' - the operation God searches the earth for is a mind that turns toward him; it is what makes a person not-a-fool.")
r.ch(274537,"evildoers who have no knowledge","cognition","the evildoers","the evildoers eat up God's people and do not call on the LORD - an ignorance that is also prayerlessness","ignorant-prayerlessness","no-knowledge-no-call",IB,
     "v4: 'Have they no KNOWLEDGE, all the evildoers who eat up my people... and do not CALL upon the LORD?' - the interior lack is twofold: they neither know nor pray; cruelty and God-forgetfulness are one.")
r.ch(274566,"gladness of restoration","affect","Jacob / Israel","when the LORD restores the fortunes of his people, Jacob rejoices and Israel is glad - joy longed for and anticipated","restoration-joy","rejoice-at-restoring",IB,
     "v7: 'when the LORD RESTORES the fortunes of his people, let Jacob REJOICE, let Israel be GLAD' - against the whole psalm's corruption, the interior reaches forward to a communal gladness when God acts.")

for sid,sense,src,d in [
 (274517,"the LORD looks down",274526,"v2: 'The LORD LOOKS DOWN from heaven on the children of man' - the divine search that seeks the seeker."),
 (274523,"to see",274526,"v2: 'to SEE if there are any who understand' - God's looking for the God-ward interior."),
 (274556,"the LORD is his refuge",274566,"v6: 'but the LORD is his REFUGE' - the shelter of the poor that grounds the hope of restoration."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (corruption-verdict 'none does good', terror-scene, or label); standalone.")
r.write()
