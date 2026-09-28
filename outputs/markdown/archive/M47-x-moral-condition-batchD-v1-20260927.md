# M47 × Moral Condition — Batch D (v1)

**Date:** 2026-09-27
**Use:** this file is meant to accompany the analysis of each cluster listed below. Start at §X to find the sections and flagged Strong's for your cluster.
**Format:** as Batch C v2 — §R (items for researcher ruling) and §X (cluster cross-reference) come first, then §0 data notes and the analysis.
**Data:** `cluster-M47-other-m-code-pairs-with-distance-20260927.csv` — pairs where the other word is in:
- M12 Righteousness & Integrity
- M58 Wickedness
- M56 Sin & Guilt
- M14 Deceit & Falsehood
- M57 Corruption & Perversion
- M62 Truth & Sincerity
- M61 Purity & Holiness
- M10c Defilement
- M08 Pride & Arrogance
- M09 Humility & Lowliness

**1,423 pairs in 835 distinct verses (1,033 verse-cluster rows); all read.** The "Holy" + "Spirit" pairs are counted and reported in §7.1. They are not dropped (§0.1).

**Spirit classes** (`M47-spirit-distinction-v1-20260927.md`, joined per verse from `M47-spirit-classification-v1-20260927.csv`):
- **[D1/D2]** divine
- **[D3]** divine per ESV only
- **[D-attr]** divine as the speaker attributes it ("spirit of the holy gods")
- **[H1/H2]** human
- **[O]** other being
- **[X]** disposition
- **[W]** wind / breath
- **[T]** / **[T-D]** *rûaḥ* as temper (human / divine)
- **[U]** not determinable
- Combined classes (e.g. [D1+O], [U+H1]) are carried as the CSV gives them.
- Wind-sense *rûaḥ* (H7307H) is not in the classification CSV; it is marked *wind* in the text.

Tags: **[Claude reading]**, **[lexical]**, **[verify]**, ◆ fringe. Not statistical.

**Component profile (verses per cluster, a verse counted once per component)** — orientation only, not a finding:

| Cluster | pairs | verses | heart | soul | spirit / wind | flesh | conscience | *pneumatikos* | other M47 |
|---|---|---|---|---|---|---|---|---|---|
| M12 Righteousness | 245 | 173 | 86 | 48 | 25 | 22 | 6 | 1 | 0 |
| M58 Wickedness | 225 | 176 | 86 | 48 | 29 | 13 | 2 | 1 | 2 (bosom) |
| M56 Sin & Guilt | 208 | 136 | 39 | 58 | 19 | 23 | 2 | 2 | 1 (G2293 "take heart") |
| M14 Deceit | 161 | 126 | 42 | 29 | 41 | 10 | 6 | 4 | 1 (G1573) |
| M57 Corruption | 25 | 17 | 12 | 5 | 1 | 2 | 0 | 0 | 0 |
| M62 Truth | 8 | 8 | 4 | 0 | 3 | 0 | 1 | 0 | 0 |
| M61 Purity & Holiness | 235 | 182 | 31 | 21 | 117 | 24 | 3 | 2 | 0 |
| M10c Defilement | 124 | 73 | 3 | 26 | 26 | 24 | 1 | 0 | 0 |
| M08 Pride | 138 | 101 | 51 | 28 | 17 | 10 | 1 | 0 | 1 (bosom) |
| M09 Humility | 54 | 41 | 22 | 9 | 10 | 2 | 0 | 0 | 1 (bosom) |

**Spirit classes in the batch** (verse × Strong's rows):
- D1 105, of which 94 are in M61, almost all "Holy Spirit"
- O 42: M10c 23, M58 15, M14 6
- H1 23 · U 12 · H2 9 · D2 8 · D-attr 4 · X 4 · D3 4
- Combined or temper classes 7: D1+O, D2+O, U+H1, O+X, T, T-D

**Assignment source.** Cluster membership is from `iba/app/db/iba.db` → `cluster_strong` (active rows, read-only query, 2026-09-27). "Source" is the assignment route recorded there:
- `old-system-migration` (**old**) — carried over from the old system; no confidence recorded
- `heuristic-family-grouping-v1-20260905` (**heur**) — family heuristic
- `llm-allocation-v1_3-20260811` (**LLM**) — LLM allocation, with a confidence value
- `auto-precedent`
- `claude-scan-20260908`

---

## R. Items for researcher ruling

Ten decisions are needed. For each one: the cluster(s) it affects, the Strong's number, what the DB currently records, the evidence, the options, and my recommendation.
- **R1–R10 are all cluster-membership questions** for `cluster_strong`.
- **No spirit-classification item is raised.** I found no verse in this batch where the CSV class looked wrong. Heb 9:14 "the eternal Spirit" is [U], and that is defensible: it could be Christ's own spirit or the Holy Spirit.
- Nothing has been changed in the DB or the CSV.
- The process question (whether to record misfiles beyond the write-ups) is **Batch A R7** and applies here too.

### R1 — H6965B "arise / rise" in M08 Pride & Arrogance
| | |
|---|---|
| **Cluster(s)** | M08 (current); M47 (partner); T3 Operations (candidate) |
| **Strong's** | H6965B *qûm* "to arise, rise, stand up" |
| **DB now** | M08 · LLM · confidence **medium** · rationale "no precedent; profile suggestion M08:5.9 \| accepted" |
| **Evidence** | 37 pairs in 30 verses. **None is about pride.** Some examples: "he arose and ran for his life" (1Ki 19:3); "Arise and eat bread and let your heart be cheerful" (1Ki 21:7); "Arise, cry out in the night … Pour out your heart" (Lam 2:19); "Then I arose in the night" (Neh 2:12); "the Spirit of the Lord rushed upon David … And Samuel rose up" (1Sa 16:13); "everyone whose spirit God had stirred … rose up" (Ezr 1:5); "though war arise against me" (Psa 27:3); "sit up and eat … that your soul may bless me" (Gen 27:19). |
| **Issue** | It is an ordinary movement verb. The allocation probably followed "rise → exalt oneself". It inflates the M08 profile (30 of 101 verses). |
| **Options** | (a) keep in M08; (b) move to T3 Operations (a function / movement verb); (c) move to another cluster you name; (d) keep in M08 with an alternative-cluster note. |
| **Recommendation** | **(b) T3** [Claude reading]. |
| **Ruling** | ______ |

### R2 — G0080 "brother" in M14 Deceit & Falsehood
| | |
|---|---|
| **Cluster(s)** | M14 (current); T8 Party-Human (already has a row) |
| **Strong's** | G0080 *adelphos* "brother" |
| **DB now** | **Two active rows:** M14 · LLM · **medium** · "no precedent; profile suggestion M14:5.9 \| accepted"; **and** T8 · heur · "no inner-being significance — … generic human-relational term" |
| **Evidence** | 35 pairs in 32 verses. All are the address "brothers" or a kinship term: 1Co 12:1; 15:50; Gal 6:18; Rom 8:12; 9:3; 10:1; Act 2:37; 7:23; Mat 18:35; 1Jo 3:16; etc. None involves deceit. |
| **Issue** | This is a clear misallocation. The T8 row is correct, so the M14 row duplicates it with the wrong sense. |
| **Options** | (a) keep both rows; (b) retire the M14 row and keep T8; (c) something else. |
| **Recommendation** | **(b)**. |
| **Ruling** | ______ |

### R3 — The clean / unclean family is split across four clusters
| | |
|---|---|
| **Cluster(s)** | M12 Righteousness; M61 Purity & Holiness; M10c Defilement; M56 Sin & Guilt |
| **Strong's** | **In M12:** H2889 *ṭāhôr* "pure / clean", H2891 *ṭāhēr* "be clean", H2135 *zākâ* "be clean", H1249 *bar* "pure", H2134 *zak* "pure", G2513 *katharos* "clean", G2511 *katharizō* "cleanse", G2514 "cleanness". **In M56:** H2932 *ṭumʾâ* "uncleanness". **Siblings already in M61:** G0048 "purify", G0054 "purity", H2893 "purifying". **Siblings already in M10c:** H2931 *ṭāmēʾ* "unclean", H2930A "defile". |
| **DB now** | H2889, H2891, H2135, H1249, G2511, G2513 → M12 · **old**. H2134 → M12 · LLM · high. G2514 → M12 · auto-precedent. H2932 → M56 · **heur** ("family=sin-guilt-iniquity"). |
| **Evidence** | **M12 "clean" verses:**<br>• Ritual body cleanness: Lev 13:13, 39; 14:9; 15:13; Num 8:7; 2Ki 5:10, 14 (Naaman); Lev 7:19; Num 19:18<br>• Moral heart cleanness: Psa 24:4; 51:10; 73:1, 13; Pro 20:9; 22:11; Mat 5:8; Jam 4:8; Act 15:9; 1Ti 1:5; Heb 10:22<br>**M56 H2932 verses:** all ritual uncleanness — Lev 7:20–21; 15:3; 22:3; Num 19:13; Zec 13:2 "spirit of uncleanness". |
| **Issue** | Clean, purify and unclean are one semantic family: purity and its opposite. Filing "clean" under Righteousness while "purify / purity" sit in M61 and "unclean" in M10c splits it. Filing "uncleanness" under Sin & Guilt splits it again. |
| **Options** | (a) keep as is; (b) move the M12 clean / pure words to M61, and H2932 to M10c; (c) move only H2932 to M10c; (d) keep, with alternative-cluster notes. |
| **Recommendation** | **(b)** [Claude reading]. Righteousness keeps upright, integrity, just and innocent. |
| **Ruling** | ______ |

### R4 — H5081G "willing / generous" in M09 Humility & Lowliness
| | |
|---|---|
| **Cluster(s)** | M09 (current); M64 Will & Resolve / M18 Desire & Longing (candidates) |
| **Strong's** | H5081G *nādîv* "willing, noble, generous" |
| **DB now** | M09 · **old** · no confidence |
| **Evidence** | 4 pairs at d1:<br>• "whoever is of a generous heart" (Exo 35:5)<br>• "all who were of a willing heart" (Exo 35:22; 2Ch 29:31)<br>• "uphold me with a willing spirit" (Psa 51:12) [H1]<br>This is the freewill family of Batch C §1.4 (*nādav*, Exo 35:21, 29). |
| **Issue** | The sense is readiness to give, not lowliness. The same root's verb (*nādav*) is reported with M18 / M64 in Batch C. |
| **Options** | (a) keep in M09; (b) move to M64 Will & Resolve; (c) move to M18 Desire & Longing; (d) keep with an alternative-cluster note. |
| **Recommendation** | **(b) M64** [Claude reading]. |
| **Ruling** | ______ |

### R5 — Function-word verbs and adverbs in M09, M08 and M62
| | |
|---|---|
| **Cluster(s)** | M09, M08, M62 (current); T3 Operations / T6 Connective (candidates) |
| **Strong's** | H4102 *māhah* "delay" · G5549 *chronizō* "delay" · G1299 *diatassō* "direct, order" (all M09); G0757 *archomai* "begin" (M08); G2117 *euthys* "straight / immediately" (M62) |
| **DB now** | H4102 → M09 · LLM · **high** · "single-cluster precedent". G5549 → M09 · auto-precedent. G1299 → M09 · old. G0757 → M08 · old. G2117 → M62 · heur ("family=truth-sincerity-certainty"). |
| **Evidence** | • "Strengthen your heart and wait [*delay*]" (Judg 19:8)<br>• "says to himself, 'My master is delayed'" (Mat 24:48; Luk 12:45)<br>• "her spirit returned … he directed that something should be given her" (Luk 8:55)<br>• "began to speak" (Act 2:4; 11:15); "began to send them out" (Mar 6:7); "begins to beat" (Luk 12:45)<br>• *euthys*: "immediately" at Mar 1:12; 7:25; Mat 3:16. Only Act 8:21 "your heart is not right [*straight*] before God" carries the M62 sense. |
| **Issue** | None of these words carries the cluster's sense in these verses. G2117 is mixed: adverb "immediately" versus adjective "straight / right". |
| **Options** | (a) keep all; (b) move H4102, G5549, G1299 and G0757 to T3; keep G2117 in M62 with a note that the adverb use is T6; (c) move all five to T-buckets; (d) decide word by word. |
| **Recommendation** | **(b)** [Claude reading]. |
| **Ruling** | ______ |

### R6 — Poverty words in M09 Humility & Lowliness
| | |
|---|---|
| **Cluster(s)** | M09 (current); M46 Wealth & Riches (candidate) |
| **Strong's** | H0034 *ʾevyôn* "needy" · H1800 *dal* "poor, weak" · H7326 *rûš* "be poor" · H6035 *ʿānî / ʿānāw* "poor, afflicted, humble" · G4434 *ptōchos* "poor" |
| **DB now** | All five → M09 · **heur** · "family=humility-lowliness-contrition" |
| **Evidence** | **Economic or social need** (H0034, H1800, H7326):<br>• "saves the lives of the needy" (Psa 72:13)<br>• "you shall not harden your heart … against your poor brother" (Deu 15:7, 9)<br>• "the rich shall not give more, and the poor shall not give less … atonement for your lives" (Exo 30:15)<br>• "a poor man hears no threat" (Pro 13:8)<br>• "the poor man had nothing but one little ewe lamb" (2Sa 12:3)<br>**Humility or affliction** (H6035, G4434):<br>• "let the humble hear and be glad" (Psa 34:2)<br>• "When the humble see it … let your hearts revive" (Psa 69:32)<br>• "a lowly spirit with the poor" (Pro 16:19)<br>• "poor in spirit" (Mat 5:3) [H1] |
| **Issue** | H6035 and G4434 bridge poverty and humility. H0034, H1800 and H7326 are mostly material need. |
| **Options** | (a) keep all in M09; (b) keep H6035 and G4434 in M09, and move H0034, H1800 and H7326 to M46 Wealth & Riches; (c) keep all with an alternative-cluster note to M46; (d) something else. |
| **Recommendation** | **(c)**, a light touch [Claude reading]. Poverty and lowliness are genuinely entangled in the Psalms (Psa 109:16, 22 "poor and needy … my heart is stricken"). |
| **Ruling** | ______ |

### R7 — H7451A "bad: harmful" and H7489A "be evil" in M58 Wickedness
| | |
|---|---|
| **Cluster(s)** | M58 (current); M03 Grief & Lament and M28 Envy & Greed (candidates for particular senses) |
| **Strong's** | H7451A *raʿ* "bad, harmful, unpleasant"; H7489A *rāʿaʿ* "be evil, be bad" |
| **DB now** | Both → M58 · **old** (relocated M27 → M10b → M58) |
| **Evidence** | **H7451A** (14 verses), mostly not wickedness:<br>• "sadness of the heart" (Neh 2:2)<br>• "sings songs to a heavy heart" (Pro 25:20)<br>• "ugly and thin" cows (Gen 41:3, 4, 19)<br>• "not afraid of bad news" (Psa 112:7)<br>• "an unhappy business" (Ecc 1:13; 4:8); "grievous" (Ecc 2:17; 6:2)<br>• "harmful spirit from God" (1Sa 16:14–16, 23; 18:10; 19:9) [O]<br>**H7489A** includes the "evil eye" idiom = begrudging: "your heart shall not be grudging" (Deu 15:10); "look grudgingly on your poor brother" (Deu 15:9); "will begrudge … the wife he embraces" (Deu 28:54, 56). |
| **Issue** | *raʿ* covers "bad" in every register. The Strong's-level filing puts sadness, ugliness and misfortune into Wickedness. |
| **Options** | (a) keep, and treat the non-moral senses at verse level in M58's analysis; (b) move H7451A to another cluster; (c) keep with alternative-cluster notes (M03 for "sad heart"; M28 for "grudging"); (d) something else. |
| **Recommendation** | **(c)** [Claude reading]. A move would lose the genuine "harmful spirit" and "evil" uses. |
| **Ruling** | ______ |

### R8 — Heuristic misfits in M61 Purity & Holiness
| | |
|---|---|
| **Cluster(s)** | M61 (current) |
| **Strong's** | H4974 *mĕtōm* "soundness"; H5352 *nāqâ* "be clear / go unpunished"; H1305 *bārar* "purify / test / sharpen"; H8235 *shiprâ* "clearness, fairness" |
| **DB now** | All four → M61 · **heur** · "family=purity-holiness-sanctification" |
| **Evidence** | • "There is no soundness in my flesh because of your indignation" (Psa 38:3, 7) — bodily health<br>• "he will not go unpunished" (Pro 16:5) — judicial<br>• "Sharpen the arrows!" (Jer 51:11); "God is testing them" (Ecc 3:18); "speak sincerely" (Job 33:3); "not to winnow or cleanse" (Jer 4:11) — mixed<br>• "By his wind the heavens were made fair" (Job 26:13) — sky |
| **Issue** | H4974 → M73 Sickness & Weakness; H5352 → M26 Judgment & Condemnation; H8235 → T13 Natural-World. H1305 is genuinely mixed. |
| **Options** | (a) keep all; (b) move H4974 → M73, H5352 → M26, H8235 → T13, and keep H1305 in M61 with a note; (c) decide word by word. |
| **Recommendation** | **(b)** [Claude reading]. |
| **Ruling** | ______ |

### R9 — Mixed items in M14 Deceit & Falsehood
| | |
|---|---|
| **Cluster(s)** | M14 (current) |
| **Strong's** | H1892 *hevel* "vanity, breath"; H3584 *kāḥaš* "deceive / grow lean"; H7423B *rĕmiyyâ* "slackness"; H3908 *laḥash* "charm, amulet"; H3868 *lûz* "turn aside"; H5956 *ʿālam* "hide, conceal" |
| **DB now** | H1892 · LLM · **medium**; H3584 · LLM · **high**; H7423B, H3908, H3868, H5956 · **old** |
| **Evidence** | • **H1892** (15 verses): the Ecclesiastes "vanity … striving after wind" refrain (Ecc 1:14; 2:11, 17, 26; 4:4, 16; 6:9); "same breath … all is vanity" (Ecc 3:19); "a breath will take them away" (Isa 57:13). The sense is futility / breath, not falsehood.<br>• **H3584**: "my body has become gaunt" (Psa 109:24) — the homograph "grow lean" [lexical; verify]<br>• **H7423B**: "an idle person will suffer hunger" (Pro 19:15) — sloth<br>• **H3908**: "the amulets" (Isa 3:20) — object<br>• **H3868**: "Let them not escape from your sight" (Pro 4:21)<br>• **H5956**: "not to hide yourself from your own flesh" (Isa 58:7); "the Lord has hidden it from me" (2Ki 4:27); "it is hidden from him" (Lev 5:2, 4) — concealment or unawareness, not deceit |
| **Issue** | Only part of each word's range fits "deceit". H1892 is the most significant, because *hevel* + *rûaḥ* is a major inner-being pairing (§4.5). |
| **Options** | (a) keep all; (b) keep H1892 in M14 with a note (idols are *hevel* = empty / false); move H7423B → M67 and H3908 → T12; leave H3584, H3868 and H5956 in M14 with verse-level notes; (c) move H1892 to M24 Faintness & Despair or another cluster you name; (d) something else. |
| **Recommendation** | **(b)** [Claude reading]. |
| **Ruling** | ______ |

### R10 — Mixed items in M08 Pride & Arrogance
| | |
|---|---|
| **Cluster(s)** | M08 (current); M53 Dishonor & Disgrace and M22 Praise & Song (candidates) |
| **Strong's** | H2778A *ḥārap* "reproach, taunt"; H1984H *hālal* "boast / glory"; H3887 *lûṣ* "mock" (as *mĕlîṣ* "envoy"); height words H4791, H6967, H1363, H1364 |
| **DB now** | H2778A · **heur** · "family=pride-arrogance-scoffing". The others → M08 · **old**. |
| **Evidence** | • **H2778A:**<br>&nbsp;&nbsp;– "Zebulun is a people who risked [*despised*] their lives to the death" (Judg 5:18)<br>&nbsp;&nbsp;– "my heart does not reproach me" (Job 27:6)<br>&nbsp;&nbsp;– "that I may answer him who reproaches me" (Pro 27:11)<br>• **H1984H** is praise as often as boast:<br>&nbsp;&nbsp;– "My soul makes its boast in the Lord" (Psa 34:2)<br>&nbsp;&nbsp;– "Glory in his holy name" (1Ch 16:10; Psa 105:3)<br>&nbsp;&nbsp;– "all the upright in heart exult" (Psa 64:10)<br>&nbsp;&nbsp;– versus "the wicked boasts of the desires of his soul" (Psa 10:3)<br>• **H3887:** "the envoys [*interpreters*] of the princes of Babylon" (2Ch 32:31)<br>• **Height words, physical or divine:**<br>&nbsp;&nbsp;– "the Spirit is poured upon us from on high" (Isa 32:15) [D2]<br>&nbsp;&nbsp;– "the height of Zion" (Jer 31:12)<br>&nbsp;&nbsp;– "persons of every stature" (Eze 13:18)<br>&nbsp;&nbsp;– "the height of his stature" (1Sa 16:7) |
| **Issue** | H2778A is reproach or disgrace rather than pride. H1984H is split between praise and boast. H3887 and the height words carry pride only in some verses. |
| **Options** | (a) keep all; (b) move H2778A → M53; keep H1984H in M08 with an alternative-cluster note to M22; leave the height words and H3887 with verse-level notes; (c) decide word by word. |
| **Recommendation** | **(b)** [Claude reading]. |
| **Ruling** | ______ |

---

## X. Cluster cross-reference — where each cluster appears in this file

Use this when the file accompanies a cluster's analysis. It lists the sections to read, and the Strong's in that cluster that are flagged in §0 or §R. "Misfile" means the word's sense **in these verses** does not match the cluster. It is **not** a claim that the Strong's is wrongly assigned everywhere.

| Cluster | Sections | Flagged Strong's (DB source · confidence) |
|---|---|---|
| **M12** Righteousness & Integrity | §1 (all); §7.3 purity (inner vs ritual) | **R3** H2889, H2891, H2135, H1249, G2511, G2513 (old); H2134 (LLM · high); G2514 (auto-precedent). H4941J "custom" at 1Sa 2:13; Num 27:11 (heur) — §0.6. H4941G/H also carry an active **FLAG** row (old) — §0.6. |
| **M58** Wickedness | §2 (all); §2.1 evil / harmful spirits | **R7** H7451A, H7489A (old) |
| **M56** Sin & Guilt | §3 (all) | **R3** H2932 (heur). H2398 piel "cleanse / purify" at Num 19:13, 20; 31:19 and "misses his way" at Pro 19:2 (heur) — §0.5 |
| **M14** Deceit & Falsehood | §4 (all); §4.5 wind and vanity | **R2** G0080 (LLM · medium; also T8). **R9** H1892 (LLM · medium), H3584 (LLM · high), H7423B, H3908, H3868, H5956 (old) |
| **M57** Corruption & Perversion | §5 | H7806 "fine twined" at Exo 36:8 (heur) — §0.7 |
| **M62** Truth & Sincerity | §6 | **R5** G2117 (heur). G0950 "confirm" at Heb 13:9 and G0951 at Phili 1:7 are only weak fits (heur) — §0.7 |
| **M61** Purity & Holiness | §7; §7.1 "Holy Spirit" pre-filter (92 verses) | **R8** H4974, H5352, H1305, H8235 (heur). H7307I "sides" at Eze 42:20 — §0.7 |
| **M10c** Defilement | §8 | — (receives H2932 under R3) |
| **M08** Pride & Arrogance | §9 | **R1** H6965B (LLM · medium). **R5** G0757 (old). **R10** H2778A (heur), H1984H, H3887, H4791, H6967, H1363, H1364 (old). G5246 is already review-flagged in the DB (LLM · low · review_flag=1). |
| **M09** Humility & Lowliness | §10 | **R4** H5081G (old). **R5** H4102 (LLM · high), G5549 (auto-precedent), G1299 (old). **R6** H0034, H1800, H7326, H6035, G4434 (heur) |
| **M47** Inner Seat | all; §11 cross-cutting | — |
| Candidate receiving clusters | M61 / M10c (R3); M64 (R4); T3 / T6 (R5, R1); M46 (R6); M03 / M28 (R7); M73 / M26 / T13 (R8); M67 / T12 (R9); M53 / M22 (R10); T8 (R2) | — |
| Already review-flagged in DB (not raised) | G5246 (M08), G4108 and G5573 (M14), H2612 (M10c), H4827 (M58) — all LLM · low · review_flag=1 | — |
| All batches | — | **Batch A R7** process ruling |

---

## 0. Data notes

1. **"Holy" inside "Holy Spirit" (M61) — pre-filter.**
   - **93 pairs in 92 verses** are G0040G / H6944G "holy" at d1 from *pneuma / rûaḥ*. In these, M61 is carried by the name of the Spirit, not by a statement about purity.
   - They are **not dropped**. They are summarised as a group in §7.1 for what they say about the Spirit and the inner seat.
   - The **other 90 M61 verses** are read in §7.2–7.5.
2. **The other pre-filters do not apply here.** Neither "declares the Lord" (M42) nor "Lord of hosts" (M72) falls in Batch D clusters.
3. **"Arise" (H6965B) accounts for 30 of the 101 M08 verses.** None is about pride. They are noted and not used in §9. **→ Ruling R1.**
4. **"Brothers" (G0080) accounts for 32 of the 126 M14 verses.** None is about deceit. They are noted and not used in §4. **→ Ruling R2.**
5. **Sin-root verbs used for purification** [lexical]. H2398 *ḥāṭāʾ* in the piel means "to de-sin", i.e. purify:
   - "does not cleanse himself" (Num 19:13, 20); "purify yourselves" (Num 31:19)
   - The qal can mean "miss": "misses his way" (Pro 19:2); "fails to find me" (Pro 8:36)
   - These are kept only where the sin sense is present (Pro 8:36, §3.2).
6. **Justice / "rules" (H4941 *mišpāṭ*).**
   - Most M12 *mišpāṭ* pairs are "rules / judgments" = statutes (Lev 26:15; Psa 119:20; Deu 26:16). They are kept in §1.5, because the soul's and heart's relation to God's rules is a real theme.
   - H4941J "custom" (1Sa 2:13 "the custom of the priests … while the meat was boiling") and Num 27:11 "a statute and rule" (with *šĕʾēr* "kinsman") are noted and not used.
   - H4941G/H also carries an active **FLAG** row in `cluster_strong` (old).
7. **Misfiled tags, noted and not used:**
   - Gen 41:3, 4, 19: "ugly and thin" cows — *bāśār* "flesh" + *raʿ* "bad" (M58).
   - Exo 36:8: "craftsmen [*wise of heart*] … fine twined linen" (H7806 "twist", M57).
   - Heb 13:9 "heart … strengthened [*confirmed*]" (G0950, M62) — confirmation, not truth. Phili 1:7 "confirmation of the gospel" (G0951) likewise.
   - Eze 42:20 "on the four sides" (H7307I *rûaḥ* = side / quarter) + "holy" (M61).
   - Job 26:13 "By his wind the heavens were made fair" (H8235, M61).
   - Pro 19:15 "idle person" (H7423B, M14); Isa 3:20 "perfume boxes … amulets" (*nephesh* "perfume box" + H3908, M14).
   - Psa 109:24 "my body has become gaunt" (H3584, M14).
   - Judg 19:5, 8, 9; 2Sa 19:7; Judg 19:3 "heart" beside "arise / delay" (M08, M09) — idioms: "strengthen your heart" = eat; "speak to the heart" = speak kindly.
   - Luk 12:45; Mat 24:48 "says to himself [*in his heart*] 'My master is delayed'" — the delay tag is a misfile (R5). The inner-speech content is kept as ◆ in §10.
   - Deu 22:26 "murdering" (*nephesh* in "strike him … a life") + "offense" (M56).
   - Lev 20:19 "relative" (*šĕʾēr* flesh) + "bear iniquity" (M56).
8. **Nephesh = corpse** [lexical]. *nephesh mēt* "soul of a dead one" = dead body. It is the M10c pairing in Num 5:2; 6:11; 9:6, 7, 10; 19:11, 13; Lev 21:1, 11; 22:4; Hag 2:13. It is kept in §8.2 as a fringe of real significance, not dropped.
9. **Distance note.** Positions are in original-language word order [verify]. d0 = one token carries both tags (e.g. 2Ch 26:16 "grew proud" = *gāvah lēv* "his heart was high"; Mic 2:11 "wind" carrying both the *rûaḥ* and the *šeqer* tags).

---

## 1. Righteousness and integrity (M12)

### 1.1 The upright heart (*yišrê lēv*)
- **The Psalms formula "upright in heart":** Psa 7:10; 11:2; 32:11; 36:10; 64:10; 94:15; 97:11; 125:4 ("upright in their hearts").
  - The upright in heart are the ones who are **saved** (Psa 7:10), **shot at in the dark** (Psa 11:2), told to **rejoice** (Psa 32:11; 64:10), **given light and joy** (Psa 97:11) and who **follow justice** (Psa 94:15).
- **In narrative:**
  - "in uprightness of heart toward you" (1Ki 3:6)
  - "In the uprightness of my heart I have freely offered" (1Ch 29:17) — the God who "tests the heart"
  - "the Levites were more upright in heart than the priests in consecrating themselves" (2Ch 29:34)
- **Heart to heart:** "Is your heart true [*upright*] to my heart as mine is to yours?" (2Ki 10:15) — uprightness as a relation between two hearts.
- **Speech from the upright heart:** "My words declare the uprightness of my heart" (Job 33:3); "I will praise you with an upright heart" (Psa 119:7).
- **Not the ground of blessing:** "Not because of your righteousness or the uprightness of your heart" (Deu 9:5); "Do not say in your heart, '… because of my righteousness'" (Deu 9:4).
- [Claude reading] **Uprightness is almost always a quality of the heart**, not of the soul or the spirit. The upright heart is a standing identity ("the upright in heart"), not a single act.

### 1.2 Integrity of heart (*tōm lēvāv*) [lexical]
- "In the integrity of my heart and the innocence of my hands I have done this" (Gen 20:5). God replies: "I know that you have done this in the integrity of your heart, and it was I who kept you from sinning" (Gen 20:6).
- "if you will walk before me … with integrity of heart and uprightness" (1Ki 9:4)
- "With upright [*integrity of*] heart he shepherded them" (Psa 78:72)
- "I will walk with integrity of heart within my house" (Psa 101:2)
- "May my heart be blameless in your statutes" (Psa 119:80)
- **Blameless vs crooked:** "Those of crooked heart are an abomination … those of blameless ways are his delight" (Pro 11:20).
- **Holding it fast:** "I hold fast my righteousness … my heart does not reproach me" (Job 27:6); "He still holds fast his integrity" (Job 2:3).
- [Claude reading] **Gen 20:5–6 separates integrity of heart from correctness of act.** Abimelech's heart was whole; the act would still have been sin, and God prevented it. **Integrity is a state of the heart that God can recognise even where knowledge is lacking.** Compare "whole heart" (*lēv shālēm*) in Batch C §5.1, R2.

### 1.3 The pure / clean heart (see R3)
- "Blessed are the pure in heart, for they shall see God" (Mat 5:8)
- "Truly God is good … to those who are pure in heart" (Psa 73:1); "All in vain have I kept my heart clean" (Psa 73:13)
- "He who has clean hands and a pure heart, who does not lift up his soul to what is false" (Psa 24:4) — **hands, heart and soul in one ethical profile**
- "Create in me a clean heart, O God, and renew a right spirit within me" (Psa 51:10) [H1]
- **Who can claim it:** "Who can say, 'I have made my heart pure'?" (Pro 20:9).
- **Loved:** "He who loves purity of heart … will have the king as his friend" (Pro 22:11).
- **NT:**
  - "love that issues from a pure heart and a good conscience and a sincere faith" (1Ti 1:5)
  - "those who call on the Lord from a pure heart" (2Ti 2:22)
  - "love one another earnestly from a pure heart" — "having purified your souls" (1Pe 1:22)
  - "having cleansed their hearts by faith" (Act 15:9)
  - "purify your hearts, you double-minded" (Jam 4:8)
- [Claude reading] **The heart is purified by God (Psa 51:10; Act 15:9) and by the person (Jam 4:8; 1Pe 1:22). It cannot be declared pure by self-assessment (Pro 20:9).**

### 1.4 The conscience clean or evil
- "hold the mystery of the faith with a clear conscience" (1Ti 3:9); "whom I serve … with a clear conscience" (2Ti 1:3)
- "our hearts sprinkled clean from an evil conscience and our bodies washed with pure water" (Heb 10:22) — **heart, conscience and body in one verse**
- "the blood of Christ, who through the eternal Spirit offered himself without blemish … purify our conscience from dead works" (Heb 9:14) [U] — set against "the purification of the flesh" (Heb 9:13)
- "both their minds and their consciences are defiled" (Tit 1:15)

### 1.5 Soul and heart toward God's rules (*mišpāṭîm*)
- **Longing:** "My soul is consumed with longing for your rules at all times" (Psa 119:20); "Let my soul live and praise you, and let your rules help me" (Psa 119:175).
- **Abhorring:** "if your soul abhors my rules" (Lev 26:15); "their soul abhorred my statutes" (Lev 26:43).
- **Doing them with all the inner seat:** "be careful to do them with all your heart and with all your soul" (Deu 26:16).
- **Heart set, heart gone elsewhere:**
  - "Ezra had set his heart to study the Law … and to teach his statutes and rules" (Ezr 7:10)
  - "they rejected my rules … for their heart went after their idols" (Eze 20:16)
  - "that he may incline our hearts to him … to keep … his rules" (1Ki 8:58)
- **The Spirit causes obedience:** "I will put my Spirit within you, and cause you to walk in my statutes and be careful to obey my rules" (Eze 36:27) [D1].
- ◆ **Flesh and judgments:** "My flesh trembles for fear of you, and I am afraid of your judgments" (Psa 119:120).
- ◆ **The breastpiece of judgment on Aaron's heart:** "Aaron shall bear the judgment of the people of Israel on his heart before the Lord regularly" (Exo 28:29–30). This is the literal chest, but it is the one place in the batch where the heart **carries other people** before God.

### 1.6 Spirit and justice
- **Divine [D1]:**
  - "filled with power, with the Spirit of the Lord, and with justice and might, to declare to Jacob his transgression" (Mic 3:8)
  - "I have put my Spirit upon him; he will bring forth justice" (Isa 42:1)
- **Disposition [X]:** "a spirit of justice to him who sits in judgment" (Isa 28:6).
- **Undetermined [U]:** "by a spirit of judgment and by a spirit of burning" (Isa 4:4).
- **Human spirit made righteous:**
  - "the spirits of the righteous made perfect" (Heb 12:23) [H2]
  - "the Lord weighs the spirit" (Pro 16:2) [H2] // "the Lord weighs the heart" (Pro 21:2)
- **NT:**
  - "the Spirit is life because of righteousness" (Rom 8:10) [U]
  - "who walk not according to the flesh but according to the Spirit" (Rom 8:4) [D3]
  - "righteousness and peace and joy in the Holy Spirit" (Rom 14:17)
  - "renewal of the Holy Spirit" — "not because of works done by us in righteousness" (Tit 3:5)
  - "through the Spirit … we eagerly wait for the hope of righteousness" (Gal 5:5) [D3]
- **Heart and justification:** "with the heart one believes and is justified" (Rom 10:10).
- [Claude reading] **Pro 16:2 / 21:2 is a doublet:** "the Lord weighs the spirit" // "the Lord weighs the heart". In the evaluating verse, spirit and heart are interchangeable.

### 1.7 The righteous soul and the innocent life
- "tormenting his righteous soul over their lawless deeds" (2Pe 2:8)
- **Righteousness saves the soul-life:** "they would deliver but their own lives by their righteousness" (Eze 14:14, 20); "does what is just and right, he shall save his life" (Eze 18:27); "He restores my soul. He leads me in paths of righteousness" (Psa 23:3).
- **Innocent blood = innocent *nephesh*:**
  - "the lifeblood of the guiltless poor" (Jer 2:34)
  - "lay not on us innocent blood" — "this man's life" (Jon 1:14)
  - "They band together against the life of the righteous and condemn the innocent" (Psa 94:21)
  - "Why then will you sin against innocent blood?" (1Sa 19:5)
  - "takes a bribe to shed innocent blood" (Deu 27:25)
- **Unjust gain and the inner seat:**
  - "you have eyes and heart only for your dishonest gain" (Jer 22:17)
  - "their heart is set on their gain" (Eze 33:31)
  - "Incline my heart to your testimonies, and not to selfish gain" (Psa 119:36)
  - "The dogs have a mighty appetite [*nephesh*]; … each to his own gain" (Isa 56:11)
  - "greedy for unjust gain; it takes away the life of its possessors" (Pro 1:19)
- ◆ **The righteous regard animal life:** "Whoever is righteous has regard for the life [*nephesh*] of his beast" (Pro 12:10).
- ◆ **The puffed-up soul:** "his soul is puffed up; it is not upright within him, but the righteous shall live by his faith" (Hab 2:4). Heb 10:38 quotes it with God as speaker: "my soul has no pleasure in him".
- ◆ **Wind takes away righteous deeds:** "all our righteous deeds are like a polluted garment … our iniquities, like the wind, take us away" (Isa 64:6).

### 1.8 ◆ Fringe
- "because the way is long … the avenger of blood in hot anger [*his heart is hot*]" (Deu 19:6) — a heated heart
- "being put to death in the flesh but made alive in the spirit" (1Pe 3:18) [U]
- "Naaman … his flesh was restored like the flesh of a little child, and he was clean" (2Ki 5:14) — flesh renewed with ritual cleanness
- "The heart of the righteous ponders how to answer, but the mouth of the wicked pours out evil" (Pro 15:28) — heart before mouth

---

## 2. Wickedness (M58)

### 2.1 Evil and harmful spirits [O]
- **From God on Saul:**
  - "the Spirit of the Lord departed from Saul, and a harmful spirit from the Lord tormented him" (1Sa 16:14) [D1+O]
  - Also 1Sa 16:15, 16, 23; 18:10 ("rushed upon Saul, and he raved"); 19:9 ("as he sat in his house with his spear in his hand")
- **Sent between parties:** "God sent an evil spirit between Abimelech and the leaders of Shechem, and the leaders of Shechem dealt treacherously" (Judg 9:23).
- **NT:**
  - "evil spirits came out of them" (Act 19:12); "the evil spirit answered them, 'Jesus I know, and Paul I recognize, but who are you?'" (Act 19:15); "the man in whom was the evil spirit leaped on them" (Act 19:16)
  - "healed … of evil spirits" (Luk 7:21; 8:2)
  - "seven other spirits more evil than itself … the last state of that person is worse than the first" (Mat 12:45; Luk 11:26)
  - "the spiritual forces of evil in the heavenly places" — "not … against flesh and blood" (Eph 6:12)
  - ◆ "What if a spirit or an angel spoke to him?" (Act 23:9) [O]
- [Claude reading] **In the OT the harmful spirit is "from God / from the Lord" and comes *upon* a person episodically. In the NT evil spirits are *in* people and are cast out.** In both, the other-spirit acts on the human agent from outside (cf. Batch C §11.8).

### 2.2 The evil heart
- **Intention:** "every intention of the thoughts of his heart was only evil continually" (Gen 6:5); "the intention of man's heart is evil from his youth" (Gen 8:21).
- **The stubbornness of the evil heart** (Jer 3:17; 7:24; 11:8; 16:12; 18:12; 13:10). See Batch C §9.1.
- **Full of evil:** "the hearts of the children of man are full of evil, and madness is in their hearts" (Ecc 9:3); "the heart of the children of man is fully set to do evil" (Ecc 8:11).
- **Devising evil:**
  - "with perverted heart devises evil" (Pro 6:14); "a heart that devises wicked plans" (Pro 6:18)
  - "Deceit is in the heart of those who devise evil" (Pro 12:20)
  - "who plan evil things in their heart" (Psa 140:2)
  - "let none of you devise evil against another in your heart" (Zec 7:10; 8:17)
  - "their hearts shall be bent on doing evil" (Dan 11:27)
- **Hidden evil beneath speech:**
  - "who speak peace with their neighbors while evil is in their hearts" (Psa 28:3)
  - "he utters empty words, while his heart gathers iniquity" (Psa 41:6)
  - "fervent lips with an evil heart" (Pro 26:23); "seven abominations in his heart" (Pro 26:25)
- **Transgression speaks inside:** "Transgression speaks to the wicked deep in his heart" (Psa 36:1).
- **NT:**
  - "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21)
  - "Why do you think evil in your hearts?" (Mat 9:4)
  - "the evil person out of his evil treasure produces evil, for out of the abundance of the heart his mouth speaks" (Luk 6:45; Mat 12:34)
  - "an evil, unbelieving heart, leading you to fall away" (Heb 3:12)
  - "the evil one … snatches away what has been sown in his heart" (Mat 13:19)
- **Guarding against it:**
  - "Do not let my heart incline to any evil" (Psa 141:4)
  - "If I had cherished iniquity in my heart, the Lord would not have listened" (Psa 66:18)
  - "A perverse heart shall be far from me" (Psa 101:4)
  - "O Jerusalem, wash your heart from evil" (Jer 4:14)
- [Claude reading] **The heart is the source of evil (Mat 15:19), its storehouse (Luk 6:45) and where it hides behind speech (Psa 28:3).** The same heart can be asked to be kept from inclining to evil (Psa 141:4). Ecc 8:11 names a cause: delayed judgment emboldens the heart.

### 2.3 The soul and wickedness
- "The soul of the wicked desires evil" (Pro 21:10)
- "their soul delights in their abominations" (Isa 66:3)
- "the wicked boasts of the desires of his soul" (Psa 10:3)
- **God's soul hates:** "his soul hates the wicked and the one who loves violence" (Psa 11:5).
- **Evil against one's own soul:** "they have brought evil on themselves [*their nephesh*]" (Isa 3:9); "Why do you commit this great evil against yourselves [*your souls*]?" (Jer 44:7).
- **The soul-life guarded from evil:**
  - "The Lord will keep you from all evil; he will keep your life" (Psa 121:7)
  - "Deliver my soul from the wicked" (Psa 17:13)
  - "They repay me evil for good; my soul is bereft" (Psa 35:12)
- **Doing harm vs saving life:** "is it lawful on the Sabbath to do good or to do harm, to save life or to destroy it?" (Luk 6:9; Mar 3:4).
- **The abomination-person cut off:** "the persons who do them shall be cut off" (Lev 18:29).

### 2.4 Blasphemy against the Spirit [D]
- "the blasphemy against the Spirit will not be forgiven" (Mat 12:31) [D2]
- "whoever blasphemes against the Holy Spirit never has forgiveness, but is guilty of an eternal sin" (Mar 3:29; Luk 12:10) [D1]
- ◆ "If you then, who are evil, know how to give good gifts … how much more will the heavenly Father give the Holy Spirit" (Luk 11:13) [D1] — **evil humans, given the Spirit**
- **Flesh and blasphemy:** "defile the flesh, reject authority, and blaspheme the glorious ones" (Jude 8; 2Pe 2:10).

### 2.5 "Bad" that is not wickedness (see R7)
- **Sad heart:** "This is nothing but sadness [*evil*] of the heart" (Neh 2:2); "sings songs to a heavy heart" (Pro 25:20); "by sadness of face the heart is made glad" (Ecc 7:3).
- **Bad news, firm heart:** "He is not afraid of bad news; his heart is firm, trusting in the Lord" (Psa 112:7).
- **Grudging heart / evil eye:** "your heart shall not be grudging when you give" (Deu 15:10); "lest there be an unworthy thought in your heart … and your eye look grudgingly on your poor brother" (Deu 15:9).
- **Unhappy business:** "I applied my heart to seek … It is an unhappy business" (Ecc 1:13); "applying my heart … when man had power over man to his hurt" (Ecc 8:9).
- **Cheerful heart against evil days:** "All the days of the afflicted are evil, but the cheerful of heart has a continual feast" (Pro 15:15).

### 2.6 Discerning good and evil
- "Give your servant therefore an understanding mind [*hearing heart*] … that I may discern between good and evil" (1Ki 3:9)
- "the wise heart will know the proper time and the just way … will know no evil thing" (Ecc 8:5)
- "I turned my heart to know … the wickedness of folly" (Ecc 7:25)
- "I would not be able … to do either good or bad of my own will [*heart*]" (Num 24:13) — **Balaam's heart subordinated to the word**
- "those who say in their hearts, 'The Lord will not do good, nor will he do ill'" (Zep 1:12) — **the complacent heart denies God's agency**

### 2.7 Wind and the wicked
- "like chaff that the wind drives away" (Psa 1:4)
- "fire and sulfur and a scorching wind shall be the portion of their cup" (Psa 11:6)
- "their metal images are empty wind" (Isa 41:29)
- "what gain is there to him who toils for the wind?" (Ecc 5:16)
- "The wind shall shepherd all your shepherds" (Jer 22:22)
- "with the breath of his lips he shall kill the wicked" (Isa 11:4) — the messianic breath as judgment
- [Claude reading] **Wind is the medium of the wicked's insubstantiality and removal.** This pairs with §4.5 (falsehood as wind).

### 2.8 ◆ Fringe
- "No man has power to retain the spirit … nor will wickedness deliver those who are given to it" (Ecc 8:8) [U]
- "uncircumcised in heart and flesh" (Eze 44:7) — heart and flesh share one state
- "I know your presumption and the evil of your heart" (1Sa 17:28) — Eliab misreads David's heart (also M08, §9.5)
- "who tear the skin from off my people and their flesh from off their bones" (Mic 3:2); "When evildoers assail me to eat up my flesh" (Psa 27:2)
- "Should good be repaid with evil? Yet they have dug a pit for my life" (Jer 18:20)

---

## 3. Sin and guilt (M56)

### 3.1 The soul as the one who sins
- "Behold, all souls are mine … the soul who sins shall die" (Eze 18:4, 20)
- **The Levitical formula "if a soul [*anyone*] sins":** Lev 4:2, 27; 5:1, 15, 17; 6:2; Num 15:27–28, 30–31
- **Realising guilt afterwards:**
  - "though he did not know it, then realizes his guilt, he shall bear his iniquity" (Lev 5:17)
  - "it is hidden from him, when he comes to know it, and he realizes his guilt" (Lev 5:4; 5:2)
  - "that person realizes his guilt" (Num 5:6)
- **The high-handed soul:** "the person who does anything with a high hand … reviles the Lord, and that person shall be cut off" (Num 15:30).
- **Bearing iniquity:** "he shall bear his iniquity" (Lev 5:1, 17; 7:18; 19:8; Num 9:13).
- [lexical; Claude reading] **Here *nephesh* is the accountable person.** The Levitical texts allow the soul to sin **without knowing it**, and then to **come to know** its guilt. Guilt is then a state that awareness catches up with. The conscience (§3.5) is the NT term for that awareness.

### 3.2 Sin against one's own soul
- "he who fails to find me injures himself [*his nephesh*]" (Pro 8:36)
- "whoever provokes him to anger forfeits [*sins against*] his life" (Pro 20:2)
- "you have forfeited your life [*sinned against your soul*]" (Hab 2:10)
- "the censers of these men who have sinned at the cost of their lives" (Num 16:38)
- **"The sin of my soul":** "Shall I give my firstborn for my transgression, the fruit of my body for the sin of my soul?" (Mic 6:7).
- [Claude reading] **Sin is pictured as damage done to one's own *nephesh*.** This matches Pro 6:32 (§5) and Pro 1:19 (§1.7).

### 3.3 Sin and the heart
- **Guarded against:** "I have stored up your word in my heart, that I might not sin against you" (Psa 119:11); "Be angry, and do not sin; ponder in your own hearts on your beds" (Psa 4:4).
- **Hidden sin in the heart:**
  - "It may be that my children have sinned, and cursed God in their hearts" (Job 1:5)
  - "You shall not hate your brother in your heart … lest you incur sin" (Lev 19:17)
  - "an unworthy thought in your heart … and you be guilty of sin" (Deu 15:9)
- **Engraved:** "The sin of Judah is written with a pen of iron … on the tablet of their heart" (Jer 17:1).
- **Idols in the heart** as "the stumbling block of their iniquity" (Eze 14:3, 4, 7).
- **Sin and hardening:** "he sinned yet again and hardened his heart" (Exo 9:34).
- **The heart that strikes** ◆: "David's heart struck him after he had numbered the people. And David said, 'I have sinned greatly'" (2Sa 24:10). [Claude reading] **The heart acting as conscience**, before the word "conscience" exists.
- **Integrity kept from sinning:** "in the integrity of your heart … I kept you from sinning" (Gen 20:6).
- **Casting away:** "Cast away from you all the transgressions … and make yourselves a new heart and a new spirit!" (Eze 18:31) [H1]
- **Humbled:** "if then their uncircumcised heart is humbled and they make amends for their iniquity" (Lev 26:41).
- **False:** "Their heart is false; now they must bear their guilt" (Hos 10:2).
- **Consequence as a heart-question:** "if you say in your heart, 'Why have these things come upon me?' it is for the greatness of your iniquity" (Jer 13:22).
- **Obedient from the heart:** "slaves of sin have become obedient from the heart" (Rom 6:17).

### 3.4 Spirit and sin
- **Human:** "in whose spirit there is no deceit" beside "the Lord counts no iniquity" (Psa 32:2) [H1].
- **All spirits:** "O God, the God of the spirits of all flesh, shall one man sin, and will you be angry with all the congregation?" (Num 16:22) [H2] — **God's relation to every spirit is the ground of the plea against collective punishment.**
- **Spirit of uncleanness:** "I will remove from the land the prophets and the spirit of uncleanness" (Zec 13:2) [O+X].
- **Divine:**
  - "an alliance, but not of my Spirit, that they may add sin to sin" (Isa 30:1) [D1]
  - "the Spirit of the Lord … to declare to Jacob his transgression" (Mic 3:8) [D1]
  - "The Spirit of God clothed Zechariah … 'Why do you break the commandments?'" (2Ch 24:20) [D1]
  - "for the forgiveness of your sins, and you will receive the gift of the Holy Spirit" (Act 2:38)
  - "the law of the Spirit of life has set you free … from the law of sin and death" (Rom 8:2)
- **Restoring in a gentle spirit:** "you who are spiritual should restore him in a spirit of gentleness" (Gal 6:1) [X].
- ◆ "The prophet is a fool; the man of the spirit is mad, because of your great iniquity" (Hos 9:7) [U].

### 3.5 Flesh and conscience
- **Flesh:**
  - "while we were living in the flesh, our sinful passions … were at work in our members" (Rom 7:5)
  - "I am of the flesh, sold under sin" (Rom 7:14); "with my flesh I serve the law of sin" (Rom 7:25)
  - "in the likeness of sinful flesh … he condemned sin in the flesh" (Rom 8:3)
  - "whoever has suffered in the flesh has ceased from sin" (1Pe 4:1)
  - "dead in your trespasses and the uncircumcision of your flesh" (Col 2:13)
  - "by works of the law no human being [*flesh*] will be justified" (Rom 3:20)
- **Body and sin (OT):** "There is no soundness in my flesh because of your indignation; there is no health in my bones because of my sin" (Psa 38:3).
- ◆ **Mouth and flesh:** "Let not your mouth lead you [*your flesh*] into sin" (Ecc 5:6) [lexical]. The flesh is the self that the mouth can cause to sin.
- **Ritual flesh:** "if he does not wash them or bathe his flesh, he shall bear his iniquity" (Lev 17:16).
- **Conscience:**
  - "would no longer have any consciousness of sins" (Heb 10:2)
  - "wounding their conscience when it is weak, you sin against Christ" (1Co 8:12)

### 3.6 The servant's soul and sin (Isa 53)
- "when his soul makes an offering for guilt" (Isa 53:10)
- "Out of the anguish of his soul he shall see … he shall bear their iniquities" (Isa 53:11)
- "he poured out his soul to death … yet he bore the sin of many" (Isa 53:12)
- [Claude reading] **The *nephesh* is itself the guilt offering.** It is the only place in the batch where one soul carries others' sin.

### 3.7 Life hunted without sin; forgiveness reaching the inner seat
- **Hunted without sin:**
  - "What is my guilt? … that he seeks my life?" (1Sa 20:1)
  - "I have not sinned against you, though you hunt my life" (1Sa 24:11)
  - "they lie in wait for my life … For no transgression or sin of mine" (Psa 59:3)
- **Forgiveness reaching the inner seat:**
  - "heal me [*my nephesh*], for I have sinned" (Psa 41:4)
  - "you have delivered my life from the pit … you have cast all my sins behind your back" (Isa 38:17)
  - "will save his soul from death and will cover a multitude of sins" (Jam 5:20)
  - "Take heart, my son; your sins are forgiven" (Mat 9:2)
  - ◆ "Speak tenderly [*to the heart of*] Jerusalem … her iniquity is pardoned" (Isa 40:2) [lexical]
  - "The Lord redeems the life of his servants; none … will be condemned" (Psa 34:22)
- **Guilt recalled through another's soul:** "we are guilty concerning our brother, in that we saw the distress of his soul" (Gen 42:21).

### 3.8 ◆ Wind and sin
- "our iniquities, like the wind, take us away" (Isa 64:6)
- "they sweep by like the wind and go on, guilty men, whose own might is their god" (Hab 1:11)
- "to the sinner he has given the business of gathering … a striving after wind" (Ecc 2:26)

---

## 4. Deceit and falsehood (M14)

### 4.1 Lying and deceiving spirits [O]
- **Put by the Lord:**
  - "I will go out, and will be a lying spirit in the mouth of all his prophets … You are to entice him" (1Ki 22:22; 2Ch 18:21)
  - "the Lord has put a lying spirit in the mouth of all these your prophets" (1Ki 22:23; 2Ch 18:22)
- **NT:**
  - "devoting themselves to deceitful spirits and teachings of demons" (1Ti 4:1) [D2+O] — introduced by "the Spirit expressly says"
  - "do not believe every spirit, but test the spirits … many false prophets" (1Jo 4:1) [U]
  - "three unclean spirits like frogs" out of "the mouth of the false prophet" (Rev 16:13)
- **Treachery follows the sent spirit:** "God sent an evil spirit … the leaders of Shechem dealt treacherously" (Judg 9:23).
- [Claude reading] **Other spirits lie through mouths** (1Ki 22; Rev 16:13). The divine Spirit, by contrast, **warns about** them (1Ti 4:1). 1Jo 4:1 makes "spirit" the thing to be tested.

### 4.2 Lying to the Holy Spirit; conscience in the Spirit
- "why has Satan filled your heart to lie to the Holy Spirit" (Act 5:3) [D1]; "Why is it that you have contrived this deed in your heart? You have not lied to man but to God" (Act 5:4)
- "I am not lying; my conscience bears me witness in the Holy Spirit" (Rom 9:1) [D1]
- [Claude reading] **In Act 5:3 the heart is filled by Satan** — an other-agent occupying the heart, not the spirit. In Rom 9:1 the conscience testifies "in" the Holy Spirit: a human faculty authenticated by the divine one.

### 4.3 The deceiving and deceived heart
- "The heart is deceitful above all things, and desperately sick; who can understand it?" (Jer 17:9)
- **Self-deception:**
  - "The pride of your heart has deceived you" (Obd 3; Jer 49:16)
  - "a deluded heart has led him astray, and he cannot deliver himself or say, 'Is there not a lie in my right hand?'" (Isa 44:20)
  - "Do not deceive yourselves [*your souls*]" (Jer 37:9)
- **Prophecy from the heart's deceit:** "the deceit of their own minds" (Jer 14:14); "lies in the heart of the prophets … the deceit of their own heart" (Jer 23:26). Cf. Batch B §6.
- **Lying words conceived in the heart:** "conceiving and uttering from the heart lying words" (Isa 59:13).
- **Divided or pretended heart:**
  - "did not return to me with her whole heart, but in pretense" (Jer 3:10)
  - "with flattering lips and a double heart [*a heart and a heart*] they speak" (Psa 12:2) [lexical]
  - "How can you say, 'I love you,' when your heart is not with me?" (Judg 16:15)
  - "This people honors me with their lips, but their heart is far from me" (Mar 7:6)
- **Crooked / perverse heart:** Pro 11:20; 17:20 ("does not discover good"); Psa 101:4; Pro 23:33 ("your heart utter perverse things" — wine).
- **Hearts of the naive deceived:** "by smooth talk and flattery they deceive the hearts of the naive" (Rom 16:18).
- **Planning in the heart:** "in his own mind he shall become great … by his cunning he shall make deceit prosper" (Dan 8:25).
- [Claude reading] **The heart is both deceiver and deceived.** It deceives its owner (Obd 3), invents false prophecy (Jer 23:26) and can be split in two (Psa 12:2). This extends Batch C §9.1 ("follow your own heart" as the charge).

### 4.4 Soul, spirit and conscience in truthfulness
- **Soul:**
  - "who does not lift up his soul to what is false" (Psa 24:4)
  - "whoever guards his soul will keep far from them [the crooked]" (Pro 22:5)
  - "putting to death souls who should not die and keeping alive souls who should not live, by your lying" (Eze 13:19) — **lies that kill and keep alive souls**
  - "A truthful witness saves lives" (Pro 14:25)
  - "the desire [*nephesh*] of the treacherous is for violence" (Pro 13:2)
- **Spirit [H1 / H2]:**
  - "in whose spirit there is no deceit" (Psa 32:2)
  - "guard yourselves in your spirit, and let none of you be faithless to the wife of your youth" (Mal 2:15 [U+H1]; 2:16 [H1])
  - "he who is trustworthy in spirit keeps a thing covered" (Pro 11:13)
  - "perverseness in it [the tongue] breaks the spirit" (Pro 15:4) [H2] — **a lying tongue damages another's spirit**
- **Conscience:**
  - "liars whose consciences are seared" (1Ti 4:2)
  - "by the open statement of the truth we would commend ourselves to everyone's conscience" (2Co 4:2)
  - "having a good conscience, so that, when you are slandered …" (1Pe 3:16)
- [Claude reading] **Faithfulness in marriage is guarded "in your spirit"** (Mal 2:15–16). The human spirit is the place where fidelity or treachery is decided.

### 4.5 Wind and vanity — falsehood as insubstantial (see R9)
- **Wind and lies at d0:** "If a man should go about and utter wind and lies" (Mic 2:11).
- "Ephraim feeds on the wind … they multiply falsehood" (Hos 12:1).
- "Like clouds and wind without rain is a man who boasts of a gift he does not give" (Pro 25:14).
- **Idols false, no breath in them:** "his images are false, and there is no breath in them" (Jer 10:14; 51:17).
- **"Vanity and a striving after wind"** (*hevel* + *rûaḥ*): Ecc 1:14; 2:11, 17, 26; 4:4, 16; 6:9.
- **Heart and vanity:**
  - "I said in my heart … this also is vanity" (Ecc 2:1, 15)
  - "Even in the night his heart does not rest. This also is vanity" (Ecc 2:23)
  - "Remove vexation from your heart, and put away pain from your body, for youth … are vanity" (Ecc 11:10)
- **Breath and vanity:** "They all have the same breath … for all is vanity" (Ecc 3:19); "The wind will carry them all off, a breath [*hevel*] will take them away" (Isa 57:13).
- [lexical; Claude reading] ***hevel* is literally "breath / vapour"** and stands in parallel with *rûaḥ* "wind". **Falsehood, idolatry and futility share one image: moving air with nothing in it.** This is the M14 side of Batch C §1.9 (desire aimed at wind).

### 4.6 ◆ Fringe
- "not to hide yourself from your own flesh" (Isa 58:7) — kin as one's flesh; concealment as withdrawal of care
- "for she is in bitter distress [*her soul is bitter*], and the Lord has hidden it from me" (2Ki 4:27) — the prophet not told of a soul's distress
- "His greed [*nephesh*] is as wide as Sheol … wine is a traitor" (Hab 2:5)
- "those who do not confess the coming of Jesus Christ in the flesh. Such a one is the deceiver" (2Jo 7)
- "satisfy your desire [*nephesh*] in scorched places … like a spring of water, whose waters do not fail [*lie*]" (Isa 58:11)
- "Whom did you dread and fear, so that you lied, and did not … lay it to heart?" (Isa 57:11) — fear → lying → not laying to heart

---

## 5. Corruption, perversion, adultery, unfaithfulness (M57)

- **Twisted heart:** "one of twisted mind [*heart*] is despised" (Pro 12:8).
- **Folly → heart rages at God:** "When a man's folly brings his way to ruin, his heart rages against the Lord" (Pro 19:3).
- **Adultery in and from the heart:**
  - "committed adultery with her in his heart" (Mat 5:28)
  - "out of the heart come … adultery" (Mat 15:19; Mar 7:21)
  - "He who commits adultery lacks sense [*heart*]; he who does it destroys himself [*his nephesh*]" (Pro 6:32) — cf. Batch C §1.5
  - "eyes full of adultery … They entice unsteady souls. They have hearts trained in greed" (2Pe 2:14)
- **The unfaithful soul (*maʿal*):** "If anyone [*a soul*] commits a breach of faith" (Lev 5:15; 6:2; Num 5:6).
- **Heart lifted → unfaithfulness:** "when he was strong, he grew proud [*his heart was high*], to his destruction. For he was unfaithful" (2Ch 26:16). This is a Pride → Corruption sequence; see §9.
- **Flesh vs Spirit harvest:** "the one who sows to his own flesh will from the flesh reap corruption, but the one who sows to the Spirit will from the Spirit reap eternal life" (Gal 6:8) [D3].
- **Perishable flesh:** "flesh and blood cannot inherit the kingdom of God, nor does the perishable inherit the imperishable" (1Co 15:50).
- **Turning the heart after perversity:** "if they turn their heart … saying, 'We have sinned and have acted perversely'" (1Ki 8:47; 2Ch 6:37).
- ◆ "Do not let the king take it to heart" (2Sa 19:19) — Shimei asks that his wrong not be laid on the king's heart.
- [Claude reading] **Adultery is located in the heart before the act (Mat 5:28), and it destroys the soul after it (Pro 6:32).** The heart is the start of the act, and the soul is what it destroys.

---

## 6. Truth and sincerity (M62)

- "they received their food with glad and generous [*simple*] hearts" (Act 2:46)
- "your heart is not right [*straight*] before God" (Act 8:21) — Simon; the only M62-sense use of G2117 (R5)
- "the testimony of our conscience, that we behaved … with simplicity and godly sincerity" (2Co 1:12) — **the conscience as witness to sincerity**
- ◆ "it is good for the heart to be strengthened by grace, not by foods" (Heb 13:9) — heart vs food, cf. Mar 7:19 (§7.3)
- "I hold you in my heart" (Phili 1:7)
- Noted and not used: "immediately" (Mar 1:12 [D2]; 7:25 [O]; Mat 3:16 [D1]).

---

## 7. Purity and holiness (M61)

### 7.1 Pre-filter: "Holy Spirit" (92 verses, reported as a group)
These verses bear on the Spirit's relation to the human inner seat, not on purity. What they say, by function:
- **Filling / fullness:**
  - "filled with the Holy Spirit" (Luk 1:15, 41, 67; Act 2:4; 4:8, 31; 9:17; 13:9, 52)
  - "full of the Holy Spirit" (Luk 4:1; Act 6:5; 7:55; 11:24)
- **Given / received / falling on:** Act 1:5, 8; 2:33, 38; 8:15, 17, 19; 10:44, 45, 47; 11:15, 16; 19:2, 6; Luk 11:13; Joh 20:22 ("he breathed on them and said … 'Receive the Holy Spirit'" — breath and Spirit together); 1Th 4:8.
- **Dwelling within:** "your body is a temple of the Holy Spirit within you" (1Co 6:19); "the Holy Spirit who dwells within us" (2Ti 1:14).
- **Into the heart:** "God's love has been poured into our hearts through the Holy Spirit" (Rom 5:5); "God, who knows the heart, bore witness to them, by giving them the Holy Spirit" (Act 15:8).
- **Speaking, testifying, teaching:**
  - Act 1:16; 4:25; 13:2; 20:23; 21:11; 28:25
  - Heb 3:7; 9:8; 10:15; Mar 12:36; 13:11 ("it is not you who speak, but the Holy Spirit"); Luk 12:12
  - Joh 14:26 ("bring to your remembrance"); 2Pe 1:21
- **Inner states in the Spirit:**
  - joy (Luk 10:21; Act 13:52; 1Th 1:6; Rom 14:17)
  - hope (Rom 15:13)
  - comfort (Act 9:31)
  - conviction (1Th 1:5)
  - conscience's witness (Rom 9:1)
- **Resisted or wronged:**
  - "you always resist the Holy Spirit" — "uncircumcised in heart" (Act 7:51)
  - "lie to the Holy Spirit" (Act 5:3)
  - "do not grieve the Holy Spirit of God" (Eph 4:30)
  - blasphemy (Mar 3:29; Mat 12:32; Luk 12:10)
  - OT: "they rebelled and grieved his Holy Spirit" (Isa 63:10); "take not your Holy Spirit from me" (Psa 51:11); "who put in the midst of them his Holy Spirit" (Isa 63:11)
- **Origin, anointing, baptism:** Mat 1:18, 20; Luk 1:35; 3:16, 22; Mat 3:11; Mar 1:8; Joh 1:33; Act 10:38; Mat 28:19; 2Co 13:14; Eph 1:13; Heb 2:4; 6:4; Tit 3:5; 1Co 12:3.
- **[D-attr] "the spirit of the holy gods is in you"** (Dan 4:8, 9, 18; 5:11) — a pagan king's attribution of Daniel's wisdom.
- [Claude reading] **Three relations to the human inner seat recur:**
  1. The Spirit **fills or dwells in** the person.
  2. The Spirit **enters the heart** (Rom 5:5; Act 15:8).
  3. The Spirit **can be grieved or resisted by** the person (Eph 4:30; Act 7:51).

  The Spirit is never said to be *in* the soul. The body is its temple (1Co 6:19) [observation, not a count].

### 7.2 Holiness of the human inner seat
- "may your whole spirit and soul and body be kept blameless" — "the God of peace himself sanctify you completely" (1Th 5:23) [H1] — **the one verse naming spirit, soul and body together**
- "cleanse ourselves from every defilement of body and spirit, bringing holiness to completion" (2Co 7:1) [H2]
- "how to be holy in body and spirit" (1Co 7:34) [H2]
- "establish your hearts blameless in holiness" (1Th 3:13)
- "in your hearts honor Christ the Lord as holy" (1Pe 3:15)
- "the hidden person of the heart with the imperishable beauty of a gentle and quiet spirit" (1Pe 3:4) [H1]
- **Sanctification by the Spirit [D]:** 1Pe 1:2; 2Th 2:13; Rom 15:16; 1Co 6:11; "has outraged the Spirit of grace" (Heb 10:29).
- **Holy flesh / body (NT):**
  - "reconciled in his body of flesh … to present you holy and blameless" (Col 1:22)
  - "present your bodies as a living sacrifice, holy … your spiritual worship" (Rom 12:1)
  - "a spiritual house, to be a holy priesthood" (1Pe 2:5)
- ◆ "the Spirit of holiness" (Rom 1:4) [U]; "you will not abandon my soul to Hades, or let your Holy One see corruption" (Act 2:27).

### 7.3 Inner purity vs ritual purity (see also §1.3–1.4, R3)
- **Heart and stomach:** "it enters not his heart but his stomach, and is expelled" (Mar 7:19) — beside "out of the heart … come evil thoughts" (Mar 7:21).
- **Flesh and conscience:** "sanctify for the purification of the flesh" (Heb 9:13) → "purify our conscience from dead works" (Heb 9:14).
- **Heart over rules of cleanness:** "who sets his heart to seek God … even though not according to the sanctuary's rules of cleanness" (2Ch 30:19).
- **Hands and hearts:** "Cleanse your hands, you sinners, and purify your hearts" (Jam 4:8); "clean hands and a pure heart" (Psa 24:4).
- **Souls purified by obedience:** "Having purified your souls by your obedience to the truth" (1Pe 1:22).
- **Defiled consciences:** "to the defiled … both their minds and their consciences are defiled" (Tit 1:15).
- **Stained flesh:** "hating even the garment stained by the flesh" (Jude 23).
- [Claude reading] **Ritual purity attaches to flesh, body and *nephesh*-as-person. Moral purity attaches to heart, spirit, soul and conscience. The NT texts deliberately move the vocabulary inward** (Mar 7:19–21; Heb 9:13–14; Act 15:9).

### 7.4 The OT inner seat and the holy
- **The high and holy with the lowly spirit:** "I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit, to revive the spirit of the lowly, and to revive the heart of the contrite" (Isa 57:15) [H1].
- **Heart glad in the holy name:** "our heart is glad in him, because we trust in his holy name" (Psa 33:21); "let the hearts of those who seek the Lord rejoice" (1Ch 16:10; Psa 105:3); "gladness of heart … when a holy feast is kept" (Isa 30:29).
- **Soul and flesh bless it:** "Bless the Lord, O my soul, and all that is within me, bless his holy name" (Psa 103:1); "let all flesh bless his holy name" (Psa 145:21).
- **Heart broken by the holy:** "My heart is broken within me; all my bones shake … because of the Lord and because of his holy words" (Jer 23:9).
- **Heart against the holy:** "his heart shall be set against the holy covenant" (Dan 11:28).
- **Fainting life reaches the holy temple:** "When my life was fainting away, I remembered the Lord, and my prayer came to you, into your holy temple" (Jon 2:7).
- **Heart and spirit give to the holy:** "everyone whose heart stirred him, and everyone whose spirit moved him … for the holy garments" (Exo 35:21) [H1]; "the money that a man's heart prompts him to bring" (2Ki 12:4).
- **Spirit of skill for consecration:** "the skillful, whom I have filled with a spirit of skill … to consecrate him" (Exo 28:3) [X].
- **God's heart in the consecrated house:** "My eyes and my heart will be there for all time" (1Ki 9:3; 2Ch 7:16).
- **The perfect law revives the soul:** "The law of the Lord is perfect, reviving the soul" (Psa 19:7).

### 7.5 Ritual holiness and the nephesh / flesh
- **Afflicting the *nephesh* on the holy day:** "a time of holy convocation, and you shall afflict yourselves [*your souls*]" (Lev 23:27; Num 29:7).
- **Consecrating oneself:** "Consecrate yourselves therefore, and be holy" (Lev 11:44); "Consecrate yourselves for tomorrow, and you shall eat meat" (Num 11:18).
- **Profaning soul cut off:** "Everyone who profanes it … that soul shall be cut off" (Exo 31:14); Lev 19:8; 22:3.
- **Holy flesh (sacrificial meat):** Exo 29:31, 34; Lev 6:27 ("Whatever touches its flesh shall be holy"); Hag 2:12 (holiness does not transfer).
- ◆ "Can even sacrificial flesh avert your doom?" (Jer 11:15)
- ◆ "Be silent, all flesh, before the Lord, for he has roused himself from his holy dwelling" (Zec 2:13)

---

## 8. Defilement (M10c)

### 8.1 Unclean spirits [O]
- **The Gospels, Acts and Revelation:** 23 verses. Mar 1:23, 26, 27; 3:11, 30; 5:2, 8, 13; 6:7; 7:25; 9:25; Luk 4:33, 36; 6:18; 8:29; 9:42; 11:24; Mat 10:1; 12:43; Act 5:16; 8:7; Rev 16:13; 18:2.
- **What they do:**
  - they **cry out** and **recognise** Jesus ("You are the Son of God", Mar 3:11)
  - they **convulse** (Mar 1:26; Luk 9:42) and **seize** and **drive** (Luk 8:29)
  - they are **mute and deaf** (Mar 9:25)
  - they **enter pigs** (Mar 5:13)
  - they **seek rest and return** to a person as "my house" (Mat 12:43; Luk 11:24)
  - they **obey** Jesus' command (Mar 1:27)
  - they **haunt** fallen Babylon (Rev 18:2)
- **Spirit of jealousy and defilement:** "if the spirit of jealousy comes over him and he is jealous of his wife who has defiled herself, or … though she has not defiled herself" (Num 5:14) [X]. The spirit of jealousy comes **whether or not** the defilement is real.
- [Claude reading] **"Unclean" is the dominant NT adjective for other-spirits**, and M10c is where they cluster. The human spirit is defiled only once (2Co 7:1, [H2]).

### 8.2 Nephesh = corpse — defilement by the dead (§0.8)
- "everyone who is unclean through contact with the dead [*a nephesh*]" (Num 5:2)
- "unclean through touching a dead body [*the nephesh of a man*]" (Num 9:6, 7, 10)
- "Whoever touches the dead body of any person" (Num 19:11, 13)
- "No one shall make himself unclean for the dead" (Lev 21:1); "He shall not go in to any dead bodies" (Lev 21:11); Lev 22:4; Hag 2:13
- "he sinned by reason of the dead body" (Num 6:11)
- [lexical; Claude reading] ◆ **The word for the living self is also the word for the body just vacated.** It defiles whoever touches it. This is the far end of *nephesh* = "person": the person as corpse.

### 8.3 The soul defiling itself
- "Ah, Lord God! Behold, I have never defiled myself [*my nephesh*] … nor has tainted meat come into my mouth" (Eze 4:14)
- "You shall not defile yourselves [*your souls*] with any swarming thing" (Lev 11:43–44; 20:25)
- "whatever the unclean person touches shall be unclean, and anyone [*the nephesh*] who touches it" (Num 19:22)
- **Resolved in the heart:** "Daniel resolved [*set on his heart*] that he would not defile himself with the king's food" (Dan 1:8).
- **The soul turning away in disgust after defilement:** "they defiled her with their whoring lust. And after she was defiled by them, she [*her nephesh*] turned from them in disgust" (Eze 23:17).
- **Hunger and defiled bread:** "all who eat of it shall be defiled; for their bread shall be for their hunger [*nephesh*] only" (Hos 9:4).

### 8.4 Flesh / body uncleanness
- **Leprosy:** "Raw flesh is unclean" (Lev 13:14, 15); Lev 13:3, 11.
- **Discharges:** Lev 15:2, 16, 19.
- **Washing:** Lev 15:7; Num 19:7, 8; Lev 22:6.
- **Animal flesh:** Lev 11:8; Deu 14:8; Lev 7:19, 21; "tainted meat" (Isa 65:4; Lev 7:18).

### 8.5 Inner defilement (NT)
- "God gave them up in the lusts of their hearts to impurity, to the dishonoring of their bodies" (Rom 1:24) — **heart-lust → bodily dishonour**
- "their conscience, being weak, is defiled" (1Co 8:7)
- "the works of the flesh … impurity" (Gal 5:19); "the lust of defiling passion" (2Pe 2:10); "members as slaves to impurity" (Rom 6:19)
- ◆ "his heart is busy with iniquity, to practice ungodliness … to leave the craving [*nephesh*] of the hungry unsatisfied" (Isa 32:6) — **a profane heart starves another's soul**

---

## 9. Pride and arrogance (M08)

### 9.1 The proud / lifted-up heart (*gāvah lēv*)
- "his heart was proud" (2Ch 32:25); "Hezekiah humbled himself for the pride of his heart" (2Ch 32:26)
- "when he was strong, he grew proud [*his heart was high*]" (2Ch 26:16, d0)
- **Tyre:**
  - "Because your heart is proud, and you have said, 'I am a god' … though you make your heart like the heart of a god" (Eze 28:2)
  - "your heart has become proud in your wealth" (Eze 28:5)
  - "Your heart was proud because of your beauty; you corrupted your wisdom" (Eze 28:17)
- **The tree:** "its heart was proud of its height" (Eze 31:10).
- **Moab:** "the pride of Moab … his loftiness, his pride, and his arrogance, and the haughtiness of his heart" (Jer 48:29) — five pride words around one heart.
- "The pride of your heart has deceived you" (Obd 3; Jer 49:16) — pride → self-deception (§4.3)
- "Before destruction a man's heart is haughty" (Pro 18:12); "Everyone who is arrogant in heart is an abomination" (Pro 16:5); "Haughty eyes and a proud heart" (Pro 21:4)
- "in pride and in arrogance of heart" (Isa 9:9); "the arrogant heart of the king of Assyria" (Isa 10:12)
- "who say in your heart, 'I am, and there is no one besides me'" (Isa 47:8)
- **Disclaimed:** "O Lord, my heart is not lifted up; my eyes are not raised too high" (Psa 131:1).
- **NT:**
  - "he has scattered the proud in the thoughts of their hearts" (Luk 1:51)
  - "God knows your hearts. For what is exalted among men is an abomination" (Luk 16:15)
  - "if you have bitter jealousy and selfish ambition in your hearts, do not boast" (Jam 3:14)
- ◆ **Same idiom, good sense:** "His heart was courageous [*lifted up*] in the ways of the Lord" (2Ch 17:6) [lexical]. The verb *gāvah* "be high" names pride in Hezekiah and courage in Jehoshaphat. **The height of the heart is judged by where it is lifted: toward the ways of the Lord, or toward itself.**
- [Claude reading] **Pride is primarily "a high heart", and is typically occasioned by strength, wealth or beauty** (2Ch 26:16; Eze 28:5, 17). Its speech is the heart's self-declaration ("I am a god", "I am, and there is no one besides me").

### 9.2 The proud and the lowly spirit
- "Pride goes before destruction, and a haughty spirit before a fall" (Pro 16:18) [H1]
- "the patient in spirit is better than the proud in spirit" (Ecc 7:8) [H1]
- "One's pride will bring him low, but he who is lowly in spirit will obtain honor" (Pro 29:23) [H1]
- "It is better to be of a lowly spirit with the poor than to divide the spoil with the proud" (Pro 16:19) [H1]
- "when his heart was lifted up and his spirit was hardened so that he dealt proudly, he was brought down" (Dan 5:20) [H1] — **heart lifted, spirit hardened**, then Dan 5:22 "you … have not humbled your heart" (§10)
- [Claude reading] **Pride and lowliness are predicated of the human spirit as freely as of the heart.** Here the spirit is the *carriage* of the person, high or low. This is one of the most concentrated human-spirit groups in the batch.

### 9.3 Soul and boasting
- **Good boast:** "My soul makes its boast in the Lord; let the humble hear and be glad" (Psa 34:2).
- **Bad boast:** "the wicked boasts of the desires of his soul" (Psa 10:3).
- **The soul wearied by the proud:** "Our soul has had more than enough of the scorn of those who are at ease, of the contempt of the proud" (Psa 123:4).
- ◆ **Weeping in secret for another's pride:** "my soul will weep in secret for your pride" (Jer 13:17).
- **God swears by his soul against pride:** "The Lord God has sworn by himself [*his nephesh*] … 'I abhor the pride of Jacob'" (Amo 6:8) [lexical].
- **Emboldened soul:** "my strength of soul you increased" (Psa 138:3) — *rāhav* "be bold / assertive" [lexical]; pride's vocabulary used as a gift.
- **Wide soul = greed:** "A greedy man [*wide of soul*] stirs up strife" (Pro 28:25); "an arrogant man … His greed is as wide as Sheol" (Hab 2:5) [lexical].
- **The soul's yearning taken away:** "the pride of your power, the delight of your eyes, and the yearning of your soul" (Eze 24:21).
- **Insolent men seek the life:** "insolent men have risen up against me; a band of ruthless men seeks my life" (Psa 86:14).

### 9.4 Flesh, boasting and the Spirit (NT)
- "so that no human being [*flesh*] might boast in the presence of God" (1Co 1:29)
- "Since many boast according to the flesh, I too will boast" (2Co 11:18)
- "that they may boast in your flesh" (Gal 6:13)
- "we are the circumcision, who worship by the Spirit of God and glory in Christ Jesus and put no confidence in the flesh" (Phili 3:3) [D1]
- "the desires of the flesh and the desires of the eyes and pride of life" (1Jo 2:16)
- "speaking loud boasts of folly, they entice by sensual passions of the flesh" (2Pe 2:18)
- "puffed up without reason by his sensuous [*fleshly*] mind" (Col 2:18)
- ◆ **The thorn in the flesh against conceit:** "to keep me from becoming conceited … a thorn was given me in the flesh, a messenger of Satan to harass me" (2Co 12:7).
- **Conscience as the proper boast:** "our boast is this, the testimony of our conscience" (2Co 1:12).
- **Heart vs appearance:** "those who boast about outward appearance and not about what is in the heart" (2Co 5:12).
- [Claude reading] **In the NT, boasting "in the flesh" = confidence in outward standing.** It is set against worship "by the Spirit" (Phili 3:3) and against what is "in the heart" (2Co 5:12).

### 9.5 ◆ Fringe
- "man looks on the outward appearance [*height of stature*], but the Lord looks on the heart" (1Sa 16:7)
- "As the heavens for height … so the heart of kings is unsearchable" (Pro 25:3) — height as depth
- "I know your presumption and the evil of your heart" (1Sa 17:28) — pride attributed to David's heart by his brother, **wrongly**; a misreading of another's heart
- "Zebulun is a people who risked [*despised*] their lives to the death" (Judg 5:18) — the *nephesh* held cheap for a cause (R10)
- "my heart does not reproach me for any of my days" (Job 27:6) — the heart as internal accuser, silent (cf. §3.3 2Sa 24:10)
- "Be wise, my son, and make my heart glad, that I may answer him who reproaches me" (Pro 27:11)
- "the Spirit is poured upon us from on high" (Isa 32:15) [D2] — divine height

---

## 10. Humility and lowliness (M09)

### 10.1 The humbled heart
- **Humbling oneself:**
  - "Hezekiah humbled himself for the pride of his heart" (2Ch 32:26)
  - "because your heart was tender [*penitent*] and you humbled yourself before God when you heard his words … and wept before me, I also have heard you" (2Ch 34:27; 2Ki 22:19) — **tender heart → humbled self → heard**
  - "if then their uncircumcised heart is humbled" (Lev 26:41)
- **Failing to:** "you his son, Belshazzar, have not humbled your heart, though you knew all this" (Dan 5:22) — knowledge without humbling.
- **God humbles:** "he bowed their hearts down with hard labor" (Psa 107:12).
- [Claude reading] **Humbling is something done to or by the heart after hearing** (2Ch 34:27) **or after knowing** (Dan 5:22). Knowing is not enough.

### 10.2 The lowly / poor spirit
- "Blessed are the poor in spirit" (Mat 5:3) [H1]
- "he who is lowly in spirit will obtain honor" (Pro 29:23) [H1]
- "It is better to be of a lowly spirit with the poor" (Pro 16:19) [H1]
- "a contrite and lowly spirit … to revive the spirit of the lowly" (Isa 57:15) [H1]
- "I am gentle and lowly in heart, and you will find rest for your souls" (Mat 11:29) — **lowly heart (Jesus) → rest for souls (disciples)**
- **Humble hearts revive:** "When the humble see it they will be glad; you who seek God, let your hearts revive" (Psa 69:32); "The afflicted shall eat and be satisfied … May your hearts live forever!" (Psa 22:26).
- **The afflicted heart strengthened:** "O Lord, you hear the desire of the afflicted; you will strengthen their heart" (Psa 10:17).

### 10.3 Poverty, need and the inner seat (R6)
- **The needy heart:**
  - "For I am poor and needy, and my heart is stricken within me" (Psa 109:22)
  - "he … pursued the poor and needy and the brokenhearted, to put them to death" (Psa 109:16)
- **The Spirit's mission to the poor and brokenhearted [D1]:**
  - "The Spirit of the Lord God is upon me, because the Lord has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted" (Isa 61:1)
  - "The Spirit of the Lord is upon me … to proclaim good news to the poor" (Luk 4:18)
- **The heart toward the poor:** "you shall not harden your heart or shut your hand against your poor brother" (Deu 15:7).
- **The soul grieved for them:** "Was not my soul grieved for the needy?" (Job 30:25).
- **God saves the needy's life:**
  - "saves the lives of the needy" (Psa 72:13)
  - "he has delivered the life of the needy from the hand of evildoers" (Jer 20:13)
  - "to save him from those who condemn his soul to death" (Psa 109:31)
- **Equal ransom:** "the rich shall not give more, and the poor shall not give less … to make atonement for your lives" (Exo 30:15) — **every nephesh ransomed at the same price**.
- **Breath:** "the breath of the ruthless is like a storm against a wall" (Isa 25:4); "with the breath of his lips he shall kill the wicked" — beside "equity for the meek" (Isa 11:4).

### 10.4 Willing heart and willing spirit (R4)
- "Whoever is of a generous heart" (Exo 35:5); "all who were of a willing heart" (Exo 35:22; 2Ch 29:31)
- "uphold me with a willing spirit" (Psa 51:12) [H1]

### 10.5 ◆ Fringe
- **False humility and the flesh:**
  - "asceticism and severity to the body, but they are of no value in stopping the indulgence of the flesh" (Col 2:23)
  - "insisting on asceticism … puffed up … by his sensuous mind" (Col 2:18)
  - [Claude reading] **Humility can be performed by the flesh and remain pride** (Col 2:18 has both "asceticism" and "puffed up").
- **The spirit returns:** "her spirit returned, and she got up at once" (Luk 8:55) [H1] — the human spirit as life-principle (the "directed" tag is a misfile, R5).
- **Inner speech of the servant:** "if that servant says to himself [*in his heart*], 'My master is delayed'" (Mat 24:48; Luk 12:45) — the heart's private conclusion licenses abuse. Cf. "said in heart" (depiction v1 §2.1c).
- **"Strengthen your heart" = eat** (Judg 19:5, 8) — the heart fed with bread.

---

## 11. Cross-cutting observations for Batch D [Claude reading]

1. **Moral condition is predicated above all of the heart.** The heart is:
   - upright, whole, pure, clean or blameless (§1)
   - evil, crooked, perverse, twisted, false or double (§2, §4, §5)
   - proud / high or humbled / tender (§9, §10)

   It is also where sin is stored, engraved or hidden (§3.3). God tests and weighs it (Psa 7:9; Pro 21:2; Luk 16:15; Act 15:8). **The heart is the organ that is morally evaluated.**
2. **The soul (*nephesh*) is the accountable person and the life at stake.**
   - It sins, realises guilt, bears iniquity and is cut off (§3.1). It is the unfaithful party (§5).
   - It is the life that righteousness delivers (§1.7) and that sin injures (§3.2).
   - It is the innocent blood that is shed (§1.7). It is afflicted on holy days (§7.5).
   - At the limit it is the corpse that defiles (§8.2).

   **The soul is less often *evaluated* (righteous soul: 2Pe 2:8; puffed-up soul: Hab 2:4) than *answerable*.**
3. **The human spirit is evaluated chiefly on the pride–humility axis** (§9.2, §10.2): haughty, proud, hardened, lowly, poor, contrite. Otherwise it is:
   - without deceit (Psa 32:2)
   - right / clean (Psa 51:10)
   - faithful in marriage (Mal 2:15–16)
   - trustworthy (Pro 11:13)
   - holy or defiled with the body (1Co 7:34; 2Co 7:1)
   - sanctified with soul and body (1Th 5:23)
   - perfected in the righteous dead (Heb 12:23)
   - weighed (Pro 16:2)
   - broken by a perverse tongue (Pro 15:4)

   [observation, not a count]
4. **Other spirits carry the negative moral adjectives.** They are evil / harmful (§2.1, 15 verses), unclean (§8.1, 23 verses) and lying / deceitful (§4.1, 6 verses). They are the moral clusters' names turned into kinds of spirit.
   - In the OT some are **sent by God** (1Sa 16; Judg 9:23; 1Ki 22:22–23).
   - In the NT they **indwell and are cast out**.

   **The Holy Spirit is the positive counterpart, and the one against whom human sin is directed:** blasphemed, lied to, grieved, resisted, outraged (§2.4, §4.2, §7.1).
5. **Inner vs outer purity.**
   - Ritual clean / unclean / holy vocabulary attaches to flesh, body and *nephesh*-as-person or corpse.
   - Moral purity attaches to heart, spirit, soul and conscience.
   - Several texts deliberately contrast the two: Psa 24:4; 2Ch 30:19; Mar 7:19–21; Heb 9:13–14; 10:22; Jam 4:8.
6. **Conscience is the NT's named moral-awareness faculty.** It can be clear, pure, good, evil, defiled, seared, weak or wounded. It testifies (2Co 1:12; Rom 9:1) and is purified by Christ's blood (Heb 9:14). It is frequently paired with the heart (1Ti 1:5; Heb 10:22).
   - The OT does this work with the heart: "David's heart struck him" (2Sa 24:10); "my heart does not reproach me" (Job 27:6).
   - The Levitical "realizes his guilt" (Lev 5) describes the same moment without naming an organ.
7. **The heart deceives itself and is the source of evil.**
   - It deceives its owner: Jer 17:9; Obd 3; Isa 44:20.
   - Evil comes from it: Gen 6:5; Mat 15:19; Luk 6:45.
   - Its evil hides behind speech: Psa 28:3; 41:6; Pro 26:23–25.
   - Pride deceives the heart that holds it (Obd 3), linking M08 and M14.
8. **Flesh carries on from Batch C (§11.5).**
   - OT: flesh is the ritual body and meat — clean or unclean, holy or tainted.
   - NT Pauline: flesh is the seat of sin (Rom 7–8; Gal 5:19) and the ground of false boasting (Phili 3:3).
   - Positive NT uses remain: "holy … in his body of flesh" (Col 1:22); "bodies as a living sacrifice" (Rom 12:1).
9. **Wind and breath are the image of moral emptiness:**
   - iniquity takes us away like wind (Isa 64:6)
   - the wicked are chaff (Psa 1:4)
   - "wind and lies" (Mic 2:11)
   - idols with no breath (Jer 10:14)
   - the *hevel* + *rûaḥ* refrain (Ecc)

   Only the messianic "breath of his lips" (Isa 11:4) and the breath that conveys the Holy Spirit (Joh 20:22) are active and effective.
10. ◆ **Fringe worth keeping:**
    - *nephesh* = corpse as the defiling body (§8.2)
    - the "high heart" that is pride or courage depending on direction (2Ch 17:6 vs 2Ch 32:25)
    - the heart that strikes or does not reproach — pre-conscience (§3.3, §9.5)
    - sin against one's own soul (§3.2)
    - the servant's soul as guilt offering (§3.6)
    - lies that kill and keep alive souls (Eze 13:19)
    - the spirit of jealousy that comes whether or not the defilement is real (Num 5:14)
    - false humility of the flesh (Col 2:18, 23)
    - the thorn in the flesh against conceit (2Co 12:7)
    - Eliab misreading David's heart (1Sa 17:28)
    - "Is your heart true to my heart as mine is to yours?" (2Ki 10:15)

---

## 12. Next

- **Batch E** (relating to God): M13, M31, M19, M36, M22, M49, M42 (report the "declares the Lord" pre-filter; "speak" verbs per B R1), M21, M54, M44, M32, M35, M60, M50, M79, M59, M45, M80, M39. "Said in heart" (H0559) is not in the pairs file; see handoff v2 §4.
- Researcher rulings R1–R10 are set out in **§R**, with a blank "Ruling" row each. Once they are ruled, the membership changes go to the relevant clusters' analysis.
- Candidate receiving clusters are affected by R3 (M61, M10c), R4 (M64), R6 (M46), R8 (M73, M26) and R10 (M53). Those clusters' own batch files should pick up the incoming Strong's when they are analysed.
