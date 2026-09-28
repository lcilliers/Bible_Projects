# M47 — seat coverage across clusters, and the verses with no tie to the seat (v1)

**Date:** 2026-09-28
**Status:** investigation + **proposal awaiting researcher approval**. No reading of no-seat verses has started. No DB writes.
**Trigger (researcher, verbatim):** "If I understand it correctly then the M47 work was about where inner being words explicitly interacts/relates to the seat. It would be interesting to know if there are any clusters that have not been included in this angle at all. Related to it, should be not explore each cluster separately, with a special emphasis on the verses that have no ties to the seat. The ties may be implicit, through cross correlation, but it may also not tie back at all - and what does that tell us. I think this work need to be done before batch H can take place, and maybe the sythesis will be redefined by then."
**Note:** Batch H was already complete. This work is read as coming **before the synthesis**, which it may redefine.

---

## 1. The researcher's understanding is correct

Batches A–H read **only M47 verses**: verses that contain a heart / soul / spirit / flesh / conscience / bosom word, together with whatever other-cluster words they contain. **A cluster verse with no seat word never entered the reading.**

**Source used here:** `iba/app/db/iba.db` → `verse_lexical`. This table records every word of all 29,760 verses with its resolved cluster (`role`).
- It reproduces the earlier inputs exactly: 3,175 M47 word rows in 2,688 verses (= the M47 surface file), and 2,404 M47 verses with another M-cluster word (= the co-occurrence assessment).
- **`strong_verse` is not usable for this.** It is incomplete; for example "king" (H4428G) has 0 rows there but 1,870 verses in `verse_lexical`.

## 2. Q1 — Is any cluster left out of the M47 angle altogether?

**No M-cluster is left out.** All 79 other M-clusters share at least one verse with an M47 word. The thinnest are Sloth & Diligence M67 (2 verses), Madness M66 (5), Encouragement M52 (8), Faith M31 (8) and Dishonor M53 (11).

**What *was* left out, by design:** the pairs file held M-codes only, so these were never in view:
- **T14 Body-Parts** (685 verses shared with M47). It includes **`qereb` "entrails: within / among" (H7130G, 194 verses)** — the "within me" word, which works like an unnamed seat — together with bones, kidneys, bowels, blood, face / nostril (= anger), eye, ear, lips and tongue. Ruling 4 excluded bones, kidneys and bowels as separate *study words*, but they were also invisible as *co-occurrences*.
- **T7 Party-Divine** (975 verses shared) and **T8 Party-Human** (724): **whose** heart or soul it is.
- **T3 Operations** (2,298): including "say" (H0559, the "said in his heart" series) and "die".
- T2, T5, T6 (function words), T9–T13, T15, and FLAG.

## 3. Q2 — How much of each cluster ties to the seat?

**Headline [measured]:** of the **24,365 verses** that carry any M-cluster word other than M47:
- **2,404 (10%)** contain a seat word in the same verse — **this is everything Batches A–H read**
- **7,588 (31%)** have no seat word in the verse, but have one **within 3 verses in the same chapter** (a possible contextual tie)
- **14,373 (59%)** have **no seat word within 3 verses at all**

Per cluster, the share with a seat word in the same verse runs from **6% to 28%**:
- **Highest:** Disobedience M75 28% · Defilement M10c 25% · Covenant M32 23% · Life & Death M25 19% · Purity & Holiness M61 19% · Seeking M83 19% · Joy M04 18%
- **Lowest:** Authority M72 6% · Fasting M21 6% · Release M59 6% · Sloth M67 6% · Worship & Service M36 7% · Judgment M26 7% · Wealth M46 7% · Shame M07 7% · Astonishment M48 7%
- **The emotion clusters are low:** Fear 11%, Anger 10%, Grief 16%, Joy 18%. **Most fear and anger in the text is stated without any seat word.**

The full table is in §7.

## 4. What this might tell us — hypotheses to test, not findings [Claude reading]

1. **The seat words may be a marked form, not the default.** If about 90% of fear, anger, joy and desire is stated of the *person* ("Saul was afraid"), then naming the heart or soul could be a deliberate choice: to locate, intensify, internalise or hide the state. The batches may have described the **marked** case. The question becomes **when and why the text reaches for the seat**.
2. **The subject may be the real variable.** Many no-seat verses may have **God** as subject (God's anger and compassion are often stated with no seat word, or with "nostril" or "bowels"). That would be a finding about how the divine inner life is spoken of. It can be measured with T7.
3. **Another vocabulary may stand in for the seat:** `qereb` "within", bones, kidneys, bowels, face / nostril, eyes. These could be implicit seats.
4. **Some clusters may barely belong to the inner being** in most of their verses. Authority, Worship & Service, Wealth and Judgment are largely **outward** acts and settings. Their low tie may say that the cluster's inner dimension is thin, or that it is carried by other clusters' words.
5. **The context tie (31%) needs testing.** "Within 3 verses" is only proximity. Whether the nearby seat word actually governs the state (Hannah's weeping → "why is your heart sad?") must be read, not assumed.

## 5. Proposed approach (for approval)

**Principle:** measure first, read second, and pilot before scaling. 21,961 no-seat verses cannot be read one by one at the current cost level ([[feedback_methodology_cycle_cost]]).

**Step 1 — Tie profile per verse (script, read-only, cheap).** Classify every no-seat cluster verse into one tie class:

| Class | Test |
|---|---|
| **N — neighbour** | seat word within ±3 verses in the same chapter |
| **B — body-seat** | T14 inward words in the verse: `qereb` within, bones, kidneys, bowels, belly / womb, nostril-anger [the list to be confirmed by you] |
| **P — person, no seat** | a party (T7 divine / T8 human / T11 collective) is present as the one who fears, rejoices, etc. Record whether it is God or a human |
| **X — cross-correlated** | the verse's cluster word is one that often co-occurs with the seat elsewhere (e.g. a Strong's code with a high seat rate across the corpus) |
| **0 — no tie** | none of the above |

Output: per-cluster profile table + CSV. **One file, no reading yet.**

**Step 2 — Pilot reading on two contrasting clusters** (you choose; my suggestion):
- **M02 Anger & Wrath** (681 verses; 10% seat). An emotion with a known alternative vocabulary (nostril) and a strong divine-subject share.
- **M20 Doubt & Discouragement** (275 verses; 11% seat). Small enough to read in full.

For each, read the no-seat verses by tie class and ask: why is the seat absent here, what carries the inner state instead, and what happened before and after. Same interaction-first format as Batches F–H.

**Step 3 — Decide the scale-up** from the pilot: all clusters in full, a sample per cluster, or only the classes that proved informative.

**Step 4 — Then revisit the synthesis.** Its candidates may change. Hypothesis 1 (the seat as a marked form), if it holds, would frame all four.

## 6. Decisions needed from you

1. Approve Step 1 (the tie-profile script)?
2. The body-seat list for class B: `qereb`, bones, kidneys, bowels, belly / womb, nostril. Add or remove anything?
3. The pilot clusters: M02 + M20, or others?
4. Treat T-cluster co-occurrence (T14, T7) as part of the M47 angle from now on, or only as tie classes in this exercise?

---

## 7. Full table (from `verse_lexical`, 2026-09-28)

"Seat word" = any M47 word. "Within ±3" = the verse has no seat word, but one occurs within 3 verses in the same chapter.

| Cluster | Name | Verses | With seat word | % | No seat word | Seat word within ±3 verses | No seat word within ±3 | % of cluster |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| FLAG | Flag | 2024 | 130 | 6% | 1894 | 666 | 1228 | 61% |
| M01 | Fear & Awe | 916 | 97 | 11% | 819 | 316 | 503 | 55% |
| M02 | Anger & Wrath | 681 | 66 | 10% | 615 | 263 | 352 | 52% |
| M03 | Grief & Lament | 841 | 136 | 16% | 705 | 260 | 445 | 53% |
| M04 | Joy & Gladness | 600 | 105 | 18% | 495 | 196 | 299 | 50% |
| M05 | Kindness & Friendship | 795 | 105 | 13% | 690 | 269 | 421 | 53% |
| M06 | Malice & Enmity | 921 | 132 | 14% | 789 | 336 | 453 | 49% |
| M07 | Shame & Confusion | 385 | 28 | 7% | 357 | 154 | 203 | 53% |
| M08 | Pride & Arrogance | 1012 | 101 | 10% | 911 | 333 | 578 | 57% |
| M09 | Humility & Lowliness | 307 | 41 | 13% | 266 | 109 | 157 | 51% |
| M10 | Violence & Cruelty | 931 | 84 | 9% | 847 | 275 | 572 | 61% |
| M11 | Turning & Repentance | 518 | 60 | 12% | 458 | 163 | 295 | 57% |
| M12 | Righteousness & Integrity | 1471 | 173 | 12% | 1298 | 557 | 741 | 50% |
| M13 | Faith & Faithfulness | 773 | 86 | 11% | 687 | 264 | 423 | 55% |
| M14 | Deceit & Falsehood | 901 | 126 | 14% | 775 | 338 | 437 | 49% |
| M15 | Knowing & Understanding | 2203 | 310 | 14% | 1893 | 739 | 1154 | 52% |
| M16 | Wisdom & Folly | 898 | 145 | 16% | 753 | 342 | 411 | 46% |
| M18 | Desire & Longing | 1386 | 220 | 16% | 1166 | 481 | 685 | 49% |
| M19 | Trust & Refuge | 563 | 65 | 12% | 498 | 198 | 300 | 53% |
| M20 | Doubt & Discouragement | 275 | 30 | 11% | 245 | 109 | 136 | 49% |
| M21 | Fasting & Piety | 349 | 22 | 6% | 327 | 80 | 247 | 71% |
| M22 | Praise & Song | 1214 | 105 | 9% | 1109 | 394 | 715 | 59% |
| M23 | Strength & Courage | 1881 | 191 | 10% | 1690 | 590 | 1100 | 58% |
| M24 | Faintness & Despair | 1487 | 216 | 15% | 1271 | 504 | 767 | 52% |
| M25 | Life & Death | 1140 | 212 | 19% | 928 | 373 | 555 | 49% |
| M26 | Judgment & Condemnation | 463 | 34 | 7% | 429 | 153 | 276 | 60% |
| M28 | Envy & Greed | 227 | 35 | 15% | 192 | 80 | 112 | 49% |
| M30 | Rebellion & Stubbornness | 714 | 90 | 13% | 624 | 246 | 378 | 53% |
| M31 | Faith | 57 | 8 | 14% | 49 | 22 | 27 | 47% |
| M32 | Covenant | 87 | 20 | 23% | 67 | 23 | 44 | 51% |
| M33 | Rest & Peace | 773 | 87 | 11% | 686 | 253 | 433 | 56% |
| M34 | Patience & Perseverance | 312 | 44 | 14% | 268 | 103 | 165 | 53% |
| M35 | Being Tested | 312 | 42 | 13% | 270 | 117 | 153 | 49% |
| M36 | Worship & Service | 2234 | 163 | 7% | 2071 | 572 | 1499 | 67% |
| M37 | Firstborn & Foreknowledge | 294 | 25 | 9% | 269 | 65 | 204 | 69% |
| M39 | Gift & Favor | 221 | 28 | 13% | 193 | 59 | 134 | 61% |
| M41 | Being Heard | 1400 | 124 | 9% | 1276 | 458 | 818 | 58% |
| M42 | Prayer & Petition | 2976 | 268 | 9% | 2708 | 984 | 1724 | 58% |
| M43 | Prophecy & Vision | 742 | 77 | 10% | 665 | 257 | 408 | 55% |
| M44 | Covenant & Fellowship | 823 | 94 | 11% | 729 | 247 | 482 | 59% |
| M45 | Renewal & Transformation | 1225 | 140 | 11% | 1085 | 430 | 655 | 53% |
| M46 | Wealth & Riches | 652 | 46 | 7% | 606 | 233 | 373 | 57% |
| M48 | Astonishment & Wonder | 192 | 13 | 7% | 179 | 64 | 115 | 60% |
| M49 | Thanksgiving | 193 | 22 | 11% | 171 | 58 | 113 | 59% |
| M50 | Grace & Mercy | 687 | 67 | 10% | 620 | 246 | 374 | 54% |
| M51 | Love & Devotion | 543 | 76 | 14% | 467 | 178 | 289 | 53% |
| M52 | Encouragement | 96 | 8 | 8% | 88 | 36 | 52 | 54% |
| M53 | Dishonor & Disgrace | 89 | 11 | 12% | 78 | 30 | 48 | 54% |
| M54 | Torah & Obedience | 567 | 73 | 13% | 494 | 209 | 285 | 50% |
| M55 | Destruction & Ruin | 525 | 47 | 9% | 478 | 169 | 309 | 59% |
| M56 | Sin & Guilt | 1087 | 136 | 13% | 951 | 374 | 577 | 53% |
| M57 | Corruption & Perversion | 206 | 17 | 8% | 189 | 76 | 113 | 55% |
| M58 | Wickedness | 1299 | 176 | 14% | 1123 | 490 | 633 | 49% |
| M59 | Release & Reconciliation | 253 | 15 | 6% | 238 | 71 | 167 | 66% |
| M60 | Confession & Forgiveness | 239 | 29 | 12% | 210 | 88 | 122 | 51% |
| M61 | Purity & Holiness | 935 | 182 | 19% | 753 | 258 | 495 | 53% |
| M62 | Truth & Sincerity | 53 | 8 | 15% | 45 | 21 | 24 | 45% |
| M63 | Reasoning & Interpretation | 565 | 51 | 9% | 514 | 178 | 336 | 59% |
| M64 | Will & Resolve | 411 | 47 | 11% | 364 | 144 | 220 | 54% |
| M65 | Speech & Tongue | 1963 | 183 | 9% | 1780 | 627 | 1153 | 59% |
| M66 | Madness & Recklessness | 28 | 5 | 18% | 23 | 10 | 13 | 46% |
| M67 | Sloth & Diligence | 35 | 2 | 6% | 33 | 10 | 23 | 66% |
| M68 | Hope & Waiting | 258 | 36 | 14% | 222 | 108 | 114 | 44% |
| M69 | Self-Control & Zeal | 49 | 7 | 14% | 42 | 14 | 28 | 57% |
| M70 | Lifting & Bearing | 167 | 16 | 10% | 151 | 51 | 100 | 60% |
| M71 | Glory & Splendor | 212 | 18 | 8% | 194 | 77 | 117 | 55% |
| M72 | Authority & Dominion | 3928 | 235 | 6% | 3693 | 1019 | 2674 | 68% |
| M73 | Sickness & Weakness | 317 | 45 | 14% | 272 | 88 | 184 | 58% |
| M74 | Keeping & Guarding | 653 | 90 | 14% | 563 | 235 | 328 | 50% |
| M75 | Disobedience & Lawlessness | 57 | 16 | 28% | 41 | 17 | 24 | 42% |
| M76 | Walk & Conduct | 500 | 62 | 12% | 438 | 182 | 256 | 51% |
| M77 | Stumbling & Trial | 210 | 30 | 14% | 180 | 82 | 98 | 47% |
| M78 | Slavery & Bondage | 241 | 25 | 10% | 216 | 78 | 138 | 57% |
| M79 | Salvation & Ransom | 255 | 36 | 14% | 219 | 89 | 130 | 51% |
| M80 | Blessing | 459 | 41 | 9% | 418 | 159 | 259 | 56% |
| M81 | Memory (act) | 377 | 56 | 15% | 321 | 140 | 181 | 48% |
| M82 | Reminder & Report | 75 | 12 | 16% | 63 | 24 | 39 | 52% |
| M83 | Seeking & Inquiring | 496 | 96 | 19% | 400 | 132 | 268 | 54% |
| M84 | Outcry & Shouting | 219 | 25 | 11% | 194 | 67 | 127 | 58% |
| M10c | Defilement | 288 | 73 | 25% | 215 | 101 | 114 | 40% |
| T2 | Supplementary | 29603 | 2673 | 9% | 26930 | 8837 | 18093 | 61% |
| T3 | Operations | 25842 | 2298 | 9% | 23544 | 7657 | 15887 | 61% |
| T4 | Adversarial | 169 | 22 | 13% | 147 | 60 | 87 | 51% |
| T5 | Negator | 6647 | 723 | 11% | 5924 | 2167 | 3757 | 57% |
| T6 | Connective | 23992 | 2244 | 9% | 21748 | 7060 | 14688 | 61% |
| T7 | Party-Divine | 9527 | 975 | 10% | 8552 | 2928 | 5624 | 59% |
| T8 | Party-Human | 10192 | 724 | 7% | 9468 | 2596 | 6872 | 67% |
| T9 | Party-Angelic | 450 | 26 | 6% | 424 | 125 | 299 | 66% |
| T10 | Places | 7806 | 491 | 6% | 7315 | 2052 | 5263 | 67% |
| T11 | Corporate-Collective | 7133 | 396 | 6% | 6737 | 1876 | 4861 | 68% |
| T12 | Objects-Artifacts | 4014 | 267 | 7% | 3747 | 988 | 2759 | 69% |
| T13 | Natural-World | 3730 | 314 | 8% | 3416 | 1135 | 2281 | 61% |
| T14 | Body-Parts | 5962 | 685 | 11% | 5277 | 1892 | 3385 | 57% |
| T15 | Calendar | 18 | 0 | 0% | 18 | 5 | 13 | 72% |

**Totals:** 24,365 M-cluster verses (excluding M47); 2,404 with a seat word; 21,961 without; 7,588 of those have a seat word within ±3 verses; 14,373 do not. 5,111 of the 29,760 verses carry no M-cluster word at all.
