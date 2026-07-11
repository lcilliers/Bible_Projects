#!/usr/bin/env python
"""Ps 18 (David's great deliverance psalm, 141 spans - mostly theophany + battle
narrative + God-as-rock = qualifier/standalone). The human-IB char-arc: tender
love for God; refuge-taking; calling and being saved; the distress-cry; the
appeal to clean hands/righteousness; keeping God's ways; blamelessness; the
humble God saves (vs the haughty); blessing the rock (doxology); praise among the
nations."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=18
r = Reading("Psa", 19, CH, note="Deliverance psalm: love/refuge/call/distress-cry + integrity (clean-hands/kept-ways/blameless) + humble-saved + doxology/praise. Theophany+battle=standalone")

r.ch(274912,"love the LORD my strength","affect","the psalmist","the self declares a tender love for the LORD its strength - the rare verb of intimate affection opening the psalm","tender-love","love-you-LORD",IB,
     "v1: 'I LOVE you, O LORD, my strength' - the operation is warm attachment (racham, womb-love); the whole deliverance-song opens not with thanks but with affection.")
r.ch(274972,"take refuge in the rock","affect","the psalmist","the self takes refuge in God named as rock, fortress, shield, horn of salvation - shelter in a cluster of strongholds","refuge-taking","take-refuge",IB,
     "v2: 'my God, my rock, in whom I TAKE REFUGE' - the interior shelters in God under a pile of fortress-images; refuge is the posture from which the rescue is told.")
r.ch(275042,"call and be saved","affect","the psalmist","the self calls on the LORD, who is worthy of praise, and is saved from its enemies - the summary confidence","calling","call-and-saved",IB,
     "v3: 'I CALL upon the LORD, who is worthy to be praised, and I am SAVED from my enemies' - the operation states the whole pattern in miniature: to call is to be delivered.")
r.ch(275203,"cry in distress","affect","the psalmist","in distress, with the cords of death around it, the self calls and cries, and its cry reaches God's ears","distress-cry","cry-in-distress",IB,
     "v6: 'In my distress I CALLED upon the LORD... my CRY to him reached his ears' - distinct from the summary call of v3: this is the specific cry from the snares of death, the cry that triggers the theophany.")
r.ch(274980,"clean hands, righteousness","cognition","the psalmist","the self reckons that God dealt with it according to its righteousness and the cleanness of its hands - a confidence of integrity rewarded","integrity-confidence","clean-hands",IB,
     "v20: 'The LORD dealt with me according to my RIGHTEOUSNESS; according to the CLEANNESS of my hands he rewarded me' - the interior reads the deliverance as a response to its uprightness, not arbitrary.")
r.ch(274987,"kept the ways of the LORD","volition","the psalmist","the self has kept God's ways and not wickedly departed from him - sustained fidelity","fidelity","keep-his-ways",IB,
     "v21: 'For I have KEPT the ways of the LORD, and have not wickedly DEPARTED from my God' - the operation is a maintained loyalty; the clean hands of v20 rest on this kept course.")
r.ch(275005,"blameless, kept from guilt","volition","the psalmist","the self was blameless before God and kept itself from its own guilt - a vigilant self-guarding against sin","self-guarding","keep-from-guilt",IB,
     "v23: 'I was BLAMELESS before him, and I KEPT myself from my GUILT' - the operation turns inward: not just keeping God's ways but policing the self away from its own iniquity.")
r.ch(275028,"the humble God saves","state","the humble","God saves a humble people but brings down haughty eyes - lowliness as the saved condition","humility","humble-saved",IB,
     "v27: 'For you SAVE a HUMBLE people, but the HAUGHTY eyes you bring down' - the operation contrasts two interiors: the humble are rescued, the proud abased; the psalmist reads himself among the former.")
r.ch(275155,"bless the rock (doxology)","affect","the psalmist","the self blesses the living God, its rock and the God of its salvation - praise erupting as the rescue is recounted","doxology","bless-my-rock",IB,
     "v46: 'The LORD lives, and BLESSED be my rock, and exalted be the God of my salvation' - the interior breaks into blessing; the whole narration turns to ascribing greatness to the deliverer.")
r.ch(275180,"praise among the nations","volition","the psalmist","the self will praise God among the nations and sing to his name - gratitude broadcast beyond Israel","proclamation","praise-among-nations",IB,
     "v49: 'For this I will PRAISE you, O LORD, among the nations, and SING to your name' - the operation carries the private deliverance into public, international praise.")

for sid,sense,src,d in [
 (274903,"delivered me",274972,"v1(title)/48: 'who DELIVERED him' - the rescue the refuge-taking rests on."),
 (274962,"rescued to a broad place",274972,"v19: 'He brought me out into a BROAD PLACE; he RESCUED me' - the liberation from the snares of death."),
 (274964,"delighted in me",274980,"v19: 'he rescued me, because he DELIGHTED in me' - God's favour behind the integrity-reward."),
 (275210,"heard my voice",275203,"v6: 'he HEARD my voice; my cry reached his ears' - the divine hearing that answers the distress-cry."),
 (275082,"trains my hands for war",274980,"v34: 'He TRAINS my hands for war' - God's equipping the righteous self for battle."),
 (275094,"your gentleness made me great",274912,"v35: 'your GENTLENESS made me great' - the tender divine dealing answering the psalmist's love."),
 (275195,"steadfast love to his anointed",275155,"v50: 'showing STEADFAST LOVE to his anointed' - the covenant loyalty the doxology celebrates."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (theophany: coals/fire/nostrils/cherub/clouds; battle: bow/arrows/pursue/fall; God-as-rock/shield/salvation, or label); standalone.")
r.write()
