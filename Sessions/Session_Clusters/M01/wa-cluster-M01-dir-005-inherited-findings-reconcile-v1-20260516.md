# wa-cluster-M01-dir-005-inherited-findings-reconcile-v1-20260516

**Phase 10 (v2_1):** Inherited-finding reconciliation
**Cluster:** `M01` Fear, Dread and Terror
**Date:** 2026-05-16
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_1-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_1-20260516.md) §13
**Researcher approval:** "option 3" (2026-05-16) — CC re-classifies AI's v1 output using v2_1 cluster-centric criterion; no AI round-trip.

---

## 1. Purpose

For each of the 24 inherited Session B findings / research flags attached to M01's contributor registries, apply its v2_1 disposition (status + resolution_note). No DELETE; only UPDATE.

This is the first cluster to apply v2_1's cluster-centric disposition catalogue. v1 of the reconciliation (AI's Phase 10 output under v2_0) is preserved on disk for audit; v2 (CC re-classification under researcher Option III) is the operative input to this directive.

## 2. Inputs

- v1 reconciliation (AI's Phase 10 output, archived): [WA-M01-inherited-findings-reconciliation-v1-20260516.md](WA-M01-inherited-findings-reconciliation-v1-20260516.md) + [.json](WA-M01-inherited-findings-reconciliation-v1-20260516.json)
- v2 reconciliation (CC re-classification, operative): [WA-M01-inherited-findings-reconciliation-v2-20260516.md](WA-M01-inherited-findings-reconciliation-v2-20260516.md) + [.json](WA-M01-inherited-findings-reconciliation-v2-20260516.json)
- Inherited findings carry-over report: [WA-M01-inherited-findings-for-reconciliation-v1-20260516.md](WA-M01-inherited-findings-for-reconciliation-v1-20260516.md)
- v2_1 catalogue + decision tree: §13.2 + §13.2.1 of the governing instruction
- v2_1 Op A status mapping: §13.4 of the governing instruction
- Proposal: [WA-disposition-catalogue-cluster-centric-proposal-v1-20260516.md](../../../Workflow/Instructions/proposals/WA-disposition-catalogue-cluster-centric-proposal-v1-20260516.md)

## 3. Scope

24 rows: 13 `wa_session_b_findings` rows + 11 `wa_session_research_flags` rows. No `session_d_term_links` rows (cluster has 0).

### Disposition distribution (v2)

| Disposition | Count |
|---|---:|
| `RESOLVED-BY-CATALOGUE` | 3 |
| `SUPERSEDED` | 1 |
| `ROUTE-TO-CLUSTER` | 16 |
| `CARRY-TO-SESSION-D` | 4 |
| **Total** | **24** |

## 4. Pre-conditions (verified)

| Check | Expected | Actual | Status |
|---|---|---|---|
| v2 reconciliation JSON present | yes | yes | ✓ |
| Total rows in v2 = total rows in inherited-findings report | 24 | 24 | ✓ |
| Every row has a disposition | yes | yes | ✓ |
| No `RESEARCHER-DECISION` rows requiring researcher gate | 0 | 0 | ✓ |
| `cluster.status` for M01 | `Analysis - In Progress` | `Analysis - In Progress` | ✓ |

## 5. Operations

### Op A — UPDATE `wa_session_b_findings.status` + `resolution_note` (13 rows)

Per v2_1 §13.4 mapping table. For each of the 13 rows in v2 JSON with `source='wa_session_b_findings'`:

```sql
UPDATE wa_session_b_findings
SET status = <mapped_status>,
    resolution_note = COALESCE(resolution_note, '') || <audit_text>
WHERE id = <row_id>;
```

`audit_text` = `' | DIR-20260516-005: {disposition} → {target}. {rationale}'`

### Op B — UPDATE `wa_session_research_flags` (11 rows)

For each of the 11 rows in v2 JSON with `source='wa_session_research_flags'`:

```sql
UPDATE wa_session_research_flags
SET resolved = 1,
    resolved_date = '2026-05-16',
    resolved_note = <audit_text>
WHERE id = <row_id>;
```

### Op C — UPDATE `cluster_finding` (0 rows)

No `FOLD-INTO-PROMPT` dispositions in v2 — operation skipped.

### Op D — INSERT new `cluster_finding` rows (0 rows)

No `NEW-CLUSTER-FINDING` dispositions in v2 — operation skipped.

## 6. Health checks (post-apply)

| Code | Check | Expected |
|---|---|---|
| F1 | `wa_session_b_findings` row count for M01 contributor registries | unchanged (no DELETE) |
| F2 | `wa_session_b_findings` rows with status `pending` for M01 contributor terms (target subset of 13) | 0 |
| F3 | `wa_session_research_flags` rows with `resolved=0` for M01 contributor registries (target subset of 11) | 0 |
| F4 | Distinct new status values introduced | includes `routed_cluster` (16) and `routed_sd` (4) |
| F5 | `cluster.status` for M01 | unchanged (`Analysis - In Progress`) |

## 7. Status transition (within this directive, per v2_1 §2.6)

No standalone status transition — `cluster.status` stays `Analysis - In Progress`. Closure is Phase 12.

## 8. Provenance & roll-back

- **Pre-apply backup:** `backups/bible_research_backup_*_DIR-20260516-005.db`
- **Audit:** every modified row carries directive id in its resolution_note / resolved_note.
- **Roll-back:** restore from pre-apply backup; OR run inverse patch resetting status / resolved per row using snapshot.

---

*End of directive.*
