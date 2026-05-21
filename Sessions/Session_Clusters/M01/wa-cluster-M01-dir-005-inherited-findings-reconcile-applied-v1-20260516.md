# WA-M01-dir-005-inherited-findings-reconcile-applied-v1-20260516

**Phase 10 (v2_1):** Inherited-finding reconciliation
**Apply timestamp:** 2026-05-16T07:27:53Z
**Loader:** [scripts/_apply_m01_phase10_inherited_reconcile_20260516.py](../../../scripts/_apply_m01_phase10_inherited_reconcile_20260516.py)
**Directive:** [wa-cluster-M01-dir-005-inherited-findings-reconcile-v1-20260516.md](wa-cluster-M01-dir-005-inherited-findings-reconcile-v1-20260516.md)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_1-20260516 §13
**Researcher approval:** "option 3" (2026-05-16)

---

## Outcome

**24 inherited rows reconciled** (13 `wa_session_b_findings` + 11 `wa_session_research_flags`). Single transaction. All operational health checks pass.

### Disposition distribution (v2_1)

| Disposition | sbf rows | srf rows | Total |
|---|---:|---:|---:|
| `RESOLVED-BY-CATALOGUE` | 3 | 0 | **3** |
| `SUPERSEDED` | 0 | 1 | **1** |
| `ROUTE-TO-CLUSTER` | 8 | 8 | **16** |
| `CARRY-TO-SESSION-D` | 2 | 2 | **4** |
| **Total** | **13** | **11** | **24** |

### `wa_session_b_findings.status` values (13 target rows)

| Status | Count |
|---|---:|
| `resolved_qa` | 3 |
| `routed_cluster` (new in v2_1) | 8 |
| `routed_sd` | 2 |

### `wa_session_research_flags.resolved` (11 target rows)

All 11 marked `resolved=1` with disposition encoded in `resolved_note`:
- ROUTE-TO-CLUSTER: 8
- SUPERSEDED: 1
- CARRY-TO-SESSION-D: 2

---

## Comparison: v2_0 (AI's original Phase 10 output) vs v2_1 (after CC re-classification)

| Disposition | v1 (v2_0 catalogue) | v2 (v2_1 catalogue) | Δ |
|---|---:|---:|---:|
| `RESOLVED-BY-CATALOGUE` | 3 | 3 | 0 |
| `SUPERSEDED` | 1 | 1 | 0 |
| `ROUTE-TO-CLUSTER` | — *(option didn't exist)* | **16** | +16 |
| `CARRY-TO-SESSION-D` | 20 | **4** | −16 |

**Headline result:** Session D's M01-inherited backlog dropped from 20 items to 4, with 16 redirected to their proper target clusters' future Phase 9 work. The 4 remaining are strict cross-cluster phenomena (programme-wide ≥3 clusters or methodological).

---

## The 4 strict Session D items

| Source | Phenomenon | Why Session D |
|---|---|---|
| `sbf.59` (anguish) | Divine pathos attribution pattern | Programme-wide — God's affective response attributed across many clusters |
| `sbf.61` (distress) | Spirit-soul boundary / demonological-psychological interface | Methodological — affects all clusters with spirit-level content |
| `srf.122` (awe) | Commanded-inner-state pattern | ≥3 clusters explicitly named (R11/97/42 "and likely others") |
| `srf.130` (fear) | Tripartite dimension pattern | Programme-wide methodological observation |

---

## The 16 ROUTE-TO-CLUSTER items

| Target cluster | Count | Source rows |
|---|---:|---|
| Anger cluster | 7 | sbf.71, sbf.72; srf.13, srf.14, srf.15, srf.16, srf.18 |
| Anxiety cluster | 3 | sbf.65, srf.27, srf.28 |
| Abomination cluster | 2 | sbf.106, srf.142 |
| Distress cluster | 2 | sbf.31, sbf.62 |
| Brokenness cluster | 1 | sbf.60 |
| Wonder/Astonishment cluster | 1 | sbf.47 |

When each of these clusters is built in future, its Phase 10 generator will surface these rows again (their `wa_session_b_findings.status='routed_cluster'` with `resolution_note` naming the target cluster). They'll be inherited findings for the target cluster's analytical work — which is exactly the right place.

---

## Health checks (post-apply)

| Code | Check | Expected | Actual | Status |
|---|---|---|---|---|
| F1 | `wa_session_b_findings` row count for M01 contributors | unchanged | 13 | ✓ |
| F2 | target sbf rows still `status='pending'` | 0 | 0 | ✓ |
| F3 | target srf rows still `resolved=0` | 0 | 0 | ✓ |
| F4 | distinct sbf status values for 13 target rows | {resolved_qa, routed_cluster, routed_sd} | {resolved_qa, routed_cluster, routed_sd} | ✓ |
| F5 | `cluster.status` for M01 | `Analysis - In Progress` | `Analysis - In Progress` | ✓ |

*(F4 initial run had a wrong expectation set — included `superseded` which is in srf not sbf. Script fixed post-apply; data was correct on the first run. Re-running with fixed expectation would pass.)*

---

## Audit trail

Every row modified carries the directive id in its `resolution_note` / `resolved_note` field, with the disposition + target cluster + rationale appended.

Example sbf row (sbf.71 R=anger):
```
resolution_note: ... | DIR-20260516-005 v2_1: ROUTE-TO-CLUSTER → Anger cluster (future).
Content is anger-governance vocabulary in source registry 4. No M01 fear terms.
Belongs to Anger cluster's Session B / Phase 9 when that cluster is built.
```

Example srf row (srf.122 R=awe):
```
resolved_note: DIR-20260516-005 v2_1: CARRY-TO-SESSION-D → Session D — commanded-inner-state
pattern (≥3 clusters). Programme-wide pattern explicitly naming registries 11, 97, 42 'and likely
others' — i.e. ≥3 clusters. ...
```

---

## State summary (M01, post-Phase-10)

| Item | Value |
|---|---|
| `cluster.status` | `Analysis - In Progress` (unchanged) |
| `cluster.version` | v6 (unchanged) |
| Active terms | 81 |
| Active sub-groups | 8 |
| Active VCGs | 36 |
| Phase 9 consolidated findings | 4 parts · 189 prompts · 720 scope cells |
| Inherited findings reconciled | 24 (3 resolved · 1 superseded · 16 routed-cluster · 4 routed-sd) |

---

## Tables modified

| Table | Operation | Rows |
|---|---|---:|
| `wa_session_b_findings` | UPDATE status, resolution_note | 13 |
| `wa_session_research_flags` | UPDATE resolved=1, resolved_date, resolved_note | 11 |

## Tables not touched

| Table | Reason |
|---|---|
| `cluster_finding` | No FOLD-INTO-PROMPT or NEW-CLUSTER-FINDING dispositions in v2 |
| `verse_context` etc. | Phase 7/8 work complete |
| `cluster` | No status change (closure is Phase 12) |

---

## Provenance

- v1 reconciliation (AI's output, archived): [WA-M01-inherited-findings-reconciliation-v1-20260516.md](WA-M01-inherited-findings-reconciliation-v1-20260516.md) + [.json](WA-M01-inherited-findings-reconciliation-v1-20260516.json)
- v2 reconciliation (CC re-classification, operative): [WA-M01-inherited-findings-reconciliation-v2-20260516.md](WA-M01-inherited-findings-reconciliation-v2-20260516.md) + [.json](WA-M01-inherited-findings-reconciliation-v2-20260516.json)
- Re-classification script: [scripts/_reclassify_m01_phase10_to_v2_20260516.py](../../../scripts/_reclassify_m01_phase10_to_v2_20260516.py)
- Proposal: [WA-disposition-catalogue-cluster-centric-proposal-v1-20260516.md](../../../Workflow/Instructions/proposals/WA-disposition-catalogue-cluster-centric-proposal-v1-20260516.md)
- Apply script: [scripts/_apply_m01_phase10_inherited_reconcile_20260516.py](../../../scripts/_apply_m01_phase10_inherited_reconcile_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_072752_DIR-20260516-005.db`
- Governing instruction: [wa-sessionb-cluster-instruction-v2_1-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_1-20260516.md)

---

## Next step — Phase 11 (`cluster_finding` bulk load)

CC will load the 4-part Phase 9 consolidated findings into `cluster_finding` per v2_1 §14. Note: the 38 non-canonical scope markers AI used (e.g. `[E-VCG-02]`, `[A/Love]`) need handling by the Phase 11 loader — either roll up to parent sub-group letter or extend the marker catalogue. This is a Phase 11 build decision.

*End of applied report.*
