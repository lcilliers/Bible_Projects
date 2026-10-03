# Life and death: strand observation ledger, unit 3 (v1)

**Date:** 2026-10-03 · **Author:** Claude Code · **Strand:** life and death, M25 (approved #1932) · **Unit:** 3, living before God · **Status:** **for researcher approval, #1940** (steps 1–4 of the working rhythm done; nothing woven yet) · Follows `life-death-strand-candidate-v2-20261002.md` §5 unit 3 and §7 (questions Q1–Q4), and the format of `life-death-observation-ledger-unit2-v1-20261002.md`.

**Threads this unit may bear on** (`../open-threads-register.md`, checked before the pull):
- **OT-01** (life by the statutes, and statutes without life): the "do this and live" verses fall in this unit (H2416E, G2198, G2222). **Main contact.**
- **OT-02** (Q1, What is death?): what life is set against; "alive" and yet dead
- **OT-03** (Q2, spirit and soul at death): "all live to him"; "the life of my spirit"; souls that "came to life"
- **OT-04** (Q3, the heart after death): checked; no verse
- **OT-05** (Q4, the body): "swallowed up by life"; "the life of Jesus … manifested in our bodies"
- **OT-08** (life and death over the inner being): every unit
- The linkage map's M02 row ("H0748 'slow / defer anger' not yet read") is read here (LD-134).

**Scope of unit 3**

| Strong | Gloss | Hits | Surfaces (ESV) |
| --- | --- | --- | --- |
| H2416A | alive, living | 240 | living · lives · live · alive · fresh · life · raw · living thing / creature · next year · spring · green · vigorous · peace |
| H2416E | life | 143 | life · live · lives · lived · lifetime · rival · life-giving · alive |
| G2198 | to live | 140 | live · living · alive · lives · lived · life · recovering · lifelong · come to life |
| G2222 | life | 133 | life · lifetime |
| H0748 | to be long, prolong | 34 | long · prolong(s) · continued · outlived · lengthen · patient · slow · defer · poles · stick out · grow long |

**690 hits in 629 verses**, all read, **grouped by surface**.

**Data**
- **The pull:** `life-death-unit3-living-before-god-pull-v1-20261003.csv`. One row per hit, with the full ESV text and a face. **Every hit has a face**, and no verse text is missing.
- **How it was built:** from iba.db (read-only) by `strand-unit-pull-v1-20261002.py` (the reusable unit-2 script, unchanged).
- **The faces as data:** `life-death-unit3-face-assign-v1-20261003.py`. Every verse is named by reading; there is **no fallback rule** in this unit. The script refuses to run if any hit is left without a face, or if any assignment matches no hit. Four hits are faced at hit level, where two hits in one verse read differently (Deu 6:2, Deu 32:47, 2Cor 13:4).

**Basis:** **S** = the verse states it · **R** = my reading, kept labelled ("I read").

**Disposition (proposed):** **W** weave where it touches · **RS** reshapes existing text · **NS** new structure needed · **H** held · **D** stays in data.

**Checks**
- **Surface alignment.** H2416A carries non-life senses ("fresh" water, "raw" flesh, "next year", "spring", "green", "vigorous", "peace" at 1Sa 25:6). H0748 carries "poles" (1Ki 8:8; 2Ch 5:9), "stick out your tongue" (Isa 57:4), long branches, cords and furrows. All are read and left in the data (L07).
- **"heart" in Joh 7:38 is not the heart word.** "Out of his heart will flow rivers of living water" is G2836 (*koilia*, "belly"), not G2588. It is quoted below as the ESV has it, but it is **not** counted as a heart verse.
- **Outside the Strong's list.** H2416C (mostly "beast") also carries "life" and "appetite" in 11 hits, several of them inner-being verses (Job 33:18–28; Isa 57:10). They are not in this pull. They are listed in LD-138 for the researcher to decide.
- **Quotes:** every quote is checked against iba.db `verse` (§G).
- **Already in the chapters:** 98 of the 629 verses are already quoted somewhere in the narrative (checked by text match, §E).

---

## A. The faces in unit 3 (change of character, #1919)

| Face | Hits / verses | What differs | Example verses |
| --- | --- | --- | --- |
| **L01. The oath by the LORD's life, or a person's** | 61 / 51 | "As the Lord lives"; "as your soul lives"; "as you yourself live"; "by the life of Pharaoh" | 1Sa 20:3; 2Ki 2:2; 2Sa 12:5; Jer 4:2; Jer 5:2 |
| **L02. God swears by his own life** | 24 / 24 | "As I live, declares the Lord God" (16 of the 24 in Ezekiel) | Eze 33:11; Num 14:21; Deu 32:40; Rom 14:11 |
| **L03. The living God** | 34 / 34 | Title, praise, against idols; "him who lives forever" | Jer 10:10; Psa 42:2; 1Th 1:9; Heb 3:12; Job 19:25 |
| **L05. Still alive; alive or dead** | 37 / 32 | Narrative: kin asked after, children, captives | Gen 45:26–28; 1Ki 3:22–27; 2Sa 12:18–22 |
| **L06. Living creatures** | 20 / 20 | Creation, flood, covenant, food laws | Gen 1:20–30; Gen 9:10–16; Lev 11:46 |
| **L07. Not the inner being** | 44 / 39 | Raw, fresh, spring, next year, the live bird and goat, poles | Lev 13–14; Lev 16:10; 1Ki 8:8 |
| **L08. Lifespan notices** | 24 / 23 | "the years of the life of"; "as long as he lived" | Gen 23:1; Gen 25:7; 2Ki 25:29–30 |
| **L09. Long life, days prolonged** | 26 / 26 | Joined to honouring, fearing, keeping; and its loss; the wicked who prolongs | Exo 20:12; Deu 6:2; Ecc 7:15; 8:12–13 |
| **L10. The days lived as the span of fearing and remembering** | 14 / 14 | "all the days that they live"; "all the days of your life" | Deu 4:9–10; Deu 16:3; Deu 17:19; Jos 24:31 |
| **L11. Life set before; choose life** | 6 / 5 | Deu 30; Jer 21:8 | Deu 30:6, 15, 19, 20 |
| **L12. Life from wisdom (Proverbs)** | 28 / 28 | Fountain, tree and path of life; the fear of the Lord; the tongue | Pro 4:23; 10:11; 13:12; 14:27; 15:4 |
| **L13. Life by doing** | 12 / 12 | "statutes of life"; "do this, and you will live"; "what shall I do to inherit eternal life?" | Eze 33:15; Luk 10:25–28; Gal 3:12; Rom 7:10 |
| **L14. Life weighed from within** | 34 / 28 | Loathed, bitter, in doubt, a breath, a mist; the living weighed | Job 10:1; Psa 88:3; Deu 28:66; Jam 4:14; Ecc 9:3–5 |
| **L15. Life valued** | 18 / 16 | Enjoyed as a portion; what life does not consist in; loving one's life | Ecc 9:9; Luk 12:15; 1Ti 6:19; Joh 12:25 |
| **L16. Life given, kept, redeemed by God** | 26 / 25 | Prayer and confession about one's own life | Job 10:12; Psa 63:3; Psa 103:4; Isa 38:16; Act 17:28 |
| **L17. As long as I live** | 8 / 7 | Praise and dwelling in his house for the length of a life | Psa 146:2; Psa 27:4; Isa 38:19–20 |
| **L18. The land, book and bundle of the living** | 22 / 22 | The world of the living, and being cut off from it | Psa 27:13; Psa 142:5; Psa 69:28; 1Sa 25:29; Eze 32 |
| **L19. Gone down alive** | 6 / 6 | Sheol (or the lake of fire) taking the living | Num 16:30, 33; Psa 55:15; Rev 19:20 |
| **L20. Living water** | 13 / 13 | Fountain, spring, river; thirst | Jer 2:13; Joh 4:10–14; Joh 7:38; Rev 22:17 |
| **L21. Eternal life** | 33 / 31 | Given, had now, promised, to come | Joh 3:16; Joh 17:3; 1Jo 5:11–13; Mar 10:30 |
| **L22. Christ the life; Christ alive** | 56 / 44 | Life in the Son; the bread of life; raised and alive | Joh 1:4; Joh 5:26; Joh 6:57; Joh 14:19; Heb 7:25 |
| **L23. Living to God** | 38 / 30 | Christ lives in me; dead to sin, alive to God; live by faith; "all live to him" | Gal 2:19–20; Rom 6:11; Rom 14:7–8; Luk 20:38 |
| **L24. Life and the Spirit** | 13 / 12 | The Spirit of life; living by the Spirit | Rom 8:2, 10, 13; Gal 5:25; 1Pe 4:6 |
| **L25. From death to life; alive yet dead** | 17 / 15 | Passed from death to life; a name for being alive | Joh 5:24–25; Rev 3:1; 1Ti 5:6; Eph 4:18 |
| **L26. Entering life; the tree, crown and book of life; the living and the dead judged** | 34 / 33 | What is entered, received, written, judged | Mat 7:14; Jam 1:12; Rev 2:7; Rev 20:12; Act 10:42 |
| **L27. The living word, hope, stones, way** | 11 / 11 | "living and active"; "a living hope" | Heb 4:12; 1Pe 1:3; 1Pe 2:5; Phili 2:16 |
| **L28. Long of anger, patience, delay** | 5 / 5 | H0748 with anger; "patient"; a proverb of delay | Pro 19:11; Isa 48:9; Job 6:11; Psa 30:5 |
| **L29. Life threatened or taken by people** | 9 / 9 | "he should not be allowed to live" | Act 22:22; Jer 11:19; Isa 53:8 |
| **L30. Healed or raised** | 9 / 9 | "your son will live" (unit 1 territory) | Joh 4:50–53; 1Ki 17:23; Act 9:41 |
| **L31. Bound by law while living** | 6 / 6 | Marriage law; a will | Rom 7:1–3; 1Cor 7:39; Heb 9:17 |
| **L32. Living as a manner of conduct** | 2 / 2 | "live like a Gentile"; "lived as a Pharisee" | Gal 2:14; Act 26:5 |

(L04 is not used. It was folded into L23 while reading.)

**Proportions.** L05–L08, L29 and L31–L32 hold 146 of the 690 hits. These are accounted for and stay in the data, except the inner-word verses drawn out in LD-135. The rest are read below.

---

## B. Observations (LD-92 onward)

### B.1 The oath of life (faces L01, L02)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-92 | **Swearing by the LORD's life and by the life of the one spoken to, as a bond.** David: "But truly, as the Lord lives and as your soul lives, there is but a step between me and death". Uriah: "As you live, and as your soul lives, I will not do this thing". Elisha, three times: "As the Lord lives, and as you yourself live, I will not leave you". The Shunammite says the same to Elisha. Ittai: "As the Lord lives, and as my lord the king lives, wherever my lord the king shall be, whether for death or for life, there also will your servant be" | 1Sa 20:3; 2Sa 11:11; 2Ki 2:2, 4, 6; 2Ki 4:30; 2Sa 15:21 | S | 10.10 (loyalty), 10.5, 2 | W |
| LD-93 | **The oath names what the LORD has done for the one who swears.** "As the Lord lives, who has redeemed my life out of every adversity"; "As the Lord lives, who has redeemed my soul out of every adversity"; "As the Lord lives, who made our souls"; "As the Lord, the God of Israel, lives, before whom I stand"; Job: "As God lives, who has taken away my right, and the Almighty, who has made my soul bitter" | 2Sa 4:9; 1Ki 1:29; Jer 38:16 (already in Ch 2); 1Ki 17:1 (18:15; 2Ki 3:14; 5:16); Job 27:2 | S | 10.9, 5 (soul), 10.1 (Job's bitterness) | W |
| LD-94 | **The same oath, said in anger, rashness, greed and secret.** "Then David's anger was greatly kindled against the man, and he said to Nathan, 'As the Lord lives, the man who has done this deserves to die'". Saul: "For as the Lord lives who saves Israel, though it be in Jonathan my son, he shall surely die", and the people's answering oath, "As the Lord lives, there shall not one hair of his head fall to the ground". Saul to the medium: "As the Lord lives, no punishment shall come upon you for this thing". Gehazi: "As the Lord lives, I will run after him and get something from him". "Then King Zedekiah swore secretly to Jeremiah" | 2Sa 12:5; 1Sa 14:39, 45; 1Sa 28:10; 2Ki 5:20; Jer 38:16 | S | 10.1 (anger), 10.6 (Gehazi), 10.5, **11 §4** | W |
| LD-95 | **The oath judged.** "Though they say, 'As the Lord lives,' yet they swear falsely"; "if you swear, 'As the Lord lives,' in truth, in justice, and in righteousness, then nations shall bless themselves in him"; "swear not, 'As the Lord lives'"; of oaths by other gods: "As your god lives, O Dan … they shall fall, and never rise again". To Judah in Egypt: "my name shall no more be invoked by the mouth of any man of Judah … saying, 'As the Lord God lives.'" Of the nations: "if they will diligently learn the ways of my people, to swear by my name, 'As the Lord lives,' … then they shall be built up". And the oath itself will change: no longer "As the Lord lives who brought up the people of Israel out of the land of Egypt," but "out of the north country" | Jer 5:2; Jer 4:2; Hos 4:15; Amo 8:14; Jer 44:26; Jer 12:16; Jer 16:14–15 (23:7–8) | S | 10.5 (speaking in truth), 10.9 | W |
| LD-96 | **God swears by his own life.** All 24 hits are God speaking. For life: "As I live, declares the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live". In judgement: "As I live, declares the Lord God, I will not be inquired of by you"; "I will deal with you according to the anger and envy that you showed because of your hatred against them". Of his glory: "as I live, and as all the earth shall be filled with the glory of the Lord"; "For I lift up my hand to heaven and swear, As I live forever". Paul cites it: "As I live, says the Lord, every knee shall bow to me, and every tongue shall confess to God" | Eze 33:11 (already in Ch 2); Eze 20:3, 31; Eze 35:11; Num 14:21; Deu 32:40; Rom 14:11 | S | 13, 2 "Life set before", 10.9 | W |

### B.2 The living God (face L03)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-97 | **The living God, named against idols and against mockery.** "But the Lord is the true God; he is the living God and the everlasting King. At his wrath the earth quakes"; "you turned to God from idols to serve the living and true God"; "turn from these vain things to a living God, who made the heaven and the earth"; Goliath "should defy the armies of the living God"; Sennacherib "has sent to mock the living God"; "you pervert the words of the living God" | Jer 10:10; 1Th 1:9; Act 14:15; 1Sa 17:26, 36; 2Ki 19:4, 16 (Isa 37:4, 17); Jer 23:36 | S | 10.9, 13 (Jer 10:10) | W |
| LD-98 | **The soul, the heart and the conscience turned toward the living God, or away.** "My soul thirsts for God, for the living God. When shall I come and appear before God?"; "My soul longs, yes, faints for the courts of the Lord; my heart and flesh sing for joy to the living God"; "lest there be in any of you an evil, unbelieving heart, leading you to fall away from the living God"; "It is a fearful thing to fall into the hands of the living God"; "purify our conscience from dead works to serve the living God"; "who is there of all flesh, that has heard the voice of the living God speaking out of the midst of fire as we have, and has still lived?"; "we have our hope set on the living God" | Psa 42:2; Psa 84:2 (already in Ch 5, 7); Heb 3:12; Heb 10:31; Heb 9:14 (already in Ch 8, 12, 14); Deu 5:26; 1Ti 4:10 | S | 10.6 (thirst, longing), 10.1 (fear, joy), 10.9, 4 (Heb 3:12) | W |
| LD-99 | **The living God among his people.** "Here is how you shall know that the living God is among you"; "we are the temple of the living God"; "written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts"; "Children of the living God"; "the church of the living God" | Jos 3:10; 2Cor 6:16 (in Ch 14); 2Cor 3:3 (in Ch 7, 14); Hos 1:10 (Rom 9:26); 1Ti 3:15 | S | 10.9, 14 | W (pointer) |
| LD-100 | **"The Lord lives", said as praise.** "The Lord lives, and blessed be my rock, and exalted be my God, the rock of my salvation"; "For I know that my Redeemer lives"; "worship him who lives forever and ever" | 2Sa 22:47 (Psa 18:46); Job 19:25 (in Ch 2); Rev 4:10 (4:9; 10:6; 15:7; Dan 12:7) | S | 10.9 | W |

### B.3 Long days, and the days of a life (faces L09, L10)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-101 | **Long days, joined to honouring, fearing and keeping.** "Honor your father and your mother, that your days may be long in the land"; "that you may fear the Lord your God … all the days of your life, and that your days may be long"; "A full and fair weight you shall have … that your days may be long"; "If you will walk in my ways … then I will lengthen your days"; of the king, "that his heart may not be lifted up above his brothers … so that he may continue long in his kingdom"; "he who hates unjust gain will prolong his days". "What man is there who desires life and loves many days, that he may see good?", which Peter cites as "Whoever desires to love life and see good days, let him keep his tongue from evil" | Exo 20:12 (Deu 5:16); Deu 6:2; Deu 25:15; 1Ki 3:14; Deu 17:20; Pro 28:16; Psa 34:12; 1Pe 3:10 | S | 2 "Life set before", 10.10 (honour), 10.6 (desire), 10.5 (tongue) | W |
| LD-102 | **Long days, seen otherwise.** "There is a righteous man who perishes in his righteousness, and there is a wicked man who prolongs his life in his evildoing"; "Though a sinner does evil a hundred times and prolongs his life, yet I know that it will be well with those who fear God"; "neither will he prolong his days like a shadow, because he does not fear before God"; "Yet God prolongs the life of the mighty by his power; they rise up when they despair of life". Of the servant: "he shall see his offspring; he shall prolong his days" | Ecc 7:15; Ecc 8:12, 13; Job 24:22; Isa 53:10 | S. Set **beside** LD-101; no reconciliation drawn | 2 "Life set before", 10.4 ("yet I know") | **RS** (side by side with LD-101, the way LD-46 and LD-47 stand in "After death") |
| LD-103 | **The days lived as the span of fearing, remembering and learning.** "so that they may learn to fear me all the days that they live on the earth, and that they may teach their children so"; "lest they depart from your heart all the days of your life"; "that all the days of your life you may remember the day when you came out of the land of Egypt"; the king "shall read in it all the days of his life, that he may learn to fear the Lord his God"; Israel served the Lord "all the days of the elders who outlived Joshua and had known all the work that the Lord did for Israel"; Hannah: "I will give him to the Lord all the days of his life" | Deu 4:10; Deu 4:9 (in Ch 11); Deu 16:3; Deu 17:19; Jos 24:31 (Judg 2:7); 1Sa 1:11 | S | 10.3 (remembering), 10.2 (learning), 10.9 | W |
| LD-104 | **A life summed.** Jacob: "Few and evil have been the days of the years of my life". Barzillai: "How many years have I still to live, that I should go up with the king to Jerusalem?" "David did what was right in the eyes of the Lord and did not turn aside from anything that he commanded him all the days of his life, except in the matter of Uriah the Hittite". "Absalom in his lifetime had taken and set up for himself the pillar … for he said, 'I have no son to keep my name in remembrance.'" | Gen 47:9; 2Sa 19:34; 1Ki 15:5; 2Sa 18:18 | S | 10.3 (Absalom), 10.4, 2 | W |

### B.4 Life set before, and life by doing (faces L11, L13): OT-01

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-105 | **God's work on the heart, in the chapter of the choice.** "And the Lord your God will circumcise your heart and the heart of your offspring, so that you will love the Lord your God with all your heart and with all your soul, that you may live". The same chapter sets "life and death" before the people, and says "choose life" and "he is your life and length of days" | Deu 30:6 (in Ch 3, 10.9, 14; **not** in Ch 2); Deu 30:15, 19, 20 (in Ch 2) | S (both are in Deu 30; the order is the chapter's own) | **2 "Life set before"** | RS (add 30:6 to Ch 2) |
| LD-106 | **Life by doing, and the counter-statements.** "walks in the statutes of life, not doing injustice, he shall surely live"; "My covenant with him was one of life and peace … It was a covenant of fear, and he feared me"; "For it is no empty word for you, but your very life". The lawyer: "Teacher, what shall I do to inherit eternal life?" Jesus: "You have answered correctly; do this, and you will live". "If you would enter life, keep the commandments". Against these: "Now it is evident that no one is justified before God by the law, for 'The righteous shall live by faith.' But the law is not of faith, rather 'The one who does them shall live by them'"; "Moses writes about the righteousness that is based on the law, that the person who does the commandments shall live by them"; "The very commandment that promised life proved to be death to me" | Eze 33:15; Mal 2:5; Deu 32:47; Luk 10:25, 28; Mat 19:17; Gal 3:11–12; Rom 10:5; Rom 7:10 (in Ch 2) | S. **Held, unreconciled**, with OT-01 (Eze 20:11, 25; Gal 3:21) | 2 "Life set before" (Lev 18:5 is already there), 10.8, 12 | **H** (to OT-01) |
| LD-107 | **Fed by the word.** "Man shall not live by bread alone, but by every word that comes from the mouth of God" | Mat 4:4 (Luk 4:4) | S. Deu 8:3 is already in Ch 2 "Where life flows from" | 2 | D (pointer only) |

### B.5 Life from wisdom (face L12)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-108 | **What Proverbs calls a fountain, tree or path of life.** "The mouth of the righteous is a fountain of life"; "The teaching of the wise is a fountain of life, that one may turn away from the snares of death"; "The fear of the Lord is a fountain of life"; "Good sense is a fountain of life to him who has it"; wisdom "is a tree of life to those who lay hold of her"; "The fruit of the righteous is a tree of life"; "Whoever heeds instruction is on the path to life"; "the reproofs of discipline are the way of life"; "The path of life leads upward for the prudent, that he may turn away from Sheol beneath"; "The fear of the Lord leads to life, and whoever has it rests satisfied"; "For whoever finds me finds life and obtains favor from the Lord" | Pro 10:11; 13:14; 14:27; 16:22; 3:18; 11:30; 10:17; 6:23; 15:24; 19:23; 8:35 | S | 10.5 (mouth), 10.2 (instruction), 10.9 (fear of the Lord) | W |
| LD-109 | **Life from within reaching the body, and the reverse.** "Hope deferred makes the heart sick, but a desire fulfilled is a tree of life"; "A gentle tongue is a tree of life, but perverseness in it breaks the spirit"; "and they will be life for your soul and adornment for your neck"; "For they are life to those who find them, and healing to all their flesh". With "A tranquil heart gives life to the flesh, but envy makes the bones rot", already in Ch 2 | Pro 13:12; 15:4; 3:22; 4:22; 14:30 | S | **2 "Where life flows from"**, 4, 6 (Pro 15:4), 10.6 (desire), 10.1 | W |
| LD-110 | **Life missed by not attending.** Of the forbidden woman: "she does not ponder the path of life; her ways wander, and she does not know it"; "none who go to her come back, nor do they regain the paths of life". "The ear that listens to life-giving reproof will dwell among the wise" | Pro 5:6; 2:19; 15:31 | S | 10.4 (pondering), 10.2 (the ear) | W |

### B.6 Life weighed from within (face L14)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-111 | **Life loathed.** "I loathe my life; I will give free utterance to my complaint; I will speak in the bitterness of my soul"; "I am blameless; I regard not myself; I loathe my life"; Rebekah: "I loathe my life because of the Hittite women … what good will my life be to me?"; "So I hated life, because what is done under the sun was grievous to me"; "Why is light given to him who is in misery, and life to the bitter in soul" | Job 10:1; Job 9:21; Gen 27:46; Ecc 2:17 (in 10.6); Job 3:20 | S | **2** (beside "Wanting to die"), 10.1, 5 (soul) | **NS or RS** (see §F, decision 2) |
| LD-112 | **Life worn down and near its end.** "For my life is spent with sorrow, and my years with sighing; my strength fails because of my iniquity"; "For my soul is full of troubles, and my life draws near to Sheol"; "Your life shall hang in doubt before you. Night and day you shall be in dread and have no assurance of your life"; "For we were so utterly burdened beyond our strength that we despaired of life itself"; "and made their lives bitter with hard service"; "because of his iniquity, none can maintain his life" | Psa 31:10; Psa 88:3; Deu 28:66; 2Cor 1:8; Exo 1:14; Eze 7:13 | S | 2 "Facing death", 10.1, 13 (Deu 28:66) | W |
| LD-113 | **Life named as brief.** "Remember that my life is a breath; my eye will never again see good"; "like a weaver I have rolled up my life; he cuts me off from the loom"; "What is your life? For you are a mist that appears for a little time and then vanishes. Instead you ought to say, 'If the Lord wills, we will live and do this or that.'" "For who knows what is good for man while he lives the few days of his vain life, which he passes like a shadow?" | Job 7:7; Isa 38:12; Jam 4:14–15; Ecc 6:12 | S | **2 "Breath lent"**, 10.7 (planning), 10.4 | W |
| LD-114 | **The living weighed.** "For the living know that they will die" (in Ch 2); "he who is joined with all the living has hope"; at the house of mourning, "the living will lay it to heart"; "the hearts of the children of man are full of evil, and madness is in their hearts while they live"; "Why should a living man complain, a man, about the punishment of his sins?"; "for no one living is righteous before you" | Ecc 9:5; 9:4; 7:2; 9:3; Lam 3:39; Psa 143:2 | S | 2 "What death is", 4 (Ecc 9:3), 10.1, 12 | W |

### B.7 Life valued (face L15)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-115 | **Life enjoyed, as given.** "Enjoy life with the wife whom you love, all the days of your vain life that he has given you under the sun, because that is your portion in life"; "to eat and drink and find enjoyment in all the toil … the few days of his life that God has given him, for this is his lot"; "For he will not much remember the days of his life because God keeps him occupied with joy in his heart"; "there is nothing better for them than to be joyful and to do good as long as they live" | Ecc 9:9; 5:18; 5:20; 3:12 | S | 10.1 (joy), 10.3 (5:20), 10.10 (Ecc 9:9) | W |
| LD-116 | **What life does not consist in.** "for one's life does not consist in the abundance of his possessions"; "men of the world whose portion is in this life"; "For though, while he lives, he counts himself blessed"; Abraham: "remember that you in your lifetime received your good things, and Lazarus in like manner bad things"; "so that they may take hold of that which is truly life"; "If in Christ we have hope in this life only, we are of all people most to be pitied"; "Whoever loves his life loses it, and whoever hates his life in this world will keep it for eternal life" | Luk 12:15; Psa 17:14; Psa 49:18; Luk 16:25; 1Ti 6:19; 1Cor 15:19; Joh 12:25 (in Ch 5) | S | 10.6 (covetousness), 10.3 (Luk 16:25 "remember"), 2 | W |

### B.8 Life given and kept by God; praise for as long as I live (faces L16, L17)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-117 | **One's own life spoken of to God.** "You have granted me life and steadfast love, and your care has preserved my spirit"; "Because your steadfast love is better than life, my lips will praise you"; "a prayer to the God of my life"; "who redeems your life from the pit"; "You have taken up my cause, O Lord; you have redeemed my life"; "Yet you brought up my life from the pit, O Lord my God"; "He asked life of you; you gave it to him"; "O Lord, by these things men live, and in all these is the life of my spirit"; "The Lord is the stronghold of my life; of whom shall I be afraid?"; "preserve my life from dread of the enemy"; "who has kept our soul among the living"; "You open your hand; you satisfy the desire of every living thing" | Job 10:12; Psa 63:3; Psa 42:8; Psa 103:4; Lam 3:58; Jon 2:6; Psa 21:4; Isa 38:16 (in Ch 2); Psa 27:1 (in 10.9); Psa 64:1; Psa 66:9; Psa 145:16 | S | **2 "Life asked for"**, "Delivered from death", 10.9, 10.1, 10.6 (Psa 145:16), 6 (Job 10:12; Isa 38:16) | W |
| LD-118 | **For as long as I live.** "I will praise the Lord as long as I live"; "So I will bless you as long as I live"; "I will sing to the Lord as long as I live"; "The living, the living, he thanks you, as I do this day" (the verse after "For Sheol does not thank you", Isa 38:18); "One thing have I asked of the Lord … that I may dwell in the house of the Lord all the days of my life"; "Surely goodness and mercy shall follow me all the days of my life" | Psa 146:2; Psa 63:4; Psa 104:33; Isa 38:19 (38:18); Psa 27:4; Psa 23:6 | S | 10.9, 10.6 (Psa 27:4), 2 "After death" (Isa 38:18–19 stand together in one song) | W |

### B.9 The land, book and bundle of the living; gone down alive (faces L18, L19)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-119 | **"The land of the living" and the records of the living.** "I believe that I shall look upon the goodness of the Lord in the land of the living!"; "You are my refuge, my portion in the land of the living"; "I shall not see the Lord, the Lord in the land of the living"; "who considered that he was cut off out of the land of the living"; "he will uproot you from the land of the living"; the nations "who spread terror in the land of the living". Abigail: "the life of my lord shall be bound in the bundle of the living in the care of the Lord your God". "Let them be blotted out of the book of the living; let them not be enrolled among the righteous"; "everyone who has been recorded for life in Jerusalem" | Psa 27:13 (in Ch 2); Psa 142:5; Isa 38:11; Isa 53:8 (Jer 11:19); Psa 52:5; Eze 32:23 (32:24–32); 1Sa 25:29; Psa 69:28; Isa 4:3 | S | 2, 10.9, 13 (Eze 32) | W |
| LD-120 | **Gone down alive.** "and they go down alive into Sheol, then you shall know that these men have despised the Lord"; "Let death steal over them; let them go down to Sheol alive; for evil is in their dwelling place and in their heart"; "like Sheol let us swallow them alive" (the sinners' words); "These two were thrown alive into the lake of fire" | Num 16:30 (16:33); Psa 55:15; Pro 1:12 (in 10.9); Rev 19:20 | S | 13, 4 (Psa 55:15) | W (pointer) |

### B.10 Living water (face L20)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-121 | **Living water, forsaken and given.** "for my people have committed two evils: they have forsaken me, the fountain of living waters, and hewed out cisterns for themselves, broken cisterns that can hold no water"; "If you knew the gift of God … he would have given you living water"; "The water that I will give him will become in him a spring of water welling up to eternal life"; "Whoever believes in me, as the Scripture has said, 'Out of his heart will flow rivers of living water'"; "let the one who is thirsty come; let the one who desires take the water of life without price"; "he will guide them to springs of living water, and God will wipe away every tear from their eyes" | Jer 2:13 (17:13); Joh 4:10, 14; Joh 7:38; Rev 22:17 (21:6); Rev 7:17 | S. In Joh 7:38 "heart" is *koilia* (G2836), not the heart word (Checks) | **2 "Where life flows from"**, 10.6 (thirst, desire), 10.1 (Rev 7:17 tears) | W |

### B.11 Eternal life, and Christ the life (faces L21, L22)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-122 | **Eternal life, had now and to come.** "Truly, truly, I say to you, whoever believes has eternal life"; "I write these things to you who believe in the name of the Son of God, that you may know that you have eternal life"; "God gave us eternal life, and this life is in his Son. Whoever has the Son has life"; "in hope of eternal life, which God, who never lies, promised before the ages began"; "and in the age to come eternal life"; "Take hold of the eternal life to which you were called"; "but the righteous into eternal life" | Joh 6:47; 1Jo 5:13; 1Jo 5:11–12; Tit 1:2; Mar 10:30 (Luk 18:30); 1Ti 6:12; Mat 25:46 | S. Both tenses stated; no reconciliation drawn | **2 "Made alive"**, 14 | W |
| LD-123 | **Life in the Son.** "In him was life, and the life was the light of men"; "For as the Father has life in himself, so he has granted the Son also to have life in himself"; "As the living Father sent me, and I live because of the Father, so whoever feeds on me, he also will live because of me"; "I came that they may have life and have it abundantly"; "Because I live, you also will live"; "you killed the Author of life"; "by the power of an indestructible life"; "he always lives to make intercession for them" | Joh 1:4; Joh 5:26; Joh 6:57; Joh 10:10; Joh 14:19; Act 3:15; Heb 7:16; Heb 7:25 | S | **2 "Where life flows from"** (Col 3:4 and Joh 11:25 are already there), 10.9, 14 | W |
| LD-124 | **Life looked for in the wrong place, or refused.** "You search the Scriptures because you think that in them you have eternal life; and it is they that bear witness about me, yet you refuse to come to me that you may have life"; "Since you thrust it aside and judge yourselves unworthy of eternal life"; "Do not work for the food that perishes, but for the food that endures to eternal life" | Joh 5:39–40; Act 13:46; Joh 6:27 | S | 10.4 ("you think"), 10.7, 10.6 | W |

### B.12 Living to God, and life with the Spirit (faces L23, L24)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-125 | **Who lives in the one who lives.** "I have been crucified with Christ. It is no longer I who live, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God"; "For through the law I died to the law, so that I might live to God"; "consider yourselves dead to sin and alive to God in Christ Jesus"; "that we might die to sin and live to righteousness"; "present your bodies as a living sacrifice"; "to live self-controlled, upright, and godly lives in the present age"; "all who desire to live a godly life in Christ Jesus will be persecuted" | Gal 2:20 (in Ch 7); Gal 2:19 (in Ch 14); Rom 6:11 (in Ch 14); 1Pe 2:24; Rom 12:1; Tit 2:12; 2Ti 3:12 | S | **2 "Made alive"** (short), 14, 3 (Gal 2:20, "I"), 10.7 | W |
| LD-126 | **"All live to him."** "Now he is not God of the dead, but of the living, for all live to him"; "who died for us so that whether we are awake or asleep we might live with him" | Luk 20:38 (Mat 22:32; Mar 12:27); 1Th 5:10 | S (said of the patriarchs, in a dispute about the resurrection, Luk 20:37) | **2 "After death"**, **Q2** | W (in the "with God" list, no reconciliation added) |
| LD-127 | **Life and the Spirit.** "For the law of the Spirit of life has set you free in Christ Jesus from the law of sin and death"; "although the body is dead because of sin, the Spirit is life because of righteousness"; "If we live by the Spirit, let us also keep in step with the Spirit"; "the one who sows to the Spirit will from the Spirit reap eternal life"; "Shall we not much more be subject to the Father of spirits and live?"; "that though judged in the flesh the way people are, they might live in the spirit the way God does" | Rom 8:2; Rom 8:10; Gal 5:25; Gal 6:8; Heb 12:9; 1Pe 4:6 | S | 6 (spirit), 7 (flesh), 14, **Q2** (1Pe 4:6) | W |

### B.13 From death to life, and alive yet dead (face L25)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-128 | **Alive in name, dead in fact.** "You have the reputation of being alive, but you are dead"; "but she who is self-indulgent is dead even while she lives"; "They are darkened in their understanding, alienated from the life of God because of the ignorance that is in them, due to their hardness of heart"; "for this your brother was dead, and is alive; he was lost, and is found"; "you know that no murderer has eternal life abiding in him"; "to one a fragrance from death to death, to the other a fragrance from life to life" | Rev 3:1; 1Ti 5:6; Eph 4:18; Luk 15:32 (in 10.10); 1Jo 3:15; 2Cor 2:16 | S | **2 › Death in the living**, 4 (Eph 4:18), 10.4 (Eph 4:18), 12 | RS (adds to the bullets) |
| LD-129 | **Life granted with repentance.** "Then to the Gentiles also God has granted repentance that leads to life"; "what will their acceptance mean but life from the dead?" | Act 11:18; Rom 11:15 | S | 14 | W |

### B.14 Entering life; the tree and the books (face L26)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-130 | **What it takes to enter life, and what is received.** "It is better for you to enter life crippled or lame than with two hands or two feet to be thrown into the eternal fire"; "For the gate is narrow and the way is hard that leads to life, and those who find it are few"; "Do not fear what you are about to suffer … Be faithful unto death, and I will give you the crown of life"; "Blessed is the man who remains steadfast under trial, for when he has stood the test he will receive the crown of life, which God has promised to those who love him" | Mat 18:8 (Mar 9:43, 45); Mat 7:14; Rev 2:10; Jam 1:12 | S | 10.7, 10.1 (Rev 2:10) | W |
| LD-131 | **The tree of life.** "The tree of life was in the midst of the garden"; "lest he reach out his hand and take also of the tree of life and eat, and live forever"; "to guard the way to the tree of life"; "To the one who conquers I will grant to eat of the tree of life, which is in the paradise of God"; "The leaves of the tree were for the healing of the nations"; "Blessed are those who wash their robes, so that they may have the right to the tree of life" | Gen 2:9; Gen 3:22 (in Ch 2); Gen 3:24; Rev 2:7; Rev 22:2, 14 | S | 2 "Life breathed in", 14 | W |
| LD-132 | **The book of life, and the living and the dead judged.** "And the dead were judged by what was written in the books, according to what they had done"; "And if anyone's name was not found written in the book of life, he was thrown into the lake of fire"; "I will never blot his name out of the book of life"; Christ "is to judge the living and the dead"; "For to this end Christ died and lived again, that he might be Lord both of the dead and of the living"; "I saw the souls of those who had been beheaded … They came to life and reigned with Christ for a thousand years"; "The rest of the dead did not come to life until the thousand years were ended" | Rev 20:12, 15; Rev 3:5; 2Ti 4:1 (Act 10:42; 1Pe 4:5); Rom 14:9; Rev 20:4–5 | S | **2 "Life, and judgment"**, **Q2** (Rev 20:4) | W |

### B.15 The living word and a living hope (face L27)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-133 | **What is called living.** "For the word of God is living and active … discerning the thoughts and intentions of the heart"; "he has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead"; "you yourselves like living stones are being built up as a spiritual house"; "He received living oracles to give to us"; "holding fast to the word of life"; "His divine power has granted to us all things that pertain to life and godliness"; husbands and wives "are heirs with you of the grace of life, so that your prayers may not be hindered" | Heb 4:12 (in Ch 9, 10.8); 1Pe 1:3 (in Ch 2, 14); 1Pe 2:5; Act 7:38; Phili 2:16; 2Pe 1:3; 1Pe 3:7 | S | 10.6 (hope), 10.10 (1Pe 3:7), 10.9 | W |

### B.16 Long of anger (face L28): the M02 link

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-134 | **Anger made long.** "Good sense makes one slow to anger, and it is his glory to overlook an offense"; "For my name's sake I defer my anger; for the sake of my praise I restrain it for you, that I may not cut you off"; "For his anger is but for a moment, and his favor is for a lifetime". Job: "What is my strength, that I should wait? And what is my end, that I should be patient?" H0748 (*to be long*) stands with "anger" in only two hits (Pro 19:11; Isa 48:9) | Pro 19:11; Isa 48:9 (in Ch 13); Psa 30:5 (in Ch 13); Job 6:11 | S | **10.1 (anger)**, 10.10 (overlooking), 13; linkage map M02 row (now read) | W |

### B.17 Inner words in the narrative "alive" verses (face L05), and the rest

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-135 | **Narrative "alive", where an inner word is in the verse.** "Joseph is still alive … And his heart became numb, for he did not believe them" (in Ch 2), then "It is enough; Joseph my son is still alive. I will go and see him before I die"; "Then the woman whose son was alive said to the king, because her heart yearned for her son"; Joab to David: "today I know that if Absalom were alive and all of us were dead today, then you would be pleased"; "Saul and Jonathan, beloved and lovely! In life and in death they were not divided"; Jonathan: "If I am still alive, show me the steadfast love of the Lord, that I may not die"; Moses: "even today while I am yet alive with you, you have been rebellious against the Lord" | Gen 45:26, 28; 1Ki 3:26; 2Sa 19:6; 2Sa 1:23; 1Sa 20:14; Deu 31:27 | S | 10.1, 10.10, 4 (1Ki 3:26) | W |
| LD-136 | **Healed or raised: unit 1 territory.** "Jesus said to him, 'Go; your son will live.' The man believed the word that Jesus spoke to him"; "See, your son lives"; "And they took the youth away alive, and were not a little comforted" | Joh 4:50; 1Ki 17:23; Act 20:12; Rev 11:11 (in Ch 2) | S | 2 "Life that returns" | D (pointer to unit 1) |
| LD-137 | **Life taken by people.** "he should not be allowed to live"; "Justice has not allowed him to live" (the islanders' reading) | Act 22:22 (25:24); Act 28:4 | S | — | D |

### B.18 Outside the pull: for the researcher

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| LD-138 | **H2416C in its "life" sense** (not in the unit's Strong's list; H2416C is mostly "beast"). "so that his life loathes bread, and his appetite the choicest food"; "His soul draws near the pit, and his life to those who bring death"; "he keeps back his soul from the pit, his life from perishing by the sword"; "He has redeemed my soul from going down into the pit, and my life shall look upon the light"; "You were wearied with the length of your way, but you did not say, 'It is hopeless'; you found new life for your strength, and so you were not faint". Also H2416D: "do not forget the life of your poor forever" | Job 33:20, 22, 18, 28; Isa 57:10; Psa 74:19 (and Psa 143:3, already LD-58; Psa 78:50; Job 36:14) | S | 2 "Delivered from death", 10.1, 5 (soul) | **decision** (§F, decision 4) |

---

## C. Change of character: what differs between the faces (#1919, for Ch 11 §4)

- **"As the LORD lives."** The same oath carries loyalty (Elisha, Ittai, Uriah), anger (David, 2Sa 12:5), a rash vow that the people overturn (Saul, 1Sa 14:39, 45), greed (Gehazi), an oath to a medium (Saul) and a secret promise (Zedekiah). The words do not change; the one swearing and what is sworn to do does. The verses give their own measure: "in truth, in justice, and in righteousness" (Jer 4:2), against "yet they swear falsely" (Jer 5:2).
- **"Long."** Days made long are joined to honouring and keeping (LD-101). Beside that stand the wicked who prolong their life (LD-102). With anger, the same word is patience, and "his glory" (Pro 19:11). In a proverb, "The days grow long, and every vision comes to nothing" (Eze 12:22), it is a saying of disbelief.
- **"Life."** It is a span ("the days of the years of my life"), a thing felt ("I loathe my life"), a thing given ("You have granted me life"), a thing to come ("in the age to come eternal life") and a person ("I am … the life"). What differs is who gives or holds it, and what it is set against.
- **"Alive."** A fact in a narrative ("Is your father still alive?"); a reputation that is false ("You have the reputation of being alive, but you are dead"); a standing toward God ("alive to God in Christ Jesus"); a state before the law came ("I was once alive apart from the law", Rom 7:9).
- **"Living."** Each verse states what "living" is set against: idols (1Th 1:9), broken cisterns (Jer 2:13), dead works (Heb 9:14), the dead (Luk 20:38). Quoted, not drawn together.

---

## D. The researcher's questions: what unit 3 shows

| Q | What the verses say | Ledger |
|---|---|---|
| **Q1 What is death?** | It is stated from the life side: "For the living know that they will die" (Ecc 9:5). A person can be called dead while alive: "dead even while she lives" (1Ti 5:6), "alienated from the life of God" (Eph 4:18). | LD-114, LD-128 |
| **Q2 Spirit and soul at death** | "for all live to him" (Luk 20:38); "that … they might live in the spirit the way God does" (1Pe 4:6); "I saw the souls of those who had been beheaded … They came to life" (Rev 20:4); while living, "in all these is the life of my spirit" (Isa 38:16). These are set beside the unit 2 verses, unreconciled. **The focused pull is still needed.** | LD-126, LD-127, LD-132, LD-117 |
| **Q3 The heart after death** | **No verse in this unit.** The heart while living: "madness is in their hearts while they live" (Ecc 9:3); "an evil, unbelieving heart" (Heb 3:12). Joh 7:38 is *koilia*, not the heart word. | LD-114, LD-98 |
| **Q4 The body** | "so that what is mortal may be swallowed up by life" (2Cor 5:4, already in Ch 2); "so that the life of Jesus also may be manifested in our bodies" (2Cor 4:10, already in Ch 2); "present your bodies as a living sacrifice" (Rom 12:1); "although the body is dead because of sin, the Spirit is life because of righteousness" (Rom 8:10). | LD-125, LD-127 |
| **OT-08 What life is set against** | Death (Deu 30:15, 19); idols (1Th 1:9; Act 14:15); broken cisterns (Jer 2:13); the abundance of possessions (Luk 12:15); "this life only" (1Cor 15:19); the law as the way to it (Gal 3:12, held). Each pairing is the verse's own. | §C |

---

## E. Already in the chapters (pointer only)

98 of the 629 verses are already quoted in the narrative (text-match check). Most are in **Ch 2** (65), and the others are spread across Ch 3, 5–9, 10.1, 10.5–10.11, 11, 12, 13 and 14. These are not woven again. Where this ledger cites one, it is marked "(in Ch …)". Examples: Pro 4:23; Deu 30:15, 19, 20; Joh 11:25; Joh 17:3; Gal 2:20 (Ch 7); Psa 84:2 (Ch 5, 7); Heb 9:14 (Ch 8, 12, 14); Isa 48:9 and Psa 30:5 (Ch 13).

---

## F. Proposed weave (after approval)

**Ch 2 (main):**
- **NS "Living before God"**, placed after "Life set before a person" and before "Life asked for". The opening of Ch 2 says life is "lived before him", and no section says it yet. Content:
  - the oath "As the Lord lives" and God's own "As I live", with how the oath is judged (LD-92 to LD-96)
  - the living God, set against idols and toward the soul's thirst (LD-97, LD-98, LD-100)
  - the days of a life as the span of fearing, remembering and praising (LD-103, LD-118)
  - the land of the living (LD-119)
- **"Life set before a person"**: **RS**. Add Deu 30:6 (LD-105). Add long days (LD-101) and, beside them, LD-102, unreconciled. LD-106 is **held** in OT-01.
- **"Where life flows from"**: add Pro 13:12 and 15:4 (LD-109), living water (LD-121), life in the Son (LD-123), short.
- **"Breath lent, and held by God"**: add LD-113 (a breath, a mist, "If the Lord wills").
- **Life weighed** (LD-111, LD-112, LD-114, LD-115, LD-116): see decision 2.
- **"What death is" › *Death in the living***: add Rev 3:1, 1Ti 5:6 and Eph 4:18 (LD-128).
- **"Made alive"**: add LD-122 (eternal life, now and to come) and LD-125 (Gal 2:19; 1Pe 2:24; Rom 12:1), short, pointing to Ch 14.
- **"After death"**: add Luk 20:38 and 1Th 5:10 to the "with God" list (LD-126), with no reconciliation drawn.
- **"Life, and judgment"**: add LD-132. **"Life breathed in"**: Gen 2:9 and 3:24 beside 3:22 (LD-131), short.

**Elsewhere:**
- **10.1 Feeling:** LD-111, LD-112 (loathing, dread); LD-134 (Pro 19:11, in "Anger"); LD-98 (Heb 10:31); LD-135 (1Ki 3:26); LD-115 (joy)
- **10.2:** LD-103 (learning to fear), LD-110 (the ear)
- **10.3:** LD-103 (remember all the days); LD-104 (Absalom's pillar); LD-115 (Ecc 5:20); LD-116 (Luk 16:25)
- **10.4:** LD-110 ("she does not ponder"); LD-124 ("you think"); LD-102 ("yet I know")
- **10.5:** LD-92 to LD-95 (the oath as speech: true, false, rash); LD-101 (1Pe 3:10); LD-108 (the mouth a fountain of life)
- **10.6:** LD-98 (the soul's thirst for the living God); LD-109 (desire fulfilled); LD-116 (covetousness); LD-121 (thirst); LD-94 (Gehazi)
- **10.7:** LD-113 (Jam 4:15); LD-124; LD-130
- **10.9:** LD-93, LD-96 to LD-100, LD-117, LD-118
- **10.10:** LD-92 (oaths of loyalty); LD-101 (honour); LD-134 (overlooking an offense); LD-135
- **11 §4:** §C
- **12:** LD-114 (Ecc 9:3; Psa 143:2); LD-128
- **13:** LD-96 (God's oath in judgement); LD-112 (Deu 28:66); LD-120; LD-134 (pointer)
- **14:** LD-122, LD-125, LD-127, LD-129
- **Ch 4 / 6 (pointers):** Heb 3:12 and Eph 4:18 (heart); Isa 38:16 and Job 10:12 (spirit)

**Held:** LD-106 (to OT-01). **Data:** LD-107, LD-136, LD-137; faces L05 (except LD-135), L06, L07, L08, L29, L31, L32.

**Decisions for the researcher:**
1. **NS "Living before God" in Ch 2.** Is it a new section in Ch 2 (as proposed), or should the oath material sit in 10.5 and 10.9 only, with Ch 2 carrying only the living God and the land of the living?
2. **Life weighed.** Either a short **new section** in Ch 2, placed before "Facing death" (life loathed, worn down, enjoyed, and what it does not consist in), or **fold** LD-111 and LD-112 into "Wanting to die" and LD-115 and LD-116 into "Where life flows from". I recommend the new section. "Wanting to die" is about death wished for; these verses weigh life itself, and several of them do not wish for death (Ecc 9:9; Luk 12:15).
3. **LD-101 and LD-102 side by side** in "Life set before", unreconciled (as LD-46 and LD-47). The other choice is to hold LD-102 in the register.
4. **LD-138 (H2416C "life", 11 hits).** Read them into a short supplement to this ledger and weave them with LD-111/LD-117, or leave them for a later pull. I recommend the supplement. Job 33:18–28 bears directly on "Delivered from death".

**Register at approval:**
- OT-01: touched (LD-106, held; Gal 3:11–12, Rom 10:5, Luk 10:28, Rom 7:10)
- OT-02: touched (LD-114, LD-128)
- OT-03: touched (LD-117 Isa 38:16; LD-126; LD-127 1Pe 4:6; LD-132 Rev 20:4)
- OT-04: touched (no answer; Joh 7:38 is *koilia*)
- OT-05: touched (LD-125 Rom 12:1; LD-127 Rom 8:10)
- OT-08: touched (§D)
- Linkage map: M02 row, H0748 now read (LD-134)
- No new thread, unless LD-102 or LD-138 is held.

## G. Quote check

Run: `../fear/fear-quote-check-v1-20261001.py life-death-observation-ledger-unit3-v1-20261003.md`. Result 2026-10-03: **284 quotes checked in table rows; 0 failures.** (A first run flagged two of my own labels, which were written in quotation marks: "Do this and live" and *to be long*. They were reworded. Neither is a verse quote.)
