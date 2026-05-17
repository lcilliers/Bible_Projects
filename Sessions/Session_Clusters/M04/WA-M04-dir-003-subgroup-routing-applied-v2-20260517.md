# WA-M04-dir-003-subgroup-routing-applied-v2-20260517

**Phase 6 v2 (post-resubmission)** — sub-group creation + term placements + verse routing
**Apply timestamp:** 2026-05-17T16:02:10Z
**Loader:** [scripts/_apply_m04_phase6_subgroup_routing_v2_20260517.py](../../../scripts/_apply_m04_phase6_subgroup_routing_v2_20260517.py)
**Directive id:** `DIR-20260517-007`
**Supersedes:** DIR-20260517-005 (v1 Phase 6, rolled back via DIR-20260517-006)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_3-20260517 §9, gated by §8.6
**Validation:** [WA-M04-phase5-distribution-validation-v2-20260517.md](WA-M04-phase5-distribution-validation-v2-20260517.md) — PASS (33.5% biggest, 1.9× ratio)
**Source design:** [files phase 5/WA-M04-subgroup-design-v2-20260517.md](files%20phase%205/WA-M04-subgroup-design-v2-20260517.md)
**Source mapping:** [files phase 5/WA-M04-subgroup-mapping-v2-20260517.json](files%20phase%205/WA-M04-subgroup-mapping-v2-20260517.json)

---

## Outcome

**11 sub-groups inserted · 75 term placements · 1138 verses routed.**

All five health checks PASS. `cluster.status M04` unchanged at `Analysis - In Progress`. §8.6 distribution gate verified PASS before apply.

## Sub-group distribution (post-v2)

| sort | subgroup_code | label | terms (primary) | verses | % of substantive |
|---:|---|---|---:|---:|---:|
| 1 | M04-A | Exultation in YHWH: Vertical Rejoicing Directed Toward God | 6 | 84 | 10.3% |
| 2 | M04-B | Communal and Festive Rejoicing: Gladness in Worship | 4 | **273** | **33.5%** |
| 3 | M04-C | NT Joy in Christ and the Spirit: Gladness of the Gospel | 8 | 143 | 17.5% |
| 4 | M04-D | Shared Communal Rejoicing: Joy as Solidarity | 2 | 10 | 1.2% |
| 5 | M04-E | Promised and Eschatological Joy: Gladness of Restoration | 3 | 35 | 4.3% |
| 6 | M04-F | Cheerfulness Under Adversity: Fragile Inner Comfort | 2 | 4 | 0.5% |
| 7 | M04-G | Delight in God's Word, Law, and Wisdom | 6 | 26 | 3.2% |
| 8 | M04-H | Volitional Delight: Inner Pleasure as Sovereign Will | 4 | 136 | 16.7% |
| 9 | M04-I | Wonder at God's Marvellous Works: Awe Before Extraordinary | 3 | 77 | 9.4% |
| 10 | M04-J | Pleasantness and Relational Delight: The Agreeable | 5 | 28 | 3.4% |
| 11 | M04-BOUNDARY | Boundary Terms | (15 boundary) | 322 | — |
| | **TOTAL** | | **43 primary + 15 boundary** | **1138** | |

## v1 vs v2 — the difference

| Metric | v1 (rejected) | v2 (applied) |
|---|---:|---:|
| Substantive sub-groups | 6 | **10** |
| Biggest sub-group share | 81% (M04-A) | **33.5%** (M04-B) |
| Biggest-to-next ratio | 8.6× | **1.9×** |
| §8.6 gate verdict | FAIL | **PASS** |

v2 distribution is comparable to M03 (33% biggest). The joy register was correctly split across multiple sub-groups instead of collapsed into one.

## Single dedup applied at Op B

AI's v2 design listed mti=790 (H8191 sha.a.shu.im) twice within M04-G — once as `primary`, once as `secondary`. The apply script collapsed this to a single primary placement (placement strength: boundary > primary > secondary). Logged as "DEDUP: mti=790 sg=M04-G: kept primary over secondary." Net result: 76 design rows → 75 mti_term_subgroup rows applied.

## Operations applied (single transaction)

| Op | Table | Rows | Detail |
|---|---|---:|---|
| A | `cluster_subgroup` | 11 INSERT | M04-A..J + M04-BOUNDARY, `status=active`, `version=v2`, `source=DIR-20260517-007` |
| B | `mti_term_subgroup` | 75 INSERT | 43 primary + 17 secondary + 15 boundary (1 intra-design dup deduped) |
| C | `verse_context.cluster_subgroup_id` | 1138 UPDATE | mechanical per mapping |

## Pre-apply housekeeping (v1 collision avoidance)

The v1 soft-deleted sub-group rows (DIR-20260517-005, rolled back via DIR-20260517-006) had original `subgroup_code` values `M04-A`...`M04-F`+`M04-BOUNDARY`. The v2 codes overlap. Without intervention, the `cluster_subgroup` UNIQUE constraint `(cluster_code, subgroup_code)` blocks v2 inserts.

Resolution: renamed v1 soft-deleted codes by appending `-rejected-v1` (one-time SQL: `UPDATE cluster_subgroup SET subgroup_code=subgroup_code||'-rejected-v1' WHERE cluster_code='M04' AND delete_flagged=1`). This preserves the historical record while clearing the namespace for v2.

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| H1 active M04 sub-groups | 11 | 11 ✓ |
| H2 is_relevant verses unrouted | 0 | 0 ✓ |
| H3 is_relevant verses routed | 1138 | 1138 ✓ |
| H4 verse routing distribution | (recorded above) | matches mapping ✓ |
| H5 cluster.status | `Analysis - In Progress` | `Analysis - In Progress` ✓ |

## Provenance

- Phase 5 v2 design: [files phase 5/WA-M04-subgroup-design-v2-20260517.md](files%20phase%205/WA-M04-subgroup-design-v2-20260517.md)
- Phase 5 v2 mapping: [files phase 5/WA-M04-subgroup-mapping-v2-20260517.json](files%20phase%205/WA-M04-subgroup-mapping-v2-20260517.json)
- Phase 5 v2 obslog: [files phase 5/wa-obslog-M04-phase5v2-v1-20260517.md](files%20phase%205/wa-obslog-M04-phase5v2-v1-20260517.md)
- Phase 5 v2 brief: [WA-M04-phase5-brief-to-AI-v2-20260517.md](WA-M04-phase5-brief-to-AI-v2-20260517.md)
- §8.6 validation report: [WA-M04-phase5-distribution-validation-v2-20260517.md](WA-M04-phase5-distribution-validation-v2-20260517.md)
- Phase 6 rollback: [WA-M04-dir-002-rollback-applied-v1-20260517.md](WA-M04-dir-002-rollback-applied-v1-20260517.md)
- v1 rejected outputs preserved: [files phase 5 rejected v1/](files%20phase%205%20rejected%20v1/)
- Pre-apply backup: `backups/bible_research_backup_20260517_*_DIR-20260517-007.db`

---

## Next step — Phase 7 v2

CC will:

1. Regenerate per-sub-group meanings report (`WA-M04-subgroup-meanings-v2-20260517.md`).
2. Draft Phase 7 v2 brief for AI VCG design across the 10 substantive sub-groups + BOUNDARY.

*End of applied report.*
