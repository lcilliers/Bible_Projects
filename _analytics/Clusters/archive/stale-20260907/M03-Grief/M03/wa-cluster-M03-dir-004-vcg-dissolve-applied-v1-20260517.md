# WA-M03-dir-004-vcg-dissolve-applied-v1-20260517

**Phase 8 (v2_2):** Inherited VCG dissolution
**Apply timestamp:** 2026-05-17T04:10:46Z
**Loader:** [scripts/_apply_m03_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m03_phase8_vcg_dissolve_20260516.py)
**Directive id:** `DIR-20260516-018`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §11
**Supersedes:** 101 inherited M03 VCGs (Session-A/B legacy) replaced by 25 new M03 VCGs from DIR-20260516-017

---

## Outcome

**101 inherited VCGs soft-deleted · 101 vcg_term links soft-deleted.**

All 5 dissolution health checks PASS. `cluster.status` unchanged at `Analysis - In Progress`.

## Operations applied (single transaction)

| Op | Table | Rows | Detail |
|---|---|---:|---|
| A | `vcg_term` | 101 UPDATE | `delete_flagged=1` for all rows where `vcg_id` is in the inherited set |
| B | `verse_context_group` | 101 UPDATE | `delete_flagged=1` + audit note appended to `notes` |

## Pre-conditions verified

- `cluster.status M03` = `Analysis - In Progress` ✓
- 101 inherited M03 VCGs (id < 3788) active before apply ✓
- **0** active is_relevant vc rows still pointing to inherited VCGs ✓ (Phase 7 routing repointed all 690 active verses at the new VCGs)

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| D1 active `vcg_term` rows referencing dissolved VCGs | 0 | 0 ✓ |
| D2 active inherited M03 VCGs (id < 3788) | 0 | 0 ✓ |
| D3 active is_relevant vc rows with `group_id IS NULL` | 0 | 0 ✓ |
| D4 active is_relevant vc rows pointing to a `delete_flagged=1` VCG | 0 | 0 ✓ |
| D5 active M03 VCGs reachable via `vcg_term` | 25 | 25 ✓ |

## Trust basis (no Phase 8 comparison report)

Per researcher direction (see [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)), the M01 blind verification (3 tests, 272 findings, 0 empty pick lists, 90.6%+ target precision) validated AI's Phase-7 internal coherence under the v2_2 methodology. M02 and now M03 use identical methodology, so the dissolution comparison report is skipped. Structural integrity (H2 group coverage, H3 vcg_term coverage, R4 anchor coverage) was verified at Phase 7 apply (DIR-20260516-017).

## State summary (post-Phase-8)

- **Active VCGs for M03:** 25 (new only; inherited soft-deleted)
- **Active is_relevant M03 vc rows:** 690 (all routed to new VCGs)
- **Active vcg_term rows for M03 terms:** 108 (new only)
- **Inherited VCGs still in DB (soft-deleted, historical record):** 101
- **`cluster.status M03`:** `Analysis - In Progress`

## Provenance

- Phase 7 applied: [WA-M03-dir-003-vcg-creation-applied-v1-20260516.md](WA-M03-dir-003-vcg-creation-applied-v1-20260516.md)
- Apply script: [scripts/_apply_m03_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m03_phase8_vcg_dissolve_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260517_*_DIR-20260516-018.db`
- Validation methodology: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)

---

## Next step — Phase 9 (AI: catalogue findings per VCG)

CC will:

1. Generate Phase 9 input report — per-VCG catalogue prompts (one section per new VCG) listing terms, members, anchor, observation-catalogue questions to address. This is the prompt set AI works against to produce per-VCG findings.
2. Draft Phase 9 brief — discipline reminders, expected output structure, staged write-out instruction (per-VCG findings → disk immediately).
3. Hand off to AI for the per-VCG question-answering pass.

*End of applied report.*
