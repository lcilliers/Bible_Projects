# Cluster remediation playbook (systematised, reusable)

**Living document** · **Doc version:** 1 · **2026-06-01** · pairs with the audit spec `wa-cluster-audit-aspect-spec-v1-20260601.md` and the auditor `scripts/audit_cluster_v1_20260601.py`.
**Purpose:** make remedial runs a **repeatable process, not ad-hoc intervention.** Every audit-failure type maps to **one defined, reusable handler**. A cluster's "remedial run" = audit → invoke the mapped handlers for its failing aspects → re-audit to verify. Handlers tie back to v3_0 phases, so we re-run the methodology rather than invent per-cluster fixes.

## The loop (identical for every cluster)

```
audit_cluster_v1 --cluster CODE        # 1. produce the failure list (read-only)
   → for each failing aspect: invoke its handler (table below)   # 2. remediate
audit_cluster_v1 --cluster CODE        # 3. re-audit; aspect must flip PASS or be explained
```

Handler **types**: **MECH** = reusable CC script (deterministic). **AI** = reusable AI input-package builder + JSON→patch applier (analytical). **DISP** = researcher/AI disposition recorded in a reusable form (file marked up, applied by patch). No bespoke per-cluster SQL.

## Aspect → handler map

| Audit aspect (fail) | Remediation | Handler type | Tool (exists / to-build) | v3 phase |
|---|---|---|---|---|
| **A6** gating flags · **A7** stray SB | convert each to a `cluster_observation` (impact described) **or** resolve/set-aside with reason | AI/DISP | **A1 pointer-conversion** package builder + patch (programme-wide; clears these in bulk) — *to-build* | pre-cluster (A1) |
| **A4** BOUNDARY members · **A5** BOUNDARY-pending | per item: set-aside / route-to-cluster / promote-to-sub-group | DISP | §G boundary-disposition package (v2_9 §11A / v3_0 Phase B) — *pattern exists* | Phase B |
| **A8** unconfirmed actionable obs | confirm or delete each | DISP | small disposition (researcher) | Phase F |
| **B1a** verse meanings | re-run Phase A meaning-writing for verses missing `analysis_note` | AI | Phase-A meaning package builder + patch — *to-build (v3_0 Phase A defines it)* | Phase A |
| **B1b** keywords | re-run Phase A keyword emission for verses missing `keywords` | AI | same Phase-A package (Pass A emits meaning+keywords together) | Phase A |
| **B2** verses grouped | assign `cluster_subgroup_id`+`group_id` to ungrouped is_relevant verses | AI | Phase-B grouping (v3_0 §C) | Phase B |
| **B3** characteristic links | link each unlinked non-BOUNDARY sub-group to a characteristic | DISP→MECH | researcher picks characteristic → CC inserts `characteristic_subgroup` (reusable inserter) | Phase C |
| **B5** VCG anchor | designate ≥1 anchor verse per anchorless VCG | AI/DISP | anchor-designation (v3_0 Phase B) | Phase B |
| **B6 / B7** citations / anchor coverage | run the **citation extractor** (re-derives `finding_citation` from finding text); residual genuinely-uncited anchors → finding needs the cite (AI) | MECH (+AI residual) | citation extractor (v3_0 §10.3) — *confirm/locate* | Phase D |
| **D1** new terms to place | place into sub-group + run Phase A–D for the new terms | AI | the differential-pass package (placement + analysis) | Phase A–D |
| **D2** pointers to adopt | adopt each into an existing/new finding + cross-ref + close | AI | pointer-adoption package (designed this session) | Phase D |

## Why this is reusable

- **One auditor, one playbook, one loop** for all 17 (and future) clusters.
- Each handler is built **once** and run per cluster — e.g. the citation extractor fixes B6/B7 for *every* cluster; the Phase-A package fixes B1a/B1b everywhere; the A1 conversion clears A6/A7 programme-wide.
- The auditor is the **acceptance test**: a handler "worked" only when the re-audit flips the aspect.
- Nothing is hand-SQL'd per cluster; dispositions are captured in marked-up files + applied by patch, so they're auditable and repeatable.

## Build order (handlers, before per-cluster runs)

1. **Citation extractor** (B6/B7) — likely the biggest single win (B7 fails on all 17; if it's mostly a citation-extraction gap, one reusable run fixes most of it). **Confirm whether the extractor exists** (v3_0 §10.3 references it) before building.
2. **A1 pointer-conversion** (A6/A7) — clears the two most common gate failures (14/17 each) programme-wide.
3. **Phase-A meaning+keyword package** (B1a/B1b) — fixes 9–13 clusters.
4. **Boundary disposition** (A4/A5) — only M01/M02/M03/M06/M15.
5. **B3 linker, B5 anchor, D1/D2 packages** — per-cluster, smaller.

## First easy run (proves the loop)

**M10c** (3 items) then **M10b** (5) — chosen because they need only B7 (+ a couple of A6/A7 leftovers), so they exercise the **citation-extractor handler** and the **A1-conversion handler** on a tiny, safe scope first, validating both handlers before applying them to the heavy clusters.
