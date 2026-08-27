# Directive — M10c Phase 7 VCG creation + verse routing

**Directive ID:** `wa-cluster-M10c-dir-002-phase7-vcg-create-v1-20260526`
**Cluster:** M10c — Defilement and Impurity
**Phase:** 7 (VCG design + structural apply)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §10
**Issued:** 2026-05-26
**Applied:** 2026-05-26T07:47:05Z

## §1 Required-inputs declaration

| # | Type | Path | Version |
|---|---|---|---|
| 1 | Instruction | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | v2_8 |
| 2 | Instruction | `Workflow/Instructions/wa-claudecode-instruction-v4_5-20260513.md` | v4_5 |
| 3 | Global rules | `Workflow/Global_rules/wa-global-rules-all-v2_8.md` | v2_8 |
| 4 | AI Phase 7 brief output (unified JSON) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-vcg-creation-v1_0-20260526.json` | v1_0 (fixed total_vcgs from 21 to actual 26 in _meta) |
| 5 | AI per-sub-group design docs | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-M10c-{A..E}-vcg-design-v1_0-20260526.md` | v1_0 (×5) |
| 6 | AI worklog | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-AI-worklog-phases3-5-7-v1-20260526.md` | v1 (renamed from non-canonical filename) |
| 7 | CC Phase 5 validation report | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase5-validation-v1-20260526.md` | v1 |
| 8 | CC Phase 6 obslog (sub-group apply) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-obslog-phase6-v1-20260526.md` | v1 |

**No brief required** — this is a CC-only structural apply directive following AI Phase 7 outputs. No AI step in this directive (the AI's design + JSON were produced under the Phase 7 brief already issued).

## §2 Out-of-scope

- Inherited VCG dissolution (Phase 8)
- BOUNDARY resolution (Phase 8.5 — no BOUNDARY verdicts on M10c)
- Characteristic mapping / cluster_observation seeding (Phase 8.7)
- Findings + synthesis (Phase 9)
- Validation gate FF-1..FF-10 (Phase 9 post-apply)
- Phase 11/12 closure

## §3 Pre-decisions (validated before this directive)

1. **AI's 26 VCGs accepted** (A=8, B=5, C=5, D=5, E=3). §10.8 pre-submission checklist: all PASS.
2. **JSON _meta correction**: `total_vcgs` was stated as 21 but actual VCG count is 26 — CC patched the _meta field. Structural data unchanged.
3. **AI's primary anchor per VCG accepted** for 26 VCGs. **R4 supplementary anchor** added: miasmos vc_id=30266 (2Pe 2:10) co-anchored alongside molusmos vc_id=9329 (2Cor 7:1) in M10c-C-VCG-03 — the AI grouped two single-verse Greek terms ("body-and-spirit purification") under one VCG with molusmos as primary anchor; R4 anchor gate per term requires miasmos to also carry an anchor.

## §4 Operations (single transaction; one supplementary anchor write outside the transaction)

| Op | Target | Rows | Effect |
|---|---|---:|---|
| A | `verse_context_group` | 26 INSERT | One row per VCG; `group_code` = AI provisional_code; `context_description` = AI description |
| B | `vcg_term` | 53 INSERT | One row per distinct (vcg_id, mti_term_id) where the VCG carries any of the term's verses; `placement_note='Phase 7 routing'` |
| C | `verse_context.group_id` | 263 UPDATE | Every is_relevant M10c verse routed to its AI-designated VCG |
| D | `verse_context.is_anchor` | 14 cleared + 26 set | Prior pseudo-anchors from earlier phases cleared; AI's 26 primary anchors set |
| D' | `verse_context.is_anchor` (supplementary) | 1 set | miasmos vc=30266 co-anchored for R4 compliance |

Source: `scripts/_apply_m10c_phase7_vcg_create_20260526.py`. Backup: `backups/bible_research_backup_20260526_074706_M10c-phase7-vcg-create.db`.

## §5 Post-checks (all PASS)

- 26 verse_context_group rows in DB with group_code LIKE 'M10c-%-VCG-%'
- 263 is_relevant verses routed to new VCGs
- 27 is_anchor=1 rows on M10c verses (26 primaries + 1 R4 supplementary)
- R4 anchor gate: every M10c term with is_relevant ≥1 has ≥1 anchor (8/8 terms PASS)

## §6 Per-sub-group VCG counts

| Sub-group | VCGs | Sub-group verses |
|---|---:|---:|
| M10c-A — Bodily-contact | 8 | 93 |
| M10c-B — Categorical/classificatory | 5 | 40 |
| M10c-C — Moral-inner | 5 | 26 |
| M10c-D — Corporate/covenantal | 5 | 83 |
| M10c-E — External spiritual agency | 3 | 21 |
| **Total** | **26** | **263** |

## §7 Result

**APPLIED.** Phase 7 complete; cluster state remains `Analysis - In Progress`. Phase 8 (inherited VCG dissolution) — M10c had no inherited VCGs entering this cluster cycle, so Phase 8 is a no-op for M10c. Next analytical work begins at Phase 8.7 (characteristic mapping) or Phase 9 (findings).
