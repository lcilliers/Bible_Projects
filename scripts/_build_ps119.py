#!/usr/bin/env python
"""Persistent char-by-char builder for Ps 119 (641 candidates, 176 verses).
Read by CHAR-ARC (each recurring disposition read across the whole psalm), NOT by
the 22 alphabetic stanzas (those are arbitrary verse-blocks the passage rule forbids).

Structure:
- WORD-SYNONYMS (law/testimonies/precepts/statutes/commandments/rules/word/promise/
  faithfulness) + God-attribute/act terms = QUALIFIERS (God's revelation/acts), each
  source-linked to that verse's anchor disposition-char.
- The psalmist's dispositions/acts + the foes = CHARACTERISTICS (distinct per-occurrence
  notes, arc-aware).
- temporal/imagery = STANDALONE.

This file accumulates: CH holds authored characteristic notes keyed by sid; run reports
how many candidates remain unauthored. Apply only when coverage == 641.
"""
import sys, json, os
sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER

CANDS=json.load(open(os.path.join(os.environ.get('TMP',''),'')) if False else open(
  r"C:\Users\lerouxc\AppData\Local\Temp\claude\c--Bible-study-projects\e78eb6e5-dae6-487a-a98b-121f066465fc\scratchpad\ps119_candidates.json"))
# index
BYSID={x['sid']:x for x in CANDS}

# ---- word-synonym qualifiers (God's revelation) : strong -> (gloss) ----
WORD={
 'H8451':"law (torah)", 'H6490':"precepts (piqqudim)", 'H2706':"statutes (chuqqim)",
 'H4687':"commandments (mitsvot)", 'H1697':"word (dabar)", 'H4941':"rules (mishpatim)",
 'H5713':"testimonies (edot)", 'H5715':"testimonies (edut)", 'H0565':"promise/word (imrah)",
 'H0530':"faithfulness (emunah)", 'H2708':"statutes (chuqqah)", 'H0559':"promise (amar)",
 'H0571':"truth (emeth)", 'H6664':"righteous rules (tsedeq)", 'H6666':"righteousness (tsedaqah)",
 'H2617':"steadfast love (chesed)", 'H2896':"good (tob)", 'H3444':"salvation (yeshuah)",
 'H8668':"salvation (teshuah)", 'H7356':"mercy (racham)", 'H8034':"name (shem)",
}
# ---- God-acts petitioned (imperatives to God) = qualifiers ----
GODACT={
 'H2421':"give life / revive (chayah)", 'H3384':"teach (yarah)", 'H1580':"deal bountifully (gamal)",
 'H1540':"open my eyes (galah)", 'H5186':"incline my heart (natah)", 'H5674':"turn my eyes (abar)",
 'H2603':"be gracious (chanan)", 'H5162':"comfort (nacham)", 'H5826':"help (azar)",
 'H3467':"save (yasha)", 'H5337':"deliver/take not (natsal)", 'H5564':"uphold (samak)",
 'H5582':"hold up (saad)", 'H6299':"redeem (padah)", 'H1350':"redeem (gaal)",
 'H2502':"deliver (chalats)", 'H7378':"plead my cause (rib)", 'H8085':"hear (shama)",
 'H7521':"accept (ratsah)", 'H2470':"entreat/be gracious (chalah)", 'H4390':"fill (male)",
 'H6437':"turn to me (panah)", 'H3559':"establish/steadfast (kun)", 'H5117':"leave not (nuach)",
 'H6565':"it is time to act (parar)", 'H6884':"tried/proven (tsaraph)",
}
# ---- standalone (temporal / imagery / structural) ----
STAND={
 'H5769':"forever (olam)", 'H6118':"end (eqeb)", 'H1870':"way (derek)", 'H0734':"way/path (orach)",
 'H5410':"path (nathib)", 'H5216':"lamp (ner)", 'H1706':"honey (debash)", 'H2441':"palate/taste (chek)",
 'H6337':"fine gold (paz)", 'H2158':"songs (zemirah)", 'H5071':"freewill offerings (nedabah)",
 'H1320':"flesh (basar)", 'H7342':"wide place (rachab)", 'H6471':"steps (paam)", 'H2940':"judgment/taste (taam)",
 'H1847':"knowledge (daath)", 'H6608':"unfolding (pethach)", 'H6612':"the simple (pethi)",
 'H2898':"good/well (tub)", 'H0937':"contempt (buz)", 'H2781':"scorn (cherpah)", 'H7723':"worthless things (shav)",
 'H1215':"selfish gain (betsa)", 'H5749':"ensnare (ud)", 'H6341':"snare (pach)", 'H4383':"stumbling block (mikshol)",
 'H7965':"peace (shalom)", 'H2154':"evil purpose (zimmah)", 'H3245':"founded (yasad)", 'H5324':"firmly fixed (natsab)",
 'H5975':"stands fast (amad)", 'H2950':"smear with lies (taphal)", 'H8649':"cunning (tarmith)",
 'H7379':"cause (rib)", 'H2135':"pure (zakah)", 'H8467':"plea (techinnah)", 'H5042':"pour forth (naba)",
 'H0779':"accursed ones (arar)", 'H6923':"before dawn (qadam)", 'H7126':"draw near (qarab)",
 'H2158b':"songs", 'H8375':"longing (taavah)", 'H1638':"consumed (garas)",
}
# ---- verse -> anchor char sid (registered as CH authored). qualifiers/standalone in a verse
#      source-link to that verse's anchor (first authored char in the verse). ----
CH={}   # sid -> dict(sense,typ,bearer,op,target,coupling,locus,note)
def ch(sid, sense,typ,bearer,op,target,coupling,locus,note):
    CH[sid]=dict(sense=sense,typ=typ,bearer=bearer,op=op,target=target,coupling=coupling,locus=locus,note=note)

# =========================================================================
# CHAR-ARCS  (author one disposition across ALL its verses; distinct nuance each)
# =========================================================================

# ---- ARC: KEEP (shamar H8104 + natsar H5341) : observing/guarding God's word ----
# shamar occurrences
KEEP_SHAMAR={
 4:"'You have commanded your precepts to be KEPT diligently' - the charge to keep, the psalm's premise.",
 5:"'Oh that my ways may be steadfast in KEEPING your statutes!' - the longing to keep, keeping as aspiration.",
 8:"'I will KEEP your statutes; do not utterly forsake me!' - the vow to keep joined to the plea not to be forsaken.",
 9:"'How can a young man keep his way pure? By guarding it according to your word' - keeping the way pure by the word.",
 17:"'Deal bountifully... that I may live and KEEP your word' - keeping as the aim of the life God gives.",
 34:"'Give me understanding, that I may KEEP your law and observe it with my whole heart' - keeping that flows from understanding, whole-hearted.",
 44:"'I will KEEP your law continually, forever and ever' - keeping vowed without end.",
 55:"'I remember your name in the night, O LORD, and KEEP your law' - keeping through the night, memory issuing in obedience.",
 57:"'The LORD is my portion; I promise to KEEP your words' - keeping as the response to God being one's portion.",
 60:"'I hasten and do not delay to KEEP your commandments' - keeping done promptly, obedience without procrastination.",
 63:"'I am a companion of all who fear you, of those who KEEP your precepts' - keeping as the bond of the God-fearing community.",
 67:"'Before I was afflicted I went astray, but now I KEEP your word' - keeping learned through affliction.",
 88:"'In your steadfast love give me life, that I may KEEP the testimonies of your mouth' - keeping as the purpose of the revival sought.",
 101:"'I hold back my feet from every evil way, in order to KEEP your word' - keeping that requires restraining the feet from evil.",
 106:"'I have sworn an oath and confirmed it, to KEEP your righteous rules' - keeping bound by solemn oath.",
 134:"'Redeem me from man's oppression, that I may KEEP your precepts' - keeping as the freedom sought from oppression.",
 136:"'My eyes shed streams of tears, because people do not KEEP your law' - grief at others' failure to keep, keeping loved so its breach is wept.",
 146:"'I call to you; save me, that I may KEEP your testimonies' - keeping as the aim of the cry for salvation.",
 158:"'I look at the faithless with disgust, because they do not KEEP your commands' - revulsion at the faithless who will not keep.",
 167:"'My soul KEEPS your testimonies; I love them exceedingly' - keeping seated in the soul, joined to intense love.",
 168:"'I KEEP your precepts and testimonies, for all my ways are before you' - keeping done in the awareness that all is open to God.",
}
KEEP_NATSAR={
 2:"'Blessed are those who KEEP his testimonies, who seek him with their whole heart' - the guarding of the testimonies that marks the blessed.",
 22:"'Take away from me scorn and contempt, for I have KEPT your testimonies' - keeping pleaded as ground for relief from scorn.",
 33:"'Teach me... the way of your statutes, and I will KEEP it to the end' - keeping vowed to the very end.",
 34:"'Give me understanding, that I may keep your law and OBSERVE it with my whole heart' - the guarding-with-the-whole-heart paired with keeping.",
 56:"'This has become mine: that I KEEP your precepts' - keeping as the psalmist's very possession.",
 69:"'The insolent smear me with lies, but with my whole heart I KEEP your precepts' - keeping held fast with the whole heart against slander.",
 100:"'I understand more than the aged, for I KEEP your precepts' - keeping as the source of understanding beyond the elders.",
 115:"'Depart from me, you evildoers, that I may KEEP the commandments of my God' - keeping that requires separation from evildoers.",
 129:"'Your testimonies are wonderful; therefore my soul KEEPS them' - the soul's guarding drawn out by the wonder of the testimonies.",
 145:"'With my whole heart I cry; answer me, O LORD! I will KEEP your statutes' - keeping vowed in the whole-hearted cry.",
}
for v,note in KEEP_SHAMAR.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H8104'), None)
    if sid: ch(sid,"keep / observe (shamar)","action","the psalmist","keep / observe","God's word","paired with the whole KEEP-arc of the psalm",GOD, f"v{v}: {note}")
for v,note in KEEP_NATSAR.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H5341'), None)
    if sid: ch(sid,"keep / guard (natsar)","action","the psalmist","keep / guard","God's testimonies","paired with the whole KEEP-arc of the psalm",GOD, f"v{v}: {note}")

# ---- ARC: LOVE (aheb H0157) : loving God's law ----
LOVE={
 47:"'I find my delight in your commandments, which I LOVE' - love of the commandments as the spring of delight.",
 48:"'I will lift up my hands toward your commandments, which I LOVE' - love expressed in the lifted hands of devotion.",
 97:"'Oh how I LOVE your law! It is my meditation all the day' - the exclamation at the heart of the psalm, love that meditates ceaselessly.",
 113:"'I hate the double-minded, but I LOVE your law' - love of the law set against hatred of the divided heart.",
 119:"'you discard all the wicked of the earth like dross, therefore I LOVE your testimonies' - love drawn out by seeing God's justice.",
 127:"'Therefore I LOVE your commandments above gold, above fine gold' - love that values the law more than the finest gold.",
 132:"'Turn to me and be gracious, as is your way with those who LOVE your name' - love of God's name as the mark of those he favours.",
 140:"'Your promise is well tried, and your servant LOVES it' - love of the tested, proven promise.",
 159:"'Consider how I LOVE your precepts! Give me life according to your steadfast love' - love pleaded as ground for revival.",
 163:"'I hate and abhor falsehood, but I LOVE your law' - love of the law against abhorrence of falsehood.",
 165:"'Great peace have those who LOVE your law; nothing can make them stumble' - love of the law as the source of unstumbling peace.",
 167:"'My soul keeps your testimonies; I LOVE them exceedingly' - love intensified, the soul's exceeding love.",
}
for v,note in LOVE.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H0157'), None)
    if sid: ch(sid,"love (aheb)","disposition","the psalmist","love","God's law/commandments/testimonies","paired with the whole LOVE-arc of the psalm",GOD, f"v{v}: {note}")

# ---- ARC: DELIGHT (shaashua H8191, shaa H8173, sus/rejoice H7797, chaphets H2654) ----
DELIGHT={
 ('H8191',24):"'Your testimonies are my DELIGHT; they are my counsellors' - the testimonies as delight and guide.",
 ('H8191',77):"'Let your mercy come to me, that I may live; for your law is my DELIGHT' - the law as the delight that sustains life.",
 ('H8191',92):"'If your law had not been my DELIGHT, I would have perished in my affliction' - delight in the law as what kept him alive in affliction.",
 ('H8191',143):"'Trouble and anguish have found me out, but your commandments are my DELIGHT' - delight persisting through trouble.",
 ('H8191',174):"'I long for your salvation, O LORD, and your law is my DELIGHT' - delight in the law joined to longing for salvation.",
 ('H8173',16):"'I will DELIGHT in your statutes; I will not forget your word' - delight vowed, paired with not forgetting.",
 ('H8173',47):"'I find my DELIGHT in your commandments, which I love' - delight found in the loved commandments.",
 ('H8173',70):"'their heart is unfeeling like fat, but I DELIGHT in your law' - delight set against the gross heart of the insolent.",
 ('H7797',14):"'In the way of your testimonies I DELIGHT (rejoice) as much as in all riches' - delight in the testimonies weighed against all wealth.",
 ('H7797',162):"'I REJOICE at your word like one who finds great spoil' - joy in the word like a soldier's plunder.",
 ('H2654',35):"'Lead me in the path of your commandments, for I DELIGHT in it' - delight as the reason to be led in the path.",
}
for (ps,v),note in DELIGHT.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']==ps), None)
    if sid: ch(sid,"delight (shaashua/shaa/sus)","disposition","the psalmist","delight / rejoice","in God's law","paired with the whole DELIGHT-arc of the psalm",GOD, f"v{v}: {note}")

# ---- ARC: MEDITATE (siach H7878, sichah H7881) ----
MED={
 ('H7878',15):"'I will MEDITATE on your precepts and fix my eyes on your ways' - meditation joined to fixing the eyes on God's ways.",
 ('H7878',23):"'Though princes sit plotting against me, your servant will MEDITATE on your statutes' - meditation held steady while princes plot.",
 ('H7878',27):"'Make me understand the way of your precepts, and I will MEDITATE on your wondrous works' - meditation on God's wonders sought.",
 ('H7878',48):"'I will lift up my hands... and MEDITATE on your statutes' - meditation joined to the lifted hands of love.",
 ('H7878',78):"'Let the insolent be put to shame... as for me, I will MEDITATE on your precepts' - meditation as the calm response to the insolent's wrong.",
 ('H7878',148):"'My eyes are awake before the watches of the night, that I may MEDITATE on your promise' - meditation through the sleepless night-watches.",
 ('H7881',97):"'Oh how I love your law! It is my MEDITATION all the day' - ceaseless meditation flowing from love.",
 ('H7881',99):"'I have more understanding than all my teachers, for your testimonies are my MEDITATION' - meditation as the source of understanding beyond teachers.",
}
for (ps,v),note in MED.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']==ps), None)
    if sid: ch(sid,"meditate (siach)","action","the psalmist","meditate / muse","on God's precepts/statutes/promise","paired with the whole MEDITATE-arc of the psalm",GOD, f"v{v}: {note}")

# ---- ARC: HOPE (yachal H3176, sabar H7663, seber H7664) ----
HOPE={
 ('H3176',43):"'Take not the word of truth utterly out of my mouth, for my HOPE is in your rules' - hope resting in God's rules.",
 ('H3176',49):"'Remember your word to your servant, in which you have made me HOPE' - hope grounded in God's own word.",
 ('H3176',74):"'Those who fear you shall see me and rejoice, because I have HOPED in your word' - hope that gladdens the God-fearing who witness it.",
 ('H3176',81):"'My soul longs for your salvation; I HOPE in your word' - hope amid the soul's fainting longing.",
 ('H3176',114):"'You are my hiding place and my shield; I HOPE in your word' - hope resting on God as refuge and shield.",
 ('H3176',147):"'I rise before dawn and cry for help; I HOPE in your words' - hope voiced in the pre-dawn cry.",
 ('H7663',166):"'I HOPE for your salvation, O LORD, and I do your commandments' - hope for salvation joined to obedience.",
 ('H7664',116):"'Uphold me according to your promise, that I may live, and let me not be put to shame in my HOPE!' - the hope that must not be shamed.",
}
for (ps,v),note in HOPE.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']==ps), None)
    if sid: ch(sid,"hope (yachal/sabar)","disposition","the psalmist","hope / wait","in God's word",  "paired with the whole HOPE-arc of the psalm",GOD, f"v{v}: {note}")

# ---- ARC: HEART (leb H3820) : the whole-heart devotion (+ the foes' gross heart) ----
HEART={
 2:("the psalmist",IB,"'Blessed are those who... seek him with their whole HEART' - the undivided heart that seeks God."),
 10:("the psalmist",IB,"'With my whole HEART I seek you; let me not wander from your commandments' - the whole heart's pursuit, guarded against straying."),
 11:("the psalmist",IB,"'I have stored up your word in my HEART, that I might not sin against you' - the word treasured in the heart as a guard against sin."),
 32:("the psalmist",IB,"'I will run in the way of your commandments when you enlarge my HEART!' - the heart God enlarges, freeing it to run."),
 34:("the psalmist",IB,"'that I may keep your law and observe it with my whole HEART' - the whole heart engaged in keeping."),
 36:("the psalmist",IB,"'Incline my HEART to your testimonies, and not to selfish gain!' - the heart begged to be bent toward the word, away from gain."),
 58:("the psalmist",IB,"'I entreat your favour with all my HEART' - the whole heart's entreaty for God's grace."),
 69:("the psalmist",IB,"'with my whole HEART I keep your precepts' - the whole heart keeping firm though the insolent smear with lies."),
 70:("the insolent",IB,"'their HEART is unfeeling like fat, but I delight in your law' - the gross, senseless heart of the foes, foil to the psalmist's delight."),
 80:("the psalmist",IB,"'May my HEART be blameless in your statutes, that I may not be put to shame!' - the plea for a blameless heart."),
 111:("the psalmist",IB,"'Your testimonies are... the joy of my HEART' - the heart whose very joy is the testimonies."),
 112:("the psalmist",IB,"'I incline my HEART to perform your statutes forever, to the end' - the heart set, self-directed, to obey to the end."),
 145:("the psalmist",IB,"'With my whole HEART I cry; answer me, O LORD!' - the whole heart's cry for answer."),
 161:("the psalmist",IB,"'Princes persecute me without cause, but my HEART stands in awe of your words' - the heart awed by the word even under persecution."),
}
for v,(bearer,loc,note) in HEART.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H3820'), None)
    if sid: ch(sid,"heart (leb)","faculty",bearer,"devote / dispose the heart","toward (or against) God's word","paired with the whole HEART-arc of the psalm",loc, f"v{v}: {note}")

# ---- ARC: SOUL (nephesh H5315) : the self longing/clinging/fainting/keeping ----
SOUL={
 20:"'My SOUL is consumed with longing for your rules at all times' - the self wasting with unceasing longing for the word.",
 25:"'My SOUL clings to the dust; give me life according to your word!' - the self pressed down to the dust, pleading revival.",
 28:"'My SOUL melts away for sorrow; strengthen me according to your word!' - the self dissolving in grief, seeking the word's strength.",
 81:"'My SOUL longs for your salvation; I hope in your word' - the self fainting with longing for salvation.",
 109:"'I hold my SOUL (life) in my hand continually, yet I do not forget your law' - the self held in constant peril, yet the law unforgotten.",
 129:"'Your testimonies are wonderful; therefore my SOUL keeps them' - the self guarding the wonderful testimonies.",
 167:"'My SOUL keeps your testimonies; I love them exceedingly' - the self keeping and loving the testimonies to excess.",
 175:"'Let my SOUL live and praise you, and let your rules help me' - the self pleading to live for praise.",
}
for v,note in SOUL.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H5315'), None)
    if sid: ch(sid,"soul (nephesh)","faculty","the psalmist","long / cling / keep with the soul","toward God's word","paired with the whole SOUL-arc of the psalm",IB, f"v{v}: {note}")

# ---- ARC: FORGET-NOT (shakach H7911) : the guarded memory (+ the foes who forget) ----
FORGET={
 16:("the psalmist",IB,GOD,"'I will delight in your statutes; I will not FORGET your word' - the guarded memory joined to delight."),
 61:("the psalmist",IB,GOD,"'Though the cords of the wicked ensnare me, I do not FORGET your law' - memory held fast though the wicked ensnare."),
 83:("the psalmist",IB,GOD,"'For I have become like a wineskin in the smoke, yet I have not FORGOTTEN your statutes' - memory kept though shrivelled by affliction."),
 93:("the psalmist",IB,GOD,"'I will never FORGET your precepts, for by them you have given me life' - memory vowed forever, for the precepts gave life."),
 109:("the psalmist",IB,GOD,"'I hold my life in my hand continually, but I do not FORGET your law' - memory unbroken though life is in peril."),
 139:("the foes",IB,GOD,"'My zeal consumes me, because my foes FORGET your words' - the foes' forgetting that stirs the psalmist's zeal."),
 141:("the psalmist",IB,GOD,"'I am small and despised, yet I do not FORGET your precepts' - memory held though the psalmist is despised."),
 153:("the psalmist",IB,GOD,"'Look on my affliction and deliver me, for I do not FORGET your law' - memory pleaded amid affliction."),
 176:("the psalmist",IB,GOD,"'I have gone astray like a lost sheep... for I do not FORGET your commandments' - memory clung to even in straying, the psalm's closing plea."),
}
for v,(bearer,loc,tloc,note) in FORGET.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H7911'), None)
    if sid: ch(sid,"forget (shakach, negated)","disposition",bearer,"not forget (or, of foes, forget)","God's word/precepts","paired with the whole FORGET-arc of the psalm",tloc, f"v{v}: {note}")

# ---- ARC: INSOLENT / PROUD (zed H2086) : the arrogant foes ----
INSOLENT={
 21:"'You rebuke the INSOLENT, accursed ones, who wander from your commandments' - the proud who stray, under God's rebuke.",
 51:"'The INSOLENT utterly deride me, but I do not turn away from your law' - the proud's derision, met by steadfastness.",
 69:"'The INSOLENT smear me with lies, but with my whole heart I keep your precepts' - the proud's slander, answered by whole-hearted keeping.",
 78:"'Let the INSOLENT be put to shame, because they have wronged me with falsehood' - the proud whose shame the psalmist invokes.",
 85:"'The INSOLENT have dug pitfalls for me; they do not live according to your law' - the proud who trap him, lawless.",
 122:"'let not the INSOLENT oppress me' - the proud from whose oppression the psalmist seeks surety.",
}
for v,note in INSOLENT.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H2086'), None)
    if sid: ch(sid,"insolent / proud (zed)","status","the insolent","deride / slander / oppress","the psalmist","paired with the whole INSOLENT-foe arc",IB, f"v{v}: {note}")

# ---- ARC: WICKED (rasha H7563) : the lawless foes ----
WICKED={
 53:"'Hot indignation seizes me because of the WICKED, who forsake your law' - the psalmist's indignation at the law-forsaking wicked.",
 61:"'Though the cords of the WICKED ensnare me, I do not forget your law' - the wicked's snares, powerless over his memory.",
 95:"'The WICKED lie in wait to destroy me, but I consider your testimonies' - the wicked's ambush, met by considering the word.",
 110:"'The WICKED have laid a snare for me, but I do not stray from your precepts' - the wicked's trap, unable to make him stray.",
 119:"'All the WICKED of the earth you discard like dross; therefore I love your testimonies' - the wicked God discards, moving the psalmist to love.",
 155:"'Salvation is far from the WICKED, for they do not seek your statutes' - the wicked far from salvation, unseeking.",
}
for v,note in WICKED.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H7563'), None)
    if sid: ch(sid,"wicked (rasha)","status","the wicked","forsake the law / ensnare","the psalmist and God's law","paired with the whole WICKED-foe arc",IB, f"v{v}: {note}")

# ---- ARC: PUT TO SHAME (bosh H0954) : the psalmist's dreaded shame (+ foes shamed) ----
SHAME={
 6:("the psalmist",IB,"'Then I shall not be PUT TO SHAME, having my eyes fixed on all your commandments' - shame averted by fixing the eyes on the commandments."),
 31:("the psalmist",IB,"'I cling to your testimonies, O LORD; let me not be PUT TO SHAME!' - the plea against shame, clinging to the word."),
 46:("the psalmist",IB,"'I will also speak of your testimonies before kings and shall not be PUT TO SHAME' - bold testimony without shame before kings."),
 78:("the insolent",IB,"'Let the insolent be PUT TO SHAME, because they have wronged me with falsehood' - the foes' shame invoked for their wrong."),
 80:("the psalmist",IB,"'May my heart be blameless in your statutes, that I may not be PUT TO SHAME!' - shame guarded against by a blameless heart."),
 116:("the psalmist",IB,"'let me not be PUT TO SHAME in my hope!' - the hope that must not end in shame."),
}
for v,(bearer,loc,note) in SHAME.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H0954'), None)
    if sid: ch(sid,"be put to shame (bosh)","state",bearer,"be (or not be) put to shame","before God/men","paired with the whole SHAME-arc of the psalm",loc, f"v{v}: {note}")

# ---- ARC: FALSEHOOD (sheqer H8267) : the false way, hated ----
FALSE={
 29:"'Put FALSE ways far from me and graciously teach me your law!' - the false way the psalmist begs God to remove.",
 69:"'The insolent smear me with lies (FALSEHOOD), but with my whole heart I keep your precepts' - the slander of the proud.",
 78:"'Let the insolent be put to shame, because they have wronged me with FALSEHOOD' - the lie by which the foes wronged him.",
 86:"'All your commandments are sure; they persecute me with FALSEHOOD; help me!' - the lying persecution against which he cries for help.",
 104:"'Through your precepts I get understanding; therefore I hate every FALSE way' - the false way hated as the fruit of understanding.",
 118:"'You spurn all who go astray from your statutes, for their cunning is in vain (FALSEHOOD)' - the vain deceit of the strayers.",
 128:"'I consider all your precepts to be right; I hate every FALSE way' - the false way hated as the counterpart to esteeming the precepts.",
 163:"'I hate and abhor FALSEHOOD, but I love your law' - falsehood abhorred, set against love of the law.",
}
for v,note in FALSE.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']=='H8267'), None)
    if sid: ch(sid,"falsehood / false way (sheqer)","disposition","the foes / the false way","lie / deceive","against the psalmist and the truth","paired with the whole FALSEHOOD arc",IB, f"v{v}: {note}")

# ---- per-verse QUALIFIER overrides (God-act direction of ambiguous lemmas) ----
QOVR={
 ('H3925',12):"teach (lamad)", ('H3925',26):"teach (lamad)", ('H3925',64):"teach (lamad)",
 ('H3925',66):"teach good judgment (lamad)", ('H3925',68):"teach (lamad)", ('H3925',108):"teach (lamad)",
 ('H3925',124):"teach (lamad)", ('H3925',135):"teach (lamad)", ('H3925',171):"teach (lamad)",
 ('H0995',27):"make me understand (bin)", ('H0995',34):"give understanding (bin)", ('H0995',73):"give understanding (bin)",
 ('H0995',125):"give understanding (bin)", ('H0995',130):"impart understanding (bin)", ('H0995',144):"give understanding (bin)",
 ('H0995',169):"give understanding (bin)",
 ('H2142',49):"remember your word (zakar)",
 ('H5800',8):"forsake not (azab)",
 ('H1245',176):"seek your servant (baqash)",
 ('H0935',41):"let your love come (bo)", ('H0935',77):"let your mercy come (bo)",
 ('H1540',18):"open my eyes (galah)", ('H6381',18):"wondrous things of the law (pala)", ('H6381',27):"wondrous works (pala)",
 ('H5641',19):"hide not (sathar)", ('H1556',22):"take away scorn (galal)",
 ('H5541',118):"spurn the strayers (salah)", ('H6565',126):"time to act, law broken (parar)",
 ('H3474',128):"right precepts (yashar)", ('H6382',129):"wonderful testimonies (pala)",
 ('H6662',137):"righteous (tsaddiq)", ('H3477',137):"right rules (yashar)",
 ('H3245',152):"founded forever (yasad)",
 ('H5493',29):"put false ways far (sur)", ('H6680',4):"commanded (tsavah)", ('H6680',138):"appointed in righteousness (tsavah)",
 ('H1605',21):"rebuke the insolent (gaar)", ('H3190',68):"do good (yatab)",
}
# ---- per-verse STANDALONE overrides ----
SOVR={
 ('H3925',99):"teachers (lamad)", ('H2459',70):"fat (cheleb)", ('H7451',101):"evil way (ra)",
 ('H8424',28):"sorrow (tugah)", ('H1320',120):"flesh (basar)", ('H6789',139):"consumes (tsamath)",
 ('H8467',170):"plea (techinnah)", ('H5042',171):"pour forth (naba)",
 ('H5766',3):"wrong (avlah)", ('H2954',70):"fat (cheleb)", ('H2895',71):"it is good (tob)",
}
# ---- remaining CHARACTERISTICS by (strong, verse): (sense, typ, bearer, op, locus, note) ----
_P="the psalmist"
CHARS={
 # LEARN (I learn)
 ('H3925',7):("learn (lamad)","action",_P,"learn","external:god","v7: 'I will praise you with an upright heart when I LEARN your righteous rules' - learning the rules as the ground of upright praise."),
 ('H3925',71):("learn (lamad)","action",_P,"learn","external:god","v71: 'It is good for me that I was afflicted, that I might LEARN your statutes' - affliction valued as the school of learning."),
 ('H3925',73):("learn (lamad)","action",_P,"learn","external:god","v73: 'give me understanding that I may LEARN your commandments' - learning as the aim of the understanding sought."),
 # UNDERSTAND (I understand)
 ('H0995',95):("understand / ponder (bin)","action",_P,"consider","external:god","v95: 'The wicked lie in wait to destroy me, but I UNDERSTAND (ponder) your testimonies' - pondering the word as refuge from the wicked's ambush."),
 ('H0995',100):("understand (bin)","disposition",_P,"understand","external:god","v100: 'I UNDERSTAND more than the aged, for I keep your precepts' - understanding beyond the elders, born of keeping."),
 ('H0995',104):("get understanding (bin)","disposition",_P,"gain understanding","external:god","v104: 'Through your precepts I get UNDERSTANDING; therefore I hate every false way' - understanding from the precepts that breeds hatred of falsehood."),
 # SEEK
 ('H1875',2):("seek (darash)","action",_P,"seek","external:god","v2: 'Blessed are those who keep his testimonies, who SEEK him with their whole heart' - the whole-hearted seeking of God."),
 ('H1875',10):("seek (darash)","action",_P,"seek","external:god","v10: 'With my whole heart I SEEK you; let me not wander from your commandments' - the whole heart's seeking, guarded from straying."),
 ('H1875',45):("seek (darash)","action",_P,"seek","external:god","v45: 'I shall walk in a wide place, for I have SOUGHT your precepts' - the sought precepts that open a wide place."),
 ('H1875',94):("seek (darash)","action",_P,"seek","external:god","v94: 'I am yours; save me, for I have SOUGHT your precepts' - the seeking pleaded as ground for salvation."),
 ('H1875',155):("seek (darash, negated)","disposition","the wicked","fail to seek","external:god","v155: 'Salvation is far from the wicked, for they do not SEEK your statutes' - the wicked's failure to seek, cause of their distance from salvation."),
 # WALK
 ('H1980',1):("walk (halak)","action","the blameless","walk","external:god","v1: 'Blessed are those whose way is blameless, who WALK in the law of the LORD!' - the blessed who walk in the law."),
 ('H1980',3):("walk (halak)","action","the blameless","walk","external:god","v3: 'who also do no wrong, but WALK in his ways!' - walking in God's ways, doing no wrong."),
 ('H1980',45):("walk (halak)","action",_P,"walk","external:god","v45: 'I shall WALK in a wide place, for I have sought your precepts' - walking freely in the wide place the word gives."),
 # KNOW
 ('H3045',75):("know (yada)","disposition",_P,"know","external:god","v75: 'I KNOW, O LORD, that your rules are righteous, and that in faithfulness you have afflicted me' - the settled knowledge that God's afflicting is righteous."),
 ('H3045',79):("know (yada)","disposition","those who fear God","know","external:god","v79: 'Let those who fear you turn to me, that they may KNOW your testimonies' - the God-fearers who come to know the testimonies."),
 ('H3045',125):("know (yada)","disposition",_P,"know","external:god","v125: 'I am your servant; give me understanding, that I may KNOW your testimonies!' - the knowing sought through understanding."),
 ('H3045',152):("know (yada)","disposition",_P,"know","external:god","v152: 'Long have I KNOWN from your testimonies that you have founded them forever' - the long-held knowledge of the testimonies' permanence."),
 # LONGS / failing eyes
 ('H3615',81):("long / faint (kalah)","state",_P,"long / faint","internal:ib-state","v81: 'My soul LONGS (faints) for your salvation; I hope in your word' - the self fainting with longing for salvation."),
 ('H3615',82):("long / fail (kalah)","state",_P,"long / fail (of the eyes)","internal:ib-state","v82: 'My eyes LONG (fail) for your promise; I ask, When will you comfort me?' - the eyes worn out watching for the promise."),
 ('H3615',87):("be near ended (kalah)","state",_P,"be almost destroyed","internal:ib-state","v87: 'They had almost made an END of me on earth, but I have not forsaken your precepts' - the near-destruction endured without forsaking the word."),
 ('H3615',123):("long / fail (kalah)","state",_P,"long / fail (of the eyes)","internal:ib-state","v123: 'My eyes LONG (fail) for your salvation and for the fulfilment of your righteous promise' - the eyes failing in the wait for salvation."),
 # HATE (of evil)
 ('H8130',104):("hate (sane)","disposition",_P,"hate","internal:ib-state","v104: 'Through your precepts I get understanding; therefore I HATE every false way' - hatred of falsehood as the fruit of understanding."),
 ('H8130',113):("hate (sane)","disposition",_P,"hate","internal:ib-state","v113: 'I HATE the double-minded, but I love your law' - hatred of the divided heart, set against love of the law."),
 ('H8130',128):("hate (sane)","disposition",_P,"hate","internal:ib-state","v128: 'I consider all your precepts to be right; I HATE every false way' - hatred of the false way, counterpart to esteeming the precepts."),
 ('H8130',163):("hate (sane)","disposition",_P,"hate","internal:ib-state","v163: 'I HATE and abhor falsehood, but I love your law' - hatred of falsehood, the negative face of love for the law."),
 # AFFLICTED / affliction
 ('H6031',67):("be afflicted (anah)","state",_P,"be afflicted","internal:ib-state","v67: 'Before I was AFFLICTED I went astray, but now I keep your word' - affliction that turned him from straying to keeping."),
 ('H6031',71):("be afflicted (anah)","state",_P,"be afflicted","internal:ib-state","v71: 'It is good for me that I was AFFLICTED, that I might learn your statutes' - affliction owned as good, the teacher of the statutes."),
 ('H6031',75):("be afflicted (anah)","state",_P,"be afflicted","internal:ib-state","v75: 'in faithfulness you have AFFLICTED me' - affliction received as God's faithful dealing."),
 ('H6031',107):("be afflicted (anah)","state",_P,"be severely afflicted","internal:ib-state","v107: 'I am severely AFFLICTED; give me life, O LORD, according to your word!' - deep affliction pleading for revival."),
 ('H6040',50):("affliction (oni)","state",_P,"suffer affliction","internal:ib-state","v50: 'This is my comfort in my AFFLICTION, that your promise gives me life' - affliction comforted by the life-giving promise."),
 ('H6040',92):("affliction (oni)","state",_P,"suffer affliction","internal:ib-state","v92: 'If your law had not been my delight, I would have perished in my AFFLICTION' - affliction survived only by delight in the law."),
 ('H6040',153):("affliction (oni)","state",_P,"suffer affliction","internal:ib-state","v153: 'Look on my AFFLICTION and deliver me, for I do not forget your law' - affliction laid before God with the plea to deliver."),
 # FEAR of God
 ('H3372',63):("fear (yare)","disposition","those who fear God","fear / revere","external:god","v63: 'I am a companion of all who FEAR you, of those who keep your precepts' - fellowship with the God-fearing keepers."),
 ('H3372',120):("fear (yare)","state",_P,"tremble in fear","external:god","v120: 'My flesh trembles for FEAR of you, and I am afraid of your judgments' - the body itself trembling in awe of God."),
 ('H3373',74):("fear (yare)","disposition","those who fear God","fear / revere","external:god","v74: 'Those who FEAR you shall see me and rejoice, because I have hoped in your word' - the God-fearers gladdened by his hope."),
 ('H3373',79):("fear (yare)","disposition","those who fear God","fear / revere","external:god","v79: 'Let those who FEAR you turn to me, that they may know your testimonies' - the reverent whose fellowship he seeks."),
 ('H6342',161):("stand in awe (pachad)","state",_P,"stand in awe","external:god","v161: 'Princes persecute me without cause, but my heart stands in AWE of your words' - the heart's awe of the word amid persecution."),
 ('H6343',120):("be afraid (pachad)","state",_P,"be afraid","external:god","v120: 'and I am AFRAID of your judgments' - dread of God's judgments joined to the trembling flesh."),
 # CLING
 ('H1692',25):("cling (dabaq)","state",_P,"cling to the dust","internal:ib-state","v25: 'My soul CLINGS to the dust; give me life according to your word!' - the self clinging low in the dust, pleading revival."),
 ('H1692',31):("cling (dabaq)","action",_P,"cling to the testimonies","external:god","v31: 'I CLING to your testimonies, O LORD; let me not be put to shame!' - clinging fast to the word against shame."),
 # TURN (my feet / the fearers)
 ('H7725',59):("turn (shuv)","action",_P,"turn the feet","external:god","v59: 'When I think on my ways, I TURN my feet to your testimonies' - reflection that redirects the feet to the word."),
 ('H7725',79):("turn (shuv)","action","those who fear God","turn to the psalmist","external:person","v79: 'Let those who fear you TURN to me' - the God-fearers turning to join him."),
 # STRAY / WANDER
 ('H7686',10):("wander (shagah, negated)","disposition",_P,"not wander","external:god","v10: 'let me not WANDER from your commandments' - the plea to be kept from straying."),
 ('H7686',21):("wander (shagah)","disposition","the insolent","wander","external:god","v21: 'the insolent, accursed ones, who WANDER from your commandments' - the proud who stray from the law."),
 ('H7686',118):("go astray (shagah)","disposition","the strayers","go astray","external:god","v118: 'You spurn all who GO ASTRAY from your statutes' - the strayers God rejects."),
 ('H8582',110):("stray (taah, negated)","disposition",_P,"not stray","external:god","v110: 'The wicked have laid a snare for me, but I do not STRAY from your precepts' - not straying though snared."),
 ('H8582',176):("go astray (taah)","state",_P,"go astray like a lost sheep","external:god","v176: 'I have gone ASTRAY like a lost sheep; seek your servant' - the closing confession of straying, the plea to be sought."),
 ('H7683',67):("go astray (shagag)","state",_P,"go astray","external:god","v67: 'Before I was afflicted I WENT ASTRAY' - the straying of the unafflicted, corrected by affliction."),
 # CHOSEN
 ('H0977',30):("choose (bachar)","action",_P,"choose the way of faithfulness","external:god","v30: 'I have CHOSEN the way of faithfulness; I set your rules before me' - the deliberate choice of the faithful way."),
 ('H0977',173):("choose (bachar)","action",_P,"choose the precepts","external:god","v173: 'Let your hand be ready to help me, for I have CHOSEN your precepts' - the chosen precepts pleaded as ground for help."),
 # LONG (taab)
 ('H8373',40):("long (taab)","disposition",_P,"long","external:god","v40: 'Behold, I LONG for your precepts; in your righteousness give me life!' - longing for the precepts joined to the plea for life."),
 ('H8373',174):("long (taab)","disposition",_P,"long","external:god","v174: 'I LONG for your salvation, O LORD, and your law is my delight' - longing for salvation, the law still the delight."),
 # PRAISE
 ('H3034',7):("praise (yadah)","action",_P,"praise","external:god","v7: 'I will PRAISE you with an upright heart, when I learn your righteous rules' - praise resolved as learning grows."),
 ('H3034',62):("praise (yadah)","action",_P,"praise","external:god","v62: 'At midnight I rise to PRAISE you, because of your righteous rules' - the midnight praise stirred by God's just rules."),
 ('H1984',164):("praise (halal)","action",_P,"praise","external:god","v164: 'Seven times a day I PRAISE you for your righteous rules' - praise offered seven times daily, ceaseless."),
 ('H1984',175):("praise (halal)","action",_P,"praise","external:god","v175: 'Let my soul live and PRAISE you, and let your rules help me' - the plea to live for praise."),
 ('H8416',171):("praise (tehillah)","action",_P,"pour forth praise","external:god","v171: 'My lips will pour forth PRAISE, for you teach me your statutes' - praise overflowing the lips as God teaches."),
 # CRY
 ('H7121',145):("cry / call (qara)","action",_P,"cry","external:god","v145: 'With my whole heart I CRY; answer me, O LORD!' - the whole heart's cry for answer."),
 ('H7121',146):("call (qara)","action",_P,"call","external:god","v146: 'I CALL to you; save me, that I may keep your testimonies' - calling for salvation to keep the word."),
 ('H7440',169):("cry (rinnah)","action",_P,"cry","external:god","v169: 'Let my CRY come before you, O LORD; give me understanding according to your word!' - the cry brought before God for understanding."),
 ('H7768',147):("cry for help (shava)","action",_P,"cry for help","external:god","v147: 'I rise before dawn and CRY for help; I hope in your words' - the pre-dawn cry, hoping in the word."),
 # REMEMBER (I remember)
 ('H2142',52):("remember (zakar)","action",_P,"remember","external:god","v52: 'When I think of your rules from of old, I take comfort, O LORD (I REMEMBER them)' - memory of God's ancient rules bringing comfort."),
 ('H2142',55):("remember (zakar)","action",_P,"remember","external:god","v55: 'I REMEMBER your name in the night, O LORD, and keep your law' - remembering God's name through the night."),
 # FORSAKE (foes/psalmist)
 ('H5800',53):("forsake (azab)","action","the wicked","forsake the law","external:god","v53: 'Hot indignation seizes me because of the wicked, who FORSAKE your law' - the wicked's forsaking of the law that fires his indignation."),
 ('H5800',87):("forsake (azab, negated)","disposition",_P,"not forsake","external:god","v87: 'They had almost made an end of me... but I have not FORSAKEN your precepts' - holding to the precepts though nearly destroyed."),
 # --- singletons ---
 ('H6466',3):("do no wrong (paal)","action","the blameless","do no wrong","internal:ib-state","v3: 'who also DO no wrong, but walk in his ways!' - the blameless who commit no wrong."),
 ('H3476',7):("upright (yashar)","disposition",_P,"be upright","internal:ib-state","v7: 'I will praise you with an UPRIGHT heart' - the straightness of heart in which praise is offered."),
 ('H3824',7):("heart (lebab)","faculty",_P,"praise with an upright heart","internal:ib-state","v7: 'I will praise you with an upright HEART' - the inner self, upright, engaged in praise."),
 ('H6845',11):("store up (tsaphan)","action",_P,"treasure the word","internal:ib-state","v11: 'I have STORED UP your word in my heart, that I might not sin against you' - the word treasured within as a guard against sin."),
 ('H2398',11):("sin (chata, negated)","disposition",_P,"not sin","external:god","v11: 'that I might not SIN against you' - the sin the treasured word guards against."),
 ('H1288',12):("bless (barak)","action",_P,"bless God","external:god","v12: 'BLESSED are you, O LORD; teach me your statutes!' - the psalmist blessing God as he asks to be taught."),
 ('H7737',30):("set (shavah)","action",_P,"set the rules before oneself","external:god","v30: 'I have chosen the way of faithfulness; I SET your rules before me' - the deliberate setting of God's rules before the eyes."),
 ('H7323',32):("run (ruts)","action",_P,"run in the way","external:god","v32: 'I will RUN in the way of your commandments when you enlarge my heart!' - the eager running once the heart is freed."),
 ('H3374',38):("be feared (yirah)","disposition",_P,"revere God","external:god","v38: 'Confirm to your servant your promise, that you may be FEARED' - the reverence the confirmed promise is meant to produce."),
 ('H3025',39):("dread (yagor)","state",_P,"dread reproach","internal:ib-state","v39: 'Turn away the reproach that I DREAD, for your rules are good' - the reproach the psalmist fears, from which he seeks relief."),
 ('H2778',42):("taunt (charaph)","action","the taunter","taunt","external:person","v42: 'then shall I have an answer for him who TAUNTS me, for I trust in your word' - the taunter answered by the psalmist's trust."),
 ('H0982',42):("trust (batach)","disposition",_P,"trust","external:god","v42: 'for I TRUST in your word' - trust in the word that arms him against the taunter."),
 ('H5375',48):("lift up (nasa)","action",_P,"lift up the hands","external:god","v48: 'I will LIFT UP my hands toward your commandments, which I love' - the lifted hands of devotion toward the loved commandments."),
 ('H5165',50):("comfort (nechamah)","state",_P,"be comforted","internal:ib-state","v50: 'This is my COMFORT in my affliction, that your promise gives me life' - the consolation the promise brings in affliction."),
 ('H3887',51):("deride (luts)","action","the insolent","deride","external:person","v51: 'The insolent utterly DERIDE me, but I do not turn away from your law' - the derision of the proud, unable to turn him from the law."),
 ('H0270',53):("seize (achaz)","state",_P,"be seized with indignation","internal:ib-state","v53: 'Hot indignation SEIZES me because of the wicked' - the zeal-indignation that grips him at the wicked's lawlessness."),
 ('H2470',58):("entreat (chalah)","action",_P,"entreat God's favour","external:god","v58: 'I ENTREAT your favour with all my heart; be gracious to me according to your promise' - the whole-hearted entreaty for grace."),
 ('H2803',59):("think / consider (chashab)","action",_P,"consider one's ways","internal:ib-state","v59: 'When I THINK on my ways, I turn my feet to your testimonies' - the self-examination that redirects the feet."),
 ('H2363',60):("hasten (chush)","action",_P,"hasten to obey","external:god","v60: 'I HASTEN and do not delay to keep your commandments' - the promptness of obedience."),
 ('H4102',60):("delay (mahah, negated)","disposition",_P,"not delay","external:god","v60: 'I hasten and do not DELAY to keep your commandments' - obedience without procrastination."),
 ('H0539',66):("believe (aman)","disposition",_P,"believe","external:god","v66: 'Teach me good judgment and knowledge, for I BELIEVE in your commandments' - faith in the commandments as ground for the plea to be taught."),
 ('H2459',70):("unfeeling (tapash)","status","the insolent","have an unfeeling heart","internal:ib-state","v70: 'their heart is UNFEELING like fat, but I delight in your law' - the gross insensibility of the foes' heart."),
 ('H8055',74):("rejoice (samach)","state","those who fear God","rejoice","internal:ib-state","v74: 'Those who fear you shall see me and REJOICE, because I have hoped in your word' - the God-fearers' joy at his hope."),
 ('H5791',78):("wrong (avath)","action","the insolent","wrong the psalmist","external:person","v78: 'Let the insolent be put to shame, because they have WRONGED me with falsehood' - the wrong done by the proud with lies."),
 ('H6960',95):("lie in wait (qavah)","action","the wicked","lie in wait","external:person","v95: 'The wicked LIE IN WAIT to destroy me, but I ponder your testimonies' - the ambush of the wicked, met by pondering the word."),
 ('H2449',98):("be wise (chakam)","disposition",_P,"be made wiser","internal:ib-state","v98: 'Your commandment makes me WISER than my enemies, for it is ever with me' - the wisdom the ever-present commandment gives."),
 ('H7919',99):("have understanding (sakal)","disposition",_P,"have understanding","internal:ib-state","v99: 'I have MORE UNDERSTANDING than all my teachers, for your testimonies are my meditation' - understanding beyond teachers from meditation."),
 ('H3607',101):("hold back (kala)","action",_P,"hold back the feet from evil","external:god","v101: 'I HOLD BACK my feet from every evil way, in order to keep your word' - restraining the feet from evil to keep the word."),
 ('H8342',111):("joy (sason)","state",_P,"rejoice in the testimonies","internal:ib-state","v111: 'Your testimonies are my heritage forever, for they are the JOY of my heart' - the testimonies as the heart's very joy."),
 ('H5588',113):("double-minded (seeph)","status","the double-minded","be divided in heart","internal:ib-state","v113: 'I hate the DOUBLE-MINDED, but I love your law' - the divided-hearted, object of the psalmist's hatred."),
 ('H7489',115):("evildoers (raa)","status","the evildoers","do evil","external:person","v115: 'Depart from me, you EVILDOERS, that I may keep the commandments of my God' - the evildoers put away so the word may be kept."),
 ('H0205',133):("iniquity (aven)","state",_P,"resist iniquity's dominion","internal:ib-state","v133: 'Keep steady my steps according to your promise, and let no INIQUITY get dominion over me' - the iniquity the psalmist begs not to be ruled by."),
 ('H7068',139):("zeal (qinah)","state",_P,"be consumed with zeal","internal:ib-state","v139: 'My ZEAL consumes me, because my foes forget your words' - the zeal for God's word that consumes him at the foes' forgetting."),
 ('H0959',141):("be despised (bazah)","state",_P,"be small and despised","internal:ib-state","v141: 'I am small and DESPISED, yet I do not forget your precepts' - the low, despised estate held with unbroken memory."),
 ('H4689',143):("anguish (matsoq)","state",_P,"be in anguish","internal:ib-state","v143: 'Trouble and ANGUISH have found me out, but your commandments are my delight' - anguish overtaken, yet delight unshaken."),
 ('H6473',131):("open the mouth (paar)","action",_P,"open the mouth in longing","internal:ib-state","v131: 'I OPEN my mouth and pant, because I long for your commandments' - the mouth opened wide in yearning for the word."),
 ('H7602',131):("pant (shaaph)","state",_P,"pant with longing","internal:ib-state","v131: 'I open my mouth and PANT, because I long for your commandments' - the panting of desire for the commandments."),
 ('H2968',131):("long (yaab)","disposition",_P,"long","external:god","v131: 'because I LONG for your commandments' - the longing that opens the mouth to pant."),
 ('H0898',158):("faithless (bagad)","status","the faithless","deal faithlessly","external:person","v158: 'I look at the FAITHLESS with disgust, because they do not keep your commands' - the treacherous who spurn God's commands."),
 ('H6962',158):("disgust (qut)","state",_P,"be filled with disgust","internal:ib-state","v158: 'I look at the faithless with DISGUST, because they do not keep your commands' - the revulsion at the faithless."),
 ('H8581',163):("abhor (taab)","disposition",_P,"abhor falsehood","internal:ib-state","v163: 'I hate and ABHOR falsehood, but I love your law' - the abhorrence of falsehood joined to hatred of it."),
 ('H0935',170):("come before (bo)","action",_P,"let the plea come before God","external:god","v170: 'Let my plea COME before you; deliver me according to your word' - the supplication brought into God's presence."),
 ('H6231',121):("oppressors (ashaq)","action","the oppressors","oppress","external:person","v121: 'I have done what is just and right; do not leave me to my OPPRESSORS' - the oppressors from whom he seeks not to be abandoned."),
 ('H6231',122):("oppress (ashaq)","action","the insolent","oppress","external:person","v122: 'Give your servant a pledge of good; let not the insolent OPPRESS me' - the oppression the psalmist seeks surety against."),
 ('H8549',1):("blameless (tamim)","disposition","the blameless","be blameless in the way","internal:ib-state","v1: 'Blessed are those whose way is BLAMELESS, who walk in the law of the LORD!' - the whole, blameless way of the blessed."),
 ('H8549',80):("blameless (tamim)","disposition",_P,"be blameless in heart","internal:ib-state","v80: 'May my heart be BLAMELESS in your statutes, that I may not be put to shame!' - the plea for a blameless heart."),
 ('H0835',1):("blessed (esher)","state","the blameless","be blessed","internal:ib-state","v1: 'BLESSED are those whose way is blameless' - the beatitude opening the psalm."),
 ('H0835',2):("blessed (esher)","state","those who keep","be blessed","internal:ib-state","v2: 'BLESSED are those who keep his testimonies, who seek him with their whole heart' - the beatitude on the whole-hearted keepers."),
 ('H1811',28):("melt away (dalaph)","state",_P,"melt away for sorrow","internal:ib-state","v28: 'My soul MELTS AWAY for sorrow; strengthen me according to your word!' - the self dissolving in grief, seeking strength."),
 ('H5493',102):("turn aside (sur, negated)","disposition",_P,"not turn aside from the rules","external:god","v102: 'I do not TURN ASIDE from your rules, for you have taught me' - not swerving from the rules God himself taught."),
 ('H5493',115):("depart / put away (sur)","action",_P,"put the evildoers away","external:person","v115: 'DEPART from me, you evildoers, that I may keep the commandments of my God!' - the separation from evildoers the psalmist enacts to keep the word."),
}
for (ps,v),(sense,typ,bearer,op,loc,note) in CHARS.items():
    sid=next((x['sid'] for x in CANDS if x['v']==v and x['ps']==ps), None)
    if sid and sid not in CH:
        tgt="God's word" if loc=="external:god" else ("the psalmist" if loc=="external:person" else "none")
        ch(sid,sense,typ,bearer,op,tgt,"paired within its char-arc across the psalm",loc,note)

# =========================================================================
# BUILD + coverage report (does NOT write until coverage complete unless --write)
# =========================================================================
def buildrole(x):
    """return ('char'|'qual'|'stand', payload) for a candidate not in CH"""
    ps=x['ps']; key=(ps,x['v'])
    if key in QOVR: return ('qual', QOVR[key])
    if key in SOVR: return ('stand', SOVR[key])
    if ps in WORD: return ('qual', WORD[ps])
    if ps in GODACT: return ('qual', GODACT[ps])
    if ps in STAND: return ('stand', STAND[ps])
    return (None,None)

authored=set(CH)
remaining=[x for x in CANDS if x['sid'] not in authored and buildrole(x)[0] is None]
from collections import Counter
print(f"Ps119 candidates: {len(CANDS)} | authored chars: {len(CH)} | auto-classified: {sum(1 for x in CANDS if x['sid'] not in authored and buildrole(x)[0])} | REMAINING to author: {len(remaining)}")
print("Remaining char-lemmas to author (ps x count : verses):")
rem=Counter(x['ps'] for x in remaining)
for ps,n in rem.most_common():
    vs=sorted(x['v'] for x in remaining if x['ps']==ps)
    print(f"  ({ps}) x{n:2}  v={vs}  e.g. {next(x['surf'] for x in remaining if x['ps']==ps)!r}")

# ---- write the JSON when fully covered ----
if not remaining:
    r=Reading("Psa",19,119,
      note="Ps119 acrostic (176v, 641 spans). Read CHAR-BY-CHAR (each recurring disposition read across the whole psalm as one arc), NOT by the 22 alphabetic stanzas. CHARACTERISTICS = the psalmist's dispositions/acts toward God's word (keep/love/delight/meditate/hope/heart/soul/forget-not/seek/walk/learn/understand/fear/cling/long/praise/cry + the foes insolent/wicked/false/put-to-shame) - each occurrence read for its distinct verse-nuance. QUALIFIERS = the word-synonyms (law/testimonies/precepts/statutes/commandments/rules/word/promise/faithfulness) + God-acts petitioned (revive/teach/give-understanding/redeem/uphold...), source-linked to that verse's anchor disposition. STANDALONE = temporal/imagery (forever/lamp/honey/gold/way).")
    anchor={}
    for x in sorted(CANDS,key=lambda z:z['sid']):
        if x['sid'] in CH and x['v'] not in anchor: anchor[x['v']]=x['sid']
    FALLBACK=sorted(CH)[0]
    for x in CANDS:
        sid=x['sid']
        if sid in CH:
            d=CH[sid]
            r.ch(sid,d['sense'],d['typ'],d['bearer'],d['op'],d['target'],d['coupling'],d['locus'],d['note'])
        else:
            role,sense=buildrole(x)
            if role=='qual':
                asid=anchor.get(x['v'],FALLBACK)
                r.qu(sid,sense,asid,f"v{x['v']}: '{x['surf']}' - God's {sense}; the revelation/act the psalmist's disposition engages in this verse. Qualifier.")
            else:
                r.st(sid,sense,f"v{x['v']}: '{x['surf']}' - {sense}; image/temporal. Standalone.")
    r.write()
