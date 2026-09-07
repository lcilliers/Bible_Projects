# M10b — Phase 9 Stage A obslog — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination
**Phase:** 9 Stage A (per-characteristic findings, 6 of 6 complete)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §12

## AI session output (in `files phase 9/`)

Six per-characteristic findings files, one per AI session:

| File | Char | Verses | E | S | G | Total |
|---|---|---:|---:|---:|---:|---:|
| char1-Wickedness-as-settled-person-identity-findings | 1 | 190 | 178 | 9 | 2 | 189 |
| char2-Evil-as-constitutional-inner-nature-findings | 2 | 90 | 180 | 7 | 2 | 189 |
| char3-Abomination-divine-revulsion-on-moral-character-findings | 3 | 40 | 181 | 6 | 2 | 189 |
| char4-Idolatrous-abomination-findings | 4 | 99 | 181 | 6 | 2 | 189 |
| char5-Iniquity-as-active-inner-scheming-and-evil-generation-findings | 5 | 79 | 180 | 7 | 2 | 189 |
| char6-Evil-expressed-through-speech-findings | 6 | 17 | 173 | 14 | 2 | 189 |
| **TOTAL** | | **515** | **1,073** | **49** | **12** | **1,134** |

## Pre-load validation: PASS

| Check | Result |
|---|---|
| 189 `**[CHAR-N]**` markers per file | ✓ 6/6 |
| 0 wrong-CHAR markers (no mixing) | ✓ 6/6 |
| 8 tier sections per file (T0–T7) | ✓ 6/6 |
| Per-tier prompt counts match expected (12+24+31+33+24+21+24+20=189) | ✓ exact across all 6 |
| No forbidden scope markers (`[SUB-`, `[CLUSTER-`, `[VCG-`) | ✓ 6/6 |
| Outcome codes (E/S/G) parse cleanly | ✓ all 1,134 |
| Citation discipline (verse/VCG/Strong's ref in E findings) | ~80% strict-cite; remaining 20% are catalogue's conditional / meta / sibling-reference prompts (T0.4.3, T1.5.3, T2.x.4 silence-confirmers, T1.1.1 name-analysis) which legitimately reference other prompts rather than verse evidence |

## DB writes

`scripts/_apply_phase9_characteristic_findings_20260518.py` ran 6× (one per char):
- 1,134 `cluster_finding` rows inserted (189 × 6)
- `characteristic_id` set for each row (47–52)
- `cluster_subgroup_id` = NULL (char-scope), `vcg_scope` = NULL
- `obs_id` mapped from T#.#.# codes via `wa_obs_question_catalogue.question_code`
- `version` = v1, `source_file` set per row
- 0 UNIQUE-constraint collisions

## Outcome distribution

| Char | E | S | G | E% |
|---|---:|---:|---:|---:|
| 1 Wickedness | 178 | 9 | 2 | 94.2% |
| 2 Evil-as-nature | 180 | 7 | 2 | 95.2% |
| 3 Abomination (moral-char) | 181 | 6 | 2 | 95.8% |
| 4 Idolatrous abomination | 181 | 6 | 2 | 95.8% |
| 5 Iniquity | 180 | 7 | 2 | 95.2% |
| 6 Evil through speech | 173 | 14 | 2 | 91.5% |
| **Cluster** | **1,073** | **49** | **12** | **94.6%** |

Char6 (Evil expressed through speech) shows the lowest E rate (91.5%) — consistent with its smallest sub-group size (17V) and narrowest evidence base (blasfēmeō, kakopoios, atopos).

Cluster-wide E rate of 94.6% is high — comparable to M10's 91.9% and reflects that M10b's 6 sharply-differentiated characteristics keep most prompts within evidence range.

## Comparison to M10 (post-split sibling, larger scale)

| | M10 | M10b |
|---|---:|---:|
| Characteristics | 22 | 6 |
| Prompts × chars | 4,158 | 1,134 |
| E rate | 91.9% | 94.6% |
| Verses | 1,325 | 515 |
| VCGs | 69 | 36 |

M10b's tighter characteristic-set + smaller corpus produces a slightly higher E rate. The 6-char structure (vs 22) means each characteristic carries a denser, less fragmented evidence pool.

## Cluster state post-Stage-A

- 17 terms · 515V · 36 VCGs · 6 sub-groups · 6 characteristics · 42 anchors
- **1,134 cluster_finding rows** (Stage A complete)
- 3 cluster_observation INTEGRATION_NOTE rows still `status='open'` — Stage A findings should have addressed them implicitly; Phase 11 fold will check
- Cluster status: `Analysis - In Progress` (unchanged)

## Next

**Phase 9 Stage B — cluster synthesis** (1 AI session, 189 cluster-scope prompts + free-form prose appendix).

The cluster synthesis reads the per-prompt matrix across all 6 characteristics (already in `cluster_finding`) and authors cluster-scope findings + thematic-prose appendix. Output:
- 189 cluster_finding rows with `characteristic_id=NULL`, `finding_status='cluster_synthesis'`
- Free-form prose appendix as standalone `-appendix-` file (not in DB)

Per memory `feedback_phase_brief_standard_practice.md` — CC will prepare the synthesis brief + structural input (per-prompt matrix) for the Stage B AI session.
