# Directive — M10c Phase 6 sub-group structural apply + verse routing

**Directive ID:** `wa-cluster-M10c-dir-001-phase6-subgroup-assign-v1-20260526`
**Cluster:** M10c — Defilement and Impurity
**Phase:** 6 (sub-group structural apply)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §9
**Issued:** 2026-05-26
**Applied:** 2026-05-26T07:04:10Z

## §1 Required-inputs declaration

| # | Type | Path | Version |
|---|---|---|---|
| 1 | Instruction | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | v2_8 |
| 2 | Instruction | `Workflow/Instructions/wa-claudecode-instruction-v4_5-20260513.md` | v4_5 |
| 3 | Instruction | `Workflow/Instructions/wa-patch-instruction-v3_2-20260415.md` | v3_2 |
| 4 | Global rules | `Workflow/Global_rules/wa-global-rules-all-v2_8.md` | v2_8 |
| 5 | AI Phase 5 output | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-design-v1_0-20260526.md` | v1_0 |
| 6 | AI Phase 5 mapping | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-mapping-v1_0-20260526.json` | v1_0 |
| 7 | Phase 3 verdicts | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase3-constitution-verdicts-v1_0-20260526.md` | v1_0 |
| 8 | Pass A meanings | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-passa-meanings-v1-20260526.json` | v1 |

**No brief required** — this is a CC-only structural apply directive following AI Phase 5 outputs. No AI step.

## §2 Out-of-scope

- VCG design within sub-groups (Phase 7 — separate directive)
- Cross-register flag enrichment (Phase 5 design already records destinations; no DB writes for flags at Phase 6)
- Inherited VCG dissolution (Phase 8)
- Findings, observations, characteristic mapping (Phases 8.7 and 9)

## §3 Pre-decisions (validated before this directive)

1. **5-sub-group structure approved** (M10c-A through M10c-E) per Phase 5 design. All §8.6 distribution gates PASS (max 93V ≤ 105V threshold).
2. **3 gap-fix verses resolved from Pass A meaning content** (verses missing from AI's per-term verse_ranges):
   - vc=21468 Num 5:3 (ta.me verb, mti=5581) → **M10c-D** (camp defilement + divine presence)
   - vc=21583 Hag 2:13 (ta.me adj, mti=920) → **M10c-A** (bodily-contact death contagion)
   - vc=21706 Zec 13:1 (nid.dah, mti=918) → **M10c-D** (corporate-prophetic cleansing)
3. **Multi-faceted term placements**: 4 terms (ta.me verb, ta.me adj, akathartos, nid.dah) routed per-verse across multiple sub-groups; 4 terms (akatharsia, miasmos, molunō, molusmos) term-level to single sub-group (all M10c-C).

## §4 Operations (single transaction)

| Op | Target | Rows | Effect |
|---|---|---:|---|
| A | `cluster_subgroup` | 5 INSERT | M10c-A…E rows with full core_description, status='active', version='v1' |
| B | `mti_term_subgroup` | 16 INSERT | Primary + secondary placements per term (placement_note records '[primary|secondary] N verses') |
| C | `verse_context.cluster_subgroup_id` | 263 UPDATE | All is_relevant rows routed to a sub-group |
| D | `cluster.status` | 1 UPDATE | 'Data - In Progress' → 'Analysis - In Progress' |

Source: `scripts/_apply_m10c_phase6_subgroup_assign_20260526.py`
Resolved mapping (audit): `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-mapping-resolved-v1-20260526.json`

## §5 Post-checks (all PASS, see obslog)

- 0 unrouted is_relevant rows for cluster M10c
- cluster.status = 'Analysis - In Progress'
- 5 cluster_subgroup rows visible; 16 mti_term_subgroup rows; 263 verse_context.cluster_subgroup_id set

## §6 Result

**APPLIED.** Backup: `backups/bible_research_backup_20260526_070410_M10c-phase6-subgroup-assign.db`. Phase 7 input report generated: `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-meanings-v1-20260526.md`.
