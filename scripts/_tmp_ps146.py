#!/usr/bin/env python
"""Ps 146 (Hallel) - 'Praise the LORD, O my soul.' IB ops: the soul summoned to
praise; lifelong praise resolve; redirecting trust away from princes; the
meditation on human mortality (breath departs, plans perish); the beatitude of
hope in God. God's acts (justice/food/free/sight/lift) = qual; the labels and
'reign forever' = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=146
r = Reading("Psa", 19, CH, note="Praise the LORD O my soul: self-summons, trust redirected from princes, hope-beatitude")

r.ch(274191,"soul summoned to praise","affect","the psalmist","the self commands its own soul to praise - the interior turned on itself as summons","self-summons","praise-O-my-soul",IB,
     "v1: 'PRAISE the LORD, O my SOUL' - the operation is reflexive: the will rouses the soul, praise begun by self-address.")
r.ch(274201,"praise while I live","affect","the psalmist","the self vows to praise and sing as long as it lives and has being - praise coextensive with life","lifelong-vow","praise-all-my-life",IB,
     "v2: 'I will PRAISE the LORD as long as I live; I will SING praises to my God while I have being' - the interior stretches praise across the whole span of existence.")
r.ch(274210,"redirect trust from princes","volition","the psalmist","the self is warned off trusting princes and mortal man, redirecting reliance to God","trust-redirection","trust-not-princes",IB,
     "v3: 'Put not your TRUST in princes, in a son of man, in whom there is no salvation' - the operation is the deliberate withdrawal of reliance from mortal power.")
r.ch(274224,"plans perish at death","cognition","mortal man","reckoning that when breath departs, man returns to earth and on that day his plans perish","mortality-reckoning","plans-perish",IB,
     "v4: 'his breath departs, he returns to the earth; on that day his PLANS PERISH' - the interior grasps why princes cannot be trusted: their very designs die with them.")
r.ch(274230,"hope in the God of Jacob","affect","the blessed","the beatitude: blessed is he whose help and hope is in the God of Jacob - hope rightly placed","rightly-placed-hope","hope-in-God",IB,
     "v5: 'BLESSED is he whose help is the God of Jacob, whose HOPE is in the LORD his God' - against perishing plans, the interior fastens hope on the maker who keeps faith forever.")

for sid,sense,src,d in [
 (274205,"sing praises (zamar)",274201,"v2: 'I will SING praises to my God' - the musical form of the lifelong vow."),
 (274216,"no salvation in man",274210,"v3: 'in whom there is no SALVATION' - the reason trust is withdrawn from princes."),
 (274233,"made heaven and earth",274230,"v6: 'who MADE heaven and earth' - the maker the hope rests on."),
 (274238,"keeps faith forever",274230,"v6: 'who KEEPS faith forever' - the reliability grounding hope, over against perishing plans."),
 (274241,"executes justice",274230,"v7: 'who EXECUTES justice for the oppressed' - God's act the hope trusts."),
 (274244,"gives food to hungry",274230,"v7: 'who GIVES food to the hungry' - God's provision."),
 (274249,"sets prisoners free",274230,"v7: 'the LORD sets prisoners FREE' - God's liberating act."),
 (274251,"opens the blind",274230,"v8: 'the LORD OPENS the eyes of the blind' - God's restoring act."),
 (274254,"lifts the bowed down",274230,"v8: 'the LORD LIFTS UP those who are bowed down' - God's raising act."),
 (274257,"loves the righteous",274230,"v8: 'the LORD LOVES the righteous' - God's disposition the hope leans on."),
 (274260,"watches sojourners",274230,"v9: 'the LORD WATCHES over the sojourners' - God's care for the vulnerable."),
 (274262,"upholds widow and fatherless",274230,"v9: 'he UPHOLDS the widow and the fatherless' - God's sustaining."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (label: oppressed/hungry/prisoners/blind/widow; or 'reign forever'); standalone.")
r.write()
