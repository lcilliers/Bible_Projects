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

# =========================================================================
# BUILD + coverage report (does NOT write until coverage complete unless --write)
# =========================================================================
def buildrole(x):
    """return ('char'|'qual'|'stand', payload) for a candidate not in CH"""
    ps=x['ps']
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
