#!/usr/bin/env python
"""Ps 144 (David, war-song + national prayer). IB ops: blessing God the rock who
trains for war; wondering that God regards frail man; contemplating human
transience (like breath, a passing shadow); the enemies' deceitful mouths (v8,
v11 distinct); singing a new song; the twofold beatitude of the people whose God
is the LORD. Theophany + prosperity + weapon imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=144
r = Reading("Psa", 19, CH, note="War-song + national prayer: blessing the rock, human frailty, deceitful foes, beatitude")

r.ch(273946,"bless God the rock","affect","the psalmist","the self blesses God as its rock, refuge and the trainer of its hands for battle","doxology","bless-the-rock",IB,
     "v1: 'BLESSED be the LORD, my rock, who trains my hands for war' - the interior opens by ascribing all martial strength to God, not the self.")
r.ch(273998,"wonder that God regards man","cognition","the psalmist","the self marvels that God takes knowledge of so small a creature as man","humbled-wonder","why-regard-man",IB,
     "v3: 'O LORD, what is man that you REGARD him?' - the operation is astonished self-assessment: the interior weighs its own smallness against God's attention.")
r.ch(308122,"man like a breath","cognition","the psalmist","the self reckons human life as breath, its days a fleeting shadow - transience owned","transience-reckoning","like-breath",IB,
     "v4: 'man is like a BREATH; his days are like a passing shadow' - the interior faces its own evanescence, the ground of the humbled wonder.")
r.ch(274017,"enemies speak lies (v8)","cognition","the foreigners","the alien foes' mouths speak falsehood, the right hand a right hand of lies","deceit","mouth-of-lies-v8",IB,
     "v8: 'whose MOUTHS speak LIES and whose right hand is a right hand of falsehood' - the enemy's interior is deceit; the outer hand is perjured.")
r.ch(273961,"enemies speak lies (v11)","cognition","the foreigners","the same deceit named again in the renewed plea - the settled falseness of the foe","deceit","mouth-of-lies-v11",IB,
     "v11: 'whose MOUTHS speak LIES...' - read distinct from v8: the repetition in the second petition marks the deceit as the persisting reason for the cry.")
r.ch(274022,"sing a new song","affect","the psalmist","the self resolves to sing a new song on the ten-stringed harp to God the giver of victory","fresh-praise","sing-new-song",IB,
     "v9: 'I will SING a new song to you, O God' - the interior turns from plea to fresh praise, anticipating the deliverance it asks.")
r.ch(308149,"blessed - such blessings (v15a)","affect","the people","the people are pronounced blessed on whom such prosperity falls - felt well-being","beatitude","blessed-blessings",IB,
     "v15a: 'BLESSED are the people to whom such blessings fall' - the first beatitude weighs the happiness of a flourishing people.")
r.ch(308152,"blessed - whose God is the LORD (v15b)","affect","the people","the deeper beatitude: blessed the people whose God is the LORD - the true ground of joy","beatitude","blessed-whose-God",IB,
     "v15b: 'BLESSED are the people whose God is the LORD' - read distinct from v15a: the interior corrects prosperity-happiness with covenant-happiness; the relation, not the granaries, is the real blessing.")

for sid,sense,src,d in [
 (273949,"trains hands for war",273946,"v1: God 'TRAINS my hands for war' - the martial skill ascribed to God."),
 (273984,"steadfast love (chesed)",273946,"v2: 'my STEADFAST LOVE and my fortress' - God's covenant loyalty named as the rock."),
 (273987,"stronghold (misgab)",273946,"v2: 'my STRONGHOLD and my deliverer' - God as fortress."),
 (273988,"deliverer (palat)",273946,"v2: 'my DELIVERER, my shield' - God as rescuer."),
 (273991,"subdues peoples",273946,"v2: 'who SUBDUES peoples under me' - God's act behind the king's victories."),
 (274001,"think of him (chashab)",273998,"v3: 'that you THINK of him' - the divine notice that astonishes."),
 (274003,"Stretch out rescue",274022,"v7: 'STRETCH OUT your hand from on high; rescue me' - the deliverance the new song anticipates."),
 (274007,"rescue (patsah)",274022,"v7: 'RESCUE me from the many waters' - the petition."),
 (274008,"deliver (natsal)",274022,"v7: 'DELIVER me from the hand of foreigners' - the petition."),
 (305890,"gives victory",274022,"v10: 'who GIVES VICTORY to kings' - God's saving act the song celebrates."),
 (305893,"rescues David",274022,"v10: 'who RESCUES David his servant' - the deliverance in view."),
 (273954,"Rescue (patsah)",273961,"v11: 'RESCUE me and deliver me from the hand of foreigners' - petition against the lying foes."),
 (273955,"deliver (natsal)",273961,"v11: 'DELIVER me' - the renewed rescue plea."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (theophany/prosperity/weapon imagery or label); standalone.")
r.write()
