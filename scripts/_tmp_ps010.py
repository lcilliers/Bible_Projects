#!/usr/bin/env python
"""Ps 10 - a profile of the wicked's INTERIOR (the psalm's distinctive: it reads
the inner life of the oppressor). IB ops: arrogance in pursuit; self-glorying
greed; pride that crowds God out of every thought; the false security ('I shall
not be moved'); malice-filled speech; the predatory lurking; the settled
conviction 'God has forgotten, he will not see'. Plus the afflicted's desire that
God hears and whose heart he strengthens. God's see/note/break/incline =
qualifier; the victims + ambush imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=10
r = Reading("Psa", 19, CH, note="Profile of the wicked's inner life (arrogance/greed/practical-atheism/false-security/malice/predation) + the afflicted's heard desire")

r.ch(270434,"arrogant hot pursuit","disposition","the wicked","in arrogance the wicked hotly pursues the poor - pride expressed as predatory chase","arrogance","arrogant-pursuit",IB,
     "v2: 'In ARROGANCE the wicked hotly pursue the poor' - the interior driving the hunt is pride; self-exaltation turned into the chase of the weak.")
r.ch(270443,"boasts of his soul's desire","disposition","the wicked","the wicked boasts of the cravings of his soul, and the greedy man curses and renounces the LORD","self-glorying-greed","boast-of-desire",IB,
     "v3: 'the wicked BOASTS of the DESIRES of his soul, and the greedy renounces the LORD' - the interior parades its own appetites as its glory; greed become a creed that dismisses God.")
r.ch(270453,"pride crowds God out","cognition","the wicked","in the pride of his face the wicked will not seek God; 'there is no God' is the whole content of his thoughts","practical-atheism","no-room-for-God",IB,
     "v4: 'in the pride of his face the wicked does not SEEK God; all his THOUGHTS are, There is no God' - the operation is a mind so full of self that God is simply absent from every calculation.")
r.ch(270469,"'I shall not be moved'","cognition","the wicked","he says in his heart he will never be moved, never meet adversity - a self-assured permanence","false-security","never-be-moved",IB,
     "v6: 'He SAYS in his HEART, I shall not be MOVED; throughout all generations I shall not meet adversity' - the interior grants itself an untouchable stability, denial of any reckoning to come.")
r.ch(270479,"mouth full of cursing and deceit","cognition","the wicked","his mouth is filled with cursing, deceit and oppression; mischief and iniquity are under his tongue - malice stored inwardly","malice-in-speech","cursing-and-deceit",IB,
     "v7: 'His MOUTH is filled with CURSING and DECEIT and oppression; under his tongue are MISCHIEF and iniquity' - the interior stockpiles harm beneath the tongue, ready to deploy.")
r.ch(306005,"lurks like a lion to seize","volition","the wicked","he lurks in ambush like a lion in its thicket, waiting to seize and drag off the poor - patient predation","predatory-ambush","lurk-and-seize",IB,
     "v9: 'He LURKS in ambush like a LION in his thicket; he lurks that he may SEIZE the poor' - the interior is a hunter's patience; the whole inner posture is coiled to spring on the helpless.")
r.ch(270364,"'God has forgotten, he won't see'","cognition","the wicked","he says in his heart God has forgotten, has hidden his face, will never see it - the conviction of impunity","impunity-conviction","God-won't-see",IB,
     "v11: 'He SAYS in his HEART, God has FORGOTTEN, he has hidden his face, he will never SEE it' - read distinct from v6's false security: this is specifically the belief that God does not observe or judge, the engine of the whole cruelty.")
r.ch(270417,"the afflicted's desire heard","affect","the afflicted","the LORD hears the desire of the afflicted, strengthens their heart and inclines his ear - the longing of the crushed answered","answered-longing","desire-heard",IB,
     "v17: 'O LORD, you hear the DESIRE of the AFFLICTED; you will STRENGTHEN their heart' - over against the wicked's inner life, the afflicted's inner longing is the one God bends down to and steadies.")

for sid,sense,src,d in [
 (270387,"you do see",270364,"v14: 'But you DO SEE, for you note mischief and vexation' - God's sight that refutes the wicked's 'he will never see'."),
 (270388,"note the mischief",270364,"v14: 'you NOTE mischief and vexation, that you may take it into your hands' - God's active reckoning against the impunity-conviction."),
 (270377,"forget not the afflicted",270417,"v12: 'Arise, O LORD; O God, lift up your hand; FORGET not the afflicted' - the petition the afflicted's heard desire rests on."),
 (270399,"break the arm of the wicked",270434,"v15: 'BREAK the arm of the wicked and evildoer' - the judgment sought on the arrogant pursuer."),
 (270419,"strengthen their heart",270417,"v17: 'you will STRENGTHEN their heart; you will incline your ear' - God's steadying of the afflicted interior."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (victim: helpless/crushed/fatherless, or ambush/lion/net imagery, or label); standalone.")
r.write()
