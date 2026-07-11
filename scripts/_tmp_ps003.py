#!/usr/bin/env python
"""Ps 3 (morning psalm, many foes). IB ops: the soul taunted that there is no
help for it; crying aloud to God; lying down and sleeping in trust amid threat;
fearlessness before many thousands; the settled confession that salvation
belongs to the LORD. God's lifting/answering/striking = qualifier; shield/head/
teeth imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=3
r = Reading("Psa", 19, CH, note="Morning psalm amid many foes: the taunted soul, crying, trustful sleep, fearlessness, confession")

r.ch(278156,"soul told there is no help","state","the psalmist","the enemies assault the soul's hope, saying there is no salvation for it in God - the interior under siege of despair-talk","besieged-hope","no-help-for-soul",IB,
     "v2: 'many are saying of my SOUL, there is no SALVATION for him in God' - the sharpest attack is aimed at the interior: not the body but the soul's confidence is targeted.")
r.ch(278168,"cry aloud to the LORD","affect","the psalmist","against the taunt the self cries aloud, and is answered from the holy hill - the interior goes vocal upward","crying-out","cry-aloud",IB,
     "v4: 'I CRIED ALOUD to the LORD, and he answered me' - the operation is the lifted voice; the soul besieged with 'no help' answers by appealing to the only helper.")
r.ch(278177,"lie down and sleep in trust","state","the psalmist","the self lies down, sleeps, and wakes - the ability to sleep amid mortal threat is trust made bodily","trustful-rest","sleep-in-trust",IB,
     "v5: 'I LAY DOWN and SLEPT; I woke again, for the LORD sustained me' - the interior is so secure it can surrender consciousness among enemies; sleep as the proof of trust.")
r.ch(278184,"not afraid of many thousands","affect","the psalmist","the self declares it will not fear even ten thousands set against it - fear refused on the ground of God's sustaining","fearlessness","not-afraid",IB,
     "v6: 'I will not be AFRAID of many thousands of people' - the operation is deliberate fearlessness; the numbers that should terrify are faced down by trust.")
r.ch(278202,"salvation belongs to the LORD","cognition","the psalmist","the closing confession: salvation is the LORD's alone, his blessing on his people - the interior settles its theology of rescue","confession","salvation-is-God's",IB,
     "v8: 'SALVATION belongs to the LORD; your BLESSING be on your people' - against the taunt of v2 ('no salvation for him'), the interior lands on the opposite settled conviction.")

for sid,sense,src,d in [
 (278165,"lifter of my head",278168,"v3: 'my glory, and the LIFTER of my head' - God's act that answers the bowed, taunted self."),
 (278172,"answered me",278168,"v4: 'and he ANSWERED me from his holy hill' - the divine response to the cry."),
 (278181,"the LORD sustained me",278177,"v5: 'for the LORD SUSTAINED me' - the upholding that makes trustful sleep possible."),
 (278191,"Arise, O LORD",278184,"v7: 'ARISE, O LORD! Save me, O my God!' - the petition the fearless self still voices."),
 (278193,"Save me",278184,"v7: 'SAVE me' - the deliverance sought that grounds the fearlessness."),
 (278195,"strike the enemies",278184,"v7: 'you STRIKE all my enemies on the cheek' - God's past act steadying present courage."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (shield/glory/head/teeth imagery or label); standalone.")
r.write()
