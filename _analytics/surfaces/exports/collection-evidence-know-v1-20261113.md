# Collection evidence report: know

Generated 2026-11-13T19:00:38Z by run RUN-20261113_190033_666-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-know-v1-20261113.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection know at a glance

Status confirmed; core term 174; created 2026-11-06T06:30:58Z, updated 2026-11-10T16:03:02Z; run RUN-20261110_160301_852-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (45)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| acknowledged | word | gathered | acknowledge | placed | 3 | 2 |
| aware | word | gathered | aware | placed | 9 | 9 |
| be unaware | phrase | phrase | be unaware | placed | 4 | 2 |
| can interpret | phrase | phrase | can interpret | placed | 2 | 1 |
| can read | phrase | phrase | can read | placed | 2 | 1 |
| certainty | word | gathered | certainty | placed | 5 | 5 |
| comprehend | word | synonym | comprehend | placed | 3 | 3 |
| comprehended | word | synonym | comprehend | placed | 1 | 1 |
| comprehends | word | synonym | comprehend | placed | 1 | 1 |
| concluded | word | synonym | conclude | placed | 1 | 1 |
| discovered | word | gathered | discover | placed | 4 | 3 |
| examine | word | synonym | examine | placed | 25 | 25 |
| fully knew | phrase | phrase | fully knew | placed | 1 | 1 |
| grasped | word | synonym | grasp | placed | 5 | 5 |
| ignorant | word | gathered | ignorant | placed | 9 | 7 |
| ignorantly | word | gathered | ignorant | placed | 1 | 1 |
| interpret | word | synonym | interpret | placed | 10 | 9 |
| interpreted | word | synonym | interpret | placed | 5 | 4 |
| knew | word | synonym | know | placed | 96 | 88 |
| know | word | core | know | placed | 997 | 867 |
| know her | phrase | phrase | know her | placed | 2 | 1 |
| know how | phrase | phrase | know how | placed | 5 | 5 |
| know then | phrase | phrase | know then | placed | 1 | 1 |
| knowing | word | synonym | know | placed | 46 | 43 |
| knowledge | word | synonym | know | placed | 162 | 156 |
| known | word | synonym | know | placed | 200 | 181 |
| knows | word | synonym | know | placed | 96 | 87 |
| learn | word | synonym | learn | placed | 43 | 41 |
| learned | word | synonym | learn | placed | 31 | 28 |
| learning | word | synonym | learn | placed | 8 | 8 |
| made known | phrase | phrase | made known | placed | 18 | 16 |
| make known | phrase | phrase | make known | placed | 11 | 11 |
| no knowledge | phrase | phrase | no knowledge | placed | 1 | 1 |
| not know | phrase | phrase | not know | placed | 2 | 2 |
| not knowing | phrase | phrase | not knowing | placed | 1 | 1 |
| not recognize | phrase | phrase | not recognize | placed | 2 | 2 |
| not recognized | phrase | phrase | not recognized | placed | 1 | 1 |
| perceived | word | gathered | perceive | placed | 19 | 19 |
| realized | word | synonym | realized | placed | 4 | 4 |
| realizes | word | synonym | realizes | placed | 3 | 2 |
| realizing | word | gathered | realizing | placed | 1 | 1 |
| recognize | word | synonym | recognize | placed | 8 | 8 |
| sound knowledge | phrase | phrase | sound knowledge | placed | 1 | 1 |
| studied | word | synonym | study | placed | 2 | 2 |
| study | word | synonym | study | placed | 3 | 3 |

### 2.2 The Strong's codes behind the members (112)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H3045 יָדַע ya.da "to know" | 795 | 28 | 772 | know 555, known 101, knew 49, knows 49, knowledge 15, perceived 5, know how 4, learn 4, knowing 3, learned 3, certainty 2, acknowledged 1, aware 1, comprehend 1, discovered 1, know then 1 | none | 151 |
| G6063 οἶδα oida "to know" | 229 | 1 | 228 | know 174, knowing 29, knows 16, aware 2, knew 2, knowledge 2, comprehends 1, fully knew 1, know how 1, realizing 1 | none | 35 |
| G1097 γινώσκω ginōskō "to know" | 188 | 1 | 175 | know 118, known 22, knew 14, knows 11, learned 6, perceived 6, aware 5, learn 3, knowing 2, learning 1 | none | 25 |
| H1847 דַּ֫עַת da.at "knowledge" | 84 | 2 | 84 | knowledge 81, know 3 | none | 32 |
| G1492G εἴδω eidō "to perceive: understand" | 39 | 0 | 21 | know 35, knows 2, knew 1, known 1 | none | 5 |
| H3046 יְדַע ye.da "to know" | 38 | 3 | 37 | known 13, know 12, make known 10, knew 1, knows 1, learn 1 | none | 7 |
| G1108 γνῶσις gnōsis "knowledge" | 28 | 0 | 27 | knowledge 27, knowing 1 | none | 10 |
| G1492I εἴδω eidō "to perceive: know" | 28 | 0 | 26 | knew 14, know 12, known 2 | none | 2 |
| G3129 μανθάνω manthanō "to learn" | 23 | 0 | 22 | learn 12, learned 9, learning 1, studied 1 | none | 0 |
| G1921 ἐπιγινώσκω epiginōskō "to come to know" | 20 | 0 | 18 | learned 4, recognize 4, know 3, known 3, knows 2, realized 2, knowing 1, perceived 1 | none | 0 |
| G1922 ἐπίγνωσις epignōsis "knowledge" | 19 | 0 | 19 | knowledge 19 | none | 5 |
| H3925H לָמַד la.mad "to learn: learn" | 18 | 2 | 20 | learn 16, learned 2 | none | 0 |
| H7200G רָאָה ra.ah "to see: see" | 17 | 0 | 17 | examine 17 | none | 0 |
| G1107 γνωρίζω gnōrizō "to make known" | 16 | 0 | 16 | made known 10, known 4, know 2 | none | 0 |
| G1110 γνωστός, γνώριμος gnōstos gnōrimos "acquainted with" | 12 | 0 | 12 | known 11, know 1 | none | 0 |
| G0050 ἀγνοέω agnoeō "be ignorant" | 11 | 2 | 12 | ignorant 4, not know 2, not recognize 2, ignorantly 1, not knowing 1, not recognized 1 | none | 1 |
| G1987 ἐπίσταμαι epistamai "to know/understand" | 11 | 0 | 11 | know 6, knowing 2, knew 1, knows 1, recognize 1 | none | 3 |
| H0995 בִּין bin "to understand" | 8 | 0 | 7 | perceived 3, learn 2, comprehended 1, discovered 1, examine 1 | none | 1 |
| H5234A נָכַר na.khar "to recognize" | 7 | 0 | 7 | recognize 3, know 1, knowing 1, known 1, knows 1 | none | 0 |
| H1844 דֵּעָה de.ah "knowledge" | 6 | 0 | 6 | knowledge 6 | none | 1 |
| H6622 פָּתַר pa.tar "to interpret" | 6 | 1 | 6 | can interpret 2, interpret 2, interpreted 2 | none | 2 |
| G5318 φανερός faneros "clear" | 5 | 0 | 5 | known 5 | none | 0 |
| H4093 מַדָּע mad.da "knowledge" | 5 | 0 | 5 | knowledge 3, learning 2 | none | 0 |
| G1329 διερμηνεύω diermēneuō "to interpret" | 4 | 0 | 4 | interpret 3, interpreted 1 | none | 0 |
| G1381 δοκιμάζω dokimazō "to test" | 4 | 0 | 3 | examine 2, interpret 2 | none | 0 |
| H5046 נָגַד na.gad "to tell" | 4 | 1 | 4 | made known 2, certainty 1, known 1 | none | 0 |
| H7200H רָאָה ra.ah "to see: examine" | 4 | 0 | 4 | perceived 2, learn 1, learned 1 | none | 0 |
| G4894 συνείδω suneidō "be aware" | 3 | 0 | 3 | knowledge 1, learned 1, realized 1 | none | 0 |
| H1875 דָּרַשׁ da.rash "to seek" | 3 | 0 | 3 | examine 1, studied 1, study 1 | none | 1 |
| G1121 γράμμα gramma "something written" | 2 | 0 | 2 | learning 2 | none | 0 |
| G1492H εἴδω eidō "to perceive: see" | 2 | 0 | 2 | know 1, knowing 1 | none | 0 |
| G2638 καταλαμβάνω katalambanō "to grasp" | 2 | 0 | 2 | comprehend 1, perceived 1 | none | 0 |
| G5319 φανερόω faneroō "to reveal" | 2 | 0 | 1 | known 2 | none | 0 |
| H1843 דֵּעַ de.a "knowledge" | 2 | 0 | 2 | knowledge 2 | none | 0 |
| H3948 לֶ֫קַח le.qach "teaching" | 2 | 0 | 2 | learning 2 | none | 0 |
| H4486 מַנְדַּע man.da "knowledge" | 2 | 0 | 2 | knowledge 2 | none | 0 |
| H8610 תָּפַשׂ ta.pha.s "to capture" | 2 | 0 | 2 | grasped 2 | none | 0 |
| G0056 ἀγνωσία agnōsia "ignorance" | 1 | 0 | 1 | no knowledge 1 | none | 0 |
| G0261 ἀμαθής amathēs "ignorant" | 1 | 0 | 1 | ignorant 1 | none | 0 |
| G0319 ἀναγνωρίζω anagnōrizō "to recognize" | 1 | 0 | 1 | known 1 | none | 0 |
| G0350 ἀνακρίνω anakrinō "to investigate" | 1 | 0 | 1 | examine 1 | none | 0 |
| G0426 ἀνετάζω anetazō "to question" | 1 | 0 | 1 | examine 1 | none | 0 |
| G0725 ἁρπαγμός harpagmos "something to grasp" | 1 | 0 | 1 | grasped 1 | none | 0 |
| G0803 ἀσφάλεια asfaleia "security" | 1 | 0 | 1 | certainty 1 | none | 0 |
| G0864 ἀφικνέομαι afikneomai "to reach" | 1 | 0 | 1 | known 1 | none | 0 |
| G1213 δηλόω dēloō "to make clear" | 1 | 0 | 1 | made known 1 | none | 0 |
| G1232 διαγνωρίζω diagnōrizō "to report" | 1 | 0 | 1 | made known 1 | none | 0 |
| G1252 διακρίνω diakrinō "to judge/doubt" | 1 | 0 | 1 | interpret 1 | none | 0 |
| G1328 διερμηνευτής diermēneutēs "interpreter" | 1 | 0 | 1 | interpret 1 | none | 0 |
| G1722 ἐν en "in/on/among" | 1 | 1 | 2 | known 1 | none | 0 |
| G1834 ἐξηγέομαι exēgeomai "to tell" | 1 | 0 | 1 | known 1 | none | 0 |
| G2467 ἴσημι isēmi "to know" | 1 | 0 | 1 | known 1 | none | 0 |
| G2657 κατανοέω katanoeō "to observe" | 1 | 0 | 1 | perceived 1 | none | 0 |
| G2919 κρίνω krinō "to judge" | 1 | 0 | 1 | concluded 1 | none | 0 |
| G3811 παιδεύω paideuō "to instruct" | 1 | 0 | 1 | learn 1 | none | 0 |
| G3985H πειράζω peirazō "to test/tempt: test" | 1 | 0 | 1 | examine 1 | none | 0 |
| G4160G ποιέω poieō "to do/make: do" | 1 | 0 | 1 | realized 1 | none | 0 |
| G4267 προγινώσκω proginōskō "to know/choose" | 1 | 0 | 1 | known 1 | none | 0 |
| G4441 πυνθάνομαι punthanomai "to inquire" | 1 | 0 | 1 | learned 1 | none | 0 |
| G6083 σύνοιδα sunoida "be conscious of" | 1 | 0 | 1 | aware 1 | none | 0 |
| H0413 אֶל el "to[wards]" | 1 | 7 | 8 | know 1 | none | 0 |
| H0502 אָלַף a.laph "to teach/learn" | 1 | 0 | 1 | learn 1 | none | 0 |
| H0816 אָשַׁם a.sham "be guilty" | 1 | 0 | 1 | realizes 1 | none | 1 |
| H2388H חָזַק cha.zaq "to strengthen: hold" | 1 | 0 | 1 | grasped 1 | none | 0 |
| H2713 חָקַר cha.qar "to search" | 1 | 0 | 1 | examine 1 | none | 0 |
| H3289 יָעַץ ya.ats "to advise" | 1 | 0 | 1 | know 1 | none | 0 |
| H3330 יַצִּיב yats.tsiv "certain" | 1 | 0 | 1 | certainty 1 | none | 0 |
| H3854 לַ֫הַג la.hag "study" | 1 | 0 | 1 | study 1 | none | 0 |
| H3925G לָמַד la.mad "to learn: teach" | 1 | 0 | 1 | learn 1 | none | 0 |
| H3943 לָפַת la.phat "to twist" | 1 | 0 | 1 | grasped 1 | none | 0 |
| H5869I עַ֫יִן a.yin "eye: appearance" | 1 | 0 | 1 | knowledge 1 | none | 0 |
| H6590 פְּשַׁר pe.shar "to interpret" | 1 | 0 | 1 | interpret 1 | none | 1 |
| H7919A שָׂכַל sa.khal "be prudent" | 1 | 0 | 1 | study 1 | none | 0 |
| H8085I שָׁמַע sha.ma "to hear: proclaim" | 1 | 0 | 1 | make known 1 | none | 0 |
| H8085J שָׁמַע sha.ma "to hear: understand" | 1 | 0 | 1 | comprehend 1 | none | 0 |
| H8454 תּוּשִׁיָּה tu.shiy.yah "wisdom" | 1 | 0 | 1 | sound knowledge 1 | none | 0 |
| G0302 ἄν an "if" | 0 | 1 | 1 |  | none | 0 |
| G0521 ἀπαίδευτος apaideutos "uninstructed" | 0 | 1 | 1 |  | none | 0 |
| G0782 ἀσπάζομαι aspazomai "to pay respects to" | 0 | 1 | 1 |  | none | 0 |
| G1161 δέ de "then" | 0 | 2 | 2 |  | none | 0 |
| G2532 καί kai "and" | 0 | 1 | 1 |  | none | 0 |
| G3670 ὁμολογέω homologeō "to confess/profess" | 0 | 1 | 1 |  | none | 0 |
| G3756 οὐ ou "no" | 0 | 2 | 2 |  | none | 0 |
| G5124 τοῦτο touto "that" | 0 | 2 | 2 |  | none | 0 |
| H0176A אוֹ o "or" | 0 | 2 | 2 |  | none | 0 |
| H0227A אָז az "then" | 0 | 1 | 1 |  | none | 0 |
| H0376G אִישׁ ish "man" | 0 | 1 | 1 |  | none | 0 |
| H0518A אִם im "if" | 0 | 1 | 1 |  | none | 0 |
| H0559 אָמַר a.mar "to say" | 0 | 1 | 1 |  | none | 0 |
| H0589 אֲנִי a.ni "I" | 0 | 1 | 1 |  | none | 0 |
| H0834A אֲשֶׁר a.sher "which" | 0 | 14 | 14 |  | none | 0 |
| H0853 אֵת et "[Obj.]" | 0 | 8 | 8 |  | none | 0 |
| H0854 אֵת et "with" | 0 | 1 | 1 |  | none | 0 |
| H0859A אַתָּ֫ה at.tah "you [m.s.]" | 0 | 3 | 3 |  | none | 0 |
| H0859D אַתֶּם at.tem "you [m.p.]" | 0 | 1 | 1 |  | none | 0 |
| H1768 דִּי di "that" | 0 | 6 | 6 |  | none | 0 |
| H1931 הוּא hu "he/she/it" | 0 | 11 | 11 |  | none | 0 |
| H1961 הָיָה ha.yah "to be" | 0 | 7 | 7 |  | none | 0 |
| H2009 הִנֵּה hin.neh "behold" | 0 | 1 | 1 |  | none | 0 |
| H2063 זֹאת zot "this" | 0 | 2 | 2 |  | none | 0 |
| H3318O יָצָא ya.tsa "to come out: speak" | 0 | 1 | 1 |  | none | 0 |
| H3426 יֵשׁ yesh "there" | 0 | 1 | 1 |  | none | 0 |
| H3588A כִּי ki "for" | 0 | 14 | 14 |  | none | 0 |
| H3808 לֹא lo "not" | 0 | 12 | 11 |  | none | 0 |
| H4616 מַ֫עַן ma.an "because" | 0 | 8 | 8 |  | none | 0 |
| H4672 מָצָא ma.tsa "to find" | 0 | 1 | 1 |  | none | 0 |
| H5668 עָבוּר a.vur "for the sake of" | 0 | 1 | 1 |  | none | 0 |
| H5750 עוֹד od "still" | 0 | 2 | 2 |  | none | 0 |
| H5921A עַל al "upon" | 0 | 1 | 1 |  | none | 0 |
| H7723G שָׁוְא shav "vanity: false" | 0 | 1 | 1 |  | none | 0 |
| H8033G שָׁם sham "there" | 0 | 1 | 1 |  | none | 0 |
| H8141 שָׁנָה sha.nah "year" | 0 | 1 | 1 |  | none | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.77.

### 3.1 H3045 יָדַע ya.da "to know": 795 own occurrences in 747 verses

- **Meaning as stored:** Hebrew; native word יָדַע, transliteration ya.da; STEP gloss "to know"; sense head "to know" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3045):** to know.
- **Related terms (21):** H1843 de.a "knowledge"; H1844 de.ah "knowledge"; H1845 de.u.el "Deuel"; H1847 da.at "knowledge"; H3037G yad.du.a "Jaddua"; H3037H yad.du.a "Jaddua"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 974; verses STEP attests 874; verse_lexical rows the parse found 946.

- **Carried by the member words:** know (555), known (101), knew (49), knows (49), knowledge (15), perceived (5), know how (4), learn (4), knowing (3), learned (3), certainty (2), acknowledged (1), aware (1), comprehend (1), discovered (1), know then (1).
- **Engagement of these occurrences:** none recorded 795.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 32:5 | acknowledged | HVhi1cs | none recorded | 13772 | 0 | I **acknowledged** my sin to you, and I did not cover my iniquity; I said, “I will confess my transgressions to the Lord,” and you forgave the iniquity of my sin. Selah |
| Song 6:12 | aware | HVqp1cs | none recorded | 15948 | 0 | Before I was **aware**, my desire set me among the chariots of my kinsman, a prince. |
| Jer 42:19 | certainty | HVqi2mp | none recorded | - | 0 | The Lord has said to you, O remnant of Judah, ‘Do not go to Egypt.’ Know for a **certainty** that I have warned you this day |
| Jer 42:22 | certainty | HVqi2mp | none recorded | - | 0 | Now therefore know for a **certainty** that you shall die by the sword, by famine, and by pestilence in the place where you desire to go to live.” |
| Job 37:5 | comprehend | HVqi1cp | none recorded | - | 0 | God thunders wondrously with his voice; he does great things that we cannot **comprehend**. |
| 1Sa 22:6 | discovered | HVNp3ms | none recorded | - | 0 | Now Saul heard that David was **discovered**, and the men who were with him. Saul was sitting at Gibeah under the tamarisk tree on the height with his spear in his hand, and all his servants were standing about him. |
| Gen 3:7 | knew | HVqw3mp | none recorded | 19189 | 0 | Then the eyes of both were opened, and they **knew** that they were naked. And they sewed fig leaves together and made themselves loincloths. |
| Gen 4:1 | knew | HVqp3ms | none recorded | - | 0 | Now Adam **knew** Eve his wife, and she conceived and bore Cain, saying, “I have gotten a man with the help of the Lord.” |
| Gen 4:17 | knew | HVqw3ms | none recorded | - | 0 | Cain **knew** his wife, and she conceived and bore Enoch. When he built a city, he called the name of the city after the name of his son, Enoch. |
| Gen 4:25 | knew | HVqw3ms | none recorded | - | 0 | And Adam **knew** his wife again, and she bore a son and called his name Seth, for she said, “ God has appointed for me another offspring instead of Abel, for Cain killed him.” |
| Gen 8:11 | knew | HVqw3ms | none recorded | - | 0 | And the dove came back to him in the evening, and behold, in her mouth was a freshly plucked olive leaf. So Noah **knew** that the waters had subsided from the earth. |
| Gen 9:24 | knew | HVqw3ms | none recorded | - | 0 | When Noah awoke from his wine and **knew** what his youngest son had done to him, |
| Gen 38:9 | knew | HVqw3ms | none recorded | - | 0 | But Onan **knew** that the offspring would not be his. So whenever he went in to his brother’s wife he would waste the semen on the ground, so as not to give offspring to his brother. |
| Exo 2:25 | knew | HVqw3ms | none recorded | - | 0 | God saw the people of Israel —and God **knew**. |
| Deu 7:15 | knew | HVqp2ms | none recorded | - | 0 | And the Lord will take away from you all sickness, and none of the evil diseases of Egypt, which you **knew**, will he inflict on you, but he will lay them on all who hate you. |
| Deu 9:24 | knew | HVqcc | none recorded | - | 0 | You have been rebellious against the Lord from the day that I **knew** you. |
| Deu 34:10 | knew | HVqp3ms | none recorded | - | 0 | And there has not arisen a prophet since in Israel like Moses, whom the Lord **knew** face to face, |
| Judg 19:25 | knew | HVqw3mp | none recorded | - | 0 | But the men would not listen to him. So the man seized his concubine and made her go out to them. And they **knew** her and abused her all night until the morning. And as the dawn began to break, they let her go. |
| 1Sa 1:19 | knew | HVqw3ms | none recorded | - | 0 | They rose early in the morning and worshiped before the Lord; then they went back to their house at Ramah. And Elkanah **knew** Hannah his wife, and the Lord remembered her. |
| 1Sa 3:13 | knew | HVqp3ms | none recorded | - | 0 | And I declare to him that I am about to punish his house forever, for the iniquity that he **knew**, because his sons were blaspheming God, and he did not restrain them. |
| 1Sa 3:20 | knew | HVqw3ms | none recorded | - | 0 | And all Israel from Dan to Beersheba **knew** that Samuel was established as a prophet of the Lord. |
| 1Sa 10:11 | knew | HVqrmsc | none recorded | - | 0 | And when all who **knew** him previously saw how he prophesied with the prophets, the people said to one another, “ What has come over the son of Kish? Is Saul also among the prophets?” |
| 1Sa 18:28 | knew | HVqw3ms | none recorded | - | 0 | But when Saul saw and **knew** that the Lord was with David, and that Michal, Saul’s daughter, loved him, |
| 1Sa 20:9 | knew | HVqaa | none recorded | - | 0 | And Jonathan said, “ Far be it from you! If I **knew** that it was determined by my father that harm should come to you, would I not tell you?” |
| 1Sa 20:33 | knew | HVqw3ms | none recorded | 14199 | 0 | But Saul hurled his spear at him to strike him. So Jonathan **knew** that his father was determined to put David to death. |
| 1Sa 20:39 | knew | HVqp3cp | none recorded | - | 0 | But the boy **knew** nothing. Only Jonathan and David knew the matter. |
| 1Sa 22:17 | knew | HVqp3cp | none recorded | - | 0 | And the king said to the guard who stood about him, “ Turn and kill the priests of the Lord, because their hand also is with David, and they **knew** that he fled and did not disclose it to me.” But the servants of the king would not put out their hand to strike the priests of the Lord. |
| 1Sa 22:22 | knew | HVqp1cs | none recorded | - | 0 | And David said to Abiathar, “I **knew** on that day, when Doeg the Edomite was there, that he would surely tell Saul. I have occasioned the death of all the persons of your father’s house. |
| 1Sa 23:9 | knew | HVqw3ms | none recorded | - | 0 | David **knew** that Saul was plotting harm against him. And he said to Abiathar the priest, “ Bring the ephod here.” |
| 1Sa 26:12 | knew | HVqrmsa | none recorded | - | 0 | So David took the spear and the jar of water from Saul’s head, and they went away. No man saw it or **knew** it, nor did any awake, for they were all asleep, because a deep sleep from the Lord had fallen upon them. |
| 1Sa 28:14 | knew | HVqw3ms | none recorded | - | 0 | He said to her, “ What is his appearance?” And she said, “An old man is coming up, and he is wrapped in a robe.” And Saul **knew** that it was Samuel, and he bowed with his face to the ground and paid homage. |
| 2Sa 5:12 | knew | HVqw3ms | none recorded | - | 0 | And David **knew** that the Lord had established him king over Israel, and that he had exalted his kingdom for the sake of his people Israel. |
| 2Sa 11:16 | knew | HVqp3ms | none recorded | - | 0 | And as Joab was besieging the city, he assigned Uriah to the place where he **knew** there were valiant men. |
| 2Sa 14:1 | knew | HVqw3ms | none recorded | 16741, 19931 | 0 | Now Joab the son of Zeruiah **knew** that the king’s heart went out to Absalom. |
| 2Sa 15:11 | knew | HVqp3cp | none recorded | - | 0 | With Absalom went two hundred men from Jerusalem who were invited guests, and they went in their innocence and **knew** nothing. |
| 1Ch 14:2 | knew | HVqw3ms | none recorded | - | 0 | And David **knew** that the Lord had established him as king over Israel, and that his kingdom was highly exalted for the sake of his people Israel. |
| 2Ch 33:13 | knew | HVqw3ms | none recorded | 14099, 14574, 15343 | 0 | He prayed to him, and God was moved by his entreaty and heard his plea and brought him again to Jerusalem into his kingdom. Then Manasseh **knew** that the Lord was God. |
| Neh 9:10 | knew | HVqp2ms | none recorded | 15130, 15146 | 0 | and performed signs and wonders against Pharaoh and all his servants and all the people of his land, for you **knew** that they acted arrogantly against our fathers. And you made a name for yourself, as it is to this day. |
| Est 1:13 | knew | HVqrmpc | none recorded | - | 0 | Then the king said to the wise men who **knew** the times (for this was the king’s procedure toward all who were versed in law and judgment, |
| Job 19:13 | knew | HVqrmpc | none recorded | - | 0 | “He has put my brothers far from me, and those who **knew** me are wholly estranged from me. |
| Job 20:20 | knew | HVqp3ms | none recorded | 17457 | 0 | “ Because he **knew** no contentment in his belly, he will not let anything in which he delights escape him. |
| Job 23:3 | knew | HVqp1cs | none recorded | - | 0 | Oh, that I **knew** where I might find him, that I might come even to his seat! |
| Ecc 4:13 | knew | HVqp3ms | none recorded | 18012 | 0 | Better was a poor and wise youth than an old and foolish king who no longer **knew** how to take advice. |
| Isa 48:7 | knew | HVqp1cs | none recorded | - | 0 | They are created now, not long ago; before today you have never heard of them, lest you should say, ‘ Behold, I **knew** them.’ |
| Isa 48:8 | knew | HVqp1cs | none recorded | - | 0 | You have never heard, you have never known, from of old your ear has not been opened. For I **knew** that you would surely deal treacherously, and that from before birth you were called a rebel. |
| Jer 1:5 | knew | HVqp1cs | none recorded | - | 0 | “ Before I formed you in the womb I **knew** you, and before you were born I consecrated you; I appointed you a prophet to the nations.” |
| Jer 11:18 | knew | HVqw1cs | none recorded | - | 0 | The Lord made it known to me and I **knew**; then you showed me their deeds. |
| Jer 32:8 | knew | HVqw1cs | none recorded | - | 0 | Then Hanamel my cousin came to me in the court of the guard, in accordance with the word of the Lord, and said to me, ‘ Buy my field that is at Anathoth in the land of Benjamin, for the right of possession and redemption is yours; buy it for yourself.’ Then I **knew** that this was the word of the Lord. |
| Jer 41:4 | knew | HVqp3ms | none recorded | - | 0 | On the day after the murder of Gedaliah, before anyone **knew** of it, |
| Jer 44:3 | knew | HVqp3cp | none recorded | - | 0 | because of the evil that they committed, provoking me to anger, in that they went to make offerings and serve other gods that they **knew** not, neither they, nor you, nor your fathers. |
| Jer 44:15 | knew | HVqrmpa | none recorded | - | 0 | Then all the men who **knew** that their wives had made offerings to other gods, and all the women who stood by, a great assembly, all the people who lived in Pathros in the land of Egypt, answered Jeremiah: |
| Eze 10:20 | knew | HVqw1cs | none recorded | - | 0 | These were the living creatures that I saw underneath the God of Israel by the Chebar canal; and I **knew** that they were cherubim. |
| Hos 13:5 | knew | HVqp1cs | none recorded | - | 0 | It was I who **knew** you in the wilderness, in the land of drought; |
| Jon 1:10 | knew | HVqp3cp | none recorded | - | 0 | Then the men were exceedingly afraid and said to him, “ What is this that you have done!” For the men **knew** that he was fleeing from the presence of the Lord, because he had told them. |
| Jon 4:2 | knew | HVqp1cs | none recorded | 13740, 14250 | 0 | And he prayed to the Lord and said, “ O Lord, is not this what I said when I was yet in my country? That is why I made haste to flee to Tarshish; for I **knew** that you are a gracious God and merciful, slow to anger and abounding in steadfast love, and relenting from disaster. |
| Gen 4:9 | know | HVqp1cs | none recorded | - | 0 | Then the Lord said to Cain, “ Where is Abel your brother?” He said, “I do not **know**; am I my brother’s keeper?” |
| Gen 12:11 | know | HVqp1cs | none recorded | - | 0 | When he was about to enter Egypt, he said to Sarai his wife, “ I **know** that you are a woman beautiful in appearance, |
| Gen 15:8 | know | HVqi1cs | none recorded | - | 0 | But he said, “O Lord God, how am I to **know** that I shall possess it?” |
| Gen 15:13 | know | HVqaa | none recorded | - | 0 | Then the Lord said to Abram, “ **Know** for certain that your offspring will be sojourners in a land that is not theirs and will be servants there, and they will be afflicted for four hundred years. |
| Gen 18:21 | know | HVqc1cs | none recorded | - | 0 | I will go down to see whether they have done altogether according to the outcry that has come to me. And if not, I will **know**.” |
| Gen 19:5 | know | HVqc1cp | none recorded | - | 0 | And they called to Lot, “ Where are the men who came to you tonight? Bring them out to us, that we may **know** them.” |
| Gen 19:33 | know | HVqp3ms | none recorded | - | 0 | So they made their father drink wine that night. And the firstborn went in and lay with her father. He did not **know** when she lay down or when she arose. |
| Gen 19:35 | know | HVqp3ms | none recorded | - | 0 | So they made their father drink wine that night also. And the younger arose and lay with him, and he did not **know** when she lay down or when she arose. |
| Gen 20:6 | know | HVqp1cs | none recorded | 16500 | 0 | Then God said to him in the dream, “ Yes, I **know** that you have done this in the integrity of your heart, and it was I who kept you from sinning against me. Therefore I did not let you touch her. |
| Gen 20:7 | know | HVqv2ms | none recorded | - | 0 | Now then, return the man’s wife, for he is a prophet, so that he will pray for you, and you shall live. But if you do not return her, **know** that you shall surely die, you and all who are yours.” |
| Gen 21:26 | know | HVqp1cs | none recorded | - | 0 | Abimelech said, “I do not **know** who has done this thing; you did not tell me, and I have not heard of it until today.” |
| Gen 22:12 | know | HVqp1cs | none recorded | - | 0 | He said, “Do not lay your hand on the boy or do anything to him, for now I **know** that you fear God, seeing you have not withheld your son, your only son, from me.” |
| Gen 24:14 | know | HVqi1cs | none recorded | - | 0 | Let the young woman to whom I shall say, ‘ Please let down your jar that I may drink,’ and who shall say, ‘ Drink, and I will water your camels ’—let her be the one whom you have appointed for your servant Isaac. By this I shall **know** that you have shown steadfast love to my master.” |
| Gen 27:2 | know | HVqp1cs | none recorded | - | 0 | He said, “ Behold, I am old; I do not **know** the day of my death. |
| Gen 28:16 | know | HVqp1cs | none recorded | - | 0 | Then Jacob awoke from his sleep and said, “ Surely the Lord is in this place, and I did not **know** it.” |
| Gen 29:5 | know | HVqp2mp | none recorded | - | 0 | He said to them, “Do you **know** Laban the son of Nahor?” They said, “We know him.” |
| Gen 29:5 | know | HVqp1cp | none recorded | - | 0 | He said to them, “Do you **know** Laban the son of Nahor?” They said, “We know him.” |
| Gen 30:26 | know | HVqp2ms | none recorded | - | 0 | Give me my wives and my children for whom I have served you, that I may go, for you **know** the service that I have given you.” |
| Gen 30:29 | know | HVqp2ms | none recorded | - | 0 | Jacob said to him, “ You yourself **know** how I have served you, and how your livestock has fared with me. |
| Gen 31:6 | know | HVqp2fp | none recorded | - | 0 | You **know** that I have served your father with all my strength, |
| Gen 31:32 | know | HVqp3ms | none recorded | - | 0 | Anyone with whom you find your gods shall not live. In the presence of our kinsmen point out what I have that is yours, and take it.” Now Jacob did not **know** that Rachel had stolen them. |
| Gen 38:16 | know | HVqp3ms | none recorded | - | 0 | He turned to her at the roadside and said, “ Come, let me come in to you,” for he did not **know** that she was his daughter-in-law. She said, “ What will you give me, that you may come in to me?” |
| Gen 42:23 | know | HVqp3cp | none recorded | - | 0 | They did not **know** that Joseph understood them, for there was an interpreter between them. |
| Gen 42:33 | know | HVqi1cs | none recorded | - | 0 | Then the man, the lord of the land, said to us, ‘ By this I shall **know** that you are honest men: leave one of your brothers with me, and take grain for the famine of your households, and go your way. |
| Gen 42:34 | know | HVqc1cs | none recorded | - | 0 | Bring your youngest brother to me. Then I shall **know** that you are not spies but honest men, and I will deliver your brother to you, and you shall trade in the land.’” |
| Gen 43:7 | know | HVqi1cp | none recorded | 20784, 20787, 20789, 20793, 20794, 20797, 20798, 20802, 20803, 20804, 20805 | 0 | They replied, “The man questioned us carefully about ourselves and our kindred, saying, ‘Is your father still alive? Do you have another brother?’ What we told him was in answer to these questions. Could we in any way **know** that he would say, ‘Bring your brother down ’?” |
| Gen 43:22 | know | HVqp1cp | none recorded | - | 0 | and we have brought other money down with us to buy food. We do not **know** who put our money in our sacks.” |
| Gen 44:15 | know | HVqp2mp | none recorded | - | 0 | Joseph said to them, “ What deed is this that you have done? Do you not **know** that a man like me can indeed practice divination?” |
| Gen 44:27 | know | HVqp2mp | none recorded | - | 0 | Then your servant my father said to us, ‘ You **know** that my wife bore me two sons. |
| Gen 47:6 | know | HVqp2ms | none recorded | - | 0 | The land of Egypt is before you. Settle your father and your brothers in the best of the land. Let them settle in the land of Goshen, and if you **know** any able men among them, put them in charge of my livestock.” |
| Gen 48:19 | know | HVqp1cs | none recorded | - | 0 | But his father refused and said, “I **know**, my son, I know. He also shall become a people, and he also shall be great. Nevertheless, his younger brother shall be greater than he, and his offspring shall become a multitude of nations.” |
| Gen 48:19 | know | HVqp1cs | none recorded | - | 0 | But his father refused and said, “I **know**, my son, I know. He also shall become a people, and he also shall be great. Nevertheless, his younger brother shall be greater than he, and his offspring shall become a multitude of nations.” |
| Exo 1:8 | know | HVqp3ms | none recorded | - | 0 | Now there arose a new king over Egypt, who did not **know** Joseph. |
| Exo 2:4 | know | HVqcc | none recorded | - | 0 | And his sister stood at a distance to **know** what would be done to him. |
| Exo 3:7 | know | HVqp1cs | none recorded | - | 0 | Then the Lord said, “I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters. I **know** their sufferings, |
| Exo 3:19 | know | HVqp1cs | none recorded | - | 0 | But I **know** that the king of Egypt will not let you go unless compelled by a mighty hand. |
| Exo 4:14 | know | HVqp1cs | none recorded | - | 0 | Then the anger of the Lord was kindled against Moses and he said, “Is there not Aaron, your brother, the Levite? I **know** that he can speak well. Behold, he is coming out to meet you, and when he sees you, he will be glad in his heart. |
| Exo 5:2 | know | HVqp1cs | none recorded | - | 0 | But Pharaoh said, “Who is the Lord, that I should obey his voice and let Israel go? I do not **know** the Lord, and moreover, I will not let Israel go.” |
| Exo 6:7 | know | HVqq2mp | none recorded | - | 0 | I will take you to be my people, and I will be your God, and you shall **know** that I am the Lord your God, who has brought you out from under the burdens of the Egyptians. |
| Exo 7:5 | know | HVqq3cp | none recorded | - | 0 | The Egyptians shall **know** that I am the Lord, when I stretch out my hand against Egypt and bring out the people of Israel from among them.” |
| Exo 7:17 | know | HVqi2ms | none recorded | - | 0 | Thus says the Lord, “ By this you shall **know** that I am the Lord: behold, with the staff that is in my hand I will strike the water that is in the Nile, and it shall turn into blood. |
| Exo 8:10 | know | HVqj2ms | none recorded | - | 0 | And he said, “ Tomorrow.” Moses said, “Be it as you say, so that you may **know** that there is no one like the Lord our God. |
| Exo 8:22 | know | HVqj2ms | none recorded | - | 0 | But on that day I will set apart the land of Goshen, where my people dwell, so that no swarms of flies shall be there, that you may **know** that I am the Lord in the midst of the earth. |
| Exo 9:14 | know | HVqj2ms | none recorded | - | 0 | For this time I will send all my plagues on you yourself, and on your servants and your people, so that you may **know** that there is none like me in all the earth. |
| Exo 9:29 | know | HVqj2ms | none recorded | - | 0 | Moses said to him, “ As soon as I have gone out of the city, I will stretch out my hands to the Lord. The thunder will cease, and there will be no more hail, so that you may **know** that the earth is the Lord’s. |
| Exo 9:30 | know | HVqp1cs | none recorded | - | 0 | But as for you and your servants, I **know** that you do not yet fear the Lord God.” |
| Exo 10:2 | know | HVqq2mp | none recorded | - | 0 | and that you may tell in the hearing of your son and of your grandson how I have dealt harshly with the Egyptians and what signs I have done among them, that you may **know** that I am the Lord.” |
| Exo 10:26 | know | HVqi1cp | none recorded | - | 0 | Our livestock also must go with us; not a hoof shall be left behind, for we must take of them to serve the Lord our God, and we do not **know** with what we must serve the Lord until we arrive there.” |
| Exo 11:7 | know | HVqj2mp | none recorded | - | 0 | But not a dog shall growl against any of the people of Israel, either man or beast, that you may **know** that the Lord makes a distinction between Egypt and Israel.’ |
| Exo 14:4 | know | HVqq3cp | none recorded | - | 0 | And I will harden Pharaoh’s heart, and he will pursue them, and I will get glory over Pharaoh and all his host, and the Egyptians shall **know** that I am the Lord.” And they did so. |
| Exo 14:18 | know | HVqq3cp | none recorded | - | 0 | And the Egyptians shall **know** that I am the Lord, when I have gotten glory over Pharaoh, his chariots, and his horsemen.” |
| Exo 16:6 | know | HVqq2mp | none recorded | - | 0 | So Moses and Aaron said to all the people of Israel, “At evening you shall **know** that it was the Lord who brought you out of the land of Egypt, |
| Exo 16:12 | know | HVqq2mp | none recorded | - | 0 | “I have heard the grumbling of the people of Israel. Say to them, ‘ At twilight you shall eat meat, and in the morning you shall be filled with bread. Then you shall **know** that I am the Lord your God.’” |
| Exo 16:15 | know | HVqp3cp | none recorded | - | 0 | When the people of Israel saw it, they said to one another, “What is it?” For they did not **know** what it was. And Moses said to them, “It is the bread that the Lord has given you to eat. |
| Exo 18:11 | know | HVqp1cs | none recorded | 15130, 15146 | 0 | Now I **know** that the Lord is greater than all gods, because in this affair they dealt arrogantly with the people.” |
| Exo 18:16 | know | HVhq1cs | none recorded | - | 0 | when they have a dispute, they come to me and I decide between one person and another, and I make them **know** the statutes of God and his laws.” |
| Exo 18:20 | know | HVhq2ms | none recorded | - | 0 | and you shall warn them about the statutes and the laws, and make them **know** the way in which they must walk and what they must do. |
| Exo 23:9 | know | HVqp2mp | none recorded | 15928, 17279 | 0 | “You shall not oppress a sojourner. You **know** the heart of a sojourner, for you were sojourners in the land of Egypt. |
| Exo 29:46 | know | HVqq3cp | none recorded | - | 0 | And they shall **know** that I am the Lord their God, who brought them out of the land of Egypt that I might dwell among them. I am the Lord their God. |
| Exo 31:13 | know | HVqcc | none recorded | - | 0 | “ You are to speak to the people of Israel and say, ‘Above all you shall keep my Sabbaths, for this is a sign between me and you throughout your generations, that you may **know** that I, the Lord, sanctify you. |
| Exo 32:1 | know | HVqp1cp | none recorded | - | 0 | When the people saw that Moses delayed to come down from the mountain, the people gathered themselves together to Aaron and said to him, “ Up, make us gods who shall go before us. As for this Moses, the man who brought us up out of the land of Egypt, we do not **know** what has become of him.” |
| Exo 32:22 | know | HVqp2ms | none recorded | 14239 | 0 | And Aaron said, “Let not the anger of my lord burn hot. You **know** the people, that they are set on evil. |
| Exo 32:23 | know | HVqp1cp | none recorded | 14239 | 0 | For they said to me, ‘ Make us gods who shall go before us. As for this Moses, the man who brought us up out of the land of Egypt, we do not **know** what has become of him.’ |
| Exo 33:5 | know | HVqc1cs | none recorded | - | 0 | For the Lord had said to Moses, “ Say to the people of Israel, ‘You are a stiff-necked people; if for a single moment I should go up among you, I would consume you. So now take off your ornaments, that I may **know** what to do with you.’” |
| Exo 33:12 | know | HVhp2ms | none recorded | - | 0 | Moses said to the Lord, “ See, you say to me, ‘Bring up this people,’ but you have not let me **know** whom you will send with me. Yet you have said, ‘I know you by name, and you have also found favor in my sight.’ |
| Exo 33:12 | know | HVqp1cs | none recorded | - | 0 | Moses said to the Lord, “ See, you say to me, ‘Bring up this people,’ but you have not let me **know** whom you will send with me. Yet you have said, ‘I know you by name, and you have also found favor in my sight.’ |
| Exo 33:13 | know | HVqc1cs | none recorded | - | 0 | Now therefore, if I have found favor in your sight, please show me now your ways, that I may **know** you in order to find favor in your sight. Consider too that this nation is your people.” |
| Exo 33:17 | know | HVqw1cs | none recorded | - | 0 | And the Lord said to Moses, “ This very thing that you have spoken I will do, for you have found favor in my sight, and I **know** you by name.” |
| Exo 34:29 | know | HVqp3ms | none recorded | - | 0 | When Moses came down from Mount Sinai, with the two tablets of the testimony in his hand as he came down from the mountain, Moses did not **know** that the skin of his face shone because he had been talking with God. |
| Exo 36:1 | know | HVqcc | none recorded | - | 0 | “ Bezalel and Oholiab and every craftsman in whom the Lord has put skill and intelligence to **know** how to do any work in the construction of the sanctuary shall work in accordance with all that the Lord has commanded.” |
| Lev 5:1 | know | HVqp3ms | none recorded | - | 0 | “If anyone sins in that he hears a public adjuration to testify, and though he is a witness, whether he has seen or come to **know** the matter, yet does not speak, he shall bear his iniquity; |
| Lev 5:3 | know | HVqp3ms | none recorded | - | 0 | or if he touches human uncleanness, of whatever sort the uncleanness may be with which one becomes unclean, and it is hidden from him, when he comes to **know** it, and realizes his guilt; |
| Lev 5:4 | know | HVqp3ms | none recorded | 16562 | 0 | or if anyone utters with his lips a rash oath to do evil or to do good, any sort of rash oath that people swear, and it is hidden from him, when he comes to **know** it, and he realizes his guilt in any of these; |
| Lev 5:17 | know | HVqp3ms | none recorded | 16562 | 0 | “ If anyone sins, doing any of the things that by the Lord’s commandments ought not to be done, though he did not **know** it, then realizes his guilt, he shall bear his iniquity. |
| Lev 23:43 | know | HVqj3mp | none recorded | - | 0 | that your generations may **know** that I made the people of Israel dwell in booths when I brought them out of the land of Egypt: I am the Lord your God.” |
| Num 10:31 | know | HVqp2ms | none recorded | - | 0 | And he said, “ Please do not leave us, for you **know** where we should camp in the wilderness, and you will serve as eyes for us. |
| Num 11:16 | know | HVqp2ms | none recorded | - | 0 | Then the Lord said to Moses, “ Gather for me seventy men of the elders of Israel, whom you **know** to be the elders of the people and officers over them, and bring them to the tent of meeting, and let them take their stand there with you. |
| Num 14:31 | know | HVqq3cp | none recorded | - | 0 | But your little ones, who you said would become a prey, I will bring in, and they shall **know** the land that you have rejected. |
| Num 14:34 | know | HVqq2mp | none recorded | - | 0 | According to the number of the days in which you spied out the land, forty days, a year for each day, you shall bear your iniquity forty years, and you shall **know** my displeasure.’ |
| Num 16:28 | know | HVqi2mp | none recorded | - | 0 | And Moses said, “ Hereby you shall **know** that the Lord has sent me to do all these works, and that it has not been of my own accord. |
| Num 16:30 | know | HVqq2mp | none recorded | 18633 | 0 | But if the Lord creates something new, and the ground opens its mouth and swallows them up with all that belongs to them, and they go down alive into Sheol, then you shall **know** that these men have despised the Lord.” |
| Num 20:14 | know | HVqp2ms | none recorded | - | 0 | Moses sent messengers from Kadesh to the king of Edom: “ Thus says your brother Israel: You **know** all the hardship that we have met: |
| Num 22:6 | know | HVqp1cs | none recorded | - | 0 | Come now, curse this people for me, since they are too mighty for me. Perhaps I shall be able to defeat them and drive them from the land, for I **know** that he whom you bless is blessed, and he whom you curse is cursed.” |
| Num 22:19 | know | HVqc1cs | none recorded | - | 0 | So you, too, please stay here tonight, that I may **know** what more the Lord will say to me.” |
| Num 22:34 | know | HVqp1cs | none recorded | - | 0 | Then Balaam said to the angel of the Lord, “I have sinned, for I did not **know** that you stood in the road against me. Now therefore, if it is evil in your sight, I will turn back.” |
| Deu 3:19 | know | HVqp1cs | none recorded | - | 0 | Only your wives, your little ones, and your livestock (I **know** that you have much livestock ) shall remain in the cities that I have given you, |
| Deu 4:35 | know | HVqcc | none recorded | 12676 | 0 | To you it was shown, that you might **know** that the Lord is God; there is no other besides him. |
| Deu 4:39 | know | HVqq2ms | none recorded | 15939 | 0 | **know** therefore today, and lay it to your heart, that the Lord is God in heaven above and on the earth beneath; there is no other. |
| Deu 7:9 | know | HVqq2ms | none recorded | - | 0 | **Know** therefore that the Lord your God is God, the faithful God who keeps covenant and steadfast love with those who love him and keep his commandments, to a thousand generations, |
| Deu 8:2 | know | HVqcc | none recorded | 15345, 15923, 15944, 16371, 16397 | 0 | And you shall remember the whole way that the Lord your God has led you these forty years in the wilderness, that he might humble you, testing you to **know** what was in your heart, whether you would keep his commandments or not. |
| Deu 8:3 | know | HVqp2ms | none recorded | 15345 | 0 | And he humbled you and let you hunger and fed you with manna, which you did not **know**, nor did your fathers know, that he might make you know that man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| Deu 8:3 | know | HVqp3cp | none recorded | - | 0 | And he humbled you and let you hunger and fed you with manna, which you did not **know**, nor did your fathers know, that he might make you know that man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| Deu 8:3 | know | HVhcc | none recorded | - | 0 | And he humbled you and let you hunger and fed you with manna, which you did not **know**, nor did your fathers know, that he might make you know that man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| Deu 8:16 | know | HVqp3cp | none recorded | 15345 | 0 | who fed you in the wilderness with manna that your fathers did not **know**, that he might humble you and test you, to do you good in the end. |
| Deu 9:2 | know | HVqp2ms | none recorded | - | 0 | a people great and tall, the sons of the Anakim, whom you **know**, and of whom you have heard it said, ‘ Who can stand before the sons of Anak?’ |
| Deu 9:3 | know | HVqq2ms | none recorded | - | 0 | **Know** therefore today that he who goes over before you as a consuming fire is the Lord your God. He will destroy them and subdue them before you. So you shall drive them out and make them perish quickly, as the Lord has promised you. |
| Deu 9:6 | know | HVqq2ms | none recorded | - | 0 | “ **Know**, therefore, that the Lord your God is not giving you this good land to possess because of your righteousness, for you are a stubborn people. |
| Deu 13:3 | know | HVqcc | none recorded | 15944, 16397 | 0 | you shall not listen to the words of that prophet or that dreamer of dreams. For the Lord your God is testing you, to **know** whether you love the Lord your God with all your heart and with all your soul. |
| Deu 18:21 | know | HVqi1cp | none recorded | - | 0 | And if you say in your heart, ‘ How may we **know** the word that the Lord has not spoken?’— |
| Deu 20:20 | know | HVqi2ms | none recorded | - | 0 | Only the trees that you **know** are not trees for food you may destroy and cut down, that you may build siegeworks against the city that makes war with you, until it falls. |
| Deu 22:2 | know | HVqp2ms | none recorded | - | 0 | And if he does not live near you and you do not **know** who he is, you shall bring it home to your house, and it shall stay with you until your brother seeks it. Then you shall restore it to him. |
| Deu 29:6 | know | HVqj2mp | none recorded | - | 0 | You have not eaten bread, and you have not drunk wine or strong drink, that you may **know** that I am the Lord your God. |
| Deu 29:16 | know | HVqp2mp | none recorded | - | 0 | “ You **know** how we lived in the land of Egypt, and how we came through the midst of the nations through which you passed. |
| Deu 31:21 | know | HVqp1cs | none recorded | 20003 | 0 | And when many evils and troubles have come upon them, this song shall confront them as a witness ( for it will live unforgotten in the mouths of their offspring ). For I **know** what they are inclined to do even today, before I have brought them into the land that I swore to give.” |
| Deu 31:27 | know | HVqp1cs | none recorded | 13888, 14065, 14522 | 0 | For I **know** how rebellious and stubborn you are. Behold, even today while I am yet alive with you, you have been rebellious against the Lord. How much more after my death! |
| Deu 31:29 | know | HVqp1cs | none recorded | 13888 | 0 | For I **know** that after my death you will surely act corruptly and turn aside from the way that I have commanded you. And in the days to come evil will befall you, because you will do what is evil in the sight of the Lord, provoking him to anger through the work of your hands.” |
| Jos 2:4 | know | HVqp1cs | none recorded | - | 0 | But the woman had taken the two men and hidden them. And she said, “ True, the men came to me, but I did not **know** where they were from. |
| Jos 2:5 | know | HVqp1cs | none recorded | - | 0 | And when the gate was about to be closed at dark, the men went out. I do not **know** where the men went. Pursue them quickly, for you will overtake them.” |
| Jos 2:9 | know | HVqp1cs | none recorded | 12703 | 0 | and said to the men, “I **know** that the Lord has given you the land, and that the fear of you has fallen upon us, and that all the inhabitants of the land melt away before you. |
| Jos 3:4 | know | HVqj2mp | none recorded | - | 0 | Yet there shall be a distance between you and it, about 2,000 cubits in length. Do not come near it, in order that you may **know** the way you shall go, for you have not passed this way before.” |
| Jos 3:7 | know | HVqi3mp | none recorded | - | 0 | The Lord said to Joshua, “ Today I will begin to exalt you in the sight of all Israel, that they may **know** that, as I was with Moses, so I will be with you. |
| Jos 3:10 | know | HVqi2mp | none recorded | - | 0 | And Joshua said, “ Here is how you shall **know** that the living God is among you and that he will without fail drive out from before you the Canaanites, the Hittites, the Hivites, the Perizzites, the Girgashites, the Amorites, and the Jebusites. |
| Jos 4:22 | know | HVhq2mp | none recorded | - | 0 | then you shall let your children **know**, ‘ Israel passed over this Jordan on dry ground.’ |
| Jos 4:24 | know | HVqcc | none recorded | - | 0 | so that all the peoples of the earth may **know** that the hand of the Lord is mighty, that you may fear the Lord your God forever.” |
| Jos 8:14 | know | HVqp3ms | none recorded | - | 0 | And as soon as the king of Ai saw this, he and all his people, the men of the city, hurried and went out early to the appointed place toward the Arabah to meet Israel in battle. But he did not **know** that there was an ambush against him behind the city. |
| Jos 14:6 | know | HVqp2ms | none recorded | - | 0 | Then the people of Judah came to Joshua at Gilgal. And Caleb the son of Jephunneh the Kenizzite said to him, “ You **know** what the Lord said to Moses the man of God in Kadesh-barnea concerning you and me. |
| Jos 22:22 | know | HVqi3ms | none recorded | 14090, 14557 | 0 | “The Mighty One, God, the Lord! The Mighty One, God, the Lord! He knows; and let Israel itself **know**! If it was in rebellion or in breach of faith against the Lord, do not spare us today |
| Jos 22:31 | know | HVqp1cp | none recorded | - | 0 | And Phinehas the son of Eleazar the priest said to the people of Reuben and the people of Gad and the people of Manasseh, “ Today we **know** that the Lord is in our midst, because you have not committed this breach of faith against the Lord. Now you have delivered the people of Israel from the hand of the Lord.” |
| Jos 23:13 | know | HVqaa | none recorded | - | 0 | **know** for certain that the Lord your God will no longer drive out these nations before you, but they shall be a snare and a trap for you, a whip on your sides and thorns in your eyes, until you perish from off this good ground that the Lord your God has given you. |
| Jos 23:14 | know | HVqq2mp | none recorded | 14067, 14070, 14523, 14525, 15939, 17272, 18137 | 0 | “And now I am about to go the way of all the earth, and you **know** in your hearts and souls, all of you, that not one word has failed of all the good things that the Lord your God promised concerning you. All have come to pass for you; not one of them has failed. |
| Judg 2:10 | know | HVqp3cp | none recorded | 14523 | 0 | And all that generation also were gathered to their fathers. And there arose another generation after them who did not **know** the Lord or the work that he had done for Israel. |
| Judg 3:2 | know | HVqcc | none recorded | - | 0 | It was only in order that the generations of the people of Israel might **know** war, to teach war to those who had not known it before. |
| Judg 3:4 | know | HVqcc | none recorded | - | 0 | They were for the testing of Israel, to **know** whether Israel would obey the commandments of the Lord, which he commanded their fathers by the hand of Moses. |
| Judg 6:37 | know | HVqq1cs | none recorded | - | 0 | behold, I am laying a fleece of wool on the threshing floor. If there is dew on the fleece alone, and it is dry on all the ground, then I shall **know** that you will save Israel by my hand, as you have said.” |
| Judg 13:16 | know | HVqp3ms | none recorded | - | 0 | And the angel of the Lord said to Manoah, “If you detain me, I will not eat of your food. But if you prepare a burnt offering, then offer it to the Lord.” (For Manoah did not **know** that he was the angel of the Lord.) |
| Judg 14:4 | know | HVqp3cp | none recorded | - | 0 | His father and mother did not **know** that it was from the Lord, for he was seeking an opportunity against the Philistines. At that time the Philistines ruled over Israel. |
| Judg 15:11 | know | HVqp2ms | none recorded | 19139 | 0 | Then 3,000 men of Judah went down to the cleft of the rock of Etam, and said to Samson, “Do you not **know** that the Philistines are rulers over us? What then is this that you have done to us?” And he said to them, “ As they did to me, so have I done to them.” |
| Judg 16:20 | know | HVqp3ms | none recorded | - | 0 | And she said, “The Philistines are upon you, Samson!” And he awoke from his sleep and said, “I will go out as at other times and shake myself free.” But he did not **know** that the Lord had left him. |
| Judg 17:13 | know | HVqp1cs | none recorded | - | 0 | Then Micah said, “ Now I **know** that the Lord will prosper me, because I have a Levite as priest.” |
| Judg 18:5 | know | HVqc1cp | none recorded | 21254, 21256, 21258, 21260, 21261, 21263, 21264, 21266 | 0 | And they said to him, “ Inquire of God, please, that we may **know** whether the journey on which we are setting out will succeed.” |
| Judg 18:14 | know | HVqp2mp | none recorded | - | 0 | Then the five men who had gone to scout out the country of Laish said to their brothers, “Do you **know** that in these houses there are an ephod, household gods, a carved image, and a metal image? Now therefore consider what you will do.” |
| Judg 19:22 | know | HVqu1cp | none recorded | 15938 | 0 | As they were making their hearts merry, behold, the men of the city, worthless fellows, surrounded the house, beating on the door. And they said to the old man, the master of the house, “ Bring out the man who came into your house, that we may **know** him.” |
| Judg 20:34 | know | HVqp3cp | none recorded | - | 0 | And there came against Gibeah 10,000 chosen men out of all Israel, and the battle was hard, but the Benjaminites did not **know** that disaster was close upon them. |
| Rut 2:11 | know | HVqp2fs | none recorded | - | 0 | But Boaz answered her, “ All that you have done for your mother-in-law since the death of your husband has been fully told to me, and how you left your father and mother and your native land and came to a people that you did not **know** before. |
| Rut 3:11 | know | HVqrmsa | none recorded | - | 0 | And now, my daughter, do not fear. I will do for you all that you ask, for all my fellow townsmen **know** that you are a worthy woman. |
| Rut 4:4 | know | HVqc1cs | none recorded | - | 0 | So I thought I would tell you of it and say, ‘ Buy it in the presence of those sitting here and in the presence of the elders of my people.’ If you will redeem it, redeem it. But if you will not, tell me, that I may **know**, for there is no one besides you to redeem it, and I come after you.” And he said, “ I will redeem it.” |
| 1Sa 2:12 | know | HVqp3cp | none recorded | - | 0 | Now the sons of Eli were worthless men. They did not **know** the Lord. |
| 1Sa 3:7 | know | HVqp3ms | none recorded | 17816 | 0 | Now Samuel did not yet **know** the Lord, and the word of the Lord had not yet been revealed to him. |
| 1Sa 6:9 | know | HVqq1cp | none recorded | - | 0 | and watch. If it goes up on the way to its own land, to Beth-shemesh, then it is he who has done us this great harm, but if not, then we shall **know** that it is not his hand that struck us; it happened to us by coincidence.” |
| 1Sa 12:17 | know | HVqv2mp | none recorded | - | 0 | Is it not wheat harvest today? I will call upon the Lord, that he may send thunder and rain. And you shall **know** and see that your wickedness is great, which you have done in the sight of the Lord, in asking for yourselves a king.” |
| 1Sa 14:3 | know | HVqp3ms | none recorded | - | 0 | including Ahijah the son of Ahitub, Ichabod’s brother, son of Phinehas, son of Eli, the priest of the Lord in Shiloh, wearing an ephod. And the people did not **know** that Jonathan had gone. |
| 1Sa 14:38 | know | HVqv2mp | none recorded | - | 0 | And Saul said, “ Come here, all you leaders of the people, and **know** and see how this sin has arisen today. |
| 1Sa 17:28 | know | HVqp1cs | none recorded | 14271, 15121, 15315, 16559, 16706 | 0 | Now Eliab his eldest brother heard when he spoke to the men. And Eliab’s anger was kindled against David, and he said, “ Why have you come down? And with whom have you left those few sheep in the wilderness? I **know** your presumption and the evil of your heart, for you have come down to see the battle.” |
| 1Sa 17:46 | know | HVqu3mp | none recorded | - | 0 | This day the Lord will deliver you into my hand, and I will strike you down and cut off your head. And I will give the dead bodies of the host of the Philistines this day to the birds of the air and to the wild beasts of the earth, that all the earth may **know** that there is a God in Israel, |
| 1Sa 17:47 | know | HVqu3mp | none recorded | - | 0 | and that all this assembly may **know** that the Lord saves not with sword and spear. For the battle is the Lord’s, and he will give you into our hand.” |
| 1Sa 17:55 | know | HVqp1cs | none recorded | 16079, 16080, 16858 | 0 | As soon as Saul saw David go out against the Philistine, he said to Abner, the commander of the army, “ Abner, whose son is this youth?” And Abner said, “As your soul lives, O king, I do not **know**.” |
| 1Sa 20:3 | know | HVqj3ms | none recorded | - | 0 | But David vowed again, saying, “Your father knows well that I have found favor in your eyes, and he thinks, ‘Do not let Jonathan **know** this, lest he be grieved.’ But truly, as the Lord lives and as your soul lives, there is but a step between me and death.” |
| 1Sa 20:7 | know | HVqv2ms | none recorded | 13480, 14199 | 0 | If he says, ‘ Good!’ it will be well with your servant, but if he is angry, then **know** that harm is determined by him. |
| 1Sa 20:30 | know | HVqp1cs | none recorded | 14271, 19742, 19941 | 0 | Then Saul’s anger was kindled against Jonathan, and he said to him, “You son of a perverse, rebellious woman, do I not **know** that you have chosen the son of Jesse to your own shame, and to the shame of your mother’s nakedness? |
| 1Sa 21:2 | know | HVqj3ms | none recorded | - | 0 | And David said to Ahimelech the priest, “The king has charged me with a matter and said to me, ‘Let no one **know** anything of the matter about which I send you, and with which I have charged you.’ I have made an appointment with the young men for such and such a place. |
| 1Sa 22:3 | know | HVqi1cs | none recorded | - | 0 | And David went from there to Mizpeh of Moab. And he said to the king of Moab, “ Please let my father and my mother stay with you, till I **know** what God will do for me.” |
| 1Sa 23:22 | know | HVqv2mp | none recorded | - | 0 | Go, make yet more sure. **Know** and see the place where his foot is, and who has seen him there, for it is told me that he is very cunning. |
| 1Sa 24:11 | know | HVqv2ms | none recorded | - | 0 | See, my father, see the corner of your robe in my hand. For by the fact that I cut off the corner of your robe and did not kill you, you may **know** and see that there is no wrong or treason in my hands. I have not sinned against you, though you hunt my life to take it. |
| 1Sa 24:20 | know | HVqp1cs | none recorded | - | 0 | And now, behold, I **know** that you shall surely be king, and that the kingdom of Israel shall be established in your hand. |
| 1Sa 25:11 | know | HVqp1cs | none recorded | - | 0 | Shall I take my bread and my water and my meat that I have killed for my shearers and give it to men who come from I do not **know** where?” |
| 1Sa 25:17 | know | HVqv2fs | none recorded | - | 0 | Now therefore **know** this and consider what you should do, for harm is determined against our master and against all his house, and he is such a worthless man that one cannot speak to him.” |
| 1Sa 28:2 | know | HVqi2ms | none recorded | - | 0 | David said to Achish, “Very well, you shall **know** what your servant can do.” And Achish said to David, “Very well, I will make you my bodyguard for life.” |
| 1Sa 28:9 | know | HVqp2ms | none recorded | - | 0 | The woman said to him, “ Surely you **know** what Saul has done, how he has cut off the mediums and the necromancers from the land. Why then are you laying a trap for my life to bring about my death?” |
| 1Sa 29:9 | know | HVqp1cs | none recorded | - | 0 | And Achish answered David and said, “I **know** that you are as blameless in my sight as an angel of God. Nevertheless, the commanders of the Philistines have said, ‘He shall not go up with us to the battle.’ |
| 2Sa 1:5 | know | HVqp2ms | none recorded | - | 0 | Then David said to the young man who told him, “ How do you **know** that Saul and his son Jonathan are dead?” |
| 2Sa 2:26 | know | HVqp2ms | none recorded | - | 0 | Then Abner called to Joab, “Shall the sword devour forever? Do you not **know** that the end will be bitter? How long will it be before you tell your people to turn from the pursuit of their brothers?” |
| 2Sa 3:25 | know | HVqp2ms | none recorded | - | 0 | You **know** that Abner the son of Ner came to deceive you and to know your going out and your coming in, and to know all that you are doing.” |
| 2Sa 3:25 | know | HVqcc | none recorded | - | 0 | You **know** that Abner the son of Ner came to deceive you and to know your going out and your coming in, and to know all that you are doing.” |
| 2Sa 3:25 | know | HVqcc | none recorded | - | 0 | You **know** that Abner the son of Ner came to deceive you and to know your going out and your coming in, and to know all that you are doing.” |
| 2Sa 3:26 | know | HVqp3ms | none recorded | - | 0 | When Joab came out from David’s presence, he sent messengers after Abner, and they brought him back from the cistern of Sirah. But David did not **know** about it. |
| 2Sa 3:38 | know | HVqi2mp | none recorded | - | 0 | And the king said to his servants, “Do you not **know** that a prince and a great man has fallen this day in Israel? |
| 2Sa 7:20 | know | HVqp2ms | none recorded | - | 0 | And what more can David say to you? For you **know** your servant, O Lord God! |
| 2Sa 11:20 | know | HVqp2mp | none recorded | 14199 | 0 | then, if the king’s anger rises, and if he says to you, ‘ Why did you go so near the city to fight? Did you not **know** that they would shoot from the wall? |
| 2Sa 14:20 | know | HVqcc | none recorded | - | 0 | In order to change the course of things your servant Joab did this. But my lord has wisdom like the wisdom of the angel of God to **know** all things that are on the earth.” |
| 2Sa 17:8 | know | HVqp2ms | none recorded | - | 0 | Hushai said, “ You **know** that your father and his men are mighty men, and that they are enraged, like a bear robbed of her cubs in the field. Besides, your father is expert in war; he will not spend the night with the people. |
| 2Sa 18:29 | know | HVqp1cs | none recorded | - | 0 | And the king said, “Is it well with the young man Absalom?” Ahimaaz answered, “When Joab sent the king’s servant, your servant, I saw a great commotion, but I do not **know** what it was.” |
| 2Sa 19:6 | know | HVqp1cs | none recorded | - | 0 | because you love those who hate you and hate those who love you. For you have made it clear today that commanders and servants are nothing to you, for today I **know** that if Absalom were alive and all of us were dead today, then you would be pleased. |
| 2Sa 19:22 | know | HVqp1cs | none recorded | - | 0 | But David said, “ What have I to do with you, you sons of Zeruiah, that you should this day be as an adversary to me? Shall anyone be put to death in Israel this day? For do I not **know** that I am this day king over Israel?” |
| 2Sa 24:2 | know | HVqq1cs | none recorded | - | 0 | So the king said to Joab, the commander of the army, who was with him, “Go through all the tribes of Israel, from Dan to Beersheba, and number the people, that I may **know** the number of the people.” |
| 1Ki 1:11 | know | HVqp3ms | none recorded | - | 0 | Then Nathan said to Bathsheba the mother of Solomon, “Have you not heard that Adonijah the son of Haggith has become king and David our lord does not **know** it? |
| 1Ki 1:18 | know | HVqp2ms | none recorded | - | 0 | And now, behold, Adonijah is king, although you, my lord the king, do not **know** it. |
| 1Ki 2:5 | know | HVqp2ms | none recorded | - | 0 | “Moreover, you also **know** what Joab the son of Zeruiah did to me, how he dealt with the two commanders of the armies of Israel, Abner the son of Ner, and Amasa the son of Jether, whom he killed, avenging in time of peace for blood that had been shed in war, and putting the blood of war on the belt around his waist and on the sandals on his feet. |
| 1Ki 2:9 | know | HVqq2ms | none recorded | - | 0 | Now therefore do not hold him guiltless, for you are a wise man. You will **know** what you ought to do to him, and you shall bring his gray head down with blood to Sheol.” |
| 1Ki 2:15 | know | HVqp2fs | none recorded | 18094, 18218 | 0 | He said, “ You **know** that the kingdom was mine, and that all Israel fully expected me to reign. However, the kingdom has turned about and become my brother’s, for it was his from the Lord. |
| 1Ki 2:37 | know | HVqaa | none recorded | - | 0 | For on the day you go out and cross the brook Kidron, **know** for certain that you shall die. Your blood shall be on your own head.” |
| 1Ki 2:42 | know | HVqaa | none recorded | 18225 | 0 | the king sent and summoned Shimei and said to him, “Did I not make you swear by the Lord and solemnly warn you, saying, ‘ **Know** for certain that on the day you go out and go to any place whatever, you shall die ’? And you said to me, ‘What you say is good; I will obey.’ |
| 1Ki 2:44 | know | HVqp2ms | none recorded | 15939 | 0 | The king also said to Shimei, “ You **know** in your own heart all the harm that you did to David my father. So the Lord will bring back your harm on your own head. |
| 1Ki 3:7 | know | HVqi1cs | none recorded | - | 0 | And now, O Lord my God, you have made your servant king in place of David my father, although I am but a little child. I do not **know** how to go out or come in. |
| 1Ki 5:3 | know | HVqp2ms | none recorded | - | 0 | “ You **know** that David my father could not build a house for the name of the Lord his God because of the warfare with which his enemies surrounded him, until the Lord put them under the soles of his feet. |
| 1Ki 5:6 | know | HVqp2ms | none recorded | - | 0 | Now therefore command that cedars of Lebanon be cut for me. And my servants will join your servants, and I will pay you for your servants such wages as you set, for you **know** that there is no one among us who knows how to cut timber like the Sidonians.” |
| 1Ki 8:39 | know | HVqi2ms | none recorded | 15944, 16409, 19939 | 0 | then hear in heaven your dwelling place and forgive and act and render to each whose heart you **know**, according to all his ways ( for you, you only, know the hearts of all the children of mankind ), |
| 1Ki 8:39 | know | HVqp2ms | none recorded | - | 0 | then hear in heaven your dwelling place and forgive and act and render to each whose heart you **know**, according to all his ways ( for you, you only, know the hearts of all the children of mankind ), |
| 1Ki 8:43 | know | HVqj3mp | none recorded | - | 0 | hear in heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may **know** your name and fear you, as do your people Israel, and that they may know that this house that I have built is called by your name. |
| 1Ki 8:43 | know | HVqcc | none recorded | - | 0 | hear in heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may **know** your name and fear you, as do your people Israel, and that they may know that this house that I have built is called by your name. |
| 1Ki 8:60 | know | HVqcc | none recorded | - | 0 | that all the peoples of the earth may **know** that the Lord is God; there is no other. |
| 1Ki 17:24 | know | HVqp1cs | none recorded | - | 0 | And the woman said to Elijah, “ Now I **know** that you are a man of God, and that the word of the Lord in your mouth is truth.” |
| 1Ki 18:12 | know | HVqi1cs | none recorded | - | 0 | And as soon as I have gone from you, the Spirit of the Lord will carry you I **know** not where. And so, when I come and tell Ahab and he cannot find you, he will kill me, although I your servant have feared the Lord from my youth. |
| 1Ki 18:37 | know | HVqu3mp | none recorded | - | 0 | Answer me, O Lord, answer me, that this people may **know** that you, O Lord, are God, and that you have turned their hearts back.” |
| 1Ki 20:13 | know | HVqq2ms | none recorded | - | 0 | And behold, a prophet came near to Ahab king of Israel and said, “ Thus says the Lord, Have you seen all this great multitude? Behold, I will give it into your hand this day, and you shall **know** that I am the Lord.” |
| 1Ki 20:28 | know | HVqq2mp | none recorded | - | 0 | And a man of God came near and said to the king of Israel, “ Thus says the Lord, ‘ Because the Syrians have said, “The Lord is a god of the hills but he is not a god of the valleys,” therefore I will give all this great multitude into your hand, and you shall **know** that I am the Lord.’” |
| 1Ki 22:3 | know | HVqp2mp | none recorded | - | 0 | And the king of Israel said to his servants, “Do you **know** that Ramoth-gilead belongs to us, and we keep quiet and do not take it out of the hand of the king of Syria?” |
| 2Ki 2:3 | know | HVqp2ms | none recorded | - | 0 | And the sons of the prophets who were in Bethel came out to Elisha and said to him, “Do you **know** that today the Lord will take away your master from over you?” And he said, “ Yes, I know it; keep quiet.” |
| 2Ki 2:3 | know | HVqp1cs | none recorded | - | 0 | And the sons of the prophets who were in Bethel came out to Elisha and said to him, “Do you **know** that today the Lord will take away your master from over you?” And he said, “ Yes, I know it; keep quiet.” |
| 2Ki 2:5 | know | HVqp2ms | none recorded | - | 0 | The sons of the prophets who were at Jericho drew near to Elisha and said to him, “Do you **know** that today the Lord will take away your master from over you?” And he answered, “ Yes, I know it; keep quiet.” |
| 2Ki 2:5 | know | HVqp1cs | none recorded | - | 0 | The sons of the prophets who were at Jericho drew near to Elisha and said to him, “Do you **know** that today the Lord will take away your master from over you?” And he answered, “ Yes, I know it; keep quiet.” |
| 2Ki 4:1 | know | HVqp2ms | none recorded | - | 0 | Now the wife of one of the sons of the prophets cried to Elisha, “Your servant my husband is dead, and you **know** that your servant feared the Lord, but the creditor has come to take my two children to be his slaves.” |
| 2Ki 4:9 | know | HVqp1cs | none recorded | - | 0 | And she said to her husband, “ Behold now, I **know** that this is a holy man of God who is continually passing our way. |
| 2Ki 5:8 | know | HVqu3ms | none recorded | - | 0 | But when Elisha the man of God heard that the king of Israel had torn his clothes, he sent to the king, saying, “ Why have you torn your clothes? Let him come now to me, that he may **know** that there is a prophet in Israel.” |
| 2Ki 5:15 | know | HVqp1cs | none recorded | - | 0 | Then he returned to the man of God, he and all his company, and he came and stood before him. And he said, “ Behold, I **know** that there is no God in all the earth but in Israel; so accept now a present from your servant.” |
| 2Ki 7:12 | know | HVqp3cp | none recorded | - | 0 | And the king rose in the night and said to his servants, “I will tell you what the Syrians have done to us. They **know** that we are hungry. Therefore they have gone out of the camp to hide themselves in the open country, thinking, ‘When they come out of the city, we shall take them alive and get into the city.’” |
| 2Ki 8:12 | know | HVqp1cs | none recorded | - | 0 | And Hazael said, “ Why does my lord weep?” He answered, “ Because I **know** the evil that you will do to the people of Israel. You will set on fire their fortresses, and you will kill their young men with the sword and dash in pieces their little ones and rip open their pregnant women.” |
| 2Ki 9:11 | know | HVqp2mp | none recorded | - | 0 | When Jehu came out to the servants of his master, they said to him, “Is all well? Why did this mad fellow come to you?” And he said to them, “ You **know** the fellow and his talk.” |
| 2Ki 10:10 | know | HVqv2mp | none recorded | - | 0 | **Know** then that there shall fall to the earth nothing of the word of the Lord, which the Lord spoke concerning the house of Ahab, for the Lord has done what he said by his servant Elijah.” |
| 2Ki 17:26 | know | HVqp3cp | none recorded | - | 0 | So the king of Assyria was told, “The nations that you have carried away and placed in the cities of Samaria do not **know** the law of the god of the land. Therefore he has sent lions among them, and behold, they are killing them, because they do not know the law of the god of the land.” |
| 2Ki 17:26 | know | HVqrmpa | none recorded | - | 0 | So the king of Assyria was told, “The nations that you have carried away and placed in the cities of Samaria do not **know** the law of the god of the land. Therefore he has sent lions among them, and behold, they are killing them, because they do not know the law of the god of the land.” |
| 2Ki 19:19 | know | HVqu3mp | none recorded | - | 0 | So now, O Lord our God, save us, please, from his hand, that all the kingdoms of the earth may **know** that you, O Lord, are God alone.” |
| 2Ki 19:27 | know | HVqp1cs | none recorded | - | 0 | “But I **know** your sitting down and your going out and coming in, and your raging against me. |
| 1Ch 12:32 | know | HVqcc | none recorded | - | 0 | Of Issachar, men who had understanding of the times, to **know** what Israel ought to do, 200 chiefs, and all their kinsmen under their command. |
| 1Ch 17:18 | know | HVqp2ms | none recorded | - | 0 | And what more can David say to you for honoring your servant? For you **know** your servant. |
| 1Ch 21:2 | know | HVqc1cs | none recorded | - | 0 | So David said to Joab and the commanders of the army, “ Go, number Israel, from Beersheba to Dan, and bring me a report, that I may **know** their number.” |
| 1Ch 28:9 | know | HVqv2ms | none recorded | 19501, 20489 | 0 | “And you, Solomon my son, **know** the God of your father and serve him with a whole heart and with a willing mind, for the Lord searches all hearts and understands every plan and thought. If you seek him, he will be found by you, but if you forsake him, he will cast you off forever. |
| 1Ch 29:17 | know | HVqq1cs | none recorded | 16397 | 0 | I **know**, my God, that you test the heart and have pleasure in uprightness. In the uprightness of my heart I have freely offered all these things, and now I have seen your people, who are present here, offering freely and joyously to you. |
| 2Ch 2:8 | know | HVqp1cs | none recorded | - | 0 | Send me also cedar, cypress, and algum timber from Lebanon, for I **know** that your servants know how to cut timber in Lebanon. And my servants will be with your servants, |
| 2Ch 6:30 | know | HVqi2ms | none recorded | 15944, 16409, 16804 | 0 | then hear from heaven your dwelling place and forgive and render to each whose heart you **know**, according to all his ways, for you, you only, know the hearts of the children of mankind, |
| 2Ch 6:30 | know | HVqp2ms | none recorded | - | 0 | then hear from heaven your dwelling place and forgive and render to each whose heart you **know**, according to all his ways, for you, you only, know the hearts of the children of mankind, |
| 2Ch 6:33 | know | HVqj3mp | none recorded | - | 0 | hear from heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may **know** your name and fear you, as do your people Israel, and that they may know that this house that I have built is called by your name. |
| 2Ch 6:33 | know | HVqcc | none recorded | - | 0 | hear from heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may **know** your name and fear you, as do your people Israel, and that they may know that this house that I have built is called by your name. |
| 2Ch 12:8 | know | HVqu3mp | none recorded | 14102, 14576 | 0 | Nevertheless, they shall be servants to him, that they may **know** my service and the service of the kingdoms of the countries.” |
| 2Ch 13:5 | know | HVqcc | none recorded | - | 0 | Ought you not to **know** that the Lord God of Israel gave the kingship over Israel forever to David and his sons by a covenant of salt? |
| 2Ch 20:12 | know | HVqi1cp | none recorded | - | 0 | O our God, will you not execute judgment on them? For we are powerless against this great horde that is coming against us. We do not **know** what to do, but our eyes are on you.” |
| 2Ch 25:16 | know | HVqp1cs | none recorded | 14080, 14535 | 0 | But as he was speaking, the king said to him, “Have we made you a royal counselor? Stop! Why should you be struck down?” So the prophet stopped, but said, “I **know** that God has determined to destroy you, because you have done this and have not listened to my counsel.” |
| 2Ch 32:13 | know | HVqi2mp | none recorded | 18226 | 0 | Do you not **know** what I and my fathers have done to all the peoples of other lands? Were the gods of the nations of those lands at all able to deliver their lands out of my hand? |
| 2Ch 32:31 | know | HVqcc | none recorded | 15235, 15944, 16397, 17117, 18001 | 0 | And so in the matter of the envoys of the princes of Babylon, who had been sent to him to inquire about the sign that had been done in the land, God left him to himself, in order to test him and to **know** all that was in his heart. |
| Neh 2:16 | know | HVqp3cp | none recorded | - | 0 | And the officials did not **know** where I had gone or what I was doing, and I had not yet told the Jews, the priests, the nobles, the officials, and the rest who were to do the work. |
| Neh 4:11 | know | HVqi3mp | none recorded | - | 0 | And our enemies said, “They will not **know** or see till we come among them and kill them and stop the work.” |
| Est 4:11 | know | HVqrmpa | none recorded | - | 0 | “ All the king’s servants and the people of the king’s provinces **know** that if any man or woman goes to the king inside the inner court without being called, there is but one law —to be put to death, except the one to whom the king holds out the golden scepter so that he may live. But as for me, I have not been called to come in to the king these thirty days.” |
| Job 5:24 | know | HVqq2ms | none recorded | - | 0 | You shall **know** that your tent is at peace, and you shall inspect your fold and miss nothing. |
| Job 5:25 | know | HVqq2ms | none recorded | - | 0 | You shall **know** also that your offspring shall be many, and your descendants as the grass of the earth. |
| Job 5:27 | know | HVqv2ms | none recorded | - | 0 | Behold, this we have searched out; it is true. Hear, and **know** it for your good.” |
| Job 8:9 | know | HVqi1cp | none recorded | - | 0 | For we are but of yesterday and **know** nothing, for our days on earth are a shadow. |
| Job 9:2 | know | HVqp1cs | none recorded | - | 0 | “Truly I **know** that it is so: But how can a man be in the right before God? |
| Job 9:5 | know | HVqp3cp | none recorded | 14608 | 0 | he who removes mountains, and they **know** it not, when he overturns them in his anger, |
| Job 9:28 | know | HVqp1cs | none recorded | - | 0 | I become afraid of all my suffering, for I **know** you will not hold me innocent. |
| Job 10:2 | know | HVhv2ms | none recorded | - | 0 | I will say to God, Do not condemn me; let me **know** why you contend against me. |
| Job 10:13 | know | HVqp1cs | none recorded | - | 0 | Yet these things you hid in your heart; I **know** that this was your purpose. |
| Job 11:6 | know | HVqv2ms | none recorded | - | 0 | and that he would tell you the secrets of wisdom! For he is manifold in understanding. **Know** then that God exacts of you less than your guilt deserves. |
| Job 11:8 | know | HVqi2ms | none recorded | - | 0 | It is higher than heaven —what can you do? Deeper than Sheol —what can you **know**? |
| Job 13:18 | know | HVqp1cs | none recorded | - | 0 | Behold, I have prepared my case; I **know** that I shall be in the right. |
| Job 13:23 | know | HVhv2ms | none recorded | - | 0 | How many are my iniquities and my sins? Make me **know** my transgression and my sin. |
| Job 14:21 | know | HVqi3ms | none recorded | - | 0 | His sons come to honor, and he does not **know** it; they are brought low, and he perceives it not. |
| Job 15:9 | know | HVqp2ms | none recorded | - | 0 | What do you **know** that we do not know? What do you understand that is not clear to us? |
| Job 15:9 | know | HVqi1cp | none recorded | - | 0 | What do you **know** that we do not know? What do you understand that is not clear to us? |
| Job 19:6 | know | HVqv2mp | none recorded | - | 0 | **know** then that God has put me in the wrong and closed his net about me. |
| Job 19:25 | know | HVqp1cs | none recorded | 13876 | 0 | For I **know** that my Redeemer lives, and at the last he will stand upon the earth. |
| Job 19:29 | know | HVqj2mp | none recorded | 13392, 13876, 14252 | 0 | be afraid of the sword, for wrath brings the punishment of the sword, that you may **know** there is a judgment.” |
| Job 20:4 | know | HVqp2ms | none recorded | - | 0 | Do you not **know** this from of old, since man was placed on earth, |
| Job 21:19 | know | HVqu3ms | none recorded | 14605, 17515 | 0 | You say, ‘ God stores up their iniquity for their children.’ Let him pay it out to them, that they may **know** it. |
| Job 21:27 | know | HVqp1cs | none recorded | - | 0 | “ Behold, I **know** your thoughts and your schemes to wrong me. |
| Job 22:13 | know | HVqp3ms | none recorded | - | 0 | But you say, ‘ What does God **know**? Can he judge through the deep darkness? |
| Job 23:5 | know | HVqc1cs | none recorded | - | 0 | I would **know** what he would answer me and understand what he would say to me. |
| Job 24:1 | know | HVqrmpc | none recorded | - | 0 | “ Why are not times of judgment kept by the Almighty, and why do those who **know** him never see his days? |
| Job 24:16 | know | HVqp3cp | none recorded | - | 0 | In the dark they dig through houses; by day they shut themselves up; they do not **know** the light. |
| Job 28:13 | know | HVqp3ms | none recorded | 17801 | 0 | Man does not **know** its worth, and it is not found in the land of the living. |
| Job 29:16 | know | HVqp1cs | none recorded | - | 0 | I was a father to the needy, and I searched out the cause of him whom I did not **know**. |
| Job 30:23 | know | HVqp1cs | none recorded | - | 0 | For I **know** that you will bring me to death and to the house appointed for all living. |
| Job 31:6 | know | HVqu3ms | none recorded | - | 0 | (Let me be weighed in a just balance, and let God **know** my integrity!) |
| Job 32:22 | know | HVqp1cs | none recorded | - | 0 | For I do not **know** how to flatter, else my Maker would soon take me away. |
| Job 34:2 | know | HVqrmpa | none recorded | - | 0 | “ Hear my words, you wise men, and give ear to me, you who **know**; |
| Job 34:4 | know | HVqc1cp | none recorded | 19472, 19585, 19739, 19857 | 0 | Let us choose what is right; let us **know** among ourselves what is good. |
| Job 34:33 | know | HVqp2ms | none recorded | 19472, 19588, 20307 | 0 | Will he then make repayment to suit you, because you reject it? For you must choose, and not I; therefore declare what you **know**. |
| Job 36:26 | know | HVqi1cp | none recorded | - | 0 | Behold, God is great, and we **know** him not; the number of his years is unsearchable. |
| Job 37:7 | know | HVqcc | none recorded | - | 0 | He seals up the hand of every man, that all men whom he made may **know** it. |
| Job 37:15 | know | HVqi2ms | none recorded | - | 0 | Do you **know** how God lays his command upon them and causes the lightning of his cloud to shine? |
| Job 37:16 | know | HVqi2ms | none recorded | - | 0 | Do you **know** the balancings of the clouds, the wondrous works of him who is perfect in knowledge, |
| Job 38:5 | know | HVqi2ms | none recorded | - | 0 | Who determined its measurements — surely you **know**! Or who stretched the line upon it? |
| Job 38:12 | know | HVpp2ms | none recorded | - | 0 | “Have you commanded the morning since your days began, and caused the dawn to **know** its place, |
| Job 38:18 | know | HVqp2ms | none recorded | - | 0 | Have you comprehended the expanse of the earth? Declare, if you **know** all this. |
| Job 38:21 | know | HVqp2ms | none recorded | - | 0 | You **know**, for you were born then, and the number of your days is great! |
| Job 38:33 | know | HVqp2ms | none recorded | - | 0 | Do you **know** the ordinances of the heavens? Can you establish their rule on the earth? |
| Job 39:1 | know | HVqp2ms | none recorded | - | 0 | “Do you **know** when the mountain goats give birth? Do you observe the calving of the does? |
| Job 39:2 | know | HVqq2ms | none recorded | - | 0 | Can you number the months that they fulfill, and do you **know** the time when they give birth, |
| Job 42:2 | know | HVqp1cs | none recorded | - | 0 | “I **know** that you can do all things, and that no purpose of yours can be thwarted. |
| Job 42:3 | know | HVqi1cs | none recorded | - | 0 | ‘ Who is this that hides counsel without knowledge?’ Therefore I have uttered what I did not understand, things too wonderful for me, which I did not **know**. |
| Psa 4:3 | know | HVqv2mp | none recorded | - | 0 | But **know** that the Lord has set apart the godly for himself; the Lord hears when I call to him. |
| Psa 9:10 | know | HVqrmpc | none recorded | - | 0 | And those who **know** your name put their trust in you, for you, O Lord, have not forsaken those who seek you. |
| Psa 9:20 | know | HVqi3mp | none recorded | 12703 | 0 | Put them in fear, O Lord! Let the nations **know** that they are but men! Selah |
| Psa 20:6 | know | HVqp1cs | none recorded | - | 0 | Now I **know** that the Lord saves his anointed; he will answer him from his holy heaven with the saving might of his right hand. |
| Psa 25:4 | know | HVhv2ms | none recorded | 19664, 19841 | 0 | Make me to **know** your ways, O Lord; teach me your paths. |
| Psa 35:8 | know | HVqi3ms | none recorded | - | 0 | Let destruction come upon him when he does not **know** it! And let the net that he hid ensnare him; let him fall into it —to his destruction! |
| Psa 35:11 | know | HVqp1cs | none recorded | - | 0 | Malicious witnesses rise up; they ask me of things that I do not **know**. |
| Psa 35:15 | know | HVqp1cs | none recorded | - | 0 | But at my stumbling they rejoiced and gathered; they gathered together against me; wretches whom I did not **know** tore at me without ceasing; |
| Psa 36:10 | know | HVqrmpc | none recorded | - | 0 | Oh, continue your steadfast love to those who **know** you, and your righteousness to the upright of heart! |
| Psa 39:4 | know | HVhv2ms | none recorded | 18138 | 0 | “O Lord, make me **know** my end and what is the measure of my days; let me know how fleeting I am! |
| Psa 39:4 | know | HVqc1cs | none recorded | - | 0 | “O Lord, make me **know** my end and what is the measure of my days; let me know how fleeting I am! |
| Psa 39:6 | know | HVqi3ms | none recorded | - | 0 | Surely a man goes about as a shadow! Surely for nothing they are in turmoil; man heaps up wealth and does not **know** who will gather! |
| Psa 40:9 | know | HVqp2ms | none recorded | - | 0 | I have told the glad news of deliverance in the great congregation; behold, I have not restrained my lips, as you **know**, O Lord. |
| Psa 41:11 | know | HVqp1cs | none recorded | 17619 | 0 | By this I **know** that you delight in me: my enemy will not shout in triumph over me. |
| Psa 46:10 | know | HVqv2mp | none recorded | - | 0 | “Be still, and **know** that I am God. I will be exalted among the nations, I will be exalted in the earth!” |
| Psa 50:11 | know | HVqp1cs | none recorded | - | 0 | I **know** all the birds of the hills, and all that moves in the field is mine. |
| Psa 51:3 | know | HVqi1cs | none recorded | - | 0 | For I **know** my transgressions, and my sin is ever before me. |
| Psa 56:9 | know | HVqp1cs | none recorded | 14602 | 0 | Then my enemies will turn back in the day when I call. This I **know**, that God is for me. |
| Psa 59:13 | know | HVqu3mp | none recorded | 13390, 14602, 14736, 19093 | 0 | consume them in wrath; consume them till they are no more, that they may **know** that God rules over Jacob to the ends of the earth. Selah |
| Psa 69:5 | know | HVqp2ms | none recorded | 15022, 19219 | 0 | O God, you **know** my folly; the wrongs I have done are not hidden from you. |
| Psa 69:19 | know | HVqp2ms | none recorded | 14968, 14969, 15022 | 0 | You **know** my reproach, and my shame and my dishonor; my foes are all known to you. |
| Psa 73:11 | know | HVqp3ms | none recorded | - | 0 | And they say, “ How can God **know**? Is there knowledge in the Most High?” |
| Psa 78:6 | know | HVqj3mp | none recorded | - | 0 | that the next generation might **know** them, the children yet unborn, and arise and tell them to their children, |
| Psa 79:6 | know | HVqp3cp | none recorded | 14602, 17849 | 0 | Pour out your anger on the nations that do not **know** you, and on the kingdoms that do not call upon your name! |
| Psa 83:18 | know | HVqu3mp | none recorded | - | 0 | that they may **know** that you alone, whose name is the Lord, are the Most High over all the earth. |
| Psa 87:4 | know | HVqrmpc | none recorded | - | 0 | Among those who **know** me I mention Rahab and Babylon; behold, Philistia and Tyre, with Cush — “ This one was born there,” they say. |
| Psa 89:15 | know | HVqrmpc | none recorded | - | 0 | Blessed are the people who **know** the festal shout, who walk, O Lord, in the light of your face, |
| Psa 92:6 | know | HVqi3ms | none recorded | - | 0 | The stupid man cannot **know**; the fool cannot understand this: |
| Psa 100:3 | know | HVqv2mp | none recorded | - | 0 | **Know** that the Lord, he is God! It is he who made us, and we are his; we are his people, and the sheep of his pasture. |
| Psa 101:4 | know | HVqi1cs | none recorded | - | 0 | A perverse heart shall be far from me; I will **know** nothing of evil. |
| Psa 109:27 | know | HVqu3mp | none recorded | - | 0 | Let them **know** that this is your hand; you, O Lord, have done it! |
| Psa 119:75 | know | HVqp1cs | none recorded | - | 0 | I **know**, O Lord, that your rules are righteous, and that in faithfulness you have afflicted me. |
| Psa 119:79 | know | HVqrmpc | none recorded | - | 0 | Let those who fear you turn to me, that they may **know** your testimonies. |
| Psa 119:125 | know | HVqc1cs | none recorded | - | 0 | I am your servant; give me understanding, that I may **know** your testimonies! |
| Psa 135:5 | know | HVqp1cs | none recorded | 17522 | 0 | For I **know** that the Lord is great, and that our Lord is above all gods. |
| Psa 139:2 | know | HVqp2ms | none recorded | 20489 | 0 | You **know** when I sit down and when I rise up; you discern my thoughts from afar. |
| Psa 139:4 | know | HVqp2ms | none recorded | - | 0 | Even before a word is on my tongue, behold, O Lord, you **know** it altogether. |
| Psa 139:23 | know | HVqv2ms | none recorded | 15915, 15944, 16397, 19251, 19255, 20452, 20489 | 0 | Search me, O God, and **know** my heart! Try me and know my thoughts! |
| Psa 139:23 | know | HVqv2ms | none recorded | 15915, 15944, 16397, 19251, 19255, 20452, 20489 | 0 | Search me, O God, and **know** my heart! Try me and know my thoughts! |
| Psa 140:12 | know | HVqp1cs | none recorded | - | 0 | I **know** that the Lord will maintain the cause of the afflicted, and will execute justice for the needy. |
| Psa 142:3 | know | HVqp2ms | none recorded | 18889, 19272 | 0 | When my spirit faints within me, you **know** my way! In the path where I walk they have hidden a trap for me. |
| Psa 143:8 | know | HVhv2ms | none recorded | - | 0 | Let me hear in the morning of your steadfast love, for in you I trust. Make me **know** the way I should go, for to you I lift up my soul. |
| Psa 147:20 | know | HVqp3cp | none recorded | - | 0 | He has not dealt thus with any other nation; they do not **know** his rules. Praise the Lord! |
| Pro 1:2 | know | HVqcc | none recorded | - | 0 | To **know** wisdom and instruction, to understand words of insight, |
| Pro 4:19 | know | HVqp3cp | none recorded | - | 0 | The way of the wicked is like deep darkness; they do not **know** over what they stumble. |
| Pro 5:6 | know | HVqi2ms | none recorded | - | 0 | she does not ponder the path of life; her ways wander, and she does not **know** it. |
| Pro 7:23 | know | HVqp3ms | none recorded | - | 0 | till an arrow pierces its liver; as a bird rushes into a snare; he does not **know** that it will cost him his life. |
| Pro 9:18 | know | HVqp3ms | none recorded | 17660 | 0 | But he does not **know** that the dead are there, that her guests are in the depths of Sheol. |
| Pro 10:32 | know | HVqi3mp | none recorded | - | 0 | The lips of the righteous **know** what is acceptable, but the mouth of the wicked, what is perverse. |
| Pro 22:21 | know | HVhcc | none recorded | - | 0 | to make you **know** what is right and true, that you may give a true answer to those who sent you? |
| Pro 24:12 | know | HVqp1cp | none recorded | 15945, 16822 | 0 | If you say, “ Behold, we did not **know** this,” does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it, and will he not repay man according to his work? |
| Pro 24:12 | know | HVqi3ms | none recorded | - | 0 | If you say, “ Behold, we did not **know** this,” does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it, and will he not repay man according to his work? |
| Pro 24:14 | know | HVqv2ms | none recorded | - | 0 | **Know** that wisdom is such to your soul; if you find it, there will be a future, and your hope will not be cut off. |
| Pro 27:1 | know | HVqi2ms | none recorded | 15180 | 0 | Do not boast about tomorrow, for you do not **know** what a day may bring. |
| Pro 27:23 | know | HVqaa | none recorded | - | 0 | **Know** well the condition of your flocks, and give attention to your herds, |
| Pro 28:22 | know | HVqi3ms | none recorded | - | 0 | A stingy man hastens after wealth and does not **know** that poverty will come upon him. |
| Pro 30:4 | know | HVqi2ms | none recorded | - | 0 | Who has ascended to heaven and come down? Who has gathered the wind in his fists? Who has wrapped up the waters in a garment? Who has established all the ends of the earth? What is his name, and what is his son’s name? Surely you **know**! |
| Ecc 1:17 | know | HVqcc | none recorded | 13918, 14224, 15940, 15965, 17173, 17264 | 0 | And I applied my heart to **know** wisdom and to know madness and folly. I perceived that this also is but a striving after wind. |
| Ecc 1:17 | know | HNcfsa | none recorded | - | 0 | And I applied my heart to **know** wisdom and to know madness and folly. I perceived that this also is but a striving after wind. |
| Ecc 5:1 | know | HVqrmpa | none recorded | - | 0 | Guard your steps when you go to the house of God. To draw near to listen is better than to offer the sacrifice of fools, for they do not **know** that they are doing evil. |
| Ecc 7:25 | know | HVqcc | none recorded | 15940, 16174, 16557, 17112, 17173, 18131 | 0 | I turned my heart to **know** and to search out and to seek wisdom and the scheme of things, and to know the wickedness of folly and the foolishness that is madness. |
| Ecc 7:25 | know | HVqcc | none recorded | 15940, 16174, 16557, 17112, 17173, 18131 | 0 | I turned my heart to **know** and to search out and to seek wisdom and the scheme of things, and to know the wickedness of folly and the foolishness that is madness. |
| Ecc 8:5 | know | HVqi3ms | none recorded | 16557 | 0 | Whoever keeps a command will **know** no evil thing, and the wise heart will know the proper time and the just way. |
| Ecc 8:5 | know | HVqi3ms | none recorded | 16557 | 0 | Whoever keeps a command will **know** no evil thing, and the wise heart will know the proper time and the just way. |
| Ecc 8:7 | know | HVqrmsa | none recorded | - | 0 | For he does not **know** what is to be, for who can tell him how it will be? |
| Ecc 8:12 | know | HVqrmsa | none recorded | - | 0 | Though a sinner does evil a hundred times and prolongs his life, yet I **know** that it will be well with those who fear God, because they fear before him. |
| Ecc 8:16 | know | HVqcc | none recorded | 15940 | 0 | When I applied my heart to **know** wisdom, and to see the business that is done on earth, how neither day nor night do one’s eyes see sleep, |
| Ecc 8:17 | know | HVqcc | none recorded | - | 0 | then I saw all the work of God, that man cannot find out the work that is done under the sun. However much man may toil in seeking, he will not find it out. Even though a wise man claims to **know**, he cannot find it out. |
| Ecc 9:1 | know | HVqrmsa | none recorded | - | 0 | But all this I laid to heart, examining it all, how the righteous and the wise and their deeds are in the hand of God. Whether it is love or hate, man does not **know**; both are before him. |
| Ecc 9:5 | know | HVqrmpa | none recorded | 16184, 18272, 18273, 18314 | 0 | For the living **know** that they will die, but the dead know nothing, and they have no more reward, for the memory of them is forgotten. |
| Ecc 9:5 | know | HVqrmpa | none recorded | 16184, 18272, 18273, 18314 | 0 | For the living **know** that they will die, but the dead know nothing, and they have no more reward, for the memory of them is forgotten. |
| Ecc 9:12 | know | HVqi3ms | none recorded | - | 0 | For man does not **know** his time. Like fish that are taken in an evil net, and like birds that are caught in a snare, so the children of man are snared at an evil time, when it suddenly falls upon them. |
| Ecc 10:15 | know | HVqp3ms | none recorded | - | 0 | The toil of a fool wearies him, for he does not **know** the way to the city. |
| Ecc 11:2 | know | HVqi2ms | none recorded | - | 0 | Give a portion to seven, or even to eight, for you **know** not what disaster may happen on earth. |
| Ecc 11:5 | know | HVqrmsa | none recorded | - | 0 | As you do not **know** the way the spirit comes to the bones in the womb of a woman with child, so you do not know the work of God who makes everything. |
| Ecc 11:5 | know | HVqi2ms | none recorded | - | 0 | As you do not **know** the way the spirit comes to the bones in the womb of a woman with child, so you do not know the work of God who makes everything. |
| Ecc 11:6 | know | HVqrmsa | none recorded | - | 0 | In the morning sow your seed, and at evening withhold not your hand, for you do not **know** which will prosper, this or that, or whether both alike will be good. |
| Ecc 11:9 | know | HVqv2ms | none recorded | 14224, 16801, 16932 | 0 | Rejoice, O young man, in your youth, and let your heart cheer you in the days of your youth. Walk in the ways of your heart and the sight of your eyes. But **know** that for all these things God will bring you into judgment. |
| Song 1:8 | know | HVqi2fs | none recorded | - | 0 | If you do not **know**, O most beautiful among women, follow in the tracks of the flock, and pasture your young goats beside the shepherds ’ tents. |
| Isa 1:3 | know | HVqp3ms | none recorded | 19653, 19658, 19840 | 0 | The ox knows its owner, and the donkey its master’s crib, but Israel does not **know**, my people do not understand.” |
| Isa 5:19 | know | HVqc1cp | none recorded | - | 0 | who say: “Let him be quick, let him speed his work that we may see it; let the counsel of the Holy One of Israel draw near, and let it come, that we may **know** it!” |
| Isa 9:9 | know | HVqq3cp | none recorded | - | 0 | and all the people will **know**, Ephraim and the inhabitants of Samaria, who say in pride and in arrogance of heart: |
| Isa 19:12 | know | HVqu3mp | none recorded | - | 0 | Where then are your wise men? Let them tell you that they might **know** what the Lord of hosts has purposed against Egypt. |
| Isa 19:21 | know | HVqq3cp | none recorded | 14971 | 0 | And the Lord will make himself known to the Egyptians, and the Egyptians will **know** the Lord in that day and worship with sacrifice and offering, and they will make vows to the Lord and perform them. |
| Isa 32:4 | know | HNcfsa | none recorded | - | 0 | The heart of the hasty will understand and **know**, and the tongue of the stammerers will hasten to speak distinctly. |
| Isa 37:20 | know | HVqu3mp | none recorded | - | 0 | So now, O Lord our God, save us from his hand, that all the kingdoms of the earth may **know** that you alone are the Lord.” |
| Isa 37:28 | know | HVqp1cs | none recorded | - | 0 | “‘I **know** your sitting down and your going out and coming in, and your raging against me. |
| Isa 40:21 | know | HVqi2mp | none recorded | - | 0 | Do you not **know**? Do you not hear? Has it not been told you from the beginning? Have you not understood from the foundations of the earth? |
| Isa 41:20 | know | HVqu3mp | none recorded | - | 0 | that they may see and **know**, may consider and understand together, that the hand of the Lord has done this, the Holy One of Israel has created it. |
| Isa 41:22 | know | HVqc1cp | none recorded | - | 0 | Let them bring them, and tell us what is to happen. Tell us the former things, what they are, that we may consider them, that we may **know** their outcome; or declare to us the things to come. |
| Isa 41:23 | know | HVqc1cp | none recorded | - | 0 | Tell us what is to come hereafter, that we may **know** that you are gods; do good, or do harm, that we may be dismayed and terrified. |
| Isa 41:26 | know | HVqc1cp | none recorded | - | 0 | Who declared it from the beginning, that we might **know**, and beforehand, that we might say, “He is right ”? There was none who declared it, none who proclaimed, none who heard your words. |
| Isa 42:16 | know | HVqp3cp | none recorded | - | 0 | And I will lead the blind in a way that they do not **know**, in paths that they have not known I will guide them. I will turn the darkness before them into light, the rough places into level ground. These are the things I do, and I do not forsake them. |
| Isa 43:10 | know | HVqj2mp | none recorded | 19491, 19506, 19533, 19708 | 0 | “ You are my witnesses,” declares the Lord, “and my servant whom I have chosen, that you may **know** and believe me and understand that I am he. Before me no god was formed, nor shall there be any after me. |
| Isa 44:8 | know | HVqp1cs | none recorded | - | 0 | Fear not, nor be afraid; have I not told you from of old and declared it? And you are my witnesses! Is there a God besides me? There is no Rock; I **know** not any.” |
| Isa 44:9 | know | HVqi3mp | none recorded | 19603, 19608 | 0 | All who fashion idols are nothing, and the things they delight in do not profit. Their witnesses neither see nor **know**, that they may be put to shame. |
| Isa 44:18 | know | HVqp3cp | none recorded | 18146, 19514, 19608 | 0 | They **know** not, nor do they discern, for he has shut their eyes, so that they cannot see, and their hearts, so that they cannot understand. |
| Isa 45:3 | know | HVqj2ms | none recorded | 19955 | 0 | I will give you the treasures of darkness and the hoards in secret places, that you may **know** that it is I, the Lord, the God of Israel, who call you by your name. |
| Isa 45:4 | know | HVqp2ms | none recorded | 19642, 19708, 19955 | 0 | For the sake of my servant Jacob, and Israel my chosen, I call you by your name, I name you, though you do not **know** me. |
| Isa 45:5 | know | HVqp2ms | none recorded | 19642, 19955 | 0 | I am the Lord, and there is no other, besides me there is no God; I equip you, though you do not **know** me, |
| Isa 45:6 | know | HVqj3mp | none recorded | - | 0 | that people may **know**, from the rising of the sun and from the west, that there is none besides me; I am the Lord, and there is no other. |
| Isa 47:8 | know | HVqi1cs | none recorded | - | 0 | Now therefore hear this, you lover of pleasures, who sit securely, who say in your heart, “ I am, and there is no one besides me; I shall not sit as a widow or **know** the loss of children ”: |
| Isa 47:11 | know | HVqi2fs | none recorded | - | 0 | But evil shall come upon you, which you will not **know** how to charm away; disaster shall fall upon you, for which you will not be able to atone; and ruin shall come upon you suddenly, of which you know nothing. |
| Isa 47:11 | know | HVqi2fs | none recorded | - | 0 | But evil shall come upon you, which you will not **know** how to charm away; disaster shall fall upon you, for which you will not be able to atone; and ruin shall come upon you suddenly, of which you know nothing. |
| Isa 48:4 | know | HVqcc | none recorded | - | 0 | Because I **know** that you are obstinate, and your neck is an iron sinew and your forehead brass, |
| Isa 49:23 | know | HVqq2fs | none recorded | - | 0 | Kings shall be your foster fathers, and their queens your nursing mothers. With their faces to the ground they shall bow down to you, and lick the dust of your feet. Then you will **know** that I am the Lord; those who wait for me shall not be put to shame.” |
| Isa 49:26 | know | HVqq3cp | none recorded | 15961 | 0 | I will make your oppressors eat their own flesh, and they shall be drunk with their own blood as with wine. Then all flesh shall **know** that I am the Lord your Savior, and your Redeemer, the Mighty One of Jacob.” |
| Isa 50:4 | know | HVqcc | none recorded | 18175 | 0 | The Lord God has given me the tongue of those who are taught, that I may **know** how to sustain with a word him who is weary. Morning by morning he awakens; he awakens my ear to hear as those who are taught. |
| Isa 50:7 | know | HVqw1cs | none recorded | - | 0 | But the Lord God helps me; therefore I have not been disgraced; therefore I have set my face like a flint, and I **know** that I shall not be put to shame. |
| Isa 51:7 | know | HVqrmpc | none recorded | - | 0 | “ Listen to me, you who **know** righteousness, the people in whose heart is my law; fear not the reproach of man, nor be dismayed at their revilings. |
| Isa 52:6 | know | HVqi3ms | none recorded | - | 0 | Therefore my people shall **know** my name. Therefore in that day they shall know that it is I who speak; here I am.” |
| Isa 55:5 | know | HVqi2ms | none recorded | - | 0 | Behold, you shall call a nation that you do not **know**, and a nation that did not know you shall run to you, because of the Lord your God, and of the Holy One of Israel, for he has glorified you. |
| Isa 55:5 | know | HVqp3cp | none recorded | - | 0 | Behold, you shall call a nation that you do not **know**, and a nation that did not know you shall run to you, because of the Lord your God, and of the Holy One of Israel, for he has glorified you. |
| Isa 59:8 | know | HVqp3cp | none recorded | - | 0 | The way of peace they do not **know**, and there is no justice in their paths; they have made their roads crooked; no one who treads on them knows peace. |
| Isa 59:12 | know | HVqp1cp | none recorded | - | 0 | For our transgressions are multiplied before you, and our sins testify against us; for our transgressions are with us, and we **know** our iniquities: |
| Isa 60:16 | know | HVqq2fs | none recorded | - | 0 | You shall suck the milk of nations; you shall nurse at the breast of kings; and you shall **know** that I, the Lord, am your Savior and your Redeemer, the Mighty One of Jacob. |
| Isa 63:16 | know | HVqp3ms | none recorded | - | 0 | For you are our Father, though Abraham does not **know** us, and Israel does not acknowledge us; you, O Lord, are our Father, our Redeemer from of old is your name. |
| Jer 2:8 | know | HVqp3cp | none recorded | - | 0 | The priests did not say, ‘ Where is the Lord?’ Those who handle the law did not **know** me; the shepherds transgressed against me; the prophets prophesied by Baal and went after things that do not profit. |
| Jer 2:19 | know | HVqv2fs | none recorded | - | 0 | Your evil will chastise you, and your apostasy will reprove you. **Know** and see that it is evil and bitter for you to forsake the Lord your God; the fear of me is not in you, declares the Lord God of hosts. |
| Jer 2:23 | know | HVqv2fs | none recorded | - | 0 | How can you say, ‘I am not unclean, I have not gone after the Baals ’? Look at your way in the valley; **know** what you have done — a restless young camel running here and there, |
| Jer 4:22 | know | HVqp3cp | none recorded | - | 0 | “ For my people are foolish; they **know** me not; they are stupid children; they have no understanding. They are ‘ wise ’—in doing evil! But how to do good they know not.” |
| Jer 4:22 | know | HVqp3cp | none recorded | - | 0 | “ For my people are foolish; they **know** me not; they are stupid children; they have no understanding. They are ‘ wise ’—in doing evil! But how to do good they know not.” |
| Jer 5:4 | know | HVqp3cp | none recorded | - | 0 | Then I said, “These are only the poor; they have no sense; for they do not **know** the way of the Lord, the justice of their God. |
| Jer 5:5 | know | HVqp3cp | none recorded | - | 0 | I will go to the great and will speak to them, for they **know** the way of the Lord, the justice of their God.” But they all alike had broken the yoke; they had burst the bonds. |
| Jer 5:15 | know | HVqi2ms | none recorded | - | 0 | Behold, I am bringing against you a nation from afar, O house of Israel, declares the Lord. It is an enduring nation; it is an ancient nation, a nation whose language you do not **know**, nor can you understand what they say. |
| Jer 6:18 | know | HVqv2fs | none recorded | - | 0 | Therefore hear, O nations, and **know**, O congregation, what will happen to them. |
| Jer 6:27 | know | HVqu2ms | none recorded | - | 0 | “I have made you a tester of metals among my people, that you may **know** and test their ways. |
| Jer 8:7 | know | HVqp3cp | none recorded | - | 0 | Even the stork in the heavens knows her times, and the turtledove, swallow, and crane keep the time of their coming, but my people **know** not the rules of the Lord. |
| Jer 9:3 | know | HVqp3cp | none recorded | - | 0 | They bend their tongue like a bow; falsehood and not truth has grown strong in the land; for they proceed from evil to evil, and they do not **know** me, declares the Lord. |
| Jer 9:6 | know | HVqcc | none recorded | - | 0 | Heaping oppression upon oppression, and deceit upon deceit, they refuse to **know** me, declares the Lord. |
| Jer 10:23 | know | HVqp1cs | none recorded | - | 0 | I **know**, O Lord, that the way of man is not in himself, that it is not in man who walks to direct his steps. |
| Jer 10:25 | know | HVqp3cp | none recorded | 13390, 14602 | 0 | Pour out your wrath on the nations that **know** you not, and on the peoples that call not on your name, for they have devoured Jacob; they have devoured him and consumed him, and have laid waste his habitation. |
| Jer 11:19 | know | HVqp1cs | none recorded | 20002 | 0 | But I was like a gentle lamb led to the slaughter. I did not **know** it was against me they devised schemes, saying, “Let us destroy the tree with its fruit, let us cut him off from the land of the living, that his name be remembered no more.” |
| Jer 12:3 | know | HVqp2ms | none recorded | - | 0 | But you, O Lord, **know** me; you see me, and test my heart toward you. Pull them out like sheep for the slaughter, and set them apart for the day of slaughter. |
| Jer 13:12 | know | HVqi1cp | none recorded | - | 0 | “You shall speak to them this word: ‘ Thus says the Lord, the God of Israel, “ Every jar shall be filled with wine.”’ And they will say to you, ‘Do we not indeed **know** that every jar will be filled with wine?’ |
| Jer 15:14 | know | HVqp2ms | none recorded | - | 0 | I will make you serve your enemies in a land that you do not **know**, for in my anger a fire is kindled that shall burn forever.” |
| Jer 15:15 | know | HVqp2ms | none recorded | 14709 | 0 | O Lord, you **know**; remember me and visit me,, and take vengeance for me on my persecutors. In your forbearance take me not away; know that for your sake I bear reproach. |
| Jer 15:15 | know | HVqv2ms | none recorded | - | 0 | O Lord, you **know**; remember me and visit me,, and take vengeance for me on my persecutors. In your forbearance take me not away; know that for your sake I bear reproach. |
| Jer 16:21 | know | HVhrmsc | none recorded | - | 0 | “ Therefore, behold, I will make them **know**, this once I will make them know my power and my might, and they shall know that my name is the Lord.” |
| Jer 16:21 | know | HVhi1cs | none recorded | - | 0 | “ Therefore, behold, I will make them **know**, this once I will make them know my power and my might, and they shall know that my name is the Lord.” |
| Jer 16:21 | know | HVqq3cp | none recorded | - | 0 | “ Therefore, behold, I will make them **know**, this once I will make them know my power and my might, and they shall know that my name is the Lord.” |
| Jer 17:4 | know | HVqp2ms | none recorded | - | 0 | You shall loosen your hand from your heritage that I gave to you, and I will make you serve your enemies in a land that you do not **know**, for in my anger a fire is kindled that shall burn forever.” |
| Jer 17:16 | know | HVqp2ms | none recorded | - | 0 | I have not run away from being your shepherd, nor have I desired the day of sickness. You **know** what came out of my lips; it was before your face. |
| Jer 18:23 | know | HVqp2ms | none recorded | 14602 | 0 | Yet you, O Lord, **know** all their plotting to kill me. Forgive not their iniquity, nor blot out their sin from your sight. Let them be overthrown before you; deal with them in the time of your anger. |
| Jer 22:28 | know | HVqp3cp | none recorded | - | 0 | Is this man Coniah a despised, broken pot, a vessel no one cares for? Why are he and his children hurled and cast into a land that they do not **know**? |
| Jer 24:7 | know | HVqcc | none recorded | 15233, 15941 | 0 | I will give them a heart to **know** me, that I am the Lord, and they shall be my people and I will be their God, for they shall return to me with their whole heart. |
| Jer 26:15 | know | HVqaa | none recorded | - | 0 | Only **know** for certain that if you put me to death, you will bring innocent blood upon yourselves and upon this city and its inhabitants, for in truth the Lord sent me to you to speak all these words in your ears.” |
| Jer 29:11 | know | HVqp1cs | none recorded | 19415 | 0 | For I **know** the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope. |
| Jer 31:34 | know | HVqv2mp | none recorded | - | 0 | And no longer shall each one teach his neighbor and each his brother, saying, ‘ **Know** the Lord,’ for they shall all know me, from the least of them to the greatest, declares the Lord. For I will forgive their iniquity, and I will remember their sin no more.” |
| Jer 31:34 | know | HVqi3mp | none recorded | - | 0 | And no longer shall each one teach his neighbor and each his brother, saying, ‘ **Know** the Lord,’ for they shall all know me, from the least of them to the greatest, declares the Lord. For I will forgive their iniquity, and I will remember their sin no more.” |
| Jer 36:19 | know | HVqj3ms | none recorded | - | 0 | Then the officials said to Baruch, “ Go and hide, you and Jeremiah, and let no one **know** where you are.” |
| Jer 38:24 | know | HVqj3ms | none recorded | 16084 | 0 | Then Zedekiah said to Jeremiah, “Let no one **know** of these words, and you shall not die. |
| Jer 40:14 | know | HVqi2ms | none recorded | - | 0 | and said to him, “Do you **know** that Baalis the king of the Ammonites has sent Ishmael the son of Nethaniah to take your life?” But Gedaliah the son of Ahikam would not believe them. |
| Jer 40:15 | know | HVqi3ms | none recorded | - | 0 | Then Johanan the son of Kareah spoke secretly to Gedaliah at Mizpah, “ Please let me go and strike down Ishmael the son of Nethaniah, and no one will **know** it. Why should he take your life, so that all the Judeans who are gathered about you would be scattered, and the remnant of Judah would perish?” |
| Jer 42:19 | know | HVqaa | none recorded | - | 0 | The Lord has said to you, O remnant of Judah, ‘Do not go to Egypt.’ **Know** for a certainty that I have warned you this day |
| Jer 42:22 | know | HVqaa | none recorded | - | 0 | Now therefore **know** for a certainty that you shall die by the sword, by famine, and by pestilence in the place where you desire to go to live.” |
| Jer 44:28 | know | HVqq3cp | none recorded | - | 0 | And those who escape the sword shall return from the land of Egypt to the land of Judah, few in number; and all the remnant of Judah, who came to the land of Egypt to live, shall **know** whose word will stand, mine or theirs. |
| Jer 44:29 | know | HVqj2mp | none recorded | - | 0 | This shall be the sign to you, declares the Lord, that I will punish you in this place, in order that you may **know** that my words will surely stand against you for harm: |
| Jer 48:17 | know | HVqrmpc | none recorded | - | 0 | Grieve for him, all you who are around him, and all who **know** his name; say, ‘ How the mighty scepter is broken, the glorious staff.’ |
| Jer 48:30 | know | HVqp1cs | none recorded | 14038 | 0 | I **know** his insolence, declares the Lord; his boasts are false, his deeds are false. |
| Jer 50:24 | know | HVqp2fs | none recorded | 14140, 14666 | 0 | I set a snare for you and you were taken, O Babylon, and you did not **know** it; you were found and caught, because you opposed the Lord. |
| Eze 2:5 | know | HVqq3cp | none recorded | - | 0 | And whether they hear or refuse to hear ( for they are a rebellious house ) they will **know** that a prophet has been among them. |
| Eze 5:13 | know | HVqq3cp | none recorded | 13027, 13068, 13163, 13216, 13287, 13328, 14731, 17848 | 0 | “Thus shall my anger spend itself, and I will vent my fury upon them and satisfy myself. And they shall **know** that I am the Lord —that I have spoken in my jealousy — when I spend my fury upon them. |
| Eze 6:7 | know | HVqq2mp | none recorded | - | 0 | And the slain shall fall in your midst, and you shall **know** that I am the Lord. |
| Eze 6:10 | know | HVqq3cp | none recorded | - | 0 | And they shall **know** that I am the Lord. I have not said in vain that I would do this evil to them.” |
| Eze 6:13 | know | HVqq2mp | none recorded | - | 0 | And you shall **know** that I am the Lord, when their slain lie among their idols around their altars, on every high hill, on all the mountaintops, under every green tree, and under every leafy oak, wherever they offered pleasing aroma to all their idols. |
| Eze 6:14 | know | HVqq3cp | none recorded | - | 0 | And I will stretch out my hand against them and make the land desolate and waste, in all their dwelling places, from the wilderness to Riblah. Then they will **know** that I am the Lord.” |
| Eze 7:4 | know | HVqq2mp | none recorded | - | 0 | And my eye will not spare you, nor will I have pity, but I will punish you for your ways, while your abominations are in your midst. Then you will **know** that I am the Lord. |
| Eze 7:9 | know | HVqq2mp | none recorded | 14731 | 0 | And my eye will not spare, nor will I have pity. I will punish you according to your ways, while your abominations are in your midst. Then you will **know** that I am the Lord, who strikes. |
| Eze 7:27 | know | HVqq3cp | none recorded | - | 0 | The king mourns, the prince is wrapped in despair, and the hands of the people of the land are paralyzed by terror. According to their way I will do to them, and according to their judgments I will judge them, and they shall **know** that I am the Lord.” |
| Eze 11:5 | know | HVqp1cs | none recorded | - | 0 | And the Spirit of the Lord fell upon me, and he said to me, “ Say, Thus says the Lord: So you think, O house of Israel. For I **know** the things that come into your mind. |
| Eze 11:10 | know | HVqq2mp | none recorded | - | 0 | You shall fall by the sword. I will judge you at the border of Israel, and you shall **know** that I am the Lord. |
| Eze 11:12 | know | HVqq2mp | none recorded | - | 0 | and you shall **know** that I am the Lord. For you have not walked in my statutes, nor obeyed my rules, but have acted according to the rules of the nations that are around you.” |
| Eze 12:15 | know | HVqq3cp | none recorded | - | 0 | And they shall **know** that I am the Lord, when I disperse them among the nations and scatter them among the countries. |
| Eze 12:16 | know | HVqq3cp | none recorded | - | 0 | But I will let a few of them escape from the sword, from famine and pestilence, that they may declare all their abominations among the nations where they go, and may **know** that I am the Lord.” |
| Eze 12:20 | know | HVqq2mp | none recorded | - | 0 | And the inhabited cities shall be laid waste, and the land shall become a desolation; and you shall **know** that I am the Lord.” |
| Eze 13:9 | know | HVqq2mp | none recorded | - | 0 | My hand will be against the prophets who see false visions and who give lying divinations. They shall not be in the council of my people, nor be enrolled in the register of the house of Israel, nor shall they enter the land of Israel. And you shall **know** that I am the Lord God. |
| Eze 13:14 | know | HVqq2mp | none recorded | - | 0 | And I will break down the wall that you have smeared with whitewash, and bring it down to the ground, so that its foundation will be laid bare. When it falls, you shall perish in the midst of it, and you shall **know** that I am the Lord. |
| Eze 13:21 | know | HVqq2fp | none recorded | - | 0 | Your veils also I will tear off and deliver my people out of your hand, and they shall be no more in your hand as prey, and you shall **know** that I am the Lord. |
| Eze 13:23 | know | HVqq2fp | none recorded | - | 0 | therefore you shall no more see false visions nor practice divination. I will deliver my people out of your hand. And you shall **know** that I am the Lord.” |
| Eze 14:8 | know | HVqq2mp | none recorded | - | 0 | And I will set my face against that man; I will make him a sign and a byword and cut him off from the midst of my people, and you shall **know** that I am the Lord. |
| Eze 14:23 | know | HVqq2mp | none recorded | - | 0 | They will console you, when you see their ways and their deeds, and you shall **know** that I have not done without cause all that I have done in it, declares the Lord God.” |
| Eze 15:7 | know | HVqq2mp | none recorded | - | 0 | And I will set my face against them. Though they escape from the fire, the fire shall yet consume them, and you will **know** that I am the Lord, when I set my face against them. |
| Eze 16:62 | know | HVqq2fs | none recorded | - | 0 | I will establish my covenant with you, and you shall **know** that I am the Lord, |
| Eze 17:12 | know | HVqp2mp | none recorded | - | 0 | “ Say now to the rebellious house, Do you not **know** what these things mean? Tell them, behold, the king of Babylon came to Jerusalem, and took her king and her princes and brought them to him to Babylon. |
| Eze 17:21 | know | HVqq2mp | none recorded | - | 0 | And all the pick of his troops shall fall by the sword, and the survivors shall be scattered to every wind, and you shall **know** that I am the Lord; I have spoken.” |
| Eze 17:24 | know | HVqq3cp | none recorded | 15577 | 0 | And all the trees of the field shall **know** that I am the Lord; I bring low the high tree, and make high the low tree, dry up the green tree, and make the dry tree flourish. I am the Lord; I have spoken, and I will do it.” |
| Eze 20:4 | know | HVhv2ms | none recorded | - | 0 | Will you judge them, son of man, will you judge them? Let them **know** the abominations of their fathers, |
| Eze 20:12 | know | HVqcc | none recorded | - | 0 | Moreover, I gave them my Sabbaths, as a sign between me and them, that they might **know** that I am the Lord who sanctifies them. |
| Eze 20:20 | know | HVqcc | none recorded | - | 0 | and keep my Sabbaths holy that they may be a sign between me and you, that you may **know** that I am the Lord your God.' |
| Eze 20:26 | know | HVqj3mp | none recorded | - | 0 | and I defiled them through their very gifts in their offering up all their firstborn, that I might devastate them. I did it that they might **know** that I am the Lord. |
| Eze 20:38 | know | HVqq2mp | none recorded | - | 0 | I will purge out the rebels from among you, and those who transgress against me. I will bring them out of the land where they sojourn, but they shall not enter the land of Israel. Then you will **know** that I am the Lord. |
| Eze 20:42 | know | HVqq2mp | none recorded | - | 0 | And you shall **know** that I am the Lord, when I bring you into the land of Israel, the country that I swore to give to your fathers. |
| Eze 20:44 | know | HVqq2mp | none recorded | - | 0 | And you shall **know** that I am the Lord, when I deal with you for my name’s sake, not according to your evil ways, nor according to your corrupt deeds, O house of Israel, declares the Lord God.” |
| Eze 21:5 | know | HVqq3cp | none recorded | 15961 | 0 | And all flesh shall **know** that I am the Lord. I have drawn my sword from its sheath; it shall not be sheathed again. |
| Eze 22:16 | know | HVqq2fs | none recorded | - | 0 | And you shall be profaned by your own doing in the sight of the nations, and you shall **know** that I am the Lord.” |
| Eze 22:22 | know | HVqq2mp | none recorded | 13372, 14748 | 0 | As silver is melted in a furnace, so you shall be melted in the midst of it, and you shall **know** that I am the Lord; I have poured out my wrath upon you.” |
| Eze 23:49 | know | HVqq2mp | none recorded | - | 0 | And they shall return your lewdness upon you, and you shall bear the penalty for your sinful idolatry, and you shall **know** that I am the Lord God.” |
| Eze 24:24 | know | HVqq2mp | none recorded | - | 0 | Thus shall Ezekiel be to you a sign; according to all that he has done you shall do. When this comes, then you will **know** that I am the Lord God.’ |
| Eze 24:27 | know | HVqq3cp | none recorded | - | 0 | On that day your mouth will be opened to the fugitive, and you shall speak and be no longer mute. So you will be a sign to them, and they will **know** that I am the Lord.” |
| Eze 25:5 | know | HVqq2mp | none recorded | - | 0 | I will make Rabbah a pasture for camels and Ammon a fold for flocks. Then you will **know** that I am the Lord. |
| Eze 25:7 | know | HVqq2ms | none recorded | - | 0 | therefore, behold, I have stretched out my hand against you, and will hand you over as plunder to the nations. And I will cut you off from the peoples and will make you perish out of the countries; I will destroy you. Then you will **know** that I am the Lord. |
| Eze 25:11 | know | HVqq3cp | none recorded | - | 0 | and I will execute judgments upon Moab. Then they will **know** that I am the Lord. |
| Eze 25:14 | know | HVqq3cp | none recorded | - | 0 | And I will lay my vengeance upon Edom by the hand of my people Israel, and they shall do in Edom according to my anger and according to my wrath, and they shall **know** my vengeance, declares the Lord God. |
| Eze 25:17 | know | HVqq3cp | none recorded | 13376, 14731 | 0 | I will execute great vengeance on them with wrathful rebukes. Then they will **know** that I am the Lord, when I lay my vengeance upon them.” |
| Eze 26:6 | know | HVqq3cp | none recorded | - | 0 | and her daughters on the mainland shall be killed by the sword. Then they will **know** that I am the Lord. |
| Eze 28:19 | know | HVqrmpc | none recorded | - | 0 | All who **know** you among the peoples are appalled at you; you have come to a dreadful end and shall be no more forever.” |
| Eze 28:22 | know | HVqq3cp | none recorded | - | 0 | and say, Thus says the Lord God: “ Behold, I am against you, O Sidon, and I will manifest my glory in your midst. And they shall **know** that I am the Lord when I execute judgments in her and manifest my holiness in her; |
| Eze 28:23 | know | HVqq3cp | none recorded | - | 0 | for I will send pestilence into her, and blood into her streets; and the slain shall fall in her midst, by the sword that is against her on every side. Then they will **know** that I am the Lord. |
| Eze 28:24 | know | HVqq3cp | none recorded | - | 0 | “And for the house of Israel there shall be no more a brier to prick or a thorn to hurt them among all their neighbors who have treated them with contempt. Then they will **know** that I am the Lord God. |
| Eze 28:26 | know | HVqq3cp | none recorded | - | 0 | And they shall dwell securely in it, and they shall build houses and plant vineyards. They shall dwell securely, when I execute judgments upon all their neighbors who have treated them with contempt. Then they will **know** that I am the Lord their God.” |
| Eze 29:6 | know | HVqq3cp | none recorded | - | 0 | Then all the inhabitants of Egypt shall **know** that I am the Lord. “ Because you have been a staff of reed to the house of Israel, |
| Eze 29:9 | know | HVqq3cp | none recorded | - | 0 | and the land of Egypt shall be a desolation and a waste. Then they will **know** that I am the Lord. “ Because you said, ‘The Nile is mine, and I made it,’ |
| Eze 29:16 | know | HVqq3cp | none recorded | - | 0 | And it shall never again be the reliance of the house of Israel, recalling their iniquity, when they turn to them for aid. Then they will **know** that I am the Lord God.” |
| Eze 29:21 | know | HVqq3cp | none recorded | - | 0 | “On that day I will cause a horn to spring up for the house of Israel, and I will open your lips among them. Then they will **know** that I am the Lord.” |
| Eze 30:8 | know | HVqq3cp | none recorded | - | 0 | Then they will **know** that I am the Lord, when I have set fire to Egypt, and all her helpers are broken. |
| Eze 30:19 | know | HVqq3cp | none recorded | - | 0 | Thus I will execute judgments on Egypt. Then they will **know** that I am the Lord.” |
| Eze 30:25 | know | HVqq3cp | none recorded | - | 0 | I will strengthen the arms of the king of Babylon, but the arms of Pharaoh shall fall. Then they shall **know** that I am the Lord, when I put my sword into the hand of the king of Babylon and he stretches it out against the land of Egypt. |
| Eze 30:26 | know | HVqq3cp | none recorded | - | 0 | And I will scatter the Egyptians among the nations and disperse them throughout the countries. Then they will **know** that I am the Lord.” |
| Eze 32:15 | know | HVqq3cp | none recorded | - | 0 | When I make the land of Egypt desolate, and when the land is desolate of all that fills it, when I strike down all who dwell in it, then they will **know** that I am the Lord. |
| Eze 33:29 | know | HVqq3cp | none recorded | - | 0 | Then they will **know** that I am the Lord, when I have made the land a desolation and a waste because of all their abominations that they have committed. |
| Eze 33:33 | know | HVqq3cp | none recorded | - | 0 | When this comes —and come it will!— then they will **know** that a prophet has been among them.” |
| Eze 34:27 | know | HVqq3cp | none recorded | - | 0 | And the trees of the field shall yield their fruit, and the earth shall yield its increase, and they shall be secure in their land. And they shall **know** that I am the Lord, when I break the bars of their yoke, and deliver them from the hand of those who enslaved them. |
| Eze 34:30 | know | HVqq3cp | none recorded | - | 0 | And they shall **know** that I am the Lord their God with them, and that they, the house of Israel, are my people, declares the Lord God. |
| Eze 35:4 | know | HVqq2ms | none recorded | - | 0 | I will lay your cities waste, and you shall become a desolation, and you shall **know** that I am the Lord. |
| Eze 35:9 | know | HVqq2mp | none recorded | - | 0 | I will make you a perpetual desolation, and your cities shall not be inhabited. Then you will **know** that I am the Lord. |
| Eze 35:12 | know | HVqq2ms | none recorded | - | 0 | And you shall **know** that I am the Lord. “I have heard all the revilings that you uttered against the mountains of Israel, saying, ‘They are laid desolate; they are given us to devour.’ |
| Eze 35:15 | know | HVqq3cp | none recorded | - | 0 | As you rejoiced over the inheritance of the house of Israel, because it was desolate, so I will deal with you; you shall be desolate, Mount Seir, and all Edom, all of it. Then they will **know** that I am the Lord. |
| Eze 36:11 | know | HVqq2mp | none recorded | - | 0 | And I will multiply on you man and beast, and they shall multiply and be fruitful. And I will cause you to be inhabited as in your former times, and will do more good to you than ever before. Then you will **know** that I am the Lord. |
| Eze 36:23 | know | HVqq3cp | none recorded | - | 0 | And I will vindicate the holiness of my great name, which has been profaned among the nations, and which you have profaned among them. And the nations will **know** that I am the Lord, declares the Lord God, when through you I vindicate my holiness before their eyes. |
| Eze 36:36 | know | HVqq3cp | none recorded | - | 0 | Then the nations that are left all around you shall **know** that I am the Lord; I have rebuilt the ruined places and replanted that which was desolate. I am the Lord; I have spoken, and I will do it. |
| Eze 36:38 | know | HVqq3cp | none recorded | - | 0 | Like the flock for sacrifices, like the flock at Jerusalem during her appointed feasts, so shall the waste cities be filled with flocks of people. Then they will **know** that I am the Lord.” |
| Eze 37:3 | know | HVqp2ms | none recorded | - | 0 | And he said to me, “ Son of man, can these bones live?” And I answered, “O Lord God, you **know**.” |
| Eze 37:6 | know | HVqq2mp | none recorded | - | 0 | And I will lay sinews upon you, and will cause flesh to come upon you, and cover you with skin, and put breath in you, and you shall live, and you shall **know** that I am the Lord.” |
| Eze 37:13 | know | HVqq2mp | none recorded | - | 0 | And you shall **know** that I am the Lord, when I open your graves, and raise you from your graves, O my people. |
| Eze 37:14 | know | HVqq2mp | none recorded | - | 0 | And I will put my Spirit within you, and you shall live, and I will place you in your own land. Then you shall **know** that I am the Lord; I have spoken, and I will do it, declares the Lord.” |
| Eze 37:28 | know | HVqq3cp | none recorded | - | 0 | Then the nations will **know** that I am the Lord who sanctifies Israel, when my sanctuary is in their midst forevermore.” |
| Eze 38:14 | know | HVqi2ms | none recorded | - | 0 | “ Therefore, son of man, prophesy, and say to Gog, Thus says the Lord God: On that day when my people Israel are dwelling securely, will you not **know** it? |
| Eze 38:16 | know | HVqcc | none recorded | - | 0 | You will come up against my people Israel, like a cloud covering the land. In the latter days I will bring you against my land, that the nations may **know** me, when through you, O Gog, I vindicate my holiness before their eyes. |
| Eze 38:23 | know | HVqq3cp | none recorded | - | 0 | So I will show my greatness and my holiness and make myself known in the eyes of many nations. Then they will **know** that I am the Lord. |
| Eze 39:6 | know | HVqq3cp | none recorded | - | 0 | I will send fire on Magog and on those who dwell securely in the coastlands, and they shall **know** that I am the Lord. |
| Eze 39:7 | know | HVqq3cp | none recorded | - | 0 | “And my holy name I will make known in the midst of my people Israel, and I will not let my holy name be profaned anymore. And the nations shall **know** that I am the Lord, the Holy One in Israel. |
| Eze 39:22 | know | HVqq3cp | none recorded | - | 0 | The house of Israel shall **know** that I am the Lord their God, from that day forward. |
| Eze 39:23 | know | HVqq3cp | none recorded | - | 0 | And the nations shall **know** that the house of Israel went into captivity for their iniquity, because they dealt so treacherously with me that I hid my face from them and gave them into the hand of their adversaries, and they all fell by the sword. |
| Eze 39:28 | know | HVqq3cp | none recorded | - | 0 | Then they shall **know** that I am the Lord their God, because I sent them into exile among the nations and then assembled them into their own land. I will leave none of them remaining among the nations anymore. |
| Dan 2:3 | know | HVqcc | none recorded | - | 0 | And the king said to them, “I had a dream, and my spirit is troubled to **know** the dream.” |
| Dan 9:25 | know | HVqu2ms | none recorded | - | 0 | **Know** therefore and understand that from the going out of the word to restore and build Jerusalem to the coming of an anointed one, a prince, there shall be seven weeks. And for sixty-two weeks it shall be built again with squares and moat, but in a troubled time. |
| Dan 10:20 | know | HVqp2ms | none recorded | - | 0 | Then he said, “Do you **know** why I have come to you? But now I will return to fight against the prince of Persia; and when I go out, behold, the prince of Greece will come. |
| Dan 11:32 | know | HVqrmpc | none recorded | - | 0 | He shall seduce with flattery those who violate the covenant, but the people who **know** their God shall stand firm and take action. |
| Dan 11:38 | know | HVqp3cp | none recorded | - | 0 | He shall honor the god of fortresses instead of these. A god whom his fathers did not **know** he shall honor with gold and silver, with precious stones and costly gifts. |
| Hos 2:8 | know | HVqp3fs | none recorded | - | 0 | And she did not **know** that it was I who gave her the grain, the wine, and the oil, and who lavished on her silver and gold, which they used for Baal. |
| Hos 2:20 | know | HVqq2fs | none recorded | - | 0 | I will betroth you to me in faithfulness. And you shall **know** the Lord. |
| Hos 5:3 | know | HVqp1cs | none recorded | 18877, 19223 | 0 | I **know** Ephraim, and Israel is not hidden from me; for now, O Ephraim, you have played the whore; Israel is defiled. |
| Hos 5:4 | know | HVqp3cp | none recorded | 15087, 17069, 19223 | 0 | Their deeds do not permit them to return to their God. For the spirit of whoredom is within them, and they **know** not the Lord. |
| Hos 6:3 | know | HVqu1cp | none recorded | - | 0 | Let us **know**; let us press on to know the Lord; his going out is sure as the dawn; he will come to us as the showers, as the spring rains that water the earth.” |
| Hos 6:3 | know | HVqcc | none recorded | - | 0 | Let us **know**; let us press on to know the Lord; his going out is sure as the dawn; he will come to us as the showers, as the spring rains that water the earth.” |
| Hos 8:2 | know | HVqp1cp | none recorded | 19039, 19040 | 0 | To me they cry, “My God, we— Israel — **know** you.” |
| Hos 9:7 | know | HVqi3mp | none recorded | - | 0 | The days of punishment have come; the days of recompense have come; Israel shall **know** it. The prophet is a fool; the man of the spirit is mad, because of your great iniquity and great hatred. |
| Hos 11:3 | know | HVqp3cp | none recorded | - | 0 | Yet it was I who taught Ephraim to walk; I took them up by their arms, but they did not **know** that I healed them. |
| Hos 13:4 | know | HVqi2ms | none recorded | - | 0 | But I am the Lord your God from the land of Egypt; you **know** no God but me, and besides me there is no savior. |
| Hos 14:9 | know | HVqu3ms | none recorded | - | 0 | Whoever is wise, let him understand these things; whoever is discerning, let him **know** them; for the ways of the Lord are right, and the upright walk in them, but transgressors stumble in them. |
| Joe 2:27 | know | HVqq2mp | none recorded | - | 0 | You shall **know** that I am in the midst of Israel, and that I am the Lord your God and there is none else. And my people shall never again be put to shame. |
| Joe 3:17 | know | HVqq2mp | none recorded | - | 0 | “So you shall **know** that I am the Lord your God, who dwells in Zion, my holy mountain. And Jerusalem shall be holy, and strangers shall never again pass through it. |
| Amo 3:10 | know | HVqp3cp | none recorded | - | 0 | “They do not **know** how to do right,” declares the Lord, “those who store up violence and robbery in their strongholds.” |
| Amo 5:12 | know | HVqp1cs | none recorded | - | 0 | For I **know** how many are your transgressions and how great are your sins — you who afflict the righteous, who take a bribe, and turn aside the needy in the gate. |
| Jon 1:7 | know | HVqc1cp | none recorded | - | 0 | And they said to one another, “ Come, let us cast lots, that we may **know** on whose account this evil has come upon us.” So they cast lots, and the lot fell on Jonah. |
| Jon 1:12 | know | HVqrmsa | none recorded | - | 0 | He said to them, “ Pick me up and hurl me into the sea; then the sea will quiet down for you, for I **know** it is because of me that this great tempest has come upon you.” |
| Jon 4:11 | know | HVqp3ms | none recorded | - | 0 | And should not I pity Nineveh, that great city, in which there are more than 120,000 persons who do not **know** their right hand from their left, and also much cattle?” |
| Mic 3:1 | know | HVqcc | none recorded | - | 0 | And I said: Hear, you heads of Jacob and rulers of the house of Israel! Is it not for you to **know** justice?— |
| Mic 4:12 | know | HVqp3cp | none recorded | - | 0 | But they do not **know** the thoughts of the Lord; they do not understand his plan, that he has gathered them as sheaves to the threshing floor. |
| Mic 6:5 | know | HVqcc | none recorded | - | 0 | O my people, remember what Balak king of Moab devised, and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal, that you may **know** the righteous acts of the Lord.” |
| Zec 2:9 | know | HVqq2mp | none recorded | - | 0 | “ Behold, I will shake my hand over them, and they shall become plunder for those who served them. Then you will **know** that the Lord of hosts has sent me. |
| Zec 2:11 | know | HVqq2fs | none recorded | - | 0 | And many nations shall join themselves to the Lord in that day, and shall be my people. And I will dwell in your midst, and you shall **know** that the Lord of hosts has sent me to you. |
| Zec 4:5 | know | HVqp2ms | none recorded | - | 0 | Then the angel who talked with me answered and said to me, “Do you not **know** what these are?” I said, “ No, my lord.” |
| Zec 4:9 | know | HVqq2ms | none recorded | - | 0 | “The hands of Zerubbabel have laid the foundation of this house; his hands shall also complete it. Then you will **know** that the Lord of hosts has sent me to you. |
| Zec 6:15 | know | HVqq2mp | none recorded | - | 0 | “And those who are far off shall come and help to build the temple of the Lord. And you shall **know** that the Lord of hosts has sent me to you. And this shall come to pass, if you will diligently obey the voice of the Lord your God.” |
| Mal 2:4 | know | HVqq2mp | none recorded | - | 0 | So shall you **know** that I have sent this command to you, that my covenant with Levi may stand, says the Lord of hosts. |
| 2Ch 2:8 | know how | HVqrmpa | none recorded | - | 0 | Send me also cedar, cypress, and algum timber from Lebanon, for I know that your servants **know how** to cut timber in Lebanon. And my servants will be with your servants, |
| Jer 1:6 | know how | HVqp1cs | none recorded | - | 0 | Then I said, “ Ah, Lord God! Behold, I do not **know how** to speak, for I am only a youth.” |
| Jer 6:15 | know how | HVqp3cp | none recorded | - | 0 | Were they ashamed when they committed abomination? No, they were not at all ashamed; they did not **know how** to blush. Therefore they shall fall among those who fall; at the time that I punish them, they shall be overthrown,” says the Lord. |
| Jer 8:12 | know how | HVqp3cp | none recorded | - | 0 | Were they ashamed when they committed abomination? No, they were not at all ashamed; they did not **know how** to blush. Therefore they shall fall among the fallen; when I punish them, they shall be overthrown, says the Lord. |
| Deu 8:5 | know then | HVqq2ms | none recorded | 15939 | 0 | **Know then** in your heart that, as a man disciplines his son, the Lord your God disciplines you. |
| Gen 3:5 | knowing | HVqrmpc | none recorded | - | 0 | For God knows that when you eat of it your eyes will be opened, and you will be like God, **knowing** good and evil.” |
| Gen 3:22 | knowing | HVqcc | none recorded | - | 0 | Then the Lord God said, “ Behold, the man has become like one of us in **knowing** good and evil. Now, lest he reach out his hand and take also of the tree of life and eat, and live forever —” |
| 2Ki 4:39 | knowing | HVqp3cp | none recorded | - | 0 | One of them went out into the field to gather herbs, and found a wild vine and gathered from it his lap full of wild gourds, and came and cut them up into the pot of stew, not **knowing** what they were. |
| Deu 1:39 | knowledge | HVqp3cp | none recorded | - | 0 | And as for your little ones, who you said would become a prey, and your children, who today have no **knowledge** of good or evil, they shall go in there. And to them I will give it, and they shall possess it. |
| 1Ki 2:32 | knowledge | HVqp3ms | none recorded | - | 0 | The Lord will bring back his bloody deeds on his own head, because, without the **knowledge** of my father David, he attacked and killed with the sword two men more righteous and better than himself, Abner the son of Ner, commander of the army of Israel, and Amasa the son of Jether, commander of the army of Judah. |
| Neh 10:28 | knowledge | HVqrmsa | none recorded | - | 0 | “The rest of the people, the priests, the Levites, the gatekeepers, the singers, the temple servants, and all who have separated themselves from the peoples of the lands to the Law of God, their wives, their sons, their daughters, all who have **knowledge** and understanding, |
| Est 2:22 | knowledge | HVNw3ms | none recorded | 14199 | 0 | And this came to the **knowledge** of Mordecai, and he told it to Queen Esther, and Esther told the king in the name of Mordecai. |
| Psa 14:4 | knowledge | HVqp3cp | none recorded | - | 0 | Have they no **knowledge**, all the evildoers who eat up my people as they eat bread and do not call upon the Lord? |
| Psa 53:4 | knowledge | HVqp3cp | none recorded | - | 0 | Have those who work evil no **knowledge**, who eat up my people as they eat bread, and do not call upon God? |
| Psa 71:15 | knowledge | HVqp1cs | none recorded | - | 0 | My mouth will tell of your righteous acts, of your deeds of salvation all the day, for their number is past my **knowledge**. |
| Psa 82:5 | knowledge | HVqp3cp | none recorded | - | 0 | They have neither **knowledge** nor understanding, they walk about in darkness; all the foundations of the earth are shaken. |
| Pro 28:2 | knowledge | HVqrmsa | none recorded | - | 0 | When a land transgresses, it has many rulers, but with a man of understanding and **knowledge**, its stability will long continue. |
| Ecc 9:11 | knowledge | HVqrmpa | none recorded | - | 0 | Again I saw that under the sun the race is not to the swift, nor the battle to the strong, nor bread to the wise, nor riches to the intelligent, nor favor to those with **knowledge**, but time and chance happen to them all. |
| Isa 45:20 | knowledge | HVqp3cp | none recorded | - | 0 | “Assemble yourselves and come; draw near together, you survivors of the nations! They have no **knowledge** who carry about their wooden idols, and keep on praying to a god that cannot save. |
| Isa 56:10 | knowledge | HVqp3cp | none recorded | - | 0 | His watchmen are blind; they are all without **knowledge**; they are all silent dogs; they cannot bark, dreaming, lying down, loving to slumber. |
| Isa 58:3 | knowledge | HVqi2ms | none recorded | 15344, 15669, 19957 | 0 | ‘ Why have we fasted, and you see it not? Why have we humbled ourselves, and you take no **knowledge** of it?’ Behold, in the day of your fast you seek your own pleasure, and oppress all your workers. |
| Jer 14:18 | knowledge | HVqp3cp | none recorded | - | 0 | If I go out into the field, behold, those pierced by the sword! And if I enter the city, behold, the diseases of famine! For both prophet and priest ply their trade through the land and have no **knowledge**.’” |
| Hab 2:14 | knowledge | HVqcc | none recorded | - | 0 | For the earth will be filled with the **knowledge** of the glory of the Lord as the waters cover the sea. |
| Gen 41:21 | known | HVNp3ms | none recorded | - | 0 | but when they had eaten them no one would have **known** that they had eaten them, for they were still as ugly as at the beginning. Then I awoke. |
| Exo 2:14 | known | HVNp3ms | none recorded | 18884, 19224 | 0 | He answered, “ Who made you a prince and a judge over us? Do you mean to kill me as you killed the Egyptian?” Then Moses was afraid, and thought, “ Surely the thing is **known**.” |
| Exo 6:3 | known | HVNp1cs | none recorded | - | 0 | I appeared to Abraham, to Isaac, and to Jacob, as God Almighty, but by my name the Lord I did not make myself **known** to them. |
| Exo 21:36 | known | HVNp3ms | none recorded | - | 0 | Or if it is **known** that the ox has been accustomed to gore in the past, and its owner has not kept it in, he shall repay ox for ox, and the dead beast shall be his. |
| Exo 33:16 | known | HVNi3ms | none recorded | - | 0 | For how shall it be **known** that I have found favor in your sight, I and your people? Is it not in your going with us, so that we are distinct, I and your people, from every other people on the face of the earth?” |
| Lev 4:14 | known | HVNq3fs | none recorded | - | 0 | when the sin which they have committed becomes **known**, the assembly shall offer a bull from the herd for a sin offering and bring it in front of the tent of meeting. |
| Num 31:17 | known | HVqrfsa | none recorded | - | 0 | Now therefore, kill every male among the little ones, and kill every woman who has **known** man by lying with him. |
| Num 31:18 | known | HVqp3cp | none recorded | - | 0 | But all the young girls who have not **known** man by lying with him keep alive for yourselves. |
| Num 31:35 | known | HVqp3cp | none recorded | - | 0 | and 32,000 persons in all, women who had not **known** man by lying with him. |
| Deu 4:9 | known | HVhq2ms | none recorded | - | 0 | “ Only take care, and keep your soul diligently, lest you forget the things that your eyes have seen, and lest they depart from your heart all the days of your life. Make them **known** to your children and your children’s children — |
| Deu 11:2 | known | HVqp3cp | none recorded | - | 0 | And consider today ( since I am not speaking to your children who have not **known** or seen it), consider the discipline of the Lord your God, his greatness, his mighty hand and his outstretched arm, |
| Deu 11:28 | known | HVqp2mp | none recorded | - | 0 | and the curse, if you do not obey the commandments of the Lord your God, but turn aside from the way that I am commanding you today, to go after other gods that you have not **known**. |
| Deu 13:2 | known | HVqp2ms | none recorded | - | 0 | and the sign or wonder that he tells you comes to pass, and if he says, ‘Let us go after other gods,’ which you have not **known**, ‘and let us serve them,’ |
| Deu 13:6 | known | HVqp2ms | none recorded | - | 0 | “ If your brother, the son of your mother, or your son or your daughter or the wife you embrace or your friend who is as your own soul entices you secretly, saying, ‘Let us go and serve other gods,’ which neither you nor your fathers have **known**, |
| Deu 13:13 | known | HVqp2mp | none recorded | - | 0 | that certain worthless fellows have gone out among you and have drawn away the inhabitants of their city, saying, ‘Let us go and serve other gods,’ which you have not **known**, |
| Deu 21:1 | known | HVNp3ms | none recorded | - | 0 | “ If in the land that the Lord your God is giving you to possess someone is found slain, lying in the open country, and it is not **known** who killed him, |
| Deu 28:33 | known | HVqp2ms | none recorded | - | 0 | A nation that you have not **known** shall eat up the fruit of your ground and of all your labors, and you shall be only oppressed and crushed continually, |
| Deu 28:36 | known | HVqp2ms | none recorded | - | 0 | “The Lord will bring you and your king whom you set over you to a nation that neither you nor your fathers have **known**. And there you shall serve other gods of wood and stone. |
| Deu 28:64 | known | HVqp2ms | none recorded | - | 0 | “And the Lord will scatter you among all peoples, from one end of the earth to the other, and there you shall serve other gods of wood and stone, which neither you nor your fathers have **known**. |
| Deu 29:26 | known | HVqp3cp | none recorded | - | 0 | and went and served other gods and worshiped them, gods whom they had not **known** and whom he had not allotted to them. |
| Deu 31:13 | known | HVqp3cp | none recorded | - | 0 | and that their children, who have not **known** it, may hear and learn to fear the Lord your God, as long as you live in the land that you are going over the Jordan to possess.” |
| Deu 32:17 | known | HVqp3cp | none recorded | - | 0 | They sacrificed to demons that were not God, to gods they had never **known**, to new gods that had come recently, whom your fathers had never dreaded. |
| Judg 3:2 | known | HVqp3cp | none recorded | - | 0 | It was only in order that the generations of the people of Israel might know war, to teach war to those who had not **known** it before. |
| Judg 16:9 | known | HVNp3ms | none recorded | - | 0 | Now she had men lying in ambush in an inner chamber. And she said to him, “The Philistines are upon you, Samson!” But he snapped the bowstrings, as a thread of flax snaps when it touches the fire. So the secret of his strength was not **known**. |
| Judg 21:12 | known | HVqp3fs | none recorded | - | 0 | And they found among the inhabitants of Jabesh-gilead 400 young virgins who had not **known** a man by lying with him, and they brought them to the camp at Shiloh, which is in the land of Canaan. |
| Rut 3:3 | known | HVNj2fs | none recorded | - | 0 | Wash therefore and anoint yourself, and put on your cloak and go down to the threshing floor, but do not make yourself **known** to the man until he has finished eating and drinking. |
| Rut 3:14 | known | HVNj3ms | none recorded | - | 0 | So she lay at his feet until the morning, but arose before one could recognize another. And he said, “Let it not be **known** that the woman came to the threshing floor.” |
| 1Sa 6:3 | known | HVNq3ms | none recorded | - | 0 | They said, “If you send away the ark of the God of Israel, do not send it empty, but by all means return him a guilt offering. Then you will be healed, and it will be **known** to you why his hand does not turn away from you.” |
| 1Sa 22:15 | known | HVqp3ms | none recorded | - | 0 | Is today the first time that I have inquired of God for him? No! Let not the king impute anything to his servant or to all the house of my father, for your servant has **known** nothing of all this, much or little.” |
| 2Sa 17:19 | known | HVNp3ms | none recorded | - | 0 | And the woman took and spread a covering over the well’s mouth and scattered grain on it, and nothing was **known** of it. |
| 2Sa 22:44 | known | HVqp1cs | none recorded | - | 0 | “You delivered me from strife with my people; you kept me as the head of the nations; people whom I had not **known** served me. |
| 1Ki 14:2 | known | HVqi3mp | none recorded | - | 0 | And Jeroboam said to his wife, “ Arise, and disguise yourself, that it not be **known** that you are the wife of Jeroboam, and go to Shiloh. Behold, Ahijah the prophet is there, who said of me that I should be king over this people. |
| 1Ki 18:36 | known | HVNi3ms | none recorded | - | 0 | And at the time of the offering of the oblation, Elijah the prophet came near and said, “O Lord, God of Abraham, Isaac, and Israel, let it be **known** this day that you are God in Israel, and that I am your servant, and that I have done all these things at your word. |
| 1Ch 16:8 | known | HVhv2mp | none recorded | - | 0 | Oh give thanks to the Lord; call upon his name; make **known** his deeds among the peoples! |
| 1Ch 17:19 | known | HVhcc | none recorded | - | 0 | For your servant’s sake, O Lord, and according to your own heart, you have done all this greatness, in making **known** all these great things. |
| Neh 4:15 | known | HVNp3ms | none recorded | - | 0 | When our enemies heard that it was **known** to us and that God had frustrated their plan, we all returned to the wall, each to his work. |
| Neh 9:14 | known | HVhp2ms | none recorded | - | 0 | and you made **known** to them your holy Sabbath and commanded them commandments and statutes and a law by Moses your servant. |
| Job 38:3 | known | HVhv2ms | none recorded | - | 0 | Dress for action like a man; I will question you, and you make it **known** to me. |
| Job 40:7 | known | HVhv2ms | none recorded | - | 0 | “ Dress for action like a man; I will question you, and you make it **known** to me. |
| Job 42:4 | known | HVhv2ms | none recorded | 20603, 20604, 20605 | 0 | ‘ Hear, and I will speak; I will question you, and you make it **known** to me.’ |
| Job 42:11 | known | HVqrmpc | none recorded | - | 0 | Then came to him all his brothers and sisters and all who had **known** him before, and ate bread with him in his house. And they showed him sympathy and comforted him for all the evil that the Lord had brought upon him. And each of them gave him a piece of money and a ring of gold. |
| Psa 9:16 | known | HVNp3ms | none recorded | - | 0 | The Lord has made himself **known**; he has executed judgment; the wicked are snared in the work of their own hands. Higgaion. Selah |
| Psa 16:11 | known | HVhi2ms | none recorded | 18370 | 0 | You make **known** to me the path of life; in your presence there is fullness of joy; at your right hand are pleasures forevermore. |
| Psa 18:43 | known | HVqp1cs | none recorded | - | 0 | You delivered me from strife with the people; you made me the head of the nations; people whom I had not **known** served me. |
| Psa 25:14 | known | HVhcc | none recorded | - | 0 | The friendship of the Lord is for those who fear him, and he makes **known** to them his covenant. |
| Psa 31:7 | known | HVqp2ms | none recorded | 13921, 16426, 19296 | 0 | I will rejoice and be glad in your steadfast love, because you have seen my affliction; you have **known** the distress of my soul, |
| Psa 48:3 | known | HVNp3ms | none recorded | - | 0 | Within her citadels God has made himself **known** as a fortress. |
| Psa 67:2 | known | HVqcc | none recorded | - | 0 | that your way may be **known** on earth, your saving power among all nations. |
| Psa 76:1 | known | HVNrmsa | none recorded | - | 0 | To the choirmaster: with stringed instruments. A Psalm of Asaph. A Song. In Judah God is **known**; his name is great in Israel. |
| Psa 77:14 | known | HVhp2ms | none recorded | - | 0 | You are the God who works wonders; you have made **known** your might among the peoples. |
| Psa 78:3 | known | HVqw1cp | none recorded | - | 0 | things that we have heard and **known**, that our fathers have told us. |
| Psa 79:10 | known | HVNi3ms | none recorded | - | 0 | Why should the nations say, “ Where is their God?” Let the avenging of the outpoured blood of your servants be **known** among the nations before our eyes! |
| Psa 81:5 | known | HVqp1cs | none recorded | - | 0 | He made it a decree in Joseph when he went out over the land of Egypt. I hear a language I had not **known**: |
| Psa 88:12 | known | HVNi3ms | none recorded | - | 0 | Are your wonders **known** in the darkness, or your righteousness in the land of forgetfulness? |
| Psa 89:1 | known | HVhi1cs | none recorded | - | 0 | A Maskil of Ethan the Ezrahite. I will sing of the steadfast love of the Lord forever; with my mouth I will make **known** your faithfulness to all generations. |
| Psa 95:10 | known | HVqp3cp | none recorded | - | 0 | For forty years I loathed that generation and said, “They are a people who go astray in their heart, and they have not **known** my ways.” |
| Psa 98:2 | known | HVhp3ms | none recorded | - | 0 | The Lord has made **known** his salvation; he has revealed his righteousness in the sight of the nations. |
| Psa 103:7 | known | HVhi3ms | none recorded | 14515 | 0 | He made **known** his ways to Moses, his acts to the people of Israel. |
| Psa 105:1 | known | HVhv2mp | none recorded | - | 0 | Oh give thanks to the Lord; call upon his name; make **known** his deeds among the peoples! |
| Psa 106:8 | known | HVhcc | none recorded | - | 0 | Yet he saved them for his name’s sake, that he might make **known** his mighty power. |
| Psa 119:152 | known | HVqp1cs | none recorded | - | 0 | Long have I **known** from your testimonies that you have founded them forever. |
| Psa 139:1 | known | HVqw2ms | none recorded | - | 0 | To the choirmaster. A Psalm of David. O Lord, you have searched me and **known** me! |
| Psa 145:12 | known | HVhcc | none recorded | - | 0 | to make **known** to the children of man your mighty deeds, and the glorious splendor of your kingdom. |
| Pro 1:23 | known | HVhc1cs | none recorded | 20162 | 0 | If you turn at my reproof, behold, I will pour out my spirit to you; I will make my words **known** to you. |
| Pro 12:16 | known | HVNi3ms | none recorded | 14187 | 0 | The vexation of a fool is **known** at once, but the prudent ignores an insult. |
| Pro 14:33 | known | HVNi3fs | none recorded | - | 0 | Wisdom rests in the heart of a man of understanding, but it makes itself **known** even in the midst of fools. |
| Pro 22:19 | known | HVhp1cs | none recorded | - | 0 | That your trust may be in the Lord, I have made them **known** to you today, even to you. |
| Pro 31:23 | known | HVNrmsa | none recorded | - | 0 | Her husband is **known** in the gates when he sits among the elders of the land. |
| Ecc 6:5 | known | HVqp3ms | none recorded | - | 0 | Moreover, it has not seen the sun or **known** anything, yet it finds rest rather than he. |
| Ecc 6:10 | known | HVNrmsa | none recorded | - | 0 | Whatever has come to be has already been named, and it is **known** what man is, and that he is not able to dispute with one stronger than he. |
| Isa 12:4 | known | HVhv2mp | none recorded | - | 0 | And you will say in that day: “Give thanks to the Lord, call upon his name, make **known** his deeds among the peoples, proclaim that his name is exalted. |
| Isa 12:5 | known | HVHsfsa | none recorded | - | 0 | “Sing praises to the Lord, for he has done gloriously; let this be made **known** in all the earth. |
| Isa 19:21 | known | HVNq3ms | none recorded | 14971 | 0 | And the Lord will make himself **known** to the Egyptians, and the Egyptians will know the Lord in that day and worship with sacrifice and offering, and they will make vows to the Lord and perform them. |
| Isa 38:19 | known | HVhi3ms | none recorded | - | 0 | The living, the living, he thanks you, as I do this day; the father makes **known** to the children your faithfulness. |
| Isa 40:28 | known | HVqp2ms | none recorded | - | 0 | Have you not **known**? Have you not heard? The Lord is the everlasting God, the Creator of the ends of the earth. He does not faint or grow weary; his understanding is unsearchable. |
| Isa 42:16 | known | HVqp3cp | none recorded | - | 0 | And I will lead the blind in a way that they do not know, in paths that they have not **known** I will guide them. I will turn the darkness before them into light, the rough places into level ground. These are the things I do, and I do not forsake them. |
| Isa 47:13 | known | HVhrmpa | none recorded | - | 0 | You are wearied with your many counsels; let them stand forth and save you, those who divide the heavens, who gaze at the stars, who at the new moons make **known** what shall come upon you. |
| Isa 48:6 | known | HVqp2ms | none recorded | - | 0 | “You have heard; now see all this; and will you not declare it? From this time forth I announce to you new things, hidden things that you have not **known**. |
| Isa 48:8 | known | HVqp2ms | none recorded | - | 0 | You have never heard, you have never **known**, from of old your ear has not been opened. For I knew that you would surely deal treacherously, and that from before birth you were called a rebel. |
| Isa 61:9 | known | HVNq3ms | none recorded | - | 0 | Their offspring shall be **known** among the nations, and their descendants in the midst of the peoples; all who see them shall acknowledge them, that they are an offspring the Lord has blessed. |
| Isa 64:2 | known | HVhcc | none recorded | - | 0 | as when fire kindles brushwood and the fire causes water to boil — to make your name **known** to your adversaries, and that the nations might tremble at your presence! |
| Isa 66:14 | known | HVNq3fs | none recorded | 13496 | 0 | You shall see, and your heart shall rejoice; your bones shall flourish like the grass; and the hand of the Lord shall be **known** to his servants, and he shall show his indignation against his enemies. |
| Jer 7:9 | known | HVqp2mp | none recorded | - | 0 | Will you steal, murder, commit adultery, swear falsely, make offerings to Baal, and go after other gods that you have not **known**, |
| Jer 9:16 | known | HVqp3cp | none recorded | - | 0 | I will scatter them among the nations whom neither they nor their fathers have **known**, and I will send the sword after them, until I have consumed them.” |
| Jer 11:18 | known | HVhp3ms | none recorded | - | 0 | The Lord made it **known** to me and I knew; then you showed me their deeds. |
| Jer 19:4 | known | HVqp3cp | none recorded | - | 0 | Because the people have forsaken me and have profaned this place by making offerings in it to other gods whom neither they nor their fathers nor the kings of Judah have **known**; and because they have filled this place with the blood of innocents, |
| Jer 28:9 | known | HVNi3ms | none recorded | - | 0 | As for the prophet who prophesies peace, when the word of that prophet comes to pass, then it will be **known** that the Lord has truly sent the prophet.” |
| Jer 33:3 | known | HVqp2ms | none recorded | - | 0 | Call to me and I will answer you, and will tell you great and hidden things that you have not **known**. |
| Eze 16:2 | known | HVhv2ms | none recorded | - | 0 | “ Son of man, make **known** to Jerusalem her abominations, |
| Eze 20:5 | known | HVNw1cs | none recorded | 19484 | 0 | and say to them, Thus says the Lord God: On the day when I chose Israel, I swore to the offspring of the house of Jacob, making myself **known** to them in the land of Egypt; I swore to them, saying, I am the Lord your God. |
| Eze 20:11 | known | HVhp1cs | none recorded | - | 0 | I gave them my statutes and made **known** to them my rules, by which, if a person does them, he shall live. |
| Eze 32:9 | known | HVqp2ms | none recorded | - | 0 | “I will trouble the hearts of many peoples, when I bring your destruction among the nations, into the countries that you have not **known**. |
| Eze 35:11 | known | HVNq1cs | none recorded | - | 0 | therefore, as I live, declares the Lord God, I will deal with you according to the anger and envy that you showed because of your hatred against them. And I will make myself **known** among them, when I judge you. |
| Eze 36:32 | known | HVNi3ms | none recorded | - | 0 | It is not for your sake that I will act, declares the Lord God; let that be **known** to you. Be ashamed and confounded for your ways, O house of Israel. |
| Eze 38:23 | known | HVNq1cs | none recorded | - | 0 | So I will show my greatness and my holiness and make myself **known** in the eyes of many nations. Then they will know that I am the Lord. |
| Eze 39:7 | known | HVhi1cs | none recorded | - | 0 | “And my holy name I will make **known** in the midst of my people Israel, and I will not let my holy name be profaned anymore. And the nations shall know that I am the Lord, the Holy One in Israel. |
| Eze 43:11 | known | HVhv2ms | none recorded | - | 0 | And if they are ashamed of all that they have done, make **known** to them the design of the temple, its arrangement, its exits and its entrances, that is, its whole design; and make known to them as well all its statutes and its whole design and all its laws, and write it down in their sight, so that they may observe all its laws and all its statutes and carry them out. |
| Dan 8:19 | known | HVhrmsc | none recorded | 14758 | 0 | He said, “ Behold, I will make **known** to you what shall be at the latter end of the indignation, for it refers to the appointed time of the end. |
| Hos 5:9 | known | HVhp1cs | none recorded | - | 0 | Ephraim shall become a desolation in the day of punishment; among the tribes of Israel I make **known** what is sure. |
| Hab 3:2 | known | HVhi2ms | none recorded | - | 0 | O Lord, I have heard the report of you, and your work, O Lord, do I fear. In the midst of the years revive it; in the midst of the years make it **known**; in wrath remember mercy. |
| Zec 7:14 | known | HVqp3cp | none recorded | - | 0 | “and I scattered them with a whirlwind among all the nations that they had not **known**. Thus the land they left was desolate, so that no one went to and fro, and the pleasant land was made desolate.” |
| Gen 33:13 | knows | HVqrmsa | none recorded | - | 0 | But Jacob said to him, “My lord **knows** that the children are frail, and that the nursing flocks and herds are a care to me. If they are driven hard for one day, all the flocks will die. |
| Num 24:16 | knows | HVqrmsc | none recorded | - | 0 | the oracle of him who hears the words of God, and **knows** the knowledge of the Most High, who sees the vision of the Almighty, falling down with his eyes uncovered: |
| Deu 2:7 | knows | HVqp3ms | none recorded | - | 0 | For the Lord your God has blessed you in all the work of your hands. He **knows** your going through this great wilderness. These forty years the Lord your God has been with you. You have lacked nothing.”’ |
| Deu 34:6 | knows | HVqp3ms | none recorded | - | 0 | and he buried him in the valley in the land of Moab opposite Beth-peor; but no one **knows** the place of his burial to this day. |
| Jos 22:22 | knows | HVqrmsa | none recorded | 13129, 14090, 14557, 14818 | 0 | “The Mighty One, God, the Lord! The Mighty One, God, the Lord! He **knows**; and let Israel itself know! If it was in rebellion or in breach of faith against the Lord, do not spare us today |
| 1Sa 20:3 | knows | HVqaa | none recorded | - | 0 | But David vowed again, saying, “Your father **knows** well that I have found favor in your eyes, and he thinks, ‘Do not let Jonathan know this, lest he be grieved.’ But truly, as the Lord lives and as your soul lives, there is but a step between me and death.” |
| 1Sa 23:17 | knows | HVqrmsa | none recorded | - | 0 | And he said to him, “Do not fear, for the hand of Saul my father shall not find you. You shall be king over Israel, and I shall be next to you. Saul my father also **knows** this.” |
| 2Sa 12:22 | knows | HVqrmsa | none recorded | - | 0 | He said, “While the child was still alive, I fasted and wept, for I said, ‘ Who **knows** whether the Lord will be gracious to me, that the child may live?’ |
| 2Sa 14:22 | knows | HVqp3ms | none recorded | - | 0 | And Joab fell on his face to the ground and paid homage and blessed the king. And Joab said, “ Today your servant **knows** that I have found favor in your sight, my lord the king, in that the king has granted the request of his servant.” |
| 2Sa 17:10 | knows | HVqrmsa | none recorded | - | 0 | Then even the valiant man, whose heart is like the heart of a lion, will utterly melt with fear, for all Israel **knows** that your father is a mighty man, and that those who are with him are valiant men. |
| 2Sa 19:20 | knows | HVqp3ms | none recorded | 18098 | 0 | For your servant **knows** that I have sinned. Therefore, behold, I have come this day, the first of all the house of Joseph to come down to meet my lord the king.” |
| 1Ki 5:6 | knows | HVqrmsa | none recorded | - | 0 | Now therefore command that cedars of Lebanon be cut for me. And my servants will join your servants, and I will pay you for your servants such wages as you set, for you know that there is no one among us who **knows** how to cut timber like the Sidonians.” |
| Est 4:14 | knows | HVqrmsa | none recorded | - | 0 | For if you keep silent at this time, relief and deliverance will rise for the Jews from another place, but you and your father’s house will perish. And who **knows** whether you have not come to the kingdom for such a time as this?” |
| Job 15:23 | knows | HVqp3ms | none recorded | - | 0 | He wanders abroad for bread, saying, ‘ Where is it?’ He **knows** that a day of darkness is ready at his hand; |
| Job 18:21 | knows | HVqp3ms | none recorded | - | 0 | Surely such are the dwellings of the unrighteous, such is the place of him who **knows** not God.” |
| Job 23:10 | knows | HVqp3ms | none recorded | - | 0 | But he **knows** the way that I take; when he has tried me, I shall come out as gold. |
| Job 28:7 | knows | HVqp3ms | none recorded | - | 0 | “That path no bird of prey **knows**, and the falcon’s eye has not seen it. |
| Job 28:23 | knows | HVqp3ms | none recorded | - | 0 | “ God understands the way to it, and he **knows** its place. |
| Psa 37:18 | knows | HVqrmsa | none recorded | - | 0 | The Lord **knows** the days of the blameless, and their heritage will remain forever; |
| Psa 44:21 | knows | HVqrmsa | none recorded | 15944, 17244 | 0 | would not God discover this? For he **knows** the secrets of the heart. |
| Psa 74:9 | knows | HVqrmsa | none recorded | - | 0 | We do not see our signs; there is no longer any prophet, and there is none among us who **knows** how long. |
| Psa 91:14 | knows | HVqp3ms | none recorded | - | 0 | “ Because he holds fast to me in love, I will deliver him; I will protect him, because he **knows** my name. |
| Psa 94:11 | knows | HVqrmsa | none recorded | 20455 | 0 | the Lord — **knows** the thoughts of man, that they are but a breath. |
| Psa 103:14 | knows | HVqp3ms | none recorded | 20019, 20547 | 0 | For he **knows** our frame; he remembers that we are dust. |
| Psa 104:19 | knows | HVqp3ms | none recorded | - | 0 | He made the moon to mark the seasons; the sun **knows** its time for setting. |
| Psa 138:6 | knows | HVqi3ms | none recorded | 15141, 15146, 15314, 15414 | 0 | For though the Lord is high, he regards the lowly, but the haughty he **knows** from afar. |
| Psa 139:14 | knows | HVqrfsa | none recorded | 15842, 15933, 15947, 16312, 17256, 18877, 19222, 19223, 19350 | 0 | I praise you, for I am fearfully and wonderfully made. Wonderful are your works; my soul **knows** it very well. |
| Pro 9:13 | knows | HVqp3fs | none recorded | - | 0 | The woman Folly is loud; she is seductive and **knows** nothing. |
| Pro 14:10 | knows | HVqrmsa | none recorded | 15866, 15939, 17244, 17282, 17283 | 0 | The heart **knows** its own bitterness, and no stranger shares its joy. |
| Pro 24:22 | knows | HVqrmsa | none recorded | - | 0 | for disaster will arise suddenly from them, and who **knows** the ruin that will come from them both? |
| Pro 29:7 | knows | HVqrmsa | none recorded | - | 0 | A righteous man **knows** the rights of the poor; a wicked man does not understand such knowledge. |
| Ecc 2:19 | knows | HVqrmsa | none recorded | - | 0 | and who **knows** whether he will be wise or a fool? Yet he will be master of all for which I toiled and used my wisdom under the sun. This also is vanity. |
| Ecc 3:21 | knows | HVqrmsa | none recorded | 17280, 18372 | 0 | Who **knows** whether the spirit of man goes upward and the spirit of the beast goes down into the earth? |
| Ecc 6:8 | knows | HVqrmsa | none recorded | - | 0 | For what advantage has the wise man over the fool? And what does the poor man have who **knows** how to conduct himself before the living? |
| Ecc 6:12 | knows | HVqrmsa | none recorded | 17900 | 0 | For who **knows** what is good for man while he lives the few days of his vain life, which he passes like a shadow? For who can tell man what will be after him under the sun? |
| Ecc 7:22 | knows | HVqp3ms | none recorded | 15939, 17245 | 0 | Your heart **knows** that many times you yourself have cursed others. |
| Ecc 8:1 | knows | HVqrmsa | none recorded | - | 0 | Who is like the wise? And who **knows** the interpretation of a thing? A man’s wisdom makes his face shine, and the hardness of his face is changed. |
| Ecc 10:14 | knows | HVqi3ms | none recorded | - | 0 | A fool multiplies words, though no man **knows** what is to be, and who can tell him what will be after him? |
| Isa 1:3 | knows | HVqp3ms | none recorded | 19653, 19840 | 0 | The ox **knows** its owner, and the donkey its master’s crib, but Israel does not know, my people do not understand.” |
| Isa 7:15 | knows | HVqcc | none recorded | 19471, 19492, 19608, 19651, 19679, 19739, 19788, 19839, 19840 | 0 | He shall eat curds and honey when he **knows** how to refuse the evil and choose the good. |
| Isa 29:15 | knows | HVqrmsc | none recorded | 18877, 19220 | 0 | Ah, you who hide deep from the Lord your counsel, whose deeds are in the dark, and who say, “ Who sees us? Who **knows** us?” |
| Isa 59:8 | knows | HVqp3ms | none recorded | - | 0 | The way of peace they do not know, and there is no justice in their paths; they have made their roads crooked; no one who treads on them **knows** peace. |
| Jer 8:7 | knows | HVqp3fs | none recorded | - | 0 | Even the stork in the heavens **knows** her times, and the turtledove, swallow, and crane keep the time of their coming, but my people know not the rules of the Lord. |
| Jer 9:24 | knows | HVqaa | none recorded | 15195, 15199, 15257, 15310, 17609 | 0 | but let him who boasts boast in this, that he understands and **knows** me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight, declares the Lord.” |
| Jer 29:23 | knows | HVqrmsa | none recorded | - | 0 | because they have done an outrageous thing in Israel, they have committed adultery with their neighbors ’ wives, and they have spoken in my name lying words that I did not command them. I am the one who **knows**, and I am witness, declares the Lord.’” |
| Joe 2:14 | knows | HVqrmsa | none recorded | 13151, 14765, 14840 | 0 | Who **knows** whether he will not turn and relent, and leave a blessing behind him, a grain offering and a drink offering for the Lord your God? |
| Nah 1:7 | knows | HVqrmsa | none recorded | 14642 | 0 | The Lord is good, a stronghold in the day of trouble; he **knows** those who take refuge in him. |
| Nah 3:17 | knows | HVNp3ms | none recorded | - | 0 | Your princes are like grasshoppers, your scribes like clouds of locusts settling on the fences in a day of cold — when the sun rises, they fly away; no one **knows** where they are. |
| Zep 3:5 | knows | HVqrmsa | none recorded | - | 0 | The Lord within her is righteous; he does no injustice; every morning he shows forth his justice; each dawn he does not fail; but the unjust **knows** no shame. |
| Gen 24:21 | learn | HVqcc | none recorded | - | 0 | The man gazed at her in silence to **learn** whether the Lord had prospered his journey or not. |
| Rut 3:18 | learn | HVqi2fs | none recorded | - | 0 | She replied, “ Wait, my daughter, until you **learn** how the matter turns out, for the man will not rest but will settle the matter today.” |
| Est 2:11 | learn | HVqcc | none recorded | - | 0 | And every day Mordecai walked in front of the court of the harem to **learn** how Esther was and what was happening to her. |
| Est 4:5 | learn | HVqcc | none recorded | - | 0 | Then Esther called for Hathach, one of the king’s eunuchs, who had been appointed to attend her, and ordered him to go to Mordecai to **learn** what this was and why it was. |
| 1Sa 4:6 | learned | HVqw3mp | none recorded | - | 0 | And when the Philistines heard the noise of the shouting, they said, “What does this great shouting in the camp of the Hebrews mean?” And when they **learned** that the ark of the Lord had come to the camp, |
| 1Sa 26:4 | learned | HVqw3ms | none recorded | - | 0 | David sent out spies and **learned** that Saul had indeed come. |
| Est 4:1 | learned | HVqp3ms | none recorded | - | 0 | When Mordecai **learned** all that had been done, Mordecai tore his clothes and put on sackcloth and ashes, and went out into the midst of the city, and he cried out with a loud and bitter cry. |
| Neh 6:16 | perceived | HVqw3mp | none recorded | - | 0 | And when all our enemies heard of it, all the nations around us were afraid and fell greatly in their own esteem, for they **perceived** that this work had been accomplished with the help of our God. |
| Ecc 1:17 | perceived | HVqp1cs | none recorded | - | 0 | And I applied my heart to know wisdom and to know madness and folly. I **perceived** that this also is but a striving after wind. |
| Ecc 2:14 | perceived | HVqq1cs | none recorded | - | 0 | The wise person has his eyes in his head, but the fool walks in darkness. And yet I **perceived** that the same event happens to all of them. |
| Ecc 3:12 | perceived | HVqp1cs | none recorded | - | 0 | I **perceived** that there is nothing better for them than to be joyful and to do good as long as they live; |
| Ecc 3:14 | perceived | HVqp1cs | none recorded | - | 0 | I **perceived** that whatever God does endures forever; nothing can be added to it, nor anything taken from it. God has done it, so that people fear before him. |

### 3.2 G6063 οἶδα oida "to know": 229 own occurrences in 227 verses

- **Meaning as stored:** Greek; native word οἶδα, transliteration oida; STEP gloss "to know"; sense head "to know" (the code is its own lemma).
- **Related terms (4):** G1492H eidō "to perceive: see"; G1492I eidō "to perceive: know"; G2467 isēmi "to know"; G6063 oida "to know".
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 286; verses STEP attests 245; verse_lexical rows the parse found 247.

- **Carried by the member words:** know (174), knowing (29), knows (16), aware (2), knew (2), knowledge (2), comprehends (1), fully knew (1), know how (1), realizing (1).
- **Engagement of these occurrences:** none recorded 229.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Th 5:2 | aware | V-RAI-2P | none recorded | - | 0 | For you yourselves are fully **aware** that the day of the Lord will come like a thief in the night. |
| 2Ti 1:15 | aware | V-RAI-2S | none recorded | - | 0 | You are **aware** that all who are in Asia turned away from me, among whom are Phygelus and Hermogenes. |
| 1Cor 2:11 | comprehends | V-RAI-3S | none recorded | - | 0 | For who knows a person’s thoughts except the spirit of that person, which is in him? So also no one **comprehends** the thoughts of God except the Spirit of God. |
| Jude 5 | fully knew | V-RAP-APM | none recorded | - | 0 | Now I want to remind you, although you once **fully knew** it, that Jesus, who saved a people out of the land of Egypt, afterward destroyed those who did not believe. |
| Joh 13:1 | knew | V-RAP-NSM | none recorded | - | 0 | Now before the Feast of the Passover, when Jesus **knew** that his hour had come to depart out of this world to the Father, having loved his own who were in the world, he loved them to the end. |
| Joh 21:12 | knew | V-RAP-NPM | none recorded | - | 0 | Jesus said to them, “ Come and have breakfast.” Now none of the disciples dared ask him, “ Who are you?” They **knew** it was the Lord. |
| Mat 7:11 | know | V-RAI-2P | none recorded | - | 0 | If you then, who are evil, **know** how to give good gifts to your children, how much more will your Father who is in heaven give good things to those who ask him! |
| Mat 9:6 | know | V-RAS-2P | none recorded | - | 0 | But that you may **know** that the Son of Man has authority on earth to forgive sins ” —he then said to the paralytic — “ Rise, pick up your bed and go home.” |
| Mat 15:12 | know | V-RAI-2S | none recorded | - | 0 | Then the disciples came and said to him, “Do you **know** that the Pharisees were offended when they heard this saying?” |
| Mat 20:22 | know | V-RAI-2P | none recorded | - | 0 | Jesus answered, “You do not **know** what you are asking. Are you able to drink the cup that I am to drink?” They said to him, “We are able.” |
| Mat 20:25 | know | V-RAI-2P | none recorded | 14276, 19009 | 0 | But Jesus called them to him and said, “You **know** that the rulers of the Gentiles lord it over them, and their great ones exercise authority over them. |
| Mat 21:27 | know | V-RAI-1P | none recorded | - | 0 | So they answered Jesus, “We do not **know**.” And he said to them, “ Neither will I tell you by what authority I do these things. |
| Mat 22:16 | know | V-RAI-1P | none recorded | - | 0 | And they sent their disciples to him, along with the Herodians, saying, “ Teacher, we **know** that you are true and teach the way of God truthfully, and you do not care about anyone’s opinion, for you are not swayed by appearances. |
| Mat 22:29 | know | V-RAP-NPM | none recorded | - | 0 | But Jesus answered them, “You are wrong, because you **know** neither the Scriptures nor the power of God. |
| Mat 24:42 | know | V-RAI-2P | none recorded | - | 0 | Therefore, stay awake, for you do not **know** on what day your Lord is coming. |
| Mat 25:12 | know | V-RAI-1S | none recorded | - | 0 | But he answered, ‘ Truly, I say to you, I do not **know** you.’ |
| Mat 25:13 | know | V-RAI-2P | none recorded | - | 0 | Watch therefore, for you **know** neither the day nor the hour. |
| Mat 26:2 | know | V-RAI-2P | none recorded | - | 0 | “You **know** that after two days the Passover is coming, and the Son of Man will be delivered up to be crucified.” |
| Mat 26:70 | know | V-RAI-1S | none recorded | - | 0 | But he denied it before them all, saying, “I do not **know** what you mean.” |
| Mat 26:72 | know | V-RAI-1S | none recorded | - | 0 | And again he denied it with an oath: “I do not **know** the man.” |
| Mat 26:74 | know | V-RAI-1S | none recorded | - | 0 | Then he began to invoke a curse on himself and to swear, “I do not **know** the man.” And immediately the rooster crowed. |
| Mat 28:5 | know | V-RAI-1S | none recorded | - | 0 | But the angel said to the women, “Do not be afraid, for I **know** that you seek Jesus who was crucified. |
| Mar 1:24 | know | V-RAI-1S | none recorded | - | 0 | “ What have you to do with us, Jesus of Nazareth? Have you come to destroy us? I **know** who you are — the Holy One of God.” |
| Mar 2:10 | know | V-RAS-2P | none recorded | - | 0 | But that you may **know** that the Son of Man has authority on earth to forgive sins ” —he said to the paralytic — |
| Mar 10:19 | know | V-RAI-2S | none recorded | - | 0 | You **know** the commandments: ‘Do not murder, Do not commit adultery, Do not steal, Do not bear false witness, Do not defraud, Honor your father and mother.’” |
| Mar 10:38 | know | V-RAI-2P | none recorded | - | 0 | Jesus said to them, “You do not **know** what you are asking. Are you able to drink the cup that I drink, or to be baptized with the baptism with which I am baptized?” |
| Mar 10:42 | know | V-RAI-2P | none recorded | 14276 | 0 | And Jesus called them to him and said to them, “You **know** that those who are considered rulers of the Gentiles lord it over them, and their great ones exercise authority over them. |
| Mar 11:33 | know | V-RAI-1P | none recorded | - | 0 | So they answered Jesus, “We do not **know**.” And Jesus said to them, “ Neither will I tell you by what authority I do these things.” |
| Mar 12:14 | know | V-RAI-1P | none recorded | - | 0 | And they came and said to him, “ Teacher, we **know** that you are true and do not care about anyone’s opinion. For you are not swayed by appearances, but truly teach the way of God. Is it lawful to pay taxes to Caesar, or not? Should we pay them, or should we not?” |
| Mar 12:24 | know | V-RAP-NPM | none recorded | - | 0 | Jesus said to them, “Is this not the reason you are wrong, because you **know** neither the Scriptures nor the power of God? |
| Mar 13:33 | know | V-RAI-2P | none recorded | - | 0 | Be on guard, keep awake. For you do not **know** when the time will come. |
| Mar 13:35 | know | V-RAI-2P | none recorded | - | 0 | Therefore stay awake — for you do not **know** when the master of the house will come, in the evening, or at midnight, or when the rooster crows, or in the morning — |
| Mar 14:68 | know | V-RAI-1S | none recorded | - | 0 | But he denied it, saying, “I neither **know** nor understand what you mean.” And he went out into the gateway and the rooster crowed. |
| Mar 14:71 | know | V-RAI-1S | none recorded | - | 0 | But he began to invoke a curse on himself and to swear, “I do not **know** this man of whom you speak.” |
| Luk 4:34 | know | V-RAI-1S | none recorded | - | 0 | “ Ha! What have you to do with us, Jesus of Nazareth? Have you come to destroy us? I **know** who you are — the Holy One of God.” |
| Luk 5:24 | know | V-RAS-2P | none recorded | - | 0 | But that you may **know** that the Son of Man has authority on earth to forgive sins ” —he said to the man who was paralyzed — “I say to you, rise, pick up your bed and go home.” |
| Luk 11:13 | know | V-RAI-2P | none recorded | 16550 | 0 | If you then, who are evil, **know** how to give good gifts to your children, how much more will the heavenly Father give the Holy Spirit to those who ask him!” |
| Luk 13:25 | know | V-RAI-1S | none recorded | - | 0 | When once the master of the house has risen and shut the door, and you begin to stand outside and to knock at the door, saying, ‘ Lord, open to us,’ then he will answer you, ‘I do not **know** where you come from.’ |
| Luk 13:27 | know | V-RAI-1S | none recorded | - | 0 | But he will say, ‘I tell you, I do not **know** where you come from. Depart from me, all you workers of evil!’ |
| Luk 18:20 | know | V-RAI-2S | none recorded | - | 0 | You **know** the commandments: ‘Do not commit adultery, Do not murder, Do not steal, Do not bear false witness, Honor your father and mother.’” |
| Luk 20:7 | know | V-RAN | none recorded | - | 0 | So they answered that they did not **know** where it came from. |
| Luk 20:21 | know | V-RAI-1P | none recorded | - | 0 | So they asked him, “ Teacher, we **know** that you speak and teach rightly, and show no partiality, but truly teach the way of God. |
| Luk 22:34 | know | V-RAN | none recorded | 18518 | 0 | Jesus said, “I tell you, Peter, the rooster will not crow this day, until you deny three times that you **know** me.” |
| Luk 22:57 | know | V-RAI-1S | none recorded | - | 0 | But he denied it, saying, “ Woman, I do not **know** him.” |
| Luk 22:60 | know | V-RAI-1S | none recorded | - | 0 | But Peter said, “ Man, I do not **know** what you are talking about.” And immediately, while he was still speaking, the rooster crowed. |
| Luk 23:34 | know | V-RAI-3P | none recorded | 15225 | 0 | And Jesus said, “ Father, forgive them, for they **know** not what they do.” And they cast lots to divide his garments. |
| Joh 1:26 | know | V-RAI-2P | none recorded | - | 0 | John answered them, “ I baptize with water, but among you stands one you do not **know**, |
| Joh 3:2 | know | V-RAI-1P | none recorded | - | 0 | This man came to Jesus by night and said to him, “ Rabbi, we **know** that you are a teacher come from God, for no one can do these signs that you do unless God is with him.” |
| Joh 3:8 | know | V-RAI-2S | none recorded | - | 0 | The wind blows where it wishes, and you hear its sound, but you do not **know** where it comes from or where it goes. So it is with everyone who is born of the Spirit.” |
| Joh 3:11 | know | V-RAI-1P | none recorded | - | 0 | Truly, truly, I say to you, we speak of what we **know**, and bear witness to what we have seen, but you do not receive our testimony. |
| Joh 4:25 | know | V-RAI-1S | none recorded | - | 0 | The woman said to him, “I **know** that Messiah is coming (he who is called Christ ). When he comes, he will tell us all things.” |
| Joh 4:32 | know | V-RAI-2P | none recorded | - | 0 | But he said to them, “ I have food to eat that you do not **know** about.” |
| Joh 4:42 | know | V-RAI-1P | none recorded | - | 0 | They said to the woman, “It is no longer because of what you said that we believe, for we have heard for ourselves, and we **know** that this is indeed the Savior of the world.” |
| Joh 5:32 | know | V-RAI-1S | none recorded | - | 0 | There is another who bears witness about me, and I **know** that the testimony that he bears about me is true. |
| Joh 6:42 | know | V-RAI-1P | none recorded | - | 0 | They said, “ Is not this Jesus, the son of Joseph, whose father and mother we **know**? How does he now say, ‘I have come down from heaven ’?” |
| Joh 7:27 | know | V-RAI-1P | none recorded | - | 0 | But we **know** where this man comes from, and when the Christ appears, no one will know where he comes from.” |
| Joh 7:29 | know | V-RAI-1S | none recorded | - | 0 | I **know** him, for I come from him, and he sent me.” |
| Joh 8:19 | know | V-RAI-2P | none recorded | - | 0 | They said to him therefore, “ Where is your Father?” Jesus answered, “You **know** neither me nor my Father. If you knew me, you would know my Father also.” |
| Joh 8:37 | know | V-RAI-1S | none recorded | - | 0 | I **know** that you are offspring of Abraham; yet you seek to kill me because my word finds no place in you. |
| Joh 9:12 | know | V-RAI-1S | none recorded | - | 0 | They said to him, “ Where is he?” He said, “I do not **know**.” |
| Joh 9:20 | know | V-RAI-1P | none recorded | - | 0 | His parents answered, “We **know** that this is our son and that he was born blind. |
| Joh 9:24 | know | V-RAI-1P | none recorded | - | 0 | So for the second time they called the man who had been blind and said to him, “ Give glory to God. We **know** that this man is a sinner.” |
| Joh 9:30 | know | V-RAI-2P | none recorded | - | 0 | The man answered, “ Why, this is an amazing thing! You do not **know** where he comes from, and yet he opened my eyes. |
| Joh 9:31 | know | V-RAI-1P | none recorded | 17682 | 0 | We **know** that God does not listen to sinners, but if anyone is a worshiper of God and does his will, God listens to him. |
| Joh 10:4 | know | V-RAI-3P | none recorded | - | 0 | When he has brought out all his own, he goes before them, and the sheep follow him, for they **know** his voice. |
| Joh 10:5 | know | V-RAI-3P | none recorded | - | 0 | A stranger they will not follow, but they will flee from him, for they do not **know** the voice of strangers.” |
| Joh 11:22 | know | V-RAI-1S | none recorded | - | 0 | But even now I **know** that whatever you ask from God, God will give you.” |
| Joh 11:24 | know | V-RAI-1S | none recorded | 18653 | 0 | Martha said to him, “I **know** that he will rise again in the resurrection on the last day.” |
| Joh 11:49 | know | V-RAI-2P | none recorded | - | 0 | But one of them, Caiaphas, who was high priest that year, said to them, “ You **know** nothing at all. |
| Joh 12:35 | know | V-RAI-3S | none recorded | - | 0 | So Jesus said to them, “The light is among you for a little while longer. Walk while you have the light, lest darkness overtake you. The one who walks in the darkness does not **know** where he is going. |
| Joh 12:50 | know | V-RAI-1S | none recorded | - | 0 | And I **know** that his commandment is eternal life. What I say, therefore, I say as the Father has told me.” |
| Joh 13:17 | know | V-RAI-2P | none recorded | - | 0 | If you **know** these things, blessed are you if you do them. |
| Joh 13:18 | know | V-RAI-1S | none recorded | 19479, 19732 | 0 | I am not speaking of all of you; I **know** whom I have chosen. But the Scripture will be fulfilled, ‘He who ate my bread has lifted his heel against me.’ |
| Joh 14:5 | know | V-PAI-1P | none recorded | - | 0 | Thomas said to him, “ Lord, we do not **know** where you are going. How can we know the way?” |
| Joh 14:5 | know | V-PAN | none recorded | - | 0 | Thomas said to him, “ Lord, we do not **know** where you are going. How can we know the way?” |
| Joh 15:15 | know | V-RAI-3S | none recorded | - | 0 | No longer do I call you servants, for the servant does not **know** what his master is doing; but I have called you friends, for all that I have heard from my Father I have made known to you. |
| Joh 15:21 | know | V-RAI-3P | none recorded | 19945, 20297 | 0 | But all these things they will do to you on account of my name, because they do not **know** him who sent me. |
| Joh 16:18 | know | V-RAI-1P | none recorded | - | 0 | So they were saying, “ What does he mean by ‘a little while ’? We do not **know** what he is talking about.” |
| Joh 18:21 | know | V-RAI-3P | none recorded | - | 0 | Why do you ask me? Ask those who have heard me what I said to them; they **know** what I said.” |
| Joh 19:10 | know | V-RAI-2S | none recorded | - | 0 | So Pilate said to him, “You will not speak to me? Do you not **know** that I have authority to release you and authority to crucify you?” |
| Joh 20:2 | know | V-RAI-1P | none recorded | - | 0 | So she ran and went to Simon Peter and the other disciple, the one whom Jesus loved, and said to them, “They have taken the Lord out of the tomb, and we do not **know** where they have laid him.” |
| Joh 20:13 | know | V-RAI-1S | none recorded | - | 0 | They said to her, “ Woman, why are you weeping?” She said to them, “They have taken away my Lord, and I do not **know** where they have laid him.” |
| Joh 21:15 | know | V-RAI-2S | none recorded | - | 0 | When they had finished breakfast, Jesus said to Simon Peter, “ Simon, son of John, do you love me more than these?” He said to him, “ Yes, Lord; you **know** that I love you.” He said to him, “ Feed my lambs.” |
| Joh 21:16 | know | V-RAI-2S | none recorded | - | 0 | He said to him a second time, “ Simon, son of John, do you love me?” He said to him, “ Yes, Lord; you **know** that I love you.” He said to him, “ Tend my sheep.” |
| Joh 21:17 | know | V-RAI-2S | none recorded | - | 0 | He said to him the third time, “ Simon, son of John, do you love me?” Peter was grieved because he said to him the third time, “Do you love me?” and he said to him, “ Lord, you **know** everything; you know that I love you.” Jesus said to him, “ Feed my sheep. |
| Joh 21:24 | know | V-RAI-1P | none recorded | - | 0 | This is the disciple who is bearing witness about these things, and who has written these things, and we **know** that his testimony is true. |
| Act 2:22 | know | V-RAI-2P | none recorded | - | 0 | “ Men of Israel, hear these words: Jesus of Nazareth, a man attested to you by God with mighty works and wonders and signs that God did through him in your midst, as you yourselves **know** — |
| Act 3:16 | know | V-RAI-2P | none recorded | - | 0 | And his name — by faith in his name —has made this man strong whom you see and **know**, and the faith that is through Jesus has given the man this perfect health in the presence of you all. |
| Act 3:17 | know | V-RAI-1S | none recorded | - | 0 | “ And now, brothers, I **know** that you acted in ignorance, as did also your rulers. |
| Act 7:40 | know | V-RAI-1P | none recorded | - | 0 | saying to Aaron, ‘ Make for us gods who will go before us. As for this Moses who led us out from the land of Egypt, we do not **know** what has become of him.’ |
| Act 10:37 | know | V-RAI-2P | none recorded | - | 0 | you yourselves **know** what happened throughout all Judea, beginning from Galilee after the baptism that John proclaimed: |
| Act 20:25 | know | V-RAI-1S | none recorded | - | 0 | And now, behold, I **know** that none of you among whom I have gone about proclaiming the kingdom will see my face again. |
| Act 20:29 | know | V-RAI-1S | none recorded | - | 0 | I **know** that after my departure fierce wolves will come in among you, not sparing the flock; |
| Act 26:27 | know | V-RAI-1S | none recorded | - | 0 | King Agrippa, do you believe the prophets? I **know** that you believe.” |
| Rom 2:2 | know | V-RAI-1P | none recorded | - | 0 | We **know** that the judgment of God rightly falls on those who practice such things. |
| Rom 3:19 | know | V-RAI-1P | none recorded | - | 0 | Now we **know** that whatever the law says it speaks to those who are under the law, so that every mouth may be stopped, and the whole world may be held accountable to God. |
| Rom 6:9 | know | V-RAP-NPM | none recorded | - | 0 | We **know** that Christ, being raised from the dead, will never die again; death no longer has dominion over him. |
| Rom 6:16 | know | V-RAI-2P | none recorded | - | 0 | Do you not **know** that if you present yourselves to anyone as obedient slaves, you are slaves of the one whom you obey, either of sin, which leads to death, or of obedience, which leads to righteousness? |
| Rom 7:14 | know | V-RAI-1P | none recorded | - | 0 | For we **know** that the law is spiritual, but I am of the flesh, sold under sin. |
| Rom 7:18 | know | V-RAI-1S | none recorded | - | 0 | For I **know** that nothing good dwells in me, that is, in my flesh. For I have the desire to do what is right, but not the ability to carry it out. |
| Rom 8:22 | know | V-RAI-1P | none recorded | - | 0 | For we **know** that the whole creation has been groaning together in the pains of childbirth until now. |
| Rom 8:26 | know | V-RAI-1P | none recorded | 15957, 19418, 19421, 20399, 20424 | 0 | Likewise the Spirit helps us in our weakness. For we do not **know** what to pray for as we ought, but the Spirit himself intercedes for us with groanings too deep for words. |
| Rom 8:28 | know | V-RAI-1P | none recorded | 19418 | 0 | And we **know** that for those who love God all things work together for good, for those who are called according to his purpose. |
| Rom 11:2 | know | V-RAI-2P | none recorded | - | 0 | God has not rejected his people whom he foreknew. Do you not **know** what the Scripture says of Elijah, how he appeals to God against Israel? |
| Rom 13:11 | know | V-RAP-NPM | none recorded | - | 0 | Besides this you **know** the time, that the hour has come for you to wake from sleep. For salvation is nearer to us now than when we first believed. |
| Rom 14:14 | know | V-RAI-1S | none recorded | - | 0 | I **know** and am persuaded in the Lord Jesus that nothing is unclean in itself, but it is unclean for anyone who thinks it unclean. |
| Rom 15:29 | know | V-RAI-1S | none recorded | - | 0 | I **know** that when I come to you I will come in the fullness of the blessing of Christ. |
| 1Cor 1:16 | know | V-RAI-1S | none recorded | - | 0 | (I did baptize also the household of Stephanas. Beyond that, I do not **know** whether I baptized anyone else.) |
| 1Cor 2:2 | know | V-RAN | none recorded | - | 0 | For I decided to **know** nothing among you except Jesus Christ and him crucified. |
| 1Cor 3:16 | know | V-RAI-2P | none recorded | - | 0 | Do you not **know** that you are God’s temple and that God’s Spirit dwells in you? |
| 1Cor 6:2 | know | V-RAI-2P | none recorded | - | 0 | Or do you not **know** that the saints will judge the world? And if the world is to be judged by you, are you incompetent to try trivial cases? |
| 1Cor 6:3 | know | V-RAI-2P | none recorded | - | 0 | Do you not **know** that we are to judge angels? How much more, then, matters pertaining to this life! |
| 1Cor 6:9 | know | V-RAI-2P | none recorded | - | 0 | Or do you not **know** that the unrighteous will not inherit the kingdom of God? Do not be deceived: neither the sexually immoral, nor idolaters, nor adulterers, nor men who practice homosexuality, |
| 1Cor 8:1 | know | V-RAI-1P | none recorded | 15151 | 0 | Now concerning food offered to idols: we **know** that “ all of us possess knowledge.” This “ knowledge ” puffs up, but love builds up. |
| 1Cor 8:4 | know | V-RAI-1P | none recorded | - | 0 | Therefore, as to the eating of food offered to idols, we **know** that “an idol has no real existence,” and that “there is no God but one.” |
| 1Cor 9:13 | know | V-RAI-2P | none recorded | - | 0 | Do you not **know** that those who are employed in the temple service get their food from the temple, and those who serve at the altar share in the sacrificial offerings? |
| 1Cor 9:24 | know | V-RAI-2P | none recorded | - | 0 | Do you not **know** that in a race all the runners run, but only one receives the prize? So run that you may obtain it. |
| 1Cor 12:2 | know | V-RAI-2P | none recorded | - | 0 | You **know** that when you were pagans you were led astray to mute idols, however you were led. |
| 1Cor 14:11 | know | V-RAS-1S | none recorded | - | 0 | but if I do not **know** the meaning of the language, I will be a foreigner to the speaker and the speaker a foreigner to me. |
| 1Cor 14:16 | know | V-RAI-3S | none recorded | - | 0 | Otherwise, if you give thanks with your spirit, how can anyone in the position of an outsider say “ Amen ” to your thanksgiving when he does not **know** what you are saying? |
| 1Cor 16:15 | know | V-RAI-2P | none recorded | - | 0 | Now I urge you, brothers —you **know** that the household of Stephanas were the first converts in Achaia, and that they have devoted themselves to the service of the saints — |
| 2Cor 1:7 | know | V-RAP-NPM | none recorded | - | 0 | Our hope for you is unshaken, for we **know** that as you share in our sufferings, you will also share in our comfort. |
| 2Cor 5:1 | know | V-RAI-1P | none recorded | - | 0 | For we **know** that if the tent that is our earthly home is destroyed, we have a building from God, a house not made with hands, eternal in the heavens. |
| 2Cor 5:6 | know | V-RAP-NPM | none recorded | 18377 | 0 | So we are always of good courage. We **know** that while we are at home in the body we are away from the Lord, |
| 2Cor 9:2 | know | V-RAI-1S | none recorded | 17867 | 0 | for I **know** your readiness, of which I boast about you to the people of Macedonia, saying that Achaia has been ready since last year. And your zeal has stirred up most of them. |
| Gal 2:16 | know | V-RAP-NPM | none recorded | - | 0 | yet we **know** that a person is not justified by works of the law but through faith in Jesus Christ, so we also have believed in Christ Jesus, in order to be justified by faith in Christ and not by works of the law, because by works of the law no one will be justified. |
| Gal 4:8 | know | V-RAP-NPM | none recorded | - | 0 | Formerly, when you did not **know** God, you were enslaved to those that by nature are not gods. |
| Gal 4:13 | know | V-RAI-2P | none recorded | - | 0 | You **know** it was because of a bodily ailment that I preached the gospel to you at first, |
| Eph 1:18 | know | V-RAN | none recorded | 15941, 16786, 17102, 19506, 20240 | 0 | having the eyes of your hearts enlightened, that you may **know** what is the hope to which he has called you, what are the riches of his glorious inheritance in the saints, |
| Eph 6:21 | know | V-RAS-2P | none recorded | - | 0 | So that you also may **know** how I am and what I am doing, Tychicus the beloved brother and faithful minister in the Lord will tell you everything. |
| Phili 1:19 | know | V-RAI-1S | none recorded | - | 0 | for I **know** that through your prayers and the help of the Spirit of Jesus Christ this will turn out for my deliverance, |
| Phili 1:25 | know | V-RAI-1S | none recorded | 19923 | 0 | Convinced of this, I **know** that I will remain and continue with you all, for your progress and joy in the faith, |
| Phili 4:15 | know | V-RAI-2P | none recorded | - | 0 | And you Philippians yourselves **know** that in the beginning of the gospel, when I left Macedonia, no church entered into partnership with me in giving and receiving, except you only. |
| Col 2:1 | know | V-RAN | none recorded | - | 0 | For I want you to **know** how great a struggle I have for you and for those at Laodicea and for all who have not seen me face to face, |
| Col 4:6 | know | V-RAN | none recorded | - | 0 | Let your speech always be gracious, seasoned with salt, so that you may **know** how you ought to answer each person. |
| 1Th 1:4 | know | V-RAP-NPM | none recorded | 19954, 20294 | 0 | For we **know**, brothers loved by God, that he has chosen you, |
| 1Th 1:5 | know | V-RAI-2P | none recorded | 19954, 20294 | 0 | because our gospel came to you not only in word, but also in power and in the Holy Spirit and with full conviction. You **know** what kind of men we proved to be among you for your sake. |
| 1Th 2:1 | know | V-RAI-2P | none recorded | - | 0 | For you yourselves **know**, brothers, that our coming to you was not in vain. |
| 1Th 2:2 | know | V-RAI-2P | none recorded | - | 0 | But though we had already suffered and been shamefully treated at Philippi, as you **know**, we had boldness in our God to declare to you the gospel of God in the midst of much conflict. |
| 1Th 2:5 | know | V-RAI-2P | none recorded | - | 0 | For we never came with words of flattery, as you **know**, nor with a pretext for greed — God is witness. |
| 1Th 2:11 | know | V-RAI-2P | none recorded | - | 0 | For you **know** how, like a father with his children, |
| 1Th 3:3 | know | V-RAI-2P | none recorded | - | 0 | that no one be moved by these afflictions. For you yourselves **know** that we are destined for this. |
| 1Th 3:4 | know | V-RAI-2P | none recorded | - | 0 | For when we were with you, we kept telling you beforehand that we were to suffer affliction, just as it has come to pass, and just as you **know**. |
| 1Th 4:2 | know | V-RAI-2P | none recorded | - | 0 | For you **know** what instructions we gave you through the Lord Jesus. |
| 1Th 4:4 | know | V-RAN | none recorded | - | 0 | that each one of you **know** how to control his own body in holiness and honor, |
| 1Th 4:5 | know | V-RAP-NPN | none recorded | 17423 | 0 | not in the passion of lust like the Gentiles who do not **know** God; |
| 2Th 1:8 | know | V-RAP-DPM | none recorded | - | 0 | in flaming fire, inflicting vengeance on those who do not **know** God and on those who do not obey the gospel of our Lord Jesus. |
| 2Th 2:6 | know | V-RAI-2P | none recorded | - | 0 | And you **know** what is restraining him now so that he may be revealed in his time. |
| 2Th 3:7 | know | V-RAI-2P | none recorded | - | 32 | For you yourselves **know** how you ought to imitate us, because we were not idle when we were with you, |
| 1Ti 1:8 | know | V-RAI-1P | none recorded | - | 0 | Now we **know** that the law is good, if one uses it lawfully, |
| 1Ti 3:15 | know | V-RAS-2S | none recorded | - | 0 | if I delay, you may **know** how one ought to behave in the household of God, which is the church of the living God, a pillar and buttress of the truth. |
| 2Ti 1:12 | know | V-RAI-1S | none recorded | - | 0 | which is why I suffer as I do. But I am not ashamed, for I **know** whom I have believed, and I am convinced that he is able to guard until that day what has been entrusted to me. |
| 2Ti 2:23 | know | V-RAP-NSM | none recorded | - | 0 | Have nothing to do with foolish, ignorant controversies; you **know** that they breed quarrels. |
| Tit 1:16 | know | V-RAN | none recorded | 19506, 20238 | 0 | They profess to **know** God, but they deny him by their works. They are detestable, disobedient, unfit for any good work. |
| Heb 10:30 | know | V-RAI-1P | none recorded | - | 0 | For we **know** him who said, “ Vengeance is mine; I will repay.” And again, “The Lord will judge his people.” |
| Heb 12:17 | know | V-RAI-2P | none recorded | - | 0 | For you **know** that afterward, when he desired to inherit the blessing, he was rejected, for he found no chance to repent, though he sought it with tears. |
| Jam 1:19 | know | V-RAM-2P | none recorded | - | 0 | **Know** this, my beloved brothers: let every person be quick to hear, slow to speak, slow to anger; |
| Jam 3:1 | know | V-RAP-NPM | none recorded | - | 0 | Not many of you should become teachers, my brothers, for you **know** that we who teach will be judged with greater strictness. |
| Jam 4:4 | know | V-RAI-2P | none recorded | 18120 | 0 | You adulterous people! Do you not **know** that friendship with the world is enmity with God? Therefore whoever wishes to be a friend of the world makes himself an enemy of God. |
| 2Pe 1:12 | know | V-RAP-APM | none recorded | - | 0 | Therefore I intend always to remind you of these qualities, though you **know** them and are established in the truth that you have. |
| 2Pe 1:14 | know | V-RAP-NSM | none recorded | - | 0 | since I **know** that the putting off of my body will be soon, as our Lord Jesus Christ made clear to me. |
| 1Jo 2:11 | know | V-RAI-3S | none recorded | - | 0 | But whoever hates his brother is in the darkness and walks in the darkness, and does not **know** where he is going, because the darkness has blinded his eyes. |
| 1Jo 2:29 | know | V-RAS-2P | none recorded | - | 0 | If you **know** that he is righteous, you may be sure that everyone who practices righteousness has been born of him. |
| 1Jo 3:2 | know | V-RAI-1P | none recorded | 18390 | 0 | Beloved, we are God’s children now, and what we will be has not yet appeared; but we **know** that when he appears we shall be like him, because we shall see him as he is. |
| 1Jo 3:5 | know | V-RAI-2P | none recorded | - | 0 | You **know** that he appeared in order to take away sins, and in him there is no sin. |
| 1Jo 3:14 | know | V-RAI-1P | none recorded | - | 0 | We **know** that we have passed out of death into life, because we love the brothers. Whoever does not love abides in death. |
| 1Jo 3:15 | know | V-RAI-2P | none recorded | - | 0 | Everyone who hates his brother is a murderer, and you **know** that no murderer has eternal life abiding in him. |
| 1Jo 5:13 | know | V-RAS-2P | none recorded | - | 0 | I write these things to you who believe in the name of the Son of God, that you may **know** that you have eternal life. |
| 1Jo 5:18 | know | V-RAI-1P | none recorded | - | 0 | We **know** that everyone who has been born of God does not keep on sinning, but he who was born of God protects him, and the evil one does not touch him. |
| 1Jo 5:19 | know | V-RAI-1P | none recorded | - | 0 | We **know** that we are from God, and the whole world lies in the power of the evil one. |
| 1Jo 5:20 | know | V-RAI-1P | none recorded | - | 0 | And we **know** that the Son of God has come and has given us understanding, so that we may know him who is true; and we are in him who is true, in his Son Jesus Christ. He is the true God and eternal life. |
| 3Jo 12 | know | V-RAI-2S | none recorded | - | 0 | Demetrius has received a good testimony from everyone, and from the truth itself. We also add our testimony, and you **know** that our testimony is true. |
| Rev 2:2 | know | V-RAI-1S | none recorded | - | 0 | “‘I **know** your works, your toil and your patient endurance, and how you cannot bear with those who are evil, but have tested those who call themselves apostles and are not, and found them to be false. |
| Rev 2:9 | know | V-RAI-1S | none recorded | - | 0 | “‘I **know** your tribulation and your poverty ( but you are rich ) and the slander of those who say that they are Jews and are not, but are a synagogue of Satan. |
| Rev 2:13 | know | V-RAI-1S | none recorded | - | 0 | “‘I **know** where you dwell, where Satan’s throne is. Yet you hold fast my name, and you did not deny my faith even in the days of Antipas my faithful witness, who was killed among you, where Satan dwells. |
| Rev 2:19 | know | V-RAI-1S | none recorded | - | 0 | “‘I **know** your works, your love and faith and service and patient endurance, and that your latter works exceed the first. |
| Rev 3:1 | know | V-RAI-1S | none recorded | - | 0 | “ And to the angel of the church in Sardis write: ‘ The words of him who has the seven spirits of God and the seven stars. “‘I **know** your works. You have the reputation of being alive, but you are dead. |
| Rev 3:8 | know | V-RAI-1S | none recorded | - | 0 | “‘I **know** your works. Behold, I have set before you an open door, which no one is able to shut. I know that you have but little power, and yet you have kept my word and have not denied my name. |
| Rev 3:15 | know | V-RAI-1S | none recorded | - | 0 | “‘I **know** your works: you are neither cold nor hot. Would that you were either cold or hot! |
| Rev 7:14 | know | V-RAI-2S | none recorded | - | 0 | I said to him, “ Sir, you **know**.” And he said to me, “ These are the ones coming out of the great tribulation. They have washed their robes and made them white in the blood of the Lamb. |
| 1Ti 3:5 | know how | V-RAI-3S | none recorded | - | 0 | for if someone does not **know how** to manage his own household, how will he care for God’s church? |
| Mar 5:33 | knowing | V-RAP-NSF | none recorded | - | 0 | But the woman, **knowing** what had happened to her, came in fear and trembling and fell down before him and told him the whole truth. |
| Mar 6:20 | knowing | V-RAP-NSM | none recorded | 18904, 18908, 19239 | 0 | for Herod feared John, **knowing** that he was a righteous and holy man, and he kept him safe. When he heard him, he was greatly perplexed, and yet he heard him gladly. |
| Mar 12:15 | knowing | V-RAP-NSM | none recorded | - | 0 | But, **knowing** their hypocrisy, he said to them, “ Why put me to the test? Bring me a denarius and let me look at it.” |
| Luk 8:53 | knowing | V-RAP-NPM | none recorded | 15226 | 0 | And they laughed at him, **knowing** that she was dead. |
| Luk 9:33 | knowing | V-RAP-NSM | none recorded | - | 0 | And as the men were parting from him, Peter said to Jesus, “ Master, it is good that we are here. Let us make three tents, one for you and one for Moses and one for Elijah ”— not **knowing** what he said. |
| Luk 9:47 | knowing | V-RAP-NSM | none recorded | - | 0 | But Jesus, **knowing** the reasoning of their hearts, took a child and put him by his side |
| Luk 11:17 | knowing | V-RAP-NSM | none recorded | 20455 | 0 | But he, **knowing** their thoughts, said to them, “ Every kingdom divided against itself is laid waste, and a divided household falls. |
| Luk 11:44 | knowing | V-RAI-3P | none recorded | - | 0 | Woe to you! For you are like unmarked graves, and people walk over them without **knowing** it.” |
| Joh 6:61 | knowing | V-RAP-NSM | none recorded | - | 0 | But Jesus, **knowing** in himself that his disciples were grumbling about this, said to them, “Do you take offense at this? |
| Joh 13:3 | knowing | V-RAP-NSM | none recorded | - | 0 | Jesus, **knowing** that the Father had given all things into his hands, and that he had come from God and was going back to God, |
| Joh 18:4 | knowing | V-RAP-NSM | none recorded | - | 0 | Then Jesus, **knowing** all that would happen to him, came forward and said to them, “ Whom do you seek?” |
| Joh 19:28 | knowing | V-RAP-NSM | none recorded | 17776 | 0 | After this, Jesus, **knowing** that all was now finished, said ( to fulfill the Scripture ), “I thirst.” |
| Act 2:30 | knowing | V-RAP-NSM | none recorded | - | 0 | Being therefore a prophet, and **knowing** that God had sworn with an oath to him that he would set one of his descendants on his throne, |
| Act 5:7 | knowing | V-RAP-NSF | none recorded | - | 0 | After an interval of about three hours his wife came in, not **knowing** what had happened. |
| Act 20:22 | knowing | V-RAP-NSM | none recorded | - | 0 | And now, behold, I am going to Jerusalem, constrained by the Spirit, not **knowing** what will happen to me there, |
| Rom 5:3 | knowing | V-RAP-NPM | none recorded | 15195, 15199 | 0 | Not only that, but we rejoice in our sufferings, **knowing** that suffering produces endurance, |
| 1Cor 15:58 | knowing | V-RAP-NPM | none recorded | - | 0 | Therefore, my beloved brothers, be steadfast, immovable, always abounding in the work of the Lord, **knowing** that in the Lord your labor is not in vain. |
| 2Cor 4:14 | knowing | V-RAP-NPM | none recorded | - | 0 | **knowing** that he who raised the Lord Jesus will raise us also with Jesus and bring us with you into his presence. |
| 2Cor 5:11 | knowing | V-RAP-NPM | none recorded | 12670 | 0 | Therefore, **knowing** the fear of the Lord, we persuade others. But what we are is known to God, and I hope it is known also to your conscience. |
| Eph 6:8 | knowing | V-RAP-NPM | none recorded | - | 0 | **knowing** that whatever good anyone does, this he will receive back from the Lord, whether he is a bondservant or is free. |
| Eph 6:9 | knowing | V-RAP-NPM | none recorded | 18989, 18991, 19024 | 0 | Masters, do the same to them, and stop your threatening, **knowing** that he who is both their Master and yours is in heaven, and that there is no partiality with him. |
| Phili 1:16 | knowing | V-RAP-NPM | none recorded | - | 0 | The latter do it out of love, **knowing** that I am put here for the defense of the gospel. |
| Col 3:24 | knowing | V-RAP-NPM | none recorded | - | 0 | **knowing** that from the Lord you will receive the inheritance as your reward. You are serving the Lord Christ. |
| Col 4:1 | knowing | V-RAP-NPM | none recorded | - | 0 | Masters, treat your bondservants justly and fairly, **knowing** that you also have a Master in heaven. |
| 2Ti 3:14 | knowing | V-RAP-NSM | none recorded | - | 0 | But as for you, continue in what you have learned and have firmly believed, **knowing** from whom you learned it |
| Tit 3:11 | knowing | V-RAP-NSM | none recorded | - | 0 | **knowing** that such a person is warped and sinful; he is self-condemned. |
| Phile 21 | knowing | V-RAP-NSM | none recorded | - | 0 | Confident of your obedience, I write to you, **knowing** that you will do even more than I say. |
| 1Pe 1:18 | knowing | V-RAP-NPM | none recorded | - | 0 | **knowing** that you were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold, |
| 1Pe 5:9 | knowing | V-RAP-NPM | none recorded | - | 0 | Resist him, firm in your faith, **knowing** that the same kinds of suffering are being experienced by your brotherhood throughout the world. |
| Act 24:22 | knowledge | V-RAP-NSM | none recorded | - | 0 | But Felix, having a rather accurate **knowledge** of the Way, put them off, saying, “ When Lysias the tribune comes down, I will decide your case.” |
| 1Jo 2:20 | knowledge | V-RAI-2P | none recorded | - | 0 | But you have been anointed by the Holy One, and you all have **knowledge**. |
| Mat 6:8 | knows | V-RAI-3S | none recorded | - | 0 | Do not be like them, for your Father **knows** what you need before you ask him. |
| Mat 6:32 | knows | V-RAI-3S | none recorded | 19246 | 0 | For the Gentiles seek after all these things, and your heavenly Father **knows** that you need them all. |
| Mat 24:36 | knows | V-RAI-3S | none recorded | - | 0 | “ But concerning that day and hour no one **knows**, not even the angels of heaven, nor the Son, but the Father only. |
| Mar 4:27 | knows | V-RAI-3S | none recorded | - | 0 | He sleeps and rises night and day, and the seed sprouts and grows; he **knows** not how. |
| Mar 13:32 | knows | V-RAI-3S | none recorded | - | 0 | “ But concerning that day or that hour, no one **knows**, not even the angels in heaven, nor the Son, but only the Father. |
| Luk 12:30 | knows | V-RAI-3S | none recorded | - | 0 | For all the nations of the world seek after these things, and your Father **knows** that you need them. |
| Joh 19:35 | knows | V-RAI-3S | none recorded | - | 0 | He who saw it has borne witness — his testimony is true, and he **knows** that he is telling the truth — that you also may believe. |
| Rom 8:27 | knows | V-RAI-3S | none recorded | 15957, 16258, 17064, 17263, 19418, 20399 | 0 | And he who searches hearts **knows** what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God. |
| 1Cor 2:11 | knows | V-RAI-3S | none recorded | 15949, 17260, 20455 | 0 | For who **knows** a person’s thoughts except the spirit of that person, which is in him? So also no one comprehends the thoughts of God except the Spirit of God. |
| 2Cor 11:11 | knows | V-RAI-3S | none recorded | - | 0 | And why? Because I do not love you? God **knows** I do! |
| 2Cor 11:31 | knows | V-RAI-3S | none recorded | - | 0 | The God and Father of the Lord Jesus, he who is blessed forever, **knows** that I am not lying. |
| Jam 4:17 | knows | V-RAP-DSM | none recorded | - | 0 | So whoever **knows** the right thing to do and fails to do it, for him it is sin. |
| 2Pe 2:9 | knows | V-RAI-3S | none recorded | - | 0 | then the Lord **knows** how to rescue the godly from trials, and to keep the unrighteous under punishment until the day of judgment, |
| Rev 2:17 | knows | V-RAI-3S | none recorded | - | 0 | He who has an ear, let him hear what the Spirit says to the churches. To the one who conquers I will give some of the hidden manna, and I will give him a white stone, with a new name written on the stone that no one **knows** except the one who receives it.’ |
| Rev 12:12 | knows | V-RAP-NSM | none recorded | 13208 | 0 | Therefore, rejoice, O heavens and you who dwell in them! But woe to you, O earth and sea, for the devil has come down to you in great wrath, because he **knows** that his time is short!” |
| Rev 19:12 | knows | V-RAI-3S | none recorded | - | 0 | His eyes are like a flame of fire, and on his head are many diadems, and he has a name written that no one **knows** but himself. |
| Rev 3:17 | realizing | V-RAI-2S | none recorded | 14346, 15585 | 0 | For you say, “I am rich, I have prospered, and I need nothing,” not **realizing** that you are wretched, pitiable, poor, blind, and naked. |

### 3.3 G1097 γινώσκω ginōskō "to know": 188 own occurrences in 174 verses

- **Meaning as stored:** Greek; native word γινώσκω, transliteration ginōskō; STEP gloss "to know"; sense head "to know" (the code is its own lemma).
- **Related terms (24):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (high).
- **Counts, three measures as stored:** STEP token count 824; verses STEP attests 205; verse_lexical rows the parse found 222.

- **Carried by the member words:** know (118), known (22), knew (14), knows (11), learned (6), perceived (6), aware (5), learn (3), knowing (2), learning (1).
- **Engagement of these occurrences:** none recorded 188.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 12:15 | aware | V-2AAP-NSM | none recorded | - | 0 | Jesus, **aware** of this, withdrew from there. And many followed him, and he healed them all |
| Mat 16:8 | aware | V-2AAP-NSM | none recorded | - | 0 | But Jesus, **aware** of this, said, “O you of little faith, why are you discussing among yourselves the fact that you have no bread? |
| Mat 22:18 | aware | V-2AAP-NSM | none recorded | - | 0 | But Jesus, **aware** of their malice, said, “ Why put me to the test, you hypocrites? |
| Mat 26:10 | aware | V-2AAP-NSM | none recorded | - | 0 | But Jesus, **aware** of this, said to them, “ Why do you trouble the woman? For she has done a beautiful thing to me. |
| Mar 8:17 | aware | V-2AAP-NSM | none recorded | - | 0 | And Jesus, **aware** of this, said to them, “ Why are you discussing the fact that you have no bread? Do you not yet perceive or understand? Are your hearts hardened? |
| Mat 1:25 | knew | V-IAI-3S | none recorded | - | 0 | but **knew** her not until she had given birth to a son. And he called his name Jesus. |
| Mat 7:23 | knew | V-2AAI-1S | none recorded | - | 0 | And then will I declare to them, ‘I never **knew** you; depart from me, you workers of lawlessness.’ |
| Mat 25:24 | knew | V-2AAI-1S | none recorded | 12880, 13766, 13774, 19228 | 0 | He also who had received the one talent came forward, saying, ‘ Master, I **knew** you to be a hard man, reaping where you did not sow, and gathering where you scattered no seed, |
| Luk 12:47 | knew | V-2AAP-NSM | none recorded | 17677 | 0 | And that servant who **knew** his master’s will but did not get ready or act according to his will, will receive a severe beating. |
| Joh 2:24 | knew | V-PAN | none recorded | - | 0 | But Jesus on his part did not entrust himself to them, because he **knew** all people |
| Joh 2:25 | knew | V-IAI-3S | none recorded | - | 0 | and needed no one to bear witness about man, for he himself **knew** what was in man. |
| Joh 4:53 | knew | V-2AAI-3S | none recorded | - | 0 | The father **knew** that was the hour when Jesus had said to him, “ Your son will live.” And he himself believed, and all his household. |
| Joh 5:6 | knew | V-2AAP-NSM | none recorded | - | 0 | When Jesus saw him lying there and **knew** that he had already been there a long time, he said to him, “Do you want to be healed?” |
| Joh 11:57 | knew | V-2AAS-3S | none recorded | - | 0 | Now the chief priests and the Pharisees had given orders that if anyone **knew** where he was, he should let them know, so that they might arrest him. |
| Joh 13:28 | knew | V-2AAI-3S | none recorded | - | 0 | Now no one at the table **knew** why he said this to him. |
| Joh 16:19 | knew | V-2AAI-3S | none recorded | - | 0 | Jesus **knew** that they wanted to ask him, so he said to them, “Is this what you are asking yourselves, what I meant by saying, ‘A little while and you will not see me, and again a little while and you will see me ’? |
| Rom 1:21 | knew | V-2AAP-NPM | none recorded | 15049 | 0 | For although they **knew** God, they did not honor him as God or give thanks to him, but they became futile in their thinking, and their foolish hearts were darkened. |
| 2Cor 5:21 | knew | V-2AAP-ASM | none recorded | - | 0 | For our sake he made him to be sin who **knew** no sin, so that in him we might become the righteousness of God. |
| Heb 10:34 | knew | V-PAP-NPM | none recorded | - | 0 | For you had compassion on those in prison, and you joyfully accepted the plundering of your property, since you **knew** that you yourselves had a better possession and an abiding one. |
| Mat 6:3 | know | V-2AAM-3S | none recorded | - | 0 | But when you give to the needy, do not let your left hand **know** what your right hand is doing, |
| Mat 13:11 | know | V-2AAN | none recorded | - | 0 | And he answered them, “ To you it has been given to **know** the secrets of the kingdom of heaven, but to them it has not been given. |
| Mat 16:3 | know | V-PAI-2P | none recorded | - | 0 | And in the morning, ‘It will be stormy today, for the sky is red and threatening.’ You **know** how to interpret the appearance of the sky, but you cannot interpret the signs of the times. |
| Mat 24:32 | know | V-PAI-2P | none recorded | - | 0 | “ From the fig tree learn its lesson: as soon as its branch becomes tender and puts out its leaves, you **know** that summer is near. |
| Mat 24:33 | know | V-PAI-2P | none recorded | - | 0 | So also, when you see all these things, you **know** that he is near, at the very gates. |
| Mat 24:43 | know | V-PAM-2P | none recorded | - | 0 | But **know** this, that if the master of the house had known in what part of the night the thief was coming, he would have stayed awake and would not have let his house be broken into. |
| Mat 24:50 | know | V-PAI-3S | none recorded | - | 0 | the master of that servant will come on a day when he does not expect him and at an hour he does not **know** |
| Mar 5:43 | know | V-2AAS-3S | none recorded | - | 0 | And he strictly charged them that no one should **know** this, and told them to give her something to eat. |
| Mar 7:24 | know | V-2AAN | none recorded | - | 0 | And from there he arose and went away to the region of Tyre and Sidon. And he entered a house and did not want anyone to **know**, yet he could not be hidden. |
| Mar 9:30 | know | V-2AAS-3S | none recorded | - | 0 | They went on from there and passed through Galilee. And he did not want anyone to **know**, |
| Mar 13:28 | know | V-PAI-2P | none recorded | - | 0 | “ From the fig tree learn its lesson: as soon as its branch becomes tender and puts out its leaves, you **know** that summer is near. |
| Mar 13:29 | know | V-PAM-2P | none recorded | - | 0 | So also, when you see these things taking place, you **know** that he is near, at the very gates. |
| Luk 1:18 | know | V-FDI-1S | none recorded | - | 0 | And Zechariah said to the angel, “ How shall I **know** this? For I am an old man, and my wife is advanced in years.” |
| Luk 2:43 | know | V-2AAI-3P | none recorded | - | 0 | And when the feast was ended, as they were returning, the boy Jesus stayed behind in Jerusalem. His parents did not **know** it, |
| Luk 8:10 | know | V-2AAN | none recorded | - | 0 | he said, “To you it has been given to **know** the secrets of the kingdom of God, but for others they are in parables, so that ‘ seeing they may not see, and hearing they may not understand.’ |
| Luk 10:11 | know | V-PAM-2P | none recorded | - | 0 | ‘ Even the dust of your town that clings to our feet we wipe off against you. Nevertheless **know** this, that the kingdom of God has come near.’ |
| Luk 12:39 | know | V-PAM-2P | none recorded | - | 0 | But **know** this, that if the master of the house had known at what hour the thief was coming, he would not have left his house to be broken into. |
| Luk 12:46 | know | V-PAI-3S | none recorded | - | 0 | the master of that servant will come on a day when he does not expect him and at an hour he does not **know**, and will cut him in pieces and put him with the unfaithful. |
| Luk 12:48 | know | V-2AAP-NSM | none recorded | 17677 | 0 | But the one who did not **know**, and did what deserved a beating, will receive a light beating. Everyone to whom much was given, of him much will be required, and from him to whom they entrusted much, they will demand the more. |
| Luk 19:15 | know | V-2AAS-3S | none recorded | - | 0 | When he returned, having received the kingdom, he ordered these servants to whom he had given the money to be called to him, that he might **know** what they had gained by doing business. |
| Luk 19:44 | know | V-2AAI-2S | none recorded | - | 0 | and tear you down to the ground, you and your children within you. And they will not leave one stone upon another in you, because you did not **know** the time of your visitation.” |
| Luk 21:20 | know | V-2AAM-2P | none recorded | - | 0 | “ But when you see Jerusalem surrounded by armies, then **know** that its desolation has come near. |
| Luk 21:30 | know | V-PAI-2P | none recorded | - | 0 | As soon as they come out in leaf, you see for yourselves and **know** that the summer is already near. |
| Luk 21:31 | know | V-PAM-2P | none recorded | - | 0 | So also, when you see these things taking place, you **know** that the kingdom of God is near. |
| Luk 24:18 | know | V-2AAI-2S | none recorded | - | 0 | Then one of them, named Cleopas, answered him, “Are you the only visitor to Jerusalem who does not **know** the things that have happened there in these days?” |
| Joh 1:10 | know | V-2AAI-3S | none recorded | - | 0 | He was in the world, and the world was made through him, yet the world did not **know** him. |
| Joh 1:48 | know | V-PAI-2S | none recorded | - | 0 | Nathanael said to him, “ How do you **know** me?” Jesus answered him, “ Before Philip called you, when you were under the fig tree, I saw you.” |
| Joh 5:42 | know | V-RAI-1S | none recorded | - | 0 | But I **know** that you do not have the love of God within you. |
| Joh 6:69 | know | V-RAI-1P | none recorded | - | 0 | and we have believed, and have come to **know**, that you are the Holy One of God.” |
| Joh 7:17 | know | V-FDI-3S | none recorded | 17677 | 0 | If anyone’s will is to do God’s will, he will **know** whether the teaching is from God or whether I am speaking on my own authority. |
| Joh 7:26 | know | V-2AAI-3P | none recorded | - | 0 | And here he is, speaking openly, and they say nothing to him! Can it be that the authorities really **know** that this is the Christ? |
| Joh 7:27 | know | V-PAI-3S | none recorded | - | 0 | But we **know** where this man comes from, and when the Christ appears, no one will know where he comes from.” |
| Joh 7:49 | know | V-PAP-NSM | none recorded | - | 0 | But this crowd that does not **know** the law is accursed.” |
| Joh 8:28 | know | V-FDI-2P | none recorded | - | 0 | So Jesus said to them, “ When you have lifted up the Son of Man, then you will **know** that I am he, and that I do nothing on my own authority, but speak just as the Father taught me. |
| Joh 8:32 | know | V-FDI-2P | none recorded | - | 0 | and you will **know** the truth, and the truth will set you free.” |
| Joh 8:52 | know | V-RAI-1P | none recorded | - | 0 | The Jews said to him, “ Now we **know** that you have a demon! Abraham died, as did the prophets, yet you say, ‘ If anyone keeps my word, he will never taste death.’ |
| Joh 10:14 | know | V-PAI-1S | none recorded | - | 0 | I am the good shepherd. I **know** my own and my own know me, |
| Joh 10:14 | know | V-PAI-3P | none recorded | - | 0 | I am the good shepherd. I **know** my own and my own know me, |
| Joh 10:15 | know | V-PAI-1S | none recorded | - | 0 | just as the Father knows me and I **know** the Father; and I lay down my life for the sheep. |
| Joh 10:27 | know | V-PAI-1S | none recorded | - | 0 | My sheep hear my voice, and I **know** them, and they follow me. |
| Joh 10:38 | know | V-2AAS-2P | none recorded | - | 0 | but if I do them, even though you do not believe me, believe the works, that you may **know** and understand that the Father is in me and I am in the Father.” |
| Joh 13:35 | know | V-FDI-3P | none recorded | - | 0 | By this all people will **know** that you are my disciples, if you have love for one another.” |
| Joh 14:7 | know | V-PAI-2P | none recorded | - | 0 | If you had known me, you would have known my Father also. From now on you do **know** him and have seen him.” |
| Joh 14:9 | know | V-RAI-2S | none recorded | - | 0 | Jesus said to him, “Have I been with you so long, and you still do not **know** me, Philip? Whoever has seen me has seen the Father. How can you say, ‘ Show us the Father ’? |
| Joh 14:17 | know | V-PAI-2P | none recorded | - | 0 | even the Spirit of truth, whom the world cannot receive, because it neither sees him nor knows him. You **know** him, for he dwells with you and will be in you. |
| Joh 14:20 | know | V-FDI-2P | none recorded | - | 0 | In that day you will **know** that I am in my Father, and you in me, and I in you. |
| Joh 14:31 | know | V-2AAS-3S | none recorded | - | 0 | but I do as the Father has commanded me, so that the world may **know** that I love the Father. Rise, let us go from here. |
| Joh 15:18 | know | V-PAI-2P | none recorded | 19945 | 0 | “ If the world hates you, **know** that it has hated me before it hated you. |
| Joh 17:3 | know | V-PAS-3P | none recorded | - | 0 | And this is eternal life, that they **know** you, the only true God, and Jesus Christ whom you have sent. |
| Joh 17:7 | know | V-RAI-3P | none recorded | - | 0 | Now they **know** that everything that you have given me is from you. |
| Joh 17:8 | know | V-2AAI-3P | none recorded | - | 0 | For I have given them the words that you gave me, and they have received them and have come to **know** in truth that I came from you; and they have believed that you sent me. |
| Joh 17:23 | know | V-PAS-3S | none recorded | - | 0 | I in them and you in me, that they may become perfectly one, so that the world may **know** that you sent me and loved them even as you loved me. |
| Joh 17:25 | know | V-2AAI-3S | none recorded | - | 0 | O righteous Father, even though the world does not **know** you, I know you, and these know that you have sent me. |
| Joh 17:25 | know | V-2AAI-1S | none recorded | - | 0 | O righteous Father, even though the world does not **know** you, I know you, and these know that you have sent me. |
| Joh 17:25 | know | V-2AAI-3P | none recorded | - | 0 | O righteous Father, even though the world does not **know** you, I know you, and these know that you have sent me. |
| Joh 19:4 | know | V-2AAS-2P | none recorded | - | 0 | Pilate went out again and said to them, “ See, I am bringing him out to you that you may **know** that I find no guilt in him.” |
| Joh 21:17 | know | V-PAI-2S | none recorded | - | 0 | He said to him the third time, “ Simon, son of John, do you love me?” Peter was grieved because he said to him the third time, “Do you love me?” and he said to him, “ Lord, you **know** everything; you know that I love you.” Jesus said to him, “ Feed my sheep. |
| Act 1:7 | know | V-2AAN | none recorded | 19096 | 0 | He said to them, “It is not for you to **know** times or seasons that the Father has fixed by his own authority. |
| Act 2:36 | know | V-PAM-3S | none recorded | - | 0 | Let all the house of Israel therefore **know** for certain that God has made him both Lord and Christ, this Jesus whom you crucified.” |
| Act 17:19 | know | V-2AAN | none recorded | - | 0 | And they took him and brought him to the Areopagus, saying, “ May we **know** what this new teaching is that you are presenting? |
| Act 17:20 | know | V-2AAN | none recorded | 20184 | 0 | For you bring some strange things to our ears. We wish to **know** therefore what these things mean.” |
| Act 19:15 | know | V-PAI-1S | none recorded | 16534, 16757 | 0 | But the evil spirit answered them, “ Jesus I **know**, and Paul I recognize, but who are you?” |
| Act 19:35 | know | V-PAI-3S | none recorded | - | 0 | And when the town clerk had quieted the crowd, he said, “ Men of Ephesus, who is there who does not **know** that the city of the Ephesians is temple keeper of the great Artemis, and of the sacred stone that fell from the sky? |
| Act 20:34 | know | V-PAI-2P | none recorded | 17413 | 0 | You yourselves **know** that these hands ministered to my necessities and to those who were with me. |
| Act 21:24 | know | V-FDI-3P | none recorded | - | 0 | take these men and purify yourself along with them and pay their expenses, so that they may shave their heads. Thus all will **know** that there is nothing in what they have been told about you, but that you yourself also live in observance of the law. |
| Act 21:37 | know | V-PAI-2S | none recorded | - | 0 | As Paul was about to be brought into the barracks, he said to the tribune, “ May I say something to you?” And he said, “Do you **know** Greek? |
| Act 22:14 | know | V-2AAN | none recorded | 17677 | 0 | And he said, ‘The God of our fathers appointed you to **know** his will, to see the Righteous One and to hear a voice from his mouth; |
| Act 22:30 | know | V-2AAN | none recorded | 20184 | 0 | But on the next day, desiring to **know** the real reason why he was being accused by the Jews, he unbound him and commanded the chief priests and all the council to meet, and he brought Paul down and set him before them. |
| Act 23:28 | know | V-2AAN | none recorded | 20184 | 0 | And desiring to **know** the charge for which they were accusing him, I brought him down to their council. |
| Rom 2:18 | know | V-PAI-2S | none recorded | 17677 | 0 | and **know** his will and approve what is excellent, because you are instructed from the law; |
| Rom 6:6 | know | V-PAP-NPM | none recorded | - | 0 | We **know** that our old self was crucified with him in order that the body of sin might be brought to nothing, so that we would no longer be enslaved to sin. |
| Rom 7:1 | know | V-PAP-DPM | none recorded | - | 0 | Or do you not **know**, brothers — for I am speaking to those who know the law — that the law is binding on a person only as long as he lives? |
| 1Cor 1:21 | know | V-2AAI-3S | none recorded | - | 0 | For since, in the wisdom of God, the world did not **know** God through wisdom, it pleased God through the folly of what we preach to save those who believe. |
| 1Cor 8:2 | know | V-2AAI-3S | none recorded | - | 0 | If anyone imagines that he knows something, he does not yet **know** as he ought to know. |
| 1Cor 8:2 | know | V-2AAN | none recorded | - | 0 | If anyone imagines that he knows something, he does not yet **know** as he ought to know. |
| 1Cor 13:9 | know | V-PAI-1P | none recorded | - | 0 | For we **know** in part and we prophesy in part, |
| 1Cor 13:12 | know | V-PAI-1S | none recorded | - | 0 | For now we see in a mirror dimly, but then face to face. Now I **know** in part; then I shall know fully, even as I have been fully known. |
| 1Cor 14:7 | know | V-FPI-3S | none recorded | - | 0 | If even lifeless instruments, such as the flute or the harp, do not give distinct notes, how will anyone **know** what is played? |
| 1Cor 14:9 | know | V-FPI-3S | none recorded | - | 0 | So with yourselves, if with your tongue you utter speech that is not intelligible, how will anyone **know** what is said? For you will be speaking into the air. |
| 2Cor 2:4 | know | V-2AAS-2P | none recorded | - | 0 | For I wrote to you out of much affliction and anguish of heart and with many tears, not to cause you pain but to let you **know** the abundant love that I have for you. |
| 2Cor 2:9 | know | V-2AAS-1S | none recorded | - | 0 | For this is why I wrote, that I might test you and **know** whether you are obedient in everything. |
| 2Cor 8:9 | know | V-PAI-2P | none recorded | - | 0 | For you **know** the grace of our Lord Jesus Christ, that though he was rich, yet for your sake he became poor, so that you by his poverty might become rich. |
| Gal 3:7 | know | V-PAM-2P | none recorded | - | 0 | **Know** then that it is those of faith who are the sons of Abraham. |
| Gal 4:9 | know | V-2AAP-NPM | none recorded | - | 0 | But now that you have come to **know** God, or rather to be known by God, how can you turn back again to the weak and worthless elementary principles of the world, whose slaves you want to be once more? |
| Eph 3:19 | know | V-2AAN | none recorded | - | 0 | and to **know** the love of Christ that surpasses knowledge, that you may be filled with all the fullness of God. |
| Eph 6:22 | know | V-2AAS-2P | none recorded | - | 0 | I have sent him to you for this very purpose, that you may **know** how we are, and that he may encourage your hearts. |
| Phili 1:12 | know | V-PAN | none recorded | 20128, 20186 | 0 | I want you to **know**, brothers, that what has happened to me has really served to advance the gospel, |
| Phili 2:22 | know | V-PAI-2P | none recorded | - | 0 | But you **know** Timothy’s proven worth, how as a son with a father he has served with me in the gospel. |
| Phili 3:10 | know | V-2AAN | none recorded | 18391 | 0 | that I may **know** him and the power of his resurrection, and may share his sufferings, becoming like him in his death, |
| Col 4:8 | know | V-2AAS-2P | none recorded | - | 0 | I have sent him to you for this very purpose, that you may **know** how we are and that he may encourage your hearts, |
| 2Ti 1:18 | know | V-PAI-2S | none recorded | - | 0 | may the Lord grant him to find mercy from the Lord on that day!— and you well **know** all the service he rendered at Ephesus. |
| Heb 8:11 | know | V-2AAM-2S | none recorded | - | 0 | And they shall not teach, each one his neighbor and each one his brother, saying, ‘ **Know** the Lord,’ for they shall all know me, from the least of them to the greatest. |
| Heb 13:23 | know | V-PAI-2P | none recorded | - | 0 | You should **know** that our brother Timothy has been released, with whom I shall see you if he comes soon. |
| Jam 1:3 | know | V-PAP-NPM | none recorded | - | 0 | for you **know** that the testing of your faith produces steadfastness. |
| Jam 5:20 | know | V-PAM-3S | none recorded | - | 0 | let him **know** that whoever brings back a sinner from his wandering will save his soul from death and will cover a multitude of sins. |
| 1Jo 2:3 | know | V-PAI-1P | none recorded | - | 0 | And by this we **know** that we have come to know him, if we keep his commandments. |
| 1Jo 2:3 | know | V-RAI-1P | none recorded | - | 0 | And by this we **know** that we have come to know him, if we keep his commandments. |
| 1Jo 2:4 | know | V-RAI-1S | none recorded | - | 0 | Whoever says “I **know** him ” but does not keep his commandments is a liar, and the truth is not in him, |
| 1Jo 2:5 | know | V-PAI-1P | none recorded | - | 0 | but whoever keeps his word, in him truly the love of God is perfected. By this we may **know** that we are in him: |
| 1Jo 2:13 | know | V-RAI-2P | none recorded | - | 0 | I am writing to you, fathers, because you **know** him who is from the beginning. I am writing to you, young men, because you have overcome the evil one. I write to you, children, because you know the Father. |
| 1Jo 2:13 | know | V-RAI-2P | none recorded | - | 0 | I am writing to you, fathers, because you **know** him who is from the beginning. I am writing to you, young men, because you have overcome the evil one. I write to you, children, because you know the Father. |
| 1Jo 2:14 | know | V-RAI-2P | none recorded | - | 0 | I write to you, fathers, because you **know** him who is from the beginning. I write to you, young men, because you are strong, and the word of God abides in you, and you have overcome the evil one. |
| 1Jo 2:18 | know | V-PAI-1P | none recorded | - | 0 | Children, it is the last hour, and as you have heard that antichrist is coming, so now many antichrists have come. Therefore we **know** that it is the last hour. |
| 1Jo 3:1 | know | V-PAI-3S | none recorded | - | 0 | See what kind of love the Father has given to us, that we should be called children of God; and so we are. The reason why the world does not **know** us is that it did not know him. |
| 1Jo 3:1 | know | V-2AAI-3S | none recorded | - | 0 | See what kind of love the Father has given to us, that we should be called children of God; and so we are. The reason why the world does not **know** us is that it did not know him. |
| 1Jo 3:16 | know | V-RAI-1P | none recorded | - | 0 | By this we **know** love, that he laid down his life for us, and we ought to lay down our lives for the brothers. |
| 1Jo 3:19 | know | V-FDI-1P | none recorded | - | 0 | By this we shall **know** that we are of the truth and reassure our heart before him; |
| 1Jo 3:24 | know | V-PAI-1P | none recorded | - | 0 | Whoever keeps his commandments abides in God, and God in him. And by this we **know** that he abides in us, by the Spirit whom he has given us. |
| 1Jo 4:2 | know | V-PAI-2P | none recorded | - | 0 | By this you **know** the Spirit of God: every spirit that confesses that Jesus Christ has come in the flesh is from God, |
| 1Jo 4:6 | know | V-PAI-1P | none recorded | - | 0 | We are from God. Whoever knows God listens to us; whoever is not from God does not listen to us. By this we **know** the Spirit of truth and the spirit of error. |
| 1Jo 4:8 | know | V-2AAI-3S | none recorded | - | 0 | Anyone who does not love does not **know** God, because God is love. |
| 1Jo 4:13 | know | V-PAI-1P | none recorded | - | 0 | By this we **know** that we abide in him and he in us, because he has given us of his Spirit. |
| 1Jo 4:16 | know | V-RAI-1P | none recorded | - | 0 | So we have come to **know** and to believe the love that God has for us. God is love, and whoever abides in love abides in God, and God abides in him. |
| 1Jo 5:2 | know | V-PAI-1P | none recorded | - | 0 | By this we **know** that we love the children of God, when we love God and obey his commandments. |
| 1Jo 5:20 | know | V-PAS-1P | none recorded | - | 0 | And we **know** that the Son of God has come and has given us understanding, so that we may know him who is true; and we are in him who is true, in his Son Jesus Christ. He is the true God and eternal life. |
| 2Jo 1 | know | V-RAP-NPM | none recorded | 19478, 20293 | 0 | The elder to the elect lady and her children, whom I love in truth, and not only I, but also all who **know** the truth, |
| Rev 2:23 | know | V-FDI-3P | none recorded | 16184, 16393 | 0 | and I will strike her children dead. And all the churches will **know** that I am he who searches mind and heart, and I will give to each of you according to your works. |
| Rev 3:3 | know | V-2AAS-2S | none recorded | - | 0 | Remember, then, what you received and heard. Keep it, and repent. If you will not wake up, I will come like a thief, and you will not **know** at what hour I will come against you. |
| 2Pe 1:20 | knowing | V-PAP-NPM | none recorded | - | 0 | **knowing** this first of all, that no prophecy of Scripture comes from someone’s own interpretation. |
| 2Pe 3:3 | knowing | V-PAP-NPM | none recorded | - | 0 | **knowing** this first of all, that scoffers will come in the last days with scoffing, following their own sinful desires. |
| Mat 10:26 | known | V-FPI-3S | none recorded | - | 0 | “ So have no fear of them, for nothing is covered that will not be revealed, or hidden that will not be **known**. |
| Mat 12:7 | known | V-LAI-2P | none recorded | - | 0 | And if you had **known** what this means, ‘I desire mercy, and not sacrifice,’ you would not have condemned the guiltless. |
| Mat 12:33 | known | V-PPI-3S | none recorded | - | 0 | “ Either make the tree good and its fruit good, or make the tree bad and its fruit bad, for the tree is **known** by its fruit. |
| Luk 6:44 | known | V-PPI-3S | none recorded | - | 0 | for each tree is **known** by its own fruit. For figs are not gathered from thornbushes, nor are grapes picked from a bramble bush. |
| Luk 8:17 | known | V-APS-3S | none recorded | - | 0 | For nothing is hidden that will not be made manifest, nor is anything secret that will not be **known** and come to light. |
| Luk 12:2 | known | V-FPI-3S | none recorded | - | 0 | Nothing is covered up that will not be revealed, or hidden that will not be **known**. |
| Luk 19:42 | known | V-2AAI-2S | none recorded | 19232 | 0 | saying, “ Would that you, even you, had **known** on this day the things that make for peace! But now they are hidden from your eyes. |
| Luk 24:35 | known | V-2API-3S | none recorded | - | 0 | Then they told what had happened on the road, and how he was **known** to them in the breaking of the bread. |
| Joh 8:55 | known | V-RAI-2P | none recorded | - | 0 | But you have not **known** him. I know him. If I were to say that I do not know him, I would be a liar like you, but I do know him and I keep his word. |
| Joh 14:7 | known | V-RAI-2P | none recorded | - | 0 | If you had **known** me, you would have known my Father also. From now on you do know him and have seen him.” |
| Joh 14:7 | known | V-FDI-2P | none recorded | - | 0 | If you had **known** me, you would have known my Father also. From now on you do know him and have seen him.” |
| Joh 16:3 | known | V-2AAI-3P | none recorded | - | 0 | And they will do these things because they have not **known** the Father, nor me. |
| Act 9:24 | known | V-2API-3S | none recorded | - | 0 | but their plot became **known** to Saul. They were watching the gates day and night in order to kill him, |
| Rom 3:17 | known | V-2AAI-3P | none recorded | - | 0 | and the way of peace they have not **known**.” |
| Rom 7:7 | known | V-2AAI-1S | none recorded | 17411 | 0 | What then shall we say? That the law is sin? By no means! Yet if it had not been for the law, I would not have **known** sin. For I would not have known what it is to covet if the law had not said, “You shall not covet.” |
| Rom 11:34 | known | V-2AAI-3S | none recorded | - | 0 | “ For who has **known** the mind of the Lord, or who has been his counselor?” |
| 1Cor 8:3 | known | V-RPI-3S | none recorded | 15151 | 0 | But if anyone loves God, he is **known** by God. |
| 2Cor 3:2 | known | V-PPP-NSF | none recorded | - | 0 | You yourselves are our letter of recommendation, written on our hearts, to be **known** and read by all. |
| Gal 4:9 | known | V-APP-NPM | none recorded | - | 0 | But now that you have come to know God, or rather to be **known** by God, how can you turn back again to the weak and worthless elementary principles of the world, whose slaves you want to be once more? |
| Phili 4:5 | known | V-APM-3S | none recorded | - | 0 | Let your reasonableness be **known** to everyone. The Lord is at hand; |
| Heb 3:10 | known | V-2AAI-3P | none recorded | - | 0 | Therefore I was provoked with that generation, and said, ‘They always go astray in their heart; they have not **known** my ways.’ |
| 1Jo 3:6 | known | V-RAI-3S | none recorded | - | 0 | No one who abides in him keeps on sinning; no one who keeps on sinning has either seen him or **known** him. |
| Mat 9:30 | knows | V-PAM-3S | none recorded | - | 0 | And their eyes were opened. And Jesus sternly warned them, “ See that no one **knows** about it.” |
| Luk 10:22 | knows | V-PAI-3S | none recorded | - | 0 | All things have been handed over to me by my Father, and no one **knows** who the Son is except the Father, or who the Father is except the Son and anyone to whom the Son chooses to reveal him.” |
| Luk 16:15 | knows | V-PAI-3S | none recorded | 15166, 15170, 15944, 16688, 16839, 16841, 17244 | 0 | And he said to them, “ You are those who justify yourselves before men, but God **knows** your hearts. For what is exalted among men is an abomination in the sight of God. |
| Joh 10:15 | knows | V-PAI-3S | none recorded | - | 0 | just as the Father **knows** me and I know the Father; and I lay down my life for the sheep. |
| Joh 14:17 | knows | V-PAI-3S | none recorded | - | 0 | even the Spirit of truth, whom the world cannot receive, because it neither sees him nor **knows** him. You know him, for he dwells with you and will be in you. |
| 1Cor 3:20 | knows | V-PAI-3S | none recorded | 20455 | 0 | and again, “The Lord **knows** the thoughts of the wise, that they are futile.” |
| 1Cor 8:2 | knows | V-RAN | none recorded | 15151 | 0 | If anyone imagines that he **knows** something, he does not yet know as he ought to know. |
| 2Ti 2:19 | knows | V-2AAI-3S | none recorded | - | 0 | But God’s firm foundation stands, bearing this seal: “The Lord **knows** those who are his,” and, “Let everyone who names the name of the Lord depart from iniquity.” |
| 1Jo 3:20 | knows | V-PAI-3S | none recorded | 16841 | 0 | for whenever our heart condemns us, God is greater than our heart, and he **knows** everything. |
| 1Jo 4:6 | knows | V-PAP-NSM | none recorded | - | 0 | We are from God. Whoever **knows** God listens to us; whoever is not from God does not listen to us. By this we know the Spirit of truth and the spirit of error. |
| 1Jo 4:7 | knows | V-PAI-3S | none recorded | - | 0 | Beloved, let us love one another, for love is from God, and whoever loves has been born of God and **knows** God. |
| Act 21:34 | learn | V-2AAN | none recorded | - | 0 | Some in the crowd were shouting one thing, some another. And as he could not **learn** the facts because of the uproar, he ordered him to be brought into the barracks. |
| 1Th 3:5 | learn | V-2AAN | none recorded | - | 0 | For this reason, when I could bear it no longer, I sent to **learn** about your faith, for fear that somehow the tempter had tempted you and our labor would be in vain. |
| Rev 3:9 | learn | V-2AAS-3P | none recorded | - | 0 | Behold, I will make those of the synagogue of Satan who say that they are Jews and are not, but lie — behold, I will make them come and bow down before your feet, and they will **learn** that I have loved you. |
| Mar 15:45 | learned | V-2AAP-NSM | none recorded | - | 0 | And when he **learned** from the centurion that he was dead, he granted the corpse to Joseph. |
| Luk 9:11 | learned | V-2AAP-NPM | none recorded | - | 0 | When the crowds **learned** it, they followed him, and he welcomed them and spoke to them of the kingdom of God and cured those who had need of healing. |
| Joh 4:1 | learned | V-2AAI-3S | none recorded | - | 0 | Now when Jesus **learned** that the Pharisees had heard that Jesus was making and baptizing more disciples than John |
| Joh 12:9 | learned | V-2AAI-3S | none recorded | - | 0 | When the large crowd of the Jews **learned** that Jesus was there, they came, not only on account of him but also to see Lazarus, whom he had raised from the dead. |
| Act 17:13 | learned | V-2AAI-3P | none recorded | - | 0 | But when the Jews from Thessalonica **learned** that the word of God was proclaimed by Paul at Berea also, they came there too, agitating and stirring up the crowds. |
| Rev 2:24 | learned | V-2AAI-3P | none recorded | - | 0 | But to the rest of you in Thyatira, who do not hold this teaching, who have not **learned** what some call the deep things of Satan, to you I say, I do not lay on you any other burden. |
| Joh 7:51 | learning | V-2AAS-3S | none recorded | - | 0 | “Does our law judge a man without first giving him a hearing and **learning** what he does?” |
| Mat 21:45 | perceived | V-2AAI-3P | none recorded | - | 0 | When the chief priests and the Pharisees heard his parables, they **perceived** that he was speaking about them. |
| Mar 12:12 | perceived | V-2AAI-3P | none recorded | - | 0 | And they were seeking to arrest him but feared the people, for they **perceived** that he had told the parable against them. So they left him and went away. |
| Mar 15:10 | perceived | V-IAI-3S | none recorded | - | 0 | For he **perceived** that it was out of envy that the chief priests had delivered him up. |
| Luk 20:19 | perceived | V-2AAI-3P | none recorded | - | 0 | The scribes and the chief priests sought to lay hands on him at that very hour, for they **perceived** that he had told this parable against them, but they feared the people. |
| Act 23:6 | perceived | V-2AAP-NSM | none recorded | - | 0 | Now when Paul **perceived** that one part were Sadducees and the other Pharisees, he cried out in the council, “ Brothers, I am a Pharisee, a son of Pharisees. It is with respect to the hope and the resurrection of the dead that I am on trial.” |
| Gal 2:9 | perceived | V-2AAP-NPM | none recorded | - | 0 | and when James and Cephas and John, who seemed to be pillars, **perceived** the grace that was given to me, they gave the right hand of fellowship to Barnabas and me, that we should go to the Gentiles and they to the circumcised. |

### 3.4 H1847 דַּ֫עַת da.at "knowledge": 84 own occurrences in 82 verses

- **Meaning as stored:** Hebrew; native word דַּ֫עַת, transliteration da.at; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1847):** knowledge.
- **Related terms (20):** H1843 de.a "knowledge"; H1844 de.ah "knowledge"; H1845 de.u.el "Deuel"; H3037G yad.du.a "Jaddua"; H3037H yad.du.a "Jaddua"; H3043G ye.di.a.el "Jediael"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 91; verses STEP attests 89; verse_lexical rows the parse found 91.

- **Carried by the member words:** knowledge (81), know (3).
- **Engagement of these occurrences:** none recorded 84.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 13:2 | know | HNcfsc | none recorded | - | 0 | What you **know**, I also know; I am not inferior to you. |
| Job 33:3 | know | HNcfsc | none recorded | - | 0 | My words declare the uprightness of my heart, and what my lips **know** they speak sincerely. |
| Isa 58:2 | know | HNcfsc | none recorded | 17632, 19957 | 0 | Yet they seek me daily and delight to **know** my ways, as if they were a nation that did righteousness and did not forsake the judgment of their God; they ask of me righteous judgments; they delight to draw near to God. |
| Gen 2:9 | knowledge | HNcfsc | none recorded | - | 0 | And out of the ground the Lord God made to spring up every tree that is pleasant to the sight and good for food. The tree of life was in the midst of the garden, and the tree of the **knowledge** of good and evil. |
| Gen 2:17 | knowledge | HNcfsc | none recorded | - | 0 | but of the tree of the **knowledge** of good and evil you shall not eat, for in the day that you eat of it you shall surely die.” |
| Exo 31:3 | knowledge | HNcfsa | none recorded | 15957, 17263 | 0 | and I have filled him with the Spirit of God, with ability and intelligence, with **knowledge** and all craftsmanship, |
| Exo 35:31 | knowledge | HNcfsa | none recorded | 15957, 17263 | 0 | and he has filled him with the Spirit of God, with skill, with intelligence, with **knowledge**, and with all craftsmanship, |
| Num 24:16 | knowledge | HNcfsc | none recorded | - | 0 | the oracle of him who hears the words of God, and knows the **knowledge** of the Most High, who sees the vision of the Almighty, falling down with his eyes uncovered: |
| Job 15:2 | knowledge | HNcfsc | none recorded | 15965, 17264, 20304 | 0 | “Should a wise man answer with windy **knowledge**, and fill his belly with the east wind? |
| Job 21:14 | knowledge | HNcfsc | none recorded | 14605, 17634 | 0 | They say to God, ‘ Depart from us! We do not desire the **knowledge** of your ways. |
| Job 21:22 | knowledge | HNcfsa | none recorded | - | 0 | Will any teach God **knowledge**, seeing that he judges those who are on high? |
| Job 34:35 | knowledge | HNcfsa | none recorded | 19589 | 0 | ‘ Job speaks without **knowledge**; his words are without insight.’ |
| Job 35:16 | knowledge | HNcfsa | none recorded | - | 0 | Job opens his mouth in empty talk; he multiplies words without **knowledge**.” |
| Job 36:12 | knowledge | HNcfsa | none recorded | 18557 | 0 | But if they do not listen, they perish by the sword and die without **knowledge**. |
| Job 38:2 | knowledge | HNcfsa | none recorded | - | 0 | “ Who is this that darkens counsel by words without **knowledge**? |
| Job 42:3 | knowledge | HNcfsa | none recorded | - | 0 | ‘ Who is this that hides counsel without **knowledge**?’ Therefore I have uttered what I did not understand, things too wonderful for me, which I did not know. |
| Psa 19:2 | knowledge | HNcfsa | none recorded | - | 0 | Day to day pours out speech, and night to night reveals **knowledge**. |
| Psa 94:10 | knowledge | HNcfsa | none recorded | - | 0 | He who disciplines the nations, does he not rebuke? He who teaches man **knowledge** — |
| Psa 119:66 | knowledge | HNcfsa | none recorded | - | 0 | Teach me good judgment and **knowledge**, for I believe in your commandments. |
| Psa 139:6 | knowledge | HNcfsa | none recorded | - | 0 | Such **knowledge** is too wonderful for me; it is high; I cannot attain it. |
| Pro 1:4 | knowledge | HNcfsa | none recorded | 20438 | 0 | to give prudence to the simple, **knowledge** and discretion to the youth — |
| Pro 1:7 | knowledge | HNcfsa | none recorded | 12598, 12676, 13184 | 0 | The fear of the Lord is the beginning of **knowledge**; fools despise wisdom and instruction. |
| Pro 1:22 | knowledge | HNcfsa | none recorded | 15205 | 0 | “How long, O simple ones, will you love being simple? How long will scoffers delight in their scoffing and fools hate **knowledge**? |
| Pro 1:29 | knowledge | HNcfsa | none recorded | 19740, 20164, 20402 | 0 | Because they hated **knowledge** and did not choose the fear of the Lord, |
| Pro 2:5 | knowledge | HNcfsc | none recorded | - | 0 | then you will understand the fear of the Lord and find the **knowledge** of God. |
| Pro 2:6 | knowledge | HNcfsa | none recorded | - | 0 | For the Lord gives wisdom; from his mouth come **knowledge** and understanding; |
| Pro 2:10 | knowledge | HNcfsa | none recorded | 15947, 17017, 17270, 17271 | 0 | for wisdom will come into your heart, and **knowledge** will be pleasant to your soul; |
| Pro 3:20 | knowledge | HNcfsc | none recorded | - | 0 | by his **knowledge** the deeps broke open, and the clouds drop down the dew. |
| Pro 5:2 | knowledge | HNcfsa | none recorded | 20438 | 0 | that you may keep discretion, and your lips may guard **knowledge**. |
| Pro 8:9 | knowledge | HNcfsa | none recorded | 19592 | 0 | They are all straight to him who understands, and right to those who find **knowledge**. |
| Pro 8:10 | knowledge | HNcfsa | none recorded | 19473, 19593, 19599 | 0 | Take my instruction instead of silver, and **knowledge** rather than choice gold, |
| Pro 8:12 | knowledge | HNcfsc | none recorded | 20438 | 0 | “ I, wisdom, dwell with prudence, and I find **knowledge** and discretion. |
| Pro 9:10 | knowledge | HNcfsc | none recorded | - | 0 | The fear of the Lord is the beginning of wisdom, and the **knowledge** of the Holy One is insight. |
| Pro 10:14 | knowledge | HNcfsa | none recorded | - | 0 | The wise lay up **knowledge**, but the mouth of a fool brings ruin near. |
| Pro 11:9 | knowledge | HNcfsa | none recorded | - | 0 | With his mouth the godless man would destroy his neighbor, but by **knowledge** the righteous are delivered. |
| Pro 12:1 | knowledge | HNcfsa | none recorded | - | 0 | Whoever loves discipline loves **knowledge**, but he who hates reproof is stupid. |
| Pro 12:23 | knowledge | HNcfsa | none recorded | 16480 | 0 | A prudent man conceals **knowledge**, but the heart of fools proclaims folly. |
| Pro 13:16 | knowledge | HNcfsa | none recorded | - | 0 | Every prudent man acts with **knowledge**, but a fool flaunts his folly. |
| Pro 14:6 | knowledge | HNcfsa | none recorded | 15205 | 0 | A scoffer seeks wisdom in vain, but **knowledge** is easy for a man of understanding. |
| Pro 14:7 | knowledge | HNcfsa | none recorded | - | 0 | Leave the presence of a fool, for there you do not meet words of **knowledge**. |
| Pro 14:18 | knowledge | HNcfsa | none recorded | - | 0 | The simple inherit folly, but the prudent are crowned with **knowledge**. |
| Pro 15:2 | knowledge | HNcfsa | none recorded | - | 0 | The tongue of the wise commends **knowledge**, but the mouths of fools pour out folly. |
| Pro 15:7 | knowledge | HNcfsa | none recorded | - | 0 | The lips of the wise spread **knowledge**; not so the hearts of fools. |
| Pro 15:14 | knowledge | HNcfsa | none recorded | 17112 | 0 | The heart of him who has understanding seeks **knowledge**, but the mouths of fools feed on folly. |
| Pro 17:27 | knowledge | HNcfsa | none recorded | - | 0 | Whoever restrains his words has **knowledge**, and he who has a cool spirit is a man of understanding. |
| Pro 18:15 | knowledge | HNcfsa | none recorded | 17112, 17236 | 0 | An intelligent heart acquires **knowledge**, and the ear of the wise seeks knowledge. |
| Pro 18:15 | knowledge | HNcfsa | none recorded | 17112, 17236 | 0 | An intelligent heart acquires **knowledge**, and the ear of the wise seeks knowledge. |
| Pro 19:2 | knowledge | HNcfsa | none recorded | 15948, 17041 | 0 | Desire without **knowledge** is not good, and whoever makes haste with his feet misses his way. |
| Pro 19:25 | knowledge | HNcfsa | none recorded | 15205 | 0 | Strike a scoffer, and the simple will learn prudence; reprove a man of understanding, and he will gain **knowledge**. |
| Pro 19:27 | knowledge | HNcfsa | none recorded | - | 0 | Cease to hear instruction, my son, and you will stray from the words of **knowledge**. |
| Pro 20:15 | knowledge | HNcfsa | none recorded | - | 0 | There is gold and abundance of costly stones, but the lips of **knowledge** are a precious jewel. |
| Pro 21:11 | knowledge | HNcfsa | none recorded | 15205 | 0 | When a scoffer is punished, the simple becomes wise; when a wise man is instructed, he gains **knowledge**. |
| Pro 22:12 | knowledge | HNcfsa | none recorded | - | 0 | The eyes of the Lord keep watch over **knowledge**, but he overthrows the words of the traitor. |
| Pro 22:17 | knowledge | HNcfsc | none recorded | - | 0 | Incline your ear, and hear the words of the wise, and apply your heart to my **knowledge**, |
| Pro 22:20 | knowledge | HNcfsa | none recorded | - | 0 | Have I not written for you thirty sayings of counsel and **knowledge**, |
| Pro 23:12 | knowledge | HNcfsa | none recorded | - | 0 | Apply your heart to instruction and your ear to words of **knowledge**. |
| Pro 24:4 | knowledge | HNcfsa | none recorded | - | 0 | by **knowledge** the rooms are filled with all precious and pleasant riches. |
| Pro 24:5 | knowledge | HNcfsa | none recorded | - | 0 | A wise man is full of strength, and a man of **knowledge** enhances his might, |
| Pro 29:7 | knowledge | HNcfsa | none recorded | - | 0 | A righteous man knows the rights of the poor; a wicked man does not understand such **knowledge**. |
| Pro 30:3 | knowledge | HNcfsc | none recorded | - | 0 | I have not learned wisdom, nor have I **knowledge** of the Holy One. |
| Ecc 1:16 | knowledge | HNcfsa | none recorded | 13918 | 0 | I said in my heart, “ I have acquired great wisdom, surpassing all who were over Jerusalem before me, and my heart has had great experience of wisdom and **knowledge**.” |
| Ecc 1:18 | knowledge | HNcfsa | none recorded | 14224 | 0 | For in much wisdom is much vexation, and he who increases **knowledge** increases sorrow. |
| Ecc 2:21 | knowledge | HNcfsa | none recorded | - | 0 | because sometimes a person who has toiled with wisdom and **knowledge** and skill must leave everything to be enjoyed by someone who did not toil for it. This also is vanity and a great evil. |
| Ecc 2:26 | knowledge | HNcfsa | none recorded | - | 0 | For to the one who pleases him God has given wisdom and **knowledge** and joy, but to the sinner he has given the business of gathering and collecting, only to give to one who pleases God. This also is vanity and a striving after wind. |
| Ecc 7:12 | knowledge | HNcfsa | none recorded | - | 0 | For the protection of wisdom is like the protection of money, and the advantage of **knowledge** is that wisdom preserves the life of him who has it. |
| Ecc 9:10 | knowledge | HNcfsa | none recorded | - | 0 | Whatever your hand finds to do, do it with your might, for there is no work or thought or **knowledge** or wisdom in Sheol, to which you are going. |
| Ecc 12:9 | knowledge | HNcfsa | none recorded | - | 0 | Besides being wise, the Preacher also taught the people **knowledge**, weighing and studying and arranging many proverbs with great care. |
| Isa 5:13 | knowledge | HNcfsa | none recorded | 17782 | 0 | Therefore my people go into exile for lack of **knowledge**; their honored men go hungry, and their multitude is parched with thirst. |
| Isa 11:2 | knowledge | HNcfsa | none recorded | 15840, 15957 | 0 | And the Spirit of the Lord shall rest upon him, the Spirit of wisdom and understanding, the Spirit of counsel and might, the Spirit of **knowledge** and the fear of the Lord. |
| Isa 33:6 | knowledge | HNcfsa | none recorded | - | 0 | and he will be the stability of your times, abundance of salvation, wisdom, and **knowledge**; the fear of the Lord is Zion’s treasure. |
| Isa 40:14 | knowledge | HNcfsa | none recorded | - | 0 | Whom did he consult, and who made him understand? Who taught him the path of justice, and taught him **knowledge**, and showed him the way of understanding? |
| Isa 44:19 | knowledge | HNcfsa | none recorded | - | 0 | No one considers, nor is there **knowledge** or discernment to say, “ Half of it I burned in the fire; I also baked bread on its coals; I roasted meat and have eaten. And shall I make the rest of it an abomination? Shall I fall down before a block of wood?” |
| Isa 44:25 | knowledge | HNcfsc | none recorded | - | 0 | who frustrates the signs of liars and makes fools of diviners, who turns wise men back and makes their **knowledge** foolish, |
| Isa 47:10 | knowledge | HNcfsc | none recorded | 15968 | 0 | You felt secure in your wickedness; you said, “No one sees me”; your wisdom and your **knowledge** led you astray, and you said in your heart, “ I am, and there is no one besides me.” |
| Isa 53:11 | knowledge | HNcfsc | none recorded | - | 0 | Out of the anguish of his soul he shall see and be satisfied; by his **knowledge** shall the righteous one, my servant, make many to be accounted righteous, and he shall bear their iniquities. |
| Jer 10:14 | knowledge | HNcfsa | none recorded | 15965 | 0 | Every man is stupid and without **knowledge**; every goldsmith is put to shame by his idols, for his images are false, and there is no breath in them. |
| Jer 51:17 | knowledge | HNcfsa | none recorded | 15965 | 0 | Every man is stupid and without **knowledge**; every goldsmith is put to shame by his idols, for his images are false, and there is no breath in them. |
| Dan 1:4 | knowledge | HNcfsa | none recorded | - | 0 | youths without blemish, of good appearance and skillful in all wisdom, endowed with **knowledge**, understanding learning, and competent to stand in the king’s palace, and to teach them the literature and language of the Chaldeans. |
| Dan 12:4 | knowledge | HNcfsa | none recorded | - | 0 | But you, Daniel, shut up the words and seal the book, until the time of the end. Many shall run to and fro, and **knowledge** shall increase.” |
| Hos 4:1 | knowledge | HNcfsc | none recorded | - | 0 | Hear the word of the Lord, O children of Israel, for the Lord has a controversy with the inhabitants of the land. There is no faithfulness or steadfast love, and no **knowledge** of God in the land; |
| Hos 4:6 | knowledge | HNcfsa | none recorded | - | 0 | My people are destroyed for lack of **knowledge**; because you have rejected knowledge, I reject you from being a priest to me. And since you have forgotten the law of your God, I also will forget your children. |
| Hos 4:6 | knowledge | HNcfsa | none recorded | - | 0 | My people are destroyed for lack of **knowledge**; because you have rejected knowledge, I reject you from being a priest to me. And since you have forgotten the law of your God, I also will forget your children. |
| Hos 6:6 | knowledge | HNcfsc | none recorded | - | 0 | For I desire steadfast love and not sacrifice, the **knowledge** of God rather than burnt offerings. |
| Mal 2:7 | knowledge | HNcfsa | none recorded | - | 0 | For the lips of a priest should guard **knowledge**, and people should seek instruction from his mouth, for he is the messenger of the Lord of hosts. |

### 3.5 G1492G εἴδω eidō "to perceive: understand": 39 own occurrences in 21 verses

- **Meaning as stored:** Greek; native word εἴδω, transliteration eidō; STEP gloss "to perceive: understand"; sense head "to perceive: understand" (the code is its own lemma).
- **Related terms (28):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (medium).
- **Counts, three measures as stored:** STEP token count 1390; verses STEP attests 49; verse_lexical rows the parse found 68.

- **Carried by the member words:** know (35), knows (2), knew (1), known (1).
- **Engagement of these occurrences:** none recorded 39.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 11:42 | knew | V-2LAI-1S | none recorded | - | 0 | I **knew** that you always hear me, but I said this on account of the people standing around, that they may believe that you sent me.” |
| Luk 12:56 | know | V-PAI-2P | none recorded | - | 0 | You hypocrites! You **know** how to interpret the appearance of earth and sky, but why do you not know how to interpret the present time? |
| Joh 1:31 | know | V-2LAI-1S | none recorded | - | 0 | I myself did not **know** him, but for this purpose I came baptizing with water, that he might be revealed to Israel.” |
| Joh 4:22 | know | V-PAI-2P | none recorded | - | 0 | You worship what you do not **know**; we worship what we know, for salvation is from the Jews. |
| Joh 4:22 | know | V-PAI-1P | none recorded | - | 0 | You worship what you do not **know**; we worship what we know, for salvation is from the Jews. |
| Joh 7:28 | know | V-PAI-2P | none recorded | - | 0 | So Jesus proclaimed, as he taught in the temple, “You **know** me, and you know where I come from. But I have not come of my own accord. He who sent me is true, and him you do not know. |
| Joh 7:28 | know | V-PAI-2P | none recorded | - | 0 | So Jesus proclaimed, as he taught in the temple, “You **know** me, and you know where I come from. But I have not come of my own accord. He who sent me is true, and him you do not know. |
| Joh 7:28 | know | V-PAI-2P | none recorded | - | 0 | So Jesus proclaimed, as he taught in the temple, “You **know** me, and you know where I come from. But I have not come of my own accord. He who sent me is true, and him you do not know. |
| Joh 8:14 | know | V-PAI-1S | none recorded | - | 0 | Jesus answered, “ Even if I do bear witness about myself, my testimony is true, for I **know** where I came from and where I am going, but you do not know where I come from or where I am going. |
| Joh 8:14 | know | V-PAI-2P | none recorded | - | 0 | Jesus answered, “ Even if I do bear witness about myself, my testimony is true, for I **know** where I came from and where I am going, but you do not know where I come from or where I am going. |
| Joh 8:55 | know | V-PAI-1S | none recorded | - | 0 | But you have not known him. I **know** him. If I were to say that I do not know him, I would be a liar like you, but I do know him and I keep his word. |
| Joh 8:55 | know | V-PAI-1S | none recorded | - | 0 | But you have not known him. I **know** him. If I were to say that I do not know him, I would be a liar like you, but I do know him and I keep his word. |
| Joh 8:55 | know | V-PAI-1S | none recorded | - | 0 | But you have not known him. I **know** him. If I were to say that I do not know him, I would be a liar like you, but I do know him and I keep his word. |
| Joh 9:21 | know | V-PAI-1P | none recorded | - | 0 | But how he now sees we do not **know**, nor do we know who opened his eyes. Ask him; he is of age. He will speak for himself.” |
| Joh 9:21 | know | V-PAI-1P | none recorded | - | 0 | But how he now sees we do not **know**, nor do we know who opened his eyes. Ask him; he is of age. He will speak for himself.” |
| Joh 9:25 | know | V-PAI-1S | none recorded | - | 0 | He answered, “ Whether he is a sinner I do not **know**. One thing I do know, that though I was blind, now I see.” |
| Joh 9:25 | know | V-PAI-1S | none recorded | - | 0 | He answered, “ Whether he is a sinner I do not **know**. One thing I do know, that though I was blind, now I see.” |
| Joh 9:29 | know | V-PAI-1P | none recorded | 17682 | 0 | We **know** that God has spoken to Moses, but as for this man, we do not know where he comes from.” |
| Joh 9:29 | know | V-PAI-1P | none recorded | 17682 | 0 | We **know** that God has spoken to Moses, but as for this man, we do not know where he comes from.” |
| Joh 14:4 | know | V-PAI-2P | none recorded | - | 0 | And you **know** the way to where I am going.” |
| Joh 16:30 | know | V-PAI-1P | none recorded | - | 0 | Now we **know** that you know all things and do not need anyone to question you; this is why we believe that you came from God.” |
| Joh 16:30 | know | V-PAI-2S | none recorded | - | 0 | Now we **know** that you know all things and do not need anyone to question you; this is why we believe that you came from God.” |
| Act 23:5 | know | V-2LAI-1S | none recorded | - | 0 | And Paul said, “I did not **know**, brothers, that he was the high priest, for it is written, ‘You shall not speak evil of a ruler of your people.’” |
| 1Cor 6:19 | know | V-RAI-2P | none recorded | - | 0 | Or do you not **know** that your body is a temple of the Holy Spirit within you, whom you have from God? You are not your own, |
| 1Cor 7:16 | know | V-PAI-2S | none recorded | - | 0 | For how do you **know**, wife, whether you will save your husband? Or how do you know, husband, whether you will save your wife? |
| 1Cor 7:16 | know | V-PAI-2S | none recorded | - | 0 | For how do you **know**, wife, whether you will save your husband? Or how do you know, husband, whether you will save your wife? |
| 2Cor 12:2 | know | V-PAI-1S | none recorded | - | 0 | I **know** a man in Christ who fourteen years ago was caught up to the third heaven — whether in the body or out of the body I do not know, God knows. |
| 2Cor 12:2 | know | V-PAI-1S | none recorded | - | 0 | I **know** a man in Christ who fourteen years ago was caught up to the third heaven — whether in the body or out of the body I do not know, God knows. |
| 2Cor 12:3 | know | V-PAI-1S | none recorded | - | 0 | And I **know** that this man was caught up into paradise — whether in the body or out of the body I do not know, God knows — |
| 2Cor 12:3 | know | V-PAI-1S | none recorded | - | 0 | And I **know** that this man was caught up into paradise — whether in the body or out of the body I do not know, God knows — |
| Phili 4:12 | know | V-PAI-1S | none recorded | 15470 | 0 | I **know** how to be brought low, and I know how to abound. In any and every circumstance, I have learned the secret of facing plenty and hunger, abundance and need. |
| Phili 4:12 | know | V-PAI-1S | none recorded | 15470 | 0 | I **know** how to be brought low, and I know how to abound. In any and every circumstance, I have learned the secret of facing plenty and hunger, abundance and need. |
| 1Jo 2:21 | know | V-PAI-2P | none recorded | - | 0 | I write to you, not because you do not **know** the truth, but because you know it, and because no lie is of the truth. |
| 1Jo 2:21 | know | V-PAI-2P | none recorded | - | 0 | I write to you, not because you do not **know** the truth, but because you know it, and because no lie is of the truth. |
| 1Jo 5:15 | know | V-PAI-1P | none recorded | - | 0 | And if we **know** that he hears us in whatever we ask, we know that we have the requests that we have asked of him. |
| 1Jo 5:15 | know | V-PAI-1P | none recorded | - | 0 | And if we **know** that he hears us in whatever we ask, we know that we have the requests that we have asked of him. |
| Rom 7:7 | known | V-2LAI-1S | none recorded | 17411 | 0 | What then shall we say? That the law is sin? By no means! Yet if it had not been for the law, I would not have **known** sin. For I would not have known what it is to covet if the law had not said, “You shall not covet.” |
| 2Cor 12:2 | knows | V-PAI-1S | none recorded | - | 0 | I know a man in Christ who fourteen years ago was caught up to the third heaven — whether in the body or out of the body I do not know, God **knows**. |
| 2Cor 12:3 | knows | V-PAI-3S | none recorded | - | 0 | And I know that this man was caught up into paradise — whether in the body or out of the body I do not know, God **knows** — |

### 3.6 H3046 יְדַע ye.da "to know": 38 own occurrences in 34 verses

- **Meaning as stored:** Hebrew; native word יְדַע, transliteration ye.da; STEP gloss "to know"; sense head "to know" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3046):** to know.
- **Related terms (2):** H3045 ya.da "to know"; H4486 man.da "knowledge".
- **Clusters (cluster_strong):** M15 Knowing & Understanding (medium).
- **Counts, three measures as stored:** STEP token count 47; verses STEP attests 42; verse_lexical rows the parse found 47.

- **Carried by the member words:** known (13), know (12), make known (10), knew (1), knows (1), learn (1).
- **Engagement of these occurrences:** none recorded 38.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 5:22 | knew | AVqp2ms | none recorded | 15333, 15339, 16708, 20194, 20216 | 0 | And you his son, Belshazzar, have not humbled your heart, though you **knew** all this, |
| Ezr 7:25 | know | AVqrmpc | none recorded | - | 0 | “And you, Ezra, according to the wisdom of your God that is in your hand, appoint magistrates and judges who may judge all the people in the province Beyond the River, all such as **know** the laws of your God. And those who do not know them, you shall teach. |
| Ezr 7:25 | know | AVqrmsa | none recorded | - | 0 | “And you, Ezra, according to the wisdom of your God that is in your hand, appoint magistrates and judges who may judge all the people in the province Beyond the River, all such as **know** the laws of your God. And those who do not know them, you shall teach. |
| Dan 2:8 | know | AVqrmsa | none recorded | - | 0 | The king answered and said, “ I **know** with certainty that you are trying to gain time, because you see that the word from me is firm — |
| Dan 2:9 | know | AVqu1cs | none recorded | - | 0 | if you do not make the dream known to me, there is but one sentence for you. You have agreed to speak lying and corrupt words before me till the times change. Therefore tell me the dream, and I shall **know** that you can show me its interpretation.” |
| Dan 2:30 | know | AVqi2ms | none recorded | - | 0 | But as for me, this mystery has been revealed to me, not because of any wisdom that I have more than all the living, but in order that the interpretation may be made known to the king, and that you may **know** the thoughts of your mind. |
| Dan 4:9 | know | AVqp1cs | none recorded | - | 0 | “O Belteshazzar, chief of the magicians, because I **know** that the spirit of the holy gods is in you and that no mystery is too difficult for you, tell me the visions of my dream that I saw and their interpretation. |
| Dan 4:17 | know | AVqi3mp | none recorded | - | 0 | The sentence is by the decree of the watchers, the decision by the word of the holy ones, to the end that the living may **know** that the Most High rules the kingdom of men and gives it to whom he will and sets over it the lowliest of men.’ |
| Dan 4:25 | know | AVqi2ms | none recorded | - | 0 | that you shall be driven from among men, and your dwelling shall be with the beasts of the field. You shall be made to eat grass like an ox, and you shall be wet with the dew of heaven, and seven periods of time shall pass over you, till you **know** that the Most High rules the kingdom of men and gives it to whom he will. |
| Dan 4:26 | know | AVqi2ms | none recorded | 19076 | 0 | And as it was commanded to leave the stump of the roots of the tree, your kingdom shall be confirmed for you from the time that you **know** that Heaven rules. |
| Dan 4:32 | know | AVqi2ms | none recorded | - | 0 | and you shall be driven from among men, and your dwelling shall be with the beasts of the field. And you shall be made to eat grass like an ox, and seven periods of time shall pass over you, until you **know** that the Most High rules the kingdom of men and gives it to whom he will.” |
| Dan 5:23 | know | AVqrmpa | none recorded | - | 0 | but you have lifted up yourself against the Lord of heaven. And the vessels of his house have been brought in before you, and you and your lords, your wives, and your concubines have drunk wine from them. And you have praised the gods of silver and gold, of bronze, iron, wood, and stone, which do not see or hear or **know**, but the God in whose hand is your breath, and whose are all your ways, you have not honored. |
| Dan 6:15 | know | AVqv2ms | none recorded | - | 0 | Then these men came by agreement to the king and said to the king, “ **Know**, O king, that it is a law of the Medes and Persians that no injunction or ordinance that the king establishes can be changed.” |
| Ezr 4:12 | known | AVQrmsa | none recorded | - | 0 | be it **known** to the king that the Jews who came up from you to us have gone to Jerusalem. They are rebuilding that rebellious and wicked city. They are finishing the walls and repairing the foundations. |
| Ezr 4:13 | known | AVQrmsa | none recorded | - | 0 | Now be it **known** to the king that if this city is rebuilt and the walls finished, they will not pay tribute, custom, or toll, and the royal revenue will be impaired. |
| Ezr 4:16 | known | AVhrmpa | none recorded | - | 0 | We make **known** to the king that if this city is rebuilt and its walls finished, you will then have no possession in the province Beyond the River.” |
| Dan 2:9 | known | AVhi2mp | none recorded | - | 0 | if you do not make the dream **known** to me, there is but one sentence for you. You have agreed to speak lying and corrupt words before me till the times change. Therefore tell me the dream, and I shall know that you can show me its interpretation.” |
| Dan 2:15 | known | AVhp3ms | none recorded | - | 0 | He declared to Arioch, the king’s captain, “ Why is the decree of the king so urgent?” Then Arioch made the matter **known** to Daniel. |
| Dan 2:17 | known | AVhp3ms | none recorded | - | 0 | Then Daniel went to his house and made the matter **known** to Hananiah, Mishael, and Azariah, his companions, |
| Dan 2:23 | known | AVhp2ms | none recorded | - | 0 | To you, O God of my fathers, I give thanks and praise, for you have given me wisdom and might, and have now made **known** to me what we asked of you, for you have made known to us the king’s matter.” |
| Dan 2:23 | known | AVhp2ms | none recorded | - | 0 | To you, O God of my fathers, I give thanks and praise, for you have given me wisdom and might, and have now made **known** to me what we asked of you, for you have made known to us the king’s matter.” |
| Dan 2:28 | known | AVhp3ms | none recorded | - | 0 | but there is a God in heaven who reveals mysteries, and he has made **known** to King Nebuchadnezzar what will be in the latter days. Your dream and the visions of your head as you lay in bed are these: |
| Dan 2:29 | known | AVhp3ms | none recorded | 20482, 20559 | 0 | To you, O king, as you lay in bed came thoughts of what would be after this, and he who reveals mysteries made **known** to you what is to be. |
| Dan 2:30 | known | AVhi3mp | none recorded | 20482, 20559 | 0 | But as for me, this mystery has been revealed to me, not because of any wisdom that I have more than all the living, but in order that the interpretation may be made **known** to the king, and that you may know the thoughts of your mind. |
| Dan 2:45 | known | AVhp3ms | none recorded | - | 0 | just as you saw that a stone was cut from a mountain by no human hand, and that it broke in pieces the iron, the bronze, the clay, the silver, and the gold. A great God has made **known** to the king what shall be after this. The dream is certain, and its interpretation sure.” |
| Dan 3:18 | known | AVQrmsa | none recorded | - | 0 | But if not, be it **known** to you, O king, that we will not serve your gods or worship the golden image that you have set up.” |
| Dan 2:22 | knows | AVqrmsa | none recorded | - | 0 | he reveals deep and hidden things; he **knows** what is in the darkness, and the light dwells with him. |
| Ezr 4:15 | learn | AVqu2ms | none recorded | - | 0 | in order that search may be made in the book of the records of your fathers. You will find in the book of the records and **learn** that this city is a rebellious city, hurtful to kings and provinces, and that sedition was stirred up in it from of old. That was why this city was laid waste. |
| Dan 2:5 | make known | AVhi2mp | none recorded | - | 0 | The king answered and said to the Chaldeans, “The word from me is firm: if you do not **make known** to me the dream and its interpretation, you shall be torn limb from limb, and your houses shall be laid in ruins. |
| Dan 2:25 | make known | AVhi3ms | none recorded | - | 0 | Then Arioch brought in Daniel before the king in haste and said thus to him: “I have found among the exiles from Judah a man who will **make known** to the king the interpretation.” |
| Dan 2:26 | make known | AVhcc | none recorded | - | 0 | The king declared to Daniel, whose name was Belteshazzar, “ Are you able to **make known** to me the dream that I have seen and its interpretation?” |
| Dan 4:6 | make known | AVhi3mp | none recorded | - | 0 | So I made a decree that all the wise men of Babylon should be brought before me, that they might **make known** to me the interpretation of the dream. |
| Dan 4:7 | make known | AVhrmpa | none recorded | - | 0 | Then the magicians, the enchanters, the Chaldeans, and the astrologers came in, and I told them the dream, but they could not **make known** to me its interpretation. |
| Dan 4:18 | make known | AVhcc | none recorded | - | 0 | This dream I, King Nebuchadnezzar, saw. And you, O Belteshazzar, tell me the interpretation, because all the wise men of my kingdom are not able to **make known** to me the interpretation, but you are able, for the spirit of the holy gods is in you.” |
| Dan 5:8 | make known | AVhcc | none recorded | - | 0 | Then all the king’s wise men came in, but they could not read the writing or **make known** to the king the interpretation. |
| Dan 5:15 | make known | AVhcc | none recorded | - | 0 | Now the wise men, the enchanters, have been brought in before me to read this writing and **make known** to me its interpretation, but they could not show the interpretation of the matter. |
| Dan 5:16 | make known | AVhcc | none recorded | 19125 | 0 | But I have heard that you can give interpretations and solve problems. Now if you can read the writing and **make known** to me its interpretation, you shall be clothed with purple and have a chain of gold around your neck and shall be the third ruler in the kingdom.” |
| Dan 5:17 | make known | AVhi1cs | none recorded | 19125 | 0 | Then Daniel answered and said before the king, “Let your gifts be for yourself, and give your rewards to another. Nevertheless, I will read the writing to the king and **make known** to him the interpretation. |

### 3.7 G1108 γνῶσις gnōsis "knowledge": 28 own occurrences in 27 verses

- **Meaning as stored:** Greek; native word γνῶσις, transliteration gnōsis; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (high).
- **Counts, three measures as stored:** STEP token count 71; verses STEP attests 28; verse_lexical rows the parse found 29.

- **Carried by the member words:** knowledge (27), knowing (1).
- **Engagement of these occurrences:** none recorded 28.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Phili 3:8 | knowing | N-GSF | none recorded | - | 0 | Indeed, I count everything as loss because of the surpassing worth of **knowing** Christ Jesus my Lord. For his sake I have suffered the loss of all things and count them as rubbish, in order that I may gain Christ |
| Luk 1:77 | knowledge | N-ASF | none recorded | - | 0 | to give **knowledge** of salvation to his people in the forgiveness of their sins, |
| Luk 11:52 | knowledge | N-GSF | none recorded | - | 0 | Woe to you lawyers! For you have taken away the key of **knowledge**. You did not enter yourselves, and you hindered those who were entering.” |
| Rom 2:20 | knowledge | N-GSF | none recorded | - | 0 | an instructor of the foolish, a teacher of children, having in the law the embodiment of **knowledge** and truth — |
| Rom 11:33 | knowledge | N-GSF | none recorded | - | 0 | Oh, the depth of the riches and wisdom and **knowledge** of God! How unsearchable are his judgments and how inscrutable his ways! |
| Rom 15:14 | knowledge | N-GSF | none recorded | - | 0 | I myself am satisfied about you, my brothers, that you yourselves are full of goodness, filled with all **knowledge** and able to instruct one another. |
| 1Cor 1:5 | knowledge | N-DSF | none recorded | - | 0 | that in every way you were enriched in him in all speech and all **knowledge** — |
| 1Cor 8:1 | knowledge | N-ASF | none recorded | 15151, 15307 | 0 | Now concerning food offered to idols: we know that “ all of us possess **knowledge**.” This “ knowledge ” puffs up, but love builds up. |
| 1Cor 8:1 | knowledge | N-NSF | none recorded | - | 0 | Now concerning food offered to idols: we know that “ all of us possess **knowledge**.” This “ knowledge ” puffs up, but love builds up. |
| 1Cor 8:7 | knowledge | N-NSF | none recorded | 15962 | 0 | However, not all possess this **knowledge**. But some, through former association with idols, eat food as really offered to an idol, and their conscience, being weak, is defiled. |
| 1Cor 8:10 | knowledge | N-ASF | none recorded | 15962 | 0 | For if anyone sees you who have **knowledge** eating in an idol’s temple, will he not be encouraged, if his conscience is weak, to eat food offered to idols? |
| 1Cor 8:11 | knowledge | N-DSF | none recorded | 19060 | 0 | And so by your **knowledge** this weak person is destroyed, the brother for whom Christ died. |
| 1Cor 12:8 | knowledge | N-GSF | none recorded | 15957 | 0 | For to one is given through the Spirit the utterance of wisdom, and to another the utterance of **knowledge** according to the same Spirit, |
| 1Cor 13:2 | knowledge | N-ASF | none recorded | 15151 | 0 | And if I have prophetic powers, and understand all mysteries and all **knowledge**, and if I have all faith, so as to remove mountains, but have not love, I am nothing. |
| 1Cor 13:8 | knowledge | N-NSF | none recorded | - | 0 | Love never ends. As for prophecies, they will pass away; as for tongues, they will cease; as for **knowledge**, it will pass away. |
| 1Cor 14:6 | knowledge | N-DSF | none recorded | - | 0 | Now, brothers, if I come to you speaking in tongues, how will I benefit you unless I bring you some revelation or **knowledge** or prophecy or teaching? |
| 2Cor 2:14 | knowledge | N-GSF | none recorded | - | 0 | But thanks be to God, who in Christ always leads us in triumphal procession, and through us spreads the fragrance of the **knowledge** of him everywhere. |
| 2Cor 4:6 | knowledge | N-GSF | none recorded | 15941, 16301, 17242 | 0 | For God, who said, “Let light shine out of darkness,” has shone in our hearts to give the light of the **knowledge** of the glory of God in the face of Jesus Christ. |
| 2Cor 6:6 | knowledge | N-DSF | none recorded | - | 0 | by purity, **knowledge**, patience, kindness, the Holy Spirit, genuine love; |
| 2Cor 8:7 | knowledge | N-DSF | none recorded | - | 33 | But as you excel in everything —in faith, in speech, in **knowledge**, in all earnestness, and in our love for you — see that you excel in this act of grace also. |
| 2Cor 10:5 | knowledge | N-GSF | none recorded | 15154, 15243, 20569 | 0 | We destroy arguments and every lofty opinion raised against the **knowledge** of God, and take every thought captive to obey Christ, |
| 2Cor 11:6 | knowledge | N-DSF | none recorded | - | 0 | Even if I am unskilled in speaking, I am not so in **knowledge**; indeed, in every way we have made this plain to you in all things. |
| Eph 3:19 | knowledge | N-GSF | none recorded | - | 0 | and to know the love of Christ that surpasses **knowledge**, that you may be filled with all the fullness of God. |
| Col 2:3 | knowledge | N-GSF | none recorded | - | 0 | in whom are hidden all the treasures of wisdom and **knowledge**. |
| 1Ti 6:20 | knowledge | N-GSF | none recorded | - | 0 | O Timothy, guard the deposit entrusted to you. Avoid the irreverent babble and contradictions of what is falsely called “ **knowledge**,” |
| 2Pe 1:5 | knowledge | N-ASF | none recorded | 19504 | 32 | For this very reason, make every effort to supplement your faith with virtue, and virtue with **knowledge**, |
| 2Pe 1:6 | knowledge | N-DSF | none recorded | 19504 | 0 | and **knowledge** with self-control, and self-control with steadfastness, and steadfastness with godliness, |
| 2Pe 3:18 | knowledge | N-DSF | none recorded | - | 0 | But grow in the grace and **knowledge** of our Lord and Savior Jesus Christ. To him be the glory both now and to the day of eternity. Amen. |

### 3.8 G1492I εἴδω eidō "to perceive: know": 28 own occurrences in 26 verses

- **Meaning as stored:** Greek; native word εἴδω, transliteration eidō; STEP gloss "to perceive: know"; sense head "to perceive: know" (the code is its own lemma).
- **Related terms (29):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (medium).
- **Counts, three measures as stored:** STEP token count 365; verses STEP attests 27; verse_lexical rows the parse found 29.

- **Carried by the member words:** knew (14), know (12), known (2).
- **Engagement of these occurrences:** none recorded 28.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 25:26 | knew | V-2LAI-2S | none recorded | 12880, 13774, 19228 | 20 | But his master answered him, ‘You wicked and slothful servant! You **knew** that I reap where I have not sown and gather where I scattered no seed? |
| Mat 27:18 | knew | V-2LAI-3S | none recorded | - | 0 | For he **knew** that it was out of envy that they had delivered him up. |
| Mar 1:34 | knew | V-2LAI-3P | none recorded | - | 0 | And he healed many who were sick with various diseases, and cast out many demons. And he would not permit the demons to speak, because they **knew** him. |
| Luk 4:41 | knew | V-2LAI-3P | none recorded | - | 0 | And demons also came out of many, crying, “You are the Son of God!” But he rebuked them and would not allow them to speak, because they **knew** that he was the Christ. |
| Luk 6:8 | knew | V-2LAI-3S | none recorded | - | 0 | But he **knew** their thoughts, and he said to the man with the withered hand, “ Come and stand here.” And he rose and stood there. |
| Luk 19:22 | knew | V-2LAI-2S | none recorded | - | 0 | He said to him, ‘I will condemn you with your own words, you wicked servant! You **knew** that I was a severe man, taking what I did not deposit and reaping what I did not sow? |
| Joh 2:9 | knew | V-2LAI-3P | none recorded | - | 0 | When the master of the feast tasted the water now become wine, and did not know where it came from ( though the servants who had drawn the water **knew** ), the master of the feast called the bridegroom |
| Joh 4:10 | knew | V-2LAI-2S | none recorded | - | 0 | Jesus answered her, “ If you **knew** the gift of God, and who it is that is saying to you, ‘ Give me a drink,’ you would have asked him, and he would have given you living water.” |
| Joh 6:6 | knew | V-2LAI-3S | none recorded | - | 0 | He said this to test him, for he himself **knew** what he would do. |
| Joh 6:64 | knew | V-2LAI-3S | none recorded | - | 0 | But there are some of you who do not believe.” ( For Jesus **knew** from the beginning who those were who did not believe, and who it was who would betray him.) |
| Joh 8:19 | knew | V-2LAI-2P | none recorded | - | 0 | They said to him therefore, “ Where is your Father?” Jesus answered, “You know neither me nor my Father. If you **knew** me, you would know my Father also.” |
| Joh 13:11 | knew | V-2LAI-3S | none recorded | - | 0 | For he **knew** who was to betray him; that was why he said, “ Not all of you are clean.” |
| Joh 18:2 | knew | V-2LAI-3S | none recorded | - | 0 | Now Judas, who betrayed him, also **knew** the place, for Jesus often met there with his disciples. |
| Act 16:3 | knew | V-2LAI-3P | none recorded | - | 0 | Paul wanted Timothy to accompany him, and he took him and circumcised him because of the Jews who were in those places, for they all **knew** that his father was a Greek. |
| Mar 9:6 | know | V-2LAI-3S | none recorded | - | 0 | For he did not **know** what to say, for they were terrified. |
| Mar 14:40 | know | V-2LAI-3P | none recorded | - | 0 | And again he came and found them sleeping, for their eyes were very heavy, and they did not **know** what to answer him. |
| Luk 2:49 | know | V-2LAI-2P | none recorded | 15507 | 0 | And he said to them, “ Why were you looking for me? Did you not **know** that I must be in my Father’s house?” |
| Joh 2:9 | know | V-2LAI-3S | none recorded | - | 0 | When the master of the feast tasted the water now become wine, and did not **know** where it came from ( though the servants who had drawn the water knew ), the master of the feast called the bridegroom |
| Joh 5:13 | know | V-2LAI-3S | none recorded | - | 0 | Now the man who had been healed did not **know** who it was, for Jesus had withdrawn, as there was a crowd in the place. |
| Joh 8:19 | know | V-2LAI-2P | none recorded | - | 0 | They said to him therefore, “ Where is your Father?” Jesus answered, “You **know** neither me nor my Father. If you knew me, you would know my Father also.” |
| Joh 20:14 | know | V-2LAI-3S | none recorded | - | 0 | Having said this, she turned around and saw Jesus standing, but she did not **know** that it was Jesus. |
| Joh 21:4 | know | V-2LAI-3P | none recorded | - | 0 | Just as day was breaking, Jesus stood on the shore; yet the disciples did not **know** that it was Jesus. |
| Act 7:18 | know | V-2LAI-3S | none recorded | - | 0 | until there arose over Egypt another king who did not **know** Joseph. |
| Act 12:9 | know | V-2LAI-3S | none recorded | - | 0 | And he went out and followed him. He did not **know** that what was being done by the angel was real, but thought he was seeing a vision. |
| Act 19:32 | know | V-2LAI-3P | none recorded | - | 0 | Now some cried out one thing, some another, for the assembly was in confusion, and most of them did not **know** why they had come together. |
| Heb 8:11 | know | V-FAI-3P | none recorded | - | 0 | And they shall not teach, each one his neighbor and each one his brother, saying, ‘ **Know** the Lord,’ for they shall all know me, from the least of them to the greatest. |
| Mat 24:43 | known | V-2LAI-3S | none recorded | - | 0 | But know this, that if the master of the house had **known** in what part of the night the thief was coming, he would have stayed awake and would not have let his house be broken into. |
| Luk 12:39 | known | V-2LAI-3S | none recorded | - | 0 | But know this, that if the master of the house had **known** at what hour the thief was coming, he would not have left his house to be broken into. |

### 3.9 G3129 μανθάνω manthanō "to learn": 23 own occurrences in 22 verses

- **Meaning as stored:** Greek; native word μανθάνω, transliteration manthanō; STEP gloss "to learn"; sense head "to learn" (the code is its own lemma).
- **Related terms (2):** G0261 amathēs "ignorant"; G3101 mathētēs "disciple".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 60; verses STEP attests 24; verse_lexical rows the parse found 25.

- **Carried by the member words:** learn (12), learned (9), learning (1), studied (1).
- **Engagement of these occurrences:** none recorded 23.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 9:13 | learn | V-2AAM-2P | none recorded | - | 0 | Go and **learn** what this means: ‘I desire mercy, and not sacrifice.’ For I came not to call the righteous, but sinners.” |
| Mat 11:29 | learn | V-2AAM-2P | none recorded | - | 0 | Take my yoke upon you, and **learn** from me, for I am gentle and lowly in heart, and you will find rest for your souls. |
| Mat 24:32 | learn | V-2AAM-2P | none recorded | - | 0 | “ From the fig tree **learn** its lesson: as soon as its branch becomes tender and puts out its leaves, you know that summer is near. |
| Mar 13:28 | learn | V-2AAM-2P | none recorded | - | 0 | “ From the fig tree **learn** its lesson: as soon as its branch becomes tender and puts out its leaves, you know that summer is near. |
| 1Cor 4:6 | learn | V-2AAS-2P | none recorded | - | 0 | I have applied all these things to myself and Apollos for your benefit, brothers, that you may **learn** by us not to go beyond what is written, that none of you may be puffed up in favor of one against another. |
| 1Cor 14:31 | learn | V-PAS-3P | none recorded | - | 0 | For you can all prophesy one by one, so that all may **learn** and all be encouraged, |
| 1Cor 14:35 | learn | V-2AAN | none recorded | - | 0 | If there is anything they desire to **learn**, let them ask their husbands at home. For it is shameful for a woman to speak in church. |
| 1Ti 2:11 | learn | V-PAM-3S | none recorded | - | 0 | Let a woman **learn** quietly with all submissiveness. |
| 1Ti 5:4 | learn | V-PAM-3P | none recorded | - | 0 | But if a widow has children or grandchildren, let them first **learn** to show godliness to their own household and to make some return to their parents, for this is pleasing in the sight of God. |
| 1Ti 5:13 | learn | V-PAI-3P | none recorded | - | 1 | Besides that, they **learn** to be idlers, going about from house to house, and not only idlers, but also gossips and busybodies, saying what they should not. |
| Tit 3:14 | learn | V-PAM-3P | none recorded | - | 0 | And let our people **learn** to devote themselves to good works, so as to help cases of urgent need, and not be unfruitful. |
| Rev 14:3 | learn | V-2AAN | none recorded | - | 0 | and they were singing a new song before the throne and before the four living creatures and before the elders. No one could **learn** that song except the 144,000 who had been redeemed from the earth. |
| Joh 6:45 | learned | V-2AAP-NSM | none recorded | - | 0 | It is written in the Prophets, ‘ And they will all be taught by God.’ Everyone who has heard and **learned** from the Father comes to me — |
| Act 23:27 | learned | V-2AAP-NSM | none recorded | - | 0 | This man was seized by the Jews and was about to be killed by them when I came upon them with the soldiers and rescued him, having **learned** that he was a Roman citizen. |
| Eph 4:20 | learned | V-2AAI-2P | none recorded | - | 0 | But that is not the way you **learned** Christ!— |
| Phili 4:9 | learned | V-2AAI-2P | none recorded | - | 0 | What you have **learned** and received and heard and seen in me — practice these things, and the God of peace will be with you. |
| Phili 4:11 | learned | V-2AAI-1S | none recorded | - | 0 | Not that I am speaking of being in need, for I have **learned**, in whatever situation I am, to be content. |
| Col 1:7 | learned | V-2AAI-2P | none recorded | - | 0 | just as you **learned** it from Epaphras our beloved fellow servant. He is a faithful minister of Christ on your behalf |
| 2Ti 3:14 | learned | V-2AAI-2S | none recorded | - | 0 | But as for you, continue in what you have **learned** and have firmly believed, knowing from whom you learned it |
| 2Ti 3:14 | learned | V-2AAI-2S | none recorded | - | 0 | But as for you, continue in what you have **learned** and have firmly believed, knowing from whom you learned it |
| Heb 5:8 | learned | V-2AAI-3S | none recorded | - | 0 | Although he was a son, he **learned** obedience through what he suffered. |
| 2Ti 3:7 | learning | V-PAP-APN | none recorded | - | 0 | always **learning** and never able to arrive at a knowledge of the truth. |
| Joh 7:15 | studied | V-RAP-NSM | none recorded | - | 0 | The Jews therefore marveled, saying, “ How is it that this man has learning, when he has never **studied**?” |

### 3.10 G1921 ἐπιγινώσκω epiginōskō "to come to know": 20 own occurrences in 18 verses

- **Meaning as stored:** Greek; native word ἐπιγινώσκω, transliteration epiginōskō; STEP gloss "to come to know"; sense head "to come to know" (the code is its own lemma).
- **Related terms (24):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 136; verses STEP attests 39; verse_lexical rows the parse found 43.

- **Carried by the member words:** learned (4), recognize (4), know (3), known (3), knows (2), realized (2), knowing (1), perceived (1).
- **Engagement of these occurrences:** none recorded 20.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 25:10 | know | V-PAI-2S | none recorded | - | 0 | But Paul said, “I am standing before Caesar’s tribunal, where I ought to be tried. To the Jews I have done no wrong, as you yourself **know** very well. |
| Rom 1:32 | know | V-2AAP-NPM | none recorded | - | 0 | Though they **know** God’s righteous decree that those who practice such things deserve to die, they not only do them but give approval to those who practice them. |
| 1Ti 4:3 | know | V-RAP-DPM | none recorded | - | 0 | who forbid marriage and require abstinence from foods that God created to be received with thanksgiving by those who believe and **know** the truth. |
| 2Pe 2:21 | knowing | V-2AAP-DPM | none recorded | - | 0 | For it would have been better for them never to have known the way of righteousness than after **knowing** it to turn back from the holy commandment delivered to them. |
| 1Cor 13:12 | known | V-2API-1S | none recorded | - | 0 | For now we see in a mirror dimly, but then face to face. Now I know in part; then I shall know fully, even as I have been fully **known**. |
| 2Cor 6:9 | known | V-PPP-NPM | none recorded | - | 0 | as unknown, and yet well **known**; as dying, and behold, we live; as punished, and yet not killed; |
| 2Pe 2:21 | known | V-RAN | none recorded | - | 0 | For it would have been better for them never to have **known** the way of righteousness than after knowing it to turn back from the holy commandment delivered to them. |
| Mat 11:27 | knows | V-PAI-3S | none recorded | - | 0 | All things have been handed over to me by my Father, and no one **knows** the Son except the Father, and no one knows the Father except the Son and anyone to whom the Son chooses to reveal him. |
| Mat 11:27 | knows | V-PAI-3S | none recorded | - | 0 | All things have been handed over to me by my Father, and no one **knows** the Son except the Father, and no one knows the Father except the Son and anyone to whom the Son chooses to reveal him. |
| Luk 7:37 | learned | V-2AAP-NSF | none recorded | - | 0 | And behold, a woman of the city, who was a sinner, when she **learned** that he was reclining at table in the Pharisee’s house, brought an alabaster flask of ointment, |
| Luk 23:7 | learned | V-2AAP-NSM | none recorded | - | 0 | And when he **learned** that he belonged to Herod’s jurisdiction, he sent him over to Herod, who was himself in Jerusalem at that time. |
| Act 9:30 | learned | V-2AAP-NPM | none recorded | - | 0 | And when the brothers **learned** this, they brought him down to Caesarea and sent him off to Tarsus. |
| Act 28:1 | learned | V-2AAI-1P | none recorded | - | 0 | After we were brought safely through, we then **learned** that the island was called Malta. |
| Luk 5:22 | perceived | V-2AAP-NSM | none recorded | - | 0 | When Jesus **perceived** their thoughts, he answered them, “ Why do you question in your hearts? |
| Luk 1:22 | realized | V-2AAI-3P | none recorded | - | 0 | And when he came out, he was unable to speak to them, and they **realized** that he had seen a vision in the temple. And he kept making signs to them and remained mute. |
| Act 22:29 | realized | V-2AAP-NSM | none recorded | - | 0 | So those who were about to examine him withdrew from him immediately, and the tribune also was afraid, for he **realized** that Paul was a Roman citizen and that he had bound him. |
| Mat 7:16 | recognize | V-FDI-2P | none recorded | - | 0 | You will **recognize** them by their fruits. Are grapes gathered from thornbushes, or figs from thistles? |
| Mat 7:20 | recognize | V-FDI-2P | none recorded | - | 0 | Thus you will **recognize** them by their fruits. |
| Mat 17:12 | recognize | V-2AAI-3P | none recorded | - | 0 | But I tell you that Elijah has already come, and they did not **recognize** him, but did to him whatever they pleased. So also the Son of Man will certainly suffer at their hands.” |
| Act 27:39 | recognize | V-IAI-3P | none recorded | - | 0 | Now when it was day, they did not **recognize** the land, but they noticed a bay with a beach, on which they planned if possible to run the ship ashore. |

### 3.11 G1922 ἐπίγνωσις epignōsis "knowledge": 19 own occurrences in 19 verses

- **Meaning as stored:** Greek; native word ἐπίγνωσις, transliteration epignōsis; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (high).
- **Counts, three measures as stored:** STEP token count 25; verses STEP attests 20; verse_lexical rows the parse found 20.

- **Carried by the member words:** knowledge (19).
- **Engagement of these occurrences:** none recorded 19.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 3:20 | knowledge | N-NSF | none recorded | - | 0 | For by works of the law no human being will be justified in his sight, since through the law comes **knowledge** of sin. |
| Rom 10:2 | knowledge | N-ASF | none recorded | 17748 | 0 | For I bear them witness that they have a zeal for God, but not according to **knowledge**. |
| Eph 1:17 | knowledge | N-DSF | none recorded | - | 0 | that the God of our Lord Jesus Christ, the Father of glory, may give you the Spirit of wisdom and of revelation in the **knowledge** of him, |
| Eph 4:13 | knowledge | N-GSF | none recorded | - | 0 | until we all attain to the unity of the faith and of the **knowledge** of the Son of God, to mature manhood, to the measure of the stature of the fullness of Christ, |
| Phili 1:9 | knowledge | N-DSF | none recorded | - | 0 | And it is my prayer that your love may abound more and more, with **knowledge** and all discernment, |
| Col 1:9 | knowledge | N-ASF | none recorded | - | 0 | And so, from the day we heard, we have not ceased to pray for you, asking that you may be filled with the **knowledge** of his will in all spiritual wisdom and understanding, |
| Col 1:10 | knowledge | N-DSF | none recorded | - | 0 | so as to walk in a manner worthy of the Lord, fully pleasing to him: bearing fruit in every good work and increasing in the **knowledge** of God; |
| Col 2:2 | knowledge | N-ASF | none recorded | - | 0 | that their hearts may be encouraged, being knit together in love, to reach all the riches of full assurance of understanding and the **knowledge** of God’s mystery, which is Christ, |
| Col 3:10 | knowledge | N-ASF | none recorded | 14309 | 0 | and have put on the new self, which is being renewed in **knowledge** after the image of its creator. |
| 1Ti 2:4 | knowledge | N-ASF | none recorded | - | 0 | who desires all people to be saved and to come to the **knowledge** of the truth. |
| 2Ti 2:25 | knowledge | N-ASF | none recorded | - | 0 | correcting his opponents with gentleness. God may perhaps grant them repentance leading to a **knowledge** of the truth, |
| 2Ti 3:7 | knowledge | N-ASF | none recorded | 17417 | 0 | always learning and never able to arrive at a **knowledge** of the truth. |
| Tit 1:1 | knowledge | N-ASF | none recorded | 19506, 19539, 19718, 20240 | 0 | Paul, a servant of God and an apostle of Jesus Christ, for the sake of the faith of God’s elect and their **knowledge** of the truth, which accords with godliness, |
| Phile 6 | knowledge | N-DSF | none recorded | - | 0 | and I pray that the sharing of your faith may become effective for the full **knowledge** of every good thing that is in us for the sake of Christ. |
| Heb 10:26 | knowledge | N-ASF | none recorded | - | 0 | For if we go on sinning deliberately after receiving the **knowledge** of the truth, there no longer remains a sacrifice for sins, |
| 2Pe 1:2 | knowledge | N-DSF | none recorded | - | 0 | May grace and peace be multiplied to you in the **knowledge** of God and of Jesus our Lord. |
| 2Pe 1:3 | knowledge | N-GSF | none recorded | 19504 | 0 | His divine power has granted to us all things that pertain to life and godliness, through the **knowledge** of him who called us to his own glory and excellence, |
| 2Pe 1:8 | knowledge | N-ASF | none recorded | - | 32 | For if these qualities are yours and are increasing, they keep you from being ineffective or unfruitful in the **knowledge** of our Lord Jesus Christ. |
| 2Pe 2:20 | knowledge | N-DSF | none recorded | - | 0 | For if, after they have escaped the defilements of the world through the **knowledge** of our Lord and Savior Jesus Christ, they are again entangled in them and overcome, the last state has become worse for them than the first. |

### 3.12 H3925H לָמַד la.mad "to learn: learn": 18 own occurrences in 18 verses

- **Meaning as stored:** Hebrew; native word לָמַד, transliteration la.mad; STEP gloss "to learn: learn"; sense head "learn".
- **Senses (first level of the meaning tree of the lemma H3925):** to learn. teach, exercise in.
- **Related terms (7):** H3925G la.mad "to learn: teach"; H3927 le.mu.el "Lemuel"; H3928 lim.mud "disciple"; H3929G le.mekh "Lamech"; H3929H le.mekh "Lamech"; H4451 mal.med "oxgoad"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 23; verses STEP attests 22; verse_lexical rows the parse found 23.

- **Carried by the member words:** learn (16), learned (2).
- **Engagement of these occurrences:** none recorded 18.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 4:10 | learn | HVqi3mp | none recorded | - | 0 | how on the day that you stood before the Lord your God at Horeb, the Lord said to me, ‘ Gather the people to me, that I may let them hear my words, so that they may **learn** to fear me all the days that they live on the earth, and that they may teach their children so.’ |
| Deu 5:1 | learn | HVqq2mp | none recorded | - | 0 | And Moses summoned all Israel and said to them, “ Hear, O Israel, the statutes and the rules that I speak in your hearing today, and you shall **learn** them and be careful to do them. |
| Deu 14:23 | learn | HVqj2ms | none recorded | - | 0 | And before the Lord your God, in the place that he will choose, to make his name dwell there, you shall eat the tithe of your grain, of your wine, and of your oil, and the firstborn of your herd and flock, that you may **learn** to fear the Lord your God always. |
| Deu 17:19 | learn | HVqj3ms | none recorded | - | 0 | And it shall be with him, and he shall read in it all the days of his life, that he may **learn** to fear the Lord his God by keeping all the words of this law and these statutes, and doing them, |
| Deu 18:9 | learn | HVqi2ms | none recorded | - | 0 | “When you come into the land that the Lord your God is giving you, you shall not **learn** to follow the abominable practices of those nations. |
| Deu 31:12 | learn | HVqj3mp | none recorded | - | 0 | Assemble the people, men, women, and little ones, and the sojourner within your towns, that they may hear and **learn** to fear the Lord your God, and be careful to do all the words of this law, |
| Deu 31:13 | learn | HVqq3cp | none recorded | - | 0 | and that their children, who have not known it, may hear and **learn** to fear the Lord your God, as long as you live in the land that you are going over the Jordan to possess.” |
| Psa 119:7 | learn | HVqcc | none recorded | - | 0 | I will praise you with an upright heart, when I **learn** your righteous rules. |
| Psa 119:71 | learn | HVqj1cs | none recorded | - | 0 | It is good for me that I was afflicted, that I might **learn** your statutes. |
| Psa 119:73 | learn | HVqc1cs | none recorded | - | 0 | Yodh Your hands have made and fashioned me; give me understanding that I may **learn** your commandments. |
| Isa 1:17 | learn | HVqv2mp | none recorded | - | 0 | **learn** to do good; seek justice, correct oppression; bring justice to the fatherless, plead the widow’s cause. |
| Isa 2:4 | learn | HVqi3mp | none recorded | - | 0 | He shall judge between the nations, and shall decide disputes for many peoples; and they shall beat their swords into plowshares, and their spears into pruning hooks; nation shall not lift up sword against nation, neither shall they **learn** war anymore. |
| Isa 26:9 | learn | HVqp3cp | none recorded | - | 0 | My soul yearns for you in the night; my spirit within me earnestly seeks you. For when your judgments are in the earth, the inhabitants of the world **learn** righteousness. |
| Isa 26:10 | learn | HVqp3ms | none recorded | - | 0 | If favor is shown to the wicked, he does not **learn** righteousness; in the land of uprightness he deals corruptly and does not see the majesty of the Lord. |
| Jer 10:2 | learn | HVqj2mp | none recorded | - | 0 | Thus says the Lord: “ **Learn** not the way of the nations, nor be dismayed at the signs of the heavens because the nations are dismayed at them, |
| Mic 4:3 | learn | HVqi3mp | none recorded | - | 0 | He shall judge between many peoples, and shall decide disputes for strong nations far away; and they shall beat their swords into plowshares, and their spears into pruning hooks; nation shall not lift up sword against nation, neither shall they **learn** war anymore; |
| Psa 106:35 | learned | HVqw3mp | none recorded | - | 0 | but they mixed with the nations and **learned** to do as they did. |
| Pro 30:3 | learned | HVqp1cs | none recorded | - | 0 | I have not **learned** wisdom, nor have I knowledge of the Holy One. |

### 3.13 H7200G רָאָה ra.ah "to see: see": 17 own occurrences in 17 verses

- **Meaning as stored:** Hebrew; native word רָאָה, transliteration ra.ah; STEP gloss "to see: see"; sense head "see/show".
- **Senses (first level of the meaning tree of the lemma H7200):** to see, look at, inspect, perceive, consider.
- **Related terms (26):** H3070 yir.eh "Provider [God]"; H3376 yir.iy.yah "Irijah"; H4758 mar.eh "appearance"; H4759A mar.ah "vision"; H4759B mar.ah "mirror"; H7200H ra.ah "to see: examine"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 1223; verses STEP attests 1107; verse_lexical rows the parse found 1199.

- **Carried by the member words:** examine (17).
- **Engagement of these occurrences:** none recorded 17.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lev 13:3 | examine | HVqq3ms | none recorded | - | 0 | and the priest shall **examine** the diseased area on the skin of his body. And if the hair in the diseased area has turned white and the disease appears to be deeper than the skin of his body, it is a case of leprous disease. When the priest has examined him, he shall pronounce him unclean. |
| Lev 13:5 | examine | HVqq3ms | none recorded | - | 0 | And the priest shall **examine** him on the seventh day, and if in his eyes the disease is checked and the disease has not spread in the skin, then the priest shall shut him up for another seven days. |
| Lev 13:6 | examine | HVqq3ms | none recorded | - | 0 | And the priest shall **examine** him again on the seventh day, and if the diseased area has faded and the disease has not spread in the skin, then the priest shall pronounce him clean; it is only an eruption. And he shall wash his clothes and be clean. |
| Lev 13:15 | examine | HVqq3ms | none recorded | - | 0 | And the priest shall **examine** the raw flesh and pronounce him unclean. Raw flesh is unclean, for it is a leprous disease. |
| Lev 13:17 | examine | HVqq3ms | none recorded | - | 0 | and the priest shall **examine** him, and if the disease has turned white, then the priest shall pronounce the diseased person clean; he is clean. |
| Lev 13:25 | examine | HVqq3ms | none recorded | - | 0 | the priest shall **examine** it, and if the hair in the spot has turned white and it appears deeper than the skin, then it is a leprous disease. It has broken out in the burn, and the priest shall pronounce him unclean; it is a case of leprous disease. |
| Lev 13:27 | examine | HVqq3ms | none recorded | - | 0 | and the priest shall **examine** him the seventh day. If it is spreading in the skin, then the priest shall pronounce him unclean; it is a case of leprous disease. |
| Lev 13:30 | examine | HVqq3ms | none recorded | - | 0 | the priest shall **examine** the disease. And if it appears deeper than the skin, and the hair in it is yellow and thin, then the priest shall pronounce him unclean. It is an itch, a leprous disease of the head or the beard. |
| Lev 13:32 | examine | HVqq3ms | none recorded | - | 0 | and on the seventh day the priest shall **examine** the disease. If the itch has not spread, and there is in it no yellow hair, and the itch appears to be no deeper than the skin, |
| Lev 13:34 | examine | HVqq3ms | none recorded | - | 0 | And on the seventh day the priest shall **examine** the itch, and if the itch has not spread in the skin and it appears to be no deeper than the skin, then the priest shall pronounce him clean. And he shall wash his clothes and be clean. |
| Lev 13:36 | examine | HVqq3ms | none recorded | - | 0 | then the priest shall **examine** him, and if the itch has spread in the skin, the priest need not seek for the yellow hair; he is unclean. |
| Lev 13:43 | examine | HVqq3ms | none recorded | - | 0 | Then the priest shall **examine** him, and if the diseased swelling is reddish-white on his bald head or on his bald forehead, like the appearance of leprous disease in the skin of the body, |
| Lev 13:50 | examine | HVqq3ms | none recorded | - | 0 | And the priest shall **examine** the disease and shut up that which has the disease for seven days. |
| Lev 13:51 | examine | HVqq3ms | none recorded | - | 0 | Then he shall **examine** the disease on the seventh day. If the disease has spread in the garment, in the warp or the woof, or in the skin, whatever be the use of the skin, the disease is a persistent leprous disease; it is unclean. |
| Lev 13:55 | examine | HVqq3ms | none recorded | - | 0 | And the priest shall **examine** the diseased thing after it has been washed. And if the appearance of the diseased area has not changed, though the disease has not spread, it is unclean. You shall burn it in the fire, whether the rot is on the back or on the front. |
| Lev 14:36 | examine | HVqcc | none recorded | - | 0 | Then the priest shall command that they empty the house before the priest goes to **examine** the disease, lest all that is in the house be declared unclean. And afterward the priest shall go in to see the house. |
| Lev 14:37 | examine | HVqq3ms | none recorded | - | 0 | And he shall **examine** the disease. And if the disease is in the walls of the house with greenish or reddish spots, and if it appears to be deeper than the surface, |

### 3.14 G1107 γνωρίζω gnōrizō "to make known": 16 own occurrences in 16 verses

- **Meaning as stored:** Greek; native word γνωρίζω, transliteration gnōrizō; STEP gloss "to make known"; sense head "to make known" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 90; verses STEP attests 23; verse_lexical rows the parse found 24.

- **Carried by the member words:** made known (10), known (4), know (2).
- **Engagement of these occurrences:** none recorded 16.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 8:1 | know | V-PAI-1P | none recorded | - | 0 | We want you to **know**, brothers, about the grace of God that has been given among the churches of Macedonia, |
| Gal 1:11 | know | V-PAI-1S | none recorded | - | 0 | For I would have you **know**, brothers, that the gospel that was preached by me is not man’s gospel. |
| Rom 9:22 | known | V-AAN | none recorded | - | 0 | What if God, desiring to show his wrath and to make **known** his power, has endured with much patience vessels of wrath prepared for destruction, |
| Rom 9:23 | known | V-AAS-3S | none recorded | - | 0 | in order to make **known** the riches of his glory for vessels of mercy, which he has prepared beforehand for glory — |
| Eph 1:9 | known | V-AAP-NSM | none recorded | - | 0 | making **known** to us the mystery of his will, according to his purpose, which he set forth in Christ |
| Col 1:27 | known | V-AAN | none recorded | - | 0 | To them God chose to make **known** how great among the Gentiles are the riches of the glory of this mystery, which is Christ in you, the hope of glory. |
| Luk 2:15 | made known | V-AAI-3S | none recorded | - | 0 | When the angels went away from them into heaven, the shepherds said to one another, “ Let us go over to Bethlehem and see this thing that has happened, which the Lord has **made known** to us.” |
| Joh 15:15 | made known | V-AAI-1S | none recorded | - | 0 | No longer do I call you servants, for the servant does not know what his master is doing; but I have called you friends, for all that I have heard from my Father I have **made known** to you. |
| Joh 17:26 | made known | V-AAI-1S | none recorded | - | 0 | I **made known** to them your name, and I will continue to make it known, that the love with which you have loved me may be in them, and I in them.” |
| Act 2:28 | made known | V-AAI-2S | none recorded | - | 0 | You have **made known** to me the paths of life; you will make me full of gladness with your presence.’ |
| Rom 16:26 | made known | V-APP-GSN | none recorded | - | 0 | but has now been disclosed and through the prophetic writings has been **made known** to all nations, according to the command of the eternal God, to bring about the obedience of faith — |
| Eph 3:3 | made known | V-API-3S | none recorded | - | 0 | how the mystery was **made known** to me by revelation, as I have written briefly. |
| Eph 3:5 | made known | V-API-3S | none recorded | - | 0 | which was not **made known** to the sons of men in other generations as it has now been revealed to his holy apostles and prophets by the Spirit. |
| Eph 3:10 | made known | V-APS-3S | none recorded | - | 0 | so that through the church the manifold wisdom of God might now be **made known** to the rulers and authorities in the heavenly places. |
| Phili 4:6 | made known | V-PPM-3S | none recorded | - | 0 | do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be **made known** to God. |
| 2Pe 1:16 | made known | V-AAI-1P | none recorded | - | 0 | For we did not follow cleverly devised myths when we **made known** to you the power and coming of our Lord Jesus Christ, but we were eyewitnesses of his majesty. |

### 3.15 G1110 γνωστός, γνώριμος gnōstos gnōrimos "acquainted with": 12 own occurrences in 12 verses

- **Meaning as stored:** Greek; native word γνωστός, γνώριμος, transliteration gnōstos gnōrimos; STEP gloss "acquainted with"; sense head "acquainted with" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 31; verses STEP attests 15; verse_lexical rows the parse found 15.

- **Carried by the member words:** known (11), know (1).
- **Engagement of these occurrences:** none recorded 12.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 28:22 | know | A-NSN | none recorded | - | 0 | But we desire to hear from you what your views are, for with regard to this sect we **know** that everywhere it is spoken against.” |
| Joh 18:15 | known | A-NSM | none recorded | - | 0 | Simon Peter followed Jesus, and so did another disciple. Since that disciple was **known** to the high priest, he entered with Jesus into the courtyard of the high priest, |
| Joh 18:16 | known | A-NSM | none recorded | - | 0 | but Peter stood outside at the door. So the other disciple, who was **known** to the high priest, went out and spoke to the servant girl who kept watch at the door, and brought Peter in. |
| Act 1:19 | known | A-NSN | none recorded | - | 0 | And it became **known** to all the inhabitants of Jerusalem, so that the field was called in their own language Akeldama, that is, Field of Blood.) |
| Act 2:14 | known | A-NSN | none recorded | - | 0 | But Peter, standing with the eleven, lifted up his voice and addressed them: “ Men of Judea and all who dwell in Jerusalem, let this be **known** to you, and give ear to my words. |
| Act 4:10 | known | A-NSN | none recorded | - | 0 | let it be **known** to all of you and to all the people of Israel that by the name of Jesus Christ of Nazareth, whom you crucified, whom God raised from the dead — by him this man is standing before you well. |
| Act 9:42 | known | A-NSN | none recorded | - | 0 | And it became **known** throughout all Joppa, and many believed in the Lord. |
| Act 13:38 | known | A-NSN | none recorded | - | 0 | Let it be **known** to you therefore, brothers, that through this man forgiveness of sins is proclaimed to you, |
| Act 15:18 | known | A-APN | none recorded | - | 0 | **known** from of old.’ |
| Act 19:17 | known | A-NSN | none recorded | - | 0 | And this became **known** to all the residents of Ephesus, both Jews and Greeks. And fear fell upon them all, and the name of the Lord Jesus was extolled. |
| Act 28:28 | known | A-NSN | none recorded | - | 0 | Therefore let it be **known** to you that this salvation of God has been sent to the Gentiles; they will listen.” |
| Rom 1:19 | known | A-NSN | none recorded | - | 0 | For what can be **known** about God is plain to them, because God has shown it to them. |

### 3.16 G0050 ἀγνοέω agnoeō "be ignorant": 11 own occurrences in 10 verses

- **Meaning as stored:** Greek; native word ἀγνοέω, transliteration agnoeō; STEP gloss "be ignorant"; sense head "be ignorant" (the code is its own lemma).
- **Related terms (25):** G0051 agnoēma "error"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 30; verses STEP attests 21; verse_lexical rows the parse found 22.

- **Carried by the member words:** ignorant (4), not know (2), not recognize (2), ignorantly (1), not knowing (1), not recognized (1).
- **Engagement of these occurrences:** none recorded 11.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 10:3 | ignorant | V-PAP-NPM | none recorded | - | 0 | For, being **ignorant** of the righteousness of God, and seeking to establish their own, they did not submit to God’s righteousness. |
| 2Cor 2:11 | ignorant | V-PAI-1P | none recorded | - | 0 | so that we would not be outwitted by Satan; for we are not **ignorant** of his designs. |
| Heb 5:2 | ignorant | V-PAP-DPM | none recorded | - | 0 | He can deal gently with the **ignorant** and wayward, since he himself is beset with weakness. |
| 2Pe 2:12 | ignorant | V-PAI-3P | none recorded | - | 0 | But these, like irrational animals, creatures of instinct, born to be caught and destroyed, blaspheming about matters of which they are **ignorant**, will also be destroyed in their destruction, |
| 1Ti 1:13 | ignorantly | V-PAP-NSM | none recorded | - | 0 | though formerly I was a blasphemer, persecutor, and insolent opponent. But I received mercy because I had acted **ignorantly** in unbelief, |
| Rom 6:3 | not know | V-PAI-2P | none recorded | - | 0 | Do you **not know** that all of us who have been baptized into Christ Jesus were baptized into his death? |
| Rom 7:1 | not know | V-PAI-2P | none recorded | - | 0 | Or do you **not know**, brothers — for I am speaking to those who know the law — that the law is binding on a person only as long as he lives? |
| Rom 2:4 | not knowing | V-PAP-NSM | none recorded | 14780 | 0 | Or do you presume on the riches of his kindness and forbearance and patience, **not knowing** that God’s kindness is meant to lead you to repentance? |
| Act 13:27 | not recognize | V-AAP-NPM | none recorded | - | 0 | For those who live in Jerusalem and their rulers, because they did **not recognize** him nor understand the utterances of the prophets, which are read every Sabbath, fulfilled them by condemning him. |
| 1Cor 14:38 | not recognize | V-PAI-3S | none recorded | - | 0 | If anyone does **not recognize** this, he is not recognized. |
| 1Cor 14:38 | not recognized | V-PPI-3S | none recorded | - | 0 | If anyone does not recognize this, he is **not recognized**. |

### 3.17 G1987 ἐπίσταμαι epistamai "to know/understand": 11 own occurrences in 11 verses

- **Meaning as stored:** Greek; native word ἐπίσταμαι, transliteration epistamai; STEP gloss "to know/understand"; sense head "to know/understand" (the code is its own lemma).
- **Related terms (2):** G1990 epistēmōn "knowing"; G2186 efistēmi "to approach".
- **Clusters (cluster_strong):** M15 Knowing & Understanding (medium).
- **Counts, three measures as stored:** STEP token count 72; verses STEP attests 14; verse_lexical rows the parse found 14.

- **Carried by the member words:** know (6), knowing (2), knew (1), knows (1), recognize (1).
- **Engagement of these occurrences:** none recorded 11.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 18:25 | knew | V-PNP-NSM | none recorded | - | 0 | He had been instructed in the way of the Lord. And being fervent in spirit, he spoke and taught accurately the things concerning Jesus, though he **knew** only the baptism of John. |
| Act 10:28 | know | V-PNI-2P | none recorded | - | 0 | And he said to them, “You yourselves **know** how unlawful it is for a Jew to associate with or to visit anyone of another nation, but God has shown me that I should not call any person common or unclean. |
| Act 15:7 | know | V-PNI-2P | none recorded | 19683, 19953, 20294, 20297 | 0 | And after there had been much debate, Peter stood up and said to them, “ Brothers, you **know** that in the early days God made a choice among you, that by my mouth the Gentiles should hear the word of the gospel and believe. |
| Act 19:25 | know | V-PNI-2P | none recorded | - | 0 | These he gathered together, with the workmen in similar trades, and said, “ Men, you **know** that from this business we have our wealth. |
| Act 20:18 | know | V-PNI-2P | none recorded | - | 0 | And when they came to him, he said to them: “You yourselves **know** how I lived among you the whole time from the first day that I set foot in Asia, |
| Act 22:19 | know | V-PNI-3P | none recorded | - | 0 | And I said, ‘ Lord, they themselves **know** that in one synagogue after another I imprisoned and beat those who believed in you. |
| Jam 4:14 | know | V-PNI-2P | none recorded | 15167 | 0 | yet you do not **know** what tomorrow will bring. What is your life? For you are a mist that appears for a little time and then vanishes. |
| Act 24:10 | knowing | V-PNP-NSM | none recorded | - | 0 | And when the governor had nodded to him to speak, Paul replied: “ **Knowing** that for many years you have been a judge over this nation, I cheerfully make my defense. |
| Heb 11:8 | knowing | V-PNP-NSM | none recorded | - | 0 | By faith Abraham obeyed when he was called to go out to a place that he was to receive as an inheritance. And he went out, not **knowing** where he was going. |
| Act 26:26 | knows | V-PNI-3S | none recorded | - | 0 | For the king **knows** about these things, and to him I speak boldly. For I am persuaded that none of these things has escaped his notice, for this has not been done in a corner. |
| Act 19:15 | recognize | V-PNI-1S | none recorded | 16534 | 0 | But the evil spirit answered them, “ Jesus I know, and Paul I **recognize**, but who are you?” |

### 3.18 H0995 בִּין bin "to understand": 8 own occurrences in 7 verses

- **Meaning as stored:** Hebrew; native word בִּין, transliteration bin; STEP gloss "to understand"; sense head "to understand" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0995):** to discern, understand, consider; (TWOT) prudent, regard.
- **Related terms (24):** H0946 bu.nah "Bunah"; H0996G ba.yin "between"; H0996H ba.yin "between: among"; H0998 bi.nah "understanding"; H1002 bi.rah "palace"; H1003 bi.ra.nit "fortress"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 170; verses STEP attests 162; verse_lexical rows the parse found 170.

- **Carried by the member words:** perceived (3), learn (2), comprehended (1), discovered (1), examine (1).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 38:18 | comprehended | HVtp2ms | none recorded | - | 0 | Have you **comprehended** the expanse of the earth? Declare, if you know all this. |
| Neh 13:7 | discovered | HVqw1cs | none recorded | - | 0 | and came to Jerusalem, and I then **discovered** the evil that Eliashib had done for Tobiah, preparing for him a chamber in the courts of the house of God. |
| Jer 2:10 | examine | HVtv2mp | none recorded | - | 0 | For cross to the coasts of Cyprus and see, or send to Kedar and **examine** with care; see if there has been such a thing. |
| Pro 8:5 | learn | HVhv2mp | none recorded | - | 0 | O simple ones, **learn** prudence; O fools, learn sense. |
| Pro 8:5 | learn | HVhv2mp | none recorded | - | 0 | O simple ones, **learn** prudence; O fools, learn sense. |
| 1Sa 3:8 | perceived | HVqw3ms | none recorded | 17816 | 0 | And the Lord called Samuel again the third time. And he arose and went to Eli and said, “ Here I am, for you called me.” Then Eli **perceived** that the Lord was calling the boy. |
| Pro 7:7 | perceived | HVqc1cs | none recorded | - | 0 | and I have seen among the simple, I have **perceived** among the youths, a young man lacking sense, |
| Dan 9:2 | perceived | HVqp1cs | none recorded | - | 0 | in the first year of his reign, I, Daniel, **perceived** in the books the number of years that, according to the word of the Lord to Jeremiah the prophet, must pass before the end of the desolations of Jerusalem, namely, seventy years. |

### 3.19 H5234A נָכַר na.khar "to recognize": 7 own occurrences in 7 verses

- **Meaning as stored:** Hebrew; native word נָכַר, transliteration na.khar; STEP gloss "to recognize"; sense head "to recognize" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5234):** to recognise, acknowledge, know, respect, discern, regard.
- **Related terms (3):** H1971 hak.ka.rah "look"; H4378 mak.kar "acquaintance"; H5234B na.khar "to alienate".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 45; verses STEP attests 41; verse_lexical rows the parse found 42.

- **Carried by the member words:** recognize (3), know (1), knowing (1), known (1), knows (1).
- **Engagement of these occurrences:** none recorded 7.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 7:10 | know | HVhi3ms | none recorded | - | 0 | he returns no more to his house, nor does his place **know** him anymore. |
| Job 34:25 | knowing | HVhi3ms | none recorded | - | 0 | Thus, **knowing** their works, he overturns them in the night, and they are crushed. |
| Pro 20:11 | known | HVti3ms | none recorded | - | 0 | Even a child makes himself **known** by his acts, by whether his conduct is pure and upright. |
| Psa 103:16 | knows | HVhi3ms | none recorded | - | 0 | for the wind passes over it, and it is gone, and its place **knows** it no more. |
| Gen 27:23 | recognize | HVhp3ms | none recorded | - | 0 | And he did not **recognize** him, because his hands were hairy like his brother Esau’s hands. So he blessed him. |
| Gen 42:8 | recognize | HVhp3cp | none recorded | - | 0 | And Joseph recognized his brothers, but they did not **recognize** him. |
| Job 2:12 | recognize | HVhp3cp | none recorded | - | 0 | And when they saw him from a distance, they did not **recognize** him. And they raised their voices and wept, and they tore their robes and sprinkled dust on their heads toward heaven. |

### 3.20 H1844 דֵּעָה de.ah "knowledge": 6 own occurrences in 6 verses

- **Meaning as stored:** Hebrew; native word דֵּעָה, transliteration de.ah; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Related terms (20):** H1843 de.a "knowledge"; H1845 de.u.el "Deuel"; H1847 da.at "knowledge"; H3037G yad.du.a "Jaddua"; H3037H yad.du.a "Jaddua"; H3043G ye.di.a.el "Jediael"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 6; verse_lexical rows the parse found 6.

- **Carried by the member words:** knowledge (6).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 2:3 | knowledge | HNcfpa | none recorded | 15135, 15146, 15170 | 0 | Talk no more so very proudly, let not arrogance come from your mouth; for the Lord is a God of **knowledge**, and by him actions are weighed. |
| Job 36:4 | knowledge | HNcfpa | none recorded | - | 0 | For truly my words are not false; one who is perfect in **knowledge** is with you. |
| Psa 73:11 | knowledge | HNcfsa | none recorded | - | 0 | And they say, “ How can God know? Is there **knowledge** in the Most High?” |
| Isa 11:9 | knowledge | HNcfsa | none recorded | - | 0 | They shall not hurt or destroy in all my holy mountain; for the earth shall be full of the **knowledge** of the Lord as the waters cover the sea. |
| Isa 28:9 | knowledge | HNcfsa | none recorded | - | 0 | “To whom will he teach **knowledge**, and to whom will he explain the message? Those who are weaned from the milk, those taken from the breast? |
| Jer 3:15 | knowledge | HNcfsa | none recorded | - | 0 | “‘And I will give you shepherds after my own heart, who will feed you with **knowledge** and understanding. |

### 3.21 H6622 פָּתַר pa.tar "to interpret": 6 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word פָּתַר, transliteration pa.tar; STEP gloss "to interpret"; sense head "to interpret" (the code is its own lemma).
- **Related terms (6):** H6572A par.she.gen "copy"; H6572B pat.she.gen "copy"; H6590 pe.shar "to interpret"; H6623 pit.ron "interpretation"; H6624 pat.ros "Pathros"; H6625 pat.ru.sim "Pathrusim".
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 0; verse_lexical rows the parse found 9.

- **Carried by the member words:** can interpret (2), interpret (2), interpreted (2).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 41:15 | can interpret | HVqrmsa | none recorded | - | 0 | And Pharaoh said to Joseph, “I have had a dream, and there is no one who **can interpret** it. I have heard it said of you that when you hear a dream you can interpret it.” |
| Gen 41:15 | can interpret | HVqcc | none recorded | - | 0 | And Pharaoh said to Joseph, “I have had a dream, and there is no one who **can interpret** it. I have heard it said of you that when you hear a dream you can interpret it.” |
| Gen 40:8 | interpret | HVqrmsa | none recorded | 14220 | 0 | They said to him, “We have had dreams, and there is no one to **interpret** them.” And Joseph said to them, “Do not interpretations belong to God? Please tell them to me.” |
| Gen 41:8 | interpret | HVqrmsa | none recorded | 16036 | 0 | So in the morning his spirit was troubled, and he sent and called for all the magicians of Egypt and all its wise men. Pharaoh told them his dreams, but there was none who could **interpret** them to Pharaoh. |
| Gen 41:12 | interpreted | HVqw3ms | none recorded | - | 0 | A young Hebrew was there with us, a servant of the captain of the guard. When we told him, he **interpreted** our dreams to us, giving an interpretation to each man according to his dream. |
| Gen 41:13 | interpreted | HVqp3ms | none recorded | - | 0 | And as he **interpreted** to us, so it came about. I was restored to my office, and the baker was hanged.” |

### 3.22 G5318 φανερός faneros "clear": 5 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word φανερός, transliteration faneros; STEP gloss "clear"; sense head "clear" (the code is its own lemma).
- **Related terms (17):** G0852 afanēs "hidden"; G0853 afanizō "to destroy"; G0854 afanismos "disappearance"; G0855 afantos "disappearing"; G1307 diafanēs "transparent"; G1717 emfanēs "revealed"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 29; verses STEP attests 0; verse_lexical rows the parse found 17.

- **Carried by the member words:** known (5).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 12:16 | known | A-ASM | none recorded | - | 0 | and ordered them not to make him **known**. |
| Mar 3:12 | known | A-ASM | none recorded | - | 0 | And he strictly ordered them not to make him **known**. |
| Mar 6:14 | known | A-NSN | none recorded | - | 0 | King Herod heard of it, for Jesus ’ name had become **known**. Some said, “ John the Baptist has been raised from the dead. That is why these miraculous powers are at work in him.” |
| Act 7:13 | known | A-NSN | none recorded | - | 0 | And on the second visit Joseph made himself **known** to his brothers, and Joseph’s family became known to Pharaoh. |
| Phili 1:13 | known | A-APM | none recorded | - | 0 | so that it has become **known** throughout the whole imperial guard and to all the rest that my imprisonment is for Christ. |

### 3.23 H4093 מַדָּע mad.da "knowledge": 5 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word מַדָּע, transliteration mad.da; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4093):** knowledge, thought.
- **Related terms (21):** H1843 de.a "knowledge"; H1844 de.ah "knowledge"; H1845 de.u.el "Deuel"; H1847 da.at "knowledge"; H3037G yad.du.a "Jaddua"; H3037H yad.du.a "Jaddua"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 6; verse_lexical rows the parse found 6.

- **Carried by the member words:** knowledge (3), learning (2).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ch 1:10 | knowledge | HNcmsa | none recorded | - | 0 | Give me now wisdom and **knowledge** to go out and come in before this people, for who can govern this people of yours, which is so great?” |
| 2Ch 1:11 | knowledge | HNcmsa | none recorded | - | 0 | God answered Solomon, “ Because this was in your heart, and you have not asked for possessions, wealth, honor, or the life of those who hate you, and have not even asked for long life, but have asked for wisdom and **knowledge** for yourself that you may govern my people over whom I have made you king, |
| 2Ch 1:12 | knowledge | HNcmsa | none recorded | - | 0 | wisdom and **knowledge** are granted to you. I will also give you riches, possessions, and honor, such as none of the kings had who were before you, and none after you shall have the like.” |
| Dan 1:4 | learning | HNcmsa | none recorded | - | 0 | youths without blemish, of good appearance and skillful in all wisdom, endowed with knowledge, understanding **learning**, and competent to stand in the king’s palace, and to teach them the literature and language of the Chaldeans. |
| Dan 1:17 | learning | HNcmsa | none recorded | - | 0 | As for these four youths, God gave them **learning** and skill in all literature and wisdom, and Daniel had understanding in all visions and dreams. |

### 3.24 G1329 διερμηνεύω diermēneuō "to interpret": 4 own occurrences in 4 verses

- **Meaning as stored:** Greek; native word διερμηνεύω, transliteration diermēneuō; STEP gloss "to interpret"; sense head "to interpret" (the code is its own lemma).
- **Related terms (8):** G1223 dia "through/because of"; G1328 diermēneutēs "interpreter"; G1421 dusermēneutos "hard to interpret"; G2058 hermēneia "interpretation"; G2059 hermēneuō "to interpret"; G2060G hermēs "Hermes"; more in the workbook.
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** interpret (3), interpreted (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 12:30 | interpret | V-PAI-3P | none recorded | - | 0 | Do all possess gifts of healing? Do all speak with tongues? Do all **interpret**? |
| 1Cor 14:13 | interpret | V-PAS-3S | none recorded | - | 0 | Therefore, one who speaks in a tongue should pray that he may **interpret**. |
| 1Cor 14:27 | interpret | V-PAM-3S | none recorded | - | 0 | If any speak in a tongue, let there be only two or at most three, and each in turn, and let someone **interpret**. |
| Luk 24:27 | interpreted | V-AAI-3S | none recorded | - | 0 | And beginning with Moses and all the Prophets, he **interpreted** to them in all the Scriptures the things concerning himself. |

### 3.25 G1381 δοκιμάζω dokimazō "to test": 4 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word δοκιμάζω, transliteration dokimazō; STEP gloss "to test"; sense head "to test" (the code is its own lemma).
- **Related terms (4):** G0593 apodokimazō "to reject"; G1382 dokimē "test"; G1383 dokimion "testing"; G1384 dokimos "tested".
- **Clusters (cluster_strong):** M35 Being Tested (None).
- **Counts, three measures as stored:** STEP token count 45; verses STEP attests 21; verse_lexical rows the parse found 23.

- **Carried by the member words:** examine (2), interpret (2).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 14:19 | examine | V-AAN | none recorded | - | 0 | And another said, ‘I have bought five yoke of oxen, and I go to **examine** them. Please have me excused.’ |
| 1Cor 11:28 | examine | V-PAM-3S | none recorded | - | 0 | Let a person **examine** himself, then, and so eat of the bread and drink of the cup. |
| Luk 12:56 | interpret | V-PAN | none recorded | - | 0 | You hypocrites! You know how to **interpret** the appearance of earth and sky, but why do you not know how to interpret the present time? |
| Luk 12:56 | interpret | V-PAN | none recorded | - | 0 | You hypocrites! You know how to **interpret** the appearance of earth and sky, but why do you not know how to interpret the present time? |

### 3.26 H5046 נָגַד na.gad "to tell": 4 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word נָגַד, transliteration na.gad; STEP gloss "to tell"; sense head "to tell" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5046):** to be conspicuous, tell, make known.
- **Related terms (3):** H5047 ne.gad "to flow"; H5048 ne.ged "before"; H5057 na.gid "leader".
- **Clusters (cluster_strong):** M65 Speech & Tongue (heuristic).
- **Counts, three measures as stored:** STEP token count 374; verses STEP attests 345; verse_lexical rows the parse found 371.

- **Carried by the member words:** made known (2), certainty (1), known (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jos 9:24 | certainty | HVHp3ms | none recorded | - | 0 | They answered Joshua, “Because it was told to your servants for a **certainty** that the Lord your God had commanded his servant Moses to give you all the land and to destroy all the inhabitants of the land from before you—so we feared greatly for our lives because of you and did this thing. |
| Est 2:10 | known | HVhi3fs | none recorded | - | 0 | Esther had not made **known** her people or kindred, for Mordecai had commanded her not to make it known. |
| Est 2:10 | made known | HVhp3fs | none recorded | - | 0 | Esther had not **made known** her people or kindred, for Mordecai had commanded her not to make it known. |
| Est 2:20 | made known | HVhrfsa | none recorded | - | 0 | Esther had not **made known** her kindred or her people, as Mordecai had commanded her, for Esther obeyed Mordecai just as when she was brought up by him. |

### 3.27 H7200H רָאָה ra.ah "to see: examine": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word רָאָה, transliteration ra.ah; STEP gloss "to see: examine"; sense head "examine/consider".
- **Senses (first level of the meaning tree of the lemma H7200):** to see, look at, inspect, perceive, consider.
- **Related terms (26):** H3070 yir.eh "Provider [God]"; H3376 yir.iy.yah "Irijah"; H4758 mar.eh "appearance"; H4759A mar.ah "vision"; H4759B mar.ah "mirror"; H7200G ra.ah "to see: see"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 24; verses STEP attests 24; verse_lexical rows the parse found 24.

- **Carried by the member words:** perceived (2), learn (1), learned (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 19:3 | learn | HVqq1cs | none recorded | - | 0 | And I will go out and stand beside my father in the field where you are, and I will speak to my father about you. And if I **learn** anything I will tell you.” |
| Gen 42:1 | learned | HVqw3ms | none recorded | - | 0 | When Jacob **learned** that there was grain for sale in Egypt, he said to his sons, “ Why do you look at one another?” |
| Judg 6:22 | perceived | HVqw3ms | none recorded | - | 0 | Then Gideon **perceived** that he was the angel of the Lord. And Gideon said, “ Alas, O Lord God! For now I have seen the angel of the Lord face to face.” |
| 1Ki 3:28 | perceived | HVqp3cp | none recorded | - | 0 | And all Israel heard of the judgment that the king had rendered, and they stood in awe of the king, because they **perceived** that the wisdom of God was in him to do justice. |

### 3.28 G4894 συνείδω suneidō "be aware": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word συνείδω, transliteration suneidō; STEP gloss "be aware"; sense head "be aware" (the code is its own lemma).
- **Related terms (27):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** knowledge (1), learned (1), realized (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 5:2 | knowledge | V-RAP-GSF | none recorded | - | 0 | and with his wife’s **knowledge** he kept back for himself some of the proceeds and brought only a part of it and laid it at the apostles ’ feet. |
| Act 14:6 | learned | V-2AAP-NPM | none recorded | - | 0 | they **learned** of it and fled to Lystra and Derbe, cities of Lycaonia, and to the surrounding country, |
| Act 12:12 | realized | V-2AAP-NSM | none recorded | - | 0 | When he **realized** this, he went to the house of Mary, the mother of John whose other name was Mark, where many were gathered together and were praying. |

### 3.29 H1875 דָּרַשׁ da.rash "to seek": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word דָּרַשׁ, transliteration da.rash; STEP gloss "to seek"; sense head "to seek" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1875):** to resort to, seek, seek with care, enquire, require.
- **Related terms (1):** H4097 mid.rash "story".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 167; verses STEP attests 152; verse_lexical rows the parse found 164.

- **Carried by the member words:** examine (1), studied (1), study (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ezr 10:16 | examine | HVqcc | none recorded | - | 3 | Then the returned exiles did so. Ezra the priest selected men, heads of fathers ’ houses, according to their fathers’ houses, each of them designated by name. On the first day of the tenth month they sat down to **examine** the matter; |
| Psa 111:2 | studied | HVqsmpa | none recorded | - | 3 | Great are the works of the Lord, **studied** by all who delight in them. |
| Ezr 7:10 | study | HVqcc | none recorded | 16513, 17107, 19164, 19166, 19175 | 5 | For Ezra had set his heart to **study** the Law of the Lord, and to do it and to teach his statutes and rules in Israel. |

### 3.30 G1121 γράμμα gramma "something written": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word γράμμα, transliteration gramma; STEP gloss "something written"; sense head "something written" (the code is its own lemma).
- **Related terms (1):** G1125 grafō "to write".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 33; verses STEP attests 0; verse_lexical rows the parse found 14.

- **Carried by the member words:** learning (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 7:15 | learning | N-APN | none recorded | - | 0 | The Jews therefore marveled, saying, “ How is it that this man has **learning**, when he has never studied?” |
| Act 26:24 | learning | N-NPN | none recorded | - | 0 | And as he was saying these things in his defense, Festus said with a loud voice, “ Paul, you are out of your mind; your great **learning** is driving you out of your mind.” |

### 3.31 G1492H εἴδω eidō "to perceive: see": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word εἴδω, transliteration eidō; STEP gloss "to perceive: see"; sense head "to perceive: see" (the code is its own lemma).
- **Related terms (29):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 396; verses STEP attests 0; verse_lexical rows the parse found 311.

- **Carried by the member words:** know (1), knowing (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 1:33 | know | V-2LAI-1S | none recorded | - | 0 | I myself did not **know** him, but he who sent me to baptize with water said to me, ‘He on whom you see the Spirit descend and remain, this is he who baptizes with the Holy Spirit.’ |
| Mat 9:4 | knowing | V-2AAP-NSM | none recorded | - | 0 | But Jesus, **knowing** their thoughts, said, “ Why do you think evil in your hearts? |

### 3.32 G2638 καταλαμβάνω katalambanō "to grasp": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word καταλαμβάνω, transliteration katalambanō; STEP gloss "to grasp"; sense head "to grasp" (the code is its own lemma).
- **Related terms (14):** G0353 analambanō "to take up"; G0482 antilambanō "to help"; G0618 apolambanō "to get back"; G1949 epilambanō "to catch"; G2596 kata "according to"; G2983 lambanō "to take"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 89; verses STEP attests 14; verse_lexical rows the parse found 15.

- **Carried by the member words:** comprehend (1), perceived (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 3:18 | comprehend | V-2AMN | none recorded | - | 0 | may have strength to **comprehend** with all the saints what is the breadth and length and height and depth, |
| Act 4:13 | perceived | V-2AMP-NPM | none recorded | - | 0 | Now when they saw the boldness of Peter and John, and **perceived** that they were uneducated, common men, they were astonished. And they recognized that they had been with Jesus. |

### 3.33 G5319 φανερόω faneroō "to reveal": 2 own occurrences in 1 verse

- **Meaning as stored:** Greek; native word φανερόω, transliteration faneroō; STEP gloss "to reveal"; sense head "to reveal" (the code is its own lemma).
- **Related terms (16):** G0852 afanēs "hidden"; G0853 afanizō "to destroy"; G0854 afanismos "disappearance"; G0855 afantos "disappearing"; G1307 diafanēs "transparent"; G1717 emfanēs "revealed"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 50; verses STEP attests 44; verse_lexical rows the parse found 49.

- **Carried by the member words:** known (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 5:11 | known | V-RPI-1P | none recorded | - | 0 | Therefore, knowing the fear of the Lord, we persuade others. But what we are is **known** to God, and I hope it is known also to your conscience. |
| 2Cor 5:11 | known | V-RPN | none recorded | - | 0 | Therefore, knowing the fear of the Lord, we persuade others. But what we are is **known** to God, and I hope it is known also to your conscience. |

### 3.34 H1843 דֵּעַ de.a "knowledge": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word דֵּעַ, transliteration de.a; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1843):** knowledge, opinion.
- **Related terms (21):** H1844 de.ah "knowledge"; H1845 de.u.el "Deuel"; H1847 da.at "knowledge"; H1862 dar.da "Darda"; H3037G yad.du.a "Jaddua"; H3037H yad.du.a "Jaddua"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** knowledge (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 36:3 | knowledge | HNcmsc | none recorded | - | 0 | I will get my **knowledge** from afar and ascribe righteousness to my Maker. |
| Job 37:16 | knowledge | HNcmpa | none recorded | - | 0 | Do you know the balancings of the clouds, the wondrous works of him who is perfect in **knowledge**, |

### 3.35 H3948 לֶ֫קַח le.qach "teaching": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word לֶ֫קַח, transliteration le.qach; STEP gloss "teaching"; sense head "teaching" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3948):** learning, teaching, insight.
- **Related terms (12):** H3947G la.qach "to take: take"; H3947H la.qach "to take: recieve"; H3947I la.qach "to take: marry"; H3947J la.qach "to take: bring"; H3947K la.qach "to take: buy"; H3947L la.qach "to take: fire"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 0; verse_lexical rows the parse found 9.

- **Carried by the member words:** learning (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 1:5 | learning | HNcmsa | none recorded | - | 0 | Let the wise hear and increase in **learning**, and the one who understands obtain guidance, |
| Pro 9:9 | learning | HNcmsa | none recorded | - | 0 | Give instruction to a wise man, and he will be still wiser; teach a righteous man, and he will increase in **learning**. |

### 3.36 H4486 מַנְדַּע man.da "knowledge": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word מַנְדַּע, transliteration man.da; STEP gloss "knowledge"; sense head "knowledge" (the code is its own lemma).
- **Related terms (2):** H3046 ye.da "to know"; H4093 mad.da "knowledge".
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** knowledge (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 2:21 | knowledge | ANcbsd | none recorded | - | 0 | He changes times and seasons; he removes kings and sets up kings; he gives wisdom to the wise and **knowledge** to those who have understanding; |
| Dan 5:12 | knowledge | ANcbsa | none recorded | - | 0 | because an excellent spirit, **knowledge**, and understanding to interpret dreams, explain riddles, and solve problems were found in this Daniel, whom the king named Belteshazzar. Now let Daniel be called, and he will show the interpretation.” |

### 3.37 H8610 תָּפַשׂ ta.pha.s "to capture": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word תָּפַשׂ, transliteration ta.pha.s; STEP gloss "to capture"; sense head "to capture" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8610):** to catch, handle, lay hold, take hold of, seize, wield.
- **Related terms (2):** H8612 to.phet "Topheth"; H8613 toph.teh "burning-place".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 65; verses STEP attests 60; verse_lexical rows the parse found 65.

- **Carried by the member words:** grasped (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 21:11 | grasped | HVqcc | none recorded | - | 0 | So the sword is given to be polished, that it may be **grasped** in the hand. It is sharpened and polished to be given into the hand of the slayer. |
| Eze 29:7 | grasped | HVqcc | none recorded | - | 0 | when they **grasped** you with the hand, you broke and tore all their shoulders; and when they leaned on you, you broke and made all their loins to shake. |

### 3.38 G0056 ἀγνωσία agnōsia "ignorance": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀγνωσία, transliteration agnōsia; STEP gloss "ignorance"; sense head "ignorance" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; G1097 ginōskō "to know"; more in the workbook.
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** no knowledge (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 15:34 | no knowledge | N-ASF | none recorded | - | 0 | Wake up from your drunken stupor, as is right, and do not go on sinning. For some have **no knowledge** of God. I say this to your shame. |

### 3.39 G0261 ἀμαθής amathēs "ignorant": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀμαθής, transliteration amathēs; STEP gloss "ignorant"; sense head "ignorant" (the code is its own lemma).
- **Related terms (5):** G3100 mathēteuō "to disciple"; G3101 mathētēs "disciple"; G3102 mathētria "disciple"; G3129 manthanō "to learn"; G4827 summathētēs "fellow disciple".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** ignorant (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Pe 3:16 | ignorant | A-NPM | none recorded | - | 0 | as he does in all his letters when he speaks in them of these matters. There are some things in them that are hard to understand, which the **ignorant** and unstable twist to their own destruction, as they do the other Scriptures. |

### 3.40 G0319 ἀναγνωρίζω anagnōrizō "to recognize": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀναγνωρίζω, transliteration anagnōrizō; STEP gloss "to recognize"; sense head "to recognize" (the code is its own lemma).
- **Related terms (24):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0303 ana "each"; G0314 anaginōskō "to read"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 7:13 | known | V-API-3S | none recorded | - | 0 | And on the second visit Joseph made himself **known** to his brothers, and Joseph’s family became known to Pharaoh. |

### 3.41 G0350 ἀνακρίνω anakrinō "to investigate": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀνακρίνω, transliteration anakrinō; STEP gloss "to investigate"; sense head "to investigate" (the code is its own lemma).
- **Related terms (3):** G0303 ana "each"; G0351 anakrisis "investigation"; G2919 krinō "to judge".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 17; verses STEP attests 14; verse_lexical rows the parse found 16.

- **Carried by the member words:** examine (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 9:3 | examine | V-PAP-DPM | none recorded | - | 0 | This is my defense to those who would **examine** me. |

### 3.42 G0426 ἀνετάζω anetazō "to question": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀνετάζω, transliteration anetazō; STEP gloss "to question"; sense head "to question" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** examine (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 22:29 | examine | V-PAN | none recorded | - | 0 | So those who were about to **examine** him withdrew from him immediately, and the tribune also was afraid, for he realized that Paul was a Roman citizen and that he had bound him. |

### 3.43 G0725 ἁρπαγμός harpagmos "something to grasp": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἁρπαγμός, transliteration harpagmos; STEP gloss "something to grasp"; sense head "something to grasp" (the code is its own lemma).
- **Related terms (1):** G0726 harpazō "to seize".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** grasped (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Phili 2:6 | grasped | N-ASM | none recorded | - | 0 | who, though he was in the form of God, did not count equality with God a thing to be **grasped**, |

### 3.44 G0803 ἀσφάλεια asfaleia "security": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀσφάλεια, transliteration asfaleia; STEP gloss "security"; sense head "security" (the code is its own lemma).
- **Related terms (1):** G0804 asfalēs "secure".
- **Clusters (cluster_strong):** M19 Trust & Refuge (high).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** certainty (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 1:4 | certainty | N-ASF | none recorded | - | 0 | that you may have **certainty** concerning the things you have been taught. |

### 3.45 G0864 ἀφικνέομαι afikneomai "to reach": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀφικνέομαι, transliteration afikneomai; STEP gloss "to reach"; sense head "to reach" (the code is its own lemma).
- **Related terms (2):** G0575 apo "away from"; G2425 hikanos "sufficient".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 16:19 | known | V-2ADI-3S | none recorded | - | 0 | For your obedience is **known** to all, so that I rejoice over you, but I want you to be wise as to what is good and innocent as to what is evil. |

### 3.46 G1213 δηλόω dēloō "to make clear": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word δηλόω, transliteration dēloō; STEP gloss "to make clear"; sense head "to make clear" (the code is its own lemma).
- **Related terms (7):** G0082 adēlos "unclear"; G0083 adēlotēs "uncertainty"; G0084 adēlōs "uncertainly"; G1212 dēlos "Urim"; G1552 ekdēlos "clearly evident"; G2612 katadēlos "evident"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 21; verses STEP attests 0; verse_lexical rows the parse found 7.

- **Carried by the member words:** made known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Col 1:8 | made known | V-AAP-NSM | none recorded | - | 0 | and has **made known** to us your love in the Spirit. |

### 3.47 G1232 διαγνωρίζω diagnōrizō "to report": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word διαγνωρίζω, transliteration diagnōrizō; STEP gloss "to report"; sense head "to report" (the code is its own lemma).
- **Related terms (24):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** made known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 2:17 | made known | V-AAI-3P | none recorded | - | 0 | And when they saw it, they **made known** the saying that had been told them concerning this child. |

### 3.48 G1252 διακρίνω diakrinō "to judge/doubt": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word διακρίνω, transliteration diakrinō; STEP gloss "to judge/doubt"; sense head "to judge/doubt" (the code is its own lemma).
- **Related terms (4):** G0087 adiakritos "impartial"; G1223 dia "through/because of"; G1253 diakrisis "discernment"; G2919 krinō "to judge".
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 44; verses STEP attests 18; verse_lexical rows the parse found 19.

- **Carried by the member words:** interpret (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 16:3 | interpret | V-PAN | none recorded | - | 0 | And in the morning, ‘It will be stormy today, for the sky is red and threatening.’ You know how to **interpret** the appearance of the sky, but you cannot interpret the signs of the times. |

### 3.49 G1328 διερμηνευτής diermēneutēs "interpreter": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word διερμηνευτής, transliteration diermēneutēs; STEP gloss "interpreter"; sense head "interpreter" (the code is its own lemma).
- **Related terms (8):** G1223 dia "through/because of"; G1329 diermēneuō "to interpret"; G1421 dusermēneutos "hard to interpret"; G2058 hermēneia "interpretation"; G2059 hermēneuō "to interpret"; G2060G hermēs "Hermes"; more in the workbook.
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** interpret (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 14:28 | interpret | N-NSM | none recorded | - | 0 | But if there is no one to **interpret**, let each of them keep silent in church and speak to himself and to God. |

### 3.50 G1722 ἐν en "in/on/among": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐν, transliteration en; STEP gloss "in/on/among"; sense head "in/on/among" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 10000; verses STEP attests 0; verse_lexical rows the parse found 2673.

- **Carried by the member words:** known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 7:4 | known | PREP | none recorded | - | 0 | For no one works in secret if he seeks to be **known** openly. If you do these things, show yourself to the world.” |

### 3.51 G1834 ἐξηγέομαι exēgeomai "to tell": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐξηγέομαι, transliteration exēgeomai; STEP gloss "to tell"; sense head "to tell" (the code is its own lemma).
- **Related terms (2):** G1537 ek "out from"; G2233 hēgeomai "to govern".
- **Clusters (cluster_strong):** M65 Speech & Tongue (heuristic).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 0; verse_lexical rows the parse found 7.

- **Carried by the member words:** known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 1:18 | known | V-ADI-3S | none recorded | - | 0 | No one has ever seen God; God the only Son, who is at the Father’s side, he has made him **known**. |

### 3.52 G2467 ἴσημι isēmi "to know": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἴσημι, transliteration isēmi; STEP gloss "to know"; sense head "to know" (the code is its own lemma).
- **Related terms (4):** G1492H eidō "to perceive: see"; G1492I eidō "to perceive: know"; G2467 isēmi "to know"; G6063 oida "to know".
- **Clusters (cluster_strong):** M15 Knowing & Understanding (high).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 26:4 | known | V-PAI-3P | none recorded | - | 0 | “ My manner of life from my youth, spent from the beginning among my own nation and in Jerusalem, is **known** by all the Jews. |

### 3.53 G2657 κατανοέω katanoeō "to observe": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word κατανοέω, transliteration katanoeō; STEP gloss "to observe"; sense head "to observe" (the code is its own lemma).
- **Related terms (2):** G2596 kata "according to"; G3539 noeō "to understand".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 37; verses STEP attests 14; verse_lexical rows the parse found 14.

- **Carried by the member words:** perceived (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 20:23 | perceived | V-AAP-NSM | none recorded | - | 0 | But he **perceived** their craftiness, and said to them, |

### 3.54 G2919 κρίνω krinō "to judge": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word κρίνω, transliteration krinō; STEP gloss "to judge"; sense head "to judge" (the code is its own lemma).
- **Related terms (2):** G2917 krima "judgment"; G2923 kritēs "judge".
- **Clusters (cluster_strong):** T3 Operations (None); M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 301; verses STEP attests 97; verse_lexical rows the parse found 113.

- **Carried by the member words:** concluded (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 5:14 | concluded | V-AAP-APM | none recorded | - | 0 | For the love of Christ controls us, because we have **concluded** this: that one has died for all, therefore all have died; |

### 3.55 G3811 παιδεύω paideuō "to instruct": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word παιδεύω, transliteration paideuō; STEP gloss "to instruct"; sense head "to instruct" (the code is its own lemma).
- **Related terms (4):** G0521 apaideutos "uninstructed"; G3809 paideia "discipline"; G3810 paideutēs "instructor"; G3816 pais "child".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 72; verses STEP attests 13; verse_lexical rows the parse found 13.

- **Carried by the member words:** learn (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ti 1:20 | learn | V-APS-3P | none recorded | - | 0 | among whom are Hymenaeus and Alexander, whom I have handed over to Satan that they may **learn** not to blaspheme. |

### 3.56 G3985H πειράζω peirazō "to test/tempt: test": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word πειράζω, transliteration peirazō; STEP gloss "to test/tempt: test"; sense head "to test/tempt: test" (the code is its own lemma).
- **Related terms (9):** G0552 apeiros "unacquainted"; G1598 ekpeirazō "to test/tempt"; G3984 peira "test"; G3985G peirazō "to test/tempt: tempt"; G3985H peirazō "to test/tempt: test"; G3985I peirazō "to test/tempt: try"; more in the workbook.
- **Clusters (cluster_strong):** M35 Being Tested (None).
- **Counts, three measures as stored:** STEP token count 24; verses STEP attests 0; verse_lexical rows the parse found 19.

- **Carried by the member words:** examine (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 13:5 | examine | V-PAM-2P | none recorded | - | 0 | **Examine** yourselves, to see whether you are in the faith. Test yourselves. Or do you not realize this about yourselves, that Jesus Christ is in you?— unless indeed you fail to meet the test! |

### 3.57 G4160G ποιέω poieō "to do/make: do": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ποιέω, transliteration poieō; STEP gloss "to do/make: do"; sense head "to do/make: do" (the code is its own lemma).
- **Related terms (7):** G4160G poieō "to do/make: do"; G4160H poieō "to do/make: make"; G4160I poieō "to do/make: appoint"; G4160J poieō "to do/make: spend[time]"; G4161 poiēma "workmanship"; G4162 poiēsis "he did"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 3366; verses STEP attests 497; verse_lexical rows the parse found 552.

- **Carried by the member words:** realized (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 3:11 | realized | V-AAI-3S | none recorded | - | 0 | This was according to the eternal purpose that he has **realized** in Christ Jesus our Lord, |

### 3.58 G4267 προγινώσκω proginōskō "to know/choose": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προγινώσκω, transliteration proginōskō; STEP gloss "to know/choose"; sense head "to know/choose" (the code is its own lemma).
- **Related terms (24):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (heuristic).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 26:5 | known | V-PAP-NPM | none recorded | - | 0 | They have **known** for a long time, if they are willing to testify, that according to the strictest party of our religion I have lived as a Pharisee. |

### 3.59 G4441 πυνθάνομαι punthanomai "to inquire": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word πυνθάνομαι, transliteration punthanomai; STEP gloss "to inquire"; sense head "to inquire" (the code is its own lemma).
- **Related terms (4):** G2253 hēmithanēs "half-dead"; G2286 thanasimos "deadly"; G2287 thanatēforos "deadly"; G2289 thanatoō "to kill".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 17; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** learned (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 23:34 | learned | V-2ADP-NSM | none recorded | - | 0 | On reading the letter, he asked what province he was from. And when he **learned** that he was from Cilicia, |

### 3.60 G6083 σύνοιδα sunoida "be conscious of": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word σύνοιδα, transliteration sunoida; STEP gloss "be conscious of"; sense head "be conscious of" (the code is its own lemma).
- **Related terms (4):** G4662 skōlēkobrōtos "worm-eated"; G4894 suneidō "be aware"; G6063 oida "to know"; G6083 sunoida "be conscious of".
- **Clusters (cluster_strong):** M26 Judgment & Condemnation (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** aware (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 4:4 | aware | V-RAI-1S | none recorded | - | 0 | For I am not **aware** of anything against myself, but I am not thereby acquitted. It is the Lord who judges me. |

### 3.61 H0413 אֶל el "to[wards]": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אֶל, transliteration el; STEP gloss "to[wards]"; sense head "to[wards]" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0413):** to, toward, unto (of motion); into (limit is actually entered); toward (of direction, not necessarily physical motion); against (motion or direction of a hostile character); in addition to, to; concerning, in regard to, in reference to, on account of.
- **Related terms (9):** H0454A el.ye.ho.e.nay "Eliehoenai"; H0454B el.yo.e.nay "Elioenai"; H0454G el.ye.ho.e.nay "Eliehoenai"; H0454H el.yo.e.nay "Elioenai"; H0454I el.yo.e.nay "Elioenai"; H0454J el.yo.e.nay "Elioenai"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (None).
- **Counts, three measures as stored:** STEP token count 5533; verses STEP attests 4206; verse_lexical rows the parse found 5515.

- **Carried by the member words:** know (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Zec 4:13 | know | HR | none recorded | - | 0 | He said to me, “Do you not **know** what these are?” I said, “ No, my lord.” |

### 3.62 H0502 אָלַף a.laph "to teach/learn": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אָלַף, transliteration a.laph; STEP gloss "to teach/learn"; sense head "to teach/learn" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0502):** to learn.
- **Related terms (3):** H0441A al.luph "tame"; H0441B al.luph "chief"; H0504 e.leph "cattle".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 0; verse_lexical rows the parse found 4.

- **Carried by the member words:** learn (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 22:25 | learn | HVqi2ms | none recorded | - | 0 | lest you **learn** his ways and entangle yourself in a snare. |

### 3.63 H0816 אָשַׁם a.sham "be guilty": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אָשַׁם, transliteration a.sham; STEP gloss "be guilty"; sense head "be guilty" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0816):** to offend, be guilty, trespass; (TWOT) to be desolate, acknowledge offense.
- **Related terms (3):** H0817 a.sham "guilt [offering]"; H0818 a.shem "guilty"; H0819 ash.mah "guiltiness".
- **Clusters (cluster_strong):** M56 Sin & Guilt (heuristic).
- **Counts, three measures as stored:** STEP token count 35; verses STEP attests 32; verse_lexical rows the parse found 35.

- **Carried by the member words:** realizes (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lev 5:4 | realizes | HVqq3ms | none recorded | 15752, 16562 | 0 | or if anyone utters with his lips a rash oath to do evil or to do good, any sort of rash oath that people swear, and it is hidden from him, when he comes to know it, and he **realizes** his guilt in any of these; |

### 3.64 H2388H חָזַק cha.zaq "to strengthen: hold": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָזַק, transliteration cha.zaq; STEP gloss "to strengthen: hold"; sense head "hold/seize/fix".
- **Senses (first level of the meaning tree of the lemma H2388):** to strengthen, prevail, harden, be strong, become strong, be courageou ... (cut; the whole text is in the workbook).
- **Related terms (21):** H2388G cha.zaq "to strengthen: strengthen"; H2388I cha.zaq "to strengthen: ensure"; H2388J cha.zaq "to strengthen: prevail over"; H2388K cha.zaq "to strengthen: persevere"; H2389 cha.zaq "strong"; H2390 cha.zeq "stronger"; more in the workbook.
- **Clusters (cluster_strong):** M23 Strength & Courage (None).
- **Counts, three measures as stored:** STEP token count 71; verses STEP attests 0; verse_lexical rows the parse found 71.

- **Carried by the member words:** grasped (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 45:1 | grasped | HVhp1cs | none recorded | - | 0 | Thus says the Lord to his anointed, to Cyrus, whose right hand I have **grasped**, to subdue nations before him and to loose the belts of kings, to open doors before him that gates may not be closed: |

### 3.65 H2713 חָקַר cha.qar "to search": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָקַר, transliteration cha.qar; STEP gloss "to search"; sense head "to search" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2713):** to search, search for, search out, examine, investigate.
- **Related terms (2):** H2714 che.qer "search"; H4278 mech.qar "range".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 27; verses STEP attests 26; verse_lexical rows the parse found 27.

- **Carried by the member words:** examine (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lam 3:40 | examine | HVqc1cp | none recorded | - | 0 | Let us test and **examine** our ways, and return to the Lord! |

### 3.66 H3289 יָעַץ ya.ats "to advise": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word יָעַץ, transliteration ya.ats; STEP gloss "to advise"; sense head "to advise" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3289):** to advise, consult, give counsel, counsel, purpose, devise, plan.
- **Related terms (4):** H3272A ye.at "to counsel"; H3272B ya.et "counsellor"; H4156 mo.e.tsah "counsel"; H6098 e.tsah "counsel".
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 79; verses STEP attests 73; verse_lexical rows the parse found 79.

- **Carried by the member words:** know (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 24:14 | know | HVqi1cs | none recorded | - | 0 | And now, behold, I am going to my people. Come, I will let you **know** what this people will do to your people in the latter days.” |

### 3.67 H3330 יַצִּיב yats.tsiv "certain": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word יַצִּיב, transliteration yats.tsiv; STEP gloss "certain"; sense head "certain" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3330):** the truth; surely, reliably, truly; reliable, true, certain, sure.
- **Related terms (1):** H3321 ye.tsav "to know".
- **Clusters (cluster_strong):** M62 Truth & Sincerity (heuristic).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** certainty (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 2:8 | certainty | AAabsa | none recorded | - | 0 | The king answered and said, “ I know with **certainty** that you are trying to gain time, because you see that the word from me is firm — |

### 3.68 H3854 לַ֫הַג la.hag "study": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word לַ֫הַג, transliteration la.hag; STEP gloss "study"; sense head "study" (the code is its own lemma).
- **Related terms (1):** H3855 la.had "Lahad".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** study (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 12:12 | study | HNcmsa | none recorded | - | 0 | My son, beware of anything beyond these. Of making many books there is no end, and much **study** is a weariness of the flesh. |

### 3.69 H3925G לָמַד la.mad "to learn: teach": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word לָמַד, transliteration la.mad; STEP gloss "to learn: teach"; sense head "teach".
- **Senses (first level of the meaning tree of the lemma H3925):** to learn. teach, exercise in.
- **Related terms (7):** H3925H la.mad "to learn: learn"; H3927 le.mu.el "Lemuel"; H3928 lim.mud "disciple"; H3929G le.mekh "Lamech"; H3929H le.mekh "Lamech"; H4451 mal.med "oxgoad"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 66; verses STEP attests 0; verse_lexical rows the parse found 63.

- **Carried by the member words:** learn (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 12:16 | learn | HVqi3mp | none recorded | - | 0 | And it shall come to pass, if they will diligently **learn** the ways of my people, to swear by my name, ‘As the Lord lives,’ even as they taught my people to swear by Baal, then they shall be built up in the midst of my people. |

### 3.70 H3943 לָפַת la.phat "to twist": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word לָפַת, transliteration la.phat; STEP gloss "to twist"; sense head "to twist" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3943):** to twist, grasp, turn, grasp with a twisting motion.
- **Related terms (1):** H3946 laq.qum "Lakkum".
- **Clusters (cluster_strong):** M57 Corruption & Perversion (heuristic).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 0; verse_lexical rows the parse found 3.

- **Carried by the member words:** grasped (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Judg 16:29 | grasped | HVqw3ms | none recorded | - | 0 | And Samson **grasped** the two middle pillars on which the house rested, and he leaned his weight against them, his right hand on the one and his left hand on the other. |

### 3.71 H5869I עַ֫יִן a.yin "eye: appearance": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עַ֫יִן, transliteration a.yin; STEP gloss "eye: appearance"; sense head "appearance".
- **Senses (first level of the meaning tree of the lemma H5869):** eye.
- **Related terms (29):** H4599 ma.yan "spring"; H5770 in "to watch"; H5869A a.yin "eye"; H5869B a.yin "Fountain [Gate]"; H5869G a.yin "Fountain of [Drangons]"; H5869H a.yin "eye: seeing"; more in the workbook.
- **Clusters (cluster_strong):** T14 Body-Parts (medium).
- **Counts, three measures as stored:** STEP token count 164; verses STEP attests 142; verse_lexical rows the parse found 156.

- **Carried by the member words:** knowledge (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 15:24 | knowledge | HNcfdc | none recorded | - | 0 | then if it was done unintentionally without the **knowledge** of the congregation, all the congregation shall offer one bull from the herd for a burnt offering, a pleasing aroma to the Lord, with its grain offering and its drink offering, according to the rule, and one male goat for a sin offering. |

### 3.72 H6590 פְּשַׁר pe.shar "to interpret": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word פְּשַׁר, transliteration pe.shar; STEP gloss "to interpret"; sense head "to interpret" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H6590):** to interpret.
- **Related terms (3):** H6591 pe.shar "interpretation"; H6600 pit.gam "edict"; H6622 pa.tar "to interpret".
- **Clusters (cluster_strong):** M63 Reasoning & Interpretation (heuristic).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 0; verse_lexical rows the parse found 2.

- **Carried by the member words:** interpret (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 5:12 | interpret | AVprmsc | none recorded | 16036, 19302 | 0 | because an excellent spirit, knowledge, and understanding to **interpret** dreams, explain riddles, and solve problems were found in this Daniel, whom the king named Belteshazzar. Now let Daniel be called, and he will show the interpretation.” |

### 3.73 H7919A שָׂכַל sa.khal "be prudent": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׂכַל, transliteration sa.khal; STEP gloss "be prudent"; sense head "be prudent" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7919):** to be prudent, be circumspect, wisely understand, prosper.
- **Related terms (4):** H4905 mas.kil "Maskil"; H7919B sa.khal "to cross hands"; H7920 se.khal "to contemplate"; H7922 se.khel "understanding".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (heuristic).
- **Counts, three measures as stored:** STEP token count 63; verses STEP attests 61; verse_lexical rows the parse found 61.

- **Carried by the member words:** study (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Neh 8:13 | study | HVhcc | none recorded | - | 0 | On the second day the heads of fathers’ houses of all the people, with the priests and the Levites, came together to Ezra the scribe in order to **study** the words of the Law. |

### 3.74 H8085I שָׁמַע sha.ma "to hear: proclaim": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁמַע, transliteration sha.ma; STEP gloss "to hear: proclaim"; sense head "proclaim/loud".
- **Senses (first level of the meaning tree of the lemma H8085):** to hear, listen to, obey; sound.
- **Related terms (90):** H2045 hash.ma.ut "report"; H3458G yish.ma.el "Ishmael"; H3458H yish.ma.el "Ishmael"; H3458I yish.ma.el "Ishmael"; H3458J yish.ma.el "Ishmael"; H3458K yish.ma.el "Ishmael"; more in the workbook.
- **Clusters (cluster_strong):** M41 Being Heard (None).
- **Counts, three measures as stored:** STEP token count 49; verses STEP attests 46; verse_lexical rows the parse found 49.

- **Carried by the member words:** make known (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 9:27 | make known | HVhu1cs | none recorded | - | 0 | As they were going down to the outskirts of the city, Samuel said to Saul, “ Tell the servant to pass on before us, and when he has passed on, stop here yourself for a while, that I may **make known** to you the word of God.” |

### 3.75 H8085J שָׁמַע sha.ma "to hear: understand": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁמַע, transliteration sha.ma; STEP gloss "to hear: understand"; sense head "understand".
- **Senses (first level of the meaning tree of the lemma H8085):** to hear, listen to, obey; sound.
- **Related terms (90):** H2045 hash.ma.ut "report"; H3458G yish.ma.el "Ishmael"; H3458H yish.ma.el "Ishmael"; H3458I yish.ma.el "Ishmael"; H3458J yish.ma.el "Ishmael"; H3458K yish.ma.el "Ishmael"; more in the workbook.
- **Clusters (cluster_strong):** M41 Being Heard (None).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** comprehend (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 33:19 | comprehend | HVqcc | none recorded | - | 0 | You will see no more the insolent people, the people of an obscure speech that you cannot **comprehend**, stammering in a tongue that you cannot understand. |

### 3.76 H8454 תּוּשִׁיָּה tu.shiy.yah "wisdom": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word תּוּשִׁיָּה, transliteration tu.shiy.yah; STEP gloss "wisdom"; sense head "wisdom" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8454):** wisdom, sound knowledge, success, sound or efficient wisdom, abiding s ... (cut; the whole text is in the workbook).
- **Related terms (2):** H3144 yo.shah "Joshah"; H3145 yo.shav.yah "Joshaviah".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (heuristic).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** sound knowledge (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 26:3 | sound knowledge | HNcfsa | none recorded | - | 0 | How you have counseled him who has no wisdom, and plentifully declared **sound knowledge**! |

### 3.77 Occurrences where the member surface is shared with another code's unit (165)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| Rom 11:25 | be unaware | G0050 ἀγνοέω agnoeō "be ignorant" | be unaware | content_part | 2 | none recorded | - | 0 | Lest you be wise in your own sight, I do not want you to **be unaware** of this mystery, brothers: a partial hardening has come upon Israel, until the fullness of the Gentiles has come in. |
| 1Cor 10:1 | be unaware | G0050 ἀγνοέω agnoeō "be ignorant" | be unaware | content_part | 2 | none recorded | - | 0 | For I do not want you to **be unaware**, brothers, that our fathers were all under the cloud, and all passed through the sea, |
| Luk 7:39 | known | G0302 ἄν an "if" | known | content_part | 2 | none recorded | - | 0 | Now when the Pharisee who had invited him saw this, he said to himself, “ If this man were a prophet, he would have **known** who and what sort of woman this is who is touching him, for she is a sinner.” |
| 2Ti 2:23 | ignorant | G0521 ἀπαίδευτος apaideutos "uninstructed" | ignorant | content_part | 2 | none recorded | - | 0 | Have nothing to do with foolish, **ignorant** controversies; you know that they breed quarrels. |
| Heb 11:13 | acknowledged | G0782 ἀσπάζομαι aspazomai "to pay respects to" | acknowledged | content_part | 2 | none recorded | - | 0 | These all died in faith, not having received the things promised, but having seen them and greeted them from afar, and having **acknowledged** that they were strangers and exiles on the earth. |
| Luk 7:39 | known | G1097 γινώσκω ginōskō "to know" | known | content_part | 2 | none recorded | - | 0 | Now when the Pharisee who had invited him saw this, he said to himself, “ If this man were a prophet, he would have **known** who and what sort of woman this is who is touching him, for she is a sinner.” |
| Mat 12:25 | knowing | G1161 δέ de "then" | Knowing | content_part | 2 | none recorded | - | 0 | **Knowing** their thoughts, he said to them, “ Every kingdom divided against itself is laid waste, and no city or house divided against itself will stand. |
| Rom 2:2 | know | G1161 δέ de "then" | know | content_part | 2 | none recorded | - | 0 | We **know** that the judgment of God rightly falls on those who practice such things. |
| 2Cor 6:6 | knowledge | G1722 ἐν en "in/on/among" | knowledge | content_part | 2 | none recorded | - | 0 | by purity, **knowledge**, patience, kindness, the Holy Spirit, genuine love; |
| 2Ti 2:23 | ignorant | G2532 καί kai "and" | ignorant | content_part | 2 | none recorded | - | 0 | Have nothing to do with foolish, **ignorant** controversies; you know that they breed quarrels. |
| Heb 11:13 | acknowledged | G3670 ὁμολογέω homologeō "to confess/profess" | acknowledged | content_part | 2 | none recorded | - | 0 | These all died in faith, not having received the things promised, but having seen them and greeted them from afar, and having **acknowledged** that they were strangers and exiles on the earth. |
| Rom 11:25 | be unaware | G3756 οὐ ou "no" | be unaware | content_part | 2 | none recorded | - | 0 | Lest you be wise in your own sight, I do not want you to **be unaware** of this mystery, brothers: a partial hardening has come upon Israel, until the fullness of the Gentiles has come in. |
| 1Cor 10:1 | be unaware | G3756 οὐ ou "no" | be unaware | content_part | 2 | none recorded | - | 0 | For I do not want you to **be unaware**, brothers, that our fathers were all under the cloud, and all passed through the sea, |
| Act 20:29 | know | G5124 τοῦτο touto "that" | know | content_part | 2 | none recorded | - | 0 | I **know** that after my departure fierce wolves will come in among you, not sparing the flock; |
| Rom 6:6 | know | G5124 τοῦτο touto "that" | know | content_part | 2 | none recorded | - | 0 | We **know** that our old self was crucified with him in order that the body of sin might be brought to nothing, so that we would no longer be enslaved to sin. |
| Mat 12:25 | knowing | G6063 οἶδα oida "to know" | Knowing | content_part | 2 | none recorded | 20455 | 0 | **Knowing** their thoughts, he said to them, “ Every kingdom divided against itself is laid waste, and no city or house divided against itself will stand. |
| Lev 4:23 | known | H0176A אוֹ o "or" | known | content_part | 2 | none recorded | - | 0 | or the sin which he has committed is made **known** to him, he shall bring as his offering a goat, a male without blemish, |
| Lev 4:28 | known | H0176A אוֹ o "or" | known | content_part | 2 | none recorded | - | 0 | or the sin which he has committed is made **known** to him, he shall bring for his offering a goat, a female without blemish, for his sin which he has committed. |
| Judg 13:21 | knew | H0227A אָז az "then" | knew | content_part | 3 | none recorded | - | 0 | The angel of the Lord appeared no more to Manoah and to his wife. Then Manoah **knew** that he was the angel of the Lord. |
| 1Ki 8:39 | know | H0376G אִישׁ ish "man" | know | content_part | 4 | none recorded | - | 0 | then hear in heaven your dwelling place and forgive and act and render to each whose heart you **know**, according to all his ways ( for you, you only, know the hearts of all the children of mankind ), |
| Gen 44:27 | know | H0413 אֶל el "to[wards]" | know | content_part | 4 | none recorded | - | 0 | Then your servant my father said to us, ‘ You **know** that my wife bore me two sons. |
| Num 12:6 | known | H0413 אֶל el "to[wards]" | known | content_part | 3 | none recorded | - | 0 | And he said, “ Hear my words: If there is a prophet among you, I the Lord make myself **known** to him in a vision; I speak with him in a dream. |
| Jos 3:4 | know | H0413 אֶל el "to[wards]" | know | content_part | 4 | none recorded | - | 0 | Yet there shall be a distance between you and it, about 2,000 cubits in length. Do not come near it, in order that you may **know** the way you shall go, for you have not passed this way before.” |
| 2Sa 7:20 | know | H0413 אֶל el "to[wards]" | know | content_part | 4 | none recorded | - | 0 | And what more can David say to you? For you **know** your servant, O Lord God! |
| 2Ki 5:6 | know | H0413 אֶל el "to[wards]" | know | content_part | 3 | none recorded | - | 0 | And he brought the letter to the king of Israel, which read, “ When this letter reaches you, **know** that I have sent to you Naaman my servant, that you may cure him of his leprosy.” |
| 2Ki 9:11 | know | H0413 אֶל el "to[wards]" | know | content_part | 3 | none recorded | - | 0 | When Jehu came out to the servants of his master, they said to him, “Is all well? Why did this mad fellow come to you?” And he said to them, “ You **know** the fellow and his talk.” |
| 1Ch 21:2 | know | H0413 אֶל el "to[wards]" | know | content_part | 3 | none recorded | - | 0 | So David said to Joab and the commanders of the army, “ Go, number Israel, from Beersheba to Dan, and bring me a report, that I may **know** their number.” |
| 1Sa 6:9 | know | H0518A אִם im "if" | know | content_part | 5 | none recorded | - | 0 | and watch. If it goes up on the way to its own land, to Beth-shemesh, then it is he who has done us this great harm, but if not, then we shall **know** that it is not his hand that struck us; it happened to us by coincidence.” |
| Jos 4:22 | know | H0559 אָמַר a.mar "to say" | know | content_part | 2 | none recorded | - | 0 | then you shall let your children **know**, ‘ Israel passed over this Jordan on dry ground.’ |
| Job 34:33 | know | H0589 אֲנִי a.ni "I" | know | content_part | 4 | none recorded | - | 0 | Will he then make repayment to suit you, because you reject it? For you must choose, and not I; therefore declare what you **know**. |
| Gen 19:8 | known | H0834A אֲשֶׁר a.sher "which" | known | content_part | 2 | none recorded | - | 0 | Behold, I have two daughters who have not **known** any man. Let me bring them out to you, and do to them as you please. Only do nothing to these men, for they have come under the shelter of my roof.” |
| Gen 40:22 | interpreted | H0834A אֲשֶׁר a.sher "which" | interpreted | content_part | 3 | none recorded | - | 0 | But he hanged the chief baker, as Joseph had **interpreted** to them. |
| Deu 8:3 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 2 | none recorded | - | 0 | And he humbled you and let you hunger and fed you with manna, which you did not **know**, nor did your fathers know, that he might make you know that man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| Deu 8:16 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 2 | none recorded | - | 0 | who fed you in the wilderness with manna that your fathers did not **know**, that he might humble you and test you, to do you good in the end. |
| Jos 24:31 | known | H0834A אֲשֶׁר a.sher "which" | known | content_part | 3 | none recorded | - | 0 | Israel served the Lord all the days of Joshua, and all the days of the elders who outlived Joshua and had **known** all the work that the Lord did for Israel. |
| 1Sa 25:11 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 2 | none recorded | - | 0 | Shall I take my bread and my water and my meat that I have killed for my shearers and give it to men who come from I do not **know** where?” |
| 1Ki 8:38 | knowing | H0834A אֲשֶׁר a.sher "which" | knowing | content_part | 2 | none recorded | - | 0 | whatever prayer, whatever plea is made by any man or by all your people Israel, each **knowing** the affliction of his own heart and stretching out his hands toward this house, |
| 1Ki 8:39 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 4 | none recorded | - | 0 | then hear in heaven your dwelling place and forgive and act and render to each whose heart you **know**, according to all his ways ( for you, you only, know the hearts of all the children of mankind ), |
| 2Ki 17:26 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 6 | none recorded | - | 0 | So the king of Assyria was told, “The nations that you have carried away and placed in the cities of Samaria do not **know** the law of the god of the land. Therefore he has sent lions among them, and behold, they are killing them, because they do not know the law of the god of the land.” |
| 2Ch 6:29 | knowing | H0834A אֲשֶׁר a.sher "which" | knowing | content_part | 2 | none recorded | - | 0 | whatever prayer, whatever plea is made by any man or by all your people Israel, each **knowing** his own affliction and his own sorrow and stretching out his hands toward this house, |
| 2Ch 6:30 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 3 | none recorded | - | 0 | then hear from heaven your dwelling place and forgive and render to each whose heart you **know**, according to all his ways, for you, you only, know the hearts of the children of mankind, |
| Jer 16:13 | known | H0834A אֲשֶׁר a.sher "which" | known | content_part | 3 | none recorded | - | 0 | Therefore I will hurl you out of this land into a land that neither you nor your fathers have **known**, and there you shall serve other gods day and night, for I will show you no favor.’ |
| Jer 17:4 | know | H0834A אֲשֶׁר a.sher "which" | know | content_part | 2 | none recorded | - | 0 | You shall loosen your hand from your heritage that I gave to you, and I will make you serve your enemies in a land that you do not **know**, for in my anger a fire is kindled that shall burn forever.” |
| Eze 20:9 | known | H0834A אֲשֶׁר a.sher "which" | known | content_part | 3 | none recorded | - | 0 | But I acted for the sake of my name, that it should not be profaned in the sight of the nations among whom they lived, in whose sight I made myself **known** to them in bringing them out of the land of Egypt. |
| Num 14:31 | know | H0853 אֵת et "[Obj.]" | know | content_part | 3 | none recorded | - | 0 | But your little ones, who you said would become a prey, I will bring in, and they shall **know** the land that you have rejected. |
| Deu 13:3 | know | H0853 אֵת et "[Obj.]" | know | content_part | 5 | none recorded | - | 0 | you shall not listen to the words of that prophet or that dreamer of dreams. For the Lord your God is testing you, to **know** whether you love the Lord your God with all your heart and with all your soul. |
| 2Ki 17:26 | know | H0853 אֵת et "[Obj.]" | know | content_part | 6 | none recorded | - | 0 | So the king of Assyria was told, “The nations that you have carried away and placed in the cities of Samaria do not **know** the law of the god of the land. Therefore he has sent lions among them, and behold, they are killing them, because they do not know the law of the god of the land.” |
| Isa 29:11 | can read | H0853 אֵת et "[Obj.]" | can read | content_part | 3 | none recorded | - | 0 | And the vision of all this has become to you like the words of a book that is sealed. When men give it to one who **can read**, saying, “ Read this,” he says, “I cannot, for it is sealed.” |
| Jer 3:15 | knowledge | H0853 אֵת et "[Obj.]" | knowledge | content_part | 3 | none recorded | - | 0 | “‘And I will give you shepherds after my own heart, who will feed you with **knowledge** and understanding. |
| Eze 11:10 | know | H0853 אֵת et "[Obj.]" | know | content_part | 3 | none recorded | - | 0 | You shall fall by the sword. I will judge you at the border of Israel, and you shall **know** that I am the Lord. |
| Eze 28:24 | know | H0853 אֵת et "[Obj.]" | know | content_part | 3 | none recorded | - | 0 | “And for the house of Israel there shall be no more a brier to prick or a thorn to hurt them among all their neighbors who have treated them with contempt. Then they will **know** that I am the Lord God. |
| Amo 3:2 | known | H0853 אֵת et "[Obj.]" | known | content_part | 3 | none recorded | - | 0 | “You only have I **known** of all the families of the earth; therefore I will punish you for all your iniquities. |
| Gen 45:1 | known | H0854 אֵת et "with" | known | content_part | 4 | none recorded | - | 0 | Then Joseph could not control himself before all those who stood by him. He cried, “Make everyone go out from me.” So no one stayed with him when Joseph made himself **known** to his brothers. |
| 1Ki 2:5 | know | H0859A אַתָּ֫ה at.tah "you [m.s.]" | know | content_part | 2 | none recorded | - | 0 | “Moreover, you also **know** what Joab the son of Zeruiah did to me, how he dealt with the two commanders of the armies of Israel, Abner the son of Ner, and Amasa the son of Jether, whom he killed, avenging in time of peace for blood that had been shed in war, and putting the blood of war on the belt around his waist and on the sandals on his feet. |
| Job 5:27 | know | H0859A אַתָּ֫ה at.tah "you [m.s.]" | know | content_part | 4 | none recorded | - | 0 | Behold, this we have searched out; it is true. Hear, and **know** it for your good.” |
| Hos 4:6 | knowledge | H0859A אַתָּ֫ה at.tah "you [m.s.]" | knowledge | content_part | 3 | none recorded | - | 0 | My people are destroyed for lack of **knowledge**; because you have rejected knowledge, I reject you from being a priest to me. And since you have forgotten the law of your God, I also will forget your children. |
| Deu 29:16 | know | H0859D אַתֶּם at.tem "you [m.p.]" | know | content_part | 2 | none recorded | - | 0 | “ You **know** how we lived in the land of Egypt, and how we came through the midst of the nations through which you passed. |
| Dan 4:17 | know | H1768 דִּי di "that" | know | content_part | 2 | none recorded | - | 0 | The sentence is by the decree of the watchers, the decision by the word of the holy ones, to the end that the living may **know** that the Most High rules the kingdom of men and gives it to whom he will and sets over it the lowliest of men.’ |
| Dan 4:25 | know | H1768 דִּי di "that" | know | content_part | 2 | none recorded | - | 0 | that you shall be driven from among men, and your dwelling shall be with the beasts of the field. You shall be made to eat grass like an ox, and you shall be wet with the dew of heaven, and seven periods of time shall pass over you, till you **know** that the Most High rules the kingdom of men and gives it to whom he will. |
| Dan 4:26 | know | H1768 דִּי di "that" | know | content_part | 2 | none recorded | - | 0 | And as it was commanded to leave the stump of the roots of the tree, your kingdom shall be confirmed for you from the time that you **know** that Heaven rules. |
| Dan 4:32 | know | H1768 דִּי di "that" | know | content_part | 2 | none recorded | - | 0 | and you shall be driven from among men, and your dwelling shall be with the beasts of the field. And you shall be made to eat grass like an ox, and seven periods of time shall pass over you, until you **know** that the Most High rules the kingdom of men and gives it to whom he will.” |
| Dan 5:21 | knew | H1768 דִּי di "that" | knew | content_part | 2 | none recorded | - | 0 | He was driven from among the children of mankind, and his mind was made like that of a beast, and his dwelling was with the wild donkeys. He was fed grass like an ox, and his body was wet with the dew of heaven, until he **knew** that the Most High God rules the kingdom of mankind and sets over it whom he will. |
| Dan 6:10 | knew | H1768 דִּי di "that" | knew | content_part | 3 | none recorded | - | 0 | When Daniel **knew** that the document had been signed, he went to his house where he had windows in his upper chamber open toward Jerusalem. He got down on his knees three times a day and prayed and gave thanks before his God, as he had done previously. |
| Job 10:7 | know | H1847 דַּ֫עַת da.at "knowledge" | know | content_part | 2 | none recorded | - | 0 | although you **know** that I am not guilty, and there is none to deliver out of your hand? |
| Jer 22:16 | know | H1847 דַּ֫עַת da.at "knowledge" | know | content_part | 3 | none recorded | 15594, 18013, 18070 | 0 | He judged the cause of the poor and needy; then it was well. Is not this to **know** me? declares the Lord. |
| Jos 8:14 | know | H1931 הוּא hu "he/she/it" | know | content_part | 3 | none recorded | - | 0 | And as soon as the king of Ai saw this, he and all his people, the men of the city, hurried and went out early to the appointed place toward the Arabah to meet Israel in battle. But he did not **know** that there was an ambush against him behind the city. |
| Jos 22:22 | know | H1931 הוּא hu "he/she/it" | know | content_part | 2 | none recorded | - | 0 | “The Mighty One, God, the Lord! The Mighty One, God, the Lord! He knows; and let Israel itself **know**! If it was in rebellion or in breach of faith against the Lord, do not spare us today |
| Judg 11:39 | known | H1931 הוּא hu "he/she/it" | known | content_part | 3 | none recorded | - | 0 | And at the end of two months, she returned to her father, who did with her according to his vow that he had made. She had never **known** a man, and it became a custom in Israel |
| Judg 16:20 | know | H1931 הוּא hu "he/she/it" | know | content_part | 3 | none recorded | - | 0 | And she said, “The Philistines are upon you, Samson!” And he awoke from his sleep and said, “I will go out as at other times and shake myself free.” But he did not **know** that the Lord had left him. |
| Psa 39:4 | know | H1931 הוּא hu "he/she/it" | know | content_part | 2 | none recorded | - | 0 | “O Lord, make me **know** my end and what is the measure of my days; let me know how fleeting I am! |
| Pro 24:12 | know | H1931 הוּא hu "he/she/it" | know | content_part | 3 | none recorded | - | 0 | If you say, “ Behold, we did not **know** this,” does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it, and will he not repay man according to his work? |
| Jer 22:16 | know | H1931 הוּא hu "he/she/it" | know | content_part | 3 | none recorded | - | 0 | He judged the cause of the poor and needy; then it was well. Is not this to **know** me? declares the Lord. |
| Hos 2:8 | know | H1931 הוּא hu "he/she/it" | know | content_part | 3 | none recorded | - | 0 | And she did not **know** that it was I who gave her the grain, the wine, and the oil, and who lavished on her silver and gold, which they used for Baal. |
| Hos 7:9 | knows | H1931 הוּא hu "he/she/it" | knows | content_part | 4 | none recorded | - | 0 | Strangers devour his strength, and he **knows** it not; gray hairs are sprinkled upon him, and he knows it not. |
| Zec 11:11 | knew | H1931 הוּא hu "he/she/it" | knew | content_part | 3 | none recorded | - | 0 | So it was annulled on that day, and the sheep traders, who were watching me, **knew** that it was the word of the Lord. |
| Zec 14:7 | known | H1931 הוּא hu "he/she/it" | known | content_part | 2 | none recorded | - | 0 | And there shall be a unique day, which is **known** to the Lord, neither day nor night, but at evening time there shall be light. |
| Lev 5:5 | realizes | H1961 הָיָה ha.yah "to be" | realizes | content_part | 2 | none recorded | - | 0 | when he **realizes** his guilt in any of these and confesses the sin he has committed, |
| Eze 7:4 | know | H1961 הָיָה ha.yah "to be" | know | content_part | 3 | none recorded | - | 0 | And my eye will not spare you, nor will I have pity, but I will punish you for your ways, while your abominations are in your midst. Then you will **know** that I am the Lord. |
| Eze 7:9 | know | H1961 הָיָה ha.yah "to be" | know | content_part | 3 | none recorded | - | 0 | And my eye will not spare, nor will I have pity. I will punish you according to your ways, while your abominations are in your midst. Then you will **know** that I am the Lord, who strikes. |
| Eze 12:20 | know | H1961 הָיָה ha.yah "to be" | know | content_part | 2 | none recorded | - | 0 | And the inhabited cities shall be laid waste, and the land shall become a desolation; and you shall **know** that I am the Lord.” |
| Eze 19:3 | learned | H1961 הָיָה ha.yah "to be" | learned | content_part | 2 | none recorded | - | 0 | And she brought up one of her cubs; he became a young lion, and he **learned** to catch prey; he devoured men. |
| Eze 19:6 | learned | H1961 הָיָה ha.yah "to be" | learned | content_part | 2 | none recorded | - | 0 | He prowled among the lions; he became a young lion, and he **learned** to catch prey; he devoured men, |
| Eze 35:4 | know | H1961 הָיָה ha.yah "to be" | know | content_part | 2 | none recorded | - | 0 | I will lay your cities waste, and you shall become a desolation, and you shall **know** that I am the Lord. |
| 2Ki 5:6 | know | H2009 הִנֵּה hin.neh "behold" | know | content_part | 3 | none recorded | - | 0 | And he brought the letter to the king of Israel, which read, “ When this letter reaches you, **know** that I have sent to you Naaman my servant, that you may cure him of his leprosy.” |
| 1Sa 6:9 | know | H2063 זֹאת zot "this" | know | content_part | 5 | none recorded | - | 0 | and watch. If it goes up on the way to its own land, to Beth-shemesh, then it is he who has done us this great harm, but if not, then we shall **know** that it is not his hand that struck us; it happened to us by coincidence.” |
| Jer 16:21 | know | H2063 זֹאת zot "this" | know | content_part | 3 | none recorded | - | 0 | “ Therefore, behold, I will make them **know**, this once I will make them know my power and my might, and they shall know that my name is the Lord.” |
| Gen 3:5 | knows | H3045 יָדַע ya.da "to know" | knows | content_part | 2 | none recorded | - | 0 | For God **knows** that when you eat of it your eyes will be opened, and you will be like God, knowing good and evil.” |
| Gen 19:8 | known | H3045 יָדַע ya.da "to know" | known | content_part | 2 | none recorded | - | 0 | Behold, I have two daughters who have not **known** any man. Let me bring them out to you, and do to them as you please. Only do nothing to these men, for they have come under the shelter of my roof.” |
| Gen 24:16 | known | H3045 יָדַע ya.da "to know" | known | content_part | 2 | none recorded | - | 0 | The young woman was very attractive in appearance, a maiden whom no man had **known**. She went down to the spring and filled her jar and came up. |
| Gen 38:26 | know her | H3045 יָדַע ya.da "to know" | know her | content_part | 4 | none recorded | - | 0 | Then Judah identified them and said, “She is more righteous than I, since I did not give her to my son Shelah.” And he did not **know her** again. |
| Gen 45:1 | known | H3045 יָדַע ya.da "to know" | known | content_part | 4 | none recorded | - | 0 | Then Joseph could not control himself before all those who stood by him. He cried, “Make everyone go out from me.” So no one stayed with him when Joseph made himself **known** to his brothers. |
| Lev 4:23 | known | H3045 יָדַע ya.da "to know" | known | content_part | 2 | none recorded | - | 0 | or the sin which he has committed is made **known** to him, he shall bring as his offering a goat, a male without blemish, |
| Lev 4:28 | known | H3045 יָדַע ya.da "to know" | known | content_part | 2 | none recorded | - | 0 | or the sin which he has committed is made **known** to him, he shall bring for his offering a goat, a female without blemish, for his sin which he has committed. |
| Num 12:6 | known | H3045 יָדַע ya.da "to know" | known | content_part | 3 | none recorded | - | 0 | And he said, “ Hear my words: If there is a prophet among you, I the Lord make myself **known** to him in a vision; I speak with him in a dream. |
| Jos 24:31 | known | H3045 יָדַע ya.da "to know" | known | content_part | 3 | none recorded | 19404, 19866 | 0 | Israel served the Lord all the days of Joshua, and all the days of the elders who outlived Joshua and had **known** all the work that the Lord did for Israel. |
| Judg 11:39 | known | H3045 יָדַע ya.da "to know" | known | content_part | 3 | none recorded | - | 0 | And at the end of two months, she returned to her father, who did with her according to his vow that he had made. She had never **known** a man, and it became a custom in Israel |
| Judg 13:21 | knew | H3045 יָדַע ya.da "to know" | knew | content_part | 3 | none recorded | - | 0 | The angel of the Lord appeared no more to Manoah and to his wife. Then Manoah **knew** that he was the angel of the Lord. |
| 1Sa 20:39 | knew | H3045 יָדַע ya.da "to know" | knew | content_part | 2 | none recorded | - | 0 | But the boy **knew** nothing. Only Jonathan and David knew the matter. |
| 1Ki 1:4 | knew | H3045 יָדַע ya.da "to know" | knew | content_part | 2 | none recorded | - | 0 | The young woman was very beautiful, and she was of service to the king and attended to him, but the king **knew** her not. |
| 1Ki 8:38 | knowing | H3045 יָדַע ya.da "to know" | knowing | content_part | 2 | none recorded | 16240 | 0 | whatever prayer, whatever plea is made by any man or by all your people Israel, each **knowing** the affliction of his own heart and stretching out his hands toward this house, |
| 2Ch 6:29 | knowing | H3045 יָדַע ya.da "to know" | knowing | content_part | 2 | none recorded | - | 0 | whatever prayer, whatever plea is made by any man or by all your people Israel, each **knowing** his own affliction and his own sorrow and stretching out his hands toward this house, |
| Job 11:11 | knows | H3045 יָדַע ya.da "to know" | knows | content_part | 3 | none recorded | - | 0 | For he **knows** worthless men; when he sees iniquity, will he not consider it? |
| Psa 1:6 | knows | H3045 יָדַע ya.da "to know" | knows | content_part | 2 | none recorded | - | 0 | for the Lord **knows** the way of the righteous, but the way of the wicked will perish. |
| Psa 73:22 | ignorant | H3045 יָדַע ya.da "to know" | ignorant | content_part | 3 | none recorded | 18115 | 0 | I was brutish and **ignorant**; I was like a beast toward you. |
| Isa 29:11 | can read | H3045 יָדַע ya.da "to know" | can read | content_part | 3 | none recorded | - | 0 | And the vision of all this has become to you like the words of a book that is sealed. When men give it to one who **can read**, saying, “ Read this,” he says, “I cannot, for it is sealed.” |
| Jer 16:13 | known | H3045 יָדַע ya.da "to know" | known | content_part | 3 | none recorded | - | 0 | Therefore I will hurl you out of this land into a land that neither you nor your fathers have **known**, and there you shall serve other gods day and night, for I will show you no favor.’ |
| Eze 20:9 | known | H3045 יָדַע ya.da "to know" | known | content_part | 3 | none recorded | - | 0 | But I acted for the sake of my name, that it should not be profaned in the sight of the nations among whom they lived, in whose sight I made myself **known** to them in bringing them out of the land of Egypt. |
| Hos 7:9 | knows | H3045 יָדַע ya.da "to know" | knows | content_part | 4 | none recorded | 15087 | 0 | Strangers devour his strength, and he **knows** it not; gray hairs are sprinkled upon him, and he knows it not. |
| Hos 7:9 | knows | H3045 יָדַע ya.da "to know" | knows | content_part | 5 | none recorded | 15087 | 0 | Strangers devour his strength, and he **knows** it not; gray hairs are sprinkled upon him, and he knows it not. |
| Hos 8:4 | knew | H3045 יָדַע ya.da "to know" | knew | content_part | 3 | none recorded | 19122 | 0 | They made kings, but not through me. They set up princes, but I **knew** it not. With their silver and gold they made idols for their own destruction. |
| Amo 3:2 | known | H3045 יָדַע ya.da "to know" | known | content_part | 3 | none recorded | - | 0 | “You only have I **known** of all the families of the earth; therefore I will punish you for all your iniquities. |
| Jon 3:9 | knows | H3045 יָדַע ya.da "to know" | knows | content_part | 2 | none recorded | 13069, 13151, 13176, 13211, 13280, 14765, 14840 | 0 | Who **knows**? God may turn and relent and turn from his fierce anger, so that we may not perish.” |
| Zec 11:11 | knew | H3045 יָדַע ya.da "to know" | knew | content_part | 3 | none recorded | - | 0 | So it was annulled on that day, and the sheep traders, who were watching me, **knew** that it was the word of the Lord. |
| Zec 14:7 | known | H3045 יָדַע ya.da "to know" | known | content_part | 2 | none recorded | - | 0 | And there shall be a unique day, which is **known** to the Lord, neither day nor night, but at evening time there shall be light. |
| Ezr 5:8 | known | H3046 יְדַע ye.da "to know" | known | content_part | 2 | none recorded | - | 33 | Be it **known** to the king that we went to the province of Judah, to the house of the great God. It is being built with huge stones, and timber is laid in the walls. This work goes on diligently and prospers in their hands. |
| Dan 5:21 | knew | H3046 יְדַע ye.da "to know" | knew | content_part | 2 | none recorded | 15113, 16735, 17067 | 0 | He was driven from among the children of mankind, and his mind was made like that of a beast, and his dwelling was with the wild donkeys. He was fed grass like an ox, and his body was wet with the dew of heaven, until he **knew** that the Most High God rules the kingdom of mankind and sets over it whom he will. |
| Dan 6:10 | knew | H3046 יְדַע ye.da "to know" | knew | content_part | 3 | none recorded | - | 0 | When Daniel **knew** that the document had been signed, he went to his house where he had windows in his upper chamber open toward Jerusalem. He got down on his knees three times a day and prayed and gave thanks before his God, as he had done previously. |
| Est 1:17 | made known | H3318O יָצָא ya.tsa "to come out: speak" | made known | content_part | 2 | none recorded | - | 0 | For the queen’s behavior will be **made known** to all women, causing them to look at their husbands with contempt, since they will say, ‘ King Ahasuerus commanded Queen Vashti to be brought before him, and she did not come.’ |
| Gen 47:6 | know | H3426 יֵשׁ yesh "there" | know | content_part | 2 | none recorded | - | 0 | The land of Egypt is before you. Settle your father and your brothers in the best of the land. Let them settle in the land of Goshen, and if you **know** any able men among them, put them in charge of my livestock.” |
| Gen 3:5 | knows | H3588A כִּי ki "for" | knows | content_part | 2 | none recorded | - | 0 | For God **knows** that when you eat of it your eyes will be opened, and you will be like God, knowing good and evil.” |
| Exo 3:7 | know | H3588A כִּי ki "for" | know | content_part | 3 | none recorded | - | 0 | Then the Lord said, “I have surely seen the affliction of my people who are in Egypt and have heard their cry because of their taskmasters. I **know** their sufferings, |
| Lev 5:5 | realizes | H3588A כִּי ki "for" | realizes | content_part | 2 | none recorded | - | 0 | when he **realizes** his guilt in any of these and confesses the sin he has committed, |
| Num 22:6 | know | H3588A כִּי ki "for" | know | content_part | 2 | none recorded | - | 0 | Come now, curse this people for me, since they are too mighty for me. Perhaps I shall be able to defeat them and drive them from the land, for I **know** that he whom you bless is blessed, and he whom you curse is cursed.” |
| Judg 13:16 | know | H3588A כִּי ki "for" | know | content_part | 3 | none recorded | - | 0 | And the angel of the Lord said to Manoah, “If you detain me, I will not eat of your food. But if you prepare a burnt offering, then offer it to the Lord.” (For Manoah did not **know** that he was the angel of the Lord.) |
| Rut 3:11 | know | H3588A כִּי ki "for" | know | content_part | 4 | none recorded | - | 0 | And now, my daughter, do not fear. I will do for you all that you ask, for all my fellow townsmen **know** that you are a worthy woman. |
| 1Ki 8:39 | know | H3588A כִּי ki "for" | know | content_part | 3 | none recorded | - | 0 | then hear in heaven your dwelling place and forgive and act and render to each whose heart you **know**, according to all his ways ( for you, you only, know the hearts of all the children of mankind ), |
| Est 1:17 | made known | H3588A כִּי ki "for" | made known | content_part | 2 | none recorded | - | 0 | For the queen’s behavior will be **made known** to all women, causing them to look at their husbands with contempt, since they will say, ‘ King Ahasuerus commanded Queen Vashti to be brought before him, and she did not come.’ |
| Est 3:6 | made known | H3588A כִּי ki "for" | made known | content_part | 3 | none recorded | - | 0 | But he disdained to lay hands on Mordecai alone. So, as they had **made known** to him the people of Mordecai, Haman sought to destroy all the Jews, the people of Mordecai, throughout the whole kingdom of Ahasuerus. |
| Job 11:11 | knows | H3588A כִּי ki "for" | knows | content_part | 3 | none recorded | - | 0 | For he **knows** worthless men; when he sees iniquity, will he not consider it? |
| Job 32:22 | know | H3588A כִּי ki "for" | know | content_part | 2 | none recorded | - | 0 | For I do not **know** how to flatter, else my Maker would soon take me away. |
| Psa 1:6 | knows | H3588A כִּי ki "for" | knows | content_part | 2 | none recorded | - | 0 | for the Lord **knows** the way of the righteous, but the way of the wicked will perish. |
| Psa 135:5 | know | H3588A כִּי ki "for" | know | content_part | 2 | none recorded | - | 0 | For I **know** that the Lord is great, and that our Lord is above all gods. |
| Jer 11:19 | know | H3588A כִּי ki "for" | know | content_part | 2 | none recorded | - | 0 | But I was like a gentle lamb led to the slaughter. I did not **know** it was against me they devised schemes, saying, “Let us destroy the tree with its fruit, let us cut him off from the land of the living, that his name be remembered no more.” |
| Gen 24:16 | known | H3808 לֹא lo "not" | known | content_part | 2 | none recorded | - | 0 | The young woman was very attractive in appearance, a maiden whom no man had **known**. She went down to the spring and filled her jar and came up. |
| Deu 8:3 | know | H3808 לֹא lo "not" | know | content_part | 3 | none recorded | - | 0 | And he humbled you and let you hunger and fed you with manna, which you did not **know**, nor did your fathers know, that he might make you know that man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| 1Sa 20:39 | knew | H3808 לֹא lo "not" | knew | content_part | 2 | none recorded | - | 0 | But the boy **knew** nothing. Only Jonathan and David knew the matter. |
| 1Ki 1:4 | knew | H3808 לֹא lo "not" | knew | content_part | 2 | none recorded | - | 0 | The young woman was very beautiful, and she was of service to the king and attended to him, but the king **knew** her not. |
| Job 9:5 | know | H3808 לֹא lo "not" | know | content_part | 3 | none recorded | - | 0 | he who removes mountains, and they **know** it not, when he overturns them in his anger, |
| Psa 73:22 | ignorant | H3808 לֹא lo "not" | ignorant | content_part | 3 | none recorded | - | 0 | I was brutish and **ignorant**; I was like a beast toward you. |
| Jer 16:13 | known | H3808 לֹא lo "not" | known | content_part | 3 | none recorded | - | 0 | Therefore I will hurl you out of this land into a land that neither you nor your fathers have **known**, and there you shall serve other gods day and night, for I will show you no favor.’ |
| Hos 5:4 | know | H3808 לֹא lo "not" | know | content_part | 2 | none recorded | - | 0 | Their deeds do not permit them to return to their God. For the spirit of whoredom is within them, and they **know** not the Lord. |
| Hos 7:9 | knows | H3808 לֹא lo "not" | knows | content_part | 4 | none recorded | - | 0 | Strangers devour his strength, and he **knows** it not; gray hairs are sprinkled upon him, and he knows it not. |
| Hos 7:9 | knows | H3808 לֹא lo "not" | knows | content_part | 5 | none recorded | - | 0 | Strangers devour his strength, and he **knows** it not; gray hairs are sprinkled upon him, and he knows it not. |
| Hos 8:4 | knew | H3808 לֹא lo "not" | knew | content_part | 3 | none recorded | - | 0 | They made kings, but not through me. They set up princes, but I **knew** it not. With their silver and gold they made idols for their own destruction. |
| Hos 13:4 | know | H3808 לֹא lo "not" | know | content_part | 3 | none recorded | - | 0 | But I am the Lord your God from the land of Egypt; you **know** no God but me, and besides me there is no savior. |
| Eze 19:3 | learned | H3925H לָמַד la.mad "to learn: learn" | learned | content_part | 2 | none recorded | - | 0 | And she brought up one of her cubs; he became a young lion, and he **learned** to catch prey; he devoured men. |
| Eze 19:6 | learned | H3925H לָמַד la.mad "to learn: learn" | learned | content_part | 2 | none recorded | - | 0 | He prowled among the lions; he became a young lion, and he **learned** to catch prey; he devoured men, |
| Lev 23:43 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 2 | none recorded | - | 0 | that your generations may **know** that I made the people of Israel dwell in booths when I brought them out of the land of Egypt: I am the Lord your God.” |
| Deu 8:3 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 3 | none recorded | - | 0 | And he humbled you and let you hunger and fed you with manna, which you did not **know**, nor did your fathers know, that he might make you know that man does not live by bread alone, but man lives by every word that comes from the mouth of the Lord. |
| Deu 31:12 | learn | H4616 מַ֫עַן ma.an "because" | learn | content_part | 3 | none recorded | - | 0 | Assemble the people, men, women, and little ones, and the sojourner within your towns, that they may hear and **learn** to fear the Lord your God, and be careful to do all the words of this law, |
| Jos 3:4 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 4 | none recorded | - | 0 | Yet there shall be a distance between you and it, about 2,000 cubits in length. Do not come near it, in order that you may **know** the way you shall go, for you have not passed this way before.” |
| Jos 4:24 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 2 | none recorded | - | 0 | so that all the peoples of the earth may **know** that the hand of the Lord is mighty, that you may fear the Lord your God forever.” |
| 1Ki 8:43 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 2 | none recorded | - | 0 | hear in heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may **know** your name and fear you, as do your people Israel, and that they may know that this house that I have built is called by your name. |
| 1Ki 8:60 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 2 | none recorded | - | 0 | that all the peoples of the earth may **know** that the Lord is God; there is no other. |
| Mic 6:5 | know | H4616 מַ֫עַן ma.an "because" | know | content_part | 2 | none recorded | - | 0 | O my people, remember what Balak king of Moab devised, and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal, that you may **know** the righteous acts of the Lord.” |
| 2Ki 12:5 | discovered | H4672 מָצָא ma.tsa "to find" | discovered | content_part | 2 | none recorded | - | 0 | let the priests take, each from his donor, and let them repair the house wherever any need of repairs is **discovered**.” |
| Est 3:6 | made known | H5046 נָגַד na.gad "to tell" | made known | content_part | 3 | none recorded | - | 0 | But he disdained to lay hands on Mordecai alone. So, as they had **made known** to him the people of Mordecai, Haman sought to destroy all the Jews, the people of Mordecai, throughout the whole kingdom of Ahasuerus. |
| Exo 9:14 | know | H5668 עָבוּר a.vur "for the sake of" | know | content_part | 4 | none recorded | - | 0 | For this time I will send all my plagues on you yourself, and on your servants and your people, so that you may **know** that there is none like me in all the earth. |
| Gen 38:26 | know her | H5750 עוֹד od "still" | know her | content_part | 4 | none recorded | - | 0 | Then Judah identified them and said, “She is more righteous than I, since I did not give her to my son Shelah.” And he did not **know her** again. |
| 1Sa 23:22 | know | H5750 עוֹד od "still" | Know | content_part | 2 | none recorded | - | 0 | Go, make yet more sure. **Know** and see the place where his foot is, and who has seen him there, for it is told me that he is very cunning. |
| Job 10:7 | know | H5921A עַל al "upon" | know | content_part | 2 | none recorded | - | 0 | although you **know** that I am not guilty, and there is none to deliver out of your hand? |
| Gen 40:22 | interpreted | H6622 פָּתַר pa.tar "to interpret" | interpreted | content_part | 3 | none recorded | - | 0 | But he hanged the chief baker, as Joseph had **interpreted** to them. |
| Job 11:11 | knows | H7723G שָׁוְא shav "vanity: false" | knows | content_part | 3 | none recorded | - | 0 | For he **knows** worthless men; when he sees iniquity, will he not consider it? |
| 2Ki 12:5 | discovered | H8033G שָׁם sham "there" | discovered | content_part | 2 | none recorded | - | 0 | let the priests take, each from his donor, and let them repair the house wherever any need of repairs is **discovered**.” |
| Num 14:34 | know | H8141 שָׁנָה sha.nah "year" | know | content_part | 2 | none recorded | - | 0 | According to the number of the days in which you spied out the land, forty days, a year for each day, you shall bear your iniquity forty years, and you shall **know** my displeasure.’ |

## 4. What the study has recorded for these occurrences

Of 1855 occurrences, 0 have an engagement observation and 1855 have none recorded. There are 588 live observations on them (0 engagement, 394 of other recorded stages, 194 of the retired catalogue stages) and 59 withdrawn.

### 4.1 Engagement: what each word does for the inner being (0 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

_no engagement observation covers these occurrences_

### 4.2 Other recorded observations (394)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 20784** (Analysis_phase_1, tag face, status draft): The verb is to know, here to come to know beforehand (tree H3045 1a1a 'to know, learn to know').
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20787** (Analysis_phase_1, tag qualification, status draft): The infinitive before the finite verb strengthens the question: in any way at all.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20789** (Analysis_phase_1, tag statement, status draft): The question implies that they could not have known: a refusal of that knowledge.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20793** (Analysis_phase_1, tag statement, status draft): What they say they could not know is what he would say next.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20794** (Analysis_phase_1, tag statement, status draft): What he would say, bring your brother down, is a command to act.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20797** (Analysis_phase_1, tag party, status draft): The brothers speak of the man and of what he would say.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20798** (Analysis_phase_1, tag statement, status draft): All of this is the brothers' answer to their father Israel, who has just reproached them for telling the man of another brother (Gen 43:6).
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20802** (Analysis_phase_1, tag statement, status draft): The brothers say they could not have known beforehand what he would say.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20803** (Analysis_phase_1, tag link, status draft): The man questioned them; what they told was in answer; they could not know that he would then say, bring your brother down.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20804** (Analysis_phase_1, tag link, status draft): The brothers set their telling between his questioning and his demand, as the reason they could not have known.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 20805** (Analysis_phase_1, tag statement, status draft): Discovery: whether the questioning had the purpose that its later demand shows, the verse does not say; the passage is needed.
  - applies to 1 occurrence(s): Gen 43:7 (know)
- **Observation 21254** (Analysis_phase_1, tag face, status draft): Know here is learning an outcome that cannot be seen beforehand (tree H3045 1a1a 'to know, learn to know').
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21256** (Analysis_phase_1, tag statement, status draft): The knowing is a pursuit: the men want to learn how the journey will go.
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21258** (Analysis_phase_1, tag statement, status draft): What they want to know is whether the journey will succeed.
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21260** (Analysis_phase_1, tag party, status draft): The men themselves are the ones who want to know; the Levite and God are the means.
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21261** (Analysis_phase_1, tag statement, status draft): The men have met the young Levite at Micah's house and heard that he is Micah's priest (Judg 18:3-4).
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21263** (Analysis_phase_1, tag statement, status draft): They intend by the inquiry to know how the journey will go.
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21264** (Analysis_phase_1, tag link, status draft): They tell him to inquire so that they may know; the priest answers in the next verse (Judg 18:6).
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 21266** (Analysis_phase_1, tag statement, status draft): Discovery: the answer the priest gives is in the next verse (Judg 18:6); the passage is needed.
  - applies to 1 occurrence(s): Judg 18:5 (know)
- **Observation 12598** (prior-capture, tag statement, status draft): The fear of God, named by what it is: "The fear of the Lord is the beginning of knowledge"; "The fear of the Lord is hatred of evil"; "a fountain of life"; "It was a covenant of fear, and he feared me"
  - applies to 1 occurrence(s): Pro 1:7 (knowledge)
- **Observation 12670** (prior-capture, tag statement, status draft): Fear leads to persuading others: "knowing the fear of the Lord, we persuade others"
  - applies to 1 occurrence(s): 2Cor 5:11 (knowing)
- **Observation 12676** (prior-capture, tag link, status draft): Fear and Knowing and understanding (M15): The fear of the Lord as "the beginning of knowledge"; learned by hearing; "that you might know" (verses shared or near: 73 / 31).
  - applies to 2 occurrence(s): Deu 4:35 (know), Pro 1:7 (knowledge)
- **Observation 12703** (prior-capture, tag face, status draft): Face G. Dread laid on nations, peoples and creatures (8 / 8 hits and verses; surfaces terror · dread · fear · feared): Laid by God, on cities, peoples, beasts; once so that the nations may know they are men.
  - applies to 2 occurrence(s): Jos 2:9 (know), Psa 9:20 (know)
- **Observation 12880** (prior-capture, tag statement, status draft): The heavy hand is felt from beneath, and the text corrects the feeling: "he does not afflict from his heart"; "I knew you to be a hard man", said from fear and condemned; the heaviness ended at confession.
  - applies to 2 occurrence(s): Mat 25:24 (knew), Mat 25:26 (knew)
- **Observation 13027** (prior-capture, tag statement, status draft): God's anger leads to knowing; understanding later; not taken to heart: "And they shall know that I am the Lord"; "In the latter days you will understand it clearly"; "it burned him up, but he did not take it to heart".
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 13068** (prior-capture, tag statement, status draft): A person responds to God's anger by know: "And they shall know that I am the Lord" (Eze 5:13).
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 13069** (prior-capture, tag statement, status draft): A person responds to God's anger by return without a guarantee: "Who knows? God may turn and relent" (Jon 3:9).
  - applies to 1 occurrence(s): Jon 3:9 (knows)
- **Observation 13129** (prior-capture, tag link, status draft): Sequence in Jos 7; 22:10–34: one man takes → anger on all → defeat → offender removed → anger turns → the memory drives a later confrontation → answer "He knows".
  - applies to 1 occurrence(s): Jos 22:22 (knows)
- **Observation 13151** (prior-capture, tag link, status draft): Sequence in Joe 2:11–14; Jon 3:5–10: the day, "who can endure it?" → return with the heart, fasting, sackcloth → the creed (Joel) or the preached word (Nineveh) → "Who knows?" → (Jonah) God relented.
  - applies to 2 occurrence(s): Joe 2:14 (knows), Jon 3:9 (knows)
- **Observation 13163** (prior-capture, tag link, status draft): Anger and Knowing (M15); being heard (M41): Kindled on hearing; its stated end is knowing ("they shall know that I am the Lord"); understanding "in the latter days"; the book heard and the wrath recognised; ears stopped.
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 13176** (prior-capture, tag link, status draft): Anger and Turning and repentance (M11): "Who knows? God may turn and relent"; "when he humbled himself the wrath of the Lord turned from him"; "Bear fruit in keeping with repentance"; godly grief "produces a repentance".
  - applies to 1 occurrence(s): Jon 3:9 (knows)
- **Observation 13184** (prior-capture, tag link, status draft): Anger and Knowing (M15); hearing (M41), side by side with fear: fear side, the fear of the Lord as the beginning of knowledge; fear comes by hearing (Pro 1:7; Act 5:5); anger side, kindled on hearing; its stated end is knowing (Num 11:1; Eze 5:13).
  - applies to 1 occurrence(s): Pro 1:7 (knowledge)
- **Observation 13208** (prior-capture, tag statement, status draft): A spirit as the angry party: the devil's great wrath "because he knows that his time is short" (Rev 12:12).
  - applies to 1 occurrence(s): Rev 12:12 (knows)
- **Observation 13211** (prior-capture, tag statement, status draft): The fierce anger is the anger that turns (ḥārôn with "turn" in 12 of 40 verses); Josiah's whole-hearted turning beside the burning not turned (2Ki 23:25–26); turning asked for without a guarantee ("It may be", Jer 36:7; "perhaps", Zep 2:3; "Who knows?", Jon 3:9); inner acts named as turning it (humbling, a resolve in the heart).
  - applies to 1 occurrence(s): Jon 3:9 (knows)
- **Observation 13216** (prior-capture, tag statement, status draft): The anger's stated outcome is knowing or understanding ("they shall know that I am the Lord", Eze 5:13; "In the latter days you will understand it clearly", Jer 23:20).
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 13280** (prior-capture, tag statement, status draft): F.7: What emerged: Turning is asked for without a guarantee ("It may be", "perhaps", "Who knows?", AG-46).; What it changes elsewhere: Extends U2 §56 from two verses to four. Ch 13 has Jon 3:9 only.; Where: Ch 13.
  - applies to 1 occurrence(s): Jon 3:9 (knows)
- **Observation 13287** (prior-capture, tag link, status draft): anger spent → "they shall know that I am the Lord" (Eze 5:13).
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 13328** (prior-capture, tag face, status draft): Face 2E. Spent, satisfied, then calm: Hits / verses: 6 / 5; Toward: Jerusalem, Israel; Other parties named: "they shall know that I am the Lord"; Example verses: Eze 5:13; Eze 16:42; Eze 21:17; Eze 24:13.
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 13372** (prior-capture, tag link, status draft): melted in the furnace → "you shall know that I am the Lord" (Eze 22:22).
  - applies to 1 occurrence(s): Eze 22:22 (know)
- **Observation 13376** (prior-capture, tag link, status draft): deeds → repayment, wrath (Isa 59:18); vengeance → "they will know" (Eze 25:17).
  - applies to 1 occurrence(s): Eze 25:17 (know)
- **Observation 13390** (prior-capture, tag link, status draft): devoured Jacob → "Pour out your wrath on the nations" (Jer 10:25); consumed → "that they may know that God rules" (Psa 59:13).
  - applies to 2 occurrence(s): Psa 59:13 (know), Jer 10:25 (know)
- **Observation 13392** (prior-capture, tag link, status draft): wrath → punishment of the sword → "that you may know there is a judgment" (Job 19:29); wrath → entice into scoffing ("lest", Job 36:18).
  - applies to 1 occurrence(s): Job 19:29 (know)
- **Observation 13480** (prior-capture, tag link, status draft): angry → know that harm is determined (1Sa 20:7).
  - applies to 1 occurrence(s): 1Sa 20:7 (know)
- **Observation 13496** (prior-capture, tag statement, status draft): The hand of the Lord stands with the anger (OT-06): "the hand of the Lord shall be known to his servants, and he shall show his indignation against his enemies" (Isa 66:14, AG-169).
  - applies to 1 occurrence(s): Isa 66:14 (known)
- **Observation 13740** (prior-capture, tag statement, status draft): Jon 4:1-3: "it displeased Jonah exceedingly, and he was angry. And he prayed ... I knew that you are a gracious God ... slow to anger ... please take my life from me": Jonah quotes God's own "slow to anger" against him, so the anger comes from a creed he knows well; God's reply, "Do you do well to be angry?" (4:4, 9), leads to "angry enough to die".
  - applies to 1 occurrence(s): Jon 4:2 (knew)
- **Observation 13766** (prior-capture, tag statement, status draft): A human says God is hard, and is wrong: "Master, I knew you to be a hard man, reaping where you did not sow" (Mat 25:24), the wicked servant's view of the parable's master, which the parable condemns; in Mal 3:13 the Lord says "Your words have been hard against me": the hardness is in the human speech about God.
  - applies to 1 occurrence(s): Mat 25:24 (knew)
- **Observation 13772** (prior-capture, tag statement, status draft): The psalmist: "day and night your hand was heavy upon me; my strength was dried up" (Psa 32:4); the context gives the cause inside the psalmist, "when I kept silent, my bones wasted away" (32:3); the heaviness ends at confession, "I acknowledged my sin ... and you forgave" (32:5); the psalm opens with the outcome God intended: "Blessed is the one whose transgression is forgiven" (32:1).
  - applies to 1 occurrence(s): Psa 32:5 (acknowledged)
- **Observation 13774** (prior-capture, tag statement, status draft): Mat 25:24-26: "Master, I knew you to be a hard man"; the servant names the source of his perception himself, "so I was afraid, and I went and hid your talent" (25:25); the master answers "You wicked and slothful servant!" (25:26): the perception of hardness is born of fear, and the parable condemns it.
  - applies to 2 occurrence(s): Mat 25:24 (knew), Mat 25:26 (knew)
- **Observation 13876** (prior-capture, tag statement, status draft): Job tells his friends "be afraid of the sword, for wrath brings the punishment of the sword, that you may know there is a judgment" (Job 19:29) straight after "I know that my Redeemer lives" and "My heart faints within me!" (19:25, 27), answering "How we will pursue him!" and "The root of the matter is found in him" (19:28); he tells his accusers to fear, and the reason he gives is that there is a judgment.
  - applies to 2 occurrence(s): Job 19:25 (know), Job 19:29 (know)
- **Observation 13888** (prior-capture, tag statement, status draft): Deu 31:29, "after my death you will surely act corruptly and turn aside from the way that I have commanded you ... provoking him to anger through the work of your hands": Moses grounds what he knows in what he has seen, "For I know how rebellious and stubborn you are ... How much more after my death!" (31:27); the provocation is named as "the work of your hands".
  - applies to 2 occurrence(s): Deu 31:27 (know), Deu 31:29 (know)
- **Observation 13918** (prior-capture, tag statement, status draft): Ecc 1:16–17 "I said in my heart … I applied my heart to know". Genuine. The bearer's own (E v2 §1.3; B v3 §1.2, §1.11; C v3 §10). New here is only the link: the heart that seeks knowledge comes before the vexation that knowledge brings.
  - applies to 2 occurrence(s): Ecc 1:16 (knowledge), Ecc 1:17 (know)
- **Observation 13921** (prior-capture, tag statement, status draft): Psa 31:7 "you have known the distress of my soul". Genuine.
  - applies to 1 occurrence(s): Psa 31:7 (known)
- **Observation 14038** (prior-capture, tag statement, status draft): How it co-exists. With the tongue, which carries it (Hos 7:16; Isa 16:6 "boasting"). With the prophet's own wailing: "Therefore I wail for Moab … More than for Jazer I weep for you" (Jer 48:31–32); "let Moab wail for Moab" (Isa 16:7). God knows the insolence ("I know his insolence", Jer 48:30), and the prophet weeps over its end.
  - applies to 1 occurrence(s): Jer 48:30 (know)
- **Observation 14065** (prior-capture, tag statement, status draft): Stubbornness, and not believing. "they would not listen, but were stubborn, as their fathers had been, who did not believe in the Lord their God" (2Ki 17:14); "I know how rebellious and stubborn you are" (Deu 31:27).
  - applies to 1 occurrence(s): Deu 31:27 (know)
- **Observation 14067** (prior-capture, tag statement, status draft): What is known in the heart. Joshua ties the threat to what the people already know: "you know in your hearts and souls, all of you, that not one word has failed of all the good things … so the Lord will bring upon you all the evil things" (Jos 23:14–15). The heart's own knowledge of God's faithfulness is made the ground for believing the warning.
  - applies to 1 occurrence(s): Jos 23:14 (know)
- **Observation 14070** (prior-capture, tag statement, status draft): Jos 23:14 "you know in your hearts and souls". B v3 §1.1 ("the heart as the knower").
  - applies to 1 occurrence(s): Jos 23:14 (know)
- **Observation 14080** (prior-capture, tag statement, status draft): Silenced: Amaziah to the prophet: "Have we made you a royal counselor? Stop! Why should you be struck down?" (2Ch 25:16). The prophet stops, but says: "I know that God has determined to destroy you, because you have done this and have not listened to my counsel.".
  - applies to 1 occurrence(s): 2Ch 25:16 (know)
- **Observation 14090** (prior-capture, tag statement, status draft): The accused answer by appealing to God's knowledge: "The Mighty One, God, the Lord! He knows; and let Israel itself know! If it was in rebellion … do not spare us today" (Jos 22:22).
  - applies to 2 occurrence(s): Jos 22:22 (knows), Jos 22:22 (know)
- **Observation 14099** (prior-capture, tag statement, status draft): Manasseh (context of §20): "when he was in distress, he entreated the favor of the Lord his God and humbled himself greatly … Then Manasseh knew that the Lord was God" (2Ch 33:12–13).
  - applies to 1 occurrence(s): 2Ch 33:13 (knew)
- **Observation 14102** (prior-capture, tag statement, status draft): Humbling that is partial. Rehoboam is spared destruction but made to serve Shishak, "that they may know my service and the service of the kingdoms" (2Ch 12:8). Bronze shields replace gold (12:10). And "he did evil, for he did not set his heart to seek the Lord" (12:14). The humbling turned the wrath, and the heart was still not set.
  - applies to 1 occurrence(s): 2Ch 12:8 (know)
- **Observation 14140** (prior-capture, tag statement, status draft): Babylon: "I set a snare for you and you were taken, O Babylon, and you did not know it … because you opposed the Lord" (Jer 50:24).
  - applies to 1 occurrence(s): Jer 50:24 (know)
- **Observation 14187** (prior-capture, tag statement, status draft): Part 2 verses: what they add: Anger lodges, and where it lodges is named. "Be not quick in your spirit to become angry, for anger lodges in the heart of fools" (Ecc 7:9). This joins Job 36:13 ("cherish anger"). Anger that stays has a lodging, and the lodging is the fool's. The verse before sets up the pair: "the patient in spirit is better than the proud in spirit" (7:8); Its duration is limited to a day: "Be angry and do not sin; do not let the sun go down on your anger, and give no opportunity to the devil" (Eph 4:26–27). Where Gen 27 waited years for anger to turn away, the NT sets a limit of one day. The reason given is what anger left overnight opens: "opportunity to the devil"; It repe ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 12:16 (known)
- **Observation 14199** (prior-capture, tag statement, status draft): What it does to those beneath it: Pleading against it before it rises:; Judah: "let not your anger burn against your servant, for you are like Pharaoh himself" (Gen 44:18). The plea is a long retelling of the father's love (44:19–21 onward); Rachel: "Let not my lord be angry that I cannot rise before you, for the way of women is upon me" (Gen 31:35). The plea for no anger covers a concealment: she is sitting on the stolen gods (31:34); Reading it as a sign: "If he says, 'Good!' it will be well with your servant, but if he is angry, then know that harm is determined by him" (1Sa 20:7). Saul's anger is to be read as the evidence of Saul's intent. Jonathan's knowledge follows the same path: aft ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): 1Sa 20:7 (know), 1Sa 20:33 (knew), 2Sa 11:20 (know), Est 2:22 (knowledge)
- **Observation 14220** (prior-capture, tag statement, status draft): Where it comes from: A rival's provocation, "because the Lord had closed her womb" (1Sa 1:6); calamity and God's "arrows" (Job 6:2, 4); being made "a byword of the peoples" (Job 17:6); dreams with "no one to interpret them" (Gen 40:8).
  - applies to 1 occurrence(s): Gen 40:8 (interpret)
- **Observation 14224** (prior-capture, tag statement, status draft): Part 2 verses: what they add. Three new strands: (a) The eye wasting, as in Job 17:7; "My eye wastes away because of grief; it grows weak because of all my foes" (Psa 6:7), after "every night I flood my bed with tears" (6:6); "My eye is wasted from grief; my soul and my body also. For my life is spent with sorrow" (Psa 31:9–10); The eye is where ka'as shows in the body, in all three texts (Job 17:7; Psa 6:7; 31:9); What turns Psa 6 round is being heard: "the Lord has heard the sound of my weeping. The Lord has heard my plea" (6:8–9). In Psa 10:14, "you do see, for you note mischief and vexation, that you may take it into your hands; to you the helpless commits himself". The vexation is seen ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Ecc 1:17 (know), Ecc 1:18 (knowledge), Ecc 11:9 (know)
- **Observation 14239** (prior-capture, tag statement, status draft): How it co-exists: With appeal to God against those who resist: "Moses was very angry and said to the Lord, 'Do not respect their offering. I have not taken one donkey from them'" (Num 16:15). The anger is carried straight into a plea of innocence before God; With the one beneath deflecting it: Aaron, "Let not the anger of my lord burn hot. You know the people, that they are set on evil … I threw it into the fire, and out came this calf" (Exo 32:22–24). Deflection by blaming the people and making the act passive; With being answered: Aaron's reply to the Lev 10 rebuke ("such things as these have happened to me! If I had eaten the sin offering today, would the Lord have approved?", 10:19) meet ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Exo 32:22 (know), Exo 32:23 (know)
- **Observation 14250** (prior-capture, tag statement, status draft): Part 2 verses: what they add. The occasion widens from God striking to God's mercy, and to the consequences of one's own folly: Jonah: anger at God's mercy; The occasion: "When God saw what they did, how they turned from their evil way, God relented of the disaster" (Jon 3:10). "But it displeased Jonah exceedingly, and he was angry" (4:1); He quotes God's own character against him: "I knew that you are a gracious God and merciful, slow to anger and abounding in steadfast love, and relenting from disaster" (4:2). Pilot §2.1 read this. The anger is at the very attribute that is the opposite of anger; It asks to die: "please take my life from me, for it is better for me to die than to live" (4: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jon 4:2 (knew)
- **Observation 14252** (prior-capture, tag statement, status draft): What it does: Balaam cannot pronounce it: "How can I curse whom God has not cursed? How can I denounce whom the Lord has not denounced?" (Num 23:8). Human denunciation is shown to be derivative: it cannot go beyond God's; God offers it ironically to Job: "Pour out the overflowings of your anger, and look on everyone who is proud and abase him" (Job 40:11). This comes inside the challenge, "Have you an arm like God …?" (40:9), and "Then will I also acknowledge to you that your own right hand can save you" (40:14). Anger that abases the proud belongs to the one who can save by his own right hand; Job warns his friends that their own wrath is answerable: "be afraid of the sword, for wrath bring ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 19:29 (know)
- **Observation 14271** (prior-capture, tag statement, status draft): What it does: It reads the rival's heart as evil: Eliab, "I know your presumption and the evil of your heart, for you have come down to see the battle" (1Sa 17:28); It reckons the rival's future: Saul, "They have ascribed to David ten thousands, and to me they have ascribed thousands, and what more can he have but the kingdom?" (18:8); It attacks one's own son as the rival's ally: "You son of a perverse, rebellious woman … as long as the son of Jesse lives … neither you nor your kingdom shall be established" (20:30–31); It jeers: Sanballat "was angry and greatly enraged, and he jeered at the Jews … 'What are these feeble Jews doing?'" (Neh 4:1–2); It enlarges its target: Haman "disdained to ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): 1Sa 17:28 (know), 1Sa 20:30 (know)
- **Observation 14276** (prior-capture, tag statement, status draft): Part 2 verses: what they add: The body's end of rivalrous anger: "The wicked man sees it and is angry; he gnashes his teeth and melts away; the desire of the wicked will perish!" (Psa 112:10). What he sees is the righteous man, whose "horn is exalted in honor" (112:9). Seeing the rival's rise ends in the angry one dissolving, not in the spear of 1Sa 18; Contrast seat: "His heart is steady; he will not be afraid" (112:8), said of the righteous one, two verses before. The seat is again named in the one the anger is aimed at (see Neh 4:6 above). Genuine; Rivalry among the disciples: "when the ten heard it, they were indignant at the two brothers" (Mat 20:24 = Mar 10:41). What they heard was Jes ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Mat 20:25 (know), Mar 10:42 (know)
- **Observation 14309** (prior-capture, tag statement, status draft): How it co-exists. Each list faces an opposite: "the fruit of the Spirit is love, joy, peace, patience …" (Gal 5:22); "Be kind to one another, tenderhearted, forgiving one another, as God in Christ forgave you" (Eph 4:32); "put on the new self, which is being renewed in knowledge" (Col 3:10); "put on the Lord Jesus Christ" (Rom 13:14); In Eph 4:30–31 the list comes straight after "do not grieve the Holy Spirit of God". Anger is set as something that grieves the Spirit.
  - applies to 1 occurrence(s): Col 3:10 (knowledge)
- **Observation 14346** (prior-capture, tag statement, status draft): Where it comes from. Self-sufficiency that does not see itself: "you say, 'I am rich, I have prospered, and I need nothing,' not realizing that you are wretched, pitiable, poor, blind, and naked" (3:17). The lukewarm state is linked to a failed self-perception. Compare M20's exposure phenomena.
  - applies to 1 occurrence(s): Rev 3:17 (realizing)
- **Observation 14515** (prior-capture, tag statement, status draft): Part B: Psa 86:15; 103:8; 145:8. Three more uses of the name. Pilot §2.2 already lists all three as uses of the idiom: An individual's plea against "insolent men": "But you, O Lord, are a God merciful and gracious, slow to anger … Turn to me and be gracious to me" (Psa 86:14–16); A recital with its reasoning: "He will not always chide, nor will he keep his anger forever. He does not deal with us according to our sins" (103:9–10). This comes straight after "He made known his ways to Moses" (103:7). The psalm names Moses as the one to whom the name was made known; Praise: "The Lord is good to all, and his mercy is over all that he has made" (145:9); The one creed is now used five ways: worship ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 103:7 (known)
- **Observation 14522** (prior-capture, tag statement, status draft): Where it comes from. This is where the texts give most. The roots named in the context of these verses: Forgetting. "take care lest you forget the Lord" (Deu 6:12); "You were unmindful of the Rock that bore you, and you forgot the God who gave you birth" (Deu 32:18); Fullness. "Jeshurun grew fat, and kicked; you grew fat, stout, and sleek; then he forsook God who made him" (Deu 32:15); "when … they have eaten and are full and grown fat, they will turn to other gods" (Deu 31:20). Plenty comes before the turn; A deceived or turning heart. "Take care lest your heart be deceived, and you turn aside" (Deu 11:16); "a man or woman … whose heart is turning away today" (Deu 29:18); Solomon's "heart h ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Deu 31:27 (know)
- **Observation 14523** (prior-capture, tag statement, status draft): How it co-exists: You become what you follow. "They went after false idols and became false" (2Ki 17:15). In exile "you will serve gods of wood and stone … that neither see, nor hear, nor eat, nor smell" (Deu 4:28); Walking contrary meets walking contrary. "if … you will not listen to me, but walk contrary to me, then I will walk contrary to you in fury" (Lev 26:27–28). The anger answers in the form of the provocation. The next verses are the famine ("eat the flesh of your sons", 26:29) and "my soul will abhor you" (26:30). F v4 §4 reads this as mutual abhorrence; What is known in the heart. Joshua ties the threat to what the people already know: "you know in your hearts and souls, all of yo ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Jos 23:14 (know), Judg 2:10 (know)
- **Observation 14525** (prior-capture, tag statement, status draft): Seat: In the verse: 1Ki 11:9 "his heart had turned away". Solomon's own. Genuine, the cause. Already read in A v3 §2.2 and pilot §2 ("the heart that provokes the anger"); Outside the verse (all genuine unless noted):; Deu 11:16 "lest your heart be deceived" (before) and 11:18 "lay up these words of mine in your heart and in your soul" (after). The deceived heart is the cause; the heart filled with the words is the guard. B v3 §4.1; C v3 §8.2; E v2 §4.1; G v3 §10; H v1 §5.1; Deu 29:18–19 "whose heart is turning away" / "blesses himself in his heart … stubbornness of my heart". E v2 §4.1, §12; C v3 §9.1; F v4 §9.6. Pilot §1.6 reads 29:20 with it; 1Ki 11:4 "his wives turned away his heart … his ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jos 23:14 (know)
- **Observation 14535** (prior-capture, tag statement, status draft): What it does: Spoken against: "Why then were you not afraid to speak against my servant Moses?" And the anger of the Lord was kindled against them (Num 12:8–9). The charge is a lack of fear; Silenced: Amaziah to the prophet: "Have we made you a royal counselor? Stop! Why should you be struck down?" (2Ch 25:16). The prophet stops, but says: "I know that God has determined to destroy you, because you have done this and have not listened to my counsel."; Killed: after Jehoiada died, "the king listened to them [the princes]"; prophets "testified against them, but they would not pay attention"; Zechariah, whom "the Spirit of God clothed", was stoned "in the court of the house of the Lord" (2Ch 24 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Ch 25:16 (know)
- **Observation 14557** (prior-capture, tag statement, status draft): How it co-exists: Accusation and generosity together. The same speech that threatens also offers land: "pass over into the Lord's land … and take for yourselves a possession among us" (Jos 22:19); The accused answer by appealing to God's knowledge: "The Mighty One, God, the Lord! He knows; and let Israel itself know! If it was in rebellion … do not spare us today" (Jos 22:22); The reverse plea. Moses argues against collective anger. David, after the census, asks to bear it alone: "I have sinned … But these sheep, what have they done? Please let your hand be against me and against my father's house". The one who sinned asks that the anger fall on himself only.
  - applies to 2 occurrence(s): Jos 22:22 (knows), Jos 22:22 (know)
- **Observation 14574** (prior-capture, tag statement, status draft): What it does: Foreseen in Solomon's prayer: "If they sin against you — for there is no one who does not sin — and you are angry with them … yet if they turn their heart … and repent … with all their heart and with all their soul … then hear" (1Ki 8:46–49; 2Ch 6:36–39); Josiah hears the book: "he tore his clothes … 'great is the wrath of the Lord that is kindled against us, because our fathers have not obeyed'" (2Ki 22:11, 13; 2Ch 34:19, 21). The answer names the heart: "because your heart was penitent [tender], and you humbled yourself … and have torn your clothes and wept before me, I also have heard you" (2Ki 22:19; 2Ch 34:27); Rehoboam and the princes: "humbled themselves and said, 'The L ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Ch 33:13 (knew)
- **Observation 14576** (prior-capture, tag statement, status draft): How it co-exists: Humbling with a confession of God's justice: "The Lord is righteous" (2Ch 12:6); "you are just" (Ezr 9:15); Humbling with the body: torn clothes and weeping (Josiah); Humbling that is partial. Rehoboam is spared destruction but made to serve Shishak, "that they may know my service and the service of the kingdoms" (2Ch 12:8). Bronze shields replace gold (12:10). And "he did evil, for he did not set his heart to seek the Lord" (12:14). The humbling turned the wrath, and the heart was still not set.
  - applies to 1 occurrence(s): 2Ch 12:8 (know)
- **Observation 14602** (prior-capture, tag statement, status draft): Part B: Psa 56:7; 59:13; 69:24; 79:6; Jer 10:25; 18:23; Lam 3:66 (seven verses). The imprecation is a recurring form in part B, as part A's pointer expected: The grounds given:; enemies who "injure my cause … have waited for my life" (Psa 56:5–6); "the sin of their mouths … the cursing and lies" (59:12); "they persecute him whom you have struck down, and they recount the pain of those you have wounded" (69:26): they add to God's striking; "the nations that do not know you … have devoured Jacob" (79:6–7; Jer 10:25 in the same words); Restraint inside the imprecation: "Kill them not, lest my people forget … consume them in wrath … that they may know that God rules over Jacob" (Psa 59:11, 13). ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): Psa 56:9 (know), Psa 59:13 (know), Psa 79:6 (know), Jer 10:25 (know), Jer 18:23 (know)
- **Observation 14605** (prior-capture, tag statement, status draft): How it co-exists: Job's contest wants God's anger visible on the wicked. "Let him pay it out to them, that they may know it" (21:19). Job does not deny God's anger; he denies that it is seen where the friends say; The wicked in Job 21 reject God outright: "Depart from us! We do not desire the knowledge of your ways" (21:14).
  - applies to 2 occurrence(s): Job 21:14 (knowledge), Job 21:19 (know)
- **Observation 14608** (prior-capture, tag statement, status draft): What it does: Within: "the arrows of the Almighty are in me; my spirit drinks their poison; the terrors of God are arrayed against me" (Job 6:4); As an enemy: "He has torn me in his wrath and hated me; he has gnashed his teeth at me" (16:9); "He has kindled his wrath against me and counts me as his adversary" (19:11); As a trial with fresh witnesses: "You renew your witnesses against me and increase your vexation toward me" (10:17); As irresistible and unanswerable: "God will not turn back his anger … How then can I answer him …? Though I am in the right, I cannot answer him; I must appeal for mercy to my accuser" (9:13–15). He "removes mountains, and they know it not, when he overturns them ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 9:5 (know)
- **Observation 14642** (prior-capture, tag statement, status draft): Part C: Nah 1:6; Rev 6:17: "Who can stand before his indignation? Who can endure the heat of his anger?" (Nah 1:6). The next verse: "The Lord is good, a stronghold in the day of trouble; he knows those who take refuge in him" (1:7); "for the great day of their wrath has come, and who can stand?" (Rev 6:17), said by those hiding in the caves; In unit 2 the question comes four times (Psa 76:7; Jer 10:10; Nah 1:6; Rev 6:17), each time by or about those facing the anger; Nahum and Psalm 2 both follow the anger with refuge in the same God.
  - applies to 1 occurrence(s): Nah 1:7 (knows)
- **Observation 14666** (prior-capture, tag statement, status draft): What it leads to. The agent is judged in turn: "he will punish the speech of the arrogant heart of the king of Assyria" (Isa 10:12); Babylon: "I set a snare for you and you were taken, O Babylon, and you did not know it … because you opposed the Lord" (Jer 50:24).
  - applies to 1 occurrence(s): Jer 50:24 (know)
- **Observation 14709** (prior-capture, tag statement, status draft): What it does: "In your forbearance take me not away; know that for your sake I bear reproach" (Jer 15:15); "Your words were found, and I ate them, and your words became to me a joy and the delight of my heart … I sat alone, because your hand was upon me, for you had filled me with indignation" (15:16–17); "Remember how I stood before you to speak good for them, to turn away your wrath from them" (18:20). The same verse: "they have dug a pit for my life".
  - applies to 1 occurrence(s): Jer 15:15 (know)
- **Observation 14731** (prior-capture, tag statement, status draft): What it does: "Thus shall my anger spend itself, and I will vent my fury upon them and satisfy myself. And they shall know that I am the Lord — that I have spoken in my jealousy" (Eze 5:13); "Then you will know that I am the Lord, who strikes" (7:9); For the nations too: "Then they will know that I am the Lord, when I lay my vengeance upon them" (25:17), the Philistines having "acted revengefully and took vengeance with malice of soul" (25:15); As a sign to others: "You shall be a reproach and a taunt, a warning and a horror, to the nations all around you" (5:15).
  - applies to 3 occurrence(s): Eze 5:13 (know), Eze 7:9 (know), Eze 25:17 (know)
- **Observation 14736** (prior-capture, tag statement, status draft): Linked to earlier sections: Part B §24: "that they may know that God rules" (Psa 59:13); Part B §46: "In the latter days you will understand" (Jer 23:20); Across the unit, God's anger is said to be for knowledge: of his rule (Psalms), of his purpose later (Jeremiah), of his name now (Ezekiel).
  - applies to 1 occurrence(s): Psa 59:13 (know)
- **Observation 14748** (prior-capture, tag statement, status draft): What it does: "the house of Israel has become dross to me … As one gathers silver and bronze and iron and lead and tin into a furnace, to blow the fire on it in order to melt it, so I will gather you in my anger and in my wrath, and I will put you in and melt you" (Eze 22:18, 20); "you shall know that I am the Lord; I have poured out my wrath upon you" (22:22); The pot: "Woe to the bloody city, to the pot whose corrosion is in it, and whose corrosion has not gone out of it!" (24:6). "To rouse my wrath, to take vengeance, I have set on the bare rock the blood she has shed, that it may not be covered" (24:8).
  - applies to 1 occurrence(s): Eze 22:22 (know)
- **Observation 14758** (prior-capture, tag statement, status draft): What it does. "Behold, I will make known to you what shall be at the latter end of the indignation, for it refers to the appointed time of the end" (Dan 8:19). "He shall prosper till the indignation is accomplished; for what is decreed shall be done" (11:36).
  - applies to 1 occurrence(s): Dan 8:19 (known)
- **Observation 14765** (prior-capture, tag statement, status draft): What it does: "'Yet even now,' declares the Lord, 'return to me with all your heart, with fasting, with weeping, and with mourning; and rend your hearts and not your garments.' Return to the Lord your God, for he is gracious and merciful, slow to anger … Who knows whether he will not turn and relent, and leave a blessing behind him …?" (Joe 2:12–14); The king of Nineveh: "Let neither man nor beast … taste anything … let man and beast be covered with sackcloth, and let them call out mightily to God. Let everyone turn from his evil way and from the violence that is in his hands. Who knows? God may turn and relent and turn from his fierce anger, so that we may not perish" (Jon 3:7–9).
  - applies to 2 occurrence(s): Joe 2:14 (knows), Jon 3:9 (knows)
- **Observation 14780** (prior-capture, tag statement, status draft): Where it comes from: Knowledge suppressed: "what can be known about God is plain to them … So they are without excuse" (Rom 1:19–20); Kindness presumed on: "do you presume on the riches of his kindness and forbearance and patience, not knowing that God's kindness is meant to lead you to repentance?" (2:4); Judging others while doing the same: "you who judge those who practice such things and yet do them yourself" (2:3).
  - applies to 1 occurrence(s): Rom 2:4 (not knowing)
- **Observation 14818** (prior-capture, tag statement, status draft): Jos 7; 22:10–34: Sequence the text gives: one man takes → anger on all → defeat → offender removed → anger turns → the memory drives a later confrontation → answer "He knows"; Phenomena: OS · TW.
  - applies to 1 occurrence(s): Jos 22:22 (knows)
- **Observation 14840** (prior-capture, tag statement, status draft): (v3) Joe 2:11–14; Jon 3:5–10: Sequence the text gives: the day, "who can endure it?" → return with the heart, fasting, sackcloth → the creed (Joel) or the preached word (Nineveh) → "Who knows?" → (Jonah) God relented; Phenomena: WK · SA.
  - applies to 2 occurrence(s): Joe 2:14 (knows), Jon 3:9 (knows)
- **Observation 14968** (prior-capture, tag link, status draft): Relational observation: the answer to mockery here is not a reply to the mocker. It is a prayer that God hear the mockery. I read this beside Psa 69:19 ("You know my reproach"): in both, the one under it brings it to God. The two verses state their own acts; the comparison is mine.
  - applies to 1 occurrence(s): Psa 69:19 (know)
- **Observation 14969** (prior-capture, tag statement, status draft): Purpose stated: "that all the kingdoms of the earth may know that you, O Lord, are God alone" (19:19).
  - applies to 1 occurrence(s): Psa 69:19 (know)
- **Observation 14971** (prior-capture, tag statement, status draft): What the passage adds: the reversal begins before the judgment: "She despises you, she scorns you— the virgin daughter of Zion; she wags her head behind you" (19:21). The one mocked is given the mocker's own gestures. And God says, "I know your sitting down and your going out and coming in, and your raging against me" (19:27). I read "raging" (rāgaz, a trembling word) as the inner side of the mockery, known to God.
  - applies to 2 occurrence(s): Isa 19:21 (known), Isa 19:21 (know)
- **Observation 15022** (prior-capture, tag statement, status draft): The passage. A prayer of David from deep water (69:1–2), weary with crying and waiting (69:3), hated "without cause" (69:4), and confessing "you know my folly" (69:5). The middle (69:6–12) is about reproach; the plea follows (69:13–18); then reproach again (69:19–21); and the psalm ends in praise and in "the Lord hears the needy" (69:33).
  - applies to 2 occurrence(s): Psa 69:5 (know), Psa 69:19 (know)
- **Observation 15049** (prior-capture, tag statement, status draft): "For although they knew God, they did not honor him as God or give thanks to him, but they became futile in their thinking, and their foolish hearts were darkened" (1:21). They "exchanged the glory of the immortal God for images" (1:23). Then three times "God gave them up" (1:24, 26, 28), each after an exchange (1:23, 25, and "did not see fit to acknowledge God", 1:28).
  - applies to 1 occurrence(s): Rom 1:21 (knew)
- **Observation 15087** (prior-capture, tag statement, status draft): These verses join pride to the turning away from God: Pride is a witness against its owner. "The pride of Israel testifies to his face; yet they do not return to the Lord their God, nor seek him, for all this" (Hos 7:10; also Hos 5:5); It goes with not knowing. The verse before says "Strangers devour his strength, and he knows it not; gray hairs are sprinkled upon him, and he knows it not" (Hos 7:9). In Hos 5:4–5, "they know not the Lord" stands next to "The pride of Israel testifies to his face"; Pride does not listen; "Hear and give ear; be not proud, for the Lord has spoken" (Jer 13:15). The opposite of pride here is hearing; Then: "if you will not listen, my soul will weep in secret for ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Hos 5:4 (know), Hos 7:9 (knows)
- **Observation 15113** (prior-capture, tag statement, status draft): The heart rises out of what it has been given. This is the clearest single pattern in the batch, and the verses state it each time: Strength. Uzziah "was marvelously helped, till he was strong. But when he was strong, he grew proud, to his destruction" (2Ch 26:15–16); Healing and honour. Hezekiah was healed, given a sign, and "exalted in the sight of all nations". Then: "But Hezekiah did not make return according to the benefit done to him, for his heart was proud" (2Ch 32:23–25). Here pride is a failure to return what was received. It was humbled the next verse (32:26, carried from M09); Greatness and majesty. "the Most High God gave Nebuchadnezzar your father kingship and greatness and glo ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Dan 5:21 (knew)
- **Observation 15121** (prior-capture, tag statement, status draft): zîd and zādôn name a pride that acts where it was not sent: Speaking what God did not say. "the prophet who presumes to speak a word in my name that I have not commanded him" (Deu 18:20). Such a word fails, and "You need not be afraid of him" (18:22). Presumption here borrows God's name for its own word; Going up when told not to. "Do not go up ... So I spoke to you, and you would not listen; but you rebelled against the command of the Lord and presumptuously went up" (Deu 1:42–43). It came straight after "We have sinned ... We ourselves will go up" (1:41). After the defeat, "you returned and wept before the Lord" (1:45). I read: presumption can wear the clothes of repentance. It goes up whe ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 17:28 (know)
- **Observation 15130** (prior-capture, tag statement, status draft): Egypt: Jethro: "Now I know that the Lord is greater than all gods, because in this affair they dealt arrogantly with the people" (Exo 18:11); "you knew that they acted arrogantly against our fathers. And you made a name for yourself" (Neh 9:10); God's greatness is known in his answer to arrogance against his people.
  - applies to 2 occurrence(s): Exo 18:11 (know), Neh 9:10 (knew)
- **Observation 15135** (prior-capture, tag statement, status draft): Talk no more proudly. Hannah: "Talk no more so very proudly, let not arrogance come from your mouth; for the Lord is a God of knowledge, and by him actions are weighed. The bows of the mighty are broken, but the feeble bind on strength" (1Sa 2:3–4). The reason given against proud talk is that God knows and weighs.
  - applies to 1 occurrence(s): 1Sa 2:3 (knowledge)
- **Observation 15141** (prior-capture, tag statement, status draft): "though the Lord is high, he regards the lowly, but the haughty he knows from afar" (Psa 138:6, carried).
  - applies to 1 occurrence(s): Psa 138:6 (knows)
- **Observation 15146** (prior-capture, tag statement, status draft): The verses say outright that pride takes a place that is God's: "you have said, 'I am a god, I sit in the seat of the gods' ... yet you are but a man, and no god, though you make your heart like the heart of a god" (Eze 28:2); "Who will bring me down to the ground?" (Obd 3); "By the strength of my hand I have done it" (Isa 10:13); This is the researcher's "assumed position" in the verses' own words. Pride is a heart made like the heart of a god. It is not so; What was given is turned into pride; "the Most High God gave Nebuchadnezzar ... kingship and greatness and glory and majesty ... But when his heart was lifted up" (Dan 5:18–20). Majesty is the same word family God wears (batch 1); The p ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Exo 18:11 (know), 1Sa 2:3 (knowledge), Neh 9:10 (knew), Psa 138:6 (knows)
- **Observation 15151** (prior-capture, tag statement, status draft): The Greek picture is swelling, physioō, "to inflate". In Paul it is set again and again against love: Knowledge. "This 'knowledge' puffs up, but love builds up. If anyone imagines that he knows something, he does not yet know as he ought to know. But if anyone loves God, he is known by God" (1Co 8:1–3). Swelling knowledge is answered not by more knowledge but by being known by God; Love is not. "Love is patient and kind; love does not envy or boast; it is not arrogant" (1Co 13:4). Before this: "if I have prophetic powers, and understand all mysteries and all knowledge ... but have not love, I am nothing" (13:2); Party; "that none of you may be puffed up in favor of one against another. For w ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): 1Cor 8:1 (know), 1Cor 8:1 (knowledge), 1Cor 8:2 (knows), 1Cor 8:3 (known), 1Cor 13:2 (knowledge)
- **Observation 15154** (prior-capture, tag statement, status draft): Lofty opinions. "every lofty opinion raised against the knowledge of God, and take every thought captive to obey Christ" (2Co 10:5). Height here is a thought raised against knowing God.
  - applies to 1 occurrence(s): 2Cor 10:5 (knowledge)
- **Observation 15166** (prior-capture, tag statement, status draft): Exalted among men. "You are those who justify yourselves before men, but God knows your hearts. For what is exalted among men is an abomination in the sight of God" (Luk 16:15). The Pharisees "were lovers of money" and "ridiculed him" (16:14). Height measured by people is set against God's knowing of the heart.
  - applies to 1 occurrence(s): Luk 16:15 (knows)
- **Observation 15167** (prior-capture, tag statement, status draft): Boasting about tomorrow. "you do not know what tomorrow will bring ... Instead you ought to say, 'If the Lord wills, we will live and do this or that.' As it is, you boast in your arrogance. All such boasting is evil" (Jam 4:14–16). The arrogance is planning as if life were one's own.
  - applies to 1 occurrence(s): Jam 4:14 (know)
- **Observation 15170** (prior-capture, tag statement, status draft): The given-or-taken line is stated outright. "What do you have that you did not receive? If then you received it, why do you boast as if you did not receive it?" (1Co 4:7): This is the plainest statement in the three batches of what the researcher suspected. Human pride holds as its own what was received; The researcher's word "assumed" fits: the standing is taken up as if it were not given; The right measure is the one God assigns. "not to think of himself more highly than he ought ... according to the measure of faith that God has assigned" (Rom 12:3). I read: where God has height by nature, a person has a measure by gift. Pride is thinking past the gift; Taking God's seat; "takes his seat ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): 1Sa 2:3 (knowledge), Luk 16:15 (knows)
- **Observation 15180** (prior-capture, tag statement, status draft): Before it is done: "Let not him who straps on his armor boast himself as he who takes it off" (1Ki 20:11); "Do not boast about tomorrow, for you do not know what a day may bring. Let another praise you, and not your own mouth" (Pro 27:1–2); Jam 4:16 (batch 3) is the New Testament form.
  - applies to 1 occurrence(s): Pro 27:1 (know)
- **Observation 15195** (prior-capture, tag statement, status draft): The boast is not removed. It is moved: The command. "Let the one who boasts, boast in the Lord" (1Co 1:31; 2Co 10:17). This follows Christ "who became to us wisdom from God, righteousness and sanctification and redemption" (1:30). It is joined to "it is not the one who commends himself who is approved, but the one whom the Lord commends" (2Co 10:18); What to boast in; "let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight" (Jer 9:24); The boast is in knowing God, and what is known is his character; The soul's boast. "My soul makes its boast in the Lord; let th ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Jer 9:24 (knows), Rom 5:3 (knowing)
- **Observation 15199** (prior-capture, tag statement, status draft): God is not the subject of a boast in these verses. He is its right object, and his character is what is boasted in. "let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight" (Jer 9:24). The proper boast is knowing God as he is: The boast is moved, not removed. The same impulse that boasts in wisdom, might and riches (Jer 9:23) is turned to God (9:24; 1Co 1:31). It becomes joy in hope and in suffering (Rom 5:2–3); I read: set beside batches 1–3, the human "lifting" is not abolished. Where it rests on oneself it is pride. Where it rests on God it is glory in him. ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Jer 9:24 (knows), Rom 5:3 (knowing)
- **Observation 15205** (prior-capture, tag statement, status draft): Proverbs paints the scoffer by what he will not receive: Rebuke; "A wise son hears his father's instruction, but a scoffer does not listen to rebuke" (Pro 13:1); "A scoffer does not like to be reproved; he will not go to the wise" (15:12). The verse before is "Sheol and Abaddon lie open before the Lord; how much more the hearts of the children of man!" (15:11); Hatred of correction. "Whoever corrects a scoffer gets himself abuse ... Do not reprove a scoffer, or he will hate you; reprove a wise man, and he will love you" (Pro 9:7–8). The same rebuke brings out hate in one and love in the other; Wisdom in vain. "A scoffer seeks wisdom in vain, but knowledge is easy for a man of understanding" ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Pro 1:22 (knowledge), Pro 14:6 (knowledge), Pro 19:25 (knowledge), Pro 21:11 (knowledge)
- **Observation 15225** (prior-capture, tag statement, status draft): Mocked as saviour, and in his trust: "He saved others; he cannot save himself" (Mar 15:31); "He trusts in God; let God deliver him now, if he desires him" (Mat 27:43). This is the mockery of Psa 22:8; "The soldiers also mocked him ... 'If you are the King of the Jews, save yourself!'" (Luk 23:36–37); Just before: "Father, forgive them, for they know not what they do" (23:34).
  - applies to 1 occurrence(s): Luk 23:34 (know)
- **Observation 15226** (prior-capture, tag statement, status draft): Laughed at. "'the girl is not dead but sleeping.' And they laughed at him" (Mat 9:24; Mar 5:40). "they laughed at him, knowing that she was dead" (Luk 8:53). Then the girl arose.
  - applies to 1 occurrence(s): Luk 8:53 (knowing)
- **Observation 15233** (prior-capture, tag statement, status draft): The people become the object of mockery. In Jer 24 this sits beside "I will give them a heart to know me ... for they shall return to me with their whole heart" (24:7).
  - applies to 1 occurrence(s): Jer 24:7 (know)
- **Observation 15235** (prior-capture, tag statement, status draft): 2Ch 32:31 is read for the heart elsewhere (10.11): "God left him to himself, in order to test him and to know all that was in his heart". Its M08 word is only "envoys".
  - applies to 1 occurrence(s): 2Ch 32:31 (know)
- **Observation 15243** (prior-capture, tag statement, status draft): Pride sense (42). These include: the heart proud or haughty: 2Ch 32:25–26; 2Ch 26:16; Eze 28:2, 5, 17; Eze 31:10; Pro 16:5; Pro 18:12; Psa 101:5; a haughty spirit: Pro 16:18; Ecc 7:8; haughty eyes and looks: Isa 5:15; 2Ki 19:22 and Isa 37:23 (lifting the eyes against the Holy One); the lofty brought low: Isa 10:33; Isa 26:5; Eze 31:14; "do not become proud, but fear": Rom 11:20; Rom 12:16, 2Co 10:5 ("every lofty opinion raised against the knowledge of God") and Luk 16:15; Obd 3–4 and Jer 49:16 (the nest set high); Isa 3:16 (the daughters of Zion) and Isa 22:16 (Shebna's tomb on the height). These two have no other M-code.
  - applies to 1 occurrence(s): 2Cor 10:5 (knowledge)
- **Observation 15257** (prior-capture, tag statement, status draft): Are any of the pride words indicative of God's characteristics? Yes: The gāʾôn family is used of God's majesty: "majesty", "triumphed gloriously", "robed in majesty" (Exo 15:1, 7; Psa 93:1; Isa 2:10); "Majesty" is used as a name for God (Heb 1:3; 8:1); The mocking words are used of God's derision: "He who sits in the heavens laughs" (Psa 2:4); "Toward the scorners he is scornful" (Pro 3:34); God is never the subject of a boast in these verses. He is its right object: "let him who boasts boast in this, that he understands and knows me" (Jer 9:24).
  - applies to 1 occurrence(s): Jer 9:24 (knows)
- **Observation 15307** (prior-capture, tag statement, status draft): Pride is rarely alone in these verses. It stands over someone: the poor: "In arrogance the wicked hotly pursue the poor" (Psa 10:2); "Whoever mocks the poor insults his Maker" (Pro 17:5); the widow: "tears down the house of the proud but maintains the widow's boundaries" (Pro 15:25); the needy left unaided: "pride, excess of food, and prosperous ease, but did not aid the poor and needy" (Eze 16:49); the righteous: "speak insolently against the righteous in pride and contempt" (Psa 31:18); the insolent who deride, smear and dig pits (Psa 119:51, 69, 85); with a closed heart: "They close their hearts to pity; with their mouths they speak arrogantly" (Psa 17:10); set against love, and among the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Cor 8:1 (knowledge)
- **Observation 15310** (prior-capture, tag statement, status draft): The boast is moved, not removed: "let him who boasts boast in this, that he understands and knows me" (Jer 9:24); "Let the one who boasts, boast in the Lord" (1Co 1:31); The same word becomes joy in hope and in suffering (Rom 5:2–3, 11); Boasting in weakness: "so that the power of Christ may rest upon me" (2Co 12:9); Boasting of others (2Co 7:4; 1Th 2:19); The boast within the measure God assigned (2Co 10:13), as thinking of oneself is within "the measure of faith that God has assigned" (Rom 12:3).
  - applies to 1 occurrence(s): Jer 9:24 (knows)
- **Observation 15314** (prior-capture, tag statement, status draft): What it is set against, God answers otherwise: "though the Lord is high, he regards the lowly, but the haughty he knows from afar" (Psa 138:6); God's derision answers only those who rise against him (Psa 2:2–4; 59:7–8; Pro 1:24–26; 3:34). In these verses it is never aimed at the weak.
  - applies to 1 occurrence(s): Psa 138:6 (knows)
- **Observation 15315** (prior-capture, tag statement, status draft): Pride can be named wrongly: An angry brother says "I know your presumption" (1Sa 17:28), and the chapter shows that David was sent by his father (17:17–18); A friend explains another's fall: "For when they are humbled you say, 'It is because of pride'" (Job 22:29).
  - applies to 1 occurrence(s): 1Sa 17:28 (know)
- **Observation 15333** (prior-capture, tag statement, status draft): It answers a word heard: Rehoboam and the princes humble themselves when Shemaiah brings "You abandoned me, so I have abandoned you". What they say is "The Lord is righteous" (2Ch 12:5–6); Josiah humbles himself "when you heard how I spoke against this place" (2Ki 22:19; 2Ch 34:27); Ahab does so "when Ahab heard those words" (1Ki 21:27); Belshazzar is charged: "you … have not humbled your heart, though you knew all this" (Dan 5:22). He had the word, in his father's story, and did not bow to it.
  - applies to 1 occurrence(s): Dan 5:22 (knew)
- **Observation 15339** (prior-capture, tag statement, status draft): Fathers and sons. "he did not humble himself before the Lord, as Manasseh his father had humbled himself, but this Amon incurred guilt more and more" (2Ch 33:23). Belshazzar "knew all this" of his father (Dan 5:22). One generation's humbling does not pass to the next.
  - applies to 1 occurrence(s): Dan 5:22 (knew)
- **Observation 15343** (prior-capture, tag statement, status draft): What follows in Manasseh: "Then Manasseh knew that the Lord was God" (2Ch 33:13). Knowing follows the humbling and the answer. It does not come before them.
  - applies to 1 occurrence(s): 2Ch 33:13 (knew)
- **Observation 15344** (prior-capture, tag statement, status draft): A humbling God does not take knowledge of: Isa 58:3–5: The people ask: "Why have we fasted, and you see it not? Why have we humbled ourselves, and you take no knowledge of it?"; The answer: "in the day of your fast you seek your own pleasure, and oppress all your workers", and "you fast only to quarrel and to fight"; The form is named and set aside: "Is it to bow down his head like a reed, and to spread sackcloth and ashes under him?"; The fast God chooses is turned to others: "to loose the bonds of wickedness … to share your bread with the hungry and bring the homeless poor into your house; when you see the naked, to cover him" (58:6–7); Compare Ahab. His sackcloth and fasting were seen and ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 58:3 (knowledge)
- **Observation 15345** (prior-capture, tag statement, status draft): Deu 8:2–3, 16 states the purpose: "that he might humble you, testing you to know what was in your heart, whether you would keep his commandments or not" (8:2); "And he humbled you and let you hunger and fed you with manna … that he might make you know that man does not live by bread alone" (8:3); "that he might humble you and test you, to do you good in the end" (8:16).
  - applies to 3 occurrence(s): Deu 8:2 (know), Deu 8:3 (know), Deu 8:16 (know)
- **Observation 15414** (prior-capture, tag statement, status draft): Psa 138:6: God's act: "though the Lord is high, he regards the lowly"; Set against: "the haughty he knows from afar".
  - applies to 1 occurrence(s): Psa 138:6 (knows)
- **Observation 15470** (prior-capture, tag statement, status draft): Paul, brought low and lowering himself: "I know how to be brought low, and I know how to abound … I have learned … to be content" (Phili 4:11–12). Being brought low is a circumstance here, met with contentment, "through him who strengthens me" (4:13); "did I commit a sin in humbling myself so that you might be exalted, because I preached God's gospel to you free of charge?" (2Cor 11:7). A lowering taken on for others' good. I read: this has the shape of Phili 2: lowered so that another is raised; "I fear that when I come again my God may humble me before you, and I may have to mourn over many of those who sinned earlier and have not repented" (2Cor 12:21). Here Paul is humbled by others' unr ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Phili 4:12 (know)
- **Observation 15507** (prior-capture, tag statement, status draft): The boy Jesus, submissive: "he went down with them and came to Nazareth and was submissive to them. And his mother treasured up all these things in her heart" (Luk 2:51): This follows "Did you not know that I must be in my Father's house?" (2:49); The Son who knows his Father's house goes down and is subject to Mary and Joseph; Then "Jesus increased in wisdom and in stature and in favor with God and man" (2:52); Cited in Ch 4 (for Mary's heart), not for his submission.
  - applies to 1 occurrence(s): Luk 2:49 (know)
- **Observation 15577** (prior-capture, tag statement, status draft): Eze 17:24: What it adds: the reversal's purpose ("shall know that I am the Lord") and certainty ("I have spoken, and I will do it"); Where: 10.14 Only God does it (one sentence).
  - applies to 1 occurrence(s): Eze 17:24 (know)
- **Observation 15585** (prior-capture, tag statement, status draft): Poor where the verse separates what is said or seen from what is so: "One pretends to be rich, yet has nothing; another pretends to be poor, yet has great wealth" (Pro 13:7); "you say, 'I am rich … I need nothing,' not realizing that you are … poor" (Rev 3:17); "as poor, yet making many rich; as having nothing, yet possessing everything" (2Co 6:10); "poor in the world to be rich in faith" (Jam 2:5); "though he was rich, yet for your sake he became poor" (2Co 8:9).
  - applies to 1 occurrence(s): Rev 3:17 (realizing)
- **Observation 15594** (prior-capture, tag statement, status draft): Where a verse joins the two sides: "Whoever oppresses a poor man insults his Maker, but he who is generous to the needy honors him" (Pro 14:31); "Whoever mocks the poor insults his Maker" (Pro 17:5); "Whoever is generous to the poor lends to the Lord" (Pro 19:17); "He judged the cause of the poor and needy … Is not this to know me? declares the Lord" (Jer 22:16); "The rich and the poor meet together; the Lord is the Maker of them all" (Pro 22:2); "Did not he who made me in the womb make him?" (Job 31:15).
  - applies to 1 occurrence(s): Jer 22:16 (know)
- **Observation 15669** (prior-capture, tag statement, status draft): A humbling God does not accept: OT: the fast with "your own pleasure": "Why have we humbled ourselves, and you take no knowledge of it?" (Isa 58:3); NT: "self-made religion and asceticism" that leaves one "puffed up" (Col 2:18, 23); the Pharisee's "I fast twice a week" (Luk 18:12).
  - applies to 1 occurrence(s): Isa 58:3 (knowledge)
- **Observation 15752** (prior-capture, tag statement, status draft): The guilt is realized: H0816's Leviticus 4-6 verses use and he realizes his guilt as what reads like a near-technical hinge phrase, repeated near-verbatim across Lev 4:13, 4:22, 4:27, 5:2, 5:3, 5:4, 5:5, 5:17, 6:4 and 6:5. Guilt is not complete as a status until it is recognized, not merely incurred.
  - applies to 1 occurrence(s): Lev 5:4 (realizes)
- **Observation 15840** (prior-capture, tag statement, status draft): Spirit and fear: Human, contrite: "humble and contrite in spirit and trembles at my word" (Isa 66:2) [H]; Given disposition: "God gave us a spirit not of fear but of power and love and self-control" (2Ti 1:7) [X]; Contrast: "you did not receive the spirit of slavery to fall back into fear, but … the Spirit of adoption" (Rom 8:15) [X+D1]; Divine Spirit as the ground of not fearing: "My Spirit remains in your midst. Fear not" (Hag 2:5) [D1]; Divine Spirit endowing "the fear of the Lord": "the Spirit of knowledge and the fear of the Lord" (Isa 11:2) [D1]; Fear of a spirit-being: "startled and frightened and thought they saw a spirit" (Luk 24:37) [O]; "the arrows of the Almighty are in me; my sp ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 11:2 (knowledge)
- **Observation 15842** (prior-capture, tag statement, status draft): Soul/life and fear: Fear *for* one's life: Jos 9:24; Eze 32:10; 1Sa 22:23; The right object of fear is defined by the soul: "do not fear those who kill the body but cannot kill the soul. Rather fear him who can destroy both soul and body" (Mat 10:28); "awe came upon every soul" (Act 2:43); "fearfully and wonderfully made … my soul knows it very well" (Psa 139:14)
  - applies to 1 occurrence(s): Psa 139:14 (knows)
- **Observation 15866** (prior-capture, tag statement, status draft): Heart and spirit also carry it: "The heart knows its own bitterness" (Pro 14:10); "it is bitter; it has reached your very heart" (Jer 4:18); "made life [rûaḥ] bitter" (Gen 26:35) [H]; "bitterness in the heat of my spirit" (Eze 3:14).
  - applies to 1 occurrence(s): Pro 14:10 (knows)
- **Observation 15915** (prior-capture, tag statement, status draft): God searching the anxious heart: "Search me, O God, and know my heart! Try me and know my thoughts [anxious thoughts]" (Psa 139:23) [lexical].
  - applies to 1 occurrence(s): Psa 139:23 (know)
- **Observation 15923** (prior-capture, tag statement, status draft): Affliction as God's means to reveal the heart: "that he might humble you, testing you to know what was in your heart" (Deu 8:2).
  - applies to 1 occurrence(s): Deu 8:2 (know)
- **Observation 15928** (prior-capture, tag statement, status draft): Affliction and empathy: "You know the heart [nephesh] of a sojourner, for you were sojourners" (Exo 23:9); "if you pour yourself [nephesh] out for the hungry and satisfy the desire [nephesh] of the afflicted" (Isa 58:10) — one's own nephesh poured out to satisfy another's
  - applies to 1 occurrence(s): Exo 23:9 (know)
- **Observation 15933** (prior-capture, tag statement, status draft): Soul knowing God's wonders: "Wonderful are your works; my soul knows it very well" (Psa 139:14); "Your testimonies are wonderful; therefore my soul keeps them" (Psa 119:129).
  - applies to 1 occurrence(s): Psa 139:14 (knows)
- **Observation 15938** (prior-capture, tag statement, status draft): 0. Data notes: "Set the heart" is a single idiom (H7760K / H7896K "to set: consider", often at d0, i.e. the same token as *lēv*).; It is behind "consider" (Hag 1:5, 7; 2:15, 18; Job 1:8; 2:3; Pro 24:32), "care" (2Sa 18:3), "pay attention" (1Sa 4:20), "mark well" (Eze 44:5) and "take to heart" (2Sa 13:20; Exo 7:23; Isa 42:25; Mal 2:2).; [Claude reading] Attention and consideration are expressed as *placing the heart*.; Speech verbs are elsewhere. *(Corrected in v2.)* "Speak" (H1696G/I) and "speak rashly" (H0981) are filed under M42 Prayer & Petition (→ Ruling R1). "Say" (H0559) is in T3 Operations, so it is not in the pairs file at all (→ Ruling R2). So the "said in his heart" series (depicti ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Judg 19:22 (know)
- **Observation 15939** (prior-capture, tag statement, status draft): 1.1 The heart as the knower: "Your heart knows that many times you yourself have cursed others" (Ecc 7:22); "You know in your own heart all the harm that you did" (1Ki 2:44, d0); "you know in your hearts and souls … that not one word has failed" (Jos 23:14); "Know then in your heart …" (Deu 8:5); "know therefore today, and lay it to your heart, that the Lord is God" (Deu 4:39); "The heart knows its own bitterness" (Pro 14:10); [Claude reading] "Knowing in the heart" is inner certainty and self-knowledge, not only information.
  - applies to 6 occurrence(s): Deu 4:39 (know), Deu 8:5 (know then), Jos 23:14 (know), 1Ki 2:44 (know), Pro 14:10 (knows), Ecc 7:22 (knows)
- **Observation 15940** (prior-capture, tag statement, status draft): 1.2 Attention — setting the heart (see §0.1): "Consider your ways" = set your heart on your ways.; "set your heart to understand" (Dan 10:12); "apply my heart to know wisdom" (Ecc 1:17; 7:25; 8:16); "Take to heart all the words" (Deu 32:46); The failure case: "it burned him up, but he did not take it to heart" (Isa 42:25).
  - applies to 3 occurrence(s): Ecc 1:17 (know), Ecc 7:25 (know), Ecc 8:16 (know)
- **Observation 15941** (prior-capture, tag statement, status draft): Given by God: "I will give them a heart to know me" (Jer 24:7); "I give you a wise and discerning mind [heart]" (1Ki 3:12); "Who has put wisdom in the inward parts or given understanding to the mind?" (Job 38:36); "God … has shone in our hearts to give the light of the knowledge" (2Co 4:6); "having the eyes of your hearts enlightened, that you may know" (Eph 1:18)
  - applies to 3 occurrence(s): Jer 24:7 (know), 2Cor 4:6 (knowledge), Eph 1:18 (know)
- **Observation 15944** (prior-capture, tag statement, status draft): 1.4 God knows, tests and searches the heart: "you, you only, know the hearts of all the children of mankind" (1Ki 8:39; 2Ch 6:30); "he knows the secrets of the heart" (Psa 44:21); "God knows your hearts" (Luk 16:15); "Search me, O God, and know my heart! Try me and know my thoughts!" (Psa 139:23); "he who searches mind and heart" (Rev 2:23); "testing you to know what was in your heart" (Deu 8:2; 2Ch 32:31; Deu 13:3 "with all your heart and with all your soul")
  - applies to 8 occurrence(s): Deu 8:2 (know), Deu 13:3 (know), 1Ki 8:39 (know), 2Ch 6:30 (know), 2Ch 32:31 (know), Psa 44:21 (knows), Psa 139:23 (know), Luk 16:15 (knows)
- **Observation 15945** (prior-capture, tag statement, status draft): Heart and soul together: "does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it?" (Pro 24:12)
  - applies to 1 occurrence(s): Pro 24:12 (know)
- **Observation 15947** (prior-capture, tag statement, status draft): 1.5 The soul in knowing: "my soul knows it very well" (Psa 139:14); "knowledge will be pleasant to your soul" (Pro 2:10); "wisdom is such to your soul" (Pro 24:14); "Whoever gets sense loves his own soul" (Pro 19:8); Revisit 2026-09-28: Pro 19:8 is the wisdom side of loving or hating one's own soul. In the Gospels the valuation reverses (Joh 12:25). See Batch F §3.; "take counsel in my soul" (Psa 13:2); In the NT, psychē is rendered "minds" (Act 14:2 "poisoned their minds"; 15:24 "unsettling your minds").; [Claude reading] The soul *receives* knowledge as something pleasant or nourishing, rather than being the one who investigates.
  - applies to 2 occurrence(s): Psa 139:14 (knows), Pro 2:10 (knowledge)
- **Observation 15948** (prior-capture, tag statement, status draft): Desire ahead of knowledge: "Desire [nephesh] without knowledge is not good" (Pro 19:2); "The dogs have a mighty appetite; they never have enough. But they are shepherds who have no understanding" (Isa 56:11); "Before I was aware, my desire [nephesh] set me among the chariots" (Song 6:12) — the soul's desire acts before awareness
  - applies to 2 occurrence(s): Pro 19:2 (knowledge), Song 6:12 (aware)
- **Observation 15949** (prior-capture, tag statement, status draft): Self-knowledge: "who knows a person's thoughts except the spirit of that person, which is in him?" (1Co 2:11) [H1+D1].
  - applies to 1 occurrence(s): 1Cor 2:11 (knows)
- **Observation 15957** (prior-capture, tag statement, status draft): 1.7 God's Spirit as the source of knowledge [D]: "the Spirit of wisdom and understanding … of knowledge and the fear of the Lord" (Isa 11:2); "filled him with the Spirit of God, with ability and intelligence, with knowledge and all craftsmanship" (Exo 31:3; 35:31); "through the Spirit the utterance of wisdom … of knowledge" (1Co 12:8); "the Spirit searches everything … the natural person does not accept the things of the Spirit … they are spiritually discerned" (1Co 2:10–14); "the Holy Spirit will teach you" (Luk 12:12; Joh 14:26); "we do not know what to pray for … but the Spirit himself intercedes" (Rom 8:26); "he who searches hearts knows what is the mind of the Spirit" (Rom 8:27)
  - applies to 6 occurrence(s): Exo 31:3 (knowledge), Exo 35:31 (knowledge), Isa 11:2 (knowledge), Rom 8:26 (know), Rom 8:27 (knows), 1Cor 12:8 (knowledge)
- **Observation 15961** (prior-capture, tag statement, status draft): "All flesh" as knowing humanity: "all flesh shall know that I am the Lord" (Eze 21:5; Isa 49:26).
  - applies to 2 occurrence(s): Isa 49:26 (know), Eze 21:5 (know)
- **Observation 15962** (prior-capture, tag statement, status draft): 1.9 Conscience and knowledge: "not all possess this knowledge … their conscience, being weak, is defiled" (1Co 8:7, 10) — knowledge shapes the conscience.; "both their minds and their consciences are defiled" (Tit 1:15).; "their conscience also bears witness, and their conflicting thoughts accuse or even excuse them" (Rom 2:15).
  - applies to 2 occurrence(s): 1Cor 8:7 (knowledge), 1Cor 8:10 (knowledge)
- **Observation 15965** (prior-capture, tag statement, status draft): 1.11 ◆ Breath, wind and thought: "When his breath departs … on that very day his plans perish" (Psa 146:4) — the brief's thought link; "he who … creates the wind, and declares to man what is his thought" (Amo 4:13); "windy knowledge" (Job 15:2); "I applied my heart to know wisdom … this also is but a striving after wind" (Ecc 1:17); "Every man is stupid and without knowledge … there is no breath in them" (Jer 10:14; 51:17)
  - applies to 4 occurrence(s): Job 15:2 (knowledge), Ecc 1:17 (know), Jer 10:14 (knowledge), Jer 51:17 (knowledge)
- **Observation 15968** (prior-capture, tag statement, status draft): 2.3 Wisdom going wrong through the heart: "your wisdom and your knowledge led you astray, and you said in your heart, 'I am'" (Isa 47:10); "Your heart was proud … you corrupted your wisdom" (Eze 28:17); "by your great wisdom … your heart has become proud" (Eze 28:5); "oppression drives the wise into madness, and a bribe corrupts the heart" (Ecc 7:7)
  - applies to 1 occurrence(s): Isa 47:10 (knowledge)
- **Observation 16036** (prior-capture, tag statement, status draft): Interpreting dreams by spirit: "an excellent spirit … to interpret dreams" (Dan 5:12) [H2+X]; "the spirit of the holy gods is in you" (Dan 4:9, 18) [D-attr]; "his spirit was troubled … none who could interpret" (Gen 41:8) [H].
  - applies to 2 occurrence(s): Gen 41:8 (interpret), Dan 5:12 (interpret)
- **Observation 16079** (prior-capture, tag statement, status draft): The formula: "as the Lord lives and as your soul lives" (1Sa 20:3; 25:26; 2Sa 11:11); "as the Lord lives, and as you yourself live, I will not leave you" (2Ki 2:2, 4, 6; 4:30); "As your soul lives, O king, I do not know" (1Sa 17:55); "As you live, my lord" (1Sa 1:26; 2Sa 14:19); "As the Lord lives, who has redeemed my soul out of every adversity" (1Ki 1:29; 2Sa 4:9); "As the Lord lives, who made our souls" (Jer 38:16); "As God lives, … who has made my soul bitter" (Job 27:2); [lexical; Claude reading] The oath sets the other person's *nephesh* beside the Lord's own life as the thing that guarantees the word. To swear by someone's soul is to stake one's word on their life. In the second form, ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 17:55 (know)
- **Observation 16080** (prior-capture, tag statement, status draft): 1Sa 17:55 → 18:1 | David goes out against the Philistine | Abner: "As your soul lives, O king, I do not know" whose son he is | David is brought in with the head; "the soul of Jonathan was knit to the soul of David" (18:1; Batch F §1.1)
  - applies to 1 occurrence(s): 1Sa 17:55 (know)
- **Observation 16084** (prior-capture, tag statement, status draft): Jer 38:14–24 | "hide nothing from me" (14); "will you not surely put me to death?" (15) | Zedekiah "swore secretly, 'As the Lord lives, who made our souls, I will not put you to death'" (16) | "your life shall be spared" if you surrender (17, 20); "I am afraid" (19); "Let no one know of these words, and you shall not die" (24)
  - applies to 1 occurrence(s): Jer 38:24 (know)
- **Observation 16174** (prior-capture, tag statement, status draft): 16.3 The heart and soul measured against death: "I find something more bitter than death: the woman whose heart is snares and nets" (Ecc 7:26). The context is the searcher's own heart: "I turned my heart to know … the foolishness that is madness" (7:25).; [Claude reading] One heart searching finds another heart as the trap. A heart set with snares is worse than death.; "His greed [*nephesh*] is as wide as Sheol; like death he has never enough" (Hab 2:5). It follows directly on "his soul is puffed up" (2:4; §5.5).; [Claude reading] Here the soul is compared with death as appetite. Both swallow and are never satisfied.
  - applies to 1 occurrence(s): Ecc 7:25 (know)
- **Observation 16184** (prior-capture, tag statement, status draft): The heart's condition as the cause of death — wisdom and sayings: "fools die for lack of sense [*heart*]" (Pro 10:21); "Whoever keeps the commandment keeps his life; he who despises his ways will die" (Pro 19:16); "he who fails to find me injures himself [*his soul*]; all who hate me love death" (Pro 8:36; Batch F §3.1); "The godless in heart cherish anger … They die in youth" (Job 36:13–14); "the hearts of the children of man are full of evil, and madness is in their hearts while they live, and after that they go to the dead" (Ecc 9:3) → "a living dog is better than a dead lion. For the living know that they will die" (9:4–5); "Discipline your son, for there is hope; do not set your heart o ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Ecc 9:5 (know), Rev 2:23 (know)
- **Observation 16240** (prior-capture, tag statement, status draft): The heart's affliction as the content of prayer: "whatever prayer, whatever plea … each knowing the affliction of his own heart" (1Ki 8:38).
  - applies to 1 occurrence(s): 1Ki 8:38 (knowing)
- **Observation 16258** (prior-capture, tag statement, status draft): 1.5 The Spirit prays, cries and intercedes — divine speech in the human seat: "God has sent the Spirit of his Son into our hearts, crying, 'Abba! Father!'" (Gal 4:6) [D1] — the cry sounds in the heart; "the Spirit of adoption as sons, by whom we cry, 'Abba! Father!'" (Rom 8:15) [X+D1] — the same cry, now ours; "the Spirit himself intercedes for us with groanings too deep for words" (Rom 8:26) [D1]; "he who searches hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints" (Rom 8:27) [D2]
  - applies to 1 occurrence(s): Rom 8:27 (knows)
- **Observation 16301** (prior-capture, tag statement, status draft): 3.3 Glory, the Spirit and the heart (NT); exaltation: "the Spirit of glory and of God rests upon you" (1Pe 4:14) [D1]; "we all … are being transformed … from one degree of glory to another. For this comes from the Lord who is the Spirit" (2Co 3:18); "God … has shone in our hearts to give the light of the knowledge of the glory of God" (2Co 4:6); "that according to the riches of his glory he may grant you to be strengthened with power through his Spirit in your inner being" (Eph 3:16) [D1]; "full of the Holy Spirit, gazed into heaven and saw the glory of God" (Act 7:55); "the Spirit lifted me up … the glory of the Lord filled the temple" (Eze 43:5; 3:12) [D2]
  - applies to 1 occurrence(s): 2Cor 4:6 (knowledge)
- **Observation 16312** (prior-capture, tag statement, status draft): The soul knows itself as made: "I praise you, for I am fearfully and wonderfully made … my soul knows it very well" (Psa 139:14).
  - applies to 1 occurrence(s): Psa 139:14 (knows)
- **Observation 16371** (prior-capture, tag statement, status draft): The heart tested for obedience: "testing you to know what was in your heart, whether you would keep his commandments" (Deu 8:2).
  - applies to 1 occurrence(s): Deu 8:2 (know)
- **Observation 16393** (prior-capture, tag statement, status draft): 7.3 Fellowship, assembly, sharing: "all the churches will know that I am he who searches mind and heart" (Rev 2:23); "the assembly of the firstborn … and to the spirits of the righteous made perfect" (Heb 12:23) [H2]; "the Spirit of the Lord came upon Jahaziel … in the midst of the assembly" (2Ch 20:14) [D1]; "I have not hidden your deliverance within my heart … from the great congregation" (Psa 40:10)
  - applies to 1 occurrence(s): Rev 2:23 (know)
- **Observation 16397** (prior-capture, tag statement, status draft): 8.1 God tests the heart: "I know, my God, that you test the heart" (1Ch 29:17); "I the Lord search the heart and test the mind" (Jer 17:10); "the Lord tests hearts" — like crucible and furnace (Pro 17:3); "Search me, O God, and know my heart! Try me and know my thoughts!" (Psa 139:23); "Prove me, O Lord, and try me; test my heart and my mind" (Psa 26:2); "You have tried my heart … you will find nothing" (Psa 17:3); "you who test the minds and hearts" (Psa 7:9; Jer 11:20; 20:12); "you … test my heart toward you" (Jer 12:3); "God who tests our hearts" (1Th 2:4); "testing you to know what was in your heart" (Deu 8:2); "the Lord your God is testing you, to know whether you love … with all your h ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): Deu 8:2 (know), Deu 13:3 (know), 1Ch 29:17 (know), 2Ch 32:31 (know), Psa 139:23 (know)
- **Observation 16409** (prior-capture, tag statement, status draft): Forgiveness keyed to the heart: "forgive … and render to each whose heart you know … (for you, you only, know the hearts of all the children of mankind)" (1Ki 8:39; 2Ch 6:30). Only God knows hearts; that is the ground of his judging and forgiving.
  - applies to 2 occurrence(s): 1Ki 8:39 (know), 2Ch 6:30 (know)
- **Observation 16426** (prior-capture, tag statement, status draft): Soul and mercy: "Be merciful to me … for in you my soul takes refuge" (Psa 57:1); "Be gracious to me … my soul and my body also" (Psa 31:9); "you have known the distress of my soul" (Psa 31:7); "great is your steadfast love … you have delivered my soul from the depths of Sheol" (Psa 86:13); "heal me [*my soul*], for I have sinned" (Psa 41:4); "for to you I lift up my soul" (Psa 143:8)
  - applies to 1 occurrence(s): Psa 31:7 (known)
- **Observation 16480** (prior-capture, tag statement, status draft): Covering: "he who is trustworthy in spirit keeps a thing covered" (Pro 11:13); "A prudent man conceals knowledge, but the heart of fools proclaims folly" (Pro 12:23); "I have not hidden your deliverance within my heart" (Psa 40:10); "the Lord has poured out upon you a spirit of deep sleep … and covered your heads (the seers)" (Isa 29:10) [X]; "my soul shall exult … he has covered me with the robe of righteousness" (Isa 61:10)
  - applies to 1 occurrence(s): Pro 12:23 (knowledge)
- **Observation 16500** (prior-capture, tag statement, status draft): 1.2 Integrity of heart (*tōm lēvāv*) [lexical]: "In the integrity of my heart and the innocence of my hands I have done this" (Gen 20:5). God replies: "I know that you have done this in the integrity of your heart, and it was I who kept you from sinning" (Gen 20:6).; "if you will walk before me … with integrity of heart and uprightness" (1Ki 9:4); "With upright [*integrity of*] heart he shepherded them" (Psa 78:72); "I will walk with integrity of heart within my house" (Psa 101:2); "May my heart be blameless in your statutes" (Psa 119:80)
  - applies to 1 occurrence(s): Gen 20:6 (know)
- **Observation 16513** (prior-capture, tag statement, status draft): Heart set, heart gone elsewhere: "Ezra had set his heart to study the Law … and to teach his statutes and rules" (Ezr 7:10); "they rejected my rules … for their heart went after their idols" (Eze 20:16); "that he may incline our hearts to him … to keep … his rules" (1Ki 8:58)
  - applies to 1 occurrence(s): Ezr 7:10 (study)
- **Observation 16534** (prior-capture, tag statement, status draft): NT: "evil spirits came out of them" (Act 19:12); "the evil spirit answered them, 'Jesus I know, and Paul I recognize, but who are you?'" (Act 19:15); "the man in whom was the evil spirit leaped on them" (Act 19:16); "healed … of evil spirits" (Luk 7:21; 8:2); "seven other spirits more evil than itself … the last state of that person is worse than the first" (Mat 12:45; Luk 11:26); "the spiritual forces of evil in the heavenly places" — "not … against flesh and blood" (Eph 6:12); "What if a spirit or an angel spoke to him?" (Act 23:9) [O]
  - applies to 2 occurrence(s): Act 19:15 (know), Act 19:15 (recognize)
- **Observation 16550** (prior-capture, tag statement, status draft): 2.4 Blasphemy against the Spirit [D]: "the blasphemy against the Spirit will not be forgiven" (Mat 12:31) [D2]; "whoever blasphemes against the Holy Spirit never has forgiveness, but is guilty of an eternal sin" (Mar 3:29; Luk 12:10) [D1]; "If you then, who are evil, know how to give good gifts … how much more will the heavenly Father give the Holy Spirit" (Luk 11:13) [D1] — evil humans, given the Spirit
  - applies to 1 occurrence(s): Luk 11:13 (know)
- **Observation 16557** (prior-capture, tag statement, status draft): 2.6 Discerning good and evil: "Give your servant therefore an understanding mind [*hearing heart*] … that I may discern between good and evil" (1Ki 3:9); "the wise heart will know the proper time and the just way … will know no evil thing" (Ecc 8:5); "I turned my heart to know … the wickedness of folly" (Ecc 7:25); "I would not be able … to do either good or bad of my own will [*heart*]" (Num 24:13) — Balaam's heart subordinated to the word; "those who say in their hearts, 'The Lord will not do good, nor will he do ill'" (Zep 1:12) — the complacent heart denies God's agency
  - applies to 2 occurrence(s): Ecc 7:25 (know), Ecc 8:5 (know)
- **Observation 16559** (prior-capture, tag statement, status draft): 2.8 ◆ Fringe: "No man has power to retain the spirit … nor will wickedness deliver those who are given to it" (Ecc 8:8) [U]; "uncircumcised in heart and flesh" (Eze 44:7) — heart and flesh share one state; "I know your presumption and the evil of your heart" (1Sa 17:28) — Eliab misreads David's heart (also M08, §9.5); "who tear the skin from off my people and their flesh from off their bones" (Mic 3:2); "When evildoers assail me to eat up my flesh" (Psa 27:2); "Should good be repaid with evil? Yet they have dug a pit for my life" (Jer 18:20)
  - applies to 1 occurrence(s): 1Sa 17:28 (know)
- **Observation 16562** (prior-capture, tag statement, status draft): Realising guilt afterwards: "though he did not know it, then realizes his guilt, he shall bear his iniquity" (Lev 5:17); "it is hidden from him, when he comes to know it, and he realizes his guilt" (Lev 5:4; 5:2); "that person realizes his guilt" (Num 5:6)
  - applies to 3 occurrence(s): Lev 5:4 (know), Lev 5:4 (realizes), Lev 5:17 (know)
- **Observation 16688** (prior-capture, tag statement, status draft): NT: "he has scattered the proud in the thoughts of their hearts" (Luk 1:51); "God knows your hearts. For what is exalted among men is an abomination" (Luk 16:15); "if you have bitter jealousy and selfish ambition in your hearts, do not boast" (Jam 3:14)
  - applies to 1 occurrence(s): Luk 16:15 (knows)
- **Observation 16706** (prior-capture, tag statement, status draft): 9.5 ◆ Fringe: "man looks on the outward appearance [*height of stature*], but the Lord looks on the heart" (1Sa 16:7); "As the heavens for height … so the heart of kings is unsearchable" (Pro 25:3) — height as depth; "I know your presumption and the evil of your heart" (1Sa 17:28) — pride attributed to David's heart by his brother, wrongly; a misreading of another's heart; "Zebulun is a people who risked [*despised*] their lives to the death" (Judg 5:18) — the *nephesh* held cheap for a cause (R10); "my heart does not reproach me for any of my days" (Job 27:6) — the heart as internal accuser, silent (cf. §3.3 2Sa 24:10); "Be wise, my son, and make my heart glad, that I may answer him who rep ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 17:28 (know)
- **Observation 16708** (prior-capture, tag statement, status draft): Failing to: "you his son, Belshazzar, have not humbled your heart, though you knew all this" (Dan 5:22) — knowledge without humbling.
  - applies to 1 occurrence(s): Dan 5:22 (knew)
- **Observation 16735** (prior-capture, tag statement, status draft): 1.2 The heart that claims a throne: "You said in your heart, 'I will ascend to heaven … I will set my throne on high'" (Isa 14:13); "in his own mind he shall become great … he shall even rise up against the Prince of princes" (Dan 8:25); "in her heart she says, 'I sit as a queen, I am no widow'" (Rev 18:7); "the arrogant heart of the king of Assyria" (Isa 10:12); "Your heart was proud because of your beauty … I exposed you before kings" (Eze 28:17); "when his heart was lifted up and his spirit was hardened … he was brought down from his kingly throne" (Dan 5:20). Then "his mind was made like that of a beast … until he knew that the Most High God rules the kingdom of mankind" (5:21). See Batc ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Dan 5:21 (knew)
- **Observation 16741** (prior-capture, tag statement, status draft): The heart read by another | "Joab … knew that the king's heart went out to Absalom" (14:1) → Joab stages the Tekoite woman's case
  - applies to 1 occurrence(s): 2Sa 14:1 (knew)
- **Observation 16757** (prior-capture, tag statement, status draft): The formula without the authority. Context read: Act 19:13–16. "I adjure you by the Jesus whom Paul proclaims" → "Jesus I know … but who are you?" → the man with the evil spirit "mastered all of them" (19:16) [O]. The spirit masters those who use the name without the relation.
  - applies to 1 occurrence(s): Act 19:15 (know)
- **Observation 16786** (prior-capture, tag statement, status draft): 2.4 Riches moved inward (NT): "according to the riches of his glory he may grant you to be strengthened with power through his Spirit in your inner being" (Eph 3:16) [D1]; "having the eyes of your hearts enlightened, that you may know … the riches of his glorious inheritance" (Eph 1:18); "that their hearts may be encouraged … to reach all the riches of full assurance of understanding" (Col 2:2); "Let the word of Christ dwell in you richly … singing … spiritual songs, with thankfulness in your hearts" (Col 3:16)
  - applies to 1 occurrence(s): Eph 1:18 (know)
- **Observation 16801** (prior-capture, tag statement, status draft): The way follows the heart: "he went on backsliding in the way of his own heart" (Isa 57:17); "Walk in the ways of your heart and the sight of your eyes. But know that … God will bring you into judgment" (Ecc 11:9) → Batch F §7.4; "if … my heart has gone after my eyes" (Job 31:7)
  - applies to 1 occurrence(s): Ecc 11:9 (know)
- **Observation 16804** (prior-capture, tag statement, status draft): Weighing: "All the ways of a man are pure in his own eyes, but the Lord weighs the spirit" (Pro 16:2) [H2]; "Every way of a man is right in his own eyes, but the Lord weighs the heart" (Pro 21:2); "I the Lord search the heart … to give every man according to his ways" (Jer 17:10); "render to each whose heart you know, according to all his ways" (2Ch 6:30)
  - applies to 1 occurrence(s): 2Ch 6:30 (know)
- **Observation 16822** (prior-capture, tag statement, status draft): God, watching and weighing | "does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it?" (Pro 24:12)
  - applies to 1 occurrence(s): Pro 24:12 (know)
- **Observation 16839** (prior-capture, tag statement, status draft): 6.2 The heart as judge of the self: "You are those who justify yourselves before men, but God knows your hearts" (Luk 16:15)
  - applies to 1 occurrence(s): Luk 16:15 (knows)
- **Observation 16841** (prior-capture, tag statement, status draft): 6.2 The heart as judge of the self: "Faithless Israel has shown herself [*her nephesh*] more righteous than treacherous Judah" (Jer 3:11) — comparative justification; "I do not say this to condemn you, for … you are in our hearts, to die together and to live together" (2Co 7:3); [Claude reading] The heart can condemn the self (1Jo 3:20) or justify it (Job 32:2; Luk 16:15). In both cases the text places a higher court above it: "God is greater than our heart"; "God knows your hearts". 1Jo 3 is the gentler reading: the self-condemning heart is reassured, not overruled harshly. In 2Co 7:3 condemnation is set aside because the other person is held in the heart.
  - applies to 2 occurrence(s): Luk 16:15 (knows), 1Jo 3:20 (knows)
- **Observation 16858** (prior-capture, tag statement, status draft): Revisit (Batch G §4): just before this, Abner answers the same question with an oath: "As your soul lives, O king, I do not know" (1Sa 17:55). A formal oath by Saul's soul stands on the threshold of Jonathan's soul being knit to David's.
  - applies to 1 occurrence(s): 1Sa 17:55 (know)
- **Observation 16932** (prior-capture, tag statement, status draft): What the pattern shows [Claude reading]: The merry heart is a threshold state. In every narrative it comes after eating and drinking and immediately before a decisive event, which others usually initiate. The good heart lowers guard. What enters at that moment decides the outcome: murder (Amnon); exposure and anger (Vashti, Ahasuerus); mockery turned to catastrophe (Samson); outrage (Gibeah); approach and redemption (Ruth); a dead heart the next morning (Nabal); God's claim on the soul (the rich fool); The heart's condition swings overnight. Nabal: merry heart → dead heart (1Sa 25:36–37). Ahasuerus: merry heart → burning anger (Est 1:10–12). The heart's state is not stable; wine sets it high ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Ecc 11:9 (know)
- **Observation 17017** (prior-capture, tag statement, status draft): Good to the soul: "knowledge will be pleasant to your soul" (Pro 2:10); "Gracious words are … sweetness to the soul and health to the body" (Pro 16:24); "your consolations cheer my soul" (Psa 94:19) — against "the cares of my heart"; "find rest for your souls" (Jer 6:16)
  - applies to 1 occurrence(s): Pro 2:10 (knowledge)
- **Observation 17041** (prior-capture, tag statement, status draft): Desire without knowledge: "Desire [*nephesh*] without knowledge is not good" (Pro 19:2; Batch B §1.5).
  - applies to 1 occurrence(s): Pro 19:2 (knowledge)
- **Observation 17064** (prior-capture, tag statement, status draft): 2.4 The mind-set of flesh and Spirit (*phronēma*): "to set the mind on the flesh is death, but to set the mind on the Spirit is life and peace" (Rom 8:6) [D3]; "the mind that is set on the flesh is hostile to God" (Rom 8:7); "he who searches hearts knows what is the mind of the Spirit" (Rom 8:27) [D2]
  - applies to 1 occurrence(s): Rom 8:27 (knows)
- **Observation 17067** (prior-capture, tag statement, status draft): 2.5 ◆ Spirit and resolve — fringe: "an excellent spirit was in him. And the king planned to set him over the whole kingdom" (Dan 6:3) [H2+X] — a quality of spirit prompts another's plan.; "in whose spirit there is no deceit" beside "the Lord counts no iniquity" (Psa 32:2) [H1].; "his mind was made like that of a beast … until he knew that the Most High … sets over it whom he will" (Dan 5:21).
  - applies to 1 occurrence(s): Dan 5:21 (knew)
- **Observation 17069** (prior-capture, tag statement, status draft): Spirit of whoredom [X]: "a spirit of whoredom has led them astray" (Hos 4:12); "the spirit of whoredom is within them, and they know not the Lord" (Hos 5:4)
  - applies to 1 occurrence(s): Hos 5:4 (know)
- **Observation 17102** (prior-capture, tag statement, status draft): 6.4 Hope and the NT inner seat: "my heart was glad … my flesh also will dwell in hope" (Act 2:26) — flesh in hope; "hope does not put us to shame, because God's love has been poured into our hearts through the Holy Spirit" (Rom 5:5) [D1]; "by the power of the Holy Spirit you may abound in hope" (Rom 15:13) [D1]; "through the Spirit, by faith, we ourselves eagerly wait for the hope of righteousness" (Gal 5:5) [D3]; "one body and one Spirit … one hope" (Eph 4:4) [D1]; "the eyes of your hearts enlightened, that you may know what is the hope" (Eph 1:18); "in your hearts honor Christ … a reason for the hope that is in you" (1Pe 3:15); "waiting for the consolation of Israel, and the Holy Spirit wa ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Eph 1:18 (know)
- **Observation 17107** (prior-capture, tag statement, status draft): Setting the heart to seek (cf. Batch B §0.1): "set your mind and heart [*heart and soul*] to seek the Lord" (1Ch 22:19); "those who had set their hearts to seek the Lord" (2Ch 11:16); "you … have set your heart to seek God" (2Ch 19:3); "who sets his heart to seek God … even though not according to the sanctuary's rules" (2Ch 30:19); "Ezra had set his heart to study [*seek*] the Law" (Ezr 7:10); Failure: "he did evil, for he did not set his heart to seek the Lord" (2Ch 12:14)
  - applies to 1 occurrence(s): Ezr 7:10 (study)
- **Observation 17112** (prior-capture, tag statement, status draft): 7.3 The heart seeks knowledge: "The heart of him who has understanding seeks knowledge" (Pro 15:14); "An intelligent heart acquires knowledge" (Pro 18:15); "I applied my heart to seek and to search out by wisdom" (Ecc 1:13); "I turned my heart to know and to search out and to seek wisdom" (Ecc 7:25)
  - applies to 3 occurrence(s): Pro 15:14 (knowledge), Pro 18:15 (knowledge), Ecc 7:25 (know)
- **Observation 17117** (prior-capture, tag statement, status draft): God tests the heart: "God left him to himself, in order to test him and to know all that was in his heart" (2Ch 32:31).
  - applies to 1 occurrence(s): 2Ch 32:31 (know)
- **Observation 17173** (prior-capture, tag statement, status draft): 10. Madness (M66): "the hearts of the children of man are full of evil, and madness is in their hearts while they live" (Ecc 9:3); "The Lord will strike you with madness and blindness and confusion of mind [*heart*]" (Deu 28:28); "I applied my heart to know wisdom and to know madness and folly … a striving after wind" (Ecc 1:17); "I turned my heart to know … the foolishness that is madness" (Ecc 7:25); "The prophet is a fool; the man of the spirit is mad" (Hos 9:7) [U]; [Claude reading] Madness is located in the heart (Ecc 9:3; Deu 28:28). The heart can also investigate madness (Ecc 1:17; 7:25). Hos 9:7 is the only verse linking madness to "spirit", and its spirit is not determinable.
  - applies to 2 occurrence(s): Ecc 1:17 (know), Ecc 7:25 (know)
- **Observation 17236** (prior-capture, tag statement, status draft): d. Thinking, planning, understanding, remembering: *Plans and devising:* Pro 16:1, 9; 19:21; 6:14, 18; 24:2; 12:20; Psa 140:2; 58:2; Zec 7:10; 8:17; Isa 10:7; Act 5:4; Eze 38:10.; *Understanding and knowing:*; "a heart to understand" (Deu 29:4); "understanding mind" (1Ki 3:9); "understand with their hearts" (Isa 6:10; Mat 13:15; Joh 12:40; Act 28:27); "an intelligent heart acquires knowledge" (Pro 18:15); "the heart of the hasty will understand" (Isa 32:4); *Remembering and "laying to heart":*; Isa 47:7; 57:1, 11; 42:25; Mal 2:2; Jer 12:11; Ecc 7:2; 9:1; Deu 4:39; 32:46; 1Sa 21:12; "call to mind" (Lam 3:21; Deu 30:1); "come into mind" (Jer 3:16; 7:31; 19:5; 32:35; 44:21; 51:50; Isa 65:17); H ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 18:15 (knowledge)
- **Observation 17242** (prior-capture, tag statement, status draft): j. The heart's own "senses": fringe: "having the eyes of your hearts enlightened" (Eph 1:18); "God … has shone in our hearts to give the light of the knowledge" (2Co 4:6); "until … the morning star rises in your hearts" (2Pe 1:19); "a veil lies over their hearts" (2Co 3:15).; fringe: "I slept, but my heart was awake" (Song 5:2); "Even in the night his heart does not rest" (Ecc 2:23).
  - applies to 1 occurrence(s): 2Cor 4:6 (knowledge)
- **Observation 17244** (prior-capture, tag statement, status draft): l. The heart's opacity and privacy: "The heart is deceitful above all things, and desperately sick; who can understand it?" (Jer 17:9); "the heart of kings is unsearchable" (Pro 25:3); "The heart knows its own bitterness, and no stranger shares its joy" (Pro 14:10); "he knows the secrets of the heart" (Psa 44:21); "the secrets of his heart are disclosed" (1Co 14:25); "disclose the purposes of the heart" (1Co 4:5); Only God knows it: 1Ki 8:39; 2Ch 6:30; 1Sa 16:7 ("man looks on the outward appearance, but the Lord looks on the heart"); Luk 16:15; Act 1:24 ("heart-knower"); Act 15:8; "who can say, 'I have made my heart pure'?" (Pro 20:9)
  - applies to 3 occurrence(s): Psa 44:21 (knows), Pro 14:10 (knows), Luk 16:15 (knows)
- **Observation 17245** (prior-capture, tag statement, status draft): m. Heart as the seat of self-judgment (conscience function in the OT): "David's heart struck him" (1Sa 24:5; 2Sa 24:10); "pangs of conscience" — ESV for *lēv* (1Sa 25:31); "Your heart knows that many times you yourself have cursed others" (Ecc 7:22); "my heart does not reproach me" (Job 27:6); NT: "whenever our heart condemns us, God is greater than our heart … if our heart does not condemn us, we have confidence" (1Jo 3:20–21)
  - applies to 1 occurrence(s): Ecc 7:22 (knows)
- **Observation 17256** (prior-capture, tag statement, status draft): b. What the soul characteristically does: *Needs and seeks:* thirsts, longs, pants, faints (Psa 107:5; 119:81; Isa 26:8–9), waits (Psa 33:20; 62:1, 5; 130:5–6), hopes (Lam 3:24), clings (Psa 63:8; 119:25 "clings to the dust").; *Suffers:*; bitter (1Sa 1:10; 22:2; 30:6; Job 3:20; 7:11; 10:1; 21:25; 27:2; Isa 38:15; Eze 27:31); cast down, in turmoil (Psa 42:5, 6, 11; 43:5); bowed down (Psa 44:25; 57:6; Lam 3:20); poured out (1Sa 1:15; Job 30:16; Psa 42:4; Isa 53:12 "poured out his soul to death"); refuses comfort (Psa 77:2); is troubled (Psa 6:3; Joh 12:27); "very sorrowful, even to death" (Mat 26:38; Mar 14:34); "my soul is bereft of peace; I have forgotten what happiness is" (Lam 3:17); "vex ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 139:14 (knows)
- **Observation 17260** (prior-capture, tag statement, status draft): b. The human spirit: *Troubled, anxious:* Gen 41:8; Dan 2:1, 3; 7:15 ("my spirit within me was anxious, and the visions of my head alarmed me"); Joh 13:21; 2Co 2:13.; *Revived:*; after eating ("his spirit revived" 1Sa 30:12); after drinking ("his spirit returned, and he revived" Judg 15:19); on good news (Gen 45:27); *Broken, crushed:* Exo 6:9 ("broken spirit and harsh slavery"); Pro 15:4, 13; 17:22; 18:14 ("A man's spirit will endure sickness, but a crushed spirit who can bear?"); Job 17:1; Psa 34:18; 51:17.; *Faint, failing:* Psa 77:3; 142:3; 143:4, 7; Isa 57:16; 61:3.; *Lowly, contrite vs proud, haughty:* Isa 57:15; 66:2; Pro 16:18–19; 29:23; Ecc 7:8; Mat 5:3 ("poor in spirit").; *Governe ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Cor 2:11 (knows)
- **Observation 17263** (prior-capture, tag statement, status draft): d. God's Spirit acting on and in the inner seat: *Comes upon, rushes upon, clothes:* Judg 3:10; 6:34; 14:6, 19; 15:14; 1Sa 10:6, 10 ("be turned into another man"); 16:13; 1Ch 12:18; 2Ch 24:20.; *Fills with ability:* "filled him with the Spirit of God, with ability and intelligence, with knowledge and all craftsmanship" (Exo 31:3; 35:31).; *Enters and sets on feet:* Eze 2:2; 3:24.; *Put within → changed conduct:* "I will put my Spirit within you, and cause you to walk in my statutes" (Eze 36:27; 37:14).; *Dwells in:* Rom 8:9, 11; 1Co 3:16; "your body is a temple of the Holy Spirit within you" (1Co 6:19); 2Ti 1:14; Jam 4:5 ("the spirit that he has made to dwell in us").; *Bears witness with ou ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Exo 31:3 (knowledge), Exo 35:31 (knowledge), Rom 8:27 (knows)
- **Observation 17264** (prior-capture, tag statement, status draft): e. Wind and breath in relation to the inner being — explicitly retained per the researcher: *Breath = life in flesh:*; "all flesh in which is the breath of life" (Gen 6:17; 7:15, 22); "sinews … flesh … skin … But there was no breath in them" → "breath came into them, and they lived" (Eze 37:6–10); "When you take away their breath, they die and return to their dust" (Psa 104:29); *Breath and thought:* "When his breath departs, he returns to the earth; on that very day his plans perish" (Psa 146:4). Link to the thought vocabulary (see brief §5).; *Breath as frailty:* "Remember that my life is a breath" (Job 7:7); "They all have the same breath, and man has no advantage over the beasts" (Ecc 3: ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Job 15:2 (knowledge), Ecc 1:17 (know)
- **Observation 17270** (prior-capture, tag statement, status draft): 3.1 Parallel and interchangeable (poetic pairing): *Heart // spirit:*; "Create in me a clean heart … renew a right spirit within me" (Psa 51:10); "a broken spirit; a broken and contrite heart" (Psa 51:17); "brokenhearted … crushed in spirit" (Psa 34:18); "revive the spirit of the lowly … the heart of the contrite" (Isa 57:15); "my spirit faints within me; my heart within me is appalled" (Psa 143:4); "Every heart will melt … every spirit will faint" (Eze 21:7); "heart was not steadfast … spirit was not faithful" (Psa 78:8); "meditate in my heart … my spirit made a diligent search" (Psa 77:6); "whose heart stirred him … whose spirit moved him" (Exo 35:21); "gladness of heart … pain of heart … ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 2:10 (knowledge)
- **Observation 17271** (prior-capture, tag statement, status draft): 3.1 Parallel and interchangeable (poetic pairing): [Claude reading] The translators move between heart, soul, spirit and mind when rendering the same Hebrew or Greek word. That movement is itself evidence that the words' ranges overlap.
  - applies to 1 occurrence(s): Pro 2:10 (knowledge)
- **Observation 17272** (prior-capture, tag statement, status draft): 3.2 Totality and wholeness formulas: *Heart and soul (and might):*; "with all your heart and with all your soul (and with all your might)" (Deu 4:29; 6:5; 10:12; 11:13; 13:3; 26:16; 30:2, 6, 10; Jos 22:5; 1Ki 2:4; 8:48; 2Ki 23:3, 25; 2Ch 6:38; 15:12; 34:31; Jer 32:41 — said of God); "you know in your hearts and souls" (Jos 23:14); "lay up these words … in your heart and in your soul" (Deu 11:18); "keep your soul diligently, lest … they depart from your heart" (Deu 4:9); "I am with you heart and soul" (1Sa 14:7, ESV idiom; only *lēvāv* is tagged); "one heart and soul" (Act 4:32); *NT expansion — heart, soul, mind, strength:* Mat 22:37; Mar 12:30; Luk 10:27; "heart … understanding … strength" ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jos 23:14 (know)
- **Observation 17279** (prior-capture, tag statement, status draft): 3.8 The inner seat shared or joined between persons ◆ fringe cluster: *Soul to soul:*; "the soul of Jonathan was knit to the soul of David, and Jonathan loved him as his own soul" (1Sa 18:1, 3; 20:17); "your friend who is as your own soul" (Deu 13:6, with "the wife you embrace"); "his life is bound up in the boy's life" (Gen 44:30); *Heart to heart:* "my heart will be joined to you" (1Ch 12:17); "Is your heart true to my heart as mine is to yours?" (2Ki 10:15); "you are in our hearts, to die together and to live together" (2Co 7:3); "I hold you in my heart" (Phili 1:7); "in person not in heart" (1Th 2:17).; *Shared across a group:* "one heart and soul" (Act 4:32); "one spirit, with one mind" ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Exo 23:9 (know)
- **Observation 17280** (prior-capture, tag statement, status draft): 3.9 The boundary of death — where the components come apart: *Soul departs:* "as her soul was departing" (Gen 35:18); soul to Sheol, pit, silence (§2.2d).; *Spirit and breath return to God:*; "the dust returns to the earth as it was, and the spirit returns to God who gave it" (Ecc 12:7); "Who knows whether the spirit of man goes upward and the spirit of the beast goes down into the earth?" (Ecc 3:21); "When you take away their breath, they die and return to their dust" (Psa 104:29); "Into your hand I commit my spirit" (Psa 31:5; Luk 23:46; Act 7:59); "No man has power to retain the spirit" (Ecc 8:8); *Return to life:*; "her spirit returned, and she got up" (Luk 8:55); "the life of the child ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Ecc 3:21 (knows)
- **Observation 17282** (prior-capture, tag statement, status draft): 4. Fringe observations collected (quick list): Heart = "midst" of sea, heaven, earth; the inner seat named as the *middle* (§2.1a).; Aaron carries the tribes "on his heart" before the Lord (Exo 28:29–30).; "I slept, but my heart was awake" (Song 5:2).; "Eyes of your hearts" (Eph 1:18); morning star rising in hearts (2Pe 1:19); a veil over hearts (2Co 3:15).; "Walls of my heart" (Jer 4:19); "tear open their breast" (Hos 13:8); a man without self-control = "a city … without walls" (Pro 25:28, rûaḥ). The inner seat is imaged as an enclosure.; Nabal's heart "died within him, and he became as a stone" after the wine left (1Sa 25:37).; Nephesh = neck/throat (Psa 69:1; 105:18) and = corpse (Num 19: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 14:10 (knows)
- **Observation 17283** (prior-capture, tag statement, status draft): 4. Fringe observations collected (quick list): God's own heart and soul (§3.10).
  - applies to 1 occurrence(s): Pro 14:10 (knows)
- **Observation 17411** (prior-capture, tag statement, status draft): The command names the desire, and sin multiplies it. *"I would not have known what it is to covet if the law had not said, 'You shall not covet.' But sin, seizing an opportunity through the commandment, produced in me all kinds of covetousness"* (Rom 7:7–8). I read the command as making the desire known, and sin as using that very knowledge.
  - applies to 1 occurrence(s): Rom 7:7 (known)
- **Observation 17413** (prior-capture, tag statement, status draft): The opposite, lived. Paul: *"I coveted no one's silver or gold or apparel. You yourselves know that these hands ministered to my necessities … 'It is more blessed to give than to receive'"* (Act 20:33–35). The hands that might have taken work and give.
  - applies to 1 occurrence(s): Act 20:34 (know)
- **Observation 17417** (prior-capture, tag statement, status draft): Keeps learning from arriving: *"led astray by various passions, always learning and never able to arrive at a knowledge of the truth"* (2Ti 3:6–7)
  - applies to 1 occurrence(s): 2Ti 3:7 (knowledge)
- **Observation 17423** (prior-capture, tag statement, status draft): Knowing God. *"not in the passion of lust like the Gentiles who do not know God"* (1Th 4:5); *"the passions of your former ignorance"* (1Pe 1:14). In two verses the uncontrolled desire stands beside not knowing.
  - applies to 1 occurrence(s): 1Th 4:5 (know)
- **Observation 17457** (prior-capture, tag statement, status draft): No contentment. *"Because he knew no contentment in his belly, he will not let anything in which he delights escape him"* (Job 20:20).
  - applies to 1 occurrence(s): Job 20:20 (knew)
- **Observation 17515** (prior-capture, tag statement, status draft): Passage: the friends say *"God stores up their iniquity for their children"* (21:19). Job answers, *"Let him pay it out to them, that they may know it. Let their own eyes see their destruction"* (21:19–20).
  - applies to 1 occurrence(s): Job 21:19 (know)
- **Observation 17522** (prior-capture, tag statement, status draft): Passage: before it, *"For I know that the Lord is great, and that our Lord is above all gods"* (135:5). After it, clouds, lightning and wind (135:7). Later, the idols that cannot speak or see (135:15–18).
  - applies to 1 occurrence(s): Psa 135:5 (know)
- **Observation 17609** (prior-capture, tag statement, status draft): What he delights in: "steadfast love, justice, and righteousness" (Jer 9:24). The verse before forbids boasting in wisdom, might and riches. The one who may boast boasts "that he understands and knows me". "His delight is not in the strength of the horse, nor his pleasure in the legs of a man" (Psa 147:10), beside "those who fear him" (147:11, already in 10.9). Strength is turned down twice, once as a boast and once as a delight.
  - applies to 1 occurrence(s): Jer 9:24 (knows)
- **Observation 17619** (prior-capture, tag statement, status draft): As something known: "By this I know that you delight in me: my enemy will not shout in triumph over me" (Psa 41:11), from a man whose "close friend … has lifted his heel against me" (41:9). He learns of the delight from what did not happen.
  - applies to 1 occurrence(s): Psa 41:11 (know)
- **Observation 17632** (prior-capture, tag statement, status draft): Looks right: "they seek me daily and delight to know my ways, as if they were a nation that did righteousness … they delight to draw near to God" (Isa 58:2). The next verse, already in 10.6, is "you seek your own pleasure, and oppress all your workers" (58:3). The delight is real enough to be named twice. I read that delight in religion can sit beside oppression without either one cancelling the other in the person's own eyes.
  - applies to 1 occurrence(s): Isa 58:2 (know)
- **Observation 17634** (prior-capture, tag statement, status draft): Not wanting him, by reckoning: "Depart from us! We do not desire the knowledge of your ways. What is the Almighty, that we should serve him? And what profit do we get if we pray to him?" (Job 21:14–15), said by those who "spend their days in prosperity" (21:13).
  - applies to 1 occurrence(s): Job 21:14 (knowledge)
- **Observation 17660** (prior-capture, tag statement, status draft): Pro 9:17–18. "Stolen water is sweet". The sweetness is in the stealing. "he does not know that the dead are there."
  - applies to 1 occurrence(s): Pro 9:18 (know)
- **Observation 17677** (prior-capture, tag statement, status draft): Knowing it.: *"If anyone's will is to do God's will, he will know whether the teaching is from God"* (Joh 7:17). The willing comes first, and the knowing follows it.; Paul was *"appointed … to know his will"* (Act 22:14), and was told the next moment *"why do you wait?"* (22:16).; *"Do not be foolish, but understand what the will of the Lord is"* (Eph 5:17), with *"be filled with the Spirit"* (5:18).; Knowing can stand without doing: *"you … know his will and approve what is excellent"* (Rom 2:18), said to one who *"boast[s] in God"* (2:17) and teaches others (2:19–21).; The servant *"who knew his master's will but did not get ready or act according to his will"* is beaten more than the one ... (cut; the whole text is in the workbook)
  - applies to 5 occurrence(s): Luk 12:47 (knew), Luk 12:48 (know), Joh 7:17 (know), Act 22:14 (know), Rom 2:18 (know)
- **Observation 17682** (prior-capture, tag statement, status draft): Who does it, and who is related by it.: *"whoever does the will of my Father in heaven is my brother and sister and mother"* (Mat 12:50; Mar 3:35). It is said with his hand stretched toward his disciples, while his family stands outside.; *"if anyone is a worshiper of God and does his will, God listens to him"* (Joh 9:31). The man born blind says it against those who said *"we do not know where he comes from"* (9:29).
  - applies to 2 occurrence(s): Joh 9:29 (know), Joh 9:31 (know)
- **Observation 17748** (prior-capture, tag statement, status draft): Sincere, aimed at God, and wrong for lack of knowledge | Rom 10:1–3; Gal 1:13–16; Phi 3:6–7; Act 22:3–4; Act 21:20–21 | Paul's own zeal, three times named beside persecution. Ended not by his correction but by God's revealing. He meets the same zeal in his people with prayer
  - applies to 1 occurrence(s): Rom 10:2 (knowledge)
- **Observation 17776** (prior-capture, tag statement, status draft): Joh 19:28–30; Psa 69:20–21 | "knowing that all was now finished … 'I thirst'"; sour wine; "It is finished". The psalm sets the thirst beside "I looked for pity, but there was none" | The one who offered water thirsts, and says it knowingly. I read the want spoken, not hidden
  - applies to 1 occurrence(s): Joh 19:28 (knowing)
- **Observation 17782** (prior-capture, tag statement, status draft): Isa 5:11–13 | running after strong drink, not regarding the deeds of the Lord | "lack of knowledge"; the drinkers end thirsty
  - applies to 1 occurrence(s): Isa 5:13 (knowledge)
- **Observation 17801** (prior-capture, tag statement, status draft): Not known: Job 28:13, 16. Proverbs states the worth; Job says man does not know it. I read the two together as worth and blindness to it, not as contradiction.
  - applies to 1 occurrence(s): Job 28:13 (know)
- **Observation 17816** (prior-capture, tag statement, status draft): 1Sa 3:1–9 | 10.2 | the word rare; Samuel did not yet know the Lord; Eli perceived it and taught the answer. I read hearing that had to be learned
  - applies to 2 occurrence(s): 1Sa 3:7 (know), 1Sa 3:8 (perceived)
- **Observation 17848** (prior-capture, tag statement, status draft): It ends, and something follows.; *"So will I satisfy my wrath on you, and my jealousy shall depart from you. I will be calm and will no more be angry"* (Eze 16:42). The next verse names what had enraged him: *"Because you have not remembered the days of your youth"* (16:43).; *"And they shall know that I am the Lord—that I have spoken in my jealousy"* (Eze 5:13). The stated end is knowing.
  - applies to 1 occurrence(s): Eze 5:13 (know)
- **Observation 17849** (prior-capture, tag statement, status draft): Asked about in lament. *"How long, O Lord? Will you be angry forever? Will your jealousy burn like fire? Pour out your anger on the nations that do not know you"* (Psa 79:5–6). I read a people asking for the jealousy to end on them and to turn on others. The ledger reads the same (AG-88).
  - applies to 1 occurrence(s): Psa 79:6 (know)
- **Observation 17867** (prior-capture, tag statement, status draft): 11. Zeal passed on (Ch 11 §6): *"I know your readiness, of which I boast about you to the people of Macedonia … And your zeal has stirred up most of them"* (2Co 9:2). The zeal of one church stirs another. The stirring verb is the one used of fathers provoking children (Col 3:21; anger ledger AG-239). Here it is aimed at good.
  - applies to 1 occurrence(s): 2Cor 9:2 (know)
- **Observation 17900** (prior-capture, tag statement, status draft): The question. *"For who knows what is good for man while he lives the few days of his vain life, which he passes like a shadow?"* (Ecc 6:12). It closes the passage already in 10.6: the man who lacks nothing yet cannot enjoy it (6:2), and *"Better is the sight of the eyes than the wandering of the appetite"* (6:9).
  - applies to 1 occurrence(s): Ecc 6:12 (knows)
- **Observation 18001** (prior-capture, tag statement, status draft): Pointer, kept separate: 2Ch 32:31 says of these envoys that *"God left him to himself, in order to test him and to know all that was in his heart"*.
  - applies to 1 occurrence(s): 2Ch 32:31 (know)
- **Observation 18012** (prior-capture, tag statement, status draft): Ecc 4:13 | M16; M15 | "better" than a king *"who no longer knew how to take advice"*.
  - applies to 1 occurrence(s): Ecc 4:13 (knew)
- **Observation 18013** (prior-capture, tag statement, status draft): Jer 22:15 | M12 | "it was well with him" when he did justice; *"Is not this to know me?"* (22:16).
  - applies to 1 occurrence(s): Jer 22:16 (know)
- **Observation 18070** (prior-capture, tag statement, status draft): Jer 22:16–17 | judging the cause of the poor called "to know me"; eyes and heart only for gain | 10.2 *Knowing and hearing*; pointer from 10.6
  - applies to 1 occurrence(s): Jer 22:16 (know)
- **Observation 18094** (prior-capture, tag statement, status draft): 1Ki 2:15 is uncited. Adonijah: "You know that the kingdom was mine, and that all Israel fully; expected me to reign. However, the kingdom has turned about and become my brother's, for it was; his from the Lord". Then he asks for Abishag (2:17). A claimed right, given up in words to the; Lord's giving, with a request that follows it. The passage gives the outcome.
  - applies to 1 occurrence(s): 1Ki 2:15 (know)
- **Observation 18098** (prior-capture, tag statement, status draft): 2Sa 19:18 | Ziba's men cross *"to do his pleasure"*. Then Shimei falls down: *"your servant knows that I have sinned"* (19:20). Service, and a plea, at the king's return. It is read with 19:27–30. | 10.10 *Loyalty and honour*
  - applies to 1 occurrence(s): 2Sa 19:20 (knows)
- **Observation 18115** (prior-capture, tag statement, status draft): Envy of the wicked: seen, then embittered (Psa 73:1, 3, 20–22; Pro 23:17).: Psalm 73 begins with its conclusion: *"Truly God is good to Israel, to those who are pure in heart"* (73:1). This is OT-96 *ṭôb*. "Good" is a confession about God, set over the whole psalm.; Then: *"But as for me, my feet had almost stumbled … For I was envious of the arrogant when I saw the prosperity of the wicked"* (73:2–3). Envy comes in by sight, as desire does in 10.6.; In the sanctuary (73:17, already in 10.4) the prosperity is seen again: *"Like a dream when one awakes, O Lord, when you rouse yourself, you despise them as phantoms"* (73:20, H5782). What was envied turns out to be a dream, and God's rousing is ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 73:22 (ignorant)
- **Observation 18120** (prior-capture, tag statement, status draft): Over them: *"You adulterous people! Do you not know that friendship with the world is enmity with God? … Or do you suppose it is to no purpose that the Scripture says, 'He yearns jealously over the spirit that he has made to dwell in us'? But he gives more grace"* (Jam 4:4–6).; The picture is a husband's jealousy over a divided loyalty, aimed at "the spirit that he has made to dwell in us".; The next words are "But he gives more grace". This jealousy is answered with grace, not only with wrath. Compare Eze 36, where jealousy turns outward against enemies.; I read God's jealousy as the same burning with two objects: those who harm his people, and his people's own divided heart.
  - applies to 1 occurrence(s): Jam 4:4 (know)
- **Observation 18131** (prior-capture, tag statement, status draft): A heart that is a trap (Ecc 7:26). *"And I find something more bitter than death: the woman whose heart is snares and nets, and whose hands are fetters. He who pleases God escapes her, but the sinner is taken by her."*: It is the Preacher's own finding, after *"I turned my heart to know and to search out"* (7:25), *"which my soul has sought repeatedly"* (7:28).; The figure is a hunter's: snares and nets for a heart, fetters for hands.; A heart can be a trap set for another person's desire. Escape is tied to "he who pleases God", not to strength of will.
  - applies to 1 occurrence(s): Ecc 7:25 (know)
- **Observation 18137** (prior-capture, tag statement, status draft): Knowing in heart and soul (Jos 23:14–15). *"you know in your hearts and souls, all of you, that not one word has failed of all the good things that the Lord your God promised"*. Then: *"just as all the good things … have been fulfilled for you, so the Lord will bring upon you all the evil things"*.: The knowledge comes from experience, held in heart and soul.; Joshua turns it into a warning: the same faithfulness holds for the threats.
  - applies to 1 occurrence(s): Jos 23:14 (know)
- **Observation 18138** (prior-capture, tag statement, status draft): The heart that grows hot, and then speaks (Psa 39:1–3).: *"I said, 'I will guard my ways, that I may not sin with my tongue …' I was mute and silent; I held my peace to no avail, and my distress grew worse. My heart became hot within me. As I mused, the fire burned; then I spoke with my tongue"*.; What he speaks is a prayer: *"O Lord, make me know my end"* (39:4).; The sequence is the verses' own: silence held, distress growing, the heart hot, musing as the fire, and then speech. The heat does not come out in sin, which was his fear. It comes out to God.
  - applies to 1 occurrence(s): Psa 39:4 (know)
- **Observation 18146** (prior-capture, tag statement, status draft): Warmth from a fire that also made a god (Isa 44:15–20). *"He takes a part of it and warms himself … Also he makes a god and worships it … Also he warms himself and says, 'Aha, I am warm, I have seen the fire!'"* (44:15–16). Then: *"they know not, nor do they discern, for he has shut their eyes … and their hearts, so that they cannot understand"* (44:18). Explore the figure: the same log gives comfort and a god. I read a satisfied body and a closed heart in one man, side by side. He is pleased with the warmth and does not see what he has done with the rest. 10.7 already cites Isa 44.
  - applies to 1 occurrence(s): Isa 44:18 (know)
- **Observation 18175** (prior-capture, tag statement, status draft): The ear woken each morning (Isa 50:4–5): *"The Lord God has given me the tongue of those who are taught, that I may know how to sustain with a word him who is weary. Morning by morning he awakens; he awakens my ear to hear as those who are taught. The Lord God has opened my ear, and I was not rebellious"*.; The sequence is the verses': the ear woken, then the tongue that sustains. Hearing comes before speaking, and it is daily.; *"I was not rebellious"* comes before *"I gave my back to those who strike"* (50:6).; Where: 10.2 (hearing), and 10.5 (*Speech is heard*).
  - applies to 1 occurrence(s): Isa 50:4 (know)
- **Observation 18218** (prior-capture, tag statement, status draft): 1Ki 2:18, with 2:13–25 | Bathsheba meets Adonijah with "Do you come peacefully?" (2:13). He says, "You know that the kingdom was mine … However, the kingdom has turned about and become my brother's, for it was his from the Lord" (2:15). Then: "one request … do not refuse me" (2:16), Abishag. Solomon honours his mother ("rose to meet her and bowed down to her", 2:19) and promises, "I will not refuse you" (2:20). Then he reads the request as the claim: "Ask for him the kingdom also" (2:22). He swears, and Adonijah dies (2:23–25). I read that the verses give Solomon's reading of the request, not Adonijah's own heart | 10.10 *Fear that arrives with a person* ("Do you come peacefully?", beside 1S ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Ki 2:15 (know)
- **Observation 18225** (prior-capture, tag statement, status draft): 1Ki 2:42 | Shimei's oath. 2:43 is told in 10.5. Then: "You know in your own heart all the harm that you did to David my father" (2:44, uncited) | Ch 4 (the heart knows its own harm); 10.5
  - applies to 1 occurrence(s): 1Ki 2:42 (know)
- **Observation 18226** (prior-capture, tag statement, status draft): 2Ch 32:11 | "Is not Hezekiah misleading you …?" with "On what are you trusting?" (32:10) and "Do you not know what I and my fathers have done?" (32:13). Trust is attacked through doubt of the leader and a record of power. The parallels (2Ki 18:20–22; Isa 36:5–7) are uncited | 10.9 (trust attacked); 10.5 (words that undermine)
  - applies to 1 occurrence(s): 2Ch 32:13 (know)
- **Observation 18272** (prior-capture, tag statement, status draft): Q1 What is death? (OT-02, main source.) The verses give: the common lot: "We must all die; we are like water spilled on the ground" (2Sa 14:14); "it is appointed for man to die once, and after that comes judgment" (Heb 9:27); its entry through sin: "death through sin, and so death spread to all men because all sinned" (Rom 5:12); "the wages of sin is death" (Rom 6:23); the warning and its denial: "you shall surely die" (Gen 2:17); "You will not surely die" (Gen 3:4); sleep: "not dead but sleeping" (Mat 9:24); a power that holds and is overthrown: "not possible for him to be held by it" (Act 2:24); "the last enemy to be destroyed is death" (1Cor 15:26); death in the living: "Whoever does not ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Ecc 9:5 (know)
- **Observation 18273** (prior-capture, tag statement, status draft): Q2 Spirit and soul at death (OT-03, touched): "he poured out his soul to death" (Isa 53:12); "My soul is very sorrowful, even to death" (Mat 26:38); "carried by the angels" (Luk 16:22), with no inner word named; "to die is gain" (Phili 1:21); against these, "the dead know nothing" (Ecc 9:5) and "the dead do not praise" (Psa 115:17); These name no destination for spirit or soul. The focused pull for Q2 is still needed.
  - applies to 1 occurrence(s): Ecc 9:5 (know)
- **Observation 18314** (prior-capture, tag statement, status draft): Q1 What is death? | It is stated from the life side: "For the living know that they will die" (Ecc 9:5). A person can be called dead while alive: "dead even while she lives" (1Ti 5:6), "alienated from the life of God" (Eph 4:18). | LD-114, LD-128
  - applies to 1 occurrence(s): Ecc 9:5 (know)
- **Observation 18370** (prior-capture, tag statement, status draft): "Not abandoned to Sheol", read of a death. "Therefore my heart is glad, and my whole being rejoices; my flesh also dwells secure. For you will not abandon my soul to Sheol, or let your holy one see corruption. You make known to me the path of life." Peter: David "foresaw and spoke about the resurrection of the Christ, that he was not abandoned to Hades, nor did his flesh see corruption."
  - meaning: Meaning: Peter reads Psa 16:10 of Christ's death and rising, not of a rescue before death. Implies: Psa 16:10 is now in Ch 2's list of a "living person rescued from dying" (in "Delivered from death"). Peter's reading puts it beyond death. It moves (decision 1).
  - applies to 1 occurrence(s): Psa 16:11 (known)
- **Observation 18372** (prior-capture, tag statement, status draft): Q2 (soul and spirit at death). The verses give the soul more than one face at death. It departs (Gen 35:18). It dies (Num 23:10; Eze 18:4). It is poured out to death (Isa 53:12). It goes to the generation of its fathers (Psa 49:19). It is ransomed from Sheol's power, "for he will receive me" (Psa 49:15). It is not abandoned to Sheol, which Peter reads of Christ (Act 2:27, 31). Of the spirit, they say it is committed, taken, or returns to God (Luk 23:46; Psa 104:29; Ecc 12:7); "who knows" where it goes (Ecc 3:21); and the dead "live in the spirit the way God does" (1Pe 4:6). No verse sends the soul one way and the spirit another. These are set side by side, unreconciled.
  - applies to 1 occurrence(s): Ecc 3:21 (knows)
- **Observation 18377** (prior-capture, tag statement, status draft): "We know that while we are at home in the body we are away from the Lord, for we walk by faith, not by sight. Yes, we are of good courage, and we would rather be away from the body and at home with the Lord. So whether we are at home or away, we make it our aim to please him."
  - meaning: Meaning: being away from the body is set beside being at home with the Lord. Implies: a few verses earlier, in the same chapter, Paul says "not that we would be unclothed, but that we would be further clothed" (2Cor 5:4, in Ch 2 "Waited for"). Both are stated. I leave them side by side.
  - applies to 1 occurrence(s): 2Cor 5:6 (know)
- **Observation 18390** (prior-capture, tag statement, status draft): Like his body. "our citizenship is in heaven, and from it we await a Savior … who will transform our lowly body to be like his glorious body, by the power that enables him even to subject all things to himself." "predestined to be conformed to the image of his Son". "what we will be has not yet appeared; but we know that when he appears we shall be like him, because we shall see him as he is."
  - applies to 1 occurrence(s): 1Jo 3:2 (know)
- **Observation 18391** (prior-capture, tag statement, status draft): Already now, in the inner being. "born again to a living hope through the resurrection of Jesus Christ" (1Pe 1:3); "that I may know him and the power of his resurrection" (Php 3:10); the mind "transformed" (Rom 12:2); "being transformed … from one degree of glory to another" (2Cor 3:18).
  - applies to 1 occurrence(s): Phili 3:10 (know)
- **Observation 18518** (prior-capture, tag statement, status draft): C5 | Ready to die for or with another, and readiness that fails. Jonathan: "Here I am; I will die." Peter: "ready to go with you both to prison and to death", answered "you will deny three times that you know me" (22:34). Thomas: "that we may die with him". "Be faithful unto death"; "they loved not their lives even unto death". | 1Sa 14:43; Jos 2:14; Judg 5:18; Luk 22:33–34; Joh 11:16; 1Co 9:15; Phi 2:30; Rev 2:10; 12:11 | Ch 2 *Dying to the Lord* (beside Ruth); 10.10 *Loyalty and honour*
  - applies to 1 occurrence(s): Luk 22:34 (know)
- **Observation 18557** (prior-capture, tag statement, status draft): | not listening: "they perish by the sword and die without knowledge" | Job 36:12
  - applies to 1 occurrence(s): Job 36:12 (knowledge)
- **Observation 18633** (prior-capture, tag statement, status draft): Num 16:30 | alive | … and they go down alive into Sheol, then you shall know that these men have despised the Lord.
  - applies to 1 occurrence(s): Num 16:30 (know)
- **Observation 18653** (prior-capture, tag statement, status draft): c1. The inner acts toward the resurrection: 34 verses (A1). This is the largest group.: *Denied*, and the ground Jesus gives: "the Sadducees say that there is no resurrection, nor angel, nor spirit" (Act 23:8); Jesus' answer: "You are wrong, because you know neither the Scriptures nor the power of God"; (Mat 22:29; Mar 12:24). He grounds it in God's name: "the God of Abraham" (Mar 12:26), "for; all live to him" (Luk 20:38); The section cites only Mat 22:30 and Luk 20:36, on marriage.; *Questioned, and not understood until later:*; "questioning what this rising from the dead might mean" (Mar 9:10); "as yet they did not understand the Scripture, that he must rise from the dead" (Joh 20:9); "Wh ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Joh 11:24 (know)
- **Observation 18877** (prior-capture, tag statement, status draft): Hiding from God: In each scene where a person hides from God, something of God is perceived first: a sound (Genesis 3:10), God naming himself (Exodus 3:6), "the terror of the Lord, and … the splendor of his majesty" (Isaiah 2:10), "the face of him who is seated on the throne, and … the wrath of the Lamb" (Revelation 6:16).; Adam hid because he knew he was naked (Genesis 3:10).; Moses "hid his face, for he was afraid to look at God" (Exodus 3:6), and no wrong is named.; At the end, people call "to the mountains and rocks, 'Fall on us and hide us'", for "who can stand?" (Revelation 6:16–17).; Job names the one condition on which he will not hide: "Only grant me two things, then I will not hide ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Psa 139:14 (knows), Isa 29:15 (knows), Hos 5:3 (know)
- **Observation 18884** (prior-capture, tag statement, status draft): It fails, and fear follows. Moses "struck down the Egyptian and hid him in the sand" (Exodus 2:12). When it came out, "Moses was afraid, and thought, 'Surely the thing is known'" (2:14).
  - applies to 1 occurrence(s): Exo 2:14 (known)
- **Observation 18889** (prior-capture, tag statement, status draft): The hidden trap: In the Psalms a purpose is hidden in order to catch someone. "They hold fast to their evil purpose; they talk of laying snares secretly, thinking, 'Who can see them?'" (Psalm 64:5). The next verse says where the purpose was hidden first: "For the inward mind and heart of a man are deep" (64:6).; The one it is set for prays out of his weakness. "When my spirit faints within me, you know my way! In the path where I walk they have hidden a trap for me" (Psalm 142:3). "No one cares for my soul" (142:4). It is worse when it comes from those he had prayed for: "Yet they have dug a pit for my life. Remember how I stood before you to speak good for them" (Jeremiah 18:20).; And the t ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 142:3 (know)
- **Observation 18904** (prior-capture, tag statement, status draft): What it is. Knowing that cannot close: a mind held open before something it cannot interpret. The bearers are all human: Herod (Mar 6:20; Luk 9:7), the disciples (Joh 13:22), the women at the tomb (Luk 24:4), the Pentecost crowd (Act 2:12), the temple captain and chief priests (Act 5:24), Peter (Act 10:17), Paul (2Cor 4:8; Gal 4:20), Festus (Act 25:20), and Belshazzar's lords (Dan 5:9).
  - applies to 1 occurrence(s): Mar 6:20 (knowing)
- **Observation 18908** (prior-capture, tag statement, status draft): How the sense shifts. In Mar 6:20, Herod "feared John, knowing … greatly perplexed, and yet he heard him gladly". Four inner operations sit on one bearer with no seat word, each named by a word from a different cluster (fear M01, knowing M15, gladness M04). The operations name themselves. In Gal 4:20 the perplexity is love's: it comes straight after "my little children, for whom I am again in the anguish of childbirth" (4:19).
  - applies to 1 occurrence(s): Mar 6:20 (knowing)
- **Observation 18989** (prior-capture, tag statement, status draft): The passage, before: *"Masters, do the same to them, and stop your threatening, knowing that he who is both their Master and yours is in heaven"* (6:9). Then *"be strong in the Lord and in the strength of his might"* (6:10), and *"stand against the schemes of the devil"* (6:11).
  - applies to 1 occurrence(s): Eph 6:9 (knowing)
- **Observation 18991** (prior-capture, tag statement, status draft): Pointer: three verses earlier (6:9), a human master is told to stop threatening, *"knowing"* that he has a Master in heaven. In one passage, a master's rule over others is checked by the Master above him, and the believer stands against authorities above the human ones.
  - applies to 1 occurrence(s): Eph 6:9 (knowing)
- **Observation 19009** (prior-capture, tag statement, status draft): The verses: *"You know that the rulers of the Gentiles lord it over them, and their great ones exercise authority over them. It shall not be so among you"* (Mat 20:25–26).; Luke: *"The kings of the Gentiles exercise lordship over them, and those in authority over them are called benefactors. But not so with you"* (Luk 22:25–26).
  - applies to 1 occurrence(s): Mat 20:25 (know)
- **Observation 19024** (prior-capture, tag statement, status draft): Eph 6:9 (from §2.1, a passage verse with no B word): *"Masters, do the same to them, and stop your threatening, knowing that he who is both their Master and yours is in heaven, and that there is no partiality with him."*: What checks the master is knowing that he has a Master too.
  - applies to 1 occurrence(s): Eph 6:9 (knowing)
- **Observation 19039** (prior-capture, tag statement, status draft): The passage, before: *"To me they cry, 'My God, we — Israel — know you'"* (8:2).
  - applies to 1 occurrence(s): Hos 8:2 (know)
- **Observation 19040** (prior-capture, tag statement, status draft): Reading: The people say they know God (8:2). God says of their princes, "I knew it not".; One sentence puts their kings and their idols side by side. Both are things they made with their own hands.
  - applies to 1 occurrence(s): Hos 8:2 (know)
- **Observation 19060** (prior-capture, tag statement, status draft): The passage. *"by your knowledge this weak person is destroyed, the brother for whom Christ died"* (8:11). *"if food makes my brother stumble, I will never eat meat"* (8:13). The weak conscience is in 8:7 (Ch 8).
  - applies to 1 occurrence(s): 1Cor 8:11 (knowledge)
- **Observation 19076** (prior-capture, tag statement, status draft): The verses: Daniel: *"it is you, O king, who have grown and become strong. Your greatness has grown and reaches to heaven, and your dominion to the ends of the earth"* (4:22).; *"your kingdom shall be confirmed for you from the time that you know that Heaven rules"* (4:26).; Daniel's counsel: *"break off your sins by practicing righteousness, and your iniquities by showing mercy to the oppressed"* (4:27).; Twelve months later: *"Is not this great Babylon, which I have built by my mighty power as a royal residence and for the glory of my majesty?"* (4:30).; *"While the words were still in the king's mouth, there fell a voice from heaven"* (4:31).; Before giving the interpretation, Daniel *"wa ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Dan 4:26 (know)
- **Observation 19093** (prior-capture, tag statement, status draft): His rule is to be known: *"that they may know that God rules over Jacob"* (Psa 59:13; OT-16).
  - applies to 1 occurrence(s): Psa 59:13 (know)
- **Observation 19096** (prior-capture, tag statement, status draft): The Father's own authority, and a human limit with it: *"It is not for you to know times or seasons that the Father has fixed by his own authority"* (Act 1:7).
  - applies to 1 occurrence(s): Act 1:7 (know)
- **Observation 19122** (prior-capture, tag statement, status draft): Hos 8:4. *"They made kings, but not through me. They set up princes, but I knew it not. With their silver and gold they made idols for their own destruction."*
  - applies to 1 occurrence(s): Hos 8:4 (knew)
- **Observation 19125** (prior-capture, tag statement, status draft): Dan 5:16–17. The king: *"you shall be clothed with purple … and shall be the third ruler in the kingdom."* Daniel: *"Let your gifts be for yourself, and give your rewards to another. Nevertheless, I will read the writing to the king and make known to him the interpretation."*
  - applies to 2 occurrence(s): Dan 5:16 (make known), Dan 5:17 (make known)
- **Observation 19139** (prior-capture, tag statement, status draft): Judg 15:11. *"Do you not know that the Philistines are rulers over us? What then is this that you have done to us?"*
  - applies to 1 occurrence(s): Judg 15:11 (know)
- **Observation 19164** (prior-capture, tag statement, status draft): Ezra 7:10, a heart set. "Ezra had set his heart to study the Law of the Lord, and to do it and to; teach." The setting of the heart is an act of direction. It is verse-stated, and named in three; steps: study, do, teach. The verse opens with "For", straight after the good hand (7:9). I read the; "For" as giving the hand a reason in Ezra's heart; the text does not spell that out further.
  - applies to 1 occurrence(s): Ezr 7:10 (study)
- **Observation 19166** (prior-capture, tag statement, status draft): 10.7 *Choosing and setting direction*: Ezra 7:10, setting the heart to study, do and teach. It is; a clear verse for the heart's direction, and it is not in the book. Rehoboam, who "did not set his; heart to seek the Lord" (2 Chronicles 12:14), is in 10.13 and 10.14, and is its opposite.
  - applies to 1 occurrence(s): Ezr 7:10 (study)
- **Observation 19175** (prior-capture, tag statement, status draft): Ezr 7:9 | none (ruling) | Ezra 7:10, a heart set to study, do and teach; Ezra 7:28, courage taken because God's hand is on him | 10.7; 10.12 or 10.9; 13.1 *His favor*
  - applies to 1 occurrence(s): Ezr 7:10 (study)
- **Observation 19189** (prior-capture, tag statement, status draft): Where it comes from. In every case a perception of God comes first: "I heard the sound of you in the garden" (Gen 3:10); God names himself: "I am the God of your father" (Exo 3:6); "the terror of the Lord, and … the splendor of his majesty" (Isa 2:10); "the face of him who is seated on the throne, and … the wrath of the Lamb" (Rev 6:16); Inside the person, what meets that perception differs: Adam: knowledge of exposure. "The eyes of both were opened, and they knew that they were naked" (Gen 3:7), and so "I was afraid, because I was naked" (3:10).; Moses: "he was afraid to look at God" (Exo 3:6), with no transgression stated.; The kings, the great, "slave and free": "who can stand?" (Rev 6:17 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Gen 3:7 (knew)
- **Observation 19219** (prior-capture, tag statement, status draft): What it does. The same fact works in opposite directions, depending on who is seen: Comfort for the sufferer: "all my longing is before you; my sighing is not hidden from you" (Psa 38:9), between "the tumult of my heart" (38:8) and "My heart throbs" (38:10); Confession for the penitent: "you know my folly; the wrongs I have done are not hidden from you" (Psa 69:5); Wonder at being known before birth: "My frame was not hidden from you, when I was being made in secret" (Psa 139:15); Judgement for the evildoer: "They are not hidden from me, nor is their iniquity concealed" (Jer 16:17); "Israel is not hidden from me; for now, O Ephraim, you have played the whore" (Hos 5:3); "There is no gloom or ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 69:5 (know)
- **Observation 19220** (prior-capture, tag statement, status draft): Where it comes from: the attempt to hide. "Ah, you who hide deep from the Lord your counsel … and who say, 'Who sees us? Who knows us?'" (Isa 29:15). The next verse names what that attempt does: "You turn things upside down! Shall the potter be regarded as the clay …?" (29:16). Hiding from God inverts creature and creator.
  - applies to 1 occurrence(s): Isa 29:15 (knows)
- **Observation 19222** (prior-capture, tag statement, status draft): Seat.; In the verse: 2Sa 18:13 "if I had dealt treacherously against his life". *Nephesh* here is Absalom's life, the other party's, in its life sense. It is the life that would have been taken, not an inner faculty. New in v3: the inner movement of the verse (restraint by knowing one will be seen) belongs to the soldier, and it has no seat word. This verse was not read in the M47 batches.; In the passage, the bearer's own (genuine): Psa 38:9 stands between "the tumult of my heart" (38:8) and "My heart throbs; my strength fails me" (38:10). The sighing that is not hidden from God is a heart's sighing. Exposure here is received as comfort, because what is seen is the heart's pain.; In the pas ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 139:14 (knows)
- **Observation 19223** (prior-capture, tag statement, status draft): In the next verse, the offender's (genuine) — new in v3: Hos 5:3 ("Israel is not hidden from me") → 5:4 "Their deeds do not permit them to return to their God. For the spirit of whoredom is within them, and they know not the Lord". *Ruach* here is an inner disposition, "within them", and it passes the check. The two knowings do not match: God knows Ephraim completely (5:3), and Ephraim does not know God (5:4). The spirit within is what blocks the return. This is the judgement side of the same fact that is praise in Psa 139:14–15.
  - applies to 3 occurrence(s): Psa 139:14 (knows), Hos 5:3 (know), Hos 5:4 (know)
- **Observation 19224** (prior-capture, tag statement, status draft): (a) Concealing one's own wrong. Each case has its own sequence: Achan: "when I saw … then I coveted them and took them. And see, they are hidden in the earth inside my tent" (Jos 7:21); Joshua: "tell me now what you have done; do not hide it from me" (7:19); Achan: "Truly I have sinned" (7:20); "behold, it was hidden in his tent" (7:22); Seeing, coveting, taking, hiding, being demanded to disclose, confessing, being found.; Moses: "He looked this way and that, and seeing no one, he struck down the Egyptian and hid him in the sand" (Exo 2:12). When the deed surfaces: "Moses was afraid, and thought, 'Surely the thing is known'" (2:14). Concealment fails, and fear follows.; The hidden adultery: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Exo 2:14 (known)
- **Observation 19228** (prior-capture, tag statement, status draft): (e) Hiding a treasure.; "treasure hidden in a field, which a man found and covered up. Then in his joy he goes and sells all that he has" (Mat 13:44). Concealment serves joy and resolve.; Against it, the servant's burial of the talent (Mat 25:18). He explains: "I knew you to be a hard man … so I was afraid, and I went and hid your talent" (25:24–25). A perception of the master produces fear, and fear produces burial. The master names it "wicked and slothful" (25:26).
  - applies to 2 occurrence(s): Mat 25:24 (knew), Mat 25:26 (knew)
- **Observation 19232** (prior-capture, tag statement, status draft): What it does.; Luk 9:45: "they did not understand this saying, and it was concealed from them, so that they might not perceive it. And they were afraid to ask him". The next verse: "An argument arose among them as to which of them was the greatest" (9:46). Blocked perception is followed by fear of asking, and then by rivalry.; "This saying was hidden from them, and they did not grasp what was said" (Luk 18:34).; "Would that you, even you, had known on this day the things that make for peace! But now they are hidden from your eyes" (Luk 19:42): the not-knowing has become a judgement.
  - applies to 1 occurrence(s): Luk 19:42 (known)
- **Observation 19239** (prior-capture, tag statement, status draft): How it co-exists.; Herod: "Herod feared John, knowing that he was a righteous and holy man … When he heard him, he was greatly perplexed, and yet he heard him gladly" (Mar 6:20). Fear, knowledge, perplexity and gladness are all present in one man towards one prophet, and the perplexity keeps him listening.; Amazement: "all were amazed and perplexed" (Act 2:12).; The body of another man: Belshazzar's "color changed … his limbs gave way, and his knees knocked together" (Dan 5:6) while his lords were perplexed (5:9).; Anguish of love: "I am perplexed about you" (Gal 4:20), after "my little children, for whom I am again in the anguish of childbirth" (4:19).; A limit held: "perplexed, but not dri ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Mar 6:20 (knowing)
- **Observation 19246** (prior-capture, tag statement, status draft): (a) Anxiety over provision (Mat 6:25, 27, 28, 31, 34; Luk 12:22, 25, 26, 29).; Where from: "what you will eat or what you will drink … what you will put on" (Mat 6:25).; What it does: nothing. "which of you by being anxious can add a single hour to his span of life?" (6:27 = Luk 12:25). It multiplies itself forward: "tomorrow will be anxious for itself" (6:34). It suspends the person: *meteōrizō*, "be held in suspense" (Luk 12:29).; What it co-exists with: "little faith" (Luk 12:28), and the Gentiles' seeking (Mat 6:32).; What displaces it: looking at birds and lilies (6:26, 28); knowing "your heavenly Father knows that you need them" (6:32); "seek first the kingdom" (6:33).; The seat is sta ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Mat 6:32 (knows)
- **Observation 19251** (prior-capture, tag statement, status draft): (f) Anxiety handed over or answered.; "do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God" (Phili 4:6) → "the peace of God … will guard your hearts and your minds" (4:7); "casting all your anxieties on him, because he cares for you" (1Pe 5:7); "When the cares of my heart are many, your consolations cheer my soul" (Psa 94:19); "Anxiety in a man's heart weighs him down, but a good word makes him glad" (Pro 12:25); "Search me, O God, and know my heart! Try me and know my thoughts [*sar'appim*, anxious thoughts]" (Psa 139:23); The movement: anxiety is given to another, or answered by a word, and becomes peace or ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 139:23 (know)
- **Observation 19255** (prior-capture, tag statement, status draft): Seat. Anxiety holds the most in-verse seats of any M20 phenomenon (8 of 30). The seat word plays three different roles, and v3 separates them.; The seat as where the anxiety sits (bearer's own, genuine): Pro 12:25 "Anxiety in a man's heart weighs him down" (strand f). Batch A v3 §6 ("Anxiety in the heart").; Luk 21:34 "lest your hearts be weighed down with … cares of this life" (strand e). Batch A v3 §6.; Psa 139:23 "know my heart! … know my thoughts [anxious thoughts]" (strand f). Batch A v3 §6 ("God searching the anxious heart").; The seat as where the answer lands (bearer's own, genuine): Psa 94:19 "your consolations cheer my soul" (strand f). Batch A v3 §6 notes that "heart" in this vers ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 139:23 (know)
- **Observation 19272** (prior-capture, tag statement, status draft): What it does to the one it is set for. "When my spirit faints within me, you know my way! In the path where I walk they have hidden a trap for me" (Psa 142:3). The next verse: "no one cares for my soul" (142:4). The trap is aimed at "my life" (35:7).
  - applies to 1 occurrence(s): Psa 142:3 (know)
- **Observation 19296** (prior-capture, tag statement, status draft): Psa 31:4–7: taken out of the hidden net → spirit committed into God's hand → the soul's distress known (v3)
  - applies to 1 occurrence(s): Psa 31:7 (known)
- **Observation 19302** (prior-capture, tag statement, status draft): Dan 5:9–12: lords perplexed → the queen names Daniel → an excellent spirit … to interpret (v3)
  - applies to 1 occurrence(s): Dan 5:12 (interpret)
- **Observation 19350** (prior-capture, tag statement, status draft): Psa 139:15 (EX) | Psa 139:14 "my soul knows it very well" | bearer's own · genuine | §6 Seat
  - applies to 1 occurrence(s): Psa 139:14 (knows)
- **Observation 19404** (prior-capture, tag statement, status draft): Joshua 24:15 — "choose this day whom you will serve": Joshua does not take the spoken choice to be the whole of it.; The passage records how long the choice held: *"Israel served the Lord all the days of Joshua, and all the days of the elders who outlived Joshua and had known all the work that the Lord did for Israel"* (v31). The verse ties those years to the elders who *had known the work*. I read this as saying that the choice held as long as there were people who remembered what it had been made from. The verse states the timing; it does not state the cause.
  - applies to 1 occurrence(s): Jos 24:31 (known)
- **Observation 19415** (prior-capture, tag statement, status draft): 1.6 Plans for welfare, and thought for the one in need: *"For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope"* (Jer 29:11).; The verse looks ahead to *"When seventy years are completed"* (29:10).; It is followed by *"You will seek me and find me, when you seek me with all your heart"* (29:13).; *"As for me, I am poor and needy, but the Lord takes thought for me"* (Psa 40:17).; *"But God will not take away life, and he devises means so that the banished one will not remain an outcast"* (2Sa 14:14). The wise woman says it against the fact that *"We must all die"*.
  - applies to 1 occurrence(s): Jer 29:11 (know)
- **Observation 19418** (prior-capture, tag statement, status draft): 1.9 The Spirit intercedes according to the will of God, and the purpose is turned toward those who love him: *"Likewise the Spirit helps us in our weakness. For we do not know what to pray for as we ought, but the Spirit himself intercedes for us with groanings too deep for words. And he who searches hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God"* (Rom 8:26–27).; The Spirit's praying is matched to God's will, and the one who searches hearts knows the Spirit's mind.; The meaning of "mind" (G5427) is left as Paul gives it: OT-94, which comes back with M63.; The next verse goes straight on: *"And we know that for those who ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Rom 8:26 (know), Rom 8:27 (knows), Rom 8:28 (know)
- **Observation 19421** (prior-capture, tag statement, status draft): Weakness in prayer: *"we do not know what to pray for as we ought"* (Rom 8:26), the weakness the Spirit helps.
  - applies to 1 occurrence(s): Rom 8:26 (know)
- **Observation 19471** (prior-capture, tag statement, status draft): Ground: why or how the choice is made (12): Knowing: Isa 7:15–16: *"when he knows how to refuse the evil and choose the good"*; Act 15:22, 25: *"it seemed good to us … to choose men"* (G1380); Liking or preference: Deu 23:16: *"wherever it suits him"* (H2896A); 2Sa 19:38: *"whatever seems good to you"* (H2896A); Jos 24:15: *"if it is evil in your eyes to serve the Lord, choose this day"*; Pleasure: Act 6:5, *"what they said pleased the whole gathering, and they chose Stephen"*; Fear: Psa 25:12, *"the man who fears the Lord … the way that he should choose"*; Not listening: Isa 65:12, *"when I spoke, you did not listen … and chose what I did not delight in"*; Iniquity: Job 15:5, *"your iniquit ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (knows)
- **Observation 19472** (prior-capture, tag statement, status draft): Paired: named alongside the choosing as a parallel act (10): Refuse: Isa 7:15, Isa 7:16; Reject: Job 34:33; Know: Job 34:4 (*"Let us choose what is right; let us know among ourselves what is good"*), Job 34:33; Envy: Pro 3:31 (*"Do not envy … and do not choose"*); Desire: Isa 1:29 (*"the oaks that you desired … the gardens that you have chosen"*); The soul's delight: Isa 66:3 (*"These have chosen their own ways, and their soul delights in their abominations"*); Hold fast: Isa 56:4 (*"who choose the things that please me and hold fast my covenant"*); Take care: Job 36:21
  - applies to 2 occurrence(s): Job 34:4 (know), Job 34:33 (know)
- **Observation 19473** (prior-capture, tag statement, status draft): Object: the inner thing that is itself chosen (4): Faithfulness: Psa 119:30, *"I have chosen the way of faithfulness"*; Knowledge: Pro 8:10; Wisdom and understanding: Pro 16:16
  - applies to 1 occurrence(s): Pro 8:10 (knowledge)
- **Observation 19478** (prior-capture, tag statement, status draft): None: in the same verse, but not bound to the choosing (4): Judg 20:34; Isa 7:16, *"dread"*; 2Jo 1, love and know
  - applies to 1 occurrence(s): 2Jo 1 (know)
- **Observation 19479** (prior-capture, tag statement, status draft): Ground (19): Love: Deu 4:37, Deu 10:15; Psa 47:4, Psa 78:68; Col 3:12, 1Th 1:4, 2Th 2:13 (*"beloved"*); *"Set his love / heart"* (H2836A): Deu 7:7, Deu 10:15; Desire: Psa 132:13, *"he has desired it for his dwelling place"*; Took pleasure: 1Ch 28:4; Compassion: Isa 14:1; Faithful: Isa 49:7; Soul well pleased: Mat 12:18; Knows the hearts: Act 1:24; Purpose: Rom 9:11; Grace: Rom 11:5; Jesus' knowing: Joh 13:18, *"I know whom I have chosen"*
  - applies to 1 occurrence(s): Joh 13:18 (know)
- **Observation 19484** (prior-capture, tag statement, status draft): H3045 *yādaʿ* "know" (M15) has six faces: the ground of choosing: Isa 7:15–16; paired with choosing: Job 34; the purpose of being chosen: Isa 43:10; a response: 1Sa 20:30; a contrast: Isa 45:4; God making himself known, an operation: Num 16:5, Eze 20:5
  - applies to 1 occurrence(s): Eze 20:5 (known)
- **Observation 19491** (prior-capture, tag statement, status draft): When God chooses, the choosing comes first. The inner life of the chosen is its purpose.: *"my servant whom I have chosen, that you may know and believe me and understand that I am he"* (Isa 43:10). The people chosen as witnesses are described in the same passage as *"blind, yet have eyes … deaf, yet have ears"* (43:8).; *"he chose us in him before the foundation of the world, that we should be holy and blameless before him"* (Eph 1:4).; *"has not God chosen those who are poor in the world to be rich in faith"* (Jam 2:5).; *"God chose you as the firstfruits to be saved, through sanctification by the Spirit and belief in the truth"* (2Th 2:13). The verse names God's choosing and the person's ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 43:10 (know)
- **Observation 19492** (prior-capture, tag statement, status draft): When people choose, the order is the other way. The twelve set the terms: *"pick out from among you seven men of good repute, full of the Spirit and of wisdom"* (Act 6:3). The gathering chooses Stephen, *"a man full of faith and of the Holy Spirit"* (6:5), by what is already seen in him and said of him. What was seen in him then is seen in him to his death: *"full of grace and power"* (6:8), *"full of the Holy Spirit"* (7:55).: This is the reverse of the chooser's own order in §2a, where a person chooses *"when he knows how"* (Isa 7:15).
  - applies to 1 occurrence(s): Isa 7:15 (knows)
- **Observation 19501** (prior-capture, tag statement, status draft): Know and serve with the whole inner being. *"know the God of your father and serve him with a whole heart and with a willing mind, for the Lord searches all hearts and understands every plan and thought"* (1Ch 28:9).
  - applies to 1 occurrence(s): 1Ch 28:9 (know)
- **Observation 19504** (prior-capture, tag statement, status draft): Confirm it. *"be all the more diligent to confirm your calling and election, for if you practice these qualities you will never fall"* (2Pe 1:10). The qualities are added one to another: *"supplement your faith with virtue, and virtue with knowledge, and knowledge with self-control, and self-control with steadfastness, and steadfastness with godliness, and godliness with brotherly affection, and brotherly affection with love"* (1:5–7). The effort follows what was given first: *"His divine power has granted to us all things that pertain to life and godliness"* (1:3).
  - applies to 3 occurrence(s): 2Pe 1:3 (knowledge), 2Pe 1:5 (knowledge), 2Pe 1:6 (knowledge)
- **Observation 19506** (prior-capture, tag statement, status draft): Faith, knowing and the truth: Faith, and knowing the truth, are named for the chosen in five of these verses: *"for the sake of the faith of God's elect and their knowledge of the truth, which accords with godliness, in hope of eternal life"* (Tit 1:1–2); *"rich in faith and heirs of the kingdom, which he has promised to those who love him"* (Jam 2:5); *"that you may know and believe me and understand that I am he"* (Isa 43:10); *"belief in the truth"* (2Th 2:13); *"having the eyes of your hearts enlightened, that you may know what is the hope to which he has called you"* (Eph 1:18), a prayer for people already chosen; Faith is shown in what it does: *"So also faith by itself, if it does not ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Isa 43:10 (know), Eph 1:18 (know), Tit 1:1 (knowledge), Tit 1:16 (know)
- **Observation 19514** (prior-capture, tag statement, status draft): Those who cannot know. The idol-maker: *"They know not, nor do they discern … their hearts, so that they cannot understand"* (Isa 44:18). "Know" and "discern" are the same words as "know" and "understand" in 43:10.
  - applies to 1 occurrence(s): Isa 44:18 (know)
- **Observation 19533** (prior-capture, tag statement, status draft): Isa 43:10 | order (chosen to know; blind and deaf); faith and knowing; not a guarantee (not calling, weary); the way back; set against (idol-maker) | batch 1
  - applies to 1 occurrence(s): Isa 43:10 (know)
- **Observation 19539** (prior-capture, tag statement, status draft): Tit 1:1 | faith and knowing (knowledge that accords with godliness); set against (profess and deny; minds defiled) | batch 2
  - applies to 1 occurrence(s): Tit 1:1 (knowledge)
- **Observation 19585** (prior-capture, tag statement, status draft): Choice: Urged, together: *"Let us choose what is right; let us know among ourselves what is good"* (v4).
  - applies to 1 occurrence(s): Job 34:4 (know)
- **Observation 19588** (prior-capture, tag statement, status draft): Choice: Laid on Job: *"For you must choose, and not I; therefore declare what you know"* (v33).
  - applies to 1 occurrence(s): Job 34:33 (know)
- **Observation 19589** (prior-capture, tag statement, status draft): Outcome: Job's choice is not stated. Elihu's verdict follows: *"Job speaks without knowledge; his words are without insight"* (v35).
  - applies to 1 occurrence(s): Job 34:35 (knowledge)
- **Observation 19592** (prior-capture, tag statement, status draft): Led to: Wisdom's call to *"simple ones"* and *"fools"* (v5), and her words: *"all straight to him who understands, and right to those who find knowledge"* (v9).
  - applies to 1 occurrence(s): Pro 8:9 (knowledge)
- **Observation 19593** (prior-capture, tag statement, status draft): Choice: Urged: *"Take my instruction instead of silver, and knowledge rather than choice gold"* (v10). Knowledge is set above the gold that is itself called "choice".
  - applies to 1 occurrence(s): Pro 8:10 (knowledge)
- **Observation 19599** (prior-capture, tag statement, status draft): F2. Pro 8:10 (entry 18). The choosing word describes the gold (*"choice gold"*), not the person's choosing. Knowledge is preferred over it. It sits in §2a as the "object" of choice. Should it stay there, or move with the "Choice: the best" group?
  - applies to 1 occurrence(s): Pro 8:10 (knowledge)
- **Observation 19603** (prior-capture, tag statement, status draft): 1 Chronicles 28:10: "the Lord has chosen you … be strong and do it": David speaks to the whole assembly, then to Solomon. He begins with his own heart and its refusal: *"I had it in my heart to build a house of rest for the ark"* (v2), *"But God said to me, 'You may not build a house for my name'"* (v3). The man who says *"the Lord God of Israel chose me"* (v4) was refused what was in his heart. Being chosen did not give David everything he intended.; He speaks of his own choosing in inner terms: *"among my father's sons he took pleasure in me to make me king"* (v4, H7521). Then Solomon: *"I have chosen him to be my son, and I will be his father"* (v6).; The promise to Solomon is conditional ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 44:9 (know)
- **Observation 19608** (prior-capture, tag statement, status draft): Isaiah 43:10: "my servant whom I have chosen, that you may know and believe me and understand": The setting is a court. The nations are summoned: *"All the nations gather together … Let them bring their witnesses to prove them right"* (v9). Israel is brought out as the Lord's witness, and described as unfit for it: *"Bring out the people who are blind, yet have eyes, who are deaf, yet have ears!"* (v8).; Then: *"You are my witnesses," declares the Lord, "and my servant whom I have chosen, that you may know and believe me and understand that I am he"* (v10). The knowing, believing and understanding are the purpose of the choosing. They are not its ground. The chosen were blind and deaf when c ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Isa 7:15 (knows), Isa 44:9 (know), Isa 44:18 (know)
- **Observation 19642** (prior-capture, tag statement, status draft): What others do around a choice, in these verses: grumble against the chosen man, and God counts it as against himself (Num 16:11; 17:5, 10); seek more than they were given, and are jealous (Num 16:10; Psa 106:16); name a choice as shame, and are angry at what it costs them (1Sa 20:30–31); despise the chosen in the heart, by the eyes of people (2Sa 6:16, 20); despise and abhor the chosen servant (Isa 49:7); conclude from the chosen people's ruin that God rejected them, and despise them in their own sight (Jer 33:24); ask to share the joy of the chosen (Psa 106:5); not know God, and still be called and equipped for the sake of the chosen (Isa 45:4–5); offer an inner act, the humbling of the so ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Isa 45:4 (know), Isa 45:5 (know)
- **Observation 19651** (prior-capture, tag statement, status draft): Isaiah 7:15–16 — "when he knows how to refuse the evil and choose the good": The setting is a king’s heart in fear. Syria and Ephraim are marching on Jerusalem, and *"the heart of Ahaz and the heart of his people shook as the trees of the forest shake before the wind"* (v2). The Lord sends Isaiah with a word for that heart: *"Be careful, be quiet, do not fear, and do not let your heart be faint"* (v4); the threat *"shall not stand"* (v7); then the condition: *"If you are not firm in faith, you will not be firm at all"* (v9). Both "firm" words are the one verb (H0539), so standing firm and being kept firm are the same word.; Then the Lord makes Ahaz an offer: *"Ask a sign of the Lord your God ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (knows)
- **Observation 19653** (prior-capture, tag statement, status draft): Isaiah 1:29 — "the oaks that you desired … the gardens that you have chosen": The oracle opens as a lawsuit: *"Hear, O heavens, and give ear, O earth"* (v2). The charge goes to the inner being: *"Children have I reared and brought up, but they have rebelled against me"* (v2); *"The ox knows its owner … but Israel does not know, my people do not understand"* (v3); *"The whole head is sick, and the whole heart faint"* (v5); Their worship goes on, and the Lord refuses it: *"I do not delight in the blood of bulls"* (v11); *"your appointed feasts my soul hates"* (v14); *"even though you make many prayers, I will not listen"* (v15).; Then the choice is laid before them, in the same two-sided shape ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Isa 1:3 (knows), Isa 1:3 (know)
- **Observation 19658** (prior-capture, tag statement, status draft): Choosing rests on knowing how (Isa 7:15). It is a knowing *how* to tell evil from good and turn. In Isa 1 the oracle opens with its absence: *"Israel does not know, my people do not understand"* (1:3).
  - applies to 1 occurrence(s): Isa 1:3 (know)
- **Observation 19664** (prior-capture, tag statement, status draft): Psalm 25:12 — "Him will he instruct in the way that he should choose": The psalm is a prayer from someone in trouble. It begins *"To you, O Lord, I lift up my soul"*; *"O my God, in you I trust; let me not be put to shame"* (v1–2). It ends with that same person *"lonely and afflicted"*. Among the trouble: *"The troubles of my heart are enlarged"* (v17); *"how many are my foes, and with what violent hatred they hate me"* (v19); *"guard my soul … Let me not be put to shame"* (v20); Running through the whole psalm is the person's own guilt: *"Remember not the sins of my youth or my transgressions"* (v7); *"pardon my guilt, for it is great"* (v11); *"forgive all my sins"* (v18); The person who a ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 25:4 (know)
- **Observation 19679** (prior-capture, tag statement, status draft): 2 Samuel 19:38 — "whatever seems good to you, and all that you desire of me": Barzillai had fed David in his flight. He came with others bringing *"honey and curds and sheep and cheese from the herd, for David and the people with him to eat"*, saying *"The people are hungry and weary and thirsty in the wilderness"* (17:27, 29). When David returns, the king offers him a place at court: *"Come over with me, and I will provide for you with me in Jerusalem"* (19:33).; Barzillai declines, and his reason is about his own inner capacity: *"I am this day eighty years old. Can I discern what is pleasant and what is not? Can your servant taste what he eats or what he drinks? Can I still listen to the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (knows)
- **Observation 19683** (prior-capture, tag statement, status draft): Acts 15:22, 25 — "it seemed good … having come to one accord, to choose men": The choosing ends a dispute that went to the heart of the faith. Some taught *"Unless you are circumcised according to the custom of Moses, you cannot be saved"* (v1), and there was *"no small dissension and debate"* (v2).; At the council the first word about choosing is God's. Peter says *"Brothers, you know that in the early days God made a choice among you, that by my mouth the Gentiles should hear the word of the gospel and believe"* (v7). It is the same verb as the church's later choosing (G1586). He goes on: *"God, who knows the heart, bore witness to them, by giving them the Holy Spirit … having cleansed the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Act 15:7 (know)
- **Observation 19708** (prior-capture, tag statement, status draft): Purpose: "my servant whom I have chosen, that you may know and believe me and understand that I am he" (Isa 43:10); Cyrus is called "For the sake of my servant Jacob, and Israel my chosen … though you do not know me" (Isa 45:4).
  - applies to 2 occurrence(s): Isa 43:10 (know), Isa 45:4 (know)
- **Observation 19718** (prior-capture, tag statement, status draft): Others work for the elect: "Therefore I endure everything for the sake of the elect, that they also may obtain the salvation" (2Ti 2:10); "for the sake of the faith of God's elect and their knowledge of the truth" (Tit 1:1)
  - applies to 1 occurrence(s): Tit 1:1 (knowledge)
- **Observation 19732** (prior-capture, tag statement, status draft): Chosen, and still one betrays: "Did I not choose you, the twelve? And yet one of you is a devil" (Joh 6:70); "I know whom I have chosen. But the Scripture will be fulfilled, 'He who ate my bread has lifted his heel against me'" (Joh 13:18)
  - applies to 1 occurrence(s): Joh 13:18 (know)
- **Observation 19739** (prior-capture, tag statement, status draft): Choosing needs knowing and instruction: "when he knows how to refuse the evil and choose the good" (Isa 7:15, 7:16); "Who is the man who fears the Lord? Him will he instruct in the way that he should choose" (Psa 25:12); It can be done together: "Let us choose what is right; let us know among ourselves what is good" (Job 34:4).
  - applies to 2 occurrence(s): Job 34:4 (know), Isa 7:15 (knows)
- **Observation 19740** (prior-capture, tag statement, status draft): Choosing against: "they hated knowledge and did not choose the fear of the Lord" (Pro 1:29); "Do not envy a man of violence and do not choose any of his ways" (Pro 3:31); "your iniquity teaches your mouth, and you choose the tongue of the crafty" (Job 15:5); "do not turn to iniquity, for this you have chosen rather than affliction" (Job 36:21); "These have chosen their own ways, and their soul delights in their abominations" (Isa 66:3); "when I called, you did not answer … and chose what I did not delight in" (Isa 65:12); Gods: "When new gods were chosen, then war was in the gates" (Judg 5:8); "Go and cry out to the gods whom you have chosen; let them save you" (Judg 10:14); The idol and its ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 1:29 (knowledge)
- **Observation 19742** (prior-capture, tag statement, status draft): 3.9 Choosing a king or a side (4): "your king, whom you have chosen for yourselves, but the Lord will not answer you in that day" (1Sa 8:18); "behold the king whom you have chosen, for whom you have asked; behold, the Lord has set a king over you" (1Sa 12:13). Both the people's choosing and the Lord's setting are stated.; Loyalty: "whom the Lord and this people and all the men of Israel have chosen, his I will be, and with him I will remain" (2Sa 16:18).; Choosing a friend draws anger: "Saul's anger was kindled against Jonathan … do I not know that you have chosen the son of Jesse to your own shame" (1Sa 20:30). This is an OT-62 verse (anger face 3O).
  - applies to 1 occurrence(s): 1Sa 20:30 (know)
- **Observation 19788** (prior-capture, tag face, status draft): Face: Choosing that needs knowing; Who: person; Circumstance in the verses: "knows how to refuse the evil and choose the good"; "him will he instruct in the way"; Verses: Isa 7:15, Psa 25:12
  - applies to 1 occurrence(s): Isa 7:15 (knows)
- **Observation 19839** (prior-capture, tag statement, status draft): Choosing has two sides: Refusing is itself choosing. The child *"knows how to refuse the evil and choose the good"* (Isa 7:15). The oracle around that verse shows refusing going both ways. Ahaz refuses the Lord's offer of a sign with pious words: *"I will not ask, and I will not put the Lord to the test"* (Isa 7:12). The people *"refused the waters of Shiloah that flow gently"* (8:6). The right refusing and the wrong refusing are set in one oracle, each with its own consequence.; Not answering is already choosing. *"when I called, you did not answer; when I spoke, you did not listen, but you did what was evil in my eyes and chose what I did not delight in"* (Isa 65:12; repeated in 66:4). The ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 7:15 (knows)
- **Observation 19840** (prior-capture, tag statement, status draft): Knowing how. The child chooses *"when he knows how"* (Isa 7:15). The oracle of Isaiah 1 opens with the absence of that knowing: *"Israel does not know, my people do not understand"* (1:3).
  - applies to 3 occurrence(s): Isa 1:3 (knows), Isa 1:3 (know), Isa 7:15 (knows)
- **Observation 19841** (prior-capture, tag statement, status draft): Being taught. *"Who is the man who fears the Lord? Him will he instruct in the way that he should choose"* (Psa 25:12). The teaching comes from who the Lord is: *"Good and upright is the Lord; therefore he instructs sinners in the way"* (25:8). The psalmist asks for it: *"Make me to know your ways, O Lord; teach me your paths"* (25:4). In Psalm 119 he asks *"graciously teach me your law"*, and asks God to do the refusing with him: *"Put false ways far from me"* (119:29).
  - applies to 1 occurrence(s): Psa 25:4 (know)
- **Observation 19857** (prior-capture, tag statement, status draft): Choosing together: A people can choose as one.; Israel at Shechem: *"we will serve the Lord"*, and they become *"witnesses against yourselves"* (Jos 24:21–22).; The gathering in Jerusalem, out of being pleased (Act 6:5).; The church, *"having come to one accord"* (Act 15:25).; Weighing a case together is also called choosing: *"Let us choose what is right; let us know among ourselves what is good"* (Job 34:4).
  - applies to 1 occurrence(s): Job 34:4 (know)
- **Observation 19866** (prior-capture, tag statement, status draft): It held as long as there were people who remembered what it was made from. *"Israel served the Lord all the days of Joshua, and all the days of the elders who outlived Joshua and had known all the work that the Lord did for Israel"* (Jos 24:31). The verse gives the timing; the link to remembering is mine (I read).
  - applies to 1 occurrence(s): Jos 24:31 (known)
- **Observation 19923** (prior-capture, tag statement, status draft): 3.5 Phili 1:22–25, in 10.7 *Life and death set before a person*, as a new bullet: > - A choice between two goods can stay open. *"Yet which I shall choose I cannot tell. I am hard pressed between the two. My desire is to depart and be with Christ, for that is far better. But to remain in the flesh is more necessary on your account"* (Philippians 1:22–24). Paul does not settle it by choosing. He goes on: *"Convinced of this, I know that I will remain and continue with you all"* (1:25).
  - applies to 1 occurrence(s): Phili 1:25 (know)
- **Observation 19931** (prior-capture, tag statement, status draft): 2Sa 14:13–14, in 10.7 *Planning*. This is a citation fix of the #1990 kind: the same Joab issue in a place the #1987 reading did not list. Replace the paragraph that begins *"A plan can also be held against someone's good"* with: > A plan can also be held against someone's good without anyone calling it a plot. Joab knew *"that the king's heart went out to Absalom"* (2 Samuel 14:1). He sent a wise woman of Tekoa with a staged plea, and *"put the words in her mouth"* (14:3). In it she told David that by leaving Absalom in exile he had *"planned such a thing against the people of God"* (14:13). Beside it she set God, who *"devises means so that the banished one will not remain an outcast"* (14 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 14:1 (knew)
- **Observation 19939** (prior-capture, tag statement, status draft): Turned toward it from far off: For those far from the chosen city, the city is the direction of prayer. Solomon's prayer gives the hardest case, the people in captivity because they sinned: *"for there is no one who does not sin"* (1Ki 8:46). The inner turning comes in steps: *"yet if they turn their heart in the land to which they have been carried captive"* (8:47); *"and repent and plead with you … saying, 'We have sinned and have acted perversely and wickedly'"* (8:47); *"if they repent with all their heart and with all their soul in the land of their enemies … and pray to you toward their land, … the city that you have chosen"* (8:48); "Turn" and "repent" are the one verb, *šûb*. The tur ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Ki 8:39 (know)
- **Observation 19941** (prior-capture, tag statement, status draft): Anger at what a choice costs. Saul to Jonathan: *"do I not know that you have chosen the son of Jesse to your own shame"* (1Sa 20:30). Saul calls the choice shame and gives his reason: *"neither you nor your kingdom shall be established"* (20:31). His anger is for his house. It goes from insult to a death sentence to a spear thrown at his own son (20:33). Jonathan's choice was made in love, *"for he loved him as he loved his own soul"* (20:17). His own anger answers his father's, and it is grief for the one he chose: *"he was grieved for David, because his father had disgraced him"* (20:34). The choice holds, sealed by an oath *"in the name of the Lord"* (20:42).
  - applies to 1 occurrence(s): 1Sa 20:30 (know)
- **Observation 19945** (prior-capture, tag statement, status draft): Hatred. *"If you were of the world, the world would love you as its own; but because you are not of the world, but I chose you out of the world, therefore the world hates you"* (Joh 15:19). The verse gives the cause: the choosing. The world's love goes to *"its own"*. The passage says the hatred fell first on Jesus (15:18), and names under it *"because they do not know him who sent me"* (15:21).
  - applies to 2 occurrence(s): Joh 15:18 (know), Joh 15:21 (know)
- **Observation 19953** (prior-capture, tag statement, status draft): Knowing a choice, and arguing from it. In the dispute at Jerusalem Peter appeals to what the assembly knows: *"you know that in the early days God made a choice among you, that by my mouth the Gentiles should hear the word of the gospel and believe"* (Act 15:7). The purpose of God's choosing one man lies in others: that they hear and believe. Their hearts were known by God and *"cleansed … by faith"* (15:8–9). The debate ends in silence and listening (15:12), and the assembly's own choosing follows (15:25).
  - applies to 1 occurrence(s): Act 15:7 (know)
- **Observation 19954** (prior-capture, tag statement, status draft): Knowing that others are chosen, from what was seen. *"For we know, brothers loved by God, that he has chosen you, because our gospel came to you not only in word, but also in power and in the Holy Spirit and with full conviction"* (1Th 1:4–5). The knowing rests on what Paul saw: faith, love and hope at work (1:3), joy in affliction (1:6), and a turning *"to God from idols"* (1:9).
  - applies to 2 occurrence(s): 1Th 1:4 (know), 1Th 1:5 (know)
- **Observation 19955** (prior-capture, tag statement, status draft): Not knowing, and still used. Cyrus is called for the sake of the chosen: *"For the sake of my servant Jacob, and Israel my chosen, I call you by your name, I name you, though you do not know me"* (Isa 45:4). And *"I equip you, though you do not know me"* (45:5). Knowing is held out as the purpose: *"that you may know that it is I"* (45:3).
  - applies to 3 occurrence(s): Isa 45:3 (know), Isa 45:4 (know), Isa 45:5 (know)
- **Observation 19957** (prior-capture, tag statement, status draft): An inner act weighed by what God chooses: In one passage the inner act of the others is itself set against God's choosing. The people fast and ask, *"Why have we humbled ourselves, and you take no knowledge of it?"* (Isa 58:3). They *"delight to know my ways"* and *"delight to draw near to God"* (58:2). Yet *"in the day of your fast you seek your own pleasure, and oppress all your workers"* (58:3). Then: *"Is such the fast that I choose, a day for a person to humble himself?"* (58:5). "Humble himself" is the humbling of the soul, the same words as their own complaint. What God does choose is turned outward: *"to let the oppressed go free"*, *"to share your bread with the hungry"*, *"not to h ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Isa 58:2 (know), Isa 58:3 (knowledge)
- **Observation 20002** (prior-capture, tag statement, status draft): 3.1 It happens in the heart, and it is hidden until it acts: *"Whoever winks his eyes plans dishonest things; he who purses his lips brings evil to pass"* (Pro 16:30). The planning shows only in small signs.; *"I did not know it was against me they devised schemes"* (Jer 11:19). Jeremiah did not see the plan aimed at him.; *"they intended to do me harm"* (Neh 6:2). The intent sat behind the friendly invitation, *"Come and let us meet together"*.; *"But he does not so intend, and his heart does not so think; but it is in his heart to destroy"* (Isa 10:7). Of Assyria, what is in the heart differs from the role God gives it. I read this as the intention belonging to the one who holds it, whatev ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 11:19 (know)
- **Observation 20003** (prior-capture, tag statement, status draft): 3.2 It works in time: the night before, the morning after: *"Woe to those who devise wickedness and work evil on their beds! When the morning dawns, they perform it, because it is in the power of their hand."* (Mic 2:1); *"He plots trouble while on his bed"* (Psa 36:4).; *"For I know what they are inclined to do even today, before I have brought them into the land"* (Deu 31:21). The inclination is already there before the occasion comes.; I read Mic 2:1 as the clearest picture in the set of looking ahead as such. The scheme is held overnight and carried out at dawn, when the hand has the power to do it. The verse itself names the power of the hand as the reason it is done.
  - applies to 1 occurrence(s): Deu 31:21 (know)
- **Observation 20019** (prior-capture, tag statement, status draft): 3.9 God sees the intention: *"the Lord searches all hearts and understands every plan and thought"* (1Ch 28:9).; *"the intention of man's heart is evil from his youth"* (Gen 8:21; also Gen 6:5).; *"he knows our frame; he remembers that we are dust"* (Psa 103:14). H3336 here is "frame", the thing formed.; *"will disclose the purposes of the heart"* (1Co 4:5).
  - applies to 1 occurrence(s): Psa 103:14 (knows)
- **Observation 20128** (prior-capture, tag statement, status draft): The epistle openings and requests (*"I want you to know"*, Phi 1:12; Tit 3:8; Jude 5; 1Ti 2:8; 5:14; 2Jo 12; Phm 13; 3Jo 10) mostly use the word as a stated wish in teaching. Their bearing on setting direction is slight, but each still needs to be read.
  - applies to 1 occurrence(s): Phili 1:12 (know)
- **Observation 20162** (prior-capture, tag statement, status draft): His Spirit and words: *"If you turn at my reproof, behold, I will pour out my spirit to you; I will make my words known to you"* (Pro 1:23), before *"you … would have none of my reproof"* (1:25).
  - applies to 1 occurrence(s): Pro 1:23 (known)
- **Observation 20164** (prior-capture, tag statement, status draft): What the refusal goes with. In these passages the "no" to God is placed beside something the people chose or planned instead: *"But you were unwilling, and you said, 'No! We will flee upon horses'"* (Isa 30:15–16). The refusal is said in their own words, together with their own plan. The chapter opened with *"stubborn children … who carry out a plan, but not mine"* (30:1). They told the prophets, *"Do not prophesy to us what is right; speak to us smooth things"* (30:10).; *"Israel would not submit to me. So I gave them over to their stubborn hearts, to follow their own counsels"* (Psa 81:11–12).; *"Because they hated knowledge and did not choose the fear of the Lord, would have none of my co ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 1:29 (knowledge)
- **Observation 20184** (prior-capture, tag statement, status draft): Wanting to know. *"desiring to know the real reason"* (Act 22:30; 23:28); *"We wish to know therefore what these things mean"* (Act 17:20); *"I would like to hear the man myself"* (Act 25:22); Daniel, *"I desired to know the truth about the fourth beast"* (Dan 7:19).
  - applies to 3 occurrence(s): Act 17:20 (know), Act 22:30 (know), Act 23:28 (know)
- **Observation 20186** (prior-capture, tag statement, status draft): Paul's wishes for the churches are mostly stated wishes in teaching. Their passages give each one a reason: *"I desire then that in every place the men should pray, lifting holy hands without anger or quarreling"* (1Ti 2:8); *"I would have younger widows marry … for some have already strayed after Satan"* (1Ti 5:14–15); *"I want you to insist on these things, so that those who have believed in God may be careful to devote themselves to good works"* (Tit 3:8); *"I want you to know … what has happened to me has really served to advance the gospel"* (Phi 1:12); *"I would rather not use paper and ink … talk face to face, so that our joy may be complete"* (2Jo 12); *"I want to remind you"* (Jude ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Phili 1:12 (know)
- **Observation 20194** (prior-capture, tag statement, status draft): Belshazzar: *"you … have not humbled your heart, though you knew all this"* (5:22). Knowing was not enough.
  - applies to 1 occurrence(s): Dan 5:22 (knew)
- **Observation 20216** (prior-capture, tag statement, status draft): Knowing is not enough. Belshazzar *"knew all this"* and did not humble his heart (Dan 5:22). In the plan set, God *"understands every plan"* (1Ch 28:9). The will set adds that the person's own knowing does not move the will.
  - applies to 1 occurrence(s): Dan 5:22 (knew)
- **Observation 20238** (prior-capture, tag statement, status draft): The chosen are set against others in the passage's own words: those who refused to love the truth and had pleasure in unrighteousness (2Th 2:10–12); those who profess to know God and deny him by works (Tit 1:16); an assembly that judges *"with evil thoughts"* (Jam 2:4); kings of one mind with the beast, and those whose names are not written (Rev 17:8, 13); Stephen's accusers, *"uncircumcised in heart and ears"* (Act 7:51)
  - applies to 1 occurrence(s): Tit 1:16 (know)
- **Observation 20240** (prior-capture, tag statement, status draft): Knowing and remembering.: The chosen are prayed for, that the eyes of their hearts be enlightened to know their hope (Eph 1:18).; Their knowledge of the truth accords with godliness (Tit 1:1).; Forgetting one's cleansing is blindness, and another works to keep them remembering (2Pe 1:9, 12–15).; Batch 1 had the chosen called to remember (Psa 105:5; Isa 44:21).
  - applies to 2 occurrence(s): Eph 1:18 (know), Tit 1:1 (knowledge)
- **Observation 20293** (prior-capture, tag statement, status draft): 2 John 1: "The elder to the elect lady and her children, whom I love in truth": *"The elder to the elect lady and her children, whom I love in truth, and not only I, but also all who know the truth, because of the truth that abides in us and will be with us forever"* (v1–2).; The love is the elder's, and it is shared by *"all who know the truth"*. "Love" is *agapaō* (G0025). "Know" is *ginōskō* (G1097). Both are toward the one called elect. The verse grounds the love *"in truth"* and *"because of the truth that abides in us"*. It does not ground it in the choosing.; The letter goes on: *"I rejoiced greatly to find some of your children walking in the truth"* (v4), and *"this is love, that we ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Jo 1 (know)
- **Observation 20294** (prior-capture, tag statement, status draft): What others do around a choice, in these verses: hate the chosen, because they are chosen out of the world (Joh 15:19); know that God chose, and settle a dispute on it (Act 15:7); believe, as the purpose of God's choosing one man (Act 15:7); seek and not obtain, and be hardened, with eyes that do not see (Rom 11:7–8); know that others are chosen, from what was seen when the gospel came (1Th 1:4–5); endure suffering for the sake of the chosen (2Ti 2:10); reject the chosen one after testing (1Pe 2:4, 7); believe in the chosen one, and not be put to shame (1Pe 2:6); love the chosen in truth (2Jo 1)
  - applies to 3 occurrence(s): Act 15:7 (know), 1Th 1:4 (know), 1Th 1:5 (know)
- **Observation 20297** (prior-capture, tag statement, status draft): Others knowing a choice. In Act 15:7 the assembly knows God's past choice and argues from it. In 1Th 1:4 Paul knows that the readers are chosen, from what he saw. In Joh 15:21 the haters *"do not know him who sent me"*.
  - applies to 2 occurrence(s): Joh 15:21 (know), Act 15:7 (know)
- **Observation 20304** (prior-capture, tag statement, status draft): Job 15:5 — Eliphaz: "your iniquity teaches your mouth, and you choose the tongue of the crafty": Eliphaz weighs Job by his words. He opens with *"Should a wise man answer with windy knowledge"* (v2), and charges *"you are doing away with the fear of God and hindering meditation before God"* (v4). Then he names the choice: *"For your iniquity teaches your mouth, and you choose the tongue of the crafty"* (v5). He reads it this way: something inside, iniquity, teaches the mouth; the mouth then chooses a crafty tongue; From that he gives the verdict: *"Your own mouth condemns you, and not I; your own lips testify against you"* (v6).; He takes his evaluation further inside. He moves from the mout ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 15:2 (knowledge)
- **Observation 20307** (prior-capture, tag statement, status draft): Job 34:33 — Elihu: "For you must choose, and not I": Elihu frames a confession and asks whether Job will make it: *"For has anyone said to God"*: *"I have borne punishment; I will not offend any more"*; *"teach me what I do not see; if I have done iniquity, I will do it no more"* (v31–32). Then: *"Will he then make repayment to suit you, because you reject it? For you must choose, and not I; therefore declare what you know"* (v33).; Two things stand in the verse:
  - applies to 1 occurrence(s): Job 34:33 (know)
- **Observation 20399** (prior-capture, tag statement, status draft): Romans 8:27: "knows what is the mind of the Spirit": > Q1 citation: ✅ Accurate. 10.9 *God's Spirit prays within* quotes vv26–27 accurately. The citation is written as a range, "(Romans 8:26–27)", so a search for "8:27" does not find it. The quoted words "And he who searches hearts knows what is the mind of the Spirit" are v27.; >; >; *"the Spirit helps us in our weakness. For we do not know what to pray for as we ought, but the Spirit himself intercedes for us"* (v26). *"And he who searches hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God"* (v27).; "Mind" is G5427, here the Spirit's mind. "The will of God" in the ESV has n ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Rom 8:26 (know), Rom 8:27 (knows)
- **Observation 20402** (prior-capture, tag statement, status draft): Pro 1:29 | knowledge refused (10.2) | yes, for knowing | the fear of the Lord as chosen or refused; the outcome "their own devices"
  - applies to 1 occurrence(s): Pro 1:29 (knowledge)
- **Observation 20424** (prior-capture, tag statement, status draft): Rom 8:27 | intercession, cited as "Romans 8:26–27" (10.9) | n/a (the Spirit's mind) | "we do not know what to pray for" (v26), for 10.9 *(corrected)*; the Spirit's mind: 13.1 v6 *Purposing* *(corrected)*
  - applies to 1 occurrence(s): Rom 8:26 (know)
- **Observation 20438** (prior-capture, tag face, status draft): Face: Discretion; Verses: Pro 1:4; 2:11; 3:21; 5:2; 8:12; Who thinks: the young, the son, wisdom herself; Joined with / aimed at: knowledge, prudence, sound wisdom. It "watch[es] over you" (Pro 2:11)
  - applies to 3 occurrence(s): Pro 1:4 (knowledge), Pro 5:2 (knowledge), Pro 8:12 (knowledge)
- **Observation 20452** (prior-capture, tag statement, status draft): Where they seem to agree (Claude's reading, worth testing).: Thought isn't simply self-authored.; Science: most processing is automatic and unconscious. Predictive-processing models describe the brain as constantly generating expectations before we are aware of them.; Philosophy: phenomenology observes that thoughts arrive rather than being made.; Bible: the heart runs deeper than we can see into. Jeremiah 17:9–10 says the heart is beyond knowing except by God, and in Psalm 139:23 the psalmist asks God to "know my thoughts."; Thought is shaped by what it takes in and dwells on.; Science: neuroplasticity. Repeated patterns strengthen connections.; Philosophy: Vygotsky's view that language and ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 139:23 (know)
- **Observation 20455** (prior-capture, tag statement, status draft): 4. Knowing a thought is separate from producing it. 1 Corinthians 2:11 says only "the spirit of that person" knows a person's thoughts, and only God's Spirit knows God's. Separately, God searches and knows human thoughts (Psalm 139:23; 1 Chronicles 28:9; Psalm 94:11; 1 Corinthians 3:20), and so does Jesus (Luke 5:22, 6:8, 11:17; Matthew 9:4, 12:25).: *Caveat:* in 1 Corinthians 2:11 the Strong's number is G3588, the Greek article. The word "thoughts" is supplied by the translation; the Greek says "the things of a person."
  - applies to 5 occurrence(s): Psa 94:11 (knows), Mat 12:25 (knowing), Luk 11:17 (knowing), 1Cor 2:11 (knows), 1Cor 3:20 (knows)
- **Observation 20482** (prior-capture, tag statement, status draft): 2. Thoughts arrive, often at night.: "as you lay in bed came thoughts of what would be" (Dan 2:29); "thoughts from visions of the night, when deep sleep falls on men" (Job 4:13); "thoughts will come into your mind" (Ezek 38:10); "doubts arise in your hearts" (Luke 24:38); "an argument arose among them" (Luke 9:46); In Dan 2:29–30, the thoughts that come in the night are tied to revelation: "he who reveals mysteries made known to you."
  - applies to 2 occurrence(s): Dan 2:29 (known), Dan 2:30 (known)
- **Observation 20489** (prior-capture, tag statement, status draft): 9.2 What thoughts are: Design: forming something that does not yet exist. H2803G (19 rows) describes craftsmanship: cherubim "skillfully worked" (Exod 26:1, 31) and "skilled design" (Exod 39:3). The faculty itself is neutral. *Maḥăšāvāh* covers both artistry and plots, and *mᵊzimmāh* covers both "discretion" (Prov 2:11) and "evil devices" (Prov 12:2). What makes a thought good or evil is what it is designed toward.; Reckoning: giving something its value or category. H2803H/J (60 rows): Human misreckoning: Eli "took her to be a drunken woman" (1 Sam 1:13), "we esteemed him stricken" and "we esteemed him not" (Isa 53:3–4), Judah "thought she was a prostitute" (Gen 38:15).; God's reckoning: "he ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): 1Ch 28:9 (know), Psa 139:2 (know), Psa 139:23 (know)
- **Observation 20547** (prior-capture, tag face, status draft): Face: Our frame; Verses: Psa 103:14; What differs: God "knows our frame; he remembers that we are dust"; Why: Knowing the frame produces pity (S, 103:13)
  - applies to 1 occurrence(s): Psa 103:14 (knows)
- **Observation 20559** (prior-capture, tag statement, status draft): *raʿyôn* (Aramaic) | Night thoughts that carry revelation · thoughts that alarm | Dan 2:29–30 · Dan 4:19; 5:6, 10; 7:28 | The same night thoughts become revelation when God makes them known and an interpreter speaks (2:29–30; 5:10–12 points to Daniel). Without that they alarm, and the body shows it. Daniel's own alarm is kept, not acted on: "but I kept the matter in my heart" (7:28) (S)
  - applies to 2 occurrence(s): Dan 2:29 (known), Dan 2:30 (known)
- **Observation 20569** (prior-capture, tag statement, status draft): *logismos* | An inner court of thoughts · arguments raised against God | Rom 2:15 · 2Co 10:5 | Thoughts that judge the self, against thoughts raised against God's knowledge (S)
  - applies to 1 occurrence(s): 2Cor 10:5 (knowledge)
- **Observation 20603** (reading, tag face, status draft): 'you make it known to me' is Job's request of the Lord, in the causative stem: the knowing is to come from the one questioned.
  - applies to 1 occurrence(s): Job 42:4 (known)
- **Observation 20604** (reading, tag term, status draft): H3045 yada, 'known': to know; in the causative stem, to make known, to let someone know.
  - applies to 1 occurrence(s): Job 42:4 (known)
- **Observation 20605** (reading, tag qualification, status draft): What 'you make it known to me' gives the questioning in Job 42:4: it names the end of the question, which is that the one questioned makes known to the questioner.
  - applies to 1 occurrence(s): Job 42:4 (known)

### 4.3 The retired catalogue observations (194, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

| stage | tag | live observations |
|---|---|---|
| char-reading | surface-gloss-divergence | 3 |
| char-subgroup | difference-inference | 1 |
| verse-reading | answered-no-flag | 90 |
| verse-reading | not-related-to-meaningful-word | 69 |
| verse-reading | tightly-related | 10 |
| verse-reading | no-impact | 9 |
| verse-reading | attested-pre-nt | 4 |
| verse-reading | no-direct-connection | 3 |
| verse-reading | surface-gloss-divergence | 2 |
| verse-reading | alternative-meaning | 1 |
| verse-reading | could-not-resolve | 1 |
| verse-reading | needs_adjacent_verse_context | 1 |

### 4.4 Withdrawn observations (59)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 57 |
| Analysis_phase_1 | 2 |

| reason as stored | observations |
|---|---|
| no change record | 57 |
| the old form of parts is replaced by the nine items | 2 |

## 5. Claims and the narrative

103 claims rest on these occurrences: 0 on an observation of these words and 103 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (0)

_none_

### 5.2 Claims reached by a verse only (103)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| I-6 | God's Spirit is given into the heart (Gal 4:6; 2Co 1:22), pours love into hearts (Rom 5:5), is put within (Eze 36:27), comes upon people (Judg 14:6; 1Sa 16:13), and makes the body a temple (1Co 6:19). The human spirit is one of several places, not the primary one (dep §2.3d, §3.7) | 1Co 6:19 | know G1492G | current | not told in a section |
| 1-1 | Soul and spirit in synonymous parallel (Isa 26:9; Job 7:11; Luk 1:46–47) | Isa 26:9; Pro 2:10 | learn H3925H; knowledge H1847 | current | not told in a section |
| 2-1 | In these verses *nephesh* is the person, the one who answers for sin; it is not a faculty inside the person. The soul is the accountable, answerable self (D §3.1, §11.2) | Leviticus 5:1; Leviticus 5:17 | know H3045 | current | not told in a section |
| 2-3 | Souls are saved from death and purified (Jam 5:20; 1Pe 1:22) | Jam 5:20 | know G1097 | current | chapter 02 Life, breath and death, Delivered from death (1 earlier telling(s) in the workbook) |
| 2-5 | Animals almost never have *rûaḥ*; Ecc 3:21 is the only exception; Gen 7:22 uses *neshamah*, not *rûaḥ* | Ecc 3:21 | knows H3045 | withdrawn | not told in a section |
| 2-11 | Stands for the NT. In the OT, flesh is frail, not hostile, and "a heart of flesh" is God's gift (Eze 36:26). The hostility of flesh to Spirit is NT-specific (dep §3.5) | Joh 3:8 | know G6063 | current | not told in a section |
| 2-15 | The spirit is prominent in worship and is what is committed to God at death (E §13.4). Pro 20:27 uses *neshamah* "breath", not *rûaḥ* [lexical], and is outside the reading. The human spirit is equally temper, trouble and provocation (Pro 29:11; Gen 41:8; Act 17:16) | Gen 41:8 | interpret H6622 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death (1 earlier telling(s) in the workbook) |
| 3-4 | Whether this is spirit or breath cannot be decided from the verse (SC: U) | Ecc 11:5 | know H3045 | current | not told in a section |
| 3-9 | Most of these verses speak of the soul delivered or brought up from Sheol: a living person rescued from death. Corrected 2026-10-04 (#1950): of 15 soul-delivered verses, 12 are rescue from dying; Psa 49:15 (set against the death of all, 49:10) and Psa 16:10 (as Act 2:27, 31 read it) look beyond death; Psa 89:48 says no one can. The verdict holds: no verse gives soul and spirit different destinations. The verses that name Sheol or Hades speak of the soul and never of the spirit. Ecc 3:21 leaves the spirit's destination open ("Who knows?"). The "different destinations" argument, which the original called "the most compelling evidence", does not hold (G §16.4; dep §3.9) | Ecc 3:21 | knows H3045 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death; chapter 02 Life, breath and death, Delivered from death; chapter 09 Where the words part, Lines that are often drawn, but that I cannot find (3 earlier telling(s) in the workbook) |
| 4-4 | Hebrew has no word for "mind"; it uses *lēv* | Psa 103:14 | knows H3045 | current | chapter 04 The heart, The heart thinks, attends and remembers |
| 9-7 | Rom 1:21–32 as a five-step descent | Rom 1:21–32 | knew G1097; know G1921 | held | not told in a section |
| 10-1 | The verses read give the Spirit into the heart (Gal 4:6; 2Co 1:22; Rom 5:5), within (Eze 36:27) and in the body (1Co 6:19), and bear witness with our spirit (Rom 8:16). The renewal texts renew heart and spirit together and replace stone with flesh (Eze 11:19; 36:26) (E §11.2) | 1Co 6:19 | know G1492G | current | not told in a section |
| 10-3 | "Within" is already the OT promise (Eze 36:27; 37:14). The OT also has the Spirit turning a man "into another man" (1Sa 10:6) | Eze 36:27; 37:14 | know H3045 | current | not told in a section |
| C-83 | Death comes to everyone, and falls alike on those the world would set apart | Genesis 3:22; Job 30:23 | knowing H3045; know H3045 | current | chapter 02 Life, breath and death, What death is (2 earlier telling(s) in the workbook) |
| C-84 | The same death is met in different ways, and nothing goes with the dead | Genesis 27:2 | know H3045 | current | chapter 02 Life, breath and death, What death is (1 earlier telling(s) in the workbook) |
| C-85 | Scripture ties death to sin from the first command | Genesis 2:17 | knowledge H1847 | current | chapter 02 Life, breath and death, Death and sin (2 earlier telling(s) in the workbook) |
| C-88 | Scripture speaks of death inside a living person: the heart dying first, the living called dead, abiding in death | Revelation 3:1; 1 John 3:14 | know G6063 | current | chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook) |
| C-89 | Scripture speaks of death as sleep, and gives its hope against death as waking | Luke 8:52-53 | knowing G6063 | current | chapter 02 Life, breath and death, Sleep and waking (2 earlier telling(s) in the workbook) |
| C-93 | One way the Old Testament speaks of where the dying go is going down to Sheol; it says where Sheol lies (beneath, the measure of depth) but not what it is made of | Job 11:8 | know H3045 | current | chapter 02 Life, breath and death, Going down to Sheol (2 earlier telling(s) in the workbook) |
| C-95 | The manner of going down to Sheol is named: mourning, with sorrow, in peace, with blood, silently, alive | 1 Kings 2:9 | know H3045 | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-96 | The way to Sheol is already walked in the heart before the end comes | Proverbs 5:5-6 | know H3045 | current | chapter 02 Life, breath and death, Going down to Sheol (1 earlier telling(s) in the workbook) |
| C-105 | Deliverance from death is for something: walking before God among the living and telling of him | Isaiah 38:19 | known H3045 | current | chapter 02 Life, breath and death, Delivered from death (1 earlier telling(s) in the workbook) |
| C-106 | Some verses say the dead know nothing, do not praise God and do not return | Job 7:9-10; Ecclesiastes 9:5; Ecclesiastes 9:10; Isaiah 38:18-19 | know H5234A; know H3045; knowledge H1847; known H3045 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-109 | Scripture speaks of the dead in more than one way, and neither way is made to explain the other away | Ecclesiastes 9:5 | know H3045 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-111 | Life is held in the breath, and the breath is God's to give and to take back | Daniel 5:23 | know H3046 | current | chapter 02 Life, breath and death, Breath lent, and held by God (1 earlier telling(s) in the workbook) |
| C-112 | When the breath goes, a person's plans go with it | Psalm 94:11 | knows H3045 | current | chapter 02 Life, breath and death, Breath lent, and held by God (1 earlier telling(s) in the workbook) |
| C-119 | Long days are promised with some commands, and the Preacher sets the righteous who perish beside them; both are stated | Ecclesiastes 8:12 | know H3045 | current | chapter 02 Life, breath and death, Life set before a person (2 earlier telling(s) in the workbook) |
| C-120 | Wisdom marks where the way to death ends, and some of what kills a person is named from within | Job 36:12 | knowledge H1847 | current | chapter 02 Life, breath and death, Life set before a person (3 earlier telling(s) in the workbook) |
| C-125 | The commonest form of the oath by life is "As the Lord lives" (39 verses); in six of them a second life is joined | 1 Samuel 20:3 | know H3045; knows H3045 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-126 | The oath "As the Lord lives" places a promise before the living God and binds the speaker to it by life | 1 Samuel 20:3 | know H3045; knows H3045 | current | chapter 02 Life, breath and death, Living before God (2 earlier telling(s) in the workbook) |
| C-131 | Scripture counts a life in days and says what the days are for | Deuteronomy 4:10; Deuteronomy 17:19 | learn H3925H | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-147 | The verses name what brings death in the living, each in its own place; no verse gathers them into one list | Revelation 3:1; 1 John 3:14 | know G6063 | current | chapter 02 Life, breath and death, Death in the living (2 earlier telling(s) in the workbook) |
| C-148 | The verses name the way out of death in the living: hearing the Son and believing, God making alive with forgiveness, waking, coming home; loving the brothers is its sign | 1 John 3:14 | know G6063 | current | chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook) |
| C-149 | One person's freedom can destroy another | 1 Corinthians 8:11 | knowledge G1108 | current | chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook) |
| C-150 | The believer has already died to sin, to the law and to the powers of the world, and a putting to death is still to be done | Romans 6:2-3; 2 Corinthians 5:14 | not know G0050; concluded G2919 | current | chapter 14 Made new, Revived, restored, renewed; chapter 02 Life, breath and death, Dead to sin (3 earlier telling(s) in the workbook) |
| C-152 | The coming of death is often met with anguish and terror, and the fear of dying shapes what people do | 1 Samuel 20:3 | know H3045; knows H3045 | current | chapter 02 Life, breath and death, Facing death (2 earlier telling(s) in the workbook) |
| C-155 | A death is met by those who remain: grief, not watching, fasting and then eating, reproach, limits on mourning, mourning withheld, and death not taken to heart | 2 Samuel 12:21-23; 2 Samuel 19:6 | knows H3045; know H3045 | current | chapter 02 Life, breath and death, Those left behind (3 earlier telling(s) in the workbook) |
| C-157 | Of the seven wishes to die answered in these passages, two are fed, two are answered another way, and three are granted, each to a man already blinded or wounded | Jonah 4:9-11 | know H3045 | current | chapter 02 Life, breath and death, Wanting to die (3 earlier telling(s) in the workbook) |
| C-159 | The dead made alive are living people; the crossing from death to life happens now, and life is spoken of as had now and still to come | 1 John 5:13; 1 John 3:14 | know G6063 | current | chapter 02 Life, breath and death, Made alive (1 earlier telling(s) in the workbook) |
| C-160 | The making alive rests on a death, and Christ went to it himself | Romans 6:9-10 | know G6063 | current | chapter 02 Life, breath and death, Made alive (2 earlier telling(s) in the workbook) |
| C-161 | That death changes how the living live: no longer for themselves, dead to sin, Christ living in them | 2 Corinthians 5:14-15 | concluded G2919 | current | chapter 02 Life, breath and death, Made alive (2 earlier telling(s) in the workbook) |
| C-162 | A death, too, can belong to the Lord, and a dying can go on while a person lives | 2 Corinthians 6:9 | known G1921 | current | chapter 02 Life, breath and death, Dying to the Lord (1 earlier telling(s) in the workbook) |
| C-163 | Scripture speaks of the death of the upright in its own words: precious, wished for, a refuge, in faith, bearing fruit, glorifying God | Hebrews 11:13 | acknowledged G0782; acknowledged G3670 | current | chapter 02 Life, breath and death, Dying to the Lord (1 earlier telling(s) in the workbook) |
| C-165 | People hold to someone, or to something, even to death, and the readiness can fail | Luke 22:33-34 | know G6063 | current | chapter 02 Life, breath and death, Dying to the Lord; chapter 10.10 Relating to others, Loyalty and honour (3 earlier telling(s) in the workbook) |
| C-167 | Humility is not a feeling in the verses; they speak of it as an act, a standing, a quality sought and walked in, a state of the spirit, a place taken, something done to a person, and God's own way | Deuteronomy 8:2 | know H3045 | current | chapter 10.14 Humility, (opening) (1 earlier telling(s) in the workbook) |
| C-168 | Humility is always set against a rising: the proud heart, the lifted-up self, the stiff neck, the haughty eyes | Daniel 5:20-23 | knew H1768; knew H3046; know H3046 | current | chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit; chapter 10.14 Humility, (opening) (2 earlier telling(s) in the workbook) |
| C-170 | Most often a person humbles himself when a word reaches him, and the humbling owns that God is right | Daniel 5:22 | knew H3046 | current | chapter 10.14 Humility, It answers a word heard; chapter 10.9 Relating to God, Humbling oneself before God (2 earlier telling(s) in the workbook) |
| C-171 | Humbling happens in the heart; Hezekiah's is the same heart turning back from its own pride | Daniel 5:22 | knew H3046 | current | chapter 04 The heart, The heart and anger; chapter 10.7 Choosing and setting direction, Willing; chapter 10.13 Anger, The heart that turns, and the heart that does not; chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit; chapter 10.14 Humility, Where it happens; chapter 04 The heart, The heart humbled (6 earlier telling(s) in the workbook) |
| C-175 | God sees the one who humbles himself and answers, in measure; the humbling does not hold by itself | 2 Chronicles 12:7-8; 2 Chronicles 33:13 | know H3045; knew H3045 | current | chapter 10.13 Anger, The heart that turns, and the heart that does not; chapter 10.14 Humility, God sees it, and answers in measure; chapter 10.9 Relating to God, Humbling oneself before God (4 earlier telling(s) in the workbook) |
| C-176 | The humbling God does not take knowledge of is kept alongside self-pleasure and oppression and leaves the seen naked uncovered; Ahab's, against himself when the word came, was answered | Isaiah 58:3-7 | knowledge H3045 | current | chapter 10.7 Choosing and setting direction, Others around a choice; chapter 13.1 Divine, Choosing; chapter 10.14 Humility, A humbling God does not take knowledge of (3 earlier telling(s) in the workbook) |
| C-178 | God humbles to show what is in the heart, to teach what a person lives by, and to do him good in the end, against the heart that lifts itself up in plenty | Deuteronomy 8:2-3; Deuteronomy 8:14-17 | know H3045; know H0834A; know H3808; know H4616 | current | chapter 10.14 Humility, Being humbled by God; chapter 04 The heart, The heart humbled (2 earlier telling(s) in the workbook) |
| C-181 | Only God lifts up and puts down; a person cannot abase the proud | Eze 17:24 | know H3045 | current | chapter 10.14 Humility, The proud brought low, the lowly raised (1 earlier telling(s) in the workbook) |
| C-186 | Meekness stands where another provokes and leaves the answer to God | Numbers 12:1-8 | known H0413; known H3045 | current | chapter 10.14 Humility, The humble (1 earlier telling(s) in the workbook) |
| C-187 | Humility goes with the ear that can take a reproof and a word, and does not answer before it hears | James 1:19-21 | know G6063 | current | chapter 10.14 Humility, Humility as a way of walking; chapter 10.2 Knowing and hearing, Humility and hearing (3 earlier telling(s) in the workbook) |
| C-188 | What God looks to is set against a religious act in the humility passages (the fast, the walk, the house, the broken heart), as in the other passages gathered in 13.1; the offering follows the broken heart | Isaiah 58:3-7 | knowledge H3045 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 11 Other sides of the inner being, What changes the character; chapter 13.1 Divine, Delight; chapter 10.14 Humility, Humility as a way of walking (6 earlier telling(s) in the workbook) |
| C-192 | Gentleness in meeting a wrong is joined to watching oneself, remembering what one was, and leaving the outcome to God | 2 Timothy 2:25 | knowledge G1922 | current | chapter 10.10 Relating to others, (opening); chapter 10.10 Relating to others, Holding authority over another; chapter 10.14 Humility, Toward one another; chapter 10.10 Relating to others, Humility toward one another (5 earlier telling(s) in the workbook) |
| C-197 | In the New Testament humility rests on what is said of Jesus; the saying he taught, that whoever humbles himself will be exalted, is what is told of him | Philippians 2:3-9; Matthew 11:29 | grasped G0725; learn G3129 | current | chapter 10.14 Humility, Jesus (2 earlier telling(s) in the workbook) |
| C-200 | The same lines of humility run through both Testaments; the New differs in emphasis, adding humility toward one another, and in one new thing, Christ, in whom God's lowering is done in a human life | Philippians 2:3-8 | grasped G0725 | current | chapter 10.14 Humility, The Old Testament and the New (3 earlier telling(s) in the workbook) |
| C-201 | Humility changes character with who acts, toward whom, and to what end | Philippians 4:12 | know G1492G | current | chapter 11 Other sides of the inner being, What changes the character; chapter 10.14 Humility, When humility changes character (2 earlier telling(s) in the workbook) |
| C-202 | The lowering that the Old Testament tells of God is done in the Son in a human life | Psalm 138:6; Philippians 2:6-9; Matthew 11:29 | knows H3045; grasped G0725; learn G3129 | current | chapter 10.14 Humility, The Old Testament and the New; chapter 13.1 Divine, Lowering himself (3 earlier telling(s) in the workbook) |
| C-203 | God sees and answers the one who humbles himself, gives favor to the humble, humbles to test and do good, brings the proud low and looks on a humble estate | Deuteronomy 8:16 | know H0834A; know H3045 | current | chapter 13.1 Divine, Willing; chapter 13.1 Divine, Lowering himself (2 earlier telling(s) in the workbook) |
| C-206 | The offering is weighed by what is inside the one who brings it: an ear opened, the law in the heart, a broken heart, a love that lasts | Hosea 6:4-6; Matthew 9:13; Matthew 12:7 | knowledge H1847; learn G3129; known G1097 | current | chapter 13.1 Divine, Delight (1 earlier telling(s) in the workbook) |
| C-213 | Pride, the boast and the mock belong together in the verses | Jeremiah 48:29-30 | know H3045 | current | chapter 10.15 Pride, (opening) (1 earlier telling(s) in the workbook) |
| C-214 | Pride holds as its own what was given: strength, healing, majesty, wealth, beauty and height are given, and the heart rises on them | Deuteronomy 8:14-18 | know H0834A; know H3045 | current | chapter 04 The heart, The heart and anger; chapter 10.1 Feeling, How a feeling rises; chapter 10.3 Remembering and forgetting, Remembering as a cure, and remembering as hope; chapter 10.4 Thinking, What thinking does; chapter 10.6 Wanting, Thirst answered; chapter 11 Other sides of the inner being, 2. Thresholds: the merry heart and the sad heart; chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit; chapter 10.15 Pride, Given, then held as one's own; chapter 13.1 Divine, Majesty (11 earlier telling(s) in the workbook) |
| C-217 | Pride at its full height says of itself what is true only of God: the proud city's "I am, and there is no one besides me" repeats God's self-statement | Isaiah 45:5; Isaiah 47:8; Isaiah 47:10 | know H3045; knowledge H1847 | current | chapter 10.15 Pride, The heart that says what God says; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-222 | Pride is set against hearing: it will not take rebuke or advice, and the scoffer is known by what he will not receive | Proverbs 14:6 | knowledge H1847 | current | chapter 10.2 Knowing and hearing, (opening); chapter 10.15 Pride, Pride and hearing; chapter 10.2 Knowing and hearing, Pride and hearing (3 earlier telling(s) in the workbook) |
| C-223 | Presumption acts on its own word where another word was given: speaking what God did not command, going up when told not to, not keeping the decision given | Deuteronomy 18:20-22 | know H3045 | current | chapter 10.7 Choosing and setting direction, Others around a choice; chapter 10.9 Relating to God, Kept from what would rule; chapter 10.15 Pride, The words; chapter 10.15 Pride, Pride and hearing; chapter 10.7 Choosing and setting direction, Presumption (5 earlier telling(s) in the workbook) |
| C-226 | Pride stands over someone: the poor, the widow, the needy left unaided, the righteous; it closes the heart to pity and is set against love | 1 Corinthians 8:1 | know G6063; knowledge G1108 | current | chapter 10.15 Pride, Pride over another; chapter 10.10 Relating to others, Pride over another (2 earlier telling(s) in the workbook) |
| C-228 | The verses do not condemn boasting as such; they judge it by what it rests on | Jeremiah 9:23-24; Proverbs 27:1 | knows H3045; know H3045 | current | chapter 10.15 Pride, The boast (2 earlier telling(s) in the workbook) |
| C-232 | A boast can be in another person, and it puts the one who boasts at stake on the other's conduct | 2 Corinthians 9:2-4 | know G6063 | current | chapter 10.15 Pride, The boast; chapter 10.10 Relating to others, Pride over another (2 earlier telling(s) in the workbook) |
| C-236 | The one who is high by nature comes near the low; those who make themselves high are known from afar | Psalm 138:6 | knows H3045 | current | chapter 10.15 Pride, Where it ends; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-237 | The charge of pride can come from another's anger or from a ready explanation, and the verses do not make it true | 1 Samuel 17:28-29 | know H3045 | current | chapter 04 The heart, The heart and anger; chapter 10.4 Thinking, When anger thinks; chapter 10.14 Humility, The proud brought low, the lowly raised; chapter 10.15 Pride, Where it ends (4 earlier telling(s) in the workbook) |
| C-241 | The Son's majesty is received and grounded, stands beside his being handed over, and does not defend itself against mockery; he did not grasp what pride grasps | 2 Peter 1:16-17; Luke 23:34; Philippians 2:6 | made known G1107; know G6063; grasped G0725 | current | chapter 10.15 Pride, The mock; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-243 | One Greek word is rendered both boast and rejoice: the boast in self and joy in hope and in suffering | Romans 5:2-3 | knowing G6063 | current | chapter 10.15 Pride, The words (1 earlier telling(s) in the workbook) |
| C-244 | A plan can presume on time it does not own; the boast about tomorrow is set against saying If the Lord wills | James 4:13-16; Proverbs 27:1 | know G1987; know H3045 | current | chapter 10.15 Pride, The boast; chapter 10.7 Choosing and setting direction, Presumption (2 earlier telling(s) in the workbook) |
| C-247 | Ezra's heart set to study the Law, to do it and to teach it is given straight after the good hand of God on him, as its ground in him | Ezr 7:10 | study H1875 | current | chapter 10.7 Choosing and setting direction, Setting the heart; chapter 13.1 Divine, Delight (2 earlier telling(s) in the workbook) |
| C-257 | God's reversal of high and low is done so that he is known, and is as sure as his word | Eze 17:24 | know H3045 | current | chapter 10.14 Humility, The proud brought low, the lowly raised (1 earlier telling(s) in the workbook) |
| C-258 | In the parable of the banquet the master's anger rests on the invited guests' refusals, turns into a wider invitation to the poor, and ends with the refusers shut out | Luk 14:19 | examine G1381 | current | chapter 10.13 Anger, Other parties (1 earlier telling(s) in the workbook) |
| C-259 | God names judging the cause of the poor and needy as knowing him, and sets it against eyes and heart given only to gain | Jer 22:16 | know H1847; know H1931 | current | chapter 10.2 Knowing and hearing, (opening); chapter 10.6 Wanting, Possessions (2 earlier telling(s) in the workbook) |
| C-263 | The indignation at the ointment, first said to themselves, named the poor as its reason, and Jesus put doing good to the poor in the hearers' own will | Mat 26:10 | aware G1097 | current | chapter 10.13 Anger, What it rises at (1 earlier telling(s) in the workbook) |
| C-273 | The Gospels show the risen body without defining it | Joh 20:14; Joh 21:4 | know G1492I | current | chapter 02 Life, breath and death, Christ first (1 earlier telling(s) in the workbook) |
| C-274 | Jesus puts the denial of the resurrection down to knowing neither the Scriptures nor the power of God, and answers it from God's name | Mat 22:29 | know G6063 | current | chapter 02 Life, breath and death, Believed, questioned, denied (1 earlier telling(s) in the workbook) |
| C-278 | The coming resurrection is given as a reason for how a person lives now: giving without return, enduring, self-control, steadfast work | 1Cor 15:58 | knowing G6063 | current | chapter 02 Life, breath and death, Waited for (1 earlier telling(s) in the workbook) |
| C-280 | Paul sets the creation's eager waiting and groaning before the believers' own inward groaning | Rom 8:22 | know G6063 | current | chapter 02 Life, breath and death, Waited for (1 earlier telling(s) in the workbook) |
| C-298 | Trust in God can be attacked by casting doubt on the one who leads and by naming a past of power | 2Ch 32:13 | know H3045 | current | chapter 10.9 Relating to God, Knowing who rules (1 earlier telling(s) in the workbook) |
| C-300 | God's call can go unanswered, and the same passage sets beside it the servant's ear awakened morning by morning | Isa 50:4 | know H3045 | current | chapter 10.2 Knowing and hearing, Doubt (1 earlier telling(s) in the workbook) |
| C-311 | Adonijah's wish for Abishag was read by Solomon as the throne asked for again; the verses give Solomon's reading, not Adonijah's heart | 1Ki 2:15 | know H3045 | current | chapter 10.6 Wanting, A person (1 earlier telling(s) in the workbook) |
| C-319 | The heart is called on as the witness of the harm it knows it did | 1Ki 2:44 | know H3045 | current | chapter 04 The heart, The heart judges itself (1 earlier telling(s) in the workbook) |
| C-324 | Pride's heart tells itself it will not be moved and that loss and mourning will not come, and it does not lay its end to heart | Isa 47:8 | know H3045 | current | chapter 04 The heart, The heart speaks to itself; chapter 10.15 Pride, The heart that says what God says (2 earlier telling(s) in the workbook) |
| C-332 | God chooses a people out of love, not for their number; the choosing names them his treasured possession and his chosen ones, does not cast them off, and is for their knowing him. | Isa 43:10 | know H3045 | current | chapter 13.1 Divine, Choosing; chapter 10.7 Choosing and setting direction, Being chosen |
| C-336 | Choosing the good rests on knowing and on being taught; the choice binds the one who makes it as a witness, and is held by holding fast. | Isa 7:15; Job 34:4 | knows H3045; know H3045 | current | chapter 10.7 Choosing and setting direction, What a choice rests on; chapter 10.7 Choosing and setting direction, Holding a choice |
| C-338 | The choice is the chooser's own: it is placed on them and not on another, honoured by others, and given of one's own accord. | Job 34:33 | know H0589; know H3045 | current | chapter 10.7 Choosing and setting direction, A choice that is honoured; chapter 10.7 Choosing and setting direction, Choosing before God; chapter 10.7 Choosing and setting direction, Choices weighed by another |
| C-347 | The same will word names a refusal that keeps faith, to the Lord's anointed, his priests, the lives of others, and against enticement, and a refusal that does violence, the stronger shutting out the plea of the weaker; the passage gives the reason each time. | 1Sa 22:17; Judg 19:25 | knew H3045 | current | chapter 10.7 Choosing and setting direction, Willing |
| C-353 | A king's will made absolute is brought down until he knows that the Most High rules and gives the kingdom to whom he will; the Most High does according to his will, and none can stay his hand. | Dan 5:21; Dan 4:17; Dan 4:25; Dan 4:32 | knew H1768; knew H3046; know H1768; know H3046 | current | chapter 10.7 Choosing and setting direction, Willing; chapter 13.1 Divine, Willing |
| C-359 | Looking ahead weighs ability and cost before acting, plans under uncertainty, carries a person's word, can part companions or set one apart from a council's decision, and can plan another's good. | Act 27:39 | recognize G1921 | current | chapter 10.7 Choosing and setting direction, Planning |
| C-361 | God also thinks and plans: his plan stands where human plans cross it, he takes thought for the one in need, and he speaks in his heart. | Jer 29:11 | know H3045 | current | chapter 11 Other sides of the inner being, 8. God has a heart and a soul; chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 13.1 Divine, Purposing |
| C-363 | Thoughts and plans are wholly open to God, the inclination is known before it acts, and the purposes of the heart will be disclosed. | 1Ch 28:9; Deu 31:21 | know H3045 | current | chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 04 The heart, The heart is hidden, and God sees it; chapter 10.7 Choosing and setting direction, Planning |
| C-369 | The inclination of the heart (yetser) is the same word as the potter's thing formed and as our frame; it is evil in Gen 6:5 and stayed on God in Isa 26:3. | Psa 103:14 | knows H3045 | current | chapter 10.4 Thinking, The inclination: a shaped thing; chapter 12 When the inner being goes wrong, The heart as the source |
| C-379 | God's purpose stands before the ages, does not rest on works, and is set forth in Christ. | Eph 1:9; Eph 3:11 | known G1107; realized G4160G | current | chapter 13.1 Divine, Purposing |
| C-380 | The Spirit intercedes according to God's will, the purpose is turned toward those who love him, and a person can reject it for himself. | Rom 8:27; Rom 8:28 | knows G6063; know G6063 | current | chapter 13.1 Divine, Purposing |
| C-383 | Wanting set on riches or the world leads into a snare and into enmity with God, and an intention can be pinned on another. | Jam 4:4 | know G6063 | current | chapter 10.7 Choosing and setting direction, Willing; chapter 10.10 Relating to others, Plotting against another |
| C-384 | The will word is used of the Father, the Son and the Spirit; God's will is free and stands, and at Gethsemane the Son's will is given up to the Father's. | Mat 11:27; Luk 10:22 | knows G1921; knows G1097 | current | chapter 13.1 Divine, Willing; chapter 10.7 Choosing and setting direction, Willing |
| C-393 | God's dedicating of a person comes before the person knows or wills, and the person's shrinking answer is met with a sending and a presence. | Jer 1:5 | knew H3045 | current | chapter 10.7 Choosing and setting direction, Dedicating |

### 5.3 The narrative sections that tell these claims (99)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 6 | 02 Life, breath and death | Breath lent, and held by God | C-111, C-112 |
| 8 | 02 Life, breath and death | Life set before a person | C-119, C-120 |
| 9 | 02 Life, breath and death | Living before God | C-125, C-126, C-131 |
| 11 | 02 Life, breath and death | What death is | C-83, C-84 |
| 12 | 02 Life, breath and death | Death and sin | C-85 |
| 13 | 02 Life, breath and death | Death in the living | C-88, C-147, C-148, C-149 |
| 14 | 02 Life, breath and death | Sleep and waking | C-89 |
| 16 | 02 Life, breath and death | Facing death | C-152 |
| 17 | 02 Life, breath and death | Wanting to die | C-157 |
| 18 | 02 Life, breath and death | Soul, spirit and heart at death | 2-15, 3-9 |
| 20 | 02 Life, breath and death | Delivered from death | 2-3, 3-9, C-105 |
| 21 | 02 Life, breath and death | Made alive | C-159, C-160, C-161 |
| 22 | 02 Life, breath and death | Dying to the Lord | C-162, C-163, C-165 |
| 25 | 02 Life, breath and death | Christ first | C-273 |
| 27 | 02 Life, breath and death | Waited for | C-278, C-280 |
| 29 | 02 Life, breath and death | After death | C-106, C-109 |
| 41 | 04 The heart | The heart speaks to itself | C-324 |
| 42 | 04 The heart | The heart thinks, attends and remembers | 4-4 |
| 45 | 04 The heart | The heart and anger | C-171, C-214, C-237 |
| 49 | 04 The heart | The heart judges itself | C-319 |
| 50 | 04 The heart | The heart is hidden, and God sees it | C-363 |
| 89 | 09 Where the words part | Lines that are often drawn, but that I cannot find | 3-9 |
| 98 | 10.1 Feeling | How a feeling rises | C-214 |
| 122 | 10.2 Knowing and hearing | (opening) | C-222, C-259 |
| 125 | 10.2 Knowing and hearing | Doubt | C-300 |
| 130 | 10.3 Remembering and forgetting | Remembering as a cure, and remembering as hope | C-214 |
| 136 | 10.4 Thinking | The inclination: a shaped thing | C-369 |
| 137 | 10.4 Thinking | What thinking does | C-214 |
| 139 | 10.4 Thinking | When anger thinks | C-237 |
| 144 | 10.4 Thinking | Small, passing, and wholly seen | C-361, C-363 |
| 175 | 10.6 Wanting | Thirst answered | C-214 |
| 176 | 10.6 Wanting | A person | C-311 |
| 180 | 10.6 Wanting | Possessions | C-259 |
| 184 | 10.7 Choosing and setting direction | What a choice rests on | C-336 |
| 187 | 10.7 Choosing and setting direction | Choosing before God | C-338 |
| 188 | 10.7 Choosing and setting direction | Being chosen | C-332 |
| 189 | 10.7 Choosing and setting direction | Others around a choice | C-176, C-223 |
| 191 | 10.7 Choosing and setting direction | A choice that is honoured | C-338 |
| 194 | 10.7 Choosing and setting direction | Setting the heart | C-247 |
| 195 | 10.7 Choosing and setting direction | Holding a choice | C-336 |
| 196 | 10.7 Choosing and setting direction | Planning | C-359, C-363 |
| 197 | 10.7 Choosing and setting direction | Willing | C-171, C-347, C-353, C-383, C-384 |
| 200 | 10.7 Choosing and setting direction | Choices weighed by another | C-338 |
| 214 | 10.9 Relating to God | Kept from what would rule | C-223 |
| 216 | 10.9 Relating to God | Knowing who rules | C-298 |
| 218 | 10.10 Relating to others | (opening) | C-192 |
| 229 | 10.10 Relating to others | Plotting against another | C-383 |
| 230 | 10.10 Relating to others | Holding authority over another | C-192 |
| 232 | 10.10 Relating to others | Loyalty and honour | C-165 |
| 259 | 10.13 Anger | What it rises at | C-263 |
| 282 | 10.13 Anger | The heart that turns, and the heart that does not | C-171, C-175 |
| 289 | 10.13 Anger | Other parties | C-258 |
| 294 | 11 Other sides of the inner being | 2. Thresholds: the merry heart and the sad heart | C-214 |
| 296 | 11 Other sides of the inner being | 4. One word, opposite values | C-188 |
| 297 | 11 Other sides of the inner being | What changes the character | C-188, C-201 |
| 302 | 11 Other sides of the inner being | 8. God has a heart and a soul | C-361 |
| 304 | 12 When the inner being goes wrong | The heart as the source | C-369 |
| 307 | 12 When the inner being goes wrong | Pride and the lifted-up heart and spirit | C-168, C-171, C-214 |
| 323 | 13.1 Divine | Choosing | C-176, C-332 |
| 324 | 13.1 Divine | Purposing | C-361, C-379, C-380 |
| 325 | 13.1 Divine | Willing | C-203, C-353, C-384 |
| 326 | 13.1 Divine | Delight | C-188, C-206, C-247 |
| 338 | 14 Made new | Revived, restored, renewed | C-150 |
| 348 | 02 Life, breath and death | Going down to Sheol | C-93, C-95, C-96 |
| 350 | 02 Life, breath and death | Dead to sin | C-150 |
| 351 | 02 Life, breath and death | Those left behind | C-155 |
| 352 | 10.14 Humility | (opening) | C-167, C-168 |
| 356 | 10.14 Humility | It answers a word heard | C-170 |
| 357 | 10.14 Humility | Where it happens | C-171 |
| 361 | 10.14 Humility | God sees it, and answers in measure | C-175 |
| 362 | 10.14 Humility | A humbling God does not take knowledge of | C-176 |
| 363 | 10.14 Humility | Being humbled by God | C-178 |
| 364 | 10.14 Humility | The proud brought low, the lowly raised | C-181, C-237, C-257 |
| 365 | 10.14 Humility | The humble | C-186 |
| 366 | 10.14 Humility | Humility as a way of walking | C-187, C-188 |
| 368 | 10.14 Humility | Toward one another | C-192 |
| 370 | 10.14 Humility | Jesus | C-197 |
| 371 | 10.14 Humility | The Old Testament and the New | C-200, C-202 |
| 372 | 10.14 Humility | When humility changes character | C-201 |
| 374 | 10.2 Knowing and hearing | Humility and hearing | C-187 |
| 376 | 10.9 Relating to God | Humbling oneself before God | C-170, C-175 |
| 377 | 10.10 Relating to others | Humility toward one another | C-192 |
| 378 | 04 The heart | The heart humbled | C-171, C-178 |
| 380 | 13.1 Divine | Lowering himself | C-202, C-203 |
| 381 | 10.15 Pride | (opening) | C-213 |
| 382 | 10.15 Pride | The words | C-223, C-243 |
| 383 | 10.15 Pride | Given, then held as one's own | C-214 |
| 384 | 10.15 Pride | The heart that says what God says | C-217, C-324 |
| 385 | 10.15 Pride | Pride and hearing | C-222, C-223 |
| 386 | 10.15 Pride | Pride over another | C-226 |
| 387 | 10.15 Pride | The boast | C-228, C-232, C-244 |
| 388 | 10.15 Pride | The mock | C-241 |
| 389 | 10.15 Pride | Where it ends | C-236, C-237 |
| 392 | 10.2 Knowing and hearing | Pride and hearing | C-222 |
| 393 | 10.7 Choosing and setting direction | Presumption | C-223, C-244 |
| 394 | 10.10 Relating to others | Pride over another | C-226, C-232 |
| 395 | 13.1 Divine | Majesty | C-214, C-217, C-236, C-241 |
| 401 | 02 Life, breath and death | Believed, questioned, denied | C-274 |
| 406 | 10.7 Choosing and setting direction | Dedicating | C-393 |

## 6. Phrases attached to the collection (15)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| be unaware | 10045 | the phrase be unaware is one concept, placed in know (step 4, by meaning) | 4 | 0 | 0 | 0 |
| can interpret | 10047 | the phrase can interpret is one concept, placed in know (step 4, by meaning) | 2 | 0 | 0 | 0 |
| can read | 10048 | the phrase can read is one concept, placed in know (step 4, by meaning) | 2 | 0 | 0 | 0 |
| fully knew | 7062 | english route: word knew | 1 | 0 | 0 | 0 |
| know her | 7444 | english route: word know | 2 | 0 | 0 | 0 |
| know how | 6022 | english route: word know | 5 | 0 | 0 | 0 |
| know then | 7445 | english route: word know | 1 | 0 | 1 | 1 |
| made known | 7613 | english route: word known | 18 | 0 | 0 | 0 |
| make known | 6075 | english route: word known | 11 | 0 | 2 | 1 |
| no knowledge | 7816 | english route: word knowledge | 1 | 0 | 0 | 0 |
| not know | 7822 | english route: word know | 2 | 0 | 0 | 0 |
| not knowing | 7823 | english route: word knowing | 1 | 0 | 1 | 1 |
| not recognize | 7832 | english route: word recognize | 2 | 0 | 0 | 0 |
| not recognized | 10046 | the phrase not recognized is one concept, placed in know (step 4, by meaning) | 1 | 0 | 0 | 0 |
| sound knowledge | 8252 | english route: word knowledge | 1 | 0 | 0 | 0 |

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
| live-node-with-no-verse-lexical-id | live ib_node in a verse of the report with a member surface but verse_lexical_id NULL (stored, tied to no occurrence) | 1 |

### live-node-with-no-verse-lexical-id: 1 found

| node | observation | verse | word |
|---|---|---|---|
| 32467 | 15151 | 1Cor 8:2 | know |

## 8. Sources

Occurrences: live verse_lexical rows, with the verse text from table `verse`; Strong's data from `strong`, `strong_sense`, `strong_meaning_tree`, `strong_related`, `cluster_strong`; observations and nodes from `ib_observation` and `ib_node` (an observation is withdrawn when deleted = 1); claims from `narrative_claim_source` (by observation_id or verse_id), `narrative_claim`, `narrative_claim_telling` and `narrative_section`. A table or column was used only after its recorded meaning in `cfg_table` and `cfg_column` was read (rule B:123).

