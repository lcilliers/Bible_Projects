# Collection evidence report: change

Generated 2026-11-13T19:02:01Z by run RUN-20261113_190156_110-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-change-v1-20261113.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection change at a glance

Status confirmed; core term 685; created 2026-11-08T12:19:27Z, updated 2026-11-10T16:03:37Z; run RUN-20261110_160337_351-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (31)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| alters | word | synonym | alter | placed | 2 | 1 |
| amend | word | synonym | amend | placed | 4 | 4 |
| became broader | phrase | phrase | became broader | placed | 1 | 1 |
| became detestable | phrase | phrase | became detestable | placed | 2 | 1 |
| became fat | phrase | phrase | became fat | placed | 1 | 1 |
| became fools | phrase | phrase | became fools | placed | 1 | 1 |
| became leader | phrase | phrase | became leader | placed | 2 | 1 |
| became numb | phrase | phrase | became numb | placed | 1 | 1 |
| became sick | phrase | phrase | became sick | placed | 1 | 1 |
| become anxious | phrase | phrase | become anxious | placed | 1 | 1 |
| become callous | phrase | phrase | become callous | placed | 1 | 1 |
| become desolate | phrase | phrase | become desolate | placed | 1 | 1 |
| become exhausted | phrase | phrase | become exhausted | placed | 1 | 1 |
| become fools | phrase | phrase | become fools | placed | 2 | 2 |
| become foul | phrase | phrase | become foul | placed | 1 | 1 |
| become gaunt | phrase | phrase | become gaunt | placed | 1 | 1 |
| become guilty | phrase | phrase | become guilty | placed | 3 | 2 |
| become merry | phrase | phrase | become merry | placed | 1 | 1 |
| become sick | phrase | phrase | become sick | placed | 2 | 1 |
| become slaves | phrase | phrase | become slaves | placed | 3 | 3 |
| becomes king | phrase | phrase | becomes king | placed | 2 | 1 |
| becoming conceited | phrase | phrase | becoming conceited | placed | 3 | 1 |
| change | word | core | change | placed | 20 | 18 |
| changed | word | synonym | change | placed | 32 | 29 |
| changes | word | synonym | change | placed | 8 | 8 |
| changing | word | synonym | change | placed | 1 | 1 |
| conformed | word | gathered | conform | placed | 3 | 3 |
| correct | word | synonym | correct | placed | 2 | 2 |
| correction | word | synonym | correct | placed | 6 | 6 |
| transform | word | synonym | transform | placed | 1 | 1 |
| transformed | word | synonym | transform | placed | 2 | 2 |

### 2.2 The Strong's codes behind the members (53)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H8133 שְׁנָא she.na "to change" | 10 | 3 | 13 | changed 7, change 3 | none | 5 |
| H2487 חֲלִיפָה cha.li.phah "change" | 8 | 0 | 7 | changes 6, change 2 | none | 0 |
| H2498 חָלַף cha.laph "to pass" | 6 | 0 | 6 | changed 4, change 2 | none | 0 |
| G0236 ἀλλάσσω allassō "to change" | 5 | 0 | 5 | changed 3, change 2 | none | 0 |
| H2015 הָפַךְ ha.phakh "to overturn" | 5 | 1 | 6 | changed 3, change 2 | none | 0 |
| H4171 מוּר mur "to change" | 5 | 0 | 5 | change 2, changed 2, changes 1 | none | 0 |
| H8138A שָׁנָה sha.nah "to change" | 5 | 0 | 5 | change 2, changed 2, changing 1 | none | 0 |
| H3190 יָטַב ya.tav "be good" | 4 | 0 | 4 | amend 4 | none | 0 |
| H4148G מוּסָר mu.sar "discipline" | 4 | 0 | 4 | correction 4 | none | 1 |
| H5437K סָבַב sa.vav "to turn: changed" | 4 | 0 | 4 | changed 3, change 1 | none | 0 |
| G1402 δουλόω douloō "to enslave" | 2 | 0 | 2 | become slaves 2 | none | 0 |
| G3339 μεταμορφόω metamorfoō "to transform" | 2 | 0 | 2 | transformed 2 | none | 2 |
| G4964 συσχηματίζω suschēmatizō "to conform to" | 2 | 0 | 2 | conformed 2 | none | 0 |
| H2973 יָאַל ya.al "be foolish" | 2 | 0 | 2 | become fools 2 | none | 0 |
| H8132 שָׁנָא sha.na "to change" | 2 | 0 | 2 | changed 2 | none | 0 |
| G0524 ἀπαλγέω apalgeō "to become callous" | 1 | 0 | 1 | become callous 1 | none | 0 |
| G1882 ἐπανόρθωσις epanorthōsis "correcting" | 1 | 0 | 1 | correction 1 | none | 0 |
| G3331 μετάθεσις metathesis "removal/change" | 1 | 0 | 1 | change 1 | none | 0 |
| G3345 μετασχηματίζω metaschēmatizō "to transform" | 1 | 0 | 1 | transform 1 | none | 1 |
| G3346 μετατίθημι metatithēmi "to transport" | 1 | 0 | 1 | change 1 | none | 0 |
| G3471 μωραίνω mōrainō "be foolish" | 1 | 0 | 1 | became fools 1 | none | 0 |
| G4832 σύμμορφος summorfos "conformed" | 1 | 0 | 1 | conformed 1 | none | 1 |
| G5157 τροπή tropē "turning" | 1 | 0 | 1 | change 1 | none | 0 |
| G5229 ὑπεραίρω huperairō "be haughty" | 1 | 1 | 1 | becoming conceited 1 | none | 2 |
| H0605 אָנַשׁ a.nash "be incurable" | 1 | 0 | 1 | became sick 1 | none | 0 |
| H0816 אָשַׁם a.sham "be guilty" | 1 | 1 | 2 | become guilty 1 | none | 0 |
| H0833 אָשַׁר a.shar "to bless" | 1 | 0 | 1 | correct 1 | none | 0 |
| H1672 דָּאַג da.ag "be anxious" | 1 | 0 | 1 | become anxious 1 | none | 0 |
| H2186B זָנַח za.nach "to stink" | 1 | 0 | 1 | become foul 1 | none | 0 |
| H3235 יָמַר ya.mar "to exchange" | 1 | 0 | 1 | changed 1 | none | 0 |
| H3256 יָסַר ya.sar "to discipline" | 1 | 0 | 1 | correct 1 | none | 0 |
| H3286 יָעֵף ya.eph "to faint" | 1 | 0 | 1 | become exhausted 1 | none | 0 |
| H3584 כָּחַשׁ ka.chash "to deceive" | 1 | 0 | 1 | become gaunt 1 | none | 1 |
| H5437G סָבַב sa.vav "to turn: turn" | 1 | 0 | 1 | changed 1 | none | 0 |
| H5647G עָבַד a.vad "to serve" | 1 | 0 | 1 | become slaves 1 | none | 0 |
| H5937 עָלַז a.laz "to exult" | 1 | 0 | 1 | become merry 1 | none | 0 |
| H6313 פּוּג pug "be numb" | 1 | 0 | 1 | became numb 1 | none | 1 |
| H7337 רָחַב ra.chav "to enlarge" | 1 | 0 | 1 | became broader 1 | none | 0 |
| H7626G שֵׁ֫בֶט she.vet "tribe: staff" | 1 | 0 | 1 | correction 1 | none | 0 |
| H8077A שְׁמָמָה she.ma.mah "devastation" | 1 | 0 | 1 | become desolate 1 | none | 0 |
| H8080 שָׁמֵן sha.men "to grow fat" | 1 | 0 | 1 | became fat 1 | none | 0 |
| G2532 καί kai "and" | 0 | 1 | 1 |  | none | 0 |
| H0408 אַל al "not" | 0 | 1 | 1 |  | none | 0 |
| H0409 אַל al "not" | 0 | 1 | 1 |  | none | 0 |
| H1739 דָּוֶה da.veh "sick" | 0 | 1 | 1 |  | none | 1 |
| H1768 דִּי di "that" | 0 | 1 | 1 |  | none | 0 |
| H1961 הָיָה ha.yah "to be" | 0 | 3 | 3 |  | none | 0 |
| H2009 הִנֵּה hin.neh "behold" | 0 | 1 | 1 |  | none | 0 |
| H3588A כִּי ki "for" | 0 | 1 | 1 |  | none | 0 |
| H3809 לָא la "not" | 0 | 1 | 1 |  | none | 0 |
| H4427A מָלַךְ ma.lakh "to reign" | 0 | 1 | 1 |  | none | 0 |
| H8251 שִׁקּוּץ shiq.quts "abomination" | 0 | 1 | 1 |  | none | 0 |
| H8269 שַׂר sar "ruler" | 0 | 1 | 1 |  | none | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.42.

### 3.1 H8133 שְׁנָא she.na "to change": 10 own occurrences in 10 verses

- **Meaning as stored:** Hebrew; native word שְׁנָא, transliteration she.na; STEP gloss "to change"; sense head "to change" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8133):** to change, be altered, be changed.
- **Related terms (2):** H8132 sha.na "to change"; H8140 she.nah "year".
- **Clusters (cluster_strong):** M45 Renewal & Transformation (None).
- **Counts, three measures as stored:** STEP token count 24; verses STEP attests 0; verse_lexical rows the parse found 21.

- **Carried by the member words:** changed (7), change (3).
- **Engagement of these occurrences:** none recorded 10.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 2:9 | change | AVPi3ms | none recorded | - | 0 | if you do not make the dream known to me, there is but one sentence for you. You have agreed to speak lying and corrupt words before me till the times **change**. Therefore tell me the dream, and I shall know that you can show me its interpretation.” |
| Dan 5:10 | change | AVPj3mp | none recorded | - | 0 | The queen, because of the words of the king and his lords, came into the banqueting hall, and the queen declared, “O king, live forever! Let not your thoughts alarm you or your color **change**. |
| Dan 7:25 | change | AVhcc | none recorded | - | 0 | He shall speak words against the Most High, and shall wear out the saints of the Most High, and shall think to **change** the times and the law; and they shall be given into his hand for a time, times, and half a time. |
| Dan 3:19 | changed | AVPp3ms | none recorded | 13118, 13395, 14196, 14395 | 0 | Then Nebuchadnezzar was filled with fury, and the expression of his face was **changed** against Shadrach, Meshach, and Abednego. He ordered the furnace heated seven times more than it was usually heated. |
| Dan 4:16 | changed | AVpi3mp | none recorded | 16458, 17246 | 0 | Let his mind be **changed** from a man’s, and let a beast’s mind be given to him; and let seven periods of time pass over him. |
| Dan 5:6 | changed | AVqp3mp | none recorded | 18905, 19239 | 0 | Then the king’s color **changed**, and his thoughts alarmed him; his limbs gave way, and his knees knocked together. |
| Dan 5:9 | changed | AVqrmpa | none recorded | 19239 | 0 | Then King Belshazzar was greatly alarmed, and his color **changed**, and his lords were perplexed. |
| Dan 6:8 | changed | AVhcc | none recorded | - | 0 | Now, O king, establish the injunction and sign the document, so that it cannot be **changed**, according to the law of the Medes and the Persians, which cannot be revoked.” |
| Dan 6:17 | changed | AVqi2ms | none recorded | - | 0 | And a stone was brought and laid on the mouth of the den, and the king sealed it with his own signet and with the signet of his lords, that nothing might be **changed** concerning Daniel. |
| Dan 7:28 | changed | AVPi3mp | none recorded | 16459, 16827, 20496 | 0 | “ Here is the end of the matter. As for me, Daniel, my thoughts greatly alarmed me, and my color **changed**, but I kept the matter in my heart.” |

### 3.2 H2487 חֲלִיפָה cha.li.phah "change": 8 own occurrences in 7 verses

- **Meaning as stored:** Hebrew; native word חֲלִיפָה, transliteration cha.li.phah; STEP gloss "change"; sense head "change" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2487):** a change, change (of garments), replacement.
- **Related terms (6):** H2475 cha.loph "destruction"; H2498 cha.laph "to pass"; H2500 che.leph "for"; H2501 che.leph "Heleph"; H4252 ma.cha.laph "knife"; H4253 ma.cha.la.phah "lock".
- **Clusters (cluster_strong):** T12 Objects-Artifacts (high).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 11; verse_lexical rows the parse found 12.

- **Carried by the member words:** changes (6), change (2).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 45:22 | change | HNcfpa | none recorded | - | 0 | To each and all of them he gave a **change** of clothes, but to Benjamin he gave three hundred shekels of silver and five changes of clothes. |
| Psa 55:19 | change | HNcfpa | none recorded | - | 0 | God will give ear and humble them, he who is enthroned from of old, Selah because they do not **change** and do not fear God. |
| Gen 45:22 | changes | HNcfpc | none recorded | - | 0 | To each and all of them he gave a change of clothes, but to Benjamin he gave three hundred shekels of silver and five **changes** of clothes. |
| Judg 14:12 | changes | HNcfpc | none recorded | - | 0 | And Samson said to them, “Let me now put a riddle to you. If you can tell me what it is, within the seven days of the feast, and find it out, then I will give you thirty linen garments and thirty **changes** of clothes, |
| Judg 14:13 | changes | HNcfpc | none recorded | - | 0 | but if you cannot tell me what it is, then you shall give me thirty linen garments and thirty **changes** of clothes.” And they said to him, “ Put your riddle, that we may hear it.” |
| 2Ki 5:5 | changes | HNcfpc | none recorded | - | 0 | And the king of Syria said, “ Go now, and I will send a letter to the king of Israel.” So he went, taking with him ten talents of silver, six thousand shekels of gold, and ten **changes** of clothing. |
| 2Ki 5:22 | changes | HNcfpa | none recorded | - | 0 | And he said, “All is well. My master has sent me to say, ‘ There have just now come to me from the hill country of Ephraim two young men of the sons of the prophets. Please give them a talent of silver and two **changes** of clothing.’” |
| 2Ki 5:23 | changes | HNcfpa | none recorded | - | 0 | And Naaman said, “Be pleased to accept two talents.” And he urged him and tied up two talents of silver in two bags, with two **changes** of clothing, and laid them on two of his servants. And they carried them before Gehazi. |

### 3.3 H2498 חָלַף cha.laph "to pass": 6 own occurrences in 6 verses

- **Meaning as stored:** Hebrew; native word חָלַף, transliteration cha.laph; STEP gloss "to pass"; sense head "to pass" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2498):** to pass on or away, pass through, pass by, go through, grow up, change ... (cut; the whole text is in the workbook).
- **Related terms (7):** H2475 cha.loph "destruction"; H2487 cha.li.phah "change"; H2499 cha.laph "to pass"; H2500 che.leph "for"; H2501 che.leph "Heleph"; H4252 ma.cha.laph "knife"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 28; verses STEP attests 27; verse_lexical rows the parse found 28.

- **Carried by the member words:** changed (4), change (2).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 35:2 | change | HVhv2mp | none recorded | - | 0 | So Jacob said to his household and to all who were with him, “Put away the foreign gods that are among you and purify yourselves and **change** your garments. |
| Psa 102:26 | change | HVhi2ms | none recorded | - | 0 | They will perish, but you will remain; they will all wear out like a garment. You will **change** them like a robe, and they will pass away, |
| Gen 31:7 | changed | HVhq3ms | none recorded | - | 0 | yet your father has cheated me and **changed** my wages ten times. But God did not permit him to harm me. |
| Gen 31:41 | changed | HVhw2ms | none recorded | - | 0 | These twenty years I have been in your house. I served you fourteen years for your two daughters, and six years for your flock, and you have **changed** my wages ten times. |
| Gen 41:14 | changed | HVpw3ms | none recorded | - | 0 | Then Pharaoh sent and called Joseph, and they quickly brought him out of the pit. And when he had shaved himself and **changed** his clothes, he came in before Pharaoh. |
| 2Sa 12:20 | changed | HVpw3ms | none recorded | - | 0 | Then David arose from the earth and washed and anointed himself and **changed** his clothes. And he went into the house of the Lord and worshiped. He then went to his own house. And when he asked, they set food before him, and he ate. |

### 3.4 G0236 ἀλλάσσω allassō "to change": 5 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word ἀλλάσσω, transliteration allassō; STEP gloss "to change"; sense head "to change" (the code is its own lemma).
- **Related terms (1):** G0243 allos "another".
- **Clusters (cluster_strong):** M45 Renewal & Transformation (None).
- **Counts, three measures as stored:** STEP token count 38; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** changed (3), change (2).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 6:14 | change | V-FAI-3S | none recorded | - | 0 | for we have heard him say that this Jesus of Nazareth will destroy this place and will **change** the customs that Moses delivered to us.” |
| Gal 4:20 | change | V-AAN | none recorded | - | 0 | I wish I could be present with you now and **change** my tone, for I am perplexed about you. |
| 1Cor 15:51 | changed | V-2FPI-1P | none recorded | - | 0 | Behold! I tell you a mystery. We shall not all sleep, but we shall all be **changed**, |
| 1Cor 15:52 | changed | V-2FPI-1P | none recorded | - | 0 | in a moment, in the twinkling of an eye, at the last trumpet. For the trumpet will sound, and the dead will be raised imperishable, and we shall be **changed**. |
| Heb 1:12 | changed | V-2FPI-3P | none recorded | - | 0 | like a robe you will roll them up, like a garment they will be **changed**. But you are the same, and your years will have no end.” |

### 3.5 H2015 הָפַךְ ha.phakh "to overturn": 5 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word הָפַךְ, transliteration ha.phakh; STEP gloss "to overturn"; sense head "to overturn" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2015):** to turn, overthrow, overturn.
- **Related terms (11):** H2016 he.phekh "contrariness"; H2017 ho.phekh "perversity"; H2018 ha.phe.khah "overthrow"; H2019 ha.phakh.pakh "crooked"; H2021 ho.tsen "weapon"; H2023G hor "[Mount] Hor"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 94; verses STEP attests 92; verse_lexical rows the parse found 94.

- **Carried by the member words:** changed (3), change (2).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 13:23 | change | HVqi3ms | none recorded | - | 0 | Can the Ethiopian **change** his skin or the leopard his spots? Then also you can do good who are accustomed to do evil. |
| Zep 3:9 | change | HVqi1cs | none recorded | - | 0 | “ For at that time I will **change** the speech of the peoples to a pure speech, that all of them may call upon the name of the Lord and serve him with one accord. |
| Exo 14:5 | changed | HVNw3ms | none recorded | - | 0 | When the king of Egypt was told that the people had fled, the mind of Pharaoh and his servants was **changed** toward the people, and they said, “ What is this we have done, that we have let Israel go from serving us?” |
| Job 38:14 | changed | HVti3fs | none recorded | - | 0 | It is **changed** like clay under the seal, and its features stand out like a garment. |
| Dan 10:8 | changed | HVNp3ms | none recorded | - | 0 | So I was left alone and saw this great vision, and no strength was left in me. My radiant appearance was fearfully **changed**, and I retained no strength. |

### 3.6 H4171 מוּר mur "to change": 5 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word מוּר, transliteration mur; STEP gloss "to change"; sense head "to change" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4171):** to change, exchange.
- **Related terms (4):** H4173 mo.rag "threshing sled"; H4177 mo.rah "razor"; H4185 mush "to remove"; H8545 te.mu.rah "exchange".
- **Clusters (cluster_strong):** M45 Renewal & Transformation (high).
- **Counts, three measures as stored:** STEP token count 14; verses STEP attests 10; verse_lexical rows the parse found 14.

- **Carried by the member words:** change (2), changed (2), changes (1).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 15:4 | change | HVhi3ms | none recorded | - | 0 | in whose eyes a vile person is despised, but who honors those who fear the Lord; who swears to his own hurt and does not **change**; |
| Hos 4:7 | change | HVhi1cs | none recorded | - | 0 | The more they increased, the more they sinned against me; I will **change** their glory into shame. |
| Jer 2:11 | changed | HVhp3ms | none recorded | - | 0 | Has a nation **changed** its gods, even though they are no gods? But my people have changed their glory for that which does not profit. |
| Jer 48:11 | changed | HVNp3ms | none recorded | - | 0 | “ Moab has been at ease from his youth and has settled on his dregs; he has not been emptied from vessel to vessel, nor has he gone into exile; so his taste remains in him, and his scent is not **changed**. |
| Mic 2:4 | changes | HVhi3ms | none recorded | - | 0 | In that day they shall take up a taunt song against you and moan bitterly, and say, “We are utterly ruined; he **changes** the portion of my people; how he removes it from me! To an apostate he allots our fields.” |

### 3.7 H8138A שָׁנָה sha.nah "to change": 5 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word שָׁנָה, transliteration sha.nah; STEP gloss "to change"; sense head "to change" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8138):** to repeat, do again.
- **Related terms (6):** H4932G mish.neh "Second [Quarter]"; H4932H mish.neh "second"; H8132 sha.na "to change"; H8138B sha.nah "to repeat"; H8141 sha.nah "year"; H8145 she.ni "second".
- **Clusters (cluster_strong):** M45 Renewal & Transformation (None).
- **Counts, three measures as stored:** STEP token count 14; verses STEP attests 0; verse_lexical rows the parse found 13.

- **Carried by the member words:** change (2), changed (2), changing (1).
- **Engagement of these occurrences:** none recorded 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 14:20 | change | HVprmsa | none recorded | - | 0 | You prevail forever against him, and he passes; you **change** his countenance, and send him away. |
| Mal 3:6 | change | HVqp1cs | none recorded | - | 0 | “For I the Lord do not **change**; therefore you, O children of Jacob, are not consumed. |
| 1Sa 21:13 | changed | HVpw3ms | none recorded | - | 0 | So he **changed** his behavior before them and pretended to be insane in their hands and made marks on the doors of the gate and let his spittle run down his beard. |
| Psa 34:1 | changed | HVpcc | none recorded | - | 0 | Of David, when he **changed** his behavior before Abimelech, so that he drove him out, and he went away. I will bless the Lord at all times; his praise shall continually be in my mouth. |
| Jer 2:36 | changing | HVpcc | none recorded | - | 0 | How much you go about, **changing** your way! You shall be put to shame by Egypt as you were put to shame by Assyria. |

### 3.8 H3190 יָטַב ya.tav "be good": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word יָטַב, transliteration ya.tav; STEP gloss "be good"; sense head "be good" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3190):** to be good, be pleasing, be well, be glad.
- **Related terms (7):** H2868 te.ev "be good"; H3191 ye.tav "be good"; H3192 yot.vah "Jotbah"; H3193 yot.va.tah "Jotbathah"; H4105G me.he.tav.el "Mehetabel"; H4105H me.he.tav.el "Mehetabel"; more in the workbook.
- **Clusters (cluster_strong):** M05 Kindness & Friendship (heuristic).
- **Counts, three measures as stored:** STEP token count 117; verses STEP attests 110; verse_lexical rows the parse found 117.

- **Carried by the member words:** amend (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 7:3 | amend | HVhv2mp | none recorded | - | 0 | Thus says the Lord of hosts, the God of Israel: **Amend** your ways and your deeds, and I will let you dwell in this place. |
| Jer 7:5 | amend | HVhi2mp | none recorded | - | 0 | “ For if you truly **amend** your ways and your deeds, if you truly execute justice one with another, |
| Jer 18:11 | amend | HVhv2mp | none recorded | - | 0 | Now, therefore, say to the men of Judah and the inhabitants of Jerusalem: ‘ Thus says the Lord, Behold, I am shaping disaster against you and devising a plan against you. Return, every one from his evil way, and **amend** your ways and your deeds.’ |
| Jer 35:15 | amend | HVhv2mp | none recorded | - | 0 | I have sent to you all my servants the prophets, sending them persistently, saying, ‘ Turn now every one of you from his evil way, and **amend** your deeds, and do not go after other gods to serve them, and then you shall dwell in the land that I gave to you and your fathers.’ But you did not incline your ear or listen to me. |

### 3.9 H4148G מוּסָר mu.sar "discipline": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word מוּסָר, transliteration mu.sar; STEP gloss "discipline"; sense head "discipline/punishment".
- **Senses (first level of the meaning tree of the lemma H4148):** discipline, chastening, correction.
- **Related terms (5):** H3250 yis.sor "faultfinder"; H3256 ya.sar "to discipline"; H4148H mu.sar "discipline: instruction"; H4148I mu.sar "discipline: bonds"; H4561 mo.sar "discipline".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (heuristic).
- **Counts, three measures as stored:** STEP token count 29; verses STEP attests 0; verse_lexical rows the parse found 29.

- **Carried by the member words:** correction (4).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 2:30 | correction | HNcmsa | none recorded | - | 0 | In vain have I struck your children; they took no **correction**; your own sword devoured your prophets like a ravening lion. |
| Jer 5:3 | correction | HNcmsa | none recorded | - | 0 | O Lord, do not your eyes look for truth? You have struck them down, but they felt no anguish; you have consumed them, but they refused to take **correction**. They have made their faces harder than rock; they have refused to repent. |
| Zep 3:2 | correction | HNcmsa | none recorded | - | 0 | She listens to no voice; she accepts no **correction**. She does not trust in the Lord; she does not draw near to her God. |
| Zep 3:7 | correction | HNcmsa | none recorded | 14662 | 0 | I said, ‘ Surely you will fear me; you will accept **correction**. Then your dwelling would not be cut off according to all that I have appointed against you.’ But all the more they were eager to make all their deeds corrupt. |

### 3.10 H5437K סָבַב sa.vav "to turn: changed": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word סָבַב, transliteration sa.vav; STEP gloss "to turn: changed"; sense head "changed".
- **Senses (first level of the meaning tree of the lemma H5437):** to turn, turn about or around or aside or back or towards, go about or ... (cut; the whole text is in the workbook).
- **Related terms (13):** H4036 ma.gor mis.sa.viv "`Terror on Every Side`"; H4141 mu.sav "surrounding"; H4524 me.sav "surrounds"; H5252 ne.sib.bah "turn"; H5437G sa.vav "to turn: turn"; H5437H sa.vav "to turn: surround"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 0; verse_lexical rows the parse found 4.

- **Carried by the member words:** changed (3), change (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Sa 14:20 | change | HVpcc | none recorded | - | 0 | In order to **change** the course of things your servant Joab did this. But my lord has wisdom like the wisdom of the angel of God to know all things that are on the earth.” |
| 2Ki 23:34 | changed | HVhw3ms | none recorded | - | 0 | And Pharaoh Neco made Eliakim the son of Josiah king in the place of Josiah his father, and **changed** his name to Jehoiakim. But he took Jehoahaz away, and he came to Egypt and died there. |
| 2Ki 24:17 | changed | HVhw3ms | none recorded | - | 0 | And the king of Babylon made Mattaniah, Jehoiachin’s uncle, king in his place, and **changed** his name to Zedekiah. |
| 2Ch 36:4 | changed | HVhw3ms | none recorded | - | 0 | And the king of Egypt made Eliakim his brother king over Judah and Jerusalem, and **changed** his name to Jehoiakim. But Neco took Jehoahaz his brother and carried him to Egypt. |

### 3.11 G1402 δουλόω douloō "to enslave": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word δουλόω, transliteration douloō; STEP gloss "to enslave"; sense head "to enslave" (the code is its own lemma).
- **Related terms (7):** G1396 doulagōgeō "to enslave"; G1397 douleia "slavery"; G1398 douleuō "be a slave"; G1399 doulē "female slave"; G1401 doulos "slave"; G2615 katadouloō "to enslave"; more in the workbook.
- **Clusters (cluster_strong):** M78 Slavery & Bondage (heuristic).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 8; verse_lexical rows the parse found 8.

- **Carried by the member words:** become slaves (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 6:18 | become slaves | V-API-2P | none recorded | - | 0 | and, having been set free from sin, have **become slaves** of righteousness. |
| Rom 6:22 | become slaves | V-APP-NPM | none recorded | - | 0 | But now that you have been set free from sin and have **become slaves** of God, the fruit you get leads to sanctification and its end, eternal life. |

### 3.12 G3339 μεταμορφόω metamorfoō "to transform": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word μεταμορφόω, transliteration metamorfoō; STEP gloss "to transform"; sense head "to transform" (the code is its own lemma).
- **Related terms (17):** G0276 ametathetos "unchangeable"; G3326 meta "with/after"; G3327 metabainō "to depart"; G3328 metaballō "to change mind"; G3329 metagō "to turn"; G3331 metathesis "removal/change"; more in the workbook.
- **Clusters (cluster_strong):** M45 Renewal & Transformation (None).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** transformed (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 12:2 | transformed | V-PPM-2P | none recorded | 18381, 18391, 20452 | 0 | Do not be conformed to this world, but be **transformed** by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect. |
| 2Cor 3:18 | transformed | V-PPI-1P | none recorded | 16301, 16457, 18381, 18391 | 0 | And we all, with unveiled face, beholding the glory of the Lord, are being **transformed** into the same image from one degree of glory to another. For this comes from the Lord who is the Spirit. |

### 3.13 G4964 συσχηματίζω suschēmatizō "to conform to": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word συσχηματίζω, transliteration suschēmatizō; STEP gloss "to conform to"; sense head "to conform to" (the code is its own lemma).
- **Related terms (2):** G4862 sun "with"; G4976 schēma "form".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** conformed (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 12:2 | conformed | V-PEM-2P | none recorded | - | 0 | Do not be **conformed** to this world, but be transformed by the renewal of your mind, that by testing you may discern what is the will of God, what is good and acceptable and perfect. |
| 1Pe 1:14 | conformed | V-PEP-NPM | none recorded | - | 0 | As obedient children, do not be **conformed** to the passions of your former ignorance, |

### 3.14 H2973 יָאַל ya.al "be foolish": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word יָאַל, transliteration ya.al; STEP gloss "be foolish"; sense head "be foolish" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2973):** to be foolish, become fools, act foolishly, show wicked folly.
- **Related terms (1):** H2974 ya.al "be willing".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (None).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** become fools (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 19:13 | become fools | HVNp3cp | none recorded | - | 0 | The princes of Zoan have **become fools**, and the princes of Memphis are deluded; those who are the cornerstones of her tribes have made Egypt stagger. |
| Jer 50:36 | become fools | HVNq3cp | none recorded | - | 0 | A sword against the diviners, that they may **become fools**! A sword against her warriors, that they may be destroyed! |

### 3.15 H8132 שָׁנָא sha.na "to change": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word שָׁנָא, transliteration sha.na; STEP gloss "to change"; sense head "to change" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8132):** to change, alter.
- **Related terms (4):** H8133 she.na "to change"; H8138A sha.nah "to change"; H8138B sha.nah "to repeat"; H8141 sha.nah "year".
- **Clusters (cluster_strong):** M45 Renewal & Transformation (None).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 0; verse_lexical rows the parse found 3.

- **Carried by the member words:** changed (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 8:1 | changed | HVPi3ms | none recorded | - | 0 | Who is like the wise? And who knows the interpretation of a thing? A man’s wisdom makes his face shine, and the hardness of his face is **changed**. |
| Lam 4:1 | changed | HVqi3ms | none recorded | - | 0 | How the gold has grown dim, how the pure gold is **changed**! The holy stones lie scattered at the head of every street. |

### 3.16 G0524 ἀπαλγέω apalgeō "to become callous": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀπαλγέω, transliteration apalgeō; STEP gloss "to become callous"; sense head "to become callous" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** M42 Prayer & Petition (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** become callous (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 4:19 | become callous | V-RAP-NPM | none recorded | - | 0 | They have **become callous** and have given themselves up to sensuality, greedy to practice every kind of impurity. |

### 3.17 G1882 ἐπανόρθωσις epanorthōsis "correcting": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐπανόρθωσις, transliteration epanorthōsis; STEP gloss "correcting"; sense head "correcting" (the code is its own lemma).
- **Related terms (2):** G0461 anorthoō "to restore"; G1909 epi "upon/to/against".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** correction (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ti 3:16 | correction | N-ASF | none recorded | - | 0 | All Scripture is breathed out by God and profitable for teaching, for reproof, for **correction**, and for training in righteousness, |

### 3.18 G3331 μετάθεσις metathesis "removal/change": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word μετάθεσις, transliteration metathesis; STEP gloss "removal/change"; sense head "removal/change" (the code is its own lemma).
- **Related terms (15):** G0276 ametathetos "unchangeable"; G3327 metabainō "to depart"; G3328 metaballō "to change mind"; G3329 metagō "to turn"; G3332 metairō "to leave"; G3334 metakineō "to shift"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 0; verse_lexical rows the parse found 3.

- **Carried by the member words:** change (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 7:12 | change | N-NSF | none recorded | - | 0 | For when there is a **change** in the priesthood, there is necessarily a change in the law as well. |

### 3.19 G3345 μετασχηματίζω metaschēmatizō "to transform": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word μετασχηματίζω, transliteration metaschēmatizō; STEP gloss "to transform"; sense head "to transform" (the code is its own lemma).
- **Related terms (17):** G0276 ametathetos "unchangeable"; G3326 meta "with/after"; G3327 metabainō "to depart"; G3328 metaballō "to change mind"; G3329 metagō "to turn"; G3331 metathesis "removal/change"; more in the workbook.
- **Clusters (cluster_strong):** M45 Renewal & Transformation (high).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** transform (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Phili 3:21 | transform | V-FAI-3S | none recorded | 15474, 17182, 18382, 18390, 18691 | 0 | who will **transform** our lowly body to be like his glorious body, by the power that enables him even to subject all things to himself. |

### 3.20 G3346 μετατίθημι metatithēmi "to transport": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word μετατίθημι, transliteration metatithēmi; STEP gloss "to transport"; sense head "to transport" (the code is its own lemma).
- **Related terms (17):** G0276 ametathetos "unchangeable"; G3326 meta "with/after"; G3327 metabainō "to depart"; G3328 metaballō "to change mind"; G3329 metagō "to turn"; G3331 metathesis "removal/change"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 5; verse_lexical rows the parse found 6.

- **Carried by the member words:** change (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Heb 7:12 | change | V-PPP-GSF | none recorded | - | 0 | For when there is a **change** in the priesthood, there is necessarily a change in the law as well. |

### 3.21 G3471 μωραίνω mōrainō "be foolish": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word μωραίνω, transliteration mōrainō; STEP gloss "be foolish"; sense head "be foolish" (the code is its own lemma).
- **Related terms (2):** G3471 mōrainō "be foolish"; G3474 mōros "foolish".
- **Clusters (cluster_strong):** M16 Wisdom & Folly (None).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** became fools (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 1:22 | became fools | V-API-3P | none recorded | - | 0 | Claiming to be wise, they **became fools**, |

### 3.22 G4832 σύμμορφος summorfos "conformed": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word σύμμορφος, transliteration summorfos; STEP gloss "conformed"; sense head "conformed" (the code is its own lemma).
- **Related terms (3):** G3444 morfē "form"; G4833 summorfoomai "to make like"; G4862 sun "with".
- **Clusters (cluster_strong):** M45 Renewal & Transformation (None).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 0; verse_lexical rows the parse found 2.

- **Carried by the member words:** conformed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 8:29 | conformed | A-APM | none recorded | 18390 | 0 | For those whom he foreknew he also predestined to be **conformed** to the image of his Son, in order that he might be the firstborn among many brothers. |

### 3.23 G5157 τροπή tropē "turning": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word τροπή, transliteration tropē; STEP gloss "turning"; sense head "turning" (the code is its own lemma).
- **Related terms (1):** G5158 tropos "way".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** change (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jam 1:17 | change | N-GSF | none recorded | - | 0 | Every good gift and every perfect gift is from above, coming down from the Father of lights, with whom there is no variation or shadow due to **change**. |

### 3.24 G5229 ὑπεραίρω huperairō "be haughty": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ὑπεραίρω, transliteration huperairō; STEP gloss "be haughty"; sense head "be haughty" (the code is its own lemma).
- **Related terms (2):** G0142 airō "to take up"; G5228 huper "above/for".
- **Clusters (cluster_strong):** M08 Pride & Arrogance (high).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 2; verse_lexical rows the parse found 3.

- **Carried by the member words:** becoming conceited (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Cor 12:7 | becoming conceited | V-PPS-1S | none recorded | 15155, 15306, 16702 | 0 | So to keep me from **becoming conceited** because of the surpassing greatness of the revelations, a thorn was given me in the flesh, a messenger of Satan to harass me, to keep me from becoming conceited. |

### 3.25 H0605 אָנַשׁ a.nash "be incurable": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אָנַשׁ, transliteration a.nash; STEP gloss "be incurable"; sense head "be incurable" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0605):** to be weak, sick, frail.
- **Related terms (1):** H0582 e.nosh "human".
- **Clusters (cluster_strong):** M73 Sickness & Weakness (heuristic).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** became sick (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Sa 12:15 | became sick | HVNw3ms | none recorded | - | 0 | Then Nathan went to his house. And the Lord afflicted the child that Uriah’s wife bore to David, and he **became sick**. |

### 3.26 H0816 אָשַׁם a.sham "be guilty": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אָשַׁם, transliteration a.sham; STEP gloss "be guilty"; sense head "be guilty" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0816):** to offend, be guilty, trespass; (TWOT) to be desolate, acknowledge offense.
- **Related terms (3):** H0817 a.sham "guilt [offering]"; H0818 a.shem "guilty"; H0819 ash.mah "guiltiness".
- **Clusters (cluster_strong):** M56 Sin & Guilt (heuristic).
- **Counts, three measures as stored:** STEP token count 35; verses STEP attests 32; verse_lexical rows the parse found 35.

- **Carried by the member words:** become guilty (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 22:4 | become guilty | HVqp2fs | none recorded | - | 0 | You have **become guilty** by the blood that you have shed, and defiled by the idols that you have made, and you have brought your days near, the appointed time of your years has come. Therefore I have made you a reproach to the nations, and a mockery to all the countries. |

### 3.27 H0833 אָשַׁר a.shar "to bless": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word אָשַׁר, transliteration a.shar; STEP gloss "to bless"; sense head "to bless" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0833):** to go straight, walk, go on, advance, make progress.
- **Related terms (12):** H0804G ash.shur "Assyria"; H0804H ash.shur "Asshur"; H0835 e.sher "blessed"; H0836 a.sher "Asher"; H0837 o.sher "happy"; H0838A a.shur "step"; more in the workbook.
- **Clusters (cluster_strong):** M80 Blessing (heuristic).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 15; verse_lexical rows the parse found 16.

- **Carried by the member words:** correct (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 1:17 | correct | HVpv2mp | none recorded | - | 0 | learn to do good; seek justice, **correct** oppression; bring justice to the fatherless, plead the widow’s cause. |

### 3.28 H1672 דָּאַג da.ag "be anxious": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word דָּאַג, transliteration da.ag; STEP gloss "be anxious"; sense head "be anxious" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1672):** to fear, be anxious, be concerned, be afraid, be careful.
- **Related terms (4):** H1673 do.eg "Doeg"; H1674 de.a.gah "anxiety"; H1709G dag "Fish [Gate]"; H1709H dag "fish".
- **Clusters (cluster_strong):** M20 Doubt & Discouragement (None).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 7; verse_lexical rows the parse found 7.

- **Carried by the member words:** become anxious (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 9:5 | become anxious | HVqq3ms | none recorded | - | 0 | When they came to the land of Zuph, Saul said to his servant who was with him, “ Come, let us go back, lest my father cease to care about the donkeys and **become anxious** about us.” |

### 3.29 H2186B זָנַח za.nach "to stink": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word זָנַח, transliteration za.nach; STEP gloss "to stink"; sense head "to stink" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2186):** to cast off, reject, spurn.
- **Related terms (3):** H2182G za.no.ach "Zanoah"; H2182H za.no.ach "Zanoah"; H2186A za.nach "to reject".
- **Clusters (cluster_strong):** M06 Malice & Enmity (high).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** become foul (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 19:6 | become foul | HVhq3cp | none recorded | - | 0 | and its canals will **become foul**, and the branches of Egypt’s Nile will diminish and dry up, reeds and rushes will rot away. |

### 3.30 H3235 יָמַר ya.mar "to exchange": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word יָמַר, transliteration ya.mar; STEP gloss "to exchange"; sense head "to exchange" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3235):** to exchange; (TWOT) to promise.
- **Related terms (1):** H3236 yim.rah "Imrah".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** changed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 2:11 | changed | HVhp3ms | none recorded | - | 0 | Has a nation **changed** its gods, even though they are no gods? But my people have changed their glory for that which does not profit. |

### 3.31 H3256 יָסַר ya.sar "to discipline": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word יָסַר, transliteration ya.sar; STEP gloss "to discipline"; sense head "to discipline" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3256):** to chasten, discipline, instruct, admonish.
- **Related terms (6):** H3250 yis.sor "faultfinder"; H4147 mo.ser "bond"; H4148G mu.sar "discipline"; H4148H mu.sar "discipline: instruction"; H4148I mu.sar "discipline: bonds"; H4561 mo.sar "discipline".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 43; verses STEP attests 0; verse_lexical rows the parse found 42.

- **Carried by the member words:** correct (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 10:24 | correct | HVpv2ms | none recorded | - | 0 | **Correct** me, O Lord, but in justice; not in your anger, lest you bring me to nothing. |

### 3.32 H3286 יָעֵף ya.eph "to faint": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word יָעֵף, transliteration ya.eph; STEP gloss "to faint"; sense head "to faint" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3286):** to be or grow weary, be fatigued, be faint.
- **Related terms (3):** H3287 ya.eph "weary"; H3288 ye.aph "weariness"; H8443 to.a.phah "peak".
- **Clusters (cluster_strong):** M24 Faintness & Despair (None).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 9; verse_lexical rows the parse found 9.

- **Carried by the member words:** become exhausted (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 51:64 | become exhausted | HVqq3cp | none recorded | - | 0 | and say, ‘ Thus shall Babylon sink, to rise no more, because of the disaster that I am bringing upon her, and they shall **become exhausted**.’” Thus far are the words of Jeremiah. |

### 3.33 H3584 כָּחַשׁ ka.chash "to deceive": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word כָּחַשׁ, transliteration ka.chash; STEP gloss "to deceive"; sense head "to deceive" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3584):** to deceive, lie, fail, grow lean, be disappointing, be untrue, be insu ... (cut; the whole text is in the workbook).
- **Related terms (2):** H3585 ka.chash "lie"; H3586 ke.chash "deceptive".
- **Clusters (cluster_strong):** M14 Deceit & Falsehood (high).
- **Counts, three measures as stored:** STEP token count 22; verses STEP attests 22; verse_lexical rows the parse found 22.

- **Carried by the member words:** become gaunt (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 109:24 | become gaunt | HVqp3ms | none recorded | 16493 | 0 | My knees are weak through fasting; my body has **become gaunt**, with no fat. |

### 3.34 H5437G סָבַב sa.vav "to turn: turn": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word סָבַב, transliteration sa.vav; STEP gloss "to turn: turn"; sense head "turn/bring around".
- **Senses (first level of the meaning tree of the lemma H5437):** to turn, turn about or around or aside or back or towards, go about or ... (cut; the whole text is in the workbook).
- **Related terms (13):** H4036 ma.gor mis.sa.viv "`Terror on Every Side`"; H4141 mu.sav "surrounding"; H4524 me.sav "surrounds"; H5252 ne.sib.bah "turn"; H5437H sa.vav "to turn: surround"; H5437I sa.vav "to turn: again"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 78; verses STEP attests 73; verse_lexical rows the parse found 78.

- **Carried by the member words:** changed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 32:38 | changed | HVHsfpa | none recorded | - | 0 | Nebo, and Baal-meon ( their names were **changed** ), and Sibmah. And they gave other names to the cities that they built. |

### 3.35 H5647G עָבַד a.vad "to serve": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָבַד, transliteration a.vad; STEP gloss "to serve"; sense head "serve[someone]".
- **Senses (first level of the meaning tree of the lemma H5647):** to work, serve.
- **Related terms (46):** H4566 ma.bad "work"; H5647H a.vad "to serve: minister"; H5647I a.vad "to serve: labour"; H5647J a.vad "to serve: burden"; H5648 a.vad "to make"; H5650 e.ved "servant/slave"; more in the workbook.
- **Clusters (cluster_strong):** M36 Worship & Service (None).
- **Counts, three measures as stored:** STEP token count 97; verses STEP attests 88; verse_lexical rows the parse found 97.

- **Carried by the member words:** become slaves (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 4:9 | become slaves | HVqi2mp | none recorded | - | 0 | Take courage, and be men, O Philistines, lest you **become slaves** to the Hebrews as they have been to you; be men and fight.” |

### 3.36 H5937 עָלַז a.laz "to exult": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָלַז, transliteration a.laz; STEP gloss "to exult"; sense head "to exult" (the code is its own lemma).
- **Related terms (3):** H5938 a.lez "exultant"; H5939 a.la.tah "darkness"; H5947 al.liz "jubilant".
- **Clusters (cluster_strong):** M04 Joy & Gladness (None).
- **Counts, three measures as stored:** STEP token count 19; verses STEP attests 16; verse_lexical rows the parse found 16.

- **Carried by the member words:** become merry (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 51:39 | become merry | HVqj3mp | none recorded | - | 0 | While they are inflamed I will prepare them a feast and make them drunk, that they may **become merry**, then sleep a perpetual sleep and not wake, declares the Lord. |

### 3.37 H6313 פּוּג pug "be numb": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word פּוּג, transliteration pug; STEP gloss "be numb"; sense head "be numb" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H6313):** to grow numb, be feeble, be benumbed.
- **Related terms (2):** H2014 ha.phu.gah "cessation"; H6314 pu.gat "cessation".
- **Clusters (cluster_strong):** M73 Sickness & Weakness (low).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** became numb (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 45:26 | became numb | HVqw3ms | none recorded | 15984, 16338 | 0 | And they told him, “ Joseph is still alive, and he is ruler over all the land of Egypt.” And his heart **became numb**, for he did not believe them. |

### 3.38 H7337 רָחַב ra.chav "to enlarge": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רָחַב, transliteration ra.chav; STEP gloss "to enlarge"; sense head "to enlarge" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7337):** to be or grow wide, be or grow large.
- **Related terms (18):** H4800 mer.chav "broad"; H7338 ra.chav "breadth"; H7339 re.chov "street/plaza"; H7340G re.chov "Rehob"; H7340H re.chov "Rehob"; H7340I re.chov "Rehob"; more in the workbook.
- **Clusters (cluster_strong):** M23 Strength & Courage (None).
- **Counts, three measures as stored:** STEP token count 25; verses STEP attests 25; verse_lexical rows the parse found 25.

- **Carried by the member words:** became broader (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 41:7 | became broader | HVqq3fs | none recorded | - | 0 | And it **became broader** as it wound upward to the side chambers, because the temple was enclosed upward all around the temple. Thus the temple had a broad area upward, and so one went up from the lowest story to the top story through the middle story. |

### 3.39 H7626G שֵׁ֫בֶט she.vet "tribe: staff": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שֵׁ֫בֶט, transliteration she.vet; STEP gloss "tribe: staff"; sense head "staff".
- **Senses (first level of the meaning tree of the lemma H7626):** rod, staff, branch, offshoot, club, sceptre, tribe.
- **Related terms (6):** H7625 she.vat "tribe"; H7626H she.vet "tribe"; H7626I she.vet "tribe: javelin"; H7626J she.vet "tribe: ruler"; H7627 she.vat "Shebat"; H8275 shar.vit "scepter".
- **Clusters (cluster_strong):** T12 Objects-Artifacts (high).
- **Counts, three measures as stored:** STEP token count 52; verses STEP attests 0; verse_lexical rows the parse found 50.

- **Carried by the member words:** correction (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 37:13 | correction | HNcmsa | none recorded | - | 0 | Whether for **correction** or for his land or for love, he causes it to happen. |

### 3.40 H8077A שְׁמָמָה she.ma.mah "devastation": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שְׁמָמָה, transliteration she.ma.mah; STEP gloss "devastation"; sense head "devastation" (the code is its own lemma).
- **Related terms (20):** H4923 me.sham.mah "devastation"; H8037G sham.ma "Shammah"; H8037H sham.ma "Shamma"; H8047G sham.mah "horror: destroyed"; H8047H sham.mah "horror: appalled"; H8048G sham.mah "Shammah"; more in the workbook.
- **Clusters (cluster_strong):** M55 Destruction & Ruin (heuristic).
- **Counts, three measures as stored:** STEP token count 57; verses STEP attests 52; verse_lexical rows the parse found 55.

- **Carried by the member words:** become desolate (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 23:29 | become desolate | HNcfsa | none recorded | - | 0 | I will not drive them out from before you in one year, lest the land **become desolate** and the wild beasts multiply against you. |

### 3.41 H8080 שָׁמֵן sha.men "to grow fat": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁמֵן, transliteration sha.men; STEP gloss "to grow fat"; sense head "to grow fat" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8080):** to be or become fat, grow fat.
- **Related terms (7):** H0820 ash.man.nim "strong"; H4924A sha.man "fat"; H4924B mish.man "fatness"; H4924C mash.man "fat piece"; H4925 mish.man.nah "Mishmannah"; H8081 she.men "oil"; more in the workbook.
- **Clusters (cluster_strong):** M46 Wealth & Riches (None).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 0; verse_lexical rows the parse found 5.

- **Carried by the member words:** became fat (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Neh 9:25 | became fat | HVhw3mp | none recorded | - | 0 | And they captured fortified cities and a rich land, and took possession of houses full of all good things, cisterns already hewn, vineyards, olive orchards and fruit trees in abundance. So they ate and were filled and **became fat** and delighted themselves in your great goodness. |

### 3.42 Occurrences where the member surface is shared with another code's unit (20)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| 2Cor 12:7 | becoming conceited | G2532 καί kai "and" | becoming conceited | content_part | 2 | none recorded | - | 0 | So to keep me from **becoming conceited** because of the surpassing greatness of the revelations, a thorn was given me in the flesh, a messenger of Satan to harass me, to keep me from becoming conceited. |
| 2Cor 12:7 | becoming conceited | G5229 ὑπεραίρω huperairō "be haughty" | becoming conceited | content_part | 2 | none recorded | 15155, 15306, 16702 | 0 | So to keep me from **becoming conceited** because of the surpassing greatness of the revelations, a thorn was given me in the flesh, a messenger of Satan to harass me, to keep me from becoming conceited. |
| Hos 4:15 | become guilty | H0408 אַל al "not" | become guilty | content_part | 2 | none recorded | - | 0 | Though you play the whore, O Israel, let not Judah **become guilty**. Enter not into Gilgal, nor go up to Beth-aven, and swear not, “As the Lord lives.” |
| Dan 5:10 | change | H0409 אַל al "not" | change | content_part | 3 | none recorded | - | 0 | The queen, because of the words of the king and his lords, came into the banqueting hall, and the queen declared, “O king, live forever! Let not your thoughts alarm you or your color **change**. |
| Hos 4:15 | become guilty | H0816 אָשַׁם a.sham "be guilty" | become guilty | content_part | 2 | none recorded | - | 0 | Though you play the whore, O Israel, let not Judah **become guilty**. Enter not into Gilgal, nor go up to Beth-aven, and swear not, “As the Lord lives.” |
| Lam 5:17 | become sick | H1739 דָּוֶה da.veh "sick" | become sick | content_part | 2 | none recorded | 16113, 17276 | 0 | For this our heart has **become sick**, for these things our eyes have grown dim, |
| Ezr 6:11 | alters | H1768 דִּי di "that" | alters | content_part | 2 | none recorded | - | 0 | Also I make a decree that if anyone **alters** this edict, a beam shall be pulled out of his house, and he shall be impaled on it, and his house shall be made a dunghill. |
| 1Ki 11:24 | became leader | H1961 הָיָה ha.yah "to be" | became leader | content_part | 2 | none recorded | - | 0 | And he gathered men about him and **became leader** of a marauding band, after the killing by David. And they went to Damascus and lived there and made him king in Damascus. |
| Lam 5:17 | become sick | H1961 הָיָה ha.yah "to be" | become sick | content_part | 2 | none recorded | - | 0 | For this our heart has **become sick**, for these things our eyes have grown dim, |
| Hos 9:10 | became detestable | H1961 הָיָה ha.yah "to be" | became detestable | content_part | 2 | none recorded | - | 0 | Like grapes in the wilderness, I found Israel. Like the first fruit on the fig tree in its first season, I saw your fathers. But they came to Baal-peor and consecrated themselves to the thing of shame, and **became detestable** like the thing they loved. |
| Lev 13:55 | changed | H2009 הִנֵּה hin.neh "behold" | changed | content_part | 3 | none recorded | - | 0 | And the priest shall examine the diseased thing after it has been washed. And if the appearance of the diseased area has not **changed**, though the disease has not spread, it is unclean. You shall burn it in the fire, whether the rot is on the back or on the front. |
| Lev 13:55 | changed | H2015 הָפַךְ ha.phakh "to overturn" | changed | content_part | 3 | none recorded | - | 0 | And the priest shall examine the diseased thing after it has been washed. And if the appearance of the diseased area has not **changed**, though the disease has not spread, it is unclean. You shall burn it in the fire, whether the rot is on the back or on the front. |
| Pro 30:22 | becomes king | H3588A כִּי ki "for" | becomes king | content_part | 2 | none recorded | - | 0 | a slave when he **becomes king**, and a fool when he is filled with food; |
| Dan 6:15 | changed | H3809 לָא la "not" | changed | content_part | 3 | none recorded | - | 0 | Then these men came by agreement to the king and said to the king, “ Know, O king, that it is a law of the Medes and Persians that no injunction or ordinance that the king establishes can be **changed**.” |
| Pro 30:22 | becomes king | H4427A מָלַךְ ma.lakh "to reign" | becomes king | content_part | 2 | none recorded | - | 0 | a slave when he **becomes king**, and a fool when he is filled with food; |
| Ezr 6:11 | alters | H8133 שְׁנָא she.na "to change" | alters | content_part | 2 | none recorded | - | 0 | Also I make a decree that if anyone **alters** this edict, a beam shall be pulled out of his house, and he shall be impaled on it, and his house shall be made a dunghill. |
| Dan 2:21 | changes | H8133 שְׁנָא she.na "to change" | changes | content_part | 3 | none recorded | - | 0 | He **changes** times and seasons; he removes kings and sets up kings; he gives wisdom to the wise and knowledge to those who have understanding; |
| Dan 6:15 | changed | H8133 שְׁנָא she.na "to change" | changed | content_part | 3 | none recorded | - | 0 | Then these men came by agreement to the king and said to the king, “ Know, O king, that it is a law of the Medes and Persians that no injunction or ordinance that the king establishes can be **changed**.” |
| Hos 9:10 | became detestable | H8251 שִׁקּוּץ shiq.quts "abomination" | became detestable | content_part | 2 | none recorded | - | 0 | Like grapes in the wilderness, I found Israel. Like the first fruit on the fig tree in its first season, I saw your fathers. But they came to Baal-peor and consecrated themselves to the thing of shame, and **became detestable** like the thing they loved. |
| 1Ki 11:24 | became leader | H8269 שַׂר sar "ruler" | became leader | content_part | 2 | none recorded | - | 0 | And he gathered men about him and **became leader** of a marauding band, after the killing by David. And they went to Damascus and lived there and made him king in Damascus. |

## 4. What the study has recorded for these occurrences

Of 112 occurrences, 0 have an engagement observation and 112 have none recorded. There are 30 live observations on them (0 engagement, 30 of other recorded stages, 0 of the retired catalogue stages) and 2 withdrawn.

### 4.1 Engagement: what each word does for the inner being (0 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

_no engagement observation covers these occurrences_

### 4.2 Other recorded observations (30)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 13118** (prior-capture, tag link, status draft): Sequence in Dan 3:12–28: refusal reported → furious rage → questioned → "but if not … we will not serve" → face changed, furnace heated → deliverance → the king blesses the refusal.
  - applies to 1 occurrence(s): Dan 3:19 (changed)
- **Observation 13395** (prior-capture, tag link, status draft): refused → enraged, burned within (Est 1:12); filled with fury → face changed → furnace heated (Dan 3:19).
  - applies to 1 occurrence(s): Dan 3:19 (changed)
- **Observation 14196** (prior-capture, tag statement, status draft): Part 2 verses: what they add. The four strands hold, and each gains an instance: Strand (a), a demand no one can meet, with the angry one now the demander. "There is not a man on earth who can meet the king's demand … no one can show it to the king except the gods, whose dwelling is not with flesh" (Dan 2:10–11). Then "Because of this the king was angry and very furious, and commanded that all the wise men of Babylon be destroyed" (2:12). This is the mirror of Gen 30:2. Jacob, faced with an impossible demand, named God as the only one who could meet it. Nebuchadnezzar hears the same answer ("except the gods") and orders a massacre; The anger is answered by "prudence and discretion" (Dan 2:14 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Dan 3:19 (changed)
- **Observation 14395** (prior-capture, tag statement, status draft): (v2) Dan 3:12–28: Sequence the text gives: refusal reported → furious rage → questioned → "but if not … we will not serve" → face changed, furnace heated → deliverance → the king blesses the refusal.
  - applies to 1 occurrence(s): Dan 3:19 (changed)
- **Observation 14662** (prior-capture, tag statement, status draft): Part C: Zep 3:8; Zec 7:12; Mal 1:4: Correction refused: "I said, 'Surely you will fear me; you will accept correction' … But all the more they were eager to make all their deeds corrupt" (Zep 3:7). The next verse (3:8) is wrath on the nations, followed by "a pure speech, that all of them may call upon the name of the Lord" (3:9); The heart made hard against hearing: "they refused to pay attention and turned a stubborn shoulder and stopped their ears … They made their hearts diamond-hard lest they should hear the law … Therefore great anger came" (Zec 7:11–12); Refusal returned in kind: "As I called, and they would not hear, so they called, and I would not hear" (7:13); Rebuilding against the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Zep 3:7 (correction)
- **Observation 15155** (prior-capture, tag statement, status draft): A thorn given: "to keep me from becoming conceited because of the surpassing greatness of the revelations, a thorn was given me in the flesh, a messenger of Satan to harass me" (2Co 12:7). The answer was "My grace is sufficient for you, for my power is made perfect in weakness" (12:9); What was given (the revelations) could have become conceit. A second thing was given to keep it from doing so. The verse names "a messenger of Satan" in it. I read: this is held for 13.3.
  - applies to 1 occurrence(s): 2Cor 12:7 (becoming conceited)
- **Observation 15306** (prior-capture, tag statement, status draft): This line runs through every batch: "Hear and give ear; be not proud, for the Lord has spoken" (Jer 13:15); "if you will not listen, my soul will weep in secret for your pride" (13:17); "By insolence comes nothing but strife, but with those who take advice is wisdom" (Pro 13:10); The scoffer: "does not listen to rebuke" (Pro 13:1); "does not like to be reproved; he will not go to the wise" (15:12); "Do not reprove a scoffer, or he will hate you" (9:8); "do not scoff ... Give ear, and hear my voice" (Isa 28:22–23); Presumption acts on its own word:; the prophet "who presumes to speak a word in my name that I have not commanded him" (Deu 18:20); "you would not listen; but you rebelled ... and ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Cor 12:7 (becoming conceited)
- **Observation 15474** (prior-capture, tag statement, status draft): Phili 3:21, "who will transform our lowly body to be like his glorious body". It is already OT-05 item 9 (the body raised), with G3345 and G4832. Decision: thread.
  - applies to 1 occurrence(s): Phili 3:21 (transform)
- **Observation 15984** (prior-capture, tag statement, status draft): Revival: "when they told him all the words of Joseph … the spirit of their father Jacob revived" (Gen 45:27) — one verse after "his heart became numb, for he did not believe them" (Gen 45:26).; Revisit 2026-09-28 (context Gen 45:25–28, Batch G §2): the revival comes when the words are joined by sight: "and when he saw the wagons that Joseph had sent". Then: "It is enough; Joseph my son is still alive. I will go and see him before I die" (28).; [Claude reading] Hearing alone numbs the heart. Hearing with seeing revives the spirit. This qualifies §9.5 below ("hearing is the main channel"). Here hearing needed a second channel.
  - applies to 1 occurrence(s): Gen 45:26 (became numb)
- **Observation 16113** (prior-capture, tag statement, status draft): 8.1 The sick heart: "Hope deferred makes the heart sick, but a desire fulfilled is a tree of life" (Pro 13:12) — sickness and life in one line; "for this our heart has become sick, for these things our eyes have grown dim" (Lam 5:17); "The whole head is sick, and the whole heart faint" (Isa 1:5); "The heart is deceitful above all things, and desperately sick" (Jer 17:9); "How sick is your heart … because you did all these things, the deeds of a brazen prostitute" (Eze 16:30) [lexical: "weak / languishing"; [verify]]; "Reproaches have broken my heart, so that I am in despair [*sick*]" (Psa 69:20); "A tranquil heart gives life to the flesh, but envy makes the bones rot" (Pro 14:30) — M25 pair; ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Lam 5:17 (become sick)
- **Observation 16301** (prior-capture, tag statement, status draft): 3.3 Glory, the Spirit and the heart (NT); exaltation: "the Spirit of glory and of God rests upon you" (1Pe 4:14) [D1]; "we all … are being transformed … from one degree of glory to another. For this comes from the Lord who is the Spirit" (2Co 3:18); "God … has shone in our hearts to give the light of the knowledge of the glory of God" (2Co 4:6); "that according to the riches of his glory he may grant you to be strengthened with power through his Spirit in your inner being" (Eph 3:16) [D1]; "full of the Holy Spirit, gazed into heaven and saw the glory of God" (Act 7:55); "the Spirit lifted me up … the glory of the Lord filled the temple" (Eze 43:5; 3:12) [D2]
  - applies to 1 occurrence(s): 2Cor 3:18 (transformed)
- **Observation 16338** (prior-capture, tag statement, status draft): The heart that cannot believe: "his heart became numb, for he did not believe them" (Gen 45:26) — shock blocks belief; "when he speaks graciously, believe him not, for there are seven abominations in his heart" (Pro 26:25).
  - applies to 1 occurrence(s): Gen 45:26 (became numb)
- **Observation 16457** (prior-capture, tag statement, status draft): 11.2 New heart, new spirit — renewal of the inner seat (M45): "Create in me a clean heart, O God, and renew a right spirit within me" (Psa 51:10) [H1]; "be renewed in the spirit of your minds" (Eph 4:23) [H1]; "Though our outer self is wasting away, our inner self is being renewed day by day" (2Co 4:16) — the explicit inner / outer self; "being transformed … For this comes from the Lord who is the Spirit" (2Co 3:18); "the washing of regeneration and renewal of the Holy Spirit" (Tit 3:5); "When you send forth your Spirit, they are created, and you renew the face of the ground" (Psa 104:30) [D1]; "a new covenant … of the Spirit" (2Co 3:6); "a new name" (Rev 2:17)
  - applies to 1 occurrence(s): 2Cor 3:18 (transformed)
- **Observation 16458** (prior-capture, tag statement, status draft): The heart changed for the worse: "Let his mind [*heart*] be changed from a man's, and let a beast's mind be given to him" (Dan 4:16). Transformation of the heart downward.
  - applies to 1 occurrence(s): Dan 4:16 (changed)
- **Observation 16459** (prior-capture, tag statement, status draft): 11.2 New heart, new spirit — renewal of the inner seat (M45): "my color changed, but I kept the matter in my heart" (Dan 7:28); [Claude reading] Renewal is predicated of heart and spirit together (Eze 11:19; 18:31; 36:26; Psa 51:10). Eze 18:31 makes it the person's task and Eze 36:26 makes it God's gift. Batch C §8.3 already noted the heart / spirit / flesh triad in these verses.
  - applies to 1 occurrence(s): Dan 7:28 (changed)
- **Observation 16493** (prior-capture, tag statement, status draft): 0. Data notes: "Holy" inside "Holy Spirit" (M61) — pre-filter.; 93 pairs in 92 verses are G0040G / H6944G "holy" at d1 from *pneuma / rûaḥ*. In these, M61 is carried by the name of the Spirit, not by a statement about purity.; They are not dropped. They are summarised as a group in §7.1 for what they say about the Spirit and the inner seat.; The other 90 M61 verses are read in §7.2–7.5.; The other pre-filters do not apply here. Neither "declares the Lord" (M42) nor "Lord of hosts" (M72) falls in Batch D clusters.; "Arise" (H6965B) accounts for 30 of the 101 M08 verses. None is about pride. They are noted and not used in §9. → Ruling R1.; "Brothers" (G0080) accounts for 32 of the 126 M14 vers ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 109:24 (become gaunt)
- **Observation 16702** (prior-capture, tag statement, status draft): The thorn in the flesh against conceit: "to keep me from becoming conceited … a thorn was given me in the flesh, a messenger of Satan to harass me" (2Co 12:7).
  - applies to 1 occurrence(s): 2Cor 12:7 (becoming conceited)
- **Observation 16827** (prior-capture, tag statement, status draft): 5.3 Keeping something in the heart — holding what is not yet understood: Daniel: "my thoughts greatly alarmed me, and my color changed, but I kept the matter in my heart" (Dan 7:28) → Batch B; Batch G; Mary: after the shepherds: "treasured up all these things, pondering them in her heart" (Luk 2:19); after the temple, where "they did not understand the saying" (2:50): "his mother treasured up all these things in her heart" (2:51); "keep them within your heart" (Pro 4:21); [Claude reading] "Keeping in the heart" follows alarm (Daniel) or incomprehension (Mary, 2:50). The heart holds what the mind cannot yet resolve. In both cases the keeping is the end of the scene: nothing is said or done ye ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Dan 7:28 (changed)
- **Observation 17182** (prior-capture, tag statement, status draft): The glorified body is in the verses, but none of them carries an M47 word: who will transform our lowly body to be like his glorious body (Php 3:21); it is sown in dishonor, raised in glory, raised a spiritual body (1 Cor 15:43-44); this perishable body must put on the imperishable (15:53); a building from God, a house not made with hands (2 Cor 5:1-4). They are told in Ch 2 as death and resurrection, not as the body.
  - applies to 1 occurrence(s): Phili 3:21 (transform)
- **Observation 17246** (prior-capture, tag statement, status draft): n. Heart and "mind": *ESV renders lēv as "mind":* 1Ki 3:9, 12; 4:29; 10:24; Pro 19:21; 28:26; Jer 14:14; 23:16; Lam 3:21; Neh 4:6; 6:8; 2Ki 6:11.; *Aramaic lēvav (H3825) is mostly "mind":* Dan 2:30; 4:16; 5:21; 7:4.; *Pairs in the text:* "test the heart and the mind" (Jer 11:20; 17:10; 20:12; Psa 26:2; 7:9; Rev 2:23); "hearts and … minds" (Phili 4:7); law "into their minds … on their hearts" / "on their hearts … on their minds" (Heb 8:10 / 10:16).; [lexical; verify] In several "heart and mind" pairs, the ESV "heart" may translate *kilyah* (kidneys) or the reverse. The CSV tags only the M47 word, so which English word carries the M47 tag varies (e.g. Jer 11:20, where the M47 tag sits on "mind ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Dan 4:16 (changed)
- **Observation 17276** (prior-capture, tag statement, status draft): 3.6 Cause and effect between inner seat, body and senses: *Heart → spirit:* "by sorrow of heart the spirit is crushed" (Pro 15:13).; *Heart / spirit → body, face, bones:*; "A glad heart makes a cheerful face" (Pro 15:13); "A tranquil heart gives life to the flesh, but envy makes the bones rot" (Pro 14:30); "A joyful heart is good medicine, but a crushed spirit dries up the bones" (Pro 17:22); "a trembling heart and failing eyes and a languishing soul" (Deu 28:65); "My heart throbs; my strength fails me, and the light of my eyes — it also has gone" (Psa 38:10); "Every heart will melt, and all hands will be feeble; every spirit will faint, and all knees will be weak as water" (Eze 21:7); "Hear ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Lam 5:17 (become sick)
- **Observation 18381** (prior-capture, tag statement, status draft): G3339 *metamorphoō* ("transform") | Jesus "transfigured", his face shining (Mat 17:2; Mar 9:2) · "be transformed by the renewal of your mind" (Rom 12:2) · "being transformed into the same image from one degree of glory to another" (2Cor 3:18) | Of Christ's body on the mountain, seen; of the mind, now, by renewal; of "we all", now and in degrees.
  - applies to 2 occurrence(s): Rom 12:2 (transformed), 2Cor 3:18 (transformed)
- **Observation 18382** (prior-capture, tag statement, status draft): G3345 *metaschēmatizō* ("change form") | "transform our lowly body to be like his glorious body" (Php 3:21) · Satan and his servants "disguise" themselves (2Cor 11:13–15) · Paul has "applied" these things to himself and Apollos (1Cor 4:6) | Christ's change of the body is real. The false change is a disguise. Once, the word is only a figure of speech.
  - applies to 1 occurrence(s): Phili 3:21 (transform)
- **Observation 18390** (prior-capture, tag statement, status draft): Like his body. "our citizenship is in heaven, and from it we await a Savior … who will transform our lowly body to be like his glorious body, by the power that enables him even to subject all things to himself." "predestined to be conformed to the image of his Son". "what we will be has not yet appeared; but we know that when he appears we shall be like him, because we shall see him as he is."
  - applies to 2 occurrence(s): Rom 8:29 (conformed), Phili 3:21 (transform)
- **Observation 18391** (prior-capture, tag statement, status draft): Already now, in the inner being. "born again to a living hope through the resurrection of Jesus Christ" (1Pe 1:3); "that I may know him and the power of his resurrection" (Php 3:10); the mind "transformed" (Rom 12:2); "being transformed … from one degree of glory to another" (2Cor 3:18).
  - applies to 2 occurrence(s): Rom 12:2 (transformed), 2Cor 3:18 (transformed)
- **Observation 18691** (prior-capture, tag statement, status draft): G3345 | *metaschēmatizō*, transform | M45 | 5 | the word in Php 3:21 (OT-05.9); G3339 is a different word
  - applies to 1 occurrence(s): Phili 3:21 (transform)
- **Observation 18905** (prior-capture, tag statement, status draft): What carries it instead of a seat: the question spoken aloud: "What does this mean?" (Act 2:12); "who is this about whom I hear such things?" (Luk 9:9, context); the gaze: "The disciples looked at one another" (Joh 13:22); a reflexive pronoun: Act 10:17 "inwardly perplexed" is *en heautō*, "in himself". The inner location is there, but through a pronoun, not a seat word.; the body of the other party: in Dan 5:6 the king's "color changed … his limbs gave way, and his knees knocked together". The body tells the alarm while his lords are perplexed.
  - applies to 1 occurrence(s): Dan 5:6 (changed)
- **Observation 19239** (prior-capture, tag statement, status draft): How it co-exists.; Herod: "Herod feared John, knowing that he was a righteous and holy man … When he heard him, he was greatly perplexed, and yet he heard him gladly" (Mar 6:20). Fear, knowledge, perplexity and gladness are all present in one man towards one prophet, and the perplexity keeps him listening.; Amazement: "all were amazed and perplexed" (Act 2:12).; The body of another man: Belshazzar's "color changed … his limbs gave way, and his knees knocked together" (Dan 5:6) while his lords were perplexed (5:9).; Anguish of love: "I am perplexed about you" (Gal 4:20), after "my little children, for whom I am again in the anguish of childbirth" (4:19).; A limit held: "perplexed, but not dri ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Dan 5:6 (changed), Dan 5:9 (changed)
- **Observation 20452** (prior-capture, tag statement, status draft): Where they seem to agree (Claude's reading, worth testing).: Thought isn't simply self-authored.; Science: most processing is automatic and unconscious. Predictive-processing models describe the brain as constantly generating expectations before we are aware of them.; Philosophy: phenomenology observes that thoughts arrive rather than being made.; Bible: the heart runs deeper than we can see into. Jeremiah 17:9–10 says the heart is beyond knowing except by God, and in Psalm 139:23 the psalmist asks God to "know my thoughts."; Thought is shaped by what it takes in and dwells on.; Science: neuroplasticity. Repeated patterns strengthen connections.; Philosophy: Vygotsky's view that language and ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Rom 12:2 (transformed)
- **Observation 20496** (prior-capture, tag statement, status draft): 4. From thought into the body.: "his thoughts alarmed him; his limbs gave way, and his knees knocked together" (Dan 5:6); "my color changed" (Dan 7:28)
  - applies to 1 occurrence(s): Dan 7:28 (changed)

### 4.3 The retired catalogue observations (0, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

_no rows_

### 4.4 Withdrawn observations (2)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 2 |

| reason as stored | observations |
|---|---|
| no change record | 2 |

## 5. Claims and the narrative

11 claims rest on these occurrences: 0 on an observation of these words and 11 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (0)

_none_

### 5.2 Claims reached by a verse only (11)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| 9-7 | Rom 1:21–32 as a five-step descent | Rom 1:21–32 | became fools G3471 | held | not told in a section |
| C-189 | Where God and a broken heart meet he is near and heals; the verses tell the breaking by its cause and by whether it is brought to God, not by naming contrition or despair | Psa 109:24 | become gaunt H3584 | current | chapter 04 The heart, The heart is the source; chapter 06 The spirit, The human spirit; chapter 10.2 Knowing and hearing, (opening); chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 14 Made new, Revived, restored, renewed; chapter 10.14 Humility, A lowly and contrite spirit; chapter 04 The heart, The heart humbled (9 earlier telling(s) in the workbook) |
| C-224 | God works to keep pride from a person: by warnings that open the ear, and by a thorn given against conceit | 2 Corinthians 12:7-9 | becoming conceited G2532; becoming conceited G5229 | current | chapter 10.2 Knowing and hearing, (opening); chapter 10.15 Pride, Pride and hearing (2 earlier telling(s) in the workbook) |
| C-230 | Boasting in weakness claims no more than is so, and makes room for Christ's power | 2 Corinthians 12:5-10 | becoming conceited G2532; becoming conceited G5229 | current | chapter 10.15 Pride, The boast (1 earlier telling(s) in the workbook) |
| C-268 | 'Poor and needy', said of oneself, comes with the stricken heart and the gaunt body and ends in an appeal for help | Psa 109:24 | become gaunt H3584 | current | chapter 04 The heart, The heart humbled (1 earlier telling(s) in the workbook) |
| C-270 | The hope Scripture gives against death includes the body | Phili 3:21 | transform G3345 | current | chapter 02 Life, breath and death, The body raised (1 earlier telling(s) in the workbook) |
| C-279 | 'Imperishable' is said of the raised body and also of what is within or held for a person: love, the seed of new birth, the beauty of a gentle spirit, an inheritance | 1Cor 15:52 | changed G0236 | current | chapter 02 Life, breath and death, Changed; chapter 11 Other sides of the inner being, 4. One word, opposite values (2 earlier telling(s) in the workbook) |
| C-287 | One Hebrew root, chul, is labour pain, trembling, anguish of heart, the dance, the whirling storm and patient waiting | Jer 5:3 | correction H4148G | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 10.12 Fear, Fear in the body (2 earlier telling(s) in the workbook) |
| C-327 | Glorying in shame does the boast's work turned upside down; against it stand the citizenship in heaven and the glorious body to come | Php 3:21 | transform G3345 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 10.15 Pride, The boast (2 earlier telling(s) in the workbook) |
| C-375 | God's devising against a people answers what they devise, and is spoken so that they may turn; he relents. | Jer 18:11 | amend H3190 | current | chapter 13.1 Divine, Purposing; chapter 10.4 Thinking, When thinking changes character |
| C-387 | Giving oneself or one's goods can be turned to an idol, even in the Lord's name; a person becomes like what he gives himself to and loves, and separating from God is done with idols taken into the heart. | Hos 9:10 | became detestable H1961; became detestable H8251 | current | chapter 12 When the inner being goes wrong, Idols taken inside; chapter 10.7 Choosing and setting direction, Dedicating |

### 5.3 The narrative sections that tell these claims (16)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 23 | 02 Life, breath and death | The body raised | C-270 |
| 26 | 02 Life, breath and death | Changed | C-279 |
| 46 | 04 The heart | The heart is the source | C-189 |
| 64 | 06 The spirit | The human spirit | C-189 |
| 122 | 10.2 Knowing and hearing | (opening) | C-189, C-224 |
| 138 | 10.4 Thinking | When thinking changes character | C-375 |
| 296 | 11 Other sides of the inner being | 4. One word, opposite values | C-189, C-279, C-287, C-327 |
| 313 | 12 When the inner being goes wrong | Idols taken inside | C-387 |
| 324 | 13.1 Divine | Purposing | C-375 |
| 338 | 14 Made new | Revived, restored, renewed | C-189 |
| 367 | 10.14 Humility | A lowly and contrite spirit | C-189 |
| 378 | 04 The heart | The heart humbled | C-189, C-268 |
| 385 | 10.15 Pride | Pride and hearing | C-224 |
| 387 | 10.15 Pride | The boast | C-230, C-327 |
| 403 | 10.12 Fear | Fear in the body | C-287 |
| 406 | 10.7 Choosing and setting direction | Dedicating | C-387 |

## 6. Phrases attached to the collection (20)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| became broader | 6327 | english route: word became | 1 | 0 | 0 | 0 |
| became detestable | 6329 | english route: word became | 2 | 0 | 0 | 0 |
| became fat | 6334 | english route: word became | 1 | 0 | 0 | 0 |
| became fools | 6339 | english route: word became | 1 | 0 | 0 | 0 |
| became leader | 6341 | english route: word became | 2 | 0 | 0 | 0 |
| became numb | 6343 | english route: word became | 1 | 0 | 2 | 2 |
| became sick | 6354 | english route: word became | 1 | 0 | 0 | 0 |
| become anxious | 6367 | english route: word become | 1 | 0 | 0 | 0 |
| become callous | 6369 | english route: word become | 1 | 0 | 0 | 0 |
| become desolate | 6383 | english route: word become | 1 | 0 | 0 | 0 |
| become exhausted | 6388 | english route: word become | 1 | 0 | 0 | 0 |
| become fools | 6390 | english route: word become | 2 | 0 | 0 | 0 |
| become foul | 6392 | english route: word become | 1 | 0 | 0 | 0 |
| become gaunt | 6394 | english route: word become | 1 | 0 | 1 | 1 |
| become guilty | 6396 | english route: word become | 3 | 0 | 0 | 0 |
| become merry | 6398 | english route: word become | 1 | 0 | 0 | 0 |
| become sick | 6406 | english route: word become | 2 | 0 | 2 | 2 |
| become slaves | 5890 | english route: word become | 3 | 0 | 0 | 0 |
| becomes king | 6423 | english route: word becomes | 2 | 0 | 0 | 0 |
| becoming conceited | 6433 | english route: word becoming | 3 | 0 | 6 | 3 |

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

