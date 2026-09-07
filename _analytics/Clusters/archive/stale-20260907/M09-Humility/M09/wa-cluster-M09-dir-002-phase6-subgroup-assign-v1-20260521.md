# wa-cluster-M09-dir-002-phase6-subgroup-assign-v1-20260521

> Cluster directive — M09 Phase 6 sub-group structural apply + verse routing
> Cluster: M09 — Humility, Meekness and Submission
> Date: 2026-05-22
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §9

---

## MOTIVATION

Phase 5 designed **8 sub-groups** (HUMILITY and SUBMISSION volume-split into A+B and C+D respectively; 4 single-characteristic sub-groups for CONTRITION, MEEKNESS, DIGNITY, WILLING_HEARTEDNESS). Phase 3 produced 0 BOUNDARY verdicts → no `M09-BOUNDARY` sub-group needed.

Sources:
- Phase 5 design: [wa-cluster-M09-subgroup-design-v1-20260521.md](wa-cluster-M09-subgroup-design-v1-20260521.md)
- Phase 5 mapping: [wa-cluster-M09-subgroup-mapping-v1-20260521.json](wa-cluster-M09-subgroup-mapping-v1-20260521.json)
- Resolved (vc_id-flat): [wa-cluster-M09-subgroup-mapping-resolved-v1-20260521.json](wa-cluster-M09-subgroup-mapping-resolved-v1-20260521.json)
- §8.6 validation: [wa-cluster-M09-phase5-distribution-validation-v1-20260521.md](wa-cluster-M09-phase5-distribution-validation-v1-20260521.md) — **PASS at 33.9%**

### Phase 8.5 flags (11 vc_ids on G1299 diatassō)

11 diatassō verses (Mat 11:1, Luk 3:13, Luk 17:9, Act 7:44, Act 18:2, 1Cor 7:17, 1Cor 9:14, 1Cor 11:34, 1Cor 16:1, Gal 3:19, Tit 1:5) have no M09 inner-being content per Pass A. **Provisionally routed to M09-D** to preserve Phase 5/6 structural integrity; Phase 8.5 will resolve (SET-ASIDE or ROUTE-TO-M23). Only Luk 17:10 of diatassō carries M09-relational content (routed to M09-C).

### Phase 5.5 flag (1 vc_id on G5013 tapeinoō)

Luk 3:5 ("mountains made low") routed to M09-A; Phase 5.5 may SET-ASIDE this single outlier alongside the diatassō flags or as a separate small patch.

## SCOPE

### Sub-group catalogue

| subgroup_code | label | characteristic | Verses |
|---|---|---|---:|
| M09-A | Humility — willed self-lowering | HUMILITY (voluntary) | 37 |
| M09-B | Lowliness — experienced and imposed state | HUMILITY (imposed) | 13 |
| M09-C | Submission — inner disposition of will | SUBMISSION (heart/conscience) | 17 |
| M09-D | Submission — relational pattern of obedience | SUBMISSION (relational) | 30 |
| M09-E | Contrition — crushed and broken spirit | CONTRITION | 2 |
| M09-F | Meekness — calibrated restraint and gentleness | MEEKNESS_GENTLENESS | 2 |
| M09-G | Dignity — grounded moral gravity | DIGNITY | 3 |
| M09-H | Willing-heartedness — the freely-moved spirit | WILLING_HEARTEDNESS | 5 |
| **Total** | | | **109** |

### Operations

**Op A — INSERT 8 cluster_subgroup rows**

```sql
INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description,
                              sort_order, status, version, source, created_at, last_updated_date)
VALUES (?, ?, ?, ?, ?, 'active', 'v1', 'wa-cluster-M09-dir-002-phase6-subgroup-assign-v1-20260521', ?, ?);
```

**Op B — INSERT mti_term_subgroup rows** for each distinct (mti_term_id, sub-group) pair.

**Op C — UPDATE verse_context.cluster_subgroup_id** for all 109 is_relevant vc_ids per resolved mapping.

**Op D (skipped)** — `cluster.M09.status` already at `'Analysis - In Progress'` (advanced at Phase 4).

## OUTCOME REQUIRED

- 8 `cluster_subgroup` rows for M09.
- ~N `mti_term_subgroup` rows (one per distinct term/sub-group pair).
- 109 `verse_context.cluster_subgroup_id` populated.
- 0 `is_relevant=1` M09 verses with `cluster_subgroup_id IS NULL` after apply.
- `cluster.M09.status` remains `'Analysis - In Progress'`.

## SCRIPT

`scripts/_apply_m09_phase6_subgroup_assign_20260521.py`
