# wa-cluster-M02-dir-003-vcg-create-v1-20260516

**Phase 7 (v2_2):** VCG creation, verse-to-VCG routing, anchor designation
**Cluster:** `M02` Anger, Wrath and Indignation
**Date:** 2026-05-16
**Directive id:** `DIR-20260516-010`
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §10

---

## 1. MOTIVATION

Per AI's Phase 7 VCG design + CC's missing-verse API assignment, this directive creates 26 new VCGs within M02's 7 sub-groups, routes every is_relevant verse to its primary VCG, sets anchors, and records dual-membership notes.

## 2. SCOPE

| Operation | Rows |
|---|---:|
| A — INSERT `verse_context_group` | 26 |
| B — INSERT `vcg_term` | 71 |
| C — UPDATE `verse_context.group_id` (with dual-membership notes) | 641 |
| D — UPDATE `verse_context.is_anchor` (reset 71 + set 26) | 26 sets |
| D.1 — Provisional per-term anchors (R4 fallback) | 27 |
| **Total** | **791** |

## 3. Inputs

- AI's main design: [WA-M02-vcg-creation-v1-20260516.json](WA-M02-vcg-creation-v1-20260516.json)
- 6 per-sub-group design docs: `WA-M02-M02-{A..F}-vcg-design-v1-20260516.md` (+ F-and-BOUNDARY combined)
- CC's missing-verse API assignment: [WA-M02-vcg-missing-verse-assignments-v1-20260516.json](WA-M02-vcg-missing-verse-assignments-v1-20260516.json)
- Cross-routing flags: [WA-M02-phase7-cross-routing-flags-v1-20260516.md](WA-M02-phase7-cross-routing-flags-v1-20260516.md)

## 4. Phantom vc_id filtering

5 vc_ids in AI's JSON were dropped before apply:

| vc_id | Reason |
|---|---|
| 64718 (mti=136 che.mah) | is_relevant=0 — set-aside, shouldn't be routed |
| 64660 (mti=136 che.mah) | is_relevant=0 — set-aside |
| 285 (mti=79) | is_relevant=0 — set-aside |
| 356 | Does not exist in verse_context |
| 399 | Does not exist in verse_context |

## 5. Missing-verse remediation

AI's main JSON covered 602 of M02's 641 is_relevant verses (after phantom filter). 39 verses (37 in M02-B, 2 in M02-A) were re-classified by Claude API atomic per-row pass. Distribution:

| Target VCG | Verses |
|---|---:|
| M02-A-VCG-03 | 2 |
| M02-B-VCG-01 | 6 |
| M02-B-VCG-02 | 4 |
| M02-B-VCG-03 | 5 |
| M02-B-VCG-04 | 3 |
| M02-B-VCG-05 | 6 |
| M02-B-VCG-06 | 11 |
| M02-B-VCG-07 | 2 |

All 39 fit into existing VCGs; 0 NEW-NEEDED proposals.

## 6. Pre-conditions

- `cluster.status M02 = 'Analysis - In Progress'` ✓
- Sub-groups exist (7 active) ✓
- No pre-existing M02 VCGs in the new range ✓ (the 73 inherited VCGs are kept until Phase 8)

## 7. Health checks (post-apply)

| Code | Check | Expected | Actual |
|---|---|---|---|
| H2 | is_relevant verses without `group_id` | 0 | 0 ✓ |
| H3 | vc rows whose mti is not in any of their VCG's `vcg_term` | 0 | 0 ✓ |
| R4 | Terms with is_relevant verses but no anchor | 0 | 0 ✓ |

## 8. Provenance & roll-back

- **Pre-apply backup:** `backups/bible_research_backup_*_DIR-20260516-010.db`
- **Roll-back:** restore from backup OR inverse patch resetting `group_id`, `is_anchor`, and soft-deleting the 26 new VCG rows + 71 vcg_term rows.

---

*End of directive.*
