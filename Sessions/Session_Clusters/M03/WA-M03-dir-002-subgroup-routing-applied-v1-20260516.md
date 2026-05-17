# WA-M03-dir-002-subgroup-routing-applied-v1-20260516

**Phase 6 (v2_2):** Sub-group creation + term-to-sub-group placement + verse routing
**Apply timestamp:** 2026-05-16T19:10:59Z
**Loader:** [scripts/_apply_m03_phase6_subgroup_routing_20260516.py](../../../scripts/_apply_m03_phase6_subgroup_routing_20260516.py)
**Directive id:** `DIR-20260516-016`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §9
**Source design:** [files phase 5/WA-M03-subgroup-design-v1-20260516.md](files%20phase%205/WA-M03-subgroup-design-v1-20260516.md)
**Source mapping:** [files phase 5/WA-M03-subgroup-mapping-v1-20260516.json](files%20phase%205/WA-M03-subgroup-mapping-v1-20260516.json)

---

## Outcome

**8 sub-groups inserted · 82 term placements · 691 verses routed.**

All six health checks PASS. `cluster.status` unchanged at `Analysis - In Progress`.

## Sub-groups inserted

| sort | subgroup_code | label | terms (primary) | verses routed |
|---:|---|---|---:|---:|
| 1 | M03-A | Weeping and Tears | 8 | 170 |
| 2 | M03-B | Mourning and Lamentation | 11 | 117 |
| 3 | M03-C | Sorrow and Inner Grief | 6 | 46 |
| 4 | M03-D | Anguish and Distress | 6 | 105 |
| 5 | M03-E | Groaning and Sighing | 7 | 31 |
| 6 | M03-F | Pain and Inner Ache | 5 | 36 |
| 7 | M03-G | Bitterness of Soul | 6 | 8 |
| 8 | M03-BOUNDARY | Boundary Terms | (28 boundary) | 178 |
| | **TOTAL** | | **49 primary + 28 boundary** | **691** |

5 secondary placements: pen.the.o (42) → M03-C; penthos (43) → M03-C; a.na.qah (898) → M03-A *and* M03-E; ōdinō (7472) → M03-D.

## Term-routing note

`mti_term_id 898` (a.na.qah, H0603) has **no primary placement** in AI's design — it appears as secondary in both M03-A and M03-E. The verse-routing mapping resolves the term to **M03-A** (groaning-paired-with-weeping at Mal 2:13). Op C honours that routing without synthesising a primary placement; the term ends up with two `mti_term_subgroup` rows (both placement-type `secondary`). This is recorded as a follow-up for researcher attention at Phase 12.

## Operations applied (single transaction)

| Op | Table | Rows | Detail |
|---|---|---:|---|
| A | `cluster_subgroup` | 8 INSERT | M03-A..G + M03-BOUNDARY, `status=active`, `version=v1`, `source=DIR-20260516-016` |
| B | `mti_term_subgroup` | 82 INSERT | 49 primary + 5 secondary + 28 boundary placements |
| C | `verse_context.cluster_subgroup_id` | 691 UPDATE | mechanical per `verse_assignments_by_term.mti_term_id_to_subgroup` |

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| H1 active M03 sub-groups | 8 | 8 ✓ |
| H2 is_relevant verses missing routing | 0 | 0 ✓ |
| H3 is_relevant verses routed | 691 | 691 ✓ |
| H4 active term placements | (positive) | 82 ✓ |
| H5 verse routing distribution | (recorded above) | matches mapping ✓ |
| H6 cluster.status | `Analysis - In Progress` | `Analysis - In Progress` ✓ |

## Provenance

- Sub-group design: [files phase 5/WA-M03-subgroup-design-v1-20260516.md](files%20phase%205/WA-M03-subgroup-design-v1-20260516.md)
- Mapping JSON: [files phase 5/WA-M03-subgroup-mapping-v1-20260516.json](files%20phase%205/WA-M03-subgroup-mapping-v1-20260516.json)
- Phase 5 brief: [WA-M03-phase5-brief-to-AI-v1-20260516.md](WA-M03-phase5-brief-to-AI-v1-20260516.md)
- Apply script: [scripts/_apply_m03_phase6_subgroup_routing_20260516.py](../../../scripts/_apply_m03_phase6_subgroup_routing_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_191035_DIR-20260516-016.db`

---

## Next step — Phase 7 (CC: per-sub-group meanings report + brief; AI: VCG design)

CC will:

1. Generate per-sub-group meanings report (`WA-M03-vcg-input-report-v1-20260516.md`) — one section per sub-group with the meaning corpus, in canonical order.
2. Draft Phase 7 brief for AI (VCG design over the 7 characteristic-bearing sub-groups; M03-BOUNDARY is structural-only at Phase 7).

*End of applied report.*
