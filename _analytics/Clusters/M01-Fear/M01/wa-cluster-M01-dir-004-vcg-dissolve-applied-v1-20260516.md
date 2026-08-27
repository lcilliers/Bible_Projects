# WA-M01-dir-004-vcg-dissolve-applied-v1-20260516

**Phase 8 (v2_0):** Inherited VCG dissolution
**Apply timestamp:** 2026-05-16T05:03:11Z
**Loader:** [scripts/_apply_m01_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m01_phase8_vcg_dissolve_20260516.py)
**Directive:** [wa-cluster-M01-dir-004-vcg-dissolve-v1-20260516.md](wa-cluster-M01-dir-004-vcg-dissolve-v1-20260516.md)
**Researcher approval:** "Proceed to desolve old vcgs" (2026-05-16)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §11

---

## Outcome

**115 inherited VCGs and 115 `vcg_term` links soft-deleted.** Single transaction. All 5 health checks pass.

| Op | Rows |
|---|---:|
| A — `vcg_term` soft-delete | 115 |
| B — `verse_context_group` soft-delete | 115 |

---

## Header summary (post-apply)

| Item | Count |
|---|---:|
| Active VCGs in M01 (reachable via vcg_term) | **36** (the new Phase 7 VCGs) |
| Soft-deleted VCGs in M01 | 115 + 0 = 115 |
| Active vcg_term rows in M01 | 193 |
| Soft-deleted vcg_term rows in M01 | 115 |
| Active is_relevant verses in M01 | 947 (unchanged from Phase 7) |
| Active vc rows routed to VCGs | 941 (unchanged) |
| Anchors total | 89 (unchanged) |

---

## Disposition summary (from comparison report)

Of the 115 dissolved inherited VCGs:

| Disposition | Count |
|---|---:|
| `KEEP-EQUIVALENT` (1:1 with no other source) | 0 |
| `KEEP-EQUIVALENT-OF-MERGE` (1:1 into a consolidated new VCG) | 59 |
| `SPLIT` (across 2+ new VCGs) | 55 |
| `OBSOLETE` (all members set-aside or soft-deleted) | 1 |
| **Total dissolved** | **115** |

**Researcher's interpretation:** "this is a remarkable result, and certainly re-emphasis or prove why I am so adamant that meaning must derive from the verse context. The old method did provide plausible, but fundamentally misleading results."

The 0 KEEP-EQUIVALENT count is the empirical signature: every new VCG draws from 2+ old VCGs (consolidation), confirming that the inherited per-term sub-cluster structure mapped poorly to the meaning-grounded phenomenology. Heaviest consolidations: `M01-B-VCG-03` (18 source old VCGs), `M01-B-VCG-01` (17), `M01-A-VCG-06` (15).

---

## Health checks (post-apply)

| Code | Check | Expected | Actual | Status |
|---|---|---|---|---|
| D1 | Active `vcg_term` rows pointing to dissolved VCGs | 0 | 0 | ✓ |
| D2 | Active `verse_context_group` rows in M01 with id < 3726 | 0 | 0 | ✓ |
| D3 | Active is_relevant vc rows in M01 with `group_id IS NULL` | 0 | 0 | ✓ |
| D4 | Active is_relevant vc rows pointing to a `delete_flagged` VCG | 0 | 0 | ✓ |
| D5 | Active VCGs reachable from M01 via vcg_term | 36 | 36 | ✓ |

All checks pass.

---

## Audit trail

Each dissolved VCG carries the directive id in its `notes` field:

```
| DIR-20260516-004 dissolved (superseded by DIR-20260516-003 new VCGs)
```

Appended to existing notes (not replaced).

---

## State summary (M01, post-Phase-8)

| Item | Value |
|---|---|
| `cluster.status` | `Analysis - In Progress` (unchanged) |
| `cluster.version` | v6 (unchanged) |
| Active terms | 81 |
| Active sub-groups | 8 |
| **Active VCGs (Phase 7 only)** | **36** |
| Soft-deleted VCGs (Phase 8 cleanup) | 115 |
| Active is_relevant verses | 947 |
| Routed verses | 941 |
| Anchors | 89 (36 AI + 53 provisional) |
| Set-asides | 81 (76 inherited + 1 Act 7:11 + 4 Phase 7) |

---

## Tables modified

| Table | Operation | Rows |
|---|---|---:|
| `vcg_term` | UPDATE delete_flagged=1 | 115 |
| `verse_context_group` | UPDATE delete_flagged=1, notes append | 115 |

## Tables not touched

| Table | Reason |
|---|---|
| `verse_context` | Verses already re-routed to new VCGs in Phase 7 |
| `cluster` | No status change (mid-flow until Phase 12 closure) |
| `cluster_subgroup`, `mti_term_subgroup` | Phase 6 work, complete |
| `cluster_finding` | Phase 9/11 work |
| Anchors in new VCGs | Set in Phase 7 (Op D + D.1) |

---

## Provenance

- Comparison report: [WA-M01-vcg-dissolution-comparison-v2-20260516.md](WA-M01-vcg-dissolution-comparison-v2-20260516.md)
- Pre-routing snapshot: [WA-M01-pre-phase7-routing-snapshot-v1-20260516.json](WA-M01-pre-phase7-routing-snapshot-v1-20260516.json)
- Phase 7 applied: [WA-M01-dir-003-vcg-creation-applied-v1-20260516.md](WA-M01-dir-003-vcg-creation-applied-v1-20260516.md)
- Apply script: [scripts/_apply_m01_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m01_phase8_vcg_dissolve_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_050311_DIR-20260516-004.db`

---

## Next step — Phase 9 (catalogue prompts)

The new 36-VCG structure is now the cluster's sole active phenomenology. Phase 9 next: prepare AI-facing brief + grouped report for the catalogue-prompt findings authoring against the 189 T0–T7 prompts.

Phase 9 input materials needed:
1. **Grouped report** — per-sub-group, per-VCG verse listing with meanings (already producible via `_generate_subgroup_meanings_report_v1_20260515.py` filtered to new-VCG view).
2. **Inherited findings/research-flags carry-over report** — outstanding Session B findings, research flags, SD pointers from constituent registries (via `_generate_cluster_inherited_findings_v1_20260515.py`).
3. **Phase 9 brief** — bounded task, decisions already made (sub-groups + VCGs final), special flags, discipline reminders.

*End of applied report.*
