# Programme Readiness Scorecard — 2026-04-19

| Field | Value |
| --- | --- |
| Produced | 2026-04-19T20:27:37.286244+00:00 |
| Source scan | `outputs/reports/wa-global-readinesssweep-programme-scan-raw-20260419.json` |
| Instruction | `wa-global-readiness-sweep-instruction-v1_0-20260419.md` §8 F2 |
| Schema version | 3.10.0 |
| Total registries | 213 (carry_forward=1) |

---

## Programme Summary

| Tier | Count | Share | Meaning |
| --- | ---: | ---: | --- |
| **BANKED** | 1 | 0.5% | BANKED — ready for Stage 1 (once Session A + word_synopsis land) |
| **STRUCTURALLY_CLEAN** | 0 | 0.0% | STRUCTURALLY CLEAN — pending analytical work (dominant_subject / hard-gate only) |
| **XREF_PILOT_BUG_EXPOSURE** | 24 | 11.3% | XREF-EXPOSED — pilot-flagged P1 items need OT-DBR-010 fix before reliable |
| **SUBPROCESS_NEEDED** | 154 | 72.3% | SUBPROCESS NEEDED — re-extraction / VC / DimReview required (P2 items) |
| **REMEDIATION_NEEDED** | 4 | 1.9% | REMEDIATION — has P1 or P4 items requiring attention |
| **UNPROCESSED** | 30 | 14.1% | UNPROCESSED — no file_id / Phase 1 not run |

---

## Tier Definitions

- **BANKED** — strict clean (0 Path 1 / 0 Path 2 / 0 Path 4). Ready to re-enter the post-reset Stage 1 once the programme-wide deferred items land (Session A extract generator + researcher-authored `word_synopsis`). No registry-specific work remaining.
- **STRUCTURALLY CLEAN** — 0 Path 1 / 0 Path 2 but has Path 4 items. All Path 4 items are either hard-gate status flags (VC/DimReview not Complete) or analytical-pending (e.g. `dominant_subject=NULL` on groups — requires verse reading). No mechanical corrections needed; pending analytical completion.
- **XREF-EXPOSED** — has Path 1 findings that touch XREF terms. Affected by pilot/runner join-duplication on `mti_terms` duplicates (OT-DBR-010). Path 1 counts are unreliable until either: (a) OT-DBR-009 mti_terms dedup migrates, or (b) OT-DBR-010 pilot fix filters to canonical rows. Blocked for mechanical sweep remediation.
- **SUBPROCESS NEEDED** — has Path 2 items (span filter failure, zero extraction, dimension review, etc.). Requires re-extraction / VC / DimReview work. Path 2 execution gated by OT-DBR-001 (now resolved) + researcher per-directive approval.
- **REMEDIATION NEEDED** — other combinations requiring attention.
- **UNPROCESSED** — no `wa_file_index` rows exist; Phase 1 (registration + STEP extract) never ran. Out of sweep scope until ingested.

---

## Per-Cluster Scorecard

### Cluster C01 — 6 registries

Summary: **SUBPROCESS_NEEDED**: 6

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 112 | mind | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 105 | 80 | 25 | 4 | 143 | auto:2 |
| 182 | Soul | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 20 | 17 | 1 | 1 | 68 |  |
| 183 | heart | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 49 | 468 | 177 | 26 | 136 | null_dim:1; auto:8 |
| 184 | spirit | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 45 | 303 | 105 | 32 | 113 |  |
| 185 | flesh | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 23 | 99 | 39 | 9 | 55 |  |
| 211 | being | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 18 | 119 | 30 | 3 | 62 |  |

### Cluster C02 — 14 registries

Summary: **SUBPROCESS_NEEDED**: 14

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 32 | counsel | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 12 | 30 | 17 | 2 | 30 | null_dim:1; auto:23 |
| 49 | discernment | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 20 | 41 | 26 | 15 | 33 | null_dim:1; auto:7 |
| 85 | imagination | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 3 | 2 | 3 | 8 | auto:3 |
| 91 | insight | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 104 | 74 | 2 | 19 | auto:5 |
| 93 | intention | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 12 | 8 | 1 | 7 |  |
| 100 | knowledge | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 11 | 133 | 62 | 4 | 37 | auto:25 |
| 108 | meditation | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 172 | 104 | 1 | 10 | auto:5 |
| 110 | memory | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 4 | 26 | 17 | 3 | 11 | auto:1 |
| 126 | purpose | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 83 | 514 | 154 | 73 | 137 | auto:14 |
| 127 | reasoning | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 14 | 3 | 1 | 12 | 17 | auto:3 |
| 160 | thought | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 76 | 537 | 178 | 52 | 129 | auto:20 |
| 166 | understanding | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 174 | 112 | 1 | 25 | auto:12 |
| 174 | wisdom | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 24 | 89 | 66 | 2 | 45 | null_dim:4; auto:37 |
| 213 | listen | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 38 | 41 | 14 | 4 | 59 | null_dim:3; auto:49 |

### Cluster C03 — 9 registries

Summary: **SUBPROCESS_NEEDED**: 9

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 11 | awe | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 16 | 60 | 46 | 9 | 35 | null_dim:3; auto:13 |
| 29 | contentment | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 6 | 6 | 2 | 5 | 7 | auto:2 |
| 42 | delight | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 75 | 170 | 32 | 46 | 120 | auto:40 |
| 69 | gratitude | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 0 | 0 | 1 | 4 | auto:3 |
| 97 | joy | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 39 | 28 | 4 | 11 | 58 | null_dim:1; auto:40 |
| 132 | rejoicing | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 40 | 14 | 2 | 10 | auto:1 |
| 175 | wonder | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 8 | 11 | 6 | 2 | 13 | null_dim:2; auto:8 |
| 186 | gladness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 6 | 0 | 1 | 3 | 9 | null_dim:2; auto:8 |
| 192 | comfort | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 29 | 12 | 1 | 18 | auto:7 |

### Cluster C04 — 7 registries

Summary: **SUBPROCESS_NEEDED**: 7

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 8 | appetite | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 11 | 90 | 40 | 1 | 27 | auto:12 |
| 43 | desire | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 151 | 251 | 77 | 106 | 239 | null_dim:5; auto:94 |
| 78 | hope | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 42 | 121 | 53 | 17 | 57 | null_dim:7; auto:39 |
| 102 | longing | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 15 | 32 | 15 | 2 | 24 | null_dim:1; auto:17 |
| 115 | passion | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 4 | 34 | 17 | 2 | 12 | auto:3 |
| 179 | yearning | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 1 | 14 | 3 | 1 | 5 | auto:1 |
| 193 | craving | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 4 | 147 | 70 | 3 | 23 | null_dim:2; auto:3 |

### Cluster C05 — 10 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 3 · **SUBPROCESS_NEEDED**: 6 · **REMEDIATION_NEEDED**: 1

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2 | agony | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 35 | 91 | 44 | 8 | 44 | null_dim:4; auto:29 |
| 5 | anguish | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 62 | 249 | 154 | 20 | 129 | null_dim:2; auto:48 |
| 18 | brokenness | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 7 | 17 | 14 | 0 | 9 |  |
| 51 | distress | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 78 | 362 | 220 | 7 | 150 | null_dim:25; auto:89 |
| 71 | grief | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 30 | 261 | 164 | 13 | 69 | null_dim:1; auto:21 |
| 72 | groaning | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 10 | 18 | 15 | 2 | 16 | null_dim:1; auto:13 |
| 113 | mourning | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 10 | 20 | 14 | 0 | 18 |  |
| 151 | sorrow | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 48 | 481 | 290 | 2 | 121 | null_dim:2; auto:35 |
| 188 | weeping | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 9 | 4 | 1 | 0 | 14 |  |
| 214 | suffering | REMEDIATION_NEEDED | In Progr | — | Ready for Analys | 0 | 0 | 0 | 0 | 15 |  |

### Cluster C06 — 8 registries

Summary: **SUBPROCESS_NEEDED**: 7 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 7 | anxiety | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 10 | 18 | 4 | 2 | 20 | null_dim:5; auto:15 |
| 44 | despair | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 21 | 38 | 22 | 8 | 42 | null_dim:5; auto:26 |
| 53 | dread | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 26 | 15 | 3 | 18 | auto:9 |
| 61 | fear | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 91 | 247 | 115 | 32 | 140 | null_dim:4; auto:87 |
| 79 | hopelessness | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 146 | shame | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 83 | 81 | 23 | 56 | 98 | auto:34 |
| 158 | terror | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 11 | 79 | 49 | 2 | 29 | null_dim:1; auto:8 |
| 190 | contempt | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 11 | 43 | 21 | 1 | 19 | auto:13 |

### Cluster C07 — 10 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 1 · **SUBPROCESS_NEEDED**: 8 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 4 | anger | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 104 | 21 | 9 | 71 | 137 | null_dim:4; auto:66 |
| 13 | bitterness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 11 | 36 | 27 | 1 | 15 | auto:11 |
| 56 | envy | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 28 | 7 | 4 | 16 | 40 | null_dim:9; auto:24 |
| 75 | hatred | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 4 | 2 | 2 | 9 | null_dim:1; auto:6 |
| 87 | indignation | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 78 | 55 | 1 | 9 | auto:2 |
| 96 | jealousy | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 1 | 79 | 53 | 1 | 15 | auto:2 |
| 136 | resentment | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 178 | wrath | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 9 | 194 | 97 | 2 | 39 | null_dim:2; auto:11 |
| 181 | zeal | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 67 | 41 | 2 | 18 | null_dim:2; auto:5 |
| 205 | resentment | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 46 | 26 | 0 | 12 |  |

### Cluster C08 — 11 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 1 · **SUBPROCESS_NEEDED**: 10

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 16 | boldness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 6 | 11 | 4 | 2 | 12 | auto:7 |
| 33 | courage | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 34 | 115 | 67 | 11 | 65 | null_dim:9; auto:33 |
| 46 | devotion | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 52 | 20 | 2 | 14 | null_dim:6; auto:6 |
| 48 | diligence | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 3 | 2 | 1 | 3 |  |
| 55 | endurance | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 4 | 4 | 2 | 1 | 8 | auto:5 |
| 65 | generosity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 6 | 165 | 114 | 1 | 38 | auto:10 |
| 66 | gentleness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 38 | 22 | 3 | 18 | auto:8 |
| 80 | humility | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 12 | 44 | 24 | 2 | 23 | null_dim:2; auto:16 |
| 109 | meekness | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 61 | 35 | 0 | 11 |  |
| 116 | patience | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 19 | 28 | 14 | 10 | 23 | null_dim:1; auto:14 |
| 142 | self-control | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 14 | 21 | 10 | 2 | 20 | null_dim:1; auto:15 |

### Cluster C09 — 10 registries

Summary: **SUBPROCESS_NEEDED**: 7 · **UNPROCESSED**: 3

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 15 | boastfulness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 9 | 4 | 2 | 2 | 14 | null_dim:2; auto:13 |
| 36 | cowardice | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 74 | hardness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 9 | 22 | 15 | 4 | 12 | auto:2 |
| 101 | laziness | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 123 | pride | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 56 | 28 | 14 | 7 | 69 | null_dim:13; auto:59 |
| 128 | rebellion | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 21 | 11 | 7 | 3 | 34 | null_dim:4; auto:28 |
| 133 | reliability | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 153 | stubbornness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 6 | 3 | 4 | 9 | auto:2 |
| 170 | weakness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 8 | 0 | 1 | 2 | 10 | null_dim:1; auto:9 |
| 208 | sloth | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 8 | 4 | 2 | 13 | null_dim:1; auto:11 |

### Cluster C10 — 11 registries

Summary: **SUBPROCESS_NEEDED**: 10 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 14 | blamelessness | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 60 | faithfulness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 1 | 134 | 72 | 1 | 30 | auto:7 |
| 67 | goodness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 196 | 116 | 1 | 21 | auto:9 |
| 77 | honesty | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 11 | 6 | 2 | 12 | auto:6 |
| 90 | innocence | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 23 | 12 | 8 | 3 | 39 | null_dim:1; auto:33 |
| 92 | integrity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 73 | 54 | 1 | 15 | auto:5 |
| 125 | purity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 12 | 0 | 1 | 2 | 21 | null_dim:1; auto:20 |
| 139 | righteousness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 1 | 114 | 72 | 1 | 26 | auto:1 |
| 148 | sincerity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 52 | 38 | 1 | 16 | auto:2 |
| 164 | truthfulness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 0 | 0 | 2 | 11 | null_dim:3; auto:10 |
| 168 | uprightness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 9 | 4 | 2 | 2 | 22 | auto:18 |

### Cluster C11 — 10 registries

Summary: **SUBPROCESS_NEEDED**: 10

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | corruption | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 18 | 0 | 2 | 3 | 17 | null_dim:1; auto:15 |
| 40 | deceit | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 17 | 0 | 1 | 1 | 18 | auto:17 |
| 57 | evil | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 27 | 83 | 74 | 3 | 55 | null_dim:4; auto:46 |
| 81 | hypocrisy | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 0 | 0 | 2 | 7 | null_dim:2; auto:6 |
| 89 | iniquity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 9 | 46 | 33 | 1 | 27 | auto:14 |
| 120 | perverseness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 16 | 0 | 0 | 2 | 17 | null_dim:2; auto:16 |
| 147 | sin | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 12 | 39 | 27 | 2 | 30 | null_dim:1; auto:17 |
| 162 | transgression | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 16 | 25 | 13 | 9 | 29 | auto:8 |
| 172 | wickedness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 90 | 66 | 2 | 31 | null_dim:1; auto:14 |
| 203 | treachery | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 1 | 30 | 15 | 1 | 14 | auto:1 |

### Cluster C12 — 10 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 1 · **SUBPROCESS_NEEDED**: 9

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | abomination | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 30 | 9 | 7 | 16 | 44 | null_dim:1; auto:26 |
| 39 | debauchery | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 3 | 3 | 2 | 10 | null_dim:3; auto:8 |
| 41 | defilement | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 0 | 0 | 1 | 3 | auto:2 |
| 86 | impurity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 15 | 0 | 3 | 3 | 20 | null_dim:1; auto:18 |
| 105 | lust | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 6 | 98 | 47 | 2 | 22 | null_dim:3; auto:6 |
| 144 | sensuality | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 2 | 1 | 0 | 2 |  |
| 149 | slander | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 17 | 73 | 36 | 1 | 20 | auto:16 |
| 157 | temptation | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 15 | 4 | 3 | 1 | 15 | auto:12 |
| 171 | whoredom | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 2 | 1 | 1 | 9 | auto:7 |
| 189 | malice | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 1 | 80 | 59 | 1 | 11 | auto:1 |

### Cluster C13 — 9 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 4 · **SUBPROCESS_NEEDED**: 5

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 24 | condemnation | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 13 | 12 | 8 | 0 | 5 |  |
| 26 | conscience | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 21 | 45 | 17 | 13 | 17 |  |
| 30 | contrition | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Ready for Analys | 10 | 3 | 1 | 0 | 3 |  |
| 35 | covetousness | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 7 | 17 | 7 | 0 | 4 |  |
| 50 | disobedience | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 4 | 3 | 2 | 1 | 2 |  |
| 70 | greed | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 3 | 92 | 42 | 0 | 15 |  |
| 73 | guilt | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 23 | 186 | 40 | 1 | 15 |  |
| 98 | justice | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 60 | 65 | 18 | 26 | 44 |  |
| 135 | repentance | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 33 | 24 | 10 | 22 | 27 |  |

### Cluster C14 — 10 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 1 · **SUBPROCESS_NEEDED**: 6 · **UNPROCESSED**: 3

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 17 | bondage | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 8 | 0 | 2 | 2 | 17 | null_dim:3; auto:16 |
| 21 | commitment | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 25 | conformity | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 45 | determination | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 114 | obedience | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 0 | 0 | 1 | 4 | auto:3 |
| 137 | resolve | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 21 | 5 | 0 | 3 |  |
| 155 | submission | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 0 | 0 | 1 | 3 | auto:2 |
| 156 | surrender | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 27 | 4 | 2 | 16 | 19 | auto:1 |
| 173 | will | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 58 | 182 | 44 | 30 | 121 | null_dim:7; auto:52 |
| 180 | yielding | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 24 | 4 | 6 | 2 | 71 | null_dim:10; auto:69 |

### Cluster C15 — 9 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 1 · **SUBPROCESS_NEEDED**: 8

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 59 | faith | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 46 | 138 | 65 | 29 | 80 | auto:34 |
| 94 | intercession | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 6 | 3 | 1 | 3 | 9 | auto:5 |
| 121 | praise | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 35 | 139 | 98 | 2 | 75 | null_dim:10; auto:50 |
| 122 | prayer | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 41 | 19 | 2 | 14 | null_dim:1; auto:11 |
| 138 | reverence | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 66 | 45 | 0 | 20 |  |
| 140 | seeking | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 18 | 10 | 1 | 17 | auto:13 |
| 163 | trust | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 21 | 536 | 168 | 15 | 66 | null_dim:1; auto:12 |
| 176 | worship | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 31 | 7 | 6 | 3 | 42 | null_dim:7; auto:37 |
| 212 | pray | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 295 | 37 | 5 | 38 | null_dim:1; auto:2 |

### Cluster C16 — 10 registries

Summary: **SUBPROCESS_NEEDED**: 10

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 6 | anointing | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 53 | 3 | 5 | 5 | 42 | null_dim:6; auto:38 |
| 28 | consecration | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 26 | 28 | 20 | 8 | 27 | null_dim:1; auto:17 |
| 76 | holiness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 10 | 30 | 17 | 3 | 29 | auto:11 |
| 83 | idolatry | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 19 | 2 | 2 | 14 | 22 | auto:7 |
| 124 | prophecy | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 10 | 2 | 3 | 2 | 21 | null_dim:6; auto:19 |
| 150 | sorcery | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 5 | 0 | 0 | 2 | 6 | auto:4 |
| 159 | testimony | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 20 | 2 | 2 | 13 | 21 | null_dim:1; auto:8 |
| 165 | unbelief | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 42 | 23 | 2 | 15 | null_dim:2; auto:5 |
| 191 | doubt | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 17 | 84 | 50 | 1 | 30 | auto:17 |
| 194 | blessing | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 4 | 34 | 25 | 2 | 15 | null_dim:3; auto:9 |

### Cluster C17 — 10 registries

Summary: **BANKED**: 1 · **XREF_PILOT_BUG_EXPOSURE**: 2 · **SUBPROCESS_NEEDED**: 5 · **REMEDIATION_NEEDED**: 1 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 22 | communion | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 23 | compassion | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 71 | 105 | 24 | 52 | 77 |  |
| 34 | covenant | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 44 | 43 | 13 | 28 | 33 |  |
| 62 | fellowship | BANKED | Complete | Complete | Verse Context Re | 13 | 0 | 0 | 0 | 0 |  |
| 64 | forgiveness | REMEDIATION_NEEDED | Complete | Complete | Verse Context Re | 7 | 0 | 1 | 0 | 0 |  |
| 68 | grace | XREF_PILOT_BUG_EXPOSURE | In Progr | Complete | Verse Context Re | 5 | 40 | 7 | 0 | 6 |  |
| 99 | kindness | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 23 | 141 | 79 | 0 | 34 |  |
| 103 | love | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 81 | 179 | 51 | 25 | 68 |  |
| 111 | mercy | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 31 | 140 | 34 | 6 | 32 |  |
| 117 | peace | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 93 | 112 | 36 | 40 | 57 |  |

### Cluster C18 — 7 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 1 · **SUBPROCESS_NEEDED**: 4 · **UNPROCESSED**: 2

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 12 | betrayal | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 52 | division | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 53 | 27 | 22 | 30 | 54 | null_dim:5; auto:25 |
| 104 | loyalty | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 46 | 18 | 0 | 6 |  |
| 106 | manipulation | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 131 | rejection | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 0 | 0 | 2 | 4 | null_dim:1; auto:2 |
| 152 | strife | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 10 | 45 | 27 | 1 | 21 | auto:9 |
| 167 | unity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 0 | 0 | 2 | 11 | null_dim:3; auto:10 |

### Cluster C19 — 11 registries

Summary: **SUBPROCESS_NEEDED**: 7 · **UNPROCESSED**: 4

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 19 | calling | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 28 | 4 | 5 | 4 | 28 | null_dim:4; auto:24 |
| 47 | dignity | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 7 | 122 | 32 | 2 | 14 | null_dim:3; auto:9 |
| 82 | identity | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 84 | image of God | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 107 | meaning | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 12 | 45 | 26 | 3 | 22 | null_dim:2; auto:10 |
| 119 | personhood | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 141 | self-awareness | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 177 | worth | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 16 | 45 | 25 | 3 | 42 | null_dim:5; auto:26 |
| 201 | image | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 8 | 3 | 2 | 1 | 14 | auto:12 |
| 204 | name | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 3 | 11 | 6 | 2 | 15 | null_dim:3; auto:14 |
| 209 | likeness | SUBPROCESS_NEEDED | Complete | — | Verse Context Re | 2 | 75 | 48 | 1 | 15 | auto:2 |

### Cluster C20 — 7 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 3 · **SUBPROCESS_NEEDED**: 3 · **UNPROCESSED**: 1

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 187 | strength | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 186 | 469 | 286 | 17 | 100 |  |
| 195 | spiritual powers | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 196 | power | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 14 | 238 | 163 | 0 | 44 |  |
| 197 | authority | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 132 | 162 | 96 | 41 | 91 |  |
| 198 | might | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 22 | 163 | 92 | 0 | 23 |  |
| 199 | dominion | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 40 | 245 | 125 | 9 | 59 |  |
| 200 | energy | XREF_PILOT_BUG_EXPOSURE | Complete | — | Verse Context Re | 0 | 9 | 5 | 0 | 5 |  |

### Cluster C21 — 8 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 3 · **SUBPROCESS_NEEDED**: 1 · **UNPROCESSED**: 4

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 37 | darkening | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 38 | deadness | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 134 | renewal | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 7 | 9 | 6 | 0 | 3 |  |
| 154 | stupor | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 161 | transformation | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 202 | transformation | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 3 | 79 | 51 | 0 | 15 |  |
| 207 | blindness (spiritual) | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 7 | 4 | 2 | 0 | 2 |  |
| 210 | deadness | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 13 | 0 | 1 | 1 | 1 |  |

### Cluster C22 — 16 registries

Summary: **XREF_PILOT_BUG_EXPOSURE**: 3 · **SUBPROCESS_NEEDED**: 2 · **REMEDIATION_NEEDED**: 2 · **UNPROCESSED**: 9

| no | word | tier | vc | dr | sb | OWN | XREF | P1 | P2 | P4 | notable |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | ambition | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 10 | 58 | 38 | 2 | 22 |  |
| 9 | assent | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 10 | awareness | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 3 |  |
| 20 | character | REMEDIATION_NEEDED | Complete | Complete | Verse Context Re | 4 | 0 | 0 | 0 | 1 |  |
| 27 | consciousness | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 0 | 12 | 4 | 0 | 2 |  |
| 54 | emotion | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 58 | experience | SUBPROCESS_NEEDED | Complete | Complete | Verse Context Re | 23 | 3 | 3 | 19 | 21 |  |
| 63 | foolishness | REMEDIATION_NEEDED | Complete | Complete | Verse Context Re | 12 | 0 | 1 | 0 | 0 |  |
| 88 | ingratitude | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 95 | intuition | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 118 | personality | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 129 | recognition | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 0 | 141 | 64 | 0 | 9 |  |
| 143 | sensitivity | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 145 | sexuality | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 169 | vulnerability | UNPROCESSED | — | — | — | 0 | 0 | 0 | 0 | 4 |  |
| 206 | vulnerability | XREF_PILOT_BUG_EXPOSURE | Complete | Complete | Verse Context Re | 17 | 3 | 2 | 0 | 1 |  |

---

## BANKED REGISTRIES (1)

These registries are structurally clean AND have 0 Path 4 findings. They are ready to enter post-reset Stage 1 Analysis Readiness as soon as two programme-wide deferred items land:

1. `generate_session_a_extract.py` (Session A extract generator — Path 5 deferred)
2. Researcher-authored `word_synopsis` for each banked registry (Path 3 deferred)

| no | word | cluster | VC | DimReview | SessionB | OWN | Verses | Groups |
| ---: | --- | --- | --- | --- | --- | ---: | ---: | ---: |
| 62 | fellowship | C17 | Complete | Complete | Verse Context Reset | 13 | 89 | 19 |

---

## STRUCTURALLY CLEAN REGISTRIES (0)

These registries have 0 mechanical remediations but carry Path 4 items limited to hard-gate flags or analytical-pending tasks (e.g. `dominant_subject=NULL` on groups — requires verse reading). They will graduate to BANKED when those analytical items are completed.


---

## UNPROCESSED REGISTRIES (30)

These registries have no `wa_file_index` rows and cannot be swept. They require Phase 1 (registration + STEP extract + audit_word) before sweep can inspect them.

| no | word | cluster |
| ---: | --- | --- |
| 9 | assent | C22 |
| 10 | awareness | C22 |
| 12 | betrayal | C18 |
| 14 | blamelessness | C10 |
| 21 | commitment | C14 |
| 22 | communion | C17 |
| 25 | conformity | C14 |
| 36 | cowardice | C09 |
| 37 | darkening | C21 |
| 38 | deadness | C21 |
| 45 | determination | C14 |
| 54 | emotion | C22 |
| 79 | hopelessness | C06 |
| 82 | identity | C19 |
| 84 | image of God | C19 |
| 88 | ingratitude | C22 |
| 95 | intuition | C22 |
| 101 | laziness | C09 |
| 106 | manipulation | C18 |
| 118 | personality | C22 |
| 119 | personhood | C19 |
| 133 | reliability | C09 |
| 136 | resentment | C07 |
| 141 | self-awareness | C19 |
| 143 | sensitivity | C22 |
| 145 | sexuality | C22 |
| 154 | stupor | C21 |
| 161 | transformation | C21 |
| 169 | vulnerability | C22 |
| 195 | spiritual powers | C20 |

---

## Sweep Remediation Priority Order

Given the tier distribution, the recommended work sequence is:

1. **Unblock programme-wide deferred items** — build `generate_session_a_extract.py` + solicit researcher-authored `word_synopsis` values. This clears BANKED registries for Stage 1 entry immediately.
2. **Address STRUCTURALLY_CLEAN registries** — run Verse Context anchor pass / Dimension Review on the groups with `dominant_subject=NULL`. Each is an analytical pass per registry; Claude AI work, not CC.
3. **Design OT-DBR-009 mti_terms deduplication migration** — unblocks XREF-exposed registries for reliable Path 1 patching.
4. **Fix OT-DBR-010 pilot/runner XREF join** — interim fix to surface real XREF findings while OT-DBR-009 is pending.
5. **Process SUBPROCESS_NEEDED registries in priority order** — 86 registries per earlier programme scan §4.1 (span filter failure / zero extraction). Requires per-directive researcher approval. audit_word rewrite (OT-DBR-001) now allows execution.
6. **Phase 1 for UNPROCESSED registries** — standalone programme work; requires deliberate scheduling with researcher.

---

## Scorecard Caveats

1. **OT-DBR-010 (pilot XREF join)** is a known diagnostic flaw. Path 1 and Path 4 counts on XREF-exposed registries may be inflated by duplicate-row flagging. This affects the XREF_PILOT_BUG_EXPOSURE tier and any registry with XREF terms in REMEDIATION_NEEDED.
2. The BANKED / STRUCTURALLY_CLEAN tiers are reliable — they exclude XREF-exposed registries and thus aren't affected by OT-DBR-010.
3. The 'analytical-pending' classification in STRUCTURALLY_CLEAN is optimistic — some of those P4 items might turn into data issues if examined closely. The label reflects _Path 4 nature_ (requires human decision), not guaranteed cleanliness.

---

*End of Programme Readiness Scorecard — 2026-04-19*