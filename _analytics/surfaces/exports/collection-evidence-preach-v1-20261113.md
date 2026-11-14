# Collection evidence report: preach

Generated 2026-11-13T19:01:48Z by run RUN-20261113_190144_045-COLLECTIONBUILD (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `collection-evidence-preach-v1-20261113.xlsx`. Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.

## 1. What this report holds and how to read it

A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through the observations and the claims into the narrative. Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; 6 lists the phrases; 7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading (every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is named where it is cited.

## 2. The collection preach at a glance

Status confirmed; core term 2031; created 2026-11-10T03:12:44Z, updated 2026-11-10T16:06:18Z; run RUN-20261110_160617_500-COLLECTIONBUILD. All the collection's fields are in the workbook sheet `Collection`, all its links in `Links`.

### 2.1 The member words (23)

A member is a term reached by a live link of the member tiers (core, synonym, opposite, gathered, phrase), the term itself and the terms whose base it is.

| word | form | tiers | base | collection_state | occurrences | verses |
|---|---|---|---|---|---|---|
| announce | word | gathered | announce | placed | 3 | 3 |
| declare | word | synonym | declare | placed | 84 | 79 |
| declared | word | synonym | declare | placed | 61 | 48 |
| declares | word | synonym | declare | placed | 442 | 363 |
| declaring | word | synonym | declare | placed | 4 | 4 |
| exhorted | word | synonym | exhort | placed | 2 | 2 |
| exhorting | word | synonym | exhort | placed | 1 | 1 |
| exhorts | word | synonym | exhort | placed | 1 | 1 |
| good news | phrase | phrase | good news | placed | 21 | 18 |
| preach | word | core | preach | placed | 24 | 21 |
| preach the gospel | phrase | phrase | preach the gospel | placed | 8 | 7 |
| preached | word | synonym | preach | placed | 14 | 14 |
| preached the gospel | phrase | phrase | preached the gospel | placed | 3 | 3 |
| preaching | word | synonym | preach | placed | 18 | 18 |
| preaching the gospel | phrase | phrase | preaching the gospel | placed | 3 | 3 |
| proclaim | word | synonym | proclaim | placed | 68 | 61 |
| proclaimed | word | synonym | proclaim | placed | 53 | 49 |
| proclaiming | word | synonym | proclaim | placed | 19 | 18 |
| proclaims | word | synonym | proclaim | placed | 6 | 6 |
| prophesied | word | synonym | prophesy | placed | 46 | 38 |
| prophesy | word | synonym | prophesy | placed | 72 | 64 |
| prophesying | word | synonym | prophesy | placed | 23 | 20 |
| set forth | phrase | phrase | set forth | placed | 3 | 3 |

### 2.2 The Strong's codes behind the members (75)

Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.

| code | own occurrences | shared occurrences | verses | member words (own) | engagement verdicts | occurrences with other observations |
|---|---|---|---|---|---|---|
| H5002 נְאֻם ne.um "utterance" | 296 | 65 | 347 | declares 296 | none | 17 |
| H5012 נָבָא na.va "to prophesy" | 101 | 4 | 93 | prophesy 51, prophesied 30, prophesying 20 | none | 14 |
| H5046 נָגַד na.gad "to tell" | 63 | 4 | 64 | declare 36, declared 11, declares 7, proclaim 5, announce 2, declaring 1, proclaims 1 | none | 10 |
| G2784 κηρύσσω kērussō "to preach" | 58 | 0 | 57 | proclaimed 18, preach 12, proclaim 10, proclaiming 10, preaching 4, preached 2, proclaims 2 | none | 0 |
| G2097 εὐαγγελίζομαι euangelizomai "to speak good news" | 47 | 0 | 45 | preached 12, good news 11, preach the gospel 8, preaching 7, preached the gospel 3, preaching the gospel 3, preach 2, proclaim 1 | none | 5 |
| H7121I קָרָא qa.ra "to call: call out" | 30 | 7 | 36 | proclaim 16, proclaimed 9, proclaiming 3, proclaims 2 | none | 4 |
| G4395 προφητεύω profēteuō "to prophesy" | 23 | 0 | 23 | prophesy 16, prophesied 6, prophesying 1 | none | 4 |
| H8085I שָׁמַע sha.ma "to hear: proclaim" | 20 | 0 | 18 | proclaim 9, proclaimed 6, declare 2, announce 1, proclaiming 1, proclaims 1 | none | 3 |
| G2605 καταγγέλλω katangellō "to proclaim" | 16 | 0 | 16 | proclaim 8, proclaimed 6, proclaiming 2 | none | 0 |
| H5608A סָפַר sa.phar "to recount" | 14 | 0 | 14 | declare 11, declared 2, set forth 1 | none | 0 |
| H1696I דָבַר da.var "to speak: promise" | 10 | 2 | 12 | declare 5, declared 5 | none | 4 |
| H0559 אָמַר a.mar "to say" | 9 | 4 | 13 | declares 4, declare 2, declared 2, proclaimed 1 | none | 0 |
| G0312 ἀναγγέλλω anangellō "to report" | 8 | 0 | 8 | declare 3, declared 2, declaring 2, proclaim 1 | none | 0 |
| G2980 λαλέω laleō "to speak" | 8 | 0 | 8 | declare 4, declared 3, preaching 1 | none | 0 |
| G3004G λέγω legō "to say: says" | 8 | 2 | 10 | declares 5, declare 2, preach 1 | none | 0 |
| H1319 בָּשַׂר ba.sar "to bear tidings" | 8 | 1 | 7 | good news 8 | none | 3 |
| H5197 נָטַף na.taph "to drip/prophesy" | 7 | 0 | 5 | preach 7 | none | 0 |
| G0518 ἀπαγγέλλω apangellō "to announce" | 6 | 0 | 6 | proclaim 3, declared 2, declare 1 | none | 0 |
| G2782 κήρυγμα kērugma "preaching" | 6 | 0 | 6 | preaching 5, preach 1 | none | 0 |
| G3870 παρακαλέω parakaleō "to plead/comfort" | 4 | 0 | 4 | exhorted 2, exhorting 1, exhorts 1 | none | 1 |
| H2331 חָוָה cha.vah "to explain" | 3 | 0 | 3 | declare 3 | none | 0 |
| H3045 יָדַע ya.da "to know" | 3 | 0 | 3 | declared 2, declare 1 | none | 0 |
| G1229 διαγγέλλω diangellō "to proclaim" | 2 | 0 | 2 | proclaim 1, proclaimed 1 | none | 0 |
| G1334 διηγέομαι diēgeomai "to relate fully" | 2 | 0 | 2 | declare 1, declared 1 | none | 0 |
| H0560 אֲמַר a.mar "to say" | 2 | 7 | 9 | declared 2 | none | 0 |
| H2372 חָזָה cha.zah "to see" | 2 | 0 | 1 | prophesy 2 | none | 0 |
| H5030 נָבִיא na.vi "prophet" | 2 | 0 | 2 | prophesy 2 | none | 2 |
| H7123 קְרָא qe.ra "to read" | 2 | 0 | 2 | proclaimed 2 | none | 0 |
| G0584 ἀποδείκνυμι apodeiknumi "to display" | 1 | 0 | 1 | proclaiming 1 | none | 0 |
| G0611 ἀποκρίνω apokrinō "to answer" | 1 | 1 | 2 | declared 1 | none | 0 |
| G1107 γνωρίζω gnōrizō "to make known" | 1 | 0 | 1 | proclaim 1 | none | 0 |
| G1344 δικαιόω dikaioō "to justify" | 1 | 0 | 1 | declared 1 | none | 1 |
| G1804 ἐξαγγέλλω exangellō "to proclaim" | 1 | 0 | 1 | proclaim 1 | none | 0 |
| G1957 ἐπιμαρτυρέω epimartureō "to testify to" | 1 | 0 | 1 | declaring 1 | none | 0 |
| G2036 εἶπον eipon "to say: said" | 1 | 0 | 1 | declared 1 | none | 0 |
| G3056 λόγος logos "word" | 1 | 0 | 1 | preaching 1 | none | 0 |
| G3670 ὁμολογέω homologeō "to confess/profess" | 1 | 0 | 1 | declare 1 | none | 0 |
| G3724 ὁρίζω horizō "to determine" | 1 | 0 | 1 | declared 1 | none | 0 |
| G4293 προκαταγγέλλω prokatangellō "to foretell" | 1 | 0 | 1 | proclaimed 1 | none | 0 |
| G4296 προκηρύσσω prokērussō "to announce" | 1 | 0 | 1 | proclaimed 1 | none | 0 |
| G4388 προτίθημι protithēmi "to plan/present" | 1 | 0 | 1 | set forth 1 | none | 1 |
| G4394 προφητεία profēteia "prophecy" | 1 | 0 | 1 | prophesying 1 | none | 1 |
| H2142 זָכַר za.khar "to remember" | 1 | 0 | 1 | proclaim 1 | none | 0 |
| H4448A מָלַל ma.lal "to speak" | 1 | 0 | 1 | declare 1 | none | 0 |
| H5001 נָאַם na.am "to prophesy" | 1 | 0 | 1 | declare 1 | none | 0 |
| H5013 נְבָא ne.va "to prophesy" | 1 | 0 | 1 | prophesied 1 | none | 0 |
| H5017 נְבוּאָה ne.vu.ah "prophesying" | 1 | 0 | 1 | prophesying 1 | none | 0 |
| H5674A עָבַר a.var "to pass" | 1 | 1 | 2 | proclaim 1 | none | 0 |
| H5921A עַל al "upon" | 1 | 2 | 3 | declare 1 | none | 0 |
| H6032 עֲנָה a.nah "to answer" | 1 | 7 | 8 | declared 1 | none | 0 |
| H6942J קָדַשׁ qa.dash "to consecrate: prepare" | 1 | 0 | 1 | declare 1 | none | 0 |
| H7126G קָרַב qa.rav "to present: come" | 1 | 0 | 1 | set forth 1 | none | 0 |
| H7561 רָשַׁע ra.sha "be wicked" | 1 | 0 | 1 | declared 1 | none | 1 |
| G2532 καί kai "and" | 0 | 1 | 1 |  | none | 0 |
| G2896 κράζω krazō "to cry" | 0 | 1 | 1 |  | none | 0 |
| H0310A אַחַר a.char "after" | 0 | 1 | 1 |  | none | 0 |
| H0413 אֶל el "to[wards]" | 0 | 9 | 9 |  | none | 0 |
| H0589 אֲנִי a.ni "I" | 0 | 6 | 6 |  | none | 0 |
| H0834A אֲשֶׁר a.sher "which" | 0 | 5 | 5 |  | none | 0 |
| H0853 אֵת et "[Obj.]" | 0 | 15 | 15 |  | none | 0 |
| H0854 אֵת et "with" | 0 | 2 | 2 |  | none | 0 |
| H1931 הוּא hu "he/she/it" | 0 | 18 | 18 |  | none | 0 |
| H1961 הָיָה ha.yah "to be" | 0 | 7 | 7 |  | none | 0 |
| H1992 הֵ֫מָּה hem.mah "they [masc.]" | 0 | 3 | 3 |  | none | 0 |
| H2088 זֶה zeh "this" | 0 | 2 | 2 |  | none | 0 |
| H2930A טָמֵא ta.me "to defile" | 0 | 1 | 1 |  | none | 0 |
| H3068G יְהֹוָה ye.ho.vah "LORD" | 0 | 1 | 1 |  | none | 0 |
| H3588A כִּי ki "for" | 0 | 1 | 1 |  | none | 0 |
| H3651C כֵּן ken "so" | 0 | 2 | 2 |  | none | 0 |
| H3808 לֹא lo "not" | 0 | 2 | 2 |  | none | 0 |
| H5704 עַד ad "till" | 0 | 5 | 5 |  | none | 0 |
| H6030B עָנָה a.nah "to answer" | 0 | 1 | 1 |  | none | 0 |
| H6963J קוֹל qol "voice: message" | 0 | 1 | 1 |  | none | 0 |
| H8033G שָׁם sham "there" | 0 | 2 | 2 |  | none | 0 |
| H8141 שָׁנָה sha.nah "year" | 0 | 1 | 1 |  | none | 0 |

## 3. Each Strong's code behind the collection

Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. The occurrences where the member surface is only shared with another code's unit are in section 3.54.

### 3.1 H5002 נְאֻם ne.um "utterance": 296 own occurrences in 286 verses

- **Meaning as stored:** Hebrew; native word נְאֻם, transliteration ne.um; STEP gloss "utterance"; sense head "utterance" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5002):** (Qal) utterance, declaration (of prophet).
- **Related terms (1):** H5001 na.am "to prophesy".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (high).
- **Counts, three measures as stored:** STEP token count 376; verses STEP attests 358; verse_lexical rows the parse found 376.

- **Carried by the member words:** declares (296).
- **Engagement of these occurrences:** none recorded 296.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Gen 22:16 | declares | HNcmsc | none recorded | - | 0 | and said, “ By myself I have sworn, **declares** the Lord, because you have done this and have not withheld your son, your only son, |
| 1Sa 2:30 | declares | HNcmsc | none recorded | - | 0 | Therefore the Lord, the God of Israel, **declares**: ‘I promised that your house and the house of your father should go in and out before me forever,’ but now the Lord declares: ‘Far be it from me, for those who honor me I will honor, and those who despise me shall be lightly esteemed. |
| 1Sa 2:30 | declares | HNcmsc | none recorded | - | 0 | Therefore the Lord, the God of Israel, **declares**: ‘I promised that your house and the house of your father should go in and out before me forever,’ but now the Lord declares: ‘Far be it from me, for those who honor me I will honor, and those who despise me shall be lightly esteemed. |
| 2Ki 19:33 | declares | HNcmsc | none recorded | - | 0 | By the way that he came, by the same he shall return, and he shall not come into this city, **declares** the Lord. |
| 2Ki 22:19 | declares | HNcmsc | none recorded | - | 0 | because your heart was penitent, and you humbled yourself before the Lord, when you heard how I spoke against this place and against its inhabitants, that they should become a desolation and a curse, and you have torn your clothes and wept before me, I also have heard you, **declares** the Lord. |
| 2Ch 34:27 | declares | HNcmsc | none recorded | - | 0 | because your heart was tender and you humbled yourself before God when you heard his words against this place and its inhabitants, and you have humbled yourself before me and have torn your clothes and wept before me, I also have heard you, **declares** the Lord. |
| Pro 30:1 | declares | HNcmsc | none recorded | - | 0 | The words of Agur son of Jakeh. The oracle. The man **declares**, I am weary, O God; I am weary, O God, and worn out. |
| Isa 1:24 | declares | HNcmsc | none recorded | - | 0 | Therefore the Lord **declares**, the Lord of hosts, the Mighty One of Israel: “ Ah, I will get relief from my enemies and avenge myself on my foes. |
| Isa 3:15 | declares | HNcmsc | none recorded | - | 0 | What do you mean by crushing my people, by grinding the face of the poor?” **declares** the Lord God of hosts. |
| Isa 14:22 | declares | HNcmsc | none recorded | - | 0 | “I will rise up against them,” **declares** the Lord of hosts, “and will cut off from Babylon name and remnant, descendants and posterity,” declares the Lord. |
| Isa 14:22 | declares | HNcmsc | none recorded | - | 0 | “I will rise up against them,” **declares** the Lord of hosts, “and will cut off from Babylon name and remnant, descendants and posterity,” declares the Lord. |
| Isa 14:23 | declares | HNcmsc | none recorded | - | 0 | “And I will make it a possession of the hedgehog, and pools of water, and I will sweep it with the broom of destruction,” **declares** the Lord of hosts. |
| Isa 17:6 | declares | HNcmsc | none recorded | - | 0 | Gleanings will be left in it, as when an olive tree is beaten — two or three berries in the top of the highest bough, four or five on the branches of a fruit tree, **declares** the Lord God of Israel. |
| Isa 19:4 | declares | HNcmsc | none recorded | - | 0 | and I will give over the Egyptians into the hand of a hard master, and a fierce king will rule over them, **declares** the Lord God of hosts. |
| Isa 30:1 | declares | HNcmsc | none recorded | 20135 | 0 | “ Ah, stubborn children,” **declares** the Lord, “who carry out a plan, but not mine, and who make an alliance, but not of my Spirit, that they may add sin to sin; |
| Isa 31:9 | declares | HNcmsc | none recorded | - | 0 | His rock shall pass away in terror, and his officers desert the standard in panic,” **declares** the Lord, whose fire is in Zion, and whose furnace is in Jerusalem. |
| Isa 37:34 | declares | HNcmsc | none recorded | - | 0 | By the way that he came, by the same he shall return, and he shall not come into this city, **declares** the Lord. |
| Isa 41:14 | declares | HNcmsc | none recorded | - | 0 | Fear not, you worm Jacob, you men of Israel! I am the one who helps you, **declares** the Lord; your Redeemer is the Holy One of Israel. |
| Isa 43:10 | declares | HNcmsc | none recorded | - | 0 | “ You are my witnesses,” **declares** the Lord, “and my servant whom I have chosen, that you may know and believe me and understand that I am he. Before me no god was formed, nor shall there be any after me. |
| Isa 43:12 | declares | HNcmsc | none recorded | - | 0 | I declared and saved and proclaimed, when there was no strange god among you; and you are my witnesses,” **declares** the Lord, “and I am God. |
| Isa 49:18 | declares | HNcmsc | none recorded | - | 0 | Lift up your eyes around and see; they all gather, they come to you. As I live, **declares** the Lord, you shall put them all on as an ornament; you shall bind them on as a bride does. |
| Isa 52:5 | declares | HNcmsc | none recorded | - | 0 | Now therefore what have I here,” **declares** the Lord, “seeing that my people are taken away for nothing? Their rulers wail,” declares the Lord, “and continually all the day my name is despised. |
| Isa 52:5 | declares | HNcmsc | none recorded | - | 0 | Now therefore what have I here,” **declares** the Lord, “seeing that my people are taken away for nothing? Their rulers wail,” declares the Lord, “and continually all the day my name is despised. |
| Isa 55:8 | declares | HNcmsc | none recorded | - | 0 | For my thoughts are not your thoughts, neither are your ways my ways, **declares** the Lord. |
| Isa 56:8 | declares | HNcmsc | none recorded | - | 0 | The Lord God, who gathers the outcasts of Israel, **declares**, “I will gather yet others to him besides those already gathered.” |
| Isa 59:20 | declares | HNcmsc | none recorded | - | 0 | “And a Redeemer will come to Zion, to those in Jacob who turn from transgression,” **declares** the Lord. |
| Isa 66:2 | declares | HNcmsc | none recorded | - | 0 | All these things my hand has made, and so all these things came to be, **declares** the Lord. But this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word. |
| Isa 66:17 | declares | HNcmsc | none recorded | - | 0 | “Those who sanctify and purify themselves to go into the gardens, following one in the midst, eating pig’s flesh and the abomination and mice, shall come to an end together, **declares** the Lord. |
| Jer 1:8 | declares | HNcmsc | none recorded | - | 0 | Do not be afraid of them, for I am with you to deliver you, **declares** the Lord.” |
| Jer 1:15 | declares | HNcmsc | none recorded | - | 0 | For behold, I am calling all the tribes of the kingdoms of the north, **declares** the Lord, and they shall come, and every one shall set his throne at the entrance of the gates of Jerusalem, against all its walls all around and against all the cities of Judah. |
| Jer 1:19 | declares | HNcmsc | none recorded | - | 0 | They will fight against you, but they shall not prevail against you, for I am with you, **declares** the Lord, to deliver you.” |
| Jer 2:12 | declares | HNcmsc | none recorded | - | 0 | Be appalled, O heavens, at this; be shocked, be utterly desolate, **declares** the Lord, |
| Jer 2:22 | declares | HNcmsc | none recorded | - | 0 | Though you wash yourself with lye and use much soap, the stain of your guilt is still before me, **declares** the Lord God. |
| Jer 2:29 | declares | HNcmsc | none recorded | - | 0 | “ Why do you contend with me? You have all transgressed against me, **declares** the Lord. |
| Jer 3:10 | declares | HNcmsc | none recorded | - | 0 | Yet for all this her treacherous sister Judah did not return to me with her whole heart, but in pretense, **declares** the Lord.” |
| Jer 3:12 | declares | HNcmsc | none recorded | 14699 | 0 | Go, and proclaim these words toward the north, and say, “‘ Return, faithless Israel, **declares** the Lord. I will not look on you in anger, for I am merciful, declares the Lord; I will not be angry forever. |
| Jer 3:13 | declares | HNcmsc | none recorded | 14699 | 0 | Only acknowledge your guilt, that you rebelled against the Lord your God and scattered your favors among foreigners under every green tree, and that you have not obeyed my voice, **declares** the Lord. |
| Jer 3:14 | declares | HNcmsc | none recorded | - | 0 | Return, O faithless children, **declares** the Lord; for I am your master; I will take you, one from a city and two from a family, and I will bring you to Zion. |
| Jer 3:20 | declares | HNcmsc | none recorded | - | 0 | Surely, as a treacherous wife leaves her husband, so have you been treacherous to me, O house of Israel, **declares** the Lord.’” |
| Jer 4:1 | declares | HNcmsc | none recorded | - | 0 | “ If you return, O Israel, **declares** the Lord, to me you should return. If you remove your detestable things from my presence, and do not waver, |
| Jer 4:17 | declares | HNcmsc | none recorded | - | 0 | Like keepers of a field are they against her all around, because she has rebelled against me, **declares** the Lord. |
| Jer 5:9 | declares | HNcmsc | none recorded | - | 0 | Shall I not punish them for these things? **declares** the Lord; and shall I not avenge myself on a nation such as this? |
| Jer 5:11 | declares | HNcmsc | none recorded | - | 0 | For the house of Israel and the house of Judah have been utterly treacherous to me, **declares** the Lord. |
| Jer 5:15 | declares | HNcmsc | none recorded | - | 0 | Behold, I am bringing against you a nation from afar, O house of Israel, **declares** the Lord. It is an enduring nation; it is an ancient nation, a nation whose language you do not know, nor can you understand what they say. |
| Jer 5:22 | declares | HNcmsc | none recorded | - | 0 | Do you not fear me? **declares** the Lord. Do you not tremble before me? I placed the sand as the boundary for the sea, a perpetual barrier that it cannot pass; though the waves toss, they cannot prevail; though they roar, they cannot pass over it. |
| Jer 5:29 | declares | HNcmsc | none recorded | - | 0 | Shall I not punish them for these things? **declares** the Lord, and shall I not avenge myself on a nation such as this?” |
| Jer 6:12 | declares | HNcmsc | none recorded | - | 0 | Their houses shall be turned over to others, their fields and wives together, for I will stretch out my hand against the inhabitants of the land,” **declares** the Lord. |
| Jer 7:11 | declares | HNcmsc | none recorded | - | 0 | Has this house, which is called by my name, become a den of robbers in your eyes? Behold, I myself have seen it, **declares** the Lord. |
| Jer 7:13 | declares | HNcmsc | none recorded | - | 0 | And now, because you have done all these things, **declares** the Lord, and when I spoke to you persistently you did not listen, and when I called you, you did not answer, |
| Jer 7:19 | declares | HNcmsc | none recorded | 14526 | 0 | Is it I whom they provoke? **declares** the Lord. Is it not themselves, to their own shame? |
| Jer 7:30 | declares | HNcmsc | none recorded | - | 0 | “ For the sons of Judah have done evil in my sight, **declares** the Lord. They have set their detestable things in the house that is called by my name, to defile it. |
| Jer 7:32 | declares | HNcmsc | none recorded | - | 0 | Therefore, behold, the days are coming, **declares** the Lord, when it will no more be called Topheth, or the Valley of the Son of Hinnom, but the Valley of Slaughter; for they will bury in Topheth, because there is no room elsewhere. |
| Jer 8:13 | declares | HNcmsc | none recorded | - | 0 | When I would gather them, **declares** the Lord, there are no grapes on the vine, nor figs on the fig tree; even the leaves are withered, and what I gave them has passed away from them.” |
| Jer 9:3 | declares | HNcmsc | none recorded | - | 0 | They bend their tongue like a bow; falsehood and not truth has grown strong in the land; for they proceed from evil to evil, and they do not know me, **declares** the Lord. |
| Jer 9:9 | declares | HNcmsc | none recorded | - | 0 | Shall I not punish them for these things? **declares** the Lord, and shall I not avenge myself on a nation such as this? |
| Jer 9:22 | declares | HNcmsc | none recorded | - | 0 | Speak: “ Thus **declares** the Lord, ‘The dead bodies of men shall fall like dung upon the open field, like sheaves after the reaper, and none shall gather them.’” |
| Jer 9:24 | declares | HNcmsc | none recorded | - | 0 | but let him who boasts boast in this, that he understands and knows me, that I am the Lord who practices steadfast love, justice, and righteousness in the earth. For in these things I delight, **declares** the Lord.” |
| Jer 9:25 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming, **declares** the Lord, when I will punish all those who are circumcised merely in the flesh — |
| Jer 12:17 | declares | HNcmsc | none recorded | - | 0 | But if any nation will not listen, then I will utterly pluck it up and destroy it, **declares** the Lord.” |
| Jer 13:11 | declares | HNcmsc | none recorded | - | 0 | For as the loincloth clings to the waist of a man, so I made the whole house of Israel and the whole house of Judah cling to me, **declares** the Lord, that they might be for me a people, a name, a praise, and a glory, but they would not listen. |
| Jer 13:14 | declares | HNcmsc | none recorded | - | 0 | And I will dash them one against another, fathers and sons together, **declares** the Lord. I will not pity or spare or have compassion, that I should not destroy them.’” |
| Jer 15:3 | declares | HNcmsc | none recorded | - | 0 | I will appoint over them four kinds of destroyers, **declares** the Lord: the sword to kill, the dogs to tear, and the birds of the air and the beasts of the earth to devour and destroy. |
| Jer 15:9 | declares | HNcmsc | none recorded | - | 0 | She who bore seven has grown feeble; she has fainted away; her sun went down while it was yet day; she has been shamed and disgraced. And the rest of them I will give to the sword before their enemies, **declares** the Lord.” |
| Jer 15:20 | declares | HNcmsc | none recorded | - | 0 | And I will make you to this people a fortified wall of bronze; they will fight against you, but they shall not prevail over you, for I am with you to save you and deliver you, **declares** the Lord. |
| Jer 16:5 | declares | HNcmsc | none recorded | - | 0 | “For thus says the Lord: Do not enter the house of mourning, or go to lament or grieve for them, for I have taken away my peace from this people, my steadfast love and mercy, **declares** the Lord. |
| Jer 16:14 | declares | HNcmsc | none recorded | - | 0 | “ Therefore, behold, the days are coming, **declares** the Lord, when it shall no longer be said, ‘As the Lord lives who brought up the people of Israel out of the land of Egypt,’ |
| Jer 16:16 | declares | HNcmsc | none recorded | - | 0 | “ Behold, I am sending for many fishers, **declares** the Lord, and they shall catch them. And afterward I will send for many hunters, and they shall hunt them from every mountain and every hill, and out of the clefts of the rocks. |
| Jer 17:24 | declares | HNcmsc | none recorded | - | 0 | “‘But if you listen to me, **declares** the Lord, and bring in no burden by the gates of this city on the Sabbath day, but keep the Sabbath day holy and do no work on it, |
| Jer 18:6 | declares | HNcmsc | none recorded | - | 0 | “O house of Israel, can I not do with you as this potter has done? **declares** the Lord. Behold, like the clay in the potter’s hand, so are you in my hand, O house of Israel. |
| Jer 19:6 | declares | HNcmsc | none recorded | - | 0 | therefore, behold, days are coming, **declares** the Lord, when this place shall no more be called Topheth, or the Valley of the Son of Hinnom, but the Valley of Slaughter. |
| Jer 19:12 | declares | HNcmsc | none recorded | - | 0 | Thus will I do to this place, **declares** the Lord, and to its inhabitants, making this city like Topheth. |
| Jer 21:10 | declares | HNcmsc | none recorded | - | 0 | For I have set my face against this city for harm and not for good, **declares** the Lord: it shall be given into the hand of the king of Babylon, and he shall burn it with fire.’ |
| Jer 21:13 | declares | HNcmsc | none recorded | - | 0 | “ Behold, I am against you, O inhabitant of the valley, O rock of the plain, **declares** the Lord; you who say, ‘ Who shall come down against us, or who shall enter our habitations?’ |
| Jer 21:14 | declares | HNcmsc | none recorded | - | 0 | I will punish you according to the fruit of your deeds, **declares** the Lord; I will kindle a fire in her forest, and it shall devour all that is around her.” |
| Jer 22:5 | declares | HNcmsc | none recorded | - | 0 | But if you will not obey these words, I swear by myself, **declares** the Lord, that this house shall become a desolation. |
| Jer 22:24 | declares | HNcmsc | none recorded | - | 0 | “As I live, **declares** the Lord, though Coniah the son of Jehoiakim, king of Judah, were the signet ring on my right hand, yet I would tear you off |
| Jer 23:1 | declares | HNcmsc | none recorded | - | 0 | “ Woe to the shepherds who destroy and scatter the sheep of my pasture!” **declares** the Lord. |
| Jer 23:2 | declares | HNcmsc | none recorded | - | 0 | Therefore thus says the Lord, the God of Israel, concerning the shepherds who care for my people: “ You have scattered my flock and have driven them away, and you have not attended to them. Behold, I will attend to you for your evil deeds, **declares** the Lord. |
| Jer 23:4 | declares | HNcmsc | none recorded | - | 0 | I will set shepherds over them who will care for them, and they shall fear no more, nor be dismayed, neither shall any be missing, **declares** the Lord. |
| Jer 23:5 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming, **declares** the Lord, when I will raise up for David a righteous Branch, and he shall reign as king and deal wisely, and shall execute justice and righteousness in the land. |
| Jer 23:7 | declares | HNcmsc | none recorded | - | 0 | “ Therefore, behold, the days are coming, **declares** the Lord, when they shall no longer say, ‘As the Lord lives who brought up the people of Israel out of the land of Egypt,’ |
| Jer 23:11 | declares | HNcmsc | none recorded | - | 0 | “ Both prophet and priest are ungodly; even in my house I have found their evil, **declares** the Lord. |
| Jer 23:12 | declares | HNcmsc | none recorded | - | 0 | Therefore their way shall be to them like slippery paths in the darkness, into which they shall be driven and fall, for I will bring disaster upon them in the year of their punishment, **declares** the Lord. |
| Jer 23:24 | declares | HNcmsc | none recorded | 18877 | 0 | Can a man hide himself in secret places so that I cannot see him? **declares** the Lord. Do I not fill heaven and earth? declares the Lord. |
| Jer 23:24 | declares | HNcmsc | none recorded | 18877 | 0 | Can a man hide himself in secret places so that I cannot see him? **declares** the Lord. Do I not fill heaven and earth? declares the Lord. |
| Jer 23:28 | declares | HNcmsc | none recorded | - | 0 | Let the prophet who has a dream tell the dream, but let him who has my word speak my word faithfully. What has straw in common with wheat? **declares** the Lord. |
| Jer 23:29 | declares | HNcmsc | none recorded | - | 0 | Is not my word like fire, **declares** the Lord, and like a hammer that breaks the rock in pieces? |
| Jer 23:30 | declares | HNcmsc | none recorded | - | 0 | Therefore, behold, I am against the prophets, **declares** the Lord, who steal my words from one another. |
| Jer 23:31 | declares | HNcmsc | none recorded | - | 0 | Behold, I am against the prophets, **declares** the Lord, who use their tongues and declare, ‘ declares the Lord.’ |
| Jer 23:31 | declares | HNcmsa | none recorded | - | 0 | Behold, I am against the prophets, **declares** the Lord, who use their tongues and declare, ‘ declares the Lord.’ |
| Jer 23:32 | declares | HNcmsc | none recorded | - | 0 | Behold, I am against those who prophesy lying dreams, **declares** the Lord, and who tell them and lead my people astray by their lies and their recklessness, when I did not send them or charge them. So they do not profit this people at all, declares the Lord. |
| Jer 23:32 | declares | HNcmsc | none recorded | - | 0 | Behold, I am against those who prophesy lying dreams, **declares** the Lord, and who tell them and lead my people astray by their lies and their recklessness, when I did not send them or charge them. So they do not profit this people at all, declares the Lord. |
| Jer 25:7 | declares | HNcmsc | none recorded | 14526 | 0 | Yet you have not listened to me, **declares** the Lord, that you might provoke me to anger with the work of your hands to your own harm. |
| Jer 25:9 | declares | HNcmsc | none recorded | - | 0 | behold, I will send for all the tribes of the north, **declares** the Lord, and for Nebuchadnezzar the king of Babylon, my servant, and I will bring them against this land and its inhabitants, and against all these surrounding nations. I will devote them to destruction, and make them a horror, a hissing, and an everlasting desolation. |
| Jer 25:29 | declares | HNcmsc | none recorded | - | 0 | For behold, I begin to work disaster at the city that is called by my name, and shall you go unpunished? You shall not go unpunished, for I am summoning a sword against all the inhabitants of the earth, **declares** the Lord of hosts.’ |
| Jer 25:31 | declares | HNcmsc | none recorded | - | 0 | The clamor will resound to the ends of the earth, for the Lord has an indictment against the nations; he is entering into judgment with all flesh, and the wicked he will put to the sword, **declares** the Lord.’ |
| Jer 27:11 | declares | HNcmsc | none recorded | - | 0 | But any nation that will bring its neck under the yoke of the king of Babylon and serve him, I will leave on its own land, to work it and dwell there, **declares** the Lord.”’” |
| Jer 27:15 | declares | HNcmsc | none recorded | - | 0 | I have not sent them, **declares** the Lord, but they are prophesying falsely in my name, with the result that I will drive you out and you will perish, you and the prophets who are prophesying to you.” |
| Jer 28:4 | declares | HNcmsc | none recorded | - | 0 | I will also bring back to this place Jeconiah the son of Jehoiakim, king of Judah, and all the exiles from Judah who went to Babylon, **declares** the Lord, for I will break the yoke of the king of Babylon.” |
| Jer 29:9 | declares | HNcmsc | none recorded | - | 0 | for it is a lie that they are prophesying to you in my name; I did not send them, **declares** the Lord. |
| Jer 29:11 | declares | HNcmsc | none recorded | 19415 | 0 | For I know the plans I have for you, **declares** the Lord, plans for welfare and not for evil, to give you a future and a hope. |
| Jer 29:14 | declares | HNcmsc | none recorded | - | 0 | I will be found by you, **declares** the Lord, and I will restore your fortunes and gather you from all the nations and all the places where I have driven you, declares the Lord, and I will bring you back to the place from which I sent you into exile. |
| Jer 29:19 | declares | HNcmsc | none recorded | - | 0 | because they did not pay attention to my words, **declares** the Lord, that I persistently sent to you by my servants the prophets, but you would not listen, declares the Lord.’ |
| Jer 29:19 | declares | HNcmsc | none recorded | - | 0 | because they did not pay attention to my words, **declares** the Lord, that I persistently sent to you by my servants the prophets, but you would not listen, declares the Lord.’ |
| Jer 29:23 | declares | HNcmsc | none recorded | - | 0 | because they have done an outrageous thing in Israel, they have committed adultery with their neighbors ’ wives, and they have spoken in my name lying words that I did not command them. I am the one who knows, and I am witness, **declares** the Lord.’” |
| Jer 29:32 | declares | HNcmsc | none recorded | - | 0 | therefore thus says the Lord: Behold, I will punish Shemaiah of Nehelam and his descendants. He shall not have anyone living among this people, and he shall not see the good that I will do to my people, **declares** the Lord, for he has spoken rebellion against the Lord.’” |
| Jer 30:3 | declares | HNcmsc | none recorded | - | 0 | For behold, days are coming, **declares** the Lord, when I will restore the fortunes of my people, Israel and Judah, says the Lord, and I will bring them back to the land that I gave to their fathers, and they shall take possession of it.” |
| Jer 30:10 | declares | HNcmsc | none recorded | - | 0 | “Then fear not, O Jacob my servant, **declares** the Lord, nor be dismayed, O Israel; for behold, I will save you from far away, and your offspring from the land of their captivity. Jacob shall return and have quiet and ease, and none shall make him afraid. |
| Jer 30:11 | declares | HNcmsc | none recorded | - | 0 | For I am with you to save you, **declares** the Lord; I will make a full end of all the nations among whom I scattered you, but of you I will not make a full end. I will discipline you in just measure, and I will by no means leave you unpunished. |
| Jer 30:17 | declares | HNcmsc | none recorded | - | 0 | For I will restore health to you, and your wounds I will heal, **declares** the Lord, because they have called you an outcast: ‘It is Zion, for whom no one cares!’ |
| Jer 31:14 | declares | HNcmsc | none recorded | - | 0 | I will feast the soul of the priests with abundance, and my people shall be satisfied with my goodness, **declares** the Lord.” |
| Jer 31:16 | declares | HNcmsc | none recorded | - | 0 | Thus says the Lord: “ Keep your voice from weeping, and your eyes from tears, for there is a reward for your work, **declares** the Lord, and they shall come back from the land of the enemy. |
| Jer 31:17 | declares | HNcmsc | none recorded | - | 0 | There is hope for your future, **declares** the Lord, and your children shall come back to their own country. |
| Jer 31:20 | declares | HNcmsc | none recorded | - | 0 | Is Ephraim my dear son? Is he my darling child? For as often as I speak against him, I do remember him still. Therefore my heart yearns for him; I will surely have mercy on him, **declares** the Lord. |
| Jer 31:27 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming, **declares** the Lord, when I will sow the house of Israel and the house of Judah with the seed of man and the seed of beast. |
| Jer 31:28 | declares | HNcmsc | none recorded | - | 0 | And it shall come to pass that as I have watched over them to pluck up and break down, to overthrow, destroy, and bring harm, so I will watch over them to build and to plant, **declares** the Lord. |
| Jer 31:31 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming, **declares** the Lord, when I will make a new covenant with the house of Israel and the house of Judah, |
| Jer 31:32 | declares | HNcmsc | none recorded | - | 0 | not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt, my covenant that they broke, though I was their husband, **declares** the Lord. |
| Jer 31:34 | declares | HNcmsc | none recorded | - | 0 | And no longer shall each one teach his neighbor and each his brother, saying, ‘ Know the Lord,’ for they shall all know me, from the least of them to the greatest, **declares** the Lord. For I will forgive their iniquity, and I will remember their sin no more.” |
| Jer 31:36 | declares | HNcmsc | none recorded | - | 0 | “ If this fixed order departs from before me, **declares** the Lord, then shall the offspring of Israel cease from being a nation before me forever.” |
| Jer 31:37 | declares | HNcmsc | none recorded | - | 0 | Thus says the Lord: “ If the heavens above can be measured, and the foundations of the earth below can be explored, then I will cast off all the offspring of Israel for all that they have done, **declares** the Lord.” |
| Jer 31:38 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming, **declares** the Lord, when the city shall be rebuilt for the Lord from the Tower of Hananel to the Corner Gate. |
| Jer 32:30 | declares | HNcmsc | none recorded | 14526 | 0 | For the children of Israel and the children of Judah have done nothing but evil in my sight from their youth. The children of Israel have done nothing but provoke me to anger by the work of their hands, **declares** the Lord. |
| Jer 32:44 | declares | HNcmsc | none recorded | - | 0 | Fields shall be bought for money, and deeds shall be signed and sealed and witnessed, in the land of Benjamin, in the places about Jerusalem, and in the cities of Judah, in the cities of the hill country, in the cities of the Shephelah, and in the cities of the Negeb; for I will restore their fortunes, **declares** the Lord.” |
| Jer 33:14 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming, **declares** the Lord, when I will fulfill the promise I made to the house of Israel and the house of Judah. |
| Jer 34:5 | declares | HNcmsc | none recorded | - | 0 | You shall die in peace. And as spices were burned for your fathers, the former kings who were before you, so people shall burn spices for you and lament for you, saying, “ Alas, lord!”’ For I have spoken the word, **declares** the Lord.” |
| Jer 34:17 | declares | HNcmsc | none recorded | - | 0 | “ Therefore, thus says the Lord: You have not obeyed me by proclaiming liberty, every one to his brother and to his neighbor; behold, I proclaim to you liberty to the sword, to pestilence, and to famine, **declares** the Lord. I will make you a horror to all the kingdoms of the earth. |
| Jer 34:22 | declares | HNcmsc | none recorded | - | 0 | Behold, I will command, **declares** the Lord, and will bring them back to this city. And they will fight against it and take it and burn it with fire. I will make the cities of Judah a desolation without inhabitant.” |
| Jer 35:13 | declares | HNcmsc | none recorded | - | 0 | “ Thus says the Lord of hosts, the God of Israel: Go and say to the people of Judah and the inhabitants of Jerusalem, Will you not receive instruction and listen to my words? **declares** the Lord. |
| Jer 39:18 | declares | HNcmsc | none recorded | - | 0 | For I will surely save you, and you shall not fall by the sword, but you shall have your life as a prize of war, because you have put your trust in me, **declares** the Lord.’” |
| Jer 42:11 | declares | HNcmsc | none recorded | - | 0 | Do not fear the king of Babylon, of whom you are afraid. Do not fear him, **declares** the Lord, for I am with you, to save you and to deliver you from his hand. |
| Jer 44:29 | declares | HNcmsc | none recorded | - | 0 | This shall be the sign to you, **declares** the Lord, that I will punish you in this place, in order that you may know that my words will surely stand against you for harm: |
| Jer 45:5 | declares | HNcmsc | none recorded | - | 0 | And do you seek great things for yourself? Seek them not, for behold, I am bringing disaster upon all flesh, **declares** the Lord. But I will give you your life as a prize of war in all places to which you may go.” |
| Jer 46:5 | declares | HNcmsc | none recorded | - | 0 | Why have I seen it? They are dismayed and have turned backward. Their warriors are beaten down and have fled in haste; they look not back — terror on every side! **declares** the Lord. |
| Jer 46:23 | declares | HNcmsc | none recorded | - | 0 | They shall cut down her forest, **declares** the Lord, though it is impenetrable, because they are more numerous than locusts; they are without number. |
| Jer 46:26 | declares | HNcmsc | none recorded | - | 0 | I will deliver them into the hand of those who seek their life, into the hand of Nebuchadnezzar king of Babylon and his officers. Afterward Egypt shall be inhabited as in the days of old, **declares** the Lord. |
| Jer 46:28 | declares | HNcmsc | none recorded | - | 0 | Fear not, O Jacob my servant, **declares** the Lord, for I am with you. I will make a full end of all the nations to which I have driven you, but of you I will not make a full end. I will discipline you in just measure, and I will by no means leave you unpunished.” |
| Jer 48:12 | declares | HNcmsc | none recorded | - | 0 | “ Therefore, behold, the days are coming, **declares** the Lord, when I shall send to him pourers who will pour him, and empty his vessels and break his jars in pieces. |
| Jer 48:15 | declares | HNcmsc | none recorded | - | 0 | The destroyer of Moab and his cities has come up, and the choicest of his young men have gone down to slaughter, **declares** the King, whose name is the Lord of hosts. |
| Jer 48:25 | declares | HNcmsc | none recorded | - | 0 | The horn of Moab is cut off, and his arm is broken, **declares** the Lord. |
| Jer 48:30 | declares | HNcmsc | none recorded | - | 0 | I know his insolence, **declares** the Lord; his boasts are false, his deeds are false. |
| Jer 48:35 | declares | HNcmsc | none recorded | - | 0 | And I will bring to an end in Moab, **declares** the Lord, him who offers sacrifice in the high place and makes offerings to his god. |
| Jer 48:38 | declares | HNcmsc | none recorded | - | 0 | On all the housetops of Moab and in the squares there is nothing but lamentation, for I have broken Moab like a vessel for which no one cares, **declares** the Lord. |
| Jer 48:43 | declares | HNcmsc | none recorded | - | 0 | Terror, pit, and snare are before you, O inhabitant of Moab! **declares** the Lord. |
| Jer 48:44 | declares | HNcmsc | none recorded | - | 0 | He who flees from the terror shall fall into the pit, and he who climbs out of the pit shall be caught in the snare. For I will bring these things upon Moab, the year of their punishment, **declares** the Lord. |
| Jer 48:47 | declares | HNcmsc | none recorded | - | 0 | Yet I will restore the fortunes of Moab in the latter days, **declares** the Lord.” Thus far is the judgment on Moab. |
| Jer 49:2 | declares | HNcmsc | none recorded | - | 0 | Therefore, behold, the days are coming, **declares** the Lord, when I will cause the battle cry to be heard against Rabbah of the Ammonites; it shall become a desolate mound, and its villages shall be burned with fire; then Israel shall dispossess those who dispossessed him, says the Lord. |
| Jer 49:5 | declares | HNcmsc | none recorded | - | 0 | Behold, I will bring terror upon you, **declares** the Lord God of hosts, from all who are around you, and you shall be driven out, every man straight before him, with none to gather the fugitives. |
| Jer 49:6 | declares | HNcmsc | none recorded | - | 0 | “But afterward I will restore the fortunes of the Ammonites, **declares** the Lord.” |
| Jer 49:13 | declares | HNcmsc | none recorded | - | 0 | For I have sworn by myself, **declares** the Lord, that Bozrah shall become a horror, a taunt, a waste, and a curse, and all her cities shall be perpetual wastes.” |
| Jer 49:16 | declares | HNcmsc | none recorded | - | 0 | The horror you inspire has deceived you, and the pride of your heart, you who live in the clefts of the rock, who hold the height of the hill. Though you make your nest as high as the eagle’s, I will bring you down from there, **declares** the Lord. |
| Jer 49:30 | declares | HNcmsc | none recorded | - | 0 | Flee, wander far away, dwell in the depths, O inhabitants of Hazor! **declares** the Lord. For Nebuchadnezzar king of Babylon has made a plan against you and formed a purpose against you. |
| Jer 49:31 | declares | HNcmsc | none recorded | - | 0 | “Rise up, advance against a nation at ease, that dwells securely, **declares** the Lord, that has no gates or bars, that dwells alone. |
| Jer 49:32 | declares | HNcmsc | none recorded | - | 0 | Their camels shall become plunder, their herds of livestock a spoil. I will scatter to every wind those who cut the corners of their hair, and I will bring their calamity from every side of them, **declares** the Lord. |
| Jer 49:37 | declares | HNcmsc | none recorded | - | 0 | I will terrify Elam before their enemies and before those who seek their life. I will bring disaster upon them, my fierce anger, **declares** the Lord. I will send the sword after them, until I have consumed them, |
| Jer 49:38 | declares | HNcmsc | none recorded | - | 0 | and I will set my throne in Elam and destroy their king and officials, **declares** the Lord. |
| Jer 49:39 | declares | HNcmsc | none recorded | - | 0 | “But in the latter days I will restore the fortunes of Elam, **declares** the Lord.” |
| Jer 50:10 | declares | HNcmsc | none recorded | - | 0 | Chaldea shall be plundered; all who plunder her shall be sated, **declares** the Lord. |
| Jer 50:31 | declares | HNcmsc | none recorded | - | 0 | “ Behold, I am against you, O proud one, **declares** the Lord God of hosts, for your day has come, the time when I will punish you. |
| Jer 50:35 | declares | HNcmsc | none recorded | - | 0 | “A sword against the Chaldeans, **declares** the Lord, and against the inhabitants of Babylon, and against her officials and her wise men! |
| Jer 50:40 | declares | HNcmsc | none recorded | - | 0 | As when God overthrew Sodom and Gomorrah and their neighboring cities, **declares** the Lord, so no man shall dwell there, and no son of man shall sojourn in her. |
| Jer 51:24 | declares | HNcmsc | none recorded | - | 0 | “I will repay Babylon and all the inhabitants of Chaldea before your very eyes for all the evil that they have done in Zion, **declares** the Lord. |
| Jer 51:25 | declares | HNcmsc | none recorded | - | 0 | “ Behold, I am against you, O destroying mountain, **declares** the Lord, which destroys the whole earth; I will stretch out my hand against you, and roll you down from the crags, and make you a burnt mountain. |
| Jer 51:39 | declares | HNcmsc | none recorded | - | 0 | While they are inflamed I will prepare them a feast and make them drunk, that they may become merry, then sleep a perpetual sleep and not wake, **declares** the Lord. |
| Jer 51:48 | declares | HNcmsc | none recorded | - | 0 | Then the heavens and the earth, and all that is in them, shall sing for joy over Babylon, for the destroyers shall come against them out of the north, **declares** the Lord. |
| Jer 51:52 | declares | HNcmsc | none recorded | - | 0 | “ Therefore, behold, the days are coming, **declares** the Lord, when I will execute judgment upon her images, and through all her land the wounded shall groan. |
| Jer 51:53 | declares | HNcmsc | none recorded | - | 0 | Though Babylon should mount up to heaven, and though she should fortify her strong height, yet destroyers would come from me against her, **declares** the Lord. |
| Jer 51:57 | declares | HNcmsc | none recorded | - | 0 | I will make drunk her officials and her wise men, her governors, her commanders, and her warriors; they shall sleep a perpetual sleep and not wake, **declares** the King, whose name is the Lord of hosts. |
| Eze 5:11 | declares | HNcmsc | none recorded | - | 0 | Therefore, as I live, **declares** the Lord God, surely, because you have defiled my sanctuary with all your detestable things and with all your abominations, therefore I will withdraw. My eye will not spare, and I will have no pity. |
| Eze 11:8 | declares | HNcmsc | none recorded | - | 0 | You have feared the sword, and I will bring the sword upon you, **declares** the Lord God. |
| Eze 11:21 | declares | HNcmsc | none recorded | - | 0 | But as for those whose heart goes after their detestable things and their abominations, I will bring their deeds upon their own heads, **declares** the Lord God.” |
| Eze 12:25 | declares | HNcmsc | none recorded | - | 0 | For I am the Lord; I will speak the word that I will speak, and it will be performed. It will no longer be delayed, but in your days, O rebellious house, I will speak the word and perform it, **declares** the Lord God.” |
| Eze 12:28 | declares | HNcmsc | none recorded | - | 0 | Therefore say to them, Thus says the Lord God: None of my words will be delayed any longer, but the word that I speak will be performed, **declares** the Lord God.” |
| Eze 13:6 | declares | HNcmsc | none recorded | - | 0 | They have seen false visions and lying divinations. They say, ‘ **Declares** the Lord,’ when the Lord has not sent them, and yet they expect him to fulfill their word. |
| Eze 13:7 | declares | HNcmsc | none recorded | - | 0 | Have you not seen a false vision and uttered a lying divination, whenever you have said, ‘ **Declares** the Lord,’ although I have not spoken?” |
| Eze 13:8 | declares | HNcmsc | none recorded | - | 0 | Therefore thus says the Lord God: “ Because you have uttered falsehood and seen lying visions, therefore behold, I am against you, **declares** the Lord God. |
| Eze 13:16 | declares | HNcmsc | none recorded | - | 0 | the prophets of Israel who prophesied concerning Jerusalem and saw visions of peace for her, when there was no peace, **declares** the Lord God. |
| Eze 14:11 | declares | HNcmsc | none recorded | - | 0 | that the house of Israel may no more go astray from me, nor defile themselves anymore with all their transgressions, but that they may be my people and I may be their God, **declares** the Lord God.” |
| Eze 14:14 | declares | HNcmsc | none recorded | - | 0 | even if these three men, Noah, Daniel, and Job, were in it, they would deliver but their own lives by their righteousness, **declares** the Lord God. |
| Eze 14:16 | declares | HNcmsc | none recorded | - | 0 | even if these three men were in it, as I live, **declares** the Lord God, they would deliver neither sons nor daughters. They alone would be delivered, but the land would be desolate. |
| Eze 14:18 | declares | HNcmsc | none recorded | - | 0 | though these three men were in it, as I live, **declares** the Lord God, they would deliver neither sons nor daughters, but they alone would be delivered. |
| Eze 14:20 | declares | HNcmsc | none recorded | - | 0 | even if Noah, Daniel, and Job were in it, as I live, **declares** the Lord God, they would deliver neither son nor daughter. They would deliver but their own lives by their righteousness. |
| Eze 14:23 | declares | HNcmsc | none recorded | - | 0 | They will console you, when you see their ways and their deeds, and you shall know that I have not done without cause all that I have done in it, **declares** the Lord God.” |
| Eze 15:8 | declares | HNcmsc | none recorded | - | 0 | And I will make the land desolate, because they have acted faithlessly, **declares** the Lord God.” |
| Eze 16:8 | declares | HNcmsc | none recorded | - | 0 | “When I passed by you again and saw you, behold, you were at the age for love, and I spread the corner of my garment over you and covered your nakedness; I made my vow to you and entered into a covenant with you, **declares** the Lord God, and you became mine. |
| Eze 16:14 | declares | HNcmsc | none recorded | - | 0 | And your renown went forth among the nations because of your beauty, for it was perfect through the splendor that I had bestowed on you, **declares** the Lord God. |
| Eze 16:19 | declares | HNcmsc | none recorded | - | 0 | Also my bread that I gave you— I fed you with fine flour and oil and honey —you set before them for a pleasing aroma; and so it was, **declares** the Lord God. |
| Eze 16:23 | declares | HNcmsc | none recorded | - | 0 | “And after all your wickedness ( woe, woe to you! **declares** the Lord God ), |
| Eze 16:30 | declares | HNcmsc | none recorded | - | 0 | “ How sick is your heart, **declares** the Lord God, because you did all these things, the deeds of a brazen prostitute, |
| Eze 16:43 | declares | HNcmsc | none recorded | - | 0 | Because you have not remembered the days of your youth, but have enraged me with all these things, therefore, behold, I have returned your deeds upon your head, **declares** the Lord God. Have you not committed lewdness in addition to all your abominations? |
| Eze 16:48 | declares | HNcmsc | none recorded | - | 0 | As I live, **declares** the Lord God, your sister Sodom and her daughters have not done as you and your daughters have done. |
| Eze 16:58 | declares | HNcmsc | none recorded | - | 0 | You bear the penalty of your lewdness and your abominations, **declares** the Lord. |
| Eze 16:63 | declares | HNcmsc | none recorded | - | 0 | that you may remember and be confounded, and never open your mouth again because of your shame, when I atone for you for all that you have done, **declares** the Lord God.” |
| Eze 17:16 | declares | HNcmsc | none recorded | - | 0 | “As I live, **declares** the Lord God, surely in the place where the king dwells who made him king, whose oath he despised, and whose covenant with him he broke, in Babylon he shall die. |
| Eze 18:3 | declares | HNcmsc | none recorded | - | 0 | As I live, **declares** the Lord God, this proverb shall no more be used by you in Israel. |
| Eze 18:9 | declares | HNcmsc | none recorded | - | 0 | walks in my statutes, and keeps my rules by acting faithfully —he is righteous; he shall surely live, **declares** the Lord God. |
| Eze 18:23 | declares | HNcmsc | none recorded | - | 0 | Have I any pleasure in the death of the wicked, **declares** the Lord God, and not rather that he should turn from his way and live? |
| Eze 18:30 | declares | HNcmsc | none recorded | - | 0 | “ Therefore I will judge you, O house of Israel, every one according to his ways, **declares** the Lord God. Repent and turn from all your transgressions, lest iniquity be your ruin. |
| Eze 18:32 | declares | HNcmsc | none recorded | - | 0 | For I have no pleasure in the death of anyone, **declares** the Lord God; so turn, and live.” |
| Eze 20:3 | declares | HNcmsc | none recorded | - | 0 | “ Son of man, speak to the elders of Israel, and say to them, Thus says the Lord God, Is it to inquire of me that you come? As I live, **declares** the Lord God, I will not be inquired of by you. |
| Eze 20:33 | declares | HNcmsc | none recorded | 13889 | 0 | “As I live, **declares** the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you. |
| Eze 20:36 | declares | HNcmsc | none recorded | - | 0 | As I entered into judgment with your fathers in the wilderness of the land of Egypt, so I will enter into judgment with you, **declares** the Lord God. |
| Eze 20:40 | declares | HNcmsc | none recorded | - | 0 | “ For on my holy mountain, the mountain height of Israel, **declares** the Lord God, there all the house of Israel, all of them, shall serve me in the land. There I will accept them, and there I will require your contributions and the choicest of your gifts, with all your sacred offerings. |
| Eze 20:44 | declares | HNcmsc | none recorded | - | 0 | And you shall know that I am the Lord, when I deal with you for my name’s sake, not according to your evil ways, nor according to your corrupt deeds, O house of Israel, **declares** the Lord God.” |
| Eze 22:12 | declares | HNcmsc | none recorded | - | 0 | In you they take bribes to shed blood; you take interest and profit and make gain of your neighbors by extortion; but me you have forgotten, **declares** the Lord God. |
| Eze 22:31 | declares | HNcmsc | none recorded | - | 0 | Therefore I have poured out my indignation upon them. I have consumed them with the fire of my wrath. I have returned their way upon their heads, **declares** the Lord God.” |
| Eze 23:34 | declares | HNcmsc | none recorded | - | 0 | you shall drink it and drain it out, and gnaw its shards, and tear your breasts; for I have spoken, **declares** the Lord God. |
| Eze 24:14 | declares | HNcmsc | none recorded | - | 0 | I am the Lord. I have spoken; it shall come to pass; I will do it. I will not go back; I will not spare; I will not relent; according to your ways and your deeds you will be judged, **declares** the Lord God.” |
| Eze 25:14 | declares | HNcmsc | none recorded | - | 0 | And I will lay my vengeance upon Edom by the hand of my people Israel, and they shall do in Edom according to my anger and according to my wrath, and they shall know my vengeance, **declares** the Lord God. |
| Eze 26:5 | declares | HNcmsc | none recorded | - | 0 | She shall be in the midst of the sea a place for the spreading of nets, for I have spoken, **declares** the Lord God. And she shall become plunder for the nations, |
| Eze 26:14 | declares | HNcmsc | none recorded | - | 0 | I will make you a bare rock. You shall be a place for the spreading of nets. You shall never be rebuilt, for I am the Lord; I have spoken, **declares** the Lord God. |
| Eze 26:21 | declares | HNcmsc | none recorded | - | 0 | I will bring you to a dreadful end, and you shall be no more. Though you be sought for, you will never be found again, **declares** the Lord God.” |
| Eze 28:10 | declares | HNcmsc | none recorded | - | 0 | You shall die the death of the uncircumcised by the hand of foreigners; for I have spoken, **declares** the Lord God.” |
| Eze 29:20 | declares | HNcmsc | none recorded | - | 0 | I have given him the land of Egypt as his payment for which he labored, because they worked for me, **declares** the Lord God. |
| Eze 30:6 | declares | HNcmsc | none recorded | - | 0 | “ Thus says the Lord: Those who support Egypt shall fall, and her proud might shall come down; from Migdol to Syene they shall fall within her by the sword, **declares** the Lord God. |
| Eze 31:18 | declares | HNcmsc | none recorded | - | 0 | “ Whom are you thus like in glory and in greatness among the trees of Eden? You shall be brought down with the trees of Eden to the world below. You shall lie among the uncircumcised, with those who are slain by the sword. “This is Pharaoh and all his multitude, **declares** the Lord God.” |
| Eze 32:8 | declares | HNcmsc | none recorded | - | 0 | All the bright lights of heaven will I make dark over you, and put darkness on your land, **declares** the Lord God. |
| Eze 32:14 | declares | HNcmsc | none recorded | - | 0 | Then I will make their waters clear, and cause their rivers to run like oil, **declares** the Lord God. |
| Eze 32:31 | declares | HNcmsc | none recorded | - | 0 | “When Pharaoh sees them, he will be comforted for all his multitude, Pharaoh and all his army, slain by the sword, **declares** the Lord God. |
| Eze 32:32 | declares | HNcmsc | none recorded | - | 0 | For I spread terror in the land of the living; and he shall be laid to rest among the uncircumcised, with those who are slain by the sword, Pharaoh and all his multitude, **declares** the Lord God.” |
| Eze 33:11 | declares | HNcmsc | none recorded | 18278 | 0 | Say to them, As I live, **declares** the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live; turn back, turn back from your evil ways, for why will you die, O house of Israel? |
| Eze 34:8 | declares | HNcmsc | none recorded | - | 0 | As I live, **declares** the Lord God, surely because my sheep have become a prey, and my sheep have become food for all the wild beasts, since there was no shepherd, and because my shepherds have not searched for my sheep, but the shepherds have fed themselves, and have not fed my sheep, |
| Eze 34:15 | declares | HNcmsc | none recorded | - | 0 | I myself will be the shepherd of my sheep, and I myself will make them lie down, **declares** the Lord God. |
| Eze 34:30 | declares | HNcmsc | none recorded | - | 0 | And they shall know that I am the Lord their God with them, and that they, the house of Israel, are my people, **declares** the Lord God. |
| Eze 34:31 | declares | HNcmsc | none recorded | - | 0 | And you are my sheep, human sheep of my pasture, and I am your God, **declares** the Lord God.” |
| Eze 35:6 | declares | HNcmsc | none recorded | - | 0 | therefore, as I live, **declares** the Lord God, I will prepare you for blood, and blood shall pursue you; because you did not hate bloodshed, therefore blood shall pursue you. |
| Eze 36:14 | declares | HNcmsc | none recorded | - | 0 | therefore you shall no longer devour people and no longer bereave your nation of children, **declares** the Lord God. |
| Eze 36:15 | declares | HNcmsc | none recorded | - | 0 | And I will not let you hear anymore the reproach of the nations, and you shall no longer bear the disgrace of the peoples and no longer cause your nation to stumble, **declares** the Lord God.” |
| Eze 36:23 | declares | HNcmsc | none recorded | - | 0 | And I will vindicate the holiness of my great name, which has been profaned among the nations, and which you have profaned among them. And the nations will know that I am the Lord, **declares** the Lord God, when through you I vindicate my holiness before their eyes. |
| Eze 36:32 | declares | HNcmsc | none recorded | - | 0 | It is not for your sake that I will act, **declares** the Lord God; let that be known to you. Be ashamed and confounded for your ways, O house of Israel. |
| Eze 37:14 | declares | HNcmsc | none recorded | - | 0 | And I will put my Spirit within you, and you shall live, and I will place you in your own land. Then you shall know that I am the Lord; I have spoken, and I will do it, **declares** the Lord.” |
| Eze 38:18 | declares | HNcmsc | none recorded | - | 0 | But on that day, the day that Gog shall come against the land of Israel, **declares** the Lord God, my wrath will be roused in my anger. |
| Eze 38:21 | declares | HNcmsc | none recorded | - | 0 | I will summon a sword against Gog on all my mountains, **declares** the Lord God. Every man’s sword will be against his brother. |
| Eze 39:5 | declares | HNcmsc | none recorded | - | 0 | You shall fall in the open field, for I have spoken, **declares** the Lord God. |
| Eze 39:8 | declares | HNcmsc | none recorded | - | 0 | Behold, it is coming and it will be brought about, **declares** the Lord God. That is the day of which I have spoken. |
| Eze 39:10 | declares | HNcmsc | none recorded | - | 0 | so that they will not need to take wood out of the field or cut down any out of the forests, for they will make their fires of the weapons. They will seize the spoil of those who despoiled them, and plunder those who plundered them, **declares** the Lord God. |
| Eze 39:13 | declares | HNcmsc | none recorded | - | 0 | All the people of the land will bury them, and it will bring them renown on the day that I show my glory, **declares** the Lord God. |
| Eze 39:20 | declares | HNcmsc | none recorded | - | 0 | And you shall be filled at my table with horses and charioteers, with mighty men and all kinds of warriors,’ **declares** the Lord God. |
| Eze 39:29 | declares | HNcmsc | none recorded | - | 0 | And I will not hide my face anymore from them, when I pour out my Spirit upon the house of Israel, **declares** the Lord God.” |
| Eze 43:19 | declares | HNcmsc | none recorded | - | 0 | you shall give to the Levitical priests of the family of Zadok, who draw near to me to minister to me, **declares** the Lord God, a bull from the herd for a sin offering. |
| Eze 44:12 | declares | HNcmsc | none recorded | - | 0 | Because they ministered to them before their idols and became a stumbling block of iniquity to the house of Israel, therefore I have sworn concerning them, **declares** the Lord God, and they shall bear their punishment. |
| Eze 44:15 | declares | HNcmsc | none recorded | - | 0 | “But the Levitical priests, the sons of Zadok, who kept the charge of my sanctuary when the people of Israel went astray from me, shall come near to me to minister to me. And they shall stand before me to offer me the fat and the blood, **declares** the Lord God. |
| Eze 44:27 | declares | HNcmsc | none recorded | - | 0 | And on the day that he goes into the Holy Place, into the inner court, to minister in the Holy Place, he shall offer his sin offering, **declares** the Lord God. |
| Eze 47:23 | declares | HNcmsc | none recorded | - | 0 | In whatever tribe the sojourner resides, there you shall assign him his inheritance, **declares** the Lord God. |
| Eze 48:29 | declares | HNcmsc | none recorded | - | 0 | This is the land that you shall allot as an inheritance among the tribes of Israel, and these are their portions, **declares** the Lord God. |
| Hos 2:13 | declares | HNcmsc | none recorded | - | 0 | And I will punish her for the feast days of the Baals when she burned offerings to them and adorned herself with her ring and jewelry, and went after her lovers and forgot me, **declares** the Lord. |
| Hos 2:21 | declares | HNcmsc | none recorded | - | 0 | “And in that day I will answer, **declares** the Lord, I will answer the heavens, and they shall answer the earth, |
| Hos 11:11 | declares | HNcmsc | none recorded | - | 0 | they shall come trembling like birds from Egypt, and like doves from the land of Assyria, and I will return them to their homes, **declares** the Lord. |
| Joe 2:12 | declares | HNcmsc | none recorded | 14765 | 0 | “Yet even now,” **declares** the Lord, “ return to me with all your heart, with fasting, with weeping, and with mourning; |
| Amo 2:11 | declares | HNcmsc | none recorded | - | 0 | And I raised up some of your sons for prophets, and some of your young men for Nazirites. Is it not indeed so, O people of Israel?” **declares** the Lord. |
| Amo 3:10 | declares | HNcmsc | none recorded | - | 0 | “They do not know how to do right,” **declares** the Lord, “those who store up violence and robbery in their strongholds.” |
| Amo 3:13 | declares | HNcmsc | none recorded | - | 0 | “ Hear, and testify against the house of Jacob,” **declares** the Lord God, the God of hosts, |
| Amo 3:15 | declares | HNcmsc | none recorded | - | 0 | I will strike the winter house along with the summer house, and the houses of ivory shall perish, and the great houses shall come to an end,” **declares** the Lord. |
| Amo 4:3 | declares | HNcmsc | none recorded | - | 0 | And you shall go out through the breaches, each one straight ahead; and you shall be cast out into Harmon,” **declares** the Lord. |
| Amo 4:5 | declares | HNcmsc | none recorded | - | 0 | offer a sacrifice of thanksgiving of that which is leavened, and proclaim freewill offerings, publish them; for so you love to do, O people of Israel!” **declares** the Lord God. |
| Amo 6:8 | declares | HNcmsc | none recorded | - | 0 | The Lord God has sworn by himself, **declares** the Lord, the God of hosts: “I abhor the pride of Jacob and hate his strongholds, and I will deliver up the city and all that is in it.” |
| Amo 6:14 | declares | HNcmsc | none recorded | - | 0 | “ For behold, I will raise up against you a nation, O house of Israel,” **declares** the Lord, the God of hosts; “and they shall oppress you from Lebo-hamath to the Brook of the Arabah.” |
| Amo 8:3 | declares | HNcmsc | none recorded | - | 0 | The songs of the temple shall become wailings in that day,” **declares** the Lord God. “So many dead bodies!” “They are thrown everywhere!” “ Silence!” |
| Amo 8:11 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming,” **declares** the Lord God, “when I will send a famine on the land — not a famine of bread, nor a thirst for water, but of hearing the words of the Lord. |
| Amo 9:7 | declares | HNcmsc | none recorded | - | 0 | “Are you not like the Cushites to me, O people of Israel?” **declares** the Lord. “Did I not bring up Israel from the land of Egypt, and the Philistines from Caphtor and the Syrians from Kir? |
| Amo 9:8 | declares | HNcmsc | none recorded | - | 0 | Behold, the eyes of the Lord God are upon the sinful kingdom, and I will destroy it from the surface of the ground, except that I will not utterly destroy the house of Jacob,” **declares** the Lord. |
| Amo 9:13 | declares | HNcmsc | none recorded | - | 0 | “ Behold, the days are coming,” **declares** the Lord, “when the plowman shall overtake the reaper and the treader of grapes him who sows the seed; the mountains shall drip sweet wine, and all the hills shall flow with it. |
| Obd 4 | declares | HNcmsc | none recorded | - | 0 | Though you soar aloft like the eagle, though your nest is set among the stars, from there I will bring you down, **declares** the Lord. |
| Obd 8 | declares | HNcmsc | none recorded | - | 0 | Will I not on that day, **declares** the Lord, destroy the wise men out of Edom, and understanding out of Mount Esau? |
| Mic 4:6 | declares | HNcmsc | none recorded | - | 0 | In that day, **declares** the Lord, I will assemble the lame and gather those who have been driven away and those whom I have afflicted; |
| Mic 5:10 | declares | HNcmsc | none recorded | - | 0 | And in that day, **declares** the Lord, I will cut off your horses from among you and will destroy your chariots; |
| Nah 2:13 | declares | HNcmsc | none recorded | - | 0 | Behold, I am against you, **declares** the Lord of hosts, and I will burn your chariots in smoke, and the sword shall devour your young lions. I will cut off your prey from the earth, and the voice of your messengers shall no longer be heard. |
| Nah 3:5 | declares | HNcmsc | none recorded | - | 0 | Behold, I am against you, **declares** the Lord of hosts, and will lift up your skirts over your face; and I will make nations look at your nakedness and kingdoms at your shame. |
| Zep 1:2 | declares | HNcmsc | none recorded | - | 0 | “I will utterly sweep away everything from the face of the earth,” **declares** the Lord. |
| Zep 1:3 | declares | HNcmsc | none recorded | - | 0 | “I will sweep away man and beast; I will sweep away the birds of the heavens and the fish of the sea, and the rubble with the wicked. I will cut off mankind from the face of the earth,” **declares** the Lord. |
| Zep 3:8 | declares | HNcmsc | none recorded | - | 0 | “ Therefore wait for me,” **declares** the Lord, “ for the day when I rise up to seize the prey. For my decision is to gather nations, to assemble kingdoms, to pour out upon them my indignation, all my burning anger; for in the fire of my jealousy all the earth shall be consumed. |
| Hag 1:9 | declares | HNcmsc | none recorded | - | 0 | You looked for much, and behold, it came to little. And when you brought it home, I blew it away. Why? **declares** the Lord of hosts. Because of my house that lies in ruins, while each of you busies himself with his own house. |
| Hag 1:13 | declares | HNcmsc | none recorded | 18163 | 0 | Then Haggai, the messenger of the Lord, spoke to the people with the Lord’s message, “ I am with you, **declares** the Lord.” |
| Hag 2:4 | declares | HNcmsc | none recorded | - | 0 | Yet now be strong, O Zerubbabel, **declares** the Lord. Be strong, O Joshua, son of Jehozadak, the high priest. Be strong, all you people of the land, declares the Lord. Work, for I am with you, declares the Lord of hosts, |
| Hag 2:4 | declares | HNcmsc | none recorded | - | 0 | Yet now be strong, O Zerubbabel, **declares** the Lord. Be strong, O Joshua, son of Jehozadak, the high priest. Be strong, all you people of the land, declares the Lord. Work, for I am with you, declares the Lord of hosts, |
| Hag 2:4 | declares | HNcmsc | none recorded | - | 0 | Yet now be strong, O Zerubbabel, **declares** the Lord. Be strong, O Joshua, son of Jehozadak, the high priest. Be strong, all you people of the land, declares the Lord. Work, for I am with you, declares the Lord of hosts, |
| Hag 2:8 | declares | HNcmsc | none recorded | - | 0 | The silver is mine, and the gold is mine, **declares** the Lord of hosts. |
| Hag 2:14 | declares | HNcmsc | none recorded | - | 0 | Then Haggai answered and said, “ So is it with this people, and with this nation before me, **declares** the Lord, and so with every work of their hands. And what they offer there is unclean. |
| Hag 2:23 | declares | HNcmsc | none recorded | - | 0 | On that day, **declares** the Lord of hosts, I will take you, O Zerubbabel my servant, the son of Shealtiel, declares the Lord, and make you like a signet ring, for I have chosen you, declares the Lord of hosts.” |
| Hag 2:23 | declares | HNcmsc | none recorded | - | 0 | On that day, **declares** the Lord of hosts, I will take you, O Zerubbabel my servant, the son of Shealtiel, declares the Lord, and make you like a signet ring, for I have chosen you, declares the Lord of hosts.” |
| Zec 1:16 | declares | HNcmsc | none recorded | - | 0 | Therefore, thus says the Lord, I have returned to Jerusalem with mercy; my house shall be built in it, **declares** the Lord of hosts, and the measuring line shall be stretched out over Jerusalem. |
| Zec 2:6 | declares | HNcmsc | none recorded | - | 0 | Up! Up! Flee from the land of the north, **declares** the Lord. For I have spread you abroad as the four winds of the heavens, declares the Lord. |
| Zec 2:10 | declares | HNcmsc | none recorded | - | 0 | Sing and rejoice, O daughter of Zion, for behold, I come and I will dwell in your midst, **declares** the Lord. |
| Zec 3:9 | declares | HNcmsc | none recorded | - | 0 | For behold, on the stone that I have set before Joshua, on a single stone with seven eyes, I will engrave its inscription, **declares** the Lord of hosts, and I will remove the iniquity of this land in a single day. |
| Zec 3:10 | declares | HNcmsc | none recorded | - | 0 | In that day, **declares** the Lord of hosts, every one of you will invite his neighbor to come under his vine and under his fig tree.” |
| Zec 5:4 | declares | HNcmsc | none recorded | - | 0 | I will send it out, **declares** the Lord of hosts, and it shall enter the house of the thief, and the house of him who swears falsely by my name. And it shall remain in his house and consume it, both timber and stones.” |
| Zec 8:6 | declares | HNcmsc | none recorded | - | 0 | Thus says the Lord of hosts: If it is marvelous in the sight of the remnant of this people in those days, should it also be marvelous in my sight, **declares** the Lord of hosts? |
| Zec 8:17 | declares | HNcmsc | none recorded | - | 0 | do not devise evil in your hearts against one another, and love no false oath, for all these things I hate, **declares** the Lord.” |
| Zec 10:12 | declares | HNcmsc | none recorded | - | 0 | I will make them strong in the Lord, and they shall walk in his name,” **declares** the Lord. |
| Zec 11:6 | declares | HNcmsc | none recorded | - | 0 | For I will no longer have pity on the inhabitants of this land, **declares** the Lord. Behold, I will cause each of them to fall into the hand of his neighbor, and each into the hand of his king, and they shall crush the land, and I will deliver none from their hand.” |
| Zec 12:1 | declares | HNcmsc | none recorded | - | 0 | The oracle of the word of the Lord concerning Israel: Thus **declares** the Lord, who stretched out the heavens and founded the earth and formed the spirit of man within him: |
| Zec 12:4 | declares | HNcmsc | none recorded | - | 0 | On that day, **declares** the Lord, I will strike every horse with panic, and its rider with madness. But for the sake of the house of Judah I will keep my eyes open, when I strike every horse of the peoples with blindness. |
| Zec 13:2 | declares | HNcmsc | none recorded | - | 0 | “And on that day, **declares** the Lord of hosts, I will cut off the names of the idols from the land, so that they shall be remembered no more. And also I will remove from the land the prophets and the spirit of uncleanness. |
| Zec 13:7 | declares | HNcmsc | none recorded | 18324 | 0 | “ Awake, O sword, against my shepherd, against the man who stands next to me,” **declares** the Lord of hosts. “ Strike the shepherd, and the sheep will be scattered; I will turn my hand against the little ones. |
| Zec 13:8 | declares | HNcmsc | none recorded | - | 0 | In the whole land, **declares** the Lord, two thirds shall be cut off and perish, and one third shall be left alive. |
| Mal 1:2 | declares | HNcmsc | none recorded | - | 0 | “I have loved you,” says the Lord. But you say, “ How have you loved us?” “Is not Esau Jacob’s brother?” **declares** the Lord. “Yet I have loved Jacob |

### 3.2 H5012 נָבָא na.va "to prophesy": 101 own occurrences in 90 verses

- **Meaning as stored:** Hebrew; native word נָבָא, transliteration na.va; STEP gloss "to prophesy"; sense head "to prophesy" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5012):** to prophesy.
- **Related terms (4):** H5013 ne.va "to prophesy"; H5016 ne.vu.ah "prophecy"; H5030 na.vi "prophet"; H5031 ne.vi.ah "prophetess".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (heuristic).
- **Counts, three measures as stored:** STEP token count 115; verses STEP attests 0; verse_lexical rows the parse found 115.

- **Carried by the member words:** prophesy (51), prophesied (30), prophesying (20).
- **Engagement of these occurrences:** none recorded 101.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Num 11:25 | prophesied | HVtw3mp | none recorded | 16021, 16263, 16966 | 0 | Then the Lord came down in the cloud and spoke to him, and took some of the Spirit that was on him and put it on the seventy elders. And as soon as the Spirit rested on them, they **prophesied**. But they did not continue doing it. |
| Num 11:26 | prophesied | HVtw3mp | none recorded | 16021, 16966 | 0 | Now two men remained in the camp, one named Eldad, and the other named Medad, and the Spirit rested on them. They were among those registered, but they had not gone out to the tent, and so they **prophesied** in the camp. |
| 1Sa 10:10 | prophesied | HVtw3ms | none recorded | 16021 | 0 | When they came to Gibeah, behold, a group of prophets met him, and the Spirit of God rushed upon him, and he **prophesied** among them. |
| 1Sa 10:11 | prophesied | HVNrmsa | none recorded | - | 0 | And when all who knew him previously saw how he **prophesied** with the prophets, the people said to one another, “ What has come over the son of Kish? Is Saul also among the prophets?” |
| 1Sa 19:20 | prophesied | HVtw3mp | none recorded | 16021 | 0 | Then Saul sent messengers to take David, and when they saw the company of the prophets prophesying, and Samuel standing as head over them, the Spirit of God came upon the messengers of Saul, and they also **prophesied**. |
| 1Sa 19:21 | prophesied | HVtw3mp | none recorded | - | 0 | When it was told Saul, he sent other messengers, and they also **prophesied**. And Saul sent messengers again the third time, and they also prophesied. |
| 1Sa 19:21 | prophesied | HVtw3mp | none recorded | - | 0 | When it was told Saul, he sent other messengers, and they also **prophesied**. And Saul sent messengers again the third time, and they also prophesied. |
| 1Sa 19:23 | prophesied | HVtw3ms | none recorded | 16021 | 0 | And he went there to Naioth in Ramah. And the Spirit of God came upon him also, and as he went he **prophesied** until he came to Naioth in Ramah. |
| 1Sa 19:24 | prophesied | HVtw3ms | none recorded | - | 0 | And he too stripped off his clothes, and he too **prophesied** before Samuel and lay naked all that day and all that night. Thus it is said, “Is Saul also among the prophets?” |
| 1Ki 22:12 | prophesied | HVNrmpa | none recorded | - | 0 | And all the prophets **prophesied** so and said, “Go up to Ramoth-gilead and triumph; the Lord will give it into the hand of the king.” |
| 1Ch 25:1 | prophesied | HVNrmpa | none recorded | - | 0 | David and the chiefs of the service also set apart for the service the sons of Asaph, and of Heman, and of Jeduthun, who **prophesied** with lyres, with harps, and with cymbals. The list of those who did the work and of their duties was: |
| 1Ch 25:2 | prophesied | HVNrmsa | none recorded | - | 0 | Of the sons of Asaph: Zaccur, Joseph, Nethaniah, and Asharelah, sons of Asaph, under the direction of Asaph, who **prophesied** under the direction of the king. |
| 1Ch 25:3 | prophesied | HVNrmsa | none recorded | - | 0 | Of Jeduthun, the sons of Jeduthun: Gedaliah, Zeri, Jeshaiah, Shimei, Hashabiah, and Mattithiah, six, under the direction of their father Jeduthun, who **prophesied** with the lyre in thanksgiving and praise to the Lord. |
| 2Ch 18:11 | prophesied | HVNrmpa | none recorded | - | 0 | And all the prophets **prophesied** so and said, “Go up to Ramoth-gilead and triumph. The Lord will give it into the hand of the king.” |
| 2Ch 20:37 | prophesied | HVtw3ms | none recorded | - | 0 | Then Eliezer the son of Dodavahu of Mareshah **prophesied** against Jehoshaphat, saying, “Because you have joined with Ahaziah, the Lord will destroy what you have made.” And the ships were wrecked and were not able to go to Tarshish. |
| Jer 2:8 | prophesied | HVNp3cp | none recorded | - | 0 | The priests did not say, ‘ Where is the Lord?’ Those who handle the law did not know me; the shepherds transgressed against me; the prophets **prophesied** by Baal and went after things that do not profit. |
| Jer 20:6 | prophesied | HVNp2ms | none recorded | - | 0 | And you, Pashhur, and all who dwell in your house, shall go into captivity. To Babylon you shall go, and there you shall die, and there you shall be buried, you and all your friends, to whom you have **prophesied** falsely.” |
| Jer 23:13 | prophesied | HVtp3cp | none recorded | - | 0 | In the prophets of Samaria I saw an unsavory thing: they **prophesied** by Baal and led my people Israel astray. |
| Jer 26:9 | prophesied | HVNp2ms | none recorded | - | 0 | Why have you **prophesied** in the name of the Lord, saying, ‘ This house shall be like Shiloh, and this city shall be desolate, without inhabitant ’?” And all the people gathered around Jeremiah in the house of the Lord. |
| Jer 26:11 | prophesied | HVNp3ms | none recorded | - | 0 | Then the priests and the prophets said to the officials and to all the people, “ This man deserves the sentence of death, because he has **prophesied** against this city, as you have heard with your own ears.” |
| Jer 26:20 | prophesied | HVNw3ms | none recorded | - | 0 | There was another man who **prophesied** in the name of the Lord, Uriah the son of Shemaiah from Kiriath-jearim. He prophesied against this city and against this land in words like those of Jeremiah. |
| Jer 28:6 | prophesied | HVNp2ms | none recorded | - | 0 | and the prophet Jeremiah said, “ Amen! May the Lord do so; may the Lord make the words that you have **prophesied** come true, and bring back to this place from Babylon the vessels of the house of the Lord, and all the exiles. |
| Jer 28:8 | prophesied | HVNw3mp | none recorded | - | 0 | The prophets who preceded you and me from ancient times **prophesied** war, famine, and pestilence against many countries and great kingdoms. |
| Jer 29:31 | prophesied | HVNp3ms | none recorded | - | 0 | “ Send to all the exiles, saying, ‘ Thus says the Lord concerning Shemaiah of Nehelam: Because Shemaiah had **prophesied** to you when I did not send him, and has made you trust in a lie, |
| Jer 37:19 | prophesied | HVNp3cp | none recorded | - | 0 | Where are your prophets who **prophesied** to you, saying, ‘The king of Babylon will not come against you and against this land ’? |
| Eze 13:16 | prophesied | HVNrmpa | none recorded | - | 0 | the prophets of Israel who **prophesied** concerning Jerusalem and saw visions of peace for her, when there was no peace, declares the Lord God. |
| Eze 37:7 | prophesied | HVNq1cs | none recorded | - | 0 | So I **prophesied** as I was commanded. And as I prophesied, there was a sound, and behold, a rattling, and the bones came together, bone to its bone. |
| Eze 37:7 | prophesied | HVNcc | none recorded | - | 0 | So I **prophesied** as I was commanded. And as I prophesied, there was a sound, and behold, a rattling, and the bones came together, bone to its bone. |
| Eze 37:10 | prophesied | HVtq1cs | none recorded | - | 0 | So I **prophesied** as he commanded me, and the breath came into them, and they lived and stood on their feet, an exceedingly great army. |
| Eze 38:17 | prophesied | HVNrmpa | none recorded | - | 0 | “ Thus says the Lord God: Are you he of whom I spoke in former days by my servants the prophets of Israel, who in those days **prophesied** for years that I would bring you against them? |
| 1Sa 10:6 | prophesy | HVtq2ms | none recorded | 16022 | 0 | Then the Spirit of the Lord will rush upon you, and you will **prophesy** with them and be turned into another man. |
| 1Ki 22:18 | prophesy | HVti3ms | none recorded | - | 0 | And the king of Israel said to Jehoshaphat, “Did I not tell you that he would not **prophesy** good concerning me, but evil?” |
| 2Ch 18:17 | prophesy | HVti3ms | none recorded | - | 0 | And the king of Israel said to Jehoshaphat, “Did I not tell you that he would not **prophesy** good concerning me, but evil?” |
| Jer 5:31 | prophesy | HVNp3cp | none recorded | - | 0 | the prophets **prophesy** falsely, and the priests rule at their direction; my people love to have it so, but what will you do when the end comes? |
| Jer 11:21 | prophesy | HVNi2ms | none recorded | - | 0 | Therefore thus says the Lord concerning the men of Anathoth, who seek your life, and say, “Do not **prophesy** in the name of the Lord, or you will die by our hand ”— |
| Jer 14:15 | prophesy | HVNrmpa | none recorded | - | 0 | Therefore thus says the Lord concerning the prophets who **prophesy** in my name although I did not send them, and who say, ‘ Sword and famine shall not come upon this land ’: By sword and famine those prophets shall be consumed. |
| Jer 14:16 | prophesy | HVNrmpa | none recorded | - | 0 | And the people to whom they **prophesy** shall be cast out in the streets of Jerusalem, victims of famine and sword, with none to bury them — them, their wives, their sons, and their daughters. For I will pour out their evil upon them. |
| Jer 19:14 | prophesy | HVNcc | none recorded | - | 0 | Then Jeremiah came from Topheth, where the Lord had sent him to **prophesy**, and he stood in the court of the Lord’s house and said to all the people: |
| Jer 23:16 | prophesy | HVNrmpa | none recorded | 16020, 17240 | 0 | Thus says the Lord of hosts: “Do not listen to the words of the prophets who **prophesy** to you, filling you with vain hopes. They speak visions of their own minds, not from the mouth of the Lord. |
| Jer 23:25 | prophesy | HVNrmpa | none recorded | - | 0 | I have heard what the prophets have said who **prophesy** lies in my name, saying, ‘I have dreamed, I have dreamed!’ |
| Jer 23:26 | prophesy | HVNrmpc | none recorded | 16020, 17240 | 0 | How long shall there be lies in the heart of the prophets who **prophesy** lies, and who prophesy the deceit of their own heart, |
| Jer 23:32 | prophesy | HVNrmpc | none recorded | - | 0 | Behold, I am against those who **prophesy** lying dreams, declares the Lord, and who tell them and lead my people astray by their lies and their recklessness, when I did not send them or charge them. So they do not profit this people at all, declares the Lord. |
| Jer 25:30 | prophesy | HVNi2ms | none recorded | - | 0 | “ You, therefore, shall **prophesy** against them all these words, and say to them: “‘The Lord will roar from on high, and from his holy habitation utter his voice; he will roar mightily against his fold, and shout, like those who tread grapes, against all the inhabitants of the earth. |
| Jer 26:12 | prophesy | HVNcc | none recorded | - | 0 | Then Jeremiah spoke to all the officials and all the people, saying, “The Lord sent me to **prophesy** against this house and this city all the words you have heard. |
| Jer 32:3 | prophesy | HVNrmsa | none recorded | - | 0 | For Zedekiah king of Judah had imprisoned him, saying, “ Why do you **prophesy** and say, ‘ Thus says the Lord: Behold, I am giving this city into the hand of the king of Babylon, and he shall capture it; |
| Eze 4:7 | prophesy | HVNq2ms | none recorded | - | 0 | And you shall set your face toward the siege of Jerusalem, with your arm bared, and you shall **prophesy** against the city. |
| Eze 6:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face toward the mountains of Israel, and **prophesy** against them, |
| Eze 11:4 | prophesy | HVNv2ms | none recorded | - | 0 | Therefore **prophesy** against them; prophesy, O son of man.” |
| Eze 11:4 | prophesy | HVNv2ms | none recorded | - | 0 | Therefore **prophesy** against them; prophesy, O son of man.” |
| Eze 13:2 | prophesy | HVNv2ms | none recorded | 16020, 17240 | 0 | “ Son of man, **prophesy** against the prophets of Israel, who are prophesying, and say to those who prophesy from their own hearts: ‘ Hear the word of the Lord!’ |
| Eze 13:17 | prophesy | HVtrfpa | none recorded | 14698, 14946, 16020, 17240 | 0 | “And you, son of man, set your face against the daughters of your people, who **prophesy** out of their own hearts. Prophesy against them |
| Eze 13:17 | prophesy | HVNv2ms | none recorded | 14698, 14946, 16020, 17240 | 0 | “And you, son of man, set your face against the daughters of your people, who **prophesy** out of their own hearts. Prophesy against them |
| Eze 20:46 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face toward the southland; preach against the south, and **prophesy** against the forest land in the Negeb. |
| Eze 21:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face toward Jerusalem and preach against the sanctuaries. **Prophesy** against the land of Israel |
| Eze 21:9 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, **prophesy** and say, Thus says the Lord, say: “A sword, a sword is sharpened and also polished, |
| Eze 21:14 | prophesy | HVNv2ms | none recorded | - | 0 | “As for you, son of man, **prophesy**. Clap your hands and let the sword come down twice, yes, three times, the sword for those to be slain. It is the sword for the great slaughter, which surrounds them, |
| Eze 21:28 | prophesy | HVNv2ms | none recorded | - | 0 | “And you, son of man, **prophesy**, and say, Thus says the Lord God concerning the Ammonites and concerning their reproach; say, A sword, a sword is drawn for the slaughter. It is polished to consume and to flash like lightning — |
| Eze 25:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face toward the Ammonites and **prophesy** against them. |
| Eze 28:21 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face toward Sidon, and **prophesy** against her |
| Eze 29:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face against Pharaoh king of Egypt, and **prophesy** against him and against all Egypt; |
| Eze 30:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, **prophesy**, and say, Thus says the Lord God: “ Wail, ‘ Alas for the day!’ |
| Eze 34:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, **prophesy** against the shepherds of Israel; prophesy, and say to them, even to the shepherds, Thus says the Lord God: Ah, shepherds of Israel who have been feeding yourselves! Should not shepherds feed the sheep? |
| Eze 34:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, **prophesy** against the shepherds of Israel; prophesy, and say to them, even to the shepherds, Thus says the Lord God: Ah, shepherds of Israel who have been feeding yourselves! Should not shepherds feed the sheep? |
| Eze 35:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face against Mount Seir, and **prophesy** against it, |
| Eze 36:1 | prophesy | HVNv2ms | none recorded | - | 0 | “And you, son of man, **prophesy** to the mountains of Israel, and say, O mountains of Israel, hear the word of the Lord. |
| Eze 36:3 | prophesy | HVNv2ms | none recorded | - | 0 | therefore **prophesy**, and say, Thus says the Lord God: Precisely because they made you desolate and crushed you from all sides, so that you became the possession of the rest of the nations, and you became the talk and evil gossip of the people, |
| Eze 36:6 | prophesy | HVNv2ms | none recorded | - | 0 | Therefore **prophesy** concerning the land of Israel, and say to the mountains and hills, to the ravines and valleys, Thus says the Lord God: Behold, I have spoken in my jealous wrath, because you have suffered the reproach of the nations. |
| Eze 37:4 | prophesy | HVNv2ms | none recorded | - | 0 | Then he said to me, “ **Prophesy** over these bones, and say to them, O dry bones, hear the word of the Lord. |
| Eze 37:9 | prophesy | HVNv2ms | none recorded | 16025 | 0 | Then he said to me, “ **Prophesy** to the breath; prophesy, son of man, and say to the breath, Thus says the Lord God: Come from the four winds, O breath, and breathe on these slain, that they may live.” |
| Eze 37:9 | prophesy | HVNv2ms | none recorded | 16025 | 0 | Then he said to me, “ **Prophesy** to the breath; prophesy, son of man, and say to the breath, Thus says the Lord God: Come from the four winds, O breath, and breathe on these slain, that they may live.” |
| Eze 37:12 | prophesy | HVNv2ms | none recorded | - | 0 | Therefore **prophesy**, and say to them, Thus says the Lord God: Behold, I will open your graves and raise you from your graves, O my people. And I will bring you into the land of Israel. |
| Eze 38:2 | prophesy | HVNv2ms | none recorded | - | 0 | “ Son of man, set your face toward Gog, of the land of Magog, the chief prince of Meshech and Tubal, and **prophesy** against him |
| Eze 38:14 | prophesy | HVNv2ms | none recorded | - | 0 | “ Therefore, son of man, **prophesy**, and say to Gog, Thus says the Lord God: On that day when my people Israel are dwelling securely, will you not know it? |
| Eze 39:1 | prophesy | HVNv2ms | none recorded | - | 0 | “And you, son of man, **prophesy** against Gog and say, Thus says the Lord God: Behold, I am against you, O Gog, chief prince of Meshech and Tubal. |
| Joe 2:28 | prophesy | HVNq3cp | none recorded | 16021 | 0 | “And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall **prophesy**, your old men shall dream dreams, and your young men shall see visions. |
| Amo 2:12 | prophesy | HVNi2mp | none recorded | - | 0 | “But you made the Nazirites drink wine, and commanded the prophets, saying, ‘You shall not **prophesy**.’ |
| Amo 3:8 | prophesy | HVNi3ms | none recorded | - | 0 | The lion has roared; who will not fear? The Lord God has spoken; who can but **prophesy**?” |
| Amo 7:12 | prophesy | HVNi2ms | none recorded | - | 0 | And Amaziah said to Amos, “O seer, go, flee away to the land of Judah, and eat bread there, and **prophesy** there, |
| Amo 7:13 | prophesy | HVNcc | none recorded | - | 0 | but never again **prophesy** at Bethel, for it is the king’s sanctuary, and it is a temple of the kingdom.” |
| Amo 7:15 | prophesy | HVNv2ms | none recorded | - | 0 | But the Lord took me from following the flock, and the Lord said to me, ‘ Go, **prophesy** to my people Israel.’ |
| Amo 7:16 | prophesy | HVNi2ms | none recorded | - | 0 | Now therefore hear the word of the Lord. “ You say, ‘Do not **prophesy** against Israel, and do not preach against the house of Isaac.’ |
| Num 11:27 | prophesying | HVtrmpa | none recorded | - | 0 | And a young man ran and told Moses, “ Eldad and Medad are **prophesying** in the camp.” |
| 1Sa 10:5 | prophesying | HVtrmpa | none recorded | - | 0 | After that you shall come to Gibeath-elohim, where there is a garrison of the Philistines. And there, as soon as you come to the city, you will meet a group of prophets coming down from the high place with harp, tambourine, flute, and lyre before them, **prophesying**. |
| 1Sa 10:13 | prophesying | HVtcc | none recorded | - | 0 | When he had finished **prophesying**, he came to the high place. |
| 1Sa 19:20 | prophesying | HVNrmpa | none recorded | - | 0 | Then Saul sent messengers to take David, and when they saw the company of the prophets **prophesying**, and Samuel standing as head over them, the Spirit of God came upon the messengers of Saul, and they also prophesied. |
| 1Ki 22:10 | prophesying | HVtrmpa | none recorded | - | 0 | Now the king of Israel and Jehoshaphat the king of Judah were sitting on their thrones, arrayed in their robes, at the threshing floor at the entrance of the gate of Samaria, and all the prophets were **prophesying** before them. |
| 2Ch 18:9 | prophesying | HVtrmpa | none recorded | - | 0 | Now the king of Israel and Jehoshaphat the king of Judah were sitting on their thrones, arrayed in their robes. And they were sitting at the threshing floor at the entrance of the gate of Samaria, and all the prophets were **prophesying** before them. |
| Jer 14:14 | prophesying | HVNrmpa | none recorded | - | 0 | And the Lord said to me: “The prophets are **prophesying** lies in my name. I did not send them, nor did I command them or speak to them. They are prophesying to you a lying vision, worthless divination, and the deceit of their own minds. |
| Jer 14:14 | prophesying | HVtrmpa | none recorded | - | 0 | And the Lord said to me: “The prophets are **prophesying** lies in my name. I did not send them, nor did I command them or speak to them. They are prophesying to you a lying vision, worthless divination, and the deceit of their own minds. |
| Jer 20:1 | prophesying | HVNrmsa | none recorded | - | 0 | Now Pashhur the priest, the son of Immer, who was chief officer in the house of the Lord, heard Jeremiah **prophesying** these things. |
| Jer 27:10 | prophesying | HVNrmpa | none recorded | - | 0 | For it is a lie that they are **prophesying** to you, with the result that you will be removed far from your land, and I will drive you out, and you will perish. |
| Jer 27:14 | prophesying | HVNrmpa | none recorded | - | 0 | Do not listen to the words of the prophets who are saying to you, ‘You shall not serve the king of Babylon,’ for it is a lie that they are **prophesying** to you. |
| Jer 27:15 | prophesying | HVNrmpa | none recorded | - | 0 | I have not sent them, declares the Lord, but they are **prophesying** falsely in my name, with the result that I will drive you out and you will perish, you and the prophets who are prophesying to you.” |
| Jer 27:15 | prophesying | HVNrmpa | none recorded | - | 0 | I have not sent them, declares the Lord, but they are **prophesying** falsely in my name, with the result that I will drive you out and you will perish, you and the prophets who are prophesying to you.” |
| Jer 27:16 | prophesying | HVNrmpa | none recorded | - | 0 | Then I spoke to the priests and to all this people, saying, “ Thus says the Lord: Do not listen to the words of your prophets who are **prophesying** to you, saying, ‘ Behold, the vessels of the Lord’s house will now shortly be brought back from Babylon,’ for it is a lie that they are prophesying to you. |
| Jer 27:16 | prophesying | HVNrmpa | none recorded | - | 0 | Then I spoke to the priests and to all this people, saying, “ Thus says the Lord: Do not listen to the words of your prophets who are **prophesying** to you, saying, ‘ Behold, the vessels of the Lord’s house will now shortly be brought back from Babylon,’ for it is a lie that they are prophesying to you. |
| Jer 29:9 | prophesying | HVNrmpa | none recorded | - | 0 | for it is a lie that they are **prophesying** to you in my name; I did not send them, declares the Lord. |
| Jer 29:21 | prophesying | HVNrmpa | none recorded | - | 0 | ‘ Thus says the Lord of hosts, the God of Israel, concerning Ahab the son of Kolaiah and Zedekiah the son of Maaseiah, who are **prophesying** a lie to you in my name: Behold, I will deliver them into the hand of Nebuchadnezzar king of Babylon, and he shall strike them down before your eyes. |
| Jer 29:27 | prophesying | HVtrmsa | none recorded | - | 0 | Now why have you not rebuked Jeremiah of Anathoth who is **prophesying** to you? |
| Eze 11:13 | prophesying | HVNcc | none recorded | - | 0 | And it came to pass, while I was **prophesying**, that Pelatiah the son of Benaiah died. Then I fell down on my face and cried out with a loud voice and said, “ Ah, Lord God! Will you make a full end of the remnant of Israel?” |
| Eze 13:2 | prophesying | HVNrmpa | none recorded | - | 0 | “ Son of man, prophesy against the prophets of Israel, who are **prophesying**, and say to those who prophesy from their own hearts: ‘ Hear the word of the Lord!’ |

### 3.3 H5046 נָגַד na.gad "to tell": 63 own occurrences in 60 verses

- **Meaning as stored:** Hebrew; native word נָגַד, transliteration na.gad; STEP gloss "to tell"; sense head "to tell" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5046):** to be conspicuous, tell, make known.
- **Related terms (3):** H5047 ne.gad "to flow"; H5048 ne.ged "before"; H5057 na.gid "leader".
- **Clusters (cluster_strong):** M65 Speech & Tongue (heuristic).
- **Counts, three measures as stored:** STEP token count 374; verses STEP attests 345; verse_lexical rows the parse found 371.

- **Carried by the member words:** declare (36), declared (11), declares (7), proclaim (5), announce (2), declaring (1), proclaims (1).
- **Engagement of these occurrences:** none recorded 63.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 21:6 | announce | HVhi3ms | none recorded | - | 0 | For thus the Lord said to me: “ Go, set a watchman; let him **announce** what he sees. |
| Isa 21:10 | announce | HVhp1cs | none recorded | - | 0 | O my threshed and winnowed one, what I have heard from the Lord of hosts, the God of Israel, I **announce** to you. |
| Deu 17:9 | declare | HVhq3cp | none recorded | - | 0 | And you shall come to the Levitical priests and to the judge who is in office in those days, and you shall consult them, and they shall **declare** to you the decision. |
| Deu 17:10 | declare | HVhi3mp | none recorded | - | 0 | Then you shall do according to what they **declare** to you from that place that the Lord will choose. And you shall be careful to do according to all that they direct you. |
| Deu 26:3 | declare | HVhp1cs | none recorded | - | 0 | And you shall go to the priest who is in office at that time and say to him, ‘I **declare** today to the Lord your God that I have come into the land that the Lord swore to our fathers to give us.’ |
| Deu 30:18 | declare | HVhp1cs | none recorded | - | 0 | I **declare** to you today, that you shall surely perish. You shall not live long in the land that you are going over the Jordan to enter and possess. |
| 1Sa 3:13 | declare | HVhq1cs | none recorded | - | 0 | And I **declare** to him that I am about to punish his house forever, for the iniquity that he knew, because his sons were blaspheming God, and he did not restrain them. |
| 1Ch 17:10 | declare | HVhw1cs | none recorded | - | 0 | from the time that I appointed judges over my people Israel. And I will subdue all your enemies. Moreover, I **declare** to you that the Lord will build you a house. |
| Job 33:23 | declare | HVhcc | none recorded | 15236 | 0 | If there be for him an angel, a mediator, one of the thousand, to **declare** to man what is right for him, |
| Job 38:18 | declare | HVhv2ms | none recorded | - | 0 | Have you comprehended the expanse of the earth? **Declare**, if you know all this. |
| Psa 50:6 | declare | HVhw3mp | none recorded | - | 0 | The heavens **declare** his righteousness, for God himself is judge! Selah |
| Psa 51:15 | declare | HVhi3ms | none recorded | - | 0 | O Lord, open my lips, and my mouth will **declare** your praise. |
| Psa 75:9 | declare | HVhi1cs | none recorded | - | 0 | But I will **declare** it forever; I will sing praises to the God of Jacob. |
| Psa 92:2 | declare | HVhcc | none recorded | - | 0 | to **declare** your steadfast love in the morning, and your faithfulness by night, |
| Psa 92:15 | declare | HVhcc | none recorded | - | 0 | to **declare** that the Lord is upright; he is my rock, and there is no unrighteousness in him. |
| Psa 145:4 | declare | HVhi3mp | none recorded | - | 0 | One generation shall commend your works to another, and shall **declare** your mighty acts. |
| Isa 42:9 | declare | HVhrmsa | none recorded | - | 0 | Behold, the former things have come to pass, and new things I now **declare**; before they spring forth I tell you of them.” |
| Isa 42:12 | declare | HVhi3mp | none recorded | - | 0 | Let them give glory to the Lord, and **declare** his praise in the coastlands. |
| Isa 43:9 | declare | HVhi3ms | none recorded | - | 0 | All the nations gather together, and the peoples assemble. Who among them can **declare** this, and show us the former things? Let them bring their witnesses to prove them right, and let them hear and say, It is true. |
| Isa 44:7 | declare | HVhu3ms | none recorded | - | 0 | Who is like me? Let him proclaim it. Let him **declare** and set it before me, since I appointed an ancient people. Let them declare what is to come, and what will happen. |
| Isa 44:7 | declare | HVhi3mp | none recorded | - | 0 | Who is like me? Let him proclaim it. Let him **declare** and set it before me, since I appointed an ancient people. Let them declare what is to come, and what will happen. |
| Isa 45:19 | declare | HVhrmsa | none recorded | - | 0 | I did not speak in secret, in a land of darkness; I did not say to the offspring of Jacob, ‘ Seek me in vain.’ I the Lord speak the truth; I **declare** what is right. |
| Isa 45:21 | declare | HVhv2mp | none recorded | - | 0 | **Declare** and present your case; let them take counsel together! Who told this long ago? Who declared it of old? Was it not I, the Lord? And there is no other god besides me, a righteous God and a Savior; there is none besides me. |
| Isa 48:6 | declare | HVhi2mp | none recorded | - | 0 | “You have heard; now see all this; and will you not **declare** it? From this time forth I announce to you new things, hidden things that you have not known. |
| Isa 48:20 | declare | HVhv2mp | none recorded | - | 0 | Go out from Babylon, flee from Chaldea, **declare** this with a shout of joy, proclaim it, send it out to the end of the earth; say, “The Lord has redeemed his servant Jacob!” |
| Isa 57:12 | declare | HVhi1cs | none recorded | - | 0 | I will **declare** your righteousness and your deeds, but they will not profit you. |
| Isa 58:1 | declare | HVhv2ms | none recorded | - | 0 | “ Cry aloud; do not hold back; lift up your voice like a trumpet; **declare** to my people their transgression, to the house of Jacob their sins. |
| Isa 66:19 | declare | HVhq3cp | none recorded | - | 0 | and I will set a sign among them. And from them I will send survivors to the nations, to Tarshish, Pul, and Lud, who draw the bow, to Tubal and Javan, to the coastlands far away, that have not heard my fame or seen my glory. And they shall **declare** my glory among the nations. |
| Jer 4:5 | declare | HVhv2mp | none recorded | - | 0 | **Declare** in Judah, and proclaim in Jerusalem, and say, “ Blow the trumpet through the land; cry aloud and say, ‘ Assemble, and let us go into the fortified cities!’ |
| Jer 5:20 | declare | HVhv2mp | none recorded | - | 0 | **Declare** this in the house of Jacob; proclaim it in Judah: |
| Jer 31:10 | declare | HVhv2mp | none recorded | - | 0 | “ Hear the word of the Lord, O nations, and **declare** it in the coastlands far away; say, ‘He who scattered Israel will gather him, and will keep him as a shepherd keeps his flock.’ |
| Jer 46:14 | declare | HVhv2mp | none recorded | - | 0 | “ **Declare** in Egypt, and proclaim in Migdol; proclaim in Memphis and Tahpanhes; say, ‘ Stand ready and be prepared, for the sword shall devour around you.’ |
| Jer 50:2 | declare | HVhv2mp | none recorded | - | 0 | “ **Declare** among the nations and proclaim, set up a banner and proclaim, conceal it not, and say: ‘ Babylon is taken, Bel is put to shame, Merodach is dismayed. Her images are put to shame, her idols are dismayed.’ |
| Jer 50:28 | declare | HVhcc | none recorded | - | 0 | “A voice! They flee and escape from the land of Babylon, to **declare** in Zion the vengeance of the Lord our God, vengeance for his temple. |
| Eze 23:36 | declare | HVhv2ms | none recorded | - | 0 | The Lord said to me: “ Son of man, will you judge Oholah and Oholibah? **Declare** to them their abominations. |
| Eze 40:4 | declare | HVhv2ms | none recorded | - | 0 | And the man said to me, “ Son of man, look with your eyes, and hear with your ears, and set your heart upon all that I shall show you, for you were brought here in order that I might show it to you. **Declare** all that you see to the house of Israel.” |
| Mic 3:8 | declare | HVhcc | none recorded | 16517, 16583 | 0 | But as for me, I am filled with power, with the Spirit of the Lord, and with justice and might, to **declare** to Jacob his transgression and to Israel his sin. |
| Zec 9:12 | declare | HVhrmsa | none recorded | - | 0 | Return to your stronghold, O prisoners of hope; today I **declare** that I will restore to you double. |
| Deu 4:13 | declared | HVhw3ms | none recorded | - | 0 | And he **declared** to you his covenant, which he commanded you to perform, that is, the Ten Commandments, and he wrote them on two tablets of stone. |
| 1Sa 24:18 | declared | HVhp2ms | none recorded | - | 0 | And you have **declared** this day how you have dealt well with me, in that you did not kill me when the Lord put me into your hands. |
| Isa 41:26 | declared | HVhp3ms | none recorded | - | 0 | Who **declared** it from the beginning, that we might know, and beforehand, that we might say, “He is right ”? There was none who declared it, none who proclaimed, none who heard your words. |
| Isa 41:26 | declared | HVhrmsa | none recorded | - | 0 | Who **declared** it from the beginning, that we might know, and beforehand, that we might say, “He is right ”? There was none who declared it, none who proclaimed, none who heard your words. |
| Isa 43:12 | declared | HVhp1cs | none recorded | - | 0 | I **declared** and saved and proclaimed, when there was no strange god among you; and you are my witnesses,” declares the Lord, “and I am God. |
| Isa 44:8 | declared | HVhp1cs | none recorded | 19609 | 0 | Fear not, nor be afraid; have I not told you from of old and **declared** it? And you are my witnesses! Is there a God besides me? There is no Rock; I know not any.” |
| Isa 45:21 | declared | HVhp3ms | none recorded | - | 0 | Declare and present your case; let them take counsel together! Who told this long ago? Who **declared** it of old? Was it not I, the Lord? And there is no other god besides me, a righteous God and a Savior; there is none besides me. |
| Isa 48:3 | declared | HVhp1cs | none recorded | - | 0 | “The former things I **declared** of old; they went out from my mouth, and I announced them; then suddenly I did them, and they came to pass. |
| Isa 48:5 | declared | HVhw1cs | none recorded | - | 0 | I **declared** them to you from of old, before they came to pass I announced them to you, lest you should say, ‘My idol did them, my carved image and my metal image commanded them.’ |
| Isa 48:14 | declared | HVhp3ms | none recorded | 17582 | 0 | “ Assemble, all of you, and listen! Who among them has **declared** these things? The Lord loves him; he shall perform his purpose on Babylon, and his arm shall be against the Chaldeans. |
| Jer 42:21 | declared | HVhw1cs | none recorded | 14719 | 0 | And I have this day **declared** it to you, but you have not obeyed the voice of the Lord your God in anything that he sent me to tell you. |
| 2Sa 7:11 | declares | HVhq3ms | none recorded | - | 0 | from the time that I appointed judges over my people Israel. And I will give you rest from all your enemies. Moreover, the Lord **declares** to you that the Lord will make you a house. |
| Job 21:31 | declares | HVhi3ms | none recorded | - | 0 | Who **declares** his way to his face, and who repays him for what he has done? |
| Job 36:9 | declares | HVhw3ms | none recorded | 20310 | 0 | then he **declares** to them their work and their transgressions, that they are behaving arrogantly. |
| Job 36:33 | declares | HVhi3ms | none recorded | - | 0 | Its crashing **declares** his presence; the cattle also declare that he rises. |
| Psa 147:19 | declares | HVhrmsa | none recorded | - | 0 | He **declares** his word to Jacob, his statutes and rules to Israel. |
| Jer 4:15 | declares | HVhrmsa | none recorded | - | 0 | For a voice **declares** from Dan and proclaims trouble from Mount Ephraim. |
| Amo 4:13 | declares | HVhrmsa | none recorded | 15965, 16775 | 0 | For behold, he who forms the mountains and creates the wind, and **declares** to man what is his thought, who makes the morning darkness, and treads on the heights of the earth — the Lord, the God of hosts, is his name! |
| Isa 46:10 | declaring | HVhrmsa | none recorded | 17521 | 0 | **declaring** the end from the beginning and from ancient times things not yet done, saying, ‘My counsel shall stand, and I will accomplish all my purpose,’ |
| Psa 22:31 | proclaim | HVhu3mp | none recorded | - | 0 | they shall come and **proclaim** his righteousness to a people yet unborn, that he has done it. |
| Psa 71:17 | proclaim | HVhi1cs | none recorded | - | 0 | O God, from my youth you have taught me, and I still **proclaim** your wondrous deeds. |
| Psa 71:18 | proclaim | HVhi1cs | none recorded | - | 0 | So even to old age and gray hairs, O God, do not forsake me, until I **proclaim** your might to another generation, your power to all those to come. |
| Psa 97:6 | proclaim | HVhp3cp | none recorded | - | 0 | The heavens **proclaim** his righteousness, and all the peoples see his glory. |
| Isa 3:9 | proclaim | HVhp3cp | none recorded | 18887, 19224 | 0 | For the look on their faces bears witness against them; they **proclaim** their sin like Sodom; they do not hide it. Woe to them! For they have brought evil on themselves. |
| Psa 19:1 | proclaims | HVhrmsa | none recorded | - | 0 | To the choirmaster. A Psalm of David. The heavens declare the glory of God, and the sky above **proclaims** his handiwork. |

### 3.4 G2784 κηρύσσω kērussō "to preach": 58 own occurrences in 57 verses

- **Meaning as stored:** Greek; native word κηρύσσω, transliteration kērussō; STEP gloss "to preach"; sense head "to preach" (the code is its own lemma).
- **Related terms (3):** G2782 kērugma "preaching"; G2783 kērux "preacher"; G4296 prokērussō "to announce".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 88; verses STEP attests 0; verse_lexical rows the parse found 60.

- **Carried by the member words:** proclaimed (18), preach (12), proclaim (10), proclaiming (10), preaching (4), preached (2), proclaims (2).
- **Engagement of these occurrences:** none recorded 58.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 4:17 | preach | V-PAN | none recorded | - | 0 | From that time Jesus began to **preach**, saying, “ Repent, for the kingdom of heaven is at hand.” |
| Mat 11:1 | preach | V-PAN | none recorded | - | 0 | When Jesus had finished instructing his twelve disciples, he went on from there to teach and **preach** in their cities. |
| Mar 1:38 | preach | V-AAS-1S | none recorded | - | 0 | And he said to them, “Let us go on to the next towns, that I may **preach** there also, for that is why I came out.” |
| Mar 3:14 | preach | V-PAN | none recorded | - | 0 | And he appointed twelve ( whom he also named apostles ) so that they might be with him and he might send them out to **preach** |
| Act 10:42 | preach | V-AAN | none recorded | - | 0 | And he commanded us to **preach** to the people and to testify that he is the one appointed by God to be judge of the living and the dead. |
| Rom 2:21 | preach | V-PAP-VSM | none recorded | - | 0 | you then who teach others, do you not teach yourself? While you **preach** against stealing, do you steal? |
| Rom 10:15 | preach | V-AAS-3P | none recorded | - | 0 | And how are they to **preach** unless they are sent? As it is written, “ How beautiful are the feet of those who preach the good news!” |
| 1Cor 1:23 | preach | V-PAI-1P | none recorded | - | 0 | but we **preach** Christ crucified, a stumbling block to Jews and folly to Gentiles, |
| 1Cor 15:11 | preach | V-PAI-1P | none recorded | - | 0 | Whether then it was I or they, so we **preach** and so you believed. |
| Gal 5:11 | preach | V-PAI-1S | none recorded | - | 0 | But if I, brothers, still **preach** circumcision, why am I still being persecuted? In that case the offense of the cross has been removed. |
| Phili 1:15 | preach | V-PAI-3P | none recorded | - | 0 | Some indeed **preach** Christ from envy and rivalry, but others from good will. |
| 2Ti 4:2 | preach | V-AAM-2S | none recorded | - | 0 | **preach** the word; be ready in season and out of season; reprove, rebuke, and exhort, with complete patience and teaching. |
| Mar 1:7 | preached | V-IAI-3S | none recorded | - | 0 | And he **preached**, saying, “ After me comes he who is mightier than I, the strap of whose sandals I am not worthy to stoop down and untie. |
| Mar 16:20 | preached | V-AAI-3P | none recorded | - | 0 | And they went out and **preached** everywhere, while the Lord worked with them and confirmed the message by accompanying signs.]] |
| Mat 3:1 | preaching | V-PAP-NSM | none recorded | - | 0 | In those days John the Baptist came **preaching** in the wilderness of Judea, |
| Mar 1:39 | preaching | V-PAP-NSM | none recorded | - | 0 | And he went throughout all Galilee, **preaching** in their synagogues and casting out demons. |
| Luk 4:44 | preaching | V-PAP-NSM | none recorded | - | 0 | And he was **preaching** in the synagogues of Judea. |
| 1Cor 9:27 | preaching | V-AAP-NSM | none recorded | - | 0 | But I discipline my body and keep it under control, lest after **preaching** to others I myself should be disqualified. |
| Mat 10:7 | proclaim | V-PAM-2P | none recorded | - | 0 | And **proclaim** as you go, saying, ‘The kingdom of heaven is at hand.’ |
| Mat 10:27 | proclaim | V-AAM-2P | none recorded | - | 0 | What I tell you in the dark, say in the light, and what you hear whispered, **proclaim** on the housetops. |
| Mar 5:20 | proclaim | V-PAN | none recorded | - | 0 | And he went away and began to **proclaim** in the Decapolis how much Jesus had done for him, and everyone marveled. |
| Mar 16:15 | proclaim | V-AAM-2P | none recorded | - | 0 | And he said to them, “ Go into all the world and **proclaim** the gospel to the whole creation. |
| Luk 4:18 | proclaim | V-AAN | none recorded | - | 0 | “The Spirit of the Lord is upon me, because he has anointed me to **proclaim** good news to the poor. He has sent me to proclaim liberty to the captives and recovering of sight to the blind, to set at liberty those who are oppressed, |
| Luk 9:2 | proclaim | V-PAN | none recorded | - | 0 | and he sent them out to **proclaim** the kingdom of God and to heal. |
| Act 15:21 | proclaim | V-PAP-APM | none recorded | - | 0 | For from ancient generations Moses has had in every city those who **proclaim** him, for he is read every Sabbath in the synagogues.” |
| Rom 10:8 | proclaim | V-PAI-1P | none recorded | - | 0 | But what does it say? “The word is near you, in your mouth and in your heart ” (that is, the word of faith that we **proclaim** ); |
| 2Cor 4:5 | proclaim | V-PAI-1P | none recorded | - | 0 | For what we **proclaim** is not ourselves, but Jesus Christ as Lord, with ourselves as your servants for Jesus ’ sake. |
| Gal 2:2 | proclaim | V-PAI-1S | none recorded | - | 0 | I went up because of a revelation and set before them ( though privately before those who seemed influential ) the gospel that I **proclaim** among the Gentiles, in order to make sure I was not running or had not run in vain. |
| Mat 24:14 | proclaimed | V-FPI-3S | none recorded | - | 0 | And this gospel of the kingdom will be **proclaimed** throughout the whole world as a testimony to all nations, and then the end will come. |
| Mat 26:13 | proclaimed | V-APS-3S | none recorded | - | 0 | Truly, I say to you, wherever this gospel is **proclaimed** in the whole world, what she has done will also be told in memory of her.” |
| Mar 6:12 | proclaimed | V-AAI-3P | none recorded | - | 0 | So they went out and **proclaimed** that people should repent. |
| Mar 7:36 | proclaimed | V-IAI-3P | none recorded | - | 0 | And Jesus charged them to tell no one. But the more he charged them, the more zealously they **proclaimed** it. |
| Mar 13:10 | proclaimed | V-APN | none recorded | - | 0 | And the gospel must first be **proclaimed** to all nations. |
| Mar 14:9 | proclaimed | V-APS-3S | none recorded | - | 0 | And truly, I say to you, wherever the gospel is **proclaimed** in the whole world, what she has done will be told in memory of her.” |
| Luk 12:3 | proclaimed | V-FPI-3S | none recorded | - | 0 | Therefore whatever you have said in the dark shall be heard in the light, and what you have whispered in private rooms shall be **proclaimed** on the housetops. |
| Luk 24:47 | proclaimed | V-APN | none recorded | - | 0 | and that repentance for the forgiveness of sins should be **proclaimed** in his name to all nations, beginning from Jerusalem. |
| Act 8:5 | proclaimed | V-IAI-3S | none recorded | - | 0 | Philip went down to the city of Samaria and **proclaimed** to them the Christ. |
| Act 9:20 | proclaimed | V-IAI-3S | none recorded | - | 0 | And immediately he **proclaimed** Jesus in the synagogues, saying, “ He is the Son of God.” |
| Act 10:37 | proclaimed | V-AAI-3S | none recorded | - | 0 | you yourselves know what happened throughout all Judea, beginning from Galilee after the baptism that John **proclaimed**: |
| 1Cor 15:12 | proclaimed | V-PPI-3S | none recorded | - | 0 | Now if Christ is **proclaimed** as raised from the dead, how can some of you say that there is no resurrection of the dead? |
| 2Cor 1:19 | proclaimed | V-APP-NSM | none recorded | - | 0 | For the Son of God, Jesus Christ, whom we **proclaimed** among you, Silvanus and Timothy and I, was not Yes and No, but in him it is always Yes. |
| 2Cor 11:4 | proclaimed | V-AAI-1P | none recorded | - | 0 | For if someone comes and proclaims another Jesus than the one we **proclaimed**, or if you receive a different spirit from the one you received, or if you accept a different gospel from the one you accepted, you put up with it readily enough. |
| Col 1:23 | proclaimed | V-APP-GSN | none recorded | - | 0 | if indeed you continue in the faith, stable and steadfast, not shifting from the hope of the gospel that you heard, which has been **proclaimed** in all creation under heaven, and of which I, Paul, became a minister. |
| 1Th 2:9 | proclaimed | V-AAI-1P | none recorded | - | 0 | For you remember, brothers, our labor and toil: we worked night and day, that we might not be a burden to any of you, while we **proclaimed** to you the gospel of God. |
| 1Ti 3:16 | proclaimed | V-API-3S | none recorded | - | 0 | Great indeed, we confess, is the mystery of godliness: He was manifested in the flesh, vindicated by the Spirit, seen by angels, **proclaimed** among the nations, believed on in the world, taken up in glory. |
| 1Pe 3:19 | proclaimed | V-AAI-3S | none recorded | - | 0 | in which he went and **proclaimed** to the spirits in prison, |
| Mat 4:23 | proclaiming | V-PAP-NSM | none recorded | - | 0 | And he went throughout all Galilee, teaching in their synagogues and **proclaiming** the gospel of the kingdom and healing every disease and every affliction among the people. |
| Mat 9:35 | proclaiming | V-PAP-NSM | none recorded | - | 0 | And Jesus went throughout all the cities and villages, teaching in their synagogues and **proclaiming** the gospel of the kingdom and healing every disease and every affliction. |
| Mar 1:4 | proclaiming | V-PAP-NSM | none recorded | - | 0 | John appeared, baptizing in the wilderness and **proclaiming** a baptism of repentance for the forgiveness of sins. |
| Mar 1:14 | proclaiming | V-PAP-NSM | none recorded | - | 0 | Now after John was arrested, Jesus came into Galilee, **proclaiming** the gospel of God, |
| Luk 3:3 | proclaiming | V-PAP-NSM | none recorded | - | 0 | And he went into all the region around the Jordan, **proclaiming** a baptism of repentance for the forgiveness of sins. |
| Luk 8:1 | proclaiming | V-PAP-NSM | none recorded | - | 0 | Soon afterward he went on through cities and villages, **proclaiming** and bringing the good news of the kingdom of God. And the twelve were with him, |
| Luk 8:39 | proclaiming | V-PAP-NSM | none recorded | - | 0 | “ Return to your home, and declare how much God has done for you.” And he went away, **proclaiming** throughout the whole city how much Jesus had done for him. |
| Act 20:25 | proclaiming | V-PAP-NSM | none recorded | - | 0 | And now, behold, I know that none of you among whom I have gone about **proclaiming** the kingdom will see my face again. |
| Act 28:31 | proclaiming | V-PAP-NSM | none recorded | - | 0 | **proclaiming** the kingdom of God and teaching about the Lord Jesus Christ with all boldness and without hindrance. |
| Rev 5:2 | proclaiming | V-PAP-ASM | none recorded | - | 0 | And I saw a mighty angel **proclaiming** with a loud voice, “ Who is worthy to open the scroll and break its seals?” |
| Act 19:13 | proclaims | V-PAI-3S | none recorded | - | 0 | Then some of the itinerant Jewish exorcists undertook to invoke the name of the Lord Jesus over those who had evil spirits, saying, “I adjure you by the Jesus whom Paul **proclaims**.” |
| 2Cor 11:4 | proclaims | V-PAI-3S | none recorded | - | 0 | For if someone comes and **proclaims** another Jesus than the one we proclaimed, or if you receive a different spirit from the one you received, or if you accept a different gospel from the one you accepted, you put up with it readily enough. |

### 3.5 G2097 εὐαγγελίζομαι euangelizomai "to speak good news": 47 own occurrences in 45 verses

- **Meaning as stored:** Greek; native word εὐαγγελίζομαι, transliteration euangelizomai; STEP gloss "to speak good news"; sense head "to speak good news" (the code is its own lemma).
- **Related terms (6):** G0032G angelos "angel"; G0032H angelos "angel: messenger"; G2095 eu "well/well done!"; G2098 euangelion "gospel"; G2099 euangelistēs "evangelist"; G4283 proeuangelizomai "to speak good news".
- **Clusters (cluster_strong):** M65 Speech & Tongue (heuristic).
- **Counts, three measures as stored:** STEP token count 78; verses STEP attests 52; verse_lexical rows the parse found 55.

- **Carried by the member words:** preached (12), good news (11), preach the gospel (8), preaching (7), preached the gospel (3), preaching the gospel (3), preach (2), proclaim (1).
- **Engagement of these occurrences:** none recorded 47.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 11:5 | good news | V-PPI-3P | none recorded | - | 0 | the blind receive their sight and the lame walk, lepers are cleansed and the deaf hear, and the dead are raised up, and the poor have **good news** preached to them. |
| Luk 1:19 | good news | V-AMN | none recorded | - | 0 | And the angel answered him, “ I am Gabriel. I stand in the presence of God, and I was sent to speak to you and to bring you this **good news**. |
| Luk 2:10 | good news | V-PMI-1S | none recorded | - | 0 | And the angel said to them, “ Fear not, for behold, I bring you **good news** of great joy that will be for all the people. |
| Luk 4:18 | good news | V-AMN | none recorded | 16715 | 0 | “The Spirit of the Lord is upon me, because he has anointed me to proclaim **good news** to the poor. He has sent me to proclaim liberty to the captives and recovering of sight to the blind, to set at liberty those who are oppressed, |
| Luk 4:43 | good news | V-AMN | none recorded | - | 0 | but he said to them, “ I must preach the **good news** of the kingdom of God to the other towns as well; for I was sent for this purpose.” |
| Act 8:12 | good news | V-PMP-DSM | none recorded | - | 0 | But when they believed Philip as he preached **good news** about the kingdom of God and the name of Jesus Christ, they were baptized, both men and women. |
| Act 10:36 | good news | V-PMP-NSM | none recorded | - | 0 | As for the word that he sent to Israel, preaching **good news** of peace through Jesus Christ ( he is Lord of all ), |
| 1Th 3:6 | good news | V-AMP-GSM | none recorded | - | 0 | But now that Timothy has come to us from you, and has brought us the **good news** of your faith and love and reported that you always remember us kindly and long to see us, as we long to see you — |
| Heb 4:2 | good news | V-RPP-NPM | none recorded | - | 0 | For **good news** came to us just as to them, but the message they heard did not benefit them, because they were not united by faith with those who listened. |
| Heb 4:6 | good news | V-APP-NPM | none recorded | - | 0 | Since therefore it remains for some to enter it, and those who formerly received the **good news** failed to enter because of disobedience, |
| 1Pe 1:12 | good news | V-AMP-GPM | none recorded | - | 0 | It was revealed to them that they were serving not themselves but you, in the things that have now been announced to you through those who preached the **good news** to you by the Holy Spirit sent from heaven, things into which angels long to look. |
| Gal 1:16 | preach | V-PMS-1S | none recorded | - | 0 | was pleased to reveal his Son to me, in order that I might **preach** him among the Gentiles, I did not immediately consult with anyone; |
| Eph 3:8 | preach | V-AMN | none recorded | - | 0 | To me, though I am the very least of all the saints, this grace was given, to **preach** to the Gentiles the unsearchable riches of Christ, |
| Act 14:7 | preach the gospel | V-PMP-NPM | none recorded | - | 0 | and there they continued to **preach the gospel**. |
| Act 16:10 | preach the gospel | V-AMN | none recorded | - | 0 | And when Paul had seen the vision, immediately we sought to go on into Macedonia, concluding that God had called us to **preach the gospel** to them. |
| Rom 1:15 | preach the gospel | V-AMN | none recorded | - | 0 | So I am eager to **preach the gospel** to you also who are in Rome. |
| Rom 15:20 | preach the gospel | V-PMN | none recorded | 17480 | 0 | and thus I make it my ambition to **preach the gospel**, not where Christ has already been named, lest I build on someone else’s foundation, |
| 1Cor 1:17 | preach the gospel | V-PMN | none recorded | - | 0 | For Christ did not send me to baptize but to **preach the gospel**, and not with words of eloquent wisdom, lest the cross of Christ be emptied of its power. |
| 1Cor 9:16 | preach the gospel | V-PMS-1S | none recorded | 15194 | 0 | For if I **preach the gospel**, that gives me no ground for boasting. For necessity is laid upon me. Woe to me if I do not preach the gospel! |
| 1Cor 9:16 | preach the gospel | V-AMS-1S | none recorded | - | 0 | For if I **preach the gospel**, that gives me no ground for boasting. For necessity is laid upon me. Woe to me if I do not preach the gospel! |
| 2Cor 10:16 | preach the gospel | V-AMN | none recorded | - | 0 | so that we may **preach the gospel** in lands beyond you, without boasting of work already done in another’s area of influence. |
| Mat 11:5 | preached | V-PPI-3P | none recorded | - | 0 | the blind receive their sight and the lame walk, lepers are cleansed and the deaf hear, and the dead are raised up, and the poor have good news **preached** to them. |
| Luk 3:18 | preached | V-IMI-3S | none recorded | - | 0 | So with many other exhortations he **preached** good news to the people. |
| Luk 7:22 | preached | V-PPI-3P | none recorded | - | 0 | And he answered them, “ Go and tell John what you have seen and heard: the blind receive their sight, the lame walk, lepers are cleansed, and the deaf hear, the dead are raised up, the poor have good news **preached** to them. |
| Luk 16:16 | preached | V-PEI-3S | none recorded | - | 0 | “The Law and the Prophets were until John; since then the good news of the kingdom of God is **preached**, and everyone forces his way into it. |
| 1Cor 15:1 | preached | V-AMI-1S | none recorded | - | 0 | Now I would remind you, brothers, of the gospel I **preached** to you, which you received, in which you stand, |
| 1Cor 15:2 | preached | V-AMI-1S | none recorded | - | 0 | and by which you are being saved, if you hold fast to the word I **preached** to you — unless you believed in vain. |
| 2Cor 11:7 | preached | V-AMI-1S | none recorded | 15470 | 0 | Or did I commit a sin in humbling myself so that you might be exalted, because I **preached** God’s gospel to you free of charge? |
| Gal 1:8 | preached | V-AMI-1P | none recorded | - | 0 | But even if we or an angel from heaven should preach to you a gospel contrary to the one we **preached** to you, let him be accursed. |
| Gal 1:11 | preached | V-APP-ASN | none recorded | - | 0 | For I would have you know, brothers, that the gospel that was **preached** by me is not man’s gospel. |
| Eph 2:17 | preached | V-AMI-3S | none recorded | - | 0 | And he came and **preached** peace to you who were far off and peace to those who were near. |
| 1Pe 1:25 | preached | V-APP-NSN | none recorded | - | 0 | but the word of the Lord remains forever.” And this word is the good news that was **preached** to you. |
| 1Pe 4:6 | preached | V-API-3S | none recorded | - | 0 | For this is why the gospel was **preached** even to those who are dead, that though judged in the flesh the way people are, they might live in the spirit the way God does. |
| Act 8:40 | preached the gospel | V-IMI-3S | none recorded | - | 0 | But Philip found himself at Azotus, and as he passed through he **preached the gospel** to all the towns until he came to Caesarea. |
| Act 14:21 | preached the gospel | V-AMP-NPM | none recorded | - | 0 | When they had **preached the gospel** to that city and had made many disciples, they returned to Lystra and to Iconium and to Antioch, |
| Gal 4:13 | preached the gospel | V-AMI-1S | none recorded | - | 0 | You know it was because of a bodily ailment that I **preached the gospel** to you at first, |
| Act 5:42 | preaching | V-PMP-NPM | none recorded | - | 0 | And every day, in the temple and from house to house, they did not cease teaching and **preaching** that the Christ is Jesus. |
| Act 8:4 | preaching | V-PMP-NPM | none recorded | - | 0 | Now those who were scattered went about **preaching** the word. |
| Act 11:20 | preaching | V-PMP-NPM | none recorded | - | 0 | But there were some of them, men of Cyprus and Cyrene, who on coming to Antioch spoke to the Hellenists also, **preaching** the Lord Jesus. |
| Act 15:35 | preaching | V-PMP-NPM | none recorded | - | 0 | But Paul and Barnabas remained in Antioch, teaching and **preaching** the word of the Lord, with many others also. |
| Act 17:18 | preaching | V-IMI-3S | none recorded | - | 0 | Some of the Epicurean and Stoic philosophers also conversed with him. And some said, “ What does this babbler wish to say?” Others said, “He seems to be a preacher of foreign divinities ”— because he was **preaching** Jesus and the resurrection. |
| 1Cor 9:18 | preaching | V-PMP-NSM | none recorded | 15194 | 0 | What then is my reward? That in my **preaching** I may present the gospel free of charge, so as not to make full use of my right in the gospel. |
| Gal 1:23 | preaching | V-PEI-3S | none recorded | - | 0 | They only were hearing it said, “He who used to persecute us is now **preaching** the faith he once tried to destroy.” |
| Luk 9:6 | preaching the gospel | V-PMP-NPM | none recorded | - | 0 | And they departed and went through the villages, **preaching the gospel** and healing everywhere. |
| Luk 20:1 | preaching the gospel | V-PMP-GSM | none recorded | - | 0 | One day, as Jesus was teaching the people in the temple and **preaching the gospel**, the chief priests and the scribes with the elders came up |
| Act 8:25 | preaching the gospel | V-IMI-3P | none recorded | - | 0 | Now when they had testified and spoken the word of the Lord, they returned to Jerusalem, **preaching the gospel** to many villages of the Samaritans. |
| Rev 14:6 | proclaim | V-AAN | none recorded | - | 0 | Then I saw another angel flying directly overhead, with an eternal gospel to **proclaim** to those who dwell on earth, to every nation and tribe and language and people. |

### 3.6 H7121I קָרָא qa.ra "to call: call out": 30 own occurrences in 30 verses

- **Meaning as stored:** Hebrew; native word קָרָא, transliteration qa.ra; STEP gloss "to call: call out"; sense head "call out/shout/announce".
- **Senses (first level of the meaning tree of the lemma H7121):** to call, call out, recite, read, cry out, proclaim.
- **Related terms (13):** H4744 miq.ra "assembly"; H6981G qo.re "Kore"; H6981H qo.re "Kore"; H7121G qa.ra "to call: call to"; H7121H qa.ra "to call: call by"; H7121J qa.ra "to call: read out"; more in the workbook.
- **Clusters (cluster_strong):** M42 Prayer & Petition (heuristic).
- **Counts, three measures as stored:** STEP token count 106; verses STEP attests 102; verse_lexical rows the parse found 106.

- **Carried by the member words:** proclaim (16), proclaimed (9), proclaiming (3), proclaims (2).
- **Engagement of these occurrences:** none recorded 30.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Exo 33:19 | proclaim | HVqq1cs | none recorded | - | 0 | And he said, “I will make all my goodness pass before you and will **proclaim** before you my name ‘The Lord.’ And I will be gracious to whom I will be gracious, and will show mercy on whom I will show mercy. |
| Lev 23:2 | proclaim | HVqi2mp | none recorded | - | 0 | “ Speak to the people of Israel and say to them, These are the appointed feasts of the Lord that you shall **proclaim** as holy convocations; they are my appointed feasts. |
| Lev 23:4 | proclaim | HVqi2mp | none recorded | - | 0 | “These are the appointed feasts of the Lord, the holy convocations, which you shall **proclaim** at the time appointed for them. |
| Lev 23:37 | proclaim | HVqi2mp | none recorded | - | 0 | “These are the appointed feasts of the Lord, which you shall **proclaim** as times of holy convocation, for presenting to the Lord food offerings, burnt offerings and grain offerings, sacrifices and drink offerings, each on its proper day, |
| Deu 32:3 | proclaim | HVqi1cs | none recorded | - | 0 | For I will **proclaim** the name of the Lord; ascribe greatness to our God! |
| Judg 7:3 | proclaim | HVqv2ms | none recorded | - | 0 | Now therefore **proclaim** in the ears of the people, saying, ‘ Whoever is fearful and trembling, let him return home and hurry away from Mount Gilead.’” Then 22,000 of the people returned, and 10,000 remained. |
| 1Ki 21:9 | proclaim | HVqv2mp | none recorded | - | 0 | And she wrote in the letters, “ **Proclaim** a fast, and set Naboth at the head of the people. |
| Isa 61:1 | proclaim | HVqcc | none recorded | - | 0 | The Spirit of the Lord God is upon me, because the Lord has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted, to **proclaim** liberty to the captives, and the opening of the prison to those who are bound; |
| Isa 61:2 | proclaim | HVqcc | none recorded | - | 0 | to **proclaim** the year of the Lord’s favor, and the day of vengeance of our God; to comfort all who mourn; |
| Jer 3:12 | proclaim | HVqq2ms | none recorded | - | 0 | Go, and **proclaim** these words toward the north, and say, “‘ Return, faithless Israel, declares the Lord. I will not look on you in anger, for I am merciful, declares the Lord; I will not be angry forever. |
| Jer 7:2 | proclaim | HVqq2ms | none recorded | - | 0 | “ Stand in the gate of the Lord’s house, and **proclaim** there this word, and say, Hear the word of the Lord, all you men of Judah who enter these gates to worship the Lord. |
| Jer 11:6 | proclaim | HVqv2ms | none recorded | - | 0 | And the Lord said to me, “ **Proclaim** all these words in the cities of Judah and in the streets of Jerusalem: Hear the words of this covenant and do them. |
| Jer 19:2 | proclaim | HVqq2ms | none recorded | - | 0 | and go out to the Valley of the Son of Hinnom at the entry of the Potsherd Gate, and **proclaim** there the words that I tell you. |
| Jer 34:17 | proclaim | HVqrmsa | none recorded | - | 0 | “ Therefore, thus says the Lord: You have not obeyed me by proclaiming liberty, every one to his brother and to his neighbor; behold, I **proclaim** to you liberty to the sword, to pestilence, and to famine, declares the Lord. I will make you a horror to all the kingdoms of the earth. |
| Joe 3:9 | proclaim | HVqv2mp | none recorded | - | 0 | **Proclaim** this among the nations: Consecrate for war; stir up the mighty men. Let all the men of war draw near; let them come up. |
| Amo 4:5 | proclaim | HVqv2mp | none recorded | - | 0 | offer a sacrifice of thanksgiving of that which is leavened, and **proclaim** freewill offerings, publish them; for so you love to do, O people of Israel!” declares the Lord God. |
| Exo 34:5 | proclaimed | HVqw3ms | none recorded | - | 0 | The Lord descended in the cloud and stood with him there, and **proclaimed** the name of the Lord. |
| Exo 34:6 | proclaimed | HVqw3ms | none recorded | 12952, 13012, 13207, 13248, 14511 | 0 | The Lord passed before him and **proclaimed**, “The Lord, the Lord, a God merciful and gracious, slow to anger, and abounding in steadfast love and faithfulness, |
| Deu 15:2 | proclaimed | HVqp3ms | none recorded | - | 0 | And this is the manner of the release: every creditor shall release what he has lent to his neighbor. He shall not exact it of his neighbor, his brother, because the Lord’s release has been **proclaimed**. |
| Judg 21:13 | proclaimed | HVqw3mp | none recorded | - | 0 | Then the whole congregation sent word to the people of Benjamin who were at the rock of Rimmon and **proclaimed** peace to them. |
| 1Ki 21:12 | proclaimed | HVqp3cp | none recorded | - | 0 | they **proclaimed** a fast and set Naboth at the head of the people. |
| 2Ki 10:20 | proclaimed | HVqw3mp | none recorded | - | 0 | And Jehu ordered, “ Sanctify a solemn assembly for Baal.” So they **proclaimed** it. |
| 2Ch 20:3 | proclaimed | HVqw3ms | none recorded | - | 0 | Then Jehoshaphat was afraid and set his face to seek the Lord, and **proclaimed** a fast throughout all Judah. |
| Ezr 8:21 | proclaimed | HVqw1cs | none recorded | 14595 | 0 | Then I **proclaimed** a fast there, at the river Ahava, that we might humble ourselves before our God, to seek from him a safe journey for ourselves, our children, and all our goods. |
| Jer 36:9 | proclaimed | HVqp3cp | none recorded | 14700 | 0 | In the fifth year of Jehoiakim the son of Josiah, king of Judah, in the ninth month, all the people in Jerusalem and all the people who came from the cities of Judah to Jerusalem **proclaimed** a fast before the Lord. |
| Est 6:9 | proclaiming | HVqq3cp | none recorded | - | 0 | And let the robes and the horse be handed over to one of the king’s most noble officials. Let them dress the man whom the king delights to honor, and let them lead him on the horse through the square of the city, **proclaiming** before him: ‘ Thus shall it be done to the man whom the king delights to honor.’” |
| Est 6:11 | proclaiming | HVqw3ms | none recorded | - | 0 | So Haman took the robes and the horse, and he dressed Mordecai and led him through the square of the city, **proclaiming** before him, “ Thus shall it be done to the man whom the king delights to honor.” |
| Jer 34:15 | proclaiming | HVqcc | none recorded | - | 0 | You recently repented and did what was right in my eyes by **proclaiming** liberty, each to his neighbor, and you made a covenant before me in the house that is called by my name, |
| Pro 12:23 | proclaims | HVqi3ms | none recorded | 16480 | 0 | A prudent man conceals knowledge, but the heart of fools **proclaims** folly. |
| Pro 20:6 | proclaims | HVqi3ms | none recorded | - | 0 | Many a man **proclaims** his own steadfast love, but a faithful man who can find? |

### 3.7 G4395 προφητεύω profēteuō "to prophesy": 23 own occurrences in 23 verses

- **Meaning as stored:** Greek; native word προφητεύω, transliteration profēteuō; STEP gloss "to prophesy"; sense head "to prophesy" (the code is its own lemma).
- **Related terms (5):** G4394 profēteia "prophecy"; G4396 profētēs "prophet"; G4397 profētikos "prophetic"; G4398 profētis "prophetess"; G5578 pseudoprofētēs "false prophet".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (heuristic).
- **Counts, three measures as stored:** STEP token count 144; verses STEP attests 27; verse_lexical rows the parse found 28.

- **Carried by the member words:** prophesy (16), prophesied (6), prophesying (1).
- **Engagement of these occurrences:** none recorded 23.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 11:13 | prophesied | V-AAI-3P | none recorded | - | 0 | For all the Prophets and the Law **prophesied** until John, |
| Luk 1:67 | prophesied | V-AAI-3S | none recorded | - | 0 | And his father Zechariah was filled with the Holy Spirit and **prophesied**, saying, |
| Joh 11:51 | prophesied | V-AAI-3S | none recorded | 20564 | 0 | He did not say this of his own accord, but being high priest that year he **prophesied** that Jesus would die for the nation, |
| Act 21:9 | prophesied | V-PAP-NPF | none recorded | - | 0 | He had four unmarried daughters, who **prophesied**. |
| 1Pe 1:10 | prophesied | V-AAP-NPM | none recorded | - | 0 | Concerning this salvation, the prophets who **prophesied** about the grace that was to be yours searched and inquired carefully, |
| Jude 14 | prophesied | V-AAI-3S | none recorded | - | 0 | It was also about these that Enoch, the seventh from Adam, **prophesied**, saying, “ Behold, the Lord comes with ten thousands of his holy ones, |
| Mat 7:22 | prophesy | V-AAI-1P | none recorded | - | 0 | On that day many will say to me, ‘ Lord, Lord, did we not **prophesy** in your name, and cast out demons in your name, and do many mighty works in your name?’ |
| Mat 15:7 | prophesy | V-AAI-3S | none recorded | - | 0 | You hypocrites! Well did Isaiah **prophesy** of you, when he said: |
| Mat 26:68 | prophesy | V-AAM-2S | none recorded | - | 0 | saying, “ **Prophesy** to us, you Christ! Who is it that struck you?” |
| Mar 7:6 | prophesy | V-AAI-3S | none recorded | - | 0 | And he said to them, “ Well did Isaiah **prophesy** of you hypocrites, as it is written, “‘ This people honors me with their lips, but their heart is far from me; |
| Mar 14:65 | prophesy | V-AAM-2S | none recorded | - | 0 | And some began to spit on him and to cover his face and to strike him, saying to him, “ **Prophesy**!” And the guards received him with blows. |
| Luk 22:64 | prophesy | V-AAM-2S | none recorded | 15223 | 0 | They also blindfolded him and kept asking him, “ **Prophesy**! Who is it that struck you?” |
| Act 2:17 | prophesy | V-FAI-3P | none recorded | 16021 | 0 | “‘ And in the last days it shall be, God declares, that I will pour out my Spirit on all flesh, and your sons and your daughters shall **prophesy**, and your young men shall see visions, and your old men shall dream dreams; |
| Act 2:18 | prophesy | V-FAI-3P | none recorded | 16021 | 0 | even on my male servants and female servants in those days I will pour out my Spirit, and they shall **prophesy**. |
| 1Cor 13:9 | prophesy | V-PAI-1P | none recorded | - | 0 | For we know in part and we **prophesy** in part, |
| 1Cor 14:1 | prophesy | V-PAS-2P | none recorded | - | 0 | Pursue love, and earnestly desire the spiritual gifts, especially that you may **prophesy**. |
| 1Cor 14:5 | prophesy | V-PAS-2P | none recorded | - | 0 | Now I want you all to speak in tongues, but even more to **prophesy**. The one who prophesies is greater than the one who speaks in tongues, unless someone interprets, so that the church may be built up. |
| 1Cor 14:24 | prophesy | V-PAS-3P | none recorded | - | 0 | But if all **prophesy**, and an unbeliever or outsider enters, he is convicted by all, he is called to account by all, |
| 1Cor 14:31 | prophesy | V-PAN | none recorded | - | 0 | For you can all **prophesy** one by one, so that all may learn and all be encouraged, |
| 1Cor 14:39 | prophesy | V-PAN | none recorded | - | 0 | So, my brothers, earnestly desire to **prophesy**, and do not forbid speaking in tongues. |
| Rev 10:11 | prophesy | V-AAN | none recorded | - | 0 | And I was told, “ You must again **prophesy** about many peoples and nations and languages and kings.” |
| Rev 11:3 | prophesy | V-FAI-3P | none recorded | - | 0 | And I will grant authority to my two witnesses, and they will **prophesy** for 1,260 days, clothed in sackcloth.” |
| Act 19:6 | prophesying | V-IAI-3P | none recorded | - | 0 | And when Paul had laid his hands on them, the Holy Spirit came on them, and they began speaking in tongues and **prophesying**. |

### 3.8 H8085I שָׁמַע sha.ma "to hear: proclaim": 20 own occurrences in 18 verses

- **Meaning as stored:** Hebrew; native word שָׁמַע, transliteration sha.ma; STEP gloss "to hear: proclaim"; sense head "proclaim/loud".
- **Senses (first level of the meaning tree of the lemma H8085):** to hear, listen to, obey; sound.
- **Related terms (90):** H2045 hash.ma.ut "report"; H3458G yish.ma.el "Ishmael"; H3458H yish.ma.el "Ishmael"; H3458I yish.ma.el "Ishmael"; H3458J yish.ma.el "Ishmael"; H3458K yish.ma.el "Ishmael"; more in the workbook.
- **Clusters (cluster_strong):** M41 Being Heard (None).
- **Counts, three measures as stored:** STEP token count 49; verses STEP attests 46; verse_lexical rows the parse found 49.

- **Carried by the member words:** proclaim (9), proclaimed (6), declare (2), announce (1), proclaiming (1), proclaims (1).
- **Engagement of these occurrences:** none recorded 20.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 4:16 | announce | HVhv2mp | none recorded | - | 0 | Warn the nations that he is coming; **announce** to Jerusalem, “ Besiegers come from a distant land; they shout against the cities of Judah. |
| Psa 106:2 | declare | HVhi3ms | none recorded | - | 0 | Who can utter the mighty deeds of the Lord, or **declare** all his praise? |
| Isa 41:22 | declare | HVhv2mp | none recorded | - | 0 | Let them bring them, and tell us what is to happen. Tell us the former things, what they are, that we may consider them, that we may know their outcome; or **declare** to us the things to come. |
| Isa 48:20 | proclaim | HVhv2mp | none recorded | - | 0 | Go out from Babylon, flee from Chaldea, declare this with a shout of joy, **proclaim** it, send it out to the end of the earth; say, “The Lord has redeemed his servant Jacob!” |
| Jer 4:5 | proclaim | HVhv2mp | none recorded | - | 0 | Declare in Judah, and **proclaim** in Jerusalem, and say, “ Blow the trumpet through the land; cry aloud and say, ‘ Assemble, and let us go into the fortified cities!’ |
| Jer 5:20 | proclaim | HVhv2mp | none recorded | - | 0 | Declare this in the house of Jacob; **proclaim** it in Judah: |
| Jer 31:7 | proclaim | HVhv2mp | none recorded | - | 0 | For thus says the Lord: “ Sing aloud with gladness for Jacob, and raise shouts for the chief of the nations; **proclaim**, give praise, and say, ‘O Lord, save your people, the remnant of Israel.’ |
| Jer 46:14 | proclaim | HVhv2mp | none recorded | - | 0 | “ Declare in Egypt, and **proclaim** in Migdol; proclaim in Memphis and Tahpanhes; say, ‘ Stand ready and be prepared, for the sword shall devour around you.’ |
| Jer 46:14 | proclaim | HVhv2mp | none recorded | - | 0 | “ Declare in Egypt, and **proclaim** in Migdol; proclaim in Memphis and Tahpanhes; say, ‘ Stand ready and be prepared, for the sword shall devour around you.’ |
| Jer 50:2 | proclaim | HVhv2mp | none recorded | 19226 | 0 | “ Declare among the nations and **proclaim**, set up a banner and proclaim, conceal it not, and say: ‘ Babylon is taken, Bel is put to shame, Merodach is dismayed. Her images are put to shame, her idols are dismayed.’ |
| Jer 50:2 | proclaim | HVhv2mp | none recorded | 19226 | 0 | “ Declare among the nations and **proclaim**, set up a banner and proclaim, conceal it not, and say: ‘ Babylon is taken, Bel is put to shame, Merodach is dismayed. Her images are put to shame, her idols are dismayed.’ |
| Amo 3:9 | proclaim | HVhv2mp | none recorded | - | 0 | **Proclaim** to the strongholds in Ashdod and to the strongholds in the land of Egypt, and say, “ Assemble yourselves on the mountains of Samaria, and see the great tumults within her, and the oppressed in her midst.” |
| Est 1:20 | proclaimed | HVNq3ms | none recorded | - | 0 | So when the decree made by the king is **proclaimed** throughout all his kingdom, for it is vast, all women will give honor to their husbands, high and low alike.” |
| Est 2:8 | proclaimed | HVNcc | none recorded | - | 0 | So when the king’s order and his edict were **proclaimed**, and when many young women were gathered in Susa the citadel in custody of Hegai, Esther also was taken into the king’s palace and put in custody of Hegai, who had charge of the women. |
| Isa 41:26 | proclaimed | HVhrmsa | none recorded | - | 0 | Who declared it from the beginning, that we might know, and beforehand, that we might say, “He is right ”? There was none who declared it, none who **proclaimed**, none who heard your words. |
| Isa 43:12 | proclaimed | HVhq1cs | none recorded | - | 0 | I declared and saved and **proclaimed**, when there was no strange god among you; and you are my witnesses,” declares the Lord, “and I am God. |
| Isa 62:11 | proclaimed | HVhp3ms | none recorded | - | 0 | Behold, the Lord has **proclaimed** to the end of the earth: Say to the daughter of Zion, “ Behold, your salvation comes; behold, his reward is with him, and his recompense before him.” |
| Jer 23:22 | proclaimed | HVhu3mp | none recorded | 14716 | 0 | But if they had stood in my council, then they would have **proclaimed** my words to my people, and they would have turned them from their evil way, and from the evil of their deeds. |
| Psa 26:7 | proclaiming | HVhcc | none recorded | - | 0 | **proclaiming** thanksgiving aloud, and telling all your wondrous deeds. |
| Jer 4:15 | proclaims | HVhrmsa | none recorded | - | 0 | For a voice declares from Dan and **proclaims** trouble from Mount Ephraim. |

### 3.9 G2605 καταγγέλλω katangellō "to proclaim": 16 own occurrences in 16 verses

- **Meaning as stored:** Greek; native word καταγγέλλω, transliteration katangellō; STEP gloss "to proclaim"; sense head "to proclaim" (the code is its own lemma).
- **Related terms (5):** G0032G angelos "angel"; G0032H angelos "angel: messenger"; G2596 kata "according to"; G2604 katangeleus "proclaimer"; G4293 prokatangellō "to foretell".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 18; verses STEP attests 0; verse_lexical rows the parse found 17.

- **Carried by the member words:** proclaim (8), proclaimed (6), proclaiming (2).
- **Engagement of these occurrences:** none recorded 16.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 16:17 | proclaim | V-PAI-3P | none recorded | - | 0 | She followed Paul and us, crying out, “ These men are servants of the Most High God, who **proclaim** to you the way of salvation.” |
| Act 17:3 | proclaim | V-PAI-1S | none recorded | - | 0 | explaining and proving that it was necessary for the Christ to suffer and to rise from the dead, and saying, “ This Jesus, whom I **proclaim** to you, is the Christ.” |
| Act 17:23 | proclaim | V-PAI-1S | none recorded | - | 0 | For as I passed along and observed the objects of your worship, I found also an altar with this inscription, ‘To the unknown god.’ What therefore you worship as unknown, this I **proclaim** to you. |
| Act 26:23 | proclaim | V-PAN | none recorded | - | 0 | that the Christ must suffer and that, by being the first to rise from the dead, he would **proclaim** light both to our people and to the Gentiles.” |
| 1Cor 9:14 | proclaim | V-PAP-DPM | none recorded | - | 0 | In the same way, the Lord commanded that those who **proclaim** the gospel should get their living by the gospel. |
| 1Cor 11:26 | proclaim | V-PAI-2P | none recorded | - | 0 | For as often as you eat this bread and drink the cup, you **proclaim** the Lord’s death until he comes. |
| Phili 1:17 | proclaim | V-PAI-3P | none recorded | - | 0 | The former **proclaim** Christ out of selfish ambition, not sincerely but thinking to afflict me in my imprisonment. |
| Col 1:28 | proclaim | V-PAI-1P | none recorded | - | 0 | Him we **proclaim**, warning everyone and teaching everyone with all wisdom, that we may present everyone mature in Christ. |
| Act 13:5 | proclaimed | V-IAI-3P | none recorded | - | 0 | When they arrived at Salamis, they **proclaimed** the word of God in the synagogues of the Jews. And they had John to assist them. |
| Act 13:38 | proclaimed | V-PPI-3S | none recorded | - | 0 | Let it be known to you therefore, brothers, that through this man forgiveness of sins is **proclaimed** to you, |
| Act 15:36 | proclaimed | V-AAI-1P | none recorded | - | 0 | And after some days Paul said to Barnabas, “ Let us return and visit the brothers in every city where we **proclaimed** the word of the Lord, and see how they are.” |
| Act 17:13 | proclaimed | V-2API-3S | none recorded | - | 0 | But when the Jews from Thessalonica learned that the word of God was **proclaimed** by Paul at Berea also, they came there too, agitating and stirring up the crowds. |
| Rom 1:8 | proclaimed | V-PPI-3S | none recorded | - | 0 | First, I thank my God through Jesus Christ for all of you, because your faith is **proclaimed** in all the world. |
| Phili 1:18 | proclaimed | V-PPI-3S | none recorded | - | 0 | What then? Only that in every way, whether in pretense or in truth, Christ is **proclaimed**, and in that I rejoice. Yes, and I will rejoice, |
| Act 4:2 | proclaiming | V-PAN | none recorded | - | 0 | greatly annoyed because they were teaching the people and **proclaiming** in Jesus the resurrection from the dead. |
| 1Cor 2:1 | proclaiming | V-PAP-NSM | none recorded | - | 0 | And I, when I came to you, brothers, did not come **proclaiming** to you the testimony of God with lofty speech or wisdom. |

### 3.10 H5608A סָפַר sa.phar "to recount": 14 own occurrences in 14 verses

- **Meaning as stored:** Hebrew; native word סָפַר, transliteration sa.phar; STEP gloss "to recount"; sense head "to recount" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5608):** to count, recount, relate.
- **Related terms (17):** H4557 mis.par "number"; H4558 mis.par "Mispar"; H4559 mis.pe.ret "Mispereth"; H5601 sap.pir "sapphire"; H5608B so.pher "secretary"; H5609 se.phar "scroll"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 107; verses STEP attests 102; verse_lexical rows the parse found 107.

- **Carried by the member words:** declare (11), declared (2), set forth (1).
- **Engagement of these occurrences:** none recorded 14.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ch 16:24 | declare | HVpv2mp | none recorded | - | 0 | **Declare** his glory among the nations, his marvelous works among all the peoples! |
| Job 12:8 | declare | HVpu3mp | none recorded | - | 0 | or the bushes of the earth, and they will teach you; and the fish of the sea will **declare** to you. |
| Job 15:17 | declare | HVpc1cs | none recorded | - | 0 | “I will show you; hear me, and what I have seen I will **declare** |
| Psa 19:1 | declare | HVprmpa | none recorded | - | 0 | To the choirmaster. A Psalm of David. The heavens **declare** the glory of God, and the sky above proclaims his handiwork. |
| Psa 96:3 | declare | HVpv2mp | none recorded | - | 0 | **Declare** his glory among the nations, his marvelous works among all the peoples! |
| Psa 102:21 | declare | HVpcc | none recorded | - | 0 | that they may **declare** in Zion the name of the Lord, and in Jerusalem his praise, |
| Psa 119:13 | declare | HVpp1cs | none recorded | - | 0 | With my lips I **declare** all the rules of your mouth. |
| Psa 145:6 | declare | HVpi1cs | none recorded | - | 0 | They shall speak of the might of your awesome deeds, and I will **declare** your greatness. |
| Isa 43:21 | declare | HVpi3mp | none recorded | - | 0 | the people whom I formed for myself that they might **declare** my praise. |
| Jer 51:10 | declare | HVpc1cp | none recorded | - | 0 | The Lord has brought about our vindication; come, let us **declare** in Zion the work of the Lord our God. |
| Eze 12:16 | declare | HVpj3mp | none recorded | - | 0 | But I will let a few of them escape from the sword, from famine and pestilence, that they may **declare** all their abominations among the nations where they go, and may know that I am the Lord.” |
| Job 28:27 | declared | HVpw3ms | none recorded | - | 0 | then he saw it and **declared** it; he established it, and searched it out. |
| Psa 88:11 | declared | HVPi3ms | none recorded | - | 0 | Is your steadfast love **declared** in the grave, or your faithfulness in Abaddon? |
| Isa 43:26 | set forth | HVpv2ms | none recorded | - | 0 | Put me in remembrance; let us argue together; **set forth** your case, that you may be proved right. |

### 3.11 H1696I דָבַר da.var "to speak: promise": 10 own occurrences in 10 verses

- **Meaning as stored:** Hebrew; native word דָבַר, transliteration da.var; STEP gloss "to speak: promise"; sense head "promise/declare".
- **Senses (first level of the meaning tree of the lemma H1696):** to speak, declare, converse, command, promise, warn, threaten, sing.
- **Related terms (30):** H1682 de.vo.rah "bee"; H1683G de.vo.rah "Deborah"; H1683H de.vo.rah "Deborah"; H1687 de.vir "sanctuary"; H1688A de.vir "Debir"; H1688B lid.vir "Debir"; more in the workbook.
- **Clusters (cluster_strong):** M65 Speech & Tongue (high).
- **Counts, three measures as stored:** STEP token count 81; verses STEP attests 78; verse_lexical rows the parse found 81.

- **Carried by the member words:** declare (5), declared (5).
- **Engagement of these occurrences:** none recorded 10.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 34:33 | declare | HVpv2ms | none recorded | 19588, 20307 | 0 | Will he then make repayment to suit you, because you reject it? For you must choose, and not I; therefore **declare** what you know. |
| Jer 1:16 | declare | HVpq1cs | none recorded | - | 0 | And I will **declare** my judgments against them, for all their evil in forsaking me. They have made offerings to other gods and worshiped the works of their own hands. |
| Jer 18:7 | declare | HVpi1cs | none recorded | - | 0 | If at any time I **declare** concerning a nation or a kingdom, that I will pluck up and break down and destroy it, |
| Jer 18:9 | declare | HVpi1cs | none recorded | - | 0 | And if at any time I **declare** concerning a nation or a kingdom that I will build and plant it, |
| Eze 38:19 | declare | HVpp1cs | none recorded | 17846 | 0 | For in my jealousy and in my blazing wrath I **declare**, On that day there shall be a great earthquake in the land of Israel. |
| Lev 23:44 | declared | HVpw3ms | none recorded | - | 0 | Thus Moses **declared** to the people of Israel the appointed feasts of the Lord. |
| 1Ki 22:23 | declared | HVpp3ms | none recorded | 16264 | 0 | Now therefore behold, the Lord has put a lying spirit in the mouth of all these your prophets; the Lord has **declared** disaster for you.” |
| 2Ch 6:15 | declared | HVpp2ms | none recorded | - | 0 | who have kept with your servant David my father what you **declared** to him. You spoke with your mouth, and with your hand have fulfilled it this day. |
| 2Ch 18:22 | declared | HVpp3ms | none recorded | 16264 | 0 | Now therefore behold, the Lord has put a lying spirit in the mouth of these your prophets. The Lord has **declared** disaster concerning you.” |
| Jer 44:25 | declared | HVpw3fp | none recorded | - | 0 | Thus says the Lord of hosts, the God of Israel: You and your wives have **declared** with your mouths, and have fulfilled it with your hands, saying, ‘We will surely perform our vows that we have made, to make offerings to the queen of heaven and to pour out drink offerings to her.’ Then confirm your vows and perform your vows! |

### 3.12 H0559 אָמַר a.mar "to say": 9 own occurrences in 9 verses

- **Meaning as stored:** Hebrew; native word אָמַר, transliteration a.mar; STEP gloss "to say"; sense head "to say" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H0559):** to say, speak, utter.
- **Related terms (28):** H0201 o.mar "Omar"; H0204 on "On"; H0534 a.mir "top"; H0560 a.mar "to say"; H0561 e.mer "word"; H0562 o.mer "word"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 5343; verses STEP attests 4340; verse_lexical rows the parse found 5309.

- **Carried by the member words:** declares (4), declare (2), declared (2), proclaimed (1).
- **Engagement of these occurrences:** none recorded 9.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Deu 17:11 | declare | HVqi3mp | none recorded | - | 0 | According to the instructions that they give you, and according to the decision which they pronounce to you, you shall do. You shall not turn aside from the verdict that they **declare** to you, either to the right hand or to the left. |
| 1Sa 16:3 | declare | HVqi1cs | none recorded | - | 0 | And invite Jesse to the sacrifice, and I will show you what you shall do. And you shall anoint for me him whom I **declare** to you.” |
| Deu 26:17 | declared | HVhp2ms | none recorded | - | 0 | You have **declared** today that the Lord is your God, and that you will walk in his ways, and keep his statutes and his commandments and his rules, and will obey his voice. |
| Deu 26:18 | declared | HVhp3ms | none recorded | - | 0 | And the Lord has **declared** today that you are a people for his treasured possession, as he has promised you, and that you are to keep all his commandments, |
| Isa 66:23 | declares | HVqp3ms | none recorded | - | 0 | From new moon to new moon, and from Sabbath to Sabbath, all flesh shall come to worship before me, **declares** the Lord. |
| Eze 45:9 | declares | HVqp3ms | none recorded | - | 0 | “ Thus says the Lord God: Enough, O princes of Israel! Put away violence and oppression, and execute justice and righteousness. Cease your evictions of my people, **declares** the Lord God. |
| Hag 2:9 | declares | HVqp3ms | none recorded | - | 0 | The latter glory of this house shall be greater than the former, says the Lord of hosts. And in this place I will give peace, **declares** the Lord of hosts.’” |
| Zec 1:3 | declares | HVqp3ms | none recorded | - | 0 | Therefore say to them, Thus **declares** the Lord of hosts: Return to me, says the Lord of hosts, and I will return to you, says the Lord of hosts. |
| 2Ki 9:13 | proclaimed | HVqw3mp | none recorded | - | 0 | Then in haste every man of them took his garment and put it under him on the bare steps, and they blew the trumpet and **proclaimed**, “ Jehu is king.” |

### 3.13 G0312 ἀναγγέλλω anangellō "to report": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word ἀναγγέλλω, transliteration anangellō; STEP gloss "to report"; sense head "to report" (the code is its own lemma).
- **Related terms (3):** G0032G angelos "angel"; G0032H angelos "angel: messenger"; G0303 ana "each".
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 254; verses STEP attests 0; verse_lexical rows the parse found 14.

- **Carried by the member words:** declare (3), declared (2), declaring (2), proclaim (1).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 16:13 | declare | V-FAI-3S | none recorded | - | 0 | When the Spirit of truth comes, he will guide you into all the truth, for he will not speak on his own authority, but whatever he hears he will speak, and he will **declare** to you the things that are to come. |
| Joh 16:14 | declare | V-FAI-3S | none recorded | - | 0 | He will glorify me, for he will take what is mine and **declare** it to you. |
| Joh 16:15 | declare | V-FAI-3S | none recorded | - | 0 | All that the Father has is mine; therefore I said that he will take what is mine and **declare** it to you. |
| Act 14:27 | declared | V-IAI-3P | none recorded | - | 0 | And when they arrived and gathered the church together, they **declared** all that God had done with them, and how he had opened a door of faith to the Gentiles. |
| Act 15:4 | declared | V-AAI-3P | none recorded | - | 0 | When they came to Jerusalem, they were welcomed by the church and the apostles and the elders, and they **declared** all that God had done with them. |
| Act 20:20 | declaring | V-AAN | none recorded | - | 0 | how I did not shrink from **declaring** to you anything that was profitable, and teaching you in public and from house to house, |
| Act 20:27 | declaring | V-AAN | none recorded | - | 0 | for I did not shrink from **declaring** to you the whole counsel of God. |
| 1Jo 1:5 | proclaim | V-PAI-1P | none recorded | - | 0 | This is the message we have heard from him and **proclaim** to you, that God is light, and in him is no darkness at all. |

### 3.14 G2980 λαλέω laleō "to speak": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word λαλέω, transliteration laleō; STEP gloss "to speak"; sense head "to speak" (the code is its own lemma).
- **Related terms (5):** G0215 alalētos "inexpressible"; G0216 alalos "mute"; G2981 lalia "speech"; G3004G legō "to say: says"; G3004H legō "to say: name".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 1380; verses STEP attests 265; verse_lexical rows the parse found 288.

- **Carried by the member words:** declare (4), declared (3), preaching (1).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 11:14 | declare | V-FAI-3S | none recorded | - | 0 | he will **declare** to you a message by which you will be saved, you and all your household.’ |
| Col 4:3 | declare | V-AAN | none recorded | - | 0 | At the same time, pray also for us, that God may open to us a door for the word, to **declare** the mystery of Christ, on account of which I am in prison — |
| 1Th 2:2 | declare | V-AAN | none recorded | - | 0 | But though we had already suffered and been shamefully treated at Philippi, as you know, we had boldness in our God to **declare** to you the gospel of God in the midst of much conflict. |
| Tit 2:15 | declare | V-PAM-2S | none recorded | - | 0 | **Declare** these things; exhort and rebuke with all authority. Let no one disregard you. |
| Heb 2:2 | declared | V-APP-NSM | none recorded | - | 0 | For since the message **declared** by angels proved to be reliable, and every transgression or disobedience received a just retribution, |
| Heb 2:3 | declared | V-PPN | none recorded | - | 0 | how shall we escape if we neglect such a great salvation? It was **declared** at first by the Lord, and it was attested to us by those who heard, |
| Heb 9:19 | declared | V-APP-GSF | none recorded | - | 0 | For when every commandment of the law had been **declared** by Moses to all the people, he took the blood of calves and goats, with water and scarlet wool and hyssop, and sprinkled both the book itself and all the people, |
| Mar 2:2 | preaching | V-IAI-3S | none recorded | - | 0 | And many were gathered together, so that there was no more room, not even at the door. And he was **preaching** the word to them. |

### 3.15 G3004G λέγω legō "to say: says": 8 own occurrences in 8 verses

- **Meaning as stored:** Greek; native word λέγω, transliteration legō; STEP gloss "to say: says"; sense head "to say: says" (the code is its own lemma).
- **Related terms (15):** G0483 antilegō "to dispute"; G0557 apelegmos "discredit"; G1246 diakatelenchomai "to refute"; G1256 dialegō "to dispute"; G1649 elegxis "rebuke"; G1650 elenchos "rebuke"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 3420; verses STEP attests 1170; verse_lexical rows the parse found 1251.

- **Carried by the member words:** declares (5), declare (2), preach (1).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Joh 8:26 | declare | V-PAI-1S | none recorded | - | 0 | I have much to say about you and much to judge, but he who sent me is true, and I **declare** to the world what I have heard from him.” |
| 1Th 4:15 | declare | V-PAI-1P | none recorded | - | 0 | For this we **declare** to you by a word from the Lord, that we who are alive, who are left until the coming of the Lord, will not precede those who have fallen asleep. |
| Act 2:17 | declares | V-PAI-3S | none recorded | - | 0 | “‘ And in the last days it shall be, God **declares**, that I will pour out my Spirit on all flesh, and your sons and your daughters shall prophesy, and your young men shall see visions, and your old men shall dream dreams; |
| Heb 8:8 | declares | V-PAI-3S | none recorded | - | 0 | For he finds fault with them when he says: “ Behold, the days are coming, **declares** the Lord, when I will establish a new covenant with the house of Israel and with the house of Judah, |
| Heb 8:9 | declares | V-PAI-3S | none recorded | - | 0 | not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt. For they did not continue in my covenant, and so I showed no concern for them, **declares** the Lord. |
| Heb 8:10 | declares | V-PAI-3S | none recorded | - | 0 | For this is the covenant that I will make with the house of Israel after those days, **declares** the Lord: I will put my laws into their minds, and write them on their hearts, and I will be their God, and they shall be my people. |
| Heb 10:16 | declares | V-PAI-3S | none recorded | - | 0 | “ This is the covenant that I will make with them after those days, **declares** the Lord: I will put my laws on their hearts, and write them on their minds,” |
| Mat 23:3 | preach | V-PAI-3P | none recorded | - | 0 | so do and observe whatever they tell you, but not the works they do. For they **preach**, but do not practice. |

### 3.16 H1319 בָּשַׂר ba.sar "to bear tidings": 8 own occurrences in 6 verses

- **Meaning as stored:** Hebrew; native word בָּשַׂר, transliteration ba.sar; STEP gloss "to bear tidings"; sense head "to bear tidings" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H1319):** to bear news, bear tidings, publish, preach, show forth.
- **Related terms (3):** H1308 be.s.vor "Besor"; H1309 be.so.rah "good news"; H1320 ba.sar "flesh".
- **Clusters (cluster_strong):** M70 Lifting & Bearing (heuristic).
- **Counts, three measures as stored:** STEP token count 24; verses STEP attests 21; verse_lexical rows the parse found 24.

- **Carried by the member words:** good news (8).
- **Engagement of these occurrences:** none recorded 8.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ch 10:9 | good news | HVpcc | none recorded | - | 0 | And they stripped him and took his head and his armor, and sent messengers throughout the land of the Philistines to carry the **good news** to their idols and to the people. |
| Isa 40:9 | good news | HVprfsc | none recorded | - | 0 | Go on up to a high mountain, O Zion, herald of **good news**; lift up your voice with strength, O Jerusalem, herald of good news; lift it up, fear not; say to the cities of Judah, “ Behold your God!” |
| Isa 40:9 | good news | HVprfsc | none recorded | - | 0 | Go on up to a high mountain, O Zion, herald of **good news**; lift up your voice with strength, O Jerusalem, herald of good news; lift it up, fear not; say to the cities of Judah, “ Behold your God!” |
| Isa 41:27 | good news | HVprmsa | none recorded | - | 0 | I was the first to say to Zion, “ Behold, here they are!” and I give to Jerusalem a herald of **good news**. |
| Isa 52:7 | good news | HVprmsa | none recorded | 18009, 19171, 19178 | 0 | How beautiful upon the mountains are the feet of him who brings **good news**, who publishes peace, who brings good news of happiness, who publishes salvation, who says to Zion, “ Your God reigns.” |
| Isa 52:7 | good news | HVprmsa | none recorded | 18009, 19171, 19178 | 0 | How beautiful upon the mountains are the feet of him who brings **good news**, who publishes peace, who brings good news of happiness, who publishes salvation, who says to Zion, “ Your God reigns.” |
| Isa 60:6 | good news | HVpi3mp | none recorded | - | 0 | A multitude of camels shall cover you, the young camels of Midian and Ephah; all those from Sheba shall come. They shall bring gold and frankincense, and shall bring **good news**, the praises of the Lord. |
| Nah 1:15 | good news | HVprmsa | none recorded | - | 0 | Behold, upon the mountains, the feet of him who brings **good news**, who publishes peace! Keep your feasts, O Judah; fulfill your vows, for never again shall the worthless pass through you; he is utterly cut off. |

### 3.17 H5197 נָטַף na.taph "to drip/prophesy": 7 own occurrences in 5 verses

- **Meaning as stored:** Hebrew; native word נָטַף, transliteration na.taph; STEP gloss "to drip/prophesy"; sense head "to drip/prophesy" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5197):** to drop, drip, distil, prophesy, preach, discourse.
- **Related terms (5):** H5188 ne.ti.phah "pendant"; H5198A na.taph "drop"; H5198B na.taph "gum"; H5199 ne.to.phah "Netophah"; H5200 ne.to.pha.ti "Netophathite".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (medium).
- **Counts, three measures as stored:** STEP token count 18; verses STEP attests 0; verse_lexical rows the parse found 18.

- **Carried by the member words:** preach (7).
- **Engagement of these occurrences:** none recorded 7.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 20:46 | preach | HVhv2ms | none recorded | - | 0 | “ Son of man, set your face toward the southland; **preach** against the south, and prophesy against the forest land in the Negeb. |
| Eze 21:2 | preach | HVhv2ms | none recorded | - | 0 | “ Son of man, set your face toward Jerusalem and **preach** against the sanctuaries. Prophesy against the land of Israel |
| Amo 7:16 | preach | HVhi2ms | none recorded | - | 0 | Now therefore hear the word of the Lord. “ You say, ‘Do not prophesy against Israel, and do not **preach** against the house of Isaac.’ |
| Mic 2:6 | preach | HVhi2mp | none recorded | - | 0 | “Do not **preach** ”—thus they preach — “one should not preach of such things; disgrace will not overtake us.” |
| Mic 2:6 | preach | HVhi3mp | none recorded | - | 0 | “Do not **preach** ”—thus they preach — “one should not preach of such things; disgrace will not overtake us.” |
| Mic 2:6 | preach | HVhi3mp | none recorded | - | 0 | “Do not **preach** ”—thus they preach — “one should not preach of such things; disgrace will not overtake us.” |
| Mic 2:11 | preach | HVhi1cs | none recorded | - | 0 | If a man should go about and utter wind and lies, saying, “I will **preach** to you of wine and strong drink,” he would be the preacher for this people! |

### 3.18 G0518 ἀπαγγέλλω apangellō "to announce": 6 own occurrences in 6 verses

- **Meaning as stored:** Greek; native word ἀπαγγέλλω, transliteration apangellō; STEP gloss "to announce"; sense head "to announce" (the code is its own lemma).
- **Related terms (3):** G0032G angelos "angel"; G0032H angelos "angel: messenger"; G0575 apo "away from".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 263; verses STEP attests 46; verse_lexical rows the parse found 47.

- **Carried by the member words:** proclaim (3), declared (2), declare (1).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 14:25 | declare | V-PAP-NSM | none recorded | - | 0 | the secrets of his heart are disclosed, and so, falling on his face, he will worship God and **declare** that God is really among you. |
| Luk 8:47 | declared | V-AAI-3S | none recorded | - | 0 | And when the woman saw that she was not hidden, she came trembling, and falling down before him **declared** in the presence of all the people why she had touched him, and how she had been immediately healed. |
| Act 26:20 | declared | V-IAI-1S | none recorded | - | 0 | but **declared** first to those in Damascus, then in Jerusalem and throughout all the region of Judea, and also to the Gentiles, that they should repent and turn to God, performing deeds in keeping with their repentance. |
| Mat 12:18 | proclaim | V-FAI-3S | none recorded | - | 0 | “ Behold, my servant whom I have chosen, my beloved with whom my soul is well pleased. I will put my Spirit upon him, and he will **proclaim** justice to the Gentiles. |
| 1Jo 1:2 | proclaim | V-PAI-1P | none recorded | - | 0 | the life was made manifest, and we have seen it, and testify to it and **proclaim** to you the eternal life, which was with the Father and was made manifest to us — |
| 1Jo 1:3 | proclaim | V-PAI-1P | none recorded | - | 0 | that which we have seen and heard we **proclaim** also to you, so that you too may have fellowship with us; and indeed our fellowship is with the Father and with his Son Jesus Christ. |

### 3.19 G2782 κήρυγμα kērugma "preaching": 6 own occurrences in 6 verses

- **Meaning as stored:** Greek; native word κήρυγμα, transliteration kērugma; STEP gloss "preaching"; sense head "preaching" (the code is its own lemma).
- **Related terms (1):** G2784 kērussō "to preach".
- **Clusters (cluster_strong):** T2 Supplementary (high).
- **Counts, three measures as stored:** STEP token count 12; verses STEP attests 0; verse_lexical rows the parse found 8.

- **Carried by the member words:** preaching (5), preach (1).
- **Engagement of these occurrences:** none recorded 6.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Cor 1:21 | preach | N-GSN | none recorded | - | 0 | For since, in the wisdom of God, the world did not know God through wisdom, it pleased God through the folly of what we **preach** to save those who believe. |
| Mat 12:41 | preaching | N-ASN | none recorded | - | 0 | The men of Nineveh will rise up at the judgment with this generation and condemn it, for they repented at the **preaching** of Jonah, and behold, something greater than Jonah is here. |
| Luk 11:32 | preaching | N-ASN | none recorded | - | 0 | The men of Nineveh will rise up at the judgment with this generation and condemn it, for they repented at the **preaching** of Jonah, and behold, something greater than Jonah is here. |
| Rom 16:25 | preaching | N-ASN | none recorded | - | 0 | Now to him who is able to strengthen you according to my gospel and the **preaching** of Jesus Christ, according to the revelation of the mystery that was kept secret for long ages |
| 1Cor 15:14 | preaching | N-NSN | none recorded | - | 0 | And if Christ has not been raised, then our **preaching** is in vain and your faith is in vain. |
| Tit 1:3 | preaching | N-DSN | none recorded | - | 0 | and at the proper time manifested in his word through the **preaching** with which I have been entrusted by the command of God our Savior; |

### 3.20 G3870 παρακαλέω parakaleō "to plead/comfort": 4 own occurrences in 4 verses

- **Meaning as stored:** Greek; native word παρακαλέω, transliteration parakaleō; STEP gloss "to plead/comfort"; sense head "to plead/comfort" (the code is its own lemma).
- **Related terms (4):** G2564G kaleō "to call: call"; G2564H kaleō "to call: name"; G3844 para "from/with/beside"; G3874 paraklēsis "encouragement".
- **Clusters (cluster_strong):** M42 Prayer & Petition (heuristic).
- **Counts, three measures as stored:** STEP token count 202; verses STEP attests 105; verse_lexical rows the parse found 109.

- **Carried by the member words:** exhorted (2), exhorting (1), exhorts (1).
- **Engagement of these occurrences:** none recorded 4.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 11:23 | exhorted | V-IAI-3S | none recorded | 20014 | 0 | When he came and saw the grace of God, he was glad, and he **exhorted** them all to remain faithful to the Lord with steadfast purpose, |
| 1Th 2:12 | exhorted | V-PAP-NPM | none recorded | - | 0 | we **exhorted** each one of you and encouraged you and charged you to walk in a manner worthy of God, who calls you into his own kingdom and glory. |
| 1Pe 5:12 | exhorting | V-PAP-NSM | none recorded | - | 0 | By Silvanus, a faithful brother as I regard him, I have written briefly to you, **exhorting** and declaring that this is the true grace of God. Stand firm in it. |
| Rom 12:8 | exhorts | V-PAP-NSM | none recorded | - | 19 | the one who **exhorts**, in his exhortation; the one who contributes, in generosity; the one who leads, with zeal; the one who does acts of mercy, with cheerfulness. |

### 3.21 H2331 חָוָה cha.vah "to explain": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word חָוָה, transliteration cha.vah; STEP gloss "to explain"; sense head "to explain" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2331):** (Piel) to tell, declare, show, make known; (CLBL) to breath.
- **Related terms (4):** H0262 ach.vah "declaration"; H2324 cha.vah "to show"; H2332 chav.vah "Eve"; H2421 cha.yah "to live".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 6; verses STEP attests 6; verse_lexical rows the parse found 6.

- **Carried by the member words:** declare (3).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 32:6 | declare | HVpcc | none recorded | - | 0 | And Elihu the son of Barachel the Buzite answered and said: “I am young in years, and you are aged; therefore I was timid and afraid to **declare** my opinion to you. |
| Job 32:10 | declare | HVpi1cs | none recorded | - | 0 | Therefore I say, ‘ Listen to me; let me also **declare** my opinion.’ |
| Job 32:17 | declare | HVpi1cs | none recorded | - | 0 | I also will answer with my share; I also will **declare** my opinion. |

### 3.22 H3045 יָדַע ya.da "to know": 3 own occurrences in 3 verses

- **Meaning as stored:** Hebrew; native word יָדַע, transliteration ya.da; STEP gloss "to know"; sense head "to know" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H3045):** to know.
- **Related terms (21):** H1843 de.a "knowledge"; H1844 de.ah "knowledge"; H1845 de.u.el "Deuel"; H1847 da.at "knowledge"; H3037G yad.du.a "Jaddua"; H3037H yad.du.a "Jaddua"; more in the workbook.
- **Clusters (cluster_strong):** M15 Knowing & Understanding (None).
- **Counts, three measures as stored:** STEP token count 974; verses STEP attests 874; verse_lexical rows the parse found 946.

- **Carried by the member words:** declared (2), declare (1).
- **Engagement of these occurrences:** none recorded 3.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eze 22:2 | declare | HVhq2ms | none recorded | - | 0 | “And you, son of man, will you judge, will you judge the bloody city? Then **declare** to her all her abominations. |
| Neh 8:12 | declared | HVhp3cp | none recorded | - | 0 | And all the people went their way to eat and drink and to send portions and to make great rejoicing, because they had understood the words that were **declared** to them. |
| Job 26:3 | declared | HVhp2ms | none recorded | - | 0 | How you have counseled him who has no wisdom, and plentifully **declared** sound knowledge! |

### 3.23 G1229 διαγγέλλω diangellō "to proclaim": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word διαγγέλλω, transliteration diangellō; STEP gloss "to proclaim"; sense head "to proclaim" (the code is its own lemma).
- **Related terms (3):** G0032G angelos "angel"; G0032H angelos "angel: messenger"; G1223 dia "through/because of".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 0; verse_lexical rows the parse found 3.

- **Carried by the member words:** proclaim (1), proclaimed (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 9:60 | proclaim | V-PAM-2S | none recorded | - | 0 | And Jesus said to him, “ Leave the dead to bury their own dead. But as for you, go and **proclaim** the kingdom of God.” |
| Rom 9:17 | proclaimed | V-2APS-3S | none recorded | - | 0 | For the Scripture says to Pharaoh, “ For this very purpose I have raised you up, that I might show my power in you, and that my name might be **proclaimed** in all the earth.” |

### 3.24 G1334 διηγέομαι diēgeomai "to relate fully": 2 own occurrences in 2 verses

- **Meaning as stored:** Greek; native word διηγέομαι, transliteration diēgeomai; STEP gloss "to relate fully"; sense head "to relate fully" (the code is its own lemma).
- **Related terms (9):** G1223 dia "through/because of"; G1335 diēgēsis "narrative"; G2230 hēgemoneuō "to govern"; G2231 hēgemonia "reign"; G2232 hēgemōn "ruler"; G2233 hēgeomai "to govern"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 54; verses STEP attests 8; verse_lexical rows the parse found 8.

- **Carried by the member words:** declare (1), declared (1).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 8:39 | declare | V-PNM-2S | none recorded | - | 0 | “ Return to your home, and **declare** how much God has done for you.” And he went away, proclaiming throughout the whole city how much Jesus had done for him. |
| Act 9:27 | declared | V-ADI-3S | none recorded | - | 0 | But Barnabas took him and brought him to the apostles and **declared** to them how on the road he had seen the Lord, who spoke to him, and how at Damascus he had preached boldly in the name of Jesus. |

### 3.25 H0560 אֲמַר a.mar "to say": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word אֲמַר, transliteration a.mar; STEP gloss "to say"; sense head "to say" (the code is its own lemma).
- **Related terms (3):** H0559 a.mar "to say"; H0563 im.mar "lamb"; H3983 me.mar "command".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 71; verses STEP attests 65; verse_lexical rows the parse found 71.

- **Carried by the member words:** declared (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 3:24 | declared | AVqrmsa | none recorded | - | 0 | Then King Nebuchadnezzar was astonished and rose up in haste. He **declared** to his counselors, “Did we not cast three men bound into the fire?” They answered and said to the king, “ True, O king.” |
| Dan 7:2 | declared | AVqrmsa | none recorded | - | 0 | Daniel **declared**, “I saw in my vision by night, and behold, the four winds of heaven were stirring up the great sea. |

### 3.26 H2372 חָזָה cha.zah "to see": 2 own occurrences in 1 verse

- **Meaning as stored:** Hebrew; native word חָזָה, transliteration cha.zah; STEP gloss "to see"; sense head "to see" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2372):** to see, perceive, look, behold, prophesy, provide.
- **Related terms (21):** H1957 ha.zah "to dream"; H2335 cho.zay "seer"; H2370 cha.zah "to see"; H2371 cha.za.h.el "Hazael"; H2374 cho.zeh "seer"; H2377 cha.zon "vision"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 55; verses STEP attests 51; verse_lexical rows the parse found 55.

- **Carried by the member words:** prophesy (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 30:10 | prophesy | HVqi2mp | none recorded | - | 0 | who say to the seers, “Do not see,” and to the prophets, “Do not **prophesy** to us what is right; speak to us smooth things, prophesy illusions, |
| Isa 30:10 | prophesy | HVqv2mp | none recorded | - | 0 | who say to the seers, “Do not see,” and to the prophets, “Do not **prophesy** to us what is right; speak to us smooth things, prophesy illusions, |

### 3.27 H5030 נָבִיא na.vi "prophet": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word נָבִיא, transliteration na.vi; STEP gloss "prophet"; sense head "prophet" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5030):** spokesman, speaker, prophet.
- **Related terms (4):** H5012 na.va "to prophesy"; H5016 ne.vu.ah "prophecy"; H5029 ne.vi "prophet"; H5031 ne.vi.ah "prophetess".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (medium).
- **Counts, three measures as stored:** STEP token count 322; verses STEP attests 287; verse_lexical rows the parse found 315.

- **Carried by the member words:** prophesy (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 23:26 | prophesy | HNcmpc | none recorded | 16020, 17240 | 0 | How long shall there be lies in the heart of the prophets who **prophesy** lies, and who prophesy the deceit of their own heart, |
| Eze 13:2 | prophesy | HNcmpc | none recorded | 16020, 17240 | 0 | “ Son of man, **prophesy** against the prophets of Israel, who are prophesying, and say to those who prophesy from their own hearts: ‘ Hear the word of the Lord!’ |

### 3.28 H7123 קְרָא qe.ra "to read": 2 own occurrences in 2 verses

- **Meaning as stored:** Hebrew; native word קְרָא, transliteration qe.ra; STEP gloss "to read"; sense head "to read" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7123):** to call, read aloud, read out, shout.
- **Related terms (10):** H4744 miq.ra "assembly"; H6981G qo.re "Kore"; H6981H qo.re "Kore"; H7121G qa.ra "to call: call to"; H7121H qa.ra "to call: call by"; H7121I qa.ra "to call: call out"; more in the workbook.
- **Clusters (cluster_strong):** M37 Firstborn & Foreknowledge (None).
- **Counts, three measures as stored:** STEP token count 11; verses STEP attests 10; verse_lexical rows the parse found 11.

- **Carried by the member words:** proclaimed (2).
- **Engagement of these occurrences:** none recorded 2.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 3:4 | proclaimed | AVqrmsa | none recorded | - | 0 | And the herald **proclaimed** aloud, “You are commanded, O peoples, nations, and languages, |
| Dan 4:14 | proclaimed | AVqrmsa | none recorded | - | 0 | He **proclaimed** aloud and said thus: ‘ Chop down the tree and lop off its branches, strip off its leaves and scatter its fruit. Let the beasts flee from under it and the birds from its branches. |

### 3.29 G0584 ἀποδείκνυμι apodeiknumi "to display": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀποδείκνυμι, transliteration apodeiknumi; STEP gloss "to display"; sense head "to display" (the code is its own lemma).
- **Related terms (3):** G0575 apo "away from"; G0585 apodeixis "demonstration"; G1166 deiknuō "to show".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** proclaiming (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 2Th 2:4 | proclaiming | V-PAP-ASM | none recorded | - | 0 | who opposes and exalts himself against every so-called god or object of worship, so that he takes his seat in the temple of God, **proclaiming** himself to be God. |

### 3.30 G0611 ἀποκρίνω apokrinō "to answer": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἀποκρίνω, transliteration apokrinō; STEP gloss "to answer"; sense head "to answer" (the code is its own lemma).
- **Related terms (5):** G0470 antapokrinomai "to contradict"; G0575 apo "away from"; G0610 apokrima "verdict"; G0612 apokrisis "answer"; G2919 krinō "to judge".
- **Clusters (cluster_strong):** M41 Being Heard (heuristic).
- **Counts, three measures as stored:** STEP token count 490; verses STEP attests 0; verse_lexical rows the parse found 223.

- **Carried by the member words:** declared (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 10:46 | declared | V-ADI-3S | none recorded | - | 0 | For they were hearing them speaking in tongues and extolling God. Then Peter **declared**, |

### 3.31 G1107 γνωρίζω gnōrizō "to make known": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word γνωρίζω, transliteration gnōrizō; STEP gloss "to make known"; sense head "to make known" (the code is its own lemma).
- **Related terms (23):** G0050 agnoeō "be ignorant"; G0052 agnoia "ignorance"; G0056 agnōsia "ignorance"; G0057 agnōstos "unknown"; G0314 anaginōskō "to read"; G0319 anagnōrizō "to recognize"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 90; verses STEP attests 23; verse_lexical rows the parse found 24.

- **Carried by the member words:** proclaim (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 6:19 | proclaim | V-AAN | none recorded | - | 0 | and also for me, that words may be given to me in opening my mouth boldly to **proclaim** the mystery of the gospel, |

### 3.32 G1344 δικαιόω dikaioō "to justify": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word δικαιόω, transliteration dikaioō; STEP gloss "to justify"; sense head "to justify" (the code is its own lemma).
- **Related terms (17):** G0091 adikeō "to harm"; G0092 adikēma "crime"; G0093 adikia "unrighteousness"; G0094 adikos "unjust"; G0095 adikōs "unjustly"; G0476 antidikos "opponent"; more in the workbook.
- **Clusters (cluster_strong):** M26 Judgment & Condemnation (None).
- **Counts, three measures as stored:** STEP token count 71; verses STEP attests 36; verse_lexical rows the parse found 40.

- **Carried by the member words:** declared (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Luk 7:29 | declared | V-AAI-3P | none recorded | 19419 | 0 | ( When all the people heard this, and the tax collectors too, they **declared** God just, having been baptized with the baptism of John, |

### 3.33 G1804 ἐξαγγέλλω exangellō "to proclaim": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐξαγγέλλω, transliteration exangellō; STEP gloss "to proclaim"; sense head "to proclaim" (the code is its own lemma).
- **Related terms (3):** G0032G angelos "angel"; G0032H angelos "angel: messenger"; G1537 ek "out from".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 9; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** proclaim (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Pe 2:9 | proclaim | V-AAS-2P | none recorded | - | 0 | But you are a chosen race, a royal priesthood, a holy nation, a people for his own possession, that you may **proclaim** the excellencies of him who called you out of darkness into his marvelous light. |

### 3.34 G1957 ἐπιμαρτυρέω epimartureō "to testify to": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ἐπιμαρτυρέω, transliteration epimartureō; STEP gloss "to testify to"; sense head "to testify to" (the code is its own lemma).
- **Related terms (15):** G0267 amarturos "without witness"; G1263 diamarturomai "to testify solemnly"; G1909 epi "upon/to/against"; G2649 katamartureō "to testify against"; G3140 martureō "to testify"; G3141 marturia "testimony"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** declaring (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Pe 5:12 | declaring | V-PAP-NSM | none recorded | - | 0 | By Silvanus, a faithful brother as I regard him, I have written briefly to you, exhorting and **declaring** that this is the true grace of God. Stand firm in it. |

### 3.35 G2036 εἶπον eipon "to say: said": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word εἶπον, transliteration eipon; STEP gloss "to say: said"; sense head "to say: said" (the code is its own lemma).
- **Related terms (4):** G2036 eipon "to say: said"; G2046 erō "to say: did said"; G4277 proepō "to predict"; G4483 ereō "to say: will say".
- **Clusters (cluster_strong):** T3 Operations (low).
- **Counts, three measures as stored:** STEP token count 4466; verses STEP attests 834; verse_lexical rows the parse found 896.

- **Carried by the member words:** declared (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mar 12:36 | declared | V-2AAI-3S | none recorded | - | 0 | David himself, in the Holy Spirit, **declared**, “‘The Lord said to my Lord, “ Sit at my right hand, until I put your enemies under your feet.”’ |

### 3.36 G3056 λόγος logos "word": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word λόγος, transliteration logos; STEP gloss "word"; sense head "word" (the code is its own lemma).
- **Related terms (9):** G0945 battologeō "to babble"; G1351 dilogos "insincere"; G3004G legō "to say: says"; G3004H legō "to say: name"; G3050 logikos "spiritual"; G3051 logion "oracles"; more in the workbook.
- **Clusters (cluster_strong):** M65 Speech & Tongue (heuristic).
- **Counts, three measures as stored:** STEP token count 1298; verses STEP attests 317; verse_lexical rows the parse found 330.

- **Carried by the member words:** preaching (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| 1Ti 5:17 | preaching | N-DSM | none recorded | - | 0 | Let the elders who rule well be considered worthy of double honor, especially those who labor in **preaching** and teaching. |

### 3.37 G3670 ὁμολογέω homologeō "to confess/profess": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ὁμολογέω, transliteration homologeō; STEP gloss "to confess/profess"; sense head "to confess/profess" (the code is its own lemma).
- **Related terms (6):** G0437 anthomologeomai "to praise"; G1843 exomologeomai "to agree"; G3056 logos "word"; G3671 homologia "confession"; G3672 homologoumenōs "undeniably"; G3674 homou "together".
- **Clusters (cluster_strong):** T3 Operations (low); M60 Confession & Forgiveness (high).
- **Counts, three measures as stored:** STEP token count 27; verses STEP attests 22; verse_lexical rows the parse found 25.

- **Carried by the member words:** declare (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mat 7:23 | declare | V-FAI-1S | none recorded | - | 0 | And then will I **declare** to them, ‘I never knew you; depart from me, you workers of lawlessness.’ |

### 3.38 G3724 ὁρίζω horizō "to determine": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word ὁρίζω, transliteration horizō; STEP gloss "to determine"; sense head "to determine" (the code is its own lemma).
- **Related terms (3):** G0873 aforizō "to separate"; G3725 horion "region"; G4309 proorizō "to predestine".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 28; verses STEP attests 8; verse_lexical rows the parse found 8.

- **Carried by the member words:** declared (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rom 1:4 | declared | V-APP-GSM | none recorded | - | 0 | and was **declared** to be the Son of God in power according to the Spirit of holiness by his resurrection from the dead, Jesus Christ our Lord, |

### 3.39 G4293 προκαταγγέλλω prokatangellō "to foretell": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προκαταγγέλλω, transliteration prokatangellō; STEP gloss "to foretell"; sense head "to foretell" (the code is its own lemma).
- **Related terms (2):** G2605 katangellō "to proclaim"; G4253 pro "before".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** proclaimed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 3:24 | proclaimed | V-AAI-3P | none recorded | - | 0 | And all the prophets who have spoken, from Samuel and those who came after him, also **proclaimed** these days. |

### 3.40 G4296 προκηρύσσω prokērussō "to announce": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προκηρύσσω, transliteration prokērussō; STEP gloss "to announce"; sense head "to announce" (the code is its own lemma).
- **Related terms (2):** G2784 kērussō "to preach"; G4253 pro "before".
- **Clusters (cluster_strong):** T3 Operations (None).
- **Counts, three measures as stored:** STEP token count 2; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** proclaimed (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Act 13:24 | proclaimed | V-AAP-GSM | none recorded | - | 0 | Before his coming, John had **proclaimed** a baptism of repentance to all the people of Israel. |

### 3.41 G4388 προτίθημι protithēmi "to plan/present": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προτίθημι, transliteration protithēmi; STEP gloss "to plan/present"; sense head "to plan/present" (the code is its own lemma).
- **Related terms (11):** G0111 athemitos "unlawful"; G0394 anatithēmi "to set before"; G0475 antidiatithēmi "to oppose"; G1303 diatithēmi "to make a covenant"; G2652 katanathema "curse"; G2653 katanathematizō "to curse"; more in the workbook.
- **Clusters (cluster_strong):** M64 Will & Resolve (heuristic).
- **Counts, three measures as stored:** STEP token count 13; verses STEP attests 3; verse_lexical rows the parse found 3.

- **Carried by the member words:** set forth (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Eph 1:9 | set forth | V-2AMI-3S | none recorded | 12524, 19417 | 0 | making known to us the mystery of his will, according to his purpose, which he **set forth** in Christ |

### 3.42 G4394 προφητεία profēteia "prophecy": 1 own occurrence in 1 verse

- **Meaning as stored:** Greek; native word προφητεία, transliteration profēteia; STEP gloss "prophecy"; sense head "prophecy" (the code is its own lemma).
- **Related terms (5):** G4395 profēteuō "to prophesy"; G4396 profētēs "prophet"; G4397 profētikos "prophetic"; G4398 profētis "prophetess"; G5578 pseudoprofētēs "false prophet".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (None).
- **Counts, three measures as stored:** STEP token count 27; verses STEP attests 19; verse_lexical rows the parse found 19.

- **Carried by the member words:** prophesying (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Rev 11:6 | prophesying | N-GSF | none recorded | 18234 | 0 | They have the power to shut the sky, that no rain may fall during the days of their **prophesying**, and they have power over the waters to turn them into blood and to strike the earth with every kind of plague, as often as they desire. |

### 3.43 H2142 זָכַר za.khar "to remember": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word זָכַר, transliteration za.khar; STEP gloss "to remember"; sense head "to remember" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H2142):** to remember, recall, call to mind.
- **Related terms (51):** H0234 az.ka.rah "memorial"; H2138 za.khur "male"; H2139G zak.kur "Zaccur"; H2139H zak.kur "Zaccur"; H2139I zak.kur "Zaccur"; H2139J zak.kur "Zaccur"; more in the workbook.
- **Clusters (cluster_strong):** M81 Memory (act) (heuristic).
- **Counts, three measures as stored:** STEP token count 245; verses STEP attests 223; verse_lexical rows the parse found 232.

- **Carried by the member words:** proclaim (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 12:4 | proclaim | HVhv2mp | none recorded | - | 0 | And you will say in that day: “Give thanks to the Lord, call upon his name, make known his deeds among the peoples, **proclaim** that his name is exalted. |

### 3.44 H4448A מָלַל ma.lal "to speak": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word מָלַל, transliteration ma.lal; STEP gloss "to speak"; sense head "to speak" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H4448):** to speak, utter, say.
- **Related terms (5):** H4405 mil.lah "speech"; H4413 mal.lo.ti "Mallothi"; H4448B ma.lal "to rub"; H4449 me.lal "to speak"; H4450 mi.la.lay "Milalai".
- **Clusters (cluster_strong):** T3 Operations (medium).
- **Counts, three measures as stored:** STEP token count 4; verses STEP attests 4; verse_lexical rows the parse found 4.

- **Carried by the member words:** declare (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 33:3 | declare | HVpp3cp | none recorded | - | 0 | My words **declare** the uprightness of my heart, and what my lips know they speak sincerely. |

### 3.45 H5001 נָאַם na.am "to prophesy": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נָאַם, transliteration na.am; STEP gloss "to prophesy"; sense head "to prophesy" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5001):** to prophesy, utter a prophecy, speak as prophet, say.
- **Related terms (1):** H5002 ne.um "utterance".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** declare (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Jer 23:31 | declare | HVqw3mp | none recorded | - | 0 | Behold, I am against the prophets, declares the Lord, who use their tongues and **declare**, ‘ declares the Lord.’ |

### 3.46 H5013 נְבָא ne.va "to prophesy": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נְבָא, transliteration ne.va; STEP gloss "to prophesy"; sense head "to prophesy" (the code is its own lemma).
- **Related terms (6):** H5012 na.va "to prophesy"; H5017 ne.vu.ah "prophesying"; H5020 ne.vu.khad.rets.tsar ne.vu.khad.nets.tsar "Nebuchadnezzar"; H5023 ne.viz.bah "reward"; H5029 ne.vi "prophet"; H5043 nev.rash.ta "lampstand".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (heuristic).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 0; verse_lexical rows the parse found 1.

- **Carried by the member words:** prophesied (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ezr 5:1 | prophesied | AVMp3ms | none recorded | - | 0 | Now the prophets, Haggai and Zechariah the son of Iddo, **prophesied** to the Jews who were in Judah and Jerusalem, in the name of the God of Israel who was over them. |

### 3.47 H5017 נְבוּאָה ne.vu.ah "prophesying": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word נְבוּאָה, transliteration ne.vu.ah; STEP gloss "prophesying"; sense head "prophesying" (the code is its own lemma).
- **Related terms (6):** H5013 ne.va "to prophesy"; H5016 ne.vu.ah "prophecy"; H5020 ne.vu.khad.rets.tsar ne.vu.khad.nets.tsar "Nebuchadnezzar"; H5023 ne.viz.bah "reward"; H5029 ne.vi "prophet"; H5043 nev.rash.ta "lampstand".
- **Clusters (cluster_strong):** M43 Prophecy & Vision (None).
- **Counts, three measures as stored:** STEP token count 1; verses STEP attests 1; verse_lexical rows the parse found 1.

- **Carried by the member words:** prophesying (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Ezr 6:14 | prophesying | ANcfsc | none recorded | - | 0 | And the elders of the Jews built and prospered through the **prophesying** of Haggai the prophet and Zechariah the son of Iddo. They finished their building by decree of the God of Israel and by decree of Cyrus and Darius and Artaxerxes king of Persia; |

### 3.48 H5674A עָבַר a.var "to pass": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עָבַר, transliteration a.var; STEP gloss "to pass"; sense head "to pass" (the code is its own lemma).
- **Related terms (24):** H4569A ma.a.var "ford"; H4569B ma.a.va.rah "ford"; H5668 a.vur "for the sake of"; H5669 a.vur "produce"; H5674B a.var "be angry"; H5674C a.var "to pass: bring"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 513; verses STEP attests 441; verse_lexical rows the parse found 498.

- **Carried by the member words:** proclaim (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Neh 8:15 | proclaim | HVhu3mp | none recorded | - | 0 | and that they should **proclaim** it and publish it in all their towns and in Jerusalem, “ Go out to the hills and bring branches of olive, wild olive, myrtle, palm, and other leafy trees to make booths, as it is written.” |

### 3.49 H5921A עַל al "upon": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עַל, transliteration al; STEP gloss "upon"; sense head "upon" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H5921):** upon, on the ground of, according to, on account of, on behalf of, con ... (cut; the whole text is in the workbook).
- **Related terms (38):** H0131 a.dum.mim "Adummim"; H3588A ki "for"; H3588B ki m "that if: except"; H3588C ki al ken "for as that: since"; H3651C ken "so"; H3652 ken "thus"; more in the workbook.
- **Clusters (cluster_strong):** T2 Supplementary (medium).
- **Counts, three measures as stored:** STEP token count 5802; verses STEP attests 4481; verse_lexical rows the parse found 5764.

- **Carried by the member words:** declare (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 36:33 | declare | HR | none recorded | - | 0 | Its crashing declares his presence; the cattle also **declare** that he rises. |

### 3.50 H6032 עֲנָה a.nah "to answer": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word עֲנָה, transliteration a.nah; STEP gloss "to answer"; sense head "to answer" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H6032):** to answer, respond.
- **Related terms (5):** H3705 ke.an "now"; H3706 ke.e.net "now"; H6030A un "to dwell"; H6030B a.nah "to answer"; H6030C a.nah "to sing".
- **Clusters (cluster_strong):** M41 Being Heard (heuristic).
- **Counts, three measures as stored:** STEP token count 30; verses STEP attests 0; verse_lexical rows the parse found 30.

- **Carried by the member words:** declared (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Dan 5:7 | declared | AVqrmsa | none recorded | - | 0 | The king called loudly to bring in the enchanters, the Chaldeans, and the astrologers. The king **declared** to the wise men of Babylon, “ Whoever reads this writing, and shows me its interpretation, shall be clothed with purple and have a chain of gold around his neck and shall be the third ruler in the kingdom.” |

### 3.51 H6942J קָדַשׁ qa.dash "to consecrate: prepare": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word קָדַשׁ, transliteration qa.dash; STEP gloss "to consecrate: prepare"; sense head "prepare/set apart".
- **Senses (first level of the meaning tree of the lemma H6942):** to consecrate, sanctify, prepare, dedicate, be hallowed, be holy, be s ... (cut; the whole text is in the workbook).
- **Related terms (21):** H4720 miq.dash "sanctuary"; H6918G qa.dosh "holy"; H6918H qa.dosh "holy: saint"; H6922 qad.dish "holy"; H6942G qa.dash "to consecrate: consecate"; H6942H qa.dash "to consecrate: dedicate"; more in the workbook.
- **Clusters (cluster_strong):** M61 Purity & Holiness (heuristic).
- **Counts, three measures as stored:** STEP token count 7; verses STEP attests 7; verse_lexical rows the parse found 7.

- **Carried by the member words:** declare (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Mic 3:5 | declare | HVpq3cp | none recorded | - | 0 | Thus says the Lord concerning the prophets who lead my people astray, who cry “ Peace ” when they have something to eat, but **declare** war against him who puts nothing into their mouths. |

### 3.52 H7126G קָרַב qa.rav "to present: come": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word קָרַב, transliteration qa.rav; STEP gloss "to present: come"; sense head "come/approach".
- **Senses (first level of the meaning tree of the lemma H7126):** to come near, approach, enter into, draw near.
- **Related terms (10):** H7126H qa.rav "to present: bring"; H7127 qe.rev "to approach"; H7128 qe.rav "battle"; H7130G qe.rev "entrails: among"; H7130H qe.rev "entrails: inner parts"; H7131 qa.rev "approaching"; more in the workbook.
- **Clusters (cluster_strong):** T3 Operations (high).
- **Counts, three measures as stored:** STEP token count 112; verses STEP attests 0; verse_lexical rows the parse found 112.

- **Carried by the member words:** set forth (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Isa 41:21 | set forth | HVpv2mp | none recorded | - | 0 | **Set forth** your case, says the Lord; bring your proofs, says the King of Jacob. |

### 3.53 H7561 רָשַׁע ra.sha "be wicked": 1 own occurrence in 1 verse

- **Meaning as stored:** Hebrew; native word רָשַׁע, transliteration ra.sha; STEP gloss "be wicked"; sense head "be wicked" (the code is its own lemma).
- **Senses (first level of the meaning tree of the lemma H7561):** to be wicked, act wickedly.
- **Related terms (4):** H4849 mir.sha.at "wickedness"; H7562 re.sha "wickedness"; H7563 ra.sha "wicked"; H7564 rish.ah "wickedness".
- **Clusters (cluster_strong):** M58 Wickedness (heuristic).
- **Counts, three measures as stored:** STEP token count 37; verses STEP attests 34; verse_lexical rows the parse found 34.

- **Carried by the member words:** declared (1).
- **Engagement of these occurrences:** none recorded 1.

| reference | member word | morph | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|
| Job 32:3 | declared | HVhw3mp | none recorded | 14207, 20305 | 0 | He burned with anger also at Job’s three friends because they had found no answer, although they had **declared** Job to be in the wrong. |

### 3.54 Occurrences where the member surface is shared with another code's unit (194)

In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.

| reference | member word | code | unit word | unit role | unit size | engagement | other observations | catalogue observations | verse (ESV) |
|---|---|---|---|---|---|---|---|---|---|
| Mat 11:25 | declared | G0611 ἀποκρίνω apokrinō "to answer" | declared | content_part | 2 | none recorded | - | 0 | At that time Jesus **declared**, “I thank you, Father, Lord of heaven and earth, that you have hidden these things from the wise and understanding and revealed them to little children; |
| Mat 4:17 | preach | G2532 καί kai "and" | preach | content_part | 2 | none recorded | - | 0 | From that time Jesus began to **preach**, saying, “ Repent, for the kingdom of heaven is at hand.” |
| Joh 7:28 | proclaimed | G2896 κράζω krazō "to cry" | proclaimed | content_part | 2 | none recorded | - | 0 | So Jesus **proclaimed**, as he taught in the temple, “You know me, and you know where I come from. But I have not come of my own accord. He who sent me is true, and him you do not know. |
| Mat 11:25 | declared | G3004G λέγω legō "to say: says" | declared | content_part | 2 | none recorded | - | 0 | At that time Jesus **declared**, “I thank you, Father, Lord of heaven and earth, that you have hidden these things from the wise and understanding and revealed them to little children; |
| Joh 7:28 | proclaimed | G3004G λέγω legō "to say: says" | proclaimed | content_part | 2 | none recorded | - | 0 | So Jesus **proclaimed**, as he taught in the temple, “You know me, and you know where I come from. But I have not come of my own accord. He who sent me is true, and him you do not know. |
| Jer 50:21 | declares | H0310A אַחַר a.char "after" | declares | content_part | 3 | none recorded | - | 0 | “Go up against the land of Merathaim, and against the inhabitants of Pekod. Kill, and devote them to destruction, **declares** the Lord, and do all that I have commanded you. |
| Psa 40:5 | proclaim | H0413 אֶל el "to[wards]" | proclaim | content_part | 3 | none recorded | - | 0 | You have multiplied, O Lord my God, your wondrous deeds and your thoughts toward us; none can compare with you! I will **proclaim** and tell of them, yet they are more than can be told. |
| Jer 2:3 | declares | H0413 אֶל el "to[wards]" | declares | content_part | 3 | none recorded | - | 0 | Israel was holy to the Lord, the firstfruits of his harvest. All who ate of it incurred guilt; disaster came upon them, **declares** the Lord.” |
| Jer 2:19 | declares | H0413 אֶל el "to[wards]" | declares | content_part | 4 | none recorded | - | 0 | Your evil will chastise you, and your apostasy will reprove you. Know and see that it is evil and bitter for you to forsake the Lord your God; the fear of me is not in you, **declares** the Lord God of hosts. |
| Jer 3:1 | declares | H0413 אֶל el "to[wards]" | declares | content_part | 3 | none recorded | - | 0 | “ If a man divorces his wife and she goes from him and becomes another man’s wife, will he return to her? Would not that land be greatly polluted? You have played the whore with many lovers; and would you return to me? **declares** the Lord. |
| Jer 9:12 | declare | H0413 אֶל el "to[wards]" | declare | content_part | 3 | none recorded | - | 0 | Who is the man so wise that he can understand this? To whom has the mouth of the Lord spoken, that he may **declare** it? Why is the land ruined and laid waste like a wilderness, so that no one passes through? |
| Jer 23:21 | prophesied | H0413 אֶל el "to[wards]" | prophesied | content_part | 4 | none recorded | - | 0 | “I did not send the prophets, yet they ran; I did not speak to them, yet they **prophesied**. |
| Jer 30:21 | declares | H0413 אֶל el "to[wards]" | declares | content_part | 3 | none recorded | - | 0 | Their prince shall be one of themselves; their ruler shall come out from their midst; I will make him draw near, and he shall approach me, for who would dare of himself to approach me? **declares** the Lord. |
| Jer 34:17 | proclaiming | H0413 אֶל el "to[wards]" | proclaiming | content_part | 3 | none recorded | - | 0 | “ Therefore, thus says the Lord: You have not obeyed me by **proclaiming** liberty, every one to his brother and to his neighbor; behold, I proclaim to you liberty to the sword, to pestilence, and to famine, declares the Lord. I will make you a horror to all the kingdoms of the earth. |
| Zec 1:4 | declares | H0413 אֶל el "to[wards]" | declares | content_part | 3 | none recorded | - | 0 | Do not be like your fathers, to whom the former prophets cried out, ‘ Thus says the Lord of hosts, Return from your evil ways and from your evil deeds.’ But they did not hear or pay attention to me, **declares** the Lord. |
| Deu 27:14 | declare | H0559 אָמַר a.mar "to say" | declare | content_part | 2 | none recorded | - | 0 | And the Levites shall **declare** to all the men of Israel in a loud voice: |
| Neh 6:7 | proclaim | H0559 אָמַר a.mar "to say" | proclaim | content_part | 3 | none recorded | - | 0 | And you have also set up prophets to **proclaim** concerning you in Jerusalem, ‘There is a king in Judah.’ And now the king will hear of these reports. So now come and let us take counsel together.” |
| Jer 2:2 | proclaim | H0559 אָמַר a.mar "to say" | proclaim | content_part | 2 | none recorded | - | 0 | “ Go and **proclaim** in the hearing of Jerusalem, Thus says the Lord, “I remember the devotion of your youth, your love as a bride, how you followed me in the wilderness, in a land not sown. |
| Jer 5:20 | proclaim | H0559 אָמַר a.mar "to say" | proclaim | content_part | 3 | none recorded | - | 0 | Declare this in the house of Jacob; **proclaim** it in Judah: |
| Dan 2:15 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 2 | none recorded | - | 0 | He **declared** to Arioch, the king’s captain, “ Why is the decree of the king so urgent?” Then Arioch made the matter known to Daniel. |
| Dan 2:26 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 2 | none recorded | - | 0 | The king **declared** to Daniel, whose name was Belteshazzar, “ Are you able to make known to me the dream that I have seen and its interpretation?” |
| Dan 3:9 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 2 | none recorded | - | 0 | They **declared** to King Nebuchadnezzar, “O king, live forever! |
| Dan 3:26 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 3 | none recorded | - | 0 | Then Nebuchadnezzar came near to the door of the burning fiery furnace; he **declared**, “ Shadrach, Meshach, and Abednego, servants of the Most High God, come out, and come here!” Then Shadrach, Meshach, and Abednego came out from the fire. |
| Dan 5:10 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 2 | none recorded | - | 0 | The queen, because of the words of the king and his lords, came into the banqueting hall, and the queen **declared**, “O king, live forever! Let not your thoughts alarm you or your color change. |
| Dan 6:16 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 3 | none recorded | - | 0 | Then the king commanded, and Daniel was brought and cast into the den of lions. The king **declared** to Daniel, “May your God, whom you serve continually, deliver you!” |
| Dan 6:20 | declared | H0560 אֲמַר a.mar "to say" | declared | content_part | 2 | none recorded | - | 0 | As he came near to the den where Daniel was, he cried out in a tone of anguish. The king **declared** to Daniel, “O Daniel, servant of the living God, has your God, whom you serve continually, been able to deliver you from the lions?” |
| Num 14:28 | declares | H0589 אֲנִי a.ni "I" | declares | content_part | 2 | none recorded | - | 0 | Say to them, ‘As I live, **declares** the Lord, what you have said in my hearing I will do to you: |
| Jer 3:12 | declares | H0589 אֲנִי a.ni "I" | declares | content_part | 2 | none recorded | - | 0 | Go, and proclaim these words toward the north, and say, “‘ Return, faithless Israel, **declares** the Lord. I will not look on you in anger, for I am merciful, declares the Lord; I will not be angry forever. |
| Jer 23:23 | declares | H0589 אֲנִי a.ni "I" | declares | content_part | 2 | none recorded | - | 0 | “Am I a God at hand, **declares** the Lord, and not a God far away? |
| Eze 20:31 | declares | H0589 אֲנִי a.ni "I" | declares | content_part | 2 | none recorded | - | 0 | When you present your gifts and offer up your children in fire, you defile yourselves with all your idols to this day. And shall I be inquired of by you, O house of Israel? As I live, **declares** the Lord God, I will not be inquired of by you. |
| Eze 35:11 | declares | H0589 אֲנִי a.ni "I" | declares | content_part | 2 | none recorded | - | 0 | therefore, as I live, **declares** the Lord God, I will deal with you according to the anger and envy that you showed because of your hatred against them. And I will make myself known among them, when I judge you. |
| Zep 2:9 | declares | H0589 אֲנִי a.ni "I" | declares | content_part | 2 | none recorded | - | 0 | Therefore, as I live,” **declares** the Lord of hosts, the God of Israel, “ Moab shall become like Sodom, and the Ammonites like Gomorrah, a land possessed by nettles and salt pits, and a waste forever. The remnant of my people shall plunder them, and the survivors of my nation shall possess them.” |
| 1Ki 8:24 | declared | H0834A אֲשֶׁר a.sher "which" | declared | content_part | 4 | none recorded | - | 0 | you have kept with your servant David my father what you **declared** to him. You spoke with your mouth, and with your hand have fulfilled it this day. |
| 1Ki 8:53 | declared | H0834A אֲשֶׁר a.sher "which" | declared | content_part | 2 | none recorded | - | 0 | For you separated them from among all the peoples of the earth to be your heritage, as you **declared** through Moses your servant, when you brought our fathers out of Egypt, O Lord God.” |
| 2Ki 23:16 | proclaimed | H0834A אֲשֶׁר a.sher "which" | proclaimed | content_part | 2 | none recorded | - | 0 | And as Josiah turned, he saw the tombs there on the mount. And he sent and took the bones out of the tombs and burned them on the altar and defiled it, according to the word of the Lord that the man of God **proclaimed**, who had predicted these things. |
| Jer 25:13 | prophesied | H0834A אֲשֶׁר a.sher "which" | prophesied | content_part | 4 | none recorded | - | 0 | I will bring upon that land all the words that I have uttered against it, everything written in this book, which Jeremiah **prophesied** against all the nations. |
| Zec 7:7 | proclaimed | H0834A אֲשֶׁר a.sher "which" | proclaimed | content_part | 2 | none recorded | - | 0 | Were not these the words that the Lord **proclaimed** by the former prophets, when Jerusalem was inhabited and prosperous, with her cities around her, and the South and the lowland were inhabited?'” |
| 1Ki 8:24 | declared | H0853 אֵת et "[Obj.]" | declared | content_part | 4 | none recorded | - | 0 | you have kept with your servant David my father what you **declared** to him. You spoke with your mouth, and with your hand have fulfilled it this day. |
| Isa 61:1 | good news | H0853 אֵת et "[Obj.]" | good news | content_part | 3 | none recorded | - | 0 | The Spirit of the Lord God is upon me, because the Lord has anointed me to bring **good news** to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives, and the opening of the prison to those who are bound; |
| Jer 8:17 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | For behold, I am sending among you serpents, adders that cannot be charmed, and they shall bite you,” **declares** the Lord. |
| Jer 9:6 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | Heaping oppression upon oppression, and deceit upon deceit, they refuse to know me, **declares** the Lord. |
| Jer 15:6 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | You have rejected me, **declares** the Lord; you keep going backward, so I have stretched out my hand against you and destroyed you— I am weary of relenting. |
| Jer 16:11 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 4 | none recorded | - | 0 | then you shall say to them: ‘ Because your fathers have forsaken me, **declares** the Lord, and have gone after other gods and have served and worshiped them, and have forsaken me and have not kept my law, |
| Jer 22:16 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | He judged the cause of the poor and needy; then it was well. Is not this to know me? **declares** the Lord. |
| Jer 23:33 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | “ When one of this people, or a prophet or a priest asks you, ‘ What is the burden of the Lord?’ you shall say to them, ‘ You are the burden, and I will cast you off, **declares** the Lord.’ |
| Jer 27:22 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 4 | none recorded | - | 0 | They shall be carried to Babylon and remain there until the day when I visit them, **declares** the Lord. Then I will bring them back and restore them to this place.” |
| Jer 29:14 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 4 | none recorded | - | 0 | I will be found by you, **declares** the Lord, and I will restore your fortunes and gather you from all the nations and all the places where I have driven you, declares the Lord, and I will bring you back to the place from which I sent you into exile. |
| Jer 32:5 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 4 | none recorded | - | 0 | And he shall take Zedekiah to Babylon, and there he shall remain until I visit him, **declares** the Lord. Though you fight against the Chaldeans, you shall not succeed ’?” |
| Eze 32:16 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | This is a lamentation that shall be chanted; the daughters of the nations shall chant it; over Egypt, and over all her multitude, shall they chant it, **declares** the Lord God.” |
| Eze 43:27 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | And when they have completed these days, then from the eighth day onward the priests shall offer on the altar your burnt offerings and your peace offerings, and I will accept you, **declares** the Lord God.” |
| Hag 2:17 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 4 | none recorded | - | 0 | I struck you and all the products of your toil with blight and with mildew and with hail, yet you did not turn to me, **declares** the Lord. |
| Zec 2:6 | declares | H0853 אֵת et "[Obj.]" | declares | content_part | 3 | none recorded | - | 0 | Up! Up! Flee from the land of the north, **declares** the Lord. For I have spread you abroad as the four winds of the heavens, declares the Lord. |
| Isa 54:17 | declares | H0854 אֵת et "with" | declares | content_part | 5 | none recorded | - | 0 | no weapon that is fashioned against you shall succeed, and you shall refute every tongue that rises against you in judgment. This is the heritage of the servants of the Lord and their vindication from me, **declares** the Lord.” |
| Jer 13:25 | declares | H0854 אֵת et "with" | declares | content_part | 5 | none recorded | - | 0 | This is your lot, the portion I have measured out to you, **declares** the Lord, because you have forgotten me and trusted in lies. |
| Isa 61:1 | good news | H1319 בָּשַׂר ba.sar "to bear tidings" | good news | content_part | 3 | none recorded | 16715 | 0 | The Spirit of the Lord God is upon me, because the Lord has anointed me to bring **good news** to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives, and the opening of the prison to those who are bound; |
| 1Ki 8:24 | declared | H1696I דָבַר da.var "to speak: promise" | declared | content_part | 4 | none recorded | - | 0 | you have kept with your servant David my father what you **declared** to him. You spoke with your mouth, and with your hand have fulfilled it this day. |
| 1Ki 8:53 | declared | H1696I דָבַר da.var "to speak: promise" | declared | content_part | 2 | none recorded | - | 0 | For you separated them from among all the peoples of the earth to be your heritage, as you **declared** through Moses your servant, when you brought our fathers out of Egypt, O Lord God.” |
| Deu 5:5 | declare | H1931 הוּא hu "he/she/it" | declare | content_part | 4 | none recorded | - | 0 | while I stood between the Lord and you at that time, to **declare** to you the word of the Lord. For you were afraid because of the fire, and you did not go up into the mountain. He said: |
| Isa 22:25 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | In that day, **declares** the Lord of hosts, the peg that was fastened in a secure place will give way, and it will be cut down and fall, and the load that was on it will be cut off, for the Lord has spoken.” |
| Jer 4:9 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “ In that day, **declares** the Lord, courage shall fail both king and officials. The priests shall be appalled and the prophets astounded.” |
| Jer 8:1 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “At that time, **declares** the Lord, the bones of the kings of Judah, the bones of its officials, the bones of the priests, the bones of the prophets, and the bones of the inhabitants of Jerusalem shall be brought out of their tombs. |
| Jer 25:12 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | Then after seventy years are completed, I will punish the king of Babylon and that nation, the land of the Chaldeans, for their iniquity, **declares** the Lord, making the land an everlasting waste. |
| Jer 27:8 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “‘“But if any nation or kingdom will not serve this Nebuchadnezzar king of Babylon, and put its neck under the yoke of the king of Babylon, I will punish that nation with the sword, with famine, and with pestilence, **declares** the Lord, until I have consumed it by his hand. |
| Jer 30:8 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “And it shall come to pass in that day, **declares** the Lord of hosts, that I will break his yoke from off your neck, and I will burst your bonds, and foreigners shall no more make a servant of him. |
| Jer 31:1 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “ At that time, **declares** the Lord, I will be the God of all the clans of Israel, and they shall be my people.” |
| Jer 39:17 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | But I will deliver you on that day, **declares** the Lord, and you shall not be given into the hand of the men of whom you are afraid. |
| Jer 49:26 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | Therefore her young men shall fall in her squares, and all her soldiers shall be destroyed in that day, **declares** the Lord of hosts. |
| Jer 50:4 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “In those days and in that time, **declares** the Lord, the people of Israel and the people of Judah shall come together, weeping as they come, and they shall seek the Lord their God. |
| Jer 50:20 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | In those days and in that time, **declares** the Lord, iniquity shall be sought in Israel, and there shall be none, and sin in Judah, and none shall be found, for I will pardon those whom I leave as a remnant. |
| Jer 50:30 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | Therefore her young men shall fall in her squares, and all her soldiers shall be destroyed on that day, **declares** the Lord. |
| Hos 2:16 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “And in that day, **declares** the Lord, you will call me ‘My Husband,’ and no longer will you call me ‘ My Baal.’ |
| Amo 2:16 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | and he who is stout of heart among the mighty shall flee away naked in that day,” **declares** the Lord. |
| Amo 8:9 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “And on that day,” **declares** the Lord God, “I will make the sun go down at noon and darken the earth in broad daylight. |
| Zep 1:10 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | “On that day,” **declares** the Lord, “a cry will be heard from the Fish Gate, a wail from the Second Quarter, a loud crash from the hills. |
| Hag 2:23 | declares | H1931 הוּא hu "he/she/it" | declares | content_part | 3 | none recorded | - | 0 | On that day, **declares** the Lord of hosts, I will take you, O Zerubbabel my servant, the son of Shealtiel, declares the Lord, and make you like a signet ring, for I have chosen you, declares the Lord of hosts.” |
| Isa 17:3 | declares | H1961 הָיָה ha.yah "to be" | declares | content_part | 2 | none recorded | - | 0 | The fortress will disappear from Ephraim, and the kingdom from Damascus; and the remnant of Syria will be like the glory of the children of Israel, **declares** the Lord of hosts. |
| Jer 26:18 | prophesied | H1961 הָיָה ha.yah "to be" | prophesied | content_part | 2 | none recorded | - | 0 | “ Micah of Moresheth **prophesied** in the days of Hezekiah king of Judah, and said to all the people of Judah: ‘ Thus says the Lord of hosts, “‘ Zion shall be plowed as a field; Jerusalem shall become a heap of ruins, and the mountain of the house a wooded height.’ |
| Jer 26:20 | prophesied | H1961 הָיָה ha.yah "to be" | prophesied | content_part | 2 | none recorded | - | 0 | There was another man who **prophesied** in the name of the Lord, Uriah the son of Shemaiah from Kiriath-jearim. He prophesied against this city and against this land in words like those of Jeremiah. |
| Jer 51:26 | declares | H1961 הָיָה ha.yah "to be" | declares | content_part | 2 | none recorded | - | 0 | No stone shall be taken from you for a corner and no stone for a foundation, but you shall be a perpetual waste, **declares** the Lord. |
| Eze 21:7 | declares | H1961 הָיָה ha.yah "to be" | declares | content_part | 2 | none recorded | - | 0 | And when they say to you, ‘ Why do you groan?’ you shall say, ‘Because of the news that it is coming. Every heart will melt, and all hands will be feeble; every spirit will faint, and all knees will be weak as water. Behold, it is coming, and it will be fulfilled,’” **declares** the Lord God. |
| Eze 21:13 | declares | H1961 הָיָה ha.yah "to be" | declares | content_part | 2 | none recorded | - | 0 | For it will not be a testing — what could it do if you despise the rod?” **declares** the Lord God. |
| Zec 2:5 | declares | H1961 הָיָה ha.yah "to be" | declares | content_part | 4 | none recorded | - | 0 | And I will be to her a wall of fire all around, **declares** the Lord, and I will be the glory in her midst.’” |
| Jer 3:16 | declares | H1992 הֵ֫מָּה hem.mah "they [masc.]" | declares | content_part | 3 | none recorded | - | 0 | And when you have multiplied and been fruitful in the land, in those days, **declares** the Lord, they shall no more say, “The ark of the covenant of the Lord.” It shall not come to mind or be remembered or missed; it shall not be made again. |
| Jer 5:18 | declares | H1992 הֵ֫מָּה hem.mah "they [masc.]" | declares | content_part | 3 | none recorded | - | 0 | “But even in those days, **declares** the Lord, I will not make a full end of you. |
| Jer 31:33 | declares | H1992 הֵ֫מָּה hem.mah "they [masc.]" | declares | content_part | 3 | none recorded | - | 0 | For this is the covenant that I will make with the house of Israel after those days, **declares** the Lord: I will put my law within them, and I will write it on their hearts. And I will be their God, and they shall be my people. |
| Jer 25:13 | prophesied | H2088 זֶה zeh "this" | prophesied | content_part | 4 | none recorded | - | 0 | I will bring upon that land all the words that I have uttered against it, everything written in this book, which Jeremiah **prophesied** against all the nations. |
| Zec 8:11 | declares | H2088 זֶה zeh "this" | declares | content_part | 3 | none recorded | - | 0 | But now I will not deal with the remnant of this people as in the former days, **declares** the Lord of hosts. |
| Lev 14:36 | declared | H2930A טָמֵא ta.me "to defile" | declared | content_part | 3 | none recorded | - | 0 | Then the priest shall command that they empty the house before the priest goes to examine the disease, lest all that is in the house be **declared** unclean. And afterward the priest shall go in to see the house. |
| 2Ki 9:26 | declares | H3068G יְהֹוָה ye.ho.vah "LORD" | declares | content_part | 2 | none recorded | - | 0 | ‘As surely as I saw yesterday the blood of Naboth and the blood of his sons — **declares** the Lord —I will repay you on this plot of ground.’ Now therefore take him up and throw him on the plot of ground, in accordance with the word of the Lord.” |
| Jer 46:18 | declares | H3588A כִּי ki "for" | declares | content_part | 2 | none recorded | - | 0 | “As I live, **declares** the King, whose name is the Lord of hosts, like Tabor among the mountains and like Carmel by the sea, shall one come. |
| Jer 21:7 | declares | H3651C כֵּן ken "so" | declares | content_part | 2 | none recorded | - | 0 | Afterward, **declares** the Lord, I will give Zedekiah king of Judah and his servants and the people in this city who survive the pestilence, sword, and famine into the hand of Nebuchadnezzar king of Babylon and into the hand of their enemies, into the hand of those who seek their lives. He shall strike them down with the edge of the sword. He shall not pity them or spare them or have compassion.’ |
| Jer 42:20 | declare | H3651C כֵּן ken "so" | declare | content_part | 3 | none recorded | - | 0 | that you have gone astray at the cost of your lives. For you sent me to the Lord your God, saying, ‘ Pray for us to the Lord our God, and whatever the Lord our God says, **declare** to us and we will do it.’ |
| Lev 14:36 | declared | H3808 לֹא lo "not" | declared | content_part | 3 | none recorded | - | 0 | Then the priest shall command that they empty the house before the priest goes to examine the disease, lest all that is in the house be **declared** unclean. And afterward the priest shall go in to see the house. |
| Amo 3:8 | prophesy | H3808 לֹא lo "not" | prophesy | content_part | 3 | none recorded | - | 0 | The lion has roared; who will not fear? The Lord God has spoken; who can but **prophesy**?” |
| Num 14:28 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | Say to them, ‘As I live, **declares** the Lord, what you have said in my hearing I will do to you: |
| 2Ki 9:26 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | ‘As surely as I saw yesterday the blood of Naboth and the blood of his sons — **declares** the Lord —I will repay you on this plot of ground.’ Now therefore take him up and throw him on the plot of ground, in accordance with the word of the Lord.” |
| Isa 17:3 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | The fortress will disappear from Ephraim, and the kingdom from Damascus; and the remnant of Syria will be like the glory of the children of Israel, **declares** the Lord of hosts. |
| Isa 22:25 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | In that day, **declares** the Lord of hosts, the peg that was fastened in a secure place will give way, and it will be cut down and fall, and the load that was on it will be cut off, for the Lord has spoken.” |
| Isa 54:17 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 5 | none recorded | - | 0 | no weapon that is fashioned against you shall succeed, and you shall refute every tongue that rises against you in judgment. This is the heritage of the servants of the Lord and their vindication from me, **declares** the Lord.” |
| Jer 2:3 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Israel was holy to the Lord, the firstfruits of his harvest. All who ate of it incurred guilt; disaster came upon them, **declares** the Lord.” |
| Jer 2:9 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “ Therefore I still contend with you, **declares** the Lord, and with your children’s children I will contend. |
| Jer 2:19 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | Your evil will chastise you, and your apostasy will reprove you. Know and see that it is evil and bitter for you to forsake the Lord your God; the fear of me is not in you, **declares** the Lord God of hosts. |
| Jer 3:1 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “ If a man divorces his wife and she goes from him and becomes another man’s wife, will he return to her? Would not that land be greatly polluted? You have played the whore with many lovers; and would you return to me? **declares** the Lord. |
| Jer 3:12 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | 14699 | 0 | Go, and proclaim these words toward the north, and say, “‘ Return, faithless Israel, **declares** the Lord. I will not look on you in anger, for I am merciful, declares the Lord; I will not be angry forever. |
| Jer 3:16 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | And when you have multiplied and been fruitful in the land, in those days, **declares** the Lord, they shall no more say, “The ark of the covenant of the Lord.” It shall not come to mind or be remembered or missed; it shall not be made again. |
| Jer 4:9 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “ In that day, **declares** the Lord, courage shall fail both king and officials. The priests shall be appalled and the prophets astounded.” |
| Jer 5:18 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “But even in those days, **declares** the Lord, I will not make a full end of you. |
| Jer 8:1 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “At that time, **declares** the Lord, the bones of the kings of Judah, the bones of its officials, the bones of the priests, the bones of the prophets, and the bones of the inhabitants of Jerusalem shall be brought out of their tombs. |
| Jer 8:3 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Death shall be preferred to life by all the remnant that remains of this evil family in all the places where I have driven them, **declares** the Lord of hosts. |
| Jer 8:17 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | For behold, I am sending among you serpents, adders that cannot be charmed, and they shall bite you,” **declares** the Lord. |
| Jer 9:6 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Heaping oppression upon oppression, and deceit upon deceit, they refuse to know me, **declares** the Lord. |
| Jer 13:25 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 5 | none recorded | - | 0 | This is your lot, the portion I have measured out to you, **declares** the Lord, because you have forgotten me and trusted in lies. |
| Jer 15:6 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | You have rejected me, **declares** the Lord; you keep going backward, so I have stretched out my hand against you and destroyed you— I am weary of relenting. |
| Jer 16:11 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | then you shall say to them: ‘ Because your fathers have forsaken me, **declares** the Lord, and have gone after other gods and have served and worshiped them, and have forsaken me and have not kept my law, |
| Jer 21:7 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | Afterward, **declares** the Lord, I will give Zedekiah king of Judah and his servants and the people in this city who survive the pestilence, sword, and famine into the hand of Nebuchadnezzar king of Babylon and into the hand of their enemies, into the hand of those who seek their lives. He shall strike them down with the edge of the sword. He shall not pity them or spare them or have compassion.’ |
| Jer 22:16 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | 15594 | 0 | He judged the cause of the poor and needy; then it was well. Is not this to know me? **declares** the Lord. |
| Jer 23:23 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | “Am I a God at hand, **declares** the Lord, and not a God far away? |
| Jer 23:33 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “ When one of this people, or a prophet or a priest asks you, ‘ What is the burden of the Lord?’ you shall say to them, ‘ You are the burden, and I will cast you off, **declares** the Lord.’ |
| Jer 25:12 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Then after seventy years are completed, I will punish the king of Babylon and that nation, the land of the Chaldeans, for their iniquity, **declares** the Lord, making the land an everlasting waste. |
| Jer 27:8 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “‘“But if any nation or kingdom will not serve this Nebuchadnezzar king of Babylon, and put its neck under the yoke of the king of Babylon, I will punish that nation with the sword, with famine, and with pestilence, **declares** the Lord, until I have consumed it by his hand. |
| Jer 27:22 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | They shall be carried to Babylon and remain there until the day when I visit them, **declares** the Lord. Then I will bring them back and restore them to this place.” |
| Jer 29:14 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | I will be found by you, **declares** the Lord, and I will restore your fortunes and gather you from all the nations and all the places where I have driven you, declares the Lord, and I will bring you back to the place from which I sent you into exile. |
| Jer 30:8 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “And it shall come to pass in that day, **declares** the Lord of hosts, that I will break his yoke from off your neck, and I will burst your bonds, and foreigners shall no more make a servant of him. |
| Jer 30:21 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | 19149 | 0 | Their prince shall be one of themselves; their ruler shall come out from their midst; I will make him draw near, and he shall approach me, for who would dare of himself to approach me? **declares** the Lord. |
| Jer 31:1 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “ At that time, **declares** the Lord, I will be the God of all the clans of Israel, and they shall be my people.” |
| Jer 31:33 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | For this is the covenant that I will make with the house of Israel after those days, **declares** the Lord: I will put my law within them, and I will write it on their hearts. And I will be their God, and they shall be my people. |
| Jer 32:5 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | And he shall take Zedekiah to Babylon, and there he shall remain until I visit him, **declares** the Lord. Though you fight against the Chaldeans, you shall not succeed ’?” |
| Jer 39:17 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | But I will deliver you on that day, **declares** the Lord, and you shall not be given into the hand of the men of whom you are afraid. |
| Jer 46:18 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | “As I live, **declares** the King, whose name is the Lord of hosts, like Tabor among the mountains and like Carmel by the sea, shall one come. |
| Jer 49:26 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Therefore her young men shall fall in her squares, and all her soldiers shall be destroyed in that day, **declares** the Lord of hosts. |
| Jer 50:4 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “In those days and in that time, **declares** the Lord, the people of Israel and the people of Judah shall come together, weeping as they come, and they shall seek the Lord their God. |
| Jer 50:20 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | In those days and in that time, **declares** the Lord, iniquity shall be sought in Israel, and there shall be none, and sin in Judah, and none shall be found, for I will pardon those whom I leave as a remnant. |
| Jer 50:21 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “Go up against the land of Merathaim, and against the inhabitants of Pekod. Kill, and devote them to destruction, **declares** the Lord, and do all that I have commanded you. |
| Jer 50:30 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Therefore her young men shall fall in her squares, and all her soldiers shall be destroyed on that day, **declares** the Lord. |
| Jer 51:26 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | No stone shall be taken from you for a corner and no stone for a foundation, but you shall be a perpetual waste, **declares** the Lord. |
| Eze 20:31 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | When you present your gifts and offer up your children in fire, you defile yourselves with all your idols to this day. And shall I be inquired of by you, O house of Israel? As I live, **declares** the Lord God, I will not be inquired of by you. |
| Eze 21:7 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | And when they say to you, ‘ Why do you groan?’ you shall say, ‘Because of the news that it is coming. Every heart will melt, and all hands will be feeble; every spirit will faint, and all knees will be weak as water. Behold, it is coming, and it will be fulfilled,’” **declares** the Lord God. |
| Eze 21:13 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | For it will not be a testing — what could it do if you despise the rod?” **declares** the Lord God. |
| Eze 32:16 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | This is a lamentation that shall be chanted; the daughters of the nations shall chant it; over Egypt, and over all her multitude, shall they chant it, **declares** the Lord God.” |
| Eze 35:11 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | therefore, as I live, **declares** the Lord God, I will deal with you according to the anger and envy that you showed because of your hatred against them. And I will make myself known among them, when I judge you. |
| Eze 43:27 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | And when they have completed these days, then from the eighth day onward the priests shall offer on the altar your burnt offerings and your peace offerings, and I will accept you, **declares** the Lord God.” |
| Eze 45:15 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | And one sheep from every flock of two hundred, from the watering places of Israel for grain offering, burnt offering, and peace offerings, to make atonement for them, **declares** the Lord God. |
| Hos 2:16 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “And in that day, **declares** the Lord, you will call me ‘My Husband,’ and no longer will you call me ‘ My Baal.’ |
| Amo 2:16 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | and he who is stout of heart among the mighty shall flee away naked in that day,” **declares** the Lord. |
| Amo 4:6 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “ I gave you cleanness of teeth in all your cities, and lack of bread in all your places, yet you did not return to me,” **declares** the Lord. |
| Amo 4:8 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | so two or three cities would wander to another city to drink water, and would not be satisfied; yet you did not return to me,” **declares** the Lord. |
| Amo 4:9 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “I struck you with blight and mildew; your many gardens and your vineyards, your fig trees and your olive trees the locust devoured; yet you did not return to me,” **declares** the Lord. |
| Amo 4:10 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “I sent among you a pestilence after the manner of Egypt; I killed your young men with the sword, and carried away your horses, and I made the stench of your camp go up into your nostrils; yet you did not return to me,” **declares** the Lord. |
| Amo 4:11 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “I overthrew some of you, as when God overthrew Sodom and Gomorrah, and you were as a brand plucked out of the burning; yet you did not return to me,” **declares** the Lord. |
| Amo 8:9 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “And on that day,” **declares** the Lord God, “I will make the sun go down at noon and darken the earth in broad daylight. |
| Amo 9:12 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | that they may possess the remnant of Edom and all the nations who are called by my name,” **declares** the Lord who does this. |
| Zep 1:10 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | “On that day,” **declares** the Lord, “a cry will be heard from the Fish Gate, a wail from the Second Quarter, a loud crash from the hills. |
| Zep 2:9 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 2 | none recorded | - | 0 | Therefore, as I live,” **declares** the Lord of hosts, the God of Israel, “ Moab shall become like Sodom, and the Ammonites like Gomorrah, a land possessed by nettles and salt pits, and a waste forever. The remnant of my people shall plunder them, and the survivors of my nation shall possess them.” |
| Hag 2:17 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | I struck you and all the products of your toil with blight and with mildew and with hail, yet you did not turn to me, **declares** the Lord. |
| Hag 2:23 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | On that day, **declares** the Lord of hosts, I will take you, O Zerubbabel my servant, the son of Shealtiel, declares the Lord, and make you like a signet ring, for I have chosen you, declares the Lord of hosts.” |
| Zec 1:4 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Do not be like your fathers, to whom the former prophets cried out, ‘ Thus says the Lord of hosts, Return from your evil ways and from your evil deeds.’ But they did not hear or pay attention to me, **declares** the Lord. |
| Zec 2:5 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 4 | none recorded | - | 0 | And I will be to her a wall of fire all around, **declares** the Lord, and I will be the glory in her midst.’” |
| Zec 2:6 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | Up! Up! Flee from the land of the north, **declares** the Lord. For I have spread you abroad as the four winds of the heavens, declares the Lord. |
| Zec 8:11 | declares | H5002 נְאֻם ne.um "utterance" | declares | content_part | 3 | none recorded | - | 0 | But now I will not deal with the remnant of this people as in the former days, **declares** the Lord of hosts. |
| Jer 23:21 | prophesied | H5012 נָבָא na.va "to prophesy" | prophesied | content_part | 4 | none recorded | - | 0 | “I did not send the prophets, yet they ran; I did not speak to them, yet they **prophesied**. |
| Jer 25:13 | prophesied | H5012 נָבָא na.va "to prophesy" | prophesied | content_part | 4 | none recorded | - | 0 | I will bring upon that land all the words that I have uttered against it, everything written in this book, which Jeremiah **prophesied** against all the nations. |
| Jer 26:18 | prophesied | H5012 נָבָא na.va "to prophesy" | prophesied | content_part | 2 | none recorded | - | 0 | “ Micah of Moresheth **prophesied** in the days of Hezekiah king of Judah, and said to all the people of Judah: ‘ Thus says the Lord of hosts, “‘ Zion shall be plowed as a field; Jerusalem shall become a heap of ruins, and the mountain of the house a wooded height.’ |
| Jer 26:20 | prophesied | H5012 נָבָא na.va "to prophesy" | prophesied | content_part | 2 | none recorded | - | 0 | There was another man who **prophesied** in the name of the Lord, Uriah the son of Shemaiah from Kiriath-jearim. He prophesied against this city and against this land in words like those of Jeremiah. |
| Deu 5:5 | declare | H5046 נָגַד na.gad "to tell" | declare | content_part | 4 | none recorded | - | 0 | while I stood between the Lord and you at that time, to **declare** to you the word of the Lord. For you were afraid because of the fire, and you did not go up into the mountain. He said: |
| Psa 40:5 | proclaim | H5046 נָגַד na.gad "to tell" | proclaim | content_part | 3 | none recorded | - | 0 | You have multiplied, O Lord my God, your wondrous deeds and your thoughts toward us; none can compare with you! I will **proclaim** and tell of them, yet they are more than can be told. |
| Jer 9:12 | declare | H5046 נָגַד na.gad "to tell" | declare | content_part | 3 | none recorded | - | 0 | Who is the man so wise that he can understand this? To whom has the mouth of the Lord spoken, that he may **declare** it? Why is the land ruined and laid waste like a wilderness, so that no one passes through? |
| Jer 42:20 | declare | H5046 נָגַד na.gad "to tell" | declare | content_part | 3 | none recorded | 14719 | 0 | that you have gone astray at the cost of your lives. For you sent me to the Lord your God, saying, ‘ Pray for us to the Lord our God, and whatever the Lord our God says, **declare** to us and we will do it.’ |
| Exo 36:6 | proclaimed | H5674A עָבַר a.var "to pass" | proclaimed | content_part | 2 | none recorded | - | 0 | So Moses gave command, and word was **proclaimed** throughout the camp, “Let no man or woman do anything more for the contribution for the sanctuary.” So the people were restrained from bringing, |
| Amo 4:6 | declares | H5704 עַד ad "till" | declares | content_part | 3 | none recorded | - | 0 | “ I gave you cleanness of teeth in all your cities, and lack of bread in all your places, yet you did not return to me,” **declares** the Lord. |
| Amo 4:8 | declares | H5704 עַד ad "till" | declares | content_part | 3 | none recorded | - | 0 | so two or three cities would wander to another city to drink water, and would not be satisfied; yet you did not return to me,” **declares** the Lord. |
| Amo 4:9 | declares | H5704 עַד ad "till" | declares | content_part | 3 | none recorded | - | 0 | “I struck you with blight and mildew; your many gardens and your vineyards, your fig trees and your olive trees the locust devoured; yet you did not return to me,” **declares** the Lord. |
| Amo 4:10 | declares | H5704 עַד ad "till" | declares | content_part | 3 | none recorded | - | 0 | “I sent among you a pestilence after the manner of Egypt; I killed your young men with the sword, and carried away your horses, and I made the stench of your camp go up into your nostrils; yet you did not return to me,” **declares** the Lord. |
| Amo 4:11 | declares | H5704 עַד ad "till" | declares | content_part | 3 | none recorded | - | 0 | “I overthrew some of you, as when God overthrew Sodom and Gomorrah, and you were as a brand plucked out of the burning; yet you did not return to me,” **declares** the Lord. |
| Eze 45:15 | declares | H5921A עַל al "upon" | declares | content_part | 3 | none recorded | - | 0 | And one sheep from every flock of two hundred, from the watering places of Israel for grain offering, burnt offering, and peace offerings, to make atonement for them, **declares** the Lord God. |
| Amo 9:12 | declares | H5921A עַל al "upon" | declares | content_part | 4 | none recorded | - | 0 | that they may possess the remnant of Edom and all the nations who are called by my name,” **declares** the Lord who does this. |
| Deu 27:14 | declare | H6030B עָנָה a.nah "to answer" | declare | content_part | 2 | none recorded | - | 0 | And the Levites shall **declare** to all the men of Israel in a loud voice: |
| Dan 2:15 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 2 | none recorded | - | 0 | He **declared** to Arioch, the king’s captain, “ Why is the decree of the king so urgent?” Then Arioch made the matter known to Daniel. |
| Dan 2:26 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 2 | none recorded | - | 0 | The king **declared** to Daniel, whose name was Belteshazzar, “ Are you able to make known to me the dream that I have seen and its interpretation?” |
| Dan 3:9 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 2 | none recorded | - | 0 | They **declared** to King Nebuchadnezzar, “O king, live forever! |
| Dan 3:26 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 3 | none recorded | - | 0 | Then Nebuchadnezzar came near to the door of the burning fiery furnace; he **declared**, “ Shadrach, Meshach, and Abednego, servants of the Most High God, come out, and come here!” Then Shadrach, Meshach, and Abednego came out from the fire. |
| Dan 5:10 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 2 | none recorded | - | 0 | The queen, because of the words of the king and his lords, came into the banqueting hall, and the queen **declared**, “O king, live forever! Let not your thoughts alarm you or your color change. |
| Dan 6:16 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 3 | none recorded | - | 0 | Then the king commanded, and Daniel was brought and cast into the den of lions. The king **declared** to Daniel, “May your God, whom you serve continually, deliver you!” |
| Dan 6:20 | declared | H6032 עֲנָה a.nah "to answer" | declared | content_part | 2 | none recorded | - | 0 | As he came near to the den where Daniel was, he cried out in a tone of anguish. The king **declared** to Daniel, “O Daniel, servant of the living God, has your God, whom you serve continually, been able to deliver you from the lions?” |
| Exo 36:6 | proclaimed | H6963J קוֹל qol "voice: message" | proclaimed | content_part | 2 | none recorded | - | 0 | So Moses gave command, and word was **proclaimed** throughout the camp, “Let no man or woman do anything more for the contribution for the sanctuary.” So the people were restrained from bringing, |
| Lev 25:10 | proclaim | H7121I קָרָא qa.ra "to call: call out" | proclaim | content_part | 2 | none recorded | - | 0 | And you shall consecrate the fiftieth year, and **proclaim** liberty throughout the land to all its inhabitants. It shall be a jubilee for you, when each of you shall return to his property and each of you shall return to his clan. |
| 2Ki 23:16 | proclaimed | H7121I קָרָא qa.ra "to call: call out" | proclaimed | content_part | 2 | none recorded | - | 0 | And as Josiah turned, he saw the tombs there on the mount. And he sent and took the bones out of the tombs and burned them on the altar and defiled it, according to the word of the Lord that the man of God **proclaimed**, who had predicted these things. |
| Neh 6:7 | proclaim | H7121I קָרָא qa.ra "to call: call out" | proclaim | content_part | 3 | none recorded | - | 0 | And you have also set up prophets to **proclaim** concerning you in Jerusalem, ‘There is a king in Judah.’ And now the king will hear of these reports. So now come and let us take counsel together.” |
| Isa 44:7 | proclaim | H7121I קָרָא qa.ra "to call: call out" | proclaim | content_part | 3 | none recorded | - | 0 | Who is like me? Let him **proclaim** it. Let him declare and set it before me, since I appointed an ancient people. Let them declare what is to come, and what will happen. |
| Jer 2:2 | proclaim | H7121I קָרָא qa.ra "to call: call out" | proclaim | content_part | 2 | none recorded | - | 0 | “ Go and **proclaim** in the hearing of Jerusalem, Thus says the Lord, “I remember the devotion of your youth, your love as a bride, how you followed me in the wilderness, in a land not sown. |
| Jer 34:17 | proclaiming | H7121I קָרָא qa.ra "to call: call out" | proclaiming | content_part | 3 | none recorded | - | 0 | “ Therefore, thus says the Lord: You have not obeyed me by **proclaiming** liberty, every one to his brother and to his neighbor; behold, I proclaim to you liberty to the sword, to pestilence, and to famine, declares the Lord. I will make you a horror to all the kingdoms of the earth. |
| Zec 7:7 | proclaimed | H7121I קָרָא qa.ra "to call: call out" | proclaimed | content_part | 2 | none recorded | - | 0 | Were not these the words that the Lord **proclaimed** by the former prophets, when Jerusalem was inhabited and prosperous, with her cities around her, and the South and the lowland were inhabited?'” |
| Jer 8:3 | declares | H8033G שָׁם sham "there" | declares | content_part | 3 | none recorded | - | 0 | Death shall be preferred to life by all the remnant that remains of this evil family in all the places where I have driven them, **declares** the Lord of hosts. |
| Jer 29:14 | declares | H8033G שָׁם sham "there" | declares | content_part | 4 | none recorded | - | 0 | I will be found by you, **declares** the Lord, and I will restore your fortunes and gather you from all the nations and all the places where I have driven you, declares the Lord, and I will bring you back to the place from which I sent you into exile. |
| Lev 25:10 | proclaim | H8141 שָׁנָה sha.nah "year" | proclaim | content_part | 2 | none recorded | - | 0 | And you shall consecrate the fiftieth year, and **proclaim** liberty throughout the land to all its inhabitants. It shall be a jubilee for you, when each of you shall return to his property and each of you shall return to his clan. |

## 4. What the study has recorded for these occurrences

Of 979 occurrences, 0 have an engagement observation and 979 have none recorded. There are 82 live observations on them (0 engagement, 63 of other recorded stages, 19 of the retired catalogue stages) and 10 withdrawn.

### 4.1 Engagement: what each word does for the inner being (0 observations)

An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to every occurrence it covers.

_no engagement observation covers these occurrences_

### 4.2 Other recorded observations (63)

Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.

- **Observation 12952** (prior-capture, tag face, status draft): Form of anger, "Slow to anger": the proclaimed name (9 / 9 hits and verses; faces F; units 1).
  - applies to 1 occurrence(s): Exo 34:6 (proclaimed)
- **Observation 13012** (prior-capture, tag statement, status draft): The same phrase, the speaker's purpose: "slow to anger": God's proclaimed name, Moses' plea, Joel's call to return, Nahum's warning, Jonah's complaint, the wise man's virtue.
  - applies to 1 occurrence(s): Exo 34:6 (proclaimed)
- **Observation 13207** (prior-capture, tag statement, status draft): "Slow to anger" is one phrase (Exo 34:6; Pro 14:29): God's proclaimed name, used by many speakers to different ends, and the wise man's virtue.
  - applies to 1 occurrence(s): Exo 34:6 (proclaimed)
- **Observation 13248** (prior-capture, tag face, status draft): Face F. Slow to anger: the name, and forbearance: Hits / verses: 9 / 9; Toward: —; Other parties named: Moses hears it proclaimed; others recite it; Example verses: Exo 34:6; Num 14:18; Joe 2:13; Nah 1:3; Jer 15:15.
  - applies to 1 occurrence(s): Exo 34:6 (proclaimed)
- **Observation 13889** (prior-capture, tag statement, status draft): Eze 20:33, "As I live, declares the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you", answers a thought, "What is in your mind shall never happen ... 'Let us be like the nations ... and worship wood and stone'" (20:32); the wrath poured out goes with bringing out and gathering (20:34), with judgment "face to face" (20:35), and with bringing them "into the bond of the covenant" (20:37): God answers a thought in the mind with an oath by his own life and with his rule.
  - applies to 1 occurrence(s): Eze 20:33 (declares)
- **Observation 14207** (prior-capture, tag statement, status draft): Where it comes from: A final provocation on top of the store: Laban's search (31:33–35), Ish-bosheth's accusation (3:7); For Elihu, an argument that has failed: at Job "because he justified himself rather than God", at the friends "because they had found no answer, although they had declared Job to be in the wrong" (32:2–3).
  - applies to 1 occurrence(s): Job 32:3 (declared)
- **Observation 14511** (prior-capture, tag statement, status draft): What it does. Three moments: Proclaimed and received: "The Lord, the Lord, a God merciful and gracious, slow to anger" (Exo 34:6). Moses "quickly bowed his head toward the earth and worshiped" (34:8); Pleaded back: Moses quotes it to God word for word as his argument: "'The Lord is slow to anger and abounding in steadfast love …' Please pardon the iniquity of this people" (Num 14:18–19). It is answered: "I have pardoned, according to your word" (14:20); Recited in confession, as history: "they stiffened their neck and appointed a leader to return to their slavery in Egypt. But you are a God ready to forgive, gracious and merciful, slow to anger" (Neh 9:17). The name is now told as what God h ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Exo 34:6 (proclaimed)
- **Observation 14526** (prior-capture, tag statement, status draft): Part B: Psa 78:58, 78:59, 78:62; Isa 65:3; Jer 7:18, 7:19, 7:20; 11:17; 15:14; 17:4; 25:6, 25:7; 32:29, 32:30, 32:31, 32:32 (16 verses): More roots; Treachery like the fathers': "turned away and acted treacherously like their fathers; they twisted like a deceitful bow" (Psa 78:57); Self-holiness: "who say, 'Keep to yourself, do not come near me, for I am too holy for you'" (Isa 65:5). This is said to a God who says "I spread out my hands all the day to a rebellious people" (65:2); Trust in man: "Cursed is the man who trusts in man and makes flesh his strength, whose heart turns away from the Lord" (Jer 17:5); From youth, turning the back: "done nothing but evil in my sight from their youth" ... (cut; the whole text is in the workbook)
  - applies to 3 occurrence(s): Jer 7:19 (declares), Jer 25:7 (declares), Jer 32:30 (declares)
- **Observation 14595** (prior-capture, tag statement, status draft): How it co-exists. Fasting and humbling: "I proclaimed a fast … that we might humble ourselves before our God, to seek from him a safe journey" (8:21). "we fasted and implored our God for this, and he listened" (8:23).
  - applies to 1 occurrence(s): Ezr 8:21 (proclaimed)
- **Observation 14698** (prior-capture, tag statement, status draft): Part C: Eze 13:13; 13:15: The whitewashed wall: "When the wall falls, will it not be said to you, 'Where is the coating …?'" (13:12). "the prophets of Israel who … saw visions of peace for her, when there was no peace" (13:16), and the daughters "who prophesy out of their own hearts" (13:17); False peace is a wall coated over, and the wrath is what shows what the coating hid; Seat ; In the verse: Eze 13:13 "wind". Spurious; Outside: Eze 13:17 "out of their own hearts". The false prophetesses'. Genuine.
  - applies to 1 occurrence(s): Eze 13:17 (prophesy)
- **Observation 14699** (prior-capture, tag statement, status draft): What it does: "Return, faithless Israel, declares the Lord. I will not look on you in anger, for I am merciful … I will not be angry forever. Only acknowledge your guilt" (Jer 3:12–13); "Circumcise yourselves to the Lord; remove the foreskin of your hearts … lest my wrath go forth like fire" (4:4); "Execute justice in the morning, and deliver from the hand of the oppressor him who has been robbed, lest my wrath go forth like fire" (21:12); "It may be that their plea for mercy will come before the Lord, and that every one will turn from his evil way, for great is the anger and wrath that the Lord has pronounced against this people" (36:7).
  - applies to 2 occurrence(s): Jer 3:12 (declares), Jer 3:13 (declares)
- **Observation 14700** (prior-capture, tag statement, status draft): How it co-exists: Pretense warned against: Judah "did not return to me with her whole heart, but in pretense" (3:10); Fasting: the scroll is read "on a day of fasting" (36:6), and the people "proclaimed a fast before the Lord" (36:9).
  - applies to 1 occurrence(s): Jer 36:9 (proclaimed)
- **Observation 14716** (prior-capture, tag statement, status draft): How it co-exists: In Jer 23, set against false prophets: "if they had stood in my council, then they would have proclaimed my words to my people, and they would have turned them from their evil way" (23:22); In Jer 30, set after restoration: "you shall be my people, and I will be your God" (30:22). A prince draws near: "for who would dare of himself to approach me?" (30:21).
  - applies to 1 occurrence(s): Jer 23:22 (proclaimed)
- **Observation 14719** (prior-capture, tag statement, status draft): Where it comes from: Fear: "the sword that you fear shall overtake you there … the famine of which you are afraid shall follow close after you" (42:16); Asking and not doing: "For you sent me to the Lord your God, saying, 'Pray for us … whatever the Lord our God says, declare to us and we will do it.' And I have this day declared it to you, but you have not obeyed" (42:20–21); Forgetting: "Have you forgotten the evil of your fathers …?" (44:9); No humbling: "They have not humbled themselves even to this day, nor have they feared" (44:10).
  - applies to 2 occurrence(s): Jer 42:20 (declare), Jer 42:21 (declared)
- **Observation 14765** (prior-capture, tag statement, status draft): What it does: "'Yet even now,' declares the Lord, 'return to me with all your heart, with fasting, with weeping, and with mourning; and rend your hearts and not your garments.' Return to the Lord your God, for he is gracious and merciful, slow to anger … Who knows whether he will not turn and relent, and leave a blessing behind him …?" (Joe 2:12–14); The king of Nineveh: "Let neither man nor beast … taste anything … let man and beast be covered with sackcloth, and let them call out mightily to God. Let everyone turn from his evil way and from the violence that is in his hands. Who knows? God may turn and relent and turn from his fierce anger, so that we may not perish" (Jon 3:7–9).
  - applies to 1 occurrence(s): Joe 2:12 (declares)
- **Observation 14946** (prior-capture, tag statement, status draft): (v3) Eze 13:15 (FS): Context seat: Eze 13:17 "prophesy out of their own hearts"; Whose · check: the false prophetesses' · genuine; Already read in: B v3 §6; §: §42.
  - applies to 1 occurrence(s): Eze 13:17 (prophesy)
- **Observation 15194** (prior-capture, tag statement, status draft): The ground for boasting: "I would rather die than have anyone deprive me of my ground for boasting. For if I preach the gospel, that gives me no ground for boasting. For necessity is laid upon me" (1Co 9:15–16); The preaching itself is no ground, because it is laid on him. The ground is that he preached "free of charge" (9:18).
  - applies to 2 occurrence(s): 1Cor 9:16 (preach the gospel), 1Cor 9:18 (preaching)
- **Observation 15223** (prior-capture, tag statement, status draft): Mocked as prophet. "mocking him as they beat him. They also blindfolded him and kept asking him, 'Prophesy! Who is it that struck you?'" (Luk 22:63–64).
  - applies to 1 occurrence(s): Luk 22:64 (prophesy)
- **Observation 15236** (prior-capture, tag statement, status draft): "If there be for him an angel, a mediator, one of the thousand, to declare to man what is right for him" (Job 33:23). This is held for 13.2. The M08-tagged word means "mediator" here.
  - applies to 1 occurrence(s): Job 33:23 (declare)
- **Observation 15470** (prior-capture, tag statement, status draft): Paul, brought low and lowering himself: "I know how to be brought low, and I know how to abound … I have learned … to be content" (Phili 4:11–12). Being brought low is a circumstance here, met with contentment, "through him who strengthens me" (4:13); "did I commit a sin in humbling myself so that you might be exalted, because I preached God's gospel to you free of charge?" (2Cor 11:7). A lowering taken on for others' good. I read: this has the shape of Phili 2: lowered so that another is raised; "I fear that when I come again my God may humble me before you, and I may have to mourn over many of those who sinned earlier and have not repented" (2Cor 12:21). Here Paul is humbled by others' unr ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): 2Cor 11:7 (preached)
- **Observation 15594** (prior-capture, tag statement, status draft): Where a verse joins the two sides: "Whoever oppresses a poor man insults his Maker, but he who is generous to the needy honors him" (Pro 14:31); "Whoever mocks the poor insults his Maker" (Pro 17:5); "Whoever is generous to the poor lends to the Lord" (Pro 19:17); "He judged the cause of the poor and needy … Is not this to know me? declares the Lord" (Jer 22:16); "The rich and the poor meet together; the Lord is the Maker of them all" (Pro 22:2); "Did not he who made me in the womb make him?" (Job 31:15).
  - applies to 1 occurrence(s): Jer 22:16 (declares)
- **Observation 15965** (prior-capture, tag statement, status draft): 1.11 ◆ Breath, wind and thought: "When his breath departs … on that very day his plans perish" (Psa 146:4) — the brief's thought link; "he who … creates the wind, and declares to man what is his thought" (Amo 4:13); "windy knowledge" (Job 15:2); "I applied my heart to know wisdom … this also is but a striving after wind" (Ecc 1:17); "Every man is stupid and without knowledge … there is no breath in them" (Jer 10:14; 51:17)
  - applies to 1 occurrence(s): Amo 4:13 (declares)
- **Observation 16020** (prior-capture, tag statement, status draft): Heart or own spirit as a *false* source: "those who prophesy from their own hearts" (Eze 13:2, 17); "prophesy the deceit of their own heart" (Jer 23:26); "visions of their own minds, not from the mouth of the Lord" (Jer 23:16; 14:14); "foolish prophets who follow their own spirit" (Eze 13:3) [H]
  - applies to 4 occurrence(s): Jer 23:16 (prophesy), Jer 23:26 (prophesy), Eze 13:2 (prophesy), Eze 13:17 (prophesy)
- **Observation 16021** (prior-capture, tag statement, status draft): God's Spirit as the true source: "the Spirit of God rushed upon him, and he prophesied" (1Sa 10:10; 19:20, 23); "as soon as the Spirit rested on them, they prophesied" (Num 11:25–26); "that the Lord would put his Spirit on them!" (Num 11:29); Revisit 2026-09-28 (context Num 11:24–29, Batch F §9.5): they prophesied "but they did not continue" (25). Joshua: "stop them" (28). Moses: "Are you jealous for my sake?" (29). The resting Spirit is resisted and then defended, and it is recognised by others.; "I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy" (Joe 2:28; Act 2:17–18); "carried along by the Holy Spirit" — "not by the will of man" (2Pe 1:21)
  - applies to 8 occurrence(s): Num 11:25 (prophesied), Num 11:26 (prophesied), 1Sa 10:10 (prophesied), 1Sa 19:20 (prophesied), 1Sa 19:23 (prophesied), Joe 2:28 (prophesy), Act 2:17 (prophesy), Act 2:18 (prophesy)
- **Observation 16022** (prior-capture, tag statement, status draft): Spirit, prophecy and a new heart in sequence: "the Spirit of the Lord will rush upon you, and you will prophesy … and be turned into another man" (1Sa 10:6) → "God gave him another heart" (1Sa 10:9).
  - applies to 1 occurrence(s): 1Sa 10:6 (prophesy)
- **Observation 16025** (prior-capture, tag statement, status draft): Wind prophets and prophesying to the breath: "The prophets will become wind" (Jer 5:13); "utter wind and lies" (Mic 2:11); "Prophesy to the breath … Come from the four winds, O breath" (Eze 37:9–10); "it was allowed to give breath to the image of the beast, so that the image … might even speak" (Rev 13:15) — false animation
  - applies to 1 occurrence(s): Eze 37:9 (prophesy)
- **Observation 16263** (prior-capture, tag statement, status draft): 1.6 The Spirit speaks through the person: "The Spirit of the Lord speaks by me; his word is on my tongue" (2Sa 23:2) [D1]; "as he spoke to me, the Spirit entered into me and set me on my feet, and I heard him speaking to me" (Eze 2:2; 3:24) [D3]; "How did the Spirit of the Lord go from me to speak to you?" (1Ki 22:24; 2Ch 18:23) [D1]; "the Lord … took some of the Spirit that was on him and put it on the seventy elders … they prophesied" (Num 11:17, 25) [D2]; "David, in the Spirit, calls him Lord" (Mat 22:43) [D2]
  - applies to 1 occurrence(s): Num 11:25 (prophesied)
- **Observation 16264** (prior-capture, tag statement, status draft): The lying spirit: "the Lord has put a lying spirit in the mouth … the Lord has declared disaster" (1Ki 22:23; 2Ch 18:22) [O]
  - applies to 2 occurrence(s): 1Ki 22:23 (declared), 2Ch 18:22 (declared)
- **Observation 16480** (prior-capture, tag statement, status draft): Covering: "he who is trustworthy in spirit keeps a thing covered" (Pro 11:13); "A prudent man conceals knowledge, but the heart of fools proclaims folly" (Pro 12:23); "I have not hidden your deliverance within my heart" (Psa 40:10); "the Lord has poured out upon you a spirit of deep sleep … and covered your heads (the seers)" (Isa 29:10) [X]; "my soul shall exult … he has covered me with the robe of righteousness" (Isa 61:10)
  - applies to 1 occurrence(s): Pro 12:23 (proclaims)
- **Observation 16517** (prior-capture, tag statement, status draft): Divine [D1]: "filled with power, with the Spirit of the Lord, and with justice and might, to declare to Jacob his transgression" (Mic 3:8); "I have put my Spirit upon him; he will bring forth justice" (Isa 42:1)
  - applies to 1 occurrence(s): Mic 3:8 (declare)
- **Observation 16583** (prior-capture, tag statement, status draft): Divine: "an alliance, but not of my Spirit, that they may add sin to sin" (Isa 30:1) [D1]; "the Spirit of the Lord … to declare to Jacob his transgression" (Mic 3:8) [D1]; "The Spirit of God clothed Zechariah … 'Why do you break the commandments?'" (2Ch 24:20) [D1]; "for the forgiveness of your sins, and you will receive the gift of the Holy Spirit" (Act 2:38); "the law of the Spirit of life has set you free … from the law of sin and death" (Rom 8:2)
  - applies to 1 occurrence(s): Mic 3:8 (declare)
- **Observation 16715** (prior-capture, tag statement, status draft): The Spirit's mission to the poor and brokenhearted [D1]: "The Spirit of the Lord God is upon me, because the Lord has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted" (Isa 61:1); "The Spirit of the Lord is upon me … to proclaim good news to the poor" (Luk 4:18)
  - applies to 2 occurrence(s): Isa 61:1 (good news), Luk 4:18 (good news)
- **Observation 16775** (prior-capture, tag statement, status draft): Other: "your servant has found courage [*his heart*] to pray" (2Sa 7:27); "the clans of Judah shall say to themselves" (Zec 12:5); "creates the wind, and declares to man what is his thought" (Amo 4:13); "I will remove … the spirit of uncleanness" (Zec 13:2) [O+X]; "stirred up the spirit of Zerubbabel … Joshua … and all the remnant" (Hag 1:14) → G §11; "eat the flesh" (Jer 7:21)
  - applies to 1 occurrence(s): Amo 4:13 (declares)
- **Observation 16966** (prior-capture, tag statement, status draft): The Spirit on people: "as soon as the Spirit rested on them, they prophesied. But they did not continue doing it" (Num 11:25); "the Spirit rested on them … and so they prophesied in the camp" (Num 11:26); "The Spirit of the Lord shall rest upon him, the Spirit of wisdom and understanding" (Isa 11:2); "the Spirit of glory and of God rests upon you" (1Pe 4:14); "The spirit of Elijah rests on Elisha" (2Ki 2:15)
  - applies to 2 occurrence(s): Num 11:25 (prophesied), Num 11:26 (prophesied)
- **Observation 17240** (prior-capture, tag statement, status draft): h. The heart as source of what comes out: *Source:*; "Out of the heart come evil thoughts …" (Mat 15:19; Mar 7:21); "what comes out of the mouth proceeds from the heart" (Mat 15:18); "Out of the abundance of the heart the mouth speaks" (Mat 12:34; Luk 6:45); "Keep your heart with all vigilance, for from it flow the springs of life" (Pro 4:23); *Heart producing speech:*; "The heart of the wise makes his speech judicious" (Pro 16:23); "My heart overflows with a pleasing theme; … my tongue is like the pen of a ready scribe" (Psa 45:1); "My heart became hot within me. As I mused, the fire burned; then I spoke" (Psa 39:3); "in my heart … a burning fire shut up in my bones … I cannot [hold it in]" ... (cut; the whole text is in the workbook)
  - applies to 4 occurrence(s): Jer 23:16 (prophesy), Jer 23:26 (prophesy), Eze 13:2 (prophesy), Eze 13:17 (prophesy)
- **Observation 17480** (prior-capture, tag statement, status draft): 15. Aims (10.7 *Setting the heart*): *"I make it my ambition to preach the gospel, not where Christ has already been named"* (Rom 15:20); *"whether we are at home or away, we make it our aim to please him. For we must all appear before the judgment seat of Christ"* (2Co 5:9–10); *"aspire to live quietly, and to mind your own affairs, and to work with your hands"* (1Th 4:11); *"If anyone aspires to the office of overseer, he desires a noble task"* (1Ti 3:1); The word (*philotimeomai*) is the one used for ambition. I read what it is aimed at in these verses as unexpected: going where no one has gone, pleasing him wherever one is, and quietness.
  - applies to 1 occurrence(s): Rom 15:20 (preach the gospel)
- **Observation 17521** (prior-capture, tag statement, status draft): Isa 46:10–11. *"declaring the end from the beginning … saying, 'My counsel shall stand, and I will accomplish all my purpose' … I have spoken, and I will bring it to pass; I have purposed, and I will do it."* The setting is *"Remember this and stand firm … remember the former things of old; for I am God, and there is no other"* (46:8–9).
  - applies to 1 occurrence(s): Isa 46:10 (declaring)
- **Observation 17582** (prior-capture, tag statement, status draft): Isa 48:14. *"Who among them has declared these things? The Lord loves him; he shall perform his purpose on Babylon."*
  - applies to 1 occurrence(s): Isa 48:14 (declared)
- **Observation 17846** (prior-capture, tag statement, status draft): Creation shaken. *"For in my jealousy and in my blazing wrath I declare, On that day there shall be a great earthquake … all the people who are on the face of the earth, shall quake at my presence"* (Eze 38:19–20).
  - applies to 1 occurrence(s): Eze 38:19 (declare)
- **Observation 18009** (prior-capture, tag statement, status draft): Isa 52:7 | M70; M72 | "good news of happiness", beside *"Your God reigns"*.
  - applies to 1 occurrence(s): Isa 52:7 (good news)
- **Observation 18163** (prior-capture, tag statement, status draft): Toward building. *"the Lord stirred up the spirit of Cyrus king of Persia, so that he made a proclamation"* (Ezr 1:1; 2Ch 36:22). Then *"everyone whose spirit God had stirred to go up"* (Ezr 1:5). Not everyone went: the stirred ones rose. Haggai gives the order: They *"obeyed the voice of the Lord … And the people feared the Lord"* (Hag 1:12).; *"I am with you, declares the Lord"* (1:13).; *"And the Lord stirred up the spirit of Zerubbabel … and the spirit of all the remnant of the people. And they came and worked"* (1:14).; The stirring follows obedience, fear and a word of presence, and it ends in work. Of Cyrus: *"I have stirred him up in righteousness … he shall build my city and set my ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Hag 1:13 (declares)
- **Observation 18234** (prior-capture, tag statement, status draft): Rev 11:6 | The two witnesses' power, "as often as they desire", within "the days of their prophesying"; then they are killed (11:7) | Ch 11 *Authority as a standing* (power given for a time and used at will)
  - applies to 1 occurrence(s): Rev 11:6 (prophesying)
- **Observation 18278** (prior-capture, tag face, status draft): Face: L02. God swears by his own life; Hits / verses: 24 / 24; What differs: "As I live, declares the Lord God" (16 of the 24 in Ezekiel); Example verses: Eze 33:11; Num 14:21; Deu 32:40; Rom 14:11
  - applies to 1 occurrence(s): Eze 33:11 (declares)
- **Observation 18324** (prior-capture, tag face, status draft): Face: W16. The sword roused against the shepherd; Hits / verses: 1 / 1; Life and death?: yes: a death God declares; Example: Zec 13:7
  - applies to 1 occurrence(s): Zec 13:7 (declares)
- **Observation 18877** (prior-capture, tag statement, status draft): Hiding from God: In each scene where a person hides from God, something of God is perceived first: a sound (Genesis 3:10), God naming himself (Exodus 3:6), "the terror of the Lord, and … the splendor of his majesty" (Isaiah 2:10), "the face of him who is seated on the throne, and … the wrath of the Lamb" (Revelation 6:16).; Adam hid because he knew he was naked (Genesis 3:10).; Moses "hid his face, for he was afraid to look at God" (Exodus 3:6), and no wrong is named.; At the end, people call "to the mountains and rocks, 'Fall on us and hide us'", for "who can stand?" (Revelation 6:16–17).; Job names the one condition on which he will not hide: "Only grant me two things, then I will not hide ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Jer 23:24 (declares)
- **Observation 18887** (prior-capture, tag statement, status draft): It can be not hidden at all. "They proclaim their sin like Sodom; they do not hide it. Woe to them! For they have brought evil on themselves" (Isaiah 3:9).
  - applies to 1 occurrence(s): Isa 3:9 (proclaim)
- **Observation 19149** (prior-capture, tag statement, status draft): Jer 30:21. *"Their prince shall be one of themselves; their ruler shall come out from their midst; I will make him draw near, and he shall approach me, for who would dare of himself to approach me? declares the Lord."*
  - applies to 1 occurrence(s): Jer 30:21 (declares)
- **Observation 19171** (prior-capture, tag statement, status draft): 13.1 *Ruling*: "His reign, and the nations' rage" (Rev 11:17–18) has God's reign with wrath.; Isa 52:7–9 is the other face: his reign is good news, joined to peace, salvation and comfort. This; sits with "The ruler to come", where "His rule comes with peace".
  - applies to 1 occurrence(s): Isa 52:7 (good news)
- **Observation 19178** (prior-capture, tag statement, status draft): Isa 52:7 | none (ruling) | God's reign as good news, with peace and comfort | 13.1 *Ruling*; the hearers' joy stays with M70 (OT-97.40)
  - applies to 1 occurrence(s): Isa 52:7 (good news)
- **Observation 19224** (prior-capture, tag statement, status draft): (a) Concealing one's own wrong. Each case has its own sequence: Achan: "when I saw … then I coveted them and took them. And see, they are hidden in the earth inside my tent" (Jos 7:21); Joshua: "tell me now what you have done; do not hide it from me" (7:19); Achan: "Truly I have sinned" (7:20); "behold, it was hidden in his tent" (7:22); Seeing, coveting, taking, hiding, being demanded to disclose, confessing, being found.; Moses: "He looked this way and that, and seeing no one, he struck down the Egyptian and hid him in the sand" (Exo 2:12). When the deed surfaces: "Moses was afraid, and thought, 'Surely the thing is known'" (2:14). Concealment fails, and fear follows.; The hidden adultery: ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 3:9 (proclaim)
- **Observation 19226** (prior-capture, tag statement, status draft): (c) Not withholding God's word or works.; "I have not hidden your deliverance within my heart; I have spoken" (Psa 40:10). The seat is where a word would be held back.; "We will not hide them from their children, but tell to the coming generation" (Psa 78:4).; "what is with the Almighty I will not conceal" (Job 27:11); "what wise men have told, without hiding it from their fathers" (Job 15:18).; "This would be my comfort … for I have not denied [concealed] the words of the Holy One" (Job 6:10): having not concealed is Job's comfort in pain.; "proclaim, conceal it not" (Jer 50:2).
  - applies to 1 occurrence(s): Jer 50:2 (proclaim)
- **Observation 19415** (prior-capture, tag statement, status draft): 1.6 Plans for welfare, and thought for the one in need: *"For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope"* (Jer 29:11).; The verse looks ahead to *"When seventy years are completed"* (29:10).; It is followed by *"You will seek me and find me, when you seek me with all your heart"* (29:13).; *"As for me, I am poor and needy, but the Lord takes thought for me"* (Psa 40:17).; *"But God will not take away life, and he devises means so that the banished one will not remain an outcast"* (2Sa 14:14). The wise woman says it against the fact that *"We must all die"*.
  - applies to 1 occurrence(s): Jer 29:11 (declares)
- **Observation 19417** (prior-capture, tag statement, status draft): 1.8 Before the ages, not from works: *"because of his own purpose and grace, which he gave us in Christ Jesus before the ages began"* (2Ti 1:9).; *"though they were not yet born and had done nothing either good or bad—in order that God's purpose of election might continue, not because of works but because of him who calls"* (Rom 9:11).; *"according to the purpose of him who works all things according to the counsel of his will"* (Eph 1:11).; *"the mystery of his will, according to his purpose, which he set forth in Christ as a plan for the fullness of time, to unite all things in Christ"* (Eph 1:9–10).; *"This was according to the eternal purpose that he has realized in Christ Jesus our Lord ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Eph 1:9 (set forth)
- **Observation 19419** (prior-capture, tag statement, status draft): 1.10 A person can refuse it, or serve it: *"but the Pharisees and the lawyers rejected the purpose of God for themselves, not having been baptized by him"* (Luk 7:30). Over against them, the people and the tax collectors *"declared God just"* (7:29).; *"For David, after he had served the purpose of God in his own generation, fell asleep"* (Act 13:36).
  - applies to 1 occurrence(s): Luk 7:29 (declared)
- **Observation 19588** (prior-capture, tag statement, status draft): Choice: Laid on Job: *"For you must choose, and not I; therefore declare what you know"* (v33).
  - applies to 1 occurrence(s): Job 34:33 (declare)
- **Observation 19609** (prior-capture, tag statement, status draft): Isaiah 44:2: "Fear not, O Jacob my servant, Jeshurun whom I have chosen": The chapter opens directly after a threat: *"deliver Jacob to utter destruction and Israel to reviling"* (43:28). Then: *"But now hear, O Jacob my servant, Israel whom I have chosen!"* (44:1). The "fear not" comes right after the words of destruction.; The ground of not fearing is who the Lord is to the one chosen: *"the Lord who made you, who formed you from the womb and will help you: Fear not, O Jacob my servant, Jeshurun whom I have chosen"* (v2). He made, he formed, he will help, and he has chosen. The chosen person is not told to be brave. He is told who has chosen him.; What follows is given to the chosen one's ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Isa 44:8 (declared)
- **Observation 20014** (prior-capture, tag statement, status draft): 3.6 A purpose held: resolve, aim and the mind set: *"I have purposed that my mouth will not transgress"* (Psa 17:3). The psalmist sets a course ahead for his own speech, under God's testing *"by night"*.; *"exhorted them all to remain faithful to the Lord with steadfast purpose"* (Act 11:23).; *"my teaching, my conduct, my aim in life, my faith"* (2Ti 3:10).
  - applies to 1 occurrence(s): Act 11:23 (exhorted)
- **Observation 20135** (prior-capture, tag statement, status draft): Isaiah 30 joins the refusing will to planning in one passage. It opens: *"Ah, stubborn children," declares the Lord, "who carry out a plan, but not mine"* (Isa 30:1). It goes on to the people *"unwilling to hear the instruction of the Lord"* (30:9) and ends the oracle with *"But you were unwilling"* (30:15). Here refusing God's word goes with carrying out a plan of one's own. This is the closest the Hebrew verses come to your continuum, and it is a single passage, not a pattern.
  - applies to 1 occurrence(s): Isa 30:1 (declares)
- **Observation 20305** (prior-capture, tag statement, status draft): Job 34:4 — Elihu: "Let us choose what is right; let us know among ourselves what is good": Elihu is angry with both sides. He *"burned with anger at Job because he justified himself rather than God"*, and at the friends *"because they had found no answer, although they had declared Job to be in the wrong"* (32:2–3).; He calls the listeners to weigh Job's case together, and calls that weighing a choosing: *"Hear my words, you wise men"* … *"for the ear tests words as the palate tastes food"*; *"Let us choose what is right; let us know among ourselves what is good"* (v2–4). The choosing here is not of a course of life. It is a judgement: picking out what is right in the case before them.; The ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 32:3 (declared)
- **Observation 20307** (prior-capture, tag statement, status draft): Job 34:33 — Elihu: "For you must choose, and not I": Elihu frames a confession and asks whether Job will make it: *"For has anyone said to God"*: *"I have borne punishment; I will not offend any more"*; *"teach me what I do not see; if I have done iniquity, I will do it no more"* (v31–32). Then: *"Will he then make repayment to suit you, because you reject it? For you must choose, and not I; therefore declare what you know"* (v33).; Two things stand in the verse:
  - applies to 1 occurrence(s): Job 34:33 (declare)
- **Observation 20310** (prior-capture, tag statement, status draft): Job 36:21 — Elihu: "this you have chosen rather than affliction": Elihu speaks *"on God’s behalf"* (v2), and his speech is about what affliction is for: *"if they are bound in chains and caught in the cords of affliction, then he declares to them their work … He opens their ears to instruction and commands that they return from iniquity"* (v8–10); *"If they listen and serve him, they complete their days in prosperity … But if they do not listen, they perish"* (v11–12); *"He delivers the afflicted by their affliction and opens their ear by adversity"* (v15); In Elihu's account, affliction is how God opens the ear.; Then he turns to Job, and what he sees in him is inward: *"you are full of the ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Job 36:9 (declares)
- **Observation 20564** (prior-capture, tag statement, status draft): *logizomai* | God reckons righteousness · God does not count sin · faith reckons God able · told to reckon oneself dead to sin · told to think on what is excellent · love does not reckon wrong · "may it not be charged" · others' estimate · suspicion · counting on boldness · claiming credit, denied · numbered with transgressors · counted as nothing · counted as offspring · wages counted as due, not gift · a calculation that became prophecy | Rom 4 (×11); Gal 3:6; Jam 2:23 · Rom 4:8; 2Co 5:19 · Heb 11:19 · Rom 6:11 · Phili 4:8 · 1Co 13:5 · 2Ti 4:16 · 1Co 4:1; 1Pe 5:12; 2Co 11:5; 12:6 · 2Co 10:2 · 2Co 10:2 · 2Co 3:5 · Luk 22:37 · Act 19:27 · Rom 9:8 · Rom 4:4 · Joh 11:50–51 | Who reckons (God, ... (cut; the whole text is in the workbook)
  - applies to 1 occurrence(s): Joh 11:51 (prophesied)
- **Observation 12524** (strand-reading, tag key-statement, status resolved): His purpose is before the ages and not from works: "because of his own purpose and grace, which he gave us in Christ Jesus before the ages began" (2Ti 1:9); "in order that God's purpose of election might continue, not because of works but because of him who calls" (Rom 9:11); "according to the purpose of him who works all things according to the counsel of his will" (Eph 1:11); "the mystery of his will, according to his purpose, which he set forth in Christ" (Eph 1:9); "the eternal purpose that he has realized in Christ Jesus our Lord" (Eph 3:11); "whom God put forward as a propitiation by his blood" (Rom 3:25).
  - meaning: God's purpose precedes the person and works, and is set forth in Christ.
  - implication: The purpose is grace, given before the ages (2Ti 1:9).
  - applies to 1 occurrence(s): Eph 1:9 (set forth)

### 4.3 The retired catalogue observations (19, live)

The September catalogue stages (char-answers, char-reading, char-subgroup, char-synergy, verse-reading) recorded one short verdict for each word in each verse. They are counted here by stage and tag; each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.

| stage | tag | live observations |
|---|---|---|
| verse-reading | answered-no-flag | 9 |
| verse-reading | not-related-to-meaningful-word | 7 |
| verse-reading | tightly-related | 3 |

### 4.4 Withdrawn observations (10)

A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet `Withdrawn observations`; they are not part of the sections above.

| stage | withdrawn observations |
|---|---|
| verse-reading | 10 |

| reason as stored | observations |
|---|---|
| no change record | 10 |

## 5. Claims and the narrative

41 claims rest on these occurrences: 1 on an observation of these words and 40 reached only because one of their sources is a verse where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.

### 5.1 Claims resting on an observation of these words (1)

- **C-379** (narrative, verdict New, status current, in narrative 1): God's purpose stands before the ages, does not rest on works, and is set forth in Christ.
  - beyond the text: gathers the Pauline purpose verses into one account
  - rests on: observation 12524 (strand-reading key-statement, live; Eph 1:9)
  - told in: chapter 13.1 Divine, Purposing

### 5.2 Claims reached by a verse only (40)

Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.

| claim | claim text | reached by verse | member word and code in that verse | status | told in |
|---|---|---|---|---|---|
| 2-12 | "God is spirit" (Joh 4:24) stands. But Scripture speaks freely of God's soul ("my soul shall not abhor you", Lev 26:11; "my soul hates", Isa 1:14; "my soul delights", Isa 42:1; he swears by his soul, Amo 6:8) and God's heart (Gen 6:6; Hos 11:8). No ranking of the words follows (dep §3.10) | Amo 6:8 | declares H5002 | current | chapter 11 Other sides of the inner being, 8. God has a heart and a soul |
| 3-3 | The original itself cites "the Lord who made our souls" (Jer 38:16). Also: "The Spirit of God has made me, and the breath of the Almighty gives me life" (Job 33:4). Both are made by God. The distinct-origins argument does not hold | Zec 12:1 | declares H5002 | current | not told in a section |
| 9-4 | Most "spirit of …" phrases name a disposition that comes upon a person; the verse does not name a being. The same phrasing is used for good gifts: a spirit of wisdom, skill, grace, justice. Some are given by God: "the Lord has poured out upon you a spirit of deep sleep" (Isa 29:10); the harmful spirit "from the Lord" (1Sa 16:14); God "sent an evil spirit" (Judg 9:23); the Lord "put a lying spirit" in the prophets' mouths (1Ki 22:23). 2Ti 1:7 says "God gave us a spirit not of fear". Spirit-beings are real (unclean spirits cast out; the spirit of divination, Act 16:16), but the one-to-one mapping to vice families is not in the text (SC; dep §2.3c; D §11.4) | 1Ki 22:23 | declared H1696I | current | not told in a section |
| 10-3 | "Within" is already the OT promise (Eze 36:27; 37:14). The OT also has the Spirit turning a man "into another man" (1Sa 10:6) | Eze 36:27; 37:14; 1Sa 10:6 | declares H5002; prophesy H5012 | current | not told in a section |
| C-90 | Paul uses sleep to speak to grief: grief with hope is set apart from grief without hope, and the hope rests on Christ's rising | 1 Thessalonians 4:13-15 | declare G3004G | current | chapter 02 Life, breath and death, Sleep and waking (1 earlier telling(s) in the workbook) |
| C-107 | Prophetic oracles against kings and nations speak of the dead in Sheol as stirred, speaking and comforted | Ezekiel 32:31 | declares H5002 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-110 | With God, the dead are carried, blessed and at rest | 1 Peter 4:6 | preached G2097 | current | chapter 02 Life, breath and death, After death (1 earlier telling(s) in the workbook) |
| C-121 | God has no pleasure in anyone's death and calls for turning; the turning is a considered act that reaches back over the past, and trust can lean the wrong way | Ezekiel 18:23; Ezekiel 18:32; Ezekiel 33:10-11 | declares H5002 | current | chapter 02 Life, breath and death, Life set before a person (2 earlier telling(s) in the workbook) |
| C-128 | God swears by his own life, and the oath carries what he wants and what he will do | Ezekiel 33:11; Ezekiel 20:3 | declares H5002 | current | chapter 02 Life, breath and death, Living before God (1 earlier telling(s) in the workbook) |
| C-139 | Scripture speaks of death in more than one way: the body's death, death in the living, dying to sin, a death beyond death, death as a power, and the living made like the dead | Luke 9:60 | proclaim G1229 | current | chapter 02 Life, breath and death, Life, and judgment; chapter 02 Life, breath and death, Death spoken of in more than one way (3 earlier telling(s) in the workbook) |
| C-146 | Inner things can perish: hope, endurance, courage (the heart), wisdom and truth | Jeremiah 4:9 | declares H1931; declares H5002 | current | chapter 02 Life, breath and death, Death in the living (1 earlier telling(s) in the workbook) |
| C-155 | A death is met by those who remain: grief, not watching, fasting and then eating, reproach, limits on mourning, mourning withheld, and death not taken to heart | Jeremiah 34:5 | declares H5002 | current | chapter 02 Life, breath and death, Those left behind (3 earlier telling(s) in the workbook) |
| C-160 | The making alive rests on a death, and Christ went to it himself | Zechariah 13:7 | declares H5002 | current | chapter 02 Life, breath and death, Made alive (2 earlier telling(s) in the workbook) |
| C-167 | Humility is not a feeling in the verses; they speak of it as an act, a standing, a quality sought and walked in, a state of the spirit, a place taken, something done to a person, and God's own way | 2 Kings 22:19 | declares H5002 | current | chapter 10.14 Humility, (opening) (1 earlier telling(s) in the workbook) |
| C-169 | Humbling oneself is done before someone: God, or the prophet who carries his word | 2 Kings 22:19 | declares H5002 | current | chapter 10.14 Humility, It faces someone; chapter 10.9 Relating to God, Humbling oneself before God (2 earlier telling(s) in the workbook) |
| C-170 | Most often a person humbles himself when a word reaches him, and the humbling owns that God is right | 2 Kings 22:19 | declares H5002 | current | chapter 10.14 Humility, It answers a word heard; chapter 10.9 Relating to God, Humbling oneself before God (2 earlier telling(s) in the workbook) |
| C-171 | Humbling happens in the heart; Hezekiah's is the same heart turning back from its own pride | 2 Kings 22:19; 2 Chronicles 34:27 | declares H5002 | current | chapter 04 The heart, The heart and anger; chapter 10.7 Choosing and setting direction, Willing; chapter 10.13 Anger, The heart that turns, and the heart that does not; chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit; chapter 10.14 Humility, Where it happens; chapter 04 The heart, The heart humbled (6 earlier telling(s) in the workbook) |
| C-175 | God sees the one who humbles himself and answers, in measure; the humbling does not hold by itself | 2 Kings 22:19-20 | declares H5002 | current | chapter 10.13 Anger, The heart that turns, and the heart that does not; chapter 10.14 Humility, God sees it, and answers in measure; chapter 10.9 Relating to God, Humbling oneself before God (4 earlier telling(s) in the workbook) |
| C-187 | Humility goes with the ear that can take a reproof and a word, and does not answer before it hears | Isaiah 66:2 | declares H5002 | current | chapter 10.14 Humility, Humility as a way of walking; chapter 10.2 Knowing and hearing, Humility and hearing (3 earlier telling(s) in the workbook) |
| C-188 | What God looks to is set against a religious act in the humility passages (the fast, the walk, the house, the broken heart), as in the other passages gathered in 13.1; the offering follows the broken heart | Isaiah 66:1-3 | declares H5002 | current | chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 11 Other sides of the inner being, What changes the character; chapter 13.1 Divine, Delight; chapter 10.14 Humility, Humility as a way of walking (6 earlier telling(s) in the workbook) |
| C-189 | Where God and a broken heart meet he is near and heals; the verses tell the breaking by its cause and by whether it is brought to God, not by naming contrition or despair | Isaiah 61:1 | good news H0853; good news H1319; proclaim H7121I | current | chapter 04 The heart, The heart is the source; chapter 06 The spirit, The human spirit; chapter 10.2 Knowing and hearing, (opening); chapter 11 Other sides of the inner being, 4. One word, opposite values; chapter 14 Made new, Revived, restored, renewed; chapter 10.14 Humility, A lowly and contrite spirit; chapter 04 The heart, The heart humbled (9 earlier telling(s) in the workbook) |
| C-211 | Pride can design its own honour, and the honour it designed becomes the measure of its fall | Esther 6:6-13 | proclaiming H7121I | current | chapter 12 When the inner being goes wrong, Pride and the lifted-up heart and spirit (1 earlier telling(s) in the workbook) |
| C-213 | Pride, the boast and the mock belong together in the verses | Jeremiah 48:29-30 | declares H5002 | current | chapter 10.15 Pride, (opening) (1 earlier telling(s) in the workbook) |
| C-218 | Pride claims a place that is God's: likeness to the Most High, a god's seat, his temple | 2 Thessalonians 2:4 | proclaiming G0584 | current | chapter 10.15 Pride, The heart that says what God says (1 earlier telling(s) in the workbook) |
| C-219 | Pride deceives the one who holds it, and the fear one inspires in others can feed it | Jeremiah 49:16 | declares H5002 | current | chapter 10.15 Pride, The heart that says what God says (1 earlier telling(s) in the workbook) |
| C-228 | The verses do not condemn boasting as such; they judge it by what it rests on | Jeremiah 9:23-24 | declares H5002 | current | chapter 10.15 Pride, The boast (2 earlier telling(s) in the workbook) |
| C-241 | The Son's majesty is received and grounded, stands beside his being handed over, and does not defend itself against mockery; he did not grasp what pride grasps | Luke 22:64 | prophesy G4395 | current | chapter 10.15 Pride, The mock; chapter 13.1 Divine, Majesty (2 earlier telling(s) in the workbook) |
| C-251 | God's reign is spoken with wrath in one place, and as good news with peace, salvation and comfort in another | Isa 52:7 | good news H1319 | current | chapter 13.1 Divine, Ruling (1 earlier telling(s) in the workbook) |
| C-259 | God names judging the cause of the poor and needy as knowing him, and sets it against eyes and heart given only to gain | Jer 22:16 | declares H0853; declares H5002 | current | chapter 10.2 Knowing and hearing, (opening); chapter 10.6 Wanting, Possessions (2 earlier telling(s) in the workbook) |
| C-276 | Paul lets faith and hope rest on Christ having been raised | 1Cor 15:12 | proclaimed G2784 | current | chapter 02 Life, breath and death, Believed, questioned, denied (1 earlier telling(s) in the workbook) |
| C-282 | Fear and anguish are shown in the body, and the verses see them first in the hands: hands fall at a report, grow feeble as the heart melts, and are held as in labour | Eze 21:7 | declares H1961; declares H5002 | current | chapter 10.12 Fear, Fear in the body (1 earlier telling(s) in the workbook) |
| C-286 | In the hands verses, what weakens the hands is something heard, and what strengthens them is a word, another person, or God asked to do it | Eze 21:7 | declares H1961; declares H5002 | current | chapter 10.12 Fear, Fear in the body (1 earlier telling(s) in the workbook) |
| C-299 | Rule can be turned into injustice, and power can be given for a time and used at will | Rev 11:6 | prophesying G4394 | current | chapter 11 Other sides of the inner being, Authority as a standing (1 earlier telling(s) in the workbook) |
| C-332 | God chooses a people out of love, not for their number; the choosing names them his treasured possession and his chosen ones, does not cast them off, and is for their knowing him. | Isa 43:10 | declares H5002 | current | chapter 13.1 Divine, Choosing; chapter 10.7 Choosing and setting direction, Being chosen |
| C-333 | God's choosing of a person for a task brings that person near and lays a charge on them; the one chosen still has to act. | Mat 12:18 | proclaim G0518 | current | chapter 10.7 Choosing and setting direction, Being chosen; chapter 13.1 Divine, Choosing |
| C-338 | The choice is the chooser's own: it is placed on them and not on another, honoured by others, and given of one's own accord. | Job 34:33 | declare H1696I | current | chapter 10.7 Choosing and setting direction, A choice that is honoured; chapter 10.7 Choosing and setting direction, Choosing before God; chapter 10.7 Choosing and setting direction, Choices weighed by another |
| C-356 | The power to look ahead is turned most often against another person: planned in the heart, done together, aimed at the righteous and the weak, hidden behind a friendly word, pinned on the other side, and met by the plea of another. | Zec 8:17 | declares H5002 | current | chapter 10.10 Relating to others, Plotting against another; chapter 10.11 Hiding and disclosing, The hidden trap |
| C-361 | God also thinks and plans: his plan stands where human plans cross it, he takes thought for the one in need, and he speaks in his heart. | Jer 29:11 | declares H5002 | current | chapter 11 Other sides of the inner being, 8. God has a heart and a soul; chapter 10.4 Thinking, Small, passing, and wholly seen; chapter 13.1 Divine, Purposing |
| C-364 | A purpose can be set ahead and held, for one's own speech and faithfulness; it can be kept and directed by God, and the mind's setting decides its direction. | Act 11:23 | exhorted G3870 | current | chapter 10.7 Choosing and setting direction, Planning |
| C-376 | God forms a plan, makes it known, carries it out, and those it came upon recognise it afterward. | Act 20:27 | declaring G0312 | current | chapter 13.1 Divine, Purposing |

### 5.3 The narrative sections that tell these claims (51)

The text of each section is in the workbook sheet `Narrative`.

| section | chapter | heading | claims told |
|---|---|---|---|
| 8 | 02 Life, breath and death | Life set before a person | C-121 |
| 9 | 02 Life, breath and death | Living before God | C-128 |
| 13 | 02 Life, breath and death | Death in the living | C-146 |
| 14 | 02 Life, breath and death | Sleep and waking | C-90 |
| 21 | 02 Life, breath and death | Made alive | C-160 |
| 28 | 02 Life, breath and death | Life, and judgment | C-139 |
| 29 | 02 Life, breath and death | After death | C-107, C-110 |
| 45 | 04 The heart | The heart and anger | C-171 |
| 46 | 04 The heart | The heart is the source | C-189 |
| 64 | 06 The spirit | The human spirit | C-189 |
| 122 | 10.2 Knowing and hearing | (opening) | C-189, C-259 |
| 144 | 10.4 Thinking | Small, passing, and wholly seen | C-361 |
| 180 | 10.6 Wanting | Possessions | C-259 |
| 187 | 10.7 Choosing and setting direction | Choosing before God | C-338 |
| 188 | 10.7 Choosing and setting direction | Being chosen | C-332, C-333 |
| 191 | 10.7 Choosing and setting direction | A choice that is honoured | C-338 |
| 196 | 10.7 Choosing and setting direction | Planning | C-364 |
| 197 | 10.7 Choosing and setting direction | Willing | C-171 |
| 200 | 10.7 Choosing and setting direction | Choices weighed by another | C-338 |
| 229 | 10.10 Relating to others | Plotting against another | C-356 |
| 240 | 10.11 Hiding and disclosing | The hidden trap | C-356 |
| 282 | 10.13 Anger | The heart that turns, and the heart that does not | C-171, C-175 |
| 296 | 11 Other sides of the inner being | 4. One word, opposite values | C-188, C-189 |
| 297 | 11 Other sides of the inner being | What changes the character | C-188 |
| 301 | 11 Other sides of the inner being | Authority as a standing | C-299 |
| 302 | 11 Other sides of the inner being | 8. God has a heart and a soul | 2-12, C-361 |
| 307 | 12 When the inner being goes wrong | Pride and the lifted-up heart and spirit | C-171, C-211 |
| 323 | 13.1 Divine | Choosing | C-332, C-333 |
| 324 | 13.1 Divine | Purposing | C-361, C-376, C-379 |
| 326 | 13.1 Divine | Delight | C-188 |
| 329 | 13.1 Divine | Ruling | C-251 |
| 338 | 14 Made new | Revived, restored, renewed | C-189 |
| 349 | 02 Life, breath and death | Death spoken of in more than one way | C-139 |
| 351 | 02 Life, breath and death | Those left behind | C-155 |
| 352 | 10.14 Humility | (opening) | C-167 |
| 355 | 10.14 Humility | It faces someone | C-169 |
| 356 | 10.14 Humility | It answers a word heard | C-170 |
| 357 | 10.14 Humility | Where it happens | C-171 |
| 361 | 10.14 Humility | God sees it, and answers in measure | C-175 |
| 366 | 10.14 Humility | Humility as a way of walking | C-187, C-188 |
| 367 | 10.14 Humility | A lowly and contrite spirit | C-189 |
| 374 | 10.2 Knowing and hearing | Humility and hearing | C-187 |
| 376 | 10.9 Relating to God | Humbling oneself before God | C-169, C-170, C-175 |
| 378 | 04 The heart | The heart humbled | C-171, C-189 |
| 381 | 10.15 Pride | (opening) | C-213 |
| 384 | 10.15 Pride | The heart that says what God says | C-218, C-219 |
| 387 | 10.15 Pride | The boast | C-228 |
| 388 | 10.15 Pride | The mock | C-241 |
| 395 | 13.1 Divine | Majesty | C-241 |
| 401 | 02 Life, breath and death | Believed, questioned, denied | C-276 |
| 403 | 10.12 Fear | Fear in the body | C-282, C-286 |

## 6. Phrases attached to the collection (5)

A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and the live observation nodes whose word is the phrase.

| phrase | link | route | occurrences | with engagement | live nodes on the phrase | observations |
|---|---|---|---|---|---|---|
| good news | 11712 | good news is placed in preach by meaning (step 7 correction) | 21 | 0 | 8 | 4 |
| preach the gospel | 7942 | english route: word preach | 8 | 0 | 2 | 2 |
| preached the gospel | 7943 | english route: word preached | 3 | 0 | 0 | 0 |
| preaching the gospel | 7944 | english route: word preaching | 3 | 0 | 0 | 0 |
| set forth | 8173 | strong route: strong H5608A via declare; strong H5608A via declared | 3 | 0 | 2 | 2 |

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

