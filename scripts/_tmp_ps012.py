#!/usr/bin/env python
"""Ps 12 (the faithful vanish; the pure words of the LORD). IB ops: the lament
that the godly/faithful have vanished; the double heart behind flattering lies;
the arrogance of self-sufficient speech ('with our tongue we will prevail'); the
groaning of the plundered needy that moves God. God's keep/guard + the pure words
= qualifier/standalone; the wicked prowling = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=12
r = Reading("Psa", 19, CH, note="The faithful vanish + false speech vs the needy's groaning; the pure words of the LORD")

r.ch(272740,"the godly have vanished","affect","the psalmist","the self laments that the godly one is gone and the faithful have disappeared from among men - grief at the failure of faithfulness","lament-over-loss","godly-vanished",IB,
     "v1: 'Save, O LORD, for the GODLY one is gone; the FAITHFUL have vanished from among the children of man' - the interior grieves a social collapse: it can no longer find a trustworthy person.")
r.ch(272751,"double heart behind flattery","cognition","everyone","everyone speaks lies to his neighbour with flattering lips and a heart-and-heart (double) - inner duplicity","duplicity","double-heart",IB,
     "v2: 'with FLATTERING lips and a DOUBLE HEART they speak' - the operation is a split interior: the smooth lips and the divided heart, saying one thing and being another.")
r.ch(272765,"'with our tongue we will prevail'","volition","the boasters","they say their tongue will prevail, their lips are their own, no one is master over them - autonomous, God-defying speech","self-sovereign-speech","tongue-will-prevail",IB,
     "v4: 'those who say, With our TONGUE we will PREVAIL, our lips are our own; who is master over us?' - the interior claims total ownership of its speech and denies any lord over it; pride located in the mouth.")
r.ch(306021,"the needy groan","affect","the poor / needy","because the poor are plundered and the needy groan, God rises to act - the inarticulate groan that summons rescue","groaning","needy-groan",IB,
     "v5: 'Because the poor are plundered, because the needy GROAN, I will now arise, says the LORD' - the interior of the crushed is a groan; it is precisely this sound that moves God to rise.")

for sid,sense,src,d in [
 (272738,"Save, O LORD",272740,"v1: 'SAVE, O LORD' - the plea prompted by the vanishing of the faithful."),
 (272755,"cut off flattering lips",272751,"v3: 'May the LORD CUT OFF all flattering lips' - the judgment sought on the double-hearted."),
 (306029,"place him in safety",306021,"v5: 'I will place him in the SAFETY for which he LONGS' - God's answer to the needy's groan."),
 (272783,"you will keep them",306021,"v7: 'You, O LORD, will KEEP them; you will guard us from this generation forever' - the protection the groaning receives."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (pure-words/refined-silver imagery, wicked prowling, or label); standalone.")
r.write()
