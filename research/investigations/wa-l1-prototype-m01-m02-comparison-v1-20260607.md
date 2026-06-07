# L1-mechanical prototype — comparison: M01, M02

> READ-ONLY (`scripts/_prototype_l1_mechanical.py`). Runs the **mechanical** part of L1 from STEP sense data: R2 single/multi-sense detection, R4 keyword capture, R6 pole. DB-only (morphology / R7 stem-narrow is a separate pass). Purpose: resolve R2/R4/R6 and compare clusters before V3_2.

## Comparison summary

| Metric | M01 | M02 |
|---|---|---|
| Terms | 83 | 44 |
|   Hebrew / Greek | 65 / 18 | 29 / 15 |
| Single-sense terms | 69 (83%) | 31 (70%) |
| Multi-sense terms | 14 (16%) | 13 (29%) |
| Relevant verses | 945 | 645 |
|   on single-sense terms | 477 (50%) | 232 (35%) |
|   on multi-sense terms | 468 (49%) | 413 (64%) |
| Pole-span terms (inner+phys/ext) | 12 | 7 |
|   touch physical pole | 12 | 6 |
|   touch external pole | 0 | 1 |

**Read:** single-sense terms → meaning assigned mechanically at L1 (done). Multi-sense + pole-span terms → need stem-narrow (R7) and/or per-verse select (the L2 residue). The verse-weighted multi-sense % is the true size of the 'needs analysis' load.

## M01 (Fear) — per-term

### Pole-span terms (the cross-pole cases to watch)

| Term | Gloss | Lang | Poles | Why multi | Verses |
|---|---|---|---|---|---|
| H3372G ya.re | to fear: revere | Hebrew | inner/physical | 3 stems; pole-span:inner/physical | 191 |
| H3372H ya.re | to fear: revere | Hebrew | inner/physical | 3 stems; pole-span:inner/physical | 107 |
| H2729 cha.rad | to tremble | Hebrew | inner/physical | 2 stems; pole-span:inner/physical | 34 |
| H6342 pa.chad | to dread | Hebrew | inner/physical | 3 stems; pole-span:inner/physical | 25 |
| H2865 cha.tat | to to be dismayed | Hebrew | inner/physical | 4 stems; pole-span:inner/physical | 24 |
| H7264 ra.gaz | to tremble | Hebrew | inner/physical | 3 stems; pole-span:inner/physical | 20 |
| H6206 a.rats | to tremble | Hebrew | inner/physical | 3 stems; pole-span:inner/physical | 15 |
| H4288 me.chit.tah | terror | Hebrew | inner/physical | pole-span:inner/physical | 5 |
| H4867 mish.bar | wave | Hebrew | inner/physical | pole-span:inner/physical | 4 |
| H7460 ra.ad | to tremble | Hebrew | inner/physical | 2 stems; pole-span:inner/physical | 2 |
| H1670 de.a.vah | dismay | Hebrew | inner/physical | pole-span:inner/physical | 1 |
| H6426 pa.lats | to shudder | Hebrew | inner/physical | pole-span:inner/physical | 0 |

### All terms

| Term | Gloss | Lang | Verdict | Why | Pole | Verses | Keyword candidates |
|---|---|---|---|---|---|---|---|
| H3372G ya.re | to fear: revere | Hebrew | **multi** | 3 stems; pole-span:inner/physical | inner/physical | 191 | fear, revere, afraid, astonish, awe, awed, danger, dread |
| H3372H ya.re | to fear: revere | Hebrew | **multi** | 3 stems; pole-span:inner/physical | inner/physical | 107 | fear, revere, afraid, astonish, awe, awed, awesome, dread |
| G5399 fobeō | to fear | Greek | **single** | single sense | inner | 83 | fear, absolute, act, active, afraid, alarm, anxiou, apprehensive |
| H3373 ya.re | afraid | Hebrew | **single** | single sense | inner | 64 | afraid, fear, reverent |
| H6343 pa.chad | dread | Hebrew | **single** | single sense | inner | 46 | dread, object, terror |
| G5401 fobos | fear | Greek | **single** | single sense | inner | 43 | fear, act, affright, amaze, astonish, awe, concern, cor |
| H3374 yir.ah | fear | Hebrew | **single** | single sense | inner | 43 | fear, awesome, caus, god, object, piety, respect, rever |
| H2729 cha.rad | to tremble | Hebrew | **multi** | 2 stems; pole-span:inner/physical | inner/physical | 34 | trembl, tremble, about, afraid, anxious, army, care, come |
| H0926 ba.hal | to dismay | Hebrew | **multi** | 4 stems | inner | 33 | dismay, act, afraid, alarm, anxiou, disturb, gain, haste |
| H6342 pa.chad | to dread | Hebrew | **multi** | 3 stems; pole-span:inner/physical | inner/physical | 25 | dread, awe, fear, great, revere, tremble |
| H2865 cha.tat | to to be dismayed | Hebrew | **multi** | 4 stems; pole-span:inner/physical | inner/physical | 24 | dismay, abolish, afraid, broken, scar, shatter, terrify |
| H7264 ra.gaz | to tremble | Hebrew | **multi** | 3 stems; pole-span:inner/physical | inner/physical | 20 | tremble, agitat, disquiet, disturb, enrage, excit, excite, oneself |
| H0367 e.mah | terror | Hebrew | **single** | single sense | inner | 16 | terror, dread |
| H6206 a.rats | to tremble | Hebrew | **multi** | 3 stems; pole-span:inner/physical | inner/physical | 15 | tremble, awe, awesome, awful, break, dread, fear, feel |
| H4172A mo.rah | fear | Hebrew | **single** | single sense | inner | 11 | fear, awe, deed, inspir, mean, object, rah, reverence |
| H4172B mo.ra | fear | Hebrew | **single** | single sense | inner | 11 | fear, appoint, awe, exhibition, inspir, power, spell, terror |
| H0927 be.hal | to dismay | Hebrew | **single** | single sense | inner | 10 | dismay, alarm, frighten, hasten, hurry, ithpa, part |
| H1481C gur | to dread | Hebrew | **single** | single sense | inner | 9 | dread, afraid, awe, fear, stand |
| H4032 ma.gor | terror | Hebrew | **single** | single sense | inner | 8 | terror, fear |
| H2851 chit.tit | terror | Hebrew | **single** | single sense | inner | 8 | terror |
| H8539 ta.mah | to astounded | Hebrew | **multi** | 2 stems | inner | 7 | astound, amaz, astonish, dumbfound, one, stunn, yourself |
| H2731 cha.ra.dah | trembling | Hebrew | **single** | single sense | inner | 7 | trembl, anxiety, anxiou, care, extreme, fear, quak |
| H1674 de.a.gah | anxiety | Hebrew | **single** | single sense | inner | 6 | anxiety, anxiou, care |
| H1763 de.chal | to fear | Hebrew | **single** | single sense | inner | 6 | fear, afraid, participle, pas, terrible |
| H2730 cha.red | trembling | Hebrew | **single** | single sense | inner | 6 | trembl, afraid, fear |
| H1091 bal.la.hah | terror | Hebrew | **single** | single sense | inner | 6 | terror, calam, destruction, dread, event |
| G1719 emfobos | afraid | Greek | **single** | single sense | inner | 5 | afraid, act, rev, terrible, terrifi |
| H3025 ya.gor | to fear | Hebrew | **single** | single sense | inner | 5 | fear, afraid, dread |
| G5156 tromos | trembling | Greek | **single** | single sense | inner | 5 | trembl, agitation, anxiou, awe, cor, eph, fear, mind |
| H4288 me.chit.tah | terror | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 5 | terror, break, destruction, dismay, object, ruin |
| G1568 ekthambeo | be awe-struck | Greek | **single** | single sense | inner | 4 | awe, struck, alarm, amaz, astonish, distress, overwhelm, pas |
| H6427 pal.la.tsut | shuddering | Hebrew | **single** | single sense | inner | 4 | shudder, trembl |
| H4867 mish.bar | wave | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 4 | wave, break, breaker, sea |
| G0085 ademoneo | be distressed | Greek | **single** | single sense | inner | 3 | distress, anguish, deject, depress, full, phil, sorrow, troubl |
| G5398 foberos | fearful | Greek | **single** | single sense | inner | 3 | fear, dread, heb, terrible |
| G1790 entromos | trembling | Greek | **single** | single sense | inner | 3 | trembl, act, heb, terrifi |
| H7461B re.a.dah | trembling | Hebrew | **single** | single sense | inner | 3 | trembl, mean |
| H0928 be.ha.lah | dismay | Hebrew | **single** | single sense | inner | 3 | dismay, alarm, ruin, sudden, terror |
| G1169 deilos | timid | Greek | **single** | single sense | inner | 3 | timid, afraid, coward, fear, rev |
| H0366 a.yom | terrible | Hebrew | **single** | single sense | inner | 3 | terrible, dread |
| H8178A sa.ar | shuddering | Hebrew | **single** | single sense | inner | 3 | shudder, horror, terror |
| H7461A ra.ad | trembling | Hebrew | **single** | single sense | inner | 3 | trembl, dah, spell |
| H4034 me.go.rah | fear | Hebrew | **single** | single sense | inner | 2 | fear, terror |
| H3016 ya.gor | fearing | Hebrew | **single** | single sense | inner | 2 | fear |
| G1630 ekfobos | terrified | Greek | **single** | single sense | inner | 2 | terrifi, frighten, heb, horrifi |
| H8312 sar.ap.pim | anxiety | Hebrew | **single** | single sense | inner | 2 | anxiety, disquiet, thought |
| H1205 be.a.tah | terror | Hebrew | **single** | single sense | inner | 2 | terror, dismay |
| G4422 ptoeō | to frighten | Greek | **single** | single sense | inner | 2 | frighten, affright, frightenedfrighten, passive, startl, terrifi, terrify |
| H2844A chat | terror | Hebrew | **single** | single sense | inner | 2 | terror, fear |
| H8541 tim.ma.hon | bewilderment | Hebrew | **single** | single sense | inner | 2 | bewilder, astonish, stupefaction |
| H8175A sa.ar | to shudder | Hebrew | **single** | single sense | inner | 2 | shudder, afraid, bristle, dread, horror, shiver |
| H7460 ra.ad | to tremble | Hebrew | **multi** | 2 stems; pole-span:inner/physical | inner/physical | 2 | trembl, tremble, earth, participle, quake |
| H1670 de.a.vah | dismay | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 1 | dismay, energy, failure, faint, mental |
| H3735 ke.ra | be distressed | Hebrew | **single** | single sense | inner | 1 | distress, griev, ithp |
| H7661 sha.vats | agony | Hebrew | **single** | single sense | inner | 1 | agony, anguish, cramp, mean, uncertain |
| G1168 deiliaō | be timid | Greek | **single** | single sense | inner | 1 | timid, afraid, coward, fear |
| H6345 pach.dah | dread | Hebrew | **single** | single sense | inner | 1 | dread, awe, fear, religiou |
| G4423 ptoēsis | fear | Greek | **single** | single sense | inner | 1 | fear, alarm, consternation, dismay, frighten, pet, someth |
| H4035 me.gu.rah | fear | Hebrew | **single** | single sense | inner | 1 | fear, granary, storehouse, terror |
| H7374 re.tet | panic | Hebrew | **single** | single sense | inner | 1 | panic, trembl |
| G1167 deilia | timidity | Greek | **single** | single sense | inner | 1 | tim, timid, cowardice |
| H7297 ra.hah | to fear | Hebrew | **single** | single sense | inner | 1 | fear, mean, uncertain |
| G6015 deos | fear | Greek | **single** | single sense | inner | 1 | fear, awe, heb, list, manuscript, place, reverence |
| H2847 chit.tah | terror | Hebrew | **single** | single sense | inner | 1 | terror, fear |
| H2283 chag.ga | terror | Hebrew | **single** | single sense | inner | 1 | terror, reel |
| H2113 ze.va.ah | trembling | Hebrew | **single** | single sense | inner | 1 | trembl, horror, object, terror |
| G2285 thambos | amazement | Greek | **single** | single sense | inner | 1 | amaze, act, astonish, awe, wonder |
| H7268 rag.gaz | quivering | Hebrew | **single** | single sense | inner | 1 | quiver, quak, trembl |
| H7269 rog.zah | quivering | Hebrew | **single** | single sense | inner | 1 | quiver, quak, trembl |
| G4426 pturomai | to frighten | Greek | **single** | single sense | inner | 1 | frighten, consternation, passive, phil, scare, terrifi, terrify |
| H7578 re.tet | trembling | Hebrew | **single** | single sense | inner | 1 | trembl |
| H8606 tiph.le.tset | terror | Hebrew | **single** | single sense | inner | 1 | terror, horror, shudder |
| H2849 chat.chat | terror | Hebrew | **single** | single sense | inner | 1 | terror |
| H2866 cha.tat | terror | Hebrew | **single** | single sense | inner | 1 | terror |
| H8429 te.vah | be startled | Hebrew | **single** | single sense | inner | 1 | startl, alarm |
| H2119B za.chal | to fear | Hebrew | **single** | single sense | inner | 1 | fear, afraid, aramaic, chal, equivalent |
| H4637 ma.a.ra.tsah | terror | Hebrew | **single** | single sense | inner | 1 | terror, awful, crash, shock |
| G1569 ekthambos | astonished | Greek | **single** | single sense | inner | 1 | astonish, utter |
| H6125 a.qah | pressure | Hebrew | **single** | single sense | inner | 1 | pressure, oppression |
| H8047G sham.mah | horror: destroyed | Hebrew | **single** | single sense | inner | 0 | destroy, horror, appal, appall, city, etc, land, mah |
| H2189 za.a.vah | horror | Hebrew | **single** | single sense | inner | 0 | horror, object, terror, trembl |
| H6426 pa.lats | to shudder | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 0 | shudder, tremble |
| H6178 a.ruts | dreadful | Hebrew | **single** | single sense | inner | 0 | dread, chasm, clbl, ravine, slope, steep |

## M02 (Anger) — per-term

### Pole-span terms (the cross-pole cases to watch)

| Term | Gloss | Lang | Poles | Why multi | Verses |
|---|---|---|---|---|---|
| H2534 che.mah | rage | Hebrew | inner/physical | pole-span:inner/physical | 110 |
| H2734 cha.rah | to be incensed | Hebrew | inner/physical | 4 stems; pole-span:inner/physical | 87 |
| H2740 cha.ron | burning anger | Hebrew | inner/physical | pole-span:inner/physical | 39 |
| G3709 orgē | wrath | Greek | external/inner | pole-span:external/inner | 33 |
| H2750 cho.ri | burning | Hebrew | inner/physical | pole-span:inner/physical | 5 |
| H7265 re.gaz | to enrage | Hebrew | inner/physical | pole-span:inner/physical | 1 |
| H2152 zal.a.phah | scorching | Hebrew | inner/physical | pole-span:inner/physical | 1 |

### All terms

| Term | Gloss | Lang | Verdict | Why | Pole | Verses | Keyword candidates |
|---|---|---|---|---|---|---|---|
| H2534 che.mah | rage | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 110 | rage, anger, aramaic, bottl, burn, che, displeasure, equivalent |
| H2734 cha.rah | to be incensed | Hebrew | **multi** | 4 stems; pole-span:inner/physical | inner/physical | 87 | incens, anger, angry, becomeangry, burn, furiou, heat, hot |
| H3707 ka.as | to provoke | Hebrew | **multi** | 3 stems | inner | 51 | provoke, anger, angry, griev, indignant, vex, wrath, wroth |
| H7379 riv | strife | Hebrew | **single** | single sense | inner | 48 | strife, case, controversy, dispute, law, quarrel |
| H7068 qin.ah | jealousy | Hebrew | **single** | single sense | inner | 41 | jealou, jealousy, adversar, against, anger, ardour, disposition, envy |
| H2740 cha.ron | burning anger | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 39 | anger, burn, alway, god, heat, used |
| G3709 orgē | wrath | Greek | **multi** | pole-span:external/inner | external/inner | 33 | wrath, anger, bent, can, col, disobedience, displeasure, eph |
| H7107 qa.tsaph | be angry | Hebrew | **multi** | 3 stems | inner | 32 | angry, anger, aramaic, displeas, equivalent, fret, full, furiou |
| H7065 qa.na | be jealous | Hebrew | **multi** | 2 stems | inner | 29 | jealou, anger, enviou, envy, excite, jealousy, provoke, zealou |
| H7110A qe.tseph | wrath | Hebrew | **single** | single sense | inner | 28 | wrath, anger, god, man |
| H2195 za.am | indignation | Hebrew | **single** | single sense | inner | 22 | indignation, anger |
| H3708B ka.a.s | vexation | Hebrew | **single** | single sense | inner | 22 | vexation, anger, frustration, god, grief, men, provocation |
| H0599 a.naph | be angry | Hebrew | **multi** | 2 stems | inner | 14 | angry, alway, breathe, displeas, god, hard |
| H2194 za.am | be indignant | Hebrew | **multi** | 2 stems | inner | 10 | indignant, abhorrent, anger, angri, curse, defiant, denounce, expres |
| G2054 eris | quarrel | Greek | **single** | single sense | inner | 9 | quarrel, altercation, contentiou, discord, disposition, dissension, phil, rom |
| G3710 orgizō | to anger | Greek | **single** | single sense | inner | 8 | anger, angry, can, deponent, disobedience, displeasure, enrag, expres |
| H2197 za.aph | rage | Hebrew | **single** | single sense | inner | 5 | rag, rage, indignation, storm |
| H2750 cho.ri | burning | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 5 | burn, anger, heat |
| H7067H qan.na | jealous | Hebrew | **single** | single sense | inner | 5 | jealou, god, only |
| H6696B tsur | to provoke | Hebrew | **single** | single sense | inner | 4 | provoke, adversary, foe, hostil, show, treat |
| H2196 za.aph | to enrage | Hebrew | **single** | single sense | inner | 4 | enrag, enrage, angry, appear, fret, humour, look, out |
| G4088 pikria | bitterness | Greek | **single** | single sense | inner | 4 | bitter, act, eph, harsh, heb, language, metaphorical, rom |
| G0485 antilogia | dispute | Greek | **single** | single sense | inner | 4 | dispute, argu, contradiction, heb, hostil, jude, opposition, question |
| H4683 mats.tsah | strife | Hebrew | **single** | single sense | inner | 3 | strife, contention |
| G3947 paroxunō | to provoke | Greek | **single** | single sense | inner | 2 | provoke, act, anger, cor, distress, great, incite, intr |
| G3949 parorgizō | to anger | Greek | **single** | single sense | inner | 2 | anger, eph, exasperate, irritate, provoke, rom |
| H2528 che.ma | rage | Hebrew | **single** | single sense | inner | 2 | rage, anger, aramaic, che, mah |
| H4808 me.ri.vah | provocation | Hebrew | **single** | single sense | inner | 2 | provocation, contention, strife |
| G2200 zestos | hot | Greek | **single** | single sense | inner | 2 | hot, boil, fervent, glow, metaphorical, primari, rev, zeal |
| H7072 qan.no | jealous | Hebrew | **single** | single sense | inner | 2 | jealou |
| G2042 erethizō | to provoke/irritate | Greek | **single** | single sense | inner | 2 | irritate, provoke, arouse, col, cor, embitter, exasperate, incite |
| H2198 za.eph | vexed | Hebrew | **single** | single sense | inner | 2 | vex, angry, humour, out, rag |
| H0888 be.esh | be displeased | Hebrew | **single** | single sense | inner | 1 | displeas, aramaic, ash, bad, evil, stink |
| H5307K na.phal | to fall: angry | Hebrew | **multi** | 3 stems | inner | 1 | angry, fall, apportion, assign, attack, away, before, cast |
| H7265 re.gaz | to enrage | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 1 | enrage, rage, aramaic, gaz, tremble |
| H7109 qe.tsaph | wrath | Hebrew | **single** | single sense | inner | 1 | wrath, anger, god |
| G5380 filoneikos | dispute-loving | Greek | **single** | single sense | inner | 1 | dispute, lov, contention, contentiou, cor, disputatiou, fond, quarrelsome |
| H2152 zal.a.phah | scorching | Hebrew | **multi** | pole-span:inner/physical | inner/physical | 1 | scorch, burn, heat, rag |
| G0024 aganaktēsis | indignation | Greek | **single** | single sense | inner | 1 | indignation, cor |
| G3711 orgilos | quick-tempered | Greek | **single** | single sense | inner | 1 | quick, temper, anger, inclin, irascible, passionate, prone, tit |
| G3950 parorgismos | anger | Greek | **single** | single sense | inner | 1 | anger, eph, excit, indignation, provocation, wrath |
| G2371 thumomacheō | to quarrel | Greek | **single** | single sense | inner | 1 | quarrel, act, against, enrag, fierce, fight, hostile, mad |
| G3055 logomachia | quarrel | Greek | **single** | single sense | inner | 1 | quarrel, about, contention, controversy, dispute, implication, strife, tim |
| H4695 mats.tsut | strife | Hebrew | **single** | single sense | inner | 1 | strife, contention |
