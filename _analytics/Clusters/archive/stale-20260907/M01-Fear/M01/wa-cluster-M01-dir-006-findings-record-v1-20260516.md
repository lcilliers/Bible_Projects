# wa-cluster-M01-dir-006-findings-record-v1-20260516

**Phase 11 (v2_2):** `cluster_finding` bulk load + inherited-finding fold-in
**Cluster:** `M01` Fear, Dread and Terror
**Date:** 2026-05-16
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §14

---

## 1. Purpose

Load the 4-part Phase 9 consolidated findings into `cluster_finding`. Fold the 3 RESOLVED-BY-CATALOGUE inherited findings into the named cluster_finding rows. Schema migration M48 (vcg_scope column) was applied just prior to enable v2_2 §14.4 scope-marker resolution.

## 2. Inputs

- 4-part consolidated findings: parts 1–4
- Phase 10 reconciliation (v2): identifies the 3 RESOLVED-BY-CATALOGUE candidates for fold
- v2_2 instruction §14 (loader spec + scope-marker resolution + fold operation)
- Migration M48 (vcg_scope column added to cluster_finding)

## 3. Scope

| Element | Count |
|---|---:|
| Prompts (T0–T7) covered | 189 (full catalogue) |
| Parsed scope-marker blocks | 707 |
| `cluster_finding` rows produced | 805 |
| Rows with `vcg_scope` populated | 36 |
| Cross-cluster axis markers merged into CLUSTER rows | 2 |
| Inherited findings folded | 3 (sbf.38, sbf.67, sbf.68) |
| `cluster_finding` rows receiving fold text | 14 |

## 4. Operations

### Op A — INSERT 805 `cluster_finding` rows

Per v2_2 §14.4 scope-marker resolution. Status distribution:

| Status | Count |
|---|---:|
| `finding` | 543 |
| `cluster_synthesis` | 147 |
| `silent` | 115 |
| `gap` | 0 |

### Op B — Fold inherited RESOLVED-BY-CATALOGUE text into cluster_finding rows

| Source row | Registry | Targets | Rows folded into |
|---|---|---|---:|
| sbf.id=38 | awe | T1.8.1, T1.8.3, T3.4.1, T0.3.1 — all [A] | 4 |
| sbf.id=67 | fear | T1.4.2 [A, B, CLUSTER], T7.1.3 [A], T1.2.1 [A, B] | 6 |
| sbf.id=68 | fear | T1.4.1 [B], T5.2.1 [B], T5.3.1 [B], T4.1.1 [B] | 4 |
| **Total** | | | **14** |

Fold text prefix: `**[Folded from wa_session_b_findings.id={N}; finding_id={F}; registry={W}]**`

### Op C — UPDATE `wa_session_b_findings.resolution_note`

For each of the 3 folded rows, append `| DIR-20260516-006: folded into cluster_finding.id IN ({ids})`.

## 5. Health checks (post-apply)

| Code | Check | Expected | Actual |
|---|---|---|---|
| P1 | `cluster_finding` rows for M01 v1-20260516 | ≥189 | 805 ✓ |
| P2 | distinct prompts covered | 189 | 189 ✓ |
| P3 | status distribution sums to total | 805 | 543 + 147 + 115 = 805 ✓ |
| P4 | rows with `vcg_scope` populated | ~38 (38 non-canonical markers, some merged) | 36 ✓ |
| P5 | rows carrying fold-in `**[Folded from...]**` markers | 14 | 14 ✓ |

## 6. Provenance

- Apply script: [scripts/_apply_m01_phase11_findings_load_20260516.py](../../../scripts/_apply_m01_phase11_findings_load_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_093942_DIR-20260516-006.db`
- Schema migration M48 backup: `backups/bible_research_backup_20260516_093429_M48-vcg-scope.db`

---

*End of directive.*
