#!/usr/bin/env python
"""Ps 28 (plea + thanksgiving). IB ops: the desperate call fearing God's silence
(lest I become like those in the pit); the wicked's duplicity (peace on the lips,
evil in the heart); blessing God for hearing; the heart that trusts and is
helped; the heart exulting in thanks. God's save/bless/shepherd = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=28
r = Reading("Psa", 19, CH, note="Plea+thanks: call fearing silence, the wicked's peace-mask, bless for hearing, heart trusts+helped, heart exults")

r.ch(276329,"call, lest you be silent","affect","the psalmist","the self calls to its rock, begging God not to be deaf, lest it become like those who go down to the pit - a cry that dreads divine silence","dread-of-silence","call-be-not-deaf",IB,
     "v1: 'To you, O LORD, I CALL; my rock, be not DEAF to me, lest... I become like those who go down to the pit' - the operation fears not the enemies but God's non-answer; silence from God would be death.")
r.ch(276351,"peace on the lips, evil in the heart","cognition","the wicked","the self asks not to be dragged off with the wicked, who speak peace with their neighbours while evil is in their hearts - inner duplicity","duplicity","peace-mask",IB,
     "v3: 'the workers of evil, who SPEAK PEACE with their neighbours while EVIL is in their HEARTS' - the wicked's interior is a split: the mouth offers peace, the heart hides harm.")
r.ch(276379,"blessed be the LORD, he has heard","affect","the psalmist","the self blesses the LORD for hearing the voice of its pleas - the turn from fear of silence to gratitude for being heard","gratitude-for-hearing","bless-he-heard",IB,
     "v6: 'BLESSED be the LORD! For he has HEARD the voice of my pleas' - the operation reverses v1's dread: the feared silence did not come; the interior turns to blessing.")
r.ch(276390,"my heart trusts and is helped","affect","the psalmist","the LORD is the self's strength and shield; in him the heart trusts and is helped - trust answered by help","trust-answered","heart-trusts-helped",IB,
     "v7: 'The LORD is my strength and my shield; in him my HEART TRUSTS, and I am HELPED' - the operation is the heart's reliance meeting God's aid; trust and rescue joined.")
r.ch(276393,"my heart exults, I give thanks","affect","the psalmist","the helped heart exults and, with song, the self gives thanks - joy overflowing into thanksgiving","exultant-thanks","heart-exults",IB,
     "v7: 'my HEART EXULTS, and with my song I give thanks to him' - distinct from the trust: the help received turns the interior to leaping joy and song.")

for sid,sense,src,d in [
 (276336,"Hear the voice of my pleas",276329,"v2: 'HEAR the voice of my pleas' - the hearing the call begs for."),
 (276381,"he has heard",276379,"v6: 'for he has HEARD the voice of my pleas' - the divine answer that prompts the blessing."),
 (276404,"save your people",276390,"v9: 'Oh, SAVE your people and bless your heritage' - the wider rescue the trusting heart asks for all Israel."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (pit/sanctuary/render-due-reward imagery, shepherd-carry, or label); standalone.")
r.write()
