# Anger: reconciliation and cross-ledger overview of units 1–5 (v1)

**Date:** 2026-10-05 · **Author:** Claude Code · **Status:** draft, for the researcher. **Not chapter text.** The weave stays held until this overview is approved (as for fear, OT-10).
**Process:** `anger-key-characteristic-process-proposal-v1-20261005.md`, steps 2 and 3 (approved #1963, rulings §7). Researcher, verbatim (2026-10-05): *"start with step 2: checking units 1–5 against the 65 Strong's and 919 hits, using the five faces files. Step 3, the cross-ledger overview"*.

**Sources (the five approved ledgers only; no new reading of verses):**

| Ledger | Words | Hits / verses | Observations | Faces |
|---|---|---|---|---|
| unit 1 (#1966) | *ʾaph* (anger), *ʾānap̄* (to be angry) | 239 / 230 | AG-01 to AG-59 | A–Z (25) |
| unit 2 (#1967) | *ḥēmāh* (heat, wrath) and the heat words | 132 / 125 | AG-60 to AG-101 | 2A–2W (23) |
| unit 3 (#1968) | *ḥārāh* (to burn), *ḥārôn* (burning), *ḥŏrî*, *kāʿas* (to provoke, vex) | 217 / 203 | AG-102 to AG-146 | 3A–3AA (27) |
| unit 4 (#1969) | the rest of the Hebrew and Aramaic (28 Strong's) | 221 / 202 | AG-147 to AG-198 | 4A–4AE (31) |
| unit 5 (#1973) | the Greek (25 Strong's) | 110 / 94 | AG-199 to AG-240 | 5A–5AB (28) |
| **all** | **every M02 word: 65 Strong's** | **919 / 681** (verses counted once) | **240** | **134** |

**How to read this:**
- **S** = a verse states it. **R** = my reading or my arrangement, marked as such.
- Quotes are taken from the ledgers, where they were already checked, and checked again here (§K).
- No pattern is drawn that a verse does not state (cfg_behaviour_rule 69). Where two verses are set side by side, they are not joined.
- Prior work is cited by ledger id (AG-nn), not restated.

---

## Step 2. Reconciliation (coverage check)

**Method.** `anger-reconciliation-v1-20261005.py` (read-only, iba.db) compares the five unit pulls and the five faces files with the live M02 vocabulary, hit by hit. Hits are compared as a multiset of (reference, position, Strong's), because one span can hold two codes for the same Strong's (1Sa 20:7, unit 3 data note).

**Result (2026-10-05):**

| Check | Result |
|---|---|
| Live M02 Strong's (`cluster_strong`, not deleted) | **65** (40 Hebrew and Aramaic, 25 Greek), none duplicated |
| Each Strong's in exactly one unit | **yes**: none in two units, none in no unit, no unit word outside M02, none with zero hits |
| Live hits (`verse_lexical` and `verse`, not deleted) | **919 in 681 verses** |
| Live hits missing from the five pulls | **0** |
| Pull rows that are not live hits | **0** |
| Pull rows: 239 + 132 + 217 + 221 + 110 | **919** |
| Rows without a face (pulls and faces files) | **0** |
| Faces rows with no matching pull row, or pull rows with no faces row | **0** |
| Verses against the M02 phenomena ledger v5 | 681 = 681; none missing either way |

**No gap was found, so no addendum is needed** (fear needed one, for H4172A). Step 2 is closed.

**Two notes from reading the ledgers against each other** (not coverage gaps):
- The unit 5 data notes say Rev 14:8 and 18:3 are read with the wine of God's wrath *in AG-241*. There is no AG-241; the row is **AG-216** (*Two wines*). A slip in a cross-reference only; the hits are faced (5AB).
- Units 1–3 counted "already in the chapters" without the book carried forward to bare references; units 4–5 used `anger-chapter-match-v1-20261005.py`, which does. The unit 1–3 counts in their §D are therefore a little low. This does not affect coverage.

---

## A. What the verses say anger is

No verse in the five ledgers defines anger. What the verses state falls under the headings below. **The headings are my arrangement (R).** Each line under them is stated (S).

| Heading (R) | What the verses state | Verses | basis |
|---|---|---|---|
| **It is kindled, burns and is poured** | "So the anger of the Lord was kindled against Israel"; "my anger and my wrath will be poured out on this place"; "At this the king became enraged, and his anger burned within him"; "Then Nebuchadnezzar was filled with fury" | Judg 2:20; Jer 7:20; Est 1:12; Dan 3:19 | S |
| **It is set off by something heard or seen, for God and for people** | "when the Lord heard it, his anger was kindled"; "As soon as his master heard the words that his wife spoke to him … his anger was kindled"; "When they heard these things, all in the synagogue were filled with wrath"; "when Haman saw Mordecai in the king's gate … he was filled with wrath" | Num 11:1; Gen 39:19; Luk 4:28; Est 5:9 | S |
| **It moves and has a span** | "wrath has gone out against you from the Lord"; "For his anger is but for a moment, and his favor is for a lifetime"; "with them the wrath of God is finished"; "the wrath of God remains on him"; Edom "kept his wrath forever" | 2Ch 19:2; Psa 30:5; Rev 15:1; Joh 3:36; Amo 1:11 | S |
| **It is felt in the body and the person** | "Your wrath lies heavy upon me"; "There is no soundness in my flesh because of your indignation"; "So Cain was very angry, and his face fell"; "I went in bitterness in the heat of my spirit"; "my spirit drinks their poison" | Psa 88:7; Psa 38:3; Gen 4:5; Eze 3:14; Job 6:4 | S |
| **It is drunk** | "you who have drunk from the hand of the Lord the cup of his wrath"; "he also will drink the wine of God's wrath, poured full strength into the cup of his anger" | Isa 51:17; Rev 14:10 | S |
| **What human anger is said to do and not do** | "for the anger of man does not produce the righteousness of God"; "anger lodges in the heart of fools"; "Cursed be their anger, for it is fierce, and their wrath, for it is cruel!"; "Wrath is cruel, anger is overwhelming, but who can stand before jealousy?" | Jam 1:20; Ecc 7:9; Gen 49:7; Pro 27:4 | S |
| **Governed, and put away** | "Be angry and do not sin; do not let the sun go down on your anger"; "Whoever is slow to anger is better than the mighty"; "Let all bitterness and wrath and anger and clamor and slander be put away from you". The first and last stand five verses apart, with different Greek words (AG-223) | Eph 4:26; Pro 16:32; Eph 4:31 | S; side by side, not reconciled |
| **God's anger named with who God is** | "The Lord, the Lord, a God merciful and gracious, slow to anger"; "I will not execute my burning anger … for I am God and not a man"; "until he has executed and accomplished the intents of his heart"; "I have no wrath" | Exo 34:6; Hos 11:9; Jer 23:20; Isa 27:4 | S |
| **Named by its absence** | "lifting holy hands without anger or quarreling"; love "is not irritable or resentful"; the overseer "must not be arrogant or quick-tempered" | 1Ti 2:8; 1Cor 13:5; Tit 1:7 | S |

**Which words the verses keep for whom (S, by count; from the five ledgers' "by word" tables):**

| Word | Whose anger it is | Unit |
|---|---|---|
| *ʾaph* (H0639G) with *ʾānap̄* | God's in 124 of 239 hits; people speaking or acting toward God's anger 64; a person's own 51 | 1 |
| *ḥēmāh* (H2534) | God's 69 of 132 (with the heat words); a person's 27; venom 6; heat with no anger 4 | 2 |
| *ḥārôn* (H2740) | **God's in all 39 hits that are anger** | 3 |
| *ḥārāh* (H2734) | people 49, God 41, of 91 | 3 |
| *kāʿas* verb (H3707) | people provoke God in 44 of 53 | 3 |
| *kaʿas* noun (H3708A/B) | a person's vexation or grief in 18 of 26; God's toward a sufferer 2 (both said by the sufferer) | 3 |
| *qeṣep̄* (H7110A) | God's in 25 of 28 | 4 |
| *zaʿam* noun (H2195) | **God's indignation in every hit that is anger** (21 of 22; the 22nd is insolence) | 4 |
| *ʿebrāh* (H5678) | God's 24 of 34; people 6; pride or insolence 3 | 4 |
| *qāṣap̄* verb (H7107); *zāʿap̄* family | used of God and of people; *zāʿap̄* mostly people | 4 |
| *orgē* (G3709) | God's wrath in 29 of 35; the same noun is the anger people must put away (Col 3:6, 8) | 5 |
| *orgizō* (G3710) | **never God's own anger** in the M02 Greek | 5 |
| *thymos* (G2372) | God's 8, people's 7, the devil's 1, "passion" 2 | 5 |

**What this shows (R):** the verses speak of anger in the same words for God and for people, and they also keep some words almost wholly for God (*ḥārôn*, *zaʿam*, *qeṣep̄*, and *orgē* in the Greek). The same pictures (kindled, burning, poured, drunk) are used on both sides. Where the verses mark a difference, they mark it in restraint: "for I am God and not a man" (Hos 11:9). I note this; no verse sets out the two side by side as a doctrine.

---

## B. Its forms: the faces across units 1–5, by party (ruling 6.2)

The 134 unit faces are merged into 55 forms. Counts come from the faces files (`anger-overview-forms-v1-20261005.py`, every face used once; hits / distinct verses).
**Grouping (R):** by party, as ruling 6.2 asks: whose anger it is, who provokes it, who speaks to God about it or acts on it, who carries it out, and the person who is angry. No party is placed under another.

| Part | Party | Hits / verses |
|---|---|---|
| B.1 | God is the one who is angry | 354 / 241 |
| B.2 | Those who provoke God's anger | 71 / 65 |
| B.3 | Those who speak to God about his anger, or act on it | 140 / 104 |
| B.4 | Those who carry it out | 20 / 14 |
| B.5 | Jesus; the master in the parables; a spirit | 7 / 7 |
| B.6 | A person is the one who is angry | 269 / 211 |
| B.7 | One word, several parties | 12 / 8 |
| B.8 | No anger in the verse (data) | 46 / 43 |
| | **all** | **919** |

### B.1 God is the one who is angry

| Form | Faces | Hits / verses | Units | Key verses |
|---|---|---|---|---|
| With his people, or with those who do wrong: the cause named | A, 2A, 3A, 4A, 5A | 144 / 94 | 1–5 | Judg 2:14, 20; 2Ki 22:17; Zec 7:12; 2Ch 19:2; Rom 1:18 |
| On nations, enemies and oppressors; the earth before it | C, 2C, 3C, 4I | 68 / 40 | 1–4 | Exo 22:24; Psa 2:5; 2Sa 22:8; Isa 63:3–6; Jer 10:10 |
| Restrained, held back, turned; for a moment | D, 2F, 3D, 4F | 31 / 23 | 1–4 | Psa 78:38; Eze 20:9; Hos 11:9; Isa 54:8; Isa 57:16 |
| With a named person or group | B, 3B | 20 / 12 | 1, 3 | Exo 4:14; Num 12:9; 2Sa 6:7; 1Ki 11:9; Job 42:7 |
| The day of wrath; the wrath to come, and deliverance | 4J, 5C, 5F | 19 / 19 | 4, 5 | Zep 1:15; Pro 11:4; Mat 3:7; 1Th 1:10; Rev 6:16–17 |
| The cup, the winepress, the bowls | 2H, 5G | 16 / 13 | 2, 5 | Isa 51:17, 22; Jer 25:15; Rev 14:10; Rev 15:1 |
| Guarded against; one acts and all bear it | 4C, 4D | 12 / 12 | 4 | Num 1:53; Jos 9:20; Num 16:22; 2Ch 32:25 |
| Not turned back ("his hand is stretched out still") | E | 10 / 8 | 1 | Isa 5:25; Isa 9:12; 2Ki 23:26 |
| Spent, satisfied; a set end | 2E, 4G | 10 / 9 | 2, 4 | Eze 5:13; Eze 16:42; Dan 8:19; Isa 10:25 |
| "Slow to anger": the proclaimed name | F | 9 / 9 | 1 | Exo 34:6; Num 14:18; Joe 2:13; Nah 1:3 |
| On the false prophets and the wicked (the storm) | 2B | 5 / 4 | 2 | Eze 13:13; Jer 23:19 |
| Joined with jealousy | 2D | 4 / 4 | 2 | Eze 16:38; Zec 8:2 |
| In the bringing out and the gathering | 2G | 3 / 3 | 2 | Eze 20:33–34; Jer 32:37 |
| Shown, and endured with patience | 5D | 2 / 1 | 5 | Rom 9:22 |
| Great wrath, source not named | 4N | 1 / 1 | 4 | 2Ki 3:27 (held) |

### B.2 Those who provoke God's anger

| Form | Faces | Hits / verses | Units | Key verses |
|---|---|---|---|---|
| People provoke God: what provokes, named each time | 3J, 4B, 5B | 52 / 49 | 3–5 | Deu 4:25; 1Ki 14:9; Jer 7:18; Deu 9:7; Heb 3:10 |
| Meribah: the quarrel kept in a place | 4O | 11 / 9 | 4 | Exo 17:7; Num 20:13; Psa 106:32–33 |
| Answered in kind; God provokes | 3L, 5H | 5 / 4 | 3, 5 | Deu 32:21; Rom 10:19 |
| The provocation turns on the provoker | 3K | 3 / 3 | 3 | Jer 7:19; Jer 25:7; Jer 44:8 |

### B.3 Those who speak to God about his anger, or act on it

| Form | Faces | Hits / verses | Units | Key verses |
|---|---|---|---|---|
| Lament and prayer; borne in body and days | H, 2K, 3G, 4K, K | 55 / 45 | 1–4 | Psa 6:1; Psa 38:3; Psa 88:7; Psa 90:7; Mic 7:9 |
| Acting or calling to turn it away; warned of it | L, 2L, 3E | 36 / 22 | 1–3 | Jos 7:26; 2Ch 12:12; 2Ch 29:10; 2Ki 22:13; Jon 3:9 |
| Intercession; asking him not to be angry; standing between | G, 2J, 3F, 4E | 23 / 16 | 1–4 | Gen 18:30; Exo 32:11; Deu 9:19; Num 16:48; Zec 1:12 |
| Called down on others | I, 2M, 3H, 4L | 10 / 8 | 1–4 | Psa 69:24; Jer 10:25; Neh 4:5 |
| Explained, asked about, presumed on | J | 8 / 8 | 1 | Job 4:9; Jer 2:35; Deu 29:24; Ezr 8:22 |
| The prophet filled with it; denouncing | 2N, 4M | 8 / 7 | 2, 4 | Jer 6:11; Eze 3:14; Jer 15:17; Num 23:8 |

### B.4 Those who carry it out

| Form | Faces | Hits / verses | Units | Key verses |
|---|---|---|---|---|
| Carried out by agents and instruments, and exceeded | M, 2O, 3I, 4H, 5E | 20 / 14 | 1–5 | Isa 10:5–7; Isa 47:6; Zec 1:15; 2Ch 28:9; 1Sa 28:18; Rom 13:4 |

### B.5 Jesus; the master in the parables; a spirit

| Form | Faces | Hits / verses | Unit | Key verses |
|---|---|---|---|---|
| The master in the parables | 5J | 3 / 3 | 5 | Mat 18:34; Mat 22:7; Luk 14:21 |
| Jesus's anger and indignation | 5I | 2 / 2 | 5 | Mar 3:5; Mar 10:14 |
| The devil's great wrath; the dragon's fury | 5K | 2 / 2 | 5 | Rev 12:12, 17 |

### B.6 A person is the one who is angry

| Form | Faces | Hits / verses | Units | Key verses |
|---|---|---|---|---|
| The ruler's anger, and those beneath it | T, 2P, 3R, 4P, 5O | 31 / 25 | 1–5 | Est 1:12; Dan 2:12; Pro 19:12; Pro 16:14; Mat 2:16 |
| Strife and quarrel | 4Y, 4Z, 5W, 5X, 5Z | 27 / 25 | 4, 5 | Gen 13:8; Pro 26:21; Pro 19:13; Jam 4:1; Act 15:39 |
| At a demand, a slight, an expectation, a charge or a rebuke | P, 2Q, 3P, 4R | 23 / 15 | 1–4 | Gen 30:2; Num 22:27; 2Ki 5:11; Gen 31:36; 2Ch 26:19 |
| Governed in the sayings: slow, quick, turned, stirred | V, W, 2S | 21 / 17 | 1, 2 | Pro 14:29; Pro 16:32; Pro 15:1; Pro 15:18 |
| Kindled by what is heard or seen | O, 3M, 5N | 20 / 12 | 1, 3, 5 | Gen 39:19; Exo 32:19; Job 32:2; Luk 4:28; Act 7:54 |
| Indignation: for one wronged, at waste, at good done, at idols, at one's own wrong | R, 3N, 2U, 5Q, 5S, 5U, 5V | 19 / 16 | 1–3, 5 | 2Sa 12:5; Neh 5:6; Psa 119:53; Mat 26:8; Luk 13:14; Act 17:16; 2Cor 7:11 |
| Put away and governed (the Greek lists and sayings) | 5L, 5M | 19 / 13 | 5 | Gal 5:20; Eph 4:26, 31; Col 3:8; Jam 1:19–20; Mat 5:22 |
| At a rival's honour, a brother, kin | Q, 3O, 5R, 5T | 18 / 15 | 1, 3, 5 | Gen 4:5; Gen 27:45; 1Sa 18:8; Mat 20:24; Luk 15:28 |
| Its course and company; kept forever and cursed; overflow as pride | X, 4U, 4V | 16 / 15 | 1, 4 | Gen 49:7; Pro 22:24; Amo 1:11; Pro 21:24 |
| Enemies' anger, as the attacked bear it | U, 2R, 3S, 4W, 5P | 14 / 11 | 1–5 | Psa 124:3; Isa 7:4; Isa 51:13; Heb 11:27 |
| Vexation and grief borne within | 3Y, 4X | 12 / 11 | 3, 4 | 1Sa 1:16; Psa 6:7; Ecc 2:23; Ecc 11:10 |
| Provoked between people; provoking to anger or to love | 3X, 5Y | 10 / 9 | 3, 5 | 1Sa 1:6; Pro 27:3; Col 3:21; Heb 10:24 |
| At what God does; turned against God | Y, 3T, 4T | 8 / 8 | 1, 3, 4 | Num 11:10; 2Sa 6:8; Jon 4:1; Isa 8:21; Pro 19:3 |
| God asks the angry one; a man invited to pour it out | 3U, Z | 5 / 4 | 1, 3 | Gen 4:6; Jon 4:4, 9; Job 40:11 |
| With God's Spirit | S, 3Q | 4 / 2 | 1, 3 | Judg 14:19; 1Sa 11:6 |
| "Fret not yourself" | 3W | 4 / 4 | 3 | Psa 37:1, 7–8; Pro 24:19 |
| The fool's vexation | 3Z | 4 / 3 | 3 | Pro 12:16; Ecc 7:9; Job 5:2 |
| At an order not kept | 4Q | 4 / 4 | 4 | Exo 16:20; Lev 10:16; 2Ki 13:19 |
| Against one suspected or set against | 4S | 4 / 4 | 4 | 1Sa 29:4; Est 2:21; Jer 37:15; Dan 11:30 |
| Hostility forbidden and taken up | 4AA | 4 / 4 | 4 | Deu 2:9; Exo 23:22 |
| Angry with oneself | 3V | 1 / 1 | 3 | Gen 45:5 |
| Wrath poured on a neighbour as a drink | 2T | 1 / 1 | 2 | Hab 2:15 |

### B.7 One word, several parties

| Form | Faces | Hits / verses | Unit | Key verses |
|---|---|---|---|---|
| Venom and poison: the wicked, God's creatures, the Almighty's arrows (the same word as wrath) | 2I | 6 / 5 | 2 | Psa 58:4; Psa 140:3; Job 6:4 |
| The face that falls: Cain's anger; God's withheld anger | 4AE | 4 / 2 | 4 | Gen 4:5; Jer 3:12 |
| Man's wrath and the remnant of wrath, in one verse | 2V | 2 / 1 | 2 | Psa 76:10 |

### B.8 No anger in the verse (data, accounted for)

2W heat itself (4), 3AA (2), 4AB troubled and downcast faces (5), 4AC lament, *qînāh* (18), 4AD storm, sea, smoke, twig, splinter, boundary (12), 5AA hot and cold (3), 5AB the passion of Babylon's wine (2). **46 hits in 43 verses.** These are tagged as anger words, but the verse has no anger in it (§E; *qînāh* is a cross-cluster association, #1970).

**What the counts show (S, by count):**
- **Four forms occur in all five units:** God's anger with his people or with those who do wrong (144); its being carried out by agents (20); the ruler's anger (31); and enemies' anger as the attacked bear it (14).
- **The largest forms are** God's anger with his people (144), on the nations (68), lament and prayer under it (55), the provocation of God (52) and acting to turn it away (36). Between them they hold 355 of the 919 hits.
- **God's anger and the parties around it (B.1–B.4) hold 585 hits; people's own anger (B.6) holds 269.** God is the one who is angry in 354.
- **Forms found in one unit only follow its words:** the cup and venom (*ḥēmāh*), provocation of God and vexation (*kāʿas*), the set end and the instrument (*qeṣep̄*, *zaʿam*), strife (*mᵉḏân*, *eris*), and Jesus, the master and the devil (Greek).

---

## C. What influences its nature (change of character, #1919)

These are the factors from the five §C tables, merged. A factor that appears in more than one unit is joined only where the verses name it the same way. **The wording of each factor is mine (R).** Basis applies to the verses.

| # | Factor | What the verses state | Verses | Units | basis |
|---|---|---|---|---|---|
| 1 | **Who is angry** | The same words for God and people; some words kept for God (part A). In restraint God sets himself against a man: "for I am God and not a man" | Hos 11:9; part A | 1–5 | S |
| 2 | **What sets it off** | God and people both: "when the Lord heard it, his anger was kindled"; "As soon as his master heard the words"; a sight: "when Haman saw Mordecai"; a refusal: "But Queen Vashti refused to come"; "Behold, I thought that he would surely come out to me"; news and alarm: "news from the east and the north shall alarm him, and he shall go out with great fury" | Num 11:1; Gen 39:19; Est 5:9; Est 1:12; 2Ki 5:11; Dan 11:44 | 1–5 | S |
| 3 | **Whether what sets it off is true** | Potiphar's anger rises on his wife's report, untested; the officials rage at Jeremiah's "It is a lie; I am not deserting"; the disciples' "Why this waste?" is answered "she has done a beautiful thing to me" | Gen 39:19; Jer 37:14–15; Mat 26:8–10 | 1, 4, 5 | S |
| 4 | **For whom, and against whom the bond is defended** | For the widow and fatherless: "my wrath will burn"; jealous wrath against Jerusalem ("the blood of wrath and jealousy") and for Zion ("I am jealous for her with great wrath"); Jesus "was indignant" for the children | Exo 22:24; Eze 16:38; Zec 8:2; Mar 10:14 | 1, 2, 5 | S |
| 5 | **What it is joined with in the verse** | Jealousy (Deu 6:15); grief: Jonathan "was grieved for David", Jesus "looked around at them with anger, grieved at their hardness of heart"; the Spirit (1Sa 11:6); "the anger and envy that you showed because of your hatred" (Eze 35:11); fear: "he shall be afraid and withdraw, and shall turn back and be enraged"; compassion set against it (Hos 11:8–9) | Deu 6:15; 1Sa 20:34; Mar 3:5; 1Sa 11:6; Eze 35:11; Dan 11:30; Hos 11:8–9 | 1–5 | S |
| 6 | **Time** | God's: "For his anger is but for a moment"; "in a very little while my fury will come to an end"; "the wrath of God is finished"; "the wrath of God remains on him". A man's: Edom "kept his wrath forever"; "until your brother's anger turns away from you, and he forgets"; "do not let the sun go down on your anger" | Psa 30:5; Isa 10:25; Rev 15:1; Joh 3:36; Amo 1:11; Gen 27:45; Eph 4:26 | 1–5 | S |
| 7 | **The answer it meets** | "A soft answer turns away wrath"; "A gift in secret averts anger"; Moses' plea; "when he humbled himself the wrath of the Lord turned from him"; Aaron's reason, "And when Moses heard that, he approved"; Naaman's servants; "His father came out and entreated him"; Jesus called the ten; Gamaliel's counsel. Or none: "I sought for a man … but I found none"; "I looked, but there was no one to help" | Pro 15:1; Pro 21:14; Exo 32:11–12; 2Ch 12:12; Lev 10:20; 2Ki 5:13; Luk 15:28; Mat 20:25; Act 5:34–35; Eze 22:30; Isa 63:5 | 1–5 | S |
| 8 | **The stated reason for God's restraint** | "being compassionate"; "I acted for the sake of my name, that it should not be profaned in the sight of the nations"; "had I not feared provocation by the enemy"; "for the spirit would grow faint before me"; "for I am merciful"; "They have humbled themselves. I will not destroy them" | Psa 78:38; Eze 20:9; Deu 32:27; Isa 57:16; Jer 3:12; 2Ch 12:7 | 1–4 | S |
| 9 | **Power** | The ruler's anger is followed at once by a command: custody, a decree, destruction, killing. "A king's wrath is like the growling of a lion" | Gen 40:2–3; Est 1:12; Dan 2:12; Mat 2:16; Pro 19:12 | 1–5 | S |
| 10 | **The one who carries it out** | "Woe to Assyria, the rod of my anger … but it is in his heart to destroy"; "you showed them no mercy"; "while I was angry but a little, they furthered the disaster"; "you have killed them in a rage that has reached up to heaven"; Saul judged for not carrying it out | Isa 10:5, 7; Isa 47:6; Zec 1:15; 2Ch 28:9; 1Sa 28:18 | 1–4 | S |
| 11 | **One and many** | "shall one man sin, and will you be angry with all the congregation?"; Achan's act and the people's breach; Hezekiah's proud heart and "wrath came upon him and Judah and Jerusalem" | Num 16:22; Jos 7:1; 2Ch 32:25 | 1, 4 | S |
| 12 | **What the angry person does with it** | Nehemiah: "I took counsel with myself"; Absalom "spoke to Amnon neither good nor bad"; Jacob's sons answered "deceitfully"; Samuel "cried to the Lord all night"; David "was afraid of the Lord that day"; Sanballat and Tobiah "plotted together"; Ahab "lay down on his bed and turned away his face"; Paul "reasoned in the synagogue" | Neh 5:7; 2Sa 13:22; Gen 34:13; 1Sa 15:11; 2Sa 6:9; Neh 4:8; 1Ki 21:4; Act 17:17 | 3–5 | S |
| 13 | **Who speaks to it** | God asks: "Why are you angry, and why has your face fallen?"; "Do you do well to be angry?"; Joseph: "do not be distressed or angry with yourselves"; "Fret not yourself"; "Be angry and do not sin" | Gen 4:6; Jon 4:4; Gen 45:5; Psa 37:8; Eph 4:26 | 1, 3, 5 | S |
| 14 | **Where it sits in the person** | "his anger burned within him"; "in the heat of my spirit"; "my spirit drinks their poison"; "my eye is wasted from grief; my soul and my body also"; "anger lodges in the heart of fools"; "his spirit was provoked within him"; "his heart rages against the Lord" | Est 1:12; Eze 3:14; Job 6:4; Psa 31:9; Ecc 7:9; Act 17:16; Pro 19:3 | 2–5 | S |
| 15 | **The same words in different settings** | One storm sentence among the false prophets and among the promises (Jer 23:19 = 30:23); the Exodus "a mighty hand and an outstretched arm" with "wrath poured out" added, aimed at Israel; provocation as threat and as a question inside a lament ("Why have they provoked me to anger with their carved images"); *kaʿas* as what "kills the fool" and as the "Sorrow" that "is better than laughter" | Jer 23:19; Jer 30:23; Eze 20:33–34; 1Ki 16:2; Jer 8:19; Job 5:2; Ecc 7:3 | 2, 3 | S |
| 16 | **The same phrase, the speaker's purpose** | "slow to anger": God's proclaimed name, Moses' plea, Joel's call to return, Nahum's warning, Jonah's complaint, the wise man's virtue | Exo 34:6; Num 14:18; Joe 2:13; Nah 1:3; Jon 4:2; Pro 14:29 | 1 | S |
| 17 | **One root, different things** | *ʾaph*: "pressing the nose produces blood, and pressing anger produces strife"; *ḥēmāh*: wrath, "the venom of asps", "the heat of wine"; *ʿebrāh*: wrath and "arrogant pride"; *zāʿam*: anger and "How can I denounce"; *zāʿap̄*: Uzziah's anger and "Why are your faces downcast today?"; *ʿāšan*: "Mount Sinai was wrapped in smoke" and "Why does your anger smoke"; *kāʿas*: provoking God and Hannah's "vexation"; *thymos*: God's "wrath" and Babylon's "passion"; *paroxysmos*: "a sharp disagreement" and "stir up one another to love" | Pro 30:33; Psa 140:3; Hos 7:5; Pro 21:24; Num 23:8; 2Ch 26:19; Gen 40:7; Exo 19:18; Psa 74:1; Deu 4:25; 1Sa 1:16; Rev 14:8, 10; Act 15:39; Heb 10:24 | 1–5 | S (the renderings); the link across them R (lexical) |
| 18 | **Who else is in the scene** | an intercessor (Exo 32:11); an onlooker whose gladness bears on it (Pro 24:18); a prophet sent with a question (2Ch 25:15); an angel who asks "how long" (Zec 1:12); destroying angels (Psa 78:49); the created world (Jer 7:20); brothers who "exhort one another every day" (Heb 3:13); the authority, "an avenger who carries out God's wrath" (Rom 13:4) | Exo 32:11; Pro 24:18; 2Ch 25:15; Zec 1:12; Psa 78:49; Jer 7:20; Heb 3:13; Rom 13:4 | 1–5 | S |
| 19 | **Correction with or without the anger** | "I myself will discipline you sevenfold for your sins", "in fury"; against it: "rebuke me not in your anger, nor discipline me in your wrath"; "Correct me, O Lord, but in justice; not in your anger" | Lev 26:28; Psa 6:1; Jer 10:24 | 1, 2 | S |
| 20 | **The measure** | "to increase still more the fierce anger of the Lord"; "Ahab did more to provoke the Lord … than all the kings"; "storing up wrath for yourself"; "so as always to fill up the measure of their sins" is the setting of "wrath has come upon them at last" | Num 32:14; 1Ki 16:33; Rom 2:5; 1Th 2:16 | 1, 3, 5 | S |

**What this shows (R):** the factors fall into three kinds, and the verses name each:
- **who is angry, at whom, and for whom** (#1, #4, #9, #10, #11, #18)
- **what sets it off, and what meets it** (#2, #3, #5, #7, #8, #12, #13, #19, #20)
- **how long it lasts, where it sits, and how the words are used** (#6, #14–17)

The arrangement into three kinds is mine. The factors are not.

---

## D. What anger leads to

Each outcome is stated by its verse. God's anger and a person's anger are listed apart, because the verses name different outcomes for each; where the same outcome is named on both sides, it is said.

### D.1 God's anger

| Outcome | What the verses state | Verses | Units |
|---|---|---|---|
| Giving over | "and he gave them over to plunderers"; "he gave them into the hand of the nations" | Judg 2:14; Psa 106:41 | 1, 3 |
| The land and the harvest | "he will shut up the heavens, so that there will be no rain"; "They shall be ashamed of their harvests because of the fierce anger of the Lord" | Deu 11:17; Jer 12:13 | 1, 3 |
| Presence withdrawn; no hearing | "and he departed. When the cloud removed from over the tent"; "though they cry in my ears with a loud voice, I will not hear them"; "As I called, and they would not hear, so they called, and I would not hear" | Num 12:9–10; Eze 8:18; Zec 7:13 | 2–4 |
| People turning on each other | "the people are like fuel for the fire; no one spares another" | Isa 9:19 | 4 |
| Ordinary joy, grief and courage stopped | "Let not the buyer rejoice, nor the seller mourn, for wrath is upon all their multitude"; "none goes to battle" | Eze 7:12, 14 | 3 |
| Terror | "terrify them in his fury"; "The Assyrians will be terror-stricken at the voice of the Lord" | Psa 2:5; Isa 30:31 | 1, 4 |
| Knowing; understanding later; not taken to heart | "And they shall know that I am the Lord"; "In the latter days you will understand it clearly"; "it burned him up, but he did not take it to heart" | Eze 5:13; Jer 23:20; Isa 42:25 | 1, 2 |
| A request for wisdom | "So teach us to number our days that we may get a heart of wisdom" | Psa 90:12 | 1 |
| Calm, after | "I will be calm and will no more be angry" | Eze 16:42 | 2 |
| Comfort, healing, gathering, after | "your anger turned away, that you might comfort me"; "I will heal their apostasy; I will love them freely, for my anger has turned from them"; "I will gather them … and I will make them dwell in safety" | Isa 12:1; Hos 14:4; Jer 32:37 | 1, 2, 4 |
| Borne in the body and in company | "There is no soundness in my flesh"; "I eat ashes like bread and mingle tears with my drink"; "You have caused my companions to shun me"; "I sat alone, because your hand was upon me" | Psa 38:3; Psa 102:9–10; Psa 88:8; Jer 15:17 | 2, 4 |
| Fear moving the intercessor | "For I was afraid of the anger and hot displeasure … But the Lord listened to me that time also" | Deu 9:19 | 1, 2, 4 |
| Shame for those who burn against God and his people | "all who are incensed against you shall be put to shame and confounded" | Isa 41:11 | 3 |
| The heart's joy for those it acts for | "You shall see, and your heart shall rejoice … he shall show his indignation against his enemies" | Isa 66:14 | 4 |

### D.2 A person's anger

| Outcome | What the verses state | Verses | Units |
|---|---|---|---|
| An act at once, with the hand | Moses "threw the tablets out of his hands and broke them"; Balaam "struck the donkey with his staff"; Bigthan and Teresh "sought to lay hands on King Ahasuerus" | Exo 32:19; Num 22:27; Est 2:21 | 1, 4 |
| A command, where the angry one has power | "and he put them in custody"; "commanded that all the wise men of Babylon be destroyed"; Herod "sent and killed all the male children in Bethlehem" | Gen 40:2–3; Dan 2:12; Mat 2:16 | 4, 5 |
| Killing | "For in their anger they killed men"; Cain "rose up against his brother Abel and killed him" follows "Why are you angry"; at Stephen, "they cried out with a loud voice and stopped their ears and rushed together at him" | Gen 49:6; Gen 4:6–8; Act 7:57 | 1, 3, 5 |
| A face that falls; an eye that watches; a plot | "and his face fell"; "And Saul eyed David from that day on"; "And they all plotted together" | Gen 4:5; 1Sa 18:9; Neh 4:8 | 3 |
| Strife | "A hot-tempered man stirs up strife"; "pressing anger produces strife"; "one given to anger causes much transgression" | Pro 15:18; Pro 30:33; Pro 29:22 | 1, 2 |
| Folly, evil, a snare | "A man of quick temper acts foolishly"; "Fret not yourself; it tends only to evil"; "lest you learn his ways and entangle yourself in a snare" | Pro 14:17; Psa 37:8; Pro 22:25 | 1 |
| Withdrawal into the body | Hannah "wept and would not eat"; Ahab "lay down on his bed and turned away his face and would eat no food"; Jonathan "ate no food the second day of the month" | 1Sa 1:7; 1Ki 21:4; 1Sa 20:34 | 1, 3, 4 |
| Fear; prayer | "And David was afraid of the Lord that day"; "And Samuel was angry, and he cried to the Lord all night" | 2Sa 6:9; 1Sa 15:11 | 3 |
| Counsel, then open charge; reasoning | "I took counsel with myself, and I brought charges against the nobles"; "So he reasoned in the synagogue" | Neh 5:7; Act 17:17 | 3, 5 |
| Staying outside | "But he was angry and refused to go in" | Luk 15:28 | 5 |
| Rash words | "they made his spirit bitter, and he spoke rashly with his lips"; "therefore my words have been rash" | Psa 106:33; Job 6:3 | 3, 4 |
| Discouragement in another | "Fathers, do not provoke your children, lest they become discouraged" | Col 3:21 | 5 |
| Separation | "And there arose a sharp disagreement, so that they separated from each other" | Act 15:39 | 5 |
| An opening for the devil | "do not let the sun go down on your anger, and give no opportunity to the devil" | Eph 4:26–27 | 5 |
| Not the righteousness of God; judgment | "for the anger of man does not produce the righteousness of God"; "everyone who is angry with his brother will be liable to judgment" | Jam 1:20; Mat 5:22 | 5 |
| Shame, for the incensed | "to him shall come and be ashamed all who were incensed against him" | Isa 45:24 | 3 |
| Leprosy in the act | "when he became angry with the priests, leprosy broke out on his forehead" | 2Ch 26:19 | 4 |

**Where the same outcome is named on both sides (S):** terror or fear (Psa 2:5; 2Sa 6:9), shame (Jer 12:13; Isa 45:24), and the body (Psa 38:3; 1Ki 21:4). I list them; no verse draws the parallel.

---

## E. Held, and not used here

- **Life and death (OT-08):** the death sides of AG-05 (Sheol), AG-14, AG-25, AG-27, AG-37, AG-38, AG-39, AG-58 (unit 1); AG-87 (Psa 90), AG-94 (Pro 16:14), AG-101 (Lam 5:10) (unit 2); AG-116 (Psa 88:15–16), AG-143, AG-144 (Ecc 7:2), AG-145 (Job 5:2) (unit 3); AG-155, AG-157, AG-160 ("between the dead and the living", Num 16:48), AG-163, AG-171, AG-175, AG-182 (Pro 20:2), AG-190 (unit 4); AG-201, AG-206 (Heb 3:17), AG-209, AG-214, AG-228 (Act 12:23), AG-233, AG-235 (unit 5). Not reopened (#1943, #1948).
- **Source not named:** AG-198 (2Ki 3:27, "there came great wrath against Israel"), held (AN-H4).
- **Speaker named, not Scripture's own statement:** the friends' explanations of suffering by God's anger (Eliphaz, Zophar, Elihu: AG-42), under God's verdict "you have not spoken of me what is right" (Job 42:7). Job's "my adversary" (Job 16:9, AG-44) is held beside the same verdict, unreconciled.
- **Data only:** B.8 (46 hits); AG-146, AG-197.
- **OT-15 (the heat family outside the tag) comes back here** by its own trigger ("the anger cross-ledger overview"). *ḥāmam* (H2552, 21 hits, tagged T3) was not read by any unit (focused capture). This overview reads only the ledgers, as the fear overview did, so it is **not read here**. Whether to read it as a short addendum before 10.13 is a choice for the researcher (§J).

---

## F. Anger and the other characteristics

**Two senses, kept apart (as in the fear overview §F):**
1. **In the data:** M02 words share verses with **75 other M-clusters**, and with **27 of them in 20 or more verses** (`anger-cooccurrence-v1-20261005.py`: every tagged word in the 681 M02 verses; "near" = within 3 words of an M02 hit). This is co-occurrence of tags. It points to verses to read; it is not a relation in itself (#1919). Some high counts are tagging: M72 (authority) is mostly "king", "hand", "master"; M43 (prophecy) is mostly "declares".
2. **In the verses:** anger is joined by the wording itself to other characteristics. The rows below give only joins stated in the ledgers' verses.

**Ways the verses join anger to another characteristic** (the forms are grammatical, so S; naming them is R):
- **one leading to another:** "so", "therefore", "lest", "because"
- **set against with "but":** "A soft answer turns away wrath, but a harsh word stirs up anger" (Pro 15:1)
- **named together** in one breath or list: "the anger and envy that you showed" (Eze 35:11); "with anger, grieved at their hardness of heart" (Mar 3:5)
- **the same root, rendered as another characteristic:** *ʿebrāh* as pride; *kaʿas* as grief and sorrow; *paroxysmos* as stirring to love

| Characteristic (M-code) | Verses shared / near | How the verses join it to anger | Verses | Ledger ids |
|---|---|---|---|---|
| Inner seat (M47) | 66 / 27 | Anger answers a heart turned; burns within; the heat of the spirit; a hard heart stores up wrath; anger lodges in the heart of fools | 1Ki 11:9; Est 1:12; Eze 3:14; Rom 2:5; Ecc 7:9 | AG-16, 93, 91, 200, 145 |
| Wickedness (M58); sin (M56) | 73 / 34; 49 / 23 | The cause named before the anger: "because of the evil of your deeds"; "Fret not yourself; it tends only to evil"; "one given to anger causes much transgression" | Jer 4:4; Psa 37:8; Pro 29:22 | AG-62, 53, 51 |
| Desire, jealousy, envy (M18) | 59 / 33 | Jealousy named with God's anger; "jealousy makes a man furious"; "the anger and envy that you showed because of your hatred"; "You covet and cannot obtain, so you fight and quarrel" | Deu 6:15; Pro 6:34; Eze 35:11; Jam 4:2 | AG-04, 74, 54, 237 |
| Knowing (M15); being heard (M41) | 55 / 24; 39 / 8 | Kindled on hearing; its stated end is knowing ("they shall know that I am the Lord"); understanding "in the latter days"; the book heard and the wrath recognised; ears stopped | Num 11:1; Eze 5:13; Jer 23:20; 2Ki 22:13; Act 7:57 | AG-03, 07, 31, 89, 227 |
| Speech and tongue (M65) | 48 / 20 | A harsh word stirs it; speech about God answered with anger; rash words from an embittered spirit; "slow to speak, slow to anger"; slander and obscene talk in the lists | Pro 15:1; Job 42:7; Psa 106:33; Jam 1:19; Col 3:8 | AG-52, 18, 181, 224, 222 |
| Faintness (M24); discouragement (M20) | 48 / 25; 12 / 7 | "Your sons have fainted … full of the wrath of the Lord"; "for the spirit would grow faint before me"; "lest they become discouraged" | Isa 51:20; Isa 57:16; Col 3:21 | AG-82, 163, 239 |
| Violence (M10) | 43 / 24 | "For in their anger they killed men"; "killed them in a rage that has reached up to heaven"; Herod's killing at Bethlehem | Gen 49:6; 2Ch 28:9; Mat 2:16 | AG-53, 92, 228 |
| Rebellion (M30) | 42 / 18 | "because you rebelled against my command at the waters of Meribah"; "do not harden your hearts as in the rebellion" | Num 20:24; Heb 3:8 | AG-181, 206 |
| Malice and enmity (M06) | 39 / 21 | Hatred named as the source of anger and envy; Job reads the anger as being hated; malice beside anger in the lists | Eze 35:11; Job 16:9; Eph 4:31 | AG-54, 44, 222 |
| Fear (M01) | 35 / 12 | Moses afraid of the anger, and heard; afraid, then enraged; angry, then afraid; "do not fear" at another's fierce anger; "not being afraid of the anger of the king"; indignation and fear in one verse | Deu 9:19; Dan 11:30; 2Sa 6:8–9; Isa 7:4; Heb 11:27; 2Cor 7:11 | AG-33, 86, 185, 137, 57, 229, 235 |
| Wisdom and folly (M16) | 32 / 17 | "Whoever is slow to anger has great understanding"; "A man of quick temper acts foolishly"; folly ruins a man's way and "his heart rages against the Lord"; "a heart of wisdom" asked under the anger | Pro 14:29; Pro 14:17; Pro 19:3; Psa 90:12 | AG-51, 186, 37 |
| Prayer (M42) | 31 / 11 | "how long will you be angry with your people's prayers?"; Samuel "cried to the Lord all night"; "lifting holy hands without anger" | Psa 80:4; 1Sa 15:11; 1Ti 2:8 | AG-176, 137, 226 |
| Grief and lament (M03) | 25 / 15 | "grieved for David"; "with anger, grieved at their hardness of heart"; a lament raised for "the generation of his wrath"; the provocation asked about inside a lament; godly grief produced indignation; *kaʿas* rendered "grief" | 1Sa 20:34; Mar 3:5; Jer 7:29; Jer 8:19; 2Cor 7:11; Psa 6:7 | AG-55, 218, 196, 125, 235, 143 |
| Grace and mercy (M50); kindness (M05) | 21 / 13; 21 / 9 | "being compassionate … he restrained his anger often"; "merciful and gracious, slow to anger"; "for I am merciful"; "But God, being rich in mercy"; "should not you have had mercy"; "Be kind to one another" | Psa 78:38; Exo 34:6; Jer 3:12; Eph 2:4; Mat 18:33; Eph 4:32 | AG-28, 32, 194, 209, 220, 222 |
| Pride (M08) | 20 / 11 | "his heart was proud. Therefore wrath came upon him"; "look on everyone who is proud and abase him"; *ʿebrāh* rendered "arrogant pride" | 2Ch 32:25; Job 40:11; Pro 21:24 | AG-158, 59, 188 |
| Rest and peace (M33) | 20 / 13 | "Therefore I swore in my wrath, 'They shall not enter my rest'"; Tyre and Sidon "asked for peace"; "let them make peace with me" | Psa 95:11; Act 12:20; Isa 27:5 | AG-11, 206, 228, 80 |
| Turning and repentance (M11) | 19 / 10 | "Who knows? God may turn and relent"; "when he humbled himself the wrath of the Lord turned from him"; "Bear fruit in keeping with repentance"; godly grief "produces a repentance" | Jon 3:9; 2Ch 12:12; Mat 3:8; 2Cor 7:10 | AG-46, 45, 207, 235 |
| Shame (M07) | 17 / 5 | "They shall be ashamed of their harvests because of the fierce anger"; the provocation is "to their own shame"; the incensed "put to shame"; Ezra "ashamed to ask the king" | Jer 12:13; Jer 7:19; Isa 41:11; Ezr 8:22 | AG-105, 124, 136, 43 |
| Memory (M81) | 15 / 5 | "Remember and do not forget how you provoked the Lord your God to wrath"; "Because you have not remembered the days of your youth, but have enraged me"; when the anger abated "he remembered Vashti"; "God remembered Babylon" | Deu 9:7; Eze 16:43; Est 2:1; Rev 16:19 | AG-154, 76, 77, 215 |
| Patience (M34) | 11 / 7 | "With patience a ruler may be persuaded" (the same *ʾaph*); God "has endured with much patience vessels of wrath"; "Be still before the Lord and wait patiently for him" beside "Refrain from anger" | Pro 25:15; Rom 9:22; Psa 37:7–8 | AG-51, 210, 53 |
| Authority (M72) | 100 / 46 | Mostly tagging (king, hand, master). In the verses: the ruler's anger becomes a command; "A king's wrath is like the growling of a lion"; the authority carries out God's wrath | Dan 2:12; Pro 19:12; Rom 13:4 | AG-182, 212 |
| Life and death (M25) | 36 / 17 | "the wrath of God remains on him"; "A king's wrath is a messenger of death"; "angry enough to die"; **held** (OT-08) | Joh 3:36; Pro 16:14; Jon 4:9 | AG-201, 94, 138 |

**What this answers (R):** anger does not stand alone in these verses. In the wording itself it is set off by hearing and seeing, named with jealousy, envy, hatred, grief and fear, set against mercy, patience and a soft answer, and restrained for reasons the verses give (compassion, his name, the spirit that would faint). What it leads to (§D) runs mostly into other characteristics: strife, violence, folly, shame, fear, prayer, knowing.

**Limits (R):**
- the counts are tag-based, from the live tags on 2026-10-05
- a joining verse is listed by what it says; its own word may carry another tag (for example "afraid" in Dan 11:30 is tagged M20, and "jealous" in Deu 6:15 is M18)
- no characteristic is said to cause another unless the verse says "so", "therefore", "lest" or "because"
- each touch is recorded from the anger side only; the other strand's side is read when that strand is explored (#1900)
- **anger and fear, from both sides:** the fear overview §F has the fear side (*rāgaz*, to tremble, rendered "Be angry" in Psa 4:4; Psa 90:11; 1Sa 18:29). This row is the anger side. The two meet at Deu 9:19, Psa 90:11, Dan 11:30 and Heb 11:27.

---

## G. Chains the verses state (#1946)

Each unit's §G lists every stated link, with its verse (about 230 in all). They are not repeated here. Below they are **arranged by what the link is about (R)**, with examples; each link is stated in its verse.

| Kind of link (R) | Stated examples | Units |
|---|---|---|
| **What sets God's anger off** | broke the covenant → anger → given over (Judg 2:14, 20); heard → anger → fire (Num 11:1); hearts diamond-hard, lest they hear → therefore great anger (Zec 7:12); blood left uncovered → wrath roused (Eze 24:8); mocking the messengers → wrath rose → no remedy (2Ch 36:16); proud heart → wrath came (2Ch 32:25); suppress the truth → wrath revealed (Rom 1:18) | 1–5 |
| **What sets a person's anger off** | demand → anger → "Am I in the place of God" (Gen 30:1–2); no regard → very angry → face fell (Gen 4:5); saw no homage → filled with fury → sought to destroy all the Jews (Est 3:5–6); "I thought" → rage (2Ki 5:11–12); afraid → withdraw → enraged (Dan 11:30); heard → filled with wrath → drove him out (Luk 4:28–29); passions at war within → quarrels (Jam 4:1) | 1–5 |
| **What turns or ends God's anger** | humbled → wrath turned (2Ch 12:12); Moses prayed → the Lord listened (Deu 9:19); stood in the breach → wrath turned (Psa 106:23); atonement → stood between → plague stopped (Num 16:46–48); jealous with my jealousy → wrath turned back (Num 25:11); wrath satisfied → calm, no more angry (Eze 16:42); with the last plagues → the wrath is finished (Rev 15:1) | 1, 2, 4, 5 |
| **What restrains it, by the verse's reason** | compassionate → did not stir up all his wrath (Psa 78:38); "I said I would pour out my wrath" → acted for my name (Eze 20:8–9); heart recoils → will not execute burning anger, for I am God and not a man (Hos 11:8–9); not always angry, for the spirit would grow faint (Isa 57:16); feared the enemy's provocation → not wiped out (Deu 32:26–27) | 1–4 |
| **What does not turn it** | godless, folly spoken → anger not turned (Isa 9:17); Manasseh's provocations → did not turn from the burning (2Ki 23:26); sought a man to stand in the breach → found none → poured out my indignation (Eze 22:30–31) | 1, 3, 4 |
| **What follows its end** | anger turned → comfort (Isa 12:1); drove them in wrath → gather, bring back, dwell in safety (Jer 32:37); anger abated → he remembered (Est 2:1); "how long … angry these seventy years?" → gracious and comforting words (Zec 1:12–13) | 1, 2, 4 |
| **What a person's anger leads to** | heard → anger → broke the tablets (Exo 32:19); angry → put them in custody (Gen 40:2–3); company of the angry → learning his ways → a snare (Pro 22:24–25); fret → tends only to evil (Psa 37:8); angry → afraid (2Sa 6:8–9); angry → cried to the Lord all night (1Sa 15:11); Naboth's word → vexed and sullen → would eat no food (1Ki 21:4); provoke your children → lest they become discouraged (Col 3:21) | 1–5 |
| **What turns or settles a person's anger** | soft answer → wrath turned (Pro 15:1); good sense → slow to anger (Pro 19:11); Aaron's answer → Moses heard → approved (Lev 10:16–20); servants' question → dipped → flesh restored (2Ki 5:13–14); poured out her soul, "Go in peace" → ate, face no longer sad (1Sa 1:15–18); sold me → angry with yourselves → do not, for God sent me (Gen 45:5); remember your brother has something against you → first be reconciled (Mat 5:23–24) | 1, 3–5 |
| **What the one who carries it out adds** | gave them into your hand → you showed no mercy (Isa 47:6); angry but a little → they furthered the disaster → exceedingly angry with them (Zec 1:15); killed in a rage → "Have you not sins of your own?" (2Ch 28:9–10); did not carry out → "the Lord has done this thing to you" (1Sa 28:18) | 1, 3, 4 |
| **Anger answered in kind** | no god, idols → provoked → "I will … provoke them" (Deu 32:21); pours wrath on neighbours → the Lord's cup comes around to you (Hab 2:15–16); they would not hear → I would not hear (Zec 7:13) | 2–4 |

No chain above is built from two verses that do not join themselves (rule 69).

---

## H. What emerged, and what it changes (#1945)

The five §F tables, gathered. Each item names the unit row it comes from. **Proposed, nothing woven.**

| # | What emerged | What it changes elsewhere | From |
|---|---|---|---|
| H.1 | **The vocabulary divides by party.** Some words are God's almost every time (*ḥārôn*, *zaʿam*, *qeṣep̄*, *orgē*); others are shared or mostly people's (*ḥārāh*, *qāṣap̄*, *zāʿap̄*, *thymos*, *orgizō*). | No chapter says this. 10.13 can say which words the verses keep for God's anger and which they share (part A). | U3 F.1; U4 F.1; U5 F.1 |
| H.2 | **The same order, heard or seen → anger → act, is stated for God and for people.** | Ch 13 treats God's anger from the bearer's side only; 10.1 treats human anger as a feeling. Supports writing 10.13 by what sets anger off, across parties (OT-13, OT-12). | U1 F.1 |
| H.3 | **The word's own pictures:** kindled, burning, poured, drunk from a cup, venom, smoke, a storm, a weight heavier than sand; and in the narrative it *goes out* and *comes upon*; in the Greek it is *revealed*, *stored up*, *remains*, *finished*. | 10.13 should describe anger in these pictures, not only as a state. Ch 13 has the fire and lacks the cup. | U2 F.1, F.3; U3 F.9; U4 F.2; U5 F.2, F.9 |
| H.4 | **God's heart is named with his anger three times:** "My heart recoils within me" before "I will not execute my burning anger" (Hos 11:8–9); "the intents of his heart" (Jer 23:20); "the day of vengeance was in my heart, and my year of redemption had come" (Isa 63:4). | Confirms and extends #1890. **RS** for the Ch 13 cross-check (OT-13). | U1 F.2; U2 F.2 |
| H.5 | **"Slow to anger" is one phrase** (Exo 34:6; Pro 14:29): God's proclaimed name, used by many speakers to different ends, and the wise man's virtue. | 10.9 holds the God-side uses; 10.1, 06, 11 the human ones. **NS:** one account in 10.13. | U1 F.3 |
| H.6 | **The parties around God's anger, in both Testaments:** intercessors heard and not heard; one who stands between; no one found for the breach; an angel who asks; agents and instruments with hearts of their own, charged for their excess; onlookers; John who warns; the Son who delivers; the authority; brothers who exhort one another; the one it rescues, who sings of it. | **NS** for 10.13: a part that follows the parties (ruling 6.2). | U1 F.4; U3 F.8; U4 F.3, F.4; U5 F.3 |
| H.7 | **A spirit as the angry party:** the devil's great wrath "because he knows that his time is short" (Rev 12:12). | Not in the chapters. **NS** for 10.13. | U5 F.4 |
| H.8 | **How God meets a person's anger: by asking.** "Why are you angry?" (Gen 4:6); "Do you do well to be angry?" (Jon 4:4); and the face that falls is Cain's anger and God's withheld anger, "for I am merciful" (Jer 3:12). | Each is in the chapters alone. **NS** for 10.13 (the pairing). | U3 F.4; U4 F.10 |
| H.9 | **What meets a person's anger decides its end:** an answer heard, a servants' question, a father who comes out, a teaching on serving, a counsellor; or leprosy, or the bed and no food. | For 10.13's account of what anger leads to (part D). | U3 F.5; U4 F.6; U5 F.6 |
| H.10 | **One root for provoking God and for Hannah's vexation** (*kāʿas/kaʿas*). | 10.1 and 11 hold the human side, Ch 13 the God side. Neither shows they are one word. **RS** candidate; #1947 appendix. | U3 F.2 |
| H.11 | **The provocation is spoken of as between persons:** to his face, behind his back, after being "exalted … out of the dust" (1Ki 16:2), and asked about in grief (Jer 8:19). | **NS** for 10.13: God's anger as relationship, not only cause and penalty. | U3 F.7 |
| H.12 | **The fierce anger is the anger that turns** (*ḥārôn* with "turn" in 12 of 40 verses); Josiah's whole-hearted turning beside the burning not turned (2Ki 23:25–26); turning asked for without a guarantee ("It may be", Jer 36:7; "perhaps", Zep 2:3; "Who knows?", Jon 3:9); inner acts named as turning it (humbling, a resolve in the heart). | Extends Ch 13 *Returning*; 2Ki 23:25–26 and 2Ch 29:10 are new to the narrative. | U1 F.7, F.8; U3 F.3 |
| H.13 | **Time on each side:** God's anger has a stated end ("for a moment", Isa 54:8; "the appointed time of the end", Dan 8:19; "finished", Rev 15:1), and the people are told how to wait (Isa 26:20); a man's anger "kept … forever" (Amo 1:11) is cursed (Gen 49:7). | For 10.13; set side by side, not joined. | U4 F.5; U5 C |
| H.14 | **Restraint has stated reasons, all in God:** compassion, his name before the nations, the spirit that would faint, "for I am merciful" (Jer 3:12), their humbling; and "I have no wrath" of the vineyard he keeps. | Isa 27:4 is new to the narrative (**NS**). | U1 B.4; U2 F.8 |
| H.15 | **The cup:** wrath drunk, staggering, fainting, then taken away and passed to the tormentors; a man's wrath poured as drink, answered by the Lord's cup; Babylon's wine and God's wine side by side. | Not in the chapters. **NS** for 10.13. | U2 F.3; U5 F.9 |
| H.16 | **The ruler's anger and those beneath it:** a command follows at once; the wise appease it; it is "like the growling of a lion" (Pro 19:12). | Not visible in 10.1 as anger with power to command. | U4 F.7 |
| H.17 | **Anger aimed at God:** at what he does (Moses, David, Samuel, Jonah), in hunger, and in folly's ruin, where "his heart rages against the Lord" (Pro 19:3). | For 10.13, part B by party. | U4 F.8 |
| H.18 | **The one praying separates correction from anger**; the covenant text joins them. | Not in the narrative. For 10.13 and 10.8. | U1 F.5; U2 AG-65 |
| H.19 | **The anger's stated outcome is knowing or understanding** ("they shall know that I am the Lord", Eze 5:13; "In the latter days you will understand it clearly", Jer 23:20). | 10.2 does not carry it. Pointer from 10.13 to 10.2. | U1 F.6 |
| H.20 | **Anger named by its absence:** prayer, the overseer, love; and the lists name what replaces it. | For 10.13 (part A). | U5 F.7 |
| H.21 | **Same root, no anger:** *zāʿap̄* as a downcast face, *sāʿar* as a troubled mind, *ʿāšan* as Sinai's smoke, *ʿebrāh* as pride, *zestos* as the heat of works. | **RS:** Ch 11 §4 *Storm* calls 2Ki 6:11 *the angry king's mind*; the verse says "greatly troubled" (appendix). | U4 F.9; U5 AG-240 |
| H.22 | **Cross-cluster associations, no re-tagging (#1970):** *qînāh* (lament) with grief (M03); indignation with grief and fear (2Cor 7:11); provoking with discouragement (Col 3:21); jealousy and envy in the lists (M18); zeal with *zestos*; anger at another's honour with no verse naming envy (Gen 4:5; 1Sa 18:8). | For cross-cluster analysis; part F. | U3 F.6; U4 F.11; U5 F.10 |
| H.23 | **The heat family runs outside the tag** (OT-15). | Reached by this overview; see §E and §J. | U2 F.10 |

---

## I. Appendix: earlier anger placements that cut a verse to fit a heading (#1947, listed, not reworked)

From the five units' §D. Input for the Ch 10 retune (OT-14), and for the Ch 13 cross-check (OT-13). **Nothing here is changed now.**

| # | Where | What the heading did | What the verses show | From |
|---|---|---|---|---|
| I.1 | 10.9 (*relating to God*) and 10.1, 06, 11 | Split "slow to anger" into God-side and human-side uses | One phrase, God's proclaimed name and the wise man's virtue | U1 §D; AG-32, AG-51 |
| I.2 | 10.5 (speaking) | Holds Psa 140:3 for the tongue | The "venom" is the wrath word *ḥēmāh* | U2 §D; AG-85 |
| I.3 | 10.0 (*what comes back*) | Holds Hab 2:15 alone | It belongs with the cup (Isa 51; Jer 25), which is in no chapter | U2 §D; AG-82 to AG-84 |
| I.4 | 10.1 *Feeling* and Ch 13 | Hold *kaʿas* (vexation, grief, "fret") and *kāʿas* (provoking God) in separate places | One root | U3 §D; AG-119, AG-141 |
| I.5 | Ch 13 *How it is provoked* | Names inner roots from other verses; the outward acts *kāʿas* names are there only through Jer 7:18 | The verses name the acts each time | U3 §D; AG-119, AG-120 |
| I.6 | Ch 11 §4 *Storm* | Reads 2Ki 6:11 as *the angry king's mind* | "greatly troubled"; no anger word. **RS**, when Ch 11 is next touched | U4 §D; AG-195 |
| I.7 | 10.1 *Feeling* | Holds people's anger with no sign of the ruler's power to command, or of anger aimed at God | Anger with power to command (AG-182); anger turned against God (AG-186) | U4 §D |
| I.8 | 12 *When the inner being goes wrong* | Holds God's wrath verses (Col 3:6; Eph 2:3; Rom 2:5) beside the human anger lists | Col 3:6–8 sets God's wrath and the anger to be put away in one paragraph | U5 §D; AG-202 |
| I.9 | 10.1 *Feeling* | Holds Jesus's anger (Mar 3:5) and indignation (Mar 10:14) beside the disciples' (Mat 26:8) | One word aimed three ways; the aim is not visible under *Feeling* (OT-12) | U5 §D |

**Chapter overlap (for OT-12 and OT-13), from the five §D counts:** Ch 13 holds 88 of the anger verses cited (36 + 11 + 14 + 19 + 8), 10.1 holds 53 (9 + 8 + 18 + 9 + 9), Ch 11 holds 54 (19 + 8 + 10 + 12 + 5). Units 1–3 undercount a little (Step 2, second note).

---

## J. For the researcher

1. **Approve this overview** (steps 2 and 3; **#1974**). Step 2 found no gap.
2. **OT-15 (#1975):** read *ḥāmam* (H2552, 21 hits) as a short addendum before 10.13, or leave it for a desire (M18) or speaking strand, as the register already allows. My recommendation: **leave it.** It is tagged T3, it was not part of the M02 vocabulary the process fixed, and the verses named in the register (Psa 39:3; Deu 19:6; Isa 57:5) sit with speaking, blood-vengeance and lust as much as with anger.
3. **Next, step 4: 10.13 "Anger"**, its sections taken from this overview, not from the 10.x headings (§3A, #1947). Proposed order, from parts A–D: what the verses say anger is (A, with the word-by-party table) · its forms by party (B) · what changes its nature (C) · what it leads to (D), with the chains (G) inside each. Then the Ch 13 cross-check and consolidation (OT-13). No other chapter reworked (fear precedent).

---

## K. Quote check

`../../cross-cluster-web/fear/fear-quote-check-v1-20261001.py` (unchanged), run on this file in `--prose` mode (each line a unit; the book carried forward to bare references).
- **Result (2026-10-05):** 309 quotes checked, **0 failures**, no missing verse text.
  - The first run had 12 flags, and the second 4 more; all were corrected against iba.db `verse` before this result:
    - one misquote: Isa 10:25 reads "in a very little while", not *for a very little while*
    - one quote moved to the verse with its exact wording: Psa 95:11 reads "Therefore I swore in my wrath" ("As I swore" is Heb 3:11)
    - eleven quotes lacked their verse in the row; the verses are now added (Num 16:48; Job 16:9; 1Ki 16:2; Jer 36:7; Zep 2:3; Jon 3:9; Jer 3:12; and in H.13 Isa 54:8, Dan 8:19, Rev 15:1, Amo 1:11). H.13's *a set time* was my wording; it is now Dan 8:19's "the appointed time of the end"
    - three were my own labels set in quotation marks (the unit 5 cross-reference, *Two wines*, *Feeling*); they are now in italics
  - Nine quotes of Scripture that had no reference in their row (and so were not checked) were given their verses and checked: Pro 15:1; Eze 35:11; Mar 3:5; Rev 12:12; Pro 19:12; Pro 19:3; Eze 5:13; Jer 23:20; Exo 34:6.
  - The quoted phrases left with no reference are the researcher's words, labels, the grammatical joining words in §F, and the ESV surface words "passion", "king", "hand", "master", "declares", "slow to anger", "fret". They are not quotations of a verse.
- The counts in Step 2, part B and part F come from `anger-reconciliation-v1-20261005.py`, `anger-overview-forms-v1-20261005.py` and `anger-cooccurrence-v1-20261005.py` (all read-only, in this folder).
