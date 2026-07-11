#!/usr/bin/env python
"""Ps 19 (heavens declare + the law + the servant's plea). vv1-6 (cosmic glory)
= standalone. IB ops: the soul revived by the perfect law; the simple made wise;
the heart gladdened by the precepts; the clean, enduring fear of the LORD;
desiring the law above gold; self-examination for hidden faults; the plea to be
kept from presumptuous sin's dominion; the longing that heart-meditation be
acceptable. The law-attribute words (perfect/sure/right/pure/true) = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=19
r = Reading("Psa", 19, CH, note="The law's effects on the interior + the servant's self-examination and plea (heavens vv1-6 = standalone)")

r.ch(275314,"soul revived by the law","state","the psalmist","the perfect law of the LORD revives/restores the soul - the interior brought back to life by the word","revival","soul-revived",IB,
     "v7: 'The law of the LORD is perfect, REVIVING the SOUL' - the operation is inner restoration: the word acts on the soul the way food acts on a faint body.")
r.ch(275319,"the simple made wise","cognition","the simple","the sure testimony of the LORD makes the simple wise - an interior maturing from naivety to wisdom","maturing","simple-made-wise",IB,
     "v7: 'the testimony of the LORD is sure, making WISE the SIMPLE' - the operation is the opening of an untrained interior; the word grows understanding where there was none.")
r.ch(275324,"the heart gladdened by precepts","affect","the psalmist","the right precepts of the LORD rejoice the heart - the word producing inner gladness","gladdening","heart-rejoices",IB,
     "v8: 'the precepts of the LORD are right, REJOICING the HEART' - the operation is joy: the commandments do not merely bind, they gladden the interior that loves them.")
r.ch(275331,"the fear of the LORD, clean","affect","the psalmist","the fear of the LORD is clean, enduring forever - reverent fear as a pure and permanent interior posture","reverent-fear","clean-fear",IB,
     "v9: 'the FEAR of the LORD is CLEAN, enduring forever' - the operation names reverence itself as a state of the interior; unlike defiling fears, this one is pure and lasts.")
r.ch(275244,"desire the law above gold","affect","the psalmist","the rules of the LORD are more to be desired than much fine gold, sweeter than honey - a valuing that outbids treasure","supreme-valuing","desire-above-gold",IB,
     "v10: 'More to be DESIRED are they than gold, even much fine gold' - the operation is appraisal: the interior weighs the word against wealth and prefers it.")
r.ch(275262,"discern hidden errors","cognition","the psalmist","who can discern his errors? the self asks to be declared innocent of hidden faults - awareness of unseen sin","self-scrutiny","discern-errors",IB,
     "v12: 'Who can DISCERN his errors? Declare me INNOCENT from HIDDEN faults' - the operation is humble self-suspicion: the interior knows its own faults exceed its sight and asks God to cover them.")
r.ch(275270,"kept from presumptuous sin","volition","the psalmist","the self asks to be kept from presumptuous sins and not let them have dominion - guarding against willful, ruling sin","guarding-against-dominion","keep-from-presumption",IB,
     "v13: 'Keep back your servant also from PRESUMPTUOUS sins; let them not have DOMINION over me' - distinct from hidden faults: this is the deliberate sin the interior fears could master it; the plea is against being ruled.")
r.ch(275281,"heart-meditation made acceptable","volition","the psalmist","the self desires that the words of its mouth and the meditation of its heart be acceptable to God - the interior offered for approval","self-offering","acceptable-meditation",IB,
     "v14: 'Let the words of my mouth and the MEDITATION of my HEART be ACCEPTABLE in your sight' - the operation offers the whole inner life (speech and thought) to God as an oblation seeking his approval.")

for sid,sense,src,d in [
 (275258,"keeping them is great reward",275244,"v11: 'in KEEPING them there is great REWARD' - the benefit that grounds the desiring of the law."),
 (275287,"my redeemer",275281,"v14: 'O LORD, my rock and my REDEEMER' - the God to whom the meditation is offered."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (heavens-declare cosmic imagery vv1-6, or law-attribute label perfect/sure/right/pure/true); standalone.")
r.write()
