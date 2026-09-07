# wa-cluster-M01-dir-004-vcg-dissolve-v1-20260516

**Phase 8 (v2_0):** Dissolve inherited VCGs and their `vcg_term` links
**Cluster:** `M01` Fear, Dread and Terror
**Date:** 2026-05-16
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md) §11 (Phase 8 — Dissolve old VCGs)
**Researcher approval:** "this is a remarkable result, and certainly re-emphasis or prove why I am so adamant that meaning must derive from the verse context. The old method did provide plausible, but fundamentally misleading results. Proceed to desolve old vcgs" (2026-05-16)

---

## 1. Purpose

After Phase 7 (DIR-20260516-003) constructed 36 new VCGs from meaning-only design and routed every active is_relevant verse to a new VCG, the 115 pre-Phase-7 inherited VCGs remain in the database — fully superseded but not yet retired. This directive **soft-deletes** them and their `vcg_term` links to formalise the new VCG structure as the cluster's sole active inner-being phenomenology.

## 2. Inputs

- Comparison report (researcher-reviewed): [WA-M01-vcg-dissolution-comparison-v2-20260516.md](WA-M01-vcg-dissolution-comparison-v2-20260516.md)
- Pre-Phase-7 routing snapshot: [WA-M01-pre-phase7-routing-snapshot-v1-20260516.json](WA-M01-pre-phase7-routing-snapshot-v1-20260516.json)
- Phase 7 applied report: [WA-M01-dir-003-vcg-creation-applied-v1-20260516.md](WA-M01-dir-003-vcg-creation-applied-v1-20260516.md)

## 3. Scope

### In scope
- All 115 inherited VCGs in cluster M01 (verse_context_group.id < 3726; linked via vcg_term to mti_terms.cluster_code='M01'; delete_flagged=0).
- All 115 active vcg_term rows linking those VCGs to terms.

### Out of scope
- The 36 new VCGs (id ≥ 3726) created by DIR-20260516-003.
- Inherited VCGs in other clusters (this directive is M01-only).
- The 6 soft-deleted duplicate `verse_context` rows from Op pre-A — these still carry their pre-Phase-7 `group_id` pointing into the inherited set, but they are already soft-deleted so no orphan condition arises.

## 4. Pre-conditions (verified)

| Check | Expected | Actual | Status |
|---|---|---|---|
| Active is_relevant vc rows still pointing to inherited M01 VCGs | 0 | 0 | ✓ |
| Comparison report researcher-approved | yes | yes | ✓ |
| Phase 7 directive applied | yes | DIR-20260516-003 | ✓ |
| `cluster.status` for M01 | `Analysis - In Progress` | `Analysis - In Progress` | ✓ |

## 5. Operations

### Op A — Soft-delete `vcg_term` rows (115 rows)

For each active `vcg_term` row whose `vcg_id` is in the inherited-VCG set:

```sql
UPDATE vcg_term
SET delete_flagged = 1
WHERE vcg_id IN (<inherited_ids>)
  AND COALESCE(delete_flagged, 0) = 0;
```

### Op B — Soft-delete `verse_context_group` rows (115 rows)

For each inherited VCG:

```sql
UPDATE verse_context_group
SET delete_flagged = 1,
    notes = COALESCE(notes,'') || ' | DIR-20260516-004 dissolved (superseded by DIR-20260516-003 new VCGs)'
WHERE id IN (<inherited_ids>);
```

## 6. Health checks (post-apply)

| Code | Check | Expected |
|---|---|---|
| D1 | Active vcg_term rows pointing to dissolved VCGs | 0 |
| D2 | Active verse_context_group rows in M01 with id < 3726 | 0 |
| D3 | Active is_relevant vc rows in M01 with group_id IS NULL | 0 (unchanged from Phase 7) |
| D4 | Active is_relevant vc rows in M01 with group_id pointing to a delete_flagged VCG | 0 |
| D5 | Active VCGs reachable from M01 via vcg_term | 36 |

## 7. Status transition (within this directive, per v2_0 §2.6)

No standalone status transition — `cluster.status` stays `Analysis - In Progress`. The cluster is mid-flow until Phase 12 closure.

## 8. Provenance & roll-back

- **Pre-apply backup:** `backups/bible_research_backup_*_DIR-20260516-004.db`
- **Audit:** every dissolved VCG carries the directive id in its `notes` field.
- **Roll-back:** restore from pre-apply backup; OR run an inverse patch resetting `delete_flagged=0` on the dissolved rows (idempotent — `vcg_term` will need its `delete_flagged` reset too).

---

*End of directive.*
