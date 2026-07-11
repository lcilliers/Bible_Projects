#!/usr/bin/env python
"""Ps 143 (David, penitential) - the crushed, thirsting, appalled inner self
seeking guidance. IB ops: the plea; the confession that no one living is
righteous; the crushed soul; the appalled heart; the fainting spirit (v4) vs the
failing spirit (v7); deliberate remembering/meditating to rouse faith; the
parched soul stretching out; trust grounded for the morning; seeking the way to
walk; lifting the soul; wanting to be taught God's will; the soul in trouble.
God's answer/teach/lead = qual."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=143
r = Reading("Psa", 19, CH, note="Penitential: crushed/appalled/thirsting self, remembering to rouse faith, seeking the way")

r.ch(273846,"prayer for a hearing","affect","the psalmist","the self pleads to be heard, appealing to God's faithfulness not its own merit","supplication","plea-on-faithfulness",IB,
     "v1: 'Hear my PRAYER; in your faithfulness answer me' - the interior grounds its appeal outside itself, on God's character.")
r.ch(273887,"confession of unworthiness","cognition","the psalmist","the self disclaims righteousness before God - no one living is justified in his sight","self-abasement","none-righteous",IB,
     "v2: 'Enter not into JUDGMENT with your servant, for no one living is righteous before you' - the interior refuses to plead its case on desert; a penitential clear-sightedness.")
r.ch(273901,"soul pursued and crushed","state","the psalmist","the enemy has crushed the life to the ground, seating the self in darkness like the long dead","crushedness","crushed-to-ground",IB,
     "v3: 'the enemy has pursued my SOUL, CRUSHED my life to the ground' - the interior is pressed flat, made to dwell in the darkness of the dead.")
r.ch(302614,"heart appalled within","state","the psalmist","the heart within is appalled/desolate - horror settling in the inmost self","desolation","appalled-within",IB,
     "v4: 'my HEART within me is APPALLED' - the operation is inner dismay: the heart recoils in horror at its own condition.")
r.ch(302610,"spirit faints (v4)","state","the psalmist","the spirit faints/grows faint under the weight - the animating self dimming","spirit-fainting","faint-v4",IB,
     "v4: 'my SPIRIT FAINTS within me' - the first collapse: the spirit ebbs as the heart is appalled (read distinct from the failing spirit of v7).")
r.ch(273909,"remember to rouse faith","cognition","the psalmist","deliberately recalling former days, God's deeds and works, to reignite trust","active-recall","remember-God's-deeds",IB,
     "v5: 'I REMEMBER the days of old; I meditate on all that you have done' - against the desolation the self chooses memory, feeding faith on God's past acts.")
r.ch(302620,"parched soul stretched out","affect","the psalmist","hands stretched out, the soul thirsts for God like a parched, waterless land","thirst-for-God","stretch-and-thirst",IB,
     "v6: 'I STRETCH OUT my hands to you; my SOUL thirsts for you like a PARCHED land' - the operation is bodily-imaged longing: the dry self reaching for water.")
r.ch(273921,"spirit fails (v7)","state","the psalmist","the spirit fails, at the edge of the pit - urgency of a self running out","spirit-failing","fail-v7",IB,
     "v7: 'Answer me quickly, O LORD; my SPIRIT FAILS' - the second collapse, now with the pit in view; read distinct from the fainting of v4.")
r.ch(273936,"trust for the morning","affect","the psalmist","the self entrusts itself, asking to hear steadfast love at daybreak - trust grounded","entrustment","trust-at-morning",IB,
     "v8: 'Let me hear of your steadfast love in the morning, for in you I TRUST' - the interior leans its weight on God, timing hope to the dawn.")
r.ch(273937,"seek the way to walk","volition","the psalmist","the self asks to be shown the way to go, lifting itself toward guidance","guidance-seeking","know-the-way",IB,
     "v8: 'Make me KNOW the WAY I should go, for to you I lift up my soul' - the interior wants direction, not just rescue: to be taught where to step.")
r.ch(273942,"lift up the soul","affect","the psalmist","the whole soul is lifted toward God - the self offered upward as the ground of the plea","self-offering","lift-the-soul",IB,
     "v8: 'to you I LIFT UP my SOUL' - the operation is the raising of the entire inner self as an oblation of trust.")
r.ch(273855,"desire to be taught God's will","volition","the psalmist","the self asks to be taught to do God's will, wanting the good spirit to lead it level","teachability","teach-me-your-will",IB,
     "v10: 'TEACH me to DO your WILL, for you are my God' - beyond guidance-for-safety: the interior wants conformity, to be led on level ground.")
r.ch(273874,"soul brought out of trouble","state","the psalmist","for God's name's sake the self asks to be preserved and its soul brought out of trouble","deliverance-longing","soul-out-of-trouble",IB,
     "v11: 'For your name's sake, O LORD, preserve my life; bring my SOUL out of TROUBLE' - the interior stakes its rescue on God's honour, not its own worth.")

for sid,sense,src,d in [
 (273845,"Hear (shama)",273846,"v1: 'HEAR my prayer' - the divine hearing sought."),
 (273848,"give ear (azan)",273846,"v1: 'GIVE EAR to my pleas' - the attending petition."),
 (273853,"answer (anah)",273846,"v1: 'in your faithfulness ANSWER me' - the response sought."),
 (273889,"judgment (mishpat)",273887,"v2: 'enter not into JUDGMENT' - the reckoning the self begs to avoid."),
 (273912,"meditate (hagah)",273909,"v5: 'I MEDITATE on all that you have done' - the operation of the remembering."),
 (273915,"ponder (siach)",273909,"v5: 'I PONDER the work of your hands' - the deepening of the recall."),
 (273918,"Answer quickly (anah)",273921,"v7: 'ANSWER me quickly' - the urgent response the failing spirit needs."),
 (273923,"Hide not (sathar)",273921,"v7: 'HIDE not your face from me' - lest the self go down to the pit."),
 (273931,"hear steadfast love",273936,"v8: 'let me HEAR of your steadfast love in the morning' - the assurance trust waits for."),
 (273862,"good Spirit leads level",273855,"v10: 'let your good SPIRIT LEAD me on level ground' - God's guiding the will asks for."),
 (273863,"lead (nachah)",273855,"v10: 'LEAD me' - the guiding act sought."),
 (305884,"Deliver (natsal)",273942,"v9: 'DELIVER me from my enemies; I have fled to you for refuge' - rescue tied to the lifted soul."),
 (273877,"steadfast love cuts off foes",273874,"v12: 'in your steadfast love CUT OFF my enemies' - God's covenant loyalty applied to the soul in trouble."),
 (273878,"cut off (tsamath)",273874,"v12: 'CUT OFF my enemies' - the deliverance petition."),
 (273880,"destroy adversaries (abad)",273874,"v12: 'DESTROY all the adversaries of my soul' - the plea for the soul's foes."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (darkness/pit/way imagery or God's-work label); standalone.")
r.write()
