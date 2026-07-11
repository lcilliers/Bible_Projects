#!/usr/bin/env python
"""Ps 17 (plea of integrity; kept as the apple of the eye). IB ops: the plea from
guileless lips; the resolve of a tested heart not to transgress in speech;
deliberate avoidance of the violent's ways; feet held to God's paths, not
slipping; confident calling; the plea to be kept as the apple of the eye / under
the wings; the enemies' merciless arrogance; the worldly whose satisfaction is
only in this life; the hope of beholding God's face - true satisfaction. God's
try/wondrously-show/keep/arise = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=17
r = Reading("Psa", 19, CH, note="Plea of integrity: honest lips, tested-heart resolve, avoidance of violence, feet not slipping, apple-of-eye plea, enemies' arrogance, worldly vs God-face satisfaction")

r.ch(274763,"plea from guileless lips","affect","the psalmist","the self asks God to hear a just cause from lips free of deceit - an appeal staked on its own honesty","honest-appeal","plea-no-deceit",IB,
     "v1: 'Hear a just cause, O LORD... give ear to my prayer from lips free of DECEIT' - the interior grounds its right to be heard in the truthfulness of its speech.")
r.ch(274843,"tested heart, purposed not to sin","volition","the psalmist","God has tried the heart by night and found nothing; the self has purposed that its mouth will not transgress - a settled resolve confirmed by testing","resolved-integrity","purpose-not-transgress",IB,
     "v3: 'you have TRIED my HEART, you have visited me by night... I have PURPOSED that my mouth will not transgress' - the operation is a deliberate inner resolve, one the self is willing to have God test.")
r.ch(274854,"avoided the ways of the violent","volition","the psalmist","by the word of God's lips the self has avoided the paths of the violent - active steering-clear of cruelty","deliberate-avoidance","avoid-violent-ways",IB,
     "v4: 'by the word of your lips I have AVOIDED the ways of the VIOLENT' - the operation is a chosen non-participation; the interior has kept itself off the violent's road.")
r.ch(306042,"feet held fast, not slipped","volition","the psalmist","the self's steps have held fast to God's paths; its feet have not slipped - sustained fidelity of walk","steadfast-walk","feet-not-slipped",IB,
     "v5: 'My STEPS have held fast to your paths; my feet have not SLIPPED' - the operation is a maintained course; the interior has kept its footing on God's tracks.")
r.ch(274858,"call, confident of an answer","affect","the psalmist","the self calls upon God confident he will answer - appeal made in assurance","confident-calling","call-for-answer",IB,
     "v6: 'I CALL upon you, for you will ANSWER me, O God' - the interior calls not into silence but to a God it is sure will incline his ear.")
r.ch(274876,"keep me as the apple of your eye","affect","the psalmist","the self asks to be guarded as the pupil of the eye and hidden in the shadow of God's wings - a plea for the most intimate protection","intimate-refuge-longing","apple-of-eye",IB,
     "v8: 'KEEP me as the APPLE of your eye; hide me in the shadow of your wings' - the operation is a longing for tender, close-in protection: to be as precious and guarded as the eye's own pupil.")
r.ch(274780,"enemies closed to pity, arrogant","disposition","the enemies","the enemies close their hearts to pity and speak arrogantly, tracking the self down like a lion eager to tear","merciless-arrogance","closed-and-arrogant",IB,
     "v10-12: 'They CLOSE their hearts to PITY; with their mouths they speak ARROGANTLY... like a lion eager to tear' - the enemies' interior is shut against mercy and swollen with arrogance; a pitilessness that hunts.")
r.ch(274814,"the worldly satisfied with this life","affect","men of the world","men of the world have their portion in this life; filled with treasure, satisfied with children, they leave their abundance to their infants - a contentment bounded by the present age","this-life-satisfaction","worldly-satisfied",IB,
     "v14: 'from men of the world whose portion is in this LIFE... they are SATISFIED with children' - the interior of the worldly is filled and content, but only with what this life holds; a satisfaction that stops at the grave.")
r.ch(274821,"behold your face, satisfied with your likeness","affect","the psalmist","as for the self, it will behold God's face in righteousness and be satisfied, on waking, with his likeness - the true satisfaction, set against the worldly's","God-face-satisfaction","behold-and-be-satisfied",IB,
     "v15: 'As for me, I shall BEHOLD your face in righteousness; when I AWAKE, I shall be SATISFIED with your likeness' - read as the deliberate contrast to v14: the interior's satisfaction is not this-worldly plenty but the vision of God himself.")

for sid,sense,src,d in [
 (274765,"Hear a just cause",274763,"v1: 'HEAR a just cause, O LORD; attend to my cry' - the divine hearing the honest plea seeks."),
 (274838,"you have visited me by night",274843,"v3: 'you have VISITED me by night' - God's testing that confirms the purposed integrity."),
 (274867,"wondrously show your love",274876,"v7: 'WONDROUSLY show your steadfast love, O Saviour of those who seek refuge' - the marvel of love the apple-of-eye plea appeals to."),
 (274875,"Keep me",274876,"v8: 'KEEP me' - the guarding the intimate plea asks for."),
 (274789,"Arise, confront, deliver",274821,"v13: 'ARISE, O LORD! Confront him... DELIVER my soul from the wicked' - the rescue that clears the way to beholding God's face."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (lion/sword/wings/shadow imagery, enemy-encirclement, or label); standalone.")
r.write()
