# Collection evidence report: search

Generated 2026-11-11T14:25:19Z by run RUN-20261111_142513_879-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-search-v7-20261111.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection search at a glance

Status confirmed; core term 882; created 2026-11-09T05:56:12Z, updated 2026-11-10T16:04:55Z; run RUN-20261110_160454_921-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (31)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| come upon | phrase | phrase | come upon | placed | 11 | 9 |
| earnestly seeks | phrase | phrase | earnestly seeks | placed | 1 | 1 |
| find | word | synonym | find | placed | 169 | 146 |
| find compassion | phrase | phrase | find compassion | placed | 1 | 1 |
| finds | word | synonym | find | listed_only | 37 | 29 |
| insist on | phrase | phrase | insist on | placed | 1 | 1 |
| look for | phrase | phrase | look for | placed | 5 | 5 |
| looking for | phrase | phrase | looking for | placed | 3 | 3 |
| more handsome | phrase | phrase | more handsome | placed | 1 | 1 |
| search | word | core | search | placed | 40 | 36 |
| search for | phrase | phrase | search for | placed | 1 | 1 |
| searched | word | core/synonym | search | placed | 13 | 12 |
| searched for | phrase | phrase | searched for | placed | 1 | 1 |
| searches | word | core/synonym | search | placed | 9 | 8 |
| searching | word | core/synonym | search | placed | 4 | 3 |
| searching for | phrase | phrase | searching for | placed | 1 | 1 |
| seek | word | synonym | seek | placed | 228 | 205 |
| seek after | phrase | phrase | seek after | placed | 1 | 1 |
| seek for | phrase | phrase | seek for | placed | 1 | 1 |
| seek me diligently | phrase | phrase | seek me diligently | placed | 2 | 2 |
| seek out | phrase | phrase | seek out | placed | 3 | 3 |
| seek shelter | phrase | phrase | seek shelter | placed | 1 | 1 |
| seeking | word | synonym | seek | placed | 61 | 58 |
| seeks | word | synonym | seek | listed_only | 32 | 29 |
| seeks for | phrase | phrase | seeks for | placed | 3 | 3 |
| seeks out | phrase | phrase | seeks out | placed | 2 | 2 |
| sought | word | synonym | seek | listed_only | 92 | 82 |
| sought for | phrase | phrase | sought for | placed | 1 | 1 |
| sought out | phrase | phrase | sought out | placed | 3 | 3 |
| sought refuge | phrase | phrase | sought refuge | placed | 1 | 1 |
| well disposed | phrase | phrase | well disposed | placed | 1 | 1 |

### 2.2 The Strong's codes behind the members (72)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H1245 בָּקַשׁ ba.qash "to seek" | 190 | 8 | 188 | seek 108, sought 41, seeks 19, seeking 10, search 4, searched 2, sought out 2, find 1, seek out 1, seeks out 1, sought for 1 | face 147, silence 27, use 24 | 58 |
| H4672 מָצָא ma.tsa "to find" | 110 | 4 | 110 | find 91, finds 15, seeking 2, come upon 1, seek 1 | face 3, silence 82, use 29 | 0 |
| G2212 ζητέω zēteō "to seek" | 104 | 0 | 101 | seek 40, seeking 35, sought 11, seeks 7, search 3, looking for 2, insist on 1, look for 1, searched 1, searching 1, searching for 1, seek for 1 | face 90, silence 6, use 8 | 18 |
| H1875 דָּרַשׁ da.rash "to seek" | 83 | 2 | 82 | seek 49, sought 14, search 4, seeking 4, seeks 4, searches 3, searched 2, search for 1, seek out 1, sought out 1 | face 71, silence 6, use 8 | 30 |
| G2147 εὑρίσκω heuriskō "to find/meet" | 59 | 0 | 57 | find 48, finds 11 | silence 50, use 9 | 1 |
| G1934 ἐπιζητέω epizēteō "to seek after" | 14 | 0 | 13 | seek 6, seeking 2, seeks for 2, searched for 1, seek after 1, seeks 1, sought 1 | face 13, use 1 | 3 |
| H7836 שָׁחַר sha.char "to seek" | 11 | 0 | 11 | seek 5, seek me diligently 2, earnestly seeks 1, seeking 1, seeks 1, sought 1 | face 9, silence 1, use 1 | 2 |
| H2664 חָפַשׂ cha.pha.s "to search" | 10 | 0 | 10 | search 7, searched 2, searching 1 | face 2, silence 5, use 3 | 0 |
| H2713 חָקַר cha.qar "to search" | 8 | 2 | 10 | search 6, searched 1, sought 1 | face 2, silence 5, use 3 | 0 |
| H7912 שְׁכַח she.khach "to find" | 6 | 0 | 4 | find 6 | silence 6 | 0 |
| G1567 ἐκζητέω ekzēteō "to seek out" | 5 | 0 | 5 | seek 2, searched 1, seeks for 1, sought 1 | face 5 | 0 |
| G2045 ἐρευνάω ereunaō "to look for/into" | 5 | 0 | 5 | searches 3, search 2 | silence 1, use 4 | 0 |
| H1240 בְּקַר be.qar "to enquire" | 4 | 0 | 4 | search 4 | silence 4 | 0 |
| G4328 προσδοκάω prosdokaō "to look for" | 3 | 0 | 3 | look for 3 | face 3 | 0 |
| H0935G בּוֹא bo "to come [in]: come" | 3 | 0 | 3 | come upon 3 | silence 1, use 2 | 0 |
| H1156 בְּעָא be.a "to ask" | 3 | 1 | 4 | sought 2, seek 1 | face 2, silence 1, use 1 | 1 |
| H2470B חָלָה cha.lah "to beg" | 3 | 0 | 3 | seek 2, sought 1 | face 3 | 1 |
| H2896A טוֹב tov "pleasant" | 3 | 0 | 3 | more handsome 1, searches 1, well disposed 1 | face 1, silence 1, use 1 | 0 |
| H8446 תּוּר tur "to spy" | 3 | 0 | 3 | search 2, searched 1 | face 3 | 0 |
| G0327 ἀναζητέω anazēteō "to search" | 2 | 0 | 2 | look for 1, search 1 | silence 1, use 1 | 0 |
| H1239 בָּקַר ba.qar "to enquire" | 2 | 0 | 2 | seek 1, seek out 1 | face 1, silence 1 | 0 |
| H7122I קָרָא qa.ra "to encounter: chanced" | 2 | 0 | 2 | come upon 2 | silence 2 | 1 |
| G1377 διώκω diōkō "to pursue" | 1 | 0 | 1 | seek 1 | face 1 | 0 |
| G1722 ἐν en "in/on/among" | 1 | 1 | 2 | come upon 1 | silence 2 | 0 |
| G1833 ἐξετάζω exetazō "to find out" | 1 | 0 | 1 | search 1 | use 1 | 0 |
| G2021 ἐπιχειρέω epicheireō "to attempt" | 1 | 0 | 1 | seeking 1 | face 1 | 0 |
| G2186 ἐφίστημι efistēmi "to approach" | 1 | 0 | 1 | come upon 1 | silence 1 | 0 |
| G2614 καταδιώκω katadiōkō "to seek" | 1 | 0 | 1 | searched 1 | silence 1 | 0 |
| G4327 προσδέχομαι prosdechomai "to wait for/welcome" | 1 | 0 | 1 | looking for 1 | face 1 | 0 |
| H1158 בָּעָה ba.ah "to enquire" | 1 | 0 | 1 | sought 1 | silence 1 | 0 |
| H1243 בַּקָּרָה baq.qa.rah "seeking" | 1 | 0 | 1 | seeks out 1 | face 1 | 0 |
| H1980H הָלַךְ ha.lakh "to go: come" | 1 | 0 | 1 | sought 1 | face 1 | 0 |
| H2620 חָסָה cha.sah "to seek refuge" | 1 | 0 | 1 | seek shelter 1 | face 1 | 0 |
| H2658 חָפַר cha.phar "to search" | 1 | 0 | 1 | search 1 | silence 1 | 0 |
| H2665 חֵ֫פֶשׂ che.phe.s "plot" | 1 | 0 | 1 | search 1 | face 1 | 0 |
| H2714 חֵ֫קֶר che.qer "search" | 1 | 0 | 1 | seek 1 | face 1 | 0 |
| H5183A נַ֫חַת na.chat "quietness" | 1 | 0 | 1 | finds 1 | use 1 | 0 |
| H5810 עָזַז a.zaz "be strong" | 1 | 0 | 1 | sought refuge 1 | face 1 | 1 |
| H5927G עָלָה a.lah "to ascend: rise" | 1 | 1 | 2 | come upon 1 | silence 2 | 0 |
| H6440L פָּנֶה pa.neh "face of" | 1 | 0 | 1 | sought 1 | face 1 | 0 |
| H6485I פָּקַד pa.qad "to reckon: visit" | 1 | 0 | 1 | sought 1 | face 1 | 0 |
| H7200K רָאָה ra.ah "to see: enjoy" | 1 | 1 | 2 | find 1 | use 2 | 0 |
| H7304 רָוַח ra.vach "be wide" | 1 | 0 | 1 | find 1 | use 1 | 0 |
| H7356B רַחֲמִים ra.cha.mim "compassion" | 1 | 0 | 1 | find compassion 1 | use 1 | 1 |
| H7592 שָׁאַל sha.al "to ask" | 1 | 0 | 1 | seek 1 | silence 1 | 0 |
| H0369 אַ֫יִן a.yin "nothing" | 0 | 2 | 2 |  | silence 1, use 1 | 0 |
| H0413 אֶל el "to[wards]" | 0 | 1 | 1 |  | silence 1 | 0 |
| H0595 אָֽנֹכִ֫י a.no.khi "I" | 0 | 1 | 1 |  | silence 1 | 0 |
| H0834A אֲשֶׁר a.sher "which" | 0 | 7 | 7 |  | face 1, silence 5, use 1 | 0 |
| H0853 אֵת et "[Obj.]" | 0 | 3 | 3 |  | face 2, use 1 | 0 |
| H0859A אַתָּ֫ה at.tah "you [m.s.]" | 0 | 2 | 2 |  | face 1, silence 1 | 0 |
| H1082 בָּלַג ba.lag "be cheerful" | 0 | 1 | 1 |  | use 1 | 1 |
| H1931 הוּא hu "he/she/it" | 0 | 2 | 2 |  | silence 1, use 1 | 0 |
| H1934 הֲוָא ha.va "to be" | 0 | 1 | 1 |  | face 1 | 0 |
| H1961 הָיָה ha.yah "to be" | 0 | 5 | 5 |  | face 3, silence 1, use 1 | 0 |
| H1992 הֵ֫מָּה hem.mah "they [masc.]" | 0 | 1 | 1 |  | silence 1 | 0 |
| H2088 זֶה zeh "this" | 0 | 2 | 2 |  | face 1, silence 1 | 0 |
| H3588A כִּי ki "for" | 0 | 5 | 5 |  | face 1, silence 3, use 1 | 0 |
| H3605 כֹּל kol "all" | 0 | 1 | 1 |  | silence 1 | 0 |
| H3808 לֹא lo "not" | 0 | 5 | 5 |  | face 1, silence 3, use 1 | 0 |
| H4325G מַי may "water" | 0 | 1 | 1 |  | silence 1 | 0 |
| H4392 מָלֵא ma.le "full" | 0 | 1 | 1 |  | silence 1 | 0 |
| H4480A מִן־ min- "from" | 0 | 2 | 2 |  | silence 1, use 1 | 0 |
| H4680 מָצָה ma.tsah "to drain" | 0 | 1 | 1 |  | silence 1 | 0 |
| H4994 נָא na "please" | 0 | 1 | 1 |  | silence 1 | 0 |
| H5315I נֶ֫פֶשׁ ne.phesh "soul: myself" | 0 | 1 | 1 |  | use 1 | 1 |
| H5668 עָבוּר a.vur "for the sake of" | 0 | 1 | 1 |  | silence 1 | 0 |
| H5704 עַד ad "till" | 0 | 2 | 2 |  | face 1, silence 1 | 0 |
| H5750 עוֹד od "still" | 0 | 2 | 2 |  | face 1, use 1 | 0 |
| H5921A עַל al "upon" | 0 | 1 | 1 |  | use 1 | 0 |
| H5973A עִם im "with" | 0 | 1 | 1 |  | face 1 | 0 |
| H8033G שָׁם sham "there" | 0 | 1 | 1 |  | use 1 | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.46.

### 3.1 H1245 בָּקַשׁ ba.qash "to seek": 190 own occurrences in 180 verses

- **Meaning as stored:** Hebrew; native word בָּקַשׁ, transliteration ba.qash; STEP gloss "to seek"; sense head "to seek" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1245):** to seek, require, desire, exact, request.
- **Related terms (2):** H1246 baq.qa.shah "request"; H1248 bar "son".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 225; verses STEP attests 215; verse_lexical rows the parse found 225.

- **Carried by the member words:** seek (108), sought (41), seeks (19), seeking (10), search (4), searched (2), sought out (2), find (1), seek out (1), seeks out (1), sought for (1).
- **Engagement of these occurrences:** face 144, silence 23, use 23.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 8:17 | find | HVpcc | silence | - | 2 | then I saw all the work of God, that man cannot **find** out the work that is done under the sun. However much man may toil in seeking, he will not find it out. Even though a wise man claims to know, he cannot find it out. |
| 2Sa 5:17 | search | HVpcc | use | - | 3 | When the Philistines heard that David had been anointed king over Israel, all the Philistines went up to **search** for David. But David heard of it and went down to the stronghold. |
| 1Ch 14:8 | search | HVpcc | use | - | 3 | When the Philistines heard that David had been anointed king over all Israel, all the Philistines went up to **search** for David. But David heard of it and went out against them. |
| Jer 5:1 | search | HVpv2mp | silence | - | 2 | Run to and fro through the streets of Jerusalem, look and take note! **Search** her squares to see if you can find a man, one who does justice and seeks truth, that I may pardon her. |
| Lam 1:11 | search | HVprmpa | silence | - | 0 | All her people groan as they **search** for bread; they trade their treasures for food to revive their strength. “ Look, O Lord, and see, for I am despised.” |
| Jos 2:22 | searched | HVpw3mp | silence | - | 2 | They departed and went into the hills and remained there three days until the pursuers returned, and the pursuers **searched** all along the way and found nothing. |
| 2Ch 22:9 | searched | HVpw3ms | use | - | 3 | He **searched** for Ahaziah, and he was captured while hiding in Samaria, and he was brought to Jehu and put to death. They buried him, for they said, “He is the grandson of Jehoshaphat, who sought the Lord with all his heart.” And the house of Ahaziah had no one able to rule the kingdom. |
| Lev 19:31 | seek | HVpj2mp | face | - | 3 | “Do not turn to mediums or necromancers; do not **seek** them out, and so make yourselves unclean by them: I am the Lord your God. |
| Num 16:10 | seek | HVpq2mp | face | 19038, 19621, 19642, 19940 | 3 | and that he has brought you near him, and all your brothers the sons of Levi with you? And would you **seek** the priesthood also? |
| Num 35:23 | seek | HVprmsa | face | - | 3 | or used a stone that could cause death, and without seeing him dropped it on him, so that he died, though he was not his enemy and did not **seek** his harm, |
| Deu 4:29 | seek | HVpq2mp | face | - | 3 | But from there you will **seek** the Lord your God and you will find him, if you search after him with all your heart and with all your soul. |
| Rut 3:1 | seek | HVpi1cs | face | - | 3 | Then Naomi her mother-in-law said to her, “My daughter, should I not **seek** rest for you, that it may be well with you? |
| 1Sa 10:2 | seek | HVpcc | silence | - | 3 | When you depart from me today, you will meet two men by Rachel’s tomb in the territory of Benjamin at Zelzah, and they will say to you, ‘The donkeys that you went to **seek** are found, and now your father has ceased to care about the donkeys and is anxious about you, saying, “ What shall I do about my son?”’ |
| 1Sa 10:14 | seek | HVpcc | silence | - | 1 | Saul’s uncle said to him and to his servant, “ Where did you go?” And he said, “ To **seek** the donkeys. And when we saw they were not to be found, we went to Samuel.” |
| 1Sa 23:15 | seek | HVpcc | face | 16995 | 3 | David saw that Saul had come out to **seek** his life. David was in the wilderness of Ziph at Horesh. |
| 1Sa 23:25 | seek | HVpcc | use | - | 3 | And Saul and his men went to **seek** him. And David was told, so he went down to the rock and lived in the wilderness of Maon. And when Saul heard that, he pursued after David in the wilderness of Maon. |
| 1Sa 24:2 | seek | HVpcc | use | - | 3 | Then Saul took three thousand chosen men out of all Israel and went to **seek** David and his men in front of the Wildgoats ’ Rocks. |
| 1Sa 25:26 | seek | HVprmpa | face | - | 3 | Now then, my lord, as the Lord lives, and as your soul lives, because the Lord has restrained you from bloodguilt and from saving with your own hand, now then let your enemies and those who **seek** to do evil to my lord be as Nabal. |
| 1Sa 25:29 | seek | HVpcc | face | - | 3 | If men rise up to pursue you and to **seek** your life, the life of my lord shall be bound in the bundle of the living in the care of the Lord your God. And the lives of your enemies he shall sling out as from the hollow of a sling. |
| 1Sa 26:2 | seek | HVpcc | use | - | 3 | So Saul arose and went down to the wilderness of Ziph with three thousand chosen men of Israel to **seek** David in the wilderness of Ziph. |
| 1Sa 26:20 | seek | HVpcc | use | - | 3 | Now therefore, let not my blood fall to the earth away from the presence of the Lord, for the king of Israel has come out to **seek** a single flea like one who hunts a partridge in the mountains.” |
| 1Sa 28:7 | seek | HVpv2mp | silence | - | 3 | Then Saul said to his servants, “**Seek** out for me a woman who is a medium, that I may go to her and inquire of her.” And his servants said to him, “ Behold, there is a medium at En-dor.” |
| 2Sa 17:3 | seek | HVprmsa | face | - | 3 | and I will bring all the people back to you as a bride comes home to her husband. You **seek** the life of only one man, and all the people will be at peace.” |
| 2Sa 20:19 | seek | HVprmsa | face | - | 3 | I am one of those who are peaceable and faithful in Israel. You **seek** to destroy a city that is a mother in Israel. Why will you swallow up the heritage of the Lord?” |
| 1Ki 2:40 | seek | HVpcc | silence | - | 3 | Shimei arose and saddled a donkey and went to Gath to Achish to **seek** his servants. Shimei went and brought his servants from Gath. |
| 1Ki 18:10 | seek | HVpcc | use | - | 3 | As the Lord your God lives, there is no nation or kingdom where my lord has not sent to **seek** you. And when they would say, ‘He is not here,’ he would take an oath of the kingdom or nation, that they had not found you. |
| 1Ki 19:10 | seek | HVpw3mp | face | 16774, 16995, 17029 | 3 | He said, “I have been very jealous for the Lord, the God of hosts. For the people of Israel have forsaken your covenant, thrown down your altars, and killed your prophets with the sword, and I, even I only, am left, and they **seek** my life, to take it away.” |
| 1Ki 19:14 | seek | HVpw3mp | face | 16774, 16995, 17029 | 3 | He said, “I have been very jealous for the Lord, the God of hosts. For the people of Israel have forsaken your covenant, thrown down your altars, and killed your prophets with the sword, and I, even I only, am left, and they **seek** my life, to take it away.” |
| 2Ki 2:16 | seek | HVpu3mp | silence | 17130 | 3 | And they said to him, “ Behold now, there are with your servants fifty strong men. Please let them go and **seek** your master. It may be that the Spirit of the Lord has caught him up and cast him upon some mountain or into some valley.” And he said, “You shall not send.” |
| 2Ki 6:19 | seek | HVpi2mp | silence | - | 3 | And Elisha said to them, “ This is not the way, and this is not the city. Follow me, and I will bring you to the man whom you **seek**.” And he led them to Samaria. |
| 1Ch 4:39 | seek | HVpcc | silence | - | 3 | They journeyed to the entrance of Gedor, to the east side of the valley, to **seek** pasture for their flocks, |
| 1Ch 16:10 | seek | HVprmpc | face | 15195, 16654, 17109 | 3 | Glory in his holy name; let the hearts of those who **seek** the Lord rejoice! |
| 1Ch 16:11 | seek | HVpv2mp | face | - | 0 | **Seek** the Lord and his strength; seek his presence continually! |
| 2Ch 7:14 | seek | HVpu3mp | face | 15336 | 3 | if my people who are called by my name humble themselves, and pray and **seek** my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land. |
| 2Ch 11:16 | seek | HVpcc | face | 17107 | 3 | And those who had set their hearts to **seek** the Lord God of Israel came after them from all the tribes of Israel to Jerusalem to sacrifice to the Lord, the God of their fathers. |
| 2Ch 20:4 | seek | HVpcc | face | - | 0 | And Judah assembled to **seek** help from the Lord; from all the cities of Judah they came to seek the Lord. |
| 2Ch 20:4 | seek | HVpcc | face | - | 0 | And Judah assembled to **seek** help from the Lord; from all the cities of Judah they came to seek the Lord. |
| Ezr 8:21 | seek | HVpcc | face | 14595, 15336 | 3 | Then I proclaimed a fast there, at the river Ahava, that we might humble ourselves before our God, to **seek** from him a safe journey for ourselves, our children, and all our goods. |
| Ezr 8:22 | seek | HVprmpc | face | 14594, 15337, 19162 | 2 | For I was ashamed to ask the king for a band of soldiers and horsemen to protect us against the enemy on our way, since we had told the king, “The hand of our God is for good on all who **seek** him, and the power of his wrath is against all who forsake him.” |
| Neh 2:10 | seek | HVpcc | face | - | 3 | But when Sanballat the Horonite and Tobiah the Ammonite servant heard this, it displeased them greatly that someone had come to **seek** the welfare of the people of Israel. |
| Job 10:6 | seek | HVpi2ms | use | - | 2 | that you **seek** out my iniquity and search for my sin, |
| Psa 4:2 | seek | HVpi2mp | face | - | 3 | O men, how long shall my honor be turned into shame? How long will you love vain words and **seek** after lies? Selah |
| Psa 24:6 | seek | HVprmpc | face | - | 2 | Such is the generation of those who **seek** him, who seek the face of the God of Jacob. Selah |
| Psa 27:4 | seek | HVpi1cs | face | 17979 | 3 | One thing have I asked of the Lord, that will I **seek** after: that I may dwell in the house of the Lord all the days of my life, to gaze upon the beauty of the Lord and to inquire in his temple. |
| Psa 27:8 | seek | HVpv2mp | face | - | 0 | You have said, “ **Seek** my face.” My heart says to you, “Your face, Lord, do I seek.” |
| Psa 27:8 | seek | HVpi1cs | face | - | 0 | You have said, “ **Seek** my face.” My heart says to you, “Your face, Lord, do I seek.” |
| Psa 34:14 | seek | HVpv2ms | face | 17872 | 3 | Turn away from evil and do good; **seek** peace and pursue it. |
| Psa 35:4 | seek | HVprmpc | face | 16995, 17056 | 3 | Let them be put to shame and dishonor who **seek** after my life! Let them be turned back and disappointed who devise evil against me! |
| Psa 38:12 | seek | HVprmpc | face | 16982, 16995 | 4 | Those who **seek** my life lay their snares; those who seek my hurt speak of ruin and meditate treachery all day long. |
| Psa 40:14 | seek | HVprmpc | face | 16995 | 2 | Let those be put to shame and disappointed altogether who **seek** to snatch away my life; let those be turned back and brought to dishonor who delight in my hurt! |
| Psa 40:16 | seek | HVprmpc | face | - | 3 | But may all who **seek** you rejoice and be glad in you; may those who love your salvation say continually, “ Great is the Lord!” |
| Psa 54:3 | seek | HVpp3cp | face | 16995 | 3 | For strangers have risen against me; ruthless men **seek** my life; they do not set God before themselves. Selah |
| Psa 63:9 | seek | HVpi3mp | face | 16995, 17124 | 3 | But those who **seek** to destroy my life shall go down into the depths of the earth; |
| Psa 69:6 | seek | HVprmpc | face | - | 1 | Let not those who hope in you be put to shame through me, O Lord God of hosts; let not those who **seek** you be brought to dishonor through me, O God of Israel. |
| Psa 70:2 | seek | HVprmpc | face | 16995 | 2 | Let them be put to shame and confusion who **seek** my life! Let them be turned back and brought to dishonor who delight in my hurt! |
| Psa 70:4 | seek | HVprmpc | face | - | 3 | May all who **seek** you rejoice and be glad in you! May those who love your salvation say evermore, “ God is great!” |
| Psa 71:13 | seek | HVprmpc | face | - | 2 | May my accusers be put to shame and consumed; with scorn and disgrace may they be covered who **seek** my hurt. |
| Psa 83:16 | seek | HVpu3mp | face | - | 3 | Fill their faces with shame, that they may **seek** your name, O Lord. |
| Psa 105:3 | seek | HVprmpc | face | 15195, 16654, 17109, 19606 | 3 | Glory in his holy name; let the hearts of those who **seek** the Lord rejoice! |
| Psa 105:4 | seek | HVpv2mp | face | - | 0 | **Seek** the Lord and his strength; seek his presence continually! |
| Psa 119:176 | seek | HVpv2ms | use | 18594 | 3 | I have gone astray like a lost sheep; **seek** your servant, for I do not forget your commandments. |
| Psa 122:9 | seek | HVpc1cs | face | - | 1 | For the sake of the house of the Lord our God, I will **seek** your good. |
| Pro 2:4 | seek | HVpi2ms | face | - | 2 | if you **seek** it like silver and search for it as for hidden treasures, |
| Pro 28:5 | seek | HVprmpc | face | - | 1 | Evil men do not understand justice, but those who **seek** the Lord understand it completely. |
| Pro 29:10 | seek | HVpi3mp | face | 14478, 17086 | 3 | Bloodthirsty men hate one who is blameless and **seek** the life of the upright. |
| Pro 29:26 | seek | HVprmpa | face | - | 2 | Many **seek** the face of a ruler, but it is from the Lord that a man gets justice. |
| Ecc 3:6 | seek | HVpcc | face | - | 2 | a time to **seek**, and a time to lose; a time to keep, and a time to cast away; |
| Ecc 7:25 | seek | HVpcc | face | 17112, 17236 | 2 | I turned my heart to know and to search out and to **seek** wisdom and the scheme of things, and to know the wickedness of folly and the foolishness that is madness. |
| Song 3:2 | seek | HVpc1cs | face | 16862 | 3 | I will rise now and go about the city, in the streets and in the squares; I will **seek** him whom my soul loves. I sought him, but found him not. |
| Song 6:1 | seek | HVpu1cp | face | - | 3 | Where has your beloved gone, O most beautiful among women? Where has your beloved turned, that we may **seek** him with you? |
| Isa 41:12 | seek | HVpi2ms | use | - | 3 | You shall **seek** those who contend with you, but you shall not find them; those who war against you shall be as nothing at all. |
| Isa 41:17 | seek | HVprmpa | silence | - | 2 | When the poor and needy **seek** water, and there is none, and their tongue is parched with thirst, I the Lord will answer them; I the God of Israel will not forsake them. |
| Isa 45:19 | seek | HVpv2mp | face | - | 3 | I did not speak in secret, in a land of darkness; I did not say to the offspring of Jacob, ‘ **Seek** me in vain.’ I the Lord speak the truth; I declare what is right. |
| Isa 51:1 | seek | HVprmpc | face | - | 3 | “ Listen to me, you who pursue righteousness, you who **seek** the Lord: look to the rock from which you were hewn, and to the quarry from which you were dug. |
| Isa 65:1 | seek | HVpp3cp | face | - | 2 | I was ready to be sought by those who did not ask for me; I was ready to be found by those who did not **seek** me. I said, “ Here I am, here I am,” to a nation that was not called by my name. |
| Jer 2:24 | seek | HVprmpc | face | - | 0 | a wild donkey used to the wilderness, in her heat sniffing the wind! Who can restrain her lust? None who **seek** her need weary themselves; in her month they will find her. |
| Jer 2:33 | seek | HVpcc | face | - | 3 | “ How well you direct your course to **seek** love! So that even to wicked women you have taught your ways. |
| Jer 4:30 | seek | HVpi3mp | face | - | 3 | And you, O desolate one, what do you mean that you dress in scarlet, that you adorn yourself with ornaments of gold, that you enlarge your eyes with paint? In vain you beautify yourself. Your lovers despise you; they **seek** your life. |
| Jer 11:21 | seek | HVprmpa | face | 16837, 16995 | 3 | Therefore thus says the Lord concerning the men of Anathoth, who **seek** your life, and say, “Do not prophesy in the name of the Lord, or you will die by our hand ”— |
| Jer 19:7 | seek | HVprmpc | face | 16753, 16995 | 3 | And in this place I will make void the plans of Judah and Jerusalem, and will cause their people to fall by the sword before their enemies, and by the hand of those who **seek** their life. I will give their dead bodies for food to the birds of the air and to the beasts of the earth. |
| Jer 19:9 | seek | HVprmpc | face | - | 2 | And I will make them eat the flesh of their sons and their daughters, and everyone shall eat the flesh of his neighbor in the siege and in the distress, with which their enemies and those who **seek** their life afflict them.’ |
| Jer 21:7 | seek | HVprmpc | face | 16753, 16995 | 3 | Afterward, declares the Lord, I will give Zedekiah king of Judah and his servants and the people in this city who survive the pestilence, sword, and famine into the hand of Nebuchadnezzar king of Babylon and into the hand of their enemies, into the hand of those who **seek** their lives. He shall strike them down with the edge of the sword. He shall not pity them or spare them or have compassion.’ |
| Jer 22:25 | seek | HVprmpc | face | 16753, 16995 | 3 | and give you into the hand of those who **seek** your life, into the hand of those of whom you are afraid, even into the hand of Nebuchadnezzar king of Babylon and into the hand of the Chaldeans. |
| Jer 29:13 | seek | HVpq2mp | face | 17106, 19415, 19423 | 3 | You will **seek** me and find me, when you seek me with all your heart. |
| Jer 34:20 | seek | HVprmpc | face | 16753, 16995 | 3 | And I will give them into the hand of their enemies and into the hand of those who **seek** their lives. Their dead bodies shall be food for the birds of the air and the beasts of the earth. |
| Jer 34:21 | seek | HVprmpc | face | 16753, 16995 | 3 | And Zedekiah king of Judah and his officials I will give into the hand of their enemies and into the hand of those who **seek** their lives, into the hand of the army of the king of Babylon which has withdrawn from you. |
| Jer 38:16 | seek | HVprmpa | face | 16753 | 3 | Then King Zedekiah swore secretly to Jeremiah, “As the Lord lives, who made our souls, I will not put you to death or deliver you into the hand of these men who **seek** your life.” |
| Jer 44:30 | seek | HVprmpc | face | 16753, 16995 | 2 | Thus says the Lord, Behold, I will give Pharaoh Hophra king of Egypt into the hand of his enemies and into the hand of those who **seek** his life, as I gave Zedekiah king of Judah into the hand of Nebuchadnezzar king of Babylon, who was his enemy and sought his life.” |
| Jer 45:5 | seek | HVpi2ms | face | - | 0 | And do you **seek** great things for yourself? Seek them not, for behold, I am bringing disaster upon all flesh, declares the Lord. But I will give you your life as a prize of war in all places to which you may go.” |
| Jer 45:5 | seek | HVpj2ms | face | - | 0 | And do you **seek** great things for yourself? Seek them not, for behold, I am bringing disaster upon all flesh, declares the Lord. But I will give you your life as a prize of war in all places to which you may go.” |
| Jer 46:26 | seek | HVprmpc | face | 16753, 16995 | 3 | I will deliver them into the hand of those who **seek** their life, into the hand of Nebuchadnezzar king of Babylon and his officers. Afterward Egypt shall be inhabited as in the days of old, declares the Lord. |
| Jer 49:37 | seek | HVprmpc | face | 14670, 16995 | 0 | I will terrify Elam before their enemies and before those who **seek** their life. I will bring disaster upon them, my fierce anger, declares the Lord. I will send the sword after them, until I have consumed them, |
| Jer 50:4 | seek | HVpi3mp | face | - | 3 | “In those days and in that time, declares the Lord, the people of Israel and the people of Judah shall come together, weeping as they come, and they shall **seek** the Lord their God. |
| Eze 7:25 | seek | HVpq3cp | face | - | 2 | When anguish comes, they will **seek** peace, but there shall be none. |
| Eze 7:26 | seek | HVpq3cp | face | - | 2 | Disaster comes upon disaster; rumor follows rumor. They **seek** a vision from the prophet, while the law perishes from the priest and counsel from the elders. |
| Eze 34:6 | seek | HVprmsa | use | - | 3 | they wandered over all the mountains and on every high hill. My sheep were scattered over all the face of the earth, with none to search or **seek** for them. |
| Eze 34:16 | seek | HVpi1cs | use | 18594 | 3 | I will **seek** the lost, and I will bring back the strayed, and I will bind up the injured, and I will strengthen the weak, and the fat and the strong I will destroy. I will feed them in justice. |
| Hos 2:7 | seek | HVpq3fs | face | - | 3 | She shall pursue her lovers but not overtake them, and she shall **seek** them but shall not find them. Then she shall say, ‘I will go and return to my first husband, for it was better for me then than now.’ |
| Hos 3:5 | seek | HVpq3cp | face | - | 3 | Afterward the children of Israel shall return and **seek** the Lord their God, and David their king, and they shall come in fear to the Lord and to his goodness in the latter days. |
| Hos 5:6 | seek | HVpcc | face | - | 3 | With their flocks and herds they shall go to **seek** the Lord, but they will not find him; he has withdrawn from them. |
| Hos 5:15 | seek | HVpq3cp | face | - | 0 | I will return again to my place, until they acknowledge their guilt and **seek** my face, and in their distress earnestly seek me. |
| Hos 7:10 | seek | HVpp3cp | face | 15087 | 2 | The pride of Israel testifies to his face; yet they do not return to the Lord their God, nor **seek** him, for all this. |
| Amo 8:12 | seek | HVpcc | face | - | 3 | They shall wander from sea to sea, and from north to east; they shall run to and fro, to **seek** the word of the Lord, but they shall not find it. |
| Nah 3:7 | seek | HVpi1cs | face | - | 3 | And all who look at you will shrink from you and say, “ Wasted is Nineveh; who will grieve for her?” Where shall I **seek** comforters for you? |
| Nah 3:11 | seek | HVpi2fs | face | - | 2 | You also will be drunken; you will go into hiding; you will **seek** a refuge from the enemy. |
| Zep 1:6 | seek | HVpp3cp | face | - | 2 | those who have turned back from following the Lord, who do not **seek** the Lord or inquire of him.” |
| Zep 2:3 | seek | HVpv2mp | face | - | 0 | **Seek** the Lord, all you humble of the land, who do his just commands; seek righteousness; seek humility; perhaps you may be hidden on the day of the anger of the Lord. |
| Zep 2:3 | seek | HVpv2mp | face | - | 0 | **Seek** the Lord, all you humble of the land, who do his just commands; seek righteousness; seek humility; perhaps you may be hidden on the day of the anger of the Lord. |
| Zep 2:3 | seek | HVpv2mp | face | - | 0 | **Seek** the Lord, all you humble of the land, who do his just commands; seek righteousness; seek humility; perhaps you may be hidden on the day of the anger of the Lord. |
| Zec 8:21 | seek | HVpcc | face | - | 3 | The inhabitants of one city shall go to another, saying, ‘Let us go at once to entreat the favor of the Lord and to **seek** the Lord of hosts; I myself am going.’ |
| Zec 8:22 | seek | HVpcc | face | - | 2 | Many peoples and strong nations shall come to **seek** the Lord of hosts in Jerusalem and to entreat the favor of the Lord. |
| Zec 11:16 | seek | HVpi3ms | use | - | 3 | For behold, I am raising up in the land a shepherd who does not care for those being destroyed, or **seek** the young or heal the maimed or nourish the healthy, but devours the flesh of the fat ones, tearing off even their hoofs. |
| Zec 12:9 | seek | HVpi1cs | face | - | 2 | And on that day I will **seek** to destroy all the nations that come against Jerusalem. |
| Mal 2:7 | seek | HVpi3mp | face | - | 2 | For the lips of a priest should guard knowledge, and people should **seek** instruction from his mouth, for he is the messenger of the Lord of hosts. |
| Mal 3:1 | seek | HVprmpa | face | - | 3 | “ Behold, I send my messenger, and he will prepare the way before me. And the Lord whom you **seek** will suddenly come to his temple; and the messenger of the covenant in whom you delight, behold, he is coming, says the Lord of hosts. |
| 1Sa 16:16 | seek out | HVpi3mp | use | - | 3 | Let our lord now command your servants who are before you to **seek out** a man who is skillful in playing the lyre, and when the harmful spirit from God is upon you, he will play it, and you will be well.” |
| Gen 37:15 | seeking | HVpi2ms | silence | 20884, 20886, 20889, 20890, 20892, 20893, 20894, 20895 | 2 | And a man found him wandering in the fields. And the man asked him, “ What are you **seeking**?” |
| Exo 4:19 | seeking | HVprmpa | face | 16211, 17122 | 3 | And the Lord said to Moses in Midian, “ Go back to Egypt, for all the men who were **seeking** your life are dead.” |
| Judg 14:4 | seeking | HVprmsa | face | - | 2 | His father and mother did not know that it was from the Lord, for he was **seeking** an opportunity against the Philistines. At that time the Philistines ruled over Israel. |
| Judg 18:1 | seeking | HVprmsa | face | - | 2 | In those days there was no king in Israel. And in those days the tribe of the people of Dan was **seeking** for itself an inheritance to dwell in, for until then no inheritance among the tribes of Israel had fallen to them. |
| 1Sa 27:1 | seeking | HVpcc | face | - | 3 | Then David said in his heart, “ Now I shall perish one day by the hand of Saul. There is nothing better for me than that I should escape to the land of the Philistines. Then Saul will despair of **seeking** me any longer within the borders of Israel, and I shall escape out of his hand.” |
| 1Ki 11:22 | seeking | HVprmsa | face | - | 3 | But Pharaoh said to him, “ What have you lacked with me that you are now **seeking** to go to your own country?” And he said to him, “ Only let me depart.” |
| 1Ki 20:7 | seeking | HVprmsa | face | - | 3 | Then the king of Israel called all the elders of the land and said, “ Mark, now, and see how this man is **seeking** trouble, for he sent to me for my wives and my children, and for my silver and my gold, and I did not refuse him.” |
| Psa 104:21 | seeking | HVpcc | silence | - | 2 | The young lions roar for their prey, **seeking** their food from God. |
| Dan 9:3 | seeking | HVpcc | face | - | 3 | Then I turned my face to the Lord God, **seeking** him by prayer and pleas for mercy with fasting and sackcloth and ashes. |
| Mal 2:15 | seeking | HVprmsa | face | 17115 | 3 | Did he not make them one, with a portion of the Spirit in their union? And what was the one God **seeking**? Godly offspring. So guard yourselves in your spirit, and let none of you be faithless to the wife of your youth. |
| 1Sa 19:2 | seeks | HVprmsa | face | 17959, 18878, 19193 | 3 | And Jonathan told David, “ Saul my father **seeks** to kill you. Therefore be on your guard in the morning. Stay in a secret place and hide yourself. |
| 1Sa 20:1 | seeks | HVprmsa | face | 16592, 16995, 17118 | 3 | Then David fled from Naioth in Ramah and came and said before Jonathan, “ What have I done? What is my guilt? And what is my sin before your father, that he **seeks** my life?” |
| 1Sa 22:23 | seeks | HVpi3ms | face | - | 0 | Stay with me; do not be afraid, for he who **seeks** my life seeks your life. With me you shall be in safekeeping.” |
| 1Sa 22:23 | seeks | HVpi3ms | face | - | 0 | Stay with me; do not be afraid, for he who **seeks** my life seeks your life. With me you shall be in safekeeping.” |
| 1Sa 23:10 | seeks | HVprmsa | face | - | 3 | Then David said, “O Lord, the God of Israel, your servant has surely heard that Saul **seeks** to come to Keilah, to destroy the city on my account. |
| 1Sa 24:9 | seeks | HVprmsa | face | - | 2 | And David said to Saul, “ Why do you listen to the words of men who say, ‘ Behold, David **seeks** your harm ’? |
| 2Sa 16:11 | seeks | HVprmsa | face | 17118 | 3 | And David said to Abishai and to all his servants, “ Behold, my own son **seeks** my life; how much more now may this Benjaminite! Leave him alone, and let him curse, for the Lord has told him to. |
| Psa 37:32 | seeks | HVprmsa | face | - | 3 | The wicked watches for the righteous and **seeks** to put him to death. |
| Psa 86:14 | seeks | HVpp3cp | face | 15123, 15747, 16700, 16995 | 3 | O God, insolent men have risen up against me; a band of ruthless men **seeks** my life, and they do not set you before them. |
| Pro 11:27 | seeks | HVpi3ms | face | - | 3 | Whoever diligently **seeks** good seeks favor, but evil comes to him who searches for it. |
| Pro 14:6 | seeks | HVpp3ms | face | 15205 | 2 | A scoffer **seeks** wisdom in vain, but knowledge is easy for a man of understanding. |
| Pro 15:14 | seeks | HVpi3ms | face | 17112 | 3 | The heart of him who has understanding **seeks** knowledge, but the mouths of fools feed on folly. |
| Pro 17:9 | seeks | HVprmsa | face | - | 2 | Whoever covers an offense **seeks** love, but he who repeats a matter separates close friends. |
| Pro 17:11 | seeks | HVpi3ms | face | - | 3 | An evil man **seeks** only rebellion, and a cruel messenger will be sent against him. |
| Pro 17:19 | seeks | HVprmsa | face | 15118 | 2 | Whoever loves transgression loves strife; he who makes his door high **seeks** destruction. |
| Pro 18:1 | seeks | HVpi3ms | face | 17451 | 3 | Whoever isolates himself **seeks** his own desire; he breaks out against all sound judgment. |
| Pro 18:15 | seeks | HVpi3fs | face | - | 2 | An intelligent heart acquires knowledge, and the ear of the wise **seeks** knowledge. |
| Ecc 3:15 | seeks | HVpi3ms | use | - | 3 | That which is, already has been; that which is to be, already has been; and God **seeks** what has been driven away. |
| Jer 5:1 | seeks | HVprmsa | face | - | 3 | Run to and fro through the streets of Jerusalem, look and take note! Search her squares to see if you can find a man, one who does justice and **seeks** truth, that I may pardon her. |
| Isa 40:20 | seeks out | HVpi3ms | use | - | 3 | He who is too impoverished for an offering chooses wood that will not rot; he **seeks out** a skillful craftsman to set up an idol that will not move. |
| Gen 43:30 | sought | HVpw3ms | use | - | 4 | Then Joseph hurried out, for his compassion grew warm for his brother, and he **sought** a place to weep. And he entered his chamber and wept there. |
| Exo 4:24 | sought | HVpw3ms | face | - | 3 | At a lodging place on the way the Lord met him and **sought** to put him to death. |
| Exo 33:7 | sought | HVprmsa | face | - | 3 | Now Moses used to take the tent and pitch it outside the camp, far off from the camp, and he called it the tent of meeting. And everyone who **sought** the Lord would go out to the tent of meeting, which was outside the camp. |
| Deu 13:10 | sought | HVpp3ms | face | - | 3 | You shall stone him to death with stones, because he **sought** to draw you away from the Lord your God, who brought you out of the land of Egypt, out of the house of slavery. |
| 1Sa 10:21 | sought | HVpw3mp | silence | - | 2 | He brought the tribe of Benjamin near by its clans, and the clan of the Matrites was taken by lot; and Saul the son of Kish was taken by lot. But when they **sought** him, he could not be found. |
| 1Sa 14:4 | sought | HVpp3ms | face | - | 3 | Within the passes, by which Jonathan **sought** to go over to the Philistine garrison, there was a rocky crag on the one side and a rocky crag on the other side. The name of the one was Bozez, and the name of the other Seneh. |
| 1Sa 19:10 | sought | HVpw3ms | face | - | 3 | And Saul **sought** to pin David to the wall with the spear, but he eluded Saul, so that he struck the spear into the wall. And David fled and escaped that night. |
| 1Sa 23:14 | sought | HVpw3ms | use | - | 0 | And David remained in the strongholds in the wilderness, in the hill country of the wilderness of Ziph. And Saul **sought** him every day, but God did not give him into his hand. |
| 2Sa 4:8 | sought | HVpp3ms | face | 16085, 16754 | 3 | and brought the head of Ish-bosheth to David at Hebron. And they said to the king, “Here is the head of Ish-bosheth, the son of Saul, your enemy, who **sought** your life. The Lord has avenged my lord the king this day on Saul and on his offspring.” |
| 2Sa 12:16 | sought | HVpw3ms | face | - | 3 | David therefore **sought** God on behalf of the child. And David fasted and went in and lay all night on the ground. ^ |
| 2Sa 17:20 | sought | HVpw3mp | silence | - | 3 | When Absalom’s servants came to the woman at the house, they said, “ Where are Ahimaaz and Jonathan?” And the woman said to them, “They have gone over the brook of water.” And when they had **sought** and could not find them, they returned to Jerusalem. |
| 2Sa 21:1 | sought | HVpw3ms | face | - | 3 | Now there was a famine in the days of David for three years, year after year. And David **sought** the face of the Lord. And the Lord said, “There is bloodguilt on Saul and on his house, because he put the Gibeonites to death.” |
| 2Sa 21:2 | sought | HVpw3ms | face | - | 3 | So the king called the Gibeonites and spoke to them. Now the Gibeonites were not of the people of Israel but of the remnant of the Amorites. Although the people of Israel had sworn to spare them, Saul had **sought** to strike them down in his zeal for the people of Israel and Judah. |
| 1Ki 1:2 | sought | HVpi3mp | silence | - | 2 | Therefore his servants said to him, “Let a young woman be **sought** for my lord the king, and let her wait on the king and be in his service. Let her lie in your arms, that my lord the king may be warm.” |
| 1Ki 1:3 | sought | HVpw3mp | silence | - | 3 | So they **sought** for a beautiful young woman throughout all the territory of Israel, and found Abishag the Shunammite, and brought her to the king. |
| 1Ki 10:24 | sought | HVprmpa | face | - | 3 | And the whole earth **sought** the presence of Solomon to hear his wisdom, which God had put into his mind. |
| 1Ki 11:40 | sought | HVpw3ms | face | - | 3 | Solomon **sought** therefore to kill Jeroboam. But Jeroboam arose and fled into Egypt, to Shishak king of Egypt, and was in Egypt until the death of Solomon. |
| 2Ki 2:17 | sought | HVpw3mp | silence | - | 3 | But when they urged him till he was ashamed, he said, “ Send.” They sent therefore fifty men. And for three days they **sought** him but did not find him. |
| 2Ch 9:23 | sought | HVprmpa | face | - | 3 | And all the kings of the earth **sought** the presence of Solomon to hear his wisdom, which God had put into his mind. |
| 2Ch 15:4 | sought | HVpw3mp | face | - | 1 | but when in their distress they turned to the Lord, the God of Israel, and **sought** him, he was found by them. |
| 2Ch 15:15 | sought | HVpp3cp | face | 17106 | 3 | And all Judah rejoiced over the oath, for they had sworn with all their heart and had **sought** him with their whole desire, and he was found by them, and the Lord gave them rest all around. |
| Neh 7:64 | sought | HVpp3cp | silence | - | 2 | These **sought** their registration among those enrolled in the genealogies, but it was not found there, so they were excluded from the priesthood as unclean. |
| Neh 12:27 | sought | HVpp3cp | silence | - | 3 | And at the dedication of the wall of Jerusalem they **sought** the Levites in all their places, to bring them to Jerusalem to celebrate the dedication with gladness, with thanksgivings and with singing, with cymbals, harps, and lyres. |
| Est 2:21 | sought | HVpw3mp | face | 13035, 13582, 14199 | 3 | In those days, as Mordecai was sitting at the king’s gate, Bigthan and Teresh, two of the king’s eunuchs, who guarded the threshold, became angry and **sought** to lay hands on King Ahasuerus. |
| Est 3:6 | sought | HVpw3ms | face | 13197, 13398, 14271 | 3 | But he disdained to lay hands on Mordecai alone. So, as they had made known to him the people of Mordecai, Haman **sought** to destroy all the Jews, the people of Mordecai, throughout the whole kingdom of Ahasuerus. |
| Est 6:2 | sought | HVpp3cp | face | - | 3 | And it was found written how Mordecai had told about Bigthana and Teresh, two of the king’s eunuchs, who guarded the threshold, and who had **sought** to lay hands on King Ahasuerus. |
| Est 9:2 | sought | HVprmpc | face | - | 2 | The Jews gathered in their cities throughout all the provinces of King Ahasuerus to lay hands on those who **sought** their harm. And no one could stand against them, for the fear of them had fallen on all peoples. |
| Psa 37:36 | sought | HVpw1cs | silence | - | 3 | But he passed away, and behold, he was no more; though I **sought** him, he could not be found. |
| Psa 71:24 | sought | HVprmpc | face | - | 2 | And my tongue will talk of your righteous help all the day long, for they have been put to shame and disappointed who **sought** to do me hurt. |
| Ecc 7:29 | sought | HVpp3cp | face | - | 3 | See, this alone I found, that God made man upright, but they have **sought** out many schemes. |
| Ecc 12:10 | sought | HVpp3ms | face | 17834 | 3 | The Preacher **sought** to find words of delight, and uprightly he wrote words of truth. |
| Song 3:1 | sought | HVpp1cs | face | - | 0 | On my bed by night I **sought** him whom my soul loves; I sought him, but found him not. |
| Song 3:1 | sought | HVpp1cs | face | - | 0 | On my bed by night I **sought** him whom my soul loves; I sought him, but found him not. |
| Song 3:2 | sought | HVpp1cs | face | 16862, 17111 | 1 | I will rise now and go about the city, in the streets and in the squares; I will seek him whom my soul loves. I **sought** him, but found him not. |
| Song 5:6 | sought | HVpp1cs | face | 16863, 17111 | 3 | I opened to my beloved, but my beloved had turned and gone. My soul failed me when he spoke. I **sought** him, but found him not; I called him, but he gave no answer. |
| Jer 26:21 | sought | HVpw3ms | face | - | 3 | And when King Jehoiakim, with all his warriors and all the officials, heard his words, the king **sought** to put him to death. But when Uriah heard of it, he was afraid and fled and escaped to Egypt. |
| Jer 44:30 | sought | HVprmsc | face | - | 1 | Thus says the Lord, Behold, I will give Pharaoh Hophra king of Egypt into the hand of his enemies and into the hand of those who seek his life, as I gave Zedekiah king of Judah into the hand of Nebuchadnezzar king of Babylon, who was his enemy and **sought** his life.” |
| Jer 50:20 | sought | HVPi3ms | use | - | 3 | In those days and in that time, declares the Lord, iniquity shall be **sought** in Israel, and there shall be none, and sin in Judah, and none shall be found, for I will pardon those whom I leave as a remnant. |
| Eze 22:30 | sought | HVpw1cs | use | 13003, 13019, 13150, 13200, 13554, 14692, 14839 | 3 | And I **sought** for a man among them who should build up the wall and stand in the breach before me for the land, that I should not destroy it, but I found none. |
| Eze 34:4 | sought | HVpp2mp | use | 19108 | 3 | The weak you have not strengthened, the sick you have not healed, the injured you have not bound up, the strayed you have not brought back, the lost you have not **sought**, and with force and harshness you have ruled them. |
| Dan 8:15 | sought | HVpw1cs | face | - | 3 | When I, Daniel, had seen the vision, I **sought** to understand it. And behold, there stood before me one having the appearance of a man. |
| Eze 26:21 | sought for | HVPu2fs | silence | - | 3 | I will bring you to a dreadful end, and you shall be no more. Though you be **sought for**, you will never be found again, declares the Lord God.” |
| 1Sa 13:14 | sought out | HVpp3ms | face | 17113 | 2 | But now your kingdom shall not continue. The Lord has **sought out** a man after his own heart, and the Lord has commanded him to be prince over his people, because you have not kept what the Lord commanded you.” |
| Est 2:2 | sought out | HVpi3mp | use | - | 3 | Then the king’s young men who attended him said, “Let beautiful young virgins be **sought out** for the king. |

### 3.2 H4672 מָצָא ma.tsa "to find": 110 own occurrences in 106 verses

- **Meaning as stored:** Hebrew; native word מָצָא, transliteration ma.tsa; STEP gloss "to find"; sense head "to find" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4672):** to find, attain to.
- **Related terms (1):** H4677 me.tso.va.yah "Mezobaite".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 461; verses STEP attests 425; verse_lexical rows the parse found 455.

- **Carried by the member words:** find (91), finds (15), seeking (2), come upon (1), seek (1).
- **Engagement of these occurrences:** silence 80, use 27, face 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 4:30 | come upon | HVqq3cp | silence | - | 0 | When you are in tribulation, and all these things **come upon** you in the latter days, you will return to the Lord your God and obey his voice. |
| Gen 18:26 | find | HVqi1cs | silence | - | 0 | And the Lord said, “ If I **find** at Sodom fifty righteous in the city, I will spare the whole place for their sake.” |
| Gen 18:28 | find | HVqi1cs | silence | - | 0 | Suppose five of the fifty righteous are lacking. Will you destroy the whole city for lack of five?” And he said, “I will not destroy it if I **find** forty-five there.” |
| Gen 18:30 | find | HVqi1cs | silence | - | 0 | Then he said, “ Oh let not the Lord be angry, and I will speak. Suppose thirty are found there.” He answered, “I will not do it, if I **find** thirty there.” |
| Gen 31:32 | find | HVqi2ms | silence | - | 0 | Anyone with whom you **find** your gods shall not live. In the presence of our kinsmen point out what I have that is yours, and take it.” Now Jacob did not know that Rachel had stolen them. |
| Gen 31:33 | find | HVqp3ms | silence | - | 0 | So Laban went into Jacob’s tent and into Leah’s tent and into the tent of the two female servants, but he did not **find** them. And he went out of Leah’s tent and entered Rachel’s. |
| Gen 31:34 | find | HVqp3ms | silence | - | 0 | Now Rachel had taken the household gods and put them in the camel’s saddle and sat on them. Laban felt all about the tent, but did not **find** them. |
| Gen 31:35 | find | HVqp3ms | silence | - | 0 | And she said to her father, “Let not my lord be angry that I cannot rise before you, for the way of women is upon me.” So he searched but did not **find** the household gods. |
| Gen 32:5 | find | HVqcc | use | - | 0 | I have oxen, donkeys, flocks, male servants, and female servants. I have sent to tell my lord, in order that I may **find** favor in your sight.’” |
| Gen 32:19 | find | HVqcc | silence | - | 0 | He likewise instructed the second and the third and all who followed the droves, “You shall say the same thing to Esau when you **find** him, |
| Gen 33:8 | find | HVqcc | use | - | 0 | Esau said, “ What do you mean by all this company that I met?” Jacob answered, “ To **find** favor in the sight of my lord.” |
| Gen 33:15 | find | HVqi1cs | use | - | 0 | So Esau said, “ Let me leave with you some of the people who are with me.” But he said, “ What need is there? Let me **find** favor in the sight of my lord.” |
| Gen 34:11 | find | HVqi1cs | use | - | 0 | Shechem also said to her father and to her brothers, “Let me **find** favor in your eyes, and whatever you say to me I will give. |
| Gen 38:20 | find | HVqp3ms | silence | - | 0 | When Judah sent the young goat by his friend the Adullamite to take back the pledge from the woman’s hand, he did not **find** her. |
| Gen 38:23 | find | HVqp2ms | silence | - | 0 | And Judah replied, “Let her keep the things as her own, or we shall be laughed at. You see, I sent this young goat, and you did not **find** her.” |
| Gen 41:38 | find | HVqi1cp | silence | - | 0 | And Pharaoh said to his servants, “Can we **find** a man like this, in whom is the Spirit of God?” |
| Gen 44:34 | find | HVqi3ms | silence | - | 0 | For how can I go back to my father if the boy is not with me? I fear to see the evil that would **find** my father.” |
| Exo 5:11 | find | HVqi2mp | silence | - | 0 | Go and get your straw yourselves wherever you can **find** it, but your work will not be reduced in the least.’” |
| Exo 16:25 | find | HVqi2mp | silence | - | 0 | Moses said, “ Eat it today, for today is a Sabbath to the Lord; today you will not **find** it in the field. |
| Exo 33:13 | find | HVqc1cs | use | - | 0 | Now therefore, if I have found favor in your sight, please show me now your ways, that I may know you in order to **find** favor in your sight. Consider too that this nation is your people.” |
| Num 11:15 | find | HVqp1cs | use | - | 0 | If you will treat me like this, kill me at once, if I **find** favor in your sight, that I may not see my wretchedness.” |
| Num 32:23 | find | HVqi3fs | silence | - | 0 | But if you will not do so, behold, you have sinned against the Lord, and be sure your sin will **find** you out. |
| Deu 4:29 | find | HVqq2ms | use | - | 0 | But from there you will seek the Lord your God and you will **find** him, if you search after him with all your heart and with all your soul. |
| Deu 22:3 | find | HVqq2ms | silence | - | 0 | And you shall do the same with his donkey or with his garment, or with any lost thing of your brother’s, which he loses and you **find**; you may not ignore it. |
| Deu 22:14 | find | HVqp1cs | silence | - | 0 | and accuses her of misconduct and brings a bad name upon her, saying, ‘I took this woman, and when I came near her, I did not **find** in her evidence of virginity,’ |
| Deu 22:17 | find | HVqp1cs | silence | - | 0 | and behold, he has accused her of misconduct, saying, “I did not **find** in your daughter evidence of virginity.” And yet this is the evidence of my daughter’s virginity.’ And they shall spread the cloak before the elders of the city. |
| Judg 17:8 | find | HVqi3ms | silence | - | 0 | And the man departed from the town of Bethlehem in Judah to sojourn where he could **find** a place. And as he journeyed, he came to the hill country of Ephraim to the house of Micah. |
| Judg 17:9 | find | HVqi1cs | silence | - | 0 | And Micah said to him, “ Where do you come from?” And he said to him, “I am a Levite of Bethlehem in Judah, and I am going to sojourn where I may **find** a place.” |
| Rut 1:9 | find | HVqv2fp | use | - | 0 | The Lord grant that you may **find** rest, each of you in the house of her husband!” Then she kissed them, and they lifted up their voices and wept. |
| Rut 2:2 | find | HVqi1cs | use | - | 0 | And Ruth the Moabite said to Naomi, “ Let me go to the field and glean among the ears of grain after him in whose sight I shall **find** favor.” And she said to her, “ Go, my daughter.” |
| 1Sa 1:18 | find | HVqi3fs | use | - | 0 | And she said, “Let your servant **find** favor in your eyes.” Then the woman went her way and ate, and her face was no longer sad. |
| 1Sa 9:4 | find | HVqp3cp | silence | - | 0 | And he passed through the hill country of Ephraim and passed through the land of Shalishah, but they did not **find** them. And they passed through the land of Shaalim, but they were not there. Then they passed through the land of Benjamin, but did not find them. |
| 1Sa 9:4 | find | HVqp3cp | silence | - | 0 | And he passed through the hill country of Ephraim and passed through the land of Shalishah, but they did not **find** them. And they passed through the land of Shaalim, but they were not there. Then they passed through the land of Benjamin, but did not find them. |
| 1Sa 9:13 | find | HVqi2mp | silence | - | 0 | As soon as you enter the city you will **find** him, before he goes up to the high place to eat. For the people will not eat till he comes, since he must bless the sacrifice; afterward those who are invited will eat. Now go up, for you will meet him immediately.” |
| 1Sa 20:21 | find | HVqv2ms | silence | - | 0 | And behold, I will send the boy, saying, ‘ Go, **find** the arrows.’ If I say to the boy, ‘ Look, the arrows are on this side of you, take them,’ then you are to come, for, as the Lord lives, it is safe for you and there is no danger. |
| 1Sa 20:36 | find | HVqv2ms | silence | - | 0 | And he said to his boy, “ Run and **find** the arrows that I shoot.” As the boy ran, he shot an arrow beyond him. |
| 1Sa 23:17 | find | HVqi3fs | silence | - | 0 | And he said to him, “Do not fear, for the hand of Saul my father shall not **find** you. You shall be king over Israel, and I shall be next to you. Saul my father also knows this.” |
| 1Sa 25:8 | find | HVqu3mp | use | - | 0 | Ask your young men, and they will tell you. Therefore let my young men **find** favor in your eyes, for we come on a feast day. Please give whatever you have at hand to your servants and to your son David.’” |
| 2Sa 15:25 | find | HVqi1cs | use | - | 0 | Then the king said to Zadok, “ Carry the ark of God back into the city. If I **find** favor in the eyes of the Lord, he will bring me back and let me see both it and his dwelling place. |
| 2Sa 16:4 | find | HVqi1cs | use | - | 0 | Then the king said to Ziba, “ Behold, all that belonged to Mephibosheth is now yours.” And Ziba said, “I pay homage; let me ever **find** favor in your sight, my lord the king.” |
| 2Sa 17:20 | find | HVqp3cp | silence | - | 0 | When Absalom’s servants came to the woman at the house, they said, “ Where are Ahimaaz and Jonathan?” And the woman said to them, “They have gone over the brook of water.” And when they had sought and could not **find** them, they returned to Jerusalem. |
| 1Ki 18:5 | find | HVqi1cp | silence | - | 0 | And Ahab said to Obadiah, “ Go through the land to all the springs of water and to all the valleys. Perhaps we may **find** grass and save the horses and mules alive, and not lose some of the animals.” |
| 1Ki 18:12 | find | HVqi3ms | silence | - | 0 | And as soon as I have gone from you, the Spirit of the Lord will carry you I know not where. And so, when I come and tell Ahab and he cannot **find** you, he will kill me, although I your servant have feared the Lord from my youth. |
| 2Ki 2:17 | find | HVqp3cp | silence | - | 0 | But when they urged him till he was ashamed, he said, “ Send.” They sent therefore fifty men. And for three days they sought him but did not **find** him. |
| 2Ch 20:16 | find | HVqq2mp | silence | - | 0 | Tomorrow go down against them. Behold, they will come up by the ascent of Ziz. You will **find** them at the end of the valley, east of the wilderness of Jeruel. |
| 2Ch 32:4 | find | HVqq3cp | silence | - | 0 | A great many people were gathered, and they stopped all the springs and the brook that flowed through the land, saying, “ Why should the kings of Assyria come and **find** much water?” |
| Neh 5:8 | find | HVqp3cp | silence | - | 0 | and said to them, “We, as far as we are able, have bought back our Jewish brothers who have been sold to the nations, but you even sell your brothers that they may be sold to us!” They were silent and could not **find** a word to say. |
| Job 3:22 | find | HVqi3mp | silence | - | 0 | who rejoice exceedingly and are glad when they **find** the grave? |
| Job 11:7 | find | HVqi2ms | silence | - | 0 | “Can you **find** out the deep things of God? Can you find out the limit of the Almighty? |
| Job 17:10 | find | HVqi1cs | silence | - | 0 | But you, come on again, all of you, and I shall not **find** a wise man among you. |
| Job 23:3 | find | HVqu1cs | use | - | 0 | Oh, that I knew where I might **find** him, that I might come even to his seat! |
| Job 37:23 | find | HVqp1cp | use | - | 0 | The Almighty —we cannot **find** him; he is great in power; justice and abundant righteousness he will not violate. |
| Psa 10:15 | find | HVqi2ms | silence | - | 0 | Break the arm of the wicked and evildoer; call his wickedness to account till you **find** none. |
| Psa 17:3 | find | HVqi2ms | use | - | 0 | You have tried my heart, you have visited me by night, you have tested me, and you will **find** nothing; I have purposed that my mouth will not transgress. |
| Psa 132:5 | find | HVqi1cs | silence | - | 0 | until I **find** a place for the Lord, a dwelling place for the Mighty One of Jacob.” |
| Pro 1:13 | find | HVqi1cp | silence | - | 0 | we shall **find** all precious goods, we shall fill our houses with plunder; |
| Pro 1:28 | find | HVqi3mp | use | - | 0 | Then they will call upon me, but I will not answer; they will seek me diligently but will not **find** me. |
| Pro 2:5 | find | HVqi2ms | use | - | 0 | then you will understand the fear of the Lord and **find** the knowledge of God. |
| Pro 3:4 | find | HVqv2ms | use | - | 0 | So you will **find** favor and good success in the sight of God and man. |
| Pro 4:22 | find | HVqrmpc | silence | - | 0 | For they are life to those who **find** them, and healing to all their flesh. |
| Pro 8:9 | find | HVqrmpc | silence | - | 0 | They are all straight to him who understands, and right to those who **find** knowledge. |
| Pro 8:12 | find | HVqi1cs | silence | - | 0 | “ I, wisdom, dwell with prudence, and I **find** knowledge and discretion. |
| Pro 8:17 | find | HVqi3mp | use | - | 0 | I love those who love me, and those who seek me diligently **find** me. |
| Pro 20:6 | find | HVqi3ms | silence | - | 0 | Many a man proclaims his own steadfast love, but a faithful man who can **find**? |
| Pro 21:21 | find | HVqi3ms | silence | - | 0 | Whoever pursues righteousness and kindness will **find** life, righteousness, and honor. |
| Pro 24:14 | find | HVqp2ms | silence | - | 0 | Know that wisdom is such to your soul; if you **find** it, there will be a future, and your hope will not be cut off. |
| Pro 28:23 | find | HVqi3ms | use | - | 0 | Whoever rebukes a man will afterward **find** more favor than he who flatters with his tongue. |
| Pro 31:10 | find | HVqi3ms | silence | - | 0 | An excellent wife who can **find**? She is far more precious than jewels. |
| Ecc 7:14 | find | HVqi3ms | silence | - | 0 | In the day of prosperity be joyful, and in the day of adversity consider: God has made the one as well as the other, so that man may not **find** out anything that will be after him. |
| Ecc 7:26 | find | HVqrmsa | silence | - | 0 | And I **find** something more bitter than death: the woman whose heart is snares and nets, and whose hands are fetters. He who pleases God escapes her, but the sinner is taken by her. |
| Ecc 7:27 | find | HVqcc | silence | - | 0 | Behold, this is what I found, says the Preacher, while adding one thing to another to **find** the scheme of things— |
| Ecc 8:17 | find | HVqcc | silence | - | 0 | then I saw all the work of God, that man cannot **find** out the work that is done under the sun. However much man may toil in seeking, he will not find it out. Even though a wise man claims to know, he cannot find it out. |
| Ecc 11:1 | find | HVqi2ms | silence | - | 0 | Cast your bread upon the waters, for you will **find** it after many days. |
| Ecc 12:10 | find | HVqcc | silence | - | 0 | The Preacher sought to **find** words of delight, and uprightly he wrote words of truth. |
| Song 5:8 | find | HVqi2mp | silence | - | 0 | I adjure you, O daughters of Jerusalem, if you **find** my beloved, that you tell him I am sick with love. |
| Isa 41:12 | find | HVqi2ms | silence | - | 0 | You shall seek those who contend with you, but you shall not **find** them; those who war against you shall be as nothing at all. |
| Jer 2:5 | find | HVqp3cp | silence | - | 0 | Thus says the Lord: “ What wrong did your fathers **find** in me that they went far from me, and went after worthlessness, and became worthless? |
| Jer 2:24 | find | HVqi3mp | silence | - | 0 | a wild donkey used to the wilderness, in her heat sniffing the wind! Who can restrain her lust? None who seek her need weary themselves; in her month they will **find** her. |
| Jer 2:34 | find | HVqp2fs | silence | - | 0 | Also on your skirts is found the lifeblood of the guiltless poor; you did not **find** them breaking in. Yet in spite of all these things |
| Jer 5:1 | find | HVqi2mp | silence | - | 0 | Run to and fro through the streets of Jerusalem, look and take note! Search her squares to see if you can **find** a man, one who does justice and seeks truth, that I may pardon her. |
| Jer 6:16 | find | HVqv2mp | use | - | 0 | Thus says the Lord: “ Stand by the roads, and look, and ask for the ancient paths, where the good way is; and walk in it, and **find** rest for your souls. But they said, ‘We will not walk in it.’ |
| Jer 14:3 | find | HVqp3cp | silence | - | 0 | Her nobles send their servants for water; they come to the cisterns; they **find** no water; they return with their vessels empty; they are ashamed and confounded and cover their heads. |
| Jer 29:13 | find | HVqq2mp | use | - | 0 | You will seek me and **find** me, when you seek me with all your heart. |
| Jer 45:3 | find | HVqp1cs | use | - | 0 | You said, ‘ Woe is me! For the Lord has added sorrow to my pain. I am weary with my groaning, and I **find** no rest.’ |
| Lam 1:6 | find | HVqp3cp | silence | - | 0 | From the daughter of Zion all her majesty has departed. Her princes have become like deer that **find** no pasture; they fled without strength before the pursuer. |
| Lam 2:9 | find | HVqp3cp | silence | - | 0 | Her gates have sunk into the ground; he has ruined and broken her bars; her king and princes are among the nations; the law is no more, and her prophets **find** no vision from the Lord. |
| Eze 3:1 | find | HVqi2ms | silence | - | 0 | And he said to me, “ Son of man, eat whatever you **find** here. Eat this scroll, and go, speak to the house of Israel.” |
| Hos 2:6 | find | HVqi3fs | silence | - | 0 | Therefore I will hedge up her way with thorns, and I will build a wall against her, so that she cannot **find** her paths. |
| Hos 2:7 | find | HVqi3fs | silence | - | 0 | She shall pursue her lovers but not overtake them, and she shall seek them but shall not **find** them. Then she shall say, ‘I will go and return to my first husband, for it was better for me then than now.’ |
| Hos 5:6 | find | HVqi3mp | use | - | 0 | With their flocks and herds they shall go to seek the Lord, but they will not **find** him; he has withdrawn from them. |
| Hos 12:8 | find | HVqi3mp | silence | - | 0 | Ephraim has said, “ Ah, but I am rich; I have found wealth for myself; in all my labors they cannot **find** in me iniquity or sin.” |
| Amo 8:12 | find | HVqi3mp | silence | - | 0 | They shall wander from sea to sea, and from north to east; they shall run to and fro, to seek the word of the Lord, but they shall not **find** it. |
| Lev 25:26 | finds | HVqq3ms | silence | - | 0 | If a man has no one to redeem it and then himself becomes prosperous and **finds** sufficient means to redeem it, |
| Num 35:27 | finds | HVqq3ms | silence | - | 0 | and the avenger of blood **finds** him outside the boundaries of his city of refuge, and the avenger of blood kills the manslayer, he shall not be guilty of blood. |
| 1Sa 10:7 | finds | HVqi3fs | silence | - | 0 | Now when these signs meet you, do what your hand **finds** to do, for God is with you. |
| 1Sa 24:19 | finds | HVqi3ms | silence | - | 0 | For if a man **finds** his enemy, will he let him go away safe? So may the Lord reward you with good for what you have done to me this day. |
| Psa 84:3 | finds | HVqp3fs | silence | - | 0 | Even the sparrow **finds** a home, and the swallow a nest for herself, where she may lay her young, at your altars, O Lord of hosts, my King and my God. |
| Psa 119:162 | finds | HVqrmsc | silence | - | 0 | I rejoice at your word like one who **finds** great spoil. |
| Pro 3:13 | finds | HVqp3ms | silence | - | 0 | Blessed is the one who **finds** wisdom, and the one who gets understanding, |
| Pro 8:35 | finds | HVqrmsc | silence | - | 0 | For whoever **finds** me finds life and obtains favor from the Lord, |
| Pro 8:35 | finds | HVqp3ms | silence | - | 0 | For whoever **finds** me finds life and obtains favor from the Lord, |
| Pro 18:22 | finds | HVqp3ms | silence | - | 0 | He who **finds** a wife finds a good thing and obtains favor from the Lord. |
| Pro 18:22 | finds | HVqp3ms | silence | - | 0 | He who **finds** a wife finds a good thing and obtains favor from the Lord. |
| Ecc 9:10 | finds | HVqi3fs | silence | - | 0 | Whatever your hand **finds** to do, do it with your might, for there is no work or thought or knowledge or wisdom in Sheol, to which you are going. |
| Song 8:10 | finds | HVhrfsa | use | - | 0 | I was a wall, and my breasts were like towers; then I was in his eyes as one who **finds** peace. |
| Isa 34:14 | finds | HVqq3fs | silence | - | 0 | And wild animals shall meet with hyenas; the wild goat shall cry to his fellow; indeed, there the night bird settles and **finds** for herself a resting place. |
| Lam 1:3 | finds | HVqp3fs | use | - | 0 | Judah has gone into exile because of affliction and hard servitude; she dwells now among the nations, but **finds** no resting place; her pursuers have all overtaken her in the midst of her distress. |
| Isa 58:3 | seek | HVqi2mp | face | - | 0 | ‘ Why have we fasted, and you see it not? Why have we humbled ourselves, and you take no knowledge of it?’ Behold, in the day of your fast you **seek** your own pleasure, and oppress all your workers. |
| Ecc 8:17 | seeking | HVqi3ms | face | - | 0 | then I saw all the work of God, that man cannot find out the work that is done under the sun. However much man may toil in **seeking**, he will not find it out. Even though a wise man claims to know, he cannot find it out. |
| Isa 58:13 | seeking | HVqcc | face | - | 0 | “ If you turn back your foot from the Sabbath, from doing your pleasure on my holy day, and call the Sabbath a delight and the holy day of the Lord honorable; if you honor it, not going your own ways, or **seeking** your own pleasure, or talking idly; |

### 3.3 G2212 ζητέω zēteō "to seek": 104 own occurrences in 101 verses

- **Meaning as stored:** Greek; native word ζητέω, transliteration zēteō; STEP gloss "to seek"; sense head "to seek" (the code is its own lemma).
- **Related terms (4):** G2213 zētēma "a question/dispute"; G2214 zētēsis "controversy"; G4802 suzēteō "to debate"; G4803 suzētēsis "discussion".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 376; verses STEP attests 113; verse_lexical rows the parse found 116.

- **Carried by the member words:** seek (40), seeking (35), sought (11), seeks (7), search (3), looking for (2), insist on (1), look for (1), searched (1), searching (1), searching for (1), seek for (1).
- **Engagement of these occurrences:** face 90, use 8, silence 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 13:5 | insist on | V-PAI-3S | face | - | 3 | or rude. It does not **insist on** its own way; it is not irritable or resentful; |
| Act 9:11 | look for | V-AAM-2S | use | - | 1 | And the Lord said to him, “ Rise and go to the street called Straight, and at the house of Judas **look for** a man of Tarsus named Saul, for behold, he is praying, |
| Act 10:19 | looking for | V-PAP-NPM | use | 17130 | 3 | And while Peter was pondering the vision, the Spirit said to him, “ Behold, three men are **looking for** you. |
| Act 10:21 | looking for | V-PAI-2P | use | - | 3 | And Peter went down to the men and said, “ I am the one you are **looking for**. What is the reason for your coming?” |
| Mat 2:13 | search | V-PAN | face | - | 3 | Now when they had departed, behold, an angel of the Lord appeared to Joseph in a dream and said, “ Rise, take the child and his mother, and flee to Egypt, and remain there until I tell you, for Herod is about to **search** for the child, to destroy him.” |
| Mat 13:45 | search | V-PAP-DSM | silence | - | 3 | “ Again, the kingdom of heaven is like a merchant in **search** of fine pearls, |
| Mat 18:12 | search | V-FAI-3S | silence | - | 3 | What do you think? If a man has a hundred sheep, and one of them has gone astray, does he not leave the ninety-nine on the mountains and go in **search** of the one that went astray? |
| 2Ti 1:17 | searched | V-AAI-3S | use | - | 33 | but when he arrived in Rome he **searched** for me earnestly and found me— |
| Luk 2:48 | searching | V-IAI-1P | use | - | 2 | And when his parents saw him, they were astonished. And his mother said to him, “ Son, why have you treated us so? Behold, your father and I have been **searching** for you in great distress.” |
| Luk 2:45 | searching for | V-PAP-NPM | use | - | 3 | and when they did not find him, they returned to Jerusalem, **searching for** him. |
| Mat 6:33 | seek | V-PAM-2P | face | 19246 | 3 | But **seek** first the kingdom of God and his righteousness, and all these things will be added to you. |
| Mat 7:7 | seek | V-PAM-2P | face | - | 4 | “ Ask, and it will be given to you; **seek**, and you will find; knock, and it will be opened to you. |
| Mat 28:5 | seek | V-PAI-2P | face | - | 3 | But the angel said to the women, “Do not be afraid, for I know that you **seek** Jesus who was crucified. |
| Mar 16:6 | seek | V-PAI-2P | face | - | 3 | And he said to them, “Do not be alarmed. You **seek** Jesus of Nazareth, who was crucified. He has risen; he is not here. See the place where they laid him. |
| Luk 11:9 | seek | V-PAM-2P | face | - | 3 | And I tell you, ask, and it will be given to you; **seek**, and you will find; knock, and it will be opened to you. |
| Luk 12:29 | seek | V-PAM-2P | face | - | 3 | And do not **seek** what you are to eat and what you are to drink, nor be worried. |
| Luk 12:31 | seek | V-PAM-2P | face | - | 3 | Instead, **seek** his kingdom, and these things will be added to you. |
| Luk 13:24 | seek | V-FAI-3P | face | - | 3 | “ Strive to enter through the narrow door. For many, I tell you, will **seek** to enter and will not be able. |
| Luk 15:8 | seek | V-PAI-3S | silence | 18594 | 3 | “ Or what woman, having ten silver coins, if she loses one coin, does not light a lamp and sweep the house and **seek** diligently until she finds it? |
| Luk 19:10 | seek | V-AAN | use | 18594 | 2 | For the Son of Man came to **seek** and to save the lost.” |
| Luk 24:5 | seek | V-PAI-2P | face | - | 2 | And as they were frightened and bowed their faces to the ground, the men said to them, “ Why do you **seek** the living among the dead? |
| Joh 4:27 | seek | V-PAI-2S | face | - | 3 | Just then his disciples came back. They marveled that he was talking with a woman, but no one said, “ What do you **seek**?” or, “ Why are you talking with her?” |
| Joh 5:30 | seek | V-PAI-1S | face | - | 2 | “ I can do nothing on my own. As I hear, I judge, and my judgment is just, because I **seek** not my own will but the will of him who sent me. |
| Joh 5:44 | seek | V-PAI-2P | face | 17937 | 2 | How can you believe, when you receive glory from one another and do not **seek** the glory that comes from the only God? |
| Joh 7:19 | seek | V-PAI-2P | face | - | 4 | Has not Moses given you the law? Yet none of you keeps the law. Why do you **seek** to kill me?” |
| Joh 7:25 | seek | V-PAI-3P | face | 14034, 14314 | 3 | Some of the people of Jerusalem therefore said, “ Is not this the man whom they **seek** to kill? |
| Joh 7:34 | seek | V-FAI-2P | face | - | 3 | You will **seek** me and you will not find me. Where I am you cannot come.” |
| Joh 7:36 | seek | V-FAI-2P | face | - | 3 | What does he mean by saying, ‘You will **seek** me and you will not find me,’ and, ‘ Where I am you cannot come ’?” |
| Joh 8:21 | seek | V-FAI-2P | face | - | 3 | So he said to them again, “ I am going away, and you will **seek** me, and you will die in your sin. Where I am going, you cannot come.” |
| Joh 8:37 | seek | V-PAI-2P | face | - | 3 | I know that you are offspring of Abraham; yet you **seek** to kill me because my word finds no place in you. |
| Joh 8:40 | seek | V-PAI-2P | face | - | 3 | but now you **seek** to kill me, a man who has told you the truth that I heard from God. This is not what Abraham did. |
| Joh 8:50 | seek | V-PAI-1S | face | - | 2 | Yet I do not **seek** my own glory; there is One who seeks it, and he is the judge. |
| Joh 13:33 | seek | V-FAI-2P | face | - | 3 | Little children, yet a little while I am with you. You will **seek** me, and just as I said to the Jews, so now I also say to you, ‘ Where I am going you cannot come.’ |
| Joh 18:4 | seek | V-PAI-2P | face | - | 3 | Then Jesus, knowing all that would happen to him, came forward and said to them, “ Whom do you **seek**?” |
| Joh 18:7 | seek | V-PAI-2P | face | - | 3 | So he asked them again, “ Whom do you **seek**?” And they said, “ Jesus of Nazareth.” |
| Joh 18:8 | seek | V-PAI-2P | face | - | 3 | Jesus answered, “I told you that I am he. So, if you **seek** me, let these men go.” |
| Act 17:27 | seek | V-PAN | face | - | 3 | that they should **seek** God, and perhaps feel their way toward him and find him. Yet he is actually not far from each one of us, |
| Rom 10:20 | seek | V-PAP-DPM | face | 14269 | 3 | Then Isaiah is so bold as to say, “I have been found by those who did not **seek** me; I have shown myself to those who did not ask for me.” |
| Rom 11:3 | seek | V-PAI-3P | face | 16995 | 3 | “ Lord, they have killed your prophets, they have demolished your altars, and I alone am left, and they **seek** my life.” |
| 1Cor 1:22 | seek | V-PAI-3P | face | - | 3 | For Jews demand signs and Greeks **seek** wisdom, |
| 1Cor 7:27 | seek | V-PAM-2S | face | - | 0 | Are you bound to a wife? Do not **seek** to be free. Are you free from a wife? Do not seek a wife. |
| 1Cor 7:27 | seek | V-PAM-2S | face | - | 0 | Are you bound to a wife? Do not **seek** to be free. Are you free from a wife? Do not seek a wife. |
| 1Cor 10:24 | seek | V-PAM-3S | face | - | 2 | Let no one **seek** his own good, but the good of his neighbor. |
| 2Cor 12:14 | seek | V-PAI-1S | face | - | 3 | Here for the third time I am ready to come to you. And I will not be a burden, for I **seek** not what is yours but you. For children are not obligated to save up for their parents, but parents for their children. |
| 2Cor 13:3 | seek | V-PAI-2P | face | - | 3 | since you **seek** proof that Christ is speaking in me. He is not weak in dealing with you, but is powerful among you. |
| Phili 2:21 | seek | V-PAI-3P | face | 19249 | 3 | For they all **seek** their own interests, not those of Jesus Christ. |
| Col 3:1 | seek | V-PAM-2P | face | - | 3 | If then you have been raised with Christ, **seek** the things that are above, where Christ is, seated at the right hand of God. |
| 1Th 2:6 | seek | V-PAP-NPM | face | - | 3 | Nor did we **seek** glory from people, whether from you or from others, though we could have made demands as apostles of Christ. |
| 1Pe 3:11 | seek | V-AAM-3S | face | - | 3 | let him turn away from evil and do good; let him **seek** peace and pursue it. |
| Rev 9:6 | seek | V-FAI-3P | face | - | 3 | And in those days people will **seek** death and will not find it. They will long to die, but death will flee from them. |
| Rom 2:7 | seek for | V-PAP-DPM | face | - | 3 | to those who by patience in well-doing **seek for** glory and honor and immortality, he will give eternal life; |
| Mat 12:43 | seeking | V-PAP-NSN | face | 17129, 17175 | 3 | “ When the unclean spirit has gone out of a person, it passes through waterless places **seeking** rest, but finds none. |
| Mat 21:46 | seeking | V-PAP-NPM | face | 12658 | 3 | And although they were **seeking** to arrest him, they feared the crowds, because they held him to be a prophet. |
| Mat 26:59 | seeking | V-IAI-3P | face | - | 3 | Now the chief priests and the whole council were **seeking** false testimony against Jesus that they might put him to death, |
| Mar 3:32 | seeking | V-PAI-3P | face | - | 3 | And a crowd was sitting around him, and they said to him, “ Your mother and your brothers are outside, **seeking** you.” |
| Mar 8:11 | seeking | V-PAP-NPM | face | - | 3 | The Pharisees came and began to argue with him, **seeking** from him a sign from heaven to test him. |
| Mar 11:18 | seeking | V-IAI-3P | face | - | 3 | And the chief priests and the scribes heard it and were **seeking** a way to destroy him, for they feared him, because all the crowd was astonished at his teaching. |
| Mar 12:12 | seeking | V-IAI-3P | face | - | 2 | And they were **seeking** to arrest him but feared the people, for they perceived that he had told the parable against them. So they left him and went away. |
| Mar 14:1 | seeking | V-IAI-3P | face | - | 3 | It was now two days before the Passover and the Feast of Unleavened Bread. And the chief priests and the scribes were **seeking** how to arrest him by stealth and kill him, |
| Mar 14:55 | seeking | V-IAI-3P | face | - | 3 | Now the chief priests and the whole council were **seeking** testimony against Jesus to put him to death, but they found none. |
| Luk 5:18 | seeking | V-IAI-3P | face | - | 3 | And behold, some men were bringing on a bed a man who was paralyzed, and they were **seeking** to bring him in and lay him before Jesus, |
| Luk 11:16 | seeking | V-IAI-3P | face | - | 3 | while others, to test him, kept **seeking** from him a sign from heaven. |
| Luk 11:24 | seeking | V-PAP-NSN | face | 17129 | 3 | “ When the unclean spirit has gone out of a person, it passes through waterless places **seeking** rest, and finding none it says, ‘I will return to my house from which I came.’ |
| Luk 13:6 | seeking | V-PAP-NSM | silence | - | 3 | And he told this parable: “ A man had a fig tree planted in his vineyard, and he came **seeking** fruit on it and found none. |
| Luk 13:7 | seeking | V-PAP-NSM | silence | - | 2 | And he said to the vinedresser, ‘ Look, for three years now I have come **seeking** fruit on this fig tree, and I find none. Cut it down. Why should it use up the ground?’ |
| Luk 19:3 | seeking | V-IAI-3S | face | - | 2 | And he was **seeking** to see who Jesus was, but on account of the crowd he could not, because he was small in stature. |
| Luk 19:47 | seeking | V-IAI-3P | face | - | 3 | And he was teaching daily in the temple. The chief priests and the scribes and the principal men of the people were **seeking** to destroy him, |
| Luk 22:2 | seeking | V-IAI-3P | face | - | 2 | And the chief priests and the scribes were **seeking** how to put him to death, for they feared the people. |
| Joh 1:38 | seeking | V-PAI-2P | face | - | 3 | Jesus turned and saw them following and said to them, “ What are you **seeking**?” And they said to him, “ Rabbi ” ( which means Teacher ), “ where are you staying?” |
| Joh 4:23 | seeking | V-PAI-3S | face | 17114 | 3 | But the hour is coming, and is now here, when the true worshipers will worship the Father in spirit and truth, for the Father is **seeking** such people to worship him. |
| Joh 5:18 | seeking | V-IAI-3P | face | - | 3 | This was why the Jews were **seeking** all the more to kill him, because not only was he breaking the Sabbath, but he was even calling God his own Father, making himself equal with God. |
| Joh 6:24 | seeking | V-PAP-NPM | face | - | 3 | So when the crowd saw that Jesus was not there, nor his disciples, they themselves got into the boats and went to Capernaum, **seeking** Jesus. |
| Joh 6:26 | seeking | V-PAI-2P | face | - | 3 | Jesus answered them, “ Truly, truly, I say to you, you are **seeking** me, not because you saw signs, but because you ate your fill of the loaves. |
| Joh 7:1 | seeking | V-IAI-3P | face | - | 3 | After this Jesus went about in Galilee. He would not go about in Judea, because the Jews were **seeking** to kill him. |
| Joh 7:20 | seeking | V-PAI-3S | face | - | 3 | The crowd answered, “You have a demon! Who is **seeking** to kill you?” |
| Joh 7:30 | seeking | V-IAI-3P | face | - | 3 | So they were **seeking** to arrest him, but no one laid a hand on him, because his hour had not yet come. |
| Joh 11:8 | seeking | V-IAI-3P | face | - | 3 | The disciples said to him, “ Rabbi, the Jews were just now **seeking** to stone you, and are you going there again?” |
| Joh 20:15 | seeking | V-PAI-2S | face | - | 3 | Jesus said to her, “ Woman, why are you weeping? Whom are you **seeking**?” Supposing him to be the gardener, she said to him, “ Sir, if you have carried him away, tell me where you have laid him, and I will take him away.” |
| Act 13:8 | seeking | V-PAP-NSM | face | - | 1 | But Elymas the magician ( for that is the meaning of his name ) opposed them, **seeking** to turn the proconsul away from the faith. |
| Act 13:11 | seeking | V-IAI-3S | silence | - | 3 | And now, behold, the hand of the Lord is upon you, and you will be blind and unable to see the sun for a time.” Immediately mist and darkness fell upon him, and he went about **seeking** people to lead him by the hand. |
| Act 17:5 | seeking | V-IAI-3P | face | - | 3 | But the Jews were jealous, and taking some wicked men of the rabble, they formed a mob, set the city in an uproar, and attacked the house of Jason, **seeking** to bring them out to the crowd. |
| Act 21:31 | seeking | V-PAP-GPM | face | - | 3 | And as they were **seeking** to kill him, word came to the tribune of the cohort that all Jerusalem was in confusion. |
| Act 27:30 | seeking | V-PAP-GPM | face | - | 3 | And as the sailors were **seeking** to escape from the ship, and had lowered the ship’s boat into the sea under pretense of laying out anchors from the bow, |
| Rom 10:3 | seeking | V-PAP-NPM | face | - | 3 | For, being ignorant of the righteousness of God, and **seeking** to establish their own, they did not submit to God’s righteousness. |
| 1Cor 10:33 | seeking | V-PAP-NSM | face | - | 3 | just as I try to please everyone in everything I do, not **seeking** my own advantage, but that of many, that they may be saved. |
| 1Pe 5:8 | seeking | V-PAP-NSM | use | - | 3 | Be sober-minded; be watchful. Your adversary the devil prowls around like a roaring lion, **seeking** someone to devour. |
| Mat 7:8 | seeks | V-PAP-NSM | face | 20586, 20587, 20594 | 3 | For everyone who asks receives, and the one who **seeks** finds, and to the one who knocks it will be opened. |
| Luk 11:10 | seeks | V-PAP-NSM | face | - | 3 | For everyone who asks receives, and the one who **seeks** finds, and to the one who knocks it will be opened. |
| Luk 17:33 | seeks | V-AAS-3S | face | 17024, 17125 | 2 | Whoever **seeks** to preserve his life will lose it, but whoever loses his life will keep it. |
| Joh 7:4 | seeks | V-PAI-3S | face | - | 2 | For no one works in secret if he **seeks** to be known openly. If you do these things, show yourself to the world.” |
| Joh 7:18 | seeks | V-PAI-3S | face | - | 0 | The one who speaks on his own authority **seeks** his own glory; but the one who seeks the glory of him who sent him is true, and in him there is no falsehood. |
| Joh 7:18 | seeks | V-PAP-NSM | face | - | 0 | The one who speaks on his own authority **seeks** his own glory; but the one who seeks the glory of him who sent him is true, and in him there is no falsehood. |
| Joh 8:50 | seeks | V-PAP-NSM | face | - | 2 | Yet I do not seek my own glory; there is One who **seeks** it, and he is the judge. |
| Mat 2:20 | sought | V-PAP-NPM | face | 17122 | 3 | saying, “ Rise, take the child and his mother and go to the land of Israel, for those who **sought** the child’s life are dead.” |
| Mat 26:16 | sought | V-IAI-3S | face | - | 3 | And from that moment he **sought** an opportunity to betray him. |
| Mar 14:11 | sought | V-IAI-3S | face | - | 3 | And when they heard it, they were glad and promised to give him money. And he **sought** an opportunity to betray him. |
| Luk 4:42 | sought | V-IAI-3P | face | - | 3 | And when it was day, he departed and went into a desolate place. And the people **sought** him and came to him, and would have kept him from leaving them, |
| Luk 6:19 | sought | V-IAI-3P | face | - | 3 | And all the crowd **sought** to touch him, for power came out from him and healed them all. |
| Luk 9:9 | sought | V-IAI-3S | face | 19240 | 2 | Herod said, “ John I beheaded, but who is this about whom I hear such things?” And he **sought** to see him. |
| Luk 20:19 | sought | V-AAI-3P | face | - | 2 | The scribes and the chief priests **sought** to lay hands on him at that very hour, for they perceived that he had told this parable against them, but they feared the people. |
| Luk 22:6 | sought | V-IAI-3S | face | - | 3 | So he consented and **sought** an opportunity to betray him to them in the absence of a crowd. |
| Joh 10:39 | sought | V-IAI-3P | face | - | 3 | Again they **sought** to arrest him, but he escaped from their hands. |
| Joh 19:12 | sought | V-IAI-3S | face | 18835 | 3 | From then on Pilate **sought** to release him, but the Jews cried out, “ If you release this man, you are not Caesar’s friend. Everyone who makes himself a king opposes Caesar.” |
| Act 16:10 | sought | V-AAI-1P | face | - | 1 | And when Paul had seen the vision, immediately we **sought** to go on into Macedonia, concluding that God had called us to preach the gospel to them. |

### 3.4 H1875 דָּרַשׁ da.rash "to seek": 83 own occurrences in 80 verses

- **Meaning as stored:** Hebrew; native word דָּרַשׁ, transliteration da.rash; STEP gloss "to seek"; sense head "to seek" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1875):** to resort to, seek, seek with care, enquire, require.
- **Related terms (1):** H4097 mid.rash "story".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 167; verses STEP attests 152; verse_lexical rows the parse found 164.

- **Carried by the member words:** seek (49), sought (14), search (4), seeking (4), seeks (4), searches (3), searched (2), search for (1), seek out (1), sought out (1).
- **Engagement of these occurrences:** face 69, use 8, silence 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 4:29 | search | HVqi2ms | face | 17106 | 6 | But from there you will seek the Lord your God and you will find him, if you **search** after him with all your heart and with all your soul. |
| 1Ch 26:31 | search | HVNp3cp | silence | - | 4 | Of the Hebronites, Jerijah was chief of the Hebronites of whatever genealogy or fathers’ houses. (In the fortieth year of David’s reign **search** was made and men of great ability among them were found at Jazer in Gilead.) |
| Eze 34:6 | search | HVqrmsa | use | - | 4 | they wandered over all the mountains and on every high hill. My sheep were scattered over all the face of the earth, with none to **search** or seek for them. |
| Eze 34:11 | search | HVqq1cs | use | - | 4 | “ For thus says the Lord God: Behold, I, I myself will **search** for my sheep and will seek them out. |
| Job 10:6 | search for | HVqi2ms | face | - | 4 | that you seek out my iniquity and **search for** my sin, |
| Judg 6:29 | searched | HVqw3mp | silence | - | 4 | And they said to one another, “ Who has done this thing?” And after they had **searched** and inquired, they said, “ Gideon the son of Joash has done this thing.” |
| Eze 34:8 | searched | HVqp3cp | use | - | 4 | As I live, declares the Lord God, surely because my sheep have become a prey, and my sheep have become food for all the wild beasts, since there was no shepherd, and because my shepherds have not **searched** for my sheep, but the shepherds have fed themselves, and have not fed my sheep, |
| 1Ch 28:9 | searches | HVqrmsa | use | 16318, 17057, 19501, 20019, 20455, 20498 | 1 | “And you, Solomon my son, know the God of your father and serve him with a whole heart and with a willing mind, for the Lord **searches** all hearts and understands every plan and thought. If you seek him, he will be found by you, but if you forsake him, he will cast you off forever. |
| Job 39:8 | searches | HVqi3ms | silence | - | 3 | He ranges the mountains as his pasture, and he **searches** after every green thing. |
| Pro 11:27 | searches | HVqrmsa | face | - | 4 | Whoever diligently seeks good seeks favor, but evil comes to him who **searches** for it. |
| Deu 12:5 | seek | HVqi2mp | use | - | 2 | But you shall **seek** the place that the Lord your God will choose out of all your tribes to put his name and make his habitation there. There you shall go, |
| Deu 23:6 | seek | HVqi2ms | face | - | 3 | You shall not **seek** their peace or their prosperity all your days forever. |
| 1Ch 10:14 | seek | HVqp3ms | face | 18537 | 6 | He did not **seek** guidance from the Lord. Therefore the Lord put him to death and turned the kingdom over to David the son of Jesse. |
| 1Ch 13:3 | seek | HVqp1cp | face | - | 2 | Then let us bring again the ark of our God to us, for we did not **seek** it in the days of Saul.” |
| 1Ch 15:13 | seek | HVqp1cp | face | - | 3 | Because you did not carry it the first time, the Lord our God broke out against us, because we did not **seek** him according to the rule.” |
| 1Ch 16:11 | seek | HVqv2mp | face | - | 3 | **Seek** the Lord and his strength; seek his presence continually! |
| 1Ch 22:19 | seek | HVqcc | face | 17107 | 9 | Now set your mind and heart to **seek** the Lord your God. Arise and build the sanctuary of the Lord God, so that the ark of the covenant of the Lord and the holy vessels of God may be brought into a house built for the name of the Lord.” |
| 1Ch 28:9 | seek | HVqi2ms | face | 20345 | 6 | “And you, Solomon my son, know the God of your father and serve him with a whole heart and with a willing mind, for the Lord searches all hearts and understands every plan and thought. If you **seek** him, he will be found by you, but if you forsake him, he will cast you off forever. |
| 2Ch 12:14 | seek | HVqcc | face | 13082, 14102, 14106, 14576, 14578, 15342, 17107, 19166 | 4 | And he did evil, for he did not set his heart to **seek** the Lord. |
| 2Ch 14:4 | seek | HVqcc | face | - | 3 | and commanded Judah to **seek** the Lord, the God of their fathers, and to keep the law and the commandment. |
| 2Ch 15:2 | seek | HVqi2mp | face | - | 3 | and he went out to meet Asa and said to him, “ Hear me, Asa, and all Judah and Benjamin: The Lord is with you while you are with him. If you **seek** him, he will be found by you, but if you forsake him, he will forsake you. |
| 2Ch 15:12 | seek | HVqcc | face | 16380, 17106 | 11 | And they entered into a covenant to **seek** the Lord, the God of their fathers, with all their heart and with all their soul, |
| 2Ch 15:13 | seek | HVqi3ms | face | - | 4 | but that whoever would not **seek** the Lord, the God of Israel, should be put to death, whether young or old, man or woman. |
| 2Ch 16:12 | seek | HVqp3ms | face | 14191 | 4 | In the thirty-ninth year of his reign Asa was diseased in his feet, and his disease became severe. Yet even in his disease he did not **seek** the Lord, but sought help from physicians. |
| 2Ch 17:3 | seek | HVqp3ms | face | - | 3 | The Lord was with Jehoshaphat, because he walked in the earlier ways of his father David. He did not **seek** the Baals, |
| 2Ch 19:3 | seek | HVqcc | face | 13963, 14589, 14593, 14893, 17107, 18135 | 4 | Nevertheless, some good is found in you, for you destroyed the Asheroth out of the land, and have set your heart to **seek** God.” |
| 2Ch 20:3 | seek | HVqcc | face | 12662 | 7 | Then Jehoshaphat was afraid and set his face to **seek** the Lord, and proclaimed a fast throughout all Judah. |
| 2Ch 26:5 | seek | HVqcc | face | - | 7 | He set himself to **seek** God in the days of Zechariah, who instructed him in the fear of God, and as long as he sought the Lord, God made him prosper. |
| 2Ch 30:19 | seek | HVqcc | face | 16647, 17107 | 5 | who sets his heart to **seek** God, the Lord, the God of his fathers, even though not according to the sanctuary’s rules of cleanness.” |
| 2Ch 34:3 | seek | HVqcc | face | - | 4 | For in the eighth year of his reign, while he was yet a boy, he began to **seek** the God of David his father, and in the twelfth year he began to purge Judah and Jerusalem of the high places, the Asherim, and the carved and the metal images. |
| Ezr 9:12 | seek | HVqi2mp | face | - | 3 | Therefore do not give your daughters to their sons, neither take their daughters for your sons, and never **seek** their peace or prosperity, that you may be strong and eat the good of the land and leave it for an inheritance to your children forever.’ |
| Job 3:4 | seek | HVqj3ms | use | - | 3 | Let that day be darkness! May God above not **seek** it, nor light shine upon it. |
| Job 5:8 | seek | HVqi1cs | face | - | 3 | “As for me, I would **seek** God, and to God would I commit my cause, |
| Psa 9:10 | seek | HVqrmpc | face | - | 3 | And those who know your name put their trust in you, for you, O Lord, have not forsaken those who **seek** you. |
| Psa 10:4 | seek | HVqi3ms | face | 12895, 15117, 15266 | 9 | In the pride of his face the wicked does not **seek** him; all his thoughts are, “There is no God.” |
| Psa 14:2 | seek | HVqrmsa | face | - | 2 | The Lord looks down from heaven on the children of man, to see if there are any who understand, who **seek** after God. |
| Psa 22:26 | seek | HVqrmpc | face | 15384, 16712, 17109 | 3 | The afflicted shall eat and be satisfied; those who **seek** him shall praise the Lord! May your hearts live forever! |
| Psa 24:6 | seek | HVqrmpc | face | - | 3 | Such is the generation of those who **seek** him, who seek the face of the God of Jacob. Selah |
| Psa 34:10 | seek | HVqrmpc | face | 17873 | 3 | The young lions suffer want and hunger; but those who **seek** the Lord lack no good thing. |
| Psa 38:12 | seek | HVqrmpc | face | 16982, 16995 | 0 | Those who **seek** my life lay their snares; those who seek my hurt speak of ruin and meditate treachery all day long. |
| Psa 53:2 | seek | HVqrmsa | face | - | 2 | God looks down from heaven on the children of man to see if there are any who understand, who **seek** after God. |
| Psa 69:32 | seek | HVqrmpc | face | 15384, 16052, 16712, 17109 | 3 | When the humble see it they will be glad; you who **seek** God, let your hearts revive. |
| Psa 77:2 | seek | HVqp1cs | face | 17111 | 7 | In the day of my trouble I **seek** the Lord; in the night my hand is stretched out without wearying; my soul refuses to be comforted. |
| Psa 105:4 | seek | HVqv2mp | face | - | 3 | **Seek** the Lord and his strength; seek his presence continually! |
| Psa 119:2 | seek | HVqi3mp | face | 16486, 17106 | 4 | Blessed are those who keep his testimonies, who **seek** him with their whole heart, |
| Psa 119:10 | seek | HVqp1cs | face | 17106 | 3 | With my whole heart I **seek** you; let me not wander from your commandments! |
| Psa 119:155 | seek | HVqp3cp | face | - | 3 | Salvation is far from the wicked, for they do not **seek** your statutes. |
| Ecc 1:13 | seek | HVqcc | face | 16555, 17112, 17236 | 3 | And I applied my heart to **seek** and to search out by wisdom all that is done under heaven. It is an unhappy business that God has given to the children of man to be busy with. |
| Isa 1:17 | seek | HVqv2mp | face | - | 4 | learn to do good; **seek** justice, correct oppression; bring justice to the fatherless, plead the widow’s cause. |
| Isa 34:16 | seek | HVqv2mp | use | 17130 | 3 | **Seek** and read from the book of the Lord: Not one of these shall be missing; none shall be without her mate. For the mouth of the Lord has commanded, and his Spirit has gathered them. |
| Isa 55:6 | seek | HVqv2mp | face | - | 5 | “ **Seek** the Lord while he may be found; call upon him while he is near; |
| Isa 58:2 | seek | HVqi3mp | face | 17632, 19957 | 2 | Yet they **seek** me daily and delight to know my ways, as if they were a nation that did righteousness and did not forsake the judgment of their God; they ask of me righteous judgments; they delight to draw near to God. |
| Jer 29:7 | seek | HVqv2mp | face | - | 3 | But **seek** the welfare of the city where I have sent you into exile, and pray to the Lord on its behalf, for in its welfare you will find your welfare. |
| Jer 29:13 | seek | HVqi2mp | face | 17106, 19415, 19423 | 6 | You will **seek** me and find me, when you seek me with all your heart. |
| Hos 10:12 | seek | HVqcc | face | - | 3 | Sow for yourselves righteousness; reap steadfast love; break up your fallow ground, for it is the time to **seek** the Lord, that he may come and rain righteousness upon you. |
| Amo 5:4 | seek | HVqv2mp | face | - | 9 | For thus says the Lord to the house of Israel: “ **Seek** me and live; |
| Amo 5:5 | seek | HVqj2mp | face | - | 3 | but do not **seek** Bethel, and do not enter into Gilgal or cross over to Beersheba; for Gilgal shall surely go into exile, and Bethel shall come to nothing.” |
| Amo 5:6 | seek | HVqv2mp | face | - | 5 | **Seek** the Lord and live, lest he break out like fire in the house of Joseph, and it devour, with none to quench it for Bethel, |
| Amo 5:14 | seek | HVqv2mp | face | - | 5 | **Seek** good, and not evil, that you may live; and so the Lord, the God of hosts, will be with you, as you have said. |
| 1Ch 28:8 | seek out | HVqv2mp | face | - | 4 | Now therefore in the sight of all Israel, the assembly of the Lord, and in the hearing of our God, observe and **seek out** all the commandments of the Lord your God, that you may possess this good land and leave it for an inheritance to your children after you forever. |
| 1Ch 10:13 | seeking | HVqcc | face | - | 4 | So Saul died for his breach of faith. He broke faith with the Lord in that he did not keep the command of the Lord, and also consulted a medium, **seeking** guidance. |
| 2Ch 31:21 | seeking | HVqcc | face | 17106 | 3 | And every work that he undertook in the service of the house of God and in accordance with the law and the commandments, **seeking** his God, he did with all his heart, and prospered. |
| Psa 109:10 | seeking | HVqq3cp | silence | - | 4 | May his children wander about and beg, **seeking** food far from the ruins they inhabit! |
| Jer 38:4 | seeking | HVqrmsa | face | - | 4 | Then the officials said to the king, “ Let this man be put to death, for he is weakening the hands of the soldiers who are left in this city, and the hands of all the people, by speaking such words to them. For this man is not **seeking** the welfare of this people, but their harm.” |
| Deu 22:2 | seeks | HVqcc | silence | - | 6 | And if he does not live near you and you do not know who he is, you shall bring it home to your house, and it shall stay with you until your brother **seeks** it. Then you shall restore it to him. |
| Pro 31:13 | seeks | HVqp3fs | silence | - | 4 | She **seeks** wool and flax, and works with willing hands. |
| Isa 16:5 | seeks | HVqrmsa | face | - | 4 | then a throne will be established in steadfast love, and on it will sit in faithfulness in the tent of David one who judges and **seeks** justice and is swift to do righteousness.” |
| Lam 3:25 | seeks | HVqi3fs | face | 17096, 18133 | 4 | The Lord is good to those who wait for him, to the soul who **seeks** him. |
| 2Ch 1:5 | sought | HVqw3ms | face | - | 3 | Moreover, the bronze altar that Bezalel the son of Uri, son of Hur, had made, was there before the tabernacle of the Lord. And Solomon and the assembly **sought** it out. |
| 2Ch 14:7 | sought | HVqp1cp | face | - | 0 | And he said to Judah, “Let us build these cities and surround them with walls and towers, gates and bars. The land is still ours, because we have **sought** the Lord our God. We have sought him, and he has given us peace on every side.” So they built and prospered. |
| 2Ch 14:7 | sought | HVqp1cp | face | - | 0 | And he said to Judah, “Let us build these cities and surround them with walls and towers, gates and bars. The land is still ours, because we have **sought** the Lord our God. We have sought him, and he has given us peace on every side.” So they built and prospered. |
| 2Ch 17:4 | sought | HVqp3ms | face | 15138 | 2 | but **sought** the God of his father and walked in his commandments, and not according to the practices of Israel. |
| 2Ch 22:9 | sought | HVqp3ms | face | 16214, 17106, 19201 | 5 | He searched for Ahaziah, and he was captured while hiding in Samaria, and he was brought to Jehu and put to death. They buried him, for they said, “He is the grandson of Jehoshaphat, who **sought** the Lord with all his heart.” And the house of Ahaziah had no one able to rule the kingdom. |
| 2Ch 25:15 | sought | HVqp2ms | face | - | 4 | Therefore the Lord was angry with Amaziah and sent to him a prophet, who said to him, “ Why have you **sought** the gods of a people who did not deliver their own people from your hand?” |
| 2Ch 26:5 | sought | HVqcc | face | - | 0 | He set himself to seek God in the days of Zechariah, who instructed him in the fear of God, and as long as he **sought** the Lord, God made him prosper. |
| Est 10:3 | sought | HVqrmsa | face | - | 3 | For Mordecai the Jew was second in rank to King Ahasuerus, and he was great among the Jews and popular with the multitude of his brothers, for he **sought** the welfare of his people and spoke peace to all his people. |
| Psa 34:4 | sought | HVqp1cs | face | 12725, 15385 | 6 | I **sought** the Lord, and he answered me and delivered me from all my fears. |
| Psa 78:34 | sought | HVqp3cp | face | - | 1 | When he killed them, they **sought** him; they repented and sought God earnestly. |
| Psa 119:45 | sought | HVqp1cs | face | - | 2 | and I shall walk in a wide place, for I have **sought** your precepts. |
| Psa 119:94 | sought | HVqp1cs | face | - | 2 | I am yours; save me, for I have **sought** your precepts. |
| Isa 65:1 | sought | HVNp1cs | face | 19406 | 4 | I was ready to be **sought** by those who did not ask for me; I was ready to be found by those who did not seek me. I said, “ Here I am, here I am,” to a nation that was not called by my name. |
| Isa 65:10 | sought | HVqp3cp | face | - | 3 | Sharon shall become a pasture for flocks, and the Valley of Achor a place for herds to lie down, for my people who have **sought** me. |
| Isa 62:12 | sought out | HVqsfsa | use | - | 3 | And they shall be called The Holy People, The Redeemed of the Lord; and you shall be called **Sought Out**, A City Not Forsaken. |

### 3.5 G2147 εὑρίσκω heuriskō "to find/meet": 59 own occurrences in 57 verses

- **Meaning as stored:** Greek; native word εὑρίσκω, transliteration heuriskō; STEP gloss "to find/meet"; sense head "to find/meet" (the code is its own lemma).
- **Related terms (1):** G0429 aneuriskō "to find".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 635; verses STEP attests 0; verse_lexical rows the parse found 176.

- **Carried by the member words:** find (48), finds (11).
- **Engagement of these occurrences:** silence 50, use 9.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 7:7 | find | V-FAI-2P | silence | - | 0 | “ Ask, and it will be given to you; seek, and you will **find**; knock, and it will be opened to you. |
| Mat 7:14 | find | V-PAP-NPM | silence | - | 0 | For the gate is narrow and the way is hard that leads to life, and those who **find** it are few. |
| Mat 10:39 | find | V-FAI-3S | silence | - | 0 | Whoever finds his life will lose it, and whoever loses his life for my sake will **find** it. |
| Mat 11:29 | find | V-FAI-2P | use | - | 0 | Take my yoke upon you, and learn from me, for I am gentle and lowly in heart, and you will **find** rest for your souls. |
| Mat 16:25 | find | V-FAI-3S | silence | - | 0 | For whoever would save his life will lose it, but whoever loses his life for my sake will **find** it. |
| Mat 17:27 | find | V-FAI-2S | silence | - | 0 | However, not to give offense to them, go to the sea and cast a hook and take the first fish that comes up, and when you open its mouth you will **find** a shekel. Take that and give it to them for me and for yourself.” |
| Mat 21:2 | find | V-FAI-2P | silence | - | 0 | saying to them, “ Go into the village in front of you, and immediately you will **find** a donkey tied, and a colt with her. Untie them and bring them to me. |
| Mat 22:9 | find | V-2AAS-2P | silence | - | 0 | Go therefore to the main roads and invite to the wedding feast as many as you **find**.’ |
| Mat 24:46 | find | V-FAI-3S | silence | - | 0 | Blessed is that servant whom his master will **find** so doing when he comes. |
| Mar 11:2 | find | V-FAI-2P | silence | - | 0 | and said to them, “ Go into the village in front of you, and immediately as you enter it you will **find** a colt tied, on which no one has ever sat. Untie it and bring it. |
| Mar 11:13 | find | V-FAI-3S | silence | - | 0 | And seeing in the distance a fig tree in leaf, he went to see if he could **find** anything on it. When he came to it, he found nothing but leaves, for it was not the season for figs. |
| Mar 13:36 | find | V-2AAS-3S | silence | - | 0 | lest he come suddenly and **find** you asleep. |
| Luk 2:12 | find | V-FAI-2P | silence | - | 0 | And this will be a sign for you: you will **find** a baby wrapped in swaddling cloths and lying in a manger.” |
| Luk 2:45 | find | V-2AAP-NPM | silence | - | 0 | and when they did not **find** him, they returned to Jerusalem, searching for him. |
| Luk 6:7 | find | V-2AAS-3P | silence | - | 0 | And the scribes and the Pharisees watched him, to see whether he would heal on the Sabbath, so that they might **find** a reason to accuse him. |
| Luk 11:9 | find | V-FAI-2P | silence | - | 0 | And I tell you, ask, and it will be given to you; seek, and you will **find**; knock, and it will be opened to you. |
| Luk 12:43 | find | V-FAI-3S | silence | - | 0 | Blessed is that servant whom his master will **find** so doing when he comes. |
| Luk 13:7 | find | V-PAI-1S | silence | - | 0 | And he said to the vinedresser, ‘ Look, for three years now I have come seeking fruit on this fig tree, and I **find** none. Cut it down. Why should it use up the ground?’ |
| Luk 18:8 | find | V-FAI-3S | use | - | 0 | I tell you, he will give justice to them speedily. Nevertheless, when the Son of Man comes, will he **find** faith on earth? ” |
| Luk 19:30 | find | V-FAI-2P | silence | - | 0 | saying, “ Go into the village in front of you, where on entering you will **find** a colt tied, on which no one has ever yet sat. Untie it and bring it here. |
| Luk 19:48 | find | V-IAI-3P | silence | - | 0 | but they did not **find** anything they could do, for all the people were hanging on his words. |
| Luk 23:4 | find | V-PAI-1S | silence | - | 0 | Then Pilate said to the chief priests and the crowds, “I **find** no guilt in this man.” |
| Luk 23:14 | find | V-2AAI-1S | silence | - | 0 | and said to them, “You brought me this man as one who was misleading the people. And after examining him before you, behold, I did not **find** this man guilty of any of your charges against him. |
| Luk 24:3 | find | V-2AAI-3P | silence | - | 0 | but when they went in they did not **find** the body of the Lord Jesus. |
| Luk 24:23 | find | V-2AAP-NPF | silence | - | 0 | and when they did not **find** his body, they came back saying that they had even seen a vision of angels, who said that he was alive. |
| Joh 7:34 | find | V-FAI-2P | use | - | 0 | You will seek me and you will not **find** me. Where I am you cannot come.” |
| Joh 7:35 | find | V-FAI-1P | silence | - | 0 | The Jews said to one another, “ Where does this man intend to go that we will not **find** him? Does he intend to go to the Dispersion among the Greeks and teach the Greeks? |
| Joh 7:36 | find | V-FAI-2P | use | - | 0 | What does he mean by saying, ‘You will seek me and you will not **find** me,’ and, ‘ Where I am you cannot come ’?” |
| Joh 10:9 | find | V-FAI-3S | silence | - | 0 | I am the door. If anyone enters by me, he will be saved and will go in and out and **find** pasture. |
| Joh 18:38 | find | V-PAI-1S | silence | - | 0 | Pilate said to him, “ What is truth?” After he had said this, he went back outside to the Jews and told them, “ I **find** no guilt in him. |
| Joh 19:4 | find | V-PAI-1S | silence | - | 0 | Pilate went out again and said to them, “ See, I am bringing him out to you that you may know that I **find** no guilt in him.” |
| Joh 19:6 | find | V-PAI-1S | silence | - | 0 | When the chief priests and the officers saw him, they cried out, “ Crucify him, crucify him!” Pilate said to them, “ Take him yourselves and crucify him, for I **find** no guilt in him.” |
| Joh 21:6 | find | V-FAI-2P | silence | - | 0 | He said to them, “ Cast the net on the right side of the boat, and you will **find** some.” So they cast it, and now they were not able to haul it in, because of the quantity of fish. |
| Act 5:22 | find | V-2AAI-3P | silence | - | 0 | But when the officers came, they did not **find** them in the prison, so they returned and reported, |
| Act 7:11 | find | V-IAI-3P | silence | - | 0 | Now there came a famine throughout all Egypt and Canaan, and great affliction, and our fathers could **find** no food. |
| Act 7:46 | find | V-2AAN | use | - | 0 | who found favor in the sight of God and asked to **find** a dwelling place for the God of Jacob. |
| Act 17:6 | find | V-2AAP-NPM | silence | - | 0 | And when they could not **find** them, they dragged Jason and some of the brothers before the city authorities, shouting, “ These men who have turned the world upside down have come here also, |
| Act 23:9 | find | V-PAI-1P | silence | - | 0 | Then a great clamor arose, and some of the scribes of the Pharisees ’ party stood up and contended sharply, “We **find** nothing wrong in this man. What if a spirit or an angel spoke to him?” |
| Act 24:12 | find | V-2AAI-3P | silence | - | 0 | and they did not **find** me disputing with anyone or stirring up a crowd, either in the temple or in the synagogues or in the city. |
| Rom 7:21 | find | V-PAI-1S | use | - | 0 | So I **find** it to be a law that when I want to do right, evil lies close at hand. |
| 2Cor 2:13 | find | V-2AAN | silence | - | 0 | my spirit was not at rest because I did not **find** my brother Titus there. So I took leave of them and went on to Macedonia. |
| 2Cor 9:4 | find | V-2AAS-3P | silence | - | 0 | Otherwise, if some Macedonians come with me and **find** that you are not ready, we would be humiliated —to say nothing of you—for being so confident. |
| 2Cor 12:20 | find | V-2AAS-1S | silence | - | 0 | For I fear that perhaps when I come I may **find** you not as I wish, and that you may find me not as you wish — that perhaps there may be quarreling, jealousy, anger, hostility, slander, gossip, conceit, and disorder. |
| 2Cor 12:20 | find | V-APS-1S | silence | - | 0 | For I fear that perhaps when I come I may **find** you not as I wish, and that you may find me not as you wish — that perhaps there may be quarreling, jealousy, anger, hostility, slander, gossip, conceit, and disorder. |
| 2Ti 1:18 | find | V-2AAN | use | - | 0 | may the Lord grant him to **find** mercy from the Lord on that day!— and you well know all the service he rendered at Ephesus. |
| Heb 4:16 | find | V-2AAS-1P | use | - | 0 | Let us then with confidence draw near to the throne of grace, that we may receive mercy and **find** grace to help in time of need. |
| 2Jo 4 | find | V-RAI-1S | silence | - | 0 | I rejoiced greatly to **find** some of your children walking in the truth, just as we were commanded by the Father. |
| Rev 9:6 | find | V-FAI-3P | silence | - | 0 | And in those days people will seek death and will not **find** it. They will long to die, but death will flee from them. |
| Mat 7:8 | finds | V-PAI-3S | silence | 20588, 20589, 20594 | 0 | For everyone who asks receives, and the one who seeks **finds**, and to the one who knocks it will be opened. |
| Mat 10:39 | finds | V-2AAP-NSM | silence | - | 0 | Whoever **finds** his life will lose it, and whoever loses his life for my sake will find it. |
| Mat 12:43 | finds | V-PAI-3S | use | - | 0 | “ When the unclean spirit has gone out of a person, it passes through waterless places seeking rest, but **finds** none. |
| Mat 12:44 | finds | V-PAI-3S | silence | - | 0 | Then it says, ‘I will return to my house from which I came.’ And when it comes, it **finds** the house empty, swept, and put in order. |
| Mat 18:13 | finds | V-2AAN | silence | - | 0 | And if he **finds** it, truly, I say to you, he rejoices over it more than over the ninety-nine that never went astray. |
| Luk 11:10 | finds | V-PAI-3S | silence | - | 0 | For everyone who asks receives, and the one who seeks **finds**, and to the one who knocks it will be opened. |
| Luk 11:25 | finds | V-PAI-3S | silence | - | 0 | And when it comes, it **finds** the house swept and put in order. |
| Luk 12:37 | finds | V-FAI-3S | silence | - | 0 | Blessed are those servants whom the master **finds** awake when he comes. Truly, I say to you, he will dress himself for service and have them recline at table, and he will come and serve them. |
| Luk 12:38 | finds | V-2AAS-3S | silence | - | 0 | If he comes in the second watch, or in the third, and **finds** them awake, blessed are those servants! |
| Luk 15:4 | finds | V-2AAS-3S | silence | - | 0 | “ What man of you, having a hundred sheep, if he has lost one of them, does not leave the ninety-nine in the open country, and go after the one that is lost, until he **finds** it? |
| Luk 15:8 | finds | V-2AAS-3S | silence | - | 0 | “ Or what woman, having ten silver coins, if she loses one coin, does not light a lamp and sweep the house and seek diligently until she **finds** it? |

### 3.6 G1934 ἐπιζητέω epizēteō "to seek after": 14 own occurrences in 13 verses

- **Meaning as stored:** Greek; native word ἐπιζητέω, transliteration epizēteō; STEP gloss "to seek after"; sense head "to seek after" (the code is its own lemma).
- **Related terms (2):** G1909 epi "upon/to/against"; G2212 zēteō "to seek".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 29; verses STEP attests 13; verse_lexical rows the parse found 14.

- **Carried by the member words:** seek (6), seeking (2), seeks for (2), searched for (1), seek after (1), seeks (1), sought (1).
- **Engagement of these occurrences:** face 13, use 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 12:19 | searched for | V-AAP-NSM | use | - | 3 | And after Herod **searched for** him and did not find him, he examined the sentries and ordered that they should be put to death. Then he went down from Judea to Caesarea and spent time there. |
| Mat 6:32 | seek | V-PAI-3P | face | 19246 | 3 | For the Gentiles **seek** after all these things, and your heavenly Father knows that you need them all. |
| Mar 8:12 | seek | V-PAI-3S | face | 17128 | 3 | And he sighed deeply in his spirit and said, “ Why does this generation **seek** a sign? Truly, I say to you, no sign will be given to this generation.” |
| Act 19:39 | seek | V-PAI-2P | face | - | 6 | But if you **seek** anything further, it shall be settled in the regular assembly. |
| Phili 4:17 | seek | V-PAI-1S | face | - | 0 | Not that I **seek** the gift, but I seek the fruit that increases to your credit. |
| Phili 4:17 | seek | V-PAI-1S | face | - | 0 | Not that I **seek** the gift, but I seek the fruit that increases to your credit. |
| Heb 13:14 | seek | V-PAI-1P | face | - | 12 | For here we have no lasting city, but we **seek** the city that is to come. |
| Luk 12:30 | seek after | V-PAI-3P | face | - | 3 | For all the nations of the world **seek after** these things, and your Father knows that you need them. |
| Rom 11:7 | seeking | V-PAI-3S | face | 19719, 19956, 19991 | 10 | What then? Israel failed to obtain what it was **seeking**. The elect obtained it, but the rest were hardened, |
| Heb 11:14 | seeking | V-PAI-3P | face | - | 8 | For people who speak thus make it clear that they are **seeking** a homeland. |
| Mat 16:4 | seeks | V-PAI-3S | face | - | 20 | An evil and adulterous generation **seeks** for a sign, but no sign will be given to it except the sign of Jonah.” So he left them and departed. |
| Mat 12:39 | seeks for | V-PAI-3S | face | - | 8 | But he answered them, “An evil and adulterous generation **seeks for** a sign, but no sign will be given to it except the sign of the prophet Jonah. |
| Luk 11:29 | seeks for | V-PAI-3S | face | - | 5 | When the crowds were increasing, he began to say, “ This generation is an evil generation. It **seeks for** a sign, but no sign will be given to it except the sign of Jonah. |
| Act 13:7 | sought | V-AAI-3S | face | - | 4 | He was with the proconsul, Sergius Paulus, a man of intelligence, who summoned Barnabas and Saul and **sought** to hear the word of God. |

### 3.7 H7836 שָׁחַר sha.char "to seek": 11 own occurrences in 11 verses

- **Meaning as stored:** Hebrew; native word שָׁחַר, transliteration sha.char; STEP gloss "to seek"; sense head "to seek" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7836):** to seek, seek early or earnestly, look early or diligently for.
- **Related terms (6):** H4891 mish.char "dawn"; H7835 sha.char "be black"; H7837 sha.char "dawn"; H7839 sha.cha.rut "dark hair"; H7841 she.char.yah "Shehariah"; H7842 sha.cha.ra.yim "Shaharaim".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** seek (5), seek me diligently (2), earnestly seeks (1), seeking (1), seeks (1), sought (1).
- **Engagement of these occurrences:** face 9, use 1, silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 26:9 | earnestly seeks | HVpi1cs | face | 17004, 17111, 17270, 17271 | 11 | My soul yearns for you in the night; my spirit within me **earnestly seeks** you. For when your judgments are in the earth, the inhabitants of the world learn righteousness. |
| Job 7:21 | seek | HVpq2ms | use | - | 4 | Why do you not pardon my transgression and take away my iniquity? For now I shall lie in the earth; you will **seek** me, but I shall not be.” |
| Job 8:5 | seek | HVpi2ms | face | - | 8 | If you will **seek** God and plead with the Almighty for mercy, |
| Psa 63:1 | seek | HVpi1cs | face | 17111, 17124 | 24 | A Psalm of David, when he was in the wilderness of Judah. O God, you are my God; earnestly I **seek** you; my soul thirsts for you; my flesh faints for you, as in a dry and weary land where there is no water. |
| Pro 7:15 | seek | HVpcc | face | - | 2 | so now I have come out to meet you, to **seek** you eagerly, and I have found you. |
| Hos 5:15 | seek | HVpi3mp | face | - | 17 | I will return again to my place, until they acknowledge their guilt and **seek** my face, and in their distress earnestly seek me. |
| Pro 1:28 | seek me diligently | HVpi3mp | face | - | 7 | Then they will call upon me, but I will not answer; they will **seek me diligently** but will not find me. |
| Pro 8:17 | seek me diligently | HVprmpc | face | - | 18 | I love those who love me, and those who **seek me diligently** find me. |
| Job 24:5 | seeking | HVprmpc | silence | - | 6 | Behold, like wild donkeys in the desert the poor go out to their toil, **seeking** game; the wasteland yields food for their children. |
| Pro 11:27 | seeks | HVqrmsa | face | - | 5 | Whoever diligently **seeks** good seeks favor, but evil comes to him who searches for it. |
| Psa 78:34 | sought | HVpp3cp | face | - | 10 | When he killed them, they **sought** him; they repented and sought God earnestly. |

### 3.8 H2664 חָפַשׂ cha.pha.s "to search": 10 own occurrences in 10 verses

- **Meaning as stored:** Hebrew; native word חָפַשׂ, transliteration cha.pha.s; STEP gloss "to search"; sense head "to search" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2664):** to search, search for, to search out, disguise oneself.
- **Related terms (1):** H2665 che.phe.s "plot".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 23; verses STEP attests 20; verse_lexical rows the parse found 23.

- **Carried by the member words:** search (7), searched (2), searching (1).
- **Engagement of these occurrences:** silence 5, use 3, face 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 23:23 | search | HVpq1cs | silence | - | 0 | See therefore and take note of all the lurking places where he hides, and come back to me with sure information. Then I will go with you. And if he is in the land, I will **search** him out among all the thousands of Judah.” |
| 1Ki 20:6 | search | HVpq3cp | silence | - | 0 | Nevertheless I will send my servants to you tomorrow about this time, and they shall **search** your house and the houses of your servants and lay hands on whatever pleases you and take it away.’” |
| 2Ki 10:23 | search | HVpv2mp | silence | - | 0 | Then Jehu went into the house of Baal with Jehonadab the son of Rechab, and he said to the worshipers of Baal, “ **Search**, and see that there is no servant of the Lord here among you, but only the worshipers of Baal.” |
| Psa 77:6 | search | HVpw3ms | face | - | 0 | I said, “Let me remember my song in the night; let me meditate in my heart.” Then my spirit made a diligent **search**: |
| Pro 2:4 | search | HVqi2ms | face | - | 0 | if you seek it like silver and **search** for it as for hidden treasures, |
| Amo 9:3 | search | HVpi1cs | use | - | 0 | If they hide themselves on the top of Carmel, from there I will **search** them out and take them; and if they hide from my sight at the bottom of the sea, there I will command the serpent, and it shall bite them. |
| Zep 1:12 | search | HVpi1cs | use | - | 0 | At that time I will **search** Jerusalem with lamps, and I will punish the men who are complacent, those who say in their hearts, ‘The Lord will not do good, nor will he do ill.’ |
| Gen 31:35 | searched | HVpw3ms | silence | - | 0 | And she said to her father, “Let not my lord be angry that I cannot rise before you, for the way of women is upon me.” So he **searched** but did not find the household gods. |
| Gen 44:12 | searched | HVpw3ms | silence | - | 0 | And he **searched**, beginning with the eldest and ending with the youngest. And the cup was found in Benjamin’s sack. |
| Pro 20:27 | searching | HVqrmsa | use | - | 0 | The spirit of man is the lamp of the Lord, **searching** all his innermost parts. |

### 3.9 H2713 חָקַר cha.qar "to search": 8 own occurrences in 8 verses

- **Meaning as stored:** Hebrew; native word חָקַר, transliteration cha.qar; STEP gloss "to search"; sense head "to search" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2713):** to search, search for, search out, examine, investigate.
- **Related terms (2):** H2714 che.qer "search"; H4278 mech.qar "range".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 27; verses STEP attests 26; verse_lexical rows the parse found 27.

- **Carried by the member words:** search (6), searched (1), sought (1).
- **Engagement of these occurrences:** silence 4, use 3, face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Sa 10:3 | search | HVqcc | silence | - | 0 | But the princes of the Ammonites said to Hanun their lord, “Do you think, because David has sent comforters to you, that he is honoring your father? Has not David sent his servants to you to **search** the city and to spy it out and to overthrow it?” |
| 1Ch 19:3 | search | HVqcc | silence | - | 0 | But the princes of the Ammonites said to Hanun, “Do you think, because David has sent comforters to you, that he is honoring your father? Have not his servants come to you to **search** and to overthrow and to spy out the land?” |
| Psa 139:23 | search | HVqv2ms | use | - | 0 | **Search** me, O God, and know my heart! Try me and know my thoughts! |
| Pro 25:2 | search | HVqcc | face | - | 0 | It is the glory of God to conceal things, but the glory of kings is to **search** things out. |
| Jer 17:10 | search | HVqrmsa | use | - | 0 | “ I the Lord **search** the heart and test the mind, to give every man according to his ways, according to the fruit of his deeds.” |
| Eze 39:14 | search | HVqi3mp | silence | - | 0 | They will set apart men to travel through the land regularly and bury those travelers remaining on the face of the land, so as to cleanse it. At the end of seven months they will make their **search**. |
| Psa 139:1 | searched | HVqp2ms | use | - | 0 | To the choirmaster. A Psalm of David. O Lord, you have **searched** me and known me! |
| 2Ch 4:18 | sought | HVNp3ms | silence | - | 0 | Solomon made all these things in great quantities, for the weight of the bronze was not **sought**. |

### 3.10 H7912 שְׁכַח she.khach "to find": 6 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word שְׁכַח, transliteration she.khach; STEP gloss "to find"; sense head "to find" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7912):** to find.
- **Related terms (2):** H7911 sha.khach "to forget"; H7913 sha.khe.ach "forgetful".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 18; verses STEP attests 0; verse_lexical rows the parse found 17.

- **Carried by the member words:** find (6).
- **Engagement of these occurrences:** silence 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ezr 4:15 | find | AVhu2ms | silence | - | 0 | in order that search may be made in the book of the records of your fathers. You will **find** in the book of the records and learn that this city is a rebellious city, hurtful to kings and provinces, and that sedition was stirred up in it from of old. That was why this city was laid waste. |
| Ezr 7:16 | find | AVhi2ms | silence | - | 0 | with all the silver and gold that you shall **find** in the whole province of Babylonia, and with the freewill offerings of the people and the priests, vowed willingly for the house of their God that is in Jerusalem. |
| Dan 6:4 | find | AVhcc | silence | - | 0 | Then the high officials and the satraps sought to **find** a ground for complaint against Daniel with regard to the kingdom, but they could find no ground for complaint or any fault, because he was faithful, and no error or fault was found in him. |
| Dan 6:4 | find | AVhcc | silence | - | 0 | Then the high officials and the satraps sought to **find** a ground for complaint against Daniel with regard to the kingdom, but they could find no ground for complaint or any fault, because he was faithful, and no error or fault was found in him. |
| Dan 6:5 | find | AVhi1cp | silence | - | 0 | Then these men said, “We shall not **find** any ground for complaint against this Daniel unless we find it in connection with the law of his God.” |
| Dan 6:5 | find | AVhp1cp | silence | - | 0 | Then these men said, “We shall not **find** any ground for complaint against this Daniel unless we find it in connection with the law of his God.” |

### 3.11 G1567 ἐκζητέω ekzēteō "to seek out": 5 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word ἐκζητέω, transliteration ekzēteō; STEP gloss "to seek out"; sense head "to seek out" (the code is its own lemma).
- **Related terms (2):** G1537 ek "out from"; G2212 zēteō "to seek".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 125; verses STEP attests 7; verse_lexical rows the parse found 7.

- **Carried by the member words:** seek (2), searched (1), seeks for (1), sought (1).
- **Engagement of these occurrences:** face 5.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Pe 1:10 | searched | V-AAI-3P | face | - | 4 | Concerning this salvation, the prophets who prophesied about the grace that was to be yours **searched** and inquired carefully, |
| Act 15:17 | seek | V-AAS-3P | face | - | 9 | that the remnant of mankind may **seek** the Lord, and all the Gentiles who are called by my name, says the Lord, who makes these things |
| Heb 11:6 | seek | V-PAP-DPM | face | - | 25 | And without faith it is impossible to please him, for whoever would draw near to God must believe that he exists and that he rewards those who **seek** him. |
| Rom 3:11 | seeks for | V-PAP-NSM | face | - | 15 | no one understands; no one **seeks for** God. |
| Heb 12:17 | sought | V-AAP-NSM | face | - | 18 | For you know that afterward, when he desired to inherit the blessing, he was rejected, for he found no chance to repent, though he **sought** it with tears. |

### 3.12 G2045 ἐρευνάω ereunaō "to look for/into": 5 own occurrences in 5 verses

- **Meaning as stored:** Greek; native word ἐρευνάω, transliteration ereunaō; STEP gloss "to look for/into"; sense head "to look for/into" (the code is its own lemma).
- **Related terms (2):** G1830 exereunaō "to search out"; G2065 erōtaō "to ask".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 18; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** searches (3), search (2).
- **Engagement of these occurrences:** use 4, silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 5:39 | search | V-PAI-2P | use | - | 0 | You **search** the Scriptures because you think that in them you have eternal life; and it is they that bear witness about me, |
| Joh 7:52 | search | V-AAM-2S | silence | - | 0 | They replied, “ Are you from Galilee too? **Search** and see that no prophet arises from Galilee.” |
| Rom 8:27 | searches | V-PAP-NSM | use | - | 0 | And he who **searches** hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God. |
| 1Cor 2:10 | searches | V-PAI-3S | use | - | 0 | these things God has revealed to us through the Spirit. For the Spirit **searches** everything, even the depths of God. |
| Rev 2:23 | searches | V-PAP-NSM | use | - | 0 | and I will strike her children dead. And all the churches will know that I am he who **searches** mind and heart, and I will give to each of you according to your works. |

### 3.13 H1240 בְּקַר be.qar "to enquire": 4 own occurrences in 4 verses

- **Meaning as stored:** Hebrew; native word בְּקַר, transliteration be.qar; STEP gloss "to enquire"; sense head "to enquire" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1240):** to seek, enquire.
- **Related terms (6):** H1239 ba.qar "to enquire"; H1247G bar "son: descendant/people"; H1247H bar "son: young animal"; H1247I bar "son: type of"; H1247J bar "son: son"; H1247L bar "son: aged".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 5; verse_lexical rows the parse found 5.

- **Carried by the member words:** search (4).
- **Engagement of these occurrences:** silence 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ezr 4:15 | search | AVpi3ms | silence | - | 0 | in order that **search** may be made in the book of the records of your fathers. You will find in the book of the records and learn that this city is a rebellious city, hurtful to kings and provinces, and that sedition was stirred up in it from of old. That was why this city was laid waste. |
| Ezr 4:19 | search | AVpp3mp | silence | - | 0 | And I made a decree, and **search** has been made, and it has been found that this city from of old has risen against kings, and that rebellion and sedition have been made in it. |
| Ezr 5:17 | search | AVMi3ms | silence | - | 0 | Therefore, if it seems good to the king, let **search** be made in the royal archives there in Babylon, to see whether a decree was issued by Cyrus the king for the rebuilding of this house of God in Jerusalem. And let the king send us his pleasure in this matter.” |
| Ezr 6:1 | search | AVpp3mp | silence | - | 0 | Then Darius the king made a decree, and **search** was made in Babylonia, in the house of the archives where the documents were stored. |

### 3.14 G4328 προσδοκάω prosdokaō "to look for": 3 own occurrences in 3 verses

- **Meaning as stored:** Greek; native word προσδοκάω, transliteration prosdokaō; STEP gloss "to look for"; sense head "to look for" (the code is its own lemma).
- **Related terms (2):** G4314 pros "to/with"; G4329 prosdokia "expectation".
- **Clusters (cluster_strong):** M68 Hope & Waiting (heuristic).
- **Counts, three measures as stored:** STEP token count 20; verses STEP attests 0; verse_lexical rows the parse found 16.

- **Carried by the member words:** look for (3).
- **Engagement of these occurrences:** face 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 11:3 | look for | V-PAI-1P | face | - | 0 | and said to him, “ Are you the one who is to come, or shall we **look for** another?” |
| Luk 7:19 | look for | V-PAI-1P | face | - | 0 | calling two of his disciples to him, sent them to the Lord, saying, “ Are you the one who is to come, or shall we **look for** another?” |
| Luk 7:20 | look for | V-PAI-1P | face | - | 0 | And when the men had come to him, they said, “ John the Baptist has sent us to you, saying, ‘ Are you the one who is to come, or shall we **look for** another?’” |

### 3.15 H0935G בּוֹא bo "to come [in]: come": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word בּוֹא, transliteration bo; STEP gloss "to come [in]: come"; sense head "come/go in".
- **Senses (first level of the meaning tree of the lemma H0935):** to go in, enter, come, go, come in.
- **Related terms (14):** H0872 bi.ah "entrance"; H0935H le.vo "Lebo-[Hamath]"; H0935I bo "to come [in]: towards"; H0935J bo "to come [in]: advanced"; H0935K bo "to come [in]: [sun]set"; H0935L bo "to come [in]: marry"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 1970; verses STEP attests 1753; verse_lexical rows the parse found 1938.

- **Carried by the member words:** come upon (3).
- **Engagement of these occurrences:** use 2, silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Sa 19:7 | come upon | HVqp3fs | silence | - | 0 | Now therefore arise, go out and speak kindly to your servants, for I swear by the Lord, if you do not go, not a man will stay with you this night, and this will be worse for you than all the evil that has **come upon** you from your youth until now.” |
| 2Ch 13:13 | come upon | HVqcc | use | - | 0 | Jeroboam had sent an ambush around to **come upon** them from behind. Thus his troops were in front of Judah, and the ambush was behind them. |
| 2Ch 32:26 | come upon | HVqp3ms | use | - | 0 | But Hezekiah humbled himself for the pride of his heart, both he and the inhabitants of Jerusalem, so that the wrath of the Lord did not **come upon** them in the days of Hezekiah. |

### 3.16 H1156 בְּעָא be.a "to ask": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word בְּעָא, transliteration be.a; STEP gloss "to ask"; sense head "to ask" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1156):** to ask, seek, request, desire, pray, make petition.
- **Related terms (4):** H1158 ba.ah "to enquire"; H1159 ba.u "petition"; H1169 be.el "commander"; H1236 biq.a "plain".
- **Clusters (cluster_strong):** M21 Fasting & Piety (None).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** sought (2), seek (1).
- **Engagement of these occurrences:** face 1, use 1, silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 2:18 | seek | AVqcc | face | - | 0 | and told them to **seek** mercy from the God of heaven concerning this mystery, so that Daniel and his companions might not be destroyed with the rest of the wise men of Babylon. |
| Dan 2:13 | sought | AVqp3mp | use | 13579 | 0 | So the decree went out, and the wise men were about to be killed; and they **sought** Daniel and his companions, to kill them. |
| Dan 4:36 | sought | AVpi3mp | silence | - | 0 | At the same time my reason returned to me, and for the glory of my kingdom, my majesty and splendor returned to me. My counselors and my lords **sought** me, and I was established in my kingdom, and still more greatness was added to me. |

### 3.17 H2470B חָלָה cha.lah "to beg": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word חָלָה, transliteration cha.lah; STEP gloss "to beg"; sense head "to beg" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2470):** to be or become weak, be or become sick, be or become diseased, be or ... (cut; the whole text is in the workbook).
- **Related terms (9):** H2456 cha.la "be sick"; H2470A cha.lah "be weak: weak"; H2470H cha.lah "be weak: ill"; H2470I cha.lah "be weak: grieved"; H2483 cho.li "sickness"; H4245A ma.cha.leh "sickness"; more in the workbook.
- **Clusters (cluster_strong):** M21 Fasting & Piety (None).
- **Counts, three measures as stored:** STEP token count 16; verses STEP attests 15; verse_lexical rows the parse found 16.

- **Carried by the member words:** seek (2), sought (1).
- **Engagement of these occurrences:** face 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 45:12 | seek | HVpi3mp | face | - | 0 | The people of Tyre will **seek** your favor with gifts, the richest of the people. |
| Pro 19:6 | seek | HVpi3mp | face | - | 0 | Many **seek** the favor of a generous man, and everyone is a friend to a man who gives gifts. |
| 2Ki 13:4 | sought | HVpw3ms | face | 14093, 14563 | 0 | Then Jehoahaz **sought** the favor of the Lord, and the Lord listened to him, for he saw the oppression of Israel, how the king of Syria oppressed them. |

### 3.18 H2896A טוֹב tov "pleasant": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word טוֹב, transliteration tov; STEP gloss "pleasant"; sense head "pleasant" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2896):** good, pleasant, agreeable.
- **Related terms (11):** H2869 tav "fine"; H2895 tov "be pleasing"; H2896B tov "good"; H2896C to.vah "welfare"; H2897 tov "Tob"; H2898 tuv "goodness"; more in the workbook.
- **Clusters (cluster_strong):** M18 Desire & Longing (heuristic).
- **Counts, three measures as stored:** STEP token count 409; verses STEP attests 381; verse_lexical rows the parse found 408.

- **Carried by the member words:** more handsome (1), searches (1), well disposed (1).
- **Engagement of these occurrences:** silence 1, use 1, face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 9:2 | more handsome | HAamsa | silence | - | 0 | And he had a son whose name was Saul, a handsome young man. There was not a man among the people of Israel **more handsome** than he. From his shoulders upward he was taller than any of the people. |
| Job 13:9 | searches | HAamsa | use | - | 0 | Will it be well with you when he **searches** you out? Or can you deceive him, as one deceives a man? |
| 1Sa 20:12 | well disposed | HAamsa | face | - | 0 | And Jonathan said to David, “The Lord, the God of Israel, be witness! When I have sounded out my father, about this time tomorrow, or the third day, behold, if he is **well disposed** toward David, shall I not then send and disclose it to you? |

### 3.19 H8446 תּוּר tur "to spy": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word תּוּר, transliteration tur; STEP gloss "to spy"; sense head "to spy" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H8446):** to seek, search out, spy out, explore.
- **Related terms (2):** H8447 tor "plait"; H8448 tor "border".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 24; verses STEP attests 23; verse_lexical rows the parse found 24.

- **Carried by the member words:** search (2), searched (1).
- **Engagement of these occurrences:** face 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 1:13 | search | HVqcc | face | - | 0 | And I applied my heart to seek and to **search** out by wisdom all that is done under heaven. It is an unhappy business that God has given to the children of man to be busy with. |
| Ecc 7:25 | search | HVqcc | face | - | 0 | I turned my heart to know and to **search** out and to seek wisdom and the scheme of things, and to know the wickedness of folly and the foolishness that is madness. |
| Ecc 2:3 | searched | HVqp1cs | face | - | 0 | I **searched** with my heart how to cheer my body with wine —my heart still guiding me with wisdom —and how to lay hold on folly, till I might see what was good for the children of man to do under heaven during the few days of their life. |

### 3.20 G0327 ἀναζητέω anazēteō "to search": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word ἀναζητέω, transliteration anazēteō; STEP gloss "to search"; sense head "to search" (the code is its own lemma).
- **Related terms (2):** G0303 ana "each"; G2212 zēteō "to seek".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 2; verse_lexical rows the parse found 2.

- **Carried by the member words:** look for (1), search (1).
- **Engagement of these occurrences:** use 1, silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 11:25 | look for | V-AAN | use | - | 0 | So Barnabas went to Tarsus to **look for** Saul, |
| Luk 2:44 | search | V-IAI-3P | silence | - | 0 | but supposing him to be in the group they went a day’s journey, but then they began to **search** for him among their relatives and acquaintances, |

### 3.21 H1239 בָּקַר ba.qar "to enquire": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word בָּקַר, transliteration ba.qar; STEP gloss "to enquire"; sense head "to enquire" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1239):** to seek, enquire, consider.
- **Related terms (7):** H0951 bo.qer "herdsman"; H1230 baq.baq.qar "Bakbakkar"; H1240 be.qar "to enquire"; H1241 ba.qar "cattle"; H1242 bo.qer "morning"; H1243 baq.qa.rah "seeking"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 7; verse_lexical rows the parse found 7.

- **Carried by the member words:** seek (1), seek out (1).
- **Engagement of these occurrences:** silence 1, face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Lev 13:36 | seek | HVpi3ms | silence | - | 0 | then the priest shall examine him, and if the itch has spread in the skin, the priest need not **seek** for the yellow hair; he is unclean. |
| Eze 34:12 | seek out | HVpi1cs | face | - | 0 | As a shepherd seeks out his flock when he is among his sheep that have been scattered, so will I **seek out** my sheep, and I will rescue them from all places where they have been scattered on a day of clouds and thick darkness. |

### 3.22 H7122I קָרָא qa.ra "to encounter: chanced": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word קָרָא, transliteration qa.ra; STEP gloss "to encounter: chanced"; sense head "happen[unexpectedly]".
- **Senses (first level of the meaning tree of the lemma H7122):** to encounter, befall, meet.
- **Related terms (6):** H7121G qa.ra "to call: call to"; H7121H qa.ra "to call: call by"; H7121I qa.ra "to call: call out"; H7121J qa.ra "to call: read out"; H7122G qa.ra "to encounter: meet"; H7122H qa.ra "to encounter: toward".
- **Clusters (cluster_strong):** M37 Firstborn & Foreknowledge (None).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 0; verse_lexical rows the parse found 13.

- **Carried by the member words:** come upon (2).
- **Engagement of these occurrences:** silence 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 13:22 | come upon | HVqp3cp | silence | 16578 | 0 | And if you say in your heart, ‘ Why have these things **come upon** me?’ it is for the greatness of your iniquity that your skirts are lifted up and you suffer violence. |
| Jer 32:23 | come upon | HVhw2ms | silence | - | 0 | And they entered and took possession of it. But they did not obey your voice or walk in your law. They did nothing of all you commanded them to do. Therefore you have made all this disaster **come upon** them. |

### 3.23 G1377 διώκω diōkō "to pursue": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word διώκω, transliteration diōkō; STEP gloss "to pursue"; sense head "to pursue" (the code is its own lemma).
- **Related terms (4):** G1375 diōgmos "persecution"; G1376 diōktēs "persecutor"; G1559 ekdiōkō "to persecute"; G2614 katadiōkō "to seek".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 122; verses STEP attests 44; verse_lexical rows the parse found 45.

- **Carried by the member words:** seek (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Th 5:15 | seek | V-PAM-2P | face | - | 0 | See that no one repays anyone evil for evil, but always **seek** to do good to one another and to everyone. |

### 3.24 G1722 ἐν en "in/on/among": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐν, transliteration en; STEP gloss "in/on/among"; sense head "in/on/among" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 10000; verses STEP attests 0; verse_lexical rows the parse found 2673.

- **Carried by the member words:** come upon (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Th 5:3 | come upon | PREP | silence | - | 0 | While people are saying, “There is peace and security,” then sudden destruction will **come upon** them as labor pains come upon a pregnant woman, and they will not escape. |

### 3.25 G1833 ἐξετάζω exetazō "to find out": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐξετάζω, transliteration exetazō; STEP gloss "to find out"; sense head "to find out" (the code is its own lemma).
- **Related terms (1):**  "".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 0; verse_lexical rows the parse found 3.

- **Carried by the member words:** search (1).
- **Engagement of these occurrences:** use 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 2:8 | search | V-AAM-2P | use | - | 0 | And he sent them to Bethlehem, saying, “ Go and **search** diligently for the child, and when you have found him, bring me word, that I too may come and worship him.” |

### 3.26 G2021 ἐπιχειρέω epicheireō "to attempt": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐπιχειρέω, transliteration epicheireō; STEP gloss "to attempt"; sense head "to attempt" (the code is its own lemma).
- **Related terms (2):** G1909 epi "upon/to/against"; G5495 cheir "hand".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** seeking (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 9:29 | seeking | V-IAI-3P | face | - | 0 | And he spoke and disputed against the Hellenists. But they were **seeking** to kill him. |

### 3.27 G2186 ἐφίστημι efistēmi "to approach": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐφίστημι, transliteration efistēmi; STEP gloss "to approach"; sense head "to approach" (the code is its own lemma).
- **Related terms (3):** G1909 epi "upon/to/against"; G1987 epistamai "to know/understand"; G2476 histēmi "to stand".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 82; verses STEP attests 21; verse_lexical rows the parse found 21.

- **Carried by the member words:** come upon (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Th 5:3 | come upon | V-PMI-3S | silence | - | 0 | While people are saying, “There is peace and security,” then sudden destruction will **come upon** them as labor pains come upon a pregnant woman, and they will not escape. |

### 3.28 G2614 καταδιώκω katadiōkō "to seek": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word καταδιώκω, transliteration katadiōkō; STEP gloss "to seek"; sense head "to seek" (the code is its own lemma).
- **Related terms (2):** G1377 diōkō "to pursue"; G2596 kata "according to".
- **Clusters (cluster_strong):** M83 Seeking & Inquiring (heuristic).
- **Counts, three measures as stored:** STEP token count 81; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** searched (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 1:36 | searched | V-AAI-3S | silence | - | 59 | And Simon and those who were with him **searched** for him, |

### 3.29 G4327 προσδέχομαι prosdechomai "to wait for/welcome": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προσδέχομαι, transliteration prosdechomai; STEP gloss "to wait for/welcome"; sense head "to wait for/welcome" (the code is its own lemma).
- **Related terms (2):** G1209 dechomai "to receive"; G4314 pros "to/with".
- **Clusters (cluster_strong):** M68 Hope & Waiting (medium).
- **Counts, three measures as stored:** STEP token count 48; verses STEP attests 0; verse_lexical rows the parse found 14.

- **Carried by the member words:** looking for (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 15:43 | looking for | V-PNP-NSM | face | - | 0 | Joseph of Arimathea, a respected member of the council, who was also himself **looking for** the kingdom of God, took courage and went to Pilate and asked for the body of Jesus. |

### 3.30 H1158 בָּעָה ba.ah "to enquire": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word בָּעָה, transliteration ba.ah; STEP gloss "to enquire"; sense head "to enquire" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1158):** to seek out, swell, cause to swell, boil up, enquire.
- **Related terms (3):** H0994 bi "please"; H1156 be.a "to ask"; H1159 ba.u "petition".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 5; verses STEP attests 4; verse_lexical rows the parse found 5.

- **Carried by the member words:** sought (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Obd 6 | sought | HVNp3cp | silence | - | 0 | How Esau has been pillaged, his treasures **sought** out! |

### 3.31 H1243 בַּקָּרָה baq.qa.rah "seeking": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word בַּקָּרָה, transliteration baq.qa.rah; STEP gloss "seeking"; sense head "seeking" (the code is its own lemma).
- **Related terms (5):** H0951 bo.qer "herdsman"; H1239 ba.qar "to enquire"; H1241 ba.qar "cattle"; H1242 bo.qer "morning"; H1244 biq.qo.ret "scourging".
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** seeks out (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 34:12 | seeks out | HNcfsc | face | - | 0 | As a shepherd **seeks out** his flock when he is among his sheep that have been scattered, so will I seek out my sheep, and I will rescue them from all places where they have been scattered on a day of clouds and thick darkness. |

### 3.32 H1980H הָלַךְ ha.lakh "to go: come": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word הָלַךְ, transliteration ha.lakh; STEP gloss "to go: come"; sense head "come[nearer]".
- **Senses (first level of the meaning tree of the lemma H1980):** to go, walk, come.
- **Related terms (16):** H1946 hukh "to go"; H1978 ha.likh "step"; H1979 ha.li.khah "walk"; H1980G ha.lakh "to go: went"; H1980I ha.lakh "to go: walk"; H1980J ha.lakh "to go: take"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 53; verses STEP attests 0; verse_lexical rows the parse found 47.

- **Carried by the member words:** sought (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 31:2 | sought | HVqaa | face | - | 0 | Thus says the Lord: “The people who survived the sword found grace in the wilderness; when Israel **sought** for rest, |

### 3.33 H2620 חָסָה cha.sah "to seek refuge": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָסָה, transliteration cha.sah; STEP gloss "to seek refuge"; sense head "to seek refuge" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2620):** (Qal) to seek refuge, flee for protection.
- **Related terms (5):** H2621G cho.sah "Hosah"; H2621H cho.sah "Hosah"; H2622 cha.sut "refuge"; H4268 mach.s.seh "refuge"; H4271 mach.se.yah "Mahseiah".
- **Clusters (cluster_strong):** M19 Trust & Refuge (None).
- **Counts, three measures as stored:** STEP token count 37; verses STEP attests 36; verse_lexical rows the parse found 37.

- **Carried by the member words:** seek shelter (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 30:2 | seek shelter | HVqcc | face | - | 0 | who set out to go down to Egypt, without asking for my direction, to take refuge in the protection of Pharaoh and to **seek shelter** in the shadow of Egypt! |

### 3.34 H2658 חָפַר cha.phar "to search": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חָפַר, transliteration cha.phar; STEP gloss "to search"; sense head "to search" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2658):** to dig, search for.
- **Related terms (9):** H2659 cha.pher "be ashamed"; H2660A che.pher "Hepher"; H2660B che.pher "Hepher"; H2660G che.pher "Hepher"; H2660H che.pher "Hepher"; H2661 cha.phor "mole"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 22; verses STEP attests 21; verse_lexical rows the parse found 22.

- **Carried by the member words:** search (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jos 2:3 | search | HVqcc | silence | - | 0 | Then the king of Jericho sent to Rahab, saying, “ Bring out the men who have come to you, who entered your house, for they have come to **search** out all the land.” |

### 3.35 H2665 חֵ֫פֶשׂ che.phe.s "plot": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חֵ֫פֶשׂ, transliteration che.phe.s; STEP gloss "plot"; sense head "plot" (the code is its own lemma).
- **Related terms (1):** H2664 cha.pha.s "to search".
- **Clusters (cluster_strong):** M06 Malice & Enmity (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** search (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 64:6 | search | HNcmsa | face | - | 0 | They **search** out injustice, saying, “We have accomplished a diligent search.” For the inward mind and heart of a man are deep. |

### 3.36 H2714 חֵ֫קֶר che.qer "search": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word חֵ֫קֶר, transliteration che.qer; STEP gloss "search"; sense head "search" (the code is its own lemma).
- **Related terms (2):** H2713 cha.qar "to search"; H4278 mech.qar "range".
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 12; verse_lexical rows the parse found 12.

- **Carried by the member words:** seek (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 25:27 | seek | HNcmsc | face | - | 0 | It is not good to eat much honey, nor is it glorious to **seek** one’s own glory. |

### 3.37 H5183A נַ֫חַת na.chat "quietness": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נַ֫חַת, transliteration na.chat; STEP gloss "quietness"; sense head "quietness" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5183):** rest, quietness.
- **Related terms (21):** H2010 ha.na.chah "holiday"; H3239A ya.no.ach "Janoah"; H3239B ya.no.chah "Janoah"; H4494 ma.no.ach "resting"; H4495 ma.no.ach "Manoah"; H4496G me.nu.chah "Nohah"; more in the workbook.
- **Clusters (cluster_strong):** M33 Rest & Peace (None).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 0; verse_lexical rows the parse found 6.

- **Carried by the member words:** finds (1).
- **Engagement of these occurrences:** use 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 6:5 | finds | HNcfsa | use | - | 0 | Moreover, it has not seen the sun or known anything, yet it **finds** rest rather than he. |

### 3.38 H5810 עָזַז a.zaz "be strong": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָזַז, transliteration a.zaz; STEP gloss "be strong"; sense head "be strong" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5810):** to be strong.
- **Related terms (2):** H4581 ma.oz "security"; H5808 iz.zuz "mighty".
- **Clusters (cluster_strong):** M23 Strength & Courage (None).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 11; verse_lexical rows the parse found 11.

- **Carried by the member words:** sought refuge (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Psa 52:7 | sought refuge | HVqi3ms | face | 17453 | 0 | “ See the man who would not make God his refuge, but trusted in the abundance of his riches and **sought refuge** in his own destruction!” |

### 3.39 H5927G עָלָה a.lah "to ascend: rise": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָלָה, transliteration a.lah; STEP gloss "to ascend: rise"; sense head "rise/go".
- **Senses (first level of the meaning tree of the lemma H5927):** to go up, ascend, climb.
- **Related terms (32):** H0131 a.dum.mim "Adummim"; H4605 ma.al "above"; H4607 mo.al "lifting"; H4608 ma.a.leh "ascent"; H4609A ma.a.lah "thought"; H4609B ma.a.lah "step"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 624; verses STEP attests 0; verse_lexical rows the parse found 604.

- **Carried by the member words:** come upon (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 10:12 | come upon | HVqj3ms | silence | - | 0 | Then the Lord said to Moses, “Stretch out your hand over the land of Egypt for the locusts, so that they may **come upon** the land of Egypt and eat every plant in the land, all that the hail has left.” |

### 3.40 H6440L פָּנֶה pa.neh "face of": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word פָּנֶה, transliteration pa.neh; STEP gloss "face of"; sense head "(PERSON eg 'his face' ie 'him')[face]".
- **Senses (first level of the meaning tree of the lemma H6440):** face.
- **Related terms (16):** H3312G ye.phun.neh "Jephunneh"; H3312H ye.phun.neh "Jephunneh"; H6437G pa.nah "to turn"; H6437H pa.nah "Corner [Gate]"; H6439G pe.nu.el "Peniel"; H6439H pe.nu.el "Penuel"; more in the workbook.
- **Clusters (cluster_strong):** T14 Body-Parts (medium).
- **Counts, three measures as stored:** STEP token count 102; verses STEP attests 95; verse_lexical rows the parse found 97.

- **Carried by the member words:** sought (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Sa 13:12 | sought | HNcmpc | face | - | 0 | I said, ‘ Now the Philistines will come down against me at Gilgal, and I have not **sought** the favor of the Lord.’ So I forced myself, and offered the burnt offering.” |

### 3.41 H6485I פָּקַד pa.qad "to reckon: visit": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word פָּקַד, transliteration pa.qad; STEP gloss "to reckon: visit"; sense head "visit/inspect".
- **Senses (first level of the meaning tree of the lemma H6485):** to attend to, muster, number, reckon, visit, punish, appoint, look aft ... (cut; the whole text is in the workbook).
- **Related terms (14):** H4662G miph.qad "Muster [Gate]"; H4662H miph.qad "appointment"; H6485A pa.qad "to reckon: list"; H6485B pe.qu.dim "reckoning"; H6485H pa.qad "to reckon: punish"; H6485J pa.qad "to reckon: overseer"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 47; verses STEP attests 40; verse_lexical rows the parse found 47.

- **Carried by the member words:** sought (1).
- **Engagement of these occurrences:** face 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 26:16 | sought | HVqp3cp | face | - | 0 | O Lord, in distress they **sought** you; they poured out a whispered prayer when your discipline was upon them. |

### 3.42 H7200K רָאָה ra.ah "to see: enjoy": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רָאָה, transliteration ra.ah; STEP gloss "to see: enjoy"; sense head "enjoy/see(good/life)".
- **Senses (first level of the meaning tree of the lemma H7200):** to see, look at, inspect, perceive, consider.
- **Related terms (26):** H3070 yir.eh "Provider [God]"; H3376 yir.iy.yah "Irijah"; H4758 mar.eh "appearance"; H4759A mar.ah "vision"; H4759B mar.ah "mirror"; H7200G ra.ah "to see: see"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 8; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** find (1).
- **Engagement of these occurrences:** use 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ecc 5:18 | find | HVqcc | use | - | 0 | Behold, what I have seen to be good and fitting is to eat and drink and **find** enjoyment in all the toil with which one toils under the sun the few days of his life that God has given him, for this is his lot. |

### 3.43 H7304 רָוַח ra.vach "be wide": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רָוַח, transliteration ra.vach; STEP gloss "be wide"; sense head "be wide" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7304):** to be wide, be spacious, breathe.
- **Related terms (3):** H7305 re.vach "space"; H7306 ri.ach "to smell"; H7309 re.va.chah "relief".
- **Clusters (cluster_strong):** T2 Supplementary (low).
- **Counts, three measures as stored:** STEP token count 3; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** find (1).
- **Engagement of these occurrences:** use 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 32:20 | find | HVqu3ms | use | - | 0 | I must speak, that I may **find** relief; I must open my lips and answer. |

### 3.44 H7356B רַחֲמִים ra.cha.mim "compassion": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רַחֲמִים, transliteration ra.cha.mim; STEP gloss "compassion"; sense head "compassion" (the code is its own lemma).
- **Related terms (22):** H3395G ye.ro.cham "Jeroham"; H3395H ye.ro.cham "Jeroham"; H3395I ye.ro.cham "Jeroham"; H3395J ye.ro.cham "Jeroham"; H3395K ye.ro.cham "Jeroham"; H3395L ye.ro.cham "Jeroham"; more in the workbook.
- **Clusters (cluster_strong):** M50 Grace & Mercy (heuristic).
- **Counts, three measures as stored:** STEP token count 42; verses STEP attests 39; verse_lexical rows the parse found 39.

- **Carried by the member words:** find compassion (1).
- **Engagement of these occurrences:** use 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Ch 30:9 | find compassion | HNcmpa | use | 14589 | 0 | For if you return to the Lord, your brothers and your children will **find compassion** with their captors and return to this land. For the Lord your God is gracious and merciful and will not turn away his face from you, if you return to him.” |

### 3.45 H7592 שָׁאַל sha.al "to ask": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word שָׁאַל, transliteration sha.al; STEP gloss "to ask"; sense head "to ask" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7592):** to ask, enquire, borrow, beg.
- **Related terms (12):** H4862 mish.a.lah "petition"; H7585 she.ol "hell: Sheol"; H7586G sha.ul "Saul"; H7586H sha.ul "Shaul"; H7586I sha.ul "Shaul"; H7586J sha.ul "Shaul"; more in the workbook.
- **Clusters (cluster_strong):** M21 Fasting & Piety (None).
- **Counts, three measures as stored:** STEP token count 185; verses STEP attests 157; verse_lexical rows the parse found 173.

- **Carried by the member words:** seek (1).
- **Engagement of these occurrences:** silence 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Pro 20:4 | seek | HVqq3ms | silence | - | 0 | The sluggard does not plow in the autumn; he will **seek** at harvest and have nothing. |

### 3.46 Occurrences where the member surface is shared with another code's unit (74)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| Luk 23:14 | find | G1722 ἐν en "in/on/among" | find | content_part | 2 | silence | - | 0 | and said to them, “You brought me this man as one who was misleading the people. And after examining him before you, behold, I did not **find** this man guilty of any of your charges against him. |
| Job 9:10 | searching | H0369 אַ֫יִן a.yin "nothing" | searching | content_part | 2 | silence | - | 0 | who does great things beyond **searching** out, and marvelous things beyond number. |
| Eze 34:6 | seek | H0369 אַ֫יִן a.yin "nothing" | seek | content_part | 3 | use | - | 0 | they wandered over all the mountains and on every high hill. My sheep were scattered over all the face of the earth, with none to search or **seek** for them. |
| 1Ki 20:6 | search | H0413 אֶל el "to[wards]" | search | content_part | 4 | silence | - | 0 | Nevertheless I will send my servants to you tomorrow about this time, and they shall **search** your house and the houses of your servants and lay hands on whatever pleases you and take it away.’” |
| Gen 37:16 | seeking | H0595 אָֽנֹכִ֫י a.no.khi "I" | seeking | content_part | 2 | silence | - | 0 | “ I am **seeking** my brothers,” he said. “ Tell me, please, where they are pasturing the flock.” |
| Num 32:23 | find | H0834A אֲשֶׁר a.sher "which" | find | content_part | 3 | silence | - | 0 | But if you will not do so, behold, you have sinned against the Lord, and be sure your sin will **find** you out. |
| Judg 4:22 | seeking | H0834A אֲשֶׁר a.sher "which" | seeking | content_part | 2 | silence | - | 0 | And behold, as Barak was pursuing Sisera, Jael went out to meet him and said to him, “ Come, and I will show you the man whom you are **seeking**.” So he went in to her tent, and there lay Sisera dead, with the tent peg in his temple. |
| Judg 9:33 | finds | H0834A אֲשֶׁר a.sher "which" | finds | content_part | 5 | silence | - | 0 | Then in the morning, as soon as the sun is up, rise early and rush upon the city. And when he and the people who are with him come out against you, you may do to them as your hand **finds** to do.” |
| Judg 17:8 | find | H0834A אֲשֶׁר a.sher "which" | find | content_part | 3 | silence | - | 0 | And the man departed from the town of Bethlehem in Judah to sojourn where he could **find** a place. And as he journeyed, he came to the hill country of Ephraim to the house of Micah. |
| Judg 17:9 | find | H0834A אֲשֶׁר a.sher "which" | find | content_part | 3 | silence | - | 0 | And Micah said to him, “ Where do you come from?” And he said to him, “I am a Levite of Bethlehem in Judah, and I am going to sojourn where I may **find** a place.” |
| Rut 2:2 | find | H0834A אֲשֶׁר a.sher "which" | find | content_part | 2 | use | - | 0 | And Ruth the Moabite said to Naomi, “ Let me go to the field and glean among the ears of grain after him in whose sight I shall **find** favor.” And she said to her, “ Go, my daughter.” |
| Jer 8:2 | sought | H0834A אֲשֶׁר a.sher "which" | sought | content_part | 4 | face | - | 0 | And they shall be spread before the sun and the moon and all the host of heaven, which they have loved and served, which they have gone after, and which they have **sought** and worshiped. And they shall not be gathered or buried. They shall be as dung on the surface of the ground. |
| Psa 27:4 | seek | H0853 אֵת et "[Obj.]" | seek | content_part | 3 | face | - | 0 | One thing have I asked of the Lord, that will I **seek** after: that I may dwell in the house of the Lord all the days of my life, to gaze upon the beauty of the Lord and to inquire in his temple. |
| Jer 29:13 | find | H0853 אֵת et "[Obj.]" | find | content_part | 3 | use | - | 0 | You will seek me and **find** me, when you seek me with all your heart. |
| Hos 2:7 | seek | H0853 אֵת et "[Obj.]" | seek | content_part | 3 | face | - | 0 | She shall pursue her lovers but not overtake them, and she shall **seek** them but shall not find them. Then she shall say, ‘I will go and return to my first husband, for it was better for me then than now.’ |
| Gen 38:23 | find | H0859A אַתָּ֫ה at.tah "you [m.s.]" | find | content_part | 5 | silence | - | 0 | And Judah replied, “Let her keep the things as her own, or we shall be laughed at. You see, I sent this young goat, and you did not **find** her.” |
| Psa 63:1 | seek | H0859A אַתָּ֫ה at.tah "you [m.s.]" | seek | content_part | 3 | face | - | 0 | A Psalm of David, when he was in the wilderness of Judah. O God, you are my God; earnestly I **seek** you; my soul thirsts for you; my flesh faints for you, as in a dry and weary land where there is no water. |
| Job 10:20 | find | H1082 בָּלַג ba.lag "be cheerful" | find | content_part | 3 | use | 14610 | 0 | Are not my days few? Then cease, and leave me alone, that I may **find** a little cheer |
| Dan 6:4 | sought | H1156 בְּעָא be.a "to ask" | sought | content_part | 3 | face | - | 0 | Then the high officials and the satraps **sought** to find a ground for complaint against Daniel with regard to the kingdom, but they could find no ground for complaint or any fault, because he was faithful, and no error or fault was found in him. |
| Gen 37:16 | seeking | H1245 בָּקַשׁ ba.qash "to seek" | seeking | content_part | 2 | silence | - | 3 | “ I am **seeking** my brothers,” he said. “ Tell me, please, where they are pasturing the flock.” |
| Exo 2:15 | sought | H1245 בָּקַשׁ ba.qash "to seek" | sought | content_part | 3 | face | - | 3 | When Pharaoh heard of it, he **sought** to kill Moses. But Moses fled from Pharaoh and stayed in the land of Midian. And he sat down by a well. |
| Judg 4:22 | seeking | H1245 בָּקַשׁ ba.qash "to seek" | seeking | content_part | 2 | silence | - | 2 | And behold, as Barak was pursuing Sisera, Jael went out to meet him and said to him, “ Come, and I will show you the man whom you are **seeking**.” So he went in to her tent, and there lay Sisera dead, with the tent peg in his temple. |
| 1Sa 27:4 | sought | H1245 בָּקַשׁ ba.qash "to seek" | sought | content_part | 3 | use | - | 3 | And when it was told Saul that David had fled to Gath, he no longer **sought** him. |
| 2Sa 3:17 | seeking | H1245 בָּקַשׁ ba.qash "to seek" | seeking | content_part | 2 | face | - | 3 | And Abner conferred with the elders of Israel, saying, “For some time past you have been **seeking** David as king over you. |
| Ezr 2:62 | sought | H1245 בָּקַשׁ ba.qash "to seek" | sought | content_part | 2 | silence | - | 2 | These **sought** their registration among those enrolled in the genealogies, but they were not found there, and so they were excluded from the priesthood as unclean. |
| Ecc 7:28 | sought | H1245 בָּקַשׁ ba.qash "to seek" | sought | content_part | 2 | face | 17111, 18131 | 3 | which my soul has **sought** repeatedly, but I have not found. One man among a thousand I found, but a woman among all these I have not found. |
| Lam 1:19 | sought | H1245 בָּקַשׁ ba.qash "to seek" | sought | content_part | 2 | silence | - | 3 | “I called to my lovers, but they deceived me; my priests and elders perished in the city, while they **sought** food to revive their strength. |
| 2Ch 25:20 | sought | H1875 דָּרַשׁ da.rash "to seek" | sought | content_part | 2 | face | - | 4 | But Amaziah would not listen, for it was of God, in order that he might give them into the hand of their enemies, because they had **sought** the gods of Edom. |
| Jer 8:2 | sought | H1875 דָּרַשׁ da.rash "to seek" | sought | content_part | 4 | face | 20370 | 3 | And they shall be spread before the sun and the moon and all the host of heaven, which they have loved and served, which they have gone after, and which they have **sought** and worshiped. And they shall not be gathered or buried. They shall be as dung on the surface of the ground. |
| Job 28:3 | searches | H1931 הוּא hu "he/she/it" | searches | content_part | 2 | silence | - | 0 | Man puts an end to darkness and **searches** out to the farthest limit the ore in gloom and deep darkness. |
| Zep 1:12 | search | H1931 הוּא hu "he/she/it" | search | content_part | 3 | use | - | 0 | At that time I will **search** Jerusalem with lamps, and I will punish the men who are complacent, those who say in their hearts, ‘The Lord will not do good, nor will he do ill.’ |
| Dan 6:4 | sought | H1934 הֲוָא ha.va "to be" | sought | content_part | 3 | face | - | 0 | Then the high officials and the satraps **sought** to find a ground for complaint against Daniel with regard to the kingdom, but they could find no ground for complaint or any fault, because he was faithful, and no error or fault was found in him. |
| Gen 4:14 | finds | H1961 הָיָה ha.yah "to be" | finds | content_part | 3 | silence | - | 0 | Behold, you have driven me today away from the ground, and from your face I shall be hidden. I shall be a fugitive and a wanderer on the earth, and whoever **finds** me will kill me.” |
| Deu 24:1 | finds | H1961 הָיָה ha.yah "to be" | finds | content_part | 5 | use | - | 0 | “When a man takes a wife and marries her, if then she **finds** no favor in his eyes because he has found some indecency in her, and he writes her a certificate of divorce and puts it in her hand and sends her out of his house, and she departs out of his house, |
| 2Sa 3:17 | seeking | H1961 הָיָה ha.yah "to be" | seeking | content_part | 2 | face | - | 0 | And Abner conferred with the elders of Israel, saying, “For some time past you have been **seeking** David as king over you. |
| 2Ch 26:5 | seek | H1961 הָיָה ha.yah "to be" | seek | content_part | 3 | face | - | 0 | He set himself to **seek** God in the days of Zechariah, who instructed him in the fear of God, and as long as he sought the Lord, God made him prosper. |
| Eze 7:26 | seek | H1961 הָיָה ha.yah "to be" | seek | content_part | 2 | face | - | 0 | Disaster comes upon disaster; rumor follows rumor. They **seek** a vision from the prophet, while the law perishes from the priest and counsel from the elders. |
| Pro 4:22 | find | H1992 הֵ֫מָּה hem.mah "they [masc.]" | find | content_part | 3 | silence | - | 0 | For they are life to those who **find** them, and healing to all their flesh. |
| Gen 38:23 | find | H2088 זֶה zeh "this" | find | content_part | 5 | silence | - | 0 | And Judah replied, “Let her keep the things as her own, or we shall be laughed at. You see, I sent this young goat, and you did not **find** her.” |
| Exo 2:15 | sought | H2088 זֶה zeh "this" | sought | content_part | 3 | face | - | 0 | When Pharaoh heard of it, he **sought** to kill Moses. But Moses fled from Pharaoh and stayed in the land of Midian. And he sat down by a well. |
| Job 28:3 | searches | H2713 חָקַר cha.qar "to search" | searches | content_part | 2 | silence | - | 0 | Man puts an end to darkness and **searches** out to the farthest limit the ore in gloom and deep darkness. |
| Job 32:11 | searched | H2713 חָקַר cha.qar "to search" | searched | content_part | 3 | face | - | 0 | “ Behold, I waited for your words, I listened for your wise sayings, while you **searched** out what to say. |
| Jos 2:3 | search | H3588A כִּי ki "for" | search | content_part | 4 | silence | - | 0 | Then the king of Jericho sent to Rahab, saying, “ Bring out the men who have come to you, who entered your house, for they have come to **search** out all the land.” |
| 2Ch 25:20 | sought | H3588A כִּי ki "for" | sought | content_part | 2 | face | - | 0 | But Amaziah would not listen, for it was of God, in order that he might give them into the hand of their enemies, because they had **sought** the gods of Edom. |
| Job 3:22 | find | H3588A כִּי ki "for" | find | content_part | 2 | silence | - | 0 | who rejoice exceedingly and are glad when they **find** the grave? |
| Job 10:6 | seek | H3588A כִּי ki "for" | seek | content_part | 2 | use | - | 0 | that you **seek** out my iniquity and search for my sin, |
| Lam 1:19 | sought | H3588A כִּי ki "for" | sought | content_part | 2 | silence | - | 0 | “I called to my lovers, but they deceived me; my priests and elders perished in the city, while they **sought** food to revive their strength. |
| Gen 4:14 | finds | H3605 כֹּל kol "all" | finds | content_part | 3 | silence | - | 0 | Behold, you have driven me today away from the ground, and from your face I shall be hidden. I shall be a fugitive and a wanderer on the earth, and whoever **finds** me will kill me.” |
| Deu 24:1 | finds | H3808 לֹא lo "not" | finds | content_part | 5 | use | - | 0 | “When a man takes a wife and marries her, if then she **finds** no favor in his eyes because he has found some indecency in her, and he writes her a certificate of divorce and puts it in her hand and sends her out of his house, and she departs out of his house, |
| Judg 13:5 | come upon | H3808 לֹא lo "not" | come upon | content_part | 2 | silence | - | 0 | for behold, you shall conceive and bear a son. No razor shall **come upon** his head, for the child shall be a Nazirite to God from the womb, and he shall begin to save Israel from the hand of the Philistines.” |
| Ezr 9:12 | seek | H3808 לֹא lo "not" | seek | content_part | 4 | face | - | 0 | Therefore do not give your daughters to their sons, neither take their daughters for your sons, and never **seek** their peace or prosperity, that you may be strong and eat the good of the land and leave it for an inheritance to your children forever.’ |
| Hos 2:6 | find | H3808 לֹא lo "not" | find | content_part | 3 | silence | - | 0 | Therefore I will hedge up her way with thorns, and I will build a wall against her, so that she cannot **find** her paths. |
| Hos 12:8 | find | H3808 לֹא lo "not" | find | content_part | 3 | silence | - | 0 | Ephraim has said, “ Ah, but I am rich; I have found wealth for myself; in all my labors they cannot **find** in me iniquity or sin.” |
| Psa 73:10 | find | H4325G מַי may "water" | find | content_part | 4 | silence | - | 0 | Therefore his people turn back to them, and **find** no fault in them. |
| Psa 73:10 | find | H4392 מָלֵא ma.le "full" | find | content_part | 4 | silence | - | 0 | Therefore his people turn back to them, and **find** no fault in them. |
| Deu 22:3 | find | H4480A מִן־ min- "from" | find | content_part | 3 | silence | - | 0 | And you shall do the same with his donkey or with his garment, or with any lost thing of your brother’s, which he loses and you **find**; you may not ignore it. |
| Job 10:20 | find | H4480A מִן־ min- "from" | find | content_part | 3 | use | - | 0 | Are not my days few? Then cease, and leave me alone, that I may **find** a little cheer |
| Gen 4:14 | finds | H4672 מָצָא ma.tsa "to find" | finds | content_part | 3 | silence | - | 0 | Behold, you have driven me today away from the ground, and from your face I shall be hidden. I shall be a fugitive and a wanderer on the earth, and whoever **finds** me will kill me.” |
| Deu 24:1 | finds | H4672 מָצָא ma.tsa "to find" | finds | content_part | 5 | use | - | 0 | “When a man takes a wife and marries her, if then she **finds** no favor in his eyes because he has found some indecency in her, and he writes her a certificate of divorce and puts it in her hand and sends her out of his house, and she departs out of his house, |
| Judg 9:33 | finds | H4672 מָצָא ma.tsa "to find" | finds | content_part | 5 | silence | - | 0 | Then in the morning, as soon as the sun is up, rise early and rush upon the city. And when he and the people who are with him come out against you, you may do to them as your hand **finds** to do.” |
| Job 33:10 | finds | H4672 מָצָא ma.tsa "to find" | finds | content_part | 3 | use | - | 0 | Behold, he **finds** occasions against me, he counts me as his enemy, |
| Psa 73:10 | find | H4680 מָצָה ma.tsah "to drain" | find | content_part | 4 | silence | - | 0 | Therefore his people turn back to them, and **find** no fault in them. |
| 1Sa 20:36 | find | H4994 נָא na "please" | find | content_part | 2 | silence | - | 0 | And he said to his boy, “ Run and **find** the arrows that I shoot.” As the boy ran, he shot an arrow beyond him. |
| Ecc 2:24 | find | H5315I נֶ֫פֶשׁ ne.phesh "soul: myself" | find | content_part | 2 | use | 14224, 14470, 17289 | 0 | There is nothing better for a person than that he should eat and drink and **find** enjoyment in his toil. This also, I saw, is from the hand of God, |
| 1Ch 19:3 | search | H5668 עָבוּר a.vur "for the sake of" | search | content_part | 4 | silence | - | 0 | But the princes of the Ammonites said to Hanun, “Do you think, because David has sent comforters to you, that he is honoring your father? Have not his servants come to you to **search** and to overthrow and to spy out the land?” |
| Job 9:10 | searching | H5704 עַד ad "till" | searching | content_part | 2 | silence | - | 0 | who does great things beyond **searching** out, and marvelous things beyond number. |
| Job 32:11 | searched | H5704 עַד ad "till" | searched | content_part | 3 | face | - | 0 | “ Behold, I waited for your words, I listened for your wise sayings, while you **searched** out what to say. |
| 1Sa 27:4 | sought | H5750 עוֹד od "still" | sought | content_part | 3 | use | - | 0 | And when it was told Saul that David had fled to Gath, he no longer **sought** him. |
| Ecc 7:28 | sought | H5750 עוֹד od "still" | sought | content_part | 2 | face | - | 0 | which my soul has **sought** repeatedly, but I have not found. One man among a thousand I found, but a woman among all these I have not found. |
| Job 33:10 | finds | H5921A עַל al "upon" | finds | content_part | 3 | use | - | 0 | Behold, he **finds** occasions against me, he counts me as his enemy, |
| Judg 13:5 | come upon | H5927G עָלָה a.lah "to ascend: rise" | come upon | content_part | 2 | silence | - | 0 | for behold, you shall conceive and bear a son. No razor shall **come upon** his head, for the child shall be a Nazirite to God from the womb, and he shall begin to save Israel from the hand of the Philistines.” |
| 2Ch 15:2 | seek | H5973A עִם im "with" | seek | content_part | 9 | face | - | 0 | and he went out to meet Asa and said to him, “ Hear me, Asa, and all Judah and Benjamin: The Lord is with you while you are with him. If you **seek** him, he will be found by you, but if you forsake him, he will forsake you. |
| Ecc 2:24 | find | H7200K רָאָה ra.ah "to see: enjoy" | find | content_part | 2 | use | - | 0 | There is nothing better for a person than that he should eat and drink and **find** enjoyment in his toil. This also, I saw, is from the hand of God, |
| 1Ki 18:10 | seek | H8033G שָׁם sham "there" | seek | content_part | 4 | use | - | 0 | As the Lord your God lives, there is no nation or kingdom where my lord has not sent to **seek** you. And when they would say, ‘He is not here,’ he would take an oath of the kingdom or nation, that they had not found you. |

## 4. What the study has recorded for these occurrences

Of 730 occurrences, 730 have an engagement observation and 0 have none recorded. There are 1411 live observations on them (73 engagement, 158 of other recorded stages, 1180 of the retired catalogue stages) and 1105 withdrawn.

### 4.1 Engagement: what each word does for the inner being (73 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

- **Observation 21739** (engagement, tag face, status draft): 'search' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'search' names.
  - applies to 6 occurrence(s): Psa 64:6 (search), Psa 77:6 (search), Pro 2:4 (search), Pro 25:2 (search), Ecc 1:13 (search), Ecc 7:25 (search)
- **Observation 21740** (engagement, tag face, status draft): 'search' is here a hostile or purposed intent: the will set to kill, harm, destroy, arrest or lead another astray; the deed is told by the verse's other words, the intent is what 'search' names.
  - applies to 1 occurrence(s): Mat 2:13 (search)
- **Observation 21741** (engagement, tag face, status draft): 'search' is here the seeking of God: the heart or will turned to him (his face, name, word or help), in its different degrees: wholehearted, in distress, resolved, or negated; the seeking is itself the inner operation.
  - applies to 1 occurrence(s): Deu 4:29 (search)
- **Observation 21745** (engagement, tag face, status draft): 'searched' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'searched' names.
  - applies to 3 occurrence(s): Job 32:11 (searched), Ecc 2:3 (searched), 1Pe 1:10 (searched)
- **Observation 21749** (engagement, tag face, status draft): 'searches' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'searches' names.
  - applies to 1 occurrence(s): Pro 11:27 (searches)
- **Observation 21755** (engagement, tag face, status draft): 'seek' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'seek' names.
  - applies to 76 occurrence(s): Num 16:10 (seek), Deu 23:6 (seek), Rut 3:1 (seek), 1Ch 13:3 (seek), 2Ch 17:3 (seek), 2Ch 26:5 (seek), Ezr 9:12 (seek), Neh 2:10 (seek), Psa 4:2 (seek), Psa 27:4 (seek), Psa 34:14 (seek), Psa 45:12 (seek); and 64 more (sheet `Observation nodes`)
- **Observation 21756** (engagement, tag face, status draft): 'seek' is here a hostile or purposed intent: the will set to kill, harm, destroy, arrest or lead another astray; the deed is told by the verse's other words, the intent is what 'seek' names.
  - applies to 34 occurrence(s): Num 35:23 (seek), 1Sa 23:15 (seek), 1Sa 25:26 (seek), 1Sa 25:29 (seek), 2Sa 17:3 (seek), 2Sa 20:19 (seek), 1Ki 19:10 (seek), 1Ki 19:14 (seek), Psa 35:4 (seek), Psa 38:12 (seek), Psa 40:14 (seek), Psa 54:3 (seek); and 22 more (sheet `Observation nodes`)
- **Observation 21757** (engagement, tag face, status draft): 'seek' is here the seeking of God: the heart or will turned to him (his face, name, word or help), in its different degrees: wholehearted, in distress, resolved, or negated; the seeking is itself the inner operation.
  - applies to 72 occurrence(s): Lev 19:31 (seek), Deu 4:29 (seek), 1Ch 10:14 (seek), 1Ch 15:13 (seek), 1Ch 16:10 (seek), 1Ch 16:11 (seek), 1Ch 22:19 (seek), 1Ch 28:9 (seek), 2Ch 7:14 (seek), 2Ch 11:16 (seek), 2Ch 12:14 (seek), 2Ch 14:4 (seek); and 60 more (sheet `Observation nodes`)
- **Observation 21760** (engagement, tag face, status draft): 'seeking' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'seeking' names.
  - applies to 25 occurrence(s): Judg 18:1 (seeking), 2Sa 3:17 (seeking), 1Ki 11:22 (seeking), 1Ki 20:7 (seeking), 1Ch 10:13 (seeking), Ecc 8:17 (seeking), Isa 58:13 (seeking), Jer 38:4 (seeking), Mal 2:15 (seeking), Mat 12:43 (seeking), Mat 26:59 (seeking), Mar 3:32 (seeking); and 13 more (sheet `Observation nodes`)
- **Observation 21761** (engagement, tag face, status draft): 'seeking' is here a hostile or purposed intent: the will set to kill, harm, destroy, arrest or lead another astray; the deed is told by the verse's other words, the intent is what 'seeking' names.
  - applies to 19 occurrence(s): Exo 4:19 (seeking), Judg 14:4 (seeking), Mat 21:46 (seeking), Mar 11:18 (seeking), Mar 12:12 (seeking), Mar 14:1 (seeking), Mar 14:55 (seeking), Luk 5:18 (seeking), Luk 19:47 (seeking), Luk 22:2 (seeking), Joh 5:18 (seeking), Joh 7:1 (seeking); and 7 more (sheet `Observation nodes`)
- **Observation 21762** (engagement, tag face, status draft): 'seeking' is here the seeking of God: the heart or will turned to him (his face, name, word or help), in its different degrees: wholehearted, in distress, resolved, or negated; the seeking is itself the inner operation.
  - applies to 4 occurrence(s): 1Sa 27:1 (seeking), 2Ch 31:21 (seeking), Dan 9:3 (seeking), Joh 6:26 (seeking)
- **Observation 21765** (engagement, tag face, status draft): 'seeks' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'seeks' names.
  - applies to 18 occurrence(s): 1Sa 22:23 (seeks), Pro 11:27 (seeks), Pro 14:6 (seeks), Pro 15:14 (seeks), Pro 17:9 (seeks), Pro 17:11 (seeks), Pro 17:19 (seeks), Pro 18:1 (seeks), Pro 18:15 (seeks), Isa 16:5 (seeks), Jer 5:1 (seeks), Mat 7:8 (seeks); and 6 more (sheet `Observation nodes`)
- **Observation 21766** (engagement, tag face, status draft): 'seeks' is here a hostile or purposed intent: the will set to kill, harm, destroy, arrest or lead another astray; the deed is told by the verse's other words, the intent is what 'seeks' names.
  - applies to 8 occurrence(s): 1Sa 19:2 (seeks), 1Sa 20:1 (seeks), 1Sa 22:23 (seeks), 1Sa 23:10 (seeks), 1Sa 24:9 (seeks), 2Sa 16:11 (seeks), Psa 37:32 (seeks), Psa 86:14 (seeks)
- **Observation 21767** (engagement, tag face, status draft): 'seeks' is here the seeking of God: the heart or will turned to him (his face, name, word or help), in its different degrees: wholehearted, in distress, resolved, or negated; the seeking is itself the inner operation.
  - applies to 1 occurrence(s): Lam 3:25 (seeks)
- **Observation 21770** (engagement, tag face, status draft): 'sought' is here a desire or purpose of the will directed to an object (glory, wisdom, peace, a sign, rest, favour, one's own good, or a turning to other gods), good or ill; the direction of the will is what 'sought' names.
  - applies to 24 occurrence(s): Exo 2:15 (sought), 1Sa 14:4 (sought), 1Ki 10:24 (sought), 2Ch 9:23 (sought), 2Ch 15:15 (sought), 2Ch 25:15 (sought), 2Ch 25:20 (sought), Est 10:3 (sought), Ecc 7:28 (sought), Ecc 7:29 (sought), Ecc 12:10 (sought), Song 3:1 (sought); and 12 more (sheet `Observation nodes`)
- **Observation 21771** (engagement, tag face, status draft): 'sought' is here a hostile or purposed intent: the will set to kill, harm, destroy, arrest or lead another astray; the deed is told by the verse's other words, the intent is what 'sought' names.
  - applies to 20 occurrence(s): Exo 2:15 (sought), Deu 13:10 (sought), 1Sa 19:10 (sought), 2Sa 4:8 (sought), 2Sa 21:2 (sought), 1Ki 11:40 (sought), Est 2:21 (sought), Est 3:6 (sought), Est 6:2 (sought), Est 9:2 (sought), Psa 71:24 (sought), Jer 26:21 (sought); and 8 more (sheet `Observation nodes`)
- **Observation 21772** (engagement, tag face, status draft): 'sought' is here the seeking of God: the heart or will turned to him (his face, name, word or help), in its different degrees: wholehearted, in distress, resolved, or negated; the seeking is itself the inner operation.
  - applies to 19 occurrence(s): Exo 4:24 (sought), Exo 33:7 (sought), 1Sa 13:12 (sought), 2Sa 12:16 (sought), 2Sa 21:1 (sought), 2Ki 13:4 (sought), 2Ch 1:5 (sought), 2Ch 14:7 (sought), 2Ch 15:4 (sought), 2Ch 17:4 (sought), 2Ch 22:9 (sought), 2Ch 26:5 (sought); and 7 more (sheet `Observation nodes`)
- **Observation 21779** (engagement, tag face, status draft): 'earnestly seeks' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'earnestly seeks' names.
  - applies to 1 occurrence(s): Isa 26:9 (earnestly seeks)
- **Observation 21781** (engagement, tag face, status draft): 'insist on' is here negated: the absence of seeking or of insisting is what the verse states, and it is the operation named.
  - applies to 1 occurrence(s): 1Cor 13:5 (insist on)
- **Observation 21783** (engagement, tag face, status draft): 'look for' is here an expecting or an attitude of the mind (expecting the one who is to come, the kingdom of God; being well disposed toward another); the state itself is the inner operation.
  - applies to 3 occurrence(s): Mat 11:3 (look for), Luk 7:19 (look for), Luk 7:20 (look for)
- **Observation 21785** (engagement, tag face, status draft): 'looking for' is here an expecting or an attitude of the mind (expecting the one who is to come, the kingdom of God; being well disposed toward another); the state itself is the inner operation.
  - applies to 1 occurrence(s): Mar 15:43 (looking for)
- **Observation 21787** (engagement, tag face, status draft): 'search for' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'search for' names.
  - applies to 1 occurrence(s): Job 10:6 (search for)
- **Observation 21790** (engagement, tag face, status draft): 'seek after' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seek after' names.
  - applies to 1 occurrence(s): Luk 12:30 (seek after)
- **Observation 21791** (engagement, tag face, status draft): 'seek for' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seek for' names.
  - applies to 1 occurrence(s): Rom 2:7 (seek for)
- **Observation 21792** (engagement, tag face, status draft): 'seek me diligently' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seek me diligently' names.
  - applies to 2 occurrence(s): Pro 1:28 (seek me diligently), Pro 8:17 (seek me diligently)
- **Observation 21793** (engagement, tag face, status draft): 'seek out' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seek out' names.
  - applies to 2 occurrence(s): 1Ch 28:8 (seek out), Eze 34:12 (seek out)
- **Observation 21795** (engagement, tag face, status draft): 'seek shelter' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seek shelter' names.
  - applies to 1 occurrence(s): Isa 30:2 (seek shelter)
- **Observation 21796** (engagement, tag face, status draft): 'seeks for' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seeks for' names.
  - applies to 2 occurrence(s): Mat 12:39 (seeks for), Luk 11:29 (seeks for)
- **Observation 21797** (engagement, tag face, status draft): 'seeks for' is here negated: the absence of seeking or of insisting is what the verse states, and it is the operation named.
  - applies to 1 occurrence(s): Rom 3:11 (seeks for)
- **Observation 21798** (engagement, tag face, status draft): 'seeks out' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'seeks out' names.
  - applies to 1 occurrence(s): Eze 34:12 (seeks out)
- **Observation 21801** (engagement, tag face, status draft): 'sought out' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'sought out' names.
  - applies to 1 occurrence(s): 1Sa 13:14 (sought out)
- **Observation 21804** (engagement, tag face, status draft): 'sought refuge' is here a purposed seeking, desire or turning of the will toward an object (God, wisdom, a sign, shelter, the commandments, a person's good); the direction of the will is what 'sought refuge' names.
  - applies to 1 occurrence(s): Psa 52:7 (sought refuge)
- **Observation 21805** (engagement, tag face, status draft): 'well disposed' is here an expecting or an attitude of the mind (expecting the one who is to come, the kingdom of God; being well disposed toward another); the state itself is the inner operation.
  - applies to 1 occurrence(s): 1Sa 20:12 (well disposed)
- **Observation 21733** (engagement, tag silence, status draft): 'find' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 109 occurrence(s): Gen 18:26 (find), Gen 18:28 (find), Gen 18:30 (find), Gen 31:32 (find), Gen 31:33 (find), Gen 31:34 (find), Gen 31:35 (find), Gen 32:19 (find), Gen 38:20 (find), Gen 38:23 (find), Gen 41:38 (find), Gen 44:34 (find); and 97 more (sheet `Observation nodes`)
- **Observation 21736** (engagement, tag silence, status draft): 'finds' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 23 occurrence(s): Gen 4:14 (finds), Lev 25:26 (finds), Num 35:27 (finds), Judg 9:33 (finds), 1Sa 10:7 (finds), 1Sa 24:19 (finds), Psa 84:3 (finds), Psa 119:162 (finds), Pro 3:13 (finds), Pro 8:35 (finds), Pro 18:22 (finds), Ecc 9:10 (finds); and 11 more (sheet `Observation nodes`)
- **Observation 21742** (engagement, tag silence, status draft): 'search' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 18 occurrence(s): Jos 2:3 (search), 1Sa 23:23 (search), 2Sa 10:3 (search), 1Ki 20:6 (search), 2Ki 10:23 (search), 1Ch 19:3 (search), 1Ch 26:31 (search), Ezr 4:15 (search), Ezr 4:19 (search), Ezr 5:17 (search), Ezr 6:1 (search), Jer 5:1 (search); and 6 more (sheet `Observation nodes`)
- **Observation 21746** (engagement, tag silence, status draft): 'searched' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 5 occurrence(s): Gen 31:35 (searched), Gen 44:12 (searched), Jos 2:22 (searched), Judg 6:29 (searched), Mar 1:36 (searched)
- **Observation 21750** (engagement, tag silence, status draft): 'searches' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 2 occurrence(s): Job 28:3 (searches), Job 39:8 (searches)
- **Observation 21753** (engagement, tag silence, status draft): 'searching' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 1 occurrence(s): Job 9:10 (searching)
- **Observation 21758** (engagement, tag silence, status draft): 'seek' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 11 occurrence(s): Lev 13:36 (seek), 1Sa 10:2 (seek), 1Sa 10:14 (seek), 1Sa 28:7 (seek), 1Ki 2:40 (seek), 2Ki 2:16 (seek), 2Ki 6:19 (seek), 1Ch 4:39 (seek), Pro 20:4 (seek), Isa 41:17 (seek), Luk 15:8 (seek)
- **Observation 21763** (engagement, tag silence, status draft): 'seeking' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 9 occurrence(s): Gen 37:15 (seeking), Gen 37:16 (seeking), Judg 4:22 (seeking), Job 24:5 (seeking), Psa 104:21 (seeking), Psa 109:10 (seeking), Luk 13:6 (seeking), Luk 13:7 (seeking), Act 13:11 (seeking)
- **Observation 21768** (engagement, tag silence, status draft): 'seeks' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 2 occurrence(s): Deu 22:2 (seeks), Pro 31:13 (seeks)
- **Observation 21773** (engagement, tag silence, status draft): 'sought' here only names a physical search or finding, a practical or judicial finding, a record search or reconnaissance; no inner-being operation is voiced by it.
  - applies to 13 occurrence(s): 1Sa 10:21 (sought), 2Sa 17:20 (sought), 1Ki 1:2 (sought), 1Ki 1:3 (sought), 2Ki 2:17 (sought), 2Ch 4:18 (sought), Ezr 2:62 (sought), Neh 7:64 (sought), Neh 12:27 (sought), Psa 37:36 (sought), Lam 1:19 (sought), Dan 4:36 (sought); and 1 more (sheet `Observation nodes`)
- **Observation 21776** (engagement, tag silence, status draft): 'come upon' here names an outward matter (an event arriving, a bodily feature, a being sought); no inner-being operation is voiced or qualified by it.
  - applies to 7 occurrence(s): Exo 10:12 (come upon), Deu 4:30 (come upon), Judg 13:5 (come upon), 2Sa 19:7 (come upon), Jer 13:22 (come upon), Jer 32:23 (come upon), 1Th 5:3 (come upon)
- **Observation 21786** (engagement, tag silence, status draft): 'more handsome' here names an outward matter (an event arriving, a bodily feature, a being sought); no inner-being operation is voiced or qualified by it.
  - applies to 1 occurrence(s): 1Sa 9:2 (more handsome)
- **Observation 21800** (engagement, tag silence, status draft): 'sought for' here names an outward matter (an event arriving, a bodily feature, a being sought); no inner-being operation is voiced or qualified by it.
  - applies to 1 occurrence(s): Eze 26:21 (sought for)
- **Observation 21734** (engagement, tag use, status draft): 'find' is here an act whose object is the inner being (God searching hearts, the spirit searching the innermost parts), or what is found is an inner state of the other (favour, mercy, rest, enjoyment, cheer); it bears on the inner being without being the operation.
  - applies to 27 occurrence(s): Gen 32:5 (find), Gen 33:8 (find), Gen 33:15 (find), Gen 34:11 (find), Exo 33:13 (find), Num 11:15 (find), Rut 1:9 (find), Rut 2:2 (find), 1Sa 1:18 (find), 1Sa 25:8 (find), 2Sa 15:25 (find), 2Sa 16:4 (find); and 15 more (sheet `Observation nodes`)
- **Observation 21735** (engagement, tag use, status draft): 'find' is here the finding of a person as the end of seeking (the Lord, wisdom); it names the outcome of the seeking, with the person as the relational target.
  - applies to 10 occurrence(s): Deu 4:29 (find), Job 23:3 (find), Job 37:23 (find), Pro 1:28 (find), Pro 2:5 (find), Pro 8:17 (find), Jer 29:13 (find), Hos 5:6 (find), Joh 7:34 (find), Joh 7:36 (find)
- **Observation 21737** (engagement, tag use, status draft): 'finds' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 1 occurrence(s): Job 33:10 (finds)
- **Observation 21738** (engagement, tag use, status draft): 'finds' is here an act whose object is the inner being (God searching hearts, the spirit searching the innermost parts), or what is found is an inner state of the other (favour, mercy, rest, enjoyment, cheer); it bears on the inner being without being the operation.
  - applies to 5 occurrence(s): Deu 24:1 (finds), Ecc 6:5 (finds), Song 8:10 (finds), Lam 1:3 (finds), Mat 12:43 (finds)
- **Observation 21743** (engagement, tag use, status draft): 'search' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 8 occurrence(s): 2Sa 5:17 (search), 1Ch 14:8 (search), Eze 34:6 (search), Eze 34:11 (search), Amo 9:3 (search), Zep 1:12 (search), Mat 2:8 (search), Joh 5:39 (search)
- **Observation 21744** (engagement, tag use, status draft): 'search' is here an act whose object is the inner being (God searching hearts, the spirit searching the innermost parts), or what is found is an inner state of the other (favour, mercy, rest, enjoyment, cheer); it bears on the inner being without being the operation.
  - applies to 2 occurrence(s): Psa 139:23 (search), Jer 17:10 (search)
- **Observation 21747** (engagement, tag use, status draft): 'searched' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 3 occurrence(s): 2Ch 22:9 (searched), Eze 34:8 (searched), 2Ti 1:17 (searched)
- **Observation 21748** (engagement, tag use, status draft): 'searched' is here an act whose object is the inner being (God searching hearts, the spirit searching the innermost parts), or what is found is an inner state of the other (favour, mercy, rest, enjoyment, cheer); it bears on the inner being without being the operation.
  - applies to 1 occurrence(s): Psa 139:1 (searched)
- **Observation 21751** (engagement, tag use, status draft): 'searches' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 1 occurrence(s): Job 13:9 (searches)
- **Observation 21752** (engagement, tag use, status draft): 'searches' is here an act whose object is the inner being (God searching hearts, the spirit searching the innermost parts), or what is found is an inner state of the other (favour, mercy, rest, enjoyment, cheer); it bears on the inner being without being the operation.
  - applies to 4 occurrence(s): 1Ch 28:9 (searches), Rom 8:27 (searches), 1Cor 2:10 (searches), Rev 2:23 (searches)
- **Observation 21754** (engagement, tag use, status draft): 'searching' is here an act whose object is the inner being (God searching hearts, the spirit searching the innermost parts), or what is found is an inner state of the other (favour, mercy, rest, enjoyment, cheer); it bears on the inner being without being the operation.
  - applies to 1 occurrence(s): Pro 20:27 (searching)
- **Observation 21759** (engagement, tag use, status draft): 'seek' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 16 occurrence(s): Deu 12:5 (seek), 1Sa 23:25 (seek), 1Sa 24:2 (seek), 1Sa 26:2 (seek), 1Sa 26:20 (seek), 1Ki 18:10 (seek), Job 3:4 (seek), Job 7:21 (seek), Job 10:6 (seek), Psa 119:176 (seek), Isa 34:16 (seek), Isa 41:12 (seek); and 4 more (sheet `Observation nodes`)
- **Observation 21764** (engagement, tag use, status draft): 'seeking' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 1 occurrence(s): 1Pe 5:8 (seeking)
- **Observation 21769** (engagement, tag use, status draft): 'seeks' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 1 occurrence(s): Ecc 3:15 (seeks)
- **Observation 21774** (engagement, tag use, status draft): 'sought' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 7 occurrence(s): Gen 43:30 (sought), 1Sa 23:14 (sought), 1Sa 27:4 (sought), Jer 50:20 (sought), Eze 22:30 (sought), Eze 34:4 (sought), Dan 2:13 (sought)
- **Observation 21775** (engagement, tag use, status draft): 'searching' is here the outward search or pursuit through which a purpose is carried out (a hunt for a person, God's search for the lost or for sin, the neglect of such a search); it is the outward act, and the inner intent or care is named by other words or only implied.
  - applies to 1 occurrence(s): Luk 2:48 (searching)
- **Observation 21777** (engagement, tag use, status draft): 'come upon' is here an outward act carried out against another party, enacting a hostile purpose; the purpose is told by the verse's other words.
  - applies to 1 occurrence(s): 2Ch 13:13 (come upon)
- **Observation 21778** (engagement, tag use, status draft): 'come upon' is here the coming (negated) of an inner state of another, the wrath of the Lord; it bears on the inner being without being the operation.
  - applies to 1 occurrence(s): 2Ch 32:26 (come upon)
- **Observation 21780** (engagement, tag use, status draft): 'find compassion' is here the finding or the naming of an inner state of the other (compassion, regard); it bears on the inner being without being the operation.
  - applies to 1 occurrence(s): 2Ch 30:9 (find compassion)
- **Observation 21782** (engagement, tag use, status draft): 'look for' is here an outward search for a person as the end of the search; the person sought is the relational target.
  - applies to 2 occurrence(s): Act 9:11 (look for), Act 11:25 (look for)
- **Observation 21784** (engagement, tag use, status draft): 'looking for' is here an outward search for a person as the end of the search; the person sought is the relational target.
  - applies to 2 occurrence(s): Act 10:19 (looking for), Act 10:21 (looking for)
- **Observation 21788** (engagement, tag use, status draft): 'searched for' is here an outward act carried out against another party, enacting a hostile purpose; the purpose is told by the verse's other words.
  - applies to 1 occurrence(s): Act 12:19 (searched for)
- **Observation 21789** (engagement, tag use, status draft): 'searching for' is here an outward search for a person as the end of the search; the person sought is the relational target.
  - applies to 1 occurrence(s): Luk 2:45 (searching for)
- **Observation 21794** (engagement, tag use, status draft): 'seek out' is here an outward search for a person as the end of the search; the person sought is the relational target.
  - applies to 1 occurrence(s): 1Sa 16:16 (seek out)
- **Observation 21799** (engagement, tag use, status draft): 'seeks out' is here an outward search for a person as the end of the search; the person sought is the relational target.
  - applies to 1 occurrence(s): Isa 40:20 (seeks out)
- **Observation 21802** (engagement, tag use, status draft): 'sought out' is here an outward search for a person as the end of the search; the person sought is the relational target.
  - applies to 1 occurrence(s): Est 2:2 (sought out)
- **Observation 21803** (engagement, tag use, status draft): 'sought out' is here the finding or the naming of an inner state of the other (compassion, regard); it bears on the inner being without being the operation.
  - applies to 1 occurrence(s): Isa 62:12 (sought out)

### 4.2 Other recorded observations (158)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 20884** (Analysis_phase_1, tag face, status draft): Seek here is seeking to find something or someone (tree H1245 1a1 'to seek to find').
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20886** (Analysis_phase_1, tag statement, status draft): The seeking is a pursuit: Joseph is looking for something.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20889** (Analysis_phase_1, tag party, status draft): Joseph is the one seeking; the man who found him is the one who asks about it.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20890** (Analysis_phase_1, tag statement, status draft): Joseph has been sent by Israel to see how his brothers fare (Gen 37:14) and is alone when the man finds him.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20892** (Analysis_phase_1, tag statement, status draft): Joseph is taken to be seeking something; the question assumes it.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20893** (Analysis_phase_1, tag link, status draft): Joseph is found wandering about; the man then asks what he seeks.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20894** (Analysis_phase_1, tag link, status draft): The question draws out the seeking that the verse has not yet named.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 20895** (Analysis_phase_1, tag statement, status draft): Discovery: what Joseph is seeking is not stated in this verse; the passage gives it.
  - applies to 1 occurrence(s): Gen 37:15 (seeking)
- **Observation 12658** (prior-capture, tag statement, status draft): Fear leads to the hand held back (the wish unchanged): "The young man did not draw his sword, for he was afraid"; "although they were seeking to arrest him, they feared the crowds"
  - applies to 1 occurrence(s): Mat 21:46 (seeking)
- **Observation 12662** (prior-capture, tag statement, status draft): Fear leads to turned to trust, or to seeking god: "When I am afraid, I put my trust in you"; "Jehoshaphat was afraid and set his face to seek the Lord"; "Lord, save me"
  - applies to 1 occurrence(s): 2Ch 20:3 (seek)
- **Observation 12725** (prior-capture, tag face, status draft): Face AG. Delivered from fears (1 / 1 hits and verses; surfaces fears): Sought, answered, delivered.
  - applies to 1 occurrence(s): Psa 34:4 (sought)
- **Observation 12895** (prior-capture, tag face, status draft): Face of aph (H0639), The face lifted in pride: The face/nose raised (Psa 10:4 ("In the pride of his face the wicked does not seek him")). Pride is the nose held high (S, lexical).
  - applies to 1 occurrence(s): Psa 10:4 (seek)
- **Observation 13003** (prior-capture, tag statement, status draft): The answer it meets: "A soft answer turns away wrath"; "A gift in secret averts anger"; Moses' plea; "when he humbled himself the wrath of the Lord turned from him"; Aaron's reason, "And when Moses heard that, he approved"; Naaman's servants; "His father came out and entreated him"; Jesus called the ten; Gamaliel's counsel. Or none: "I sought for a man … but I found none"; "I looked, but there was no one to help".
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 13019** (prior-capture, tag statement, status draft): The leader bears it differently from the people (v2, U2 §65 point 4): Moses: "But the Lord was angry with me because of you"; Aaron "stood between the dead and the living"; David: "let your hand be against me and against my father's house"; and none found: "I sought for a man among them who should build up the wall and stand in the breach before me for the land … but I found none".
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 13035** (prior-capture, tag statement, status draft): A person's anger leads to an act at once, with the hand: Moses "threw the tablets out of his hands and broke them"; Balaam "struck the donkey with his staff"; Bigthan and Teresh "sought to lay hands on King Ahasuerus".
  - applies to 1 occurrence(s): Est 2:21 (sought)
- **Observation 13082** (prior-capture, tag statement, status draft): The humbling that turned the wrath, and the heart still not set: "And he did evil, for he did not set his heart to seek the Lord".
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 13150** (prior-capture, tag link, status draft): Sequence in Eze 22:17–31: dross → melted in the furnace → every rank has failed → "I sought for a man … and stand in the breach … but I found none" → indignation poured out.
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 13197** (prior-capture, tag link, status draft): What sets a person's anger off: demand → anger → "Am I in the place of God" (Gen 30:1–2); no regard → very angry → face fell (Gen 4:5); saw no homage → filled with fury → sought to destroy all the Jews (Est 3:5–6); "I thought" → rage (2Ki 5:11–12); afraid → withdraw → enraged (Dan 11:30); heard → filled with wrath → drove him out (Luk 4:28–29); passions at war within → quarrels (Jam 4:1).
  - applies to 1 occurrence(s): Est 3:6 (sought)
- **Observation 13200** (prior-capture, tag link, status draft): What does not turn it: godless, folly spoken → anger not turned (Isa 9:17); Manasseh's provocations → did not turn from the burning (2Ki 23:26); sought a man to stand in the breach → found none → poured out my indignation (Eze 22:30–31).
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 13398** (prior-capture, tag link, status draft): saw no homage → filled with fury → sought to destroy all the Jews (Est 3:5–6); glad of heart → saw → filled with wrath (Est 5:9); "I thought" → rage (2Ki 5:11–12).
  - applies to 1 occurrence(s): Est 3:6 (sought)
- **Observation 13554** (prior-capture, tag link, status draft): sought a man to stand in the breach → found none → poured out my indignation (Eze 22:30–31); move the landmark → wrath poured out like water (Hos 5:10).
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 13579** (prior-capture, tag link, status draft): angry → put them in custody (Gen 40:2–3); refused to come → enraged → counsel → decree (Est 1:12–19); angry → commanded the wise men destroyed → they sought Daniel (Dan 2:12–13); provokes him → forfeits his life (Pro 20:2).
  - applies to 1 occurrence(s): Dan 2:13 (sought)
- **Observation 13582** (prior-capture, tag link, status draft): afraid → withdraw → turn back → enraged → take action (Dan 11:30); "It is a lie" → would not listen → enraged → beat, imprisoned (Jer 37:14–15); became angry → sought to lay hands on the king (Est 2:21).
  - applies to 1 occurrence(s): Est 2:21 (sought)
- **Observation 13963** (prior-capture, tag statement, status draft): Outside: 2Ch 19:3 "set your heart to seek God" (genuine; C v3 §7.1, §11).
  - applies to 1 occurrence(s): 2Ch 19:3 (seek)
- **Observation 14034** (prior-capture, tag statement, status draft): What it leads to. Arrest (Act 4:3), the reframing (above), and in Joh 7:25, the people's question, "Is not this the man whom they seek to kill?". The indignation borders on the plan to kill. Compare Mar 3:6 (§32).
  - applies to 1 occurrence(s): Joh 7:25 (seek)
- **Observation 14093** (prior-capture, tag statement, status draft): Seeking favour: "Jehoahaz sought the favor of the Lord, and the Lord listened to him, for he saw the oppression of Israel" (2Ki 13:4).
  - applies to 1 occurrence(s): 2Ki 13:4 (sought)
- **Observation 14102** (prior-capture, tag statement, status draft): Humbling that is partial. Rehoboam is spared destruction but made to serve Shishak, "that they may know my service and the service of the kingdoms" (2Ch 12:8). Bronze shields replace gold (12:10). And "he did evil, for he did not set his heart to seek the Lord" (12:14). The humbling turned the wrath, and the heart was still not set.
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 14106** (prior-capture, tag statement, status draft): 2Ch 12:14 "did not set his heart to seek the Lord".
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 14191** (prior-capture, tag statement, status draft): (c) Rebuked by a holy person: Asa, told by the seer that he "relied on the king of Syria", "was angry with the seer and put him in the stocks … for he was in a rage with him" (2Ch 16:10). The rage spreads: "Asa inflicted cruelties upon some of the people at the same time" (16:10); Uzziah, withstood by the priests at the altar: "Uzziah was angry … and when he became angry with the priests, leprosy broke out on his forehead" (2Ch 26:19); In both, the anger is against the messenger of a boundary, and the story ends with the angry king's own body struck: Asa "diseased in his feet … Yet even in his disease he did not seek the Lord" (16:12); Uzziah "a leper to the day of his death" (26:21).
  - applies to 1 occurrence(s): 2Ch 16:12 (seek)
- **Observation 14199** (prior-capture, tag statement, status draft): What it does to those beneath it: Pleading against it before it rises:; Judah: "let not your anger burn against your servant, for you are like Pharaoh himself" (Gen 44:18). The plea is a long retelling of the father's love (44:19–21 onward); Rachel: "Let not my lord be angry that I cannot rise before you, for the way of women is upon me" (Gen 31:35). The plea for no anger covers a concealment: she is sitting on the stolen gods (31:34); Reading it as a sign: "If he says, 'Good!' it will be well with your servant, but if he is angry, then know that harm is determined by him" (1Sa 20:7). Saul's anger is to be read as the evidence of Saul's intent. Jonathan's knowledge follows the same path: aft ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Est 2:21 (sought)
- **Observation 14224** (prior-capture, tag statement, status draft): Part 2 verses: what they add. Three new strands: (a) The eye wasting, as in Job 17:7; "My eye wastes away because of grief; it grows weak because of all my foes" (Psa 6:7), after "every night I flood my bed with tears" (6:6); "My eye is wasted from grief; my soul and my body also. For my life is spent with sorrow" (Psa 31:9–10); The eye is where ka'as shows in the body, in all three texts (Job 17:7; Psa 6:7; 31:9); What turns Psa 6 round is being heard: "the Lord has heard the sound of my weeping. The Lord has heard my plea" (6:8–9). In Psa 10:14, "you do see, for you note mischief and vexation, that you may take it into your hands; to you the helpless commits himself". The vexation is seen ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Ecc 2:24 (find)
- **Observation 14269** (prior-capture, tag statement, status draft): Part 2 verses: what they add (both were B8: human vexation induced by God): Paul reads Deu 32:21 as a statement about understanding: "But I ask, did Israel not understand? First Moses says, 'I will make you jealous of those who are not a nation; with a foolish nation I will make you angry'" (Rom 10:19). Then "I have been found by those who did not seek me" (10:20), and "All day long I have held out my hands to a disobedient and contrary people" (10:21); The induced anger is set inside God's outstretched hands. It is a provocation meant to bring them back, not only a punishment; Compare Deu 32:29, "If they were wise, they would understand this"; God troubles the nations' hearts at another's f ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Rom 10:20 (seek)
- **Observation 14271** (prior-capture, tag statement, status draft): What it does: It reads the rival's heart as evil: Eliab, "I know your presumption and the evil of your heart, for you have come down to see the battle" (1Sa 17:28); It reckons the rival's future: Saul, "They have ascribed to David ten thousands, and to me they have ascribed thousands, and what more can he have but the kingdom?" (18:8); It attacks one's own son as the rival's ally: "You son of a perverse, rebellious woman … as long as the son of Jesse lives … neither you nor your kingdom shall be established" (20:30–31); It jeers: Sanballat "was angry and greatly enraged, and he jeered at the Jews … 'What are these feeble Jews doing?'" (Neh 4:1–2); It enlarges its target: Haman "disdained to ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Est 3:6 (sought)
- **Observation 14314** (prior-capture, tag statement, status draft): What it leads to. Arrest (Act 4:3), the reframing (above), and in Joh 7:25, the people's question, "Is not this the man whom they seek to kill?". The indignation borders on the plan to kill. Compare Mar 3:6.
  - applies to 1 occurrence(s): Joh 7:25 (seek)
- **Observation 14470** (prior-capture, tag statement, status draft): VX §8 (Psa 10:14; 31:9; Ecc 1:18; 2:23; 7:3; 11:10; Col 3:21; Eph 6:4): Context seats: sense · batch · use: Psa 10:13 "say in his heart": offender's · C v3 §9.4 · used. Psa 31:7 "distress of my soul": bearer's own · E v2 §10.1 · used. Ecc 1:16–17 heart · E v2 §1.3, B v3 §1.2 · used. Ecc 2:22 heart · new · used. Ecc 2:24 "find" [make his soul see good] · new · used (enjoyment as answer). Ecc 5:16 "wind" · spurious. Ecc 7:2, 7:4 heart · A v3 §3.3 · used. Ecc 11:9 heart · F v4 §7, H v1 §4.1 · used. Eph 6:5–6, Col 3:22–23 "heart … heartily" (bondservants) · E v2 §6, H v1 §3.1 · not used (next household rule).
  - applies to 1 occurrence(s): Ecc 2:24 (find)
- **Observation 14478** (prior-capture, tag statement, status draft): SK §21: Context seats: sense · batch · use: Pro 6:16 "to him" [his nephesh: God's] · new · not used. Pro 21:10 "soul of the wicked desires evil" · D v2 §2.3, C v3 §1.10 · not used. Pro 21:23 "keeps himself" · new · not used. Pro 26:23 evil heart · D v2 §2.2 · used. Pro 29:10 "seek the life" · C v3 R2, §5.1 · not used. Pro 29:23 "lowly in spirit" · A v3 §5, D v2 §9.2 · not used. Pro 29:24 "hates his own life" · F v4 §3.1 · not used.
  - applies to 1 occurrence(s): Pro 29:10 (seek)
- **Observation 14563** (prior-capture, tag statement, status draft): What it does: Given over: "he gave them over to plunderers … so that they could no longer withstand their enemies … And they were in terrible distress" (Judg 2:14–15); Crying out: "when the people of Israel cried out to the Lord, the Lord raised up a deliverer" (Judg 3:9); "We have sinned against you, because we have forsaken our God" (10:10); "do to us whatever seems good to you. Only please deliver us this day" (10:15); Seeking favour: "Jehoahaz sought the favor of the Lord, and the Lord listened to him, for he saw the oppression of Israel" (2Ki 13:4); Relapsing: "whenever the judge died, they turned back and were more corrupt than their fathers … They did not drop any of their practices o ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Ki 13:4 (sought)
- **Observation 14576** (prior-capture, tag statement, status draft): How it co-exists: Humbling with a confession of God's justice: "The Lord is righteous" (2Ch 12:6); "you are just" (Ezr 9:15); Humbling with the body: torn clothes and weeping (Josiah); Humbling that is partial. Rehoboam is spared destruction but made to serve Shishak, "that they may know my service and the service of the kingdoms" (2Ch 12:8). Bronze shields replace gold (12:10). And "he did evil, for he did not set his heart to seek the Lord" (12:14). The humbling turned the wrath, and the heart was still not set.
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 14578** (prior-capture, tag statement, status draft): Seat: In the verse: 2Ch 32:25 "his heart was proud" and 32:26 "the pride of his heart". Hezekiah's own. Genuine. A v3 §2.2; D v2 §9.1, §10.1, §11; pilot §2; Outside (all genuine, the bearer's own):; 1Ki 8:47–48 / 2Ch 6:37–38 "turn their heart … with all their heart and with all their soul"; 2Ki 22:19 / 2Ch 34:27 "your heart was penitent / tender"; 2Ch 12:14 "did not set his heart to seek the Lord"; Nothing new in any single seat. What part A adds is a third kind of seat for pilot §2. The pilot has the heart that provokes (the cause) and the spirit that receives (the effect). Part A adds the heart that turns, and so turns the anger away. In these verses, and in §22, it is the human seat most ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 14589** (prior-capture, tag statement, status draft): What it does: Removal: Josiah "removed all the shrines … which kings of Israel had made, provoking the Lord to anger" (2Ki 23:19); Covenant formed in the heart: "Now it is in my heart to make a covenant with the Lord … in order that his fierce anger may turn away from us. My sons, do not now be negligent" (2Ch 29:10–11); A call to return: "Do not now be stiff-necked as your fathers were, but yield yourselves to the Lord … that his fierce anger may turn away from you. For if you return … your brothers and your children will find compassion" (2Ch 30:8–9); Separation: "Let our officials stand for the whole assembly … until the fierce wrath of our God over this matter is turned away from us" (Ez ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): 2Ch 19:3 (seek), 2Ch 30:9 (find compassion)
- **Observation 14593** (prior-capture, tag statement, status draft): Seat: In the verse: 2Ch 29:10 "it is in my heart to make a covenant". Hezekiah's own. Genuine. A v3 §2.2; E v2 §7.1; Outside: 2Ch 19:3 "set your heart to seek God"; The seat of reform is where the intent to turn is formed. This joins §19 (see there).
  - applies to 1 occurrence(s): 2Ch 19:3 (seek)
- **Observation 14594** (prior-capture, tag statement, status draft): What it does. "For I was ashamed to ask the king for a band of soldiers … since we had told the king, 'The hand of our God is for good on all who seek him, and the power of his wrath is against all who forsake him'" (Ezr 8:22).
  - applies to 1 occurrence(s): Ezr 8:22 (seek)
- **Observation 14595** (prior-capture, tag statement, status draft): How it co-exists. Fasting and humbling: "I proclaimed a fast … that we might humble ourselves before our God, to seek from him a safe journey" (8:21). "we fasted and implored our God for this, and he listened" (8:23).
  - applies to 1 occurrence(s): Ezr 8:21 (seek)
- **Observation 14610** (prior-capture, tag statement, status draft): How it co-exists: Isolation. "He has put my brothers far from me … My relatives have failed me, my close friends have forgotten me" (19:13–14). "Men have gaped at me with their mouth" (16:10); Not being able to see God. "Behold, he passes by me, and I see him not" (9:11). "If I summoned him and he answered me, I would not believe that he was listening to my voice" (9:16); A wish not to have been born. "Why did you bring me out from the womb?" (10:18). "leave me alone, that I may find a little cheer" (10:20); Hope beyond the anger, in the same breath. "Oh that you would hide me in Sheol, that you would conceal me until your wrath be past, that you would appoint me a set time, and remember me! ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 10:20 (find)
- **Observation 14670** (prior-capture, tag statement, status draft): What it does: "Behold, the day of the Lord comes, cruel, with wrath and fierce anger" (Isa 13:9); "the Lord is enraged against all the nations" (34:2); "the peaceful folds are devastated because of the fierce anger of the Lord" (Jer 25:37); The human side:; "Therefore all hands will be feeble, and every human heart will melt. They will be dismayed: pangs and agony will seize them … They will look aghast at one another; their faces will be aflame" (Isa 13:7–8); "like a hunted gazelle, or like sheep with none to gather them, each will turn to his own people, and each will flee to his own land" (13:14); "No refuge will remain for the shepherds … the cry of the shepherds, and the wail of the lor ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 49:37 (seek)
- **Observation 14692** (prior-capture, tag statement, status draft): Part C: Eze 14:19; 22:24; 22:31: "I found none": "And I sought for a man among them who should build up the wall and stand in the breach before me for the land, that I should not destroy it, but I found none. Therefore I have poured out my indignation upon them" (Eze 22:30–31, context read); Ezekiel uses the image of Psa 106:23, to say that no one did; Before it, every group is named as having failed: prophets (22:25, 28), priests (22:26), princes (22:27), the people of the land (22:29); Even the righteous could not stand for others: "even if Noah, Daniel, and Job were in it … they would deliver neither son nor daughter. They would deliver but their own lives by their righteousness" (14:20); ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 14839** (prior-capture, tag statement, status draft): (v3) Eze 22:17–31: Sequence the text gives: dross → melted in the furnace → every rank has failed → "I sought for a man … and stand in the breach … but I found none" → indignation poured out; Phenomena: FU · NI.
  - applies to 1 occurrence(s): Eze 22:30 (sought)
- **Observation 14893** (prior-capture, tag statement, status draft): 2Ch 19:2 (RF): Context seat: 2Ch 19:3 "set your heart to seek God"; Whose · check: Jehoshaphat's · genuine; Already read in: C v3 §7.1, §11; §: §22.
  - applies to 1 occurrence(s): 2Ch 19:3 (seek)
- **Observation 15087** (prior-capture, tag statement, status draft): These verses join pride to the turning away from God: Pride is a witness against its owner. "The pride of Israel testifies to his face; yet they do not return to the Lord their God, nor seek him, for all this" (Hos 7:10; also Hos 5:5); It goes with not knowing. The verse before says "Strangers devour his strength, and he knows it not; gray hairs are sprinkled upon him, and he knows it not" (Hos 7:9). In Hos 5:4–5, "they know not the Lord" stands next to "The pride of Israel testifies to his face"; Pride does not listen; "Hear and give ear; be not proud, for the Lord has spoken" (Jer 13:15). The opposite of pride here is hearing; Then: "if you will not listen, my soul will weep in secret for ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Hos 7:10 (seek)
- **Observation 15117** (prior-capture, tag statement, status draft): It has no room for God: "In the pride of his face the wicked does not seek him; all his thoughts are, 'There is no God'" (Psa 10:4); "his soul is puffed up; it is not upright within him, but the righteous shall live by his faith" (Hab 2:4). Then: "an arrogant man who is never at rest. His greed is as wide as Sheol" (2:5). The swollen soul is set against faith, and joined to restlessness and greed.
  - applies to 1 occurrence(s): Psa 10:4 (seek)
- **Observation 15118** (prior-capture, tag statement, status draft): It is seen in the eyes, the walk and the house: "Haughty eyes and a proud heart, the lamp of the wicked, are sin" (Pro 21:4). It follows "the Lord weighs the heart" (21:2); "Whoever has a haughty look and an arrogant heart I will not endure" (Psa 101:5); The daughters of Zion "walk with outstretched necks, glancing wantonly with their eyes" (Isa 3:16), in the same oracle as "the spoil of the poor is in your houses" (3:14); "he who makes his door high seeks destruction" (Pro 17:19); "How sick is your heart ... the deeds of a brazen prostitute" (Eze 16:30).
  - applies to 1 occurrence(s): Pro 17:19 (seeks)
- **Observation 15123** (prior-capture, tag statement, status draft): Rising up, with God not set before them. "insolent men have risen up against me; a band of ruthless men seeks my life, and they do not set you before them" (Psa 86:14). The answer is "But you, O Lord, are a God merciful and gracious" (86:15).
  - applies to 1 occurrence(s): Psa 86:14 (seeks)
- **Observation 15138** (prior-capture, tag statement, status draft): A heart lifted up in the ways of the Lord. Jehoshaphat "sought the God of his father and walked in his commandments ... His heart was courageous in the ways of the Lord" (2Ch 17:4–6). The word is gābah, the one used for Uzziah's and Hezekiah's proud hearts: I read: the lifting is the same; the direction differs. Jehoshaphat's heart rose in God's ways and against the high places, not above God; This is a change of character (#1919).
  - applies to 1 occurrence(s): 2Ch 17:4 (sought)
- **Observation 15195** (prior-capture, tag statement, status draft): The boast is not removed. It is moved: The command. "Let the one who boasts, boast in the Lord" (1Co 1:31; 2Co 10:17). This follows Christ "who became to us wisdom from God, righteousness and sanctification and redemption" (1:30). It is joined to "it is not the one who commends himself who is approved, but the one whom the Lord commends" (2Co 10:18); What to boast in; "let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight" (Jer 9:24); The boast is in knowing God, and what is known is his character; The soul's boast. "My soul makes its boast in the Lord; let th ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): 1Ch 16:10 (seek), Psa 105:3 (seek)
- **Observation 15205** (prior-capture, tag statement, status draft): Proverbs paints the scoffer by what he will not receive: Rebuke; "A wise son hears his father's instruction, but a scoffer does not listen to rebuke" (Pro 13:1); "A scoffer does not like to be reproved; he will not go to the wise" (15:12). The verse before is "Sheol and Abaddon lie open before the Lord; how much more the hearts of the children of man!" (15:11); Hatred of correction. "Whoever corrects a scoffer gets himself abuse ... Do not reprove a scoffer, or he will hate you; reprove a wise man, and he will love you" (Pro 9:7–8). The same rebuke brings out hate in one and love in the other; Wisdom in vain. "A scoffer seeks wisdom in vain, but knowledge is easy for a man of understanding" ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Pro 14:6 (seeks)
- **Observation 15266** (prior-capture, tag statement, status draft): Turns toward help (Deu 33:26): Human pride: Turns away from God: "does not seek him" (Psa 10:4).
  - applies to 1 occurrence(s): Psa 10:4 (seek)
- **Observation 15336** (prior-capture, tag statement, status draft): What goes with it: saying "The Lord is righteous" (2Ch 12:6); tearing clothes, sackcloth, fasting, going about "dejectedly" (1Ki 21:27); weeping (2Ki 22:19); entreating and praying (2Ch 33:12–13); fasting and seeking (Ezr 8:21); the condition "humble themselves, and pray and seek my face and turn from their wicked ways" (2Ch 7:14); confession, and making amends for iniquity (Lev 26:40–41).
  - applies to 2 occurrence(s): 2Ch 7:14 (seek), Ezr 8:21 (seek)
- **Observation 15337** (prior-capture, tag statement, status draft): In Ezra the fast to humble themselves follows a choice not to lean on the king: "I was ashamed to ask the king for a band of soldiers … since we had told the king, 'The hand of our God is for good on all who seek him'" (Ezr 8:22).
  - applies to 1 occurrence(s): Ezr 8:22 (seek)
- **Observation 15342** (prior-capture, tag statement, status draft): It does not last by itself. Of Rehoboam, two verses after his humbling: "he did evil, for he did not set his heart to seek the Lord" (2Ch 12:14).
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 15384** (prior-capture, tag statement, status draft): The humble seek: "Seek the Lord, all you humble of the land, who do his just commands; seek righteousness; seek humility; perhaps you may be hidden on the day of the anger of the Lord" (Zep 2:3). Those already called humble are told to seek humility. I read: in this verse humility is not a thing held once and for all. The humble keep seeking it, under the threat of the day of anger (2:2); "I will leave in your midst a people humble and lowly. They shall seek refuge in the name of the Lord" (Zep 3:12). They are left after God removes "your proudly exultant ones" (3:11). They are described by what they do and do not do: "they shall do no injustice and speak no lies" (3:13); "The afflicted shal ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Psa 22:26 (seek), Psa 69:32 (seek)
- **Observation 15385** (prior-capture, tag statement, status draft): The humble hear what God did for another, and are glad: "My soul makes its boast in the Lord; let the humble hear and be glad" (Psa 34:2). David's own deliverance follows: "I sought the Lord, and he answered me" (34:4). The superscription sets it after "he changed his behavior before Abimelech"; "When the humble see it they will be glad" (Psa 69:32). "It" is the deliverance of the speaker, who has said "I am afflicted and in pain" (69:29); I read: in both psalms, one man's boast is in the Lord, not in himself, and the humble are those who are glad at it. Their gladness is at what God did for someone else.
  - applies to 1 occurrence(s): Psa 34:4 (sought)
- **Observation 15747** (prior-capture, tag statement, status draft): Dominating H6184's 15 verses, cruelty is the property of oppressors and adversaries named from the position of the sufferer asking to be delivered from them: redeem me from the hand of the ruthless (Job 6:23); a band of ruthless men seeks my life (Ps 86:14); redeem you from the grasp of the ruthless (Jer 15:21).
  - applies to 1 occurrence(s): Psa 86:14 (seeks)
- **Observation 16052** (prior-capture, tag statement, status draft): Psa 69:32 (filed under "you who seek God, let your hearts revive"): seeing God's help to the humble
  - applies to 1 occurrence(s): Psa 69:32 (seek)
- **Observation 16085** (prior-capture, tag statement, status draft): What the sequences show [Claude reading]: The oath marks adherence at a cost.; Elisha's triple oath is the price of the double spirit.; The Shunammite uses Elisha's own oath against him. Her bitterness of soul becomes a hold on the prophet that he cannot refuse.; Uriah's oath by David's soul is kept against David's wish. The wine that should have lowered his guard fails (a failed threshold — Batch F §7). He dies for keeping it.; The oath by the soul can guard a life while refusing a life. Zedekiah swears secretly by "who made our souls" to spare Jeremiah's life. He then declines the life offered to him (38:17, 20), from fear (38:19). The oath and the refusal are in one conversation.; 1Sa 17: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Sa 4:8 (sought)
- **Observation 16211** (prior-capture, tag statement, status draft): 16.10 Life risked "to death" for others — the OT precedent: "Zebulun is a people who risked their lives to the death" (Judg 5:18). This is in the same song as "March on, my soul, with might!" (5:21; §3.2).; "Our life for yours even to death!" (Jos 2:14; §4 revisit); David "took his life in his hand" against the Philistine (1Sa 19:5); The men to David: "If half of us die, they will not care [*set heart*] about us. But you are worth ten thousand of us" (2Sa 18:3). The enemy's heart is indifferent to many deaths. One life is weighed at ten thousand.; "the men who were seeking your life are dead" (Exo 4:19) → Moses returns (4:20). The death of the hunters frees the hunted life.; "Why then are yo ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Exo 4:19 (seeking)
- **Observation 16214** (prior-capture, tag statement, status draft): A dead man honoured for his grandfather's heart: Ahaziah "was put to death. They buried him, for they said, 'He is the grandson of Jehoshaphat, who sought the Lord with all his heart'" (2Ch 22:9)
  - applies to 1 occurrence(s): 2Ch 22:9 (sought)
- **Observation 16318** (prior-capture, tag statement, status draft): 4.1 Serving with all the heart and all the soul: "to serve the Lord your God with all your heart and with all your soul" (Deu 10:12; 11:13; Jos 22:5); "serve him with a whole heart and with a willing mind [*soul*], for the Lord searches all hearts" (1Ch 28:9); "serve him faithfully with all your heart" (1Sa 12:24; 12:20); "direct your heart to the Lord and serve him only" (1Sa 7:3)
  - applies to 1 occurrence(s): 1Ch 28:9 (searches)
- **Observation 16380** (prior-capture, tag statement, status draft): Made with heart and soul: "to keep his commandments … with all his heart and all his soul" (2Ki 23:3; 2Ch 34:31); "a covenant to seek the Lord … with all their heart and with all their soul" (2Ch 15:12); "Now it is in my heart to make a covenant with the Lord" (2Ch 29:10)
  - applies to 1 occurrence(s): 2Ch 15:12 (seek)
- **Observation 16486** (prior-capture, tag statement, status draft): Beatitudes of the inner seat: "Blessed are the poor in spirit" (Mat 5:3) [H1]; "Blessed are the pure in heart" (Mat 5:8); "Blessed is the man … in whose spirit there is no deceit" (Psa 32:2) [H1]; "Blessed are those … who seek him with their whole heart" (Psa 119:2); "Blessed are those whose strength is in you, in whose heart are the highways to Zion" (Psa 84:5) — the heart as a road; "Blessed is the one who fears the Lord always, but whoever hardens his heart will fall into calamity" (Pro 28:14); "Blessed are you, Simon Bar-Jonah! For flesh and blood has not revealed this to you" (Mat 16:17)
  - applies to 1 occurrence(s): Psa 119:2 (seek)
- **Observation 16555** (prior-capture, tag statement, status draft): Unhappy business: "I applied my heart to seek … It is an unhappy business" (Ecc 1:13); "applying my heart … when man had power over man to his hurt" (Ecc 8:9).
  - applies to 1 occurrence(s): Ecc 1:13 (seek)
- **Observation 16578** (prior-capture, tag statement, status draft): Consequence as a heart-question: "if you say in your heart, 'Why have these things come upon me?' it is for the greatness of your iniquity" (Jer 13:22).
  - applies to 1 occurrence(s): Jer 13:22 (come upon)
- **Observation 16592** (prior-capture, tag statement, status draft): Hunted without sin: "What is my guilt? … that he seeks my life?" (1Sa 20:1); "I have not sinned against you, though you hunt my life" (1Sa 24:11); "they lie in wait for my life … For no transgression or sin of mine" (Psa 59:3)
  - applies to 1 occurrence(s): 1Sa 20:1 (seeks)
- **Observation 16647** (prior-capture, tag statement, status draft): Heart over rules of cleanness: "who sets his heart to seek God … even though not according to the sanctuary's rules of cleanness" (2Ch 30:19).
  - applies to 1 occurrence(s): 2Ch 30:19 (seek)
- **Observation 16654** (prior-capture, tag statement, status draft): Heart glad in the holy name: "our heart is glad in him, because we trust in his holy name" (Psa 33:21); "let the hearts of those who seek the Lord rejoice" (1Ch 16:10; Psa 105:3); "gladness of heart … when a holy feast is kept" (Isa 30:29).
  - applies to 2 occurrence(s): 1Ch 16:10 (seek), Psa 105:3 (seek)
- **Observation 16700** (prior-capture, tag statement, status draft): Insolent men seek the life: "insolent men have risen up against me; a band of ruthless men seeks my life" (Psa 86:14).
  - applies to 1 occurrence(s): Psa 86:14 (seeks)
- **Observation 16712** (prior-capture, tag statement, status draft): Humble hearts revive: "When the humble see it they will be glad; you who seek God, let your hearts revive" (Psa 69:32); "The afflicted shall eat and be satisfied … May your hearts live forever!" (Psa 22:26).
  - applies to 2 occurrence(s): Psa 22:26 (seek), Psa 69:32 (seek)
- **Observation 16753** (prior-capture, tag statement, status draft): The formula "into the hand of those who seek their life" (Jer 19:7; 21:7; 22:25; 34:20–21; 38:16; 44:30; 46:26) → Batch G §5.3.
  - applies to 8 occurrence(s): Jer 19:7 (seek), Jer 21:7 (seek), Jer 22:25 (seek), Jer 34:20 (seek), Jer 34:21 (seek), Jer 38:16 (seek), Jer 44:30 (seek), Jer 46:26 (seek)
- **Observation 16754** (prior-capture, tag statement, status draft): A reward for murder refused: the murderers of Ish-bosheth: "your enemy, who sought your life. The Lord has avenged my lord the king" (2Sa 4:8) → David: "As the Lord lives, who has redeemed my life out of every adversity" → he has them killed (4:9–12). The claim of vengeance on David's behalf is answered by an oath on David's own redeemed soul.
  - applies to 1 occurrence(s): 2Sa 4:8 (sought)
- **Observation 16774** (prior-capture, tag statement, status draft): Life: "surrender … your life shall be spared" (Jer 38:17); "they seek my life, to take it away" (1Ki 19:10, 14); "Why do you commit this great evil against yourselves?" (Jer 44:7)
  - applies to 2 occurrence(s): 1Ki 19:10 (seek), 1Ki 19:14 (seek)
- **Observation 16837** (prior-capture, tag statement, status draft): Jeremiah's sequence — context read, Jer 20:7–14: "you have deceived me" (7); "there is in my heart as it were a burning fire shut up in my bones … I cannot [hold it in]" (9); "my close friends, watching for my fall … 'take our revenge on him'" (10); → "let me see your vengeance … to you have I committed my cause" (12); → "Sing to the Lord; praise the Lord! For he has delivered the life of the needy" (13); → "Cursed be the day on which I was born!" (14); Jer 11:18–21 has the same prayer, and names "the men of Anathoth, who seek your life" (21).; [Claude reading]; Vengeance changes value with the heart that holds it. In the Philistines' soul it is malice. In God's heart it stands in one line w ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 11:21 (seek)
- **Observation 16862** (prior-capture, tag statement, status draft): Night one: "On my bed by night I sought him whom my soul loves; I sought him, but found him not … I will rise now … I will seek him whom my soul loves … Have you seen him whom my soul loves? … I found him whom my soul loves. I held him, and would not let him go" (Song 3:1–4). Also Song 1:7.
  - applies to 2 occurrence(s): Song 3:2 (seek), Song 3:2 (sought)
- **Observation 16863** (prior-capture, tag statement, status draft): Night two (context Song 5:2–6): "I slept, but my heart was awake. A sound! My beloved is knocking" (5:2); She delays: "I had put off my garment; how could I put it on?" (5:3); "My beloved put his hand to the latch, and my heart was thrilled within me" (5:4); "I opened … but my beloved had turned and gone. My soul failed me [*went out*] when he spoke. I sought him, but found him not" (5:6)
  - applies to 1 occurrence(s): Song 5:6 (sought)
- **Observation 16982** (prior-capture, tag statement, status draft): 12.2 The heart devising and muttering violence — one verb, opposite content: *hāgâ* "mutter, meditate" [lexical]: "The heart of the righteous ponders how to answer, but the mouth of the wicked pours out evil things" (Pro 15:28); "for their hearts devise [*mutter*] violence, and their lips talk of trouble" (Pro 24:2); "conceiving and uttering from the heart lying words" (Isa 59:13); "Your heart will muse on the terror" (Isa 33:18); "those who seek my life … meditate treachery all day long" (Psa 38:12); [Claude reading] The heart's inner murmuring is the same act for the righteous and the violent. Its content (how to answer / violence / lies / terror) decides its moral character. The heart is ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 38:12 (seek)
- **Observation 16995** (prior-capture, tag statement, status draft): 0. Data notes: Pre-filters from the handoff do not apply here. None of "Holy Spirit" (M61), "declares the Lord" (M42) or "Lord of hosts" (M72) falls in Batch C clusters. Nothing was removed.; "Seek my life" is one idiom, not inner seeking. About 40 of the 96 M83 verses are *biqqēš nephesh* — "seek (someone's) life" (1Sa 20:1; 23:15; 1Ki 19:10, 14; Jer 11:21; 19:7; 21:7; 22:25; 34:20–21; 44:30; 46:26; 49:37; Psa 35:4; 38:12; 40:14; 54:3; 63:9; 70:2; 86:14; Mat 2:20; Rom 11:3; etc.). Here *nephesh* is life as the object of hostile pursuit. It is reported in §7.5 and not mixed with the soul that seeks.; "Lacks sense" is "lacking heart" (H2638 + H3820A, d1): Pro 7:7; 9:4, 16; 10:13, 21; 11:12; 1 ... (cut; the whole text is in the workbook)
  - applies to 21 occurrence(s): 1Sa 20:1 (seeks), 1Sa 23:15 (seek), 1Ki 19:10 (seek), 1Ki 19:14 (seek), Psa 35:4 (seek), Psa 38:12 (seek), Psa 40:14 (seek), Psa 54:3 (seek), Psa 63:9 (seek), Psa 70:2 (seek), Psa 86:14 (seeks), Jer 11:21 (seek); and 9 more (sheet `Observation nodes`)
- **Observation 17004** (prior-capture, tag statement, status draft): Soul yearns, spirit seeks: "My soul yearns for you in the night; my spirit within me earnestly seeks you" (Isa 26:9) [H1]
  - applies to 1 occurrence(s): Isa 26:9 (earnestly seeks)
- **Observation 17024** (prior-capture, tag statement, status draft): Wanting to save the soul-life loses it: "whoever would save his life will lose it" (Mat 16:25; Mar 8:35; Luk 9:24); "Whoever seeks to preserve his life" (Luk 17:33, §7).
  - applies to 1 occurrence(s): Luk 17:33 (seeks)
- **Observation 17029** (prior-capture, tag statement, status draft): Zeal and the threatened life: "I have been very jealous for the Lord … they seek my life" (1Ki 19:10, 14).
  - applies to 2 occurrence(s): 1Ki 19:10 (seek), 1Ki 19:14 (seek)
- **Observation 17056** (prior-capture, tag statement, status draft): Plans and the inner seat: "they plot to take my life" (Psa 31:13); "devise evil against me … seek after my life" (Psa 35:4).
  - applies to 1 occurrence(s): Psa 35:4 (seek)
- **Observation 17057** (prior-capture, tag statement, status draft): 2.2 The intention of the heart: "every intention of the thoughts of his heart was only evil continually" (Gen 6:5); "the intention of man's heart is evil from his youth" (Gen 8:21) — said by the Lord "in his heart"; "keep forever such purposes and thoughts in the hearts of your people, and direct their hearts toward you" (1Ch 29:18); "the Lord searches all hearts and understands every plan and thought" (1Ch 28:9); "disclose the purposes of the heart" (1Co 4:5)
  - applies to 1 occurrence(s): 1Ch 28:9 (searches)
- **Observation 17086** (prior-capture, tag statement, status draft): Blameless soul-life: "I am blameless; I regard not myself; I loathe my life" (Job 9:21) — integrity with self-rejection; "Bloodthirsty men hate one who is blameless and seek the life of the upright" (Pro 29:10).
  - applies to 1 occurrence(s): Pro 29:10 (seek)
- **Observation 17096** (prior-capture, tag statement, status draft): 6.1 The soul waits and hopes: "I wait for the Lord, my soul waits, and in his word I hope" (Psa 130:5); "Our soul waits for the Lord" (Psa 33:20); "For God alone, O my soul, wait in silence, for my hope is from him" (Psa 62:5); "My soul longs for your salvation; I hope in your word" (Psa 119:81); "we wait for you; your name … the desire of our soul" (Isa 26:8); "The Lord is good to those who wait for him, to the soul who seeks him" (Lam 3:25); "your hope will not be cut off" — wisdom "to your soul" (Pro 24:14)
  - applies to 1 occurrence(s): Lam 3:25 (seeks)
- **Observation 17106** (prior-capture, tag statement, status draft): 7.1 Seeking the Lord with heart and soul: "you will find him, if you search after him with all your heart and with all your soul" (Deu 4:29); "a covenant to seek the Lord … with all their heart and with all their soul" (2Ch 15:12); "sworn with all their heart … sought him with their whole desire" (2Ch 15:15); "You will seek me and find me, when you seek me with all your heart" (Jer 29:13); "With my whole heart I seek you" (Psa 119:10); "who seek him with their whole heart" (Psa 119:2); "he sought the Lord with all his heart" (2Ch 22:9); "seeking his God, he did with all his heart" (2Ch 31:21)
  - applies to 8 occurrence(s): Deu 4:29 (search), 2Ch 15:12 (seek), 2Ch 15:15 (sought), 2Ch 22:9 (sought), 2Ch 31:21 (seeking), Psa 119:2 (seek), Psa 119:10 (seek), Jer 29:13 (seek)
- **Observation 17107** (prior-capture, tag statement, status draft): Setting the heart to seek (cf. Batch B §0.1): "set your mind and heart [*heart and soul*] to seek the Lord" (1Ch 22:19); "those who had set their hearts to seek the Lord" (2Ch 11:16); "you … have set your heart to seek God" (2Ch 19:3); "who sets his heart to seek God … even though not according to the sanctuary's rules" (2Ch 30:19); "Ezra had set his heart to study [*seek*] the Law" (Ezr 7:10); Failure: "he did evil, for he did not set his heart to seek the Lord" (2Ch 12:14)
  - applies to 5 occurrence(s): 1Ch 22:19 (seek), 2Ch 11:16 (seek), 2Ch 12:14 (seek), 2Ch 19:3 (seek), 2Ch 30:19 (seek)
- **Observation 17109** (prior-capture, tag statement, status draft): Seeking hearts rejoice / revive: "let the hearts of those who seek the Lord rejoice" (1Ch 16:10; Psa 105:3); "you who seek God, let your hearts revive" (Psa 69:32); "May your hearts live forever" (Psa 22:26).
  - applies to 4 occurrence(s): 1Ch 16:10 (seek), Psa 22:26 (seek), Psa 69:32 (seek), Psa 105:3 (seek)
- **Observation 17111** (prior-capture, tag statement, status draft): 7.2 The soul that seeks — longing in motion: "earnestly I seek you; my soul thirsts for you; my flesh faints for you" (Psa 63:1); "My soul yearns for you in the night; my spirit within me earnestly seeks you" (Isa 26:9) [H1]; "I sought him whom my soul loves; I sought him, but found him not" (Song 3:1–2); "My soul failed me when he spoke. I sought him, but found him not" (Song 5:6); "which my soul has sought repeatedly, but I have not found" (Ecc 7:28); "In the day of my trouble I seek the Lord … my soul refuses to be comforted" (Psa 77:2)
  - applies to 6 occurrence(s): Psa 63:1 (seek), Psa 77:2 (seek), Ecc 7:28 (sought), Song 3:2 (sought), Song 5:6 (sought), Isa 26:9 (earnestly seeks)
- **Observation 17112** (prior-capture, tag statement, status draft): 7.3 The heart seeks knowledge: "The heart of him who has understanding seeks knowledge" (Pro 15:14); "An intelligent heart acquires knowledge" (Pro 18:15); "I applied my heart to seek and to search out by wisdom" (Ecc 1:13); "I turned my heart to know and to search out and to seek wisdom" (Ecc 7:25)
  - applies to 3 occurrence(s): Pro 15:14 (seeks), Ecc 1:13 (seek), Ecc 7:25 (seek)
- **Observation 17113** (prior-capture, tag statement, status draft): A heart: "The Lord has sought out a man after his own heart" (1Sa 13:14).
  - applies to 1 occurrence(s): 1Sa 13:14 (sought out)
- **Observation 17114** (prior-capture, tag statement, status draft): Worshippers in spirit: "the true worshipers will worship the Father in spirit and truth, for the Father is seeking such people" (Joh 4:23) [D1+H2].
  - applies to 1 occurrence(s): Joh 4:23 (seeking)
- **Observation 17115** (prior-capture, tag statement, status draft): Offspring: "a portion of the Spirit in their union … what was the one God seeking? Godly offspring. So guard yourselves in your spirit" (Mal 2:15) [U+H1].
  - applies to 1 occurrence(s): Mal 2:15 (seeking)
- **Observation 17118** (prior-capture, tag statement, status draft): David: 1Sa 20:1; 22:23; 23:15; 25:29; 2Sa 4:8; 16:11 ("my own son seeks my life").
  - applies to 2 occurrence(s): 1Sa 20:1 (seeks), 2Sa 16:11 (seeks)
- **Observation 17122** (prior-capture, tag statement, status draft): NT: "those who sought the child's life are dead" (Mat 2:20) — echoing "all the men who were seeking your life are dead" (Exo 4:19).
  - applies to 2 occurrence(s): Exo 4:19 (seeking), Mat 2:20 (sought)
- **Observation 17124** (prior-capture, tag statement, status draft): Hostile psalms place the same *nephesh* in both roles: "those who seek my life … shall go down into the depths" (Psa 63:9), eight verses after "my soul thirsts for you" (Psa 63:1).
  - applies to 2 occurrence(s): Psa 63:1 (seek), Psa 63:9 (seek)
- **Observation 17125** (prior-capture, tag statement, status draft): 7.5 "Seek my life" — the soul-life hunted (§0.2): [Claude reading] One word is both the seeker of God (§7.2) and the object hunted by enemies. The *nephesh* is the person's life, which can long and can be taken.; "Whoever seeks to preserve his life will lose it" (Luk 17:33).; "Seek them not … I am bringing disaster upon all flesh … But I will give you your life as a prize of war" (Jer 45:5).; "Haman stayed to beg [*seek*] for his life" (Est 7:7).
  - applies to 1 occurrence(s): Luk 17:33 (seeks)
- **Observation 17128** (prior-capture, tag statement, status draft): Sign-seeking grieves the spirit: "he sighed deeply in his spirit and said, 'Why does this generation seek a sign?'" (Mar 8:12) [H1].
  - applies to 1 occurrence(s): Mar 8:12 (seek)
- **Observation 17129** (prior-capture, tag statement, status draft): The spirit that seeks rest: "When the unclean spirit has gone out of a person, it passes through waterless places seeking rest, and finding none it says, 'I will return to my house'" (Mat 12:43; Luk 11:24) [O]. An other-spirit is depicted as seeking a person as its dwelling.
  - applies to 2 occurrence(s): Mat 12:43 (seeking), Luk 11:24 (seeking)
- **Observation 17130** (prior-capture, tag statement, status draft): 7.6 Illegitimate and restless seeking: "the Spirit said to him, 'Behold, three men are looking for you'" (Act 10:19) [D2]; "It may be that the Spirit of the Lord has caught him up" (2Ki 2:16) [D1]; "his Spirit has gathered them. Seek and read" (Isa 34:16) [D1].
  - applies to 3 occurrence(s): 2Ki 2:16 (seek), Isa 34:16 (seek), Act 10:19 (looking for)
- **Observation 17175** (prior-capture, tag statement, status draft): 11. Cross-cutting observations for Batch C [Claude reading]: God is shown with his own soul and heart of desire and choice: his soul delights in the chosen servant (Isa 42:1), his heart is set on the chosen house (2Ch 7:16), he seeks a man after his heart (1Sa 13:14), his heart is grieved (Gen 6:6).; Other spirits in this batch act on orientation from outside: spirit of jealousy (Num 5), spirit of whoredom (Hos 4:12; 5:4) [X]; harmful spirit from God (1Sa 16) and the spirit at work in the disobedient (Eph 2:2) [O]; the unclean spirit seeking a dwelling (Mat 12:43) [O].; Fringe worth keeping: desire as breath-hunger — "striving after wind" (§1.9); the wine-merry heart as the point of exposure ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Mat 12:43 (seeking)
- **Observation 17236** (prior-capture, tag statement, status draft): d. Thinking, planning, understanding, remembering: *Plans and devising:* Pro 16:1, 9; 19:21; 6:14, 18; 24:2; 12:20; Psa 140:2; 58:2; Zec 7:10; 8:17; Isa 10:7; Act 5:4; Eze 38:10.; *Understanding and knowing:*; "a heart to understand" (Deu 29:4); "understanding mind" (1Ki 3:9); "understand with their hearts" (Isa 6:10; Mat 13:15; Joh 12:40; Act 28:27); "an intelligent heart acquires knowledge" (Pro 18:15); "the heart of the hasty will understand" (Isa 32:4); *Remembering and "laying to heart":*; Isa 47:7; 57:1, 11; 42:25; Mal 2:2; Jer 12:11; Ecc 7:2; 9:1; Deu 4:39; 32:46; 1Sa 21:12; "call to mind" (Lam 3:21; Deu 30:1); "come into mind" (Jer 3:16; 7:31; 19:5; 32:35; 44:21; 51:50; Isa 65:17); H ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Ecc 1:13 (seek), Ecc 7:25 (seek)
- **Observation 17270** (prior-capture, tag statement, status draft): 3.1 Parallel and interchangeable (poetic pairing): *Heart // spirit:*; "Create in me a clean heart … renew a right spirit within me" (Psa 51:10); "a broken spirit; a broken and contrite heart" (Psa 51:17); "brokenhearted … crushed in spirit" (Psa 34:18); "revive the spirit of the lowly … the heart of the contrite" (Isa 57:15); "my spirit faints within me; my heart within me is appalled" (Psa 143:4); "Every heart will melt … every spirit will faint" (Eze 21:7); "heart was not steadfast … spirit was not faithful" (Psa 78:8); "meditate in my heart … my spirit made a diligent search" (Psa 77:6); "whose heart stirred him … whose spirit moved him" (Exo 35:21); "gladness of heart … pain of heart … ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 26:9 (earnestly seeks)
- **Observation 17271** (prior-capture, tag statement, status draft): 3.1 Parallel and interchangeable (poetic pairing): [Claude reading] The translators move between heart, soul, spirit and mind when rendering the same Hebrew or Greek word. That movement is itself evidence that the words' ranges overlap.
  - applies to 1 occurrence(s): Isa 26:9 (earnestly seeks)
- **Observation 17289** (prior-capture, tag statement, status draft): 3. (a) Why the verses were not narrated: The reason is the same as for M47. The M25 units read the life and death words. The desire side of each verse was left for this strand. The M25 ledgers often quote the verse in full, but they quote it for its life or death word: Psa 34:12, "desires life", is quoted for "long days" (LD-101).; Joh 4:14, "never be thirsty again", is quoted for "living water" (LD-121).; Ecc 5:18, "find enjoyment", is quoted for "life enjoyed, as given" (LD-115). That ledger line was woven into Ch 2. 10.6 gained Ecc 2:24–26 in the M47 pass, but not the three verses that say the same thing (3:12; 5:18; 8:15).; Three verses (Exo 14:12, Psa 34:12, Pro 8:35–36) also have a Ch ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Ecc 2:24 (find)
- **Observation 17451** (prior-capture, tag statement, status draft): 9. Where desire ends, and what it is set against (10.6 *Evil desire*): *"What the wicked dreads will come upon him, but the desire of the righteous will be granted"* (Pro 10:24). Dread and desire stand against each other.; *"Whoever isolates himself seeks his own desire; he breaks out against all sound judgment"* (Pro 18:1).; *"All day long he craves and craves, but the righteous gives and does not hold back"* (Pro 21:26). This is the verse after *"The desire of the sluggard kills him"*. The craving that never ends is set against giving that does not hold back.; *"How long … will scoffers delight in their scoffing"* (Pro 1:22). This goes in the delight list.
  - applies to 1 occurrence(s): Pro 18:1 (seeks)
- **Observation 17453** (prior-capture, tag statement, status draft): Refuge in the wrong place. *"See the man who would not make God his refuge, but trusted in the abundance of his riches and sought refuge in his own destruction!"* (Psa 52:7). I read the irony as the psalm's own: what he ran to was his ruin.
  - applies to 1 occurrence(s): Psa 52:7 (sought refuge)
- **Observation 17632** (prior-capture, tag statement, status draft): Looks right: "they seek me daily and delight to know my ways, as if they were a nation that did righteousness … they delight to draw near to God" (Isa 58:2). The next verse, already in 10.6, is "you seek your own pleasure, and oppress all your workers" (58:3). The delight is real enough to be named twice. I read that delight in religion can sit beside oppression without either one cancelling the other in the person's own eyes.
  - applies to 1 occurrence(s): Isa 58:2 (seek)
- **Observation 17834** (prior-capture, tag statement, status draft): Ecc 12:10–12 | 10.2 | words of delight sought; words of the wise as goads and fixed nails, from one Shepherd. I read the figure as two works on the hearer: they move and they fix
  - applies to 1 occurrence(s): Ecc 12:10 (sought)
- **Observation 17872** (prior-capture, tag statement, status draft): What the verses do with the want. It is not answered with more days. It is answered with the mouth and the will: *"Keep your tongue from evil and your lips from speaking deceit. Turn away from evil and do good; seek peace and pursue it"* (34:13–14). The psalmist is teaching "the fear of the Lord" (34:11). So the want for life is put inside a lesson about fearing God, and it is worked out first in speech.
  - applies to 1 occurrence(s): Psa 34:14 (seek)
- **Observation 17873** (prior-capture, tag statement, status draft): Compare: two kinds of wanting in the same psalm. *"The young lions suffer want and hunger; but those who seek the Lord lack no good thing"* (34:10). The lions are the picture of strength, and they still go hungry. I read the figure as a want that strength cannot satisfy, set against a want that is met in seeking.
  - applies to 1 occurrence(s): Psa 34:10 (seek)
- **Observation 17937** (prior-capture, tag statement, status draft): What lies behind refusing. *"you refuse to come to me that you may have life"* (Joh 5:40). The passage gives what lies behind it: *"you do not have the love of God within you"* (5:42); *"How can you believe, when you receive glory from one another and do not seek the glory that comes from the only God?"* (5:44); The will refuses because the desire is set elsewhere, on glory from people. That is in the verses, not read in. They had searched the Scriptures (5:39), so the refusal is not a lack of knowing.
  - applies to 1 occurrence(s): Joh 5:44 (seek)
- **Observation 17959** (prior-capture, tag statement, status draft): What the delight does.: It warns: *"Saul my father seeks to kill you"* (19:2).; It stands beside the father (19:3).; It speaks well: *"Let not the king sin against his servant David"* (19:4).; It reminds Saul of his own past joy: *"You saw it, and rejoiced"* (19:5).; Saul listens and swears, *"he shall not be put to death"* (19:6). I read delight in a person turning into intercession, carried out at risk inside a family.
  - applies to 1 occurrence(s): 1Sa 19:2 (seeks)
- **Observation 17979** (prior-capture, tag statement, status draft): One desire, narrowed. *"One thing have I asked of the Lord, that will I seek after: that I may dwell in the house of the Lord all the days of my life, to gaze upon the beauty of the Lord and to inquire in his temple"* (Psa 27:4).
  - applies to 1 occurrence(s): Psa 27:4 (seek)
- **Observation 18131** (prior-capture, tag statement, status draft): A heart that is a trap (Ecc 7:26). *"And I find something more bitter than death: the woman whose heart is snares and nets, and whose hands are fetters. He who pleases God escapes her, but the sinner is taken by her."*: It is the Preacher's own finding, after *"I turned my heart to know and to search out"* (7:25), *"which my soul has sought repeatedly"* (7:28).; The figure is a hunter's: snares and nets for a heart, fetters for hands.; A heart can be a trap set for another person's desire. Escape is tied to "he who pleases God", not to strength of will.
  - applies to 1 occurrence(s): Ecc 7:28 (sought)
- **Observation 18133** (prior-capture, tag statement, status draft): The soul's portion, and waiting (Lam 3:24–26). *"'The Lord is my portion,' says my soul, 'therefore I will hope in him.' The Lord is good to those who wait for him, to the soul who seeks him. It is good that one should wait quietly for the salvation of the Lord."*: The soul speaks to itself, which is a voice to the soul (Ch 11 §5).; "Portion" is the same as in Psa 16:5.; Twice the goodness belongs to waiting. I read that waiting is where the soul's hope is placed, and that "good" is said both of the Lord and of the waiting.
  - applies to 1 occurrence(s): Lam 3:25 (seeks)
- **Observation 18135** (prior-capture, tag statement, status draft): A mixed verdict (2Ch 19:2–3). *"Should you help the wicked and love those who hate the Lord? Because of this, wrath has gone out against you from the Lord. Nevertheless, some good is found in you, for you destroyed the Asheroth out of the land, and have set your heart to seek God."* A love wrongly given and a heart set to seek God stand in one king, and the prophet's verdict holds both.
  - applies to 1 occurrence(s): 2Ch 19:3 (seek)
- **Observation 18537** (prior-capture, tag statement, status draft): C24 | D04 verses with an inner word. God "searches mind and heart" as he strikes (Rev 2:23). Ezekiel falls on his face at Pelatiah's death: "will you make a full end?" (Eze 11:13). Saul "did not seek guidance from the Lord. Therefore the Lord put him to death" (1Ch 10:14). One "spared to weep his eyes out to grieve his heart" (1Sa 2:33). | Rev 2:23; Eze 11:13; 1Ch 10:14; 1Sa 2:33 | 13.1 (Rev 2:23, 1Ch 10:14); 10.9 (Eze 11:13). The other 9 D04 verses are data.
  - applies to 1 occurrence(s): 1Ch 10:14 (seek)
- **Observation 18594** (prior-capture, tag statement, status draft): What they add: Lost and perishing are one word. The lost sheep, coin and son of Luk 15 (15:4, 8, 24, 32), "to seek and to save the lost" (Luk 19:10), "should not perish" (Joh 3:16), and the lost sheep of Israel (Psa 119:176; Jer 50:6; Eze 34:4, 16; Mat 10:6; 15:24). In Luk 15:24 the father sets "dead" beside "lost". Woven in *Death spoken of in more than one way*.; Perishing as a present state, set against being saved. 1Co 1:18; 2Co 2:15; 4:3; 2Th 2:10, with its stated cause: "because they refused to love the truth". Set against it is eternal life (Joh 3:16; 10:28). Woven in the same subsection.; Inner things perish. Hope (Job 8:13; Pro 10:28; Lam 3:18; Eze 19:5; 37:11), courage, literally t ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Psa 119:176 (seek), Eze 34:16 (seek), Luk 15:8 (seek), Luk 19:10 (seek)
- **Observation 18835** (prior-capture, tag statement, status draft): 1. Where the authority comes from: Pilate (Joh 19:10–11): *"So Pilate said to him, 'You will not speak to me? Do you not know that I have authority to release you and authority to crucify you?' Jesus answered him, 'You would have no authority over me at all unless it had been given you from above. Therefore he who delivered me over to you has the greater sin.'"*; The passage before: *"When Pilate heard this statement, he was even more afraid"* (19:8), after *"he has made himself the Son of God"* (19:7). He asks *"Where are you from?"*, and Jesus gives *"no answer"* (19:9). After: *"From then on Pilate sought to release him"*, and then the cry, *"you are not Caesar's friend"* (19:12).
  - applies to 1 occurrence(s): Joh 19:12 (sought)
- **Observation 18878** (prior-capture, tag statement, status draft): Hiding from people: Much of the hiding in Scripture is from people who could do harm, and in these verses it is the weaker side that hides. "When the wicked rise, people hide themselves" (Proverbs 28:28). "The poor of the earth all hide themselves" (Job 24:4). When Israel hid in the caves, "all the people followed him trembling" (1 Samuel 13:7).; Often the verse records not the feeling of the one who hides but someone else's counsel to hide.; Jonathan: "Saul my father seeks to kill you … Stay in a secret place and hide yourself" (1 Samuel 19:2).; God to Elijah: "hide yourself by the brook Cherith" (1 Kings 17:3).; Where the feeling is named, it is fear.; Jacob fled from Laban "secretly", and ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 19:2 (seeks)
- **Observation 19038** (prior-capture, tag statement, status draft): The passage. Dathan and Abiram refuse twice: *"We will not come up"* (16:12, 14). Moses before this, to Korah: *"would you seek the priesthood also?"* (16:10). After: *"Moses was very angry and said to the Lord, 'Do not respect their offering. I have not taken one donkey from them'"* (16:15).
  - applies to 1 occurrence(s): Num 16:10 (seek)
- **Observation 19108** (prior-capture, tag statement, status draft): Eze 34:4. *"The weak you have not strengthened, the sick you have not healed, the injured you have not bound up, the strayed you have not brought back, the lost you have not sought, and with force and harshness you have ruled them."*
  - applies to 1 occurrence(s): Eze 34:4 (sought)
- **Observation 19162** (prior-capture, tag statement, status draft): Ezra 8. The hand brings him the men he needed (8:18). He will not ask the king for soldiers; because he has said, "The hand of our God is for good on all who seek him" (8:22). 8:21–22 are in; 10.14.
  - applies to 1 occurrence(s): Ezr 8:22 (seek)
- **Observation 19166** (prior-capture, tag statement, status draft): 10.7 *Choosing and setting direction*: Ezra 7:10, setting the heart to study, do and teach. It is; a clear verse for the heart's direction, and it is not in the book. Rehoboam, who "did not set his; heart to seek the Lord" (2 Chronicles 12:14), is in 10.13 and 10.14, and is its opposite.
  - applies to 1 occurrence(s): 2Ch 12:14 (seek)
- **Observation 19193** (prior-capture, tag statement, status draft): (a) The fugitive hunted to death.; Verses: 1Sa 19:2; 20:5, 19, 24; 23:19, 23; 26:1; Psa 54:1 (David); Judg 9:5 (Jotham); 2Sa 17:9 (David, as Hushai pictures him); 1Ki 17:3 (Elijah); Jer 36:19 (Baruch and Jeremiah); Jos 2:16 (the spies); Jos 10:16, 17, 27 (five kings); 2Ch 22:9 (Ahaziah); Joh 8:59; 12:36 (Jesus).; Where it comes from: a stated threat to life. "Saul my father seeks to kill you" (1Sa 19:2); Abimelech "killed his brothers … But Jotham … hid himself" (Judg 9:5); "they picked up stones to throw at him" (Joh 8:59).; The feeling of the one who hides is almost never stated. What is stated is someone else's counsel to hide: Jonathan (1Sa 19:2), Rahab (Jos 2:16), the officials (Jer 36: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 1Sa 19:2 (seeks)
- **Observation 19201** (prior-capture, tag statement, status draft): Seat.; In the verse: 2Ch 22:9 "heart". The word has a genuine inner-being sense, but the heart is Jehoshaphat's, the dead grandfather's: "who sought the Lord with all his heart". Ahaziah, the one hiding, has no seat. Spurious for this phenomenon (v1 §0). Batch C v3 §7.1 read it as seeking the Lord with the heart. Batch G v3 §16.11 read it as "a dead man honoured for his grandfather's heart". Both readings stand. Neither concerns hiding.; Whose seat: none of the 40 hiders has one. In strand (a) the inner operation belongs to the counsellor, and it is shown by what the counsellor says, not by a seat word (v2, kept above).; Outside the verse — new in v3. In strand (a), the nearest seat word is ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Ch 22:9 (sought)
- **Observation 19240** (prior-capture, tag statement, status draft): What it leads to. Mostly, something from outside ends it: "While they were perplexed about this, behold, two men stood by them" (Luk 24:4); "the men … stood at the gate" and "the Spirit said to him" (Act 10:17, 19); "Peter, standing with the eleven, lifted up his voice" (Act 2:14); the queen names Daniel (Dan 5:10–12); Herod "sought to see him" (Luk 9:9); Perplexity ends when an interpreter or a meeting arrives.
  - applies to 1 occurrence(s): Luk 9:9 (sought)
- **Observation 19246** (prior-capture, tag statement, status draft): (a) Anxiety over provision (Mat 6:25, 27, 28, 31, 34; Luk 12:22, 25, 26, 29).; Where from: "what you will eat or what you will drink … what you will put on" (Mat 6:25).; What it does: nothing. "which of you by being anxious can add a single hour to his span of life?" (6:27 = Luk 12:25). It multiplies itself forward: "tomorrow will be anxious for itself" (6:34). It suspends the person: *meteōrizō*, "be held in suspense" (Luk 12:29).; What it co-exists with: "little faith" (Luk 12:28), and the Gentiles' seeking (Mat 6:32).; What displaces it: looking at birds and lilies (6:26, 28); knowing "your heavenly Father knows that you need them" (6:32); "seek first the kingdom" (6:33).; The seat is sta ... (cut; the whole text is in the workbook)
  - applies to 2 occurrence(s): Mat 6:32 (seek), Mat 6:33 (seek)
- **Observation 19249** (prior-capture, tag statement, status draft): (d) Care for others, valued as good.; "I have no one like him, who will be genuinely concerned for your welfare" (Phili 2:20), against "they all seek their own interests" (2:21).; "the daily pressure on me of my anxiety for all the churches" (2Cor 11:28). The next verse shows what that anxiety is: "Who is weak, and I am not weak? Who is made to fall, and I am not indignant?" (11:29). Anxiety for others is sharing in their condition.; "the members may have the same care for one another" (1Cor 12:25).; "that I may be less anxious" (Phili 2:28), in a chain of feeling between Epaphroditus, Paul and the Philippians (2:26–28).; A father: Kish "anxious about you, saying, 'What shall I do about my s ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Phili 2:21 (seek)
- **Observation 19406** (prior-capture, tag statement, status draft): Isaiah 65:12 — "chose what I did not delight in": This is an oracle. It opens with God, not with the people: *"I was ready to be sought by those who did not ask for me … I said, “Here I am, here I am,”"* (v1); *"I spread out my hands all the day to a rebellious people, who walk in a way that is not good, following their own devices"* (v2); The wrong choosing in v12 is made in front of a God who is calling and holding out his hands.; The oracle shows what they turned to instead: sacrifices *"in gardens"*, sitting *"in tombs"*, eating *"pig’s flesh"* (v3–4); a pride that says *"do not come near me, for I am too holy for you"* (v5); they *"forget my holy mountain"* and *"set a table for Fortune ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 65:1 (sought)
- **Observation 19415** (prior-capture, tag statement, status draft): 1.6 Plans for welfare, and thought for the one in need: *"For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope"* (Jer 29:11).; The verse looks ahead to *"When seventy years are completed"* (29:10).; It is followed by *"You will seek me and find me, when you seek me with all your heart"* (29:13).; *"As for me, I am poor and needy, but the Lord takes thought for me"* (Psa 40:17).; *"But God will not take away life, and he devises means so that the banished one will not remain an outcast"* (2Sa 14:14). The wise woman says it against the fact that *"We must all die"*.
  - applies to 1 occurrence(s): Jer 29:13 (seek)
- **Observation 19423** (prior-capture, tag statement, status draft): Seeking: after his plans for welfare, *"when you seek me with all your heart"* (Jer 29:13).
  - applies to 1 occurrence(s): Jer 29:13 (seek)
- **Observation 19501** (prior-capture, tag statement, status draft): Know and serve with the whole inner being. *"know the God of your father and serve him with a whole heart and with a willing mind, for the Lord searches all hearts and understands every plan and thought"* (1Ch 28:9).
  - applies to 1 occurrence(s): 1Ch 28:9 (searches)
- **Observation 19606** (prior-capture, tag statement, status draft): Psalm 105:43: "his chosen ones with singing": Psalm 105 is a call to remember. It is addressed to the chosen: *"Remember the wondrous works that he has done … O offspring of Abraham, his servant, children of Jacob, his chosen ones!"* (v5–6). It starts with the heart: *"let the hearts of those who seek the Lord rejoice!"* (v3).; The psalm's reason is God's own remembering: *"He remembers his covenant forever"* (v8); *"For he remembered his holy promise, and Abraham, his servant"* (v42); The verse follows straight on: *"So he brought his people out with joy, his chosen ones with singing"* (v43). The joy and singing are set on the people brought out. They come with being brought out, and the br ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Psa 105:3 (seek)
- **Observation 19621** (prior-capture, tag statement, status draft): Numbers 17:5: "Thus I will make to cease from me the grumblings of the people of Israel": The verse closes a long dispute over who God has chosen. It begins in Numbers 16. Korah and 250 chiefs, *"chosen from the assembly, well-known men"* (16:2; *qārîʾ*, H7148, "called"), rise up: *"Why then do you exalt yourselves above the assembly of the Lord?"* (16:3). Moses answers with God's choosing: *"The one whom he chooses he will bring near to him"* (16:5), and *"the man whom the Lord chooses shall be the holy one"* (16:7).; Moses names what is underneath the complaint: *"is it too small a thing for you that the God of Israel has separated you … And would you seek the priesthood also?"* (16:9–10). ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Num 16:10 (seek)
- **Observation 19642** (prior-capture, tag statement, status draft): What others do around a choice, in these verses: grumble against the chosen man, and God counts it as against himself (Num 16:11; 17:5, 10); seek more than they were given, and are jealous (Num 16:10; Psa 106:16); name a choice as shame, and are angry at what it costs them (1Sa 20:30–31); despise the chosen in the heart, by the eyes of people (2Sa 6:16, 20); despise and abhor the chosen servant (Isa 49:7); conclude from the chosen people's ruin that God rejected them, and despise them in their own sight (Jer 33:24); ask to share the joy of the chosen (Psa 106:5); not know God, and still be called and equipped for the sake of the chosen (Isa 45:4–5); offer an inner act, the humbling of the so ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Num 16:10 (seek)
- **Observation 19719** (prior-capture, tag statement, status draft): Israel and election: "Israel failed to obtain what it was seeking. The elect obtained it, but the rest were hardened" (Rom 11:7); "as regards election, they are beloved for the sake of their forefathers" (Rom 11:28)
  - applies to 1 occurrence(s): Rom 11:7 (seeking)
- **Observation 19940** (prior-capture, tag statement, status draft): Grumbling, and seeking more. When God's choice of Aaron was challenged, Moses named what lay under it: *"would you seek the priesthood also?"* (Num 16:10). The grumbling at Aaron was against God: *"What is Aaron that you grumble against him?"* (16:11), and God calls it *"the grumblings … which they grumble against you"*, to be made to *"cease from me"* (17:5). Psalm 106 names the inner act: *"men in the camp were jealous of Moses and Aaron"* (Psa 106:16). God's reply was to make the choice plain, with the staff that sprouted. Then the grumbling became terror: *"Are we all to perish?"* (Num 17:13).
  - applies to 1 occurrence(s): Num 16:10 (seek)
- **Observation 19956** (prior-capture, tag statement, status draft): Seeking, and not obtaining. *"Israel failed to obtain what it was seeking. The elect obtained it, but the rest were hardened"* (Rom 11:7). The rest were seeking. They were given *"eyes that would not see and ears that would not hear"* (11:8). Paul at once refuses the conclusion that this is the end: *"did they stumble in order that they might fall? By no means!"* (11:11). The remnant is chosen *"by grace"*, not works (11:5–6). The passage says how the elect were chosen. It does not say why the rest were not.
  - applies to 1 occurrence(s): Rom 11:7 (seeking)
- **Observation 19957** (prior-capture, tag statement, status draft): An inner act weighed by what God chooses: In one passage the inner act of the others is itself set against God's choosing. The people fast and ask, *"Why have we humbled ourselves, and you take no knowledge of it?"* (Isa 58:3). They *"delight to know my ways"* and *"delight to draw near to God"* (58:2). Yet *"in the day of your fast you seek your own pleasure, and oppress all your workers"* (58:3). Then: *"Is such the fast that I choose, a day for a person to humble himself?"* (58:5). "Humble himself" is the humbling of the soul, the same words as their own complaint. What God does choose is turned outward: *"to let the oppressed go free"*, *"to share your bread with the hungry"*, *"not to h ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 58:2 (seek)
- **Observation 19991** (prior-capture, tag statement, status draft): Rom 11:7 | seeking and not obtaining; hardened; not the end; chosen by grace | batch 3
  - applies to 1 occurrence(s): Rom 11:7 (seeking)
- **Observation 20019** (prior-capture, tag statement, status draft): 3.9 God sees the intention: *"the Lord searches all hearts and understands every plan and thought"* (1Ch 28:9).; *"the intention of man's heart is evil from his youth"* (Gen 8:21; also Gen 6:5).; *"he knows our frame; he remembers that we are dust"* (Psa 103:14). H3336 here is "frame", the thing formed.; *"will disclose the purposes of the heart"* (1Co 4:5).
  - applies to 1 occurrence(s): 1Ch 28:9 (searches)
- **Observation 20345** (prior-capture, tag statement, status draft): 1Ch 28:9 | ✅ Accurate | Include: corroborates and adds (#1986) | M18 willing mind (#1986); M83 seek
  - applies to 1 occurrence(s): 1Ch 28:9 (seek)
- **Observation 20370** (prior-capture, tag statement, status draft): Jeremiah 8:3: "Death shall be preferred to life": > Q1 citation: ⚠ Check. Ch 2 *Wanting to die*: "Under judgment, death is wished for and withheld". The verse says death "shall be preferred" (H0977, Niphal: *shall be chosen*). "Wished for" softens the choosing word, and "withheld" belongs to Rev 9:6 only, not to Jer 8:3.; >; > Q2 M64: Include: corroborates and adds. Corroborates Ch 2 *Wanting to die*. New: the preference is a choosing word, and the Lord declares it as part of a judgment, after the people had loved, served and gone after other things (v2).; >; > Q3 other M-codes: M25 life/death: carried in Ch 2. M58 evil, M43 declares, M72 hosts: no.; This follows the Topheth judgment (7:30–3 ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 8:2 (sought)
- **Observation 20455** (prior-capture, tag statement, status draft): 4. Knowing a thought is separate from producing it. 1 Corinthians 2:11 says only "the spirit of that person" knows a person's thoughts, and only God's Spirit knows God's. Separately, God searches and knows human thoughts (Psalm 139:23; 1 Chronicles 28:9; Psalm 94:11; 1 Corinthians 3:20), and so does Jesus (Luke 5:22, 6:8, 11:17; Matthew 9:4, 12:25).: *Caveat:* in 1 Corinthians 2:11 the Strong's number is G3588, the Greek article. The word "thoughts" is supplied by the translation; the Greek says "the things of a person."
  - applies to 1 occurrence(s): 1Ch 28:9 (searches)
- **Observation 20498** (prior-capture, tag statement, status draft): 6. Vertical: between God's thinking and human thinking.: God searches, knows and discerns thoughts (Ps 139:2, 23; 1 Chr 28:9; Heb 4:12).; God reckons (Gen 15:6; Ps 32:2).; God overrules: "you meant evil … God meant it for good" (Gen 50:20); "it is the purpose of the Lord that will stand" (Prov 19:21).; Human thought can also turn back toward God: "When I think on my ways, I turn my feet to your testimonies" (Ps 119:59).
  - applies to 1 occurrence(s): 1Ch 28:9 (searches)
- **Observation 20586** (reading, tag face, status draft): In 7:8 'seeks' is the second act of the series and is answered by 'finds'; the verse does not name what is sought.
  - applies to 1 occurrence(s): Mat 7:8 (seeks)
- **Observation 20587** (reading, tag term, status draft): G2212 zeteo, 'seeks': to look for, to search for something. Here it is the seeker's own pursuit, answered by finding.
  - applies to 1 occurrence(s): Mat 7:8 (seeks)
- **Observation 20588** (reading, tag face, status draft): 'finds' is what seeking yields in 7:8: the seeker comes upon what was sought.
  - applies to 1 occurrence(s): Mat 7:8 (finds)
- **Observation 20589** (reading, tag term, status draft): G2147 heurisko, 'finds': to find, to come upon what was looked for.
  - applies to 1 occurrence(s): Mat 7:8 (finds)
- **Observation 20594** (reading, tag qualification, status draft): What the three answers give the three acts in Mat 7:8: 'receives' gives asking its result of being given, 'finds' gives seeking its result of coming upon, 'opened' gives knocking its result of being let in; each act has its own answer.
  - applies to 2 occurrence(s): Mat 7:8 (seeks), Mat 7:8 (finds)

### 4.3 The retired catalogue observations (1180, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

| stage | tag | live observations |
|---|---|---|
| char-answers | answered-no-flag | 123 |
| char-answers | not-related-to-meaningful-word | 29 |
| char-answers | could-not-resolve | 6 |
| char-answers | needs_adjacent_verse_context | 2 |
| char-reading | verse-grouping | 6 |
| char-reading | surface-gloss-divergence | 6 |
| char-reading | difference-inference | 5 |
| char-reading | no-direct-connection | 4 |
| char-reading | tightly-related | 3 |
| char-subgroup | difference-inference | 2 |
| char-subgroup | attested-pre-nt | 1 |
| char-subgroup | not-related-to-meaningful-word | 1 |
| char-subgroup | surface-gloss-divergence | 1 |
| verse-reading | answered-no-flag | 296 |
| verse-reading | no-impact | 200 |
| verse-reading | no-direct-connection | 172 |
| verse-reading | tightly-related | 102 |
| verse-reading | sole-mcode-in-verse | 84 |
| verse-reading | surface-gloss-divergence | 80 |
| verse-reading | not-related-to-meaningful-word | 42 |
| verse-reading | alternative-meaning | 5 |
| verse-reading | difference-inference | 4 |
| verse-reading | cluster-pole-negative | 2 |
| verse-reading | cluster-pole-positive | 2 |
| verse-reading | qualifier-for-term | 1 |
| verse-reading | attested-pre-nt | 1 |

### 4.4 Withdrawn observations (1105)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 1104 |
| Analysis_phase_1 | 1 |

| reason as stored | observations |
|---|---|
| no change record | 1104 |
| the old form of parts is replaced by the nine items | 1 |

## 5. Claims and the narrative

43 claims rest on these occurrences: 2 on an observation of these words and 41 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (2)

- **C-331** (narrative, verdict New, status current, in narrative 1): God chooses a place to set his name, and his eyes and heart are there; the people's offerings, joy, judgement and prayer turn toward it, and the choice can be cast off and made again.
  - beyond the text: gathers the place verses of Deuteronomy, Kings, Chronicles and Zechariah into one account of the choosing
  - rests on: observation 5317 (verse-reading no-direct-connection, live; Deu 12:5)
  - told in: chapter 13.1 Divine, Choosing; chapter 10.7 Choosing and setting direction, Others around a choice
- **C-387** (narrative, verdict New, status current, in narrative 1): Giving oneself or one's goods can be turned to an idol, even in the Lord's name; a person becomes like what he gives himself to and loves, and separating from God is done with idols taken into the heart.
  - beyond the text: reads Hos 9:10 as the self shaped by what it loves
  - rests on: observation 7289 (char-answers answered-no-flag, live; Psa 10:4)
  - told in: chapter 12 When the inner being goes wrong, Idols taken inside; chapter 10.7 Choosing and setting direction, Dedicating

### 5.2 Claims reached by a verse only (41)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| 1-1 | Soul and spirit in synonymous parallel (Isa 26:9; Job 7:11; Luk 1:46–47) | Isa 26:9 | earnestly seeks H7836 | current | not told in a section |
| 2-14 | The soul is the needing self, and much of its need is for God: "My soul thirsts for you" (Psa 63:1); "To you, O Lord, I lift up my soul" (Psa 25:1); "Bless the Lord, O my soul" (Psa 103:1) (dep §2.2b) | Psa 63:1 | seek H0859A; seek H7836 | current | not told in a section |
| 2-15 | The spirit is prominent in worship and is what is committed to God at death (E §13.4). Pro 20:27 uses *neshamah* "breath", not *rûaḥ* [lexical], and is outside the reading. The human spirit is equally temper, trouble and provocation (Pro 29:11; Gen 41:8; Act 17:16) | Pro 20:27 | searching H2664 | current | chapter 02 Life, breath and death, Soul, spirit and heart at death (1 earlier telling(s) in the workbook) |
| 3-3 | The original itself cites "the Lord who made our souls" (Jer 38:16). Also: "The Spirit of God has made me, and the breath of the Almighty gives me life" (Job 33:4). Both are made by God. The distinct-origins argument does not hold | Jer 38:16 | seek H1245 | current | not told in a section |
| 10-5 | Seven conditions (2Ch 7:14) | 2Ch 7:14 | seek H1245 | withdrawn | not told in a section |
| C-87 | Each person answers for his own sin, and sin can be put away while a death still follows | John 8:21 | seek G2212 | current | chapter 02 Life, breath and death, Death and sin (2 earlier telling(s) in the workbook) |
| C-106 | Some verses say the dead know nothing, do not praise God and do not return | Ecclesiastes 9:10 | finds H4672 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-114 | The breath also gives understanding, and words come out on it | Proverbs 20:27 | searching H2664 | current | chapter 02 Life, breath and death, Breath lent, and held by God (1 earlier telling(s) in the workbook) |
| C-118 | Life and death are set before a person to choose; life is chosen by doing, seeking and holding on | Amos 5:4; Amos 5:14 | seek H1875 | current | chapter 02 Life, breath and death, Life set before a person (2 earlier telling(s) in the workbook) |
| C-120 | Wisdom marks where the way to death ends, and some of what kills a person is named from within | Proverbs 8:35-36 | finds H4672 | current | chapter 02 Life, breath and death, Life set before a person (3 earlier telling(s) in the workbook) |
| C-125 | The commonest form of the oath by life is "As the Lord lives" (39 verses); in six of them a second life is joined | 1 Samuel 25:26 | seek H1245 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-131 | Scripture counts a life in days and says what the days are for | Psalm 27:4 | seek H0853; seek H1245 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-132 | The world where life is lived is named "the land of the living" | 1 Samuel 25:29 | seek H1245 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-140 | The father sets "dead" beside "lost" and "alive" beside "found"; to perish and to be lost are one word | Luke 15:4; Luke 15:8; Luke 19:10 | finds G2147; seek G2212 | current | chapter 02 Life, breath and death, Death spoken of in more than one way (1 earlier telling(s) in the workbook) |
| C-167 | Humility is not a feeling in the verses; they speak of it as an act, a standing, a quality sought and walked in, a state of the spirit, a place taken, something done to a person, and God's own way | Zephaniah 2:3 | seek H1245 | current | chapter 10.14 Humility, (opening) (1 earlier telling(s) in the workbook) |
| C-168 | Humility is always set against a rising: the proud heart, the lifted-up self, the stiff neck, the haughty eyes | 2 Chronicles 32:25-26 | come upon H0935G | current | chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit; chapter 10.14 Humility, (opening) (2 earlier telling(s) in the workbook) |
| C-171 | Humbling happens in the heart; Hezekiah's is the same heart turning back from its own pride | 2 Chronicles 32:25-26 | come upon H0935G | current | chapter 04 The heart, The heart and anger; chapter 10.7 Choosing and setting direction, Willing; chapter 10.13 Anger, The heart that turns, and the heart that does not; chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit; chapter 10.14 Humility, Where it happens; chapter 04 The heart, The heart humbled (6 earlier telling(s) in the workbook) |
| C-175 | God sees the one who humbles himself and answers, in measure; the humbling does not hold by itself | 2 Chronicles 12:14 | seek H1875 | current | chapter 10.13 Anger, The heart that turns, and the heart that does not; chapter 10.14 Humility, God sees it, and answers in measure; chapter 10.9 Relating to God, Humbling oneself before God (4 earlier telling(s) in the workbook) |
| C-176 | The humbling God does not take knowledge of is kept alongside self-pleasure and oppression and leaves the seen naked uncovered; Ahab's, against himself when the word came, was answered | Isaiah 58:3-7 | seek H4672 | current | chapter 10.7 Choosing and setting direction, Others around a choice; chapter 13.1 Divine, Choosing; chapter 10.14 Humility, A humbling God does not take knowledge of (3 earlier telling(s) in the workbook) |
| C-183 | Humility is not held once for all: the humble are told to seek it | Zephaniah 2:3 | seek H1245 | current | chapter 10.13 Anger, Shelter, and who can stand; chapter 10.14 Humility, The humble (2 earlier telling(s) in the workbook) |
| C-184 | The humble are glad at what God did for another | Psalm 34:4; Psalm 69:29-32 | sought H1875; seek H1875 | current | chapter 10.14 Humility, The humble (1 earlier telling(s) in the workbook) |
| C-188 | What God looks to is set against a religious act in the humility passages (the fast, the walk, the house, the broken heart), as in the other passages gathered in 13.1; the offering follows the broken heart | Isaiah 58:3-7 | seek H4672 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 11 Other sides of the inner being, What changes the character; chapter 13.1 Divine, Delight; chapter 10.14 Humility, Humility as a way of walking (6 earlier telling(s) in the workbook) |
| C-197 | In the New Testament humility rests on what is said of Jesus; the saying he taught, that whoever humbles himself will be exalted, is what is told of him | Matthew 11:29 | find G2147 | current | chapter 10.14 Humility, Jesus (2 earlier telling(s) in the workbook) |
| C-202 | The lowering that the Old Testament tells of God is done in the Son in a human life | Matthew 11:29 | find G2147 | current | chapter 10.14 Humility, The Old Testament and the New; chapter 13.1 Divine, Lowering himself (3 earlier telling(s) in the workbook) |
| C-220 | Pride shuts God out of the thoughts, is set against faith, and gives no rest | Psalm 10:4 | seek H1875 | current | chapter 10.15 Pride, The heart that says what God says (1 earlier telling(s) in the workbook) |
| C-222 | Pride is set against hearing: it will not take rebuke or advice, and the scoffer is known by what he will not receive | Proverbs 14:6 | seeks H1245 | current | chapter 10.2 Knowing and hearing, (opening); chapter 10.15 Pride, Pride and hearing; chapter 10.2 Knowing and hearing, Pride and hearing (3 earlier telling(s) in the workbook) |
| C-232 | A boast can be in another person, and it puts the one who boasts at stake on the other's conduct | 2 Corinthians 9:2-4 | find G2147 | current | chapter 10.15 Pride, The boast; chapter 10.10 Relating to others, Pride over another (2 earlier telling(s) in the workbook) |
| C-238 | The same words are not pride when the height is given or faces God: a heart lifted up in God's ways, strength of soul given, a heart not lifted up and at rest | 2 Chronicles 17:4-6 | sought H1875 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 10.15 Pride, The other face (2 earlier telling(s) in the workbook) |
| C-245 | Dread on a people is not always said to come from God: in Esther it falls with no giver named, and brings many of the peoples over to the name of those they fear | Est 9:2 | sought H1245 | current | chapter 10.10 Relating to others, Fear that arrives with a person; chapter 10.12 Fear, Dread laid on others (3 earlier telling(s) in the workbook) |
| C-247 | Ezra's heart set to study the Law, to do it and to teach it is given straight after the good hand of God on him, as its ground in him | 2Ch 12:14 | seek H1875 | current | chapter 10.7 Choosing and setting direction, Setting the heart; chapter 13.1 Divine, Delight (2 earlier telling(s) in the workbook) |
| C-248 | Knowing that God's hand is on him is the named ground of Ezra's courage, and the courage turns at once into a deed | Ezr 8:22 | seek H1245 | current | chapter 10.12 Fear, What changes it (1 earlier telling(s) in the workbook) |
| C-252 | Those on whom God's good hand rests name it as the reason for what came about, and it is said to be for good on all who seek him | Ezr 8:22 | seek H1245 | current | chapter 13.1 Divine, Delight (1 earlier telling(s) in the workbook) |
| C-269 | The one who calls himself poor is the one who cries and is heard, and what he is delivered from includes his fears | Psa 34:4 | sought H1875 | current | chapter 10.9 Relating to God, Waiting, and pleading (1 earlier telling(s) in the workbook) |
| C-271 | Paul speaks of believers as already raised with Christ, while their mortal bodies are still to be given life | Col 3:1 | seek G2212 | current | chapter 02 Life, breath and death, The body raised (1 earlier telling(s) in the workbook) |
| C-278 | The coming resurrection is given as a reason for how a person lives now: giving without return, enduring, self-control, steadfast work | Rom 2:7 | seek for G2212 | current | chapter 02 Life, breath and death, Waited for (1 earlier telling(s) in the workbook) |
| C-293 | In 2 Kings 3:27 the wrath has no bearer named and no breach before it, and the verse leaves open whose wrath it was | 2Ch 32:26 | come upon H0935G | current | chapter 10.13 Anger, How it is spoken of (1 earlier telling(s) in the workbook) |
| C-307 | Anger can rise at contempt for a request that rested on good done | 1Sa 25:8 | find H4672 | current | chapter 10.13 Anger, What it rises at (1 earlier telling(s) in the workbook) |
| C-315 | The king's remembering of Vashti was turned aside by a pleasure offered, and the young women's own wishes were not asked | Est 2:2 | sought out H1245 | current | chapter 10.3 Remembering and forgetting, Forgetting lets anger go, and remembering brings it back (1 earlier telling(s) in the workbook) |
| C-363 | Thoughts and plans are wholly open to God, the inclination is known before it acts, and the purposes of the heart will be disclosed. | 1Ch 28:9 | searches H1875; seek H1875 | current | chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 04 The heart, The heart is hidden, and God sees it; chapter 10.7 Choosing and setting direction, Planning |
| C-364 | A purpose can be set ahead and held, for one's own speech and faithfulness; it can be kept and directed by God, and the mind's setting decides its direction. | Psa 17:3 | find H4672 | current | chapter 10.7 Choosing and setting direction, Planning |
| C-380 | The Spirit intercedes according to God's will, the purpose is turned toward those who love him, and a person can reject it for himself. | Rom 8:27 | searches G2045 | current | chapter 13.1 Divine, Purposing |

### 5.3 The narrative sections that tell these claims (51)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 6 | 02 Life, breath and death | Breath lent, and held by God | C-114 |
| 8 | 02 Life, breath and death | Life set before a person | C-118, C-120 |
| 9 | 02 Life, breath and death | Living before God | C-125, C-131, C-132 |
| 12 | 02 Life, breath and death | Death and sin | C-87 |
| 18 | 02 Life, breath and death | Soul, spirit and heart at death | 2-15 |
| 23 | 02 Life, breath and death | The body raised | C-271 |
| 27 | 02 Life, breath and death | Waited for | C-278 |
| 29 | 02 Life, breath and death | After death | C-106 |
| 45 | 04 The heart | The heart and anger | C-171 |
| 50 | 04 The heart | The heart is hidden, and God sees it | C-363 |
| 122 | 10.2 Knowing and hearing | (opening) | C-222 |
| 128 | 10.3 Remembering and forgetting | Forgetting lets anger go, and remembering brings it back | C-315 |
| 144 | 10.4 Thinking | Small, passing, and wholly seen | C-363 |
| 189 | 10.7 Choosing and setting direction | Others around a choice | C-176, C-331 |
| 194 | 10.7 Choosing and setting direction | Setting the heart | C-247 |
| 196 | 10.7 Choosing and setting direction | Planning | C-363, C-364 |
| 197 | 10.7 Choosing and setting direction | Willing | C-171 |
| 212 | 10.9 Relating to God | Waiting, and pleading | C-269 |
| 224 | 10.10 Relating to others | Fear that arrives with a person | C-245 |
| 252 | 10.12 Fear | Dread laid on others | C-245 |
| 254 | 10.12 Fear | What changes it | C-248 |
| 259 | 10.13 Anger | What it rises at | C-307 |
| 270 | 10.13 Anger | How it is spoken of | C-293 |
| 282 | 10.13 Anger | The heart that turns, and the heart that does not | C-171, C-175 |
| 284 | 10.13 Anger | Shelter, and who can stand | C-183 |
| 296 | 11 Other sides of the inner being | 4. One word, opposite values | C-188, C-238 |
| 297 | 11 Other sides of the inner being | What changes the character | C-188 |
| 307 | 12 When the inner being goes wrong | Pride and the lifted-up heart and spirit | C-168, C-171 |
| 313 | 12 When the inner being goes wrong | Idols taken inside | C-387 |
| 323 | 13.1 Divine | Choosing | C-176, C-331 |
| 324 | 13.1 Divine | Purposing | C-380 |
| 326 | 13.1 Divine | Delight | C-188, C-247, C-252 |
| 349 | 02 Life, breath and death | Death spoken of in more than one way | C-140 |
| 352 | 10.14 Humility | (opening) | C-167, C-168 |
| 357 | 10.14 Humility | Where it happens | C-171 |
| 361 | 10.14 Humility | God sees it, and answers in measure | C-175 |
| 362 | 10.14 Humility | A humbling God does not take knowledge of | C-176 |
| 365 | 10.14 Humility | The humble | C-183, C-184 |
| 366 | 10.14 Humility | Humility as a way of walking | C-188 |
| 370 | 10.14 Humility | Jesus | C-197 |
| 371 | 10.14 Humility | The Old Testament and the New | C-202 |
| 376 | 10.9 Relating to God | Humbling oneself before God | C-175 |
| 378 | 04 The heart | The heart humbled | C-171 |
| 380 | 13.1 Divine | Lowering himself | C-202 |
| 384 | 10.15 Pride | The heart that says what God says | C-220 |
| 385 | 10.15 Pride | Pride and hearing | C-222 |
| 387 | 10.15 Pride | The boast | C-232 |
| 390 | 10.15 Pride | The other face | C-238 |
| 392 | 10.2 Knowing and hearing | Pride and hearing | C-222 |
| 394 | 10.10 Relating to others | Pride over another | C-232 |
| 406 | 10.7 Choosing and setting direction | Dedicating | C-387 |

## 6. Phrases attached to the collection (21)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| come upon | 6695 | strong route: strong H4672 via find; strong H4672 via finds; strong H4672 via seek; strong H4672 via seeking | 11 | 11 | 12 | 4 |
| earnestly seeks | 6876 | english route: word seeks | 1 | 1 | 16 | 16 |
| find compassion | 7009 | english route: word find | 1 | 1 | 2 | 2 |
| insist on | 7376 | strong route: strong G2212 via search; strong G2212 via searched; strong G2212 via searching; strong G2212 via seek; strong G2212 via seeking; strong G2212 via seeks; strong G2212 via sought | 1 | 1 | 4 | 4 |
| look for | 6049 | strong route: strong G0327 via search; strong G2212 via search; strong G2212 via searched; strong G2212 via searching; strong G2212 via seek; strong G2212 via seeking; strong G2212 via seeks; strong G2212 via sought | 5 | 5 | 6 | 3 |
| looking for | 6059 | strong route: strong G2212 via search; strong G2212 via searched; strong G2212 via searching; strong G2212 via seek; strong G2212 via seeking; strong G2212 via seeks; strong G2212 via sought | 3 | 3 | 10 | 8 |
| more handsome | 7758 | strong route: strong H2896A via searches | 1 | 1 | 1 | 1 |
| search for | 8109 | english route: word search | 1 | 1 | 5 | 5 |
| searched for | 8110 | english route: word searched | 1 | 1 | 4 | 4 |
| searching for | 8111 | english route: word searching | 1 | 1 | 4 | 4 |
| seek after | 8122 | english route: word seek | 1 | 1 | 4 | 4 |
| seek for | 8123 | english route: word seek | 1 | 1 | 4 | 4 |
| seek me diligently | 8124 | english route: word seek | 2 | 2 | 27 | 26 |
| seek out | 6102 | english route: word seek | 3 | 3 | 10 | 9 |
| seek shelter | 8125 | english route: word seek | 1 | 1 | 1 | 1 |
| seeks for | 6103 | english route: word seeks | 3 | 3 | 31 | 28 |
| seeks out | 8127 | english route: word seeks | 2 | 2 | 5 | 5 |
| sought for | 8248 | english route: word sought | 1 | 1 | 4 | 4 |
| sought out | 6191 | english route: word sought | 3 | 3 | 12 | 12 |
| sought refuge | 8249 | english route: word sought | 1 | 1 | 2 | 2 |
| well disposed | 8618 | strong route: strong H2896A via searches | 1 | 1 | 1 | 1 |

## 7. Stored-data faults

Blatant errors and omissions in the stored rows, each found by the rule stated. A fault is shown with the rows that identify it; the first 25 of a long list are shown and every row is in the workbook sheet `Faults`.

| rule | what it looks for | found |
|---|---|---|
| link-to-missing-or-deleted-term | live collection_link of this collection whose term_id has no live surface_term row | 0 |
| collection-merge-inconsistent | collection.status and collection.merged_into_id disagree, or the target is not live | 0 |
| member-surface-with-no-occurrence | member term of origin 'surface' that no live verse_lexical row carries | 0 |
| occurrence-in-deleted-verse | occurrence whose verse row is soft deleted | 0 |
| live-node-on-deleted-observation | ib_node with deleted=0 whose observation is deleted or missing (the node still names a verse and word the observation no longer covers) | 1221 |
| claim-source-on-deleted-observation | narrative_claim_source naming an observation that is deleted or missing | 0 |
| claim-in-narrative-with-no-current-telling | narrative_claim.in_narrative=1 and no current narrative_claim_telling | 0 |
| live-node-with-no-verse-lexical-id | live ib_node in a verse of the report with a member surface but verse_lexical_id NULL (stored, tied to no occurrence) | 114 |

### live-node-on-deleted-observation: 1221 found

| observation stage | tag | status | nodes |
|---|---|---|---|
| verse-reading | answered-no-flag | withdrawn | 875 |
| verse-reading | not-related-to-meaningful-word | withdrawn | 296 |
| verse-reading | attested-pre-nt | withdrawn | 44 |
| verse-reading | could-not-resolve | withdrawn | 4 |
| Analysis_phase_1 | statement | withdrawn | 1 |
| verse-reading | qualifier-for-term | withdrawn | 1 |

| node | observation | observation stage | observation tag | observation status | verse | word | Strong's code |
|---|---|---|---|---|---|---|---|
| 5981 | 4789 | verse-reading | answered-no-flag | withdrawn | Gen 37:15 | seeking | H1245 |
| 5982 | 4790 | verse-reading | answered-no-flag | withdrawn | Gen 37:15 | seeking | H1245 |
| 5985 | 4793 | verse-reading | answered-no-flag | withdrawn | Gen 37:15 | seeking | H1245 |
| 5987 | 4795 | verse-reading | not-related-to-meaningful-word | withdrawn | Gen 37:15 | seeking | H1245 |
| 5990 | 4798 | verse-reading | not-related-to-meaningful-word | withdrawn | Gen 37:15 | seeking | H1245 |
| 5992 | 4800 | verse-reading | not-related-to-meaningful-word | withdrawn | Gen 37:15 | seeking | H1245 |
| 69465 | 20635 | Analysis_phase_1 | statement | withdrawn | Gen 37:15 | seeking | H1245 |
| 5615 | 4430 | verse-reading | answered-no-flag | withdrawn | Gen 37:16 | seeking | H1245 |
| 5619 | 4434 | verse-reading | answered-no-flag | withdrawn | Gen 37:16 | seeking | H1245 |
| 5623 | 4438 | verse-reading | answered-no-flag | withdrawn | Gen 37:16 | seeking | H1245 |
| 6590 | 5450 | verse-reading | answered-no-flag | withdrawn | Gen 43:30 | sought | H1245 |
| 6655 | 5512 | verse-reading | answered-no-flag | withdrawn | Exo 2:15 | sought | H1245 |
| 6661 | 5518 | verse-reading | not-related-to-meaningful-word | withdrawn | Exo 2:15 | sought | H1245 |
| 5983 | 4791 | verse-reading | answered-no-flag | withdrawn | Exo 4:19 | seeking | H1245 |
| 5986 | 4794 | verse-reading | answered-no-flag | withdrawn | Exo 4:19 | seeking | H1245 |
| 5989 | 4797 | verse-reading | not-related-to-meaningful-word | withdrawn | Exo 4:19 | seeking | H1245 |
| 5991 | 4799 | verse-reading | answered-no-flag | withdrawn | Exo 4:19 | seeking | H1245 |
| 6591 | 5451 | verse-reading | answered-no-flag | withdrawn | Exo 4:24 | sought | H1245 |
| 6361 | 5219 | verse-reading | answered-no-flag | withdrawn | Exo 33:7 | sought | H1245 |
| 6370 | 5223 | verse-reading | answered-no-flag | withdrawn | Exo 33:7 | sought | H1245 |
| 6376 | 5227 | verse-reading | not-related-to-meaningful-word | withdrawn | Exo 33:7 | sought | H1245 |
| 6916 | 5762 | verse-reading | answered-no-flag | withdrawn | Lev 19:31 | seek | H1245 |
| 6919 | 5765 | verse-reading | answered-no-flag | withdrawn | Lev 19:31 | seek | H1245 |
| 6921 | 5767 | verse-reading | not-related-to-meaningful-word | withdrawn | Lev 19:31 | seek | H1245 |
| 6925 | 5771 | verse-reading | answered-no-flag | withdrawn | Lev 19:31 | seek | H1245 |

_1196 more in the workbook sheet `Faults`_

### live-node-with-no-verse-lexical-id: 114 found

| node | observation | verse | word |
|---|---|---|---|
| 4423 | 3367 | Zep 2:3 | seek |
| 4426 | 3370 | Zep 2:3 | seek |
| 4427 | 3371 | Zep 2:3 | seek |
| 4431 | 3375 | Zep 2:3 | seek |
| 4432 | 3376 | Zep 2:3 | seek |
| 4434 | 3378 | Zep 2:3 | seek |
| 4439 | 3383 | Zep 2:3 | seek |
| 4601 | 3528 | Jer 45:5 | seek |
| 4606 | 3533 | Jer 45:5 | seek |
| 4614 | 3538 | Jer 45:5 | seek |
| 4615 | 3538 | Jer 45:5 | seek |
| 4621 | 3544 | Jer 45:5 | seek |
| 4819 | 3735 | 1Sa 22:23 | seeks |
| 4822 | 3736 | 1Sa 22:23 | seeks |
| 4824 | 3737 | 1Sa 22:23 | seeks |
| 4826 | 3738 | 1Sa 22:23 | seeks |
| 4830 | 3740 | 1Sa 22:23 | seeks |
| 4839 | 3747 | 1Sa 22:23 | seeks |
| 4842 | 3749 | 1Sa 22:23 | seeks |
| 4845 | 3751 | 1Sa 22:23 | seeks |
| 4848 | 3754 | 1Sa 22:23 | seeks |
| 5491 | 4310 | 1Cor 7:27 | seek |
| 5501 | 4320 | 1Cor 7:27 | seek |
| 5503 | 4322 | 1Cor 7:27 | seek |
| 5506 | 4325 | 1Cor 7:27 | seek |

_89 more in the workbook sheet `Faults`_

## 8. Sources

Occurrences: live verse_lexical rows, with the verse text from table `verse`; Strong's data from `strong`, `strong_sense`, `strong_meaning_tree`, `strong_related`, `cluster_strong`; observations and nodes from `ib_observation` and `ib_node` (an observation is withdrawn when deleted = 1); claims from `narrative_claim_source` (by observation_id or verse_id), `narrative_claim`, `narrative_claim_telling` and `narrative_section`. A table or column was used only after its recorded meaning in `cfg_table` and `cfg_column` was read (rule B:123).

