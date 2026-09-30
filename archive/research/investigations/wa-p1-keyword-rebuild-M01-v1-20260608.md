# P1 keyword rebuild + self-check — M01 (prototype)

> READ-ONLY (`scripts/_prototype_p1_keywords.py`). Keywords = whole words from the term's STEP meaning; named filters drop function/analytic/transliteration/short tokens and **report what they dropped**. Self-check asserts: no duplicates · all alpha & length≥3 · none in the analytic/translit/stop lists. No DB writes.

**85 terms · self-check PASS 85/85 · dropped: stop 23 · analytic 42 · translit 3 · short 299**

_Suspect (over-long, likely concatenation artifact from HTML-strip): 1 terms — flagged not dropped._

| Term | Keywords (whole-word, deduped) | self-check | dropped (analytic/translit) | suspect |
|---|---|---|---|---|
| G0085 ademoneo | distressed, troubled, depressed, dejected, full, anguish, sorrow | PASS | analytic:phil |  |
| G0318 anankē | necessity, constraint, compulsion, obligation, duty, moral, spiritual, distress, trial, affliction, hardship | PASS | analytic:cor,rom,thess |  |
| G1167 deilia | timidity, cowardice | PASS | analytic:tim |  |
| G1168 deiliaō | timid, afraid, cowardly, fear | PASS |  |  |
| G1169 deilos | timid, afraid, cowardly, fearful | PASS | analytic:rev |  |
| G1568 ekthambeo | awe-struck, overwhelmed, wonder, distressed, alarmed, pas, amazed, astonished | PASS |  |  |
| G1569 ekthambos | astonished | PASS |  |  |
| G1630 ekfobos | terrified, frightened, horrified | PASS | analytic:heb |  |
| G1719 emfobos | afraid, terrified, terrible | PASS | analytic:acts,rev |  |
| G1790 entromos | trembling, terrified | PASS | analytic:acts,heb |  |
| G2285 thambos | amazement, astonishment, wonder, awe | PASS | analytic:acts |  |
| G4422 ptoeō | frighten, startled, frightenedfrighten, terrify, affright, passive, terrified, frightened | PASS |  | frightenedfrighten |
| G4423 ptoēsis | fear, something, alarming, consternation, dismay, frightening, thing | PASS | analytic:pet |  |
| G4426 pturomai | frighten, frightened, scare, terrify, passive, terrified, consternation | PASS | analytic:phil |  |
| G5156 tromos | trembling, fear, primarily, quaking, terror, agitation, mind, anxious, solemn, responsibility, reverence, veneration, awe | PASS | analytic:cor,eph,phil |  |
| G5398 foberos | fearful, dreadful, terrible | PASS | analytic:heb |  |
| G5399 fobeō | fear, afraid, alarmed, contexts, improper, impediment, faith, love, reverence, respect, worship, proper, god, deep, awe, active, but, only, occurs, passive, literature, dread, reverentially, thing, reluctant, scruple, apprehensive, fearfully, anxious, fearful, impressed | PASS | analytic:absolute,acts,cor,eph,form,heb,rev,rom |  |
| G5400 fobētron | fearful, thing, eventthing, something, inspires, terror, terrible, sight, event | PASS |  |  |
| G5401 fobos | fear, terror, respect, reverence, affright, astonishment, amazement, trembling, concern, object, cause, reverential, awe, deference | PASS | analytic:acts,cor,metonymy,pet,rom,see |  |
| G6015 deos | fear, reverence, awe, manuscripts, list, place | PASS | analytic:heb |  |
| H0366 a.yom | terrible, dreadful | PASS |  |  |
| H0367 e.mah | terror, dread | PASS |  |  |
| H0926 ba.hal | dismay, disturb, alarm, terrify, hurry, disturbed, anxious, afraid, hurried, nervous | PASS |  |  |
| H0927 be.hal | dismay, frighten, alarm, hurry, hasten, alarmed | PASS |  |  |
| H0928 be.ha.lah | dismay, sudden, terror, ruin, alarm | PASS |  |  |
| H1091 bal.la.hah | terror, destruction, calamity, dreadful, event | PASS |  |  |
| H1205 be.a.tah | terror, dismay | PASS |  |  |
| H1481C gur | dread, fear, stand, awe, afraid | PASS |  |  |
| H1670 de.a.vah | dismay, faintness, failure, mental, energy | PASS |  |  |
| H1674 de.a.gah | anxiety, anxious, care | PASS |  |  |
| H1763 de.chal | fear | PASS |  |  |
| H2113 ze.va.ah | trembling, horror, object, terror | PASS |  |  |
| H2119B za.chal | fear, afraid, aramaic, equivalent | PASS | translit:chal |  |
| H2189 za.a.vah | horror, trembling, object, terror | PASS |  |  |
| H2283 chag.ga | terror, reeling | PASS |  |  |
| H2729 cha.rad | tremble, quake, move, afraid, startled, terrified | PASS |  |  |
| H2730 cha.red | trembling, fearful, afraid | PASS |  |  |
| H2731 cha.ra.dah | trembling, fear, anxiety, quaking, anxious, care | PASS |  |  |
| H2844A chat | terror, fear | PASS |  |  |
| H2847 chit.tah | terror, fear | PASS |  |  |
| H2849 chat.chat | terror | PASS |  |  |
| H2851 chit.tit | terror | PASS |  |  |
| H2865 cha.tat | dismayed, shattered, broken, abolished, afraid | PASS |  |  |
| H2866 cha.tat | terror | PASS |  |  |
| H3016 ya.gor | fearing, fearful | PASS |  |  |
| H3025 ya.gor | fear, dread, afraid | PASS |  |  |
| H3372G ya.re | fear, revere, frightening, afraid, stand, awe, awed, reverence, honour, respect, fearful, dreadful, feared, cause, astonishment, held, inspire, godly, make, terrify, shoot, pour | PASS |  |  |
| H3372H ya.re | fear, revere, awesome, afraid, stand, awe, awed, reverence, honour, respect, fearful, dreadful, feared, cause, astonishment, held, inspire, godly, make, terrify, shoot, pour, means | PASS |  |  |
| H3373 ya.re | afraid, fearing, reverent | PASS |  |  |
| H3374 yir.ah | fear, terror, fearing | PASS |  |  |
| H3735 ke.ra | distressed, grieved | PASS |  |  |
| H4032 ma.gor | terror, fear | PASS |  |  |
| H4034 me.go.rah | fear, terror | PASS |  |  |
| H4035 me.gu.rah | fear, terror, storehouse, granary | PASS |  |  |
| H4172A mo.rah | fear, reverence, terror | PASS |  |  |
| H4172B mo.ra | fear, appoint, terror | PASS | analytic:spelling |  |
| H4288 me.chit.tah | terror, destruction, ruin, breaking | PASS |  |  |
| H4637 ma.a.ra.tsah | terror, awful, shock, crash | PASS |  |  |
| H4867 mish.bar | wave, breaker, breaking | PASS |  |  |
| H6125 a.qah | pressure, oppression | PASS |  |  |
| H6178 a.ruts | dreadful, chasm, ravine, steep, slope | PASS |  |  |
| H6206 a.rats | tremble, dread, fear, oppress, prevail, break, terrified, cause | PASS |  |  |
| H6342 pa.chad | dread, fear, tremble, revere, awe | PASS |  |  |
| H6343 pa.chad | dread, terror | PASS |  |  |
| H6345 pach.dah | dread, fear, awe, religious | PASS |  |  |
| H6426 pa.lats | shudder, tremble | PASS |  |  |
| H6427 pal.la.tsut | shuddering, trembling | PASS |  |  |
| H7264 ra.gaz | tremble, quake, rage, quiver, agitated, excited, perturbed | PASS |  |  |
| H7268 rag.gaz | quivering, trembling, quaking | PASS |  |  |
| H7269 rog.zah | quivering, trembling, quaking | PASS |  |  |
| H7297 ra.hah | fear | PASS |  |  |
| H7374 re.tet | panic, trembling | PASS |  |  |
| H7460 ra.ad | tremble, quake | PASS |  |  |
| H7461A ra.ad | trembling, dah | PASS | analytic:spelling |  |
| H7461B re.a.dah | trembling, means | PASS |  |  |
| H7578 re.tet | trembling | PASS |  |  |
| H7661 sha.vats | agony, cramp, anguish | PASS |  |  |
| H8047G sham.mah | horror, destroyed, waste, appalment, means | PASS | translit:mah,sham |  |
| H8175A sa.ar | shudder, shiver, dread, bristle, afraid | PASS |  |  |
| H8178A sa.ar | shuddering, terror, horror | PASS |  |  |
| H8312 sar.ap.pim | anxiety, disquieting, thoughts | PASS |  |  |
| H8429 te.vah | startled, alarmed | PASS |  |  |
| H8539 ta.mah | astounded, stunned, amazed, dumbfounded | PASS |  |  |
| H8541 tim.ma.hon | bewilderment, astonishment, stupefaction | PASS |  |  |
| H8606 tiph.le.tset | terror, shuddering, horror | PASS |  |  |

> The self-check is the deliverable: every term's keyword list is asserted clean (no fragments, no dupes, no analytic/translit leakage). A FAIL row names the exact offending token for fix.