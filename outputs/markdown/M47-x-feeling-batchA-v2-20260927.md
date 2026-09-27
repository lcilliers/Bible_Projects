# M47 × Feeling — Batch A (v2)

**Date:** 2026-09-27
**Supersedes:** v1 (same date; `archive/`). v2 adds §R (items for researcher ruling) and §X (cluster cross-reference), with DB assignment sources. The analysis in §0–§9 is unchanged.
**Use:** this file is meant to accompany the analysis of each cluster listed below. Start at §X to find the sections and flagged Strong's for your cluster.
**Data:** `cluster-M47-other-m-code-pairs-with-distance-20260927.csv` — pairs where the other word is in:
- M01 Fear & Awe
- M02 Anger & Wrath
- M03 Grief & Lament
- M04 Joy & Gladness
- M07 Shame & Confusion
- M20 Doubt & Discouragement
- M24 Faintness & Despair
- M48 Astonishment & Wonder
- M53 Dishonor & Disgrace

**949 pairs in 611 verses; all read.**

**Plan:** `M47-other-cluster-cooccurrence-assessment-v1-20260927.md` §5.
**Spirit classes:** `M47-spirit-distinction-v1-20260927.md`. Each spirit row below is tagged:
- **[D1/D2]** divine
- **[D3]** divine only per ESV capitalisation
- **[H]** human
- **[O]** other being
- **[X]** disposition
- **[T]** temper
- **[U]** not determinable

Tags as before: **[Claude reading]**, **[lexical]**, **[verify]**, ◆ fringe. Not a statistical analysis.

**Assignment source.** Cluster membership is from `iba/app/db/iba.db` → `cluster_strong` (active rows, read-only query, 2026-09-27). "Source" is the assignment route recorded there:
- `old-system-migration` — carried over; no confidence recorded
- `heuristic-family-grouping-v1-20260905` — family heuristic
- `llm-allocation-v1_3-20260811` — LLM allocation, with a confidence value
- `auto-precedent`
- `claude-scan-20260908`

**A Strong's can hold more than one cluster row** (e.g. an M-cluster and a T-bucket). Where that applies, all rows are shown.

---

## R. Items for researcher ruling

Seven decisions are needed.
- **R1–R6** are **cluster-membership** questions for `cluster_strong`.
- **R7** is a **process** question that applies to all batches (A–H).
- Nothing has been changed in the DB.
- "Pairs / verses" counts are for this batch only.

### R1 — H3513H "to honor: heavy" in M03 Grief & Lament
| | |
|---|---|
| **Cluster(s)** | M03 (current); T3 Operations (current, second row); M75 Disobedience & Lawlessness (candidate) |
| **Strong's** | H3513H *kāvēd* "be heavy" |
| **DB now** | M03 · `heuristic-family-grouping-v1-20260905` · heuristic · "family=grief-lament-sorrow". **Also** T3 · `llm-reassignment-v1_1-20260811` · "T2/FLAG operation → T3". |
| **Evidence** | 13 pairs / 8 verses. "Pharaoh hardened [made heavy] his heart" (Exo 8:15, 32; 9:7, 34; 10:1); "Why should you harden your hearts" (1Sa 6:6); "their ears heavy" (Isa 6:10). See §0.2 and §3.6. |
| **Issue** | In these verses "heavy" means **hardened** (of heart), not grief. The M03 row comes from a family heuristic, not from the verses. |
| **Options** | (a) keep M03; (b) remove the M03 row and keep T3; (c) replace M03 with M75 (hardening is in M75's description); (d) keep M03 with an alternative-cluster note. |
| **Recommendation** | **(c) M75** [Claude reading]. It matches how Batch C reads the hardening vocabulary (C §9.3). |
| **Ruling** | ______ |

### R2 — "cord" sub-entries H2256M, H5688, H3499B in M03 Grief & Lament
| | |
|---|---|
| **Cluster(s)** | M03 (current); T12 Objects-Artifacts (current, second row) |
| **Strong's** | H2256M *ḥevel* "cord" · H5688 *ʿăvōt* "cord" · H3499B *yeter* "cord / bowstring" |
| **DB now** | Each: M03 · `auto-precedent` · no confidence. **Also** T12 · `heuristic-family-grouping-v1-20260905` · "no inner-being significance". |
| **Evidence** | 6 pairs / 6 verses: ropes, bowstring, clouds, a group of prophets (1Ki 20:31; Psa 11:2; 1Sa 10:10; Eze 31:10). See §0.2. |
| **Issue** | [lexical] *ḥevel* is a homograph: "cord" and "pang". Only the **pang** sense belongs in Grief. The "cord" sub-entries seem to have inherited M03 by precedent. The T12 row already records "no inner-being significance". |
| **Options** | (a) keep both rows; (b) remove the M03 rows and keep T12. |
| **Recommendation** | **(b)**. |
| **Ruling** | ______ |

### R3 — H7451C "distress: harm" in M24 Faintness & Despair
| | |
|---|---|
| **Cluster(s)** | M24 (current); M55 Destruction & Ruin or M58 Wickedness (candidates) |
| **Strong's** | H7451C *rāʿâ* "evil, harm, disaster" |
| **DB now** | M24 · `heuristic-family-grouping-v1-20260905` · heuristic · "family=faint-despair-languishing" |
| **Evidence** | 28 pairs / 24 verses. Surfaces: calamity, disaster, doom, harm, hurt, trouble, pain, plight. Mostly **evil done or suffered**, not an inner state of despair. See §0.2. |
| **Issue** | Only a minority of verses ("troubles", "plight") fit M24. The heuristic grouped it by family. |
| **Options** | (a) keep M24; (b) move to M55 (disaster / ruin sense); (c) move to M58 (evil-done sense); (d) keep M24 with M55 / M58 as alternatives. |
| **Recommendation** | **(d)** [Claude reading]. The word has both senses; a single move would lose one of them. |
| **Ruling** | ______ |

### R4 — H7186 "severe" in M24 Faintness & Despair
| | |
|---|---|
| **Cluster(s)** | M24 (current); M30 Rebellion & Stubbornness (candidate) |
| **Strong's** | H7186 *qāšeh* "hard, severe, stubborn" |
| **DB now** | M24 · `old-system-migration` · no confidence |
| **Evidence** | 8 pairs / 7 verses. Surfaces: stubborn, hard, harsh, fierce, impudent, troubled. "a hard forehead and a stubborn heart" (Eze 3:7); "harsh slavery" (Exo 6:9). See §0.2. |
| **Issue** | The heart sense is **stubbornness**, which is in M30's description. "Harsh slavery" is an external condition. Only "troubled [hard of spirit]" (1Sa 1:15) is near M24. |
| **Options** | (a) keep M24; (b) move to M30; (c) keep M24 with M30 as an alternative. |
| **Recommendation** | **(b) M30** [Claude reading]. |
| **Ruling** | ______ |

### R5 — H0926 "to dismay" in M24 Faintness & Despair — the "hasty / rash" sense
| | |
|---|---|
| **Cluster(s)** | M24 (current); M66 Madness & Recklessness or M69 Self-Control & Zeal (candidates, for the haste sense) |
| **Strong's** | H0926 *bāhal* "be dismayed; hasten" |
| **DB now** | M24 · `heuristic-family-grouping-v1-20260905` · heuristic |
| **Evidence** | 8 pairs / 7 verses. Mostly "dismayed / terrified / troubled" (fits M24). Two verses have the **haste** sense: "let not your heart be hasty" (Ecc 5:2); "Be not quick in your spirit to become angry" (Ecc 7:9). |
| **Issue** | One Strong's with two senses. The dismay sense fits M24; the haste sense is about self-restraint. |
| **Options** | (a) keep M24 only; (b) keep M24 and note an alternative cluster for the haste sense. |
| **Recommendation** | **(b)**, alternative **M69** (restraint of heart and spirit) [Claude reading]. |
| **Ruling** | ______ |

### R6 — "to hide" words in M20 Doubt & Discouragement
| | |
|---|---|
| **Cluster(s)** | M20 (current) |
| **Strong's and DB now** | H5641 (`old-system-migration`) · H3582 (`llm-allocation` · **high**) · H2244, H2934, G2928 (`auto-precedent`) |
| **Evidence** | 19 pairs / 17 verses. "I have not hidden your deliverance within my heart" (Psa 40:10); "God … has hidden his face" (Psa 10:11); "Hide not your face from me" (Psa 143:7). H3582 also carries "be destroyed / cut off" (Zec 11:8–9). See §0.2 and §6. |
| **Issue** | Hiding and concealing are not doubt or discouragement. The M20 link in the verses comes through **God hiding his face**, which is paired with the human spirit failing (§6 ◆). It does not come from the word's own sense. |
| **Options** | (a) keep M20; (b) move to a cluster you name (e.g. M14 Deceit & Falsehood for concealment); (c) keep M20 and set the review flag for later. |
| **Recommendation** | **(c)** [Claude reading]. There is no clear better home, and the God-hides-his-face link is real evidence for M20. |
| **Ruling** | ______ |

### R7 — Should misfiled tags be recorded beyond these write-ups? (all batches)
| | |
|---|---|
| **Scope** | Every §0 misfile list and every §R membership item in Batches A–H |
| **Question** | This was raised in v1 §10 and is still open. The earlier ruling ("the tag/surface misalignment note is sufficient") was about surface forms, not cluster membership. |
| **Options** | (a) leave them in the batch files only; (b) after Batch H, compile **one** consolidated register of membership rulings (R items + §0 misfiles) to apply to `cluster_strong` in a single reviewed pass; (c) set `review_flag=1` on each affected `cluster_strong` row now, as each batch is ruled. |
| **Recommendation** | **(b)**. It keeps one living register, avoids piecemeal DB writes, and gives one approval point. |
| **Ruling** | ______ |

---

## X. Cluster cross-reference — where each cluster appears in this file

Use this when the file accompanies a cluster's analysis. "Sense-level" means that in these verses the word is used in a sense outside the cluster, but the assignment itself is not questioned.

| Cluster | Sections | Flagged Strong's (DB source · confidence) |
|---|---|---|
| **M01** Fear & Awe | §1; also §4.5 fringe (dread-word for joy) | — |
| **M02** Anger & Wrath | §2; §2.3 anger = nose / breath | H0639G "face: anger" — correctly dual: M02 + T14 Body-Parts (`claude-scan-20260908` · high). No ruling. |
| **M03** Grief & Lament | §3; §3.6 "heavy" | **R1** H3513H (heuristic; also T3) · **R2** H2256M, H5688, H3499B (auto-precedent; also T12) |
| **M04** Joy & Gladness | §4 | — |
| **M07** Shame & Confusion | §5 | — |
| **M53** Dishonor & Disgrace | §5 | Sense-level: "filth" = literal dirt at 1Pe 3:21 (G4509, heuristic); H5708, H6675, G4507 (heuristic) |
| **M20** Doubt & Discouragement | §6 | **R6** H5641, H3582, H2244, H2934, G2928 |
| **M24** Faintness & Despair | §7 | **R3** H7451C (heuristic) · **R4** H7186 (old-system) · **R5** H0926 (heuristic); H0927 "alarmed" fits |
| **M48** Astonishment & Wonder | §8 | Sense-level: H6381 = "hard" (Jer 32:27), "special" vow (Lev 27:2) (heuristic) |
| **M47** Inner Seat | all; §9 cross-cutting | Spirit classes used: [D1] [D2] [D3] [H] [X] [T] [O] [U], plus combined [D3+H] (Eze 3:14) and [X+D1] (Rom 8:15) |
| Candidate receiving clusters | M75 (R1); M55 / M58 (R3); M30 (R4); M69 (R5); M14 (R6, option) | — |
| All batches | — | **R7** process ruling |

---

## 0. Notes on the data before reading

1. **What `distance` measures.** The positions follow **original-language word order**, not English (e.g. rûaḥ is at 0 in 1Ch 12:18, where the Hebrew opens with it) [verify]. So `distance` counts words in the Hebrew or Greek.
   - **d0** = one word carries both tags, e.g. "brokenhearted" (Psa 147:3), "fainthearted" (Heb 12:3), "merry-hearted" (Isa 24:7). These compounds are themselves evidence of fusion.
   - **d1–d2** almost always marks a grammatical tie: "my heart **trembled**", "**bitter** in soul".
   - **Larger distances** are sometimes still meaningful (e.g. Mar 3:5, d5: "anger, grieved at their hardness of heart"). But they are often incidental: "declares the Lord", or a different subject.
   - I read every verse, and used distance only as a guide.
2. **Cluster tags that don't mean what the cluster name says.** Reported, not silently dropped:

   | Strong's | Filed under | What it actually is in these verses |
   |---|---|---|
   | H3513H "to honor: heavy" | **Grief** | **"hardened"** (made heavy) the heart of Pharaoh (Exo 8:15, 32; 9:7, 34; 10:1; 1Sa 6:6; Isa 6:10 "ears heavy") |
   | H2256? "cord" | **Grief** | ropes, bowstring, a group of prophets, clouds (1Ki 20:31; Psa 11:2; 1Sa 10:10; Eze 31:10). [lexical: *ḥebel* = cord / pang]. Not grief here |
   | H7451C "distress: harm" | **Faintness** | "disaster / calamity / harm" — often *evil* done or suffered (brief §6 already flags this) |
   | H0639G "face: anger" | **Anger** | the anger word = "nose/nostrils" [lexical]. Relevant to breath (§2.2) |
   | H5641 / H3582 "to hide" | **Doubt** | hiding, concealing, "destroyed" (Zec 11:8–9) |
   | H7186 "severe" | **Faintness** | "stubborn / hard / harsh" (Eze 3:7 "stubborn heart"; Exo 6:9 "harsh slavery") |
   | H0926 "to dismay" | **Faintness** | also "hasty / rash / quick" (Ecc 5:2 "let not your heart be hasty"; Ecc 7:9 "quick in your spirit") |
   | H6381 "to wonder" | **Astonishment** | "hard" (Jer 32:27 "Is anything too hard for me?"); "special" vow (Lev 27:2) |
   | H5708 / G4509 "filth" | **Dishonor** | literal dirt (1Pe 3:21) as well as moral filth |

---

## 1. Fear & Awe (M01)

**Heart as the one who fears or trembles**
- "his heart trembled greatly" (1Sa 28:5, d1); "his heart trembled for the ark of God" (1Sa 4:13)
- "my heart trembles and leaps out of its place" (Job 37:1)
- "a trembling heart and failing eyes and a languishing soul" (Deu 28:65); "the dread that your heart shall feel" (Deu 28:67)
- "My heart is in anguish within me; the terrors of death have fallen upon me" (Psa 55:4)
- "My heart staggers; horror has appalled me" (Isa 21:4)

**A stable heart means no fear** [Claude reading: the text makes the heart's state the ground of fearlessness]
- "His heart is steady; he will not be afraid" (Psa 112:8); "He is not afraid of bad news; his heart is firm, trusting" (112:7)
- "my heart shall not fear" (Psa 27:3)
- "Let not your heart faint … do not fear" (Deu 20:3; Isa 7:4; Jer 51:46); "Say to those who have an anxious heart, 'Be strong; fear not!'" (Isa 35:4)
- "the people in whose heart is my law; fear not the reproach of man" (Isa 51:7) — what is *in* the heart sets what the person need not fear.

**Reverent fear (of God) placed in or governing the heart**
- "I will put the fear of me in their hearts" (Jer 32:40)
- "I will give them one heart … that they may fear me forever" (Jer 32:39); "unite my heart to fear your name" (Psa 86:11)
- "Oh that they had such a heart as this always, to fear me" (Deu 5:29)
- "my heart stands in awe of your words" (Psa 119:161)
- Opposite: "harden our heart, so that we fear you not" (Isa 63:17); "Blessed is the one who fears the Lord always, but whoever hardens his heart will fall" (Pro 28:14); "Transgression speaks to the wicked deep in his heart; there is no fear of God before his eyes" (Psa 36:1)
- [Claude reading] Hardening of heart is set **against** the fear of God. The fear of God is something God can **put into** the heart.

**Spirit and fear**
- Human, contrite: "humble and contrite in spirit and trembles at my word" (Isa 66:2) [H]
- Given disposition: "God gave us a spirit not of fear but of power and love and self-control" (2Ti 1:7) [X]
- Contrast: "you did not receive the spirit of slavery to fall back into fear, but … the Spirit of adoption" (Rom 8:15) [X+D1]
- Divine Spirit as the ground of not fearing: "My Spirit remains in your midst. Fear not" (Hag 2:5) [D1]
- Divine Spirit endowing "the fear of the Lord": "the Spirit of knowledge and the fear of the Lord" (Isa 11:2) [D1]
- Fear of a spirit-being: "startled and frightened and thought they saw a spirit" (Luk 24:37) [O]
- ◆ "the arrows of the Almighty are in me; my spirit drinks their poison; the terrors of God are arrayed against me" (Job 6:4) [H]

**Flesh and fear**
- "My flesh trembles for fear of you" (Psa 119:120); "shuddering seizes my flesh" (Job 21:6)
- ◆ Flesh as the one *not* to be feared: "in God I trust; I shall not be afraid. What can flesh do to me?" (Psa 56:4)
- [Claude reading] The same word covers the person who trembles and the power one need not dread.

**Soul/life and fear**
- Fear *for* one's life: Jos 9:24; Eze 32:10; 1Sa 22:23
- The right object of fear is defined by the soul: "do not fear those who kill the body but cannot kill the soul. Rather fear him who can destroy both soul and body" (Mat 10:28)
- "awe came upon every soul" (Act 2:43)
- "fearfully and wonderfully made … my soul knows it very well" (Psa 139:14)

**Courage compound as the antidote:** "Take heart; it is I. Do not be afraid" (Mat 14:27; Mar 6:50).

**◆ Fringe**
- **The dread-word used for joy:** "your heart shall **thrill** [*pāḥad*, dread] and exult" (Isa 60:5) [lexical].
- **The tremble-word used for anger:** "Be angry [*rāgaz*, tremble], and do not sin; ponder in your own hearts" (Psa 4:4) [lexical].
- **Inner vs outer:** "our bodies had no rest … fighting without and fear within" (2Co 7:5).

---

## 2. Anger & Wrath (M02)

### 2.1 Human anger in the inner seat
- **Heart:**
  - "his heart rages against the Lord" when folly ruins his way (Pro 19:3)
  - "The godless in heart cherish anger" (Job 36:13)
  - "the mind [heart] of the king of Syria was greatly troubled [*sāʿar*, storm]" (2Ki 6:11)
- **Spirit and bosom in sequence:** "Be not quick in your spirit to become angry, for anger lodges in the heart [bosom] of fools" (Ecc 7:9) [H/T].
  - [Claude reading] Anger *rises* in the spirit and *lodges* in the bosom: two stages, two seats.
- **Spirit as temper:**
  - "slow to anger" // "rules his spirit" (Pro 16:32) [H]; "hasty temper" (Pro 14:29) [T]
  - "their anger [rûaḥ] against him subsided" (Judg 8:3) [T]
- **Spirit provoked or heated:**
  - "his spirit was provoked within him" (Act 17:16) [H]
  - "I went in bitterness in the heat of my spirit" (Eze 3:14) [D3+H]
- **Anger harming the self:** "You who tear yourself [nephesh] in your anger" (Job 18:4).
- **Soul withdrawing from others' anger:** "Let my soul come not into their council … in their anger they killed men" (Gen 49:6).
- **Vexation in heart, pain in body:** "Remove vexation from your heart, and put away pain from your body" (Ecc 11:10); "his work is a vexation. Even in the night his heart does not rest" (Ecc 2:23).

### 2.2 God's anger and the human heart
- **Heart-state provokes or averts wrath:**
  - "because of your hard and impenitent heart you are storing up wrath" (Rom 2:5)
  - "the Lord was angry with Solomon, because his heart had turned away" (1Ki 11:9)
  - "his heart was proud. Therefore wrath came" / "humbled himself for the pride of his heart … the wrath of the Lord did not come" (2Ch 32:25–26)
  - "remove the foreskin of your hearts … lest my wrath go forth like fire" (Jer 4:4)
  - "it is in my heart to make a covenant … that his fierce anger may turn away" (2Ch 29:10)
  - "they made their hearts diamond-hard lest they should hear … Therefore great anger came" (Zec 7:12)
- **God's anger carries out his heart's intents:** "The anger of the Lord will not turn back until he has executed and accomplished the intents of his heart" (Jer 23:20; 30:24 "mind").
- **God's anger and the human spirit:** "nor will I always be angry; for the spirit would grow faint before me" (Isa 57:16) [H].
- **God's indignation and the flesh:** "There is no soundness in my flesh because of your indignation" (Psa 38:3).
- **Flesh and wrath (Paul):** "the passions of our flesh … by nature children of wrath" (Eph 2:3).
- **Craving and anger:** "While the meat was yet between their teeth … the anger of the Lord was kindled" (Num 11:33).

### 2.3 ◆ Anger, breath and nose
- "By the breath of God they perish, and by the blast [rûaḥ] of his anger [nose] they are consumed" (Job 4:9).
- "a stormy wind break out in my wrath" (Eze 13:13).
- [lexical] The Hebrew anger word is "nose / nostrils"; rûaḥ is the breath or blast from it. So anger and breath share a bodily image.

### 2.4 ◆ Divine Spirit followed by human anger
- "the Spirit of God rushed upon Saul when he heard these words, and his anger was greatly kindled" (1Sa 11:6) [D1]
- "the Spirit of the Lord rushed upon him … In hot anger he went back" (Judg 14:19) [D1]
- [Claude reading] Twice, anger follows the Spirit's coming. The text puts them in sequence without comment.

### 2.5 Anger and grief together
- "he looked around at them with anger, grieved at their hardness of heart" (Mar 3:5).

---

## 3. Grief & Lament (M03)

### 3.1 Bitterness — overwhelmingly a soul word
- **Soul:** "bitter in soul" (1Sa 22:2; Job 3:20); "deeply distressed [bitter of nephesh]" (1Sa 1:10); "bitterness of my soul" (Job 7:11; 10:1; Isa 38:15); "dies in bitterness of soul" (Job 21:25); "the Almighty, who has made my soul bitter" (Job 27:2); "they weep over you in bitterness of soul" (Eze 27:31).
- **Heart and spirit also carry it:** "The heart knows its own bitterness" (Pro 14:10); "it is bitter; it has reached your very heart" (Jer 4:18); "made life [rûaḥ] bitter" (Gen 26:35) [H]; "bitterness in the heat of my spirit" (Eze 3:14).
- ◆ **Breath and bitterness:** "he will not let me get my breath, but fills me with bitterness" (Job 9:18).
- ◆ **The bitter-word also means "enraged" and "angry":** "enraged, like a bear robbed of her cubs" (2Sa 17:8, d0); "lest angry fellows fall upon you" (Judg 18:25, d0). [Claude reading] Bitterness of soul shades into rage.

### 3.2 Weeping, sorrow, trouble — all three components
- **Soul:**
  - "my soul will weep in secret for your pride; my eyes will weep bitterly" (Jer 13:17) — inner weeping paired with the eyes'
  - "Was not my soul grieved for the needy?" (Job 30:25)
  - "My soul melts away for sorrow" (Psa 119:28)
  - "My soul is very sorrowful, even to death" (Mat 26:38; Mar 14:34); "Now is my soul troubled" (Joh 12:27)
- **Spirit [H]:**
  - "his spirit was troubled" — after dreams (Gen 41:8; Dan 2:1, 3). ◆ Dreams trouble the spirit; the brief §6 notes dream words sit in T2.
  - "Jesus was troubled in his spirit" (Joh 13:21); "deeply moved in his spirit and greatly troubled" at others' weeping (Joh 11:33); "he sighed deeply in his spirit" (Mar 8:12)
- **Heart:**
  - "Let not your hearts be troubled" (Joh 14:1, 27); "sorrow has filled your heart" (Joh 16:6)
  - "great sorrow and unceasing anguish in my heart" (Rom 9:2); "what are you doing, weeping and breaking my heart?" (Act 21:13)
  - "my heart is sick within me" (Jer 8:18)
- **All three together:** "sorrow in my heart … counsel in my soul" (Psa 13:2); "anguish of my spirit … bitterness of my soul" (Job 7:11); "pain of heart … breaking of spirit" (Isa 65:14).

### 3.3 Authentic vs performed grief — the heart decides
- "return to me with all your heart, with fasting, with weeping, and with mourning … rend your hearts and not your garments" (Joe 2:12–13)
- "They do not cry to me from the heart, but they wail upon their beds" (Hos 7:14)
- "because your heart was tender … you have wept before me, I also have heard you" (2Ch 34:27; 2Ki 22:19)
- "The heart of the wise is in the house of mourning" (Ecc 7:4); "the living will lay it to heart" (Ecc 7:2)

### 3.4 The divine Spirit and grief — in both directions
- **Humans grieve the Spirit:** "do not grieve the Holy Spirit of God" (Eph 4:30); "they rebelled and grieved his Holy Spirit" (Isa 63:10) [D1].
- **The Spirit shares human groaning:**
  - "we … who have the firstfruits of the Spirit, groan inwardly" (Rom 8:23) [D2]
  - "the Spirit himself intercedes for us with groanings too deep for words" (Rom 8:26) [D1]
- **God's own heart grieved:** "it grieved him to his heart" (Gen 6:6).
- [Claude reading] Grief is not only a human inner state. The divine Spirit can be grieved and itself groans.

### 3.5 Body and grief
- "He feels only the pain of his own body, and he mourns only for himself [nephesh]" (Job 14:22)
- "you groan, when your flesh and body are consumed" (Pro 5:11)
- "Because of my loud groaning my bones cling to my flesh" (Psa 102:5)
- ◆ **Frustrated appetite leading to weeping:** "the people of Israel also wept again and said, 'Oh that we had meat to eat!'" (Num 11:4, 13, 18). Appetite (see soul L) and grief meet over food.

### 3.6 ◆ "Heavy" heart = hardened (tagged as Grief)
- See §0. "Pharaoh hardened [made heavy] his heart" (Exo 8:15, 32; 9:34); "Why should you harden your hearts as the Egyptians" (1Sa 6:6); "Make the heart of this people dull, and their ears heavy" (Isa 6:10).
- [Claude reading] The data's cluster assignment links hardness of heart with the grief vocabulary through the "heavy" root. I note it, but I don't treat it as the text's own link.

### 3.7 Grief in giving
- "as he has decided in his heart, not reluctantly [out of grief]" (2Co 9:7) [lexical].

---

## 4. Joy & Gladness (M04)

### 4.1 Where joy is placed
- **Heart:** most joy verses place it in the heart (d1) — "glad of heart", "my heart exults", "the joy of my heart".
- **Soul:** "my soul shall exult in my God" (Isa 61:10); "my soul will rejoice in the Lord" (Psa 35:9); "Gladden the soul of your servant" (Psa 86:4); "A desire fulfilled is sweet to the soul" (Pro 13:19).
- **Spirit [H]:** "my spirit rejoices in God my Savior" (Luk 1:47); "with you in spirit, rejoicing" while absent in body (Col 2:5); "his spirit has been refreshed … we rejoiced" (2Co 7:13).
- **Flesh / whole being:** "my heart is glad, and my whole being rejoices; my flesh also dwells secure" (Psa 16:9; Act 2:26).

### 4.2 What gladdens the heart (as the text names it)
- **God and his salvation:** Psa 13:5; 28:7; 33:21 ("our heart is glad in him, because we trust").
- **His word:** "the precepts of the Lord … rejoicing the heart" (Psa 19:8); "Your testimonies … are the joy of my heart" (Psa 119:111); ◆ "Your words were found, and **I ate them**, and your words became to me a joy and the delight of my heart" (Jer 15:16).
- **God directly:** "You have put more joy in my heart than they have when their grain and wine abound" (Psa 4:7); "God keeps him occupied with joy in his heart" (Ecc 5:20).
- **Wine, oil, perfume, bread:** "wine to gladden the heart of man" (Psa 104:15); "hearts shall be glad as with wine" (Zec 10:7); "Oil and perfume make the heart glad" (Pro 27:9).
- **Food and gladness from God:** "satisfying your hearts with food and gladness" (Act 14:17).
- **People:** a wise son (Pro 23:15; 27:11); "the sweetness of a friend" (Pro 27:9); "a good word makes him glad" (Pro 12:25).
- **The senses:** "The light of the eyes rejoices the heart" (Pro 15:30).
- **Planning peace:** "those who plan peace have joy" (Pro 12:20).

### 4.3 Joy's effect on the body
- "A glad heart makes a cheerful face" (Pro 15:13)
- "A joyful heart is good medicine" (Pro 17:22)
- "your heart shall rejoice; your bones shall flourish" (Isa 66:14)

### 4.4 Joy that is mixed, hidden or morally wrong ◆
- "Even in laughter the heart may ache, and the end of joy may be grief" (Pro 14:13)
- "no stranger shares its joy" (Pro 14:10) — the privacy of joy
- "the heart of fools is in the house of mirth" (Ecc 7:4)
- "wholehearted joy and utter contempt" (Eze 36:5); "rejoiced with all the malice within your soul" (Eze 25:6)
- "let not your heart be glad when he stumbles" (Pro 24:17)
- Haman "joyful and glad of heart" then "filled with wrath" (Est 5:9)
- Michal saw David "dancing and celebrating, and she despised him in her heart" (1Ch 15:29)
- Abraham "laughed and said to himself [in his heart]" (Gen 17:17) — laughter with inner speech

### 4.5 The divine Spirit and joy
- "the joy of the Holy Spirit" (1Th 1:6) [D1]; "filled with joy and with the Holy Spirit" (Act 13:52) [D1]
- "joy in the Holy Spirit" (Rom 14:17) [D1]; "the fruit of the Spirit is love, joy …" (Gal 5:22) [D3]
- Jesus "rejoiced in the Holy Spirit" (Luk 10:21) [D1]
- "Restore to me the joy of your salvation, and uphold me with a willing spirit" (Psa 51:12) [H]

### 4.6 God's joy
- "I will rejoice in doing them good … with all my heart and all my soul" (Jer 32:41).

---

## 5. Shame & Confusion (M07) and Dishonor & Disgrace (M53)

- **Shame enters or breaks the heart:** "Reproaches have broken my heart, so that I am in despair" (Psa 69:20); "I bear in my heart [bosom] the insults of all the many nations" (Psa 89:50).
- **An inner condition protects from shame:**
  - "the people in whose heart is my law; fear not the reproach of man" (Isa 51:7)
  - "May my heart be blameless in your statutes, that I may not be put to shame!" (Psa 119:80)
  - "guard my soul … Let me not be put to shame" (Psa 25:20)
  - "having a good conscience, so that … those who revile … may be put to shame" (1Pe 3:16); "commend ourselves to everyone's conscience" having "renounced disgraceful … ways" (2Co 4:2)
- **Hope not shamed because of the Spirit's work in the heart:** "hope does not put us to shame, because God's love has been poured into our hearts through the Holy Spirit" (Rom 5:5) [D1].
- **Heart → body dishonour:** "God gave them up in the lusts of their hearts to impurity, to the dishonoring of their bodies" (Rom 1:24).
- **Self-humbling becomes reproach:** "When I wept and humbled my soul with fasting, it became my reproach" (Psa 69:10).
- **Heart and curse:** "dullness of heart; your curse will be on them" (Lam 3:65); "if you will not take it to heart … I will send the curse" (Mal 2:2).
- **Lowly spirit and honour:** "better to be of a lowly spirit" (Pro 16:19); "he who is lowly in spirit will obtain honor" (Pro 29:23) [H].
- **Body dirt vs conscience:** "not as a removal of dirt from the body but as an appeal to God for a good conscience" (1Pe 3:21).
- **Filth removed:**
  - "washed away the filth … by a spirit of judgment and by a spirit of burning" (Isa 4:4) [U]
  - "put away all filthiness … receive … the implanted word, which is able to save your souls" (Jam 1:21)
- ◆ **Muteness caused by a spirit:** "a spirit that makes him mute"; "You mute and deaf spirit" (Mar 9:17, 25) [O].

---

## 6. Doubt & Discouragement (M20)

- **Anxiety in the heart:**
  - "Anxiety in a man's heart weighs him down, but a good word makes him glad" (Pro 12:25)
  - "lest your hearts be weighed down with dissipation and drunkenness and cares of this life" (Luk 21:34)
  - "When the cares of my heart are many, your consolations cheer my soul" (Psa 94:19; the "heart" here is English only)
- **Anxiety about life (psychē) and body:** "do not be anxious about your life … nor about your body" (Mat 6:25; Luk 12:22).
- **Divided interests:** "anxious about the things of the Lord, how to be holy in body and spirit" (1Co 7:34) [H].
- **Double-mindedness:** "purify your hearts, you double-minded" (Jam 4:8).
- **Doubt in the heart:** "why do doubts arise in your hearts?" (Luk 24:38); "does not doubt in his heart" (Mar 11:23, M47 row).
- **Disheartened by others:** "you have disheartened the righteous falsely" (Eze 13:22, d0).
- **God searching the anxious heart:** "Search me, O God, and know my heart! Try me and know my thoughts [anxious thoughts]" (Psa 139:23) [lexical].
- **The heart can conceal or not:** "I have not hidden your deliverance within my heart" (Psa 40:10).
- ◆ **God's hidden face and the human spirit or breath:**
  - "My spirit fails! Hide not your face from me" (Psa 143:7) [H]
  - "When you hide your face, they are dismayed; when you take away their breath, they die" (Psa 104:29)
  - "I will not hide my face anymore … when I pour out my Spirit" (Eze 39:29) [D1]
  - The wicked "says in his heart, 'God … has hidden his face'" (Psa 10:11)
  - [Claude reading] God's face turned away is paired with the human spirit or breath failing. God's face turned toward is paired with his Spirit poured out.

---

## 7. Faintness & Despair (M24)

- **Broken heart and crushed spirit — and their healing:**
  - "The Lord is near to the brokenhearted and saves the crushed in spirit" (Psa 34:18, d0)
  - "He heals the brokenhearted and binds up their wounds" (Psa 147:3)
  - "The Spirit of the Lord God is upon me … to bind up the brokenhearted" (Isa 61:1) [D1] — ◆ the divine Spirit on the anointed one directed at the human broken heart
- **Broken spirit and heart as acceptable:** "The sacrifices of God are a broken spirit; a broken and contrite heart … you will not despise" (Psa 51:17); "humble and contrite in spirit" (Isa 66:2).
- **Fainting across every component:**
  - heart: "the whole heart faint" // "the whole head is sick" (Isa 1:5); Lam 1:22; Psa 61:2
  - spirit [H]: Psa 142:3; 143:4; ◆ "When I remember God, I moan; **when I meditate, my spirit faints**" (Psa 77:3)
  - soul: "hungry and thirsty, their soul fainted within them" (Psa 107:5)
  - flesh: "my flesh faints for you" (Psa 63:1)
  - life: ◆ "When my life was fainting away, I remembered the Lord, and my prayer came to you" (Jon 2:7) — fainting turns into remembering and prayer
  - bosom: "their life is poured out on their mothers' bosom" (Lam 2:12)
- **The weary soul revived:** "I will satisfy the weary soul, and every languishing soul I will replenish" (Jer 31:25); "Like cold water to a thirsty soul, so is good news" (Pro 25:25); "my soul thirsts for you like a parched land" (Psa 143:6).
- **Self-affliction of the nephesh (fasting, Day of Atonement):** "you shall afflict yourselves" (Lev 16:29, 31; 23:27, 32; Num 29:7); "Why have we humbled ourselves?" (Isa 58:3, 5); "I afflicted myself with fasting" (Psa 35:13); a vow "to afflict herself" (Num 30:13).
- **Affliction as God's means to reveal the heart:** "that he might humble you, testing you to know what was in your heart" (Deu 8:2).
- **Heart in labour:**
  - "The heart of the warriors of Moab shall be … like the heart of a woman in her birth pains" (Jer 48:41; 49:22)
  - "my stomach churns; my heart is wrung within me" (Lam 1:20)
- **Withering — heart, spirit, and the breath of God:**
  - "My heart is struck down like grass and has withered" (Psa 102:4)
  - "a crushed spirit dries up [withers] the bones" (Pro 17:22)
  - "The grass withers … when the breath of the Lord blows on it; surely the people are grass" (Isa 40:7)
  - [Claude reading] The same withering verb covers the heart, the bones under a crushed spirit, and grass under God's breath.
- **Pride before breaking:** "a haughty spirit before a fall" (Pro 16:18); "Before destruction a man's heart is haughty" (Pro 18:12).
- **Despair:** "I … gave my heart up to despair over all the toil" (Ecc 2:20); "the speech of a despairing man is wind" (Job 6:26).
- **Affliction and empathy:**
  - "You know the heart [nephesh] of a sojourner, for you were sojourners" (Exo 23:9)
  - "if you pour yourself [nephesh] out for the hungry and satisfy the desire [nephesh] of the afflicted" (Isa 58:10) — ◆ one's own nephesh poured out to satisfy another's
- **God's heart in affliction:** "he does not afflict from his heart or grieve the children of men" (Lam 3:33).
- **Suffering in the flesh:** "whoever has suffered in the flesh has ceased from sin" (1Pe 4:1); "in my flesh I am filling up what is lacking in Christ's afflictions" (Col 1:24).
- **Lose heart / take heart:** "not to lose heart over what I am suffering" (Eph 3:13); "In the world you will have tribulation. But take heart" (Joh 16:33).

---

## 8. Astonishment & Wonder (M48)

- **Wonders set against a hardened heart:** "I will harden Pharaoh's heart, and though I multiply my signs and wonders" (Exo 7:3; 4:21; 11:10).
- **Soul knowing God's wonders:** "Wonderful are your works; my soul knows it very well" (Psa 139:14); "Your testimonies are wonderful; therefore my soul keeps them" (Psa 119:129).
- **The whole heart recounting wonders:** "I will give thanks to the Lord with my whole heart; I will recount all of your wonderful deeds" (Psa 9:1).
- **The humble heart not reaching for wonders:** "my heart is not lifted up … I do not occupy myself with things too great and too marvelous for me" (Psa 131:1).
- **Amazement at spirits obeying:** Mar 1:27; Luk 4:36 [O].

---

## 9. Cross-cutting observations for Batch A [Claude reading]

1. **Each component has its own feeling profile in the text, but they overlap:**
   - *Heart:* the widest range, including joy, fear, anger, grief, anxiety, despair.
   - *Soul:* strongly **bitterness, longing, weariness, being troubled**.
   - *Spirit (human):* **troubled, broken or crushed, faint, provoked, rejoicing**, and **temper**.
   - *Flesh:* **trembles, faints, rejoices**, and is afflicted by divine indignation.
2. **The heart's state governs whether a feeling takes hold.** A firm heart has no fear, a blameless heart no shame, a hardened heart no fear of God. A proud heart brings wrath; a humbled heart averts it.
3. **Feelings pass between the inner seat and the body in both directions:**
   - glad heart → face; joyful heart → medicine; crushed spirit → dry bones
   - wine, bread, perfume, eyes' light → heart; meat craved → weeping
4. **The divine Spirit is involved in feeling:**
   - it gives joy (1Th 1:6; Act 13:52) and grounds the absence of fear (Hag 2:5; Rom 8:15)
   - it can be grieved (Eph 4:30), and it groans (Rom 8:26)
   - twice, its coming is followed by human anger (1Sa 11:6; Judg 14:19)
   - it is sent to heal the broken heart (Isa 61:1)
5. **Breath and wind tie feeling to the body and to God:** the blast of God's anger from the "nose"; "fills me with bitterness" instead of breath; the breath that withers grass; despair's speech is "wind".
6. **God is given the same feelings in heart and soul:** his heart grieved (Gen 6:6), his joy with all heart and soul (Jer 32:41), anger executing the intents of his heart (Jer 23:20).

---

## 10. Next

- **Batch B (knowing / thinking / speaking / hearing)** is next, unless you'd like to redirect.
- Spirit classes will be applied throughout.
- The v1 question on recording misfiled cluster tags beyond these write-ups is now **Ruling R7** (§R).
