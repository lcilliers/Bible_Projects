# M47 × Knowing / Thinking / Speaking / Hearing — Batch B (v2)

**Date:** 2026-09-27
**Supersedes:** v1 (same date; `archive/`). v2 adds §R (items for researcher ruling) and §X (cluster cross-reference), with DB assignment sources. It also **corrects §0.2** on where the speech verbs sit. The analysis in §1–§9 is otherwise unchanged.
**Use:** this file is meant to accompany the analysis of each cluster listed below. Start at §X to find the sections and flagged Strong's for your cluster.
**Data:** `cluster-M47-other-m-code-pairs-with-distance-20260927.csv` — pairs where the other word is in:
- M15 Knowing & Understanding
- M16 Wisdom & Folly
- M41 Being Heard
- M43 Prophecy & Vision
- M63 Reasoning & Interpretation
- M65 Speech & Tongue
- M81 Memory (act)
- M82 Reminder & Report

**1,338 pairs in 765 verses; all read.**

**Spirit classes** (`M47-spirit-distinction-v1-20260927.md`):
- **[D1/D2]** divine
- **[D3]** divine per ESV only
- **[H]** human
- **[O]** other being
- **[X]** disposition
- **[T]** temper
- **[U]** not determinable

Tags: **[Claude reading]**, **[lexical]**, **[verify]**, ◆ fringe. Not statistical.

**Assignment source.** Cluster membership is from `iba/app/db/iba.db` → `cluster_strong` (active rows, read-only query, 2026-09-27). "Source" is the assignment route recorded there:
- `old-system-migration` — carried over; no confidence recorded
- `heuristic-family-grouping-v1-20260905` — family heuristic
- `llm-allocation-v1_3-20260811` — LLM allocation, with a confidence value
- `auto-precedent`

---

## R. Items for researcher ruling

Four decisions are needed.
- **R1, R3 and R4** are **cluster-membership** questions for `cluster_strong`.
- **R2** is a **scope** question for Batch E.
- The process question (whether to record misfiles beyond the write-ups) is **Batch A R7** and applies here too.
- Nothing has been changed in the DB.
- "Pairs / verses" counts are for the whole pairs file.

### R1 — Speech verbs H1696G, H1696I, H0981 in M42 Prayer & Petition
| | |
|---|---|
| **Cluster(s)** | M42 (current); M65 Speech & Tongue (candidate) |
| **Strong's** | H1696G *dibbēr* "to speak" · H1696I "to speak: promise" · H0981 *bāṭāʾ* "to speak rashly" |
| **DB now** | All three: M42 · `llm-allocation-v1_3-20260811` · **low** · rationale "operation → M42 (kw:speak)" · **review_flag = 1 already set** |
| **Evidence** | H1696G: 132 pairs / 105 verses. Surfaces: said, say, speak, spoke, decree, entreated, even a name (Adonijah). H0981: "spoke rashly with his lips" (Psa 106:33). Almost all are ordinary speech, not prayer. |
| **Issue** | M65's description is "Speaking, the mouth/tongue/lips, declaring, telling". The M42 assignment came from a keyword, at low confidence, and is already flagged for review. |
| **Options** | (a) keep M42; (b) move all three to M65; (c) move to M65 and keep an M42 alternative for the "entreated / pleaded" uses. |
| **Recommendation** | **(c)** [Claude reading]. |
| **Ruling** | ______ |

### R2 — "Said in his heart": H0559 "to say" is not in the M-code pairs file
| | |
|---|---|
| **Cluster(s)** | T3 Operations (current); affects Batch E (M42) and the M47 depiction |
| **Strong's** | H0559 *ʾāmar* "to say" |
| **DB now** | **T3** · `llm-allocation-v1_3-20260811` · low · "operation, cluster undetermined → T3" · review_flag = 1 |
| **Correction to v1** | v1 §0.2 said H0559 and H1696 are filed under M42, and that the "said in his heart" series would come up in Batch E. **Only H1696 is in M42 (R1). H0559 is in T3**, so it is not in the M-code pairs file at all. Checked: 1Sa 27:1 and Psa 14:1 have no "said" pair in the file. **Batch E will not contain the H0559 "said in heart" series.** |
| **Options** | (a) read the "said in heart" series in Batch E from depiction v1 §2.1c (already done, full verse read), with no new export; (b) request a re-export that includes T3 pairs for H0559 only; (c) treat it as out of scope for the cross-cluster batches. |
| **Recommendation** | **(a)**. It costs nothing new, and the verses are already read. Only (b) would add distance data. |
| **Ruling** | ______ |

### R3 — G0746 *archē* "beginning / authorities / firstfruits" in M16 Wisdom & Folly
| | |
|---|---|
| **Cluster(s)** | M16 (current); M72 Authority & Dominion (candidate) |
| **Strong's** | G0746 *archē* "beginning, rule, ruler" |
| **DB now** | M16 · `old-system-migration` · rationale "relocated M17 → M16 2026-09-06 (escalation #1525: merge M17 into M16)" |
| **Evidence** | 6 pairs / 4 verses. Surfaces: beginning, authorities, firstfruits. None is about wisdom. |
| **Issue** | The word came into M16 through the M17 merge, not on its own sense. Its senses are "beginning" (time) and "rule / authorities" (M72). |
| **Options** | (a) keep M16; (b) move to M72; (c) move to a T-bucket (no inner-being significance); (d) M72 plus T-bucket. |
| **Recommendation** | **(b) M72** for the "rule / authorities" sense [Claude reading]. |
| **Ruling** | ______ |

### R4 — H1697I "word: thing" in M65 Speech & Tongue
| | |
|---|---|
| **Cluster(s)** | M65 (current) |
| **Strong's** | H1697I *dāvār* in the sense "thing, matter" |
| **DB now** | M65 · `heuristic-family-grouping-v1-20260905` · heuristic · "family=speech-mouth-tongue" |
| **Evidence** | 32 pairs / 25 verses. Surfaces: thing, things, anything, nothing, some, business, it, one, "regard to", theme. |
| **Issue** | The sub-entry is the **non-speech** sense of *dāvār*. It was grouped with speech by family (because *dāvār* also means "word"). |
| **Options** | (a) keep M65; (b) remove M65 and move to a T-bucket (no inner-being significance). |
| **Recommendation** | **(b)**. |
| **Ruling** | ______ |

---

## X. Cluster cross-reference — where each cluster appears in this file

Use this when the file accompanies a cluster's analysis. "Tag-level" means the source tagged the wrong word or sense in that verse; the cluster assignment itself is not questioned.

| Cluster | Sections | Flagged Strong's (DB source · confidence) |
|---|---|---|
| **M15** Knowing & Understanding | §1; §1.2 "set the heart"; §0.1 | H7760K (auto-precedent), H7896K (old-system) "set: consider" — fits; no ruling. Sense-level: H3045 sexual "know" (Num 31:35; Judg 19:22). Tag-level: H4609A "thought" at Psa 131:1 "Ascents" (LLM · high). |
| **M16** Wisdom & Folly | §2 | **R3** G0746 (old-system, via M17 merge). Tag-level: H8454 "wisdom" at Job 30:22 "toss" (heuristic; Kethiv/Qere [verify]). |
| **M41** Being Heard | §3 | — |
| **M65** Speech & Tongue | §4 | **R4** H1697I (heuristic) |
| **M81** Memory (act) | §5 | — |
| **M82** Reminder & Report | §5 | — |
| **M43** Prophecy & Vision | §6 | — |
| **M63** Reasoning & Interpretation | §7 | — |
| **M42** Prayer & Petition (not a Batch B cluster) | §0.2 | **R1** H1696G, H1696I, H0981 (LLM · low · already review-flagged) |
| **T3** Operations | §0.2 | **R2** H0559 "to say" (LLM · low · review-flagged) — not in the pairs file |
| **M47** Inner Seat | all; §8 *psychikos / pneumatikos*; §9 | — |
| Candidate receiving clusters | M65 (R1); M72 (R3) | — |

---

## 0. Data notes

1. **"Set the heart" is a single idiom** (H7760K / H7896K "to set: consider", often at **d0**, i.e. the same token as *lēv*).
   - It is behind "consider" (Hag 1:5, 7; 2:15, 18; Job 1:8; 2:3; Pro 24:32), "care" (2Sa 18:3), "pay attention" (1Sa 4:20), "mark well" (Eze 44:5) and "take to heart" (2Sa 13:20; Exo 7:23; Isa 42:25; Mal 2:2).
   - [Claude reading] **Attention and consideration are expressed as *placing the heart*.**
2. **Speech verbs are elsewhere.** *(Corrected in v2.)* "Speak" (H1696G/I) and "speak rashly" (H0981) are filed under **M42 Prayer & Petition** (**→ Ruling R1**). "Say" (H0559) is in **T3 Operations**, so it is **not in the pairs file at all** (**→ Ruling R2**). So the "said in his heart" series (depiction v1 §2.1c) is not in this batch, and it will **not** appear in Batch E either. M65 here holds mainly "word / tell / thing".
3. **Noise, noted and not used:**
   - "Ascents" tagged as thought (Psa 131:1)
   - "toss" tagged as wisdom (Job 30:22)
   - G0746 "beginning / authorities / firstfruits" filed under Wisdom
   - sexual "know" (Num 31:35; Judg 19:22)
   - H1697I "thing / nothing / some" (generic)
4. **G5591 "natural" is *psychikos*,** the adjective of *psychē* ("soul-ish") [lexical]. It appears here in contrast to "spiritual" (*pneumatikos*). See §8.
5. **The brief's [verify] is resolved.** 1 Kgs 3:9 "an understanding mind" carries **H3820A (lēv) + H8085J "to hear: understand"**, at distance 1. The "hearing heart" is tagged in the data exactly as the brief supposed.

---

## 1. Knowing and understanding (M15)

### 1.1 The heart as the knower
- "Your heart knows that many times you yourself have cursed others" (Ecc 7:22)
- "You know in your own heart all the harm that you did" (1Ki 2:44, d0)
- "you know in your hearts and souls … that not one word has failed" (Jos 23:14)
- "Know then in your heart …" (Deu 8:5); "know therefore today, and lay it to your heart, that the Lord is God" (Deu 4:39)
- "The heart knows its own bitterness" (Pro 14:10)
- [Claude reading] "Knowing in the heart" is inner certainty and self-knowledge, not only information.

### 1.2 Attention — setting the heart (see §0.1)
- "Consider your ways" = set your heart on your ways.
- "set your heart to understand" (Dan 10:12)
- "apply my heart to know wisdom" (Ecc 1:17; 7:25; 8:16)
- "Take to heart all the words" (Deu 32:46)
- The failure case: "it burned him up, but he did not take it to heart" (Isa 42:25).

### 1.3 Understanding given, withheld or blocked
- **Given by God:**
  - "I will give them a heart to know me" (Jer 24:7)
  - "I give you a wise and discerning mind [heart]" (1Ki 3:12)
  - "Who has put wisdom in the inward parts or given understanding to the mind?" (Job 38:36)
  - "God … has shone in our hearts to give the light of the knowledge" (2Co 4:6)
  - "having the eyes of your hearts enlightened, that you may know" (Eph 1:18)
- **Withheld:** "the Lord has not given you a heart to understand or eyes to see or ears to hear" (Deu 29:4).
- **Blocked:**
  - "Make the heart of this people dull … lest they … understand with their hearts" (Isa 6:10; Mat 13:15; Joh 12:40; Act 28:27)
  - "he has shut … their hearts, so that they cannot understand" (Isa 44:18); "you have closed their hearts to understanding" (Job 17:4)
  - "they did not understand about the loaves, but their hearts were hardened" (Mar 6:52; 8:17)
  - "futile in their thinking, and their foolish hearts were darkened" (Rom 1:21); "darkened in their understanding … due to their hardness of heart" (Eph 4:18)
- [Claude reading] **Hardness of heart and failure to understand are the same event seen from two sides.**

### 1.4 God knows, tests and searches the heart
- "you, you only, know the hearts of all the children of mankind" (1Ki 8:39; 2Ch 6:30)
- "he knows the secrets of the heart" (Psa 44:21); "God knows your hearts" (Luk 16:15)
- "Search me, O God, and know my heart! Try me and know my thoughts!" (Psa 139:23)
- "he who searches mind and heart" (Rev 2:23)
- "testing you to know what was in your heart" (Deu 8:2; 2Ch 32:31; Deu 13:3 "with all your heart and with all your soul")
- **Heart and soul together:** "does not he who weighs the heart perceive it? Does not he who keeps watch over your soul know it?" (Pro 24:12)
- ◆ "The heart is deceitful above all things … who can understand it?" (Jer 17:9) — the heart is opaque even to its owner.

### 1.5 The soul in knowing
- "my soul knows it very well" (Psa 139:14)
- "knowledge will be pleasant to your soul" (Pro 2:10); "wisdom is such to your soul" (Pro 24:14); "Whoever gets sense loves his own soul" (Pro 19:8)
- "take counsel in my soul" (Psa 13:2)
- In the NT, psychē is rendered "minds" (Act 14:2 "poisoned their minds"; 15:24 "unsettling your minds").
- [Claude reading] The soul *receives* knowledge as something pleasant or nourishing, rather than being the one who investigates.
- ◆ **Desire ahead of knowledge:**
  - "Desire [nephesh] without knowledge is not good" (Pro 19:2)
  - "The dogs have a mighty appetite; they never have enough. But they are shepherds who have no understanding" (Isa 56:11)
  - "Before I was aware, my desire [nephesh] set me among the chariots" (Song 6:12) — the soul's desire acts before awareness

### 1.6 The human spirit in knowing [H]
- **Self-knowledge:** "who knows a person's thoughts except the spirit of that person, which is in him?" (1Co 2:11) [H1+D1].
- **Understanding as God's breath in man:** "it is the spirit in man, the breath of the Almighty, that makes him understand" (Job 32:8).
- "out of my understanding a spirit answers me" (Job 20:3).
- **A cool spirit = understanding:** "he who has a cool spirit is a man of understanding" (Pro 17:27); "slow to anger has great understanding, but … a hasty temper exalts folly" (Pro 14:29) [T].
- "those who go astray in spirit will come to understanding" (Isa 29:24).
- ◆ **Inner inquiry in sequence:** "let me meditate in my heart.' Then my spirit made a diligent search" (Psa 77:6). The heart meditates, then the spirit searches.
- **Spirit vs mind (nous):**
  - "my spirit prays but my mind is unfruitful … I will pray with my spirit, but I will pray with my mind also" (1Co 14:14–15)
  - "be renewed in the spirit of your minds" (Eph 4:23)
- **Perceiving others' inner reasoning:** "Jesus, perceiving in his spirit that they thus questioned within themselves" (Mar 2:8).

### 1.7 God's Spirit as the source of knowledge [D]
- "the Spirit of wisdom and understanding … of knowledge and the fear of the Lord" (Isa 11:2)
- "filled him with the Spirit of God, with ability and intelligence, with knowledge and all craftsmanship" (Exo 31:3; 35:31)
- "through the Spirit the utterance of wisdom … of knowledge" (1Co 12:8)
- "the Spirit searches everything … the natural person does not accept the things of the Spirit … they are spiritually discerned" (1Co 2:10–14)
- "the Holy Spirit will teach you" (Luk 12:12; Joh 14:26)
- "we do not know what to pray for … but the Spirit himself intercedes" (Rom 8:26); "he who searches hearts knows what is the mind of the Spirit" (Rom 8:27)
- ◆ **The Spirit and the heart's reasoning, together:** "it has seemed good to the Holy Spirit and to us" (Act 15:28).

### 1.8 Flesh as a way of knowing
- "we regard no one according to the flesh. Even though we once regarded Christ according to the flesh" (2Co 5:16)
- "set their minds on the things of the flesh … the Spirit" (Rom 8:5) [D3]
- "the desires of the flesh and the mind" (Eph 2:3)
- "his sensuous mind [mind of flesh]" (Col 2:18)
- "I myself serve the law of God with my mind, but with my flesh …" (Rom 7:25)
- **Contrast:** "flesh and blood has not revealed this to you, but my Father" (Mat 16:17).
- **"All flesh" as knowing humanity:** "all flesh shall know that I am the Lord" (Eze 21:5; Isa 49:26).

### 1.9 Conscience and knowledge
- "not all possess this knowledge … their conscience, being weak, is defiled" (1Co 8:7, 10) — knowledge shapes the conscience.
- "both their minds and their consciences are defiled" (Tit 1:15).
- "their conscience also bears witness, and their conflicting thoughts accuse or even excuse them" (Rom 2:15).

### 1.10 Heart and mind (nous / dianoia) side by side
- "put my laws into their minds, and write them on their hearts" / "on their hearts … on their minds" (Heb 8:10 / 10:16)
- "guard your hearts and your minds" (Phili 4:7)
- The love command lists heart, soul, mind and strength **as separate items** (Mar 12:30; Mat 22:37; Luk 10:27)
- "evil thoughts [reasonings]" come "out of the heart" (Mat 15:19; Mar 7:21); "the reasoning of their hearts" (Luk 9:47)
- ◆ **Soul pierced, heart revealed:** "a sword will pierce through your own soul also, so that thoughts from many hearts may be revealed" (Luk 2:35).

### 1.11 ◆ Breath, wind and thought
- "When his breath departs … on that very day his plans perish" (Psa 146:4) — the brief's thought link
- "he who … creates the wind, and declares to man what is his thought" (Amo 4:13)
- "windy knowledge" (Job 15:2)
- "I applied my heart to know wisdom … this also is but a striving after wind" (Ecc 1:17)
- "Every man is stupid and without knowledge … there is no breath in them" (Jer 10:14; 51:17)

---

## 2. Wisdom and folly (M16)

### 2.1 "Wise of heart" = skilled ◆
- "every skillful craftsman" = *wise of heart* (Exo 35:10, 25; 36:1, 2, 8; 31:6, d0)
- "whom I have filled with a spirit of skill" (Exo 28:3) [X]
- "every craftsman in whose mind [heart] the Lord had put skill, everyone whose heart stirred him up" (Exo 36:2)
- "whose hearts stirred them to use their skill" (Exo 35:26)
- [Claude reading] Wisdom in the heart includes **craft skill**. God puts it there, and the stirred heart puts it to work.

### 2.2 The heart's direction decides wise or foolish
- "A wise man's heart inclines him to the right, but a fool's heart to the left" (Ecc 10:2)
- "The heart of the wise is in the house of mourning" (Ecc 7:4)
- "The heart of the wise makes his speech judicious" (Pro 16:23); "The wise of heart will receive commandments" (Pro 10:8)
- "The fool says in his heart, 'There is no God'" (Psa 14:1; 53:1)
- "Folly is bound up in the heart of a child, but the rod of discipline drives it far from him" (Pro 22:15) — ◆ folly located *in* the heart and removable from outside
- "Whoever trusts in his own mind [heart] is a fool" (Pro 28:26); "Trust in the Lord with all your heart, and do not lean on your own understanding" (Pro 3:5)

### 2.3 Wisdom going wrong through the heart
- "your wisdom and your knowledge led you astray, and you said in your heart, 'I am'" (Isa 47:10)
- "Your heart was proud … you corrupted your wisdom" (Eze 28:17)
- "by your great wisdom … your heart has become proud" (Eze 28:5)
- "oppression drives the wise into madness, and a bribe corrupts the heart" (Ecc 7:7)

### 2.4 Wisdom entering and staying
- "wisdom will come into your heart" (Pro 2:10); "Wisdom rests in the heart of a man of understanding" (Pro 14:33)
- "teach us to number our days that we may get a heart of wisdom" (Psa 90:12)
- ◆ "I searched with my heart how to cheer my body with wine — my heart still guiding me with wisdom" (Ecc 2:3) — the heart guiding the body's experiment

### 2.5 Spirit and wisdom
- **Transmitted:** "full of the spirit of wisdom, for Moses had laid his hands on him" (Deu 34:9) [X].
- **Divine:** "the Spirit of wisdom" (Isa 11:2) [D1]; "full of the Spirit and of wisdom" (Act 6:3, 10) [D2]; "words … taught by the Spirit," not human wisdom (1Co 2:13) [D2].
- **Human spirit, fool vs wise:** "A fool gives full vent to his spirit, but a wise man quietly holds it back" (Pro 29:11) [H].
- **Foolish prophets:** "who follow their own spirit" (Eze 13:3) [H]; "the man of the spirit is mad" (Hos 9:7) [U].

### 2.6 Counsel and plans
- "take counsel in my soul" (Psa 13:2)
- "gave them over to their stubborn hearts, to follow their own counsels" (Psa 81:12; Jer 7:24)
- "Many are the plans in the mind [heart] of a man, but it is the purpose of the Lord that will stand" (Pro 19:21)
- "The purpose in a man's heart is like deep water" (Pro 20:5)
- "The counsel of the Lord stands forever, the plans of his heart" (Psa 33:11) — God's heart plans
- ◆ **Plans without the Spirit:** "who carry out a plan, but not mine, and who make an alliance, but not of my Spirit" (Isa 30:1) [D1]
- ◆ **Spirit emptied, counsel confounded:** "the spirit of the Egyptians within them will be emptied out, and I will confound their counsel" (Isa 19:3) [H]

### 2.7 Flesh, soul and folly
- "not many of you were wise according to worldly standards [flesh]" (1Co 1:26)
- "an appearance of wisdom … of no value in stopping the indulgence of the flesh" (Col 2:23)
- ◆ "The fool folds his hands and eats his own flesh" (Ecc 4:5)
- "Fool! This night your soul is required of you" (Luk 12:20)
- "his lips are a snare to his soul" (Pro 18:7)

---

## 3. Hearing (M41) — the brief's open question

### 3.1 The ear receives, the heart keeps or understands
- "all my words … receive in your heart, and hear with your ears" (Eze 3:10)
- "hear with your ears, and set your heart upon all that I shall show you" (Eze 40:4; 44:5)
- "making your ear attentive to wisdom and inclining your heart to understanding" (Pro 2:2); "Incline your ear … apply your heart" (Pro 22:17; 23:12); "Hear, my son … direct your heart" (Pro 23:19)
- **The hearing heart:** "Give your servant … an understanding [hearing] mind" (1Ki 3:9) — lēv + šāmaʿ confirmed (§0.5)

### 3.2 A hardened heart does not listen
- "Pharaoh's heart was hardened, and he would not listen" (Exo 7:13, 22; 8:15, 19; 9:12)
- "They made their hearts diamond-hard lest they should hear the law … sent by his Spirit" (Zec 7:12) [D1]
- "a hard forehead and a stubborn heart … not willing to listen" (Eze 3:7)
- "every one of you follows his stubborn, evil will [heart], refusing to listen to me" (Jer 16:12, d1); "did not obey or incline their ear, but … walked in the stubbornness of their evil hearts" (Jer 7:24; 11:8; 13:10)
- "if your heart turns away, and you will not hear" (Deu 30:17)
- **Hearing without doing:** "they hear what you say but they will not do it … their heart is set on their gain" (Eze 33:31)
- ◆ **An inner state blocks hearing:** "they did not listen to Moses, because of their broken spirit and harsh slavery" (Exo 6:9) [H]

### 3.3 What is heard moves the inner seat — hearing as its main entry
- **Collapse:**
  - "as soon as we heard it, our hearts melted, and there was no spirit left in any man" (Jos 2:11; 5:1) [H]
  - "I hear the sound of the trumpet … my heart is beating wildly" (Jer 4:19)
  - "his wife told him these things, and his heart died within him" (1Sa 25:37)
  - "Because of the news … every heart will melt … every spirit will faint" (Eze 21:7)
  - "Let not your heart faint … at the report" (Jer 51:46)
- **Revival:** "when they told him all the words of Joseph … the spirit of their father Jacob revived" (Gen 45:27) — one verse after "his heart became numb, for he did not believe them" (Gen 45:26).
- **Refreshment:** "good news refreshes the bones" (Pro 15:30); "Like cold water to a thirsty soul, so is good news" (Pro 25:25).
- **Immunity:** "He is not afraid of bad news; his heart is firm" (Psa 112:7).
- **The divine Spirit on hearing:** "the Spirit of God rushed upon Saul when he heard these words" (1Sa 11:6) [D1].
- ◆ **Hearing as eating for the soul:**
  - "Listen diligently to me, and eat what is good, and delight yourselves [nephesh] in rich food. Incline your ear … hear, that your soul may live" (Isa 55:2–3)
  - cf. "Your words were found, and I ate them" (Jer 15:16; Batch A)

### 3.4 God hearing the heart
- "If I had cherished iniquity in my heart, the Lord would not have listened" (Psa 66:18)
- "you hear the desire of the afflicted; you will strengthen their heart; you will incline your ear" (Psa 10:17)
- "you set your heart to understand … your words have been heard" (Dan 10:12)
- "because your heart was tender … I also have heard you" (2Ch 34:27; 2Ki 22:19)
- ◆ **Inner speech unheard by people:** "Hannah was speaking in her heart; only her lips moved, and her voice was not heard" (1Sa 1:13)

### 3.5 Hearing and the divine Spirit
- "Did you receive the Spirit by works of the law or by hearing with faith?" (Gal 3:2, 5) [D2]
- "the Holy Spirit fell on all who heard the word" (Act 10:44)
- "warned them by your Spirit through your prophets. Yet they would not give ear" (Neh 9:30)
- "He who has an ear, let him hear what the Spirit says to the churches" (Rev 2–3) [D2]
- ◆ **No hearing, no breath:** "they have ears, but do not hear, nor is there any breath in their mouths" (Psa 135:17)

---

## 4. Word and speech (M65)

### 4.1 Words placed in the heart (and soul)
- "these words … shall be on your heart" (Deu 6:6)
- "lay up these words of mine in your heart and in your soul" (Deu 11:18); "lay up his words in your heart" (Job 22:22)
- "Let your heart hold fast my words" (Pro 4:4); "I have stored up your word in my heart" (Psa 119:11)
- "the word is very near you. It is in your mouth and in your heart" (Deu 30:14)
- **Word removed or kept:** "the devil … takes away the word from their hearts" (Luk 8:12); "hold it fast in an honest and good heart" (Luk 8:15)

### 4.2 Words coming from the heart
- "My words declare the uprightness of my heart" (Job 33:3)
- "My heart overflows with a pleasing theme" (Psa 45:1)
- "uttering from the heart lying words" (Isa 59:13)
- **Mismatch:** "His speech was smooth as butter, yet war was in his heart" (Psa 55:21)
- "let not your heart be hasty to utter a word before God" (Ecc 5:2)

### 4.3 Disclosing or keeping the heart ◆
- **Telling the heart:** "he told her all his heart" (Judg 16:17–18) — revealing the heart is speech.
- **What is "on the mind":** "I … will tell you all that is on your mind [heart]" (1Sa 9:19); the queen "told him all that was on her mind" (1Ki 10:2).
- **Keeping:**
  - "I kept the matter in my heart" (Dan 7:28)
  - "he who is trustworthy in spirit keeps a thing covered" (Pro 11:13) [H]
  - "Whoever restrains his words … a cool spirit" (Pro 17:27) [H]
  - "I told no one what my God had put into my heart" (Neh 2:12)

### 4.4 Words acting on the inner seat
- **For good:**
  - "Gracious words … sweetness to the soul and health to the body" (Pro 16:24)
  - "a good word makes him glad" (Pro 12:25)
  - "my soul waits, and in his word I hope" (Psa 130:5; 119:81); "give me life … strengthen me according to your word" (Psa 119:25, 28)
  - "the implanted word, which is able to save your souls" (Jam 1:21)
- **For harm:**
  - "when she pressed him hard with her words … his soul was vexed to death" (Judg 16:16)
  - "troubled you with words, unsettling your minds [psychē]" (Act 15:24)
  - "by smooth talk and flattery they deceive the hearts of the naive" (Rom 16:18)
- **Dividing and discerning:** "the word of God … piercing to the division of soul and of spirit … discerning the thoughts and intentions of the heart" (Heb 4:12).

### 4.5 ◆ Word and breath/wind paired
- "By the word of the Lord the heavens were made, and by the breath of his mouth all their host" (Psa 33:6)
- "He sends out his word … he makes his wind blow" (Psa 147:18); "stormy wind fulfilling his word" (Psa 148:8)
- "My Spirit that is upon you, and my words that I have put in your mouth, shall not depart" (Isa 59:21) [D1]
- **Empty words as wind:** "windy words" (Job 16:3); "the words of your mouth be a great wind" (Job 8:2); "the speech of a despairing man is wind" (Job 6:26)
- ◆ **Word and flesh:** "the Word became flesh" (Joh 1:14); "according to the word of the man of God … his flesh was restored" (2Ki 5:14)

---

## 5. Memory and forgetting (M81, M82)

- **Heart forgets when full and proud:** "your heart be lifted up, and you forget the Lord" (Deu 8:14); "they became full … their heart was lifted up; therefore they forgot me" (Hos 13:6).
- **Soul and heart told to remember:**
  - "Bless the Lord, O my soul, and forget not all his benefits" (Psa 103:2)
  - "keep your soul diligently, lest you forget … lest they depart from your heart" (Deu 4:9)
  - "do not forget my teaching, but let your heart keep my commandments" (Pro 3:1)
- **Remembering weighs on the soul:** "My soul continually remembers it and is bowed down within me" (Lam 3:20); "I have forgotten what happiness is" (Lam 3:17); "These things I remember, as I pour out my soul" (Psa 42:4, 6).
- **Remembering turns to hope:** "this I call to mind [heart], and therefore I have hope" (Lam 3:21).
- **Remembering and the spirit:** "When I remember God, I moan; when I meditate, my spirit faints" (Psa 77:3); "Let me remember my song … meditate in my heart. Then my spirit made a diligent search" (Psa 77:6) [H].
- **Fainting leads to remembering:** "When my life was fainting away, I remembered the Lord" (Jon 2:7).
- ◆ **Grief makes one forget food:** "My heart is struck down like grass … I forget to eat my bread" (Psa 102:4).
- **"Turning the heart" = returning:** "if they turn their heart [bring back to heart]" (1Ki 8:47; 2Ch 6:37) [lexical].
- ◆ **God remembers human frailty:** "He remembered that they were but flesh, a wind that passes" (Psa 78:39); "I will remember my covenant … every living creature of all flesh" (Gen 9:15–16); "Remember that my life is a breath" (Job 7:7).
- **The Spirit reminds:** "the Holy Spirit … will … bring to your remembrance" (Joh 14:26) [D1].
- **Conscience and remembrance:** "with a clear conscience, as I remember you constantly in my prayers" (2Ti 1:3).
- ◆ **Suppressed remembering becomes fire:** "If I say, 'I will not mention him' … there is in my heart as it were a burning fire" (Jer 20:9).

---

## 6. Prophecy and vision (M43)

- **Heart or own spirit as a *false* source:**
  - "those who prophesy from their own hearts" (Eze 13:2, 17)
  - "prophesy the deceit of their own heart" (Jer 23:26); "visions of their own minds, not from the mouth of the Lord" (Jer 23:16; 14:14)
  - "foolish prophets who follow their own spirit" (Eze 13:3) [H]
- **God's Spirit as the true source:**
  - "the Spirit of God rushed upon him, and he prophesied" (1Sa 10:10; 19:20, 23)
  - "as soon as the Spirit rested on them, they prophesied" (Num 11:25–26); "that the Lord would put his Spirit on them!" (Num 11:29)
  - "I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy" (Joe 2:28; Act 2:17–18)
  - "carried along by the Holy Spirit" — "not by the will of man" (2Pe 1:21)
- ◆ **Spirit, prophecy and a new heart in sequence:** "the Spirit of the Lord will rush upon you, and you will prophesy … and be turned into another man" (1Sa 10:6) → "God gave him another heart" (1Sa 10:9).
- **The prophet's own spirit remains governable:** "the spirits of prophets are subject to prophets" (1Co 14:32) [H].
- ◆ **One verb, two spirits:**
  - "a harmful spirit from God rushed upon Saul, and he **raved** [*prophesied*] within his house" (1Sa 18:10) [O]
  - "a lying spirit in the mouth of all his prophets" (1Ki 22:22–23) [O]
- ◆ **Wind prophets and prophesying to the breath:**
  - "The prophets will become wind" (Jer 5:13); "utter wind and lies" (Mic 2:11)
  - "Prophesy to the breath … Come from the four winds, O breath" (Eze 37:9–10)
  - "it was allowed to give breath to the image of the beast, so that the image … might even speak" (Rev 13:15) — false animation
- ◆ **Inner and outer signs:**
  - "lay up these words … in your heart and in your soul, and you shall bind them as a sign on your hand" (Deu 11:18)
  - "circumcised in the flesh … a sign of the covenant" (Gen 17:11)
- **Signs set against a hardened heart:** Exo 7:3; 10:1.

---

## 7. Reasoning, judging and interpreting (M63)

- **Questioning in the heart, perceived in the spirit:** "some of the scribes … questioning in their hearts … Jesus, perceiving in his spirit" (Mar 2:6–8) [H]; "Why do you question in your hearts?" (Luk 5:22); "all were questioning in their hearts concerning John" (Luk 3:15).
- **Evil reasonings from the heart:** "out of the heart come evil thoughts" (Mat 15:19; Mar 7:21); "why do doubts arise in your hearts?" (Luk 24:38); "does not doubt in his heart" (Mar 11:23).
- **Resolving in the heart:** "whoever is firmly established in his heart … and has determined this in his heart" (1Co 7:37); ◆ "I took counsel with myself [my heart]" (Neh 5:7).
- **Judgment and the inner seat:**
  - "who will … disclose the purposes of the heart" (1Co 4:5)
  - "I said in my heart, God will judge" (Ecc 3:17)
  - "an understanding mind to govern [judge]" (1Ki 3:9)
- **Flesh as a standard of judging:** "You judge according to the flesh" (Joh 8:15); "set their minds on the things of the flesh" (Rom 8:5).
- **Conscience judged by another's:** "why should my liberty be determined by someone else's conscience?" (1Co 10:29).
- **Judging in spirit, absent in body:** "though absent in body, I am present in spirit … I have already pronounced judgment" (1Co 5:3) [H].
- ◆ **No distinction:** "the Spirit told me to go with them, making no distinction" (Act 11:12) [D2] // "he made no distinction … having cleansed their hearts by faith" (Act 15:9).
- **Interpreting dreams by spirit:** "an excellent spirit … to interpret dreams" (Dan 5:12) [H2+X]; "the spirit of the holy gods is in you" (Dan 4:9, 18) [D-attr]; "his spirit was troubled … none who could interpret" (Gen 41:8) [H].

---

## 8. ◆ Soul-ish vs spiritual — psychikos / pneumatikos

- "The natural [*psychikos*] person does not accept the things of the Spirit of God … they are spiritually discerned" (1Co 2:14) [D1]
- "It is sown a natural body; it is raised a spiritual body … not the spiritual that is first but the natural, and then the spiritual" (1Co 15:44–46)
- "worldly [*psychikoi*] people, devoid of the Spirit" (Jude 19) [D3]
- [lexical; Claude reading] In these verses the adjective formed from *soul* is set **against** the adjective formed from *spirit*. It is the clearest place in the data where soul and spirit are contrasted as two orders, rather than paralleled (cf. depiction v1 §3.4 on Heb 4:12 and 1Co 15:45).

---

## 9. Cross-cutting observations for Batch B [Claude reading]

1. **The heart is the organ of attention, knowing, understanding, storing, remembering and reasoning.** Attention is literally *setting the heart*. The heart's **hardness** is the same thing as failing to hear and understand.
2. **The soul relates to knowledge by *receiving* it** (pleasant, sweet, life-giving) and by **dwelling on memories** (bowed down). The soul can be commanded to remember. Soul-desire can run ahead of knowledge.
3. **The human spirit is the seat of self-knowledge and searching.** It knows a person's thoughts, makes understanding possible as God's breath in man, searches after the heart meditates, and perceives others' inner reasoning. A **cool** spirit (temper) is linked with understanding and restrained speech.
4. **God's Spirit is the true source of knowledge, wisdom, skill, teaching, remembrance and prophecy.** The heart or own spirit as a source of prophecy is condemned.
5. **Hearing is the main channel into the inner seat.** The ear receives; the heart keeps, understands or refuses. News makes hearts melt, spirits revive and souls refresh. God hears the heart. The "hearing heart" of 1 Kgs 3:9 is confirmed in the tags.
6. **Word and breath belong together:** creative word // breath of his mouth; Spirit and words in the mouth; empty words are "wind".
7. **Flesh appears as a *way of knowing and judging*** ("according to the flesh"), set against revelation from the Father and the Spirit.
8. **Soul-ish vs spiritual (§8)** is a genuine textual contrast between the soul and spirit orders, and it touches the open question from depiction v1.

---

## 10. Next

- **Batch C** (willing / desiring / orientation): M18, M64, M28, M69, M34, M68, M83, M11, M30, M75, M66, M67.
- The "speak" verbs held in **M42** will be read in **Batch E** (relating to God). The H0559 "said in heart" series is not in the pairs file; see **Ruling R2** for how to cover it.
