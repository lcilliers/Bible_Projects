# Cluster Overview Report — escalation #1598

**Date:** 2026-09-08
**Status:** untagged pool closed — every content-role strong in the corpus now has a cluster home.

---

## 1. Headline numbers

| Metric | Value |
|---|---:|
| Distinct content-role strongs in the corpus | 15,287 |
| Distinct strongs carrying at least one cluster tag | 15,595 |
| Total live `cluster_strong` rows (some strongs dual-tagged, e.g. H0113 "lord" → both Party-Divine and Party-Human) | 15,693 |
| Live clusters (M-codes + T-codes + FLAG) | 95 |
| **Untagged pool at session start** | **7,810–8,268** (sized differently at different points as the pool definition was refined) |
| **Untagged pool now** | **0** |

Confidence on the live tags:

| confidence | rows |
|---|---:|
| high | 8,411 |
| medium | 2,084 |
| heuristic | 1,256 |
| low | 706 |
| (unset — pre-#1598 legacy rows) | 3,236 |

This session's own work (`source='claude-scan-20260908'`) accounts for 8,295 of the 15,693 live rows — the majority of the table, concentrated in the untagged-pool closure (escalation #1598, this session) rather than a rebuild of what was already there.

---

## 2. M-code clusters (characteristic/thematic — the study's primary taxonomy)

"Verses" = distinct verses containing at least one strong tagged to that cluster (a verse can and often does count toward several M-codes at once).

| Code | Name | Members | Verses |
|---|---|---:|---:|
| M01 | Fear & Awe | 99 | 916 |
| M02 | Anger & Wrath | 68 | 681 |
| M03 | Grief & Lament | 111 | 841 |
| M04 | Joy & Gladness | 51 | 600 |
| M05 | Kindness & Friendship | 90 | 807 |
| M06 | Malice & Enmity | 90 | 921 |
| M07 | Shame & Confusion | 41 | 385 |
| M08 | Pride & Arrogance | 81 | 1,012 |
| M09 | Humility & Lowliness | 30 | 307 |
| M10 | Violence & Cruelty | 51 | 931 |
| M10c | Defilement | 20 | 288 |
| M11 | Turning & Repentance | 24 | 518 |
| M12 | Righteousness & Integrity | 75 | 1,471 |
| M13 | Faith & Faithfulness | 24 | 773 |
| M14 | Deceit & Falsehood | 86 | 901 |
| M15 | Knowing & Understanding | 94 | 2,230 |
| M16 | Wisdom & Folly | 71 | 898 |
| M18 | Desire & Longing | 105 | 1,395 |
| M19 | Trust & Refuge | 31 | 563 |
| M20 | Doubt & Discouragement | 28 | 275 |
| M21 | Fasting & Piety | 20 | 349 |
| M22 | Praise & Song | 48 | 1,214 |
| M23 | Strength & Courage | 126 | 2,472 |
| M24 | Faintness & Despair | 139 | 1,487 |
| M25 | Life & Death | 30 | 1,140 |
| M26 | Judgment & Condemnation | 37 | 463 |
| M28 | Envy & Greed | 39 | 238 |
| M30 | Rebellion & Stubbornness | 48 | 714 |
| M31 | Faith | 9 | 89 |
| M32 | Covenant | 9 | 82 |
| M33 | Rest & Peace | 58 | 773 |
| M34 | Patience & Perseverance | 36 | 312 |
| M35 | Being Tested | 22 | 312 |
| M36 | Worship & Service | 34 | 2,234 |
| M37 | Firstborn & Foreknowledge | 22 | 294 |
| M39 | Gift & Favor | 23 | 221 |
| M41 | Being Heard | 20 | 1,400 |
| M42 | Prayer & Petition | 55 | 2,976 |
| M43 | Prophecy & Vision | 23 | 742 |
| M44 | Covenant & Fellowship | 38 | 823 |
| M45 | Renewal & Transformation | 70 | 1,225 |
| M46 | Wealth & Riches | 42 | 652 |
| M47 | Inner Seat | 45 | 2,688 |
| M48 | Astonishment & Wonder | 15 | 192 |
| M49 | Thanksgiving | 5 | 193 |
| M50 | Grace & Mercy | 31 | 687 |
| M51 | Love & Devotion | 22 | 543 |
| M52 | Encouragement | 8 | 96 |
| M53 | Dishonor & Disgrace | 24 | 89 |
| M54 | Torah & Obedience | 9 | 566 |
| M55 | Destruction & Ruin | 63 | 568 |
| M56 | Sin & Guilt | 41 | 1,087 |
| M57 | Corruption & Perversion | 32 | 206 |
| M58 | Wickedness | 49 | 1,299 |
| M59 | Release & Reconciliation | 15 | 244 |
| M60 | Confession & Forgiveness | 9 | 213 |
| M61 | Purity & Holiness | 47 | 935 |
| M62 | Truth & Sincerity | 20 | 72 |
| M63 | Reasoning & Interpretation | 38 | 565 |
| M64 | Will & Resolve | 28 | 411 |
| M65 | Speech & Tongue | 18 | 1,963 |
| M66 | Madness & Recklessness | 13 | 28 |
| M67 | Sloth & Diligence | 2 | 14 |
| M68 | Hope & Waiting | 22 | 258 |
| M69 | Self-Control & Zeal | 14 | 49 |
| M70 | Lifting & Bearing | 10 | 167 |
| M71 | Glory & Splendor | 23 | 212 |
| M72 | Authority & Dominion | 54 | 3,928 |
| M73 | Sickness & Weakness | 51 | 317 |
| M74 | Keeping & Guarding | 22 | 653 |
| M75 | Disobedience & Lawlessness | 15 | 57 |
| M76 | Walk & Conduct | 10 | 500 |
| M77 | Stumbling & Trial | 18 | 210 |
| M78 | Slavery & Bondage | 22 | 241 |
| M79 | Salvation & Ransom | 13 | 255 |
| M80 | Blessing | 10 | 459 |
| M81 | Memory (act) | 14 | 377 |
| M82 | Reminder & Report | 12 | 75 |
| M83 | Seeking & Inquiring | 7 | 496 |
| M84 | Outcry & Shouting | 23 | 219 |
| **FLAG** | Flag | 29 | 2,024 |

79 M-codes + FLAG, 3,616 members total. Smallest by members: M67 Sloth & Diligence (2). Largest by members: M24 Faintness & Despair (139). Largest by verse-reach: M72 Authority & Dominion (3,928 verses) and M42 Prayer & Petition (2,976) — both driven by a small set of very high-frequency terms (e.g. M72's "king"), not by member count. Smallest verse-reach: M66 Madness & Recklessness (28) and M67 Sloth & Diligence (14).

Distinct verses touched by at least one M-code: **24,757 of 29,759 live verses (83.2%)**.

---

## 3. T-code clusters (special lookup groups — structural/type, not thematic)

| Code | Name | Members | Purpose |
|---|---|---:|---|
| T2 | Supplementary | 6,375 | Deliberately set aside from the M/T thematic scaffold — **not** a claim of irrelevance (see §5) |
| T3 | Operations | 2,577 | Action/verb bucket — used when a verb isn't directly tied to one specific characteristic |
| T4 | Adversarial | 6 | Feeds live `party_kind` on every `lexical.build` |
| T5 | Negator | 7 | Feeds live `is_negator` |
| T6 | Connective | 6 | Reference only — actual connective-note mechanism lives in `verse_lexical_note` |
| T7 | Party-Divine | 44 | Feeds live `party_kind` |
| T8 | Party-Human | 1,787 | Feeds live `party_kind` |
| T9 | Party-Angelic | 6 | Feeds live `party_kind` |
| T10 | Places | 990 | |
| T11 | Corporate-Collective | 112 | Ethnic/tribal/national collective identity (Philistine, Jew, Levite...) |
| T12 | Objects-Artifacts | 271 | |
| T13 | Natural-World | 285 | |
| T14 | Body-Parts | 97 | |
| T15 | Calendar | 9 | Created this session — Hebrew month names, no prior home |

T4/T5/T7/T8/T9 are not just reference tags — they are read directly by `lexical.py:load_code_classes`/`load_mcode_strongs` on every Layer 1 build to compute the `is_negator` and `party_kind` columns. A word missing from these five clusters produces a wrong (`NULL`) value on those fields, not just a missing thematic tag — this was the finding that reframed the second half of this escalation (see §4).

---

## 4. How the pool closed — method summary

The untagged pool (words with zero cluster tag, despite live `role='content'` occurrences) went from ~7,810–8,268 to 0 in this session, escalation #1598, across phases A–O:

1. **A–F (manual, verse-checked reallocation):** T2/T3 pool triage, verb screening against the standing rule ("a verb only moves to T3 when not directly tied to a specific characteristic"), correcting several miscategorizations caught mid-batch (idolater vs. idol, etc.).
2. **Faculty-ontology retirement** (a parallel thread, not pool-closure): the 11-faculty catalogue (T3.1–T3.11 observation questions) was investigated for provenance and retired by researcher verdict — unrelated to clusters, noted here only because it shares the session.
3. **G–J (T-code party/place/collective sweep):** discovered `party_kind`/`is_negator` are live-computed from T4/5/7/8/9 membership (not the retired `resolved_sense` mechanism people originally worried about). Closed the proper-noun population via STEP's own TIP biographical-marker text (`strong_meaning_parsed`'s first sense row: "living at the time of..." = person, "A location..." = place, "People from/group..." = collective, "deity"/"angel" = divine/angelic) — a structurally-grounded method, not gloss-keyword guessing. 1,621 (Phase G) + 796 (Phase H) + 186 (Phase J) items placed this way.
4. **Family-expansion tool** (`iba/app/lib/clusterfamilyscan.py`, built this session): candidate generation via `strong_related` (shared Hebrew/Greek roots). Worked well for T10 Places (82% genuine hit rate after proper-noun filtering) but failed for M-code thematic fit (M08 Pride & Arrogance: ~10-15% genuine, the rest coincidental root-sharing — e.g. "in/on/among" surfacing as "related to" *mock* via an unrelated Greek root). **Abandoned for M-codes; kept as a place/party/collective candidate tool.**
5. **K–M (T-code structural pivot):** once M-code family-expansion was shown unreliable, pivoted the remaining pool to structural T-code homes using mechanically reliable signals instead of thematic guessing — verbs via `morph_code` (V/HV/AV) → T3; body-parts/nature/objects via closed-vocabulary gloss matching, individually reviewed (not blind substring accept — caught coincidental hits like "spear" riding a root-share with "camp", place-name compounds like "Field of Blood" riding "blood").
6. **N (direct M-code match):** a different, more reliable variant of gloss matching — checking a word's *own* gloss against a cluster's own definition, not a related word's. Applied to the adjective remainder; yield was low (17/630, ~2.7%) — confirming the remainder is genuinely non-thematic, not an under-mined seam.
7. **O (final T2 sweep):** researcher decision — route the genuine, non-thematic residual (4,294 strongs: ordinals, directionals, physical/material descriptors, generic vocabulary, plus the 233 items with no `strong_meaning_parsed` row at all) into the existing T2 bucket rather than invent a new catch-all code.

---

## 5. Live governance note for Layer 2 (T2 semantics)

Because Phase O routed a large, genuinely-diverse population into T2, a `cfg_method_rule` was filed (pending approval, escalation #1604) so Layer 2 does not treat T2 membership as a green light to skip a word:

> A T2 (Supplementary) cluster tag sets a code aside from the M/T thematic-cluster scaffold by default — it is NOT a signal that the code is irrelevant to any given verse. Layer 2 must still judge, per occurrence, whether a T2-tagged code is doing real interpretive work in THIS verse's specific context. When it does, that gets a note recorded, not a silent skip.

---

## 6. Open items

- **Pending config approvals** (non-blocking): #1599, #1600 (utility registrations), #1602 (`clusterfamilyscan.py` registration), #1604 (the T2 relevance rule above).
- **`H5799` (Azazel)** — STEP's own TIP text calls it "A male deity/angel," a genuine type ambiguity between T7/T9. Not decided; deferred to the researcher.
- **233 strongs with no `strong_meaning_parsed` row at all** (a subset of the 4,294 now in T2) — these have no lexicon data to classify from at all, only a bare `surface` translation. They're structurally homed now (T2), but a STEP backfill decision is still open if richer classification is ever wanted for them.
- **Family-expansion tool** (`clusterfamilyscan.py`) remains available and validated for place/party/collective candidate generation, not for M-code thematic work.

---

*Full phase-by-phase detail (JSON payloads + rationale) is filed alongside this report as `iba/docs/1598-phase-[a-o]-*-v1-20260908.{json,md}`.*
