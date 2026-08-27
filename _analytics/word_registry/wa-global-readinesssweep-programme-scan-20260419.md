# Readiness Sweep — Programme-Wide Assessment

| Field | Value |
| --- | --- |
| Scan date | 2026-04-19T20:31:40.200979+00:00 |
| Schema version | 3.10.0 (post-DBR) |
| Instruction | wa-global-readiness-sweep-instruction-v1_0-20260419.md |
| Mode | Read-only (phases R.A–R.H via pilot) |
| Registries scanned | 213 |

---

## 1. Programme Summary

**Total findings across programme:** 7,411

### By path

| Path | Count | Share | Description |
| --- | --- | --- | --- |
| 1 | 179 | 2.4% | Mechanical patch (CC can fix automatically) |
| 2 | 1,361 | 18.4% | Sub-process directive (re-extract / VC / DimReview) |
| 3 | 219 | 3.0% | Deferred to per-word Stage 1 |
| 4 | 5,422 | 73.2% | RESEARCHER_DECISION |
| 5 | 230 | 3.1% | Outstanding task — beyond CC skill |

### By phase

| Phase | Finding count | Focus |
| --- | --- | --- |
| R.A | 445 | Registry state (status, cluster, counts) |
| R.B | 3,914 | Term inventory (OWNER/XREF/deleted; three-number diagnostic) |
| R.D | 2,611 | Verse context groups (group_code, anchor count, dominant_subject) |
| R.E | 222 | Dimension assignments (NULL/AUTOMATED confidence, vocab drift) |
| R.G | 6 | Supporting term data (meaning parse, root, related) |
| R.H | 213 | Prose coverage (Session A/B/C/D sections) |

### Distribution of registries by findings count

| Bin | Registries |
| --- | --- |
| clean (≤2) | 5 |
| light (3–10) | 63 |
| moderate (11–30) | 75 |
| heavy (31–70) | 42 |
| critical (>70) | 28 |

---

## 2. Cluster Breakdown

Registries grouped by `cluster_assignment`; sorted by total findings per cluster.

| Cluster | Registries | Findings | Path 1 | Path 2 | Path 3 | Path 4 | Path 5 | Avg per registry |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| C02 | 14 | 917 | 8 | 175 | 15 | 699 | 20 | 65.5 |
| C01 | 6 | 587 | 11 | 75 | 6 | 483 | 12 | 97.8 |
| C06 | 8 | 513 | 6 | 104 | 8 | 387 | 8 | 64.1 |
| C15 | 9 | 509 | 5 | 60 | 9 | 426 | 9 | 56.6 |
| C05 | 10 | 502 | 5 | 52 | 10 | 422 | 13 | 50.2 |
| C04 | 7 | 497 | 1 | 132 | 7 | 349 | 8 | 71.0 |
| C17 | 10 | 440 | 32 | 151 | 11 | 235 | 11 | 44.0 |
| C07 | 10 | 419 | 4 | 96 | 10 | 299 | 10 | 41.9 |
| C03 | 9 | 329 | 4 | 80 | 9 | 227 | 9 | 36.6 |
| C14 | 10 | 306 | 10 | 52 | 10 | 224 | 10 | 30.6 |
| C16 | 10 | 278 | 12 | 52 | 12 | 192 | 10 | 27.8 |
| C20 | 7 | 266 | 31 | 67 | 7 | 154 | 7 | 38.0 |
| C11 | 10 | 246 | 14 | 26 | 10 | 186 | 10 | 24.6 |
| C10 | 11 | 227 | 3 | 16 | 12 | 185 | 11 | 20.6 |
| C08 | 11 | 222 | 3 | 35 | 11 | 162 | 11 | 20.2 |
| C12 | 10 | 211 | 8 | 28 | 10 | 155 | 10 | 21.1 |
| C19 | 11 | 209 | 5 | 16 | 11 | 166 | 11 | 19.0 |
| C09 | 10 | 205 | 1 | 24 | 10 | 160 | 10 | 20.5 |
| C13 | 9 | 201 | 12 | 63 | 9 | 108 | 9 | 22.3 |
| C18 | 7 | 149 | 1 | 35 | 8 | 98 | 7 | 21.3 |
| C22 | 16 | 134 | 2 | 21 | 16 | 79 | 16 | 8.4 |
| C21 | 8 | 44 | 1 | 1 | 8 | 26 | 8 | 5.5 |

---

## 3. Top 20 Registries by Findings (triage priority)

High-findings registries likely benefit most from pre-processing before the full sweep runs. Typical remediations:

- Many Path 2 (span filter / zero extraction) → re-extract + audit_word re-run
- Many Path 2 (NULL dimension / AUTOMATED confidence) → run Dimension Review on cluster
- Many Path 4 on group-level NULL dominant_subject → run Verse Context anchor pass

| no | word | cluster | VC | DimRev | SB status | OWN terms | Findings | P1 | P2 | P3 | P4 | P5 | Notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | desire | C04 | Complete | — | Verse Context Reset | 151 | 319 | 1 | 106 | 1 | 209 | 2 | NULL dim:5; AUTO conf:94 |
| 160 | thought | C02 | Complete | — | Verse Context Reset | 76 | 251 | 0 | 52 | 1 | 196 | 2 | AUTO conf:20 |
| 126 | purpose | C02 | Complete | — | Verse Context Reset | 83 | 245 | 0 | 73 | 1 | 169 | 2 | AUTO conf:14 |
| 4 | anger | C07 | Complete | — | Verse Context Reset | 104 | 216 | 2 | 71 | 1 | 141 | 1 | NULL dim:4; AUTO conf:66 |
| 61 | fear | C06 | Complete | — | Verse Context Reset | 91 | 200 | 1 | 32 | 1 | 165 | 1 | NULL dim:4; AUTO conf:87 |
| 146 | shame | C06 | Complete | — | Verse Context Reset | 83 | 171 | 4 | 56 | 1 | 109 | 1 | AUTO conf:34 |
| 163 | trust | C15 | Complete | — | Verse Context Reset | 21 | 155 | 0 | 15 | 1 | 138 | 1 | NULL dim:1; AUTO conf:12 |
| 183 | heart | C01 | Complete | — | Verse Context Reset | 49 | 155 | 1 | 26 | 1 | 125 | 2 | NULL dim:1; AUTO conf:8 |
| 42 | delight | C03 | Complete | — | Verse Context Reset | 75 | 153 | 0 | 46 | 1 | 105 | 1 | AUTO conf:40 |
| 51 | distress | C05 | Complete | — | Verse Context Reset | 78 | 136 | 2 | 7 | 1 | 125 | 1 | NULL dim:25; AUTO conf:89 |
| 112 | mind | C01 | Complete | — | Verse Context Reset | 105 | 136 | 7 | 4 | 1 | 122 | 2 | AUTO conf:2 |
| 173 | will | C14 | Complete | — | Verse Context Reset | 58 | 132 | 4 | 30 | 1 | 96 | 1 | NULL dim:7; AUTO conf:52 |
| 184 | spirit | C01 | Complete | Complete | Verse Context Reset | 45 | 132 | 1 | 32 | 1 | 96 | 2 |  |
| 117 | peace | C17 | Complete | Complete | Verse Context Reset | 93 | 126 | 6 | 40 | 2 | 77 | 1 |  |
| 197 | authority | C20 | Complete | Complete | Verse Context Reset | 132 | 118 | 7 | 41 | 1 | 68 | 1 |  |
| 23 | compassion | C17 | Complete | Complete | Verse Context Reset | 71 | 114 | 5 | 52 | 1 | 55 | 1 |  |
| 59 | faith | C15 | Complete | — | Verse Context Reset | 46 | 102 | 0 | 29 | 1 | 71 | 1 | AUTO conf:34 |
| 5 | anguish | C05 | Complete | — | Verse Context Reset | 62 | 95 | 1 | 20 | 1 | 72 | 1 | NULL dim:2; AUTO conf:48 |
| 78 | hope | C04 | Complete | — | Verse Context Reset | 42 | 94 | 0 | 17 | 1 | 75 | 1 | NULL dim:7; AUTO conf:39 |
| 52 | division | C18 | Complete | — | Verse Context Reset | 53 | 92 | 1 | 30 | 2 | 58 | 1 | NULL dim:5; AUTO conf:25 |

---

## 4. Pre-Process Recommendations

### 4.1 — Registries with probable span filter failure / zero extraction

Candidates for `audit_word` re-run (blocked on OT-DBR-001 until audit_word.py rewrite lands).

**86 registries affected**, involving 1,156 term-level Path 2 items total.

| no | word | cluster | affected terms |
| ---: | --- | --- | ---: |
| 43 | desire | C04 | 104 |
| 126 | purpose | C02 | 72 |
| 4 | anger | C07 | 69 |
| 146 | shame | C06 | 55 |
| 23 | compassion | C17 | 52 |
| 160 | thought | C02 | 51 |
| 42 | delight | C03 | 45 |
| 197 | authority | C20 | 41 |
| 117 | peace | C17 | 40 |
| 184 | spirit | C01 | 32 |
| 61 | fear | C06 | 30 |
| 34 | covenant | C17 | 28 |
| 52 | division | C18 | 28 |
| 59 | faith | C15 | 28 |
| 173 | will | C14 | 28 |
| 98 | justice | C13 | 26 |
| 103 | love | C17 | 25 |
| 183 | heart | C01 | 24 |
| 135 | repentance | C13 | 22 |
| 58 | experience | C22 | 19 |
| 5 | anguish | C05 | 18 |
| 187 | strength | C20 | 17 |
| 78 | hope | C04 | 15 |
| 156 | surrender | C14 | 15 |
| 1 | abomination | C12 | 14 |
| … 61 more | | | |

### 4.2 — Registries needing Dimension Review

NULL dimension OR non-reviewed confidence on multiple groups → benefit from Dimension Review pre-process (cluster-wide approach).

**104 registries affected**.

| no | word | cluster | NULL dim | AUTO conf | total |
| ---: | --- | --- | ---: | ---: | ---: |
| 51 | distress | C05 | 25 | 89 | 114 |
| 43 | desire | C04 | 5 | 94 | 99 |
| 61 | fear | C06 | 4 | 87 | 91 |
| 180 | yielding | C14 | 10 | 69 | 79 |
| 123 | pride | C09 | 13 | 59 | 72 |
| 4 | anger | C07 | 4 | 66 | 70 |
| 121 | praise | C15 | 10 | 50 | 60 |
| 173 | will | C14 | 7 | 52 | 59 |
| 213 | listen | C02 | 3 | 49 | 52 |
| 5 | anguish | C05 | 2 | 48 | 50 |
| 57 | evil | C11 | 4 | 46 | 50 |
| 78 | hope | C04 | 7 | 39 | 46 |
| 6 | anointing | C16 | 6 | 38 | 44 |
| 176 | worship | C15 | 7 | 37 | 44 |
| 33 | courage | C08 | 9 | 33 | 42 |
| 97 | joy | C03 | 1 | 40 | 41 |
| 174 | wisdom | C02 | 4 | 37 | 41 |
| 42 | delight | C03 | 0 | 40 | 40 |
| 151 | sorrow | C05 | 2 | 35 | 37 |
| 59 | faith | C15 | 0 | 34 | 34 |
| 90 | innocence | C10 | 1 | 33 | 34 |
| 146 | shame | C06 | 0 | 34 | 34 |
| 2 | agony | C05 | 4 | 29 | 33 |
| 56 | envy | C07 | 9 | 24 | 33 |
| 128 | rebellion | C09 | 4 | 28 | 32 |
| … 79 more | | | | | |

### 4.3 — Registries needing Verse Context completion

**34 registries** have `verse_context_status != 'Complete'`.

| no | word | cluster | VC status | SB status |
| ---: | --- | --- | --- | --- |
| 9 | assent | C22 | — | — |
| 10 | awareness | C22 | — | — |
| 12 | betrayal | C18 | — | — |
| 14 | blamelessness | C10 | — | — |
| 21 | commitment | C14 | — | — |
| 22 | communion | C17 | — | — |
| 25 | conformity | C14 | — | — |
| 27 | consciousness | C22 | — | Verse Context Reset |
| 36 | cowardice | C09 | — | — |
| 37 | darkening | C21 | — | — |
| 38 | deadness | C21 | — | — |
| 45 | determination | C14 | — | — |
| 54 | emotion | C22 | — | — |
| 68 | grace | C17 | In Progress | Verse Context Reset |
| 79 | hopelessness | C06 | — | — |
| 82 | identity | C19 | — | — |
| 84 | image of God | C19 | — | — |
| 88 | ingratitude | C22 | — | — |
| 95 | intuition | C22 | — | — |
| 101 | laziness | C09 | — | — |
| 106 | manipulation | C18 | — | — |
| 118 | personality | C22 | — | — |
| 119 | personhood | C19 | — | — |
| 129 | recognition | C22 | — | Verse Context Reset |
| 133 | reliability | C09 | — | — |
| … 9 more | | | | |

### 4.4 — Registries needing Dim Review completion (status flag)

**173 registries** have `dim_review_status != 'Complete'`.

Note: the dimensions extract (2026-04-19) showed 172 registries have actual dimension data; the status flag has lagged. Path 4 'hard gate' findings are predominantly this flag mismatch, not actual missing data. Bulk-status-update may be warranted if a sample confirms dimension data is present.

### 4.5 — Clean registries (ready for Stage 1 once OT-DBR-001 lands)

**5 registries** have ≤2 findings (just word_synopsis + Session A extract gaps, both deferred).

- **C13** (1): 35 covetousness
- **C17** (1): 62 fellowship
- **C21** (2): 134 renewal, 207 blindness (spiritual)
- **C22** (1): 206 vulnerability

---

## 5. Suggested Pre-Process Sequence

Based on the scan, the most efficient unlock sequence is:

1. **OT-DBR-001 rewrite (audit_word.py)** — unblocks Path 2 re-extraction directives across the programme.
2. **Bulk re-extraction for 86 registries** with span filter failure / zero extraction — reclaims hundreds of analytical term-verse rows.
3. **Dimension Review on 104 registries** — most via cluster-level batch (C01 legacy vocab also needs normalisation; see dimensions extract).
4. **Verse Context completion for 34 registries** — some are at 'In Progress' already (e.g. suffering r214).
5. **Dim Review status flag normalisation** — bulk patch setting `dim_review_status = 'Complete'` where `wa_dimension_index` has reviewed content (status flag has lagged the data).
6. **Session A extract generator** — unblocks prose coverage Path 5 for all 213 registries.

Completing 1–5 would likely **drop programme findings count by 60–80%** and place a sizable cohort at 'ready for Stage 1' state.

---

## 6. Per-Registry Detail (full list)

Sorted by total findings descending. Full raw data in `wa-global-readinesssweep-programme-scan-raw-{date}.json`.

| no | word | cluster | VC | DimRev | SB status | OWN | XREF | V | G | Dim | ΣF | P1 | P2 | P3 | P4 | P5 |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | desire | C04 | Complete | — | Verse Context Re | 151 | 48 | 1409 | 97 | 97 | 319 | 1 | 106 | 1 | 209 | 2 |
| 160 | thought | C02 | Complete | — | Verse Context Re | 76 | 166 | 501 | 27 | 27 | 251 | 0 | 52 | 1 | 196 | 2 |
| 126 | purpose | C02 | Complete | — | Verse Context Re | 83 | 128 | 400 | 16 | 16 | 245 | 0 | 73 | 1 | 169 | 2 |
| 4 | anger | C07 | Complete | — | Verse Context Re | 104 | 6 | 823 | 66 | 66 | 216 | 2 | 71 | 1 | 141 | 1 |
| 61 | fear | C06 | Complete | — | Verse Context Re | 91 | 69 | 662 | 87 | 87 | 200 | 1 | 32 | 1 | 165 | 1 |
| 146 | shame | C06 | Complete | — | Verse Context Re | 83 | 28 | 435 | 34 | 34 | 171 | 4 | 56 | 1 | 109 | 1 |
| 163 | trust | C15 | Complete | — | Verse Context Re | 21 | 152 | 127 | 12 | 12 | 155 | 0 | 15 | 1 | 138 | 1 |
| 183 | heart | C01 | Complete | — | Verse Context Re | 49 | 96 | 814 | 59 | 59 | 155 | 1 | 26 | 1 | 125 | 2 |
| 42 | delight | C03 | Complete | — | Verse Context Re | 75 | 51 | 329 | 40 | 40 | 153 | 0 | 46 | 1 | 105 | 1 |
| 51 | distress | C05 | Complete | — | Verse Context Re | 78 | 85 | 1184 | 89 | 89 | 136 | 2 | 7 | 1 | 125 | 1 |
| 112 | mind | C01 | Complete | — | Verse Context Re | 105 | 21 | 826 | 73 | 73 | 136 | 7 | 4 | 1 | 122 | 2 |
| 173 | will | C14 | Complete | — | Verse Context Re | 58 | 53 | 1635 | 52 | 52 | 132 | 4 | 30 | 1 | 96 | 1 |
| 184 | spirit | C01 | Complete | Complete | Verse Context Re | 45 | 63 | 342 | 37 | 37 | 132 | 1 | 32 | 1 | 96 | 2 |
| 117 | peace | C17 | Complete | Complete | Verse Context Re | 93 | 32 | 1462 | 69 | 69 | 126 | 6 | 40 | 2 | 77 | 1 |
| 197 | authority | C20 | Complete | Complete | Verse Context Re | 132 | 35 | 1943 | 84 | 84 | 118 | 7 | 41 | 1 | 68 | 1 |
| 23 | compassion | C17 | Complete | Complete | Verse Context Re | 71 | 26 | 351 | 22 | 22 | 114 | 5 | 52 | 1 | 55 | 1 |
| 59 | faith | C15 | Complete | — | Verse Context Re | 46 | 25 | 549 | 34 | 34 | 102 | 0 | 29 | 1 | 71 | 1 |
| 5 | anguish | C05 | Complete | — | Verse Context Re | 62 | 69 | 735 | 48 | 48 | 95 | 1 | 20 | 1 | 72 | 1 |
| 78 | hope | C04 | Complete | — | Verse Context Re | 42 | 22 | 493 | 39 | 39 | 94 | 0 | 17 | 1 | 75 | 1 |
| 52 | division | C18 | Complete | — | Verse Context Re | 53 | 4 | 395 | 25 | 25 | 92 | 1 | 30 | 2 | 58 | 1 |
| 212 | pray | C15 | Complete | — | Verse Context Re | 5 | 101 | 14 | 2 | 2 | 83 | 0 | 5 | 1 | 76 | 1 |
| 180 | yielding | C14 | Complete | — | Verse Context Re | 24 | 2 | 589 | 69 | 69 | 79 | 4 | 2 | 1 | 71 | 1 |
| 123 | pride | C09 | Complete | — | Verse Context Re | 56 | 8 | 808 | 59 | 59 | 78 | 0 | 7 | 1 | 69 | 1 |
| 213 | listen | C02 | Complete | — | Verse Context Re | 38 | 25 | 2894 | 49 | 49 | 78 | 3 | 4 | 1 | 69 | 1 |
| 34 | covenant | C17 | Complete | Complete | Verse Context Re | 44 | 16 | 638 | 32 | 32 | 74 | 3 | 28 | 1 | 41 | 1 |
| 151 | sorrow | C05 | Complete | — | Verse Context Re | 48 | 118 | 674 | 35 | 35 | 73 | 0 | 2 | 1 | 69 | 1 |
| 71 | grief | C05 | Complete | — | Verse Context Re | 30 | 56 | 212 | 21 | 21 | 71 | 1 | 13 | 1 | 55 | 1 |
| 103 | love | C17 | Complete | Complete | Verse Context Re | 81 | 59 | 1156 | 67 | 66 | 71 | 7 | 25 | 1 | 37 | 1 |
| 182 | Soul | C01 | Complete | Complete | Verse Context Re | 20 | 4 | 752 | 61 | 61 | 68 | 1 | 1 | 1 | 63 | 2 |
| 185 | flesh | C01 | Complete | Complete | Verse Context Re | 23 | 34 | 661 | 30 | 30 | 68 | 0 | 9 | 1 | 56 | 2 |
| 97 | joy | C03 | Complete | — | Verse Context Re | 39 | 10 | 628 | 40 | 40 | 67 | 1 | 11 | 1 | 53 | 1 |
| 57 | evil | C11 | Complete | — | Verse Context Re | 27 | 11 | 1303 | 46 | 46 | 65 | 8 | 3 | 1 | 52 | 1 |
| 98 | justice | C13 | Complete | Complete | Verse Context Re | 60 | 27 | 877 | 50 | 50 | 65 | 5 | 26 | 1 | 32 | 1 |
| 1 | abomination | C12 | Complete | — | Verse Context Re | 30 | 3 | 227 | 26 | 26 | 61 | 2 | 16 | 1 | 41 | 1 |
| 121 | praise | C15 | Complete | — | Verse Context Re | 35 | 25 | 783 | 50 | 50 | 59 | 2 | 2 | 1 | 53 | 1 |
| 33 | courage | C08 | Complete | — | Verse Context Re | 34 | 23 | 625 | 33 | 33 | 57 | 0 | 11 | 1 | 44 | 1 |
| 56 | envy | C07 | Complete | — | Verse Context Re | 28 | 2 | 212 | 24 | 24 | 57 | 1 | 16 | 1 | 38 | 1 |
| 174 | wisdom | C02 | Complete | — | Verse Context Re | 24 | 20 | 462 | 37 | 37 | 57 | 1 | 2 | 1 | 52 | 1 |
| 2 | agony | C05 | Complete | — | Verse Context Re | 35 | 17 | 119 | 29 | 29 | 55 | 0 | 8 | 1 | 45 | 1 |
| 187 | strength | C20 | Complete | Complete | Verse Context Re | 186 | 112 | 3540 | 200 | 200 | 55 | 11 | 17 | 1 | 25 | 1 |
| 6 | anointing | C16 | Complete | — | Verse Context Re | 53 | 1 | 735 | 38 | 38 | 52 | 3 | 5 | 2 | 41 | 1 |
| 100 | knowledge | C02 | Complete | — | Verse Context Re | 11 | 23 | 658 | 25 | 25 | 51 | 1 | 4 | 1 | 44 | 1 |
| 178 | wrath | C07 | Complete | — | Verse Context Re | 9 | 61 | 141 | 11 | 11 | 50 | 0 | 2 | 1 | 46 | 1 |
| 135 | repentance | C13 | Complete | Complete | Verse Context Re | 33 | 6 | 253 | 14 | 14 | 47 | 0 | 22 | 1 | 23 | 1 |
| 67 | goodness | C10 | Complete | — | Verse Context Re | 3 | 42 | 317 | 9 | 9 | 46 | 0 | 1 | 1 | 43 | 1 |
| 176 | worship | C15 | Complete | — | Verse Context Re | 31 | 3 | 718 | 37 | 37 | 46 | 2 | 3 | 1 | 39 | 1 |
| 44 | despair | C06 | Complete | — | Verse Context Re | 21 | 9 | 1002 | 26 | 26 | 44 | 1 | 8 | 1 | 33 | 1 |
| 199 | dominion | C20 | Complete | Complete | Verse Context Re | 40 | 63 | 454 | 41 | 41 | 43 | 6 | 9 | 1 | 26 | 1 |
| 47 | dignity | C19 | Complete | — | Verse Context Re | 7 | 32 | 85 | 9 | 9 | 42 | 0 | 2 | 1 | 38 | 1 |
| 58 | experience | C22 | Complete | Complete | Verse Context Re | 23 | 1 | 297 | 16 | 16 | 42 | 1 | 19 | 1 | 20 | 1 |
| 73 | guilt | C13 | Complete | Complete | Verse Context Re | 23 | 47 | 1064 | 30 | 30 | 40 | 3 | 1 | 1 | 34 | 1 |
| 90 | innocence | C10 | Complete | — | Verse Context Re | 23 | 4 | 812 | 33 | 33 | 40 | 0 | 3 | 1 | 35 | 1 |
| 49 | discernment | C02 | Complete | — | Verse Context Re | 20 | 12 | 55 | 7 | 7 | 39 | 1 | 15 | 1 | 21 | 1 |
| 108 | meditation | C02 | Complete | — | Verse Context Re | 5 | 34 | 22 | 5 | 5 | 39 | 0 | 1 | 1 | 36 | 1 |
| 83 | idolatry | C16 | Complete | — | Verse Context Re | 19 | 1 | 34 | 7 | 7 | 38 | 1 | 14 | 1 | 21 | 1 |
| 166 | understanding | C02 | Complete | — | Verse Context Re | 7 | 32 | 267 | 12 | 12 | 38 | 1 | 1 | 1 | 34 | 1 |
| 19 | calling | C19 | Complete | — | Verse Context Re | 28 | 1 | 1195 | 24 | 24 | 37 | 4 | 4 | 1 | 27 | 1 |
| 149 | slander | C12 | Complete | — | Verse Context Re | 17 | 20 | 313 | 16 | 16 | 37 | 0 | 1 | 1 | 34 | 1 |
| 156 | surrender | C14 | Complete | — | Verse Context Re | 27 | 2 | 1146 | 1 | 1 | 37 | 0 | 16 | 1 | 19 | 1 |
| 28 | consecration | C16 | Complete | — | Verse Context Re | 26 | 4 | 326 | 17 | 17 | 36 | 0 | 8 | 2 | 25 | 1 |
| 116 | patience | C08 | Complete | — | Verse Context Re | 19 | 7 | 248 | 14 | 14 | 36 | 0 | 10 | 1 | 24 | 1 |
| 159 | testimony | C16 | Complete | — | Verse Context Re | 20 | 1 | 277 | 8 | 8 | 36 | 1 | 13 | 1 | 20 | 1 |
| 177 | worth | C19 | Complete | — | Verse Context Re | 16 | 17 | 272 | 26 | 26 | 36 | 0 | 3 | 1 | 31 | 1 |
| 128 | rebellion | C09 | Complete | — | Verse Context Re | 21 | 4 | 485 | 28 | 28 | 35 | 0 | 3 | 1 | 30 | 1 |
| 190 | contempt | C06 | Complete | — | Verse Context Re | 11 | 22 | 127 | 13 | 13 | 34 | 0 | 1 | 1 | 31 | 1 |
| 198 | might | C20 | Complete | Complete | Verse Context Re | 22 | 49 | 881 | 24 | 24 | 34 | 6 | 0 | 1 | 26 | 1 |
| 11 | awe | C03 | Complete | — | Verse Context Re | 16 | 14 | 506 | 13 | 13 | 33 | 1 | 9 | 1 | 21 | 1 |
| 26 | conscience | C13 | Complete | Complete | Verse Context Re | 21 | 8 | 62 | 8 | 8 | 33 | 1 | 13 | 1 | 17 | 1 |
| 32 | counsel | C02 | Complete | — | Verse Context Re | 12 | 4 | 345 | 25 | 25 | 32 | 1 | 2 | 1 | 26 | 2 |
| 127 | reasoning | C02 | Complete | — | Verse Context Re | 14 | 1 | 33 | 4 | 4 | 31 | 0 | 12 | 1 | 16 | 2 |
| 111 | mercy | C17 | Complete | Complete | Verse Context Re | 31 | 34 | 595 | 36 | 36 | 30 | 8 | 6 | 1 | 14 | 1 |
| 86 | impurity | C12 | Complete | — | Verse Context Re | 15 | 0 | 438 | 18 | 18 | 28 | 3 | 3 | 1 | 20 | 1 |
| 162 | transgression | C11 | Complete | — | Verse Context Re | 16 | 12 | 91 | 8 | 8 | 28 | 0 | 9 | 1 | 17 | 1 |
| 211 | being | C01 | Complete | Complete | Verse Context Re | 18 | 42 | 75 | 15 | 15 | 28 | 1 | 3 | 1 | 21 | 2 |
| 191 | doubt | C16 | Complete | — | Verse Context Re | 17 | 17 | 157 | 17 | 17 | 27 | 1 | 1 | 1 | 23 | 1 |
| 80 | humility | C08 | Complete | — | Verse Context Re | 12 | 9 | 97 | 16 | 16 | 26 | 2 | 2 | 1 | 20 | 1 |
| 124 | prophecy | C16 | Complete | — | Verse Context Re | 10 | 1 | 253 | 19 | 19 | 26 | 2 | 2 | 1 | 20 | 1 |
| 125 | purity | C10 | Complete | — | Verse Context Re | 12 | 0 | 206 | 20 | 20 | 26 | 1 | 2 | 1 | 21 | 1 |
| 91 | insight | C02 | Complete | — | Verse Context Re | 3 | 24 | 163 | 5 | 5 | 25 | 0 | 2 | 2 | 20 | 1 |
| 102 | longing | C04 | Complete | — | Verse Context Re | 15 | 9 | 242 | 17 | 17 | 25 | 0 | 2 | 1 | 21 | 1 |
| 147 | sin | C11 | Complete | — | Verse Context Re | 12 | 13 | 299 | 17 | 17 | 25 | 2 | 2 | 1 | 19 | 1 |
| 168 | uprightness | C10 | Complete | — | Verse Context Re | 9 | 2 | 180 | 18 | 18 | 25 | 0 | 2 | 2 | 20 | 1 |
| 31 | corruption | C11 | Complete | — | Verse Context Re | 18 | 0 | 255 | 15 | 15 | 24 | 2 | 3 | 1 | 17 | 1 |
| 140 | seeking | C15 | Complete | — | Verse Context Re | 7 | 9 | 697 | 13 | 13 | 24 | 1 | 1 | 1 | 20 | 1 |
| 142 | self-control | C08 | Complete | — | Verse Context Re | 14 | 8 | 293 | 15 | 15 | 24 | 0 | 2 | 1 | 20 | 1 |
| 172 | wickedness | C11 | Complete | — | Verse Context Re | 5 | 20 | 274 | 14 | 14 | 24 | 1 | 2 | 1 | 19 | 1 |
| 17 | bondage | C14 | Complete | — | Verse Context Re | 8 | 0 | 158 | 16 | 16 | 23 | 2 | 2 | 1 | 17 | 1 |
| 105 | lust | C12 | Complete | — | Verse Context Re | 6 | 26 | 59 | 6 | 6 | 23 | 1 | 2 | 1 | 18 | 1 |
| 122 | prayer | C15 | Complete | — | Verse Context Re | 7 | 9 | 164 | 11 | 11 | 23 | 0 | 2 | 1 | 19 | 1 |
| 204 | name | C19 | Complete | — | Verse Context Re | 3 | 3 | 495 | 14 | 14 | 23 | 1 | 2 | 1 | 18 | 1 |
| 13 | bitterness | C07 | Complete | — | Verse Context Re | 11 | 9 | 333 | 11 | 11 | 22 | 1 | 1 | 1 | 18 | 1 |
| 40 | deceit | C11 | Complete | — | Verse Context Re | 17 | 0 | 273 | 17 | 17 | 22 | 1 | 1 | 1 | 18 | 1 |
| 7 | anxiety | C06 | Complete | — | Verse Context Re | 10 | 5 | 52 | 15 | 15 | 21 | 0 | 2 | 1 | 17 | 1 |
| 76 | holiness | C16 | Complete | — | Verse Context Re | 10 | 15 | 418 | 11 | 11 | 21 | 2 | 3 | 1 | 14 | 1 |
| 120 | perverseness | C11 | Complete | — | Verse Context Re | 16 | 0 | 146 | 16 | 16 | 21 | 0 | 2 | 1 | 17 | 1 |
| 193 | craving | C04 | Complete | — | Verse Context Re | 4 | 24 | 13 | 3 | 3 | 21 | 0 | 3 | 1 | 16 | 1 |
| 53 | dread | C06 | Complete | — | Verse Context Re | 7 | 9 | 111 | 9 | 9 | 20 | 0 | 3 | 1 | 15 | 1 |
| 107 | meaning | C19 | Complete | — | Verse Context Re | 12 | 13 | 53 | 10 | 10 | 20 | 0 | 3 | 1 | 15 | 1 |
| 129 | recognition | C22 | — | — | Verse Context Re | 0 | 23 | 0 | 0 | 0 | 20 | 0 | 0 | 1 | 18 | 1 |
| 15 | boastfulness | C09 | Complete | — | Verse Context Re | 9 | 1 | 249 | 13 | 13 | 19 | 0 | 2 | 1 | 15 | 1 |
| 152 | strife | C18 | Complete | — | Verse Context Re | 10 | 17 | 73 | 9 | 9 | 19 | 0 | 1 | 1 | 16 | 1 |
| 181 | zeal | C07 | Complete | — | Verse Context Re | 3 | 21 | 25 | 5 | 5 | 19 | 0 | 2 | 1 | 15 | 1 |
| 194 | blessing | C16 | Complete | — | Verse Context Re | 4 | 9 | 306 | 9 | 9 | 19 | 1 | 2 | 1 | 14 | 1 |
| 208 | sloth | C09 | Complete | — | Verse Context Re | 7 | 4 | 67 | 11 | 11 | 19 | 0 | 2 | 1 | 15 | 1 |
| 60 | faithfulness | C10 | Complete | — | Verse Context Re | 1 | 28 | 242 | 7 | 7 | 18 | 1 | 1 | 1 | 14 | 1 |
| 72 | groaning | C05 | Complete | — | Verse Context Re | 10 | 2 | 71 | 13 | 13 | 18 | 0 | 2 | 1 | 14 | 1 |
| 89 | iniquity | C11 | Complete | — | Verse Context Re | 9 | 12 | 375 | 14 | 14 | 18 | 0 | 1 | 1 | 15 | 1 |
| 158 | terror | C06 | Complete | — | Verse Context Re | 11 | 25 | 76 | 8 | 8 | 18 | 0 | 2 | 1 | 14 | 1 |
| 8 | appetite | C04 | Complete | — | Verse Context Re | 11 | 10 | 1122 | 12 | 12 | 17 | 0 | 1 | 1 | 14 | 1 |
| 65 | generosity | C08 | Complete | — | Verse Context Re | 6 | 27 | 103 | 10 | 10 | 17 | 1 | 1 | 1 | 13 | 1 |
| 66 | gentleness | C08 | Complete | — | Verse Context Re | 7 | 8 | 91 | 8 | 8 | 17 | 0 | 3 | 1 | 12 | 1 |
| 139 | righteousness | C10 | Complete | — | Verse Context Re | 1 | 33 | 10 | 1 | 1 | 17 | 1 | 1 | 1 | 13 | 1 |
| 157 | temptation | C12 | Complete | — | Verse Context Re | 15 | 2 | 85 | 12 | 12 | 17 | 1 | 1 | 1 | 13 | 1 |
| 214 | suffering | C05 | In Progr | — | Ready for Analys | 0 | 0 | 907 | 12 | 0 | 17 | 0 | 0 | 1 | 15 | 1 |
| 29 | contentment | C03 | Complete | — | Verse Context Re | 6 | 2 | 3 | 2 | 2 | 16 | 0 | 5 | 1 | 9 | 1 |
| 92 | integrity | C10 | Complete | — | Verse Context Re | 3 | 16 | 62 | 5 | 5 | 16 | 0 | 1 | 1 | 13 | 1 |
| 115 | passion | C04 | Complete | — | Verse Context Re | 4 | 14 | 6 | 3 | 3 | 16 | 0 | 2 | 1 | 12 | 1 |
| 201 | image | C19 | Complete | — | Verse Context Re | 8 | 1 | 79 | 12 | 12 | 16 | 0 | 1 | 1 | 13 | 1 |
| 87 | indignation | C07 | Complete | — | Verse Context Re | 2 | 15 | 4 | 2 | 2 | 15 | 0 | 1 | 1 | 12 | 1 |
| 96 | jealousy | C07 | Complete | — | Verse Context Re | 1 | 21 | 4 | 2 | 2 | 15 | 0 | 1 | 1 | 12 | 1 |
| 113 | mourning | C05 | Complete | Complete | Verse Context Re | 10 | 6 | 60 | 11 | 11 | 15 | 1 | 0 | 1 | 11 | 2 |
| 164 | truthfulness | C10 | Complete | — | Verse Context Re | 5 | 0 | 161 | 10 | 10 | 15 | 0 | 2 | 1 | 11 | 1 |
| 167 | unity | C18 | Complete | — | Verse Context Re | 7 | 0 | 562 | 10 | 10 | 15 | 0 | 2 | 1 | 11 | 1 |
| 170 | weakness | C09 | Complete | — | Verse Context Re | 8 | 0 | 81 | 9 | 9 | 15 | 1 | 2 | 1 | 10 | 1 |
| 175 | wonder | C03 | Complete | — | Verse Context Re | 8 | 5 | 269 | 8 | 8 | 15 | 1 | 2 | 1 | 10 | 1 |
| 186 | gladness | C03 | Complete | — | Verse Context Re | 6 | 0 | 129 | 8 | 8 | 15 | 1 | 3 | 1 | 9 | 1 |
| 209 | likeness | C19 | Complete | — | Verse Context Re | 2 | 21 | 3 | 2 | 2 | 15 | 0 | 1 | 1 | 12 | 1 |
| 39 | debauchery | C12 | Complete | — | Verse Context Re | 5 | 1 | 132 | 8 | 8 | 14 | 1 | 2 | 1 | 9 | 1 |
| 16 | boldness | C08 | Complete | — | Verse Context Re | 6 | 3 | 43 | 7 | 7 | 13 | 0 | 2 | 1 | 9 | 1 |
| 77 | honesty | C10 | Complete | — | Verse Context Re | 3 | 3 | 332 | 6 | 6 | 13 | 0 | 2 | 1 | 9 | 1 |
| 94 | intercession | C15 | Complete | — | Verse Context Re | 6 | 1 | 61 | 5 | 5 | 13 | 0 | 3 | 1 | 8 | 1 |
| 165 | unbelief | C16 | Complete | — | Verse Context Re | 3 | 11 | 30 | 5 | 5 | 13 | 1 | 2 | 1 | 8 | 1 |
| 188 | weeping | C05 | Complete | Complete | Verse Context Re | 9 | 3 | 165 | 10 | 10 | 13 | 0 | 0 | 1 | 10 | 2 |
| 46 | devotion | C08 | Complete | — | Verse Context Re | 5 | 8 | 13 | 6 | 6 | 12 | 0 | 2 | 1 | 8 | 1 |
| 74 | hardness | C09 | Complete | — | Verse Context Re | 9 | 6 | 21 | 2 | 2 | 12 | 0 | 4 | 1 | 6 | 1 |
| 85 | imagination | C02 | Complete | — | Verse Context Re | 5 | 1 | 13 | 3 | 3 | 12 | 0 | 3 | 1 | 7 | 1 |
| 110 | memory | C02 | Complete | — | Verse Context Re | 4 | 5 | 26 | 3 | 3 | 12 | 0 | 3 | 1 | 6 | 2 |
| 132 | rejoicing | C03 | Complete | — | Verse Context Re | 2 | 12 | 1 | 1 | 1 | 12 | 0 | 2 | 1 | 8 | 1 |
| 153 | stubbornness | C09 | Complete | — | Verse Context Re | 7 | 3 | 13 | 2 | 2 | 12 | 0 | 4 | 1 | 6 | 1 |
| 75 | hatred | C07 | Complete | — | Verse Context Re | 5 | 2 | 26 | 6 | 6 | 11 | 0 | 2 | 1 | 7 | 1 |
| 81 | hypocrisy | C11 | Complete | — | Verse Context Re | 5 | 0 | 31 | 6 | 6 | 11 | 0 | 2 | 1 | 7 | 1 |
| 171 | whoredom | C12 | Complete | — | Verse Context Re | 3 | 1 | 102 | 7 | 7 | 11 | 0 | 1 | 1 | 8 | 1 |
| 189 | malice | C12 | Complete | — | Verse Context Re | 1 | 15 | 3 | 1 | 1 | 11 | 0 | 1 | 1 | 8 | 1 |
| 192 | comfort | C03 | Complete | — | Verse Context Re | 5 | 10 | 37 | 7 | 7 | 11 | 0 | 1 | 1 | 8 | 1 |
| 202 | transformation | C21 | Complete | Complete | Verse Context Re | 3 | 24 | 32 | 7 | 7 | 11 | 0 | 0 | 1 | 9 | 1 |
| 150 | sorcery | C16 | Complete | — | Verse Context Re | 5 | 0 | 15 | 4 | 4 | 10 | 0 | 2 | 1 | 6 | 1 |
| 18 | brokenness | C05 | Complete | Complete | Verse Context Re | 7 | 2 | 82 | 6 | 6 | 9 | 0 | 0 | 1 | 6 | 2 |
| 55 | endurance | C08 | Complete | — | Verse Context Re | 4 | 2 | 110 | 5 | 5 | 9 | 0 | 1 | 1 | 6 | 1 |
| 205 | resentment | C07 | Complete | — | Verse Context Re | 0 | 16 | 0 | 0 | 0 | 9 | 0 | 0 | 1 | 7 | 1 |
| 99 | kindness | C17 | Complete | Complete | Verse Context Re | 23 | 38 | 2017 | 28 | 28 | 8 | 2 | 0 | 1 | 4 | 1 |
| 131 | rejection | C18 | Complete | — | Verse Context Re | 3 | 0 | 5 | 2 | 2 | 8 | 0 | 2 | 1 | 4 | 1 |
| 196 | power | C20 | Complete | Complete | Verse Context Re | 14 | 47 | 422 | 21 | 21 | 8 | 1 | 0 | 1 | 5 | 1 |
| 203 | treachery | C11 | Complete | — | Verse Context Re | 1 | 15 | 3 | 1 | 1 | 8 | 0 | 1 | 1 | 5 | 1 |
| 3 | ambition | C22 | Complete | Complete | Verse Context Re | 10 | 19 | 20 | 11 | 11 | 7 | 0 | 2 | 1 | 3 | 1 |
| 69 | gratitude | C03 | Complete | — | Verse Context Re | 3 | 0 | 54 | 3 | 3 | 7 | 0 | 1 | 1 | 4 | 1 |
| 93 | intention | C02 | Complete | Complete | Verse Context Re | 2 | 3 | 9 | 2 | 2 | 7 | 0 | 1 | 1 | 3 | 2 |
| 114 | obedience | C14 | Complete | — | Verse Context Re | 2 | 0 | 16 | 3 | 3 | 7 | 0 | 1 | 1 | 4 | 1 |
| 9 | assent | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 21 | commitment | C14 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 25 | conformity | C14 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 37 | darkening | C21 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 38 | deadness | C21 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 41 | defilement | C12 | Complete | — | Verse Context Re | 2 | 0 | 4 | 2 | 2 | 6 | 0 | 1 | 1 | 3 | 1 |
| 54 | emotion | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 68 | grace | C17 | In Progr | Complete | Verse Context Re | 5 | 8 | 226 | 11 | 11 | 6 | 0 | 0 | 1 | 4 | 1 |
| 88 | ingratitude | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 95 | intuition | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 106 | manipulation | C18 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 109 | meekness | C08 | Complete | — | Verse Context Re | 0 | 13 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 118 | personality | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 143 | sensitivity | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 145 | sexuality | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 148 | sincerity | C10 | Complete | — | Verse Context Re | 2 | 13 | 5 | 2 | 2 | 6 | 0 | 1 | 1 | 3 | 1 |
| 154 | stupor | C21 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 155 | submission | C14 | Complete | — | Verse Context Re | 2 | 0 | 36 | 2 | 2 | 6 | 0 | 1 | 1 | 3 | 1 |
| 161 | transformation | C21 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 169 | vulnerability | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 4 | 1 |
| 10 | awareness | C22 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 12 | betrayal | C18 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 14 | blamelessness | C10 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 22 | communion | C17 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 36 | cowardice | C09 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 45 | determination | C14 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 48 | diligence | C08 | Complete | — | Verse Context Re | 7 | 1 | 82 | 0 | 0 | 5 | 0 | 1 | 1 | 2 | 1 |
| 79 | hopelessness | C06 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 82 | identity | C19 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 84 | image of God | C19 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 101 | laziness | C09 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 119 | personhood | C19 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 133 | reliability | C09 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 136 | resentment | C07 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 137 | resolve | C14 | Complete | — | Verse Context Re | 0 | 4 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 141 | self-awareness | C19 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 179 | yearning | C04 | Complete | — | Verse Context Re | 1 | 3 | 1 | 1 | 1 | 5 | 0 | 1 | 1 | 2 | 1 |
| 195 | spiritual powers | C20 | — | — | — | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 1 |
| 210 | deadness | C21 | Complete | Complete | Verse Context Re | 13 | 0 | 690 | 22 | 22 | 5 | 1 | 1 | 1 | 1 | 1 |
| 27 | consciousness | C22 | — | — | Verse Context Re | 0 | 2 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 2 | 1 |
| 50 | disobedience | C13 | Complete | Complete | Verse Context Re | 4 | 1 | 11 | 4 | 4 | 4 | 0 | 1 | 1 | 1 | 1 |
| 64 | forgiveness | C17 | Complete | Complete | Verse Context Re | 7 | 0 | 190 | 14 | 14 | 4 | 1 | 0 | 1 | 0 | 2 |
| 70 | greed | C13 | Complete | Complete | Verse Context Re | 3 | 11 | 20 | 4 | 4 | 4 | 1 | 0 | 1 | 1 | 1 |
| 104 | loyalty | C18 | Complete | — | Verse Context Re | 0 | 6 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 2 | 1 |
| 138 | reverence | C15 | Complete | — | Verse Context Re | 0 | 20 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 2 | 1 |
| 20 | character | C22 | Complete | Complete | Verse Context Re | 4 | 0 | 36 | 5 | 5 | 3 | 0 | 0 | 1 | 1 | 1 |
| 24 | condemnation | C13 | Complete | Complete | Verse Context Re | 13 | 5 | 251 | 10 | 10 | 3 | 1 | 0 | 1 | 0 | 1 |
| 30 | contrition | C13 | Complete | Complete | Ready for Analys | 10 | 3 | 55 | 9 | 9 | 3 | 1 | 0 | 1 | 0 | 1 |
| 63 | foolishness | C22 | Complete | Complete | Verse Context Re | 12 | 0 | 100 | 19 | 19 | 3 | 1 | 0 | 1 | 0 | 1 |
| 144 | sensuality | C12 | Complete | — | Verse Context Re | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 1 | 1 |
| 200 | energy | C20 | Complete | — | Verse Context Re | 0 | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 1 | 1 |
| 35 | covetousness | C13 | Complete | Complete | Verse Context Re | 7 | 4 | 25 | 10 | 10 | 2 | 0 | 0 | 1 | 0 | 1 |
| 62 | fellowship | C17 | Complete | Complete | Verse Context Re | 13 | 0 | 89 | 19 | 19 | 2 | 0 | 0 | 1 | 0 | 1 |
| 134 | renewal | C21 | Complete | Complete | Verse Context Re | 7 | 3 | 22 | 5 | 5 | 2 | 0 | 0 | 1 | 0 | 1 |
| 206 | vulnerability | C22 | Complete | Complete | Verse Context Re | 17 | 1 | 128 | 34 | 34 | 2 | 0 | 0 | 1 | 0 | 1 |
| 207 | blindness (spiritual) | C21 | Complete | Complete | Verse Context Re | 7 | 2 | 103 | 12 | 12 | 2 | 0 | 0 | 1 | 0 | 1 |

---

*End of programme-wide scan — 2026-04-19*