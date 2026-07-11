#!/usr/bin/env python
"""Ps 7 (plea of the persecuted righteous; oath of innocence). IB ops: taking
refuge; the soul threatened like prey; the oath of innocence (if I have done
wrong...); the appeal to be judged on integrity; the upright heart as ground of
confidence; the wicked's impenitence; the gestation of evil (conceives->pregnant
->gives birth to lies); thanksgiving. God's judging/testing/wrath = qualifier;
the pit-recoil, sword/arrow imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=7
r = Reading("Psa", 19, CH, note="Persecuted righteous: refuge, oath of innocence, appeal to integrity, upright heart, the wicked's gestating evil, thanks")

r.ch(283567,"take refuge in you","affect","the psalmist","the self takes refuge in God and asks to be saved from all pursuers - shelter sought first","refuge-taking","take-refuge",IB,
     "v1: 'O LORD my God, in you do I TAKE REFUGE; save me from all my pursuers' - before the oath, the interior first shelters; the whole plea is spoken from inside that refuge.")
r.ch(283631,"soul torn like prey","state","the psalmist","the fear that the enemy will tear the soul like a lion, with none to rescue - the self imagined as hunted prey","dread-of-being-torn","soul-as-prey",IB,
     "v2: 'lest they tear my SOUL apart like a lion, rending it in pieces, with none to deliver' - the interior registers the threat as a beast's kill; the soul, not just the body, is what could be shredded.")
r.ch(283641,"oath of innocence","cognition","the psalmist","the self submits itself to a conditional self-curse - if I have done this wrong, then let the enemy overtake me - rigorous self-examination staked on integrity","self-imprecation","oath-if-guilty",IB,
     "v3-4: 'if I have done THIS, if there is WRONG in my hands, if I have repaid my friend with evil...' - the operation is a searching self-audit turned into an oath: the self dares the worst on itself if it is guilty.")
r.ch(283683,"appeal to be judged on integrity","volition","the psalmist","the self asks God to judge it according to its righteousness and the integrity that is in it - confidence to be tried","appeal-to-be-judged","judge-my-integrity",IB,
     "v8: 'judge me, O LORD, according to my righteousness and according to the INTEGRITY that is in me' - the interior is so sure of its innocence that it invites, rather than fears, the divine verdict.")
r.ch(283578,"upright in heart","state","the psalmist","the ground of confidence: God saves the upright in heart - the interior's uprightness is what it rests on","uprightness","upright-heart",IB,
     "v10: 'My shield is with God, who saves the UPRIGHT in HEART' - the operation locates safety not in strength but in a straight interior; the heart's uprightness is the qualification for rescue.")
r.ch(283588,"the wicked will not repent","volition","the wicked","if the wicked man does not turn/repent, God whets his sword - impenitence as the wicked's settled refusal","impenitence","refuse-to-repent",IB,
     "v12: 'if a man does not REPENT, God will whet his sword' - the wicked's interior is read as a refusal to turn; the judgment hangs on that unrelenting inner posture.")
r.ch(283602,"conceives evil, births lies","cognition","the wicked","the wicked conceives evil, is pregnant with mischief, and gives birth to lies - harm gestated from within","gestation-of-evil","conceive-and-birth",IB,
     "v14: 'he CONCEIVES evil and is PREGNANT with mischief and gives birth to LIES' - the operation is a grim generation: the wicked interior gestates and delivers its harm like a pregnancy.")
r.ch(283622,"give thanks and sing","affect","the psalmist","the psalm closes with thanks to the LORD for his righteousness and song to his name - vindication answered with praise","thanksgiving","thanks-and-sing",IB,
     "v17: 'I will GIVE THANKS to the LORD due to his righteousness, and I will SING praise to the name of the LORD' - the interior lands in gratitude; the righteous judge trusted, the self already praises.")

for sid,sense,src,d in [
 (283634,"deliver me",283631,"v2: 'with none to DELIVER' - the rescue the threatened soul needs."),
 (283664,"Arise in your anger",283683,"v6: 'ARISE, O LORD, in your anger' - the judicial rousing the appeal to integrity calls for."),
 (283680,"judge the peoples",283683,"v8: 'the LORD JUDGES the peoples' - the divine court the self submits to."),
 (283691,"test minds and hearts",283578,"v9: 'you who TEST the minds and hearts, O righteous God' - God's searching of the interior that the upright heart welcomes."),
 (283581,"a righteous judge",283588,"v11: 'God is a righteous JUDGE, and a God who feels indignation every day' - the justice the impenitent runs against."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (sword/bow/arrow/pit imagery, poetic-justice recoil, or label); standalone.")
r.write()
