---
name: project-characteristic-backfill-backlog
description: "Pre-v2_6 characteristic backfill — DONE 2026-05-27. All 10 closed pre-v2_6 clusters (M01, M02, M03, M05, M06, M15, M20, M26, M39, M46) now have characteristic + characteristic_subgroup rows and findings linked. 1:1 generic mapping ('workable, not perfect')."
metadata:
  node_type: memory
  type: project
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

**Status: DONE 2026-05-27.**

Schema migration M49 (applied 2026-05-18) introduced `characteristic`, `characteristic_subgroup`, `cluster_observation` tables. The 10 closed pre-v2_6 clusters were missing characteristic rows entirely; their findings were sub-group-scoped only.

Backfill applied 2026-05-27 in two passes:

1. **M03 (test cluster)** — `scripts/_apply_m03_characteristic_backfill_20260527.py` (commit fe10ab0). 7 characteristics with hand-written definitions, 237 findings linked. Established the 1:1 sub-group → characteristic pattern.

2. **Remaining 9 clusters (generic)** — `scripts/_apply_generic_characteristic_backfill_20260527.py`. Auto-derives 1:1 from existing sub-group structure (short_name = sub-group label; definition = sub-group core_description). 46 characteristics, 6,604 findings linked.

**Total final state:**

| Cluster | Chars | Findings linked | Remaining NULL findings (cluster-scope or BOUNDARY) |
|---|---:|---:|---:|
| M01 | 7 | 648 | 157 |
| M02 | 6 | 316 | 73 |
| M03 | 7 | 237 | 123 |
| M05 | 7 | 1,323 | 194 |
| M06 | 7 | 1,323 | 193 |
| M15 | 8 | 1,512 | 212 |
| M20 | 4 | 482 | 43 |
| M26 | 8 | 543 | 134 |
| M39 | 2 | 374 | 10 |
| M46 | 4 | 320 | 61 |

NULL-characteristic findings remaining = cluster-scope synthesis findings (1,094) + BOUNDARY sub-group findings (204). Both correctly excluded by design — neither is characteristic-scoped.

**Caveat ("workable, not perfect"):** the generic backfill is purely 1:1 mechanical. It does not split or merge sub-groups against deeper analytical insight. Where the original sub-group design was clean (M03), the result is fully usable. Where the sub-group structure carries pre-v2_6 baggage (M05 reset still pending; M15 has 189 BOUNDARY findings; M26 has split A1/A2), the characteristic map is the cheapest workable mapping rather than a re-thought analytic structure.

**Idempotency:** both scripts abort if characteristic rows already exist for the cluster — safe to re-run as part of larger pipelines.

**Why this was done now:** prerequisite for v3_0 publication pipeline. The pipeline expects characteristic-scoped findings (Phase D batches one characteristic at a time). Without the backfill, the 10 pre-v2_6 clusters couldn't enter the v3_0 publication routine.

Related: [[project-v25-audit-tool]], [[project-m04-paused-at-phase9]] (M04 was the precedent for the more-careful AI-designed mapping).
