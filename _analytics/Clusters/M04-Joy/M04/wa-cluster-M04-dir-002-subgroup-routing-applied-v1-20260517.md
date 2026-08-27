# WA-M04-dir-002-subgroup-routing-applied-v1-20260517

**Phase 6 (v2_2):** Sub-group creation + term-to-sub-group placement + verse routing
**Apply timestamp:** 2026-05-17T11:47:53Z
**Loader:** [scripts/_apply_m04_phase6_subgroup_routing_20260517.py](../../../scripts/_apply_m04_phase6_subgroup_routing_20260517.py)
**Directive id:** `DIR-20260517-005`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §9
**Source design:** [files phase 5/WA-M04-subgroup-design-v1-20260517.md](files%20phase%205/WA-M04-subgroup-design-v1-20260517.md)
**Source mapping:** [files phase 5/WA-M04-subgroup-mapping-v1-20260517.json](files%20phase%205/WA-M04-subgroup-mapping-v1-20260517.json)

---

## Outcome

**7 sub-groups inserted · 86 term placements · 1138 verses routed.**

All six health checks PASS. `cluster.status M04` unchanged at `Analysis - In Progress`.

## Sub-groups inserted

| sort | subgroup_code | label | terms routed (primary) | verses routed |
|---:|---|---|---:|---:|
| 1 | M04-A | Exultant Joy in the LORD | 28 | 661 |
| 2 | M04-B | Communal and Festive Rejoicing | 2 | 10 |
| 3 | M04-C | Delight in God's Word and Law | 3 | 16 |
| 4 | M04-D | Promised and Eschatological Joy | 2 | 24 |
| 5 | M04-E | Pleasantness and Relational Delight | 5 | 28 |
| 6 | M04-F | Wonder at God's Marvellous Works | 3 | 77 |
| 7 | M04-BOUNDARY | Boundary Terms | (15 boundary) | 322 |
| | **TOTAL** | | **43 primary + 15 boundary** | **1138** |

**Note:** M04-A absorbs 661 of 816 substantive verses (81% of the substantive corpus) — driven by sa.mach (147), sim.chah (89), chairō (58), chara (57), gil_verb (44), su.s (23), sa.s.von (22 — routed to M04-D), sa.me.ach (21), ma.s.vo.s (16), and ~20 other rejoicing terms. M04-BOUNDARY's 322-verse weight is dominated by H2896A tov (230 verses).

## Primary-label reconciliation (5 fixes)

AI's design had 4 label inconsistencies that CC reconciled at apply time. The verse-routing mapping is the source of truth for primary placement; design's other "primary" labels were downgraded to "secondary".

| mti_id | Strong's | Translit | Issue | Reconciliation |
|---:|---|---|---|---|
| 3844 | H8173B | sha.a | listed primary in both M04-A and M04-C | mapping=M04-C → kept primary at M04-C; downgraded M04-A to secondary |
| 790 | H8191 | sha.a.shu.im | listed primary in both M04-A and M04-C | mapping=M04-C → kept primary at M04-C; downgraded M04-A to secondary |
| 3837 | H5730B | ed.nah | listed primary in both M04-A and M04-E | mapping=M04-E → kept primary at M04-E; downgraded M04-A to secondary |
| 361 | H8342 | sa.s.von | listed primary M04-A only, secondary M04-D; mapping routes to M04-D | upgraded M04-D from secondary to primary; downgraded M04-A from primary to secondary |

After reconciliation: 43 primary placements (one per STAYS term) + 28 secondary + 15 boundary = 86 total.

## Operations applied (single transaction)

| Op | Table | Rows | Detail |
|---|---|---:|---|
| A | `cluster_subgroup` | 7 INSERT | M04-A..F + M04-BOUNDARY, `status=active`, `version=v1`, `source=DIR-20260517-005` |
| B | `mti_term_subgroup` | 86 INSERT | 43 primary + 28 secondary + 15 boundary (reconciliation note in placement_note) |
| C | `verse_context.cluster_subgroup_id` | 1138 UPDATE | mechanical per `verse_assignments_by_term.mti_term_id_to_subgroup` |

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| H1 active M04 sub-groups | 7 | 7 ✓ |
| H2 is_relevant verses missing routing | 0 | 0 ✓ |
| H3 is_relevant verses routed | 1138 | 1138 ✓ |
| H4 active term placements | (positive) | 86 ✓ |
| H5 verse routing distribution | (recorded above) | matches mapping ✓ |
| H6 cluster.status | `Analysis - In Progress` | `Analysis - In Progress` ✓ |

## Provenance

- Sub-group design: [files phase 5/WA-M04-subgroup-design-v1-20260517.md](files%20phase%205/WA-M04-subgroup-design-v1-20260517.md)
- Mapping JSON: [files phase 5/WA-M04-subgroup-mapping-v1-20260517.json](files%20phase%205/WA-M04-subgroup-mapping-v1-20260517.json)
- Phase 5 brief: [WA-M04-phase5-brief-to-AI-v1-20260517.md](WA-M04-phase5-brief-to-AI-v1-20260517.md)
- Apply script: [scripts/_apply_m04_phase6_subgroup_routing_20260517.py](../../../scripts/_apply_m04_phase6_subgroup_routing_20260517.py)
- Pre-apply backup: `backups/bible_research_backup_20260517_*_DIR-20260517-005.db`

---

## Next step — Phase 7 (CC: per-sub-group meanings report + brief; AI: VCG design)

CC will:

1. Generate per-sub-group meanings report (`WA-M04-vcg-input-report-v1-20260517.md`) — one section per sub-group with the meaning corpus, in canonical order.
2. Draft Phase 7 brief for AI VCG design (over the 6 characteristic-bearing sub-groups; M04-BOUNDARY is structural-only at Phase 7).

*End of applied report.*
