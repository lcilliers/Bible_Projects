# WA-M01-dir-006-findings-record-applied-v1-20260516

**Phase 11 (v2_2):** `cluster_finding` bulk load + inherited-finding fold-in
**Apply timestamp:** 2026-05-16T09:39:43Z
**Loader:** [scripts/_apply_m01_phase11_findings_load_20260516.py](../../../scripts/_apply_m01_phase11_findings_load_20260516.py)
**Directive:** [wa-cluster-M01-dir-006-findings-record-v1-20260516.md](wa-cluster-M01-dir-006-findings-record-v1-20260516.md)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §14
**Schema:** 3.22.0 (migration M48 applied just prior)

---

## Outcome

**805 `cluster_finding` rows inserted · 3 inherited findings folded into 14 of those rows · all health checks pass.**

| Operation | Rows |
|---|---:|
| Op A — INSERT cluster_finding | 805 |
| Op B — Fold inherited findings | 3 source rows folded into 14 cluster_finding rows |
| Op C — UPDATE `wa_session_b_findings.resolution_note` | 3 |

---

## Status distribution (M01 v1-20260516)

| Status | Count | Meaning |
|---|---:|---|
| `finding` | 543 | E-coded findings for sub-group scopes |
| `cluster_synthesis` | 147 | E-coded findings for CLUSTER scope (programme-wide synthesis) |
| `silent` | 115 | S-coded — evidence is silent on the prompt for this scope |
| `gap` | 0 | G-coded — none used in M01 Phase 9 output |
| **Total** | **805** | |

Cross-prompt average: 805 / 189 ≈ **4.3 scope cells per prompt**.

---

## VCG-level scope (v2_2 innovation)

**36 rows** carry a non-NULL `vcg_scope` — preserving AI's analytical precision where a finding applies to specific VCGs within a sub-group rather than the whole sub-group. Examples:

- `M01-E-VCG-02` (single VCG — Isa 66:2 trembling-at-God's-word)
- `M01-E-VCG-01;M01-E-VCG-03;M01-E-VCG-04;M01-E-VCG-05` (semicolon-joined list — somatic trembling sub-VCGs silent at spirit level)

Without v2_2 §14.4 + migration M48, these 36 cells would have either dissolved into text (losing queryability) or violated the original UNIQUE constraint.

---

## Cross-cluster axis markers (v2_2 innovation)

**2 markers absorbed** — both in prompt T6.6.2 ("What does the shared anchor reveal about the relationship between the two characteristics?"):

- `[A/Love]` (M01 ↔ Love cluster — 1Jo 4:18 shared anchor)
- `[A/Wisdom]` (M01 ↔ Wisdom cluster — Pro 1:7 shared anchor)

Per v2_2 §14.4.1, these merged into T6.6.2's CLUSTER row with `**M01 ↔ {axis} pair:**` prefix. No separate cluster_finding rows for cross-cluster pair markers.

---

## Fold operation (v2_2 §14.5)

Three inherited Session B findings flagged RESOLVED-BY-CATALOGUE in Phase 10 had their full text folded into the matching cluster_finding rows:

| Source | Registry | T-codes × scopes targeted | Rows receiving fold |
|---|---|---|---:|
| `sbf.id=38` | awe | T0.3.1[A], T1.8.1[A], T1.8.3[A], T3.4.1[A] | 4 |
| `sbf.id=67` | fear | T1.2.1[A], T1.2.1[B], T1.4.2[A], T1.4.2[B], T1.4.2[CLUSTER], T7.1.3[A] | 6 |
| `sbf.id=68` | fear | T1.4.1[B], T4.1.1[B], T5.2.1[B], T5.3.1[B] | 4 |
| **Total** | | | **14** |

Each folded cluster_finding row's `finding_text` now carries:

```
**[Folded from wa_session_b_findings.id={N}; finding_id={F}; registry={W}]**
{original inherited finding text}
```

After fold:
- `wa_session_b_findings.resolution_note` updated to record the cluster_finding ids that received the fold.
- The 3 source `wa_session_b_findings` rows retain `status='resolved_qa'` (unchanged from Phase 10).

This implements the principle: every inherited observation's analytical content reaches the Tier-keyed corpus where applicable, with audit chain intact.

---

## Health checks (post-apply)

| Code | Check | Expected | Actual | Status |
|---|---|---|---|---|
| P1 | `cluster_finding` rows for M01 v=v1-20260516 | ≥189 | 805 | ✓ |
| P2 | distinct prompts covered | 189 | 189 | ✓ |
| P3 | status sums to row count | 805 | 543+147+115+0=805 | ✓ |
| P4 | rows with `vcg_scope` populated | ~36 (38 markers - merges) | 36 | ✓ |
| P5 | rows carrying fold-in markers | 14 | 14 | ✓ |

---

## Comparison with prior cluster loads

| Cluster | cluster_finding rows | Status epoch |
|---|---:|---|
| M05 | 1517 | pre-v2_2 (no vcg_scope) |
| M06 | 1516 | pre-v2_2 |
| M15 | 1724 | pre-v2_2 |
| M20 | 525 | pre-v2_2 |
| M26 | 677 | pre-v2_2 |
| M39 | 384 | pre-v2_2 |
| M46 | 381 | pre-v2_2 |
| **M01** | **805** | **first cluster on v2_2 schema** |

M01's 805 sits in the typical range for v2_0+ clusters (which use sub-group scope expansion rather than registry-style cells). 36 of M01's rows are the first instances of vcg_scope-keyed findings in the corpus.

---

## State summary (M01, post-Phase-11)

| Item | Value |
|---|---|
| `cluster.status` | `Analysis - In Progress` (unchanged — closure is Phase 12) |
| `cluster.version` | v6 |
| Active terms | 81 · Active sub-groups | 8 · Active VCGs | 36 |
| `cluster_finding` rows (M01) | **805** |
| Inherited findings reconciled | 24 (Phase 10) — 3 of which folded into cluster_finding (Phase 11 Op B) |
| Phase 11 schema | 3.22.0 (M48: vcg_scope) |
| Phase 11 instruction | v2_2 |

---

## Tables modified

| Table | Operation | Rows |
|---|---|---:|
| `cluster_finding` | INSERT | 805 (Op A) |
| `cluster_finding` | UPDATE (fold-in text append) | 14 (Op B) |
| `wa_session_b_findings` | UPDATE `resolution_note` (record fold targets) | 3 (Op C) |

## Tables not touched

| Table | Reason |
|---|---|
| `cluster` | No status change — Phase 12 owns closure |
| `verse_context_group`, `vcg_term`, `verse_context` | Phase 7/8 final |
| `cluster_subgroup`, `mti_term_subgroup` | Phase 6 final |
| `wa_session_research_flags` | Phase 10 final |

---

## Provenance

- Phase 9 consolidated findings (parts 1–4): present at cluster root
- Phase 10 v2 reconciliation: [WA-M01-inherited-findings-reconciliation-v2-20260516.md](WA-M01-inherited-findings-reconciliation-v2-20260516.md) + [.json](WA-M01-inherited-findings-reconciliation-v2-20260516.json)
- Schema migration M48: [scripts/_migrate_m48_cluster_finding_vcg_scope_20260516.py](../../../scripts/_migrate_m48_cluster_finding_vcg_scope_20260516.py)
- v2_2 instruction: [Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)
- Apply script: [scripts/_apply_m01_phase11_findings_load_20260516.py](../../../scripts/_apply_m01_phase11_findings_load_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_093942_DIR-20260516-006.db`

---

## Next step — Phase 12 (cluster closure)

Validate cluster completeness, transition `cluster.status` from `Analysis - In Progress` to `Analysis Completed`. CC-only operation per v2_2 §15.

*End of applied report.*
