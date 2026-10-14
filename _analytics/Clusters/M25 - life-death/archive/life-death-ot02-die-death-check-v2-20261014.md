# OT-02 Q1 What is death? The death words: claims, narration, missed perspectives, and which death (v2, 2026-10-14)

Researcher, chat 2026-10-14 (verbatim): *"continue with OT-02. I checked out how the sheol work came out on the site, and I like it. checking the remainder of the OT-02 list of strongs is focussed around die related words. There is a large batch of verses that would not be inner being specific nor add any additional value. You already did several extracts of these verses and therefore, inspect the preparatory work before redoing preparatory work. check the completeness and validity of existing claims, check narration for unsubstantiated or unrecorded claims, and check the verses for perspectives that were missed in the first round."*

**Scope.** The four OT-02 Strong's not covered by the Sheol pass: H4191 *mûṯ* (to die), H4194 *māweṯ* (death), G0599 *apothnēskō* (to die), G2288 *thanatos* (death). That is 1,034 verses.

**v2 (same day)** adds §F (the death words hidden in T-codes: 250 more verses read) and §G (which death the verses speak of, its causes, and how the word changes character), after the researcher asked whether spiritual death, dead to sin and the causes of death had been adequately recognised. In v1 they had not. §A–§C are unchanged from v1; §D and §E are revised.

**Nothing is written yet.** This file is the check, plus the proposed actions (§E). The narrative, the register and OT-02 change only after you have read it.

## Preparatory work used, not redone

| Existing work | Used for |
|---|---|
| Unit 2 ledger `life-death-observation-ledger-unit2-v1-20261002.md` (approved and woven, #1939) | Every hit was read and given one of 28 faces |
| Unit 2 faces `life-death-unit2-faces-v1-20261002.csv` | The face of each verse |
| Cross-check script `life-death-claim-register-crosscheck-v2-20261013.py` | **Re-run today** against Ch 2 v24 and register updates 135–139: `life-death-ot02-die-death-crosscheck-v1-20261014.csv`. The v3 cross-check from the Sheol pass was built on Ch 2 v22 and is stale. |
| R0 batch `life-death-ot02-r0-batch-ch2-death-v1-20261013.md` | The eight Ch 2 sections already given claims (not re-checked here) |
| New, reusable: `life-death-ot02-face-coverage-v1-20261014.py` | Joins the cross-check to the faces. Output: `life-death-ot02-die-death-face-coverage-v1-20261014.csv` |

## The verse set, by face

| Group | Faces | Verses | In narrative or register | In neither |
|---|---|---|---|---|
| **Data only**: death notices, put to death under law, killed by people, uncleanness from the dead, not the inner being | D01, D02, D03, D26, D27 | 448 | 33 | 415 |
| **Struck down by God** (judgement events) | D04 | 119 | 19 | 100 |
| **Inner-being faces** | D05–D25 | 467 | 236 | 231 |

The 448 data-only verses are the large batch you described. They stay data and are not read again. In D04, only the 13 verses that name an inner word were read (§C). The rest are judgement events, carried in 13.1 where it matters.

---

## A. Existing claims: completeness and validity

31 register claims cite a die/death verse. 23 are the narrative claims from yesterday's R0 (C-83 to C-110). 8 are original-essay claims (2-1, 2-3, 2-5, 3-3, 3-7, 3-9, 4-10, 9-7).

**Validity.** Every claim was checked against the full text of its sources. **None is contradicted by its verses.** Five of the eight original claims touch the death words only in passing (Jer 38:16 in 3-3, Eze 18:31 in 4-10, Rom 1:32 in 9-7, and 2-3 and 2-5); none of them turns on death. Three small faults:

| # | Claim | Problem | Action |
|---|---|---|---|
| A1 | C-90, C-93, C-94 | Each source verse is stored twice in `narrative_claim_source` | Remove the duplicate rows |
| A2 | 2-1 | One source is "Lev 5", a chapter with no verse | Resolve to the verse the original essay meant ("if anyone sins", Lev 5:1, 5:17) or note as unresolved |
| A3 | C-109 | Its *beyond* note reads "sets n25 beside n26, n27", working labels from the R0 batch | Restate: "sets the dead silent beside the dead stirred and the dead with God" |

**Completeness.** Several claims rest on fewer verses than the set holds. These verses say the same thing and are in neither the narrative nor the register. They are added as sources, and the claim text does not change:

| Claim | Verses to add |
|---|---|
| C-83 Death comes to everyone | Num 16:29 ("die as all men die … the fate of all mankind"); Job 30:23 ("the house appointed for all living"); Psa 82:7 ("like men you shall die"); Isa 51:6 |
| C-84 The same death met in different ways | Job 34:20 ("In a moment they die"); Job 4:21 ("do they not die, and that without wisdom?"); Psa 73:4 ("they have no pangs until death") |
| C-85 Death tied to sin | Rom 5:15, 17, 21 (death's reign set against grace's); Rom 6:21 ("the end of those things is death") |
| C-87 Each answers for his own sin | Deu 24:16; 2Ch 25:4; Jer 31:30; Eze 18:13, 17, 18; Num 27:3 ("died for his own sin"); Joh 8:21 |
| C-88 Death in the living | Rom 7:13 ("sin, producing death in me through what is good"); Hos 13:1 ("he incurred guilt through Baal and died"); Jude 12 ("twice dead"); Lam 3:6; Luk 1:79 ("the shadow of death") |
| C-89 Death as sleep | Mar 5:39; Luk 8:52–53 (the parallels of Mat 9:24) |
| C-104 / C-105 Delivered from death | Job 5:20; Isa 51:14; Hab 1:12 ("Are you not from everlasting … We shall not die") |
| C-106 The dead do not praise | Psa 88:10 ("Do the departed rise up to praise you?") |

---

## B. Narration: unsubstantiated or unrecorded claims

Yesterday's R0 covered Ch 2's *What death is*, *Death and sin*, *Death in the living*, *Sleep and waking*, *Going down to Sheol*, *Soul, spirit and heart at death*, *Delivered from death* and *After death*. Ch 2 holds eight more sections that cite die/death verses, and **no register claim is linked to any of them**. So every statement in them that goes beyond its verses is unrecorded. *The body raised* and its subsections are OT-05 (Q4) and are left for that thread.

Outside Ch 2, the die/death verses are cited 360 times in 110 sections, almost always for another act (fear, choosing, anger, relating). By your standing ruling, those are re-read when that strand comes into focus. They are not checked here.

### B1. Faults: statements the verses do not support

| # | Section | As written | Problem | Proposed |
|---|---|---|---|---|
| B1.1 | Life set before a person | Pro 8:36: "To hate wisdom is to love death, a love the person does not know he has." | The verse does not say the person does not know. No verse basis. | Remove the second clause; keep the quote and "To hate wisdom is to love death." |
| B1.2 | Life set before a person | "The same chapter begins the choice with God's own work on the heart" (Deu 30:6) | "Begins" makes 30:6 the start of the choice in 30:19. The chapter states both and does not order them. | "The same chapter also speaks of God's own work on the heart" |
| B1.3 | Living before God | "Scripture shows it most plainly in an oath" | Uncounted superlative (OT-02.10) | "Scripture shows it in an oath that people swore by life itself." |
| B1.4 | Living before God | "'As the Lord lives' is its commonest form, and often a second life is joined to it" | Counted: "As the Lord lives" 39 verses, "As God lives" 2, so "commonest" holds. A second life is joined in **6 of the 39** (1Sa 20:3; 25:26; 2Ki 2:2, 4, 6; 4:30). "Often" does not hold. | "… is its commonest form (39 verses). In six of them a second life is joined to it …" |
| B1.5 | Facing death | "Scripture does not make the coming of death a calm thing." | Verses in the same chapter say otherwise: "The righteous finds refuge in his death" (Pro 14:32); "to die is gain" (Phi 1:21); "Now let me die, since I have seen your face" (Gen 46:30). This is a verse set aside because it does not fit the line. | "Scripture shows the inner being under the coming of death. Often it is anguish: … (the calmer deaths are in *Dying to the Lord*)." |
| B1.6 | Wanting to die | "What answers these wishes is seldom death." and "In these passages, the one who has had enough is more often fed than taken." | Counted from the section's own list: **2 fed** (Elijah; Israel given bread), **2 answered another way** (Jonah given a question; Israel given the bronze serpent), **3 taken** (Samson, Abimelech, Saul). "Seldom" and "more often fed than taken" are both wrong (OT-02.10). | "Of these wishes, four are answered with something other than death: food for Elijah and for Israel, a question for Jonah, a serpent to look at. Three are granted." |
| B1.7 | Wanting to die | "Where the wish is granted, it comes at the end of a life already lost." | "Already lost" is a reading the verses do not state | State what the verses give: Samson blinded and captive (Judg 16:21), Abimelech and Saul mortally wounded (Judg 9:53–54; 2Sa 1:9) |
| B1.8 | Wanting to die | "Most other such wishes name no inner word at all." | Counted: 7 of the 24 wish-to-die verses carry *nephesh*, spirit or heart; 17 do not, so it holds. But the list of inner-word speakers omits Samson (Judg 16:30, *nephesh*) | Name Samson with Elijah, Jonah, Job and Saul; keep "most" with the count |
| B1.9 | Dying to the Lord | "The death of those who belong to God is seen by him." | Only Psa 116:15 says this. The other verses under it (Num 23:10, Pro 14:32, Heb 11:13, 11:4, Joh 12:24) are a wish, a refuge, faith and fruit, not God seeing. Verses fitted under one line. | "Scripture speaks of the death of the upright in its own words: precious in the Lord's sight (Psa 116:15), wished for (Num 23:10), a refuge (Pro 14:32), died in faith and still speaking (Heb 11:13, 4), bearing fruit (Joh 12:24)." |
| B1.10 | Dying to the Lord | "Some of the last words … are a blessing or a request" | Gen 46:30 is contentment; Gen 50:24 is a word about what God will do | "… are a blessing, a request, or a word about what God will do" |

### B2. Unrecorded claims to register

Each becomes a narrative claim (`AddClaim`, origin narrative) told by its passage (`Tell`). Quotes alone are not claims. These are the statements that join or interpret. "I read" claims are marked.

| # | Section | Claim | Sources |
|---|---|---|---|
| R1 | Breath lent | Life is held in the breath, and the breath is God's to give and to take back | Job 12:10; Dan 5:23; Job 34:14–15; Psa 104:29–30; Ecc 8:8 |
| R2 | Breath lent | When the breath goes, a person's plans go with it | Psa 146:4; 144:4; 94:11 |
| R3 | Breath lent | God holds both ends, killing and making alive, and keeps alive between them | Deu 32:39; 1Sa 2:6; 2Ki 5:7; Psa 33:19; Job 36:6; Gen 50:20; Deu 6:24 |
| R4 | Breath lent | The breath also gives understanding, and words come out on it | Job 32:8; Pro 20:27; Job 26:4; Pro 14:5 |
| R5 | Breath lent | The breath can fail in someone still alive | Dan 10:17; Jer 4:31 |
| R6 | Breath lent | God gives human frailty as a reason for holding back his anger | Isa 57:16; Psa 78:38–39; 90:9 |
| R7 | Breath lent | Humans and animals share one breath and one lot | Ecc 3:19; Gen 6:17; 7:22 |
| R8 | Life set before | Life and death are set before a person to choose; life is chosen by doing, seeking and holding on | Deu 30:15, 19, 6; Lev 18:5; Deu 16:20; Pro 4:4; 9:6; Amo 5:4, 14; Hab 2:4; Jer 21:8 |
| R9 | Life set before | Long days are promised with some commands, and the Preacher sets the righteous who perish beside them; both are stated | Exo 20:12; Deu 6:2; 1Pe 3:10; Ecc 7:15; 8:12 |
| R10 | Life set before | Wisdom marks where the way to death ends, and some of what kills a person is named from within | Pro 14:12; 12:28; 8:35–36; 18:21; Job 5:2; Pro 21:25 (+ §C, C13) |
| R11 | Life set before | God has no pleasure in anyone's death and calls for turning; the turning is a considered act that reaches back over the past | Eze 18:23, 32; 33:10–11; 18:28, 22, 24 |
| R12 | Life set before | Life can be wrongly kept or taken by lying words | Eze 13:19 |
| R13 | Living before God | *I read*: the oath "As the Lord lives" places a promise before the living God and binds the speaker to it by life | 1Sa 20:3; 2Ki 2:2; 2Sa 15:21; 1Ki 1:29; 17:1; Job 27:2 |
| R14 | Living before God | The oath's words stay the same while the heart that speaks them differs; it is judged by how it is sworn | 2Sa 12:5; 1Sa 14:45; 2Ki 5:20; Jer 5:2; 4:2 |
| R15 | Living before God | God swears by his own life, and the oath carries what he wants and what he will do | Eze 33:11; 20:3; Rom 14:11 |
| R16 | Living before God | "The living God" sets him against idols, which have no breath | Jer 10:10; 1Th 1:9; Hab 2:18–20 |
| R17 | Living before God | Scripture counts a life in days and says what the days are for | Deu 4:10; 17:19; 16:3; Psa 146:2; 27:4; Gen 47:9 |
| R18 | Living before God | The world where life is lived is named "the land of the living" | Psa 27:13; 142:5; Isa 38:11; 1Sa 25:29 |
| R19 | Life weighed | People weigh their own lives: loathed, worn down, enjoyed, and what life does not consist in | Job 10:1; Gen 27:46; Ecc 2:17; Job 3:20; Psa 31:10; 88:3; Deu 28:66; 2Co 1:8; Ecc 9:9; 5:20; Luk 12:15; 1Ti 6:19; 1Co 15:19; Joh 12:25 |
| R20 | Life weighed | *I read*: where the hope of seeing good has gone, life is weighed as a breath | Psa 34:12; Job 7:7 |
| R21 | Life weighed | *I read*: the difference lies in what each verse sets life beside | as R19 |
| R22 | Facing death | The coming of death is met with anguish and terror, and the fear of dying shapes what people do | Psa 55:4; 1Sa 20:3; Psa 13:3; Mat 26:38; Gen 26:9; Isa 51:12; Heb 2:14–15 (+ §C, C8) |
| R23 | Facing death | The nearness of death is given a purpose: to rely on God who raises the dead | 2Co 1:9; Heb 5:7 |
| R24 | Wanting to die | People sometimes want to die; few of these wishes name an inner word | the 24 D12 verses (count in B1.8) |
| R25 | Wanting to die | Of the wishes to die, four are answered with something other than death; three are granted | 1Ki 19:4–8; Jon 4:3, 9–11; Exo 16:3–4; Num 21:5–8; Judg 16:30; 9:54; 2Sa 1:9–16 |
| R26 | Made alive | Giving life belongs to the Father, the Son and the Spirit | Joh 5:21; Rom 4:17; Joh 6:63; 2Co 3:6 |
| R27 | Made alive | The dead made alive are living people; the crossing from death to life happens now, and life is spoken of as had now and still to come | Col 2:13; Eph 2:5; Joh 5:24; 8:51; 11:26; 6:47; 1Jo 5:13; Mar 10:30; 1Jo 3:14; Rom 6:4; Col 3:3 |
| R28 | Made alive | The making alive rests on a death | 1Co 15:3; Rom 5:8; Heb 2:9; Zec 13:7; Mat 26:31; Isa 53:12 |
| R29 | Made alive | That death changes how the living live: no longer for themselves, dead to sin, Christ living in them | 2Co 5:15; Rom 6:2; Col 3:5; Gal 2:19–20; Rom 12:1; 1Pe 2:24 |
| R30 | Dying to the Lord | A death, too, can belong to the Lord, and a dying can go on while a person lives | Rom 14:7–8; Phi 1:20–21; 1Co 15:31; 2Co 4:11; 6:9 |
| R31 | Dying to the Lord | The death of the upright is spoken of in its own words (as restated in B1.9) | Psa 116:15; Num 23:10; Pro 14:32; Heb 11:13, 4; Joh 12:24 |

---

## C. Perspectives missed in the first round

231 inner-being verses (D05–D25), plus 13 D04 verses that name an inner word, are in neither the narrative nor the register. All 244 were read in their text, with the passage where the act needed it (Luk 2:29, Luk 22:34, Rom 8:39, Isa 22:14, Psa 73:3, Jer 20:14–18).

**Most add nothing new:**
- the priestly "lest you die" statutes (Exo 28–30, Lev 8–22, Num 1–18: 21 verses)
- the trial and condemnation verses of Jesus (Mat 20:18; 26:66; Mar 10:33; 14:64; 15:44; Luk 23:15, 22; 24:20; Joh 18:14, 32; 19:7; Act 13:28)
- burial instructions and notices of approaching death (Gen 47:29; 50:5, 16; 1Ki 2:1)
- danger and sickness verses already carried by a parallel (2Ki 20:1 = Isa 38:1; Luk 8:42; Joh 4:47, 49)

These are left as data. The verses below carry something the narrative does not.

| # | Perspective | Verses | Proposed home |
|---|---|---|---|
| C1 | **What lies beyond death is God's to know.** God asks Job, "Have the gates of death been revealed to you, or have you seen the gates of deep darkness?" | Job 38:17 | Ch 2 *What death is* |
| C2 | **Death's certainty taken as a reason to indulge, and answered.** "Let us eat and drink, for tomorrow we die." In Isaiah the Lord answers it: "Surely this iniquity will not be atoned for you until you die" (22:14). Paul says it is what follows *if* the dead are not raised. | Isa 22:13–14; 1Co 15:32 | Ch 2 *Life weighed* (beside 1Co 15:19, already cited) |
| C3 | **The wicked's easy death, envied.** "They have no pangs until death," from one who says "I was envious" (73:3). | Psa 73:4 | Ch 2 *What death is* (C-84); pointer to 10.6 *Jealousy and envy* |
| C4 | **Death accepted once what was waited for is seen.** Simeon "would not see death before he had seen the Lord's Christ", then: "now you are letting your servant depart in peace". Jacob: "It is enough; Joseph my son is still alive. I will go and see him before I die." | Luk 2:26, 29; Gen 45:28 (with 46:30, cited) | Ch 2 *Dying to the Lord*; also answers B1.5 |
| C5 | **Ready to die for or with another, and readiness that fails.** Jonathan: "Here I am; I will die." Peter: "ready to go with you both to prison and to death", answered "you will deny three times that you know me" (22:34). Thomas: "that we may die with him". "Be faithful unto death"; "they loved not their lives even unto death". | 1Sa 14:43; Jos 2:14; Judg 5:18; Luk 22:33–34; Joh 11:16; 1Co 9:15; Phi 2:30; Rev 2:10; 12:11 | Ch 2 *Dying to the Lord* (beside Ruth); 10.10 *Loyalty and honour* |
| C6 | **What death cuts off.** A man goes home from battle "lest he die in the battle and another man dedicate it … enjoy its fruit … take her". The law names what a death would leave unfinished. *I read*: the verse weighs a life by what it had begun. | Deu 20:5–7 | Ch 2 *What death is* (beside "nothing goes with the dead") |
| C7 | **Those left behind.** Hagar: "Let me not look on the death of the child", and she wept. David fasted while the child lived and ate when he died, and his servants ask why (2Sa 12:21); 12:23, already cited in *After death*, is his answer. Joab rebukes David's grief for Absalom (2Sa 19:6). Paul: God had mercy on Epaphroditus "lest I should have sorrow upon sorrow". "You shall not cut yourselves … for the dead." No comfort for the mourner under judgment. | Gen 21:16; 2Sa 12:19–21; 19:6; Phi 2:27; Deu 14:1; Jer 16:7; Gen 44:22 | **New short Ch 2 section, *Those left behind***, pointing to 10.1 for grief. Ch 2 has no place for death as the living meet it in another. |
| C8 | **The fear of dying shapes acts.** Judah withholds Shelah "for he feared that he would die, like his brothers". Lot cannot flee to the hills "lest the disaster overtake me and I die". Agag comes "cheerfully": "Surely the bitterness of death is past". The Egyptians: "We shall all be dead." | Gen 38:11; Gen 19:19; 1Sa 15:32; Exo 12:33; 1Sa 5:11; 12:19 | Ch 2 *Facing death* (beside Gen 26:9) |
| C9 | **Fear of death crossing into death (OT-02.9).** Bildad: the wicked man "is brought to the king of terrors", spoken of Job, under God's later verdict on the friends (Job 42:7). In age, "terrors are in the way … and desire fails, because man is going to his eternal home". Ananias and Sapphira die, and "great fear came upon all who heard of it". | Job 18:14; Ecc 12:5; Act 5:5, 10–11 | Ch 2 *Facing death*; Act 5 also *Death and sin* (5:3–4, the heart that contrived the lie). **Closes OT-02.9**, and the 10.12 working note is removed. |
| C10 | **A prophet's wish not to have been born.** "because he did not kill me in the womb … Why did I come out from the womb to see toil and sorrow, and spend my days in shame?" | Jer 20:14–18 | Ch 2 *Wanting to die* (beside Job 3:11) |
| C11 | **The wilderness complaint, "to die in the wilderness".** | Exo 14:11; Num 20:4; 21:5 | Sources only, for the lines already in *Wanting to die* |
| C12 | **The same message is death to one and life to another.** "to one a fragrance from death to death, to the other a fragrance from life to life. Who is sufficient for these things?" | 2Co 2:16 | Ch 2 *Life set before a person*; Ch 11 §4 (change of character) |
| C13 | **What kills from within, in wisdom.** "He dies for lack of discipline"; "whoever hates reproof will die"; "he who despises his ways will die"; "righteousness delivers from death". | Pro 5:23; 15:10; 19:16; 11:19; 10:2; 13:14; 21:6; Psa 34:21 | Ch 2 *Life set before a person*, widening "named from within" (R10) |
| C14 | **Another's death laid at one's hand.** The watchman who does not warn: "his blood I will require at your hand". If he warns, "you will have delivered your soul". | Eze 3:19–20; 33:8–9 | 10.10 (pointer from Ch 2 *Life set before a person*) |
| C15 | **Trusting one's own righteousness leads to death.** "if he trusts in his righteousness and does injustice … he shall die" | Eze 33:13 (with 33:18; 18:26) | Ch 2 *Life set before a person*, beside the turning (R11) |
| C16 | **Nothing separates.** "neither death nor life … will be able to separate us from the love of God in Christ Jesus our Lord" | Rom 8:38–39 | Ch 2 *Dying to the Lord* |
| C17 | **Christ's death as his own act.** "he humbled himself by becoming obedient to the point of death"; "the love of Christ controls us … one has died for all, therefore all have died"; "the death he died he died to sin, once for all, but the life he lives he lives to God". | Phi 2:8; 2Co 5:14; Rom 6:9–10; 5:6; 8:34; Gal 2:21; Heb 9:15 | Ch 2 *Made alive* |
| C18 | **Baptized into his death.** | Rom 6:3, 5, 8; Col 2:20 | Ch 2 *Made alive* (beside Rom 6:2, 4) |
| C19 | **The living and the dead.** Inquiring of the dead and offering to them are forbidden; kindness to the dead is blessed (Naomi). | Deu 18:11; 26:14; Psa 106:28; Rut 1:8 | Ch 2 *After death* |
| C20 | **A death that glorifies God; death as "yours".** "by what kind of death he was to glorify God"; "Christ died and lived again, that he might be Lord both of the dead and of the living"; "life or death … all are yours"; "death is at work in us, but life in you"; Zedekiah, "You shall die in peace". | Joh 21:19; Rom 14:9; 1Co 3:22; 2Co 4:12; Jer 34:5 | Ch 2 *Dying to the Lord* |
| C21 | **Not seeing death.** Enoch "was taken up so that he should not see death … he was commended as having pleased God". The bread "that one may eat of it and not die". | Heb 11:5; Joh 6:50, 58; 8:52–53 | Ch 2 *Made alive* (with Joh 8:51, cited) |
| C22 | **The command as Eve held it.** "neither shall you touch it, lest you die" | Gen 3:3 | Ch 2 *Death and sin*, quote only (beside 2:17 and 3:4) |
| C23 | **Wished dead by enemies.** "When will he die, and his name perish?" | Psa 41:5 | 10.10 (data for Ch 2) |
| C24 | **D04 verses with an inner word.** God "searches mind and heart" as he strikes (Rev 2:23). Ezekiel falls on his face at Pelatiah's death: "will you make a full end?" (Eze 11:13). Saul "did not seek guidance from the Lord. Therefore the Lord put him to death" (1Ch 10:14). One "spared to weep his eyes out to grieve his heart" (1Sa 2:33). | Rev 2:23; Eze 11:13; 1Ch 10:14; 1Sa 2:33 | 13.1 (Rev 2:23, 1Ch 10:14); 10.9 (Eze 11:13). The other 9 D04 verses are data. |

---

---

## F. The death words hidden in T-codes (added in v2)

Researcher, chat 2026-10-14 (verbatim): *"have you adequately recognised the different perspectives of death related to 'spiritual death', 'dead to sin', 'causes of death - especially spiritual death'"*; then *"yes, proceed with the pull and reading. If these verses were not part of M25, are they included in other M-codes or hidden in T-Codes?"*

**Where they sit.** They are hidden in T-codes. The four OT-02 words were also T-coded, and gained an M25 tag under #1880 (*"Death side of Life & Death is invisible"*). These were not brought across:

| Strong | Word | Verses | Cluster |
|---|---|---|---|
| G3498 | *nekros*, dead | 119 | T2 Supplementary |
| G2289 | *thanatoō*, put to death | 11 | T3 Operations |
| G2348 | *thnēskō*, be dead | 10 | T3 |
| G4880 | *synapothnēskō*, die with | 3 | T3 |
| G3500 | *nekrōsis*, dying, deadness | 2 | T2 |
| G2349 | *thnētos*, mortal | 5 | T2 |
| G5053 / G5054 | *teleutaō* / *teleutē*, die / death | 11 / 1 | T3 / T2 |
| H1478 | *gāwaʿ*, breathe one's last, perish | 23 | T3 |
| H7901J | *šāḵaḇ*, lie down: be dead ("slept with his fathers") | 45 | T3 |
| H5315M | *nephesh*, soul: dead (body) | 13 | M47 |
| H8546, H4463, H4193, G1935, G2286, G2287 | death, deadly, condemned to death | 8 | T2 |

**Not pulled, named for the record.** These carry death beside other senses and are tagged elsewhere, or are killing words (people killing people: data):
- H0006 *ʾāḇaḏ*, perish (174, T3)
- G0622 *apollymi*, destroy, perish (81, M10)
- G0684 *apōleia*, destruction (17, M55)
- H2026, G0615, G0337, the kill words (T3)
- the grave and corpse words (T2)

"Perish" bears on the question ("should not perish", Joh 3:16) and is the next pull if you want it.

**The pull.** 250 verses: `life-death-ot02-dead-words-pull-v1-20261014.csv`; cross-check `life-death-ot02-dead-words-crosscheck-v1-20261014.csv`. 66 are cited in the narrative, and 21 back a register claim. All 250 were read.

About 140 add nothing new:
- the "raised from the dead" references in preaching and narrative (Mat 14:2; Act 3:15; Rom 1:4 and others)
- the uncleanness laws (H5315M)
- death notices
- the plotting to put Jesus to death (Mat 26:59; 27:1)

---

## G. Which death: the kinds the verses speak of, what they give as the cause, and how the word changes character (#1919)

The narrative has the parts but no account that sets them side by side:
- *Death in the living* (Ch 2) lists the uses.
- *Made alive* (Ch 2) and Ch 14 carry dying to sin.
- *Life, and judgment* (Ch 2) carries the second death.
- Ch 12 traces James 1:15.

Read together, the verses speak of death in these ways. The groups are named from the verses' own words, not from a framework.

**G1. The body's death.** The breath taken, the return to dust (Psa 104:29; Ecc 12:7). This covers most of the 1,284 verses.

**G2. Death in the living.** People still alive are called dead:
- "you were dead in the trespasses and sins" (Eph 2:1; also 2:5; Col 2:13)
- "she who is self-indulgent is dead even while she lives" (1Ti 5:6)
- "You have the reputation of being alive, but you are dead" (Rev 3:1)
- "this my son was dead, and is alive again; he was lost, and is found" (Luk 15:24, 32)
- "leave the dead to bury their own dead" (Mat 8:22; Luk 9:60)
- "an hour is coming, and is now here, when the dead will hear the voice of the Son of God, and those who hear will live" (Joh 5:25)
- "Awake, O sleeper, and arise from the dead" (Eph 5:14), said to believers
- Within, the hypocrites are "full of dead people's bones" (Mat 23:27)

The word reaches to what a person does:
- "dead works" (Heb 6:1; 9:14)
- "faith by itself, if it does not have works, is dead" (Jam 2:17, 26)

**G3. Dying to.** A death the verses count as already died, with a release in it. The relationship carried in it is "to":
- "How can we who died to sin still live in it?" (Rom 6:2)
- "consider yourselves dead to sin and alive to God" (6:11)
- "you also have died to the law through the body of Christ, so that you may belong to another … in order that we may bear fruit for God" (Rom 7:4)
- "If with Christ you died to the elemental spirits of the world" (Col 2:20)
- "If we have died with him, we will also live with him" (2Ti 2:11)

Beside it stands a putting to death still to be done: "if by the Spirit you put to death the deeds of the body, you will live" (Rom 8:13); "Put to death therefore what is earthly in you" (Col 3:5). And a death carried in the body: "always carrying in the body the death of Jesus" (2Co 4:10).

**G4. Death beyond death.** The "second death" (Rev 2:11; 20:6, 14; 21:8). "you will die in your sins" (Joh 8:21, 24). "their worm does not die" (Mar 9:48; Isa 66:24).

**G5. Death as a power.** It reigns (Rom 5:14, 17, 21), stings (1Co 15:56) and is held by one who "has the power of death" (Heb 2:14); C-99.

**G6. Like the dead.**
- The guards "became like dead men" for fear (Mat 28:4).
- John "fell at his feet as though dead" (Rev 1:17).
- Abraham's body "as good as dead" (Rom 4:19).

### How the word changes character

**"Dead in" and "dead to" are opposites.** Of the same people, Paul says they "were dead in" trespasses (Eph 2:1, 5; Col 2:13: 3 verses) and that they "died to sin" or "died to the law" (Rom 6:2, 10, 11; 7:4; Gal 2:19; 1Pe 2:24: 6 verses). The word is the same, *nekros* or *apothnēskō*. What differs is what the death is related to:
- "in" trespasses is death under them
- "to" sin is death that ends their rule: "one who has died has been set free from sin" (Rom 6:7)

The verses give the turn in each place. It is God's act ("God made alive together with him, having forgiven us all our trespasses", Col 2:13) and union with Christ's death ("baptized into his death", Rom 6:3).

**One sentence can use both senses.** "Leave the dead to bury their own dead" (Mat 8:22). The first "dead" are the living; the second, the man's father. Jesus does not explain the first.

**The father's word.** "This my son was dead … he was lost" (Luk 15:24). The father sets "dead" beside "lost", and "alive" beside "found". The son was never dead in body.

**The same body, both ways.** "although the body is dead because of sin, the Spirit is life because of righteousness" (Rom 8:10).

**Sin can be dead too.** "apart from the law, sin lies dead" (Rom 7:8). Then: "when the commandment came, sin came alive and I died" (7:9). Here the word passes between sin and the person.

**The same message, death to one and life to another.** "to one a fragrance from death to death, to the other a fragrance from life to life" (2Co 2:16).

### What the verses give as the cause

Only what a verse states is listed, by kind. No verse sets these out as one scheme, and none is made here.

| Kind | What the verses name as its cause | Verses |
|---|---|---|
| The body's death | sin entering through one man | Rom 5:12; 1Co 15:21 |
| | God taking the breath | Psa 104:29 |
| | "for lack of discipline"; hating reproof; despising one's ways | Pro 5:23; 15:10; 19:16 |
| | vexation, jealousy, the sluggard's desire | Job 5:2; Pro 21:25 |
| | not listening: "they perish by the sword and die without knowledge" | Job 36:12 |
| Death in the living | trespasses and sins, "the uncircumcision of your flesh" | Eph 2:1; Col 2:13 |
| | self-indulgence | 1Ti 5:6 |
| | works that look alive | Rev 3:1 |
| | not loving | 1Jo 3:14 |
| | the mind set on the flesh | Rom 8:6 |
| | sin taking opportunity through the commandment, "producing death in me through what is good" | Rom 7:8–11, 13 |
| | desire conceiving sin, sin brought forth to full growth | Jam 1:15 |
| | the letter: "the letter kills" | 2Co 3:6 |
| | worldly grief | 2Co 7:10 |
| | hating wisdom: "all who hate me love death" | Pro 8:36 |
| The way out of it | hearing the Son's voice and believing | Joh 5:24–25 |
| | God making alive, with forgiveness | Col 2:13; Eph 2:5 |
| | waking | Eph 5:14 |
| | coming home | Luk 15:24 |
| | its sign: loving the brothers | 1Jo 3:14 |
| Dying to sin | through the body of Christ | Rom 7:4 |
| | baptism into his death | Rom 6:3–4 |
| | crucified with Christ | Gal 2:19–20 |
| | the putting to death, done "by the Spirit" | Rom 8:13 |
| Death beyond death | dying in one's sins, unless one believes | Joh 8:24 |
| | the list beginning "the cowardly, the faithless" | Rev 21:8 |
| | not found written in the book of life | Rev 20:15 |

**Which death a verse means, where it does not say.** Several verses the narrative cites under *Death and sin* set death against life without saying which death:
- "the wages of sin is death, but the free gift of God is eternal life" (Rom 6:23)
- "sin when it is fully grown brings forth death" (Jam 1:15)
- "if you live according to the flesh you will die" (Rom 8:13)
- "the soul who sins shall die" (Eze 18:4)

The narrative should not decide it for them. Where the opposite is "eternal life" (Rom 6:23), the verse sets the death against more than the body's life. That is *I read*.

### G7. Other verses from the pull that carry something

| Verse | What it carries | Home |
|---|---|---|
| "slept with his fathers": **36 verses**, the common way Kings and Chronicles tell a king's death | Death told as sleep and as joining one's fathers. C-89 rests on the sleep words alone and does not hold the commonest Old Testament form. | Ch 2 *Sleep and waking*; C-89 gains these as sources |
| Mar 14:31: "If I must die with you, I will not deny you." And they all said the same. | Readiness that failed (with Luk 22:33–34, §C C5) | Ch 2 *Dying to the Lord* |
| Job 27:5: "till I die I will not put away my integrity from me"; Job 13:19 | Holding to the end | Ch 2 *Dying to the Lord* |
| Job 10:18; Num 20:3 ("Would that we had perished") | Wishes to die | Sources for *Wanting to die* |
| Num 17:12–13: "Behold, we perish, we are undone … Are we all to perish?" | Fear of death near the holy (cited in 10.7) | Ch 2 *Facing death* |
| Psa 88:15: "close to death from my youth up, I suffer your terrors" | A life lived near death | Ch 2 *Life weighed* |
| Psa 79:11; 102:20: "preserve those doomed to die" | God hears the doomed | C-104 sources |
| Luk 7:12–15 (the widow's only son); Joh 11:21 ("Lord, if you had been here"); Jer 16:4 ("They shall not be lamented") | Those left behind | Ch 2 *Those left behind* (§C C7) |
| Heb 11:22: "By faith Joseph, at the end of his life, made mention of the exodus" | Last words of faith | Ch 2 *Dying to the Lord* (with Heb 11:21) |
| 1Co 4:9: "like men sentenced to death … a spectacle to the world" | Living as the condemned (with 2Co 1:9) | Ch 2 *Facing death* |
| Jam 3:8: the tongue "full of deadly poison" | The tongue (with Pro 18:21) | Ch 2 *Life set before a person*; 10.5 |
| Mat 22:32; Mar 12:27; Luk 20:38: "not God of the dead, but of the living" | Luk 20:38 is cited in *After death*; the parallels are sources for C-110 | — |
| Rom 6:9: "death no longer has dominion over him"; Rom 14:9; Heb 9:17 | Sources (C-99; *Dying to the Lord*); Heb 9:17 is data | — |

---

## D. What this shows

1. **The claims are sound but thin in places.** None of the 31 is contradicted by its verses; 8 rest on fewer verses than the set holds (§A).
2. **Half of Ch 2's death narration has no register cover.** Eight sections, 31 claims, none recorded. Ten statements fail on their verses (§B1).
3. **The first round read the face of death, not the kind.** The words that carry "dead in trespasses", "dead to sin" and "dead works" sat in T-codes and were never pulled (§F). The narrative holds the parts in four places but no account of how *death* differs between them, or of what the verses give as each one's cause (§G).
4. **The missed perspectives are mostly about how the living meet death** (§C) and about the death in the living and the dying to sin (§G).

## E. Proposed actions (on your word)

1. **Ch 2 v24 → v25.**
   - Make the 10 corrections (§B1).
   - **Restructure the death part around §G.** *What death is* gains a subsection on the ways Scripture speaks of death, giving the kinds G1–G6 and how the word changes character: dead in / dead to, the father's "dead … lost", "leave the dead to bury their own dead", sin lying dead, faith and works dead. *Death and sin* states, verse by verse, where a verse does not say which death (*I read* marked). *Death in the living* becomes the account of G2, with its stated causes and the way out of it. A new subsection, *Dead to sin*, gives G3 and points to Ch 14 for the new life.
   - Weave the perspectives of §C (C1–C10, C12, C13, C15–C22) and §G7, including the new section *Those left behind* and "slept with his fathers" in *Sleep and waking*.
2. **Ch 14.** Check its *Died to sin* lines against §G3 and point back to Ch 2. No new reading.
3. **Ch 12.** Its James 1:15 line points to Ch 2 *Death in the living*.
4. **10.12 v9 → v10.** Remove the OT-02 working note (C9 read).
5. **10.10.** Pointers only: C5, C14, C23.
6. **Register.** One update file:
   - claims R1–R31 with their tellings
   - claims for §G: the kinds, the "dead in / dead to" change, the stated causes per kind, and the "which death" restraint (*I read*)
   - claims for the interpreting perspectives (C2, C6, C7, C12, C17)
   - the §A sources, the "slept with his fathers" sources for C-89, and fixes A1–A3
7. **OT-02.** Add items for the §F Strong's and complete them with 1–10 after the weave. Raise a forward thread item for "perish" (H0006, G0622, G0684) if you want it read.

**Limits.** The narration check covers Ch 2, with only pointers to Ch 12 and 14 (the other 360 citations wait for their strands). The 448 data-only verses, the plain D04 events, and the ~140 plain verses of §F were not given a second reading. Counts come from iba.db `verse` and `verse_lexical` this session. The 27 §G quotes and all §C quotes are checked against iba.db `verse`.
