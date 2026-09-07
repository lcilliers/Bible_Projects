# WA-M02-dir-006-findings-record-applied-v1-20260516

**Phase 11 (v2_2):** `cluster_finding` bulk load + inherited-finding fold-in
**Apply timestamp:** 2026-05-16T16:33:55Z (Op A) + 2026-05-16T16:35:43Z (Op B fold patch)
**Loaders:**
- [scripts/_apply_m02_phase11_findings_load_20260516.py](../../../scripts/_apply_m02_phase11_findings_load_20260516.py) (Op A + initial Op B attempt)
- [scripts/_apply_m02_phase11_folds_fallback_20260516.py](../../../scripts/_apply_m02_phase11_folds_fallback_20260516.py) (Op B fallback)

**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §14
**Directive ids:** `DIR-20260516-013` (Op A + Op C) + `DIR-20260516-013-folds` (Op B fallback)

---

## Outcome

**389 `cluster_finding` rows inserted · 2 inherited findings folded · all health checks pass.**

| Operation | Rows |
|---|---:|
| Op A — INSERT cluster_finding | 389 |
| Op B — Fold inherited findings | 2 (sbf.74 + srf.622) |
| Op C — UPDATE resolution_note | 2 |

---

## Status distribution (M02 v1-20260516)

| Status | Count | Meaning |
|---|---:|---|
| `finding` | 289 | E-coded findings for sub-group scopes |
| `cluster_synthesis` | 56 | E-coded findings for CLUSTER scope |
| `silent` | 41 | S-coded — evidence is silent on prompt |
| `gap` | 3 | G-coded — data missing for prompt |
| **Total** | **389** | |

Cross-prompt average: 389 / 189 ≈ **2.1 scope cells per prompt** (vs M01's 4.3 — M02 used scope expansion more sparingly).

---

## VCG-level scope usage (v2_2 §14.4)

**260 of 389 rows (67%)** have a non-NULL `vcg_scope` — even higher proportion than M01 (36 of 805 = 4.5%). AI used VCG-level scope markers heavily for M02, taking full advantage of the v2_2 schema affordance.

Sample distribution:
- Single-VCG markers: 176 (e.g. `[E-VCG-02]`)
- Multi-VCG slash markers: ~41 (e.g. `[E-VCG-01/02/03/04]`)
- Plus some VCG with qualifiers (e.g. `[C-VCG-01 sustained]`) absorbed via contrast-merge

---

## Non-canonical marker handling

AI used several non-canonical scope marker forms during Phase 9. The Phase 11 loader handled them as follows:

| Marker form | Count | Handling |
|---|---:|---|
| `[A vs B]`, `[B-VCG-04 vs B-VCG-02]`, `[M02 vs M06]`, `[M02-E vs M28]` (contrast) | 20 | Merged into prompt's CLUSTER row with body prefix `**Contrast: ...**` |
| `[E-VCG-01 → D-VCG-01]`, `[C-VCG-01 → body]` (transition) | 6 | Merged into CLUSTER row with prefix `**Transition: ...**` |
| `[A-VCG-01 anchor: Heb 3:11]` (anchor focus) | 3 | Merged into CLUSTER row with prefix `**Anchor focus: ...**` |
| `[Num 25 pericope]` (pericope reference) | 1 | Merged into CLUSTER row with prefix `**Pericope: ...**` |
| `[C-VCG-01 sustained]` (VCG with qualifier suffix) | 1 | Stored as VCG-scoped row with body prefix `**Qualifier: ...**` |
| **NO scope marker** (silent-confirmation T*.X.3/.4 prompts) | ~15 | Defaulted to CLUSTER scope, outcome `S` |

All non-canonical content is preserved in `finding_text` with appropriate prefix annotations.

---

## Fold operation (v2_2 §14.5 with fallback)

Two inherited findings flagged FOLD-INTO-PROMPT in Phase 10:

| Source | Phase 10 target | Actual fold target (after fallback) | Cluster_finding id |
|---|---|---|---:|
| sbf.id=74 (R56 envy, DIM-56-001) | T0.3.2 [E-VCG-01/02/03/04] | T0.3.2 [E] sub-group level | 8147 |
| srf.id=622 (R103 love) | T6.6.2 [E-VCG-04] | T6.6.2 [CLUSTER] (E sub-group row didn't exist) | 8491 |

### Why the fallback was needed

AI's Phase 10 reconciliation pointed at VCG-level targets (`[E-VCG-01/02/03/04]`, `[E-VCG-04]`), but AI's Phase 9 authored those prompts at coarser scope (T0.3.2 at sub-group level; T6.6.2 at CLUSTER level). The exact-match fold lookup returned no rows. A fallback strategy was added (try exact VCG → sub-group level → CLUSTER) which located both targets at coarser scope. The fold preserves the inherited finding's content while accepting a slightly less-granular structural placement than AI intended.

Each folded cluster_finding row's `finding_text` now carries:

```
**[Folded from {table}.id={N}; finding_id={F}; registry={W}]**
_(Phase 10 target was T0.3.2 [E-VCG-...]; folded into available T0.3.2 row via fallback)_
{original inherited finding text}
```

`wa_session_b_findings.resolution_note` (sbf.74) and `wa_session_research_flags.resolved_note` (srf.622) updated to record the cluster_finding.id targets.

---

## Health checks (post-apply)

| Code | Check | Expected | Actual |
|---|---|---|---|
| P1 | cluster_finding rows for M02 v1-20260516 | ≥189 | 389 ✓ |
| P2 | distinct prompts covered | 189 | 189 ✓ |
| P3 | status sums to row count | 389 | 289+56+41+3=389 ✓ |
| P4 | rows with `vcg_scope` populated | ~260 | 260 ✓ |
| P5 | rows carrying fold-in markers | ≥2 | 2 ✓ |

---

## Comparison with M01 Phase 11

| Metric | M01 | M02 |
|---|---:|---:|
| cluster_finding rows | 805 | 389 |
| Prompts covered | 189 | 189 |
| Scope cells per prompt | 4.3 | 2.1 |
| `vcg_scope` rows | 36 (4.5%) | 260 (67%) |
| Fold-in count | 14 (3 sbf folded into 14 rows) | 2 (1 sbf + 1 srf each folded into 1 row) |

M02 produced fewer rows because:
1. Smaller cluster (43 active terms vs 81; 7 sub-groups vs 8)
2. Heavier use of VCG-level markers (which collapse multi-scope blocks into single VCG-scoped rows)
3. Less aggressive scope expansion (more single-letter markers vs comma-grouped)

---

## State summary (M02, post-Phase-11)

| Item | Value |
|---|---|
| `cluster.status` | `Analysis - In Progress` (unchanged — Phase 12 owns closure) |
| Active terms | 43 · Active sub-groups | 7 · Active VCGs | 25 (+1 empty) |
| `cluster_finding` rows (M02) | **389** |
| Inherited findings reconciled | 88 (Phase 10) — 2 of which folded into cluster_finding (Phase 11 Op B) |
| Phase 11 schema | 3.22.0 (M48: vcg_scope, applied at M01 Phase 11) |
| Phase 11 instruction | v2_2 |

---

## Tables modified

| Table | Operation | Rows |
|---|---|---:|
| `cluster_finding` | INSERT | 389 (Op A) |
| `cluster_finding` | UPDATE (fold-in text append) | 2 (Op B) |
| `wa_session_b_findings` | UPDATE `resolution_note` | 1 (sbf.74) |
| `wa_session_research_flags` | UPDATE `resolved_note` | 1 (srf.622) |

## Provenance

- Phase 9 consolidated findings (parts 1-4): at cluster root
- Phase 10 v1 reconciliation: [WA-M02-inherited-findings-reconciliation-v1-20260516.md](WA-M02-inherited-findings-reconciliation-v1-20260516.md)
- Phase 9 validation: [WA-M02-phase9-findings-validation-v1-20260516.md](WA-M02-phase9-findings-validation-v1-20260516.md)
- Apply scripts: [scripts/_apply_m02_phase11_findings_load_20260516.py](../../../scripts/_apply_m02_phase11_findings_load_20260516.py) + [scripts/_apply_m02_phase11_folds_fallback_20260516.py](../../../scripts/_apply_m02_phase11_folds_fallback_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_*_DIR-20260516-013.db`
- Trust framework: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)

---

## Next step — Phase 12 (cluster closure)

Validate cluster completeness; transition `cluster.status` to `Analysis Completed`; raise BOUNDARY_DECISION_PENDING flags for the 6 M02-BOUNDARY terms.

*End of applied report.*
