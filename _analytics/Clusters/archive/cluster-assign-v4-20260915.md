# Cluster-assignment quality report

> Generated 2026-09-15T07:17:40Z by `cluster.validate`. Read-only findings, not a gate.

- `strong` rows with no cluster assignment at all: **0**
- `backfill`-origin, non-T2 assignment, not yet promoted (should be `word`): **0**
- exception — non-T2 assignment with no `word_registry` link: **4460**
- exception — `backfill` code with an active/clustered sibling: **2789**

## Contents

- [Summary](#summary)
- [Exception - no word](#exception-non-t2-cluster-no-word-registry-link)
- [Exception - sibling conflict](#exception-backfill-code-with-an-activeclustered-sibling)
- unclassified

<a id="summary"></a>
## Summary

15455 strong(s) checked
unclassified: 0
not yet promoted (backfill, non-T2, has a word): 0
exception — no word: 4460
exception — sibling conflict: 2789

<a id="exception-non-t2-cluster-no-word-registry-link"></a>
## Exception -- non-T2 cluster, no word_registry link

`H8088A` — 'sound', cluster M62
`H2048A` — 'to mock', cluster M08
`H5607A` — 'mockery', cluster M08
`H8178A` — 'shuddering', cluster M01
`H3856A` — 'to languish', cluster M24
`H5254G` — 'to test', cluster M35
`H4148G` — 'discipline', cluster M16
`H5183A` — 'quietness', cluster M33
`H7067G` — 'Jealous [God]', cluster FLAG,M18
`H4654A` — 'ruin', cluster M55
`H7032G` — 'voice: sound', cluster M84
`H8186A` — 'horror', cluster M01
`H8438A` — 'worm', cluster T13
`H0430G` — 'God', cluster T7
`H0776G` — 'land: country/planet', cluster T10
`H0828` — 'Ashpenaz', cluster T8
`H0834A` — 'which', cluster T6
`H0894` — 'Babylon', cluster T10
`H1004Q` — 'house: temple', cluster T10
`H1095` — 'Belteshazzar', cluster T8
`H3063G` — 'Judah', cluster T11
`H3079` — 'Jehoiakim', cluster T8
`H3389` — 'Jerusalem', cluster T11
`H3478` — 'Israel', cluster T11
`H3627` — 'article/utensil', cluster T12
`H3778` — 'Chaldea', cluster T10
`H4335` — 'Meshach', cluster T8
`H4428G` — 'king', cluster M72
`H4487` — 'to count', cluster M26
`H5019` — 'Nebuchadnezzar', cluster T8
`H5612H` — 'scroll: book', cluster T12
`H5664` — 'Abednego', cluster T8
`H6440G` — 'face: before', cluster T14
`H6579` — 'noble', cluster M34
`H7714` — 'Shadrach', cluster T8
`H8152` — 'Shinar', cluster T10
`H8269` — 'ruler', cluster M72
`H9002` — 'and', cluster T6
`H3808` — 'not', cluster T5
`H0113` — 'lord', cluster T7,T8
`H2196` — 'to enrage', cluster M02
`H3566` — 'Cyrus', cluster T8
`H4325G` — 'water', cluster T13
`H7218A` — 'head', cluster T14
`H0007` — 'to destroy', cluster M10
`H0746B` — 'Arioch', cluster T8
`H0895` — 'Babylon', cluster T10
`H1768` — 'that', cluster T6
`H1841H` — 'Daniel', cluster T8
`H2006A` — 'if', cluster T6
`H2006B` — 'therefore', cluster T6
`H2164` — 'to agree', cluster M44
`H2324` — 'to show', cluster M05
`H3779` — 'Chaldean', cluster T11
`H3809` — 'not', cluster T5
`H3861` — 'except', cluster T6
`H4406` — 'word', cluster M65
`H4430` — 'king', cluster M72
`H4978` — 'gift', cluster M39
`H5649` — 'servant/slave', cluster M36
`H5957` — 'perpetuity', cluster M34
`H6032` — 'to answer', cluster M41
`H6591` — 'interpretation', cluster M63
`H7593` — 'to ask', cluster M21
`H8133` — 'to change', cluster M45
`H1096` — 'Belteshazzar', cluster T8
`H2608B` — 'Hananiah', cluster T8
`H3061` — 'Judah', cluster T8
`H4333` — 'Mishael', cluster T8
`H4903` — 'bed', cluster T12
`H5020` — 'Nebuchadnezzar', cluster T8
`H5642A` — 'to hide', cluster M20
`H5839` — 'Azariah', cluster T8
`H1757` — 'Dura', cluster T10
`H7030` — 'lyre', cluster T12
`H7314` — 'height', cluster M08
`H0772H` — 'earth: inferior', cluster T10
`H0772I` — 'earth: planet', cluster T10
`H2122` — 'splendor', cluster M71
`H2255` — 'to destroy', cluster M10
`H2635` — 'clay', cluster T13
`H3410` — 'thigh', cluster T14
`H4336` — 'Meshach', cluster T8
`H4437` — 'kingdom', cluster M72
`H5208` — 'soothing', cluster M04
`H5665` — 'Abednego', cluster T8
`H5673` — 'service', cluster M36
`H5776` — 'bird', cluster T13
`H6523` — 'iron', cluster T12
`H7236` — 'to grow great', cluster M23
`H7715` — 'Shadrach', cluster T8
`H1907` — 'counselor', cluster M16
`H3831` — 'garment', cluster T12
`H4398` — 'angel', cluster T9
`H5943` — 'Most High [God]', cluster M72
`H0772G` — 'earth: soil', cluster T13
`H0852` — 'sign', cluster M43
`H1883` — 'grass', cluster T13
`H1922` — 'to honor', cluster M71
`H1923` — 'honor', cluster M71
`H2920` — 'dew', cluster T13
`H5403` — 'eagle', cluster T13
`H6136` — 'root', cluster T13
`H6211B` — 'grass', cluster T13
`H6853` — 'bird', cluster T13
`H7032H` — 'voice', cluster M84
`H7261` — 'noble', cluster M34
`H7680` — 'to grow great', cluster M23
`H8215` — 'low', cluster M09
`H8330` — 'root', cluster T13
`H8421G` — 'to return: return', cluster M11
`H8627` — 'to confirm', cluster M62
`H0263` — 'explanation', cluster M43
`H1113` — 'Belshazzar', cluster T8
`H2002` — 'chain', cluster T12
`H2112` — 'to tremble', cluster M01
`H3390` — 'Jerusalem', cluster T10
`H4076G` — 'Mede', cluster T10
`H5043` — 'lampstand', cluster T12
`H6540` — 'Persia', cluster T10
`H6590` — 'to interpret', cluster M63
`H0744` — 'lion', cluster T13
`H1868H` — 'Darius', cluster T8
`H2248` — 'crime', cluster M55
`H2908` — 'fasting', cluster M21
`H5824` — 'signet ring', cluster T12
`H7712` — 'to strive', cluster M34
`H8122` — 'sun', cluster T13
`H1519` — 'to strive', cluster M34
`H1535` — 'wheel', cluster T12
`H1678` — 'bear', cluster T13
`H5103H` — 'river', cluster T10
`H5202` — 'to keep', cluster M74
`H5245` — 'leopard', cluster T13
`H5609` — 'scroll', cluster T12
`H5946` — 'Most High [God]', cluster T7
`H5967` — 'rib', cluster T14
`H6015` — 'wool', cluster T13
`H6050` — 'cloud', cluster T13
`H7920` — 'to contemplate', cluster M15
`H8046` — 'to destroy', cluster M10
`H8120` — 'to minister', cluster M36
`H8128` — 'tooth', cluster T14
`H8517` — 'snow', cluster T13
`H0120G` — 'man', cluster T8
`H0195` — 'Ulai', cluster T10
`H0352A` — 'ram', cluster T13
`H0776H` — 'land: soil', cluster T13
`H1002` — 'palace', cluster M72
`H1112` — 'Belshazzar', cluster T8
`H1403` — 'Gabriel', cluster T9
`H2416C` — 'living thing', cluster M25
`H3120H` — 'Greece', cluster T10
`H3588A` — 'for', cluster T6
`H4074H` — 'Media', cluster T10
`H5045H` — 'south', cluster T10
`H5867A` — 'Elam', cluster T10
`H5869A` — 'eye', cluster T14
`H6440H` — 'face', cluster T14
`H6440J` — 'face: surface', cluster T14
`H6539` — 'Persia', cluster T10
`H6743B` — 'to prosper', cluster M46
`H6828G` — 'north', cluster T10
`H6842` — 'male goat', cluster T13
`H7800` — 'Susa', cluster T10
`H8064` — 'heaven', cluster T10
`H8462` — 'beginning', cluster M16
`H0325` — 'Ahasuerus', cluster T8
`H0376G` — 'man', cluster T8
`H0408` — 'not', cluster T5
`H0410G` — 'God', cluster T7
`H1867I` — 'Darius', cluster T8
`H2022G` — 'mountain: mount', cluster T10
`H3068G` — 'LORD', cluster T7
`H3414L` — 'Jeremiah', cluster T8
`H4074I` — 'Mede', cluster T10
`H4421` — 'battle', cluster M10
`H4503G` — 'grain offering', cluster M36
`H4687` — 'commandment', cluster M54
`H4714G` — 'Egypt', cluster T11
`H4872` — 'Moses', cluster T8
`H5892B` — 'city', cluster T11
`H0210` — 'Uphaz', cluster T10
`H0518B` — 'if: except', cluster T6
`H0582` — 'human', cluster T8
`H0784` — 'fire', cluster T13
`H1300B` — 'lightning', cluster T13
`H2244` — 'to hide', cluster M20
`H2313` — 'Tigris', cluster T10
`H3588B` — 'that if: except', cluster T6
`H3709G` — 'palm', cluster T14
`H4317Q` — 'Michael', cluster T8,T9
`H5104H` — 'river', cluster T10
`H6310G` — 'lip', cluster T14
`H0068G` — 'stone', cluster T12
`H0123G` — 'Edom', cluster T10
`H0127G` — 'land: soil', cluster T13
`H0168G` — 'tent', cluster T10
`H0410K` — 'god', cluster T7
`H0643` — 'palace', cluster M72
`H0802G` — 'woman', cluster T8
`H0961` — 'plunder', cluster M24
`H1925` — 'glory', cluster M22
`H2091` — 'gold', cluster T12
`H2388J` — 'to strengthen: prevail over', cluster M23
`H2719` — 'sword', cluster T12
`H3220G` — 'sea', cluster T13
`H3368` — 'precious', cluster M18
`H3569G` — 'Cushite', cluster T11
`H3701G` — 'silver: money', cluster T12
`H3794H` — 'Cyprus', cluster T10
`H3864` — 'Libya', cluster T10
`H4075` — 'Mede', cluster T11
`H4124G` — 'Moab', cluster T11
`H4924B` — 'fatness', cluster M46
`H5342` — 'branch', cluster T13
`H5782` — 'to rouse', cluster M25
`H5983` — 'Ammon', cluster T10
`H6716` — 'ship', cluster T12
`H7393G` — 'chariot', cluster T12
`H7979` — 'table', cluster T12
`H8045` — 'to destroy', cluster M10
`H8052` — 'tidings', cluster M82
`H8328` — 'root', cluster T13
`H2416A` — 'alive', cluster M25
`H2416E` — 'life', cluster M25
`H5703` — 'perpetuity', cluster M34
`H6083` — 'dust', cluster T13
`H8193J` — 'lip: shore', cluster T14
`H0573` — 'Amittai', cluster T8
`H1709H` — 'fish', cluster T13
`H3124` — 'Jonah', cluster T8
`H3305` — 'Joppa', cluster T10
`H5210` — 'Nineveh', cluster T10
`H5600` — 'ship', cluster T12
`H5680` — 'Hebrew', cluster T10
`H7453` — 'neighbor', cluster T8
`H8659H` — 'Tarshish', cluster T10
`H1710` — 'fish', cluster T13
`H4867` — 'wave', cluster M01
`H5869H` — 'eye: seeing', cluster T14
`H7585` — 'hell: Sheol', cluster T10
`H1870G` — 'way: conduct', cluster M76
`H2394` — 'force', cluster M23
`H3678G` — 'throne', cluster M72
`H6629G` — 'flock', cluster T13
`H7021` — 'plant', cluster T13
`H8121` — 'sun', cluster T13
`H8438B` — 'worm', cluster T13
`H0518A` — 'if', cluster T6
`H0697` — 'locust', cluster T13
`H0738B` — 'lion', cluster T13
`H1501` — 'locust', cluster T13
`H1612` — 'vine', cluster T13
`H2625` — 'locust', cluster T13
`H3100T` — 'Joel', cluster T8
`H3218` — 'locust', cluster T13
`H3548` — 'priest', cluster M36
`H3755` — 'to tend vineyards', cluster T8
`H3833C` — 'lion', cluster T13
`H4057B` — 'wilderness', cluster T10
`H4196` — 'altar', cluster T12
`H4973` — 'jaw', cluster T14
`H6086H` — 'tree', cluster T13
`H6116` — 'assembly', cluster M44
`H6602` — 'Pethuel', cluster T8
`H7111` — 'splinter', cluster M02
`H7704G` — 'land: country', cluster T10
`H8047G` — 'horror: destroyed', cluster M01
`H8127G` — 'tooth', cluster T14
`H0899B` — 'garment', cluster T12
`H1653` — 'rain', cluster T13
`H3394` — 'moon', cluster T13
`H4264` — 'camp', cluster T10
`H4456` — 'spring rain', cluster T13
`H4818` — 'chariot', cluster T12
`H5012` — 'to prophesy', cluster M43
`H5159` — 'inheritance', cluster M46
`H5731B` — 'Eden', cluster T10
`H6051` — 'cloud', cluster T13
`H6205` — 'cloud', cluster T13
`H6726` — 'Zion', cluster T10
`H6951` — 'assembly', cluster M44
`H7130G` — 'entrails: among', cluster T14
`H7218I` — 'head: top', cluster T14
`H7704M` — 'field', cluster T10
`H7782` — 'trumpet', cluster T12
`H1389I` — 'hill', cluster T10
`H3092K` — '[Valley of] Jehoshaphat', cluster T10
`H4038` — 'sickle', cluster T12
`H4725` — 'place', cluster T10
`H5158I` — '[Shittim] Valley', cluster T10
`H5197` — 'to drip/prophesy', cluster M43
`H5789` — 'to help', cluster M45
`H6010N` — 'Valley [of Kidron]', cluster T10
`H6010R` — 'valley', cluster T10
`H6429` — 'Philistia', cluster T10
`H6721H` — 'Sidon', cluster T10
`H6865` — 'Tyre', cluster T10
`H7420` — 'spear', cluster T12
`H7615` — 'Sabean', cluster T8
`H3069` — 'YHWH/God', cluster T7
`H3130G` — 'Joseph', cluster T8
`H3290` — 'Jacob', cluster T8
`H3669A` — 'Canaanite', cluster T11
`H5045G` — 'Negeb', cluster T10
`H5404` — 'eagle', cluster T13
`H5553H` — 'crag', cluster T10
`H5614` — 'Sepharad', cluster T10
`H5662R` — 'Obadiah', cluster T8
`H6215H` — 'Esau', cluster T11
`H6215I` — '[Mount] Esau', cluster T10
`H6563` — 'plunder', cluster M24
`H6886` — 'Zarephath', cluster T10
`H8179G` — 'gate', cluster T12
`H8487H` — 'Teman', cluster T10
`H0271G` — 'Ahaz', cluster T8
`H0392G` — 'Achzib', cluster T10
`H1018` — 'Beth-ezel', cluster T10
`H1036` — 'Beth-le-aphrah', cluster T10
`H1116` — 'high place', cluster T10
`H1516R` — 'valley', cluster T10
`H1661` — 'Gath', cluster T10
`H3147H` — 'Jotham', cluster T8
`H3169H` — 'Hezekiah', cluster T8
`H3284` — 'ostrich', cluster T13
`H3923` — 'Lachish', cluster T10
`H4182` — 'Moresheth-gath', cluster T10
`H4318K` — 'Micah', cluster T8
`H4762G` — 'Mareshah', cluster T10
`H4796` — 'Maroth', cluster T10
`H5725` — 'Adullam', cluster T10
`H5979` — 'support', cluster M70
`H6630` — 'Zaanan', cluster T10
`H8111` — 'Samaria', cluster T10
`H8208` — 'Shaphir', cluster T10
`H8577A` — 'jackal', cluster T13
`H0341` — 'enemy', cluster M06
`H0518I` — 'if: surely yes', cluster T6
`H1699A` — 'pasture', cluster T10
`H2256D` — 'destruction', cluster M55
`H2256M` — 'cord', cluster M03,T12
`H3863` — 'if', cluster T6
`H4496H` — 'resting', cluster M33
`H4904` — 'bed', cluster T12
`H8008` — 'garment', cluster T12
`H3384B` — 'to show', cluster M05
`H5518A` — 'pot', cluster T12
`H5785` — 'skin', cluster T14
`H7218H` — 'head: leader', cluster M72
`H1270` — 'iron', cluster T12
`H1854` — 'to crush', cluster M10
`H2388H` — 'to strengthen: hold', cluster M23
`H2595` — 'spear', cluster T12
`H6541` — 'hoof', cluster T14
`H6635B` — '[Lord of] Hosts', cluster M72
`H7151` — 'town', cluster T10
`H0672G` — 'Ephrathah', cluster T8
`H0804G` — 'Assyria', cluster T11
`H1035G` — 'Bethlehem', cluster T10
`H2919` — 'dew', cluster T13
`H3715A` — 'lion', cluster T13
`H3895H` — 'jaw', cluster T14
`H5248` — 'Nimrod', cluster T8
`H5483M` — 'horse', cluster T13
`H7626G` — 'tribe: staff', cluster T12
`H0175` — 'Aaron', cluster T8
`H0256G` — 'Ahab', cluster T8
`H1060` — 'firstborn', cluster M37
`H1109A` — 'Balaam', cluster T8
`H1111` — 'Balak', cluster T8
`H1160H` — 'Beor', cluster T8
`H1537G` — 'Gilgal', cluster T10
`H3599` — 'purse', cluster T12
`H4294G` — 'tribe: rod', cluster T12
`H4813G` — 'Miriam', cluster T8
`H5158A` — 'torrent: river', cluster T10
`H5695` — 'calf', cluster T13
`H5930A` — 'burnt offering', cluster M36
`H6018G` — 'Omri', cluster T8
`H7851G` — 'Shittim', cluster T10
`H0085` — 'Abraham', cluster T8
`H0480` — 'woe!', cluster M03
`H1316` — 'Bashan', cluster T10
`H1568G` — 'Gilead', cluster T10
`H2916` — 'mud', cluster T13
`H4693` — 'Egypt', cluster T10
`H5104G` — 'River', cluster T10
`H6822` — 'to watch', cluster M74
`H8104H` — 'to keep: guard', cluster M74
`H0802H` — 'woman: wife', cluster T8
`H0882H` — 'Beeri', cluster T8
`H1954J` — 'Hosea', cluster T8
`H2344` — 'sand', cluster T13
`H3058H` — 'Jehu', cluster T8
`H3101J` — 'Joash', cluster T8
`H3157H` — 'Jezreel', cluster T10
`H3157K` — 'Jezreel', cluster T8
`H3379H` — 'Jeroboam', cluster T8
`H4468` — 'kingdom', cluster M72
`H5818G` — 'Uzziah', cluster T8
`H6010M` — 'Valley [of Jezreel]', cluster T10
`H0269` — 'sister', cluster M44
`H0781` — 'to betroth', cluster M44
`H1168A` — 'Baal', cluster T10
`H2320H` — 'month: new moon', cluster T13
`H5040` — 'lewdness', cluster M57
`H5141` — 'ring', cluster T12
`H5518B` — 'thorn', cluster T13
`H5775` — 'bird', cluster T13
`H5911` — '[Valley of] Achor', cluster T10
`H6010G` — 'Valley [of Achor]', cluster T10
`H6435` — 'lest', cluster T6
`H6601B` — 'to entice', cluster M77
`H6785` — 'wool', cluster T13
`H0646` — 'ephod', cluster T12
`H1732` — 'David', cluster T8
`H0669G` — 'Ephraim', cluster T8
`H1007` — 'Beth-aven', cluster T10
`H3532` — 'lamb', cluster T13
`H4731` — 'rod', cluster T12
`H5493H` — 'to turn aside: depart', cluster M11
`H6086G` — 'tree: wood', cluster T13
`H6510` — 'heifer', cluster T13
`H1144G` — 'Benjamin', cluster T8
`H1390H` — 'Gibeah', cluster T10
`H2502A` — 'to rescue', cluster M45
`H2689` — 'trumpet', cluster T12
`H4709H` — 'Mizpah', cluster T10
`H7414G` — 'Ramah', cluster T10
`H7826` — 'lion', cluster T13
`H8396G` — '[Mount] Tabor', cluster T10
`H0121G` — 'Adam', cluster T8
`H0561` — 'word', cluster M65
`H7927G` — 'Shechem', cluster T10
`H8186B` — 'horror', cluster M01
`H0188` — 'woe!', cluster M03
`H1077` — 'not', cluster T5
`H3123` — 'dove', cluster T13
`H5074` — 'to wander', cluster M76
`H5920H` — 'height', cluster M08
`H7701` — 'violence', cluster M10
`H8088B` — 'report', cluster M82
`H8574H` — 'oven', cluster T12
`H1890` — 'gift', cluster M39
`H2803H` — 'to devise: count', cluster M64
`H6780` — 'branch', cluster T13
`H1187` — 'Baal of Peor', cluster T7
`H2336` — 'thistle', cluster T13
`H4644` — 'Memphis', cluster T10
`H0206H` — 'Aven', cluster T10
`H1008G` — 'Bethel', cluster T10
`H1009` — 'Beth-arbel', cluster T10
`H1863` — 'thistle', cluster T13
`H2986` — 'to conduct', cluster M76
`H5697A` — 'heifer', cluster T13
`H6975` — 'thorn', cluster T13
`H8020` — 'Shalman', cluster T8
`H0126` — 'Admah', cluster T10
`H5288` — 'youth', cluster T8
`H5688` — 'cord', cluster M03,T12
`H6636` — 'Zeboiim', cluster T10
`H6833` — 'bird', cluster T13
`H8637` — 'to teach', cluster M16
`H0758O` — 'Aram', cluster T10
`H3667B` — 'merchant', cluster T10
`H4397H` — 'messenger: angel', cluster T9
`H8104J` — 'to keep: careful', cluster M74
`H0645` — 'then', cluster T6
`H1677` — 'bear', cluster T13
`H5246` — 'leopard', cluster T13
`H6987` — 'destruction', cluster M55
`H3844G` — 'Lebanon', cluster T10
`H0176A` — 'or', cluster T6
`H0518J` — 'if: until', cluster T6
`H0738A` — 'lion', cluster T13
`H0758I` — 'Syria', cluster T10
`H0831` — 'Ashkelon', cluster T10
`H1040` — 'Beth-eden', cluster T10
`H1130I` — 'Ben-hadad', cluster T8
`H1224G` — 'Bozrah', cluster T10
`H1237J` — '[Aven] Valley', cluster T10
`H1834` — 'Damascus', cluster T10
`H2371` — 'Hazael', cluster T8
`H3760G` — 'Carmel', cluster T10
`H3767` — 'leg', cluster T14
`H4296` — 'bed', cluster T12
`H5275` — 'sandal', cluster T12
`H5331` — 'perpetuity', cluster M34
`H5804` — 'Gaza', cluster T10
`H5986` — 'Amos', cluster T8
`H6138` — 'Ekron', cluster T10
`H6210` — 'bed', cluster T12
`H6430G` — 'Philistine', cluster T11
`H7024B` — 'Kir', cluster T10
`H7152H` — 'Kerioth', cluster T10
`H7237` — 'Rabbah', cluster T10
`H7272` — 'foot', cluster T14
`H8127H` — 'tooth: ivory', cluster T14
`H8620` — 'Tekoa', cluster T10
`G0006` — 'Abel', cluster T8
`G0011` — 'Abraham', cluster T8
`G0030` — 'jar', cluster T12
`G0032G` — 'angel', cluster T9
`G0032H` — 'angel: messenger', cluster T9
`G0068H` — 'Field (of blood)', cluster T10
`G0079` — 'sister', cluster M44
`G0086` — 'hell: Hades', cluster T10
`G0091` — 'to harm', cluster M24
`G0105` — 'eagle', cluster T13
`G0125` — 'Egypt', cluster T10
`G0129G` — 'blood', cluster T14
`G0129H` — '(Field of) Blood', cluster T10
`G0140` — 'to choose', cluster M64
`G0173` — 'a thorn', cluster T13
`G0200` — 'locust', cluster T13
`G0211` — 'jar', cluster T12
`G0258` — 'fox', cluster T13
`G0285` — 'sand', cluster T13
`G0288` — 'vine', cluster T13
`G0302` — 'if', cluster T6
`G0310` — 'to cry out', cluster M42
`G0315` — 'to compel', cluster M23
`G0344` — 'to return', cluster M11
`G0372` — 'rest', cluster M33
`G0373` — 'to give rest', cluster M33
`G0402` — 'to leave', cluster M59
`G0417` — 'wind', cluster T13
`G0435G` — 'man', cluster T8
`G0436` — 'to oppose', cluster M06
`G0444` — 'a human', cluster T8
`G0476` — 'opponent', cluster M06
`G0513` — 'axe', cluster T12
`G0527` — 'tender', cluster M05
`G0611` — 'to answer', cluster M41
`G0622` — 'to destroy', cluster M10
`G0672` — 'to leave', cluster M59
`G0684` — 'destruction', cluster M55
`G0686` — 'therefore', cluster T6
`G0694` — 'money', cluster M46
`G0707` — 'Arimathea', cluster T10
`G0726` — 'to seize', cluster M24
`G0732` — 'ill', cluster M73
`G0796` — 'lightning', cluster T13
`G0820` — 'dishonored', cluster M07
`G0897` — 'Babylon', cluster T11
`G0914` — 'Barachiah', cluster T8
`G0928G` — 'to torture: torture', cluster M03
`G0930` — 'torturer', cluster M55
`G0931` — 'torment', cluster M03
`G0936` — 'to reign', cluster M72
`G0965` — 'Bethlehem', cluster T10
`G0975` — 'scroll', cluster T12
`G0997` — 'to help', cluster M45
`G1028` — 'rain', cluster T13
`G1056G` — 'Galilee', cluster T10
`G1056H` — '(Sea of) Galilee', cluster T10
`G1057` — 'Galilean', cluster T11
`G1116` — 'Gomorrah', cluster T10
`G1127` — 'to keep watch', cluster M74
`G1135G` — 'woman', cluster T8
`G1135H` — 'woman: wife', cluster T8
`G1138` — 'David', cluster T8
`G1140` — 'demon', cluster T4
`G1147` — 'finger', cluster T14
`G1158` — 'Daniel', cluster T8
`G1161` — 'then', cluster T6
`G1166` — 'to show', cluster M05
`G1321` — 'to teach', cluster M15
`G1372` — 'to thirst', cluster M18
`G1390` — 'gift', cluster M39
`G1401` — 'slave', cluster M78
`G1435` — 'gift', cluster M39
`G1437` — 'if', cluster T6
`G1484` — 'Gentiles', cluster T11
`G1518` — 'peacemaker', cluster M33
`G1577` — 'assembly', cluster M44
`G1598` — 'to test/tempt', cluster M35
`G1654` — 'charity', cluster M05
`G1694` — 'Immanuel', cluster T8
`G1718` — 'to show', cluster M05
`G1727` — 'hostile', cluster M06
`G1777` — 'liable for', cluster M55
`G1843` — 'to agree', cluster M44
`G1875` — 'when/as soon as', cluster T6
`G1893` — 'since', cluster T6
`G1894` — 'since', cluster T6
`G1950` — 'to forget', cluster M81
`G2047` — 'desert', cluster T10
`G2048` — 'deserted', cluster T10
`G2050` — 'devastation', cluster M55
`G2083` — 'friend', cluster M05
`G2132` — 'to reconcile', cluster M05
`G2168` — 'to thank', cluster M49
`G2190` — 'enemy', cluster M06
`G2194` — 'Zebulun', cluster T8
`G2197G` — 'Zechariah', cluster T8
`G2198` — 'to live', cluster M25
`G2218` — 'yoke/scales', cluster T12
`G2222` — 'life', cluster M25
`G2223` — 'belt/sash/girdle', cluster T12
`G2228` — 'or', cluster T6
`G2243` — 'Elijah', cluster T8
`G2246` — 'sun', cluster T13
`G2268` — 'Isaiah', cluster T8
`G2384G` — 'Jacob', cluster T8
`G2384H` — 'Jacob', cluster T8
`G2408` — 'Jeremiah', cluster T8
`G2410` — 'Jericho', cluster T10
`G2414` — 'Jerusalem', cluster T11
`G2419` — 'Jerusalem', cluster T10
`G2421` — 'Jesse', cluster T8
`G2423` — 'Jechoniah', cluster T8
`G2424G` — 'Jesus', cluster T7
`G2446` — 'Jordan', cluster T10
`G2448` — 'Judah', cluster T11
`G2449` — 'Judea', cluster T10
`G2453` — 'Jew', cluster T11
`G2455H` — 'Judas', cluster T8
`G2455I` — 'Jude', cluster T8
`G2455N` — 'Judah', cluster T8
`G2464` — 'Isaac', cluster T8
`G2474` — 'Israel', cluster T11
`G2485` — 'little fish', cluster T13
`G2486` — 'fish', cluster T13
`G2495H` — 'Jonah', cluster T8
`G2501H` — 'Joseph', cluster T8
`G2501I` — 'Joseph', cluster T8
`G2502` — 'Josiah', cluster T8
`G2505` — 'as/just as', cluster T6
`G2511` — 'to clean', cluster M12
`G2531` — 'as/just as', cluster T6
`G2532` — 'and', cluster T6
`G2537` — 'new', cluster M45
`G2572` — 'to cover', cluster M45
`G2574` — 'camel', cluster T13
`G2579` — 'and/even if', cluster T6
`G2581` — 'Zealot', cluster M18
`G2602` — 'beginning', cluster M16
`G2606` — 'to mock', cluster M08
`G2647` — 'to destroy/lodge', cluster M55,T3
`G2665` — 'curtain', cluster T12
`G2705` — 'to kiss', cluster M05
`G2770` — 'to gain', cluster M37
`G2798` — 'branch', cluster T13
`G2807` — 'key', cluster T12
`G2823` — 'oven', cluster T12
`G2825` — 'bed', cluster T12
`G2873` — 'labor', cluster M24
`G2889` — 'world', cluster T10
`G2894` — 'basket', cluster T12
`G2898` — 'Skull', cluster T14
`G2928` — 'to hide', cluster M20
`G2948` — 'crippled', cluster M73
`G2952` — 'little dog', cluster T13
`G2962G` — 'lord: God', cluster T7
`G2962H` — 'lord: master', cluster M72
`G2971` — 'gnat', cluster T13
`G3001` — 'plant', cluster T13
`G3039` — 'to crush', cluster M10
`G3043` — 'linen/wick', cluster T12
`G3074` — 'wolf', cluster T13
`G3087` — 'lampstand', cluster T12
`G3088` — 'lamp', cluster T12
`G3101` — 'disciple', cluster T8
`G3162` — 'sword', cluster T12
`G3332` — 'to leave', cluster M59
`G3361` — 'not', cluster T5
`G3362` — 'unless', cluster T6
`G3363` — 'lest/so that... not', cluster T6
`G3366` — 'nor', cluster T5
`G3379` — 'lest', cluster T6
`G3383` — 'neither', cluster T5
`G3385` — 'surely not', cluster T6
`G3423` — 'to betroth', cluster M44
`G3428` — 'adulterous', cluster M57
`G3429` — 'to commit adultery', cluster M57
`G3458` — 'millstone', cluster T12
`G3475` — 'Moses', cluster T8
`G3501` — 'new', cluster M45
`G3507` — 'cloud', cluster T13
`G3508` — 'Naphtali', cluster T8
`G3523` — 'fasting', cluster M21
`G3536` — 'Ninevite', cluster T11
`G3551` — 'law', cluster M54
`G3554` — 'illness', cluster M73
`G3558H` — '(Queen of) the South', cluster T8
`G3575` — 'Noah', cluster T8
`G3599` — 'tooth', cluster T14
`G3606` — 'whence', cluster T6
`G3684` — 'huge millstone', cluster T12
`G3699` — 'where(-ever)', cluster T6
`G3704` — 'that', cluster T6
`G3751` — 'loins', cluster T14
`G3752` — 'when(-ever)', cluster T6
`G3753` — 'when', cluster T6
`G3754G` — 'that/since: that', cluster T6
`G3754H` — 'that/since: since', cluster T6
`G3756` — 'no', cluster T5
`G3759` — 'woe!', cluster M03
`G3761` — 'nor', cluster T5
`G3765` — 'not any more', cluster T5
`G3767` — 'therefore/then', cluster T6
`G3768` — 'not yet', cluster T5
`G3772` — 'heaven', cluster T10
`G3774` — 'Uriah', cluster T8
`G3777` — 'neither', cluster T5
`G3780` — 'not!', cluster T5
`G3793` — 'crowd', cluster T11
`G3844` — 'from/with/beside', cluster FLAG,T2
`G3953` — 'dish', cluster T12
`G3957` — 'Passover lamb', cluster T13
`G3985G` — 'to test/tempt: tempt', cluster M35
`G3985H` — 'to test/tempt: test', cluster M35
`G4058` — 'dove', cluster T13
`G4071` — 'bird', cluster T13
`G4082` — 'bag', cluster T12
`G4090` — 'bitterly', cluster M03
`G4133` — 'but/however', cluster T6
`G4143` — 'boat', cluster T12
`G4145` — 'rich', cluster M46
`G4172` — 'city', cluster T11
`G4221` — 'cup', cluster T12
`G4263` — 'sheep', cluster T13
`G4328` — 'to look for', cluster M68
`G4396` — 'prophet', cluster M43
`G4416` — 'firstborn', cluster M37
`G4464` — 'rod', cluster T12
`G4471` — 'Ramah', cluster T10
`G4476` — 'needle', cluster T12
`G4478` — 'Rachel', cluster T8
`G4491` — 'root', cluster T13
`G4536` — 'trumpet', cluster T12
`G4541` — 'Samaritan', cluster T10
`G4567` — 'Satan', cluster T4
`G4582` — 'moon', cluster T13
`G4597` — 'moth', cluster T13
`G4600` — 'cheek', cluster T14
`G4605` — 'Sidon', cluster T10
`G4622` — 'Zion', cluster T10
`G4624` — 'to cause to stumble', cluster M77
`G4670` — 'Sodom', cluster T10
`G4672G` — 'Solomon', cluster T8
`G4690H` — 'seed(s)', cluster T13
`G4711` — 'basket', cluster T12
`G4715` — 'coin', cluster T12
`G4765` — 'sparrow', cluster T13
`G4816` — 'to collect', cluster M16
`G4862` — 'with', cluster FLAG,T2
`G4889` — 'fellow slave', cluster M78
`G4947` — 'Syria', cluster T11
`G4983` — 'body', cluster T14
`G5022` — 'bull', cluster T13
`G5037` — 'and/both', cluster T6
`G5083H` — 'to keep: guard', cluster M74
`G5091` — 'to honor', cluster M71
`G5092` — 'honor', cluster M71
`G5117` — 'place', cluster T10
`G5132` — 'table', cluster T12
`G5146` — 'thistle', cluster T13
`G5184` — 'Tyre', cluster T10
`G5263` — 'to show', cluster M05
`G5266` — 'sandal', cluster T12
`G5273` — 'hypocrite', cluster M14
`G5308` — 'high', cluster M08
`G5310` — 'Highest', cluster T7
`G5384` — 'friendly/friend', cluster M05
`G5413` — 'burden', cluster M78
`G5444` — 'leaf', cluster T13
`G5451` — 'plant', cluster T13
`G5456H` — 'voice/sound: noise', cluster M84
`G5478` — 'Canaanite', cluster T11
`G5495` — 'hand', cluster T14
`G5510` — 'snow', cluster T13
`G5528` — 'grass', cluster T13
`G5549` — 'to delay', cluster M09
`G5578` — 'false prophet', cluster M14
`G5580` — 'false Christ', cluster M14
`G5606` — 'shoulder', cluster T14
`G5613` — 'as/when', cluster T6
`G5618` — 'just as', cluster T6
`G5620` — 'so', cluster T6
`G5623` — 'to help', cluster M45
`G0008` — 'Abiathar', cluster T8
`G0216` — 'mute', cluster M53
`G0254` — 'chain', cluster T12
`G0657` — 'to leave', cluster M59
`G0759` — 'spices', cluster T12
`G0942` — 'thorn bush', cluster T13
`G0950` — 'to confirm', cluster M62
`G0984` — 'to hurt', cluster M24
`G1027` — 'thunder', cluster T13
`G1119` — 'a knee', cluster T14
`G1199` — 'chain', cluster T12
`G1407` — 'sickle', cluster T12
`G1606` — 'to expire', cluster M24
`G1758` — 'to oppose', cluster M06
`G1899` — 'then', cluster T6
`G2415` — 'Jerusalem', cluster T10
`G2512` — 'cleansing', cluster M12
`G2765` — 'clay jar', cluster T12
`G2895` — 'bed', cluster T12
`G2969` — 'village', cluster T10
`G2978` — 'storm', cluster T13
`G3016` — 'coin', cluster T12
`G3017I` — 'Levi', cluster T8
`G3457` — 'millstone', cluster T12
`G3582` — 'pitcher', cluster T12
`G3619` — 'building', cluster M52
`G4028` — 'to cover', cluster M45
`G4142` — 'small boat', cluster T12
`G4319` — 'to beg', cluster M21
`G4327` — 'to wait for/welcome', cluster M68
`G4547` — 'sandal', cluster T12
`G4663` — 'worm', cluster T13
`G4746` — 'leafy branch', cluster T13
`G4949` — 'Syrophoenician', cluster T11
`G5141` — 'to tremble', cluster M01
`G5290` — 'to return', cluster M11
`G5475` — 'copper/bronze/coin', cluster T12
`G0002` — 'Aaron', cluster T8
`G0007H` — 'Abijah', cluster T8
`G0012` — 'abyss', cluster T10
`G0075` — 'to struggle', cluster M34
`G0076` — 'Adam', cluster T8
`G0364` — 'remembrance', cluster M82
`G0376` — 'crippled', cluster M73
`G0459` — 'lawless', cluster M75
`G0467` — 'to repay', cluster M26
`G0474` — 'to discuss', cluster M63
`G0482` — 'to help', cluster M45
`G0488` — 'to return', cluster M11
`G0525` — 'to release', cluster M59
`G0612` — 'answer', cluster M42
`G0613` — 'to conceal', cluster M14
`G0620` — 'to leave', cluster M59
`G0723` — 'plow', cluster T12
`G0768` — 'Asher', cluster T8
`G0840` — 'severe', cluster M24
`G0868` — 'to leave', cluster M59
`G0905` — 'purse', cluster T12
`G0933` — 'palace', cluster M72
`G1000` — 'throwing', cluster M24
`G1016` — 'ox', cluster T13
`G1070` — 'to laugh', cluster M04
`G1146` — 'ring', cluster T12
`G1248` — 'service', cluster M36
`G1255` — 'to discuss', cluster M63
`G1298` — 'to trouble', cluster M03
`G1301` — 'to keep', cluster M74
`G1329` — 'to interpret', cluster M63
`G1360` — 'because', cluster T6
`G1399` — 'female slave', cluster M78
`G1666` — 'Elisha', cluster T8
`G1800` — 'Enos', cluster T8
`G1834` — 'to tell', cluster M65
`G1880` — 'to return', cluster M11
`G1895` — 'since', cluster T6
`G1948` — 'to decide', cluster M63
`G2197H` — 'Zechariah', cluster T8
`G2201` — 'a yoke/pair', cluster T12
`G2208` — 'Zealot', cluster M18
`G2230` — 'to govern', cluster M72
`G2352` — 'to crush', cluster M10
`G2368` — 'incense', cluster T12
`G2407` — 'to serve as priest', cluster M36
`G2455G` — 'Judas', cluster T8
`G2530` — 'as/just as', cluster T6
`G2766` — 'clay roof tile', cluster T13
`G2800` — 'breaking', cluster M24
`G2826` — 'bed', cluster T12
`G2845` — 'bed', cluster T12
`G2876` — 'raven', cluster T13
`G2901` — 'to strengthen', cluster M23
`G3019` — 'Levite', cluster T8
`G3091` — 'Lot', cluster T8
`G3167` — 'mighty', cluster M23
`G3168` — 'majesty', cluster M08
`G3312` — 'arbiter', cluster M15
`G3330` — 'to share', cluster M44
`G3448` — 'calf', cluster T13
`G3497` — 'Naaman', cluster T8
`G3521` — 'fasting', cluster M21
`G3528` — 'to conquer', cluster M23
`G3610` — 'slave', cluster M78
`G3681` — 'disgrace', cluster M07
`G3698` — 'when(-ever)', cluster T6
`G3790` — 'brow', cluster T14
`G3871` — 'to hide', cluster M20
`G4032` — 'to hide', cluster M20
`G4218` — 'once/when', cluster T6
`G4273` — 'traitor', cluster M14
`G4422` — 'to frighten', cluster M01
`G4485` — 'destruction', cluster M55
`G4540` — 'Samaria', cluster T10
`G4589` — 'Seth', cluster T8
`G4611` — 'Siloam', cluster T10
`G4617` — 'to sift', cluster M77
`G4648` — 'to watch out', cluster M74
`G4651` — 'scorpion', cluster T13
`G4661` — 'plunder', cluster M24
`G4738` — 'chest', cluster T14
`G4780` — 'to conceal', cluster M14
`G4788` — 'to confine', cluster M23
`G4878` — 'to help', cluster M45
`G4884` — 'to seize', cluster M24
`G4948` — 'Syrian', cluster T11
`G4990` — 'savior', cluster M79
`G5050` — 'perfection', cluster M61
`G5106` — 'then', cluster T6
`G5135` — 'to wound', cluster M10
`G5167` — 'dove', cluster T13
`G5172` — 'self-indulgence', cluster M28
`G5271` — 'to pretend', cluster M14
`G5311` — 'height', cluster M08
`G5327` — 'valley', cluster T10
`G5345` — 'news', cluster M82
`G5370` — 'kiss', cluster M05
`G5442H` — 'to keep/guard: guard', cluster M74
`G5442I` — 'to keep/guard: protect', cluster M74
`G0286` — 'lamb', cluster T13
`G0721` — 'lamb', cluster T13
`G0755` — 'head waiter', cluster T8
`G0937` — 'royal', cluster M72
`G1431` — 'free gift', cluster M39
`G1903` — 'coat', cluster T12
`G2059` — 'to interpret', cluster M63
`G2187` — 'Ephraim', cluster T8
`G2227` — 'to make alive', cluster M25
`G2260` — 'than', cluster T6
`G2475` — 'Israelite', cluster T8
`G2501N` — 'Joseph', cluster T8
`G2544` — 'and yet/although', cluster T6
`G2580` — 'Cana', cluster T10
`G2748` — 'Kidron', cluster T10
`G2772` — 'coin', cluster T12
`G2814` — 'branch', cluster T13
`G3057` — 'spear', cluster T12
`G3105` — 'to rave', cluster M66
`G3305` — 'yet', cluster T6
`G3378` — "isn't it?", cluster T6
`G3537` — 'wash basin', cluster T12
`G3676` — 'just as', cluster T6
`G3696` — 'weapon', cluster T12
`G3766` — 'so', cluster T6
`G3795` — 'fish', cluster T13
`G3942` — 'proverb', cluster M35
`G4081` — 'clay', cluster T13
`G4262` — 'Sheep Gate', cluster T10
`G4371` — 'fish', cluster T13
`G4418` — 'heel', cluster T14
`G4542` — 'Samaria', cluster T10
`G4628` — 'leg', cluster T14
`G4827` — 'fellow disciple', cluster T8
`G4979` — 'rope', cluster T12
`G5083I` — 'to keep: protect', cluster M74
`G5201` — 'jar', cluster T12
`H5207` — 'soothing', cluster M04
`G0049` — 'purification', cluster M61
`G0052` — 'ignorance', cluster M63
`G0124` — 'Egyptian', cluster T11
`G0128` — 'Ethiopian', cluster T8
`G0157` — 'charge', cluster M26
`G0178` — 'uncondemned', cluster M61
`G0236` — 'to change', cluster M45
`G0295` — 'Amphipolis', cluster T8
`G0333` — 'to contemplate', cluster M15
`G0374` — 'to persuade', cluster M77
`G0442` — 'human', cluster T8
`G0677` — 'not stumbling', cluster M77
`G0690` — 'Arabian', cluster T10
`G0693` — 'silver', cluster T12
`G0716` — 'chariot', cluster T12
`G0777` — 'fasting', cluster M21
`G0778` — 'to strive', cluster M34
`G0780` — 'gladly', cluster M04
`G0958` — 'Benjamin', cluster T8
`G0970` — 'force', cluster M23
`G1041` — 'altar', cluster T12
`G1048` — 'Gaza', cluster T10
`G1154` — 'Damascus', cluster T10
`G1175` — 'religion', cluster M31
`G1231` — 'to decide', cluster M63
`G1429` — 'twelve tribes', cluster T11
`G1494` — 'sacrificed to idols', cluster M55
`G1497` — 'idol', cluster M55,T12
`G1551` — 'to wait for', cluster M68
`G1634` — 'to expire', cluster M24
`G1671` — 'Greece', cluster T10
`G1675` — 'Hellenist', cluster T11
`G1697` — 'Hamor', cluster T8
`G1813` — 'to blot out', cluster M60
`G1917` — 'plot', cluster M06
`G1962` — 'to accept', cluster M39
`G1991` — 'to strengthen', cluster M23
`G2016` — 'glorious', cluster M71
`G2026` — 'to build up/upon', cluster M52
`G2148` — 'a north wind', cluster T13
`G2152` — 'pious', cluster M05
`G2207` — 'zealot', cluster M18
`G2424I` — 'Joshua', cluster T8
`G2445` — 'Joppa', cluster T10
`G2455K` — 'Judas', cluster T8
`G2455L` — 'Judas', cluster T8
`G2455M` — 'Judas', cluster T8
`G2493` — 'Joel', cluster T8
`G2501M` — 'Joseph', cluster T8
`G2534` — 'even/even though', cluster T6
`G2547` — 'and from there', cluster T6
`G2663` — 'rest', cluster M33
`G2687` — 'to quiet', cluster M33
`G2797` — 'Kish', cluster T8
`G2880` — 'to satisfy', cluster M45
`G2912` — 'Cretan', cluster T11
`G2914` — 'Crete', cluster T10
`G2953` — 'Cyprus', cluster T11
`G2954` — 'Cyprus', cluster T11
`G3069` — 'Lydda', cluster T10
`G3099` — 'Midian', cluster T10
`G3102` — 'disciple', cluster T8
`G3116` — 'patiently', cluster M34
`G3143` — 'to testify', cluster M35
`G3318` — 'Mesopotamia', cluster T10
`G3343` — 'to summon', cluster M37
`G3344` — 'to change', cluster M45
`G3365` — 'surely not', cluster T6
`G3381` — 'so that', cluster T6
`G3491` — 'ship', cluster T12
`G3635` — 'to delay', cluster M09
`G3905` — 'to prolong', cluster M25
`G3926` — 'to trouble', cluster M03
`G3985I` — 'to test/tempt: try', cluster M35
`G3987` — 'to try', cluster M77
`G4037` — 'to await', cluster M68
`G4157` — 'wind/breath', cluster T13
`G4268` — 'foreknowledge', cluster M37
`G4288` — 'eagerness', cluster M18
`G4307` — 'foresight', cluster M43
`G4312` — 'reckless', cluster M66
`G4361` — 'very hungry', cluster M18
`G4384` — 'to predetermine', cluster M37
`G4389` — 'to encourage', cluster M52
`G4401` — 'to choose', cluster M64
`G4424` — 'Ptolemais', cluster T10
`G4467` — 'crime', cluster M55
`G4545` — 'Samuel', cluster T8
`G4549H` — 'Saul', cluster T8
`G4602` — 'silence', cluster M33
`G4603` — 'iron', cluster T12
`G4606` — 'Sidonian', cluster T11
`G4614` — '(Mount) Sinai', cluster T10
`G4662` — 'worm-eated', cluster T13
`G4672H` — "Solomon's [Portico]", cluster T8
`G4826I` — 'Simeon', cluster T8
`G4826K` — 'Simeon', cluster T8
`G4945` — 'plot', cluster M06
`G4966` — 'Shechem', cluster T10
`G4974` — 'ankle', cluster T14
`G5093` — 'precious', cluster M18
`G5104` — 'certainly', cluster T6
`G5183` — 'Tyre', cluster T10
`G5205` — 'rain', cluster T13
`G5334` — 'news', cluster M82
`G5339` — 'to spare', cluster M05
`G5466` — 'Chaldean', cluster T11
`G5477` — 'Canaan', cluster T10
`G5488` — 'Haran', cluster T10
`G5559` — 'skin', cluster T14
`G5564H` — 'Field (of Blood)', cluster T10
`G5571` — 'false', cluster M14
`G6048` — 'judgment', cluster M26
`G0463` — 'tolerance', cluster M05
`G0663` — 'severity', cluster M06
`G0765` — 'ungodly', cluster M58
`G0785` — 'asp', cluster T13
`G0802` — 'untrustworthy', cluster M14
`G0949` — 'firm', cluster M23
`G1384` — 'tested', cluster M35
`G1434` — 'free gift', cluster M39
`G1558` — 'avenging', cluster M26
`G1731` — 'to show', cluster M05
`G1738` — 'just', cluster M12
`G1878` — 'to remind', cluster M82
`G1943` — 'to cover', cluster M45
`G2269H` — 'Esau', cluster T11
`G2509` — 'just as', cluster T6
`G2526` — 'insofar as', cluster T6
`G2644` — 'to reconcile', cluster M05
`G2995` — 'throat', cluster T14
`G3304` — 'rather', cluster T6
`G3380` — 'not yet', cluster T5
`G4152` — 'spiritual', cluster M47
`G4306` — 'to care for', cluster M05
`G4348` — 'stumbling block', cluster M77
`G4356` — 'acceptance', cluster M18
`G4417` — 'to stumble', cluster M77
`G4479` — 'Rebekah', cluster T8
`G4519` — 'hosts', cluster M72
`G4564` — 'Sarah', cluster T8
`G4825` — 'counselor', cluster M16
`G4832` — 'conformed', cluster M45
`G4837` — 'to encourage', cluster M52
`G4852` — 'to agree', cluster M44
`G4865` — 'to struggle', cluster M34
`G4888` — 'to glory with', cluster M71
`G4973` — 'seal', cluster T12
`G5245` — 'to conquer', cluster M23
`G5267` — 'accountable', cluster M26
`G5275` — 'to leave', cluster M59
`G5313` — 'height', cluster M08
`G5381` — 'hospitality', cluster M05
`G5542` — 'smooth talk', cluster M65
`G5617` — 'Hosea', cluster T8
`G1328` — 'interpreter', cluster M63
`G1355` — 'for', cluster T6
`G1396` — 'to enslave', cluster M78
`G1493` — "idol's temple", cluster T10
`G1496` — 'idolater', cluster M55,T8
`G1652` — 'pitiful', cluster M05
`G1755` — 'working', cluster M23
`G2058` — 'interpretation', cluster M63
`G2619` — 'to cover', cluster M45
`G2788` — 'harp', cluster T12
`G2908` — 'greater', cluster M23
`G2950` — 'cymbal', cluster T12
`G3048` — 'collection', cluster M18
`G3348` — 'to share', cluster M44
`G3386` — 'how much more', cluster T6
`G3513` — 'as surely as', cluster T6
`G3740` — 'whenever', cluster T6
`G4148` — 'to enrich', cluster M46
`G4421` — 'bird', cluster T13
`G4821` — 'to reign with', cluster M72
`G4829` — 'to share', cluster M44
`G0718` — 'to betroth', cluster M44
`G1373` — 'thirst', cluster M18
`G1389` — 'to distort', cluster M14
`G1704` — 'to walk in/among', cluster M76
`G2096` — 'Eve', cluster T8
`G2236` — 'most gladly', cluster M04
`G2259` — 'when', cluster T6
`G2506` — 'destruction', cluster M55
`G2583` — 'rule', cluster M72
`G2676` — 'perfection', cluster M61
`G3749` — 'clay', cluster T13
`G3841` — 'almighty', cluster M23
`G4255` — 'to predetermine', cluster M37
`G4349` — 'stumbling', cluster M77
`G4553` — 'basket', cluster T12
`G4560` — 'fleshly', cluster M28
`G4647` — 'thorn', cluster T13
`G4705` — 'eager', cluster M69
`G5569` — 'false brother', cluster M14
`G0028` — 'Hagar', cluster T8
`G0688` — 'Arabia', cluster T10
`G3445` — 'to form', cluster M61
`G3456` — 'to mock', cluster M08
`G5422` — 'to deceive', cluster M14
`G0604` — 'to reconcile', cluster M05
`G0781` — 'unwise', cluster M63
`G0956` — 'arrow', cluster T12
`G2282` — 'to care for', cluster M05
`G2382` — 'breastplate', cluster T12
`G2940` — 'cunning', cluster M14
`G3809` — 'discipline', cluster M15
`G4806` — 'to make alive with', cluster M25
`G5603` — 'song', cluster M22
`G0138` — 'to choose', cluster M64
`G0951` — 'confirmation', cluster M62
`G1394` — 'gift', cluster M39
`G2539` — 'although', cluster T6
`G4426` — 'to frighten', cluster M01
`G5251` — 'to exalt', cluster M22
`G1018` — 'to rule', cluster M72
`G2404` — 'Hierapolis', cluster T8
`G2424J` — 'Jesus', cluster T8
`G3561` — 'New Moon', cluster T13
`G3884` — 'to deceive', cluster M14
`G4146` — 'richly', cluster M46
`G4733` — 'firmness', cluster M23
`G5047` — 'perfection', cluster M61
`G0743` — 'archangel', cluster T9
`G2850` — 'flattery', cluster M14
`G3642` — 'fainthearted', cluster M24
`G5105` — 'therefore', cluster T6
`G0462` — 'unholy', cluster M61
`G0594` — 'acceptance', cluster M18
`G1128` — 'to train', cluster M15
`G1226` — 'to insist', cluster M15
`G1236` — 'to live', cluster M25
`G1624` — 'to turn/wander away', cluster M11
`G1884` — 'to help', cluster M45
`G2272` — 'quiet', cluster M33
`G4751` — 'stomach', cluster T14
`G5382` — 'hospitable', cluster M05
`G0329` — 'to rekindle', cluster M45
`G0475` — 'to oppose', cluster M06
`G3023` — 'lion', cluster T13
`G5341` — 'cloak', cluster T12
`G5367` — 'selfish', cluster M08
`G5552` — 'golden', cluster T12
`G1993` — 'to silence', cluster M33
`G2451` — 'Jewish', cluster T8
`G3533` — 'Nicopolis', cluster T8
`G3711` — 'quick-tempered', cluster M02
`G4767` — 'hated', cluster M06
`G4994` — 'to train', cluster M15,T3
`G0661` — 'to repay', cluster M26
`G0464` — 'to struggle', cluster M34
`G0577` — 'to throw away', cluster M07
`G0913` — 'Barak', cluster T8
`G1066` — 'Gideon', cluster T8
`G1151` — 'heifer', cluster T13
`G1585` — 'to forget', cluster M81
`G1776` — 'to trouble', cluster M03
`G1802` — 'Enoch', cluster T8
`G2053` — 'wool', cluster T13
`G2226` — 'living thing', cluster M25
`G2269G` — 'Esau', cluster T8
`G2366` — 'storm', cluster T13
`G2369` — 'incense altar', cluster T12
`G2422` — 'Jephthah', cluster T8
`G2428` — 'supplication', cluster M42
`G2514` — 'cleanness', cluster M12
`G2535` — 'Cain', cluster T8
`G2543` — 'and yet/although', cluster T6
`G2610` — 'to conquer', cluster M23
`G2777` — 'scroll', cluster T12
`G3017J` — 'Levi', cluster T8
`G3020` — 'Levitical', cluster T8
`G3172` — 'majesty', cluster M08
`G3198` — 'Melchizedek', cluster T8
`G3375` — 'certainly', cluster T6
`G3452` — 'marrow', cluster T14
`G3509` — 'cloud', cluster T13
`G3645` — 'to destroy', cluster M10
`G3831` — 'assembly', cluster M44
`G4372` — 'new', cluster M45
`G4460` — 'Rahab', cluster T8
`G4532` — 'Salem', cluster T10
`G4546` — 'Samson', cluster T8
`G4713` — 'jar', cluster T12
`G4881` — 'to die/destroy with', cluster M25
`G5502` — 'Cherub', cluster T10
`G0087` — 'impartial', cluster M26
`G0438` — 'flower', cluster T13
`G0995` — 'outcry', cluster M84
`G1383` — 'testing', cluster M35
`G1503` — 'to resemble', cluster M15
`G1953` — 'forgetfulness', cluster M81
`G2462` — 'horse', cluster T13
`G2492` — 'Job', cluster T8
`G3797` — 'late (rain)', cluster T13
`G4406` — 'early rain', cluster T13
`G4507` — 'filth', cluster M53
`G4508` — 'filthy', cluster M53
`G4598` — 'moth-eaten', cluster T13
`G5164` — 'course/wheel', cluster T12
`G5373` — 'friendship', cluster M05
`G5425` — 'to shudder', cluster M01
`G0081` — 'brotherhood', cluster M44
`G0934` — 'kingly', cluster M72
`G0980` — 'to live', cluster M25
`G2900` — 'mighty', cluster M23
`G4509` — 'filth', cluster M53
`G4599` — 'to strengthen', cluster M23
`G5391` — 'friendly', cluster M05
`G5612` — 'to roar', cluster M84
`G0113` — 'lawless', cluster M75
`G0903` — 'Balaam', cluster T8
`G1007` — 'Beor', cluster T8
`G1955` — 'explanation', cluster M43
`G3024` — 'forgetfulness', cluster M81
`G3420` — 'remembrance', cluster M82
`G3913` — 'insanity', cluster M66
`G4577` — 'chain', cluster T12
`G4740` — 'security', cluster M19
`G4761` — 'to distort', cluster M14
`G2434` — 'propitiation', cluster M79
`G0679` — 'without falling', cluster M34
`G2879` — 'Korah', cluster T8
`G3413` — 'Michael', cluster T8,T9
`G0715` — 'bear', cluster T13
`G0717` — 'Armageddon', cluster T10
`G0904` — 'Balak', cluster T8
`G0929` — 'torment', cluster M35
`G0938G` — 'queen', cluster M72
`G0944` — 'frog', cluster T13
`G0974` — 'little scroll', cluster T12
`G1136` — 'Gog', cluster T10
`G1238` — 'diadem', cluster T12
`G1404` — 'dragon', cluster T4
`G2166` — 'Euphrates', cluster T10
`G2200` — 'hot', cluster M02
`G2403` — 'Jezebel', cluster T8
`G2764` — 'made of clay', cluster T13
`G2854` — 'eye salve', cluster T12
`G3031` — 'censer', cluster T12
`G3045` — 'rich', cluster M46
`G3382` — 'thigh', cluster T14
`G3455` — 'to roar', cluster M84
`G3732` — 'bird', cluster T13
`G3917` — 'leopard', cluster T13
`G4554` — 'Sardis', cluster T10
`G4556` — 'gem', cluster T12
`G4604` — 'iron', cluster T12
`G5464` — 'hail', cluster T13
`H0040G` — 'Abimelech', cluster T8
`H0046` — 'mighty', cluster M23
`H0067` — 'Abel-mizraim', cluster T10
`H0087` — 'Abram', cluster T8
`H0110` — 'Adbeel', cluster T8
`H0120H` — 'the man [Adam]', cluster T8
`H0123H` — 'Edom', cluster T8
`H0173` — 'Oholibamah', cluster T8
`H0201` — 'Omar', cluster T8
`H0204` — 'On', cluster T10
`H0209` — 'Onan', cluster T8
`H0218B` — 'Ur', cluster T10
`H0276` — 'Ahuzzath', cluster T8
`H0329G` — 'Atad', cluster T10
`H0345G` — 'Aiah', cluster T8
`H0356G` — 'Elon', cluster T8
`H0364` — 'El-paran', cluster T10
`H0390` — 'Accad', cluster T10
`H0410I` — 'El [Elohe]', cluster T7
`H0410J` — 'El [Most High]', cluster T7
`H0416` — 'El-bethel', cluster T10
`H0430H` — '[LORD]-Elohe', cluster T10
`H0439` — 'Allon-bacuth', cluster T10
`H0461G` — 'Eliezer', cluster T8
`H0464G` — 'Eliphaz', cluster T8
`H0495` — 'Ellasar', cluster T10
`H0518H` — 'if: surely no', cluster T6
`H0565A` — 'word', cluster M65
`H0569` — 'Amraphel', cluster T8
`H0572` — 'sack', cluster T12
`H0583` — 'Enosh', cluster T8
`H0621` — 'Asenath', cluster T8
`H0672H` — 'Ephrath', cluster T10
`H0727` — 'ark', cluster T12
`H0746A` — 'Arioch', cluster T8
`H0751` — 'Erech', cluster T10
`H0758L` — '[Paddan]-aram', cluster T10
`H0761J` — 'Aramean', cluster T11
`H0763G` — 'Mesopotamia', cluster T10
`H0775` — 'Arpachshad', cluster T8
`H0780` — 'Ararat', cluster T10
`H0805A` — 'Asshurim', cluster T11
`H0812G` — 'Eshcol', cluster T8
`H0836` — 'Asher', cluster T8
`H0882G` — 'Beeri', cluster T8
`H0883` — 'Beer-lahai-roi', cluster T10
`H0884` — 'Beersheba', cluster T10
`H0911` — 'Bedad', cluster T8
`H1004P` — 'house: palace', cluster T10
`H1067` — 'firstborn', cluster M37
`H1090A` — 'Bilhah', cluster T8
`H1106B` — 'Bela', cluster T10
`H1106G` — 'Bela', cluster T8
`H1126` — 'Ben-oni', cluster T8
`H1151` — 'Ben-ammi', cluster T8
`H1160G` — 'Beor', cluster T8
`H1177G` — 'Baal-hanan', cluster T8
`H1237K` — 'valley', cluster T10
`H1260G` — 'Bered', cluster T10
`H1298` — 'Bera', cluster T8
`H1306` — 'Birsha', cluster T8
`H1315H` — 'Basemath', cluster T8
`H1315I` — 'Basemath', cluster T8
`H1328A` — 'Bethuel', cluster T8
`H1375` — 'cup', cluster T12
`H1410G` — 'Gad', cluster T8
`H1469` — 'young bird', cluster T13
`H1514` — 'Gaham', cluster T8
`H1517` — 'sinew', cluster T14
`H1521` — 'Gihon', cluster T10
`H1567` — 'Galeed', cluster T10
`H1581` — 'camel', cluster T13
`H1609` — 'Gatam', cluster T8
`H1642` — 'Gerar', cluster T10
`H1657G` — 'Goshen', cluster T10
`H1683G` — 'Deborah', cluster T8
`H1719C` — 'Dedan', cluster T8
`H1783` — 'Dinah', cluster T8
`H1835G` — 'Dan', cluster T10
`H1835H` — 'Dan', cluster T8
`H1838` — 'Dinhabah', cluster T10
`H1877` — 'grass', cluster T13
`H1886` — 'Dothan', cluster T10
`H1893` — 'Abel', cluster T8
`H1904` — 'Hagar', cluster T8
`H1908G` — 'Hadad', cluster T8
`H1924` — 'Hadar', cluster T8
`H1967` — 'Hemam', cluster T8
`H2022H` — 'mountain: hill country', cluster T10
`H2039G` — 'Haran', cluster T8
`H2048B` — 'to deceive', cluster M14
`H2061` — 'wolf', cluster T13
`H2074` — 'Zebulun', cluster T8
`H2102` — 'to boil', cluster M08
`H2153` — 'Zilpah', cluster T8
`H2226G` — 'Zerah', cluster T8
`H2226H` — 'Zerah', cluster T8
`H2226I` — 'Zerah', cluster T8
`H2275A` — 'Hebron', cluster T10
`H2275H` — 'Hebron [Valley]', cluster T10
`H2327` — 'Hobah', cluster T10
`H2332` — 'Eve', cluster T8
`H2341G` — 'Havilah', cluster T10
`H2341J` — 'Havilah', cluster T10
`H2367` — 'Husham', cluster T8
`H2368` — 'signet', cluster T12
`H2437` — 'Hirah', cluster T8
`H2526G` — 'Ham', cluster T8
`H2538` — 'Hamul', cluster T8
`H2544` — 'Hamor', cluster T8
`H2563A` — 'clay', cluster T13
`H2585G` — 'Enoch', cluster T8
`H2585H` — 'Enoch', cluster T8
`H2671` — 'arrow', cluster T12
`H2688` — 'Hazazon-tamar', cluster T10
`H2696H` — 'Hezron', cluster T8
`H2752` — 'Horite', cluster T8
`H2753H` — 'Hori', cluster T8
`H2771A` — 'Haran', cluster T10
`H2845` — 'Heth', cluster T8
`H2850` — 'Hittite', cluster T8
`H2858` — 'ring', cluster T12
`H2875` — 'Tebah', cluster T8
`H2885` — 'ring', cluster T12
`H2934` — 'to hide', cluster M20
`H2975G` — 'Nile', cluster T10
`H2989` — 'Jabal', cluster T8
`H2999` — 'Jabbok', cluster T10
`H3026A` — 'Jegar', cluster T10
`H3026B` — '[Jegar]-sahadutha', cluster T10
`H3067` — 'Judith', cluster T8
`H3103H` — 'Jobab', cluster T8
`H3106` — 'Jubal', cluster T8
`H3252` — 'Iscah', cluster T8
`H3266G` — 'Jeush', cluster T8
`H3281` — 'Jalam', cluster T8
`H3315` — 'Japheth', cluster T8
`H3326A` — 'bed', cluster T12
`H3327` — 'Isaac', cluster T8
`H3355` — 'Joktan', cluster T8
`H3370` — 'Jokshan', cluster T8
`H3382G` — 'Jared', cluster T8
`H3383` — 'Jordan', cluster T10
`H3409` — 'thigh', cluster T14
`H3458G` — 'Ishmael', cluster T8
`H3459` — 'Ishmaelite', cluster T8
`H3485G` — 'Issachar', cluster T8
`H3509` — 'Jetheth', cluster T8
`H3513J` — 'to honor: dull', cluster M16,T3
`H3535` — 'ewe-lamb', cluster T13
`H3536` — 'kiln', cluster T12
`H3537` — 'jar', cluster T12
`H3540` — 'Chedorlaomer', cluster T8
`H3563A` — 'cup', cluster T12
`H3568A` — 'Cush', cluster T10
`H3568G` — 'Cush', cluster T8
`H3580` — 'Chezib', cluster T10
`H3588C` — 'for as that: since', cluster T6
`H3625` — 'Calah', cluster T10
`H3641A` — 'Calneh', cluster T10
`H3658` — 'lyre', cluster T12
`H3667A` — 'Canaan', cluster T10
`H3667G` — 'Canaan', cluster T8
`H3695` — 'Casluhim', cluster T11
`H3722B` — 'to cover', cluster M45
`H3742` — 'cherub', cluster T9
`H3775` — 'sheep', cluster T13
`H3812` — 'Leah', cluster T8
`H3817` — 'Leummim', cluster T11
`H3837A` — 'Laban', cluster T8
`H3870H` — 'Luz', cluster T10
`H3876G` — 'Lot', cluster T8
`H3877` — 'Lotan', cluster T8
`H3878` — 'Levi', cluster T8
`H3884` — 'unless', cluster T6
`H3912` — 'Letushim', cluster T11
`H3929G` — 'Lamech', cluster T8
`H3929H` — 'Lamech', cluster T8
`H3962` — 'Lasha', cluster T10
`H3979` — 'knife', cluster T12
`H4017G` — 'Mibsam', cluster T8
`H4030` — 'precious thing', cluster M28
`H4080H` — 'Midian', cluster T10
`H4084` — 'Midianite', cluster T11
`H4092` — 'Midianite', cluster T11
`H4105G` — 'Mehetabel', cluster T8
`H4111G` — 'Mahalalel', cluster T8
`H4124H` — 'Moab', cluster T8
`H4176G` — 'Moreh', cluster T10
`H4179` — '[Mount] Moriah', cluster T10
`H4199` — 'Mizzah', cluster T8
`H4241` — 'recovery', cluster M25
`H4258G` — 'Mahalath', cluster T8
`H4266` — 'Mahanaim', cluster T10
`H4308G` — 'Matred', cluster T8
`H4314` — 'Mezahab', cluster T8
`H4353G` — 'Machir', cluster T8
`H4375` — 'Machpelah', cluster T10
`H4397G` — 'messenger', cluster T9
`H4417G` — 'Salt [Sea]', cluster T10
`H4435G` — 'Milcah', cluster T8
`H4471G` — 'Mamre', cluster T10
`H4471H` — 'Mamre', cluster T8
`H4519G` — 'Manasseh', cluster T8
`H4569A` — 'ford', cluster T11
`H4601G` — 'Maacah', cluster T8
`H4713` — 'Egyptian', cluster T10
`H4852` — 'Mesha', cluster T10
`H4957` — 'Masrekah', cluster T10
`H4968` — 'Methuselah', cluster T8
`H4976` — 'gift', cluster M39
`H4979` — 'gift', cluster M39
`H5032` — 'Nebaioth', cluster T8
`H5113` — 'Nod', cluster T10
`H5146` — 'Noah', cluster T8
`H5152G` — 'Nahor', cluster T8
`H5152H` — 'Nahor', cluster T8
`H5158N` — 'torrent: valley', cluster T10
`H5184G` — 'Nahath', cluster T8
`H5219` — 'tragacanth gum', cluster T13
`H5321G` — 'Naphtali', cluster T8
`H5387A` — 'leader', cluster M72
`H5467` — 'Sodom', cluster T10
`H5523G` — 'Succoth', cluster T10
`H5536` — 'basket', cluster T12
`H5611` — 'Sephar', cluster T10
`H5657` — 'service', cluster M36
`H5676H` — 'side: beyond', cluster T10
`H5677G` — 'Eber', cluster T8
`H5711G` — 'Adah', cluster T8
`H5711H` — 'Adah', cluster T8
`H5726` — 'Adullamite', cluster T11
`H5748` — 'pipe', cluster T12
`H5762` — 'Avith', cluster T10
`H5857G` — 'Ai', cluster T10
`H5869M` — 'spring', cluster T10
`H5879G` — 'Enaim', cluster T10
`H5880` — 'En-mishpat', cluster T10
`H5893H` — '[Rehoboth]-Ir  ', cluster T10
`H5907G` — 'Achbor', cluster T8
`H5929` — 'leaf', cluster T13
`H5933` — 'Alvah', cluster T8
`H5945A` — 'high', cluster M08
`H5945H` — '[LORD] Most High', cluster T7
`H6002H` — 'Amalek', cluster T8
`H6003` — 'Amalekite', cluster T11
`H6010K` — 'Valley [of Hebron]', cluster T10
`H6010O` — 'Valley [of Kings]', cluster T10
`H6010Q` — 'Valley [of Siddim]', cluster T10
`H6017` — 'Gomorrah', cluster T10
`H6034` — 'Anah', cluster T8
`H6063G` — 'Aner', cluster T8
`H6085G` — 'Ephron', cluster T8
`H6119` — 'heel', cluster T14
`H6147G` — 'Er', cluster T8
`H6158` — 'raven', cluster T13
`H6215G` — 'Esau', cluster T8
`H6230` — 'Esek', cluster T10
`H6290G` — 'Paran', cluster T10
`H6307` — 'Paddan', cluster T10
`H6310K` — 'lip: according', cluster T14
`H6318` — 'Potiphar', cluster T8
`H6319` — 'Potiphera', cluster T8
`H6349` — 'recklessness', cluster M66
`H6369` — 'Phicol', cluster T8
`H6376` — 'Pishon', cluster T10
`H6389` — 'Peleg', cluster T8
`H6430H` — 'Philistine', cluster T11
`H6439G` — 'Peniel', cluster T10
`H6464` — 'Pau', cluster T10
`H6547G` — 'Pharaoh', cluster T8
`H6547H` — 'Pharaoh', cluster T8
`H6557` — 'Perez', cluster T8
`H6578` — 'Euphrates', cluster T10
`H6616` — 'cord', cluster M03,T12
`H6617` — 'to twist', cluster M57
`H6622` — 'to interpret', cluster M63
`H6625` — 'Pathrusim', cluster T11
`H6649` — 'Zibeon', cluster T8
`H6711` — 'to laugh', cluster M04
`H6714G` — 'Zohar', cluster T8
`H6741` — 'Zillah', cluster T8
`H6781A` — 'bracelet', cluster T12
`H6820` — 'Zoar', cluster T10
`H6825` — 'Zepho', cluster T8
`H6847` — 'Zaphenath-paneah', cluster T8
`H6938` — 'Kedar', cluster T8
`H6946G` — 'Kadesh', cluster T10
`H6967` — 'height', cluster M08
`H6989` — 'Keturah', cluster T8
`H7014B` — 'Cain', cluster T8
`H7018` — 'Kenan', cluster T8
`H7070H` — 'branch: stem', cluster T13
`H7073G` — 'Kenaz', cluster T8
`H7122G` — 'to encounter: meet', cluster M37
`H7122I` — 'to encounter: chanced', cluster M37
`H7141G` — 'Korah', cluster T8
`H7153` — 'Kiriath-arba', cluster T10
`H7192` — 'coin', cluster T12
`H7200N` — 'Provider [God]', cluster T7
`H7205` — 'Reuben', cluster T8
`H7208` — 'Reumah', cluster T8
`H7218J` — 'head: first', cluster T14
`H7242` — 'necklace', cluster T12
`H7259` — 'Rebekah', cluster T8
`H7344G` — 'Rehoboth', cluster T10
`H7344H` — 'Rehoboth', cluster T10
`H7344I` — 'Rehoboth', cluster T10
`H7354` — 'Rachel', cluster T8
`H7411B` — 'to deceive', cluster M14
`H7449` — 'Resen', cluster T10
`H7466` — 'Reu', cluster T8
`H7467G` — 'Reuel', cluster T8
`H7486G` — 'Rameses', cluster T10
`H7586I` — 'Shaul', cluster T8
`H7614I` — 'Sheba', cluster T8
`H7656` — 'Shibah', cluster T10
`H7704A` — 'Sirion', cluster T10
`H7706` — 'Almighty [God]', cluster T7
`H7708` — 'Valley', cluster T10
`H7716` — 'sheep', cluster T13
`H7732G` — 'Shobal', cluster T8
`H7740` — 'Shaveh', cluster T10
`H7770` — 'Shua', cluster T8
`H7793` — 'Shur', cluster T10
`H7856` — 'Sitnah', cluster T10
`H7892A` — 'song', cluster M22
`H7926` — 'shoulder', cluster T14
`H7927H` — 'Shechem', cluster T8
`H7956` — 'Shelah', cluster T8
`H7974` — 'Shelah', cluster T8
`H8035` — 'Shem', cluster T8
`H8038` — 'Shemeber', cluster T8
`H8048G` — 'Shammah', cluster T8
`H8072` — 'Samlah', cluster T8
`H8082` — 'rich', cluster M46
`H8095G` — 'Simeon', cluster T8
`H8134` — 'Shinab', cluster T8
`H8165A` — 'Seir', cluster T10
`H8165B` — 'Seir', cluster T8
`H8193H` — 'lip: words', cluster T14
`H8207` — 'horned viper', cluster T13
`H8255` — 'shekel', cluster T12
`H8283` — 'Sarah', cluster T8
`H8286` — 'Serug', cluster T8
`H8297` — 'Sarai', cluster T8
`H8321B` — 'vine', cluster T13
`H8352` — 'Seth', cluster T8
`H8413` — 'Tidal', cluster T8
`H8477` — 'Tahash', cluster T8
`H8487G` — 'Teman', cluster T8
`H8489` — 'Temanite', cluster T11
`H8495` — 'male goat', cluster T13
`H8553G` — 'Timnah', cluster T10
`H8555` — 'Timna', cluster T8
`H8559G` — 'Tamar', cluster T8
`H8646G` — 'Terah', cluster T8
`H0030` — 'Abihu', cluster T8
`H0070` — 'wheel', cluster T12
`H0073` — 'girdle', cluster T12
`H0171` — 'Oholiab', cluster T8
`H0212` — 'wheel', cluster T12
`H0221G` — 'Uri', cluster T8
`H0294` — 'Ahisamach', cluster T8
`H0362` — 'Elim', cluster T10
`H0385` — 'Ithamar', cluster T8
`H0461H` — 'Eliezer', cluster T8
`H0483` — 'mute', cluster M53
`H0642` — 'ephod', cluster T12
`H0676` — 'finger', cluster T14
`H0802I` — 'woman: another', cluster T8
`H0931` — 'thumb/big toe', cluster T14
`H1189` — 'Baal-zephon', cluster T10
`H1212G` — 'Bezalel', cluster T8
`H1259` — 'hail', cluster T13
`H1304A` — 'gem', cluster T12
`H1314` — 'spice', cluster T12
`H1342` — 'to rise up', cluster M08
`H1647G` — 'Gershom', cluster T8
`H1648` — 'Gershon', cluster T8
`H1826A` — 'to silence: stationary', cluster M33
`H1921` — 'to honor', cluster M71
`H2053` — 'hook', cluster T12
`H2098` — 'this', cluster T6
`H2176` — 'song', cluster M22
`H2287` — 'to celebrate', cluster M71
`H2319H` — 'new', cluster M45
`H2354G` — 'Hur', cluster T8
`H2390` — 'stronger', cluster M23
`H2397` — 'hook', cluster T12
`H2422` — 'vigorous', cluster M25
`H2436H` — 'bosom: garment', cluster T12
`H2722` — 'Horeb', cluster T10
`H2750` — 'burning', cluster M02
`H2803G` — 'to devise: design', cluster M64
`H2838` — 'ring', cluster T12
`H2983G` — 'Jebusite', cluster T10
`H3091G` — 'Joshua', cluster T8
`H3407` — 'curtain', cluster T12
`H3500L` — 'Jethro', cluster T8
`H3503` — 'Jethro', cluster T8
`H3517` — 'heaviness', cluster FLAG,T2
`H3558` — 'bracelet', cluster T12
`H3595` — 'basin', cluster T12
`H3654` — 'gnat', cluster T13
`H3725` — 'atonement', cluster M60
`H3802` — 'shoulder', cluster T14
`H3881` — 'Levi', cluster T11
`H4020` — 'twisted', cluster M14
`H4024B` — 'Migdol', cluster T10
`H4289` — 'censer', cluster T12
`H4290` — 'breaking', cluster M24
`H4306` — 'rain', cluster T13
`H4340` — 'cord', cluster M03,T12
`H4501` — 'lampstand', cluster T12
`H4532` — 'Massah', cluster T10
`H4744` — 'assembly', cluster M44
`H4785` — 'Marah', cluster T10
`H4809G` — 'Meribah', cluster M02,T10
`H4847` — 'Merari', cluster T8
`H4938B` — 'staff', cluster T12
`H5070G` — 'Nadab', cluster T8
`H5126` — 'Nun', cluster T8
`H5198B` — 'gum', cluster T14
`H5216A` — 'lamp', cluster T12
`H5251G` — 'Banner [God]', cluster T10
`H5327A` — 'to struggle', cluster M34
`H5514G` — 'Sinai', cluster T10
`H5514H` — '[Wilderness of] Sinai', cluster T10
`H5526B` — 'to cover', cluster M45
`H5526E` — 'to cover', cluster M45
`H5561` — 'spice', cluster T12
`H5592A` — 'basin', cluster T12
`H5645` — 'cloud', cluster T13
`H5676G` — 'side: beside', cluster T10
`H6002G` — 'Amalek', cluster T10
`H6030C` — 'to sing', cluster M22
`H6154M` — 'racial-mix', cluster T11
`H6310H` — 'lip: edge', cluster T14
`H6310J` — 'lip: opening', cluster T14
`H6326` — 'Puah', cluster T8
`H6341B` — 'plate', cluster T12
`H6363A` — 'firstborn', cluster M37
`H6367` — 'Pi-hahiroth', cluster T10
`H6430I` — '[Sea of the] Philistines', cluster T10
`H6438H` — 'corner', cluster T10
`H6525` — 'flower', cluster T13
`H6531` — 'severity', cluster M06
`H6532` — 'curtain', cluster T12
`H6547I` — 'Pharaoh', cluster T8
`H6547J` — 'Pharaoh', cluster T8
`H6569` — 'refuse', cluster M30
`H6619` — 'Pithom', cluster T10
`H6696C` — 'to form', cluster M61
`H6731A` — 'flower', cluster T13
`H6803` — 'jar', cluster T12
`H6854` — 'frog', cluster T13
`H6855` — 'Zipporah', cluster T8
`H6955` — 'Kohath', cluster T8
`H7004` — 'incense', cluster T12
`H7050B` — 'curtain', cluster T12
`H7067H` — 'jealous', cluster M18
`H7070G` — 'branch', cluster T13
`H7086` — 'dish', cluster T12
`H7218L` — 'head: count', cluster T14
`H7347` — 'millstone', cluster T12
`H7415` — 'worm', cluster T13
`H7461A` — 'trembling', cluster M01
`H7467J` — 'Reuel', cluster T8
`H7486H` — 'Raamses', cluster T10
`H7508` — 'Rephidim', cluster T10
`H7545` — 'spice', cluster T12
`H7785` — 'leg', cluster T14
`H7806` — 'to twist', cluster M57
`H7892B` — 'song', cluster M22
`H7950` — 'snow', cluster T13
`H7958` — 'quail', cluster T13
`H8193I` — 'lip: edge', cluster T14
`H8236` — 'Shiphrah', cluster T8
`H8331` — 'chain', cluster T12
`H8333` — 'chain', cluster T12
`H8473` — 'breastplate', cluster T12
`H8513` — 'hardship', cluster M24
`H8549G` — 'unblemished', cluster M61
`H8577M` — 'serpent: snake', cluster T10
`H0469G` — 'Elizaphan', cluster T8
`H0499G` — 'Eleazar', cluster T8
`H1500` — 'violence', cluster M10
`H1704` — 'Dibri', cluster T8
`H1739` — 'sick', cluster M73
`H2206` — 'beard', cluster T14
`H2284` — 'locust', cluster T13
`H2467` — 'weasel', cluster T13
`H2546` — 'lizard', cluster T13
`H2624` — 'stork', cluster T13
`H2728` — 'locust', cluster T13
`H2893` — 'purifying', cluster M61
`H3049` — 'spiritist', cluster T4
`H3481H` — 'Israelite', cluster T8
`H3776` — 'lamb', cluster T13
`H3911` — 'lizard', cluster T13
`H4055` — 'garment', cluster T12
`H4057G` — 'Wilderness [of Sinai]', cluster T10
`H4332G` — 'Mishael', cluster T8
`H4383` — 'stumbling', cluster M77
`H4432` — 'Molech', cluster T7
`H4768` — 'greatness', cluster M71
`H4817` — 'chariot', cluster T12
`H5322B` — 'hawk', cluster T13
`H5556` — 'locust', cluster T13
`H5816G` — 'Uzziel', cluster T8
`H6057` — 'branch', cluster T13
`H6096` — 'spine', cluster T14
`H6186B` — 'to value', cluster M26
`H6632B` — 'lizard', cluster T13
`H7106A` — 'to scrape', cluster M23
`H7147` — 'hostility', cluster M06
`H7673B` — 'to keep', cluster M74
`H7829` — 'illness', cluster M73
`H8019B` — 'Shelomith', cluster T8
`H8166` — 'female goat', cluster T13
`H8464` — 'ostrich', cluster T13
`H8549I` — 'unblemished: complete', cluster M61
`H8580` — 'chameleon', cluster T13
`H0008` — 'destruction', cluster M55
`H0027` — 'Abidan', cluster T8
`H0032G` — 'Abihail', cluster T8
`H0048G` — 'Abiram', cluster T8
`H0063` — 'Abel-shittim', cluster T10
`H0088` — 'Oboth', cluster T10
`H0090G` — 'Agag', cluster T8
`H0154` — 'Edrei', cluster T10
`H0189` — 'Evi', cluster T8
`H0203` — 'On', cluster T8
`H0289G` — 'Ahiman', cluster T8
`H0295G` — 'Ahiezer', cluster T8
`H0299` — 'Ahira', cluster T8
`H0419` — 'Eldad', cluster T8
`H0442` — 'Alush', cluster T10
`H0446G` — 'Eliab', cluster T8
`H0446H` — 'Eliab', cluster T8
`H0460G` — 'Eliasaph', cluster T8
`H0468` — 'Elizur', cluster T8
`H0476G` — 'Elishama', cluster T8
`H0714G` — 'Ard', cluster T8
`H0714H` — 'Ard', cluster T8
`H0716` — 'Ardite', cluster T8
`H0769` — 'Arnon', cluster T10
`H0812H` — '[Valley of] Eshcol', cluster T10
`H0864` — 'Etham', cluster T10
`H0871` — 'Atharim', cluster T10
`H0876G` — 'Beer', cluster T10
`H0935H` — 'Lebo-[Hamath]', cluster T10
`H0957` — 'plunder', cluster M24
`H1020` — 'Beth-jeshimoth', cluster T10
`H1106A` — 'Bela', cluster T8
`H1120G` — 'Bamoth', cluster T10
`H1120H` — 'Bamoth', cluster T10
`H1186` — 'Baal-meon', cluster T10
`H1350H` — 'to redeem: avenge', cluster M79
`H1350I` — 'to redeem: relative', cluster M79
`H1441` — 'Gideoni', cluster T8
`H1442` — 'to blaspheme', cluster M58
`H1568H` — 'Gilead', cluster T8
`H1583` — 'Gamaliel', cluster T8
`H1649` — 'Gershonite', cluster T8
`H1714` — 'standard', cluster T12
`H1769G` — 'Dibon', cluster T10
`H1845` — 'Deuel', cluster T8
`H1850` — 'Dophkah', cluster T10
`H1885` — 'Dathan', cluster T8
`H1954K` — 'Hoshea', cluster T8
`H2052` — 'Waheb', cluster T10
`H2085` — 'skin', cluster T14
`H2139G` — 'Zaccur', cluster T8
`H2156` — 'branch', cluster T13
`H2174G` — 'Zimri', cluster T8
`H2202` — 'Ziphron', cluster T10
`H2246` — 'Hobab', cluster T8
`H2295` — 'Hoglah', cluster T8
`H2354H` — 'Hur', cluster T8
`H2497` — 'Helon', cluster T8
`H2539` — 'Hamulite', cluster T8
`H2574G` — 'Hamath', cluster T10
`H2660A` — 'Hepher', cluster T8
`H2692` — 'Hazar-addar', cluster T10
`H2697` — 'Hezronite', cluster T8
`H2698` — 'Hazeroth', cluster T10
`H2704` — 'Hazar-enan', cluster T10
`H2767` — 'Hormah', cluster T10
`H2809` — 'Heshbon', cluster T10
`H2971G` — 'Jair', cluster T8
`H3096` — 'Jahaz', cluster T10
`H3115` — 'Jochebed', cluster T8
`H3270G` — 'Jazer', cluster T10
`H3312G` — 'Jephunneh', cluster T8
`H3324` — 'Izhar', cluster T8
`H3405G` — 'Jericho', cluster T10
`H3452H` — 'wilderness', cluster T10
`H3579` — 'Cozbi', cluster T8
`H3612G` — 'Caleb', cluster T8
`H3645` — 'Chemosh', cluster T7
`H3672G` — '[Sea of] Chinnereth', cluster T10
`H3845G` — 'Libni', cluster T8
`H4124I` — '[Plains of] Moab', cluster T10
`H4244G` — 'Mahlah', cluster T8
`H4272` — 'to wound', cluster M10
`H4311` — 'Medeba', cluster T10
`H4312` — 'Medad', cluster T8
`H4435H` — 'Milcah', cluster T8
`H4610` — 'Akrabbim', cluster T10
`H4848` — 'Merari', cluster T8
`H4980` — 'Mattanah', cluster T10
`H5015A` — 'Nebo', cluster T10
`H5025G` — 'Nobah', cluster T8
`H5081H` — 'noble', cluster M34
`H5158H` — '[Eshcol] Valley', cluster T10
`H5158L` — 'Brook', cluster T10
`H5177` — 'Nahshon', cluster T8
`H5241G` — 'Nemuel', cluster T8
`H5270` — 'Noah', cluster T8
`H5280` — 'Naamite', cluster T8
`H5283H` — 'Naaman', cluster T8
`H5302` — 'Nophah', cluster T10
`H5417G` — 'Nethanel', cluster T8
`H5492B` — 'Suphah', cluster T10
`H5511` — 'Sihon', cluster T8
`H5543C` — 'Salu', cluster T8
`H5682` — 'Abarim', cluster T10
`H5694` — 'ring', cluster T12
`H5747` — 'Og', cluster T8
`H5863` — 'Iye-abarim', cluster T10
`H5871G` — 'Ain', cluster T10
`H5881` — 'Enan', cluster T8
`H5918` — 'Ochran', cluster T8
`H5945B` — 'Most High [God]', cluster T7
`H5989G` — 'Ammihud', cluster T8
`H5992G` — 'Amminadab', cluster T8
`H5996` — 'Ammishaddai', cluster T8
`H6019G` — 'Amram', cluster T8
`H6111` — 'Azmon', cluster T10
`H6144` — 'Ar', cluster T10
`H6160I` — 'Plains [of Moab]', cluster T10
`H6166A` — 'Arad', cluster T10
`H6295` — 'Pagiel', cluster T8
`H6301` — 'Pedahzur', cluster T8
`H6363B` — 'firstborn', cluster M37
`H6372G` — 'Phinehas', cluster T8
`H6431G` — 'Peleth', cluster T8
`H6449` — 'Pisgah', cluster T10
`H6465` — 'Peor', cluster T10
`H6517` — 'pot', cluster T12
`H6558` — 'Perezite', cluster T8
`H6604` — 'Pethor', cluster T10
`H6657` — 'Zedad', cluster T10
`H6686` — 'Zuar', cluster T8
`H6698G` — 'Zur', cluster T8
`H6698H` — 'Zur', cluster T8
`H6700` — 'Zuriel', cluster T8
`H6701` — 'Zurishaddai', cluster T8
`H6765` — 'Zelophehad', cluster T8
`H6790` — 'Zin', cluster T10
`H6792` — 'sheep', cluster T13
`H6796` — 'thorn', cluster T13
`H6814` — 'Zoan', cluster T10
`H6834` — 'Zippor', cluster T8
`H6839` — 'Zophim', cluster T10
`H6914` — 'Kibroth-hattaavah', cluster T10
`H6947` — 'Kadesh-barnea', cluster T10
`H6956` — 'Kohathite', cluster T8
`H6979C` — 'to destroy', cluster M10
`H7014A` — 'Kain', cluster T10
`H7017` — 'Kenite', cluster T11
`H7074H` — 'Kenizzite', cluster T8
`H7079` — 'Kenath', cluster T10
`H7141I` — 'Korah', cluster T8
`H7206` — 'Reubenite', cluster T8
`H7247G` — 'Riblah', cluster T10
`H7254` — 'Reba', cluster T8
`H7340K` — 'Rehob', cluster T10
`H7552G` — 'Rekem', cluster T8
`H7643H` — 'Sibmah', cluster T10
`H7707` — 'Shedeur', cluster T8
`H7847` — 'to turn aside', cluster M11
`H7899` — 'thorn', cluster T13
`H8017` — 'Shelumiel', cluster T8
`H8024` — 'Shelanite', cluster T8
`H8051G` — 'Shammua', cluster T8
`H8096G` — 'Shimei', cluster T8
`H8099` — 'Simeon', cluster T8
`H8221` — 'Shepham', cluster T10
`H8294` — 'Serah', cluster T8
`H8323A` — 'to rule', cluster M72
`H8344` — 'Sheshai', cluster T8
`H8404` — 'Taberah', cluster T10
`H8526G` — 'Talmai', cluster T8
`H8656G` — 'Tirzah', cluster T8
`H0130` — 'Edomite', cluster T11
`H0359A` — 'Elath', cluster T10
`H0368` — 'Emim', cluster T11
`H0380` — 'pupil', cluster T14
`H0709G` — 'Argob', cluster T10
`H0798` — 'Slopes [of Pisgah]', cluster T10
`H0881H` — 'Beeroth-[bene-jaakan]', cluster T10
`H1047` — 'Beth-peor', cluster T10
`H1142H` — '[Beeroth] Bene-jaakan', cluster T10
`H1221G` — 'Bezer', cluster T10
`H1237G` — 'Valley [of Jericho]', cluster T10
`H1425` — 'Gad', cluster T8
`H1474` — 'Golan', cluster T10
`H1630` — '[Mount] Gerizim', cluster T10
`H1631` — 'axe', cluster T12
`H1651` — 'Geshurite', cluster T11
`H1682` — 'bee', cluster T13
`H1703` — 'word', cluster M65
`H1772` — 'hawk', cluster T13
`H1774` — 'Dizahab', cluster T10
`H1795` — 'crushing', cluster M10
`H2157` — 'Zamzummin', cluster T11
`H2218` — 'Zered', cluster T10
`H2388I` — 'to strengthen: ensure', cluster M23
`H2768` — '[Mount] Hermon', cluster T10
`H2770` — 'sickle', cluster T12
`H2935` — 'basket', cluster T12
`H2960` — 'burden', cluster M78
`H3138` — 'autumn rain', cluster T13
`H3405H` — '[Plain of] Jericho', cluster T10
`H3419` — 'herb', cluster T13
`H3484` — 'Jeshurun', cluster T8
`H3603G` — 'environs', cluster T10
`H3631` — 'failing', cluster M24
`H3731` — 'Caphtor', cluster T10
`H3733C` — 'ram', cluster T13
`H3837B` — 'Laban', cluster T10
`H3893` — 'vigor', cluster M23
`H4064` — 'disease', cluster M73
`H4125` — 'Moabite', cluster T8
`H4149A` — 'Moserah', cluster T10
`H4520` — 'Manassite', cluster T8
`H4602` — 'Maacathite', cluster T11
`H5015H` — '[Mount] Nebo', cluster T10
`H5254H` — 'to test: try', cluster M35
`H5489` — 'Suph', cluster T10
`H5548` — 'Salecah', cluster T10
`H5603` — 'to cover', cluster M45
`H5612A` — 'scroll: document', cluster T12
`H5761G` — 'Avvim', cluster T11
`H5858C` — '[Mount] Ebal', cluster T10
`H5899` — 'Ir-hatmarim', cluster T10
`H5984H` — 'Ammon', cluster T10
`H6028` — 'dainty', cluster M04
`H6100` — 'Ezion-geber', cluster T10
`H6137` — 'scorpion', cluster T13
`H6160G` — 'Arabah', cluster T10
`H6177H` — 'Aroer', cluster T10
`H6252H` — 'Ashtaroth', cluster T10
`H6290H` — '[Mount] Paran', cluster T10
`H6618` — 'twisted', cluster M14
`H6643B` — 'gazelle', cluster T13
`H6722` — 'Sidonian', cluster T11
`H6896` — 'stomach', cluster T14
`H6932` — 'Kedemoth', cluster T10
`H6952` — 'assembly', cluster M44
`H6986` — 'destruction', cluster M55
`H6988` — 'incense', cluster T12
`H7216H` — 'Ramoth', cluster T10
`H7268` — 'quivering', cluster M01
`H7393H` — 'chariot: millstone', cluster T12
`H7497B` — 'Rephaim', cluster T11
`H7682` — 'to exalt', cluster M22
`H7697` — 'madness', cluster M66
`H7709` — 'field', cluster T10
`H7760K` — 'to set: consider', cluster M15
`H7834` — 'cloud', cluster T13
`H7865` — '[Mount] Sirion', cluster T10
`H8080` — 'to grow fat', cluster M46
`H8146` — 'hated', cluster M06
`H8149` — 'Senir', cluster T10
`H8164` — 'rain', cluster T13
`H8165G` — '[Mount] Seir', cluster T10
`H8303` — 'Sirion', cluster T10
`H8541` — 'bewilderment', cluster M01
`H8603` — 'Tophel', cluster T10
`H0044I` — 'Abiezer', cluster T8
`H0121H` — 'Adam', cluster T10
`H0129` — 'Adami', cluster T10
`H0131` — 'Adummim', cluster T10
`H0139` — 'Adoni-zedek', cluster T8
`H0146G` — 'Addar', cluster T10
`H0243` — 'Aznoth-tabor', cluster T10
`H0357` — 'Aijalon', cluster T10
`H0392H` — 'Achzib', cluster T10
`H0407` — 'Achshaph', cluster T10
`H0487` — 'Allammelech', cluster T10
`H0663H` — 'Aphek', cluster T10
`H0704` — 'Arba', cluster T8
`H0832` — 'Ashkelonite', cluster T11
`H0844G` — 'Asriel', cluster T8
`H0847` — 'Eshtaol', cluster T10
`H0932` — 'Bohan', cluster T8
`H0991` — 'Beten', cluster T10
`H0993` — 'Betonim', cluster T10
`H1004L` — 'Beth-[baal-meon]', cluster T10
`H1016H` — 'Beth-dagon', cluster T10
`H1025` — 'Beth-emek', cluster T10
`H1026` — 'Beth-arabah', cluster T10
`H1027` — 'Beth-haram', cluster T10
`H1031` — 'Beth-hoglah', cluster T10
`H1032G` — 'Beth-horon', cluster T10
`H1032H` — '[Upper] Beth-horon', cluster T10
`H1032I` — '[Lower] Beth-horon', cluster T10
`H1039` — 'Beth-nimrah', cluster T10
`H1052` — 'Beth-shean', cluster T10
`H1053G` — 'Beth-shemesh', cluster T10
`H1053H` — 'Beth-shemesh', cluster T10
`H1171` — 'Baal-gad', cluster T10
`H1173G` — '[Mount] Baalah', cluster T10
`H1173I` — 'Baalah', cluster T10
`H1192` — 'Baalath-beer', cluster T10
`H1237H` — '[Mizpah] Valley', cluster T10
`H1237I` — '[Lebanon] Valley', cluster T10
`H1382` — 'Gebalite', cluster T11
`H1389H` — 'Gibeath-[haaraloth]', cluster T10
`H1391` — 'Gibeon', cluster T10
`H1507` — 'Gezer', cluster T10
`H1516G` — 'Valley', cluster T10
`H1516H` — '[Iphtahel] Valley', cluster T10
`H1516Q` — 'Valley', cluster T10
`H1537I` — 'Galilee', cluster T10
`H1551` — 'Galilee', cluster T10
`H1650` — 'Geshur', cluster T10
`H1657H` — 'Goshen', cluster T10
`H1662` — 'Gath-hepher', cluster T10
`H1663` — 'Gittite', cluster T11
`H1688A` — 'Debir', cluster T10
`H1688B` — 'Debir', cluster T10
`H1688G` — 'Debir', cluster T10
`H1688H` — 'Debir', cluster T8
`H1705` — 'Daberath', cluster T10
`H1708` — 'Dabbesheth', cluster T10
`H1756G` — 'Dor', cluster T10
`H1756H` — 'Dor', cluster T10
`H1944` — 'Hoham', cluster T8
`H2036` — 'Horam', cluster T8
`H2067G` — 'Zabdi', cluster T8
`H2247` — 'to hide', cluster M20
`H2256A` — 'Mahalab', cluster T10
`H2482` — 'Hali', cluster T10
`H2501` — 'Heleph', cluster T10
`H2507` — 'Helek', cluster T8
`H2520` — 'Helkath', cluster T10
`H2525` — 'hot', cluster M02
`H2540` — 'Hammon', cluster T10
`H2576` — 'Hammoth-dor', cluster T10
`H2615` — 'Hannathon', cluster T10
`H2621G` — 'Hosah', cluster T10
`H2674G` — 'Hazor', cluster T10
`H2696J` — 'Hezron', cluster T10
`H2712A` — 'Hukkok', cluster T10
`H2971H` — 'Jair', cluster T10
`H2983H` — 'Jebus', cluster T10
`H2985G` — 'Jabin', cluster T8
`H2991` — 'Ibleam', cluster T10
`H2995G` — 'Jabneel', cluster T10
`H2995H` — 'Jabneel', cluster T10
`H3017` — 'Jagur', cluster T10
`H3103I` — 'Jobab', cluster T8
`H3239B` — 'Janoah', cluster T10
`H3297` — '[Mount] Jearim', cluster T10
`H3309G` — 'Japhia', cluster T8
`H3309H` — 'Japhia', cluster T10
`H3317` — '[Valley of] Iphtahel', cluster T10
`H3362` — 'Jokneam', cluster T10
`H3412G` — 'Jarmuth', cluster T10
`H3521G` — 'Cabul', cluster T10
`H3693` — 'Chesalon', cluster T10
`H3694` — 'Chesulloth', cluster T10
`H3696` — 'Chisloth-tabor', cluster T10
`H3756H` — 'Carmi', cluster T8
`H3841H` — 'Libnah', cluster T10
`H3844I` — '[Valley of] Lebanon', cluster T10
`H3946` — 'Lakkum', cluster T10
`H3956I` — 'tongue: bar', cluster T14
`H3959` — 'Leshem', cluster T10
`H4023` — 'Megiddo', cluster T10
`H4068` — 'Madon', cluster T10
`H4137` — 'Moladah', cluster T10
`H4158` — 'Mephaath', cluster T10
`H4366` — 'Michmethath', cluster T10
`H4569B` — 'ford', cluster T10
`H4601R` — 'Maacah', cluster T10
`H4632` — 'Mearah', cluster T10
`H4708J` — '[Valley of] Mizpeh', cluster T10
`H4719` — 'Makkedah', cluster T10
`H4792` — 'Merom', cluster T10
`H4831` — 'Mareal', cluster T10
`H4861` — 'Mishal', cluster T10
`H4956` — 'Misrephoth-maim', cluster T10
`H5269` — 'Neah', cluster T10
`H5272` — 'Neiel', cluster T10
`H5292A` — 'Naarah', cluster T10
`H5316G` — 'Naphath', cluster T10
`H5316H` — 'Naphath', cluster T10
`H5346` — '[Adami]-nekeb', cluster T10
`H5683` — 'Ebron', cluster T10
`H5700G` — 'Eglon', cluster T10
`H5740B` — 'Eder', cluster T10
`H5825` — 'Azekah', cluster T10
`H5841` — 'Gaza', cluster T10
`H5852H` — 'Ataroth', cluster T10
`H5853` — 'Ataroth-addar', cluster T10
`H5874` — 'En-dor', cluster T10
`H5883` — 'En-rogel', cluster T10
`H5885` — 'En-shemesh', cluster T10
`H5887` — 'En-tappuah', cluster T10
`H5905` — 'Ir-shemesh', cluster T10
`H5912` — 'Achan', cluster T8
`H5915G` — 'Achsah', cluster T8
`H5945G` — 'Upper [Beth Horon]', cluster T10
`H6008` — 'Amad', cluster T10
`H6010J` — 'Emek', cluster T10
`H6010P` — 'Valley [of Rephaim]', cluster T10
`H6024` — 'Anab', cluster T10
`H6139` — 'Ekron', cluster T10
`H6160J` — '[Beth]-arabah', cluster T10
`H6160K` — '[Sea of] the Arabah', cluster T10
`H6177G` — 'Aroer', cluster T10
`H6190G` — '[Gilgal]-haaraloth', cluster T10
`H6278` — 'Eth-kazin', cluster T10
`H6502` — 'Piram', cluster T8
`H6721I` — 'Sidon', cluster T10
`H6815` — 'Zaanannim', cluster T10
`H6829` — 'Zaphon', cluster T10
`H6881` — 'Zorah', cluster T10
`H6891` — 'Zarethan', cluster T10
`H6909` — 'Kabzeel', cluster T10
`H6943G` — 'Kedesh', cluster T10
`H7071G` — 'Kanah', cluster T10
`H7071H` — 'Kanah', cluster T10
`H7104` — '[Emek]-keziz', cluster T10
`H7154` — 'Kiriath-baal', cluster T10
`H7157` — 'Kiriath-jearim', cluster T10
`H7158` — 'Kiriath-sannah', cluster T10
`H7173` — 'Karka', cluster T10
`H7178` — 'Kartan', cluster T10
`H7340G` — 'Rehob', cluster T10
`H7343` — 'Rahab', cluster T8
`H7414H` — 'Ramah', cluster T10
`H7417H` — 'Rimmon', cluster T10
`H7434` — 'Ramath-mizpeh', cluster T10
`H7497G` — '[Valley of] Rephaim', cluster T10
`H7652B` — 'Sheba', cluster T10
`H7671` — 'Shebarim', cluster T10
`H7766` — 'Shunem', cluster T10
`H7831` — 'Shahazumah', cluster T10
`H7850` — 'scourge', cluster M06
`H7883G` — 'Shihor', cluster T10
`H7884` — 'Shihor-libnath', cluster T10
`H7887` — 'Shiloh', cluster T10
`H7928G` — 'Shechem', cluster T8
`H7942` — 'Shikkeron', cluster T10
`H8061` — 'Shemida', cluster T8
`H8089` — 'report', cluster M82
`H8110A` — 'Shimron', cluster T10
`H8165H` — '[Mount] Seir', cluster T10
`H8301` — 'Sarid', cluster T10
`H8387` — 'Taanath-shiloh', cluster T10
`H8481G` — 'Lower [Beth Horon]', cluster T10
`H8556B` — 'Timnath-serah', cluster T10
`H8590` — 'Taanach', cluster T10
`H8599B` — 'Tappuah', cluster T10
`H0033` — 'Abiezrite', cluster T8
`H0040H` — 'Abimelech', cluster T8
`H0042` — 'Abinoam', cluster T8
`H0047H` — 'mighty: stallion', cluster M23
`H0064` — 'Abel-keramim', cluster T10
`H0065` — 'Abel-meholah', cluster T10
`H0078` — 'Ibzan', cluster T8
`H0137` — 'Adoni-bezek', cluster T8
`H0164G` — 'Ehud', cluster T8
`H0303` — 'Ahlab', cluster T10
`H0356J` — 'Elon', cluster T8
`H0410H` — 'El [Berith]', cluster T7
`H0673G` — 'Ephraimite', cluster T8
`H0725` — 'Arumah', cluster T10
`H0758N` — 'Mesopotamia', cluster T10
`H0843` — 'Asherite', cluster T8
`H0876H` — 'Beer', cluster T10
`H0966G` — 'Bezek', cluster T10
`H1012` — 'Beth-barah', cluster T10
`H1029` — 'Beth-shittah', cluster T10
`H1043` — 'Beth-anath', cluster T10
`H1050` — 'Beth-rehob', cluster T10
`H1053I` — 'Beth-shemesh', cluster T10
`H1066` — 'Bochim', cluster T10
`H1145` — 'Benjaminite', cluster T8
`H1170` — 'Baal-berith', cluster T7
`H1179` — '[Mount] Baal-hermon', cluster T10
`H1193` — 'Baal-tamar', cluster T10
`H1301` — 'Barak', cluster T8
`H1387H` — 'Gibeah', cluster T10
`H1387J` — '[Maareh]-geba', cluster T10
`H1439` — 'Gideon', cluster T8
`H1440` — 'Gidom', cluster T10
`H1568I` — 'Gilead', cluster T8
`H1568K` — '[Mount] Gilead', cluster T10
`H1568L` — '[Jabesh]-gilead', cluster T10
`H1569` — 'Gileadite', cluster T11
`H1603` — 'Gaal', cluster T8
`H1617G` — 'Gera', cluster T8
`H1683H` — 'Deborah', cluster T8
`H1712` — 'Dagon', cluster T7
`H1734G` — 'Dodo', cluster T8
`H1807` — 'Delilah', cluster T8
`H1839` — 'Danite', cluster T11
`H1985` — 'Hillel', cluster T8
`H1989` — 'hammer', cluster T12
`H2062` — 'Zeeb', cluster T8
`H2075` — 'Zebulunite', cluster T8
`H2078` — 'Zebah', cluster T8
`H2083` — 'Zebul', cluster T8
`H2115` — 'to crush', cluster M10
`H2268H` — 'Heber', cluster T8
`H2462` — 'Helbah', cluster T10
`H2717B` — 'to destroy', cluster M10
`H2775A` — 'sun', cluster T13
`H2776G` — 'Heres', cluster T10
`H2776H` — '[Mount] Heres', cluster T10
`H2800` — 'Harosheth', cluster T10
`H2888` — 'Tabbath', cluster T10
`H2897` — 'Tob', cluster T10
`H2971I` — 'Jair', cluster T8
`H2982` — 'Jebus', cluster T10
`H2985H` — 'Jabin', cluster T8
`H3003G` — 'Jabesh [Gilead]', cluster T10
`H3003I` — 'Jabesh', cluster T10
`H3011` — 'Jogbehah', cluster T10
`H3083G` — 'Jonathan', cluster T8
`H3101G` — 'Joash', cluster T8
`H3147G` — 'Jotham', cluster T8
`H3278` — 'Jael', cluster T8
`H3316H` — 'Jephthah', cluster T8
`H3378` — 'Jerubbaal', cluster T8
`H3499B` — 'cord', cluster M03,T12
`H3500G` — 'Jether', cluster T8
`H3573` — 'Cushan-rishathaim', cluster T8
`H3829` — 'Lebonah', cluster T10
`H3844H` — '[Mount] Lebanon', cluster T10
`H3870G` — 'Luz', cluster T10
`H3895G` — 'Lehi', cluster T10
`H3896` — 'Lehi', cluster T10
`H3919A` — 'Laish', cluster T10
`H3941` — 'Lappidoth', cluster T8
`H3943` — 'to twist', cluster M57
`H4176H` — 'Moreh', cluster T10
`H4265` — 'Mahaneh-dan', cluster T10
`H4277` — 'to destroy', cluster M10
`H4318G` — 'Micah', cluster T8
`H4321I` — 'Micah', cluster T8
`H4495` — 'Manoah', cluster T8
`H4496G` — 'Nohah', cluster T10
`H4511` — 'Minnith', cluster T10
`H4519K` — 'Moses', cluster T8
`H4584G` — 'Maon', cluster T10
`H4629G` — 'Maareh', cluster T10
`H4668` — 'key', cluster T12
`H4708K` — 'Mizpah', cluster T10
`H4709G` — 'Mizpah', cluster T10
`H4718A` — 'hammer', cluster T12
`H4789` — 'Meroz', cluster T10
`H5025H` — 'Nobah', cluster T10
`H5096` — 'Nahalol', cluster T10
`H5158J` — '[Sorek] Valley', cluster T10
`H5321H` — '[Kedesh]-naphtali', cluster T10
`H5516G` — 'Sisera', cluster T8
`H5651G` — 'Ebed', cluster T8
`H5658H` — 'Abdon', cluster T8
`H5700H` — 'Eglon', cluster T8
`H5862G` — 'Etam', cluster T10
`H5875` — 'En-hakkore', cluster T10
`H5878` — 'Harod', cluster T10
`H5910` — 'Acco', cluster T10
`H6049G` — "Diviners' [Oak]", cluster T10
`H6060B` — 'necklace', cluster T12
`H6067` — 'Anath', cluster T8
`H6084H` — 'Ophrah', cluster T10
`H6128` — 'crooked', cluster M14
`H6159` — 'Oreb', cluster T8
`H6252G` — 'Ashtaroth', cluster T10
`H6274` — 'Othniel', cluster T8
`H6312H` — 'Puah', cluster T8
`H6400` — 'millstone', cluster T12
`H6513` — 'Purah', cluster T8
`H6552` — 'Pirathon', cluster T10
`H6553` — 'Pirathon', cluster T10
`H6574` — 'refuse', cluster M30
`H6759` — 'Zalmunna', cluster T8
`H6828H` — 'Zaphon', cluster T10
`H6857` — 'Zephath', cluster T10
`H6888` — 'Zererah', cluster T10
`H6943J` — 'Kedesh', cluster T10
`H6965K` — 'to arise: guard', cluster M74
`H7003` — 'Kitron', cluster T10
`H7014G` — 'Kenite', cluster T11
`H7028` — 'Kishon', cluster T10
`H7056` — 'Kamon', cluster T10
`H7073I` — 'Kenaz', cluster T8
`H7134` — 'axe', cluster T12
`H7336` — 'to rule', cluster M72
`H7340H` — 'Rehob', cluster T10
`H7417C` — '[Rock of] Rimmon', cluster T10
`H7754A` — 'branch', cluster T13
`H7754B` — 'branch', cluster T13
`H7776` — 'fox', cluster T13
`H7796` — '[Valley of] Sorek', cluster T10
`H8044` — 'Shamgar', cluster T8
`H8069H` — 'Shamir', cluster T10
`H8123` — 'Samson', cluster T8
`H8167` — 'Seirah', cluster T10
`H8169` — 'Shaalbim', cluster T10
`H8439H` — 'Tola', cluster T8
`H0458` — 'Elimelech', cluster T8
`H0673H` — 'Ephrathite', cluster T8
`H1162G` — 'Boaz', cluster T8
`H3448` — 'Jesse', cluster T8
`H3630` — 'Chilion', cluster T8
`H3860` — 'therefore', cluster T6
`H4248` — 'Mahlon', cluster T8
`H4304` — 'cloak', cluster T12
`H4755` — 'Mara', cluster T8
`H5281` — 'Naomi', cluster T8
`H5744G` — 'Obed', cluster T8
`H6204` — 'Orpah', cluster T8
`H7327` — 'Ruth', cluster T8
`H0022G` — 'Abiel', cluster T8
`H0026G` — 'Abigail', cluster T8
`H0029G` — 'Abijah', cluster T8
`H0041G` — 'Abinadab', cluster T8
`H0041H` — 'Abinadab', cluster T8
`H0041I` — 'Abinadab', cluster T8
`H0052` — 'Abishai', cluster T8
`H0054` — 'Abiathar', cluster T8
`H0059G` — 'Abel', cluster T10
`H0072` — 'Ebenezer', cluster T10
`H0074` — 'Abner', cluster T8
`H0090H` — 'Agag', cluster T8
`H0237` — 'Ezel', cluster T10
`H0281O` — 'Ahijah', cluster T8
`H0285G` — 'Ahitub', cluster T8
`H0288G` — 'Ahimelech', cluster T8
`H0288H` — 'Ahimelech', cluster T8
`H0290G` — 'Ahimaaz', cluster T8
`H0293G` — 'Ahinoam', cluster T8
`H0293H` — 'Ahinoam', cluster T8
`H0350` — 'Ichabod', cluster T8
`H0371` — "isn't?", cluster T6
`H0397` — 'Achish', cluster T8
`H0430I` — '[Gibeath]-elohim', cluster T10
`H0446I` — 'Eliab', cluster T8
`H0453G` — 'Elihu', cluster T8
`H0499H` — 'Eleazar', cluster T8
`H0511H` — 'Elkanah', cluster T8
`H0647` — 'Aphiah', cluster T8
`H0663G` — 'Aphek', cluster T10
`H0712` — 'box', cluster T12
`H0830H` — 'refuse', cluster M30
`H0917H` — 'Barak', cluster T8
`H0949` — 'Bozez', cluster T10
`H0966H` — 'Bezek', cluster T10
`H1022` — 'Bethlehemite', cluster T10
`H1030` — 'Bethshemite', cluster T11
`H1033` — 'Beth-car', cluster T10
`H1064` — 'Becorath', cluster T8
`H1308` — 'Besor', cluster T10
`H1387G` — 'Geba', cluster T10
`H1410H` — 'Gad', cluster T8
`H1516I` — '[Zeboim] Valley', cluster T10
`H1516P` — 'Gath', cluster T10
`H1533H` — '[Mount] Gilboa', cluster T10
`H1555` — 'Goliath', cluster T8
`H1673` — 'Doeg', cluster T8
`H1731` — 'pot', cluster T12
`H1826I` — 'to silence: destroyed', cluster M55
`H2128H` — 'Ziph', cluster T10
`H2130` — 'Ziphite', cluster T11
`H2416B` — 'kinsfolk', cluster M25,T8
`H2444` — 'Hachilah', cluster T10
`H2584` — 'Hannah', cluster T8
`H2638` — 'lacking', cluster M18
`H2652` — 'Hophni', cluster T8
`H2678` — 'arrow', cluster T12
`H2793G` — 'Horesh', cluster T10
`H2802` — 'Hereth', cluster T10
`H2923` — 'Telaim', cluster T10
`H2924` — 'lamb', cluster T13
`H3083H` — 'Jonathan', cluster T8
`H3091H` — 'Joshua', cluster T8
`H3097G` — 'Joab', cluster T8
`H3100G` — 'Joel', cluster T8
`H3129G` — 'Jonathan', cluster T8
`H3129N` — 'Jonathan', cluster T8
`H3157G` — 'Jezreel', cluster T10
`H3158G` — 'Jezreel', cluster T10
`H3227B` — '[Ben]jaminite', cluster T8
`H3293B` — 'honeycomb', cluster T10
`H3395G` — 'Jeroham', cluster T8
`H3397` — 'Jerahmeelite', cluster T8
`H3440H` — 'Ishvi', cluster T8
`H3452G` — 'Jeshimon', cluster T10
`H3614` — 'Calebite', cluster T8
`H3761` — 'Carmelite', cluster T11
`H3774G` — 'Cherethite', cluster T11
`H4051` — 'Migron', cluster T10
`H4224B` — 'refuge', cluster M19
`H4324G` — 'Michal', cluster T8
`H4363` — 'Michmash', cluster T10
`H4444` — 'Malchi-shua', cluster T8
`H4582` — 'Maoch', cluster T8
`H4708H` — 'Mizpeh', cluster T10
`H4764` — 'Merab', cluster T8
`H5011` — 'Nob', cluster T10
`H5035A` — 'bag', cluster T12
`H5035B` — 'harp', cluster T12
`H5037` — 'Nabal', cluster T8
`H5121` — 'Naioth', cluster T10
`H5176G` — 'Nahash', cluster T8
`H5369G` — 'Ner', cluster T8
`H5573` — 'Seneh', cluster T10
`H5741` — 'Adriel', cluster T8
`H5770` — 'to watch', cluster M74
`H5872` — 'Engedi', cluster T10
`H5941` — 'Eli', cluster T8
`H6010I` — 'Valley [of Elah]', cluster T10
`H6084G` — 'Ophrah', cluster T10
`H6145` — 'enemy', cluster M06
`H6310L` — 'lip: one third', cluster T14
`H6372H` — 'Phinehas', cluster T8
`H6444` — 'Peninnah', cluster T8
`H6477` — 'bluntness', cluster M53
`H6550` — 'flea', cluster T13
`H6571A` — 'horse', cluster T13
`H6650H` — '[Valley of] Zeboim', cluster T10
`H6678G` — 'Zobah', cluster T10
`H6689G` — 'Zuph', cluster T8
`H6689H` — 'Zuph', cluster T10
`H6766` — 'Zelzah', cluster T10
`H6835` — 'jar', cluster T12
`H6860` — 'Ziklag', cluster T10
`H6870G` — 'Zeruiah', cluster T8
`H6872C` — 'Zeror', cluster T8
`H7027G` — 'Kish', cluster T8
`H7084` — 'Keilah', cluster T10
`H7414J` — 'Ramah', cluster T10
`H7436` — 'Ramathaim-zophim', cluster T10
`H7586G` — 'Saul', cluster T8
`H7704B` — 'land: soil', cluster T13
`H7777A` — 'Shual', cluster T10
`H7906` — 'Secu', cluster T10
`H8031` — 'Shalishah', cluster T10
`H8048J` — 'Shammah', cluster T8
`H8050G` — 'Samuel', cluster T8
`H8127I` — 'tooth: crag', cluster T14
`H8127J` — 'tooth: prong', cluster T14
`H8129` — 'Shen', cluster T10
`H8138A` — 'to change', cluster M45
`H8171` — 'Shaalim', cluster T10
`H8189G` — 'Shaaraim', cluster T10
`H8213` — 'to abase', cluster M53
`H8302B` — 'armor', cluster T12
`H8396H` — 'Tabor', cluster T10
`H8459` — 'Tohu', cluster T8
`H0026H` — 'Abigail', cluster T8
`H0053` — 'Absalom', cluster T8
`H0059H` — 'Abel', cluster T10
`H0062` — 'Abel-beth-maachah', cluster T10
`H0089` — 'Agee', cluster T8
`H0151` — 'Adoram', cluster T8
`H0223A` — 'Uriah', cluster T8
`H0283G` — 'Ahio', cluster T8
`H0286` — 'Ahilud', cluster T8
`H0290H` — 'Ahimaaz', cluster T8
`H0302` — 'Ahithophel', cluster T8
`H0345H` — 'Aiah', cluster T8
`H0378` — 'Ish-bosheth', cluster T8
`H0445G` — 'Elhanan', cluster T8
`H0463G` — 'Eliam', cluster T8
`H0499I` — 'Eleazar', cluster T8
`H0522` — 'Ammah', cluster T10
`H0550G` — 'Amnon', cluster T8
`H0669K` — '[Forest of] Ephraim', cluster T10
`H0669L` — 'Ephraim', cluster T10
`H0728` — 'Araunah', cluster T8
`H0739` — 'Ariel', cluster T11
`H0758M` — 'Edom', cluster T10
`H0764` — 'Armoni', cluster T8
`H0805B` — 'Ashurite', cluster T8
`H0863G` — 'Ittai', cluster T8
`H0881G` — 'Beeroth', cluster T10
`H0886` — 'Beerothite', cluster T11
`H0972` — 'chosen', cluster M64
`H0980` — 'Bahurim', cluster T10
`H0984` — 'Betah', cluster T10
`H1075` — 'Bichri', cluster T8
`H1141G` — 'Benaiah', cluster T8
`H1178` — 'Baal-hazor', cluster T10
`H1188` — 'Baal-perazim', cluster T10
`H1196G` — 'Baanah', cluster T8
`H1268B` — 'Berothai', cluster T10
`H1271G` — 'Barzillai', cluster T8
`H1271H` — 'Barzillai', cluster T8
`H1276` — 'Bichrites', cluster T8
`H1295H` — 'pool', cluster T10
`H1339` — 'Bathsheba', cluster T8
`H1359` — 'Gob', cluster T10
`H1387I` — 'Geba', cluster T10
`H1393` — 'Gibeonite', cluster T11
`H1516J` — '[Salt] Valley', cluster T10
`H1520` — 'Giah', cluster T10
`H1526` — 'Gilonite', cluster T11
`H1533G` — 'Gilboa', cluster T10
`H1542` — 'Giloh', cluster T10
`H1617H` — 'Gera', cluster T8
`H1664` — 'Gittaim', cluster T10
`H1734H` — 'Dodo', cluster T8
`H1842` — 'Jaan', cluster T10
`H1909` — 'Hadadezer', cluster T8
`H1928` — 'Hadarezer', cluster T8
`H2043` — 'Hararite', cluster T11
`H2365` — 'Hushai', cluster T8
`H2416D` — 'community', cluster M44,T8
`H2424` — 'living', cluster M25
`H2431` — 'Helam', cluster T10
`H2438G` — 'Hiram', cluster T8
`H2521` — 'Helkath-hazzurim', cluster T10
`H2586G` — 'Hanun', cluster T8
`H2645` — 'to cover', cluster M45
`H2773` — 'Horonaim', cluster T10
`H2841` — 'collection', cluster M18
`H2972` — 'Jairite', cluster T8
`H3041` — 'Jedidiah', cluster T8
`H3063O` — '[Baalah of]Judah', cluster T10
`H3077G` — 'Jehoiada', cluster T8
`H3082H` — 'Jonadab', cluster T8
`H3083I` — 'Jonathan', cluster T8
`H3083O` — 'Jonathan', cluster T8
`H3092G` — 'Jehoshaphat', cluster T8
`H3122G` — 'Jonadab', cluster T8
`H3141G` — 'Joram', cluster T8
`H3157I` — 'Jezreel', cluster T10
`H3228G` — '[Ben]jaminite', cluster T8
`H3293H` — '[Ephraim] Forest', cluster T10
`H3296` — 'Jaare-oregim', cluster T8
`H3380` — 'Jerubbesheth', cluster T8
`H3429` — 'Josheb-basshebeth', cluster T8
`H3430` — 'Ishbi-benob', cluster T8
`H3481G` — 'Ishmaelite', cluster T8
`H3501` — 'Ithra', cluster T8
`H3643` — 'Chimham', cluster T8
`H3774H` — 'Cherethite', cluster T11
`H3810` — 'Lo-debar', cluster T10
`H3813` — 'to cover', cluster M45
`H3919B` — 'Laish', cluster T8
`H4037` — 'axe', cluster T12
`H4063` — 'garment', cluster T12
`H4316J` — 'Mica', cluster T8
`H4324H` — 'Merab', cluster T8
`H4353H` — 'Machir', cluster T8
`H4417H` — '[Valley of] Salt', cluster T10
`H4500` — 'loom-beam', cluster T12
`H4648G` — 'Mephibosheth', cluster T8
`H4648H` — 'Mephibosheth', cluster T8
`H4937A` — 'support', cluster M70
`H4965` — 'Metheg-ammah', cluster T10
`H5176H` — 'Nahash', cluster T8
`H5176I` — 'Nahash', cluster T8
`H5176J` — 'Nahash', cluster T8
`H5225` — 'Nacon', cluster T8
`H5273B` — 'musical', cluster M22
`H5379` — 'gift', cluster M39
`H5416G` — 'Nathan', cluster T8
`H5416H` — 'Nathan', cluster T8
`H5444` — 'Sibbecai', cluster T8
`H5593` — 'Saph', cluster T8
`H5626` — 'Sirah', cluster T10
`H5654` — 'Obed-edom', cluster T8
`H5679` — 'ford', cluster T10
`H5722` — '`wielded`', cluster T8
`H5798A` — 'Uzzah', cluster T8
`H5896G` — 'Ira', cluster T8
`H5988H` — 'Ammiel', cluster T8
`H5989J` — 'Ammihud', cluster T8
`H6021G` — 'Amasa', cluster T8
`H6214G` — 'Asahel', cluster T8
`H6409H` — 'Paltiel', cluster T8
`H6505` — 'mule', cluster T13
`H6560H` — 'Perez-uzzah', cluster T8
`H6659G` — 'Zadok', cluster T8
`H6717` — 'Ziba', cluster T8
`H6762` — 'Zela', cluster T10
`H6789` — 'to destroy', cluster M10
`H6939` — 'Kidron', cluster T10
`H7013` — 'spear', cluster T12
`H7166` — 'ankle', cluster T14
`H7274` — 'Rogelim', cluster T10
`H7340I` — 'Rehob', cluster T8
`H7394G` — 'Rechab', cluster T8
`H7417B` — 'Rimmon', cluster T8
`H7463` — 'friend', cluster M05
`H7497A` — 'Rapha', cluster T8
`H7532` — 'Rizpah', cluster T8
`H7629` — 'Shobi', cluster T8
`H7652A` — 'Sheba', cluster T8
`H7727G` — 'Shobab', cluster T8
`H7731` — 'Shobach', cluster T8
`H7734` — 'to turn back', cluster M11
`H7987` — 'quietness', cluster M33
`H8010` — 'Solomon', cluster T8
`H8037G` — 'Shammah', cluster T8
`H8051H` — 'Shammua', cluster T8
`H8093` — 'Shimeah', cluster T8
`H8096H` — 'Shimei', cluster T8
`H8405` — 'Thebez', cluster T10
`H8461` — 'Tahchemonite', cluster T11
`H8483` — 'Kadesh', cluster T10
`H8526H` — 'Talmai', cluster T8
`H8559H` — 'Tamar', cluster T8
`H8559I` — 'Tamar', cluster T8
`H8583` — 'Toi', cluster T8
`H8621` — 'Tekoa', cluster T10
`H0029H` — 'Abijah', cluster T8
`H0038` — 'Abijam', cluster T8
`H0048H` — 'Abiram', cluster T8
`H0049` — 'Abishag', cluster T8
`H0068I` — '[Zoheleth] Stone', cluster T10
`H0111` — 'Hadad', cluster T8
`H0138G` — 'Adonijah', cluster T8
`H0141` — 'Adoniram', cluster T8
`H0197G` — 'Hall [of pillars]', cluster T10
`H0211H` — 'Ophir', cluster T10
`H0274G` — 'Ahaziah', cluster T8
`H0281G` — 'Ahijah', cluster T8
`H0281H` — 'Ahijah', cluster T8
`H0281I` — 'Ahijah', cluster T8
`H0301` — 'Ahishar', cluster T8
`H0348` — 'Jezebel', cluster T8
`H0359B` — 'Eloth', cluster T10
`H0387G` — 'Ethan', cluster T8
`H0388` — 'Ethanim', cluster T15
`H0425H` — 'Elah', cluster T8
`H0450H` — 'Eliada', cluster T8
`H0452G` — 'Elijah', cluster T8
`H0456` — 'Elihoreph', cluster T8
`H0477` — 'Elisha', cluster T8
`H0526G` — 'Amon', cluster T8
`H0609G` — 'Asa', cluster T8
`H0663I` — 'Aphek', cluster T10
`H0777` — 'Arza', cluster T8
`H0856` — 'Ethbaal', cluster T8
`H0935O` — 'Lebo', cluster T10
`H0945` — 'Bul', cluster T15
`H1017` — 'Bethelite', cluster T11
`H1130G` — 'Ben-hadad', cluster T8
`H1195G` — 'Baana', cluster T8
`H1201` — 'Baasha', cluster T8
`H1405` — 'Gibbethon', cluster T10
`H1527` — 'Ginath', cluster T8
`H1568M` — '[Ramoth]-gilead', cluster T10
`H1592` — 'Genubath', cluster T8
`H1827` — 'silence', cluster M33
`H1862` — 'Darda', cluster T8
`H1908I` — 'Hadad', cluster T8
`H1968G` — 'Heman', cluster T8
`H2071` — 'Zabud', cluster T8
`H2099` — 'Ziv', cluster T15
`H2120` — "Serpent's [Stone]", cluster T10
`H2174A` — 'Zimri', cluster T8
`H2294` — 'Haggith', cluster T8
`H2383` — 'Hezion', cluster T8
`H2419` — 'Hiel', cluster T8
`H2438H` — 'Hiram', cluster T8
`H2607G` — 'Hanani', cluster T8
`H2682A` — 'grass', cluster T13
`H2715` — 'noble', cluster M34
`H2886` — 'Tabrimmon', cluster T8
`H2955` — 'Taphath', cluster T8
`H2977G` — 'Josiah', cluster T8
`H3058G` — 'Jehu', cluster T8
`H3088G` — 'Jehoram', cluster T8
`H3092I` — 'Jehoshaphat', cluster T8
`H3101H` — 'Joash', cluster T8
`H3129O` — 'Jonathan', cluster T8
`H3158H` — 'Jezreelite', cluster T10
`H3199H` — 'Jachin', cluster T12
`H3229` — 'Imlah', cluster T8
`H3293I` — '[House of] the Forest', cluster T10
`H3361G` — 'Jokmeam', cluster T10
`H3379G` — 'Jeroboam', cluster T8
`H3500H` — 'Jether', cluster T8
`H3521H` — 'Cabul', cluster T10
`H3633G` — 'Calcol', cluster T8
`H3668G` — 'Chenaanah', cluster T8
`H3672H` — 'Chinneroth', cluster T10
`H3747` — 'Cherith', cluster T10
`H3760H` — '[Mount] Carmel', cluster T10
`H3844J` — '[House of the Forest of] Lebanon', cluster T10
`H4235` — 'Mahol', cluster T8
`H4321G` — 'Micaiah', cluster T8
`H4403` — 'garment', cluster T12
`H4445B` — 'Milcom', cluster T7
`H4552` — 'support', cluster M70
`H4601K` — 'Maacah', cluster T8
`H4601Q` — 'Maacah', cluster T8
`H4717` — 'hammer', cluster T12
`H4991` — 'gift', cluster M39
`H5022` — 'Naboth', cluster T8
`H5028` — 'Nebat', cluster T8
`H5070H` — 'Nadab', cluster T8
`H5216B` — 'lamp', cluster T12
`H5250` — 'Nimshi', cluster T8
`H5279A` — 'Naamah', cluster T8
`H5447` — 'burden', cluster M78
`H5449` — 'burden', cluster M78
`H5653G` — 'Abda', cluster T8
`H5662G` — 'Obadiah', cluster T8
`H5676I` — 'side: west', cluster T10
`H5806G` — 'Azubah', cluster T8
`H5838H` — 'Azariah', cluster T8
`H5859` — 'Ijon', cluster T10
`H5982H` — '[Hall of] Pillars', cluster T10
`H6068G` — 'Anathoth', cluster T10
`H6152B` — 'Arabia', cluster T10
`H6253` — 'Ashtoreth', cluster T7
`H6506` — 'female mule', cluster T13
`H6547K` — 'Pharaoh', cluster T8
`H6667G` — 'Zedekiah', cluster T8
`H6868G` — 'Zeredah', cluster T10
`H6871` — 'Zeruah', cluster T8
`H6876` — 'Tyrian', cluster T11
`H6995` — 'little finger', cluster T14
`H7182` — 'attentiveness', cluster M41
`H7331` — 'Rezon', cluster T8
`H7346` — 'Rehoboam', cluster T8
`H7418G` — 'Ramoth', cluster T10
`H7472` — 'Rei', cluster T8
`H7569` — 'chain', cluster T12
`H7614J` — 'Sheba', cluster T10
`H7687G` — 'Segub', cluster T8
`H7888` — 'Shilonite', cluster T11
`H7894` — 'Shisha', cluster T8
`H7895` — 'Shishak', cluster T8
`H7977` — 'Shilhi', cluster T8
`H8096I` — 'Shimei', cluster T8
`H8098A` — 'Shemaiah', cluster T8
`H8106A` — 'Shemer', cluster T8
`H8202H` — 'Shaphat', cluster T8
`H8402` — 'Tibni', cluster T8
`H8472G` — 'Tahpenes', cluster T8
`H8500` — 'peacock', cluster T13
`H8607G` — 'Tiphsah', cluster T10
`H8656H` — 'Tirzah', cluster T10
`H0021` — 'Abi', cluster T8
`H0152G` — 'Adrammelech', cluster T8
`H0152H` — 'Adrammelech', cluster T8
`H0219B` — 'herb', cluster T13
`H0223G` — 'Uriah', cluster T8
`H0232` — 'girdle', cluster T12
`H0274H` — 'Ahaziah', cluster T8
`H0296` — 'Ahikam', cluster T8
`H0425I` — 'Elah', cluster T8
`H0471G` — 'Eliakim', cluster T8
`H0471I` — 'Eliakim', cluster T8
`H0476I` — 'Elishama', cluster T8
`H0494G` — 'Elnathan', cluster T8
`H0526H` — 'Amon', cluster T8
`H0531` — 'Amoz', cluster T8
`H0549H` — 'Amana', cluster T10
`H0558G` — 'Amaziah', cluster T8
`H0623G` — 'Asaph', cluster T8
`H0634` — 'Esarhaddon', cluster T8
`H0669H` — 'Ephraim [Gate]', cluster T10
`H0683` — 'Azaliah', cluster T8
`H0709H` — 'Argob', cluster T8
`H0745` — 'Arieh', cluster T8
`H0761H` — 'Syrian', cluster T11
`H0774` — 'Arpad', cluster T10
`H0807` — 'Ashima', cluster T7
`H0920` — 'Bidkar', cluster T8
`H1004H` — 'Beth [Haggan]', cluster T10
`H1044` — 'Beth-eked', cluster T10
`H1081` — 'Baladan', cluster T8
`H1130H` — 'Ben-hadad', cluster T8
`H1190` — 'Baal-shalishah', cluster T10
`H1218` — 'Bozkath', cluster T10
`H1255` — 'Merodach-baladan', cluster T8
`H1424` — 'Gadi', cluster T8
`H1436B` — 'Gedaliah', cluster T8
`H1470` — 'Gozan', cluster T10
`H1483` — 'Gur', cluster T10
`H1522` — 'Gehazi', cluster T8
`H1537H` — 'Gilgal', cluster T10
`H1954G` — 'Hoshea', cluster T8
`H2012` — 'Hena', cluster T10
`H2080` — 'Zebidah', cluster T8
`H2148C` — 'Zechariah', cluster T8
`H2148P` — 'Zechariah', cluster T8
`H2249` — 'Habor', cluster T10
`H2396G` — 'Hezekiah', cluster T8
`H2468` — 'Huldah', cluster T8
`H2477` — 'Halah', cluster T10
`H2518G` — 'Hilkiah', cluster T8
`H2518H` — 'Hilkiah', cluster T8
`H2537` — 'Hamutal', cluster T8
`H2743` — 'Haruz', cluster T8
`H2745` — 'Harhas', cluster T8
`H2754` — 'purse', cluster T12
`H2970J` — 'Jezaniah', cluster T8
`H3003H` — 'Jabesh', cluster T8
`H3040` — 'Jedidah', cluster T8
`H3059G` — 'Jehoahaz', cluster T8
`H3059H` — 'Jehoahaz', cluster T8
`H3060G` — 'Jehoash', cluster T8
`H3060H` — 'Jehoash', cluster T8
`H3075G` — 'Jehozabad', cluster T8
`H3077H` — 'Jehoiada', cluster T8
`H3078` — 'Jehoiachin', cluster T8
`H3082G` — 'Jonadab', cluster T8
`H3086` — 'Jehoaddan', cluster T8
`H3088I` — 'Joram', cluster T8
`H3089` — 'Jehosheba', cluster T8
`H3091I` — 'Joshua', cluster T8
`H3092J` — 'Jehoshaphat', cluster T8
`H3098G` — 'Joah', cluster T8
`H3099H` — 'Joahaz', cluster T8
`H3101I` — 'Joash', cluster T8
`H3107G` — 'Jozacar', cluster T8
`H3110G` — 'Johanan', cluster T8
`H3141H` — 'Joram', cluster T8
`H3141J` — 'Joram', cluster T8
`H3192` — 'Jotbah', cluster T10
`H3203` — 'Jecoliah', cluster T8
`H3239A` — 'Janoah', cluster T10
`H3371H` — 'Joktheel', cluster T10
`H3388` — 'Jerusha ', cluster T8
`H3414G` — 'Jeremiah', cluster T8
`H3458H` — 'Ishmael', cluster T8
`H3470A` — 'Isaiah', cluster T8
`H3526G` — "Washer's", cluster T10
`H3575` — 'Cuthah', cluster T10
`H3746` — 'Carite', cluster T11
`H4320G` — 'Micaiah', cluster T8
`H4338` — 'Mesha', cluster T8
`H4505` — 'Menahem', cluster T8
`H4519H` — 'Manasseh', cluster T8
`H4918G` — 'Meshullam', cluster T8
`H4922` — 'Meshullemeth', cluster T8
`H4933` — 'plunder', cluster M24
`H4977G` — 'Mattan', cluster T8
`H4983Q` — 'Mattaniah', cluster T8
`H5018` — 'Nebuzaradan', cluster T8
`H5026` — 'Nibhaz', cluster T7
`H5179` — 'Nehushta', cluster T8
`H5180` — 'Nehushtan', cluster T7
`H5224H` — '[Pharaoh] Neco', cluster T8
`H5268` — 'Nisroch', cluster T7
`H5283I` — 'Naaman', cluster T8
`H5370` — 'Nergal', cluster T7
`H5418G` — 'Nethaniah', cluster T8
`H5419` — 'Nathan-melech', cluster T8
`H5495` — 'Sur', cluster T10
`H5524` — 'Succoth-benoth', cluster T7
`H5538` — 'Silla', cluster T10
`H5554` — 'Sela', cluster T10
`H5576` — 'Sennacherib', cluster T8
`H5616` — 'Sepharvaim', cluster T10
`H5617` — 'Sepharvaim', cluster T10
`H5718G` — 'Adaiah', cluster T8
`H5729` — 'Eden', cluster T10
`H5755` — 'Ivvah', cluster T10
`H5761I` — 'Avvite', cluster T10
`H5838x` — 'Azariah', cluster T8
`H5907H` — 'Achbor', cluster T8
`H6048` — 'Anammelech', cluster T8
`H6122` — 'cunning', cluster M14
`H6222G` — 'Asaiah', cluster T8
`H6271G` — 'Athaliah', cluster T8
`H6305G` — 'Pedaiah', cluster T8
`H6322G` — 'Pul', cluster T8
`H6438G` — 'Corner [Gate]', cluster T10
`H6492` — 'Pekah', cluster T8
`H6494` — 'Pekahiah', cluster T8
`H6547L` — 'Pharaoh', cluster T8
`H6547Q` — 'Pharaoh [Neco]', cluster T8
`H6547T` — 'Pharaoh', cluster T8
`H6554` — 'Pharpar', cluster T10
`H6645` — 'Zibiah', cluster T8
`H6659H` — 'Zadok', cluster T8
`H6667H` — 'Zedekiah', cluster T8
`H6675` — 'filth', cluster M53
`H6746` — 'jar', cluster T12
`H6747` — 'dish', cluster T12
`H6811` — 'Zair', cluster T10
`H6846G` — 'Zephaniah', cluster T8
`H6861` — 'sack', cluster T12
`H7025` — 'Kir-hareseth', cluster T10
`H7143` — 'Kareah', cluster T8
`H7247H` — 'Riblah', cluster T10
`H7316H` — 'Rumah', cluster T10
`H7394H` — 'Rechab', cluster T8
`H7414K` — 'Ramah', cluster T10
`H7417A` — 'Rimmon', cluster T7
`H7425` — 'Remaliah', cluster T8
`H7526G` — 'Rezin', cluster T8
`H7530` — 'Rezeph', cluster T10
`H7644` — 'Shebna', cluster T8
`H7704H` — 'Field [of the Launderer]', cluster T10
`H7763G` — 'Shomer', cluster T8
`H7967G` — 'Shallum', cluster T8
`H7967H` — 'Shallum', cluster T8
`H8022` — 'Shalmaneser', cluster T8
`H8100` — 'Shimeath', cluster T8
`H8118` — 'Samaritan', cluster T11
`H8132` — 'to change', cluster M45
`H8227B` — 'Shaphan', cluster T8
`H8272G` — 'Sharezer', cluster T8
`H8304H` — 'Seraiah', cluster T8
`H8304I` — 'Seraiah', cluster T8
`H8407` — 'Tiglath-pileser', cluster T8
`H8466` — 'encampment', cluster T10
`H8515` — 'Telassar', cluster T10
`H8576` — 'Tanhumeth', cluster T8
`H8594` — 'security', cluster M19
`H8612` — 'Topheth', cluster T10
`H8616G` — 'Tikvah', cluster T8
`H8640` — 'Tirhakah', cluster T8
`H8662` — 'Tartak', cluster T7
`H0029J` — '`his father`', cluster T8
`H0031` — 'Abihud', cluster T8
`H0032H` — 'Abihail', cluster T8
`H0043` — 'Ebiasaph', cluster T8
`H0044G` — 'Abiezer', cluster T8
`H0051` — 'Abishur', cluster T8
`H0146H` — 'Addar', cluster T8
`H0179` — 'Obil', cluster T8
`H0198G` — 'Ulam', cluster T8
`H0198H` — 'Ulam', cluster T8
`H0207` — 'Ono', cluster T10
`H0208H` — 'Onam', cluster T8
`H0222H` — 'Uriel', cluster T8
`H0257` — 'Ahban', cluster T8
`H0261` — 'Ehud', cluster T8
`H0281J` — 'Ahijah', cluster T8
`H0281M` — 'Ahijah', cluster T8
`H0288I` — 'Ahimelech', cluster T8
`H0291` — 'Ahian', cluster T8
`H0387J` — 'Ethan', cluster T8
`H0443H` — 'Elzabad', cluster T8
`H0445H` — 'Elhanan', cluster T8
`H0446K` — 'Eliab', cluster T8
`H0447G` — 'Eliel', cluster T8
`H0447M` — 'Eliel', cluster T8
`H0453H` — 'Elihu', cluster T8
`H0453I` — 'Elihu', cluster T8
`H0461K` — 'Eliezer', cluster T8
`H0466` — 'Eliphelehu', cluster T8
`H0496` — 'Elead', cluster T8
`H0499J` — 'Eleazar', cluster T8
`H0508` — 'Elpaal', cluster T8
`H0511K` — 'Elkanah', cluster T8
`H0593` — 'Aniam', cluster T8
`H0609H` — 'Asa', cluster T8
`H0623H` — 'Asaph', cluster T8
`H0623K` — 'Asaph', cluster T8
`H0649` — 'Appaim', cluster T11
`H0675H` — 'Ezbon', cluster T8
`H0682A` — 'Azel', cluster T8
`H0684H` — 'Ozem', cluster T8
`H0758G` — 'Aram', cluster T8
`H0758K` — 'Aram [Maacah]', cluster T10
`H0767` — 'Oren', cluster T8
`H0771` — 'Ornan', cluster T8
`H0791` — '[Beth]-ashbea', cluster T10
`H0806` — 'Ashhur', cluster T8
`H0841` — 'Asharelah', cluster T8
`H0848` — 'Eshtaolite', cluster T11
`H0851` — 'Eshtemoa', cluster T10
`H0946` — 'Bunah', cluster T8
`H1004G` — 'Beth-[ashbea]', cluster T10
`H1011` — 'Beth-biri', cluster T10
`H1024` — 'Beth-marcaboth', cluster T10
`H1074` — 'Bocheru', cluster T8
`H1106H` — 'Bela', cluster T8
`H1141H` — 'Benaiah', cluster T8
`H1141J` — 'Benaiah', cluster T8
`H1141K` — 'Benaiah', cluster T8
`H1168H` — 'Baal', cluster T10
`H1177H` — 'Baal-hanan', cluster T8
`H1199` — 'Baara', cluster T8
`H1283H` — 'Beriah', cluster T8
`H1283I` — 'Beriah', cluster T8
`H1283J` — 'Beriah', cluster T8
`H1296H` — 'Berechiah', cluster T8
`H1296I` — 'Berechiah', cluster T8
`H1332` — 'Bithiah', cluster T8
`H1436I` — 'Gedaliah', cluster T8
`H1446H` — 'Gedor', cluster T10
`H1449` — 'Gederah', cluster T10
`H1451` — 'Gederite', cluster T11
`H1452` — 'Gederathite', cluster T11
`H1516K` — 'Ge', cluster T10
`H1559H` — 'Galal', cluster T8
`H1617I` — 'Gera', cluster T8
`H1647H` — 'Gershom', cluster T8
`H1734I` — 'Dodo', cluster T8
`H1737` — 'Dodai', cluster T8
`H1840H` — 'Daniel', cluster T8
`H1908H` — 'Hadad', cluster T8
`H1913G` — 'Hadoram', cluster T8
`H1927` — 'adornment', cluster M71
`H1938H` — 'Hodaviah', cluster T8
`H1968I` — 'Heman', cluster T8
`H2024` — 'Hara', cluster T10
`H2066H` — 'Zabad', cluster T8
`H2067I` — 'Zabdi', cluster T8
`H2068G` — 'Zabdiel', cluster T8
`H2069K` — 'Zebadiah', cluster T8
`H2117` — 'Zaza', cluster T8
`H2125` — 'Zizah', cluster T8
`H2139J` — 'Zaccur', cluster T8
`H2147M` — 'Zichri', cluster T8
`H2148A` — 'Zechariah', cluster T8
`H2241` — 'Zetham', cluster T8
`H2361G` — 'Hiram', cluster T8
`H2366A` — 'Hushim', cluster T8
`H2453G` — 'Hachmonite', cluster T11
`H2453H` — 'Hachmoni', cluster T8
`H2458` — 'Helah', cluster T8
`H2469H` — 'Heldai', cluster T8
`H2503G` — 'Helez', cluster T8
`H2526H` — 'Ham', cluster T10
`H2575B` — 'Hammath', cluster T8
`H2605H` — 'Hanan', cluster T8
`H2621H` — 'Hosah', cluster T8
`H2650G` — 'Huppim', cluster T8
`H2702` — 'Hazar-susim', cluster T10
`H2705` — 'Hazar-shual', cluster T10
`H2811I` — 'Hashabiah', cluster T8
`H2811J` — 'Hashabiah', cluster T8
`H2880` — 'Tibhath', cluster T10
`H3005` — 'Ibsam', cluster T8
`H3031` — 'Idbash', cluster T8
`H3038G` — 'Jeduthun', cluster T8
`H3038H` — 'Jeduthun', cluster T8
`H3043G` — 'Jediael', cluster T8
`H3043I` — 'Jediael', cluster T8
`H3047` — 'Jada', cluster T8
`H3076G` — 'Johanan', cluster T8
`H3077I` — 'Jehoiada', cluster T8
`H3083K` — 'Jonathan', cluster T8
`H3087` — 'Jehozadak', cluster T8
`H3097H` — 'Joab', cluster T8
`H3100J` — 'Joel', cluster T8
`H3100N` — 'Joel', cluster T8
`H3100O` — 'Joel', cluster T8
`H3101K` — 'Joash', cluster T8
`H3107H` — 'Jozabad', cluster T8
`H3107I` — 'Jozabad', cluster T8
`H3107J` — 'Jozabad', cluster T8
`H3130I` — 'Joseph', cluster T8
`H3135H` — 'Joash', cluster T8
`H3137` — 'Jokim', cluster T8
`H3151` — 'Jaziz', cluster T8
`H3155` — 'Izrahite', cluster T8
`H3157J` — 'Jezreel', cluster T8
`H3164` — 'Jahdiel', cluster T8
`H3165H` — 'Jehdeiah', cluster T8
`H3166G` — 'Jahaziel', cluster T8
`H3166H` — 'Jahaziel', cluster T8
`H3171G` — 'Jehiel', cluster T8
`H3171H` — 'Jehiel', cluster T8
`H3171I` — 'Jehiel', cluster T8
`H3172` — 'Jehieli', cluster T8
`H3181` — 'Jahmai', cluster T8
`H3189H` — 'Jahath', cluster T8
`H3210` — 'Jalon', cluster T8
`H3226H` — 'Jamin', cluster T8
`H3258G` — 'Jabez', cluster T10
`H3258H` — 'Jabez', cluster T8
`H3265` — 'Jair', cluster T8
`H3266J` — 'Jeush', cluster T8
`H3273G` — 'Jeiel', cluster T8
`H3273I` — 'Jeiel', cluster T8
`H3273P` — 'Jeiel', cluster T8
`H3325` — 'Izharite', cluster T8
`H3335H` — 'to form: potter', cluster T8
`H3396G` — 'Jerahmeel', cluster T8
`H3398` — 'Jarha', cluster T8
`H3400` — 'Jeriel', cluster T8
`H3404H` — 'Jerijah', cluster T8
`H3406G` — 'Jerimoth', cluster T8
`H3414H` — 'Jeremiah', cluster T8
`H3414I` — 'Jeremiah', cluster T8
`H3431` — 'Ishbah', cluster T8
`H3433` — 'Lehem', cluster T10
`H3434G` — 'Jashobeam', cluster T8
`H3457` — 'Ishma', cluster T8
`H3458I` — 'Ishmael', cluster T8
`H3460G` — 'Ishmaiah', cluster T8
`H3469J` — 'Ishi', cluster T8
`H3470H` — 'Jeshaiah', cluster T8
`H3485H` — 'Issachar', cluster T8
`H3492` — 'Jattir', cluster T10
`H3500I` — 'Jether', cluster T8
`H3500J` — 'Jether', cluster T8
`H3560` — 'Cun', cluster T10
`H3578` — 'Cozeba', cluster T10
`H3592` — 'Chidon', cluster T8
`H3612H` — 'Caleb', cluster T8
`H3613` — 'Caleb', cluster T10
`H3620H` — 'Chelub', cluster T8
`H3663` — 'Chenaniah', cluster T8
`H3850` — 'Lod', cluster T10
`H3902` — 'Lahmi', cluster T8
`H3922` — 'Lecah', cluster T8
`H3935` — 'Laadah', cluster T8
`H3949` — 'Likhi', cluster T8
`H4121` — 'Maharai', cluster T8
`H4140` — 'Molid', cluster T8
`H4249G` — 'Mahli', cluster T8
`H4317M` — 'Michael', cluster T8,T9
`H4409G` — 'Malluch', cluster T8
`H4506A` — 'Manahath', cluster T10
`H4506H` — 'Menuhoth', cluster T10
`H4586G` — 'Meunite', cluster T11
`H4587` — 'Meonothai', cluster T8
`H4601H` — '[Aram]-maacah', cluster T10
`H4601M` — 'Maacah', cluster T8
`H4601N` — 'Maacah', cluster T8
`H4601P` — 'Maacah', cluster T8
`H4619` — 'Maaz', cluster T8
`H4641G` — 'Maaseiah', cluster T8
`H4667` — 'hip', cluster T14
`H4700` — 'cymbal', cluster T12
`H4732G` — 'Mikloth', cluster T8
`H4732H` — 'Mikloth', cluster T8
`H4737` — 'Mikneiah', cluster T8
`H4762H` — 'Mareshah', cluster T8
`H4778` — 'Mered', cluster T8
`H4813H` — 'Miriam', cluster T8
`H4920` — 'Meshelemiah', cluster T8
`H4936` — 'Misham', cluster T8
`H4993G` — 'Mattithiah', cluster T8
`H4993H` — 'Mattithiah', cluster T8
`H5070I` — 'Nadab', cluster T8
`H5196` — 'Netaim', cluster T10
`H5292B` — 'Naarah', cluster T8
`H5295` — 'Naaran', cluster T10
`H5329` — 'to conduct', cluster M76
`H5418H` — 'Nethaniah', cluster T8
`H5540` — 'Seled', cluster T8
`H5565` — 'Semachiah', cluster T8
`H5598` — 'Sippai', cluster T8
`H5660G` — 'Abdi', cluster T8
`H5662J` — 'Obadiah', cluster T8
`H5662K` — 'Obadiah', cluster T8
`H5677I` — 'Eber', cluster T8
`H5717I` — 'Adiel', cluster T8
`H5721` — 'Adina', cluster T8
`H5724` — 'Adlai', cluster T8
`H5734G` — 'Adnah', cluster T8
`H5744J` — 'Obed', cluster T8
`H5806H` — 'Azubah', cluster T8
`H5811` — 'Azaz', cluster T8
`H5812G` — 'Azaziah', cluster T8
`H5813H` — 'Uzzi', cluster T8
`H5813I` — 'Uzzi', cluster T8
`H5815` — 'Aziel', cluster T8
`H5816I` — 'Uzziel', cluster T8
`H5818I` — 'Uzziah', cluster T8
`H5820J` — 'Azmaveth', cluster T8
`H5829K` — 'Ezer', cluster T8
`H5834` — 'Ezrah', cluster T8
`H5836` — 'Ezri', cluster T8
`H5837G` — 'Azriel', cluster T8
`H5840H` — 'Azrikam', cluster T8
`H5851` — 'Atarah', cluster T8
`H5862H` — 'Etam', cluster T10
`H5896H` — 'Ira', cluster T8
`H5901` — 'Iri', cluster T8
`H5917` — 'Achan', cluster T8
`H5988I` — 'Ammiel', cluster T8
`H5990` — 'Ammizabad', cluster T8
`H5992H` — 'Amminadab', cluster T8
`H6022H` — 'Amasai', cluster T8
`H6042G` — 'Unni', cluster T8
`H6069` — 'Anathoth', cluster T10
`H6081H` — 'Epher', cluster T8
`H6081I` — 'Epher', cluster T8
`H6084I` — 'Ophrah', cluster T8
`H6134` — 'Eker', cluster T8
`H6142` — 'Ikkesh', cluster T8
`H6147H` — 'Er', cluster T8
`H6222K` — 'Asaiah', cluster T8
`H6262G` — 'Attai', cluster T8
`H6273` — 'Othni', cluster T8
`H6431H` — 'Peleth', cluster T8
`H6450` — 'Pas-dammim', cluster T10
`H6469` — 'Peullethai', cluster T8
`H6560G` — 'Perez-uzza', cluster T10
`H6570` — 'Peresh', cluster T8
`H6678H` — 'Zobah', cluster T10
`H6753` — 'Hazzelelponi', cluster T8
`H6769H` — 'Zillethai', cluster T8
`H6874` — 'Zeri', cluster T8
`H6981G` — 'Kore', cluster T8
`H7027H` — 'Kish', cluster T8
`H7029` — 'Kishi', cluster T8
`H7145` — 'Korahite', cluster T8
`H7204` — 'Haroeh', cluster T8
`H7345` — 'Rehabiah', cluster T8
`H7410H` — 'Ram', cluster T8
`H7497H` — 'Raphaite', cluster T10
`H7501` — 'Rephael', cluster T8
`H7509I` — 'Rephaiah', cluster T8
`H7552J` — 'Rakem', cluster T8
`H7619G` — 'Shebuel', cluster T8
`H7687H` — 'Segub', cluster T8
`H7732H` — 'Shobal', cluster T8
`H7780` — 'Shophach', cluster T8
`H7803H` — 'Shuthelah', cluster T8
`H7842` — 'Shaharaim', cluster T8
`H7861` — 'Shitrai', cluster T8
`H7877` — 'Shiza', cluster T8
`H7883H` — 'Nile', cluster T10
`H7928H` — 'Shechem', cluster T8
`H7967M` — 'Shallum', cluster T8
`H7996` — 'Shallecheth', cluster T10
`H8013H` — 'Shelomoth', cluster T8
`H8018O` — 'Shelemiah', cluster T8
`H8019J` — 'Shelomoth', cluster T8
`H8039` — 'Shimeah', cluster T8
`H8043` — 'Shimeam', cluster T8
`H8049` — 'Shamhuth', cluster T8
`H8050I` — 'Shemuel', cluster T8
`H8060G` — 'Shammai', cluster T8
`H8060I` — 'Shammai', cluster T8
`H8070G` — 'Shemiramoth', cluster T8
`H8087H` — 'Shema', cluster T8
`H8087I` — 'Shema', cluster T8
`H8092H` — 'Shimea', cluster T8
`H8092I` — 'Shimea', cluster T8
`H8096K` — 'Shimei', cluster T8
`H8096O` — 'Shimei', cluster T8
`H8098F` — 'Shemaiah', cluster T8
`H8098G` — 'Shemaiah', cluster T8
`H8098I` — 'Shemaiah', cluster T8
`H8113I` — 'Shimri', cluster T8
`H8187` — 'Sheariah', cluster T8
`H8189H` — 'Shaaraim', cluster T10
`H8202K` — 'Shaphat', cluster T8
`H8203J` — 'Shephatiah', cluster T8
`H8206G` — 'Shuppim', cluster T8
`H8206H` — 'Shuppim', cluster T8
`H8289H` — 'Sharon', cluster T10
`H8289I` — 'Sharon', cluster T10
`H8290` — 'Sharonite', cluster T11
`H8304J` — 'Seraiah', cluster T8
`H8315` — 'Saraph', cluster T8
`H8329` — 'Sheresh', cluster T8
`H8348` — 'Sheshan', cluster T8
`H8439G` — 'Tola', cluster T8
`H8527` — 'pupil', cluster T14
`H8654` — 'Tirathite', cluster T11
`H0001H` — '[Huram]-abi', cluster T8
`H0029I` — 'Abijah', cluster T8
`H0029N` — 'Abijah', cluster T8
`H0066` — 'Abel-maim', cluster T10
`H0222I` — 'Uriel', cluster T8
`H0447N` — 'Eliel', cluster T8
`H0450I` — 'Eliada', cluster T8
`H0461L` — 'Eliezer', cluster T8
`H0478` — 'Elishaphat', cluster T8
`H0511N` — 'Elkanah', cluster T8
`H0568J` — 'Amariah', cluster T8
`H0568K` — 'Amariah', cluster T8
`H1134` — 'Ben-hail', cluster T8
`H1141L` — 'Benaiah', cluster T8
`H1141M` — 'Benaiah', cluster T8
`H1162H` — 'Boaz', cluster T12
`H1191H` — 'Baalath', cluster T10
`H1296J` — 'Berechiah', cluster T8
`H1390G` — 'Gibeah', cluster T10
`H1450` — 'Gederoth', cluster T10
`H1485` — 'Gurbaal', cluster T10
`H1516L` — '[Zephathah] Valley', cluster T10
`H1516M` — 'Valley [Gate]', cluster T10
`H1579` — 'Gimzo', cluster T10
`H1709G` — 'Fish [Gate]', cluster T10
`H1735` — 'Dodavahu', cluster T8
`H1913B` — 'Hadoram', cluster T8
`H2066M` — 'Zabad', cluster T8
`H2069M` — 'Zebadiah', cluster T8
`H2147N` — 'Zichri', cluster T8
`H2147O` — 'Zichri', cluster T8
`H2147P` — 'Zichri', cluster T8
`H2148H` — 'Zechariah', cluster T8
`H2148I` — 'Zechariah', cluster T8
`H2148L` — 'Zechariah', cluster T8
`H2148N` — 'Zechariah', cluster T8
`H2148O` — 'Zechariah', cluster T8
`H2148w` — 'Zechariah', cluster T8
`H2155H` — 'Zimmah', cluster T8
`H2226K` — 'Zerah', cluster T8
`H2311` — 'Hadlai', cluster T8
`H2361I` — 'Huram', cluster T8
`H2361J` — 'Hiram', cluster T8
`H2578` — 'Hamath-zobah', cluster T10
`H2608Q` — 'Hananiah', cluster T8
`H2641` — 'Hasrah', cluster T8
`H2810` — 'invention', cluster M14
`H2811L` — 'Hashabiah', cluster T8
`H2996` — 'Jabneh', cluster T10
`H3059I` — 'Ahaziah', cluster T8
`H3075I` — 'Jehozabad', cluster T8
`H3076J` — 'Jehohanan', cluster T8
`H3076K` — 'Jehohanan', cluster T8
`H3076L` — 'Johanan', cluster T8
`H3090` — 'Jehoshabeath', cluster T8
`H3094H` — 'Jehallelel', cluster T8
`H3098J` — 'Joah', cluster T8
`H3098K` — 'Joah', cluster T8
`H3098L` — 'Joah', cluster T8
`H3099G` — 'Joahaz', cluster T8
`H3099I` — 'Jehoahaz', cluster T8
`H3100Q` — 'Joel', cluster T8
`H3107K` — 'Jozabad', cluster T8
`H3107L` — 'Jozabad', cluster T8
`H3166J` — 'Jahaziel', cluster T8
`H3169G` — 'Jehizkiah', cluster T8
`H3171L` — 'Jehiel', cluster T8
`H3171M` — 'Jehiel', cluster T8
`H3189K` — 'Jahath', cluster T8
`H3232H` — 'Imnah', cluster T8
`H3253` — 'Ismachiah', cluster T8
`H3260` — 'Iddo', cluster T8
`H3273J` — 'Jeiel', cluster T8
`H3273K` — 'Jeiel', cluster T8
`H3273M` — 'Jeiel', cluster T8
`H3385` — 'Jeruel', cluster T10
`H3395M` — 'Jeroham', cluster T8
`H3406O` — 'Jerimoth', cluster T8
`H3442H` — 'Jeshua', cluster T8
`H3458J` — 'Ishmael', cluster T8
`H3458K` — 'Ishmael', cluster T8
`H3466G` — 'Jeshanah', cluster T10
`H3562G` — 'Conaniah', cluster T8
`H3751` — 'Carchemish', cluster T10
`H4287G` — 'Mahath', cluster T8
`H4287H` — 'Mahath', cluster T8
`H4318M` — 'Micah', cluster T8
`H4318N` — 'Micaiah', cluster T8
`H4322G` — 'Micaiah', cluster T8
`H4322H` — 'Micaiah', cluster T8
`H4509G` — 'Miniamin', cluster T8
`H4641H` — 'Maaseiah', cluster T8
`H4641I` — 'Maaseiah', cluster T8
`H4641J` — 'Maaseiah', cluster T8
`H4641K` — 'Maaseiah', cluster T8
`H4730` — 'censer', cluster T12
`H4918N` — 'Meshullam', cluster T8
`H4919G` — 'Meshillemoth', cluster T8
`H4983I` — 'Mattaniah', cluster T8
`H5184H` — 'Nahath', cluster T8
`H5224G` — 'Neco', cluster T8
`H5417L` — 'Nethanel', cluster T8
`H5417M` — 'Nethanel', cluster T8
`H5658K` — 'Abdon', cluster T8
`H5660H` — 'Abdi', cluster T8
`H5662N` — 'Obadiah', cluster T8
`H5662O` — 'Obadiah', cluster T8
`H5714I` — 'Iddo', cluster T8
`H5718J` — 'Adaiah', cluster T8
`H5731A` — 'Eden', cluster T8
`H5731G` — 'Eden', cluster T8
`H5734H` — 'Adnah', cluster T8
`H5744K` — 'Obed', cluster T8
`H5752G` — 'Oded', cluster T8
`H5752H` — 'Oded', cluster T8
`H5812I` — 'Azaziah', cluster T8
`H5838G` — 'Azariah', cluster T8
`H5838M` — 'Azariah', cluster T8
`H5838N` — 'Azariah', cluster T8
`H5838O` — 'Azariah', cluster T8
`H5838P` — 'Azariah', cluster T8
`H5838S` — 'Azariah', cluster T8
`H5838T` — 'Azariah', cluster T8
`H5838U` — 'Azariah', cluster T8
`H5838V` — 'Azariah', cluster T8
`H5838z` — 'Ahaziah', cluster T8
`H5840J` — 'Azrikam', cluster T8
`H5984G` — 'Meunite', cluster T11
`H6007` — 'Amasiah', cluster T8
`H6010H` — 'Valley [of Beracah]', cluster T10
`H6021H` — 'Amasa', cluster T8
`H6022J` — 'Amasai', cluster T8
`H6077` — 'Ophel', cluster T10
`H6085I` — 'Ephron', cluster T8
`H6163B` — 'Arabian', cluster T11
`H6214I` — 'Asahel', cluster T8
`H6437H` — 'Corner [Gate]', cluster T10
`H6732` — 'Ziz', cluster T10
`H6745` — 'pot', cluster T12
`H6787` — '[Mount] Zemaraim', cluster T10
`H6859` — 'Zephathah', cluster T10
`H6981H` — 'Kore', cluster T8
`H6999C` — 'incense-altar', cluster T12
`H7027I` — 'Kish', cluster T8
`H7183B` — 'attentive', cluster M41
`H7421` — 'Syrian', cluster T11
`H7755I` — 'Soco', cluster T8
`H7935I` — 'Shecaniah', cluster T8
`H7967N` — 'Shallum', cluster T8
`H8096Q` — 'Shimei', cluster T8
`H8098L` — 'Shemaiah', cluster T8
`H8098M` — 'Shemaiah', cluster T8
`H8116` — 'Shimrith', cluster T8
`H8196` — 'judgment', cluster M26
`H0112` — 'Iddo', cluster T8
`H0135` — 'Addan', cluster T10
`H0140` — 'Adonikam', cluster T8
`H0153` — 'force', cluster M23
`H0163` — 'Ahava', cluster T10
`H0221I` — 'Uri', cluster T8
`H0223H` — 'Uriah', cluster T8
`H0252` — 'brother', cluster M14,T8
`H0461M` — 'Eliezer', cluster T8
`H0461N` — 'Eliezer', cluster T8
`H0467K` — 'Eliphelet', cluster T8
`H0475I` — 'Eliashib', cluster T8
`H0475J` — 'Eliashib', cluster T8
`H0494H` — 'Elnathan', cluster T8
`H0494I` — 'Elnathan', cluster T8
`H0494J` — 'Elnathan', cluster T8
`H0499K` — 'Eleazar', cluster T8
`H0563` — 'lamb', cluster T13
`H0564I` — 'Immer', cluster T10
`H0670` — 'Persia', cluster T10
`H0740G` — 'Ariel', cluster T8
`H0756` — 'Erech', cluster T10
`H0783A` — 'Artaxerxes', cluster T8
`H0783B` — 'Artaxerxes', cluster T8
`H0896` — 'Babylonian', cluster T11
`H0902G` — 'Bigvai', cluster T8
`H1059` — 'bitterly', cluster M03
`H1114` — 'Bilshan', cluster T8
`H1131H` — 'Binnui', cluster T8
`H1196I` — 'Baanah', cluster T8
`H1271I` — 'Barzillai', cluster T8
`H1312` — 'Bishlam', cluster T8
`H1436A` — 'Gedaliah', cluster T8
`H1778` — 'to judge', cluster M26
`H1798` — 'ram', cluster T13
`H1867H` — 'Darius', cluster T8
`H1868G` — 'Darius', cluster T8
`H2148B` — 'Zechariah', cluster T8
`H2148S` — 'Zechariah', cluster T8
`H2216` — 'Zerubbabel', cluster T8
`H2252` — 'Habaiah', cluster T8
`H2292B` — 'Haggai', cluster T8
`H2323` — 'new', cluster M45
`H2582G` — 'Henadad', cluster T8
`H2870A` — 'Tabeel', cluster T8
`H2928H` — 'Telem', cluster T8
`H3063L` — 'Judah', cluster T8
`H3063N` — 'Judea', cluster T10
`H3076M` — 'Jehohanan', cluster T8
`H3107M` — 'Jozabad', cluster T8
`H3114H` — 'Joiarib', cluster T8
`H3129I` — 'Jonathan', cluster T8
`H3136A` — 'Jozadak', cluster T8
`H3136G` — 'Jozadak', cluster T8
`H3167` — 'Jahzeiah', cluster T8
`H3171O` — 'Jehiel', cluster T8
`H3246` — 'beginning', cluster M16
`H3273N` — 'Jeuel', cluster T8
`H3402G` — 'Jarib', cluster T8
`H3402H` — 'Jarib', cluster T8
`H3442G` — 'Jeshua', cluster T8
`H3442J` — 'Jeshua', cluster T8
`H3442K` — 'Jeshua', cluster T8
`H3442P` — 'Jeshua', cluster T8
`H3479` — 'Israel', cluster T8
`H3567` — 'Cyrus', cluster T8
`H3679` — 'Chaldean', cluster T11
`H3703` — 'Casiphia', cluster T10
`H3743` — 'Cherub', cluster T10
`H3879` — 'Levite', cluster T8
`H4558` — 'Mispar', cluster T8
`H4641L` — 'Maaseiah', cluster T8
`H4782G` — 'Mordecai', cluster T8
`H4822G` — 'Meremoth', cluster T8
`H4873` — 'Moses', cluster T8
`H4918O` — 'Meshullam', cluster T8
`H4918P` — 'Meshullam', cluster T8
`H4990G` — 'Mithredath', cluster T8
`H4990H` — 'Mithredath', cluster T8
`H5013` — 'to prophesy', cluster M43
`H5103G` — 'River', cluster T10
`H5129G` — 'Noadiah', cluster T8
`H5166G` — 'Nehemiah', cluster T8
`H5416K` — 'Nathan', cluster T8
`H5479` — 'Sotai', cluster T8
`H5642B` — 'to destroy', cluster M10
`H5714J` — 'Iddo', cluster T8
`H5830G` — 'Ezra', cluster T8
`H5831` — 'Ezra', cluster T8
`H5838L` — 'Azariah', cluster T8
`H5867B` — 'Elam', cluster T8
`H5962` — 'Elamite', cluster T11
`H6214J` — 'Asahel', cluster T8
`H6372I` — 'Phinehas', cluster T8
`H6402` — 'service', cluster M36
`H6514` — 'Peruda', cluster T8
`H6744` — 'to prosper', cluster M46
`H6841` — 'male goat', cluster T13
`H6934` — 'Kadmiel', cluster T8
`H6976I` — 'Hakkoz', cluster T8
`H7348A` — 'Rehum', cluster T8
`H7348B` — 'Rehum', cluster T8
`H7480` — 'Reelaiah', cluster T8
`H7597A` — 'Shealtiel', cluster T8
`H7678G` — 'Shabbethai', cluster T8
`H7801` — 'Susa', cluster T10
`H7935L` — 'Shecaniah', cluster T8
`H7967O` — 'Shallum', cluster T8
`H8098N` — 'Shemaiah', cluster T8
`H8098O` — 'Shemaiah', cluster T8
`H8115` — 'Samaria', cluster T10
`H8124` — 'Shimshai', cluster T8
`H8200` — 'to judge', cluster M63
`H8274G` — 'Sherebiah', cluster T8
`H8304L` — 'Seraiah', cluster T8
`H8339` — 'Sheshbazzar', cluster T8
`H8340` — 'Sheshbazzar', cluster T8
`H8370` — 'Shethar-bozenai', cluster T8
`H8521` — 'Tel-harsha', cluster T10
`H8528` — 'Tel-melah', cluster T10
`H8589` — 'fasting', cluster M21
`H8616H` — 'Tikvah', cluster T8
`H8674` — 'Tattenai', cluster T8
`H0114` — 'Addon', cluster T10
`H0223I` — 'Uriah', cluster T8
`H0435` — 'Elul', cluster T15
`H0475M` — 'Eliashib', cluster T8
`H0475N` — 'Eliashib', cluster T8
`H0475O` — 'Eliashib', cluster T8
`H0499M` — 'Eleazar', cluster T8
`H0548` — 'sure', cluster M62
`H0557H` — 'Amzi', cluster T8
`H0564J` — 'Immer', cluster T8
`H0566H` — 'Imri', cluster T8
`H0568N` — 'Amariah', cluster T8
`H0623I` — 'Asaph', cluster T8
`H0623J` — 'Asaph', cluster T8
`H0669I` — 'Ephraim [Gate]', cluster T10
`H0733I` — 'Arah', cluster T8
`H0942` — 'Bavvai', cluster T8
`H1019` — 'Beth-gilgal', cluster T10
`H1021` — 'Beth-haccherem', cluster T10
`H1049` — 'Beth-zur', cluster T10
`H1131K` — 'Binnui', cluster T8
`H1131L` — 'Binnui', cluster T8
`H1137L` — 'Bani', cluster T8
`H1137M` — 'Bani', cluster T8
`H1137N` — 'Bani', cluster T8
`H1137O` — 'Bani', cluster T8
`H1138G` — 'Bunni', cluster T8
`H1144J` — 'Benjamin', cluster T8
`H1152` — 'Besodeiah', cluster T8
`H1195I` — 'Baana', cluster T8
`H1229` — 'Bakbukiah', cluster T8
`H1263G` — 'Baruch', cluster T8
`H1295G` — '[Shelah] Pool', cluster T10
`H1296K` — 'Berechiah', cluster T8
`H1419B` — 'Haggedolim', cluster T8
`H1654` — 'Geshem', cluster T8
`H1658` — 'Gishpa', cluster T8
`H1769H` — 'Dibon', cluster T10
`H1806J` — 'Delaiah', cluster T8
`H1867G` — 'Darius', cluster T8
`H1941G` — 'Hodiah', cluster T8
`H2067J` — 'Zabdi', cluster T8
`H2068H` — 'Zabdiel', cluster T8
`H2139L` — 'Zaccur', cluster T8
`H2139N` — 'Zaccur', cluster T8
`H2140` — 'Zaccai', cluster T8
`H2147Q` — 'Zichri', cluster T8
`H2148U` — 'Zechariah', cluster T8
`H2148V` — 'Zechariah', cluster T8
`H2148X` — 'Zechariah', cluster T8
`H2182G` — 'Zanoah', cluster T10
`H2240H` — 'Zattu', cluster T8
`H2354I` — 'Hur', cluster T8
`H2407I` — 'Hattush', cluster T8
`H2446` — 'Hacaliah', cluster T8
`H2518K` — 'Hilkiah', cluster T8
`H2582H` — 'Henadad', cluster T8
`H2582I` — 'Henadad', cluster T8
`H2586H` — 'Hanun', cluster T8
`H2586I` — 'Hanun', cluster T8
`H2605K` — 'Hanan', cluster T8
`H2605N` — 'Hanan', cluster T8
`H2606` — '[Tower of] Hananel', cluster T10
`H2607J` — 'Hanani', cluster T8
`H2608G` — 'Hananiah', cluster T8
`H2608H` — 'Hananiah', cluster T8
`H2608J` — 'Hananiah', cluster T8
`H2608S` — 'Hananiah', cluster T8
`H2736` — 'Harhaiah', cluster T8
`H2739` — 'Harumaph', cluster T8
`H2766I` — 'Harim', cluster T8
`H2772` — 'Horonite', cluster T11
`H2806` — 'Hashbaddanah', cluster T8
`H2811M` — 'Hashabiah', cluster T8
`H2811N` — 'Hashabiah', cluster T8
`H2811O` — 'Hashabiah', cluster T8
`H2813G` — 'Hashabneiah', cluster T8
`H2813H` — 'Hashabneiah', cluster T8
`H2815H` — 'Hasshub', cluster T8
`H2815I` — 'Hasshub', cluster T8
`H2828H` — 'Hashum', cluster T8
`H2900I` — 'Tobiah', cluster T8
`H2926` — 'to cover', cluster M45
`H2929` — 'Talmon', cluster T8
`H3036` — 'Jadon', cluster T8
`H3037H` — 'Jaddua', cluster T8
`H3042H` — 'Jedaiah', cluster T8
`H3063I` — 'Judah', cluster T8
`H3063M` — 'Judah', cluster T8
`H3076O` — 'Jehohanan', cluster T8
`H3076Q` — 'Jehohanan', cluster T8
`H3100S` — 'Joel', cluster T8
`H3107P` — 'Jozabad', cluster T8
`H3107Q` — 'Jozabad', cluster T8
`H3110L` — 'Johanan', cluster T8
`H3111G` — 'Joiada', cluster T8
`H3111H` — 'Joiada', cluster T8
`H3113` — 'Joiakim', cluster T8
`H3156H` — 'Jezrahiah', cluster T8
`H3226I` — 'Jamin', cluster T8
`H3343` — 'Jekabzeel', cluster T10
`H3395J` — 'Jeroham', cluster T8
`H3414M` — 'Jeremiah', cluster T8
`H3442L` — 'Jeshua', cluster T8
`H3442N` — 'Jeshua', cluster T8
`H3442O` — 'Jeshua', cluster T8
`H3626G` — 'Col-hozeh', cluster T8
`H3662` — 'Chenani', cluster T8
`H3691` — 'Chislev', cluster T15
`H3715B` — 'Hakkephirim', cluster T10
`H3873` — 'Hallohesh', cluster T8
`H3968` — '[Tower of] the Hundred', cluster T10
`H4105H` — 'Mehetabel', cluster T8
`H4111H` — 'Mahalalel', cluster T8
`H4217G` — 'East [Gate]', cluster T10
`H4316I` — 'Mica', cluster T8
`H4318L` — 'Mica', cluster T8
`H4332H` — 'Mishael', cluster T8
`H4424` — 'Melatiah', cluster T8
`H4441H` — 'Malchijah', cluster T8
`H4441M` — 'Malchijah', cluster T8
`H4441N` — 'Malchijah', cluster T8
`H4441O` — 'Malchijah', cluster T8
`H4441P` — 'Malchijah', cluster T8
`H4441R` — 'Malchijah', cluster T8
`H4559` — 'Mispereth', cluster T8
`H4641P` — 'Maaseiah', cluster T8
`H4641Q` — 'Maaseiah', cluster T8
`H4641R` — 'Maaseiah', cluster T8
`H4641W` — 'Maaseiah', cluster T8
`H4811` — 'Meraiah', cluster T8
`H4898G` — 'Meshezabel', cluster T8
`H4898I` — 'Meshezabel', cluster T8
`H4918R` — 'Meshullam', cluster T8
`H4918S` — 'Meshullam', cluster T8
`H4918T` — 'Meshullam', cluster T8
`H4918Z` — 'Meshullam', cluster T8
`H4983G` — 'Mattaniah', cluster T8
`H4983O` — 'Mattaniah', cluster T8
`H4983P` — 'Mattaniah', cluster T8
`H4993J` — 'Mattithiah', cluster T8
`H5129H` — 'Noadiah', cluster T8
`H5149` — 'Nehum', cluster T8
`H5166H` — 'Nehemiah', cluster T8
`H5166I` — 'Nehemiah', cluster T8
`H5167` — 'Nahamani', cluster T8
`H5212` — 'Nisan', cluster T15
`H5483B` — 'Horse [Gate]', cluster T10
`H5571G` — 'Sanballat', cluster T8
`H5653H` — 'Abda', cluster T8
`H5718I` — 'Adaiah', cluster T8
`H5802` — 'Azbuk', cluster T8
`H5813K` — 'Uzzi', cluster T8
`H5813M` — 'Uzzi', cluster T8
`H5816L` — 'Uzziel', cluster T8
`H5818K` — 'Uzziah', cluster T8
`H5820K` — 'Azmaveth', cluster T10
`H5829I` — 'Ezer', cluster T8
`H5829J` — 'Ezer', cluster T8
`H5838W` — 'Azariah', cluster T8
`H5838X` — 'Azariah', cluster T8
`H5838Y` — 'Azariah', cluster T8
`H5867I` — 'Elam', cluster T8
`H5867J` — 'Elam', cluster T8
`H5869B` — 'Fountain [Gate]', cluster T10
`H5869G` — 'Fountain of [Drangons]', cluster T10
`H6042H` — 'Unni', cluster T8
`H6043G` — 'Anaiah', cluster T8
`H6055G` — 'Ananiah', cluster T8
`H6126H` — 'Akkub', cluster T8
`H6126J` — 'Akkub', cluster T8
`H6265` — 'Athaiah', cluster T8
`H6305K` — 'Pedaiah', cluster T8
`H6305M` — 'Pedaiah', cluster T8
`H6355H` — 'Pahath-moab', cluster T8
`H6355I` — 'Pahath-moab', cluster T8
`H6411A` — 'Pelaiah', cluster T8
`H6421` — 'Pelaliah', cluster T8
`H6454I` — 'Paseah', cluster T8
`H6542` — 'Persian', cluster T11
`H6551J` — 'Parosh', cluster T8
`H6583G` — 'Pashhur', cluster T8
`H6611I` — 'Pethahiah', cluster T8
`H6611J` — 'Pethahiah', cluster T8
`H6629H` — 'Sheep [Gate]', cluster T10
`H6659J` — 'Zadok', cluster T8
`H6659K` — 'Zadok', cluster T8
`H6659M` — 'Zadok', cluster T8
`H6667J` — 'Zedekiah', cluster T8
`H6727H` — 'Ziha', cluster T8
`H6764` — 'Zalaph', cluster T8
`H6976J` — 'Hakkoz', cluster T8
`H7042G` — 'Kelita', cluster T8
`H7183A` — 'attentive', cluster M41
`H7348G` — 'Rehum', cluster T8
`H7394I` — 'Rechab', cluster T8
`H7485` — 'Raamiah', cluster T8
`H7509J` — 'Rephaiah', cluster T8
`H7645H` — 'Shebaniah', cluster T8
`H7678H` — 'Shabbethai', cluster T8
`H7678I` — 'Shabbethai', cluster T8
`H7935M` — 'Shecaniah', cluster T8
`H7967Q` — 'Shallum', cluster T8
`H7968` — 'Shallum', cluster T8
`H8018I` — 'Shelemiah', cluster T8
`H8018J` — 'Shelemiah', cluster T8
`H8051J` — 'Shammua', cluster T8
`H8087J` — 'Shema', cluster T8
`H8098R` — 'Shemaiah', cluster T8
`H8098S` — 'Shemaiah', cluster T8
`H8098W` — 'Shemaiah', cluster T8
`H8203N` — 'Shephatiah', cluster T8
`H8274H` — 'Sherebiah', cluster T8
`H8442` — 'error', cluster M55
`H8574G` — '[Tower of] the Ovens', cluster T10
`H8577B` — 'Dragon', cluster T10
`H0005` — 'Abagtha', cluster T8
`H0012` — 'destruction', cluster M55
`H0013` — 'destruction', cluster M55
`H0032K` — 'Abihail', cluster T8
`H0091` — 'Agagite', cluster T8
`H0133` — 'Admatha', cluster T8
`H0143` — 'Adar', cluster T15
`H0432` — 'except', cluster T6
`H0597` — 'to compel', cluster M23
`H0635` — 'Esther', cluster T8
`H0903` — 'Bigtha', cluster T8
`H0904` — 'Bigthan', cluster T8
`H0968` — 'Biztha', cluster T8
`H1055` — 'palace', cluster M72
`H1896` — 'Hegai', cluster T8
`H1912` — 'India', cluster T10
`H1919` — 'Hadassah', cluster T8
`H2001` — 'Haman', cluster T8
`H2047` — 'Hathach', cluster T8
`H2060` — 'Vashti', cluster T8
`H2238` — 'Zeresh', cluster T8
`H2242` — 'Zethar', cluster T8
`H2726G` — 'Harbona', cluster T8
`H2726H` — 'Harbona', cluster T8
`H2887` — 'Tebeth', cluster T15
`H2971J` — 'Jair', cluster T8
`H3752` — 'Carkas', cluster T8
`H3771` — 'Carshena', cluster T8
`H4099` — 'Hammedatha', cluster T8
`H4104` — 'Mehuman', cluster T8
`H4462` — 'Memucan', cluster T8
`H4782H` — 'Mordecai', cluster T8
`H4825` — 'Meres', cluster T8
`H4826` — 'Marsena', cluster T8
`H5510` — 'Sivan', cluster T15
`H6599` — 'edict', cluster FLAG,T2
`H7027J` — 'Kish', cluster T8
`H8096U` — 'Shimei', cluster T8
`H8190` — 'Shaashgaz', cluster T8
`H8275` — 'scepter', cluster T12
`H8369` — 'Shethar', cluster T8
`H8657` — 'Teresh', cluster T8
`H8659J` — 'Tarshish', cluster T8
`H0336` — 'not', cluster T5
`H0347` — 'Job', cluster T8
`H0405` — 'burden', cluster M78
`H0453K` — 'Elihu', cluster T8
`H0464H` — 'Eliphaz', cluster T8
`H0562` — 'word', cluster M65
`H0660` — 'viper', cluster T13
`H1085` — 'Bildad', cluster T8
`H1292` — 'Barachel', cluster T8
`H1539` — 'skin', cluster T14
`H1623` — 'to scrape', cluster M23
`H1700` — 'cause', cluster M16
`H2230` — 'storm', cluster T13
`H2385` — 'lightning', cluster T13
`H2443` — 'hook', cluster T12
`H2862` — 'to seize', cluster M24
`H3224` — 'Jemimah', cluster T8
`H3712` — 'branch', cluster T13
`H3918` — 'lion', cluster T13
`H4221` — 'marrow', cluster T14
`H4300` — 'rod', cluster T12
`H4561` — 'discipline', cluster M15
`H4651` — 'refuse', cluster M30
`H4879` — 'error', cluster M55
`H4901` — 'bag/price', cluster T12
`H5076` — 'tossing', cluster M03
`H5243A` — 'to languish', cluster M24
`H5328` — 'flower', cluster T13
`H5587B` — 'disquietings', cluster FLAG,T2
`H5780J` — 'Uz', cluster T10
`H5848A` — 'to turn aside', cluster M11
`H5906` — 'Bear', cluster T13
`H5908` — 'spider', cluster T13
`H6053` — 'cloud', cluster T13
`H6079` — 'eyelid', cluster T14
`H6211A` — 'moth', cluster T13
`H6344` — 'thigh', cluster T14
`H6443` — 'jewel', cluster T12
`H6691` — 'Zophar', cluster T8
`H6761` — 'stumbling', cluster M77
`H6767B` — 'spear', cluster T12
`H6791` — 'thorn', cluster T13
`H7009` — 'adversary', cluster M06
`H7059` — 'to seize', cluster M24
`H7070J` — 'branch: shoulder', cluster T13,T14
`H7103` — 'Keziah', cluster T8
`H7163` — 'Keren-happuch', cluster T8
`H7176` — 'town', cluster T10
`H7410I` — 'Ram', cluster T8
`H7443` — 'ostrich', cluster T13
`H7482` — 'thunder', cluster T13
`H7483` — 'mane', cluster T14
`H7614G` — 'Sheba', cluster T8
`H7679` — 'to grow great', cluster M23
`H7717` — 'advocate', cluster T10
`H7722B` — 'devastation', cluster M55
`H7747` — 'Shuhite', cluster T11
`H7905` — 'spear', cluster T12
`H7929` — 'shoulder', cluster T14
`H8183` — 'storm', cluster T13
`H8235` — 'clearness', cluster M61
`H8417` — 'error', cluster M55
`H8485H` — 'Tema', cluster T10
`H8630` — 'to prevail', cluster M23
`H0047G` — 'mighty: ox', cluster T13
`H0047J` — 'mighty: angel', cluster M23
`H0190` — 'woe!', cluster M03
`H0760` — 'Aram-zobah', cluster T10
`H0814` — 'gift', cluster M39
`H1056` — '[Tophet of] Baca', cluster T10
`H1381` — 'Gebal', cluster T10
`H1534` — 'wheel', cluster T12
`H1627` — 'throat', cluster T14
`H1866` — 'swallow', cluster T13
`H2050` — 'to plot', cluster M06
`H2172` — 'melody', cluster M22
`H2270` — 'companion', cluster M44
`H2626` — 'mighty', cluster M23
`H2769` — 'Hermon', cluster T10
`H3053` — 'burden', cluster M78
`H3084` — 'Joseph', cluster T8
`H3293G` — 'Jaar', cluster T10
`H3401` — 'opponent', cluster M06
`H3446` — 'Isaac', cluster T8
`H3512B` — 'disheartened', cluster M20
`H3563B` — 'owl', cluster T13
`H3574` — 'prosperity', cluster M46
`H3597` — 'axe', cluster T12
`H3781` — 'axe', cluster T12
`H3833A` — 'lion', cluster T13
`H4039` — 'scroll', cluster T12
`H4210` — 'melody', cluster M22
`H4442` — 'Melchizedek', cluster T8
`H4455B` — 'jaw', cluster T14
`H4459` — 'tooth', cluster T14
`H4721` — 'assembly', cluster M44
`H4902H` — 'Meshech', cluster T10
`H5010` — 'to disown', cluster M06
`H5195` — 'plant', cluster T13
`H5222` — 'smitten', cluster M24
`H5434H` — 'Seba', cluster T10
`H5612B` — 'scroll', cluster T12
`H5765` — 'to act unjustly', cluster M12
`H5919` — 'viper', cluster T13
`H6010L` — 'Valley [of Topheth]', cluster T10
`H6073` — 'branch', cluster T13
`H6115` — 'coercion', cluster M24
`H6125` — 'pressure', cluster M01
`H6199` — 'destitute', cluster M09
`H6374` — 'tooth', cluster T14
`H6728` — 'wild beast', cluster T13
`H7398` — 'chariot', cluster T12
`H7438` — 'song', cluster M22
`H7691` — 'error', cluster M55
`H7790` — 'enemy', cluster M06
`H7862` — 'gift', cluster M39
`H7897` — 'garment', cluster T12
`H7959` — 'prosperity', cluster M46
`H8004` — 'Salem', cluster T10
`H8324` — 'enemy', cluster M06
`H8428` — 'to wound', cluster M10
`H8502` — 'perfection', cluster M61
`H0010` — 'destruction', cluster M55
`H0094` — 'Agur', cluster T8
`H0384H` — '`God`', cluster T8
`H2019` — 'crooked', cluster M14
`H2415` — 'branch', cluster T13
`H2475` — 'destruction', cluster M55
`H3348` — 'Jakeh', cluster T8
`H3513I` — 'to honor: many', cluster M71,T3
`H3514` — 'heaviness', cluster FLAG,T2
`H3677` — 'full moon', cluster T13
`H3783` — 'stumbling', cluster M77
`H3927` — 'Lemuel', cluster T8
`H3930` — 'throat', cluster T14
`H5099` — 'roaring', cluster M84
`H5244` — 'ant', cluster T13
`H5390` — 'kiss', cluster M05
`H5464` — 'rain', cluster T13
`H5914` — 'anklet', cluster T12
`H6104` — 'sluggishness', cluster M24
`H7063` — 'thorn', cluster T13
`H7258` — 'rest', cluster M33
`H7342I` — 'broad: arrogant', cluster M08
`H7915` — 'knife', cluster T12
`H8079` — 'lizard', cluster T13
`H0337` — 'woe!', cluster M03
`H0627` — 'collection', cluster M18
`H1947` — 'madness', cluster M66
`H1948` — 'madness', cluster M66
`H2070` — 'fly', cluster T13
`H3908` — 'charm', cluster M14
`H8623` — 'mighty', cluster M23
`H1174` — 'Baal-hamon', cluster T10
`H1313` — 'spice', cluster T12
`H1337` — 'Bath-rabbim', cluster T10
`H2159` — 'branch', cluster T13
`H2559` — 'to turn away', cluster M11
`H3842` — 'moon', cluster T13
`H4840` — 'spice', cluster T12
`H5339` — 'flower', cluster T13
`H5993` — 'Amminadib', cluster T8
`H6170` — 'bed', cluster T12
`H6247` — 'plate', cluster T12
`H6646` — 'gazelle', cluster T13
`H6677B` — 'necklace', cluster T12
`H7514` — 'to lean', cluster M19
`H0097` — 'Eglaim', cluster T10
`H0338` — 'wild beast', cluster T13
`H0500` — 'Elealeh', cluster T10
`H0740H` — 'Ariel', cluster T10
`H0879` — 'Beer-elim', cluster T10
`H0976` — 'testing', cluster M35
`H1070` — 'young camel', cluster T13
`H1078` — 'Bel', cluster T7
`H1357` — 'locust', cluster T13
`H1374` — 'Gebim', cluster T10
`H1408` — 'Fortune', cluster T7
`H1421` — 'reviling', cluster M53
`H1554` — 'Gallim', cluster T10
`H1720` — 'Dedanite', cluster T11
`H1746H` — 'Dumah', cluster T10
`H1775` — 'Dibon', cluster T10
`H1852` — 'curtain', cluster T12
`H1998` — 'sound', cluster M62
`H2041` — '[City of] Destruction', cluster T10
`H2148z` — 'Zechariah', cluster T8
`H2609` — 'Hanes', cluster T10
`H2630` — 'to hoard', cluster M46
`H2870B` — 'Tabeal', cluster T8
`H2922` — 'lamb', cluster T13
`H3000` — 'Jeberechiah', cluster T8
`H3068I` — '[Jerusalem of] the Lord', cluster T10
`H3244` — 'owl', cluster T13
`H3271` — 'to cover', cluster M45
`H3865` — 'Lud', cluster T8
`H3872` — 'Luhith', cluster T10
`H3919C` — 'Laishah', cluster T10
`H4088` — 'Madmenah', cluster T10
`H4122` — 'Maher-shalal-hash-baz', cluster T8
`H4507` — 'Destiny', cluster T7
`H4621` — 'axe', cluster T12
`H4654B` — 'ruin', cluster M55
`H4702` — 'bed', cluster T12
`H4757` — 'Merodach-baladan', cluster T8
`H4766` — 'abundance', cluster M46
`H4893A` — 'mutilation', cluster M53
`H4923` — 'devastation', cluster M55
`H4926` — 'hearing', cluster M41
`H4937B` — 'support', cluster M70
`H4938A` — 'support', cluster M70
`H5015B` — 'Nebo', cluster T7
`H5158G` — 'Brook', cluster T10
`H5249` — 'Nimrim', cluster T10
`H5285` — 'thorn bush', cluster T13
`H5297` — 'Memphis', cluster T10
`H5311` — 'storm', cluster T13
`H5364` — 'rope', cluster T12
`H5385` — 'burden', cluster M78
`H5436` — 'Sabeans', cluster T8
`H5448` — 'burden', cluster M78
`H5483A` — 'swallow', cluster T13
`H5580` — 'moth', cluster T13
`H5612I` — 'scroll: read', cluster T12
`H5623` — 'Sargon', cluster T8
`H5693` — 'crane', cluster T13
`H5697B` — 'Eglath-shelishiyah', cluster T10
`H5708` — 'filth', cluster M53
`H5719` — 'voluptuous', cluster M08
`H5790` — 'to help', cluster M45
`H5800G` — 'Forsaken', cluster T10
`H5953C` — 'to mock', cluster M08
`H6005` — 'Immanuel', cluster T8
`H6129` — 'crooked', cluster M14
`H6152A` — 'Arabia', cluster T10
`H6163A` — 'Arab', cluster T11
`H6183` — 'cloud', cluster T13
`H6322H` — 'Pul', cluster T10
`H6360` — 'hammer', cluster T12
`H6512` — 'mole', cluster T13
`H6559` — '[Mount] Perazim', cluster T10
`H6624` — 'Pathros', cluster T10
`H6733` — 'flower', cluster T13
`H6899` — 'collection', cluster M18
`H6957A` — 'cord', cluster M03,T12
`H7024A` — 'Kir', cluster T10
`H7070K` — 'branch: scales', cluster T13
`H7577` — 'chain', cluster T12
`H7610` — 'Shear-jashub', cluster T8
`H7641G` — 'Euphrates', cluster T10
`H7923` — 'bereavement', cluster M03
`H7975B` — 'Shiloah', cluster T10
`H8068` — 'thorn', cluster T13
`H8077G` — 'Desolate', cluster T10
`H8178B` — 'storm', cluster T13
`H8314B` — 'Seraph', cluster T9
`H8321A` — 'vine', cluster T13
`H8399` — 'destruction', cluster M55
`H8422H` — 'Tubal', cluster T10
`H8613` — 'burning-place', cluster T10
`H0223B` — 'Uriah', cluster T8
`H0246` — 'chains', cluster T12
`H0256H` — 'Ahab', cluster T8
`H0476L` — 'Elishama', cluster T8
`H0494K` — 'Elnathan', cluster T8
`H0501J` — 'Elasah', cluster T8
`H0528` — 'Amon', cluster T7
`H0564H` — 'Immer', cluster T8
`H0669J` — '[Mount] Ephraim', cluster T10
`H0778` — 'earth', cluster T10
`H0813H` — 'Ashkenaz', cluster T10
`H1010` — 'Beth-meon', cluster T10
`H1014` — 'Beth-gamul', cluster T10
`H1015` — 'Beth-diblathaim', cluster T10
`H1053J` — 'Heliopolis', cluster T10
`H1072` — 'young camel', cluster T13
`H1144L` — 'Benjamin [Gate]', cluster T10
`H1185` — 'Baalis', cluster T8
`H1224H` — 'Bozrah', cluster T10
`H1263J` — 'Baruch', cluster T8
`H1436G` — 'Gedaliah', cluster T8
`H1436J` — 'Gedaliah', cluster T8
`H1516S` — 'Valley', cluster T10
`H1587G` — 'Gemariah', cluster T8
`H1587H` — 'Gemariah', cluster T8
`H1601` — 'Goah', cluster T10
`H1619H` — 'Gareb', cluster T10
`H1719A` — 'Dedan', cluster T10
`H1806K` — 'Delaiah', cluster T8
`H1808` — 'branch', cluster T13
`H1955H` — 'Hoshaiah', cluster T8
`H2028G` — '[Topheth of] Slaughter', cluster T10
`H2262` — 'Habazziniah', cluster T8
`H2473H` — 'Holon', cluster T10
`H2518M` — 'Hilkiah', cluster T8
`H2601` — 'Hanamel', cluster T8
`H2608A` — 'Hananiah', cluster T8
`H2608M` — 'Hananiah', cluster T8
`H2608N` — 'Hananiah', cluster T8
`H2613` — 'profaneness', cluster M10c
`H2674K` — 'Hazor', cluster T10
`H2970G` — 'Jaazaniah', cluster T8
`H3065` — 'Jehudi', cluster T8
`H3077J` — 'Jehoiada', cluster T8
`H3081` — 'Jehucal', cluster T8
`H3083N` — 'Jonathan', cluster T8
`H3116` — 'Jucal', cluster T8
`H3122H` — 'Jonadab', cluster T8
`H3153` — 'Jezaniah', cluster T8
`H3204` — 'Jeconiah', cluster T8
`H3270H` — '[Sea of] Jazer', cluster T10
`H3306` — 'to breathe', cluster M25
`H3357` — 'precious', cluster M18
`H3376` — 'Irijah', cluster T8
`H3396I` — 'Jerahmeel', cluster T8
`H3414N` — 'Jeremiah', cluster T8
`H3570` — 'Cushi', cluster T8
`H3619` — 'basket', cluster T12
`H3659` — 'Coniah', cluster T8
`H3820B` — 'Leb', cluster T10
`H3866H` — 'Lydian', cluster T8
`H4086` — 'Madmen', cluster T10
`H4271` — 'Mahseiah', cluster T8
`H4321H` — 'Micaiah', cluster T8
`H4428K` — 'Milcom', cluster T7
`H4441S` — 'Malchiah', cluster T8
`H4508` — 'Minni', cluster T10
`H4641X` — 'Maaseiah', cluster T8
`H4641Y` — 'Maaseiah', cluster T8
`H4781` — 'Merodach', cluster T7
`H4835` — 'oppression', cluster M06
`H4850` — 'Merathaim', cluster T10
`H4977H` — 'Mattan', cluster T8
`H4996` — 'Thebes', cluster T10
`H5001` — 'to prophesy', cluster M43
`H5021` — 'Nebushazban', cluster T8
`H5371H` — 'Nergal-sar-ezer', cluster T8
`H5374` — 'Neriah', cluster T8
`H5418J` — 'Nethaniah', cluster T8
`H5494` — 'degenerate', cluster M57
`H5552` — 'branch', cluster T13
`H5562` — 'Samgar, Nebu-sar-sekim', cluster T8
`H5630` — 'armor', cluster T12
`H5655` — 'Abdeel', cluster T8
`H5663` — 'Ebed-melech', cluster T8
`H5809H` — 'Azzur', cluster T8
`H5837I` — 'Azriel', cluster T8
`H5838y` — 'Azariah', cluster T8
`H5857H` — 'Ai', cluster T10
`H6154A` — 'Arabia', cluster T10
`H6316H` — 'Put', cluster T10
`H6489` — 'Pekod', cluster T10
`H6547N` — 'Pharaoh', cluster T8
`H6547R` — 'Pharaoh', cluster T8
`H6547S` — 'Pharaoh [Hophra]', cluster T8
`H6548` — '[Pharaoh]-hophra', cluster T8
`H6583I` — 'Pashhur', cluster T8
`H6583J` — 'Pashhur', cluster T8
`H6583K` — 'Pashhur', cluster T8
`H6667K` — 'Zedekiah', cluster T8
`H6667L` — 'Zedekiah', cluster T8
`H6731B` — 'feather', cluster T14
`H6964H` — 'Kolaiah', cluster T8
`H6965A` — '[Leb]-kamai', cluster T10
`H7002` — 'incense', cluster T12
`H7156G` — 'Kiriathaim', cluster T10
`H7397A` — 'Rechabite', cluster T8
`H7967R` — 'Shallum', cluster T8
`H7967U` — 'Shallum', cluster T8
`H8018K` — 'Shelemiah', cluster T8
`H8018L` — 'Shelemiah', cluster T8
`H8018M` — 'Shelemiah', cluster T8
`H8018N` — 'Shelemiah', cluster T8
`H8098X` — 'Shemaiah', cluster T8
`H8098Y` — 'Shemaiah', cluster T8
`H8098Z` — 'Shemaiah', cluster T8
`H8203O` — 'Shephatiah', cluster T8
`H8284` — 'vine-row', cluster T13
`H8304M` — 'Seraiah', cluster T8
`H8304N` — 'Seraiah', cluster T8
`H8308` — 'to twist', cluster M57
`H8310` — 'Samgar, Nebu-sar-sekim', cluster T8
`H8347` — 'Babylon', cluster T10
`H8471` — 'Tahpanhes', cluster T10
`H3283` — 'ostrich', cluster T13
`H5206` — 'filth', cluster M53
`H7612` — 'devastation', cluster M55
`H0170` — 'Oholah', cluster T8
`H0172` — 'Oholibah', cluster T8
`H0187H` — 'Uzal', cluster T10
`H0417` — 'hail', cluster T13
`H0473H` — 'Elishah', cluster T10
`H0657B` — 'soles', cluster T14
`H0719` — 'Arvad', cluster T10
`H0741` — 'altar', cluster T12
`H0941` — 'Buzi', cluster T8
`H0965` — 'lightning', cluster T13
`H1004I` — 'Beth-[togarmah]', cluster T10
`H1117` — 'Bamah', cluster T10
`H1141R` — 'Benaiah', cluster T8
`H1304B` — 'gem', cluster T12
`H1380` — 'Gebal', cluster T10
`H1463H` — 'Gog', cluster T10
`H1516N` — '[Hamon-gog] Valley', cluster T10
`H1516O` — 'Valley', cluster T10
`H1575` — 'Gamaddim', cluster T10
`H1586G` — 'Gomer', cluster T8
`H1689` — 'Riblah', cluster T10
`H1997` — 'Hamonah', cluster T10
`H2051` — 'casks', cluster T10
`H2362` — 'Hauran', cluster T10
`H2428B` — 'Helech', cluster T10
`H2463` — 'Helbon', cluster T10
`H2629` — 'to muzzle', cluster M53
`H2703` — 'Hazar-enan', cluster T10
`H2855` — 'Hethlon', cluster T10
`H2970H` — 'Jaazaniah', cluster T8
`H2970I` — 'Jaazaniah', cluster T8
`H3068H` — 'The Lord', cluster T10
`H3168H` — 'Ezekiel', cluster T8
`H3314` — 'splendor', cluster M71
`H3520A` — 'glorious', cluster M71
`H3529` — 'Chebar', cluster T10
`H3552` — 'Libya', cluster T10
`H4031H` — 'Magog', cluster T10
`H4358` — 'perfection', cluster M61
`H4769` — 'resting', cluster M33
`H4833` — 'mud', cluster T13
`H4892` — 'destruction', cluster M55
`H4902I` — 'Meshech', cluster T10
`H5078` — 'gift', cluster M39
`H5083` — 'gift', cluster M39
`H5158M` — 'Brook', cluster T10
`H5204` — 'wailing', cluster M03
`H5482` — 'Syene', cluster T10
`H5500` — 'to scrape', cluster M23
`H5621` — 'thorn', cluster T13
`H5674G` — '[Valley of] the Travelers', cluster T10
`H5809I` — 'Azzur', cluster T8
`H5882` — 'Eneglaim', cluster T10
`H6410J` — 'Pelatiah', cluster T8
`H6713` — 'Sahar', cluster T10
`H6904` — 'battering-ram', cluster T13
`H6970` — 'Koa', cluster T10
`H7070I` — 'branch: measuring rod', cluster T12
`H7070L` — 'branch: calamus', cluster T13
`H7083` — 'pot', cluster T12
`H7159` — 'to cover', cluster M45
`H7221` — 'beginning', cluster M16
`H7269` — 'quivering', cluster M01
`H7419` — 'refuse', cluster M30
`H7484H` — 'Raamah', cluster T10
`H7772` — 'Shoa', cluster T10
`H7986` — 'imperious', cluster M08
`H8033H` — '[Jerusalem] Is There', cluster T10
`H8227G` — 'Shaphan', cluster T8
`H8240B` — 'hook', cluster T12
`H8383` — 'toil', cluster M24
`H8422I` — '[Meshech]-Tubal', cluster T10
`H8425H` — '[Beth]-togarmah', cluster T10
`H8512` — 'Tel-abib', cluster T10
`H8542` — 'Tammuz', cluster T7
`H8559J` — 'Tamar', cluster T10
`H8619` — 'trumpet', cluster T12
`H0558J` — 'Amaziah', cluster T8
`H1462B` — 'locust', cluster T13
`H2038` — 'Harmon', cluster T10
`H3594` — 'Kiyyun', cluster T7
`H3641B` — 'Calneh', cluster T10
`H5158K` — 'Brook', cluster T10
`H5522` — 'Sikkuth', cluster T7
`H6160H` — '[Brook of] the Arabah', cluster T10
`H6793A` — 'hook', cluster T12
`H7161B` — 'Karnaim', cluster T10
`H1462A` — 'locust', cluster T13
`H6393` — 'iron', cluster T12
`H2265` — 'Habakkuk', cluster T8
`H3572` — 'Cushan', cluster T10
`H4294I` — 'tribe: arrow', cluster T12
`H6127` — 'to twist', cluster M57
`H0568O` — 'Amariah', cluster T8
`H1436H` — 'Gedaliah', cluster T8
`H2396K` — 'Hezekiah', cluster T8
`H3569H` — 'Cushi', cluster T8
`H6846H` — 'Zephaniah', cluster T8
`H2292A` — 'Haggai', cluster T8
`H3091J` — 'Joshua', cluster T8
`H7597B` — 'Shealtiel', cluster T8
`H0264` — 'brotherhood', cluster M44
`H0682B` — 'Azal', cluster T10
`H1144M` — '[Gate of] Benjamin', cluster T10
`H1296L` — 'Berechiah', cluster T8
`H1910` — 'Hadad-rimmon', cluster T10
`H2148v` — 'Zechariah', cluster T8
`H2256C` — 'union', cluster M44
`H2317` — 'Hadrach', cluster T10
`H2469G` — 'Heldai', cluster T8
`H2494` — 'Helem', cluster T8
`H2581` — 'Hen', cluster T8
`H2900J` — 'Tobijah', cluster T8
`H2977H` — 'Josiah', cluster T8
`H3048J` — 'Jedaiah', cluster T8
`H4614` — 'burden', cluster M78
`H6434` — 'Corner', cluster T10
`H6674` — 'filthy', cluster M53
`H6804` — 'pipe', cluster T12
`H6846I` — 'Zephaniah', cluster T8
`H7278` — 'Regem-melech', cluster T8
`H7417G` — 'Rimmon', cluster T10
`H7627` — 'Shebat', cluster T15
`H8272H` — 'Sharezer', cluster T8
`H4401` — 'Malachi', cluster T8
`H0761G` — 'Aramean', cluster T11
`H3057` — 'Judahite wife', cluster T11
`G0007G` — 'Abijah', cluster T8
`G0284` — 'Amminadab', cluster T8
`G0300` — 'Amos', cluster T8
`G0760` — 'Asaph', cluster T8
`G0881` — 'Ahaz', cluster T8
`G1003` — 'Boaz', cluster T8
`G1478` — 'Hezekiah', cluster T8
`G2074` — 'Hezron', cluster T8
`G2196` — 'Zerah', cluster T8
`G2216H` — 'Zerubbabel', cluster T8
`G2283` — 'Tamar', cluster T8
`G2488` — 'Jotham', cluster T8
`G2496` — 'Joram', cluster T8
`G2498` — 'Jehoshaphat', cluster T8
`G3128H` — 'Manasseh', cluster T8
`G3476` — 'Nahshon', cluster T8
`G3604` — 'Uzziah', cluster T8
`G4477` — 'Rahab', cluster T8
`G4497` — 'Rehoboam', cluster T8
`G4503` — 'Ruth', cluster T8
`G4528H` — 'Shealtiel', cluster T8
`G5329` — 'Perez', cluster T8
`G5601` — 'Obed', cluster T8
`G3496` — 'Neapolis', cluster T10
`G4565` — 'Sharon', cluster T10
`H3846` — 'Libnite', cluster T11
`H4250` — 'Mahlite', cluster T11
`H4354` — 'Machirite', cluster T11
`G1045` — 'Gad', cluster T8
`G4502` — 'Reuben', cluster T8
`H4077` — 'Mede', cluster T11

<a id="exception-backfill-code-with-an-activeclustered-sibling"></a>
## Exception -- backfill code with an active/clustered sibling

`H8088A` — 'sound', cluster M62
`H3724A` — 'ransom', cluster T2
`H2048A` — 'to mock', cluster M08
`H5607A` — 'mockery', cluster M08
`H8178A` — 'shuddering', cluster M01
`H3856A` — 'to languish', cluster M24
`H1350A` — 'to redeem: redeem', cluster T3
`H5254G` — 'to test', cluster M35
`H4148G` — 'discipline', cluster M16
`H8210G` — 'to pour: pour', cluster T3
`H7323G` — 'to run: run', cluster T3
`G5456G` — 'voice/sound: voice', cluster T2
`H3867A` — 'to join', cluster T3
`H3898A` — 'to fight', cluster T3
`H4869A` — 'high refuge', cluster T2
`H5183A` — 'quietness', cluster M33
`H6601A` — 'to open wide', cluster T3
`H7067G` — 'Jealous [God]', cluster FLAG,M18
`H3925G` — 'to learn: teach', cluster T3
`H4654A` — 'ruin', cluster M55
`H5258A` — 'to pour', cluster T3
`H7032G` — 'voice: sound', cluster M84
`H8186A` — 'horror', cluster M01
`H8438A` — 'worm', cluster T13
`H0430G` — 'God', cluster T7
`H0776G` — 'land: country/planet', cluster T10
`H0935P` — 'to come [in]: bring', cluster T3
`H1004B` — 'house: home', cluster T2
`H1004Q` — 'house: temple', cluster T10
`H1121G` — 'son: descendant/people', cluster T2
`H1697N` — 'word: portion', cluster T2
`H1840G` — 'Daniel', cluster T2
`H1964H` — 'temple: palace', cluster T2
`H2233H` — 'seed: children', cluster T2
`H2608T` — 'Hananiah', cluster T2
`H3063G` — 'Judah', cluster T11
`H3117J` — 'day: daily', cluster T2
`H3956H` — 'tongue: language', cluster T2
`H4332I` — 'Mishael', cluster T2
`H4428G` — 'king', cluster M72
`H4480A` — 'from', cluster T2
`H5612H` — 'scroll: book', cluster T12
`H5838Z` — 'Azariah', cluster T2
`H6440G` — 'face: before', cluster T14
`H7227B` — 'chief', cluster T2
`H2235A` — 'vegetable', cluster T2
`H2235B` — 'vegetable', cluster T2
`H3117G` — 'day', cluster T2
`H4325G` — 'water', cluster T13
`H5375G` — 'to lift: raise', cluster T3
`H5973A` — 'with', cluster T2
`H7218A` — 'head', cluster T14
`H0746B` — 'Arioch', cluster T8
`H2006A` — 'if', cluster T6
`H2006B` — 'therefore', cluster T6
`H2492B` — 'to dream', cluster T3
`H4070B` — 'dwelling', cluster T2
`H7761H` — 'to set: put/give', cluster T3
`H8421I` — 'to return: reply', cluster T3
`H1247I` — 'son: type of', cluster T2
`H2608B` — 'Hananiah', cluster T8
`H5094A` — 'light', cluster T2
`H5642A` — 'to hide', cluster M20
`H6903G` — 'before', cluster T2
`H0772H` — 'earth: inferior', cluster T10
`H0772I` — 'earth: planet', cluster T10
`H1888B` — 'behold!', cluster T2
`H6966G` — 'to stand: rise', cluster T3
`H8523B` — 'third', cluster T2
`H1888A` — 'behold', cluster T2
`H2818A` — 'to need', cluster T3
`H0772G` — 'earth: soil', cluster T13
`H1965H` — 'temple: palace', cluster T2
`H4070A` — 'dwelling', cluster T2
`H5415G` — 'to give: give', cluster T3
`H6211B` — 'grass', cluster T13
`H7032H` — 'voice', cluster M84
`H8421G` — 'to return: return', cluster M11
`H1247J` — 'son: son', cluster T2
`H1965G` — 'temple', cluster T2
`H4076G` — 'Mede', cluster T10
`H6537A` — 'to divide', cluster T3
`H6537B` — 'half', cluster T2
`H8523A` — 'third', cluster T2
`H1868H` — 'Darius', cluster T8
`H5103H` — 'river', cluster T10
`H6966H` — 'to stand: raise', cluster T3
`H0120G` — 'man', cluster T8
`H0310A` — 'after', cluster T2
`H0352A` — 'ram', cluster T13
`H0505G` — 'thousand', cluster T2
`H0657A` — 'end', cluster T2
`H0776H` — 'land: soil', cluster T13
`H0859A` — 'you [m.s.]', cluster T2
`H0996G` — 'between', cluster T2
`H1121A` — 'son: child', cluster T2
`H1167J` — 'master: owning', cluster T2
`H2416C` — 'living thing', cluster M25
`H3220H` — 'sea: west', cluster T2
`H3499A` — 'remainder', cluster T2
`H3588A` — 'for', cluster T6
`H4074H` — 'Media', cluster T10
`H4150G` — 'meeting: time appointed', cluster T2
`H4217H` — 'east', cluster T2
`H5045H` — 'south', cluster T10
`H5375M` — 'to lift: look', cluster T3
`H5640A` — 'to close', cluster T3
`H5867A` — 'Elam', cluster T10
`H5869A` — 'eye', cluster T14
`H5927G` — 'to ascend: rise', cluster T3
`H6440H` — 'face', cluster T14
`H6440J` — 'face: surface', cluster T14
`H6643A` — 'beauty', cluster T2
`H6743B` — 'to prosper', cluster M46
`H6828G` — 'north', cluster T10
`H7161A` — 'horn', cluster T2
`H7223G` — 'first', cluster T2
`H8163B` — 'he-goat', cluster T2
`H8478H` — 'underneath: instead', cluster T2
`H0001G` — 'father', cluster T2
`H0376G` — 'man', cluster T8
`H0376I` — 'man: anyone', cluster T2
`H0410G` — 'God', cluster T7
`H1867I` — 'Darius', cluster T8
`H1980I` — 'to go: walk', cluster T3
`H2022G` — 'mountain: mount', cluster T10
`H2742C` — 'trench', cluster T2
`H3068G` — 'LORD', cluster T7
`H3117L` — 'day: today', cluster T2
`H3318H` — 'to come out: send', cluster T3
`H3318O` — 'to come out: speak', cluster T3
`H3414L` — 'Jeremiah', cluster T8
`H3615G` — 'to end: finish', cluster T3
`H3772I` — 'to cut: eliminate', cluster T3
`H4074I` — 'Mede', cluster T10
`H4503G` — 'grain offering', cluster M36
`H4639K` — 'deed', cluster T2
`H4714G` — 'Egypt', cluster T11
`H5307N` — 'to fall: presenting', cluster T3
`H5892B` — 'city', cluster T11
`H7620I` — 'week', cluster T2
`H7673A` — 'to cease', cluster T3
`H7725H` — 'to return: rescue', cluster T3
`H8033G` — 'there', cluster T2
`H8478G` — 'underneath: under', cluster T2
`H0518B` — 'if: except', cluster T6
`H0905H` — 'alone', cluster T2
`H1540H` — 'to reveal: reveal', cluster T3
`H2320G` — 'month', cluster T2
`H3254G` — 'to add: again', cluster T3
`H3588B` — 'that if: except', cluster T6
`H3709G` — 'palm', cluster T14
`H3899G` — 'food', cluster T2
`H4317Q` — 'Michael', cluster T8,T9
`H4759A` — 'vision', cluster T2
`H5104H` — 'river', cluster T10
`H5178A` — 'bronze', cluster T2
`H6310G` — 'lip', cluster T14
`H6605A` — 'to open', cluster T3
`H6635H` — 'army: war', cluster T2
`H6963H` — 'voice: sound', cluster T2
`H7136A` — 'to meet', cluster T3
`H7223I` — 'first: chief', cluster T2
`H0068G` — 'stone', cluster T12
`H0123G` — 'Edom', cluster T10
`H0127G` — 'land: soil', cluster T13
`H0168G` — 'tent', cluster T10
`H0410K` — 'god', cluster T7
`H0430J` — 'gods', cluster T2
`H0802G` — 'woman', cluster T8
`H0905J` — 'alone: besides', cluster T2
`H1121I` — 'son: type of', cluster T2
`H1323G` — 'daughter', cluster T2
`H2388J` — 'to strengthen: prevail over', cluster M23
`H2505A` — 'to divide', cluster T3
`H3220G` — 'sea', cluster T13
`H3569G` — 'Cushite', cluster T11
`H3701G` — 'silver: money', cluster T12
`H3835A` — 'to whiten', cluster T3
`H4124G` — 'Moab', cluster T11
`H4924B` — 'fatness', cluster M46
`H5257A` — 'libation', cluster T2
`H5307J` — 'to fall: kill', cluster T3
`H5414O` — 'to give: give [marriage]', cluster T3
`H6213J` — 'to make: [do]', cluster T3
`H6571B` — 'horseman', cluster T2
`H7223H` — 'first: previous', cluster T2
`H7225H` — 'first: best', cluster T2
`H7393G` — 'chariot', cluster T12
`H7628A` — 'captivity', cluster T2
`H7725L` — 'to return: refuse', cluster T3
`H7760H` — 'to set: put', cluster T3
`H7971K` — 'to send: reach', cluster T3
`H8210I` — 'to pour: build siege mound', cluster T3
`H1980M` — 'to go: journey', cluster T3
`H2094A` — 'to shine', cluster T3
`H2416A` — 'alive', cluster M25
`H2416E` — 'life', cluster M25
`H2975H` — 'stream', cluster T2
`H3225G` — 'right', cluster T2
`H5975H` — 'to stand: appoint', cluster T3
`H7751A` — 'to rove', cluster T3
`H8040G` — 'left', cluster T2
`H8193J` — 'lip: shore', cluster T14
`H1709H` — 'fish', cluster T13
`H1980K` — 'to go: come!', cluster T3
`H1980L` — 'to go: continue', cluster T3
`H5307I` — 'to fall: allot', cluster T3
`H5414N` — 'to give: pay', cluster T3
`H5591A` — 'tempest', cluster T2
`H7126G` — 'to present: come', cluster T3
`H7901G` — 'to lie down: lay down', cluster T3
`H8659H` — 'Tarshish', cluster T10
`H0990G` — 'belly: abdomen', cluster T2
`H1530H` — 'heap: wave', cluster T2
`H1644G` — 'to drive out: drive out', cluster T3
`H1964G` — 'temple', cluster T2
`H5488H` — 'reed', cluster T2
`H5869H` — 'eye: seeing', cluster T14
`H5927H` — 'to ascend: establish', cluster T3
`H7723H` — 'vanity: vain', cluster T2
`H1870G` — 'way: conduct', cluster M76
`H3678G` — 'throne', cluster M72
`H6629G` — 'flock', cluster T13
`H6996A` — 'small', cluster T2
`H0127H` — 'land: country', cluster T2
`H3651C` — 'so', cluster T2
`H6924G` — 'front: east', cluster T2
`H8438B` — 'worm', cluster T13
`H0518A` — 'if', cluster T6
`H0738B` — 'lion', cluster T13
`H1167H` — 'master: husband', cluster T2
`H2205G` — 'old: elder', cluster T2
`H3100T` — 'Joel', cluster T8
`H3833C` — 'lion', cluster T13
`H4057B` — 'wilderness', cluster T10
`H5271A` — 'youth', cluster T2
`H6086H` — 'tree', cluster T13
`H7105A` — 'harvest', cluster T2
`H7704G` — 'land: country', cluster T10
`H8047G` — 'horror: destroyed', cluster M01
`H8127G` — 'tooth', cluster T14
`H0197J` — 'Portico', cluster T2
`H0251I` — 'brother: compatriot', cluster T2
`H0899B` — 'garment', cluster T12
`H1250A` — 'grain', cluster T2
`H1588M` — 'garden', cluster T2
`H1870L` — 'way: journey', cluster T2
`H2205H` — 'old', cluster T2
`H2346G` — 'wall', cluster T2
`H3243J` — 'suckling-baby', cluster T2
`H3618G` — 'daughter-in-law: bride', cluster T2
`H5414M` — 'to give: cry out', cluster T3
`H5731B` — 'Eden', cluster T10
`H6186A` — 'to arrange', cluster T3
`H6931G` — 'eastern', cluster T2
`H7130G` — 'entrails: among', cluster T14
`H7218I` — 'head: top', cluster T14
`H7699A` — 'breast', cluster T2
`H7704M` — 'field', cluster T10
`H0859D` — 'you [m.p.]', cluster T2
`H1366G` — 'border: boundary', cluster T2
`H1389I` — 'hill', cluster T10
`H2742B` — 'decision', cluster T3
`H3092K` — '[Valley of] Jehoshaphat', cluster T10
`H5066G` — 'to approach: approach', cluster T3
`H5158I` — '[Shittim] Valley', cluster T10
`H6010N` — 'Valley [of Kidron]', cluster T10
`H6010R` — 'valley', cluster T10
`H6721H` — 'Sidon', cluster T10
`H7851H` — '[Valley of] Shittim', cluster T2
`H8210H` — 'to pour: kill', cluster T3
`H8248G` — 'to water: watering', cluster T3
`H0251G` — 'brother: male-sibling', cluster T2
`H0349A` — 'how?', cluster T2
`H0996H` — 'between: among', cluster T2
`H1004M` — 'house: household', cluster T2
`H3130G` — 'Joseph', cluster T8
`H3423H` — 'to possess: take', cluster T3
`H3669A` — 'Canaanite', cluster T11
`H3899H` — 'food: bread', cluster T2
`H5045G` — 'Negeb', cluster T10
`H5553H` — 'crag', cluster T10
`H5662R` — 'Obadiah', cluster T8
`H6215H` — 'Esau', cluster T11
`H6215I` — '[Mount] Esau', cluster T10
`H6412A` — 'survivor', cluster T2
`H6735A` — 'envoy', cluster T2
`H6965J` — 'to arise: attack', cluster T3
`H6996B` — 'small', cluster T2
`H8179G` — 'gate', cluster T12
`H8487H` — 'Teman', cluster T10
`H0271G` — 'Ahaz', cluster T8
`H0392G` — 'Achzib', cluster T10
`H1516R` — 'valley', cluster T10
`H1540I` — 'to reveal: uncover', cluster T3
`H1540K` — 'to reveal: remove', cluster T3
`H3147H` — 'Jotham', cluster T8
`H3169H` — 'Hezekiah', cluster T8
`H3247H` — 'foundation', cluster T2
`H4318K` — 'Micah', cluster T8
`H4762G` — 'Mareshah', cluster T10
`H7225G` — 'first: beginning', cluster T2
`H8577A` — 'jackal', cluster T13
`H0518I` — 'if: surely yes', cluster T6
`H1644H` — 'to drive out: divorce', cluster T3
`H1699A` — 'pasture', cluster T10
`H2256D` — 'destruction', cluster M55
`H2256M` — 'cord', cluster M03,T12
`H3162A` — 'unitedness', cluster T2
`H4496H` — 'resting', cluster M33
`H5375N` — 'to lift: loud', cluster T3
`H6677A` — 'neck', cluster T2
`H0227A` — 'then', cluster T2
`H0935K` — 'to come [in]: [sun]set', cluster T3
`H3293A` — 'wood', cluster T2
`H3384B` — 'to show', cluster M05
`H5391A` — 'to bite', cluster T3
`H5518A` — 'pot', cluster T12
`H5844A` — 'to enwrap', cluster T3
`H7218H` — 'head: leader', cluster M72
`H1980H` — 'to go: come', cluster T3
`H2388H` — 'to strengthen: hold', cluster M23
`H5375R` — 'to lift: fight', cluster T3
`H6635B` — '[Lord of] Hosts', cluster M72
`H0672G` — 'Ephrathah', cluster T8
`H0759G` — 'citadel: palace', cluster T2
`H3715A` — 'lion', cluster T13
`H3895H` — 'jaw', cluster T14
`H4639G` — 'deed: work', cluster T2
`H5257B` — 'prince', cluster T2
`H5483M` — 'horse', cluster T13
`H6924H` — 'front: old', cluster T2
`H6965H` — 'to arise: raise', cluster T3
`H7626G` — 'tribe: staff', cluster T12
`H0068H` — 'stone: weight', cluster T2
`H0256G` — 'Ahab', cluster T8
`H0990J` — 'belly: body', cluster T2
`H1121L` — 'son: aged', cluster T2
`H1160H` — 'Beor', cluster T8
`H1537G` — 'Gilgal', cluster T10
`H2132H` — 'olive', cluster T2
`H4294G` — 'tribe: rod', cluster T12
`H4813G` — 'Miriam', cluster T8
`H5158A` — 'torrent: river', cluster T10
`H5930A` — 'burnt offering', cluster M36
`H7114B` — 'to reap', cluster T3
`H7851G` — 'Shittim', cluster T10
`H0441A` — 'tame', cluster T2
`H1568G` — 'Gilead', cluster T10
`H2119A` — 'to crawl', cluster T3
`H3618H` — 'daughter-in-law', cluster T2
`H5104G` — 'River', cluster T10
`H6679A` — 'to hunt', cluster T3
`H8104H` — 'to keep: guard', cluster M74
`H0802H` — 'woman: wife', cluster T8
`H0882H` — 'Beeri', cluster T8
`H1954J` — 'Hosea', cluster T8
`H3058H` — 'Jehu', cluster T8
`H3101J` — 'Joash', cluster T8
`H3157H` — 'Jezreel', cluster T10
`H3157K` — 'Jezreel', cluster T8
`H3157L` — '[Valley of] Jezreel', cluster T2
`H3162B` — 'together', cluster T2
`H3379H` — 'Jeroboam', cluster T8
`H3947I` — 'to take: marry', cluster T3
`H5818G` — 'Uzziah', cluster T8
`H6010M` — 'Valley [of Jezreel]', cluster T10
`H6485H` — 'to reckon: punish', cluster T3
`H7760L` — 'to set: appoint', cluster T3
`H0376H` — 'man: husband', cluster T2
`H1168A` — 'Baal', cluster T10
`H1980J` — 'to go: take', cluster T3
`H1980N` — 'to go: follow', cluster T3
`H2320H` — 'month: new moon', cluster T13
`H4150H` — 'meeting: festival', cluster T2
`H5410B` — 'path', cluster T2
`H5518B` — 'thorn', cluster T13
`H5710B` — 'to adorn', cluster T3
`H6010G` — 'Valley [of Achor]', cluster T10
`H6601B` — 'to entice', cluster M77
`H7896G` — 'to set: make', cluster T3
`H0669G` — 'Ephraim', cluster T8
`H5493H` — 'to turn aside: depart', cluster M11
`H6086G` — 'tree: wood', cluster T13
`H1144G` — 'Benjamin', cluster T8
`H1390H` — 'Gibeah', cluster T10
`H2502A` — 'to rescue', cluster M45
`H4709H` — 'Mizpah', cluster T10
`H5414K` — 'to give: allow', cluster T3
`H6341A` — 'snare', cluster T2
`H7414G` — 'Ramah', cluster T10
`H7626H` — 'tribe', cluster T2
`H7819B` — 'slaughtering', cluster T2
`H8396G` — '[Mount] Tabor', cluster T10
`H8433A` — 'rebuke', cluster T2
`H0121G` — 'Adam', cluster T8
`H1870K` — 'way: road', cluster T2
`H3384A` — 'to shoot', cluster T3
`H7896I` — 'to set: appoint', cluster T3
`H7927G` — 'Shechem', cluster T10
`H8186B` — 'horror', cluster M01
`H1197A` — 'to burn: burn', cluster T3
`H2556A` — 'to leaven', cluster T3
`H8088B` — 'report', cluster M82
`H8574H` — 'oven', cluster T12
`H0759H` — 'citadel: fortress', cluster T2
`H2803H` — 'to devise: count', cluster M64
`H5492A` — 'whirlwind', cluster T2
`H0990H` — 'belly: womb', cluster T2
`H3423G` — 'to possess: possess', cluster T3
`H5116A` — 'pasture', cluster T2
`H0206H` — 'Aven', cluster T10
`H3947J` — 'to take: bring', cluster T3
`H4503I` — 'offering: tribute', cluster T2
`H5697A` — 'heifer', cluster T13
`H6524A` — 'to sprout', cluster T3
`H0758O` — 'Aram', cluster T10
`H1530G` — 'heap', cluster T2
`H3667B` — 'merchant', cluster T10
`H4397H` — 'messenger: angel', cluster T9
`H8104J` — 'to keep: careful', cluster M74
`H2030B` — 'pregnant', cluster T2
`H2717A` — 'to dry', cluster T3
`H5375L` — 'to lift: exalt', cluster T3
`H7704I` — 'land: wildlife', cluster T2
`H3844G` — 'Lebanon', cluster T10
`H3947H` — 'to take: recieve', cluster T3
`H7488B` — 'luxuriant', cluster T2
`H0127I` — 'land: planet', cluster T2
`H0206G` — '[Valley of] Aven', cluster T2
`H0518J` — 'if: until', cluster T6
`H0738A` — 'lion', cluster T13
`H0758I` — 'Syria', cluster T10
`H1130I` — 'Ben-hadad', cluster T8
`H1224G` — 'Bozrah', cluster T10
`H1237J` — '[Aven] Valley', cluster T10
`H2030A` — 'pregnant', cluster T2
`H2254A` — 'to pledge', cluster T3
`H2706G` — 'statute: decree', cluster T2
`H2742A` — 'sharp', cluster T2
`H3760G` — 'Carmel', cluster T10
`H6430G` — 'Philistine', cluster T11
`H7024B` — 'Kir', cluster T10
`H8127H` — 'tooth: ivory', cluster T14
`H8248H` — 'to water: drink', cluster T3
`G0032G` — 'angel', cluster T9
`G0032H` — 'angel: messenger', cluster T9
`G0068G` — 'field', cluster T2
`G0068H` — 'Field (of blood)', cluster T10
`G0129G` — 'blood', cluster T14
`G0129H` — '(Field of) Blood', cluster T10
`G0165G` — 'an age: age', cluster T2
`G0435G` — 'man', cluster T8
`G0435H` — 'man: husband', cluster T2
`G0568H` — 'to have in full', cluster T3
`G0630H` — 'to release: divorce', cluster T3
`G0906G` — 'to throw: throw', cluster T3
`G0906H` — 'to throw: put', cluster T3
`G0906J` — 'to throw: pour', cluster T3
`G0928G` — 'to torture: torture', cluster M03
`G0938H` — 'Queen', cluster T2
`G1056G` — 'Galilee', cluster T10
`G1056H` — '(Sea of) Galilee', cluster T10
`G1081G` — 'offspring', cluster T2
`G1081H` — 'offspring: fruit', cluster T2
`G1093G` — 'earth: planet', cluster T2
`G1093H` — 'earth: country', cluster T2
`G1093I` — 'earth: soil', cluster T2
`G1135G` — 'woman', cluster T8
`G1135H` — 'woman: wife', cluster T8
`G1487G` — 'if', cluster T2
`G1487H` — 'if: not', cluster T2
`G1487I` — 'if: is[question]', cluster T2
`G1487L` — 'if: else', cluster T2
`G1492H` — 'to perceive: see', cluster T3
`G2012` — 'manager', cluster T2
`G2083` — 'friend', cluster M05
`G2149` — 'broad', cluster T2
`G2197G` — 'Zechariah', cluster T8
`G2264G` — 'Herod', cluster T2
`G2264H` — 'Herod', cluster T2
`G2384G` — 'Jacob', cluster T8
`G2384H` — 'Jacob', cluster T8
`G2385G` — 'James', cluster T2
`G2385H` — 'James', cluster T2
`G2385I` — 'James', cluster T2
`G2424G` — 'Jesus', cluster T7
`G2455H` — 'Judas', cluster T8
`G2455I` — 'Jude', cluster T8
`G2455N` — 'Judah', cluster T8
`G2491G` — 'John', cluster T2
`G2491H` — 'John', cluster T2
`G2495H` — 'Jonah', cluster T8
`G2501G` — 'Joseph', cluster T2
`G2501H` — 'Joseph', cluster T8
`G2501I` — 'Joseph', cluster T8
`G2541J` — 'Caesar', cluster T2
`G2542G` — 'Caesarea [Philippi]', cluster T2
`G2763H` — 'Potter (Field)', cluster T2
`G2787H` — 'ark: Noah', cluster T2
`G2962G` — 'lord: God', cluster T7
`G2962H` — 'lord: master', cluster M72
`G3123G` — 'more', cluster T2
`G3123H` — 'more: rather', cluster T2
`G3137G` — 'Mary', cluster T2
`G3137I` — 'Mary', cluster T2
`G3558H` — '(Queen of) the South', cluster T8
`G3614G` — 'home', cluster T2
`G3614H` — 'home: household', cluster T2
`G3624G` — 'house: home', cluster T2
`G3624H` — 'house: household', cluster T2
`G3708G` — 'to see: to see', cluster T3
`G3754G` — 'that/since: that', cluster T6
`G3754H` — 'that/since: since', cluster T6
`G3985G` — 'to test/tempt: tempt', cluster M35
`G3985H` — 'to test/tempt: test', cluster M35
`G4160I` — 'to do/make: appoint', cluster T3
`G4245G` — 'elder: Elder', cluster T2
`G4413G` — 'first', cluster T2
`G4613G` — 'Simon', cluster T2
`G4613H` — 'Simon', cluster T2
`G4613I` — 'Simon', cluster T2
`G4613J` — 'Simon', cluster T2
`G4613O` — 'Simon', cluster T2
`G4672G` — 'Solomon', cluster T8
`G4690G` — 'seed: offspring', cluster T2
`G4690H` — 'seed(s)', cluster T13
`G5083G` — 'to keep: observe', cluster T3
`G5083H` — 'to keep: guard', cluster M74
`G5259H` — 'by/under: under', cluster T2
`G5376G` — 'Philip', cluster T2
`G5376H` — 'Philip', cluster T2
`G5376K` — ' Philippi', cluster T2
`G5438G` — 'prison/watch: prison', cluster T2
`G5438H` — 'prison/watch: watch', cluster T2
`G5456H` — 'voice/sound: noise', cluster M84
`G5564G` — 'place', cluster T2
`G0223G` — 'Alexander', cluster T2
`G0906I` — 'to throw: sow', cluster T3
`G1085G` — 'family: descendant', cluster T2
`G1487M` — 'if: even though', cluster T2
`G2500G` — 'Joses', cluster T2
`G3017I` — 'Levi', cluster T8
`G3708H` — 'to see: to appear', cluster T3
`G4413I` — 'first: chief', cluster T2
`G4413J` — 'first: best', cluster T2
`G4504G` — 'Rufus', cluster T2
`G0007H` — 'Abijah', cluster T8
`G1487J` — 'if: if only', cluster T2
`G2197H` — 'Zechariah', cluster T8
`G2385J` — 'James', cluster T2
`G2455G` — 'Judas', cluster T8
`G2541G` — 'Caesar', cluster T2
`G2976G` — 'Lazarus', cluster T2
`G3137J` — 'Mary', cluster T2
`G3558G` — 'south', cluster T2
`G4245H` — 'elder: old', cluster T2
`G4826G` — 'Simeon', cluster T2
`G5376I` — 'Philip', cluster T2
`G5442H` — 'to keep/guard: guard', cluster M74
`G5442I` — 'to keep/guard: protect', cluster M74
`G2495G` — 'John', cluster T2
`G2501N` — 'Joseph', cluster T8
`G2976H` — 'Lazarus', cluster T2
`G3137K` — 'Mary', cluster T2
`G4413H` — 'first: previous', cluster T2
`G4613L` — 'Simon', cluster T2
`G5083I` — 'to keep: protect', cluster M74
`G5085H` — 'Tiberias', cluster T2
`G0223H` — 'Alexander', cluster T2
`G0223I` — 'Alexander', cluster T2
`G0367G` — 'Ananias', cluster T2
`G0367H` — 'Ananias', cluster T2
`G0367I` — 'Ananias', cluster T2
`G0490G` — 'Antioch', cluster T2
`G0490H` — 'Antioch', cluster T2
`G0568I` — 'to abstain', cluster T3
`G0923G` — 'Barsabbas', cluster T2
`G0923H` — 'Barsabbas', cluster T2
`G1050G` — 'Gaius', cluster T2
`G1487K` — 'if: surely', cluster T2
`G2060G` — 'Hermes', cluster T2
`G2264I` — 'Herod', cluster T2
`G2424I` — 'Joshua', cluster T8
`G2455K` — 'Judas', cluster T8
`G2455L` — 'Judas', cluster T8
`G2455M` — 'Judas', cluster T8
`G2459G` — 'Justus', cluster T2
`G2459I` — 'Justus', cluster T2
`G2491I` — 'John', cluster T2
`G2491J` — 'John', cluster T2
`G2500I` — 'Joses', cluster T2
`G2501M` — 'Joseph', cluster T8
`G2541H` — 'Caesar', cluster T2
`G2542H` — 'Caesarea', cluster T2
`G2804G` — 'Claudius', cluster T2
`G2804H` — 'Claudius', cluster T2
`G2839H` — 'common: shared', cluster T2
`G3137L` — 'Mary', cluster T2
`G3972G` — 'Paul', cluster T2
`G3972H` — ' Paulus', cluster T2
`G3985I` — 'to test/tempt: try', cluster M35
`G4160J` — 'to do/make: spend[time]', cluster T3
`G4549G` — 'Saul', cluster T2
`G4549H` — 'Saul', cluster T8
`G4613M` — 'Simon', cluster T2
`G4613N` — 'Simon', cluster T2
`G4672H` — "Solomon's [Portico]", cluster T8
`G4826I` — 'Simeon', cluster T8
`G4826K` — 'Simeon', cluster T8
`G5328G` — 'Pharaoh', cluster T2
`G5376J` — 'Philip', cluster T2
`G5564H` — 'Field (of Blood)', cluster T10
`G5586H` — 'stone: vote', cluster T2
`G1050I` — 'Gaius', cluster T2
`G2060H` — 'Hermes', cluster T2
`G2269H` — 'Esau', cluster T11
`G2763G` — 'potter', cluster T2
`G3137M` — 'Mary', cluster T2
`G4160H` — 'to do/make: make', cluster T3
`G5328I` — 'Pharaoh', cluster T2
`G2541I` — 'Caesar', cluster T2
`G2424J` — 'Jesus', cluster T8
`G2459H` — 'Justus', cluster T2
`G0223J` — 'Alexander', cluster T2
`G2269G` — 'Esau', cluster T8
`G3017J` — 'Levi', cluster T8
`G5328H` — 'Pharaoh', cluster T2
`G1050J` — 'Gaius', cluster T2
`G0938G` — 'queen', cluster M72
`G5586G` — 'stone', cluster T2
`H0040G` — 'Abimelech', cluster T8
`H0120H` — 'the man [Adam]', cluster T8
`H0122B` — 'red stuff', cluster T2
`H0123H` — 'Edom', cluster T8
`H0227B` — 'the past', cluster T2
`H0241I` — 'ear: to ears', cluster T2
`H0251H` — 'brother: male-relative', cluster T2
`H0328B` — 'softly', cluster T2
`H0329G` — 'Atad', cluster T10
`H0345G` — 'Aiah', cluster T8
`H0356G` — 'Elon', cluster T8
`H0410I` — 'El [Elohe]', cluster T7
`H0410J` — 'El [Most High]', cluster T7
`H0430H` — '[LORD]-Elohe', cluster T10
`H0436H` — 'terebinth', cluster T2
`H0441B` — 'chief', cluster T2
`H0461G` — 'Eliezer', cluster T8
`H0464G` — 'Eliphaz', cluster T8
`H0518H` — 'if: surely no', cluster T6
`H0520A` — 'cubit', cluster T2
`H0565A` — 'word', cluster M65
`H0672H` — 'Ephrath', cluster T10
`H0746A` — 'Arioch', cluster T8
`H0758L` — '[Paddan]-aram', cluster T10
`H0761J` — 'Aramean', cluster T11
`H0805A` — 'Asshurim', cluster T11
`H0812G` — 'Eshcol', cluster T8
`H0859C` — 'you [f.s.]', cluster T2
`H0859E` — 'you [f.p.]', cluster T2
`H0882G` — 'Beeri', cluster T8
`H0935I` — 'to come [in]: towards', cluster T3
`H0935J` — 'to come [in]: advanced', cluster T3
`H0935M` — 'to come [in]: fulfill', cluster T3
`H0953A` — 'pit', cluster T2
`H1004O` — 'house: inside', cluster T2
`H1004P` — 'house: palace', cluster T10
`H1106B` — 'Bela', cluster T10
`H1106G` — 'Bela', cluster T8
`H1121H` — 'son: young animal', cluster T2
`H1121J` — 'son', cluster T2
`H1160G` — 'Beor', cluster T8
`H1166I` — 'rule: to marry', cluster T3
`H1167I` — 'master: men', cluster T2
`H1167K` — 'master: [master of]', cluster T2
`H1177G` — 'Baal-hanan', cluster T8
`H1237K` — 'valley', cluster T10
`H1254A` — 'to create', cluster T3
`H1315H` — 'Basemath', cluster T8
`H1315I` — 'Basemath', cluster T8
`H1366H` — 'border: area', cluster T2
`H1410G` — 'Gad', cluster T8
`H1419K` — 'great: old', cluster T2
`H1481A` — 'to sojourn', cluster T3
`H1657G` — 'Goshen', cluster T10
`H1683G` — 'Deborah', cluster T8
`H1697O` — 'Chronicles', cluster T2
`H1719C` — 'Dedan', cluster T8
`H1803B` — 'poor', cluster T2
`H1817C` — 'door', cluster T2
`H1835G` — 'Dan', cluster T10
`H1835H` — 'Dan', cluster T8
`H1908G` — 'Hadad', cluster T8
`H2022H` — 'mountain: hill country', cluster T10
`H2048B` — 'to deceive', cluster M14
`H2226G` — 'Zerah', cluster T8
`H2226H` — 'Zerah', cluster T8
`H2226I` — 'Zerah', cluster T8
`H2233G` — 'seed', cluster T2
`H2275A` — 'Hebron', cluster T10
`H2275H` — 'Hebron [Valley]', cluster T10
`H2290B` — 'belt', cluster T2
`H2341G` — 'Havilah', cluster T10
`H2341J` — 'Havilah', cluster T10
`H2513A` — 'portion', cluster T2
`H2513B` — 'smoothness', cluster T2
`H2526G` — 'Ham', cluster T8
`H2529A` — 'curd', cluster T2
`H2563A` — 'clay', cluster T13
`H2585G` — 'Enoch', cluster T8
`H2585H` — 'Enoch', cluster T8
`H2590B` — 'embalming', cluster T2
`H2691B` — 'village', cluster T2
`H2696H` — 'Hezron', cluster T8
`H2706H` — 'statute: portion', cluster T2
`H2721A` — 'drought', cluster T2
`H2771A` — 'Haran', cluster T10
`H2975G` — 'Nile', cluster T10
`H3026A` — 'Jegar', cluster T10
`H3026B` — '[Jegar]-sahadutha', cluster T10
`H3103H` — 'Jobab', cluster T8
`H3117I` — 'day: year', cluster T2
`H3243H` — 'to suckle', cluster T3
`H3243I` — 'suckling-nurse', cluster T2
`H3266G` — 'Jeush', cluster T8
`H3318K` — 'to come out: [sun]rise', cluster T3
`H3318L` — 'to come out: issue', cluster T3
`H3326A` — 'bed', cluster T12
`H3335G` — 'to form: formed', cluster T3
`H3382G` — 'Jared', cluster T8
`H3423I` — 'to possess: poor', cluster T3
`H3458G` — 'Ishmael', cluster T8
`H3485G` — 'Issachar', cluster T8
`H3513J` — 'to honor: dull', cluster M16,T3
`H3559A` — 'to establish: prepare', cluster T3
`H3563A` — 'cup', cluster T12
`H3568A` — 'Cush', cluster T10
`H3568G` — 'Cush', cluster T8
`H3588C` — 'for as that: since', cluster T6
`H3603H` — 'talent', cluster T2
`H3641A` — 'Calneh', cluster T10
`H3651A` — 'right', cluster T2
`H3651B` — 'as', cluster T2
`H3667A` — 'Canaan', cluster T10
`H3667G` — 'Canaan', cluster T8
`H3701H` — 'silver: price', cluster T2
`H3709H` — 'palm: sole', cluster T2
`H3709I` — 'palm: dish', cluster T2
`H3722B` — 'to cover', cluster M45
`H3724B` — 'pitch', cluster T2
`H3733A` — 'saddle', cluster T2
`H3835B` — 'to make bricks', cluster T3
`H3837A` — 'Laban', cluster T8
`H3870H` — 'Luz', cluster T10
`H3929G` — 'Lamech', cluster T8
`H3929H` — 'Lamech', cluster T8
`H4026M` — 'tower', cluster T2
`H4080H` — 'Midian', cluster T10
`H4105G` — 'Mehetabel', cluster T8
`H4111G` — 'Mahalalel', cluster T8
`H4124H` — 'Moab', cluster T8
`H4176G` — 'Moreh', cluster T10
`H4229A` — 'to wipe', cluster T3
`H4353G` — 'Machir', cluster T8
`H4397G` — 'messenger', cluster T9
`H4417G` — 'Salt [Sea]', cluster T10
`H4417M` — 'salt', cluster T2
`H4428L` — "King's", cluster T2
`H4435G` — 'Milcah', cluster T8
`H4471G` — 'Mamre', cluster T10
`H4471H` — 'Mamre', cluster T8
`H4503H` — 'offering: gift', cluster T2
`H4519G` — 'Manasseh', cluster T8
`H4569A` — 'ford', cluster T11
`H4601G` — 'Maacah', cluster T8
`H4924A` — 'fat', cluster T2
`H4932H` — 'second', cluster T2
`H4945A` — 'cupbearer', cluster T3
`H4945B` — 'irrigation', cluster T2
`H5066H` — 'to approach: bring', cluster T3
`H5090A` — 'to lead', cluster T3
`H5152G` — 'Nahor', cluster T8
`H5152H` — 'Nahor', cluster T8
`H5158N` — 'torrent: valley', cluster T10
`H5184G` — 'Nahath', cluster T8
`H5234B` — 'to alienate', cluster T3
`H5321G` — 'Naphtali', cluster T8
`H5387A` — 'leader', cluster M72
`H5439I` — 'around: whole', cluster T2
`H5523G` — 'Succoth', cluster T10
`H5676H` — 'side: beyond', cluster T10
`H5677G` — 'Eber', cluster T8
`H5711G` — 'Adah', cluster T8
`H5711H` — 'Adah', cluster T8
`H5857G` — 'Ai', cluster T10
`H5869J` — 'eye: before[the eyes]', cluster T2
`H5869M` — 'spring', cluster T10
`H5907G` — 'Achbor', cluster T8
`H5921B` — 'as', cluster T2
`H5927I` — 'to ascend: offer up', cluster T3
`H5927K` — 'to ascend: copulate', cluster T3
`H5945A` — 'high', cluster M08
`H5945H` — '[LORD] Most High', cluster T7
`H5973B` — 'from with', cluster T2
`H6002H` — 'Amalek', cluster T8
`H6010K` — 'Valley [of Hebron]', cluster T10
`H6010O` — 'Valley [of Kings]', cluster T10
`H6010Q` — 'Valley [of Siddim]', cluster T10
`H6049A` — 'to cloud', cluster T3
`H6085G` — 'Ephron', cluster T8
`H6106H` — 'bone: same', cluster T2
`H6131B` — 'to hamstring', cluster T3
`H6147G` — 'Er', cluster T8
`H6215G` — 'Esau', cluster T8
`H6290G` — 'Paran', cluster T10
`H6310K` — 'lip: according', cluster T14
`H6327A` — 'to scatter', cluster T3
`H6430H` — 'Philistine', cluster T11
`H6440K` — 'face: east', cluster T2
`H6547G` — 'Pharaoh', cluster T8
`H6547H` — 'Pharaoh', cluster T8
`H6595A` — 'morsel', cluster T2
`H6672A` — 'midday', cluster T2
`H6672B` — 'roof', cluster T2
`H6718A` — 'wild game', cluster T2
`H6781A` — 'bracelet', cluster T12
`H6872A` — 'bundle', cluster T2
`H6924B` — 'east', cluster T2
`H6946G` — 'Kadesh', cluster T10
`H6963J` — 'voice: message', cluster T2
`H6996H` — 'small: young', cluster T2
`H7014B` — 'Cain', cluster T8
`H7070H` — 'branch: stem', cluster T13
`H7073G` — 'Kenaz', cluster T8
`H7097A` — 'end', cluster T2
`H7122G` — 'to encounter: meet', cluster M37
`H7122I` — 'to encounter: chanced', cluster M37
`H7141G` — 'Korah', cluster T8
`H7200J` — 'to see: select', cluster T3
`H7200N` — 'Provider [God]', cluster T7
`H7218J` — 'head: first', cluster T14
`H7235B` — 'to shoot', cluster T3
`H7298A` — 'trough', cluster T2
`H7342H` — 'broad: wide', cluster T2
`H7344G` — 'Rehoboth', cluster T10
`H7344H` — 'Rehoboth', cluster T10
`H7344I` — 'Rehoboth', cluster T10
`H7363B` — 'to hover', cluster T3
`H7411B` — 'to deceive', cluster M14
`H7467G` — 'Reuel', cluster T8
`H7486G` — 'Rameses', cluster T10
`H7586I` — 'Shaul', cluster T8
`H7614I` — 'Sheba', cluster T8
`H7620H` — 'week', cluster T2
`H7641B` — 'ear', cluster T2
`H7704A` — 'Sirion', cluster T10
`H7732G` — 'Shobal', cluster T8
`H7892A` — 'song', cluster M22
`H7896H` — 'to set: put', cluster T3
`H7901H` — 'to lie down: sleep', cluster T3
`H7901I` — 'to lie down: have sex', cluster T3
`H7927H` — 'Shechem', cluster T8
`H7936B` — 'to hire', cluster T3
`H7971H` — 'to send: let go', cluster T3
`H7971I` — 'to send: divorce', cluster T3
`H8040H` — 'left: north', cluster T2
`H8048G` — 'Shammah', cluster T8
`H8138B` — 'to repeat', cluster T3
`H8163A` — 'hairy', cluster T2
`H8165A` — 'Seir', cluster T10
`H8165B` — 'Seir', cluster T8
`H8193H` — 'lip: words', cluster T14
`H8193K` — 'lip: language', cluster T2
`H8321B` — 'vine', cluster T13
`H8336B` — 'linen', cluster T2
`H8453A` — 'sojourner', cluster T2
`H8478I` — 'underneath: stand', cluster T2
`H8478L` — 'underneath: swear', cluster T2
`H8487G` — 'Teman', cluster T8
`H8559G` — 'Tamar', cluster T8
`H8577N` — 'serpent: monster', cluster T2
`H8646G` — 'Terah', cluster T8
`H0221G` — 'Uri', cluster T8
`H0352C` — 'leader', cluster T2
`H0461H` — 'Eliezer', cluster T8
`H0802I` — 'woman: another', cluster T8
`H0905G` — 'alone: pole', cluster T2
`H0905I` — 'alone: each', cluster T2
`H1004N` — 'house: container', cluster T2
`H1167G` — 'master', cluster T2
`H1304A` — 'gem', cluster T12
`H1430A` — 'stack', cluster T2
`H1647G` — 'Gershom', cluster T8
`H1697L` — 'word: case', cluster T2
`H1826A` — 'to silence: stationary', cluster M33
`H1980O` — 'to go: send', cluster T3
`H2094B` — 'to warn', cluster T3
`H2100G` — 'to flow: flowing', cluster T3
`H2319H` — 'new', cluster M45
`H2354G` — 'Hur', cluster T8
`H2436H` — 'bosom: garment', cluster T12
`H2560B` — 'to daub', cluster T3
`H2563B` — 'heap', cluster T2
`H2691A` — 'court', cluster T2
`H2803G` — 'to devise: design', cluster M64
`H2859A` — 'relative', cluster T3
`H2983G` — 'Jebusite', cluster T10
`H3091G` — 'Joshua', cluster T8
`H3233G` — 'right', cluster T2
`H3332H` — 'to pour: cast metal', cluster T3
`H3500L` — 'Jethro', cluster T8
`H3713B` — 'frost', cluster T2
`H3772G` — 'to cut: cut', cluster T3
`H3947L` — 'to take: fire', cluster T3
`H4024B` — 'Migdol', cluster T10
`H4118B` — 'quickly', cluster T3
`H4150I` — 'meeting', cluster T2
`H4207B` — 'fork', cluster T2
`H4245B` — 'sickness', cluster T2
`H4294H` — 'tribe', cluster T2
`H4414B` — 'to salt', cluster T3
`H4478A` — 'manna', cluster T2
`H4478B` — 'What?', cluster T2
`H4609B` — 'step', cluster T2
`H4740H` — 'corner', cluster T2
`H4759B` — 'mirror', cluster T2
`H4809G` — 'Meribah', cluster M02,T10
`H4938B` — 'staff', cluster T12
`H5070G` — 'Nadab', cluster T8
`H5130B` — 'to wave', cluster T3
`H5137A` — 'to sprinkle', cluster T3
`H5198B` — 'gum', cluster T14
`H5216A` — 'lamp', cluster T12
`H5251G` — 'Banner [God]', cluster T10
`H5307H` — 'to fall: deserting', cluster T3
`H5327A` — 'to struggle', cluster M34
`H5375S` — 'to lift: enthuse', cluster T3
`H5375V` — 'to lift: count', cluster T3
`H5414Q` — 'to give: if only!', cluster T3
`H5439H` — 'around: side', cluster T2
`H5488G` — 'Red [Sea]', cluster T2
`H5514G` — 'Sinai', cluster T10
`H5514H` — '[Wilderness of] Sinai', cluster T10
`H5526B` — 'to cover', cluster M45
`H5526E` — 'to cover', cluster M45
`H5592A` — 'basin', cluster T12
`H5676G` — 'side: beside', cluster T10
`H5800C` — 'to leave: release', cluster T3
`H5953A` — 'to abuse', cluster T3
`H5982G` — 'pillar', cluster T2
`H6002G` — 'Amalek', cluster T10
`H6016B` — 'omer', cluster T2
`H6030C` — 'to sing', cluster M22
`H6086I` — 'tree: stick', cluster T2
`H6154M` — 'racial-mix', cluster T11
`H6306B` — 'redemption', cluster T2
`H6310H` — 'lip: edge', cluster T14
`H6310J` — 'lip: opening', cluster T14
`H6341B` — 'plate', cluster T12
`H6363A` — 'firstborn', cluster M37
`H6430I` — '[Sea of the] Philistines', cluster T10
`H6438H` — 'corner', cluster T10
`H6485A` — 'to reckon: list', cluster T3
`H6485B` — 'reckoning', cluster T3
`H6547I` — 'Pharaoh', cluster T8
`H6547J` — 'Pharaoh', cluster T8
`H6605B` — 'to engrave', cluster T3
`H6696C` — 'to form', cluster M61
`H6731A` — 'flower', cluster T13
`H6963I` — 'voice: thunder', cluster T2
`H6963K` — 'voice: [sound of]', cluster T2
`H6999A` — 'offer: to burn', cluster T3
`H7050B` — 'curtain', cluster T12
`H7067H` — 'jealous', cluster M18
`H7070G` — 'branch', cluster T13
`H7126H` — 'to present: bring', cluster T3
`H7218L` — 'head: count', cluster T14
`H7411A` — 'to shoot', cluster T3
`H7461A` — 'trembling', cluster M01
`H7467J` — 'Reuel', cluster T8
`H7486H` — 'Raamses', cluster T10
`H7620G` — 'Weeks', cluster T2
`H7725M` — 'to return: reply', cluster T3
`H7760I` — 'to set: take', cluster T3
`H7892B` — 'song', cluster M22
`H7991C` — 'officer', cluster T2
`H8193I` — 'lip: edge', cluster T14
`H8478J` — 'underneath: because of', cluster T2
`H8478K` — 'underneath: owning', cluster T2
`H8549G` — 'unblemished', cluster M61
`H8577M` — 'serpent: snake', cluster T10
`H0499G` — 'Eleazar', cluster T8
`H2100H` — 'to flow: discharge', cluster T3
`H2233I` — 'seed: semen', cluster T2
`H2563C` — 'homer', cluster T2
`H2720A` — 'dry', cluster T2
`H2778C` — 'to acquire', cluster T3
`H2902A` — 'to overspread', cluster T3
`H3465H` — 'old', cluster T2
`H3481H` — 'Israelite', cluster T8
`H3971B` — 'blemish', cluster T2
`H4057G` — 'Wilderness [of Sinai]', cluster T10
`H4294K` — 'tribe: supply', cluster T2
`H4332G` — 'Mishael', cluster T8
`H5414L` — 'to give: throw', cluster T3
`H5599B` — 'aftergrowth', cluster T2
`H5816G` — 'Uzziel', cluster T8
`H5927M` — 'to ascend: regurgitate', cluster T3
`H5953B` — 'to glean', cluster T3
`H5975J` — 'to stand: put', cluster T3
`H6016A` — 'sheaf', cluster T2
`H6154B` — 'mixture', cluster T2
`H6155H` — 'willow', cluster T2
`H6186B` — 'to value', cluster M26
`H6632B` — 'lizard', cluster T13
`H6867B` — 'scar', cluster T2
`H7106A` — 'to scrape', cluster M23
`H7133A` — 'offering', cluster T2
`H7673B` — 'to keep', cluster M74
`H8019B` — 'Shelomith', cluster T8
`H8042G` — 'left', cluster T2
`H8163C` — 'satyr', cluster T2
`H8227A` — 'rock badger', cluster T2
`H8296A` — 'incision', cluster T2
`H8296B` — 'incision', cluster T2
`H8549I` — 'unblemished: complete', cluster M61
`H0032G` — 'Abihail', cluster T8
`H0048G` — 'Abiram', cluster T8
`H0090G` — 'Agag', cluster T8
`H0122A` — 'red', cluster T2
`H0446G` — 'Eliab', cluster T8
`H0446H` — 'Eliab', cluster T8
`H0476G` — 'Elishama', cluster T8
`H0714G` — 'Ard', cluster T8
`H0714H` — 'Ard', cluster T8
`H0812H` — '[Valley of] Eshcol', cluster T10
`H0876G` — 'Beer', cluster T10
`H0935H` — 'Lebo-[Hamath]', cluster T10
`H1106A` — 'Bela', cluster T8
`H1120G` — 'Bamoth', cluster T10
`H1120H` — 'Bamoth', cluster T10
`H1168I` — '[Bamoth]-baal', cluster T2
`H1323H` — 'daughter: village', cluster T2
`H1350H` — 'to redeem: avenge', cluster M79
`H1350I` — 'to redeem: relative', cluster M79
`H1419J` — 'Great [Sea]', cluster T2
`H1568H` — 'Gilead', cluster T8
`H1633B` — 'to break bones', cluster T3
`H1769G` — 'Dibon', cluster T10
`H1870I` — "[King's] Highway", cluster T2
`H1954K` — 'Hoshea', cluster T8
`H2023G` — '[Mount] Hor', cluster T2
`H2023H` — '[Mount] Hor', cluster T2
`H2139G` — 'Zaccur', cluster T8
`H2174G` — 'Zimri', cluster T8
`H2354H` — 'Hur', cluster T8
`H2574G` — 'Hamath', cluster T10
`H2660A` — 'Hepher', cluster T8
`H2682B` — 'leek', cluster T2
`H2971G` — 'Jair', cluster T8
`H3270G` — 'Jazer', cluster T10
`H3318I` — 'to come out: extends', cluster T3
`H3318J` — 'to come out: casting [lot]', cluster T3
`H3318N` — 'to come out: regular', cluster T3
`H3405G` — 'Jericho', cluster T10
`H3452H` — 'wilderness', cluster T10
`H3559I` — 'to establish: make', cluster T3
`H3612G` — 'Caleb', cluster T8
`H3672G` — '[Sea of] Chinnereth', cluster T10
`H4124I` — '[Plains of] Moab', cluster T10
`H4229B` — 'to strike', cluster T3
`H4244G` — 'Mahlah', cluster T8
`H4428I` — "King's", cluster T2
`H4435H` — 'Milcah', cluster T8
`H4455A` — 'prey', cluster T2
`H4714J` — '[Brook of] Egypt', cluster T2
`H5015A` — 'Nebo', cluster T10
`H5025G` — 'Nobah', cluster T8
`H5081H` — 'noble', cluster M34
`H5158B` — 'palm-tree', cluster T2
`H5158H` — '[Eshcol] Valley', cluster T10
`H5158L` — 'Brook', cluster T10
`H5251H` — 'ensign', cluster T2
`H5283H` — 'Naaman', cluster T8
`H5417G` — 'Nethanel', cluster T8
`H5492B` — 'Suphah', cluster T10
`H5606A` — 'to slap', cluster T3
`H5945B` — 'Most High [God]', cluster T7
`H5989G` — 'Ammihud', cluster T8
`H5992G` — 'Amminadab', cluster T8
`H6075B` — 'to presume', cluster T3
`H6160I` — 'Plains [of Moab]', cluster T10
`H6306A` — 'redemption', cluster T2
`H6363B` — 'firstborn', cluster M37
`H6372G` — 'Phinehas', cluster T8
`H6412B` — 'survivor', cluster T2
`H6431G` — 'Peleth', cluster T8
`H6632A` — 'litter', cluster T2
`H6635I` — 'army: duty', cluster T2
`H6692A` — 'to blossom', cluster T3
`H6698G` — 'Zur', cluster T8
`H6698H` — 'Zur', cluster T8
`H6781B` — 'cover', cluster T2
`H6979C` — 'to destroy', cluster M10
`H7014A` — 'Kain', cluster T10
`H7141I` — 'Korah', cluster T8
`H7247G` — 'Riblah', cluster T10
`H7340K` — 'Rehob', cluster T10
`H7552G` — 'Rekem', cluster T8
`H7896J` — 'to set: accuse', cluster T3
`H8051G` — 'Shammua', cluster T8
`H8096G` — 'Shimei', cluster T8
`H8314A` — 'serpent', cluster T2
`H8526G` — 'Talmai', cluster T8
`H8656G` — 'Tirzah', cluster T8
`H0349B` — 'how?', cluster T2
`H0359A` — 'Elath', cluster T10
`H0709G` — 'Argob', cluster T10
`H0881H` — 'Beeroth-[bene-jaakan]', cluster T10
`H0935N` — 'to come [in]: besiege', cluster T3
`H1100G` — 'Belial', cluster T2
`H1142H` — '[Beeroth] Bene-jaakan', cluster T10
`H1197I` — 'to burn: purge', cluster T3
`H1237G` — 'Valley [of Jericho]', cluster T10
`H1697J` — 'word: promised', cluster T2
`H2388I` — 'to strengthen: ensure', cluster M23
`H2490I` — 'to profane/begin: fruit', cluster T3
`H2775B` — 'itch', cluster T2
`H3243G` — 'to suck', cluster T3
`H3405H` — '[Plain of] Jericho', cluster T10
`H3603G` — 'environs', cluster T10
`H3733C` — 'ram', cluster T13
`H3739A` — 'to trade', cluster T3
`H3837B` — 'Laban', cluster T10
`H3898B` — 'to feed on', cluster T3
`H4149A` — 'Moserah', cluster T10
`H4916A` — 'sending', cluster T2
`H5015H` — '[Mount] Nebo', cluster T10
`H5254H` — 'to test: try', cluster M35
`H5375T` — 'to lift: journey', cluster T3
`H5391B` — 'to pay interest', cluster T3
`H5612A` — 'scroll: document', cluster T12
`H5643A` — 'secrecy', cluster T2
`H5643B` — 'shelter', cluster T2
`H5761G` — 'Avvim', cluster T11
`H5984H` — 'Ammon', cluster T10
`H6014B` — 'to tyranise', cluster T3
`H6086J` — 'tree: stake', cluster T2
`H6160G` — 'Arabah', cluster T10
`H6177H` — 'Aroer', cluster T10
`H6252H` — 'Ashtaroth', cluster T10
`H6286B` — 'to re-harvest', cluster T3
`H6290H` — '[Mount] Paran', cluster T10
`H6643B` — 'gazelle', cluster T13
`H6946H` — '[Meribath]-kadesh', cluster T2
`H7393H` — 'chariot: millstone', cluster T12
`H7497B` — 'Rephaim', cluster T11
`H7711B` — 'blight', cluster T2
`H7760J` — 'to set: accuse', cluster T3
`H7760K` — 'to set: consider', cluster M15
`H8165G` — '[Mount] Seir', cluster T10
`H8179H` — 'gate: town', cluster T2
`H0044I` — 'Abiezer', cluster T8
`H0121H` — 'Adam', cluster T10
`H0146G` — 'Addar', cluster T10
`H0168H` — 'tent: home', cluster T2
`H0392H` — 'Achzib', cluster T10
`H0663H` — 'Aphek', cluster T10
`H0844G` — 'Asriel', cluster T8
`H0935L` — 'to come [in]: marry', cluster T3
`H1004L` — 'Beth-[baal-meon]', cluster T10
`H1032G` — 'Beth-horon', cluster T10
`H1032H` — '[Upper] Beth-horon', cluster T10
`H1032I` — '[Lower] Beth-horon', cluster T10
`H1053G` — 'Beth-shemesh', cluster T10
`H1053H` — 'Beth-shemesh', cluster T10
`H1173G` — '[Mount] Baalah', cluster T10
`H1173I` — 'Baalah', cluster T10
`H1237H` — '[Mizpah] Valley', cluster T10
`H1237I` — '[Lebanon] Valley', cluster T10
`H1389H` — 'Gibeath-[haaraloth]', cluster T10
`H1516G` — 'Valley', cluster T10
`H1516H` — '[Iphtahel] Valley', cluster T10
`H1516Q` — 'Valley', cluster T10
`H1537I` — 'Galilee', cluster T10
`H1657H` — 'Goshen', cluster T10
`H1688A` — 'Debir', cluster T10
`H1688B` — 'Debir', cluster T10
`H1688G` — 'Debir', cluster T10
`H1688H` — 'Debir', cluster T8
`H1756G` — 'Dor', cluster T10
`H1756H` — 'Dor', cluster T10
`H2011G` — '[Topheth of] Hinnom', cluster T2
`H2011H` — '[Topheth of son of] Hinnom', cluster T2
`H2067G` — 'Zabdi', cluster T8
`H2256A` — 'Mahalab', cluster T10
`H2621G` — 'Hosah', cluster T10
`H2674G` — 'Hazor', cluster T10
`H2696J` — 'Hezron', cluster T10
`H2791A` — 'silently', cluster T2
`H2971H` — 'Jair', cluster T10
`H2983H` — 'Jebus', cluster T10
`H2985G` — 'Jabin', cluster T8
`H2995G` — 'Jabneel', cluster T10
`H2995H` — 'Jabneel', cluster T10
`H3103I` — 'Jobab', cluster T8
`H3225H` — 'right: south', cluster T2
`H3239B` — 'Janoah', cluster T10
`H3309G` — 'Japhia', cluster T8
`H3309H` — 'Japhia', cluster T10
`H3332I` — 'to pour: set down', cluster T3
`H3521G` — 'Cabul', cluster T10
`H3841H` — 'Libnah', cluster T10
`H3844I` — '[Valley of] Lebanon', cluster T10
`H3956I` — 'tongue: bar', cluster T14
`H4569B` — 'ford', cluster T10
`H4601R` — 'Maacah', cluster T10
`H4708J` — '[Valley of] Mizpeh', cluster T10
`H5292A` — 'Naarah', cluster T10
`H5307L` — 'to fall: fail', cluster T3
`H5316G` — 'Naphath', cluster T10
`H5316H` — 'Naphath', cluster T10
`H5700G` — 'Eglon', cluster T10
`H5915G` — 'Achsah', cluster T8
`H5927J` — 'to ascend: attack', cluster T3
`H5945G` — 'Upper [Beth Horon]', cluster T10
`H6010J` — 'Emek', cluster T10
`H6010P` — 'Valley [of Rephaim]', cluster T10
`H6160J` — '[Beth]-arabah', cluster T10
`H6160K` — '[Sea of] the Arabah', cluster T10
`H6160L` — 'plain', cluster T2
`H6177G` — 'Aroer', cluster T10
`H6190G` — '[Gilgal]-haaraloth', cluster T10
`H6679B` — 'to provision', cluster T3
`H6718B` — 'food', cluster T2
`H6721I` — 'Sidon', cluster T10
`H6943G` — 'Kedesh', cluster T10
`H7071G` — 'Kanah', cluster T10
`H7071H` — 'Kanah', cluster T10
`H7227G` — '[Sidon] the Great', cluster T2
`H7340G` — 'Rehob', cluster T10
`H7414H` — 'Ramah', cluster T10
`H7417H` — 'Rimmon', cluster T10
`H7497G` — '[Valley of] Rephaim', cluster T10
`H7652B` — 'Sheba', cluster T10
`H7883G` — 'Shihor', cluster T10
`H7928G` — 'Shechem', cluster T8
`H8165H` — '[Mount] Seir', cluster T10
`H8388A` — 'to border', cluster T3
`H8481G` — 'Lower [Beth Horon]', cluster T10
`H8556B` — 'Timnath-serah', cluster T10
`H0040H` — 'Abimelech', cluster T8
`H0047H` — 'mighty: stallion', cluster M23
`H0329H` — 'bramble', cluster T2
`H0356J` — 'Elon', cluster T8
`H0410H` — 'El [Berith]', cluster T7
`H0436G` — "[Diviners'] Oak", cluster T2
`H0673G` — 'Ephraimite', cluster T8
`H0758N` — 'Mesopotamia', cluster T10
`H0876H` — 'Beer', cluster T10
`H0966G` — 'Bezek', cluster T10
`H1053I` — 'Beth-shemesh', cluster T10
`H1101B` — 'to feed', cluster T3
`H1121K` — 'son: warrior', cluster T2
`H1387H` — 'Gibeah', cluster T10
`H1387J` — '[Maareh]-geba', cluster T10
`H1568I` — 'Gilead', cluster T8
`H1568K` — '[Mount] Gilead', cluster T10
`H1568L` — '[Jabesh]-gilead', cluster T10
`H1617G` — 'Gera', cluster T8
`H1683H` — 'Deborah', cluster T8
`H1734G` — 'Dodo', cluster T8
`H2268H` — 'Heber', cluster T8
`H2686B` — 'to shoot', cluster T3
`H2717B` — 'to destroy', cluster M10
`H2775A` — 'sun', cluster T13
`H2776G` — 'Heres', cluster T10
`H2776H` — '[Mount] Heres', cluster T10
`H2971I` — 'Jair', cluster T8
`H2985H` — 'Jabin', cluster T8
`H3003G` — 'Jabesh [Gilead]', cluster T10
`H3003I` — 'Jabesh', cluster T10
`H3083G` — 'Jonathan', cluster T8
`H3101G` — 'Joash', cluster T8
`H3147G` — 'Jotham', cluster T8
`H3499B` — 'cord', cluster M03,T12
`H3500G` — 'Jether', cluster T8
`H3844H` — '[Mount] Lebanon', cluster T10
`H3870G` — 'Luz', cluster T10
`H3895G` — 'Lehi', cluster T10
`H3919A` — 'Laish', cluster T10
`H4150J` — 'meeting: signal appointed', cluster T2
`H4176H` — 'Moreh', cluster T10
`H4318G` — 'Micah', cluster T8
`H4321I` — 'Micah', cluster T8
`H4496G` — 'Nohah', cluster T10
`H4519K` — 'Moses', cluster T8
`H4629G` — 'Maareh', cluster T10
`H4708K` — 'Mizpah', cluster T10
`H4709G` — 'Mizpah', cluster T10
`H4718A` — 'hammer', cluster T12
`H5025H` — 'Nobah', cluster T10
`H5158J` — '[Sorek] Valley', cluster T10
`H5274A` — 'to lock', cluster T3
`H5321H` — '[Kedesh]-naphtali', cluster T10
`H5375U` — 'to lift: marry', cluster T3
`H5375W` — 'to lift: bearing [armour]', cluster T3
`H5592B` — 'threshold', cluster T2
`H5608B` — 'secretary', cluster T2
`H5658H` — 'Abdon', cluster T8
`H5700H` — 'Eglon', cluster T8
`H5862G` — 'Etam', cluster T10
`H6049G` — "Diviners' [Oak]", cluster T10
`H6084H` — 'Ophrah', cluster T10
`H6252G` — 'Ashtaroth', cluster T10
`H6544A` — 'to lead', cluster T3
`H6743A` — 'to rush', cluster T3
`H6828H` — 'Zaphon', cluster T10
`H6924A` — 'East', cluster T2
`H6943J` — 'Kedesh', cluster T10
`H6965K` — 'to arise: guard', cluster M74
`H7014G` — 'Kenite', cluster T11
`H7049A` — 'to sling', cluster T3
`H7073I` — 'Kenaz', cluster T8
`H7340H` — 'Rehob', cluster T10
`H7417C` — '[Rock of] Rimmon', cluster T10
`H7462D` — 'to befriend', cluster T3
`H7641H` — 'Shibboleth', cluster T2
`H7754A` — 'branch', cluster T13
`H7754B` — 'branch', cluster T13
`H7971J` — 'to send: marriage', cluster T3
`H7971L` — 'to send: burn', cluster T3
`H8385B` — 'opportunity', cluster T2
`H8439H` — 'Tola', cluster T8
`H0673H` — 'Ephrathite', cluster T8
`H1162G` — 'Boaz', cluster T8
`H5744G` — 'Obed', cluster T8
`H0026G` — 'Abigail', cluster T8
`H0029G` — 'Abijah', cluster T8
`H0041G` — 'Abinadab', cluster T8
`H0041H` — 'Abinadab', cluster T8
`H0041I` — 'Abinadab', cluster T8
`H0059G` — 'Abel', cluster T10
`H0090H` — 'Agag', cluster T8
`H0281O` — 'Ahijah', cluster T8
`H0285G` — 'Ahitub', cluster T8
`H0288G` — 'Ahimelech', cluster T8
`H0288H` — 'Ahimelech', cluster T8
`H0290G` — 'Ahimaaz', cluster T8
`H0293G` — 'Ahinoam', cluster T8
`H0293H` — 'Ahinoam', cluster T8
`H0425L` — '[Valley of] Elah', cluster T2
`H0430I` — '[Gibeath]-elohim', cluster T10
`H0446I` — 'Eliab', cluster T8
`H0453G` — 'Elihu', cluster T8
`H0499H` — 'Eleazar', cluster T8
`H0511H` — 'Elkanah', cluster T8
`H0663G` — 'Aphek', cluster T10
`H0830H` — 'refuse', cluster M30
`H0966H` — 'Bezek', cluster T10
`H1254B` — 'to fatten', cluster T3
`H1387G` — 'Geba', cluster T10
`H1410H` — 'Gad', cluster T8
`H1516I` — '[Zeboim] Valley', cluster T10
`H1516P` — 'Gath', cluster T10
`H1533H` — '[Mount] Gilboa', cluster T10
`H1697K` — 'word: deed', cluster T2
`H1826I` — 'to silence: destroyed', cluster M55
`H1861A` — 'goad', cluster T2
`H2290A` — 'belt', cluster T2
`H2416B` — 'kinsfolk', cluster M25,T8
`H2793G` — 'Horesh', cluster T10
`H3083H` — 'Jonathan', cluster T8
`H3091H` — 'Joshua', cluster T8
`H3097G` — 'Joab', cluster T8
`H3100G` — 'Joel', cluster T8
`H3129G` — 'Jonathan', cluster T8
`H3129N` — 'Jonathan', cluster T8
`H3157G` — 'Jezreel', cluster T10
`H3158G` — 'Jezreel', cluster T10
`H3277G` — "Wildgoats'", cluster T2
`H3293B` — 'honeycomb', cluster T10
`H3395G` — 'Jeroham', cluster T8
`H3452G` — 'Jeshimon', cluster T10
`H3543B` — 'to rebuke', cluster T3
`H3559J` — 'to establish: commit', cluster T3
`H3724D` — 'village', cluster T2
`H3774G` — 'Cherethite', cluster T11
`H4207A` — 'fork', cluster T2
`H4224B` — 'refuge', cluster M19
`H4307H` — 'guardhouse', cluster T2
`H4324G` — 'Michal', cluster T8
`H4686B` — 'fortress', cluster T2
`H4708H` — 'Mizpeh', cluster T10
`H5035A` — 'bag', cluster T12
`H5035B` — 'harp', cluster T12
`H5176G` — 'Nahash', cluster T8
`H5310B` — 'to disperse', cluster T3
`H5369G` — 'Ner', cluster T8
`H5737C` — 'to lack', cluster T3
`H5860B` — 'to pounce', cluster T3
`H6010I` — 'Valley [of Elah]', cluster T10
`H6030A` — 'to dwell', cluster T3
`H6084G` — 'Ophrah', cluster T10
`H6310L` — 'lip: one third', cluster T14
`H6372H` — 'Phinehas', cluster T8
`H6571A` — 'horse', cluster T13
`H6678G` — 'Zobah', cluster T10
`H6689G` — 'Zuph', cluster T8
`H6689H` — 'Zuph', cluster T10
`H6697G` — 'Rocks [of Goats]', cluster T2
`H6872C` — 'Zeror', cluster T8
`H6931H` — 'eastern: older', cluster T2
`H7027G` — 'Kish', cluster T8
`H7050A` — 'sling', cluster T2
`H7203A` — 'seer', cluster T2
`H7323H` — 'to run: guard', cluster T3
`H7414J` — 'Ramah', cluster T10
`H7586G` — 'Saul', cluster T8
`H7704B` — 'land: soil', cluster T13
`H7991B` — 'triangle', cluster T2
`H8048J` — 'Shammah', cluster T8
`H8050G` — 'Samuel', cluster T8
`H8127I` — 'tooth: crag', cluster T14
`H8127J` — 'tooth: prong', cluster T14
`H8138A` — 'to change', cluster M45
`H8189G` — 'Shaaraim', cluster T10
`H8302B` — 'armor', cluster T12
`H8396H` — 'Tabor', cluster T10
`H8549J` — 'unblemished: Thummim', cluster T3
`H0026H` — 'Abigail', cluster T8
`H0059H` — 'Abel', cluster T10
`H0223A` — 'Uriah', cluster T8
`H0290H` — 'Ahimaaz', cluster T8
`H0345H` — 'Aiah', cluster T8
`H0445G` — 'Elhanan', cluster T8
`H0499I` — 'Eleazar', cluster T8
`H0669K` — '[Forest of] Ephraim', cluster T10
`H0669L` — 'Ephraim', cluster T10
`H0758M` — 'Edom', cluster T10
`H0805B` — 'Ashurite', cluster T8
`H0881G` — 'Beeroth', cluster T10
`H0953B` — 'Cistern', cluster T2
`H1141G` — 'Benaiah', cluster T8
`H1196G` — 'Baanah', cluster T8
`H1197H` — 'to burn: destroy', cluster T3
`H1268B` — 'Berothai', cluster T10
`H1271G` — 'Barzillai', cluster T8
`H1271H` — 'Barzillai', cluster T8
`H1295H` — 'pool', cluster T10
`H1387I` — 'Geba', cluster T10
`H1516J` — '[Salt] Valley', cluster T10
`H1533G` — 'Gilboa', cluster T10
`H1617H` — 'Gera', cluster T8
`H1734H` — 'Dodo', cluster T8
`H2132G` — '[Mount of] Olives', cluster T2
`H2416D` — 'community', cluster M44,T8
`H2438G` — 'Hiram', cluster T8
`H2586G` — 'Hanun', cluster T8
`H3063O` — '[Baalah of]Judah', cluster T10
`H3077G` — 'Jehoiada', cluster T8
`H3082H` — 'Jonadab', cluster T8
`H3083I` — 'Jonathan', cluster T8
`H3083O` — 'Jonathan', cluster T8
`H3092G` — 'Jehoshaphat', cluster T8
`H3122G` — 'Jonadab', cluster T8
`H3141G` — 'Joram', cluster T8
`H3157I` — 'Jezreel', cluster T10
`H3293H` — '[Ephraim] Forest', cluster T10
`H3481G` — 'Ishmaelite', cluster T8
`H3774H` — 'Cherethite', cluster T11
`H3823B` — 'to bake', cluster T3
`H3919B` — 'Laish', cluster T8
`H4024A` — 'tower', cluster T2
`H4316J` — 'Mica', cluster T8
`H4324H` — 'Merab', cluster T8
`H4353H` — 'Machir', cluster T8
`H4417H` — '[Valley of] Salt', cluster T10
`H4648G` — 'Mephibosheth', cluster T8
`H4648H` — 'Mephibosheth', cluster T8
`H4662H` — 'appointment', cluster T2
`H4937A` — 'support', cluster M70
`H5176H` — 'Nahash', cluster T8
`H5176I` — 'Nahash', cluster T8
`H5176J` — 'Nahash', cluster T8
`H5273B` — 'musical', cluster M22
`H5416G` — 'Nathan', cluster T8
`H5416H` — 'Nathan', cluster T8
`H5425B` — 'to free', cluster T3
`H5437K` — 'to turn: changed', cluster T3
`H5798A` — 'Uzzah', cluster T8
`H5896G` — 'Ira', cluster T8
`H5988H` — 'Ammiel', cluster T8
`H5989J` — 'Ammihud', cluster T8
`H6021G` — 'Amasa', cluster T8
`H6086K` — 'tree: carpenter', cluster T2
`H6214G` — 'Asahel', cluster T8
`H6452B` — 'to limp', cluster T3
`H6560H` — 'Perez-uzzah', cluster T8
`H6659G` — 'Zadok', cluster T8
`H6767D` — 'banging', cluster T2
`H6807A` — 'marching', cluster T2
`H6872B` — 'pebble', cluster T2
`H7340I` — 'Rehob', cluster T8
`H7394G` — 'Rechab', cluster T8
`H7417B` — 'Rimmon', cluster T8
`H7462A` — 'House of Shepherds', cluster T3
`H7497A` — 'Rapha', cluster T8
`H7626I` — 'tribe: javelin', cluster T2
`H7626J` — 'tribe: ruler', cluster T2
`H7652A` — 'Sheba', cluster T8
`H7727G` — 'Shobab', cluster T8
`H7760B` — 'fate', cluster T3
`H8051H` — 'Shammua', cluster T8
`H8096H` — 'Shimei', cluster T8
`H8526H` — 'Talmai', cluster T8
`H8559H` — 'Tamar', cluster T8
`H8559I` — 'Tamar', cluster T8
`H0029H` — 'Abijah', cluster T8
`H0048H` — 'Abiram', cluster T8
`H0068I` — '[Zoheleth] Stone', cluster T10
`H0197G` — 'Hall [of pillars]', cluster T10
`H0197I` — 'Hall [of the Throne]', cluster T2
`H0274G` — 'Ahaziah', cluster T8
`H0281G` — 'Ahijah', cluster T8
`H0281H` — 'Ahijah', cluster T8
`H0281I` — 'Ahijah', cluster T8
`H0352B` — 'pillar', cluster T2
`H0359B` — 'Eloth', cluster T10
`H0387G` — 'Ethan', cluster T8
`H0425H` — 'Elah', cluster T8
`H0450H` — 'Eliada', cluster T8
`H0526G` — 'Amon', cluster T8
`H0609G` — 'Asa', cluster T8
`H0663I` — 'Aphek', cluster T10
`H0935O` — 'Lebo', cluster T10
`H0990I` — 'belly: hump', cluster T2
`H1004K` — 'House [of the Forests of Lebanon]', cluster T2
`H1130G` — 'Ben-hadad', cluster T8
`H1195G` — 'Baana', cluster T8
`H1568M` — '[Ramoth]-gilead', cluster T10
`H1908I` — 'Hadad', cluster T8
`H1964I` — 'temple: nave', cluster T2
`H1968G` — 'Heman', cluster T8
`H2174A` — 'Zimri', cluster T8
`H2436I` — 'bosom: lap', cluster T2
`H2438H` — 'Hiram', cluster T8
`H2490B` — 'to play flute', cluster T3
`H2607G` — 'Hanani', cluster T8
`H2682A` — 'grass', cluster T13
`H2977G` — 'Josiah', cluster T8
`H3058G` — 'Jehu', cluster T8
`H3088G` — 'Jehoram', cluster T8
`H3092I` — 'Jehoshaphat', cluster T8
`H3101H` — 'Joash', cluster T8
`H3129O` — 'Jonathan', cluster T8
`H3158H` — 'Jezreelite', cluster T10
`H3233H` — 'right: south', cluster T2
`H3293I` — '[House of] the Forest', cluster T10
`H3326B` — 'floor', cluster T2
`H3379G` — 'Jeroboam', cluster T8
`H3500H` — 'Jether', cluster T8
`H3521H` — 'Cabul', cluster T10
`H3672H` — 'Chinneroth', cluster T10
`H3678H` — '[Hall of] the Throne', cluster T2
`H3734A` — 'kor', cluster T2
`H3760H` — '[Mount] Carmel', cluster T10
`H3844J` — '[House of the Forest of] Lebanon', cluster T10
`H3899I` — 'food: allowance', cluster T2
`H4321G` — 'Micaiah', cluster T8
`H4436G` — 'Queen [of Sheba]', cluster T2
`H4445B` — 'Milcom', cluster T7
`H4551A` — 'quarry', cluster T2
`H4601K` — 'Maacah', cluster T8
`H4601Q` — 'Maacah', cluster T8
`H4629H` — 'gap', cluster T2
`H5070H` — 'Nadab', cluster T8
`H5216B` — 'lamp', cluster T12
`H5279A` — 'Naamah', cluster T8
`H5606B` — 'to suffice', cluster T3
`H5653G` — 'Abda', cluster T8
`H5662G` — 'Obadiah', cluster T8
`H5676I` — 'side: west', cluster T10
`H5806G` — 'Azubah', cluster T8
`H5838H` — 'Azariah', cluster T8
`H5982H` — '[Hall of] Pillars', cluster T10
`H6152B` — 'Arabia', cluster T10
`H6547K` — 'Pharaoh', cluster T8
`H6667G` — 'Zedekiah', cluster T8
`H6793C` — 'shield', cluster T2
`H6957B` — 'line', cluster T2
`H7049B` — 'to carve', cluster T3
`H7614J` — 'Sheba', cluster T10
`H7687G` — 'Segub', cluster T8
`H8042H` — 'left: north', cluster T2
`H8096I` — 'Shimei', cluster T8
`H8098A` — 'Shemaiah', cluster T8
`H8106A` — 'Shemer', cluster T8
`H8202H` — 'Shaphat', cluster T8
`H8453B` — 'Tishbe', cluster T2
`H8481H` — 'lower', cluster T2
`H8585A` — 'conduit', cluster T2
`H8607G` — 'Tiphsah', cluster T10
`H8656H` — 'Tirzah', cluster T10
`H0152G` — 'Adrammelech', cluster T8
`H0152H` — 'Adrammelech', cluster T8
`H0219B` — 'herb', cluster T13
`H0223G` — 'Uriah', cluster T8
`H0274H` — 'Ahaziah', cluster T8
`H0425I` — 'Elah', cluster T8
`H0471G` — 'Eliakim', cluster T8
`H0471I` — 'Eliakim', cluster T8
`H0476I` — 'Elishama', cluster T8
`H0494G` — 'Elnathan', cluster T8
`H0526H` — 'Amon', cluster T8
`H0549H` — 'Amana', cluster T10
`H0558G` — 'Amaziah', cluster T8
`H0623G` — 'Asaph', cluster T8
`H0669H` — 'Ephraim [Gate]', cluster T10
`H0709H` — 'Argob', cluster T8
`H0761H` — 'Syrian', cluster T11
`H1004H` — 'Beth [Haggan]', cluster T10
`H1130H` — 'Ben-hadad', cluster T8
`H1436B` — 'Gedaliah', cluster T8
`H1537H` — 'Gilgal', cluster T10
`H1588G` — 'Garden [of Uzza]', cluster T2
`H1588H` — '[Beth]-haggan', cluster T2
`H1954G` — 'Hoshea', cluster T8
`H2148C` — 'Zechariah', cluster T8
`H2148P` — 'Zechariah', cluster T8
`H2396G` — 'Hezekiah', cluster T8
`H2518G` — 'Hilkiah', cluster T8
`H2518H` — 'Hilkiah', cluster T8
`H2657G` — 'Hephzibah', cluster T2
`H2717C` — 'to slay', cluster T3
`H2970J` — 'Jezaniah', cluster T8
`H3003H` — 'Jabesh', cluster T8
`H3059G` — 'Jehoahaz', cluster T8
`H3059H` — 'Jehoahaz', cluster T8
`H3060G` — 'Jehoash', cluster T8
`H3060H` — 'Jehoash', cluster T8
`H3075G` — 'Jehozabad', cluster T8
`H3077H` — 'Jehoiada', cluster T8
`H3082G` — 'Jonadab', cluster T8
`H3088I` — 'Joram', cluster T8
`H3091I` — 'Joshua', cluster T8
`H3092J` — 'Jehoshaphat', cluster T8
`H3098G` — 'Joah', cluster T8
`H3099H` — 'Joahaz', cluster T8
`H3101I` — 'Joash', cluster T8
`H3107G` — 'Jozacar', cluster T8
`H3110G` — 'Johanan', cluster T8
`H3141H` — 'Joram', cluster T8
`H3141J` — 'Joram', cluster T8
`H3239A` — 'Janoah', cluster T10
`H3414G` — 'Jeremiah', cluster T8
`H3458H` — 'Ishmael', cluster T8
`H3470A` — 'Isaiah', cluster T8
`H3526G` — "Washer's", cluster T10
`H3739B` — 'to feed', cluster T3
`H4519H` — 'Manasseh', cluster T8
`H4853B` — 'oracle', cluster T2
`H4918G` — 'Meshullam', cluster T8
`H4932G` — 'Second [Quarter]', cluster T2
`H4977G` — 'Mattan', cluster T8
`H4983Q` — 'Mattaniah', cluster T8
`H5224H` — '[Pharaoh] Neco', cluster T8
`H5283I` — 'Naaman', cluster T8
`H5307M` — 'to fall: fell [trees]', cluster T3
`H5327B` — 'to desolate', cluster T3
`H5418G` — 'Nethaniah', cluster T8
`H5591B` — 'tempest', cluster T2
`H5718G` — 'Adaiah', cluster T8
`H5761I` — 'Avvite', cluster T10
`H5798G` — '[Garden of] Uzza', cluster T2
`H5907H` — 'Achbor', cluster T8
`H6222G` — 'Asaiah', cluster T8
`H6305G` — 'Pedaiah', cluster T8
`H6322G` — 'Pul', cluster T8
`H6438G` — 'Corner [Gate]', cluster T10
`H6485L` — 'to reckon: put', cluster T3
`H6547L` — 'Pharaoh', cluster T8
`H6547Q` — 'Pharaoh [Neco]', cluster T8
`H6547T` — 'Pharaoh', cluster T8
`H6659H` — 'Zadok', cluster T8
`H6667H` — 'Zedekiah', cluster T8
`H6846G` — 'Zephaniah', cluster T8
`H6979A` — 'to dig', cluster T3
`H7200M` — 'to see: approach', cluster T3
`H7247H` — 'Riblah', cluster T10
`H7249G` — 'Rab-saris', cluster T2
`H7323I` — 'to run: pieces', cluster T3
`H7394H` — 'Rechab', cluster T8
`H7414K` — 'Ramah', cluster T10
`H7417A` — 'Rimmon', cluster T7
`H7704H` — 'Field [of the Launderer]', cluster T10
`H7711A` — 'blight', cluster T2
`H7763G` — 'Shomer', cluster T8
`H7921C` — 'barrenness', cluster T3
`H7967G` — 'Shallum', cluster T8
`H7967H` — 'Shallum', cluster T8
`H8227B` — 'Shaphan', cluster T8
`H8272G` — 'Sharezer', cluster T8
`H8304H` — 'Seraiah', cluster T8
`H8304I` — 'Seraiah', cluster T8
`H8616G` — 'Tikvah', cluster T8
`H0001I` — 'father of [Gibeon]', cluster T2
`H0029J` — '`his father`', cluster T8
`H0032H` — 'Abihail', cluster T8
`H0044G` — 'Abiezer', cluster T8
`H0146H` — 'Addar', cluster T8
`H0198G` — 'Ulam', cluster T8
`H0198H` — 'Ulam', cluster T8
`H0222H` — 'Uriel', cluster T8
`H0281J` — 'Ahijah', cluster T8
`H0281M` — 'Ahijah', cluster T8
`H0288I` — 'Ahimelech', cluster T8
`H0387J` — 'Ethan', cluster T8
`H0445H` — 'Elhanan', cluster T8
`H0446K` — 'Eliab', cluster T8
`H0447G` — 'Eliel', cluster T8
`H0447M` — 'Eliel', cluster T8
`H0453H` — 'Elihu', cluster T8
`H0453I` — 'Elihu', cluster T8
`H0461K` — 'Eliezer', cluster T8
`H0499J` — 'Eleazar', cluster T8
`H0511K` — 'Elkanah', cluster T8
`H0609H` — 'Asa', cluster T8
`H0623H` — 'Asaph', cluster T8
`H0623K` — 'Asaph', cluster T8
`H0682A` — 'Azel', cluster T8
`H0758G` — 'Aram', cluster T8
`H0758K` — 'Aram [Maacah]', cluster T10
`H1004G` — 'Beth-[ashbea]', cluster T10
`H1106H` — 'Bela', cluster T8
`H1141H` — 'Benaiah', cluster T8
`H1141J` — 'Benaiah', cluster T8
`H1141K` — 'Benaiah', cluster T8
`H1168H` — 'Baal', cluster T10
`H1177H` — 'Baal-hanan', cluster T8
`H1283H` — 'Beriah', cluster T8
`H1283I` — 'Beriah', cluster T8
`H1283J` — 'Beriah', cluster T8
`H1296H` — 'Berechiah', cluster T8
`H1296I` — 'Berechiah', cluster T8
`H1323I` — 'Bath [Shua]', cluster T2
`H1436I` — 'Gedaliah', cluster T8
`H1446H` — 'Gedor', cluster T10
`H1516K` — 'Ge', cluster T10
`H1617I` — 'Gera', cluster T8
`H1647H` — 'Gershom', cluster T8
`H1734I` — 'Dodo', cluster T8
`H1840H` — 'Daniel', cluster T8
`H1908H` — 'Hadad', cluster T8
`H1913G` — 'Hadoram', cluster T8
`H1968I` — 'Heman', cluster T8
`H2066H` — 'Zabad', cluster T8
`H2067I` — 'Zabdi', cluster T8
`H2068G` — 'Zabdiel', cluster T8
`H2069K` — 'Zebadiah', cluster T8
`H2139J` — 'Zaccur', cluster T8
`H2147M` — 'Zichri', cluster T8
`H2148A` — 'Zechariah', cluster T8
`H2361G` — 'Hiram', cluster T8
`H2453G` — 'Hachmonite', cluster T11
`H2453H` — 'Hachmoni', cluster T8
`H2469H` — 'Heldai', cluster T8
`H2503G` — 'Helez', cluster T8
`H2526H` — 'Ham', cluster T10
`H2574H` — '[Zobah]-Hamath', cluster T2
`H2605H` — 'Hanan', cluster T8
`H2621H` — 'Hosah', cluster T8
`H2811I` — 'Hashabiah', cluster T8
`H2811J` — 'Hashabiah', cluster T8
`H3038G` — 'Jeduthun', cluster T8
`H3038H` — 'Jeduthun', cluster T8
`H3043G` — 'Jediael', cluster T8
`H3043I` — 'Jediael', cluster T8
`H3076G` — 'Johanan', cluster T8
`H3077I` — 'Jehoiada', cluster T8
`H3083K` — 'Jonathan', cluster T8
`H3097H` — 'Joab', cluster T8
`H3100J` — 'Joel', cluster T8
`H3100N` — 'Joel', cluster T8
`H3100O` — 'Joel', cluster T8
`H3101K` — 'Joash', cluster T8
`H3107H` — 'Jozabad', cluster T8
`H3107I` — 'Jozabad', cluster T8
`H3107J` — 'Jozabad', cluster T8
`H3130I` — 'Joseph', cluster T8
`H3157J` — 'Jezreel', cluster T8
`H3166G` — 'Jahaziel', cluster T8
`H3166H` — 'Jahaziel', cluster T8
`H3171G` — 'Jehiel', cluster T8
`H3171H` — 'Jehiel', cluster T8
`H3171I` — 'Jehiel', cluster T8
`H3189H` — 'Jahath', cluster T8
`H3226H` — 'Jamin', cluster T8
`H3258G` — 'Jabez', cluster T10
`H3258H` — 'Jabez', cluster T8
`H3266J` — 'Jeush', cluster T8
`H3273G` — 'Jeiel', cluster T8
`H3273I` — 'Jeiel', cluster T8
`H3273P` — 'Jeiel', cluster T8
`H3335H` — 'to form: potter', cluster T8
`H3396G` — 'Jerahmeel', cluster T8
`H3406G` — 'Jerimoth', cluster T8
`H3414H` — 'Jeremiah', cluster T8
`H3414I` — 'Jeremiah', cluster T8
`H3458I` — 'Ishmael', cluster T8
`H3469J` — 'Ishi', cluster T8
`H3470H` — 'Jeshaiah', cluster T8
`H3485H` — 'Issachar', cluster T8
`H3500I` — 'Jether', cluster T8
`H3500J` — 'Jether', cluster T8
`H3612H` — 'Caleb', cluster T8
`H3620H` — 'Chelub', cluster T8
`H3713A` — 'bowl', cluster T2
`H4060G` — 'huge', cluster T2
`H4317M` — 'Michael', cluster T8,T9
`H4506A` — 'Manahath', cluster T10
`H4506H` — 'Menuhoth', cluster T10
`H4601H` — '[Aram]-maacah', cluster T10
`H4601M` — 'Maacah', cluster T8
`H4601N` — 'Maacah', cluster T8
`H4601P` — 'Maacah', cluster T8
`H4641G` — 'Maaseiah', cluster T8
`H4732G` — 'Mikloth', cluster T8
`H4732H` — 'Mikloth', cluster T8
`H4762H` — 'Mareshah', cluster T8
`H4813H` — 'Miriam', cluster T8
`H4993G` — 'Mattithiah', cluster T8
`H4993H` — 'Mattithiah', cluster T8
`H5070I` — 'Nadab', cluster T8
`H5292B` — 'Naarah', cluster T8
`H5418H` — 'Nethaniah', cluster T8
`H5437I` — 'to turn: again', cluster T3
`H5660G` — 'Abdi', cluster T8
`H5662J` — 'Obadiah', cluster T8
`H5662K` — 'Obadiah', cluster T8
`H5677I` — 'Eber', cluster T8
`H5734G` — 'Adnah', cluster T8
`H5744J` — 'Obed', cluster T8
`H5806H` — 'Azubah', cluster T8
`H5812G` — 'Azaziah', cluster T8
`H5813H` — 'Uzzi', cluster T8
`H5813I` — 'Uzzi', cluster T8
`H5816I` — 'Uzziel', cluster T8
`H5818I` — 'Uzziah', cluster T8
`H5820J` — 'Azmaveth', cluster T8
`H5829K` — 'Ezer', cluster T8
`H5837G` — 'Azriel', cluster T8
`H5840H` — 'Azrikam', cluster T8
`H5862H` — 'Etam', cluster T10
`H5896H` — 'Ira', cluster T8
`H5988I` — 'Ammiel', cluster T8
`H5992H` — 'Amminadab', cluster T8
`H6022H` — 'Amasai', cluster T8
`H6042G` — 'Unni', cluster T8
`H6081H` — 'Epher', cluster T8
`H6081I` — 'Epher', cluster T8
`H6084I` — 'Ophrah', cluster T8
`H6147H` — 'Er', cluster T8
`H6222K` — 'Asaiah', cluster T8
`H6262G` — 'Attai', cluster T8
`H6431H` — 'Peleth', cluster T8
`H6560G` — 'Perez-uzza', cluster T10
`H6678H` — 'Zobah', cluster T10
`H6981G` — 'Kore', cluster T8
`H7027H` — 'Kish', cluster T8
`H7410H` — 'Ram', cluster T8
`H7497H` — 'Raphaite', cluster T10
`H7509I` — 'Rephaiah', cluster T8
`H7552J` — 'Rakem', cluster T8
`H7687H` — 'Segub', cluster T8
`H7732H` — 'Shobal', cluster T8
`H7883H` — 'Nile', cluster T10
`H7928H` — 'Shechem', cluster T8
`H7967M` — 'Shallum', cluster T8
`H8018O` — 'Shelemiah', cluster T8
`H8019J` — 'Shelomoth', cluster T8
`H8050I` — 'Shemuel', cluster T8
`H8060G` — 'Shammai', cluster T8
`H8060I` — 'Shammai', cluster T8
`H8087H` — 'Shema', cluster T8
`H8087I` — 'Shema', cluster T8
`H8092H` — 'Shimea', cluster T8
`H8092I` — 'Shimea', cluster T8
`H8096K` — 'Shimei', cluster T8
`H8096O` — 'Shimei', cluster T8
`H8098F` — 'Shemaiah', cluster T8
`H8098G` — 'Shemaiah', cluster T8
`H8098I` — 'Shemaiah', cluster T8
`H8189H` — 'Shaaraim', cluster T10
`H8202K` — 'Shaphat', cluster T8
`H8203J` — 'Shephatiah', cluster T8
`H8206G` — 'Shuppim', cluster T8
`H8206H` — 'Shuppim', cluster T8
`H8289H` — 'Sharon', cluster T10
`H8289I` — 'Sharon', cluster T10
`H8304J` — 'Seraiah', cluster T8
`H8439G` — 'Tola', cluster T8
`H0001H` — '[Huram]-abi', cluster T8
`H0029I` — 'Abijah', cluster T8
`H0029N` — 'Abijah', cluster T8
`H0222I` — 'Uriel', cluster T8
`H0447N` — 'Eliel', cluster T8
`H0450I` — 'Eliada', cluster T8
`H0461L` — 'Eliezer', cluster T8
`H0511N` — 'Elkanah', cluster T8
`H0568J` — 'Amariah', cluster T8
`H0568K` — 'Amariah', cluster T8
`H1141L` — 'Benaiah', cluster T8
`H1141M` — 'Benaiah', cluster T8
`H1162H` — 'Boaz', cluster T12
`H1296J` — 'Berechiah', cluster T8
`H1390G` — 'Gibeah', cluster T10
`H1516L` — '[Zephathah] Valley', cluster T10
`H1516M` — 'Valley [Gate]', cluster T10
`H1696H` — 'to speak: subdue', cluster T3
`H1709G` — 'Fish [Gate]', cluster T10
`H1913B` — 'Hadoram', cluster T8
`H2066M` — 'Zabad', cluster T8
`H2069M` — 'Zebadiah', cluster T8
`H2147N` — 'Zichri', cluster T8
`H2147O` — 'Zichri', cluster T8
`H2147P` — 'Zichri', cluster T8
`H2148H` — 'Zechariah', cluster T8
`H2148I` — 'Zechariah', cluster T8
`H2148L` — 'Zechariah', cluster T8
`H2148N` — 'Zechariah', cluster T8
`H2148O` — 'Zechariah', cluster T8
`H2226K` — 'Zerah', cluster T8
`H2361I` — 'Huram', cluster T8
`H2361J` — 'Hiram', cluster T8
`H2608Q` — 'Hananiah', cluster T8
`H2811L` — 'Hashabiah', cluster T8
`H3059I` — 'Ahaziah', cluster T8
`H3075I` — 'Jehozabad', cluster T8
`H3076J` — 'Jehohanan', cluster T8
`H3076K` — 'Jehohanan', cluster T8
`H3076L` — 'Johanan', cluster T8
`H3098J` — 'Joah', cluster T8
`H3098K` — 'Joah', cluster T8
`H3098L` — 'Joah', cluster T8
`H3099G` — 'Joahaz', cluster T8
`H3099I` — 'Jehoahaz', cluster T8
`H3100Q` — 'Joel', cluster T8
`H3107K` — 'Jozabad', cluster T8
`H3107L` — 'Jozabad', cluster T8
`H3166J` — 'Jahaziel', cluster T8
`H3169G` — 'Jehizkiah', cluster T8
`H3171L` — 'Jehiel', cluster T8
`H3171M` — 'Jehiel', cluster T8
`H3189K` — 'Jahath', cluster T8
`H3247G` — '[Gate of the] Foundation', cluster T2
`H3273J` — 'Jeiel', cluster T8
`H3273K` — 'Jeiel', cluster T8
`H3273M` — 'Jeiel', cluster T8
`H3395M` — 'Jeroham', cluster T8
`H3406O` — 'Jerimoth', cluster T8
`H3442H` — 'Jeshua', cluster T8
`H3458J` — 'Ishmael', cluster T8
`H3458K` — 'Ishmael', cluster T8
`H3466G` — 'Jeshanah', cluster T10
`H3947K` — 'to take: buy', cluster T3
`H4245A` — 'sickness', cluster T2
`H4287G` — 'Mahath', cluster T8
`H4287H` — 'Mahath', cluster T8
`H4318M` — 'Micah', cluster T8
`H4318N` — 'Micaiah', cluster T8
`H4322G` — 'Micaiah', cluster T8
`H4322H` — 'Micaiah', cluster T8
`H4641H` — 'Maaseiah', cluster T8
`H4641I` — 'Maaseiah', cluster T8
`H4641J` — 'Maaseiah', cluster T8
`H4641K` — 'Maaseiah', cluster T8
`H4740G` — 'Angle', cluster T2
`H4918N` — 'Meshullam', cluster T8
`H4983I` — 'Mattaniah', cluster T8
`H5184H` — 'Nahath', cluster T8
`H5224G` — 'Neco', cluster T8
`H5274B` — 'to shoe', cluster T3
`H5401B` — 'to handle', cluster T3
`H5417L` — 'Nethanel', cluster T8
`H5417M` — 'Nethanel', cluster T8
`H5553G` — 'rock', cluster T2
`H5658K` — 'Abdon', cluster T8
`H5660H` — 'Abdi', cluster T8
`H5662N` — 'Obadiah', cluster T8
`H5662O` — 'Obadiah', cluster T8
`H5714I` — 'Iddo', cluster T8
`H5718J` — 'Adaiah', cluster T8
`H5731A` — 'Eden', cluster T8
`H5731G` — 'Eden', cluster T8
`H5734H` — 'Adnah', cluster T8
`H5744K` — 'Obed', cluster T8
`H5752G` — 'Oded', cluster T8
`H5752H` — 'Oded', cluster T8
`H5812I` — 'Azaziah', cluster T8
`H5838G` — 'Azariah', cluster T8
`H5838M` — 'Azariah', cluster T8
`H5838N` — 'Azariah', cluster T8
`H5838O` — 'Azariah', cluster T8
`H5838P` — 'Azariah', cluster T8
`H5838S` — 'Azariah', cluster T8
`H5838T` — 'Azariah', cluster T8
`H5838U` — 'Azariah', cluster T8
`H5838V` — 'Azariah', cluster T8
`H5840J` — 'Azrikam', cluster T8
`H5984G` — 'Meunite', cluster T11
`H6010H` — 'Valley [of Beracah]', cluster T10
`H6021H` — 'Amasa', cluster T8
`H6022J` — 'Amasai', cluster T8
`H6085I` — 'Ephron', cluster T8
`H6163B` — 'Arabian', cluster T11
`H6214I` — 'Asahel', cluster T8
`H6437H` — 'Corner [Gate]', cluster T10
`H6981H` — 'Kore', cluster T8
`H6999C` — 'incense-altar', cluster T12
`H7027I` — 'Kish', cluster T8
`H7183B` — 'attentive', cluster M41
`H7531A` — 'pavement', cluster T2
`H7755I` — 'Soco', cluster T8
`H7935I` — 'Shecaniah', cluster T8
`H7967N` — 'Shallum', cluster T8
`H8096Q` — 'Shimei', cluster T8
`H8098L` — 'Shemaiah', cluster T8
`H8098M` — 'Shemaiah', cluster T8
`H0221I` — 'Uri', cluster T8
`H0223H` — 'Uriah', cluster T8
`H0461M` — 'Eliezer', cluster T8
`H0461N` — 'Eliezer', cluster T8
`H0475I` — 'Eliashib', cluster T8
`H0475J` — 'Eliashib', cluster T8
`H0494H` — 'Elnathan', cluster T8
`H0494I` — 'Elnathan', cluster T8
`H0494J` — 'Elnathan', cluster T8
`H0499K` — 'Eleazar', cluster T8
`H0564I` — 'Immer', cluster T10
`H0671A` — 'governors', cluster T2
`H0671B` — 'governors', cluster T2
`H0740G` — 'Ariel', cluster T8
`H0783A` — 'Artaxerxes', cluster T8
`H0783B` — 'Artaxerxes', cluster T8
`H1131H` — 'Binnui', cluster T8
`H1196I` — 'Baanah', cluster T8
`H1247G` — 'son: descendant/people', cluster T2
`H1271I` — 'Barzillai', cluster T8
`H1436A` — 'Gedaliah', cluster T8
`H1799B` — 'record', cluster T2
`H1867H` — 'Darius', cluster T8
`H1868G` — 'Darius', cluster T8
`H2148B` — 'Zechariah', cluster T8
`H2148S` — 'Zechariah', cluster T8
`H2292B` — 'Haggai', cluster T8
`H2582G` — 'Henadad', cluster T8
`H2818B` — 'necessity', cluster T2
`H2870A` — 'Tabeel', cluster T8
`H3063L` — 'Judah', cluster T8
`H3063N` — 'Judea', cluster T10
`H3076M` — 'Jehohanan', cluster T8
`H3107M` — 'Jozabad', cluster T8
`H3129I` — 'Jonathan', cluster T8
`H3136A` — 'Jozadak', cluster T8
`H3136G` — 'Jozadak', cluster T8
`H3171O` — 'Jehiel', cluster T8
`H3273N` — 'Jeuel', cluster T8
`H3402G` — 'Jarib', cluster T8
`H3402H` — 'Jarib', cluster T8
`H3442G` — 'Jeshua', cluster T8
`H3442J` — 'Jeshua', cluster T8
`H3442K` — 'Jeshua', cluster T8
`H3442P` — 'Jeshua', cluster T8
`H3734B` — 'kor', cluster T2
`H4641L` — 'Maaseiah', cluster T8
`H4782G` — 'Mordecai', cluster T8
`H4918O` — 'Meshullam', cluster T8
`H4918P` — 'Meshullam', cluster T8
`H4990G` — 'Mithredath', cluster T8
`H4990H` — 'Mithredath', cluster T8
`H5103G` — 'River', cluster T10
`H5129G` — 'Noadiah', cluster T8
`H5166G` — 'Nehemiah', cluster T8
`H5415I` — 'to give: pay', cluster T3
`H5416K` — 'Nathan', cluster T8
`H5642B` — 'to destroy', cluster M10
`H5714J` — 'Iddo', cluster T8
`H5838L` — 'Azariah', cluster T8
`H5867B` — 'Elam', cluster T8
`H6214J` — 'Asahel', cluster T8
`H6372I` — 'Phinehas', cluster T8
`H6572A` — 'copy', cluster T2
`H6976I` — 'Hakkoz', cluster T8
`H7348A` — 'Rehum', cluster T8
`H7348B` — 'Rehum', cluster T8
`H7597A` — 'Shealtiel', cluster T8
`H7678G` — 'Shabbethai', cluster T8
`H7761I` — 'to set: appoint', cluster T3
`H7935L` — 'Shecaniah', cluster T8
`H7936A` — 'to hire', cluster T3
`H7967O` — 'Shallum', cluster T8
`H8098N` — 'Shemaiah', cluster T8
`H8098O` — 'Shemaiah', cluster T8
`H8274G` — 'Sherebiah', cluster T8
`H8304L` — 'Seraiah', cluster T8
`H8616H` — 'Tikvah', cluster T8
`H0223I` — 'Uriah', cluster T8
`H0475M` — 'Eliashib', cluster T8
`H0475N` — 'Eliashib', cluster T8
`H0475O` — 'Eliashib', cluster T8
`H0499M` — 'Eleazar', cluster T8
`H0564J` — 'Immer', cluster T8
`H0568N` — 'Amariah', cluster T8
`H0623I` — 'Asaph', cluster T8
`H0623J` — 'Asaph', cluster T8
`H0669I` — 'Ephraim [Gate]', cluster T10
`H0830G` — 'Dung [Gate]', cluster T2
`H1004A` — 'place', cluster T2
`H1131K` — 'Binnui', cluster T8
`H1131L` — 'Binnui', cluster T8
`H1137L` — 'Bani', cluster T8
`H1137M` — 'Bani', cluster T8
`H1137N` — 'Bani', cluster T8
`H1137O` — 'Bani', cluster T8
`H1144J` — 'Benjamin', cluster T8
`H1195I` — 'Baana', cluster T8
`H1263G` — 'Baruch', cluster T8
`H1295G` — '[Shelah] Pool', cluster T10
`H1296K` — 'Berechiah', cluster T8
`H1419B` — 'Haggedolim', cluster T8
`H1769H` — 'Dibon', cluster T10
`H1806J` — 'Delaiah', cluster T8
`H1867G` — 'Darius', cluster T8
`H2067J` — 'Zabdi', cluster T8
`H2068H` — 'Zabdiel', cluster T8
`H2139L` — 'Zaccur', cluster T8
`H2139N` — 'Zaccur', cluster T8
`H2147Q` — 'Zichri', cluster T8
`H2148U` — 'Zechariah', cluster T8
`H2148V` — 'Zechariah', cluster T8
`H2148X` — 'Zechariah', cluster T8
`H2346H` — '[Broad] Wall', cluster T2
`H2354I` — 'Hur', cluster T8
`H2518K` — 'Hilkiah', cluster T8
`H2582H` — 'Henadad', cluster T8
`H2582I` — 'Henadad', cluster T8
`H2586H` — 'Hanun', cluster T8
`H2586I` — 'Hanun', cluster T8
`H2605K` — 'Hanan', cluster T8
`H2605N` — 'Hanan', cluster T8
`H2607J` — 'Hanani', cluster T8
`H2608G` — 'Hananiah', cluster T8
`H2608H` — 'Hananiah', cluster T8
`H2608J` — 'Hananiah', cluster T8
`H2608S` — 'Hananiah', cluster T8
`H2720B` — 'desolate', cluster T2
`H2811M` — 'Hashabiah', cluster T8
`H2811N` — 'Hashabiah', cluster T8
`H2811O` — 'Hashabiah', cluster T8
`H2813G` — 'Hashabneiah', cluster T8
`H2813H` — 'Hashabneiah', cluster T8
`H2815H` — 'Hasshub', cluster T8
`H2815I` — 'Hasshub', cluster T8
`H2900I` — 'Tobiah', cluster T8
`H3063I` — 'Judah', cluster T8
`H3063M` — 'Judah', cluster T8
`H3076O` — 'Jehohanan', cluster T8
`H3076Q` — 'Jehohanan', cluster T8
`H3100S` — 'Joel', cluster T8
`H3107P` — 'Jozabad', cluster T8
`H3107Q` — 'Jozabad', cluster T8
`H3110L` — 'Johanan', cluster T8
`H3111G` — 'Joiada', cluster T8
`H3111H` — 'Joiada', cluster T8
`H3226I` — 'Jamin', cluster T8
`H3395J` — 'Jeroham', cluster T8
`H3414M` — 'Jeremiah', cluster T8
`H3442L` — 'Jeshua', cluster T8
`H3442N` — 'Jeshua', cluster T8
`H3442O` — 'Jeshua', cluster T8
`H3465G` — '[Gate of] Yeshanah', cluster T2
`H3466H` — '[Gate of] Yeshanah', cluster T2
`H3715B` — 'Hakkephirim', cluster T10
`H4026G` — '[Hananel] Tower', cluster T2
`H4026H` — 'Tower [of the Hundred]', cluster T2
`H4026I` — 'Tower [Of the Ovens]', cluster T2
`H4060B` — 'tribute', cluster T2
`H4105H` — 'Mehetabel', cluster T8
`H4111H` — 'Mahalalel', cluster T8
`H4217G` — 'East [Gate]', cluster T10
`H4307G` — '[Gate of the] Guard', cluster T2
`H4316I` — 'Mica', cluster T8
`H4318L` — 'Mica', cluster T8
`H4325H` — 'Water [Gate]', cluster T2
`H4332H` — 'Mishael', cluster T8
`H4428J` — "King's", cluster T2
`H4441H` — 'Malchijah', cluster T8
`H4441M` — 'Malchijah', cluster T8
`H4441N` — 'Malchijah', cluster T8
`H4441O` — 'Malchijah', cluster T8
`H4441P` — 'Malchijah', cluster T8
`H4441R` — 'Malchijah', cluster T8
`H4641P` — 'Maaseiah', cluster T8
`H4641Q` — 'Maaseiah', cluster T8
`H4641R` — 'Maaseiah', cluster T8
`H4641W` — 'Maaseiah', cluster T8
`H4662G` — 'Muster [Gate]', cluster T2
`H4898G` — 'Meshezabel', cluster T8
`H4898I` — 'Meshezabel', cluster T8
`H4918R` — 'Meshullam', cluster T8
`H4918S` — 'Meshullam', cluster T8
`H4918T` — 'Meshullam', cluster T8
`H4918Z` — 'Meshullam', cluster T8
`H4924C` — 'fat piece', cluster T2
`H4983G` — 'Mattaniah', cluster T8
`H4983O` — 'Mattaniah', cluster T8
`H4983P` — 'Mattaniah', cluster T8
`H4993J` — 'Mattithiah', cluster T8
`H5129H` — 'Noadiah', cluster T8
`H5166H` — 'Nehemiah', cluster T8
`H5166I` — 'Nehemiah', cluster T8
`H5483B` — 'Horse [Gate]', cluster T10
`H5653H` — 'Abda', cluster T8
`H5718I` — 'Adaiah', cluster T8
`H5800B` — 'to restore', cluster T3
`H5813K` — 'Uzzi', cluster T8
`H5813M` — 'Uzzi', cluster T8
`H5816L` — 'Uzziel', cluster T8
`H5818K` — 'Uzziah', cluster T8
`H5820K` — 'Azmaveth', cluster T10
`H5829I` — 'Ezer', cluster T8
`H5829J` — 'Ezer', cluster T8
`H5838W` — 'Azariah', cluster T8
`H5838X` — 'Azariah', cluster T8
`H5838Y` — 'Azariah', cluster T8
`H5867I` — 'Elam', cluster T8
`H5867J` — 'Elam', cluster T8
`H5869B` — 'Fountain [Gate]', cluster T10
`H5869G` — 'Fountain of [Drangons]', cluster T10
`H6042H` — 'Unni', cluster T8
`H6126H` — 'Akkub', cluster T8
`H6126J` — 'Akkub', cluster T8
`H6305K` — 'Pedaiah', cluster T8
`H6305M` — 'Pedaiah', cluster T8
`H6355H` — 'Pahath-moab', cluster T8
`H6355I` — 'Pahath-moab', cluster T8
`H6454I` — 'Paseah', cluster T8
`H6551J` — 'Parosh', cluster T8
`H6583G` — 'Pashhur', cluster T8
`H6611I` — 'Pethahiah', cluster T8
`H6611J` — 'Pethahiah', cluster T8
`H6629H` — 'Sheep [Gate]', cluster T10
`H6659J` — 'Zadok', cluster T8
`H6659K` — 'Zadok', cluster T8
`H6659M` — 'Zadok', cluster T8
`H6667J` — 'Zedekiah', cluster T8
`H6976J` — 'Hakkoz', cluster T8
`H7133B` — 'offering', cluster T2
`H7183A` — 'attentive', cluster M41
`H7342G` — 'Broad', cluster T2
`H7348G` — 'Rehum', cluster T8
`H7394I` — 'Rechab', cluster T8
`H7509J` — 'Rephaiah', cluster T8
`H7645H` — 'Shebaniah', cluster T8
`H7663A` — 'to inspect', cluster T3
`H7678H` — 'Shabbethai', cluster T8
`H7678I` — 'Shabbethai', cluster T8
`H7935M` — 'Shecaniah', cluster T8
`H7967Q` — 'Shallum', cluster T8
`H7975A` — 'Shelah', cluster T2
`H8018I` — 'Shelemiah', cluster T8
`H8018J` — 'Shelemiah', cluster T8
`H8051J` — 'Shammua', cluster T8
`H8087J` — 'Shema', cluster T8
`H8098R` — 'Shemaiah', cluster T8
`H8098S` — 'Shemaiah', cluster T8
`H8098W` — 'Shemaiah', cluster T8
`H8203N` — 'Shephatiah', cluster T8
`H8274H` — 'Sherebiah', cluster T8
`H8574G` — '[Tower of] the Ovens', cluster T10
`H8577B` — 'Dragon', cluster T10
`H0032K` — 'Abihail', cluster T8
`H0219A` — 'light', cluster T2
`H0349C` — 'how?', cluster T2
`H1540J` — 'to reveal: proclaim', cluster T3
`H2726G` — 'Harbona', cluster T8
`H2726H` — 'Harbona', cluster T8
`H2971J` — 'Jair', cluster T8
`H4436H` — 'queen', cluster T2
`H4782H` — 'Mordecai', cluster T8
`H4916B` — 'sending', cluster T2
`H6572B` — 'copy', cluster T2
`H7027J` — 'Kish', cluster T8
`H8096U` — 'Shimei', cluster T8
`H8336A` — 'alabaster', cluster T2
`H8659J` — 'Tarshish', cluster T8
`H0453K` — 'Elihu', cluster T8
`H0464H` — 'Eliphaz', cluster T8
`H0838A` — 'step', cluster T2
`H0838B` — 'step', cluster T2
`H1250B` — 'field', cluster T2
`H1430B` — 'tomb', cluster T2
`H1460B` — 'midst', cluster T2
`H2131B` — 'fetter', cluster T2
`H2490A` — 'to bore', cluster T3
`H2491H` — 'slain: wounded', cluster T2
`H2529B` — 'heat', cluster T2
`H2686A` — 'to divide', cluster T3
`H2706I` — 'statute: allotment', cluster T2
`H3117H` — 'day: old', cluster T2
`H3277H` — 'goat', cluster T2
`H3559B` — 'blow', cluster T2
`H3669B` — 'merchant', cluster T2
`H3685G` — 'Orion', cluster T2
`H3886B` — 'to talk wildly', cluster T3
`H4148H` — 'discipline: instruction', cluster T2
`H4148I` — 'discipline: bonds', cluster T2
`H4551B` — 'missile', cluster T2
`H4685B` — 'net', cluster T2
`H5170A` — 'snorting', cluster T2
`H5362A` — 'to strike', cluster T3
`H5410A` — 'path', cluster T2
`H5526A` — 'to fence', cluster T3
`H5526F` — 'to weave', cluster T3
`H5587B` — 'disquietings', cluster FLAG,T2
`H5599A` — 'outpouring', cluster T2
`H5607B` — 'sufficiency', cluster T2
`H5710A` — 'to advance', cluster T3
`H5774B` — 'gloom', cluster T2
`H5848A` — 'to turn aside', cluster M11
`H6211A` — 'moth', cluster T13
`H6327D` — 'to shatter', cluster T3
`H6767B` — 'spear', cluster T12
`H6924I` — 'front: forward', cluster T2
`H7070J` — 'branch: shoulder', cluster T13,T14
`H7105B` — 'foliage', cluster T2
`H7200K` — 'to see: enjoy', cluster T3
`H7280A` — 'to disturb', cluster T3
`H7410I` — 'Ram', cluster T8
`H7614G` — 'Sheba', cluster T8
`H7685A` — 'to grow', cluster T3
`H7699B` — 'breast', cluster T2
`H7722B` — 'devastation', cluster M55
`H7771A` — 'rich', cluster T2
`H8302A` — 'lance', cluster T2
`H8433B` — 'argument', cluster T2
`H8602A` — 'insipid', cluster T2
`H0047G` — 'mighty: ox', cluster T13
`H0047J` — 'mighty: angel', cluster M23
`H1760A` — 'to thrust', cluster T3
`H1817A` — 'door', cluster T2
`H2123A` — 'creature', cluster T2
`H2560A` — 'to aggitate', cluster T3
`H3293G` — 'Jaar', cluster T10
`H3512B` — 'disheartened', cluster M20
`H3563B` — 'owl', cluster T13
`H3733B` — 'pasture', cluster T2
`H3833A` — 'lion', cluster T13
`H4057A` — 'mouth', cluster T2
`H4364B` — 'net', cluster T2
`H4455B` — 'jaw', cluster T14
`H4480B` — 'portion', cluster T2
`H4659B` — 'deed', cluster T2
`H4686A` — 'net', cluster T2
`H4902H` — 'Meshech', cluster T10
`H4911A` — 'to liken', cluster T3
`H5102B` — 'to shine', cluster T3
`H5116B` — 'dwelling', cluster T2
`H5258B` — 'to install', cluster T3
`H5387B` — 'mist', cluster T2
`H5526C` — 'to weave', cluster T3
`H5612B` — 'scroll', cluster T12
`H5848B` — 'to envelope', cluster T3
`H5849B` — 'to crown', cluster T3
`H6010L` — 'Valley [of Topheth]', cluster T10
`H6670B` — 'to shine', cluster T3
`H7285A` — 'throng', cluster T2
`H7285B` — 'scheming', cluster T2
`H7462C` — 'to accompany', cluster T3
`H7641A` — 'stream', cluster T2
`H7692G` — 'Shiggaion', cluster T2
`H7722A` — 'ravage', cluster T2
`H7991A` — 'third', cluster T2
`H7997B` — 'to loot', cluster T3
`H8210J` — 'to pour: scatter', cluster T3
`H0310B` — 'backwards', cluster T2
`H1460A` — 'back', cluster T2
`H2131A` — 'missile', cluster T2
`H2436J` — 'bosom: secret', cluster T2
`H2506B` — 'smoothness', cluster T2
`H2742D` — 'gold', cluster T2
`H3513I` — 'to honor: many', cluster M71,T3
`H3856B` — 'to amaze', cluster T3
`H4659A` — 'work', cluster T2
`H4881A` — 'hedge', cluster T2
`H5433A` — 'to imbibe', cluster T3
`H6106I` — 'bone: body', cluster T2
`H6612B` — 'simplicity', cluster T2
`H6735B` — 'hinge', cluster T2
`H6793B` — 'coolness', cluster T2
`H6867A` — 'burning', cluster T2
`H6892A` — 'vomit', cluster T2
`H7342I` — 'broad: arrogant', cluster M08
`H7389A` — 'poverty', cluster T2
`H7389B` — 'poverty', cluster T2
`H1861B` — 'goad', cluster T2
`H2363B` — 'to enjoy', cluster T3
`H4685A` — 'siegework', cluster T2
`H4685C` — 'net', cluster T2
`H5533A` — 'to endanger', cluster T3
`H6001B` — 'laborious', cluster T2
`H6131A` — 'to uproot', cluster T3
`H1713A` — 'to look', cluster T3
`H1803A` — 'hair', cluster T2
`H3724C` — 'henna', cluster T2
`H5132B` — 'to bud', cluster T3
`H5437J` — 'to turn: repell', cluster T3
`H6677B` — 'necklace', cluster T12
`H7298B` — 'lock', cluster T2
`H7447A` — 'drop', cluster T2
`H0217A` — 'flame', cluster T2
`H0217B` — 'flame', cluster T2
`H0352D` — 'terebinth', cluster T2
`H0520B` — 'foundation', cluster T2
`H0740H` — 'Ariel', cluster T10
`H1004J` — 'House [of the Forest]', cluster T2
`H1166G` — 'Married', cluster T3
`H1238B` — 'to empty', cluster T3
`H1350B` — 'redemption', cluster T2
`H1754A` — 'circle', cluster T3
`H1754B` — 'ball', cluster T2
`H1817B` — 'door', cluster T2
`H1826B` — 'to wail', cluster T3
`H1870H` — 'Way', cluster T2
`H2123B` — 'abundance', cluster T2
`H2151A` — 'to shake', cluster T3
`H2721B` — 'desolation', cluster T2
`H2778B` — 'to winter', cluster T3
`H2791B` — 'craftily', cluster T2
`H2793H` — 'wood', cluster T2
`H2870B` — 'Tabeal', cluster T8
`H3068I` — '[Jerusalem of] the Lord', cluster T10
`H3685H` — 'constellation', cluster T2
`H3919C` — 'Laishah', cluster T10
`H4224A` — 'hiding-place', cluster T2
`H4294J` — 'tribe: stick', cluster T2
`H4364A` — 'net', cluster T2
`H4365B` — 'net', cluster T2
`H4414A` — 'to dissipate', cluster T3
`H4654B` — 'ruin', cluster M55
`H4685D` — 'stronghold', cluster T2
`H4714I` — '[Sea of] Egypt', cluster T2
`H4718B` — 'hole', cluster T2
`H4881B` — 'hedge', cluster T2
`H4893A` — 'mutilation', cluster M53
`H4937B` — 'support', cluster M70
`H4938A` — 'support', cluster M70
`H5015B` — 'Nebo', cluster T7
`H5158G` — 'Brook', cluster T10
`H5183B` — 'descent', cluster T2
`H5218A` — 'stricken', cluster T2
`H5299A` — 'sieve', cluster T2
`H5483A` — 'swallow', cluster T13
`H5533B` — 'to impoverish', cluster T3
`H5612I` — 'scroll: read', cluster T12
`H5697B` — 'Eglath-shelishiyah', cluster T10
`H5737B` — 'to hoe', cluster T3
`H5800G` — 'Forsaken', cluster T10
`H5891J` — 'Ephah', cluster T2
`H5892G` — 'City [of On]', cluster T2
`H5892I` — 'city [of God]', cluster T2
`H5953C` — 'to mock', cluster M08
`H6090B` — 'idol', cluster T2
`H6105B` — 'to shut eyes', cluster T3
`H6121B` — 'steep', cluster T2
`H6152A` — 'Arabia', cluster T10
`H6155G` — '[Brook of] Willows', cluster T2
`H6163A` — 'Arab', cluster T11
`H6288B` — 'bough', cluster T2
`H6322H` — 'Pul', cluster T10
`H6767A` — 'buzzing', cluster T2
`H6807B` — 'bracelette', cluster T2
`H6848A` — 'serpent', cluster T2
`H6848B` — 'serpent', cluster T2
`H6892B` — 'vomit', cluster T2
`H6957A` — 'cord', cluster M03,T12
`H7024A` — 'Kir', cluster T10
`H7070K` — 'branch: scales', cluster T13
`H7097B` — 'end', cluster T2
`H7203B` — 'vision', cluster T2
`H7531B` — 'glowing stone', cluster T2
`H7628B` — 'captive', cluster T3
`H7641G` — 'Euphrates', cluster T10
`H7971M` — 'to send: exile', cluster T3
`H7975B` — 'Shiloah', cluster T10
`H8077G` — 'Desolate', cluster T10
`H8178B` — 'storm', cluster T13
`H8314B` — 'Seraph', cluster T9
`H8321A` — 'vine', cluster T13
`H8388B` — 'to delimit', cluster T3
`H8422H` — 'Tubal', cluster T10
`H0223B` — 'Uriah', cluster T8
`H0256H` — 'Ahab', cluster T8
`H0476L` — 'Elishama', cluster T8
`H0494K` — 'Elnathan', cluster T8
`H0501J` — 'Elasah', cluster T8
`H0564H` — 'Immer', cluster T8
`H0669J` — '[Mount] Ephraim', cluster T10
`H1053J` — 'Heliopolis', cluster T10
`H1144L` — 'Benjamin [Gate]', cluster T10
`H1224H` — 'Bozrah', cluster T10
`H1263J` — 'Baruch', cluster T8
`H1436G` — 'Gedaliah', cluster T8
`H1436J` — 'Gedaliah', cluster T8
`H1516S` — 'Valley', cluster T10
`H1587G` — 'Gemariah', cluster T8
`H1587H` — 'Gemariah', cluster T8
`H1699B` — 'statement', cluster T3
`H1719A` — 'Dedan', cluster T10
`H1760B` — 'to thrust', cluster T3
`H1806K` — 'Delaiah', cluster T8
`H2028G` — '[Topheth of] Slaughter', cluster T10
`H2028H` — 'slaughter', cluster T2
`H2319G` — 'New [Gate]', cluster T2
`H2518M` — 'Hilkiah', cluster T8
`H2608A` — 'Hananiah', cluster T8
`H2608M` — 'Hananiah', cluster T8
`H2608N` — 'Hananiah', cluster T8
`H2674K` — 'Hazor', cluster T10
`H2970G` — 'Jaazaniah', cluster T8
`H3077J` — 'Jehoiada', cluster T8
`H3083N` — 'Jonathan', cluster T8
`H3122H` — 'Jonadab', cluster T8
`H3270H` — '[Sea of] Jazer', cluster T10
`H3396I` — 'Jerahmeel', cluster T8
`H3414N` — 'Jeremiah', cluster T8
`H3820B` — 'Leb', cluster T10
`H3866H` — 'Lydian', cluster T8
`H4321H` — 'Micaiah', cluster T8
`H4428H` — '`the king`', cluster T2
`H4428K` — 'Milcom', cluster T7
`H4441S` — 'Malchiah', cluster T8
`H4641X` — 'Maaseiah', cluster T8
`H4641Y` — 'Maaseiah', cluster T8
`H4869B` — 'Misgab', cluster T2
`H4977H` — 'Mattan', cluster T8
`H5170B` — 'snorting', cluster T2
`H5271B` — 'youth', cluster T2
`H5418J` — 'Nethaniah', cluster T8
`H5809H` — 'Azzur', cluster T8
`H5837I` — 'Azriel', cluster T8
`H5857H` — 'Ai', cluster T10
`H6089B` — 'vessel', cluster T2
`H6154A` — 'Arabia', cluster T10
`H6245A` — 'to gleam', cluster T3
`H6335A` — 'to leap', cluster T3
`H6547N` — 'Pharaoh', cluster T8
`H6547R` — 'Pharaoh', cluster T8
`H6547S` — 'Pharaoh [Hophra]', cluster T8
`H6583I` — 'Pashhur', cluster T8
`H6583J` — 'Pashhur', cluster T8
`H6583K` — 'Pashhur', cluster T8
`H6667K` — 'Zedekiah', cluster T8
`H6667L` — 'Zedekiah', cluster T8
`H6731B` — 'feather', cluster T14
`H6963B` — 'frivolity', cluster T2
`H6965A` — '[Leb]-kamai', cluster T10
`H6979B` — 'to cool', cluster T3
`H7249H` — 'Rab-saris', cluster T2
`H7397A` — 'Rechabite', cluster T8
`H7967R` — 'Shallum', cluster T8
`H7967U` — 'Shallum', cluster T8
`H8018K` — 'Shelemiah', cluster T8
`H8018L` — 'Shelemiah', cluster T8
`H8018M` — 'Shelemiah', cluster T8
`H8018N` — 'Shelemiah', cluster T8
`H8098X` — 'Shemaiah', cluster T8
`H8098Y` — 'Shemaiah', cluster T8
`H8098Z` — 'Shemaiah', cluster T8
`H8203O` — 'Shephatiah', cluster T8
`H8304M` — 'Seraiah', cluster T8
`H8304N` — 'Seraiah', cluster T8
`H0565B` — 'threat', cluster T2
`H2100I` — 'to flow: waste away', cluster T3
`H5439J` — 'around: neighours', cluster T2
`H5640B` — 'to stopper', cluster T3
`H0657B` — 'soles', cluster T14
`H1004I` — 'Beth-[togarmah]', cluster T10
`H1141R` — 'Benaiah', cluster T8
`H1304B` — 'gem', cluster T12
`H1516N` — '[Hamon-gog] Valley', cluster T10
`H1516O` — 'Valley', cluster T10
`H1586G` — 'Gomer', cluster T8
`H2258A` — 'pledge', cluster T2
`H2258B` — 'pledge', cluster T2
`H2428B` — 'Helech', cluster T10
`H2970H` — 'Jaazaniah', cluster T8
`H2970I` — 'Jaazaniah', cluster T8
`H3068H` — 'The Lord', cluster T10
`H3520A` — 'glorious', cluster M71
`H3833B` — 'lioness', cluster T2
`H4880A` — 'oar', cluster T2
`H4880B` — 'oar', cluster T2
`H4894A` — 'spreading-place', cluster T2
`H4894B` — 'spreading-place', cluster T2
`H4902I` — 'Meshech', cluster T10
`H5158M` — 'Brook', cluster T10
`H5414J` — 'to give: turn', cluster T3
`H5674G` — '[Valley of] the Travelers', cluster T10
`H5809I` — 'Azzur', cluster T8
`H6213B` — 'to press', cluster T3
`H6288A` — 'bough', cluster T2
`H6410J` — 'Pelatiah', cluster T8
`H6524C` — 'to fly', cluster T3
`H6595B` — 'morsel', cluster T2
`H7070I` — 'branch: measuring rod', cluster T12
`H7070L` — 'branch: calamus', cluster T13
`H7106B` — 'to corner', cluster T3
`H7218B` — 'prince', cluster T2
`H7751B` — 'to row', cluster T3
`H8033H` — '[Jerusalem] Is There', cluster T10
`H8077B` — 'desolation', cluster T2
`H8227G` — 'Shaphan', cluster T8
`H8422I` — '[Meshech]-Tubal', cluster T10
`H8559J` — 'Tamar', cluster T10
`H8602B` — 'whitewash', cluster T2
`H0558J` — 'Amaziah', cluster T8
`H1462B` — 'locust', cluster T13
`H3641B` — 'Calneh', cluster T10
`H5158K` — 'Brook', cluster T10
`H6160H` — '[Brook of] the Arabah', cluster T10
`H6793A` — 'hook', cluster T12
`H7161B` — 'Karnaim', cluster T10
`H7447B` — 'fragment', cluster T2
`H1462A` — 'locust', cluster T13
`H5526D` — 'protector', cluster T2
`H6327B` — 'scatterer', cluster T3
`H6335B` — 'to scatter', cluster T3
`H4294I` — 'tribe: arrow', cluster T12
`H4365A` — 'net', cluster T2
`H5115B` — 'to dwell', cluster T3
`H6075A` — 'to swell', cluster T3
`H7692H` — 'Shigionoth', cluster T2
`H0568O` — 'Amariah', cluster T8
`H1436H` — 'Gedaliah', cluster T8
`H2396K` — 'Hezekiah', cluster T8
`H3569H` — 'Cushi', cluster T8
`H4118A` — 'quick', cluster T3
`H6658B` — 'to waste', cluster T3
`H6846H` — 'Zephaniah', cluster T8
`H7197B` — 'to assemble', cluster T3
`H2292A` — 'Haggai', cluster T8
`H3091J` — 'Joshua', cluster T8
`H7597B` — 'Shealtiel', cluster T8
`H0682B` — 'Azal', cluster T10
`H1144M` — '[Gate of] Benjamin', cluster T10
`H1296L` — 'Berechiah', cluster T8
`H2256C` — 'union', cluster M44
`H2469G` — 'Heldai', cluster T8
`H2900J` — 'Tobijah', cluster T8
`H2977H` — 'Josiah', cluster T8
`H6327C` — 'to flow', cluster T3
`H6846I` — 'Zephaniah', cluster T8
`H7087B` — 'thickness', cluster T2
`H7417G` — 'Rimmon', cluster T10
`H8272H` — 'Sharezer', cluster T8
`H6999B` — 'incense', cluster T3
`H0044H` — 'Abiezer', cluster T2
`H0271H` — 'Ahaz', cluster T2
`H0281K` — 'Ahijah', cluster T2
`H0285H` — 'Ahitub', cluster T2
`H0285I` — 'Ahitub', cluster T2
`H0461J` — 'Eliezer', cluster T2
`H0476J` — 'Elishama', cluster T2
`H0501G` — 'Eleasah', cluster T2
`H0501H` — 'Eleasah', cluster T2
`H0568G` — 'Amariah', cluster T2
`H0568H` — 'Amariah', cluster T2
`H0761G` — 'Aramean', cluster T11
`H0844H` — 'Asriel', cluster T2
`H1446G` — 'Gedor', cluster T2
`H1495G` — 'Gazez', cluster T2
`H1495H` — 'Gazez', cluster T2
`H1540G` — 'Heglam', cluster T3
`H1617J` — 'Gera', cluster T2
`H2066G` — 'Zabad', cluster T2
`H2148D` — 'Zechariah', cluster T2
`H2174H` — 'Zimri', cluster T2
`H2268G` — 'Heber', cluster T2
`H2268I` — 'Heber', cluster T2
`H2503H` — 'Helez', cluster T2
`H2660G` — 'Hepher', cluster T2
`H2771B` — 'Haran', cluster T2
`H3058I` — 'Jehu', cluster T2
`H3103J` — 'Jobab', cluster T2
`H3110J` — 'Johanan', cluster T2
`H3189G` — 'Jahath', cluster T2
`H3382H` — 'Jered', cluster T2
`H3469I` — 'Ishi', cluster T2
`H3620G` — 'Chelub', cluster T2
`H3866G` — 'Ludite', cluster T2
`H4080G` — 'Midian', cluster T2
`H4162G` — 'Moza', cluster T2
`H4162H` — 'Moza', cluster T2
`H4244H` — 'Mahlah', cluster T2
`H4318H` — 'Micah', cluster T2
`H4445A` — 'Malcam', cluster T2
`H4601L` — 'Maacah', cluster T2
`H4714H` — 'Egypt', cluster T2
`H5176K` — '[Ir]-nahash', cluster T2
`H5283J` — 'Naaman', cluster T2
`H5369H` — 'Ner', cluster T2
`H5416J` — 'Nathan', cluster T2
`H5417I` — 'Nethanel', cluster T2
`H5417J` — 'Nethanel', cluster T2
`H5744H` — 'Obed', cluster T2
`H5798H` — 'Uzza', cluster T2
`H5813G` — 'Uzzi', cluster T2
`H5816H` — 'Uzziel', cluster T2
`H5820H` — 'Azmaveth', cluster T2
`H5838J` — 'Azariah', cluster T2
`H5838K` — 'Azariah', cluster T2
`H5891H` — 'Ephah', cluster T2
`H5892H` — 'Ir-[nahash]', cluster T2
`H5915H` — 'Achsah', cluster T2
`H5988J` — 'Ammiel', cluster T2
`H6022I` — 'Amasai', cluster T2
`H6410H` — 'Pelatiah', cluster T2
`H6454G` — 'Paseah', cluster T2
`H6659I` — 'Zadok', cluster T2
`H6721G` — 'Sidon', cluster T2
`H6976G` — 'Koz', cluster T2
`H7397B` — 'Recah', cluster T2
`H7410G` — 'Ram', cluster T2
`H7509H` — 'Rephaiah', cluster T2
`H7509K` — 'Rephaiah', cluster T2
`H7552I` — 'Rekem', cluster T2
`H7645G` — 'Shebaniah', cluster T2
`H7727H` — 'Shobab', cluster T2
`H7763H` — 'Shomer', cluster T2
`H7967I` — 'Shallum', cluster T2
`H7967L` — 'Shallum', cluster T2
`H8060H` — 'Shammai', cluster T2
`H8087G` — 'Shema', cluster T2
`H8092J` — 'Shimea', cluster T2
`H8098H` — 'Shemaiah', cluster T2
`G0007G` — 'Abijah', cluster T8
`H1142G` — 'Bene-jaakan', cluster T2
`H1410I` — '[Dibon]-gad', cluster T2
`H1769I` — 'Dibon[-gad]', cluster T2
`H3841G` — 'Libnah', cluster T2
`H4149B` — 'Moseroth', cluster T2
`H5523H` — 'Succoth', cluster T2
`H8646H` — 'Terah', cluster T2
`H5279G` — 'Naamah', cluster T2
`H1799A` — 'record', cluster T2
`H2148Q` — 'Zechariah', cluster T2
`H3136B` — 'Jozadak', cluster T2
`H4076H` — 'Media', cluster T2
`H6551H` — 'Parosh', cluster T2
`H7935J` — 'Shecaniah', cluster T2
`H8421H` — 'to return: rescue', cluster T3
`H1268A` — 'Berothah', cluster T2
`H5930B` — 'ascent', cluster T3
`H2605O` — 'Hanan', cluster T2
`H3129L` — 'Jonathan', cluster T2
`H4641Z` — 'Maaseiah', cluster T2
`H7967S` — 'Shallum', cluster T2
`H5596B` — 'to scar', cluster T3
`H7771B` — 'cry', cluster T2
`H5198A` — 'drop', cluster T2
`H3266K` — 'Jeush', cluster T2
`H6262I` — 'Attai', cluster T2
`H8019G` — 'Shelomith', cluster T2
`H5299B` — 'height', cluster T2
`H6085H` — '[Mount] Ephron', cluster T2
`H1247L` — 'son: aged', cluster T2
`H0549G` — 'Amana', cluster T2
`H6999I` — 'to offer: to perfume', cluster T3
`G5085G` — '(Sea of) Tiberias', cluster T2
`H8556A` — 'Timnath-heres', cluster T2
`G4504H` — 'Rufus', cluster T2
`H7755G` — 'Socoh', cluster T2
`H1586H` — 'Gomer', cluster T2
`H8607H` — 'Tiphsah', cluster T2
`H3129M` — 'Jonathan', cluster T2
`H4448B` — 'to rub', cluster T3

(none)
