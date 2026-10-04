# Life and death: Q2 and Q3 focused pulls — soul, spirit and heart at death (v1)

**Date:** 2026-10-04 · **Author:** Claude Code · **Strand:** life and death, M25 · **Threads:** OT-03 / Q2 (researcher): *"What happens to the spirit and soul at death?"* · OT-04 / Q3 (researcher): *"Is anything said about the heart after death?"* · **Trigger:** researcher, 2026-10-04: *"do the Q2 and Q3 focused pulls first"* · **Status:** **for researcher approval** (nothing woven yet) · Format follows the Q4 ledger. Written with meaning in setting and implication (#1943).

**Data** (iba.db, read-only)
- **Pull script (new, reusable):** `strand-cooccurrence-pull-v1-20261004.py`. One row per hit of a target word, in a verse that also holds a partner word. Strong's are matched by prefix (H5315 covers H5315G–N).
- **Partner words (death):** H4191, H4194, G0599, G2288, G3498, H7585 (Sheol), G0086 (Hades), H1478, G1606, G1634, H6757, H7845 (pit), G5053, H6297, G2348.
- **Q2 targets (soul, spirit, breath):** H5315, G5590, H7307, G4151, H5397 → `life-death-q2-soul-spirit-death-pull-v1-20261004.csv`: **123 hits in 111 verses**.
- **Q3 targets (heart):** H3820, H3824, G2588 → `life-death-q3-heart-death-pull-v1-20261004.csv`: **23 hits in 21 verses**.
- **Faces:** `life-death-q2-q3-face-assign-v1-20261004.py`. Every hit has one; it refuses to run otherwise.
- **Context read:** Psa 49:7–20; Psa 16:9–11; Act 2:27–31; Pro 23:13–14; 1Pe 4:5–6; Isa 5:13–14.
- **Limit of the method:** the pull finds a soul or heart word and a death word **in the same verse**. Psa 49:19 has "his soul" with "dies" two verses earlier (49:17), so it was found by reading the context, not by the pull. Verses about the person after death that use **neither** soul nor spirit (Luk 23:43; Phili 1:23; 2Cor 5:8) are outside it (§F, decision 4).

**Basis:** **S** = the verse states it · **R** = my reading ("I read"). **Disposition:** **W** weave · **RS** restates existing text · **NS** new structure · **H** held · **D** data.

---

## A. Faces

**Q2 (123 hits)**

| Face | Hits | Example |
|---|---|---|
| S01 The soul departs | 1 | Gen 35:18 |
| S02 The spirit and breath at death | 9 | Luk 23:46; Ecc 8:8; Psa 104:29; Jam 2:26; Gen 7:22; Ecc 3:19 |
| S03 The soul dies, or asks to die | 15 | Num 23:10; Judg 16:30; Eze 18:4, 20; 1Ki 19:4; Jon 4:3, 8 |
| S04 The soul near death, or brought to it | 13 | Isa 53:12; Mat 26:38; Judg 16:16; Psa 88:3; 107:18 |
| S05 The soul delivered from death while living | 17 | Psa 30:3; 33:19; 56:13; 86:13; 116:8; Job 33:18–30; Pro 23:14 |
| S06 The soul beyond death | 4 | Psa 49:15; Psa 16:10; Act 2:27, 31 |
| S07 Spirit and life set against death | 15 | Rom 8:2–13; 1Pe 4:6; Rev 14:13; Eze 18:31 |
| S08 The soul as a dead body | 6 | Num 19:11, 13; Lev 21:11 |
| S09 Sheol's and death's appetite | 2 | Isa 5:14; Hab 2:5 |
| S10 Life sought, risked or taken (law and narrative) | 32 | Num 35:30–31; 1Sa 19:11; Jer 38:16 |
| S11 Not the inner being | 9 | wind (Jon 4:8; Job 1:19; Eze 5:12); "breath of his lips" (Isa 11:4); sea creatures; God's soul (Lev 26:30) |

**Q3 (23 hits)**

| Face | Hits | Example |
|---|---|---|
| H01 The heart in anguish before death | 3 | Psa 55:4; Lam 1:20; Act 21:13 |
| H02 The heart at the moment of death | 1 | 1Sa 4:20 |
| H03 The heart dies before the body | 2 | 1Sa 25:37; Psa 31:12 |
| H04 The heart while living, then the dead | 2 | Ecc 9:3 |
| H05 The heart and the way to death | 3 | Pro 10:21; Eze 18:31; Ecc 7:26 |
| H06 Believing in the heart the raising from the dead | 1 | Rom 10:9 |
| H07 The heart searched, and death as judgment | 1 | Rev 2:23 |
| H08 Love strong as death, set on the heart | 1 | Song 8:6 |
| H09 The heart in narratives of killing | 8 | 2Sa 13:28, 33; 2Sa 18:3; Exo 9:7 |
| H10 Idiom: the heart of the seas | 1 | Eze 28:8 |

---

## B. Q2 observations

| ID | what the verses state | meaning in setting, and what it implies | verses | basis | disposition |
|---|---|---|---|---|---|
| Q2-01 | **The soul is said to die.** "Let me die the death of the upright, and let my end be like his!" "Let me die with the Philistines." In both, the Hebrew is *let my soul die*. "Behold, all souls are mine … the soul who sins shall die." Elijah "asked that he might die" (literally, asked for his soul to die), and so did Jonah. | **Meaning:** *nephesh* ("soul, life") is used of the one who dies. It is not only something that leaves at death. **Implies:** Ch 2's "The soul departs" (Gen 35:18) is one face only. The same word is also the subject of dying. | Num 23:10; Judg 16:30; Eze 18:4, 20 (in Ch 2); 1Ki 19:4; Jon 4:8 | S | **RS** (Ch 2, decision 1) |
| Q2-02 | **The soul poured out to death.** "because he poured out his soul to death and was numbered with the transgressors"; "My soul is very sorrowful, even to death"; Samson's "soul was vexed to death"; "my soul is full of troubles, and my life draws near to Sheol" | **Meaning:** the soul is what is poured out, and what is brought to the edge of death by sorrow or vexation. **Implies:** the soul is spoken of as the one who suffers dying, as well as the one who dies. | Isa 53:12; Mat 26:38 (Mar 14:34); Judg 16:16; Psa 88:3 (all but Judg 16:16 already in the chapters) | S | W (in the account, decision 1) |
| Q2-03 | **Delivered from death: counted.** Of **15** verses in the pull where a soul is delivered, brought up, kept back, ransomed, saved or not abandoned from death, Sheol or the pit, **12** speak of a living person kept from dying or brought back from near it (Psa 30:3; 33:19; 56:13; 86:13; 116:8; Jos 2:13; Job 33:18, 28, 30; Isa 38:17; Jam 5:20; Pro 23:14, where the child "will not die", 23:13). **2** look beyond death (Q2-04, Q2-05). **1** says no man can do it: "Who can deliver his soul from the power of Sheol?" (Psa 89:48). | **Meaning:** most of these verses speak of rescue from dying, as Ch 2 says. **Implies:** Ch 2's "almost always" was never counted, and it hides the two verses that do not fit. The claim is restated with the count. | as listed | S (count) | **RS** (Ch 2 "Delivered from death") |
| Q2-04 | **Psalm 49: two ends for the soul.** "Truly no man can ransom another, or give to God the price of his life … that he should live on forever and never see the pit. For he sees that even the wise die … Like sheep they are appointed for Sheol; death shall be their shepherd … Their form shall be consumed in Sheol, with no place to dwell. **But God will ransom my soul from the power of Sheol, for he will receive me.** … For when he dies he will carry nothing away … **his soul will go to the generation of his fathers, who will never again see light.**" | **Setting:** the psalm is about death that comes to everyone, the wise and the fool alike (49:10). It is not about escaping a danger in life. **Meaning:** set against that death, the psalmist says God will ransom his soul from Sheol's power, "for he will receive me". Of the rich man who trusts in his wealth, "his soul will go to the generation of his fathers, who will never again see light." **Implies:** here the soul has an end beyond death, and there are two ends: received by God, or gone to the fathers in the dark. What the psalm sets against each other is two souls, not soul and spirit. It does not say what "receive" involves. (The same verb is used of Enoch: "God took him", Gen 5:24. I note this; I do not draw it in.) | Psa 49:7–20 (49:17 already in Ch 2) | S; R (the setting read as death of all, from 49:10) | **W** (decision 1) |
| Q2-05 | **"Not abandoned to Sheol", read of a death.** "Therefore my heart is glad, and my whole being rejoices; my flesh also dwells secure. For you will not abandon my soul to Sheol, or let your holy one see corruption. You make known to me the path of life." Peter: David "foresaw and spoke about the resurrection of the Christ, that he was not abandoned to Hades, nor did his flesh see corruption." | **Meaning:** Peter reads Psa 16:10 of Christ's death and rising, not of a rescue before death. **Implies:** Psa 16:10 is now in Ch 2's list of a "living person rescued from dying" (in "Delivered from death"). Peter's reading puts it beyond death. It moves (decision 1). | Psa 16:9–11; Act 2:27, 31 | S | **RS** |
| Q2-06 | **The spirit at death.** "Into your hands I commit my spirit!" and "he breathed his last"; "No man has power to retain the spirit, or power over the day of death"; "when you take away their breath, they die and return to their dust"; "the body apart from the spirit is dead"; "They all have the same breath" | **Meaning:** at death the spirit or breath is given up, taken, or not kept; the body without it is dead. **Implies:** what the verses say of the spirit at death is that it goes to God or is taken by God (with Ecc 12:7, already in Ch 2). "Who knows whether the spirit of man goes upward" (Ecc 3:21) stands beside this, unreconciled, as Ch 2 already has it. | Luk 23:46; Ecc 8:8; Psa 104:29; Jam 2:26; Ecc 3:19 (all in Ch 2) | S | D (no change) |
| Q2-07 | **"Live in the spirit the way God does."** "but they will give account to him who is ready to judge the living and the dead. For this is why the gospel was preached even to those who are dead, that though judged in the flesh the way people are, they might live in the spirit the way God does." With "Blessed are the dead who die in the Lord … 'Blessed indeed,' says the Spirit, 'that they may rest from their labors'." | **Meaning:** Peter speaks of the dead living "in the spirit the way God does". **Implies (R):** I read "those who are dead" as people now dead, who heard the gospel while they lived. The verse does not say when they heard it, and I leave that open. | 1Pe 4:5–6; Rev 14:13 (in Ch 2) | S; R | **W** (side by side in "After death"; OT-03) |
| Q2-08 | **The spirit against death while living.** "the law of the Spirit of life has set you free … from the law of sin and death"; "to set the mind on the Spirit is life and peace"; "if by the Spirit you put to death the deeds of the body, you will live"; "make yourselves a new heart and a new spirit! Why will you die?" | Already woven (Ch 2 "Death in the living"; Ch 14). No new meaning beyond those places. | Rom 8:2, 6, 10–13; Eze 18:31 | S | D (no change) |
| Q2-09 | **The soul as a corpse; Sheol's soul.** "Whoever touches the dead body of any person" (*nephesh*); Sheol "has enlarged its appetite" (*nephesh*); the greedy man: "His greed is as wide as Sheol; like death he has never enough" ("greed" is *nephesh*). | **Meaning:** the word names the individual to the end (as Ch 2 says). It is also used of Sheol's own appetite. **Implies:** the soul word is used of the one who wants. Sheol is pictured as wanting, as the greedy are. | Num 19:11; Isa 5:14; Hab 2:5 (in 10.6) | S | W (Isa 5:14 short, in the account) |

## C. Q3 observations

| ID | what the verses state | meaning in setting, and what it implies | verses | basis | disposition |
|---|---|---|---|---|---|
| Q3-01 | **No verse speaks of the heart after death.** In this pull (21 verses), and in units 1–4, no verse says anything of the heart beyond death. The verses speak of the heart **before** death ("My heart is in anguish within me; the terrors of death have fallen upon me"), **at** it (the wife of Phinehas "did not answer or pay attention", literally did not set her heart), and **dying before the body** (Nabal's "heart died within him"). | **Meaning:** Scripture speaks of the heart up to death. **Implies (R):** the closest verse draws the line itself: "madness is in their hearts while they live, and after that they go to the dead" (Ecc 9:3). The heart is named for "while they live". After that, only "they go to the dead". I read this as Scripture being silent on the heart beyond death. I do not argue from the silence. | Psa 55:4; 1Sa 4:20; 1Sa 25:37; Ecc 9:3 (all in Ch 2 or 12) | S; R (the silence) | **W** (one sentence, decision 2); OT-04 **resolved**, if approved |
| Q3-02 | **The heart and the way to death.** "The lips of the righteous feed many, but fools die for lack of sense" (literally *lack of heart*); "make yourselves a new heart and a new spirit! Why will you die, O house of Israel?"; "I find something more bitter than death: the woman whose heart is snares and nets" | **Meaning:** lack of heart is named as what fools die of. A new heart is set against dying. **Implies:** these are stated links: the heart's lack leads to death, and its renewal is the answer to "why will you die?" (a chain of cause, #1946, as the verses state it). | Pro 10:21; Eze 18:31 (in 14); Ecc 7:26 | S | **W** (Ch 4, short) |
| Q3-03 | **The heart and the raising of the dead.** "if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved" | **Meaning:** believing that God raised Jesus from the dead is done in the heart. | Rom 10:9 | S | **W** (Ch 4, short) |
| Q3-04 | **Love set on the heart, strong as death.** "Set me as a seal upon your heart … for love is strong as death, jealousy is fierce as the grave" | Already in 10.6. Set on the heart. | Song 8:6 | S | D (no change) |

---

## D. What the verses say to Q2 and Q3

- **Q2 (soul and spirit at death).** The verses give the soul more than one face at death. It departs (Gen 35:18). It dies (Num 23:10; Eze 18:4). It is poured out to death (Isa 53:12). It goes to the generation of its fathers (Psa 49:19). It is ransomed from Sheol's power, "for he will receive me" (Psa 49:15). It is not abandoned to Sheol, which Peter reads of Christ (Act 2:27, 31). Of the spirit, they say it is committed, taken, or returns to God (Luk 23:46; Psa 104:29; Ecc 12:7); "who knows" where it goes (Ecc 3:21); and the dead "live in the spirit the way God does" (1Pe 4:6). **No verse sends the soul one way and the spirit another.** These are set side by side, unreconciled.
- **Q3 (the heart after death).** No verse found. Scripture names the heart "while they live" (Ecc 9:3), and stops there.

## E. Claim register

- **3-9** (verdict Restated): its restatement said the soul-and-Sheol verses (including Psa 16:10 and 49:15) "speak of the soul delivered or brought up from Sheol: a living person rescued from death". **The count corrects it** (Q2-03 to Q2-05): 12 of 15 do, but Psa 49:15 and Psa 16:10 (as Acts reads it) look beyond death. **The verdict on the original claim still holds**: no verse gives soul and spirit different destinations. Only the wording of the restatement changes.
- **6-2** (survival after death): Psa 49:15 and 49:19 add Old Testament witnesses on both sides.

---

## F. Proposed weave (after approval)

**What emerges.** At present Ch 2 has "The inner person dying" (one verb for each word), "Delivered from death" (rescue, "almost always"), and "After death" (two groups, side by side). The verses show the soul with several faces at death: dying, departing, poured out, going to the fathers, ransomed, received. They also show the spirit committed and returning, and the heart named only up to death. That is one account, and splitting it across three sections loses it.

**Decisions for the researcher:**
1. **Rework "The inner person dying" into "Soul, spirit and heart at death"** (recommended). It would be one account, set out by word:
   - the soul: departs, dies, is poured out, goes to the fathers, is ransomed and received (Q2-01, 02, 04, 05)
   - the spirit: committed, taken, returns, "who knows" (Q2-06)
   - the heart: up to death only (Q3-01)
   - Nabal's heart and the corpse as *nephesh* stay in it.

   With it:
   - "Delivered from death" is **restated with the count** (Q2-03). Psa 16:10 moves out of its list into the new account.
   - "After death" gains Psa 49:15, 49:19 and 1Pe 4:6 in its two groups, unreconciled.

   The alternative is to add these to the three existing sections. I do not recommend it: it keeps the three-way split that hides the soul's faces.
2. **Q3: one sentence and OT-04 resolved** (recommended). In the new account: "Scripture speaks of the heart while a person lives: 'madness is in their hearts while they live, and after that they go to the dead' (Ecclesiastes 9:3). I have found no verse that speaks of the heart after death." Q3-02 and Q3-03 go into Ch 4, short.
3. **Claim register 3-9**: restate the wording as in §E (recommended).
4. **The verses about after death without soul or spirit words** (Luk 23:43 "today you will be with me in paradise"; Phili 1:23 "to depart and be with Christ"; 2Cor 5:8 "away from the body and at home with the Lord", already signposted in OT-03). Read them as a short supplement before weaving (recommended), because Q2 asks what happens, not only which word is used. The alternative is to leave OT-03 open for them.

**Register at approval:**
- OT-03: touched (Q2-01 to Q2-09); stays open if decision 4 is deferred
- OT-04: **resolved** (Q3-01)
- OT-08: touched
- Claim register: 3-9 restated wording; 6-2 more witnesses

## G. Quote check

Every quoted fragment in §B–§F was checked against the whole ESV text in iba.db `verse`, split at "…" and at sentence ends: **87 fragments; 0 verse-text failures.** The flags were section titles, quoted claim wording, the proposed narrative sentence (decision 2), and one gloss inserted inside a quote. The gloss has now been moved outside the quote (Hab 2:5).
