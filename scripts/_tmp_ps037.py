#!/usr/bin/env python
"""Ps 37 (the great wisdom 'fret not' psalm, 152 spans, acrostic). Much is the
righteous-vs-wicked fate contrast (inheritance / grass / cut-off) = standalone/
qualifier. IB imperatives + states: refusing to fret/envy the wicked; trust and
do good; delight in the LORD; commit your way; be still and wait; refrain from
anger; the meek delighting in peace; the righteous' generosity; habitual generous
lending; turning from evil to good; the mouth that utters wisdom; the law in the
heart (steps not slipping); waiting while keeping God's way; marking the blameless
man's future; taking refuge."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=37
r = Reading("Psa", 19, CH, note="'Fret not' wisdom: fret-not/envy-not, trust+do-good, delight, commit-way, be-still+wait, refrain-anger, meek, generous, lending, turn-from-evil, utter-wisdom, law-in-heart, wait+keep-way, mark-blameless, refuge")

r.ch(277585,"fret not, be not envious of evildoers","volition","the hearer","the self is told not to fret over evildoers or be envious of wrongdoers - refusing the corrosive envy of the wicked's prosperity","refusing-envy","fret-not",IB,
     "v1: 'FRET not yourself because of evildoers; be not ENVIOUS of wrongdoers' - the operation is the disciplining of a specific inner unrest: the interior refuses to burn with envy at the wicked's success.")
r.ch(277739,"trust in the LORD and do good","volition","the hearer","the self is told to trust in the LORD and do good, dwelling in the land and befriending faithfulness - reliance joined to action","active-trust","trust-and-do-good",IB,
     "v3: 'TRUST in the LORD, and do GOOD; dwell in the land and befriend FAITHFULNESS' - the operation pairs an inner reliance with an outward doing; trust is not passive but works.")
r.ch(277814,"delight yourself in the LORD","affect","the hearer","the self is told to delight in the LORD, who will give the desires of the heart - joy in God that reshapes desire","delight","delight-in-the-LORD",IB,
     "v4: 'DELIGHT yourself in the LORD, and he will give you the DESIRES of your HEART' - the operation is the cultivation of joy in God; the interior that delights in him finds its wants aligned and met.")
r.ch(277828,"commit your way to the LORD","volition","the hearer","the self is told to commit its way to the LORD and trust him to act - handing over the whole course of life","entrustment","commit-your-way",IB,
     "v5: 'COMMIT your way to the LORD; TRUST in him, and he will act' - the operation is the rolling of one's road onto God; the interior lets go of managing outcomes and trusts him to work.")
r.ch(277841,"be still and wait patiently","volition","the hearer","the self is told to be still before the LORD and wait patiently, not fretting over the one who prospers - quiet, patient stillness","stillness","be-still-and-wait",IB,
     "v7: 'Be STILL before the LORD and WAIT patiently for him; fret not yourself over the one who prospers' - the operation is an inner quiet; the interior stops agitating and holds still before God.")
r.ch(277849,"refrain from anger, forsake wrath","volition","the hearer","the self is told to refrain from anger and forsake wrath, for fretting tends only to evil - the deliberate release of anger","anger-release","refrain-from-anger",IB,
     "v8: 'REFRAIN from ANGER, and forsake WRATH! Fret not yourself; it tends only to evil' - the operation is the letting-go of anger; the interior is warned that nursed wrath breeds only harm.")
r.ch(277600,"the meek delight in abundant peace","affect","the meek","the meek shall inherit the land and delight themselves in abundant peace - lowliness rewarded with peace-filled joy","meek-peace","meek-delight-in-peace",IB,
     "v11: 'the MEEK shall inherit the land and DELIGHT themselves in abundant PEACE' - the operation is the interior contentment of the lowly; meekness ends not in loss but in a peace it delights in.")
r.ch(277679,"the righteous is generous and gives","volition","the righteous","the wicked borrows and does not repay, but the righteous is generous and gives - open-handedness as a mark of the righteous interior","generosity","generous-and-gives",IB,
     "v21: 'the RIGHTEOUS is GENEROUS and gives' - the operation is open-handed giving; the righteous interior is marked by a freedom to give that the grasping wicked lacks.")
r.ch(277711,"ever lending generously","volition","the righteous","he is ever lending generously, and his children become a blessing - habitual, ongoing generosity","habitual-generosity","ever-lending",IB,
     "v26: 'He is ever LENDING GENEROUSLY, and his children become a blessing' - distinct from v21's giving: this is the sustained habit, a generosity that runs through the whole life and blesses the next generation.")
r.ch(277716,"turn from evil and do good","volition","the hearer","the self is told to turn away from evil and do good, so as to dwell forever - the twofold moral turn","moral-turn","turn-and-do-good",IB,
     "v27: 'Turn away from EVIL and do GOOD, so shall you dwell forever' - the operation is the double movement of the will: away from evil, toward good; the interior reorients its whole direction.")
r.ch(277748,"the righteous utters wisdom","cognition","the righteous","the mouth of the righteous utters wisdom and his tongue speaks justice - an interior so shaped that wise, just speech flows out","wise-speech","utter-wisdom",IB,
     "v30: 'The mouth of the RIGHTEOUS utters WISDOM, and his tongue speaks JUSTICE' - the operation is speech welling from a wise interior; what the righteous heart holds, the mouth pours out as wisdom.")
r.ch(277754,"the law in his heart, steps not slipping","cognition","the righteous","the law of his God is in his heart, so his steps do not slip - internalised law producing a steady walk","internalised-law","law-in-heart",IB,
     "v31: 'The LAW of his God is in his HEART; his steps do not SLIP' - the operation is the law made inward; because it lives in the heart, the interior's walk stays sure-footed.")
r.ch(277773,"wait for the LORD and keep his way","volition","the hearer","the self is told to wait for the LORD and keep his way, and he will exalt it to inherit the land - patient waiting joined to obedient keeping","patient-obedience","wait-and-keep-way",IB,
     "v34: 'WAIT for the LORD and KEEP his way, and he will exalt you to inherit the land' - distinct from v7's stillness: this waiting is active, coupled with keeping God's way while it waits.")
r.ch(277795,"mark the blameless - the man of peace has a future","cognition","the observer","the self bids one mark the blameless and behold the upright, for there is a future for the man of peace - a discernment that reads the end of the righteous","discernment","mark-the-blameless",IB,
     "v37: 'MARK the BLAMELESS and behold the UPRIGHT, for there is a FUTURE for the man of peace' - the operation is a trained perception: the interior learns to look past present appearances to the righteous man's lasting end.")
r.ch(277826,"they take refuge in him","affect","the righteous","the LORD helps and delivers the righteous from the wicked because they take refuge in him - refuge as the ground of rescue","refuge-taking","take-refuge",IB,
     "v40: 'The LORD helps them and delivers them... and saves them, because they TAKE REFUGE in him' - the operation closes the psalm on refuge: the whole deliverance of the righteous rests on their sheltering in God.")

for sid,sense,src,d in [
 (277817,"desires of your heart",277814,"v4: 'he will give you the DESIRES of your heart' - the fulfilment delighting in God brings."),
 (277601,"the meek shall inherit",277600,"v11: 'the meek shall INHERIT the land' - the possession that grounds the meek's peace-filled delight."),
 (277641,"the LORD upholds the righteous",277773,"v17: 'the LORD UPHOLDS the righteous' - the sustaining that rewards waiting and keeping his way."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (righteous-vs-wicked fate: inherit/cut-off/grass/chaff/sword-bow imagery, or God's-act label); standalone.")
r.write()
