# M10b Phase 8 — VCG dissolution comparison report

**Date:** 2026-05-25
**Cluster:** M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
**Phase:** 8 (Dissolve inherited VCGs)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_8-20260519 §11

## Context

M10b is a fresh post-split cluster (created 2026-05-22 from the M10 split). Its 17 terms previously lived in M10's pre-cluster-pivot Session B structure, carrying legacy per-term VCG codes (pattern: `{mti_id}-NNN`). Phase 7 routed all 515 active is_relevant verses to the new `M10b-{X}-VCG-{NN}` structure (36 VCGs).

The inherited VCGs identified below are linked to M10b's terms via `vcg_term` but were NOT created by the Phase 7 directive. All have 0 active is_relevant verse_context rows still referencing them — Phase 7's re-routing was complete.

## Summary

- Inherited VCGs identified: **30**
- Uniform disposition: **OBSOLETE** — every inherited VCG's old framing has no analogue in the new M10b-{X}-VCG-{NN} structure (post-split fresh design)
- Active vc rows still referencing inherited VCGs: **0** (across all 30)
- Researcher gate (§11.4): **informational** for post-M01 cohort clusters; dissolution proceeds without per-VCG approval

## Inherited VCG list (table format)

| VCG id | group_code | M10b term-links | Total term-links | Active vc | Disposition |
|---:|---|---:|---:|---:|---|
| 4 | `12-001` | 1 | 1 | 0 | OBSOLETE |
| 2403 | `1223-001` | 1 | 1 | 0 | OBSOLETE |
| 2404 | `1223-002` | 1 | 1 | 0 | OBSOLETE |
| 2405 | `1223-003` | 1 | 1 | 0 | OBSOLETE |
| 2406 | `1223-004` | 1 | 1 | 0 | OBSOLETE |
| 2407 | `1223-005` | 1 | 1 | 0 | OBSOLETE |
| 5 | `13-001` | 1 | 1 | 0 | OBSOLETE |
| 2238 | `238-001` | 1 | 1 | 0 | OBSOLETE |
| 122 | `245-001` | 1 | 1 | 0 | OBSOLETE |
| 123 | `245-002` | 1 | 1 | 0 | OBSOLETE |
| 129 | `250-001` | 1 | 1 | 0 | OBSOLETE |
| 130 | `250-002` | 1 | 1 | 0 | OBSOLETE |
| 131 | `250-003` | 1 | 1 | 0 | OBSOLETE |
| 132 | `250-004` | 1 | 1 | 0 | OBSOLETE |
| 133 | `250-005` | 1 | 1 | 0 | OBSOLETE |
| 2400 | `6650-001` | 1 | 1 | 0 | OBSOLETE |
| 2221 | `74-001` | 1 | 1 | 0 | OBSOLETE |
| 878 | `832-001` | 1 | 1 | 0 | OBSOLETE |
| 879 | `832-002` | 1 | 1 | 0 | OBSOLETE |
| 880 | `832-003` | 1 | 1 | 0 | OBSOLETE |
| 881 | `832-004` | 1 | 1 | 0 | OBSOLETE |
| 883 | `836-001` | 1 | 1 | 0 | OBSOLETE |
| 877 | `837-001` | 1 | 1 | 0 | OBSOLETE |
| 873 | `839-001` | 1 | 1 | 0 | OBSOLETE |
| 868 | `840-001` | 1 | 1 | 0 | OBSOLETE |
| 869 | `840-002` | 1 | 1 | 0 | OBSOLETE |
| 870 | `841-001` | 1 | 1 | 0 | OBSOLETE |
| 947 | `846-001` | 1 | 1 | 0 | OBSOLETE |
| 948 | `846-002` | 1 | 1 | 0 | OBSOLETE |
| 865 | `853-001` | 1 | 1 | 0 | OBSOLETE |

## Dispositions

- **OBSOLETE:** all 30 inherited VCGs. The pre-cluster-pivot per-term VCG framing (`{mti_id}-NNN`) has been entirely replaced by the post-split characteristic-aligned `M10b-{X}-VCG-{NN}` structure. No old → new mapping is preserved because the framing has shifted: the pre-pivot VCGs were per-term descriptive bins (one verse-cluster per Strong's number), whereas the new VCGs are characteristic-aligned across terms.

- **KEEP-EQUIVALENT / SPLIT / MERGED:** 0 — M10b has no inherited characteristic-aligned VCG analogues to preserve.

- **UNROUTED:** 0 — all M10b's is_relevant rows are routed to new VCGs.

## Action

Phase 8 directive applies Ops A + B: soft-delete the 30 inherited VCGs and their 30 `vcg_term` links (single transaction). The descriptions remain queryable post-soft-delete for future inspection (§11.4.1).
