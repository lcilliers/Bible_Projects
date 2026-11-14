# Collection evidence report: intend

Generated 2026-11-13T19:01:41Z by run RUN-20261113_190137_323-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-intend-v1-20261113.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection intend at a glance

Status confirmed; core term 1861; created 2026-11-08T13:08:39Z, updated 2026-11-10T16:03:40Z; run RUN-20261110_160340_252-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (14)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| intend | word | core | intend | placed | 11 | 9 |
| intended | word | synonym | intend | placed | 6 | 6 |
| intending | word | synonym | intend | placed | 4 | 3 |
| intent | word | synonym | intent | placed | 3 | 3 |
| intention | word | synonym | intent | placed | 2 | 2 |
| intentions | word | synonym |  | placed | 2 | 2 |
| intents | word | synonym | intent | placed | 1 | 1 |
| made plans | phrase | phrase | made plans | placed | 2 | 2 |
| meant | word | synonym | mean | placed | 11 | 9 |
| plan | word | synonym | plan | placed | 32 | 28 |
| plans | word | synonym | plan | placed | 29 | 26 |
| purpose | word | synonym | purpose | placed | 40 | 40 |
| purposed | word | synonym | purpose | placed | 18 | 15 |
| purposes | word | synonym | purpose | placed | 6 | 6 |

### 2.2 The Strong's codes behind the members (60)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H4284 מַחֲשָׁבָה ma.cha.sha.vah "plot" | 17 | 1 | 17 | plans 11, purposes 3, plan 2, purpose 1 | none | 14 |
| H6098 עֵצָה e.tsah "counsel" | 14 | 2 | 16 | plan 5, purpose 5, plans 3, purposes 1 | none | 8 |
| H2803I חָשַׁב cha.shav "to devise: devise" | 11 | 0 | 10 | intend 3, plans 3, intended 2, meant 2, plan 1 | none | 10 |
| H3289 יָעַץ ya.ats "to advise" | 10 | 1 | 11 | purposed 6, plan 2, plans 2 | none | 1 |
| G1012 βουλή boulē "plan" | 8 | 0 | 8 | plan 4, purpose 3, purposes 1 | none | 8 |
| G3195 μέλλω mellō "to ensue" | 7 | 0 | 5 | intend 3, intending 3, intended 1 | none | 0 |
| G4286 πρόθεσις prothesis "purpose" | 6 | 0 | 6 | purpose 6 | none | 6 |
| H2161 זָמַם za.mam "to plan" | 6 | 1 | 7 | purposed 5, meant 1 | none | 7 |
| H3336 יֵ֫צֶר ye.tser "intention" | 4 | 0 | 4 | intention 2, plan 1, purposes 1 | none | 4 |
| H4209 מְזִמָּה me.zim.mah "plot" | 4 | 0 | 4 | purpose 2, intentions 1, intents 1 | none | 4 |
| G1011 βουλεύω bouleuō "to plan" | 3 | 0 | 3 | made plans 2, plans 1 | none | 3 |
| G1510 εἰμί eimi "to be" | 3 | 0 | 3 | meant 3 | none | 0 |
| H0559 אָמַר a.mar "to say" | 3 | 1 | 4 | intend 1, intended 1, purposed 1 | none | 0 |
| H2656 חֵ֫פֶץ che.phets "pleasure" | 3 | 0 | 3 | purpose 3 | none | 3 |
| H8403 תַּבְנִית tav.nit "pattern" | 3 | 1 | 4 | plan 3 | none | 0 |
| G0846 αὐτός autos "it/s/he" | 2 | 0 | 2 | purpose 2 | none | 0 |
| G1014 βούλομαι boulomai "to plan" | 2 | 0 | 2 | intend 1, intending 1 | none | 2 |
| G2107 εὐδοκία eudokia "goodwill" | 2 | 0 | 2 | purpose 2 | none | 1 |
| G3622 οἰκονομία oikonomia "management" | 2 | 0 | 2 | plan 2 | none | 0 |
| H2654A חָפֵץ cha.phets "to delight in" | 2 | 0 | 2 | meant 1, purpose 1 | none | 1 |
| H7684 שְׁגָגָה she.ga.gah "unintentionally" | 2 | 0 | 2 | intent 2 | none | 0 |
| G1013 βούλημα boulēma "plan" | 1 | 0 | 1 | plan 1 | none | 1 |
| G1106 γνώμη gnōmē "resolution" | 1 | 0 | 1 | purpose 1 | none | 1 |
| G1223 διά dia "through/because of" | 1 | 0 | 1 | purpose 1 | none | 0 |
| G1771 ἔννοια ennoia "thought/purpose" | 1 | 0 | 1 | intentions 1 | none | 1 |
| G1963 ἐπίνοια epinoia "thought" | 1 | 0 | 1 | intent 1 | none | 1 |
| G2309 θέλω thelō "to will/desire" | 1 | 0 | 1 | meant 1 | none | 1 |
| G2588 καρδία kardia "heart" | 1 | 0 | 1 | purpose 1 | none | 1 |
| G2761 κενῶς kenōs "vainly" | 1 | 0 | 1 | purpose 1 | none | 0 |
| G3004G λέγω legō "to say: says" | 1 | 0 | 1 | meant 1 | none | 0 |
| G3778 οὗτος houtos "this/these" | 1 | 0 | 1 | purpose 1 | none | 0 |
| G4388 προτίθημι protithēmi "to plan/present" | 1 | 0 | 1 | intended 1 | none | 1 |
| G5056 τέλος telos "goal/tax" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H1584 גָּמַר ga.mar "to cease" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H1697I דָּבָר da.var "word: thing" | 1 | 0 | 1 | plan 1 | none | 0 |
| H1697K דָּבָר da.var "word: deed" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H1697M דָּבָר da.var "word: because" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H1819 דָּמָה da.mah "to resemble" | 1 | 1 | 2 | intend 1 | none | 1 |
| H2154 זִמָּה zim.mah "wickedness" | 1 | 0 | 1 | plans 1 | none | 0 |
| H2790A חָרַשׁ cha.rash "to plow/plot" | 1 | 0 | 1 | plan 1 | none | 0 |
| H3335I יָצַר ya.tsar "to form: plan" | 1 | 0 | 1 | purposed 1 | none | 0 |
| H3820A לֵב lev "heart" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H4399 מְלָאכָה me.la.khah "work" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H4616 מַ֫עַן ma.an "because" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H4617 מַעֲנֶה ma.a.neh "answer" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H4633 מַעֲרָךְ ma.a.rakh "plan" | 1 | 0 | 1 | plans 1 | none | 0 |
| H4639G מַעֲשֶׂה ma.a.seh "deed: work" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H4941J מִשְׁפָּט mish.pat "justice: custom" | 1 | 0 | 1 | plan 1 | none | 0 |
| H5475 סוֹד sod "counsel" | 1 | 0 | 1 | plans 1 | none | 0 |
| H5668 עָבוּר a.vur "for the sake of" | 1 | 0 | 1 | purpose 1 | none | 0 |
| H6250 עֶשְׁתֹּנָה esh.to.nah "thought" | 1 | 0 | 1 | plans 1 | none | 1 |
| H6440H פָּנֶה pa.neh "face" | 1 | 0 | 1 | intended 1 | none | 0 |
| H7760K שׂוּם sum "to set: consider" | 1 | 0 | 1 | plans 1 | none | 0 |
| H0834A אֲשֶׁר a.sher "which" | 0 | 2 | 2 |  | none | 0 |
| H0853 אֵת et "[Obj.]" | 0 | 6 | 6 |  | none | 0 |
| H1931 הוּא hu "he/she/it" | 0 | 1 | 1 |  | none | 0 |
| H2005 הֵן hen "look!" | 0 | 1 | 1 |  | none | 0 |
| H3588A כִּי ki "for" | 0 | 1 | 1 |  | none | 0 |
| H5186 נָטָה na.tah "to stretch" | 0 | 1 | 1 |  | none | 0 |
| H8508 תׇּכְנִית tokh.nit "proportion" | 0 | 1 | 1 |  | none | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.54.

### 3.1 H4284 מַחֲשָׁבָה ma.cha.sha.vah "plot": 17 own occurrences in 17 verses

- **Meaning as stored:** Hebrew; native word מַחֲשָׁבָה, transliteration ma.cha.sha.vah; STEP gloss "plot"; sense head "plot" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4284):** thought, device.
- **Related terms (28):** H2803G cha.shav "to devise: design"; H2803H cha.shav "to devise: count"; H2803I cha.shav "to devise: devise"; H2803J cha.shav "to devise: think"; H2804 cha.shav "to account"; H2805 che.shev "artwork"; more in the workbook.
- **Clusters (cluster_strong):** M06 Malice & Enmity (heuristic).
- **Counts, three measures as stored:** STEP token count 56; verses STEP attests 52; verse_lexical rows the parse found 56.

- **Carried by the member words:** plans (11), purposes (3), plan (2), purpose (1).
- **Engagement of these occurrences:** none recorded 17.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Est 9:25 | plan | HNcfsc | none recorded | 12452, 20012, 20436, 20470, 20497 | 0 | But when it came before the king, he gave orders in writing that his evil **plan** that he had devised against the Jews should return on his own head, and that he and his sons should be hanged on the gallows. |
| Jer 18:11 | plan | HNcfsa | none recorded | 12442, 19410, 19420, 20028 | 0 | Now, therefore, say to the men of Judah and the inhabitants of Jerusalem: ‘ Thus says the Lord, Behold, I am shaping disaster against you and devising a **plan** against you. Return, every one from his evil way, and amend your ways and your deeds.’ |
| Psa 33:10 | plans | HNcfpc | none recorded | 12430, 20488 | 0 | The Lord brings the counsel of the nations to nothing; he frustrates the **plans** of the peoples. |
| Psa 33:11 | plans | HNcfpc | none recorded | 12430, 15974, 20443, 20458, 20471, 20488 | 0 | The counsel of the Lord stands forever, the **plans** of his heart to all generations. |
| Pro 6:18 | plans | HNcfpc | none recorded | 12407, 12424, 16538, 17236, 17277, 20481, 20493 | 0 | a heart that devises wicked **plans**, feet that make haste to run to evil, |
| Pro 15:22 | plans | HNcfpa | none recorded | 12411, 20444, 20446, 20478, 20486, 20494 | 0 | Without counsel **plans** fail, but with many advisers they succeed. |
| Pro 16:3 | plans | HNcfpc | none recorded | 12452, 20444, 20446, 20458 | 0 | Commit your work to the Lord, and your **plans** will be established. |
| Pro 19:21 | plans | HNcfpa | none recorded | 12430, 14479, 15974, 17236, 20488, 20508 | 0 | Many are the **plans** in the mind of a man, but it is the purpose of the Lord that will stand. |
| Pro 20:18 | plans | HNcfpa | none recorded | 12411, 20444, 20446, 20478, 20486, 20494 | 0 | **Plans** are established by counsel; by wise guidance wage war. |
| Pro 21:5 | plans | HNcfpc | none recorded | 12452, 20436, 20444, 20446, 20478, 20497 | 0 | The **plans** of the diligent lead surely to abundance, but everyone who is hasty comes only to poverty. |
| Jer 18:12 | plans | HNcfpc | none recorded | 17146, 19410 | 0 | “But they say, ‘That is in vain! We will follow our own **plans**, and will every one act according to the stubbornness of his evil heart.’ |
| Jer 29:11 | plans | HNcfpc | none recorded | - | 0 | For I know the **plans** I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope. |
| Dan 11:24 | plans | HNcfpc | none recorded | - | 0 | Without warning he shall come into the richest parts of the province, and he shall do what neither his fathers nor his fathers ’ fathers have done, scattering among them plunder, spoil, and goods. He shall devise **plans** against strongholds, but only for a time. |
| Jer 49:30 | purpose | HNcfsa | none recorded | - | 0 | Flee, wander far away, dwell in the depths, O inhabitants of Hazor! declares the Lord. For Nebuchadnezzar king of Babylon has made a plan against you and formed a **purpose** against you. |
| Jer 49:20 | purposes | HNcfpc | none recorded | 19409 | 0 | Therefore hear the plan that the Lord has made against Edom and the **purposes** that he has formed against the inhabitants of Teman: Even the little ones of the flock shall be dragged away. Surely their fold shall be appalled at their fate. |
| Jer 50:45 | purposes | HNcfpc | none recorded | 19409 | 0 | Therefore hear the plan that the Lord has made against Babylon, and the **purposes** that he has formed against the land of the Chaldeans: Surely the little ones of their flock shall be dragged away; surely their fold shall be appalled at their fate. |
| Jer 51:29 | purposes | HNcfpc | none recorded | - | 0 | The land trembles and writhes in pain, for the Lord’s **purposes** against Babylon stand, to make the land of Babylon a desolation, without inhabitant. |

### 3.2 H6098 עֵצָה e.tsah "counsel": 14 own occurrences in 14 verses

- **Meaning as stored:** Hebrew; native word עֵצָה, transliteration e.tsah; STEP gloss "counsel"; sense head "counsel" (the code is its own lemma).
- **Related terms (2):** H3289 ya.ats "to advise"; H4156 mo.e.tsah "counsel".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (heuristic).
- **Counts, three measures as stored:** STEP token count 92; verses STEP attests 85; verse_lexical rows the parse found 89.

- **Carried by the member words:** plan (5), purpose (5), plans (3), purposes (1).
- **Engagement of these occurrences:** none recorded 14.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 30:1 | plan | HNcfsa | none recorded | 15975, 20135, 20142, 20164, 20207 | 0 | “ Ah, stubborn children,” declares the Lord, “who carry out a **plan**, but not mine, and who make an alliance, but not of my Spirit, that they may add sin to sin; |
| Jer 49:20 | plan | HNcfsc | none recorded | 19409 | 0 | Therefore hear the **plan** that the Lord has made against Edom and the purposes that he has formed against the inhabitants of Teman: Even the little ones of the flock shall be dragged away. Surely their fold shall be appalled at their fate. |
| Jer 49:30 | plan | HNcfsa | none recorded | 20031 | 0 | Flee, wander far away, dwell in the depths, O inhabitants of Hazor! declares the Lord. For Nebuchadnezzar king of Babylon has made a **plan** against you and formed a purpose against you. |
| Jer 50:45 | plan | HNcfsc | none recorded | 19409 | 0 | Therefore hear the **plan** that the Lord has made against Babylon, and the purposes that he has formed against the land of the Chaldeans: Surely the little ones of their flock shall be dragged away; surely their fold shall be appalled at their fate. |
| Mic 4:12 | plan | HNcfsc | none recorded | 20456 | 0 | But they do not know the thoughts of the Lord; they do not understand his **plan**, that he has gathered them as sheaves to the threshing floor. |
| Psa 14:6 | plans | HNcfsc | none recorded | - | 0 | You would shame the **plans** of the poor, but the Lord is his refuge. |
| Psa 20:4 | plans | HNcfsc | none recorded | - | 0 | May he grant you your heart’s desire and fulfill all your **plans**! |
| Isa 25:1 | plans | HNcfpa | none recorded | - | 0 | O Lord, you are my God; I will exalt you; I will praise your name, for you have done wonderful things, **plans** formed of old, faithful and sure. |
| Ezr 4:5 | purpose | HNcfsc | none recorded | - | 0 | and bribed counselors against them to frustrate their **purpose**, all the days of Cyrus king of Persia, even until the reign of Darius king of Persia. |
| Pro 19:21 | purpose | HNcfsc | none recorded | 15974, 20488, 20498, 20508 | 0 | Many are the plans in the mind of a man, but it is the **purpose** of the Lord that will stand. |
| Pro 20:5 | purpose | HNcfsa | none recorded | 15974, 17237 | 0 | The **purpose** in a man’s heart is like deep water, but a man of understanding will draw it out. |
| Isa 14:26 | purpose | HNcfsa | none recorded | - | 0 | This is the **purpose** that is purposed concerning the whole earth, and this is the hand that is stretched out over all the nations. |
| Isa 19:17 | purpose | HNcfsc | none recorded | - | 0 | And the land of Judah will become a terror to the Egyptians. Everyone to whom it is mentioned will fear because of the **purpose** that the Lord of hosts has purposed against them. |
| Psa 106:43 | purposes | HNcfsc | none recorded | 14565, 19067 | 0 | Many times he delivered them, but they were rebellious in their **purposes** and were brought low through their iniquity. |

### 3.3 H2803I חָשַׁב cha.shav "to devise: devise": 11 own occurrences in 10 verses

- **Meaning as stored:** Hebrew; native word חָשַׁב, transliteration cha.shav; STEP gloss "to devise: devise"; sense head "devise/plot/plan".
- **Senses (first level of the meaning tree of the lemma H2803):** to think, plan, esteem, calculate, invent, make a judgment, imagine, c ... (cut; the whole text is in the workbook).
- **Related terms (28):** H2803G cha.shav "to devise: design"; H2803H cha.shav "to devise: count"; H2803J cha.shav "to devise: think"; H2804 cha.shav "to account"; H2805 che.shev "artwork"; H2806 chash.bad.da.nah "Hashbaddanah"; more in the workbook.
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 44; verses STEP attests 43; verse_lexical rows the parse found 44.

- **Carried by the member words:** intend (3), plans (3), intended (2), meant (2), plan (1).
- **Engagement of these occurrences:** none recorded 11.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Neh 6:6 | intend | HVqrmpa | none recorded | 12514, 20208 | 0 | In it was written, “It is reported among the nations, and Geshem also says it, that you and the Jews **intend** to rebel; that is why you are building the wall. And according to these reports you wish to become their king. |
| Jer 26:3 | intend | HVqrmsa | none recorded | 12442, 19411, 20535 | 0 | It may be they will listen, and every one turn from his evil way, that I may relent of the disaster that I **intend** to do to them because of their evil deeds. |
| Jer 36:3 | intend | HVqrmsa | none recorded | 12442, 19411, 20535 | 0 | It may be that the house of Judah will hear all the disaster that I **intend** to do to them, so that every one may turn from his evil way, and that I may forgive their iniquity and their sin.” |
| Neh 6:2 | intended | HVqrmpa | none recorded | 12514, 20002 | 0 | Sanballat and Geshem sent to me, saying, “ Come and let us meet together at Hakkephirim in the plain of Ono.” But they **intended** to do me harm. |
| Jer 18:8 | intended | HVqp1cs | none recorded | 12442, 19411, 20028 | 0 | and if that nation, concerning which I have spoken, turns from its evil, I will relent of the disaster that I **intended** to do to it. |
| Gen 50:20 | meant | HVqp2mp | none recorded | 12430, 12450, 19416, 20018, 20459, 20488, 20498 | 0 | As for you, you **meant** evil against me, but God meant it for good, to bring it about that many people should be kept alive, as they are today. |
| Gen 50:20 | meant | HVqp3ms | none recorded | - | 0 | As for you, you **meant** evil against me, but God meant it for good, to bring it about that many people should be kept alive, as they are today. |
| Psa 140:2 | plan | HVqp3cp | none recorded | 12407, 14322, 16538, 16982, 17054, 19275, 19276, 19351, 19997, 20031, 20211, 20481 | 0 | who **plan** evil things in their heart and stir up wars continually. |
| Pro 16:9 | plans | HVpi3ms | none recorded | 12407, 17053, 17236, 17277, 19686, 19997, 19999, 20018, 20211, 20217, 20420, 20459, 20481, 20488, 20508 | 0 | The heart of man **plans** his way, but the Lord establishes his steps. |
| Pro 16:30 | plans | HVqcc | none recorded | 12424, 20002, 20490, 20493 | 0 | Whoever winks his eyes **plans** dishonest things; he who purses his lips brings evil to pass. |
| Pro 24:8 | plans | HVprmsa | none recorded | 12510, 20012 | 0 | Whoever **plans** to do evil will be called a schemer. |

### 3.4 H3289 יָעַץ ya.ats "to advise": 10 own occurrences in 10 verses

- **Meaning as stored:** Hebrew; native word יָעַץ, transliteration ya.ats; STEP gloss "to advise"; sense head "to advise" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3289):** to advise, consult, give counsel, counsel, purpose, devise, plan.
- **Related terms (4):** H3272A ye.at "to counsel"; H3272B ya.et "counsellor"; H4156 mo.e.tsah "counsel"; H6098 e.tsah "counsel".
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 79; verses STEP attests 73; verse_lexical rows the parse found 79.

- **Carried by the member words:** purposed (6), plan (2), plans (2).
- **Engagement of these occurrences:** none recorded 10.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 62:4 | plan | HVqp3cp | none recorded | - | 0 | They only **plan** to thrust him down from his high position. They take pleasure in falsehood. They bless with their mouths, but inwardly they curse. Selah |
| Pro 12:20 | plan | HVqrmpc | none recorded | 15892 | 0 | Deceit is in the heart of those who devise evil, but those who **plan** peace have joy. |
| Isa 32:7 | plans | HVqp3ms | none recorded | - | 0 | As for the scoundrel — his devices are evil; he **plans** wicked schemes to ruin the poor with lying words, even when the plea of the needy is right. |
| Isa 32:8 | plans | HVqp3ms | none recorded | - | 0 | But he who is noble **plans** noble things, and on noble things he stands. |
| Isa 14:24 | purposed | HVqp1cs | none recorded | - | 0 | The Lord of hosts has sworn: “ As I have planned, so shall it be, and as I have **purposed**, so shall it stand, |
| Isa 14:26 | purposed | HVqsfsa | none recorded | - | 0 | This is the purpose that is **purposed** concerning the whole earth, and this is the hand that is stretched out over all the nations. |
| Isa 14:27 | purposed | HVqp3ms | none recorded | - | 0 | For the Lord of hosts has **purposed**, and who will annul it? His hand is stretched out, and who will turn it back? |
| Isa 19:12 | purposed | HVqp3ms | none recorded | - | 0 | Where then are your wise men? Let them tell you that they might know what the Lord of hosts has **purposed** against Egypt. |
| Isa 23:8 | purposed | HVqp3ms | none recorded | - | 0 | Who has **purposed** this against Tyre, the bestower of crowns, whose merchants were princes, whose traders were the honored of the earth? |
| Isa 23:9 | purposed | HVqp3ms | none recorded | - | 0 | The Lord of hosts has **purposed** it, to defile the pompous pride of all glory, to dishonor all the honored of the earth. |

### 3.5 G1012 βουλή boulē "plan": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word βουλή, transliteration boulē; STEP gloss "plan"; sense head "plan" (the code is its own lemma).
- **Related terms (6):** G1011 bouleuō "to plan"; G1013 boulēma "plan"; G1014 boulomai "to plan"; G1917 epiboulē "plot"; G4824 sumboulion "counsel/council"; G4825 sumboulos "counselor".
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 138; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** plan (4), purpose (3), purposes (1).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 2:23 | plan | N-DSF | none recorded | 12519, 19416 | 0 | this Jesus, delivered up according to the definite **plan** and foreknowledge of God, you crucified and killed by the hands of lawless men. |
| Act 4:28 | plan | N-NSF | none recorded | 12519, 19416 | 0 | to do whatever your hand and your **plan** had predestined to take place. |
| Act 5:38 | plan | N-NSF | none recorded | 12520, 20018, 20029 | 0 | So in the present case I tell you, keep away from these men and let them alone, for if this **plan** or this undertaking is of man, it will fail; |
| Act 27:42 | plan | N-NSF | none recorded | 12514, 20031, 20207 | 0 | The soldiers ’ **plan** was to kill the prisoners, lest any should swim away and escape. |
| Luk 7:30 | purpose | N-ASF | none recorded | 12522, 19419 | 0 | but the Pharisees and the lawyers rejected the **purpose** of God for themselves, not having been baptized by him.) |
| Act 13:36 | purpose | N-DSF | none recorded | 19419 | 0 | For David, after he had served the **purpose** of God in his own generation, fell asleep and was laid with his fathers and saw corruption, |
| Heb 6:17 | purpose | N-GSF | none recorded | 12511, 19412, 20126, 20201, 20210 | 0 | So when God desired to show more convincingly to the heirs of the promise the unchangeable character of his **purpose**, he guaranteed it with an oath, |
| 1Cor 4:5 | purposes | N-APF | none recorded | 12508, 16031, 16302, 17057, 17244, 19997, 20019 | 0 | Therefore do not pronounce judgment before the time, before the Lord comes, who will bring to light the things now hidden in darkness and will disclose the **purposes** of the heart. Then each one will receive his commendation from God. |

### 3.6 G3195 μέλλω mellō "to ensue": 7 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word μέλλω, transliteration mellō; STEP gloss "to ensue"; sense head "to ensue" (the code is its own lemma).
- **Related terms (1):** G3199 melō "to concern".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 128; verses STEP attests 106; verse_lexical rows the parse found 109.

- **Carried by the member words:** intend (3), intending (3), intended (1).
- **Engagement of these occurrences:** none recorded 7.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 7:35 | intend | V-PAI-3S | none recorded | - | 0 | The Jews said to one another, “ Where does this man **intend** to go that we will not find him? Does he intend to go to the Dispersion among the Greeks and teach the Greeks? |
| Joh 7:35 | intend | V-PAI-3S | none recorded | - | 0 | The Jews said to one another, “ Where does this man **intend** to go that we will not find him? Does he intend to go to the Dispersion among the Greeks and teach the Greeks? |
| 2Pe 1:12 | intend | V-FAI-1S | none recorded | - | 0 | Therefore I **intend** always to remind you of these qualities, though you know them and are established in the truth that you have. |
| Act 25:4 | intended | V-PAN | none recorded | - | 0 | Festus replied that Paul was being kept at Caesarea and that he himself **intended** to go there shortly. |
| Act 20:7 | intending | V-PAP-NSM | none recorded | - | 0 | On the first day of the week, when we were gathered together to break bread, Paul talked with them, **intending** to depart on the next day, and he prolonged his speech until midnight. |
| Act 20:13 | intending | V-PAP-NPM | none recorded | - | 0 | But going ahead to the ship, we set sail for Assos, **intending** to take Paul aboard there, for so he had arranged, intending himself to go by land. |
| Act 20:13 | intending | V-PAP-NSM | none recorded | - | 0 | But going ahead to the ship, we set sail for Assos, **intending** to take Paul aboard there, for so he had arranged, intending himself to go by land. |

### 3.7 G4286 πρόθεσις prothesis "purpose": 6 own occurrences in 6 verses

- **Meaning as stored:** Greek; native word πρόθεσις, transliteration prothesis; STEP gloss "purpose"; sense head "purpose" (the code is its own lemma).
- **Related terms (1):** G4388 protithēmi "to plan/present".
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 25; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** purpose (6).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 27:13 | purpose | N-GSF | none recorded | 12518, 20005, 20029 | 0 | Now when the south wind blew gently, supposing that they had obtained their **purpose**, they weighed anchor and sailed along Crete, close to the shore. |
| Rom 8:28 | purpose | N-ASF | none recorded | 12522, 19418 | 0 | And we know that for those who love God all things work together for good, for those who are called according to his **purpose**. |
| Rom 9:11 | purpose | N-NSF | none recorded | 12524, 19417, 19479, 19714 | 0 | though they were not yet born and had done nothing either good or bad —in order that God’s **purpose** of election might continue, not because of works but because of him who calls — |
| Eph 1:11 | purpose | N-ASF | none recorded | 12524, 19417 | 0 | In him we have obtained an inheritance, having been predestined according to the **purpose** of him who works all things according to the counsel of his will, |
| Eph 3:11 | purpose | N-ASF | none recorded | 12524, 19417 | 0 | This was according to the eternal **purpose** that he has realized in Christ Jesus our Lord, |
| 2Ti 1:9 | purpose | N-ASF | none recorded | 12524, 19417 | 0 | who saved us and called us to a holy calling, not because of our works but because of his own **purpose** and grace, which he gave us in Christ Jesus before the ages began, |

### 3.8 H2161 זָמַם za.mam "to plan": 6 own occurrences in 6 verses

- **Meaning as stored:** Hebrew; native word זָמַם, transliteration za.mam; STEP gloss "to plan"; sense head "to plan" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2161):** to have a thought, devise, plan, consider, purpose.
- **Related terms (6):** H2154 zim.mah "wickedness"; H2155G zim.mah "Zimmah"; H2155H zim.mah "Zimmah"; H2157 zam.zum.mim "Zamzummin"; H2162 za.mam "plan"; H4209 me.zim.mah "plot".
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 13; verse_lexical rows the parse found 13.

- **Carried by the member words:** purposed (5), meant (1).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 19:19 | meant | HVqp3ms | none recorded | 12510, 20012 | 0 | then you shall do to him as he had **meant** to do to his brother. So you shall purge the evil from your midst. |
| Psa 17:3 | purposed | HVqp1cs | none recorded | 12509, 17059, 20014, 20025 | 0 | You have tried my heart, you have visited me by night, you have tested me, and you will find nothing; I have **purposed** that my mouth will not transgress. |
| Jer 4:28 | purposed | HVqp1cs | none recorded | 12511, 19412, 20025 | 0 | “ For this the earth shall mourn, and the heavens above be dark; for I have spoken; I have **purposed**; I have not relented, nor will I turn back.” |
| Lam 2:17 | purposed | HVqp3ms | none recorded | 12512, 19414 | 0 | The Lord has done what he **purposed**; he has carried out his word, which he commanded long ago; he has thrown down without pity; he has made the enemy rejoice over you and exalted the might of your foes. |
| Zec 1:6 | purposed | HVqp3ms | none recorded | 12512, 19414 | 0 | But my words and my statutes, which I commanded my servants the prophets, did they not overtake your fathers? So they repented and said, ‘As the Lord of hosts **purposed** to deal with us for our ways and deeds, so has he dealt with us.’” |
| Zec 8:15 | purposed | HVqp1cs | none recorded | 12511, 13556, 14632, 19412, 19427 | 0 | so again have I **purposed** in these days to bring good to Jerusalem and to the house of Judah; fear not. |

### 3.9 H3336 יֵ֫צֶר ye.tser "intention": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word יֵ֫צֶר, transliteration ye.tser; STEP gloss "intention"; sense head "intention" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3336):** form, framing, purpose, framework.
- **Related terms (7):** H3335G ya.tsar "to form: formed"; H3335H ya.tsar "to form: potter"; H3335I ya.tsar "to form: plan"; H3337 ye.tser "Jezer"; H3338 ye.tsu.rim "member"; H3339 yits.ri "Izri"; more in the workbook.
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** intention (2), plan (1), purposes (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 6:5 | intention | HNcmsc | none recorded | 12412, 12423, 12428, 16535, 17057, 19997, 20019, 20027, 20325, 20375, 20385, 20449, 20453, 20462, 20499, 20515 | 0 | The Lord saw that the wickedness of man was great in the earth, and that every **intention** of the thoughts of his heart was only evil continually. |
| Gen 8:21 | intention | HNcmsc | none recorded | 12412, 12423, 16535, 17057, 20019, 20462, 20515 | 0 | And when the Lord smelled the pleasing aroma, the Lord said in his heart, “I will never again curse the ground because of man, for the **intention** of man’s heart is evil from his youth. Neither will I ever again strike down every living creature as I have done. |
| 1Ch 28:9 | plan | HNcmsc | none recorded | 12412, 12413, 12431, 17057, 19501, 20019, 20029, 20216, 20414 | 0 | “And you, Solomon my son, know the God of your father and serve him with a whole heart and with a willing mind, for the Lord searches all hearts and understands every **plan** and thought. If you seek him, he will be found by you, but if you forsake him, he will cast you off forever. |
| 1Ch 29:18 | purposes | HNcmsc | none recorded | 12434, 17057, 20015, 20027, 20327, 20415 | 0 | O Lord, the God of Abraham, Isaac, and Israel, our fathers, keep forever such **purposes** and thoughts in the hearts of your people, and direct their hearts toward you. |

### 3.10 H4209 מְזִמָּה me.zim.mah "plot": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word מְזִמָּה, transliteration me.zim.mah; STEP gloss "plot"; sense head "plot" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4209):** purpose, discretion, device, plot.
- **Related terms (6):** H2154 zim.mah "wickedness"; H2155G zim.mah "Zimmah"; H2155H zim.mah "Zimmah"; H2157 zam.zum.mim "Zamzummin"; H2161 za.mam "to plan"; H2162 za.mam "plan".
- **Clusters (cluster_strong):** M06 Malice & Enmity (heuristic).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 19; verse_lexical rows the parse found 19.

- **Carried by the member words:** purpose (2), intentions (1), intents (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 30:24 | intentions | HNcfpc | none recorded | 14715 | 0 | The fierce anger of the Lord will not turn back until he has executed and accomplished the **intentions** of his mind. In the latter days you will understand this. |
| Jer 23:20 | intents | HNcfpc | none recorded | 12939, 13206, 13273, 13279, 13298, 13736, 13756, 14715, 15856, 15937, 17281, 20440, 20488, 20544, 20578 | 0 | The anger of the Lord will not turn back until he has executed and accomplished the **intents** of his heart. In the latter days you will understand it clearly. |
| Job 42:2 | purpose | HNcfsa | none recorded | 12430, 20440, 20488 | 0 | “I know that you can do all things, and that no **purpose** of yours can be thwarted. |
| Jer 51:11 | purpose | HNcfsc | none recorded | 16143, 18164, 19409, 20440 | 0 | “ Sharpen the arrows! Take up the shields! The Lord has stirred up the spirit of the kings of the Medes, because his **purpose** concerning Babylon is to destroy it, for that is the vengeance of the Lord, the vengeance for his temple. |

### 3.11 G1011 βουλεύω bouleuō "to plan": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word βουλεύω, transliteration bouleuō; STEP gloss "to plan"; sense head "to plan" (the code is its own lemma).
- **Related terms (7):** G1010 bouleutēs "member of a council"; G1012 boulē "plan"; G1013 boulēma "plan"; G1014 boulomai "to plan"; G1917 epiboulē "plot"; G4823 sumbouleuō "to consult"; more in the workbook.
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 60; verses STEP attests 7; verse_lexical rows the parse found 9.

- **Carried by the member words:** made plans (2), plans (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 11:53 | made plans | V-ADI-3P | none recorded | 12514, 20010 | 0 | So from that day on they **made plans** to put him to death. |
| Joh 12:10 | made plans | V-ADI-3P | none recorded | 12514 | 0 | So the chief priests **made plans** to put Lazarus to death as well, |
| 2Cor 1:17 | plans | V-PNP-NSM | none recorded | 17065, 17267, 20006, 20122, 20181, 20207 | 0 | Was I vacillating when I wanted to do this? Do I make my **plans** according to the flesh, ready to say “ Yes, yes ” and “ No, no ” at the same time? |

### 3.12 G1510 εἰμί eimi "to be": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word εἰμί, transliteration eimi; STEP gloss "to be"; sense head "to be" (the code is its own lemma).
- **Related terms (11):** G1498 eiēn "may be"; G1510 eimi "to be"; G1511 einai "to exist"; G1526 eisi "they are"; G2071 esomai "will be"; G2075 este "you are"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 7942; verses STEP attests 1786; verse_lexical rows the parse found 2068.

- **Carried by the member words:** meant (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 8:9 | meant | V-PAO-3S | none recorded | - | 0 | And when his disciples asked him what this parable **meant**, |
| Luk 15:26 | meant | V-PAO-3S | none recorded | - | 0 | And he called one of the servants and asked what these things **meant**. |
| Luk 18:36 | meant | V-PAO-3S | none recorded | - | 0 | And hearing a crowd going by, he inquired what this **meant**. |

### 3.13 H0559 אָמַר a.mar "to say": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word אָמַר, transliteration a.mar; STEP gloss "to say"; sense head "to say" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0559):** to say, speak, utter.
- **Related terms (28):** H0201 o.mar "Omar"; H0204 on "On"; H0534 a.mir "top"; H0560 a.mar "to say"; H0561 e.mer "word"; H0562 o.mer "word"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 5343; verses STEP attests 4340; verse_lexical rows the parse found 5309.

- **Carried by the member words:** intend (1), intended (1), purposed (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ch 28:10 | intend | HVqrmpa | none recorded | - | 0 | And now you **intend** to subjugate the people of Judah and Jerusalem, male and female, as your slaves. Have you not sins of your own against the Lord your God? |
| Jer 18:10 | intended | HVqp1cs | none recorded | - | 0 | and if it does evil in my sight, not listening to my voice, then I will relent of the good that I had **intended** to do to it. |
| 2Ch 2:1 | purposed | HVqw3ms | none recorded | - | 0 | Now Solomon **purposed** to build a temple for the name of the Lord, and a royal palace for himself. |

### 3.14 H2656 חֵ֫פֶץ che.phets "pleasure": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word חֵ֫פֶץ, transliteration che.phets; STEP gloss "pleasure"; sense head "pleasure" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2656):** delight, pleasure.
- **Related terms (5):** H2654A cha.phets "to delight in"; H2654B cha.phats "to sway"; H2655 cha.phets "delighting"; H2657G cheph.tsi-vah "Hephzibah"; H2657H cheph.tsi-vah "My Delight Is in Her".
- **Clusters (cluster_strong):** M18 Desire & Longing (heuristic).
- **Counts, three measures as stored:** STEP token count 39; verses STEP attests 38; verse_lexical rows the parse found 39.

- **Carried by the member words:** purpose (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 44:28 | purpose | HNcmsc | none recorded | 17520, 17566 | 0 | who says of Cyrus, ‘He is my shepherd, and he shall fulfill all my **purpose** ’; saying of Jerusalem, ‘She shall be built,’ and of the temple, ‘Your foundation shall be laid.’” |
| Isa 46:10 | purpose | HNcmsc | none recorded | 17521, 17566 | 0 | declaring the end from the beginning and from ancient times things not yet done, saying, ‘My counsel shall stand, and I will accomplish all my **purpose**,’ |
| Isa 48:14 | purpose | HNcmsc | none recorded | 17566, 17582 | 0 | “ Assemble, all of you, and listen! Who among them has declared these things? The Lord loves him; he shall perform his **purpose** on Babylon, and his arm shall be against the Chaldeans. |

### 3.15 H8403 תַּבְנִית tav.nit "pattern": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word תַּבְנִית, transliteration tav.nit; STEP gloss "pattern"; sense head "pattern" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8403):** pattern, plan, form, construction, figure.
- **Related terms (42):** H1129 ba.nah "to build"; H1131G bin.nuy "Binnui"; H1131H bin.nuy "Binnui"; H1131I bin.nuy "Binnui"; H1131J bin.nuy "Binnui"; H1131K bin.nuy "Binnui"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 20; verses STEP attests 17; verse_lexical rows the parse found 20.

- **Carried by the member words:** plan (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ch 28:12 | plan | HNcfsc | none recorded | - | 0 | and the **plan** of all that he had in mind for the courts of the house of the Lord, all the surrounding chambers, the treasuries of the house of God, and the treasuries for dedicated gifts; |
| 1Ch 28:18 | plan | HNcfsc | none recorded | - | 0 | for the altar of incense made of refined gold, and its weight; also his **plan** for the golden chariot of the cherubim that spread their wings and covered the ark of the covenant of the Lord. |
| 1Ch 28:19 | plan | HNcfsa | none recorded | - | 0 | “ All this he made clear to me in writing from the hand of the Lord, all the work to be done according to the **plan**.” |

### 3.16 G0846 αὐτός autos "it/s/he": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word αὐτός, transliteration autos; STEP gloss "it/s/he"; sense head "it/s/he" (the code is its own lemma).
- **Related terms (3):** G0847 autou "there"; G1438 heautou "themself"; G1683 emautou "of myself".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 10000; verses STEP attests 0; verse_lexical rows the parse found 5485.

- **Carried by the member words:** purpose (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 9:17 | purpose | P-ASN | none recorded | - | 0 | For the Scripture says to Pharaoh, “ For this very **purpose** I have raised you up, that I might show my power in you, and that my name might be proclaimed in all the earth.” |
| Eph 6:22 | purpose | P-ASN | none recorded | - | 0 | I have sent him to you for this very **purpose**, that you may know how we are, and that he may encourage your hearts. |

### 3.17 G1014 βούλομαι boulomai "to plan": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word βούλομαι, transliteration boulomai; STEP gloss "to plan"; sense head "to plan" (the code is its own lemma).
- **Related terms (6):** G1011 bouleuō "to plan"; G1012 boulē "plan"; G1013 boulēma "plan"; G1917 epiboulē "plot"; G2309 thelō "to will/desire"; G4824 sumboulion "counsel/council".
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 117; verses STEP attests 34; verse_lexical rows the parse found 34.

- **Carried by the member words:** intend (1), intending (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 5:28 | intend | V-PNI-2P | none recorded | 12523, 20190, 20208 | 0 | saying, “We strictly charged you not to teach in this name, yet here you have filled Jerusalem with your teaching, and you **intend** to bring this man’s blood upon us.” |
| Act 12:4 | intending | V-PNP-NSM | none recorded | 12515, 20121, 20180, 20207 | 0 | And when he had seized him, he put him in prison, delivering him over to four squads of soldiers to guard him, **intending** after the Passover to bring him out to the people. |

### 3.18 G2107 εὐδοκία eudokia "goodwill": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word εὐδοκία, transliteration eudokia; STEP gloss "goodwill"; sense head "goodwill" (the code is its own lemma).
- **Related terms (3):** G1380 dokeō "to think"; G2095 eu "well/well done!"; G2106 eudokeō "to delight".
- **Clusters (cluster_strong):** M39 Gift & Favor (None).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** purpose (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 1:5 | purpose | N-ASF | none recorded | - | 0 | he predestined us for adoption to himself as sons through Jesus Christ, according to the **purpose** of his will, |
| Eph 1:9 | purpose | N-ASF | none recorded | 19417 | 0 | making known to us the mystery of his will, according to his **purpose**, which he set forth in Christ |

### 3.19 G3622 οἰκονομία oikonomia "management": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word οἰκονομία, transliteration oikonomia; STEP gloss "management"; sense head "management" (the code is its own lemma).
- **Related terms (25):** G1460 enkatoikeō "to live among"; G1774 enoikeō "to dwell in/with"; G2730 katoikeō "to dwell"; G3350 metoikesia "deportation"; G3351 metoikizō "to deport"; G3609 oikeios "of one’s household"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 0; verse_lexical rows the parse found 9.

- **Carried by the member words:** plan (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 1:10 | plan | N-ASF | none recorded | - | 0 | as a **plan** for the fullness of time, to unite all things in Christ, things in heaven and things on earth in him. |
| Eph 3:9 | plan | N-NSF | none recorded | - | 0 | and to bring to light for everyone what is the **plan** of the mystery hidden for ages in God, who created all things, |

### 3.20 H2654A חָפֵץ cha.phets "to delight in": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word חָפֵץ, transliteration cha.phets; STEP gloss "to delight in"; sense head "to delight in" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2654):** to delight in, take pleasure in, desire, be pleased with.
- **Related terms (5):** H2654B cha.phats "to sway"; H2655 cha.phets "delighting"; H2656 che.phets "pleasure"; H2657G cheph.tsi-vah "Hephzibah"; H2657H cheph.tsi-vah "My Delight Is in Her".
- **Clusters (cluster_strong):** M18 Desire & Longing (heuristic).
- **Counts, three measures as stored:** STEP token count 74; verses STEP attests 69; verse_lexical rows the parse found 73.

- **Carried by the member words:** meant (1), purpose (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Judg 13:23 | meant | HVqp3ms | none recorded | - | 0 | But his wife said to him, “ If the Lord had **meant** to kill us, he would not have accepted a burnt offering and a grain offering at our hands, or shown us all these things, or now announced to us such things as these.” |
| Isa 55:11 | purpose | HVqp1cs | none recorded | 17353, 17508, 17616 | 0 | so shall my word be that goes out from my mouth; it shall not return to me empty, but it shall accomplish that which I **purpose**, and shall succeed in the thing for which I sent it. |

### 3.21 H7684 שְׁגָגָה she.ga.gah "unintentionally": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word שְׁגָגָה, transliteration she.ga.gah; STEP gloss "unintentionally"; sense head "unintentionally" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7684):** sin, sin of error or inadvertence, inadvertent sin.
- **Related terms (1):** H7683 sha.gag "to go astray".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 0; verse_lexical rows the parse found 19.

- **Carried by the member words:** intent (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 35:11 | intent | HNcfsa | none recorded | - | 0 | then you shall select cities to be cities of refuge for you, that the manslayer who kills any person without **intent** may flee there. |
| Num 35:15 | intent | HNcfsa | none recorded | - | 0 | These six cities shall be for refuge for the people of Israel, and for the stranger and for the sojourner among them, that anyone who kills any person without **intent** may flee there. |

### 3.22 G1013 βούλημα boulēma "plan": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word βούλημα, transliteration boulēma; STEP gloss "plan"; sense head "plan" (the code is its own lemma).
- **Related terms (5):** G1011 bouleuō "to plan"; G1012 boulē "plan"; G1014 boulomai "to plan"; G1917 epiboulē "plot"; G4824 sumboulion "counsel/council".
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** plan (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 27:43 | plan | N-GSN | none recorded | 19399, 20031, 20116, 20119, 20182, 20207, 20223 | 0 | But the centurion, wishing to save Paul, kept them from carrying out their **plan**. He ordered those who could swim to jump overboard first and make for the land, |

### 3.23 G1106 γνώμη gnōmē "resolution": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word γνώμη, transliteration gnōmē; STEP gloss "resolution"; sense head "resolution" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 33; verses STEP attests 8; verse_lexical rows the parse found 9.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rev 17:17 | purpose | N-ASF | none recorded | 19524, 20241 | 0 | for God has put it into their hearts to carry out his **purpose** by being of one mind and handing over their royal power to the beast, until the words of God are fulfilled. |

### 3.24 G1223 διά dia "through/because of": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word διά, transliteration dia; STEP gloss "through/because of"; sense head "through/because of" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T6 Connective (high).
- **Counts, three measures as stored:** STEP token count 1667; verses STEP attests 567; verse_lexical rows the parse found 627.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 12:27 | purpose | PREP | none recorded | - | 0 | “ Now is my soul troubled. And what shall I say? ‘ Father, save me from this hour ’? But for this **purpose** I have come to this hour. |

### 3.25 G1771 ἔννοια ennoia "thought/purpose": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἔννοια, transliteration ennoia; STEP gloss "thought/purpose"; sense head "thought/purpose" (the code is its own lemma).
- **Related terms (12):** G0143 aisthanomai "to perceive"; G1271 dianoia "mind"; G1272 dianoigō "to open up"; G1722 en "in/on/among"; G1950 epilanthanō "to forget"; G1963 epinoia "thought"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 14; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** intentions (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 4:12 | intentions | N-GPF | none recorded | 16004, 17274, 20568 | 0 | For the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and **intentions** of the heart. |

### 3.26 G1963 ἐπίνοια epinoia "thought": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐπίνοια, transliteration epinoia; STEP gloss "thought"; sense head "thought" (the code is its own lemma).
- **Related terms (12):** G0143 aisthanomai "to perceive"; G1271 dianoia "mind"; G1272 dianoigō "to open up"; G1771 ennoia "thought/purpose"; G1909 epi "upon/to/against"; G1950 epilanthanō "to forget"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** intent (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 8:22 | intent | N-NSF | none recorded | 16410, 17131, 19041 | 0 | Repent, therefore, of this wickedness of yours, and pray to the Lord that, if possible, the **intent** of your heart may be forgiven you. |

### 3.27 G2309 θέλω thelō "to will/desire": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word θέλω, transliteration thelō; STEP gloss "to will/desire"; sense head "to will/desire" (the code is its own lemma).
- **Related terms (3):** G2307 thelēma "will/desire"; G2308 thelēsis "will"; G2309 thelō "to will/desire".
- **Clusters (cluster_strong):** M18 Desire & Longing (heuristic).
- **Counts, three measures as stored:** STEP token count 323; verses STEP attests 196; verse_lexical rows the parse found 206.

- **Carried by the member words:** meant (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 6:48 | meant | V-IAI-3S | none recorded | 17699 | 0 | And he saw that they were making headway painfully, for the wind was against them. And about the fourth watch of the night he came to them, walking on the sea. He **meant** to pass by them, |

### 3.28 G2588 καρδία kardia "heart": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word καρδία, transliteration kardia; STEP gloss "heart"; sense head "heart" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** M47 Inner Seat (None).
- **Counts, three measures as stored:** STEP token count 905; verses STEP attests 149; verse_lexical rows the parse found 156.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 11:23 | purpose | N-GSF | none recorded | 17058, 20014, 20029, 20104 | 0 | When he came and saw the grace of God, he was glad, and he exhorted them all to remain faithful to the Lord with steadfast **purpose**, |

### 3.29 G2761 κενῶς kenōs "vainly": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word κενῶς, transliteration kenōs; STEP gloss "vainly"; sense head "vainly" (the code is its own lemma).
- **Related terms (1):** G2756 kenos "empty".
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jam 4:5 | purpose | ADV | none recorded | - | 0 | Or do you suppose it is to no **purpose** that the Scripture says, “He yearns jealously over the spirit that he has made to dwell in us ”? |

### 3.30 G3004G λέγω legō "to say: says": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word λέγω, transliteration legō; STEP gloss "to say: says"; sense head "to say: says" (the code is its own lemma).
- **Related terms (15):** G0483 antilegō "to dispute"; G0557 apelegmos "discredit"; G1246 diakatelenchomai "to refute"; G1256 dialegō "to dispute"; G1649 elegxis "rebuke"; G1650 elenchos "rebuke"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 3420; verses STEP attests 1170; verse_lexical rows the parse found 1251.

- **Carried by the member words:** meant (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 11:13 | meant | V-PAI-3S | none recorded | - | 0 | Now Jesus had spoken of his death, but they thought that he **meant** taking rest in sleep. |

### 3.31 G3778 οὗτος houtos "this/these": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word οὗτος, transliteration houtos; STEP gloss "this/these"; sense head "this/these" (the code is its own lemma).
- **Related terms (11):** G3588 ho "the/this/who"; G3778 houtos "this/these"; G3779 houtōs "thus(-ly)"; G5023 tauta "these"; G5124 touto "that"; G5125 toutois "to these"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 2919; verses STEP attests 0; verse_lexical rows the parse found 1210.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Col 4:8 | purpose | P-ASN | none recorded | - | 0 | I have sent him to you for this very **purpose**, that you may know how we are and that he may encourage your hearts, |

### 3.32 G4388 προτίθημι protithēmi "to plan/present": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προτίθημι, transliteration protithēmi; STEP gloss "to plan/present"; sense head "to plan/present" (the code is its own lemma).
- **Related terms (11):** G0111 athemitos "unlawful"; G0394 anatithēmi "to set before"; G0475 antidiatithēmi "to oppose"; G1303 diatithēmi "to make a covenant"; G2652 katanathema "curse"; G2653 katanathematizō "to curse"; more in the workbook.
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** intended (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 1:13 | intended | V-2AMI-1S | none recorded | 12520, 17686, 20018 | 0 | I do not want you to be unaware, brothers, that I have often **intended** to come to you ( but thus far have been prevented ), in order that I may reap some harvest among you as well as among the rest of the Gentiles. |

### 3.33 G5056 τέλος telos "goal/tax": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word τέλος, transliteration telos; STEP gloss "goal/tax"; sense head "goal/tax" (the code is its own lemma).
- **Related terms (4):** G0754 architelōnēs "chief tax collector"; G5055 teleō "to finish"; G5057 telōnēs "tax collector"; G5058 telōnion "tax booth".
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 164; verses STEP attests 39; verse_lexical rows the parse found 40.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jam 5:11 | purpose | N-ASN | none recorded | - | 0 | Behold, we consider those blessed who remained steadfast. You have heard of the steadfastness of Job, and you have seen the **purpose** of the Lord, how the Lord is compassionate and merciful. |

### 3.34 H1584 גָּמַר ga.mar "to cease": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word גָּמַר, transliteration ga.mar; STEP gloss "to cease"; sense head "to cease" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1584):** to end, come to an end, complete, cease; (TWOT) to fail, perfect, perform.
- **Related terms (5):** H1585 ge.mar "to complete"; H1586G go.mer "Gomer"; H1586H go.mer "Gomer"; H1587G ge.mar.ya.hu "Gemariah"; H1587H ge.mar.ya.hu "Gemariah".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 0; verse_lexical rows the parse found 5.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 57:2 | purpose | HVqrmsa | none recorded | - | 0 | I cry out to God Most High, to God who fulfills his **purpose** for me. |

### 3.35 H1697I דָּבָר da.var "word: thing": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word דָּבָר, transliteration da.var; STEP gloss "word: thing"; sense head "thing/matter".
- **Senses (first level of the meaning tree of the lemma H1697):** speech, word, speaking, thing.
- **Related terms (30):** H1682 de.vo.rah "bee"; H1683G de.vo.rah "Deborah"; H1683H de.vo.rah "Deborah"; H1687 de.vir "sanctuary"; H1688A de.vir "Debir"; H1688B lid.vir "Debir"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 314; verses STEP attests 272; verse_lexical rows the parse found 295.

- **Carried by the member words:** plan (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ch 30:4 | plan | HNcmsa | none recorded | - | 0 | and the **plan** seemed right to the king and all the assembly. |

### 3.36 H1697K דָּבָר da.var "word: deed": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word דָּבָר, transliteration da.var; STEP gloss "word: deed"; sense head "deed".
- **Senses (first level of the meaning tree of the lemma H1697):** speech, word, speaking, thing.
- **Related terms (30):** H1682 de.vo.rah "bee"; H1683G de.vo.rah "Deborah"; H1683H de.vo.rah "Deborah"; H1687 de.vir "sanctuary"; H1688A de.vir "Debir"; H1688B lid.vir "Debir"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 78; verses STEP attests 0; verse_lexical rows the parse found 75.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 64:5 | purpose | HNcmsa | none recorded | - | 0 | They hold fast to their evil **purpose**; they talk of laying snares secretly, thinking, “ Who can see them?” |

### 3.37 H1697M דָּבָר da.var "word: because": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word דָּבָר, transliteration da.var; STEP gloss "word: because"; sense head "because".
- **Senses (first level of the meaning tree of the lemma H1697):** speech, word, speaking, thing.
- **Related terms (30):** H1682 de.vo.rah "bee"; H1683G de.vo.rah "Deborah"; H1683H de.vo.rah "Deborah"; H1687 de.vir "sanctuary"; H1688A de.vir "Debir"; H1688B lid.vir "Debir"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (medium).
- **Counts, three measures as stored:** STEP token count 33; verses STEP attests 33; verse_lexical rows the parse found 33.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Neh 8:4 | purpose | HNcmsa | none recorded | - | 0 | And Ezra the scribe stood on a wooden platform that they had made for the **purpose**. And beside him stood Mattithiah, Shema, Anaiah, Uriah, Hilkiah, and Maaseiah on his right hand, and Pedaiah, Mishael, Malchijah, Hashum, Hashbaddanah, Zechariah, and Meshullam on his left hand. |

### 3.38 H1819 דָּמָה da.mah "to resemble": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word דָּמָה, transliteration da.mah; STEP gloss "to resemble"; sense head "to resemble" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1819):** to be like, resemble.
- **Related terms (3):** H1821 de.mah "be like"; H1823 de.mut "likeness"; H1825 dim.yon "likeness".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 30; verses STEP attests 28; verse_lexical rows the parse found 30.

- **Carried by the member words:** intend (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 10:7 | intend | HVpi3ms | none recorded | 12407, 12416 | 0 | But he does not so **intend**, and his heart does not so think; but it is in his heart to destroy, and to cut off nations not a few; |

### 3.39 H2154 זִמָּה zim.mah "wickedness": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word זִמָּה, transliteration zim.mah; STEP gloss "wickedness"; sense head "wickedness" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2154):** plan, device, wickedness, evil plan, mischievous purpose.
- **Related terms (6):** H2155G zim.mah "Zimmah"; H2155H zim.mah "Zimmah"; H2157 zam.zum.mim "Zamzummin"; H2161 za.mam "to plan"; H2162 za.mam "plan"; H4209 me.zim.mah "plot".
- **Clusters (cluster_strong):** M58 Wickedness (None).
- **Counts, three measures as stored:** STEP token count 29; verses STEP attests 27; verse_lexical rows the parse found 29.

- **Carried by the member words:** plans (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 17:11 | plans | HNcfpc | none recorded | - | 0 | My days are past; my **plans** are broken off, the desires of my heart. |

### 3.40 H2790A חָרַשׁ cha.rash "to plow/plot": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָרַשׁ, transliteration cha.rash; STEP gloss "to plow/plot"; sense head "to plow/plot" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2790):** to cut in, plough, engrave, devise.
- **Related terms (13):** H2758 cha.rish "plowing"; H2759 cha.ri.shi "scorching"; H2790B cha.resh "be quiet"; H2791A che.resh "silently"; H2791B che.resh "craftily"; H2793G cho.resh "Horesh"; more in the workbook.
- **Clusters (cluster_strong):** M06 Malice & Enmity (heuristic).
- **Counts, three measures as stored:** STEP token count 26; verses STEP attests 22; verse_lexical rows the parse found 25.

- **Carried by the member words:** plan (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 3:29 | plan | HVqj2ms | none recorded | - | 0 | Do not **plan** evil against your neighbor, who dwells trustingly beside you. |

### 3.41 H3335I יָצַר ya.tsar "to form: plan": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word יָצַר, transliteration ya.tsar; STEP gloss "to form: plan"; sense head "plan".
- **Senses (first level of the meaning tree of the lemma H3335):** to form, fashion, frame.
- **Related terms (8):** H3334 ya.tsar "be distressed"; H3335G ya.tsar "to form: formed"; H3335H ya.tsar "to form: potter"; H3336 ye.tser "intention"; H3337 ye.tser "Jezer"; H3338 ye.tsu.rim "member"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 6; verse_lexical rows the parse found 6.

- **Carried by the member words:** purposed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 46:11 | purposed | HVqp1cs | none recorded | - | 0 | calling a bird of prey from the east, the man of my counsel from a far country. I have spoken, and I will bring it to pass; I have **purposed**, and I will do it. |

### 3.42 H3820A לֵב lev "heart": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word לֵב, transliteration lev; STEP gloss "heart"; sense head "heart" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3820):** inner man, mind, will, heart, understanding.
- **Related terms (14):** H1079 bal "mind"; H3820B lev "Leb"; H3821 lev "heart"; H3823A la.vav "to encourage"; H3823B lib.bev "to bake"; H3824 le.vav "heart"; more in the workbook.
- **Clusters (cluster_strong):** M47 Inner Seat (None).
- **Counts, three measures as stored:** STEP token count 603; verses STEP attests 550; verse_lexical rows the parse found 594.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ch 12:33 | purpose | HNcmsa | none recorded | - | 0 | Of Zebulun 50,000 seasoned troops, equipped for battle with all the weapons of war, to help David with singleness of **purpose**. |

### 3.43 H4399 מְלָאכָה me.la.khah "work": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מְלָאכָה, transliteration me.la.khah; STEP gloss "work"; sense head "work" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4399):** occupation, work, business.
- **Related terms (6):** H3815 la.el "Lael"; H4397G mal.akh "messenger"; H4397H mal.akh "messenger: angel"; H4398 mal.akh "angel"; H4400 mal.a.khut "message"; H4401 mal.a.khi "Malachi".
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 173; verses STEP attests 0; verse_lexical rows the parse found 166.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lev 11:32 | purpose | HNcfsa | none recorded | - | 0 | And anything on which any of them falls when they are dead shall be unclean, whether it is an article of wood or a garment or a skin or a sack, any article that is used for any **purpose**. It must be put into water, and it shall be unclean until the evening; then it shall be clean. |

### 3.44 H4616 מַ֫עַן ma.an "because": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מַ֫עַן, transliteration ma.an; STEP gloss "because"; sense head "because" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4616):** purpose, intent prep.
- **Related terms (13):** H3282 ya.an "because"; H4617 ma.a.neh "answer"; H5772 o.nah "cohabitation"; H6030A un "to dwell"; H6030B a.nah "to answer"; H6030C a.nah "to sing"; more in the workbook.
- **Clusters (cluster_strong):** T6 Connective (high).
- **Counts, three measures as stored:** STEP token count 272; verses STEP attests 252; verse_lexical rows the parse found 272.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Neh 6:13 | purpose | HTc | none recorded | - | 0 | For this **purpose** he was hired, that I should be afraid and act in this way and sin, and so they could give me a bad name in order to taunt me. |

### 3.45 H4617 מַעֲנֶה ma.a.neh "answer": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מַעֲנֶה, transliteration ma.a.neh; STEP gloss "answer"; sense head "answer" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4617):** answer, response; (TWOT) place for task.
- **Related terms (13):** H3282 ya.an "because"; H4616 ma.an "because"; H5772 o.nah "cohabitation"; H6030A un "to dwell"; H6030B a.nah "to answer"; H6030C a.nah "to sing"; more in the workbook.
- **Clusters (cluster_strong):** M41 Being Heard (heuristic).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 7; verse_lexical rows the parse found 7.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 16:4 | purpose | HNcmsc | none recorded | - | 0 | The Lord has made everything for its **purpose**, even the wicked for the day of trouble. |

### 3.46 H4633 מַעֲרָךְ ma.a.rakh "plan": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מַעֲרָךְ, transliteration ma.a.rakh; STEP gloss "plan"; sense head "plan" (the code is its own lemma).
- **Related terms (6):** H4630 ma.a.rah "army"; H4634 ma.a.ra.khah "rank"; H4635 ma.a.re.khet "row"; H6186A a.rakh "to arrange"; H6186B a.rakh "to value"; H6187 e.rekh "valuation".
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** plans (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 16:1 | plans | HNcmpc | none recorded | - | 0 | The **plans** of the heart belong to man, but the answer of the tongue is from the Lord. |

### 3.47 H4639G מַעֲשֶׂה ma.a.seh "deed: work": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מַעֲשֶׂה, transliteration ma.a.seh; STEP gloss "deed: work"; sense head "work/product".
- **Senses (first level of the meaning tree of the lemma H4639):** deed, work.
- **Related terms (43):** H3299 ve.ya.a.so "Jaasu"; H3300G ya.a.si.el "Jaasiel"; H3300H ya.a.si.el "Jaasiel"; H4639H ma.a.seh "deed: justice"; H4639I ma.a.seh "deed: judgement"; H4639J ma.a.seh "deed: custom"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 186; verses STEP attests 0; verse_lexical rows the parse found 185.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 54:16 | purpose | HNcmsc | none recorded | - | 0 | Behold, I have created the smith who blows the fire of coals and produces a weapon for its **purpose**. I have also created the ravager to destroy; |

### 3.48 H4941J מִשְׁפָּט mish.pat "justice: custom": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מִשְׁפָּט, transliteration mish.pat; STEP gloss "justice: custom"; sense head "custom/manner".
- **Senses (first level of the meaning tree of the lemma H4941):** judgment, justice, ordinance.
- **Related terms (23):** H4941G mish.pat "justice: judgement"; H4941H mish.pat "justice"; H4941I mish.pat "justice: rule"; H4941K mish.pat "[Hall of] Judgment"; H8196 she.phot "judgment"; H8199 sha.phat "to judge"; more in the workbook.
- **Clusters (cluster_strong):** M12 Righteousness & Integrity (heuristic).
- **Counts, three measures as stored:** STEP token count 27; verses STEP attests 24; verse_lexical rows the parse found 24.

- **Carried by the member words:** plan (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 26:30 | plan | HNcmsc | none recorded | - | 0 | Then you shall erect the tabernacle according to the **plan** for it that you were shown on the mountain. |

### 3.49 H5475 סוֹד sod "counsel": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word סוֹד, transliteration sod; STEP gloss "counsel"; sense head "counsel" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5475):** council, counsel, assembly.
- **Related terms (1):** H5476 so.di "Sodi".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (heuristic).
- **Counts, three measures as stored:** STEP token count 21; verses STEP attests 21; verse_lexical rows the parse found 21.

- **Carried by the member words:** plans (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 83:3 | plans | HNcmsa | none recorded | - | 0 | They lay crafty **plans** against your people; they consult together against your treasured ones. |

### 3.50 H5668 עָבוּר a.vur "for the sake of": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָבוּר, transliteration a.vur; STEP gloss "for the sake of"; sense head "for the sake of" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5668):** for the sake of, on account of, because of, in order to; in order that.
- **Related terms (24):** H4569A ma.a.var "ford"; H4569B ma.a.va.rah "ford"; H5669 a.vur "produce"; H5674A a.var "to pass"; H5674B a.var "be angry"; H5674C a.var "to pass: bring"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 49; verses STEP attests 47; verse_lexical rows the parse found 49.

- **Carried by the member words:** purpose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 9:16 | purpose | HNcmsa | none recorded | - | 0 | But for this **purpose** I have raised you up, to show you my power, so that my name may be proclaimed in all the earth. |

### 3.51 H6250 עֶשְׁתֹּנָה esh.to.nah "thought": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עֶשְׁתֹּנָה, transliteration esh.to.nah; STEP gloss "thought"; sense head "thought" (the code is its own lemma).
- **Related terms (10):** H6245A a.shat "to gleam"; H6245B a.shat "to think"; H6248 ash.tut "thought"; H6249 ash.te "eleven"; H6251 ash.ta.rot "young"; H6252G ash.ta.rot "Ashtaroth"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** plans (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 146:4 | plans | HNcfpc | none recorded | 15965, 17264, 17280, 17282, 17283, 18484, 20489, 20512 | 0 | When his breath departs, he returns to the earth; on that very day his **plans** perish. |

### 3.52 H6440H פָּנֶה pa.neh "face": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word פָּנֶה, transliteration pa.neh; STEP gloss "face"; sense head "face".
- **Senses (first level of the meaning tree of the lemma H6440):** face.
- **Related terms (16):** H3312G ye.phun.neh "Jephunneh"; H3312H ye.phun.neh "Jephunneh"; H6437G pa.nah "to turn"; H6437H pa.nah "Corner [Gate]"; H6439G pe.nu.el "Peniel"; H6439H pe.nu.el "Penuel"; more in the workbook.
- **Clusters (cluster_strong):** T14 Body-Parts (None).
- **Counts, three measures as stored:** STEP token count 417; verses STEP attests 0; verse_lexical rows the parse found 400.

- **Carried by the member words:** intended (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ch 32:2 | intended | HNcmpc | none recorded | - | 0 | And when Hezekiah saw that Sennacherib had come and **intended** to fight against Jerusalem, |

### 3.53 H7760K שׂוּם sum "to set: consider": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שׂוּם, transliteration sum; STEP gloss "to set: consider"; sense head "consider".
- **Senses (first level of the meaning tree of the lemma H7760):** to put, place, set, appoint, make.
- **Related terms (12):** H3450 ye.shi.mi.el "Jesimiel"; H7760A sum "to set: make"; H7760B su.mah "fate"; H7760H sum "to set: put"; H7760I sum "to set: take"; H7760J sum "to set: accuse"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 29; verses STEP attests 0; verse_lexical rows the parse found 29.

- **Carried by the member words:** plans (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 9:8 | plans | HVqi3ms | none recorded | - | 0 | Their tongue is a deadly arrow; it speaks deceitfully; with his mouth each speaks peace to his neighbor, but in his heart he **plans** an ambush for him. |

### 3.54 Occurrences where the member surface is shared with another code's unit (21)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| 1Ki 5:5 | intend | H0559 אָמַר a.mar "to say" | intend | content_part | 4 | none recorded | - | 0 | And so I **intend** to build a house for the name of the Lord my God, as the Lord said to David my father, ‘Your son, whom I will set on your throne in your place, shall build the house for my name.’ |
| Isa 19:17 | purposed | H0834A אֲשֶׁר a.sher "which" | purposed | content_part | 3 | none recorded | - | 0 | And the land of Judah will become a terror to the Egyptians. Everyone to whom it is mentioned will fear because of the purpose that the Lord of hosts has **purposed** against them. |
| Zec 8:14 | purposed | H0834A אֲשֶׁר a.sher "which" | purposed | content_part | 2 | none recorded | - | 0 | For thus says the Lord of hosts: “ As I **purposed** to bring disaster to you when your fathers provoked me to wrath, and I did not relent, says the Lord of hosts, |
| Judg 20:5 | meant | H0853 אֵת et "[Obj.]" | meant | content_part | 3 | none recorded | - | 0 | And the leaders of Gibeah rose against me and surrounded the house against me by night. They **meant** to kill me, and they violated my concubine, and she is dead. |
| 1Ch 28:11 | plan | H0853 אֵת et "[Obj.]" | plan | content_part | 3 | none recorded | - | 0 | Then David gave Solomon his son the **plan** of the vestibule of the temple, and of its houses, its treasuries, its upper rooms, and its inner chambers, and of the room for the mercy seat; |
| Neh 4:15 | plan | H0853 אֵת et "[Obj.]" | plan | content_part | 2 | none recorded | - | 0 | When our enemies heard that it was known to us and that God had frustrated their **plan**, we all returned to the wall, each to his work. |
| Jer 19:7 | plans | H0853 אֵת et "[Obj.]" | plans | content_part | 2 | none recorded | - | 0 | And in this place I will make void the **plans** of Judah and Jerusalem, and will cause their people to fall by the sword before their enemies, and by the hand of those who seek their life. I will give their dead bodies for food to the birds of the air and to the beasts of the earth. |
| Jer 29:11 | plans | H0853 אֵת et "[Obj.]" | plans | content_part | 3 | none recorded | - | 0 | For I know the **plans** I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope. |
| Eze 43:10 | plan | H0853 אֵת et "[Obj.]" | plan | content_part | 2 | none recorded | - | 0 | “As for you, son of man, describe to the house of Israel the temple, that they may be ashamed of their iniquities; and they shall measure the **plan**. |
| Judg 20:5 | meant | H1819 דָּמָה da.mah "to resemble" | meant | content_part | 3 | none recorded | - | 0 | And the leaders of Gibeah rose against me and surrounded the house against me by night. They **meant** to kill me, and they violated my concubine, and she is dead. |
| Isa 19:17 | purposed | H1931 הוּא hu "he/she/it" | purposed | content_part | 3 | none recorded | - | 0 | And the land of Judah will become a terror to the Egyptians. Everyone to whom it is mentioned will fear because of the purpose that the Lord of hosts has **purposed** against them. |
| 1Ki 5:5 | intend | H2005 הֵן hen "look!" | intend | content_part | 4 | none recorded | - | 0 | And so I **intend** to build a house for the name of the Lord my God, as the Lord said to David my father, ‘Your son, whom I will set on your throne in your place, shall build the house for my name.’ |
| Zec 8:14 | purposed | H2161 זָמַם za.mam "to plan" | purposed | content_part | 2 | none recorded | 13556, 13873, 14632, 19412 | 0 | For thus says the Lord of hosts: “ As I **purposed** to bring disaster to you when your fathers provoked me to wrath, and I did not relent, says the Lord of hosts, |
| Isa 19:17 | purposed | H3289 יָעַץ ya.ats "to advise" | purposed | content_part | 3 | none recorded | - | 0 | And the land of Judah will become a terror to the Egyptians. Everyone to whom it is mentioned will fear because of the purpose that the Lord of hosts has **purposed** against them. |
| Psa 21:11 | plan | H3588A כִּי ki "for" | plan | content_part | 2 | none recorded | - | 0 | Though they **plan** evil against you, though they devise mischief, they will not succeed. |
| Jer 29:11 | plans | H4284 מַחֲשָׁבָה ma.cha.sha.vah "plot" | plans | content_part | 3 | none recorded | 12430, 19415, 20024, 20443, 20458, 20471, 20492, 20536 | 0 | For I know the **plans** I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope. |
| Psa 21:11 | plan | H5186 נָטָה na.tah "to stretch" | plan | content_part | 2 | none recorded | - | 0 | Though they **plan** evil against you, though they devise mischief, they will not succeed. |
| Neh 4:15 | plan | H6098 עֵצָה e.tsah "counsel" | plan | content_part | 2 | none recorded | - | 0 | When our enemies heard that it was known to us and that God had frustrated their **plan**, we all returned to the wall, each to his work. |
| Jer 19:7 | plans | H6098 עֵצָה e.tsah "counsel" | plans | content_part | 2 | none recorded | - | 0 | And in this place I will make void the **plans** of Judah and Jerusalem, and will cause their people to fall by the sword before their enemies, and by the hand of those who seek their life. I will give their dead bodies for food to the birds of the air and to the beasts of the earth. |
| 1Ch 28:11 | plan | H8403 תַּבְנִית tav.nit "pattern" | plan | content_part | 3 | none recorded | - | 0 | Then David gave Solomon his son the **plan** of the vestibule of the temple, and of its houses, its treasuries, its upper rooms, and its inner chambers, and of the room for the mercy seat; |
| Eze 43:10 | plan | H8508 תׇּכְנִית tokh.nit "proportion" | plan | content_part | 2 | none recorded | - | 0 | “As for you, son of man, describe to the house of Israel the temple, that they may be ashamed of their iniquities; and they shall measure the **plan**. |

## 4. What the study has recorded for these occurrences

Of 167 occurrences, 0 have an engagement observation and 167 have none recorded. There are 187 live observations on them (0 engagement, 187 of other recorded stages, 0 of the retired catalogue stages) and 4 withdrawn.

### 4.1 Engagement: what each word does for the inner being (0 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

_no engagement observation covers these occurrences_

### 4.2 Other recorded observations (187)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 12939** (prior-capture, tag statement, status draft): God's anger named with who God is: "The Lord, the Lord, a God merciful and gracious, slow to anger"; "I will not execute my burning anger … for I am God and not a man"; "until he has executed and accomplished the intents of his heart"; "I have no wrath".
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13206** (prior-capture, tag statement, status draft): God's heart is named with his anger three times: "My heart recoils within me" before "I will not execute my burning anger" (Hos 11:8–9); "the intents of his heart" (Jer 23:20); "the day of vengeance was in my heart, and my year of redemption had come" (Isa 63:4).
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13273** (prior-capture, tag statement, status draft): Time (existing): a moment; forever; until forgotten; until the intents of his heart; "how long?": Verses: Psa 30:5; Amo 1:11; Gen 27:45; Jer 23:20; Psa 79:5 (AG-29, 54, 31, 36).
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13279** (prior-capture, tag statement, status draft): F.2: What emerged: God's heart is named twice with his anger: the heart that recoils and the compassion that warms, before "I will not execute my burning anger" (Hos 11:8–9); and "the intents of his heart" that the anger accomplishes (Jer 23:20; 30:24).; What it changes elsewhere: Confirms and extends #1890 ("no text hardens God's own heart"): these two passages name God's heart in connection with his anger, one in restraint, one in purpose. Ch 13 quotes Jer 23:20 and Hos 11:9, but not Hos 11:8's heart line beside them (Hos 11:8 is in Ch 11 only). Proposed RS for the Ch 13 cross-check (OT-13).; Where: Ch 13; #1890 findings.
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13298** (prior-capture, tag link, status draft): anger continues until the intents of his heart are done → understanding later (Jer 23:20).
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13556** (prior-capture, tag link, status draft): provoked to wrath → ready to destroy you (Deu 9:8); fathers angered God → given into Nebuchadnezzar's hand → house destroyed (Ezr 5:12); purposed disaster, did not relent → so again purposed good → fear not (Zec 8:14–15).
  - applies to 2 occurrence(s): Zec 8:14 (purposed), Zec 8:15 (purposed)
- **Observation 13736** (prior-capture, tag statement, status draft): Whose seat the anger points to, The angry party's own seat: genuine links Human: Job 36:13 "the godless in heart cherish anger"; Job 18:4 "you who tear yourself in your anger"; Pro 14:29 / 16:32 (slow to anger with "rules his spirit"); Ecc 7:9 "anger lodges in the heart of fools"; Act 17:16 Paul's "spirit was provoked within him". Divine: Jer 23:20 / 30:24 "the intents of his heart / mind". What it implies for the no-seat verses: The human anger narratives (§2.1 below) and the wisdom sayings (§2.2).
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13756** (prior-capture, tag statement, status draft): God's own seat in resolve and purpose, none of it hardened: he "said in his heart, 'I will never again curse the ground'" (Gen 8:21); "what is in my heart" (1Sa 2:35); "a man after his own heart" (1Sa 13:14; Act 13:22); "my eyes and my heart will be there" (1Ki 9:3; 2Ch 7:16); 2Ki 10:30; 1Ch 17:19; Psa 33:11; "the day of vengeance was in my heart" (Isa 63:4); "the intents of his heart" (Jer 23:20; 30:24); "with all my heart and all my soul" (Jer 32:41); Job 7:17; 10:13; 34:14.
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 13873** (prior-capture, tag statement, status draft): Zec 8:14 (4B People provoke the Lord to wrath): purposed disaster when provoked, and did not relent.
  - applies to 1 occurrence(s): Zec 8:14 (purposed)
- **Observation 14322** (prior-capture, tag statement, status draft): Where it comes from. The enemy's heart: "in your hearts you devise wrongs" (Psa 58:2); "who plan evil things in their heart and stir up wars continually" (140:2); they are "estranged from the womb" (58:3).
  - applies to 1 occurrence(s): Psa 140:2 (plan)
- **Observation 14479** (prior-capture, tag statement, status draft): SL §22: Context seats: sense · batch · use: Pro 14:30 tranquil heart, flesh · A v3 §4.3 et al. · used. Pro 17:27 cool spirit · B v3 §1.6 · used. Pro 19:18 heart ("do not set your heart on putting him to death") · G v3 §16.5 et al. · not used. Pro 19:21 "plans in the mind" · B v3 §2.6 · not used. Jam 1:21 souls · B v3 §4.4 · used.
  - applies to 1 occurrence(s): Pro 19:21 (plans)
- **Observation 14565** (prior-capture, tag statement, status draft): Part B: Psa 106:40: "they poured out innocent blood, the blood of their sons and daughters … Then the anger of the Lord was kindled against his people, and he abhorred his heritage; he gave them into the hand of the nations" (106:38–41); The psalm sums the whole cycle: "Many times he delivered them, but they were rebellious in their purposes and were brought low through their iniquity. Nevertheless, he looked upon their distress, when he heard their cry. For their sake he remembered his covenant, and relented" (106:43–45); This confirms the part-A reading that God answers the cry and the distress, not a completed repentance.
  - applies to 1 occurrence(s): Psa 106:43 (purposes)
- **Observation 14632** (prior-capture, tag statement, status draft): Part C: Zec 8:14. "As I purposed to bring disaster to you when your fathers provoked me to wrath, and I did not relent … so again have I purposed in these days to bring good to Jerusalem … fear not" (8:14–15): The human response asked for: "Fear not, but let your hands be strong" (8:13); "Speak the truth to one another" (8:16).
  - applies to 2 occurrence(s): Zec 8:14 (purposed), Zec 8:15 (purposed)
- **Observation 14715** (prior-capture, tag statement, status draft): What it does. "The anger of the Lord will not turn back until he has executed and accomplished the intents of his heart. In the latter days you will understand it clearly" (Jer 23:20). "Behold the storm of the Lord! Wrath has gone forth" (30:23), and "The fierce anger of the Lord will not turn back until he has executed and accomplished the intentions of his mind. In the latter days you will understand this" (30:24).
  - applies to 2 occurrence(s): Jer 23:20 (intents), Jer 30:24 (intentions)
- **Observation 15856** (prior-capture, tag statement, status draft): God's anger carries out his heart's intents: "The anger of the Lord will not turn back until he has executed and accomplished the intents of his heart" (Jer 23:20; 30:24 "mind").
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 15892** (prior-capture, tag statement, status draft): Planning peace: "those who plan peace have joy" (Pro 12:20).
  - applies to 1 occurrence(s): Pro 12:20 (plan)
- **Observation 15937** (prior-capture, tag statement, status draft): 9. Cross-cutting observations for Batch A [Claude reading]: Each component has its own feeling profile in the text, but they overlap: *Heart:* the widest range, including joy, fear, anger, grief, anxiety, despair.; *Soul:* strongly bitterness, longing, weariness, being troubled.; *Spirit (human):* troubled, broken or crushed, faint, provoked, rejoicing, and temper.; *Flesh:* trembles, faints, rejoices, and is afflicted by divine indignation.; The heart's state governs whether a feeling takes hold. A firm heart has no fear, a blameless heart no shame, a hardened heart no fear of God. A proud heart brings wrath; a humbled heart averts it.; Feelings pass between the inner seat and the body in b ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 15965** (prior-capture, tag statement, status draft): 1.11 ◆ Breath, wind and thought: "When his breath departs … on that very day his plans perish" (Psa 146:4) — the brief's thought link; "he who … creates the wind, and declares to man what is his thought" (Amo 4:13); "windy knowledge" (Job 15:2); "I applied my heart to know wisdom … this also is but a striving after wind" (Ecc 1:17); "Every man is stupid and without knowledge … there is no breath in them" (Jer 10:14; 51:17)
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 15974** (prior-capture, tag statement, status draft): 2.6 Counsel and plans: "take counsel in my soul" (Psa 13:2); "gave them over to their stubborn hearts, to follow their own counsels" (Psa 81:12; Jer 7:24); "Many are the plans in the mind [heart] of a man, but it is the purpose of the Lord that will stand" (Pro 19:21); "The purpose in a man's heart is like deep water" (Pro 20:5); "The counsel of the Lord stands forever, the plans of his heart" (Psa 33:11) — God's heart plans
  - applies to 4 occurrence(s): Psa 33:11 (plans), Pro 19:21 (plans), Pro 19:21 (purpose), Pro 20:5 (purpose)
- **Observation 15975** (prior-capture, tag statement, status draft): Plans without the Spirit: "who carry out a plan, but not mine, and who make an alliance, but not of my Spirit" (Isa 30:1) [D1]
  - applies to 1 occurrence(s): Isa 30:1 (plan)
- **Observation 16004** (prior-capture, tag statement, status draft): Dividing and discerning: "the word of God … piercing to the division of soul and of spirit … discerning the thoughts and intentions of the heart" (Heb 4:12).
  - applies to 1 occurrence(s): Heb 4:12 (intentions)
- **Observation 16031** (prior-capture, tag statement, status draft): Judgment and the inner seat: "who will … disclose the purposes of the heart" (1Co 4:5); "I said in my heart, God will judge" (Ecc 3:17); "an understanding mind to govern [judge]" (1Ki 3:9)
  - applies to 1 occurrence(s): 1Cor 4:5 (purposes)
- **Observation 16143** (prior-capture, tag statement, status draft): The kings of the Medes (filed under destroying Babylon): "The Lord has stirred up the spirit of the kings of the Medes, because his purpose concerning Babylon is to destroy it" (Jer 51:11) [H1]
  - applies to 1 occurrence(s): Jer 51:11 (purpose)
- **Observation 16302** (prior-capture, tag statement, status draft): Praise from God, not from people: "circumcision is a matter of the heart, by the Spirit … His praise is not from man but from God" (Rom 2:29) [U]; "will disclose the purposes of the heart. Then each one will receive his commendation from God" (1Co 4:5)
  - applies to 1 occurrence(s): 1Cor 4:5 (purposes)
- **Observation 16410** (prior-capture, tag statement, status draft): From the heart: "if you do not forgive your brother from your heart" (Mat 18:35); "that, if possible, the intent of your heart may be forgiven you" (Act 8:22); "with the heart one believes … with the mouth one confesses" (Rom 10:9–10)
  - applies to 1 occurrence(s): Act 8:22 (intent)
- **Observation 16535** (prior-capture, tag statement, status draft): Intention: "every intention of the thoughts of his heart was only evil continually" (Gen 6:5); "the intention of man's heart is evil from his youth" (Gen 8:21).
  - applies to 2 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention)
- **Observation 16538** (prior-capture, tag statement, status draft): Devising evil: "with perverted heart devises evil" (Pro 6:14); "a heart that devises wicked plans" (Pro 6:18); "Deceit is in the heart of those who devise evil" (Pro 12:20); "who plan evil things in their heart" (Psa 140:2); "let none of you devise evil against another in your heart" (Zec 7:10; 8:17); "their hearts shall be bent on doing evil" (Dan 11:27)
  - applies to 2 occurrence(s): Psa 140:2 (plan), Pro 6:18 (plans)
- **Observation 16982** (prior-capture, tag statement, status draft): 12.2 The heart devising and muttering violence — one verb, opposite content: *hāgâ* "mutter, meditate" [lexical]: "The heart of the righteous ponders how to answer, but the mouth of the wicked pours out evil things" (Pro 15:28); "for their hearts devise [*mutter*] violence, and their lips talk of trouble" (Pro 24:2); "conceiving and uttering from the heart lying words" (Isa 59:13); "Your heart will muse on the terror" (Isa 33:18); "those who seek my life … meditate treachery all day long" (Psa 38:12); [Claude reading] The heart's inner murmuring is the same act for the righteous and the violent. Its content (how to answer / violence / lies / terror) decides its moral character. The heart is ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 140:2 (plan)
- **Observation 17053** (prior-capture, tag statement, status draft): 2.1 The heart plans and devises: "The heart of man plans his way, but the Lord establishes his steps" (Pro 16:9)
  - applies to 1 occurrence(s): Pro 16:9 (plans)
- **Observation 17054** (prior-capture, tag statement, status draft): Evil devised in the heart: "who plan evil things in their heart" (Psa 140:2); "let none of you devise evil against another in your heart" (Zec 7:10; 8:17); "thoughts will come into your mind, and you will devise an evil scheme" (Eze 38:10); "his heart does not so think; but it is in his heart to destroy" (Isa 10:7)
  - applies to 1 occurrence(s): Psa 140:2 (plan)
- **Observation 17057** (prior-capture, tag statement, status draft): 2.2 The intention of the heart: "every intention of the thoughts of his heart was only evil continually" (Gen 6:5); "the intention of man's heart is evil from his youth" (Gen 8:21) — said by the Lord "in his heart"; "keep forever such purposes and thoughts in the hearts of your people, and direct their hearts toward you" (1Ch 29:18); "the Lord searches all hearts and understands every plan and thought" (1Ch 28:9); "disclose the purposes of the heart" (1Co 4:5)
  - applies to 5 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention), 1Ch 28:9 (plan), 1Ch 29:18 (purposes), 1Cor 4:5 (purposes)
- **Observation 17058** (prior-capture, tag statement, status draft): Steadfast purpose [of heart]: "remain faithful to the Lord with steadfast purpose" (Act 11:23).
  - applies to 1 occurrence(s): Act 11:23 (purpose)
- **Observation 17059** (prior-capture, tag statement, status draft): Resolved: "You have tried my heart … I have purposed that my mouth will not transgress" (Psa 17:3); "Daniel resolved [*set on his heart*] that he would not defile himself" (Dan 1:8).
  - applies to 1 occurrence(s): Psa 17:3 (purposed)
- **Observation 17065** (prior-capture, tag statement, status draft): Planning according to the flesh = vacillating: "Do I make my plans according to the flesh, ready to say 'Yes, yes' and 'No, no' at the same time?" (2Co 1:17).
  - applies to 1 occurrence(s): 2Cor 1:17 (plans)
- **Observation 17131** (prior-capture, tag statement, status draft): 8.1 Returning with heart and soul: "if they turn their heart [*bring back to heart*] … and repent" (1Ki 8:47; 2Ch 6:37); "if they repent with all their heart and with all their soul" (1Ki 8:48; 2Ch 6:38); "If you are returning to the Lord with all your heart, then put away the foreign gods … and direct your heart to the Lord" (1Sa 7:3); "put away the foreign gods … and incline your heart to the Lord" (Jos 24:23); "rend your hearts and not your garments. Return to the Lord your God" (Joe 2:13); "lest they … understand with their hearts, and turn and be healed" (Isa 6:10; Joh 12:40); "the intent of your heart may be forgiven you" (Act 8:22)
  - applies to 1 occurrence(s): Act 8:22 (intent)
- **Observation 17146** (prior-capture, tag statement, status draft): 9.1 The stubbornness of the heart (*šerîrût lēv*): "I shall be safe, though I walk in the stubbornness of my heart" (Deu 29:19) — the heart blessing itself; "So I gave them over to their stubborn hearts, to follow their own counsels" (Psa 81:12); "everyone walked in the stubbornness of his evil heart" (Jer 11:8); "walked in their own counsels and the stubbornness of their evil hearts, and went backward and not forward" (Jer 7:24); "who … stubbornly follow their own heart and have gone after other gods" (Jer 13:10; 9:14); "every one of you follows his stubborn, evil will [*heart*], refusing to listen to me" (Jer 16:12); "We will follow our own plans, and will every one act according to the st ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 18:12 (plans)
- **Observation 17236** (prior-capture, tag statement, status draft): d. Thinking, planning, understanding, remembering: *Plans and devising:* Pro 16:1, 9; 19:21; 6:14, 18; 24:2; 12:20; Psa 140:2; 58:2; Zec 7:10; 8:17; Isa 10:7; Act 5:4; Eze 38:10.; *Understanding and knowing:*; "a heart to understand" (Deu 29:4); "understanding mind" (1Ki 3:9); "understand with their hearts" (Isa 6:10; Mat 13:15; Joh 12:40; Act 28:27); "an intelligent heart acquires knowledge" (Pro 18:15); "the heart of the hasty will understand" (Isa 32:4); *Remembering and "laying to heart":*; Isa 47:7; 57:1, 11; 42:25; Mal 2:2; Jer 12:11; Ecc 7:2; 9:1; Deu 4:39; 32:46; 1Sa 21:12; "call to mind" (Lam 3:21; Deu 30:1); "come into mind" (Jer 3:16; 7:31; 19:5; 32:35; 44:21; 51:50; Isa 65:17); H ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Pro 6:18 (plans), Pro 16:9 (plans), Pro 19:21 (plans)
- **Observation 17237** (prior-capture, tag statement, status draft): e. Willing, deciding, purposing, being moved: *Deciding:*; "Daniel resolved" (Dan 1:8); "Joash decided" (2Ch 24:4); "has determined this in his heart" (1Co 7:37); "Each one must give as he has decided in his heart" (2Co 9:7); "of my own will / accord" (Num 24:13; 16:28, lēv); "It is in my heart to make a covenant" (2Ch 29:10); "I had it in my heart to build a house" (1Ch 22:7; 28:2; 1Ki 8:17–18); *Being moved to give:* "everyone whose heart stirred him … and everyone whose spirit moved him" (Exo 35:21); also Exo 25:2; 35:5, 22, 26, 29; 36:2; 2Ki 12:4 ("the money that a man's heart prompts him to bring").; *Intention as depth:* "The purpose in a man's heart is like deep water, but a man of un ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 20:5 (purpose)
- **Observation 17244** (prior-capture, tag statement, status draft): l. The heart's opacity and privacy: "The heart is deceitful above all things, and desperately sick; who can understand it?" (Jer 17:9); "the heart of kings is unsearchable" (Pro 25:3); "The heart knows its own bitterness, and no stranger shares its joy" (Pro 14:10); "he knows the secrets of the heart" (Psa 44:21); "the secrets of his heart are disclosed" (1Co 14:25); "disclose the purposes of the heart" (1Co 4:5); Only God knows it: 1Ki 8:39; 2Ch 6:30; 1Sa 16:7 ("man looks on the outward appearance, but the Lord looks on the heart"); Luk 16:15; Act 1:24 ("heart-knower"); Act 15:8; "who can say, 'I have made my heart pure'?" (Pro 20:9)
  - applies to 1 occurrence(s): 1Cor 4:5 (purposes)
- **Observation 17264** (prior-capture, tag statement, status draft): e. Wind and breath in relation to the inner being — explicitly retained per the researcher: *Breath = life in flesh:*; "all flesh in which is the breath of life" (Gen 6:17; 7:15, 22); "sinews … flesh … skin … But there was no breath in them" → "breath came into them, and they lived" (Eze 37:6–10); "When you take away their breath, they die and return to their dust" (Psa 104:29); *Breath and thought:* "When his breath departs, he returns to the earth; on that very day his plans perish" (Psa 146:4). Link to the thought vocabulary (see brief §5).; *Breath as frailty:* "Remember that my life is a breath" (Job 7:7); "They all have the same breath, and man has no advantage over the beasts" (Ecc 3: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 17267** (prior-capture, tag statement, status draft): b. Greek *sarx*: *Neutral uses continue:* one flesh; all flesh; "the Word became flesh" (Joh 1:14); "in the days of his flesh" (Heb 5:7); "flesh and blood" (Heb 2:14; Mat 16:17); "a thorn … in the flesh" (2Co 12:7); "our bodies had no rest … fighting without and fear within" (2Co 7:5).; *Pauline and Petrine ethical flesh — flesh as an inner orientation:*; "the desires of the flesh and the desires of the eyes" (1Jo 2:16); "the passions of our flesh, carrying out the desires of the flesh and the mind" (Eph 2:3); "the works of the flesh" (Gal 5:19); "crucified the flesh with its passions and desires" (Gal 5:24); "nothing good dwells in me, that is, in my flesh. For I have the desire to do what ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Cor 1:17 (plans)
- **Observation 17274** (prior-capture, tag statement, status draft): 3.4 Distinction — where the text separates the components: *Division of soul and spirit (Heb 4:12):* "piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart." [Claude reading] Soul and spirit are close enough that only the word of God can separate them, just as joints and marrow are adjacent parts of the body. The heart is where the *thoughts and intentions* are, and they are *discerned* there.; *Living soul vs life-giving spirit:* "The first man Adam became a living being [psychē]; the last Adam became a life-giving spirit" (1Co 15:45; cf. Gen 2:7).; *Spirit vs mind:* 1Co 14:14–15 (above).; *Spirit vs flesh (as kind): ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Heb 4:12 (intentions)
- **Observation 17277** (prior-capture, tag statement, status draft): 3.6 Cause and effect between inner seat, body and senses: *Appetite (soul) and heart:* "They tested God in their heart by demanding the food they craved" (Psa 78:18); the fool's heart "busy with iniquity … to leave the craving of the hungry unsatisfied" (Isa 32:6); "you crave meat" (Deu 12:20).; *Heart → mouth, hands, feet, deeds:* §2.1h. Also: "clean hands and a pure heart" (Psa 24:4); "Let us lift up our hearts and hands to God" (Lam 3:41); "a heart that devises wicked plans, feet that make haste to run to evil" (Pro 6:18); "The heart of man plans his way, but the Lord establishes his steps" (Pro 16:9); "The law of his God is in his heart; his steps do not slip" (Psa 37:31); *Heart ↔ ears ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Pro 6:18 (plans), Pro 16:9 (plans)
- **Observation 17280** (prior-capture, tag statement, status draft): 3.9 The boundary of death — where the components come apart: *Soul departs:* "as her soul was departing" (Gen 35:18); soul to Sheol, pit, silence (§2.2d).; *Spirit and breath return to God:*; "the dust returns to the earth as it was, and the spirit returns to God who gave it" (Ecc 12:7); "Who knows whether the spirit of man goes upward and the spirit of the beast goes down into the earth?" (Ecc 3:21); "When you take away their breath, they die and return to their dust" (Psa 104:29); "Into your hand I commit my spirit" (Psa 31:5; Luk 23:46; Act 7:59); "No man has power to retain the spirit" (Ecc 8:8); *Return to life:*; "her spirit returned, and she got up" (Luk 8:55); "the life of the child ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 17281** (prior-capture, tag statement, status draft): 3.10 God, animals and things — the vocabulary is not limited to humans ◆ fringe: *God has a heart:* grieved (Gen 6:6); speaks in it (Gen 8:21); "a man after my own heart" (1Sa 13:14; Act 13:22); "My heart recoils within me; my compassion grows warm and tender" (Hos 11:8); "he does not afflict from his heart" (Lam 3:33); "my eyes and my heart will be there" (1Ki 9:3); "the intents of his heart" (Jer 23:20); "with all my heart and all my soul" (Jer 32:41).; *God has a soul:* "my soul hates" (Isa 1:14); "my soul delights" (Isa 42:1; Mat 12:18); "my soul shall not abhor you" (Lev 26:11); "Does your soul loathe Zion?" (Jer 14:19); "my soul has no pleasure in him" (Heb 10:38); "The Lord God has sw ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 17282** (prior-capture, tag statement, status draft): 4. Fringe observations collected (quick list): Heart = "midst" of sea, heaven, earth; the inner seat named as the *middle* (§2.1a).; Aaron carries the tribes "on his heart" before the Lord (Exo 28:29–30).; "I slept, but my heart was awake" (Song 5:2).; "Eyes of your hearts" (Eph 1:18); morning star rising in hearts (2Pe 1:19); a veil over hearts (2Co 3:15).; "Walls of my heart" (Jer 4:19); "tear open their breast" (Hos 13:8); a man without self-control = "a city … without walls" (Pro 25:28, rûaḥ). The inner seat is imaged as an enclosure.; Nabal's heart "died within him, and he became as a stone" after the wine left (1Sa 25:37).; Nephesh = neck/throat (Psa 69:1; 105:18) and = corpse (Num 19: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 17283** (prior-capture, tag statement, status draft): 4. Fringe observations collected (quick list): God's own heart and soul (§3.10).
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 17353** (prior-capture, tag statement, status draft): 27 | Isa 55:11 | purpose |
  - applies to 1 occurrence(s): Isa 55:11 (purpose)
- **Observation 17508** (prior-capture, tag statement, status draft): Isa 55:11 | the word going out and doing its work | "purpose" is a delight word | 13.1, *Purposing* (out of *Delight*)
  - applies to 1 occurrence(s): Isa 55:11 (purpose)
- **Observation 17520** (prior-capture, tag statement, status draft): Isa 44:28. *"who says of Cyrus, 'He is my shepherd, and he shall fulfill all my purpose'"*. It closes a chain of "who says": *"who confirms the word of his servant and fulfills the counsel of his messengers"* (44:26).
  - applies to 1 occurrence(s): Isa 44:28 (purpose)
- **Observation 17521** (prior-capture, tag statement, status draft): Isa 46:10–11. *"declaring the end from the beginning … saying, 'My counsel shall stand, and I will accomplish all my purpose' … I have spoken, and I will bring it to pass; I have purposed, and I will do it."* The setting is *"Remember this and stand firm … remember the former things of old; for I am God, and there is no other"* (46:8–9).
  - applies to 1 occurrence(s): Isa 46:10 (purpose)
- **Observation 17566** (prior-capture, tag statement, status draft): 13.1 *Purposing*: Isa 44:28; 46:10–11; 48:14 (his purpose, spoken and carried out by another)
  - applies to 3 occurrence(s): Isa 44:28 (purpose), Isa 46:10 (purpose), Isa 48:14 (purpose)
- **Observation 17582** (prior-capture, tag statement, status draft): Isa 48:14. *"Who among them has declared these things? The Lord loves him; he shall perform his purpose on Babylon."*
  - applies to 1 occurrence(s): Isa 48:14 (purpose)
- **Observation 17616** (prior-capture, tag statement, status draft): Purposing: "it shall accomplish that which I purpose" (Isa 55:11). The word is the delight word. His word carries out his delight and does not return empty.
  - applies to 1 occurrence(s): Isa 55:11 (purpose)
- **Observation 17686** (prior-capture, tag statement, status draft): 2.3 D2. Plans held under God's will (8 verses): 10.7 *Planning* already has Paul's "often intended … prevented" (Rom 1:13) and James 4:15 ("If the Lord wills"). The group shows the same thing in Paul's own plans, and in what holds them back:
  - applies to 1 occurrence(s): Rom 1:13 (intended)
- **Observation 17699** (prior-capture, tag statement, status draft): Meaning to pass by. *"He meant to pass by them, but when they saw him walking on the sea they thought it was a ghost, and cried out … But immediately he spoke to them and said, 'Take heart; it is I. Do not be afraid'"* (Mar 6:48–50). The verse states the intention and does not explain it. Their terror is met at once with his word. Home: 10.12, beside "Fear not", as a pointer only. I place nothing on the intention itself.
  - applies to 1 occurrence(s): Mar 6:48 (meant)
- **Observation 18164** (prior-capture, tag statement, status draft): Toward destroying.: *"So the God of Israel stirred up the spirit of Pul king of Assyria"*, after *"they broke faith with the God of their fathers"* (1Ch 5:25–26); *"the Lord stirred up against Jehoram the anger of the Philistines"* (2Ch 21:16), after a written warning (21:12–15); *"I will stir up the spirit of a destroyer against Babylon"* (Jer 51:1); *"The Lord has stirred up the spirit of the kings of the Medes, because his purpose concerning Babylon is to destroy it"* (51:11); Each time the verses give the ground: broken faith, a king's sin, or his purpose and vengeance for his temple.
  - applies to 1 occurrence(s): Jer 51:11 (purpose)
- **Observation 18484** (prior-capture, tag statement, status draft): R2 | Breath lent | When the breath goes, a person's plans go with it | Psa 146:4; 144:4; 94:11
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 19041** (prior-capture, tag statement, status draft): The passage. *"he offered them money"* (8:18). Peter answers: *"you thought you could obtain the gift of God with money!"* (8:20); *"your heart is not right before God"* (8:21); *"pray to the Lord that, if possible, the intent of your heart may be forgiven you"* (8:22); *"I see that you are in the gall of bitterness and in the bond of iniquity"* (8:23)
  - applies to 1 occurrence(s): Act 8:22 (intent)
- **Observation 19067** (prior-capture, tag statement, status draft): The verses: *"he gave them into the hand of the nations, so that those who hated them ruled over them"* (Psa 106:41).; *"Many times he delivered them, but they were rebellious in their purposes … Nevertheless, he looked upon their distress, when he heard their cry"* (106:43–44).; *"But after they had rest they did evil again before you, and you abandoned them to the hand of their enemies, so that they had dominion over them. Yet when they turned and cried to you, you heard from heaven"* (Neh 9:28).
  - applies to 1 occurrence(s): Psa 106:43 (purposes)
- **Observation 19275** (prior-capture, tag statement, status draft): Seat.; In the verse, the victim's own (genuine): Psa 142:3 "When my spirit faints within me … they have hidden a trap for me". Batch A v3 §7 (Faintness & Despair, M24). → 142:4 "no one cares for my soul" (v2).; In the verse, the victim's life (life-sense): Psa 35:7 "without cause they dug a pit for my life". *Nephesh* here is the life aimed at, in its life sense. It passes the check as life, not as an inner faculty. New in v3: this verse was not read in the M47 batches. It is the same use as Batch G v3 §5.3 ("Hunting souls").; In the next verse, the trapper's (genuine): Psa 64:5 → 64:6 "the inward mind and heart of a man are deep" (v2). The heart is where the trap is first hidden, before the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 140:2 (plan)
- **Observation 19276** (prior-capture, tag statement, status draft): What the map shows. This phenomenon has three seats in three hands: the trapper's heart (the hiding place of the intent), the victim's spirit (fainting, then committed), and God's knowing of the victim's soul.
  - applies to 1 occurrence(s): Psa 140:2 (plan)
- **Observation 19351** (prior-capture, tag statement, status draft): Psa 140:5 (TR) | Psa 140:2 "plan evil things in their heart" | trappers' · genuine | §15 Seat
  - applies to 1 occurrence(s): Psa 140:2 (plan)
- **Observation 19399** (prior-capture, tag statement, status draft): G1013 *plan* (2 hits) is already in the will set, so it is not repeated here. Act 27:43 is the verse that set holds for G1013 together with G1014.
  - applies to 1 occurrence(s): Act 27:43 (plan)
- **Observation 19409** (prior-capture, tag statement, status draft): 1.1 He forms a plan and makes it known: *"Therefore hear the plan that the Lord has made against Edom and the purposes that he has formed against the inhabitants of Teman"* (Jer 49:20). The same words are used against Babylon in Jer 50:45.; In both passages the plan follows his question *"For who is like me? Who will summon me?"* (49:19; 50:44).; *"the Lord has both planned and done what he spoke concerning the inhabitants of Babylon"* (Jer 51:12).; The verse before gives the purpose and how it moves: *"The Lord has stirred up the spirit of the kings of the Medes, because his purpose concerning Babylon is to destroy it"* (51:11).; His purpose goes forward through the stirred spirit of other ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): Jer 49:20 (plan), Jer 49:20 (purposes), Jer 50:45 (plan), Jer 50:45 (purposes), Jer 51:11 (purpose)
- **Observation 19410** (prior-capture, tag statement, status draft): 1.2 His devising answers human devising: Micah 2 opens with those *"who devise wickedness and work evil on their beds"* (2:1), who *"covet fields and seize them"* (2:2). Then: *"Therefore thus says the Lord: behold, against this family I am devising disaster"* (2:3).; The same verb is used for both. The "therefore" ties his devising to theirs.; In Jeremiah 18 he says *"I am shaping disaster against you and devising a plan against you. Return"* (18:11). They answer: *"We will follow our own plans, and will every one act according to the stubbornness of his evil heart"* (18:12).; His plan and their plans stand in one exchange.
  - applies to 2 occurrence(s): Jer 18:11 (plan), Jer 18:12 (plans)
- **Observation 19411** (prior-capture, tag statement, status draft): 1.3 He states a plan so that people may turn, and he relents: Jer 18:7–10 sets out both directions.; If a nation he has spoken against *"turns from its evil, I will relent of the disaster that I intended to do to it"* (18:8).; If a nation he has promised to build *"does evil in my sight, not listening to my voice, then I will relent of the good that I had intended to do to it"* (18:10).; Both are set in the potter's house: *"like the clay in the potter's hand, so are you in my hand"* (18:6).; *"It may be they will listen, and every one turn from his evil way, that I may relent of the disaster that I intend to do to them"* (Jer 26:3).; *"It may be that the house of Judah will hear all the dis ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Jer 18:8 (intended), Jer 26:3 (intend), Jer 36:3 (intend)
- **Observation 19412** (prior-capture, tag statement, status draft): 1.4 He also purposes and does not turn back: *"for I have spoken; I have purposed; I have not relented, nor will I turn back"* (Jer 4:28). The verse before sets a limit within it: *"yet I will not make a full end"* (4:27).; *"As I purposed to bring disaster to you when your fathers provoked me to wrath, and I did not relent … so again have I purposed in these days to bring good to Jerusalem and to the house of Judah; fear not"* (Zec 8:14–15).; The fixed purpose is set beside a fixed purpose for good.; *"the unchangeable character of his purpose"* (Heb 6:17). He guaranteed it with an oath, *"so that … we who have fled for refuge might have strong encouragement to hold fast to the hope set bef ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Jer 4:28 (purposed), Zec 8:14 (purposed), Zec 8:15 (purposed), Heb 6:17 (purpose)
- **Observation 19414** (prior-capture, tag statement, status draft): 1.5 It is carried out, and people see afterward that it was his: *"The Lord has done what he purposed; he has carried out his word, which he commanded long ago"* (Lam 2:17).; *"The Lord determined to lay in ruins the wall of the daughter of Zion; he stretched out the measuring line; he did not restrain his hand"* (Lam 2:8).; Straight after 2:17: *"Their heart cried to the Lord … Pour out your heart like water before the presence of the Lord!"* (2:18–19). The fulfilled purpose is met with the heart poured out to the one who purposed it.; *"So they repented and said, 'As the Lord of hosts purposed to deal with us for our ways and deeds, so has he dealt with us'"* (Zec 1:6).; The fathers recogn ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Lam 2:17 (purposed), Zec 1:6 (purposed)
- **Observation 19415** (prior-capture, tag statement, status draft): 1.6 Plans for welfare, and thought for the one in need: *"For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope"* (Jer 29:11).; The verse looks ahead to *"When seventy years are completed"* (29:10).; It is followed by *"You will seek me and find me, when you seek me with all your heart"* (29:13).; *"As for me, I am poor and needy, but the Lord takes thought for me"* (Psa 40:17).; *"But God will not take away life, and he devises means so that the banished one will not remain an outcast"* (2Sa 14:14). The wise woman says it against the fact that *"We must all die"*.
  - applies to 1 occurrence(s): Jer 29:11 (plans)
- **Observation 19416** (prior-capture, tag statement, status draft): 1.7 It takes in what people do against him, without excusing them: *"this Jesus, delivered up according to the definite plan and foreknowledge of God, you crucified and killed by the hands of lawless men"* (Act 2:23). The plan and the guilt are stated in one sentence.; The church prays Psalm 2, *"Why did the Gentiles rage, and the peoples plot in vain?"* (Act 4:25). They say those gathered against Jesus came *"to do whatever your hand and your plan had predestined to take place"* (4:28).; Their next words are a request for themselves: *"grant to your servants to continue to speak your word with all boldness"* (4:29).; Pointer, from outside the 31: *"you meant evil against me, but God meant i ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Gen 50:20 (meant), Act 2:23 (plan), Act 4:28 (plan)
- **Observation 19417** (prior-capture, tag statement, status draft): 1.8 Before the ages, not from works: *"because of his own purpose and grace, which he gave us in Christ Jesus before the ages began"* (2Ti 1:9).; *"though they were not yet born and had done nothing either good or bad—in order that God's purpose of election might continue, not because of works but because of him who calls"* (Rom 9:11).; *"according to the purpose of him who works all things according to the counsel of his will"* (Eph 1:11).; *"the mystery of his will, according to his purpose, which he set forth in Christ as a plan for the fullness of time, to unite all things in Christ"* (Eph 1:9–10).; *"This was according to the eternal purpose that he has realized in Christ Jesus our Lord ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): Rom 9:11 (purpose), Eph 1:9 (purpose), Eph 1:11 (purpose), Eph 3:11 (purpose), 2Ti 1:9 (purpose)
- **Observation 19418** (prior-capture, tag statement, status draft): 1.9 The Spirit intercedes according to the will of God, and the purpose is turned toward those who love him: *"Likewise the Spirit helps us in our weakness. For we do not know what to pray for as we ought, but the Spirit himself intercedes for us with groanings too deep for words. And he who searches hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God"* (Rom 8:26–27).; The Spirit's praying is matched to God's will, and the one who searches hearts knows the Spirit's mind.; The meaning of "mind" (G5427) is left as Paul gives it: OT-94, which comes back with M63.; The next verse goes straight on: *"And we know that for those who ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Rom 8:28 (purpose)
- **Observation 19419** (prior-capture, tag statement, status draft): 1.10 A person can refuse it, or serve it: *"but the Pharisees and the lawyers rejected the purpose of God for themselves, not having been baptized by him"* (Luk 7:30). Over against them, the people and the tax collectors *"declared God just"* (7:29).; *"For David, after he had served the purpose of God in his own generation, fell asleep"* (Act 13:36).
  - applies to 2 occurrence(s): Luk 7:30 (purpose), Act 13:36 (purpose)
- **Observation 19420** (prior-capture, tag statement, status draft): Turning: in Jer 18:8, 11; 26:3 and 36:3, the plan is spoken so that a person may hear and turn.
  - applies to 1 occurrence(s): Jer 18:11 (plan)
- **Observation 19427** (prior-capture, tag statement, status draft): Fear not: *"so again have I purposed … to bring good … fear not"* (Zec 8:15), with commands that follow (8:16–17), including *"do not devise evil in your hearts against one another"*. The verb is the one used for his own purposing in 8:14–15.
  - applies to 1 occurrence(s): Zec 8:15 (purposed)
- **Observation 19479** (prior-capture, tag statement, status draft): Ground (19): Love: Deu 4:37, Deu 10:15; Psa 47:4, Psa 78:68; Col 3:12, 1Th 1:4, 2Th 2:13 (*"beloved"*); *"Set his love / heart"* (H2836A): Deu 7:7, Deu 10:15; Desire: Psa 132:13, *"he has desired it for his dwelling place"*; Took pleasure: 1Ch 28:4; Compassion: Isa 14:1; Faithful: Isa 49:7; Soul well pleased: Mat 12:18; Knows the hearts: Act 1:24; Purpose: Rom 9:11; Grace: Rom 11:5; Jesus' knowing: Joh 13:18, *"I know whom I have chosen"*
  - applies to 1 occurrence(s): Rom 9:11 (purpose)
- **Observation 19501** (prior-capture, tag statement, status draft): Know and serve with the whole inner being. *"know the God of your father and serve him with a whole heart and with a willing mind, for the Lord searches all hearts and understands every plan and thought"* (1Ch 28:9).
  - applies to 1 occurrence(s): 1Ch 28:9 (plan)
- **Observation 19524** (prior-capture, tag statement, status draft): God acting on others' hearts: God sends *"a strong delusion"* (2Th 2:11), and *"God has put it into their hearts to carry out his purpose"* (Rev 17:17). These are for 13.1.
  - applies to 1 occurrence(s): Rev 17:17 (purpose)
- **Observation 19686** (prior-capture, tag statement, status draft): Proverbs 16:16 — "To get understanding is to be chosen rather than silver": The saying weighs one good against another: *"How much better to get wisdom than gold! To get understanding is to be chosen rather than silver."* "Better" is H2896A, and "to be chosen" is the choosing verb (H0977). To choose here is to prefer: to set one thing above another and take it. What is preferred is inward, wisdom and understanding, and what is passed over is wealth.; The same weighing is made at more length in Proverbs 3: *"the gain from her is better than gain from silver and her profit better than gold. She is more precious than jewels, and nothing you desire can compare with her"* (3:14–15). "Nothing you ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 16:9 (plans)
- **Observation 19714** (prior-capture, tag statement, status draft): Its ground, as the verses state it: "chose us in him before the foundation of the world, that we should be holy and blameless before him" (Eph 1:4); "in order that God's purpose of election might continue, not because of works but because of him who calls" (Rom 9:11; said of the twins "not yet born"); "a remnant, chosen by grace" (Rom 11:5); "brothers loved by God, that he has chosen you" (1Th 1:4); "God chose you as the firstfruits to be saved, through sanctification by the Spirit and belief in the truth" (2Th 2:13, G0138)
  - applies to 1 occurrence(s): Rom 9:11 (purpose)
- **Observation 19997** (prior-capture, tag statement, status draft): Where it is placed. The verses place this in the heart: *"The heart of man plans his way"* (Pro 16:9); *"who plan evil things in their heart"* (Psa 140:2); *"the month that he had devised from his own heart"* (1Ki 12:33); *"the purposes of the heart"* (1Co 4:5); *"every intention of the thoughts of his heart"* (Gen 6:5)
  - applies to 4 occurrence(s): Gen 6:5 (intention), Psa 140:2 (plan), Pro 16:9 (plans), 1Cor 4:5 (purposes)
- **Observation 19999** (prior-capture, tag statement, status draft): What it does not secure. The capacity does not hold the outcome. *"The heart of man plans his way, but the Lord establishes his steps"* (Pro 16:9).
  - applies to 1 occurrence(s): Pro 16:9 (plans)
- **Observation 20002** (prior-capture, tag statement, status draft): 3.1 It happens in the heart, and it is hidden until it acts: *"Whoever winks his eyes plans dishonest things; he who purses his lips brings evil to pass"* (Pro 16:30). The planning shows only in small signs.; *"I did not know it was against me they devised schemes"* (Jer 11:19). Jeremiah did not see the plan aimed at him.; *"they intended to do me harm"* (Neh 6:2). The intent sat behind the friendly invitation, *"Come and let us meet together"*.; *"But he does not so intend, and his heart does not so think; but it is in his heart to destroy"* (Isa 10:7). Of Assyria, what is in the heart differs from the role God gives it. I read this as the intention belonging to the one who holds it, whatev ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Neh 6:2 (intended), Pro 16:30 (plans)
- **Observation 20005** (prior-capture, tag statement, status draft): The sailors of Acts 27 plan under uncertainty. They act *"on the chance that somehow they could reach Phoenix"* (v12) and *"supposing that they had obtained their purpose"* (v13). Later they *"planned if possible to run the ship ashore"* (v39). Their looking ahead is hedged by what they cannot know.
  - applies to 1 occurrence(s): Act 27:13 (purpose)
- **Observation 20006** (prior-capture, tag statement, status draft): Paul and his own planning: *"Do I make my plans according to the flesh, ready to say 'Yes, yes' and 'No, no' at the same time?"* (2Co 1:17). For Paul, a plan carries one's word. A plan that wavers raises the question of where it comes from.
  - applies to 1 occurrence(s): 2Cor 1:17 (plans)
- **Observation 20010** (prior-capture, tag statement, status draft): The forms: plotting (*"as they scheme together against me, as they plot to take my life"*, Psa 31:13); imagining (*"they imagine the worst for me"*, Psa 41:7); using the tongue (*"Your tongue plots destruction"*, Psa 52:2; *"let us strike him with the tongue"*, Jer 18:18); group plans (*"Come, let us cut her off from being a nation!"*, Jer 48:2; *"they made plans to put him to death"*, Joh 11:53); against God himself (*"What do you plot against the Lord?"*, Nah 1:9)
  - applies to 1 occurrence(s): Joh 11:53 (made plans)
- **Observation 20012** (prior-capture, tag statement, status draft): What comes back on the planner: *"you shall do to him as he had meant to do to his brother"* (Deu 19:19); Haman's plan should *"return on his own head"* (Est 9:25); *"Whoever plans to do evil will be called a schemer"* (Pro 24:8)
  - applies to 3 occurrence(s): Deu 19:19 (meant), Est 9:25 (plan), Pro 24:8 (plans)
- **Observation 20014** (prior-capture, tag statement, status draft): 3.6 A purpose held: resolve, aim and the mind set: *"I have purposed that my mouth will not transgress"* (Psa 17:3). The psalmist sets a course ahead for his own speech, under God's testing *"by night"*.; *"exhorted them all to remain faithful to the Lord with steadfast purpose"* (Act 11:23).; *"my teaching, my conduct, my aim in life, my faith"* (2Ti 3:10).
  - applies to 2 occurrence(s): Psa 17:3 (purposed), Act 11:23 (purpose)
- **Observation 20015** (prior-capture, tag statement, status draft): David asks God to keep his people's purposes: *"keep forever such purposes and thoughts in the hearts of your people, and direct their hearts toward you"* (1Ch 29:18).
  - applies to 1 occurrence(s): 1Ch 29:18 (purposes)
- **Observation 20018** (prior-capture, tag statement, status draft): 3.8 The plan and its outcome: *"The heart of man plans his way, but the Lord establishes his steps"* (Pro 16:9).; *"Take counsel together, but it will come to nothing"* (Isa 8:10).; *"if this plan or this undertaking is of man, it will fail"* (Act 5:38). Gamaliel's counsel.; *"I have often intended to come to you (but thus far have been prevented)"* (Rom 1:13).; *"you meant evil against me, but God meant it for good"* (Gen 50:20). The same word, H2803I, is used for both meanings.; *"they will not succeed"* (Psa 21:11), and *"but only for a time"* (Dan 11:24).
  - applies to 4 occurrence(s): Gen 50:20 (meant), Pro 16:9 (plans), Act 5:38 (plan), Rom 1:13 (intended)
- **Observation 20019** (prior-capture, tag statement, status draft): 3.9 God sees the intention: *"the Lord searches all hearts and understands every plan and thought"* (1Ch 28:9).; *"the intention of man's heart is evil from his youth"* (Gen 8:21; also Gen 6:5).; *"he knows our frame; he remembers that we are dust"* (Psa 103:14). H3336 here is "frame", the thing formed.; *"will disclose the purposes of the heart"* (1Co 4:5).
  - applies to 4 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention), 1Ch 28:9 (plan), 1Cor 4:5 (purposes)
- **Observation 20024** (prior-capture, tag statement, status draft): H2803I: God shaping disaster that he may relent from (Jer 18:8, 11); God's plans for welfare (Jer 29:11); people devising evil (Psa 35:4); Saul's plot (1Sa 18:25); a ship "threatened" (Jon 1:4)
  - applies to 1 occurrence(s): Jer 29:11 (plans)
- **Observation 20025** (prior-capture, tag statement, status draft): H2161: God's fixed purpose, *"I have purposed; I have not relented"* (Jer 4:28); the psalmist's resolve (Psa 17:3); the wise woman considering a field (Pro 31:16); the wicked plotting (Psa 37:12)
  - applies to 2 occurrence(s): Psa 17:3 (purposed), Jer 4:28 (purposed)
- **Observation 20027** (prior-capture, tag statement, status draft): H3336: the evil intention of the heart (Gen 6:5); purposes David asks God to keep (1Ch 29:18); the mind stayed on God (Isa 26:3); the human frame (Psa 103:14); the idol-maker's own creation (Hab 2:18)
  - applies to 2 occurrence(s): Gen 6:5 (intention), 1Ch 29:18 (purposes)
- **Observation 20028** (prior-capture, tag statement, status draft): God's intentions in Jeremiah are conditional: *"if that nation … turns from its evil, I will relent of the disaster that I intended"* (Jer 18:8; also 26:3, 36:3). His plan is stated so that people may *"Return, every one from his evil way"* (Jer 18:11). These 31 verses on God's purposing are routed A for 13.1; the 15 that invite or bear on a human response are also B.
  - applies to 2 occurrence(s): Jer 18:8 (intended), Jer 18:11 (plan)
- **Observation 20029** (prior-capture, tag statement, status draft): 10.7 Choosing and setting direction, new section *Planning* | The account of looking ahead. Planning carries a choice ahead (Gen 11:6; Pro 16:9). It covers: weighing first (Luk 14:28–33; Pro 31:15–16; Judg 19:30); planning without knowing (Act 27:10–14, 39–41; Rom 1:13; Jam 4:15); a plan carrying a person's word (2Co 1:17–18); planning together and parting (Act 15:37–39; Luk 23:51–52); planning for another's good (Dan 6:3–4), with the king's planning measured against God's (2Sa 14:13–14); a purpose held (Psa 17:3, 5; Act 11:23; 2Ti 3:10; 1Ch 29:18; Rom 8:6–7; Isa 26:3); devised from one's own heart (1Ki 12:32–33; Neh 6:8); the plan and its outcome (Pro 16:9; Isa 8:10; Act 5:38–39; Psa 21:11; ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): 1Ch 28:9 (plan), Act 5:38 (plan), Act 11:23 (purpose), Act 27:13 (purpose)
- **Observation 20031** (prior-capture, tag statement, status draft): 10.10 Relating to others, new section *Plotting against another* | Planned in the heart (Psa 140:2; Zec 7:10; 8:17). Done together (Psa 31:13; Jer 48:2; Joh 11:53; 12:10–11; Eze 11:2; Dan 11:25, 27; Jer 49:30). Aimed at the quiet and the weak (Psa 10:2; 35:20; 37:12; Eze 38:10–11). Hidden behind something friendly (Neh 6:2–3; 1Sa 18:25). Accusing the other of a plan (Neh 6:6, 8–9). The one plotted against: not knowing (Jer 11:19–20); praying to be guarded (Psa 140:4, 8; 35:4); trusting (Psa 31:14–15); another pleading (Est 8:3; 9:24); another stopping it (Act 27:42–43). Named and checked (Pro 24:8–9; 30:32–33; Deu 19:19–20) | New section
  - applies to 4 occurrence(s): Psa 140:2 (plan), Jer 49:30 (plan), Act 27:42 (plan), Act 27:43 (plan)
- **Observation 20104** (prior-capture, tag statement, status draft): Act 11:23 | A purpose held, the mind set | 10.7 | —
  - applies to 1 occurrence(s): Act 11:23 (purpose)
- **Observation 20116** (prior-capture, tag statement, status draft): G1013 | *boulēma* | plan | plan (Act 27:43), will (Rom 9:19)
  - applies to 1 occurrence(s): Act 27:43 (plan)
- **Observation 20119** (prior-capture, tag statement, status draft): A will set against a plan. *"But the centurion, wishing to save Paul, kept them from carrying out their plan"* (Act 27:43). His wishing (G1014) stopped the soldiers' plan (G1013).
  - applies to 1 occurrence(s): Act 27:43 (plan)
- **Observation 20121** (prior-capture, tag statement, status draft): An intention carried ahead. Herod put Peter in prison, *"intending after the Passover to bring him out to the people"* (Act 12:4).
  - applies to 1 occurrence(s): Act 12:4 (intending)
- **Observation 20122** (prior-capture, tag statement, status draft): A wish that becomes a plan. *"I wanted to come to you first"* (2Co 1:15), and two verses on, *"Do I make my plans according to the flesh"* (1:17). The passage moves from wanting (G1014) to plans (G1011). This is already in 10.7 *Planning*.
  - applies to 1 occurrence(s): 2Cor 1:17 (plans)
- **Observation 20126** (prior-capture, tag statement, status draft): God's will (route A, for 13.1): *"Of his own will he brought us forth"* (Jam 1:18); *"not wishing that any should perish"* (2Pe 3:9); *"when God desired to show more convincingly … the unchangeable character of his purpose"* (Heb 6:17), where will and purpose stand in one sentence; *"who can resist his will?"* (Rom 9:19); the Spirit *"apportions to each one individually as he wills"* (1Co 12:11)
  - applies to 1 occurrence(s): Heb 6:17 (purpose)
- **Observation 20135** (prior-capture, tag statement, status draft): Isaiah 30 joins the refusing will to planning in one passage. It opens: *"Ah, stubborn children," declares the Lord, "who carry out a plan, but not mine"* (Isa 30:1). It goes on to the people *"unwilling to hear the instruction of the Lord"* (30:9) and ends the oracle with *"But you were unwilling"* (30:15). Here refusing God's word goes with carrying out a plan of one's own. This is the closest the Hebrew verses come to your continuum, and it is a single passage, not a pattern.
  - applies to 1 occurrence(s): Isa 30:1 (plan)
- **Observation 20142** (prior-capture, tag statement, status draft): Planning and devising (10.7, 10.4, 10.10) | Shaping ahead, weighing, plotting | G1011 and G1012 are in the same family; Isa 30:1 ties the refusal to a plan "not mine"
  - applies to 1 occurrence(s): Isa 30:1 (plan)
- **Observation 20164** (prior-capture, tag statement, status draft): What the refusal goes with. In these passages the "no" to God is placed beside something the people chose or planned instead: *"But you were unwilling, and you said, 'No! We will flee upon horses'"* (Isa 30:15–16). The refusal is said in their own words, together with their own plan. The chapter opened with *"stubborn children … who carry out a plan, but not mine"* (30:1). They told the prophets, *"Do not prophesy to us what is right; speak to us smooth things"* (30:10).; *"Israel would not submit to me. So I gave them over to their stubborn hearts, to follow their own counsels"* (Psa 81:11–12).; *"Because they hated knowledge and did not choose the fear of the Lord, would have none of my co ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 30:1 (plan)
- **Observation 20180** (prior-capture, tag statement, status draft): Herod. *"when he saw that it pleased the Jews, he proceeded to arrest Peter … intending after the Passover to bring him out to the people. So Peter was kept in prison, but earnest prayer for him was made to God by the church"* (Act 12:3–5). His intention is set beside the church's prayer, and the intention was not carried out (12:6–11).
  - applies to 1 occurrence(s): Act 12:4 (intending)
- **Observation 20181** (prior-capture, tag statement, status draft): Paul. *"I wanted to come to you first … I wanted to visit you on my way to Macedonia"* (2Co 1:15–16). Then *"Do I make my plans according to the flesh"* (1:17).
  - applies to 1 occurrence(s): 2Cor 1:17 (plans)
- **Observation 20182** (prior-capture, tag statement, status draft): The centurion. *"wishing to save Paul, kept them from carrying out their plan"* (Act 27:43).
  - applies to 1 occurrence(s): Act 27:43 (plan)
- **Observation 20190** (prior-capture, tag statement, status draft): Imputing intent: the council to the apostles, *"you intend to bring this man's blood upon us"* (Act 5:28). Peter's answer was *"We must obey God rather than men"* (5:29).
  - applies to 1 occurrence(s): Act 5:28 (intend)
- **Observation 20201** (prior-capture, tag statement, status draft): His will, positively: *"he has mercy on whomever he wills, and he hardens whomever he wills"* (Rom 9:18). *"So then it depends not on human will or exertion, but on God, who has mercy"* (9:16). Then the objection, *"who can resist his will?"* (9:19), and the potter: *"Will what is molded say to its molder, 'Why have you made me like this?'"* (9:20).; *"Of his own will he brought us forth by the word of truth"* (Jam 1:18). Just before: *"desire when it has conceived gives birth to sin"* (1:15), and the Father of lights *"with whom there is no variation"* (1:17).; *"not wishing that any should perish, but that all should reach repentance"* (2Pe 3:9), said against those who *"count slowness"*.; ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Heb 6:17 (purpose)
- **Observation 20207** (prior-capture, tag statement, status draft): 2.2 Passages where Scripture itself puts them together: Pro 1:29–31. Did not choose the fear of the Lord, would have none of my counsel, are filled with their own devices: choosing, willing and devising in one sentence. Earlier in the same chapter, *"if sinners entice you, do not consent. If they say, 'Come with us, let us lie in wait for blood'"* (1:10–11) puts the will's "no" right against a group plot. That is plotting as written in 10.10.; Psa 81:11–12. Would not submit, given over to stubborn hearts, to follow their own counsels.; Isa 30:1, 9, 15–16. A plan *"but not mine"*; unwilling to hear; unwilling, and *"No! We will flee upon horses."* The refusal and the people's own plan are in ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): Isa 30:1 (plan), Act 12:4 (intending), Act 27:42 (plan), Act 27:43 (plan), 2Cor 1:17 (plans)
- **Observation 20208** (prior-capture, tag statement, status draft): Imputing intent. *"you and the Jews intend to rebel"* (Neh 6:6, plan set) and *"you intend to bring this man's blood upon us"* (Act 5:28, will set). In both, an intention is pinned on the other side by those set against them.
  - applies to 2 occurrence(s): Neh 6:6 (intend), Act 5:28 (intend)
- **Observation 20210** (prior-capture, tag statement, status draft): Heb 6:17 is in both sets. God *"desired"* (will) to show the unchangeable character of *"his purpose"* (plan).
  - applies to 1 occurrence(s): Heb 6:17 (purpose)
- **Observation 20211** (prior-capture, tag statement, status draft): The heart and spirit named with the act.; Planning: *"The heart of man plans his way"* (Pro 16:9); *"plan evil things in their heart"* (Psa 140:2).; Willing: the heart or spirit hardened, stubborn or lifted up (Exo 10:27; Deu 2:30; Eze 3:7; Psa 81:12; Deu 29:19; Dan 5:20); the willing heart and spirit (Exo 35:21–22; 2Ch 29:31; Psa 51:12).; So the will verses name the state of the heart and spirit more often than the plan verses do. Chapters 4 (the heart) and 6 (the spirit) should take this.
  - applies to 2 occurrence(s): Psa 140:2 (plan), Pro 16:9 (plans)
- **Observation 20216** (prior-capture, tag statement, status draft): Knowing is not enough. Belshazzar *"knew all this"* and did not humble his heart (Dan 5:22). In the plan set, God *"understands every plan"* (1Ch 28:9). The will set adds that the person's own knowing does not move the will.
  - applies to 1 occurrence(s): 1Ch 28:9 (plan)
- **Observation 20217** (prior-capture, tag statement, status draft): The outcome is not held. Plans fail or are overruled (Pro 16:9; Isa 8:10; Act 5:38). Wills are overruled as well: Herod's intention (Act 12), the Romans' wish to free Paul (Act 28:18–19), Paul's wish to enter the theater (Act 19:30). And human will is set under God's: *"it depends not on human will or exertion"* (Rom 9:16); *"not my will, but yours"* (Luk 22:42).
  - applies to 1 occurrence(s): Pro 16:9 (plans)
- **Observation 20223** (prior-capture, tag statement, status draft): Already in the narrative for another reason (#1987): Deu 1:26; 2:30; 1Sa 31:4; Psa 51:12; Pro 6:35; Dan 5:19; Act 25:20; 1Ti 2:8; Act 27:43 (as a plan verse in 10.10). Each is now read for its will word above.
  - applies to 1 occurrence(s): Act 27:43 (plan)
- **Observation 20241** (prior-capture, tag statement, status draft): God giving over the perishing (2Th 2:11, *"a strong delusion"*), and God putting a purpose into the kings' hearts (Rev 17:17). These are God acting on the hearts of others. They are for 13.1, not §2b.
  - applies to 1 occurrence(s): Rev 17:17 (purpose)
- **Observation 20325** (prior-capture, tag statement, status draft): Gen 6:5: Ch 11 §1 "Even the leaning is formed" rests on the word, not the verse; Ch 11 §8 says the intention "grieved him", which 6:6 does not say.
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 20327** (prior-capture, tag statement, status draft): 1Ch 29:18: Ch 14 quotes "such purposes" without saying what they are (the free, willing giving).
  - applies to 1 occurrence(s): 1Ch 29:18 (purposes)
- **Observation 20375** (prior-capture, tag statement, status draft): Genesis 6:5 and 8:21: "every intention of the thoughts of his heart": > Q1 citation: ⚠ Check. Gen 6:5 is accurate in 10.0, 10.4 and Ch 12. Two places to check in Ch 11: (1) §1 *Even the leaning is formed* rests on the word *yēṣer* (also "what a potter forms", "our frame"), not on what Gen 6:5 says. Under a pattern of God acting on the inner being it can read as if God formed the evil intention. It needs "I read" or a restatement. (2) §8 says "the same evil intention had grieved him 'to his heart' (6:5–6)". Gen 6:6 says the Lord regretted making man, "and it grieved him to his heart". It does not name the intention as what grieved him. Gen 8:21: ✅ accurate in Ch 4, Ch 11 §8 and Ch 12.; >; > Q ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 20385** (prior-capture, tag statement, status draft): 1 Chronicles 28:9: "understands every plan and thought": > Q1 citation: ✅ Accurate. Accurate in 10.4, 10.9, 10.7 *Being chosen is not a guarantee* (the condition) and 13.1 *He searches hearts*.; >; > Q2 M64: Include: corroborates and adds (#1986). Corroborates 10.4, 10.9, 10.7 and 13.1. New for #1986: "with a willing mind" (H2655, tagged M18).; >; > Q3 other M-codes: M18 willing (H2655): yes, for #1986 and 10.6. M83 seek ("If you seek him"): yes, when seeking is taken up. M12 whole heart and M36 serve: corroborate 10.9's "with all your heart"; no. M30 forsake: carried in 10.7.; David charges Solomon: *"know the God of your father and serve him with a whole heart and with a willing mind, for ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 20414** (prior-capture, tag statement, status draft): 1Ch 28:9 | God knows every plan (10.4, 10.9) | yes | "willing mind", H2655, M18 (#1986 note)
  - applies to 1 occurrence(s): 1Ch 28:9 (plan)
- **Observation 20415** (prior-capture, tag statement, status draft): 1Ch 29:18 | the leaning kept (Ch 14) | yes | "such purposes" = the free, joyful giving; H5068, M18 (#1986 note)
  - applies to 1 occurrence(s): 1Ch 29:18 (purposes)
- **Observation 20420** (prior-capture, tag statement, status draft): Pro 16:9 | the heart plans (Ch 4, 10.4) | yes | v3, plans committed are established
  - applies to 1 occurrence(s): Pro 16:9 (plans)
- **Observation 20436** (prior-capture, tag statement, status draft): Ledger OT-H2. I held the discussion's §11 ("thought as a system", six directions of flow) as "superseded by 10.0". Two of its flows reached the narrative only in part, and two not at all: Flow 3 — thoughts acting on the self: "my thoughts answer me, because of my haste within me" (Job 20:2); "my thoughts greatly alarmed me" (Dan 7:28). Not woven.; Flow 5 — consequences returning to the one who devised: Haman's "evil plan … should return on his own head" (Est 9:25); "the fruit of their devices" (Jer 6:19, quoted in 10.2 but not for this point); "let them be caught in the schemes that they have devised" (Ps 10:2); "the plans of the diligent lead surely to abundance" (Pro 21:5). Not woven.
  - applies to 2 occurrence(s): Est 9:25 (plan), Pro 21:5 (plans)
- **Observation 20440** (prior-capture, tag face, status draft): Face: God's purpose; Verses: Jer 23:20; 30:24; 51:11; Job 42:2; Who thinks: God; Joined with / aimed at: "the intents of his heart"; cannot be thwarted
  - applies to 3 occurrence(s): Job 42:2 (purpose), Jer 23:20 (intents), Jer 51:11 (purpose)
- **Observation 20443** (prior-capture, tag face, status draft): Face: God's plans; Verses: Jer 29:11; Ps 33:11; 40:5; 92:5; Isa 55:8–9; Mic 4:12; 2Sa 14:14 ("devises means")
  - applies to 2 occurrence(s): Psa 33:11 (plans), Jer 29:11 (plans)
- **Observation 20444** (prior-capture, tag face, status draft): Face: Ordinary plans, in need of counsel or commitment; Verses: Pro 15:22; 16:3; 20:18; 21:5
  - applies to 4 occurrence(s): Pro 15:22 (plans), Pro 16:3 (plans), Pro 20:18 (plans), Pro 21:5 (plans)
- **Observation 20446** (prior-capture, tag statement, status draft): Wisdom literature gives plans a fourth character: unfinished. They fail without counsel (Pro 15:22), are established by counsel (20:18) and by committing the work to the Lord (16:3), and reward diligence against haste (21:5). Thinking is completed with others and before God, not alone.
  - applies to 4 occurrence(s): Pro 15:22 (plans), Pro 16:3 (plans), Pro 20:18 (plans), Pro 21:5 (plans)
- **Observation 20449** (prior-capture, tag statement, status draft): The Hebrew Bible: The source is the *lēv* (heart), not the brain. Examples are Proverbs 4:23 ("from it flow the springs of life") and Genesis 6:5 ("every intention of the thoughts of his heart").
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 20453** (prior-capture, tag statement, status draft): 1. From within: the heart is where they come from.: Mark 7:21 and Matthew 15:19 say it directly: "from within, out of the heart … come evil thoughts."; Genesis 6:5 speaks of "the intention of the thoughts of his heart," and Luke 1:51 of "the thoughts of their hearts."; Also Hebrews 4:12, Luke 2:35, 1 Chronicles 29:18, Matthew 9:4 and Luke 5:22.; In these verses thoughts are never located in the head. They come out of the heart, the centre of the person.
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 20456** (prior-capture, tag statement, status draft): 4.2 What thoughts are: Inner speech. 21 of the rows (H0559, *ʾāmar*, "to say") are places where the Hebrew says "he *said*" and the ESV renders it "he thought," as in 1 Samuel 18:11: "Saul thought, 'I will pin David…'" The Greek *dialogismos* (G1261) and *logismos* (G3053) are also built on *logos*, "word" [lexical]. In these texts, to think is to speak inwardly. *Caveat:* how many rows show this depends on the ESV's choices.; Devising or planning. H4284 *maḥăšāvāh* (from H2803 *ḥāšav*, "to devise"). These thoughts are designs with a direction. They can be just (Proverbs 12:5), evil (Isaiah 59:7), or God's own plan (Micah 4:12). Because they point somewhere, they can be judged, and they can ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Mic 4:12 (plan)
- **Observation 20458** (prior-capture, tag statement, status draft): H4284 is rendered "plans" in Jeremiah 29:11 and Proverbs 16:3, and "plans of his heart" in Psalm 33:11.
  - applies to 3 occurrence(s): Psa 33:11 (plans), Pro 16:3 (plans), Jer 29:11 (plans)
- **Observation 20459** (prior-capture, tag statement, status draft): H2803 is rendered "meant" in Genesis 50:20 and "plans" in Proverbs 16:9.
  - applies to 2 occurrence(s): Gen 50:20 (meant), Pro 16:9 (plans)
- **Observation 20462** (prior-capture, tag statement, status draft): intention / intent | H3336 *yēṣer* | Gen 8:21 | *yēṣer* is also in Gen 6:5; central to origins
  - applies to 2 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention)
- **Observation 20470** (prior-capture, tag statement, status draft): Evil schemes: Esther 9:25 (Haman's "evil plan"), Jeremiah 18:18, Proverbs 6:18.
  - applies to 1 occurrence(s): Est 9:25 (plan)
- **Observation 20471** (prior-capture, tag statement, status draft): God: Jeremiah 29:11, Psalm 33:11 ("the plans of his heart"), 2 Samuel 14:14 ("he devises means").
  - applies to 2 occurrence(s): Psa 33:11 (plans), Jer 29:11 (plans)
- **Observation 20478** (prior-capture, tag statement, status draft): 5. Plans are refined through counsel. Proverbs 15:22 ("Without counsel plans fail") and Proverbs 20:18. Proverbs 21:5 contrasts the plans of the diligent with haste, which echoes Job 20:2. Thinking is formed together with others and over time, not only alone.
  - applies to 3 occurrence(s): Pro 15:22 (plans), Pro 20:18 (plans), Pro 21:5 (plans)
- **Observation 20481** (prior-capture, tag statement, status draft): 1. The heart or mind is the place thoughts come from. Mark 7:21 and Matt 15:19 ("out of the heart come evil thoughts"). Also: "a heart that devises wicked plans" (Prov 6:18); "plan evil things in their heart" (Ps 140:2); "devise evil … in your heart" (Zech 7:10; 8:17); "The heart of man plans his way" (Prov 16:9); "his heart does not so think; but it is in his heart to destroy" (Isa 10:7); "the reasoning of their hearts" (Luke 9:47); In Jer 4:14, thoughts *lodge* within: "How long shall your wicked thoughts lodge within you?" This follows the call to "wash your heart."
  - applies to 3 occurrence(s): Psa 140:2 (plan), Pro 6:18 (plans), Pro 16:9 (plans)
- **Observation 20486** (prior-capture, tag statement, status draft): By counsel: "Plans are established by counsel" (Prov 20:18; 15:22).
  - applies to 2 occurrence(s): Pro 15:22 (plans), Pro 20:18 (plans)
- **Observation 20488** (prior-capture, tag statement, status draft): 5. God is a thinker too, and his thinking has the last word. The same vocabulary is used of God: *maḥăšāvāh*: Jer 29:11; Ps 33:11; 40:5; 92:5; Isa 55:8–9; *ḥāšav*: Jer 18:11; 2 Sam 14:14; Lam 2:8; "the Lord takes thought for me" (Ps 40:17); "that you think of him" (Ps 144:3); *mᵊzimmāh*: "the intents of his heart" (Jer 23:20); "no purpose of yours can be thwarted" (Job 42:2); In Gen 50:20 there are two opposite intentions about one event, expressed with the same verb: "you meant evil … God meant it for good." Human plans are real, but "it is the purpose of the Lord that will stand" (Prov 19:21; also Prov 16:9; Ps 33:10–11; Job 5:12).
  - applies to 8 occurrence(s): Gen 50:20 (meant), Job 42:2 (purpose), Psa 33:10 (plans), Psa 33:11 (plans), Pro 16:9 (plans), Pro 19:21 (plans), Pro 19:21 (purpose), Jer 23:20 (intents)
- **Observation 20489** (prior-capture, tag statement, status draft): 9.2 What thoughts are: Design: forming something that does not yet exist. H2803G (19 rows) describes craftsmanship: cherubim "skillfully worked" (Exod 26:1, 31) and "skilled design" (Exod 39:3). The faculty itself is neutral. *Maḥăšāvāh* covers both artistry and plots, and *mᵊzimmāh* covers both "discretion" (Prov 2:11) and "evil devices" (Prov 12:2). What makes a thought good or evil is what it is designed toward.; Reckoning: giving something its value or category. H2803H/J (60 rows): Human misreckoning: Eli "took her to be a drunken woman" (1 Sam 1:13), "we esteemed him stricken" and "we esteemed him not" (Isa 53:3–4), Judah "thought she was a prostitute" (Gen 38:15).; God's reckoning: "he ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 20490** (prior-capture, tag statement, status draft): 9.3 From thought to action (Claude's reading): The verses trace a path from thought to deed: Arising. Thoughts come, often in the night (Dan 2:29; Job 4:13; Ezek 38:10; Luke 24:38).; Lodging. They stay and are dwelt on (Jer 4:14).; Reckoning. They weigh up and value things (Isa 53:4; 1 Sam 1:13).; Devising. They take the form of a plan (Ezek 38:10b; Ps 36:4).; Expression. Tongue, lips and eyes: "your tongue plots" (Ps 52:2), "devise words of deceit" (Ps 35:20), "winks his eyes plans" (Prov 16:30), "whisper … imagine the worst" (Ps 41:7).; Action. Hand and feet: "when the morning dawns, they perform it" (Mic 2:1); "a heart that devises … feet that make haste" (Prov 6:18); "their feet run to e ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 16:30 (plans)
- **Observation 20492** (prior-capture, tag statement, status draft): Some English words are artifacts of how the data links each word to the English. "Have" (Jer 29:11, "the plans I have"), "make", "itself", "took her", "amid" (Job 4:13), "seem", "execute", "threatened" and "evil" are only part of the full rendering. Read them in context.
  - applies to 1 occurrence(s): Jer 29:11 (plans)
- **Observation 20493** (prior-capture, tag statement, status draft): 1. Outward: heart → speech → body → action.: "a heart that devises wicked plans, feet that make haste" (Prov 6:18); "your tongue plots" (Ps 52:2); "winks his eyes plans" (Prov 16:30); "when the morning dawns, they perform it, because it is in the power of their hand" (Mic 2:1)
  - applies to 2 occurrence(s): Pro 6:18 (plans), Pro 16:30 (plans)
- **Observation 20494** (prior-capture, tag statement, status draft): 2. Inward: outside influences → heart and mind.: God writes on minds and hearts (Heb 8:10; 10:16) and fills people with skill (Exod 35:35).; Instruction gives discretion (Prov 1:4).; Counsel establishes plans (Prov 15:22; 20:18).; The serpent leads thoughts astray (2 Cor 11:3), and "the god of this world" blinds (2 Cor 4:4).
  - applies to 2 occurrence(s): Pro 15:22 (plans), Pro 20:18 (plans)
- **Observation 20497** (prior-capture, tag statement, status draft): 5. Back again: consequences returning to the one who devised.: "his evil plan … should return on his own head" (Esth 9:25); "the fruit of their devices" (Jer 6:19); "let them be caught in the schemes that they have devised" (Ps 10:2); "The plans of the diligent lead surely to abundance" (Prov 21:5)
  - applies to 2 occurrence(s): Est 9:25 (plan), Pro 21:5 (plans)
- **Observation 20498** (prior-capture, tag statement, status draft): 6. Vertical: between God's thinking and human thinking.: God searches, knows and discerns thoughts (Ps 139:2, 23; 1 Chr 28:9; Heb 4:12).; God reckons (Gen 15:6; Ps 32:2).; God overrules: "you meant evil … God meant it for good" (Gen 50:20); "it is the purpose of the Lord that will stand" (Prov 19:21).; Human thought can also turn back toward God: "When I think on my ways, I turn my feet to your testimonies" (Ps 119:59).
  - applies to 2 occurrence(s): Gen 50:20 (meant), Pro 19:21 (purpose)
- **Observation 20499** (prior-capture, tag statement, status draft): 2 | Intention and formation | Gen 6:5 already pairs *yēṣer* with *maḥăšāvāh* | H3336 *yēṣer*
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 20508** (prior-capture, tag statement, status draft): The heart plans, but the Lord's purpose stands: Pro 16:9; 19:21 (§9.1.5): Ch 3 "The heart thinks, attends and remembers"
  - applies to 3 occurrence(s): Pro 16:9 (plans), Pro 19:21 (plans), Pro 19:21 (purpose)
- **Observation 20512** (prior-capture, tag statement, status draft): Thought is creaturely: "his breath departs … his plans perish", Ps 146:4 (§9.2.5): Ch 9 "Life, breath and death" (not yet using this verse)
  - applies to 1 occurrence(s): Psa 146:4 (plans)
- **Observation 20515** (prior-capture, tag statement, status draft): 5. Checks needed before any of it enters a chapter: Under the narrative rules ("each unfounded claim must be checked and restated", quotes checked against the ESV): Quotations: the discussion quotes the ESV "as supplied in the datasets". Each verse must be checked against iba.db verse before use, as was done for chapters 01–14 (#1915).; Items marked [verify]: the discussion's own uncertain claims, including the Hebrew notes that §9.4 says the English obscures.; Claude's readings: §4.3, §9.3 and §11 are labelled as Claude's reading. They stay inferential and would enter as "I read this as…", not as findings.; Open threads (§14): these words have not been pulled yet: *yēṣer* H3336 (Gen 6:5; 8: ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention)
- **Observation 20535** (prior-capture, tag face, status draft): Face: God devising against, conditionally; Verses: Jer 18:8, 11; 26:3; 36:3; Mic 2:3; Jer 49:20, 30; 50:45; Lam 2:8; What differs: God devises "against", but: "Return, every one from his evil way" (18:11); "It may be they will listen … that I may relent of the disaster that I intend" (26:3); Why (basis): God's "against" is aimed at turning, and it is open to change. "Against" alone does not make thinking evil (S)
  - applies to 2 occurrence(s): Jer 26:3 (intend), Jer 36:3 (intend)
- **Observation 20536** (prior-capture, tag face, status draft): Face: God devising for; Verses: Jer 29:11; 2Sa 14:14; Gen 50:20b; What differs: "plans for welfare and not for evil" (Jer 29:11); "he devises means so that the banished one will not remain an outcast" (2Sa 14:14); Why (basis): For whom God thinks: the exile, the banished (S)
  - applies to 1 occurrence(s): Jer 29:11 (plans)
- **Observation 20544** (prior-capture, tag statement, status draft): God's purpose is carried by his anger: "The anger of the Lord will not turn back until he has executed and accomplished the intents of his heart. In the latter days you will understand it clearly" (Jer 23:20; 30:24). The word for discretion and for evil device is here God's *intent*, and his anger serves it. Understanding comes only afterwards. This is a link to the anger strand.
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 20568** (prior-capture, tag statement, status draft): *enthymēsis / dianoēma* | Thoughts known by Jesus · thoughts and intentions discerned by the word · imagination that makes images of God | Mat 9:4; 12:25; Luk 11:17 · Heb 4:12 · Act 17:29 | "an image formed by the art and imagination of man" (Act 17:29). Imagination is the faculty of design (*ḥāšav* G) turned to making gods. This is the Greek counterpart of Hab 2:18 and the false likening of *dāmāh* (S/R)
  - applies to 1 occurrence(s): Heb 4:12 (intentions)
- **Observation 20578** (prior-capture, tag statement, status draft): *mᵊzimmāh* | 10.3; 11 §4 | Third face: God's intents, carried by his anger (Jer 23:20)
  - applies to 1 occurrence(s): Jer 23:20 (intents)
- **Observation 12407** (strand-reading, tag key-statement, status resolved): The heart is where thoughts come from
  - meaning: The heart is where thoughts come from
  - applies to 4 occurrence(s): Psa 140:2 (plan), Pro 6:18 (plans), Pro 16:9 (plans), Isa 10:7 (intend)
- **Observation 12411** (strand-reading, tag key-statement, status resolved): What rises is shaped from outside: God writes on minds; he gives skill to devise; instruction and counsel form thought; minds can be blinded
  - meaning: What rises is shaped from outside: God writes on minds; he gives skill to devise; instruction and counsel form thought; minds can be blinded
  - applies to 2 occurrence(s): Pro 15:22 (plans), Pro 20:18 (plans)
- **Observation 12412** (strand-reading, tag key-statement, status resolved): yēṣer ("intention", "inclination") is the same word as the potter's thing formed, and as our frame.
  - meaning: yēṣer ("intention", "inclination") is the same word as the potter's thing formed, and as our frame. The inclination of the heart is itself something formed
  - applies to 3 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention), 1Ch 28:9 (plan)
- **Observation 12413** (strand-reading, tag key-statement, status resolved): God knows the inclination before it acts ("what they are inclined to do even today")
  - meaning: God knows the inclination before it acts ("what they are inclined to do even today")
  - applies to 1 occurrence(s): 1Ch 28:9 (plan)
- **Observation 12416** (strand-reading, tag key-statement, status resolved): Thought as likening, i.e.
  - meaning: Thought as likening, i.e. comparing (dāmāh: think / plan / be like)
  - applies to 1 occurrence(s): Isa 10:7 (intend)
- **Observation 12423** (strand-reading, tag key-statement, status resolved): God also speaks in his heart.
  - meaning: God also speaks in his heart. Faced with man's evil inclination, he says "I will never again curse the ground" (Gen 8:21). The same fact that grounded judgement in 6:5–7 grounds forbearance in 8:21
  - applies to 2 occurrence(s): Gen 6:5 (intention), Gen 8:21 (intention)
- **Observation 12424** (strand-reading, tag key-statement, status resolved): The path: arising → lodging → reckoning → devising → expression (tongue, lips, eyes) → action (hand, feet)
  - meaning: The path: arising → lodging → reckoning → devising → expression (tongue, lips, eyes) → action (hand, feet)
  - applies to 2 occurrence(s): Pro 6:18 (plans), Pro 16:30 (plans)
- **Observation 12428** (strand-reading, tag key-statement, status resolved): Responsibility sits from lodging onward.
  - meaning: Responsibility sits from lodging onward. The commands address lodging, devising and saying, not arising; what arises shows the heart
  - applies to 1 occurrence(s): Gen 6:5 (intention)
- **Observation 12430** (strand-reading, tag key-statement, status resolved): God thinks and plans, and his purpose stands over human plans
  - meaning: God thinks and plans, and his purpose stands over human plans
  - applies to 6 occurrence(s): Gen 50:20 (meant), Job 42:2 (purpose), Psa 33:10 (plans), Psa 33:11 (plans), Pro 19:21 (plans), Jer 29:11 (plans)
- **Observation 12431** (strand-reading, tag key-statement, status resolved): Thoughts are fully open to God and to Jesus.
  - meaning: Thoughts are fully open to God and to Jesus. Jesus perceives inner questioning "in his spirit"
  - applies to 1 occurrence(s): 1Ch 28:9 (plan)
- **Observation 12434** (strand-reading, tag key-statement, status resolved): The inclination can be kept, directed and stayed.
  - meaning: The inclination can be kept, directed and stayed. David prays God to "keep … such purposes and thoughts … and direct their hearts"; "perfect peace whose mind is stayed on you"
  - applies to 1 occurrence(s): 1Ch 29:18 (purposes)
- **Observation 12442** (strand-reading, tag key-statement, status resolved): God's devising "against" is conditional, aimed at turning
  - meaning: God's devising "against" is conditional, aimed at turning
  - applies to 4 occurrence(s): Jer 18:8 (intended), Jer 18:11 (plan), Jer 26:3 (intend), Jer 36:3 (intend)
- **Observation 12450** (strand-reading, tag key-statement, status resolved): A cold calculation taken up into God's purpose
  - meaning: A cold calculation taken up into God's purpose
  - applies to 1 occurrence(s): Gen 50:20 (meant)
- **Observation 12452** (strand-reading, tag key-statement, status resolved): Flow 5: what is devised comes back.
  - meaning: Flow 5: what is devised comes back. The plan returns on the deviser's head (Est 9:25); the schemer is caught in his own scheme (Psa 10:2); disaster is "the fruit of their devices" (Jer 6:19). God answers "devise wickedness" with "I am devising disaster" (Mic 2:1, 3). It also comes back for good: "The plans of the diligent lead surely to abundance" (Pro 21:5); "Commit your work to the Lord, and your plans will be established" (16:3)
  - applies to 3 occurrence(s): Est 9:25 (plan), Pro 16:3 (plans), Pro 21:5 (plans)
- **Observation 12508** (strand-reading, tag key-statement, status resolved): A thing can be devised from one's own heart: Jeroboam's feast "in the month that he had devised from his own heart" (1Ki 12:33); "you are inventing them out of your own mind" (Neh 6:8). The purposes are hidden until the Lord comes, "who will bring to light the things now hidden in darkness and will disclose the purposes of the heart" (1Co 4:5).
  - meaning: What the heart devises on its own can be a rival worship or a false report, and its purposes are hidden until God discloses them.
  - implication: The heart's purposes are judged at their disclosure, not before (1Co 4:5).
  - applies to 1 occurrence(s): 1Cor 4:5 (purposes)
- **Observation 12509** (strand-reading, tag key-statement, status resolved): A purpose can be held ahead: "I have purposed that my mouth will not transgress" (Psa 17:3), after "You have tried my heart, you have visited me by night"; "to remain faithful to the Lord with steadfast purpose" (Act 11:23); "my teaching, my conduct, my aim in life, my faith" (2Ti 3:10). The mind can be set: "the mind that is set on the flesh is hostile to God" (Rom 8:7).
  - meaning: A person can set a course ahead for his own speech and faithfulness and hold it; the mind's setting decides its direction toward God.
  - implication: The purpose held is set under God's testing of the heart (Psa 17:3).
  - applies to 1 occurrence(s): Psa 17:3 (purposed)
- **Observation 12510** (strand-reading, tag key-statement, status resolved): The plan to harm is named and checked: "Whoever plans to do evil will be called a schemer" (Pro 24:8); "if you have been devising evil, put your hand on your mouth" (Pro 30:32); of the false witness, "you shall do to him as he had meant to do to his brother" (Deu 19:19).
  - meaning: The schemer is named by his plan, told to stop it at the mouth, and in the law receives what he meant for his brother.
  - implication: What is devised comes back on the one who devised it.
  - applies to 2 occurrence(s): Deu 19:19 (meant), Pro 24:8 (plans)
- **Observation 12511** (strand-reading, tag key-statement, status resolved): God also purposes and does not turn back: "I have spoken; I have purposed; I have not relented, nor will I turn back" (Jer 4:28); "so again have I purposed in these days to bring good to Jerusalem and to the house of Judah; fear not" (Zec 8:15); "the unchangeable character of his purpose, he guaranteed it with an oath" (Heb 6:17).
  - meaning: Beside the purposes he relents of, God states fixed purposes, for judgement and for good; no verse here explains how the two stand together.
  - implication: The fixed purpose is given as encouragement, "a sure and steadfast anchor of the soul" (Heb 6:19).
  - applies to 3 occurrence(s): Jer 4:28 (purposed), Zec 8:15 (purposed), Heb 6:17 (purpose)
- **Observation 12512** (strand-reading, tag key-statement, status resolved): God forms a plan and makes it known: "hear the plan that the Lord has made against Edom and the purposes that he has formed against the inhabitants of Teman" (Jer 49:20; 50:45); "the Lord has both planned and done what he spoke concerning the inhabitants of Babylon" (Jer 51:12); "the whole counsel of God" (Act 20:27). It is carried out and seen: "The Lord has done what he purposed; he has carried out his word" (Lam 2:17); "The Lord determined to lay in ruins the wall of the daughter of Zion" (Lam 2:8); and the fathers "repented and said, As the Lord of hosts purposed to deal with us for our ways and deeds, so has he dealt with us" (Zec 1:6).
  - meaning: God's plan is announced, carried out, and recognised afterward by those it came upon, who repent.
  - implication: The fulfilled purpose is met with the heart poured out (Lam 2:18-19) and with repentance (Zec 1:6).
  - applies to 2 occurrence(s): Lam 2:17 (purposed), Zec 1:6 (purposed)
- **Observation 12514** (strand-reading, tag key-statement, status resolved): The looking-ahead words are used most often against another person. It is placed in the heart: "let none of you devise evil against another in your heart" (Zec 7:10), "do not devise evil in your hearts against one another" (Zec 8:17). It is done together: "Come, let us make plots against Jeremiah" (Jer 18:18); "In Heshbon they planned disaster against her" (Jer 48:2); "they made plans to put him to death" (Joh 11:53), and Lazarus as well (Joh 12:10); "The soldiers’ plan was to kill the prisoners" (Act 27:42). It is aimed at the righteous and the weak: "The wicked plots against the righteous and gnashes his teeth at him" (Psa 37:12); "who have planned to trip up my feet" (Psa 140:4). It hides ... (cut; the whole text is in the workbook)
  - meaning: Looking ahead in these verses is mostly turned against another: devised in the heart, done together, aimed at the righteous and the weak, covered by a friendly word, and met by the plea of another.
  - implication: The plotter's power and the outcome are not the same: "though they devise mischief, they will not succeed" (Psa 21:11); "do not further their evil plot" (Psa 140:8).
  - applies to 5 occurrence(s): Neh 6:2 (intended), Neh 6:6 (intend), Joh 11:53 (made plans), Joh 12:10 (made plans), Act 27:42 (plan)
- **Observation 12515** (strand-reading, tag key-statement, status resolved): The will resolves, intends and steers: Joseph, "unwilling to put her to shame, resolved to divorce her quietly" (Mat 1:19), until the angel spoke as he considered; Herod "intending after the Passover to bring him out to the people" (Act 12:4), and the intention was not carried out; "I wanted to come to you first" (2Co 1:15); "the centurion, wishing to save Paul, kept them from carrying out their plan" (Act 27:43); "guided by a very small rudder wherever the will of the pilot directs" (Jam 3:4).
  - meaning: A resolve can still be weighed and redirected, an intention can be stopped, and one will can stand against a group's plan; the will sets the course of the whole.
  - implication: Herod's intention is set beside the church's prayer (Act 12:5).
  - applies to 1 occurrence(s): Act 12:4 (intending)
- **Observation 12518** (strand-reading, tag key-statement, status resolved): Looking ahead weighs before it acts: a king "will not sit down first and deliberate whether he is able with ten thousand to meet him who comes against him with twenty thousand" (Luk 14:31); "She considers a field and buys it" (Pro 31:16); "consider it, take counsel, and speak" (Judg 19:30). It plans without knowing: "on the chance that somehow they could reach Phoenix" (Act 27:12), "supposing that they had obtained their purpose" (Act 27:13), "they planned if possible to run the ship ashore" (Act 27:39). A plan carries a word: "Do I make my plans according to the flesh, ready to say Yes, yes and No, no at the same time?" (2Co 1:17). Plans part people: "Barnabas wanted to take with them John ... (cut; the whole text is in the workbook)
  - meaning: The capacity to look ahead weighs ability and cost first, plans under uncertainty, binds one's word, can part companions or set one apart from a council, and can plan another's good.
  - implication: The plan in Dan 6:3 rests on what the king saw in Daniel's spirit.
  - applies to 1 occurrence(s): Act 27:13 (purpose)
- **Observation 12519** (strand-reading, tag key-statement, status resolved): God's plan takes in what people do against him without excusing them: "this Jesus, delivered up according to the definite plan and foreknowledge of God, you crucified and killed by the hands of lawless men" (Act 2:23); "to do whatever your hand and your plan had predestined to take place" (Act 4:28).
  - meaning: The plan and the guilt are stated in one sentence.
  - implication: The church's next words ask boldness for itself (Act 4:29).
  - applies to 2 occurrence(s): Act 2:23 (plan), Act 4:28 (plan)
- **Observation 12520** (strand-reading, tag key-statement, status resolved): The capacity is real, and it does not hold the outcome: "nothing that they propose to do will now be impossible for them" (Gen 11:6); "Take counsel together, but it will come to nothing; speak a word, but it will not stand, for God is with us" (Isa 8:10); "if this plan or this undertaking is of man, it will fail" (Act 5:38); "I have often intended to come to you (but thus far have been prevented)" (Rom 1:13).
  - meaning: A human plan is real in its reach, and its outcome rests with God.
  - implication: Pro 16:9 gives the pair in one verse: the heart plans, the Lord establishes the steps.
  - applies to 2 occurrence(s): Act 5:38 (plan), Rom 1:13 (intended)
- **Observation 12522** (strand-reading, tag key-statement, status resolved): "he who searches hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God" (Rom 8:27); "for those who love God all things work together for good, for those who are called according to his purpose" (Rom 8:28). And a person can refuse it: "the Pharisees and the lawyers rejected the purpose of God for themselves" (Luk 7:30).
  - meaning: The Spirit's praying is matched to God's will, the purpose is turned toward those who love him, and it can be rejected for oneself.
  - implication: Rejecting the purpose is said to be "for themselves" (Luk 7:30).
  - applies to 2 occurrence(s): Luk 7:30 (purpose), Rom 8:28 (purpose)
- **Observation 12523** (strand-reading, tag key-statement, status resolved): The will turned toward harm: "those who desire to be rich fall into temptation, into a snare, into many senseless and harmful desires" (1Ti 6:9); "whoever wishes to be a friend of the world makes himself an enemy of God" (Jam 4:4). An intention is imputed: "you intend to bring this man's blood upon us" (Act 5:28).
  - meaning: Wanting set on riches or the world leads into a snare and into enmity with God; an intention can be pinned on another by those set against them.
  - implication: The wish itself makes a person an enemy of God (Jam 4:4).
  - applies to 1 occurrence(s): Act 5:28 (intend)
- **Observation 12524** (strand-reading, tag key-statement, status resolved): His purpose is before the ages and not from works: "because of his own purpose and grace, which he gave us in Christ Jesus before the ages began" (2Ti 1:9); "in order that God's purpose of election might continue, not because of works but because of him who calls" (Rom 9:11); "according to the purpose of him who works all things according to the counsel of his will" (Eph 1:11); "the mystery of his will, according to his purpose, which he set forth in Christ" (Eph 1:9); "the eternal purpose that he has realized in Christ Jesus our Lord" (Eph 3:11); "whom God put forward as a propitiation by his blood" (Rom 3:25).
  - meaning: God's purpose precedes the person and works, and is set forth in Christ.
  - implication: The purpose is grace, given before the ages (2Ti 1:9).
  - applies to 4 occurrence(s): Rom 9:11 (purpose), Eph 1:11 (purpose), Eph 3:11 (purpose), 2Ti 1:9 (purpose)

### 4.3 The retired catalogue observations (0, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

_no rows_

### 4.4 Withdrawn observations (4)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 4 |

| reason as stored | observations |
|---|---|
| no change record | 4 |

## 5. Claims and the narrative

28 claims rest on these occurrences: 22 on an observation of these words and 6 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (22)

- **C-356** (narrative, verdict New, status current, in narrative 1): The power to look ahead is turned most often against another person: planned in the heart, done together, aimed at the righteous and the weak, hidden behind a friendly word, pinned on the other side, and met by the plea of another.
  - beyond the text: gathers the plotting verses into one account of what passes between the plotter and the plotted against
  - rests on: observation 12514 (strand-reading key-statement, live; Act 27:42, Joh 11:53, Joh 12:10, Neh 6:2, Neh 6:6)
  - told in: chapter 10.10 Relating to others, Plotting against another; chapter 10.11 Hiding and disclosing, The hidden trap
- **C-358** (narrative, verdict New, status current, in narrative 1): What is devised comes back on the one who devised it, and the schemer is named by his plan and told to stop it at the mouth.
  - beyond the text: reads the return of the plan as the end of the path from thought to deed
  - rests on: observation 12510 (strand-reading key-statement, live; Deu 19:19, Pro 24:8); observation 12452 (strand-reading key-statement, live; Est 9:25, Pro 16:3, Pro 21:5)
  - told in: chapter 10.4 Thinking, What is devised comes back; chapter 10.0 The inner being at work, The path runs back; chapter 10.10 Relating to others, Plotting against another
- **C-359** (narrative, verdict New, status current, in narrative 1): Looking ahead weighs ability and cost before acting, plans under uncertainty, carries a person's word, can part companions or set one apart from a council's decision, and can plan another's good.
  - beyond the text: reads the voyage of Acts 27 as the fullest picture of planning without knowing
  - rests on: observation 12518 (strand-reading key-statement, live; Act 27:13)
  - told in: chapter 10.7 Choosing and setting direction, Planning
- **C-360** (narrative, verdict New, status current, in narrative 1): A human plan is real in its reach, and its outcome rests with God.
  - beyond the text: reads the rest of the planning verses inside Pro 16:9
  - rests on: observation 12520 (strand-reading key-statement, live; Act 5:38, Rom 1:13)
  - told in: chapter 10.7 Choosing and setting direction, Planning
- **C-361** (narrative, verdict New, status current, in narrative 1): God also thinks and plans: his plan stands where human plans cross it, he takes thought for the one in need, and he speaks in his heart.
  - beyond the text: sets God's thinking beside human thinking as the same words with a different end
  - rests on: observation 12430 (strand-reading key-statement, live; Gen 50:20, Jer 29:11, Job 42:2, Pro 19:21, Psa 33:10, Psa 33:11); observation 12450 (strand-reading key-statement, live; Gen 50:20); observation 12423 (strand-reading key-statement, live; Gen 6:5, Gen 8:21)
  - told in: chapter 11 Other sides of the inner being, 8. God has a heart and a soul; chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 13.1 Divine, Purposing
- **C-362** (narrative, verdict New, status current, in narrative 1): What the heart devises on its own can be a rival worship, a false report, or a god its maker trusts.
  - beyond the text: joins the self-devised feast, the invented report and the idol as the same capacity making up what is not there
  - rests on: observation 12508 (strand-reading key-statement, live; 1Cor 4:5)
  - told in: chapter 10.7 Choosing and setting direction, Planning; chapter 12 When the inner being goes wrong, Idols taken inside; chapter 10.4 Thinking, When thinking changes character
- **C-363** (narrative, verdict New, status current, in narrative 1): Thoughts and plans are wholly open to God, the inclination is known before it acts, and the purposes of the heart will be disclosed.
  - beyond the text: reads God's knowing of the inclination as before the act, from Deu 31:21
  - rests on: observation 12431 (strand-reading key-statement, live; 1Ch 28:9); observation 12413 (strand-reading key-statement, live; 1Ch 28:9)
  - told in: chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 04 The heart, The heart is hidden, and God sees it; chapter 10.7 Choosing and setting direction, Planning
- **C-364** (narrative, verdict New, status current, in narrative 1): A purpose can be set ahead and held, for one's own speech and faithfulness; it can be kept and directed by God, and the mind's setting decides its direction.
  - beyond the text: reads David's prayer as asking God to hold the purpose in place
  - rests on: observation 12509 (strand-reading key-statement, live; Psa 17:3); observation 12434 (strand-reading key-statement, live; 1Ch 29:18)
  - told in: chapter 10.7 Choosing and setting direction, Planning
- **C-366** (narrative, verdict New, status current, in narrative 1): Thoughts often arise unbidden, at night, and what arises is shaped from outside: by God's gift of skill, by instruction, or by blinding.
  - beyond the text: reads the arising thought as not chosen, from where the verses place it
  - rests on: observation 12411 (strand-reading key-statement, live; Pro 15:22, Pro 20:18)
  - told in: chapter 10.4 Thinking, Where thoughts come from
- **C-367** (narrative, verdict New, status current, in narrative 1): The heart is where thoughts and plans come from.
  - beyond the text: names the heart as the place of planning, from the verses that say it
  - rests on: observation 12407 (strand-reading key-statement, live; Isa 10:7, Pro 16:9, Pro 6:18, Psa 140:2)
  - told in: chapter 10.4 Thinking, Where thoughts come from; chapter 04 The heart, The heart thinks, attends and remembers
- **C-369** (narrative, verdict New, status current, in narrative 1): The inclination of the heart (yetser) is the same word as the potter's thing formed and as our frame; it is evil in Gen 6:5 and stayed on God in Isa 26:3.
  - beyond the text: reads the inclination as a shaped thing, from the word's other uses
  - rests on: observation 12412 (strand-reading key-statement, live; 1Ch 28:9, Gen 6:5, Gen 8:21)
  - told in: chapter 10.4 Thinking, The inclination: a shaped thing; chapter 12 When the inner being goes wrong, The heart as the source
- **C-370** (narrative, verdict New, status current, in narrative 1): Read together, the verses trace a path from a thought arising to the deed: lodging, reckoning, devising, the tongue, lips and eyes, then the hand and feet; no single verse lists it.
  - beyond the text: the order is a reading of many verses together
  - rests on: observation 12424 (strand-reading key-statement, live; Pro 16:30, Pro 6:18)
  - told in: chapter 10.0 The inner being at work, From a thought to a deed; chapter 10.5 Speaking, The tongue, the lips and the eyes devise
- **C-371** (narrative, verdict New, status current, in narrative 1): The commands meet the path from where a thought lodges onward; none addresses what first arises, though what arises is not neutral.
  - beyond the text: reads responsibility as beginning where the thought lodges
  - rests on: observation 12428 (strand-reading key-statement, live; Gen 6:5)
  - told in: chapter 10.0 The inner being at work, Where I am answerable
- **C-373** (narrative, verdict New, status current, in narrative 1): Thinking likens: the Hebrew damah means both to be like and to think.
  - beyond the text: reads likening as a kind of thinking, from the one verb
  - rests on: observation 12416 (strand-reading key-statement, live; Isa 10:7)
  - told in: chapter 10.4 Thinking, What thinking does
- **C-375** (narrative, verdict New, status current, in narrative 1): God's devising against a people answers what they devise, and is spoken so that they may turn; he relents.
  - beyond the text: reads the hearing and turning of the people as part of what happens to the plan
  - rests on: observation 12442 (strand-reading key-statement, live; Jer 18:11, Jer 18:8, Jer 26:3, Jer 36:3)
  - told in: chapter 13.1 Divine, Purposing; chapter 10.4 Thinking, When thinking changes character
- **C-376** (narrative, verdict New, status current, in narrative 1): God forms a plan, makes it known, carries it out, and those it came upon recognise it afterward.
  - beyond the text: reads the plan as announced rather than hidden
  - rests on: observation 12512 (strand-reading key-statement, live; Lam 2:17, Zec 1:6)
  - told in: chapter 13.1 Divine, Purposing
- **C-377** (narrative, verdict New, status current, in narrative 1): God also purposes and does not turn back, for judgement and for good; the verses do not explain how this stands with his relenting.
  - beyond the text: leaves the relenting and the fixed purpose side by side as written
  - rests on: observation 12511 (strand-reading key-statement, live; Heb 6:17, Jer 4:28, Zec 8:15)
  - told in: chapter 13.1 Divine, Purposing
- **C-378** (narrative, verdict New, status current, in narrative 1): God's plan takes in what people do against him without excusing them.
  - beyond the text: reads the plan and the guilt as stated together
  - rests on: observation 12519 (strand-reading key-statement, live; Act 2:23, Act 4:28)
  - told in: chapter 13.1 Divine, Purposing
- **C-379** (narrative, verdict New, status current, in narrative 1): God's purpose stands before the ages, does not rest on works, and is set forth in Christ.
  - beyond the text: gathers the Pauline purpose verses into one account
  - rests on: observation 12524 (strand-reading key-statement, live; 2Ti 1:9, Eph 1:11, Eph 3:11, Rom 9:11)
  - told in: chapter 13.1 Divine, Purposing
- **C-380** (narrative, verdict New, status current, in narrative 1): The Spirit intercedes according to God's will, the purpose is turned toward those who love him, and a person can reject it for himself.
  - beyond the text: sets the Spirit's praying, the purpose for those who love him, and its refusal in one account
  - rests on: observation 12522 (strand-reading key-statement, live; Luk 7:30, Rom 8:28)
  - told in: chapter 13.1 Divine, Purposing
- **C-382** (narrative, verdict New, status current, in narrative 1): The will resolves, intends and steers; a resolve can still be weighed and redirected, an intention stopped, and one will can stand against a group's plan.
  - beyond the text: reads Joseph's considering as where God spoke into the resolve
  - rests on: observation 12515 (strand-reading key-statement, live; Act 12:4)
  - told in: chapter 10.7 Choosing and setting direction, Willing; chapter 10.10 Relating to others, Plotting against another
- **C-383** (narrative, verdict New, status current, in narrative 1): Wanting set on riches or the world leads into a snare and into enmity with God, and an intention can be pinned on another.
  - beyond the text: sets the wish for riches and for the world's friendship side by side
  - rests on: observation 12523 (strand-reading key-statement, live; Act 5:28)
  - told in: chapter 10.7 Choosing and setting direction, Willing; chapter 10.10 Relating to others, Plotting against another

### 5.2 Claims reached by a verse only (6)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| 2-16 | The verse puts soul and spirit beside joints and marrow, which are adjacent, and its end point is the heart: "discerning the thoughts and intentions of the heart". It shows closeness that only the word can divide. It is one of several places the words part; others are added (1Co 15:45; 1Co 14:14–15; the *psychikos* / *pneumatikos* contrast in 1Co 2:14; 15:44–46) (dep §3.4; B §8) | Heb 4:12 | intentions G1771 | current | not told in a section |
| 4-4 | Hebrew has no word for "mind"; it uses *lēv* | Pro 19:21; Gen 6:5 | plans H4284; purpose H6098; intention H3336 | current | chapter 04 The heart, The heart thinks, attends and remembers |
| 9-1 | Scripture locates the source of evil chiefly in the heart: "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21); "the heart is deceitful above all things" (Jer 17:9); sin "engraved on the tablet of their heart" (Jer 17:1). The vice-list catalogue is not yet read (D §11.1, §11.7). Added 2026-10-01: Gen 6:5's "intention" is *yēṣer*, the formed inclination of the heart. It must be read with Gen 8:21, where the same evil inclination is the ground of God's forbearance | Gen 6:5; Gen 8:21 | intention H3336 | current | chapter 12 When the inner being goes wrong, The heart as the source |
| C-89 | Scripture speaks of death as sleep, and gives its hope against death as waking | John 11:11-14 | meant G3004G | current | chapter 02 Life, breath and death, Sleep and waking (2 earlier telling(s) in the workbook) |
| C-112 | When the breath goes, a person's plans go with it | Psalm 146:4 | plans H6250 | current | chapter 02 Life, breath and death, Breath lent, and held by God (1 earlier telling(s) in the workbook) |
| C-113 | God holds both ends, killing and making alive, and keeps alive between them | Genesis 50:20 | meant H2803I | current | chapter 02 Life, breath and death, Breath lent, and held by God (1 earlier telling(s) in the workbook) |

### 5.3 The narrative sections that tell these claims (22)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 6 | 02 Life, breath and death | Breath lent, and held by God | C-112, C-113 |
| 14 | 02 Life, breath and death | Sleep and waking | C-89 |
| 42 | 04 The heart | The heart thinks, attends and remembers | 4-4, C-367 |
| 50 | 04 The heart | The heart is hidden, and God sees it | C-363 |
| 92 | 10.0 The inner being at work | From a thought to a deed | C-370 |
| 94 | 10.0 The inner being at work | The path runs back | C-358 |
| 95 | 10.0 The inner being at work | Where I am answerable | C-371 |
| 135 | 10.4 Thinking | Where thoughts come from | C-366, C-367 |
| 136 | 10.4 Thinking | The inclination: a shaped thing | C-369 |
| 137 | 10.4 Thinking | What thinking does | C-373 |
| 138 | 10.4 Thinking | When thinking changes character | C-362, C-375 |
| 142 | 10.4 Thinking | What is devised comes back | C-358 |
| 144 | 10.4 Thinking | Small, passing, and wholly seen | C-361, C-363 |
| 149 | 10.5 Speaking | The tongue, the lips and the eyes devise | C-370 |
| 196 | 10.7 Choosing and setting direction | Planning | C-359, C-360, C-362, C-363, C-364 |
| 197 | 10.7 Choosing and setting direction | Willing | C-382, C-383 |
| 229 | 10.10 Relating to others | Plotting against another | C-356, C-358, C-382, C-383 |
| 240 | 10.11 Hiding and disclosing | The hidden trap | C-356 |
| 302 | 11 Other sides of the inner being | 8. God has a heart and a soul | C-361 |
| 304 | 12 When the inner being goes wrong | The heart as the source | 9-1, C-369 |
| 313 | 12 When the inner being goes wrong | Idols taken inside | C-362 |
| 324 | 13.1 Divine | Purposing | C-361, C-375, C-376, C-377, C-378, C-379, C-380 |

## 6. Phrases attached to the collection (1)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| made plans | 7626 | english route: word plans | 2 | 0 | 3 | 2 |

## 7. Stored-data faults

Blatant errors and omissions in the stored rows, each found by the rule stated. A fault is shown with the rows that identify it; the first 25 of a long list are shown and every row is in the workbook sheet `Faults`.

| rule | what it looks for | found |
|---|---|---|
| link-to-missing-or-deleted-term | live collection_link of this collection whose term_id has no live surface_term row | 0 |
| collection-merge-inconsistent | collection.status and collection.merged_into_id disagree, or the target is not live | 0 |
| member-surface-with-no-occurrence | member term of origin 'surface' that no live verse_lexical row carries | 0 |
| occurrence-in-deleted-verse | occurrence whose verse row is soft deleted | 0 |
| live-node-on-deleted-observation | ib_node with deleted=0 whose observation is deleted or missing (the node still names a verse and word the observation no longer covers) | 0 |
| claim-source-on-deleted-observation | narrative_claim_source naming an observation that is deleted or missing | 0 |
| claim-in-narrative-with-no-current-telling | narrative_claim.in_narrative=1 and no current narrative_claim_telling | 0 |
| live-node-with-no-verse-lexical-id | live ib_node in a verse of the report with a member surface but verse_lexical_id NULL (stored, tied to no occurrence) | 0 |

## 8. Sources

Occurrences: live verse_lexical rows, with the verse text from table `verse`; Strong's data from `strong`, `strong_sense`, `strong_meaning_tree`, `strong_related`, `cluster_strong`; observations and nodes from `ib_observation` and `ib_node` (an observation is withdrawn when deleted = 1); claims from `narrative_claim_source` (by observation_id or verse_id), `narrative_claim`, `narrative_claim_telling` and `narrative_section`. A table or column was used only after its recorded meaning in `cfg_table` and `cfg_column` was read (rule B:123).

