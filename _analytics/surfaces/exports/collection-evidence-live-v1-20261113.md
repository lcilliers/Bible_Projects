# Collection evidence report: live

Generated 2026-11-13T19:02:17Z by run RUN-20261113_190212_368-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-live-v1-20261113.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection live at a glance

Status confirmed; core term 318; created 2026-11-08T04:48:28Z, updated 2026-11-10T16:03:22Z; run RUN-20261110_160322_065-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (15)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| alive | word | synonym | alive | placed | 84 | 77 |
| come to life | phrase | phrase | come to life | placed | 1 | 1 |
| dead | word | opposite | dead | placed | 305 | 247 |
| deadly | word | opposite | dead | listed_only | 9 | 9 |
| deadly peril | phrase | phrase | deadly peril | placed | 1 | 1 |
| half dead | phrase | phrase | half dead | placed | 1 | 1 |
| live | word | core | live | placed | 336 | 290 |
| live on | phrase | phrase | live on | placed | 2 | 2 |
| live peaceably | phrase | phrase | live peaceably | placed | 1 | 1 |
| live quietly | phrase | phrase | live quietly | placed | 1 | 1 |
| lived | word | synonym | live | placed | 253 | 228 |
| lives | word | synonym | live | placed | 151 | 124 |
| lives on | phrase | phrase | lives on | placed | 1 | 1 |
| living | word | synonym | live | placed | 142 | 132 |
| remained alive | phrase | phrase | remained alive | placed | 2 | 1 |

### 2.2 The Strong's codes behind the members (100)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H2421 חָיָה cha.yah "to live" | 195 | 3 | 189 | live 131, lived 39, alive 20, lives 5 | none | 89 |
| H2416A חַי chay "alive" | 191 | 17 | 190 | living 64, lives 49, live 41, alive 37 | none | 129 |
| H3427 יָשַׁב ya.shav "to dwell" | 177 | 16 | 182 | lived 146, live 29, living 2 | none | 0 |
| G2198 ζάω zaō "to live" | 134 | 0 | 118 | live 54, living 41, alive 18, lives 16, lived 4, come to life 1 | none | 95 |
| G3498 νεκρός nekros "dead" | 121 | 0 | 113 | dead 121 | none | 0 |
| H4191 מוּת mut "to die" | 89 | 30 | 106 | dead 89 | none | 55 |
| H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | 24 | 10 | 33 | lives 22, alive 1, deadly 1 | none | 19 |
| H2416E חַיִּים chay.yim "life" | 18 | 2 | 20 | live 11, lives 3, lived 2, alive 1, living 1 | none | 17 |
| G2730 κατοικέω katoikeō "to dwell" | 14 | 0 | 13 | lived 8, live 3, living 3 | none | 0 |
| H1481A גּוּר gur "to sojourn" | 10 | 4 | 14 | live 6, lives 4 | none | 0 |
| G0599 ἀποθνήσκω apothnēskō "to die" | 8 | 0 | 8 | dead 8 | none | 5 |
| G2226 ζῷον zōon "living thing" | 8 | 0 | 8 | living 8 | none | 0 |
| G2348 θνῄσκω thnēskō "to die/be dead" | 6 | 0 | 6 | dead 6 | none | 0 |
| H7931 שָׁכַן sha.khan "to dwell" | 6 | 2 | 8 | lived 4, live 2 | none | 0 |
| G5590H ψυχή psuchē "soul: life" | 5 | 0 | 5 | lives 5 | none | 3 |
| H2417 חַי chay "living" | 5 | 1 | 6 | living 4, lives 1 | none | 0 |
| H2418 חֲיָא cha.ya "to live" | 5 | 0 | 5 | live 5 | none | 0 |
| G1510 εἰμί eimi "to be" | 4 | 0 | 4 | live 3, lived 1 | none | 0 |
| H5315M נֶ֫פֶשׁ ne.phesh "soul: dead" | 4 | 0 | 4 | dead 4 | none | 3 |
| H7496 רְפָאִים re.pha.im "shade" | 4 | 0 | 4 | dead 4 | none | 3 |
| G0979 βίος bios "life" | 3 | 0 | 3 | live on 2, living 1 | none | 2 |
| H3117G יוֹם yom "day" | 3 | 1 | 4 | live 3 | none | 0 |
| H4186 מוֹשָׁב mo.shav "seat" | 3 | 1 | 4 | lived 3 | none | 0 |
| H4194 מָ֫וֶת ma.vet "death" | 3 | 1 | 4 | dead 2, deadly 1 | none | 1 |
| G0390 ἀναστρέφω anastrefō "to live/return" | 2 | 0 | 2 | live 1, lived 1 | none | 0 |
| G1096 γίνομαι ginomai "to be" | 2 | 0 | 2 | lived 1, lives 1 | none | 0 |
| G3306 μένω menō "to stay" | 2 | 0 | 2 | lived 2 | none | 0 |
| G3499 νεκρόω nekroō "to put to death" | 2 | 0 | 2 | dead 2 | none | 2 |
| G3611 οἰκέω oikeō "to dwell" | 2 | 0 | 2 | live 2 | none | 0 |
| G4800 συζάω suzaō "to live together" | 2 | 0 | 2 | live 2 | none | 0 |
| G0391 ἀναστροφή anastrofē "behaviour" | 1 | 0 | 1 | lives 1 | none | 0 |
| G0740 ἄρτος artos "bread" | 1 | 0 | 1 | living 1 | none | 0 |
| G0980 βιόω bioō "to live" | 1 | 0 | 1 | live 1 | none | 0 |
| G1460 ἐγκατοικέω enkatoikeō "to live among" | 1 | 0 | 1 | lived 1 | none | 0 |
| G1514 εἰρηνεύω eirēneuō "be at peace" | 1 | 0 | 1 | live peaceably 1 | none | 1 |
| G2253 ἡμιθανής hēmithanēs "half-dead" | 1 | 0 | 1 | half dead 1 | none | 0 |
| G2270 ἡσυχάζω hēsuchazō "be quiet/give up" | 1 | 0 | 1 | live quietly 1 | none | 1 |
| G2286 θανάσιμος thanasimos "deadly" | 1 | 0 | 1 | deadly 1 | none | 0 |
| G2287 θανατήφορος thanatēforos "deadly" | 1 | 0 | 1 | deadly 1 | none | 0 |
| G2288 θάνατος thanatos "death" | 1 | 1 | 2 | deadly peril 1 | none | 2 |
| G3348 μετέχω metechō "to share" | 1 | 0 | 1 | lives on 1 | none | 0 |
| G3939 παροικέω paroikeō "be a stranger" | 1 | 0 | 1 | live 1 | none | 0 |
| G4924 συνοικέω sunoikeō "to live with" | 1 | 0 | 1 | live 1 | none | 0 |
| G5225 ὑπάρχω huparchō "be already" | 1 | 0 | 1 | live 1 | none | 0 |
| H0398 אָכַל a.khal "to eat" | 1 | 0 | 1 | lived 1 | none | 0 |
| H1100H בְּלִיַּ֫עַל be.liy.ya.al "Belial: destruction" | 1 | 0 | 1 | deadly 1 | none | 0 |
| H1753 דּוּר dur "to dwell" | 1 | 0 | 1 | lived 1 | none | 0 |
| H1942 הַוָּה hav.vah "desire" | 1 | 0 | 1 | deadly 1 | none | 0 |
| H1980I הָלַךְ ha.lakh "to go: walk" | 1 | 0 | 1 | lived 1 | none | 0 |
| H2416C חַיָּה chay.yah "living thing" | 1 | 0 | 1 | lives 1 | none | 1 |
| H2424 חַיּוּת chay.yut "living" | 1 | 0 | 1 | living 1 | none | 0 |
| H2425 חָיַי cha.yay "to live" | 1 | 0 | 1 | lives 1 | none | 1 |
| H2506A חֵ֫לֶק che.leq "portion" | 1 | 0 | 1 | lives 1 | none | 0 |
| H4033 מָגוֹר ma.gor "sojourning" | 1 | 0 | 1 | live 1 | none | 0 |
| H4241 מִחְיָה mich.yah "recovery" | 1 | 1 | 2 | living 1 | none | 0 |
| H4908 מִשְׁכָּן mish.kan "tabernacle" | 1 | 0 | 1 | lived 1 | none | 0 |
| H7451A רַע ra "bad: harmful" | 1 | 0 | 1 | deadly 1 | none | 0 |
| H7703 שָׁדַד sha.dad "to ruin" | 1 | 0 | 1 | dead 1 | none | 0 |
| H7819A שָׁחַט sha.chat "to slaughter" | 1 | 0 | 1 | deadly 1 | none | 0 |
| H8463 תַּחֲלֻאִים ta.cha.lu.im "disease" | 1 | 0 | 1 | deadly 1 | none | 0 |
| G0737 ἄρτι arti "now" | 0 | 1 | 1 |  | none | 0 |
| G1722 ἐν en "in/on/among" | 0 | 1 | 1 |  | none | 0 |
| G2192 ἔχω echō "to have/be" | 0 | 2 | 2 |  | none | 0 |
| G2193 ἕως heōs "until" | 0 | 1 | 1 |  | none | 0 |
| G2731 κατοίκησις katoikēsis "dwelling" | 0 | 1 | 1 |  | none | 0 |
| G3303 μέν men "on the other hand" | 0 | 1 | 1 |  | none | 0 |
| G5590G ψυχή psuchē "soul" | 0 | 1 | 1 |  | none | 1 |
| H0369 אַ֫יִן a.yin "nothing" | 0 | 1 | 1 |  | none | 0 |
| H0413 אֶל el "to[wards]" | 0 | 7 | 7 |  | none | 0 |
| H0518A אִם im "if" | 0 | 1 | 1 |  | none | 0 |
| H0518B [כִּי] אם   "if: except" | 0 | 2 | 2 |  | none | 0 |
| H0589 אֲנִי a.ni "I" | 0 | 1 | 1 |  | none | 0 |
| H0595 אָֽנֹכִ֫י a.no.khi "I" | 0 | 1 | 1 |  | none | 0 |
| H0754 אַרְכָֿא ar.kha "lengthening" | 0 | 1 | 1 |  | none | 0 |
| H0834A אֲשֶׁר a.sher "which" | 0 | 10 | 10 |  | none | 0 |
| H0853 אֵת et "[Obj.]" | 0 | 18 | 16 |  | none | 0 |
| H0854 אֵת et "with" | 0 | 2 | 1 |  | none | 0 |
| H0859A אַתָּ֫ה at.tah "you [m.s.]" | 0 | 1 | 1 |  | none | 0 |
| H0996G בַּ֫יִן ba.yin "between" | 0 | 2 | 2 |  | none | 0 |
| H1121A בֵּן ben "son: child" | 0 | 1 | 1 |  | none | 0 |
| H1571 גַּם gam "also" | 0 | 1 | 1 |  | none | 0 |
| H1768 דִּי di "that" | 0 | 1 | 1 |  | none | 0 |
| H1931 הוּא hu "he/she/it" | 0 | 7 | 7 |  | none | 0 |
| H1961 הָיָה ha.yah "to be" | 0 | 6 | 6 |  | none | 0 |
| H1992 הֵ֫מָּה hem.mah "they [masc.]" | 0 | 2 | 2 |  | none | 0 |
| H2009 הִנֵּה hin.neh "behold" | 0 | 1 | 1 |  | none | 0 |
| H2088 זֶה zeh "this" | 0 | 2 | 2 |  | none | 0 |
| H3117K יוֹם yom "day: always" | 0 | 1 | 1 |  | none | 0 |
| H3488 יְתִב ye.tiv "to dwell" | 0 | 1 | 1 |  | none | 0 |
| H3588A כִּי ki "for" | 0 | 15 | 15 |  | none | 0 |
| H3588B כִּי [אם] ki m "that if: except" | 0 | 1 | 1 |  | none | 0 |
| H3605 כֹּל kol "all" | 0 | 2 | 2 |  | none | 0 |
| H3644G כְּמוֹ ke.mo "like" | 0 | 1 | 1 |  | none | 0 |
| H4100 מָה mah "what?" | 0 | 1 | 1 |  | none | 0 |
| H4480A מִן־ min- "from" | 0 | 2 | 2 |  | none | 0 |
| H4616 מַ֫עַן ma.an "because" | 0 | 2 | 2 |  | none | 0 |
| H5750 עוֹד od "still" | 0 | 1 | 1 |  | none | 0 |
| H5921A עַל al "upon" | 0 | 8 | 8 |  | none | 0 |
| H7794 שׁוֹר shor "cattle" | 0 | 1 | 1 |  | none | 0 |
| H8033G שָׁם sham "there" | 0 | 6 | 6 |  | none | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.61.

### 3.1 H2421 חָיָה cha.yah "to live": 195 own occurrences in 186 verses

- **Meaning as stored:** Hebrew; native word חָיָה, transliteration cha.yah; STEP gloss "to live"; sense head "to live" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2421):** to live, have life, remain alive, sustain life, live prosperously, liv ... (cut; the whole text is in the workbook).
- **Related terms (24):** H2416A chay "alive"; H2416B chay "kinsfolk"; H2416C chay.yah "living thing"; H2416D chay.yah "community"; H2416E chay.yim "life"; H2418 cha.ya "to live"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 291; verses STEP attests 257; verse_lexical rows the parse found 282.

- **Carried by the member words:** live (131), lived (39), alive (20), lives (5).
- **Engagement of these occurrences:** none recorded 195.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 6:19 | alive | HVhcc | none recorded | - | 0 | And of every living thing of all flesh, you shall bring two of every sort into the ark to keep them **alive** with you. They shall be male and female. |
| Gen 6:20 | alive | HVhcc | none recorded | - | 0 | Of the birds according to their kinds, and of the animals according to their kinds, of every creeping thing of the ground, according to its kind, two of every sort shall come in to you to keep them **alive**. |
| Gen 7:3 | alive | HVpcc | none recorded | - | 0 | and seven pairs of the birds of the heavens also, male and female, to keep their offspring **alive** on the face of all the earth. |
| Gen 45:7 | alive | HVhcc | none recorded | - | 0 | And God sent me before you to preserve for you a remnant on earth, and to keep **alive** for you many survivors. |
| Gen 50:20 | alive | HVhcc | none recorded | 12247, 18485, 18790 | 0 | As for you, you meant evil against me, but God meant it for good, to bring it about that many people should be kept **alive**, as they are today. |
| Num 14:38 | alive | HVqp3cp | none recorded | - | 0 | Of those men who went to spy out the land, only Joshua the son of Nun and Caleb the son of Jephunneh remained **alive**. |
| Deu 6:24 | alive | HVpcc | none recorded | 12247, 18485 | 0 | And the Lord commanded us to do all these statutes, to fear the Lord our God, for our good always, that he might preserve us **alive**, as we are this day. |
| Deu 20:16 | alive | HVpi2ms | none recorded | - | 0 | But in the cities of these peoples that the Lord your God is giving you for an inheritance, you shall save **alive** nothing that breathes, |
| Deu 32:39 | alive | HVpu1cs | none recorded | 12245, 18485, 18791, 18816 | 0 | “‘ See now that I, even I, am he, and there is no god beside me; I kill and I make **alive**; I wound and I heal; and there is none that can deliver out of my hand. |
| Jos 14:10 | alive | HVhp3ms | none recorded | - | 0 | And now, behold, the Lord has kept me **alive**, just as he said, these forty-five years since the time that the Lord spoke this word to Moses, while Israel walked in the wilderness. And now, behold, I am this day eighty-five years old. |
| 1Sa 27:9 | alive | HVpi3ms | none recorded | - | 0 | And David would strike the land and would leave neither man nor woman **alive**, but would take away the sheep, the oxen, the donkeys, the camels, and the garments, and come back to Achish. |
| 2Ki 5:7 | alive | HVhcc | none recorded | 12245, 18485, 18791 | 0 | And when the king of Israel read the letter, he tore his clothes and said, “Am I God, to kill and to make **alive**, that this man sends word to me to cure a man of his leprosy? Only consider, and see how he is seeking a quarrel with me.” |
| Neh 5:2 | alive | HVqu1cp | none recorded | 18788 | 0 | For there were those who said, “With our sons and our daughters, we are many. So let us get grain, that we may eat and keep **alive**.” |
| Job 36:6 | alive | HVpi3ms | none recorded | 12247, 18485, 18790 | 0 | He does not keep the wicked **alive**, but gives the afflicted their right. |
| Psa 22:29 | alive | HVpp3ms | none recorded | 12241, 18790 | 0 | All the prosperous of the earth eat and worship; before him shall bow all who go down to the dust, even the one who could not keep himself **alive**. |
| Psa 33:19 | alive | HVpcc | none recorded | 12247, 16179, 18485, 18790 | 0 | that he may deliver their soul from death and keep them **alive** in famine. |
| Psa 41:2 | alive | HVpu3ms | none recorded | 12247, 18790 | 0 | the Lord protects him and keeps him **alive**; he is called blessed in the land; you do not give him up to the will of his enemies. |
| Jer 49:11 | alive | HVpi1cs | none recorded | - | 0 | Leave your fatherless children; I will keep them **alive**; and let your widows trust in me.” |
| Eze 13:18 | alive | HVpi2fp | none recorded | 16089, 18710, 18802 | 0 | and say, Thus says the Lord God: Woe to the women who sew magic bands upon all wrists, and make veils for the heads of persons of every stature, in the hunt for souls! Will you hunt down souls belonging to my people and keep your own souls **alive**? |
| Eze 13:19 | alive | HVpcc | none recorded | 12269, 16089, 16610, 16727, 18710, 18802 | 0 | You have profaned me among my people for handfuls of barley and for pieces of bread, putting to death souls who should not die and keeping **alive** souls who should not live, by your lying to my people, who listen to lies. |
| Gen 3:22 | live | HVqq3ms | none recorded | 12272, 12364 | 0 | Then the Lord God said, “ Behold, the man has become like one of us in knowing good and evil. Now, lest he reach out his hand and take also of the tree of life and eat, and **live** forever —” |
| Gen 12:12 | live | HVpi3mp | none recorded | - | 0 | and when the Egyptians see you, they will say, ‘This is his wife.’ Then they will kill me, but they will let you **live**. |
| Gen 17:18 | live | HVqi3ms | none recorded | 12244 | 0 | And Abraham said to God, “Oh that Ishmael might **live** before you!” |
| Gen 20:7 | live | HVqv2ms | none recorded | - | 0 | Now then, return the man’s wife, for he is a prophet, so that he will pray for you, and you shall **live**. But if you do not return her, know that you shall surely die, you and all who are yours.” |
| Gen 27:40 | live | HVqi2ms | none recorded | - | 0 | By your sword you shall **live**, and you shall serve your brother; but when you grow restless you shall break his yoke from your neck.” |
| Gen 31:32 | live | HVqi3ms | none recorded | - | 0 | Anyone with whom you find your gods shall not **live**. In the presence of our kinsmen point out what I have that is yours, and take it.” Now Jacob did not know that Rachel had stolen them. |
| Gen 42:2 | live | HVqu1cp | none recorded | 18244 | 0 | And he said, “ Behold, I have heard that there is grain for sale in Egypt. Go down and buy grain for us there, that we may **live** and not die.” |
| Gen 42:18 | live | HVqv2mp | none recorded | 12274 | 0 | On the third day Joseph said to them, “ Do this and you will **live**, for I fear God: |
| Gen 43:8 | live | HVqu1cp | none recorded | - | 0 | And Judah said to Israel his father, “ Send the boy with me, and we will arise and go, that we may **live** and not die, both we and you and also our little ones. |
| Gen 47:19 | live | HVqu1cp | none recorded | - | 0 | Why should we die before your eyes, both we and our land? Buy us and our land for food, and we with our land will be servants to Pharaoh. And give us seed that we may **live** and not die, and that the land may not be desolate.” |
| Exo 1:16 | live | HVqq3fs | none recorded | 18789 | 0 | “ When you serve as midwife to the Hebrew women and see them on the birthstool, if it is a son, you shall kill him, but if it is a daughter, she shall **live**.” |
| Exo 1:17 | live | HVpw3fp | none recorded | 12274, 18789 | 0 | But the midwives feared God and did not do as the king of Egypt commanded them, but let the male children **live**. |
| Exo 1:18 | live | HVpw2fp | none recorded | 18789 | 0 | So the king of Egypt called the midwives and said to them, “ Why have you done this, and let the male children **live**?” |
| Exo 1:22 | live | HVpi2mp | none recorded | 18789 | 0 | Then Pharaoh commanded all his people, “ Every son that is born to the Hebrews you shall cast into the Nile, but you shall let every daughter **live**.” |
| Exo 19:13 | live | HVqi3ms | none recorded | - | 0 | No hand shall touch him, but he shall be stoned or shot; whether beast or man, he shall not **live**.’ When the trumpet sounds a long blast, they shall come up to the mountain.” |
| Exo 22:18 | live | HVpi2ms | none recorded | - | 0 | “You shall not permit a sorceress to **live**. |
| Exo 33:20 | live | HVqq3ms | none recorded | 12270 | 0 | But,” he said, “you cannot see my face, for man shall not see me and **live**.” |
| Lev 18:5 | live | HVqq3ms | none recorded | 12262, 18801 | 0 | You shall therefore keep my statutes and my rules; if a person does them, he shall **live** by them: I am the Lord. |
| Lev 25:35 | live | HVqq3ms | none recorded | - | 0 | “If your brother becomes poor and cannot maintain himself with you, you shall support him as though he were a stranger and a sojourner, and he shall **live** with you. |
| Lev 25:36 | live | HVqq3ms | none recorded | - | 0 | Take no interest from him or profit, but fear your God, that your brother may **live** beside you. |
| Num 4:19 | live | HVqq3cp | none recorded | - | 0 | but deal thus with them, that they may **live** and not die when they come near to the most holy things: Aaron and his sons shall go in and appoint them each to his task and to his burden, |
| Num 21:8 | live | HVqq3ms | none recorded | 16167 | 0 | And the Lord said to Moses, “ Make a fiery serpent and set it on a pole, and everyone who is bitten, when he sees it, shall **live**.” |
| Num 21:9 | live | HVqq3ms | none recorded | 16167 | 0 | So Moses made a bronze serpent and set it on a pole. And if a serpent bit anyone, he would look at the bronze serpent and **live**. |
| Num 22:33 | live | HVhp1cs | none recorded | - | 0 | The donkey saw me and turned aside before me these three times. If she had not turned aside from me, surely just now I would have killed you and let her **live**.” |
| Num 24:23 | live | HVqi3ms | none recorded | - | 0 | And he took up his discourse and said, “ Alas, who shall **live** when God does this? |
| Deu 4:1 | live | HVqj2mp | none recorded | - | 0 | “And now, O Israel, listen to the statutes and the rules that I am teaching you, and do them, that you may **live**, and go in and take possession of the land that the Lord, the God of your fathers, is giving you. |
| Deu 4:33 | live | HVqw3ms | none recorded | - | 0 | Did any people ever hear the voice of a god speaking out of the midst of the fire, as you have heard, and still **live**? |
| Deu 5:24 | live | HVqq3ms | none recorded | 12270 | 0 | And you said, ‘ Behold, the Lord our God has shown us his glory and greatness, and we have heard his voice out of the midst of the fire. This day we have seen God speak with man, and man still **live**. |
| Deu 5:33 | live | HVqj2mp | none recorded | - | 0 | You shall walk in all the way that the Lord your God has commanded you, that you may **live**, and that it may go well with you, and that you may live long in the land that you shall possess. |
| Deu 8:1 | live | HVqj2mp | none recorded | - | 0 | “The whole commandment that I command you today you shall be careful to do, that you may **live** and multiply, and go in and possess the land that the Lord swore to give to your fathers. |
| Deu 8:3 | live | HVqi3ms | none recorded | 12262, 15345, 18801 | 0 | And he humbled you and let you hunger and fed you with manna, which you did not know, nor did your fathers know, that he might make you know that man does not **live** by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| Deu 16:20 | live | HVqj2ms | none recorded | 12262, 18712 | 0 | Justice, and only justice, you shall follow, that you may **live** and inherit the land that the Lord your God is giving you. |
| Deu 19:5 | live | HVqq3ms | none recorded | - | 0 | as when someone goes into the forest with his neighbor to cut wood, and his hand swings the axe to cut down a tree, and the head slips from the handle and strikes his neighbor so that he dies — he may flee to one of these cities and **live**, |
| Deu 30:16 | live | HVqq2ms | none recorded | 18723 | 0 | If you obey the commandments of the Lord your God that I command you today, by loving the Lord your God, by walking in his ways, and by keeping his commandments and his statutes and his rules, then you shall **live** and multiply, and the Lord your God will bless you in the land that you are entering to take possession of it. |
| Deu 30:19 | live | HVqj2ms | none recorded | 12263, 12338, 18801 | 0 | I call heaven and earth to witness against you today, that I have set before you life and death, blessing and curse. Therefore choose life, that you and your offspring may **live**, |
| Deu 33:6 | live | HVqj3ms | none recorded | 18804 | 0 | “Let Reuben **live**, and not die, but let his men be few.” |
| Jos 6:17 | live | HVqi3fs | none recorded | - | 0 | And the city and all that is within it shall be devoted to the Lord for destruction. Only Rahab the prostitute and all who are with her in her house shall **live**, because she hid the messengers whom we sent. |
| Jos 9:15 | live | HVpcc | none recorded | - | 0 | And Joshua made peace with them and made a covenant with them, to let them **live**, and the leaders of the congregation swore to them. |
| Jos 9:20 | live | HVhaa | none recorded | 12275, 13558, 13856, 14559, 18789 | 0 | This we will do to them: let them **live**, lest wrath be upon us, because of the oath that we swore to them.” |
| Jos 9:21 | live | HVqi3mp | none recorded | 14091 | 0 | And the leaders said to them, “Let them **live**.” So they became cutters of wood and drawers of water for all the congregation, just as the leaders had said of them. |
| 1Sa 10:24 | live | HVqj3ms | none recorded | - | 0 | And Samuel said to all the people, “Do you see him whom the Lord has chosen? There is none like him among all the people.” And all the people shouted, “Long **live** the king!” |
| 2Sa 1:10 | live | HVqi3ms | none recorded | - | 0 | So I stood beside him and killed him, because I was sure that he could not **live** after he had fallen. And I took the crown that was on his head and the armlet that was on his arm, and I have brought them here to my lord.” |
| 2Sa 12:22 | live | HVqq3ms | none recorded | 12244, 18800 | 0 | He said, “While the child was still alive, I fasted and wept, for I said, ‘ Who knows whether the Lord will be gracious to me, that the child may **live**?’ |
| 2Sa 16:16 | live | HVqj3ms | none recorded | - | 0 | And when Hushai the Archite, David’s friend, came to Absalom, Hushai said to Absalom, “Long **live** the king! Long live the king!” |
| 2Sa 16:16 | live | HVqj3ms | none recorded | - | 0 | And when Hushai the Archite, David’s friend, came to Absalom, Hushai said to Absalom, “Long **live** the king! Long live the king!” |
| 1Ki 1:25 | live | HVqj3ms | none recorded | 18804 | 0 | For he has gone down this day and has sacrificed oxen, fattened cattle, and sheep in abundance, and has invited all the king’s sons, the commanders of the army, and Abiathar the priest. And behold, they are eating and drinking before him, and saying, ‘Long **live** King Adonijah!’ |
| 1Ki 1:31 | live | HVqj3ms | none recorded | 18804 | 0 | Then Bathsheba bowed with her face to the ground and paid homage to the king and said, “May my lord King David **live** forever!” |
| 1Ki 1:34 | live | HVqj3ms | none recorded | 18804 | 0 | And let Zadok the priest and Nathan the prophet there anoint him king over Israel. Then blow the trumpet and say, ‘Long **live** King Solomon!’ |
| 1Ki 1:39 | live | HVqj3ms | none recorded | 18804 | 0 | There Zadok the priest took the horn of oil from the tent and anointed Solomon. Then they blew the trumpet, and all the people said, “Long **live** King Solomon!” |
| 1Ki 20:32 | live | HVqj3fs | none recorded | 16087, 18789 | 0 | So they tied sackcloth around their waists and put ropes on their heads and went to the king of Israel and said, “Your servant Ben-hadad says, ‘ Please, let me **live**.’” And he said, “Does he still live? He is my brother.” |
| 2Ki 4:7 | live | HVqi2fs | none recorded | - | 0 | She came and told the man of God, and he said, “ Go, sell the oil and pay your debts, and you and your sons can **live** on the rest.” |
| 2Ki 7:4 | live | HVqi1cp | none recorded | 18244 | 0 | If we say, ‘Let us enter the city,’ the famine is in the city, and we shall die there. And if we sit here, we die also. So now come, let us go over to the camp of the Syrians. If they spare our lives we shall **live**, and if they kill us we shall but die.” |
| 2Ki 10:19 | live | HVqi3ms | none recorded | - | 0 | Now therefore call to me all the prophets of Baal, all his worshipers and all his priests. Let none be missing, for I have a great sacrifice to offer to Baal. Whoever is missing shall not **live**.” But Jehu did it with cunning in order to destroy the worshipers of Baal. |
| 2Ki 11:12 | live | HVqj3ms | none recorded | - | 0 | Then he brought out the king’s son and put the crown on him and gave him the testimony. And they proclaimed him king and anointed him, and they clapped their hands and said, “Long **live** the king!” |
| 2Ki 18:32 | live | HVqv2mp | none recorded | - | 0 | until I come and take you away to a land like your own land, a land of grain and wine, a land of bread and vineyards, a land of olive trees and honey, that you may **live**, and not die. And do not listen to Hezekiah when he misleads you by saying, “The Lord will deliver us.” |
| 2Ch 23:11 | live | HVqj3ms | none recorded | - | 0 | Then they brought out the king’s son and put the crown on him and gave him the testimony. And they proclaimed him king, and Jehoiada and his sons anointed him, and they said, “Long **live** the king.” |
| Neh 2:3 | live | HVqi3ms | none recorded | 18804 | 0 | I said to the king, “Let the king **live** forever! Why should not my face be sad, when the city, the place of my fathers ’ graves, lies in ruins, and its gates have been destroyed by fire?” |
| Neh 6:11 | live | HVqq3ms | none recorded | - | 0 | But I said, “Should such a man as I run away? And what man such as I could go into the temple and **live**? I will not go in.” |
| Neh 9:29 | live | HVqq3ms | none recorded | - | 0 | And you warned them in order to turn them back to your law. Yet they acted presumptuously and did not obey your commandments, but sinned against your rules, which if a person does them, he shall **live** by them, and they turned a stubborn shoulder and stiffened their neck and would not obey. |
| Est 4:11 | live | HVqq3ms | none recorded | 18789 | 0 | “ All the king’s servants and the people of the king’s provinces know that if any man or woman goes to the king inside the inner court without being called, there is but one law —to be put to death, except the one to whom the king holds out the golden scepter so that he may **live**. But as for me, I have not been called to come in to the king these thirty days.” |
| Job 7:16 | live | HVqi1cs | none recorded | 12273, 18805, 20363 | 0 | I loathe my life; I would not **live** forever. Leave me alone, for my days are a breath. |
| Job 14:14 | live | HVqi3ms | none recorded | 12256, 12376, 18816 | 0 | If a man dies, shall he **live** again? All the days of my service I would wait, till my renewal should come. |
| Job 21:7 | live | HVqi3mp | none recorded | 12276 | 0 | Why do the wicked **live**, reach old age, and grow mighty in power? |
| Psa 22:26 | live | HVqj3ms | none recorded | 12241, 15405, 16053, 16473, 16712, 17092, 17109, 18818, 19344 | 0 | The afflicted shall eat and be satisfied; those who seek him shall praise the Lord! May your hearts **live** forever! |
| Psa 49:9 | live | HVqj3ms | none recorded | 12272, 12390 | 0 | that he should **live** on forever and never see the pit. |
| Psa 72:15 | live | HVqj3ms | none recorded | - | 0 | Long may he **live**; may gold of Sheba be given to him! May prayer be made for him continually, and blessings invoked for him all the day! |
| Psa 89:48 | live | HVqi3ms | none recorded | 12272, 14132, 16178, 18627 | 0 | What man can **live** and never see death? Who can deliver his soul from the power of Sheol? Selah |
| Psa 118:17 | live | HVqi1cs | none recorded | 12243 | 0 | I shall not die, but I shall **live**, and recount the deeds of the Lord. |
| Psa 119:17 | live | HVqi1cs | none recorded | 12238 | 0 | Gimel Deal bountifully with your servant, that I may **live** and keep your word. |
| Psa 119:77 | live | HVqu1cs | none recorded | 17909 | 0 | Let your mercy come to me, that I may **live**; for your law is my delight. |
| Psa 119:116 | live | HVqu1cs | none recorded | - | 0 | Uphold me according to your promise, that I may **live**, and let me not be put to shame in my hope! |
| Psa 119:144 | live | HVqu1cs | none recorded | 12238, 17571 | 0 | Your testimonies are righteous forever; give me understanding that I may **live**. |
| Psa 119:175 | live | HVqj3fs | none recorded | 12238, 16472, 16510 | 0 | Let my soul **live** and praise you, and let your rules help me. |
| Pro 4:4 | live | HVqv2ms | none recorded | 12262, 18723 | 0 | he taught me and said to me, “Let your heart hold fast my words; keep my commandments, and **live**. |
| Pro 7:2 | live | HVqv2ms | none recorded | 18723 | 0 | keep my commandments and **live**; keep my teaching as the apple of your eye; |
| Pro 9:6 | live | HVqv2mp | none recorded | 12262 | 0 | Leave your simple ways, and **live**, and walk in the way of insight.” |
| Pro 15:27 | live | HVqi3ms | none recorded | 17929 | 0 | Whoever is greedy for unjust gain troubles his own household, but he who hates bribes will **live**. |
| Ecc 6:6 | live | HVqp3ms | none recorded | - | 0 | Even though he should **live** a thousand years twice over, yet enjoy no good —do not all go to the one place? |
| Isa 26:14 | live | HVqi3mp | none recorded | 12255, 12383 | 0 | They are dead, they will not **live**; they are shades, they will not arise; to that end you have visited them with destruction and wiped out all remembrance of them. |
| Isa 26:19 | live | HVqi3mp | none recorded | 12255, 12383, 14677 | 0 | Your dead shall **live**; their bodies shall rise. You who dwell in the dust, awake and sing for joy! For your dew is a dew of light, and the earth will give birth to the dead. |
| Isa 38:16 | live | HVqi3mp | none recorded | 12240, 12350, 18315, 18446 | 0 | O Lord, by these things men **live**, and in all these is the life of my spirit. Oh restore me to health and make me live! |
| Isa 38:16 | live | HVhv2ms | none recorded | - | 0 | O Lord, by these things men **live**, and in all these is the life of my spirit. Oh restore me to health and make me live! |
| Isa 55:3 | live | HVqj3fs | none recorded | 12240, 15988, 16382, 17277 | 0 | Incline your ear, and come to me; hear, that your soul may **live**; and I will make with you an everlasting covenant, my steadfast, sure love for David. |
| Jer 21:9 | live | HVqq3ms | none recorded | 18807 | 0 | He who stays in this city shall die by the sword, by famine, and by pestilence, but he who goes out and surrenders to the Chaldeans who are besieging you shall **live** and shall have his life as a prize of war. |
| Jer 27:12 | live | HVqv2mp | none recorded | 18807 | 0 | To Zedekiah king of Judah I spoke in like manner: “ Bring your necks under the yoke of the king of Babylon, and serve him and his people and **live**. |
| Jer 27:17 | live | HVqv2mp | none recorded | 18807 | 0 | Do not listen to them; serve the king of Babylon and **live**. Why should this city become a desolation? |
| Jer 35:7 | live | HVqj2mp | none recorded | - | 0 | You shall not build a house; you shall not sow seed; you shall not plant or have a vineyard; but you shall **live** in tents all your days, that you may live many days in the land where you sojourn.’ |
| Jer 38:2 | live | HVqq3ms | none recorded | 18807 | 0 | “ Thus says the Lord: He who stays in this city shall die by the sword, by famine, and by pestilence, but he who goes out to the Chaldeans shall **live**. He shall have his life as a prize of war, and live. |
| Jer 38:2 | live | HVqq3ms | none recorded | 18807 | 0 | “ Thus says the Lord: He who stays in this city shall die by the sword, by famine, and by pestilence, but he who goes out to the Chaldeans shall **live**. He shall have his life as a prize of war, and live. |
| Jer 38:17 | live | HVqq2ms | none recorded | 18807 | 0 | Then Jeremiah said to Zedekiah, “ Thus says the Lord, the God of hosts, the God of Israel: If you will surrender to the officials of the king of Babylon, then your life shall be spared, and this city shall not be burned with fire, and you and your house shall **live**. |
| Lam 4:20 | live | HVqi1cp | none recorded | - | 0 | The breath of our nostrils, the Lord’s anointed, was captured in their pits, of whom we said, “ Under his shadow we shall **live** among the nations.” |
| Eze 3:21 | live | HVqi3ms | none recorded | - | 0 | But if you warn the righteous person not to sin, and he does not sin, he shall surely **live**, because he took warning, and you will have delivered your soul.” |
| Eze 13:19 | live | HVqi3fp | none recorded | 16089, 16610, 18710, 18802 | 0 | You have profaned me among my people for handfuls of barley and for pieces of bread, putting to death souls who should not die and keeping alive souls who should not **live**, by your lying to my people, who listen to lies. |
| Eze 16:6 | live | HVqv2fs | none recorded | - | 0 | “And when I passed by you and saw you wallowing in your blood, I said to you in your blood, ‘ **Live**!’ I said to you in your blood, ‘ Live!’ |
| Eze 16:6 | live | HVqv2fs | none recorded | - | 0 | “And when I passed by you and saw you wallowing in your blood, I said to you in your blood, ‘ **Live**!’ I said to you in your blood, ‘ Live!’ |
| Eze 18:9 | live | HVqi3ms | none recorded | - | 0 | walks in my statutes, and keeps my rules by acting faithfully —he is righteous; he shall surely **live**, declares the Lord God. |
| Eze 18:13 | live | HVqq3ms | none recorded | - | 0 | lends at interest, and takes profit; shall he then **live**? He shall not live. He has done all these abominations; he shall surely die; his blood shall be upon himself. |
| Eze 18:13 | live | HVqi3ms | none recorded | - | 0 | lends at interest, and takes profit; shall he then **live**? He shall not live. He has done all these abominations; he shall surely die; his blood shall be upon himself. |
| Eze 18:17 | live | HVqi3ms | none recorded | - | 0 | withholds his hand from iniquity, takes no interest or profit, obeys my rules, and walks in my statutes; he shall not die for his father’s iniquity; he shall surely **live**. |
| Eze 18:19 | live | HVqi3ms | none recorded | - | 0 | “Yet you say, ‘ Why should not the son suffer for the iniquity of the father?’ When the son has done what is just and right, and has been careful to observe all my statutes, he shall surely **live**. |
| Eze 18:21 | live | HVqi3ms | none recorded | - | 0 | “But if a wicked person turns away from all his sins that he has committed and keeps all my statutes and does what is just and right, he shall surely **live**; he shall not die. |
| Eze 18:22 | live | HVqi3ms | none recorded | 12267 | 0 | None of the transgressions that he has committed shall be remembered against him; for the righteousness that he has done he shall **live**. |
| Eze 18:23 | live | HVqq3ms | none recorded | 12266, 17944, 18720 | 0 | Have I any pleasure in the death of the wicked, declares the Lord God, and not rather that he should turn from his way and **live**? |
| Eze 18:24 | live | HVqq3ms | none recorded | 12267 | 0 | But when a righteous person turns away from his righteousness and does injustice and does the same abominations that the wicked person does, shall he **live**? None of the righteous deeds that he has done shall be remembered; for the treachery of which he is guilty and the sin he has committed, for them he shall die. |
| Eze 18:28 | live | HVqi3ms | none recorded | - | 0 | Because he considered and turned away from all the transgressions that he had committed, he shall surely **live**; he shall not die. |
| Eze 18:32 | live | HVqv2mp | none recorded | 12266, 17944, 18720 | 0 | For I have no pleasure in the death of anyone, declares the Lord God; so turn, and **live**.” |
| Eze 20:11 | live | HVqq3ms | none recorded | 12265 | 0 | I gave them my statutes and made known to them my rules, by which, if a person does them, he shall **live**. |
| Eze 20:13 | live | HVqq3ms | none recorded | - | 0 | But the house of Israel rebelled against me in the wilderness. They did not walk in my statutes but rejected my rules, by which, if a person does them, he shall **live**; and my Sabbaths they greatly profaned. “Then I said I would pour out my wrath upon them in the wilderness, to make a full end of them. |
| Eze 20:21 | live | HVqq3ms | none recorded | - | 0 | But the children rebelled against me. They did not walk in my statutes and were not careful to obey my rules, by which, if a person does them, he shall **live**; they profaned my Sabbaths. “Then I said I would pour out my wrath upon them and spend my anger against them in the wilderness. |
| Eze 33:10 | live | HVqi1cp | none recorded | 12268, 17944 | 0 | “And you, son of man, say to the house of Israel, Thus have you said: ‘ Surely our transgressions and our sins are upon us, and we rot away because of them. How then can we **live**?’ |
| Eze 33:11 | live | HVqq3ms | none recorded | 12266, 12268, 12329, 17944, 18278, 18720 | 0 | Say to them, As I **live**, declares the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live; turn back, turn back from your evil ways, for why will you die, O house of Israel? |
| Eze 33:12 | live | HVqcc | none recorded | - | 0 | “And you, son of man, say to your people, The righteousness of the righteous shall not deliver him when he transgresses, and as for the wickedness of the wicked, he shall not fall by it when he turns from his wickedness, and the righteous shall not be able to **live** by his righteousness when he sins. |
| Eze 33:13 | live | HVqi3ms | none recorded | - | 0 | Though I say to the righteous that he shall surely **live**, yet if he trusts in his righteousness and does injustice, none of his righteous deeds shall be remembered, but in his injustice that he has done he shall die. |
| Eze 33:15 | live | HVqi3ms | none recorded | 18288 | 0 | if the wicked restores the pledge, gives back what he has taken by robbery, and walks in the statutes of life, not doing injustice, he shall surely **live**; he shall not die. |
| Eze 33:16 | live | HVqi3ms | none recorded | - | 0 | None of the sins that he has committed shall be remembered against him. He has done what is just and right; he shall surely **live**. |
| Eze 33:19 | live | HVqi3ms | none recorded | - | 0 | And when the wicked turns from his wickedness and does what is just and right, he shall **live** by this. |
| Eze 37:3 | live | HVqi3fp | none recorded | 12254 | 0 | And he said to me, “ Son of man, can these bones **live**?” And I answered, “O Lord God, you know.” |
| Eze 37:5 | live | HVqq2mp | none recorded | 12254, 17259 | 0 | Thus says the Lord God to these bones: Behold, I will cause breath to enter you, and you shall **live**. |
| Eze 37:6 | live | HVqq2mp | none recorded | 12254, 16481, 17259 | 0 | And I will lay sinews upon you, and will cause flesh to come upon you, and cover you with skin, and put breath in you, and you shall **live**, and you shall know that I am the Lord.” |
| Eze 37:9 | live | HVqu3mp | none recorded | 17259 | 0 | Then he said to me, “ Prophesy to the breath; prophesy, son of man, and say to the breath, Thus says the Lord God: Come from the four winds, O breath, and breathe on these slain, that they may **live**.” |
| Eze 37:14 | live | HVqq2mp | none recorded | 16274 | 0 | And I will put my Spirit within you, and you shall **live**, and I will place you in your own land. Then you shall know that I am the Lord; I have spoken, and I will do it, declares the Lord.” |
| Eze 47:9 | live | HVqi3ms | none recorded | 18710 | 0 | And wherever the river goes, every living creature that swarms will **live**, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes. |
| Eze 47:9 | live | HVqq3ms | none recorded | - | 0 | And wherever the river goes, every living creature that swarms will **live**, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes. |
| Hos 6:2 | live | HVqu1cp | none recorded | - | 0 | After two days he will revive us; on the third day he will raise us up, that we may **live** before him. |
| Amo 5:4 | live | HVqv2mp | none recorded | 12264, 18801 | 0 | For thus says the Lord to the house of Israel: “ Seek me and **live**; |
| Amo 5:6 | live | HVqv2mp | none recorded | - | 0 | Seek the Lord and **live**, lest he break out like fire in the house of Joseph, and it devour, with none to quench it for Bethel, |
| Amo 5:14 | live | HVqj2mp | none recorded | 12264 | 0 | Seek good, and not evil, that you may **live**; and so the Lord, the God of hosts, will be with you, as you have said. |
| Hab 2:4 | live | HVqi3ms | none recorded | 12264, 15117, 16095, 16344, 16529, 18801 | 0 | “ Behold, his soul is puffed up; it is not upright within him, but the righteous shall **live** by his faith. |
| Zec 1:5 | live | HVqi3mp | none recorded | 12272 | 0 | Your fathers, where are they? And the prophets, do they **live** forever? |
| Zec 10:9 | live | HVqq3cp | none recorded | - | 0 | Though I scattered them among the nations, yet in far countries they shall remember me, and with their children they shall **live** and return. |
| Zec 13:3 | live | HVqi2ms | none recorded | - | 0 | And if anyone again prophesies, his father and mother who bore him will say to him, ‘You shall not **live**, for you speak lies in the name of the Lord.’ And his father and mother who bore him shall pierce him through when he prophesies. |
| Gen 5:3 | lived | HVqw3ms | none recorded | - | 0 | When Adam had **lived** 130 years, he fathered a son in his own likeness, after his image, and named him Seth. |
| Gen 5:6 | lived | HVqw3ms | none recorded | - | 0 | When Seth had **lived** 105 years, he fathered Enosh. |
| Gen 5:7 | lived | HVqw3ms | none recorded | - | 0 | Seth **lived** after he fathered Enosh 807 years and had other sons and daughters. |
| Gen 5:9 | lived | HVqw3ms | none recorded | - | 0 | When Enosh had **lived** 90 years, he fathered Kenan. |
| Gen 5:10 | lived | HVqw3ms | none recorded | - | 0 | Enosh **lived** after he fathered Kenan 815 years and had other sons and daughters. |
| Gen 5:12 | lived | HVqw3ms | none recorded | - | 0 | When Kenan had **lived** 70 years, he fathered Mahalalel. |
| Gen 5:13 | lived | HVqw3ms | none recorded | - | 0 | Kenan **lived** after he fathered Mahalalel 840 years and had other sons and daughters. |
| Gen 5:15 | lived | HVqw3ms | none recorded | - | 0 | When Mahalalel had **lived** 65 years, he fathered Jared. |
| Gen 5:16 | lived | HVqw3ms | none recorded | - | 0 | Mahalalel **lived** after he fathered Jared 830 years and had other sons and daughters. |
| Gen 5:18 | lived | HVqw3ms | none recorded | - | 0 | When Jared had **lived** 162 years, he fathered Enoch. |
| Gen 5:19 | lived | HVqw3ms | none recorded | - | 0 | Jared **lived** after he fathered Enoch 800 years and had other sons and daughters. |
| Gen 5:21 | lived | HVqw3ms | none recorded | - | 0 | When Enoch had **lived** 65 years, he fathered Methuselah. |
| Gen 5:25 | lived | HVqw3ms | none recorded | - | 0 | When Methuselah had **lived** 187 years, he fathered Lamech. |
| Gen 5:26 | lived | HVqw3ms | none recorded | - | 0 | Methuselah **lived** after he fathered Lamech 782 years and had other sons and daughters. |
| Gen 5:28 | lived | HVqw3ms | none recorded | - | 0 | When Lamech had **lived** 182 years, he fathered a son |
| Gen 5:30 | lived | HVqw3ms | none recorded | - | 0 | Lamech **lived** after he fathered Noah 595 years and had other sons and daughters. |
| Gen 9:28 | lived | HVqw3ms | none recorded | - | 0 | After the flood Noah **lived** 350 years. |
| Gen 11:11 | lived | HVqw3ms | none recorded | - | 0 | And Shem **lived** after he fathered Arpachshad 500 years and had other sons and daughters. |
| Gen 11:12 | lived | HVqp3ms | none recorded | - | 0 | When Arpachshad had **lived** 35 years, he fathered Shelah. |
| Gen 11:13 | lived | HVqw3ms | none recorded | - | 0 | And Arpachshad **lived** after he fathered Shelah 403 years and had other sons and daughters. |
| Gen 11:14 | lived | HVqp3ms | none recorded | - | 0 | When Shelah had **lived** 30 years, he fathered Eber. |
| Gen 11:15 | lived | HVqw3ms | none recorded | - | 0 | And Shelah **lived** after he fathered Eber 403 years and had other sons and daughters. |
| Gen 11:16 | lived | HVqw3ms | none recorded | - | 0 | When Eber had **lived** 34 years, he fathered Peleg. |
| Gen 11:17 | lived | HVqw3ms | none recorded | - | 0 | And Eber **lived** after he fathered Peleg 430 years and had other sons and daughters. |
| Gen 11:18 | lived | HVqw3ms | none recorded | - | 0 | When Peleg had **lived** 30 years, he fathered Reu. |
| Gen 11:19 | lived | HVqw3ms | none recorded | - | 0 | And Peleg **lived** after he fathered Reu 209 years and had other sons and daughters. |
| Gen 11:20 | lived | HVqw3ms | none recorded | - | 0 | When Reu had **lived** 32 years, he fathered Serug. |
| Gen 11:21 | lived | HVqw3ms | none recorded | - | 0 | And Reu **lived** after he fathered Serug 207 years and had other sons and daughters. |
| Gen 11:22 | lived | HVqw3ms | none recorded | - | 0 | When Serug had **lived** 30 years, he fathered Nahor. |
| Gen 11:23 | lived | HVqw3ms | none recorded | - | 0 | And Serug **lived** after he fathered Nahor 200 years and had other sons and daughters. |
| Gen 11:24 | lived | HVqw3ms | none recorded | - | 0 | When Nahor had **lived** 29 years, he fathered Terah. |
| Gen 11:25 | lived | HVqw3ms | none recorded | - | 0 | And Nahor **lived** after he fathered Terah 119 years and had other sons and daughters. |
| Gen 11:26 | lived | HVqw3ms | none recorded | - | 0 | When Terah had **lived** 70 years, he fathered Abram, Nahor, and Haran. |
| Gen 47:28 | lived | HVqw3ms | none recorded | - | 0 | And Jacob **lived** in the land of Egypt seventeen years. So the days of Jacob, the years of his life, were 147 years. |
| Gen 50:22 | lived | HVqw3ms | none recorded | - | 0 | So Joseph remained in Egypt, he and his father’s house. Joseph **lived** 110 years. |
| 2Ki 14:17 | lived | HVqw3ms | none recorded | - | 0 | Amaziah the son of Joash, king of Judah, **lived** fifteen years after the death of Jehoash son of Jehoahaz, king of Israel. |
| 2Ch 25:25 | lived | HVqw3ms | none recorded | - | 0 | Amaziah the son of Joash, king of Judah, **lived** fifteen years after the death of Joash the son of Jehoahaz, king of Israel. |
| Job 42:16 | lived | HVqw3ms | none recorded | 18787 | 0 | And after this Job **lived** 140 years, and saw his sons, and his sons ’ sons, four generations. |
| Eze 37:10 | lived | HVqw3mp | none recorded | 17264 | 0 | So I prophesied as he commanded me, and the breath came into them, and they **lived** and stood on their feet, an exceedingly great army. |
| Gen 47:25 | lives | HVhp2ms | none recorded | - | 0 | And they said, “You have saved our **lives**; may it please my lord, we will be servants to Pharaoh.” |
| Deu 8:3 | lives | HVqi3ms | none recorded | - | 0 | And he humbled you and let you hunger and fed you with manna, which you did not know, nor did your fathers know, that he might make you know that man does not live by bread alone, but man **lives** by every word that comes from the mouth of the Lord. |
| 2Ki 7:4 | lives | HVpi3mp | none recorded | - | 0 | If we say, ‘Let us enter the city,’ the famine is in the city, and we shall die there. And if we sit here, we die also. So now come, let us go over to the camp of the Syrians. If they spare our **lives** we shall live, and if they kill us we shall but die.” |
| Ecc 6:3 | lives | HVqi3ms | none recorded | 12276, 16097 | 0 | If a man fathers a hundred children and **lives** many years, so that the days of his years are many, but his soul is not satisfied with life’s good things, and he also has no burial, I say that a stillborn child is better off than he. |
| Ecc 11:8 | lives | HVqi3ms | none recorded | 12276 | 0 | So if a person **lives** many years, let him rejoice in them all; but let him remember that the days of darkness will be many. All that comes is vanity. |

### 3.2 H2416A חַי chay "alive": 191 own occurrences in 175 verses

- **Meaning as stored:** Hebrew; native word חַי, transliteration chay; STEP gloss "alive"; sense head "alive" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2416):** living thing, animal.
- **Related terms (24):** H2416B chay "kinsfolk"; H2416C chay.yah "living thing"; H2416D chay.yah "community"; H2416E chay.yim "life"; H2417 chay "living"; H2419 chi.el "Hiel"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 249; verses STEP attests 0; verse_lexical rows the parse found 240.

- **Carried by the member words:** living (64), lives (49), live (41), alive (37).
- **Engagement of these occurrences:** none recorded 191.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 43:7 | alive | HAamsa | none recorded | 20782, 20786, 20791, 20795, 20798, 20800, 20803, 20804, 20805 | 0 | They replied, “The man questioned us carefully about ourselves and our kindred, saying, ‘Is your father still **alive**? Do you have another brother?’ What we told him was in answer to these questions. Could we in any way know that he would say, ‘Bring your brother down ’?” |
| Gen 43:27 | alive | HAamsa | none recorded | 20919, 20920, 20923, 20924, 20925, 20927, 20928, 20929, 20930 | 0 | And he inquired about their welfare and said, “Is your father well, the old man of whom you spoke? Is he still **alive**?” |
| Gen 43:28 | alive | HAamsa | none recorded | - | 0 | They said, “Your servant our father is well; he is still **alive**.” And they bowed their heads and prostrated themselves. |
| Gen 45:3 | alive | HAamsa | none recorded | - | 0 | And Joseph said to his brothers, “ I am Joseph! Is my father still **alive**?” But his brothers could not answer him, for they were dismayed at his presence. |
| Gen 45:26 | alive | HAamsa | none recorded | 12368, 15984, 18280 | 0 | And they told him, “ Joseph is still **alive**, and he is ruler over all the land of Egypt.” And his heart became numb, for he did not believe them. |
| Gen 45:28 | alive | HAamsa | none recorded | 12368, 15984, 18280, 18517 | 0 | And Israel said, “It is enough; Joseph my son is still **alive**. I will go and see him before I die.” |
| Gen 46:30 | alive | HAamsa | none recorded | 12305 | 0 | Israel said to Joseph, “ Now let me die, since I have seen your face and know that you are still **alive**.” |
| Exo 4:18 | alive | HAampa | none recorded | - | 0 | Moses went back to Jethro his father-in-law and said to him, “ Please let me go back to my brothers in Egypt to see whether they are still **alive**.” And Jethro said to Moses, “ Go in peace.” |
| Exo 22:4 | alive | HAampa | none recorded | - | 0 | If the stolen beast is found **alive** in his possession, whether it is an ox or a donkey or a sheep, he shall pay double. |
| Lev 16:10 | alive | HAamsa | none recorded | - | 0 | but the goat on which the lot fell for Azazel shall be presented **alive** before the Lord to make atonement over it, that it may be sent away into the wilderness to Azazel. |
| Num 16:30 | alive | HAampa | none recorded | 12353, 18294, 18633 | 0 | But if the Lord creates something new, and the ground opens its mouth and swallows them up with all that belongs to them, and they go down **alive** into Sheol, then you shall know that these men have despised the Lord.” |
| Num 16:33 | alive | HAampa | none recorded | 12353, 18294, 18614, 18634 | 0 | So they and all that belonged to them went down **alive** into Sheol, and the earth closed over them, and they perished from the midst of the assembly. |
| Deu 5:3 | alive | HAampa | none recorded | - | 0 | Not with our fathers did the Lord make this covenant, but with us, who are all of us here **alive** today. |
| Deu 31:27 | alive | HAamsa | none recorded | 12368 | 0 | For I know how rebellious and stubborn you are. Behold, even today while I am yet **alive** with you, you have been rebellious against the Lord. How much more after my death! |
| Jos 8:23 | alive | HAamsa | none recorded | - | 0 | But the king of Ai they took **alive**, and brought him near to Joshua. |
| 1Sa 15:8 | alive | HAamsa | none recorded | - | 0 | And he took Agag the king of the Amalekites **alive** and devoted to destruction all the people with the edge of the sword. |
| 1Sa 20:14 | alive | HAamsa | none recorded | 12368 | 0 | If I am still **alive**, show me the steadfast love of the Lord, that I may not die; |
| 2Sa 12:18 | alive | HAamsa | none recorded | 18280 | 0 | On the seventh day the child died. And the servants of David were afraid to tell him that the child was dead, for they said, “ Behold, while the child was yet **alive**, we spoke to him, and he did not listen to us. How then can we say to him the child is dead? He may do himself some harm.” |
| 2Sa 12:21 | alive | HAamsa | none recorded | 18280 | 0 | Then his servants said to him, “ What is this thing that you have done? You fasted and wept for the child while he was **alive**; but when the child died, you arose and ate food.” |
| 2Sa 12:22 | alive | HAamsa | none recorded | 12244, 18280 | 0 | He said, “While the child was still **alive**, I fasted and wept, for I said, ‘ Who knows whether the Lord will be gracious to me, that the child may live?’ |
| 2Sa 18:14 | alive | HAamsa | none recorded | - | 0 | Joab said, “I will not waste time like this with you.” And he took three javelins in his hand and thrust them into the heart of Absalom while he was still **alive** in the oak. |
| 2Sa 19:6 | alive | HAamsa | none recorded | 12368 | 0 | because you love those who hate you and hate those who love you. For you have made it clear today that commanders and servants are nothing to you, for today I know that if Absalom were **alive** and all of us were dead today, then you would be pleased. |
| 1Ki 3:23 | alive | HAamsa | none recorded | 18280 | 0 | Then the king said, “The one says, ‘ This is my son that is **alive**, and your son is dead ’; and the other says, ‘ No; but your son is dead, and my son is the living one.’” |
| 1Ki 3:26 | alive | HAamsa | none recorded | 12368, 18280, 18450 | 0 | Then the woman whose son was **alive** said to the king, because her heart yearned for her son, “ Oh, my lord, give her the living child, and by no means put him to death.” But the other said, “He shall be neither mine nor yours; divide him.” |
| 1Ki 12:6 | alive | HAamsa | none recorded | - | 0 | Then King Rehoboam took counsel with the old men, who had stood before Solomon his father while he was yet **alive**, saying, “ How do you advise me to answer this people?” |
| 1Ki 20:18 | alive | HAampa | none recorded | - | 0 | He said, “ If they have come out for peace, take them **alive**. Or if they have come out for war, take them alive.” |
| 1Ki 20:18 | alive | HAampa | none recorded | - | 0 | He said, “ If they have come out for peace, take them **alive**. Or if they have come out for war, take them alive.” |
| 1Ki 21:15 | alive | HAamsa | none recorded | - | 0 | As soon as Jezebel heard that Naboth had been stoned and was dead, Jezebel said to Ahab, “ Arise, take possession of the vineyard of Naboth the Jezreelite, which he refused to give you for money, for Naboth is not **alive**, but dead.” |
| 2Ki 7:12 | alive | HAampa | none recorded | - | 0 | And the king rose in the night and said to his servants, “I will tell you what the Syrians have done to us. They know that we are hungry. Therefore they have gone out of the camp to hide themselves in the open country, thinking, ‘When they come out of the city, we shall take them **alive** and get into the city.’” |
| 2Ki 10:14 | alive | HAampa | none recorded | - | 0 | He said, “ Take them **alive**.” And they took them alive and slaughtered them at the pit of Beth-eked, forty-two persons, and he spared none of them. |
| 2Ki 10:14 | alive | HAampa | none recorded | - | 0 | He said, “ Take them **alive**.” And they took them alive and slaughtered them at the pit of Beth-eked, forty-two persons, and he spared none of them. |
| 2Ch 10:6 | alive | HAamsa | none recorded | - | 0 | Then King Rehoboam took counsel with the old men, who had stood before Solomon his father while he was yet **alive**, saying, “ How do you advise me to answer this people?” |
| 2Ch 25:12 | alive | HAampa | none recorded | - | 0 | The men of Judah captured another 10,000 **alive** and took them to the top of a rock and threw them down from the top of the rock, and they were all dashed to pieces. |
| Psa 55:15 | alive | HAampa | none recorded | 12353, 18294, 18614, 18635 | 0 | Let death steal over them; let them go down to Sheol **alive**; for evil is in their dwelling place and in their heart. |
| Psa 124:3 | alive | HAampa | none recorded | 13585, 13860, 14321 | 0 | then they would have swallowed us up **alive**, when their anger was kindled against us; |
| Pro 1:12 | alive | HAampa | none recorded | 12353, 18614, 18636 | 0 | like Sheol let us swallow them **alive**, and whole, like those who go down to the pit; |
| Ecc 4:2 | alive | HAampa | none recorded | - | 0 | And I thought the dead who are already dead more fortunate than the living who are still **alive**. |
| Lev 14:4 | live | HAafpa | none recorded | - | 0 | the priest shall command them to take for him who is to be cleansed two **live** clean birds and cedarwood and scarlet yarn and hyssop. |
| Lev 14:6 | live | HAafsa | none recorded | - | 0 | He shall take the **live** bird with the cedarwood and the scarlet yarn and the hyssop, and dip them and the live bird in the blood of the bird that was killed over the fresh water. |
| Lev 14:6 | live | HAafsa | none recorded | - | 0 | He shall take the **live** bird with the cedarwood and the scarlet yarn and the hyssop, and dip them and the live bird in the blood of the bird that was killed over the fresh water. |
| Lev 14:51 | live | HAafsa | none recorded | - | 0 | and shall take the cedarwood and the hyssop and the scarlet yarn, along with the **live** bird, and dip them in the blood of the bird that was killed and in the fresh water and sprinkle the house seven times. |
| Lev 14:52 | live | HAafsa | none recorded | - | 0 | Thus he shall cleanse the house with the blood of the bird and with the fresh water and with the **live** bird and with the cedarwood and hyssop and scarlet yarn. |
| Lev 14:53 | live | HAafsa | none recorded | - | 0 | And he shall let the **live** bird go out of the city into the open country. So he shall make atonement for the house, and it shall be clean.” |
| Lev 16:20 | live | HAamsa | none recorded | - | 0 | “And when he has made an end of atoning for the Holy Place and the tent of meeting and the altar, he shall present the **live** goat. |
| Lev 16:21 | live | HAamsa | none recorded | - | 0 | And Aaron shall lay both his hands on the head of the **live** goat, and confess over it all the iniquities of the people of Israel, and all their transgressions, all their sins. And he shall put them on the head of the goat and send it away into the wilderness by the hand of a man who is in readiness. |
| Num 14:21 | live | HAamsa | none recorded | 12329, 18278 | 0 | But truly, as I **live**, and as all the earth shall be filled with the glory of the Lord, |
| Num 14:28 | live | HAamsa | none recorded | - | 0 | Say to them, ‘As I **live**, declares the Lord, what you have said in my hearing I will do to you: |
| Deu 4:10 | live | HAampa | none recorded | 12336, 18285 | 0 | how on the day that you stood before the Lord your God at Horeb, the Lord said to me, ‘ Gather the people to me, that I may let them hear my words, so that they may learn to fear me all the days that they **live** on the earth, and that they may teach their children so.’ |
| Deu 31:13 | live | HAampa | none recorded | - | 0 | and that their children, who have not known it, may hear and learn to fear the Lord your God, as long as you **live** in the land that you are going over the Jordan to possess.” |
| Deu 32:40 | live | HAamsa | none recorded | 12329, 18278 | 0 | For I lift up my hand to heaven and swear, As I **live** forever, |
| 1Sa 1:26 | live | HAamsa | none recorded | 16079 | 0 | And she said, “ Oh, my lord! As you **live**, my lord, I am the woman who was standing here in your presence, praying to the Lord. |
| 2Sa 11:11 | live | HNcmpc | none recorded | 12325, 16079, 16081 | 0 | Uriah said to David, “The ark and Israel and Judah dwell in booths, and my lord Joab and the servants of my lord are camping in the open field. Shall I then go to my house, to eat and to drink and to lie with my wife? As you **live**, and as your soul lives, I will not do this thing.” |
| 2Sa 14:19 | live | HAamsa | none recorded | 16079 | 0 | The king said, “Is the hand of Joab with you in all this?” The woman answered and said, “As surely as you **live**, my lord the king, one cannot turn to the right hand or to the left from anything that my lord the king has said. It was your servant Joab who commanded me; it was he who put all these words in the mouth of your servant. |
| 1Ki 20:32 | live | HAamsa | none recorded | 16087, 18789 | 0 | So they tied sackcloth around their waists and put ropes on their heads and went to the king of Israel and said, “Your servant Ben-hadad says, ‘ Please, let me **live**.’” And he said, “Does he still live? He is my brother.” |
| 2Ki 2:2 | live | HAamsa | none recorded | 16079, 16082, 16995, 17252, 18277 | 0 | And Elijah said to Elisha, “ Please stay here, for the Lord has sent me as far as Bethel.” But Elisha said, “As the Lord lives, and as you yourself **live**, I will not leave you.” So they went down to Bethel. |
| 2Ki 2:4 | live | HAamsa | none recorded | 16079, 16082, 16995, 17252 | 0 | Elijah said to him, “ Elisha, please stay here, for the Lord has sent me to Jericho.” But he said, “As the Lord lives, and as you yourself **live**, I will not leave you.” So they came to Jericho. |
| 2Ki 2:6 | live | HAamsa | none recorded | 16079, 16082, 16995, 17252 | 0 | Then Elijah said to him, “ Please stay here, for the Lord has sent me to the Jordan.” But he said, “As the Lord lives, and as you yourself **live**, I will not leave you.” So the two of them went on. |
| 2Ki 4:30 | live | HAamsa | none recorded | 16079, 16083, 16995 | 0 | Then the mother of the child said, “As the Lord lives and as you yourself **live**, I will not leave you.” So he arose and followed her. |
| 2Ch 6:31 | live | HAampa | none recorded | - | 0 | that they may fear you and walk in your ways all the days that they **live** in the land that you gave to our fathers. |
| Isa 49:18 | live | HAamsa | none recorded | - | 0 | Lift up your eyes around and see; they all gather, they come to you. As I **live**, declares the Lord, you shall put them all on as an ornament; you shall bind them on as a bride does. |
| Jer 22:24 | live | HAamsa | none recorded | - | 0 | “As I **live**, declares the Lord, though Coniah the son of Jehoiakim, king of Judah, were the signet ring on my right hand, yet I would tear you off |
| Jer 46:18 | live | HAamsa | none recorded | - | 0 | “As I **live**, declares the King, whose name is the Lord of hosts, like Tabor among the mountains and like Carmel by the sea, shall one come. |
| Eze 5:11 | live | HAamsa | none recorded | - | 0 | Therefore, as I **live**, declares the Lord God, surely, because you have defiled my sanctuary with all your detestable things and with all your abominations, therefore I will withdraw. My eye will not spare, and I will have no pity. |
| Eze 14:16 | live | HAamsa | none recorded | - | 0 | even if these three men were in it, as I **live**, declares the Lord God, they would deliver neither sons nor daughters. They alone would be delivered, but the land would be desolate. |
| Eze 14:18 | live | HAamsa | none recorded | - | 0 | though these three men were in it, as I **live**, declares the Lord God, they would deliver neither sons nor daughters, but they alone would be delivered. |
| Eze 14:20 | live | HAamsa | none recorded | - | 0 | even if Noah, Daniel, and Job were in it, as I **live**, declares the Lord God, they would deliver neither son nor daughter. They would deliver but their own lives by their righteousness. |
| Eze 16:48 | live | HAamsa | none recorded | - | 0 | As I **live**, declares the Lord God, your sister Sodom and her daughters have not done as you and your daughters have done. |
| Eze 17:16 | live | HAamsa | none recorded | - | 0 | “As I **live**, declares the Lord God, surely in the place where the king dwells who made him king, whose oath he despised, and whose covenant with him he broke, in Babylon he shall die. |
| Eze 17:19 | live | HAamsa | none recorded | - | 0 | Therefore thus says the Lord God: As I **live**, surely it is my oath that he despised, and my covenant that he broke. I will return it upon his head. |
| Eze 18:3 | live | HAamsa | none recorded | - | 0 | As I **live**, declares the Lord God, this proverb shall no more be used by you in Israel. |
| Eze 20:3 | live | HAamsa | none recorded | 12329 | 0 | “ Son of man, speak to the elders of Israel, and say to them, Thus says the Lord God, Is it to inquire of me that you come? As I **live**, declares the Lord God, I will not be inquired of by you. |
| Eze 20:31 | live | HAamsa | none recorded | 12329 | 0 | When you present your gifts and offer up your children in fire, you defile yourselves with all your idols to this day. And shall I be inquired of by you, O house of Israel? As I **live**, declares the Lord God, I will not be inquired of by you. |
| Eze 20:33 | live | HAamsa | none recorded | 13889, 14742 | 0 | “As I **live**, declares the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you. |
| Eze 33:27 | live | HAamsa | none recorded | - | 0 | Say this to them, Thus says the Lord God: As I **live**, surely those who are in the waste places shall fall by the sword, and whoever is in the open field I will give to the beasts to be devoured, and those who are in strongholds and in caves shall die by pestilence. |
| Eze 34:8 | live | HAamsa | none recorded | - | 0 | As I **live**, declares the Lord God, surely because my sheep have become a prey, and my sheep have become food for all the wild beasts, since there was no shepherd, and because my shepherds have not searched for my sheep, but the shepherds have fed themselves, and have not fed my sheep, |
| Eze 35:6 | live | HAamsa | none recorded | - | 0 | therefore, as I **live**, declares the Lord God, I will prepare you for blood, and blood shall pursue you; because you did not hate bloodshed, therefore blood shall pursue you. |
| Eze 35:11 | live | HAamsa | none recorded | 12329, 13845 | 0 | therefore, as I **live**, declares the Lord God, I will deal with you according to the anger and envy that you showed because of your hatred against them. And I will make myself known among them, when I judge you. |
| Zep 2:9 | live | HAamsa | none recorded | - | 0 | Therefore, as I **live**,” declares the Lord of hosts, the God of Israel, “ Moab shall become like Sodom, and the Ammonites like Gomorrah, a land possessed by nettles and salt pits, and a waste forever. The remnant of my people shall plunder them, and the survivors of my nation shall possess them.” |
| 1Sa 14:39 | lives | HAamsa | none recorded | 12327, 18310 | 0 | For as the Lord **lives** who saves Israel, though it be in Jonathan my son, he shall surely die.” But there was not a man among all the people who answered him. |
| 1Sa 14:45 | lives | HAamsa | none recorded | 12327, 18310 | 0 | Then the people said to Saul, “Shall Jonathan die, who has worked this great salvation in Israel? Far from it! As the Lord **lives**, there shall not one hair of his head fall to the ground, for he has worked with God this day.” So the people ransomed Jonathan, so that he did not die. |
| 1Sa 17:55 | lives | HAamsa | none recorded | 16079, 16080, 16858 | 0 | As soon as Saul saw David go out against the Philistine, he said to Abner, the commander of the army, “ Abner, whose son is this youth?” And Abner said, “As your soul **lives**, O king, I do not know.” |
| 1Sa 19:6 | lives | HAamsa | none recorded | - | 0 | And Saul listened to the voice of Jonathan. Saul swore, “As the Lord **lives**, he shall not be put to death.” |
| 1Sa 20:3 | lives | HAamsa | none recorded | 12299, 12325, 16079, 16085, 16437, 18277, 18477, 18495 | 0 | But David vowed again, saying, “Your father knows well that I have found favor in your eyes, and he thinks, ‘Do not let Jonathan know this, lest he be grieved.’ But truly, as the Lord **lives** and as your soul lives, there is but a step between me and death.” |
| 1Sa 20:3 | lives | HAamsa | none recorded | 12299, 12325, 16079, 16085, 16437, 18277, 18477, 18495 | 0 | But David vowed again, saying, “Your father knows well that I have found favor in your eyes, and he thinks, ‘Do not let Jonathan know this, lest he be grieved.’ But truly, as the Lord **lives** and as your soul lives, there is but a step between me and death.” |
| 1Sa 20:21 | lives | HAamsa | none recorded | - | 0 | And behold, I will send the boy, saying, ‘ Go, find the arrows.’ If I say to the boy, ‘ Look, the arrows are on this side of you, take them,’ then you are to come, for, as the Lord **lives**, it is safe for you and there is no danger. |
| 1Sa 25:26 | lives | HAamsa | none recorded | 16079, 18477 | 0 | Now then, my lord, as the Lord **lives**, and as your soul lives, because the Lord has restrained you from bloodguilt and from saving with your own hand, now then let your enemies and those who seek to do evil to my lord be as Nabal. |
| 1Sa 25:26 | lives | HAamsa | none recorded | 16079, 18477 | 0 | Now then, my lord, as the Lord **lives**, and as your soul lives, because the Lord has restrained you from bloodguilt and from saving with your own hand, now then let your enemies and those who seek to do evil to my lord be as Nabal. |
| 1Sa 25:34 | lives | HAamsa | none recorded | - | 0 | For as surely as the Lord, the God of Israel, **lives**, who has restrained me from hurting you, unless you had hurried and come to meet me, truly by morning there had not been left to Nabal so much as one male.” |
| 1Sa 26:10 | lives | HAamsa | none recorded | 12283 | 0 | And David said, “As the Lord **lives**, the Lord will strike him, or his day will come to die, or he will go down into battle and perish. |
| 1Sa 26:16 | lives | HAamsa | none recorded | - | 0 | This thing that you have done is not good. As the Lord **lives**, you deserve to die, because you have not kept watch over your lord, the Lord’s anointed. And now see where the king’s spear is and the jar of water that was at his head.” |
| 1Sa 28:10 | lives | HAamsa | none recorded | 12327 | 0 | But Saul swore to her by the Lord, “As the Lord **lives**, no punishment shall come upon you for this thing.” |
| 2Sa 2:27 | lives | HAamsa | none recorded | - | 0 | And Joab said, “As God **lives**, if you had not spoken, surely the men would not have given up the pursuit of their brothers until the morning.” |
| 2Sa 4:9 | lives | HAamsa | none recorded | 12326, 16079, 16085, 16443, 16754 | 0 | But David answered Rechab and Baanah his brother, the sons of Rimmon the Beerothite, “As the Lord **lives**, who has redeemed my life out of every adversity, |
| 2Sa 11:11 | lives | HAamsc | none recorded | 16079, 16081, 16932 | 0 | Uriah said to David, “The ark and Israel and Judah dwell in booths, and my lord Joab and the servants of my lord are camping in the open field. Shall I then go to my house, to eat and to drink and to lie with my wife? As you live, and as your soul **lives**, I will not do this thing.” |
| 2Sa 12:5 | lives | HAamsa | none recorded | 12327, 18277, 18310 | 0 | Then David’s anger was greatly kindled against the man, and he said to Nathan, “As the Lord **lives**, the man who has done this deserves to die, |
| 2Sa 14:11 | lives | HAamsa | none recorded | - | 0 | Then she said, “ Please let the king invoke the Lord your God, that the avenger of blood kill no more, and my son be not destroyed.” He said, “As the Lord **lives**, not one hair of your son shall fall to the ground.” |
| 2Sa 15:21 | lives | HAamsa | none recorded | 12306, 12325, 18495 | 0 | But Ittai answered the king, “As the Lord **lives**, and as my lord the king lives, wherever my lord the king shall be, whether for death or for life, there also will your servant be.” |
| 2Sa 15:21 | lives | HAamsc | none recorded | - | 0 | But Ittai answered the king, “As the Lord **lives**, and as my lord the king lives, wherever my lord the king shall be, whether for death or for life, there also will your servant be.” |
| 2Sa 22:47 | lives | HAamsa | none recorded | 12333 | 0 | “The Lord **lives**, and blessed be my rock, and exalted be my God, the rock of my salvation, |
| 1Ki 1:29 | lives | HAamsa | none recorded | 12326, 16079, 16443, 18495 | 0 | And the king swore, saying, “As the Lord **lives**, who has redeemed my soul out of every adversity, |
| 1Ki 2:24 | lives | HAamsa | none recorded | - | 0 | Now therefore as the Lord **lives**, who has established me and placed me on the throne of David my father, and who has made me a house, as he promised, Adonijah shall be put to death today.” |
| 1Ki 17:1 | lives | HAamsa | none recorded | 12326, 18495, 18709, 18761 | 0 | Now Elijah the Tishbite, of Tishbe in Gilead, said to Ahab, “As the Lord, the God of Israel, **lives**, before whom I stand, there shall be neither dew nor rain these years, except by my word.” |
| 1Ki 17:12 | lives | HAamsa | none recorded | 18709 | 0 | And she said, “As the Lord your God **lives**, I have nothing baked, only a handful of flour in a jar and a little oil in a jug. And now I am gathering a couple of sticks that I may go in and prepare it for myself and my son, that we may eat it and die.” |
| 1Ki 17:23 | lives | HAamsa | none recorded | 12369 | 0 | And Elijah took the child and brought him down from the upper chamber into the house and delivered him to his mother. And Elijah said, “ See, your son **lives**.” |
| 1Ki 18:10 | lives | HAamsa | none recorded | 18709, 18761 | 0 | As the Lord your God **lives**, there is no nation or kingdom where my lord has not sent to seek you. And when they would say, ‘He is not here,’ he would take an oath of the kingdom or nation, that they had not found you. |
| 1Ki 18:15 | lives | HAamsa | none recorded | - | 0 | And Elijah said, “As the Lord of hosts **lives**, before whom I stand, I will surely show myself to him today.” |
| 1Ki 22:14 | lives | HAamsa | none recorded | - | 0 | But Micaiah said, “As the Lord **lives**, what the Lord says to me, that I will speak.” |
| 2Ki 2:2 | lives | HAamsa | none recorded | 12325, 16079, 16082, 18277, 18477, 18495 | 0 | And Elijah said to Elisha, “ Please stay here, for the Lord has sent me as far as Bethel.” But Elisha said, “As the Lord **lives**, and as you yourself live, I will not leave you.” So they went down to Bethel. |
| 2Ki 2:4 | lives | HAamsa | none recorded | 12325, 16079, 16082, 18477 | 0 | Elijah said to him, “ Elisha, please stay here, for the Lord has sent me to Jericho.” But he said, “As the Lord **lives**, and as you yourself live, I will not leave you.” So they came to Jericho. |
| 2Ki 2:6 | lives | HAamsa | none recorded | 12325, 16079, 16082, 18477 | 0 | Then Elijah said to him, “ Please stay here, for the Lord has sent me to the Jordan.” But he said, “As the Lord **lives**, and as you yourself live, I will not leave you.” So the two of them went on. |
| 2Ki 3:14 | lives | HAamsa | none recorded | 12326 | 0 | And Elisha said, “As the Lord of hosts **lives**, before whom I stand, were it not that I have regard for Jehoshaphat the king of Judah, I would neither look at you nor see you. |
| 2Ki 4:30 | lives | HAamsa | none recorded | 12325, 16079, 16083, 18477 | 0 | Then the mother of the child said, “As the Lord **lives** and as you yourself live, I will not leave you.” So he arose and followed her. |
| 2Ki 5:16 | lives | HAamsa | none recorded | 12326 | 0 | But he said, “As the Lord **lives**, before whom I stand, I will receive none.” And he urged him to take it, but he refused. |
| 2Ki 5:20 | lives | HAamsa | none recorded | 12327, 16085 | 0 | Gehazi, the servant of Elisha the man of God, said, “ See, my master has spared this Naaman the Syrian, in not accepting from his hand what he brought. As the Lord **lives**, I will run after him and get something from him.” |
| 2Ch 18:13 | lives | HAamsa | none recorded | - | 0 | But Micaiah said, “As the Lord **lives**, what my God says, that I will speak.” |
| Job 19:25 | lives | HAamsa | none recorded | 12333, 12405, 13876, 18279 | 0 | For I know that my Redeemer **lives**, and at the last he will stand upon the earth. |
| Job 27:2 | lives | HAamsa | none recorded | 12326, 16079, 18495 | 0 | “As God **lives**, who has taken away my right, and the Almighty, who has made my soul bitter, |
| Psa 18:46 | lives | HAamsa | none recorded | 12333 | 0 | The Lord **lives**, and blessed be my rock, and exalted be the God of my salvation — |
| Jer 4:2 | lives | HAamsa | none recorded | 12328, 18277, 18310 | 0 | and if you swear, ‘As the Lord **lives**,’ in truth, in justice, and in righteousness, then nations shall bless themselves in him, and in him shall they glory.” |
| Jer 12:16 | lives | HAamsc | none recorded | 12328 | 0 | And it shall come to pass, if they will diligently learn the ways of my people, to swear by my name, ‘As the Lord **lives**,’ even as they taught my people to swear by Baal, then they shall be built up in the midst of my people. |
| Jer 23:7 | lives | HAamsc | none recorded | 12328 | 0 | “ Therefore, behold, the days are coming, declares the Lord, when they shall no longer say, ‘As the Lord **lives** who brought up the people of Israel out of the land of Egypt,’ |
| Jer 38:16 | lives | HAamsa | none recorded | 12326, 12327, 16079, 16084 | 0 | Then King Zedekiah swore secretly to Jeremiah, “As the Lord **lives**, who made our souls, I will not put you to death or deliver you into the hand of these men who seek your life.” |
| Jer 44:26 | lives | HAamsc | none recorded | 12328 | 0 | Therefore hear the word of the Lord, all you of Judah who dwell in the land of Egypt: Behold, I have sworn by my great name, says the Lord, that my name shall no more be invoked by the mouth of any man of Judah in all the land of Egypt, saying, ‘As the Lord God **lives**.’ |
| Dan 12:7 | lives | HAamsc | none recorded | 12333 | 0 | And I heard the man clothed in linen, who was above the waters of the stream; he raised his right hand and his left hand toward heaven and swore by him who **lives** forever that it would be for a time, times, and half a time, and that when the shattering of the power of the holy people comes to an end all these things would be finished. |
| Hos 4:15 | lives | HAamsa | none recorded | 12328 | 0 | Though you play the whore, O Israel, let not Judah become guilty. Enter not into Gilgal, nor go up to Beth-aven, and swear not, “As the Lord **lives**.” |
| Amo 8:14 | lives | HAamsa | none recorded | 12328 | 0 | Those who swear by the Guilt of Samaria, and say, ‘As your god **lives**, O Dan,’ and, ‘As the Way of Beersheba lives,’ they shall fall, and never rise again.” |
| Amo 8:14 | lives | HAamsa | none recorded | 12328 | 0 | Those who swear by the Guilt of Samaria, and say, ‘As your god **lives**, O Dan,’ and, ‘As the Way of Beersheba lives,’ they shall fall, and never rise again.” |
| Gen 1:20 | living | HAafsa | none recorded | 17254, 18281, 18710 | 0 | And God said, “Let the waters swarm with swarms of **living** creatures, and let birds fly above the earth across the expanse of the heavens.” |
| Gen 1:21 | living | HAafsa | none recorded | 17254, 18281, 18710 | 0 | So God created the great sea creatures and every **living** creature that moves, with which the waters swarm, according to their kinds, and every winged bird according to its kind. And God saw that it was good. |
| Gen 1:24 | living | HAafsa | none recorded | 17254, 18281 | 0 | And God said, “Let the earth bring forth **living** creatures according to their kinds — livestock and creeping things and beasts of the earth according to their kinds.” And it was so. |
| Gen 1:28 | living | HNcfsa | none recorded | 18281 | 0 | And God blessed them. And God said to them, “Be fruitful and multiply and fill the earth and subdue it, and have dominion over the fish of the sea and over the birds of the heavens and over every **living** thing that moves on the earth.” |
| Gen 2:7 | living | HAafsa | none recorded | 16040, 16217, 17254, 17274 | 0 | then the Lord God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a **living** creature. |
| Gen 2:19 | living | HAafsa | none recorded | 16234 | 0 | Now out of the ground the Lord God had formed every beast of the field and every bird of the heavens and brought them to the man to see what he would call them. And whatever the man called every **living** creature, that was its name. |
| Gen 3:20 | living | HAamsa | none recorded | - | 0 | The man called his wife’s name Eve, because she was the mother of all **living**. |
| Gen 9:10 | living | HAafsa | none recorded | 18281 | 0 | and with every **living** creature that is with you, the birds, the livestock, and every beast of the earth with you, as many as came out of the ark; it is for every beast of the earth. |
| Gen 9:16 | living | HAafsa | none recorded | 16016, 16042, 16385, 18281 | 0 | When the bow is in the clouds, I will see it and remember the everlasting covenant between God and every **living** creature of all flesh that is on the earth.” |
| Lev 11:10 | living | HAafsa | none recorded | - | 0 | But anything in the seas or the rivers that does not have fins and scales, of the swarming creatures in the waters and of the **living** creatures that are in the waters, is detestable to you. |
| Lev 11:46 | living | HAafsa | none recorded | 18281 | 0 | This is the law about beast and bird and every **living** creature that moves through the waters and every creature that swarms on the ground, |
| Lev 14:7 | living | HAafsa | none recorded | - | 0 | And he shall sprinkle it seven times on him who is to be cleansed of the leprous disease. Then he shall pronounce him clean and shall let the **living** bird go into the open field. |
| Deu 5:26 | living | HAampa | none recorded | 12270, 12331, 18803 | 0 | For who is there of all flesh, that has heard the voice of the **living** God speaking out of the midst of fire as we have, and has still lived? |
| Jos 3:10 | living | HAamsa | none recorded | 12332 | 0 | And Joshua said, “ Here is how you shall know that the **living** God is among you and that he will without fail drive out from before you the Canaanites, the Hittites, the Hivites, the Perizzites, the Girgashites, the Amorites, and the Jebusites. |
| 1Sa 17:26 | living | HAampa | none recorded | 12330, 15121 | 0 | And David said to the men who stood by him, “ What shall be done for the man who kills this Philistine and takes away the reproach from Israel? For who is this uncircumcised Philistine, that he should defy the armies of the **living** God?” |
| 1Sa 17:36 | living | HAampa | none recorded | 12330 | 0 | Your servant has struck down both lions and bears, and this uncircumcised Philistine shall be like one of them, for he has defied the armies of the **living** God.” |
| 1Sa 25:29 | living | HAampa | none recorded | 12352, 16097, 18293, 18500 | 0 | If men rise up to pursue you and to seek your life, the life of my lord shall be bound in the bundle of the **living** in the care of the Lord your God. And the lives of your enemies he shall sling out as from the hollow of a sling. |
| 1Ki 3:22 | living | HAamsa | none recorded | - | 0 | But the other woman said, “ No, the **living** child is mine, and the dead child is yours.” The first said, “ No, the dead child is yours, and the living child is mine.” Thus they spoke before the king. |
| 1Ki 3:23 | living | HAamsa | none recorded | - | 0 | Then the king said, “The one says, ‘ This is my son that is alive, and your son is dead ’; and the other says, ‘ No; but your son is dead, and my son is the **living** one.’” |
| 1Ki 3:25 | living | HAamsa | none recorded | - | 0 | And the king said, “ Divide the **living** child in two, and give half to the one and half to the other.” |
| 1Ki 3:26 | living | HAamsa | none recorded | - | 0 | Then the woman whose son was alive said to the king, because her heart yearned for her son, “ Oh, my lord, give her the **living** child, and by no means put him to death.” But the other said, “He shall be neither mine nor yours; divide him.” |
| 1Ki 3:27 | living | HAamsa | none recorded | - | 0 | Then the king answered and said, “ Give the **living** child to the first woman, and by no means put him to death; she is his mother.” |
| 2Ki 19:4 | living | HAamsa | none recorded | 12330 | 0 | It may be that the Lord your God heard all the words of the Rabshakeh, whom his master the king of Assyria has sent to mock the **living** God, and will rebuke the words that the Lord your God has heard; therefore lift up your prayer for the remnant that is left.” |
| 2Ki 19:16 | living | HAamsa | none recorded | 12330 | 0 | Incline your ear, O Lord, and hear; open your eyes, O Lord, and see; and hear the words of Sennacherib, which he has sent to mock the **living** God. |
| Job 28:13 | living | HAampa | none recorded | - | 0 | Man does not know its worth, and it is not found in the land of the **living**. |
| Job 28:21 | living | HAamsa | none recorded | 19233 | 0 | It is hidden from the eyes of all **living** and concealed from the birds of the air. |
| Job 30:23 | living | HAamsa | none recorded | 18468 | 0 | For I know that you will bring me to death and to the house appointed for all **living**. |
| Psa 27:13 | living | HAampa | none recorded | 12352, 18293, 18411, 18500 | 0 | I believe that I shall look upon the goodness of the Lord in the land of the **living**! |
| Psa 42:2 | living | HAamsa | none recorded | 12331, 18279, 18439 | 0 | My soul thirsts for God, for the **living** God. When shall I come and appear before God? |
| Psa 52:5 | living | HAampa | none recorded | 12352 | 0 | But God will break you down forever; he will snatch and tear you from your tent; he will uproot you from the land of the **living**. Selah |
| Psa 69:28 | living | HAampa | none recorded | 12352, 18293 | 0 | Let them be blotted out of the book of the **living**; let them not be enrolled among the righteous. |
| Psa 84:2 | living | HAamsa | none recorded | 12331, 16290 | 0 | My soul longs, yes, faints for the courts of the Lord; my heart and flesh sing for joy to the **living** God. |
| Psa 142:5 | living | HAampa | none recorded | 12352, 18293, 18500 | 0 | I cry to you, O Lord; I say, “ You are my refuge, my portion in the land of the **living**.” |
| Psa 143:2 | living | HAamsa | none recorded | 12347, 18444 | 0 | Enter not into judgment with your servant, for no one **living** is righteous before you. |
| Ecc 4:15 | living | HAampa | none recorded | - | 0 | I saw all the **living** who move about under the sun, along with that youth who was to stand in the king’s place. |
| Ecc 6:8 | living | HAampa | none recorded | - | 0 | For what advantage has the wise man over the fool? And what does the poor man have who knows how to conduct himself before the **living**? |
| Ecc 7:2 | living | HAamsa | none recorded | 12347, 15873, 17021 | 0 | It is better to go to the house of mourning than to go to the house of feasting, for this is the end of all mankind, and the **living** will lay it to heart. |
| Ecc 9:4 | living | HAampa | none recorded | 12280, 12347, 16184, 18289 | 0 | But he who is joined with all the **living** has hope, for a living dog is better than a dead lion. |
| Ecc 9:4 | living | HAamsa | none recorded | - | 0 | But he who is joined with all the **living** has hope, for a living dog is better than a dead lion. |
| Ecc 9:5 | living | HAampa | none recorded | 12280, 12347, 16184, 18289, 18314 | 0 | For the **living** know that they will die, but the dead know nothing, and they have no more reward, for the memory of them is forgotten. |
| Song 4:15 | living | HAampa | none recorded | - | 0 | a garden fountain, a well of **living** water, and flowing streams from Lebanon. |
| Isa 8:19 | living | HAampa | none recorded | 12323 | 0 | And when they say to you, “ Inquire of the mediums and the necromancers who chirp and mutter,” should not a people inquire of their God? Should they inquire of the dead on behalf of the **living**? |
| Isa 37:4 | living | HAamsa | none recorded | 12330 | 0 | It may be that the Lord your God will hear the words of the Rabshakeh, whom his master the king of Assyria has sent to mock the **living** God, and will rebuke the words that the Lord your God has heard; therefore lift up your prayer for the remnant that is left.’” |
| Isa 37:17 | living | HAamsa | none recorded | 12330 | 0 | Incline your ear, O Lord, and hear; open your eyes, O Lord, and see; and hear all the words of Sennacherib, which he has sent to mock the **living** God. |
| Isa 38:11 | living | HAampa | none recorded | 12352, 18500 | 0 | I said, I shall not see the Lord, the Lord in the land of the **living**; I shall look on man no more among the inhabitants of the world. |
| Isa 38:19 | living | HAamsa | none recorded | 12351 | 0 | The **living**, the living, he thanks you, as I do this day; the father makes known to the children your faithfulness. |
| Isa 38:19 | living | HAamsa | none recorded | 12351 | 0 | The **living**, the living, he thanks you, as I do this day; the father makes known to the children your faithfulness. |
| Isa 53:8 | living | HAampa | none recorded | 12352 | 0 | By oppression and judgment he was taken away; and as for his generation, who considered that he was cut off out of the land of the **living**, stricken for the transgression of my people? |
| Jer 2:13 | living | HAampa | none recorded | 12354, 17918, 18295, 18313 | 0 | for my people have committed two evils: they have forsaken me, the fountain of **living** waters, and hewed out cisterns for themselves, broken cisterns that can hold no water. |
| Jer 10:10 | living | HAampa | none recorded | 12330, 13850, 18279, 18498 | 0 | But the Lord is the true God; he is the **living** God and the everlasting King. At his wrath the earth quakes, and the nations cannot endure his indignation. |
| Jer 11:19 | living | HAampa | none recorded | 12352 | 0 | But I was like a gentle lamb led to the slaughter. I did not know it was against me they devised schemes, saying, “Let us destroy the tree with its fruit, let us cut him off from the land of the **living**, that his name be remembered no more.” |
| Jer 17:13 | living | HAampa | none recorded | 12354 | 0 | O Lord, the hope of Israel, all who forsake you shall be put to shame; those who turn away from you shall be written in the earth, for they have forsaken the Lord, the fountain of **living** water. |
| Jer 23:36 | living | HAampa | none recorded | 12330 | 0 | But ‘the burden of the Lord ’ you shall mention no more, for the burden is every man’s own word, and you pervert the words of the **living** God, the Lord of hosts, our God. |
| Lam 3:39 | living | HAamsa | none recorded | 12347, 14774 | 0 | Why should a **living** man complain, a man, about the punishment of his sins? |
| Eze 26:20 | living | HAampa | none recorded | - | 0 | then I will make you go down with those who go down to the pit, to the people of old, and I will make you to dwell in the world below, among ruins from of old, with those who go down to the pit, so that you will not be inhabited; but I will set beauty in the land of the **living**. |
| Eze 32:23 | living | HAampa | none recorded | 12352, 12652, 12708 | 0 | whose graves are set in the uttermost parts of the pit; and her company is all around her grave, all of them slain, fallen by the sword, who spread terror in the land of the **living**. |
| Eze 32:24 | living | HAampa | none recorded | 12352, 12708 | 0 | “ Elam is there, and all her multitude around her grave; all of them slain, fallen by the sword, who went down uncircumcised into the world below, who spread their terror in the land of the **living**; and they bear their shame with those who go down to the pit. |
| Eze 32:25 | living | HAampa | none recorded | 12352, 12708 | 0 | They have made her a bed among the slain with all her multitude, her graves all around it, all of them uncircumcised, slain by the sword; for terror of them was spread in the land of the **living**, and they bear their shame with those who go down to the pit; they are placed among the slain. |
| Eze 32:26 | living | HAampa | none recorded | 12352, 12708 | 0 | “ Meshech-Tubal is there, and all her multitude, her graves all around it, all of them uncircumcised, slain by the sword; for they spread their terror in the land of the **living**. |
| Eze 32:27 | living | HAampa | none recorded | 12352, 12708, 18637 | 0 | And they do not lie with the mighty, the fallen from among the uncircumcised, who went down to Sheol with their weapons of war, whose swords were laid under their heads, and whose iniquities are upon their bones; for the terror of the mighty men was in the land of the **living**. |
| Eze 32:32 | living | HAampa | none recorded | 12352, 12708 | 0 | For I spread terror in the land of the **living**; and he shall be laid to rest among the uncircumcised, with those who are slain by the sword, Pharaoh and all his multitude, declares the Lord God.” |
| Eze 47:9 | living | HAafsa | none recorded | 18710 | 0 | And wherever the river goes, every **living** creature that swarms will live, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes. |
| Hos 1:10 | living | HAamsa | none recorded | 12332 | 0 | Yet the number of the children of Israel shall be like the sand of the sea, which cannot be measured or numbered. And in the place where it was said to them, “You are not my people,” it shall be said to them, “ Children of the **living** God.” |
| Zec 14:8 | living | HAampa | none recorded | - | 0 | On that day **living** waters shall flow out from Jerusalem, half of them to the eastern sea and half of them to the western sea. It shall continue in summer as in winter. |

### 3.3 H3427 יָשַׁב ya.shav "to dwell": 177 own occurrences in 166 verses

- **Meaning as stored:** Hebrew; native word יָשַׁב, transliteration ya.shav; STEP gloss "to dwell"; sense head "to dwell" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3427):** to dwell, remain, sit, abide.
- **Related terms (11):** H3143 yo.shiv.yah "Joshibiah"; H3428 ye.shev.av "Jeshebeab"; H3429 yo.shev bash.she.vet "Josheb-basshebeth"; H3430 yish.bo be.nov "Ishbi-benob"; H3436 yosh.be.qa.shah "Joshbekashah"; H3488 ye.tiv "to dwell"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 1113; verses STEP attests 971; verse_lexical rows the parse found 1078.

- **Carried by the member words:** lived (146), live (29), living (2).
- **Engagement of these occurrences:** none recorded 177.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 19:30 | live | HVqcc | none recorded | - | 0 | Now Lot went up out of Zoar and lived in the hills with his two daughters, for he was afraid to **live** in Zoar. So he lived in a cave with his two daughters. |
| Lev 13:46 | live | HVqi3ms | none recorded | - | 0 | He shall remain unclean as long as he has the disease. He is unclean. He shall **live** alone. His dwelling shall be outside the camp. |
| Lev 14:8 | live | HVqq3ms | none recorded | - | 0 | And he who is to be cleansed shall wash his clothes and shave off all his hair and bathe himself in water, and he shall be clean. And after that he may come into the camp, but **live** outside his tent seven days. |
| Num 32:17 | live | HVqq3ms | none recorded | - | 0 | but we will take up arms, ready to go before the people of Israel, until we have brought them to their place. And our little ones shall **live** in the fortified cities because of the inhabitants of the land. |
| Num 35:34 | live | HVqrmpa | none recorded | - | 0 | You shall not defile the land in which you **live**, in the midst of which I dwell, for I the Lord dwell in the midst of the people of Israel.” |
| Deu 2:4 | live | HVqrmpa | none recorded | - | 0 | and command the people, “ You are about to pass through the territory of your brothers, the people of Esau, who **live** in Seir; and they will be afraid of you. So be very careful. |
| Deu 2:8 | live | HVqrmpa | none recorded | - | 0 | So we went on, away from our brothers, the people of Esau, who **live** in Seir, away from the Arabah road from Elath and Ezion-geber. “And we turned and went in the direction of the wilderness of Moab. |
| Deu 2:22 | live | HVqrmpa | none recorded | - | 0 | as he did for the people of Esau, who **live** in Seir, when he destroyed the Horites before them and they dispossessed them and settled in their place even to this day. |
| Deu 2:29 | live | HVqrmpa | none recorded | - | 0 | as the sons of Esau who **live** in Seir and the Moabites who live in Ar did for me, until I go over the Jordan into the land that the Lord our God is giving to us.’ |
| Deu 2:29 | live | HVqrmpa | none recorded | - | 0 | as the sons of Esau who **live** in Seir and the Moabites who live in Ar did for me, until I go over the Jordan into the land that the Lord our God is giving to us.’ |
| Deu 8:12 | live | HVqq2ms | none recorded | - | 0 | lest, when you have eaten and are full and have built good houses and **live** in them, |
| Deu 11:30 | live | HVqrmsa | none recorded | - | 0 | Are they not beyond the Jordan, west of the road, toward the going down of the sun, in the land of the Canaanites who **live** in the Arabah, opposite Gilgal, beside the oak of Moreh? |
| Deu 12:10 | live | HVqq2mp | none recorded | - | 0 | But when you go over the Jordan and **live** in the land that the Lord your God is giving you to inherit, and when he gives you rest from all your enemies around, so that you live in safety, |
| Deu 12:10 | live | HVqq2mp | none recorded | - | 0 | But when you go over the Jordan and **live** in the land that the Lord your God is giving you to inherit, and when he gives you rest from all your enemies around, so that you live in safety, |
| Deu 26:1 | live | HVqq2ms | none recorded | - | 0 | “ When you come into the land that the Lord your God is giving you for an inheritance and have taken possession of it and **live** in it, |
| Jos 9:7 | live | HVqrmsa | none recorded | - | 0 | But the men of Israel said to the Hivites, “ Perhaps you **live** among us; then how can we make a covenant with you?” |
| 1Ki 3:17 | live | HVqrfpa | none recorded | - | 0 | The one woman said, “ Oh, my lord, this woman and I **live** in the same house, and I gave birth to a child while she was in the house. |
| 2Ki 25:24 | live | HVqv2mp | none recorded | - | 0 | And Gedaliah swore to them and their men, saying, “Do not be afraid because of the Chaldean officials. **Live** in the land and serve the king of Babylon, and it shall be well with you.” |
| 2Ch 8:11 | live | HVqi3fs | none recorded | - | 0 | Solomon brought Pharaoh’s daughter up from the city of David to the house that he had built for her, for he said, “My wife shall not **live** in the house of David king of Israel, for the places to which the ark of the Lord has come are holy.” |
| 2Ch 19:10 | live | HVqrmpa | none recorded | - | 0 | whenever a case comes to you from your brothers who **live** in their cities, concerning bloodshed, law or commandment, statutes or rules, then you shall warn them, that they may not incur guilt before the Lord and wrath may not come upon you and your brothers. Thus you shall do, and you will not incur guilt. |
| Neh 11:1 | live | HVqcc | none recorded | - | 0 | Now the leaders of the people lived in Jerusalem. And the rest of the people cast lots to bring one out of ten to **live** in Jerusalem the holy city, while nine out of ten remained in the other towns. |
| Neh 11:2 | live | HVqcc | none recorded | - | 0 | And the people blessed all the men who willingly offered to **live** in Jerusalem. |
| Est 9:19 | live | HVqrmpa | none recorded | - | 0 | Therefore the Jews of the villages, who **live** in the rural towns, hold the fourteenth day of the month of Adar as a day for gladness and feasting, as a holiday, and as a day on which they send gifts of food to one another. |
| Pro 21:9 | live | HVqcc | none recorded | - | 0 | It is better to **live** in a corner of the housetop than in a house shared with a quarrelsome wife. |
| Pro 21:19 | live | HVqcc | none recorded | - | 0 | It is better to **live** in a desert land than with a quarrelsome and fretful woman. |
| Pro 25:24 | live | HVqcc | none recorded | - | 0 | It is better to **live** in a corner of the housetop than in a house shared with a quarrelsome wife. |
| Jer 29:5 | live | HVqv2mp | none recorded | - | 0 | Build houses and **live** in them; plant gardens and eat their produce. |
| Jer 29:28 | live | HVqv2mp | none recorded | - | 0 | For he has sent to us in Babylon, saying, “ Your exile will be long; build houses and **live** in them, and plant gardens and eat their produce.”’” |
| Jer 35:7 | live | HVqi2mp | none recorded | - | 0 | You shall not build a house; you shall not sow seed; you shall not plant or have a vineyard; but you shall **live** in tents all your days, that you may live many days in the land where you sojourn.’ |
| Gen 16:3 | lived | HVqcc | none recorded | - | 0 | So, after Abram had **lived** ten years in the land of Canaan, Sarai, Abram’s wife, took Hagar the Egyptian, her servant, and gave her to Abram her husband as a wife. |
| Gen 19:29 | lived | HVqp3ms | none recorded | - | 0 | So it was that, when God destroyed the cities of the valley, God remembered Abraham and sent Lot out of the midst of the overthrow when he overthrew the cities in which Lot had **lived**. |
| Gen 19:30 | lived | HVqw3ms | none recorded | - | 0 | Now Lot went up out of Zoar and **lived** in the hills with his two daughters, for he was afraid to live in Zoar. So he lived in a cave with his two daughters. |
| Gen 19:30 | lived | HVqw3ms | none recorded | - | 0 | Now Lot went up out of Zoar and **lived** in the hills with his two daughters, for he was afraid to live in Zoar. So he lived in a cave with his two daughters. |
| Gen 20:1 | lived | HVqw3ms | none recorded | - | 0 | From there Abraham journeyed toward the territory of the Negeb and **lived** between Kadesh and Shur; and he sojourned in Gerar. |
| Gen 21:20 | lived | HVqw3ms | none recorded | - | 0 | And God was with the boy, and he grew up. He **lived** in the wilderness and became an expert with the bow. |
| Gen 21:21 | lived | HVqw3ms | none recorded | - | 0 | He **lived** in the wilderness of Paran, and his mother took a wife for him from the land of Egypt. |
| Gen 22:19 | lived | HVqw3ms | none recorded | - | 0 | So Abraham returned to his young men, and they arose and went together to Beersheba. And Abraham **lived** at Beersheba. |
| Gen 37:1 | lived | HVqw3ms | none recorded | - | 0 | Jacob **lived** in the land of his father’s sojournings, in the land of Canaan. |
| Exo 12:40 | lived | HVqp3cp | none recorded | - | 0 | The time that the people of Israel **lived** in Egypt was 430 years. |
| Lev 18:3 | lived | HVqp2mp | none recorded | - | 0 | You shall not do as they do in the land of Egypt, where you **lived**, and you shall not do as they do in the land of Canaan, to which I am bringing you. You shall not walk in their statutes. |
| Num 14:45 | lived | HVqrmsa | none recorded | - | 0 | Then the Amalekites and the Canaanites who **lived** in that hill country came down and defeated them and pursued them, even to Hormah. |
| Num 20:15 | lived | HVqw1cp | none recorded | - | 0 | how our fathers went down to Egypt, and we **lived** in Egypt a long time. And the Egyptians dealt harshly with us and our fathers. |
| Num 21:1 | lived | HVqrmsa | none recorded | - | 0 | When the Canaanite, the king of Arad, who **lived** in the Negeb, heard that Israel was coming by the way of Atharim, he fought against Israel, and took some of them captive. |
| Num 21:31 | lived | HVqw3ms | none recorded | - | 0 | Thus Israel **lived** in the land of the Amorites. |
| Num 21:34 | lived | HVqrmsa | none recorded | - | 0 | But the Lord said to Moses, “Do not fear him, for I have given him into your hand, and all his people, and his land. And you shall do to him as you did to Sihon king of the Amorites, who **lived** at Heshbon.” |
| Num 25:1 | lived | HVqw3ms | none recorded | - | 0 | While Israel **lived** in Shittim, the people began to whore with the daughters of Moab. |
| Deu 1:4 | lived | HVqrmsa | none recorded | - | 0 | after he had defeated Sihon the king of the Amorites, who **lived** in Heshbon, and Og the king of Bashan, who lived in Ashtaroth and in Edrei. |
| Deu 1:4 | lived | HVqrmsa | none recorded | - | 0 | after he had defeated Sihon the king of the Amorites, who **lived** in Heshbon, and Og the king of Bashan, who lived in Ashtaroth and in Edrei. |
| Deu 1:44 | lived | HVqrmsa | none recorded | - | 0 | Then the Amorites who **lived** in that hill country came out against you and chased you as bees do and beat you down in Seir as far as Hormah. |
| Deu 2:10 | lived | HVqp3cp | none recorded | - | 0 | ( The Emim formerly **lived** there, a people great and many, and tall as the Anakim. |
| Deu 2:12 | lived | HVqp3cp | none recorded | - | 0 | The Horites also **lived** in Seir formerly, but the people of Esau dispossessed them and destroyed them from before them and settled in their place, as Israel did to the land of their possession, which the Lord gave to them.) |
| Deu 2:20 | lived | HVqp3cp | none recorded | - | 0 | (It is also counted as a land of Rephaim. Rephaim formerly **lived** there—but the Ammonites call them Zamzummim — |
| Deu 2:23 | lived | HVqrmpa | none recorded | - | 0 | As for the Avvim, who **lived** in villages as far as Gaza, the Caphtorim, who came from Caphtor, destroyed them and settled in their place.) |
| Deu 3:2 | lived | HVqrmsa | none recorded | - | 0 | But the Lord said to me, ‘Do not fear him, for I have given him and all his people and his land into your hand. And you shall do to him as you did to Sihon the king of the Amorites, who **lived** at Heshbon.’ |
| Deu 4:46 | lived | HVqrmsa | none recorded | - | 0 | beyond the Jordan in the valley opposite Beth-peor, in the land of Sihon the king of the Amorites, who **lived** at Heshbon, whom Moses and the people of Israel defeated when they came out of Egypt. |
| Deu 29:16 | lived | HVqp1cp | none recorded | - | 0 | “ You know how we **lived** in the land of Egypt, and how we came through the midst of the nations through which you passed. |
| Jos 2:15 | lived | HVqrfsa | none recorded | - | 0 | Then she let them down by a rope through the window, for her house was built into the city wall, so that she **lived** in the wall. |
| Jos 6:25 | lived | HVqw3fs | none recorded | - | 0 | But Rahab the prostitute and her father’s household and all who belonged to her, Joshua saved alive. And she has **lived** in Israel to this day, because she hid the messengers whom Joshua sent to spy out Jericho. |
| Jos 9:16 | lived | HVqrmpa | none recorded | - | 0 | At the end of three days after they had made a covenant with them, they heard that they were their neighbors and that they **lived** among them. |
| Jos 12:2 | lived | HVqrmsa | none recorded | - | 0 | Sihon king of the Amorites who **lived** at Heshbon and ruled from Aroer, which is on the edge of the Valley of the Arnon, and from the middle of the valley as far as the river Jabbok, the boundary of the Ammonites, that is, half of Gilead, |
| Jos 12:4 | lived | HVqrmsa | none recorded | - | 0 | and Og king of Bashan, one of the remnant of the Rephaim, who **lived** at Ashtaroth and at Edrei |
| Jos 13:21 | lived | HVqrmpc | none recorded | - | 0 | that is, all the cities of the tableland, and all the kingdom of Sihon king of the Amorites, who reigned in Heshbon, whom Moses defeated with the leaders of Midian, Evi and Rekem and Zur and Hur and Reba, the princes of Sihon, who **lived** in the land. |
| Jos 16:10 | lived | HVqrmsa | none recorded | - | 0 | However, they did not drive out the Canaanites who **lived** in Gezer, so the Canaanites have lived in the midst of Ephraim to this day but have been made to do forced labor. |
| Jos 16:10 | lived | HVqw3ms | none recorded | - | 0 | However, they did not drive out the Canaanites who **lived** in Gezer, so the Canaanites have lived in the midst of Ephraim to this day but have been made to do forced labor. |
| Jos 24:2 | lived | HVqp3cp | none recorded | - | 0 | And Joshua said to all the people, “Thus says the Lord, the God of Israel, ‘ Long ago, your fathers **lived** beyond the Euphrates, Terah, the father of Abraham and of Nahor; and they served other gods. |
| Jos 24:7 | lived | HVqw2mp | none recorded | - | 0 | And when they cried to the Lord, he put darkness between you and the Egyptians and made the sea come upon them and cover them; and your eyes saw what I did in Egypt. And you **lived** in the wilderness a long time. |
| Jos 24:8 | lived | HVqrmsa | none recorded | - | 0 | Then I brought you to the land of the Amorites, who **lived** on the other side of the Jordan. They fought with you, and I gave them into your hand, and you took possession of their land, and I destroyed them before you. |
| Jos 24:18 | lived | HVqrmsa | none recorded | - | 0 | And the Lord drove out before us all the peoples, the Amorites who **lived** in the land. Therefore we also will serve the Lord, for he is our God.” |
| Judg 1:9 | lived | HVqrmsa | none recorded | - | 0 | And afterward the men of Judah went down to fight against the Canaanites who **lived** in the hill country, in the Negeb, and in the lowland. |
| Judg 1:10 | lived | HVqrmsa | none recorded | - | 0 | And Judah went against the Canaanites who **lived** in Hebron (now the name of Hebron was formerly Kiriath-arba ), and they defeated Sheshai and Ahiman and Talmai. |
| Judg 1:21 | lived | HVqrmsa | none recorded | - | 0 | But the people of Benjamin did not drive out the Jebusites who **lived** in Jerusalem, so the Jebusites have lived with the people of Benjamin in Jerusalem to this day. |
| Judg 1:21 | lived | HVqw3ms | none recorded | - | 0 | But the people of Benjamin did not drive out the Jebusites who **lived** in Jerusalem, so the Jebusites have lived with the people of Benjamin in Jerusalem to this day. |
| Judg 1:29 | lived | HVqrmsa | none recorded | - | 0 | And Ephraim did not drive out the Canaanites who **lived** in Gezer, so the Canaanites lived in Gezer among them. |
| Judg 1:29 | lived | HVqw3ms | none recorded | - | 0 | And Ephraim did not drive out the Canaanites who **lived** in Gezer, so the Canaanites lived in Gezer among them. |
| Judg 1:30 | lived | HVqw3ms | none recorded | - | 0 | Zebulun did not drive out the inhabitants of Kitron, or the inhabitants of Nahalol, so the Canaanites **lived** among them, but became subject to forced labor. |
| Judg 1:32 | lived | HVqw3ms | none recorded | - | 0 | so the Asherites **lived** among the Canaanites, the inhabitants of the land, for they did not drive them out. |
| Judg 1:33 | lived | HVqw3ms | none recorded | - | 0 | Naphtali did not drive out the inhabitants of Beth-shemesh, or the inhabitants of Beth-anath, so they **lived** among the Canaanites, the inhabitants of the land. Nevertheless, the inhabitants of Beth-shemesh and of Beth-anath became subject to forced labor for them. |
| Judg 3:3 | lived | HVqrmsc | none recorded | - | 0 | These are the nations: the five lords of the Philistines and all the Canaanites and the Sidonians and the Hivites who **lived** on Mount Lebanon, from Mount Baal-hermon as far as Lebo-hamath. |
| Judg 3:5 | lived | HVqp3cp | none recorded | - | 0 | So the people of Israel **lived** among the Canaanites, the Hittites, the Amorites, the Perizzites, the Hivites, and the Jebusites. |
| Judg 8:29 | lived | HVqw3ms | none recorded | - | 0 | Jerubbaal the son of Joash went and **lived** in his own house. |
| Judg 9:21 | lived | HVqw3ms | none recorded | - | 0 | And Jotham ran away and fled and went to Beer and **lived** there, because of Abimelech his brother. |
| Judg 9:41 | lived | HVqw3ms | none recorded | - | 0 | And Abimelech **lived** at Arumah, and Zebul drove out Gaal and his relatives, so that they could not dwell at Shechem. |
| Judg 10:1 | lived | HVqrmsa | none recorded | - | 0 | After Abimelech there arose to save Israel Tola the son of Puah, son of Dodo, a man of Issachar, and he **lived** at Shamir in the hill country of Ephraim. |
| Judg 11:3 | lived | HVqw3ms | none recorded | - | 0 | Then Jephthah fled from his brothers and **lived** in the land of Tob, and worthless fellows collected around Jephthah and went out with him. |
| Judg 11:26 | lived | HVqcc | none recorded | - | 0 | While Israel **lived** in Heshbon and its villages, and in Aroer and its villages, and in all the cities that are on the banks of the Arnon, 300 years, why did you not deliver them within that time? |
| Judg 18:7 | lived | HVqrfsa | none recorded | - | 0 | Then the five men departed and came to Laish and saw the people who were there, how they **lived** in security, after the manner of the Sidonians, quiet and unsuspecting, lacking nothing that is in the earth and possessing wealth, and how they were far from the Sidonians and had no dealings with anyone. |
| Judg 18:28 | lived | HVqw3mp | none recorded | - | 0 | And there was no deliverer because it was far from Sidon, and they had no dealings with anyone. It was in the valley that belongs to Beth-rehob. Then they rebuilt the city and **lived** in it. |
| Judg 21:23 | lived | HVqw3mp | none recorded | - | 0 | And the people of Benjamin did so and took their wives, according to their number, from the dancers whom they carried off. Then they went and returned to their inheritance and rebuilt the towns and **lived** in them. |
| Rut 1:4 | lived | HVqw3mp | none recorded | - | 0 | These took Moabite wives; the name of the one was Orpah and the name of the other Ruth. They **lived** there about ten years, |
| Rut 2:23 | lived | HVqw3fs | none recorded | - | 0 | So she kept close to the young women of Boaz, gleaning until the end of the barley and wheat harvests. And she **lived** with her mother-in-law. |
| 1Sa 12:11 | lived | HVqw2mp | none recorded | - | 0 | And the Lord sent Jerubbaal and Barak and Jephthah and Samuel and delivered you out of the hand of your enemies on every side, and you **lived** in safety. |
| 1Sa 23:25 | lived | HVqw3ms | none recorded | - | 0 | And Saul and his men went to seek him. And David was told, so he went down to the rock and **lived** in the wilderness of Maon. And when Saul heard that, he pursued after David in the wilderness of Maon. |
| 1Sa 23:29 | lived | HVqw3ms | none recorded | - | 0 | And David went up from there and **lived** in the strongholds of Engedi. |
| 1Sa 27:3 | lived | HVqw3ms | none recorded | - | 0 | And David **lived** with Achish at Gath, he and his men, every man with his household, and David with his two wives, Ahinoam of Jezreel, and Abigail of Carmel, Nabal’s widow. |
| 1Sa 27:7 | lived | HVqp3ms | none recorded | - | 0 | And the number of the days that David **lived** in the country of the Philistines was a year and four months. |
| 1Sa 31:7 | lived | HVqw3mp | none recorded | - | 0 | And when the men of Israel who were on the other side of the valley and those beyond the Jordan saw that the men of Israel had fled and that Saul and his sons were dead, they abandoned their cities and fled. And the Philistines came and **lived** in them. |
| 2Sa 2:3 | lived | HVqw3mp | none recorded | - | 0 | And David brought up his men who were with him, everyone with his household, and they **lived** in the towns of Hebron. |
| 2Sa 5:9 | lived | HVqw3ms | none recorded | - | 0 | And David **lived** in the stronghold and called it the city of David. And David built the city all around from the Millo inward. |
| 2Sa 9:13 | lived | HVqrmsa | none recorded | - | 0 | So Mephibosheth **lived** in Jerusalem, for he ate always at the king’s table. Now he was lame in both his feet. |
| 2Sa 14:28 | lived | HVqw3ms | none recorded | - | 0 | So Absalom **lived** two full years in Jerusalem, without coming into the king’s presence. |
| 2Sa 15:8 | lived | HVqcc | none recorded | - | 0 | For your servant vowed a vow while I **lived** at Geshur in Aram, saying, ‘ If the Lord will indeed bring me back to Jerusalem, then I will offer worship to the Lord ^.’” |
| 1Ki 2:38 | lived | HVqw3ms | none recorded | - | 0 | And Shimei said to the king, “ What you say is good; as my lord the king has said, so will your servant do.” So Shimei **lived** in Jerusalem many days. |
| 1Ki 4:25 | lived | HVqw3ms | none recorded | - | 0 | And Judah and Israel **lived** in safety, from Dan even to Beersheba, every man under his vine and under his fig tree, all the days of Solomon. |
| 1Ki 9:16 | lived | HVqrmsa | none recorded | - | 0 | ( Pharaoh king of Egypt had gone up and captured Gezer and burned it with fire, and had killed the Canaanites who **lived** in the city, and had given it as dowry to his daughter, Solomon’s wife; |
| 1Ki 11:24 | lived | HVqw3mp | none recorded | - | 0 | And he gathered men about him and became leader of a marauding band, after the killing by David. And they went to Damascus and **lived** there and made him king in Damascus. |
| 1Ki 12:17 | lived | HVqrmpa | none recorded | - | 0 | But Rehoboam reigned over the people of Israel who **lived** in the cities of Judah. |
| 1Ki 12:25 | lived | HVqw3ms | none recorded | - | 0 | Then Jeroboam built Shechem in the hill country of Ephraim and **lived** there. And he went out from there and built Penuel. |
| 1Ki 13:11 | lived | HVqrmsa | none recorded | - | 0 | Now an old prophet **lived** in Bethel. And his sons came and told him all that the man of God had done that day in Bethel. They also told to their father the words that he had spoken to the king. |
| 1Ki 13:25 | lived | HVqrmsa | none recorded | - | 0 | And behold, men passed by and saw the body thrown in the road and the lion standing by the body. And they came and told it in the city where the old prophet **lived**. |
| 1Ki 15:18 | lived | HVqrmsa | none recorded | - | 0 | Then Asa took all the silver and the gold that were left in the treasures of the house of the Lord and the treasures of the king’s house and gave them into the hands of his servants. And King Asa sent them to Ben-hadad the son of Tabrimmon, the son of Hezion, king of Syria, who **lived** in Damascus, saying, |
| 1Ki 15:21 | lived | HVqw3ms | none recorded | - | 0 | And when Baasha heard of it, he stopped building Ramah, and he **lived** in Tirzah. |
| 1Ki 17:5 | lived | HVqw3ms | none recorded | - | 0 | So he went and did according to the word of the Lord. He went and **lived** by the brook Cherith that is east of the Jordan. |
| 1Ki 21:8 | lived | HVqrmpa | none recorded | - | 0 | So she wrote letters in Ahab’s name and sealed them with his seal, and she sent the letters to the elders and the leaders who **lived** with Naboth in his city. |
| 1Ki 21:11 | lived | HVqrmpa | none recorded | - | 0 | And the men of his city, the elders and the leaders who **lived** in his city, did as Jezebel had sent word to them. As it was written in the letters that she had sent to them, |
| 2Ki 13:5 | lived | HVqw3mp | none recorded | - | 0 | (Therefore the Lord gave Israel a savior, so that they escaped from the hand of the Syrians, and the people of Israel **lived** in their homes as formerly. |
| 2Ki 15:5 | lived | HVqw3ms | none recorded | - | 0 | And the Lord touched the king, so that he was a leper to the day of his death, and he **lived** in a separate house. And Jotham the king’s son was over the household, governing the people of the land. |
| 2Ki 17:24 | lived | HVqw3mp | none recorded | - | 0 | And the king of Assyria brought people from Babylon, Cuthah, Avva, Hamath, and Sepharvaim, and placed them in the cities of Samaria instead of the people of Israel. And they took possession of Samaria and **lived** in its cities. |
| 2Ki 17:28 | lived | HVqw3ms | none recorded | - | 0 | So one of the priests whom they had carried away from Samaria came and **lived** in Bethel and taught them how they should fear the Lord. |
| 2Ki 19:36 | lived | HVqw3ms | none recorded | - | 0 | Then Sennacherib king of Assyria departed and went home and **lived** at Nineveh. |
| 2Ki 22:14 | lived | HVqrfsa | none recorded | - | 0 | So Hilkiah the priest, and Ahikam, and Achbor, and Shaphan, and Asaiah went to Huldah the prophetess, the wife of Shallum the son of Tikvah, son of Harhas, keeper of the wardrobe (now she **lived** in Jerusalem in the Second Quarter ), and they talked with her. |
| 1Ch 2:55 | lived | HVqrmpc | none recorded | - | 0 | The clans also of the scribes who **lived** at Jabez: the Tirathites, the Shimeathites and the Sucathites. These are the Kenites who came from Hammath, the father of the house of Rechab. |
| 1Ch 4:23 | lived | HVqp3cp | none recorded | - | 0 | These were the potters who were inhabitants of Netaim and Gederah. They **lived** there in the king’s service. |
| 1Ch 4:28 | lived | HVqw3mp | none recorded | - | 0 | They **lived** in Beersheba, Moladah, Hazar-shual, |
| 1Ch 4:43 | lived | HVqw3mp | none recorded | - | 0 | And they defeated the remnant of the Amalekites who had escaped, and they have **lived** there to this day. |
| 1Ch 5:9 | lived | HVqp3ms | none recorded | - | 0 | He also **lived** to the east as far as the entrance of the desert this side of the Euphrates, because their livestock had multiplied in the land of Gilead. |
| 1Ch 5:10 | lived | HVqw3mp | none recorded | - | 0 | And in the days of Saul they waged war against the Hagrites, who fell into their hand. And they **lived** in their tents throughout all the region east of Gilead. |
| 1Ch 5:11 | lived | HVqp3cp | none recorded | - | 0 | The sons of Gad **lived** over against them in the land of Bashan as far as Salecah: |
| 1Ch 5:16 | lived | HVqw3mp | none recorded | - | 0 | and they **lived** in Gilead, in Bashan and in its towns, and in all the pasturelands of Sharon to their limits. |
| 1Ch 5:22 | lived | HVqw3mp | none recorded | - | 0 | For many fell, because the war was of God. And they **lived** in their place until the exile. |
| 1Ch 5:23 | lived | HVqp3cp | none recorded | - | 0 | The members of the half-tribe of Manasseh **lived** in the land. They were very numerous from Bashan to Baal-hermon, Senir, and Mount Hermon. |
| 1Ch 8:29 | lived | HVqp3cp | none recorded | - | 0 | , Jeiel the father of Gibeon **lived** in Gibeon, and the name of his wife was Maacah. |
| 1Ch 8:32 | lived | HVqp3cp | none recorded | - | 0 | and Mikloth (he fathered Shimeah ). Now these also **lived** opposite their kinsmen in Jerusalem, with their kinsmen. |
| 1Ch 9:3 | lived | HVqp3cp | none recorded | - | 0 | And some of the people of Judah, Benjamin, Ephraim, and Manasseh **lived** in Jerusalem: |
| 1Ch 9:16 | lived | HVqrmsa | none recorded | - | 0 | and Obadiah the son of Shemaiah, son of Galal, son of Jeduthun, and Berechiah the son of Asa, son of Elkanah, who **lived** in the villages of the Netophathites. |
| 1Ch 9:35 | lived | HVqp3cp | none recorded | - | 0 | In Gibeon **lived** the father of Gibeon, Jeiel, and the name of his wife was Maacah, |
| 1Ch 9:38 | lived | HVqp3cp | none recorded | - | 0 | and Mikloth was the father of Shimeam; and these also **lived** opposite their kinsmen in Jerusalem, with their kinsmen. |
| 1Ch 10:7 | lived | HVqw3mp | none recorded | - | 0 | And when all the men of Israel who were in the valley saw that the army had fled and that Saul and his sons were dead, they abandoned their cities and fled, and the Philistines came and **lived** in them. |
| 1Ch 11:7 | lived | HVqw3ms | none recorded | - | 0 | And David **lived** in the stronghold; therefore it was called the city of David. |
| 1Ch 17:5 | lived | HVqp1cs | none recorded | - | 0 | For I have not **lived** in a house since the day I brought up Israel to this day, but I have gone from tent to tent and from dwelling to dwelling. |
| 2Ch 10:17 | lived | HVqrmpa | none recorded | - | 0 | But Rehoboam reigned over the people of Israel who **lived** in the cities of Judah. |
| 2Ch 11:5 | lived | HVqw3ms | none recorded | - | 0 | Rehoboam **lived** in Jerusalem, and he built cities for defense in Judah. |
| 2Ch 16:2 | lived | HVqrmsa | none recorded | - | 0 | Then Asa took silver and gold from the treasures of the house of the Lord and the king’s house and sent them to Ben-hadad king of Syria, who **lived** in Damascus, saying, |
| 2Ch 19:4 | lived | HVqw3ms | none recorded | - | 0 | Jehoshaphat **lived** at Jerusalem. And he went out again among the people, from Beersheba to the hill country of Ephraim, and brought them back to the Lord, the God of their fathers. |
| 2Ch 20:8 | lived | HVqw3mp | none recorded | - | 0 | And they have **lived** in it and have built for you in it a sanctuary for your name, saying, |
| 2Ch 26:7 | lived | HVqrmpa | none recorded | - | 0 | God helped him against the Philistines and against the Arabians who **lived** in Gurbaal and against the Meunites. |
| 2Ch 26:21 | lived | HVqw3ms | none recorded | - | 0 | And King Uzziah was a leper to the day of his death, and being a leper **lived** in a separate house, for he was excluded from the house of the Lord. And Jotham his son was over the king’s household, governing the people of the land. |
| 2Ch 30:25 | lived | HVqrmpa | none recorded | - | 0 | The whole assembly of Judah, and the priests and the Levites, and the whole assembly that came out of Israel, and the sojourners who came out of the land of Israel, and the sojourners who **lived** in Judah, rejoiced. |
| 2Ch 31:4 | lived | HVqrmpc | none recorded | - | 0 | And he commanded the people who **lived** in Jerusalem to give the portion due to the priests and the Levites, that they might give themselves to the Law of the Lord. |
| 2Ch 31:6 | lived | HVqrmpa | none recorded | - | 0 | And the people of Israel and Judah who **lived** in the cities of Judah also brought in the tithe of cattle and sheep, and the tithe of the dedicated things that had been dedicated to the Lord their God, and laid them in heaps. |
| 2Ch 34:22 | lived | HVqrfsa | none recorded | - | 0 | So Hilkiah and those whom the king had sent went to Huldah the prophetess, the wife of Shallum the son of Tokhath, son of Hasrah, keeper of the wardrobe (now she **lived** in Jerusalem in the Second Quarter ) and spoke to her to that effect. |
| Ezr 2:70 | lived | HVqw3mp | none recorded | - | 0 | Now the priests, the Levites, some of the people, the singers, the gatekeepers, and the temple servants **lived** in their towns, and all the rest of Israel in their towns. |
| Neh 4:12 | lived | HVqrmpa | none recorded | - | 0 | At that time the Jews who **lived** near them came from all directions and said to us ten times, “You must return to us.” |
| Neh 7:73 | lived | HVqw3mp | none recorded | - | 0 | So the priests, the Levites, the gatekeepers, the singers, some of the people, the temple servants, and all Israel, **lived** in their towns. And when the seventh month had come, the people of Israel were in their towns. |
| Neh 8:17 | lived | HVqw3mp | none recorded | - | 0 | And all the assembly of those who had returned from the captivity made booths and **lived** in the booths, for from the days of Jeshua the son of Nun to that day the people of Israel had not done so. And there was very great rejoicing. |
| Neh 11:1 | lived | HVqw3mp | none recorded | - | 0 | Now the leaders of the people **lived** in Jerusalem. And the rest of the people cast lots to bring one out of ten to live in Jerusalem the holy city, while nine out of ten remained in the other towns. |
| Neh 11:3 | lived | HVqp3cp | none recorded | - | 0 | These are the chiefs of the province who **lived** in Jerusalem; but in the towns of Judah everyone lived on his property in their towns: Israel, the priests, the Levites, the temple servants, and the descendants of Solomon’s servants. |
| Neh 11:3 | lived | HVqp3cp | none recorded | - | 0 | These are the chiefs of the province who **lived** in Jerusalem; but in the towns of Judah everyone lived on his property in their towns: Israel, the priests, the Levites, the temple servants, and the descendants of Solomon’s servants. |
| Neh 11:4 | lived | HVqp3cp | none recorded | - | 0 | And in Jerusalem **lived** certain of the sons of Judah and of the sons of Benjamin. Of the sons of Judah: Athaiah the son of Uzziah, son of Zechariah, son of Amariah, son of Shephatiah, son of Mahalalel, of the sons of Perez; |
| Neh 11:6 | lived | HVqrmpa | none recorded | - | 0 | All the sons of Perez who **lived** in Jerusalem were 468 valiant men. |
| Neh 11:21 | lived | HVqrmpa | none recorded | - | 0 | But the temple servants **lived** on Ophel; and Ziha and Gishpa were over the temple servants. |
| Neh 11:25 | lived | HVqp3cp | none recorded | - | 0 | And as for the villages, with their fields, some of the people of Judah **lived** in Kiriath-arba and its villages, and in Dibon and its villages, and in Jekabzeel and its villages, |
| Neh 13:16 | lived | HVqp3cp | none recorded | - | 0 | Tyrians also, who **lived** in the city, brought in fish and all kinds of goods and sold them on the Sabbath to the people of Judah, in Jerusalem itself! |
| Job 22:8 | lived | HVqi3ms | none recorded | - | 0 | The man with power possessed the land, and the favored man **lived** in it. |
| Isa 37:37 | lived | HVqw3ms | none recorded | - | 0 | Then Sennacherib king of Assyria departed and returned home and **lived** at Nineveh. |
| Jer 39:14 | lived | HVqw3ms | none recorded | - | 0 | sent and took Jeremiah from the court of the guard. They entrusted him to Gedaliah the son of Ahikam, son of Shaphan, that he should take him home. So he **lived** among the people. |
| Jer 40:6 | lived | HVqw3ms | none recorded | - | 0 | Then Jeremiah went to Gedaliah the son of Ahikam, at Mizpah, and **lived** with him among the people who were left in the land. |
| Jer 44:1 | lived | HVqrmpa | none recorded | - | 0 | The word that came to Jeremiah concerning all the Judeans who **lived** in the land of Egypt, at Migdol, at Tahpanhes, at Memphis, and in the land of Pathros, |
| Jer 44:15 | lived | HVqrmpa | none recorded | - | 0 | Then all the men who knew that their wives had made offerings to other gods, and all the women who stood by, a great assembly, all the people who **lived** in Pathros in the land of Egypt, answered Jeremiah: |
| Eze 16:46 | lived | HVqrfsa | none recorded | - | 0 | And your elder sister is Samaria, who **lived** with her daughters to the north of you; and your younger sister, who lived to the south of you, is Sodom with her daughters. |
| Eze 16:46 | lived | HVqrfsa | none recorded | - | 0 | And your elder sister is Samaria, who **lived** with her daughters to the north of you; and your younger sister, who lived to the south of you, is Sodom with her daughters. |
| Eze 31:6 | lived | HVqi3mp | none recorded | - | 0 | All the birds of the heavens made their nests in its boughs; under its branches all the beasts of the field gave birth to their young, and under its shadow **lived** all great nations. |
| Eze 31:17 | lived | HVqp3cp | none recorded | - | 0 | They also went down to Sheol with it, to those who are slain by the sword; yes, those who were its arm, who **lived** under its shadow among the nations. |
| Eze 36:17 | lived | HVqrmpa | none recorded | - | 0 | “ Son of man, when the house of Israel **lived** in their own land, they defiled it by their ways and their deeds. Their ways before me were like the uncleanness of a woman in her menstrual impurity. |
| Eze 37:25 | lived | HVqp3cp | none recorded | - | 0 | They shall dwell in the land that I gave to my servant Jacob, where your fathers **lived**. They and their children and their children’s children shall dwell there forever, and David my servant shall be their prince forever. |
| Zep 2:15 | lived | HVqrfsa | none recorded | - | 0 | This is the exultant city that **lived** securely, that said in her heart, “ I am, and there is no one else.” What a desolation she has become, a lair for wild beasts! Everyone who passes by her hisses and shakes his fist. |
| Jer 29:32 | living | HVqrmsa | none recorded | - | 0 | therefore thus says the Lord: Behold, I will punish Shemaiah of Nehelam and his descendants. He shall not have anyone **living** among this people, and he shall not see the good that I will do to my people, declares the Lord, for he has spoken rebellion against the Lord.’” |
| Jer 35:11 | living | HVqw1cp | none recorded | - | 0 | But when Nebuchadnezzar king of Babylon came up against the land, we said, ‘ Come, and let us go to Jerusalem for fear of the army of the Chaldeans and the army of the Syrians.’ So we are **living** in Jerusalem.” |

### 3.4 G2198 ζάω zaō "to live": 134 own occurrences in 118 verses

- **Meaning as stored:** Greek; native word ζάω, transliteration zaō; STEP gloss "to live"; sense head "to live" (the code is its own lemma).
- **Related terms (3):** G2198 zaō "to live"; G2222 zōē "life"; G2226 zōon "living thing".
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 582; verses STEP attests 0; verse_lexical rows the parse found 140.

- **Carried by the member words:** live (54), living (41), alive (18), lives (16), lived (4), come to life (1).
- **Engagement of these occurrences:** none recorded 134.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 27:63 | alive | V-PAP-NSM | none recorded | - | 0 | and said, “ Sir, we remember how that impostor said, while he was still **alive**, ‘ After three days I will rise.’ |
| Mar 16:11 | alive | V-PAI-3S | none recorded | - | 0 | But when they heard that he was **alive** and had been seen by her, they would not believe it. |
| Luk 15:32 | alive | V-AAI-3S | none recorded | 12361, 18542 | 0 | It was fitting to celebrate and be glad, for this your brother was dead, and is **alive**; he was lost, and is found.’” |
| Luk 24:23 | alive | V-PAN | none recorded | - | 0 | and when they did not find his body, they came back saying that they had even seen a vision of angels, who said that he was **alive**. |
| Act 1:3 | alive | V-PAP-ASM | none recorded | - | 0 | He presented himself **alive** to them after his suffering by many proofs, appearing to them during forty days and speaking about the kingdom of God. |
| Act 9:41 | alive | V-PAP-ASF | none recorded | - | 0 | And he gave her his hand and raised her up. Then, calling the saints and widows, he presented her **alive**. |
| Act 20:12 | alive | V-PAP-ASM | none recorded | 12369 | 0 | And they took the youth away **alive**, and were not a little comforted. |
| Act 25:19 | alive | V-PAN | none recorded | - | 0 | Rather they had certain points of dispute with him about their own religion and about a certain Jesus, who was dead, but whom Paul asserted to be **alive**. |
| Rom 6:11 | alive | V-PAP-APM | none recorded | 12358, 18298, 18543 | 0 | So you also must consider yourselves dead to sin and **alive** to God in Christ Jesus. |
| Rom 7:3 | alive | V-PAP-GSM | none recorded | - | 0 | Accordingly, she will be called an adulteress if she lives with another man while her husband is **alive**. But if her husband dies, she is free from that law, and if she marries another man she is not an adulteress. |
| Rom 7:9 | alive | V-IAI-1S | none recorded | 12287, 18267, 18312, 18551 | 0 | I was once **alive** apart from the law, but when the commandment came, sin came alive and I died. |
| Col 2:20 | alive | V-PAP-NPM | none recorded | 18531 | 0 | If with Christ you died to the elemental spirits of the world, why, as if you were still **alive** in the world, do you submit to regulations — |
| 1Th 4:15 | alive | V-PAP-NPM | none recorded | - | 0 | For this we declare to you by a word from the Lord, that we who are **alive**, who are left until the coming of the Lord, will not precede those who have fallen asleep. |
| 1Th 4:17 | alive | V-PAP-NPM | none recorded | 12404 | 0 | Then we who are **alive**, who are left, will be caught up together with them in the clouds to meet the Lord in the air, and so we will always be with the Lord. |
| Heb 9:17 | alive | V-PAI-3S | none recorded | - | 0 | For a will takes effect only at death, since it is not in force as long as the one who made it is **alive**. |
| Rev 1:18 | alive | V-PAP-NSM | none recorded | 18631 | 0 | and the living one. I died, and behold I am **alive** forevermore, and I have the keys of Death and Hades. |
| Rev 3:1 | alive | V-PAI-2S | none recorded | 12361, 18300, 18542, 18560 | 0 | “ And to the angel of the church in Sardis write: ‘ The words of him who has the seven spirits of God and the seven stars. “‘I know your works. You have the reputation of being **alive**, but you are dead. |
| Rev 19:20 | alive | V-PAP-NPM | none recorded | 12353, 18294 | 0 | And the beast was captured, and with it the false prophet who in its presence had done the signs by which he deceived those who had received the mark of the beast and those who worshiped its image. These two were thrown **alive** into the lake of fire that burns with sulfur. |
| Rev 20:5 | come to life | V-AAI-3P | none recorded | 12365 | 0 | The rest of the dead did not **come to life** until the thousand years were ended. This is the first resurrection. |
| Mat 4:4 | live | V-FDI-3S | none recorded | 12340 | 0 | But he answered, “It is written, “‘ Man shall not **live** by bread alone, but by every word that comes from the mouth of God.’” |
| Mat 9:18 | live | V-FDI-3S | none recorded | - | 0 | While he was saying these things to them, behold, a ruler came in and knelt before him, saying, “ My daughter has just died, but come and lay your hand on her, and she will **live**.” |
| Mar 5:23 | live | V-AAS-3S | none recorded | - | 0 | and implored him earnestly, saying, “ My little daughter is at the point of death. Come and lay your hands on her, so that she may be made well and **live**.” |
| Luk 4:4 | live | V-FDI-3S | none recorded | 12340 | 0 | And Jesus answered him, “It is written, ‘ Man shall not **live** by bread alone.’” |
| Luk 10:28 | live | V-FDI-2S | none recorded | 12339, 18288 | 0 | And he said to him, “You have answered correctly; do this, and you will **live**.” |
| Luk 20:38 | live | V-PAI-3P | none recorded | 18298, 18315, 18653 | 0 | Now he is not God of the dead, but of the living, for all **live** to him.” |
| Joh 4:50 | live | V-PAI-3S | none recorded | 12369, 18305 | 0 | Jesus said to him, “ Go; your son will **live**.” The man believed the word that Jesus spoke to him and went on his way. |
| Joh 4:53 | live | V-PAI-3S | none recorded | 18305 | 0 | The father knew that was the hour when Jesus had said to him, “ Your son will **live**.” And he himself believed, and all his household. |
| Joh 5:25 | live | V-FAI-3P | none recorded | 18542 | 0 | “ Truly, truly, I say to you, an hour is coming, and is now here, when the dead will hear the voice of the Son of God, and those who hear will **live**. |
| Joh 6:51 | live | V-FAI-3S | none recorded | - | 0 | I am the living bread that came down from heaven. If anyone eats of this bread, he will **live** forever. And the bread that I will give for the life of the world is my flesh.” |
| Joh 6:57 | live | V-PAI-1S | none recorded | - | 0 | As the living Father sent me, and I **live** because of the Father, so whoever feeds on me, he also will live because of me. |
| Joh 6:57 | live | V-FAI-3S | none recorded | - | 0 | As the living Father sent me, and I **live** because of the Father, so whoever feeds on me, he also will live because of me. |
| Joh 6:58 | live | V-FAI-3S | none recorded | - | 0 | This is the bread that came down from heaven, not like the bread the fathers ate, and died. Whoever feeds on this bread will **live** forever.” |
| Joh 11:25 | live | V-FDI-3S | none recorded | 12406 | 0 | Jesus said to her, “ I am the resurrection and the life. Whoever believes in me, though he die, yet shall he **live**, |
| Joh 14:19 | live | V-PAI-1S | none recorded | 12356 | 0 | Yet a little while and the world will see me no more, but you will see me. Because I **live**, you also will live. |
| Joh 14:19 | live | V-FAI-2P | none recorded | - | 0 | Yet a little while and the world will see me no more, but you will see me. Because I **live**, you also will live. |
| Act 17:28 | live | V-PAI-1P | none recorded | 18414 | 0 | for “‘ In him we **live** and move and have our being ’; as even some of your own poets have said, “‘ For we are indeed his offspring.’ |
| Act 22:22 | live | V-PAN | none recorded | 12370, 18304 | 0 | Up to this word they listened to him. Then they raised their voices and said, “Away with such a fellow from the earth! For he should not be allowed to **live**.” |
| Act 25:24 | live | V-PAN | none recorded | 12370 | 0 | And Festus said, “ King Agrippa and all who are present with us, you see this man about whom the whole Jewish people petitioned me, both in Jerusalem and here, shouting that he ought not to **live** any longer. |
| Act 28:4 | live | V-PAN | none recorded | 12370 | 0 | When the native people saw the creature hanging from his hand, they said to one another, “ No doubt this man is a murderer. Though he has escaped from the sea, Justice has not allowed him to **live**.” |
| Rom 1:17 | live | V-FDI-3S | none recorded | - | 0 | For in it the righteousness of God is revealed from faith for faith, as it is written, “The righteous shall **live** by faith.” |
| Rom 6:2 | live | V-FAI-1P | none recorded | 12313, 18509, 18543 | 0 | By no means! How can we who died to sin still **live** in it? |
| Rom 8:12 | live | V-PAN | none recorded | 12393, 16106 | 0 | So then, brothers, we are debtors, not to the flesh, to **live** according to the flesh. |
| Rom 8:13 | live | V-PAI-2P | none recorded | 12313, 12393, 16106, 16202, 18543, 18580 | 0 | For if you **live** according to the flesh you will die, but if by the Spirit you put to death the deeds of the body, you will live. |
| Rom 8:13 | live | V-FDI-2P | none recorded | - | 0 | For if you **live** according to the flesh you will die, but if by the Spirit you put to death the deeds of the body, you will live. |
| Rom 10:5 | live | V-FDI-3S | none recorded | 12339 | 0 | For Moses writes about the righteousness that is based on the law, that the person who does the commandments shall **live** by them. |
| Rom 14:8 | live | V-PAS-1P | none recorded | 12314, 18298 | 0 | For if we **live**, we live to the Lord, and if we die, we die to the Lord. So then, whether we live or whether we die, we are the Lord’s. |
| Rom 14:8 | live | V-PAI-1P | none recorded | - | 0 | For if we **live**, we live to the Lord, and if we die, we die to the Lord. So then, whether we live or whether we die, we are the Lord’s. |
| Rom 14:8 | live | V-PAS-1P | none recorded | 12314, 18298 | 0 | For if we **live**, we live to the Lord, and if we die, we die to the Lord. So then, whether we live or whether we die, we are the Lord’s. |
| Rom 14:11 | live | V-PAI-1S | none recorded | 12329, 18278 | 0 | for it is written, “As I **live**, says the Lord, every knee shall bow to me, and every tongue shall confess to God.” |
| 2Cor 4:11 | live | V-PAP-NPM | none recorded | 12314, 16107, 16204 | 0 | For we who **live** are always being given over to death for Jesus ’ sake, so that the life of Jesus also may be manifested in our mortal flesh. |
| 2Cor 5:15 | live | V-PAP-NPM | none recorded | 12312, 18509 | 0 | and he died for all, that those who **live** might no longer live for themselves but for him who for their sake died and was raised. |
| 2Cor 5:15 | live | V-PAS-3P | none recorded | - | 0 | and he died for all, that those who **live** might no longer live for themselves but for him who for their sake died and was raised. |
| 2Cor 6:9 | live | V-PAI-1P | none recorded | 12314 | 0 | as unknown, and yet well known; as dying, and behold, we **live**; as punished, and yet not killed; |
| 2Cor 13:4 | live | V-FAI-1P | none recorded | - | 0 | For he was crucified in weakness, but lives by the power of God. For we also are weak in him, but in dealing with you we will **live** with him by the power of God. |
| Gal 2:14 | live | V-PAI-2S | none recorded | 18307 | 0 | But when I saw that their conduct was not in step with the truth of the gospel, I said to Cephas before them all, “ If you, though a Jew, **live** like a Gentile and not like a Jew, how can you force the Gentiles to live like Jews?” |
| Gal 2:19 | live | V-AAS-1S | none recorded | 12313, 12358, 18298, 18509, 18723 | 0 | For through the law I died to the law, so that I might **live** to God. |
| Gal 2:20 | live | V-PAI-1S | none recorded | 12358, 16107, 16346, 17275, 18298, 18509, 18721 | 0 | I have been crucified with Christ. It is no longer I who **live**, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God, who loved me and gave himself for me. |
| Gal 2:20 | live | V-PAI-1S | none recorded | 12358, 16107, 16346, 17275, 18298, 18509, 18721 | 0 | I have been crucified with Christ. It is no longer I who **live**, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God, who loved me and gave himself for me. |
| Gal 2:20 | live | V-PAI-1S | none recorded | 12358, 16107, 16346, 17275, 18298, 18509, 18721 | 0 | I have been crucified with Christ. It is no longer I who **live**, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God, who loved me and gave himself for me. |
| Gal 3:11 | live | V-FDI-3S | none recorded | 12339, 18721 | 0 | Now it is evident that no one is justified before God by the law, for “The righteous shall **live** by faith.” |
| Gal 3:12 | live | V-FDI-3S | none recorded | 12339, 18288 | 0 | But the law is not of faith, rather “The one who does them shall **live** by them.” |
| Gal 5:25 | live | V-PAI-1P | none recorded | 12360, 16110 | 0 | If we **live** by the Spirit, let us also keep in step with the Spirit. |
| Phili 1:21 | live | V-PAN | none recorded | 12281, 12314, 12398, 16110 | 0 | For to me to **live** is Christ, and to die is gain. |
| Phili 1:22 | live | V-PAN | none recorded | 12398, 16107, 16110, 17060, 19741, 19769 | 0 | If I am to **live** in the flesh, that means fruitful labor for me. Yet which I shall choose I cannot tell. |
| 1Th 5:10 | live | V-AAS-1P | none recorded | 12359 | 0 | who died for us so that whether we are awake or asleep we might **live** with him. |
| 2Ti 3:12 | live | V-PAN | none recorded | 12358, 17939 | 0 | Indeed, all who desire to **live** a godly life in Christ Jesus will be persecuted, |
| Tit 2:12 | live | V-AAS-1P | none recorded | 12358, 17880 | 0 | training us to renounce ungodliness and worldly passions, and to **live** self-controlled, upright, and godly lives in the present age, |
| Heb 10:38 | live | V-FDI-3S | none recorded | 16344, 16529, 18721 | 0 | but my righteous one shall **live** by faith, and if he shrinks back, my soul has no pleasure in him.” |
| Heb 12:9 | live | V-FAI-1P | none recorded | 12360, 15668 | 0 | Besides this, we have had earthly fathers who disciplined us and we respected them. Shall we not much more be subject to the Father of spirits and **live**? |
| Jam 4:15 | live | V-FAI-1P | none recorded | 12346, 15167 | 0 | Instead you ought to say, “ If the Lord wills, we will **live** and do this or that.” |
| 1Pe 2:24 | live | V-AAS-1P | none recorded | 12358, 18509, 18712 | 0 | He himself bore our sins in his body on the tree, that we might die to sin and **live** to righteousness. By his wounds you have been healed. |
| 1Pe 4:6 | live | V-PAS-3P | none recorded | 12360, 12392, 18315, 18372 | 0 | For this is why the gospel was preached even to those who are dead, that though judged in the flesh the way people are, they might **live** in the spirit the way God does. |
| 1Jo 4:9 | live | V-AAS-1P | none recorded | - | 0 | In this the love of God was made manifest among us, that God sent his only Son into the world, so that we might **live** through him. |
| Luk 2:36 | lived | V-AAP-NSF | none recorded | - | 0 | And there was a prophetess, Anna, the daughter of Phanuel, of the tribe of Asher. She was advanced in years, having **lived** with her husband seven years from when she was a virgin, |
| Act 26:5 | lived | V-AAI-1S | none recorded | 18307 | 0 | They have known for a long time, if they are willing to testify, that according to the strictest party of our religion I have **lived** as a Pharisee. |
| Rom 14:9 | lived | V-AAI-3S | none recorded | 12365, 18533 | 0 | For to this end Christ died and **lived** again, that he might be Lord both of the dead and of the living. |
| Rev 13:14 | lived | V-AAI-3S | none recorded | - | 0 | and by the signs that it is allowed to work in the presence of the beast it deceives those who dwell on earth, telling them to make an image for the beast that was wounded by the sword and yet **lived**. |
| Joh 11:26 | lives | V-PAP-NSM | none recorded | 12309 | 0 | and everyone who **lives** and believes in me shall never die. Do you believe this?” |
| Rom 6:10 | lives | V-PAI-3S | none recorded | 18530 | 0 | For the death he died he died to sin, once for all, but the life he **lives** he lives to God. |
| Rom 6:10 | lives | V-PAI-3S | none recorded | 18530 | 0 | For the death he died he died to sin, once for all, but the life he **lives** he lives to God. |
| Rom 7:1 | lives | V-PAI-3S | none recorded | - | 0 | Or do you not know, brothers — for I am speaking to those who know the law — that the law is binding on a person only as long as he **lives**? |
| Rom 7:2 | lives | V-PAP-DSM | none recorded | - | 0 | For a married woman is bound by law to her husband while he **lives**, but if her husband dies she is released from the law of marriage. |
| Rom 14:7 | lives | V-PAI-3S | none recorded | 12314, 18298, 18510 | 0 | For none of us **lives** to himself, and none of us dies to himself. |
| 1Cor 7:39 | lives | V-PAI-3S | none recorded | - | 0 | A wife is bound to her husband as long as he **lives**. But if her husband dies, she is free to be married to whom she wishes, only in the Lord. |
| 2Cor 13:4 | lives | V-PAI-3S | none recorded | - | 0 | For he was crucified in weakness, but **lives** by the power of God. For we also are weak in him, but in dealing with you we will live with him by the power of God. |
| Gal 2:20 | lives | V-PAI-3S | none recorded | 18298 | 0 | I have been crucified with Christ. It is no longer I who live, but Christ who **lives** in me. And the life I now live in the flesh I live by faith in the Son of God, who loved me and gave himself for me. |
| 1Ti 5:6 | lives | V-PAP-NSF | none recorded | 12361, 18314, 18542 | 0 | but she who is self-indulgent is dead even while she **lives**. |
| Heb 7:8 | lives | V-PAI-3S | none recorded | - | 0 | In the one case tithes are received by mortal men, but in the other case, by one of whom it is testified that he **lives**. |
| Heb 7:25 | lives | V-PAP-NSM | none recorded | 12356 | 0 | Consequently, he is able to save to the uttermost those who draw near to God through him, since he always **lives** to make intercession for them. |
| Rev 4:9 | lives | V-PAP-DSM | none recorded | - | 0 | And whenever the living creatures give glory and honor and thanks to him who is seated on the throne, who **lives** forever and ever, |
| Rev 4:10 | lives | V-PAP-DSM | none recorded | 12333 | 0 | the twenty-four elders fall down before him who is seated on the throne and worship him who **lives** forever and ever. They cast their crowns before the throne, saying, |
| Rev 10:6 | lives | V-PAP-DSM | none recorded | - | 0 | and swore by him who **lives** forever and ever, who created heaven and what is in it, the earth and what is in it, and the sea and what is in it, that there would be no more delay, |
| Rev 15:7 | lives | V-PAP-GSM | none recorded | 13866 | 0 | And one of the four living creatures gave to the seven angels seven golden bowls full of the wrath of God who **lives** forever and ever, |
| Mat 16:16 | living | V-PAP-GSM | none recorded | - | 0 | Simon Peter replied, “ You are the Christ, the Son of the **living** God.” |
| Mat 22:32 | living | V-PAP-GPM | none recorded | 12359, 18590 | 0 | ‘ I am the God of Abraham, and the God of Isaac, and the God of Jacob ’? He is not God of the dead, but of the **living**.” |
| Mat 26:63 | living | V-PAP-GSM | none recorded | - | 0 | But Jesus remained silent. And the high priest said to him, “I adjure you by the **living** God, tell us if you are the Christ, the Son of God.” |
| Mar 12:27 | living | V-PAP-GPM | none recorded | 12359, 18590 | 0 | He is not God of the dead, but of the **living**. You are quite wrong.” |
| Luk 15:13 | living | V-PAP-NSM | none recorded | - | 0 | Not many days later, the younger son gathered all he had and took a journey into a far country, and there he squandered his property in reckless **living**. |
| Luk 20:38 | living | V-PAP-GPM | none recorded | 12359, 18298, 18313, 18315, 18590 | 0 | Now he is not God of the dead, but of the **living**, for all live to him.” |
| Luk 24:5 | living | V-PAP-ASM | none recorded | - | 0 | And as they were frightened and bowed their faces to the ground, the men said to them, “ Why do you seek the **living** among the dead? |
| Joh 4:10 | living | V-PAP-ASN | none recorded | 12354, 18295 | 0 | Jesus answered her, “ If you knew the gift of God, and who it is that is saying to you, ‘ Give me a drink,’ you would have asked him, and he would have given you **living** water.” |
| Joh 4:11 | living | V-PAP-ASN | none recorded | 18295 | 0 | The woman said to him, “ Sir, you have nothing to draw water with, and the well is deep. Where do you get that **living** water? |
| Joh 6:51 | living | V-PAP-NSM | none recorded | - | 0 | I am the **living** bread that came down from heaven. If anyone eats of this bread, he will live forever. And the bread that I will give for the life of the world is my flesh.” |
| Joh 6:57 | living | V-PAP-NSM | none recorded | 12356 | 0 | As the **living** Father sent me, and I live because of the Father, so whoever feeds on me, he also will live because of me. |
| Joh 7:38 | living | V-PAP-GSN | none recorded | 12354, 17775, 18295, 18316 | 0 | Whoever believes in me, as the Scripture has said, ‘ Out of his heart will flow rivers of **living** water.’” |
| Act 7:38 | living | V-PAP-APN | none recorded | 12366 | 0 | This is the one who was in the congregation in the wilderness with the angel who spoke to him at Mount Sinai, and with our fathers. He received **living** oracles to give to us. |
| Act 10:42 | living | V-PAP-GPM | none recorded | 12365, 18301 | 0 | And he commanded us to preach to the people and to testify that he is the one appointed by God to be judge of the **living** and the dead. |
| Act 14:15 | living | V-PAP-ASM | none recorded | 12330 | 0 | “ Men, why are you doing these things? We also are men, of like nature with you, and we bring you good news, that you should turn from these vain things to a **living** God, who made the heaven and the earth and the sea and all that is in them. |
| Rom 9:26 | living | V-PAP-GSM | none recorded | 12332 | 0 | “ And in the very place where it was said to them, ‘ You are not my people,’ there they will be called ‘ sons of the **living** God.’” |
| Rom 12:1 | living | V-PAP-ASF | none recorded | 12358, 16323, 16643, 16727, 18317, 18509 | 0 | I appeal to you therefore, brothers, by the mercies of God, to present your bodies as a **living** sacrifice, holy and acceptable to God, which is your spiritual worship. |
| Rom 14:9 | living | V-PAP-GPM | none recorded | 18533 | 0 | For to this end Christ died and lived again, that he might be Lord both of the dead and of the **living**. |
| 1Cor 9:14 | living | V-PAN | none recorded | - | 0 | In the same way, the Lord commanded that those who proclaim the gospel should get their **living** by the gospel. |
| 1Cor 15:45 | living | V-PAP-ASF | none recorded | 12259, 16047, 17274, 18710 | 0 | Thus it is written, “The first man Adam became a **living** being ”; the last Adam became a life-giving spirit. |
| 2Cor 3:3 | living | V-PAP-GSM | none recorded | 12332, 16110, 16323, 17073 | 0 | And you show that you are a letter from Christ delivered by us, written not with ink but with the Spirit of the **living** God, not on tablets of stone but on tablets of human hearts. |
| 2Cor 6:16 | living | V-PAP-GSM | none recorded | 12332 | 0 | What agreement has the temple of God with idols? For we are the temple of the **living** God; as God said, “I will make my dwelling among them and walk among them, and I will be their God, and they shall be my people. |
| Col 3:7 | living | V-IAI-2P | none recorded | 14786 | 0 | In these you too once walked, when you were **living** in them. |
| 1Th 1:9 | living | V-PAP-DSM | none recorded | 12330, 14786, 18279, 18313, 18498 | 0 | For they themselves report concerning us the kind of reception we had among you, and how you turned to God from idols to serve the **living** and true God, |
| 1Ti 3:15 | living | V-PAP-GSM | none recorded | 12332 | 0 | if I delay, you may know how one ought to behave in the household of God, which is the church of the **living** God, a pillar and buttress of the truth. |
| 1Ti 4:10 | living | V-PAP-DSM | none recorded | 12331 | 0 | For to this end we toil and strive, because we have our hope set on the **living** God, who is the Savior of all people, especially of those who believe. |
| 2Ti 4:1 | living | V-PAP-APM | none recorded | 12365 | 0 | I charge you in the presence of God and of Christ Jesus, who is to judge the **living** and the dead, and by his appearing and his kingdom: |
| Heb 3:12 | living | V-PAP-GSM | none recorded | 12331, 14534, 16348, 18279, 18316, 18439 | 0 | Take care, brothers, lest there be in any of you an evil, unbelieving heart, leading you to fall away from the **living** God. |
| Heb 4:12 | living | V-PAP-NSM | none recorded | 12366, 18302 | 0 | For the word of God is **living** and active, sharper than any two-edged sword, piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart. |
| Heb 9:14 | living | V-PAP-DSM | none recorded | 12331, 16326, 18313 | 0 | how much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from dead works to serve the **living** God. |
| Heb 10:20 | living | V-PAP-ASF | none recorded | 16108 | 0 | by the new and **living** way that he opened for us through the curtain, that is, through his flesh, |
| Heb 10:31 | living | V-PAP-GSM | none recorded | 12331, 18439 | 0 | It is a fearful thing to fall into the hands of the **living** God. |
| Heb 12:22 | living | V-PAP-GSM | none recorded | - | 0 | But you have come to Mount Zion and to the city of the **living** God, the heavenly Jerusalem, and to innumerable angels in festal gathering, |
| 1Pe 1:3 | living | V-PAP-ASF | none recorded | 12366, 18302, 18391, 18645 | 0 | Blessed be the God and Father of our Lord Jesus Christ! According to his great mercy, he has caused us to be born again to a **living** hope through the resurrection of Jesus Christ from the dead, |
| 1Pe 2:4 | living | V-PAP-ASM | none recorded | 19727, 19946 | 0 | As you come to him, a **living** stone rejected by men but in the sight of God chosen and precious, |
| 1Pe 2:5 | living | V-PAP-NPM | none recorded | 12366, 18302 | 0 | you yourselves like **living** stones are being built up as a spiritual house, to be a holy priesthood, to offer spiritual sacrifices acceptable to God through Jesus Christ. |
| 1Pe 4:5 | living | V-PAP-APM | none recorded | 12365, 12392 | 0 | but they will give account to him who is ready to judge the **living** and the dead. |
| Rev 1:18 | living | V-PAP-NSM | none recorded | 12296, 18631 | 0 | and the **living** one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades. |
| Rev 7:2 | living | V-PAP-GSM | none recorded | - | 0 | Then I saw another angel ascending from the rising of the sun, with the seal of the **living** God, and he called with a loud voice to the four angels who had been given power to harm earth and sea, |
| Rev 7:17 | living | N-GSF | none recorded | 12354 | 0 | For the Lamb in the midst of the throne will be their shepherd, and he will guide them to springs of **living** water, and God will wipe away every tear from their eyes.” |
| Rev 16:3 | living | N-GSF | none recorded | 13985, 14964, 16039 | 0 | The second angel poured out his bowl into the sea, and it became like the blood of a corpse, and every **living** thing died that was in the sea. |

### 3.5 G3498 νεκρός nekros "dead": 121 own occurrences in 113 verses

- **Meaning as stored:** Greek; native word νεκρός, transliteration nekros; STEP gloss "dead"; sense head "dead" (the code is its own lemma).
- **Related terms (1):** G3499 nekroō "to put to death".
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 182; verses STEP attests 119; verse_lexical rows the parse found 127.

- **Carried by the member words:** dead (121).
- **Engagement of these occurrences:** none recorded 121.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 8:22 | dead | A-APM | none recorded | - | 0 | And Jesus said to him, “ Follow me, and leave the **dead** to bury their own dead.” |
| Mat 8:22 | dead | A-APM | none recorded | - | 0 | And Jesus said to him, “ Follow me, and leave the **dead** to bury their own dead.” |
| Mat 10:8 | dead | A-APM | none recorded | - | 0 | Heal the sick, raise the **dead**, cleanse lepers, cast out demons. You received without paying; give without pay. |
| Mat 11:5 | dead | A-NPM | none recorded | - | 0 | the blind receive their sight and the lame walk, lepers are cleansed and the deaf hear, and the **dead** are raised up, and the poor have good news preached to them. |
| Mat 14:2 | dead | A-GPM | none recorded | - | 0 | and he said to his servants, “ This is John the Baptist. He has been raised from the **dead**; that is why these miraculous powers are at work in him.” |
| Mat 17:9 | dead | A-GPM | none recorded | - | 0 | And as they were coming down the mountain, Jesus commanded them, “ Tell no one the vision, until the Son of Man is raised from the **dead**.” |
| Mat 22:31 | dead | A-GPM | none recorded | - | 0 | And as for the resurrection of the **dead**, have you not read what was said to you by God: |
| Mat 22:32 | dead | A-GPM | none recorded | - | 0 | ‘ I am the God of Abraham, and the God of Isaac, and the God of Jacob ’? He is not God of the **dead**, but of the living.” |
| Mat 27:64 | dead | A-GPM | none recorded | - | 0 | Therefore order the tomb to be made secure until the third day, lest his disciples go and steal him away and tell the people, ‘He has risen from the **dead**,’ and the last fraud will be worse than the first.” |
| Mat 28:4 | dead | A-NPM | none recorded | - | 0 | And for fear of him the guards trembled and became like **dead** men. |
| Mat 28:7 | dead | A-GPM | none recorded | - | 0 | Then go quickly and tell his disciples that he has risen from the **dead**, and behold, he is going before you to Galilee; there you will see him. See, I have told you.” |
| Mar 6:14 | dead | A-GPM | none recorded | - | 0 | King Herod heard of it, for Jesus ’ name had become known. Some said, “ John the Baptist has been raised from the **dead**. That is why these miraculous powers are at work in him.” |
| Mar 9:9 | dead | A-GPM | none recorded | - | 0 | And as they were coming down the mountain, he charged them to tell no one what they had seen, until the Son of Man had risen from the **dead**. |
| Mar 9:10 | dead | A-GPM | none recorded | - | 0 | So they kept the matter to themselves, questioning what this rising from the **dead** might mean. |
| Mar 12:25 | dead | A-GPM | none recorded | - | 0 | For when they rise from the **dead**, they neither marry nor are given in marriage, but are like angels in heaven. |
| Mar 12:26 | dead | A-GPM | none recorded | - | 0 | And as for the **dead** being raised, have you not read in the book of Moses, in the passage about the bush, how God spoke to him, saying, ‘ I am the God of Abraham, and the God of Isaac, and the God of Jacob ’? |
| Mar 12:27 | dead | A-GPM | none recorded | - | 0 | He is not God of the **dead**, but of the living. You are quite wrong.” |
| Luk 7:15 | dead | A-NSM | none recorded | - | 0 | And the **dead** man sat up and began to speak, and Jesus gave him to his mother. |
| Luk 7:22 | dead | A-NPM | none recorded | - | 0 | And he answered them, “ Go and tell John what you have seen and heard: the blind receive their sight, the lame walk, lepers are cleansed, and the deaf hear, the **dead** are raised up, the poor have good news preached to them. |
| Luk 9:7 | dead | A-GPM | none recorded | - | 0 | Now Herod the tetrarch heard about all that was happening, and he was perplexed, because it was said by some that John had been raised from the **dead**, |
| Luk 9:60 | dead | A-APM | none recorded | - | 0 | And Jesus said to him, “ Leave the **dead** to bury their own dead. But as for you, go and proclaim the kingdom of God.” |
| Luk 9:60 | dead | A-APM | none recorded | - | 0 | And Jesus said to him, “ Leave the **dead** to bury their own dead. But as for you, go and proclaim the kingdom of God.” |
| Luk 15:24 | dead | A-NSM | none recorded | - | 0 | For this my son was **dead**, and is alive again; he was lost, and is found.’ And they began to celebrate. |
| Luk 15:32 | dead | A-NSM | none recorded | - | 0 | It was fitting to celebrate and be glad, for this your brother was **dead**, and is alive; he was lost, and is found.’” |
| Luk 16:30 | dead | A-GPM | none recorded | - | 0 | And he said, ‘ No, father Abraham, but if someone goes to them from the **dead**, they will repent.’ |
| Luk 16:31 | dead | A-GPM | none recorded | - | 0 | He said to him, ‘ If they do not hear Moses and the Prophets, neither will they be convinced if someone should rise from the **dead**.’” |
| Luk 20:35 | dead | A-GPM | none recorded | - | 0 | but those who are considered worthy to attain to that age and to the resurrection from the **dead** neither marry nor are given in marriage, |
| Luk 20:37 | dead | A-NPM | none recorded | - | 0 | But that the **dead** are raised, even Moses showed, in the passage about the bush, where he calls the Lord the God of Abraham and the God of Isaac and the God of Jacob. |
| Luk 20:38 | dead | A-GPM | none recorded | - | 0 | Now he is not God of the **dead**, but of the living, for all live to him.” |
| Luk 24:5 | dead | A-GPM | none recorded | - | 0 | And as they were frightened and bowed their faces to the ground, the men said to them, “ Why do you seek the living among the **dead**? |
| Luk 24:46 | dead | A-GPM | none recorded | - | 0 | and said to them, “ Thus it is written, that the Christ should suffer and on the third day rise from the **dead**, |
| Joh 2:22 | dead | A-GPM | none recorded | - | 0 | When therefore he was raised from the **dead**, his disciples remembered that he had said this, and they believed the Scripture and the word that Jesus had spoken. |
| Joh 5:21 | dead | A-APM | none recorded | - | 0 | For as the Father raises the **dead** and gives them life, so also the Son gives life to whom he will. |
| Joh 5:25 | dead | A-NPM | none recorded | - | 0 | “ Truly, truly, I say to you, an hour is coming, and is now here, when the **dead** will hear the voice of the Son of God, and those who hear will live. |
| Joh 12:1 | dead | A-GPM | none recorded | - | 0 | Six days before the Passover, Jesus therefore came to Bethany, where Lazarus was, whom Jesus had raised from the **dead**. |
| Joh 12:9 | dead | A-GPM | none recorded | - | 0 | When the large crowd of the Jews learned that Jesus was there, they came, not only on account of him but also to see Lazarus, whom he had raised from the **dead**. |
| Joh 12:17 | dead | A-GPM | none recorded | - | 0 | The crowd that had been with him when he called Lazarus out of the tomb and raised him from the **dead** continued to bear witness. |
| Joh 20:9 | dead | A-GPM | none recorded | - | 0 | for as yet they did not understand the Scripture, that he must rise from the **dead**. |
| Joh 21:14 | dead | A-GPM | none recorded | - | 0 | This was now the third time that Jesus was revealed to the disciples after he was raised from the **dead**. |
| Act 3:15 | dead | A-GPM | none recorded | - | 0 | and you killed the Author of life, whom God raised from the **dead**. To this we are witnesses. |
| Act 4:2 | dead | A-GPM | none recorded | - | 0 | greatly annoyed because they were teaching the people and proclaiming in Jesus the resurrection from the **dead**. |
| Act 4:10 | dead | A-GPM | none recorded | - | 0 | let it be known to all of you and to all the people of Israel that by the name of Jesus Christ of Nazareth, whom you crucified, whom God raised from the **dead** — by him this man is standing before you well. |
| Act 5:10 | dead | A-ASF | none recorded | - | 0 | Immediately she fell down at his feet and breathed her last. When the young men came in they found her **dead**, and they carried her out and buried her beside her husband. |
| Act 10:41 | dead | A-GPM | none recorded | - | 0 | not to all the people but to us who had been chosen by God as witnesses, who ate and drank with him after he rose from the **dead**. |
| Act 10:42 | dead | A-GPM | none recorded | - | 0 | And he commanded us to preach to the people and to testify that he is the one appointed by God to be judge of the living and the **dead**. |
| Act 13:30 | dead | A-GPM | none recorded | - | 0 | But God raised him from the **dead**, |
| Act 13:34 | dead | A-GPM | none recorded | - | 0 | And as for the fact that he raised him from the **dead**,, no more to return to corruption, he has spoken in this way, “‘I will give you the holy and sure blessings of David.’ |
| Act 17:3 | dead | A-GPM | none recorded | - | 0 | explaining and proving that it was necessary for the Christ to suffer and to rise from the **dead**, and saying, “ This Jesus, whom I proclaim to you, is the Christ.” |
| Act 17:31 | dead | A-GPM | none recorded | - | 0 | because he has fixed a day on which he will judge the world in righteousness by a man whom he has appointed; and of this he has given assurance to all by raising him from the **dead**.” |
| Act 17:32 | dead | A-GPM | none recorded | - | 0 | Now when they heard of the resurrection of the **dead**, some mocked. But others said, “We will hear you again about this.” |
| Act 20:9 | dead | A-NSM | none recorded | - | 0 | And a young man named Eutychus, sitting at the window, sank into a deep sleep as Paul talked still longer. And being overcome by sleep, he fell down from the third story and was taken up **dead**. |
| Act 23:6 | dead | A-GPM | none recorded | - | 0 | Now when Paul perceived that one part were Sadducees and the other Pharisees, he cried out in the council, “ Brothers, I am a Pharisee, a son of Pharisees. It is with respect to the hope and the resurrection of the **dead** that I am on trial.” |
| Act 24:21 | dead | A-GPM | none recorded | - | 0 | other than this one thing that I cried out while standing among them: ‘It is with respect to the resurrection of the **dead** that I am on trial before you this day.’” |
| Act 26:8 | dead | A-APM | none recorded | - | 0 | Why is it thought incredible by any of you that God raises the **dead**? |
| Act 26:23 | dead | A-GPM | none recorded | - | 0 | that the Christ must suffer and that, by being the first to rise from the **dead**, he would proclaim light both to our people and to the Gentiles.” |
| Act 28:6 | dead | A-ASM | none recorded | - | 0 | They were waiting for him to swell up or suddenly fall down **dead**. But when they had waited a long time and saw no misfortune come to him, they changed their minds and said that he was a god. |
| Rom 1:4 | dead | A-GPM | none recorded | - | 0 | and was declared to be the Son of God in power according to the Spirit of holiness by his resurrection from the **dead**, Jesus Christ our Lord, |
| Rom 4:17 | dead | A-APM | none recorded | - | 0 | as it is written, “I have made you the father of many nations ”—in the presence of the God in whom he believed, who gives life to the **dead** and calls into existence the things that do not exist. |
| Rom 4:24 | dead | A-GPM | none recorded | - | 0 | but for ours also. It will be counted to us who believe in him who raised from the **dead** Jesus our Lord, |
| Rom 6:4 | dead | A-GPM | none recorded | - | 0 | We were buried therefore with him by baptism into death, in order that, just as Christ was raised from the **dead** by the glory of the Father, we too might walk in newness of life. |
| Rom 6:9 | dead | A-GPM | none recorded | - | 0 | We know that Christ, being raised from the **dead**, will never die again; death no longer has dominion over him. |
| Rom 6:11 | dead | A-APM | none recorded | - | 0 | So you also must consider yourselves **dead** to sin and alive to God in Christ Jesus. |
| Rom 7:4 | dead | A-GPM | none recorded | - | 0 | Likewise, my brothers, you also have died to the law through the body of Christ, so that you may belong to another, to him who has been raised from the **dead**, in order that we may bear fruit for God. |
| Rom 7:8 | dead | A-NSF | none recorded | - | 0 | But sin, seizing an opportunity through the commandment, produced in me all kinds of covetousness. For apart from the law, sin lies **dead**. |
| Rom 8:10 | dead | A-NSN | none recorded | - | 0 | But if Christ is in you, although the body is **dead** because of sin, the Spirit is life because of righteousness. |
| Rom 8:11 | dead | A-GPM | none recorded | - | 0 | If the Spirit of him who raised Jesus from the **dead** dwells in you, he who raised Christ Jesus from the dead will also give life to your mortal bodies through his Spirit who dwells in you. |
| Rom 8:11 | dead | A-GPM | none recorded | - | 0 | If the Spirit of him who raised Jesus from the **dead** dwells in you, he who raised Christ Jesus from the dead will also give life to your mortal bodies through his Spirit who dwells in you. |
| Rom 10:7 | dead | A-GPM | none recorded | - | 0 | “ or ‘ Who will descend into the abyss?’” (that is, to bring Christ up from the **dead** ). |
| Rom 10:9 | dead | A-GPM | none recorded | - | 0 | because, if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the **dead**, you will be saved. |
| Rom 11:15 | dead | A-GPM | none recorded | - | 0 | For if their rejection means the reconciliation of the world, what will their acceptance mean but life from the **dead**? |
| Rom 14:9 | dead | A-GPM | none recorded | - | 0 | For to this end Christ died and lived again, that he might be Lord both of the **dead** and of the living. |
| 1Cor 15:12 | dead | A-GPM | none recorded | - | 0 | Now if Christ is proclaimed as raised from the **dead**, how can some of you say that there is no resurrection of the dead? |
| 1Cor 15:12 | dead | A-GPM | none recorded | - | 0 | Now if Christ is proclaimed as raised from the **dead**, how can some of you say that there is no resurrection of the dead? |
| 1Cor 15:13 | dead | A-GPM | none recorded | - | 0 | But if there is no resurrection of the **dead**, then not even Christ has been raised. |
| 1Cor 15:15 | dead | A-NPM | none recorded | - | 0 | We are even found to be misrepresenting God, because we testified about God that he raised Christ, whom he did not raise if it is true that the **dead** are not raised. |
| 1Cor 15:16 | dead | A-NPM | none recorded | - | 0 | For if the **dead** are not raised, not even Christ has been raised. |
| 1Cor 15:20 | dead | A-GPM | none recorded | - | 0 | But in fact Christ has been raised from the **dead**, the firstfruits of those who have fallen asleep. |
| 1Cor 15:21 | dead | A-GPM | none recorded | - | 0 | For as by a man came death, by a man has come also the resurrection of the **dead**. |
| 1Cor 15:29 | dead | A-GPM | none recorded | - | 0 | Otherwise, what do people mean by being baptized on behalf of the **dead**? If the dead are not raised at all, why are people baptized on their behalf? |
| 1Cor 15:29 | dead | A-NPM | none recorded | - | 0 | Otherwise, what do people mean by being baptized on behalf of the **dead**? If the dead are not raised at all, why are people baptized on their behalf? |
| 1Cor 15:32 | dead | A-NPM | none recorded | - | 0 | What do I gain if, humanly speaking, I fought with beasts at Ephesus? If the **dead** are not raised, “Let us eat and drink, for tomorrow we die.” |
| 1Cor 15:35 | dead | A-NPM | none recorded | - | 0 | But someone will ask, “ How are the **dead** raised? With what kind of body do they come?” |
| 1Cor 15:42 | dead | A-GPM | none recorded | - | 0 | So is it with the resurrection of the **dead**. What is sown is perishable; what is raised is imperishable. |
| 1Cor 15:52 | dead | A-NPM | none recorded | - | 0 | in a moment, in the twinkling of an eye, at the last trumpet. For the trumpet will sound, and the **dead** will be raised imperishable, and we shall be changed. |
| 2Cor 1:9 | dead | A-APM | none recorded | - | 0 | Indeed, we felt that we had received the sentence of death. But that was to make us rely not on ourselves but on God who raises the **dead**. |
| Gal 1:1 | dead | A-GPM | none recorded | - | 0 | Paul, an apostle — not from men nor through man, but through Jesus Christ and God the Father, who raised him from the **dead** — |
| Eph 1:20 | dead | A-GPM | none recorded | - | 0 | that he worked in Christ when he raised him from the **dead** and seated him at his right hand in the heavenly places, |
| Eph 2:1 | dead | A-APM | none recorded | - | 0 | And you were **dead** in the trespasses and sins |
| Eph 2:5 | dead | A-APM | none recorded | - | 0 | even when we were **dead** in our trespasses, made us alive together with Christ — by grace you have been saved — |
| Eph 5:14 | dead | A-GPM | none recorded | - | 0 | for anything that becomes visible is light. Therefore it says, “ Awake, O sleeper, and arise from the **dead**, and Christ will shine on you.” |
| Phili 3:11 | dead | A-GPM | none recorded | - | 0 | that by any means possible I may attain the resurrection from the **dead**. |
| Col 1:18 | dead | A-GPM | none recorded | - | 0 | And he is the head of the body, the church. He is the beginning, the firstborn from the **dead**, that in everything he might be preeminent. |
| Col 2:12 | dead | A-GPM | none recorded | - | 0 | having been buried with him in baptism, in which you were also raised with him through faith in the powerful working of God, who raised him from the **dead**. |
| Col 2:13 | dead | A-APM | none recorded | - | 0 | And you, who were **dead** in your trespasses and the uncircumcision of your flesh, God made alive together with him, having forgiven us all our trespasses, |
| 1Th 1:10 | dead | A-GPM | none recorded | - | 0 | and to wait for his Son from heaven, whom he raised from the **dead**, Jesus who delivers us from the wrath to come. |
| 1Th 4:16 | dead | A-NPM | none recorded | - | 0 | For the Lord himself will descend from heaven with a cry of command, with the voice of an archangel, and with the sound of the trumpet of God. And the **dead** in Christ will rise first. |
| 2Ti 2:8 | dead | A-GPM | none recorded | - | 0 | Remember Jesus Christ, risen from the **dead**, the offspring of David, as preached in my gospel, |
| 2Ti 4:1 | dead | A-APM | none recorded | - | 0 | I charge you in the presence of God and of Christ Jesus, who is to judge the living and the **dead**, and by his appearing and his kingdom: |
| Heb 6:1 | dead | A-GPN | none recorded | - | 0 | Therefore let us leave the elementary doctrine of Christ and go on to maturity, not laying again a foundation of repentance from **dead** works and of faith toward God, |
| Heb 6:2 | dead | A-GPM | none recorded | - | 0 | and of instruction about washings, the laying on of hands, the resurrection of the **dead**, and eternal judgment. |
| Heb 9:14 | dead | A-GPN | none recorded | - | 0 | how much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from **dead** works to serve the living God. |
| Heb 11:19 | dead | A-GPM | none recorded | - | 0 | He considered that God was able even to raise him from the **dead**, from which, figuratively speaking, he did receive him back. |
| Heb 11:35 | dead | A-APM | none recorded | - | 0 | Women received back their **dead** by resurrection. Some were tortured, refusing to accept release, so that they might rise again to a better life. |
| Heb 13:20 | dead | A-GPM | none recorded | - | 0 | Now may the God of peace who brought again from the **dead** our Lord Jesus, the great shepherd of the sheep, by the blood of the eternal covenant, |
| Jam 2:17 | dead | A-NSF | none recorded | - | 0 | So also faith by itself, if it does not have works, is **dead**. |
| Jam 2:26 | dead | A-NSN | none recorded | - | 0 | For as the body apart from the spirit is **dead**, so also faith apart from works is dead. |
| Jam 2:26 | dead | A-NSF | none recorded | - | 0 | For as the body apart from the spirit is **dead**, so also faith apart from works is dead. |
| 1Pe 1:3 | dead | A-GPM | none recorded | - | 0 | Blessed be the God and Father of our Lord Jesus Christ! According to his great mercy, he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the **dead**, |
| 1Pe 1:21 | dead | A-GPM | none recorded | - | 0 | who through him are believers in God, who raised him from the **dead** and gave him glory, so that your faith and hope are in God. |
| 1Pe 4:5 | dead | A-APM | none recorded | - | 0 | but they will give account to him who is ready to judge the living and the **dead**. |
| 1Pe 4:6 | dead | A-DPM | none recorded | - | 0 | For this is why the gospel was preached even to those who are **dead**, that though judged in the flesh the way people are, they might live in the spirit the way God does. |
| Rev 1:5 | dead | A-GPM | none recorded | - | 0 | and from Jesus Christ the faithful witness, the firstborn of the **dead**, and the ruler of kings on earth. To him who loves us and has freed us from our sins by his blood |
| Rev 1:17 | dead | A-NSM | none recorded | - | 0 | When I saw him, I fell at his feet as though **dead**. But he laid his right hand on me, saying, “ Fear not, I am the first and the last, |
| Rev 3:1 | dead | A-NSM | none recorded | - | 0 | “ And to the angel of the church in Sardis write: ‘ The words of him who has the seven spirits of God and the seven stars. “‘I know your works. You have the reputation of being alive, but you are **dead**. |
| Rev 11:18 | dead | A-GPM | none recorded | - | 0 | The nations raged, but your wrath came, and the time for the **dead** to be judged, and for rewarding your servants, the prophets and saints, and those who fear your name, both small and great, and for destroying the destroyers of the earth.” |
| Rev 14:13 | dead | A-NPM | none recorded | - | 0 | And I heard a voice from heaven saying, “ Write this: Blessed are the **dead** who die in the Lord from now on.” “Blessed indeed,” says the Spirit, “ that they may rest from their labors, for their deeds follow them!” |
| Rev 20:5 | dead | A-GPM | none recorded | - | 0 | The rest of the **dead** did not come to life until the thousand years were ended. This is the first resurrection. |
| Rev 20:12 | dead | A-APM | none recorded | - | 0 | And I saw the **dead**, great and small, standing before the throne, and books were opened. Then another book was opened, which is the book of life. And the dead were judged by what was written in the books, according to what they had done. |
| Rev 20:12 | dead | A-NPM | none recorded | - | 0 | And I saw the **dead**, great and small, standing before the throne, and books were opened. Then another book was opened, which is the book of life. And the dead were judged by what was written in the books, according to what they had done. |
| Rev 20:13 | dead | A-APM | none recorded | - | 0 | And the sea gave up the **dead** who were in it, Death and Hades gave up the dead who were in them, and they were judged, each one of them, according to what they had done. |
| Rev 20:13 | dead | A-APM | none recorded | - | 0 | And the sea gave up the **dead** who were in it, Death and Hades gave up the dead who were in them, and they were judged, each one of them, according to what they had done. |

### 3.6 H4191 מוּת mut "to die": 89 own occurrences in 80 verses

- **Meaning as stored:** Hebrew; native word מוּת, transliteration mut; STEP gloss "to die"; sense head "to die" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4191):** to die, kill, have one executed.
- **Related terms (4):** H4192 lab.ben "[Muth-]labben"; H4194 ma.vet "death"; H4463 ma.mot "death"; H8546 te.mu.tah "death".
- **Clusters (cluster_strong):** T3 Operations (None); M25 Life & Death (high).
- **Counts, three measures as stored:** STEP token count 849; verses STEP attests 699; verse_lexical rows the parse found 840.

- **Carried by the member words:** dead (89).
- **Engagement of these occurrences:** none recorded 89.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 23:3 | dead | HVqrmsc | none recorded | - | 0 | And Abraham rose up from before his **dead** and said to the Hittites, |
| Gen 23:4 | dead | HVqrmsc | none recorded | - | 0 | “I am a sojourner and foreigner among you; give me property among you for a burying place, that I may bury my **dead** out of my sight.” |
| Gen 23:6 | dead | HVqrmsc | none recorded | - | 0 | “Hear us, my lord; you are a prince of God among us. Bury your **dead** in the choicest of our tombs. None of us will withhold from you his tomb to hinder you from burying your dead.” |
| Gen 23:11 | dead | HVqrmsc | none recorded | - | 0 | “ No, my lord, hear me: I give you the field, and I give you the cave that is in it. In the sight of the sons of my people I give it to you. Bury your **dead**.” |
| Gen 42:38 | dead | HVqrmsa | none recorded | - | 0 | But he said, “My son shall not go down with you, for his brother is **dead**, and he is the only one left. If harm should happen to him on the journey that you are to make, you would bring down my gray hairs with sorrow to Sheol.” |
| Gen 44:20 | dead | HVqp3ms | none recorded | - | 0 | And we said to my lord, ‘We have a father, an old man, and a young brother, the child of his old age. His brother is **dead**, and he alone is left of his mother’s children, and his father loves him.’ |
| Gen 50:15 | dead | HVqp3ms | none recorded | - | 0 | When Joseph’s brothers saw that their father was **dead**, they said, “It may be that Joseph will hate us and pay us back for all the evil that we did to him.” |
| Exo 9:7 | dead | HVqp3ms | none recorded | 16213 | 0 | And Pharaoh sent, and behold, not one of the livestock of Israel was **dead**. But the heart of Pharaoh was hardened, and he did not let the people go. |
| Exo 12:30 | dead | HVqrmsa | none recorded | - | 0 | And Pharaoh rose up in the night, he and all his servants and all the Egyptians. And there was a great cry in Egypt, for there was not a house where someone was not **dead**. |
| Exo 12:33 | dead | HVqrmpa | none recorded | 18521 | 0 | The Egyptians were urgent with the people to send them out of the land in haste. For they said, “We shall all be **dead**.” |
| Exo 14:30 | dead | HVqrmsa | none recorded | - | 0 | Thus the Lord saved Israel that day from the hand of the Egyptians, and Israel saw the Egyptians **dead** on the seashore. |
| Exo 21:34 | dead | HVqrmsa | none recorded | - | 0 | the owner of the pit shall make restoration. He shall give money to its owner, and the **dead** beast shall be his. |
| Exo 21:36 | dead | HVqrmsa | none recorded | - | 0 | Or if it is known that the ox has been accustomed to gore in the past, and its owner has not kept it in, he shall repay ox for ox, and the **dead** beast shall be his. |
| Lev 21:11 | dead | HVqrmsa | none recorded | 16039, 16190, 16494, 16672, 18264, 18354 | 0 | He shall not go in to any **dead** bodies nor make himself unclean, even for his father or for his mother. |
| Num 6:6 | dead | HVqrmsa | none recorded | 16039, 16190, 17255 | 0 | “ All the days that he separates himself to the Lord he shall not go near a **dead** body. |
| Num 12:12 | dead | HVqrmsa | none recorded | 12292, 16191 | 0 | Let her not be as one **dead**, whose flesh is half eaten away when he comes out of his mother’s womb.” |
| Num 16:48 | dead | HVqrmpa | none recorded | 13019, 13543, 14538 | 0 | And he stood between the **dead** and the living, and the plague was stopped. |
| Num 19:11 | dead | HVqrmsa | none recorded | 12394, 16039, 16190, 16494, 16672, 17255, 17280, 18354 | 0 | “Whoever touches the **dead** body of any person shall be unclean seven days. |
| Num 19:13 | dead | HVqrmsa | none recorded | 16039, 16190, 16494, 16672, 17280, 18354 | 0 | Whoever touches a **dead** person, the body of anyone who has died, and does not cleanse himself, defiles the tabernacle of the Lord, and that person shall be cut off from Israel; because the water for impurity was not thrown on him, he shall be unclean. His uncleanness is still on him. |
| Deu 2:16 | dead | HVqcc | none recorded | - | 0 | “So as soon as all the men of war had perished and were **dead** from among the people, |
| Deu 14:1 | dead | HVqrmsa | none recorded | 18520 | 0 | “You are the sons of the Lord your God. You shall not cut yourselves or make any baldness on your foreheads for the **dead**. |
| Deu 25:6 | dead | HVqrmsa | none recorded | - | 0 | And the first son whom she bears shall succeed to the name of his **dead** brother, that his name may not be blotted out of Israel. |
| Jos 1:2 | dead | HVqp3ms | none recorded | - | 0 | “ Moses my servant is **dead**. Now therefore arise, go over this Jordan, you and all this people, into the land that I am giving to them, to the people of Israel. |
| Judg 3:25 | dead | HVqrmsa | none recorded | - | 0 | And they waited till they were embarrassed. But when he still did not open the doors of the roof chamber, they took the key and opened them, and there lay their lord **dead** on the floor. |
| Judg 4:22 | dead | HVqrmsa | none recorded | - | 0 | And behold, as Barak was pursuing Sisera, Jael went out to meet him and said to him, “ Come, and I will show you the man whom you are seeking.” So he went in to her tent, and there lay Sisera **dead**, with the tent peg in his temple. |
| Judg 20:5 | dead | HVqw3fs | none recorded | - | 0 | And the leaders of Gibeah rose against me and surrounded the house against me by night. They meant to kill me, and they violated my concubine, and she is **dead**. |
| Rut 4:5 | dead | HVqrmsa | none recorded | - | 0 | Then Boaz said, “The day you buy the field from the hand of Naomi, you also acquire Ruth the Moabite, the widow of the **dead**, in order to perpetuate the name of the dead in his inheritance.” |
| Rut 4:5 | dead | HVqrmsa | none recorded | - | 0 | Then Boaz said, “The day you buy the field from the hand of Naomi, you also acquire Ruth the Moabite, the widow of the **dead**, in order to perpetuate the name of the dead in his inheritance.” |
| Rut 4:10 | dead | HVqrmsa | none recorded | - | 0 | Also Ruth the Moabite, the widow of Mahlon, I have bought to be my wife, to perpetuate the name of the **dead** in his inheritance, that the name of the dead may not be cut off from among his brothers and from the gate of his native place. You are witnesses this day.” |
| Rut 4:10 | dead | HVqrmsa | none recorded | - | 0 | Also Ruth the Moabite, the widow of Mahlon, I have bought to be my wife, to perpetuate the name of the **dead** in his inheritance, that the name of the dead may not be cut off from among his brothers and from the gate of his native place. You are witnesses this day.” |
| 1Sa 4:17 | dead | HVqp3cp | none recorded | - | 0 | He who brought the news answered and said, “ Israel has fled before the Philistines, and there has also been a great defeat among the people. Your two sons also, Hophni and Phinehas, are **dead**, and the ark of God has been captured.” |
| 1Sa 4:19 | dead | HVqq3ms | none recorded | - | 0 | Now his daughter-in-law, the wife of Phinehas, was pregnant, about to give birth. And when she heard the news that the ark of God was captured, and that her father-in-law and her husband were **dead**, she bowed and gave birth, for her pains came upon her. |
| 1Sa 17:51 | dead | HVqp3ms | none recorded | - | 0 | Then David ran and stood over the Philistine and took his sword and drew it out of its sheath and killed him and cut off his head with it. When the Philistines saw that their champion was **dead**, they fled. |
| 1Sa 24:14 | dead | HVqrmsa | none recorded | 12293 | 0 | After whom has the king of Israel come out? After whom do you pursue? After a **dead** dog! After a flea! |
| 1Sa 31:5 | dead | HVqp3ms | none recorded | - | 0 | And when his armor-bearer saw that Saul was **dead**, he also fell upon his sword and died with him. |
| 1Sa 31:7 | dead | HVqp3cp | none recorded | - | 0 | And when the men of Israel who were on the other side of the valley and those beyond the Jordan saw that the men of Israel had fled and that Saul and his sons were **dead**, they abandoned their cities and fled. And the Philistines came and lived in them. |
| 2Sa 1:4 | dead | HVqw3mp | none recorded | - | 0 | And David said to him, “ How did it go? Tell me.” And he answered, “The people fled from the battle, and also many of the people have fallen and are **dead**, and Saul and his son Jonathan are also dead.” |
| 2Sa 1:4 | dead | HVqp3cp | none recorded | - | 0 | And David said to him, “ How did it go? Tell me.” And he answered, “The people fled from the battle, and also many of the people have fallen and are **dead**, and Saul and his son Jonathan are also dead.” |
| 2Sa 9:8 | dead | HVqrmsa | none recorded | 12293, 18262, 18269 | 0 | And he paid homage and said, “ What is your servant, that you should show regard for a **dead** dog such as I?” |
| 2Sa 11:21 | dead | HVqp3ms | none recorded | 14199 | 0 | Who killed Abimelech the son of Jerubbesheth? Did not a woman cast an upper millstone on him from the wall, so that he died at Thebez? Why did you go so near the wall?’ then you shall say, ‘Your servant Uriah the Hittite is **dead** also.’” |
| 2Sa 11:24 | dead | HVqw3mp | none recorded | - | 0 | Then the archers shot at your servants from the wall. Some of the king’s servants are **dead**, and your servant Uriah the Hittite is dead also.” |
| 2Sa 11:24 | dead | HVqp3ms | none recorded | - | 0 | Then the archers shot at your servants from the wall. Some of the king’s servants are **dead**, and your servant Uriah the Hittite is dead also.” |
| 2Sa 12:19 | dead | HVqp3ms | none recorded | 18280, 18520 | 0 | But when David saw that his servants were whispering together, David understood that the child was **dead**. And David said to his servants, “Is the child dead?” They said, “He is dead.” |
| 2Sa 12:19 | dead | HVqp3ms | none recorded | 18280, 18520 | 0 | But when David saw that his servants were whispering together, David understood that the child was **dead**. And David said to his servants, “Is the child dead?” They said, “He is dead.” |
| 2Sa 12:23 | dead | HVqp3ms | none recorded | 12281, 12320, 18247, 18613 | 0 | But now he is **dead**. Why should I fast? Can I bring him back again? I shall go to him, but he will not return to me.” |
| 2Sa 13:32 | dead | HVqp3ms | none recorded | - | 0 | But Jonadab the son of Shimeah, David’s brother, said, “Let not my lord suppose that they have killed all the young men, the king’s sons, for Amnon alone is **dead**. For by the command of Absalom this has been determined from the day he violated his sister Tamar. |
| 2Sa 13:33 | dead | HVqp3cp | none recorded | - | 0 | Now therefore let not my lord the king so take it to heart as to suppose that all the king’s sons are **dead**, for Amnon alone is dead.” |
| 2Sa 13:33 | dead | HVqp3ms | none recorded | - | 0 | Now therefore let not my lord the king so take it to heart as to suppose that all the king’s sons are **dead**, for Amnon alone is dead.” |
| 2Sa 13:39 | dead | HVqp3ms | none recorded | 12320, 14214 | 0 | And the spirit of the king longed to go out to Absalom, because he was comforted about Amnon, since he was **dead**. |
| 2Sa 16:9 | dead | HVqrmsa | none recorded | 12293, 18269 | 0 | Then Abishai the son of Zeruiah said to the king, “ Why should this **dead** dog curse my lord the king? Let me go over and take off his head.” |
| 2Sa 18:20 | dead | HVqp3ms | none recorded | - | 0 | And Joab said to him, “ You are not to carry news today. You may carry news another day, but today you shall carry no news, because the king’s son is **dead**.” |
| 2Sa 19:6 | dead | HVqrmpa | none recorded | 12368, 18520 | 0 | because you love those who hate you and hate those who love you. For you have made it clear today that commanders and servants are nothing to you, for today I know that if Absalom were alive and all of us were **dead** today, then you would be pleased. |
| 2Sa 19:10 | dead | HVqp3ms | none recorded | - | 0 | But Absalom, whom we anointed over us, is **dead** in battle. Now therefore why do you say nothing about bringing the king back?” |
| 1Ki 3:20 | dead | HVqrmsa | none recorded | - | 0 | And she arose at midnight and took my son from beside me, while your servant slept, and laid him at her breast, and laid her **dead** son at my breast. |
| 1Ki 3:21 | dead | HVqp3ms | none recorded | - | 0 | When I rose in the morning to nurse my child, behold, he was **dead**. But when I looked at him closely in the morning, behold, he was not the child that I had borne.” |
| 1Ki 3:22 | dead | HVqrmsa | none recorded | 18280 | 0 | But the other woman said, “ No, the living child is mine, and the **dead** child is yours.” The first said, “ No, the dead child is yours, and the living child is mine.” Thus they spoke before the king. |
| 1Ki 3:22 | dead | HVqrmsa | none recorded | 18280 | 0 | But the other woman said, “ No, the living child is mine, and the **dead** child is yours.” The first said, “ No, the dead child is yours, and the living child is mine.” Thus they spoke before the king. |
| 1Ki 3:23 | dead | HVqrmsa | none recorded | 18280 | 0 | Then the king said, “The one says, ‘ This is my son that is alive, and your son is **dead** ’; and the other says, ‘ No; but your son is dead, and my son is the living one.’” |
| 1Ki 3:23 | dead | HVqrmsa | none recorded | 18280 | 0 | Then the king said, “The one says, ‘ This is my son that is alive, and your son is **dead** ’; and the other says, ‘ No; but your son is dead, and my son is the living one.’” |
| 1Ki 21:14 | dead | HVqw3ms | none recorded | - | 0 | Then they sent to Jezebel, saying, “ Naboth has been stoned; he is **dead**.” |
| 1Ki 21:15 | dead | HVqw3ms | none recorded | - | 0 | As soon as Jezebel heard that Naboth had been stoned and was **dead**, Jezebel said to Ahab, “ Arise, take possession of the vineyard of Naboth the Jezreelite, which he refused to give you for money, for Naboth is not alive, but dead.” |
| 1Ki 21:15 | dead | HVqp3ms | none recorded | - | 0 | As soon as Jezebel heard that Naboth had been stoned and was **dead**, Jezebel said to Ahab, “ Arise, take possession of the vineyard of Naboth the Jezreelite, which he refused to give you for money, for Naboth is not alive, but dead.” |
| 1Ki 21:16 | dead | HVqp3ms | none recorded | 14176 | 0 | And as soon as Ahab heard that Naboth was **dead**, Ahab arose to go down to the vineyard of Naboth the Jezreelite, to take possession of it. |
| 2Ki 4:1 | dead | HVqp3ms | none recorded | - | 0 | Now the wife of one of the sons of the prophets cried to Elisha, “Your servant my husband is **dead**, and you know that your servant feared the Lord, but the creditor has come to take my two children to be his slaves.” |
| 2Ki 4:32 | dead | HVqrmsa | none recorded | 12384, 18346 | 0 | When Elisha came into the house, he saw the child lying **dead** on his bed. |
| 2Ki 11:1 | dead | HVqp3ms | none recorded | - | 0 | Now when Athaliah the mother of Ahaziah saw that her son was **dead**, she arose and destroyed all the royal family. |
| 2Ki 19:35 | dead | HVqrmpa | none recorded | - | 0 | And that night the angel of the Lord went out and struck down 185,000 in the camp of the Assyrians. And when people arose early in the morning, behold, these were all **dead** bodies. |
| 2Ki 23:30 | dead | HVqrmsa | none recorded | - | 0 | And his servants carried him **dead** in a chariot from Megiddo and brought him to Jerusalem and buried him in his own tomb. And the people of the land took Jehoahaz the son of Josiah, and anointed him, and made him king in his father’s place. |
| 2Ch 22:10 | dead | HVqp3ms | none recorded | - | 0 | Now when Athaliah the mother of Ahaziah saw that her son was **dead**, she arose and destroyed all the royal family of the house of Judah. |
| Job 1:19 | dead | HVqw3mp | none recorded | 16194 | 0 | and behold, a great wind came across the wilderness and struck the four corners of the house, and it fell upon the young people, and they are **dead**, and I alone have escaped to tell you.” |
| Psa 31:12 | dead | HVqrmsa | none recorded | 16160 | 0 | I have been forgotten like one who is **dead**; I have become like a broken vessel. |
| Psa 88:5 | dead | HVqrmpa | none recorded | 12292, 18262 | 0 | like one set loose among the **dead**, like the slain that lie in the grave, like those whom you remember no more, for they are cut off from your hand. |
| Psa 88:10 | dead | HVqrmpa | none recorded | 12280, 18475 | 0 | Do you work wonders for the **dead**? Do the departed rise up to praise you? Selah |
| Psa 106:28 | dead | HVqrmpa | none recorded | 12323, 18532 | 0 | Then they yoked themselves to the Baal of Peor, and ate sacrifices offered to the **dead**; |
| Psa 115:17 | dead | HVqrmpa | none recorded | 12280, 18247, 18271, 18273, 18612 | 0 | The **dead** do not praise the Lord, nor do any who go down into silence. |
| Psa 143:3 | dead | HVqrmpc | none recorded | 12292, 12371, 18262 | 0 | For the enemy has pursued my soul; he has crushed my life to the ground; he has made me sit in darkness like those long **dead**. |
| Ecc 4:2 | dead | HVqp3cp | none recorded | - | 0 | And I thought the **dead** who are already dead more fortunate than the living who are still alive. |
| Ecc 9:3 | dead | HVqrmpa | none recorded | 12347, 12395, 16184, 18274, 18361 | 0 | This is an evil in all that is done under the sun, that the same event happens to all. Also, the hearts of the children of man are full of evil, and madness is in their hearts while they live, and after that they go to the **dead**. |
| Ecc 9:4 | dead | HVqrmsa | none recorded | 12280, 12347, 16184 | 0 | But he who is joined with all the living has hope, for a living dog is better than a **dead** lion. |
| Ecc 9:5 | dead | HVqrmpa | none recorded | 16184, 18272, 18273, 18314, 18612 | 0 | For the living know that they will die, but the **dead** know nothing, and they have no more reward, for the memory of them is forgotten. |
| Isa 22:2 | dead | HVqrmpc | none recorded | - | 0 | you who are full of shoutings, tumultuous city, exultant town? Your slain are not slain with the sword or **dead** in battle. |
| Isa 26:14 | dead | HVqrmpa | none recorded | 12255, 12383, 18346, 18603 | 0 | They are **dead**, they will not live; they are shades, they will not arise; to that end you have visited them with destruction and wiped out all remembrance of them. |
| Isa 26:19 | dead | HVqrmpc | none recorded | 12255, 12383, 14677, 18603, 18797 | 0 | Your **dead** shall live; their bodies shall rise. You who dwell in the dust, awake and sing for joy! For your dew is a dew of light, and the earth will give birth to the dead. |
| Isa 37:36 | dead | HVqrmpa | none recorded | - | 0 | And the angel of the Lord went out and struck down 185,000 in the camp of the Assyrians. And when people arose early in the morning, behold, these were all **dead** bodies. |
| Isa 59:10 | dead | HVqrmpa | none recorded | 12292 | 0 | We grope for the wall like the blind; we grope like those who have no eyes; we stumble at noon as in the twilight, among those in full vigor we are like **dead** men. |
| Jer 22:10 | dead | HVqrmsa | none recorded | 12320 | 0 | Weep not for him who is **dead**, nor grieve for him, but weep bitterly for him who goes away, for he shall return no more to see his native land. |
| Lam 3:6 | dead | HVqrmpc | none recorded | 12292, 18472 | 0 | he has made me dwell in darkness like the **dead** of long ago. |
| Eze 24:17 | dead | HVqrmpa | none recorded | 12320 | 0 | Sigh, but not aloud; make no mourning for the **dead**. Bind on your turban, and put your shoes on your feet; do not cover your lips, nor eat the bread of men.” |
| Eze 44:25 | dead | HVqrmsc | none recorded | 18264 | 0 | They shall not defile themselves by going near to a **dead** person. However, for father or mother, for son or daughter, for brother or unmarried sister they may defile themselves. |

### 3.7 H5315H נֶ֫פֶשׁ ne.phesh "soul: life": 24 own occurrences in 24 verses

- **Meaning as stored:** Hebrew; native word נֶ֫פֶשׁ, transliteration ne.phesh; STEP gloss "soul: life"; sense head "soul: life" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5315):** soul, self, life, creature, person, appetite, mind, living being, desi ... (cut; the whole text is in the workbook).
- **Related terms (11):** H5305 na.phish "Naphish"; H5314 na.phash "be refreshed"; H5315G ne.phesh "soul"; H5315I ne.phesh "soul: myself"; H5315J ne.phesh "soul: person"; H5315K ne.phesh "soul: animal"; more in the workbook.
- **Clusters (cluster_strong):** M47 Inner Seat (heuristic).
- **Counts, three measures as stored:** STEP token count 211; verses STEP attests 180; verse_lexical rows the parse found 207.

- **Carried by the member words:** lives (22), alive (1), deadly (1).
- **Engagement of these occurrences:** none recorded 24.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ch 5:21 | alive | HNcfsc | none recorded | - | 0 | They carried off their livestock: 50,000 of their camels, 250,000 sheep, 2,000 donkeys, and 100,000 men **alive**. |
| Psa 17:9 | deadly | HNcfsa | none recorded | 19343 | 0 | from the wicked who do me violence, my **deadly** enemies who surround me. |
| Num 16:38 | lives | HNcfpc | none recorded | 16565 | 0 | As for the censers of these men who have sinned at the cost of their **lives**, let them be made into hammered plates as a covering for the altar, for they offered them before the Lord, and they became holy. Thus they shall be a sign to the people of Israel.” |
| Jos 9:24 | lives | HNcfpc | none recorded | - | 0 | They answered Joshua, “Because it was told to your servants for a certainty that the Lord your God had commanded his servant Moses to give you all the land and to destroy all the inhabitants of the land from before you—so we feared greatly for our **lives** because of you and did this thing. |
| Judg 5:18 | lives | HNcfsc | none recorded | 16211, 16706, 16884, 18518, 18944 | 0 | Zebulun is a people who risked their **lives** to the death; Naphtali, too, on the heights of the field. |
| Judg 18:25 | lives | HNcfsc | none recorded | - | 0 | And the people of Dan said to him, “Do not let your voice be heard among us, lest angry fellows fall upon you, and you lose your life with the **lives** of your household.” |
| 2Sa 19:5 | lives | HNcfsc | none recorded | - | 0 | Then Joab came into the house to the king and said, “You have today covered with shame the faces of all your servants, who have this day saved your life and the **lives** of your sons and your daughters and the lives of your wives and your concubines, |
| 2Sa 23:17 | lives | HNcfpc | none recorded | 20134, 20151, 20152 | 0 | and said, “ Far be it from me, O Lord, that I should do this. Shall I drink the blood of the men who went at the risk of their **lives**?” Therefore he would not drink it. These things the three mighty men did. |
| Psa 72:13 | lives | HNcfpc | none recorded | 16718 | 0 | He has pity on the weak and the needy, and saves the **lives** of the needy. |
| Psa 97:10 | lives | HNcfpc | none recorded | - | 0 | O you who love the Lord, hate evil! He preserves the **lives** of his saints; he delivers them from the hand of the wicked. |
| Pro 1:18 | lives | HNcfpc | none recorded | - | 0 | but these men lie in wait for their own blood; they set an ambush for their own **lives**. |
| Pro 14:25 | lives | HNcfpa | none recorded | 16464, 16610 | 0 | A truthful witness saves **lives**, but one who breathes out lies is deceitful. |
| Jer 17:21 | lives | HNcfpc | none recorded | 16797 | 0 | Thus says the Lord: Take care for the sake of your **lives**, and do not bear a burden on the Sabbath day or bring it in by the gates of Jerusalem. |
| Jer 21:7 | lives | HNcfsc | none recorded | - | 0 | Afterward, declares the Lord, I will give Zedekiah king of Judah and his servants and the people in this city who survive the pestilence, sword, and famine into the hand of Nebuchadnezzar king of Babylon and into the hand of their enemies, into the hand of those who seek their **lives**. He shall strike them down with the edge of the sword. He shall not pity them or spare them or have compassion.’ |
| Jer 34:20 | lives | HNcfsc | none recorded | - | 0 | And I will give them into the hand of their enemies and into the hand of those who seek their **lives**. Their dead bodies shall be food for the birds of the air and the beasts of the earth. |
| Jer 34:21 | lives | HNcfsc | none recorded | - | 0 | And Zedekiah king of Judah and his officials I will give into the hand of their enemies and into the hand of those who seek their **lives**, into the hand of the army of the king of Babylon which has withdrawn from you. |
| Jer 42:20 | lives | HNcfpc | none recorded | 13976, 14722, 14937 | 0 | that you have gone astray at the cost of your **lives**. For you sent me to the Lord your God, saying, ‘ Pray for us to the Lord our God, and whatever the Lord our God says, declare to us and we will do it.’ |
| Lam 2:19 | lives | HNcfsc | none recorded | 14726, 16154 | 0 | “ Arise, cry out in the night, at the beginning of the night watches! Pour out your heart like water before the presence of the Lord! Lift your hands to him for the **lives** of your children, who faint for hunger at the head of every street.” |
| Lam 5:9 | lives | HNcfsc | none recorded | - | 0 | We get our bread at the peril of our **lives**, because of the sword in the wilderness. |
| Eze 14:14 | lives | HNcfsc | none recorded | 16525 | 0 | even if these three men, Noah, Daniel, and Job, were in it, they would deliver but their own **lives** by their righteousness, declares the Lord God. |
| Eze 14:20 | lives | HNcfsc | none recorded | 13972, 14692, 14947, 16525 | 0 | even if Noah, Daniel, and Job were in it, as I live, declares the Lord God, they would deliver neither son nor daughter. They would deliver but their own **lives** by their righteousness. |
| Eze 17:17 | lives | HNcfpa | none recorded | - | 0 | Pharaoh with his mighty army and great company will not help him in war, when mounds are cast up and siege walls built to cut off many **lives**. |
| Eze 22:25 | lives | HNcfsa | none recorded | 13972, 14692, 14951, 16782 | 0 | The conspiracy of her prophets in her midst is like a roaring lion tearing the prey; they have devoured human **lives**; they have taken treasure and precious things; they have made many widows in her midst. |
| Eze 22:27 | lives | HNcfpa | none recorded | 17071 | 0 | Her princes in her midst are like wolves tearing the prey, shedding blood, destroying **lives** to get dishonest gain. |

### 3.8 H2416E חַיִּים chay.yim "life": 18 own occurrences in 18 verses

- **Meaning as stored:** Hebrew; native word חַיִּים, transliteration chay.yim; STEP gloss "life"; sense head "life" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2416):** living thing, animal.
- **Related terms (23):** H2416A chay "alive"; H2416B chay "kinsfolk"; H2416C chay.yah "living thing"; H2416D chay.yah "community"; H2419 chi.el "Hiel"; H2421 cha.yah "to live"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 151; verses STEP attests 0; verse_lexical rows the parse found 143.

- **Carried by the member words:** live (11), lives (3), lived (2), alive (1), living (1).
- **Engagement of these occurrences:** none recorded 18.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lam 3:53 | alive | HNcmpc | none recorded | - | 0 | they flung me **alive** into the pit and cast stones on me; |
| Deu 30:6 | live | HNcmpc | none recorded | 12338 | 0 | And the Lord your God will circumcise your heart and the heart of your offspring, so that you will love the Lord your God with all your heart and with all your soul, that you may **live**. |
| 2Sa 19:34 | live | HNcmpc | none recorded | 12337 | 0 | But Barzillai said to the king, “ How many years have I still to **live**, that I should go up with the king to Jerusalem? |
| Psa 63:4 | live | HNcmpc | none recorded | 12351 | 0 | So I will bless you as long as I **live**; in your name I will lift up my hands. |
| Psa 104:33 | live | HNcmpc | none recorded | 12351 | 0 | I will sing to the Lord as long as I **live**; I will sing praise to my God while I have being. |
| Psa 146:2 | live | HNcmpc | none recorded | 12351, 18292 | 0 | I will praise the Lord as long as I **live**; I will sing praises to my God while I have my being. |
| Pro 11:19 | live | HNcmpa | none recorded | 12316 | 0 | Whoever is steadfast in righteousness will **live**, but he who pursues evil will die. |
| Ecc 3:12 | live | HNcmpc | none recorded | 12348 | 0 | I perceived that there is nothing better for them than to be joyful and to do good as long as they **live**; |
| Ecc 9:3 | live | HNcmpc | none recorded | 12347, 12395, 16184, 17173, 18274, 18316, 18373 | 0 | This is an evil in all that is done under the sun, that the same event happens to all. Also, the hearts of the children of man are full of evil, and madness is in their hearts while they **live**, and after that they go to the dead. |
| Eze 7:13 | live | HNcmpa | none recorded | 12345 | 0 | For the seller shall not return to what he has sold, while they **live**. For the vision concerns all their multitude; it shall not turn back; and because of his iniquity, none can maintain his life. |
| Jon 4:3 | live | HNcmpc | none recorded | 14250, 16162 | 0 | Therefore now, O Lord, please take my life from me, for it is better for me to die than to **live**.” |
| Jon 4:8 | live | HNcmpc | none recorded | 14250, 16162 | 0 | When the sun rose, God appointed a scorching east wind, and the sun beat down on the head of Jonah so that he was faint. And he asked that he might die and said, “It is better for me to die than to **live**.” |
| 2Ki 25:30 | lived | HNcmpc | none recorded | 18283 | 0 | and for his allowance, a regular allowance was given him by the king, according to his daily needs, as long as he **lived**. |
| Jer 52:34 | lived | HNcmpc | none recorded | - | 0 | and for his allowance, a regular allowance was given him by the king, according to his daily needs, until the day of his death, as long as he **lived**. |
| Psa 49:18 | lives | HNcmpc | none recorded | 12349, 12390, 16317 | 0 | For though, while he **lives**, he counts himself blessed — and though you get praise when you do well for yourself — |
| Ecc 6:12 | lives | HNcmpa | none recorded | 12346, 17900 | 0 | For who knows what is good for man while he **lives** the few days of his vain life, which he passes like a shadow? For who can tell man what will be after him under the sun? |
| Isa 38:20 | lives | HNcmpc | none recorded | - | 0 | The Lord will save me, and we will play my music on stringed instruments all the days of our **lives**, at the house of the Lord. |
| Psa 66:9 | living | HNcmpa | none recorded | 12350 | 0 | who has kept our soul among the **living** and has not let our feet slip. |

### 3.9 G2730 κατοικέω katoikeō "to dwell": 14 own occurrences in 13 verses

- **Meaning as stored:** Greek; native word κατοικέω, transliteration katoikeō; STEP gloss "to dwell"; sense head "to dwell" (the code is its own lemma).
- **Related terms (28):** G1460 enkatoikeō "to live among"; G1774 enoikeō "to dwell in/with"; G2596 kata "according to"; G2731 katoikēsis "dwelling"; G2732 katoikētērion "dwelling place"; G3350 metoikesia "deportation"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 652; verses STEP attests 0; verse_lexical rows the parse found 43.

- **Carried by the member words:** lived (8), live (3), living (3).
- **Engagement of these occurrences:** none recorded 14.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 13:27 | live | V-PAP-NPM | none recorded | - | 0 | For those who **live** in Jerusalem and their rulers, because they did not recognize him nor understand the utterances of the prophets, which are read every Sabbath, fulfilled them by condemning him. |
| Act 17:24 | live | V-PAI-3S | none recorded | - | 0 | The God who made the world and everything in it, being Lord of heaven and earth, does not **live** in temples made by man, |
| Act 17:26 | live | V-PAN | none recorded | - | 0 | And he made from one man every nation of mankind to **live** on all the face of the earth, having determined allotted periods and the boundaries of their dwelling place, |
| Mat 2:23 | lived | V-AAI-3S | none recorded | - | 0 | And he went and **lived** in a city called Nazareth, so that what was spoken by the prophets might be fulfilled, that he would be called a Nazarene. |
| Mat 4:13 | lived | V-AAI-3S | none recorded | - | 0 | And leaving Nazareth he went and **lived** in Capernaum by the sea, in the territory of Zebulun and Naphtali, |
| Luk 13:4 | lived | V-PAP-APM | none recorded | - | 0 | Or those eighteen on whom the tower in Siloam fell and killed them: do you think that they were worse offenders than all the others who **lived** in Jerusalem? |
| Act 7:2 | lived | V-AAN | none recorded | - | 0 | And Stephen said: “ Brothers and fathers, hear me. The God of glory appeared to our father Abraham when he was in Mesopotamia, before he **lived** in Haran, |
| Act 7:4 | lived | V-AAI-3S | none recorded | - | 0 | Then he went out from the land of the Chaldeans and **lived** in Haran. And after his father died, God removed him from there into this land in which you are now living. |
| Act 9:22 | lived | V-PAP-APM | none recorded | - | 0 | But Saul increased all the more in strength, and confounded the Jews who **lived** in Damascus by proving that Jesus was the Christ. |
| Act 9:32 | lived | V-PAP-APM | none recorded | - | 0 | Now as Peter went here and there among them all, he came down also to the saints who **lived** at Lydda. |
| Act 22:12 | lived | V-PAP-GPM | none recorded | - | 0 | “ And one Ananias, a devout man according to the law, well spoken of by all the Jews who **lived** there, |
| Act 7:4 | living | V-PAI-2P | none recorded | - | 0 | Then he went out from the land of the Chaldeans and lived in Haran. And after his father died, God removed him from there into this land in which you are now **living**. |
| Act 11:29 | living | V-PAP-DPM | none recorded | - | 0 | So the disciples determined, every one according to his ability, to send relief to the brothers **living** in Judea. |
| Heb 11:9 | living | V-AAP-NSM | none recorded | - | 0 | By faith he went to live in the land of promise, as in a foreign land, **living** in tents with Isaac and Jacob, heirs with him of the same promise. |

### 3.10 H1481A גּוּר gur "to sojourn": 10 own occurrences in 10 verses

- **Meaning as stored:** Hebrew; native word גּוּר, transliteration gur; STEP gloss "to sojourn"; sense head "to sojourn" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1481):** to stir up trouble, strife, quarrel, gather together.
- **Related terms (11):** H1481B gur "to quarrel"; H1481C gur "to dread"; H1482 gur "whelp"; H1483 gur "Gur"; H1485 gur-ba.al "Gurbaal"; H1616 ger "sojourner"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 82; verses STEP attests 0; verse_lexical rows the parse found 81.

- **Carried by the member words:** live (6), lives (4).
- **Engagement of these occurrences:** none recorded 10.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 42:15 | live | HVqcc | none recorded | - | 0 | then hear the word of the Lord, O remnant of Judah. Thus says the Lord of hosts, the God of Israel: If you set your faces to enter Egypt and go to **live** there, |
| Jer 42:17 | live | HVqcc | none recorded | - | 0 | All the men who set their faces to go to Egypt to **live** there shall die by the sword, by famine, and by pestilence. They shall have no remnant or survivor from the disaster that I will bring upon them. |
| Jer 42:22 | live | HVqcc | none recorded | - | 0 | Now therefore know for a certainty that you shall die by the sword, by famine, and by pestilence in the place where you desire to go to **live**.” |
| Jer 43:2 | live | HVqcc | none recorded | - | 0 | Azariah the son of Hoshaiah and Johanan the son of Kareah and all the insolent men said to Jeremiah, “ You are telling a lie. The Lord our God did not send you to say, ‘Do not go to Egypt to **live** there,’ |
| Jer 44:8 | live | HVqcc | none recorded | - | 0 | Why do you provoke me to anger with the works of your hands, making offerings to other gods in the land of Egypt where you have come to **live**, so that you may be cut off and become a curse and a taunt among all the nations of the earth? |
| Jer 44:14 | live | HVqcc | none recorded | - | 0 | so that none of the remnant of Judah who have come to **live** in the land of Egypt shall escape or survive or return to the land of Judah, to which they desire to return to dwell there. For they shall not return, except some fugitives.” |
| Exo 3:22 | lives | HVqrfsc | none recorded | - | 0 | but each woman shall ask of her neighbor, and any woman who **lives** in her house, for silver and gold jewelry, and for clothing. You shall put them on your sons and on your daughters. So you shall plunder the Egyptians.” |
| Lev 25:6 | lives | HVqrmpa | none recorded | - | 0 | The Sabbath of the land shall provide food for you, for yourself and for your male and female slaves and for your hired worker and the sojourner who **lives** with you, |
| Deu 18:6 | lives | HVqrmsa | none recorded | - | 0 | “And if a Levite comes from any of your towns out of all Israel, where he **lives** —and he may come when he desires — to the place that the Lord will choose, |
| Job 28:4 | lives | HVqrmsa | none recorded | - | 0 | He opens shafts in a valley away from where anyone **lives**; they are forgotten by travelers; they hang in the air, far away from mankind; they swing to and fro. |

### 3.11 G0599 ἀποθνήσκω apothnēskō "to die": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word ἀποθνήσκω, transliteration apothnēskō; STEP gloss "to die"; sense head "to die" (the code is its own lemma).
- **Related terms (4):** G0575 apo "away from"; G2348 thnēskō "to die/be dead"; G2349 thnētos "mortal"; G4880 sunapothnēskō "to die with".
- **Clusters (cluster_strong):** T3 Operations (high); M25 Life & Death (high).
- **Counts, three measures as stored:** STEP token count 585; verses STEP attests 99; verse_lexical rows the parse found 110.

- **Carried by the member words:** dead (8).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 9:24 | dead | V-2AAI-3S | none recorded | 12282, 15226, 18247, 18272 | 0 | he said, “Go away, for the girl is not **dead** but sleeping.” And they laughed at him. |
| Mar 5:35 | dead | V-2AAI-3S | none recorded | - | 0 | While he was still speaking, there came from the ruler’s house some who said, “ Your daughter is **dead**. Why trouble the Teacher any further?” |
| Mar 5:39 | dead | V-2AAI-3S | none recorded | 12282 | 0 | And when he had entered, he said to them, “ Why are you making a commotion and weeping? The child is not **dead** but sleeping.” |
| Mar 9:26 | dead | V-2AAI-3S | none recorded | - | 0 | And after crying out and convulsing him terribly, it came out, and the boy was like a corpse, so that most of them said, “He is **dead**.” |
| Mar 15:44 | dead | V-2AAI-3S | none recorded | - | 0 | Pilate was surprised to hear that he should have already died. And summoning the centurion, he asked him whether he was already **dead**. |
| Luk 8:52 | dead | V-2AAI-3S | none recorded | 12282 | 0 | And all were weeping and mourning for her, but he said, “Do not weep, for she is not **dead** but sleeping.” |
| Luk 8:53 | dead | V-2AAI-3S | none recorded | 15226 | 0 | And they laughed at him, knowing that she was **dead**. |
| Jude 12 | dead | V-2AAP-NPN | none recorded | 12291, 18472 | 0 | These are hidden reefs at your love feasts, as they feast with you without fear, shepherds feeding themselves; waterless clouds, swept along by winds; fruitless trees in late autumn, twice **dead**, uprooted; |

### 3.12 G2226 ζῷον zōon "living thing": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word ζῷον, transliteration zōon; STEP gloss "living thing"; sense head "living thing" (the code is its own lemma).
- **Related terms (4):** G2198 zaō "to live"; G2225 zōogoneō "to give life"; G2227 zōopoieō "to make alive"; G4806 suzōopoieō "to make alive with".
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 41; verses STEP attests 0; verse_lexical rows the parse found 23.

- **Carried by the member words:** living (8).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rev 5:6 | living | N-GPN | none recorded | - | 0 | And between the throne and the four **living** creatures and among the elders I saw a Lamb standing, as though it had been slain, with seven horns and with seven eyes, which are the seven spirits of God sent out into all the earth. |
| Rev 5:8 | living | N-NPN | none recorded | - | 0 | And when he had taken the scroll, the four **living** creatures and the twenty-four elders fell down before the Lamb, each holding a harp, and golden bowls full of incense, which are the prayers of the saints. |
| Rev 5:11 | living | N-GPN | none recorded | - | 0 | Then I looked, and I heard around the throne and the **living** creatures and the elders the voice of many angels, numbering myriads of myriads and thousands of thousands, |
| Rev 5:14 | living | N-NPN | none recorded | - | 0 | And the four **living** creatures said, “ Amen!” and the elders fell down and worshiped. |
| Rev 6:3 | living | N-GSN | none recorded | - | 0 | When he opened the second seal, I heard the second **living** creature say, “ Come!” |
| Rev 6:5 | living | N-GSN | none recorded | - | 0 | When he opened the third seal, I heard the third **living** creature say, “ Come!” And I looked, and behold, a black horse! And its rider had a pair of scales in his hand. |
| Rev 6:6 | living | N-GPN | none recorded | - | 0 | And I heard what seemed to be a voice in the midst of the four **living** creatures, saying, “A quart of wheat for a denarius, and three quarts of barley for a denarius, and do not harm the oil and wine!” |
| Rev 6:7 | living | N-GSN | none recorded | - | 0 | When he opened the fourth seal, I heard the voice of the fourth **living** creature say, “ Come!” |

### 3.13 G2348 θνῄσκω thnēskō "to die/be dead": 6 own occurrences in 6 verses

- **Meaning as stored:** Greek; native word θνῄσκω, transliteration thnēskō; STEP gloss "to die/be dead"; sense head "to die/be dead" (the code is its own lemma).
- **Related terms (5):** G0599 apothnēskō "to die"; G2253 hēmithanēs "half-dead"; G2288 thanatos "death"; G2349 thnētos "mortal"; G4880 sunapothnēskō "to die with".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 92; verses STEP attests 10; verse_lexical rows the parse found 10.

- **Carried by the member words:** dead (6).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 2:20 | dead | V-RAI-3P | none recorded | - | 0 | saying, “ Rise, take the child and his mother and go to the land of Israel, for those who sought the child’s life are **dead**.” |
| Luk 8:49 | dead | V-RAI-3S | none recorded | - | 0 | While he was still speaking, someone from the ruler’s house came and said, “ Your daughter is **dead**; do not trouble the Teacher any more.” |
| Joh 19:33 | dead | V-RAP-ASM | none recorded | - | 0 | But when they came to Jesus and saw that he was already **dead**, they did not break his legs. |
| Act 14:19 | dead | V-RAN | none recorded | - | 0 | But Jews came from Antioch and Iconium, and having persuaded the crowds, they stoned Paul and dragged him out of the city, supposing that he was **dead**. |
| Act 25:19 | dead | V-RAP-GSM | none recorded | - | 0 | Rather they had certain points of dispute with him about their own religion and about a certain Jesus, who was **dead**, but whom Paul asserted to be alive. |
| 1Ti 5:6 | dead | V-RAI-3S | none recorded | - | 0 | but she who is self-indulgent is **dead** even while she lives. |

### 3.14 H7931 שָׁכַן sha.khan "to dwell": 6 own occurrences in 6 verses

- **Meaning as stored:** Hebrew; native word שָׁכַן, transliteration sha.khan; STEP gloss "to dwell"; sense head "to dwell" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7931):** to settle down, abide, dwell, tabernacle, reside.
- **Related terms (15):** H4908 mish.kan "tabernacle"; H7901G sha.khav "to lie down: lay down"; H7901H sha.khav "to lie down: sleep"; H7901I sha.khav "to lie down: have sex"; H7901J sha.khav "to lie down: be dead"; H7932 she.khen "to dwell"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 132; verses STEP attests 124; verse_lexical rows the parse found 129.

- **Carried by the member words:** lived (4), live (2).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 49:16 | live | HVqrmsc | none recorded | - | 0 | The horror you inspire has deceived you, and the pride of your heart, you who **live** in the clefts of the rock, who hold the height of the hill. Though you make your nest as high as the eagle’s, I will bring you down from there, declares the Lord. |
| Obd 3 | live | HVqrmsc | none recorded | - | 0 | The pride of your heart has deceived you, you who **live** in the clefts of the rock, in your lofty dwelling, who say in your heart, “ Who will bring me down to the ground?” |
| Deu 33:28 | lived | HVqw3ms | none recorded | - | 0 | So Israel **lived** in safety, Jacob lived alone, in a land of grain and wine, whose heavens drop down dew. |
| Job 15:28 | lived | HVqw3ms | none recorded | - | 0 | and has **lived** in desolate cities, in houses that none should inhabit, which were ready to become heaps of ruins; |
| Job 29:25 | lived | HVqu1cs | none recorded | - | 0 | I chose their way and sat as chief, and I **lived** like a king among his troops, like one who comforts mourners. |
| Psa 94:17 | lived | HVqp3fs | none recorded | - | 0 | If the Lord had not been my help, my soul would soon have **lived** in the land of silence. |

### 3.15 G5590H ψυχή psuchē "soul: life": 5 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word ψυχή, transliteration psuchē; STEP gloss "soul: life"; sense head "soul: life" (the code is its own lemma).
- **Related terms (14):** G0674 apopsuchō "to faint"; G0895 apsuchos "lifeless"; G1374 dipsuchos "double-minded"; G1634 ekpsuchō "to expire"; G2174 eupsucheō "be glad"; G2473 isopsuchos "like-minded"; more in the workbook.
- **Clusters (cluster_strong):** M47 Inner Seat (heuristic).
- **Counts, three measures as stored:** STEP token count 42; verses STEP attests 33; verse_lexical rows the parse found 40.

- **Carried by the member words:** lives (5).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 21:19 | lives | N-APF | none recorded | 17087 | 0 | By your endurance you will gain your **lives**. |
| Act 15:26 | lives | N-APF | none recorded | - | 0 | men who have risked their **lives** for the name of our Lord Jesus Christ. |
| Act 27:10 | lives | N-GPF | none recorded | - | 0 | saying, “ Sirs, I perceive that the voyage will be with injury and much loss, not only of the cargo and the ship, but also of our **lives**.” |
| 1Jo 3:16 | lives | N-APF | none recorded | 16878 | 0 | By this we know love, that he laid down his life for us, and we ought to lay down our **lives** for the brothers. |
| Rev 12:11 | lives | N-ASF | none recorded | 16206, 16877, 16884, 18518 | 0 | And they have conquered him by the blood of the Lamb and by the word of their testimony, for they loved not their **lives** even unto death. |

### 3.16 H2417 חַי chay "living": 5 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word חַי, transliteration chay; STEP gloss "living"; sense head "living" (the code is its own lemma).
- **Related terms (4):** H2416A chay "alive"; H2418 cha.ya "to live"; H2423 che.va "beast"; H2429 cha.yil "strength".
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 0; verse_lexical rows the parse found 7.

- **Carried by the member words:** living (4), lives (1).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 4:34 | lives | AAabsc | none recorded | - | 0 | At the end of the days I, Nebuchadnezzar, lifted my eyes to heaven, and my reason returned to me, and I blessed the Most High, and praised and honored him who **lives** forever, for his dominion is an everlasting dominion, and his kingdom endures from generation to generation; |
| Dan 2:30 | living | AAampd | none recorded | - | 0 | But as for me, this mystery has been revealed to me, not because of any wisdom that I have more than all the **living**, but in order that the interpretation may be made known to the king, and that you may know the thoughts of your mind. |
| Dan 4:17 | living | AAampd | none recorded | - | 0 | The sentence is by the decree of the watchers, the decision by the word of the holy ones, to the end that the **living** may know that the Most High rules the kingdom of men and gives it to whom he will and sets over it the lowliest of men.’ |
| Dan 6:20 | living | AAabsd | none recorded | - | 0 | As he came near to the den where Daniel was, he cried out in a tone of anguish. The king declared to Daniel, “O Daniel, servant of the **living** God, has your God, whom you serve continually, been able to deliver you from the lions?” |
| Dan 6:26 | living | AAabsd | none recorded | - | 0 | I make a decree, that in all my royal dominion people are to tremble and fear before the God of Daniel, for he is the **living** God, enduring forever; his kingdom shall never be destroyed, and his dominion shall be to the end. |

### 3.17 H2418 חֲיָא cha.ya "to live": 5 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word חֲיָא, transliteration cha.ya; STEP gloss "to live"; sense head "to live" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2418):** to live.
- **Related terms (5):** H2417 chay "living"; H2421 cha.yah "to live"; H2423 che.va "beast"; H2425 cha.yay "to live"; H2429 cha.yil "strength".
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** live (5).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 2:4 | live | AVqv2ms | none recorded | - | 0 | Then the Chaldeans said to the king in Aramaic, “O king, **live** forever! Tell your servants the dream, and we will show the interpretation.” |
| Dan 3:9 | live | AVqv2ms | none recorded | - | 0 | They declared to King Nebuchadnezzar, “O king, **live** forever! |
| Dan 5:10 | live | AVqv2ms | none recorded | - | 0 | The queen, because of the words of the king and his lords, came into the banqueting hall, and the queen declared, “O king, **live** forever! Let not your thoughts alarm you or your color change. |
| Dan 6:6 | live | AVqv2ms | none recorded | - | 0 | Then these high officials and satraps came by agreement to the king and said to him, “O King Darius, **live** forever! |
| Dan 6:21 | live | AVqv2ms | none recorded | - | 0 | Then Daniel said to the king, “O king, **live** forever! |

### 3.18 G1510 εἰμί eimi "to be": 4 own occurrences in 4 verses

- **Meaning as stored:** Greek; native word εἰμί, transliteration eimi; STEP gloss "to be"; sense head "to be" (the code is its own lemma).
- **Related terms (11):** G1498 eiēn "may be"; G1510 eimi "to be"; G1511 einai "to exist"; G1526 eisi "they are"; G2071 esomai "will be"; G2075 este "you are"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 7942; verses STEP attests 1786; verse_lexical rows the parse found 2068.

- **Carried by the member words:** live (3), lived (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 8:5 | live | V-PAP-NPM | none recorded | - | 0 | For those who **live** according to the flesh set their minds on the things of the flesh, but those who live according to the Spirit set their minds on the things of the Spirit. |
| 1Cor 7:29 | live | V-PAS-3P | none recorded | - | 0 | This is what I mean, brothers: the appointed time has grown very short. From now on, let those who have wives **live** as though they had none, |
| Eph 6:3 | live | V-FDI-2S | none recorded | - | 0 | “ that it may go well with you and that you may **live** long in the land.” |
| Mat 23:30 | lived | V-IMI-1P | none recorded | - | 0 | saying, ‘ If we had **lived** in the days of our fathers, we would not have taken part with them in shedding the blood of the prophets.’ |

### 3.19 H5315M נֶ֫פֶשׁ ne.phesh "soul: dead": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word נֶ֫פֶשׁ, transliteration ne.phesh; STEP gloss "soul: dead"; sense head "soul: dead" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5315):** soul, self, life, creature, person, appetite, mind, living being, desi ... (cut; the whole text is in the workbook).
- **Related terms (11):** H5305 na.phish "Naphish"; H5314 na.phash "be refreshed"; H5315G ne.phesh "soul"; H5315H ne.phesh "soul: life"; H5315I ne.phesh "soul: myself"; H5315J ne.phesh "soul: person"; more in the workbook.
- **Clusters (cluster_strong):** M47 Inner Seat (None).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 13; verse_lexical rows the parse found 13.

- **Carried by the member words:** dead (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lev 19:28 | dead | HNcfsa | none recorded | - | 0 | You shall not make any cuts on your body for the **dead** or tattoo yourselves: I am the Lord. |
| Lev 21:1 | dead | HNcfsa | none recorded | 16494, 16672 | 0 | And the Lord said to Moses, “ Speak to the priests, the sons of Aaron, and say to them, No one shall make himself unclean for the **dead** among his people, |
| Lev 22:4 | dead | HNcfsa | none recorded | 16494, 16672 | 0 | None of the offspring of Aaron who has a leprous disease or a discharge may eat of the holy things until he is clean. Whoever touches anything that is unclean through contact with the **dead** or a man who has had an emission of semen, |
| Num 5:2 | dead | HNcfsa | none recorded | 16494, 16672 | 0 | “ Command the people of Israel that they put out of the camp everyone who is leprous or has a discharge and everyone who is unclean through contact with the **dead**. |

### 3.20 H7496 רְפָאִים re.pha.im "shade": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word רְפָאִים, transliteration re.pha.im; STEP gloss "shade"; sense head "shade" (the code is its own lemma).
- **Related terms (9):** H7495 ra.pha "to heal"; H7497A ra.phah "Rapha"; H7497B re.pha.im "Rephaim"; H7497G re.pha.im "[Valley of] Rephaim"; H7497H re.pha.im "Raphaite"; H7503 ra.phah "to slacken"; more in the workbook.
- **Clusters (cluster_strong):** M55 Destruction & Ruin (None).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 8; verse_lexical rows the parse found 8.

- **Carried by the member words:** dead (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 26:5 | dead | HNcmpa | none recorded | 12547, 12562 | 0 | The **dead** tremble under the waters and their inhabitants. |
| Pro 9:18 | dead | HNcmpa | none recorded | 17660 | 0 | But he does not know that the **dead** are there, that her guests are in the depths of Sheol. |
| Pro 21:16 | dead | HNcmpa | none recorded | - | 0 | One who wanders from the way of good sense will rest in the assembly of the **dead**. |
| Isa 26:19 | dead | HNcmpa | none recorded | 14677, 18603, 18797 | 0 | Your **dead** shall live; their bodies shall rise. You who dwell in the dust, awake and sing for joy! For your dew is a dew of light, and the earth will give birth to the dead. |

### 3.21 G0979 βίος bios "life": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word βίος, transliteration bios; STEP gloss "life"; sense head "life" (the code is its own lemma).
- **Related terms (3):** G0980 bioō "to live"; G0981 biōsis "lifestyle"; G0982 biōtikos "of this life".
- **Clusters (cluster_strong):** M25 Life & Death (high).
- **Counts, three measures as stored:** STEP token count 35; verses STEP attests 10; verse_lexical rows the parse found 10.

- **Carried by the member words:** live on (2), living (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 12:44 | live on | N-ASM | none recorded | 15542, 15562, 18751 | 0 | For they all contributed out of their abundance, but she out of her poverty has put in everything she had, all she had to **live on**.” |
| Luk 21:4 | live on | N-ASM | none recorded | 15542 | 0 | For they all contributed out of their abundance, but she out of her poverty put in all she had to **live on**.” |
| Luk 8:43 | living | N-ASM | none recorded | - | 0 | And there was a woman who had had a discharge of blood for twelve years, and though she had spent all her **living** on physicians, she could not be healed by anyone. |

### 3.22 H3117G יוֹם yom "day": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word יוֹם, transliteration yom; STEP gloss "day"; sense head "day/when/time/period".
- **Senses (first level of the meaning tree of the lemma H3117):** day, time, year.
- **Related terms (7):** H3117H yom "day: old"; H3117I yom "day: year"; H3117J yom "day: daily"; H3117K yom "day: always"; H3117L yom "day: today"; H3118 yom "day"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1950; verses STEP attests 0; verse_lexical rows the parse found 1895.

- **Carried by the member words:** live (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 32:47 | live | HNcmpa | none recorded | - | 0 | For it is no empty word for you, but your very life, and by this word you shall **live** long in the land that you are going over the Jordan to possess.” |
| 1Sa 25:28 | live | HNcmpc | none recorded | - | 0 | Please forgive the trespass of your servant. For the Lord will certainly make my lord a sure house, because my lord is fighting the battles of the Lord, and evil shall not be found in you so long as you **live**. |
| Psa 116:2 | live | HNcmpc | none recorded | - | 0 | Because he inclined his ear to me, therefore I will call on him as long as I **live**. |

### 3.23 H4186 מוֹשָׁב mo.shav "seat": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word מוֹשָׁב, transliteration mo.shav; STEP gloss "seat"; sense head "seat" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4186):** seat, assembly, dwelling-place, dwelling, dwellers.
- **Related terms (10):** H3143 yo.shiv.yah "Joshibiah"; H3427 ya.shav "to dwell"; H3428 ye.shev.av "Jeshebeab"; H3429 yo.shev bash.she.vet "Josheb-basshebeth"; H3430 yish.bo be.nov "Ishbi-benob"; H3436 yosh.be.qa.shah "Joshbekashah"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (medium).
- **Counts, three measures as stored:** STEP token count 44; verses STEP attests 0; verse_lexical rows the parse found 42.

- **Carried by the member words:** lived (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 10:23 | lived | HNcfpc | none recorded | - | 0 | They did not see one another, nor did anyone rise from his place for three days, but all the people of Israel had light where they **lived**. |
| Num 31:10 | lived | HNcfpc | none recorded | - | 0 | All their cities in the places where they **lived**, and all their encampments, they burned with fire, |
| 2Sa 9:12 | lived | HNcmsc | none recorded | - | 0 | And Mephibosheth had a young son, whose name was Mica. And all who **lived** in Ziba’s house became Mephibosheth’s servants. |

### 3.24 H4194 מָ֫וֶת ma.vet "death": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word מָ֫וֶת, transliteration ma.vet; STEP gloss "death"; sense head "death" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4194):** death, dying, Death (personified), realm of the dead.
- **Related terms (4):** H4191 mut "to die"; H4193 mot "death"; H4463 ma.mot "death"; H8546 te.mu.tah "death".
- **Clusters (cluster_strong):** T10 Places (None); M25 Life & Death (high).
- **Counts, three measures as stored:** STEP token count 156; verses STEP attests 151; verse_lexical rows the parse found 156.

- **Carried by the member words:** dead (2), deadly (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lev 11:31 | dead | HNcmsc | none recorded | - | 0 | These are unclean to you among all that swarm. Whoever touches them when they are **dead** shall be unclean until the evening. |
| Ecc 10:1 | dead | HNcmsa | none recorded | - | 0 | **Dead** flies make the perfumer’s ointment give off a stench; so a little folly outweighs wisdom and honor. |
| Psa 7:13 | deadly | HNcmsa | none recorded | 18750 | 0 | he has prepared for him his **deadly** weapons, making his arrows fiery shafts. |

### 3.25 G0390 ἀναστρέφω anastrefō "to live/return": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word ἀναστρέφω, transliteration anastrefō; STEP gloss "to live/return"; sense head "to live/return" (the code is its own lemma).
- **Related terms (3):** G0303 ana "each"; G0391 anastrofē "behaviour"; G4762 strefō "to turn".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 116; verses STEP attests 0; verse_lexical rows the parse found 9.

- **Carried by the member words:** live (1), lived (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Pe 2:18 | live | V-PPP-APM | none recorded | - | 0 | For, speaking loud boasts of folly, they entice by sensual passions of the flesh those who are barely escaping from those who **live** in error. |
| Eph 2:3 | lived | V-2API-1P | none recorded | - | 0 | among whom we all once **lived** in the passions of our flesh, carrying out the desires of the flesh and the mind, and were by nature children of wrath, like the rest of mankind. |

### 3.26 G1096 γίνομαι ginomai "to be": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word γίνομαι, transliteration ginomai; STEP gloss "to be"; sense head "to be" (the code is its own lemma).
- **Related terms (1):** G1096 ginomai "to be".
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 2460; verses STEP attests 594; verse_lexical rows the parse found 633.

- **Carried by the member words:** lived (1), lives (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 20:18 | lived | V-2ADI-1S | none recorded | - | 0 | And when they came to him, he said to them: “You yourselves know how I **lived** among you the whole time from the first day that I set foot in Asia, |
| Rom 7:3 | lives | V-2ADS-3S | none recorded | - | 0 | Accordingly, she will be called an adulteress if she **lives** with another man while her husband is alive. But if her husband dies, she is free from that law, and if she marries another man she is not an adulteress. |

### 3.27 G3306 μένω menō "to stay": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word μένω, transliteration menō; STEP gloss "to stay"; sense head "to stay" (the code is its own lemma).
- **Related terms (2):** G3306 menō "to stay"; G3415 mnaomai "to remember".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 177; verses STEP attests 102; verse_lexical rows the parse found 118.

- **Carried by the member words:** lived (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 8:27 | lived | V-IAI-3S | none recorded | - | 0 | When Jesus had stepped out on land, there met him a man from the city who had demons. For a long time he had worn no clothes, and he had not **lived** in a house but among the tombs. |
| Act 28:30 | lived | V-AAI-3S | none recorded | - | 0 | He **lived** there two whole years at his own expense, and welcomed all who came to him, |

### 3.28 G3499 νεκρόω nekroō "to put to death": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word νεκρόω, transliteration nekroō; STEP gloss "to put to death"; sense head "to put to death" (the code is its own lemma).
- **Related terms (2):** G3498 nekros "dead"; G3500 nekrōsis "death".
- **Clusters (cluster_strong):** M25 Life & Death (heuristic).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** dead (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 4:19 | dead | V-RPP-ASN | none recorded | 12294, 18262, 18268, 18546 | 0 | He did not weaken in faith when he considered his own body, which was as good as **dead** ( since he was about a hundred years old ), or when he considered the barrenness of Sarah’s womb. |
| Heb 11:12 | dead | V-RPP-GSM | none recorded | 12294, 18268 | 0 | Therefore from one man, and him as good as **dead**, were born descendants as many as the stars of heaven and as many as the innumerable grains of sand by the seashore. |

### 3.29 G3611 οἰκέω oikeō "to dwell": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word οἰκέω, transliteration oikeō; STEP gloss "to dwell"; sense head "to dwell" (the code is its own lemma).
- **Related terms (25):** G1460 enkatoikeō "to live among"; G1774 enoikeō "to dwell in/with"; G2730 katoikeō "to dwell"; G3350 metoikesia "deportation"; G3351 metoikizō "to deport"; G3609 oikeios "of one’s household"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 110; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** live (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 7:12 | live | V-PAN | none recorded | - | 0 | To the rest I say ( I, not the Lord ) that if any brother has a wife who is an unbeliever, and she consents to **live** with him, he should not divorce her. |
| 1Cor 7:13 | live | V-PAN | none recorded | - | 0 | If any woman has a husband who is an unbeliever, and he consents to **live** with her, she should not divorce him. |

### 3.30 G4800 συζάω suzaō "to live together": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word συζάω, transliteration suzaō; STEP gloss "to live together"; sense head "to live together" (the code is its own lemma).
- **Related terms (2):** G2198 zaō "to live"; G4862 sun "with".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 0; verse_lexical rows the parse found 3.

- **Carried by the member words:** live (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 6:8 | live | V-FAI-1P | none recorded | - | 0 | Now if we have died with Christ, we believe that we will also **live** with him. |
| 2Ti 2:11 | live | V-FAI-1P | none recorded | - | 0 | The saying is trustworthy, for: If we have died with him, we will also **live** with him; |

### 3.31 G0391 ἀναστροφή anastrofē "behaviour": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀναστροφή, transliteration anastrofē; STEP gloss "behaviour"; sense head "behaviour" (the code is its own lemma).
- **Related terms (3):** G0303 ana "each"; G0390 anastrefō "to live/return"; G4762 strefō "to turn".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 0; verse_lexical rows the parse found 13.

- **Carried by the member words:** lives (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Pe 3:11 | lives | N-DPF | none recorded | - | 0 | Since all these things are thus to be dissolved, what sort of people ought you to be in **lives** of holiness and godliness, |

### 3.32 G0740 ἄρτος artos "bread": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἄρτος, transliteration artos; STEP gloss "bread"; sense head "bread" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 373; verses STEP attests 0; verse_lexical rows the parse found 97.

- **Carried by the member words:** living (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Th 3:12 | living | N-ASM | none recorded | - | 0 | Now such persons we command and encourage in the Lord Jesus Christ to do their work quietly and to earn their own **living**. |

### 3.33 G0980 βιόω bioō "to live": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word βιόω, transliteration bioō; STEP gloss "to live"; sense head "to live" (the code is its own lemma).
- **Related terms (3):** G0979 bios "life"; G0981 biōsis "lifestyle"; G0982 biōtikos "of this life".
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** live (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Pe 4:2 | live | V-AAN | none recorded | - | 0 | so as to **live** for the rest of the time in the flesh no longer for human passions but for the will of God. |

### 3.34 G1460 ἐγκατοικέω enkatoikeō "to live among": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐγκατοικέω, transliteration enkatoikeō; STEP gloss "to live among"; sense head "to live among" (the code is its own lemma).
- **Related terms (26):** G1722 en "in/on/among"; G1774 enoikeō "to dwell in/with"; G2730 katoikeō "to dwell"; G3350 metoikesia "deportation"; G3351 metoikizō "to deport"; G3609 oikeios "of one’s household"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** lived (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Pe 2:8 | lived | V-PAP-NSM | none recorded | - | 0 | (for as that righteous man **lived** among them day after day, he was tormenting his righteous soul over their lawless deeds that he saw and heard ); |

### 3.35 G1514 εἰρηνεύω eirēneuō "be at peace": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word εἰρηνεύω, transliteration eirēneuō; STEP gloss "be at peace"; sense head "be at peace" (the code is its own lemma).
- **Related terms (4):** G1515 eirēnē "peace"; G1516 eirēnikos "peaceful"; G1517 eirēnopoieō "to make peace"; G1518 eirēnopoios "peacemaker".
- **Clusters (cluster_strong):** M33 Rest & Peace (None).
- **Counts, three measures as stored:** STEP token count 14; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** live peaceably (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 12:18 | live peaceably | V-PAP-NPM | none recorded | 13154, 14795, 14843 | 0 | If possible, so far as it depends on you, **live peaceably** with all. |

### 3.36 G2253 ἡμιθανής hēmithanēs "half-dead": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἡμιθανής, transliteration hēmithanēs; STEP gloss "half-dead"; sense head "half-dead" (the code is its own lemma).
- **Related terms (6):** G2255 hēmisus "half"; G2286 thanasimos "deadly"; G2287 thanatēforos "deadly"; G2289 thanatoō "to kill"; G2348 thnēskō "to die/be dead"; G4441 punthanomai "to inquire".
- **Clusters (cluster_strong):** M25 Life & Death (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** half dead (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 10:30 | half dead | A-ASM | none recorded | - | 0 | Jesus replied, “ A man was going down from Jerusalem to Jericho, and he fell among robbers, who stripped him and beat him and departed, leaving him **half dead**. |

### 3.37 G2270 ἡσυχάζω hēsuchazō "be quiet/give up": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἡσυχάζω, transliteration hēsuchazō; STEP gloss "be quiet/give up"; sense head "be quiet/give up" (the code is its own lemma).
- **Related terms (2):** G2271 hēsuchia "quietness"; G2272 hēsuchios "quiet".
- **Clusters (cluster_strong):** M33 Rest & Peace (None).
- **Counts, three measures as stored:** STEP token count 38; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** live quietly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Th 4:11 | live quietly | V-PAN | none recorded | 17480 | 0 | and to aspire to **live quietly**, and to mind your own affairs, and to work with your hands, as we instructed you, |

### 3.38 G2286 θανάσιμος thanasimos "deadly": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word θανάσιμος, transliteration thanasimos; STEP gloss "deadly"; sense head "deadly" (the code is its own lemma).
- **Related terms (5):** G2253 hēmithanēs "half-dead"; G2287 thanatēforos "deadly"; G2288 thanatos "death"; G2289 thanatoō "to kill"; G4441 punthanomai "to inquire".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 16:18 | deadly | A-ASN | none recorded | - | 0 | they will pick up serpents with their hands; and if they drink any **deadly** poison, it will not hurt them; they will lay their hands on the sick, and they will recover.” |

### 3.39 G2287 θανατήφορος thanatēforos "deadly": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word θανατήφορος, transliteration thanatēforos; STEP gloss "deadly"; sense head "deadly" (the code is its own lemma).
- **Related terms (6):** G2253 hēmithanēs "half-dead"; G2286 thanasimos "deadly"; G2288 thanatos "death"; G2289 thanatoō "to kill"; G4441 punthanomai "to inquire"; G5342 ferō "to bear/lead".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jam 3:8 | deadly | A-GSM | none recorded | - | 0 | but no human being can tame the tongue. It is a restless evil, full of **deadly** poison. |

### 3.40 G2288 θάνατος thanatos "death": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word θάνατος, transliteration thanatos; STEP gloss "death"; sense head "death" (the code is its own lemma).
- **Related terms (4):** G0110 athanasia "immortality"; G2286 thanasimos "deadly"; G2289 thanatoō "to kill"; G2348 thnēskō "to die/be dead".
- **Clusters (cluster_strong):** T10 Places (None); M25 Life & Death (high).
- **Counts, three measures as stored:** STEP token count 375; verses STEP attests 106; verse_lexical rows the parse found 120.

- **Carried by the member words:** deadly peril (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 1:10 | deadly peril | N-GSM | none recorded | 12307 | 0 | He delivered us from such a **deadly peril**, and he will deliver us. On him we have set our hope that he will deliver us again. |

### 3.41 G3348 μετέχω metechō "to share": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word μετέχω, transliteration metechō; STEP gloss "to share"; sense head "to share" (the code is its own lemma).
- **Related terms (4):** G2192 echō "to have/be"; G3326 meta "with/after"; G3352 metochē "participation"; G3353 metochos "partaker".
- **Clusters (cluster_strong):** M44 Covenant & Fellowship (None).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** lives on (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 5:13 | lives on | V-PAP-NSM | none recorded | - | 0 | for everyone who **lives on** milk is unskilled in the word of righteousness, since he is a child. |

### 3.42 G3939 παροικέω paroikeō "be a stranger": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word παροικέω, transliteration paroikeō; STEP gloss "be a stranger"; sense head "be a stranger" (the code is its own lemma).
- **Related terms (4):** G3611 oikeō "to dwell"; G3844 para "from/with/beside"; G3940 paroikia "sojourning"; G3941 paroikos "foreigner".
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 59; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** live (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 11:9 | live | V-AAI-3S | none recorded | - | 0 | By faith he went to **live** in the land of promise, as in a foreign land, living in tents with Isaac and Jacob, heirs with him of the same promise. |

### 3.43 G4924 συνοικέω sunoikeō "to live with": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word συνοικέω, transliteration sunoikeō; STEP gloss "to live with"; sense head "to live with" (the code is its own lemma).
- **Related terms (26):** G1460 enkatoikeō "to live among"; G1774 enoikeō "to dwell in/with"; G2730 katoikeō "to dwell"; G3350 metoikesia "deportation"; G3351 metoikizō "to deport"; G3609 oikeios "of one’s household"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** live (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Pe 3:7 | live | V-PAP-NPM | none recorded | - | 0 | Likewise, husbands, **live** with your wives in an understanding way, showing honor to the woman as the weaker vessel, since they are heirs with you of the grace of life, so that your prayers may not be hindered. |

### 3.44 G5225 ὑπάρχω huparchō "be already": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ὑπάρχω, transliteration huparchō; STEP gloss "be already"; sense head "be already" (the code is its own lemma).
- **Related terms (5):** G0756 archomai "to rule/begin"; G5223 huparxis "property"; G5225 huparchō "be already"; G5259G hupo "by/under: by"; G5259H hupo "by/under: under".
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 170; verses STEP attests 46; verse_lexical rows the parse found 46.

- **Carried by the member words:** live (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 7:25 | live | V-PAP-NPM | none recorded | - | 0 | What then did you go out to see? A man dressed in soft clothing? Behold, those who are dressed in splendid clothing and **live** in luxury are in kings’ courts. |

### 3.45 H0398 אָכַל a.khal "to eat": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אָכַל, transliteration a.khal; STEP gloss "to eat"; sense head "to eat" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0398):** to eat, devour, burn up, feed.
- **Related terms (9):** H0396 a.khi.lah "food"; H0399 a.khal "to devour"; H0400 o.khel "food"; H0401 u.khal "`worn out`"; H0402 okh.lah "food"; H3978 ma.a.khal "food"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 822; verses STEP attests 701; verse_lexical rows the parse found 810.

- **Carried by the member words:** lived (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 47:22 | lived | HVqq3cp | none recorded | - | 0 | Only the land of the priests he did not buy, for the priests had a fixed allowance from Pharaoh and **lived** on the allowance that Pharaoh gave them; therefore they did not sell their land. |

### 3.46 H1100H בְּלִיַּ֫עַל be.liy.ya.al "Belial: destruction": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word בְּלִיַּ֫עַל, transliteration be.liy.ya.al; STEP gloss "Belial: destruction"; sense head "destruction".
- **Senses (first level of the meaning tree of the lemma H1100):** worthlessness.
- **Related terms (11):** H1077 bal "not"; H1086 ba.lah "to become old"; H1087 ba.leh "old"; H1094 be.lo "old"; H1097 be.li "without"; H1100G be.liy.ya.al "Belial"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (medium).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 41:8 | deadly | HNcmsa | none recorded | - | 0 | They say, “A **deadly** thing is poured out on him; he will not rise again from where he lies.” |

### 3.47 H1753 דּוּר dur "to dwell": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word דּוּר, transliteration dur; STEP gloss "to dwell"; sense head "to dwell" (the code is its own lemma).
- **Related terms (6):** H1752 dur "to dwell"; H1757 du.ra "Dura"; H1859 dar "generation"; H4070A me.dor "dwelling"; H4070B me.dar "dwelling"; H8411 te.di.ra "continuance".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 25; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** lived (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 4:12 | lived | AVqi3fp | none recorded | - | 0 | Its leaves were beautiful and its fruit abundant, and in it was food for all. The beasts of the field found shade under it, and the birds of the heavens **lived** in its branches, and all flesh was fed from it. |

### 3.48 H1942 הַוָּה hav.vah "desire": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word הַוָּה, transliteration hav.vah; STEP gloss "desire"; sense head "desire" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1942):** desire; chasm (fig. of destruction).
- **Related terms (174):** H1933A ha.va "to fall"; H1933B ha.vah "to be"; H1934 ha.va "to be"; H1943 ho.vah "misfortune"; H1944 ho.ham "Hoham"; H1953 ye.ho.sha.ma "Hoshama"; more in the workbook.
- **Clusters (cluster_strong):** M18 Desire & Longing (heuristic).
- **Counts, three measures as stored:** STEP token count 16; verses STEP attests 16; verse_lexical rows the parse found 16.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 91:3 | deadly | HNcfpa | none recorded | - | 0 | For he will deliver you from the snare of the fowler and from the **deadly** pestilence. |

### 3.49 H1980I הָלַךְ ha.lakh "to go: walk": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word הָלַךְ, transliteration ha.lakh; STEP gloss "to go: walk"; sense head "walk/move".
- **Senses (first level of the meaning tree of the lemma H1980):** to go, walk, come.
- **Related terms (16):** H1946 hukh "to go"; H1978 ha.likh "step"; H1979 ha.li.khah "walk"; H1980G ha.lakh "to go: went"; H1980H ha.lakh "to go: come"; H1980J ha.lakh "to go: take"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 335; verses STEP attests 0; verse_lexical rows the parse found 323.

- **Carried by the member words:** lived (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jos 8:35 | lived | HVqrmsa | none recorded | - | 0 | There was not a word of all that Moses commanded that Joshua did not read before all the assembly of Israel, and the women, and the little ones, and the sojourners who **lived** among them. |

### 3.50 H2416C חַיָּה chay.yah "living thing": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חַיָּה, transliteration chay.yah; STEP gloss "living thing"; sense head "living thing" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2416):** living thing, animal.
- **Related terms (24):** H2416A chay "alive"; H2416B chay "kinsfolk"; H2416D chay.yah "community"; H2416E chay.yim "life"; H2419 chi.el "Hiel"; H2421 cha.yah "to live"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 109; verses STEP attests 0; verse_lexical rows the parse found 105.

- **Carried by the member words:** lives (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 78:50 | lives | HNcfsc | none recorded | 12321, 12371, 12373 | 0 | He made a path for his anger; he did not spare them from death, but gave their **lives** over to the plague. |

### 3.51 H2424 חַיּוּת chay.yut "living": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חַיּוּת, transliteration chay.yut; STEP gloss "living"; sense head "living" (the code is its own lemma).
- **Related terms (23):** H2416A chay "alive"; H2416B chay "kinsfolk"; H2416C chay.yah "living thing"; H2416D chay.yah "community"; H2416E chay.yim "life"; H2419 chi.el "Hiel"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** living (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Sa 20:3 | living | HNcfsa | none recorded | - | 0 | And David came to his house at Jerusalem. And the king took the ten concubines whom he had left to care for the house and put them in a house under guard and provided for them, but did not go in to them. So they were shut up until the day of their death, **living** as if in widowhood. |

### 3.52 H2425 חָיַי cha.yay "to live": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָיַי, transliteration cha.yay; STEP gloss "to live"; sense head "to live" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2425):** to live, have life, remain alive, sustain life, live prosperously, liv ... (cut; the whole text is in the workbook).
- **Related terms (24):** H2416A chay "alive"; H2416B chay "kinsfolk"; H2416C chay.yah "living thing"; H2416D chay.yah "community"; H2416E chay.yim "life"; H2418 cha.ya "to live"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** lives (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 20:31 | lives | HVqp3ms | none recorded | 14271 | 0 | For as long as the son of Jesse **lives** on the earth, neither you nor your kingdom shall be established. Therefore send and bring him to me, for he shall surely die.” |

### 3.53 H2506A חֵ֫לֶק che.leq "portion": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חֵ֫לֶק, transliteration che.leq; STEP gloss "portion"; sense head "portion" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2506):** portion, share, part, territory.
- **Related terms (20):** H2505A cha.laq "to divide"; H2505B cha.laq "to smooth"; H2506B che.leq "smoothness"; H2507 che.leq "Helek"; H2508 cha.laq "portion"; H2513A chel.qah "portion"; more in the workbook.
- **Clusters (cluster_strong):** FLAG Flag (None); T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 66; verses STEP attests 62; verse_lexical rows the parse found 66.

- **Carried by the member words:** lives (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Hab 1:16 | lives | HNcmsc | none recorded | - | 0 | Therefore he sacrifices to his net and makes offerings to his dragnet; for by them he **lives** in luxury, and his food is rich. |

### 3.54 H4033 מָגוֹר ma.gor "sojourning": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מָגוֹר, transliteration ma.gor; STEP gloss "sojourning"; sense head "sojourning" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4033):** sojourning place, dwelling-place, sojourning.
- **Related terms (12):** H1481A gur "to sojourn"; H1481B gur "to quarrel"; H1481C gur "to dread"; H1483 gur "Gur"; H1485 gur-ba.al "Gurbaal"; H1616 ger "sojourner"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 0; verse_lexical rows the parse found 11.

- **Carried by the member words:** live (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 18:19 | live | HNcmpc | none recorded | - | 0 | He has no posterity or progeny among his people, and no survivor where he used to **live**. |

### 3.55 H4241 מִחְיָה mich.yah "recovery": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מִחְיָה, transliteration mich.yah; STEP gloss "recovery"; sense head "recovery" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4241):** preservation of life, sustenance.
- **Related terms (23):** H2416A chay "alive"; H2416B chay "kinsfolk"; H2416C chay.yah "living thing"; H2416D chay.yah "community"; H2416E chay.yim "life"; H2419 chi.el "Hiel"; more in the workbook.
- **Clusters (cluster_strong):** M25 Life & Death (None).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** living (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Judg 17:10 | living | HNcfsc | none recorded | - | 0 | And Micah said to him, “ Stay with me, and be to me a father and a priest, and I will give you ten pieces of silver a year and a suit of clothes and your **living**.” And the Levite went in. |

### 3.56 H4908 מִשְׁכָּן mish.kan "tabernacle": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מִשְׁכָּן, transliteration mish.kan; STEP gloss "tabernacle"; sense head "tabernacle" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4908):** dwelling place, tabernacle.
- **Related terms (11):** H4907 mish.kan "habitation"; H7931 sha.khan "to dwell"; H7934 sha.khen "neighboring"; H7935G she.khan.ya.hu "Shecaniah"; H7935H she.khan.ya.hu "Shecaniah"; H7935I she.khan.ya.hu "Shecaniah"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 139; verses STEP attests 0; verse_lexical rows the parse found 128.

- **Carried by the member words:** lived (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 21:28 | lived | HNcfpc | none recorded | - | 0 | For you say, ‘ Where is the house of the prince? Where is the tent in which the wicked **lived**?’ |

### 3.57 H7451A רַע ra "bad: harmful": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רַע, transliteration ra; STEP gloss "bad: harmful"; sense head "harmful".
- **Senses (first level of the meaning tree of the lemma H7451):** evil, misery, distress, injury.
- **Related terms (8):** H4827 me.ra "mischief"; H7451B ra "bad: evil"; H7451C ra.ah "distress: harm"; H7451H ra "bad: evil"; H7451I ra.ah "distress: evil"; H7455 ro.a "evil"; more in the workbook.
- **Clusters (cluster_strong):** M58 Wickedness (None).
- **Counts, three measures as stored:** STEP token count 68; verses STEP attests 64; verse_lexical rows the parse found 68.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 5:16 | deadly | HAampa | none recorded | - | 0 | when I send against you the **deadly** arrows of famine, arrows for destruction, which I will send to destroy you, and when I bring more and more famine upon you and break your supply of bread. |

### 3.58 H7703 שָׁדַד sha.dad "to ruin": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁדַד, transliteration sha.dad; STEP gloss "to ruin"; sense head "to ruin" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7703):** to deal violently with, despoil, devastate, ruin, destroy, spoil.
- **Related terms (3):** H7701 shod "violence"; H7706 shad.day "Almighty [God]"; H7736 shud "to waste".
- **Clusters (cluster_strong):** M55 Destruction & Ruin (heuristic).
- **Counts, three measures as stored:** STEP token count 60; verses STEP attests 47; verse_lexical rows the parse found 57.

- **Carried by the member words:** dead (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Judg 5:27 | dead | HVqsmsa | none recorded | - | 0 | Between her feet he sank, he fell, he lay still; between her feet he sank, he fell; where he sank, there he fell — **dead**. |

### 3.59 H7819A שָׁחַט sha.chat "to slaughter": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁחַט, transliteration sha.chat; STEP gloss "to slaughter"; sense head "to slaughter" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7819):** (BDB) slaughtering.
- **Related terms (3):** H7819B sha.cha.tah "slaughtering"; H7820 sha.chut "beaten"; H7821 she.chi.tah "slaughtering".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 83; verses STEP attests 69; verse_lexical rows the parse found 80.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 9:8 | deadly | HVqsmsa | none recorded | - | 0 | Their tongue is a **deadly** arrow; it speaks deceitfully; with his mouth each speaks peace to his neighbor, but in his heart he plans an ambush for him. |

### 3.60 H8463 תַּחֲלֻאִים ta.cha.lu.im "disease": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word תַּחֲלֻאִים, transliteration ta.cha.lu.im; STEP gloss "disease"; sense head "disease" (the code is its own lemma).
- **Related terms (1):** H2456 cha.la "be sick".
- **Clusters (cluster_strong):** M73 Sickness & Weakness (heuristic).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** deadly (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 16:4 | deadly | HNcmpa | none recorded | - | 0 | They shall die of **deadly** diseases. They shall not be lamented, nor shall they be buried. They shall be as dung on the surface of the ground. They shall perish by the sword and by famine, and their dead bodies shall be food for the birds of the air and for the beasts of the earth. |

### 3.61 Occurrences where the member surface is shared with another code's unit (208)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| 1Cor 15:6 | alive | G0737 ἄρτι arti "now" | alive | content_part | 2 | none recorded | - | 0 | Then he appeared to more than five hundred brothers at one time, most of whom are still **alive**, though some have fallen asleep. |
| Rev 2:23 | dead | G1722 ἐν en "in/on/among" | dead | content_part | 2 | none recorded | - | 0 | and I will strike her children **dead**. And all the churches will know that I am he who searches mind and heart, and I will give to each of you according to your works. |
| Mar 5:3 | lived | G2192 ἔχω echō "to have/be" | lived | content_part | 2 | none recorded | - | 0 | He **lived** among the tombs. And no one could bind him anymore, not even with a chain, |
| Rev 8:9 | living | G2192 ἔχω echō "to have/be" | living | content_part | 2 | none recorded | - | 0 | A third of the **living** creatures in the sea died, and a third of the ships were destroyed. |
| 1Cor 15:6 | alive | G2193 ἕως heōs "until" | alive | content_part | 2 | none recorded | - | 0 | Then he appeared to more than five hundred brothers at one time, most of whom are still **alive**, though some have fallen asleep. |
| Rev 2:23 | dead | G2288 θάνατος thanatos "death" | dead | content_part | 2 | none recorded | 16184 | 0 | and I will strike her children **dead**. And all the churches will know that I am he who searches mind and heart, and I will give to each of you according to your works. |
| Mar 5:3 | lived | G2731 κατοίκησις katoikēsis "dwelling" | lived | content_part | 2 | none recorded | - | 0 | He **lived** among the tombs. And no one could bind him anymore, not even with a chain, |
| Rom 6:11 | dead | G3303 μέν men "on the other hand" | dead | content_part | 2 | none recorded | - | 0 | So you also must consider yourselves **dead** to sin and alive to God in Christ Jesus. |
| Rev 8:9 | living | G5590G ψυχή psuchē "soul" | living | content_part | 2 | none recorded | 16039 | 0 | A third of the **living** creatures in the sea died, and a third of the ships were destroyed. |
| 2Ch 14:13 | remained alive | H0369 אַ֫יִן a.yin "nothing" | remained alive | content_part | 5 | none recorded | - | 0 | Asa and the people who were with him pursued them as far as Gerar, and the Ethiopians fell until none **remained alive**, for they were broken before the Lord and his army. The men of Judah carried away very much spoil. |
| Lev 21:1 | dead | H0413 אֶל el "to[wards]" | dead | content_part | 4 | none recorded | - | 0 | And the Lord said to Moses, “ Speak to the priests, the sons of Aaron, and say to them, No one shall make himself unclean for the **dead** among his people, |
| Deu 18:11 | dead | H0413 אֶל el "to[wards]" | dead | content_part | 3 | none recorded | - | 0 | or a charmer or a medium or a necromancer or one who inquires of the **dead**, |
| 1Sa 29:6 | lives | H0413 אֶל el "to[wards]" | lives | content_part | 3 | none recorded | - | 0 | Then Achish called David and said to him, “As the Lord **lives**, you have been honest, and to me it seems right that you should march out and in with me in the campaign. For I have found nothing wrong in you from the day of your coming to me to this day. Nevertheless, the lords do not approve of you. |
| 2Sa 12:18 | dead | H0413 אֶל el "to[wards]" | dead | content_part | 3 | none recorded | - | 0 | On the seventh day the child died. And the servants of David were afraid to tell him that the child was **dead**, for they said, “ Behold, while the child was yet alive, we spoke to him, and he did not listen to us. How then can we say to him the child is dead? He may do himself some harm.” |
| 2Ki 7:7 | lives | H0413 אֶל el "to[wards]" | lives | content_part | 2 | none recorded | - | 0 | So they fled away in the twilight and abandoned their tents, their horses, and their donkeys, leaving the camp as it was, and fled for their **lives**. |
| Isa 8:19 | dead | H0413 אֶל el "to[wards]" | dead | content_part | 3 | none recorded | - | 0 | And when they say to you, “ Inquire of the mediums and the necromancers who chirp and mutter,” should not a people inquire of their God? Should they inquire of the **dead** on behalf of the living? |
| Eze 33:11 | live | H0413 אֶל el "to[wards]" | live | content_part | 3 | none recorded | - | 0 | Say to them, As I **live**, declares the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live; turn back, turn back from your evil ways, for why will you die, O house of Israel? |
| Jer 5:2 | lives | H0518A אִם im "if" | lives | content_part | 3 | none recorded | - | 0 | Though they say, “As the Lord **lives**,” yet they swear falsely. |
| Jer 16:15 | lives | H0518B [כִּי] אם   "if: except" | lives | content_part | 3 | none recorded | - | 0 | but ‘As the Lord **lives** who brought up the people of Israel out of the north country and out of all the countries where he had driven them.’ For I will bring them back to their own land that I gave to their fathers. |
| Jer 23:8 | lives | H0518B [כִּי] אם   "if: except" | lives | content_part | 2 | none recorded | - | 0 | but ‘As the Lord **lives** who brought up and led the offspring of the house of Israel out of the north country and out of all the countries where he had driven them.’ Then they shall dwell in their own land.” |
| 2Sa 14:5 | dead | H0589 אֲנִי a.ni "I" | dead | content_part | 2 | none recorded | - | 0 | And the king said to her, “ What is your trouble?” She answered, “ Alas, I am a widow; my husband is **dead**. |
| Rut 3:13 | lives | H0595 אָֽנֹכִ֫י a.no.khi "I" | lives | content_part | 3 | none recorded | - | 0 | Remain tonight, and in the morning, if he will redeem you, good; let him do it. But if he is not willing to redeem you, then, as the Lord **lives**, I will redeem you. Lie down until the morning.” |
| Dan 7:12 | lives | H0754 אַרְכָֿא ar.kha "lengthening" | lives | content_part | 5 | none recorded | - | 0 | As for the rest of the beasts, their dominion was taken away, but their **lives** were prolonged for a season and a time. |
| Gen 5:5 | lived | H0834A אֲשֶׁר a.sher "which" | lived | content_part | 2 | none recorded | - | 0 | Thus all the days that Adam **lived** were 930 years, and he died. |
| Exo 6:4 | lived | H0834A אֲשֶׁר a.sher "which" | lived | content_part | 3 | none recorded | - | 0 | I also established my covenant with them to give them the land of Canaan, the land in which they **lived** as sojourners. |
| Num 16:33 | alive | H0834A אֲשֶׁר a.sher "which" | alive | content_part | 4 | none recorded | - | 0 | So they and all that belonged to them went down **alive** into Sheol, and the earth closed over them, and they perished from the midst of the assembly. |
| Deu 12:1 | live | H0834A אֲשֶׁר a.sher "which" | live | content_part | 2 | none recorded | - | 0 | “ These are the statutes and rules that you shall be careful to do in the land that the Lord, the God of your fathers, has given you to possess, all the days that you **live** on the earth. |
| Judg 16:30 | dead | H0834A אֲשֶׁר a.sher "which" | dead | content_part | 5 | none recorded | - | 0 | And Samson said, “Let me die with the Philistines.” Then he bowed with all his strength, and the house fell upon the lords and upon all the people who were in it. So the **dead** whom he killed at his death were more than those whom he had killed during his life. |
| 1Sa 27:11 | lived | H0834A אֲשֶׁר a.sher "which" | lived | content_part | 2 | none recorded | - | 0 | And David would leave neither man nor woman alive to bring news to Gath, thinking, “ lest they should tell about us and say, ‘ So David has done.’” Such was his custom all the while he **lived** in the country of the Philistines. |
| 1Ki 8:40 | live | H0834A אֲשֶׁר a.sher "which" | live | content_part | 2 | none recorded | - | 0 | that they may fear you all the days that they **live** in the land that you gave to our fathers. |
| 2Ki 17:29 | lived | H0834A אֲשֶׁר a.sher "which" | lived | content_part | 3 | none recorded | - | 0 | But every nation still made gods of its own and put them in the shrines of the high places that the Samaritans had made, every nation in the cities in which they **lived**. |
| 1Ch 17:1 | lived | H0834A אֲשֶׁר a.sher "which" | lived | content_part | 4 | none recorded | - | 0 | Now when David **lived** in his house, David said to Nathan the prophet, “ Behold, I dwell in a house of cedar, but the ark of the covenant of the Lord is under a tent.” |
| Ecc 4:2 | alive | H0834A אֲשֶׁר a.sher "which" | alive | content_part | 3 | none recorded | - | 0 | And I thought the dead who are already dead more fortunate than the living who are still **alive**. |
| Gen 12:12 | live | H0853 אֵת et "[Obj.]" | live | content_part | 6 | none recorded | - | 0 | and when the Egyptians see you, they will say, ‘This is his wife.’ Then they will kill me, but they will let you **live**. |
| Gen 12:12 | live | H0853 אֵת et "[Obj.]" | live | content_part | 6 | none recorded | - | 0 | and when the Egyptians see you, they will say, ‘This is his wife.’ Then they will kill me, but they will let you **live**. |
| Gen 23:6 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 2 | none recorded | - | 0 | “Hear us, my lord; you are a prince of God among us. Bury your **dead** in the choicest of our tombs. None of us will withhold from you his tomb to hinder you from burying your dead.” |
| Gen 23:8 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 2 | none recorded | - | 0 | And he said to them, “If you are willing that I should bury my **dead** out of my sight, hear me and entreat for me Ephron the son of Zohar, |
| Gen 23:13 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 2 | none recorded | - | 0 | And he said to Ephron in the hearing of the people of the land, “But if you will, hear me: I give the price of the field. Accept it from me, that I may bury my **dead** there.” |
| Gen 23:15 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 9 | none recorded | - | 0 | “My lord, listen to me: a piece of land worth four hundred shekels of silver, what is that between you and me? Bury your **dead**.” |
| Exo 1:14 | lives | H0853 אֵת et "[Obj.]" | lives | content_part | 2 | none recorded | - | 0 | and made their **lives** bitter with hard service, in mortar and brick, and in all kinds of work in the field. In all their work they ruthlessly made them work as slaves. |
| Exo 21:35 | live | H0853 אֵת et "[Obj.]" | live | content_part | 5 | none recorded | - | 0 | “ When one man’s ox butts another’s, so that it dies, then they shall sell the **live** ox and share its price, and the dead beast also they shall share. |
| Exo 21:35 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 6 | none recorded | - | 0 | “ When one man’s ox butts another’s, so that it dies, then they shall sell the live ox and share its price, and the **dead** beast also they shall share. |
| Lev 20:22 | live | H0853 אֵת et "[Obj.]" | live | content_part | 6 | none recorded | - | 0 | “You shall therefore keep all my statutes and all my rules and do them, that the land where I am bringing you to **live** may not vomit you out. |
| Num 21:8 | live | H0853 אֵת et "[Obj.]" | live | content_part | 3 | none recorded | - | 0 | And the Lord said to Moses, “ Make a fiery serpent and set it on a pole, and everyone who is bitten, when he sees it, shall **live**.” |
| Num 22:33 | live | H0853 אֵת et "[Obj.]" | live | content_part | 4 | none recorded | - | 0 | The donkey saw me and turned aside before me these three times. If she had not turned aside from me, surely just now I would have killed you and let her **live**.” |
| Deu 11:31 | live | H0853 אֵת et "[Obj.]" | live | content_part | 3 | none recorded | - | 0 | For you are to cross over the Jordan to go in to take possession of the land that the Lord your God is giving you. And when you possess it and **live** in it, |
| Jos 2:13 | lives | H0853 אֵת et "[Obj.]" | lives | content_part | 2 | none recorded | - | 0 | that you will save alive my father and mother, my brothers and sisters, and all who belong to them, and deliver our **lives** from death.” |
| 1Sa 25:29 | lives | H0853 אֵת et "[Obj.]" | lives | content_part | 4 | none recorded | - | 0 | If men rise up to pursue you and to seek your life, the life of my lord shall be bound in the bundle of the living in the care of the Lord your God. And the **lives** of your enemies he shall sling out as from the hollow of a sling. |
| 2Sa 19:5 | lives | H0853 אֵת et "[Obj.]" | lives | content_part | 3 | none recorded | - | 0 | Then Joab came into the house to the king and said, “You have today covered with shame the faces of all your servants, who have this day saved your life and the **lives** of your sons and your daughters and the lives of your wives and your concubines, |
| 2Ki 8:5 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 3 | none recorded | - | 0 | And while he was telling the king how Elisha had restored the **dead** to life, behold, the woman whose son he had restored to life appealed to the king for her house and her land. And Gehazi said, “My lord, O king, here is the woman, and here is her son whom Elisha restored to life.” |
| Ecc 4:2 | dead | H0853 אֵת et "[Obj.]" | dead | content_part | 3 | none recorded | - | 0 | And I thought the **dead** who are already dead more fortunate than the living who are still alive. |
| Rut 2:20 | living | H0854 אֵת et "with" | living | content_part | 4 | none recorded | - | 0 | And Naomi said to her daughter-in-law, “May he be blessed by the Lord, whose kindness has not forsaken the **living** or the dead!” Naomi also said to her, “ The man is a close relative of ours, one of our redeemers.” |
| Rut 2:20 | dead | H0854 אֵת et "with" | dead | content_part | 4 | none recorded | - | 0 | And Naomi said to her daughter-in-law, “May he be blessed by the Lord, whose kindness has not forsaken the living or the **dead**!” Naomi also said to her, “ The man is a close relative of ours, one of our redeemers.” |
| Deu 4:33 | live | H0859A אַתָּ֫ה at.tah "you [m.s.]" | live | content_part | 2 | none recorded | - | 0 | Did any people ever hear the voice of a god speaking out of the midst of the fire, as you have heard, and still **live**? |
| Gen 23:15 | dead | H0996G בַּ֫יִן ba.yin "between" | dead | content_part | 9 | none recorded | - | 0 | “My lord, listen to me: a piece of land worth four hundred shekels of silver, what is that between you and me? Bury your **dead**.” |
| Num 16:48 | living | H0996G בַּ֫יִן ba.yin "between" | living | content_part | 4 | none recorded | - | 0 | And he stood between the dead and the **living**, and the plague was stopped. |
| 1Ki 3:22 | living | H1121A בֵּן ben "son: child" | living | content_part | 5 | none recorded | - | 0 | But the other woman said, “ No, the **living** child is mine, and the dead child is yours.” The first said, “ No, the dead child is yours, and the living child is mine.” Thus they spoke before the king. |
| Exo 6:4 | lived | H1481A גּוּר gur "to sojourn" | lived | content_part | 3 | none recorded | - | 0 | I also established my covenant with them to give them the land of Canaan, the land in which they **lived** as sojourners. |
| Jer 43:5 | live | H1481A גּוּר gur "to sojourn" | live | content_part | 3 | none recorded | - | 0 | But Johanan the son of Kareah and all the commanders of the forces took all the remnant of Judah who had returned to **live** in the land of Judah from all the nations to which they had been driven — |
| Jer 44:12 | live | H1481A גּוּר gur "to sojourn" | live | content_part | 3 | none recorded | - | 0 | I will take the remnant of Judah who have set their faces to come to the land of Egypt to **live**, and they shall all be consumed. In the land of Egypt they shall fall; by the sword and by famine they shall be consumed. From the least to the greatest, they shall die by the sword and by famine, and they shall become an oath, a horror, a curse, and a taunt. |
| Jer 44:28 | live | H1481A גּוּר gur "to sojourn" | live | content_part | 3 | none recorded | - | 0 | And those who escape the sword shall return from the land of Egypt to the land of Judah, few in number; and all the remnant of Judah, who came to the land of Egypt to **live**, shall know whose word will stand, mine or theirs. |
| Exo 21:35 | dead | H1571 גַּם gam "also" | dead | content_part | 6 | none recorded | - | 0 | “ When one man’s ox butts another’s, so that it dies, then they shall sell the live ox and share its price, and the **dead** beast also they shall share. |
| Ezr 4:17 | live | H1768 דִּי di "that" | live | content_part | 3 | none recorded | - | 0 | The king sent an answer: “ To Rehum the commander and Shimshai the scribe and the rest of their associates who **live** in Samaria and in the rest of the province Beyond the River, greeting. And now |
| Gen 9:3 | lives | H1931 הוּא hu "he/she/it" | lives | content_part | 2 | none recorded | - | 0 | Every moving thing that **lives** shall be food for you. And as I gave you the green plants, I give you everything. |
| Gen 14:13 | living | H1931 הוּא hu "he/she/it" | living | content_part | 3 | none recorded | - | 0 | Then one who had escaped came and told Abram the Hebrew, who was **living** by the oaks of Mamre the Amorite, brother of Eshcol and of Aner. These were allies of Abram. |
| Gen 23:15 | dead | H1931 הוּא hu "he/she/it" | dead | content_part | 9 | none recorded | - | 0 | “My lord, listen to me: a piece of land worth four hundred shekels of silver, what is that between you and me? Bury your **dead**.” |
| Num 33:40 | lived | H1931 הוּא hu "he/she/it" | lived | content_part | 3 | none recorded | - | 0 | And the Canaanite, the king of Arad, who **lived** in the Negeb in the land of Canaan, heard of the coming of the people of Israel. |
| Judg 4:2 | lived | H1931 הוּא hu "he/she/it" | lived | content_part | 3 | none recorded | - | 0 | And the Lord sold them into the hand of Jabin king of Canaan, who reigned in Hazor. The commander of his army was Sisera, who **lived** in Harosheth-hagoyim. |
| 1Ch 5:8 | lived | H1931 הוּא hu "he/she/it" | lived | content_part | 2 | none recorded | - | 0 | and Bela the son of Azaz, son of Shema, son of Joel, who **lived** in Aroer, as far as Nebo and Baal-meon. |
| Isa 7:21 | alive | H1931 הוּא hu "he/she/it" | alive | content_part | 3 | none recorded | - | 0 | In that day a man will keep **alive** a young cow and two sheep, |
| Gen 10:30 | lived | H1961 הָיָה ha.yah "to be" | lived | content_part | 2 | none recorded | - | 0 | The territory in which they **lived** extended from Mesha in the direction of Sephar to the hill country of the east. |
| Gen 23:1 | lived | H1961 הָיָה ha.yah "to be" | lived | content_part | 2 | none recorded | - | 0 | Sarah **lived** 127 years; these were the years of the life of Sarah. |
| Gen 35:22 | lived | H1961 הָיָה ha.yah "to be" | lived | content_part | 3 | none recorded | - | 0 | While Israel **lived** in that land, Reuben went and lay with Bilhah his father’s concubine. And Israel heard of it. Now the sons of Jacob were twelve. |
| 2Sa 7:1 | lived | H1961 הָיָה ha.yah "to be" | lived | content_part | 3 | none recorded | - | 0 | Now when the king **lived** in his house and the Lord had given him rest from all his surrounding enemies, |
| 1Ch 17:1 | lived | H1961 הָיָה ha.yah "to be" | lived | content_part | 4 | none recorded | - | 0 | Now when David **lived** in his house, David said to Nathan the prophet, “ Behold, I dwell in a house of cedar, but the ark of the covenant of the Lord is under a tent.” |
| Neh 3:26 | living | H1961 הָיָה ha.yah "to be" | living | content_part | 2 | none recorded | - | 0 | and the temple servants **living** on Ophel repaired to a point opposite the Water Gate on the east and the projecting tower. |
| Judg 8:19 | lives | H1992 הֵ֫מָּה hem.mah "they [masc.]" | lives | content_part | 3 | none recorded | - | 0 | And he said, “They were my brothers, the sons of my mother. As the Lord **lives**, if you had saved them alive, I would not kill you.” |
| Ecc 4:2 | alive | H1992 הֵ֫מָּה hem.mah "they [masc.]" | alive | content_part | 3 | none recorded | - | 0 | And I thought the dead who are already dead more fortunate than the living who are still **alive**. |
| 2Sa 4:10 | dead | H2009 הִנֵּה hin.neh "behold" | dead | content_part | 5 | none recorded | - | 0 | when one told me, ‘Behold, Saul is **dead**,’ and thought he was bringing good news, I seized him and killed him at Ziklag, which was the reward I gave him for his news. |
| Exo 1:18 | live | H2088 זֶה zeh "this" | live | content_part | 3 | none recorded | - | 0 | So the king of Egypt called the midwives and said to them, “ Why have you done this, and let the male children **live**?” |
| 2Sa 13:20 | lived | H2088 זֶה zeh "this" | lived | content_part | 3 | none recorded | - | 0 | And her brother Absalom said to her, “Has Amnon your brother been with you? Now hold your peace, my sister. He is your brother; do not take this to heart.” So Tamar **lived**, a desolate woman, in her brother Absalom’s house. |
| Gen 9:3 | lives | H2416A חַי chay "alive" | lives | content_part | 2 | none recorded | - | 0 | Every moving thing that **lives** shall be food for you. And as I gave you the green plants, I give you everything. |
| Gen 25:6 | living | H2416A חַי chay "alive" | living | content_part | 5 | none recorded | - | 0 | But to the sons of his concubines Abraham gave gifts, and while he was still **living** he sent them away from his son Isaac, eastward to the east country. |
| Exo 21:35 | live | H2416A חַי chay "alive" | live | content_part | 5 | none recorded | - | 0 | “ When one man’s ox butts another’s, so that it dies, then they shall sell the **live** ox and share its price, and the dead beast also they shall share. |
| Num 16:48 | living | H2416A חַי chay "alive" | living | content_part | 4 | none recorded | 13019, 13543, 14538 | 0 | And he stood between the dead and the **living**, and the plague was stopped. |
| Deu 12:1 | live | H2416A חַי chay "alive" | live | content_part | 2 | none recorded | - | 0 | “ These are the statutes and rules that you shall be careful to do in the land that the Lord, the God of your fathers, has given you to possess, all the days that you **live** on the earth. |
| Judg 8:19 | lives | H2416A חַי chay "alive" | lives | content_part | 3 | none recorded | - | 0 | And he said, “They were my brothers, the sons of my mother. As the Lord **lives**, if you had saved them alive, I would not kill you.” |
| Rut 2:20 | living | H2416A חַי chay "alive" | living | content_part | 4 | none recorded | 12323 | 0 | And Naomi said to her daughter-in-law, “May he be blessed by the Lord, whose kindness has not forsaken the **living** or the dead!” Naomi also said to her, “ The man is a close relative of ours, one of our redeemers.” |
| Rut 3:13 | lives | H2416A חַי chay "alive" | lives | content_part | 3 | none recorded | 17938 | 0 | Remain tonight, and in the morning, if he will redeem you, good; let him do it. But if he is not willing to redeem you, then, as the Lord **lives**, I will redeem you. Lie down until the morning.” |
| 1Sa 29:6 | lives | H2416A חַי chay "alive" | lives | content_part | 3 | none recorded | - | 0 | Then Achish called David and said to him, “As the Lord **lives**, you have been honest, and to me it seems right that you should march out and in with me in the campaign. For I have found nothing wrong in you from the day of your coming to me to this day. Nevertheless, the lords do not approve of you. |
| 1Ki 3:22 | living | H2416A חַי chay "alive" | living | content_part | 5 | none recorded | - | 0 | But the other woman said, “ No, the **living** child is mine, and the dead child is yours.” The first said, “ No, the dead child is yours, and the living child is mine.” Thus they spoke before the king. |
| 1Ki 8:40 | live | H2416A חַי chay "alive" | live | content_part | 2 | none recorded | - | 0 | that they may fear you all the days that they **live** in the land that you gave to our fathers. |
| Ecc 4:2 | living | H2416A חַי chay "alive" | living | content_part | 3 | none recorded | 12303 | 0 | And I thought the dead who are already dead more fortunate than the **living** who are still alive. |
| Jer 5:2 | lives | H2416A חַי chay "alive" | lives | content_part | 3 | none recorded | 12328, 18277, 18310 | 0 | Though they say, “As the Lord **lives**,” yet they swear falsely. |
| Jer 16:14 | lives | H2416A חַי chay "alive" | lives | content_part | 2 | none recorded | 12328 | 0 | “ Therefore, behold, the days are coming, declares the Lord, when it shall no longer be said, ‘As the Lord **lives** who brought up the people of Israel out of the land of Egypt,’ |
| Jer 16:15 | lives | H2416A חַי chay "alive" | lives | content_part | 3 | none recorded | 12328 | 0 | but ‘As the Lord **lives** who brought up the people of Israel out of the north country and out of all the countries where he had driven them.’ For I will bring them back to their own land that I gave to their fathers. |
| Jer 23:8 | lives | H2416A חַי chay "alive" | lives | content_part | 2 | none recorded | 12328 | 0 | but ‘As the Lord **lives** who brought up and led the offspring of the house of Israel out of the north country and out of all the countries where he had driven them.’ Then they shall dwell in their own land.” |
| Eze 33:11 | live | H2416A חַי chay "alive" | live | content_part | 3 | none recorded | 12266, 12268, 12329, 17944, 18278, 18720 | 0 | Say to them, As I **live**, declares the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live; turn back, turn back from your evil ways, for why will you die, O house of Israel? |
| Gen 23:1 | lived | H2416E חַיִּים chay.yim "life" | lived | content_part | 2 | none recorded | 18283 | 0 | Sarah **lived** 127 years; these were the years of the life of Sarah. |
| Exo 1:14 | lives | H2416E חַיִּים chay.yim "life" | lives | content_part | 2 | none recorded | 12345 | 0 | and made their **lives** bitter with hard service, in mortar and brick, and in all kinds of work in the field. In all their work they ruthlessly made them work as slaves. |
| Dan 7:12 | lives | H2417 חַי chay "living" | lives | content_part | 5 | none recorded | - | 0 | As for the rest of the beasts, their dominion was taken away, but their **lives** were prolonged for a season and a time. |
| Gen 5:5 | lived | H2421 חָיָה cha.yah "to live" | lived | content_part | 2 | none recorded | - | 0 | Thus all the days that Adam **lived** were 930 years, and he died. |
| Deu 5:26 | lived | H2421 חָיָה cha.yah "to live" | lived | content_part | 3 | none recorded | 12270, 12331 | 0 | For who is there of all flesh, that has heard the voice of the living God speaking out of the midst of fire as we have, and has still **lived**? |
| Isa 7:21 | alive | H2421 חָיָה cha.yah "to live" | alive | content_part | 3 | none recorded | - | 0 | In that day a man will keep **alive** a young cow and two sheep, |
| 1Sa 1:28 | lives | H3117G יוֹם yom "day" | lives | content_part | 3 | none recorded | - | 0 | Therefore I have lent him to the Lord. As long as he **lives**, he is lent to the Lord.” And he worshiped the Lord there. |
| Deu 12:19 | live | H3117K יוֹם yom "day: always" | live | content_part | 2 | none recorded | - | 0 | Take care that you do not neglect the Levite as long as you **live** in your land. |
| Lev 20:22 | live | H3427 יָשַׁב ya.shav "to dwell" | live | content_part | 6 | none recorded | - | 0 | “You shall therefore keep all my statutes and all my rules and do them, that the land where I am bringing you to **live** may not vomit you out. |
| Num 33:40 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 3 | none recorded | - | 0 | And the Canaanite, the king of Arad, who **lived** in the Negeb in the land of Canaan, heard of the coming of the people of Israel. |
| Num 35:25 | live | H3427 יָשַׁב ya.shav "to dwell" | live | content_part | 3 | none recorded | - | 0 | And the congregation shall rescue the manslayer from the hand of the avenger of blood, and the congregation shall restore him to his city of refuge to which he had fled, and he shall **live** in it until the death of the high priest who was anointed with the holy oil. |
| Deu 11:31 | live | H3427 יָשַׁב ya.shav "to dwell" | live | content_part | 3 | none recorded | - | 0 | For you are to cross over the Jordan to go in to take possession of the land that the Lord your God is giving you. And when you possess it and **live** in it, |
| Judg 4:2 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 3 | none recorded | - | 0 | And the Lord sold them into the hand of Jabin king of Canaan, who reigned in Hazor. The commander of his army was Sisera, who **lived** in Harosheth-hagoyim. |
| 1Sa 27:11 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 2 | none recorded | - | 0 | And David would leave neither man nor woman alive to bring news to Gath, thinking, “ lest they should tell about us and say, ‘ So David has done.’” Such was his custom all the while he **lived** in the country of the Philistines. |
| 2Sa 7:1 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 3 | none recorded | - | 0 | Now when the king **lived** in his house and the Lord had given him rest from all his surrounding enemies, |
| 2Sa 7:6 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 2 | none recorded | - | 0 | I have not **lived** in a house since the day I brought up the people of Israel from Egypt to this day, but I have been moving about in a tent for my dwelling. |
| 2Sa 13:20 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 3 | none recorded | - | 0 | And her brother Absalom said to her, “Has Amnon your brother been with you? Now hold your peace, my sister. He is your brother; do not take this to heart.” So Tamar **lived**, a desolate woman, in her brother Absalom’s house. |
| 2Ki 17:29 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 3 | none recorded | - | 0 | But every nation still made gods of its own and put them in the shrines of the high places that the Samaritans had made, every nation in the cities in which they **lived**. |
| 1Ch 5:8 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 2 | none recorded | - | 0 | and Bela the son of Azaz, son of Shema, son of Joel, who **lived** in Aroer, as far as Nebo and Baal-meon. |
| 1Ch 7:29 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 4 | none recorded | - | 0 | also in possession of the Manassites, Beth-shean and its towns, Taanach and its towns, Megiddo and its towns, Dor and its towns. In these **lived** the sons of Joseph the son of Israel. |
| 1Ch 8:28 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 2 | none recorded | - | 0 | These were the heads of fathers’ houses, according to their generations, chief men. These **lived** in Jerusalem. |
| 1Ch 9:34 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 2 | none recorded | - | 0 | These were heads of fathers’ houses of the Levites, according to their generations, leaders. These **lived** in Jerusalem. |
| 1Ch 17:1 | lived | H3427 יָשַׁב ya.shav "to dwell" | lived | content_part | 4 | none recorded | - | 0 | Now when David **lived** in his house, David said to Nathan the prophet, “ Behold, I dwell in a house of cedar, but the ark of the covenant of the Lord is under a tent.” |
| Neh 3:26 | living | H3427 יָשַׁב ya.shav "to dwell" | living | content_part | 2 | none recorded | - | 0 | and the temple servants **living** on Ophel repaired to a point opposite the Water Gate on the east and the projecting tower. |
| Ezr 4:17 | live | H3488 יְתִב ye.tiv "to dwell" | live | content_part | 3 | none recorded | - | 0 | The king sent an answer: “ To Rehum the commander and Shimshai the scribe and the rest of their associates who **live** in Samaria and in the rest of the province Beyond the River, greeting. And now |
| Exo 4:19 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | And the Lord said to Moses in Midian, “ Go back to Egypt, for all the men who were seeking your life are **dead**.” |
| Judg 9:55 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | And when the men of Israel saw that Abimelech was **dead**, everyone departed to his home. |
| 1Sa 25:39 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | When David heard that Nabal was **dead**, he said, “ Blessed be the Lord who has avenged the insult I received at the hand of Nabal, and has kept back his servant from wrongdoing. The Lord has returned the evil of Nabal on his own head.” Then David sent and spoke to Abigail, to take her as his wife. |
| 2Sa 1:5 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | Then David said to the young man who told him, “ How do you know that Saul and his son Jonathan are **dead**?” |
| 2Sa 1:10 | live | H3588A כִּי ki "for" | live | content_part | 2 | none recorded | - | 0 | So I stood beside him and killed him, because I was sure that he could not **live** after he had fallen. And I took the crown that was on his head and the armlet that was on his arm, and I have brought them here to my lord.” |
| 2Sa 2:7 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | Now therefore let your hands be strong, and be valiant, for Saul your lord is **dead**, and the house of Judah has anointed me king over them.” |
| 2Sa 7:1 | lived | H3588A כִּי ki "for" | lived | content_part | 3 | none recorded | - | 0 | Now when the king **lived** in his house and the Lord had given him rest from all his surrounding enemies, |
| 2Sa 7:6 | lived | H3588A כִּי ki "for" | lived | content_part | 2 | none recorded | - | 0 | I have not **lived** in a house since the day I brought up the people of Israel from Egypt to this day, but I have been moving about in a tent for my dwelling. |
| 2Sa 11:26 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | When the wife of Uriah heard that Uriah her husband was **dead**, she lamented over her husband. |
| 2Sa 12:18 | dead | H3588A כִּי ki "for" | dead | content_part | 4 | none recorded | - | 0 | On the seventh day the child died. And the servants of David were afraid to tell him that the child was **dead**, for they said, “ Behold, while the child was yet alive, we spoke to him, and he did not listen to us. How then can we say to him the child is dead? He may do himself some harm.” |
| 2Sa 12:19 | dead | H3588A כִּי ki "for" | dead | content_part | 2 | none recorded | - | 0 | But when David saw that his servants were whispering together, David understood that the child was **dead**. And David said to his servants, “Is the child dead?” They said, “He is dead.” |
| 1Ki 11:21 | dead | H3588A כִּי ki "for" | dead | content_part | 4 | none recorded | - | 0 | But when Hadad heard in Egypt that David slept with his fathers and that Joab the commander of the army was **dead**, Hadad said to Pharaoh, “Let me depart, that I may go to my own country.” |
| 1Ch 10:5 | dead | H3588A כִּי ki "for" | dead | content_part | 3 | none recorded | - | 0 | And when his armor-bearer saw that Saul was **dead**, he also fell upon his sword and died. |
| 1Ch 10:7 | dead | H3588A כִּי ki "for" | dead | content_part | 3 | none recorded | - | 0 | And when all the men of Israel who were in the valley saw that the army had fled and that Saul and his sons were **dead**, they abandoned their cities and fled, and the Philistines came and lived in them. |
| 1Ch 11:19 | lives | H3588A כִּי ki "for" | lives | content_part | 4 | none recorded | - | 0 | and said, “ Far be it from me before my God that I should do this. Shall I drink the lifeblood of these men? For at the risk of their **lives** they brought it.” Therefore he would not drink it. These things did the three mighty men. |
| Jer 16:15 | lives | H3588B כִּי [אם] ki m "that if: except" | lives | content_part | 3 | none recorded | - | 0 | but ‘As the Lord **lives** who brought up the people of Israel out of the north country and out of all the countries where he had driven them.’ For I will bring them back to their own land that I gave to their fathers. |
| Deu 12:19 | live | H3605 כֹּל kol "all" | live | content_part | 2 | none recorded | - | 0 | Take care that you do not neglect the Levite as long as you **live** in your land. |
| 1Sa 1:28 | lives | H3605 כֹּל kol "all" | lives | content_part | 3 | none recorded | - | 0 | Therefore I have lent him to the Lord. As long as he **lives**, he is lent to the Lord.” And he worshiped the Lord there. |
| Deu 5:26 | lived | H3644G כְּמוֹ ke.mo "like" | lived | content_part | 3 | none recorded | - | 0 | For who is there of all flesh, that has heard the voice of the living God speaking out of the midst of fire as we have, and has still **lived**? |
| Gen 23:15 | dead | H4100 מָה mah "what?" | dead | content_part | 9 | none recorded | - | 0 | “My lord, listen to me: a piece of land worth four hundred shekels of silver, what is that between you and me? Bury your **dead**.” |
| Gen 10:30 | lived | H4186 מוֹשָׁב mo.shav "seat" | lived | content_part | 2 | none recorded | - | 0 | The territory in which they **lived** extended from Mesha in the direction of Sephar to the hill country of the east. |
| Gen 23:6 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | “Hear us, my lord; you are a prince of God among us. Bury your **dead** in the choicest of our tombs. None of us will withhold from you his tomb to hinder you from burying your dead.” |
| Gen 23:8 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | 16039, 16191 | 0 | And he said to them, “If you are willing that I should bury my **dead** out of my sight, hear me and entreat for me Ephron the son of Zohar, |
| Gen 23:13 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | And he said to Ephron in the hearing of the people of the land, “But if you will, hear me: I give the price of the field. Accept it from me, that I may bury my **dead** there.” |
| Gen 23:15 | dead | H4191 מוּת mut "to die" | dead | content_part | 9 | none recorded | - | 0 | “My lord, listen to me: a piece of land worth four hundred shekels of silver, what is that between you and me? Bury your **dead**.” |
| Exo 4:19 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | 16211, 17122 | 0 | And the Lord said to Moses in Midian, “ Go back to Egypt, for all the men who were seeking your life are **dead**.” |
| Exo 21:35 | dead | H4191 מוּת mut "to die" | dead | content_part | 6 | none recorded | - | 0 | “ When one man’s ox butts another’s, so that it dies, then they shall sell the live ox and share its price, and the **dead** beast also they shall share. |
| Num 19:18 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 16039 | 0 | Then a clean person shall take hyssop and dip it in the water and sprinkle it on the tent and on all the furnishings and on the persons who were there and on whoever touched the bone, or the slain or the **dead** or the grave. |
| Deu 18:11 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 12323, 18532 | 0 | or a charmer or a medium or a necromancer or one who inquires of the **dead**, |
| Deu 26:14 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 18532 | 0 | I have not eaten of the tithe while I was mourning, or removed any of it while I was unclean, or offered any of it to the **dead**. I have obeyed the voice of the Lord my God. I have done according to all that you have commanded me. |
| Judg 9:55 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | And when the men of Israel saw that Abimelech was **dead**, everyone departed to his home. |
| Judg 16:30 | dead | H4191 מוּת mut "to die" | dead | content_part | 5 | none recorded | - | 0 | And Samson said, “Let me die with the Philistines.” Then he bowed with all his strength, and the house fell upon the lords and upon all the people who were in it. So the **dead** whom he killed at his death were more than those whom he had killed during his life. |
| Rut 1:8 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 18532 | 0 | But Naomi said to her two daughters-in-law, “ Go, return each of you to her mother’s house. May the Lord deal kindly with you, as you have dealt with the **dead** and with me. |
| Rut 2:20 | dead | H4191 מוּת mut "to die" | dead | content_part | 4 | none recorded | 12323 | 0 | And Naomi said to her daughter-in-law, “May he be blessed by the Lord, whose kindness has not forsaken the living or the **dead**!” Naomi also said to her, “ The man is a close relative of ours, one of our redeemers.” |
| 1Sa 25:39 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | When David heard that Nabal was **dead**, he said, “ Blessed be the Lord who has avenged the insult I received at the hand of Nabal, and has kept back his servant from wrongdoing. The Lord has returned the evil of Nabal on his own head.” Then David sent and spoke to Abigail, to take her as his wife. |
| 2Sa 1:5 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | Then David said to the young man who told him, “ How do you know that Saul and his son Jonathan are **dead**?” |
| 2Sa 2:7 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | Now therefore let your hands be strong, and be valiant, for Saul your lord is **dead**, and the house of Judah has anointed me king over them.” |
| 2Sa 4:10 | dead | H4191 מוּת mut "to die" | dead | content_part | 5 | none recorded | - | 0 | when one told me, ‘Behold, Saul is **dead**,’ and thought he was bringing good news, I seized him and killed him at Ziklag, which was the reward I gave him for his news. |
| 2Sa 11:26 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | When the wife of Uriah heard that Uriah her husband was **dead**, she lamented over her husband. |
| 2Sa 12:18 | dead | H4191 מוּת mut "to die" | dead | content_part | 4 | none recorded | 18280 | 0 | On the seventh day the child died. And the servants of David were afraid to tell him that the child was **dead**, for they said, “ Behold, while the child was yet alive, we spoke to him, and he did not listen to us. How then can we say to him the child is dead? He may do himself some harm.” |
| 2Sa 12:18 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 18280 | 0 | On the seventh day the child died. And the servants of David were afraid to tell him that the child was **dead**, for they said, “ Behold, while the child was yet alive, we spoke to him, and he did not listen to us. How then can we say to him the child is dead? He may do himself some harm.” |
| 2Sa 12:19 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | 18280, 18520 | 0 | But when David saw that his servants were whispering together, David understood that the child was **dead**. And David said to his servants, “Is the child dead?” They said, “He is dead.” |
| 2Sa 14:2 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | And Joab sent to Tekoa and brought from there a wise woman and said to her, “Pretend to be a mourner and put on mourning garments. Do not anoint yourself with oil, but behave like a woman who has been mourning many days for the **dead**. |
| 2Sa 14:5 | dead | H4191 מוּת mut "to die" | dead | content_part | 2 | none recorded | - | 0 | And the king said to her, “ What is your trouble?” She answered, “ Alas, I am a widow; my husband is **dead**. |
| 1Ki 11:21 | dead | H4191 מוּת mut "to die" | dead | content_part | 4 | none recorded | - | 0 | But when Hadad heard in Egypt that David slept with his fathers and that Joab the commander of the army was **dead**, Hadad said to Pharaoh, “Let me depart, that I may go to my own country.” |
| 2Ki 8:5 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 18811 | 0 | And while he was telling the king how Elisha had restored the **dead** to life, behold, the woman whose son he had restored to life appealed to the king for her house and her land. And Gehazi said, “My lord, O king, here is the woman, and here is her son whom Elisha restored to life.” |
| 1Ch 10:5 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | - | 0 | And when his armor-bearer saw that Saul was **dead**, he also fell upon his sword and died. |
| 1Ch 10:7 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | - | 0 | And when all the men of Israel who were in the valley saw that the army had fled and that Saul and his sons were **dead**, they abandoned their cities and fled, and the Philistines came and lived in them. |
| Ecc 4:2 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 12303 | 0 | And I thought the **dead** who are already dead more fortunate than the living who are still alive. |
| Isa 8:19 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 12323, 18247 | 0 | And when they say to you, “ Inquire of the mediums and the necromancers who chirp and mutter,” should not a people inquire of their God? Should they inquire of the **dead** on behalf of the living? |
| Jer 16:7 | dead | H4191 מוּת mut "to die" | dead | content_part | 3 | none recorded | 18520 | 0 | No one shall break bread for the mourner, to comfort him for the **dead**, nor shall anyone give him the cup of consolation to drink for his father or his mother. |
| Lev 11:32 | dead | H4194 מָ֫וֶת ma.vet "death" | dead | content_part | 6 | none recorded | - | 0 | And anything on which any of them falls when they are **dead** shall be unclean, whether it is an article of wood or a garment or a skin or a sack, any article that is used for any purpose. It must be put into water, and it shall be unclean until the evening; then it shall be clean. |
| 2Ch 14:13 | remained alive | H4241 מִחְיָה mich.yah "recovery" | remained alive | content_part | 5 | none recorded | - | 0 | Asa and the people who were with him pursued them as far as Gerar, and the Ethiopians fell until none **remained alive**, for they were broken before the Lord and his army. The men of Judah carried away very much spoil. |
| Deu 26:14 | dead | H4480A מִן־ min- "from" | dead | content_part | 3 | none recorded | - | 0 | I have not eaten of the tithe while I was mourning, or removed any of it while I was unclean, or offered any of it to the **dead**. I have obeyed the voice of the Lord my God. I have done according to all that you have commanded me. |
| Ecc 4:2 | living | H4480A מִן־ min- "from" | living | content_part | 3 | none recorded | - | 0 | And I thought the dead who are already dead more fortunate than the **living** who are still alive. |
| Deu 8:1 | live | H4616 מַ֫עַן ma.an "because" | live | content_part | 2 | none recorded | - | 0 | “The whole commandment that I command you today you shall be careful to do, that you may **live** and multiply, and go in and possess the land that the Lord swore to give to your fathers. |
| Jer 35:7 | live | H4616 מַ֫עַן ma.an "because" | live | content_part | 3 | none recorded | - | 0 | You shall not build a house; you shall not sow seed; you shall not plant or have a vineyard; but you shall **live** in tents all your days, that you may live many days in the land where you sojourn.’ |
| Exo 30:15 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 2 | none recorded | 16408, 16719, 16782 | 0 | The rich shall not give more, and the poor shall not give less, than the half shekel, when you give the Lord’s offering to make atonement for your **lives**. |
| Exo 30:16 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 2 | none recorded | 16408, 16782 | 0 | You shall take the atonement money from the people of Israel and shall give it for the service of the tent of meeting, that it may bring the people of Israel to remembrance before the Lord, so as to make atonement for your **lives**.” |
| Jos 2:13 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 2 | none recorded | 16085, 16088 | 0 | that you will save alive my father and mother, my brothers and sisters, and all who belong to them, and deliver our **lives** from death.” |
| 1Sa 25:29 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 4 | none recorded | - | 0 | If men rise up to pursue you and to seek your life, the life of my lord shall be bound in the bundle of the living in the care of the Lord your God. And the **lives** of your enemies he shall sling out as from the hollow of a sling. |
| 2Sa 19:5 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 3 | none recorded | - | 0 | Then Joab came into the house to the king and said, “You have today covered with shame the faces of all your servants, who have this day saved your life and the **lives** of your sons and your daughters and the lives of your wives and your concubines, |
| 1Ki 20:32 | live | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | live | content_part | 2 | none recorded | 16087, 18789 | 0 | So they tied sackcloth around their waists and put ropes on their heads and went to the king of Israel and said, “Your servant Ben-hadad says, ‘ Please, let me **live**.’” And he said, “Does he still live? He is my brother.” |
| 2Ki 7:7 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 2 | none recorded | - | 0 | So they fled away in the twilight and abandoned their tents, their horses, and their donkeys, leaving the camp as it was, and fled for their **lives**. |
| 1Ch 11:19 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 4 | none recorded | 20151 | 0 | and said, “ Far be it from me before my God that I should do this. Shall I drink the lifeblood of these men? For at the risk of their **lives** they brought it.” Therefore he would not drink it. These things did the three mighty men. |
| Est 8:11 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 2 | none recorded | 13703 | 0 | saying that the king allowed the Jews who were in every city to gather and defend their **lives**, to destroy, to kill, and to annihilate any armed force of any people or province that might attack them, children and women included, and to plunder their goods, |
| Est 9:16 | lives | H5315H נֶ֫פֶשׁ ne.phesh "soul: life" | lives | content_part | 2 | none recorded | - | 0 | Now the rest of the Jews who were in the king’s provinces also gathered to defend their **lives**, and got relief from their enemies and killed 75,000 of those who hated them, but they laid no hands on the plunder. |
| Jer 16:14 | lives | H5750 עוֹד od "still" | lives | content_part | 2 | none recorded | - | 0 | “ Therefore, behold, the days are coming, declares the Lord, when it shall no longer be said, ‘As the Lord **lives** who brought up the people of Israel out of the land of Egypt,’ |
| Exo 30:15 | lives | H5921A עַל al "upon" | lives | content_part | 2 | none recorded | - | 0 | The rich shall not give more, and the poor shall not give less, than the half shekel, when you give the Lord’s offering to make atonement for your **lives**. |
| Exo 30:16 | lives | H5921A עַל al "upon" | lives | content_part | 2 | none recorded | - | 0 | You shall take the atonement money from the people of Israel and shall give it for the service of the tent of meeting, that it may bring the people of Israel to remembrance before the Lord, so as to make atonement for your **lives**.” |
| Lev 11:32 | dead | H5921A עַל al "upon" | dead | content_part | 6 | none recorded | - | 0 | And anything on which any of them falls when they are **dead** shall be unclean, whether it is an article of wood or a garment or a skin or a sack, any article that is used for any purpose. It must be put into water, and it shall be unclean until the evening; then it shall be clean. |
| 2Sa 14:2 | dead | H5921A עַל al "upon" | dead | content_part | 2 | none recorded | - | 0 | And Joab sent to Tekoa and brought from there a wise woman and said to her, “Pretend to be a mourner and put on mourning garments. Do not anoint yourself with oil, but behave like a woman who has been mourning many days for the **dead**. |
| Est 8:11 | lives | H5921A עַל al "upon" | lives | content_part | 2 | none recorded | - | 0 | saying that the king allowed the Jews who were in every city to gather and defend their **lives**, to destroy, to kill, and to annihilate any armed force of any people or province that might attack them, children and women included, and to plunder their goods, |
| Est 9:16 | lives | H5921A עַל al "upon" | lives | content_part | 2 | none recorded | - | 0 | Now the rest of the Jews who were in the king’s provinces also gathered to defend their **lives**, and got relief from their enemies and killed 75,000 of those who hated them, but they laid no hands on the plunder. |
| Jer 16:7 | dead | H5921A עַל al "upon" | dead | content_part | 3 | none recorded | - | 0 | No one shall break bread for the mourner, to comfort him for the **dead**, nor shall anyone give him the cup of consolation to drink for his father or his mother. |
| Jer 21:9 | live | H5921A עַל al "upon" | live | content_part | 3 | none recorded | - | 0 | He who stays in this city shall die by the sword, by famine, and by pestilence, but he who goes out and surrenders to the Chaldeans who are besieging you shall **live** and shall have his life as a prize of war. |
| Exo 21:35 | live | H7794 שׁוֹר shor "cattle" | live | content_part | 5 | none recorded | - | 0 | “ When one man’s ox butts another’s, so that it dies, then they shall sell the **live** ox and share its price, and the dead beast also they shall share. |
| Gen 14:13 | living | H7931 שָׁכַן sha.khan "to dwell" | living | content_part | 3 | none recorded | - | 0 | Then one who had escaped came and told Abram the Hebrew, who was **living** by the oaks of Mamre the Amorite, brother of Eshcol and of Aner. These were allies of Abram. |
| Gen 35:22 | lived | H7931 שָׁכַן sha.khan "to dwell" | lived | content_part | 3 | none recorded | - | 0 | While Israel **lived** in that land, Reuben went and lay with Bilhah his father’s concubine. And Israel heard of it. Now the sons of Jacob were twelve. |
| Gen 42:2 | live | H8033G שָׁם sham "there" | live | content_part | 5 | none recorded | - | 0 | And he said, “ Behold, I have heard that there is grain for sale in Egypt. Go down and buy grain for us there, that we may **live** and not die.” |
| Lev 20:22 | live | H8033G שָׁם sham "there" | live | content_part | 6 | none recorded | - | 0 | “You shall therefore keep all my statutes and all my rules and do them, that the land where I am bringing you to **live** may not vomit you out. |
| Num 35:25 | live | H8033G שָׁם sham "there" | live | content_part | 3 | none recorded | - | 0 | And the congregation shall rescue the manslayer from the hand of the avenger of blood, and the congregation shall restore him to his city of refuge to which he had fled, and he shall **live** in it until the death of the high priest who was anointed with the holy oil. |
| Jer 43:5 | live | H8033G שָׁם sham "there" | live | content_part | 3 | none recorded | - | 0 | But Johanan the son of Kareah and all the commanders of the forces took all the remnant of Judah who had returned to **live** in the land of Judah from all the nations to which they had been driven — |
| Jer 44:12 | live | H8033G שָׁם sham "there" | live | content_part | 3 | none recorded | - | 0 | I will take the remnant of Judah who have set their faces to come to the land of Egypt to **live**, and they shall all be consumed. In the land of Egypt they shall fall; by the sword and by famine they shall be consumed. From the least to the greatest, they shall die by the sword and by famine, and they shall become an oath, a horror, a curse, and a taunt. |
| Jer 44:28 | live | H8033G שָׁם sham "there" | live | content_part | 3 | none recorded | - | 0 | And those who escape the sword shall return from the land of Egypt to the land of Judah, few in number; and all the remnant of Judah, who came to the land of Egypt to **live**, shall know whose word will stand, mine or theirs. |

## 4. What the study has recorded for these occurrences

Of 1290 occurrences, 0 have an engagement observation and 1290 have none recorded. There are 404 live observations on them (0 engagement, 404 of other recorded stages, 0 of the retired catalogue stages) and 10 withdrawn.

### 4.1 Engagement: what each word does for the inner being (0 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

_no engagement observation covers these occurrences_

### 4.2 Other recorded observations (404)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 20782** (Analysis_phase_1, tag face, status draft): Alive here is the state of their father's life, asked of (tree H2416 1 'living, alive').
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20786** (Analysis_phase_1, tag qualification, status draft): Still asks whether the life continues (tree H5750 2a 'still, yet (of continuance or persistence)').
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20791** (Analysis_phase_1, tag statement, status draft): What he asked of their father is whether he still lives.
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20795** (Analysis_phase_1, tag party, status draft): The man questions the brothers, and the question is about their father.
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20798** (Analysis_phase_1, tag statement, status draft): All of this is the brothers' answer to their father Israel, who has just reproached them for telling the man of another brother (Gen 43:6).
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20800** (Analysis_phase_1, tag statement, status draft): The man asked whether their father was still alive.
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20803** (Analysis_phase_1, tag link, status draft): The man questioned them; what they told was in answer; they could not know that he would then say, bring your brother down.
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20804** (Analysis_phase_1, tag link, status draft): The brothers set their telling between his questioning and his demand, as the reason they could not have known.
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20805** (Analysis_phase_1, tag statement, status draft): Discovery: whether the questioning had the purpose that its later demand shows, the verse does not say; the passage is needed.
  - applies to 1 occurrence(s): Gen 43:7 (alive)
- **Observation 20919** (Analysis_phase_1, tag face, status draft): Alive here is the father's life, asked of (tree H2416 1 'living, alive').
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20920** (Analysis_phase_1, tag qualification, status draft): Still asks whether the life continues after the time that has passed (tree H5750 2a 'still, yet (of continuance or persistence)').
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20923** (Analysis_phase_1, tag statement, status draft): What he asks of the father is whether he lives still.
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20924** (Analysis_phase_1, tag party, status draft): Joseph asks; his brothers are the ones asked, and their father is the one asked about.
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20925** (Analysis_phase_1, tag statement, status draft): The brothers have just brought the present and bowed to him in his house (Gen 43:26).
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20927** (Analysis_phase_1, tag statement, status draft): Joseph asked whether the father was well and whether he still lived.
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20928** (Analysis_phase_1, tag link, status draft): He inquires after their welfare, then asks whether their father is well and whether he still lives.
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20929** (Analysis_phase_1, tag statement, status draft): He takes up the brothers' own earlier words about their father.
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 20930** (Analysis_phase_1, tag statement, status draft): Discovery: the brothers' answer to both questions is in the next verse; the passage is needed.
  - applies to 1 occurrence(s): Gen 43:27 (alive)
- **Observation 12547** (prior-capture, tag face, status draft): Face, The earth, heavens, waters and the dead tremble: The subject is the physical world, or the dead, before God
  - applies to 1 occurrence(s): Job 26:5 (dead)
- **Observation 12562** (prior-capture, tag statement, status draft): The physical world and the dead tremble before God, with the words used of people: mountains quake at his anger, the deep trembles when the waters see him, the pillars of heaven tremble at his rebuke, the dead tremble under the waters, and the land trembles at those who trample the needy.
  - applies to 1 occurrence(s): Job 26:5 (dead)
- **Observation 12652** (prior-capture, tag statement, status draft): Being feared works on the one feared: "The horror you inspire has deceived you"; those "who spread terror in the land of the living"
  - applies to 1 occurrence(s): Eze 32:23 (living)
- **Observation 12708** (prior-capture, tag face, status draft): Face M. Making others afraid, as an act (8 / 8 hits and verses; surfaces terror): Nations "who spread terror in the land of the living"; once God: "I spread terror".
  - applies to 6 occurrence(s): Eze 32:23 (living), Eze 32:24 (living), Eze 32:25 (living), Eze 32:26 (living), Eze 32:27 (living), Eze 32:32 (living)
- **Observation 13019** (prior-capture, tag statement, status draft): The leader bears it differently from the people (v2, U2 §65 point 4): Moses: "But the Lord was angry with me because of you"; Aaron "stood between the dead and the living"; David: "let your hand be against me and against my father's house"; and none found: "I sought for a man among them who should build up the wall and stand in the breach before me for the land … but I found none".
  - applies to 2 occurrence(s): Num 16:48 (dead), Num 16:48 (living)
- **Observation 13154** (prior-capture, tag link, status draft): Sequence in Rom 12:17–21: repay no evil → live peaceably → never avenge yourselves: leave it to the wrath of God → feed the enemy → overcome evil with good.
  - applies to 1 occurrence(s): Rom 12:18 (live peaceably)
- **Observation 13543** (prior-capture, tag statement, status draft): F.3: What emerged: Those who stand between, and the one not found. Moses heard (Deu 9:19); Moses not heard for himself (3:26); Aaron standing between the dead and the living (Num 16:48); an angel asking (Zec 1:12); no one found for the breach (Eze 22:30) (AG-151, 159–161).; What it changes elsewhere: Extends unit 3 face 3E/3F (those who turn it away) to its full set of parties. NS for 10.13: who stands with God's anger.; Where: 10.13; 13 (OT-13).
  - applies to 2 occurrence(s): Num 16:48 (dead), Num 16:48 (living)
- **Observation 13558** (prior-capture, tag link, status draft): sworn oath → let them live, lest wrath (Jos 9:20); warn them → not incur guilt, wrath not come (2Ch 19:10); mouth leads into sin → God angry at your voice → destroy the work of your hands (Ecc 5:6).
  - applies to 1 occurrence(s): Jos 9:20 (live)
- **Observation 13585** (prior-capture, tag link, status draft): their anger kindled → swallowed us alive → the raging waters (Psa 124:3–5).
  - applies to 1 occurrence(s): Psa 124:3 (alive)
- **Observation 13703** (prior-capture, tag silence, status draft): Links that do not count are non-inner-being senses of the M47 word: Pro 25:23, Eze 13:13, 19:12 and Psa 11:6 (wind); Num 11:33 (meat); Eze 16:26 (lustful "flesh"); Eze 7:19 (nephesh as hunger); Psa 124:5 ("us"); Est 8:11 (lives as targets); no M02 Strong's loses its implicit status through this.
  - applies to 1 occurrence(s): Est 8:11 (lives)
- **Observation 13845** (prior-capture, tag statement, status draft): Eze 35:11 (Q Anger against a brother, rival or kin, kept or turned): "as I live"; anger and envy from hatred.
  - applies to 1 occurrence(s): Eze 35:11 (live)
- **Observation 13850** (prior-capture, tag statement, status draft): Jer 10:10 (4I God's wrath on the nations and enemies; the earth before it): the living God (Ch 2); the earth quaking at his wrath is carried through Psa 18:7 and Isa 13:13.
  - applies to 1 occurrence(s): Jer 10:10 (living)
- **Observation 13856** (prior-capture, tag statement, status draft): Jos 9:20 (4C Wrath guarded against: an order, an oath, a warning, a decree): let them live, lest wrath be upon us.
  - applies to 1 occurrence(s): Jos 9:20 (live)
- **Observation 13860** (prior-capture, tag statement, status draft): Psa 124:3 (U Enemies' anger, as the one attacked bears it): swallowed alive in the enemies' anger.
  - applies to 1 occurrence(s): Psa 124:3 (alive)
- **Observation 13866** (prior-capture, tag statement, status draft): Rev 15:7 (5G The cup, the winepress, the bowls: the wrath finished): the bowls of the wrath of God who lives forever; no inner act.
  - applies to 1 occurrence(s): Rev 15:7 (lives)
- **Observation 13876** (prior-capture, tag statement, status draft): Job tells his friends "be afraid of the sword, for wrath brings the punishment of the sword, that you may know there is a judgment" (Job 19:29) straight after "I know that my Redeemer lives" and "My heart faints within me!" (19:25, 27), answering "How we will pursue him!" and "The root of the matter is found in him" (19:28); he tells his accusers to fear, and the reason he gives is that there is a judgment.
  - applies to 1 occurrence(s): Job 19:25 (lives)
- **Observation 13889** (prior-capture, tag statement, status draft): Eze 20:33, "As I live, declares the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you", answers a thought, "What is in your mind shall never happen ... 'Let us be like the nations ... and worship wood and stone'" (20:32); the wrath poured out goes with bringing out and gathering (20:34), with judgment "face to face" (20:35), and with bringing them "into the bond of the covenant" (20:37): God answers a thought in the mind with an oath by his own life and with his rule.
  - applies to 1 occurrence(s): Eze 20:33 (live)
- **Observation 13972** (prior-capture, tag statement, status draft): Seat (v3). Outside: Eze 14:20 "their own lives" (nephesh). Life-sense. Eze 22:25 "devoured human lives".
  - applies to 2 occurrence(s): Eze 14:20 (lives), Eze 22:25 (lives)
- **Observation 13976** (prior-capture, tag statement, status draft): Jer 42:20 "at the cost of your lives" (nephesh). Life-sense. Not found in the batches.
  - applies to 1 occurrence(s): Jer 42:20 (lives)
- **Observation 13985** (prior-capture, tag statement, status draft): Seat. None in-verse. Outside: Rev 16:3 "every living thing" (psyche). Life-sense.
  - applies to 1 occurrence(s): Rev 16:3 (living)
- **Observation 14091** (prior-capture, tag statement, status draft): What it leads to. The Gibeonites live as servants (Jos 9:21–23); justice is ordered (2Ch 19); the temple is provided for (Ezr 7).
  - applies to 1 occurrence(s): Jos 9:21 (live)
- **Observation 14132** (prior-capture, tag statement, status draft): Mortality: "Remember how short my time is! … What man can live and never see death?" (Psa 89:47–48).
  - applies to 1 occurrence(s): Psa 89:48 (live)
- **Observation 14176** (prior-capture, tag statement, status draft): What it leads to. In both passages, killing: "Cain rose up against his brother Abel and killed him" (Gen 4:8); Naboth is falsely charged and "stoned to death" (1Ki 21:13). "As soon as Ahab heard that Naboth was dead, Ahab arose to go down to the vineyard … to take possession of it" (21:16). Ahab rises from the bed he lay down on in 21:4.
  - applies to 1 occurrence(s): 1Ki 21:16 (dead)
- **Observation 14199** (prior-capture, tag statement, status draft): What it does to those beneath it: Pleading against it before it rises:; Judah: "let not your anger burn against your servant, for you are like Pharaoh himself" (Gen 44:18). The plea is a long retelling of the father's love (44:19–21 onward); Rachel: "Let not my lord be angry that I cannot rise before you, for the way of women is upon me" (Gen 31:35). The plea for no anger covers a concealment: she is sitting on the stolen gods (31:34); Reading it as a sign: "If he says, 'Good!' it will be well with your servant, but if he is angry, then know that harm is determined by him" (1Sa 20:7). Saul's anger is to be read as the evidence of Saul's intent. Jonathan's knowledge follows the same path: aft ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 11:21 (dead)
- **Observation 14214** (prior-capture, tag statement, status draft): How it co-exists: With grief: Jonathan's anger is joined to being "grieved for David" (1Sa 20:34). Pilot §1.4 noted "anger, grief and fasting together"; With deliberation: Neh 5:6 → 5:7, "I took counsel with myself"; With a hidden self-accusation: David's verdict on the rich man is turned on himself: "You are the man!" (2Sa 12:7). Indignation at another's outrage becomes the instrument of the angry man's own conviction; With inaction: 2Sa 13:21 says only "he was very angry". Nothing follows from David, and Absalom acts instead. "Absalom hated Amnon" (13:22). "After two full years" (13:23) he orders, "Mark when Amnon's heart is merry with wine … then kill him" (13:28). The verse sets the king ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 13:39 (dead)
- **Observation 14250** (prior-capture, tag statement, status draft): Part 2 verses: what they add. The occasion widens from God striking to God's mercy, and to the consequences of one's own folly: Jonah: anger at God's mercy; The occasion: "When God saw what they did, how they turned from their evil way, God relented of the disaster" (Jon 3:10). "But it displeased Jonah exceedingly, and he was angry" (4:1); He quotes God's own character against him: "I knew that you are a gracious God and merciful, slow to anger and abounding in steadfast love, and relenting from disaster" (4:2). Pilot §2.1 read this. The anger is at the very attribute that is the opposite of anger; It asks to die: "please take my life from me, for it is better for me to die than to live" (4: ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Jon 4:3 (live), Jon 4:8 (live)
- **Observation 14271** (prior-capture, tag statement, status draft): What it does: It reads the rival's heart as evil: Eliab, "I know your presumption and the evil of your heart, for you have come down to see the battle" (1Sa 17:28); It reckons the rival's future: Saul, "They have ascribed to David ten thousands, and to me they have ascribed thousands, and what more can he have but the kingdom?" (18:8); It attacks one's own son as the rival's ally: "You son of a perverse, rebellious woman … as long as the son of Jesse lives … neither you nor your kingdom shall be established" (20:30–31); It jeers: Sanballat "was angry and greatly enraged, and he jeered at the Jews … 'What are these feeble Jews doing?'" (Neh 4:1–2); It enlarges its target: Haman "disdained to ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 20:31 (lives)
- **Observation 14321** (prior-capture, tag statement, status draft): What it does to the one attacked: It swallows: "they would have swallowed us up alive, when their anger was kindled against us; then the flood would have swept us away" (Psa 124:3–4); It bears a grudge and drops trouble: "they drop trouble upon me, and in anger they bear a grudge against me" (Psa 55:3); It poisons through speech: "They make their tongue sharp as a serpent's, and under their lips is the venom of asps" (140:3); "They have venom like the venom of a serpent, like the deaf adder that stops its ear" (58:4). Venom is the image of the enemy's anger in speech. Compare §16's Deu 32:33; In Paul's case it is summed up without detail: "our bodies had no rest, but we were afflicted at eve ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 124:3 (alive)
- **Observation 14534** (prior-capture, tag statement, status draft): Part C: Heb 3:10; 3:11; 3:17; 4:3: Hebrews reads Psalm 95 to a new audience:; "Take care, brothers, lest there be in any of you an evil, unbelieving heart, leading you to fall away from the living God. But exhort one another every day, as long as it is called 'today,' that none of you may be hardened by the deceitfulness of sin" (Heb 3:12–13); "So we see that they were unable to enter because of unbelief" (3:19); "let us fear lest any of you should seem to have failed to reach it" (4:1); "we who have believed enter that rest" (4:3); The wilderness provocation is made a daily warning, kept by exhorting one another — part A's "remember and do not forget" (Deu 9:7) in a new form; Seat ; In the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Heb 3:12 (living)
- **Observation 14538** (prior-capture, tag statement, status draft): What it does: Atonement carried into the plague: "Take your censer … carry it quickly to the congregation and make atonement for them, for wrath has gone out from the Lord" (Num 16:46). Aaron "ran into the midst … And he stood between the dead and the living, and the plague was stopped" (16:47–48). The priest's body stands on the line; Execution of the leaders: "hang them in the sun before the Lord, that the fierce anger of the Lord may turn away from Israel" (Num 25:4). Then Phinehas's spear (25:7), read in U1 §15 (SP, 25:11); Nothing of the devoted thing kept: "None of the devoted things shall stick to your hand, that the Lord may turn from the fierceness of his anger and show you mercy an ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Num 16:48 (dead), Num 16:48 (living)
- **Observation 14559** (prior-capture, tag statement, status draft): What it does: An oath kept, though obtained by deceit: "We have sworn to them by the Lord … now we may not touch them. This we will do to them: let them live, lest wrath be upon us, because of the oath" (Jos 9:19–20). "Then all the congregation murmured against the leaders" (9:18); A brother warned: judges are to "warn them, that they may not incur guilt before the Lord and wrath may not come upon you and your brothers" (2Ch 19:10). Warning another guards both of them; A foreign king's decree: "Whatever is decreed by the God of heaven, let it be done in full … lest his wrath be against the realm of the king and his sons" (Ezr 7:23). Fear of God's wrath appears in a Persian king.
  - applies to 1 occurrence(s): Jos 9:20 (live)
- **Observation 14677** (prior-capture, tag statement, status draft): How it co-exists: Fear addressed: "Let not your heart faint, and be not fearful at the report heard in the land" (Jer 51:46); Hope: "Your dead shall live; their bodies shall rise" (Isa 26:19).
  - applies to 2 occurrence(s): Isa 26:19 (dead), Isa 26:19 (live)
- **Observation 14692** (prior-capture, tag statement, status draft): Part C: Eze 14:19; 22:24; 22:31: "I found none": "And I sought for a man among them who should build up the wall and stand in the breach before me for the land, that I should not destroy it, but I found none. Therefore I have poured out my indignation upon them" (Eze 22:30–31, context read); Ezekiel uses the image of Psa 106:23, to say that no one did; Before it, every group is named as having failed: prophets (22:25, 28), priests (22:26), princes (22:27), the people of the land (22:29); Even the righteous could not stand for others: "even if Noah, Daniel, and Job were in it … they would deliver neither son nor daughter. They would deliver but their own lives by their righteousness" (14:20); ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Eze 14:20 (lives), Eze 22:25 (lives)
- **Observation 14722** (prior-capture, tag statement, status draft): Seat. None in-verse. Outside: Jer 42:20 "at the cost of your lives" (nephesh). Life-sense. Not found in the batches; Jer 44:7 "against yourselves" (nephesh). Genuine, the self harmed.
  - applies to 1 occurrence(s): Jer 42:20 (lives)
- **Observation 14726** (prior-capture, tag statement, status draft): How it co-exists: The body of the one speaking: "From on high he sent fire; into my bones he made it descend … he has left me stunned, faint all the day long" (1:13); "He has made my flesh and my skin waste away; he has broken my bones" (3:4); "He has walled me about so that I cannot escape; he has made my chains heavy; though I call and cry for help, he shuts out my prayer" (3:7–8); Hunger at its worst: "The hands of compassionate women have boiled their own children" (4:10); "Should women eat the fruit of their womb …?" (2:20); Pouring out the heart: "Arise, cry out in the night … Pour out your heart like water before the presence of the Lord! Lift your hands to him for the lives of your c ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Lam 2:19 (lives)
- **Observation 14742** (prior-capture, tag statement, status draft): What it does: "What is in your mind shall never happen — the thought, 'Let us be like the nations, like the tribes of the countries, and worship wood and stone.' As I live … surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you" (Eze 20:32–33); "I will bring you out from the peoples and gather you … with wrath poured out. And I will bring you into the wilderness of the peoples, and there I will enter into judgment with you face to face" (20:34–35); "Where now is your king, to save you …? Where are all your rulers — those of whom you said, 'Give me a king and princes'? I gave you a king in my anger, and I took him away in my wrath" (Hos 13:10–11).
  - applies to 1 occurrence(s): Eze 20:33 (live)
- **Observation 14774** (prior-capture, tag statement, status draft): Compared with earlier sections: Part B §28 asked "correct me, but not in anger". Job and Psalm 88 bore the anger without a cause; Mic 7:9 bears it willingly, with a cause named ("because I have sinned"); Lam 3:39 said the same from another side: "Why should a living man complain … about the punishment of his sins?" (read as context in part B).
  - applies to 1 occurrence(s): Lam 3:39 (living)
- **Observation 14786** (prior-capture, tag statement, status draft): How it co-exists: A past remembered: "In these you too once walked" (compare Col 3:7); Turning and waiting: "you turned to God from idols to serve the living and true God, and to wait for his Son from heaven" (1Th 1:9–10); Soberness and hope: "let us be sober, having put on the breastplate of faith and love, and for a helmet the hope of salvation" (5:8); Joy: "we also rejoice in God" (Rom 5:11).
  - applies to 2 occurrence(s): Col 3:7 (living), 1Th 1:9 (living)
- **Observation 14795** (prior-capture, tag statement, status draft): How it co-exists: "Repay no one evil for evil" (12:17); "If possible, so far as it depends on you, live peaceably with all" (12:18); "Do not be overcome by evil, but overcome evil with good" (12:21).
  - applies to 1 occurrence(s): Rom 12:18 (live peaceably)
- **Observation 14843** (prior-capture, tag statement, status draft): (v3) Rom 12:17–21: Sequence the text gives: repay no evil → live peaceably → never avenge yourselves: leave it to the wrath of God → feed the enemy → overcome evil with good; Phenomena: LV.
  - applies to 1 occurrence(s): Rom 12:18 (live peaceably)
- **Observation 14937** (prior-capture, tag statement, status draft): (v2) Jer 42:18 (EG): Context seat: Jer 42:20 "at the cost of your lives"; Whose · check: the remnant's · life-sense; Already read in: — (not found in the batches); §: §47.
  - applies to 1 occurrence(s): Jer 42:20 (lives)
- **Observation 14947** (prior-capture, tag statement, status draft): (v3) Eze 14:19 (NI): Context seat: Eze 14:20 "deliver but their own lives"; Whose · check: the righteous · life-sense; Already read in: D v2 §1.7; E v2 §11.3; §: §41.
  - applies to 1 occurrence(s): Eze 14:20 (lives)
- **Observation 14951** (prior-capture, tag statement, status draft): (v3) Eze 22:24 (NI): Context seat: Eze 22:25 "devoured human lives"; Whose · check: the victims' · life-sense; Already read in: H v1 §2.2; §: §41.
  - applies to 1 occurrence(s): Eze 22:25 (lives)
- **Observation 14964** (prior-capture, tag statement, status draft): (v3) Rev 16:1 (FW): Context seat: Rev 16:3 "every living thing" psyche; Whose · check: creatures · life-sense; Already read in: G v3 §0; §: §64.
  - applies to 1 occurrence(s): Rev 16:3 (living)
- **Observation 15117** (prior-capture, tag statement, status draft): It has no room for God: "In the pride of his face the wicked does not seek him; all his thoughts are, 'There is no God'" (Psa 10:4); "his soul is puffed up; it is not upright within him, but the righteous shall live by his faith" (Hab 2:4). Then: "an arrogant man who is never at rest. His greed is as wide as Sheol" (2:5). The swollen soul is set against faith, and joined to restlessness and greed.
  - applies to 1 occurrence(s): Hab 2:4 (live)
- **Observation 15121** (prior-capture, tag statement, status draft): zîd and zādôn name a pride that acts where it was not sent: Speaking what God did not say. "the prophet who presumes to speak a word in my name that I have not commanded him" (Deu 18:20). Such a word fails, and "You need not be afraid of him" (18:22). Presumption here borrows God's name for its own word; Going up when told not to. "Do not go up ... So I spoke to you, and you would not listen; but you rebelled against the command of the Lord and presumptuously went up" (Deu 1:42–43). It came straight after "We have sinned ... We ourselves will go up" (1:41). After the defeat, "you returned and wept before the Lord" (1:45). I read: presumption can wear the clothes of repentance. It goes up whe ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 17:26 (living)
- **Observation 15167** (prior-capture, tag statement, status draft): Boasting about tomorrow. "you do not know what tomorrow will bring ... Instead you ought to say, 'If the Lord wills, we will live and do this or that.' As it is, you boast in your arrogance. All such boasting is evil" (Jam 4:14–16). The arrogance is planning as if life were one's own.
  - applies to 1 occurrence(s): Jam 4:15 (live)
- **Observation 15226** (prior-capture, tag statement, status draft): Laughed at. "'the girl is not dead but sleeping.' And they laughed at him" (Mat 9:24; Mar 5:40). "they laughed at him, knowing that she was dead" (Luk 8:53). Then the girl arose.
  - applies to 2 occurrence(s): Mat 9:24 (dead), Luk 8:53 (dead)
- **Observation 15345** (prior-capture, tag statement, status draft): Deu 8:2–3, 16 states the purpose: "that he might humble you, testing you to know what was in your heart, whether you would keep his commandments or not" (8:2); "And he humbled you and let you hunger and fed you with manna … that he might make you know that man does not live by bread alone" (8:3); "that he might humble you and test you, to do you good in the end" (8:16).
  - applies to 1 occurrence(s): Deu 8:3 (live)
- **Observation 15405** (prior-capture, tag statement, status draft): The seven verses decided "thread" are those where the verse is about the afflicted being oppressed or crying out. They are already coded in the poor/needy split (P or G) and carried by OT-105. Two of them name the heart: "you will strengthen their heart" (Psa 10:17), and "May your hearts live forever!" (Psa 22:26).
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 15542** (prior-capture, tag statement, status draft): Mar 12:42; Luk 21:3: "a poor widow came and put in two small copper coins". Jesus says she "has put in more than all those who are contributing … For they all contributed out of their abundance, but she out of her poverty has put in everything she had, all she had to live on" (Mar 12:43–44; Luk 21:3–4): The measure is what is left, not what is given: "out of their abundance" against "out of her poverty … all she had to live on"; In Mark the scene follows directly on the scribes "who devour widows' houses and for a pretense make long prayers" (12:40). The poor widow gives everything at the treasury, while those who devour widows pray at length for show; I read: the verses name no inner word f ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Mar 12:44 (live on), Luk 21:4 (live on)
- **Observation 15562** (prior-capture, tag statement, status draft): 1. Poor as a state of means: What these 27 verses show: Corroborated, clearly. "owned nothing" (Jer 39:10); "becomes poor and sells" (Lev 25:25, 47); "out of her poverty … all she had to live on" (Mar 12:44); the shabby clothing (Jam 2:2)..
  - applies to 1 occurrence(s): Mar 12:44 (live on)
- **Observation 15668** (prior-capture, tag statement, status draft): God humbles, for good: OT: "that he might humble you and test you, to do you good in the end" (Deu 8:16); NT: "he disciplines us for our good, that we may share his holiness" (Heb 12:10); "be subject to the Father of spirits and live" (12:9).
  - applies to 1 occurrence(s): Heb 12:9 (live)
- **Observation 15873** (prior-capture, tag statement, status draft): 3.3 Authentic vs performed grief — the heart decides: "return to me with all your heart, with fasting, with weeping, and with mourning … rend your hearts and not your garments" (Joe 2:12–13); "They do not cry to me from the heart, but they wail upon their beds" (Hos 7:14); "because your heart was tender … you have wept before me, I also have heard you" (2Ch 34:27; 2Ki 22:19); Revisit 2026-09-28: the same "tender heart" means fear before battle and lack of resolve in youth. What decides is what the heart yields to (Batch F §6).; "The heart of the wise is in the house of mourning" (Ecc 7:4); "the living will lay it to heart" (Ecc 7:2)
  - applies to 1 occurrence(s): Ecc 7:2 (living)
- **Observation 15984** (prior-capture, tag statement, status draft): Revival: "when they told him all the words of Joseph … the spirit of their father Jacob revived" (Gen 45:27) — one verse after "his heart became numb, for he did not believe them" (Gen 45:26).; Revisit 2026-09-28 (context Gen 45:25–28, Batch G §2): the revival comes when the words are joined by sight: "and when he saw the wagons that Joseph had sent". Then: "It is enough; Joseph my son is still alive. I will go and see him before I die" (28).; [Claude reading] Hearing alone numbs the heart. Hearing with seeing revives the spirit. This qualifies §9.5 below ("hearing is the main channel"). Here hearing needed a second channel.
  - applies to 2 occurrence(s): Gen 45:26 (alive), Gen 45:28 (alive)
- **Observation 15988** (prior-capture, tag statement, status draft): Hearing as eating for the soul: "Listen diligently to me, and eat what is good, and delight yourselves [nephesh] in rich food. Incline your ear … hear, that your soul may live" (Isa 55:2–3); cf. "Your words were found, and I ate them" (Jer 15:16; Batch A)
  - applies to 1 occurrence(s): Isa 55:3 (live)
- **Observation 16016** (prior-capture, tag statement, status draft): God remembers human frailty: "He remembered that they were but flesh, a wind that passes" (Psa 78:39); "I will remember my covenant … every living creature of all flesh" (Gen 9:15–16); "Remember that my life is a breath" (Job 7:7).
  - applies to 1 occurrence(s): Gen 9:16 (living)
- **Observation 16039** (prior-capture, tag statement, status draft): 0. Data notes (short): No pre-filter applies. There is no M42, M61 or M72 in this batch.; Death — v3 note (replaces the v1 note). In v1 and v2 the death words were filed outside the M-codes ("die" in T3, "death" in T10), so §1–§13 read the life side only. After #1880 both also carry M25. The death side is read in §16, and the earlier sections carry Revisit (delta) notes where it bears on them.; Tags that would mislead in the delta: "the heart of the seas" (Eze 28:8) = midst; the "flesh" of an ox (Exo 21:28) and the "meat" pots (Exo 16:3).; Not misleading, but lexically marked (kept, read in §16): *nephesh* = dead body (Lev 21:11; Num 6:6; 19:11, 13, 18); *nephesh* = "willing" (Gen 23:8); the ... (cut; the whole text is in the workbook)
  - applies to 8 occurrence(s): Gen 23:8 (dead), Lev 21:11 (dead), Num 6:6 (dead), Num 19:11 (dead), Num 19:13 (dead), Num 19:18 (dead), Rev 8:9 (living), Rev 16:3 (living)
- **Observation 16040** (prior-capture, tag statement, status draft): 1.1 "The breath of life" is shared by all flesh: "the Lord God formed the man of dust … and breathed into his nostrils the breath of life, and the man became a living creature [*nephesh ḥayyâ*]" (Gen 2:7); The same phrase *nephesh ḥayyâ* is used of fish, birds and beasts: Gen 1:20, 21, 24; 2:19; 9:10, 12, 15, 16; Lev 11:10, 46; Eze 47:9.; The flood falls on "all flesh in which is the breath of life" (Gen 6:17; 7:15, 22).; "In his hand is the life of every living thing and the breath of all mankind" (Job 12:10).; [lexical; Claude reading] "Living soul" does not mark man off from the animals lexically. What Gen 2:7 adds is God's own breathing into one creature.
  - applies to 1 occurrence(s): Gen 2:7 (living)
- **Observation 16042** (prior-capture, tag statement, status draft): Context Gen 6:5–13 → 8:20–21: [Claude reading] The diagnosis of the human heart is the same before and after the flood. What changes is God's heart: grief (6:6) becomes resolve (8:21).; Between the two come the flood and Noah's offering. The resolve is spoken in God's heart as he receives the offering.; The covenant then names "every living creature of all flesh" (Gen 9:15–16). The same flesh that corrupted its way becomes the partner of the covenant.
  - applies to 1 occurrence(s): Gen 9:16 (living)
- **Observation 16047** (prior-capture, tag statement, status draft): 1.5 ◆ "Living soul" and "life-giving spirit": "The first man Adam became a living being [*psychē*]; the last Adam became a life-giving spirit" (1Co 15:45) [U]; Read with 1.1: Gen 2:7's receiver of breath is set against one who gives it.; Other spirit: "the spirit of the living creatures was in the wheels" (Eze 1:20–21; 10:17) [O]
  - applies to 1 occurrence(s): 1Cor 15:45 (living)
- **Observation 16053** (prior-capture, tag statement, status draft): Psa 22:26 (filed under "The afflicted shall eat and be satisfied … May your hearts live forever"): eating before God
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 16079** (prior-capture, tag statement, status draft): The formula: "as the Lord lives and as your soul lives" (1Sa 20:3; 25:26; 2Sa 11:11); "as the Lord lives, and as you yourself live, I will not leave you" (2Ki 2:2, 4, 6; 4:30); "As your soul lives, O king, I do not know" (1Sa 17:55); "As you live, my lord" (1Sa 1:26; 2Sa 14:19); "As the Lord lives, who has redeemed my soul out of every adversity" (1Ki 1:29; 2Sa 4:9); "As the Lord lives, who made our souls" (Jer 38:16); "As God lives, … who has made my soul bitter" (Job 27:2); [lexical; Claude reading] The oath sets the other person's *nephesh* beside the Lord's own life as the thing that guarantees the word. To swear by someone's soul is to stake one's word on their life. In the second form, ... (cut; the whole text is in the workbook)
  - applies to 19 occurrence(s): 1Sa 1:26 (live), 1Sa 17:55 (lives), 1Sa 20:3 (lives), 1Sa 25:26 (lives), 2Sa 4:9 (lives), 2Sa 11:11 (live), 2Sa 11:11 (lives), 2Sa 14:19 (live), 1Ki 1:29 (lives), 2Ki 2:2 (lives), 2Ki 2:2 (live), 2Ki 2:4 (lives); and 7 more (sheet `Observation nodes`)
- **Observation 16080** (prior-capture, tag statement, status draft): 1Sa 17:55 → 18:1 | David goes out against the Philistine | Abner: "As your soul lives, O king, I do not know" whose son he is | David is brought in with the head; "the soul of Jonathan was knit to the soul of David" (18:1; Batch F §1.1)
  - applies to 1 occurrence(s): 1Sa 17:55 (lives)
- **Observation 16081** (prior-capture, tag statement, status draft): 2Sa 11:8–15 | David: "Go down to your house" (8); Uriah sleeps at the king's door (9) | Uriah: "Shall I then go to my house, to eat and to drink and to lie with my wife? As you live, and as your soul lives, I will not do this thing" (11) | David "made him drunk" (13) — he still does not go down. Next morning, the letter: "that he may be struck down, and die" (15)
  - applies to 2 occurrence(s): 2Sa 11:11 (live), 2Sa 11:11 (lives)
- **Observation 16082** (prior-capture, tag statement, status draft): 2Ki 2:2–6 | Elijah: "Please stay here" (three times) | Elisha: "As the Lord lives, and as you yourself live, I will not leave you" (three times) | "Let there be a double portion of your spirit on me" (2:9) → "The spirit of Elijah rests on Elisha" (2:15; Batch F §9.5)
  - applies to 6 occurrence(s): 2Ki 2:2 (lives), 2Ki 2:2 (live), 2Ki 2:4 (lives), 2Ki 2:4 (live), 2Ki 2:6 (lives), 2Ki 2:6 (live)
- **Observation 16083** (prior-capture, tag statement, status draft): 2Ki 4:27–30 | The Shunammite "caught hold of his feet … she is in bitter distress [*her soul is bitter*]" (27); "Did I not say, 'Do not deceive me?'" (28); Gehazi is sent with the staff (29) | "As the Lord lives and as you yourself live, I will not leave you" (30) | "So he arose and followed her" (30)
  - applies to 2 occurrence(s): 2Ki 4:30 (lives), 2Ki 4:30 (live)
- **Observation 16084** (prior-capture, tag statement, status draft): Jer 38:14–24 | "hide nothing from me" (14); "will you not surely put me to death?" (15) | Zedekiah "swore secretly, 'As the Lord lives, who made our souls, I will not put you to death'" (16) | "your life shall be spared" if you surrender (17, 20); "I am afraid" (19); "Let no one know of these words, and you shall not die" (24)
  - applies to 1 occurrence(s): Jer 38:16 (lives)
- **Observation 16085** (prior-capture, tag statement, status draft): What the sequences show [Claude reading]: The oath marks adherence at a cost.; Elisha's triple oath is the price of the double spirit.; The Shunammite uses Elisha's own oath against him. Her bitterness of soul becomes a hold on the prophet that he cannot refuse.; Uriah's oath by David's soul is kept against David's wish. The wine that should have lowered his guard fails (a failed threshold — Batch F §7). He dies for keeping it.; The oath by the soul can guard a life while refusing a life. Zedekiah swears secretly by "who made our souls" to spare Jeremiah's life. He then declines the life offered to him (38:17, 20), from fear (38:19). The oath and the refusal are in one conversation.; 1Sa 17: ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Jos 2:13 (lives), 1Sa 20:3 (lives), 2Sa 4:9 (lives), 2Ki 5:20 (lives)
- **Observation 16087** (prior-capture, tag statement, status draft): 5.1 Surrender for life: "he who goes out and surrenders … shall have his life as a prize of war" (Jer 21:9; 38:2); "your life shall be spared" (Jer 38:17, 20) — see §4; Ben-hadad's servants in sackcloth and ropes: "Perhaps he will spare your life … 'Please, let me live.' And he said, 'Does he still live? He is my brother'" (1Ki 20:31–32)
  - applies to 1 occurrence(s): 1Ki 20:32 (live)
- **Observation 16088** (prior-capture, tag statement, status draft): 5.2 Life saved by others — or by deceit: "Say you are my sister … that my life may be spared for your sake" (Gen 12:13) — a life saved by putting another at risk; "you have shown me great kindness in saving my life. But I cannot escape to the hills … my life will be saved" in a little city (Gen 19:19–20); "save alive my father and mother … and deliver our lives from death" (Jos 2:13)
  - applies to 1 occurrence(s): Jos 2:13 (lives)
- **Observation 16089** (prior-capture, tag statement, status draft): 5.3 Hunting souls: "Woe to the women who sew magic bands … in the hunt for souls! Will you hunt down souls belonging to my people and keep your own souls alive?" (Eze 13:18); "for handfuls of barley and for pieces of bread, putting to death souls who should not die and keeping alive souls who should not live" (Eze 13:19); "you have disheartened the righteous falsely … and encouraged the wicked … to save his life" (Eze 13:22)
  - applies to 3 occurrence(s): Eze 13:18 (alive), Eze 13:19 (alive), Eze 13:19 (live)
- **Observation 16095** (prior-capture, tag statement, status draft): 5.5 The soul's life and its failure to be satisfied: "his soul is puffed up; it is not upright within him, but the righteous shall live by his faith" (Hab 2:4)
  - applies to 1 occurrence(s): Hab 2:4 (live)
- **Observation 16097** (prior-capture, tag statement, status draft): 5.5 The soul's life and its failure to be satisfied: "lives many years … but his soul is not satisfied with life's good things" (Ecc 6:3); "the life of my lord shall be bound in the bundle of the living in the care of the Lord" (1Sa 25:29) — see §9.3 for its sequel (25:31)
  - applies to 2 occurrence(s): 1Sa 25:29 (living), Ecc 6:3 (lives)
- **Observation 16106** (prior-capture, tag statement, status draft): Opposed to Spirit | "to set the mind on the flesh is death, but to set the mind on the Spirit is life and peace" (Rom 8:6); "if you live according to the flesh you will die, but if by the Spirit you put to death the deeds of the body, you will live" (Rom 8:13); Gal 6:8; Rom 8:12
  - applies to 2 occurrence(s): Rom 8:12 (live), Rom 8:13 (live)
- **Observation 16107** (prior-capture, tag statement, status draft): Neutral mortal life | "the life I now live in the flesh I live by faith in the Son of God" (Gal 2:20); "If I am to live in the flesh, that means fruitful labor for me … to remain in the flesh is more necessary on your account" (Phili 1:22–24); "the life of Jesus … manifested in our mortal flesh" (2Co 4:11)
  - applies to 3 occurrence(s): 2Cor 4:11 (live), Gal 2:20 (live), Phili 1:22 (live)
- **Observation 16108** (prior-capture, tag statement, status draft): Christ's flesh | "in the days of his flesh, Jesus offered up prayers … with loud cries and tears" (Heb 5:7); "the new and living way … through his flesh" (Heb 10:20); "put to death in the flesh but made alive in the spirit" (1Pe 3:18) [U]
  - applies to 1 occurrence(s): Heb 10:20 (living)
- **Observation 16110** (prior-capture, tag statement, status draft): The Spirit gives life [D1/D2/D3]: "the law of the Spirit of life" (Rom 8:2); "the letter kills, but the Spirit gives life" (2Co 3:6); "written … with the Spirit of the living God, not on tablets of stone but on tablets of human hearts" (2Co 3:3); "If we live by the Spirit, let us also keep in step with the Spirit" (Gal 5:25); "he … will also give life to your mortal bodies through his Spirit" (Rom 8:11); "although the body is dead because of sin, the Spirit is life" (Rom 8:10) [U]; [Claude reading] Context sets "flesh" as: mortality to be lived in faithfully (Gal 2:20; Phili 1:22); Christ's own path (Heb 10:20); an orientation that ends in death (Rom 8:6, 13); Paul uses all three within a fe ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): 2Cor 3:3 (living), Gal 5:25 (live), Phili 1:21 (live), Phili 1:22 (live)
- **Observation 16154** (prior-capture, tag statement, status draft): 13.1 Spirit and the laying on of hands: "Take Joshua … a man in whom is the Spirit, and lay your hand on him" (Num 27:18) [U]; "Joshua … was full of the spirit of wisdom, for Moses had laid his hands on him. So the people of Israel obeyed him" (Deu 34:9) [X]; [Claude reading] The sequence across two books: Joshua already has "the Spirit" (Num 27:18).; The hands are laid on him.; He is "full of the spirit of wisdom" (Deu 34:9).; The people obey.; As in Num 11 and 2Ki 2 (Batch F §9.5), the spirit's presence is confirmed by others' response — here, obedience.; "men spoke from God as they were carried along by the Holy Spirit" (2Pe 1:21) [D1]; "uphold me with a willing spirit" (Psa 51:12) — Batc ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Lam 2:19 (lives)
- **Observation 16160** (prior-capture, tag statement, status draft): Two related figures of a death in life: "I have been forgotten [*from the heart*] like one who is dead; I have become like a broken vessel" (Psa 31:12). The context is adversaries and plots "to take my life" (31:11, 13). To be dead is to be out of other people's hearts.; "he pursued the poor and needy and the brokenhearted, to put them to death" (Psa 109:16). A broken heart is the prey of the pursuer.
  - applies to 1 occurrence(s): Psa 31:12 (dead)
- **Observation 16162** (prior-capture, tag statement, status draft): Jonah | "take my life … better for me to die than to live" (Jon 4:3, 8) | mercy to Nineveh; the loss of the plant; a scorching wind (*rûaḥ*) | A question about pity (4:10–11) (§6)
  - applies to 2 occurrence(s): Jon 4:3 (live), Jon 4:8 (live)
- **Observation 16167** (prior-capture, tag statement, status draft): Israel (Num 21) | "Why have you brought us up out of Egypt to die in the wilderness? … we loathe this worthless food" (21:5) | impatience on the way (21:4) | serpents → confession → "when he sees it, shall live" (21:6–9)
  - applies to 2 occurrence(s): Num 21:8 (live), Num 21:9 (live)
- **Observation 16178** (prior-capture, tag statement, status draft): No one: "What man can live and never see death? Who can deliver his soul from the power of Sheol?" (Psa 89:48). The context is "Remember how short my time is!" (89:47).
  - applies to 1 occurrence(s): Psa 89:48 (live)
- **Observation 16179** (prior-capture, tag statement, status draft): God: "that he may deliver their soul from death and keep them alive in famine" (Psa 33:19)
  - applies to 1 occurrence(s): Psa 33:19 (alive)
- **Observation 16184** (prior-capture, tag statement, status draft): The heart's condition as the cause of death — wisdom and sayings: "fools die for lack of sense [*heart*]" (Pro 10:21); "Whoever keeps the commandment keeps his life; he who despises his ways will die" (Pro 19:16); "he who fails to find me injures himself [*his soul*]; all who hate me love death" (Pro 8:36; Batch F §3.1); "The godless in heart cherish anger … They die in youth" (Job 36:13–14); "the hearts of the children of man are full of evil, and madness is in their hearts while they live, and after that they go to the dead" (Ecc 9:3) → "a living dog is better than a dead lion. For the living know that they will die" (9:4–5); "Discipline your son, for there is hope; do not set your heart o ... (cut; the whole text is in the workbook)
  - applies to 7 occurrence(s): Ecc 9:3 (live), Ecc 9:3 (dead), Ecc 9:4 (living), Ecc 9:4 (dead), Ecc 9:5 (living), Ecc 9:5 (dead), Rev 2:23 (dead)
- **Observation 16190** (prior-capture, tag statement, status draft): The word for "living soul" names the corpse [lexical]: "dead *nephesh*": "He shall not go in to any dead bodies nor make himself unclean, even for his father or for his mother" (Lev 21:11). The high priest's consecration forbids it (21:10–12).; "All the days that he separates himself to the Lord he shall not go near a dead body" (Num 6:6). This is the Nazirite.; "Whoever touches the dead body of any person shall be unclean seven days" (Num 19:11); "Whoever touches a dead person … and does not cleanse himself, defiles the tabernacle of the Lord, and that person [*nephesh*] shall be cut off" (Num 19:13). In one verse *nephesh* is both the corpse and the living person cut off.; Num 19:18 (the s ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Lev 21:11 (dead), Num 6:6 (dead), Num 19:11 (dead), Num 19:13 (dead)
- **Observation 16191** (prior-capture, tag statement, status draft): 16.7 *nephesh* for the dead body: "Let her not be as one dead, whose flesh is half eaten away when he comes out of his mother's womb" (Num 12:12) → "O God, please heal her — please" (12:13). This is Miriam.; "the dead bodies of the men who have rebelled … an abhorrence to all flesh" (Isa 66:24); "What is to die, let it die … let those who are left devour the flesh of one another" (Zec 11:9). This follows the shepherd's "my soul was short with them" (Batch F §4).; The willing *nephesh*: "If it is your will [*nephesh*] that I should bury my dead" (Gen 23:8).
  - applies to 2 occurrence(s): Gen 23:8 (dead), Num 12:12 (dead)
- **Observation 16194** (prior-capture, tag statement, status draft): 16.8 Breath, spirit and wind at death: "No man has power to retain the spirit, or power over the day of death" (Ecc 8:8) [U]; "with the breath of his lips he shall kill the wicked" (Isa 11:4). The one on whom the Spirit rests (11:2) kills with his breath.; "a great wind came across the wilderness … and they are dead" (Job 1:19); "a third part I will scatter to all the winds" (Eze 5:12), after the thirds that die by pestilence and sword; [Claude reading] *rûaḥ* is on both sides of death:
  - applies to 1 occurrence(s): Job 1:19 (dead)
- **Observation 16202** (prior-capture, tag statement, status draft): Flesh bears fruit for death; Spirit is the new way | "while we were living in the flesh, our sinful passions … bear fruit for death" (Rom 7:5) → "we serve in the new way of the Spirit" (7:6) [D3]; "the mind on the flesh is death" (Rom 8:6); "live according to the flesh you will die" (8:13); "the law of the Spirit of life has set you free … from the law of sin and death" (8:2) [D1]
  - applies to 1 occurrence(s): Rom 8:13 (live)
- **Observation 16204** (prior-capture, tag statement, status draft): Mortal flesh as the place of both | "we who live are always being given over to death … so that the life of Jesus also may be manifested in our mortal flesh" (2Co 4:11)
  - applies to 1 occurrence(s): 2Cor 4:11 (live)
- **Observation 16206** (prior-capture, tag statement, status draft): The life given up to death | "he poured out his soul to death" (Isa 53:12; Batch D §3.6); "they loved not their lives even unto death" (Rev 12:11; Batch F §3.2); "he nearly died for the work of Christ, risking his life" (Phili 2:30)
  - applies to 1 occurrence(s): Rev 12:11 (lives)
- **Observation 16211** (prior-capture, tag statement, status draft): 16.10 Life risked "to death" for others — the OT precedent: "Zebulun is a people who risked their lives to the death" (Judg 5:18). This is in the same song as "March on, my soul, with might!" (5:21; §3.2).; "Our life for yours even to death!" (Jos 2:14; §4 revisit); David "took his life in his hand" against the Philistine (1Sa 19:5); The men to David: "If half of us die, they will not care [*set heart*] about us. But you are worth ten thousand of us" (2Sa 18:3). The enemy's heart is indifferent to many deaths. One life is weighed at ten thousand.; "the men who were seeking your life are dead" (Exo 4:19) → Moses returns (4:20). The death of the hunters frees the hunted life.; "Why then are yo ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Exo 4:19 (dead), Judg 5:18 (lives)
- **Observation 16213** (prior-capture, tag statement, status draft): Death as evidence that hardens: "not one of the livestock of Israel was dead. But the heart of Pharaoh was hardened" (Exo 9:7). The evidence is seen and the heart still hardens (§3.3). Evidence does not move the heart (compare Jacob, whose spirit revives on seeing, §2).
  - applies to 1 occurrence(s): Exo 9:7 (dead)
- **Observation 16217** (prior-capture, tag statement, status draft): 14. Cross-cutting observations for Batch G [Claude reading]: Life is held in the breath and the soul, and it is God's to give and gather.; "Living soul" is shared with the animals. God's breathing is what marks Gen 2:7.; One decision of God's heart could gather every breath back (Job 34:14–15).; In the flood narrative God's heart changes while man's heart does not (Gen 6:5–6 → 8:21).; *rûaḥ* moves across senses within a single passage, and the passage uses the movement: Eze 37: carrying Spirit → breath → winds → "my Spirit within you"; Judg 15: rushing Spirit → one's own spirit returning; Jon 4: an appointed wind that makes the soul wish to die; Strength and hardness are one word. *ḥāzaq* is ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Gen 2:7 (living)
- **Observation 16234** (prior-capture, tag statement, status draft): 0. Data notes: "Declares the Lord" (M42) — pre-filter.; H5002 *nĕʾum* accounts for 43 pairs in 38 verses. The M47 word sits in the oracle's content, not in the formula. The formula itself is not about the inner seat.; The pairs are not dropped. The oracle content is read in §1.9.; → Ruling R1.; The other pre-filters do not apply here. Neither "Holy Spirit" (M61, done in Batch D) nor "Lord of hosts" (M72) falls in Batch E clusters.; Misfiled tags, noted and not used (beyond R1–R11): M42 "call by name" (H7121H): naming, not calling on God — "whatever the man called every living creature [*nephesh*]" (Gen 2:19), "she shall be called Woman" (Gen 2:23), Peniel (Gen 32:30). Two are kept as in §1.8 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Gen 2:19 (living)
- **Observation 16274** (prior-capture, tag statement, status draft): Spirit: "I will put my Spirit within you, and you shall live" (Eze 37:14) [D1]; "when I pour out my Spirit upon the house of Israel" (Eze 39:29) [D1]; "formed the spirit of man within him" (Zec 12:1) [H1]; "he who is humble and contrite in spirit and trembles at my word" (Isa 66:2) [H1]; "every heart will melt … every spirit will faint" (Eze 21:7) [H2]
  - applies to 1 occurrence(s): Eze 37:14 (live)
- **Observation 16290** (prior-capture, tag statement, status draft): Heart and flesh sing: "My soul longs, yes, faints … my heart and flesh sing for joy to the living God" (Psa 84:2).
  - applies to 1 occurrence(s): Psa 84:2 (living)
- **Observation 16317** (prior-capture, tag statement, status draft): Self-congratulation: "though, while he lives, he counts himself [*his soul*] blessed — and though you get praise when you do well for yourself" (Psa 49:18).
  - applies to 1 occurrence(s): Psa 49:18 (lives)
- **Observation 16323** (prior-capture, tag statement, status draft): 4.2 Worship in spirit: "God is spirit, and those who worship him must worship in spirit and truth" (Joh 4:24); "the true worshipers will worship the Father in spirit and truth" (Joh 4:23) [D1+H2]; "who worship by the Spirit of God … and put no confidence in the flesh" (Phili 3:3) [D1]; "God is my witness, whom I serve with my spirit" (Rom 1:9) [H1]; "the ministry of the Spirit" (2Co 3:8); "written … with the Spirit of the living God … on tablets of human hearts" (2Co 3:3); "present your bodies as a living sacrifice … your spiritual worship" (Rom 12:1, d0)
  - applies to 2 occurrence(s): Rom 12:1 (living), 2Cor 3:3 (living)
- **Observation 16326** (prior-capture, tag statement, status draft): 4.3 The conscience of the worshiper: "gifts and sacrifices are offered that cannot perfect the conscience of the worshiper" (Heb 9:9); "purify our conscience from dead works to serve the living God" (Heb 9:14) [U]; "the worshipers, having once been cleansed, would no longer have any consciousness of sins" (Heb 10:2); "I thank God whom I serve … with a clear conscience" (2Ti 1:3)
  - applies to 1 occurrence(s): Heb 9:14 (living)
- **Observation 16344** (prior-capture, tag statement, status draft): Soul: "entrust their souls to a faithful Creator" (1Pe 4:19); "the outcome of your faith, the salvation of your souls" (1Pe 1:9); "those who have faith and preserve their souls" (Heb 10:39); "strengthening the souls … to continue in the faith" (Act 14:22); "his soul is puffed up … but the righteous shall live by his faith" (Hab 2:4; Heb 10:38); "a faithful messenger … refreshes the soul of his masters" (Pro 25:13)
  - applies to 2 occurrence(s): Hab 2:4 (live), Heb 10:38 (live)
- **Observation 16346** (prior-capture, tag statement, status draft): Flesh: "the life I now live in the flesh I live by faith in the Son of God" (Gal 2:20).
  - applies to 1 occurrence(s): Gal 2:20 (live)
- **Observation 16348** (prior-capture, tag statement, status draft): 5.4 Unbelief (M31): "an evil, unbelieving heart, leading you to fall away from the living God" (Heb 3:12); "he rebuked them for their unbelief and hardness of heart" (Mar 16:14); "If anyone thinks he is religious and does not bridle his tongue but deceives his heart, this person's religion is worthless" (Jam 1:26); "to the defiled and unbelieving, nothing is pure; but both their minds and their consciences are defiled" (Tit 1:15); "self-made religion … of no value in stopping the indulgence of the flesh" (Col 2:23)
  - applies to 1 occurrence(s): Heb 3:12 (living)
- **Observation 16382** (prior-capture, tag statement, status draft): Offered to the soul: "hear, that your soul may live; and I will make with you an everlasting covenant" (Isa 55:3).
  - applies to 1 occurrence(s): Isa 55:3 (live)
- **Observation 16385** (prior-capture, tag statement, status draft): The covenant with all flesh and every living *nephesh*: "between me and you and every living creature [*nephesh ḥayyâ*] of all flesh" (Gen 9:12, 15–17); "never again shall all flesh be cut off" (Gen 9:11).
  - applies to 1 occurrence(s): Gen 9:16 (living)
- **Observation 16408** (prior-capture, tag statement, status draft): 9.1 Atonement for souls; forgiveness according to the heart: "the Lord's offering to make atonement for your lives" (Exo 30:15–16); "to make atonement for ourselves [*our souls*]" (Num 31:50); "the Day of Atonement … you shall afflict yourselves [*your souls*]" (Lev 23:27)
  - applies to 2 occurrence(s): Exo 30:15 (lives), Exo 30:16 (lives)
- **Observation 16437** (prior-capture, tag statement, status draft): Favor and the soul-life: "they will be life for your soul and adornment [*grace*] for your neck" (Pro 3:22); "If I have found favor … let my life be granted" (Est 7:3); Gen 19:19; "as your soul lives, there is but a step between me and death" (1Sa 20:3)
  - applies to 1 occurrence(s): 1Sa 20:3 (lives)
- **Observation 16443** (prior-capture, tag statement, status draft): Oath of the redeemed soul: "As the Lord lives, who has redeemed my soul [*life*] out of every adversity" (1Ki 1:29; 2Sa 4:9).
  - applies to 2 occurrence(s): 2Sa 4:9 (lives), 1Ki 1:29 (lives)
- **Observation 16464** (prior-capture, tag statement, status draft): Others save the soul: "If you strike him with the rod, you will save his soul from Sheol" (Pro 23:14); "A truthful witness saves lives" (Pro 14:25); "whoever brings back a sinner … will save his soul from death" (Jam 5:20).
  - applies to 1 occurrence(s): Pro 14:25 (lives)
- **Observation 16472** (prior-capture, tag statement, status draft): 11.4 Help — spirit vs flesh: "Let my soul live and praise you, and let your rules help me" (Psa 119:175); "he bowed their hearts down with hard labor; they fell down, with none to help" (Psa 107:12)
  - applies to 1 occurrence(s): Psa 119:175 (live)
- **Observation 16473** (prior-capture, tag statement, status draft): The soul satisfied: "My soul will be satisfied as with fat and rich food" (Psa 63:5); "he satisfies the longing soul" (Psa 107:9); "if you pour yourself out for the hungry and satisfy the desire [*nephesh*] of the afflicted" (Isa 58:10) — pouring out one's own nephesh to satisfy another's; "satisfy your desire in scorched places" (Isa 58:11); "Out of the anguish of his soul he shall see and be satisfied" (Isa 53:11); "I will feast the soul of the priests" (Jer 31:14); "The afflicted shall eat and be satisfied … May your hearts live forever!" (Psa 22:26)
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 16481** (prior-capture, tag statement, status draft): Flesh first, then breath: "I will … cause flesh to come upon you, and cover you with skin, and put breath in you, and you shall live" (Eze 37:6); "flesh had come upon them, and skin had covered them. But there was no breath in them" (Eze 37:8). [Claude reading] Covered flesh without *rûaḥ* is not yet life. The two-stage sequence keeps flesh and breath distinct.
  - applies to 1 occurrence(s): Eze 37:6 (live)
- **Observation 16494** (prior-capture, tag statement, status draft): 0. Data notes: Luk 12:45; Mat 24:48 "says to himself [*in his heart*] 'My master is delayed'" — the delay tag is a misfile (R5). The inner-speech content is kept as in §10.; Deu 22:26 "murdering" (*nephesh* in "strike him … a life") + "offense" (M56).; Lev 20:19 "relative" (*šĕʾēr* flesh) + "bear iniquity" (M56).; Nephesh = corpse [lexical]. *nephesh mēt* "soul of a dead one" = dead body. It is the M10c pairing in Num 5:2; 6:11; 9:6, 7, 10; 19:11, 13; Lev 21:1, 11; 22:4; Hag 2:13. It is kept in §8.2 as a fringe of real significance, not dropped.; Distance note. Positions are in original-language word order [verify]. d0 = one token carries both tags (e.g. 2Ch 26:16 "grew proud" = *gāvah lēv* ... (cut; the whole text is in the workbook)
  - applies to 6 occurrence(s): Lev 21:1 (dead), Lev 21:11 (dead), Lev 22:4 (dead), Num 5:2 (dead), Num 19:11 (dead), Num 19:13 (dead)
- **Observation 16510** (prior-capture, tag statement, status draft): Longing: "My soul is consumed with longing for your rules at all times" (Psa 119:20); "Let my soul live and praise you, and let your rules help me" (Psa 119:175).
  - applies to 1 occurrence(s): Psa 119:175 (live)
- **Observation 16525** (prior-capture, tag statement, status draft): Righteousness saves the soul-life: "they would deliver but their own lives by their righteousness" (Eze 14:14, 20); "does what is just and right, he shall save his life" (Eze 18:27); "He restores my soul. He leads me in paths of righteousness" (Psa 23:3).
  - applies to 2 occurrence(s): Eze 14:14 (lives), Eze 14:20 (lives)
- **Observation 16529** (prior-capture, tag statement, status draft): The puffed-up soul: "his soul is puffed up; it is not upright within him, but the righteous shall live by his faith" (Hab 2:4). Heb 10:38 quotes it with God as speaker: "my soul has no pleasure in him".
  - applies to 2 occurrence(s): Hab 2:4 (live), Heb 10:38 (live)
- **Observation 16565** (prior-capture, tag statement, status draft): 3.2 Sin against one's own soul: "he who fails to find me injures himself [*his nephesh*]" (Pro 8:36); "whoever provokes him to anger forfeits [*sins against*] his life" (Pro 20:2); "you have forfeited your life [*sinned against your soul*]" (Hab 2:10); "the censers of these men who have sinned at the cost of their lives" (Num 16:38)
  - applies to 1 occurrence(s): Num 16:38 (lives)
- **Observation 16610** (prior-capture, tag statement, status draft): Soul: "who does not lift up his soul to what is false" (Psa 24:4); "whoever guards his soul will keep far from them [the crooked]" (Pro 22:5); "putting to death souls who should not die and keeping alive souls who should not live, by your lying" (Eze 13:19) — lies that kill and keep alive souls; "A truthful witness saves lives" (Pro 14:25); "the desire [*nephesh*] of the treacherous is for violence" (Pro 13:2)
  - applies to 3 occurrence(s): Pro 14:25 (lives), Eze 13:19 (alive), Eze 13:19 (live)
- **Observation 16643** (prior-capture, tag statement, status draft): Holy flesh / body (NT): "reconciled in his body of flesh … to present you holy and blameless" (Col 1:22); "present your bodies as a living sacrifice, holy … your spiritual worship" (Rom 12:1); "a spiritual house, to be a holy priesthood" (1Pe 2:5)
  - applies to 1 occurrence(s): Rom 12:1 (living)
- **Observation 16672** (prior-capture, tag statement, status draft): 8.2 Nephesh = corpse — defilement by the dead (§0.8): "everyone who is unclean through contact with the dead [*a nephesh*]" (Num 5:2); "unclean through touching a dead body [*the nephesh of a man*]" (Num 9:6, 7, 10); "Whoever touches the dead body of any person" (Num 19:11, 13); "No one shall make himself unclean for the dead" (Lev 21:1); "He shall not go in to any dead bodies" (Lev 21:11); Lev 22:4; Hag 2:13; "he sinned by reason of the dead body" (Num 6:11); [lexical; Claude reading] The word for the living self is also the word for the body just vacated. It defiles whoever touches it. This is the far end of *nephesh* = "person": the person as corpse.
  - applies to 6 occurrence(s): Lev 21:1 (dead), Lev 21:11 (dead), Lev 22:4 (dead), Num 5:2 (dead), Num 19:11 (dead), Num 19:13 (dead)
- **Observation 16706** (prior-capture, tag statement, status draft): 9.5 ◆ Fringe: "man looks on the outward appearance [*height of stature*], but the Lord looks on the heart" (1Sa 16:7); "As the heavens for height … so the heart of kings is unsearchable" (Pro 25:3) — height as depth; "I know your presumption and the evil of your heart" (1Sa 17:28) — pride attributed to David's heart by his brother, wrongly; a misreading of another's heart; "Zebulun is a people who risked [*despised*] their lives to the death" (Judg 5:18) — the *nephesh* held cheap for a cause (R10); "my heart does not reproach me for any of my days" (Job 27:6) — the heart as internal accuser, silent (cf. §3.3 2Sa 24:10); "Be wise, my son, and make my heart glad, that I may answer him who rep ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Judg 5:18 (lives)
- **Observation 16712** (prior-capture, tag statement, status draft): Humble hearts revive: "When the humble see it they will be glad; you who seek God, let your hearts revive" (Psa 69:32); "The afflicted shall eat and be satisfied … May your hearts live forever!" (Psa 22:26).
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 16718** (prior-capture, tag statement, status draft): God saves the needy's life: "saves the lives of the needy" (Psa 72:13); "he has delivered the life of the needy from the hand of evildoers" (Jer 20:13); "to save him from those who condemn his soul to death" (Psa 109:31)
  - applies to 1 occurrence(s): Psa 72:13 (lives)
- **Observation 16719** (prior-capture, tag statement, status draft): Equal ransom: "the rich shall not give more, and the poor shall not give less … to make atonement for your lives" (Exo 30:15) — every nephesh ransomed at the same price.
  - applies to 1 occurrence(s): Exo 30:15 (lives)
- **Observation 16727** (prior-capture, tag statement, status draft): 11. Cross-cutting observations for Batch D [Claude reading]: Conscience is the NT's named moral-awareness faculty. It can be clear, pure, good, evil, defiled, seared, weak or wounded. It testifies (2Co 1:12; Rom 9:1) and is purified by Christ's blood (Heb 9:14). It is frequently paired with the heart (1Ti 1:5; Heb 10:22).; The OT does this work with the heart: "David's heart struck him" (2Sa 24:10); "my heart does not reproach me" (Job 27:6).; The Levitical "realizes his guilt" (Lev 5) describes the same moment without naming an organ.; The heart deceives itself and is the source of evil.; It deceives its owner: Jer 17:9; Obd 3; Isa 44:20.; Evil comes from it: Gen 6:5; Mat 15:19; Luk 6:45.; ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Eze 13:19 (alive), Rom 12:1 (living)
- **Observation 16754** (prior-capture, tag statement, status draft): A reward for murder refused: the murderers of Ish-bosheth: "your enemy, who sought your life. The Lord has avenged my lord the king" (2Sa 4:8) → David: "As the Lord lives, who has redeemed my life out of every adversity" → he has them killed (4:9–12). The claim of vengeance on David's behalf is answered by an oath on David's own redeemed soul.
  - applies to 1 occurrence(s): 2Sa 4:9 (lives)
- **Observation 16782** (prior-capture, tag statement, status draft): 2.2 The price of a life, again: "The ransom of a man's life is his wealth, but a poor man hears no threat" (Pro 13:8); "each shall give a ransom for his life … The rich shall not give more, and the poor shall not give less … to make atonement for your lives" (Exo 30:12–16; context read) → Batch D; Batch E; "your life shall be for his life, or else you shall pay a talent of silver" (1Ki 20:39) → §1.4; Satan: "Skin for skin! All that a man has he will give for his life" (Job 2:4) → "only spare [*guard*] his life" (2:6). Context read: Job 2:3–7.; "they have devoured human lives; they have taken treasure" (Eze 22:25); [Claude reading] Batch G §5.4 read Mic 6:7 and Mat 16:26 as a refusal to set a ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Exo 30:15 (lives), Exo 30:16 (lives), Eze 22:25 (lives)
- **Observation 16797** (prior-capture, tag statement, status draft): 3.3 Burden — who bears it: "it has seemed good to the Holy Spirit and to us to lay on you no greater burden" (Act 15:28) [D1]; "they cannot save the burden, but themselves [*their nephesh*] go into captivity" (Isa 46:2) — the idols, which have to be carried, and their carriers; "Take care for the sake of your lives, and do not bear a burden on the Sabbath" (Jer 17:21) → §5.1
  - applies to 1 occurrence(s): Jer 17:21 (lives)
- **Observation 16858** (prior-capture, tag statement, status draft): Revisit (Batch G §4): just before this, Abner answers the same question with an oath: "As your soul lives, O king, I do not know" (1Sa 17:55). A formal oath by Saul's soul stands on the threshold of Jonathan's soul being knit to David's.
  - applies to 1 occurrence(s): 1Sa 17:55 (lives)
- **Observation 16877** (prior-capture, tag statement, status draft): 3.2 In the Gospels: hate your soul: "Whoever loves his life loses it, and whoever hates his life in this world will keep it for eternal life" (Joh 12:25); "If anyone … does not hate … even his own life, he cannot be my disciple" (Luk 14:26); "they loved not their lives even unto death" (Rev 12:11); Lose / save: Mat 10:39; 16:25; Mar 8:35; Luk 9:24; 17:33
  - applies to 1 occurrence(s): Rev 12:11 (lives)
- **Observation 16878** (prior-capture, tag statement, status draft): The positive form — laying the soul down: "The good shepherd lays down his life" (Joh 10:11, 17); "Greater love has no one than this, that someone lay down his life for his friends" (Joh 15:13); "we ought to lay down our lives for the brothers" (1Jo 3:16); "I will most gladly spend and be spent for your souls" (2Co 12:15)
  - applies to 1 occurrence(s): 1Jo 3:16 (lives)
- **Observation 16884** (prior-capture, tag statement, status draft): Revisit (Batch G v3 §16.10): The "chosen" form has an OT precedent in battle and pledge.; "Zebulun … risked their lives to the death" (Judg 5:18); "Our life for yours even to death!" (Jos 2:14); David "took his life in his hand" (1Sa 19:5); Rev 12:11 ("loved not their lives even unto death") uses the same shape. What the NT adds is the object ("for the name of the Lord Jesus", Act 21:13) and the example ("poured out his soul to death", Isa 53:12).
  - applies to 2 occurrence(s): Judg 5:18 (lives), Rev 12:11 (lives)
- **Observation 16932** (prior-capture, tag statement, status draft): What the pattern shows [Claude reading]: The merry heart is a threshold state. In every narrative it comes after eating and drinking and immediately before a decisive event, which others usually initiate. The good heart lowers guard. What enters at that moment decides the outcome: murder (Amnon); exposure and anger (Vashti, Ahasuerus); mockery turned to catastrophe (Samson); outrage (Gibeah); approach and redemption (Ruth); a dead heart the next morning (Nabal); God's claim on the soul (the rich fool); The heart's condition swings overnight. Nabal: merry heart → dead heart (1Sa 25:36–37). Ahasuerus: merry heart → burning anger (Est 1:10–12). The heart's state is not stable; wine sets it high ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 11:11 (lives)
- **Observation 16995** (prior-capture, tag statement, status draft): 0. Data notes: Pre-filters from the handoff do not apply here. None of "Holy Spirit" (M61), "declares the Lord" (M42) or "Lord of hosts" (M72) falls in Batch C clusters. Nothing was removed.; "Seek my life" is one idiom, not inner seeking. About 40 of the 96 M83 verses are *biqqēš nephesh* — "seek (someone's) life" (1Sa 20:1; 23:15; 1Ki 19:10, 14; Jer 11:21; 19:7; 21:7; 22:25; 34:20–21; 44:30; 46:26; 49:37; Psa 35:4; 38:12; 40:14; 54:3; 63:9; 70:2; 86:14; Mat 2:20; Rom 11:3; etc.). Here *nephesh* is life as the object of hostile pursuit. It is reported in §7.5 and not mixed with the soul that seeks.; "Lacks sense" is "lacking heart" (H2638 + H3820A, d1): Pro 7:7; 9:4, 16; 10:13, 21; 11:12; 1 ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): 2Ki 2:2 (live), 2Ki 2:4 (live), 2Ki 2:6 (live), 2Ki 4:30 (live)
- **Observation 17021** (prior-capture, tag statement, status draft): Sorrow better than laughter: "by sadness of face the heart is made glad" (Ecc 7:3); "the living will lay it to heart" (Ecc 7:2).
  - applies to 1 occurrence(s): Ecc 7:2 (living)
- **Observation 17060** (prior-capture, tag statement, status draft): Human choosing: "I would choose strangling and death rather than my bones" (Job 7:15) — the *nephesh* chooses death; "These have chosen their own ways, and their soul delights in their abominations" (Isa 66:3); "If I am to live in the flesh … which I shall choose I cannot tell" (Phili 1:22)
  - applies to 1 occurrence(s): Phili 1:22 (live)
- **Observation 17071** (prior-capture, tag statement, status draft): 3.2 Greed: "They have eyes full of adultery … They entice unsteady souls. They have hearts trained in greed" (2Pe 2:14) — heart trained, souls unsteady; "their heart is set on their gain" (Eze 33:31); "the one greedy for gain … renounces the Lord" (Psa 10:3); "greedy for unjust gain; it takes away the life [*nephesh*] of its possessors" (Pro 1:19) — greed kills its own soul; "destroying lives to get dishonest gain" (Eze 22:27)
  - applies to 1 occurrence(s): Eze 22:27 (lives)
- **Observation 17073** (prior-capture, tag statement, status draft): Positive flesh-heart: "written … with the Spirit of the living God, not on tablets of stone but on tablets of human [*fleshly*] hearts" (2Co 3:3) [D1]. This echoes the "heart of flesh" of Eze 36:26 (§8.3).
  - applies to 1 occurrence(s): 2Cor 3:3 (living)
- **Observation 17087** (prior-capture, tag statement, status draft): 5.2 Patience and endurance: "be patient. Establish your hearts" (Jam 5:8); "hold it fast in an honest and good heart, and bear fruit with patience" (Luk 8:15); "By your endurance you will gain your lives [*souls*]" (Luk 21:19); "so that you may not grow weary or fainthearted [*faint in your souls*]" (Heb 12:3); "May the Lord direct your hearts to the love of God and to the steadfastness of Christ" (2Th 3:5); "firmly established in his heart" (1Co 7:37)
  - applies to 1 occurrence(s): Luk 21:19 (lives)
- **Observation 17092** (prior-capture, tag statement, status draft): 5.3 Forever — the inner seat and duration: "May your hearts live forever!" (Psa 22:26); "For I will not contend forever … for the spirit would grow faint before me, and the breath of life that I made" (Isa 57:16) [H2] — God limits his contending for the sake of the human spirit; "who inhabits eternity … I dwell … also with him who is of a contrite and lowly spirit, to revive the spirit of the lowly, and to revive the heart of the contrite" (Isa 57:15) [H1]; "Do not deliver the soul of your dove to the wild beasts" (Psa 74:19)
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 17109** (prior-capture, tag statement, status draft): Seeking hearts rejoice / revive: "let the hearts of those who seek the Lord rejoice" (1Ch 16:10; Psa 105:3); "you who seek God, let your hearts revive" (Psa 69:32); "May your hearts live forever" (Psa 22:26).
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 17122** (prior-capture, tag statement, status draft): NT: "those who sought the child's life are dead" (Mat 2:20) — echoing "all the men who were seeking your life are dead" (Exo 4:19).
  - applies to 1 occurrence(s): Exo 4:19 (dead)
- **Observation 17173** (prior-capture, tag statement, status draft): 10. Madness (M66): "the hearts of the children of man are full of evil, and madness is in their hearts while they live" (Ecc 9:3); "The Lord will strike you with madness and blindness and confusion of mind [*heart*]" (Deu 28:28); "I applied my heart to know wisdom and to know madness and folly … a striving after wind" (Ecc 1:17); "I turned my heart to know … the foolishness that is madness" (Ecc 7:25); "The prophet is a fool; the man of the spirit is mad" (Hos 9:7) [U]; [Claude reading] Madness is located in the heart (Ecc 9:3; Deu 28:28). The heart can also investigate madness (Ecc 1:17; 7:25). Hos 9:7 is the only verse linking madness to "spirit", and its spirit is not determinable.
  - applies to 1 occurrence(s): Ecc 9:3 (live)
- **Observation 17252** (prior-capture, tag statement, status draft): self (H5315I, G5590I) | "as you yourself live" (2Ki 2:2, 4, 6); "afflict yourselves" on the Day of Atonement (Lev 16:29, 31; 23:27, 32); vows "by which she has bound herself" (Num 30)
  - applies to 3 occurrence(s): 2Ki 2:2 (live), 2Ki 2:4 (live), 2Ki 2:6 (live)
- **Observation 17254** (prior-capture, tag statement, status draft): living creature (H5315K) | Gen 1:20–24; "the man became a living creature" (Gen 2:7)
  - applies to 4 occurrence(s): Gen 1:20 (living), Gen 1:21 (living), Gen 1:24 (living), Gen 2:7 (living)
- **Observation 17255** (prior-capture, tag statement, status draft): dead body (H5315M) | "the dead body of any person" (Num 19:11; 6:6; 9:6–10)
  - applies to 2 occurrence(s): Num 6:6 (dead), Num 19:11 (dead)
- **Observation 17259** (prior-capture, tag statement, status draft): a. One word: wind, breath, spirit, Spirit, spirits, side, temper: *Wind:* storms, the east wind, the four winds (e.g. Exo 14:21; 1Ki 19:11; Jon 1:4; Psa 1:4).; *Breath:* "the breath of life" (Gen 7:22); "put breath in you, and you shall live" (Eze 37:5–10).; *A person's spirit:* troubled, revived, broken, lowly (below).; *God's Spirit:* rushing upon, filling, indwelling (below).; *Other spirits:* lying (1Ki 22:21–23), harmful (1Sa 16:14–23), unclean (Mar 1–9; Luk 4–11), deceitful (1Ti 4:1).; *"Side" of the compass* (H7307I; 1Ch 9:24; Eze 42:16–20) — fringe: *wind* = *direction*.; *Temper* (H7307J): "hasty temper" (Pro 14:29); "cool spirit" (Pro 17:27); "A fool gives full vent to his spirit" ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Eze 37:5 (live), Eze 37:6 (live), Eze 37:9 (live)
- **Observation 17264** (prior-capture, tag statement, status draft): e. Wind and breath in relation to the inner being — explicitly retained per the researcher: *Breath = life in flesh:*; "all flesh in which is the breath of life" (Gen 6:17; 7:15, 22); "sinews … flesh … skin … But there was no breath in them" → "breath came into them, and they lived" (Eze 37:6–10); "When you take away their breath, they die and return to their dust" (Psa 104:29); *Breath and thought:* "When his breath departs, he returns to the earth; on that very day his plans perish" (Psa 146:4). Link to the thought vocabulary (see brief §5).; *Breath as frailty:* "Remember that my life is a breath" (Job 7:7); "They all have the same breath, and man has no advantage over the beasts" (Ecc 3: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Eze 37:10 (lived)
- **Observation 17274** (prior-capture, tag statement, status draft): 3.4 Distinction — where the text separates the components: *Division of soul and spirit (Heb 4:12):* "piercing to the division of soul and of spirit, of joints and of marrow, and discerning the thoughts and intentions of the heart." [Claude reading] Soul and spirit are close enough that only the word of God can separate them, just as joints and marrow are adjacent parts of the body. The heart is where the *thoughts and intentions* are, and they are *discerned* there.; *Living soul vs life-giving spirit:* "The first man Adam became a living being [psychē]; the last Adam became a life-giving spirit" (1Co 15:45; cf. Gen 2:7).; *Spirit vs mind:* 1Co 14:14–15 (above).; *Spirit vs flesh (as kind): ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Gen 2:7 (living), 1Cor 15:45 (living)
- **Observation 17275** (prior-capture, tag statement, status draft): 3.5 Opposition: *Flesh vs Spirit* (Paul): Gal 3:3; 4:29; 5:16–17; 6:8; Rom 8:4–9, 13; Phili 3:3.; *Flesh's passions vs soul:* "passions of the flesh, which wage war against your soul" (1Pe 2:11).; *Mind vs flesh:* Rom 7:25.; *Hebrew background:*; "He remembered that they were but flesh" (Psa 78:39); "My Spirit shall not abide in man forever, for he is flesh" (Gen 6:3); trusting flesh ↔ heart turning from the Lord (Jer 17:5); [Claude reading] In the OT verses read here, flesh is frail, not hostile. The hostility of flesh to Spirit is NT-specific in this dataset. Even in the NT, neutral flesh remains (one flesh, Word became flesh, "the life I now live in the flesh I live by faith" Gal 2:20).
  - applies to 1 occurrence(s): Gal 2:20 (live)
- **Observation 17277** (prior-capture, tag statement, status draft): 3.6 Cause and effect between inner seat, body and senses: *Appetite (soul) and heart:* "They tested God in their heart by demanding the food they craved" (Psa 78:18); the fool's heart "busy with iniquity … to leave the craving of the hungry unsatisfied" (Isa 32:6); "you crave meat" (Deu 12:20).; *Heart → mouth, hands, feet, deeds:* §2.1h. Also: "clean hands and a pure heart" (Psa 24:4); "Let us lift up our hearts and hands to God" (Lam 3:41); "a heart that devises wicked plans, feet that make haste to run to evil" (Pro 6:18); "The heart of man plans his way, but the Lord establishes his steps" (Pro 16:9); "The law of his God is in his heart; his steps do not slip" (Psa 37:31); *Heart ↔ ears ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 55:3 (live)
- **Observation 17280** (prior-capture, tag statement, status draft): 3.9 The boundary of death — where the components come apart: *Soul departs:* "as her soul was departing" (Gen 35:18); soul to Sheol, pit, silence (§2.2d).; *Spirit and breath return to God:*; "the dust returns to the earth as it was, and the spirit returns to God who gave it" (Ecc 12:7); "Who knows whether the spirit of man goes upward and the spirit of the beast goes down into the earth?" (Ecc 3:21); "When you take away their breath, they die and return to their dust" (Psa 104:29); "Into your hand I commit my spirit" (Psa 31:5; Luk 23:46; Act 7:59); "No man has power to retain the spirit" (Ecc 8:8); *Return to life:*; "her spirit returned, and she got up" (Luk 8:55); "the life of the child ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Num 19:11 (dead), Num 19:13 (dead)
- **Observation 17480** (prior-capture, tag statement, status draft): 15. Aims (10.7 *Setting the heart*): *"I make it my ambition to preach the gospel, not where Christ has already been named"* (Rom 15:20); *"whether we are at home or away, we make it our aim to please him. For we must all appear before the judgment seat of Christ"* (2Co 5:9–10); *"aspire to live quietly, and to mind your own affairs, and to work with your hands"* (1Th 4:11); *"If anyone aspires to the office of overseer, he desires a noble task"* (1Ti 3:1); The word (*philotimeomai*) is the one used for ambition. I read what it is aimed at in these verses as unexpected: going where no one has gone, pleasing him wherever one is, and quietness.
  - applies to 1 occurrence(s): 1Th 4:11 (live quietly)
- **Observation 17571** (prior-capture, tag statement, status draft): Psa 119:143. *"Trouble and anguish have found me out, but your commandments are my delight."* It is followed by *"give me understanding that I may live"* (119:144).
  - applies to 1 occurrence(s): Psa 119:144 (live)
- **Observation 17660** (prior-capture, tag statement, status draft): Pro 9:17–18. "Stolen water is sweet". The sweetness is in the stealing. "he does not know that the dead are there."
  - applies to 1 occurrence(s): Pro 9:18 (dead)
- **Observation 17775** (prior-capture, tag statement, status draft): Joh 7:37–39 | "Out of his heart will flow rivers of living water", said "about the Spirit" | Compare John 4:14: there the spring wells up *in* him; here rivers flow *out of* him. I read a want met that becomes a source for others (Ch 6)
  - applies to 1 occurrence(s): Joh 7:38 (living)
- **Observation 17880** (prior-capture, tag statement, status draft): Compare the other Titus verse: a slave becomes a pupil. *"For the grace of God has appeared … training us to renounce ungodliness and worldly passions, and to live self-controlled, upright, and godly lives"* (2:11–12).: In 3:3 the passions are a master. In 2:12 grace is a teacher, and the person now does something: renounces.
  - applies to 1 occurrence(s): Tit 2:12 (live)
- **Observation 17900** (prior-capture, tag statement, status draft): The question. *"For who knows what is good for man while he lives the few days of his vain life, which he passes like a shadow?"* (Ecc 6:12). It closes the passage already in 10.6: the man who lacks nothing yet cannot enjoy it (6:2), and *"Better is the sight of the eyes than the wandering of the appetite"* (6:9).
  - applies to 1 occurrence(s): Ecc 6:12 (lives)
- **Observation 17909** (prior-capture, tag statement, status draft): Psalm 119: longing and delight, joined to asking for life.: *"Turn my eyes from looking at worthless things; and give me life in your ways"* (119:37), then *"Behold, I long for your precepts; in your righteousness give me life!"* (119:40). The eye is turned from worthless things, and the longing is set on the precepts. Yet the life is still asked for. The longing does not give it.; *"Let your mercy come to me, that I may live; for your law is my delight"* (119:77). It comes just after *"in faithfulness you have afflicted me"* (119:75).; Compare 119:70, already in 10.6: "their heart is unfeeling like fat, but I delight in your law". There, delight stands against other people's dullness. Here, ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 119:77 (live)
- **Observation 17918** (prior-capture, tag statement, status draft): The figure: a spring, not a cistern. *"The water that I will give him will become in him a spring of water welling up to eternal life"* (4:14). Set it beside Jeremiah, in Ch 2: *"they have forsaken me, the fountain of living waters, and hewed out cisterns for themselves, broken cisterns that can hold no water"* (Jer 2:13).: A cistern holds what is poured into it, and a broken one loses it.; A spring wells up from inside.; "Everyone who drinks of this water will be thirsty again" (4:13) describes a want that must be refilled. "Never be thirsty again" describes a want met at its source, and the source is "in him".
  - applies to 1 occurrence(s): Jer 2:13 (living)
- **Observation 17929** (prior-capture, tag statement, status draft): Who greed harms. *"Whoever is greedy for unjust gain troubles his own household, but he who hates bribes will live"* (Pro 15:27).: Already in 10.6, greed *"takes away the life of its possessors"* (Pro 1:19).; Here it reaches his household.; The answer is not a lack of desire. It is a counter-desire: he "hates" bribes. I read it as one passion held off by another.
  - applies to 1 occurrence(s): Pro 15:27 (live)
- **Observation 17938** (prior-capture, tag statement, status draft): A will that changes when the cost appears. In Ruth, the nearer redeemer first says *"I will redeem it"* about the land (Rut 4:4). When he hears that Ruth comes with it: *"I cannot redeem it for myself, lest I impair my own inheritance"* (4:6). It is the same man in the same scene. His will turns when his own inheritance is touched.: Set against him is Boaz: *"if he is not willing to redeem you, then, as the Lord lives, I will redeem you"* (3:13).; Boaz leaves room for the other man's will, by law and in public at the gate.; He binds his own will by oath.; Ruth's choice frames it: *"you have not gone after young men"* (3:10).
  - applies to 1 occurrence(s): Rut 3:13 (lives)
- **Observation 17939** (prior-capture, tag statement, status draft): The will set on godliness, and what it meets. *"Indeed, all who desire to live a godly life in Christ Jesus will be persecuted"* (2Ti 3:12). Paul has listed his "aim in life" and his sufferings (3:10–11).: Compare 1Ti 6:9, in 10.7: *"those who desire to be rich fall into temptation, into a snare"*. It is the same verb of wanting.; Wanting riches leads into a snare. Wanting godliness leads into persecution.
  - applies to 1 occurrence(s): 2Ti 3:12 (live)
- **Observation 17944** (prior-capture, tag statement, status draft): No pleasure in death, said to two kinds of hearer.: In Ezekiel 18 the people accuse: *"The way of the Lord is not just"* (18:25, 29). God answers with his pleasure, *"Have I any pleasure in the death of the wicked … and not rather that he should turn from his way and live?"* (18:23). He ends with *"make yourselves a new heart and a new spirit! Why will you die?"* and *"For I have no pleasure in the death of anyone"* (18:31–32).; In Ezekiel 33 the people despair: *"Surely our transgressions and our sins are upon us, and we rot away because of them. How then can we live?"* (33:10). God answers on oath: *"As I live … I have no pleasure in the death of the wicked"* (33:11).
  - applies to 4 occurrence(s): Eze 18:23 (live), Eze 18:32 (live), Eze 33:10 (live), Eze 33:11 (live)
- **Observation 18244** (prior-capture, tag face, status draft): Face: D06. Dying of hunger, thirst, sickness or danger; Hits / verses: 39 / 33; What differs: "that we may live and not die"; "at the point of death"; "before my child dies"; Example verses: Gen 42:2; 2Ki 7:4; 2Ki 20:1; Joh 4:47
  - applies to 2 occurrence(s): Gen 42:2 (live), 2Ki 7:4 (live)
- **Observation 18247** (prior-capture, tag face, status draft): Face: D09. The dead; Hits / verses: 20 / 19; What differs: The dead do not praise; inquiring of the dead; "not dead but sleeping"; going to the dead; Example verses: Psa 6:5; 115:17; Isa 8:19; Mat 9:24; 2Sa 12:23
  - applies to 4 occurrence(s): 2Sa 12:23 (dead), Psa 115:17 (dead), Isa 8:19 (dead), Mat 9:24 (dead)
- **Observation 18262** (prior-capture, tag face, status draft): Face: D24. Like the dead; Hits / verses: 12 / 12; What differs: The living likened to the dead; the heart that died; "dead dog"; Example verses: Psa 88:5; 143:3; 1Sa 25:37; 2Sa 9:8; Rom 4:19
  - applies to 4 occurrence(s): 2Sa 9:8 (dead), Psa 88:5 (dead), Psa 143:3 (dead), Rom 4:19 (dead)
- **Observation 18264** (prior-capture, tag face, status draft): Face: D26. Uncleanness from the dead; Hits / verses: 13 / 11; What differs: Touching the dead (law); Example verses: Num 19; Lev 21:11; Eze 44:25
  - applies to 2 occurrence(s): Lev 21:11 (dead), Eze 44:25 (dead)
- **Observation 18267** (prior-capture, tag statement, status draft): "Die" and "death" (H4191, H4194, G0599, G2288) move between: the body's end ("and he died", Gen 5); a sentence passed by people ("shall surely be put to death", Lev 20); a judgement from God (Gen 38:7; 2Sa 6:7); the end of a way taken ("its end is the way to death", Pro 14:12); something that happens inside a living person ("sin came alive and I died", Rom 7:9; "abides in death", 1Jo 3:14; Nabal's heart, 1Sa 25:37); a power that reigns, holds and is destroyed (Rom 5:14; Act 2:24; 1Cor 15:26); a death undergone on purpose ("died to sin", Rom 6:2; "I died to the law", Gal 2:19); a death that belongs to the Lord ("if we die, we die to the Lord", Rom 14:8); What differs is what produces the deat ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Rom 7:9 (alive)
- **Observation 18268** (prior-capture, tag statement, status draft): "Put to death" (H4191 hiphil, G3499) is used of executing a person (Num 35) and of "what is earthly in you" (Col 3:5). The same Greek root gives a body "as good as dead" (Rom 4:19; Heb 11:12). *(R: noted as the range of the word. No verse sets these side by side.)*
  - applies to 2 occurrence(s): Rom 4:19 (dead), Heb 11:12 (dead)
- **Observation 18269** (prior-capture, tag statement, status draft): "Dead" as a measure of worth: "a dead dog such as I" (2Sa 9:8) is said of oneself in lowliness. "this dead dog" (2Sa 16:9) is said of another in contempt.
  - applies to 2 occurrence(s): 2Sa 9:8 (dead), 2Sa 16:9 (dead)
- **Observation 18271** (prior-capture, tag statement, status draft): The dead and praise: "The dead do not praise the Lord" (Psa 115:17) and "Blessed are the dead who die in the Lord" (Rev 14:13) stand in different books and settings. The narrative is to set them side by side without reconciling them (LD-46, LD-47).
  - applies to 1 occurrence(s): Psa 115:17 (dead)
- **Observation 18272** (prior-capture, tag statement, status draft): Q1 What is death? (OT-02, main source.) The verses give: the common lot: "We must all die; we are like water spilled on the ground" (2Sa 14:14); "it is appointed for man to die once, and after that comes judgment" (Heb 9:27); its entry through sin: "death through sin, and so death spread to all men because all sinned" (Rom 5:12); "the wages of sin is death" (Rom 6:23); the warning and its denial: "you shall surely die" (Gen 2:17); "You will not surely die" (Gen 3:4); sleep: "not dead but sleeping" (Mat 9:24); a power that holds and is overthrown: "not possible for him to be held by it" (Act 2:24); "the last enemy to be destroyed is death" (1Cor 15:26); death in the living: "Whoever does not ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Ecc 9:5 (dead), Mat 9:24 (dead)
- **Observation 18273** (prior-capture, tag statement, status draft): Q2 Spirit and soul at death (OT-03, touched): "he poured out his soul to death" (Isa 53:12); "My soul is very sorrowful, even to death" (Mat 26:38); "carried by the angels" (Luk 16:22), with no inner word named; "to die is gain" (Phili 1:21); against these, "the dead know nothing" (Ecc 9:5) and "the dead do not praise" (Psa 115:17); These name no destination for spirit or soul. The focused pull for Q2 is still needed.
  - applies to 2 occurrence(s): Psa 115:17 (dead), Ecc 9:5 (dead)
- **Observation 18274** (prior-capture, tag statement, status draft): Q3 The heart after death (OT-04, touched): The heart *before* death: "My heart is in anguish within me; the terrors of death have fallen upon me" (Psa 55:4); "my heart is wrung within me … in the house it is like death" (Lam 1:20); "breaking my heart" (Act 21:13).; The heart in the living, before going to the dead: "madness is in their hearts while they live, and after that they go to the dead" (Ecc 9:3).; Unit 2 has no verse on the heart after death. The focused pull is still needed.
  - applies to 2 occurrence(s): Ecc 9:3 (live), Ecc 9:3 (dead)
- **Observation 18277** (prior-capture, tag face, status draft): Face: L01. The oath by the LORD's life, or a person's; Hits / verses: 61 / 51; What differs: "As the Lord lives"; "as your soul lives"; "as you yourself live"; "by the life of Pharaoh"; Example verses: 1Sa 20:3; 2Ki 2:2; 2Sa 12:5; Jer 4:2; Jer 5:2
  - applies to 6 occurrence(s): 1Sa 20:3 (lives), 2Sa 12:5 (lives), 2Ki 2:2 (lives), 2Ki 2:2 (live), Jer 4:2 (lives), Jer 5:2 (lives)
- **Observation 18278** (prior-capture, tag face, status draft): Face: L02. God swears by his own life; Hits / verses: 24 / 24; What differs: "As I live, declares the Lord God" (16 of the 24 in Ezekiel); Example verses: Eze 33:11; Num 14:21; Deu 32:40; Rom 14:11
  - applies to 4 occurrence(s): Num 14:21 (live), Deu 32:40 (live), Eze 33:11 (live), Rom 14:11 (live)
- **Observation 18279** (prior-capture, tag face, status draft): Face: L03. The living God; Hits / verses: 34 / 34; What differs: Title, praise, against idols; "him who lives forever"; Example verses: Jer 10:10; Psa 42:2; 1Th 1:9; Heb 3:12; Job 19:25
  - applies to 5 occurrence(s): Job 19:25 (lives), Psa 42:2 (living), Jer 10:10 (living), 1Th 1:9 (living), Heb 3:12 (living)
- **Observation 18280** (prior-capture, tag face, status draft): Face: L05. Still alive; alive or dead; Hits / verses: 37 / 32; What differs: Narrative: kin asked after, children, captives; Example verses: Gen 45:26–28; 1Ki 3:22–27; 2Sa 12:18–22
  - applies to 11 occurrence(s): Gen 45:26 (alive), Gen 45:28 (alive), 2Sa 12:18 (dead), 2Sa 12:18 (alive), 2Sa 12:19 (dead), 2Sa 12:21 (alive), 2Sa 12:22 (alive), 1Ki 3:22 (dead), 1Ki 3:23 (alive), 1Ki 3:23 (dead), 1Ki 3:26 (alive)
- **Observation 18281** (prior-capture, tag face, status draft): Face: L06. Living creatures; Hits / verses: 20 / 20; What differs: Creation, flood, covenant, food laws; Example verses: Gen 1:20–30; Gen 9:10–16; Lev 11:46
  - applies to 7 occurrence(s): Gen 1:20 (living), Gen 1:21 (living), Gen 1:24 (living), Gen 1:28 (living), Gen 9:10 (living), Gen 9:16 (living), Lev 11:46 (living)
- **Observation 18283** (prior-capture, tag face, status draft): Face: L08. Lifespan notices; Hits / verses: 24 / 23; What differs: "the years of the life of"; "as long as he lived"; Example verses: Gen 23:1; Gen 25:7; 2Ki 25:29–30
  - applies to 2 occurrence(s): Gen 23:1 (lived), 2Ki 25:30 (lived)
- **Observation 18285** (prior-capture, tag face, status draft): Face: L10. The days lived as the span of fearing and remembering; Hits / verses: 14 / 14; What differs: "all the days that they live"; "all the days of your life"; Example verses: Deu 4:9–10; Deu 16:3; Deu 17:19; Jos 24:31
  - applies to 1 occurrence(s): Deu 4:10 (live)
- **Observation 18288** (prior-capture, tag face, status draft): Face: L13. Life by doing; Hits / verses: 12 / 12; What differs: "statutes of life"; "do this, and you will live"; "what shall I do to inherit eternal life?"; Example verses: Eze 33:15; Luk 10:25–28; Gal 3:12; Rom 7:10
  - applies to 3 occurrence(s): Eze 33:15 (live), Luk 10:28 (live), Gal 3:12 (live)
- **Observation 18289** (prior-capture, tag face, status draft): Face: L14. Life weighed from within; Hits / verses: 34 / 28; What differs: Loathed, bitter, in doubt, a breath, a mist; the living weighed; Example verses: Job 10:1; Psa 88:3; Deu 28:66; Jam 4:14; Ecc 9:3–5
  - applies to 2 occurrence(s): Ecc 9:4 (living), Ecc 9:5 (living)
- **Observation 18292** (prior-capture, tag face, status draft): Face: L17. As long as I live; Hits / verses: 8 / 7; What differs: Praise and dwelling in his house for the length of a life; Example verses: Psa 146:2; Psa 27:4; Isa 38:19–20
  - applies to 1 occurrence(s): Psa 146:2 (live)
- **Observation 18293** (prior-capture, tag face, status draft): Face: L18. The land, book and bundle of the living; Hits / verses: 22 / 22; What differs: The world of the living, and being cut off from it; Example verses: Psa 27:13; Psa 142:5; Psa 69:28; 1Sa 25:29; Eze 32
  - applies to 4 occurrence(s): 1Sa 25:29 (living), Psa 27:13 (living), Psa 69:28 (living), Psa 142:5 (living)
- **Observation 18294** (prior-capture, tag face, status draft): Face: L19. Gone down alive; Hits / verses: 6 / 6; What differs: Sheol (or the lake of fire) taking the living; Example verses: Num 16:30, 33; Psa 55:15; Rev 19:20
  - applies to 4 occurrence(s): Num 16:30 (alive), Num 16:33 (alive), Psa 55:15 (alive), Rev 19:20 (alive)
- **Observation 18295** (prior-capture, tag face, status draft): Face: L20. Living water; Hits / verses: 13 / 13; What differs: Fountain, spring, river; thirst; Example verses: Jer 2:13; Joh 4:10–14; Joh 7:38; Rev 22:17
  - applies to 4 occurrence(s): Jer 2:13 (living), Joh 4:10 (living), Joh 4:11 (living), Joh 7:38 (living)
- **Observation 18298** (prior-capture, tag face, status draft): Face: L23. Living to God; Hits / verses: 38 / 30; What differs: Christ lives in me; dead to sin, alive to God; live by faith; "all live to him"; Example verses: Gal 2:19–20; Rom 6:11; Rom 14:7–8; Luk 20:38
  - applies to 8 occurrence(s): Luk 20:38 (living), Luk 20:38 (live), Rom 6:11 (alive), Rom 14:7 (lives), Rom 14:8 (live), Gal 2:19 (live), Gal 2:20 (live), Gal 2:20 (lives)
- **Observation 18300** (prior-capture, tag face, status draft): Face: L25. From death to life; alive yet dead; Hits / verses: 17 / 15; What differs: Passed from death to life; a name for being alive; Example verses: Joh 5:24–25; Rev 3:1; 1Ti 5:6; Eph 4:18
  - applies to 1 occurrence(s): Rev 3:1 (alive)
- **Observation 18301** (prior-capture, tag face, status draft): Face: L26. Entering life; the tree, crown and book of life; the living and the dead judged; Hits / verses: 34 / 33; What differs: What is entered, received, written, judged; Example verses: Mat 7:14; Jam 1:12; Rev 2:7; Rev 20:12; Act 10:42
  - applies to 1 occurrence(s): Act 10:42 (living)
- **Observation 18302** (prior-capture, tag face, status draft): Face: L27. The living word, hope, stones, way; Hits / verses: 11 / 11; What differs: "living and active"; "a living hope"; Example verses: Heb 4:12; 1Pe 1:3; 1Pe 2:5; Phili 2:16
  - applies to 3 occurrence(s): Heb 4:12 (living), 1Pe 1:3 (living), 1Pe 2:5 (living)
- **Observation 18304** (prior-capture, tag face, status draft): Face: L29. Life threatened or taken by people; Hits / verses: 9 / 9; What differs: "he should not be allowed to live"; Example verses: Act 22:22; Jer 11:19; Isa 53:8
  - applies to 1 occurrence(s): Act 22:22 (live)
- **Observation 18305** (prior-capture, tag face, status draft): Face: L30. Healed or raised; Hits / verses: 9 / 9; What differs: "your son will live" (unit 1 territory); Example verses: Joh 4:50–53; 1Ki 17:23; Act 9:41
  - applies to 2 occurrence(s): Joh 4:50 (live), Joh 4:53 (live)
- **Observation 18307** (prior-capture, tag face, status draft): Face: L32. Living as a manner of conduct; Hits / verses: 2 / 2; What differs: "live like a Gentile"; "lived as a Pharisee"; Example verses: Gal 2:14; Act 26:5
  - applies to 2 occurrence(s): Act 26:5 (lived), Gal 2:14 (live)
- **Observation 18310** (prior-capture, tag statement, status draft): "As the LORD lives." The same oath carries loyalty (Elisha, Ittai, Uriah), anger (David, 2Sa 12:5), a rash vow that the people overturn (Saul, 1Sa 14:39, 45), greed (Gehazi), an oath to a medium (Saul) and a secret promise (Zedekiah). The words do not change; the one swearing and what is sworn to do does. The verses give their own measure: "in truth, in justice, and in righteousness" (Jer 4:2), against "yet they swear falsely" (Jer 5:2).
  - applies to 5 occurrence(s): 1Sa 14:39 (lives), 1Sa 14:45 (lives), 2Sa 12:5 (lives), Jer 4:2 (lives), Jer 5:2 (lives)
- **Observation 18312** (prior-capture, tag statement, status draft): "Alive." A fact in a narrative ("Is your father still alive?"); a reputation that is false ("You have the reputation of being alive, but you are dead"); a standing toward God ("alive to God in Christ Jesus"); a state before the law came ("I was once alive apart from the law", Rom 7:9).
  - applies to 1 occurrence(s): Rom 7:9 (alive)
- **Observation 18313** (prior-capture, tag statement, status draft): "Living." Each verse states what "living" is set against: idols (1Th 1:9), broken cisterns (Jer 2:13), dead works (Heb 9:14), the dead (Luk 20:38). Quoted, not drawn together.
  - applies to 4 occurrence(s): Jer 2:13 (living), Luk 20:38 (living), 1Th 1:9 (living), Heb 9:14 (living)
- **Observation 18314** (prior-capture, tag statement, status draft): Q1 What is death? | It is stated from the life side: "For the living know that they will die" (Ecc 9:5). A person can be called dead while alive: "dead even while she lives" (1Ti 5:6), "alienated from the life of God" (Eph 4:18). | LD-114, LD-128
  - applies to 3 occurrence(s): Ecc 9:5 (living), Ecc 9:5 (dead), 1Ti 5:6 (lives)
- **Observation 18315** (prior-capture, tag statement, status draft): Q2 Spirit and soul at death | "for all live to him" (Luk 20:38); "that … they might live in the spirit the way God does" (1Pe 4:6); "I saw the souls of those who had been beheaded … They came to life" (Rev 20:4); while living, "in all these is the life of my spirit" (Isa 38:16). These are set beside the unit 2 verses, unreconciled. The focused pull is still needed. | LD-126, LD-127, LD-132, LD-117
  - applies to 4 occurrence(s): Isa 38:16 (live), Luk 20:38 (living), Luk 20:38 (live), 1Pe 4:6 (live)
- **Observation 18316** (prior-capture, tag statement, status draft): Q3 The heart after death | No verse in this unit. The heart while living: "madness is in their hearts while they live" (Ecc 9:3); "an evil, unbelieving heart" (Heb 3:12). Joh 7:38 is *koilia*, not the heart word. | LD-114, LD-98
  - applies to 3 occurrence(s): Ecc 9:3 (live), Joh 7:38 (living), Heb 3:12 (living)
- **Observation 18317** (prior-capture, tag statement, status draft): Q4 The body | "so that what is mortal may be swallowed up by life" (2Cor 5:4, already in Ch 2); "so that the life of Jesus also may be manifested in our bodies" (2Cor 4:10, already in Ch 2); "present your bodies as a living sacrifice" (Rom 12:1); "although the body is dead because of sin, the Spirit is life because of righteousness" (Rom 8:10). | LD-125, LD-127
  - applies to 1 occurrence(s): Rom 12:1 (living)
- **Observation 18346** (prior-capture, tag statement, status draft): Data: life-death-unit4-supplement-h6974-pull-v1-20261004.csv (H6974, 22 hits in 21 verses, from iba.db; tagged T3, not M25). Faces from life-death-unit4-supplement-face-assign-v1-20261004.py; every hit has one. Five verses carry both words and were already read (Job 14:12; Hab 2:19; Psa 35:23; 44:23; 73:20). New faces: W18 The dead waking (3) · W19 The child not awakened (1) · W20 A perpetual sleep (2) · W21 Waking kept by God (2) · W22 The end awakened (1) · W23 Waking in the inner being (5, to #1942) · W17 data (2: 1Sa 26:12, a deep sleep from the Lord; Jer 31:26). W06 gains Psa 59:5. Context read: 2Ki 4:32–35; Psa 3:1–6; 73:17–20; 139:17–18; Jer 51:38–40; Dan 12:1–3; Isa 26:14.: Unit 5, i ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): 2Ki 4:32 (dead), Isa 26:14 (dead)
- **Observation 18354** (prior-capture, tag face, status draft): Face: S08 The soul as a dead body; Hits: 6; Example: Num 19:11, 13; Lev 21:11
  - applies to 3 occurrence(s): Lev 21:11 (dead), Num 19:11 (dead), Num 19:13 (dead)
- **Observation 18361** (prior-capture, tag face, status draft): Face: H04 The heart while living, then the dead; Hits: 2; Example: Ecc 9:3
  - applies to 1 occurrence(s): Ecc 9:3 (dead)
- **Observation 18372** (prior-capture, tag statement, status draft): Q2 (soul and spirit at death). The verses give the soul more than one face at death. It departs (Gen 35:18). It dies (Num 23:10; Eze 18:4). It is poured out to death (Isa 53:12). It goes to the generation of its fathers (Psa 49:19). It is ransomed from Sheol's power, "for he will receive me" (Psa 49:15). It is not abandoned to Sheol, which Peter reads of Christ (Act 2:27, 31). Of the spirit, they say it is committed, taken, or returns to God (Luk 23:46; Psa 104:29; Ecc 12:7); "who knows" where it goes (Ecc 3:21); and the dead "live in the spirit the way God does" (1Pe 4:6). No verse sends the soul one way and the spirit another. These are set side by side, unreconciled.
  - applies to 1 occurrence(s): 1Pe 4:6 (live)
- **Observation 18373** (prior-capture, tag statement, status draft): Q3 (the heart after death). No verse found. Scripture names the heart "while they live" (Ecc 9:3), and stops there.
  - applies to 1 occurrence(s): Ecc 9:3 (live)
- **Observation 18391** (prior-capture, tag statement, status draft): Already now, in the inner being. "born again to a living hope through the resurrection of Jesus Christ" (1Pe 1:3); "that I may know him and the power of his resurrection" (Php 3:10); the mind "transformed" (Rom 12:2); "being transformed … from one degree of glory to another" (2Cor 3:18).
  - applies to 1 occurrence(s): 1Pe 1:3 (living)
- **Observation 18411** (prior-capture, tag statement, status draft): "the land of the living" | 14: Psa 27:13; 116:9; Eze 32 … | where life is lived before God
  - applies to 1 occurrence(s): Psa 27:13 (living)
- **Observation 18414** (prior-capture, tag statement, status draft): "In him we live and move and have our being"; "he himself gives to all mankind life and breath and everything" | Act 17:28, 25 | life and breath as given by God, in him
  - applies to 1 occurrence(s): Act 17:28 (live)
- **Observation 18439** (prior-capture, tag statement, status draft): The living God, and the inner being turned toward him or away | LD-97–LD-100 | Ch 2 "Living before God"; 10.9 "The living God" | Ch 4 (Heb 3:12); 10.1 (Heb 10:31); 10.6 (Psa 42:2) | carried (unit 3)
  - applies to 3 occurrence(s): Psa 42:2 (living), Heb 3:12 (living), Heb 10:31 (living)
- **Observation 18444** (prior-capture, tag statement, status draft): Life weighed: loathed, worn down, the living weighed, enjoyed, what life does not consist in | LD-111, LD-112, LD-114–LD-116 | Ch 2 "Life weighed" | 10.1; 10.3; 10.6; Ch 12 (Ecc 9:3; Psa 143:2); Ch 13 (Deu 28:66) | carried (unit 3)
  - applies to 1 occurrence(s): Psa 143:2 (living)
- **Observation 18446** (prior-capture, tag statement, status draft): One's own life spoken of to God; praise as long as I live; the life of the poor | LD-117, LD-118, LD-142 | 10.9 "The living God" | Ch 2 "Life asked for" (Psa 74:19); Ch 6 (Job 10:12; Isa 38:16) | carried (unit 3)
  - applies to 1 occurrence(s): Isa 38:16 (live)
- **Observation 18450** (prior-capture, tag statement, status draft): Inner words in narrative "alive" verses | LD-135 | 10.1 (1Ki 3:26) | 10.10 (2Sa 1:23) | carried (unit 3)
  - applies to 1 occurrence(s): 1Ki 3:26 (alive)
- **Observation 18468** (prior-capture, tag statement, status draft): C-83 Death comes to everyone: Num 16:29 ("die as all men die … the fate of all mankind"); Job 30:23 ("the house appointed for all living"); Psa 82:7 ("like men you shall die"); Isa 51:6
  - applies to 1 occurrence(s): Job 30:23 (living)
- **Observation 18472** (prior-capture, tag statement, status draft): C-88 Death in the living: Rom 7:13 ("sin, producing death in me through what is good"); Hos 13:1 ("he incurred guilt through Baal and died"); Jude 12 ("twice dead"); Lam 3:6; Luk 1:79 ("the shadow of death")
  - applies to 2 occurrence(s): Lam 3:6 (dead), Jude 12 (dead)
- **Observation 18475** (prior-capture, tag statement, status draft): C-106 The dead do not praise: Psa 88:10 ("Do the departed rise up to praise you?")
  - applies to 1 occurrence(s): Psa 88:10 (dead)
- **Observation 18477** (prior-capture, tag statement, status draft): B1.4 | Living before God | "'As the Lord lives' is its commonest form, and often a second life is joined to it" | Counted: "As the Lord lives" 39 verses, "As God lives" 2, so "commonest" holds. A second life is joined in 6 of the 39 (1Sa 20:3; 25:26; 2Ki 2:2, 4, 6; 4:30). "Often" does not hold. | "… is its commonest form (39 verses). In six of them a second life is joined to it …"
  - applies to 6 occurrence(s): 1Sa 20:3 (lives), 1Sa 25:26 (lives), 2Ki 2:2 (lives), 2Ki 2:4 (lives), 2Ki 2:6 (lives), 2Ki 4:30 (lives)
- **Observation 18485** (prior-capture, tag statement, status draft): R3 | Breath lent | God holds both ends, killing and making alive, and keeps alive between them | Deu 32:39; 1Sa 2:6; 2Ki 5:7; Psa 33:19; Job 36:6; Gen 50:20; Deu 6:24
  - applies to 6 occurrence(s): Gen 50:20 (alive), Deu 6:24 (alive), Deu 32:39 (alive), 2Ki 5:7 (alive), Job 36:6 (alive), Psa 33:19 (alive)
- **Observation 18495** (prior-capture, tag statement, status draft): R13 | Living before God | *I read*: the oath "As the Lord lives" places a promise before the living God and binds the speaker to it by life | 1Sa 20:3; 2Ki 2:2; 2Sa 15:21; 1Ki 1:29; 17:1; Job 27:2
  - applies to 6 occurrence(s): 1Sa 20:3 (lives), 2Sa 15:21 (lives), 1Ki 1:29 (lives), 1Ki 17:1 (lives), 2Ki 2:2 (lives), Job 27:2 (lives)
- **Observation 18498** (prior-capture, tag statement, status draft): R16 | Living before God | "The living God" sets him against idols, which have no breath | Jer 10:10; 1Th 1:9; Hab 2:18–20
  - applies to 2 occurrence(s): Jer 10:10 (living), 1Th 1:9 (living)
- **Observation 18500** (prior-capture, tag statement, status draft): R18 | Living before God | The world where life is lived is named "the land of the living" | Psa 27:13; 142:5; Isa 38:11; 1Sa 25:29
  - applies to 4 occurrence(s): 1Sa 25:29 (living), Psa 27:13 (living), Psa 142:5 (living), Isa 38:11 (living)
- **Observation 18509** (prior-capture, tag statement, status draft): R29 | Made alive | That death changes how the living live: no longer for themselves, dead to sin, Christ living in them | 2Co 5:15; Rom 6:2; Col 3:5; Gal 2:19–20; Rom 12:1; 1Pe 2:24
  - applies to 6 occurrence(s): Rom 6:2 (live), Rom 12:1 (living), 2Cor 5:15 (live), Gal 2:19 (live), Gal 2:20 (live), 1Pe 2:24 (live)
- **Observation 18510** (prior-capture, tag statement, status draft): R30 | Dying to the Lord | A death, too, can belong to the Lord, and a dying can go on while a person lives | Rom 14:7–8; Phi 1:20–21; 1Co 15:31; 2Co 4:11; 6:9
  - applies to 1 occurrence(s): Rom 14:7 (lives)
- **Observation 18517** (prior-capture, tag statement, status draft): C4 | Death accepted once what was waited for is seen. Simeon "would not see death before he had seen the Lord's Christ", then: "now you are letting your servant depart in peace". Jacob: "It is enough; Joseph my son is still alive. I will go and see him before I die." | Luk 2:26, 29; Gen 45:28 (with 46:30, cited) | Ch 2 *Dying to the Lord*; also answers B1.5
  - applies to 1 occurrence(s): Gen 45:28 (alive)
- **Observation 18518** (prior-capture, tag statement, status draft): C5 | Ready to die for or with another, and readiness that fails. Jonathan: "Here I am; I will die." Peter: "ready to go with you both to prison and to death", answered "you will deny three times that you know me" (22:34). Thomas: "that we may die with him". "Be faithful unto death"; "they loved not their lives even unto death". | 1Sa 14:43; Jos 2:14; Judg 5:18; Luk 22:33–34; Joh 11:16; 1Co 9:15; Phi 2:30; Rev 2:10; 12:11 | Ch 2 *Dying to the Lord* (beside Ruth); 10.10 *Loyalty and honour*
  - applies to 2 occurrence(s): Judg 5:18 (lives), Rev 12:11 (lives)
- **Observation 18520** (prior-capture, tag statement, status draft): C7 | Those left behind. Hagar: "Let me not look on the death of the child", and she wept. David fasted while the child lived and ate when he died, and his servants ask why (2Sa 12:21); 12:23, already cited in *After death*, is his answer. Joab rebukes David's grief for Absalom (2Sa 19:6). Paul: God had mercy on Epaphroditus "lest I should have sorrow upon sorrow". "You shall not cut yourselves … for the dead." No comfort for the mourner under judgment. | Gen 21:16; 2Sa 12:19–21; 19:6; Phi 2:27; Deu 14:1; Jer 16:7; Gen 44:22 | New short Ch 2 section, *Those left behind*, pointing to 10.1 for grief. Ch 2 has no place for death as the living meet it in another.
  - applies to 4 occurrence(s): Deu 14:1 (dead), 2Sa 12:19 (dead), 2Sa 19:6 (dead), Jer 16:7 (dead)
- **Observation 18521** (prior-capture, tag statement, status draft): C8 | The fear of dying shapes acts. Judah withholds Shelah "for he feared that he would die, like his brothers". Lot cannot flee to the hills "lest the disaster overtake me and I die". Agag comes "cheerfully": "Surely the bitterness of death is past". The Egyptians: "We shall all be dead." | Gen 38:11; Gen 19:19; 1Sa 15:32; Exo 12:33; 1Sa 5:11; 12:19 | Ch 2 *Facing death* (beside Gen 26:9)
  - applies to 1 occurrence(s): Exo 12:33 (dead)
- **Observation 18530** (prior-capture, tag statement, status draft): C17 | Christ's death as his own act. "he humbled himself by becoming obedient to the point of death"; "the love of Christ controls us … one has died for all, therefore all have died"; "the death he died he died to sin, once for all, but the life he lives he lives to God". | Phi 2:8; 2Co 5:14; Rom 6:9–10; 5:6; 8:34; Gal 2:21; Heb 9:15 | Ch 2 *Made alive*
  - applies to 1 occurrence(s): Rom 6:10 (lives)
- **Observation 18531** (prior-capture, tag statement, status draft): C18 | Baptized into his death. | Rom 6:3, 5, 8; Col 2:20 | Ch 2 *Made alive* (beside Rom 6:2, 4)
  - applies to 1 occurrence(s): Col 2:20 (alive)
- **Observation 18532** (prior-capture, tag statement, status draft): C19 | The living and the dead. Inquiring of the dead and offering to them are forbidden; kindness to the dead is blessed (Naomi). | Deu 18:11; 26:14; Psa 106:28; Rut 1:8 | Ch 2 *After death*
  - applies to 4 occurrence(s): Deu 18:11 (dead), Deu 26:14 (dead), Rut 1:8 (dead), Psa 106:28 (dead)
- **Observation 18533** (prior-capture, tag statement, status draft): C20 | A death that glorifies God; death as "yours". "by what kind of death he was to glorify God"; "Christ died and lived again, that he might be Lord both of the dead and of the living"; "life or death … all are yours"; "death is at work in us, but life in you"; Zedekiah, "You shall die in peace". | Joh 21:19; Rom 14:9; 1Co 3:22; 2Co 4:12; Jer 34:5 | Ch 2 *Dying to the Lord*
  - applies to 2 occurrence(s): Rom 14:9 (lived), Rom 14:9 (living)
- **Observation 18542** (prior-capture, tag statement, status draft): G2. Death in the living. People still alive are called dead: "you were dead in the trespasses and sins" (Eph 2:1; also 2:5; Col 2:13); "she who is self-indulgent is dead even while she lives" (1Ti 5:6); "You have the reputation of being alive, but you are dead" (Rev 3:1); "this my son was dead, and is alive again; he was lost, and is found" (Luk 15:24, 32); "leave the dead to bury their own dead" (Mat 8:22; Luk 9:60); "an hour is coming, and is now here, when the dead will hear the voice of the Son of God, and those who hear will live" (Joh 5:25); "Awake, O sleeper, and arise from the dead" (Eph 5:14), said to believers; Within, the hypocrites are "full of dead people's bones" (Mat 23:27); T ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Luk 15:32 (alive), Joh 5:25 (live), 1Ti 5:6 (lives), Rev 3:1 (alive)
- **Observation 18543** (prior-capture, tag statement, status draft): G3. Dying to. A death the verses count as already died, with a release in it. The relationship carried in it is "to": "How can we who died to sin still live in it?" (Rom 6:2); "consider yourselves dead to sin and alive to God" (6:11); "you also have died to the law through the body of Christ, so that you may belong to another … in order that we may bear fruit for God" (Rom 7:4); "If with Christ you died to the elemental spirits of the world" (Col 2:20); "If we have died with him, we will also live with him" (2Ti 2:11); Beside it stands a putting to death still to be done: "if by the Spirit you put to death the deeds of the body, you will live" (Rom 8:13); "Put to death therefore what is eart ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Rom 6:2 (live), Rom 6:11 (alive), Rom 8:13 (live)
- **Observation 18546** (prior-capture, tag statement, status draft): G6. Like the dead.: The guards "became like dead men" for fear (Mat 28:4).; John "fell at his feet as though dead" (Rev 1:17).; Abraham's body "as good as dead" (Rom 4:19).
  - applies to 1 occurrence(s): Rom 4:19 (dead)
- **Observation 18551** (prior-capture, tag statement, status draft): Sin can be dead too. "apart from the law, sin lies dead" (Rom 7:8). Then: "when the commandment came, sin came alive and I died" (7:9). Here the word passes between sin and the person.
  - applies to 1 occurrence(s): Rom 7:9 (alive)
- **Observation 18560** (prior-capture, tag statement, status draft): | works that look alive | Rev 3:1
  - applies to 1 occurrence(s): Rev 3:1 (alive)
- **Observation 18580** (prior-capture, tag statement, status draft): Which death a verse means, where it does not say. Several verses the narrative cites under *Death and sin* set death against life without saying which death: "the wages of sin is death, but the free gift of God is eternal life" (Rom 6:23); "sin when it is fully grown brings forth death" (Jam 1:15); "if you live according to the flesh you will die" (Rom 8:13); "the soul who sins shall die" (Eze 18:4); The narrative should not decide it for them. Where the opposite is "eternal life" (Rom 6:23), the verse sets the death against more than the body's life. That is *I read*.
  - applies to 1 occurrence(s): Rom 8:13 (live)
- **Observation 18590** (prior-capture, tag statement, status draft): Mat 22:32; Mar 12:27; Luk 20:38: "not God of the dead, but of the living" | Luk 20:38 is cited in *After death*; the parallels are sources for C-110 | —
  - applies to 3 occurrence(s): Mat 22:32 (living), Mar 12:27 (living), Luk 20:38 (living)
- **Observation 18603** (prior-capture, tag statement, status draft): N9 | Sleep and waking | The waking of the dead is not the same for all | Dan 12:2; Isa 26:14, 19 |
  - applies to 2 occurrence(s): Isa 26:14 (dead), Isa 26:19 (dead)
- **Observation 18612** (prior-capture, tag statement, status draft): N20 | After death | From this side of death, the dead are silent and gone | Job 14:10; Ecc 9:5; Psa 6:5; 115:17; 49:19 |
  - applies to 2 occurrence(s): Psa 115:17 (dead), Ecc 9:5 (dead)
- **Observation 18613** (prior-capture, tag statement, status draft): N21 | After death | With God, the dead are carried, blessed and at rest | Luk 16:22; Rev 14:13; 2Sa 12:23; Luk 20:38; 23:43; Php 1:23; 2Co 5:8 |
  - applies to 1 occurrence(s): 2Sa 12:23 (dead)
- **Observation 18614** (prior-capture, tag statement, status draft): On who goes down, and how: Jacob: "I shall go down to Sheol to my son, mourning" (Gen 37:35; also 42:38; 44:29, 31); "The wicked shall return to Sheol" (Psa 9:17); "Sheol … those who have sinned" (Job 24:19); 1Ki 2:6, 9; Hezekiah: "I am consigned to the gates of Sheol for the rest of my years" (Isa 38:10); Job 17:13, 16 (Sheol as house and bed); Psa 141:7; Pro 5:5; 7:27; Pro 15:24; Num 16:33; Psa 55:15; Pro 1:12 (down alive); Psa 31:17 ("go silently to Sheol"); Nations and kings brought down: Isa 14:15; Eze 31:15–17; Mat 11:23; Luk 10:15
  - applies to 3 occurrence(s): Num 16:33 (alive), Psa 55:15 (alive), Pro 1:12 (alive)
- **Observation 18627** (prior-capture, tag statement, status draft): Psa 89:48 | live; soul | What man can live and never see death? Who can deliver his soul from the power of Sheol? Selah
  - applies to 1 occurrence(s): Psa 89:48 (live)
- **Observation 18631** (prior-capture, tag statement, status draft): Rev 1:18 | living; alive | and the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades.
  - applies to 2 occurrence(s): Rev 1:18 (living), Rev 1:18 (alive)
- **Observation 18633** (prior-capture, tag statement, status draft): Num 16:30 | alive | … and they go down alive into Sheol, then you shall know that these men have despised the Lord.
  - applies to 1 occurrence(s): Num 16:30 (alive)
- **Observation 18634** (prior-capture, tag statement, status draft): Num 16:33 | alive | So they and all that belonged to them went down alive into Sheol, and the earth closed over them …
  - applies to 1 occurrence(s): Num 16:33 (alive)
- **Observation 18635** (prior-capture, tag statement, status draft): Psa 55:15 | alive | Let death steal over them; let them go down to Sheol alive; for evil is in their dwelling place and in their heart.
  - applies to 1 occurrence(s): Psa 55:15 (alive)
- **Observation 18636** (prior-capture, tag statement, status draft): Pro 1:12 | alive | like Sheol let us swallow them alive, and whole, like those who go down to the pit;
  - applies to 1 occurrence(s): Pro 1:12 (alive)
- **Observation 18637** (prior-capture, tag statement, status draft): Eze 32:27 | living | … for the terror of the mighty men was in the land of the living.
  - applies to 1 occurrence(s): Eze 32:27 (living)
- **Observation 18645** (prior-capture, tag statement, status draft): a2 | "The resurrection reaches the inner being before it reaches the body" (on 1Pe 1:3) | 1Pe 1:3 says "born again to a living hope through the resurrection"; it says nothing of "before" | Restate on the verses that say it (see c2), or mark "I read" and register
  - applies to 1 occurrence(s): 1Pe 1:3 (living)
- **Observation 18653** (prior-capture, tag statement, status draft): c1. The inner acts toward the resurrection: 34 verses (A1). This is the largest group.: *Denied*, and the ground Jesus gives: "the Sadducees say that there is no resurrection, nor angel, nor spirit" (Act 23:8); Jesus' answer: "You are wrong, because you know neither the Scriptures nor the power of God"; (Mat 22:29; Mar 12:24). He grounds it in God's name: "the God of Abraham" (Mar 12:26), "for; all live to him" (Luk 20:38); The section cites only Mat 22:30 and Luk 20:36, on marriage.; *Questioned, and not understood until later:*; "questioning what this rising from the dead might mean" (Mar 9:10); "as yet they did not understand the Scripture, that he must rise from the dead" (Joh 20:9); "Wh ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Luk 20:38 (live)
- **Observation 18709** (prior-capture, tag statement, status draft): H2416A with the divine party in 98 verses. Its commonest near pair is "alive + LORD" (64), e.g. 1Ki 17:1, 17:12, 18:10. This points to the oath "as the LORD lives". It is a pointer only; reading would confirm it.
  - applies to 3 occurrence(s): 1Ki 17:1 (lives), 1Ki 17:12 (lives), 1Ki 18:10 (lives)
- **Observation 18710** (prior-capture, tag statement, status draft): M47 Inner Seat | 302 | 188 | alive + flesh 13; alive + soul (living creature) 12 (Gen 1:20–21, Eze 47:9); live + soul 11 (1Co 15:45, Eze 13:18–19)
  - applies to 8 occurrence(s): Gen 1:20 (living), Gen 1:21 (living), Eze 13:18 (alive), Eze 13:19 (alive), Eze 13:19 (live), Eze 47:9 (living), Eze 47:9 (live), 1Cor 15:45 (living)
- **Observation 18712** (prior-capture, tag statement, status draft): M12 Righteousness | 114 | 76 | live + righteousness / justice / righteous (Eze 18, Eze 33, Deu 16:20, 1Pe 2:24)
  - applies to 2 occurrence(s): Deu 16:20 (live), 1Pe 2:24 (live)
- **Observation 18720** (prior-capture, tag statement, status draft): M11 Turning & Repentance | 44 | 14 | live + turn (Eze 18:23, 18:32, 33:11)
  - applies to 3 occurrence(s): Eze 18:23 (live), Eze 18:32 (live), Eze 33:11 (live)
- **Observation 18721** (prior-capture, tag statement, status draft): M13 Faith | 43 | 18 | live + faith (Gal 2:20, 3:11, Heb 10:38)
  - applies to 3 occurrence(s): Gal 2:20 (live), Gal 3:11 (live), Heb 10:38 (live)
- **Observation 18723** (prior-capture, tag statement, status draft): M54 Torah & Obedience | 40 | 19 | die / live + law, commandment (Gal 2:19, Pro 4:4, 7:2, Deu 30:16)
  - applies to 4 occurrence(s): Deu 30:16 (live), Pro 4:4 (live), Pro 7:2 (live), Gal 2:19 (live)
- **Observation 18750** (prior-capture, tag statement, status draft): 3A.1 One root, several renderings (selected; the full list is in the data file): deathly [panic]: 1Sa 5:11; deadly: Psa 7:13
  - applies to 1 occurrence(s): Psa 7:13 (deadly)
- **Observation 18751** (prior-capture, tag statement, status draft): Greek: G2227 "make alive" (12): gives life (Joh 5:21, 6:63, 2Co 3:6), made alive (1Co 15:22, 1Pe 3:18), life-giving (1Co 15:45); G4806 "made alive together with": Eph 2:5, Col 2:13; G3499 "put to death": Col 3:5; G0979 *bios*: life / property / goods / "live on" (Mar 12:44, Luk 15:12, 1Jo 3:17)
  - applies to 1 occurrence(s): Mar 12:44 (live on)
- **Observation 18761** (prior-capture, tag statement, status draft): "As the LORD lives" (alive + LORD 64) | 1Ki 17:1, 18:10 … | 10.5 / 10.9
  - applies to 2 occurrence(s): 1Ki 17:1 (lives), 1Ki 18:10 (lives)
- **Observation 18787** (prior-capture, tag face, status draft): Face: A. Living out one's years; Hits / verses: 46 / 46; What differs: Duration: "X lived N years"; Example verses: Gen 5; Gen 11; Job 42:16; Ecc 6:3; 11:8
  - applies to 1 occurrence(s): Job 42:16 (lived)
- **Observation 18788** (prior-capture, tag face, status draft): Face: B. Kept alive by food and support; Hits / verses: 20 / 19; What differs: What keeps life going: grain, oil, a brother's support; Example verses: Gen 42:2; 47:19; Neh 5:2; Lev 25:35–36
  - applies to 1 occurrence(s): Neh 5:2 (alive)
- **Observation 18789** (prior-capture, tag face, status draft): Face: C. Let live, or put to death, by people; Hits / verses: 39 / 38; What differs: A person holds another's life: a king, a midwife, a soldier, a court; Example verses: Exo 1:16–22; Jos 9:20; 1Ki 20:31–32; Est 4:11
  - applies to 7 occurrence(s): Exo 1:16 (live), Exo 1:17 (live), Exo 1:18 (live), Exo 1:22 (live), Jos 9:20 (live), 1Ki 20:32 (live), Est 4:11 (live)
- **Observation 18790** (prior-capture, tag face, status draft): Face: D. God keeps alive; Hits / verses: 15 / 15; What differs: God as the keeper of life, in famine and danger; Example verses: Gen 50:20; Psa 33:19; 41:2; Job 36:6; Psa 22:29
  - applies to 5 occurrence(s): Gen 50:20 (alive), Job 36:6 (alive), Psa 22:29 (alive), Psa 33:19 (alive), Psa 41:2 (alive)
- **Observation 18791** (prior-capture, tag face, status draft): Face: X. God kills and makes alive; Hits / verses: 3 / 3; What differs: Both acts held by God alone; Example verses: Deu 32:39; 1Sa 2:6; 2Ki 5:7
  - applies to 2 occurrence(s): Deu 32:39 (alive), 2Ki 5:7 (alive)
- **Observation 18797** (prior-capture, tag face, status draft): Face: K. Life returned to the dead, or promised; Hits / verses: 19 / 14; What differs: Bodies come back to life; a people raised; Example verses: 1Ki 17:22; 2Ki 13:21; Eze 37; Isa 26:19; Hos 6:2
  - applies to 1 occurrence(s): Isa 26:19 (dead)
- **Observation 18800** (prior-capture, tag face, status draft): Face: N. Asking God for life; Hits / verses: 22 / 22; What differs: "give me life", "revive us", "that the child may live"; Example verses: Psa 119 (×15); Psa 80:18; 85:6; 2Sa 12:22
  - applies to 1 occurrence(s): 2Sa 12:22 (live)
- **Observation 18801** (prior-capture, tag face, status draft): Face: O. Live by doing God's word; Hits / verses: 25 / 24; What differs: Life tied to statutes, justice, wisdom, seeking him, faith; Example verses: Lev 18:5; Deu 8:3; 30:19; Amo 5:4; Hab 2:4
  - applies to 5 occurrence(s): Lev 18:5 (live), Deu 8:3 (live), Deu 30:19 (live), Amo 5:4 (live), Hab 2:4 (live)
- **Observation 18802** (prior-capture, tag face, status draft): Face: P. Turn and live (Ezekiel); Hits / verses: 34 / 23; What differs: Righteous and wicked; turning; false prophets keeping alive; Example verses: Eze 18; 33; 13:18–22
  - applies to 3 occurrence(s): Eze 13:18 (alive), Eze 13:19 (alive), Eze 13:19 (live)
- **Observation 18803** (prior-capture, tag face, status draft): Face: Q. Seeing or hearing God and living; Hits / verses: 10 / 10; What differs: Living through God's presence or voice; looking at the serpent; Example verses: Exo 33:20; Deu 5:24, 26; Num 21:8–9
  - applies to 1 occurrence(s): Deu 5:26 (living)
- **Observation 18804** (prior-capture, tag face, status draft): Face: R. "Long live the king"; Hits / verses: 13 / 12; What differs: Acclamation and blessing; Example verses: 1Ki 1:25–39; Neh 2:3; Deu 33:6
  - applies to 6 occurrence(s): Deu 33:6 (live), 1Ki 1:25 (live), 1Ki 1:31 (live), 1Ki 1:34 (live), 1Ki 1:39 (live), Neh 2:3 (live)
- **Observation 18805** (prior-capture, tag face, status draft): Face: S. Not wanting to live; Hits / verses: 1 / 1; What differs: —; Example verses: Job 7:16
  - applies to 1 occurrence(s): Job 7:16 (live)
- **Observation 18807** (prior-capture, tag face, status draft): Face: V. Live by surrender; Hits / verses: 8 / 6; What differs: The prophet's word: go out to Babylon and live; Example verses: Jer 21:9; 27:12, 17; 38:2, 17, 20
  - applies to 5 occurrence(s): Jer 21:9 (live), Jer 27:12 (live), Jer 27:17 (live), Jer 38:2 (live), Jer 38:17 (live)
- **Observation 18811** (prior-capture, tag statement, status draft): | – the Shunammite's son, "how Elisha had restored the dead to life" | 2Ki 8:5, 1 | | |
  - applies to 1 occurrence(s): 2Ki 8:5 (dead)
- **Observation 18816** (prior-capture, tag statement, status draft): Q1 What is death?; The breath is gone: "Everything … in whose nostrils was the breath of life died" (Gen 7:22); "no breath left in him" (1Ki 17:17).; God holds both ends: "I kill and I make alive" (Deu 32:39).; Scripture also calls the living dead: "dead in your trespasses" (Col 2:13; Eph 2:5).; It is asked whether death ends life: "If a man dies, shall he live again?" (Job 14:14).; Unit 2 (die, death) is the main source.
  - applies to 2 occurrence(s): Deu 32:39 (alive), Job 14:14 (live)
- **Observation 18818** (prior-capture, tag statement, status draft): Q3 The heart after death.; Unit 1 has no verse on the heart after death.; The nearest are the living heart revived (Isa 57:15; Psa 69:32) and the wish "May your hearts live forever!" (Psa 22:26), which is not about death.; A focused pull (heart with die, death or Sheol) is needed before anything is said.
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 18944** (prior-capture, tag statement, status draft): H2778A *ḥārap̄*: the stem changes the direction. Piel 35 hits: taunting, defying and mocking another. Qal 4 hits: Psa 69:9 and Psa 119:42 ("those who reproach you", "him who taunts me"), Pro 27:11 ("him who reproaches me"), and Job 27:6, "my heart does not reproach me". In Job 27:6 the reproach is the heart's own act on the self (told in Ch 8). And Judg 5:18 (Piel) has the people's own soul as the object: "reproached its soul to death", rendered "risked their lives" (batch 1).
  - applies to 1 occurrence(s): Judg 5:18 (lives)
- **Observation 19233** (prior-capture, tag statement, status draft): Where it comes from.; God's own act: "you have hidden these things from the wise and understanding and revealed them to little children" (Mat 11:25), said in thanks; "I will utter what has been hidden since the foundation of the world" (Mat 13:35).; Judgement: "the discernment of their discerning men shall be hidden" (Isa 29:14), on a people who "honor me with their lips, while their hearts are far from me" (29:13). Discernment is hidden from those whose heart is absent from their worship.; The nature of things: "It is hidden from the eyes of all living" (Job 28:21, of wisdom); "he reveals deep and hidden things" (Dan 2:22).; Hidden from oneself: "Who can discern his errors? Declare me innoc ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 28:21 (living)
- **Observation 19343** (prior-capture, tag statement, status draft): Psa 17:8 (SH) | Psa 17:9 "deadly enemies" | the sheltered one's · life-sense | §3 Seat
  - applies to 1 occurrence(s): Psa 17:9 (deadly)
- **Observation 19344** (prior-capture, tag statement, status draft): Psa 22:24 (FH) | Psa 22:26 "May your hearts live forever!" | bearers' own · genuine | §5 Seat
  - applies to 1 occurrence(s): Psa 22:26 (live)
- **Observation 19727** (prior-capture, tag statement, status draft): The Son: from the cloud: "This is my Son, my Chosen One; listen to him!" (Luk 9:35); mocked at the cross: "let him save himself, if he is the Christ of God, his Chosen One!" (Luk 23:35); "a living stone rejected by men but in the sight of God chosen and precious" (1Pe 2:4); "a cornerstone chosen and precious, and whoever believes in him will not be put to shame" (1Pe 2:6); Chosen by God and rejected by men are stated together.
  - applies to 1 occurrence(s): 1Pe 2:4 (living)
- **Observation 19741** (prior-capture, tag statement, status draft): Choosing between death and life: "so that I would choose strangling and death rather than my bones" (Job 7:15; the M47 tag on "I" is *nephesh*); "Death shall be preferred to life by all the remnant" (Jer 8:3); Paul: "If I am to live in the flesh, that means fruitful labor for me. Yet which I shall choose I cannot tell" (Phili 1:22, G0138); All three stand against "choose life" (Deu 30:19). In Job and Jeremiah death is preferred out of suffering. In Philippians the choice is held open, with no answer given.
  - applies to 1 occurrence(s): Phili 1:22 (live)
- **Observation 19769** (prior-capture, tag statement, status draft): Phili 1:22 | flesh | "If I am to live in the flesh … which I shall choose I cannot tell"
  - applies to 1 occurrence(s): Phili 1:22 (live)
- **Observation 19946** (prior-capture, tag statement, status draft): Rejection. *"a living stone rejected by men but in the sight of God chosen and precious"* (1Pe 2:4). The word is to reject after testing: men weighed him and set him aside.
  - applies to 1 occurrence(s): 1Pe 2:4 (living)
- **Observation 20134** (prior-capture, tag statement, status draft): Something offered at a cost to others: David *"would not drink it"* and gives his reason: *"Shall I drink the blood of the men who went at the risk of their lives?"* (2Sa 23:16–17).
  - applies to 1 occurrence(s): 2Sa 23:17 (lives)
- **Observation 20151** (prior-capture, tag statement, status draft): A gift: water from Bethlehem, brought at the risk of three men's lives (2Sa 23:16–17; 1Ch 11:18–19).
  - applies to 2 occurrence(s): 2Sa 23:17 (lives), 1Ch 11:19 (lives)
- **Observation 20152** (prior-capture, tag statement, status draft): A refusal that keeps faith: The king's servants would not kill the priests of the Lord. Doeg did (1Sa 22:17–18).; David *"would not put out my hand against the Lord's anointed"* (1Sa 26:23). He sets it beside a prayer: *"as your life was precious this day in my sight, so may my life be precious in the sight of the Lord"* (26:24).; David *"said longingly, 'Oh, that someone would give me water'"* (2Sa 23:15). When it came, *"he would not drink of it. He poured it out to the Lord and said, 'Far be it from me, O Lord, that I should do this. Shall I drink the blood of the men who went at the risk of their lives?'"* (23:16–17). His own longing was met, and he refused it for the sake of the men's l ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 23:17 (lives)
- **Observation 20363** (prior-capture, tag statement, status draft): Job 7:15: "so that I would choose strangling and death rather than my bones": > Q1 citation: ❗ Needs attention. Ch 2 *Wanting to die* is accurate. The 10.7 working note (*Expected additions*) puts "Job's own words about choosing (Job 7:15 …)" under *Choices weighed by another*. No one weighs this choice: it is Job's own would-be choice, spoken to God in complaint. It belongs with the next bullet, *Choosing between death and life*. This is a working note, not narrative text.; >; > Q2 M64: Include: new. Corroborates Ch 2 *Wanting to die*. New: the soul (*nepheš*) is the chooser; the choice is set off by terror sent in dreams (v14); it is spoken to God, not acted on.; >; > Q3 other M-codes: M47 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 7:16 (live)
- **Observation 12238** (strand-reading, tag key-statement, status draft): The life asked for is for something.
  - meaning: The life asked for is for something. It is asked for in order to keep, praise and call: "give me life, that I may keep the testimonies of your mouth"; "Let my soul live and praise you"; "give us life, and we will call upon your name!"; "that I may live and keep your word". It is asked for with understanding: "give me understanding that I may live"
  - applies to 3 occurrence(s): Psa 119:17 (live), Psa 119:144 (live), Psa 119:175 (live)
- **Observation 12240** (strand-reading, tag key-statement, status draft): The heart, the spirit and the soul revived.
  - meaning: The heart, the spirit and the soul revived. God dwells "with him who is of a contrite and lowly spirit, to revive the spirit of the lowly, and to revive the heart of the contrite". "you who seek God, let your hearts revive". "hear, that your soul may live". Hezekiah: "in all these is the life of my spirit"
  - applies to 2 occurrence(s): Isa 38:16 (live), Isa 55:3 (live)
- **Observation 12241** (strand-reading, tag key-statement, status draft): "May your hearts live forever!"
  - meaning: "May your hearts live forever!" is said to "those who seek him". Three verses later, the same psalm says "before him shall bow all who go down to the dust, even the one who could not keep himself alive". The verse says no more than the wish
  - applies to 2 occurrence(s): Psa 22:26 (live), Psa 22:29 (alive)
- **Observation 12243** (strand-reading, tag key-statement, status draft): Restored from Sheol while still living.
  - meaning: Restored from Sheol while still living. "O Lord, you have brought up my soul from Sheol; you restored me to life from among those who go down to the pit"; "from the depths of the earth you will bring me up again"; "I shall not die, but I shall live, and recount the deeds of the Lord"
  - applies to 1 occurrence(s): Psa 118:17 (live)
- **Observation 12244** (strand-reading, tag key-statement, status draft): Asked for another.
  - meaning: Asked for another. "Oh that Ishmael might live before you!"; David, fasting: "Who knows whether the Lord will be gracious to me, that the child may live?"
  - applies to 3 occurrence(s): Gen 17:18 (live), 2Sa 12:22 (alive), 2Sa 12:22 (live)
- **Observation 12245** (strand-reading, tag key-statement, status draft): God kills and makes alive; no one else can.
  - meaning: God kills and makes alive; no one else can. "I kill and I make alive; I wound and I heal"; "The Lord kills and brings to life; he brings down to Sheol and raises up". A king rejects the role: "Am I God, to kill and to make alive …?"
  - applies to 2 occurrence(s): Deu 32:39 (alive), 2Ki 5:7 (alive)
- **Observation 12247** (strand-reading, tag key-statement, status open): Life kept in famine and danger.
  - meaning: Life kept in famine and danger. "that he may deliver their soul from death and keep them alive in famine"; "the Lord protects him and keeps him alive"; "He does not keep the wicked alive, but gives the afflicted their right"; Joseph: "you meant evil against me, but God meant it for good, to bring it about that many people should be kept alive". Kept alive is joined to fearing him: "to fear the Lord our God, for our good always, that he might preserve us alive"
  - applies to 5 occurrence(s): Gen 50:20 (alive), Deu 6:24 (alive), Job 36:6 (alive), Psa 33:19 (alive), Psa 41:2 (alive)
- **Observation 12254** (strand-reading, tag key-statement, status draft): Ezekiel 37 builds the body before the breath.
  - meaning: Ezekiel 37 builds the body before the breath. "I will lay sinews upon you, and will cause flesh to come upon you, and cover you with skin, and put breath in you, and you shall live, and you shall know that I am the Lord". The question comes first: "Son of man, can these bones live?" And Ezekiel answers, "O Lord God, you know"
  - applies to 3 occurrence(s): Eze 37:3 (live), Eze 37:5 (live), Eze 37:6 (live)
- **Observation 12255** (strand-reading, tag key-statement, status draft): Bodies rise.
  - meaning: Bodies rise. "Your dead shall live; their bodies shall rise. You who dwell in the dust, awake and sing for joy! … the earth will give birth to the dead". Seven verses earlier, of other lords: "They are dead, they will not live; they are shades, they will not arise"
  - applies to 4 occurrence(s): Isa 26:14 (dead), Isa 26:14 (live), Isa 26:19 (dead), Isa 26:19 (live)
- **Observation 12256** (strand-reading, tag key-statement, status draft): "If a man dies, shall he live again?"
  - meaning: "If a man dies, shall he live again?" Job asks it and goes on: "All the days of my service I would wait, till my renewal should come"
  - applies to 1 occurrence(s): Job 14:14 (live)
- **Observation 12259** (strand-reading, tag key-statement, status draft): Adam and Christ; sowing.
  - meaning: Adam and Christ; sowing. "For as in Adam all die, so also in Christ shall all be made alive"; "What you sow does not come to life unless it dies"; "the last Adam became a life-giving spirit" (set against "The first man Adam became a living being", the Gen 2:7 phrase)
  - applies to 1 occurrence(s): 1Cor 15:45 (living)
- **Observation 12262** (strand-reading, tag key-statement, status draft): Live by doing.
  - meaning: Live by doing. "if a person does them, he shall live by them: I am the Lord"; "man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord"; "Justice, and only justice, you shall follow, that you may live"; "Let your heart hold fast my words; keep my commandments, and live"; "Leave your simple ways, and live"
  - applies to 5 occurrence(s): Lev 18:5 (live), Deu 8:3 (live), Deu 16:20 (live), Pro 4:4 (live), Pro 9:6 (live)
- **Observation 12263** (strand-reading, tag key-statement, status resolved): Life set before a person to choose.
  - meaning: Life set before a person to choose. "I have set before you life and death, blessing and curse. Therefore choose life, that you and your offspring may live". The next verse names God as that life: "for he is your life and length of days"
  - applies to 1 occurrence(s): Deu 30:19 (live)
- **Observation 12264** (strand-reading, tag key-statement, status draft): Seek and live.
  - meaning: Seek and live. "Seek me and live"; "Seek good, and not evil, that you may live". The righteous man and the proud man are set side by side: "his soul is puffed up; it is not upright within him, but the righteous shall live by his faith"
  - applies to 3 occurrence(s): Amo 5:4 (live), Amo 5:14 (live), Hab 2:4 (live)
- **Observation 12265** (strand-reading, tag key-statement, status draft): Statutes by which they could not have life.
  - meaning: Statutes by which they could not have life. Of the same people, God says he gave statutes "by which, if a person does them, he shall live". Then: "I gave them statutes that were not good and rules by which they could not have life". Paul: "if a law had been given that could give life, then righteousness would indeed be by the law"
  - applies to 1 occurrence(s): Eze 20:11 (live)
- **Observation 12266** (strand-reading, tag key-statement, status draft): Turn and live.
  - meaning: Turn and live. "Have I any pleasure in the death of the wicked, declares the Lord God, and not rather that he should turn from his way and live?"; "For I have no pleasure in the death of anyone, declares the Lord God; so turn, and live"; "turn back, turn back from your evil ways, for why will you die, O house of Israel?"
  - applies to 3 occurrence(s): Eze 18:23 (live), Eze 18:32 (live), Eze 33:11 (live)
- **Observation 12267** (strand-reading, tag key-statement, status draft): Turning is considered, and it reaches back.
  - meaning: Turning is considered, and it reaches back. "Because he considered and turned away from all the transgressions that he had committed, he shall surely live; he shall not die". "None of the transgressions that he has committed shall be remembered against him". The other way: "None of the righteous deeds that he has done shall be remembered"; "if he trusts in his righteousness and does injustice …"
  - applies to 2 occurrence(s): Eze 18:22 (live), Eze 18:24 (live)
- **Observation 12268** (strand-reading, tag key-statement, status draft): The despairing question.
  - meaning: The despairing question. "Surely our transgressions and our sins are upon us, and we rot away because of them. How then can we live?" God's answer is the next verse (LD-31)
  - applies to 2 occurrence(s): Eze 33:10 (live), Eze 33:11 (live)
- **Observation 12269** (strand-reading, tag key-statement, status draft): False words keep the wrong souls alive.
  - meaning: False words keep the wrong souls alive. "putting to death souls who should not die and keeping alive souls who should not live, by your lying to my people, who listen to lies"; "you have disheartened the righteous falsely, although I have not grieved him"
  - applies to 1 occurrence(s): Eze 13:19 (alive)
- **Observation 12270** (strand-reading, tag key-statement, status draft): Seeing God and living.
  - meaning: Seeing God and living. "you cannot see my face, for man shall not see me and live"; "This day we have seen God speak with man, and man still live"; "who is there of all flesh, that has heard the voice of the living God speaking out of the midst of fire as we have, and has still lived?"
  - applies to 4 occurrence(s): Exo 33:20 (live), Deu 5:24 (live), Deu 5:26 (living), Deu 5:26 (lived)
- **Observation 12272** (strand-reading, tag key-statement, status draft): Living forever is withheld at the start
  - meaning: Living forever is withheld at the start: "lest he reach out his hand and take also of the tree of life and eat, and live forever". Later it is asked: "What man can live and never see death?"; of the one trusting in wealth, "that he should live on forever and never see the pit"; "Your fathers, where are they? And the prophets, do they live forever?"
  - applies to 4 occurrence(s): Gen 3:22 (live), Psa 49:9 (live), Psa 89:48 (live), Zec 1:5 (live)
- **Observation 12273** (strand-reading, tag key-statement, status draft): Not wanting to live forever.
  - meaning: Not wanting to live forever. "I loathe my life; I would not live forever. Leave me alone, for my days are a breath"
  - applies to 1 occurrence(s): Job 7:16 (live)
- **Observation 12274** (strand-reading, tag key-statement, status draft): Fearing God, the midwives let the boys live.
  - meaning: Fearing God, the midwives let the boys live. "But the midwives feared God and did not do as the king of Egypt commanded them, but let the male children live". Joseph: "Do this and you will live, for I fear God"
  - applies to 2 occurrence(s): Gen 42:18 (live), Exo 1:17 (live)
- **Observation 12275** (strand-reading, tag key-statement, status draft): Mercy hoped for from a person.
  - meaning: Mercy hoped for from a person. "we have heard that the kings of the house of Israel are merciful kings … Perhaps he will spare your life"; an oath keeps others alive: "let them live, lest wrath be upon us, because of the oath that we swore to them"
  - applies to 1 occurrence(s): Jos 9:20 (live)
- **Observation 12276** (strand-reading, tag key-statement, status draft): Years without good.
  - meaning: Years without good. "his soul is not satisfied with life's good things"; "if a person lives many years, let him rejoice in them all; but let him remember that the days of darkness will be many"; "Why do the wicked live, reach old age, and grow mighty in power?"
  - applies to 3 occurrence(s): Job 21:7 (live), Ecc 6:3 (lives), Ecc 11:8 (lives)
- **Observation 12280** (strand-reading, tag key-statement, status draft): The dead, seen from this side.
  - meaning: The dead, seen from this side. "But a man dies and is laid low; man breathes his last, and where is he?"; "For the living know that they will die, but the dead know nothing, and they have no more reward, for the memory of them is forgotten"; "a living dog is better than a dead lion". The dead do not praise: "For in death there is no remembrance of you; in Sheol who will give you praise?"; "The dead do not praise the Lord, nor do any who go down into silence"; "Do the departed rise up to praise you?"; "death does not praise you; those who go down to the pit do not hope for your faithfulness"
  - applies to 5 occurrence(s): Psa 88:10 (dead), Psa 115:17 (dead), Ecc 9:4 (living), Ecc 9:4 (dead), Ecc 9:5 (living)
- **Observation 12281** (strand-reading, tag key-statement, status draft): The dead, with God.
  - meaning: The dead, with God. "The poor man died and was carried by the angels to Abraham's side". "Blessed are the dead who die in the Lord from now on." The Spirit adds, "that they may rest from their labors, for their deeds follow them!" Paul: "For to me to live is Christ, and to die is gain". David, of his dead child: "I shall go to him, but he will not return to me"
  - applies to 2 occurrence(s): 2Sa 12:23 (dead), Phili 1:21 (live)
- **Observation 12282** (strand-reading, tag key-statement, status open): Death spoken of as sleep.
  - meaning: Death spoken of as sleep. "the girl is not dead but sleeping. And they laughed at him"; "Now Jesus had spoken of his death, but they thought that he meant taking rest in sleep"; "through Jesus, God will bring with him those who have fallen asleep"; "David, after he had served the purpose of God in his own generation, fell asleep and was laid with his fathers and saw corruption"
  - applies to 3 occurrence(s): Mat 9:24 (dead), Mar 5:39 (dead), Luk 8:52 (dead)
- **Observation 12283** (strand-reading, tag key-statement, status draft): The day of death.
  - meaning: The day of death. "I am old; I do not know the day of my death"; "his day will come to die"; "A good name is better than precious ointment, and the day of death than the day of birth"
  - applies to 1 occurrence(s): 1Sa 26:10 (lives)
- **Observation 12287** (strand-reading, tag key-statement, status draft): The inner sequence, in the verses' own words.
  - meaning: The inner sequence, in the verses' own words. "Then desire when it has conceived gives birth to sin, and sin when it is fully grown brings forth death"; "our sinful passions, aroused by the law, were at work in our members to bear fruit for death"; "I was once alive apart from the law, but when the commandment came, sin came alive and I died"; "The very commandment that promised life proved to be death to me"; "It was sin, producing death in me through what is good"
  - applies to 1 occurrence(s): Rom 7:9 (alive)
- **Observation 12291** (strand-reading, tag key-statement, status resolved): Death named inside a living person.
  - meaning: Death named inside a living person. "For to set the mind on the flesh is death, but to set the mind on the Spirit is life and peace"; "Whoever does not love abides in death"; "worldly grief produces death"; "Wretched man that I am! Who will deliver me from this body of death?"; "For the end of those things is death"; to a church: "strengthen what remains and is about to die"; of false teachers: "fruitless trees in late autumn, twice dead, uprooted"
  - applies to 1 occurrence(s): Jude 12 (dead)
- **Observation 12292** (strand-reading, tag key-statement, status draft): The living likened to the dead.
  - meaning: The living likened to the dead. "like one set loose among the dead, like the slain that lie in the grave, like those whom you remember no more, for they are cut off from your hand"; "For the enemy has pursued my soul; he has crushed my life to the ground; he has made me sit in darkness like those long dead"; "among those in full vigor we are like dead men"; of Miriam: "Let her not be as one dead". "for those dwelling in the region and shadow of death, on them a light has dawned"
  - applies to 5 occurrence(s): Num 12:12 (dead), Psa 88:5 (dead), Psa 143:3 (dead), Isa 59:10 (dead), Lam 3:6 (dead)
- **Observation 12293** (strand-reading, tag key-statement, status draft): "A dead dog": how a person rates himself or another.
  - meaning: "A dead dog": how a person rates himself or another. Mephibosheth: "What is your servant, that you should show regard for a dead dog such as I?"; David to Saul: "After a dead dog! After a flea!"; Abishai of Shimei: "Why should this dead dog curse my lord the king?"
  - applies to 3 occurrence(s): 1Sa 24:14 (dead), 2Sa 9:8 (dead), 2Sa 16:9 (dead)
- **Observation 12294** (strand-reading, tag key-statement, status draft): A body "as good as dead", and faith that considers it.
  - meaning: A body "as good as dead", and faith that considers it. "He did not weaken in faith when he considered his own body, which was as good as dead (since he was about a hundred years old), or when he considered the barrenness of Sarah's womb"; "from one man, and him as good as dead, were born descendants as many as the stars of heaven"
  - applies to 2 occurrence(s): Rom 4:19 (dead), Heb 11:12 (dead)
- **Observation 12296** (strand-reading, tag key-statement, status draft): Death as a ruler that is overthrown.
  - meaning: Death as a ruler that is overthrown. "death no longer has dominion over him"; "God raised him up, loosing the pangs of death, because it was not possible for him to be held by it"; "that through death he might destroy the one who has the power of death, that is, the devil"; "The last enemy to be destroyed is death"; "I died, and behold I am alive forevermore, and I have the keys of Death and Hades"; "For I am sure that neither death nor life, nor angels nor rulers"
  - applies to 1 occurrence(s): Rev 1:18 (living)
- **Observation 12299** (strand-reading, tag key-statement, status draft): The heart and the soul as death comes near.
  - meaning: The heart and the soul as death comes near. "My heart is in anguish within me; the terrors of death have fallen upon me"; "My soul is very sorrowful, even to death"; "his soul was vexed to death"; "there is but a step between me and death"; "Surely the bitterness of death is past"; "light up my eyes, lest I sleep the sleep of death"; "you lay me in the dust of death"; "my heart is wrung within me … in the house it is like death"
  - applies to 1 occurrence(s): 1Sa 20:3 (lives)
- **Observation 12303** (strand-reading, tag key-statement, status resolved): Death longed for and not found.
  - meaning: Death longed for and not found. "who long for death, but it comes not, and dig for it more than for hidden treasures"; "Why did I not die at birth, come out from the womb and expire?"; "people will seek death and will not find it. They will long to die, but death will flee from them"; "Death shall be preferred to life by all the remnant that remains of this evil family"; "I thought the dead who are already dead more fortunate than the living who are still alive"
  - applies to 2 occurrence(s): Ecc 4:2 (dead), Ecc 4:2 (living)
- **Observation 12305** (strand-reading, tag key-statement, status draft): What is asked or given before dying.
  - meaning: What is asked or given before dying. Isaac: "that my soul may bless you before I die"; Jacob: "Now let me die, since I have seen your face and know that you are still alive"; Joseph: "I am about to die, but God will visit you and bring you up out of this land"; "Two things I ask of you; deny them not to me before I die"; "By faith Jacob, when dying, blessed each of the sons of Joseph, bowing in worship over the head of his staff"
  - applies to 1 occurrence(s): Gen 46:30 (alive)
- **Observation 12306** (strand-reading, tag key-statement, status draft): Loyalty that reaches to death.
  - meaning: Loyalty that reaches to death. Ruth: "Where you die I will die, and there will I be buried. May the Lord do so to me and more also if anything but death parts me from you". "In life and in death they were not divided". Ittai: "wherever my lord the king shall be, whether for death or for life, there also will your servant be". Peter: "Even if I must die with you, I will not deny you!" Thomas: "Let us also go, that we may die with him". Paul: "What are you doing, weeping and breaking my heart? For I am ready not only to be imprisoned but even to die in Jerusalem for the name of the Lord Jesus". "they loved not their lives even unto death"; "Be faithful unto death, and I will give you the crown ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 15:21 (lives)
- **Observation 12307** (strand-reading, tag key-statement, status draft): More deliverance from death.
  - meaning: More deliverance from death. "Our God is a God of salvation, and to God, the Lord, belong deliverances from death"; "O you who lift me up from the gates of death"; "In famine he will redeem you from death"; "The Lord has disciplined me severely, but he has not given me over to death"; "He delivered us from such a deadly peril, and he will deliver us". A person may do it too: "whoever brings back a sinner from his wandering will save his soul from death"; "Rescue those who are being taken away to death"
  - applies to 1 occurrence(s): 2Cor 1:10 (deadly peril)
- **Observation 12309** (strand-reading, tag key-statement, status draft): Never to see death.
  - meaning: Never to see death. "if anyone keeps my word, he will never see death"; "everyone who lives and believes in me shall never die. Do you believe this?"; "so that one may eat of it and not die"; Enoch "was taken up so that he should not see death"; "We know that we have passed out of death into life, because we love the brothers"
  - applies to 1 occurrence(s): Joh 11:26 (lives)
- **Observation 12312** (strand-reading, tag key-statement, status draft): What his death is for those who live.
  - meaning: What his death is for those who live. "For the love of Christ controls us, because we have concluded this: that one has died for all, therefore all have died; and he died for all, that those who live might no longer live for themselves but for him who for their sake died and was raised". "By what you eat, do not destroy the one for whom Christ died"
  - applies to 1 occurrence(s): 2Cor 5:15 (live)
- **Observation 12313** (strand-reading, tag key-statement, status draft): Dying to sin and to the law; putting to death.
  - meaning: Dying to sin and to the law; putting to death. "How can we who died to sin still live in it?"; "For one who has died has been set free from sin"; "For through the law I died to the law, so that I might live to God"; "we are released from the law, having died to that which held us captive, so that we serve in the new way of the Spirit"; "Put to death therefore what is earthly in you: sexual immorality, impurity, passion, evil desire, and covetousness, which is idolatry"; "if by the Spirit you put to death the deeds of the body, you will live"
  - applies to 3 occurrence(s): Rom 6:2 (live), Rom 8:13 (live), Gal 2:19 (live)
- **Observation 12314** (strand-reading, tag key-statement, status draft): A death that belongs to the Lord.
  - meaning: A death that belongs to the Lord. "For none of us lives to himself, and none of us dies to himself. For if we live, we live to the Lord, and if we die, we die to the Lord. So then, whether we live or whether we die, we are the Lord's"; "Christ will be honored in my body, whether by life or by death. For to me to live is Christ, and to die is gain"; "I die every day!"; "For we who live are always being given over to death for Jesus' sake, so that the life of Jesus also may be manifested in our mortal flesh"; "as dying, and behold, we live"
  - applies to 5 occurrence(s): Rom 14:7 (lives), Rom 14:8 (live), 2Cor 4:11 (live), 2Cor 6:9 (live), Phili 1:21 (live)
- **Observation 12316** (strand-reading, tag key-statement, status draft): Death set before a person as a way.
  - meaning: Death set before a person as a way. "See, I have set before you today life and good, death and evil"; "Behold, I set before you the way of life and the way of death"; "There is a way that seems right to a man, but its end is the way to death"; "In the path of righteousness is life, and in its pathway there is no death"; "Whoever is steadfast in righteousness will live, but he who pursues evil will die"; "righteousness delivers from death"; "Death and life are in the power of the tongue, and those who love it will eat its fruits"
  - applies to 1 occurrence(s): Pro 11:19 (live)
- **Observation 12320** (strand-reading, tag key-statement, status draft): Grief at a death, in its forms.
  - meaning: Grief at a death, in its forms. David, after the child died: "But now he is dead. Why should I fast? Can I bring him back again? I shall go to him, but he will not return to me"; "the spirit of the king longed to go out to Absalom, because he was comforted about Amnon, since he was dead"; "Weep not for him who is dead, nor grieve for him, but weep bitterly for him who goes away"; Hagar: "Let me not look on the death of the child"; Judah of Jacob: "as soon as he sees that the boy is not with us, he will die"; Mary: "Lord, if you had been here, my brother would not have died"; to Ezekiel: "Sigh, but not aloud; make no mourning for the dead"
  - applies to 4 occurrence(s): 2Sa 12:23 (dead), 2Sa 13:39 (dead), Jer 22:10 (dead), Eze 24:17 (dead)
- **Observation 12321** (strand-reading, tag key-statement, status draft): Judgement where the verse names the inner cause.
  - meaning: Judgement where the verse names the inner cause. "But Er, Judah's firstborn, was wicked in the sight of the Lord, and the Lord put him to death"; "the anger of the Lord was kindled against Uzzah, and God struck him down there because of his error"; "So Saul died for his breach of faith. He broke faith with the Lord"; "He made a path for his anger; he did not spare them from death"; "the men who brought up a bad report of the land— died by plague before the Lord"
  - applies to 1 occurrence(s): Psa 78:50 (lives)
- **Observation 12323** (strand-reading, tag key-statement, status draft): Turning to the dead instead of God.
  - meaning: Turning to the dead instead of God. "should not a people inquire of their God? Should they inquire of the dead on behalf of the living?"; "or a medium or a necromancer or one who inquires of the dead"; "they yoked themselves to the Baal of Peor, and ate sacrifices offered to the dead". And kindness that reaches the dead: "May he be blessed by the Lord, whose kindness has not forsaken the living or the dead!"
  - applies to 6 occurrence(s): Deu 18:11 (dead), Rut 2:20 (living), Rut 2:20 (dead), Psa 106:28 (dead), Isa 8:19 (dead), Isa 8:19 (living)
- **Observation 12325** (strand-reading, tag key-statement, status draft): Swearing by the LORD's life and by the life of the one spoken to, as a bond.
  - meaning: Swearing by the LORD's life and by the life of the one spoken to, as a bond. David: "But truly, as the Lord lives and as your soul lives, there is but a step between me and death". Uriah: "As you live, and as your soul lives, I will not do this thing". Elisha, three times: "As the Lord lives, and as you yourself live, I will not leave you". The Shunammite says the same to Elisha. Ittai: "As the Lord lives, and as my lord the king lives, wherever my lord the king shall be, whether for death or for life, there also will your servant be"
  - applies to 7 occurrence(s): 1Sa 20:3 (lives), 2Sa 11:11 (live), 2Sa 15:21 (lives), 2Ki 2:2 (lives), 2Ki 2:4 (lives), 2Ki 2:6 (lives), 2Ki 4:30 (lives)
- **Observation 12326** (strand-reading, tag key-statement, status draft): The oath names what the LORD has done for the one who swears.
  - meaning: The oath names what the LORD has done for the one who swears. "As the Lord lives, who has redeemed my life out of every adversity"; "As the Lord lives, who has redeemed my soul out of every adversity"; "As the Lord lives, who made our souls"; "As the Lord, the God of Israel, lives, before whom I stand"; Job: "As God lives, who has taken away my right, and the Almighty, who has made my soul bitter"
  - applies to 7 occurrence(s): 2Sa 4:9 (lives), 1Ki 1:29 (lives), 1Ki 17:1 (lives), 2Ki 3:14 (lives), 2Ki 5:16 (lives), Job 27:2 (lives), Jer 38:16 (lives)
- **Observation 12327** (strand-reading, tag key-statement, status draft): The same oath, said in anger, rashness, greed and secret.
  - meaning: The same oath, said in anger, rashness, greed and secret. "Then David's anger was greatly kindled against the man, and he said to Nathan, 'As the Lord lives, the man who has done this deserves to die'". Saul: "For as the Lord lives who saves Israel, though it be in Jonathan my son, he shall surely die", and the people's answering oath, "As the Lord lives, there shall not one hair of his head fall to the ground". Saul to the medium: "As the Lord lives, no punishment shall come upon you for this thing". Gehazi: "As the Lord lives, I will run after him and get something from him". "Then King Zedekiah swore secretly to Jeremiah"
  - applies to 6 occurrence(s): 1Sa 14:39 (lives), 1Sa 14:45 (lives), 1Sa 28:10 (lives), 2Sa 12:5 (lives), 2Ki 5:20 (lives), Jer 38:16 (lives)
- **Observation 12328** (strand-reading, tag key-statement, status draft): The oath judged.
  - meaning: The oath judged. "Though they say, 'As the Lord lives,' yet they swear falsely"; "if you swear, 'As the Lord lives,' in truth, in justice, and in righteousness, then nations shall bless themselves in him"; "swear not, 'As the Lord lives'"; of oaths by other gods: "As your god lives, O Dan … they shall fall, and never rise again". To Judah in Egypt: "my name shall no more be invoked by the mouth of any man of Judah … saying, 'As the Lord God lives.'" Of the nations: "if they will diligently learn the ways of my people, to swear by my name, 'As the Lord lives,' … then they shall be built up". And the oath itself will change: no longer "As the Lord lives who brought up the people of Israel out ... (cut; the whole text is in the workbook)
  - applies to 10 occurrence(s): Jer 4:2 (lives), Jer 5:2 (lives), Jer 12:16 (lives), Jer 16:14 (lives), Jer 16:15 (lives), Jer 23:7 (lives), Jer 23:8 (lives), Jer 44:26 (lives), Hos 4:15 (lives), Amo 8:14 (lives)
- **Observation 12329** (strand-reading, tag key-statement, status draft): God swears by his own life.
  - meaning: God swears by his own life. All 24 hits are God speaking. For life: "As I live, declares the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live". In judgement: "As I live, declares the Lord God, I will not be inquired of by you"; "I will deal with you according to the anger and envy that you showed because of your hatred against them". Of his glory: "as I live, and as all the earth shall be filled with the glory of the Lord"; "For I lift up my hand to heaven and swear, As I live forever". Paul cites it: "As I live, says the Lord, every knee shall bow to me, and every tongue shall confess to God"
  - applies to 7 occurrence(s): Num 14:21 (live), Deu 32:40 (live), Eze 20:3 (live), Eze 20:31 (live), Eze 33:11 (live), Eze 35:11 (live), Rom 14:11 (live)
- **Observation 12330** (strand-reading, tag key-statement, status draft): The living God, named against idols and against mockery.
  - meaning: The living God, named against idols and against mockery. "But the Lord is the true God; he is the living God and the everlasting King. At his wrath the earth quakes"; "you turned to God from idols to serve the living and true God"; "turn from these vain things to a living God, who made the heaven and the earth"; Goliath "should defy the armies of the living God"; Sennacherib "has sent to mock the living God"; "you pervert the words of the living God"
  - applies to 10 occurrence(s): 1Sa 17:26 (living), 1Sa 17:36 (living), 2Ki 19:4 (living), 2Ki 19:16 (living), Isa 37:4 (living), Isa 37:17 (living), Jer 10:10 (living), Jer 23:36 (living), Act 14:15 (living), 1Th 1:9 (living)
- **Observation 12331** (strand-reading, tag key-statement, status draft): The soul, the heart and the conscience turned toward the living God, or away.
  - meaning: The soul, the heart and the conscience turned toward the living God, or away. "My soul thirsts for God, for the living God. When shall I come and appear before God?"; "My soul longs, yes, faints for the courts of the Lord; my heart and flesh sing for joy to the living God"; "lest there be in any of you an evil, unbelieving heart, leading you to fall away from the living God"; "It is a fearful thing to fall into the hands of the living God"; "purify our conscience from dead works to serve the living God"; "who is there of all flesh, that has heard the voice of the living God speaking out of the midst of fire as we have, and has still lived?"; "we have our hope set on the living God"
  - applies to 8 occurrence(s): Deu 5:26 (living), Deu 5:26 (lived), Psa 42:2 (living), Psa 84:2 (living), 1Ti 4:10 (living), Heb 3:12 (living), Heb 9:14 (living), Heb 10:31 (living)
- **Observation 12332** (strand-reading, tag key-statement, status draft): The living God among his people.
  - meaning: The living God among his people. "Here is how you shall know that the living God is among you"; "we are the temple of the living God"; "written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts"; "Children of the living God"; "the church of the living God"
  - applies to 6 occurrence(s): Jos 3:10 (living), Hos 1:10 (living), Rom 9:26 (living), 2Cor 3:3 (living), 2Cor 6:16 (living), 1Ti 3:15 (living)
- **Observation 12333** (strand-reading, tag key-statement, status draft): "The Lord lives", said as praise.
  - meaning: "The Lord lives", said as praise. "The Lord lives, and blessed be my rock, and exalted be my God, the rock of my salvation"; "For I know that my Redeemer lives"; "worship him who lives forever and ever"
  - applies to 5 occurrence(s): 2Sa 22:47 (lives), Job 19:25 (lives), Psa 18:46 (lives), Dan 12:7 (lives), Rev 4:10 (lives)
- **Observation 12336** (strand-reading, tag key-statement, status draft): The days lived as the span of fearing, remembering and learning.
  - meaning: The days lived as the span of fearing, remembering and learning. "so that they may learn to fear me all the days that they live on the earth, and that they may teach their children so"; "lest they depart from your heart all the days of your life"; "that all the days of your life you may remember the day when you came out of the land of Egypt"; the king "shall read in it all the days of his life, that he may learn to fear the Lord his God"; Israel served the Lord "all the days of the elders who outlived Joshua and had known all the work that the Lord did for Israel"; Hannah: "I will give him to the Lord all the days of his life"
  - applies to 1 occurrence(s): Deu 4:10 (live)
- **Observation 12337** (strand-reading, tag key-statement, status draft): A life summed.
  - meaning: A life summed. Jacob: "Few and evil have been the days of the years of my life". Barzillai: "How many years have I still to live, that I should go up with the king to Jerusalem?" "David did what was right in the eyes of the Lord and did not turn aside from anything that he commanded him all the days of his life, except in the matter of Uriah the Hittite". "Absalom in his lifetime had taken and set up for himself the pillar … for he said, 'I have no son to keep my name in remembrance.'"
  - applies to 1 occurrence(s): 2Sa 19:34 (live)
- **Observation 12338** (strand-reading, tag key-statement, status resolved): God's work on the heart, in the chapter of the choice.
  - meaning: God's work on the heart, in the chapter of the choice. "And the Lord your God will circumcise your heart and the heart of your offspring, so that you will love the Lord your God with all your heart and with all your soul, that you may live". The same chapter sets "life and death" before the people, and says "choose life" and "he is your life and length of days"
  - applies to 2 occurrence(s): Deu 30:6 (live), Deu 30:19 (live)
- **Observation 12339** (strand-reading, tag key-statement, status draft): Life by doing, and the counter-statements.
  - meaning: Life by doing, and the counter-statements. "walks in the statutes of life, not doing injustice, he shall surely live"; "My covenant with him was one of life and peace … It was a covenant of fear, and he feared me"; "For it is no empty word for you, but your very life". The lawyer: "Teacher, what shall I do to inherit eternal life?" Jesus: "You have answered correctly; do this, and you will live". "If you would enter life, keep the commandments". Against these: "Now it is evident that no one is justified before God by the law, for 'The righteous shall live by faith.' But the law is not of faith, rather 'The one who does them shall live by them'"; "Moses writes about the righteousness that is ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Luk 10:28 (live), Rom 10:5 (live), Gal 3:11 (live), Gal 3:12 (live)
- **Observation 12340** (strand-reading, tag key-statement, status draft): Fed by the word.
  - meaning: Fed by the word. "Man shall not live by bread alone, but by every word that comes from the mouth of God"
  - applies to 2 occurrence(s): Mat 4:4 (live), Luk 4:4 (live)
- **Observation 12345** (strand-reading, tag key-statement, status draft): Life worn down and near its end.
  - meaning: Life worn down and near its end. "For my life is spent with sorrow, and my years with sighing; my strength fails because of my iniquity"; "For my soul is full of troubles, and my life draws near to Sheol"; "Your life shall hang in doubt before you. Night and day you shall be in dread and have no assurance of your life"; "For we were so utterly burdened beyond our strength that we despaired of life itself"; "and made their lives bitter with hard service"; "because of his iniquity, none can maintain his life"
  - applies to 2 occurrence(s): Exo 1:14 (lives), Eze 7:13 (live)
- **Observation 12346** (strand-reading, tag key-statement, status draft): Life named as brief.
  - meaning: Life named as brief. "Remember that my life is a breath; my eye will never again see good"; "like a weaver I have rolled up my life; he cuts me off from the loom"; "What is your life? For you are a mist that appears for a little time and then vanishes. Instead you ought to say, 'If the Lord wills, we will live and do this or that.'" "For who knows what is good for man while he lives the few days of his vain life, which he passes like a shadow?"
  - applies to 2 occurrence(s): Ecc 6:12 (lives), Jam 4:15 (live)
- **Observation 12347** (strand-reading, tag key-statement, status draft): The living weighed.
  - meaning: The living weighed. "For the living know that they will die" (in Ch 2); "he who is joined with all the living has hope"; at the house of mourning, "the living will lay it to heart"; "the hearts of the children of man are full of evil, and madness is in their hearts while they live"; "Why should a living man complain, a man, about the punishment of his sins?"; "for no one living is righteous before you"
  - applies to 8 occurrence(s): Psa 143:2 (living), Ecc 7:2 (living), Ecc 9:3 (live), Ecc 9:3 (dead), Ecc 9:4 (living), Ecc 9:4 (dead), Ecc 9:5 (living), Lam 3:39 (living)
- **Observation 12348** (strand-reading, tag key-statement, status draft): Life enjoyed, as given.
  - meaning: Life enjoyed, as given. "Enjoy life with the wife whom you love, all the days of your vain life that he has given you under the sun, because that is your portion in life"; "to eat and drink and find enjoyment in all the toil … the few days of his life that God has given him, for this is his lot"; "For he will not much remember the days of his life because God keeps him occupied with joy in his heart"; "there is nothing better for them than to be joyful and to do good as long as they live"
  - applies to 1 occurrence(s): Ecc 3:12 (live)
- **Observation 12349** (strand-reading, tag key-statement, status draft): What life does not consist in.
  - meaning: What life does not consist in. "for one's life does not consist in the abundance of his possessions"; "men of the world whose portion is in this life"; "For though, while he lives, he counts himself blessed"; Abraham: "remember that you in your lifetime received your good things, and Lazarus in like manner bad things"; "so that they may take hold of that which is truly life"; "If in Christ we have hope in this life only, we are of all people most to be pitied"; "Whoever loves his life loses it, and whoever hates his life in this world will keep it for eternal life"
  - applies to 1 occurrence(s): Psa 49:18 (lives)
- **Observation 12350** (strand-reading, tag key-statement, status draft): One's own life spoken of to God.
  - meaning: One's own life spoken of to God. "You have granted me life and steadfast love, and your care has preserved my spirit"; "Because your steadfast love is better than life, my lips will praise you"; "a prayer to the God of my life"; "who redeems your life from the pit"; "You have taken up my cause, O Lord; you have redeemed my life"; "Yet you brought up my life from the pit, O Lord my God"; "He asked life of you; you gave it to him"; "O Lord, by these things men live, and in all these is the life of my spirit"; "The Lord is the stronghold of my life; of whom shall I be afraid?"; "preserve my life from dread of the enemy"; "who has kept our soul among the living"; "You open your hand; you satisfy ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Psa 66:9 (living), Isa 38:16 (live)
- **Observation 12351** (strand-reading, tag key-statement, status draft): For as long as I live.
  - meaning: For as long as I live. "I will praise the Lord as long as I live"; "So I will bless you as long as I live"; "I will sing to the Lord as long as I live"; "The living, the living, he thanks you, as I do this day" (the verse after "For Sheol does not thank you", Isa 38:18); "One thing have I asked of the Lord … that I may dwell in the house of the Lord all the days of my life"; "Surely goodness and mercy shall follow me all the days of my life"
  - applies to 4 occurrence(s): Psa 63:4 (live), Psa 104:33 (live), Psa 146:2 (live), Isa 38:19 (living)
- **Observation 12352** (strand-reading, tag key-statement, status open): "The land of the living" and the records of the living.
  - meaning: "The land of the living" and the records of the living. "I believe that I shall look upon the goodness of the Lord in the land of the living!"; "You are my refuge, my portion in the land of the living"; "I shall not see the Lord, the Lord in the land of the living"; "who considered that he was cut off out of the land of the living"; "he will uproot you from the land of the living"; the nations "who spread terror in the land of the living". Abigail: "the life of my lord shall be bound in the bundle of the living in the care of the Lord your God". "Let them be blotted out of the book of the living; let them not be enrolled among the righteous"; "everyone who has been recorded for life in Jerus ... (cut; the whole text is in the workbook)
  - applies to 14 occurrence(s): 1Sa 25:29 (living), Psa 27:13 (living), Psa 52:5 (living), Psa 69:28 (living), Psa 142:5 (living), Isa 38:11 (living), Isa 53:8 (living), Jer 11:19 (living), Eze 32:23 (living), Eze 32:24 (living), Eze 32:25 (living), Eze 32:26 (living); and 2 more (sheet `Observation nodes`)
- **Observation 12353** (strand-reading, tag key-statement, status draft): Gone down alive.
  - meaning: Gone down alive. "and they go down alive into Sheol, then you shall know that these men have despised the Lord"; "Let death steal over them; let them go down to Sheol alive; for evil is in their dwelling place and in their heart"; "like Sheol let us swallow them alive" (the sinners' words); "These two were thrown alive into the lake of fire"
  - applies to 5 occurrence(s): Num 16:30 (alive), Num 16:33 (alive), Psa 55:15 (alive), Pro 1:12 (alive), Rev 19:20 (alive)
- **Observation 12354** (strand-reading, tag key-statement, status draft): Living water, forsaken and given.
  - meaning: Living water, forsaken and given. "for my people have committed two evils: they have forsaken me, the fountain of living waters, and hewed out cisterns for themselves, broken cisterns that can hold no water"; "If you knew the gift of God … he would have given you living water"; "The water that I will give him will become in him a spring of water welling up to eternal life"; "Whoever believes in me, as the Scripture has said, 'Out of his heart will flow rivers of living water'"; "let the one who is thirsty come; let the one who desires take the water of life without price"; "he will guide them to springs of living water, and God will wipe away every tear from their eyes"
  - applies to 5 occurrence(s): Jer 2:13 (living), Jer 17:13 (living), Joh 4:10 (living), Joh 7:38 (living), Rev 7:17 (living)
- **Observation 12356** (strand-reading, tag key-statement, status draft): Life in the Son.
  - meaning: Life in the Son. "In him was life, and the life was the light of men"; "For as the Father has life in himself, so he has granted the Son also to have life in himself"; "As the living Father sent me, and I live because of the Father, so whoever feeds on me, he also will live because of me"; "I came that they may have life and have it abundantly"; "Because I live, you also will live"; "you killed the Author of life"; "by the power of an indestructible life"; "he always lives to make intercession for them"
  - applies to 3 occurrence(s): Joh 6:57 (living), Joh 14:19 (live), Heb 7:25 (lives)
- **Observation 12358** (strand-reading, tag key-statement, status draft): Who lives in the one who lives.
  - meaning: Who lives in the one who lives. "I have been crucified with Christ. It is no longer I who live, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God"; "For through the law I died to the law, so that I might live to God"; "consider yourselves dead to sin and alive to God in Christ Jesus"; "that we might die to sin and live to righteousness"; "present your bodies as a living sacrifice"; "to live self-controlled, upright, and godly lives in the present age"; "all who desire to live a godly life in Christ Jesus will be persecuted"
  - applies to 7 occurrence(s): Rom 6:11 (alive), Rom 12:1 (living), Gal 2:19 (live), Gal 2:20 (live), 2Ti 3:12 (live), Tit 2:12 (live), 1Pe 2:24 (live)
- **Observation 12359** (strand-reading, tag key-statement, status draft): "All live to him."
  - meaning: "All live to him." "Now he is not God of the dead, but of the living, for all live to him"; "who died for us so that whether we are awake or asleep we might live with him"
  - applies to 4 occurrence(s): Mat 22:32 (living), Mar 12:27 (living), Luk 20:38 (living), 1Th 5:10 (live)
- **Observation 12360** (strand-reading, tag key-statement, status draft): Life and the Spirit.
  - meaning: Life and the Spirit. "For the law of the Spirit of life has set you free in Christ Jesus from the law of sin and death"; "although the body is dead because of sin, the Spirit is life because of righteousness"; "If we live by the Spirit, let us also keep in step with the Spirit"; "the one who sows to the Spirit will from the Spirit reap eternal life"; "Shall we not much more be subject to the Father of spirits and live?"; "that though judged in the flesh the way people are, they might live in the spirit the way God does"
  - applies to 3 occurrence(s): Gal 5:25 (live), Heb 12:9 (live), 1Pe 4:6 (live)
- **Observation 12361** (strand-reading, tag key-statement, status draft): Alive in name, dead in fact.
  - meaning: Alive in name, dead in fact. "You have the reputation of being alive, but you are dead"; "but she who is self-indulgent is dead even while she lives"; "They are darkened in their understanding, alienated from the life of God because of the ignorance that is in them, due to their hardness of heart"; "for this your brother was dead, and is alive; he was lost, and is found"; "you know that no murderer has eternal life abiding in him"; "to one a fragrance from death to death, to the other a fragrance from life to life"
  - applies to 3 occurrence(s): Luk 15:32 (alive), 1Ti 5:6 (lives), Rev 3:1 (alive)
- **Observation 12364** (strand-reading, tag key-statement, status draft): The tree of life.
  - meaning: The tree of life. "The tree of life was in the midst of the garden"; "lest he reach out his hand and take also of the tree of life and eat, and live forever"; "to guard the way to the tree of life"; "To the one who conquers I will grant to eat of the tree of life, which is in the paradise of God"; "The leaves of the tree were for the healing of the nations"; "Blessed are those who wash their robes, so that they may have the right to the tree of life"
  - applies to 1 occurrence(s): Gen 3:22 (live)
- **Observation 12365** (strand-reading, tag key-statement, status draft): The book of life, and the living and the dead judged.
  - meaning: The book of life, and the living and the dead judged. "And the dead were judged by what was written in the books, according to what they had done"; "And if anyone's name was not found written in the book of life, he was thrown into the lake of fire"; "I will never blot his name out of the book of life"; Christ "is to judge the living and the dead"; "For to this end Christ died and lived again, that he might be Lord both of the dead and of the living"; "I saw the souls of those who had been beheaded … They came to life and reigned with Christ for a thousand years"; "The rest of the dead did not come to life until the thousand years were ended"
  - applies to 5 occurrence(s): Act 10:42 (living), Rom 14:9 (lived), 2Ti 4:1 (living), 1Pe 4:5 (living), Rev 20:5 (come to life)
- **Observation 12366** (strand-reading, tag key-statement, status draft): What is called living.
  - meaning: What is called living. "For the word of God is living and active … discerning the thoughts and intentions of the heart"; "he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead"; "you yourselves like living stones are being built up as a spiritual house"; "He received living oracles to give to us"; "holding fast to the word of life"; "His divine power has granted to us all things that pertain to life and godliness"; husbands and wives "are heirs with you of the grace of life, so that your prayers may not be hindered"
  - applies to 4 occurrence(s): Act 7:38 (living), Heb 4:12 (living), 1Pe 1:3 (living), 1Pe 2:5 (living)
- **Observation 12368** (strand-reading, tag key-statement, status draft): Narrative "alive", where an inner word is in the verse.
  - meaning: Narrative "alive", where an inner word is in the verse. "Joseph is still alive … And his heart became numb, for he did not believe them" (in Ch 2), then "It is enough; Joseph my son is still alive. I will go and see him before I die"; "Then the woman whose son was alive said to the king, because her heart yearned for her son"; Joab to David: "today I know that if Absalom were alive and all of us were dead today, then you would be pleased"; "Saul and Jonathan, beloved and lovely! In life and in death they were not divided"; Jonathan: "If I am still alive, show me the steadfast love of the Lord, that I may not die"; Moses: "even today while I am yet alive with you, you have been rebellious aga ... (cut; the whole text is in the workbook)
  - applies to 7 occurrence(s): Gen 45:26 (alive), Gen 45:28 (alive), Deu 31:27 (alive), 1Sa 20:14 (alive), 2Sa 19:6 (alive), 2Sa 19:6 (dead), 1Ki 3:26 (alive)
- **Observation 12369** (strand-reading, tag key-statement, status draft): Healed or raised: unit 1 territory.
  - meaning: Healed or raised: unit 1 territory. "Jesus said to him, 'Go; your son will live.' The man believed the word that Jesus spoke to him"; "See, your son lives"; "And they took the youth away alive, and were not a little comforted"
  - applies to 3 occurrence(s): 1Ki 17:23 (lives), Joh 4:50 (live), Act 20:12 (alive)
- **Observation 12370** (strand-reading, tag key-statement, status draft): Life taken by people.
  - meaning: Life taken by people. "he should not be allowed to live"; "Justice has not allowed him to live" (the islanders' reading)
  - applies to 3 occurrence(s): Act 22:22 (live), Act 25:24 (live), Act 28:4 (live)
- **Observation 12371** (strand-reading, tag key-statement, status draft): H2416C in its "life" sense
  - meaning: H2416C in its "life" sense (not in the unit's Strong's list; H2416C is mostly "beast"). "so that his life loathes bread, and his appetite the choicest food"; "His soul draws near the pit, and his life to those who bring death"; "he keeps back his soul from the pit, his life from perishing by the sword"; "He has redeemed my soul from going down into the pit, and my life shall look upon the light"; "You were wearied with the length of your way, but you did not say, 'It is hopeless'; you found new life for your strength, and so you were not faint". Also H2416D: "do not forget the life of your poor forever"
  - applies to 2 occurrence(s): Psa 78:50 (lives), Psa 143:3 (dead)
- **Observation 12373** (strand-reading, tag key-statement, status draft): Life given over.
  - meaning: Life given over. "He let loose on them his burning anger … He made a path for his anger; he did not spare them from death, but gave their lives over to the plague"; "The godless in heart cherish anger; they do not cry for help when he binds them. They die in youth, and their life ends among the cult prostitutes"
  - applies to 1 occurrence(s): Psa 78:50 (lives)
- **Observation 12376** (strand-reading, tag key-statement, status draft): Death as a sleep not roused.
  - meaning: Setting: Job sets a man against a tree. The tree has hope from its own root; the man has none from himself. Meaning: death is named as sleep, and the sleep has no waking "till the heavens are no more". Implies (R): I read the limit, "till the heavens are no more", as a boundary set on the not-waking rather than an open "never". Job does not draw it out. What he does is turn at once from the fact to God: hide me, appoint a time, remember me, call, and I will answer. The hope he cannot find in nature, he asks of God. The verses state both the despair (14:12) and the asking (14:13–15), side by side.
  - applies to 1 occurrence(s): Job 14:14 (live)
- **Observation 12383** (strand-reading, tag key-statement, status draft): The dead waking.
  - meaning: Meaning: the hope against death is named with the same picture as death itself: those who sleep in the dust shall awake. Implies: the waking is not the same for all. Daniel divides it into life and contempt. Isaiah sets two kinds of dead side by side, those who "will not arise" and those told to "awake and sing for joy". For the psalmist, waking means seeing God's face and being satisfied: the inner being's desire is met. Job 14:12 ("he will not awake … till the heavens are no more") stands beside these, unreconciled.
  - applies to 4 occurrence(s): Isa 26:14 (dead), Isa 26:14 (live), Isa 26:19 (dead), Isa 26:19 (live)
- **Observation 12384** (strand-reading, tag key-statement, status draft): The child not awakened.
  - meaning: Meaning: a death is spoken of, in the household, as not waking. Implies: the return of life is told as a waking: warmth, breath (a sneeze), open eyes. Prayer comes first (4:33).
  - applies to 1 occurrence(s): 2Ki 4:32 (dead)
- **Observation 12390** (strand-reading, tag key-statement, status draft): Psalm 49: two ends for the soul.
  - meaning: Setting: the psalm is about death that comes to everyone, the wise and the fool alike (49:10). It is not about escaping a danger in life. Meaning: set against that death, the psalmist says God will ransom his soul from Sheol's power, "for he will receive me". Of the rich man who trusts in his wealth, "his soul will go to the generation of his fathers, who will never again see light." Implies: here the soul has an end beyond death, and there are two ends: received by God, or gone to the fathers in the dark. What the psalm sets against each other is two souls, not soul and spirit. It does not say what "receive" involves. (The same verb is used of Enoch: "God took him", Gen 5:24. I note this; I ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Psa 49:9 (live), Psa 49:18 (lives)
- **Observation 12392** (strand-reading, tag key-statement, status draft): "Live in the spirit the way God does."
  - meaning: Meaning: Peter speaks of the dead living "in the spirit the way God does". Implies (R): I read "those who are dead" as people now dead, who heard the gospel while they lived. The verse does not say when they heard it, and I leave that open.
  - applies to 2 occurrence(s): 1Pe 4:5 (living), 1Pe 4:6 (live)
- **Observation 12393** (strand-reading, tag key-statement, status resolved): The spirit against death while living.
  - meaning: Already woven (Ch 2 "Death in the living"; Ch 14). No new meaning beyond those places.
  - applies to 2 occurrence(s): Rom 8:12 (live), Rom 8:13 (live)
- **Observation 12394** (strand-reading, tag key-statement, status draft): The soul as a corpse; Sheol's soul.
  - meaning: Meaning: the word names the individual to the end (as Ch 2 says). It is also used of Sheol's own appetite. Implies: the soul word is used of the one who wants. Sheol is pictured as wanting, as the greedy are.
  - applies to 1 occurrence(s): Num 19:11 (dead)
- **Observation 12395** (strand-reading, tag key-statement, status draft): No verse speaks of the heart after death.
  - meaning: Meaning: Scripture speaks of the heart up to death. Implies (R): the closest verse draws the line itself: "madness is in their hearts while they live, and after that they go to the dead" (Ecc 9:3). The heart is named for "while they live". After that, only "they go to the dead". I read this as Scripture being silent on the heart beyond death. I do not argue from the silence.
  - applies to 2 occurrence(s): Ecc 9:3 (live), Ecc 9:3 (dead)
- **Observation 12398** (strand-reading, tag key-statement, status resolved): "For to me to live is Christ, and to die is gain … I am hard pressed between the two. My desire is to depart and be with Christ, for that is far better. But to remain in the flesh is more necessary on your account."
  - meaning: Meaning: Paul names death as departing to be with Christ, "far better". He holds it against staying, which is better for others. Implies: the weighing is itself an inner act ("hard pressed", "my desire"). Death is weighed as gain because of who it leads to.
  - applies to 2 occurrence(s): Phili 1:21 (live), Phili 1:22 (live)
- **Observation 12404** (strand-reading, tag key-statement, status draft): Order at his coming.
  - meaning: Order at his coming. "the dead in Christ will rise first. Then we who are alive … will be caught up together with them … and so we will always be with the Lord."
  - applies to 1 occurrence(s): 1Th 4:17 (alive)
- **Observation 12405** (strand-reading, tag key-statement, status draft): Old Testament: seen in the flesh.
  - meaning: Old Testament: seen in the flesh. Job: "after my skin has been thus destroyed, yet in my flesh I shall see God, whom I shall see for myself, and my eyes shall behold, and not another. My heart faints within me!" Psalm 17:15: "when I awake, I shall be satisfied with your likeness."
  - applies to 1 occurrence(s): Job 19:25 (lives)
- **Observation 12406** (strand-reading, tag key-statement, status draft): Resurrection is a person.
  - meaning: Resurrection is a person. "I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live." Martha already knew "he will rise again in the resurrection on the last day".
  - applies to 1 occurrence(s): Joh 11:25 (live)

### 4.3 The retired catalogue observations (0, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

_no rows_

### 4.4 Withdrawn observations (10)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 6 |
| reading | 2 |
| Analysis_phase_1 | 2 |

| reason as stored | observations |
|---|---|
| no change record | 6 |
| the old form of parts is replaced by the nine items | 3 |
| a second observation of the same word in this verse that repeats the face with the dictionary sense; the face observation is kept (RW-03, RW-04) | 1 |

## 5. Claims and the narrative

93 claims rest on these occurrences: 4 on an observation of these words and 89 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (4)

- **C-88** (narrative, verdict New, status current, in narrative 1): Scripture speaks of death inside a living person: the heart dying first, the living called dead, abiding in death
  - beyond the text: gathers the uses into one account
  - rests on: observation 12291 (strand-reading key-statement, live; Jude 12); observation 12393 (strand-reading key-statement, live; Rom 8:12, Rom 8:13)
  - told in: chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook)
- **C-118** (narrative, verdict New, status current, in narrative 1): Life and death are set before a person to choose; life is chosen by doing, seeking and holding on
  - beyond the text: gathers the commands that end "and live"
  - rests on: observation 12263 (strand-reading key-statement, live; Deu 30:19); observation 12338 (strand-reading key-statement, live; Deu 30:19, Deu 30:6)
  - told in: chapter 02 Life, breath and death, Life set before a person (2 earlier telling(s) in the workbook)
- **C-156** (narrative, verdict New, status current, in narrative 1): People sometimes want to die; of the 24 verses with such a wish, 17 name no inner word
  - beyond the text: a count over the wish-to-die verses (2026-10-14)
  - rests on: observation 12303 (strand-reading key-statement, live; Ecc 4:2)
  - told in: chapter 02 Life, breath and death, Wanting to die (1 earlier telling(s) in the workbook)
- **C-342** (narrative, verdict New, status current, in narrative 1): A choice between living and dying can be held open: Paul names both as good and does not settle it by choosing.
  - beyond the text: reads Paul's 'which I shall choose I cannot tell' as a choice deliberately left open
  - rests on: observation 12398 (strand-reading key-statement, live; Phili 1:21, Phili 1:22)
  - told in: chapter 10.7 Choosing and setting direction, Life and death set before a person

### 5.2 Claims reached by a verse only (89)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| 2-4 | Animals are *nephesh ḥayyâ* just as man is (Gen 1:20–24; 2:7; 9:10) | Gen 1:20–24; 2:7; 9:10 | living H2416A | current | not told in a section |
| 2-5 | Animals almost never have *rûaḥ*; Ecc 3:21 is the only exception; Gen 7:22 uses *neshamah*, not *rûaḥ* | Gen 2:7 | living H2416A | withdrawn | not told in a section |
| 2-16 | The verse puts soul and spirit beside joints and marrow, which are adjacent, and its end point is the heart: "discerning the thoughts and intentions of the heart". It shows closeness that only the word can divide. It is one of several places the words part; others are added (1Co 15:45; 1Co 14:14–15; the *psychikos* / *pneumatikos* contrast in 1Co 2:14; 15:44–46) (dep §3.4; B §8) | Heb 4:12; 1Co 15:45; 1Co 2:14; 15:44–46 | living G2198 | current | not told in a section |
| 3-1 | The man becomes a *nephesh* (Gen 2:7) | Gen 2:7 | living H2416A | current | not told in a section |
| 3-2 | Gen 2:7's phrase is shared with the animals. The verse is marked by God breathing into one creature. The "formula" is an inference, not something the text states. 1Co 15:45 sets "a living being" against "a life-giving spirit" (G §1.1, §1.5) | Gen 2:7; 1Co 15:45 | living H2416A; living G2198 | current | not told in a section |
| 3-3 | The original itself cites "the Lord who made our souls" (Jer 38:16). Also: "The Spirit of God has made me, and the breath of the Almighty gives me life" (Job 33:4). Both are made by God. The distinct-origins argument does not hold | Jer 38:16 | lives H2416A | current | not told in a section |
| 3-9 | Most of these verses speak of the soul delivered or brought up from Sheol: a living person rescued from death. Corrected 2026-10-04 (#1950): of 15 soul-delivered verses, 12 are rescue from dying; Psa 49:15 (set against the death of all, 49:10) and Psa 16:10 (as Act 2:27, 31 read it) look beyond death; Psa 89:48 says no one can. The verdict holds: no verse gives soul and spirit different destinations. The verses that name Sheol or Hades speak of the soul and never of the spirit. Ecc 3:21 leaves the spirit's destination open ("Who knows?"). The "different destinations" argument, which the original called "the most compelling evidence", does not hold (G §16.4; dep §3.9) | Psa 16:10; 30:3; 49:15; 86:13; 89:48; Psa 89:48 | live H2421 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death; chapter 02 Life, breath and death, Delivered from death; chapter 09 Where the words part, Lines that are often drawn, but that I cannot find (3 earlier telling(s) in the workbook) |
| 3-13 | "The body apart from the spirit is dead" (Jam 2:26) | Jam 2:26 | dead G3498 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death (1 earlier telling(s) in the workbook) |
| 8-4 | The spirit was "dead through sin" (Eph 2:1–5) | Eph 2:1–5 | dead G3498; lived G0390 | held | not told in a section |
| 9-6 | Flesh (Jam 1:14), devil, world as three sources (Eph 2:2–3) | Eph 2:2–3 | lived G0390 | held | not told in a section |
| 10-3 | "Within" is already the OT promise (Eze 36:27; 37:14). The OT also has the Spirit turning a man "into another man" (1Sa 10:6) | Eze 36:27; 37:14 | live H2421 | current | not told in a section |
| 10-4 | The body's redemption at the end stands (Rom 8:23; 1Co 15:42–44), told in Chapter 2. The text renews the inner self "day by day" (2Co 4:16); renewal is both God's gift (Eze 36:26) and the person's task (Eze 18:31). Assigning each phase to one component is not stated | 1Co 15:42–44 | dead G3498 | current | chapter 02 Life, breath and death, Waited for (1 earlier telling(s) in the workbook) |
| C-83 | Death comes to everyone, and falls alike on those the world would set apart | Psalm 89:48; Zechariah 1:5; Genesis 3:22; Job 14:14; Job 30:23 | live H2421; living H2416A | current | chapter 02 Life, breath and death, What death is (2 earlier telling(s) in the workbook) |
| C-86 | James and Paul trace death's coming from within: desire, sin, death | Romans 7:9 | alive G2198 | current | chapter 02 Life, breath and death, Death and sin (1 earlier telling(s) in the workbook) |
| C-87 | Each person answers for his own sin, and sin can be put away while a death still follows | Ezekiel 18:13; Ezekiel 18:17 | live H2421 | current | chapter 02 Life, breath and death, Death and sin (2 earlier telling(s) in the workbook) |
| C-89 | Scripture speaks of death as sleep, and gives its hope against death as waking | Matthew 9:24; Mark 5:39; Luke 8:52-53 | dead G0599 | current | chapter 02 Life, breath and death, Sleep and waking (2 earlier telling(s) in the workbook) |
| C-90 | Paul uses sleep to speak to grief: grief with hope is set apart from grief without hope, and the hope rests on Christ's rising | 1 Thessalonians 4:13-15; 1 Corinthians 15:20; 1 Corinthians 15:6 | alive G2198; dead G3498; alive G0737; alive G2193 | current | chapter 02 Life, breath and death, Sleep and waking (1 earlier telling(s) in the workbook) |
| C-92 | The waking of the dead is not the same for all | Isaiah 26:14; Isaiah 26:19 | dead H4191; live H2421; dead H7496 | current | chapter 02 Life, breath and death, Sleep and waking; chapter 02 Life, breath and death, Life, and judgment (2 earlier telling(s) in the workbook) |
| C-94 | The righteous speak of going down to Sheol, as the wicked are said to | Genesis 42:38; Isaiah 38:10-11; Ezekiel 31:15-17 | dead H4191; living H2416A; lived H3427 | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-95 | The manner of going down to Sheol is named: mourning, with sorrow, in peace, with blood, silently, alive | Genesis 42:38; Numbers 16:33; Psalm 55:13-15 | dead H4191; alive H0834A; alive H2416A | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-97 | Sheol is pictured as never satisfied, and the same picture is used of the eyes and the greed of man | Proverbs 1:12 | alive H2416A | current | chapter 05 The soul, From throat to corpse; chapter 02 Life, breath and death, Going down to Sheol (2 earlier telling(s) in the workbook) |
| C-99 | Sheol and Hades are named beside death as a power that holds the dead, gives them up to judgment and is ended | Revelation 20:13-14; Revelation 1:18 | dead G3498; alive G2198; living G2198 | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-100 | At death the soul departs, dies, is poured out, is named to the very end, and has an end beyond death | Judges 16:30; Numbers 19:11 | dead H0834A; dead H4191 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death (1 earlier telling(s) in the workbook) |
| C-102 | The verses that name Sheol or Hades speak of the soul and never of the spirit | Psalm 89:48 | live H2421 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death; chapter 09 Where the words part, Lines that are often drawn, but that I cannot find (2 earlier telling(s) in the workbook) |
| C-103 | The heart can die before the body does; no verse found speaks of the heart after death | Psalm 31:12; Ecclesiastes 9:3 | dead H4191; live H2416E | current | chapter 02 Life, breath and death, Soul, spirit and heart at death (2 earlier telling(s) in the workbook) |
| C-105 | Deliverance from death is for something: walking before God among the living and telling of him | Psalm 118:17; Isaiah 38:19 | live H2421; living H2416A | current | chapter 02 Life, breath and death, Delivered from death (1 earlier telling(s) in the workbook) |
| C-106 | Some verses say the dead know nothing, do not praise God and do not return | Ecclesiastes 9:5; Psalm 115:17; Isaiah 38:18-19; Psalm 88:10 | dead H4191; living H2416A | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-107 | Prophetic oracles against kings and nations speak of the dead in Sheol as stirred, speaking and comforted | Ezekiel 32:24 | living H2416A | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-108 | In Jesus' account of the rich man and Lazarus the dead remember, see, ask and are answered; one is comforted and one in anguish, and the chasm between them cannot be crossed | Luke 16:22-31 | dead G3498 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-109 | Scripture speaks of the dead in more than one way, and neither way is made to explain the other away | Ecclesiastes 9:5; Psalm 115:17 | dead H4191; living H2416A | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-110 | With God, the dead are carried, blessed and at rest | Revelation 14:13; 2 Samuel 12:23; Luke 20:38; 1 Thessalonians 5:10; 1 Peter 4:6; Matthew 22:32; Mark 12:27 | dead G3498; dead H4191; live G2198; living G2198 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-113 | God holds both ends, killing and making alive, and keeps alive between them | Deuteronomy 32:39; 2 Kings 5:7; Psalm 33:19; Job 36:6; Genesis 50:20; Deuteronomy 6:24 | alive H2421 | current | chapter 02 Life, breath and death, Breath lent, and held by God (1 earlier telling(s) in the workbook) |
| C-120 | Wisdom marks where the way to death ends, and some of what kills a person is named from within | James 3:8 | deadly G2287 | current | chapter 02 Life, breath and death, Life set before a person (3 earlier telling(s) in the workbook) |
| C-121 | God has no pleasure in anyone's death and calls for turning; the turning is a considered act that reaches back over the past, and trust can lean the wrong way | Ezekiel 18:23; Ezekiel 18:32; Ezekiel 33:10-11; Ezekiel 18:28; Ezekiel 18:22; Ezekiel 18:24; Ezekiel 33:13 | live H2421; live H0413; live H2416A | current | chapter 02 Life, breath and death, Life set before a person (2 earlier telling(s) in the workbook) |
| C-122 | Life can be wrongly kept or taken by lying words | Ezekiel 13:19 | alive H2421; live H2421 | current | chapter 02 Life, breath and death, Life set before a person (1 earlier telling(s) in the workbook) |
| C-125 | The commonest form of the oath by life is "As the Lord lives" (39 verses); in six of them a second life is joined | 1 Samuel 20:3; 1 Samuel 25:26; 2 Kings 2:2; 2 Kings 2:4; 2 Kings 2:6; 2 Kings 4:30 | lives H2416A; live H2416A | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-126 | The oath "As the Lord lives" places a promise before the living God and binds the speaker to it by life | 1 Samuel 20:3; 2 Kings 2:2; 2 Samuel 15:21; 1 Kings 1:29; 1 Kings 17:1; Job 27:2 | lives H2416A; live H2416A | current | chapter 02 Life, breath and death, Living before God (2 earlier telling(s) in the workbook) |
| C-127 | The oath's words stay the same while the heart that speaks them differs; it is judged by how it is sworn | 2 Samuel 12:5; 1 Samuel 14:45; 2 Kings 5:20; Jeremiah 5:2; Jeremiah 4:2 | lives H2416A; lives H0518A | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-128 | God swears by his own life, and the oath carries what he wants and what he will do | Ezekiel 33:11; Ezekiel 20:3; Romans 14:11 | live H0413; live H2416A; live H2421; live G2198 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-129 | "The living God" sets him against idols, which have no breath | Jeremiah 10:10; 1 Thessalonians 1:9 | living H2416A; living G2198 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-130 | The inner being turns toward the living God, or away from him | Psalm 42:2; Psalm 84:2; Hebrews 3:12; Hebrews 10:31 | living H2416A; living G2198 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-131 | Scripture counts a life in days and says what the days are for | Deuteronomy 4:10; Psalm 146:2 | live H2416A; live H2416E | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-132 | The world where life is lived is named "the land of the living" | Psalm 27:13; Psalm 142:5; Isaiah 38:11; 1 Samuel 25:29 | living H2416A; lives H0853; lives H5315H | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-133 | People weigh their own lives: loathed, worn down, enjoyed, and not consisting in possessions | Ecclesiastes 9:4; Ecclesiastes 9:3; Psalm 143:2 | dead H4191; living H2416A; live H2416E | current | chapter 02 Life, breath and death, Life weighed (6 earlier telling(s) in the workbook) |
| C-136 | Death's certainty can be turned into a reason to indulge, and Scripture answers it | 1 Corinthians 15:32 | dead G3498 | current | chapter 02 Life, breath and death, Life weighed (1 earlier telling(s) in the workbook) |
| C-139 | Scripture speaks of death in more than one way: the body's death, death in the living, dying to sin, a death beyond death, death as a power, and the living made like the dead | Matthew 8:22; Luke 9:60; Ephesians 2:1; Romans 6:2; Matthew 28:4; Revelation 1:17 | dead G3498; live G2198 | current | chapter 02 Life, breath and death, Life, and judgment; chapter 02 Life, breath and death, Death spoken of in more than one way (3 earlier telling(s) in the workbook) |
| C-140 | The father sets "dead" beside "lost" and "alive" beside "found"; to perish and to be lost are one word | Luke 15:24; Luke 15:32 | dead G3498; alive G2198 | current | chapter 02 Life, breath and death, Death spoken of in more than one way (1 earlier telling(s) in the workbook) |
| C-141 | "Dead in" trespasses and "died to" sin are opposites: death under sin, and death that ends its rule | Ephesians 2:1; Ephesians 2:5; Colossians 2:13; Romans 6:2; Romans 6:10; Romans 6:11; Romans 7:4; Galatians 2:19; 1 Peter 2:24 | dead G3498; live G2198; lives G2198; alive G2198; dead G3303 | current | chapter 02 Life, breath and death, Death spoken of in more than one way; chapter 02 Life, breath and death, Dead to sin (2 earlier telling(s) in the workbook) |
| C-142 | The word "dead" passes to sin itself, to faith and to works | Romans 7:8-9; James 2:17; James 2:26; Hebrews 6:1; Hebrews 9:14; Romans 8:10 | dead G3498; alive G2198; living G2198 | current | chapter 02 Life, breath and death, Death in the living; chapter 02 Life, breath and death, Death spoken of in more than one way (2 earlier telling(s) in the workbook) |
| C-144 | Where a verse sets death against eternal life (Romans 6:23) it speaks of more than the body's death; other verses do not say which death, and are left as written | Romans 8:13 | live G2198 | current | chapter 02 Life, breath and death, Death and sin (1 earlier telling(s) in the workbook) |
| C-145 | In Acts a lie contrived in the heart is followed at once by death, and fear comes on all who hear | Acts 5:10-11 | dead G3498 | current | chapter 02 Life, breath and death, Death and sin; chapter 02 Life, breath and death, Facing death (2 earlier telling(s) in the workbook) |
| C-147 | The verses name what brings death in the living, each in its own place; no verse gathers them into one list | Ephesians 2:1; Colossians 2:13; 1 Timothy 5:6; Revelation 3:1 | dead G3498; dead G2348; lives G2198; alive G2198 | current | chapter 02 Life, breath and death, Death in the living (2 earlier telling(s) in the workbook) |
| C-148 | The verses name the way out of death in the living: hearing the Son and believing, God making alive with forgiveness, waking, coming home; loving the brothers is its sign | John 5:24-25; Colossians 2:13; Ephesians 5:14; Luke 15:17-24 | dead G3498; live G2198 | current | chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook) |
| C-150 | The believer has already died to sin, to the law and to the powers of the world, and a putting to death is still to be done | Romans 6:2-3; Romans 6:11; Romans 7:4; Galatians 2:19; Colossians 2:20; 2 Timothy 2:11; Romans 8:13 | live G2198; alive G2198; dead G3303; dead G3498; live G4800 | current | chapter 14 Made new, Revived, restored, renewed; chapter 02 Life, breath and death, Dead to sin (3 earlier telling(s) in the workbook) |
| C-152 | The coming of death is often met with anguish and terror, and the fear of dying shapes what people do | 1 Samuel 20:3 | lives H2416A | current | chapter 02 Life, breath and death, Facing death (2 earlier telling(s) in the workbook) |
| C-154 | The nearness of death is given a purpose: to rely on God who raises the dead | 2 Corinthians 1:9 | dead G3498 | current | chapter 02 Life, breath and death, Facing death (1 earlier telling(s) in the workbook) |
| C-155 | A death is met by those who remain: grief, not watching, fasting and then eating, reproach, limits on mourning, mourning withheld, and death not taken to heart | 2 Samuel 12:21-23; 2 Samuel 19:6; Luke 7:12-15; 2 Samuel 11:26; Deuteronomy 14:1; Jeremiah 16:4; Jeremiah 16:7 | alive H2416A; live H2421; dead H4191; dead G3498; dead H3588A; deadly H8463; dead H5921A | current | chapter 02 Life, breath and death, Those left behind (3 earlier telling(s) in the workbook) |
| C-157 | Of the seven wishes to die answered in these passages, two are fed, two are answered another way, and three are granted, each to a man already blinded or wounded | Jonah 4:3; Numbers 21:5-8; Judges 16:30; 2 Samuel 1:9-16 | live H2416E; live H0853; live H2421; dead H0834A; dead H4191; live H3588A | current | chapter 02 Life, breath and death, Wanting to die (3 earlier telling(s) in the workbook) |
| C-158 | Giving life belongs to the Father, the Son and the Spirit | John 5:21; Romans 4:17 | dead G3498 | current | chapter 02 Life, breath and death, Made alive (1 earlier telling(s) in the workbook) |
| C-159 | The dead made alive are living people; the crossing from death to life happens now, and life is spoken of as had now and still to come | Colossians 2:13; Ephesians 2:5; John 11:26; Romans 6:4 | dead G3498; lives G2198 | current | chapter 02 Life, breath and death, Made alive (1 earlier telling(s) in the workbook) |
| C-160 | The making alive rests on a death, and Christ went to it himself | Romans 6:9-10 | dead G3498; lives G2198 | current | chapter 02 Life, breath and death, Made alive (2 earlier telling(s) in the workbook) |
| C-161 | That death changes how the living live: no longer for themselves, dead to sin, Christ living in them | 2 Corinthians 5:14-15; Galatians 2:19-20; Romans 12:1; 1 Peter 2:24 | live G2198; lives G2198; living G2198 | current | chapter 02 Life, breath and death, Made alive (2 earlier telling(s) in the workbook) |
| C-162 | A death, too, can belong to the Lord, and a dying can go on while a person lives | Romans 14:7-9; Philippians 1:20-21; 2 Corinthians 4:11; 2 Corinthians 6:9 | lives G2198; live G2198; dead G3498; lived G2198; living G2198 | current | chapter 02 Life, breath and death, Dying to the Lord (1 earlier telling(s) in the workbook) |
| C-164 | Some wait to see one thing before they die, and then let go | Genesis 45:28; Genesis 46:30 | alive H2416A | current | chapter 02 Life, breath and death, Dying to the Lord (1 earlier telling(s) in the workbook) |
| C-165 | People hold to someone, or to something, even to death, and the readiness can fail | Revelation 12:11 | lives G5590H | current | chapter 02 Life, breath and death, Dying to the Lord; chapter 10.10 Relating to others, Loyalty and honour (3 earlier telling(s) in the workbook) |
| C-166 | The living are told how to deal with the dead: inquiring of them and offering to them are forbidden; kindness to the dead is blessed | Deuteronomy 18:11; Psalm 106:28; Ruth 1:8 | dead H0413; dead H4191 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-178 | God humbles to show what is in the heart, to teach what a person lives by, and to do him good in the end, against the heart that lifts itself up in plenty | Deuteronomy 8:2-3; Hebrews 12:9-11 | live H2421; lives H2421; live G2198 | current | chapter 10.14 Humility, Being humbled by God; chapter 04 The heart, The heart humbled (2 earlier telling(s) in the workbook) |
| C-194 | Submission among people is told with a ground that faces God and, where the passage goes on, with a duty on the other side | 1 Peter 3:1-7 | live G4924 | current | chapter 10.10 Relating to others, Holding authority over another; chapter 10.14 Humility, Submitting; chapter 10.10 Relating to others, Humility toward one another (5 earlier telling(s) in the workbook) |
| C-205 | The parts of the inner person give way in sequence: soul, spirit, heart under an enemy, then a turn; heart, then spirit, then body under sorrow | Psalm 143:3-6 | dead H4191 | current | chapter 11 Other sides of the inner being, 3. The parts give way in sequence (2 earlier telling(s) in the workbook) |
| C-217 | Pride at its full height says of itself what is true only of God: the proud city's "I am, and there is no one besides me" repeats God's self-statement | Zephaniah 2:15 | lived H3427 | current | chapter 10.15 Pride, The heart that says what God says; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-219 | Pride deceives the one who holds it, and the fear one inspires in others can feed it | Obadiah 3; Jeremiah 49:16 | live H7931 | current | chapter 10.15 Pride, The heart that says what God says (1 earlier telling(s) in the workbook) |
| C-220 | Pride shuts God out of the thoughts, is set against faith, and gives no rest | Habakkuk 2:4-5 | live H2421 | current | chapter 10.15 Pride, The heart that says what God says (1 earlier telling(s) in the workbook) |
| C-241 | The Son's majesty is received and grounded, stands beside his being handed over, and does not defend itself against mockery; he did not grasp what pride grasps | Colossians 1:18-19 | dead G3498 | current | chapter 10.15 Pride, The mock; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-244 | A plan can presume on time it does not own; the boast about tomorrow is set against saying If the Lord wills | James 4:13-16 | live G2198 | current | chapter 10.15 Pride, The boast; chapter 10.7 Choosing and setting direction, Presumption (2 earlier telling(s) in the workbook) |
| C-251 | God's reign is spoken with wrath in one place, and as good news with peace, salvation and comfort in another | Rev 11:18 | dead G3498 | current | chapter 13.1 Divine, Ruling (1 earlier telling(s) in the workbook) |
| C-270 | The hope Scripture gives against death includes the body | Isa 26:19; Rom 8:11 | dead H4191; dead H7496; live H2421; dead G3498 | current | chapter 02 Life, breath and death, The body raised (1 earlier telling(s) in the workbook) |
| C-271 | Paul speaks of believers as already raised with Christ, while their mortal bodies are still to be given life | Col 2:12; Rom 8:11 | dead G3498 | current | chapter 02 Life, breath and death, The body raised (1 earlier telling(s) in the workbook) |
| C-274 | Jesus puts the denial of the resurrection down to knowing neither the Scriptures nor the power of God, and answers it from God's name | Mar 12:26; Luk 20:38 | dead G3498; live G2198; living G2198 | current | chapter 02 Life, breath and death, Believed, questioned, denied (1 earlier telling(s) in the workbook) |
| C-275 | The disciples did not understand the rising from the dead until afterwards, when they remembered and their minds were opened | Mar 9:10; Joh 20:9; Joh 2:22 | dead G3498 | current | chapter 02 Life, breath and death, Believed, questioned, denied (1 earlier telling(s) in the workbook) |
| C-276 | Paul lets faith and hope rest on Christ having been raised | 1Cor 15:12 | dead G3498 | current | chapter 02 Life, breath and death, Believed, questioned, denied (1 earlier telling(s) in the workbook) |
| C-277 | Herod's word that John has been raised is his conscience speaking | Luk 9:7 | dead G3498 | current | chapter 02 Life, breath and death, Believed, questioned, denied (1 earlier telling(s) in the workbook) |
| C-278 | The coming resurrection is given as a reason for how a person lives now: giving without return, enduring, self-control, steadfast work | Heb 11:35 | dead G3498 | current | chapter 02 Life, breath and death, Waited for (1 earlier telling(s) in the workbook) |
| C-279 | 'Imperishable' is said of the raised body and also of what is within or held for a person: love, the seed of new birth, the beauty of a gentle spirit, an inheritance | 1Cor 15:52 | dead G3498 | current | chapter 02 Life, breath and death, Changed; chapter 11 Other sides of the inner being, 4. One word, opposite values (2 earlier telling(s) in the workbook) |
| C-303 | Loyalty can fail at its post: Abner did not keep watch over the Lord's anointed, while David refused to strike him | 1Sa 26:16 | lives H2416A | current | chapter 10.10 Relating to others, Loyalty and honour (1 earlier telling(s) in the workbook) |
| C-341 | Choosing is joined to the inner being: in God to his heart and his soul, in people to the heart, the soul's delight and its appetite. | Deu 18:6 | lives H1481A | current | chapter 13.1 Divine, Choosing; chapter 10.7 Choosing and setting direction, Others around a choice; chapter 10.7 Choosing and setting direction, What draws it |
| C-347 | The same will word names a refusal that keeps faith, to the Lord's anointed, his priests, the lives of others, and against enticement, and a refusal that does violence, the stronger shutting out the plea of the weaker; the passage gives the reason each time. | 2Sa 23:17; 1Ch 11:19 | lives H5315H; lives H3588A | current | chapter 10.7 Choosing and setting direction, Willing |
| C-353 | A king's will made absolute is brought down until he knows that the Most High rules and gives the kingdom to whom he will; the Most High does according to his will, and none can stay his hand. | Dan 4:17 | living H2417 | current | chapter 10.7 Choosing and setting direction, Willing; chapter 13.1 Divine, Willing |
| C-361 | God also thinks and plans: his plan stands where human plans cross it, he takes thought for the one in need, and he speaks in his heart. | Gen 50:20 | alive H2421 | current | chapter 11 Other sides of the inner being, 8. God has a heart and a soul; chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 13.1 Divine, Purposing |
| C-392 | The setting apart of gifts is done in abundance and joy, and is answered with blessing. | 2Ch 31:6 | lived H3427 | current | chapter 10.7 Choosing and setting direction, Dedicating |

### 5.3 The narrative sections that tell these claims (51)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 6 | 02 Life, breath and death | Breath lent, and held by God | C-113 |
| 8 | 02 Life, breath and death | Life set before a person | C-118, C-120, C-121, C-122 |
| 9 | 02 Life, breath and death | Living before God | C-125, C-126, C-127, C-128, C-129, C-130, C-131, C-132 |
| 11 | 02 Life, breath and death | What death is | C-83 |
| 12 | 02 Life, breath and death | Death and sin | C-86, C-87, C-144, C-145 |
| 13 | 02 Life, breath and death | Death in the living | C-88, C-142, C-147, C-148 |
| 14 | 02 Life, breath and death | Sleep and waking | C-89, C-90, C-92 |
| 15 | 02 Life, breath and death | Life weighed | C-133, C-136 |
| 16 | 02 Life, breath and death | Facing death | C-145, C-152, C-154 |
| 17 | 02 Life, breath and death | Wanting to die | C-156, C-157 |
| 18 | 02 Life, breath and death | Soul, spirit and heart at death | 3-9, 3-13, C-100, C-102, C-103 |
| 20 | 02 Life, breath and death | Delivered from death | 3-9, C-105 |
| 21 | 02 Life, breath and death | Made alive | C-158, C-159, C-160, C-161 |
| 22 | 02 Life, breath and death | Dying to the Lord | C-162, C-164, C-165 |
| 23 | 02 Life, breath and death | The body raised | C-270, C-271 |
| 26 | 02 Life, breath and death | Changed | C-279 |
| 27 | 02 Life, breath and death | Waited for | 10-4, C-278 |
| 28 | 02 Life, breath and death | Life, and judgment | C-92, C-139 |
| 29 | 02 Life, breath and death | After death | C-106, C-107, C-108, C-109, C-110, C-166 |
| 53 | 05 The soul | From throat to corpse | C-97 |
| 89 | 09 Where the words part | Lines that are often drawn, but that I cannot find | 3-9, C-102 |
| 144 | 10.4 Thinking | Small, passing, and wholly seen | C-361 |
| 185 | 10.7 Choosing and setting direction | What draws it | C-341 |
| 189 | 10.7 Choosing and setting direction | Others around a choice | C-341 |
| 197 | 10.7 Choosing and setting direction | Willing | C-347, C-353 |
| 198 | 10.7 Choosing and setting direction | Life and death set before a person | C-342 |
| 230 | 10.10 Relating to others | Holding authority over another | C-194 |
| 232 | 10.10 Relating to others | Loyalty and honour | C-165, C-303 |
| 295 | 11 Other sides of the inner being | 3. The parts give way in sequence | C-205 |
| 296 | 11 Other sides of the inner being | 4. One word, opposite values | C-279 |
| 302 | 11 Other sides of the inner being | 8. God has a heart and a soul | C-361 |
| 323 | 13.1 Divine | Choosing | C-341 |
| 324 | 13.1 Divine | Purposing | C-361 |
| 325 | 13.1 Divine | Willing | C-353 |
| 329 | 13.1 Divine | Ruling | C-251 |
| 338 | 14 Made new | Revived, restored, renewed | C-150 |
| 348 | 02 Life, breath and death | Going down to Sheol | C-94, C-95, C-97, C-99 |
| 349 | 02 Life, breath and death | Death spoken of in more than one way | C-139, C-140, C-141, C-142 |
| 350 | 02 Life, breath and death | Dead to sin | C-141, C-150 |
| 351 | 02 Life, breath and death | Those left behind | C-155 |
| 363 | 10.14 Humility | Being humbled by God | C-178 |
| 369 | 10.14 Humility | Submitting | C-194 |
| 377 | 10.10 Relating to others | Humility toward one another | C-194 |
| 378 | 04 The heart | The heart humbled | C-178 |
| 384 | 10.15 Pride | The heart that says what God says | C-217, C-219, C-220 |
| 387 | 10.15 Pride | The boast | C-244 |
| 388 | 10.15 Pride | The mock | C-241 |
| 393 | 10.7 Choosing and setting direction | Presumption | C-244 |
| 395 | 13.1 Divine | Majesty | C-217, C-241 |
| 401 | 02 Life, breath and death | Believed, questioned, denied | C-274, C-275, C-276, C-277 |
| 406 | 10.7 Choosing and setting direction | Dedicating | C-392 |

## 6. Phrases attached to the collection (8)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| come to life | 6674 | strong route: strong G2198 via live; strong G2198 via lived; strong G2198 via lives; strong G2198 via living | 1 | 0 | 1 | 1 |
| deadly peril | 6741 | english route: word deadly | 1 | 0 | 1 | 1 |
| half dead | 7263 | english route: word dead | 1 | 0 | 0 | 0 |
| live on | 7552 | english route: word live | 2 | 0 | 4 | 3 |
| live peaceably | 7554 | english route: word live | 1 | 0 | 3 | 3 |
| live quietly | 7556 | english route: word live | 1 | 0 | 1 | 1 |
| lives on | 7560 | english route: word lives | 1 | 0 | 0 | 0 |
| remained alive | 10000 | the phrase remained alive is one concept, placed in live (step 4, by meaning) | 2 | 0 | 0 | 0 |

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

