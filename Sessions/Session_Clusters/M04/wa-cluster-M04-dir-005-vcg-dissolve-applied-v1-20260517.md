# WA-M04-dir-005-vcg-dissolve-applied-v1-20260517

**Phase 8** — Inherited VCG dissolution
**Apply timestamp:** 2026-05-17T16:57:35Z
**Loader:** [scripts/_apply_m04_phase8_vcg_dissolve_20260517.py](../../../scripts/_apply_m04_phase8_vcg_dissolve_20260517.py)
**Directive id:** `DIR-20260517-009`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_4-20260517 §11
**Supersedes:** 86 inherited M04 VCGs (Session-A/B legacy, id range 490–3580) replaced by 30 new VCGs from DIR-20260517-008

---

## Outcome

**86 inherited VCGs soft-deleted · 86 vcg_term links soft-deleted.**

All 5 dissolution health checks PASS. `cluster.status` unchanged at `Analysis - In Progress`.

## Operations

| Op | Table | Rows | Detail |
|---|---|---:|---|
| A | `vcg_term` | 86 UPDATE | `delete_flagged=1` |
| B | `verse_context_group` | 86 UPDATE | `delete_flagged=1` + audit note appended |

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| D1 active `vcg_term` rows referencing dissolved VCGs | 0 | 0 ✓ |
| D2 active inherited M04 VCGs (id < 3813) | 0 | 0 ✓ |
| D3 active is_relevant vc rows with `group_id IS NULL` | 0 | 0 ✓ |
| D4 active is_relevant vc rows pointing to delete_flagged VCG | 0 | 0 ✓ |
| D5 active M04 VCGs reachable via `vcg_term` | 30 | 30 ✓ |

## State summary (post-Phase 8)

- **Active VCGs for M04**: 30 (new only; inherited soft-deleted)
- **Active is_relevant M04 vc rows**: 1135 (all routed to new VCGs)
- **Active vcg_term rows for M04 terms**: 110 (new only)
- **Inherited VCGs still in DB (soft-deleted)**: 86
- **`cluster.status M04`**: `Analysis - In Progress`

## Provenance

- Phase 7 v2 applied: [WA-M04-dir-004-vcg-creation-applied-v2-20260517.md](WA-M04-dir-004-vcg-creation-applied-v2-20260517.md)
- Apply script: [scripts/_apply_m04_phase8_vcg_dissolve_20260517.py](../../../scripts/_apply_m04_phase8_vcg_dissolve_20260517.py)
- Pre-apply backup: `backups/bible_research_backup_20260517_*_DIR-20260517-009.db`

---

## Next step — Phase 9 (AI: catalogue findings per VCG)

CC will:

1. Generate per-VCG grouped report (`wa-cluster-M04-vcg-grouped-v1-20260517.md`) — AI's Phase 9 input.
2. Draft Phase 9 brief for AI catalogue-prompt findings authoring.

*End of applied report.*
