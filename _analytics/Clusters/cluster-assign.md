# Cluster-assignment quality report

> Generated 2026-09-05T16:25:28Z by `cluster.validate`. Read-only findings, not a gate.

- `strong` rows with no cluster assignment at all: **7969**
- `backfill`-origin, non-T2 assignment, not yet promoted (should be `word`): **0**
- exception — non-T2 assignment with no `word_registry` link: **772**
- exception — `backfill` code with an active/clustered sibling: **829**

## Contents

- [Summary](#summary)
- [Exception - no word](#exception-non-t2-cluster-no-word-registry-link)
- [Exception - sibling conflict](#exception-backfill-code-with-an-activeclustered-sibling)

<a id="summary"></a>
## Summary

15293 strong(s) checked
unclassified: 7969
not yet promoted (backfill, non-T2, has a word): 0
exception — no word: 772
exception — sibling conflict: 829

<a id="exception-non-t2-cluster-no-word-registry-link"></a>
## Exception -- non-T2 cluster, no word_registry link

`H8088A` — 'sound', cluster M62
`H2048A` — 'to mock', cluster M08
`H5607A` — 'mockery', cluster M06,M08
`H8178A` — 'shuddering', cluster M01
`H3856A` — 'to languish', cluster M24
`H5254G` — 'to test', cluster M35
`H4148G` — 'discipline', cluster M15,M16
`H5183A` — 'quietness', cluster M33
`H7067G` — 'Jealous [God]', cluster FLAG,M18,M28
`H4654A` — 'ruin', cluster M27,M55
`H7032G` — 'voice: sound', cluster M84
`H8186A` — 'horror', cluster M01
`H0430G` — 'God', cluster T7
`H4487` — 'to count', cluster M26
`H6579` — 'noble', cluster M34
`H9002` — 'and', cluster T6
`H3808` — 'not', cluster T5
`H2196` — 'to enrage', cluster M02
`H0007` — 'to destroy', cluster M10
`H2164` — 'to agree', cluster M44
`H2324` — 'to show', cluster M05
`H3809` — 'not', cluster T5
`H4406` — 'word', cluster M65
`H4978` — 'gift', cluster M39
`H5649` — 'servant/slave', cluster M36
`H5957` — 'perpetuity', cluster M34
`H6032` — 'to answer', cluster M24,M41
`H6591` — 'interpretation', cluster M63
`H7593` — 'to ask', cluster M21
`H8133` — 'to change', cluster M45
`H5642A` — 'to hide', cluster M20
`H7314` — 'height', cluster M08
`H2122` — 'splendor', cluster M71
`H2255` — 'to destroy', cluster M10
`H4437` — 'kingdom', cluster M72
`H5208` — 'soothing', cluster M04
`H5673` — 'service', cluster M36
`H7236` — 'to grow great', cluster M23
`H1907` — 'counselor', cluster M16,M17
`H4398` — 'angel', cluster T9
`H5943` — 'Most High [God]', cluster M72
`H0852` — 'sign', cluster M43
`H1922` — 'to honor', cluster M71
`H1923` — 'honor', cluster M71
`H7032H` — 'voice', cluster M84
`H7261` — 'noble', cluster M34
`H7680` — 'to grow great', cluster M23
`H8215` — 'low', cluster M09
`H8421G` — 'to return: return', cluster M11
`H8627` — 'to confirm', cluster M62
`H0263` — 'explanation', cluster M15,M43
`H2112` — 'to tremble', cluster M01
`H6590` — 'to interpret', cluster M43,M63
`H2248` — 'crime', cluster M55
`H2908` — 'fasting', cluster M21
`H7712` — 'to strive', cluster M34
`H1519` — 'to strive', cluster M34
`H5202` — 'to keep', cluster M74
`H7920` — 'to contemplate', cluster M15
`H8046` — 'to destroy', cluster M10
`H0120G` — 'man', cluster T8
`H1002` — 'palace', cluster M72
`H2416C` — 'living thing', cluster M25
`H3588A` — 'for', cluster T6
`H6743B` — 'to prosper', cluster M46
`H8462` — 'beginning', cluster M17
`H0309` — 'to delay', cluster M09
`H0376G` — 'man', cluster T8
`H0408` — 'not', cluster T5
`H0410G` — 'God', cluster T7
`H3068G` — 'LORD', cluster T7
`H0582` — 'human', cluster T8
`H2244` — 'to hide', cluster M20
`H0410K` — 'god', cluster T7
`H0643` — 'palace', cluster M72
`H0961` — 'plunder', cluster M24
`H1925` — 'glory', cluster M22
`H2388J` — 'to strengthen: prevail over', cluster M23
`H3368` — 'precious', cluster M29
`H4924B` — 'fatness', cluster M46
`H5782` — 'to rouse', cluster M25
`H8045` — 'to destroy', cluster M10
`H8052` — 'tidings', cluster M82
`H2416A` — 'alive', cluster M25
`H2416E` — 'life', cluster M25
`H5703` — 'perpetuity', cluster M34
`H4867` — 'wave', cluster M01
`H2394` — 'force', cluster M23
`H6116` — 'assembly', cluster M05,M44
`H7111` — 'splinter', cluster M02
`H8047G` — 'horror: destroyed', cluster M01
`H5012` — 'to prophesy', cluster M42,M43
`H6951` — 'assembly', cluster M05,M44
`H5789` — 'to help', cluster M38
`H6563` — 'plunder', cluster M24
`H5979` — 'support', cluster M70
`H0341` — 'enemy', cluster M06,M44
`H2256D` — 'destruction', cluster M55
`H2256M` — 'cord', cluster M03,T2
`H4496H` — 'resting', cluster M33
`H3384B` — 'to show', cluster M05
`H1854` — 'to crush', cluster M10,M24
`H2388H` — 'to strengthen: hold', cluster M23
`H6635B` — '[Lord of] Hosts', cluster M72
`H1060` — 'firstborn', cluster M37
`H0480` — 'woe!', cluster M03
`H6822` — 'to watch', cluster M74
`H8104H` — 'to keep: guard', cluster M74
`H4468` — 'kingdom', cluster M72
`H0269` — 'sister', cluster M44
`H0781` — 'to betroth', cluster M44
`H5040` — 'lewdness', cluster M57
`H6601B` — 'to entice', cluster M10,M77
`H5493H` — 'to turn aside: depart', cluster M11,M30
`H2502A` — 'to rescue', cluster M38
`H0561` — 'word', cluster M65
`H8186B` — 'horror', cluster M01
`H0188` — 'woe!', cluster M03
`H5074` — 'to wander', cluster M18,M76
`H5920H` — 'height', cluster M08
`H7701` — 'violence', cluster M10,M27
`H8088B` — 'report', cluster M82
`H1890` — 'gift', cluster M39
`H2803H` — 'to devise: count', cluster M64
`H2986` — 'to conduct', cluster M22,M76
`H5688` — 'cord', cluster M03,T2
`H8637` — 'to teach', cluster M15,M16
`H4397H` — 'messenger: angel', cluster T9
`H8104J` — 'to keep: careful', cluster M74
`H6987` — 'destruction', cluster M55
`H5331` — 'perpetuity', cluster M34
`G0032G` — 'angel', cluster T9
`G0032H` — 'angel: messenger', cluster T9
`G0079` — 'sister', cluster M44
`G0091` — 'to harm', cluster M24
`G0140` — 'to choose', cluster M37,M64
`G0310` — 'to cry out', cluster M42
`G0315` — 'to compel', cluster M23
`G0344` — 'to return', cluster M11
`G0372` — 'rest', cluster M33
`G0402` — 'to leave', cluster M59
`G0435G` — 'man', cluster T8
`G0436` — 'to oppose', cluster M06
`G0444` — 'a human', cluster T8
`G0476` — 'opponent', cluster M06
`G0527` — 'tender', cluster M05
`G0611` — 'to answer', cluster M24,M41
`G0622` — 'to destroy', cluster M10
`G0672` — 'to leave', cluster M59
`G0684` — 'destruction', cluster M55
`G0694` — 'money', cluster M28,M46
`G0726` — 'to seize', cluster M24
`G0928G` — 'to torture: torture', cluster M03
`G0930` — 'torturer', cluster M03,M27
`G0931` — 'torment', cluster M03
`G0936` — 'to reign', cluster M72
`G0997` — 'to help', cluster M38
`G1161` — 'then', cluster T6
`G1166` — 'to show', cluster M05
`G1321` — 'to teach', cluster M15,M16
`G1372` — 'to thirst', cluster M18,M29
`G1390` — 'gift', cluster M39
`G1401` — 'slave', cluster M78
`G1435` — 'gift', cluster M39
`G1518` — 'peacemaker', cluster M33
`G1577` — 'assembly', cluster M05,M44
`G1598` — 'to test/tempt', cluster M35
`G1654` — 'charity', cluster M05,T2
`G1718` — 'to show', cluster M05
`G1777` — 'liable for', cluster M55
`G1843` — 'to agree', cluster M44
`G1950` — 'to forget', cluster M81
`G2050` — 'devastation', cluster M27,M55
`G2083` — 'friend', cluster M05
`G2132` — 'to reconcile', cluster M05,M11
`G2168` — 'to thank', cluster M21,M49
`G2190` — 'enemy', cluster M06,M44
`G2198` — 'to live', cluster M25
`G2222` — 'life', cluster M25
`G2511` — 'to clean', cluster M12
`G2532` — 'and', cluster T6
`G2537` — 'new', cluster M45
`G2572` — 'to cover', cluster M38
`G2581` — 'Zealot', cluster M18,M21
`G2602` — 'beginning', cluster M17
`G2606` — 'to mock', cluster M08
`G2705` — 'to kiss', cluster M05
`G2770` — 'to gain', cluster M37
`G2873` — 'labor', cluster M24
`G2928` — 'to hide', cluster M20
`G2948` — 'crippled', cluster M73
`G2962H` — 'lord: master', cluster M72
`G3039` — 'to crush', cluster M10,M24
`G3332` — 'to leave', cluster M59
`G3361` — 'not', cluster T5
`G3423` — 'to betroth', cluster M44
`G3429` — 'to commit adultery', cluster M57
`G3501` — 'new', cluster M45
`G3523` — 'fasting', cluster M21
`G3554` — 'illness', cluster M73
`G3756` — 'no', cluster T5
`G3759` — 'woe!', cluster M03
`G3761` — 'nor', cluster T5
`G3844` — 'from/with/beside', cluster FLAG,T2
`G3985G` — 'to test/tempt: tempt', cluster M35
`G3985H` — 'to test/tempt: test', cluster M35
`G4090` — 'bitterly', cluster M03
`G4145` — 'rich', cluster M46
`G4328` — 'to look for', cluster M68
`G4416` — 'firstborn', cluster M37
`G4567` — 'Satan', cluster T4
`G4624` — 'to cause to stumble', cluster M77
`G4816` — 'to collect', cluster M17
`G4862` — 'with', cluster FLAG,T2
`G4889` — 'fellow slave', cluster M44,M78
`G4929` — 'to direct', cluster M09
`G5083H` — 'to keep: guard', cluster M74
`G5091` — 'to honor', cluster M71
`G5092` — 'honor', cluster M71
`G5263` — 'to show', cluster M05
`G5273` — 'hypocrite', cluster M14
`G5308` — 'high', cluster M08
`G5384` — 'friendly/friend', cluster M05
`G5413` — 'burden', cluster M78
`G5456H` — 'voice/sound: noise', cluster M84
`G5549` — 'to delay', cluster M09
`G5578` — 'false prophet', cluster M14
`G5580` — 'false Christ', cluster M14
`G5623` — 'to help', cluster M38
`G0216` — 'mute', cluster M53
`G0657` — 'to leave', cluster M59
`G0950` — 'to confirm', cluster M62
`G0984` — 'to hurt', cluster M24
`G1606` — 'to expire', cluster M24
`G1758` — 'to oppose', cluster M06
`G2512` — 'cleansing', cluster M12
`G3619` — 'building', cluster M52
`G4028` — 'to cover', cluster M38
`G4319` — 'to beg', cluster M21
`G5141` — 'to tremble', cluster M01
`G5290` — 'to return', cluster M11
`G0075` — 'to struggle', cluster M34
`G0364` — 'remembrance', cluster M82
`G0376` — 'crippled', cluster M73
`G0467` — 'to repay', cluster M26
`G0474` — 'to discuss', cluster M63
`G0482` — 'to help', cluster M38
`G0488` — 'to return', cluster M11
`G0525` — 'to release', cluster M59
`G0612` — 'answer', cluster M41,M42
`G0613` — 'to conceal', cluster M14
`G0620` — 'to leave', cluster M59
`G0840` — 'severe', cluster M24
`G0868` — 'to leave', cluster M59
`G0933` — 'palace', cluster M72
`G1000` — 'throwing', cluster M24
`G1070` — 'to laugh', cluster M04
`G1248` — 'service', cluster M36
`G1255` — 'to discuss', cluster M63
`G1298` — 'to trouble', cluster M03
`G1301` — 'to keep', cluster M74
`G1329` — 'to interpret', cluster M43,M63
`G1399` — 'female slave', cluster M78
`G1834` — 'to tell', cluster M42,M65
`G1880` — 'to return', cluster M11
`G1948` — 'to decide', cluster M63
`G2208` — 'Zealot', cluster M18,M21
`G2230` — 'to govern', cluster M72
`G2352` — 'to crush', cluster M10,M24
`G2800` — 'breaking', cluster M24
`G3168` — 'majesty', cluster M08
`G3312` — 'arbiter', cluster M15
`G3330` — 'to share', cluster M44
`G3521` — 'fasting', cluster M21
`G3528` — 'to conquer', cluster M23
`G3610` — 'slave', cluster M78
`G3681` — 'disgrace', cluster M07
`G3871` — 'to hide', cluster M20
`G4032` — 'to hide', cluster M20
`G4229` — 'thing', cluster M28,T2
`G4273` — 'traitor', cluster M14
`G4422` — 'to frighten', cluster M01
`G4485` — 'destruction', cluster M55
`G4617` — 'to sift', cluster M77
`G4648` — 'to watch out', cluster M06,M74
`G4661` — 'plunder', cluster M24
`G4780` — 'to conceal', cluster M14
`G4788` — 'to confine', cluster M23
`G4878` — 'to help', cluster M38
`G4884` — 'to seize', cluster M24
`G4990` — 'savior', cluster M79
`G5050` — 'perfection', cluster M61
`G5135` — 'to wound', cluster M03,M10
`G5172` — 'self-indulgence', cluster M28
`G5271` — 'to pretend', cluster M14
`G5311` — 'height', cluster M08
`G5345` — 'news', cluster M82
`G5370` — 'kiss', cluster M05
`G0937` — 'royal', cluster M72
`G1431` — 'free gift', cluster M38,M39
`G2059` — 'to interpret', cluster M43,M63
`G3105` — 'to rave', cluster M66
`G3605` — 'to stink', cluster M06
`G3942` — 'proverb', cluster M23,M35
`H5207` — 'soothing', cluster M04
`G0049` — 'purification', cluster M61
`G0052` — 'ignorance', cluster M63
`G0157` — 'charge', cluster M26
`G0178` — 'uncondemned', cluster M61
`G0236` — 'to change', cluster M45
`G0333` — 'to contemplate', cluster M15
`G0374` — 'to persuade', cluster M77
`G0442` — 'human', cluster T8
`G0677` — 'not stumbling', cluster M77
`G0777` — 'fasting', cluster M21
`G0778` — 'to strive', cluster M34
`G0780` — 'gladly', cluster M04
`G0970` — 'force', cluster M23
`G1175` — 'religion', cluster M31
`G1231` — 'to decide', cluster M63
`G1494` — 'sacrificed to idols', cluster M27,T2
`G1497` — 'idol', cluster M27,T2
`G1634` — 'to expire', cluster M24
`G1813` — 'to blot out', cluster M60
`G1917` — 'plot', cluster M06,M14
`G1962` — 'to accept', cluster M39
`G2016` — 'glorious', cluster M71
`G2026` — 'to build up/upon', cluster M52
`G2152` — 'pious', cluster M05
`G2207` — 'zealot', cluster M18,M21
`G2663` — 'rest', cluster M33
`G2687` — 'to quiet', cluster M33
`G2880` — 'to satisfy', cluster M38,M46
`G3116` — 'patiently', cluster M34
`G3143` — 'to testify', cluster M13,M35
`G3343` — 'to summon', cluster M37
`G3344` — 'to change', cluster M45
`G3635` — 'to delay', cluster M09
`G3905` — 'to prolong', cluster M25
`G3926` — 'to trouble', cluster M03
`G3985I` — 'to test/tempt: try', cluster M35
`G3987` — 'to try', cluster M77
`G4037` — 'to await', cluster M17,M68
`G4268` — 'foreknowledge', cluster M37
`G4288` — 'eagerness', cluster M29
`G4307` — 'foresight', cluster M15,M43
`G4384` — 'to predetermine', cluster M37
`G4389` — 'to encourage', cluster M52
`G4401` — 'to choose', cluster M37,M64
`G4467` — 'crime', cluster M55
`G4602` — 'silence', cluster M33
`G4945` — 'plot', cluster M06,M14
`G5093` — 'precious', cluster M29
`G5334` — 'news', cluster M82
`G5339` — 'to spare', cluster M05
`G6048` — 'judgment', cluster M26
`G0463` — 'tolerance', cluster M05
`G0663` — 'severity', cluster M06
`G0802` — 'untrustworthy', cluster M14
`G0949` — 'firm', cluster M19,M23
`G1384` — 'tested', cluster M35
`G1434` — 'free gift', cluster M38,M39
`G1558` — 'avenging', cluster M26
`G1731` — 'to show', cluster M05
`G1738` — 'just', cluster M12,M26
`G1878` — 'to remind', cluster M82
`G1943` — 'to cover', cluster M38
`G2644` — 'to reconcile', cluster M05,M11
`G4152` — 'spiritual', cluster M43,M47
`G4306` — 'to care for', cluster M05
`G4348` — 'stumbling block', cluster M77
`G4356` — 'acceptance', cluster M29
`G4417` — 'to stumble', cluster M77
`G4519` — 'hosts', cluster M72
`G4825` — 'counselor', cluster M16,M17
`G4832` — 'conformed', cluster M45
`G4837` — 'to encourage', cluster M52
`G4852` — 'to agree', cluster M44
`G4865` — 'to struggle', cluster M34
`G5245` — 'to conquer', cluster M23
`G5267` — 'accountable', cluster M26
`G5275` — 'to leave', cluster M59
`G5313` — 'height', cluster M08
`G5381` — 'hospitality', cluster M05
`G5542` — 'smooth talk', cluster M14,M65
`G1328` — 'interpreter', cluster M63
`G1396` — 'to enslave', cluster M78
`G1493` — "idol's temple", cluster M27,T2
`G1496` — 'idolater', cluster M27,T2
`G1652` — 'pitiful', cluster M05
`G1755` — 'working', cluster M23
`G2058` — 'interpretation', cluster M63
`G2619` — 'to cover', cluster M38
`G2908` — 'greater', cluster M23
`G3048` — 'collection', cluster M18
`G3348` — 'to share', cluster M44
`G4148` — 'to enrich', cluster M46
`G4821` — 'to reign with', cluster M72
`G4829` — 'to share', cluster M44
`G0718` — 'to betroth', cluster M44
`G1373` — 'thirst', cluster M18,M29
`G1389` — 'to distort', cluster M14
`G2236` — 'most gladly', cluster M04
`G2506` — 'destruction', cluster M55
`G2583` — 'rule', cluster M72
`G2676` — 'perfection', cluster M61
`G3841` — 'almighty', cluster M23
`G4255` — 'to predetermine', cluster M37
`G4349` — 'stumbling', cluster M77
`G4560` — 'fleshly', cluster M28
`G4705` — 'eager', cluster M34,M69
`G5569` — 'false brother', cluster M14
`G3445` — 'to form', cluster M61
`G3456` — 'to mock', cluster M08
`G5422` — 'to deceive', cluster M14
`G0604` — 'to reconcile', cluster M05,M11
`G0781` — 'unwise', cluster M63
`G2282` — 'to care for', cluster M05
`G2940` — 'cunning', cluster M14
`G3809` — 'discipline', cluster M15,M16
`G5603` — 'song', cluster M22,M42
`G0138` — 'to choose', cluster M37,M64
`G0951` — 'confirmation', cluster M62
`G1394` — 'gift', cluster M39
`G4426` — 'to frighten', cluster M01
`G5251` — 'to exalt', cluster M08,M22
`G1018` — 'to rule', cluster M72
`G3884` — 'to deceive', cluster M14
`G4146` — 'richly', cluster M46
`G4733` — 'firmness', cluster M19,M23
`G5047` — 'perfection', cluster M61
`G2850` — 'flattery', cluster M14
`G3642` — 'fainthearted', cluster M20,M24
`G0462` — 'unholy', cluster M61
`G0594` — 'acceptance', cluster M29
`G1019` — 'to delay', cluster M09
`G1128` — 'to train', cluster M15
`G1226` — 'to insist', cluster M15
`G1236` — 'to live', cluster M25
`G1884` — 'to help', cluster M38
`G2272` — 'quiet', cluster M33
`G5382` — 'hospitable', cluster M05
`G0329` — 'to rekindle', cluster M45
`G0475` — 'to oppose', cluster M06
`G5367` — 'selfish', cluster M08
`G1993` — 'to silence', cluster M33
`G3711` — 'quick-tempered', cluster M02
`G4767` — 'hated', cluster M06
`G4994` — 'to train', cluster M15,T3
`G0661` — 'to repay', cluster M26
`G0464` — 'to struggle', cluster M34
`G0577` — 'to throw away', cluster M07
`G1585` — 'to forget', cluster M81
`G1776` — 'to trouble', cluster M03
`G2226` — 'living thing', cluster M25
`G2428` — 'supplication', cluster M21,M42
`G2514` — 'cleanness', cluster M12
`G2610` — 'to conquer', cluster M23
`G3172` — 'majesty', cluster M08
`G3645` — 'to destroy', cluster M10
`G3831` — 'assembly', cluster M05,M44
`G4007` — 'indeed', cluster M08,T2
`G4372` — 'new', cluster M45
`G0087` — 'impartial', cluster M26
`G0995` — 'outcry', cluster M84
`G1383` — 'testing', cluster M35
`G1503` — 'to resemble', cluster M15
`G1953` — 'forgetfulness', cluster M81
`G4507` — 'filth', cluster M53
`G5373` — 'friendship', cluster M05
`G5425` — 'to shudder', cluster M01
`G0081` — 'brotherhood', cluster M44
`G0934` — 'kingly', cluster M72
`G0980` — 'to live', cluster M25
`G2900` — 'mighty', cluster M23,T2
`G4509` — 'filth', cluster M53
`G4599` — 'to strengthen', cluster M23
`G5391` — 'friendly', cluster M05
`G5612` — 'to roar', cluster M84
`G1955` — 'explanation', cluster M15,M43
`G3024` — 'forgetfulness', cluster M81
`G3420` — 'remembrance', cluster M82
`G3913` — 'insanity', cluster M66
`G4740` — 'security', cluster M19
`G4761` — 'to distort', cluster M14
`G2434` — 'propitiation', cluster M79
`G0679` — 'without falling', cluster M34
`G0929` — 'torment', cluster M03,M35
`G0938G` — 'queen', cluster M72
`G2200` — 'hot', cluster M02
`G3045` — 'rich', cluster M46
`G3455` — 'to roar', cluster M84
`H0565A` — 'word', cluster M65
`H1067` — 'firstborn', cluster M37
`H2048B` — 'to deceive', cluster M14
`H2102` — 'to boil', cluster M02,M08
`H2934` — 'to hide', cluster M20
`H3513J` — 'to honor: dull', cluster M16,M22,T3
`H3722B` — 'to cover', cluster M38
`H4030` — 'precious thing', cluster M28
`H4241` — 'recovery', cluster M25
`H4397G` — 'messenger', cluster T9
`H4976` — 'gift', cluster M39
`H4979` — 'gift', cluster M39
`H5657` — 'service', cluster M36
`H5945A` — 'high', cluster M08
`H6349` — 'recklessness', cluster M66
`H6616` — 'cord', cluster M03,T2
`H6617` — 'to twist', cluster M57
`H6622` — 'to interpret', cluster M43,M63
`H6711` — 'to laugh', cluster M04
`H6967` — 'height', cluster M08
`H7122G` — 'to encounter: meet', cluster M37
`H7122I` — 'to encounter: chanced', cluster M37
`H7411B` — 'to deceive', cluster M14
`H7892A` — 'song', cluster M22,M42
`H8082` — 'rich', cluster M46
`H0483` — 'mute', cluster M53
`H1342` — 'to rise up', cluster M08
`H1826A` — 'to silence: stationary', cluster M33
`H1921` — 'to honor', cluster M71
`H2176` — 'song', cluster M22,M42
`H2287` — 'to celebrate', cluster M71
`H2319H` — 'new', cluster M45
`H2390` — 'stronger', cluster M23
`H2422` — 'vigorous', cluster M25
`H2750` — 'burning', cluster M01,M02
`H2803G` — 'to devise: design', cluster M64
`H3517` — 'heaviness', cluster FLAG,T2
`H3725` — 'atonement', cluster M10,M60
`H4020` — 'twisted', cluster M14
`H4290` — 'breaking', cluster M24
`H4340` — 'cord', cluster M03,T2
`H4744` — 'assembly', cluster M05,M44
`H4809G` — 'Meribah', cluster M02,T2
`H5327A` — 'to struggle', cluster M34
`H5526B` — 'to cover', cluster M38
`H5526E` — 'to cover', cluster M38
`H6363A` — 'firstborn', cluster M37
`H6531` — 'severity', cluster M06
`H6569` — 'refuse', cluster M27,M30
`H6696C` — 'to form', cluster M61
`H7067H` — 'jealous', cluster M02,M18
`H7461A` — 'trembling', cluster M01
`H7806` — 'to twist', cluster M57
`H7892B` — 'song', cluster M22,M42
`H8513` — 'hardship', cluster M24
`H8549G` — 'unblemished', cluster M61
`H1500` — 'violence', cluster M10,M27
`H1739` — 'sick', cluster M73
`H2893` — 'purifying', cluster M61
`H4383` — 'stumbling', cluster M77
`H4768` — 'greatness', cluster M23,M71
`H6186B` — 'to value', cluster M26
`H7106A` — 'to scrape', cluster M23
`H7147` — 'hostility', cluster M06
`H7673B` — 'to keep', cluster M74
`H7829` — 'illness', cluster M73
`H8549I` — 'unblemished: complete', cluster M61
`H0008` — 'destruction', cluster M55
`H0957` — 'plunder', cluster M24
`H1442` — 'to blaspheme', cluster M10b
`H4272` — 'to wound', cluster M03,M10
`H5081H` — 'noble', cluster M34
`H6363B` — 'firstborn', cluster M37
`H6979C` — 'to destroy', cluster M10
`H8323A` — 'to rule', cluster M72
`H1703` — 'word', cluster M65
`H1795` — 'crushing', cluster M10,M24
`H2388I` — 'to strengthen: ensure', cluster M23
`H2960` — 'burden', cluster M78
`H3631` — 'failing', cluster M24
`H3893` — 'vigor', cluster M23
`H4064` — 'disease', cluster M73
`H5603` — 'to cover', cluster M38
`H6028` — 'dainty', cluster M04
`H6618` — 'twisted', cluster M14
`H6952` — 'assembly', cluster M05,M44
`H6986` — 'destruction', cluster M55
`H7268` — 'quivering', cluster M01
`H7682` — 'to exalt', cluster M08,M22
`H7697` — 'madness', cluster M66
`H7760K` — 'to set: consider', cluster M15
`H8080` — 'to grow fat', cluster M46
`H8146` — 'hated', cluster M06
`H8541` — 'bewilderment', cluster M01
`H2247` — 'to hide', cluster M20
`H2525` — 'hot', cluster M02
`H7850` — 'scourge', cluster M06
`H8089` — 'report', cluster M82
`H2115` — 'to crush', cluster M10,M24
`H2717B` — 'to destroy', cluster M10
`H3499B` — 'cord', cluster M03,T2
`H3943` — 'to twist', cluster M57
`H4277` — 'to destroy', cluster M10
`H6128` — 'crooked', cluster M14
`H6574` — 'refuse', cluster M27,M30
`H7336` — 'to rule', cluster M72
`H0830H` — 'refuse', cluster M27,M30
`H2416B` — 'kinsfolk', cluster M25,T8
`H2638` — 'lacking', cluster M18,M24
`H4224B` — 'refuge', cluster M19
`H5770` — 'to watch', cluster M74
`H6145` — 'enemy', cluster M06,M44
`H6477` — 'bluntness', cluster M53
`H8138A` — 'to change', cluster M45
`H8213` — 'to abase', cluster M53
`H8549J` — 'unblemished: Thummim', cluster M61
`H0972` — 'chosen', cluster M29,M64
`H2416D` — 'community', cluster M44,T8
`H2424` — 'living', cluster M25
`H2645` — 'to cover', cluster M38
`H2841` — 'collection', cluster M18
`H3813` — 'to cover', cluster M38
`H4937A` — 'support', cluster M70
`H5273B` — 'musical', cluster M22
`H5379` — 'gift', cluster M39
`H6789` — 'to destroy', cluster M10
`H7463` — 'friend', cluster M05
`H7987` — 'quietness', cluster M33
`H1827` — 'silence', cluster M33
`H2715` — 'noble', cluster M34
`H4552` — 'support', cluster M70
`H4991` — 'gift', cluster M39
`H5447` — 'burden', cluster M78
`H5449` — 'burden', cluster M78
`H7182` — 'attentiveness', cluster M41
`H4933` — 'plunder', cluster M24
`H6122` — 'cunning', cluster M14
`H6675` — 'filth', cluster M53
`H8132` — 'to change', cluster M45
`H8594` — 'security', cluster M19
`H1927` — 'adornment', cluster M71
`H5329` — 'to conduct', cluster M22,M76
`H2810` — 'invention', cluster M14
`H7183B` — 'attentive', cluster M41
`H8196` — 'judgment', cluster M26
`H0153` — 'force', cluster M23
`H0252` — 'brother', cluster M14,T8
`H1059` — 'bitterly', cluster M03
`H2323` — 'new', cluster M45
`H3246` — 'beginning', cluster M17
`H5013` — 'to prophesy', cluster M42,M43
`H5642B` — 'to destroy', cluster M10
`H6402` — 'service', cluster M36
`H6744` — 'to prosper', cluster M46
`H8200` — 'to judge', cluster M26,M63
`H8589` — 'fasting', cluster M21
`H0548` — 'sure', cluster M62
`H2926` — 'to cover', cluster M38
`H7183A` — 'attentive', cluster M41
`H8442` — 'error', cluster M55
`H0012` — 'destruction', cluster M55
`H0013` — 'destruction', cluster M55
`H0597` — 'to compel', cluster M23
`H1055` — 'palace', cluster M72
`H6599` — 'edict', cluster FLAG,T2
`H0405` — 'burden', cluster M78
`H0562` — 'word', cluster M65
`H1623` — 'to scrape', cluster M23
`H1700` — 'cause', cluster M17
`H2862` — 'to seize', cluster M24
`H4561` — 'discipline', cluster M15,M16
`H4651` — 'refuse', cluster M27,M30
`H4879` — 'error', cluster M55
`H5076` — 'tossing', cluster M03
`H5243A` — 'to languish', cluster M24
`H5587B` — 'disquietings', cluster FLAG,T2
`H6761` — 'stumbling', cluster M77
`H7009` — 'adversary', cluster M06
`H7059` — 'to seize', cluster M24
`H7679` — 'to grow great', cluster M23
`H7722B` — 'devastation', cluster M27,M55
`H8235` — 'clearness', cluster M61
`H8417` — 'error', cluster M55
`H8630` — 'to prevail', cluster M23
`H0190` — 'woe!', cluster M03
`H0814` — 'gift', cluster M39
`H2050` — 'to plot', cluster M06,M14
`H2172` — 'melody', cluster M22
`H2270` — 'companion', cluster M44
`H2626` — 'mighty', cluster M23
`H3053` — 'burden', cluster M78
`H3401` — 'opponent', cluster M06
`H3512B` — 'disheartened', cluster M20
`H3574` — 'prosperity', cluster M46
`H4210` — 'melody', cluster M22
`H4721` — 'assembly', cluster M05,M44
`H5010` — 'to disown', cluster M06
`H5222` — 'smitten', cluster M24
`H5765` — 'to act unjustly', cluster M12,M26
`H6115` — 'coercion', cluster M24
`H6125` — 'pressure', cluster M01
`H6199` — 'destitute', cluster M09,M24
`H7438` — 'song', cluster M22,M42
`H7691` — 'error', cluster M55
`H7790` — 'enemy', cluster M06,M44
`H7862` — 'gift', cluster M39
`H7959` — 'prosperity', cluster M46
`H8324` — 'enemy', cluster M06,M44
`H8428` — 'to wound', cluster M03,M10
`H8502` — 'perfection', cluster M61
`H0010` — 'destruction', cluster M55
`H2019` — 'crooked', cluster M14
`H2475` — 'destruction', cluster M55
`H3513I` — 'to honor: many', cluster M71,T3
`H3514` — 'heaviness', cluster FLAG,T2
`H3783` — 'stumbling', cluster M77
`H5099` — 'roaring', cluster M84
`H5390` — 'kiss', cluster M05
`H6104` — 'sluggishness', cluster M24
`H7258` — 'rest', cluster M33
`H0337` — 'woe!', cluster M03
`H0627` — 'collection', cluster M18
`H1947` — 'madness', cluster M66
`H1948` — 'madness', cluster M66
`H3908` — 'charm', cluster M14
`H8623` — 'mighty', cluster M23
`H2559` — 'to turn away', cluster M06,M11
`H7514` — 'to lean', cluster M19
`H0976` — 'testing', cluster M35
`H1421` — 'reviling', cluster M53
`H1998` — 'sound', cluster M62
`H2630` — 'to hoard', cluster M46
`H3271` — 'to cover', cluster M38
`H4654B` — 'ruin', cluster M27,M55
`H4766` — 'abundance', cluster M33,M46
`H4893A` — 'mutilation', cluster M53
`H4923` — 'devastation', cluster M27,M55
`H4926` — 'hearing', cluster M41
`H4937B` — 'support', cluster M70
`H4938A` — 'support', cluster M70
`H5385` — 'burden', cluster M78
`H5448` — 'burden', cluster M78
`H5708` — 'filth', cluster M53
`H5719` — 'voluptuous', cluster M08
`H5790` — 'to help', cluster M38
`H5953C` — 'to mock', cluster M08
`H6129` — 'crooked', cluster M14
`H6899` — 'collection', cluster M18
`H6957A` — 'cord', cluster M03,T2
`H7923` — 'bereavement', cluster M03
`H8399` — 'destruction', cluster M55
`H2613` — 'profaneness', cluster M10c
`H3306` — 'to breathe', cluster M25
`H3357` — 'precious', cluster M29
`H4835` — 'oppression', cluster M06,M24
`H5001` — 'to prophesy', cluster M42,M43
`H5494` — 'degenerate', cluster M57
`H8308` — 'to twist', cluster M57
`H5206` — 'filth', cluster M53
`H7612` — 'devastation', cluster M27,M55
`H2629` — 'to muzzle', cluster M53
`H3314` — 'splendor', cluster M71
`H3520A` — 'glorious', cluster M71
`H4358` — 'perfection', cluster M61
`H4769` — 'resting', cluster M33
`H4892` — 'destruction', cluster M55
`H5078` — 'gift', cluster M39
`H5083` — 'gift', cluster M39
`H5204` — 'wailing', cluster M03
`H5500` — 'to scrape', cluster M23
`H7159` — 'to cover', cluster M38
`H7221` — 'beginning', cluster M17
`H7269` — 'quivering', cluster M01
`H7419` — 'refuse', cluster M27,M30
`H7986` — 'imperious', cluster M08
`H8383` — 'toil', cluster M03,M24,M36
`H6127` — 'to twist', cluster M57
`H0264` — 'brotherhood', cluster M44
`H2256C` — 'union', cluster M44
`H4614` — 'burden', cluster M78

<a id="exception-backfill-code-with-an-activeclustered-sibling"></a>
## Exception -- backfill code with an active/clustered sibling

`H8088A` — 'sound', cluster M62
`H2048A` — 'to mock', cluster M08
`H3856A` — 'to languish', cluster M24
`H1350A` — 'to redeem: redeem', cluster T3
`H8210G` — 'to pour: pour', cluster T2
`H7323G` — 'to run: run', cluster T3
`G5456G` — 'voice/sound: voice', cluster (none)
`H3867A` — 'to join', cluster (none)
`H3898A` — 'to fight', cluster (none)
`H6601A` — 'to open wide', cluster T2
`H7067G` — 'Jealous [God]', cluster FLAG,M18,M28
`H3925G` — 'to learn: teach', cluster (none)
`H4654A` — 'ruin', cluster M27,M55
`H5258A` — 'to pour', cluster T2
`H7032G` — 'voice: sound', cluster M84
`H8186A` — 'horror', cluster M01
`H0935P` — 'to come [in]: bring', cluster T2
`H1004B` — 'house: home', cluster (none)
`H1004Q` — 'house: temple', cluster (none)
`H1121G` — 'son: descendant/people', cluster T2
`H1697N` — 'word: portion', cluster (none)
`H2233H` — 'seed: children', cluster T2
`H3117J` — 'day: daily', cluster T2
`H3956H` — 'tongue: language', cluster T2
`H6440G` — 'face: before', cluster T2
`H7227B` — 'chief', cluster (none)
`H2235A` — 'vegetable', cluster T2
`H2235B` — 'vegetable', cluster T2
`H3117G` — 'day', cluster (none)
`H4325G` — 'water', cluster T2
`H5375G` — 'to lift: raise', cluster (none)
`H5973A` — 'with', cluster (none)
`H7218A` — 'head', cluster T2
`H2006A` — 'if', cluster T2
`H2006B` — 'therefore', cluster T2
`H2492B` — 'to dream', cluster T2
`H4070B` — 'dwelling', cluster T2
`H7761H` — 'to set: put/give', cluster T3
`H8421I` — 'to return: reply', cluster (none)
`H1247I` — 'son: type of', cluster (none)
`H5094A` — 'light', cluster (none)
`H5642A` — 'to hide', cluster M20
`H6903G` — 'before', cluster T2
`H1888B` — 'behold!', cluster T2
`H6966G` — 'to stand: rise', cluster T3
`H1888A` — 'behold', cluster T2
`H2818A` — 'to need', cluster T3
`H4070A` — 'dwelling', cluster T2
`H5415G` — 'to give: give', cluster T3
`H7032H` — 'voice', cluster M84
`H1247J` — 'son: son', cluster (none)
`H6537B` — 'half', cluster (none)
`H6966H` — 'to stand: raise', cluster T2
`H0352A` — 'ram', cluster (none)
`H0505G` — 'thousand', cluster (none)
`H0859A` — 'you [m.s.]', cluster (none)
`H0996G` — 'between', cluster (none)
`H1121A` — 'son: child', cluster (none)
`H1167J` — 'master: owning', cluster T2
`H2416C` — 'living thing', cluster M25
`H3499A` — 'remainder', cluster (none)
`H3588A` — 'for', cluster T6
`H5375M` — 'to lift: look', cluster (none)
`H5640A` — 'to close', cluster T2
`H5869A` — 'eye', cluster T2
`H5927G` — 'to ascend: rise', cluster (none)
`H6440H` — 'face', cluster T2
`H6440J` — 'face: surface', cluster T2
`H6743B` — 'to prosper', cluster M46
`H8478H` — 'underneath: instead', cluster (none)
`H0376I` — 'man: anyone', cluster (none)
`H0410G` — 'God', cluster T7
`H1980I` — 'to go: walk', cluster T3
`H2022G` — 'mountain: mount', cluster T2
`H3117L` — 'day: today', cluster (none)
`H3318H` — 'to come out: send', cluster T3
`H3318O` — 'to come out: speak', cluster T3
`H3615G` — 'to end: finish', cluster T3
`H3772I` — 'to cut: eliminate', cluster T3
`H4639K` — 'deed', cluster (none)
`H4714G` — 'Egypt', cluster (none)
`H5307N` — 'to fall: presenting', cluster (none)
`H5892B` — 'city', cluster (none)
`H7620I` — 'week', cluster T2
`H7673A` — 'to cease', cluster T2
`H7725H` — 'to return: rescue', cluster (none)
`H8478G` — 'underneath: under', cluster (none)
`H0518B` — 'if: except', cluster T2
`H1540H` — 'to reveal: reveal', cluster T3
`H3254G` — 'to add: again', cluster T3
`H3588B` — 'that if: except', cluster T2
`H3709G` — 'palm', cluster T2
`H5178A` — 'bronze', cluster T2
`H6310G` — 'lip', cluster T2
`H6605A` — 'to open', cluster T2
`H6635H` — 'army: war', cluster T2
`H6963H` — 'voice: sound', cluster T2
`H7136A` — 'to meet', cluster (none)
`H0127G` — 'land: soil', cluster (none)
`H0168G` — 'tent', cluster (none)
`H0410K` — 'god', cluster T7
`H0430J` — 'gods', cluster (none)
`H1121I` — 'son: type of', cluster (none)
`H2388J` — 'to strengthen: prevail over', cluster M23
`H2505A` — 'to divide', cluster T3
`H3835A` — 'to whiten', cluster T3
`H4924B` — 'fatness', cluster M46
`H5257A` — 'libation', cluster (none)
`H5307J` — 'to fall: kill', cluster (none)
`H5414O` — 'to give: give [marriage]', cluster T3
`H6213J` — 'to make: [do]', cluster T3
`H7725L` — 'to return: refuse', cluster (none)
`H7760H` — 'to set: put', cluster T3
`H7971K` — 'to send: reach', cluster T3
`H8210I` — 'to pour: build siege mound', cluster (none)
`H1980M` — 'to go: journey', cluster T3
`H2094A` — 'to shine', cluster T2
`H2416A` — 'alive', cluster M25
`H2416E` — 'life', cluster M25
`H5975H` — 'to stand: appoint', cluster (none)
`H7751A` — 'to rove', cluster T3
`H8193J` — 'lip: shore', cluster (none)
`H1980K` — 'to go: come!', cluster T3
`H1980L` — 'to go: continue', cluster T3
`H5307I` — 'to fall: allot', cluster (none)
`H5414N` — 'to give: pay', cluster T3
`H7901G` — 'to lie down: lay down', cluster T2
`H0990G` — 'belly: abdomen', cluster T2
`H1644G` — 'to drive out: drive out', cluster T3
`H5869H` — 'eye: seeing', cluster (none)
`H5927H` — 'to ascend: establish', cluster T3
`H7723H` — 'vanity: vain', cluster (none)
`H1870G` — 'way: conduct', cluster (none)
`H3678G` — 'throne', cluster T2
`H0518A` — 'if', cluster T2
`H1167H` — 'master: husband', cluster T2
`H4057B` — 'wilderness', cluster (none)
`H5271A` — 'youth', cluster T2
`H6086H` — 'tree', cluster T2
`H8047G` — 'horror: destroyed', cluster M01
`H0197J` — 'Portico', cluster (none)
`H0899B` — 'garment', cluster (none)
`H1588M` — 'garden', cluster T2
`H1870L` — 'way: journey', cluster (none)
`H2346G` — 'wall', cluster T2
`H3243J` — 'suckling-baby', cluster (none)
`H5414M` — 'to give: cry out', cluster T3
`H6186A` — 'to arrange', cluster T3
`H7130G` — 'entrails: among', cluster T2
`H7218I` — 'head: top', cluster (none)
`H7699A` — 'breast', cluster T2
`H7704M` — 'field', cluster (none)
`H0859D` — 'you [m.p.]', cluster T2
`H5066G` — 'to approach: approach', cluster T3
`H5158I` — '[Shittim] Valley', cluster (none)
`H8210H` — 'to pour: kill', cluster T2
`H8248G` — 'to water: watering', cluster T2
`H1004M` — 'house: household', cluster T2
`H5553H` — 'crag', cluster (none)
`H6735A` — 'envoy', cluster T2
`H6965J` — 'to arise: attack', cluster T3
`H1540I` — 'to reveal: uncover', cluster T2
`H1540K` — 'to reveal: remove', cluster (none)
`H8577A` — 'jackal', cluster (none)
`H0518I` — 'if: surely yes', cluster (none)
`H1644H` — 'to drive out: divorce', cluster T2
`H2256D` — 'destruction', cluster M55
`H2256M` — 'cord', cluster M03,T2
`H3162A` — 'unitedness', cluster T2
`H5375N` — 'to lift: loud', cluster (none)
`H0935K` — 'to come [in]: [sun]set', cluster T3
`H3384B` — 'to show', cluster M05
`H5391A` — 'to bite', cluster T3
`H5844A` — 'to enwrap', cluster T3
`H7218H` — 'head: leader', cluster T2
`H1980H` — 'to go: come', cluster T3
`H2388H` — 'to strengthen: hold', cluster M23
`H5375R` — 'to lift: fight', cluster (none)
`H6635B` — '[Lord of] Hosts', cluster M72
`H4639G` — 'deed: work', cluster (none)
`H6965H` — 'to arise: raise', cluster T3
`H7626G` — 'tribe: staff', cluster (none)
`H0990J` — 'belly: body', cluster T2
`H1121L` — 'son: aged', cluster (none)
`H5158A` — 'torrent: river', cluster (none)
`H7114B` — 'to reap', cluster T3
`H7851G` — 'Shittim', cluster (none)
`H2119A` — 'to crawl', cluster T3
`H6679A` — 'to hunt', cluster T3
`H8104H` — 'to keep: guard', cluster M74
`H3157H` — 'Jezreel', cluster (none)
`H3157K` — 'Jezreel', cluster (none)
`H3162B` — 'together', cluster T2
`H3947I` — 'to take: marry', cluster (none)
`H6485H` — 'to reckon: punish', cluster T3
`H7760L` — 'to set: appoint', cluster (none)
`H0376H` — 'man: husband', cluster (none)
`H1168A` — 'Baal', cluster (none)
`H1980J` — 'to go: take', cluster T3
`H1980N` — 'to go: follow', cluster T3
`H5710B` — 'to adorn', cluster T3
`H6601B` — 'to entice', cluster M10,M77
`H7896G` — 'to set: make', cluster T3
`H5493H` — 'to turn aside: depart', cluster M11,M30
`H6086G` — 'tree: wood', cluster T2
`H2502A` — 'to rescue', cluster M38
`H5414K` — 'to give: allow', cluster T3
`H7626H` — 'tribe', cluster (none)
`H7819B` — 'slaughtering', cluster (none)
`H1870K` — 'way: road', cluster (none)
`H3384A` — 'to shoot', cluster T2
`H7896I` — 'to set: appoint', cluster (none)
`H8186B` — 'horror', cluster M01
`H1197A` — 'to burn: burn', cluster T3
`H2556A` — 'to leaven', cluster T3
`H8088B` — 'report', cluster M82
`H2803H` — 'to devise: count', cluster M64
`H0990H` — 'belly: womb', cluster T2
`H5116A` — 'pasture', cluster (none)
`H0206H` — 'Aven', cluster (none)
`H3947J` — 'to take: bring', cluster T2
`H6524A` — 'to sprout', cluster T3
`H4397H` — 'messenger: angel', cluster T9
`H8104J` — 'to keep: careful', cluster M74
`H2717A` — 'to dry', cluster T3
`H5375L` — 'to lift: exalt', cluster (none)
`H7704I` — 'land: wildlife', cluster (none)
`H3947H` — 'to take: recieve', cluster T3
`H7488B` — 'luxuriant', cluster (none)
`H0127I` — 'land: planet', cluster (none)
`H0518J` — 'if: until', cluster (none)
`H2254A` — 'to pledge', cluster T3
`H8248H` — 'to water: drink', cluster T2
`G0032G` — 'angel', cluster T9
`G0032H` — 'angel: messenger', cluster T9
`G0129H` — '(Field of) Blood', cluster (none)
`G0165G` — 'an age: age', cluster (none)
`G0435H` — 'man: husband', cluster (none)
`G0568H` — 'to have in full', cluster T3
`G0630H` — 'to release: divorce', cluster (none)
`G0928G` — 'to torture: torture', cluster M03
`G0938H` — 'Queen', cluster (none)
`G1081G` — 'offspring', cluster T2
`G1081H` — 'offspring: fruit', cluster T2
`G1093G` — 'earth: planet', cluster (none)
`G1093I` — 'earth: soil', cluster (none)
`G1487H` — 'if: not', cluster (none)
`G1487I` — 'if: is[question]', cluster (none)
`G1487L` — 'if: else', cluster (none)
`G1492H` — 'to perceive: see', cluster (none)
`G2012` — 'manager', cluster T2
`G2083` — 'friend', cluster M05
`G2149` — 'broad', cluster (none)
`G2787H` — 'ark: Noah', cluster T2
`G2962G` — 'lord: God', cluster (none)
`G3614G` — 'home', cluster T2
`G3614H` — 'home: household', cluster T2
`G3624G` — 'house: home', cluster (none)
`G3708G` — 'to see: to see', cluster T3
`G3985G` — 'to test/tempt: tempt', cluster M35
`G3985H` — 'to test/tempt: test', cluster M35
`G4160I` — 'to do/make: appoint', cluster (none)
`G4690H` — 'seed(s)', cluster (none)
`G5083G` — 'to keep: observe', cluster (none)
`G5259H` — 'by/under: under', cluster (none)
`G1085G` — 'family: descendant', cluster (none)
`G1487M` — 'if: even though', cluster (none)
`G3708H` — 'to see: to appear', cluster T3
`G1487J` — 'if: if only', cluster (none)
`G5442H` — 'to keep/guard: guard', cluster (none)
`G5442I` — 'to keep/guard: protect', cluster (none)
`G5083I` — 'to keep: protect', cluster (none)
`G0568I` — 'to abstain', cluster T3
`G1487K` — 'if: surely', cluster (none)
`G2839H` — 'common: shared', cluster T2
`G3985I` — 'to test/tempt: try', cluster M35
`G4160J` — 'to do/make: spend[time]', cluster T3
`G5564H` — 'Field (of Blood)', cluster (none)
`G4160H` — 'to do/make: make', cluster T3
`H0120H` — 'the man [Adam]', cluster (none)
`H0227B` — 'the past', cluster (none)
`H0241I` — 'ear: to ears', cluster T2
`H0328B` — 'softly', cluster T2
`H0410I` — 'El [Elohe]', cluster (none)
`H0410J` — 'El [Most High]', cluster (none)
`H0430H` — '[LORD]-Elohe', cluster (none)
`H0436H` — 'terebinth', cluster T2
`H0518H` — 'if: surely no', cluster (none)
`H0520A` — 'cubit', cluster (none)
`H0859C` — 'you [f.s.]', cluster T2
`H0859E` — 'you [f.p.]', cluster T2
`H0935I` — 'to come [in]: towards', cluster T3
`H0935J` — 'to come [in]: advanced', cluster T3
`H0935M` — 'to come [in]: fulfill', cluster (none)
`H1004O` — 'house: inside', cluster T2
`H1004P` — 'house: palace', cluster (none)
`H1121H` — 'son: young animal', cluster T2
`H1121J` — 'son', cluster (none)
`H1166I` — 'rule: to marry', cluster T2
`H1167I` — 'master: men', cluster T2
`H1167K` — 'master: [master of]', cluster T2
`H1254A` — 'to create', cluster T3
`H1419K` — 'great: old', cluster T2
`H1481A` — 'to sojourn', cluster T3
`H1697O` — 'Chronicles', cluster (none)
`H1803B` — 'poor', cluster (none)
`H1817C` — 'door', cluster T2
`H2022H` — 'mountain: hill country', cluster T2
`H2048B` — 'to deceive', cluster M14
`H2233G` — 'seed', cluster T2
`H2290B` — 'belt', cluster T2
`H2513A` — 'portion', cluster T2
`H2513B` — 'smoothness', cluster T2
`H2590B` — 'embalming', cluster (none)
`H2975G` — 'Nile', cluster (none)
`H3117I` — 'day: year', cluster (none)
`H3243H` — 'to suckle', cluster T3
`H3243I` — 'suckling-nurse', cluster (none)
`H3318K` — 'to come out: [sun]rise', cluster (none)
`H3318L` — 'to come out: issue', cluster T3
`H3335G` — 'to form: formed', cluster T3
`H3513J` — 'to honor: dull', cluster M16,M22,T3
`H3559A` — 'to establish: prepare', cluster (none)
`H3588C` — 'for as that: since', cluster (none)
`H3651A` — 'right', cluster (none)
`H3651B` — 'as', cluster (none)
`H3709H` — 'palm: sole', cluster T2
`H3709I` — 'palm: dish', cluster T2
`H3722B` — 'to cover', cluster M38
`H3724B` — 'pitch', cluster (none)
`H3835B` — 'to make bricks', cluster T3
`H4026M` — 'tower', cluster T2
`H4229A` — 'to wipe', cluster T3
`H4397G` — 'messenger', cluster T9
`H4924A` — 'fat', cluster T2
`H5066H` — 'to approach: bring', cluster T2
`H5090A` — 'to lead', cluster (none)
`H5158N` — 'torrent: valley', cluster (none)
`H5234B` — 'to alienate', cluster T3
`H5439I` — 'around: whole', cluster T2
`H5869J` — 'eye: before[the eyes]', cluster T2
`H5869M` — 'spring', cluster (none)
`H5921B` — 'as', cluster (none)
`H5927I` — 'to ascend: offer up', cluster T3
`H5927K` — 'to ascend: copulate', cluster T3
`H5945H` — '[LORD] Most High', cluster (none)
`H6049A` — 'to cloud', cluster T3
`H6106H` — 'bone: same', cluster T2
`H6131B` — 'to hamstring', cluster T3
`H6310K` — 'lip: according', cluster (none)
`H6327A` — 'to scatter', cluster T3
`H6440K` — 'face: east', cluster T2
`H6872A` — 'bundle', cluster T2
`H6946G` — 'Kadesh', cluster (none)
`H6963J` — 'voice: message', cluster T2
`H7122G` — 'to encounter: meet', cluster M37
`H7122I` — 'to encounter: chanced', cluster M37
`H7200J` — 'to see: select', cluster T3
`H7200N` — 'Provider [God]', cluster (none)
`H7218J` — 'head: first', cluster (none)
`H7235B` — 'to shoot', cluster T2
`H7298A` — 'trough', cluster (none)
`H7363B` — 'to hover', cluster T3
`H7411B` — 'to deceive', cluster M14
`H7620H` — 'week', cluster T2
`H7641B` — 'ear', cluster T2
`H7704A` — 'Sirion', cluster (none)
`H7892A` — 'song', cluster M22,M42
`H7896H` — 'to set: put', cluster T3
`H7901H` — 'to lie down: sleep', cluster T2
`H7901I` — 'to lie down: have sex', cluster T2
`H7936B` — 'to hire', cluster T3
`H7971H` — 'to send: let go', cluster T3
`H7971I` — 'to send: divorce', cluster T2
`H8138B` — 'to repeat', cluster T3
`H8163A` — 'hairy', cluster (none)
`H8193H` — 'lip: words', cluster (none)
`H8193K` — 'lip: language', cluster T2
`H8478I` — 'underneath: stand', cluster T2
`H8478L` — 'underneath: swear', cluster T2
`H0352C` — 'leader', cluster T2
`H1004N` — 'house: container', cluster T2
`H1167G` — 'master', cluster T2
`H1697L` — 'word: case', cluster (none)
`H1826A` — 'to silence: stationary', cluster M33
`H1980O` — 'to go: send', cluster T3
`H2094B` — 'to warn', cluster T3
`H2100G` — 'to flow: flowing', cluster T3
`H2436H` — 'bosom: garment', cluster (none)
`H2560B` — 'to daub', cluster T3
`H2803G` — 'to devise: design', cluster M64
`H2859A` — 'relative', cluster (none)
`H3332H` — 'to pour: cast metal', cluster T3
`H3713B` — 'frost', cluster (none)
`H3772G` — 'to cut: cut', cluster T3
`H3947L` — 'to take: fire', cluster T3
`H4024B` — 'Migdol', cluster (none)
`H4245B` — 'sickness', cluster T2
`H4414B` — 'to salt', cluster T3
`H4478A` — 'manna', cluster T2
`H4478B` — 'What?', cluster T2
`H4609B` — 'step', cluster (none)
`H4809G` — 'Meribah', cluster M02,T2
`H4938B` — 'staff', cluster (none)
`H5130B` — 'to wave', cluster (none)
`H5137A` — 'to sprinkle', cluster T3
`H5251G` — 'Banner [God]', cluster (none)
`H5307H` — 'to fall: deserting', cluster (none)
`H5327A` — 'to struggle', cluster M34
`H5375S` — 'to lift: enthuse', cluster (none)
`H5375V` — 'to lift: count', cluster (none)
`H5414Q` — 'to give: if only!', cluster T3
`H5439H` — 'around: side', cluster T2
`H5526B` — 'to cover', cluster M38
`H5526E` — 'to cover', cluster M38
`H5800C` — 'to leave: release', cluster (none)
`H5953A` — 'to abuse', cluster T3
`H6030C` — 'to sing', cluster (none)
`H6086I` — 'tree: stick', cluster T2
`H6154M` — 'racial-mix', cluster (none)
`H6306B` — 'redemption', cluster T2
`H6310H` — 'lip: edge', cluster (none)
`H6310J` — 'lip: opening', cluster (none)
`H6363A` — 'firstborn', cluster M37
`H6485A` — 'to reckon: list', cluster T3
`H6485B` — 'reckoning', cluster (none)
`H6605B` — 'to engrave', cluster T3
`H6696C` — 'to form', cluster M61
`H6963I` — 'voice: thunder', cluster T2
`H6963K` — 'voice: [sound of]', cluster T2
`H6999A` — 'offer: to burn', cluster (none)
`H7067H` — 'jealous', cluster M02,M18
`H7218L` — 'head: count', cluster (none)
`H7411A` — 'to shoot', cluster T3
`H7461A` — 'trembling', cluster M01
`H7620G` — 'Weeks', cluster (none)
`H7725M` — 'to return: reply', cluster (none)
`H7760I` — 'to set: take', cluster T3
`H7892B` — 'song', cluster M22,M42
`H8193I` — 'lip: edge', cluster (none)
`H8478J` — 'underneath: because of', cluster T2
`H8478K` — 'underneath: owning', cluster (none)
`H8549G` — 'unblemished', cluster M61
`H8577M` — 'serpent: snake', cluster (none)
`H2100H` — 'to flow: discharge', cluster T3
`H2233I` — 'seed: semen', cluster T2
`H2778C` — 'to acquire', cluster T3
`H2902A` — 'to overspread', cluster T3
`H3971B` — 'blemish', cluster T2
`H4057G` — 'Wilderness [of Sinai]', cluster (none)
`H5414L` — 'to give: throw', cluster (none)
`H5927M` — 'to ascend: regurgitate', cluster T3
`H5953B` — 'to glean', cluster T3
`H5975J` — 'to stand: put', cluster T2
`H6186B` — 'to value', cluster M26
`H7106A` — 'to scrape', cluster M23
`H7133A` — 'offering', cluster T2
`H7673B` — 'to keep', cluster M74
`H8163C` — 'satyr', cluster (none)
`H8549I` — 'unblemished: complete', cluster M61
`H0935H` — 'Lebo-[Hamath]', cluster (none)
`H1350H` — 'to redeem: avenge', cluster (none)
`H1350I` — 'to redeem: relative', cluster (none)
`H1419J` — 'Great [Sea]', cluster T2
`H1633B` — 'to break bones', cluster (none)
`H1870I` — "[King's] Highway", cluster (none)
`H2023G` — '[Mount] Hor', cluster T2
`H2023H` — '[Mount] Hor', cluster T2
`H2574G` — 'Hamath', cluster (none)
`H3318I` — 'to come out: extends', cluster T3
`H3318J` — 'to come out: casting [lot]', cluster T2
`H3318N` — 'to come out: regular', cluster T3
`H3559I` — 'to establish: make', cluster T3
`H4229B` — 'to strike', cluster (none)
`H4714J` — '[Brook of] Egypt', cluster T2
`H5081H` — 'noble', cluster M34
`H5158H` — '[Eshcol] Valley', cluster (none)
`H5158L` — 'Brook', cluster (none)
`H5606A` — 'to slap', cluster T3
`H5945B` — 'Most High [God]', cluster (none)
`H6075B` — 'to presume', cluster T3
`H6160I` — 'Plains [of Moab]', cluster (none)
`H6306A` — 'redemption', cluster T2
`H6363B` — 'firstborn', cluster M37
`H6635I` — 'army: duty', cluster T2
`H6692A` — 'to blossom', cluster T3
`H6979C` — 'to destroy', cluster M10
`H7896J` — 'to set: accuse', cluster T3
`H0935N` — 'to come [in]: besiege', cluster T3
`H1100G` — 'Belial', cluster (none)
`H1197I` — 'to burn: purge', cluster T3
`H1697J` — 'word: promised', cluster (none)
`H2388I` — 'to strengthen: ensure', cluster M23
`H2490I` — 'to profane/begin: fruit', cluster T3
`H3243G` — 'to suck', cluster T3
`H3739A` — 'to trade', cluster T3
`H5254H` — 'to test: try', cluster (none)
`H5375T` — 'to lift: journey', cluster (none)
`H5391B` — 'to pay interest', cluster T3
`H6014B` — 'to tyranise', cluster T3
`H6086J` — 'tree: stake', cluster T2
`H6160G` — 'Arabah', cluster (none)
`H6286B` — 'to re-harvest', cluster T3
`H6643B` — 'gazelle', cluster (none)
`H7760J` — 'to set: accuse', cluster T3
`H7760K` — 'to set: consider', cluster M15
`H0935L` — 'to come [in]: marry', cluster (none)
`H1004L` — 'Beth-[baal-meon]', cluster (none)
`H2011G` — '[Topheth of] Hinnom', cluster T2
`H2011H` — '[Topheth of son of] Hinnom', cluster T2
`H2256A` — 'Mahalab', cluster (none)
`H2791A` — 'silently', cluster T2
`H3332I` — 'to pour: set down', cluster T3
`H3956I` — 'tongue: bar', cluster (none)
`H5307L` — 'to fall: fail', cluster (none)
`H5927J` — 'to ascend: attack', cluster T3
`H5945G` — 'Upper [Beth Horon]', cluster (none)
`H6160J` — '[Beth]-arabah', cluster (none)
`H6160K` — '[Sea of] the Arabah', cluster (none)
`H6190G` — '[Gilgal]-haaraloth', cluster (none)
`H6679B` — 'to provision', cluster T2
`H6718B` — 'food', cluster (none)
`H7227G` — '[Sidon] the Great', cluster (none)
`H8388A` — 'to border', cluster T3
`H0047H` — 'mighty: stallion', cluster (none)
`H0410H` — 'El [Berith]', cluster (none)
`H0436G` — "[Diviners'] Oak", cluster T2
`H1101B` — 'to feed', cluster T3
`H1121K` — 'son: warrior', cluster (none)
`H2686B` — 'to shoot', cluster T2
`H2717B` — 'to destroy', cluster M10
`H4496G` — 'Nohah', cluster (none)
`H4629G` — 'Maareh', cluster (none)
`H4718A` — 'hammer', cluster (none)
`H5158J` — '[Sorek] Valley', cluster (none)
`H5274A` — 'to lock', cluster T2
`H5375U` — 'to lift: marry', cluster (none)
`H5375W` — 'to lift: bearing [armour]', cluster (none)
`H5608B` — 'secretary', cluster (none)
`H6049G` — "Diviners' [Oak]", cluster (none)
`H6544A` — 'to lead', cluster (none)
`H6743A` — 'to rush', cluster T2
`H6965K` — 'to arise: guard', cluster (none)
`H7049A` — 'to sling', cluster T3
`H7462D` — 'to befriend', cluster T3
`H7641H` — 'Shibboleth', cluster (none)
`H7971J` — 'to send: marriage', cluster T3
`H7971L` — 'to send: burn', cluster T3
`H8385B` — 'opportunity', cluster (none)
`H0430I` — '[Gibeath]-elohim', cluster (none)
`H1254B` — 'to fatten', cluster T3
`H1697K` — 'word: deed', cluster (none)
`H1826I` — 'to silence: destroyed', cluster (none)
`H2290A` — 'belt', cluster T2
`H2416B` — 'kinsfolk', cluster M25,T8
`H2793G` — 'Horesh', cluster (none)
`H3157G` — 'Jezreel', cluster (none)
`H3277G` — "Wildgoats'", cluster (none)
`H3293B` — 'honeycomb', cluster (none)
`H3543B` — 'to rebuke', cluster T3
`H3559J` — 'to establish: commit', cluster T3
`H3724D` — 'village', cluster (none)
`H4224B` — 'refuge', cluster M19
`H4686B` — 'fortress', cluster (none)
`H5310B` — 'to disperse', cluster T3
`H5737C` — 'to lack', cluster T3
`H5860B` — 'to pounce', cluster T3
`H6030A` — 'to dwell', cluster T2
`H6310L` — 'lip: one third', cluster (none)
`H6697G` — 'Rocks [of Goats]', cluster T2
`H6872C` — 'Zeror', cluster (none)
`H7323H` — 'to run: guard', cluster (none)
`H7704B` — 'land: soil', cluster (none)
`H8138A` — 'to change', cluster M45
`H8549J` — 'unblemished: Thummim', cluster M61
`H0953B` — 'Cistern', cluster (none)
`H1197H` — 'to burn: destroy', cluster (none)
`H2416D` — 'community', cluster M44,T8
`H3157I` — 'Jezreel', cluster (none)
`H3293H` — '[Ephraim] Forest', cluster (none)
`H3823B` — 'to bake', cluster T2
`H4937A` — 'support', cluster M70
`H5273B` — 'musical', cluster M22
`H5425B` — 'to free', cluster (none)
`H5437K` — 'to turn: changed', cluster (none)
`H5798A` — 'Uzzah', cluster (none)
`H6086K` — 'tree: carpenter', cluster T2
`H6452B` — 'to limp', cluster T3
`H6872B` — 'pebble', cluster T2
`H7462A` — 'House of Shepherds', cluster T2
`H7626I` — 'tribe: javelin', cluster (none)
`H7760B` — 'fate', cluster (none)
`H0197G` — 'Hall [of pillars]', cluster (none)
`H0197I` — 'Hall [of the Throne]', cluster T2
`H0352B` — 'pillar', cluster T2
`H0425H` — 'Elah', cluster (none)
`H0935O` — 'Lebo', cluster (none)
`H0990I` — 'belly: hump', cluster T2
`H1004K` — 'House [of the Forests of Lebanon]', cluster T2
`H2436I` — 'bosom: lap', cluster (none)
`H2490B` — 'to play flute', cluster T3
`H3293I` — '[House of] the Forest', cluster (none)
`H3678H` — '[Hall of] the Throne', cluster T2
`H4436G` — 'Queen [of Sheba]', cluster T2
`H5606B` — 'to suffice', cluster T3
`H5982H` — '[Hall of] Pillars', cluster (none)
`H6957B` — 'line', cluster (none)
`H7049B` — 'to carve', cluster T3
`H8106A` — 'Shemer', cluster (none)
`H8585A` — 'conduit', cluster (none)
`H0425I` — 'Elah', cluster (none)
`H1004H` — 'Beth [Haggan]', cluster (none)
`H1588G` — 'Garden [of Uzza]', cluster T2
`H1588H` — '[Beth]-haggan', cluster T2
`H2657G` — 'Hephzibah', cluster T2
`H2717C` — 'to slay', cluster T3
`H3526G` — "Washer's", cluster (none)
`H3739B` — 'to feed', cluster T2
`H4853B` — 'oracle', cluster (none)
`H5307M` — 'to fall: fell [trees]', cluster (none)
`H5327B` — 'to desolate', cluster T3
`H6485L` — 'to reckon: put', cluster T2
`H6979A` — 'to dig', cluster T3
`H7200M` — 'to see: approach', cluster T3
`H7323I` — 'to run: pieces', cluster T3
`H7704H` — 'Field [of the Launderer]', cluster (none)
`H7921C` — 'barrenness', cluster (none)
`H8227B` — 'Shaphan', cluster (none)
`H1004G` — 'Beth-[ashbea]', cluster (none)
`H1168H` — 'Baal', cluster (none)
`H3157J` — 'Jezreel', cluster (none)
`H3335H` — 'to form: potter', cluster T3
`H4060G` — 'huge', cluster (none)
`H5437I` — 'to turn: again', cluster (none)
`H1696H` — 'to speak: subdue', cluster T3
`H3247G` — '[Gate of the] Foundation', cluster (none)
`H3947K` — 'to take: buy', cluster T3
`H4245A` — 'sickness', cluster T2
`H5274B` — 'to shoe', cluster T3
`H5401B` — 'to handle', cluster T3
`H6437H` — 'Corner [Gate]', cluster (none)
`H6999C` — 'incense-altar', cluster (none)
`H7183B` — 'attentive', cluster M41
`H2818B` — 'necessity', cluster T2
`H5415I` — 'to give: pay', cluster T3
`H5642B` — 'to destroy', cluster M10
`H7761I` — 'to set: appoint', cluster (none)
`H7936A` — 'to hire', cluster T3
`H0830G` — 'Dung [Gate]', cluster (none)
`H1004A` — 'place', cluster T2
`H1419B` — 'Haggedolim', cluster (none)
`H2346H` — '[Broad] Wall', cluster T2
`H4026G` — '[Hananel] Tower', cluster T2
`H4026H` — 'Tower [of the Hundred]', cluster T2
`H4026I` — 'Tower [Of the Ovens]', cluster T2
`H4060B` — 'tribute', cluster T2
`H4325H` — 'Water [Gate]', cluster T2
`H4662G` — 'Muster [Gate]', cluster (none)
`H4924C` — 'fat piece', cluster T2
`H5800B` — 'to restore', cluster T3
`H5869B` — 'Fountain [Gate]', cluster (none)
`H5869G` — 'Fountain of [Drangons]', cluster (none)
`H7133B` — 'offering', cluster T2
`H7183A` — 'attentive', cluster M41
`H7663A` — 'to inspect', cluster T3
`H8577B` — 'Dragon', cluster (none)
`H1540J` — 'to reveal: proclaim', cluster (none)
`H4436H` — 'queen', cluster T2
`H1250B` — 'field', cluster (none)
`H1460B` — 'midst', cluster (none)
`H2490A` — 'to bore', cluster T3
`H2491H` — 'slain: wounded', cluster T2
`H2686A` — 'to divide', cluster T2
`H3117H` — 'day: old', cluster (none)
`H3559B` — 'blow', cluster (none)
`H3685G` — 'Orion', cluster (none)
`H3886B` — 'to talk wildly', cluster (none)
`H4148H` — 'discipline: instruction', cluster (none)
`H4148I` — 'discipline: bonds', cluster (none)
`H4685B` — 'net', cluster T2
`H5362A` — 'to strike', cluster (none)
`H5526A` — 'to fence', cluster T3
`H5526F` — 'to weave', cluster T2
`H5587B` — 'disquietings', cluster FLAG,T2
`H5607B` — 'sufficiency', cluster (none)
`H5710A` — 'to advance', cluster T2
`H5774B` — 'gloom', cluster (none)
`H5848A` — 'to turn aside', cluster (none)
`H6327D` — 'to shatter', cluster T3
`H7200K` — 'to see: enjoy', cluster T3
`H7280A` — 'to disturb', cluster T3
`H7685A` — 'to grow', cluster (none)
`H7699B` — 'breast', cluster T2
`H0047G` — 'mighty: ox', cluster (none)
`H0047J` — 'mighty: angel', cluster (none)
`H1760A` — 'to thrust', cluster T3
`H1817A` — 'door', cluster T2
`H2560A` — 'to aggitate', cluster T3
`H3293G` — 'Jaar', cluster (none)
`H3512B` — 'disheartened', cluster M20
`H4364B` — 'net', cluster T2
`H4455B` — 'jaw', cluster (none)
`H4480B` — 'portion', cluster (none)
`H4659B` — 'deed', cluster (none)
`H4911A` — 'to liken', cluster T3
`H5102B` — 'to shine', cluster T2
`H5258B` — 'to install', cluster T3
`H5387B` — 'mist', cluster (none)
`H5526C` — 'to weave', cluster T2
`H5848B` — 'to envelope', cluster T3
`H5849B` — 'to crown', cluster T2
`H6670B` — 'to shine', cluster T2
`H7462C` — 'to accompany', cluster T3
`H7641A` — 'stream', cluster T2
`H7722A` — 'ravage', cluster (none)
`H7997B` — 'to loot', cluster T3
`H8210J` — 'to pour: scatter', cluster T2
`H2436J` — 'bosom: secret', cluster (none)
`H2506B` — 'smoothness', cluster T2
`H3513I` — 'to honor: many', cluster M71,T3
`H3856B` — 'to amaze', cluster T3
`H5433A` — 'to imbibe', cluster T3
`H6106I` — 'bone: body', cluster T2
`H6612B` — 'simplicity', cluster (none)
`H6735B` — 'hinge', cluster T2
`H6793B` — 'coolness', cluster (none)
`H7389A` — 'poverty', cluster T2
`H7389B` — 'poverty', cluster T2
`H2363B` — 'to enjoy', cluster T3
`H4685A` — 'siegework', cluster (none)
`H4685C` — 'net', cluster T2
`H5533A` — 'to endanger', cluster T3
`H6001B` — 'laborious', cluster T2
`H6131A` — 'to uproot', cluster T3
`H1713A` — 'to look', cluster (none)
`H3724C` — 'henna', cluster (none)
`H5132B` — 'to bud', cluster T3
`H5437J` — 'to turn: repell', cluster (none)
`H6677B` — 'necklace', cluster (none)
`H7447A` — 'drop', cluster (none)
`H0352D` — 'terebinth', cluster T2
`H1004J` — 'House [of the Forest]', cluster T2
`H1166G` — 'Married', cluster (none)
`H1238B` — 'to empty', cluster T3
`H1350B` — 'redemption', cluster T2
`H1754B` — 'ball', cluster (none)
`H1817B` — 'door', cluster T2
`H1826B` — 'to wail', cluster T3
`H1870H` — 'Way', cluster (none)
`H2151A` — 'to shake', cluster T3
`H2778B` — 'to winter', cluster T3
`H2791B` — 'craftily', cluster T2
`H3068I` — '[Jerusalem of] the Lord', cluster (none)
`H4224A` — 'hiding-place', cluster T2
`H4364A` — 'net', cluster T2
`H4365B` — 'net', cluster T2
`H4414A` — 'to dissipate', cluster T3
`H4654B` — 'ruin', cluster M27,M55
`H4685D` — 'stronghold', cluster (none)
`H4714I` — '[Sea of] Egypt', cluster T2
`H4893A` — 'mutilation', cluster M53
`H4937B` — 'support', cluster M70
`H5158G` — 'Brook', cluster (none)
`H5183B` — 'descent', cluster (none)
`H5218A` — 'stricken', cluster T2
`H5533B` — 'to impoverish', cluster T3
`H5737B` — 'to hoe', cluster T3
`H5800G` — 'Forsaken', cluster (none)
`H5892G` — 'City [of On]', cluster T2
`H5892I` — 'city [of God]', cluster (none)
`H5953C` — 'to mock', cluster M08
`H6090B` — 'idol', cluster T2
`H6105B` — 'to shut eyes', cluster T3
`H6121B` — 'steep', cluster (none)
`H7641G` — 'Euphrates', cluster (none)
`H7971M` — 'to send: exile', cluster T3
`H8077G` — 'Desolate', cluster (none)
`H8178B` — 'storm', cluster (none)
`H8388B` — 'to delimit', cluster T3
`H1760B` — 'to thrust', cluster T3
`H2319G` — 'New [Gate]', cluster (none)
`H3820B` — 'Leb', cluster (none)
`H5271B` — 'youth', cluster T2
`H6089B` — 'vessel', cluster T2
`H6154A` — 'Arabia', cluster (none)
`H6245A` — 'to gleam', cluster T3
`H6335A` — 'to leap', cluster T3
`H6963B` — 'frivolity', cluster T2
`H6965A` — '[Leb]-kamai', cluster (none)
`H6979B` — 'to cool', cluster T3
`H0565B` — 'threat', cluster (none)
`H2100I` — 'to flow: waste away', cluster (none)
`H5439J` — 'around: neighours', cluster T2
`H5640B` — 'to stopper', cluster T3
`H1004I` — 'Beth-[togarmah]', cluster (none)
`H2258A` — 'pledge', cluster T2
`H2258B` — 'pledge', cluster T2
`H2428B` — 'Helech', cluster (none)
`H3068H` — 'The Lord', cluster (none)
`H3520A` — 'glorious', cluster M71
`H4894A` — 'spreading-place', cluster T2
`H4894B` — 'spreading-place', cluster T2
`H5158M` — 'Brook', cluster (none)
`H5414J` — 'to give: turn', cluster (none)
`H5674G` — '[Valley of] the Travelers', cluster (none)
`H6213B` — 'to press', cluster T3
`H6524C` — 'to fly', cluster T3
`H7106B` — 'to corner', cluster T3
`H7218B` — 'prince', cluster T2
`H7751B` — 'to row', cluster T3
`H8033H` — '[Jerusalem] Is There', cluster (none)
`H8077B` — 'desolation', cluster (none)
`H8227G` — 'Shaphan', cluster (none)
`H5158K` — 'Brook', cluster (none)
`H6160H` — '[Brook of] the Arabah', cluster (none)
`H6793A` — 'hook', cluster (none)
`H7161B` — 'Karnaim', cluster (none)
`H5526D` — 'protector', cluster (none)
`H6327B` — 'scatterer', cluster (none)
`H6335B` — 'to scatter', cluster T3
`H4365A` — 'net', cluster T2
`H5115B` — 'to dwell', cluster T2
`H6075A` — 'to swell', cluster T3
`H6658B` — 'to waste', cluster T3
`H7197B` — 'to assemble', cluster T3
`H2256C` — 'union', cluster M44
`H6327C` — 'to flow', cluster T3
`H7087B` — 'thickness', cluster (none)
`H6999B` — 'incense', cluster (none)
