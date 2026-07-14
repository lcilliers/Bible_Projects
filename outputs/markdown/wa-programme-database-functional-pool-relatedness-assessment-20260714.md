# Database Functional Pools — Relatedness and Staleness Assessment (2026-07-14)

## Scope
Assessment of table relatedness inside each functional pool from:
- Explicit foreign-key (FK) links inside the pool.
- Graph connectivity/components inside the pool.
- Staleness signals from row counts and table-name markers (`legacy`, `backup`, `quarantine`, `pre_reset`, `reverse`, `premap`, `session_d_*`).

This report complements:
- [outputs/markdown/wa-programme-database-overview-20260714.md](outputs/markdown/wa-programme-database-overview-20260714.md)
- [outputs/markdown/wa-programme-database-functional-pools-20260714.md](outputs/markdown/wa-programme-database-functional-pools-20260714.md)

## Important Interpretation Note
No internal FK does not necessarily mean no relationship. Some families are logically related via shared keys/conventions rather than enforced FK constraints. Results below are structural signals to guide cleanup, not final deletion decisions.

## Executive Findings
- Coherent pools (single connected FK component): P2, P5, P6, P11.
- Strongly split pools that likely contain multiple sub-pools: P3, P4, P7, P8, P9, P12.
- Explicit stale/legacy-heavy pools: P14 (all zero-row legacy family), and archival-like segments inside P3.
- Zero-row likely inactive tables: `finding_revision`, `prose_section_dimension_link`, `prose_section_finding_link`, `themes`, `sources`, all `session_d_*` tables.

## Stale-Candidate Tables (Structural Heuristic)

### High-confidence stale/legacy candidates
- `session_d_observations`, `session_d_runs`, `session_d_term_links`, `session_d_verse_links`
- Reason: all zero rows + legacy family naming.

### Candidate archival/legacy sidecar tables
- `ve_lexical_legacy`
- `ve_lexical_faculty_backup`
- `ve_lexical_faculty_pre_reset_20260626`
- `ve_lexical_valence_quarantine_20260626`
- `ve_lexical_origin_quarantine_20260626`
- `ve_lexical_overlay_reverse_20260626`
- `ve_lexical_divinv_pre_reverse_20260626`
- `ve_lexical_divinv_roles_premap_20260626`
- `ve_lexical_objtype_premap_20260626`
- `ve_lexical_faculty_seat_reverse_20260626`
- `ib_characteristic_legacy`

### Zero-row likely dormant (not necessarily stale)
- `finding_revision`
- `prose_section_dimension_link`
- `prose_section_finding_link`
- `themes`
- `sources`

## Per-Pool Assessment

### P1 Finding Model
- FK connectivity: 7 components for 7 tables (all isolated structurally).
- Stale signals: `finding_revision` is zero-row.
- Assessment: conceptually related pool, but FK-unenforced. Not a split by domain; split is due to missing/unenforced FK model.
- Suggested sub-pools:
  - `finding` + linkage tables (`finding_question_link`, `finding_citation`, `finding_verse_link`, `finding_revision`)
  - cluster narrative tables (`cluster_finding`, `cluster_observation`)

### P2 Cluster Model
- FK connectivity: fully connected single component.
- Stale signals: none.
- Assessment: coherent and internally related as-is.

### P3 Verse Lexical Indexes
- FK connectivity: 12 components across 14 tables.
- Connected core: `ve_lexical`, `ve_lexical_legacy`, `verse_span_index`.
- Isolated inside pool: all `*_backup`, `*_quarantine_*`, `*_reverse_*`, `*_premap_*`, plus `verse_evidence_index`, `verse_term_index`.
- Stale signals: extensive legacy/archive naming.
- Assessment: strong evidence of multiple sub-pools mixed together.
- Suggested sub-pools:
  - Live lexical/index core: `ve_lexical`, `verse_span_index`, `verse_term_index`, `verse_evidence_index`
  - Legacy baseline: `ve_lexical_legacy`
  - Transitional/repair quarantine set: all `*_backup`, `*_quarantine_*`, `*_reverse_*`, `*_premap_*`, `*_pre_reset_*`

### P4 Verse Core and Morphology
- FK connectivity: 10 components across 14 tables.
- Connected groups:
  - `verse` + `verse_morphology` + `verse_morphology_raw`
  - `verse_context` + `verse_context_group` + `vcg_term`
- Isolated: `passage`, `segment_unit`, `segment_unit_verse`, `verse_coverage`, `verse_coverage_morphology`, `verse_morph_complexity`, `verse_analysis_progress`, `verse_evidence_orphan`.
- Assessment: domain-related but structurally multi-stranded; likely sub-pooled operational tables.
- Suggested sub-pools:
  - Verse/context operational core
  - Morphology core
  - Coverage/quality metrics
  - Progress/orphan tracking
  - Passage/segment modelling

### P5 WA Term Verse Foundation
- FK connectivity: fully connected single component.
- Stale signals: none.
- Assessment: coherent and strongly related.

### P6 MTI and Term Junctions
- FK connectivity: fully connected single component.
- Stale signals: none.
- Assessment: coherent and strongly related.

### P7 Meaning and Lexicon
- FK connectivity: 5 components.
- Connected core: `wa_meaning_parsed` + `wa_meaning_sense` + `wa_meaning_stem`.
- Isolated: `lexicon`, `lemma_faculty_map`, `term_collection_lexical`, `wa_lsj_parsed`.
- Assessment: mixed pool with one parsed-meaning pipeline plus dictionary/reference side tables.
- Suggested sub-pools:
  - Parsed meaning pipeline
  - Lexicon/reference resources

### P8 Observation Catalogue and Registries
- FK connectivity: 9 components.
- Connected groups:
  - `wa_obs_question_catalogue` + `wa_finding_catalogue_links` + `wa_flag_type_question_link` + `wa_quality_flag_types`
  - `wa_vocab_set` + `wa_vocab_member`
- Isolated governance registries: `wa_rule_registry`, `wa_addendum_registry`, `wa_file_name_pattern`, `wa_label_pattern`, `wa_patch_type_registry`, `wa_crosslink_type`, `phase2_flag_types`.
- Assessment: clearly multiple governance sub-pools currently bundled.
- Suggested sub-pools:
  - Observation-question linkage
  - Vocabulary sets
  - Governance registries/reference types

### P9 Prose Store
- FK connectivity: 7 components.
- Connected relational core: `prose_section`, `prose_section_type`, `prose_section_dimension_link`, `prose_section_finding_link`, `wa_prose_section_citations`.
- Isolated but expected FTS shadow family: `prose_section_fts`, `prose_section_fts_content`, `prose_section_fts_data`, `prose_section_fts_docsize`, `prose_section_fts_idx`, `prose_section_fts_config`.
- Zero-row: `prose_section_dimension_link`, `prose_section_finding_link`.
- Assessment: legitimate two-subpool design (relational store + FTS shadow). Not inherently problematic.

### P10 Quality Flags and Research
- FK connectivity: all isolated.
- Stale signals: none.
- Assessment: likely workflow/event tables linked by logical IDs, not FK.
- Suggested sub-pools:
  - Data quality flags (`wa_data_quality_flags`, `wa_term_phase2_flags`)
  - Session research pointers (`wa_session_research_flags`, `reread_worklist`)

### P11 Engine Control and Run State
- FK connectivity: fully connected single component.
- Stale signals: none.
- Assessment: coherent and strongly related.

### P12 Registry and IB
- FK connectivity: 8 components.
- Connected pairs:
  - `word_registry` + `wa_cross_registry_links`
  - `wa_session_b_findings` + `wa_finding_entity_links`
- Isolated: `wa_dimension_index`, `wa_dim_review_cluster_log`, `wa_session_b_dimensions`, `ib_characteristic`, `ib_characteristic_legacy`, `ib_observation`.
- Stale signals: `ib_characteristic_legacy` name token.
- Assessment: clear mixed-era pool; likely multiple sub-pools.
- Suggested sub-pools:
  - Registry core
  - Session B legacy/remnant
  - IB verse-analysis family
  - Dimension-review remnants

### P13 Reference Static
- FK connectivity: `books` + `book_code_variants` connected; `themes` and `sources` isolated.
- Stale signals: `themes`, `sources` are zero-row.
- Assessment: mostly coherent reference pool with two dormant placeholders.

### P14 SessionD Legacy
- FK connectivity: all isolated.
- Stale signals: all zero-row and legacy-family names.
- Assessment: high-confidence legacy inactive sub-pool.

### P15 Metadata
- Singleton table (`schema_version`).
- Assessment: coherent as metadata singleton.

## Suspected Sub-Pool Architecture (Recommended Split Model)
- Live analytical core: P1 + P2 + selected P3 + selected P4 + P5 + P6 + P11.
- Lexical archive/transitional: legacy/quarantine/reverse/premap tables in P3.
- Prose search subsystem: P9 relational core + FTS shadow core as explicit paired sub-pools.
- Governance/reference registries: isolated registries in P8 + P13 placeholders.
- Legacy remnants: P14, `ib_characteristic_legacy`, and possibly Session-B/dimension remnants in P12.

## Practical Next Step
Run a dependency-safe usage audit before any archival move:
1. Verify runtime reads/writes in scripts and engine code for each stale-candidate table.
2. Confirm whether isolated tables are queried by joins, even without FK constraints.
3. Promote candidates to a formal `active`, `legacy-retain`, `archive-ready` triage list.
