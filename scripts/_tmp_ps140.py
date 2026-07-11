#!/usr/bin/env python
"""Ps 140 (David) - deliverance from violent, scheming men. IB ops: the wicked's
heart-scheming + specific ambush + arrogant trap-laying + craving for triumph;
the psalmist's crying pleas + assurance that God maintains the afflicted's cause
+ the righteous' thanksgiving. God's deliver/preserve/grant-not = qual; the
weapon/trap/serpent/coal imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=140
r = Reading("Psa", 19, CH, note="Deliverance from violent men; the wicked's schemes vs the psalmist's plea and assurance")

r.ch(273608,"plan evil in the heart","cognition","the wicked","the wicked devise evils inwardly, the heart as a workshop of harm","heart-scheming","devise-evil",IB,
     "v2: they 'PLAN evil things in their HEART' - the interior is where the violence is first manufactured, before it stirs up wars.")
r.ch(273632,"planned to trip the feet","cognition","the wicked","a specific ambush is premeditated - to trip the walking feet, a targeted trap","targeted plot","plan-the-ambush",IB,
     "v4: 'who have PLANNED to trip up my feet' - distinct from the general malice of v2: a concrete, aimed snare, deliberation narrowed to one victim.")
r.ch(273636,"arrogant lay a trap","disposition","the arrogant","pride expresses itself as covert trap-setting - the haughty spread nets in secret","proud entrapment","hidden-snare",IB,
     "v5: 'the ARROGANT have hidden a trap for me' - the operation is pride turned to concealment; self-exaltation works by ambush, not open force.")
r.ch(273666,"desires of the wicked","volition","the wicked","the wicked crave the granting of their designs, an appetite for triumph over the righteous","craving-triumph","desire-to-prevail",IB,
     "v8: 'Grant not, O LORD, the DESIRES of the wicked' - their inner appetite is to see their plot furthered and themselves exalted.")
r.ch(273653,"pleas for mercy voiced","affect","the psalmist","the psalmist lifts a crying voice of supplication, the cry as the counter-move to the schemes","crying-out","voice-pleas",IB,
     "v6: 'give ear to the voice of my PLEAS for mercy' - against the silent scheming, the psalmist's interior goes vocal, appealing upward.")
r.ch(273591,"know the LORD maintains","cognition","the psalmist","settled assurance that God will uphold the afflicted's cause - knowledge that steadies","confident-assurance","know-God-maintains",IB,
     "v12: 'I KNOW that the LORD will maintain the cause of the afflicted' - the interior resolves from plea into confidence; the outcome is already owned.")
r.ch(273601,"give thanks (upright)","affect","the upright","the righteous respond to vindication with thanksgiving and dwelling in God's presence","grateful-response","thank-and-dwell",IB,
     "v13: 'the righteous shall GIVE THANKS to your name' - the arc closes in gratitude; the interior moves from threat through assurance to thanks.")

for sid,sense,src,d in [
 (273581,"Deliver (chalats)",273653,"v1: 'DELIVER me from evil men' - God-act petitioned against the violent."),
 (273586,"preserve (natsar)",273653,"v1: 'PRESERVE me from violent men' - the guarding petition."),
 (273622,"Guard (shamar)",273653,"v4: 'GUARD me from the hands of the wicked' - protective petition."),
 (273627,"preserve (natsar)",273653,"v4: 'PRESERVE me from violent men' - repeated guarding petition."),
 (273650,"give ear (azan)",273653,"v6: 'GIVE EAR to the voice of my pleas' - the divine hearing sought."),
 (273657,"strength of salvation",273653,"v7: 'the STRENGTH of my salvation' - God as the might behind rescue."),
 (273658,"salvation (yeshuah)",273653,"v7: God's SALVATION - the deliverance appealed to."),
 (273659,"covered head in battle",273653,"v7: 'you have COVERED my head in the day of battle' - God's protecting act."),
 (273594,"maintain (asah)",273591,"v12: God will MAINTAIN the cause - the act the assurance rests on."),
 (273595,"cause (din)",273591,"v12: the CAUSE of the afflicted God upholds."),
 (273597,"justice (mishpat)",273591,"v12: God secures JUSTICE for the needy - the assured outcome."),
 (273663,"Grant not (natan)",273666,"v8: 'GRANT not the desires of the wicked' - petition that God withhold their appetite."),
 (273669,"further not (puq)",273666,"v8: 'FURTHER not their evil plot' - that God not advance their scheme."),
 (273671,"lest exalted (rum)",273666,"v8: 'lest they be EXALTED' - the self-exaltation the psalmist asks God to block."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))") for _ in [0]}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (weapon/trap/serpent/coal imagery or label); standalone.")
r.write()
