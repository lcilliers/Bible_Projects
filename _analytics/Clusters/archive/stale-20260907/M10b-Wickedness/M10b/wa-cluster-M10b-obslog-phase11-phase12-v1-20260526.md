# M10b — Phase 11 + Phase 12 obslog — 2026-05-26

**Cluster:** M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
**Phases:** 11 (Inherited-finding fold + validation) · 12 (Cluster closure)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §14, §15

## Phase 11 — Inherited-finding fold + validation

**Script:** `scripts/_validate_m10b_phase11_v1_20260526.py` (cloned from M09 validator with M10b adaptations: cluster code, output path, SUBGROUP_REF_RE, BOUNDARY-PENDING query narrowed to M10b's own Strong's set rather than shared-registry scope).
**Validation report:** [`wa-cluster-M10b-phase11-validation-v1-20260526.md`](wa-cluster-M10b-phase11-validation-v1-20260526.md)

### Fold operation: no-op

M10b is a fresh post-split cluster — no inherited Session B findings target M10b's terms. The §14.5 fold has nothing to fold.

### §14.6 + §15.2 validation: 11/11 PASS

| Check | Result |
|---|---|
| Row counts | ✓ 1,323 / 1,323 (1,134 char + 189 synthesis) |
| Per-scope 189-prompt completeness | ✓ all chars 189; synthesis 189 |
| Evidence-grounding | ✓ soft pass — 1,215/1,262 E-rows explicitly anchored; 47 meta-analytical legitimately reference sibling prompts |
| Prompt × scope completeness | ✓ no gaps |
| Observations resolved | ✓ 3/3 INTEGRATION_NOTEs `confirmed` |
| No legacy markers in new rows | ✓ |
| C1 (VC-coverage) | ✓ 0 orphans |
| C2 (vc_status) | ✓ all `vc_completed` |
| group_id + cluster_subgroup_id populated | ✓ |
| R4 (anchors) | ✓ 17/17 terms |
| M10b-BOUNDARY empty | ✓ (no BOUNDARY sub-group exists) |

## Phase 12 — Cluster closure

**Script:** `scripts/_apply_m10b_phase12_closure_20260526.py`
**DB write:** UPDATE `cluster` SET `status='Analysis Completed'`, `last_updated_date='2026-05-26T03:21:49Z'` WHERE `cluster_code='M10b'` AND `status='Analysis - In Progress'`. 1 row affected.

### §15.2 pre-flight: all clean

Both evidence-grounding and completeness pass (carried forward from Phase 11 validation). All structural carry-forwards (C1, C2, R4, H-checks, BOUNDARY-PENDING) are at baseline.

## Final cluster state

| | |
|---|---:|
| Terms | 17 |
| Active is_relevant verses | 515 |
| Sub-groups | 6 |
| VCGs | 36 |
| Characteristics | 6 |
| Anchors (is_anchor=1) | 42 |
| `cluster_finding` rows | **1,323** |
| → char-scope findings | 1,134 |
| → cluster-synthesis findings | 189 |
| → E rate (overall) | 94.9% |
| `cluster_observation` rows confirmed | 3 of 3 |
| **Status** | **`Analysis Completed`** |

## End-to-end run summary

M10b was a 1-day end-to-end Session B run (2026-05-25 → 2026-05-26), entirely under the v2_8 methodology. The post-split fresh-design cluster was small enough (17 terms, 515V) to roll through all phases in sequence:

| Phase | Action | Notes |
|---|---|---|
| 1 | UT review via API | 134 UT verses → 111 R / 22 S / 1 borderline |
| 2 | Pass A meanings + keywords | 514 verses → meanings + 5 atomic keywords each; 2,167 distinct keywords |
| — | Hygiene | 19 orphan vc rows soft-deleted (parents delete_flagged upstream) |
| 3 | Constitution debate | 17/17 STAYS (15 with cross-register flags to M27/M10/M06/M03/M10c); 0 TRANSFERS; 0 BOUNDARY |
| — | Ezr 9:11 borderline | Disposed as is_relevant=1 (parent to.e.vah STAYS); meaning + keywords added |
| 4 | SKIPPED | Per §7.5 (no transfers); status flip deferred to Phase 6 |
| 5 | Sub-group design | 6 characteristics → 6 sub-groups (1:1, no volume-splits); §8.6 PASS |
| 6 | Sub-group apply | 6 cluster_subgroup + 20 mti_term_subgroup + 515 vc routings; status flip |
| 7 | VCG design | 36 VCGs across 6 sub-groups; 3 mandatory polysemy splits preserved; 42 anchors (36 VCG-primary + 6 R4-supplementary) |
| 8 | Dissolve inherited VCGs | 30 pre-pivot per-term VCGs soft-deleted (uniform OBSOLETE) |
| 8.5 | BOUNDARY resolution | NO-OP confirmed |
| 8.7 | Characteristic mapping | 6 characteristics, 1:1 with sub-groups (all is_partial=0); 3 INTEGRATION_NOTE carry-forwards |
| 9 A | Per-char findings | 6 AI sessions × 189 prompts = 1,134 findings (94.6% E) |
| 9 B | Cluster synthesis | 189 cluster-scope findings + 26 KB free-form appendix (95.8% E) |
| 11 | Validation + fold | Fold = no-op; 11/11 validation checks PASS |
| 12 | Closure | Status `Analysis Completed` |

## Comparison: M10b vs sibling M10

| | M10 | M10b |
|---|---:|---:|
| Terms | 63 | 17 |
| Active is_relevant verses | 1,325 | 515 |
| Characteristics | 22 | 6 |
| Sub-groups | 23 (with 1 BOUNDARY) | 6 |
| VCGs | 69 | 36 |
| cluster_finding rows | 4,158 (no synthesis yet) | 1,323 |
| E rate | 91.9% | 94.9% |
| Status | Analysis - In Progress (Phase 9 done, no Stage B yet) | **Analysis Completed** |

M10b reaches Analysis Completed first; M10 still needs its Stage B synthesis. M10c (Defilement and Impurity) remains `Not started`.

## Next

- **Session C cluster publication** — M10b is ready. The 6-characteristic structure + 1,323 findings + appendix is the input. Per `wa-sessionc-cluster-overview [current]`, Session C produces 7 publication chapters + appendices.
- M10c — the third sibling cluster from the 2026-05-22 split — remains awaiting its own Phase 1.
