# wa-cluster-M02-dir-002-subgroup-routing-v1-20260516

**Phase 6 (v2_2):** Sub-group creation + term placement + verse routing
**Cluster:** `M02` Anger, Wrath and Indignation
**Date:** 2026-05-16
**Directive id:** `DIR-20260516-009`
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §9

---

## 1. MOTIVATION

Per AI's Phase 5 sub-group design ([WA-M02-subgroup-design-v1-20260516.md](WA-M02-subgroup-design-v1-20260516.md)) and mapping JSON ([WA-M02-subgroup-mapping-v1-20260516.json](WA-M02-subgroup-mapping-v1-20260516.json)), AI clustered the 43-term M02 corpus into 7 sub-groups (6 substantive + BOUNDARY). This directive applies the structure mechanically.

## 2. SCOPE

### Operation A — INSERT 7 `cluster_subgroup` rows

| subgroup_code | label | sort_order |
|---|---|---:|
| M02-A | Divine Wrath as Judicial Force | 1 |
| M02-B | Burning Rage and Inner Heat | 2 |
| M02-C | Indignation and Moral Displeasure | 3 |
| M02-D | Provocation — Anger Aroused | 4 |
| M02-E | Jealousy, Zeal and Possessive Passion | 5 |
| M02-F | Strife, Quarrel and Contentious Anger | 6 |
| M02-BOUNDARY | Boundary — Pending Researcher Disposition | 7 |

### Operation B — INSERT 52 `mti_term_subgroup` rows

43 primary placements + 9 secondary placements = 52 total.

### Operation C — UPDATE `verse_context.cluster_subgroup_id` for 641 rows

Per-verse routing follows the term's primary sub-group (multi-faceted terms' secondary routings are at the `mti_term_subgroup` level only, not the verse level).

| Sub-group | Verse count (is_relevant=1) |
|---|---:|
| M02-A | 109 |
| M02-B | 263 |
| M02-BOUNDARY | 82 |
| M02-C | 36 |
| M02-D | 58 |
| M02-E | 77 |
| M02-F | 16 |
| **Total** | **641** |

### Operation D — Status transition

**Not applicable.** `cluster.status` is already `Analysis - In Progress` (set at Phase 4). Per v2_2 §9.5, Op D is omitted when Phase 4 already fired the transition.

## 3. Pre-conditions (verified)

| Check | Expected | Actual | Status |
|---|---|---|---|
| `cluster.status M02` | `Analysis - In Progress` | `Analysis - In Progress` | ✓ |
| 43 active M02 terms ↔ 43 mapping entries | 1:1 | 1:1 | ✓ |
| No pre-existing active M02 sub-groups | 0 | 0 | ✓ |

## 4. Health checks (post-apply)

| Code | Check | Expected |
|---|---|---|
| H1 | Active M02 sub-groups | 7 |
| H2 | is_relevant verses without `cluster_subgroup_id` | 0 |
| H3 | Active `mti_term_subgroup` placements for M02 | 52 |
| H4 | `cluster.status M02` | `Analysis - In Progress` (unchanged) |

## 5. Operations summary

| Op | Description | Rows |
|---|---|---:|
| A | INSERT `cluster_subgroup` | 7 |
| B | INSERT `mti_term_subgroup` | 52 |
| C | UPDATE `verse_context.cluster_subgroup_id` | 641 |
| _Total DB writes_ | | **700** |

## 6. Provenance & roll-back

- **Pre-apply backup:** `backups/bible_research_backup_*_DIR-20260516-009.db`
- **Roll-back:** restore from backup; OR inverse patch resetting `verse_context.cluster_subgroup_id` to NULL + soft-delete the 52 `mti_term_subgroup` rows + soft-delete the 7 `cluster_subgroup` rows.

---

*End of directive.*
