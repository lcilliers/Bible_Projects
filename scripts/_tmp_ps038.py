#!/usr/bin/env python
"""Ps 38 (penitential; the crushing weight of sin and sickness; 83 spans). IB ops:
the body diseased by sin (no soundness); iniquities as a crushing burden;
festering wounds from folly; bowed down and mourning all day; feeble, groaning
from heart-tumult; all longing laid before God; the heart pounding, strength gone;
abandonment by friends; the deliberate silence of a deaf/mute man before accusers;
waiting for God to answer; confessing iniquity, sorry for sin. God's rebuke/heal/
haste = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=38
r = Reading("Psa", 19, CH, note="Penitential sickness: no-soundness, iniquity-burden, festering-wounds, bowed-mourning, groan-heart-tumult, longing-before-you, heart-throbs, friends-aloof, deaf-silence, wait, confess")

r.ch(277959,"no soundness in my flesh because of sin","state","the psalmist","there is no soundness in the self's flesh because of God's indignation, no health in its bones because of its sin - the body sick with guilt","sin-sickness","no-soundness",IB,
     "v3: 'There is no SOUNDNESS in my flesh because of your indignation; there is no health in my BONES because of my SIN' - the operation reads the illness as the body's registration of sin; guilt has gone into the flesh.")
r.ch(277969,"my iniquities a burden too heavy","state","the psalmist","the self's iniquities have gone over its head; like a heavy burden they are too heavy for it - the crushing weight of guilt","guilt's-weight","iniquities-burden",IB,
     "v4: 'For my INIQUITIES have gone over my head; like a HEAVY BURDEN, they are too heavy for me' - the operation is the felt mass of sin: the interior is pressed under a load it cannot carry.")
r.ch(277977,"my wounds fester through my folly","state","the psalmist","the self's wounds stink and fester because of its foolishness - self-inflicted rot from folly","festering-folly","wounds-fester",IB,
     "v5: 'My WOUNDS STINK and FESTER because of my FOOLISHNESS' - distinct from the sin-sickness: this names the wounds as the fruit of the self's own folly, corrupting from within.")
r.ch(277984,"utterly bowed down, mourning all day","state","the psalmist","the self is utterly bowed down and prostrate; all the day it goes about mourning - a whole day bent under grief","prostration","bowed-and-mourning",IB,
     "v6: 'I am utterly BOWED DOWN and prostrate; all the day I go about MOURNING' - the operation is the body folded by grief; the interior's mourning bends the whole frame.")
r.ch(277999,"I groan from the tumult of my heart","state","the psalmist","the self is feeble and crushed; it groans because of the tumult of its heart - inner uproar breaking out as groaning","inner-tumult","groan-heart-tumult",IB,
     "v8: 'I am feeble and crushed; I GROAN because of the TUMULT of my HEART' - the operation is the heart in uproar forcing itself out as a groan; the interior's turmoil is audible.")
r.ch(278006,"all my longing is before you","affect","the psalmist","all the self's longing is before the Lord; its sighing is not hidden from him - the desire laid open to God","open-longing","longing-before-you",IB,
     "v9: 'O Lord, all my LONGING is before you; my SIGHING is not hidden from you' - the operation exposes the interior: the self takes comfort that its whole ache is already visible to God.")
r.ch(277872,"my heart throbs, my strength fails","state","the psalmist","the self's heart throbs, its strength fails, the light of its eyes gone - the collapse of vitality","vitality-failing","heart-throbs",IB,
     "v10: 'My HEART throbs; my STRENGTH fails me, and the light of my eyes - it also has gone from me' - the operation is the ebbing of life-force; the interior's engine falters and even sight dims.")
r.ch(277883,"my friends stand aloof","state","the psalmist","the self's friends and companions stand aloof from its plague; its nearest kin stand far off - the isolation of the afflicted","abandonment","friends-aloof",IB,
     "v11: 'My FRIENDS and companions stand ALOOF from my plague, and my nearest kin stand far off' - the operation is the wound of being deserted; affliction has emptied the room of everyone.")
r.ch(277903,"like a deaf, mute man I do not answer","volition","the psalmist","the self becomes like a deaf man who does not hear, a mute who does not open his mouth - a deliberate silence before accusers","chosen-silence","deaf-and-mute",IB,
     "v13-14: 'But I am like a DEAF man; I do not hear, like a MUTE man who does not open his mouth' - the operation is a chosen refusal to answer: the interior, though slandered, keeps silence and leaves its case to God.")
r.ch(277919,"for you, O LORD, do I wait","affect","the psalmist","for the LORD the self waits; it is he who will answer - hope fixed on God's response","waiting","wait-you-answer",IB,
     "v15: 'But for you, O LORD, do I WAIT; it is you, O Lord my God, who will ANSWER' - the operation is the turn from silence to hope: the interior stops defending itself and waits for God to speak.")
r.ch(277935,"I confess my iniquity, I am sorry for my sin","cognition","the psalmist","the self confesses its iniquity and is sorry for its sin - penitence spoken and felt","penitence","confess-and-sorry",IB,
     "v18: 'I CONFESS my iniquity; I am SORRY for my sin' - the operation is the penitent turn: the interior names its guilt and grieves it, not merely its consequences.")

for sid,sense,src,d in [
 (277867,"rebuke me not in your anger",277959,"v1: 'O LORD, REBUKE me not in your anger' - the discipline the sin-sick body pleads to be spared."),
 (277922,"you will answer",277919,"v15: 'it is you, O Lord my God, who will ANSWER' - the response the waiting self expects."),
 (306284,"make haste to help me",277935,"v22: 'MAKE HASTE to help me, O Lord, my salvation!' - the rescue the confession appeals for."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (arrows/plague imagery, enemies-snares/accuse, or God's-discipline label); standalone.")
r.write()
