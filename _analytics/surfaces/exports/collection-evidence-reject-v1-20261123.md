# Collection evidence report: reject

Generated 2026-11-23T14:56:16Z by run RUN-20261123_145605_590-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-reject-v1-20261123.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection reject at a glance

Status confirmed; core term 1276; created 2026-11-06T06:30:58Z, updated 2026-11-10T16:03:13Z; run RUN-20261110_160312_587-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (34)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| accept | word | opposite | accept | placed | 53 | 50 |
| accept circumcision | phrase | phrase | accept circumcision | placed | 1 | 1 |
| acceptable | word | opposite | accept | placed | 20 | 18 |
| accepted | word | opposite | accept | placed | 25 | 21 |
| accepted me | phrase | phrase | accepted me | placed | 1 | 1 |
| accepts | word | opposite | accept | placed | 5 | 5 |
| accepts circumcision | phrase | phrase | accepts circumcision | placed | 1 | 1 |
| cast off | phrase | phrase | cast off | placed | 9 | 8 |
| denied | word | synonym | deny | placed | 17 | 17 |
| deny | word | synonym | deny | placed | 25 | 24 |
| denying | word | synonym | deny | placed | 3 | 3 |
| disqualified | word | synonym | disqualify | placed | 2 | 2 |
| disqualify | word | synonym | disqualify | placed | 1 | 1 |
| disregard | word | synonym | disregard | placed | 1 | 1 |
| disregarded | word | synonym | disregard | placed | 3 | 2 |
| exclude | word | synonym | exclude | placed | 1 | 1 |
| excluded | word | synonym | exclude | placed | 3 | 3 |
| more acceptable | phrase | phrase | more acceptable | placed | 2 | 2 |
| oppose | word | synonym | oppose | placed | 3 | 3 |
| opposed | word | synonym | oppose | placed | 12 | 10 |
| opposes | word | synonym | oppose | placed | 6 | 6 |
| refuse | word | synonym | refuse | placed | 46 | 37 |
| refused | word | synonym | refuse | placed | 36 | 28 |
| refused him | phrase | phrase | refused him | placed | 1 | 1 |
| refusing | word | synonym | refuse | placed | 3 | 3 |
| reject | word | core | reject | placed | 9 | 8 |
| reject him | phrase | phrase | reject him | placed | 1 | 1 |
| rejected | word | synonym | reject | placed | 65 | 56 |
| rejecting | word | synonym | reject | placed | 2 | 2 |
| rejection | word | synonym | reject | placed | 1 | 1 |
| rejects | word | synonym | reject | placed | 6 | 3 |
| renounce | word | synonym | renounce | placed | 3 | 3 |
| renounced | word | synonym | renounce | placed | 2 | 2 |
| renounces | word | synonym | renounce | placed | 1 | 1 |

### 2.2 The Strong's codes behind the members (97)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H3988A מָאַס ma.as "to reject" | 40 | 6 | 41 | rejected 30, reject 6, cast off 2, refuse 2 | none | 16 |
| H3985 מָאֵן ma.en "to refuse" | 33 | 0 | 32 | refused 21, refuse 11, refusing 1 | none | 6 |
| G0720 ἀρνέομαι arneomai "to deny" | 28 | 0 | 27 | denied 13, deny 10, denying 2, refused 1, rejected 1, renounce 1 | none | 0 |
| H3947H לָקַח la.qach "to take: recieve" | 22 | 1 | 23 | accept 17, accepts 4, accepted 1 | none | 0 |
| H7521 רָצָה ra.tsah "to accept" | 19 | 2 | 21 | accept 13, accepted 3, acceptable 1, accepted me 1, accepts 1 | none | 2 |
| H7522 רָצוֹן ra.tson "acceptance" | 12 | 2 | 14 | accepted 7, acceptable 5 | none | 8 |
| G0533 ἀπαρνέομαι aparneomai "to deny" | 11 | 0 | 11 | deny 10, denied 1 | none | 0 |
| H2186A זָנַח za.nach "to reject" | 9 | 0 | 9 | rejected 6, cast off 2, reject 1 | none | 2 |
| G0114 ἀθετέω atheteō "to reject" | 8 | 0 | 5 | rejects 5, reject 1, rejected 1, rejecting 1 | none | 2 |
| G0593 ἀποδοκιμάζω apodokimazō "to reject" | 8 | 1 | 9 | rejected 8 | none | 1 |
| G1209 δέχομαι dechomai "to receive" | 6 | 1 | 7 | accept 3, accepted 3 | none | 0 |
| G0436 ἀνθίστημι anthistēmi "to oppose" | 5 | 0 | 4 | opposed 4, oppose 1 | none | 0 |
| G2144 εὐπρόσδεκτος euprosdektos "acceptable" | 4 | 0 | 4 | acceptable 4 | none | 0 |
| H3584 כָּחַשׁ ka.chash "to deceive" | 4 | 0 | 4 | deny 2, denied 1, denying 1 | none | 1 |
| H3986 מָאֵן ma.en "refusing" | 4 | 0 | 4 | refuse 4 | none | 0 |
| H5106 נוּא nu "to forbid" | 4 | 0 | 3 | opposes 2, opposed 1, refuse 1 | none | 0 |
| H7725L שׁוּב shuv "to return: refuse" | 4 | 0 | 3 | refuse 4 | none | 0 |
| G0498 ἀντιτάσσω antitassō "to resist" | 3 | 0 | 3 | opposes 2, opposed 1 | none | 0 |
| G0683 ἀπωθέω apōtheō "to reject" | 3 | 0 | 3 | rejected 2, rejecting 1 | none | 1 |
| G2101 εὐάρεστος euarestos "well-pleasing" | 3 | 0 | 3 | acceptable 3 | none | 0 |
| G3858 παραδέχομαι paradechomai "to welcome" | 3 | 0 | 3 | accept 3 | none | 0 |
| G3868 παραιτέομαι paraiteomai "to refuse/excuse" | 3 | 0 | 2 | refuse 2, refused him 1 | none | 0 |
| H6901 קָבַל qa.val "to receive" | 3 | 0 | 3 | accept 2, accepted 1 | none | 0 |
| G0096 ἀδόκιμος adokimos "failing" | 2 | 0 | 2 | disqualified 2 | none | 0 |
| G0480 ἀντίκειμαι antikeimai "be an opponent" | 2 | 0 | 2 | opposed 1, opposes 1 | none | 2 |
| G0483 ἀντιλέγω antilegō "to dispute" | 2 | 1 | 3 | deny 1, opposes 1 | none | 0 |
| G0654 ἀποστρέφω apostrefō "to turn away" | 2 | 0 | 2 | refuse 1, reject him 1 | none | 0 |
| G1184 δεκτός dektos "acceptable" | 2 | 0 | 2 | acceptable 2 | none | 0 |
| G4059 περιτέμνω peritemnō "to circumcise" | 2 | 0 | 2 | accept circumcision 1, accepts circumcision 1 | none | 0 |
| G4327 προσδέχομαι prosdechomai "to wait for/welcome" | 2 | 1 | 3 | accept 1, accepted 1 | none | 0 |
| H1115 בִּלְתִּי bil.ti "lest" | 2 | 0 | 2 | refusing 2 | none | 0 |
| H2310 חָדֵל cha.del "rejected/fleeting" | 2 | 0 | 2 | refuse 1, rejected 1 | none | 0 |
| H4513 מָנַע ma.na "to withhold" | 2 | 0 | 2 | deny 1, refuse 1 | none | 0 |
| H5006 נָאַץ na.ats "to spurn" | 2 | 0 | 2 | renounce 1, renounces 1 | none | 1 |
| H5203 נָטַשׁ na.tash "to leave" | 2 | 0 | 2 | rejected 2 | none | 0 |
| H5375Q נָשָׂא na.sa "to lift: kindness" | 2 | 1 | 3 | accept 2 | none | 2 |
| G0142 αἴρω airō "to take up" | 1 | 0 | 1 | denied 1 | none | 0 |
| G0430 ἀνέχω anechō "to endure" | 1 | 0 | 1 | accept 1 | none | 0 |
| G0550 ἀπεῖπον apeipon "to renounce" | 1 | 0 | 1 | renounced 1 | none | 0 |
| G0579 ἀπόβλητος apoblētos "rejected" | 1 | 0 | 1 | rejected 1 | none | 0 |
| G0580 ἀποβολή apobolē "deprivation" | 1 | 0 | 1 | rejection 1 | none | 0 |
| G0588 ἀποδέχομαι apodechomai "to receive" | 1 | 0 | 1 | accept 1 | none | 0 |
| G0657 ἀποτάσσω apotassō "to leave" | 1 | 0 | 1 | renounce 1 | none | 0 |
| G0659 ἀποτίθημι apotithēmi "to put aside" | 1 | 0 | 1 | cast off 1 | none | 0 |
| G0873 ἀφορίζω aforizō "to separate" | 1 | 0 | 1 | exclude 1 | none | 0 |
| G1576 ἐκκλείω ekkleiō "to exclude" | 1 | 0 | 1 | excluded 1 | none | 0 |
| G1727 ἐναντίος enantios "hostile" | 1 | 0 | 1 | oppose 1 | none | 0 |
| G1848 ἐξουθενέω exoutheneō "to reject" | 1 | 0 | 1 | rejected 1 | none | 0 |
| G2102 εὐαρέστως euarestōs "acceptably" | 1 | 0 | 1 | acceptable 1 | none | 0 |
| G2603 καταβραβεύω katabrabeuō "to disqualify" | 1 | 0 | 1 | disqualify 1 | none | 0 |
| G3361 μή mē "not" | 1 | 0 | 1 | refuse 1 | none | 0 |
| G3756 οὐ ou "no" | 1 | 7 | 8 | refuse 1 | none | 0 |
| G4014 περιαιρέω periaireō "to take away" | 1 | 0 | 1 | cast off 1 | none | 0 |
| G4065 περιφρονέω perifroneō "to despise" | 1 | 0 | 1 | disregard 1 | none | 0 |
| G4067 περίψημα peripsēma "scum" | 1 | 0 | 1 | refuse 1 | none | 0 |
| G4183 πολύς polus "much" | 1 | 0 | 1 | more acceptable 1 | none | 0 |
| H0977 בָּחַר ba.char "to choose" | 1 | 0 | 1 | more acceptable 1 | none | 1 |
| H1351 גָּאַל ga.al "to defile" | 1 | 0 | 1 | excluded 1 | none | 0 |
| H1624 גָּרָה ga.rah "to stir up" | 1 | 0 | 1 | opposed 1 | none | 0 |
| H2308 חָדַל cha.dal "to cease" | 1 | 3 | 4 | refuse 1 | none | 0 |
| H3582 כָּחַד ka.chad "to hide" | 1 | 0 | 1 | denied 1 | none | 1 |
| H3925H לָמַד la.mad "to learn: learn" | 1 | 0 | 1 | accept 1 | none | 0 |
| H3987 מֵאֵן me.en "refusing" | 1 | 0 | 1 | refuse 1 | none | 0 |
| H5010 נָאַר na.ar "to disown" | 1 | 0 | 1 | renounced 1 | none | 0 |
| H5186 נָטָה na.tah "to stretch" | 1 | 0 | 1 | deny 1 | none | 0 |
| H5234A נָכַר na.khar "to recognize" | 1 | 0 | 1 | accept 1 | none | 0 |
| H5375H נָשָׂא na.sa "to lift: bear" | 1 | 0 | 1 | accept 1 | none | 0 |
| H5375P נָשָׂא na.sa "to lift: vow" | 1 | 0 | 1 | accepted 1 | none | 0 |
| H5478 סוּחָה su.chah "offal" | 1 | 0 | 1 | refuse 1 | none | 0 |
| H5493I סוּר sur "to turn aside: turn aside" | 1 | 0 | 1 | rejected 1 | none | 0 |
| H5541A סָלָה sa.lah "to reject" | 1 | 0 | 1 | rejected 1 | none | 0 |
| H5674A עָבַר a.var "to pass" | 1 | 0 | 1 | disregarded 1 | none | 0 |
| H5800H עָזַב a.zav "to leave: neglect" | 1 | 0 | 1 | rejects 1 | none | 0 |
| H7306 רִיחַ ri.ach "to smell" | 1 | 0 | 1 | accept 1 | none | 0 |
| H7613 שְׂאֵת se.et "elevation" | 1 | 0 | 1 | accepted 1 | none | 0 |
| H7843 שָׁחַת sha.chat "to ruin" | 1 | 0 | 1 | cast off 1 | none | 1 |
| H7854 שָׂטָן sa.tan "Satan" | 1 | 0 | 1 | oppose 1 | none | 0 |
| H8232 שְׁפַר she.phar "to acceptable" | 1 | 0 | 1 | acceptable 1 | none | 0 |
| G1014 βούλομαι boulomai "to plan" | 0 | 1 | 1 |  | none | 1 |
| G1161 δέ de "then" | 0 | 2 | 2 |  | none | 0 |
| G2309 θέλω thelō "to will/desire" | 0 | 6 | 6 |  | none | 4 |
| G2532 καί kai "and" | 0 | 2 | 2 |  | none | 0 |
| G3303 μέν men "on the other hand" | 0 | 1 | 1 |  | none | 0 |
| H0014 אָבָה a.vah "be willing" | 0 | 1 | 1 |  | none | 1 |
| H0518A אִם im "if" | 0 | 3 | 3 |  | none | 0 |
| H0853 אֵת et "[Obj.]" | 0 | 4 | 3 |  | none | 0 |
| H1504 גָּזַר ga.zar "to cut" | 0 | 1 | 1 |  | none | 0 |
| H1931 הוּא hu "he/she/it" | 0 | 1 | 1 |  | none | 0 |
| H1961 הָיָה ha.yah "to be" | 0 | 1 | 1 |  | none | 0 |
| H3588A כִּי ki "for" | 0 | 4 | 4 |  | none | 0 |
| H3808 לֹא lo "not" | 0 | 3 | 3 |  | none | 0 |
| H5869A עַ֫יִן a.yin "eye" | 0 | 1 | 1 |  | none | 0 |
| H5921A עַל al "upon" | 0 | 2 | 2 |  | none | 0 |
| H5956 עָלַם a.lam "to conceal" | 0 | 1 | 1 |  | none | 0 |
| H5975G עָמַד a.mad "to stand: stand" | 0 | 1 | 1 |  | none | 0 |
| H6440N פָּנֶה pa.neh "face: kindness" | 0 | 1 | 1 |  | none | 1 |
| H7126H קָרַב qa.rav "to present: bring" | 0 | 1 | 1 |  | none | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.79.

### 3.1 H3988A מָאַס ma.as "to reject": 40 own occurrences in 36 verses

- **Meaning as stored:** Hebrew; native word מָאַס, transliteration ma.as; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3988):** to reject, despise, refuse.
- **Related terms (2):** H3973 ma.os "refuse"; H3988B ma.as "to flow".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 74; verses STEP attests 67; verse_lexical rows the parse found 74.

- **Carried by the member words:** rejected (30), reject (6), cast off (2), refuse (2).
- **Engagement of these occurrences:** none recorded 40.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ki 23:27 | cast off | HVqq1cs | none recorded | 19704, 19784 | 0 | And the Lord said, “I will remove Judah also out of my sight, as I have removed Israel, and I will **cast off** this city that I have chosen, Jerusalem, and the house of which I said, My name shall be there.” |
| Jer 31:37 | cast off | HVqi1cs | none recorded | - | 0 | Thus says the Lord: “ If the heavens above can be measured, and the foundations of the earth below can be explored, then I will **cast off** all the offspring of Israel for all that they have done, declares the Lord.” |
| Isa 7:15 | refuse | HVqaa | none recorded | 19471, 19472, 19607, 19641, 19651, 19657, 19660, 19664, 19679, 19739, 19788, 19836, 19839, 20308, 20313 | 0 | He shall eat curds and honey when he knows how to **refuse** the evil and choose the good. |
| Isa 7:16 | refuse | HVqaa | none recorded | 19472, 19597, 19652, 19657, 19679, 19739 | 0 | For before the boy knows how to **refuse** the evil and choose the good, the land whose two kings you dread will be deserted. |
| Job 8:20 | reject | HVqi3ms | none recorded | - | 0 | “ Behold, God will not **reject** a blameless man, nor take the hand of evildoers. |
| Job 34:33 | reject | HVqp2ms | none recorded | 19472, 19587, 19836, 19910, 20307 | 0 | Will he then make repayment to suit you, because you **reject** it? For you must choose, and not I; therefore declare what you know. |
| Psa 36:4 | reject | HVqi3ms | none recorded | - | 0 | He plots trouble while on his bed; he sets himself in a way that is not good; he does not **reject** evil. |
| Jer 33:26 | reject | HVqi1cs | none recorded | - | 0 | then I will **reject** the offspring of Jacob and David my servant and will not choose one of his offspring to rule over the offspring of Abraham, Isaac, and Jacob. For I will restore their fortunes and will have mercy on them.” |
| Hos 4:6 | reject | HVqu1cs | none recorded | - | 0 | My people are destroyed for lack of knowledge; because you have rejected knowledge, I **reject** you from being a priest to me. And since you have forgotten the law of your God, I also will forget your children. |
| Hos 9:17 | reject | HVqi3ms | none recorded | - | 0 | My God will **reject** them because they have not listened to him; they shall be wanderers among the nations. |
| Num 14:31 | rejected | HVqp2mp | none recorded | - | 0 | But your little ones, who you said would become a prey, I will bring in, and they shall know the land that you have **rejected**. |
| 1Sa 10:19 | rejected | HVqp2mp | none recorded | - | 0 | But today you have **rejected** your God, who saves you from all your calamities and your distresses, and you have said to him, ‘ Set a king over us.’ Now therefore present yourselves before the Lord by your tribes and by your thousands.” |
| 1Sa 15:23 | rejected | HVqp2ms | none recorded | 17525 | 0 | For rebellion is as the sin of divination, and presumption is as iniquity and idolatry. Because you have **rejected** the word of the Lord, he has also rejected you from being king.” |
| 1Sa 15:23 | rejected | HVqw3ms | none recorded | - | 0 | For rebellion is as the sin of divination, and presumption is as iniquity and idolatry. Because you have **rejected** the word of the Lord, he has also rejected you from being king.” |
| 1Sa 15:26 | rejected | HVqp2ms | none recorded | 18008, 19174 | 0 | And Samuel said to Saul, “I will not return with you. For you have **rejected** the word of the Lord, and the Lord has rejected you from being king over Israel.” |
| 1Sa 15:26 | rejected | HVqw3ms | none recorded | - | 0 | And Samuel said to Saul, “I will not return with you. For you have **rejected** the word of the Lord, and the Lord has rejected you from being king over Israel.” |
| 1Sa 16:1 | rejected | HVqp1cs | none recorded | - | 0 | The Lord said to Samuel, “ How long will you grieve over Saul, since I have **rejected** him from being king over Israel? Fill your horn with oil, and go. I will send you to Jesse the Bethlehemite, for I have provided for myself a king among his sons.” |
| 1Sa 16:7 | rejected | HVqp1cs | none recorded | 17166 | 0 | But the Lord said to Samuel, “Do not look on his appearance or on the height of his stature, because I have **rejected** him. For the Lord sees not as man sees: man looks on the outward appearance, but the Lord looks on the heart.” |
| 2Ki 17:20 | rejected | HVqw3ms | none recorded | - | 0 | And the Lord **rejected** all the descendants of Israel and afflicted them and gave them into the hand of plunderers, until he had cast them out of his sight. |
| Job 31:13 | rejected | HVqi1cs | none recorded | - | 0 | “ If I have **rejected** the cause of my manservant or my maidservant, when they brought a complaint against me, |
| Psa 53:5 | rejected | HVqp3ms | none recorded | - | 0 | There they are, in great terror, where there is no terror! For God scatters the bones of him who encamps against you; you put them to shame, for God has **rejected** them. |
| Psa 78:59 | rejected | HVqw3ms | none recorded | - | 0 | When God heard, he was full of wrath, and he utterly **rejected** Israel. |
| Psa 78:67 | rejected | HVqw3ms | none recorded | 19711 | 0 | He **rejected** the tent of Joseph; he did not choose the tribe of Ephraim, |
| Psa 89:38 | rejected | HVqw2ms | none recorded | - | 0 | But now you have cast off and **rejected**; you are full of wrath against your anointed. |
| Psa 118:22 | rejected | HVqp3cp | none recorded | - | 0 | The stone that the builders **rejected** has become the cornerstone. |
| Isa 5:24 | rejected | HVqp3cp | none recorded | 14658 | 0 | Therefore, as the tongue of fire devours the stubble, and as dry grass sinks down in the flame, so their root will be as rottenness, and their blossom go up like dust; for they have **rejected** the law of the Lord of hosts, and have despised the word of the Holy One of Israel. |
| Jer 2:37 | rejected | HVqp3ms | none recorded | - | 0 | From it too you will come away with your hands on your head, for the Lord has **rejected** those in whom you trust, and you will not prosper by them. |
| Jer 6:19 | rejected | HVqw3mp | none recorded | - | 0 | Hear, O earth; behold, I am bringing disaster upon this people, the fruit of their devices, because they have not paid attention to my words; and as for my law, they have **rejected** it. |
| Jer 6:30 | rejected | HVNrmsa | none recorded | - | 0 | **Rejected** silver they are called, for the Lord has rejected them.” |
| Jer 6:30 | rejected | HVqp3ms | none recorded | - | 0 | **Rejected** silver they are called, for the Lord has rejected them.” |
| Jer 7:29 | rejected | HVqp3ms | none recorded | 13590, 14704 | 0 | “‘Cut off your hair and cast it away; raise a lamentation on the bare heights, for the Lord has **rejected** and forsaken the generation of his wrath.’ |
| Jer 8:9 | rejected | HVqp3cp | none recorded | - | 0 | The wise men shall be put to shame; they shall be dismayed and taken; behold, they have **rejected** the word of the Lord, so what wisdom is in them? |
| Jer 14:19 | rejected | HVqp2ms | none recorded | 16892, 17163 | 0 | Have you utterly **rejected** Judah? Does your soul loathe Zion? Why have you struck us down so that there is no healing for us? We looked for peace, but no good came; for a time of healing, but behold, terror. |
| Jer 33:24 | rejected | HVqw3ms | none recorded | 19475, 19642, 19711, 19944, 19947, 19959, 20296 | 0 | “Have you not observed that these people are saying, ‘The Lord has **rejected** the two clans that he chose ’? Thus they have despised my people so that they are no longer a nation in their sight. |
| Lam 5:22 | rejected | HVqp2ms | none recorded | 14727 | 0 | unless you have utterly **rejected** us, and you remain exceedingly angry with us. |
| Eze 5:6 | rejected | HVqp3cp | none recorded | - | 0 | And she has rebelled against my rules by doing wickedness more than the nations, and against my statutes more than the countries all around her; for they have **rejected** my rules and have not walked in my statutes. |
| Eze 20:13 | rejected | HVqp3cp | none recorded | - | 0 | But the house of Israel rebelled against me in the wilderness. They did not walk in my statutes but **rejected** my rules, by which, if a person does them, he shall live; and my Sabbaths they greatly profaned. “Then I said I would pour out my wrath upon them in the wilderness, to make a full end of them. |
| Eze 20:16 | rejected | HVqp3cp | none recorded | 16513 | 0 | because they **rejected** my rules and did not walk in my statutes, and profaned my Sabbaths; for their heart went after their idols. |
| Eze 20:24 | rejected | HVqp3cp | none recorded | - | 0 | because they had not obeyed my rules, but had **rejected** my statutes and profaned my Sabbaths, and their eyes were set on their fathers ’ idols. |
| Hos 4:6 | rejected | HVqp2ms | none recorded | - | 0 | My people are destroyed for lack of knowledge; because you have **rejected** knowledge, I reject you from being a priest to me. And since you have forgotten the law of your God, I also will forget your children. |

### 3.2 H3985 מָאֵן ma.en "to refuse": 33 own occurrences in 32 verses

- **Meaning as stored:** Hebrew; native word מָאֵן, transliteration ma.en; STEP gloss "to refuse"; sense head "to refuse" (the code is its own lemma).
- **Related terms (2):** H3986 ma.en "refusing"; H3987 me.en "refusing".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 41; verses STEP attests 39; verse_lexical rows the parse found 41.

- **Carried by the member words:** refused (21), refuse (11), refusing (1).
- **Engagement of these occurrences:** none recorded 33.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 4:23 | refuse | HVpw2ms | none recorded | - | 0 | and I say to you, “Let my son go that he may serve me.” If you **refuse** to let him go, behold, I will kill your firstborn son.’” |
| Exo 10:3 | refuse | HVpp2ms | none recorded | 15335 | 0 | So Moses and Aaron went in to Pharaoh and said to him, “ Thus says the Lord, the God of the Hebrews, ‘ How long will you **refuse** to humble yourself before me? Let my people go, that they may serve me. |
| Exo 16:28 | refuse | HVpp2mp | none recorded | - | 0 | And the Lord said to Moses, “ How long will you **refuse** to keep my commandments and my laws? |
| Pro 21:7 | refuse | HVpp3cp | none recorded | - | 0 | The violence of the wicked will sweep them away, because they **refuse** to do what is just. |
| Pro 21:25 | refuse | HVpp3cp | none recorded | - | 0 | The desire of the sluggard kills him, for his hands **refuse** to labor. |
| Isa 1:20 | refuse | HVpi2mp | none recorded | 19653, 19660, 19839, 20163 | 0 | but if you **refuse** and rebel, you shall be eaten by the sword; for the mouth of the Lord has spoken.” |
| Jer 3:3 | refuse | HVpp2fs | none recorded | - | 0 | Therefore the showers have been withheld, and the spring rain has not come; yet you have the forehead of a whore; you **refuse** to be ashamed. |
| Jer 8:5 | refuse | HVpp3cp | none recorded | - | 0 | Why then has this people turned away in perpetual backsliding? They hold fast to deceit; they **refuse** to return. |
| Jer 9:6 | refuse | HVpp3cp | none recorded | - | 0 | Heaping oppression upon oppression, and deceit upon deceit, they **refuse** to know me, declares the Lord. |
| Jer 25:28 | refuse | HVpi3mp | none recorded | - | 0 | “And if they **refuse** to accept the cup from your hand to drink, then you shall say to them, ‘ Thus says the Lord of hosts: You must drink! |
| Jer 50:33 | refuse | HVpp3cp | none recorded | - | 0 | “ Thus says the Lord of hosts: The people of Israel are oppressed, and the people of Judah with them. All who took them captive have held them fast; they **refuse** to let them go. |
| Gen 37:35 | refused | HVpw3ms | none recorded | - | 0 | All his sons and all his daughters rose up to comfort him, but he **refused** to be comforted and said, “ No, I shall go down to Sheol to my son, mourning.” Thus his father wept for him. |
| Gen 39:8 | refused | HVpw3ms | none recorded | - | 0 | But he **refused** and said to his master’s wife, “ Behold, because of me my master has no concern about anything in the house, and he has put everything that he has in my charge. |
| Gen 48:19 | refused | HVpw3ms | none recorded | - | 0 | But his father **refused** and said, “I know, my son, I know. He also shall become a people, and he also shall be great. Nevertheless, his younger brother shall be greater than he, and his offspring shall become a multitude of nations.” |
| Num 20:21 | refused | HVpw3ms | none recorded | - | 0 | Thus Edom **refused** to give Israel passage through his territory, so Israel turned away from him. |
| Num 22:13 | refused | HVpp3ms | none recorded | - | 0 | So Balaam rose in the morning and said to the princes of Balak, “ Go to your own land, for the Lord has **refused** to let me go with you.” |
| 1Sa 8:19 | refused | HVpw3mp | none recorded | - | 0 | But the people **refused** to obey the voice of Samuel. And they said, “ No! But there shall be a king over us, |
| 1Sa 28:23 | refused | HVpw3ms | none recorded | - | 0 | He **refused** and said, “I will not eat.” But his servants, together with the woman, urged him, and he listened to their words. So he arose from the earth and sat on the bed. |
| 2Sa 2:23 | refused | HVpw3ms | none recorded | 20150 | 0 | But he **refused** to turn aside. Therefore Abner struck him in the stomach with the butt of his spear, so that the spear came out at his back. And he fell there and died where he was. And all who came to the place where Asahel had fallen and died, stood still. |
| 2Sa 13:9 | refused | HVpw3ms | none recorded | - | 0 | And she took the pan and emptied it out before him, but he **refused** to eat. And Amnon said, “ Send out everyone from me.” So everyone went out from him. |
| 1Ki 20:35 | refused | HVpw3ms | none recorded | - | 0 | And a certain man of the sons of the prophets said to his fellow at the command of the Lord, “ Strike me, please.” But the man **refused** to strike him. |
| 1Ki 21:15 | refused | HVpp3ms | none recorded | - | 0 | As soon as Jezebel heard that Naboth had been stoned and was dead, Jezebel said to Ahab, “ Arise, take possession of the vineyard of Naboth the Jezreelite, which he **refused** to give you for money, for Naboth is not alive, but dead.” |
| 2Ki 5:16 | refused | HVpw3ms | none recorded | - | 0 | But he said, “As the Lord lives, before whom I stand, I will receive none.” And he urged him to take it, but he **refused**. |
| Neh 9:17 | refused | HVpw3mp | none recorded | - | 0 | They **refused** to obey and were not mindful of the wonders that you performed among them, but they stiffened their neck and appointed a leader to return to their slavery in Egypt. But you are a God ready to forgive, gracious and merciful, slow to anger and abounding in steadfast love, and did not forsake them. |
| Est 1:12 | refused | HVpw3fs | none recorded | 12998, 13395, 13579, 14192 | 0 | But Queen Vashti **refused** to come at the king’s command delivered by the eunuchs. At this the king became enraged, and his anger burned within him. |
| Psa 78:10 | refused | HVpp3cp | none recorded | - | 0 | They did not keep God’s covenant, but **refused** to walk according to his law. |
| Pro 1:24 | refused | HVpw2mp | none recorded | 15230, 15237 | 0 | Because I have called and you **refused** to listen, have stretched out my hand and no one has heeded, |
| Jer 5:3 | refused | HVpp3cp | none recorded | - | 0 | O Lord, do not your eyes look for truth? You have struck them down, but they felt no anguish; you have consumed them, but they **refused** to take correction. They have made their faces harder than rock; they have refused to repent. |
| Jer 5:3 | refused | HVpp3cp | none recorded | - | 0 | O Lord, do not your eyes look for truth? You have struck them down, but they felt no anguish; you have consumed them, but they **refused** to take correction. They have made their faces harder than rock; they have refused to repent. |
| Jer 11:10 | refused | HVpp3cp | none recorded | - | 0 | They have turned back to the iniquities of their forefathers, who **refused** to hear my words. They have gone after other gods to serve them. The house of Israel and the house of Judah have broken my covenant that I made with their fathers. |
| Hos 11:5 | refused | HVpp3cp | none recorded | - | 0 | They shall not return to the land of Egypt, but Assyria shall be their king, because they have **refused** to return to me. |
| Zec 7:11 | refused | HVpw3mp | none recorded | 14662 | 0 | But they **refused** to pay attention and turned a stubborn shoulder and stopped their ears that they might not hear. |
| Jer 15:18 | refusing | HVpp3fs | none recorded | - | 0 | Why is my pain unceasing, my wound incurable, **refusing** to be healed? Will you be to me like a deceitful brook, like waters that fail? |

### 3.3 G0720 ἀρνέομαι arneomai "to deny": 28 own occurrences in 27 verses

- **Meaning as stored:** Greek; native word ἀρνέομαι, transliteration arneomai; STEP gloss "to deny"; sense head "to deny" (the code is its own lemma).
- **Related terms (2):** G0533 aparneomai "to deny"; G4483 ereō "to say: will say".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 34; verses STEP attests 30; verse_lexical rows the parse found 33.

- **Carried by the member words:** denied (13), deny (10), denying (2), refused (1), rejected (1), renounce (1).
- **Engagement of these occurrences:** none recorded 28.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 26:70 | denied | V-ADI-3S | none recorded | - | 0 | But he **denied** it before them all, saying, “I do not know what you mean.” |
| Mat 26:72 | denied | V-ADI-3S | none recorded | - | 0 | And again he **denied** it with an oath: “I do not know the man.” |
| Mar 14:68 | denied | V-ADI-3S | none recorded | - | 0 | But he **denied** it, saying, “I neither know nor understand what you mean.” And he went out into the gateway and the rooster crowed. |
| Mar 14:70 | denied | V-INI-3S | none recorded | - | 0 | But again he **denied** it. And after a little while the bystanders again said to Peter, “ Certainly you are one of them, for you are a Galilean.” |
| Luk 8:45 | denied | V-PNP-GPM | none recorded | - | 0 | And Jesus said, “ Who was it that touched me?” When all **denied** it, Peter said, “ Master, the crowds surround you and are pressing in on you!” |
| Luk 22:57 | denied | V-ADI-3S | none recorded | - | 0 | But he **denied** it, saying, “ Woman, I do not know him.” |
| Joh 13:38 | denied | V-FDI-2S | none recorded | - | 0 | Jesus answered, “Will you lay down your life for me? Truly, truly, I say to you, the rooster will not crow till you have **denied** me three times. |
| Joh 18:25 | denied | V-ADI-3S | none recorded | - | 0 | Now Simon Peter was standing and warming himself. So they said to him, “ You also are not one of his disciples, are you?” He **denied** it and said, “I am not.” |
| Joh 18:27 | denied | V-ADI-3S | none recorded | - | 0 | Peter again **denied** it, and at once a rooster crowed. |
| Act 3:13 | denied | V-ADI-2P | none recorded | - | 0 | The God of Abraham, the God of Isaac, and the God of Jacob, the God of our fathers, glorified his servant Jesus, whom you delivered over and **denied** in the presence of Pilate, when he had decided to release him. |
| Act 3:14 | denied | V-ADI-2P | none recorded | - | 0 | But you **denied** the Holy and Righteous One, and asked for a murderer to be granted to you, |
| 1Ti 5:8 | denied | V-RDI-3S | none recorded | - | 0 | But if anyone does not provide for his relatives, and especially for members of his household, he has **denied** the faith and is worse than an unbeliever. |
| Rev 3:8 | denied | V-ADI-2S | none recorded | - | 0 | “‘I know your works. Behold, I have set before you an open door, which no one is able to shut. I know that you have but little power, and yet you have kept my word and have not **denied** my name. |
| Mat 10:33 | deny | V-FDI-1S | none recorded | - | 0 | but whoever denies me before men, I also will **deny** before my Father who is in heaven. |
| Luk 9:23 | deny | V-ADM-3S | none recorded | - | 0 | And he said to all, “ If anyone would come after me, let him **deny** himself and take up his cross daily and follow me. |
| Joh 1:20 | deny | V-ADI-3S | none recorded | - | 0 | He confessed, and did not **deny**, but confessed, “ I am not the Christ.” |
| Act 4:16 | deny | V-PNN | none recorded | - | 0 | saying, “ What shall we do with these men? For that a notable sign has been performed through them is evident to all the inhabitants of Jerusalem, and we cannot **deny** it. |
| 2Ti 2:12 | deny | V-FDI-1P | none recorded | - | 0 | if we endure, we will also reign with him; if we **deny** him, he also will deny us; |
| 2Ti 2:12 | deny | V-FDI-3S | none recorded | - | 0 | if we endure, we will also reign with him; if we **deny** him, he also will deny us; |
| 2Ti 2:13 | deny | V-ADN | none recorded | - | 0 | if we are faithless, he remains faithful — for he cannot **deny** himself. |
| Tit 1:16 | deny | V-PNI-3P | none recorded | - | 0 | They profess to know God, but they **deny** him by their works. They are detestable, disobedient, unfit for any good work. |
| Jude 4 | deny | V-PNP-NPM | none recorded | - | 0 | For certain people have crept in unnoticed who long ago were designated for this condemnation, ungodly people, who pervert the grace of our God into sensuality and **deny** our only Master and Lord, Jesus Christ. |
| Rev 2:13 | deny | V-ADI-2S | none recorded | - | 0 | “‘I know where you dwell, where Satan’s throne is. Yet you hold fast my name, and you did not **deny** my faith even in the days of Antipas my faithful witness, who was killed among you, where Satan dwells. |
| 2Ti 3:5 | denying | V-RNP-NPM | none recorded | - | 0 | having the appearance of godliness, but **denying** its power. Avoid such people. |
| 2Pe 2:1 | denying | V-PNP-NPM | none recorded | - | 0 | But false prophets also arose among the people, just as there will be false teachers among you, who will secretly bring in destructive heresies, even **denying** the Master who bought them, bringing upon themselves swift destruction. |
| Heb 11:24 | refused | V-ADI-3S | none recorded | - | 0 | By faith Moses, when he was grown up, **refused** to be called the son of Pharaoh’s daughter, |
| Act 7:35 | rejected | V-ADI-3P | none recorded | - | 0 | “ This Moses, whom they **rejected**, saying, ‘ Who made you a ruler and a judge?’—this man God sent as both ruler and redeemer by the hand of the angel who appeared to him in the bush. |
| Tit 2:12 | renounce | V-ADP-NPM | none recorded | - | 0 | training us to **renounce** ungodliness and worldly passions, and to live self-controlled, upright, and godly lives in the present age, |

### 3.4 H3947H לָקַח la.qach "to take: recieve": 22 own occurrences in 22 verses

- **Meaning as stored:** Hebrew; native word לָקַח, transliteration la.qach; STEP gloss "to take: recieve"; sense head "recieve".
- **Senses (first level of the meaning tree of the lemma H3947):** to take, get, fetch, lay hold of, seize, receive, acquire, buy, bring, ... (cut; the whole text is in the workbook).
- **Related terms (12):** H3947G la.qach "to take: take"; H3947I la.qach "to take: marry"; H3947J la.qach "to take: bring"; H3947K la.qach "to take: buy"; H3947L la.qach "to take: fire"; H3948 le.qach "teaching"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 77; verses STEP attests 0; verse_lexical rows the parse found 70.

- **Carried by the member words:** accept (17), accepts (4), accepted (1).
- **Engagement of these occurrences:** none recorded 22.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 23:13 | accept | HVqv2ms | none recorded | - | 0 | And he said to Ephron in the hearing of the people of the land, “But if you will, hear me: I give the price of the field. **Accept** it from me, that I may bury my dead there.” |
| Gen 33:10 | accept | HVqq2ms | none recorded | - | 0 | Jacob said, “ No, please, if I have found favor in your sight, then **accept** my present from my hand. For I have seen your face, which is like seeing the face of God, and you have accepted me. |
| Gen 33:11 | accept | HVqv2ms | none recorded | - | 0 | Please **accept** my blessing that is brought to you, because God has dealt graciously with me, and because I have enough.” Thus he urged him, and he took it. |
| Exo 22:11 | accept | HVqq3ms | none recorded | - | 0 | an oath by the Lord shall be between them both to see whether or not he has put his hand to his neighbor’s property. The owner shall **accept** the oath, and he shall not make restitution. |
| Num 7:5 | accept | HVqv2ms | none recorded | - | 0 | “ **Accept** these from them, that they may be used in the service of the tent of meeting, and give them to the Levites, to each man according to his service.” |
| Num 35:31 | accept | HVqi2mp | none recorded | - | 0 | Moreover, you shall **accept** no ransom for the life of a murderer, who is guilty of death, but he shall be put to death. |
| Num 35:32 | accept | HVqi2mp | none recorded | - | 0 | And you shall **accept** no ransom for him who has fled to his city of refuge, that he may return to dwell in the land before the death of the high priest. |
| Deu 16:19 | accept | HVqi2ms | none recorded | - | 0 | You shall not pervert justice. You shall not show partiality, and you shall not **accept** a bribe, for a bribe blinds the eyes of the wise and subverts the cause of the righteous. |
| 1Sa 2:15 | accept | HVqi3ms | none recorded | - | 0 | Moreover, before the fat was burned, the priest’s servant would come and say to the man who was sacrificing, “ Give meat for the priest to roast, for he will not **accept** boiled meat from you but only raw.” |
| 1Sa 10:4 | accept | HVqq2ms | none recorded | - | 0 | And they will greet you and give you two loaves of bread, which you shall **accept** from their hand. |
| 2Ki 5:15 | accept | HVqv2ms | none recorded | - | 0 | Then he returned to the man of God, he and all his company, and he came and stood before him. And he said, “ Behold, I know that there is no God in all the earth but in Israel; so **accept** now a present from your servant.” |
| 2Ki 5:23 | accept | HVqv2ms | none recorded | - | 0 | And Naaman said, “Be pleased to **accept** two talents.” And he urged him and tied up two talents of silver in two bags, with two changes of clothing, and laid them on two of his servants. And they carried them before Gehazi. |
| 2Ki 5:26 | accept | HVqcc | none recorded | - | 0 | But he said to him, “Did not my heart go when the man turned from his chariot to meet you? Was it a time to **accept** money and garments, olive orchards and vineyards, sheep and oxen, male servants and female servants? |
| Pro 4:10 | accept | HVqv2ms | none recorded | - | 0 | Hear, my son, and **accept** my words, that the years of your life may be many. |
| Jer 7:28 | accept | HVqp3cp | none recorded | - | 0 | And you shall say to them, ‘ This is the nation that did not obey the voice of the Lord their God, and did not **accept** discipline; truth has perished; it is cut off from their lips. |
| Jer 25:28 | accept | HVqcc | none recorded | - | 0 | “And if they refuse to **accept** the cup from your hand to drink, then you shall say to them, ‘ Thus says the Lord of hosts: You must drink! |
| Hos 14:2 | accept | HVqv2ms | none recorded | - | 0 | Take with you words and return to the Lord; say to him, “ Take away all iniquity; **accept** what is good, and we will pay with bulls the vows of our lips. |
| Judg 13:23 | accepted | HVqp3ms | none recorded | - | 0 | But his wife said to him, “ If the Lord had meant to kill us, he would not have **accepted** a burnt offering and a grain offering at our hands, or shown us all these things, or now announced to us such things as these.” |
| Psa 6:9 | accepts | HVqi3ms | none recorded | - | 0 | The Lord has heard my plea; the Lord **accepts** my prayer. |
| Pro 17:23 | accepts | HVqi3ms | none recorded | - | 0 | The wicked **accepts** a bribe in secret to pervert the ways of justice. |
| Zep 3:2 | accepts | HVqp3fs | none recorded | - | 0 | She listens to no voice; she **accepts** no correction. She does not trust in the Lord; she does not draw near to her God. |
| Mal 2:13 | accepts | HVqcc | none recorded | - | 0 | And this second thing you do. You cover the Lord’s altar with tears, with weeping and groaning because he no longer regards the offering or **accepts** it with favor from your hand. |

### 3.5 H7521 רָצָה ra.tsah "to accept": 19 own occurrences in 19 verses

- **Meaning as stored:** Hebrew; native word רָצָה, transliteration ra.tsah; STEP gloss "to accept"; sense head "to accept" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7521):** to be pleased with, be favourable to, accept favourably.
- **Related terms (3):** H7522 ra.tson "acceptance"; H8656G tir.tsah "Tirzah"; H8656H tir.tsah "Tirzah".
- **Clusters (cluster_strong):** M39 Gift & Favor (None).
- **Counts, three measures as stored:** STEP token count 59; verses STEP attests 54; verse_lexical rows the parse found 56.

- **Carried by the member words:** accept (13), accepted (3), acceptable (1), accepted me (1), accepts (1).
- **Engagement of these occurrences:** none recorded 19.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 33:11 | accept | HVqi2ms | none recorded | - | 0 | Bless, O Lord, his substance, and **accept** the work of his hands; crush the loins of his adversaries, of those who hate him, that they rise not again.” |
| 2Sa 24:23 | accept | HVqi3ms | none recorded | - | 0 | All this, O king, Araunah gives to the king.” And Araunah said to the king, “May the Lord your God **accept** you.” |
| Psa 119:108 | accept | HVqv2ms | none recorded | - | 0 | **Accept** my freewill offerings of praise, O Lord, and teach me your rules. |
| Jer 14:10 | accept | HVqp3ms | none recorded | - | 0 | Thus says the Lord concerning this people: “They have loved to wander thus; they have not restrained their feet; therefore the Lord does not **accept** them; now he will remember their iniquity and punish their sins.” |
| Jer 14:12 | accept | HVqrmsc | none recorded | - | 0 | Though they fast, I will not hear their cry, and though they offer burnt offering and grain offering, I will not **accept** them. But I will consume them by the sword, by famine, and by pestilence.” |
| Eze 20:40 | accept | HVqi1cs | none recorded | - | 0 | “ For on my holy mountain, the mountain height of Israel, declares the Lord God, there all the house of Israel, all of them, shall serve me in the land. There I will **accept** them, and there I will require your contributions and the choicest of your gifts, with all your sacred offerings. |
| Eze 20:41 | accept | HVqi1cs | none recorded | - | 0 | As a pleasing aroma I will **accept** you, when I bring you out from the peoples and gather you out of the countries where you have been scattered. And I will manifest my holiness among you in the sight of the nations. |
| Eze 43:27 | accept | HVqq1cs | none recorded | - | 0 | And when they have completed these days, then from the eighth day onward the priests shall offer on the altar your burnt offerings and your peace offerings, and I will **accept** you, declares the Lord God.” |
| Hos 8:13 | accept | HVqp3ms | none recorded | - | 0 | As for my sacrificial offerings, they sacrifice meat and eat it, but the Lord does not **accept** them. Now he will remember their iniquity and punish their sins; they shall return to Egypt. |
| Amo 5:22 | accept | HVqi1cs | none recorded | - | 0 | Even though you offer me your burnt offerings and grain offerings, I will not **accept** them; and the peace offerings of your fattened animals, I will not look upon them. |
| Mal 1:8 | accept | HVqi3ms | none recorded | 17527 | 0 | When you offer blind animals in sacrifice, is that not evil? And when you offer those that are lame or sick, is that not evil? Present that to your governor; will he **accept** you or show you favor? says the Lord of hosts. |
| Mal 1:10 | accept | HVqi1cs | none recorded | 17585 | 0 | Oh that there were one among you who would shut the doors, that you might not kindle fire on my altar in vain! I have no pleasure in you, says the Lord of hosts, and I will not **accept** an offering from your hand. |
| Mal 1:13 | accept | HVqi1cs | none recorded | - | 0 | But you say, ‘ What a weariness this is,’ and you snort at it, says the Lord of hosts. You bring what has been taken by violence or is lame or sick, and this you bring as your offering! Shall I **accept** that from your hand? says the Lord. |
| Lev 22:27 | acceptable | HVNi3ms | none recorded | - | 0 | “When an ox or sheep or goat is born, it shall remain seven days with its mother, and from the eighth day on it shall be **acceptable** as a food offering to the Lord. |
| Lev 1:4 | accepted | HVNq3ms | none recorded | - | 0 | He shall lay his hand on the head of the burnt offering, and it shall be **accepted** for him to make atonement for him. |
| Lev 7:18 | accepted | HVNi3ms | none recorded | - | 0 | If any of the flesh of the sacrifice of his peace offering is eaten on the third day, he who offers it shall not be **accepted**, neither shall it be credited to him. It is tainted, and he who eats of it shall bear his iniquity. |
| Lev 22:25 | accepted | HVNi3mp | none recorded | - | 0 | neither shall you offer as the bread of your God any such animals gotten from a foreigner. Since there is a blemish in them, because of their mutilation, they will not be **accepted** for you.” |
| Gen 33:10 | accepted me | HVqw2ms | none recorded | - | 0 | Jacob said, “ No, please, if I have found favor in your sight, then accept my present from my hand. For I have seen your face, which is like seeing the face of God, and you have **accepted me**. |
| Job 33:26 | accepts | HVqw3ms | none recorded | - | 0 | then man prays to God, and he **accepts** him; he sees his face with a shout of joy, and he restores to man his righteousness. |

### 3.6 H7522 רָצוֹן ra.tson "acceptance": 12 own occurrences in 12 verses

- **Meaning as stored:** Hebrew; native word רָצוֹן, transliteration ra.tson; STEP gloss "acceptance"; sense head "acceptance" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7522):** pleasure, delight, favour, goodwill, acceptance, will.
- **Related terms (3):** H7521 ra.tsah "to accept"; H8656G tir.tsah "Tirzah"; H8656H tir.tsah "Tirzah".
- **Clusters (cluster_strong):** M18 Desire & Longing (None).
- **Counts, three measures as stored:** STEP token count 56; verses STEP attests 56; verse_lexical rows the parse found 56.

- **Carried by the member words:** accepted (7), acceptable (5).
- **Engagement of these occurrences:** none recorded 12.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 19:14 | acceptable | HNcmsa | none recorded | 18986 | 0 | Let the words of my mouth and the meditation of my heart be **acceptable** in your sight, O Lord, my rock and my redeemer. |
| Psa 69:13 | acceptable | HNcmsa | none recorded | - | 0 | But as for me, my prayer is to you, O Lord. At an **acceptable** time, O God, in the abundance of your steadfast love answer me in your saving faithfulness. |
| Pro 10:32 | acceptable | HNcmsa | none recorded | - | 0 | The lips of the righteous know what is **acceptable**, but the mouth of the wicked, what is perverse. |
| Isa 58:5 | acceptable | HNcmsa | none recorded | - | 0 | Is such the fast that I choose, a day for a person to humble himself? Is it to bow down his head like a reed, and to spread sackcloth and ashes under him? Will you call this a fast, and a day **acceptable** to the Lord? |
| Jer 6:20 | acceptable | HNcmsa | none recorded | - | 0 | What use to me is frankincense that comes from Sheba, or sweet cane from a distant land? Your burnt offerings are not **acceptable**, nor your sacrifices pleasing to me. |
| Exo 28:38 | accepted | HNcmsa | none recorded | 17724 | 0 | It shall be on Aaron’s forehead, and Aaron shall bear any guilt from the holy things that the people of Israel consecrate as their holy gifts. It shall regularly be on his forehead, that they may be **accepted** before the Lord. |
| Lev 19:5 | accepted | HNcmsc | none recorded | 17724 | 0 | “When you offer a sacrifice of peace offerings to the Lord, you shall offer it so that you may be **accepted**. |
| Lev 22:19 | accepted | HNcmsc | none recorded | 17724 | 0 | if it is to be **accepted** for you it shall be a male without blemish, of the bulls or the sheep or the goats. |
| Lev 22:21 | accepted | HNcmsa | none recorded | 17724 | 0 | And when anyone offers a sacrifice of peace offerings to the Lord to fulfill a vow or as a freewill offering from the herd or from the flock, to be **accepted** it must be perfect; there shall be no blemish in it. |
| Lev 22:29 | accepted | HNcmsc | none recorded | 17724 | 0 | And when you sacrifice a sacrifice of thanksgiving to the Lord, you shall sacrifice it so that you may be **accepted**. |
| Lev 23:11 | accepted | HNcmsc | none recorded | 17724 | 0 | and he shall wave the sheaf before the Lord, so that you may be **accepted**. On the day after the Sabbath the priest shall wave it. |
| Isa 56:7 | accepted | HNcmsa | none recorded | - | 0 | these I will bring to my holy mountain, and make them joyful in my house of prayer; their burnt offerings and their sacrifices will be **accepted** on my altar; for my house shall be called a house of prayer for all peoples.” |

### 3.7 G0533 ἀπαρνέομαι aparneomai "to deny": 11 own occurrences in 11 verses

- **Meaning as stored:** Greek; native word ἀπαρνέομαι, transliteration aparneomai; STEP gloss "to deny"; sense head "to deny" (the code is its own lemma).
- **Related terms (2):** G0575 apo "away from"; G0720 arneomai "to deny".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 14; verses STEP attests 11; verse_lexical rows the parse found 11.

- **Carried by the member words:** deny (10), denied (1).
- **Engagement of these occurrences:** none recorded 11.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 12:9 | denied | V-FPI-3S | none recorded | - | 0 | but the one who denies me before men will be **denied** before the angels of God. |
| Mat 16:24 | deny | V-ADM-3S | none recorded | - | 0 | Then Jesus told his disciples, “ If anyone would come after me, let him **deny** himself and take up his cross and follow me. |
| Mat 26:34 | deny | V-FDI-2S | none recorded | - | 0 | Jesus said to him, “ Truly, I tell you, this very night, before the rooster crows, you will **deny** me three times.” |
| Mat 26:35 | deny | V-FDI-1S | none recorded | - | 0 | Peter said to him, “Even if I must die with you, I will not **deny** you!” And all the disciples said the same. |
| Mat 26:75 | deny | V-FDI-2S | none recorded | - | 0 | And Peter remembered the saying of Jesus, “ Before the rooster crows, you will **deny** me three times.” And he went out and wept bitterly. |
| Mar 8:34 | deny | V-ADM-3S | none recorded | - | 0 | And calling the crowd to him with his disciples, he said to them, “If anyone would come after me, let him **deny** himself and take up his cross and follow me. |
| Mar 14:30 | deny | V-FDI-2S | none recorded | - | 0 | And Jesus said to him, “ Truly, I tell you, this very night, before the rooster crows twice, you will **deny** me three times.” |
| Mar 14:31 | deny | V-FDI-1S | none recorded | - | 0 | But he said emphatically, “ If I must die with you, I will not **deny** you.” And they all said the same. |
| Mar 14:72 | deny | V-FDI-2S | none recorded | - | 0 | And immediately the rooster crowed a second time. And Peter remembered how Jesus had said to him, “ Before the rooster crows twice, you will **deny** me three times.” And he broke down and wept. |
| Luk 22:34 | deny | V-AMS-2S | none recorded | - | 0 | Jesus said, “I tell you, Peter, the rooster will not crow this day, until you **deny** three times that you know me.” |
| Luk 22:61 | deny | V-FDI-2S | none recorded | - | 0 | And the Lord turned and looked at Peter. And Peter remembered the saying of the Lord, how he had said to him, “ Before the rooster crows today, you will **deny** me three times.” |

### 3.8 H2186A זָנַח za.nach "to reject": 9 own occurrences in 9 verses

- **Meaning as stored:** Hebrew; native word זָנַח, transliteration za.nach; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2186):** to cast off, reject, spurn.
- **Related terms (3):** H2182G za.no.ach "Zanoah"; H2182H za.no.ach "Zanoah"; H2186B za.nach "to stink".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 19; verse_lexical rows the parse found 19.

- **Carried by the member words:** rejected (6), cast off (2), reject (1).
- **Engagement of these occurrences:** none recorded 9.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 89:38 | cast off | HVqp2ms | none recorded | - | 0 | But now you have **cast off** and rejected; you are full of wrath against your anointed. |
| Lam 3:31 | cast off | HVqi3ms | none recorded | 13773, 14726 | 0 | For the Lord will not **cast off** forever, |
| Psa 44:23 | reject | HVqj2ms | none recorded | - | 0 | Awake! Why are you sleeping, O Lord? Rouse yourself! Do not **reject** us forever! |
| Psa 43:2 | rejected | HVqp2ms | none recorded | - | 0 | For you are the God in whom I take refuge; why have you **rejected** me? Why do I go about mourning because of the oppression of the enemy? |
| Psa 44:9 | rejected | HVqp2ms | none recorded | 15195 | 0 | But you have **rejected** us and disgraced us and have not gone out with our armies. |
| Psa 60:1 | rejected | HVqp2ms | none recorded | - | 0 | To the choirmaster: according to Shushan Eduth. A Miktam of David; for instruction; when he strove with Aram-naharaim and with Aram-zobah, and when Joab on his return struck down twelve thousand of Edom in the Valley of Salt. O God, you have **rejected** us, broken our defenses; you have been angry; oh, restore us. |
| Psa 60:10 | rejected | HVqp2ms | none recorded | - | 0 | Have you not **rejected** us, O God? You do not go forth, O God, with our armies. |
| Psa 108:11 | rejected | HVqp2ms | none recorded | - | 0 | Have you not **rejected** us, O God? You do not go out, O God, with our armies. |
| Zec 10:6 | rejected | HVqp1cs | none recorded | - | 0 | “I will strengthen the house of Judah, and I will save the house of Joseph. I will bring them back because I have compassion on them, and they shall be as though I had not **rejected** them, for I am the Lord their God and I will answer them. |

### 3.9 G0114 ἀθετέω atheteō "to reject": 8 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word ἀθετέω, transliteration atheteō; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Related terms (2):** G0115 athetēsis "nullification"; G5087 tithēmi "to place".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 72; verses STEP attests 12; verse_lexical rows the parse found 16.

- **Carried by the member words:** rejects (5), reject (1), rejected (1), rejecting (1).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jude 8 | reject | V-PAI-3P | none recorded | 16551, 17161, 19124 | 0 | Yet in like manner these people also, relying on their dreams, defile the flesh, **reject** authority, and blaspheme the glorious ones. |
| Luk 7:30 | rejected | V-AAI-3P | none recorded | 19419 | 0 | but the Pharisees and the lawyers **rejected** the purpose of God for themselves, not having been baptized by him.) |
| Mar 7:9 | rejecting | V-PAI-2P | none recorded | - | 0 | And he said to them, “You have a fine way of **rejecting** the commandment of God in order to establish your tradition! |
| Luk 10:16 | rejects | V-PAP-NSM | none recorded | - | 0 | “The one who hears you hears me, and the one who **rejects** you rejects me, and the one who rejects me rejects him who sent me.” |
| Luk 10:16 | rejects | V-PAI-3S | none recorded | - | 0 | “The one who hears you hears me, and the one who **rejects** you rejects me, and the one who rejects me rejects him who sent me.” |
| Luk 10:16 | rejects | V-PAP-NSM | none recorded | - | 0 | “The one who hears you hears me, and the one who **rejects** you rejects me, and the one who rejects me rejects him who sent me.” |
| Luk 10:16 | rejects | V-PAI-3S | none recorded | - | 0 | “The one who hears you hears me, and the one who **rejects** you rejects me, and the one who rejects me rejects him who sent me.” |
| Joh 12:48 | rejects | V-PAP-NSM | none recorded | - | 0 | The one who **rejects** me and does not receive my words has a judge; the word that I have spoken will judge him on the last day. |

### 3.10 G0593 ἀποδοκιμάζω apodokimazō "to reject": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word ἀποδοκιμάζω, transliteration apodokimazō; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Related terms (2):** G0575 apo "away from"; G1381 dokimazō "to test".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 18; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** rejected (8).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 21:42 | rejected | V-AAI-3P | none recorded | - | 0 | Jesus said to them, “Have you never read in the Scriptures: “‘The stone that the builders **rejected** has become the cornerstone; this was the Lord’s doing, and it is marvelous in our eyes ’? |
| Mar 8:31 | rejected | V-APN | none recorded | - | 0 | And he began to teach them that the Son of Man must suffer many things and be **rejected** by the elders and the chief priests and the scribes and be killed, and after three days rise again. |
| Mar 12:10 | rejected | V-AAI-3P | none recorded | - | 0 | Have you not read this Scripture: “‘The stone that the builders **rejected** has become the cornerstone; |
| Luk 9:22 | rejected | V-APN | none recorded | - | 0 | saying, “The Son of Man must suffer many things and be **rejected** by the elders and chief priests and scribes, and be killed, and on the third day be raised.” |
| Luk 17:25 | rejected | V-APN | none recorded | - | 0 | But first he must suffer many things and be **rejected** by this generation. |
| Luk 20:17 | rejected | V-AAI-3P | none recorded | - | 0 | But he looked directly at them and said, “ What then is this that is written: “‘ The stone that the builders **rejected** has become the cornerstone ’? |
| Heb 12:17 | rejected | V-API-3S | none recorded | - | 0 | For you know that afterward, when he desired to inherit the blessing, he was **rejected**, for he found no chance to repent, though he sought it with tears. |
| 1Pe 2:7 | rejected | V-AAI-3P | none recorded | - | 0 | So the honor is for you who believe, but for those who do not believe, “The stone that the builders **rejected** has become the cornerstone,” |

### 3.11 G1209 δέχομαι dechomai "to receive": 6 own occurrences in 6 verses

- **Meaning as stored:** Greek; native word δέχομαι, transliteration dechomai; STEP gloss "to receive"; sense head "to receive" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 109; verses STEP attests 47; verse_lexical rows the parse found 58.

- **Carried by the member words:** accept (3), accepted (3).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 11:14 | accept | V-ADN | none recorded | - | 0 | and if you are willing to **accept** it, he is Elijah who is to come. |
| 1Cor 2:14 | accept | V-PNI-3S | none recorded | - | 0 | The natural person does not **accept** the things of the Spirit of God, for they are folly to him, and he is not able to understand them because they are spiritually discerned. |
| 2Cor 11:16 | accept | V-AMM-2P | none recorded | - | 0 | I repeat, let no one think me foolish. But even if you do, **accept** me as a fool, so that I too may boast a little. |
| 2Cor 8:17 | accepted | V-ADI-3S | none recorded | - | 0 | For he not only **accepted** our appeal, but being himself very earnest he is going to you of his own accord. |
| 2Cor 11:4 | accepted | V-ADI-2P | none recorded | - | 0 | For if someone comes and proclaims another Jesus than the one we proclaimed, or if you receive a different spirit from the one you received, or if you accept a different gospel from the one you **accepted**, you put up with it readily enough. |
| 1Th 2:13 | accepted | V-ADI-2P | none recorded | - | 0 | And we also thank God constantly for this, that when you received the word of God, which you heard from us, you **accepted** it not as the word of men but as what it really is, the word of God, which is at work in you believers. |

### 3.12 G0436 ἀνθίστημι anthistēmi "to oppose": 5 own occurrences in 4 verses

- **Meaning as stored:** Greek; native word ἀνθίστημι, transliteration anthistēmi; STEP gloss "to oppose"; sense head "to oppose" (the code is its own lemma).
- **Related terms (2):** G0473 anti "for"; G2476 histēmi "to stand".
- **Clusters (cluster_strong):** M06 Malice & Enmity (None).
- **Counts, three measures as stored:** STEP token count 56; verses STEP attests 0; verse_lexical rows the parse found 14.

- **Carried by the member words:** opposed (4), oppose (1).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ti 3:8 | oppose | V-PMI-3P | none recorded | - | 0 | Just as Jannes and Jambres opposed Moses, so these men also **oppose** the truth, men corrupted in mind and disqualified regarding the faith. |
| Act 13:8 | opposed | V-IMI-3S | none recorded | - | 0 | But Elymas the magician ( for that is the meaning of his name ) **opposed** them, seeking to turn the proconsul away from the faith. |
| Gal 2:11 | opposed | V-2AAI-1S | none recorded | - | 0 | But when Cephas came to Antioch, I **opposed** him to his face, because he stood condemned. |
| 2Ti 3:8 | opposed | V-2AAI-3P | none recorded | - | 0 | Just as Jannes and Jambres **opposed** Moses, so these men also oppose the truth, men corrupted in mind and disqualified regarding the faith. |
| 2Ti 4:15 | opposed | V-2AAI-3S | none recorded | - | 0 | Beware of him yourself, for he strongly **opposed** our message. |

### 3.13 G2144 εὐπρόσδεκτος euprosdektos "acceptable": 4 own occurrences in 4 verses

- **Meaning as stored:** Greek; native word εὐπρόσδεκτος, transliteration euprosdektos; STEP gloss "acceptable"; sense head "acceptable" (the code is its own lemma).
- **Related terms (2):** G2095 eu "well/well done!"; G4327 prosdechomai "to wait for/welcome".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 0; verse_lexical rows the parse found 5.

- **Carried by the member words:** acceptable (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 15:16 | acceptable | A-NSF | none recorded | - | 0 | to be a minister of Christ Jesus to the Gentiles in the priestly service of the gospel of God, so that the offering of the Gentiles may be **acceptable**, sanctified by the Holy Spirit. |
| Rom 15:31 | acceptable | A-NSF | none recorded | - | 0 | that I may be delivered from the unbelievers in Judea, and that my service for Jerusalem may be **acceptable** to the saints, |
| 2Cor 8:12 | acceptable | A-NSF | none recorded | - | 0 | For if the readiness is there, it is **acceptable** according to what a person has, not according to what he does not have. |
| 1Pe 2:5 | acceptable | A-APF | none recorded | - | 0 | you yourselves like living stones are being built up as a spiritual house, to be a holy priesthood, to offer spiritual sacrifices **acceptable** to God through Jesus Christ. |

### 3.14 H3584 כָּחַשׁ ka.chash "to deceive": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word כָּחַשׁ, transliteration ka.chash; STEP gloss "to deceive"; sense head "to deceive" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3584):** to deceive, lie, fail, grow lean, be disappointing, be untrue, be insu ... (cut; the whole text is in the workbook).
- **Related terms (2):** H3585 ka.chash "lie"; H3586 ke.chash "deceptive".
- **Clusters (cluster_strong):** M14 Deceit & Falsehood (high).
- **Counts, three measures as stored:** STEP token count 22; verses STEP attests 22; verse_lexical rows the parse found 22.

- **Carried by the member words:** deny (2), denied (1), denying (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 18:15 | denied | HVpw3fs | none recorded | 12657 | 0 | But Sarah **denied** it, saying, “I did not laugh,” for she was afraid. He said, “ No, but you did laugh.” |
| Job 8:18 | deny | HVpq3ms | none recorded | - | 0 | If he is destroyed from his place, then it will **deny** him, saying, ‘I have never seen you.’ |
| Pro 30:9 | deny | HVpq1cs | none recorded | - | 0 | lest I be full and **deny** you and say, “ Who is the Lord?” or lest I be poor and steal and profane the name of my God. |
| Isa 59:13 | denying | HVpcc | none recorded | - | 0 | transgressing, and **denying** the Lord, and turning back from following our God, speaking oppression and revolt, conceiving and uttering from the heart lying words. |

### 3.15 H3986 מָאֵן ma.en "refusing": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word מָאֵן, transliteration ma.en; STEP gloss "refusing"; sense head "refusing" (the code is its own lemma).
- **Related terms (2):** H3985 ma.en "to refuse"; H3987 me.en "refusing".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** refuse (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 8:2 | refuse | HVprmsa | none recorded | - | 0 | But if you **refuse** to let them go, behold, I will plague all your country with frogs. |
| Exo 9:2 | refuse | HVprmsa | none recorded | - | 0 | For if you **refuse** to let them go and still hold them, |
| Exo 10:4 | refuse | HVprmsa | none recorded | - | 0 | For if you **refuse** to let my people go, behold, tomorrow I will bring locusts into your country, |
| Jer 38:21 | refuse | HVprmsa | none recorded | - | 0 | But if you **refuse** to surrender, this is the vision which the Lord has shown to me: |

### 3.16 H5106 נוּא nu "to forbid": 4 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word נוּא, transliteration nu; STEP gloss "to forbid"; sense head "to forbid" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5106):** to hinder, hold back, forbid, disallow, restrain, frustrate.
- **Related terms (1):** H8569 te.nu.ah "opposition".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** opposes (2), opposed (1), refuse (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 30:5 | opposed | HVhp3ms | none recorded | - | 0 | But if her father opposes her on the day that he hears of it, no vow of hers, no pledge by which she has bound herself shall stand. And the Lord will forgive her, because her father **opposed** her. |
| Num 30:5 | opposes | HVhp3ms | none recorded | - | 0 | But if her father **opposes** her on the day that he hears of it, no vow of hers, no pledge by which she has bound herself shall stand. And the Lord will forgive her, because her father opposed her. |
| Num 30:8 | opposes | HVhi3ms | none recorded | - | 0 | But if, on the day that her husband comes to hear of it, he **opposes** her, then he makes void her vow that was on her, and the thoughtless utterance of her lips by which she bound herself. And the Lord will forgive her. |
| Psa 141:5 | refuse | HVhi3ms | none recorded | - | 0 | Let a righteous man strike me—it is a kindness; let him rebuke me—it is oil for my head; let my head not **refuse** it. Yet my prayer is continually against their evil deeds. |

### 3.17 H7725L שׁוּב shuv "to return: refuse": 4 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word שׁוּב, transliteration shuv; STEP gloss "to return: refuse"; sense head "refuse/turn(face)".
- **Senses (first level of the meaning tree of the lemma H7725):** to return, turn back.
- **Related terms (30):** H3142 yu.shav che.sed "Jushab-hesed"; H3432 ya.shu.vi "Jashubite"; H3433 ya.shu.vi la.chem "Lehem"; H3434G ya.shov.am "Jashobeam"; H3434H ya.shov.am "Jashobeam"; H3437G ya.shuv "Jashub"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 0; verse_lexical rows the parse found 5.

- **Carried by the member words:** refuse (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ki 2:16 | refuse | HVhi2fs | none recorded | - | 0 | And now I have one request to make of you; do not **refuse** me.” She said to him, “ Speak.” |
| 1Ki 2:17 | refuse | HVhi3ms | none recorded | - | 0 | And he said, “ Please ask King Solomon — he will not **refuse** you —to give me Abishag the Shunammite as my wife.” |
| 1Ki 2:20 | refuse | HVhj2ms | none recorded | - | 0 | Then she said, “I have one small request to make of you; do not **refuse** me.” And the king said to her, “Make your request, my mother, for I will not refuse you.” |
| 1Ki 2:20 | refuse | HVhi1cs | none recorded | - | 0 | Then she said, “I have one small request to make of you; do not **refuse** me.” And the king said to her, “Make your request, my mother, for I will not refuse you.” |

### 3.18 G0498 ἀντιτάσσω antitassō "to resist": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word ἀντιτάσσω, transliteration antitassō; STEP gloss "to resist"; sense head "to resist" (the code is its own lemma).
- **Related terms (2):** G0473 anti "for"; G5021 tassō "to appoint".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** opposes (2), opposed (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 18:6 | opposed | V-PMP-GPM | none recorded | - | 0 | And when they **opposed** and reviled him, he shook out his garments and said to them, “ Your blood be on your own heads! I am innocent. From now on I will go to the Gentiles.” |
| Jam 4:6 | opposes | V-PMI-3S | none recorded | - | 0 | But he gives more grace. Therefore it says, “ God **opposes** the proud but gives grace to the humble.” |
| 1Pe 5:5 | opposes | V-PMI-3S | none recorded | - | 0 | Likewise, you who are younger, be subject to the elders. Clothe yourselves, all of you, with humility toward one another, for “ God **opposes** the proud but gives grace to the humble.” |

### 3.19 G0683 ἀπωθέω apōtheō "to reject": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word ἀπωθέω, transliteration apōtheō; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 75; verses STEP attests 6; verse_lexical rows the parse found 9.

- **Carried by the member words:** rejected (2), rejecting (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 11:1 | rejected | V-ADI-3S | none recorded | - | 0 | I ask, then, has God **rejected** his people? By no means! For I myself am an Israelite, a descendant of Abraham, a member of the tribe of Benjamin. |
| Rom 11:2 | rejected | V-ADI-3S | none recorded | - | 0 | God has not **rejected** his people whom he foreknew. Do you not know what the Scripture says of Elijah, how he appeals to God against Israel? |
| 1Ti 1:19 | rejecting | V-ADP-NPM | none recorded | 16345, 17159 | 0 | holding faith and a good conscience. By **rejecting** this, some have made shipwreck of their faith, |

### 3.20 G2101 εὐάρεστος euarestos "well-pleasing": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word εὐάρεστος, transliteration euarestos; STEP gloss "well-pleasing"; sense head "well-pleasing" (the code is its own lemma).
- **Related terms (4):** G0701 arestos "pleasing"; G2095 eu "well/well done!"; G2100 euaresteō "to please"; G2102 euarestōs "acceptably".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 0; verse_lexical rows the parse found 9.

- **Carried by the member words:** acceptable (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 12:1 | acceptable | A-ASF | none recorded | - | 0 | I appeal to you therefore, brothers, by the mercies of God, to present your bodies as a living sacrifice, holy and **acceptable** to God, which is your spiritual worship. |
| Rom 12:2 | acceptable | A-NSN | none recorded | - | 0 | Do not be conformed to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and **acceptable** and perfect. |
| Rom 14:18 | acceptable | A-NSM | none recorded | - | 0 | Whoever thus serves Christ is **acceptable** to God and approved by men. |

### 3.21 G3858 παραδέχομαι paradechomai "to welcome": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word παραδέχομαι, transliteration paradechomai; STEP gloss "to welcome"; sense head "to welcome" (the code is its own lemma).
- **Related terms (2):** G1209 dechomai "to receive"; G3844 para "from/with/beside".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 0; verse_lexical rows the parse found 5.

- **Carried by the member words:** accept (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 4:20 | accept | V-PNI-3P | none recorded | - | 0 | But those that were sown on the good soil are the ones who hear the word and **accept** it and bear fruit, thirtyfold and sixtyfold and a hundredfold.” |
| Act 16:21 | accept | V-PNN | none recorded | - | 0 | They advocate customs that are not lawful for us as Romans to **accept** or practice.” |
| Act 22:18 | accept | V-FNI-3P | none recorded | - | 0 | and saw him saying to me, ‘ Make haste and get out of Jerusalem quickly, because they will not **accept** your testimony about me.’ |

### 3.22 G3868 παραιτέομαι paraiteomai "to refuse/excuse": 3 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word παραιτέομαι, transliteration paraiteomai; STEP gloss "to refuse/excuse"; sense head "to refuse/excuse" (the code is its own lemma).
- **Related terms (3):** G0154 aiteō "to ask"; G0155 aitēma "request"; G3844 para "from/with/beside".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 16; verses STEP attests 10; verse_lexical rows the parse found 12.

- **Carried by the member words:** refuse (2), refused him (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ti 5:11 | refuse | V-PNM-2S | none recorded | - | 0 | But **refuse** to enroll younger widows, for when their passions draw them away from Christ, they desire to marry |
| Heb 12:25 | refuse | V-ADS-2P | none recorded | - | 0 | See that you do not **refuse** him who is speaking. For if they did not escape when they refused him who warned them on earth, much less will we escape if we reject him who warns from heaven. |
| Heb 12:25 | refused him | V-ADP-NPM | none recorded | - | 0 | See that you do not refuse him who is speaking. For if they did not escape when they **refused him** who warned them on earth, much less will we escape if we reject him who warns from heaven. |

### 3.23 H6901 קָבַל qa.val "to receive": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word קָבַל, transliteration qa.val; STEP gloss "to receive"; sense head "to receive" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H6901):** to take, receive, be before.
- **Related terms (3):** H6902 qab.bel "to receive"; H6904 qe.vol "battering-ram"; H6905H qa.val "before".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 16; verses STEP attests 12; verse_lexical rows the parse found 13.

- **Carried by the member words:** accept (2), accepted (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Est 4:4 | accept | HVpp3ms | none recorded | - | 0 | When Esther’s young women and her eunuchs came and told her, the queen was deeply distressed. She sent garments to clothe Mordecai, so that he might take off his sackcloth, but he would not **accept** them. |
| Pro 19:20 | accept | HVpv2ms | none recorded | - | 0 | Listen to advice and **accept** instruction, that you may gain wisdom in the future. |
| Est 9:23 | accepted | HVpq3ms | none recorded | - | 0 | So the Jews **accepted** what they had started to do, and what Mordecai had written to them. |

### 3.24 G0096 ἀδόκιμος adokimos "failing": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word ἀδόκιμος, transliteration adokimos; STEP gloss "failing"; sense head "failing" (the code is its own lemma).
- **Related terms (1):** G1384 dokimos "tested".
- **Clusters (cluster_strong):** M24 Faintness & Despair (high).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 8; verse_lexical rows the parse found 9.

- **Carried by the member words:** disqualified (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 9:27 | disqualified | A-NSM | none recorded | - | 0 | But I discipline my body and keep it under control, lest after preaching to others I myself should be **disqualified**. |
| 2Ti 3:8 | disqualified | A-NPM | none recorded | - | 0 | Just as Jannes and Jambres opposed Moses, so these men also oppose the truth, men corrupted in mind and **disqualified** regarding the faith. |

### 3.25 G0480 ἀντίκειμαι antikeimai "be an opponent": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word ἀντίκειμαι, transliteration antikeimai; STEP gloss "be an opponent"; sense head "be an opponent" (the code is its own lemma).
- **Related terms (2):** G0473 anti "for"; G2749 keimai "to lay/be appointed".
- **Clusters (cluster_strong):** M06 Malice & Enmity (medium).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 8; verse_lexical rows the parse found 8.

- **Carried by the member words:** opposed (1), opposes (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gal 5:17 | opposed | V-PNI-3S | none recorded | 16950 | 0 | For the desires of the flesh are against the Spirit, and the desires of the Spirit are against the flesh, for these are **opposed** to each other, to keep you from doing the things you want to do. |
| 2Th 2:4 | opposes | V-PNP-NSM | none recorded | 15168 | 0 | who **opposes** and exalts himself against every so-called god or object of worship, so that he takes his seat in the temple of God, proclaiming himself to be God. |

### 3.26 G0483 ἀντιλέγω antilegō "to dispute": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word ἀντιλέγω, transliteration antilegō; STEP gloss "to dispute"; sense head "to dispute" (the code is its own lemma).
- **Related terms (15):** G0471 anteipon "to contradict"; G0473 anti "for"; G0485 antilogia "dispute"; G0557 apelegmos "discredit"; G1246 diakatelenchomai "to refute"; G1256 dialegō "to dispute"; more in the workbook.
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 17; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** deny (1), opposes (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 20:27 | deny | V-PAP-NPM | none recorded | - | 0 | There came to him some Sadducees, those who **deny** that there is a resurrection, |
| Joh 19:12 | opposes | V-PAI-3S | none recorded | - | 0 | From then on Pilate sought to release him, but the Jews cried out, “ If you release this man, you are not Caesar’s friend. Everyone who makes himself a king **opposes** Caesar.” |

### 3.27 G0654 ἀποστρέφω apostrefō "to turn away": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word ἀποστρέφω, transliteration apostrefō; STEP gloss "to turn away"; sense head "to turn away" (the code is its own lemma).
- **Related terms (2):** G0575 apo "away from"; G4762 strefō "to turn".
- **Clusters (cluster_strong):** M11 Turning & Repentance (heuristic).
- **Counts, three measures as stored:** STEP token count 423; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** refuse (1), reject him (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 5:42 | refuse | V-2APS-2S | none recorded | - | 0 | Give to the one who begs from you, and do not **refuse** the one who would borrow from you. |
| Heb 12:25 | reject him | V-PPP-NPM | none recorded | - | 0 | See that you do not refuse him who is speaking. For if they did not escape when they refused him who warned them on earth, much less will we escape if we **reject him** who warns from heaven. |

### 3.28 G1184 δεκτός dektos "acceptable": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word δεκτός, transliteration dektos; STEP gloss "acceptable"; sense head "acceptable" (the code is its own lemma).
- **Related terms (1):** G1209 dechomai "to receive".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 36; verses STEP attests 0; verse_lexical rows the parse found 4.

- **Carried by the member words:** acceptable (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 4:24 | acceptable | A-NSM | none recorded | - | 0 | And he said, “ Truly, I say to you, no prophet is **acceptable** in his hometown. |
| Phili 4:18 | acceptable | A-ASF | none recorded | - | 0 | I have received full payment, and more. I am well supplied, having received from Epaphroditus the gifts you sent, a fragrant offering, a sacrifice **acceptable** and pleasing to God. |

### 3.29 G4059 περιτέμνω peritemnō "to circumcise": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word περιτέμνω, transliteration peritemnō; STEP gloss "to circumcise"; sense head "to circumcise" (the code is its own lemma).
- **Related terms (4):** G0564 aperitmētos "uncircumcised"; G4012 peri "about"; G4061 peritomē "circumcision"; G5114 tomōteros "sharper".
- **Clusters (cluster_strong):** M32 Covenant (medium).
- **Counts, three measures as stored:** STEP token count 52; verses STEP attests 15; verse_lexical rows the parse found 17.

- **Carried by the member words:** accept circumcision (1), accepts circumcision (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gal 5:2 | accept circumcision | V-PPS-2P | none recorded | - | 0 | Look: I, Paul, say to you that if you **accept circumcision**, Christ will be of no advantage to you. |
| Gal 5:3 | accepts circumcision | V-PPP-DSM | none recorded | - | 0 | I testify again to every man who **accepts circumcision** that he is obligated to keep the whole law. |

### 3.30 G4327 προσδέχομαι prosdechomai "to wait for/welcome": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word προσδέχομαι, transliteration prosdechomai; STEP gloss "to wait for/welcome"; sense head "to wait for/welcome" (the code is its own lemma).
- **Related terms (2):** G1209 dechomai "to receive"; G4314 pros "to/with".
- **Clusters (cluster_strong):** M68 Hope & Waiting (medium).
- **Counts, three measures as stored:** STEP token count 48; verses STEP attests 0; verse_lexical rows the parse found 14.

- **Carried by the member words:** accept (1), accepted (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 11:35 | accept | V-ADP-NPM | none recorded | - | 0 | Women received back their dead by resurrection. Some were tortured, refusing to **accept** release, so that they might rise again to a better life. |
| Heb 10:34 | accepted | V-ADI-2P | none recorded | - | 0 | For you had compassion on those in prison, and you joyfully **accepted** the plundering of your property, since you knew that you yourselves had a better possession and an abiding one. |

### 3.31 H1115 בִּלְתִּי bil.ti "lest": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word בִּלְתִּי, transliteration bil.ti; STEP gloss "lest"; sense head "lest" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1115):** not, except; not; except (after preceding negation); except (after an implied or expressed negation); so as not, in order not; an account of not, because...not.
- **Related terms (10):** H1077 bal "not"; H1086 ba.lah "to become old"; H1087 ba.leh "old"; H1094 be.lo "old"; H1097 be.li "without"; H1100G be.liy.ya.al "Belial"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 112; verses STEP attests 0; verse_lexical rows the parse found 112.

- **Carried by the member words:** refusing (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 19:15 | refusing | HNcbsa | none recorded | - | 0 | “ Thus says the Lord of hosts, the God of Israel, behold, I am bringing upon this city and upon all its towns all the disaster that I have pronounced against it, because they have stiffened their neck, **refusing** to hear my words.” |
| Dan 9:11 | refusing | HNcbsa | none recorded | - | 0 | All Israel has transgressed your law and turned aside, **refusing** to obey your voice. And the curse and oath that are written in the Law of Moses the servant of God have been poured out upon us, because we have sinned against him. |

### 3.32 H2310 חָדֵל cha.del "rejected/fleeting": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word חָדֵל, transliteration cha.del; STEP gloss "rejected/fleeting"; sense head "rejected/fleeting" (the code is its own lemma).
- **Related terms (3):** H2308 cha.dal "to cease"; H2309 che.del "world"; H2311 chad.la "Hadlai".
- **Clusters (cluster_strong):** T2 Supplementary (medium).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** refuse (1), rejected (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 3:27 | refuse | HAamsa | none recorded | - | 0 | But when I speak with you, I will open your mouth, and you shall say to them, ‘ Thus says the Lord God.’ He who will hear, let him hear; and he who will **refuse** to hear, let him refuse, for they are a rebellious house. |
| Isa 53:3 | rejected | HAamsc | none recorded | - | 0 | He was despised and **rejected** by men, a man of sorrows, and acquainted with grief; and as one from whom men hide their faces he was despised, and we esteemed him not. |

### 3.33 H4513 מָנַע ma.na "to withhold": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word מָנַע, transliteration ma.na; STEP gloss "to withhold"; sense head "to withhold" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4513):** to withhold, hold back, keep back, refrain, deny, keep restrain, hinde ... (cut; the whole text is in the workbook).
- **Related terms (9):** H3234 yim.na "Imna"; H4519G me.nash.sheh "Manasseh"; H4519H me.nash.sheh "Manasseh"; H4519I me.nash.sheh "Manasseh"; H4519J me.nash.sheh "Manasseh"; H4519K me.nash.sheh "Moses"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 29; verses STEP attests 29; verse_lexical rows the parse found 29.

- **Carried by the member words:** deny (1), refuse (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 30:7 | deny | HVqj2ms | none recorded | - | 0 | Two things I ask of you; **deny** them not to me before I die: |
| 1Ki 20:7 | refuse | HVqp1cs | none recorded | - | 0 | Then the king of Israel called all the elders of the land and said, “ Mark, now, and see how this man is seeking trouble, for he sent to me for my wives and my children, and for my silver and my gold, and I did not **refuse** him.” |

### 3.34 H5006 נָאַץ na.ats "to spurn": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word נָאַץ, transliteration na.ats; STEP gloss "to spurn"; sense head "to spurn" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5006):** to spurn, contemn, despise, abhor.
- **Related terms (4):** H5007A ne.a.tsah "contempt"; H5007B ne.a.tsah "contempt"; H5132A na.tsah "to flee"; H5132B na.tsats "to bud".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 25; verses STEP attests 24; verse_lexical rows the parse found 25.

- **Carried by the member words:** renounce (1), renounces (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 10:13 | renounce | HVpp3ms | none recorded | - | 0 | Why does the wicked **renounce** God and say in his heart, “You will not call to account”? |
| Psa 10:3 | renounces | HVpp3ms | none recorded | 17038, 17071, 17158 | 0 | For the wicked boasts of the desires of his soul, and the one greedy for gain curses and **renounces** the Lord. |

### 3.35 H5203 נָטַשׁ na.tash "to leave": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word נָטַשׁ, transliteration na.tash; STEP gloss "to leave"; sense head "to leave" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5203):** to leave, permit, forsake, cast off or away, reject, suffer, join, spr ... (cut; the whole text is in the workbook).
- **Related terms (1):** H5189 ne.ti.shah "tendril".
- **Clusters (cluster_strong):** M59 Release & Reconciliation (heuristic).
- **Counts, three measures as stored:** STEP token count 40; verses STEP attests 39; verse_lexical rows the parse found 40.

- **Carried by the member words:** rejected (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 2:6 | rejected | HVqp2ms | none recorded | - | 0 | For you have **rejected** your people, the house of Jacob, because they are full of things from the east and of fortune-tellers like the Philistines, and they strike hands with the children of foreigners. |
| Jer 15:6 | rejected | HVqp2fs | none recorded | - | 0 | You have **rejected** me, declares the Lord; you keep going backward, so I have stretched out my hand against you and destroyed you— I am weary of relenting. |

### 3.36 H5375Q נָשָׂא na.sa "to lift: kindness": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word נָשָׂא, transliteration na.sa; STEP gloss "to lift: kindness"; sense head "kindness/honour/favour/lift(head/face)".
- **Senses (first level of the meaning tree of the lemma H5375):** to lift, bear up, carry, take.
- **Related terms (30):** H4853A mas.sa "burden"; H4853B mas.sa "oracle"; H4856 mas.so "respect"; H4858 mas.sa.ah "smoke"; H4864 mas.et "tribute"; H5375G na.sa "to lift: raise"; more in the workbook.
- **Clusters (cluster_strong):** M50 Grace & Mercy (heuristic).
- **Counts, three measures as stored:** STEP token count 41; verses STEP attests 40; verse_lexical rows the parse found 41.

- **Carried by the member words:** accept (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 32:20 | accept | HVqi3ms | none recorded | - | 0 | and you shall say, ‘ Moreover, your servant Jacob is behind us.’” For he thought, “I may appease him with the present that goes ahead of me, and afterward I shall see his face. Perhaps he will **accept** me.” |
| Job 42:8 | accept | HVqi1cs | none recorded | 14606 | 0 | Now therefore take seven bulls and seven rams and go to my servant Job and offer up a burnt offering for yourselves. And my servant Job shall pray for you, for I will **accept** his prayer not to deal with you according to your folly. For you have not spoken of me what is right, as my servant Job has.” |

### 3.37 G0142 αἴρω airō "to take up": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word αἴρω, transliteration airō; STEP gloss "to take up"; sense head "to take up" (the code is its own lemma).
- **Related terms (20):** G0138 haireō "to choose"; G0522 apairō "to take away"; G0685 ara "curse"; G0686 ara "therefore"; G0700 areskō "to please"; G0706 arithmos "number"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 370; verses STEP attests 96; verse_lexical rows the parse found 100.

- **Carried by the member words:** denied (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 8:33 | denied | V-API-3S | none recorded | - | 0 | In his humiliation justice was **denied** him. Who can describe his generation? For his life is taken away from the earth.” |

### 3.38 G0430 ἀνέχω anechō "to endure": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀνέχω, transliteration anechō; STEP gloss "to endure"; sense head "to endure" (the code is its own lemma).
- **Related terms (3):** G0303 ana "each"; G0463 anochē "tolerance"; G2192 echō "to have/be".
- **Clusters (cluster_strong):** M34 Patience & Perseverance (heuristic).
- **Counts, three measures as stored:** STEP token count 25; verses STEP attests 14; verse_lexical rows the parse found 15.

- **Carried by the member words:** accept (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 18:14 | accept | V-2AMI-1S | none recorded | - | 0 | But when Paul was about to open his mouth, Gallio said to the Jews, “ If it were a matter of wrongdoing or vicious crime, O Jews, I would have reason to **accept** your complaint. |

### 3.39 G0550 ἀπεῖπον apeipon "to renounce": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀπεῖπον, transliteration apeipon; STEP gloss "to renounce"; sense head "to renounce" (the code is its own lemma).
- **Related terms (2):** G0575 apo "away from"; G2036 eipon "to say: said".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** renounced (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 4:2 | renounced | V-2AMI-1P | none recorded | - | 0 | But we have **renounced** disgraceful, underhanded ways. We refuse to practice cunning or to tamper with God’s word, but by the open statement of the truth we would commend ourselves to everyone’s conscience in the sight of God. |

### 3.40 G0579 ἀπόβλητος apoblētos "rejected": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀπόβλητος, transliteration apoblētos; STEP gloss "rejected"; sense head "rejected" (the code is its own lemma).
- **Related terms (7):** G0575 apo "away from"; G0577 apoballō "to throw away"; G0906G ballō "to throw: throw"; G0906H ballō "to throw: put"; G0906I ballō "to throw: sow"; G0906J ballō "to throw: pour"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (medium).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** rejected (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ti 4:4 | rejected | A-NSN | none recorded | - | 0 | For everything created by God is good, and nothing is to be **rejected** if it is received with thanksgiving, |

### 3.41 G0580 ἀποβολή apobolē "deprivation": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀποβολή, transliteration apobolē; STEP gloss "deprivation"; sense head "deprivation" (the code is its own lemma).
- **Related terms (3):** G0575 apo "away from"; G0577 apoballō "to throw away"; G1000 bolē "throwing".
- **Clusters (cluster_strong):** M59 Release & Reconciliation (heuristic).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** rejection (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 11:15 | rejection | N-NSF | none recorded | - | 0 | For if their **rejection** means the reconciliation of the world, what will their acceptance mean but life from the dead? |

### 3.42 G0588 ἀποδέχομαι apodechomai "to receive": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀποδέχομαι, transliteration apodechomai; STEP gloss "to receive"; sense head "to receive" (the code is its own lemma).
- **Related terms (4):** G0575 apo "away from"; G0587 apodektos "pleasing"; G0594 apodochē "acceptance"; G1209 dechomai "to receive".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** accept (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 24:3 | accept | V-PNI-1P | none recorded | - | 0 | in every way and everywhere we **accept** this with all gratitude. |

### 3.43 G0657 ἀποτάσσω apotassō "to leave": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀποτάσσω, transliteration apotassō; STEP gloss "to leave"; sense head "to leave" (the code is its own lemma).
- **Related terms (2):** G0575 apo "away from"; G5021 tassō "to appoint".
- **Clusters (cluster_strong):** M59 Release & Reconciliation (heuristic).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** renounce (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 14:33 | renounce | V-PMI-3S | none recorded | - | 0 | So therefore, any one of you who does not **renounce** all that he has cannot be my disciple. |

### 3.44 G0659 ἀποτίθημι apotithēmi "to put aside": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀποτίθημι, transliteration apotithēmi; STEP gloss "to put aside"; sense head "to put aside" (the code is its own lemma).
- **Related terms (4):** G0575 apo "away from"; G0595 apothesis "removal"; G0596 apothēkē "storehouse"; G5087 tithēmi "to place".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 23; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** cast off (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 13:12 | cast off | V-2AMS-1P | none recorded | - | 0 | The night is far gone; the day is at hand. So then let us **cast off** the works of darkness and put on the armor of light. |

### 3.45 G0873 ἀφορίζω aforizō "to separate": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀφορίζω, transliteration aforizō; STEP gloss "to separate"; sense head "to separate" (the code is its own lemma).
- **Related terms (3):** G0575 apo "away from"; G3724 horizō "to determine"; G4309 proorizō "to predestine".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 98; verses STEP attests 9; verse_lexical rows the parse found 10.

- **Carried by the member words:** exclude (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 6:22 | exclude | V-AAS-3P | none recorded | - | 0 | “ Blessed are you when people hate you and when they **exclude** you and revile you and spurn your name as evil, on account of the Son of Man! |

### 3.46 G1576 ἐκκλείω ekkleiō "to exclude": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐκκλείω, transliteration ekkleiō; STEP gloss "to exclude"; sense head "to exclude" (the code is its own lemma).
- **Related terms (9):** G0608 apokleiō "to shut"; G1537 ek "out from"; G2623 katakleiō "to lock up"; G2807 kleis "key"; G2808 kleiō "to shut"; G2809 klemma "theft"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 2; verse_lexical rows the parse found 3.

- **Carried by the member words:** excluded (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 3:27 | excluded | V-API-3S | none recorded | - | 0 | Then what becomes of our boasting? It is **excluded**. By what kind of law? By a law of works? No, but by the law of faith. |

### 3.47 G1727 ἐναντίος enantios "hostile": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐναντίος, transliteration enantios; STEP gloss "hostile"; sense head "hostile" (the code is its own lemma).
- **Related terms (5):** G0561 apenanti "opposite"; G1725 enanti "before"; G1726 enantion "in front of"; G2713 katenanti "before"; G2714 katenōpion "before".
- **Clusters (cluster_strong):** M06 Malice & Enmity (high).
- **Counts, three measures as stored:** STEP token count 141; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** oppose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Th 2:15 | oppose | A-GPM | none recorded | - | 0 | who killed both the Lord Jesus and the prophets, and drove us out, and displease God and **oppose** all mankind |

### 3.48 G1848 ἐξουθενέω exoutheneō "to reject": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐξουθενέω, transliteration exoutheneō; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Related terms (1):** G1847 exoudenoō "be rejected".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 21; verses STEP attests 11; verse_lexical rows the parse found 11.

- **Carried by the member words:** rejected (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 4:11 | rejected | V-APP-NSM | none recorded | - | 0 | This Jesus is the stone that was **rejected** by you, the builders, which has become the cornerstone. |

### 3.49 G2102 εὐαρέστως euarestōs "acceptably": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word εὐαρέστως, transliteration euarestōs; STEP gloss "acceptably"; sense head "acceptably" (the code is its own lemma).
- **Related terms (1):** G2101 euarestos "well-pleasing".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** acceptable (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 12:28 | acceptable | ADV | none recorded | - | 0 | Therefore let us be grateful for receiving a kingdom that cannot be shaken, and thus let us offer to God **acceptable** worship, with reverence and awe, |

### 3.50 G2603 καταβραβεύω katabrabeuō "to disqualify": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word καταβραβεύω, transliteration katabrabeuō; STEP gloss "to disqualify"; sense head "to disqualify" (the code is its own lemma).
- **Related terms (2):** G1018 brabeuō "to rule"; G2596 kata "according to".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** disqualify (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Col 2:18 | disqualify | V-PAM-3S | none recorded | - | 0 | Let no one **disqualify** you, insisting on asceticism and worship of angels, going on in detail about visions, puffed up without reason by his sensuous mind, |

### 3.51 G3361 μή mē "not": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word μή, transliteration mē; STEP gloss "not"; sense head "not" (the code is its own lemma).
- **Related terms (2):** G3361 mē "not"; G3364 ou mē "never".
- **Clusters (cluster_strong):** T5 Negator (None).
- **Counts, three measures as stored:** STEP token count 3474; verses STEP attests 0; verse_lexical rows the parse found 871.

- **Carried by the member words:** refuse (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 4:2 | refuse | PRT-N | none recorded | - | 0 | But we have renounced disgraceful, underhanded ways. We **refuse** to practice cunning or to tamper with God’s word, but by the open statement of the truth we would commend ourselves to everyone’s conscience in the sight of God. |

### 3.52 G3756 οὐ ou "no": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word οὐ, transliteration ou; STEP gloss "no"; sense head "no" (the code is its own lemma).
- **Related terms (2):** G3756 ou "no"; G3765 ouketi "not any more".
- **Clusters (cluster_strong):** T5 Negator (None).
- **Counts, three measures as stored:** STEP token count 6775; verses STEP attests 0; verse_lexical rows the parse found 1578.

- **Carried by the member words:** refuse (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rev 11:9 | refuse | PRT-N | none recorded | - | 0 | For three and a half days some from the peoples and tribes and languages and nations will gaze at their dead bodies and **refuse** to let them be placed in a tomb, |

### 3.53 G4014 περιαιρέω periaireō "to take away": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word περιαιρέω, transliteration periaireō; STEP gloss "to take away"; sense head "to take away" (the code is its own lemma).
- **Related terms (2):** G0138 haireō "to choose"; G4012 peri "about".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 60; verses STEP attests 0; verse_lexical rows the parse found 4.

- **Carried by the member words:** cast off (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 27:40 | cast off | V-2AAP-NPM | none recorded | - | 0 | So they **cast off** the anchors and left them in the sea, at the same time loosening the ropes that tied the rudders. Then hoisting the foresail to the wind they made for the beach. |

### 3.54 G4065 περιφρονέω perifroneō "to despise": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word περιφρονέω, transliteration perifroneō; STEP gloss "to despise"; sense head "to despise" (the code is its own lemma).
- **Related terms (2):** G4012 peri "about"; G5426 froneō "to reason".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** disregard (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Tit 2:15 | disregard | V-PAM-3S | none recorded | - | 0 | Declare these things; exhort and rebuke with all authority. Let no one **disregard** you. |

### 3.55 G4067 περίψημα peripsēma "scum": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word περίψημα, transliteration peripsēma; STEP gloss "scum"; sense head "scum" (the code is its own lemma).
- **Related terms (1):** G4012 peri "about".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** refuse (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 4:13 | refuse | N-NSN | none recorded | - | 0 | when slandered, we entreat. We have become, and are still, like the scum of the world, the **refuse** of all things. |

### 3.56 G4183 πολύς polus "much": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word πολύς, transliteration polus; STEP gloss "much"; sense head "much" (the code is its own lemma).
- **Related terms (6):** G3827 pampolus "great"; G4118 pleistos "most"; G4119 pleiōn pleion "greater"; G4178 pollakis "often"; G4179 pollaplasiōn "many times more"; G4182 polupoikilos "manifold".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 902; verses STEP attests 367; verse_lexical rows the parse found 405.

- **Carried by the member words:** more acceptable (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 11:4 | more acceptable | A-ASF-C | none recorded | - | 0 | By faith Abel offered to God a **more acceptable** sacrifice than Cain, through which he was commended as righteous, God commending him by accepting his gifts. And through his faith, though he died, he still speaks. |

### 3.57 H0977 בָּחַר ba.char "to choose": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word בָּחַר, transliteration ba.char; STEP gloss "to choose"; sense head "to choose" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0977):** to choose, elect, decide for.
- **Related terms (9):** H0970 ba.chur "youth"; H0972 ba.chir "chosen"; H0978 ba.cha.ru.mi "Baharumite"; H0979 be.chu.rim "youth"; H0980 ba.chu.rim "Bahurim"; H2984 yiv.char "Ibhar"; more in the workbook.
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 174; verses STEP attests 163; verse_lexical rows the parse found 171.

- **Carried by the member words:** more acceptable (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 21:3 | more acceptable | HVNrmsa | none recorded | 12492, 19735 | 0 | To do righteousness and justice is **more acceptable** to the Lord than sacrifice. |

### 3.58 H1351 גָּאַל ga.al "to defile": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word גָּאַל, transliteration ga.al; STEP gloss "to defile"; sense head "to defile" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1351):** to defile, pollute, desecrate.
- **Related terms (5):** H1350A ga.al "to redeem: redeem"; H1350B ge.u.lay "redemption"; H1350H ga.al "to redeem: avenge"; H1350I ga.al "to redeem: relative"; H1352 go.el "defilement".
- **Clusters (cluster_strong):** M10c Defilement (medium).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 9; verse_lexical rows the parse found 11.

- **Carried by the member words:** excluded (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ezr 2:62 | excluded | HVPw3mp | none recorded | - | 0 | These sought their registration among those enrolled in the genealogies, but they were not found there, and so they were **excluded** from the priesthood as unclean. |

### 3.59 H1624 גָּרָה ga.rah "to stir up": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word גָּרָה, transliteration ga.rah; STEP gloss "to stir up"; sense head "to stir up" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1624):** to cause strife, stir up, contend, meddle, strive, be stirred up.
- **Related terms (2):** H1627 ga.ron "throat"; H8409 tig.rah "strife".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 17; verses STEP attests 13; verse_lexical rows the parse found 14.

- **Carried by the member words:** opposed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 50:24 | opposed | HVtp2fs | none recorded | - | 0 | I set a snare for you and you were taken, O Babylon, and you did not know it; you were found and caught, because you **opposed** the Lord. |

### 3.60 H2308 חָדַל cha.dal "to cease": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָדַל, transliteration cha.dal; STEP gloss "to cease"; sense head "to cease" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2308):** to stop, cease, desist, forego, cease to be, leave undone, forbear.
- **Related terms (3):** H2309 che.del "world"; H2310 cha.del "rejected/fleeting"; H2311 chad.la "Hadlai".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 61; verses STEP attests 56; verse_lexical rows the parse found 58.

- **Carried by the member words:** refuse (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 3:27 | refuse | HVqi3ms | none recorded | - | 0 | But when I speak with you, I will open your mouth, and you shall say to them, ‘ Thus says the Lord God.’ He who will hear, let him hear; and he who will **refuse** to hear, let him refuse, for they are a rebellious house. |

### 3.61 H3582 כָּחַד ka.chad "to hide": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word כָּחַד, transliteration ka.chad; STEP gloss "to hide"; sense head "to hide" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3582):** to hide, conceal, cut off, cut down, make desolate, kick.
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** M20 Doubt & Discouragement (high).
- **Counts, three measures as stored:** STEP token count 32; verses STEP attests 30; verse_lexical rows the parse found 32.

- **Carried by the member words:** denied (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 6:10 | denied | HVpp1cs | none recorded | 18888, 19226, 19231 | 0 | This would be my comfort; I would even exult in pain unsparing, for I have not **denied** the words of the Holy One. |

### 3.62 H3925H לָמַד la.mad "to learn: learn": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word לָמַד, transliteration la.mad; STEP gloss "to learn: learn"; sense head "learn".
- **Senses (first level of the meaning tree of the lemma H3925):** to learn. teach, exercise in.
- **Related terms (7):** H3925G la.mad "to learn: teach"; H3927 le.mu.el "Lemuel"; H3928 lim.mud "disciple"; H3929G le.mekh "Lamech"; H3929H le.mekh "Lamech"; H4451 mal.med "oxgoad"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 23; verses STEP attests 22; verse_lexical rows the parse found 23.

- **Carried by the member words:** accept (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 29:24 | accept | HVqi3mp | none recorded | - | 0 | And those who go astray in spirit will come to understanding, and those who murmur will **accept** instruction.” |

### 3.63 H3987 מֵאֵן me.en "refusing": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מֵאֵן, transliteration me.en; STEP gloss "refusing"; sense head "refusing" (the code is its own lemma).
- **Related terms (2):** H3985 ma.en "to refuse"; H3986 ma.en "refusing".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** refuse (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 13:10 | refuse | HVprmpa | none recorded | - | 0 | This evil people, who **refuse** to hear my words, who stubbornly follow their own heart and have gone after other gods to serve them and worship them, shall be like this loincloth, which is good for nothing. |

### 3.64 H5010 נָאַר na.ar "to disown": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נָאַר, transliteration na.ar; STEP gloss "to disown"; sense head "to disown" (the code is its own lemma).
- **Related terms (1):** H5011 nov "Nob".
- **Clusters (cluster_strong):** M06 Malice & Enmity (None).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 0; verse_lexical rows the parse found 2.

- **Carried by the member words:** renounced (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 89:39 | renounced | HVpp2ms | none recorded | - | 0 | You have **renounced** the covenant with your servant; you have defiled his crown in the dust. |

### 3.65 H5186 נָטָה na.tah "to stretch": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נָטָה, transliteration na.tah; STEP gloss "to stretch"; sense head "to stretch" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5186):** to stretch out, extend, spread out, pitch, turn, pervert, incline, ben ... (cut; the whole text is in the workbook).
- **Related terms (10):** H3194 yut.tah "Juttah"; H4294G mat.teh "tribe: rod"; H4294H mat.teh "tribe"; H4294I mat.teh "tribe: arrow"; H4294J mat.teh "tribe: stick"; H4294K mat.teh "tribe: supply"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 222; verses STEP attests 207; verse_lexical rows the parse found 214.

- **Carried by the member words:** deny (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lam 3:35 | deny | HVhcc | none recorded | - | 0 | to **deny** a man justice in the presence of the Most High, |

### 3.66 H5234A נָכַר na.khar "to recognize": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נָכַר, transliteration na.khar; STEP gloss "to recognize"; sense head "to recognize" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5234):** to recognise, acknowledge, know, respect, discern, regard.
- **Related terms (3):** H1971 hak.ka.rah "look"; H4378 mak.kar "acquaintance"; H5234B na.khar "to alienate".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 45; verses STEP attests 41; verse_lexical rows the parse found 42.

- **Carried by the member words:** accept (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 21:29 | accept | HVpi2mp | none recorded | - | 0 | Have you not asked those who travel the roads, and do you not **accept** their testimony |

### 3.67 H5375H נָשָׂא na.sa "to lift: bear": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נָשָׂא, transliteration na.sa; STEP gloss "to lift: bear"; sense head "look/lift(eyes)".
- **Senses (first level of the meaning tree of the lemma H5375):** to lift, bear up, carry, take.
- **Related terms (30):** H4853A mas.sa "burden"; H4853B mas.sa "oracle"; H4856 mas.so "respect"; H4858 mas.sa.ah "smoke"; H4864 mas.et "tribute"; H5375G na.sa "to lift: raise"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 221; verses STEP attests 208; verse_lexical rows the parse found 221.

- **Carried by the member words:** accept (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 5:19 | accept | HVqcc | none recorded | - | 0 | Everyone also to whom God has given wealth and possessions and power to enjoy them, and to **accept** his lot and rejoice in his toil — this is the gift of God. |

### 3.68 H5375P נָשָׂא na.sa "to lift: vow": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נָשָׂא, transliteration na.sa; STEP gloss "to lift: vow"; sense head "vow/swear/bless/lift(hand)".
- **Senses (first level of the meaning tree of the lemma H5375):** to lift, bear up, carry, take.
- **Related terms (30):** H4853A mas.sa "burden"; H4853B mas.sa "oracle"; H4856 mas.so "respect"; H4858 mas.sa.ah "smoke"; H4864 mas.et "tribute"; H5375G na.sa "to lift: raise"; more in the workbook.
- **Clusters (cluster_strong):** M70 Lifting & Bearing (heuristic).
- **Counts, three measures as stored:** STEP token count 26; verses STEP attests 22; verse_lexical rows the parse found 26.

- **Carried by the member words:** accepted (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 42:9 | accepted | HVqw3ms | none recorded | - | 0 | So Eliphaz the Temanite and Bildad the Shuhite and Zophar the Naamathite went and did what the Lord had told them, and the Lord **accepted** Job’s prayer. |

### 3.69 H5478 סוּחָה su.chah "offal": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word סוּחָה, transliteration su.chah; STEP gloss "offal"; sense head "offal" (the code is its own lemma).
- **Related terms (2):** H5477 su.ach "Suah"; H5479 so.tay "Sotai".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** refuse (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 5:25 | refuse | HNcfsa | none recorded | - | 0 | Therefore the anger of the Lord was kindled against his people, and he stretched out his hand against them and struck them, and the mountains quaked; and their corpses were as **refuse** in the midst of the streets. For all this his anger has not turned away, and his hand is stretched out still. |

### 3.70 H5493I סוּר sur "to turn aside: turn aside": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word סוּר, transliteration sur; STEP gloss "to turn aside: turn aside"; sense head "turn aside/deflect".
- **Senses (first level of the meaning tree of the lemma H5493):** to turn aside, depart.
- **Related terms (6):** H3249 ya.sur "departed"; H5493G sur "to turn aside: remove"; H5493H sur "to turn aside: depart"; H5494 sur "degenerate"; H5495 sur "Sur"; H5627 sa.rah "revolt".
- **Clusters (cluster_strong):** M11 Turning & Repentance (heuristic).
- **Counts, three measures as stored:** STEP token count 84; verses STEP attests 81; verse_lexical rows the parse found 84.

- **Carried by the member words:** rejected (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 66:20 | rejected | HVhp3ms | none recorded | - | 0 | Blessed be God, because he has not **rejected** my prayer or removed his steadfast love from me! |

### 3.71 H5541A סָלָה sa.lah "to reject": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word סָלָה, transliteration sa.lah; STEP gloss "to reject"; sense head "to reject" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5541):** to make light of, toss aside.
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** M30 Rebellion & Stubbornness (heuristic).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** rejected (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lam 1:15 | rejected | HVpp3ms | none recorded | - | 0 | “The Lord **rejected** all my mighty men in my midst; he summoned an assembly against me to crush my young men; the Lord has trodden as in a winepress the virgin daughter of Judah. |

### 3.72 H5674A עָבַר a.var "to pass": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָבַר, transliteration a.var; STEP gloss "to pass"; sense head "to pass" (the code is its own lemma).
- **Related terms (24):** H4569A ma.a.var "ford"; H4569B ma.a.va.rah "ford"; H5668 a.vur "for the sake of"; H5669 a.vur "produce"; H5674B a.var "be angry"; H5674C a.var "to pass: bring"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 513; verses STEP attests 441; verse_lexical rows the parse found 498.

- **Carried by the member words:** disregarded (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 40:27 | disregarded | HVqi3ms | none recorded | - | 0 | Why do you say, O Jacob, and speak, O Israel, “My way is hidden from the Lord, and my right is **disregarded** by my God ”? |

### 3.73 H5800H עָזַב a.zav "to leave: neglect": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָזַב, transliteration a.zav; STEP gloss "to leave: neglect"; sense head "to leave: neglect" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5800):** to leave, loose, forsake.
- **Related terms (8):** H5800A a.zav "to leave: forsake"; H5800B a.zav "to restore"; H5800C a.zav "to leave: release"; H5800G a.zav "Forsaken"; H5801 iz.za.von "ware"; H5805 a.zu.vah "desolation"; more in the workbook.
- **Clusters (cluster_strong):** M59 Release & Reconciliation (heuristic).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 7; verse_lexical rows the parse found 7.

- **Carried by the member words:** rejects (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 10:17 | rejects | HVqrmsc | none recorded | - | 0 | Whoever heeds instruction is on the path to life, but he who **rejects** reproof leads others astray. |

### 3.74 H7306 רִיחַ ri.ach "to smell": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רִיחַ, transliteration ri.ach; STEP gloss "to smell"; sense head "to smell" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7306):** (Hiphil) to smell, scent, perceive odour, accept.
- **Related terms (6):** H7304 ra.vach "be wide"; H7307G ru.ach "spirit"; H7307H ru.ach "spirit: breath"; H7307I ru.ach "spirit: side"; H7307J ru.ach "spirit: temper"; H7381 re.ach "aroma".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 11; verse_lexical rows the parse found 11.

- **Carried by the member words:** accept (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 26:19 | accept | HVhj3ms | none recorded | - | 0 | Now therefore let my lord the king hear the words of his servant. If it is the Lord who has stirred you up against me, may he **accept** an offering, but if it is men, may they be cursed before the Lord, for they have driven me out this day that I should have no share in the heritage of the Lord, saying, ‘ Go, serve other gods.’ |

### 3.75 H7613 שְׂאֵת se.et "elevation": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שְׂאֵת, transliteration se.et; STEP gloss "elevation"; sense head "elevation" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7613):** elevation, exaltation, dignity, swelling, uprising.
- **Related terms (29):** H4853A mas.sa "burden"; H4853B mas.sa "oracle"; H4856 mas.so "respect"; H4858 mas.sa.ah "smoke"; H4864 mas.et "tribute"; H5375G na.sa "to lift: raise"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 14; verses STEP attests 13; verse_lexical rows the parse found 14.

- **Carried by the member words:** accepted (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 4:7 | accepted | HNcfsa | none recorded | - | 0 | If you do well, will you not be **accepted**? And if you do not do well, sin is crouching at the door. Its desire is for you, and you must rule over it.” |

### 3.76 H7843 שָׁחַת sha.chat "to ruin": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁחַת, transliteration sha.chat; STEP gloss "to ruin"; sense head "to ruin" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7843):** to destroy, corrupt, go to ruin, decay.
- **Related terms (9):** H0516 al tash.chet "Do Not Destroy"; H4889 mash.chit "destruction"; H4892 mash.chet "destruction"; H4893A mish.chat "mutilation"; H4893B ma.she.chat "corruption"; H7844 she.chat "to corrupt"; more in the workbook.
- **Clusters (cluster_strong):** M55 Destruction & Ruin (heuristic).
- **Counts, three measures as stored:** STEP token count 146; verses STEP attests 135; verse_lexical rows the parse found 146.

- **Carried by the member words:** cast off (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Amo 1:11 | cast off | HVpq3ms | none recorded | 13584, 14181 | 0 | Thus says the Lord: “For three transgressions of Edom, and for four, I will not revoke the punishment, because he pursued his brother with the sword and **cast off** all pity, and his anger tore perpetually, and he kept his wrath forever. |

### 3.77 H7854 שָׂטָן sa.tan "Satan": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׂטָן, transliteration sa.tan; STEP gloss "Satan"; sense head "Satan" (the code is its own lemma).
- **Related terms (7):** G0954 beelzeboul "Beelzebul"; G0955 belial "Belial"; G4566 satan "Satan"; G4567 satanas "Satan"; H1100G be.liy.ya.al "Belial"; H1100H be.liy.ya.al "Belial: destruction"; more in the workbook.
- **Clusters (cluster_strong):** M85 Other Beings (high).
- **Counts, three measures as stored:** STEP token count 27; verses STEP attests 23; verse_lexical rows the parse found 27.

- **Carried by the member words:** oppose (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 22:32 | oppose | HNcmsa | none recorded | - | 0 | And the angel of the Lord said to him, “ Why have you struck your donkey these three times? Behold, I have come out to **oppose** you because your way is perverse before me. |

### 3.78 H8232 שְׁפַר she.phar "to acceptable": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שְׁפַר, transliteration she.phar; STEP gloss "to acceptable"; sense head "to acceptable" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8232):** to be fair, be seemly, seem good, seem pleasing.
- **Related terms (3):** H8209 shap.pir "fair"; H8231 sha.phar "to polish"; H8238 she.phar.par "dawn".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** acceptable (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 4:27 | acceptable | AVqi3ms | none recorded | - | 0 | Therefore, O king, let my counsel be **acceptable** to you: break off your sins by practicing righteousness, and your iniquities by showing mercy to the oppressed, that there may perhaps be a lengthening of your prosperity.” |

### 3.79 Occurrences where the member surface is shared with another code's unit (63)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| Luk 2:34 | opposed | G0483 ἀντιλέγω antilegō "to dispute" | opposed | content_part | 2 | none recorded | - | 0 | And Simeon blessed them and said to Mary his mother, “ Behold, this child is appointed for the fall and rising of many in Israel, and for a sign that is **opposed** |
| 1Pe 2:4 | rejected | G0593 ἀποδοκιμάζω apodokimazō "to reject" | rejected | content_part | 2 | none recorded | 19475, 19727, 19781, 19946, 19947, 20296 | 0 | As you come to him, a living stone **rejected** by men but in the sight of God chosen and precious, |
| Act 18:15 | refuse | G1014 βούλομαι boulomai "to plan" | refuse | content_part | 2 | none recorded | 12521, 20185 | 0 | But since it is a matter of questions about words and names and your own law, see to it yourselves. I **refuse** to be a judge of these things.” |
| Luk 2:34 | opposed | G1161 δέ de "then" | opposed | content_part | 2 | none recorded | - | 0 | And Simeon blessed them and said to Mary his mother, “ Behold, this child is appointed for the fall and rising of many in Israel, and for a sign that is **opposed** |
| Jude 8 | reject | G1161 δέ de "then" | reject | content_part | 2 | none recorded | - | 0 | Yet in like manner these people also, relying on their dreams, defile the flesh, **reject** authority, and blaspheme the glorious ones. |
| 2Th 2:10 | refused | G1209 δέχομαι dechomai "to receive" | refused | content_part | 2 | none recorded | - | 0 | and with all wicked deception for those who are perishing, because they **refused** to love the truth and so be saved. |
| Mat 2:18 | refused | G2309 θέλω thelō "to will/desire" | refused | content_part | 2 | none recorded | 14196 | 0 | “A voice was heard in Ramah, weeping and loud lamentation, Rachel weeping for her children; she **refused** to be comforted, because they are no more.” |
| Mat 18:30 | refused | G2309 θέλω thelō "to will/desire" | refused | content_part | 2 | none recorded | - | 0 | He **refused** and went and put him in prison until he should pay the debt. |
| Luk 15:28 | refused | G2309 θέλω thelō "to will/desire" | refused | content_part | 2 | none recorded | 13044, 13672, 17861 | 0 | But he was angry and **refused** to go in. His father came out and entreated him, |
| Luk 18:4 | refused | G2309 θέλω thelō "to will/desire" | refused | content_part | 2 | none recorded | - | 0 | For a while he **refused**, but afterward he said to himself, ‘ Though I neither fear God nor respect man, |
| Joh 5:40 | refuse | G2309 θέλω thelō "to will/desire" | refuse | content_part | 2 | none recorded | 17937 | 0 | yet you **refuse** to come to me that you may have life. |
| Act 7:39 | refused | G2309 θέλω thelō "to will/desire" | refused | content_part | 2 | none recorded | 16379 | 0 | Our fathers **refused** to obey him, but thrust him aside, and in their hearts they turned to Egypt, |
| Mat 2:18 | refused | G2532 καί kai "and" | refused | content_part | 2 | none recorded | - | 0 | “A voice was heard in Ramah, weeping and loud lamentation, Rachel weeping for her children; she **refused** to be comforted, because they are no more.” |
| Act 24:15 | accept | G2532 καί kai "and" | accept | content_part | 2 | none recorded | - | 0 | having a hope in God, which these men themselves **accept**, that there will be a resurrection of both the just and the unjust. |
| 1Pe 2:4 | rejected | G3303 μέν men "on the other hand" | rejected | content_part | 2 | none recorded | - | 0 | As you come to him, a living stone **rejected** by men but in the sight of God chosen and precious, |
| Mat 18:30 | refused | G3756 οὐ ou "no" | refused | content_part | 2 | none recorded | - | 0 | He **refused** and went and put him in prison until he should pay the debt. |
| Luk 15:28 | refused | G3756 οὐ ou "no" | refused | content_part | 2 | none recorded | - | 0 | But he was angry and **refused** to go in. His father came out and entreated him, |
| Luk 18:4 | refused | G3756 οὐ ou "no" | refused | content_part | 2 | none recorded | - | 0 | For a while he **refused**, but afterward he said to himself, ‘ Though I neither fear God nor respect man, |
| Joh 5:40 | refuse | G3756 οὐ ou "no" | refuse | content_part | 2 | none recorded | - | 0 | yet you **refuse** to come to me that you may have life. |
| Act 7:39 | refused | G3756 οὐ ou "no" | refused | content_part | 2 | none recorded | - | 0 | Our fathers **refused** to obey him, but thrust him aside, and in their hearts they turned to Egypt, |
| Act 18:15 | refuse | G3756 οὐ ou "no" | refuse | content_part | 2 | none recorded | - | 0 | But since it is a matter of questions about words and names and your own law, see to it yourselves. I **refuse** to be a judge of these things.” |
| 2Th 2:10 | refused | G3756 οὐ ou "no" | refused | content_part | 2 | none recorded | - | 0 | and with all wicked deception for those who are perishing, because they **refused** to love the truth and so be saved. |
| Act 24:15 | accept | G4327 προσδέχομαι prosdechomai "to wait for/welcome" | accept | content_part | 2 | none recorded | - | 0 | having a hope in God, which these men themselves **accept**, that there will be a resurrection of both the just and the unjust. |
| Pro 6:35 | refuse | H0014 אָבָה a.vah "be willing" | refuse | content_part | 3 | none recorded | 12501, 20157 | 0 | He will accept no compensation; he will **refuse** though you multiply gifts. |
| Eze 2:5 | refuse | H0518A אִם im "if" | refuse | content_part | 3 | none recorded | - | 0 | And whether they hear or **refuse** to hear ( for they are a rebellious house ) they will know that a prophet has been among them. |
| Eze 2:7 | refuse | H0518A אִם im "if" | refuse | content_part | 3 | none recorded | - | 0 | And you shall speak my words to them, whether they hear or **refuse** to hear, for they are a rebellious house. |
| Eze 3:11 | refuse | H0518A אִם im "if" | refuse | content_part | 3 | none recorded | - | 0 | And go to the exiles, to your people, and speak to them and say to them, ‘ Thus says the Lord God,’ whether they hear or **refuse** to hear.” |
| Lev 1:3 | accepted | H0853 אֵת et "[Obj.]" | accepted | content_part | 5 | none recorded | - | 0 | “If his offering is a burnt offering from the herd, he shall offer a male without blemish. He shall bring it to the entrance of the tent of meeting, that he may be **accepted** before the Lord. |
| 1Sa 8:7 | rejected | H0853 אֵת et "[Obj.]" | rejected | content_part | 3 | none recorded | - | 0 | And the Lord said to Samuel, “ Obey the voice of the people in all that they say to you, for they have not **rejected** you, but they have rejected me from being king over them. |
| 1Sa 8:7 | rejected | H0853 אֵת et "[Obj.]" | rejected | content_part | 3 | none recorded | - | 0 | And the Lord said to Samuel, “ Obey the voice of the people in all that they say to you, for they have not **rejected** you, but they have rejected me from being king over them. |
| Zep 3:7 | accept | H0853 אֵת et "[Obj.]" | accept | content_part | 3 | none recorded | - | 0 | I said, ‘ Surely you will fear me; you will **accept** correction. Then your dwelling would not be cut off according to all that I have appointed against you.’ But all the more they were eager to make all their deeds corrupt. |
| 2Ch 26:21 | excluded | H1504 גָּזַר ga.zar "to cut" | excluded | content_part | 2 | none recorded | - | 0 | And King Uzziah was a leper to the day of his death, and being a leper lived in a separate house, for he was **excluded** from the house of the Lord. And Jotham his son was over the king’s household, governing the people of the land. |
| Lev 19:7 | accepted | H1931 הוּא hu "he/she/it" | accepted | content_part | 2 | none recorded | - | 0 | If it is eaten at all on the third day, it is tainted; it will not be **accepted**, |
| Jer 3:3 | refuse | H1961 הָיָה ha.yah "to be" | refuse | content_part | 4 | none recorded | - | 0 | Therefore the showers have been withheld, and the spring rain has not come; yet you have the forehead of a whore; you **refuse** to be ashamed. |
| Eze 2:5 | refuse | H2308 חָדַל cha.dal "to cease" | refuse | content_part | 3 | none recorded | - | 0 | And whether they hear or **refuse** to hear ( for they are a rebellious house ) they will know that a prophet has been among them. |
| Eze 2:7 | refuse | H2308 חָדַל cha.dal "to cease" | refuse | content_part | 3 | none recorded | - | 0 | And you shall speak my words to them, whether they hear or **refuse** to hear, for they are a rebellious house. |
| Eze 3:11 | refuse | H2308 חָדַל cha.dal "to cease" | refuse | content_part | 3 | none recorded | - | 0 | And go to the exiles, to your people, and speak to them and say to them, ‘ Thus says the Lord God,’ whether they hear or **refuse** to hear.” |
| Lev 22:20 | acceptable | H3588A כִּי ki "for" | acceptable | content_part | 4 | none recorded | - | 0 | You shall not offer anything that has a blemish, for it will not be **acceptable** for you. |
| Num 11:20 | rejected | H3588A כִּי ki "for" | rejected | content_part | 2 | none recorded | - | 0 | but a whole month, until it comes out at your nostrils and becomes loathsome to you, because you have **rejected** the Lord who is among you and have wept before him, saying, “ Why did we come out of Egypt?”’” |
| Isa 8:6 | refused | H3588A כִּי ki "for" | refused | content_part | 2 | none recorded | - | 0 | “ Because this people has **refused** the waters of Shiloah that flow gently, and rejoice over Rezin and the son of Remaliah, |
| Isa 54:6 | cast off | H3588A כִּי ki "for" | cast off | content_part | 2 | none recorded | - | 0 | For the Lord has called you like a wife deserted and grieved in spirit, like a wife of youth when she is **cast off**, says your God. |
| Lev 22:20 | acceptable | H3808 לֹא lo "not" | acceptable | content_part | 4 | none recorded | - | 0 | You shall not offer anything that has a blemish, for it will not be **acceptable** for you. |
| Lev 22:23 | accepted | H3808 לֹא lo "not" | accepted | content_part | 2 | none recorded | - | 0 | You may present a bull or a lamb that has a part too long or too short for a freewill offering, but for a vow offering it cannot be **accepted**. |
| Pro 6:35 | refuse | H3808 לֹא lo "not" | refuse | content_part | 3 | none recorded | - | 0 | He will accept no compensation; he will **refuse** though you multiply gifts. |
| Zep 3:7 | accept | H3947H לָקַח la.qach "to take: recieve" | accept | content_part | 3 | none recorded | - | 0 | I said, ‘ Surely you will fear me; you will **accept** correction. Then your dwelling would not be cut off according to all that I have appointed against you.’ But all the more they were eager to make all their deeds corrupt. |
| Num 11:20 | rejected | H3988A מָאַס ma.as "to reject" | rejected | content_part | 2 | none recorded | - | 0 | but a whole month, until it comes out at your nostrils and becomes loathsome to you, because you have **rejected** the Lord who is among you and have wept before him, saying, “ Why did we come out of Egypt?”’” |
| 1Sa 8:7 | rejected | H3988A מָאַס ma.as "to reject" | rejected | content_part | 3 | none recorded | - | 0 | And the Lord said to Samuel, “ Obey the voice of the people in all that they say to you, for they have not **rejected** you, but they have rejected me from being king over them. |
| 1Sa 8:7 | rejected | H3988A מָאַס ma.as "to reject" | rejected | content_part | 3 | none recorded | - | 0 | And the Lord said to Samuel, “ Obey the voice of the people in all that they say to you, for they have not **rejected** you, but they have rejected me from being king over them. |
| Isa 8:6 | refused | H3988A מָאַס ma.as "to reject" | refused | content_part | 2 | none recorded | 19652, 19836, 19839 | 0 | “ Because this people has **refused** the waters of Shiloah that flow gently, and rejoice over Rezin and the son of Remaliah, |
| Isa 54:6 | cast off | H3988A מָאַס ma.as "to reject" | cast off | content_part | 2 | none recorded | 17164 | 0 | For the Lord has called you like a wife deserted and grieved in spirit, like a wife of youth when she is **cast off**, says your God. |
| Amo 2:4 | rejected | H3988A מָאַס ma.as "to reject" | rejected | content_part | 3 | none recorded | - | 0 | Thus says the Lord: “For three transgressions of Judah, and for four, I will not revoke the punishment, because they have **rejected** the law of the Lord, and have not kept his statutes, but their lies have led them astray, those after which their fathers walked. |
| Pro 6:35 | accept | H5375Q נָשָׂא na.sa "to lift: kindness" | accept | content_part | 2 | none recorded | 14187, 17760, 20157 | 0 | He will **accept** no compensation; he will refuse though you multiply gifts. |
| Eze 22:26 | disregarded | H5869A עַ֫יִן a.yin "eye" | disregarded | content_part | 3 | none recorded | - | 0 | Her priests have done violence to my law and have profaned my holy things. They have made no distinction between the holy and the common, neither have they taught the difference between the unclean and the clean, and they have **disregarded** my Sabbaths, so that I am profaned among them. |
| Ezr 10:15 | opposed | H5921A עַל al "upon" | opposed | content_part | 2 | none recorded | - | 0 | Only Jonathan the son of Asahel and Jahzeiah the son of Tikvah **opposed** this, and Meshullam and Shabbethai the Levite supported them. |
| Amo 2:4 | rejected | H5921A עַל al "upon" | rejected | content_part | 3 | none recorded | - | 0 | Thus says the Lord: “For three transgressions of Judah, and for four, I will not revoke the punishment, because they have **rejected** the law of the Lord, and have not kept his statutes, but their lies have led them astray, those after which their fathers walked. |
| Eze 22:26 | disregarded | H5956 עָלַם a.lam "to conceal" | disregarded | content_part | 3 | none recorded | - | 0 | Her priests have done violence to my law and have profaned my holy things. They have made no distinction between the holy and the common, neither have they taught the difference between the unclean and the clean, and they have **disregarded** my Sabbaths, so that I am profaned among them. |
| Ezr 10:15 | opposed | H5975G עָמַד a.mad "to stand: stand" | opposed | content_part | 2 | none recorded | - | 0 | Only Jonathan the son of Asahel and Jahzeiah the son of Tikvah **opposed** this, and Meshullam and Shabbethai the Levite supported them. |
| Pro 6:35 | accept | H6440N פָּנֶה pa.neh "face: kindness" | accept | content_part | 2 | none recorded | 14187, 17760, 20157 | 0 | He will **accept** no compensation; he will refuse though you multiply gifts. |
| Lev 1:3 | accepted | H7126H קָרַב qa.rav "to present: bring" | accepted | content_part | 5 | none recorded | - | 0 | “If his offering is a burnt offering from the herd, he shall offer a male without blemish. He shall bring it to the entrance of the tent of meeting, that he may be **accepted** before the Lord. |
| Lev 19:7 | accepted | H7521 רָצָה ra.tsah "to accept" | accepted | content_part | 2 | none recorded | - | 0 | If it is eaten at all on the third day, it is tainted; it will not be **accepted**, |
| Lev 22:23 | accepted | H7521 רָצָה ra.tsah "to accept" | accepted | content_part | 2 | none recorded | - | 0 | You may present a bull or a lamb that has a part too long or too short for a freewill offering, but for a vow offering it cannot be **accepted**. |
| Lev 1:3 | accepted | H7522 רָצוֹן ra.tson "acceptance" | accepted | content_part | 5 | none recorded | 17724 | 0 | “If his offering is a burnt offering from the herd, he shall offer a male without blemish. He shall bring it to the entrance of the tent of meeting, that he may be **accepted** before the Lord. |
| Lev 22:20 | acceptable | H7522 רָצוֹן ra.tson "acceptance" | acceptable | content_part | 4 | none recorded | - | 0 | You shall not offer anything that has a blemish, for it will not be **acceptable** for you. |

## 3a. What lives with the member words in their verses (pairings)

The member words are not alone in their verses. This section and the workbook sheets `Verse view`, `Pairings`, `Pairing summary` and `Verse observations` put the other words of each verse beside them, so that each word's company can be plotted and the pairings counted at the Strong's code, the surface and the collection. A type is a stored field (the entity party_kind, the negator flag, the collection of the surface, the qualifier subgroup, the morph class); a distance is the difference of the stored positions of two words (span order in the verse, not syntax); a side is before or after the member word. The meaning of a pairing, and what it does for the inner being, is read in context and is recorded in the empty `reading` column of the sheets, not computed here.

- 315 verses hold a member occurrence; they hold 6198 live verse_lexical rows, 370 of them member occurrences; 2768 pairings of a member occurrence with a typed word of its verse (a word with no type of its own, such as an article, is in `Verse view` and not in `Pairings`).
- Member occurrences with a live node: 54 of 370; typed neighbours with a live node: 390 of 2768 pairings.

### 3a.1 The pairings by type of neighbour

| neighbour type | pairings | adjacent | near | far | before | after |
|---|---|---|---|---|---|---|
| word of another collection | 1040 | 135 | 253 | 652 | 521 | 519 |
| connective | 798 | 130 | 215 | 453 | 464 | 334 |
| qualifier candidate | 279 | 36 | 60 | 183 | 168 | 111 |
| entity (divine) | 212 | 39 | 54 | 119 | 117 | 95 |
| negator | 191 | 60 | 51 | 80 | 116 | 75 |
| entity (human) | 182 | 12 | 48 | 122 | 107 | 75 |
| member of this collection | 66 | 6 | 30 | 30 | 33 | 33 |

Bands: adjacent is a distance of up to 1 position, near up to 3, far above that (cfg_setting collection.evidence_pairs).

The member occurrences placed in a subgroup of the collection index (`collection_subgroup_surface`, #2503): 0 of 370. The subgroup level below counts the pairings by the subgroup of the member word and, for a word of another collection, of that word; while the surfaces are unplaced it shows `(unplaced)`.

### 3a.2 The same pairings at each level

| level | distinct pairs | seen once | seen five or more times |
|---|---|---|---|
| Strong's code | 1645 | 1224 | 58 |
| surface | 1430 | 993 | 79 |
| subgroup | 145 | 17 | 84 |
| collection or type | 143 | 16 | 85 |

A pair seen once cannot show a trend; the level at which pairs recur is the level at which the comparison can be read. The pairs of each level are in `Pairing summary`.

### 3a.3 The most frequent partners at the collection level (top 15)

| neighbour (collection or type) | pairings | verses | adjacent | near | far | before | after |
|---|---|---|---|---|---|---|---|
| connective | 798 | 280 | 130 | 215 | 453 | 464 | 334 |
| qualifier candidate | 279 | 149 | 36 | 60 | 183 | 168 | 111 |
| entity (divine) | 212 | 135 | 39 | 54 | 119 | 117 | 95 |
| negator | 191 | 117 | 60 | 51 | 80 | 116 | 75 |
| entity (human) | 182 | 92 | 12 | 48 | 122 | 107 | 75 |
| member of this collection | 66 | 18 | 6 | 30 | 30 | 33 | 33 |
| hear | 49 | 29 | 12 | 15 | 22 | 40 | 9 |
| offer | 31 | 22 | 1 | 9 | 21 | 24 | 7 |
| know | 30 | 21 | 7 | 7 | 16 | 14 | 16 |
| righteous | 28 | 19 | 2 | 8 | 18 | 11 | 17 |
| supplication | 25 | 16 | 2 | 12 | 11 | 14 | 11 |
| serve | 22 | 19 | 2 | 5 | 15 | 10 | 12 |
| sin | 22 | 12 | 2 | 7 | 13 | 12 | 10 |
| anger | 21 | 11 | 1 | 6 | 14 | 7 | 14 |
| laugh | 19 | 10 | 0 | 3 | 16 | 10 | 9 |

### 3a.4 The most frequent Strong's code pairs (top 15)

| member code | neighbour code | neighbour type | pairings | verses |
|---|---|---|---|---|
| H3988A | H9002 | connective | 47 | 25 |
| G0720 | G2532 | connective | 40 | 20 |
| H3988A | H3588A | connective | 31 | 20 |
| H3985 | H9002 | connective | 29 | 19 |
| H7521 | H9002 | connective | 28 | 15 |
| H3988A | H3068G | entity (divine) | 27 | 18 |
| H3947H | H9002 | connective | 22 | 12 |
| H3988A | H3808 | negator | 22 | 17 |
| H3947H | H3808 | negator | 19 | 10 |
| H3988A | H0834A | connective | 18 | 13 |
| G0533 | G2532 | connective | 15 | 8 |
| G0593 | G2532 | connective | 14 | 5 |
| G3756 | G2532 | connective | 14 | 7 |
| G0720 | G1161 | connective | 13 | 13 |
| G0720 | G3756 | negator | 13 | 12 |

### 3a.5 Qualifier candidates as pairs

A neighbour is a qualifier candidate when a stored field says so: the negator flag (cluster T5), a surface in a qualifier subgroup (history data), or a morph class that qualifies (the classes are in cfg_setting collection.evidence_pairs). It is a candidate, not a finding; what a qualifier does to the pairing is read in context.

| why a candidate | pairings | adjacent | near | far |
|---|---|---|---|---|
| morph: adjective | 241 | 33 | 55 | 153 |
| negator | 194 | 60 | 54 | 80 |
| morph: adverb | 127 | 18 | 23 | 86 |
| qualifier subgroup | 26 | 6 | 10 | 10 |

The most frequent qualifier candidates (top 15):

| word | code | why | pairings |
|---|---|---|---|
| not | H3808 | negator | 84 |
| not | G3756 | negator | 27 |
| no | H3808 | negator | 19 |
| thus | H3541 | morph: adverb | 14 |
| all | G3956 | morph: adjective | 13 |
| not | G3361 | negator | 11 |
| there | H8033G | morph: adverb | 7 |
| now | H6258 | morph: adverb | 7 |
| not | H0408 | negator | 7 |
| three times | G5151 | morph: adverb | 7 |
| also | H1571 | morph: adverb | 6 |
| after | H0310A | morph: adjective | 5 |
| again | G3825 | morph: adverb | 5 |
| male | H2145 | morph: adjective | 4 |
| without blemish | H8549G | morph: adjective | 4 |

## 4. What the study has recorded for these occurrences

Of 370 occurrences, 0 have an engagement observation and 370 have none recorded. There are 94 live observations on them (0 engagement, 94 of other recorded stages, 0 of the retired catalogue stages) and 8 withdrawn.

### 4.1 Engagement: what each word does for the inner being (0 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

_no engagement observation covers these occurrences_

### 4.2 Other recorded observations (94)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 12657** (prior-capture, tag statement, marker not yet marked, status draft): Fear leads to lying, wrong, hypocrisy: "I feared the people and obeyed their voice"; Sarah "denied it … for she was afraid"; "he drew back and separated himself, fearing the circumcision party"
  - applies to 1 occurrence(s): Gen 18:15 (denied)
- **Observation 12998** (prior-capture, tag statement, marker not yet marked, status draft): What sets it off: God and people both: "when the Lord heard it, his anger was kindled"; "As soon as his master heard the words"; a sight: "when Haman saw Mordecai"; a refusal: "But Queen Vashti refused to come"; "Behold, I thought that he would surely come out to me"; news and alarm: "news from the east and the north shall alarm him, and he shall go out with great fury".
  - applies to 1 occurrence(s): Est 1:12 (refused)
- **Observation 13044** (prior-capture, tag statement, marker not yet marked, status draft): A person's anger leads to staying outside: "But he was angry and refused to go in".
  - applies to 1 occurrence(s): Luk 15:28 (refused)
- **Observation 13395** (prior-capture, tag link, marker not yet marked, status draft): refused → enraged, burned within (Est 1:12); filled with fury → face changed → furnace heated (Dan 3:19).
  - applies to 1 occurrence(s): Est 1:12 (refused)
- **Observation 13579** (prior-capture, tag link, marker not yet marked, status draft): angry → put them in custody (Gen 40:2–3); refused to come → enraged → counsel → decree (Est 1:12–19); angry → commanded the wise men destroyed → they sought Daniel (Dan 2:12–13); provokes him → forfeits his life (Pro 20:2).
  - applies to 1 occurrence(s): Est 1:12 (refused)
- **Observation 13584** (prior-capture, tag link, marker not yet marked, status draft): in their anger killed men → cursed be their anger → I will divide them (Gen 49:6–7); cast off pity, kept his wrath forever → punishment not revoked (Amo 1:11); sows injustice → reap calamity; rod of his fury will fail (Pro 22:8).
  - applies to 1 occurrence(s): Amo 1:11 (cast off)
- **Observation 13590** (prior-capture, tag link, marker not yet marked, status draft): the Lord has rejected the generation of his wrath → raise a lamentation (Jer 7:29).
  - applies to 1 occurrence(s): Jer 7:29 (rejected)
- **Observation 13672** (prior-capture, tag link, marker not yet marked, status draft): heard → angry → refused to go in → father came out and entreated (Luk 15:27–28).
  - applies to 1 occurrence(s): Luk 15:28 (refused)
- **Observation 13773** (prior-capture, tag statement, marker not yet marked, status draft): Lam 3: "He has made my chains heavy ... he shuts out my prayer ... He is a bear lying in wait for me" (3:7-10); the same poem then says "the Lord will not cast off forever, for, though he cause grief, he will have compassion according to the abundance of his steadfast love; for he does not afflict from his heart" (3:31-33): the chains are felt as heavy, and the poet confesses that the affliction does not come from God's heart; here the action and the heart are explicitly not the same.
  - applies to 1 occurrence(s): Lam 3:31 (cast off)
- **Observation 14181** (prior-capture, tag statement, marker not yet marked, status draft): Part 2 verses: what they add: Kin offence hardens. "A brother offended is more unyielding than a strong city, and quarreling is like the bars of a castle" (Pro 18:19). The closer the tie, the harder the wall. This is the reverse of Gen 13's reason for yielding ("for we are kinsmen"); Brothers' anger takes the form of imposed labour: "My mother's sons were angry with me; they made me keeper of the vineyards, but my own vineyard I have not kept!" (Song 1:6). The anger is felt by the one it lands on as the loss of her own vineyard. The next verse turns straight to "you whom my soul loves" (1:7); Edom against his brother: anger that never turns away. Edom "pursued his brother with the sword and ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Amo 1:11 (cast off)
- **Observation 14187** (prior-capture, tag statement, marker not yet marked, status draft): Part 2 verses: what they add: Anger lodges, and where it lodges is named. "Be not quick in your spirit to become angry, for anger lodges in the heart of fools" (Ecc 7:9). This joins Job 36:13 ("cherish anger"). Anger that stays has a lodging, and the lodging is the fool's. The verse before sets up the pair: "the patient in spirit is better than the proud in spirit" (7:8); Its duration is limited to a day: "Be angry and do not sin; do not let the sun go down on your anger, and give no opportunity to the devil" (Eph 4:26–27). Where Gen 27 waited years for anger to turn away, the NT sets a limit of one day. The reason given is what anger left overnight opens: "opportunity to the devil"; It repe ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 6:35 (accept)
- **Observation 14192** (prior-capture, tag statement, marker not yet marked, status draft): (d) Refused by a subordinate, or exposed: Vashti's refusal: "the king became enraged, and his anger burned within him" (Est 1:12). The counsellor at once generalises the fear to every household: "there will be contempt and wrath in plenty" (1:18). One refusal is read as a threat to the whole order of husbands, and answered by decree (1:19–20); The king of Syria, whose plans Elisha keeps disclosing: "the mind of the king of Syria was greatly troubled because of this thing" (2Ki 6:11). He suspects a traitor: "Will you not show me who of us is for the king of Israel?" (6:11). The servant's answer shows how completely he is exposed: Elisha "tells the king of Israel the words that you speak in yo ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Est 1:12 (refused)
- **Observation 14196** (prior-capture, tag statement, marker not yet marked, status draft): Part 2 verses: what they add. The four strands hold, and each gains an instance: Strand (a), a demand no one can meet, with the angry one now the demander. "There is not a man on earth who can meet the king's demand … no one can show it to the king except the gods, whose dwelling is not with flesh" (Dan 2:10–11). Then "Because of this the king was angry and very furious, and commanded that all the wise men of Babylon be destroyed" (2:12). This is the mirror of Gen 30:2. Jacob, faced with an impossible demand, named God as the only one who could meet it. Nebuchadnezzar hears the same answer ("except the gods") and orders a massacre; The anger is answered by "prudence and discretion" (Dan 2:14 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Mat 2:18 (refused)
- **Observation 14606** (prior-capture, tag statement, marker not yet marked, status draft): What it leads to: The explainers must go to the sufferer, and he prays for them. "go to my servant Job and offer up a burnt offering for yourselves. And my servant Job shall pray for you, for I will accept his prayer" (42:8). "the Lord restored the fortunes of Job, when he had prayed for his friends" (42:10). The one they explained by God's anger stands between them and God's anger; Job himself has just said: "I had heard of you by the hearing of the ear, but now my eye sees you; therefore I despise myself, and repent in dust and ashes" (42:5–6). God's anger then turns on the friends, not on Job.
  - applies to 1 occurrence(s): Job 42:8 (accept)
- **Observation 14658** (prior-capture, tag statement, marker not yet marked, status draft): Where it comes from: Pride: "The bricks have fallen, but we will build with dressed stones" (Isa 9:10); Leaders who mislead: "those who guide this people have been leading them astray" (9:16); Rejecting the law: "they have rejected the law of the Lord of hosts" (5:24).
  - applies to 1 occurrence(s): Isa 5:24 (rejected)
- **Observation 14662** (prior-capture, tag statement, marker not yet marked, status draft): Part C: Zep 3:8; Zec 7:12; Mal 1:4: Correction refused: "I said, 'Surely you will fear me; you will accept correction' … But all the more they were eager to make all their deeds corrupt" (Zep 3:7). The next verse (3:8) is wrath on the nations, followed by "a pure speech, that all of them may call upon the name of the Lord" (3:9); The heart made hard against hearing: "they refused to pay attention and turned a stubborn shoulder and stopped their ears … They made their hearts diamond-hard lest they should hear the law … Therefore great anger came" (Zec 7:11–12); Refusal returned in kind: "As I called, and they would not hear, so they called, and I would not hear" (7:13); Rebuilding against the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Zec 7:11 (refused)
- **Observation 14704** (prior-capture, tag statement, marker not yet marked, status draft): What it does: "For this put on sackcloth, lament and wail, for the fierce anger of the Lord has not turned back from us" (Jer 4:8); "Cut off your hair and cast it away; raise a lamentation on the bare heights, for the Lord has rejected and forsaken the generation of his wrath" (7:29); The land itself: "I looked, and behold, there was no man … the fruitful land was a desert … before his fierce anger" (4:25–26); "For this the earth shall mourn" (4:28).
  - applies to 1 occurrence(s): Jer 7:29 (rejected)
- **Observation 14726** (prior-capture, tag statement, marker not yet marked, status draft): How it co-exists: The body of the one speaking: "From on high he sent fire; into my bones he made it descend … he has left me stunned, faint all the day long" (1:13); "He has made my flesh and my skin waste away; he has broken my bones" (3:4); "He has walled me about so that I cannot escape; he has made my chains heavy; though I call and cry for help, he shuts out my prayer" (3:7–8); Hunger at its worst: "The hands of compassionate women have boiled their own children" (4:10); "Should women eat the fruit of their womb …?" (2:20); Pouring out the heart: "Arise, cry out in the night … Pour out your heart like water before the presence of the Lord! Lift your hands to him for the lives of your c ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Lam 3:31 (cast off)
- **Observation 14727** (prior-capture, tag statement, marker not yet marked, status draft): What it leads to. "Restore us to yourself, O Lord, that we may be restored! Renew our days as of old — unless you have utterly rejected us, and you remain exceedingly angry with us" (5:21–22). The book ends on the question.
  - applies to 1 occurrence(s): Lam 5:22 (rejected)
- **Observation 15168** (prior-capture, tag statement, marker not yet marked, status draft): The seat of God. "the man of lawlessness ... who opposes and exalts himself against every so-called god or object of worship, so that he takes his seat in the temple of God, proclaiming himself to be God" (2Th 2:3–4). This is the New Testament form of Eze 28:2 (batch 2): "I sit in the seat of the gods".
  - applies to 1 occurrence(s): 2Th 2:4 (opposes)
- **Observation 15195** (prior-capture, tag statement, marker not yet marked, status draft): The boast is not removed. It is moved: The command. "Let the one who boasts, boast in the Lord" (1Co 1:31; 2Co 10:17). This follows Christ "who became to us wisdom from God, righteousness and sanctification and redemption" (1:30). It is joined to "it is not the one who commends himself who is approved, but the one whom the Lord commends" (2Co 10:18); What to boast in; "let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight" (Jer 9:24); The boast is in knowing God, and what is known is his character; The soul's boast. "My soul makes its boast in the Lord; let th ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 44:9 (rejected)
- **Observation 15230** (prior-capture, tag statement, marker not yet marked, status draft): Wisdom: "Because I have called and you refused to listen ... I also will laugh at your calamity; I will mock when terror strikes you" (Pro 1:24–26).
  - applies to 1 occurrence(s): Pro 1:24 (refused)
- **Observation 15237** (prior-capture, tag statement, marker not yet marked, status draft): A pride word is used of God here. lāʿag "mock" and lîṣ "scorn" are said of God: "the Lord holds them in derision" (Psa 2:4); "you hold all the nations in derision" (Psa 59:8); "Toward the scorners he is scornful" (Pro 3:34); wisdom: "I will mock when terror strikes you" (Pro 1:26); The verses show how God's derision differs from human mocking; Where it comes from. It comes from the one who "sits in the heavens" (Psa 2:4), from the height that batches 1–3 found is his by nature; What it answers. It always answers a rising against him: kings set "against the Lord and against his Anointed" (Psa 2:2), those of whom it says "'Who,' they think, 'will hear us?'" (Psa 59:7), the scorners (Pro 3:34), ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 1:24 (refused)
- **Observation 15335** (prior-capture, tag statement, marker not yet marked, status draft): What it is set against: pride of heart (2Ch 32:25); "you have lifted up yourself against the Lord" (Dan 5:23), as his father's "heart was lifted up and his spirit was hardened so that he dealt proudly" (5:20); "He stiffened his neck and hardened his heart against turning" (2Ch 36:13); "Do not now be stiff-necked … but yield yourselves" (2Ch 30:8), answered by mocking in some and humbling in others (30:10–11; carried); "How long will you refuse to humble yourself before me?" (Exo 10:3), said to Pharaoh, whose heart is hardened (10:1).
  - applies to 1 occurrence(s): Exo 10:3 (refuse)
- **Observation 16345** (prior-capture, tag statement, marker not yet marked, status draft): Conscience: "holding faith and a good conscience. By rejecting this, some have made shipwreck of their faith" (1Ti 1:19; 1:5; 3:9).
  - applies to 1 occurrence(s): 1Ti 1:19 (rejecting)
- **Observation 16379** (prior-capture, tag statement, marker not yet marked, status draft): Obedience from the heart: "obedient from the heart to the standard of teaching" (Rom 6:17); "obey … with a sincere heart" (Eph 6:5; Col 3:22); "the Holy Spirit, whom God has given to those who obey him" (Act 5:32); "Our fathers refused to obey him … in their hearts they turned to Egypt" (Act 7:39); "He commands even the unclean spirits, and they obey him" (Mar 1:27) [O]
  - applies to 1 occurrence(s): Act 7:39 (refused)
- **Observation 16513** (prior-capture, tag statement, marker not yet marked, status draft): Heart set, heart gone elsewhere: "Ezra had set his heart to study the Law … and to teach his statutes and rules" (Ezr 7:10); "they rejected my rules … for their heart went after their idols" (Eze 20:16); "that he may incline our hearts to him … to keep … his rules" (1Ki 8:58)
  - applies to 1 occurrence(s): Eze 20:16 (rejected)
- **Observation 16551** (prior-capture, tag statement, marker not yet marked, status draft): Flesh and blasphemy: "defile the flesh, reject authority, and blaspheme the glorious ones" (Jude 8; 2Pe 2:10).
  - applies to 1 occurrence(s): Jude 8 (reject)
- **Observation 16892** (prior-capture, tag statement, marker not yet marked, status draft): The people later ask whether 26:30 has come true: "Have you utterly rejected Judah? Does your soul loathe Zion?" (Jer 14:19).
  - applies to 1 occurrence(s): Jer 14:19 (rejected)
- **Observation 16950** (prior-capture, tag statement, marker not yet marked, status draft): Flesh and Spirit as enemies: "the desires of the flesh are against the Spirit … opposed to each other" (Gal 5:17) [D3]; "the mind that is set on the flesh is hostile to God" (Rom 8:7); "he … has broken down in his flesh the dividing wall of hostility" (Eph 2:14) — flesh as the site of both enmity and its abolition.
  - applies to 1 occurrence(s): Gal 5:17 (opposed)
- **Observation 17038** (prior-capture, tag statement, marker not yet marked, status draft): 1.10 Evil desire of the soul: "the great man utters the evil desire of his soul" (Mic 7:3); "The soul of the wicked desires evil" (Pro 21:10); "the wicked boasts of the desires of his soul, and the one greedy for gain … renounces the Lord" (Psa 10:3); "These have chosen their own ways, and their soul delights in their abominations" (Isa 66:3); "The Lord … thwarts the craving [*nephesh*] of the wicked" (Pro 10:3); "The soul of the sluggard craves and gets nothing" (Pro 13:4)
  - applies to 1 occurrence(s): Psa 10:3 (renounces)
- **Observation 17071** (prior-capture, tag statement, marker not yet marked, status draft): 3.2 Greed: "They have eyes full of adultery … They entice unsteady souls. They have hearts trained in greed" (2Pe 2:14) — heart trained, souls unsteady; "their heart is set on their gain" (Eze 33:31); "the one greedy for gain … renounces the Lord" (Psa 10:3); "greedy for unjust gain; it takes away the life [*nephesh*] of its possessors" (Pro 1:19) — greed kills its own soul; "destroying lives to get dishonest gain" (Eze 22:27)
  - applies to 1 occurrence(s): Psa 10:3 (renounces)
- **Observation 17158** (prior-capture, tag statement, marker not yet marked, status draft): 9.4 Despising and rejecting — heart and soul as agents: "she despised him in her heart" (2Sa 6:16; 1Ch 15:29) — Michal; "How I hated discipline, and my heart despised reproof!" (Pro 5:12); "Whoever ignores instruction despises himself [*his nephesh*]" (Pro 15:32); "if your soul abhors my rules" (Lev 26:15); "their soul abhorred my statutes" (Lev 26:43); "the wicked … renounces God and says in his heart, 'You will not call to account'" (Psa 10:13; 10:3); "their heart went after their idols" (Eze 20:16)
  - applies to 1 occurrence(s): Psa 10:3 (renounces)
- **Observation 17159** (prior-capture, tag statement, marker not yet marked, status draft): Conscience rejected: "holding faith and a good conscience. By rejecting this, some have made shipwreck of their faith" (1Ti 1:19).
  - applies to 1 occurrence(s): 1Ti 1:19 (rejecting)
- **Observation 17161** (prior-capture, tag statement, marker not yet marked, status draft): Flesh rejecting authority: "defile the flesh, reject authority" (Jude 8); "the lust of defiling passion … despise authority" (2Pe 2:10).
  - applies to 1 occurrence(s): Jude 8 (reject)
- **Observation 17163** (prior-capture, tag statement, marker not yet marked, status draft): Cast off: "O Lord, why do you cast my soul away?" (Psa 88:14); "Have you utterly rejected Judah? Does your soul loathe Zion?" (Jer 14:19) — God's *nephesh*.
  - applies to 1 occurrence(s): Jer 14:19 (rejected)
- **Observation 17164** (prior-capture, tag statement, marker not yet marked, status draft): Deserted: "like a wife deserted and grieved in spirit … cast off" (Isa 54:6) [H1].
  - applies to 1 occurrence(s): Isa 54:6 (cast off)
- **Observation 17166** (prior-capture, tag statement, marker not yet marked, status draft): God's heart vs man's eyes: "I have rejected him … the Lord looks on the heart" (1Sa 16:7).
  - applies to 1 occurrence(s): 1Sa 16:7 (rejected)
- **Observation 17525** (prior-capture, tag statement, marker not yet marked, status draft): Passage: Saul says *"I have obeyed"*, and puts the spoil down to the people, *"to sacrifice to the Lord"* (15:20–21). Samuel answers, and goes on: *"rebellion is as the sin of divination, and presumption is as iniquity and idolatry. Because you have rejected the word of the Lord, he has also rejected you"* (15:23).
  - applies to 1 occurrence(s): 1Sa 15:23 (rejected)
- **Observation 17527** (prior-capture, tag statement, marker not yet marked, status draft): Passage: the priests *"despise my name"* (1:6). They offer the blind and lame. *"Present that to your governor; will he accept you or show you favor?"* (1:8). After the verse: *"my name will be great among the nations"* (1:11).
  - applies to 1 occurrence(s): Mal 1:8 (accept)
- **Observation 17585** (prior-capture, tag statement, marker not yet marked, status draft): Mal 1:10. *"Oh that there were one among you who would shut the doors, that you might not kindle fire on my altar in vain! I have no pleasure in you, says the Lord of hosts, and I will not accept an offering from your hand."*
  - applies to 1 occurrence(s): Mal 1:10 (accept)
- **Observation 17724** (prior-capture, tag statement, marker not yet marked, status draft): A2 Offerings accepted | Lev 1:3; 19:5; 22:19–21, 29; 23:11; Exo 28:38; Jer 6:20; Mal 2:13; Pro 15:8 | Accepted: the person, through the offering. Refused: where word or covenant is broken. | 13.1 *Delight*: new paragraph, "What makes an offering accepted"
  - applies to 7 occurrence(s): Exo 28:38 (accepted), Lev 1:3 (accepted), Lev 19:5 (accepted), Lev 22:19 (accepted), Lev 22:21 (accepted), Lev 22:29 (accepted), Lev 23:11 (accepted)
- **Observation 17760** (prior-capture, tag statement, marker not yet marked, status draft): 3. A husband's jealousy with no witness (10.6): Num 5:14–31. The "spirit of jealousy" comes over the husband whether the wife "has defiled herself" or "has not" (5:14): the law itself says the jealousy may be wrong. The offering is "of jealousy … of remembrance", with no oil and no frankincense (5:15). The matter is not his to settle: "he shall set the woman before the Lord" (5:30); "The man shall be free from iniquity" (5:31). Beside Pro 6:34–35, where a husband's jealousy "will accept no compensation", I read the law as taking the jealousy out of the husband's hands and putting it before God. Num 5:18 and 5:25 (the ritual) are carried by this account.
  - applies to 1 occurrence(s): Pro 6:35 (accept)
- **Observation 17861** (prior-capture, tag statement, marker not yet marked, status draft): The will that stays outside. *"But he was angry and refused to go in. His father came out and entreated him"* (Luk 15:28). The verb is the will word. The older brother's anger takes the form of a will that refuses to go in. The father does not wait inside; he comes out. 10.13 has the anger. 10.7 gets the will.
  - applies to 1 occurrence(s): Luk 15:28 (refused)
- **Observation 17937** (prior-capture, tag statement, marker not yet marked, status draft): What lies behind refusing. *"you refuse to come to me that you may have life"* (Joh 5:40). The passage gives what lies behind it: *"you do not have the love of God within you"* (5:42); *"How can you believe, when you receive glory from one another and do not seek the glory that comes from the only God?"* (5:44); The will refuses because the desire is set elsewhere, on glory from people. That is in the verses, not read in. They had searched the Scriptures (5:39), so the refusal is not a lack of knowing.
  - applies to 1 occurrence(s): Joh 5:40 (refuse)
- **Observation 18008** (prior-capture, tag statement, marker not yet marked, status draft): 1Sa 15:28 | M72 | "better than you": the kingdom torn away after *"you have rejected the word"* (15:26).
  - applies to 1 occurrence(s): 1Sa 15:26 (rejected)
- **Observation 18888** (prior-capture, tag statement, marker not yet marked, status draft): Hiding what I hold: What God has done is not to be hidden. "I have not concealed your steadfast love and your faithfulness from the great congregation" (Psalm 40:10). "We will not hide them from their children, but tell to the coming generation the glorious deeds of the Lord" (Psalm 78:4). In his pain, Job's comfort is that "I have not denied the words of the Holy One" (Job 6:10). Some things cannot be hidden: "A city set on a hill cannot be hidden" (Matthew 5:14). And a hidden good is worth less than a visible one: "Better is open rebuke than hidden love" (Proverbs 27:5).; Two men in Jesus's parables hide something in the ground, and they hide it for different reasons. One finds "treasure h ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 6:10 (denied)
- **Observation 18986** (prior-capture, tag statement, marker not yet marked, status draft): The passage. The verse before is *"Who can discern his errors? Declare me innocent from hidden faults"* (19:12). The verse after is *"Let the words of my mouth and the meditation of my heart be acceptable in your sight"* (19:14).
  - applies to 1 occurrence(s): Psa 19:14 (acceptable)
- **Observation 19124** (prior-capture, tag statement, marker not yet marked, status draft): Jude 8 (read with 2Pe 2:10, carried in Ch 7). *"Yet in like manner these people also, relying on their dreams, defile the flesh, reject authority, and blaspheme the glorious ones."*
  - applies to 1 occurrence(s): Jude 8 (reject)
- **Observation 19174** (prior-capture, tag statement, marker not yet marked, status draft): 1Sa 15:28 | none (ruling) | the kingdom taken from the one who rejected the word (15:26, 28) | 13.1 *Ruling*; Saul's "yet honor me now" (15:30) forward to M22
  - applies to 1 occurrence(s): 1Sa 15:26 (rejected)
- **Observation 19226** (prior-capture, tag statement, marker not yet marked, status draft): (c) Not withholding God's word or works.; "I have not hidden your deliverance within my heart; I have spoken" (Psa 40:10). The seat is where a word would be held back.; "We will not hide them from their children, but tell to the coming generation" (Psa 78:4).; "what is with the Almighty I will not conceal" (Job 27:11); "what wise men have told, without hiding it from their fathers" (Job 15:18).; "This would be my comfort … for I have not denied [concealed] the words of the Holy One" (Job 6:10): having not concealed is Job's comfort in pain.; "proclaim, conceal it not" (Jer 50:2).
  - applies to 1 occurrence(s): Job 6:10 (denied)
- **Observation 19231** (prior-capture, tag statement, marker not yet marked, status draft): Seat.; In the verse, the bearer's own (genuine): Psa 40:10 "I have not hidden your deliverance within my heart". Batch A v3 §6 ("The heart can conceal or not"). The heart is the place where a word could be kept back, and the verse says it was not.; In the verse, the offender's own self: Isa 3:9 "they have brought evil on themselves [*their nephesh*]". Batch D v2 §2.3 ("Evil against one's own soul"). Seat-sense: *nephesh* is here the self, reflexively, and it passes the check in that sense. New in v3: the verse holds the phenomenon and its outcome together. The face does *not* conceal ("they do not hide it"), and the evil disclosed comes back on the self that disclosed it. Shamelessness is no ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 6:10 (denied)
- **Observation 19419** (prior-capture, tag statement, marker not yet marked, status draft): 1.10 A person can refuse it, or serve it: *"but the Pharisees and the lawyers rejected the purpose of God for themselves, not having been baptized by him"* (Luk 7:30). Over against them, the people and the tax collectors *"declared God just"* (7:29).; *"For David, after he had served the purpose of God in his own generation, fell asleep"* (Act 13:36).
  - applies to 1 occurrence(s): Luk 7:30 (rejected)
- **Observation 19471** (prior-capture, tag statement, marker not yet marked, status draft): Ground: why or how the choice is made (12): Knowing: Isa 7:15–16: *"when he knows how to refuse the evil and choose the good"*; Act 15:22, 25: *"it seemed good to us … to choose men"* (G1380); Liking or preference: Deu 23:16: *"wherever it suits him"* (H2896A); 2Sa 19:38: *"whatever seems good to you"* (H2896A); Jos 24:15: *"if it is evil in your eyes to serve the Lord, choose this day"*; Pleasure: Act 6:5, *"what they said pleased the whole gathering, and they chose Stephen"*; Fear: Psa 25:12, *"the man who fears the Lord … the way that he should choose"*; Not listening: Isa 65:12, *"when I spoke, you did not listen … and chose what I did not delight in"*; Iniquity: Job 15:5, *"your iniquit ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 19472** (prior-capture, tag statement, marker not yet marked, status draft): Paired: named alongside the choosing as a parallel act (10): Refuse: Isa 7:15, Isa 7:16; Reject: Job 34:33; Know: Job 34:4 (*"Let us choose what is right; let us know among ourselves what is good"*), Job 34:33; Envy: Pro 3:31 (*"Do not envy … and do not choose"*); Desire: Isa 1:29 (*"the oaks that you desired … the gardens that you have chosen"*); The soul's delight: Isa 66:3 (*"These have chosen their own ways, and their soul delights in their abominations"*); Hold fast: Isa 56:4 (*"who choose the things that please me and hold fast my covenant"*); Take care: Job 36:21
  - applies to 3 occurrence(s): Job 34:33 (reject), Isa 7:15 (refuse), Isa 7:16 (refuse)
- **Observation 19475** (prior-capture, tag statement, marker not yet marked, status draft): Contrast: set against the choosing (8): Despised and abhorred by people: Isa 49:7, Jer 33:24, 1Pe 2:4 (*"rejected by men but in the sight of God chosen"*); Rom 11:7: Israel's seeking, and the hardening; Pro 10:20: *"the heart of the wicked is of little worth"*, set against "choice silver"; Isa 45:4: *"though you do not know me"*
  - applies to 2 occurrence(s): Jer 33:24 (rejected), 1Pe 2:4 (rejected)
- **Observation 19587** (prior-capture, tag statement, marker not yet marked, status draft): Led to: Elihu's question whether anyone has said to God *"I will not offend any more; teach me what I do not see"* (v31–32).; *"Will he then make repayment to suit you, because you reject it?"* (v33).
  - applies to 1 occurrence(s): Job 34:33 (reject)
- **Observation 19597** (prior-capture, tag statement, marker not yet marked, status draft): Outcome: The knowing serves as a measure of time: *"before the boy knows how to refuse the evil and choose the good, the land whose two kings you dread will be deserted"* (v16).; *"the king of Assyria"* follows (v17).; Ahaz's own refusal in v12 is the occasion of the whole sign. The verses do not connect it to the child's refusing.
  - applies to 1 occurrence(s): Isa 7:16 (refuse)
- **Observation 19607** (prior-capture, tag statement, marker not yet marked, status draft): Psalm 106:5: "that I may rejoice in the gladness of your nation": Psalm 106 follows 105 and tells the same history from the other side. I read the two side by side because they stand together; neither refers to the other.; The speaker asks to be included: *"Remember me, O Lord, when you show favor to your people; help me when you save them, that I may look upon the prosperity of your chosen ones, that I may rejoice in the gladness of your nation, that I may glory with your inheritance"* (v4–5). He does not claim the chosen ones' gladness. He asks to look upon it and to share it. "Gladness" here (H8057) is the same word as David's *"rejoicing"* in 2 Samuel 6:12.; He then confesses at once: *" ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 19641** (prior-capture, tag statement, marker not yet marked, status draft): Jeremiah 33:24: "'The Lord has rejected the two clans that he chose'? Thus they have despised my people": *"Have you not observed that these people are saying, 'The Lord has rejected the two clans that he chose'? Thus they have despised my people so that they are no longer a nation in their sight"* (v24).; Others look at the state of the chosen and draw a conclusion about God: he has rejected them. Their contempt rests on that conclusion. "Despised" is *nāʾaṣ* (*to spurn*; H5006). The measure is their own: *"in their sight"*. "Rejected" is *māʾas* (H3988A), the same verb as *"refuse the evil"* in Isaiah 7:15 (§2a).; God answers with the fixed order of creation: *"If I have not established my ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 19642** (prior-capture, tag statement, marker not yet marked, status draft): What others do around a choice, in these verses: grumble against the chosen man, and God counts it as against himself (Num 16:11; 17:5, 10); seek more than they were given, and are jealous (Num 16:10; Psa 106:16); name a choice as shame, and are angry at what it costs them (1Sa 20:30–31); despise the chosen in the heart, by the eyes of people (2Sa 6:16, 20); despise and abhor the chosen servant (Isa 49:7); conclude from the chosen people's ruin that God rejected them, and despise them in their own sight (Jer 33:24); ask to share the joy of the chosen (Psa 106:5); not know God, and still be called and equipped for the sake of the chosen (Isa 45:4–5); offer an inner act, the humbling of the so ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 33:24 (rejected)
- **Observation 19651** (prior-capture, tag statement, marker not yet marked, status draft): Isaiah 7:15–16 — "when he knows how to refuse the evil and choose the good": The setting is a king’s heart in fear. Syria and Ephraim are marching on Jerusalem, and *"the heart of Ahaz and the heart of his people shook as the trees of the forest shake before the wind"* (v2). The Lord sends Isaiah with a word for that heart: *"Be careful, be quiet, do not fear, and do not let your heart be faint"* (v4); the threat *"shall not stand"* (v7); then the condition: *"If you are not firm in faith, you will not be firm at all"* (v9). Both "firm" words are the one verb (H0539), so standing firm and being kept firm are the same word.; Then the Lord makes Ahaz an offer: *"Ask a sign of the Lord your God ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 19652** (prior-capture, tag statement, marker not yet marked, status draft): Isaiah 7:15–16 — "when he knows how to refuse the evil and choose the good": The next verse sets a second consequence against the same knowing: *"before the boy knows how to refuse the evil and choose the good, the land whose two kings you dread will be deserted"* (v16). What Ahaz feared will be gone. Then comes what Ahaz’s own choice brings on him: *"The Lord will bring upon you and upon your people and upon your father’s house such days as have not come … the king of Assyria!"* (v17).; The oracle uses the same verb for refusing once more. Isaiah 8:6 has *"Because this people has refused the waters of Shiloah that flow gently"*, and it is the same word as *"refuse the evil"* (H3988A). Its c ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Isa 7:16 (refuse), Isa 8:6 (refused)
- **Observation 19653** (prior-capture, tag statement, marker not yet marked, status draft): Isaiah 1:29 — "the oaks that you desired … the gardens that you have chosen": The oracle opens as a lawsuit: *"Hear, O heavens, and give ear, O earth"* (v2). The charge goes to the inner being: *"Children have I reared and brought up, but they have rebelled against me"* (v2); *"The ox knows its owner … but Israel does not know, my people do not understand"* (v3); *"The whole head is sick, and the whole heart faint"* (v5); Their worship goes on, and the Lord refuses it: *"I do not delight in the blood of bulls"* (v11); *"your appointed feasts my soul hates"* (v14); *"even though you make many prayers, I will not listen"* (v15).; Then the choice is laid before them, in the same two-sided shape ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 1:20 (refuse)
- **Observation 19657** (prior-capture, tag statement, marker not yet marked, status draft): Refusing is choosing (Isa 7:15–16). The act is one act with two sides, and refusing can go either way. The child refuses the evil. Ahaz refuses the sign, and the people refuse the gentle waters (8:6), with the same verb. This sharpens the test reading of Isa 65:12, which said that not answering and not listening are already choosing: in Isa 8:6 the refusal is named outright.
  - applies to 2 occurrence(s): Isa 7:15 (refuse), Isa 7:16 (refuse)
- **Observation 19660** (prior-capture, tag statement, marker not yet marked, status draft): The choice is laid out as an offer, with both outcomes (Isa 1:16–20). *"cease to do evil, learn to do good"*; *"willing"* or *"refuse"*; eat, or be eaten. In Isa 7:15 the right choice also ends in eating.
  - applies to 2 occurrence(s): Isa 1:20 (refuse), Isa 7:15 (refuse)
- **Observation 19664** (prior-capture, tag statement, marker not yet marked, status draft): Psalm 25:12 — "Him will he instruct in the way that he should choose": The psalm is a prayer from someone in trouble. It begins *"To you, O Lord, I lift up my soul"*; *"O my God, in you I trust; let me not be put to shame"* (v1–2). It ends with that same person *"lonely and afflicted"*. Among the trouble: *"The troubles of my heart are enlarged"* (v17); *"how many are my foes, and with what violent hatred they hate me"* (v19); *"guard my soul … Let me not be put to shame"* (v20); Running through the whole psalm is the person's own guilt: *"Remember not the sins of my youth or my transgressions"* (v7); *"pardon my guilt, for it is great"* (v11); *"forgive all my sins"* (v18); The person who a ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 19679** (prior-capture, tag statement, marker not yet marked, status draft): 2 Samuel 19:38 — "whatever seems good to you, and all that you desire of me": Barzillai had fed David in his flight. He came with others bringing *"honey and curds and sheep and cheese from the herd, for David and the people with him to eat"*, saying *"The people are hungry and weary and thirsty in the wilderness"* (17:27, 29). When David returns, the king offers him a place at court: *"Come over with me, and I will provide for you with me in Jerusalem"* (19:33).; Barzillai declines, and his reason is about his own inner capacity: *"I am this day eighty years old. Can I discern what is pleasant and what is not? Can your servant taste what he eats or what he drinks? Can I still listen to the ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Isa 7:15 (refuse), Isa 7:16 (refuse)
- **Observation 19704** (prior-capture, tag statement, marker not yet marked, status draft): The chosen city can be cast off, and chosen again: "I will cast off this city that I have chosen, Jerusalem" (2Ki 23:27); "the Lord will again comfort Zion and again choose Jerusalem" (Zec 1:17; also Zec 2:12); The choice is named against an accuser: "The Lord who has chosen Jerusalem rebuke you!" (Zec 3:2)
  - applies to 1 occurrence(s): 2Ki 23:27 (cast off)
- **Observation 19711** (prior-capture, tag statement, marker not yet marked, status draft): Rejection stands beside choosing: "He rejected the tent of Joseph; he did not choose the tribe of Ephraim, but he chose the tribe of Judah" (Psa 78:67–68); Others can say the choice has been withdrawn: "The Lord has rejected the two clans that he chose" (Jer 33:24).
  - applies to 2 occurrence(s): Psa 78:67 (rejected), Jer 33:24 (rejected)
- **Observation 19727** (prior-capture, tag statement, marker not yet marked, status draft): The Son: from the cloud: "This is my Son, my Chosen One; listen to him!" (Luk 9:35); mocked at the cross: "let him save himself, if he is the Christ of God, his Chosen One!" (Luk 23:35); "a living stone rejected by men but in the sight of God chosen and precious" (1Pe 2:4); "a cornerstone chosen and precious, and whoever believes in him will not be put to shame" (1Pe 2:6); Chosen by God and rejected by men are stated together.
  - applies to 1 occurrence(s): 1Pe 2:4 (rejected)
- **Observation 19735** (prior-capture, tag statement, marker not yet marked, status draft): What is "more acceptable": "To do righteousness and justice is more acceptable to the Lord than sacrifice" (Pro 21:3, Niphal).
  - applies to 1 occurrence(s): Pro 21:3 (more acceptable)
- **Observation 19739** (prior-capture, tag statement, marker not yet marked, status draft): Choosing needs knowing and instruction: "when he knows how to refuse the evil and choose the good" (Isa 7:15, 7:16); "Who is the man who fears the Lord? Him will he instruct in the way that he should choose" (Psa 25:12); It can be done together: "Let us choose what is right; let us know among ourselves what is good" (Job 34:4).
  - applies to 2 occurrence(s): Isa 7:15 (refuse), Isa 7:16 (refuse)
- **Observation 19781** (prior-capture, tag face, marker not yet marked, status draft): Face: Chosen by God, rejected or hated by men (v2); Who: God, Jesus; Circumstance in the verses: "rejected by men but in the sight of God chosen"; "I chose you out of the world, therefore the world hates you"; scoffed "his Chosen One"; Verses: 1Pe 2:4, Joh 15:19, Luk 23:35
  - applies to 1 occurrence(s): 1Pe 2:4 (rejected)
- **Observation 19784** (prior-capture, tag face, marker not yet marked, status draft): Face: Choosing withdrawn, and renewed; Who: God; Circumstance in the verses: "cast off this city that I have chosen"; "again choose Jerusalem"; Verses: 2Ki 23:27, Zec 1:17, Isa 14:1
  - applies to 1 occurrence(s): 2Ki 23:27 (cast off)
- **Observation 19788** (prior-capture, tag face, marker not yet marked, status draft): Face: Choosing that needs knowing; Who: person; Circumstance in the verses: "knows how to refuse the evil and choose the good"; "him will he instruct in the way"; Verses: Isa 7:15, Psa 25:12
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 19836** (prior-capture, tag statement, marker not yet marked, status draft): H3988A, "refuse, reject, despise". This is the other side of the act: *"refuse the evil"* (Isa 7:15); *"this people has refused the waters of Shiloah"* (Isa 8:6); *"because you reject it"* (Job 34:33); Job's last word: *"I despise myself, and repent"* (Job 42:6)
  - applies to 3 occurrence(s): Job 34:33 (reject), Isa 7:15 (refuse), Isa 8:6 (refused)
- **Observation 19839** (prior-capture, tag statement, marker not yet marked, status draft): Choosing has two sides: Refusing is itself choosing. The child *"knows how to refuse the evil and choose the good"* (Isa 7:15). The oracle around that verse shows refusing going both ways. Ahaz refuses the Lord's offer of a sign with pious words: *"I will not ask, and I will not put the Lord to the test"* (Isa 7:12). The people *"refused the waters of Shiloah that flow gently"* (8:6). The right refusing and the wrong refusing are set in one oracle, each with its own consequence.; Not answering is already choosing. *"when I called, you did not answer; when I spoke, you did not listen, but you did what was evil in my eyes and chose what I did not delight in"* (Isa 65:12; repeated in 66:4). The ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Isa 1:20 (refuse), Isa 7:15 (refuse), Isa 8:6 (refused)
- **Observation 19910** (prior-capture, tag statement, marker not yet marked, status draft): Job 34:33 | the words (reject); weighed by another (cannot choose for him); Job's choice at 42:6; faces | batch 4
  - applies to 1 occurrence(s): Job 34:33 (reject)
- **Observation 19944** (prior-capture, tag statement, marker not yet marked, status draft): A conclusion drawn from ruin. *"'The Lord has rejected the two clans that he chose'? Thus they have despised my people so that they are no longer a nation in their sight"* (Jer 33:24). Others look at the state of the chosen, decide God has rejected them, and despise them on that ground. God's answer is that his choosing is as fixed as day and night (33:25–26).
  - applies to 1 occurrence(s): Jer 33:24 (rejected)
- **Observation 19946** (prior-capture, tag statement, marker not yet marked, status draft): Rejection. *"a living stone rejected by men but in the sight of God chosen and precious"* (1Pe 2:4). The word is to reject after testing: men weighed him and set him aside.
  - applies to 1 occurrence(s): 1Pe 2:4 (rejected)
- **Observation 19947** (prior-capture, tag statement, marker not yet marked, status draft): Whose eyes. In four of these the measure is named, and it is set against God's: *"in his own eyes"* against the place God chooses (Deu 12:8); *"before the eyes of his servants' female servants"* against *"before the Lord"* (2Sa 6:20–21); *"in their sight"* (Jer 33:24); *"rejected by men but in the sight of God chosen"* (1Pe 2:4).
  - applies to 2 occurrence(s): Jer 33:24 (rejected), 1Pe 2:4 (rejected)
- **Observation 19959** (prior-capture, tag statement, marker not yet marked, status draft): Despising.; Michal despises the chosen man *"in her heart"*, by the eyes of people (2Sa 6:16, 20).; The servant is *"deeply despised"* by others, and kings will bow (Isa 49:7). Same verb, *bāzâ*.; The chosen people themselves *"despised the pleasant land"* (Psa 106:24, §2b; *māʾas*).; Others *"despised my people"*, concluding that God had rejected them (Jer 33:24; *nāʾaṣ*).; *Why:* who despises what. It is aimed at the chosen by others, and by the chosen at what they were given. Each verse names its own ground: honour before people, the chosen people's ruin, no faith in the promise.
  - applies to 1 occurrence(s): Jer 33:24 (rejected)
- **Observation 20150** (prior-capture, tag statement, marker not yet marked, status draft): A warning: Abner warned Asahel twice, *"Turn aside from following me. Why should I strike you to the ground?"*, and *"he refused to turn aside"* (2Sa 2:21–23).
  - applies to 1 occurrence(s): 2Sa 2:23 (refused)
- **Observation 20157** (prior-capture, tag statement, marker not yet marked, status draft): Jealousy: *"For jealousy makes a man furious … He will accept no compensation; he will refuse though you multiply gifts"* (Pro 6:34–35).
  - applies to 2 occurrence(s): Pro 6:35 (accept), Pro 6:35 (refuse)
- **Observation 20163** (prior-capture, tag statement, marker not yet marked, status draft): Cleansing, after reasoning: *"Come now, let us reason together … though your sins are like scarlet, they shall be as white as snow … If you are willing and obedient, you shall eat the good of the land; but if you refuse and rebel, you shall be eaten by the sword"* (Isa 1:18–20). This is the one place in the set where the will is invited with "if". Both ways are set out, as in *Life and death set before a person* (10.7).
  - applies to 1 occurrence(s): Isa 1:20 (refuse)
- **Observation 20185** (prior-capture, tag statement, marker not yet marked, status draft): Refusing a role. *"I refuse to be a judge of these things"* (Act 18:15).
  - applies to 1 occurrence(s): Act 18:15 (refuse)
- **Observation 20296** (prior-capture, tag statement, marker not yet marked, status draft): Whose measure. *"rejected by men but in the sight of God chosen"* (1Pe 2:4). This sits with batch 1 (Deu 12:8), batch 2 (2Sa 6:20; Jer 33:24) and §2a.
  - applies to 2 occurrence(s): Jer 33:24 (rejected), 1Pe 2:4 (rejected)
- **Observation 20307** (prior-capture, tag statement, marker not yet marked, status draft): Job 34:33 — Elihu: "For you must choose, and not I": Elihu frames a confession and asks whether Job will make it: *"For has anyone said to God"*: *"I have borne punishment; I will not offend any more"*; *"teach me what I do not see; if I have done iniquity, I will do it no more"* (v31–32). Then: *"Will he then make repayment to suit you, because you reject it? For you must choose, and not I; therefore declare what you know"* (v33).; Two things stand in the verse:
  - applies to 1 occurrence(s): Job 34:33 (reject)
- **Observation 20308** (prior-capture, tag statement, marker not yet marked, status draft): The refusing word comes back. *"because you reject it"* uses H3988A, the same verb as *"refuse the evil"* in Isaiah 7:15. Elihu says Job is refusing, and that God will not repay on Job's terms because of it.
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 20313** (prior-capture, tag statement, marker not yet marked, status draft): The refusing verb returns at the end. Elihu's *"you reject"* and Job's *"I despise … and repent"* are the same verb (34:33; 42:6), the verb of *"refuse the evil"* (Isa 7:15). In Job the choice is made when *"now my eye sees you"* (42:5). This stands beside the test reading of Jos 24, where the people chose from what they had seen.
  - applies to 1 occurrence(s): Isa 7:15 (refuse)
- **Observation 12492** (strand-reading, tag key-statement, marker not yet marked, status resolved): God chooses what he wants: "Is not this the fast that I choose: to loose the bonds of wickedness" (Isa 58:6), set against a fast of bowing the head (Isa 58:5); "To do righteousness and justice is more acceptable to the Lord than sacrifice" (Pro 21:3); "I will appoint over her whomever I choose. For who is like me?" (Jer 49:19; Jer 50:44).
  - meaning: God's choosing states what pleases him: justice and freeing the oppressed over outward humbling; his choice is sovereign.
  - implication: God's will is shown in what he chooses.
  - applies to 1 occurrence(s): Pro 21:3 (more acceptable)
- **Observation 12501** (strand-reading, tag key-statement, marker not yet marked, status resolved): A refusal from inside a feeling: fear, "David was afraid of the Lord that day" and "was not willing to take the ark of the Lord into the city of David" (2Sa 6:9-10), until "it was told King David, The Lord has blessed the household of Obed-edom" (6:12); grief, the elders came "to raise him from the ground, but he would not, nor did he eat food with them" (2Sa 12:17); jealousy, "He will accept no compensation; he will refuse though you multiply gifts" (Pro 6:35).
  - meaning: Fear, grief and jealousy hold the will in a no; what a person then hears can change what they are willing to do.
  - implication: The feelings of M01 fear, grief and jealousy act on the will, in the verses themselves.
  - applies to 1 occurrence(s): Pro 6:35 (refuse)
- **Observation 12521** (strand-reading, tag key-statement, marker not yet marked, status open): The will word also carries wanting to know and stated wishes: "desiring to know the real reason" (Act 22:30; 23:28); "We wish to know therefore what these things mean" (Act 17:20); "I would like to hear the man myself" (Act 25:22); "I refuse to be a judge of these things" (Act 18:15). Paul's wishes in teaching each come with their reason: "I desire then that in every place the men should pray, lifting holy hands without anger or quarreling" (1Ti 2:8); "So I would have younger widows marry" (1Ti 5:14); "I want you to insist on these things, so that those who have believed in God may be careful to devote themselves to good works" (Tit 3:8); "I want you to know" (Phi 1:12); "so that our joy may ... (cut; the whole text is in the workbook)
  - meaning: The Greek will word also names a desire to know, a refusal of a role, and a teacher's stated wish, each given its reason.
  - implication: A stated wish in teaching is weaker evidence for the inner act than a wish in narrative.
  - applies to 1 occurrence(s): Act 18:15 (refuse)

### 4.3 The retired catalogue observations (0, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

_no rows_

### 4.4 Withdrawn observations (8)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 8 |

| reason as stored | observations |
|---|---|
| no change record | 8 |

## 5. Claims and the narrative

43 claims rest on these occurrences: 2 on an observation of these words and 41 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (2)

- **C-340** (narrative, verdict New, status current, in narrative 1): What God chooses shows what pleases him: justice and freeing the oppressed above an outward humbling; whom he appoints is his own choice.
  - beyond the text: reads God's choosing of a fast and of whom he appoints as a statement of his pleasure
  - rests on: observation 12492 (strand-reading key-statement, live; Pro 21:3)
  - told in: chapter 13.1 Divine, Choosing; chapter 10.7 Choosing and setting direction, Others around a choice
- **C-349** (narrative, verdict New, status current, in narrative 1): Fear, a melted heart, grief and jealousy hold the will in a refusal, and what a person then hears can move it.
  - beyond the text: gathers four feelings under one effect on the will, and reads David's change as moved by what he heard
  - rests on: observation 12501 (strand-reading key-statement, live; Pro 6:35)
  - told in: chapter 10.7 Choosing and setting direction, Willing

### 5.2 Claims reached by a verse only (41)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| 2-11 | Stands for the NT. In the OT, flesh is frail, not hostile, and "a heart of flesh" is God's gift (Eze 36:26). The hostility of flesh to Spirit is NT-specific (dep §3.5) | Gal 5:17 | opposed G0480 | current | not told in a section |
| 2-16 | The verse puts soul and spirit beside joints and marrow, which are adjacent, and its end point is the heart: "discerning the thoughts and intentions of the heart". It shows closeness that only the word can divide. It is one of several places the words part; others are added (1Co 15:45; 1Co 14:14–15; the *psychikos* / *pneumatikos* contrast in 1Co 2:14; 15:44–46) (dep §3.4; B §8) | 1Co 2:14; 15:44–46 | accept G1209 | current | not told in a section |
| 9-3 | Idols are taken "into their hearts" (Eze 14:3–7); the heart "goes after" idols (Eze 20:16); a "spirit of whoredom" leads astray (Hos 4:12) (dep §2.1i, §2.3c) | Eze 20:16 | rejected H3988A | current | chapter 12 When the inner being goes wrong, Idols taken inside |
| C-91 | The calls on God to wake speak from how it feels when God does not act | Psalm 44:23 | reject H2186A | current | chapter 02 Life, breath and death, Sleep and waking (1 earlier telling(s) in the workbook) |
| C-94 | The righteous speak of going down to Sheol, as the wicked are said to | Genesis 37:35 | refused H3985 | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-95 | The manner of going down to Sheol is named: mourning, with sorrow, in peace, with blood, silently, alive | Genesis 37:35 | refused H3985 | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-105 | Deliverance from death is for something: walking before God among the living and telling of him | Job 33:26-30 | accepts H7521 | current | chapter 02 Life, breath and death, Delivered from death (1 earlier telling(s) in the workbook) |
| C-120 | Wisdom marks where the way to death ends, and some of what kills a person is named from within | Proverbs 21:25 | refuse H3985 | current | chapter 02 Life, breath and death, Life set before a person (3 earlier telling(s) in the workbook) |
| C-143 | Some are perishing now, set against being saved; what is set against perishing is eternal life | 2 Thessalonians 2:10 | refused G1209; refused G3756 | current | chapter 02 Life, breath and death, Death spoken of in more than one way (1 earlier telling(s) in the workbook) |
| C-146 | Inner things can perish: hope, endurance, courage (the heart), wisdom and truth | Jeremiah 7:28 | accept H3947H | current | chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook) |
| C-161 | That death changes how the living live: no longer for themselves, dead to sin, Christ living in them | Romans 12:1 | acceptable G2101 | current | chapter 02 Life, breath and death, Made alive (2 earlier telling(s) in the workbook) |
| C-163 | Scripture speaks of the death of the upright in its own words: precious, wished for, a refuge, in faith, bearing fruit, glorifying God | Hebrews 11:4 | more acceptable G4183 | current | chapter 02 Life, breath and death, Dying to the Lord (1 earlier telling(s) in the workbook) |
| C-165 | People hold to someone, or to something, even to death, and the readiness can fail | Luke 22:33-34; Mark 14:31 | deny G0533 | current | chapter 02 Life, breath and death, Dying to the Lord; chapter 10.10 Relating to others, Loyalty and honour (3 earlier telling(s) in the workbook) |
| C-176 | The humbling God does not take knowledge of is kept alongside self-pleasure and oppression and leaves the seen naked uncovered; Ahab's, against himself when the word came, was answered | Isaiah 58:3-7 | acceptable H7522 | current | chapter 10.7 Choosing and setting direction, Others around a choice; chapter 13.1 Divine, Choosing; chapter 10.14 Humility, A humbling God does not take knowledge of (3 earlier telling(s) in the workbook) |
| C-177 | What looks like lowering can puff a person up | Colossians 2:18 | disqualify G2603 | current | chapter 10.14 Humility, A humbling God does not take knowledge of (1 earlier telling(s) in the workbook) |
| C-188 | What God looks to is set against a religious act in the humility passages (the fast, the walk, the house, the broken heart), as in the other passages gathered in 13.1; the offering follows the broken heart | Isaiah 58:3-7 | acceptable H7522 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 11 Other sides of the inner being, What changes the character; chapter 13.1 Divine, Delight; chapter 10.14 Humility, Humility as a way of walking (6 earlier telling(s) in the workbook) |
| C-190 | Humility between people is a way of counting the other, worn toward them, and named with bearing with and forgiving | 1 Peter 5:5 | opposes G0498 | current | chapter 10.7 Choosing and setting direction, Being chosen; chapter 10.14 Humility, Toward one another; chapter 10.10 Relating to others, Humility toward one another (4 earlier telling(s) in the workbook) |
| C-194 | Submission among people is told with a ground that faces God and, where the passage goes on, with a duty on the other side | 1 Peter 5:3-5 | opposes G0498 | current | chapter 10.10 Relating to others, Holding authority over another; chapter 10.14 Humility, Submitting; chapter 10.10 Relating to others, Humility toward one another (5 earlier telling(s) in the workbook) |
| C-200 | The same lines of humility run through both Testaments; the New differs in emphasis, adding humility toward one another, and in one new thing, Christ, in whom God's lowering is done in a human life | James 4:6 | opposes G0498 | current | chapter 10.14 Humility, The Old Testament and the New (3 earlier telling(s) in the workbook) |
| C-201 | Humility changes character with who acts, toward whom, and to what end | Colossians 2:18 | disqualify G2603 | current | chapter 11 Other sides of the inner being, What changes the character; chapter 10.14 Humility, When humility changes character (2 earlier telling(s) in the workbook) |
| C-203 | God sees and answers the one who humbles himself, gives favor to the humble, humbles to test and do good, brings the proud low and looks on a humble estate | James 4:6 | opposes G0498 | current | chapter 13.1 Divine, Willing; chapter 13.1 Divine, Lowering himself (2 earlier telling(s) in the workbook) |
| C-218 | Pride claims a place that is God's: likeness to the Most High, a god's seat, his temple | 2 Thessalonians 2:4 | opposes G0480 | current | chapter 10.15 Pride, The heart that says what God says (1 earlier telling(s) in the workbook) |
| C-223 | Presumption acts on its own word where another word was given: speaking what God did not command, going up when told not to, not keeping the decision given | Nehemiah 9:16-17 | refused H3985 | current | chapter 10.7 Choosing and setting direction, Others around a choice; chapter 10.9 Relating to God, Kept from what would rule; chapter 10.15 Pride, The words; chapter 10.15 Pride, Pride and hearing; chapter 10.7 Choosing and setting direction, Presumption (5 earlier telling(s) in the workbook) |
| C-229 | Boasting in oneself is excluded because what is held was given: grace, gift, and God's choosing of the low | Romans 3:27 | excluded G1576 | current | chapter 10.15 Pride, The boast (1 earlier telling(s) in the workbook) |
| C-235 | In the proverbs pride brings its own fall, with no other hand named; elsewhere God brings it down | James 4:6 | opposes G0498 | current | chapter 10.14 Humility, The proud brought low, the lowly raised; chapter 10.15 Pride, Where it ends (3 earlier telling(s) in the workbook) |
| C-240 | God's majesty is challenged and not overturned; his laughter answers only those who rise against him and is never aimed at the weak | Proverbs 1:24-26 | refused H3985 | current | chapter 10.15 Pride, The words; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-250 | God's taking of the kingdom from Saul answers Saul's rejection of his word, in the same word | 1Sa 15:26 | rejected H3988A | current | chapter 13.1 Divine, Ruling (1 earlier telling(s) in the workbook) |
| C-256 | Even the prophet sent to choose formed his thought from appearance, and God's word corrected it | 1Sa 16:7 | rejected H3988A | current | chapter 04 The heart, The heart is hidden, and God sees it (1 earlier telling(s) in the workbook) |
| C-272 | The word psychikos carries no blame when it is said of the body and carries blame when it is said of a person | 1Cor 2:14 | accept G1209 | current | chapter 02 Life, breath and death, Sown and raised (1 earlier telling(s) in the workbook) |
| C-278 | The coming resurrection is given as a reason for how a person lives now: giving without return, enduring, self-control, steadfast work | Heb 11:35 | accept G4327 | current | chapter 02 Life, breath and death, Waited for (1 earlier telling(s) in the workbook) |
| C-287 | One Hebrew root, chul, is labour pain, trembling, anguish of heart, the dance, the whirling storm and patient waiting | Jer 5:3 | refused H3985 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 10.12 Fear, Fear in the body (2 earlier telling(s) in the workbook) |
| C-305 | Solomon on his throne showed honour upward to his mother, then refused her request | 1Ki 2:20 | refuse H7725L | current | chapter 10.10 Relating to others, Loyalty and honour (1 earlier telling(s) in the workbook) |
| C-311 | Adonijah's wish for Abishag was read by Solomon as the throne asked for again; the verses give Solomon's reading, not Adonijah's heart | 1Ki 2:16; 1Ki 2:17 | refuse H7725L | current | chapter 10.6 Wanting, A person (1 earlier telling(s) in the workbook) |
| C-318 | A promise not to refuse can be overridden by an oath | 1Ki 2:20 | refuse H7725L | current | chapter 10.5 Speaking, The oath (1 earlier telling(s) in the workbook) |
| C-331 | God chooses a place to set his name, and his eyes and heart are there; the people's offerings, joy, judgement and prayer turn toward it, and the choice can be cast off and made again. | 2Ki 23:27 | cast off H3988A | current | chapter 13.1 Divine, Choosing; chapter 10.7 Choosing and setting direction, Others around a choice |
| C-336 | Choosing the good rests on knowing and on being taught; the choice binds the one who makes it as a witness, and is held by holding fast. | Isa 7:15 | refuse H3988A | current | chapter 10.7 Choosing and setting direction, What a choice rests on; chapter 10.7 Choosing and setting direction, Holding a choice |
| C-338 | The choice is the chooser's own: it is placed on them and not on another, honoured by others, and given of one's own accord. | Job 34:33; 2Cor 8:17 | reject H3988A; accepted G1209 | current | chapter 10.7 Choosing and setting direction, A choice that is honoured; chapter 10.7 Choosing and setting direction, Choosing before God; chapter 10.7 Choosing and setting direction, Choices weighed by another |
| C-368 | The bed holds both deliberate plotting and meditation on God, and what fills the heart in the night shows by morning. | Psa 36:4 | reject H3988A | current | chapter 10.4 Thinking, The night and the bed |
| C-370 | Read together, the verses trace a path from a thought arising to the deed: lodging, reckoning, devising, the tongue, lips and eyes, then the hand and feet; no single verse lists it. | Psa 36:4 | reject H3988A | current | chapter 10.0 The inner being at work, From a thought to a deed; chapter 10.5 Speaking, The tongue, the lips and the eyes devise |
| C-372 | Thinking reckons worth: people reckon wrongly, being reckoned is felt from inside, God reckons truly and counts righteousness or guilt to a person, and reckoning serves release or is laid aside in trust. | Lev 7:18 | accepted H7521 | current | chapter 10.4 Thinking, What thinking does |
| C-380 | The Spirit intercedes according to God's will, the purpose is turned toward those who love him, and a person can reject it for himself. | Luk 7:30 | rejected G0114 | current | chapter 13.1 Divine, Purposing |

### 5.3 The narrative sections that tell these claims (53)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 8 | 02 Life, breath and death | Life set before a person | C-120 |
| 13 | 02 Life, breath and death | Death in the living | C-146 |
| 14 | 02 Life, breath and death | Sleep and waking | C-91 |
| 20 | 02 Life, breath and death | Delivered from death | C-105 |
| 21 | 02 Life, breath and death | Made alive | C-161 |
| 22 | 02 Life, breath and death | Dying to the Lord | C-163, C-165 |
| 24 | 02 Life, breath and death | Sown and raised | C-272 |
| 27 | 02 Life, breath and death | Waited for | C-278 |
| 50 | 04 The heart | The heart is hidden, and God sees it | C-256 |
| 92 | 10.0 The inner being at work | From a thought to a deed | C-370 |
| 137 | 10.4 Thinking | What thinking does | C-372 |
| 140 | 10.4 Thinking | The night and the bed | C-368 |
| 149 | 10.5 Speaking | The tongue, the lips and the eyes devise | C-370 |
| 158 | 10.5 Speaking | The oath | C-318 |
| 176 | 10.6 Wanting | A person | C-311 |
| 184 | 10.7 Choosing and setting direction | What a choice rests on | C-336 |
| 187 | 10.7 Choosing and setting direction | Choosing before God | C-338 |
| 188 | 10.7 Choosing and setting direction | Being chosen | C-190 |
| 189 | 10.7 Choosing and setting direction | Others around a choice | C-176, C-223, C-331, C-340 |
| 191 | 10.7 Choosing and setting direction | A choice that is honoured | C-338 |
| 195 | 10.7 Choosing and setting direction | Holding a choice | C-336 |
| 197 | 10.7 Choosing and setting direction | Willing | C-349 |
| 200 | 10.7 Choosing and setting direction | Choices weighed by another | C-338 |
| 214 | 10.9 Relating to God | Kept from what would rule | C-223 |
| 230 | 10.10 Relating to others | Holding authority over another | C-194 |
| 232 | 10.10 Relating to others | Loyalty and honour | C-165, C-305 |
| 296 | 11 Other sides of the inner being | 4. One word, opposite values | C-188, C-287 |
| 297 | 11 Other sides of the inner being | What changes the character | C-188, C-201 |
| 313 | 12 When the inner being goes wrong | Idols taken inside | 9-3 |
| 323 | 13.1 Divine | Choosing | C-176, C-331, C-340 |
| 324 | 13.1 Divine | Purposing | C-380 |
| 325 | 13.1 Divine | Willing | C-203 |
| 326 | 13.1 Divine | Delight | C-188 |
| 329 | 13.1 Divine | Ruling | C-250 |
| 348 | 02 Life, breath and death | Going down to Sheol | C-94, C-95 |
| 349 | 02 Life, breath and death | Death spoken of in more than one way | C-143 |
| 362 | 10.14 Humility | A humbling God does not take knowledge of | C-176, C-177 |
| 364 | 10.14 Humility | The proud brought low, the lowly raised | C-235 |
| 366 | 10.14 Humility | Humility as a way of walking | C-188 |
| 368 | 10.14 Humility | Toward one another | C-190 |
| 369 | 10.14 Humility | Submitting | C-194 |
| 371 | 10.14 Humility | The Old Testament and the New | C-200 |
| 372 | 10.14 Humility | When humility changes character | C-201 |
| 377 | 10.10 Relating to others | Humility toward one another | C-190, C-194 |
| 380 | 13.1 Divine | Lowering himself | C-203 |
| 382 | 10.15 Pride | The words | C-223, C-240 |
| 384 | 10.15 Pride | The heart that says what God says | C-218 |
| 385 | 10.15 Pride | Pride and hearing | C-223 |
| 387 | 10.15 Pride | The boast | C-229 |
| 389 | 10.15 Pride | Where it ends | C-235 |
| 393 | 10.7 Choosing and setting direction | Presumption | C-223 |
| 395 | 13.1 Divine | Majesty | C-240 |
| 403 | 10.12 Fear | Fear in the body | C-287 |

## 6. Phrases attached to the collection (7)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| accept circumcision | 6254 | english route: word accept | 1 | 0 | 0 | 0 |
| accepted me | 6255 | english route: word accepted | 1 | 0 | 0 | 0 |
| accepts circumcision | 6256 | english route: word accepts | 1 | 0 | 0 | 0 |
| cast off | 10759 | cast off does not belong where it was: it goes to reject (long tail) | 9 | 0 | 7 | 7 |
| more acceptable | 7733 | english route: word acceptable | 2 | 0 | 2 | 2 |
| refused him | 8031 | english route: word refused | 1 | 0 | 0 | 0 |
| reject him | 8034 | english route: word reject | 1 | 0 | 0 | 0 |

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

