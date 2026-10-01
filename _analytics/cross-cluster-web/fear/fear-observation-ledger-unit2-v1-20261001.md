# Fear: strand observation ledger, unit 2 (v1)

**Date:** 2026-10-01 · **Author:** Claude Code · **Strand:** fear (approved #1927) · **Unit:** 2 · **Status:** approved and woven (#1929). Follows `fear-observation-ledger-v1-20261001.md` (unit 1, FE-01 to FE-46, woven #1928). Scope is from `fear-strand-handoff-v1-20261001.md`.

**Scope of unit 2:** *paḥad*, "dread", and the trembling and shuddering words.

| Strong | Gloss | Hits | Surfaces (ESV) |
| --- | --- | --- | --- |
| H6343 | dread | 49 | fear · terror · dread · great [terror] · thing · panic · Dreadful |
| H6342 | to dread | 24 | fear · afraid · dread · terror · terrified · thrill · awe · shake · feel · come trembling |
| H6345 | dread | 1 | fear |
| H2729 | to tremble | 39 | tremble · trembling · afraid · make them afraid · panic · terrify · frighten away · startled · disturb · taken [trouble] · come trembling |
| H2730 | trembling | 6 | tremble · trembled · trembles · trembling |
| H2731 | trembling | 9 | panic · trembling · fear · trouble · [trembled very violently] |
| H7264 | to tremble | 41 | tremble · quaked · disturbed · raging · raged · rages · enraged · angry · provoke · quarrel · deeply moved · stirred up · roused · shaken · unrest · shudder · turn |
| H6206 | to tremble | 15 | dread · terrify · frighten · fear · feared · awe · inspire terror · strike terror |
| H2342A | to twist: tremble | 11 | tremble · shakes · anguish · distressed · wrung |
| H7460 · H7461A/B · H2111 · H2112 · H2113 · H7268 · H7269 · H7578 · H7322 · H6426 · H6427 · H8175A · H8178A | tremble · trembling · quivering · shudder · shuddering | 31 | trembling · tremble · horror · bristle · shocked · shuddering · sheer terror |
| H4172A | fear | 1 (Isa 8:13 only) | fear |

**227 hits in 196 verses**, read **grouped by surface**.

**Scope decisions (mine, for the researcher to confirm):**
- The handoff's "other shudder/tremble entries" is taken as every **Hebrew** M01 entry whose gloss is tremble, trembling, quivering, shudder or shuddering. That adds **H6206** (15 hits; Isa 8:13 is one of them), H6426, H6427, H7268, H7269, H7322, H7578, H8175A and H8178A.
- **Greek trembling** (G5156, G5141, G1790) is left to unit 4, with the *phobos* group.
- **Terror and horror roots** (H0367, H4288, H8047, H1091, H2851, H4032 …) are left to unit 3. Where they share a verse with a unit 2 word, only the unit 2 word is read here.

**Data:** `fear-unit2-pahad-trembling-pull-v1-20261001.csv`
- Built afresh from iba.db (read-only), not filtered from the web pull, so no hit is lost to a verse with no other-cluster word.
- One row per hit: reference · position · strong · surface · negated flag · divine-near flag · full ESV verse text · **face**.
- **Every hit has a face.** No verse text is missing.

**Basis:** **S** = the verse states it · **R** = my reading, kept labelled.

**Disposition (proposed; nothing is woven until the researcher approves):** **W** woven where it touches · **RS** reshapes existing text · **NS** new structure needed · **H** held.

**Checks**
- **Quotes:** every quote below was checked mechanically against the ESV text in iba.db `verse` (checker rebuilt this unit, see §F).
- **Surface alignment is not always exact.** In a few verses STEP sets the surface on the neighbouring English word:
  - Mic 7:17 gives H7264 "turn" and H6342 "come trembling"
  - Gen 27:33 gives H2731 "said"
  - Psa 14:5 and 53:5 give H6343 "great"
  - Job 3:25 gives H6343 "thing"

  The face was read from the verse, not from the surface word.
- **The "negated" flag is approximate** (as in unit 1). Faces were assigned by reading.

---

## A. The faces in unit 2 (change of character, #1919)

Letters A–J are the unit 1 faces, reused where the verses show the same face. K–T are new in this unit.

| Face | Hits / verses | Surfaces | What differs | Example verses |
| --- | --- | --- | --- | --- |
| **A. Felt before a threat or a person** | 22 / 18 | trembled · trembling · afraid · fear · anguish · shuddering · panic | Object: an army, an enemy's anger, a prophet's arrival, the multitude, the oppressor, a discovery | 1Sa 28:5; Psa 55:4–5; Job 31:34; Pro 29:25; Gen 27:33; 1Sa 16:4 |
| **B. Felt before God's presence, act or word, or a spirit** | 18 / 14 | dread · terrified · trembled · trembles · trembling · fear | Object: God's presence, his voice in the thunder, his word read aloud, a vision, his act; once **a spirit in the night** | Job 23:15; Job 37:1; Exo 19:16; Dan 10:7, 11; Jer 36:16; Job 4:14 |
| **C. Spoken against** | 11 / 11 | dread · frightened · Fear [not] · afraid · terror | "Do not be in dread", with a ground; self-spoken "I will not be afraid" | Deu 7:21; Jos 1:9; Isa 8:12; Isa 12:2; Psa 91:5 |
| **D. Fearing or trembling before God as a standing** | 11 / 10 | tremble · trembled · awe · fear · fears · dread · trembling | Trembling at his word; "let him be your dread"; fearing "always"; awe of his words | Isa 66:2; Ezr 9:4; Isa 8:13; Pro 28:14; Psa 119:161 |
| **F. What or who inspires dread** | 7 / 7 | Fear · fear · feared · dread · trembling · tremble | God named "the Fear of Isaac"; a person who is an object of dread; Ephraim's speech | Gen 31:42, 53; Psa 89:7; Psa 31:11; Hos 13:1 |
| **G. Dread laid on nations and peoples** | 31 / 25 | fear · dread · tremble · trembling · horror · bristle | Laid by God, or fallen on peoples because of Israel, the Jews, Mordecai, a king | Deu 11:25; 2Ch 17:10; Exo 15:14–16; Est 9:3; Dan 5:19; Eze 32:10 |
| **I. Not fearing** | 7 / 7 | fear · afraid · trembled | No fear of God; not afraid at his word; not trembling before a man; creatures without fear | Psa 36:1; Jer 2:19; Jer 36:24; Est 5:9; Job 39:22 |
| **J. Other** | 1 / 1 | wrung | "no hands were wrung for her" | Lam 4:6 |
| **K. Terror that comes upon** | 34 / 25 | terror · dread · panic · trembling · horror · sheer terror · Dreadful | Terror as an event: it falls, strikes, overwhelms, comes like a storm; terror, pit and snare; a trembling heart given in the curse | Isa 24:17–18; Pro 1:26–27; Deu 28:65–67; Job 3:25; Isa 2:10 |
| **L. None to make afraid (and its inversion)** | 18 / 18 | make them afraid · afraid · disturbed · frighten away · disturb · fear · dread | Promised peace: "none shall make you afraid". The same phrase is used of corpses no one drives the birds from, and of deserted cities | Lev 26:6; Mic 4:4; 2Sa 7:10; Deu 28:26; Isa 17:2; Nah 2:11 |
| **M. Making others afraid, as an act** | 8 / 8 | panic · terrify · inspire terror · strike terror · frighten · tremble | The subject is the one who frightens: a counsellor, a judge, sorceries, debtors, God's messengers, "horns" | 2Sa 17:2; Judg 8:12; Isa 47:12; Psa 10:18; Zec 1:21 |
| **N. The earth, heavens, waters and the dead tremble** | 21 / 19 | trembled · trembles · quaked · shakes · shaken · tremble | The subject is the physical world, or the dead, before God | Exo 19:18; Psa 18:7; Psa 77:16; Psa 104:32; Job 26:5, 11 |
| **O. *Rāgaz* stirred: rage, anger, quarrel, grief, disturbance** | 14 / 14 | angry · raging · raged · rages · enraged · provoke · quarrel · deeply moved · disturbed · stirred up · roused · unrest | One root, rendered by many English words; subjects include God, Sennacherib, David, Joseph's brothers, a fool, Samuel brought up, Sheol | Psa 4:4; 2Ki 19:27–28; Eze 16:43; Gen 45:24; 2Sa 18:33; 1Sa 28:15 |
| **P. Trembling as care, concern or a start** | 5 / 4 | trembled · taken [trouble] · trouble · distressed · startled | Trembling **for** someone or something, or a sudden start | 1Sa 4:13; 2Ki 4:13; Est 4:4; Rut 3:8 |
| **Q. Coming to God in trembling** | 5 / 4 | come trembling · fear · turn [in dread] | Movement **toward** God, trembling | Hos 11:10–11; Hos 3:5; Mic 7:17 |
| **R. Trembling joined with joy or good** | 3 / 2 | thrill · fear · tremble | The dread root rendered "thrill"; trembling "because of all the good" | Isa 60:5; Jer 33:9 |
| **S. Trembling of the body in age** | 1 / 1 | tremble | "the keepers of the house tremble" | Ecc 12:3 |
| **T. Trembling called for** | 10 / 9 | tremble · Tremble · shudder · to tremble · shocked | A summons or decree: to the earth, the peoples, the complacent, the heavens | Psa 96:9; Psa 99:1; Joe 2:1; Isa 32:11; Dan 6:26; Jer 2:12 |

Face E (awe toward people) and H (fearing other gods) do not occur in unit 2.

---

## B. Observations

### B.1 Dread and trembling felt (faces A, B)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-47 | Dread and trembling are felt in the heart, the bones, the flesh, the hair and the face. "dread came upon me, and trembling, which made all my bones shake"; "My heart is in anguish within me; the terrors of death have fallen upon me. Fear and trembling come upon me, and horror overwhelms me"; "shuddering seizes my flesh"; "my heart trembles and leaps out of its place"; "My heart staggers; horror has appalled me"; "the hair of their kings bristles with horror; their faces are convulsed" | Job 4:14; Psa 55:4–5; Job 21:6; Job 37:1; Isa 21:4; Eze 27:35 | S | 10.1 "Where it goes in the body", 3, 6 | W (adds to FE-01) |
| FE-48 | The verbs set dread and trembling as something that comes upon the person: "dread came upon me"; "Fear and trembling come upon me"; "trembling has seized the godless"; "Trembling took hold of them there"; "a great trembling fell upon them"; "horror seizes them of the east". The verses give no further account | Job 4:14; Psa 55:5; Isa 33:14; Psa 48:6; Dan 10:7; Job 18:20 | S (the verbs); no mechanism is drawn | 10.1 "How a feeling rises", 11 §1 | W |
| FE-49 | **Dread before a spirit.** Eliphaz, "amid thoughts from visions of the night": "dread came upon me, and trembling, which made all my bones shake. A spirit glided past my face; the hair of my flesh stood up. It stood still, but I could not discern its appearance". The spirit is not named | Job 4:13–16 | S | 10.1, 15 (other parties, §7a: a spirit, unnamed, in its own terms) | W |
| FE-50 | **Dread before God's presence, voice, word and act:** | | S | 10.9 "Fear before God", 10.2 | W |
| | – Job: "I am terrified at his presence; when I consider, I am in dread of him … the Almighty has terrified me" | Job 23:15–16 | | | |
| | – at the thunder: "At this also my heart trembles … Keep listening to the thunder of his voice" | Job 37:1–2 | | | |
| | – at Sinai: "all the people in the camp trembled" | Exo 19:16 | | | |
| | – Daniel's vision: the men with him "fled to hide themselves"; "a hand touched me and set me trembling on my hands and knees"; "I stood up trembling" | Dan 10:7, 10–11 | | | |
| | – the brothers at the returned money: "they turned trembling to one another, saying, 'What is this that God has done to us?'" | Gen 42:28 | | | |
| | – "The sinners in Zion are afraid … 'Who among us can dwell with the consuming fire?'" | Isa 33:14 | | | |
| | – "I was in terror of calamity from God, and I could not have faced his majesty" | Job 31:23 | | | |
| | – Job to his friends: "Will not his majesty terrify you, and the dread of him fall upon you?" | Job 13:11 | | | |
| FE-51 | **One scroll, two hearings.** The officials "heard all the words, they turned one to another in fear". The king and his servants "who heard all these words" were not afraid, "nor did they tear their garments". Between the two verses the king cuts the scroll and burns it | Jer 36:16, 23–24 | S (the sequence is in the text) | 10.2 (hearing), **11 §4** | **RS** (11 §4: the same words heard, fear and no fear, side by side) |
| FE-52 | **Dread leads to hiding.** "Enter into the rock and hide in the dust from before the terror of the Lord, and from the splendor of his majesty"; people "enter the caves of the rocks … when he rises to terrify the earth"; the men with Daniel "fled to hide themselves" | Isa 2:10, 19, 21; Dan 10:7 | S | 10.1 "Where it turns", 13 | W (with FE-02) |
| FE-53 | **Fear of the many keeps a man silent and indoors.** "because I stood in great fear of the multitude, and the contempt of families terrified me, so that I kept silence, and did not go out of doors". The verse before speaks of hiding iniquity "in my heart" | Job 31:33–34 | S | 10.5 (with FE-04), 10.10 | W |
| FE-54 | **Fear of man set beside trust.** "The fear of man lays a snare, but whoever trusts in the Lord is safe". "you fear continually all the day because of the wrath of the oppressor … And where is the wrath of the oppressor?" Prayed: "preserve my life from dread of the enemy" | Pro 29:25; Isa 51:13; Psa 64:1 | S | 10.9 (with FE-19), 12 | W |
| FE-55 | **The thing feared comes.** "For the thing that I fear comes upon me, and what I dread befalls me" | Job 3:25 | S | 10.1 "How long it stays", 12 | W (with FE-10) |
| FE-56 | **Trembling at an arrival or a discovery:** | | S | 10.1, 10.10 | W |
| | – the elders "came to meet him trembling and said, 'Do you come peaceably?'" (Samuel) | 1Sa 16:4 | | | |
| | – Ahimelech "came to meet David, trembling" | 1Sa 21:1 | | | |
| | – "all the guests of Adonijah trembled and rose, and each went his own way" | 1Ki 1:49 | | | |
| | – Isaac "trembled very violently" on learning who had brought the game | Gen 27:33 | | | |
| | – "the man was startled and turned over" | Rut 3:8 | | | |
| | – "all the people followed him trembling" | 1Sa 13:7 | | | |
| | – towns before an advancing army: "Ramah trembles; Gibeah of Saul has fled" | Isa 10:29 | | | |

### B.2 Terror that comes upon (face K)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-57 | **Terror, pit and snare.** "Terror and the pit and the snare are upon you … He who flees at the sound of the terror shall fall into the pit, and he who climbs out of the pit shall be caught in the snare". The same words are said of Moab, with "For I will bring these things upon Moab". Also: "sudden terror overwhelms you"; "panic and pitfall have come upon us"; "I will bring terror upon you, declares the Lord God of hosts" | Isa 24:17–18; Jer 48:43–44; Job 22:10; Lam 3:47; Jer 49:5 | S | 13 | W |
| FE-58 | **Wisdom laughs at the terror of those who refused her.** "I also will laugh at your calamity; I will mock when terror strikes you, when terror strikes you like a storm". Then: "whoever listens to me will dwell secure and will be at ease, without dread of disaster". The speaker is Wisdom | Pro 1:26–27, 33 | S | 10.2, 13 | W (§7a: Wisdom speaks, in her own terms) |
| FE-59 | **A trembling heart given in the curse.** "the Lord will give you there a trembling heart and failing eyes and a languishing soul … Night and day you shall be in dread … In the morning you shall say, 'If only it were evening!' and at evening you shall say, 'If only it were morning!' because of the dread that your heart shall feel, and the sights that your eyes shall see" | Deu 28:65–67 | S | 13, 3, 10.1 "How long it stays" | W |
| FE-60 | **Dread as a message and a sign.** "it will be sheer terror to understand the message". Ezekiel is told: "eat your bread with quaking, and drink water with trembling and with anxiety", and the people "shall eat their bread with anxiety" | Isa 28:19; Eze 12:18–19 | S | 13, 10.2 | W |
| FE-61 | **Terror where there is no terror.** "There they are in great terror, for God is with the generation of the righteous". "There they are, in great terror, where there is no terror!" Also: the idol-makers "shall be terrified; they shall be put to shame together"; "horror covers them. Shame is on all faces" | Psa 14:5; 53:5; Isa 44:11; Eze 7:18 | S | 12, 13 | W |
| FE-62 | **Terror of the night** is guarded against, and promised away. Each man has "his sword at his thigh, against terror by night". "You will not fear the terror of the night". "Do not be afraid of sudden terror". "If you lie down, you will not be afraid; when you lie down, your sleep will be sweet" | Song 3:8; Psa 91:5; Pro 3:25; Pro 3:24 | S | 10.1, 10.9 "Fear not" | W (Pro 3:25 was unwoven in unit 1) |

### B.3 Dread laid on others, and making afraid (faces G, M, F)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-63 | **God lays dread on peoples, and the verses say what follows:** | | S | 15, 10.10 | W (adds to FE-41) |
| | – "The Lord your God will lay the fear of you and the dread of you on all the land"; "No one shall be able to stand against you" | Deu 11:25 | | | |
| | – "the Lord brought the fear of him upon all nations" | 1Ch 14:17 | | | |
| | – "the fear of the Lord fell upon all the kingdoms … and they made no war against Jehoshaphat" | 2Ch 17:10 | | | |
| | – "when they heard that the Lord had fought against the enemies of Israel" | 2Ch 20:29 | | | |
| | – "The peoples have heard; they tremble … Terror and dread fall upon them; because of the greatness of your arm, they are still as a stone" | Exo 15:14–16 | | | |
| | – "Egypt was glad when they departed, for dread of them had fallen upon it" | Psa 105:38 | | | |
| | – the Egyptians "tremble with fear before the hand that the Lord of hosts shakes over them" | Isa 19:16–17 | | | |
| | – kings who saw Zion: "Trembling took hold of them there, anguish as of a woman in labor" | Psa 48:5–6 | | | |
| | – "that the nations might tremble at your presence" | Isa 64:2 | | | |
| FE-64 | **Fear of a people or a person falls on others.** "many from the peoples of the country declared themselves Jews, for fear of the Jews had fallen on them"; officials "helped the Jews, for the fear of Mordecai had fallen on them". Of Nebuchadnezzar: "because of the greatness that he gave him, all peoples, nations, and languages trembled and feared before him. Whom he would, he killed". Of Ephraim: "When Ephraim spoke, there was trembling; he was exalted in Israel, but he incurred guilt through Baal and died". Of the king of Babylon: "Is this the man who made the earth tremble" | Est 8:17; 9:2–3; Dan 5:19; Hos 13:1; Isa 14:16 | S | 10.10, 12 | W (§7a: Dan 5:19 names God as giver of the greatness) |
| FE-65 | **The dread of the Lord falls on his own people.** After Saul's message with the cut-up oxen, "the dread of the Lord fell upon the people, and they came out as one man". Jehoshaphat to the judges: "let the fear of the Lord be upon you. Be careful what you do, for there is no injustice with the Lord our God, or partiality or taking bribes" | 1Sa 11:7; 2Ch 19:7 | S | 10.10, 10.7 | W (2Ch 19:7 with FE-31) |
| FE-66 | **Trembling at another's fall.** The princes of the sea "will clothe themselves with trembling; they will sit on the ground and tremble every moment and be appalled at you"; "They shall tremble every moment, every one for his own life, on the day of your downfall"; "They of the west are appalled at his day" | Eze 26:16–18; 32:10; 27:35; Job 18:20 | S | 13, 15 | W |
| FE-67 | **Making others afraid, as an act** (subject = the one who frightens). Links FE-07 | | S | 10.10, 12 | W |
| | – Ahithophel: "I will … throw him into a panic, and all the people who are with him will flee" | 2Sa 17:2 | | | |
| | – Gideon "threw all the army into a panic" | Judg 8:12 | | | |
| | – to Babylon: "Stand fast in your enchantments … perhaps you may inspire terror" | Isa 47:12 | | | |
| | – God does justice "so that man who is of the earth may strike terror no more" | Psa 10:18 | | | |
| | – "those awake who will make you tremble" | Hab 2:7 | | | |
| | – Job to God: "Will you frighten a driven leaf and pursue dry chaff?" | Job 13:25 | | | |
| | – "these have come to terrify them, to cast down the horns of the nations" | Zec 1:21 | | | |
| | – "messengers shall go out from me in ships to terrify the unsuspecting people of Cush" | Eze 30:9 | | | |
| FE-68 | **An object of dread to friends.** "an object of dread to my acquaintances; those who see me in the street flee from me" | Psa 31:11 | S | 10.10 | W |
| FE-69 | **God named by fear.** "the God of Abraham and the Fear of Isaac"; "Jacob swore by the Fear of his father Isaac". "Dominion and fear are with God; he makes peace in his high heaven". "a God greatly to be feared in the council of the holy ones" | Gen 31:42, 53; Job 25:2; Psa 89:7 | S | 10.9, 11 §4 ("The one who is feared") | W |

### B.4 Spoken against, and absent (faces C, L, I)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-70 | **"Do not be in dread", with its ground:** | | S | 10.9 "Fear not", 10.7 | W (adds to FE-14, FE-15) |
| | – "Do not be in dread or afraid of them" | Deu 1:29 | | | |
| | – "You shall not be in dread of them, for the Lord your God is in your midst, a great and awesome God" | Deu 7:21 | | | |
| | – "Do not fear or be in dread of them, for it is the Lord your God who goes with you" | Deu 31:6 | | | |
| | – "Have I not commanded you? … Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go" | Jos 1:9 | | | |
| | – "let not your heart faint. Do not fear or panic or be in dread of them" | Deu 20:3 | | | |
| | – "Fear not, nor be afraid; have I not told you from of old and declared it? … Is there a God besides me?" | Isa 44:8 | | | |
| | – self-spoken: "I will trust, and will not be afraid; for the Lord God is my strength and my song"; "The Lord is my light and my salvation; whom shall I fear?" | Isa 12:2; Psa 27:1 | | | |
| FE-71 | **Isa 8:12–13 (held from FE-19).** "do not fear what they fear, nor be in dread. But the Lord of hosts, him you shall honor as holy. Let him be your fear, and let him be your dread". The next verse: "he will become a sanctuary and a stone of offense" | Isa 8:12–14 | S | 10.9, **11 §4** ("What it is turned toward") | **RS** (the same two words, forbidden and then commanded, in consecutive verses) |
| FE-72 | **"None shall make you afraid":** | | S | 14, 10.1 | W |
| | – "I will give peace in the land, and you shall lie down, and none shall make you afraid" | Lev 26:6 | | | |
| | – "they shall sit every man under his vine and under his fig tree, and no one shall make them afraid, for the mouth of the Lord of hosts has spoken" | Mic 4:4 | | | |
| | – "they shall do no injustice and speak no lies … and none shall make them afraid" | Zep 3:13 | | | |
| | – "They shall forget their shame … when they dwell securely in their land with none to make them afraid" | Eze 39:26; 34:28 | | | |
| | – "Jacob shall return and have quiet and ease, and none shall make him afraid" | Jer 30:10; 46:27 | | | |
| | – "dwell in their own place and be disturbed no more" (*rāgaz*) | 2Sa 7:10; 1Ch 17:9 | | | |
| | – "He led them in safety, so that they were not afraid" | Psa 78:53 | | | |
| | – Zophar to Job: "You will lie down, and none will make you afraid" | Job 11:19 | | | |
| FE-73 | **The same phrase, used of ruin.** "there shall be no one to frighten them away", of the birds at the dead bodies; "The cities of Aroer are deserted; they will be for flocks, which will lie down, and none will make them afraid"; the lions' den "with none to disturb". Job of the wicked: "Their houses are safe from fear, and no rod of God is upon them" | Deu 28:26; Jer 7:33; Isa 17:2; Nah 2:11; Job 21:9 | S | **11 §4**, 13, 10.9 | **RS** (11 §4: one phrase used of promised peace and of desolation) |
| FE-74 | **Not fearing.** "there is no fear of God before his eyes"; "the fear of me is not in you, declares the Lord God of hosts"; the king and his servants heard the scroll and were not afraid (FE-51). Mordecai "neither rose nor trembled before him", and Haman "was filled with wrath". Of the ostrich, "she has no fear"; of the horse, "He laughs at fear and is not dismayed" | Psa 36:1; Jer 2:19; Jer 36:24; Est 5:9; Job 39:16, 22 | S | 12, 10.10, 15 (creatures) | W (Psa 36:1 and Est 5:9 are already in the chapters) |

### B.5 Trembling before God as a standing, coming, joy, summons (faces D, Q, R, T)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-75 | **Trembling at his word.** "this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word"; "you who tremble at his word: 'Your brothers who hate you and cast you out for my name's sake …'"; "all who trembled at the words of the God of Israel, because of the faithlessness of the returned exiles, gathered around me"; "those who tremble at the commandment of our God"; "Princes persecute me without cause, but my heart stands in awe of your words" | Isa 66:2, 5; Ezr 9:4; Ezr 10:3; Psa 119:161 | S | 10.2, 10.9, 5 ("contrite in spirit") | W |
| FE-76 | **Fearing always, set against hardening.** "Blessed is the one who fears the Lord always, but whoever hardens his heart will fall into calamity". Also: they "will stand in awe of the God of Israel" | Pro 28:14; Isa 29:23 | S | 10.9, 12 | W |
| FE-77 | **Coming to God in trembling.** "he will roar like a lion; when he roars, his children shall come trembling from the west; they shall come trembling like birds from Egypt … and I will return them to their homes". "they shall come in fear to the Lord and to his goodness in the latter days". The nations "shall turn in dread to the Lord our God" | Hos 11:10–11; Hos 3:5; Mic 7:17 | S | 10.9, 14 | W |
| FE-78 | **The dread root in joy.** "your heart shall thrill and exult" (the *paḥad* verb, "to dread", H6342). "They shall fear and tremble because of all the good and all the prosperity I provide for it", after "I will forgive all the guilt of their sin". With "rejoice with trembling" (already woven) | Isa 60:5; Jer 33:8–9; Psa 2:11 | S | **11 §4**, 10.1, 14 | **RS** (11 §4: the dread root rendered "thrill"; fear at good) |
| FE-79 | **Trembling called for, and decreed:** | | S | 10.9, 15 | W |
| | – "Worship the Lord in the splendor of holiness; tremble before him, all the earth!" | Psa 96:9; 1Ch 16:30 | | | |
| | – "The Lord reigns; let the peoples tremble!" | Psa 99:1 | | | |
| | – "Tremble, O earth, at the presence of the Lord" | Psa 114:7 | | | |
| | – "Let all the inhabitants of the land tremble, for the day of the Lord is coming" | Joe 2:1 | | | |
| | – to the women at ease: "Tremble, you women who are at ease, shudder, you complacent ones" | Isa 32:9–11 | | | |
| | – Darius: "people are to tremble and fear before the God of Daniel, for he is the living God" | Dan 6:26 | | | |
| | – to the heavens: "Be appalled, O heavens, at this; be shocked" | Jer 2:12 | | | |

### B.6 The physical world trembles (face N)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-80 | **The earth, mountains, heavens, waters and the dead tremble.** The verses use for them the words used of people: | | S | 15 (the physical world, §7a), 13 | W |
| | – "the whole mountain trembled greatly" | Exo 19:18 | | | |
| | – "the foundations also of the mountains trembled and quaked, because he was angry" | Psa 18:7; 2Sa 22:8 | | | |
| | – "When the waters saw you, O God, when the waters saw you, they were afraid; indeed, the deep trembled" | Psa 77:16, 18 | | | |
| | – "who looks on the earth and it trembles" | Psa 104:32 | | | |
| | – "The voice of the Lord shakes the wilderness" | Psa 29:8 | | | |
| | – "the earth sees and trembles" | Psa 97:4 | | | |
| | – "The pillars of heaven tremble and are astounded at his rebuke" | Job 26:11 | | | |
| | – "who shakes the earth out of its place, and its pillars tremble" | Job 9:6 | | | |
| | – "The dead tremble under the waters" | Job 26:5 | | | |
| | – "I will make the heavens tremble … at the wrath of the Lord of hosts" | Isa 13:13 | | | |
| | – "the anger of the Lord was kindled … and the mountains quaked" | Isa 5:25 | | | |
| | – "The earth quakes before them; the heavens tremble" | Joe 2:10 | | | |
| | – "Shall not the land tremble on this account", after "you who trample on the needy" | Amo 8:8 (with 8:4) | | | |
| | – "Under three things the earth trembles", then four kinds of people | Pro 30:21–23 | | | |
| | – also | 1Sa 14:15; Isa 23:11; Hab 3:7 | | | |

### B.7 *Rāgaz*: one root, trembling, rage and grief (face O)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-81 | **One root, *rāgaz*, "to tremble", rendered by the ESV:** | | S (the renderings) | **11 §4**, 10.1, 13, 10.10 | **RS** (11 §4: new entry. The anger strand already cites Psa 4:4 and 2Ki 19:28 as anger, and the root behind both is this trembling word) |
| | – trembling and quaking (the peoples, the earth, Habakkuk's body) | Exo 15:14; Psa 18:7; Hab 3:16 | | | |
| | – "Be angry, and do not sin" | Psa 4:4 | | | |
| | – God to Sennacherib: "I know … your raging against me. Because you have raged against me" | 2Ki 19:27–28; Isa 37:28–29 | | | |
| | – God: "you … have enraged me with all these things" | Eze 16:43 | | | |
| | – "those who provoke God are secure" | Job 12:6 | | | |
| | – Joseph to his brothers: "Do not quarrel on the way" | Gen 45:24 | | | |
| | – "the fool only rages and laughs, and there is no quiet" | Pro 29:9 | | | |
| | – David at the news of Absalom: "the king was deeply moved and went up to the chamber over the gate and wept" | 2Sa 18:33 | | | |
| | – Samuel to Saul: "Why have you disturbed me by bringing me up?" | 1Sa 28:15 | | | |
| | – "Sheol beneath is stirred up to meet you" | Isa 14:9 | | | |
| | – God "will be roused; to do his deed — strange is his deed!" | Isa 28:21 | | | |
| | – "unrest to the inhabitants of Babylon" | Jer 50:34 | | | |
| | External parties in these verses (§7a): God (enraged, roused); Samuel brought up from the dead (1Sa 28:15); Sheol (Isa 14:9). | | | | |

### B.8 Trembling for another, in age, under rain; other (faces P, S, J)

| id | observation | verses | basis | touches | disposition |
|---|---|---|---|---|---|
| FE-82 | **Trembling for someone or something.** Eli "was sitting on his seat by the road watching, for his heart trembled for the ark of God". Elisha to the Shunammite: "you have taken all this trouble for us" (the ESV renders the trembling root as taking trouble). When told of Mordecai, "the queen was deeply distressed" | 1Sa 4:13; 2Ki 4:13; Est 4:4 | S | **11 §4**, 10.10, 3 | **RS** (11 §4: trembling **for** another sits beside trembling **before** a threat) |
| FE-83 | **Trembling in age.** "in the day when the keepers of the house tremble, and the strong men are bent" | Ecc 12:3 | S | 9, 6 | W |
| FE-84 | **Two causes in one verse.** "all the people sat in the open square before the house of God, trembling because of this matter and because of the heavy rain" | Ezr 10:9 | S | 10.1 "How a feeling rises" (§7a: the rain) | W |
| FE-85 | Lam 4:6, "no hands were wrung for her", is tagged with the trembling root. The English shows no fear | Lam 4:6 | S | none | H (accounted for here; not woven) |

---

## C. Change of character: what differs between the faces (#1919, for Ch 11 §4)

Stated only as far as the verses go. Factors already in 11 §4 are marked "(existing)".

| Factor | Verses that show it | basis |
|---|---|---|
| **What it is turned toward** (existing): dread forbidden toward what the people dread, commanded toward the Lord, in consecutive verses | Isa 8:12–13 | S |
| **The same words heard by two groups**: fear in one, none in the other | Jer 36:16, 24 | S |
| **The direction of the trembling**: before a threat (A), toward God (Q), for another (P), at another's fall (FE-66) | 1Sa 28:5; Hos 11:10–11; 1Sa 4:13; Eze 32:10 | S (the grouping is R) |
| **The subject**: a person, a people, the earth, the waters, the dead | FE-47, FE-63, FE-80 | S |
| **One root, rendered as trembling, rage, quarrel and grief** | FE-81 | S (renderings) |
| **The dread root in joy** ("thrill"; fear "because of all the good") | Isa 60:5; Jer 33:9 | S |
| **One phrase, peace and ruin**: "none shall make them afraid" of promised peace and of deserted land | FE-72, FE-73 | S |
| **Who frightens, and to what end**: a counsellor's plan, sorceries, God's messengers, debtors | FE-67 | S (the grouping is R) |

---

## D. Already in the chapters (no new weave needed beyond the pointer)

- 1Sa 28:5, Psa 119:120 (FE-01, 10.1 and 6)
- Hab 3:16 (Ch 6)
- Judg 7:3 (FE-11; 10.1, 10.10, 11 §6)
- Psa 2:11 (10.1, 10.9, 11 §4)
- Psa 4:4 (10.1, 10.4, 10.9, as anger)
- 2Ki 19:28 (11 §4, "the nose")
- Psa 36:1 (Ch 12)
- Est 5:9 (Ch 11)
- Jer 5:22 (FE-43; 10.4, 10.10, 13)

## E. Not in this unit (pointers)

- **Unit 3:** terror, horror and desolation roots (H0367, H4288, H8047G/H, H1091, H2851, H4032, H2189 and others), with the §3A.3 non-fear surfaces.
- **Unit 4:** the Greek *phobos* group, Greek trembling (G5156, G5141, G1790), the "respect" surfaces, and claim 9-4 (2Ti 1:7).
- **Anger strand:** FE-81 shows that the trembling root *rāgaz* stands behind two verses the anger material already uses (Psa 4:4; 2Ki 19:27–28). The proposal is to name this in 11 §4 only. The anger sections are not re-read in this unit.

## F. Quote check

All quotes in §B were run through `fear-quote-check-v1-20261001.py`, rebuilt this unit (see the handoff). For each table row, it takes the references cited in that row, fetches their ESV text from iba.db `verse`, and checks that every quoted fragment (split at "…") occurs in that text, ignoring case, punctuation and quotation marks.
- It also strips [bracketed insertions] and skips gloss labels (*translit*, "gloss").
- **Result (2026-10-01):** 176 quotes checked, **0 failures**, no missing verse text. Two heading labels are not checked as quotes ("Do not be in dread", "None shall make you afraid"); their wording is quoted from Deu 1:29 and Lev 26:6 in the rows below them.
- Tested against a deliberately wrong quote (caught) and a quote running across two verses (passed).
- Run on the unit 1 ledger as well, it found two ledger-only slips (Isa 11:2 in FE-24; Job 5:21 in FE-44). Both were corrected there, with a note at its foot. Neither quote is in the chapters.

## G. Next

1. **Researcher review of this ledger**: the faces, the scope decisions above, the observations and the proposed dispositions.
2. **On approval, weave.** Version bumps, prior versions to `archive/`, claim register in the same pass.
   - Likely touches: 10.1, 10.2, 10.5, 10.7, 10.9, 10.10, 11 §4, 12, 13, 14, 15, 3, 5, 6, 9.
   - **RS items for 11 §4:** FE-51, FE-71, FE-73, FE-78, FE-81, FE-82.
3. **Unit 3:** terror, horror and desolation.

---

## Woven — where (2026-10-01, #1929)

The researcher approved the ledger: *"proceed with the weaving"*. FE-47 to FE-84 are woven; FE-85 is held.

**Chapter versions:**
- 03 v5 · 05 v3 · 06 v4
- 10.1 v5 · 10.2 v5 · 10.5 v5 · 10.7 v5
- 10.9 v6 · 10.10 v6 · 11 v6 · 12 v6 · 14 v6
- 13 v3 · 15 v4

Prior versions are in `archive/`. The claim register is now v6, and the index has a Structure log row for this unit.

| Observations | Woven in |
|---|---|
| FE-47 | 10.1 "Where it goes in the body" (heart: Psa 55:4; Job 37:1; Isa 21:4); Ch 6 (bones, flesh, hair and face: Job 4:14; 21:6; Eze 27:35) |
| FE-48 | Ch 11 §1 "Dread is laid on, given, and comes upon"; 10.1 (pointer) |
| FE-49 | 10.1 "How a feeling rises" (Job 4:13–15); Ch 15 "A spirit passes by"; Ch 6 already had Job 4:15 |
| FE-50 | 10.9 "Fear before God" (Exo 19:16; Job 23:15; 37:1–2; Dan 10:10–11; Gen 42:28; Isa 33:14; Job 31:23) |
| FE-51 (**RS**) | 10.2; Ch 11 §4 factor "Who hears it" |
| FE-52 | 10.1 hiding (Isa 2:10); Ch 13 "Shelter" (Isa 2:10, 19) |
| FE-53 | 10.5 "Fear and the mouth"; 10.1 (Job 31:34) |
| FE-54 | 10.9 "Fear not" (Isa 51:13; Psa 64:1); Ch 12 (Pro 29:25) |
| FE-55 | 10.1 "How long it stays" (Job 3:25) |
| FE-56 | 10.1 "How a feeling rises" (1Sa 16:4; 1Ki 1:49; Gen 27:33); 10.10 (1Sa 16:4; 21:1) |
| FE-57, FE-60 | Ch 13 "Dread and trembling"; FE-60 also 10.2 (Isa 28:19) |
| FE-58 | 10.2 (Pro 1:26, 33); Ch 13 (Pro 1:27, set apart from the list on God's anger) |
| FE-59 | 10.1 (Deu 28:66–67); Ch 11 §1 and Ch 3 (Deu 28:65); Ch 13 (pointer) |
| FE-61 | Ch 12 (Psa 53:1, 5) |
| FE-62 | 10.9 "Fear not" (Psa 91:5; Pro 3:24–25) |
| FE-63 | Ch 15 "Dread falls on whole peoples"; Ch 11 §1 (Deu 11:25) |
| FE-64, FE-67, FE-68 | 10.10 |
| FE-65 | 10.7 (2Ch 19:7; 1Sa 11:7) |
| FE-66 | Ch 13 (Eze 32:10; 26:16) |
| FE-69 | 10.9 (Gen 31:42, 53; Psa 89:7) |
| FE-70 | 10.9 "Fear not" (Deu 7:21; Isa 44:8; Isa 12:2); 10.7 (Jos 1:9; Deu 20:3) |
| FE-71 (**RS**) | 10.9 "Fear not"; Ch 11 §4 face "Dread" |
| FE-72 | Ch 14 "No one to make them afraid" (2Sa 7:10, Psa 78:53 and others stay in the ledger) |
| FE-73 (**RS**) | Ch 11 §4 face "None shall make you afraid" (Lev 26:6; Isa 17:2; Deu 28:26) |
| FE-74 | Ch 12 (Jer 2:19); 10.10 (Est 5:9); Ch 15 (Job 39:16, 22) |
| FE-75 | 10.9 "Trembled at his word"; 10.2 (Psa 119:161); Ch 5 (Isa 66:2) |
| FE-76 | 10.9 "Kept always"; Ch 12 (Pro 28:14) |
| FE-77 | 10.9 "People come to him trembling"; Ch 14 (pointer) |
| FE-78 (**RS**) | Ch 11 §4 face "Dread"; 10.9 (Jer 33:8–9); Ch 3 (Isa 60:5); 10.1 (pointer) |
| FE-79 | 10.9 "Trembling before him is called for" |
| FE-80 | Ch 15 "The earth, the waters and the dead tremble"; Ch 13 (Psa 18:7; Isa 13:13; 5:25) |
| FE-81 (**RS**) | Ch 11 §4 face "Trembling"; 10.1 (pointer); 10.10 (Gen 45:24; Pro 29:9); Ch 13 (Eze 16:43); Ch 15 (Isa 14:9) |
| FE-82 (**RS**) | Ch 11 §4 face "Trembling" (1Sa 4:13); 10.10; Ch 3 |
| FE-83 | Ch 6 (Ecc 12:3). Not Ch 9: the verse is placed with the flesh |
| FE-84 | 10.1 "How a feeling rises" (Ezr 10:9) |
| FE-85 | Held (Lam 4:6) |

**Not quoted in the chapters, kept here:** among them Job 13:11, 13:25, 18:20, 22:10, 25:2; Lam 3:47; Isa 19:16–17, 64:2, 44:11; Eze 7:18; Hab 2:7; Zec 1:21; Eze 30:9; Psa 14:5, 48:5; 2Sa 7:10; 1Ch 17:9; Psa 78:53; Job 11:19; Isa 37:28–29; Job 12:6; Isa 28:21; Jer 50:34; Exo 15:15; 1Ch 16:30. Every hit stays accounted for in the face column of `fear-unit2-pahad-trembling-pull-v1-20261001.csv`.
