# M47 × Willing / Desiring / Orientation — Batch C (v2)

**Date:** 2026-09-27
**Supersedes:** v1 (same date; `archive/`). v2 adds §R (items for researcher ruling), §X (cluster cross-reference) and DB assignment sources. The analysis in §1–§11 is unchanged.
**Use:** this file is meant to accompany the analysis of each cluster listed below. Start at §X to find the sections and flagged Strong's for your cluster.
**Data:** `cluster-M47-other-m-code-pairs-with-distance-20260927.csv` — pairs where the other word is in:
- M18 Desire & Longing
- M64 Will & Resolve
- M28 Envy & Greed
- M69 Self-Control & Zeal
- M34 Patience & Perseverance
- M68 Hope & Waiting
- M83 Seeking & Inquiring
- M11 Turning & Repentance
- M30 Rebellion & Stubbornness
- M75 Disobedience & Lawlessness
- M66 Madness & Recklessness
- M67 Sloth & Diligence

**896 pairs in 578 verses; all read.**

**Spirit classes** (`M47-spirit-distinction-v1-20260927.md`, joined per verse from `M47-spirit-classification-v1-20260927.csv`):
- **[D1/D2]** divine
- **[D3]** divine per ESV only
- **[H1/H2]** human
- **[O]** other being
- **[X]** disposition
- **[W]** wind / breath
- **[U]** not determinable
- Combined classes (e.g. [D1+O], [U+H1]) are carried as the CSV gives them.
- Wind-sense rûaḥ (H7307H) is not in the classification CSV; it is marked *wind* in the text.

Tags: **[Claude reading]**, **[lexical]**, **[verify]**, ◆ fringe. Not statistical.

**Component profile (verses per cluster, a verse counted once per component)** — orientation only, not a finding:

| Cluster | heart | soul | spirit / wind | flesh | conscience | *pneumatikos* |
|---|---|---|---|---|---|---|
| M18 Desire | 81 | 87 | 38 | 26 | 2 | 5 |
| M64 Will | 26 | 15 | 9 | 5 | 0 | 0 |
| M28 Envy/Greed | 12 | 8 | 5 | 7 | 1 | 4 |
| M69 Zeal | 1 | 0 | 5 | 2 | 0 | 1 |
| M34 Patience | 26 | 8 | 8 | 2 | 2 | 0 |
| M68 Hope | 12 | 19 | 6 | 1 | 1 | 0 |
| M83 Seeking | 33 | 54 | 13 | 4 | 0 | 0 |
| M11 Turning | 41 | 13 | 13 | 4 | 0 | 0 |
| M30 Rebellion | 40 | 32 | 11 | 11 | 1 | 0 |
| M75 Disobedience | 11 | 1 | 3 | 2 | 0 | 0 |
| M66 Madness | 4 | 0 | 2 | 0 | 0 | 0 |
| M67 Sloth | 1 | 0 | 1 | 0 | 0 | 0 |

Spirit classes present in the batch (verses): D1 24 · D2 9 · D3 8 · H1 24 · H2 2 · X 6 · O 5 · U 4 · W 2 · combined 5.

**Assignment source.** Cluster membership is from `iba/app/db/iba.db` → `cluster_strong` (active rows, read-only query, 2026-09-27). "Source" is the assignment route recorded there:
- `old-system-migration` — carried over from the old system; no confidence recorded
- `heuristic-family-grouping-v1-20260905` — family heuristic
- `llm-allocation-v1_3-20260811` — LLM allocation, with a confidence value
- `auto-precedent`

---

## R. Items for researcher ruling

Five decisions are needed. For each one: the cluster(s) it affects, the Strong's number, what the DB currently records, the evidence, the options, and my recommendation.
- **R1–R3 and R5** are **cluster-membership** questions for `cluster_strong`.
- **R4** is a **spirit-classification** question for `M47-spirit-classification-v1-20260927.csv`.
- Nothing has been changed in the DB or the CSV.
- The process question (whether to record misfiles beyond the write-ups) is **Batch A R7** and applies here too.

### R1 — H2638 "lacking" in M18 Desire & Longing
| | |
|---|---|
| **Cluster(s)** | M18 (current); M47 (partner) |
| **Strong's** | H2638 *ḥāsēr* "lacking, in want of" |
| **DB now** | M18 · `heuristic-family-grouping-v1-20260905` · confidence *heuristic* · rationale "family=desire-longing-appetite" |
| **Evidence** | 14 pairs. 12 verses are "lacking heart" = "lacks sense", H2638 + H3820A at d1: Pro 6:32; 7:7; 9:4, 16; 10:13, 21; 11:12; 12:11; 15:21; 17:18; 24:30; Ecc 10:3. Also Ecc 6:2 "he lacks nothing". See §1.5. |
| **Issue** | The word states a lack or deficiency, not a desire. In the Proverbs verses, what is lacking is the heart itself (folly), not something wanted. |
| **Options** | (a) keep in M18; (b) move to M16 Wisdom & Folly (fits the Proverbs usage); (c) move to another cluster you name; (d) keep in M18 with an alternative-cluster note. |
| **Recommendation** | **(b) M16** [Claude reading], or at least (d). |
| **Ruling** | ______ |

### R2 — H8003 "complete / whole" in M34 Patience & Perseverance
| | |
|---|---|
| **Cluster(s)** | M34 (current); M47 (partner) |
| **Strong's** | H8003 *shālēm* "complete, whole, at peace" |
| **DB now** | M34 · `llm-allocation-v1_3-20260811` · confidence **high** · rationale "single-cluster precedent (P1+P2)" |
| **Evidence** | 20 M34 pairs, nearly all *lēv shālēm* "whole heart / wholly true" at d1: 1Ki 8:61; 11:4; 15:3, 14; 1Ch 12:38; 28:9; 29:9, 19; 2Ch 15:17; 16:9; 19:9; 25:2; 2Ki 20:3; Isa 38:3. Also "blameless" (Job 9:21; Pro 29:10). See §5.1. |
| **Issue** | The sense is an undivided, integral heart toward God, not endurance. The "high" confidence rests on precedent, not on the verse sense. |
| **Options** | (a) keep in M34; (b) move to M12 Righteousness & Integrity; (c) move to M33 Rest & Peace (the *shālôm* family); (d) keep with an alternative-cluster note. |
| **Recommendation** | **(b) M12** [Claude reading]. The verses evaluate kings by the integrity of their heart. |
| **Ruling** | ______ |

### R3 — H1793A "contrite" in M11 Turning & Repentance
| | |
|---|---|
| **Cluster(s)** | M11 (current); M47 (partner); M09 Humility & Lowliness (candidate) |
| **Strong's** | H1793A *dakkāʾ* "crushed, contrite" |
| **DB now** | M11 · `old-system-migration` · no confidence · no rationale |
| **Evidence** | "saves the crushed in spirit" (Psa 34:18, d1); "a contrite and lowly spirit … the heart of the contrite" (Isa 57:15, d2). See §8.4. |
| **Issue** | The verses describe a crushed or broken state of spirit and heart that God accepts. No act of turning is described. The word is closer to brokenness and lowliness than to repentance. |
| **Options** | (a) keep in M11 (contrition as the inner side of repentance); (b) move to M09 Humility & Lowliness (paired with "lowly" in Isa 57:15); (c) move to M24 Faintness & Despair (crushed / broken); (d) keep with an alternative-cluster note. |
| **Recommendation** | **(b) M09** [Claude reading]. Not strong: (a) is theologically defensible. |
| **Ruling** | ______ |

### R4 — Psa 106:33: whose spirit is "bitter"?
| | |
|---|---|
| **Cluster(s)** | M47 spirit classification; M30 (partner, via H4784) |
| **Strong's** | H7307G *rûaḥ* + H4784 *mārâ* "to rebel" |
| **Classification now** | **[H1]** human (Moses' spirit), in `M47-spirit-classification-v1-20260927.csv` |
| **Evidence** | ESV: "they made his spirit bitter, and he spoke rashly with his lips". Hebrew: *himrû ʾet-rûḥô* "they **rebelled against** his spirit" [lexical]. Isa 63:10 uses the same verb of God's Holy Spirit: "they rebelled and grieved his Holy Spirit". |
| **Issue** | The M30 tag (H4784 "to rebel") is lexically correct. The question is whose spirit. If it is Moses', the people embittered his spirit and he spoke rashly. If it is God's, the people rebelled against God's Spirit, and Moses then spoke rashly. |
| **Options** | (a) keep [H1]; (b) change to [D1]; (c) mark [U] (not determinable), noting both readings. |
| **Recommendation** | **(c) [U]** with both readings noted. The text supports either [Claude reading]. |
| **Ruling** | ______ |

### R5 — 1Sa 30:6 "bitter in soul" tagged H4784 "to rebel" (M30)
| | |
|---|---|
| **Cluster(s)** | M30 Rebellion & Stubbornness (current tag); M03 Grief & Lament (where *mārar* H4843 and *mar* H4751 sit) |
| **Strong's** | Tagged H4784 *mārâ* "to rebel"; expected H4843 *mārar* "be bitter" |
| **DB now** | H4784 → M30 · `old-system-migration`. H4843 and H4751 → M03 · `old-system-migration`. |
| **Evidence** | "all the people were bitter in soul, each for his sons and daughters" (1Sa 30:6, d1). The sense is grief and bitterness, not rebellion. |
| **Issue** | This is a verse-level **tagging** question (which Strong's the source assigned), not a cluster-membership question. If the tag is a lemma confusion (*mārâ / mārar*), the pair belongs with M03, not M30. |
| **Options** | (a) accept the tag as given; (b) treat it as mis-lemmatised and read the verse with M03; (c) check the source tagging (STEP) before deciding. |
| **Recommendation** | **(c) then (b)** [verify]. |
| **Ruling** | ______ |

---

## X. Cluster cross-reference — where each cluster appears in this file

Use this when the file accompanies a cluster's analysis. It lists the sections to read, and the Strong's in that cluster that are flagged in §0 or §R. "Misfile" means the word's sense **in these verses** does not match the cluster. It is **not** a claim that the Strong's is wrongly assigned everywhere.

| Cluster | Sections | Flagged Strong's (DB source · confidence) |
|---|---|---|
| **M18** Desire & Longing | §1 (all); §1.6 wine-merry heart; §1.9 wind; §1.11 flesh | **R1** H2638 (heuristic). Generic "good / better": H2896A, H2895 (heuristic) — §0.4 |
| **M64** Will & Resolve | §2; also §1.12 (God's will) | H2803I "devise" at Jon 1:4 (heuristic) — §0.8 |
| **M28** Envy & Greed | §3; §1.8 jealousy | H6424 *pālas* at Psa 58:2; 78:50 (LLM · high) — §0.8 |
| **M69** Self-Control & Zeal | §4 | — |
| **M67** Sloth & Diligence | §4 | — |
| **M34** Patience & Perseverance | §5 | **R2** H8003 (LLM · high) |
| **M68** Hope & Waiting | §6 | H3176G at Jer 4:19 (Kethiv/Qere *yāḥal / ḥûl* [verify]) and at 2Sa 18:14 (literal heart) (heuristic) — §0.8 |
| **M83** Seeking & Inquiring | §7; §7.5 "seek my life" idiom (~40 verses) | — (idiom noted, not a misfile) |
| **M11** Turning & Repentance | §8 | **R3** H1793A (old-system). H5493G/H at 1Ki 15:14; Pro 9:4, 16 (heuristic); G5290 at Luk 4:1, 14 (auto-precedent) — §0.8 |
| **M30** Rebellion & Stubbornness | §9.1–9.7 | **R4** (spirit class, Psa 106:33) · **R5** H4784 at 1Sa 30:6 (old-system). Misfiles: H6569 "dung" at Exo 29:14; Lev 4:11; 8:17; 16:27; Num 19:5 (heuristic); H7419 at Eze 32:5 and H4651 at Job 41:23 (heuristic); H0014 at 1Ch 11:19; 2Sa 23:17 (old-system); H5800A at 2Ki 2:2, 4, 6; 4:30; Gen 2:24 (heuristic). H5620 at 1Ki 21:5 is already review-flagged in the DB (LLM · low · review_flag=1). |
| **M75** Disobedience & Lawlessness | §9.3 hardening; §9.8 | H7280C at Job 7:5 (heuristic) — §0.8 |
| **M66** Madness & Recklessness | §10 | — |
| **M47** Inner Seat | all; §11 cross-cutting | R4 (spirit class) |
| Candidate receiving clusters | M16 Wisdom & Folly (R1); M12 Righteousness & Integrity / M33 Rest & Peace (R2); M09 Humility & Lowliness / M24 Faintness & Despair (R3); M03 Grief & Lament (R5) | — |
| All batches | — | **Batch A R7** process ruling |

---

## 0. Data notes

1. **Pre-filters from the handoff do not apply here.** None of "Holy Spirit" (M61), "declares the Lord" (M42) or "Lord of hosts" (M72) falls in Batch C clusters. Nothing was removed.
2. **"Seek my life" is one idiom, not inner seeking.** About 40 of the 96 M83 verses are *biqqēš nephesh* — "seek (someone's) life" (1Sa 20:1; 23:15; 1Ki 19:10, 14; Jer 11:21; 19:7; 21:7; 22:25; 34:20–21; 44:30; 46:26; 49:37; Psa 35:4; 38:12; 40:14; 54:3; 63:9; 70:2; 86:14; Mat 2:20; Rom 11:3; etc.). Here *nephesh* is **life as the object of hostile pursuit**. It is reported in §7.5 and not mixed with the soul that seeks.
3. **"Lacks sense" is "lacking heart"** (H2638 + H3820A, d1): Pro 7:7; 9:4, 16; 10:13, 21; 11:12; 12:11; 15:21; 17:18; 24:30; 6:32; Ecc 10:3. H2638 "lacking" is filed under M18 Desire. It is a lack, not a desire. See §1.5. **→ Ruling R1.**
4. **"Pleasant" (H2896A *ṭôv*) is mostly generic "good / better".** It accounts for 59 M18 pairs. The inner-being uses ("glad / merry / good of heart", "good to the soul", "better … in spirit") are kept in §1.6. Generic "better" is noted and not used (Num 11:18; Judg 9:2; Dan 1:15; 2Sa 18:3; Gen 1:21).
5. **"Striving after wind"** (H7469 *reʿût rûaḥ* "longing/pursuit" + rûaḥ *wind*, d1) is the Ecclesiastes refrain (Ecc 1:14; 2:11, 17, 26; 4:4, 6; 6:9). It is correctly a desire + wind pairing. See §1.9.
6. **"Whole heart" is *lēv shālēm*** (H8003 "complete", d1). It is filed under **M34 Patience**. In the verses it means an undivided, integral heart, not endurance. See §5.1. **→ Ruling R2.**
7. **"Contrite" (H1793A) is filed under M11 Turning.** The verses are about a crushed spirit and heart (Psa 34:18; Isa 57:15), not about turning. They are kept in §8.4. **→ Ruling R3.**
8. **Misfiled tags, noted and not used:**
   - H6569 "refuse" = *dung*, read as "refuse" (M30): the flesh-skin-dung-burned sacrificial verses (Exo 29:14; Lev 4:11; 8:17; 16:27; Num 19:5); also Eze 32:5 "carcass" and Job 41:23 "folds of his flesh".
   - H0014 "be willing" filed under M30 because it appears as "would not" (1Ch 11:19; 2Sa 23:17 "he would not drink it"). It is kept only where it is the heart's or spirit's refusal (Exo 10:27; Deu 2:30; Eze 3:7).
   - "As you yourself live, I will not leave you" (2Ki 2:2, 4, 6; 4:30): an oath formula. H5800A "leave" → M30.
   - Gen 2:24 "leave … one flesh" → M30.
   - Jer 4:19 "I writhe in pain" tagged H3176G "to wait" (M68). The Kethiv/Qere allows *yāḥal* "wait" or *ḥûl* "writhe" [lexical; verify]. ESV follows *ḥûl*.
   - 2Sa 18:14 "waste time … heart of Absalom" (literal heart; M68).
   - Psa 58:2 "deal out" and Psa 78:50 "made a path" tagged "to envy" (H6424 *pālas* "weigh / level") — M28.
   - Pro 9:4, 16 "turn in here" (M11); Luk 4:1, 14 "returned" (travel, M11).
   - "High places taken away" beside "heart wholly true" (1Ki 15:14; 2Ch 15:17; 20:33; 17:6; M11).
   - Jon 1:4 "the ship threatened [*thought*] to break up" (H2803 "devise", M64) ◆ — a lexical curiosity only.
   - Lev 7:18 "credited"; Exo 35:35; 36:8 "designer / skillfully" (M64). The last two tie back to "wise of heart" = skill (Batch B §2.1).
   - Col 2:1 "face" and Gal 1:16 "anyone" (G4561 "flesh" behind idioms).
   - Job 7:5 "my skin hardens" (literal body; M75).
9. **Flesh = meat, appetite = nephesh** in the Deuteronomy meat laws (Deu 12:15, 20–21; 14:26): "because you crave [*your nephesh desires*] meat" (d0/d1). This is the plainest place where *nephesh* is **appetite**. It is kept in §1.1.
10. **Distance note.** Positions are in original-language word order [verify]. d0 = one token carries both tags (e.g. Deu 12:20 "crave" = *nephesh* + desire; 2Pe 2:10 "lust" = flesh + desire).

---

## 1. Desire and longing (M18)

### 1.1 The soul as the desiring faculty — appetite
- **Plain appetite:**
  - "because you crave meat [*your soul desires*], you may eat meat whenever you desire" (Deu 12:20, d0)
  - "whatever your appetite craves" (Deu 14:26); "as much as you desire" (Deu 12:15, 21)
  - "if the man said … take as much as you wish [*your soul desires*]" (1Sa 2:16)
- **Appetite as a driver:** "A worker's appetite works for him; his mouth urges him on" (Pro 16:26).
- **Appetite that turns away:**
  - "his life loathes bread, and his appetite the choicest food" (Job 33:20)
  - "My appetite refuses to touch them" (Job 6:7; §9)
- **The soul desires what it lacks:** "no first-ripe fig that my soul desires" (Mic 7:1).
- **Soul-desire as rule and scope:** "reign over all that your soul desires" (1Ki 11:37; 2Sa 3:21 "all that your heart [*nephesh*] desires"); "according to all your heart's [*nephesh*] desire" (1Sa 23:20).
- **Desire in the person:** "The soul of my son Shechem longs for your daughter" (Gen 34:8).
- [Claude reading] **In the OT, *nephesh* is the ordinary word for "want".** Much of what English renders "you desire / wish / crave" is literally "your soul". Desire is not something the soul *has*; desire is what the soul *is doing*.

### 1.2 The soul longing for God
- "As a deer pants for flowing streams, so pants my soul for you, O God. My soul thirsts for God" (Psa 42:1–2)
- "my soul thirsts for you; my flesh faints for you" (Psa 63:1) — **soul and flesh together**
- "My soul longs, yes, faints for the courts of the Lord; my heart and flesh sing for joy" (Psa 84:2) — **soul, heart and flesh**
- "My soul is consumed with longing for your rules" (Psa 119:20); "My soul longs for your salvation" (Psa 119:81)
- "your name and remembrance are the desire of our soul" (Isa 26:8)
- **Soul yearns, spirit seeks:** "My soul yearns for you in the night; my spirit within me earnestly seeks you" (Isa 26:9) [H1]
- ◆ **Longing as thirst:** "Like cold water to a thirsty soul, so is good news" (Pro 25:25; Batch B §3.3).

### 1.3 The heart's desire
- **Granted:**
  - "You have given him his heart's desire" (Psa 21:2)
  - "Delight yourself in the Lord, and he will give you the desires of your heart" (Psa 37:4)
  - "you hear the desire of the afflicted; you will strengthen their heart" (Psa 10:17)
- **Deferred:** "Hope deferred makes the heart sick, but a desire fulfilled is a tree of life" (Pro 13:12).
- **Heart-desire toward sin:**
  - "Do not desire her beauty in your heart" (Pro 6:25)
  - "everyone who looks at a woman with lustful intent has already committed adultery with her in his heart" (Mat 5:28)
  - "God gave them up in the lusts of their hearts" (Rom 1:24)
  - "flee youthful passions … call on the Lord from a pure heart" (2Ti 2:22)
- **Desire governed in the heart:** "firmly established in his heart … having his desire under control … determined this in his heart" (1Co 7:37).
- ◆ **Heart present, body absent:** "torn away from you … in person not in heart, we endeavored … with great desire to see you" (1Th 2:17).
- [Claude reading] **The heart is where desire is either consented to or governed.** Mat 5:28 places the act itself in the heart before any deed.

### 1.4 The willing heart and the moved spirit — freewill
- "From every man whose heart moves him" (Exo 25:2)
- "everyone whose heart stirred him, and everyone whose spirit moved him" (Exo 35:21) [H1] — **heart and spirit in parallel**, the same verb (*nādav*)
- "All … whose heart moved them … as a freewill offering" (Exo 35:29)
- "with a whole heart they had offered freely" (1Ch 29:9); "In the uprightness of my heart I have freely offered" (1Ch 29:17)
- "serve him with a whole heart and with a willing [delighting] soul [*nephesh*]" (1Ch 28:9)
- "My heart goes out to the commanders … who offered themselves willingly" (Judg 5:9)
- ◆ **Conscience as disposed:** "you are disposed [*willing*] to go … without raising any question on the ground of conscience" (1Co 10:27); "a clear conscience, desiring to act honorably" (Heb 13:18).
- [Claude reading] **Willingness belongs to heart and spirit together.** The heart "moves" the person; the spirit "impels" them. This matches the Batch B finding that the stirred heart puts God-given skill to work (Exo 35–36).

### 1.5 "Lacking heart" — the heart as what is missing
- "a young man lacking sense [*heart*]" (Pro 7:7); "him who lacks sense" (Pro 9:4, 16); "fools die for lack of sense" (Pro 10:21)
- "He who commits adultery lacks sense; he who does it destroys himself [*his nephesh*]" (Pro 6:32) — **lacking heart destroys the soul**
- "Folly is a joy to him who lacks sense" (Pro 15:21); "the vineyard of a man lacking sense" (Pro 24:30)
- [Claude reading] In Proverbs "sense" is literally "heart". A fool is **not someone with a bad heart but someone without one**: the heart is the capacity that is absent (cf. Batch B §2.2).

### 1.6 Good, glad and better — the inner seat's well-being
- **Glad / merry heart:**
  - "joyful and glad of heart" (1Ki 8:66; 2Ch 7:10; Est 5:9)
  - "the cheerful of heart has a continual feast" (Pro 15:15)
  - "drink your wine with a merry heart" (Ecc 9:7)
- ◆ **The merry heart made vulnerable by wine:**
  - "Nabal's heart was merry within him, for he was very drunk" (1Sa 25:36)
  - "when Amnon's heart is merry with wine … strike Amnon" (2Sa 13:28)
  - "when the heart of the king was merry with wine, he commanded" (Est 1:10)
  - "when their hearts were merry, they said, 'Call Samson'" (Judg 16:25)
  - [Claude reading] Four narratives in which a wine-merry heart is the moment of exposure or rash command.
- **Good to the soul:**
  - "knowledge will be pleasant to your soul" (Pro 2:10)
  - "Gracious words are … sweetness to the soul and health to the body" (Pro 16:24)
  - "your consolations cheer my soul" (Psa 94:19) — against "the cares of my heart"
  - "find rest for your souls" (Jer 6:16)
- **"Better in spirit":**
  - "the patient in spirit is better than the proud in spirit" (Ecc 7:8) [H1]
  - "better to be of a lowly spirit with the poor" (Pro 16:19) [H1]
  - "he who rules his spirit [is better] than he who takes a city" (Pro 16:32) [H1]
  - "he who has a cool [*precious*] spirit is a man of understanding" (Pro 17:27) [H1]
- **Good Spirit [D1]:** "You gave your good Spirit to instruct them" (Neh 9:20); "Teach me to do your will … Let your good Spirit lead me" (Psa 143:10).
- ◆ **Harmful spirit, made well:** "whenever the harmful spirit from God was upon Saul … Saul was refreshed and was well" (1Sa 16:16, 23) [O].
- ◆ **Sorrow better than laughter:** "by sadness of face the heart is made glad" (Ecc 7:3); "the living will lay it to heart" (Ecc 7:2).

### 1.7 Life as precious — the valued soul
- "my life was precious in your eyes this day" (1Sa 26:21); "let my life be precious in your sight" (2Ki 1:13–14)
- "precious is their blood in his sight" (Psa 72:14)
- "the ransom of their life is costly" (Psa 49:8)
- "a married woman hunts down a precious life" (Pro 6:26)
- "Because you are precious in my eyes … I give … peoples in exchange for your life" (Isa 43:4)
- **Refusing to treat one's own life as precious:** "I do not account my life of any value nor as precious to myself" (Act 20:24).
- ◆ **Wanting to save the soul-life loses it:** "whoever would save his life will lose it" (Mat 16:25; Mar 8:35; Luk 9:24); "Whoever seeks to preserve his life" (Luk 17:33, §7).
- ◆ **Life "better" gone:** "take my life from me, for it is better for me to die" (Jon 4:3, 8); "take away my life, for I am no better than my fathers" (1Ki 19:4).

### 1.8 Jealousy and envy
- **Spirit of jealousy [X]:** "if the spirit of jealousy comes over him and he is jealous of his wife" (Num 5:14, 30).
- **Heart envy:**
  - "Let not your heart envy sinners" (Pro 23:17)
  - "A tranquil heart gives life to the flesh, but envy makes the bones rot" (Pro 14:30) — **heart state → flesh**
  - "if you have bitter jealousy and selfish ambition in your hearts" (Jam 3:14)
- **Godly zeal:** "Set me as a seal upon your heart … jealousy is fierce as the grave" (Song 8:6).
- **Zeal and the threatened life:** "I have been very jealous for the Lord … they seek my life" (1Ki 19:10, 14).
- **God's jealousy:** "in my hot jealousy against … Edom, who gave my land to themselves … with wholehearted joy and utter contempt [*nephesh*]" (Eze 36:5).
- ◆ **Jealousy for the Spirit's spread:** "Are you jealous for my sake? Would that … the Lord would put his Spirit on them!" (Num 11:29) [D1].
- ◆ **God's jealous yearning over the spirit:** "He yearns jealously over the spirit that he has made to dwell in us" (Jam 4:5) [U] — the classification leaves open whether this is the human spirit or God's.

### 1.9 ◆ Desire aimed at wind
- "all is vanity and a striving after wind" (Ecc 1:14; 2:11, 17, 26; 4:4, 6)
- **Appetite and wind in one verse:** "Better is the sight of the eyes than the wandering of the appetite [*nephesh*]: this also is vanity and a striving after wind" (Ecc 6:9)
- **Envy as the root:** "all toil and all skill in work come from a man's envy of his neighbor. This also is … a striving after wind" (Ecc 4:4)
- **Animal desire and wind:** "a wild donkey … in her heat [*the desire of her nephesh*] sniffing the wind! Who can restrain her lust?" (Jer 2:24); "they pant for air [*wind*] like jackals" (Jer 14:6)
- [Claude reading] Ecclesiastes names the object of restless desire as *rûaḥ* in its wind sense. Jer 2:24 puts the *nephesh*'s craving and the gulping of wind in one image. **Desire here is breath-hunger.**

### 1.10 Evil desire of the soul
- "the great man utters the evil desire of his soul" (Mic 7:3)
- "The soul of the wicked desires evil" (Pro 21:10)
- "the wicked boasts of the desires of his soul, and the one greedy for gain … renounces the Lord" (Psa 10:3)
- "These have chosen their own ways, and their soul delights in their abominations" (Isa 66:3)
- "The Lord … thwarts the craving [*nephesh*] of the wicked" (Pro 10:3)
- "The soul of the sluggard craves and gets nothing" (Pro 13:4)
- **Unsatisfied soul:** "a man to whom God gives wealth … so that he lacks nothing of all that he desires [*for his nephesh*], yet God does not give him power to enjoy them" (Ecc 6:2); "his soul is not satisfied with life's good things" (Ecc 6:3).
- **Craving and meat:** "the rabble … had a strong craving … 'Oh that we had meat [*flesh*] to eat!'" (Num 11:4).
- **Desire without knowledge:** "Desire [*nephesh*] without knowledge is not good" (Pro 19:2; Batch B §1.5).

### 1.11 The desires of the flesh (NT)
- "walk by the Spirit, and you will not gratify the desires of the flesh" (Gal 5:16) [D3]
- "the desires of the flesh are against the Spirit, and the desires of the Spirit are against the flesh … to keep you from doing the things you want to do" (Gal 5:17) [D3] — **the Spirit also desires**
- "those who belong to Christ Jesus have crucified the flesh with its passions and desires" (Gal 5:24)
- "carrying out the desires of the flesh and the mind" (Eph 2:3); "the desires of the flesh and the desires of the eyes" (1Jo 2:16)
- "make no provision for the flesh, to gratify its desires" (Rom 13:14)
- "the passions of the flesh, which wage war against your soul" (1Pe 2:11) — **flesh against soul**
- "no longer for human passions but for the will of God" (1Pe 4:2)
- "the lust of defiling passion" (2Pe 2:10, d0); "sensual passions of the flesh" (2Pe 2:18)
- "born, not of blood nor of the will of the flesh nor of the will of man, but of God" (Joh 1:13)
- ◆ **Desire without ability:** "nothing good dwells in me, that is, in my flesh. For I have the desire to do what is right, but not the ability" (Rom 7:18).
- [Claude reading] In the OT the *soul* desires (§1.1–1.2, §1.10). In the NT the flesh becomes the main subject of desire, and in 1Pe 2:11 it is set **against** the soul.

### 1.12 Divine desire and delight
- **God's soul delights:**
  - "my chosen, in whom my soul delights; I have put my Spirit upon him" (Isa 42:1) [D1]
  - "my beloved with whom my soul is well pleased. I will put my Spirit upon him" (Mat 12:18) [D1]
  - "if he shrinks back, my soul has no pleasure in him" (Heb 10:38)
- **God desires and does:** "What he [*his nephesh*] desires, that he does" (Job 23:13).
- **God's heart and will:**
  - "a man after my heart, who will do all my will" (Act 13:22)
  - "according to all that was in my heart" (2Ki 10:30)
  - "The king's heart is a stream of water in the hand of the Lord; he turns it wherever he will" (Pro 21:1)
- **God's pleasure in a human heart-intention:** "it was in your heart to build a house … you did well that it was in your heart" (1Ki 8:18; 2Ch 6:8).
- **The will of God from the heart:** "doing the will of God from the heart [*psychē*]" (Eph 6:6); "those who suffer according to God's will entrust their souls to a faithful Creator" (1Pe 4:19).
- ◆ **Soul-offering as the will of the Lord:** "it was the will of the Lord to crush him … when his soul makes an offering for guilt … the will of the Lord shall prosper" (Isa 53:10).
- ◆ **Wind and Spirit that will:** "The wind blows where it wishes … So it is with everyone who is born of the Spirit" (Joh 3:8) [W+D3]; "prophecy was never produced by the will of man … carried along by the Holy Spirit" (2Pe 1:21) [D1].

### 1.13 Longing for the spiritual
- "long for the pure spiritual milk" (1Pe 2:2)
- "earnestly desire the spiritual gifts" (1Co 14:1); "eager for manifestations of the Spirit" (1Co 14:12) [D2]
- "I long to see you, that I may impart … some spiritual gift" (Rom 1:11)
- "The Spirit and the Bride say, 'Come.' … let the one who is thirsty come; let the one who desires take the water of life" (Rev 22:17) [D2]
- ◆ "things into which angels long to look" (1Pe 1:12) — beside "the Holy Spirit sent from heaven" [D1]

---

## 2. Will, resolve, planning and choosing (M64)

### 2.1 The heart plans and devises
- "The heart of man plans his way, but the Lord establishes his steps" (Pro 16:9)
- **Evil devised in the heart:**
  - "who plan evil things in their heart" (Psa 140:2)
  - "let none of you devise evil against another in your heart" (Zec 7:10; 8:17)
  - "thoughts will come into your mind, and you will devise an evil scheme" (Eze 38:10)
  - "his heart does not so think; but it is in his heart to destroy" (Isa 10:7)
- **Invented from one's own heart:**
  - "the month that he had devised from his own heart" (1Ki 12:33) — Jeroboam's feast
  - "you are inventing them out of your own mind" (Neh 6:8)
  - Compare prophecy "from their own hearts" (Batch B §6).
- **Plans and the inner seat:** "they plot to take my life" (Psa 31:13); "devise evil against me … seek after my life" (Psa 35:4).

### 2.2 The intention of the heart
- "every intention of the thoughts of his heart was only evil continually" (Gen 6:5)
- "the intention of man's heart is evil from his youth" (Gen 8:21) — said by the Lord "in his heart"
- "keep forever such purposes and thoughts in the hearts of your people, and direct their hearts toward you" (1Ch 29:18)
- "the Lord searches all hearts and understands every plan and thought" (1Ch 28:9)
- "disclose the purposes of the heart" (1Co 4:5)
- **Steadfast purpose [of heart]:** "remain faithful to the Lord with steadfast purpose" (Act 11:23).
- **Resolved:** "You have tried my heart … I have purposed that my mouth will not transgress" (Psa 17:3); "Daniel resolved [*set on his heart*] that he would not defile himself" (Dan 1:8).
- [Claude reading] **Intention (*yēṣer*) is located in the heart, and God reads it.** The same organ that God tests (Batch B §1.4) is the one that forms intentions.

### 2.3 Choosing — soul and heart
- **Human choosing:**
  - "I would choose strangling and death rather than my bones" (Job 7:15) — the *nephesh* chooses death
  - "These have chosen their own ways, and their soul delights in their abominations" (Isa 66:3)
  - "If I am to live in the flesh … which I shall choose I cannot tell" (Phili 1:22)
- **God choosing with his soul and heart:**
  - "my chosen, in whom my soul delights; I have put my Spirit upon him" (Isa 42:1; Mat 12:18)
  - "I have chosen and consecrated this house … My eyes and my heart will be there for all time" (2Ch 7:16)
  - "God chose you … through sanctification by the Spirit" (2Th 2:13) [D2]
- **Human heart and soul turned toward what God chose:** "repent with all their heart and with all their soul … pray toward … the city that you have chosen" (1Ki 8:48; 2Ch 6:38).
- ◆ "The heart of the wicked is of little worth" against "choice silver" (Pro 10:20).

### 2.4 The mind-set of flesh and Spirit (*phronēma*)
- "to set the mind on the flesh is death, but to set the mind on the Spirit is life and peace" (Rom 8:6) [D3]
- "the mind that is set on the flesh is hostile to God" (Rom 8:7)
- "he who searches hearts knows what is the mind of the Spirit" (Rom 8:27) [D2]
- **Planning according to the flesh = vacillating:** "Do I make my plans according to the flesh, ready to say 'Yes, yes' and 'No, no' at the same time?" (2Co 1:17).
- **The Spirit wills:** "one and the same Spirit, who apportions to each one individually as he wills" (1Co 12:11) [D1].
- [lexical] G5427 *phronēma* is filed under Will & Resolve. It carries "orientation of mind" rather than a single decision.

### 2.5 ◆ Spirit and resolve — fringe
- "an excellent spirit was in him. And the king planned to set him over the whole kingdom" (Dan 6:3) [H2+X] — a quality of spirit prompts another's plan.
- "in whose spirit there is no deceit" beside "the Lord counts no iniquity" (Psa 32:2) [H1].
- "his mind was made like that of a beast … until he knew that the Most High … sets over it whom he will" (Dan 5:21).

---

## 3. Envy, greed and sexual desire (M28)

### 3.1 The whoring heart and the spirit of whoredom
- "their whoring heart that has departed from me and … their eyes that go whoring after their idols" (Eze 6:9)
- "not to follow after your own heart and your own eyes, which you are inclined to whore after" (Num 15:39)
- **Spirit of whoredom [X]:** "a spirit of whoredom has led them astray" (Hos 4:12); "the spirit of whoredom is within them, and they know not the Lord" (Hos 5:4)
- "whoredom, wine, and new wine, which take away the understanding [*heart*]" (Hos 4:11)
- "How sick is your heart … the deeds of a brazen prostitute" (Eze 16:30)
- "dressed as a prostitute, wily of heart" (Pro 7:10)
- "If a person [*nephesh*] turns to mediums … whoring after them" (Lev 20:6)
- [Claude reading] **Idolatry is described with a sexual verb, and the heart, eyes and a "spirit" are its agents.** In Hos 5:4 the "spirit of whoredom" is a disposition within [X] that blocks knowing God.

### 3.2 Greed
- "They have eyes full of adultery … They entice unsteady souls. They have hearts trained in greed" (2Pe 2:14) — **heart trained, souls unsteady**
- "their heart is set on their gain" (Eze 33:31)
- "the one greedy for gain … renounces the Lord" (Psa 10:3)
- "greedy for unjust gain; it takes away the life [*nephesh*] of its possessors" (Pro 1:19) — **greed kills its own soul**
- "destroying lives to get dishonest gain" (Eze 22:27)

### 3.3 ◆ Fleshly vs spiritual (*sarkikos / pneumatikos*)
- "I … could not address you as spiritual people, but as people of the flesh" (1Co 3:1)
- "the law is spiritual, but I am of the flesh, sold under sin" (Rom 7:14)
- "If we have sown spiritual things among you, is it too much if we reap material [*fleshly*] things?" (1Co 9:11); "spiritual blessings … material blessings" (Rom 15:27) — neutral
- "not by earthly [*fleshly*] wisdom but by the grace of God" (2Co 1:12) — with "the testimony of our conscience"
- ◆ **Positive flesh-heart:** "written … with the Spirit of the living God, not on tablets of stone but on tablets of human [*fleshly*] hearts" (2Co 3:3) [D1]. This echoes the "heart of flesh" of Eze 36:26 (§8.3).
- [lexical; Claude reading] This pairs with the *psychikos / pneumatikos* contrast in Batch B §8. "Fleshly" can be moral (1Co 3:1; Rom 7:14), neutral (1Co 9:11; Rom 15:27) or positive (2Co 3:3). **The sense depends on what it is contrasted with.**

### 3.4 Flesh and passion
- "the works of the flesh are evident: sexual immorality, impurity, sensuality" (Gal 5:19)
- "abstain from the passions of the flesh, which wage war against your soul" (1Pe 2:11)
- "indulged in sexual immorality and pursued unnatural desire [*other flesh*]" (Jude 7)
- "do not get drunk with wine, for that is debauchery, but be filled with the Spirit" (Eph 5:18) [D3] — **filled with wine vs filled with the Spirit**
- [lexical] Flesh = genitals in Eze 16:26 ("lustful [*great of flesh*] neighbors") and Eze 23:20.
- ◆ Ezekiel: "defiled her with their whoring lust … she turned from them in disgust [*her nephesh*]" (Eze 23:17–18). The soul turns away in revulsion from what it lusted after.

---

## 4. Zeal, eagerness and diligence (M69, M67)

- **Fervent in spirit [H1]:**
  - "Do not be slothful in zeal, be fervent in spirit, serve the Lord" (Rom 12:11) — both M69 and M67
  - "being fervent in spirit, he spoke and taught accurately" (Act 18:25)
- **Spirit willing, flesh weak [H1]:** "The spirit indeed is willing, but the flesh is weak" (Mat 26:41; Mar 14:38). This is the clearest statement in the batch of the human spirit and the flesh **pulling in different directions within one person**.
- **Heart eagerness:** "in person not in heart, we endeavored the more eagerly" (1Th 2:17).
- **Earnestness given by God:** "God … put into the heart of Titus the same earnest care I have for you" (2Co 8:16).
- **Toward the Spirit:** "eager to maintain the unity of the Spirit" (Eph 4:3) [D2]; "earnestly desire the spiritual gifts" (1Co 14:1).
- [Claude reading] **Zeal is predicated of the spirit ("fervent" = *boiling*), not of the heart.** Laziness is set against it (Rom 12:11).

---

## 5. Wholeness, patience and perseverance (M34)

### 5.1 The whole heart (*lēv shālēm*) — see §0.6
- "a whole heart" (1Ch 29:9, 19; 2Ch 19:9; 2Ki 20:3; Isa 38:3); "with a whole heart to make David king … of a single mind" (1Ch 12:38)
- "Let your heart therefore be wholly true to the Lord" (1Ki 8:61)
- **Measured against David:**
  - "his heart was not wholly true to the Lord his God, as was the heart of David his father" (1Ki 11:4; 15:3)
  - "the heart of Asa was wholly true to the Lord all his days" (1Ki 15:14; 2Ch 15:17)
- **The qualified verdict:** "he did what was right in the eyes of the Lord, yet not with a whole heart" (2Ch 25:2).
- **God's support for it:** "to give strong support to those whose heart is blameless [*whole*] toward him" (2Ch 16:9).
- ◆ **Blameless soul-life:** "I am blameless; I regard not myself; I loathe my life" (Job 9:21) — integrity with self-rejection; "Bloodthirsty men hate one who is blameless and seek the life of the upright" (Pro 29:10).
- [Claude reading] **"Whole" measures the heart by its undividedness toward God**, not by its feeling or its knowledge. The whole heart is the standard for evaluating kings.

### 5.2 Patience and endurance
- "be patient. Establish your hearts" (Jam 5:8)
- "hold it fast in an honest and good heart, and bear fruit with patience" (Luk 8:15)
- "By your endurance you will gain your lives [*souls*]" (Luk 21:19)
- "so that you may not grow weary or fainthearted [*faint in your souls*]" (Heb 12:3)
- "May the Lord direct your hearts to the love of God and to the steadfastness of Christ" (2Th 3:5)
- "firmly established in his heart" (1Co 7:37)
- **Patience given by the Spirit:** "the fruit of the Spirit is … patience" (Gal 5:22) [D3]; "by … patience … the Holy Spirit" (2Co 6:6) [D1]; "praying at all times in the Spirit … with all perseverance" (Eph 6:18) [D3]
- **Patience in spirit:** "the patient in spirit is better than the proud in spirit" (Ecc 7:8) [H1]
- **Conscience and endurance:** "mindful [*conscious*] of God, one endures sorrows" (1Pe 2:19); "I always take pains to have a clear conscience" (Act 24:16)
- **Soul "long" = patient** [lexical]: "what is my end, that I should be patient [*lengthen my soul*]?" (Job 6:11)

### 5.3 Forever — the inner seat and duration
- "May your hearts live forever!" (Psa 22:26)
- "For I will not contend forever … for the spirit would grow faint before me, and the breath of life that I made" (Isa 57:16) [H2] — **God limits his contending for the sake of the human spirit**
- "who inhabits eternity … I dwell … also with him who is of a contrite and lowly spirit, to revive the spirit of the lowly, and to revive the heart of the contrite" (Isa 57:15) [H1]
- "Do not deliver the soul of your dove to the wild beasts" (Psa 74:19)
- **The contrary:** "He says in his heart, 'God has forgotten … he will never see it'" (Psa 10:11)
- "let all flesh bless his holy name forever" (Psa 145:21)

### 5.4 ◆ Fringe
- "I slept, but my heart was awake" (Song 5:2) — the heart keeping watch while the body sleeps
- "if you receive a different spirit … you put up with it readily enough" (2Co 11:4) [U] — **endurance misplaced**
- "Then my God put it into my heart to assemble the nobles" (Neh 7:5); "I took counsel with myself [*my heart*]" (Neh 5:7)

---

## 6. Hope and waiting (M68)

### 6.1 The soul waits and hopes
- "I wait for the Lord, my soul waits, and in his word I hope" (Psa 130:5)
- "Our soul waits for the Lord" (Psa 33:20)
- "For God alone, O my soul, wait in silence, for my hope is from him" (Psa 62:5)
- "My soul longs for your salvation; I hope in your word" (Psa 119:81)
- "we wait for you; your name … the desire of our soul" (Isa 26:8)
- "The Lord is good to those who wait for him, to the soul who seeks him" (Lam 3:25)
- "your hope will not be cut off" — wisdom "to your soul" (Pro 24:14)

### 6.2 The soul addressed, and the soul speaking
- **Addressed:** "Why are you cast down, O my soul … Hope in God" (Psa 42:5, 11; 43:5).
- **Speaking:** "'The Lord is my portion,' says my soul, 'therefore I will hope in him'" (Lam 3:24).
- **Recalling:** "But this I call to mind [*heart*], and therefore I have hope" (Lam 3:21).
- [Claude reading] Hope is produced by an **inner dialogue**. The self speaks to its soul (Psa 42), the soul speaks back (Lam 3:24), and the heart recalls (Lam 3:21). This matches the "said in heart" material due in Batch E.

### 6.3 The heart waits and takes courage
- "Wait for the Lord; be strong, and let your heart take courage" (Psa 27:14)
- "let your heart take courage, all you who wait for the Lord!" (Psa 31:24)
- "Hope deferred makes the heart sick" (Pro 13:12)
- "Reproaches have broken my heart … I looked for pity, but there was none" (Psa 69:20)
- "do not set your heart [*nephesh*] on putting him to death … there is hope" (Pro 19:18)

### 6.4 Hope and the NT inner seat
- "my heart was glad … my flesh also will dwell in hope" (Act 2:26) — **flesh in hope**
- "hope does not put us to shame, because God's love has been poured into our hearts through the Holy Spirit" (Rom 5:5) [D1]
- "by the power of the Holy Spirit you may abound in hope" (Rom 15:13) [D1]
- "through the Spirit, by faith, we ourselves eagerly wait for the hope of righteousness" (Gal 5:5) [D3]
- "one body and one Spirit … one hope" (Eph 4:4) [D1]
- "the eyes of your hearts enlightened, that you may know what is the hope" (Eph 1:18)
- "in your hearts honor Christ … a reason for the hope that is in you" (1Pe 3:15)
- "waiting for the consolation of Israel, and the Holy Spirit was upon him" (Luk 2:25) [D1]
- **Expectation in the heart:** "As the people were in expectation, and all were questioning in their hearts" (Luk 3:15).
- **Hope and conscience:** "I hope it is known also to your conscience" (2Co 5:11).

### 6.5 Hope's end
- "their hope is to breathe their last [*breathing out of soul*]" (Job 11:20)
- "what is the hope of the godless when God … takes away his life?" (Job 27:8)
- "They … lurk … as they have waited for my life" (Psa 56:6) — hostile waiting, cf. §7.5
- ◆ "while Paul was waiting … his spirit was provoked within him" (Act 17:16) [H1] — waiting and inner provocation together.

---

## 7. Seeking and inquiring (M83)

### 7.1 Seeking the Lord with heart and soul
- "you will find him, if you search after him with all your heart and with all your soul" (Deu 4:29)
- "a covenant to seek the Lord … with all their heart and with all their soul" (2Ch 15:12); "sworn with all their heart … sought him with their whole desire" (2Ch 15:15)
- "You will seek me and find me, when you seek me with all your heart" (Jer 29:13)
- "With my whole heart I seek you" (Psa 119:10); "who seek him with their whole heart" (Psa 119:2)
- "he sought the Lord with all his heart" (2Ch 22:9); "seeking his God, he did with all his heart" (2Ch 31:21)
- **Setting the heart to seek** (cf. Batch B §0.1):
  - "set your mind and heart [*heart and soul*] to seek the Lord" (1Ch 22:19)
  - "those who had set their hearts to seek the Lord" (2Ch 11:16)
  - "you … have set your heart to seek God" (2Ch 19:3); "who sets his heart to seek God … even though not according to the sanctuary's rules" (2Ch 30:19)
  - "Ezra had set his heart to study [*seek*] the Law" (Ezr 7:10)
  - **Failure:** "he did evil, for he did not set his heart to seek the Lord" (2Ch 12:14)
- **Heart answering God's invitation:** "You have said, 'Seek my face.' My heart says to you, 'Your face, Lord, do I seek'" (Psa 27:8).
- **Seeking hearts rejoice / revive:** "let the hearts of those who seek the Lord rejoice" (1Ch 16:10; Psa 105:3); "you who seek God, let your hearts revive" (Psa 69:32); "May your hearts live forever" (Psa 22:26).
- [Claude reading] **Seeking God is the orientation of heart and soul together.** 2Ch 30:19 makes the heart's setting outweigh ritual cleanness.

### 7.2 The soul that seeks — longing in motion
- "earnestly I seek you; my soul thirsts for you; my flesh faints for you" (Psa 63:1)
- "My soul yearns for you in the night; my spirit within me earnestly seeks you" (Isa 26:9) [H1]
- "I sought him whom my soul loves; I sought him, but found him not" (Song 3:1–2)
- "My soul failed me when he spoke. I sought him, but found him not" (Song 5:6)
- "which my soul has sought repeatedly, but I have not found" (Ecc 7:28)
- "In the day of my trouble I seek the Lord … my soul refuses to be comforted" (Psa 77:2)

### 7.3 The heart seeks knowledge
- "The heart of him who has understanding seeks knowledge" (Pro 15:14)
- "An intelligent heart acquires knowledge" (Pro 18:15)
- "I applied my heart to seek and to search out by wisdom" (Ecc 1:13)
- "I turned my heart to know and to search out and to seek wisdom" (Ecc 7:25)

### 7.4 God seeks
- **A heart:** "The Lord has sought out a man after his own heart" (1Sa 13:14).
- **Worshippers in spirit:** "the true worshipers will worship the Father in spirit and truth, for the Father is seeking such people" (Joh 4:23) [D1+H2].
- **Offspring:** "a portion of the Spirit in their union … what was the one God seeking? Godly offspring. So guard yourselves in your spirit" (Mal 2:15) [U+H1].
- **God requires the soul-life:**
  - "for your lifeblood I will require a reckoning … for the life of man" (Gen 9:5)
  - "his blood I will require at the watchman's hand" (Eze 33:6)
- **God tests the heart:** "God left him to himself, in order to test him and to know all that was in his heart" (2Ch 32:31).

### 7.5 "Seek my life" — the soul-life hunted (§0.2)
- **David:** 1Sa 20:1; 22:23; 23:15; 25:29; 2Sa 4:8; 16:11 ("my own son seeks my life").
- **Elijah:** 1Ki 19:10, 14 (Rom 11:3).
- **Jeremiah and the nations:** Jer 4:30; 11:21; 19:7, 9; 21:7; 22:25; 34:20–21; 38:16; 44:30; 46:26; 49:37.
- **Psalms:** Psa 35:4; 38:12; 40:14; 54:3; 63:9; 70:2; 86:14.
- **NT:** "those who sought the child's life are dead" (Mat 2:20) — echoing "all the men who were seeking your life are dead" (Exo 4:19).
- **Care for the soul, by contrast:** "no one cares for [*seeks*] my soul" (Psa 142:4).
- **Hostile psalms place the same *nephesh* in both roles:** "those who seek my life … shall go down into the depths" (Psa 63:9), eight verses after "my soul thirsts for you" (Psa 63:1).
- [Claude reading] One word is both the seeker of God (§7.2) and the object hunted by enemies. **The *nephesh* is the person's life, which can long and can be taken.**
- ◆ "Whoever seeks to preserve his life will lose it" (Luk 17:33).
- ◆ "Seek them not … I am bringing disaster upon all flesh … But I will give you your life as a prize of war" (Jer 45:5).
- ◆ "Haman stayed to beg [*seek*] for his life" (Est 7:7).

### 7.6 Illegitimate and restless seeking
- **Idols in the heart, consulting God:** "these men have taken their idols into their hearts … Should I indeed let myself be consulted by them?" (Eze 14:3, 7).
- **Emptied spirit → occult inquiry:** "the spirit of the Egyptians within them will be emptied out … and they will inquire of the idols and the sorcerers" (Isa 19:3) [H1].
- **Sign-seeking grieves the spirit:** "he sighed deeply in his spirit and said, 'Why does this generation seek a sign?'" (Mar 8:12) [H1].
- ◆ **The spirit that seeks rest:** "When the unclean spirit has gone out of a person, it passes through waterless places seeking rest, and finding none it says, 'I will return to my house'" (Mat 12:43; Luk 11:24) [O]. **An other-spirit is depicted as seeking a person as its dwelling.**
- ◆ "the Spirit said to him, 'Behold, three men are looking for you'" (Act 10:19) [D2]; "It may be that the Spirit of the Lord has caught him up" (2Ki 2:16) [D1]; "his Spirit has gathered them. Seek and read" (Isa 34:16) [D1].

---

## 8. Turning and repentance (M11)

### 8.1 Returning with heart and soul
- "if they turn their heart [*bring back to heart*] … and repent" (1Ki 8:47; 2Ch 6:37); "if they repent with all their heart and with all their soul" (1Ki 8:48; 2Ch 6:38)
- "If you are returning to the Lord with all your heart, then put away the foreign gods … and direct your heart to the Lord" (1Sa 7:3); "put away the foreign gods … and incline your heart to the Lord" (Jos 24:23)
- "rend your hearts and not your garments. Return to the Lord your God" (Joe 2:13)
- "lest they … understand with their hearts, and turn and be healed" (Isa 6:10; Joh 12:40)
- "the intent of your heart may be forgiven you" (Act 8:22)
- **Repentance and the Spirit:** "Repent … and you will receive the gift of the Holy Spirit" (Act 2:38) [D1]; "for repentance … he will baptize you with the Holy Spirit" (Mat 3:11) [D1].
- ◆ **Turning brings the outpoured spirit:** "If you turn at my reproof, behold, I will pour out my spirit to you" (Pro 1:23) [X] — Wisdom's spirit.
- [Claude reading] **Repentance is the heart turning back, and putting away idols is its outward correlate.** "Put away … direct your heart" is one movement (1Sa 7:3).

### 8.2 The heart turning away
- "lest his heart turn away" (Deu 17:17); "that his heart may not be lifted up … that he may not turn aside" (Deu 17:20)
- "Take care lest your heart be deceived, and you turn aside" (Deu 11:16)
- "Cursed is the man who … makes flesh his strength, whose heart turns away from the Lord" (Jer 17:5) — **heart turning and trusting flesh are the same act**
- "this people has a stubborn and rebellious heart; they have turned aside" (Jer 5:23)
- "Let not your heart turn aside to her ways" (Pro 7:25)
- "his wives turned away his heart after other gods" (1Ki 11:4)
- "their whoring heart that has departed from me" (Eze 6:9)
- "I will put the fear of me in their hearts, that they may not turn from me" (Jer 32:40) — **God guards the heart against turning**
- "keep your soul diligently … lest they depart from your heart" (Deu 4:9)
- ◆ "They do not cry to me from the heart, but they wail upon their beds … they rebel against me" (Hos 7:14).

### 8.3 God removes and replaces — heart, spirit and flesh in one act
- "I will give them one heart, and a new spirit I will put within them. I will remove the heart of stone from their flesh and give them a heart of flesh" (Eze 11:19; 36:26) [H1]
- "remove the foreskin of your hearts" (Jer 4:4)
- **Heart and body:** "Remove vexation from your heart, and put away pain from your body" (Ecc 11:10).
- **God takes away understanding:** "He takes away understanding [*heart*] from the chiefs" (Job 12:24).
- [Claude reading] In Eze 11:19 / 36:26, heart, spirit and flesh are all tagged "remove" within four positions. **Flesh is the good material here (a "heart of flesh") and stone is the bad**, the reverse of NT flesh-desire (§1.11). Compare 2Co 3:3 (§3.3).

### 8.4 The contrite spirit and heart (§0.7)
- "The Lord is near to the brokenhearted and saves the crushed in spirit" (Psa 34:18) [H1]
- "The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise" (Psa 51:17) [H1] (M30 tag)
- "to revive the spirit of the lowly, and to revive the heart of the contrite" (Isa 57:15) [H1]
- [Claude reading] **In each verse the spirit and the heart are paired as the crushed, and God is the one who draws near, accepts or revives.**

### 8.5 God's regret and relenting
- "the Lord regretted that he had made man … and it grieved him to his heart" (Gen 6:6)
- "rend your hearts … he relents over disaster" (Joe 2:13)
- "did not the Lord relent … But we are about to bring great disaster upon ourselves [*our souls*]" (Jer 26:19)

### 8.6 The watchman's soul
- "if you warn the wicked, and he does not turn … you will have delivered your soul" (Eze 3:19; 33:9)
- "when a wicked person turns away from the wickedness … he shall save his life" (Eze 18:27)
- "you have disheartened the righteous falsely … encouraged the wicked, that he should not turn" (Eze 13:22)
- "whoever guards his way preserves his life" (Pro 16:17)
- **To turn from evil is abhorrent to fools:** "A desire fulfilled is sweet to the soul, but to turn away from evil is an abomination to fools" (Pro 13:19).

### 8.7 ◆ Spirits departing and returning
- "the Spirit of the Lord departed from Saul, and a harmful spirit from the Lord tormented him" (1Sa 16:14) [D1+O]
- "Saul was refreshed … and the harmful spirit departed from him" (1Sa 16:23) [O]
- "I will return to my house from which I came" (Luk 11:24) [O]
- "Jesus, full of the Holy Spirit, returned from the Jordan and was led by the Spirit" (Luk 4:1) [D1] — travel, noted for the Spirit only
- "by the breath of his mouth he will depart" (Job 15:30)
- ◆ "my beloved had turned and gone. My soul failed me" (Song 5:6)

---

## 9. Rebellion, stubbornness, refusal and hardening (M30, M75)

### 9.1 The stubbornness of the heart (*šerîrût lēv*)
- "I shall be safe, though I walk in the stubbornness of my heart" (Deu 29:19) — **the heart blessing itself**
- "So I gave them over to their stubborn hearts, to follow their own counsels" (Psa 81:12)
- "everyone walked in the stubbornness of his evil heart" (Jer 11:8); "walked in their own counsels and the stubbornness of their evil hearts, and went backward and not forward" (Jer 7:24)
- "who … stubbornly follow their own heart and have gone after other gods" (Jer 13:10; 9:14)
- "every one of you follows his stubborn, evil will [*heart*], refusing to listen to me" (Jer 16:12)
- "We will follow our own plans, and will every one act according to the stubbornness of his evil heart" (Jer 18:12)
- "to everyone who stubbornly follows his own heart, they say, 'No disaster shall come upon you'" (Jer 23:17)
- **Promised end:** "they shall no more stubbornly follow their own evil heart" (Jer 3:17)
- [Claude reading] **Stubbornness is the heart used as a guide in place of God.** "Follow your own heart" is the charge, not the advice. This links to "Whoever trusts in his own mind [heart] is a fool" (Pro 28:26; Batch B §2.2).

### 9.2 Rebellious heart and unfaithful spirit
- "a stubborn and rebellious heart; they have turned aside" (Jer 5:23)
- "a stubborn and rebellious generation, a generation whose heart was not steadfast, whose spirit was not faithful to God" (Psa 78:8) [H1] — **heart and spirit in parallel**
- **Rebelling against God's Spirit [D1]:**
  - "they rebelled and grieved his Holy Spirit" (Isa 63:10)
  - "stubborn children … who make an alliance, but not of my Spirit" (Isa 30:1)
  - "whoever disregards this, disregards … God, who gives his Holy Spirit to you" (1Th 4:8)
  - "the Spirit of God clothed Zechariah … 'Because you have forsaken the Lord, he has forsaken you'" (2Ch 24:20)
- **Self-rebuke:** "my heart is wrung within me, because I have been very rebellious" (Lam 1:20).

### 9.3 Hardening
- **God hardens:**
  - "the Lord hardened Pharaoh's heart, and he would not let them go" (Exo 10:27); "Pharaoh's heart is hardened; he refuses" (Exo 7:14)
  - "the Lord your God hardened his spirit and made his heart obstinate" (Deu 2:30) [H1] — **spirit and heart hardened together**
  - "why do you … harden our heart, so that we fear you not?" (Isa 63:17)
  - "He has blinded their eyes and hardened their heart" (Joh 12:40)
- **People harden:** "He … stiffened his neck and hardened his heart against turning to the Lord" (2Ch 36:13); "do not harden your hearts as in the rebellion" (Heb 3:8, 15; 4:7).
- **Hardness and failure to understand** (cf. Batch B §1.3):
  - "their hearts were hardened" (Mar 6:52); "Do you not yet perceive or understand? Are your hearts hardened?" (Mar 8:17)
  - "darkened in their understanding … due to their hardness of heart" (Eph 4:18)
- **Consequences:** "grieved at their hardness of heart" (Mar 3:5); "because of your hard and impenitent heart you are storing up wrath" (Rom 2:5).
- **Unfeeling heart:** "their heart is unfeeling like fat" (Psa 119:70).
- **Unwillingness to listen:** "they are not willing to listen to me: because all the house of Israel have a hard forehead and a stubborn heart" (Eze 3:7).

### 9.4 Despising and rejecting — heart and soul as agents
- "she despised him in her heart" (2Sa 6:16; 1Ch 15:29) — Michal
- "How I hated discipline, and my heart despised reproof!" (Pro 5:12)
- "Whoever ignores instruction despises himself [*his nephesh*]" (Pro 15:32)
- "if your soul abhors my rules" (Lev 26:15); "their soul abhorred my statutes" (Lev 26:43)
- "the wicked … renounces God and says in his heart, 'You will not call to account'" (Psa 10:13; 10:3)
- "their heart went after their idols" (Eze 20:16)
- **Conscience rejected:** "holding faith and a good conscience. By rejecting this, some have made shipwreck of their faith" (1Ti 1:19).
- **Refusal as the soul's own act:** "my soul refuses to be comforted" (Psa 77:2); "My appetite refuses to touch them" (Job 6:7).
- **Flesh rejecting authority:** "defile the flesh, reject authority" (Jude 8); "the lust of defiling passion … despise authority" (2Pe 2:10).

### 9.5 God's rejection and non-rejection of the inner seat
- **Not despised:** "a broken and contrite heart, O God, you will not despise" (Psa 51:17); "God is mighty, and does not despise any" (Job 36:5).
- **Cast off:** "O Lord, why do you cast my soul away?" (Psa 88:14); "Have you utterly rejected Judah? Does your soul loathe Zion?" (Jer 14:19) — God's *nephesh*.
- **Deserted:** "like a wife deserted and grieved in spirit … cast off" (Isa 54:6) [H1].
- **Not abandoned:** "you will not abandon my soul to Sheol" (Psa 16:10).
- **God's heart vs man's eyes:** "I have rejected him … the Lord looks on the heart" (1Sa 16:7).
- "if you forsake him, he will cast you off forever" (1Ch 28:9).
- **Beloved of the soul given up:** "I have given the beloved of my soul into the hands of her enemies" (Jer 12:7).

### 9.6 ◆ The heart that forsakes its owner
- "my iniquities have overtaken me, and I cannot see; they are more than the hairs of my head; my heart fails [*forsakes*] me" (Psa 40:12)
- "My heart throbs; my strength fails me" (Psa 38:10)
- [lexical; Claude reading] The verb is *ʿāzav* "forsake", the same verb used of Israel forsaking God. The heart is pictured as able to **abandon the person**.

### 9.7 ◆ Spirit and soul made bitter, sullen or unrestrainable
- "Why is your spirit so vexed [*sullen*] that you eat no food?" (1Ki 21:5) [H1] — spirit state stops appetite
- "they made his spirit bitter, and he spoke rashly with his lips" (Psa 106:33) [H1] — whose spirit is open. **→ Ruling R4.**
- "all the people were bitter in soul" (1Sa 30:6) — the H4784 "rebel" tag may be a *mārâ / mārar* lemma confusion. **→ Ruling R5.**
- "No man has power to retain the spirit, or power over the day of death" (Ecc 8:8) [U] — the spirit cannot be held back
- "there is in my heart as it were a burning fire shut up in my bones, and I am weary with holding it in" (Jer 20:9) — restraint fails
- "he was tormenting his righteous soul over their lawless deeds" (2Pe 2:8)
- **Minds poisoned:** "the unbelieving Jews … poisoned their minds [*souls*] against the brothers" (Act 14:2).

### 9.8 Disobedience and the spirit at work
- "the spirit that is now at work in the sons of disobedience" (Eph 2:2) [O]
- "in the spirit and power of Elijah, to turn the hearts of the fathers to the children, and the disobedient to the wisdom of the just" (Luk 1:17) [H2]
- "the lawless one … whom the Lord Jesus will kill with the breath of his mouth" (2Th 2:8) [W]
- "present your members as slaves to … lawlessness" — "because of your natural [*fleshly*] limitations" (Rom 6:19)

---

## 10. Madness (M66)

- "the hearts of the children of man are full of evil, and madness is in their hearts while they live" (Ecc 9:3)
- "The Lord will strike you with madness and blindness and confusion of mind [*heart*]" (Deu 28:28)
- "I applied my heart to know wisdom and to know madness and folly … a striving after wind" (Ecc 1:17); "I turned my heart to know … the foolishness that is madness" (Ecc 7:25)
- "The prophet is a fool; the man of the spirit is mad" (Hos 9:7) [U]
- [Claude reading] **Madness is located in the heart** (Ecc 9:3; Deu 28:28). The heart can also **investigate** madness (Ecc 1:17; 7:25). Hos 9:7 is the only verse linking madness to "spirit", and its spirit is not determinable.

---

## 11. Cross-cutting observations for Batch C [Claude reading]

1. **The soul is the desiring self.** In the OT, *nephesh* is the ordinary subject of "want / crave / long / thirst", from appetite for meat (Deu 12:20) to thirst for God (Psa 42:1–2). The same *nephesh* is the **life that enemies seek** (§7.5) and the **life that is precious** (§1.7). **Desire and vitality are one word.**
2. **The heart is where orientation is set, held, divided or hardened.** It plans, forms intentions, resolves, seeks, turns, is whole or not whole, and is stubborn or hardened. Many of these are expressed as **setting / directing / inclining the heart** (1Sa 7:3; Jos 24:23; 2Ch 19:3; 30:19). This extends Batch B's "attention = setting the heart" into will.
3. **The human spirit carries energy and disposition, more than choice.** It is "moved" to give (Exo 35:21), "fervent" (Rom 12:11), "willing" against weak flesh (Mat 26:41), patient or proud (Ecc 7:8), ruled (Pro 16:32), hardened with the heart (Deu 2:30), not faithful (Psa 78:8), and crushed or contrite (Psa 34:18; 51:17). **Planning and choosing are rarely predicated of the human spirit** [observation, not a count].
4. **Heart and spirit are paired in the orientation verses** (Exo 35:21; Deu 2:30; Psa 51:17; 78:8; Isa 57:15; Eze 11:19; 36:26). **Heart and soul are paired in the "all your heart and all your soul" formula** for seeking and returning (Deu 4:29; 1Ki 8:48; 2Ch 15:12).
5. **Flesh changes role across the corpus.**
   - OT: flesh longs and faints for God with the soul (Psa 63:1; 84:2). The "heart of flesh" is God's gift (Eze 36:26).
   - NT: flesh is the main subject of wrong desire (Gal 5:16–17; 1Jo 2:16), set against the Spirit and the soul (1Pe 2:11) and weak beside a willing spirit (Mat 26:41).
   - 2Co 3:3 ("tablets of fleshly hearts") keeps the OT positive use inside the NT.
6. **God's Spirit relates to orientation as giver and as the one resisted.**
   - Giver: good Spirit leading (Psa 143:10), patience (Gal 5:22), hope (Rom 5:5; 15:13), received on repentance (Act 2:38).
   - Resisted: rebelled against and grieved (Isa 63:10), disregarded (1Th 4:8), bypassed in plans (Isa 30:1).
   - The Spirit also **desires against the flesh** (Gal 5:17) and **wills** (1Co 12:11).
7. **God is shown with his own soul and heart of desire and choice**: his soul delights in the chosen servant (Isa 42:1), his heart is set on the chosen house (2Ch 7:16), he seeks a man after his heart (1Sa 13:14), his heart is grieved (Gen 6:6).
8. **Other spirits in this batch act on orientation from outside:** spirit of jealousy (Num 5), spirit of whoredom (Hos 4:12; 5:4) [X]; harmful spirit from God (1Sa 16) and the spirit at work in the disobedient (Eph 2:2) [O]; the unclean spirit seeking a dwelling (Mat 12:43) [O].
9. ◆ **Fringe worth keeping:**
   - desire as breath-hunger — "striving after wind" (§1.9)
   - the wine-merry heart as the point of exposure (§1.6)
   - the heart that forsakes its owner (§9.6)
   - the spirit that cannot be retained (Ecc 8:8)
   - fleshly vs spiritual, with its moral / neutral / positive senses (§3.3)
   - the heart awake while the body sleeps (Song 5:2)

---

## 12. Next

- **Batch D** (moral condition): M12, M58, M56, M14, M57, M62, M61 (report "Holy Spirit" pre-filter), M10c, M08, M09.
- Researcher rulings R1–R5 are set out in **§R**, with a blank "Ruling" row each. Once they are ruled, the cluster-membership changes (R1–R3) and the tagging decision (R5) go to the relevant clusters' analysis. R4 goes to the spirit-classification CSV.
