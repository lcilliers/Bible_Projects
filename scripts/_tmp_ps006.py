#!/usr/bin/env python
"""Ps 6 (first penitential). IB ops: the languishing, bone-troubled self; the
greatly troubled soul; the plea from mortality (the dead cannot praise - longing
to remain among the praising living); weariness from moaning; nightly weeping
that drenches the bed; the eye wasting from grief; then the turn - dismissing
evildoers in new confidence. God's gracious/heal/deliver/hear = qualifier; the
enemies' shame = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=6
r = Reading("Psa", 19, CH, note="First penitential: languishing body, troubled soul, mortality-plea, weeping, then confident turn")

r.ch(281933,"languishing, bones troubled","state","the psalmist","the self is languishing, its very bones shaken - weakness that reaches to the frame","frailty","languishing",IB,
     "v2: 'Be gracious to me, for I am LANGUISHING; heal me, for my BONES are troubled' - the interior distress is felt as bodily collapse; the trouble has gone to the bones.")
r.ch(281939,"soul greatly troubled","state","the psalmist","beyond the bones, the soul itself is greatly troubled - the disturbance reaching the innermost self","inner-turmoil","soul-troubled",IB,
     "v3: 'my SOUL also is greatly TROUBLED. But you, O LORD - how long?' - read distinct from the bones: the trouble has penetrated past the body to the soul, and the cry becomes 'how long?'")
r.ch(281961,"the dead cannot praise you","cognition","the psalmist","the self pleads on the ground that in death and Sheol there is no remembrance or praise of God - motivating rescue by love of praising","plea-from-mortality","dead-cannot-praise",IB,
     "v5: 'For in DEATH there is no remembrance of you; in Sheol who will GIVE you PRAISE?' - the interior argues for its life by its desire to keep praising; the motive to be saved is to remain among the worshipping living.")
r.ch(281962,"weary with moaning","state","the psalmist","the self is worn out by its own groaning - grief exhausting the whole person","exhaustion","weary-moaning",IB,
     "v6: 'I am WEARY with my MOANING' - the operation is depletion: the sustained groaning has drained the interior of strength.")
r.ch(281971,"nightly weeping floods the bed","affect","the psalmist","every night the self floods its bed and drenches its couch with tears - grief overflowing in the dark hours","weeping","flood-the-bed",IB,
     "v6: 'every night I flood my bed with tears; I DRENCH my couch with my WEEPING' - read distinct from weariness: this is the active overflow, the measurable flood of grief through the night.")
r.ch(281972,"eye wasting from grief","state","the psalmist","the eye itself grows weak and wastes away because of grief and the foes - sorrow consuming the body's sight","grief-consumption","eye-wastes",IB,
     "v7: 'my EYE wastes away because of GRIEF; it grows weak because of all my foes' - the interior sorrow is written on the failing eye; grief is eating the body.")
r.ch(281978,"depart from me, evildoers","volition","the psalmist","the sudden turn: the self, now sure it is heard, dismisses the workers of evil - grief flipping to confident command","confident-dismissal","depart-from-me",IB,
     "v8: 'DEPART from me, all you WORKERS of evil, for the LORD has heard the sound of my weeping' - the interior pivots: the same weeping that drenched the bed is now the proof God has heard, and the self turns to expel the enemies.")

for sid,sense,src,d in [
 (281931,"be gracious (chanan)",281933,"v2: 'Be GRACIOUS to me' - the mercy the languishing self begs."),
 (281934,"heal me",281933,"v2: 'HEAL me, for my bones are troubled' - the restoring act sought for the shaken frame."),
 (281946,"turn and deliver",281961,"v4: 'TURN, O LORD, DELIVER my life' - the rescue the mortality-plea presses for."),
 (281953,"for your steadfast love",281961,"v4: 'save me for the sake of your STEADFAST LOVE' - the ground of the appeal for life."),
 (281984,"the LORD has heard",281978,"v8: 'the LORD has HEARD the sound of my weeping' - the divine act that turns grief to confidence."),
 (281992,"accepts my prayer",281978,"v9: 'the LORD ACCEPTS my prayer' - the answered supplication behind the dismissal of the foes."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (bed/couch/Sheol imagery or enemy-shame label); standalone.")
r.write()
