# Programme Readiness Scorecard v2 (post OT-DBR-010 fix) — 2026-04-19

| Field | Value |
| --- | --- |
| Produced | 2026-04-19T20:32:57.616812+00:00 |
| Source scan | re-run after OT-DBR-010 XREF join fix |
| Instruction | `wa-global-readiness-sweep-instruction-v1_0-20260419.md` §8 F2 |
| Schema version | 3.10.0 |
| Total registries | 213 (carry_forward=1) |
| Supersedes | `wa-global-readiness-scorecard-20260419.md` (v1) |

---

## Impact of OT-DBR-010 fix

The pilot's XREF join filter was corrected to check for canonical `mti_terms` rows rather than naive `strongs_number` match (which conflated against the ~3,600 duplicate rows). Result:

| Metric | Pre-fix | Post-fix | Change |
| --- | ---: | ---: | ---: |
| Total findings | 14,284 | 7,411 | **−48%** |
| Path 1 (mechanical) | 6,398 | **179** | **−97%** |
| Path 2 (sub-process) | 1,361 | 1,361 | unchanged (correct) |
| Path 3 (deferred) | 219 | 219 | unchanged |
| Path 4 (RD) | 6,076 | 5,422 | −11% |
| Path 5 (outstanding) | 230 | 230 | unchanged |
| Clean registries (≤2 findings) | 1 | 5 | +400% |

The ~6,200 eliminated Path 1 findings were spurious — they were flagging deprecated `mti_terms` duplicate rows for `xref_*` status fixes that would have corrupted data.

---

## Programme Summary (post-fix)

| Tier | Count | Share | Meaning |
| --- | ---: | ---: | --- |
| **BANKED** | 5 | 2.3% | BANKED — ready for Stage 1 (once Session A extract + word_synopsis land) |
| **STRUCTURALLY_CLEAN** | 12 | 5.6% | STRUCTURALLY CLEAN — 0 P1, 0 P2; P4 limited to hard-gate / analytical-pending / broken-XREF RD |
| **P1_REMEDIATION** | 9 | 4.2% | P1 REMEDIATION — has Path 1 mechanical items (no Path 2 directives) |
| **SUBPROCESS_NEEDED** | 154 | 72.3% | SUBPROCESS NEEDED — has Path 2 directives (re-extract / VC / DimReview) |
| **OTHER** | 3 | 1.4% | OTHER — non-categorised residual |
| **UNPROCESSED** | 30 | 14.1% | UNPROCESSED — no file_id / Phase 1 not run |

---

## BANKED REGISTRIES (5) — ready for Stage 1 entry

Each has 0 P1, 0 P2, 0 P4 findings. Only blockers remaining are programme-wide deferred items (`word_synopsis` + Session A extract).

| no | word | cluster | VC | DimRev | SB status | OWN | XREF | V | G | D |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 35 | covetousness | C13 | Complete | Complete | Verse Context Reset | 7 | 4 | 25 | 10 | 10 |
| 62 | fellowship | C17 | Complete | Complete | Verse Context Reset | 13 | 0 | 89 | 19 | 19 |
| 134 | renewal | C21 | Complete | Complete | Verse Context Reset | 7 | 3 | 22 | 5 | 5 |
| 206 | vulnerability | C22 | Complete | Complete | Verse Context Reset | 17 | 1 | 128 | 34 | 34 |
| 207 | blindness (spiritual) | C21 | Complete | Complete | Verse Context Reset | 7 | 2 | 103 | 12 | 12 |

## STRUCTURALLY CLEAN REGISTRIES (12) — no mechanical remediation needed

These registries have 0 P1 / 0 P2. All Path 4 items are either hard-gate flags (VC or DimReview not Complete) or analytical-pending (dominant_subject NULL, broken XREF pointers). No mechanical patch applicable; require analytical completion or researcher disposition of each P4.

| no | word | cluster | VC | DimReview | P4 | breakdown |
| ---: | --- | --- | --- | --- | ---: | --- |
| 18 | brokenness | C05 | Complete | Complete | 6 | dom_subj:6 |
| 27 | consciousness | C22 | — | — | 2 | hg:2 |
| 68 | grace | C17 | In Progres | Complete | 4 | hg:1 · broken_xref:3 |
| 104 | loyalty | C18 | Complete | — | 2 | hg:1 · broken_xref:1 |
| 109 | meekness | C08 | Complete | — | 4 | hg:1 · broken_xref:3 |
| 137 | resolve | C14 | Complete | — | 3 | hg:1 · broken_xref:2 |
| 138 | reverence | C15 | Complete | — | 2 | hg:1 · broken_xref:1 |
| 144 | sensuality | C12 | Complete | — | 1 | hg:1 |
| 188 | weeping | C05 | Complete | Complete | 10 | dom_subj:10 |
| 200 | energy | C20 | Complete | — | 1 | hg:1 |
| 202 | transformation | C21 | Complete | Complete | 9 | broken_xref:9 |
| 205 | resentment | C07 | Complete | — | 7 | hg:1 · broken_xref:6 |

---

## Per-Cluster Scorecard

### Cluster C01 — 6 registries

Summary: **SUBPROCESS_NEEDED**: 6

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 112 | mind | SUBPROCESS_NEEDED | Complete | — | 105 | 21 | 7 | 4 | 122 |
| 182 | Soul | SUBPROCESS_NEEDED | Complete | Complete | 20 | 4 | 1 | 1 | 63 |
| 183 | heart | SUBPROCESS_NEEDED | Complete | — | 49 | 96 | 1 | 26 | 125 |
| 184 | spirit | SUBPROCESS_NEEDED | Complete | Complete | 45 | 63 | 1 | 32 | 96 |
| 185 | flesh | SUBPROCESS_NEEDED | Complete | Complete | 23 | 34 | 0 | 9 | 56 |
| 211 | being | SUBPROCESS_NEEDED | Complete | Complete | 18 | 42 | 1 | 3 | 21 |

### Cluster C02 — 14 registries

Summary: **SUBPROCESS_NEEDED**: 14

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 32 | counsel | SUBPROCESS_NEEDED | Complete | — | 12 | 4 | 1 | 2 | 26 |
| 49 | discernment | SUBPROCESS_NEEDED | Complete | — | 20 | 12 | 1 | 15 | 21 |
| 85 | imagination | SUBPROCESS_NEEDED | Complete | — | 5 | 1 | 0 | 3 | 7 |
| 91 | insight | SUBPROCESS_NEEDED | Complete | — | 3 | 24 | 0 | 2 | 20 |
| 93 | intention | SUBPROCESS_NEEDED | Complete | Complete | 2 | 3 | 0 | 1 | 3 |
| 100 | knowledge | SUBPROCESS_NEEDED | Complete | — | 11 | 23 | 1 | 4 | 44 |
| 108 | meditation | SUBPROCESS_NEEDED | Complete | — | 5 | 34 | 0 | 1 | 36 |
| 110 | memory | SUBPROCESS_NEEDED | Complete | — | 4 | 5 | 0 | 3 | 6 |
| 126 | purpose | SUBPROCESS_NEEDED | Complete | — | 83 | 128 | 0 | 73 | 169 |
| 127 | reasoning | SUBPROCESS_NEEDED | Complete | — | 14 | 1 | 0 | 12 | 16 |
| 160 | thought | SUBPROCESS_NEEDED | Complete | — | 76 | 166 | 0 | 52 | 196 |
| 166 | understanding | SUBPROCESS_NEEDED | Complete | — | 7 | 32 | 1 | 1 | 34 |
| 174 | wisdom | SUBPROCESS_NEEDED | Complete | — | 24 | 20 | 1 | 2 | 52 |
| 213 | listen | SUBPROCESS_NEEDED | Complete | — | 38 | 25 | 3 | 4 | 69 |

### Cluster C03 — 9 registries

Summary: **SUBPROCESS_NEEDED**: 9

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 11 | awe | SUBPROCESS_NEEDED | Complete | — | 16 | 14 | 1 | 9 | 21 |
| 29 | contentment | SUBPROCESS_NEEDED | Complete | — | 6 | 2 | 0 | 5 | 9 |
| 42 | delight | SUBPROCESS_NEEDED | Complete | — | 75 | 51 | 0 | 46 | 105 |
| 69 | gratitude | SUBPROCESS_NEEDED | Complete | — | 3 | 0 | 0 | 1 | 4 |
| 97 | joy | SUBPROCESS_NEEDED | Complete | — | 39 | 10 | 1 | 11 | 53 |
| 132 | rejoicing | SUBPROCESS_NEEDED | Complete | — | 2 | 12 | 0 | 2 | 8 |
| 175 | wonder | SUBPROCESS_NEEDED | Complete | — | 8 | 5 | 1 | 2 | 10 |
| 186 | gladness | SUBPROCESS_NEEDED | Complete | — | 6 | 0 | 1 | 3 | 9 |
| 192 | comfort | SUBPROCESS_NEEDED | Complete | — | 5 | 10 | 0 | 1 | 8 |

### Cluster C04 — 7 registries

Summary: **SUBPROCESS_NEEDED**: 7

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 8 | appetite | SUBPROCESS_NEEDED | Complete | — | 11 | 10 | 0 | 1 | 14 |
| 43 | desire | SUBPROCESS_NEEDED | Complete | — | 151 | 48 | 1 | 106 | 209 |
| 78 | hope | SUBPROCESS_NEEDED | Complete | — | 42 | 22 | 0 | 17 | 75 |
| 102 | longing | SUBPROCESS_NEEDED | Complete | — | 15 | 9 | 0 | 2 | 21 |
| 115 | passion | SUBPROCESS_NEEDED | Complete | — | 4 | 14 | 0 | 2 | 12 |
| 179 | yearning | SUBPROCESS_NEEDED | Complete | — | 1 | 3 | 0 | 1 | 2 |
| 193 | craving | SUBPROCESS_NEEDED | Complete | — | 4 | 24 | 0 | 3 | 16 |

### Cluster C05 — 10 registries

Summary: **STRUCTURALLY_CLEAN**: 2 · **P1_REMEDIATION**: 1 · **SUBPROCESS_NEEDED**: 6 · **OTHER**: 1

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2 | agony | SUBPROCESS_NEEDED | Complete | — | 35 | 17 | 0 | 8 | 45 |
| 5 | anguish | SUBPROCESS_NEEDED | Complete | — | 62 | 69 | 1 | 20 | 72 |
| 18 | brokenness | STRUCTURALLY_CLEAN | Complete | Complete | 7 | 2 | 0 | 0 | 6 |
| 51 | distress | SUBPROCESS_NEEDED | Complete | — | 78 | 85 | 2 | 7 | 125 |
| 71 | grief | SUBPROCESS_NEEDED | Complete | — | 30 | 56 | 1 | 13 | 55 |
| 72 | groaning | SUBPROCESS_NEEDED | Complete | — | 10 | 2 | 0 | 2 | 14 |
| 113 | mourning | P1_REMEDIATION | Complete | Complete | 10 | 6 | 1 | 0 | 11 |
| 151 | sorrow | SUBPROCESS_NEEDED | Complete | — | 48 | 118 | 0 | 2 | 69 |
| 188 | weeping | STRUCTURALLY_CLEAN | Complete | Complete | 9 | 3 | 0 | 0 | 10 |
| 214 | suffering | OTHER | In Progres | — | 0 | 0 | 0 | 0 | 15 |

### Cluster C06 — 8 registries

Summary: **SUBPROCESS_NEEDED**: 7 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 7 | anxiety | SUBPROCESS_NEEDED | Complete | — | 10 | 5 | 0 | 2 | 17 |
| 44 | despair | SUBPROCESS_NEEDED | Complete | — | 21 | 9 | 1 | 8 | 33 |
| 53 | dread | SUBPROCESS_NEEDED | Complete | — | 7 | 9 | 0 | 3 | 15 |
| 61 | fear | SUBPROCESS_NEEDED | Complete | — | 91 | 69 | 1 | 32 | 165 |
| 79 | hopelessness | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 146 | shame | SUBPROCESS_NEEDED | Complete | — | 83 | 28 | 4 | 56 | 109 |
| 158 | terror | SUBPROCESS_NEEDED | Complete | — | 11 | 25 | 0 | 2 | 14 |
| 190 | contempt | SUBPROCESS_NEEDED | Complete | — | 11 | 22 | 0 | 1 | 31 |

### Cluster C07 — 10 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 8 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 4 | anger | SUBPROCESS_NEEDED | Complete | — | 104 | 6 | 2 | 71 | 141 |
| 13 | bitterness | SUBPROCESS_NEEDED | Complete | — | 11 | 9 | 1 | 1 | 18 |
| 56 | envy | SUBPROCESS_NEEDED | Complete | — | 28 | 2 | 1 | 16 | 38 |
| 75 | hatred | SUBPROCESS_NEEDED | Complete | — | 5 | 2 | 0 | 2 | 7 |
| 87 | indignation | SUBPROCESS_NEEDED | Complete | — | 2 | 15 | 0 | 1 | 12 |
| 96 | jealousy | SUBPROCESS_NEEDED | Complete | — | 1 | 21 | 0 | 1 | 12 |
| 136 | resentment | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 178 | wrath | SUBPROCESS_NEEDED | Complete | — | 9 | 61 | 0 | 2 | 46 |
| 181 | zeal | SUBPROCESS_NEEDED | Complete | — | 3 | 21 | 0 | 2 | 15 |
| 205 | resentment | STRUCTURALLY_CLEAN | Complete | — | 0 | 16 | 0 | 0 | 7 |

### Cluster C08 — 11 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 10

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 16 | boldness | SUBPROCESS_NEEDED | Complete | — | 6 | 3 | 0 | 2 | 9 |
| 33 | courage | SUBPROCESS_NEEDED | Complete | — | 34 | 23 | 0 | 11 | 44 |
| 46 | devotion | SUBPROCESS_NEEDED | Complete | — | 5 | 8 | 0 | 2 | 8 |
| 48 | diligence | SUBPROCESS_NEEDED | Complete | — | 7 | 1 | 0 | 1 | 2 |
| 55 | endurance | SUBPROCESS_NEEDED | Complete | — | 4 | 2 | 0 | 1 | 6 |
| 65 | generosity | SUBPROCESS_NEEDED | Complete | — | 6 | 27 | 1 | 1 | 13 |
| 66 | gentleness | SUBPROCESS_NEEDED | Complete | — | 7 | 8 | 0 | 3 | 12 |
| 80 | humility | SUBPROCESS_NEEDED | Complete | — | 12 | 9 | 2 | 2 | 20 |
| 109 | meekness | STRUCTURALLY_CLEAN | Complete | — | 0 | 13 | 0 | 0 | 4 |
| 116 | patience | SUBPROCESS_NEEDED | Complete | — | 19 | 7 | 0 | 10 | 24 |
| 142 | self-control | SUBPROCESS_NEEDED | Complete | — | 14 | 8 | 0 | 2 | 20 |

### Cluster C09 — 10 registries

Summary: **SUBPROCESS_NEEDED**: 7 · **UNPROCESSED**: 3

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 15 | boastfulness | SUBPROCESS_NEEDED | Complete | — | 9 | 1 | 0 | 2 | 15 |
| 36 | cowardice | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 74 | hardness | SUBPROCESS_NEEDED | Complete | — | 9 | 6 | 0 | 4 | 6 |
| 101 | laziness | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 123 | pride | SUBPROCESS_NEEDED | Complete | — | 56 | 8 | 0 | 7 | 69 |
| 128 | rebellion | SUBPROCESS_NEEDED | Complete | — | 21 | 4 | 0 | 3 | 30 |
| 133 | reliability | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 153 | stubbornness | SUBPROCESS_NEEDED | Complete | — | 7 | 3 | 0 | 4 | 6 |
| 170 | weakness | SUBPROCESS_NEEDED | Complete | — | 8 | 0 | 1 | 2 | 10 |
| 208 | sloth | SUBPROCESS_NEEDED | Complete | — | 7 | 4 | 0 | 2 | 15 |

### Cluster C10 — 11 registries

Summary: **SUBPROCESS_NEEDED**: 10 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 14 | blamelessness | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 60 | faithfulness | SUBPROCESS_NEEDED | Complete | — | 1 | 28 | 1 | 1 | 14 |
| 67 | goodness | SUBPROCESS_NEEDED | Complete | — | 3 | 42 | 0 | 1 | 43 |
| 77 | honesty | SUBPROCESS_NEEDED | Complete | — | 3 | 3 | 0 | 2 | 9 |
| 90 | innocence | SUBPROCESS_NEEDED | Complete | — | 23 | 4 | 0 | 3 | 35 |
| 92 | integrity | SUBPROCESS_NEEDED | Complete | — | 3 | 16 | 0 | 1 | 13 |
| 125 | purity | SUBPROCESS_NEEDED | Complete | — | 12 | 0 | 1 | 2 | 21 |
| 139 | righteousness | SUBPROCESS_NEEDED | Complete | — | 1 | 33 | 1 | 1 | 13 |
| 148 | sincerity | SUBPROCESS_NEEDED | Complete | — | 2 | 13 | 0 | 1 | 3 |
| 164 | truthfulness | SUBPROCESS_NEEDED | Complete | — | 5 | 0 | 0 | 2 | 11 |
| 168 | uprightness | SUBPROCESS_NEEDED | Complete | — | 9 | 2 | 0 | 2 | 20 |

### Cluster C11 — 10 registries

Summary: **SUBPROCESS_NEEDED**: 10

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 31 | corruption | SUBPROCESS_NEEDED | Complete | — | 18 | 0 | 2 | 3 | 17 |
| 40 | deceit | SUBPROCESS_NEEDED | Complete | — | 17 | 0 | 1 | 1 | 18 |
| 57 | evil | SUBPROCESS_NEEDED | Complete | — | 27 | 11 | 8 | 3 | 52 |
| 81 | hypocrisy | SUBPROCESS_NEEDED | Complete | — | 5 | 0 | 0 | 2 | 7 |
| 89 | iniquity | SUBPROCESS_NEEDED | Complete | — | 9 | 12 | 0 | 1 | 15 |
| 120 | perverseness | SUBPROCESS_NEEDED | Complete | — | 16 | 0 | 0 | 2 | 17 |
| 147 | sin | SUBPROCESS_NEEDED | Complete | — | 12 | 13 | 2 | 2 | 19 |
| 162 | transgression | SUBPROCESS_NEEDED | Complete | — | 16 | 12 | 0 | 9 | 17 |
| 172 | wickedness | SUBPROCESS_NEEDED | Complete | — | 5 | 20 | 1 | 2 | 19 |
| 203 | treachery | SUBPROCESS_NEEDED | Complete | — | 1 | 15 | 0 | 1 | 5 |

### Cluster C12 — 10 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 9

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | abomination | SUBPROCESS_NEEDED | Complete | — | 30 | 3 | 2 | 16 | 41 |
| 39 | debauchery | SUBPROCESS_NEEDED | Complete | — | 5 | 1 | 1 | 2 | 9 |
| 41 | defilement | SUBPROCESS_NEEDED | Complete | — | 2 | 0 | 0 | 1 | 3 |
| 86 | impurity | SUBPROCESS_NEEDED | Complete | — | 15 | 0 | 3 | 3 | 20 |
| 105 | lust | SUBPROCESS_NEEDED | Complete | — | 6 | 26 | 1 | 2 | 18 |
| 144 | sensuality | STRUCTURALLY_CLEAN | Complete | — | 0 | 1 | 0 | 0 | 1 |
| 149 | slander | SUBPROCESS_NEEDED | Complete | — | 17 | 20 | 0 | 1 | 34 |
| 157 | temptation | SUBPROCESS_NEEDED | Complete | — | 15 | 2 | 1 | 1 | 13 |
| 171 | whoredom | SUBPROCESS_NEEDED | Complete | — | 3 | 1 | 0 | 1 | 8 |
| 189 | malice | SUBPROCESS_NEEDED | Complete | — | 1 | 15 | 0 | 1 | 8 |

### Cluster C13 — 9 registries

Summary: **BANKED**: 1 · **P1_REMEDIATION**: 3 · **SUBPROCESS_NEEDED**: 5

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 24 | condemnation | P1_REMEDIATION | Complete | Complete | 13 | 5 | 1 | 0 | 0 |
| 26 | conscience | SUBPROCESS_NEEDED | Complete | Complete | 21 | 8 | 1 | 13 | 17 |
| 30 | contrition | P1_REMEDIATION | Complete | Complete | 10 | 3 | 1 | 0 | 0 |
| 35 | covetousness | BANKED | Complete | Complete | 7 | 4 | 0 | 0 | 0 |
| 50 | disobedience | SUBPROCESS_NEEDED | Complete | Complete | 4 | 1 | 0 | 1 | 1 |
| 70 | greed | P1_REMEDIATION | Complete | Complete | 3 | 11 | 1 | 0 | 1 |
| 73 | guilt | SUBPROCESS_NEEDED | Complete | Complete | 23 | 47 | 3 | 1 | 34 |
| 98 | justice | SUBPROCESS_NEEDED | Complete | Complete | 60 | 27 | 5 | 26 | 32 |
| 135 | repentance | SUBPROCESS_NEEDED | Complete | Complete | 33 | 6 | 0 | 22 | 23 |

### Cluster C14 — 10 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 6 · **UNPROCESSED**: 3

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 17 | bondage | SUBPROCESS_NEEDED | Complete | — | 8 | 0 | 2 | 2 | 17 |
| 21 | commitment | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 25 | conformity | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 45 | determination | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 114 | obedience | SUBPROCESS_NEEDED | Complete | — | 2 | 0 | 0 | 1 | 4 |
| 137 | resolve | STRUCTURALLY_CLEAN | Complete | — | 0 | 4 | 0 | 0 | 3 |
| 155 | submission | SUBPROCESS_NEEDED | Complete | — | 2 | 0 | 0 | 1 | 3 |
| 156 | surrender | SUBPROCESS_NEEDED | Complete | — | 27 | 2 | 0 | 16 | 19 |
| 173 | will | SUBPROCESS_NEEDED | Complete | — | 58 | 53 | 4 | 30 | 96 |
| 180 | yielding | SUBPROCESS_NEEDED | Complete | — | 24 | 2 | 4 | 2 | 71 |

### Cluster C15 — 9 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 8

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 59 | faith | SUBPROCESS_NEEDED | Complete | — | 46 | 25 | 0 | 29 | 71 |
| 94 | intercession | SUBPROCESS_NEEDED | Complete | — | 6 | 1 | 0 | 3 | 8 |
| 121 | praise | SUBPROCESS_NEEDED | Complete | — | 35 | 25 | 2 | 2 | 53 |
| 122 | prayer | SUBPROCESS_NEEDED | Complete | — | 7 | 9 | 0 | 2 | 19 |
| 138 | reverence | STRUCTURALLY_CLEAN | Complete | — | 0 | 20 | 0 | 0 | 2 |
| 140 | seeking | SUBPROCESS_NEEDED | Complete | — | 7 | 9 | 1 | 1 | 20 |
| 163 | trust | SUBPROCESS_NEEDED | Complete | — | 21 | 152 | 0 | 15 | 138 |
| 176 | worship | SUBPROCESS_NEEDED | Complete | — | 31 | 3 | 2 | 3 | 39 |
| 212 | pray | SUBPROCESS_NEEDED | Complete | — | 5 | 101 | 0 | 5 | 76 |

### Cluster C16 — 10 registries

Summary: **SUBPROCESS_NEEDED**: 10

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 6 | anointing | SUBPROCESS_NEEDED | Complete | — | 53 | 1 | 3 | 5 | 41 |
| 28 | consecration | SUBPROCESS_NEEDED | Complete | — | 26 | 4 | 0 | 8 | 25 |
| 76 | holiness | SUBPROCESS_NEEDED | Complete | — | 10 | 15 | 2 | 3 | 14 |
| 83 | idolatry | SUBPROCESS_NEEDED | Complete | — | 19 | 1 | 1 | 14 | 21 |
| 124 | prophecy | SUBPROCESS_NEEDED | Complete | — | 10 | 1 | 2 | 2 | 20 |
| 150 | sorcery | SUBPROCESS_NEEDED | Complete | — | 5 | 0 | 0 | 2 | 6 |
| 159 | testimony | SUBPROCESS_NEEDED | Complete | — | 20 | 1 | 1 | 13 | 20 |
| 165 | unbelief | SUBPROCESS_NEEDED | Complete | — | 3 | 11 | 1 | 2 | 8 |
| 191 | doubt | SUBPROCESS_NEEDED | Complete | — | 17 | 17 | 1 | 1 | 23 |
| 194 | blessing | SUBPROCESS_NEEDED | Complete | — | 4 | 9 | 1 | 2 | 14 |

### Cluster C17 — 10 registries

Summary: **BANKED**: 1 · **STRUCTURALLY_CLEAN**: 1 · **P1_REMEDIATION**: 2 · **SUBPROCESS_NEEDED**: 5 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 22 | communion | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 23 | compassion | SUBPROCESS_NEEDED | Complete | Complete | 71 | 26 | 5 | 52 | 55 |
| 34 | covenant | SUBPROCESS_NEEDED | Complete | Complete | 44 | 16 | 3 | 28 | 41 |
| 62 | fellowship | BANKED | Complete | Complete | 13 | 0 | 0 | 0 | 0 |
| 64 | forgiveness | P1_REMEDIATION | Complete | Complete | 7 | 0 | 1 | 0 | 0 |
| 68 | grace | STRUCTURALLY_CLEAN | In Progres | Complete | 5 | 8 | 0 | 0 | 4 |
| 99 | kindness | P1_REMEDIATION | Complete | Complete | 23 | 38 | 2 | 0 | 4 |
| 103 | love | SUBPROCESS_NEEDED | Complete | Complete | 81 | 59 | 7 | 25 | 37 |
| 111 | mercy | SUBPROCESS_NEEDED | Complete | Complete | 31 | 34 | 8 | 6 | 14 |
| 117 | peace | SUBPROCESS_NEEDED | Complete | Complete | 93 | 32 | 6 | 40 | 77 |

### Cluster C18 — 7 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 4 · **UNPROCESSED**: 2

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 12 | betrayal | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 52 | division | SUBPROCESS_NEEDED | Complete | — | 53 | 4 | 1 | 30 | 58 |
| 104 | loyalty | STRUCTURALLY_CLEAN | Complete | — | 0 | 6 | 0 | 0 | 2 |
| 106 | manipulation | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 131 | rejection | SUBPROCESS_NEEDED | Complete | — | 3 | 0 | 0 | 2 | 4 |
| 152 | strife | SUBPROCESS_NEEDED | Complete | — | 10 | 17 | 0 | 1 | 16 |
| 167 | unity | SUBPROCESS_NEEDED | Complete | — | 7 | 0 | 0 | 2 | 11 |

### Cluster C19 — 11 registries

Summary: **SUBPROCESS_NEEDED**: 7 · **UNPROCESSED**: 4

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 19 | calling | SUBPROCESS_NEEDED | Complete | — | 28 | 1 | 4 | 4 | 27 |
| 47 | dignity | SUBPROCESS_NEEDED | Complete | — | 7 | 32 | 0 | 2 | 38 |
| 82 | identity | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 84 | image of God | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 107 | meaning | SUBPROCESS_NEEDED | Complete | — | 12 | 13 | 0 | 3 | 15 |
| 119 | personhood | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 141 | self-awareness | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 177 | worth | SUBPROCESS_NEEDED | Complete | — | 16 | 17 | 0 | 3 | 31 |
| 201 | image | SUBPROCESS_NEEDED | Complete | — | 8 | 1 | 0 | 1 | 13 |
| 204 | name | SUBPROCESS_NEEDED | Complete | — | 3 | 3 | 1 | 2 | 18 |
| 209 | likeness | SUBPROCESS_NEEDED | Complete | — | 2 | 21 | 0 | 1 | 12 |

### Cluster C20 — 7 registries

Summary: **STRUCTURALLY_CLEAN**: 1 · **P1_REMEDIATION**: 2 · **SUBPROCESS_NEEDED**: 3 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 187 | strength | SUBPROCESS_NEEDED | Complete | Complete | 186 | 112 | 11 | 17 | 25 |
| 195 | spiritual powers | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 196 | power | P1_REMEDIATION | Complete | Complete | 14 | 47 | 1 | 0 | 5 |
| 197 | authority | SUBPROCESS_NEEDED | Complete | Complete | 132 | 35 | 7 | 41 | 68 |
| 198 | might | P1_REMEDIATION | Complete | Complete | 22 | 49 | 6 | 0 | 26 |
| 199 | dominion | SUBPROCESS_NEEDED | Complete | Complete | 40 | 63 | 6 | 9 | 26 |
| 200 | energy | STRUCTURALLY_CLEAN | Complete | — | 0 | 4 | 0 | 0 | 1 |

### Cluster C21 — 8 registries

Summary: **BANKED**: 2 · **STRUCTURALLY_CLEAN**: 1 · **SUBPROCESS_NEEDED**: 1 · **UNPROCESSED**: 4

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 37 | darkening | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 38 | deadness | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 134 | renewal | BANKED | Complete | Complete | 7 | 3 | 0 | 0 | 0 |
| 154 | stupor | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 161 | transformation | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 202 | transformation | STRUCTURALLY_CLEAN | Complete | Complete | 3 | 24 | 0 | 0 | 9 |
| 207 | blindness (spiritual) | BANKED | Complete | Complete | 7 | 2 | 0 | 0 | 0 |
| 210 | deadness | SUBPROCESS_NEEDED | Complete | Complete | 13 | 0 | 1 | 1 | 1 |

### Cluster C22 — 16 registries

Summary: **BANKED**: 1 · **STRUCTURALLY_CLEAN**: 1 · **P1_REMEDIATION**: 1 · **SUBPROCESS_NEEDED**: 2 · **OTHER**: 2 · **UNPROCESSED**: 9

| no | word | tier | vc | dr | OWN | XREF | P1 | P2 | P4 |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 3 | ambition | SUBPROCESS_NEEDED | Complete | Complete | 10 | 19 | 0 | 2 | 3 |
| 9 | assent | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 10 | awareness | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 3 |
| 20 | character | OTHER | Complete | Complete | 4 | 0 | 0 | 0 | 1 |
| 27 | consciousness | STRUCTURALLY_CLEAN | — | — | 0 | 2 | 0 | 0 | 2 |
| 54 | emotion | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 58 | experience | SUBPROCESS_NEEDED | Complete | Complete | 23 | 1 | 1 | 19 | 20 |
| 63 | foolishness | P1_REMEDIATION | Complete | Complete | 12 | 0 | 1 | 0 | 0 |
| 88 | ingratitude | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 95 | intuition | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 118 | personality | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 129 | recognition | OTHER | — | — | 0 | 23 | 0 | 0 | 18 |
| 143 | sensitivity | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 145 | sexuality | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 169 | vulnerability | UNPROCESSED | — | — | 0 | 0 | 0 | 0 | 4 |
| 206 | vulnerability | BANKED | Complete | Complete | 17 | 1 | 0 | 0 | 0 |

---

## Top 10 P1 Remediation Candidates (post-fix: 179 P1 items in total)

| no | word | cluster | P1 | P2 | P4 | OWN | XREF |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 187 | strength | C20 | 11 | 17 | 25 | 186 | 112 |
| 57 | evil | C11 | 8 | 3 | 52 | 27 | 11 |
| 111 | mercy | C17 | 8 | 6 | 14 | 31 | 34 |
| 103 | love | C17 | 7 | 25 | 37 | 81 | 59 |
| 112 | mind | C01 | 7 | 4 | 122 | 105 | 21 |
| 197 | authority | C20 | 7 | 41 | 68 | 132 | 35 |
| 117 | peace | C17 | 6 | 40 | 77 | 93 | 32 |
| 198 | might | C20 | 6 | 0 | 26 | 22 | 49 |
| 199 | dominion | C20 | 6 | 9 | 26 | 40 | 63 |
| 23 | compassion | C17 | 5 | 52 | 55 | 71 | 26 |

Total registries with Path 1 items: 80
Avg P1 per affected registry: 2.2

---

## Recommended next actions

1. **Bank the 5 BANKED registries** — produce formal completion records for each. Ready for Stage 1 entry when Session A + word_synopsis land.
2. **Review STRUCTURALLY_CLEAN registries (12)** — most Path 4 items are analytical-pending. Claude AI's per-word Stage 1 Step 1.2 will address them. Ready to send each to Stage 1 as soon as VC/DimReview completes.
3. **Tackle P1_REMEDIATION tier** — 179 real Path 1 items across affected registries. These are small mechanical fixes that batch well. Propose producing a global READINESSSWEEP patch covering all 179.
4. **SUBPROCESS_NEEDED — the 154 registries with Path 2 items** — this is the genuine analytical work queue: audit_word re-runs (86 registries), Dimension Review (various), Verse Context (32 registries). Per-directive researcher approval required.
5. **UNPROCESSED (30)** — standalone Phase 1 scheduling.

---

*End of Programme Readiness Scorecard v2 — 2026-04-19*