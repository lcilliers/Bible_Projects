# #2286 prototype step 9: surface subgroups in bulk, as an extension of clustering (E3, ruled)

Date: 2026-10-25. Escalation #2286 v22. **v2** carries the researcher's rulings on the conditions.
The earlier version is in `outputs/escalation/archive/2286-bulk-surface-mapping-e3-v1-20261025.md`.
Nothing is built: the design (the new table, the step, the config) comes to the researcher first
(B:105).

## 0. The rulings so far (verbatim)

v20:
> E1 - agree, strongly; E2 - surface to verse is in the verse-lexical table. Cluster to sub group is
> saved in sub group table. surface to subgroup is saved in a new table. E3 - is there any reason why
> the sub group mapping cannot be done prior to Analysis in bulk, similar to what was done for cluster
> work. E4 - this decision is not clear. more exploration is needed for it.

v22:
> conditions: 1 API can be used for LLM work to allocate the tail. 2 - agree, set flag on
> surface_subgroup table. 3. agree, and this should be stressed in the analytic phase. 4 agree, there
> are deemed to be anomalies, group them in a bucked where they can be cleared manually. 5 agree, and
> must be enforced. The bulk update of the subgroups will sit in the program at the same stage as
> clustering, it is in fact an extension of clustering. I am concerned that we did not deal with E4
> and T-code clusters. lets think through that after you updated the documentation with the above.

## 1. What is decided

| # | decision | source |
|---|---|---|
| E1 | Subgroups are based on the **surface** (the ESV rendering in `verse_lexical.surface`), not the gloss. | v20 |
| E2 | Storage: surface to verse is already in `verse_lexical`; cluster to subgroup in `cluster_subgroup`; **surface to subgroup in a new table** (`surface_subgroup`). | v20, v22 |
| E3a | The mapping is done **in bulk, before analysis**. | v20, v22 |
| E3-stage | It sits in the programme **at the same stage as clustering**: it is an extension of clustering (governance.programme_stages, Base_data). | v22 |
| C1 | Each cluster is mapped with its reasons recorded. **The API may be used for LLM work to allocate the tail**: the pairs left after the first pass. | v22 |
| C2 | A pair carrying two senses is **flagged on `surface_subgroup`** and settled per occurrence in the reading. | v22 |
| C3 | The mapping is **provisional, not a finding**. A reading may move a pair, with its reason. **This is to be stressed in the analytic phase.** | v22 |
| C4 | Each group gets a size check. Pairs that fit no group are **anomalies, grouped in a bucket where they are cleared manually**. | v22 |
| C5 | When a code moves cluster, its pairs' subgroups are redone, and **this must be enforced** (with #2281, the cluster status lifecycle). | v22 |

## 2. The scale (from v1, facts)

| measure | value |
|---|---|
| live M clusters | 80 |
| M-tagged codes | 2,924, each in exactly one M cluster |
| M-coded hits | 64,460, in 24,227 verses |
| (code, surface) pairs to map | 13,411 (6,029 distinct surfaces) |
| pairs covering 80% / 90% / 95% of the hits | 3,079 / 6,965 / 10,188 |
| pairs with one hit only | 8,101 |
| pairs per cluster | median 129; largest M24 582, M23 574, M15 460, M18 454, M47 393 |
| M18 trial (step 8) | 279 surfaces (454 pairs), grouped in 1 minute 44 seconds on the system clock |

## 3. What the design will have to settle

These follow from the rulings. The design will set them out with options.

- **`surface_subgroup`:** the key is the pair (code, surface). Its columns include the subgroup, the
  two-sense flag (C2), the provisional status (C3), the reason, and who or what allocated it (session,
  first pass, or API for the tail, C1).
- **The anomaly bucket** (C4): one per cluster or one for all, and how a manual clearance is recorded.
- **The occurrence-level exception** for a flagged pair: where the per-verse sense is recorded when a
  reading settles it (C2, C3).
- **The step:** registered beside the clustering steps, with its config rows and rules, built through
  the app (governance.project_change_rule).
- **The enforcement** (C5): what stops a cluster change from leaving stale pairs (#2281).
- **The existing 13 pipeline subgroups** for M49, M67 and M83 (step 7 D5), and retiring
  `cluster.subgroup` (step 7 D1, with #2275).

## 4. Still open

- **E4:** the qualifier group ("good, better, well", M18 S8). Needs more exploration.
- **The T-code clusters:** not yet considered. See step 10.
