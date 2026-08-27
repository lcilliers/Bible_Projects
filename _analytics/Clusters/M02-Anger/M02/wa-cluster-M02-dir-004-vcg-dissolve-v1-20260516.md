# wa-cluster-M02-dir-004-vcg-dissolve-v1-20260516

**Phase 8 (v2_2):** Inherited VCG dissolution
**Cluster:** `M02` Anger, Wrath and Indignation
**Date:** 2026-05-16
**Directive id:** `DIR-20260516-011`
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §11

---

## 1. MOTIVATION

After Phase 7 (DIR-20260516-010) constructed 26 new VCGs and routed every active is_relevant M02 verse to one of them, the 68 inherited (pre-cluster-pivot) VCGs remain in the DB but are fully superseded. This directive soft-deletes them.

**Trust basis:** the M01 blind verification methodology (recorded at [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)) validated AI's Phase 7 internal coherence across three increasingly hard tests (272 findings, 0 empty pick lists, 90.6% target precision under maximum distractor pressure). Per researcher direction, this validation transfers to M02 (same methodology, same AI, smaller and more homogeneous cluster than M01) without re-running a dissolution comparison report.

## 2. SCOPE

- 68 inherited M02 VCGs (id < 3762, vcg_term-linked to M02 terms, active)
- 68 active vcg_term rows linking those VCGs to terms

## 3. Pre-conditions (verified)

| Check | Expected | Actual |
|---|---|---|
| `cluster.status M02` | `Analysis - In Progress` | `Analysis - In Progress` ✓ |
| Active is_relevant vc rows still pointing to inherited M02 VCGs | 0 | 0 ✓ |
| Inherited M02 VCGs to dissolve | 68 | 68 ✓ |
| Active vcg_term linking inherited VCGs | 68 | 68 ✓ |

## 4. Operations

| Op | Description | Rows |
|---|---|---:|
| A | UPDATE `vcg_term.delete_flagged=1` | 68 |
| B | UPDATE `verse_context_group.delete_flagged=1` + append audit note | 68 |

Audit text appended: `| DIR-20260516-011 dissolved (superseded by DIR-20260516-010 new VCGs)`

## 5. Health checks (post-apply, all PASS)

| Code | Check | Expected | Actual |
|---|---|---|---|
| D1 | Active vcg_term pointing to dissolved | 0 | 0 ✓ |
| D2 | Active inherited M02 VCGs (id < 3762) | 0 | 0 ✓ |
| D3 | Active is_relevant vc with group_id NULL | 0 | 0 ✓ |
| D4 | Active is_relevant vc pointing to delete_flagged VCG | 0 | 0 ✓ |
| D5 | Active M02 VCGs reachable via vcg_term | 26 | 25 ⚠ |

**D5 note:** M02-D-VCG-04 (id=3781) was designed with 2 member verses but both ended up dual-routed to other VCGs (M02-D-VCG-02 / M02-B-VCG-02) at Phase 7 apply due to dual-membership precedence. The VCG row remains active in `verse_context_group` (id=3781, not delete_flagged) but has 0 vcg_term links and 0 member verses — it's a dangling empty VCG. D5 counts active VCGs **reachable via vcg_term**, which excludes the empty M02-D-VCG-04. Total active M02 VCG rows: 26 (25 reachable + 1 dangling-empty). Researcher may decide at Phase 12 closure whether to soft-delete the empty VCG row.

## 6. Provenance & roll-back

- **Pre-apply backup:** `backups/bible_research_backup_20260516_143147_DIR-20260516-011.db`
- **Apply script:** [scripts/_apply_m02_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m02_phase8_vcg_dissolve_20260516.py)
- **Roll-back:** restore from backup OR inverse patch resetting `delete_flagged=0` on the 68 + 68 rows.

---

*End of directive.*
