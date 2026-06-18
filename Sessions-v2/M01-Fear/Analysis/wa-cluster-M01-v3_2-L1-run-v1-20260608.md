# M01 — V3_2 L1 run report

> **WRITE-then-report · wa-cluster-M01-v3_2-L1-run-v1-20260608.md · CC.** V3_2 L1 (verse establishment) executed on the live DB (`scripts/v3_2_l1.py`). Cluster status → **In Progress**. Per discipline 2, L1 assigned only single-sense terms; all multi-sense → **residue for L2**.

## Result

- Terms: **83** — single-sense **72**, multi-sense **11**
- Relevant verses touched: **945**
  - **assigned a STEP meaning (single-sense): 482**
  - **residue → L2 (multi-sense): 463** (48% of touched)
- Set-aside verses (left as-is): 81
- Pole distribution (verses): inner 897, physical 48
- Terms flagged `pole_is_metaphor` (heat/tremble/melt): 10 · homonym-filtered terms: 2

## What L1 wrote (per relevant verse_context row)

- single-sense → `step_meaning_applied` (terse STEP sense) + `sense_id` + `sense_multiplicity='single'` + `residue_flag=0`
- multi-sense → `sense_multiplicity='multi'` + `residue_flag=1` (no meaning assigned — deferred to L2)
- all → `pole`, `pole_is_metaphor`, `keywords` (STEP-capture JSON), `step_envelope_note`
- `analysis_note` (existing AI/L3 layer) **preserved, untouched**

## a · Keyword analysis — STEP-capture keywords across assigned verses

Distinct keywords on assigned verses: **113**. Top 40 by verse-frequency:

| keyword | verses | keyword | verses | keyword | verses | keyword | verses |
|---|---|---|---|---|---|---|---|
| `fear` | 321 | `afraid` | 185 | `dread` | 174 | `terror` | 169 |
| `awe` | 158 | `alarm` | 102 | `anxiou` | 101 | `object` | 101 |
| `apprehensive` | 83 | `but` | 83 | `deep` | 83 | `faith` | 83 |
| `reverent` | 64 | `reverence` | 60 | `astonish` | 51 | `terrify` | 46 |
| `affright` | 45 | `amaze` | 44 | `pet` | 44 | `concern` | 43 |
| `deference` | 43 | `metonymy` | 43 | `awesome` | 43 | `piety` | 43 |
| `respect` | 43 | `rever` | 43 | `trembl` | 31 | `dismay` | 17 |
| `terrible` | 17 | `mean` | 16 | `frighten` | 16 | `anxiety` | 15 |
| `spell` | 14 | `quak` | 14 | `care` | 13 | `terrifi` | 13 |
| `deed` | 11 | `inspir` | 11 | `rah` | 11 | `spectacle` | 11 |

## b · Assigned verses (single-sense) — reference · text · STEP-applied meaning

482 verses across 68 single-sense terms. The **STEP-applied meaning** is the per-term head (the same for each of a term's verses at L1; the per-verse contextual reading is L2 work).

### a.qah (pressure) → **pressure**
*pole `inner` · keywords ['oppression', 'pressure'] · 1 verses*

| ref | verse text |
|---|---|
| Psa 55:3 | because of the noise of the enemy , because of the oppression of the wicked . For they drop trouble upon me, and in anger they bear a grudge against me . |

### a.yom (terrible) → **terrible**
*pole `inner` · keywords ['dread', 'terrible'] · 3 verses*

| ref | verse text |
|---|---|
| Song 6:4 | You are beautiful as Tirzah , my love , lovely as Jerusalem , awesome as an army with banners . |
| Song 6:10 | “ Who is this who looks down like the dawn , beautiful as the moon , bright as the sun , awesome as an army with banners ?” |
| Hab 1:7 | They are dreaded and fearsome ; their justice and dignity go forth from themselves. |

### ademoneo (be distressed) → **be distressed / to be troubled, distressed**
*pole `inner` · keywords ['anguish', 'deject', 'depress', 'distress', 'full', 'phil', 'sorrow', 'troubl'] · 3 verses*

| ref | verse text |
|---|---|
| Mat 26:37 | And taking with him Peter and the two sons of Zebedee , he began to be sorrowful and troubled . |
| Mar 14:33 | And he took with him Peter and James and John , and began to be greatly distressed and troubled . |
| Phili 2:26 | for he has been longing for you all and has been distressed because you heard that he was ill . |

### bal.la.hah (terror) → **terror**
*pole `inner` · keywords ['calam', 'destruction', 'dread', 'event', 'terror'] · 6 verses*

| ref | verse text |
|---|---|
| Job 18:11 | Terrors frighten him on every side , and chase him at his heels . |
| Job 18:14 | He is torn from the tent in which he trusted and is brought to the king of terrors . |
| Job 24:17 | For deep darkness is morning to all of them ; for they are friends with the terrors of deep darkness . |
| Job 27:20 | Terrors overtake him like a flood ; in the night a whirlwind carries him off. |
| Job 30:15 | Terrors are turned upon me; my honor is pursued as by the wind , and my prosperity has passed away like a cloud . |
| Isa 17:14 | At evening time , behold , terror ! Before morning , they are no more ! This is the portion of those who loot us, and the lot of those who plunder us . |

### be.a.tah (terror) → **terror**
*pole `inner` · keywords ['dismay', 'terror'] · 2 verses*

| ref | verse text |
|---|---|
| Jer 8:15 | We looked for peace , but no good came; for a time of healing , but behold , terror . |
| Jer 14:19 | Have you utterly rejected Judah ? Does your soul loathe Zion ? Why have you struck us down so that there is no healing for us? We looked for peace , but no good |

### be.ha.lah (dismay) → **dismay**
*pole `inner` · keywords ['alarm', 'dismay', 'ruin', 'sudden', 'terror'] · 3 verses*

| ref | verse text |
|---|---|
| Lev 26:16 | then I will do this to you: I will visit you with panic , with wasting disease and fever that consume the eyes and make the heart ache . And you shall sow your  |
| Isa 65:23 | They shall not labor in vain or bear children for calamity , for they shall be the offspring of the blessed of the Lord , and their descendants with them . |
| Jer 15:8 | I have made their widows more in number than the sand of the seas ; I have brought against the mothers of young men a destroyer at noonday ; I have made anguish |

### be.hal (to dismay) → **to dismay**
*pole `inner` · keywords ['alarm', 'dismay', 'frighten', 'hasten', 'hurry'] · 10 verses*

| ref | verse text |
|---|---|
| Dan 2:25 | Then Arioch brought in Daniel before the king in haste and said thus to him: “I have found among the exiles from Judah a man who will make known to the king the |
| Dan 3:24 | Then King Nebuchadnezzar was astonished and rose up in haste . He declared to his counselors , “Did we not cast three men bound into the fire ?” They answered a |
| Dan 4:5 | I saw a dream that made me afraid . As I lay in bed the fancies and the visions of my head alarmed me . |
| Dan 4:19 | Then Daniel , whose name was Belteshazzar , was dismayed for a while , and his thoughts alarmed him. The king answered and said , “ Belteshazzar , let not the d |
| Dan 5:6 | Then the king’s color changed , and his thoughts alarmed him; his limbs gave way , and his knees knocked together . |
| Dan 5:9 | Then King Belshazzar was greatly alarmed , and his color changed , and his lords were perplexed . |
| Dan 5:10 | The queen , because of the words of the king and his lords , came into the banqueting hall , and the queen declared , “O king , live forever ! Let not your thou |
| Dan 6:19 | Then , at break of day , the king arose and went in haste to the den of lions . |
| Dan 7:15 | “As for me , Daniel , my spirit within me was anxious , and the visions of my head alarmed me . |
| Dan 7:28 | “ Here is the end of the matter . As for me , Daniel , my thoughts greatly alarmed me, and my color changed , but I kept the matter in my heart .” |

### cha.ra.dah (trembling) → **trembling**
*pole `inner` · keywords ['anxiety', 'anxiou', 'care', 'fear', 'quak', 'trembl'] · 7 verses*

| ref | verse text |
|---|---|
| Gen 27:33 | Then Isaac trembled very violently and said , “ Who was it then that hunted game and brought it to me, and I ate it all before you came , and I have blessed him |
| 1Sa 14:15 | And there was a panic in the camp , in the field , and among all the people . The garrison and even the raiders trembled , the earth quaked , and it became a ve |
| Pro 29:25 | The fear of man lays a snare , but whoever trusts in the Lord is safe . |
| Isa 21:4 | My heart staggers ; horror has appalled me; the twilight I longed for has been turned for me into trembling . |
| Jer 30:5 | “ Thus says the Lord : We have heard a cry of panic , of terror , and no peace . |
| Eze 26:16 | Then all the princes of the sea will step down from their thrones and remove their robes and strip off their embroidered garments . They will clothe themselves  |
| Dan 10:7 | And I , Daniel , alone saw the vision , for the men who were with me did not see the vision , but a great trembling fell upon them, and they fled to hide themse |

### cha.red (trembling) → **trembling**
*pole `inner` · keywords ['afraid', 'fear', 'trembl'] · 6 verses*

| ref | verse text |
|---|---|
| Judg 7:3 | Now therefore proclaim in the ears of the people , saying , ‘ Whoever is fearful and trembling , let him return home and hurry away from Mount Gilead .’” Then 2 |
| 1Sa 4:13 | When he arrived , Eli was sitting on his seat by the road watching , for his heart trembled for the ark of God . And when the man came into the city and told th |
| Ezr 9:4 | Then all who trembled at the words of the God of Israel , because of the faithlessness of the returned exiles , gathered around me while I sat appalled until th |
| Ezr 10:3 | Therefore let us make a covenant with our God to put away all these wives and their children , according to the counsel of my lord and of those who tremble at t |
| Isa 66:2 | All these things my hand has made , and so all these things came to be, declares the Lord . But this is the one to whom I will look : he who is humble and contr |
| Isa 66:5 | Hear the word of the Lord , you who tremble at his word : “Your brothers who hate you and cast you out for my name’s sake have said , ‘Let the Lord be glorified |

### cha.tat (terror) → **terror**
*pole `inner` · keywords ['terror'] · 1 verses*

| ref | verse text |
|---|---|
| Job 6:21 | For you have now become nothing ; you see my calamity and are afraid . |

### chag.ga (terror) → **terror**
*pole `inner` · keywords ['reel', 'terror'] · 1 verses*

| ref | verse text |
|---|---|
| Isa 19:17 | And the land of Judah will become a terror to the Egyptians . Everyone to whom it is mentioned will fear because of the purpose that the Lord of hosts has purpo |

### chat (terror) → **terror**
*pole `inner` · keywords ['fear', 'terror'] · 2 verses*

| ref | verse text |
|---|---|
| Gen 9:2 | The fear of you and the dread of you shall be upon every beast of the earth and upon every bird of the heavens , upon everything that creeps on the ground and a |
| Job 41:33 | On earth there is not his like , a creature without fear . |

### chat.chat (terror) → **terror**
*pole `inner` · keywords ['terror'] · 1 verses*

| ref | verse text |
|---|---|
| Ecc 12:5 | they are afraid also of what is high , and terrors are in the way ; the almond tree blossoms , the grasshopper drags itself along, and desire fails , because ma |

### chit.tah (terror) → **terror**
*pole `inner` · keywords ['fear', 'terror'] · 1 verses*

| ref | verse text |
|---|---|
| Gen 35:5 | And as they journeyed , a terror from God fell upon the cities that were around them, so that they did not pursue the sons of Jacob . |

### chit.tit (terror) → **terror**
*pole `inner` · keywords ['terror'] · 8 verses*

| ref | verse text |
|---|---|
| Eze 26:17 | And they will raise a lamentation over you and say to you, “‘ How you have perished , you who were inhabited from the seas , O city renowned , who was mighty on |
| Eze 32:23 | whose graves are set in the uttermost parts of the pit ; and her company is all around her grave , all of them slain , fallen by the sword , who spread terror i |
| Eze 32:24 | “ Elam is there , and all her multitude around her grave ; all of them slain , fallen by the sword , who went down uncircumcised into the world below , who spre |
| Eze 32:25 | They have made her a bed among the slain with all her multitude , her graves all around it, all of them uncircumcised , slain by the sword ; for terror of them  |
| Eze 32:26 | “ Meshech-Tubal is there , and all her multitude , her graves all around it, all of them uncircumcised , slain by the sword ; for they spread their terror in th |
| Eze 32:27 | And they do not lie with the mighty , the fallen from among the uncircumcised , who went down to Sheol with their weapons of war , whose swords were laid under  |
| Eze 32:30 | “The princes of the north are there , all of them, and all the Sidonians , who have gone down in shame with the slain , for all the terror that they caused by t |
| Eze 32:32 | For I spread terror in the land of the living ; and he shall be laid to rest among the uncircumcised , with those who are slain by the sword , Pharaoh and all h |

### de.a.gah (anxiety) → **anxiety**
*pole `inner` · keywords ['anxiety', 'anxiou', 'care'] · 6 verses*

| ref | verse text |
|---|---|
| Jos 22:24 | No , but we did it from fear that in time to come your children might say to our children , ‘ What have you to do with the Lord , the God of Israel ? |
| Pro 12:25 | Anxiety in a man’s heart weighs him down , but a good word makes him glad . |
| Jer 49:23 | Concerning Damascus : “ Hamath and Arpad are confounded , for they have heard bad news ; they melt in fear , they are troubled like the sea that cannot be quiet |
| Eze 4:16 | Moreover, he said to me, “ Son of man , behold , I will break the supply of bread in Jerusalem . They shall eat bread by weight and with anxiety , and they shal |
| Eze 12:18 | “ Son of man , eat your bread with quaking , and drink water with trembling and with anxiety . |
| Eze 12:19 | And say to the people of the land , Thus says the Lord God concerning the inhabitants of Jerusalem in the land of Israel : They shall eat their bread with anxie |

### de.a.vah (dismay) → **dismay**
*pole `inner` · keywords ['dismay', 'energy', 'failure', 'faint', 'mental'] · 1 verses*

| ref | verse text |
|---|---|
| Job 41:22 | In his neck abides strength , and terror dances before him. |

### de.chal (to fear) → **to fear**
*pole `inner` · keywords ['afraid', 'fear', 'terrible'] · 6 verses*

| ref | verse text |
|---|---|
| Dan 2:31 | “ You saw , O king , and behold , a great image . This image , mighty and of exceeding brightness , stood before you, and its appearance was frightening . |
| Dan 4:5 | I saw a dream that made me afraid . As I lay in bed the fancies and the visions of my head alarmed me . |
| Dan 5:19 | And because of the greatness that he gave him, all peoples , nations , and languages trembled and feared before him. Whom he would , he killed , and whom he wou |
| Dan 6:26 | I make a decree , that in all my royal dominion people are to tremble and fear before the God of Daniel , for he is the living God , enduring forever ; his king |
| Dan 7:7 | After this I saw in the night visions , and behold , a fourth beast , terrifying and dreadful and exceedingly strong . It had great iron teeth ; it devoured and |
| Dan 7:19 | “ Then I desired to know the truth about the fourth beast , which was different from all the rest, exceedingly terrifying , with its teeth of iron and claws of  |

### deilia (timidity) → **timidity / timidity, cowardice**
*pole `inner` · keywords ['cowardice', 'tim', 'timid'] · 1 verses*

| ref | verse text |
|---|---|
| 2Ti 1:7 | for God gave us a spirit not of fear but of power and love and self-control . |

### deiliaō (be timid) → **be timid / to be afraid, cowardly, timid**
*pole `inner` · keywords ['afraid', 'coward', 'fear', 'timid'] · 1 verses*

| ref | verse text |
|---|---|
| Joh 14:27 | Peace I leave with you ; my peace I give to you . Not as the world gives do I give to you . Let not your hearts be troubled , neither let them be afraid . |

### deilos (timid) → **timid / afraid, cowardly, timid**
*pole `inner` · keywords ['afraid', 'coward', 'fear', 'rev', 'timid'] · 3 verses*

| ref | verse text |
|---|---|
| Mat 8:26 | And he said to them , “ Why are you afraid , O you of little faith ?” Then he rose and rebuked the winds and the sea , and there was a great calm . |
| Mar 4:40 | He said to them , “ Why are you so afraid ? Have you still no faith ?” |
| Rev 21:8 | But as for the cowardly , the faithless , the detestable , as for murderers , the sexually immoral , sorcerers , idolaters , and all liars , their portion will  |

### deos (fear) → **fear / fear, reverence, awe**
*pole `inner` · keywords ['awe', 'fear', 'list', 'manuscript', 'place', 'reverence'] · 1 verses*

| ref | verse text |
|---|---|
| Heb 12:28 | Therefore let us be grateful for receiving a kingdom that cannot be shaken , and thus let us offer to God acceptable worship, with reverence and awe , |

### e.mah (terror) → **terror**
*pole `inner` · keywords ['dread', 'terror'] · 16 verses*

| ref | verse text |
|---|---|
| Gen 15:12 | As the sun was going down , a deep sleep fell on Abram . And behold , dreadful and great darkness fell upon him . |
| Exo 15:16 | Terror and dread fall upon them; because of the greatness of your arm , they are still as a stone , till your people , O Lord , pass by , till the people pass b |
| Exo 23:27 | I will send my terror before you and will throw into confusion all the people against whom you shall come , and I will make all your enemies turn their backs to |
| Deu 32:25 | Outdoors the sword shall bereave , and indoors terror , for young man and woman alike, the nursing child with the man of gray hairs . |
| Jos 2:9 | and said to the men , “I know that the Lord has given you the land , and that the fear of you has fallen upon us, and that all the inhabitants of the land melt  |
| Ezr 3:3 | They set the altar in its place , for fear was on them because of the peoples of the lands , and they offered burnt offerings on it to the Lord , burnt offering |
| Job 9:34 | Let him take his rod away from me, and let not dread of him terrify me . |
| Job 13:21 | withdraw your hand far from me, and let not dread of you terrify me . |
| Job 20:25 | It is drawn forth and comes out of his body ; the glittering point comes out of his gallbladder ; terrors come upon him. |
| Job 33:7 | Behold , no fear of me need terrify you; my pressure will not be heavy upon you. |
| Job 39:20 | Do you make him leap like the locust ? His majestic snorting is terrifying . |
| Job 41:14 | Who can open the doors of his face ? Around his teeth is terror . |
| Psa 55:4 | My heart is in anguish within me; the terrors of death have fallen upon me . |
| Psa 88:15 | Afflicted and close to death from my youth up, I suffer your terrors ; I am helpless . |
| Pro 20:2 | The terror of a king is like the growling of a lion ; whoever provokes him to anger forfeits his life . |
| Isa 33:18 | Your heart will muse on the terror : “ Where is he who counted , where is he who weighed the tribute ? Where is he who counted the towers ?” |

### ekfobos (terrified) → **terrified / frightened, terrified**
*pole `inner` · keywords ['frighten', 'horrifi', 'terrifi'] · 2 verses*

| ref | verse text |
|---|---|
| Mar 9:6 | For he did not know what to say , for they were terrified . |
| Heb 12:21 | Indeed , so terrifying was the sight that Moses said , “ I tremble with fear .” |

### ekthambeo (be awe-struck) → **be awe-struck / (<i>passive</i>) to be overwhelmed with wonder, distressed, alarmed**
*pole `inner` · keywords ['alarm', 'amaz', 'astonish', 'awe', 'distress', 'overwhelm', 'pas', 'struck'] · 4 verses*

| ref | verse text |
|---|---|
| Mar 9:15 | And immediately all the crowd , when they saw him , were greatly amazed and ran up to him and greeted him . |
| Mar 14:33 | And he took with him Peter and James and John , and began to be greatly distressed and troubled . |
| Mar 16:5 | And entering the tomb , they saw a young man sitting on the right side , dressed in a white robe , and they were alarmed . |
| Mar 16:6 | And he said to them , “Do not be alarmed . You seek Jesus of Nazareth , who was crucified . He has risen ; he is not here . See the place where they laid him . |

### ekthambos (astonished) → **astonished**
*pole `inner` · keywords ['astonish'] · 1 verses*

| ref | verse text |
|---|---|
| Act 3:11 | While he clung to Peter and John , all the people , utterly astounded , ran together to them in the portico called Solomon’s . |

### emfobos (afraid) → **afraid / afraid, terrified**
*pole `inner` · keywords ['afraid', 'rev', 'terrible', 'terrifi'] · 5 verses*

| ref | verse text |
|---|---|
| Luk 24:5 | And as they were frightened and bowed their faces to the ground , the men said to them , “ Why do you seek the living among the dead ? |
| Luk 24:37 | But they were startled and frightened and thought they saw a spirit . |
| Act 10:4 | And he stared at him in terror and said , “ What is it , Lord ?” And he said to him , “ Your prayers and your alms have ascended as a memorial before God . |
| Act 24:25 | And as he reasoned about righteousness and self-control and the coming judgment , Felix was alarmed and said , “ Go away for the present . When I get an opportu |
| Rev 11:13 | And at that hour there was a great earthquake , and a tenth of the city fell . Seven thousand people were killed in the earthquake , and the rest were terrified |

### entromos (trembling) → **trembling**
*pole `inner` · keywords ['terrifi', 'trembl'] · 3 verses*

| ref | verse text |
|---|---|
| Act 7:32 | ‘ I am the God of your fathers , the God of Abraham and of Isaac and of Jacob .’ And Moses trembled and did not dare to look . |
| Act 16:29 | And the jailer called for lights and rushed in , and trembling with fear he fell down before Paul and Silas . |
| Heb 12:21 | Indeed , so terrifying was the sight that Moses said , “ I tremble with fear .” |

### foberos (fearful) → **fearful / fearful, dreadful, terrible**
*pole `inner` · keywords ['dread', 'fear', 'terrible'] · 3 verses*

| ref | verse text |
|---|---|
| Heb 10:27 | but a fearful expectation of judgment , and a fury of fire that will consume the adversaries . |
| Heb 10:31 | It is a fearful thing to fall into the hands of the living God . |
| Heb 12:21 | Indeed , so terrifying was the sight that Moses said , “ I tremble with fear .” |

### fobeō (to fear) → **to fear / to fear, be afraid, alarmed, in some contexts improper and an impediment to faith and love; to reverence, respect, worship, in other contexts a proper**
*pole `inner` · keywords ['afraid', 'alarm', 'anxiou', 'apprehensive', 'awe', 'but', 'deep', 'dread'] · 83 verses*

| ref | verse text |
|---|---|
| Mat 1:20 | But as he considered these things , behold , an angel of the Lord appeared to him in a dream , saying , “ Joseph , son of David , do not fear to take Mary as yo |
| Mat 2:22 | But when he heard that Archelaus was reigning over Judea in place of his father Herod , he was afraid to go there , and being warned in a dream he withdrew to t |
| Mat 9:8 | When the crowds saw it, they were afraid , and they glorified God , who had given such authority to men . |
| Mat 10:26 | “ So have no fear of them , for nothing is covered that will not be revealed , or hidden that will not be known . |
| Mat 10:28 | And do not fear those who kill the body but cannot kill the soul . Rather fear him who can destroy both soul and body in hell . |
| Mat 10:31 | Fear not , therefore ; you are of more value than many sparrows . |
| Mat 14:5 | And though he wanted to put him to death , he feared the people , because they held him to be a prophet . |
| Mat 14:27 | But immediately Jesus spoke to them , saying , “Take heart ; it is I . Do not be afraid .” |
| Mat 14:30 | But when he saw the wind , he was afraid , and beginning to sink he cried out, “ Lord , save me .” |
| Mat 17:6 | When the disciples heard this, they fell on their faces and were terrified . |
| Mat 17:7 | But Jesus came and touched them , saying , “ Rise , and have no fear .” |
| Mat 21:26 | But if we say , ‘ From man ,’ we are afraid of the crowd , for they all hold that John was a prophet .” |
| Mat 21:46 | And although they were seeking to arrest him , they feared the crowds , because they held him to be a prophet . |
| Mat 25:25 | so I was afraid , and I went and hid your talent in the ground . Here , you have what is yours .’ |
| Mat 27:54 | When the centurion and those who were with him , keeping watch over Jesus , saw the earthquake and what took place , they were filled with awe and said , “ Trul |
| Mat 28:5 | But the angel said to the women , “Do not be afraid , for I know that you seek Jesus who was crucified . |
| Mat 28:10 | Then Jesus said to them , “Do not be afraid ; go and tell my brothers to go to Galilee , and there they will see me .” |
| Mar 4:41 | And they were filled with great fear and said to one another , “ Who then is this , that even the wind and the sea obey him ?” |
| Mar 5:15 | And they came to Jesus and saw the demon -possessed man, the one who had had the legion , sitting there, clothed and in his right mind , and they were afraid . |
| Mar 5:33 | But the woman , knowing what had happened to her , came in fear and trembling and fell down before him and told him the whole truth . |
| Mar 5:36 | But overhearing what they said , Jesus said to the ruler of the synagogue , “Do not fear , only believe .” |
| Mar 6:20 | for Herod feared John , knowing that he was a righteous and holy man , and he kept him safe . When he heard him , he was greatly perplexed , and yet he heard hi |
| Mar 6:50 | for they all saw him and were terrified . But immediately he spoke to them and said , “Take heart ; it is I . Do not be afraid .” |
| Mar 9:32 | But they did not understand the saying , and were afraid to ask him . |
| Mar 10:32 | And they were on the road , going up to Jerusalem , and Jesus was walking ahead of them . And they were amazed , and those who followed were afraid . And taking |
| Mar 11:18 | And the chief priests and the scribes heard it and were seeking a way to destroy him , for they feared him , because all the crowd was astonished at his teachin |
| Mar 11:32 | But shall we say , ‘ From man ’?”— they were afraid of the people , for they all held that John really was a prophet . |
| Mar 12:12 | And they were seeking to arrest him but feared the people , for they perceived that he had told the parable against them . So they left him and went away . |
| Mar 16:8 | And they went out and fled from the tomb , for trembling and astonishment had seized them, and they said nothing to anyone , for they were afraid . |
| Luk 1:13 | But the angel said to him , “Do not be afraid , Zechariah , for your prayer has been heard , and your wife Elizabeth will bear you a son , and you shall call hi |
| Luk 1:30 | And the angel said to her , “Do not be afraid , Mary , for you have found favor with God . |
| Luk 1:50 | And his mercy is for those who fear him from generation to generation . |
| Luk 2:9 | And an angel of the Lord appeared to them , and the glory of the Lord shone around them , and they were filled with great fear . |
| Luk 2:10 | And the angel said to them , “ Fear not , for behold , I bring you good news of great joy that will be for all the people . |
| Luk 5:10 | and so also were James and John , sons of Zebedee , who were partners with Simon . And Jesus said to Simon , “Do not be afraid ; from now on you will be catchin |
| Luk 8:25 | He said to them , “ Where is your faith ?” And they were afraid , and they marveled , saying to one another , “Who then is this , that he commands even winds an |
| Luk 8:35 | Then people went out to see what had happened , and they came to Jesus and found the man from whom the demons had gone , sitting at the feet of Jesus , clothed  |
| Luk 8:50 | But Jesus on hearing this answered him , “Do not fear ; only believe , and she will be well .” |
| Luk 9:34 | As he was saying these things , a cloud came and overshadowed them , and they were afraid as they entered the cloud . |
| Luk 9:45 | But they did not understand this saying , and it was concealed from them , so that they might not perceive it . And they were afraid to ask him about this sayin |
| Luk 12:4 | “I tell you , my friends , do not fear those who kill the body , and after that have nothing more that they can do . |
| Luk 12:5 | But I will warn you whom to fear : fear him who, after he has killed , has authority to cast into hell . Yes , I tell you , fear him ! |
| Luk 12:7 | Why , even the hairs of your head are all numbered . Fear not ; you are of more value than many sparrows . |
| Luk 12:32 | “ Fear not , little flock , for it is your Father’s good pleasure to give you the kingdom . |
| Luk 18:2 | He said , “ In a certain city there was a judge who neither feared God nor respected man . |
| Luk 18:4 | For a while he refused , but afterward he said to himself , ‘ Though I neither fear God nor respect man , |
| Luk 19:21 | for I was afraid of you , because you are a severe man . You take what you did not deposit , and reap what you did not sow .’ |
| Luk 20:19 | The scribes and the chief priests sought to lay hands on him at that very hour , for they perceived that he had told this parable against them , but they feared |
| Luk 22:2 | And the chief priests and the scribes were seeking how to put him to death , for they feared the people . |
| Luk 23:40 | But the other rebuked him , saying , “Do you not fear God , since you are under the same sentence of condemnation ? |
| Joh 6:19 | When they had rowed about three or four miles , they saw Jesus walking on the sea and coming near the boat , and they were frightened . |
| Joh 6:20 | But he said to them , “It is I ; do not be afraid .” |
| Joh 9:22 | ( His parents said these things because they feared the Jews , for the Jews had already agreed that if anyone should confess Jesus to be Christ , he was to be p |
| Joh 12:15 | “ Fear not , daughter of Zion ; behold , your king is coming , sitting on a donkey’s colt !” |
| Joh 19:8 | When Pilate heard this statement , he was even more afraid . |
| Act 5:26 | Then the captain with the officers went and brought them , but not by force , for they were afraid of being stoned by the people . |
| Act 9:26 | And when he had come to Jerusalem , he attempted to join the disciples . And they were all afraid of him , for they did not believe that he was a disciple . |
| Act 10:2 | a devout man who feared God with all his household , gave alms generously to the people , and prayed continually to God . |
| Act 10:22 | And they said , “ Cornelius , a centurion , an upright and God - fearing man , who is well spoken of by the whole Jewish nation , was directed by a holy angel t |
| Act 10:35 | but in every nation anyone who fears him and does what is right is acceptable to him . |
| Rom 11:20 | That is true . They were broken off because of their unbelief , but you stand fast through faith . So do not become proud , but fear . |
| Rom 13:3 | For rulers are not a terror to good conduct , but to bad . Would you have no fear of the one who is in authority ? Then do what is good , and you will receive h |
| Rom 13:4 | for he is God’s servant for your good . But if you do wrong , be afraid , for he does not bear the sword in vain . For he is the servant of God , an avenger who |
| 2Cor 11:3 | But I am afraid that as the serpent deceived Eve by his cunning , your thoughts will be led astray from a sincere and pure devotion to Christ . |
| 2Cor 12:20 | For I fear that perhaps when I come I may find you not as I wish , and that you may find me not as you wish — that perhaps there may be quarreling , jealousy ,  |
| Gal 2:12 | For before certain men came from James , he was eating with the Gentiles ; but when they came he drew back and separated himself , fearing the circumcision part |
| Gal 4:11 | I am afraid I may have labored over you in vain . |
| Eph 5:33 | However , let each one of you love his wife as himself , and let the wife see that she respects her husband . |
| Col 3:22 | Bondservants , obey in everything those who are your earthly masters , not by way of eye-service , as people-pleasers , but with sincerity of heart , fearing th |
| Heb 4:1 | Therefore , while the promise of entering his rest still stands , let us fear lest any of you should seem to have failed to reach it. |
| Heb 11:23 | By faith Moses , when he was born , was hidden for three months by his parents , because they saw that the child was beautiful , and they were not afraid of the |
| Heb 11:27 | By faith he left Egypt , not being afraid of the anger of the king , for he endured as seeing him who is invisible . |
| Heb 13:6 | So we can confidently say , “The Lord is my helper ; I will not fear ; what can man do to me ?” |
| 1Pe 2:17 | Honor everyone . Love the brotherhood . Fear God . Honor the emperor . |
| 1Pe 3:6 | as Sarah obeyed Abraham , calling him lord . And you are her children , if you do good and do not fear anything that is frightening . |
| 1Pe 3:14 | But even if you should suffer for righteousness ’ sake, you will be blessed . Have no fear of them , nor be troubled , |
| 1Jo 4:18 | There is no fear in love , but perfect love casts out fear . For fear has to do with punishment , and whoever fears has not been perfected in love . |
| Rev 1:17 | When I saw him , I fell at his feet as though dead . But he laid his right hand on me , saying , “ Fear not , I am the first and the last , |
| Rev 2:10 | Do not fear what you are about to suffer . Behold , the devil is about to throw some of you into prison , that you may be tested , and for ten days you will hav |
| Rev 11:18 | The nations raged , but your wrath came , and the time for the dead to be judged , and for rewarding your servants , the prophets and saints , and those who fea |
| Rev 14:7 | And he said with a loud voice , “ Fear God and give him glory , because the hour of his judgment has come , and worship him who made heaven and earth , the sea  |
| Rev 15:4 | Who will not fear , O Lord , and glorify your name ? For you alone are holy . All nations will come and worship you , for your righteous acts have been revealed |
| Rev 19:5 | And from the throne came a voice saying , “ Praise our God , all you his servants , you who fear him , small and great .” |

### fobos (fear) → **fear / fear, terror; respect, reverence; see also G4989**
*pole `inner` · keywords ['affright', 'amaze', 'astonish', 'awe', 'concern', 'deference', 'fear', 'metonymy'] · 43 verses*

| ref | verse text |
|---|---|
| Mat 14:26 | But when the disciples saw him walking on the sea , they were terrified , and said , “It is a ghost !” and they cried out in fear . |
| Mat 28:4 | And for fear of him the guards trembled and became like dead men. |
| Mat 28:8 | So they departed quickly from the tomb with fear and great joy , and ran to tell his disciples . |
| Mar 4:41 | And they were filled with great fear and said to one another , “ Who then is this , that even the wind and the sea obey him ?” |
| Luk 1:12 | And Zechariah was troubled when he saw him, and fear fell upon him . |
| Luk 1:65 | And fear came on all their neighbors . And all these things were talked about through all the hill country of Judea , |
| Luk 5:26 | And amazement seized them all , and they glorified God and were filled with awe , saying , “We have seen extraordinary things today .” |
| Luk 7:16 | Fear seized them all , and they glorified God , saying , “A great prophet has arisen among us !” and “ God has visited his people !” |
| Luk 8:37 | Then all the people of the surrounding country of the Gerasenes asked him to depart from them , for they were seized with great fear . So he got into the boat a |
| Luk 21:26 | people fainting with fear and with foreboding of what is coming on the world . For the powers of the heavens will be shaken . |
| Joh 7:13 | Yet for fear of the Jews no one spoke openly of him . |
| Joh 19:38 | After these things Joseph of Arimathea , who was a disciple of Jesus , but secretly for fear of the Jews , asked Pilate that he might take away the body of Jesu |
| Joh 20:19 | On the evening of that day , the first day of the week , the doors being locked where the disciples were for fear of the Jews , Jesus came and stood among them  |
| Act 2:43 | And awe came upon every soul , and many wonders and signs were being done through the apostles . |
| Act 5:5 | When Ananias heard these words , he fell down and breathed his last . And great fear came upon all who heard of it. |
| Act 5:11 | And great fear came upon the whole church and upon all who heard of these things . |
| Act 9:31 | So the church throughout all Judea and Galilee and Samaria had peace and was being built up . And walking in the fear of the Lord and in the comfort of the Holy |
| Act 19:17 | And this became known to all the residents of Ephesus , both Jews and Greeks . And fear fell upon them all , and the name of the Lord Jesus was extolled . |
| Rom 3:18 | “There is no fear of God before their eyes .” |
| Rom 8:15 | For you did not receive the spirit of slavery to fall back into fear , but you have received the Spirit of adoption as sons, by whom we cry , “ Abba ! Father !” |
| Rom 13:3 | For rulers are not a terror to good conduct , but to bad . Would you have no fear of the one who is in authority ? Then do what is good , and you will receive h |
| Rom 13:7 | Pay to all what is owed to them: taxes to whom taxes are owed , revenue to whom revenue is owed , respect to whom respect is owed , honor to whom honor is owed  |
| 1Cor 2:3 | And I was with you in weakness and in fear and much trembling , |
| 2Cor 5:11 | Therefore , knowing the fear of the Lord , we persuade others . But what we are is known to God , and I hope it is known also to your conscience . |
| 2Cor 7:1 | Since we have these promises , beloved , let us cleanse ourselves from every defilement of body and spirit , bringing holiness to completion in the fear of God  |
| 2Cor 7:5 | For even when we came into Macedonia , our bodies had no rest , but we were afflicted at every turn— fighting without and fear within . |
| 2Cor 7:11 | For see what earnestness this godly grief has produced in you , but also what eagerness to clear yourselves, what indignation , what fear , what longing , what  |
| 2Cor 7:15 | And his affection for you is even greater , as he remembers the obedience of you all , how you received him with fear and trembling . |
| Eph 5:21 | submitting to one another out of reverence for Christ . |
| Eph 6:5 | Bondservants , obey your earthly masters with fear and trembling , with a sincere heart , as you would Christ , |
| Phili 2:12 | Therefore , my beloved , as you have always obeyed , so now , not only as in my presence but much more in my absence , work out your own salvation with fear and |
| 1Ti 5:20 | As for those who persist in sin , rebuke them in the presence of all , so that the rest may stand in fear . |
| Heb 2:15 | and deliver all those who through fear of death were subject to lifelong slavery . |
| 1Pe 1:17 | And if you call on him as Father who judges impartially according to each one’s deeds , conduct yourselves with fear throughout the time of your exile , |
| 1Pe 2:18 | Servants , be subject to your masters with all respect , not only to the good and gentle but also to the unjust . |
| 1Pe 3:2 | when they see your respectful and pure conduct . |
| 1Pe 3:14 | But even if you should suffer for righteousness ’ sake, you will be blessed . Have no fear of them , nor be troubled , |
| 1Pe 3:15 | but in your hearts honor Christ the Lord as holy , always being prepared to make a defense to anyone who asks you for a reason for the hope that is in you ; yet |
| 1Jo 4:18 | There is no fear in love , but perfect love casts out fear . For fear has to do with punishment , and whoever fears has not been perfected in love . |
| Jude 23 | save others by snatching them out of the fire ; to others show mercy with fear , hating even the garment stained by the flesh . |
| Rev 11:11 | But after the three and a half days a breath of life from God entered them , and they stood up on their feet , and great fear fell on those who saw them . |
| Rev 18:10 | They will stand far off , in fear of her torment , and say , “ Alas ! Alas ! You great city , you mighty city , Babylon ! For in a single hour your judgment has |
| Rev 18:15 | The merchants of these wares, who gained wealth from her , will stand far off , in fear of her torment , weeping and mourning aloud , |

### gur (to dread) → **to dread**
*pole `inner` · keywords ['afraid', 'awe', 'dread', 'fear', 'stand'] · 9 verses*

| ref | verse text |
|---|---|
| Num 22:3 | And Moab was in great dread of the people , because they were many . Moab was overcome with fear of the people of Israel . |
| Deu 1:17 | You shall not be partial in judgment . You shall hear the small and the great alike. You shall not be intimidated by anyone , for the judgment is God’s . And th |
| Deu 18:22 | when a prophet speaks in the name of the Lord , if the word does not come to pass or come true, that is a word that the Lord has not spoken ; the prophet has sp |
| 1Sa 18:15 | And when Saul saw that he had great success , he stood in fearful awe of him. |
| Job 19:29 | be afraid of the sword , for wrath brings the punishment of the sword , that you may know there is a judgment .” |
| Job 41:25 | When he raises himself up, the mighty are afraid ; at the crashing they are beside themselves. |
| Psa 22:23 | You who fear the Lord , praise him! All you offspring of Jacob , glorify him, and stand in awe of him, all you offspring of Israel ! |
| Psa 33:8 | Let all the earth fear the Lord ; let all the inhabitants of the world stand in awe of him! |
| Hos 10:5 | The inhabitants of Samaria tremble for the calf of Beth-aven . Its people mourn for it, and so do its idolatrous priests — those who rejoiced over it and over i |

### ke.ra (be distressed) → **be distressed**
*pole `inner` · keywords ['distress', 'griev'] · 1 verses*

| ref | verse text |
|---|---|
| Dan 7:15 | “As for me , Daniel , my spirit within me was anxious , and the visions of my head alarmed me . |

### ma.a.ra.tsah (terror) → **terror**
*pole `inner` · keywords ['awful', 'crash', 'shock', 'terror'] · 1 verses*

| ref | verse text |
|---|---|
| Isa 10:33 | Behold , the Lord God of hosts will lop the boughs with terrifying power; the great in height will be hewn down , and the lofty will be brought low . |

### ma.gor (terror) → **terror**
*pole `inner` · keywords ['fear', 'terror'] · 8 verses*

| ref | verse text |
|---|---|
| Psa 31:13 | For I hear the whispering of many — terror on every side !— as they scheme together against me, as they plot to take my life . |
| Isa 31:9 | His rock shall pass away in terror , and his officers desert the standard in panic ,” declares the Lord , whose fire is in Zion , and whose furnace is in Jerusa |
| Jer 6:25 | Go not out into the field , nor walk on the road , for the enemy has a sword ; terror is on every side . |
| Jer 20:4 | For thus says the Lord : Behold , I will make you a terror to yourself and to all your friends . They shall fall by the sword of their enemies while you look on |
| Jer 20:10 | For I hear many whispering . Terror is on every side ! “ Denounce him! Let us denounce him!” say all my close friends , watching for my fall . “ Perhaps he will |
| Jer 46:5 | Why have I seen it? They are dismayed and have turned backward . Their warriors are beaten down and have fled in haste ; they look not back — terror on every si |
| Jer 49:29 | Their tents and their flocks shall be taken , their curtains and all their goods ; their camels shall be led away from them, and men shall cry to them: ‘ Terror |
| Lam 2:22 | You summoned as if to a festival day my terrors on every side , and on the day of the anger of the Lord no one escaped or survived ; those whom I held and raise |

### me.go.rah (fear) → **fear**
*pole `inner` · keywords ['fear', 'terror'] · 2 verses*

| ref | verse text |
|---|---|
| Psa 34:4 | I sought the Lord , and he answered me and delivered me from all my fears . |
| Pro 10:24 | What the wicked dreads will come upon him, but the desire of the righteous will be granted . |

### me.gu.rah (fear) → **fear**
*pole `inner` · keywords ['fear', 'granary', 'storehouse', 'terror'] · 1 verses*

| ref | verse text |
|---|---|
| Isa 66:4 | I also will choose harsh treatment for them and bring their fears upon them, because when I called , no one answered , when I spoke , they did not listen ; but  |

### mish.bar (wave) → **wave**
*pole `physical` · keywords ['break', 'breaker', 'wave'] · 4 verses*

| ref | verse text |
|---|---|
| 2Sa 22:5 | “For the waves of death encompassed me, the torrents of destruction assailed me; |
| Psa 42:7 | Deep calls to deep at the roar of your waterfalls ; all your breakers and your waves have gone over me. |
| Psa 88:7 | Your wrath lies heavy upon me, and you overwhelm me with all your waves . Selah |
| Jon 2:3 | For you cast me into the deep , into the heart of the seas , and the flood surrounded me; all your breakers and your waves passed over me. |

### mo.ra (fear) → **fear**
*pole `inner` · keywords ['appoint', 'fear', 'spell', 'terror'] · 11 verses*

| ref | verse text |
|---|---|
| Gen 9:2 | The fear of you and the dread of you shall be upon every beast of the earth and upon every bird of the heavens , upon everything that creeps on the ground and a |
| Deu 4:34 | Or has any god ever attempted to go and take a nation for himself from the midst of another nation , by trials , by signs , by wonders , and by war , by a might |
| Deu 11:25 | No one shall be able to stand against you. The Lord your God will lay the fear of you and the dread of you on all the land that you shall tread , as he promised |
| Deu 26:8 | And the Lord brought us out of Egypt with a mighty hand and an outstretched arm , with great deeds of terror , with signs and wonders . |
| Deu 34:12 | and for all the mighty power and all the great deeds of terror that Moses did in the sight of all Israel . |
| Psa 76:11 | Make your vows to the Lord your God and perform them; let all around him bring gifts to him who is to be feared , |
| Isa 8:12 | “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread . |
| Isa 8:13 | But the Lord of hosts , him you shall honor as holy . Let him be your fear , and let him be your dread . |
| Jer 32:21 | You brought your people Israel out of the land of Egypt with signs and wonders , with a strong hand and outstretched arm , and with great terror . |
| Mal 1:6 | “A son honors his father , and a servant his master . If then I am a father , where is my honor ? And if I am a master , where is my fear ? says the Lord of hos |
| Mal 2:5 | My covenant with him was one of life and peace , and I gave them to him. It was a covenant of fear , and he feared me. He stood in awe of my name . |

### mo.rah (fear) → **fear**
*pole `inner` · keywords ['awe', 'deed', 'fear', 'inspir', 'mean', 'object', 'rah', 'reverence'] · 11 verses*

| ref | verse text |
|---|---|
| Gen 9:2 | The fear of you and the dread of you shall be upon every beast of the earth and upon every bird of the heavens , upon everything that creeps on the ground and a |
| Deu 4:34 | Or has any god ever attempted to go and take a nation for himself from the midst of another nation , by trials , by signs , by wonders , and by war , by a might |
| Deu 11:25 | No one shall be able to stand against you. The Lord your God will lay the fear of you and the dread of you on all the land that you shall tread , as he promised |
| Deu 26:8 | And the Lord brought us out of Egypt with a mighty hand and an outstretched arm , with great deeds of terror , with signs and wonders . |
| Deu 34:12 | and for all the mighty power and all the great deeds of terror that Moses did in the sight of all Israel . |
| Psa 76:11 | Make your vows to the Lord your God and perform them; let all around him bring gifts to him who is to be feared , |
| Isa 8:12 | “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread . |
| Isa 8:13 | But the Lord of hosts , him you shall honor as holy . Let him be your fear , and let him be your dread . |
| Jer 32:21 | You brought your people Israel out of the land of Egypt with signs and wonders , with a strong hand and outstretched arm , and with great terror . |
| Mal 1:6 | “A son honors his father , and a servant his master . If then I am a father , where is my honor ? And if I am a master , where is my fear ? says the Lord of hos |
| Mal 2:5 | My covenant with him was one of life and peace , and I gave them to him. It was a covenant of fear , and he feared me. He stood in awe of my name . |

### pa.chad (dread) → **dread**
*pole `inner` · keywords ['dread', 'object', 'terror'] · 46 verses*

| ref | verse text |
|---|---|
| Gen 31:42 | If the God of my father , the God of Abraham and the Fear of Isaac , had not been on my side, surely now you would have sent me away empty-handed . God saw my a |
| Gen 31:53 | The God of Abraham and the God of Nahor , the God of their father , judge between us .” So Jacob swore by the Fear of his father Isaac , |
| Exo 15:16 | Terror and dread fall upon them; because of the greatness of your arm , they are still as a stone , till your people , O Lord , pass by , till the people pass b |
| Deu 2:25 | This day I will begin to put the dread and fear of you on the peoples who are under the whole heaven , who shall hear the report of you and shall tremble and be |
| Deu 11:25 | No one shall be able to stand against you. The Lord your God will lay the fear of you and the dread of you on all the land that you shall tread , as he promised |
| Deu 28:67 | In the morning you shall say , ‘ If only it were evening !’ and at evening you shall say , ‘ If only it were morning !’ because of the dread that your heart sha |
| 1Sa 11:7 | He took a yoke of oxen and cut them in pieces and sent them throughout all the territory of Israel by the hand of the messengers , saying , “ Whoever does not c |
| 1Ch 14:17 | And the fame of David went out into all lands , and the Lord brought the fear of him upon all nations . |
| 2Ch 14:14 | And they attacked all the cities around Gerar , for the fear of the Lord was upon them. They plundered all the cities , for there was much plunder in them . |
| 2Ch 17:10 | And the fear of the Lord fell upon all the kingdoms of the lands that were around Judah , and they made no war against Jehoshaphat . |
| 2Ch 19:7 | Now then, let the fear of the Lord be upon you. Be careful what you do , for there is no injustice with the Lord our God , or partiality or taking bribes .” |
| 2Ch 20:29 | And the fear of God came on all the kingdoms of the countries when they heard that the Lord had fought against the enemies of Israel . |
| Est 8:17 | And in every province and in every city , wherever the king’s command and his edict reached , there was gladness and joy among the Jews , a feast and a holiday  |
| Est 9:2 | The Jews gathered in their cities throughout all the provinces of King Ahasuerus to lay hands on those who sought their harm . And no one could stand against th |
| Est 9:3 | All the officials of the provinces and the satraps and the governors and the royal agents also helped the Jews , for the fear of Mordecai had fallen on them . |
| Job 3:25 | For the thing that I fear comes upon me, and what I dread befalls me . |
| Job 4:14 | dread came upon me, and trembling , which made all my bones shake . |
| Job 13:11 | Will not his majesty terrify you, and the dread of him fall upon you ? |
| Job 15:21 | Dreadful sounds are in his ears ; in prosperity the destroyer will come upon him . |
| Job 21:9 | Their houses are safe from fear , and no rod of God is upon them . |
| Job 22:10 | Therefore snares are all around you, and sudden terror overwhelms you, |
| Job 31:23 | For I was in terror of calamity from God , and I could not have faced his majesty . |
| Job 39:22 | He laughs at fear and is not dismayed ; he does not turn back from the sword . |
| Psa 14:5 | There they are in great terror , for God is with the generation of the righteous . |
| Psa 31:11 | Because of all my adversaries I have become a reproach , especially to my neighbors , and an object of dread to my acquaintances ; those who see me in the stree |
| Psa 36:1 | To the choirmaster . Of David , the servant of the Lord . Psa 36:1 Transgression speaks to the wicked deep in his heart ; there is no fear of God before his eye |
| Psa 53:5 | There they are, in great terror , where there is no terror ! For God scatters the bones of him who encamps against you; you put them to shame , for God has reje |
| Psa 64:1 | To the choirmaster . A Psalm of David . Psa 64:1 Hear my voice , O God , in my complaint ; preserve my life from dread of the enemy . |
| Psa 91:5 | You will not fear the terror of the night , nor the arrow that flies by day , |
| Psa 105:38 | Egypt was glad when they departed , for dread of them had fallen upon it . |
| Psa 119:120 | My flesh trembles for fear of you, and I am afraid of your judgments . |
| Pro 1:26 | I also will laugh at your calamity ; I will mock when terror strikes you, |
| Pro 1:27 | when terror strikes you like a storm and your calamity comes like a whirlwind , when distress and anguish come upon you. |
| Pro 1:33 | but whoever listens to me will dwell secure and will be at ease , without dread of disaster .” |
| Pro 3:25 | Do not be afraid of sudden terror or of the ruin of the wicked , when it comes , |
| Song 3:8 | all of them wearing swords and expert in war , each with his sword at his thigh , against terror by night . |
| Isa 2:10 | Enter into the rock and hide in the dust from before the terror of the Lord , and from the splendor of his majesty . |
| Isa 2:19 | And people shall enter the caves of the rocks and the holes of the ground , from before the terror of the Lord , and from the splendor of his majesty , when he  |
| Isa 2:21 | to enter the caverns of the rocks and the clefts of the cliffs , from before the terror of the Lord , and from the splendor of his majesty , when he rises to te |
| Isa 24:17 | Terror and the pit and the snare are upon you, O inhabitant of the earth ! |
| Isa 24:18 | He who flees at the sound of the terror shall fall into the pit , and he who climbs out of the pit shall be caught in the snare . For the windows of heaven are  |
| Jer 30:5 | “ Thus says the Lord : We have heard a cry of panic , of terror , and no peace . |
| Jer 48:43 | Terror , pit , and snare are before you, O inhabitant of Moab ! declares the Lord . |
| Jer 48:44 | He who flees from the terror shall fall into the pit , and he who climbs out of the pit shall be caught in the snare . For I will bring these things upon Moab , |
| Jer 49:5 | Behold , I will bring terror upon you, declares the Lord God of hosts , from all who are around you, and you shall be driven out , every man straight before him |
| Lam 3:47 | panic and pitfall have come upon us, devastation and destruction ; |

### pach.dah (dread) → **dread**
*pole `inner` · keywords ['awe', 'dread', 'fear', 'religiou'] · 1 verses*

| ref | verse text |
|---|---|
| Jer 2:19 | Your evil will chastise you, and your apostasy will reprove you. Know and see that it is evil and bitter for you to forsake the Lord your God ; the fear of me i |

### pal.la.tsut (shuddering) → **shuddering**
*pole `inner` · metaphor-flagged · keywords ['shudder', 'trembl'] · 4 verses*

| ref | verse text |
|---|---|
| Job 21:6 | When I remember , I am dismayed , and shuddering seizes my flesh . |
| Psa 55:5 | Fear and trembling come upon me, and horror overwhelms me. |
| Isa 21:4 | My heart staggers ; horror has appalled me; the twilight I longed for has been turned for me into trembling . |
| Eze 7:18 | They put on sackcloth , and horror covers them. Shame is on all faces , and baldness on all their heads . |

### ptoeō (to frighten) → **to frighten / (<i>passive</i>) to be startled, frightenedfrighten**
*pole `inner` · keywords ['affright', 'frighten', 'frightenedfrighten', 'passive', 'startl', 'terrifi', 'terrify'] · 2 verses*

| ref | verse text |
|---|---|
| Luk 21:9 | And when you hear of wars and tumults , do not be terrified , for these things must first take place , but the end will not be at once .” |
| Luk 24:37 | But they were startled and frightened and thought they saw a spirit . |

### ptoēsis (fear) → **fear / something alarming fear**
*pole `inner` · keywords ['alarm', 'consternation', 'dismay', 'fear', 'frighten', 'pet', 'someth'] · 1 verses*

| ref | verse text |
|---|---|
| 1Pe 3:6 | as Sarah obeyed Abraham , calling him lord . And you are her children , if you do good and do not fear anything that is frightening . |

### pturomai (to frighten) → **to frighten / (<i>passive</i>) to be frightened frighten**
*pole `inner` · keywords ['consternation', 'frighten', 'passive', 'phil', 'scare', 'terrifi', 'terrify'] · 1 verses*

| ref | verse text |
|---|---|
| Phili 1:28 | and not frightened in anything by your opponents . This is a clear sign to them of their destruction , but of your salvation , and that from God . |

### ra.ad (trembling) → **trembling**
*pole `inner` · keywords ['dah', 'spell', 'trembl'] · 3 verses*

| ref | verse text |
|---|---|
| Exo 15:15 | Now are the chiefs of Edom dismayed ; trembling seizes the leaders of Moab ; all the inhabitants of Canaan have melted away . |
| Job 4:14 | dread came upon me, and trembling , which made all my bones shake . |
| Psa 55:5 | Fear and trembling come upon me, and horror overwhelms me. |

### ra.hah (to fear) → **to fear**
*pole `inner` · keywords ['fear', 'mean', 'uncertain'] · 1 verses*

| ref | verse text |
|---|---|
| Isa 44:8 | Fear not , nor be afraid ; have I not told you from of old and declared it? And you are my witnesses ! Is there a God besides me? There is no Rock ; I know not  |

### rag.gaz (quivering) → **quivering**
*pole `inner` · keywords ['quak', 'quiver', 'trembl'] · 1 verses*

| ref | verse text |
|---|---|
| Deu 28:65 | And among these nations you shall find no respite , and there shall be no resting place for the sole of your foot , but the Lord will give you there a trembling |

### re.a.dah (trembling) → **trembling**
*pole `inner` · keywords ['mean', 'trembl'] · 3 verses*

| ref | verse text |
|---|---|
| Psa 2:11 | Serve the Lord with fear , and rejoice with trembling . |
| Psa 48:6 | Trembling took hold of them there , anguish as of a woman in labor . |
| Isa 33:14 | The sinners in Zion are afraid ; trembling has seized the godless : “ Who among us can dwell with the consuming fire ? Who among us can dwell with everlasting b |

### re.tet (panic) → **panic**
*pole `inner` · keywords ['panic', 'trembl'] · 1 verses*

| ref | verse text |
|---|---|
| Jer 49:24 | Damascus has become feeble , she turned to flee , and panic seized her; anguish and sorrows have taken hold of her, as of a woman in labor . |

### re.tet (trembling) → **trembling**
*pole `inner` · keywords ['trembl'] · 1 verses*

| ref | verse text |
|---|---|
| Hos 13:1 | When Ephraim spoke , there was trembling ; he was exalted in Israel , but he incurred guilt through Baal and died . |

### rog.zah (quivering) → **quivering**
*pole `inner` · keywords ['quak', 'quiver', 'trembl'] · 1 verses*

| ref | verse text |
|---|---|
| Eze 12:18 | “ Son of man , eat your bread with quaking , and drink water with trembling and with anxiety . |

### sa.ar (shuddering) → **shuddering**
*pole `inner` · metaphor-flagged · keywords ['horror', 'shudder', 'terror'] · 3 verses*

| ref | verse text |
|---|---|
| Job 18:20 | They of the west are appalled at his day , and horror seizes them of the east . |
| Eze 27:35 | All the inhabitants of the coastlands are appalled at you, and the hair of their kings bristles with horror ; their faces are convulsed . |
| Eze 32:10 | I will make many peoples appalled at you, and the hair of their kings shall bristle with horror because of you, when I brandish my sword before them . They shal |

### sa.ar (to shudder) → **to shudder**
*pole `inner` · metaphor-flagged · keywords ['afraid', 'bristle', 'dread', 'shiver', 'shudder'] · 2 verses*

| ref | verse text |
|---|---|
| Eze 27:35 | All the inhabitants of the coastlands are appalled at you, and the hair of their kings bristles with horror ; their faces are convulsed . |
| Eze 32:10 | I will make many peoples appalled at you, and the hair of their kings shall bristle with horror because of you, when I brandish my sword before them . They shal |

### sar.ap.pim (anxiety) → **anxiety**
*pole `inner` · keywords ['anxiety', 'disquiet', 'thought'] · 2 verses*

| ref | verse text |
|---|---|
| Psa 94:19 | When the cares of my heart are many , your consolations cheer my soul . |
| Psa 139:23 | Search me, O God , and know my heart ! Try me and know my thoughts ! |

### sha.vats (agony) → **agony**
*pole `inner` · keywords ['agony', 'anguish', 'cramp', 'mean', 'uncertain'] · 1 verses*

| ref | verse text |
|---|---|
| 2Sa 1:9 | And he said to me, ‘ Stand beside me and kill me, for anguish has seized me , and yet my life still lingers .’ |

### te.vah (be startled) → **be startled**
*pole `inner` · keywords ['alarm', 'startl'] · 1 verses*

| ref | verse text |
|---|---|
| Dan 3:24 | Then King Nebuchadnezzar was astonished and rose up in haste . He declared to his counselors , “Did we not cast three men bound into the fire ?” They answered a |

### thambos (amazement) → **amazement / amazement, astonishment, wonder**
*pole `inner` · keywords ['amaze', 'astonish', 'awe', 'wonder'] · 1 verses*

| ref | verse text |
|---|---|
| Act 3:10 | and recognized him as the one who sat at the Beautiful Gate of the temple , asking for alms . And they were filled with wonder and amazement at what had happene |

### tim.ma.hon (bewilderment) → **bewilderment**
*pole `inner` · keywords ['astonish', 'bewilder', 'stupefaction'] · 2 verses*

| ref | verse text |
|---|---|
| Deu 28:28 | The Lord will strike you with madness and blindness and confusion of mind , |
| Zec 12:4 | On that day , declares the Lord , I will strike every horse with panic , and its rider with madness . But for the sake of the house of Judah I will keep my eyes |

### tiph.le.tset (terror) → **terror**
*pole `inner` · metaphor-flagged · keywords ['horror', 'shudder', 'terror'] · 1 verses*

| ref | verse text |
|---|---|
| Jer 49:16 | The horror you inspire has deceived you, and the pride of your heart , you who live in the clefts of the rock , who hold the height of the hill . Though you mak |

### tromos (trembling) → **trembling / trembling, fear**
*pole `inner` · keywords ['agitation', 'anxiou', 'awe', 'fear', 'mind', 'phil', 'primari', 'quak'] · 5 verses*

| ref | verse text |
|---|---|
| Mar 16:8 | And they went out and fled from the tomb , for trembling and astonishment had seized them, and they said nothing to anyone , for they were afraid . |
| 1Cor 2:3 | And I was with you in weakness and in fear and much trembling , |
| 2Cor 7:15 | And his affection for you is even greater , as he remembers the obedience of you all , how you received him with fear and trembling . |
| Eph 6:5 | Bondservants , obey your earthly masters with fear and trembling , with a sincere heart , as you would Christ , |
| Phili 2:12 | Therefore , my beloved , as you have always obeyed , so now , not only as in my presence but much more in my absence , work out your own salvation with fear and |

### ya.gor (fearing) → **fearing**
*pole `inner` · keywords ['fear'] · 2 verses*

| ref | verse text |
|---|---|
| Jer 22:25 | and give you into the hand of those who seek your life , into the hand of those of whom you are afraid , even into the hand of Nebuchadnezzar king of Babylon an |
| Jer 39:17 | But I will deliver you on that day , declares the Lord , and you shall not be given into the hand of the men of whom you are afraid . |

### ya.gor (to fear) → **to fear**
*pole `inner` · keywords ['afraid', 'dread', 'fear'] · 5 verses*

| ref | verse text |
|---|---|
| Deu 9:19 | For I was afraid of the anger and hot displeasure that the Lord bore against you, so that he was ready to destroy you. But the Lord listened to me that time als |
| Deu 28:60 | And he will bring upon you again all the diseases of Egypt , of which you were afraid , and they shall cling to you . |
| Job 3:25 | For the thing that I fear comes upon me, and what I dread befalls me . |
| Job 9:28 | I become afraid of all my suffering, for I know you will not hold me innocent . |
| Psa 119:39 | Turn away the reproach that I dread , for your rules are good . |

### ya.re (afraid) → **afraid**
*pole `inner` · keywords ['afraid', 'fear', 'reverent'] · 64 verses*

| ref | verse text |
|---|---|
| Gen 22:12 | He said , “Do not lay your hand on the boy or do anything to him, for now I know that you fear God , seeing you have not withheld your son , your only son, from |
| Gen 32:11 | Please deliver me from the hand of my brother , from the hand of Esau , for I fear him, that he may come and attack me , the mothers with the children . |
| Gen 42:18 | On the third day Joseph said to them, “ Do this and you will live , for I fear God : |
| Exo 9:20 | Then whoever feared the word of the Lord among the servants of Pharaoh hurried his slaves and his livestock into the houses , |
| Exo 18:21 | Moreover, look for able men from all the people , men who fear God , who are trustworthy and hate a bribe , and place such men over the people as chiefs of thou |
| Deu 7:19 | the great trials that your eyes saw , the signs , the wonders , the mighty hand , and the outstretched arm , by which the Lord your God brought you out. So will |
| Deu 20:8 | And the officers shall speak further to the people , and say , ‘ Is there any man who is fearful and fainthearted ? Let him go back to his house , lest he make  |
| Judg 7:3 | Now therefore proclaim in the ears of the people , saying , ‘ Whoever is fearful and trembling , let him return home and hurry away from Mount Gilead .’” Then 2 |
| Judg 7:10 | But if you are afraid to go down , go down to the camp with Purah your servant . |
| 1Sa 23:3 | But David’s men said to him, “ Behold , we are afraid here in Judah ; how much more then if we go to Keilah against the armies of the Philistines ?” |
| 1Ki 18:3 | And Ahab called Obadiah , who was over the household . (Now Obadiah feared the Lord greatly , |
| 1Ki 18:12 | And as soon as I have gone from you, the Spirit of the Lord will carry you I know not where . And so, when I come and tell Ahab and he cannot find you, he will  |
| 2Ki 4:1 | Now the wife of one of the sons of the prophets cried to Elisha , “Your servant my husband is dead , and you know that your servant feared the Lord , but the cr |
| 2Ki 17:32 | They also feared the Lord and appointed from among themselves all sorts of people as priests of the high places , who sacrificed for them in the shrines of the  |
| 2Ki 17:33 | So they feared the Lord but also served their own gods , after the manner of the nations from among whom they had been carried away . |
| 2Ki 17:34 | To this day they do according to the former manner . They do not fear the Lord , and they do not follow the statutes or the rules or the law or the commandment  |
| 2Ki 17:41 | So these nations feared the Lord and also served their carved images . Their children did likewise, and their children’s children — as their fathers did, so the |
| Job 1:1 | There was a man in the land of Uz whose name was Job , and that man was blameless and upright , one who feared God and turned away from evil . |
| Job 1:8 | And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and tu |
| Job 2:3 | And the Lord said to Satan , “Have you considered my servant Job , that there is none like him on the earth , a blameless and upright man , who fears God and tu |
| Psa 15:4 | in whose eyes a vile person is despised , but who honors those who fear the Lord ; who swears to his own hurt and does not change ; |
| Psa 22:23 | You who fear the Lord , praise him! All you offspring of Jacob , glorify him, and stand in awe of him, all you offspring of Israel ! |
| Psa 22:25 | From you comes my praise in the great congregation ; my vows I will perform before those who fear him. |
| Psa 25:12 | Who is the man who fears the Lord ? Him will he instruct in the way that he should choose . |
| Psa 25:14 | The friendship of the Lord is for those who fear him, and he makes known to them his covenant . |
| Psa 31:19 | Oh, how abundant is your goodness , which you have stored up for those who fear you and worked for those who take refuge in you, in the sight of the children of |
| Psa 33:18 | Behold , the eye of the Lord is on those who fear him, on those who hope in his steadfast love , |
| Psa 34:7 | The angel of the Lord encamps around those who fear him, and delivers them . |
| Psa 34:9 | Oh, fear the Lord , you his saints , for those who fear him have no lack ! |
| Psa 60:4 | You have set up a banner for those who fear you, that they may flee to it from the bow . Selah |
| Psa 61:5 | For you , O God , have heard my vows ; you have given me the heritage of those who fear your name . |
| Psa 66:16 | Come and hear , all you who fear God , and I will tell what he has done for my soul . |
| Psa 85:9 | Surely his salvation is near to those who fear him, that glory may dwell in our land . |
| Psa 103:11 | For as high as the heavens are above the earth , so great is his steadfast love toward those who fear him; |
| Psa 103:13 | As a father shows compassion to his children , so the Lord shows compassion to those who fear him. |
| Psa 103:17 | But the steadfast love of the Lord is from everlasting to everlasting on those who fear him, and his righteousness to children’s children , |
| Psa 111:5 | He provides food for those who fear him; he remembers his covenant forever . |
| Psa 112:1 | Praise the Lord ! Blessed is the man who fears the Lord , who greatly delights in his commandments ! |
| Psa 115:11 | You who fear the Lord , trust in the Lord ! He is their help and their shield . |
| Psa 115:13 | he will bless those who fear the Lord , both the small and the great . |
| Psa 118:4 | Let those who fear the Lord say , “ His steadfast love endures forever .” |
| Psa 119:74 | Those who fear you shall see me and rejoice , because I have hoped in your word . |
| Psa 119:79 | Let those who fear you turn to me, that they may know your testimonies . |
| Psa 128:1 | A Song of Ascents . Psa 128:1 Blessed is everyone who fears the Lord , who walks in his ways ! |
| Psa 128:4 | Behold , thus shall the man be blessed who fears the Lord . |
| Psa 135:20 | O house of Levi , bless the Lord ! You who fear the Lord , bless the Lord ! |
| Psa 145:19 | He fulfills the desire of those who fear him; he also hears their cry and saves them . |
| Psa 147:11 | but the Lord takes pleasure in those who fear him, in those who hope in his steadfast love . |
| Pro 13:13 | Whoever despises the word brings destruction on himself , but he who reveres the commandment will be rewarded . |
| Pro 14:2 | Whoever walks in uprightness fears the Lord , but he who is devious in his ways despises him . |
| Pro 14:16 | One who is wise is cautious and turns away from evil , but a fool is reckless and careless . |
| Pro 31:30 | Charm is deceitful , and beauty is vain , but a woman who fears the Lord is to be praised . |
| Ecc 7:18 | It is good that you should take hold of this , and from that withhold not your hand , for the one who fears God shall come out from both of them. |
| Ecc 8:12 | Though a sinner does evil a hundred times and prolongs his life, yet I know that it will be well with those who fear God , because they fear before him. |
| Ecc 8:13 | But it will not be well with the wicked , neither will he prolong his days like a shadow , because he does not fear before God . |
| Ecc 9:2 | It is the same for all , since the same event happens to the righteous and the wicked , to the good and the evil , to the clean and the unclean , to him who sac |
| Isa 50:10 | Who among you fears the Lord and obeys the voice of his servant ? Let him who walks in darkness and has no light trust in the name of the Lord and rely on his G |
| Jer 26:19 | Did Hezekiah king of Judah and all Judah put him to death ? Did he not fear the Lord and entreat the favor of the Lord , and did not the Lord relent of the disa |
| Jer 42:11 | Do not fear the king of Babylon , of whom you are afraid . Do not fear him, declares the Lord , for I am with you, to save you and to deliver you from his hand  |
| Jer 42:16 | then the sword that you fear shall overtake you there in the land of Egypt , and the famine of which you are afraid shall follow close after you to Egypt , and  |
| Dan 1:10 | and the chief of the eunuchs said to Daniel , “ I fear my lord the king , who assigned your food and your drink ; for why should he see that you were in worse c |
| Jon 1:9 | And he said to them, “I am a Hebrew , and I fear the Lord , the God of heaven , who made the sea and the dry land.” |
| Mal 3:16 | Then those who feared the Lord spoke with one another . The Lord paid attention and heard them, and a book of remembrance was written before him of those who fe |
| Mal 4:2 | But for you who fear my name , the sun of righteousness shall rise with healing in its wings . You shall go out leaping like calves from the stall . |

### yir.ah (fear) → **fear**
*pole `inner` · keywords ['awesome', 'fear', 'piety', 'respect', 'rever', 'reverence', 'terrify', 'terror'] · 43 verses*

| ref | verse text |
|---|---|
| Gen 20:11 | Abraham said , “I did it because I thought , ‘ There is no fear of God at all in this place , and they will kill me because of my wife .’ |
| Exo 20:20 | Moses said to the people , “Do not fear , for God has come to test you, that the fear of him may be before you , that you may not sin .” |
| Deu 2:25 | This day I will begin to put the dread and fear of you on the peoples who are under the whole heaven , who shall hear the report of you and shall tremble and be |
| 2Sa 23:3 | The God of Israel has spoken ; the Rock of Israel has said to me: When one rules justly over men , ruling in the fear of God , |
| 2Ch 19:9 | And he charged them: “ Thus you shall do in the fear of the Lord , in faithfulness , and with your whole heart : |
| Neh 5:9 | So I said , “The thing that you are doing is not good . Ought you not to walk in the fear of our God to prevent the taunts of the nations our enemies ? |
| Neh 5:15 | The former governors who were before me laid heavy burdens on the people and took from them for their daily ration forty shekels of silver . Even their servants |
| Job 4:6 | Is not your fear of God your confidence , and the integrity of your ways your hope ? |
| Job 6:14 | “He who withholds kindness from a friend forsakes the fear of the Almighty . |
| Job 15:4 | But you are doing away with the fear of God and hindering meditation before God . |
| Job 22:4 | Is it for your fear of him that he reproves you and enters into judgment with you? |
| Job 28:28 | And he said to man , ‘ Behold , the fear of the Lord , that is wisdom , and to turn away from evil is understanding .’” |
| Psa 2:11 | Serve the Lord with fear , and rejoice with trembling . |
| Psa 5:7 | But I , through the abundance of your steadfast love , will enter your house . I will bow down toward your holy temple in the fear of you. |
| Psa 19:9 | the fear of the Lord is clean , enduring forever ; the rules of the Lord are true , and righteous altogether . |
| Psa 34:11 | Come , O children , listen to me; I will teach you the fear of the Lord . |
| Psa 55:5 | Fear and trembling come upon me, and horror overwhelms me. |
| Psa 90:11 | Who considers the power of your anger , and your wrath according to the fear of you? |
| Psa 111:10 | The fear of the Lord is the beginning of wisdom ; all those who practice it have a good understanding . His praise endures forever ! |
| Psa 119:38 | Confirm to your servant your promise , that you may be feared . |
| Pro 1:7 | The fear of the Lord is the beginning of knowledge ; fools despise wisdom and instruction . |
| Pro 1:29 | Because they hated knowledge and did not choose the fear of the Lord , |
| Pro 2:5 | then you will understand the fear of the Lord and find the knowledge of God . |
| Pro 8:13 | The fear of the Lord is hatred of evil . Pride and arrogance and the way of evil and perverted speech I hate . |
| Pro 9:10 | The fear of the Lord is the beginning of wisdom , and the knowledge of the Holy One is insight . |
| Pro 10:27 | The fear of the Lord prolongs life , but the years of the wicked will be short . |
| Pro 14:26 | In the fear of the Lord one has strong confidence , and his children will have a refuge . |
| Pro 14:27 | The fear of the Lord is a fountain of life , that one may turn away from the snares of death . |
| Pro 15:16 | Better is a little with the fear of the Lord than great treasure and trouble with it . |
| Pro 15:33 | The fear of the Lord is instruction in wisdom , and humility comes before honor . |
| Pro 16:6 | By steadfast love and faithfulness iniquity is atoned for , and by the fear of the Lord one turns away from evil . |
| Pro 19:23 | The fear of the Lord leads to life , and whoever has it rests satisfied ; he will not be visited by harm . |
| Pro 22:4 | The reward for humility and fear of the Lord is riches and honor and life . |
| Pro 23:17 | Let not your heart envy sinners , but continue in the fear of the Lord all the day . |
| Isa 11:2 | And the Spirit of the Lord shall rest upon him, the Spirit of wisdom and understanding , the Spirit of counsel and might , the Spirit of knowledge and the fear  |
| Isa 11:3 | And his delight shall be in the fear of the Lord . He shall not judge by what his eyes see , or decide disputes by what his ears hear , |
| Isa 29:13 | And the Lord said : “ Because this people draw near with their mouth and honor me with their lips , while their hearts are far from me, and their fear of me is  |
| Isa 33:6 | and he will be the stability of your times , abundance of salvation , wisdom , and knowledge ; the fear of the Lord is Zion’s treasure . |
| Isa 63:17 | O Lord , why do you make us wander from your ways and harden our heart , so that we fear you not ? Return for the sake of your servants , the tribes of your her |
| Jer 32:40 | I will make with them an everlasting covenant , that I will not turn away from doing good to them . And I will put the fear of me in their hearts , that they ma |
| Eze 30:13 | “ Thus says the Lord God : “I will destroy the idols and put an end to the images in Memphis ; there shall no longer be a prince from the land of Egypt ; so I w |
| Jon 1:10 | Then the men were exceedingly afraid and said to him, “ What is this that you have done !” For the men knew that he was fleeing from the presence of the Lord ,  |
| Jon 1:16 | Then the men feared the Lord exceedingly , and they offered a sacrifice to the Lord and made vows . |

### za.chal (to fear) → **to fear**
*pole `inner` · keywords ['afraid', 'chal', 'fear'] · 1 verses*

| ref | verse text |
|---|---|
| Mic 7:17 | they shall lick the dust like a serpent , like the crawling things of the earth ; they shall come trembling out of their strongholds ; they shall turn in dread  |

### ze.va.ah (trembling) → **trembling**
*pole `inner` · keywords ['horror', 'object', 'terror', 'trembl'] · 1 verses*

| ref | verse text |
|---|---|
| Isa 28:19 | As often as it passes through it will take you; for morning by morning it will pass through , by day and by night ; and it will be sheer terror to understand th |

## c · Postponed to L2 (multi-sense residue) — assess why each is not L1

463 verses across 11 multi-sense terms. Each term shows **why it was classified multi-sense** (the signal that triggered the L1→L2 deferral, per discipline 2). Read the verses to judge whether the deferral is right.

### a.rats (to tremble) — **multi-sense: 3 stems (Hiphil/Niphal/Qal); pole-span:inner/physical** · 15 verses

| ref | verse text |
|---|---|
| Deu 1:29 | Then I said to you, ‘Do not be in dread or afraid of them . |
| Deu 7:21 | You shall not be in dread of them , for the Lord your God is in your midst , a great and awesome God . |
| Deu 20:3 | and shall say to them, ‘ Hear , O Israel , today you are drawing near for battle against your enemies : let not your heart faint . Do not fear or panic or be in |
| Deu 31:6 | Be strong and courageous . Do not fear or be in dread of them , for it is the Lord your God who goes with you. He will not leave you or forsake you .” |
| Jos 1:9 | Have I not commanded you? Be strong and courageous . Do not be frightened , and do not be dismayed , for the Lord your God is with you wherever you go .” |
| Job 13:25 | Will you frighten a driven leaf and pursue dry chaff ? |
| Job 31:34 | because I stood in great fear of the multitude , and the contempt of families terrified me, so that I kept silence , and did not go out of doors — |
| Psa 10:18 | to do justice to the fatherless and the oppressed , so that man who is of the earth may strike terror no more . |
| Psa 89:7 | a God greatly to be feared in the council of the holy ones , and awesome above all who are around him ? |
| Isa 2:19 | And people shall enter the caves of the rocks and the holes of the ground , from before the terror of the Lord , and from the splendor of his majesty , when he  |
| Isa 2:21 | to enter the caverns of the rocks and the clefts of the cliffs , from before the terror of the Lord , and from the splendor of his majesty , when he rises to te |
| Isa 8:12 | “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread . |
| Isa 8:13 | But the Lord of hosts , him you shall honor as holy . Let him be your fear , and let him be your dread . |
| Isa 29:23 | For when he sees his children , the work of my hands , in his midst , they will sanctify my name ; they will sanctify the Holy One of Jacob and will stand in aw |
| Isa 47:12 | Stand fast in your enchantments and your many sorceries , with which you have labored from your youth ; perhaps you may be able to succeed ; perhaps you may ins |

### ba.hal (to dismay) — **multi-sense: 4 stems (Hiphil/Niphal/Piel/Pual)** · 33 verses

| ref | verse text |
|---|---|
| Gen 45:3 | And Joseph said to his brothers , “ I am Joseph ! Is my father still alive ?” But his brothers could not answer him, for they were dismayed at his presence . |
| Exo 15:15 | Now are the chiefs of Edom dismayed ; trembling seizes the leaders of Moab ; all the inhabitants of Canaan have melted away . |
| Judg 20:41 | Then the men of Israel turned , and the men of Benjamin were dismayed , for they saw that disaster was close upon them. |
| 1Sa 28:21 | And the woman came to Saul , and when she saw that he was terrified , she said to him, “ Behold , your servant has obeyed you . I have taken my life in my hand  |
| 2Sa 4:1 | When Ish-bosheth, Saul’s son , heard that Abner had died at Hebron , his courage failed , and all Israel was dismayed . |
| 2Ch 32:18 | And they shouted it with a loud voice in the language of Judah to the people of Jerusalem who were on the wall , to frighten and terrify them, in order that the |
| Ezr 4:4 | Then the people of the land discouraged the people of Judah and made them afraid to build |
| Job 4:5 | But now it has come to you, and you are impatient ; it touches you, and you are dismayed . |
| Job 21:6 | When I remember , I am dismayed , and shuddering seizes my flesh . |
| Job 22:10 | Therefore snares are all around you, and sudden terror overwhelms you, |
| Job 23:15 | Therefore I am terrified at his presence ; when I consider , I am in dread of him . |
| Job 23:16 | God has made my heart faint ; the Almighty has terrified me ; |
| Psa 2:5 | Then he will speak to them in his wrath , and terrify them in his fury , saying, |
| Psa 6:2 | Be gracious to me, O Lord , for I am languishing ; heal me, O Lord , for my bones are troubled . |
| Psa 6:3 | My soul also is greatly troubled . But you , O Lord — how long ? |
| Psa 6:10 | All my enemies shall be ashamed and greatly troubled ; they shall turn back and be put to shame in a moment . |
| Psa 30:7 | By your favor , O Lord , you made my mountain stand strong ; you hid your face ; I was dismayed . |
| Psa 48:5 | As soon as they saw it, they were astounded ; they were in panic ; they took to flight . |
| Psa 83:15 | so may you pursue them with your tempest and terrify them with your hurricane ! |
| Psa 83:17 | Let them be put to shame and dismayed forever ; let them perish in disgrace , |
| Psa 90:7 | For we are brought to an end by your anger ; by your wrath we are dismayed . |
| Psa 104:29 | When you hide your face , they are dismayed ; when you take away their breath , they die and return to their dust . |
| Pro 28:22 | A stingy man hastens after wealth and does not know that poverty will come upon him . |
| Ecc 5:2 | Be not rash with your mouth , nor let your heart be hasty to utter a word before God , for God is in heaven and you are on earth . Therefore let your words be f |
| Ecc 7:9 | Be not quick in your spirit to become angry , for anger lodges in the heart of fools . |
| Ecc 8:3 | Be not hasty to go from his presence . Do not take your stand in an evil cause , for he does whatever he pleases . |
| Isa 13:8 | They will be dismayed : pangs and agony will seize them; they will be in anguish like a woman in labor . They will look aghast at one another ; their faces will |
| Isa 21:3 | Therefore my loins are filled with anguish ; pangs have seized me, like the pangs of a woman in labor ; I am bowed down so that I cannot hear ; I am dismayed so |
| Jer 51:32 | the fords have been seized , the marshes are burned with fire , and the soldiers are in panic . |
| Eze 7:27 | The king mourns , the prince is wrapped in despair , and the hands of the people of the land are paralyzed by terror . According to their way I will do to them, |
| Eze 26:18 | Now the coastlands tremble on the day of your fall , and the coastlands that are on the sea are dismayed at your passing .’ |
| Dan 11:44 | But news from the east and the north shall alarm him, and he shall go out with great fury to destroy and devote many to destruction. |
| Zep 1:18 | Neither their silver nor their gold shall be able to deliver them on the day of the wrath of the Lord . In the fire of his jealousy , all the earth shall be con |

### cha.rad (to tremble) — **multi-sense: 2 stems (Hiphil/Qal)** · 34 verses

| ref | verse text |
|---|---|
| Gen 27:33 | Then Isaac trembled very violently and said , “ Who was it then that hunted game and brought it to me, and I ate it all before you came , and I have blessed him |
| Gen 42:28 | He said to his brothers , “My money has been put back ; here it is in the mouth of my sack !” At this their hearts failed them, and they turned trembling to one |
| Exo 19:16 | On the morning of the third day there were thunders and lightnings and a thick cloud on the mountain and a very loud trumpet blast , so that all the people in t |
| Exo 19:18 | Now Mount Sinai was wrapped in smoke because the Lord had descended on it in fire . The smoke of it went up like the smoke of a kiln , and the whole mountain tr |
| Lev 26:6 | I will give peace in the land , and you shall lie down , and none shall make you afraid . And I will remove harmful beasts from the land , and the sword shall n |
| Judg 8:12 | And Zebah and Zalmunna fled , and he pursued them and captured the two kings of Midian , Zebah and Zalmunna , and he threw all the army into a panic . |
| Rut 3:8 | At midnight the man was startled and turned over , and behold , a woman lay at his feet ! |
| 1Sa 13:7 | and some Hebrews crossed the fords of the Jordan to the land of Gad and Gilead . Saul was still at Gilgal , and all the people followed him trembling . |
| 1Sa 14:15 | And there was a panic in the camp , in the field , and among all the people . The garrison and even the raiders trembled , the earth quaked , and it became a ve |
| 1Sa 16:4 | Samuel did what the Lord commanded and came to Bethlehem . The elders of the city came to meet him trembling and said , “Do you come peaceably ?” |
| 1Sa 21:1 | Then David came to Nob , to Ahimelech the priest . And Ahimelech came to meet David , trembling and said to him, “ Why are you alone , and no one with you ?” |
| 1Sa 28:5 | When Saul saw the army of the Philistines , he was afraid , and his heart trembled greatly . |
| 2Sa 17:2 | I will come upon him while he is weary and discouraged and throw him into a panic , and all the people who are with him will flee . I will strike down only the  |
| 1Ki 1:49 | Then all the guests of Adonijah trembled and rose , and each went his own way . |
| Job 11:19 | You will lie down , and none will make you afraid ; many will court your favor . |
| Job 37:1 | “At this also my heart trembles and leaps out of its place . |
| Isa 10:29 | they have crossed over the pass ; at Geba they lodge for the night ; Ramah trembles ; Gibeah of Saul has fled . |
| Isa 19:16 | In that day the Egyptians will be like women , and tremble with fear before the hand that the Lord of hosts shakes over them . |
| Isa 32:11 | Tremble , you women who are at ease , shudder , you complacent ones ; strip , and make yourselves bare , and tie sackcloth around your waist . |
| Isa 41:5 | The coastlands have seen and are afraid ; the ends of the earth tremble ; they have drawn near and come . |
| Jer 30:10 | “Then fear not , O Jacob my servant , declares the Lord , nor be dismayed , O Israel ; for behold , I will save you from far away , and your offspring from the  |
| Jer 46:27 | “But fear not , O Jacob my servant , nor be dismayed , O Israel , for behold , I will save you from far away , and your offspring from the land of their captivi |
| Eze 26:16 | Then all the princes of the sea will step down from their thrones and remove their robes and strip off their embroidered garments . They will clothe themselves  |
| Eze 26:18 | Now the coastlands tremble on the day of your fall , and the coastlands that are on the sea are dismayed at your passing .’ |
| Eze 30:9 | “On that day messengers shall go out from me in ships to terrify the unsuspecting people of Cush , and anguish shall come upon them on the day of Egypt’s doom;  |
| Eze 32:10 | I will make many peoples appalled at you, and the hair of their kings shall bristle with horror because of you, when I brandish my sword before them . They shal |
| Eze 34:28 | They shall no more be a prey to the nations , nor shall the beasts of the land devour them. They shall dwell securely , and none shall make them afraid . |
| Eze 39:26 | They shall forget their shame and all the treachery they have practiced against me, when they dwell securely in their land with none to make them afraid , |
| Hos 11:10 | They shall go after the Lord ; he will roar like a lion ; when he roars , his children shall come trembling from the west ; |
| Hos 11:11 | they shall come trembling like birds from Egypt , and like doves from the land of Assyria , and I will return them to their homes , declares the Lord . |
| Amo 3:6 | Is a trumpet blown in a city , and the people are not afraid ? Does disaster come to a city , unless the Lord has done it? |
| Mic 4:4 | but they shall sit every man under his vine and under his fig tree , and no one shall make them afraid , for the mouth of the Lord of hosts has spoken . |
| Zep 3:13 | those who are left in Israel ; they shall do no injustice and speak no lies , nor shall there be found in their mouth a deceitful tongue . For they shall graze  |
| Zec 1:21 | And I said , “ What are these coming to do ?” He said , “ These are the horns that scattered Judah , so that no one raised his head . And these have come to ter |

### cha.tat (to to be dismayed) — **multi-sense: 4 stems (Hiphil/Niphal/Piel/Qal); pole-span:inner/physical** · 24 verses

| ref | verse text |
|---|---|
| Job 7:14 | then you scare me with dreams and terrify me with visions , |
| Job 31:34 | because I stood in great fear of the multitude , and the contempt of families terrified me, so that I kept silence , and did not go out of doors — |
| Job 32:15 | “They are dismayed ; they answer no more ; they have not a word to say . |
| Job 39:22 | He laughs at fear and is not dismayed ; he does not turn back from the sword . |
| Isa 20:5 | Then they shall be dismayed and ashamed because of Cush their hope and of Egypt their boast . |
| Isa 30:31 | The Assyrians will be terror-stricken at the voice of the Lord , when he strikes with his rod . |
| Isa 31:4 | For thus the Lord said to me, “As a lion or a young lion growls over his prey , and when a band of shepherds is called out against him he is not terrified by th |
| Isa 31:9 | His rock shall pass away in terror , and his officers desert the standard in panic ,” declares the Lord , whose fire is in Zion , and whose furnace is in Jerusa |
| Isa 37:27 | while their inhabitants , shorn of strength , are dismayed and confounded , and have become like plants of the field and like tender grass , like grass on the h |
| Isa 51:7 | “ Listen to me, you who know righteousness , the people in whose heart is my law ; fear not the reproach of man , nor be dismayed at their revilings . |
| Jer 1:17 | But you , dress yourself for work; arise , and say to them everything that I command you. Do not be dismayed by them , lest I dismay you before them. |
| Jer 8:9 | The wise men shall be put to shame ; they shall be dismayed and taken ; behold , they have rejected the word of the Lord , so what wisdom is in them ? |
| Jer 10:2 | Thus says the Lord : “ Learn not the way of the nations , nor be dismayed at the signs of the heavens because the nations are dismayed at them , |
| Jer 17:18 | Let those be put to shame who persecute me, but let me not be put to shame ; let them be dismayed , but let me not be dismayed ; bring upon them the day of disa |
| Jer 23:4 | I will set shepherds over them who will care for them, and they shall fear no more , nor be dismayed , neither shall any be missing , declares the Lord . |
| Jer 30:10 | “Then fear not , O Jacob my servant , declares the Lord , nor be dismayed , O Israel ; for behold , I will save you from far away , and your offspring from the  |
| Jer 46:27 | “But fear not , O Jacob my servant , nor be dismayed , O Israel , for behold , I will save you from far away , and your offspring from the land of their captivi |
| Jer 48:20 | Moab is put to shame , for it is broken ; wail and cry ! Tell it beside the Arnon , that Moab is laid waste . |
| Jer 48:39 | How it is broken ! How they wail ! How Moab has turned his back in shame ! So Moab has become a derision and a horror to all that are around him .” |
| Jer 49:37 | I will terrify Elam before their enemies and before those who seek their life . I will bring disaster upon them, my fierce anger , declares the Lord . I will se |
| Jer 50:2 | “ Declare among the nations and proclaim , set up a banner and proclaim , conceal it not , and say : ‘ Babylon is taken , Bel is put to shame , Merodach is dism |
| Jer 50:36 | A sword against the diviners , that they may become fools ! A sword against her warriors , that they may be destroyed ! |
| Hab 2:17 | The violence done to Lebanon will overwhelm you, as will the destruction of the beasts that terrified them, for the blood of man and violence to the earth , to  |
| Mal 2:5 | My covenant with him was one of life and peace , and I gave them to him. It was a covenant of fear , and he feared me. He stood in awe of my name . |

### me.chit.tah (terror) — **multi-sense: pole-span:inner/physical** · 5 verses

| ref | verse text |
|---|---|
| Pro 18:7 | A fool’s mouth is his ruin , and his lips are a snare to his soul . |
| Pro 21:15 | When justice is done , it is a joy to the righteous but terror to evildoers . |
| Isa 54:14 | In righteousness you shall be established ; you shall be far from oppression , for you shall not fear ; and from terror , for it shall not come near you . |
| Jer 17:17 | Be not a terror to me; you are my refuge in the day of disaster . |
| Jer 48:39 | How it is broken ! How they wail ! How Moab has turned his back in shame ! So Moab has become a derision and a horror to all that are around him .” |

### pa.chad (to dread) — **multi-sense: 3 stems (Hiphil/Piel/Qal)** · 25 verses

| ref | verse text |
|---|---|
| Deu 28:66 | Your life shall hang in doubt before you. Night and day you shall be in dread and have no assurance of your life . |
| Deu 28:67 | In the morning you shall say , ‘ If only it were evening !’ and at evening you shall say , ‘ If only it were morning !’ because of the dread that your heart sha |
| Job 3:25 | For the thing that I fear comes upon me, and what I dread befalls me . |
| Job 4:14 | dread came upon me, and trembling , which made all my bones shake . |
| Job 23:15 | Therefore I am terrified at his presence ; when I consider , I am in dread of him . |
| Psa 14:5 | There they are in great terror , for God is with the generation of the righteous . |
| Psa 27:1 | Of David . Psa 27:1 The Lord is my light and my salvation ; whom shall I fear ? The Lord is the stronghold of my life ; of whom shall I be afraid ? |
| Psa 53:5 | There they are, in great terror , where there is no terror ! For God scatters the bones of him who encamps against you; you put them to shame , for God has reje |
| Psa 78:53 | He led them in safety , so that they were not afraid , but the sea overwhelmed their enemies . |
| Psa 119:161 | Sin and Shin Psa 119:161 Princes persecute me without cause , but my heart stands in awe of your words . |
| Pro 3:24 | If you lie down , you will not be afraid ; when you lie down , your sleep will be sweet . |
| Pro 28:14 | Blessed is the one who fears the Lord always , but whoever hardens his heart will fall into calamity . |
| Isa 12:2 | “ Behold , God is my salvation ; I will trust , and will not be afraid ; for the Lord God is my strength and my song , and he has become my salvation .” |
| Isa 19:16 | In that day the Egyptians will be like women , and tremble with fear before the hand that the Lord of hosts shakes over them . |
| Isa 19:17 | And the land of Judah will become a terror to the Egyptians . Everyone to whom it is mentioned will fear because of the purpose that the Lord of hosts has purpo |
| Isa 33:14 | The sinners in Zion are afraid ; trembling has seized the godless : “ Who among us can dwell with the consuming fire ? Who among us can dwell with everlasting b |
| Isa 44:8 | Fear not , nor be afraid ; have I not told you from of old and declared it? And you are my witnesses ! Is there a God besides me? There is no Rock ; I know not  |
| Isa 44:11 | Behold , all his companions shall be put to shame , and the craftsmen are only human . Let them all assemble , let them stand forth . They shall be terrified ;  |
| Isa 51:13 | and have forgotten the Lord , your Maker , who stretched out the heavens and laid the foundations of the earth , and you fear continually all the day because of |
| Isa 60:5 | Then you shall see and be radiant ; your heart shall thrill and exult , because the abundance of the sea shall be turned to you, the wealth of the nations shall |
| Jer 33:9 | And this city shall be to me a name of joy , a praise and a glory before all the nations of the earth who shall hear of all the good that I do for them. They sh |
| Jer 36:16 | When they heard all the words , they turned one to another in fear . And they said to Baruch , “We must report all these words to the king .” |
| Jer 36:24 | Yet neither the king nor any of his servants who heard all these words was afraid , nor did they tear their garments . |
| Hos 3:5 | Afterward the children of Israel shall return and seek the Lord their God , and David their king , and they shall come in fear to the Lord and to his goodness i |
| Mic 7:17 | they shall lick the dust like a serpent , like the crawling things of the earth ; they shall come trembling out of their strongholds ; they shall turn in dread  |

### ra.ad (to tremble) — **multi-sense: 2 stems (Hiphil/Qal)** · 2 verses

| ref | verse text |
|---|---|
| Ezr 10:9 | Then all the men of Judah and Benjamin assembled at Jerusalem within the three days . It was the ninth month , on the twentieth day of the month . And all the p |
| Dan 10:11 | And he said to me, “O Daniel , man greatly loved , understand the words that I speak to you, and stand upright , for now I have been sent to you.” And when he h |

### ra.gaz (to tremble) — **multi-sense: 3 stems (Hiphil/Hithpael/Qal)** · 20 verses

| ref | verse text |
|---|---|
| Exo 15:14 | The peoples have heard ; they tremble ; pangs have seized the inhabitants of Philistia . |
| Deu 2:25 | This day I will begin to put the dread and fear of you on the peoples who are under the whole heaven , who shall hear the report of you and shall tremble and be |
| 1Sa 28:15 | Then Samuel said to Saul , “ Why have you disturbed me by bringing me up ?” Saul answered , “I am in great distress , for the Philistines are warring against me |
| 2Sa 7:10 | And I will appoint a place for my people Israel and will plant them, so that they may dwell in their own place and be disturbed no more. And violent men shall a |
| 2Sa 18:33 | And the king was deeply moved and went up to the chamber over the gate and wept . And as he went , he said , “O my son Absalom , my son , my son Absalom ! Would |
| 1Ch 17:9 | And I will appoint a place for my people Israel and will plant them, that they may dwell in their own place and be disturbed no more . And violent men shall was |
| Psa 4:4 | Be angry , and do not sin ; ponder in your own hearts on your beds , and be silent . Selah |
| Psa 77:16 | When the waters saw you, O God , when the waters saw you, they were afraid ; indeed , the deep trembled . |
| Psa 99:1 | The Lord reigns ; let the peoples tremble ! He sits enthroned upon the cherubim ; let the earth quake ! |
| Isa 14:9 | Sheol beneath is stirred up to meet you when you come ; it rouses the shades to greet you, all who were leaders of the earth ; it raises from their thrones all  |
| Isa 14:16 | Those who see you will stare at you and ponder over you: ‘Is this the man who made the earth tremble , who shook kingdoms , |
| Isa 32:10 | In little more than a year you will shudder , you complacent women ; for the grape harvest fails , the fruit harvest will not come . |
| Isa 32:11 | Tremble , you women who are at ease , shudder , you complacent ones ; strip , and make yourselves bare , and tie sackcloth around your waist . |
| Isa 64:2 | as when fire kindles brushwood and the fire causes water to boil — to make your name known to your adversaries , and that the nations might tremble at your pres |
| Jer 33:9 | And this city shall be to me a name of joy , a praise and a glory before all the nations of the earth who shall hear of all the good that I do for them. They sh |
| Jer 50:34 | Their Redeemer is strong ; the Lord of hosts is his name . He will surely plead their cause , that he may give rest to the earth , but unrest to the inhabitants |
| Joe 2:1 | Blow a trumpet in Zion ; sound an alarm on my holy mountain ! Let all the inhabitants of the land tremble , for the day of the Lord is coming ; it is near , |
| Mic 7:17 | they shall lick the dust like a serpent , like the crawling things of the earth ; they shall come trembling out of their strongholds ; they shall turn in dread  |
| Hab 3:7 | I saw the tents of Cushan in affliction ; the curtains of the land of Midian did tremble . |
| Hab 3:16 | I hear , and my body trembles ; my lips quiver at the sound ; rottenness enters into my bones ; my legs tremble beneath me. Yet I will quietly wait for the day  |

### ta.mah (to astounded) — **multi-sense: 2 stems (Hithpael/Qal)** · 7 verses

| ref | verse text |
|---|---|
| Gen 43:33 | And they sat before him, the firstborn according to his birthright and the youngest according to his youth . And the men looked at one another in amazement . |
| Psa 48:5 | As soon as they saw it, they were astounded ; they were in panic ; they took to flight . |
| Ecc 5:8 | If you see in a province the oppression of the poor and the violation of justice and righteousness , do not be amazed at the matter , for the high official is w |
| Isa 13:8 | They will be dismayed : pangs and agony will seize them; they will be in anguish like a woman in labor . They will look aghast at one another ; their faces will |
| Isa 29:9 | Astonish yourselves and be astonished ; blind yourselves and be blind ! Be drunk , but not with wine ; stagger , but not with strong drink ! |
| Jer 4:9 | “ In that day , declares the Lord , courage shall fail both king and officials . The priests shall be appalled and the prophets astounded .” |
| Hab 1:5 | “ Look among the nations , and see ; wonder and be astounded . For I am doing a work in your days that you would not believe if told . |

### ya.re (to fear: revere) — **multi-sense: 3 stems (Niphal/Piel/Qal); 2 numbered senses** · 107 verses

| ref | verse text |
|---|---|
| Gen 28:17 | And he was afraid and said , “ How awesome is this place ! This is none other than the house of God , and this is the gate of heaven .” |
| Exo 1:17 | But the midwives feared God and did not do as the king of Egypt commanded them, but let the male children live . |
| Exo 1:21 | And because the midwives feared God , he gave them families . |
| Exo 9:30 | But as for you and your servants , I know that you do not yet fear the Lord God .” |
| Exo 14:31 | Israel saw the great power that the Lord used against the Egyptians , so the people feared the Lord , and they believed in the Lord and in his servant Moses . |
| Exo 15:11 | “ Who is like you , O Lord , among the gods ? Who is like you , majestic in holiness , awesome in glorious deeds , doing wonders ? |
| Exo 34:10 | And he said , “ Behold , I am making a covenant . Before all your people I will do marvels , such as have not been created in all the earth or in any nation . A |
| Lev 19:3 | Every one of you shall revere his mother and his father , and you shall keep my Sabbaths : I am the Lord your God . |
| Lev 19:14 | You shall not curse the deaf or put a stumbling block before the blind , but you shall fear your God : I am the Lord . |
| Lev 19:30 | You shall keep my Sabbaths and reverence my sanctuary : I am the Lord . |
| Lev 19:32 | “You shall stand up before the gray head and honor the face of an old man , and you shall fear your God : I am the Lord . |
| Lev 25:17 | You shall not wrong one another , but you shall fear your God , for I am the Lord your God . |
| Lev 25:36 | Take no interest from him or profit , but fear your God , that your brother may live beside you . |
| Lev 25:43 | You shall not rule over him ruthlessly but shall fear your God . |
| Lev 26:2 | You shall keep my Sabbaths and reverence my sanctuary : I am the Lord . |
| Deu 4:10 | how on the day that you stood before the Lord your God at Horeb , the Lord said to me, ‘ Gather the people to me, that I may let them hear my words , so that th |
| Deu 5:29 | Oh that they had such a heart as this always , to fear me and to keep all my commandments , that it might go well with them and with their descendants forever ! |
| Deu 6:2 | that you may fear the Lord your God , you and your son and your son’s son , by keeping all his statutes and his commandments , which I command you, all the days |
| Deu 6:13 | It is the Lord your God you shall fear . Him you shall serve and by his name you shall swear . |
| Deu 6:24 | And the Lord commanded us to do all these statutes , to fear the Lord our God , for our good always , that he might preserve us alive , as we are this day . |
| Deu 7:21 | You shall not be in dread of them , for the Lord your God is in your midst , a great and awesome God . |
| Deu 8:6 | So you shall keep the commandments of the Lord your God by walking in his ways and by fearing him . |
| Deu 10:12 | “And now , Israel , what does the Lord your God require of you, but to fear the Lord your God , to walk in all his ways , to love him, to serve the Lord your Go |
| Deu 10:17 | For the Lord your God is God of gods and Lord of lords , the great , the mighty , and the awesome God , who is not partial and takes no bribe . |
| Deu 10:20 | You shall fear the Lord your God . You shall serve him and hold fast to him, and by his name you shall swear . |
| Deu 10:21 | He is your praise . He is your God , who has done for you these great and terrifying things that your eyes have seen . |
| Deu 13:4 | You shall walk after the Lord your God and fear him and keep his commandments and obey his voice , and you shall serve him and hold fast to him. |
| Deu 14:23 | And before the Lord your God , in the place that he will choose , to make his name dwell there , you shall eat the tithe of your grain , of your wine , and of y |
| Deu 17:19 | And it shall be with him, and he shall read in it all the days of his life , that he may learn to fear the Lord his God by keeping all the words of this law and |
| Deu 28:58 | “ If you are not careful to do all the words of this law that are written in this book , that you may fear this glorious and awesome name , the Lord your God , |
| Deu 31:12 | Assemble the people , men , women , and little ones , and the sojourner within your towns , that they may hear and learn to fear the Lord your God , and be care |
| Deu 31:13 | and that their children , who have not known it, may hear and learn to fear the Lord your God , as long as you live in the land that you are going over the Jord |
| Jos 4:14 | On that day the Lord exalted Joshua in the sight of all Israel , and they stood in awe of him just as they had stood in awe of Moses , all the days of his life  |
| Jos 4:24 | so that all the peoples of the earth may know that the hand of the Lord is mighty , that you may fear the Lord your God forever .” |
| Jos 22:25 | For the Lord has made the Jordan a boundary between us and you, you people of Reuben and people of Gad . You have no portion in the Lord .’ So your children mig |
| Jos 24:14 | “ Now therefore fear the Lord and serve him in sincerity and in faithfulness . Put away the gods that your fathers served beyond the River and in Egypt , and se |
| Judg 6:10 | And I said to you, ‘ I am the Lord your God ; you shall not fear the gods of the Amorites in whose land you dwell .’ But you have not obeyed my voice .” |
| Judg 13:6 | Then the woman came and told her husband , “A man of God came to me, and his appearance was like the appearance of the angel of God , very awesome . I did not a |
| 1Sa 12:14 | If you will fear the Lord and serve him and obey his voice and not rebel against the commandment of the Lord , and if both you and the king who reigns over you  |
| 1Sa 12:18 | So Samuel called upon the Lord , and the Lord sent thunder and rain that day , and all the people greatly feared the Lord and Samuel . |
| 1Sa 12:24 | Only fear the Lord and serve him faithfully with all your heart . For consider what great things he has done for you . |
| 2Sa 7:23 | And who is like your people Israel , the one nation on earth whom God went to redeem to be his people , making himself a name and doing for them great and aweso |
| 1Ki 3:28 | And all Israel heard of the judgment that the king had rendered , and they stood in awe of the king , because they perceived that the wisdom of God was in him t |
| 2Ki 17:7 | And this occurred because the people of Israel had sinned against the Lord their God , who had brought them up out of the land of Egypt from under the hand of P |
| 1Ch 17:21 | And who is like your people Israel , the one nation on earth whom God went to redeem to be his people , making for yourself a name for great and awesome things  |
| 2Ch 6:33 | hear from heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may know your name |
| Neh 1:5 | And I said , “ O Lord God of heaven , the great and awesome God who keeps covenant and steadfast love with those who love him and keep his commandments , |
| Neh 1:11 | O Lord , let your ear be attentive to the prayer of your servant , and to the prayer of your servants who delight to fear your name , and give success to your s |
| Neh 4:14 | And I looked and arose and said to the nobles and to the officials and to the rest of the people , “Do not be afraid of them . Remember the Lord , who is great  |
| Neh 7:2 | I gave my brother Hanani and Hananiah the governor of the castle charge over Jerusalem , for he was a more faithful and God-fearing man than many . |
| Neh 9:32 | “ Now , therefore, our God , the great , the mighty , and the awesome God , who keeps covenant and steadfast love , let not all the hardship seem little to you  |
| Job 1:9 | Then Satan answered the Lord and said , “Does Job fear God for no reason ? |
| Job 37:22 | Out of the north comes golden splendor ; God is clothed with awesome majesty . |
| Job 37:24 | Therefore men fear him; he does not regard any who are wise in their own conceit .” |
| Psa 27:1 | Of David . Psa 27:1 The Lord is my light and my salvation ; whom shall I fear ? The Lord is the stronghold of my life ; of whom shall I be afraid ? |
| Psa 33:8 | Let all the earth fear the Lord ; let all the inhabitants of the world stand in awe of him! |
| Psa 34:9 | Oh, fear the Lord , you his saints , for those who fear him have no lack ! |
| Psa 40:3 | He put a new song in my mouth , a song of praise to our God . Many will see and fear , and put their trust in the Lord . |
| Psa 45:4 | In your majesty ride out victoriously for the cause of truth and meekness and righteousness ; let your right hand teach you awesome deeds ! |
| Psa 47:2 | For the Lord , the Most High , is to be feared , a great king over all the earth . |
| Psa 52:6 | The righteous shall see and fear , and shall laugh at him, saying, |
| Psa 55:19 | God will give ear and humble them, he who is enthroned from of old , Selah because they do not change and do not fear God . |
| Psa 64:9 | Then all mankind fears ; they tell what God has brought about and ponder what he has done . |
| Psa 65:5 | By awesome deeds you answer us with righteousness , O God of our salvation , the hope of all the ends of the earth and of the farthest seas ; |
| Psa 65:8 | so that those who dwell at the ends of the earth are in awe at your signs . You make the going out of the morning and the evening to shout for joy . |
| Psa 66:3 | Say to God , “ How awesome are your deeds ! So great is your power that your enemies come cringing to you. |
| Psa 66:5 | Come and see what God has done: he is awesome in his deeds toward the children of man . |
| Psa 67:7 | God shall bless us; let all the ends of the earth fear him! |
| Psa 68:35 | Awesome is God from his sanctuary ; the God of Israel — he is the one who gives power and strength to his people . Blessed be God ! |
| Psa 86:11 | Teach me your way , O Lord , that I may walk in your truth ; unite my heart to fear your name . |
| Psa 89:7 | a God greatly to be feared in the council of the holy ones , and awesome above all who are around him ? |
| Psa 96:4 | For great is the Lord , and greatly to be praised ; he is to be feared above all gods . |
| Psa 99:3 | Let them praise your great and awesome name ! Holy is he ! |
| Psa 102:15 | Nations will fear the name of the Lord , and all the kings of the earth will fear your glory . |
| Psa 106:22 | wondrous works in the land of Ham , and awesome deeds by the Red Sea . |
| Psa 111:9 | He sent redemption to his people ; he has commanded his covenant forever . Holy and awesome is his name ! |
| Psa 119:63 | I am a companion of all who fear you, of those who keep your precepts . |
| Psa 130:4 | But with you there is forgiveness , that you may be feared . |
| Psa 139:14 | I praise you, for I am fearfully and wonderfully made . Wonderful are your works ; my soul knows it very well . |
| Psa 145:6 | They shall speak of the might of your awesome deeds , and I will declare your greatness . |
| Pro 3:7 | Be not wise in your own eyes ; fear the Lord , and turn away from evil . |
| Pro 24:21 | My son , fear the Lord and the king , and do not join with those who do otherwise , |
| Ecc 3:14 | I perceived that whatever God does endures forever ; nothing can be added to it, nor anything taken from it. God has done it, so that people fear before him. |
| Ecc 5:7 | For when dreams increase and words grow many , there is vanity ; but God is the one you must fear . |
| Ecc 8:12 | Though a sinner does evil a hundred times and prolongs his life, yet I know that it will be well with those who fear God , because they fear before him. |
| Ecc 12:13 | The end of the matter ; all has been heard . Fear God and keep his commandments , for this is the whole duty of man . |
| Isa 57:11 | Whom did you dread and fear , so that you lied , and did not remember me, did not lay it to heart ? Have I not held my peace , even for a long time , and you do |
| Isa 59:19 | So they shall fear the name of the Lord from the west , and his glory from the rising of the sun ; for he will come like a rushing stream , which the wind of th |
| Isa 64:3 | When you did awesome things that we did not look for, you came down , the mountains quaked at your presence . |
| Jer 5:22 | Do you not fear me? declares the Lord . Do you not tremble before me ? I placed the sand as the boundary for the sea , a perpetual barrier that it cannot pass ; |
| Jer 5:24 | They do not say in their hearts , ‘Let us fear the Lord our God , who gives the rain in its season , the autumn rain and the spring rain , and keeps for us the  |
| Jer 10:7 | Who would not fear you, O King of the nations ? For this is your due ; for among all the wise ones of the nations and in all their kingdoms there is none like y |
| Jer 32:39 | I will give them one heart and one way , that they may fear me forever , for their own good and the good of their children after them . |
| Jer 44:10 | They have not humbled themselves even to this day , nor have they feared , nor walked in my law and my statutes that I set before you and before your fathers . |
| Eze 1:22 | Over the heads of the living creatures there was the likeness of an expanse , shining like awe-inspiring crystal , spread out above their heads . |
| Dan 9:4 | I prayed to the Lord my God and made confession , saying , “ O Lord , the great and awesome God , who keeps covenant and steadfast love with those who love him  |
| Hos 10:3 | For now they will say : “We have no king , for we do not fear the Lord ; and a king — what could he do for us ?” |
| Joe 2:11 | The Lord utters his voice before his army , for his camp is exceedingly great ; he who executes his word is powerful . For the day of the Lord is great and very |
| Jon 1:16 | Then the men feared the Lord exceedingly , and they offered a sacrifice to the Lord and made vows . |
| Mic 7:17 | they shall lick the dust like a serpent , like the crawling things of the earth ; they shall come trembling out of their strongholds ; they shall turn in dread  |
| Hab 3:2 | O Lord , I have heard the report of you, and your work, O Lord , do I fear . In the midst of the years revive it ; in the midst of the years make it known ; in  |
| Zep 2:11 | The Lord will be awesome against them; for he will famish all the gods of the earth , and to him shall bow down, each in its place , all the lands of the nation |
| Zep 3:7 | I said , ‘ Surely you will fear me; you will accept correction . Then your dwelling would not be cut off according to all that I have appointed against you.’ Bu |
| Hag 1:12 | Then Zerubbabel the son of Shealtiel , and Joshua the son of Jehozadak , the high priest , with all the remnant of the people , obeyed the voice of the Lord the |
| Mal 1:14 | Cursed be the cheat who has a male in his flock , and vows it, and yet sacrifices to the Lord what is blemished . For I am a great King , says the Lord of hosts |
| Mal 2:5 | My covenant with him was one of life and peace , and I gave them to him. It was a covenant of fear , and he feared me. He stood in awe of my name . |
| Mal 3:5 | “Then I will draw near to you for judgment . I will be a swift witness against the sorcerers , against the adulterers , against those who swear falsely , agains |

### ya.re (to fear: revere) — **multi-sense: 3 stems (Niphal/Piel/Qal); 2 numbered senses** · 191 verses

| ref | verse text |
|---|---|
| Gen 3:10 | And he said , “I heard the sound of you in the garden , and I was afraid , because I was naked , and I hid myself.” |
| Gen 15:1 | After these things the word of the Lord came to Abram in a vision : “ Fear not , Abram , I am your shield ; your reward shall be very great .” |
| Gen 18:15 | But Sarah denied it, saying , “I did not laugh ,” for she was afraid . He said , “ No , but you did laugh .” |
| Gen 19:30 | Now Lot went up out of Zoar and lived in the hills with his two daughters , for he was afraid to live in Zoar . So he lived in a cave with his two daughters . |
| Gen 20:8 | So Abimelech rose early in the morning and called all his servants and told them all these things . And the men were very much afraid . |
| Gen 21:17 | And God heard the voice of the boy , and the angel of God called to Hagar from heaven and said to her, “What troubles you, Hagar ? Fear not, for God has heard t |
| Gen 26:7 | When the men of the place asked him about his wife , he said , “She is my sister ,” for he feared to say , “My wife ,” thinking, “lest the men of the place shou |
| Gen 26:24 | And the Lord appeared to him the same night and said , “ I am the God of Abraham your father . Fear not, for I am with you and will bless you and multiply your  |
| Gen 31:31 | Jacob answered and said to Laban , “ Because I was afraid , for I thought that you would take your daughters from me by force . |
| Gen 32:7 | Then Jacob was greatly afraid and distressed . He divided the people who were with him, and the flocks and herds and camels , into two camps , |
| Gen 35:17 | And when her labor was at its hardest , the midwife said to her, “Do not fear , for you have another son .” |
| Gen 42:35 | As they emptied their sacks , behold , every man’s bundle of money was in his sack . And when they and their father saw their bundles of money , they were afrai |
| Gen 43:18 | And the men were afraid because they were brought to Joseph’s house , and they said , “It is because of the money , which was replaced in our sacks the first ti |
| Gen 43:23 | He replied , “ Peace to you, do not be afraid . Your God and the God of your father has put treasure in your sacks for you. I received your money .” Then he bro |
| Gen 46:3 | Then he said , “ I am God , the God of your father . Do not be afraid to go down to Egypt , for there I will make you into a great nation . |
| Gen 50:19 | But Joseph said to them, “Do not fear , for am I in the place of God ? |
| Gen 50:21 | So do not fear ; I will provide for you and your little ones .” Thus he comforted them and spoke kindly to them. |
| Exo 2:14 | He answered , “ Who made you a prince and a judge over us? Do you mean to kill me as you killed the Egyptian ?” Then Moses was afraid , and thought , “ Surely t |
| Exo 3:6 | And he said , “ I am the God of your father , the God of Abraham , the God of Isaac , and the God of Jacob .” And Moses hid his face , for he was afraid to look |
| Exo 14:10 | When Pharaoh drew near , the people of Israel lifted up their eyes , and behold , the Egyptians were marching after them, and they feared greatly . And the peop |
| Exo 14:13 | And Moses said to the people , “ Fear not, stand firm , and see the salvation of the Lord , which he will work for you today . For the Egyptians whom you see to |
| Exo 20:20 | Moses said to the people , “Do not fear , for God has come to test you, that the fear of him may be before you , that you may not sin .” |
| Exo 34:30 | Aaron and all the people of Israel saw Moses , and behold , the skin of his face shone , and they were afraid to come near him . |
| Num 12:8 | With him I speak mouth to mouth , clearly , and not in riddles , and he beholds the form of the Lord . Why then were you not afraid to speak against my servant  |
| Num 14:9 | Only do not rebel against the Lord . And do not fear the people of the land , for they are bread for us. Their protection is removed from them, and the Lord is  |
| Num 21:34 | But the Lord said to Moses , “Do not fear him, for I have given him into your hand , and all his people , and his land . And you shall do to him as you did to S |
| Deu 1:21 | See , the Lord your God has set the land before you. Go up , take possession , as the Lord , the God of your fathers , has told you. Do not fear or be dismayed  |
| Deu 1:29 | Then I said to you, ‘Do not be in dread or afraid of them . |
| Deu 2:4 | and command the people , “ You are about to pass through the territory of your brothers , the people of Esau , who live in Seir ; and they will be afraid of you |
| Deu 3:2 | But the Lord said to me, ‘Do not fear him, for I have given him and all his people and his land into your hand . And you shall do to him as you did to Sihon the |
| Deu 3:22 | You shall not fear them, for it is the Lord your God who fights for you .’ |
| Deu 5:5 | while I stood between the Lord and you at that time , to declare to you the word of the Lord . For you were afraid because of the fire , and you did not go up i |
| Deu 7:18 | you shall not be afraid of them but you shall remember what the Lord your God did to Pharaoh and to all Egypt , |
| Deu 13:11 | And all Israel shall hear and fear and never again do any such wickedness as this among you. |
| Deu 17:13 | And all the people shall hear and fear and not act presumptuously again . |
| Deu 19:20 | And the rest shall hear and fear , and shall never again commit any such evil among you. |
| Deu 20:1 | “When you go out to war against your enemies , and see horses and chariots and an army larger than your own, you shall not be afraid of them, for the Lord your  |
| Deu 20:3 | and shall say to them, ‘ Hear , O Israel , today you are drawing near for battle against your enemies : let not your heart faint . Do not fear or panic or be in |
| Deu 21:21 | Then all the men of the city shall stone him to death with stones . So you shall purge the evil from your midst , and all Israel shall hear , and fear . |
| Deu 25:18 | how he attacked you on the way when you were faint and weary , and cut off your tail , those who were lagging behind you, and he did not fear God . |
| Deu 28:10 | And all the peoples of the earth shall see that you are called by the name of the Lord , and they shall be afraid of you . |
| Deu 28:58 | “ If you are not careful to do all the words of this law that are written in this book , that you may fear this glorious and awesome name , the Lord your God , |
| Deu 31:6 | Be strong and courageous . Do not fear or be in dread of them , for it is the Lord your God who goes with you. He will not leave you or forsake you .” |
| Deu 31:8 | It is the Lord who goes before you. He will be with you; he will not leave you or forsake you. Do not fear or be dismayed .” |
| Jos 8:1 | And the Lord said to Joshua , “Do not fear and do not be dismayed . Take all the fighting men with you, and arise , go up to Ai . See , I have given into your h |
| Jos 9:24 | They answered Joshua , “Because it was told to your servants for a certainty that the Lord your God had commanded his servant Moses to give you all the land and |
| Jos 10:2 | he feared greatly , because Gibeon was a great city , like one of the royal cities , and because it was greater than Ai , and all its men were warriors . |
| Jos 10:8 | And the Lord said to Joshua , “Do not fear them, for I have given them into your hands . Not a man of them shall stand before you.” |
| Jos 10:25 | And Joshua said to them, “Do not be afraid or dismayed ; be strong and courageous . For thus the Lord will do to all your enemies against whom you fight .” |
| Jos 11:6 | And the Lord said to Joshua , “Do not be afraid of them, for tomorrow at this time I will give over all of them, slain , to Israel . You shall hamstring their h |
| Judg 4:18 | And Jael came out to meet Sisera and said to him, “Turn aside , my lord ; turn aside to me; do not be afraid .” So he turned aside to her into the tent , and sh |
| Judg 6:23 | But the Lord said to him, “ Peace be to you. Do not fear ; you shall not die .” |
| Judg 6:27 | So Gideon took ten men of his servants and did as the Lord had told him. But because he was too afraid of his family and the men of the town to do it by day , h |
| Judg 8:20 | So he said to Jether his firstborn , “ Rise and kill them!” But the young man did not draw his sword , for he was afraid , because he was still a young man . |
| Rut 3:11 | And now , my daughter , do not fear . I will do for you all that you ask , for all my fellow townsmen know that you are a worthy woman . |
| 1Sa 3:15 | Samuel lay until morning ; then he opened the doors of the house of the Lord . And Samuel was afraid to tell the vision to Eli . |
| 1Sa 4:7 | the Philistines were afraid , for they said , “A god has come into the camp .” And they said , “ Woe to us! For nothing like this has happened before . |
| 1Sa 4:20 | And about the time of her death the women attending her said to her, “Do not be afraid , for you have borne a son .” But she did not answer or pay attention . |
| 1Sa 7:7 | Now when the Philistines heard that the people of Israel had gathered at Mizpah , the lords of the Philistines went up against Israel . And when the people of I |
| 1Sa 12:20 | And Samuel said to the people , “Do not be afraid ; you have done all this evil . Yet do not turn aside from following the Lord , but serve the Lord with all yo |
| 1Sa 14:26 | And when the people entered the forest , behold , the honey was dropping , but no one put his hand to his mouth , for the people feared the oath . |
| 1Sa 15:24 | Saul said to Samuel , “I have sinned , for I have transgressed the commandment of the Lord and your words , because I feared the people and obeyed their voice . |
| 1Sa 17:11 | When Saul and all Israel heard these words of the Philistine , they were dismayed and greatly afraid . |
| 1Sa 17:24 | All the men of Israel , when they saw the man , fled from him and were much afraid . |
| 1Sa 18:12 | Saul was afraid of David because the Lord was with him but had departed from Saul . |
| 1Sa 18:29 | Saul was even more afraid of David . So Saul was David’s enemy continually . |
| 1Sa 21:12 | And David took these words to heart and was much afraid of Achish the king of Gath . |
| 1Sa 22:23 | Stay with me; do not be afraid , for he who seeks my life seeks your life . With me you shall be in safekeeping .” |
| 1Sa 23:17 | And he said to him, “Do not fear , for the hand of Saul my father shall not find you . You shall be king over Israel , and I shall be next to you. Saul my fathe |
| 1Sa 28:5 | When Saul saw the army of the Philistines , he was afraid , and his heart trembled greatly . |
| 1Sa 28:13 | The king said to her, “Do not be afraid . What do you see ?” And the woman said to Saul , “I see a god coming up out of the earth .” |
| 1Sa 28:20 | Then Saul fell at once full length on the ground , filled with fear because of the words of Samuel . And there was no strength in him, for he had eaten nothing  |
| 1Sa 31:4 | Then Saul said to his armor-bearer , “ Draw your sword , and thrust me through with it, lest these uncircumcised come and thrust me through , and mistreat me.”  |
| 2Sa 1:14 | David said to him, “ How is it you were not afraid to put out your hand to destroy the Lord’s anointed ?” |
| 2Sa 3:11 | And Ish-bosheth could not answer Abner another word , because he feared him . |
| 2Sa 6:9 | And David was afraid of the Lord that day , and he said , “How can the ark of the Lord come to me?” |
| 2Sa 9:7 | And David said to him, “Do not fear , for I will show you kindness for the sake of your father Jonathan , and I will restore to you all the land of Saul your fa |
| 2Sa 10:19 | And when all the kings who were servants of Hadadezer saw that they had been defeated by Israel , they made peace with Israel and became subject to them. So the |
| 2Sa 12:18 | On the seventh day the child died . And the servants of David were afraid to tell him that the child was dead , for they said , “ Behold , while the child was y |
| 2Sa 13:28 | Then Absalom commanded his servants , “ Mark when Amnon’s heart is merry with wine , and when I say to you, ‘ Strike Amnon ,’ then kill him. Do not fear ; have  |
| 2Sa 14:15 | Now I have come to say this to my lord the king because the people have made me afraid , and your servant thought , ‘I will speak to the king ; it may be that t |
| 1Ki 1:50 | And Adonijah feared Solomon . So he arose and went and took hold of the horns of the altar . |
| 1Ki 1:51 | Then it was told Solomon , “ Behold , Adonijah fears King Solomon , for behold , he has laid hold of the horns of the altar , saying , ‘Let King Solomon swear t |
| 1Ki 8:40 | that they may fear you all the days that they live in the land that you gave to our fathers . |
| 1Ki 8:43 | hear in heaven your dwelling place and do according to all for which the foreigner calls to you, in order that all the peoples of the earth may know your name a |
| 1Ki 17:13 | And Elijah said to her, “Do not fear ; go and do as you have said . But first make me a little cake of it and bring it to me, and afterward make something for y |
| 2Ki 1:15 | Then the angel of the Lord said to Elijah , “Go down with him; do not be afraid of him .” So he arose and went down with him to the king |
| 2Ki 6:16 | He said , “Do not be afraid , for those who are with us are more than those who are with them .” |
| 2Ki 10:4 | But they were exceedingly afraid and said , “ Behold , the two kings could not stand before him. How then can we stand ?” |
| 2Ki 17:25 | And at the beginning of their dwelling there , they did not fear the Lord . Therefore the Lord sent lions among them, which killed some of them . |
| 2Ki 17:28 | So one of the priests whom they had carried away from Samaria came and lived in Bethel and taught them how they should fear the Lord . |
| 2Ki 17:35 | The Lord made a covenant with them and commanded them, “You shall not fear other gods or bow yourselves to them or serve them or sacrifice to them , |
| 2Ki 17:36 | but you shall fear the Lord , who brought you out of the land of Egypt with great power and with an outstretched arm . You shall bow yourselves to him, and to h |
| 2Ki 17:37 | And the statutes and the rules and the law and the commandment that he wrote for you, you shall always be careful to do . You shall not fear other gods , |
| 2Ki 17:38 | and you shall not forget the covenant that I have made with you. You shall not fear other gods , |
| 2Ki 17:39 | but you shall fear the Lord your God , and he will deliver you out of the hand of all your enemies .” |
| 2Ki 19:6 | Isaiah said to them, “ Say to your master , ‘Thus says the Lord : Do not be afraid because of the words that you have heard , with which the servants of the kin |
| 2Ki 25:24 | And Gedaliah swore to them and their men , saying , “Do not be afraid because of the Chaldean officials . Live in the land and serve the king of Babylon , and i |
| 2Ki 25:26 | Then all the people , both small and great , and the captains of the forces arose and went to Egypt , for they were afraid of the Chaldeans . |
| 1Ch 10:4 | Then Saul said to his armor-bearer , “ Draw your sword and thrust me through with it, lest these uncircumcised come and mistreat me.” But his armor-bearer would |
| 1Ch 13:12 | And David was afraid of God that day , and he said , “ How can I bring the ark of God home to me?” |
| 1Ch 16:25 | For great is the Lord , and greatly to be praised , and he is to be feared above all gods . |
| 1Ch 22:13 | Then you will prosper if you are careful to observe the statutes and the rules that the Lord commanded Moses for Israel . Be strong and courageous . Fear not ;  |
| 1Ch 28:20 | Then David said to Solomon his son , “Be strong and courageous and do it . Do not be afraid and do not be dismayed , for the Lord God , even my God , is with yo |
| Neh 2:2 | And the king said to me, “ Why is your face sad , seeing you are not sick ? This is nothing but sadness of the heart .” Then I was very much afraid . |
| Neh 4:14 | And I looked and arose and said to the nobles and to the officials and to the rest of the people , “Do not be afraid of them . Remember the Lord , who is great  |
| Neh 6:9 | For they all wanted to frighten us, thinking , “Their hands will drop from the work , and it will not be done .” But now , O God, strengthen my hands . |
| Neh 6:13 | For this purpose he was hired , that I should be afraid and act in this way and sin , and so they could give me a bad name in order to taunt me . |
| Neh 6:14 | Remember Tobiah and Sanballat , O my God , according to these things that they did , and also the prophetess Noadiah and the rest of the prophets who wanted to  |
| Neh 6:16 | And when all our enemies heard of it, all the nations around us were afraid and fell greatly in their own esteem , for they perceived that this work had been ac |
| Neh 6:19 | Also they spoke of his good deeds in my presence and reported my words to him. And Tobiah sent letters to make me afraid . |
| Job 5:21 | You shall be hidden from the lash of the tongue , and shall not fear destruction when it comes . |
| Job 5:22 | At destruction and famine you shall laugh , and shall not fear the beasts of the earth . |
| Job 6:21 | For you have now become nothing ; you see my calamity and are afraid . |
| Job 9:35 | Then I would speak without fear of him, for I am not so in myself . |
| Job 11:15 | Surely then you will lift up your face without blemish ; you will be secure and will not fear . |
| Job 32:6 | And Elihu the son of Barachel the Buzite answered and said : “I am young in years , and you are aged ; therefore I was timid and afraid to declare my opinion to |
| Psa 3:6 | I will not be afraid of many thousands of people who have set themselves against me all around . |
| Psa 23:4 | Even though I walk through the valley of the shadow of death , I will fear no evil , for you are with me; your rod and your staff , they comfort me . |
| Psa 27:3 | Though an army encamp against me, my heart shall not fear ; though war arise against me, yet I will be confident . |
| Psa 46:2 | Therefore we will not fear though the earth give way , though the mountains be moved into the heart of the sea , |
| Psa 49:5 | Why should I fear in times of trouble , when the iniquity of those who cheat me surrounds me , |
| Psa 49:16 | Be not afraid when a man becomes rich , when the glory of his house increases . |
| Psa 56:3 | When I am afraid , I put my trust in you. |
| Psa 56:4 | In God , whose word I praise , in God I trust ; I shall not be afraid . What can flesh do to me ? |
| Psa 56:11 | in God I trust ; I shall not be afraid . What can man do to me ? |
| Psa 64:4 | shooting from ambush at the blameless , shooting at him suddenly and without fear . |
| Psa 72:5 | May they fear you while the sun endures , and as long as the moon , throughout all generations ! |
| Psa 76:7 | But you , you are to be feared ! Who can stand before you when once your anger is roused ? |
| Psa 76:8 | From the heavens you uttered judgment ; the earth feared and was still , |
| Psa 76:12 | who cuts off the spirit of princes , who is to be feared by the kings of the earth . |
| Psa 91:5 | You will not fear the terror of the night , nor the arrow that flies by day , |
| Psa 112:7 | He is not afraid of bad news ; his heart is firm , trusting in the Lord . |
| Psa 112:8 | His heart is steady ; he will not be afraid , until he looks in triumph on his adversaries . |
| Psa 118:6 | The Lord is on my side; I will not fear . What can man do to me? |
| Psa 119:120 | My flesh trembles for fear of you, and I am afraid of your judgments . |
| Pro 3:25 | Do not be afraid of sudden terror or of the ruin of the wicked , when it comes , |
| Pro 31:21 | She is not afraid of snow for her household , for all her household are clothed in scarlet . |
| Ecc 12:5 | they are afraid also of what is high , and terrors are in the way ; the almond tree blossoms , the grasshopper drags itself along, and desire fails , because ma |
| Isa 7:4 | And say to him, ‘Be careful , be quiet , do not fear , and do not let your heart be faint because of these two smoldering stumps of firebrands , at the fierce a |
| Isa 8:12 | “Do not call conspiracy all that this people calls conspiracy , and do not fear what they fear , nor be in dread . |
| Isa 10:24 | Therefore thus says the Lord God of hosts : “O my people , who dwell in Zion , be not afraid of the Assyrians when they strike with the rod and lift up their st |
| Isa 18:2 | which sends ambassadors by the sea , in vessels of papyrus on the waters ! Go , you swift messengers , to a nation tall and smooth , to a people feared near and |
| Isa 18:7 | At that time tribute will be brought to the Lord of hosts from a people tall and smooth , from a people feared near and far , a nation mighty and conquering , w |
| Isa 25:3 | Therefore strong peoples will glorify you; cities of ruthless nations will fear you . |
| Isa 35:4 | Say to those who have an anxious heart , “Be strong ; fear not ! Behold , your God will come with vengeance , with the recompense of God . He will come and save |
| Isa 37:6 | Isaiah said to them, “ Say to your master , ‘ Thus says the Lord : Do not be afraid because of the words that you have heard , with which the young men of the k |
| Isa 40:9 | Go on up to a high mountain , O Zion , herald of good news ; lift up your voice with strength , O Jerusalem , herald of good news ; lift it up , fear not ; say  |
| Isa 41:5 | The coastlands have seen and are afraid ; the ends of the earth tremble ; they have drawn near and come . |
| Isa 41:10 | fear not , for I am with you; be not dismayed , for I am your God ; I will strengthen you, I will help you, I will uphold you with my righteous right hand . |
| Isa 41:13 | For I , the Lord your God , hold your right hand ; it is I who say to you, “ Fear not , I am the one who helps you .” |
| Isa 41:14 | Fear not , you worm Jacob , you men of Israel ! I am the one who helps you, declares the Lord ; your Redeemer is the Holy One of Israel . |
| Isa 43:1 | But now thus says the Lord , he who created you, O Jacob , he who formed you, O Israel : “ Fear not , for I have redeemed you; I have called you by name , you a |
| Isa 43:5 | Fear not , for I am with you; I will bring your offspring from the east , and from the west I will gather you . |
| Isa 44:2 | Thus says the Lord who made you, who formed you from the womb and will help you: Fear not , O Jacob my servant , Jeshurun whom I have chosen . |
| Isa 51:7 | “ Listen to me, you who know righteousness , the people in whose heart is my law ; fear not the reproach of man , nor be dismayed at their revilings . |
| Isa 51:12 | “ I , I am he who comforts you; who are you that you are afraid of man who dies , of the son of man who is made like grass , |
| Isa 54:4 | “ Fear not , for you will not be ashamed ; be not confounded , for you will not be disgraced ; for you will forget the shame of your youth , and the reproach of |
| Isa 54:14 | In righteousness you shall be established ; you shall be far from oppression , for you shall not fear ; and from terror , for it shall not come near you . |
| Jer 1:8 | Do not be afraid of them , for I am with you to deliver you, declares the Lord .” |
| Jer 3:8 | She saw that for all the adulteries of that faithless one, Israel , I had sent her away with a decree of divorce . Yet her treacherous sister Judah did not fear |
| Jer 10:5 | Their idols are like scarecrows in a cucumber field , and they cannot speak ; they have to be carried , for they cannot walk . Do not be afraid of them, for the |
| Jer 23:4 | I will set shepherds over them who will care for them, and they shall fear no more , nor be dismayed , neither shall any be missing , declares the Lord . |
| Jer 26:21 | And when King Jehoiakim , with all his warriors and all the officials , heard his words , the king sought to put him to death . But when Uriah heard of it, he w |
| Jer 30:10 | “Then fear not , O Jacob my servant , declares the Lord , nor be dismayed , O Israel ; for behold , I will save you from far away , and your offspring from the  |
| Jer 40:9 | Gedaliah the son of Ahikam , son of Shaphan , swore to them and their men , saying , “Do not be afraid to serve the Chaldeans . Dwell in the land and serve the  |
| Jer 41:18 | because of the Chaldeans . For they were afraid of them, because Ishmael the son of Nethaniah had struck down Gedaliah the son of Ahikam , whom the king of Baby |
| Jer 42:11 | Do not fear the king of Babylon , of whom you are afraid . Do not fear him, declares the Lord , for I am with you, to save you and to deliver you from his hand  |
| Jer 46:27 | “But fear not , O Jacob my servant , nor be dismayed , O Israel , for behold , I will save you from far away , and your offspring from the land of their captivi |
| Jer 46:28 | Fear not , O Jacob my servant , declares the Lord , for I am with you. I will make a full end of all the nations to which I have driven you, but of you I will n |
| Jer 51:46 | Let not your heart faint , and be not fearful at the report heard in the land , when a report comes in one year and afterward a report in another year , and vio |
| Lam 3:57 | You came near when I called on you; you said , ‘Do not fear !’ |
| Eze 2:6 | And you , son of man , be not afraid of them, nor be afraid of their words , though briers and thorns are with you and you sit on scorpions . Be not afraid of t |
| Eze 3:9 | Like emery harder than flint have I made your forehead . Fear them not , nor be dismayed at their looks , for they are a rebellious house .” |
| Eze 11:8 | You have feared the sword , and I will bring the sword upon you, declares the Lord God . |
| Dan 10:12 | Then he said to me, “ Fear not , Daniel , for from the first day that you set your heart to understand and humbled yourself before your God , your words have be |
| Dan 10:19 | And he said , “O man greatly loved , fear not , peace be with you; be strong and of good courage .” And as he spoke to me, I was strengthened and said , “Let my |
| Joe 2:21 | “ Fear not , O land ; be glad and rejoice , for the Lord has done great things ! |
| Joe 2:22 | Fear not , you beasts of the field , for the pastures of the wilderness are green ; the tree bears its fruit ; the fig tree and vine give their full yield . |
| Joe 2:31 | The sun shall be turned to darkness , and the moon to blood , before the great and awesome day of the Lord comes . |
| Amo 3:8 | The lion has roared ; who will not fear ? The Lord God has spoken ; who can but prophesy ?” |
| Jon 1:5 | Then the mariners were afraid , and each cried out to his god . And they hurled the cargo that was in the ship into the sea to lighten it for them. But Jonah ha |
| Jon 1:10 | Then the men were exceedingly afraid and said to him, “ What is this that you have done !” For the men knew that he was fleeing from the presence of the Lord ,  |
| Hab 1:7 | They are dreaded and fearsome ; their justice and dignity go forth from themselves. |
| Zep 3:15 | The Lord has taken away the judgments against you; he has cleared away your enemies . The King of Israel , the Lord , is in your midst ; you shall never again f |
| Zep 3:16 | On that day it shall be said to Jerusalem : “ Fear not , O Zion ; let not your hands grow weak . |
| Hag 2:5 | according to the covenant that I made with you when you came out of Egypt . My Spirit remains in your midst . Fear not . |
| Zec 8:13 | And as you have been a byword of cursing among the nations , O house of Judah and house of Israel , so will I save you, and you shall be a blessing . Fear not , |
| Zec 8:15 | so again have I purposed in these days to bring good to Jerusalem and to the house of Judah ; fear not . |
| Zec 9:5 | Ashkelon shall see it, and be afraid ; Gaza too, and shall writhe in anguish ; Ekron also, because its hopes are confounded . The king shall perish from Gaza ;  |
| Mal 4:5 | “ Behold , I will send you Elijah the prophet before the great and awesome day of the Lord comes . |

## Notes for the L1→L2 gate

- **Morphology capture deferred to L2.** Since L1 assigns only single-sense (multi → L2), the per-verse stem (which *helps resolve* multi-sense) is an L2 input — captured there, not forced into L1. Flagged for your confirmation.
- **`sense_id` is coarse** (points to the term's parsed sense row, not a split sub-sense — the BDB tree is not yet split into stem-branch rows). Precise sub-sense pointing is a refinement.
- **Pole is term-level first-pass** (per-verse pole refines at L2); literal-physical vs metaphor is flagged (`pole_is_metaphor`) not auto-assigned (R6).
- **Next:** run the L1 audit, then the **L1→L2 gate** (researcher review).