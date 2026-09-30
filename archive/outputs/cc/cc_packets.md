# CC verse-read packets — M02 — 7 verses

INSTRUCTIONS — produce one @@@…@@@END record per WRITE-term, in this exact format and field discipline:

You are doing VERSE-LEVEL MEANING extraction for an academic study of Scripture's vocabulary for the inner life of mankind. You read one verse at a time and, for each in-scope inner-life TERM in that verse, you extract a structured record and then write a short MEANING PARAGRAPH.

CORE DISCIPLINE
- "Characteristic" = the typed term-in-verse you are examining (e.g. THIS ya.re here), NOT a cluster label.
- STATE, NEVER INDUCE. If the verse does not resolve a field, output the null token (NONE / SILENT / not-stated). Silence is a first-class, significant finding. Do NOT guess, infer beyond the verse, or import doctrine.
- Read the verse in its own context; use the term's sense options only to disambiguate, not to override the verse.
- Option-list fields MUST use one of the listed values exactly.

FIELDS (per term-in-verse)
- sense_applied: the verse-specific sense of the term (short phrase).
- type: one of action | status | quality
- compound: simple  OR  compound:<parts>
- mode: the operative mode/stem nuance in this verse (short), or NONE
- constitutional_location: multi, comma-sep from {spirit, soul, heart, mind, body} or NONE  (only if the verse locates it there)
- origin: one of within-person | received-from-outside | bestowed-by-God | carried-generationally | from-other-spirits | not-stated
- faculty: multi, comma-sep from {perception, cognition, memory, affect, creativity, volition, agency, moral-evaluation, conscience, relational} or NONE  (which inner faculty the term engages here, from its meaning)
- attributed_to_God: yes | no   (is the term predicated of / related to God in THIS verse)
- purpose_equips: what the verse says it equips the person to be/do/become, or not-stated
- typology_direction: human->divine | divine->human | none
- immediate_response: the first inner response shown in the verse, or SILENT
- produces_effect: what it produces in the inner being here, or not-stated
- relational_implication: directional/relational force the term carries here, or not-stated
- literary_setting: the literary form of the verse (narrative | poetry | law | prophecy | wisdom | epistle | ...)

OUTPUT FORMAT — for EACH (verse, term) pair, emit exactly:
@@@ <reference> | <term_translit> | vcid=<vcid>
sense_applied: ...
type: ...
compound: ...
mode: ...
constitutional_location: ...
origin: ...
faculty: ...
attributed_to_God: ...
purpose_equips: ...
typology_direction: ...
immediate_response: ...
produces_effect: ...
relational_implication: ...
literary_setting: ...
MEANING: <2-4 sentence paragraph that collates the fields above into the meaning of this term in THIS verse's context. Every non-null field above must be reflected in the paragraph.>
SELFAUDIT: <comma-list of any field name NOT represented in MEANING, or "OK">
@@@END

Process every (verse, term) pair given. Use the exact vcid supplied. No preamble, no other text.

Embed the QUALIFIERS-PRESENT (T2) force into the relevant WRITE-term meaning; do NOT emit records for them.
============================================================

@@@VERSE 1Ti 6:4
TEXT: 1Ti 6:4 he is puffed up with conceit and understands nothing . He has an unhealthy craving for controversy and for quarrels about words , which produce envy , dissension , slander , evil suspicions ,
WRITE:
  - phthonos (G5355) cluster=M28 vcid=14239 morph=N-NSM stem=-
      senses: envy, jealously, spite, Mt. 27:18; Mk. 15:10; Rom. 1:29; Gal. 5:21; Phil. 1:15; 1Tim. 6:4; Tit. 3:3; Jas. 4:5; 1Pet. 2:1*
  - ponēros (G4190) cluster=M10b vcid=14470 morph=A-NPF stem=-
      senses: bad, the negative quality of an object; evil, wicked, crime, the negative moral quality of a person or action opposed to God and his goodness; (n.) wicked deed, wicked thing; the Evil One, a title of Satan 
bad, unsound, Mt. 6:23; 7:17, 18; evil, afflictive, wicked Eph. 5:16; 6:13; Rev. 16:2; evil, wrongful, malignant, malevolent, Mt. 5:11, 39; Acts 28:21; evil, wicked, impious, and τὸ πονηρόν, evil, wrong, wickedness, Mt. 5:37, 45; 9:4; slothful, inactive, Mt. 25:26; Lk. 19:22; ὁ πονηρός, the evil one, the devil, Mt. 13:19, 38; Jn. 17:15; evil eye, i.q. φθονερός envious, Mt. 20:15; Mk. 7:22; implication covetous, Mt. 7:11
  - tufoō (G5187) cluster=M08 vcid=33925 morph=V-RPI-3S stem=-
      senses: (passive) to be or become conceited, implying foolishness 
to besmoke;, metaphorically to possess with the fumes of conceit; passive to be demented with conceit, puffed up, 1Tim. 3:6; 6:4; 2Tim. 3:4; 1Tim. 6:4*
  - blasfēmia (G0988) cluster=M10 vcid=37622 morph=N-NPF stem=-
      senses: blasphemy, slander, malicious talk 
slander, railing, reproach, malicious talk Mt. 15:19; Mk. 7:22; blasphemy, Mt. 12:31; 26:65
  - eris (G2054) cluster=M02 vcid=38078 morph=N-NSF stem=-
      senses: quarrel, strife, dissension, discord 
altercation, strife, Rom. 13:13; contentious disposition, Rom. 1:29; Phil. 1:15
  - logomachia (G3055) cluster=M02 vcid=38082 morph=N-APF stem=-
      senses: quarrel about words 
contention, or strife about words; by implication a dispute about trivial things, unprofitable controversy, 1Tim. 6:4*
  - noseō (G3552) cluster=M24 vcid=54958 morph=V-PAP-NSM stem=-
      senses: to be unhealthy, ill sick 
to be sick;, metaphorically to have a diseased appetite or craving for a thing, have an excessive and vicious fondness for a thing, 1Tim. 6:4*

@@@VERSE Phili 1:15
TEXT: Phili 1:15 Some indeed preach Christ from envy and rivalry , but others from good will .
WRITE:
  - eudokia (G2107) cluster=M39 vcid=9810 morph=N-ASF stem=-
      senses: goodwill, good purpose, favor, pleasure, desire 
good will, favor, Lk. 2:14; good pleasure, purpose, intention, Mt. 11:26; Lk. 10:21; Eph. 1:5, 9; Phil. 2:13; by implication desire, Rom. 10:1; Phil. 1:15; 2Thess. 1:11*
  - phthonos (G5355) cluster=M28 vcid=14238 morph=N-ASM stem=-
      senses: envy, jealously, spite, Mt. 27:18; Mk. 15:10; Rom. 1:29; Gal. 5:21; Phil. 1:15; 1Tim. 6:4; Tit. 3:3; Jas. 4:5; 1Pet. 2:1*
  - eris (G2054) cluster=M02 vcid=38079 morph=N-ASF stem=-
      senses: quarrel, strife, dissension, discord 
altercation, strife, Rom. 13:13; contentious disposition, Rom. 1:29; Phil. 1:15

@@@VERSE Tit 3:9
TEXT: Tit 3:9 But avoid foolish controversies , genealogies , dissensions , and quarrels about the law , for they are unprofitable and worthless .
WRITE:
  - mōros (G3474) cluster=M16 vcid=17441 morph=A-APF stem=-
      senses: primarily dull; foolish, Mt. 7:26; 23:17; 25:2f., 8; 1Cor. 1:25, 27; 3:18; 4:10; 2Tim. 2:23; Tit. 3:9; from the Hebrew, a fool in senseless wickedness, Mt. 5:22*
  - eris (G2054) cluster=M02 vcid=38080 morph=N-APF stem=-
      senses: quarrel, strife, dissension, discord 
altercation, strife, Rom. 13:13; contentious disposition, Rom. 1:29; Phil. 1:15

@@@VERSE Pro 17:19
TEXT: Pro 17:19 Whoever loves transgression loves strife ; he who makes his door high seeks destruction .
WRITE:
  - ba.qash (H1245) cluster=M41 vcid=10510 morph=HVprmsa stem=Piel
      senses: to seek, require, desire, exact, request | (Piel) | to seek to find
  - ga.vah (H1361) cluster=M08 vcid=34055 morph=HVhrmsa stem=Hiphil
      senses: to be high, be exalted | (Qal) | to be high, lofty, tall
  - pe.sha (H6588) cluster=M10 vcid=35697 morph=HNcmsa stem=-
      senses: transgression, rebellion | transgression (against individuals) | transgression (nation against nation)
  - mats.tsah (H4683) cluster=M02 vcid=38084 morph=HNcfsa stem=-
      senses: strife, contention

@@@VERSE Isa 41:12
TEXT: Isa 41:12 You shall seek those who contend with you, but you shall not find them; those who war against you shall be as nothing at all .
WRITE:
  - ba.qash (H1245) cluster=M41 vcid=10567 morph=HVpi2ms stem=Piel
      senses: to seek, require, desire, exact, request | (Piel) | to seek to find
  - mats.tsut (H4695) cluster=M02 vcid=38086 morph=HNcfsc stem=-
      senses: strife, contention

@@@VERSE 1Ki 20:43
TEXT: 1Ki 20:43 And the king of Israel went to his house vexed and sullen and came to Samaria .
WRITE:
  - za.eph (H2198) cluster=M02 vcid=46133 morph=HAamsa stem=-
      senses: angry, raging, out of humour, vexed

@@@VERSE 1Ki 21:4
TEXT: 1Ki 21:4 And Ahab went into his house vexed and sullen because of what Naboth the Jezreelite had said to him, for he had said , “I will not give you the inheritance of my fathers .” And he lay down on his bed and turned away his face and would eat no food .
WRITE:
  - za.eph (H2198) cluster=M02 vcid=46132 morph=HAamsa stem=-
      senses: angry, raging, out of humour, vexed
