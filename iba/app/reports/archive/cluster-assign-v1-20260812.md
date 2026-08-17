# Cluster-assignment quality report

> Generated 2026-08-12T14:50:21Z by `cluster.validate`. Read-only findings, not a gate.

- `strong` rows with no cluster assignment at all: **10972**
- `backfill`-origin, non-T2 assignment, not yet promoted (should be `word`): **0**
- exception — non-T2 assignment with no `word_registry` link: **428**
- exception — `backfill` code with an active/clustered sibling: **481**

## Contents

- [Summary](#summary)
- [Exception - no word](#exception-non-t2-cluster-no-word-registry-link)
- [Exception - sibling conflict](#exception-backfill-code-with-an-activeclustered-sibling)

<a id="summary"></a>
## Summary

15293 strong(s) checked
unclassified: 10972
not yet promoted (backfill, non-T2, has a word): 0
exception — no word: 428
exception — sibling conflict: 481

<a id="exception-non-t2-cluster-no-word-registry-link"></a>
## Exception -- non-T2 cluster, no word_registry link

`H8088A` — 'sound', cluster M13
`H8178A` — 'shuddering', cluster M01
`H5254G` — 'to test', cluster M35
`H4148G` — 'discipline', cluster M15
`H5183A` — 'quietness', cluster M33
`H7067G` — 'Jealous [God]', cluster FLAG
`H7067G` — 'Jealous [God]', cluster M28
`H7032G` — 'voice: sound', cluster M42
`H2196` — 'to enrage', cluster M02
`H7236` — 'to grow great', cluster M23
`H5943` — 'Most High [God]', cluster M23
`H7032H` — 'voice', cluster M42
`H1519` — 'to strive', cluster M34
`H7920` — 'to contemplate', cluster M15
`H2416C` — 'living thing', cluster M25
`H8462` — 'beginning', cluster M17
`H1925` — 'glory', cluster M22
`H2388J` — 'to strengthen: prevail over', cluster M23
`H3368` — 'precious', cluster M29
`H4924B` — 'fatness', cluster M46
`H5782` — 'to rouse', cluster M25
`H8052` — 'tidings', cluster M41
`H2416A` — 'alive', cluster M25
`H2416E` — 'life', cluster M25
`H4867` — 'wave', cluster M01
`H2394` — 'force', cluster M23
`H6116` — 'assembly', cluster M05
`H8047G` — 'horror: destroyed', cluster M01
`H5012` — 'to prophesy', cluster M42
`H0341` — 'enemy', cluster M44
`H2256D` — 'destruction', cluster M10
`H4496H` — 'resting', cluster M33
`H2388H` — 'to strengthen: hold', cluster M23
`H6635B` — '[Lord of] Hosts', cluster M23
`H8104H` — 'to keep: guard', cluster M30
`H4468` — 'kingdom', cluster M23
`H0781` — 'to betroth', cluster M44
`H5040` — 'lewdness', cluster M10
`H5493H` — 'to turn aside: depart', cluster M30
`H5074` — 'to wander', cluster M18
`H8088B` — 'report', cluster M41
`H2803H` — 'to devise: count', cluster M15
`H8637` — 'to teach', cluster M15
`H8104J` — 'to keep: careful', cluster M30
`H5331` — 'perpetuity', cluster M34
`G0079` — 'sister', cluster M44
`G0091` — 'to harm', cluster M24
`G0140` — 'to choose', cluster M37
`G0315` — 'to compel', cluster M23
`G0476` — 'opponent', cluster M06
`G0726` — 'to seize', cluster M24
`G0928G` — 'to torture: torture', cluster M03
`G0930` — 'torturer', cluster M03
`G0930` — 'torturer', cluster M27
`G0931` — 'torment', cluster M03
`G0936` — 'to reign', cluster M23
`G1401` — 'slave', cluster M36
`G1435` — 'gift', cluster M39
`G1518` — 'peacemaker', cluster M33
`G1577` — 'assembly', cluster M05
`G1598` — 'to test/tempt', cluster M35
`G1654` — 'charity', cluster M05
`G1777` — 'liable for', cluster M10
`G1843` — 'to agree', cluster M44
`G1950` — 'to forget', cluster M41
`G2168` — 'to thank', cluster M21
`G2511` — 'to clean', cluster M12
`G2537` — 'new', cluster M45
`G2705` — 'to kiss', cluster M05
`G2770` — 'to gain', cluster M37
`G2962H` — 'lord: master', cluster M23
`G3554` — 'illness', cluster M24
`G3844` — 'from/with/beside', cluster FLAG
`G3985G` — 'to test/tempt: tempt', cluster M35
`G3985H` — 'to test/tempt: test', cluster M35
`G4090` — 'bitterly', cluster M03
`G4145` — 'rich', cluster M46
`G4328` — 'to look for', cluster M18
`G4416` — 'firstborn', cluster M37
`G4624` — 'to cause to stumble', cluster M35
`G4862` — 'with', cluster FLAG
`G4889` — 'fellow slave', cluster M44
`G5273` — 'hypocrite', cluster M14
`G5308` — 'high', cluster M08
`G5384` — 'friendly/friend', cluster M05
`G5456H` — 'voice/sound: noise', cluster M42
`G5578` — 'false prophet', cluster M14
`G5580` — 'false Christ', cluster M14
`G0950` — 'to confirm', cluster M13
`G0984` — 'to hurt', cluster M24
`G2512` — 'cleansing', cluster M12
`G3619` — 'building', cluster M05
`G0075` — 'to struggle', cluster M34
`G0364` — 'remembrance', cluster M41
`G0467` — 'to repay', cluster M26
`G0933` — 'palace', cluster M23
`G1000` — 'throwing', cluster M24
`G1329` — 'to interpret', cluster M43
`G1399` — 'female slave', cluster M36
`G3312` — 'arbiter', cluster M15
`G3330` — 'to share', cluster M44
`G3610` — 'slave', cluster M36
`G4273` — 'traitor', cluster M14
`G4422` — 'to frighten', cluster M01
`G4617` — 'to sift', cluster M35
`G4661` — 'plunder', cluster M24
`G4990` — 'savior', cluster M38
`G5271` — 'to pretend', cluster M14
`G5345` — 'news', cluster M41
`G5370` — 'kiss', cluster M05
`G0937` — 'royal', cluster M23
`G1431` — 'free gift', cluster M38
`G2059` — 'to interpret', cluster M43
`G3105` — 'to rave', cluster M16
`H5207` — 'soothing', cluster M04
`G0049` — 'purification', cluster M12
`G0178` — 'uncondemned', cluster M12
`G0236` — 'to change', cluster M45
`G0677` — 'not stumbling', cluster M35
`G1231` — 'to decide', cluster M15
`G1494` — 'sacrificed to idols', cluster M27
`G1497` — 'idol', cluster M27
`G1634` — 'to expire', cluster M24
`G1813` — 'to blot out', cluster M11
`G1917` — 'plot', cluster M14
`G2026` — 'to build up/upon', cluster M05
`G2207` — 'zealot', cluster M21
`G3116` — 'patiently', cluster M34
`G3635` — 'to delay', cluster M09
`G3985I` — 'to test/tempt: try', cluster M35
`G3987` — 'to try', cluster M35
`G4268` — 'foreknowledge', cluster M37
`G4288` — 'eagerness', cluster M29
`G4307` — 'foresight', cluster M15
`G4401` — 'to choose', cluster M37
`G4602` — 'silence', cluster M33
`G6048` — 'judgment', cluster M26
`G0463` — 'tolerance', cluster M05
`G0802` — 'untrustworthy', cluster M14
`G0949` — 'firm', cluster M19
`G1384` — 'tested', cluster M35
`G1434` — 'free gift', cluster M38
`G1558` — 'avenging', cluster M26
`G1731` — 'to show', cluster M05
`G1738` — 'just', cluster M26
`G2644` — 'to reconcile', cluster M11
`G4152` — 'spiritual', cluster M43
`G4306` — 'to care for', cluster M05
`G4348` — 'stumbling block', cluster M35
`G4417` — 'to stumble', cluster M35
`G4519` — 'hosts', cluster M23
`G4825` — 'counselor', cluster M17
`G4832` — 'conformed', cluster M45
`G4865` — 'to struggle', cluster M34
`G5267` — 'accountable', cluster M26
`G5381` — 'hospitality', cluster M05
`G5542` — 'smooth talk', cluster M14
`G1328` — 'interpreter', cluster M15
`G1396` — 'to enslave', cluster M36
`G1493` — "idol's temple", cluster M27
`G1496` — 'idolater', cluster M27
`G1652` — 'pitiful', cluster M05
`G1755` — 'working', cluster M23
`G2058` — 'interpretation', cluster M15
`G2908` — 'greater', cluster M23
`G4148` — 'to enrich', cluster M46
`G4821` — 'to reign with', cluster M23
`G4829` — 'to share', cluster M44
`G1389` — 'to distort', cluster M14
`G2236` — 'most gladly', cluster M04
`G3841` — 'almighty', cluster M23
`G4255` — 'to predetermine', cluster M37
`G4349` — 'stumbling', cluster M35
`G4560` — 'fleshly', cluster M28
`G4705` — 'eager', cluster M34
`G5569` — 'false brother', cluster M14
`G3445` — 'to form', cluster M12
`G0604` — 'to reconcile', cluster M11
`G0781` — 'unwise', cluster M15
`G0138` — 'to choose', cluster M37
`G0951` — 'confirmation', cluster M13
`G4426` — 'to frighten', cluster M01
`G4146` — 'richly', cluster M46
`G4733` — 'firmness', cluster M19
`G3642` — 'fainthearted', cluster M20
`G0462` — 'unholy', cluster M12
`G1128` — 'to train', cluster M15
`G1226` — 'to insist', cluster M15
`G2272` — 'quiet', cluster M33
`G5382` — 'hospitable', cluster M05
`G0329` — 'to rekindle', cluster M45
`G5367` — 'selfish', cluster M08
`G3711` — 'quick-tempered', cluster M02
`G4994` — 'to train', cluster M15
`G0464` — 'to struggle', cluster M34
`G0577` — 'to throw away', cluster M07
`G2610` — 'to conquer', cluster M23
`G0087` — 'impartial', cluster M26
`G1383` — 'testing', cluster M35
`G1503` — 'to resemble', cluster M15
`G5373` — 'friendship', cluster M05
`G0081` — 'brotherhood', cluster M44
`G0934` — 'kingly', cluster M23
`G2900` — 'mighty', cluster M23
`G4599` — 'to strengthen', cluster M23
`G5391` — 'friendly', cluster M05
`G3420` — 'remembrance', cluster M41
`G3913` — 'insanity', cluster M16
`G2434` — 'propitiation', cluster M38
`G0679` — 'without falling', cluster M34
`G0929` — 'torment', cluster M03
`G0929` — 'torment', cluster M35
`G0938G` — 'queen', cluster M23
`G2200` — 'hot', cluster M02
`G3045` — 'rich', cluster M46
`H2102` — 'to boil', cluster M02
`H2102` — 'to boil', cluster M08
`H3513J` — 'to honor: dull', cluster M22
`H3722B` — 'to cover', cluster M38
`H4241` — 'recovery', cluster M25
`H5657` — 'service', cluster M36
`H6349` — 'recklessness', cluster M16
`H6967` — 'height', cluster M08
`H7122G` — 'to encounter: meet', cluster M37
`H7122I` — 'to encounter: chanced', cluster M37
`H7411B` — 'to deceive', cluster M14
`H8082` — 'rich', cluster M46
`H1342` — 'to rise up', cluster M08
`H1826A` — 'to silence: stationary', cluster M33
`H1921` — 'to honor', cluster M22
`H2176` — 'song', cluster M42
`H2390` — 'stronger', cluster M23
`H2422` — 'vigorous', cluster M25
`H2750` — 'burning', cluster M01
`H2750` — 'burning', cluster M02
`H2803G` — 'to devise: design', cluster M15
`H3517` — 'heaviness', cluster FLAG
`H3725` — 'atonement', cluster M10
`H4744` — 'assembly', cluster M05
`H5327A` — 'to struggle', cluster M34
`H6531` — 'severity', cluster M06
`H6696C` — 'to form', cluster M12
`H7067H` — 'jealous', cluster M02
`H7461A` — 'trembling', cluster M01
`H8513` — 'hardship', cluster M24
`H8549G` — 'unblemished', cluster M12
`H1739` — 'sick', cluster M24
`H2893` — 'purifying', cluster M12
`H4768` — 'greatness', cluster M23
`H6186B` — 'to value', cluster M26
`H8549I` — 'unblemished: complete', cluster M12
`H5081H` — 'noble', cluster M34
`H1795` — 'crushing', cluster M24
`H2388I` — 'to strengthen: ensure', cluster M23
`H3631` — 'failing', cluster M24
`H4064` — 'disease', cluster M24
`H6028` — 'dainty', cluster M04
`H7268` — 'quivering', cluster M01
`H7697` — 'madness', cluster M16
`H8080` — 'to grow fat', cluster M46
`H8146` — 'hated', cluster M06
`H8541` — 'bewilderment', cluster M01
`H7850` — 'scourge', cluster M06
`H8089` — 'report', cluster M41
`H2416B` — 'kinsfolk', cluster M25
`H8213` — 'to abase', cluster M07
`H8549J` — 'unblemished: Thummim', cluster M12
`H2416D` — 'community', cluster M44
`H2424` — 'living', cluster M25
`H4937A` — 'support', cluster M19
`H5273B` — 'musical', cluster M22
`H7463` — 'friend', cluster M05
`H1827` — 'silence', cluster M33
`H7182` — 'attentiveness', cluster M41
`H6122` — 'cunning', cluster M14
`H1927` — 'adornment', cluster M22
`H5329` — 'to conduct', cluster M22
`H2810` — 'invention', cluster M14
`H7183B` — 'attentive', cluster M41
`H8196` — 'judgment', cluster M26
`H1059` — 'bitterly', cluster M03
`H8200` — 'to judge', cluster M26
`H8589` — 'fasting', cluster M21
`H0548` — 'sure', cluster M13
`H7183A` — 'attentive', cluster M41
`H6599` — 'edict', cluster FLAG
`H5076` — 'tossing', cluster M03
`H5587B` — 'disquietings', cluster FLAG
`H7009` — 'adversary', cluster M06
`H8630` — 'to prevail', cluster M23
`H2172` — 'melody', cluster M22
`H2270` — 'companion', cluster M44
`H2626` — 'mighty', cluster M23
`H3401` — 'opponent', cluster M06
`H3512B` — 'disheartened', cluster M20
`H4210` — 'melody', cluster M22
`H5010` — 'to disown', cluster M06
`H5222` — 'smitten', cluster M24
`H5765` — 'to act unjustly', cluster M26
`H6115` — 'coercion', cluster M24
`H6125` — 'pressure', cluster M01
`H6199` — 'destitute', cluster M24
`H7438` — 'song', cluster M42
`H7862` — 'gift', cluster M39
`H8428` — 'to wound', cluster M03
`H8502` — 'perfection', cluster M12
`H2019` — 'crooked', cluster M14
`H2475` — 'destruction', cluster M10
`H3513I` — 'to honor: many', cluster M22
`H3514` — 'heaviness', cluster FLAG
`H5099` — 'roaring', cluster M42
`H6104` — 'sluggishness', cluster M24
`H1947` — 'madness', cluster M16
`H1948` — 'madness', cluster M16
`H3908` — 'charm', cluster M14
`H8623` — 'mighty', cluster M23
`H2630` — 'to hoard', cluster M46
`H4766` — 'abundance', cluster M33
`H4893A` — 'mutilation', cluster M07
`H4926` — 'hearing', cluster M41
`H4937B` — 'support', cluster M19
`H5719` — 'voluptuous', cluster M08
`H4835` — 'oppression', cluster M24
`H5494` — 'degenerate', cluster M10
`H5206` — 'filth', cluster M07
`H3520A` — 'glorious', cluster M22
`H4892` — 'destruction', cluster M10
`H7269` — 'quivering', cluster M01
`H7419` — 'refuse', cluster M27
`H7986` — 'imperious', cluster M08
`H8383` — 'toil', cluster M03
`H8383` — 'toil', cluster M36
`H2256C` — 'union', cluster M44
`G0456` — 'to rebuild', cluster T3
`G0598` — 'to crowd up to', cluster T3
`G0618` — 'to get back', cluster T3
`G1239` — 'to distribute', cluster T3
`G1251` — 'to give a hearing', cluster T3
`G1266` — 'to divide', cluster T3
`G1433` — 'to give', cluster T3
`G1460` — 'to live among', cluster T3
`G1554` — 'to lease', cluster T3
`G1629` — 'to terrify', cluster T3
`G1774` — 'to dwell in/with', cluster T3
`G2001` — 'to insist', cluster T3
`G2004` — 'to command', cluster T3
`G2051` — 'to quarrel', cluster T3
`G2767` — 'to mix', cluster T3
`G3307` — 'to divide', cluster T3
`G3346` — 'to transport', cluster T3
`G3351` — 'to deport', cluster T3
`G3611` — 'to dwell', cluster T3
`G3616` — 'to manage a house', cluster T3
`G3621` — 'to manage', cluster T3
`G4039` — 'to dwell around', cluster T3
`G4049` — 'to distract', cluster T3
`G4137` — 'to fulfill', cluster T3
`G4275` — 'to foresee', cluster T3
`G4350` — 'to strike', cluster T3
`G4400` — 'to appoint', cluster T3
`G4880` — 'to die with', cluster T3
`G4900` — 'to bring together', cluster T3
`G4918` — 'to push against', cluster T3
`G4944` — 'to labor together', cluster T3
`G4994` — 'to train', cluster T3
`G5177` — 'to obtain/happen', cluster T3
`G5188` — 'to smoulder', cluster T3
`H0413` — 'to[wards]', cluster T3
`H0935G` — 'to come [in]: come', cluster T3
`H1101B` — 'to feed', cluster T3
`H1598` — 'to defend', cluster T3
`H1680` — 'to glide', cluster T3
`H1820` — 'to cease', cluster T3
`H1980G` — 'to go: went', cluster T3
`H2118` — 'to remove', cluster T3
`H2151A` — 'to shake', cluster T3
`H2168` — 'to prune', cluster T3
`H2232` — 'to sow', cluster T3
`H2254A` — 'to pledge', cluster T3
`H2490A` — 'to bore', cluster T3
`H2490B` — 'to play flute', cluster T3
`H2490I` — 'to profane/begin: fruit', cluster T3
`H2505A` — 'to divide', cluster T3
`H2631` — 'to possess', cluster T3
`H2636` — 'to peel', cluster T3
`H2787` — 'to scorch', cluster T3
`H2939` — 'to feed', cluster T3
`H2963` — 'to tear', cluster T3
`H3245` — 'to found', cluster T3
`H3332H` — 'to pour: cast metal', cluster T3
`H3332I` — 'to pour: set down', cluster T3
`H3335G` — 'to form: formed', cluster T3
`H3335H` — 'to form: potter', cluster T3
`H3513I` — 'to honor: many', cluster T3
`H3513J` — 'to honor: dull', cluster T3
`H3615G` — 'to end: finish', cluster T3
`H3738B` — 'to pierce', cluster T3
`H3745` — 'to proclaim', cluster T3
`H3772G` — 'to cut: cut', cluster T3
`H4804` — 'to pluck', cluster T3
`H4911A` — 'to liken', cluster T3
`H5312` — 'to go out', cluster T3
`H5327B` — 'to desolate', cluster T3
`H5330` — 'to distinguish oneself', cluster T3
`H5452` — 'to intend', cluster T3
`H5456` — 'to prostrate', cluster T3
`H5463` — 'to shut', cluster T3
`H5648` — 'to make', cluster T3
`H5954` — 'to come', cluster T3
`H5998` — 'to toil', cluster T3
`H6105B` — 'to shut eyes', cluster T3
`H6168` — 'to uncover', cluster T3
`H6186A` — 'to arrange', cluster T3
`H6245A` — 'to gleam', cluster T3
`H6485A` — 'to reckon: list', cluster T3
`H6485H` — 'to reckon: punish', cluster T3
`H6589` — 'to open', cluster T3
`H6737` — 'to take provision', cluster T3
`H7088` — 'to roll', cluster T3
`H7114B` — 'to reap', cluster T3
`H7280A` — 'to disturb', cluster T3
`H7411A` — 'to shoot', cluster T3
`H7490` — 'to break', cluster T3
`H7660` — 'to weave', cluster T3
`H7663A` — 'to inspect', cluster T3
`H7666` — 'to buy grain', cluster T3
`H7750` — 'to swerve', cluster T3
`H8618` — 'to confront', cluster T3

<a id="exception-backfill-code-with-an-activeclustered-sibling"></a>
## Exception -- backfill code with an active/clustered sibling

`H8088A` — 'sound', cluster M13
`G5456G` — 'voice/sound: voice', cluster (none)
`H7067G` — 'Jealous [God]', cluster FLAG,M28
`H7032G` — 'voice: sound', cluster M42
`H0935P` — 'to come [in]: bring', cluster (none)
`H1697N` — 'word: portion', cluster (none)
`H2233H` — 'seed: children', cluster T2
`H3117J` — 'day: daily', cluster (none)
`H3956H` — 'tongue: language', cluster (none)
`H6440G` — 'face: before', cluster T2
`H7227B` — 'chief', cluster (none)
`H2235A` — 'vegetable', cluster T2
`H2235B` — 'vegetable', cluster T2
`H3117G` — 'day', cluster (none)
`H5375G` — 'to lift: raise', cluster (none)
`H5973A` — 'with', cluster (none)
`H7218A` — 'head', cluster (none)
`H2006A` — 'if', cluster T2
`H2006B` — 'therefore', cluster T2
`H2492B` — 'to dream', cluster (none)
`H7761H` — 'to set: put/give', cluster (none)
`H5094A` — 'light', cluster (none)
`H6903G` — 'before', cluster (none)
`H6966G` — 'to stand: rise', cluster (none)
`H7032H` — 'voice', cluster M42
`H6966H` — 'to stand: raise', cluster (none)
`H0352A` — 'ram', cluster (none)
`H0505G` — 'thousand', cluster (none)
`H0859A` — 'you [m.s.]', cluster (none)
`H1167J` — 'master: owning', cluster T2
`H2416C` — 'living thing', cluster M25
`H5375M` — 'to lift: look', cluster (none)
`H5869A` — 'eye', cluster (none)
`H5927G` — 'to ascend: rise', cluster (none)
`H6440H` — 'face', cluster (none)
`H6440J` — 'face: surface', cluster (none)
`H0410G` — 'God', cluster T2
`H1980I` — 'to go: walk', cluster (none)
`H3117L` — 'day: today', cluster (none)
`H3318H` — 'to come out: send', cluster (none)
`H3318O` — 'to come out: speak', cluster (none)
`H3615G` — 'to end: finish', cluster T3
`H3772I` — 'to cut: eliminate', cluster (none)
`H4639K` — 'deed', cluster (none)
`H4714G` — 'Egypt', cluster (none)
`H5307N` — 'to fall: presenting', cluster (none)
`H5892B` — 'city', cluster (none)
`H7725H` — 'to return: rescue', cluster (none)
`H3254G` — 'to add: again', cluster (none)
`H3709G` — 'palm', cluster T2
`H5178A` — 'bronze', cluster T2
`H6310G` — 'lip', cluster T2
`H6635H` — 'army: war', cluster (none)
`H6963H` — 'voice: sound', cluster T2
`H0410K` — 'god', cluster (none)
`H2388J` — 'to strengthen: prevail over', cluster M23
`H2505A` — 'to divide', cluster T3
`H4924B` — 'fatness', cluster M46
`H5307J` — 'to fall: kill', cluster (none)
`H5414O` — 'to give: give [marriage]', cluster (none)
`H6213J` — 'to make: [do]', cluster (none)
`H7725L` — 'to return: refuse', cluster (none)
`H7760H` — 'to set: put', cluster (none)
`H7971K` — 'to send: reach', cluster (none)
`H1980M` — 'to go: journey', cluster (none)
`H2416A` — 'alive', cluster M25
`H2416E` — 'life', cluster M25
`H5975H` — 'to stand: appoint', cluster (none)
`H8193J` — 'lip: shore', cluster (none)
`H1980K` — 'to go: come!', cluster (none)
`H1980L` — 'to go: continue', cluster (none)
`H5307I` — 'to fall: allot', cluster (none)
`H5414N` — 'to give: pay', cluster (none)
`H7901G` — 'to lie down: lay down', cluster (none)
`H5869H` — 'eye: seeing', cluster (none)
`H5927H` — 'to ascend: establish', cluster (none)
`H7723H` — 'vanity: vain', cluster (none)
`H1870G` — 'way: conduct', cluster (none)
`H3678G` — 'throne', cluster T2
`H1167H` — 'master: husband', cluster T2
`H8047G` — 'horror: destroyed', cluster M01
`H0197J` — 'Portico', cluster (none)
`H0899B` — 'garment', cluster (none)
`H1588M` — 'garden', cluster T2
`H1870L` — 'way: journey', cluster (none)
`H2346G` — 'wall', cluster T2
`H5414M` — 'to give: cry out', cluster (none)
`H6186A` — 'to arrange', cluster T3
`H7130G` — 'entrails: among', cluster (none)
`H7218I` — 'head: top', cluster (none)
`H0859D` — 'you [m.p.]', cluster T2
`H6735A` — 'envoy', cluster T2
`H6965J` — 'to arise: attack', cluster (none)
`H2256D` — 'destruction', cluster M10
`H2256M` — 'cord', cluster (none)
`H3162A` — 'unitedness', cluster T2
`H5375N` — 'to lift: loud', cluster (none)
`H0935K` — 'to come [in]: [sun]set', cluster (none)
`H7218H` — 'head: leader', cluster (none)
`H1980H` — 'to go: come', cluster (none)
`H2388H` — 'to strengthen: hold', cluster M23
`H5375R` — 'to lift: fight', cluster (none)
`H6635B` — '[Lord of] Hosts', cluster M23
`H4639G` — 'deed: work', cluster (none)
`H6965H` — 'to arise: raise', cluster (none)
`H7114B` — 'to reap', cluster T3
`H7851G` — 'Shittim', cluster (none)
`H2119A` — 'to crawl', cluster (none)
`H8104H` — 'to keep: guard', cluster M30
`H3157H` — 'Jezreel', cluster (none)
`H3157K` — 'Jezreel', cluster (none)
`H3162B` — 'together', cluster T2
`H3947I` — 'to take: marry', cluster (none)
`H6485H` — 'to reckon: punish', cluster T3
`H7760L` — 'to set: appoint', cluster (none)
`H1168A` — 'Baal', cluster (none)
`H1980J` — 'to go: take', cluster (none)
`H1980N` — 'to go: follow', cluster (none)
`H7896G` — 'to set: make', cluster (none)
`H5493H` — 'to turn aside: depart', cluster M30
`H2502A` — 'to rescue', cluster (none)
`H5414K` — 'to give: allow', cluster (none)
`H1870K` — 'way: road', cluster (none)
`H7896I` — 'to set: appoint', cluster (none)
`H1197A` — 'to burn: burn', cluster (none)
`H2556A` — 'to leaven', cluster (none)
`H8088B` — 'report', cluster M41
`H2803H` — 'to devise: count', cluster M15
`H0206H` — 'Aven', cluster (none)
`H3947J` — 'to take: bring', cluster (none)
`H6524A` — 'to sprout', cluster (none)
`H8104J` — 'to keep: careful', cluster M30
`H5375L` — 'to lift: exalt', cluster (none)
`H3947H` — 'to take: recieve', cluster (none)
`H7488B` — 'luxuriant', cluster (none)
`H2254A` — 'to pledge', cluster T3
`G0165G` — 'an age: age', cluster (none)
`G0568H` — 'to have in full', cluster (none)
`G0630H` — 'to release: divorce', cluster (none)
`G0928G` — 'to torture: torture', cluster M03
`G0938H` — 'Queen', cluster (none)
`G1492H` — 'to perceive: see', cluster (none)
`G2012` — 'manager', cluster (none)
`G2083` — 'friend', cluster (none)
`G2149` — 'broad', cluster (none)
`G2787H` — 'ark: Noah', cluster T2
`G2962G` — 'lord: God', cluster (none)
`G3614G` — 'home', cluster T2
`G3614H` — 'home: household', cluster T2
`G3624G` — 'house: home', cluster (none)
`G3985G` — 'to test/tempt: tempt', cluster M35
`G3985H` — 'to test/tempt: test', cluster M35
`G4160I` — 'to do/make: appoint', cluster (none)
`G5259H` — 'by/under: under', cluster (none)
`G1085G` — 'family: descendant', cluster (none)
`G5442H` — 'to keep/guard: guard', cluster (none)
`G5442I` — 'to keep/guard: protect', cluster (none)
`G0568I` — 'to abstain', cluster (none)
`G2839H` — 'common: shared', cluster (none)
`G3985I` — 'to test/tempt: try', cluster M35
`G4160J` — 'to do/make: spend[time]', cluster (none)
`G4160H` — 'to do/make: make', cluster (none)
`H0120H` — 'the man [Adam]', cluster (none)
`H0241I` — 'ear: to ears', cluster T2
`H0328B` — 'softly', cluster T2
`H0410I` — 'El [Elohe]', cluster (none)
`H0410J` — 'El [Most High]', cluster (none)
`H0436H` — 'terebinth', cluster T2
`H0859C` — 'you [f.s.]', cluster T2
`H0859E` — 'you [f.p.]', cluster T2
`H0935I` — 'to come [in]: towards', cluster (none)
`H0935J` — 'to come [in]: advanced', cluster (none)
`H0935M` — 'to come [in]: fulfill', cluster (none)
`H1166I` — 'rule: to marry', cluster T2
`H1167I` — 'master: men', cluster T2
`H1167K` — 'master: [master of]', cluster T2
`H1419K` — 'great: old', cluster T2
`H1481A` — 'to sojourn', cluster (none)
`H1697O` — 'Chronicles', cluster (none)
`H2233G` — 'seed', cluster T2
`H2513A` — 'portion', cluster T2
`H2513B` — 'smoothness', cluster T2
`H3117I` — 'day: year', cluster (none)
`H3318K` — 'to come out: [sun]rise', cluster (none)
`H3318L` — 'to come out: issue', cluster (none)
`H3335G` — 'to form: formed', cluster T3
`H3513J` — 'to honor: dull', cluster M22,T3
`H3559A` — 'to establish: prepare', cluster (none)
`H3709H` — 'palm: sole', cluster T2
`H3709I` — 'palm: dish', cluster (none)
`H3722B` — 'to cover', cluster M38
`H3724B` — 'pitch', cluster (none)
`H4026M` — 'tower', cluster T2
`H4229A` — 'to wipe', cluster (none)
`H4924A` — 'fat', cluster T2
`H5234B` — 'to alienate', cluster (none)
`H5439I` — 'around: whole', cluster (none)
`H5869J` — 'eye: before[the eyes]', cluster (none)
`H5869M` — 'spring', cluster (none)
`H5921B` — 'as', cluster (none)
`H5927I` — 'to ascend: offer up', cluster (none)
`H5927K` — 'to ascend: copulate', cluster (none)
`H6049A` — 'to cloud', cluster (none)
`H6106H` — 'bone: same', cluster T2
`H6310K` — 'lip: according', cluster (none)
`H6440K` — 'face: east', cluster (none)
`H6872A` — 'bundle', cluster T2
`H6946G` — 'Kadesh', cluster (none)
`H6963J` — 'voice: message', cluster T2
`H7122G` — 'to encounter: meet', cluster M37
`H7122I` — 'to encounter: chanced', cluster M37
`H7200J` — 'to see: select', cluster (none)
`H7200N` — 'Provider [God]', cluster (none)
`H7218J` — 'head: first', cluster (none)
`H7235B` — 'to shoot', cluster (none)
`H7363B` — 'to hover', cluster (none)
`H7411B` — 'to deceive', cluster M14
`H7620H` — 'week', cluster (none)
`H7896H` — 'to set: put', cluster (none)
`H7901H` — 'to lie down: sleep', cluster (none)
`H7901I` — 'to lie down: have sex', cluster (none)
`H7971H` — 'to send: let go', cluster (none)
`H7971I` — 'to send: divorce', cluster (none)
`H8193H` — 'lip: words', cluster (none)
`H8193K` — 'lip: language', cluster (none)
`H0352C` — 'leader', cluster T2
`H1167G` — 'master', cluster T2
`H1697L` — 'word: case', cluster (none)
`H1826A` — 'to silence: stationary', cluster M33
`H1980O` — 'to go: send', cluster (none)
`H2436H` — 'bosom: garment', cluster (none)
`H2560B` — 'to daub', cluster (none)
`H2803G` — 'to devise: design', cluster M15
`H2859A` — 'relative', cluster (none)
`H3332H` — 'to pour: cast metal', cluster T3
`H3772G` — 'to cut: cut', cluster T3
`H3947L` — 'to take: fire', cluster (none)
`H4024B` — 'Migdol', cluster (none)
`H4245B` — 'sickness', cluster T2
`H4478B` — 'What?', cluster (none)
`H4609B` — 'step', cluster (none)
`H4809G` — 'Meribah', cluster (none)
`H5251G` — 'Banner [God]', cluster (none)
`H5307H` — 'to fall: deserting', cluster (none)
`H5327A` — 'to struggle', cluster M34
`H5375S` — 'to lift: enthuse', cluster (none)
`H5375V` — 'to lift: count', cluster (none)
`H5414Q` — 'to give: if only!', cluster (none)
`H5439H` — 'around: side', cluster (none)
`H5800C` — 'to leave: release', cluster (none)
`H5953A` — 'to abuse', cluster (none)
`H6030C` — 'to sing', cluster (none)
`H6306B` — 'redemption', cluster T2
`H6310H` — 'lip: edge', cluster (none)
`H6310J` — 'lip: opening', cluster (none)
`H6485A` — 'to reckon: list', cluster T3
`H6485B` — 'reckoning', cluster (none)
`H6696C` — 'to form', cluster M12
`H6963I` — 'voice: thunder', cluster T2
`H6963K` — 'voice: [sound of]', cluster T2
`H7067H` — 'jealous', cluster M02
`H7218L` — 'head: count', cluster (none)
`H7411A` — 'to shoot', cluster T3
`H7461A` — 'trembling', cluster M01
`H7620G` — 'Weeks', cluster (none)
`H7725M` — 'to return: reply', cluster (none)
`H7760I` — 'to set: take', cluster (none)
`H8193I` — 'lip: edge', cluster (none)
`H8549G` — 'unblemished', cluster M12
`H2233I` — 'seed: semen', cluster T2
`H2778C` — 'to acquire', cluster (none)
`H2902A` — 'to overspread', cluster (none)
`H3971B` — 'blemish', cluster (none)
`H5414L` — 'to give: throw', cluster (none)
`H5927M` — 'to ascend: regurgitate', cluster (none)
`H5953B` — 'to glean', cluster (none)
`H5975J` — 'to stand: put', cluster (none)
`H6186B` — 'to value', cluster M26
`H8549I` — 'unblemished: complete', cluster M12
`H0935H` — 'Lebo-[Hamath]', cluster (none)
`H1419J` — 'Great [Sea]', cluster T2
`H1870I` — "[King's] Highway", cluster (none)
`H2023G` — '[Mount] Hor', cluster T2
`H2023H` — '[Mount] Hor', cluster T2
`H2574G` — 'Hamath', cluster (none)
`H3318I` — 'to come out: extends', cluster (none)
`H3318J` — 'to come out: casting [lot]', cluster (none)
`H3318N` — 'to come out: regular', cluster (none)
`H3559I` — 'to establish: make', cluster (none)
`H4229B` — 'to strike', cluster (none)
`H4714J` — '[Brook of] Egypt', cluster T2
`H5081H` — 'noble', cluster M34
`H6306A` — 'redemption', cluster T2
`H6635I` — 'army: duty', cluster (none)
`H7896J` — 'to set: accuse', cluster (none)
`H0935N` — 'to come [in]: besiege', cluster (none)
`H1100G` — 'Belial', cluster (none)
`H1197I` — 'to burn: purge', cluster (none)
`H1697J` — 'word: promised', cluster (none)
`H2388I` — 'to strengthen: ensure', cluster M23
`H2490I` — 'to profane/begin: fruit', cluster T3
`H5254H` — 'to test: try', cluster (none)
`H5375T` — 'to lift: journey', cluster (none)
`H6286B` — 'to re-harvest', cluster (none)
`H7760J` — 'to set: accuse', cluster (none)
`H7760K` — 'to set: consider', cluster (none)
`H0935L` — 'to come [in]: marry', cluster (none)
`H2011G` — '[Topheth of] Hinnom', cluster T2
`H2011H` — '[Topheth of son of] Hinnom', cluster T2
`H2256A` — 'Mahalab', cluster (none)
`H2791A` — 'silently', cluster T2
`H3332I` — 'to pour: set down', cluster T3
`H3956I` — 'tongue: bar', cluster (none)
`H5307L` — 'to fall: fail', cluster (none)
`H5927J` — 'to ascend: attack', cluster (none)
`H7227G` — '[Sidon] the Great', cluster (none)
`H0047H` — 'mighty: stallion', cluster (none)
`H0410H` — 'El [Berith]', cluster (none)
`H0436G` — "[Diviners'] Oak", cluster T2
`H1101B` — 'to feed', cluster T3
`H4496G` — 'Nohah', cluster (none)
`H4629G` — 'Maareh', cluster (none)
`H5375U` — 'to lift: marry', cluster (none)
`H5375W` — 'to lift: bearing [armour]', cluster (none)
`H6049G` — "Diviners' [Oak]", cluster (none)
`H6965K` — 'to arise: guard', cluster (none)
`H7462D` — 'to befriend', cluster (none)
`H7971J` — 'to send: marriage', cluster (none)
`H7971L` — 'to send: burn', cluster (none)
`H8385B` — 'opportunity', cluster (none)
`H1697K` — 'word: deed', cluster (none)
`H1826I` — 'to silence: destroyed', cluster (none)
`H2416B` — 'kinsfolk', cluster M25
`H2793G` — 'Horesh', cluster (none)
`H3157G` — 'Jezreel', cluster (none)
`H3543B` — 'to rebuke', cluster (none)
`H3559J` — 'to establish: commit', cluster (none)
`H3724D` — 'village', cluster (none)
`H5310B` — 'to disperse', cluster (none)
`H5737C` — 'to lack', cluster (none)
`H5860B` — 'to pounce', cluster (none)
`H6030A` — 'to dwell', cluster (none)
`H6310L` — 'lip: one third', cluster (none)
`H6697G` — 'Rocks [of Goats]', cluster T2
`H6872C` — 'Zeror', cluster (none)
`H8549J` — 'unblemished: Thummim', cluster M12
`H1197H` — 'to burn: destroy', cluster (none)
`H2416D` — 'community', cluster M44
`H3157I` — 'Jezreel', cluster (none)
`H3823B` — 'to bake', cluster (none)
`H4937A` — 'support', cluster M19
`H5273B` — 'musical', cluster M22
`H5437K` — 'to turn: changed', cluster (none)
`H5798A` — 'Uzzah', cluster (none)
`H6872B` — 'pebble', cluster T2
`H7462A` — 'House of Shepherds', cluster (none)
`H7760B` — 'fate', cluster (none)
`H0197G` — 'Hall [of pillars]', cluster (none)
`H0197I` — 'Hall [of the Throne]', cluster T2
`H0352B` — 'pillar', cluster T2
`H0425H` — 'Elah', cluster (none)
`H0935O` — 'Lebo', cluster (none)
`H2436I` — 'bosom: lap', cluster (none)
`H2490B` — 'to play flute', cluster T3
`H3678H` — '[Hall of] the Throne', cluster T2
`H4436G` — 'Queen [of Sheba]', cluster T2
`H8106A` — 'Shemer', cluster (none)
`H8585A` — 'conduit', cluster (none)
`H0425I` — 'Elah', cluster (none)
`H1588G` — 'Garden [of Uzza]', cluster T2
`H1588H` — '[Beth]-haggan', cluster T2
`H2657G` — 'Hephzibah', cluster T2
`H4853B` — 'oracle', cluster (none)
`H5307M` — 'to fall: fell [trees]', cluster (none)
`H5327B` — 'to desolate', cluster T3
`H6485L` — 'to reckon: put', cluster (none)
`H7200M` — 'to see: approach', cluster (none)
`H7921C` — 'barrenness', cluster (none)
`H1168H` — 'Baal', cluster (none)
`H3157J` — 'Jezreel', cluster (none)
`H3335H` — 'to form: potter', cluster T3
`H4060G` — 'huge', cluster (none)
`H5437I` — 'to turn: again', cluster (none)
`H1696H` — 'to speak: subdue', cluster (none)
`H3947K` — 'to take: buy', cluster (none)
`H4245A` — 'sickness', cluster T2
`H5401B` — 'to handle', cluster (none)
`H6437H` — 'Corner [Gate]', cluster (none)
`H7183B` — 'attentive', cluster M41
`H7761I` — 'to set: appoint', cluster (none)
`H1419B` — 'Haggedolim', cluster (none)
`H2346H` — '[Broad] Wall', cluster T2
`H4026G` — '[Hananel] Tower', cluster T2
`H4026H` — 'Tower [of the Hundred]', cluster T2
`H4026I` — 'Tower [Of the Ovens]', cluster T2
`H4060B` — 'tribute', cluster (none)
`H4662G` — 'Muster [Gate]', cluster (none)
`H4924C` — 'fat piece', cluster T2
`H5800B` — 'to restore', cluster (none)
`H5869B` — 'Fountain [Gate]', cluster (none)
`H5869G` — 'Fountain of [Drangons]', cluster (none)
`H7183A` — 'attentive', cluster M41
`H7663A` — 'to inspect', cluster T3
`H4436H` — 'queen', cluster T2
`H2490A` — 'to bore', cluster T3
`H2491H` — 'slain: wounded', cluster T2
`H3117H` — 'day: old', cluster (none)
`H3559B` — 'blow', cluster (none)
`H4148H` — 'discipline: instruction', cluster (none)
`H4148I` — 'discipline: bonds', cluster (none)
`H5362A` — 'to strike', cluster (none)
`H5587B` — 'disquietings', cluster FLAG,T2
`H5848A` — 'to turn aside', cluster (none)
`H7200K` — 'to see: enjoy', cluster (none)
`H7280A` — 'to disturb', cluster T3
`H0047G` — 'mighty: ox', cluster (none)
`H0047J` — 'mighty: angel', cluster (none)
`H2560A` — 'to aggitate', cluster (none)
`H3512B` — 'disheartened', cluster M20
`H4480B` — 'portion', cluster (none)
`H4911A` — 'to liken', cluster T3
`H5848B` — 'to envelope', cluster (none)
`H5849B` — 'to crown', cluster (none)
`H6670B` — 'to shine', cluster (none)
`H7462C` — 'to accompany', cluster (none)
`H7997B` — 'to loot', cluster (none)
`H2436J` — 'bosom: secret', cluster (none)
`H2506B` — 'smoothness', cluster T2
`H3513I` — 'to honor: many', cluster M22,T3
`H5433A` — 'to imbibe', cluster (none)
`H6106I` — 'bone: body', cluster T2
`H6612B` — 'simplicity', cluster (none)
`H6735B` — 'hinge', cluster T2
`H6001B` — 'laborious', cluster T2
`H3724C` — 'henna', cluster (none)
`H5437J` — 'to turn: repell', cluster (none)
`H0352D` — 'terebinth', cluster T2
`H1166G` — 'Married', cluster (none)
`H1238B` — 'to empty', cluster (none)
`H1826B` — 'to wail', cluster (none)
`H1870H` — 'Way', cluster (none)
`H2151A` — 'to shake', cluster T3
`H2778B` — 'to winter', cluster (none)
`H2791B` — 'craftily', cluster T2
`H3068I` — '[Jerusalem of] the Lord', cluster (none)
`H4714I` — '[Sea of] Egypt', cluster T2
`H4893A` — 'mutilation', cluster M07
`H4937B` — 'support', cluster M19
`H5183B` — 'descent', cluster (none)
`H5218A` — 'stricken', cluster (none)
`H5737B` — 'to hoe', cluster (none)
`H5800G` — 'Forsaken', cluster (none)
`H5892G` — 'City [of On]', cluster (none)
`H5892I` — 'city [of God]', cluster (none)
`H5953C` — 'to mock', cluster (none)
`H6090B` — 'idol', cluster T2
`H6105B` — 'to shut eyes', cluster T3
`H6121B` — 'steep', cluster (none)
`H7971M` — 'to send: exile', cluster (none)
`H8077G` — 'Desolate', cluster (none)
`H8178B` — 'storm', cluster (none)
`H3820B` — 'Leb', cluster (none)
`H6089B` — 'vessel', cluster T2
`H6245A` — 'to gleam', cluster T3
`H6963B` — 'frivolity', cluster T2
`H6965A` — '[Leb]-kamai', cluster (none)
`H5439J` — 'around: neighours', cluster (none)
`H2258A` — 'pledge', cluster T2
`H2258B` — 'pledge', cluster T2
`H2428B` — 'Helech', cluster (none)
`H3068H` — 'The Lord', cluster (none)
`H3520A` — 'glorious', cluster M22
`H5414J` — 'to give: turn', cluster (none)
`H5674G` — '[Valley of] the Travelers', cluster (none)
`H6213B` — 'to press', cluster (none)
`H6524C` — 'to fly', cluster (none)
`H7218B` — 'prince', cluster (none)
`H8077B` — 'desolation', cluster (none)
`H7161B` — 'Karnaim', cluster (none)
`H5115B` — 'to dwell', cluster (none)
`H2256C` — 'union', cluster M44
