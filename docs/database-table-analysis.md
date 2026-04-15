# Database Table Analysis

> Framework B — Soul Word Analysis Programme
> Schema v3.8.0 | 43 tables | Analysis date: 2026-04-13 | Updated 2026-04-15

This document analyses every table in `bible_research.db`: purpose, field inventory with source and status, relationships, and readiness assessment.

> **2026-04-15 schema changes** (directives DIR-20260415-001 through 006):
> - `wa_quality_flag_types`: +3 fields (deprecated, deprecation_note, category); +15 rows; 3 rows deprecated
> - `wa_session_b_findings`: +9 lifecycle fields; finding_type normalised to UPPER_SNAKE_CASE
> - `wa_session_research_flags`: 19 VOLUME_LIMITATION rows consolidated to PH2_VOLUME_LIMITATION
> - New table: `wa_finding_entity_links` (table count: 42 → 43)
> See `Logs/wa-session-log-20260415-flag-remediation.md` for full details.

**Readiness key:**
- **Complete** — field is fully populated and actively used
- **Functional** — field is populated where applicable; NULLs are expected
- **Sparse** — populated for a minority of rows; may indicate incomplete backfill or limited applicability
- **Unused** — all NULL or zero rows; either not yet activated or superseded
- **Superseded** — field exists but has been replaced by a newer mechanism
- **Legacy** — field from an earlier schema version; retained but no longer written to

---

## Table of Contents

1. [Reference Tables](#1-reference-tables) — books, book_code_variants, themes, sources
2. [Registry](#2-registry) — word_registry
3. [File Index](#3-file-index) — wa_file_index
4. [Term Data](#4-term-data) — wa_term_inventory, wa_term_related_words, wa_term_root_family
5. [Mounce Term Index (MTI)](#5-mounce-term-index) — mti_terms, mti_term_cross_refs, mti_term_flags
6. [Verse Records](#6-verse-records) — wa_verse_records, wa_verse_term_links
7. [Meaning Parse](#7-meaning-parse) — wa_meaning_parsed, wa_meaning_sense, wa_meaning_stem, wa_lsj_parsed
8. [Flags](#8-flags) — phase2_flag_types, wa_term_phase2_flags, wa_quality_flag_types, wa_data_quality_flags
9. [Verse Context](#9-verse-context) — verse_context_group, verse_context
10. [Dimension Review](#10-dimension-review) — wa_dimension_index, wa_dim_review_cluster_log
11. [Cross-Registry Links](#11-cross-registry-links) — wa_crosslink_type, wa_cross_registry_links
12. [Session B Structured](#12-session-b-structured) — wa_session_b_dimensions, wa_session_b_findings
13. [Session Research Flags](#13-session-research-flags) — wa_session_research_flags
14. [Session D](#14-session-d) — session_d_runs, session_d_verse_links, session_d_term_links, session_d_observations
15. [Engine Control](#15-engine-control) — engine_run_log, engine_stream_checkpoint, term_fetch_log, word_run_state
16. [Schema Metadata](#16-schema-metadata) — schema_version

---

## 1. Reference Tables

### books (66 rows)

**Purpose:** Static reference table for the 66 books of the Bible. Provides book identity, ordering, and testament classification.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| name | TEXT | Book name (e.g. "Genesis") | Manual seed | Complete |
| abbreviation | TEXT | Short code (e.g. "Gen") | Manual seed | Complete |
| testament | TEXT | "OT" or "NT" | Manual seed | Complete |
| book_order | INTEGER | Canonical ordering (1-66) | Manual seed | Complete |
| full_name | TEXT | Extended name | Manual seed | Functional — NULL for some |
| short_code | TEXT | Alternative short code | Manual seed | Functional — NULL for some |
| verse_count | INTEGER | Total verses in book | Manual seed | Complete |
| last_updated | TEXT | Row modification timestamp | Auto (default) | Complete |

**Relations:** Parent to `book_code_variants` (book_id), referenced by `wa_verse_records` (book_id).

**Assessment:** Stable reference data. Fully populated. No issues.

---

### book_code_variants (112 rows)

**Purpose:** Maps alternative book code strings (e.g. "1Sa", "1Sam") to the canonical `books.id`. Used by the engine to normalise book references from STEP data.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| code | TEXT PK | Variant code string | Manual seed | Complete |
| book_id | INTEGER FK | Links to books.id | Manual seed | Complete |

**Relations:** FK to `books.id`.

**Assessment:** Stable lookup table. Complete.

---

### themes (0 rows)

**Purpose:** Originally intended for thematic classification of words. Never populated.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | — | Unused |
| name | TEXT | Theme name | — | Unused |
| description | TEXT | Theme description | — | Unused |

**Relations:** None active.

**Assessment:** **Unused.** No rows. The thematic classification function has been absorbed by `cluster_assignment` on `word_registry` and `dimensions` on the same table. Candidate for removal or future repurposing.

---

### sources (0 rows)

**Purpose:** Originally intended for bibliographic source tracking via Zotero integration. Never populated.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | — | Unused |
| zotero_key | TEXT | Zotero item key | — | Unused |
| title | TEXT | Source title | — | Unused |
| author | TEXT | Author name | — | Unused |
| year | INTEGER | Publication year | — | Unused |
| source_type | TEXT | Type of source | — | Unused |

**Relations:** None active.

**Assessment:** **Unused.** Zotero integration was designed but never operationalised. Zero rows.

---

## 2. Registry

### word_registry (214 rows)

**Purpose:** Master list of all words in the programme. The anchor for everything — every term, verse, flag, and analytical output traces back to a registry entry. Defines research scope and tracks pipeline progress.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| no | INTEGER | Registry number — human-readable identifier used in all file naming | Sequential (register.py) | Complete (214 unique) |
| word | TEXT | English word label for this registry | Researcher | Complete (210 unique — 4 duplicates from split registries) |
| source_list | TEXT | How the word entered the registry (High Confidence, Low Confidence / Inferred, etc.) | Researcher at registration | Complete |
| category_hint | TEXT | Broad semantic category (navigational aid, not analytical) | Researcher | Sparse (17% — 36 of 214). Largely superseded by cluster_assignment |
| phase1_input_file | TEXT | Path to original Phase 1 input file | Engine (legacy) | Sparse (22%). Legacy field from early pipeline |
| phase1_status | TEXT | Phase 1 extraction state: Pending, Complete, Excluded, In Progress | Engine (audit_word) | Complete (3 distinct values) |
| phase1_output_file | TEXT | Path to Phase 1 output file | Engine (legacy) | Sparse (15%). Legacy field |
| phase2_datasets | REAL | Phase 2 dataset identifier | Legacy | Sparse (14%). Legacy field — not used in current pipeline |
| notes | TEXT | Free-text notes about this registry | Researcher / engine | Complete (99.5%) |
| automation_eligible | INTEGER | Whether engine automation can run on this registry | Engine | Complete (all rows) |
| last_automation_run | TEXT | Lock sentinel (IN_PROGRESS) or completion marker (AUDITED) | Engine | Complete (99.5%) |
| automation_run_id | TEXT | ID of the last engine run for this registry | Engine | Complete (99.5%) |
| phase1_term_count | INTEGER | Number of terms extracted in Phase 1 | Engine (audit_word) | Complete. **Note: Phase 1 snapshot only — not updated by Session B** |
| phase1_verse_count | INTEGER | Verses with confirmed span matches in Phase 1 | Engine (audit_word) | Complete. **Note: Phase 1 snapshot only** |
| strongs_list | TEXT | Comma-separated list of Strong's numbers for this registry | Engine (audit_word) | Complete (99.5%) |
| description | TEXT | Description of the word | Researcher / engine | Complete (98%) |
| origin | TEXT | original_list or programme_addition | Researcher | Complete (99%) |
| dimensions | TEXT | Multi-value semantic category (comma-delimited). Formerly source_category (renamed M17) | Session B extraction | Functional (88% — 26 NULL are Excluded/zero-term registries) |
| inference_note | TEXT | Researcher-only note about inference/scope decisions | Researcher | Sparse (11%). **Pipeline must never overwrite** |
| session_b_status | TEXT | Session B pipeline progress: NULL, Verse Context Reset, Ready for Analysis, Pre-Analysis Complete, Analysis Complete, Session B Complete | Engine / patch applicator | Functional (86% — 30 NULL are Excluded registries) |
| cluster_assignment | TEXT | Cluster code C01–C22 | Researcher / CLUSTERING patch | Complete (all 214 assigned) |
| sb_classification | TEXT | Inner being standing classification from Session B | Session B analytical work | Sparse (3% — only 7 registries classified so far) |
| sb_classification_reasoning | TEXT | Reasoning for non-confirmed classifications | Session B | Sparse (2%) |
| carry_forward | INTEGER | Whether word carries to Session D (1/0) | Session B | Complete (default 1) |
| unique_term_count | INTEGER | Terms unique to this registry | Engine | Complete. **Phase 1 snapshot only** |
| shared_term_count | INTEGER | Terms shared with other registries | Engine | Complete. **Phase 1 snapshot only** |
| term_sharing_ratio | REAL | 0.0 (all unique) to 1.0 (all shared) | Engine | Complete. **Phase 1 snapshot only** |
| verse_context_status | TEXT | VC completion state: NULL, In Progress, Complete | Claude Code (post-patch) | Functional (86% — 30 NULL are Excluded) |
| dim_review_status | TEXT | Dimension review stamp per registry | Claude Code (post-patch) | Sparse (16% — 35 registries stamped across 5 clusters) |
| dim_review_version | TEXT | Instruction version used for dimension review | Claude Code (post-patch) | Sparse (16% — matches dim_review_status) |

**Relations:** Parent to `wa_file_index`, `wa_session_research_flags`, `wa_cross_registry_links`, `mti_terms`, `wa_session_b_dimensions`. Referenced by many tables via FK.

**Assessment:** Core table. Well-populated for active registries. Legacy fields (phase1_input_file, phase1_output_file, phase2_datasets, category_hint) are functionally superseded but retained. The `sb_classification` and `sb_classification_reasoning` fields will fill as Session B progresses. The `dim_review_status` will fill as more clusters complete Dimension Review.

---

## 3. File Index

### wa_file_index (206 rows)

**Purpose:** One row per imported Session A JSON file. Acts as the parent for all WA term and verse data. Links imported data back to its source file and registry.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| filename | TEXT | Name of the imported JSON file | Engine (audit_word) | Complete |
| registry_id | TEXT | Registry number as string (e.g. "068") | Engine | Complete |
| word_registry_fk | INTEGER FK | Links to word_registry.id | Engine (M12 FK alignment) | Complete |
| word | TEXT | English word label | Engine | Complete |
| part_number | INTEGER | Part number for split files (1, 2, 3...) | Engine | Sparse (19%) — only populated for multi-part files |
| total_parts | INTEGER | Total number of parts | Engine | Sparse (19%) — matches part_number |
| is_split | INTEGER | Whether the file is part of a split set | Engine | Complete |
| schema_version | TEXT | JSON schema version at time of import | Engine | Sparse (28%) — older imports predate versioning |
| phase | TEXT | Pipeline phase (e.g. "Session A") | Engine | Complete (99.5%) |
| produced_date | TEXT | Date the source JSON was produced | Engine | Complete (99.5%) |
| source_file | TEXT | Original file path | Engine | Sparse (28%) — older imports |
| translation_used | TEXT | Bible translation (always "ESV") | Engine | Complete (99.5%) |
| specification | TEXT | Specification label | Engine | Complete |
| revision_note | TEXT | Notes on file revisions | Engine | Sparse (3%) — rarely needed |
| source_list | TEXT | Source list classification | Engine | Complete (98%) |
| category | TEXT | Category from source file | Engine | Sparse (6%) — legacy field |
| testament_coverage | TEXT | OT_only, NT_only, or both | Engine (audit_word) | Complete (99%) |
| root_families_in_prior_parts | TEXT | Root families from earlier parts (multi-part only) | Engine | Sparse (11%) — only for multi-part files |
| last_changed | TEXT | Row modification timestamp | Auto (default) | Complete |

**Relations:** FK to `word_registry.id`. Parent to `wa_term_inventory`, `wa_verse_records`, `wa_data_quality_flags`, `wa_session_research_flags`, `wa_cross_registry_links`.

**Assessment:** Functional. Sparse fields are mostly explained by multi-part file logic or pre-versioning imports. The `category` field is legacy — superseded by `word_registry.cluster_assignment`.

---

## 4. Term Data

### wa_term_inventory (7,550 rows)

**Purpose:** Per-term metadata for every Strong's number in the programme. Each row represents one term within one registry's file index. Contains lexical data, occurrence counts, analytical flags, and OWNER/XREF classification.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| file_id | INTEGER FK | Links to wa_file_index.id | Engine (audit_word) | Complete |
| language | TEXT | "Hebrew" or "Greek" | STEP API | Complete |
| term_id | TEXT | Term identifier (Strong's number or composite) | STEP API | Complete |
| strongs_number | TEXT | Strong's number (H/G prefix) | STEP API | Complete (99.9% — 9 NULL from legacy) |
| transliteration | TEXT | Romanised form of the term | STEP API | Complete |
| step_search_gloss | TEXT | STEP Bible search gloss | STEP API | Complete |
| word_analysis_gloss | TEXT | Programme-specific gloss | STEP API / Claude AI | Complete (99.9%) |
| occurrence_count | INTEGER | Total ESV occurrences for this Strong's number | STEP API | Complete (99.7%) |
| occurrence_count_qualifier | TEXT | Qualifier on count (e.g. "approximate") | STEP API | Sparse (9%) — only when applicable |
| meaning | TEXT | Full meaning text from STEP | STEP API (legacy path) | Sparse (1%). **Superseded by wa_meaning_parsed** |
| meaning_numbered | TEXT | Numbered meaning variant | STEP API (legacy path) | Sparse (1%). **Superseded by wa_meaning_parsed** |
| also_spelled | TEXT | Alternative spellings | STEP API | Sparse (0.2%) — rare |
| lsj_entry | TEXT | Liddell-Scott-Jones lexicon entry (Greek terms) | STEP API | Sparse (29%) — Greek terms only |
| testament | TEXT | OT or NT | Derived from language | Complete (99.9%) |
| god_as_subject | INTEGER | Whether God appears as subject with this term | STEP data / Claude AI | Complete. **Superseded by mti_term_flags** — do not write |
| somatic_link | INTEGER | Whether term has somatic/body connection | STEP data / Claude AI | Complete. **Superseded by mti_term_flags** — do not write |
| causative_form_present | INTEGER | Whether term has a causative Hebrew stem | STEP meaning parse | Complete |
| status_note | TEXT | Note on term status | Engine | Sparse (2%). **NULL across nearly all records — no pipeline purpose** |
| last_changed | TEXT | Row modification timestamp | Auto (default) | Complete |
| short_def_mounce | TEXT | Mounce short definition (Greek terms) | STEP API | Sparse (29%) — Greek terms only |
| parsed_meaning_id | INTEGER | Links to wa_meaning_parsed.id | Engine (meaning_parser) | Complete (99%) |
| delete_flagged | INTEGER | Soft delete flag (1 = deleted) | Engine | Complete |
| evidential_status | TEXT | confirmed, plausible, uncertain, instrumental, relational_only | Session B (Claude AI) | Sparse (2%) — only set for Session B completed registries |
| retention_note | TEXT | Why a term is retained despite low evidence | Session B (Claude AI) | Sparse (0.7%) — only where needed |
| term_owner_type | TEXT | OWNER or XREF | Engine (audit_word) | Functional (94% — 457 NULL from pre-OWNER/XREF era terms) |

**Relations:** FK to `wa_file_index.id`. Parent to `wa_verse_records`, `wa_term_related_words`, `wa_term_root_family`, `wa_term_phase2_flags`, `wa_meaning_parsed`, `wa_lsj_parsed`, `wa_verse_term_links`.

**Assessment:** Core data table. Well-populated for essential fields. Several **superseded fields** remain: `god_as_subject` and `somatic_link` (now on mti_term_flags), `meaning` and `meaning_numbered` (now in wa_meaning_parsed), `status_note` (no pipeline purpose). The `evidential_status` and `retention_note` fields will fill as Session B progresses. The 457 NULL `term_owner_type` rows are from early imports before OWNER/XREF classification was implemented.

---

### wa_term_related_words (101,970 rows)

**Purpose:** Lexical relatives for each term — words that STEP identifies as related by etymology, meaning overlap, or lexical grouping. Physically deleted and re-inserted on STALE_TERM updates.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| term_inv_id | INTEGER FK | Links to wa_term_inventory.id | Engine | Complete |
| gloss | TEXT | English gloss of the related word | STEP API | Complete |
| transliteration | TEXT | Romanised form | STEP API | Complete (99.99%) |
| strongs_number | TEXT | Strong's number of the related word | STEP API | Functional (98%) — 1,597 NULL where STEP lacks the number |
| relationship_note | TEXT | Description of how the words are related | STEP API | Sparse (0.3%) — rarely provided by STEP |
| delete_flagged | INTEGER | Soft delete flag | Engine | Complete (all 0 — physical deletes used instead) |

**Relations:** FK to `wa_term_inventory.id`.

**Assessment:** Large table, well-populated. The `relationship_note` sparseness reflects STEP's data — not a gap. The `delete_flagged` column is always 0 because this table uses physical deletes on refresh (unlike other tables).

---

### wa_term_root_family (2,861 rows)

**Purpose:** Maps terms to their Hebrew/Greek root families. Used for cross-term linguistic grouping and correlation signals.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| term_inv_id | INTEGER FK | Links to wa_term_inventory.id | Engine | Complete |
| root_code | TEXT | Root identifier (e.g. "CHARAH", "AGAPE") | STEP API / root backfill script | Complete (964 unique roots) |
| root_language | TEXT | Hebrew or Greek | Derived | Functional (78%) — 634 NULL from early imports before backfill |
| root_gloss | TEXT | English gloss of the root | STEP API / backfill | Functional (78%) — matches root_language gap |
| note | TEXT | Additional root information | Various | Functional (78%) |
| delete_flagged | INTEGER | Soft delete flag | Engine | Complete |

**Relations:** FK to `wa_term_inventory.id`.

**Assessment:** Functional. The 22% NULL gap in root_language/root_gloss/note is from early imports before the root family backfill was completed. These could be backfilled but are not blocking.

---

## 5. Mounce Term Index

### mti_terms (7,571 rows)

**Purpose:** Programme-wide index of Strong's numbers. One record per Strong's number regardless of how many registries reference it. The canonical identity record for each term. `mti_term_id` is the FK used by verse_context for cross-registry sharing.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key — the programme-wide term identity | Auto-generated | Complete |
| strongs_number | TEXT | Strong's number (unique programme-wide) | STEP API | Complete (3,955 unique) |
| transliteration | TEXT | Romanised form | STEP API | Complete |
| gloss | TEXT | English gloss | STEP API | Complete |
| language | TEXT | Hebrew or Greek | STEP API | Complete |
| owning_registry | TEXT | Registry number as string | Engine (audit_word) | Complete |
| owning_registry_fk | INTEGER FK | Links to word_registry.id | Engine (M12 FK alignment) | Sparse (54%) — 3,522 NULL from pre-FK-alignment imports |
| owning_word | TEXT | English word of the owning registry | Engine | Complete (99.96%) |
| owning_part | TEXT | Part label (for multi-part files) | Engine | Sparse (5%) — only for multi-part registries |
| word_data_reference | TEXT | Reference to wa_file_index | Engine | Sparse (18%) — only populated for certain imports |
| word_data_ref_fk | INTEGER FK | Links to wa_file_index.id | Engine (M12) | Sparse (18%) — matches word_data_reference |
| status | TEXT | Term lifecycle: NULL, extracted, extracted_thin, candidate_delete, delete, excluded, etc. | Engine (audit_word A6b) / Session B patches | Functional (70%) — 2,276 NULL are unclassified terms |
| status_note | TEXT | Notes on status decisions (written by A10 only) | Engine (audit_word A10) | Sparse (20%) — only where classification reasoning exists |
| exclusion_reason | TEXT | Why a term was excluded or deleted | Engine / Session B | Sparse (15%) — only for excluded/deleted terms |
| extraction_date | TEXT | When the term was first extracted | Engine | Complete (99.7%) |
| strongs_reconciled | INTEGER | Whether Strong's number has been verified | Engine | Complete |
| anchor_note | TEXT | Note about anchor verse designation | Claude AI | Sparse (0.3%) — rarely used |
| last_changed | TEXT | Row modification timestamp | Auto (default) | Complete |
| delete_flagged | INTEGER | Soft delete flag | Engine | Complete |

**Relations:** FK to `word_registry.id`, `wa_file_index.id`. Parent to `mti_term_cross_refs`, `mti_term_flags`, `verse_context_group`, `verse_context`, `wa_dimension_index`.

**Assessment:** Critical table. The 46% NULL on `owning_registry_fk` is a significant gap from pre-FK-alignment data — these records have `owning_registry` (string) but not the integer FK. The 30% NULL `status` represents terms that audit_word has not classified (no verses or signals to trigger a filter). This is expected state, not missing data. The `word_data_reference`/`word_data_ref_fk` sparseness reflects the same pre-FK-alignment gap.

---

### mti_term_cross_refs (464 rows)

**Purpose:** Records which registries reference a given Strong's number. Enables cross-registry term sharing analysis.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| mti_term_id | INTEGER FK | Links to mti_terms.id | Engine | Complete |
| registry | TEXT | Registry number as string | Engine | Complete |
| registry_fk | INTEGER FK | Links to word_registry.id | Engine (M12) | Functional |
| word | TEXT | English word of the referencing registry | Engine | Functional |
| part | TEXT | Part label | Engine | Sparse — only for multi-part |
| word_data_reference | TEXT | File reference | Engine | Sparse |

**Relations:** FK to `mti_terms.id`, `word_registry.id`.

**Assessment:** Functional. Used for XREF sharing analysis and correlation signals.

---

### mti_term_flags (54 rows)

**Purpose:** Semantic/analytical flags at the MTI term level (programme-wide, not per-registry). Supersedes the per-inventory `god_as_subject` and `somatic_link` fields.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| mti_term_id | INTEGER PK | Links to mti_terms.id (composite PK) | Session B patches | Complete |
| flag_id | INTEGER PK | Links to phase2_flag_types.id (composite PK) | Session B patches | Complete |

**Relations:** FK to `mti_terms.id`, `phase2_flag_types.id`.

**Assessment:** Sparse (54 rows) — only populated for terms that have been through Session B analytical work. Will grow as more registries complete Session B. This is the correct location for GOD_AS_SUBJECT, SOMATIC_INNER_LINK, etc.

---

## 6. Verse Records

### wa_verse_records (229,778 rows)

**Purpose:** Core research table. One row per term-in-verse occurrence — every place in the ESV where a Strong's number appears. Contains verse text, location parsing, span confirmation, and context windows.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| file_id | INTEGER FK | Links to wa_file_index.id | Engine | Complete |
| term_inv_id | INTEGER FK | Links to wa_term_inventory.id | Engine | Complete |
| term_id | TEXT | Strong's number / term identifier | Engine | Complete (99.99%) |
| transliteration | TEXT | Romanised form of the term | Engine | Complete (99.99%) |
| testament | TEXT | OT or NT | Derived | Complete |
| reference | TEXT | Verse reference (e.g. "Gen 1:1") | STEP API | Complete |
| verse_text | TEXT | Full ESV verse text | STEP API | Complete |
| last_changed | TEXT | Row modification timestamp | Auto (default) | Complete |
| book_id | INTEGER FK | Links to books.id | Engine (parsed from reference) | Complete (99.99%) |
| chapter | INTEGER | Chapter number | Engine (parsed) | Complete |
| verse_num | INTEGER | Verse number | Engine (parsed) | Complete |
| translation | TEXT | Bible translation (always "ESV") | Engine | Complete |
| note | TEXT | General note field | — | **ALL NULL.** Never used |
| claude_output | TEXT | Originally for Claude AI analysis output | — | **ALL NULL.** Never used. Superseded by verse_context |
| created_at | TEXT | Row creation timestamp | Engine | Functional (79%) — missing for early imports |
| updated_at | TEXT | Row update timestamp | Engine | Functional (98%) |
| target_word | TEXT | The English word found at this verse position | STEP API (span filter) | Functional (99%) — missing for pre-span-filter imports |
| span_strong_match | INTEGER | Whether the Strong's number was confirmed by STEP HTML span analysis | Engine (span_filter) | Functional (99%) — all confirmed are 1 (no 0 values in data) |
| context_before | TEXT | Text immediately before the target word | STEP API | Functional (84%) — missing for early imports before context was added |
| context_after | TEXT | Text immediately after the target word | STEP API | Functional (84%) — matches context_before |
| delete_flagged | INTEGER | Soft delete flag (1 for XREF verses and removed terms) | Engine | Complete |
| mti_term_id | INTEGER FK | Links to mti_terms.id — the cross-registry key | Engine | Functional (98%) — 5,249 NULL from pre-MTI-linking imports |

**Relations:** FK to `wa_file_index.id`, `wa_term_inventory.id`, `books.id`. Parent to `wa_verse_term_links`, `verse_context`.

**Assessment:** Largest table and most critical data asset. Core fields (reference, verse_text, book_id, chapter, verse_num) are fully populated. Two fields are **completely unused** (`note`, `claude_output`) — candidates for removal. The `mti_term_id` gap (2.3%) and `context_before/after` gap (16%) are from early imports. The `span_strong_match` field shows all non-NULL values as 1, meaning it effectively functions as a "has been span-checked" boolean rather than a pass/fail indicator.

---

### wa_verse_term_links (226,791 rows)

**Purpose:** Links verses to terms with STEP sub-gloss detail. Enables verse-level term co-occurrence analysis and sub-gloss tracking.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| verse_id | INTEGER FK | Links to wa_verse_records.id | Engine | Complete |
| term_inv_id | INTEGER FK | Links to wa_term_inventory.id | Engine | Complete |
| step_subgloss_code | TEXT | STEP sub-gloss code (e.g. "H7965.1") | STEP API | Complete (99.97%) |
| step_subgloss_label | TEXT | Human-readable sub-gloss label | STEP API | Complete (99.96%) |
| span_strong_match | INTEGER | Span confirmation for this specific link | Engine (span_filter) | Complete (99.9%) |
| target_word | TEXT | English word at this position | STEP API | Complete (99.9%) |
| created_at | TEXT | Row creation timestamp | Auto (default) | Complete |

**Relations:** FK to `wa_verse_records.id`, `wa_term_inventory.id`.

**Assessment:** Well-populated. Near-complete coverage on all fields. Functional and actively used.

---

## 7. Meaning Parse

### wa_meaning_parsed (7,449 rows)

**Purpose:** Structured parse of each term's meaning text. Breaks the free-text meaning field from STEP into countable senses, stems, and domain indicators.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| term_inv_id | INTEGER FK | Links to wa_term_inventory.id (1:1) | Engine (meaning_parser) | Complete |
| strongs_number | TEXT | Strong's number | Engine | Complete (only 3 distinct — appears to store language, not strongs) |
| language | TEXT | Hebrew or Greek | Engine | Complete |
| top_sense_count | INTEGER | Number of top-level senses | Engine (parsed) | Complete |
| stem_count | INTEGER | Number of Hebrew stems identified | Engine (parsed) | Complete |
| has_causative_stem | INTEGER | Whether a causative stem (Hiphil etc.) was found | Engine (parsed) | Complete |
| has_domain_tags | INTEGER | Whether domain tags were identified | Engine (parsed) | Complete (all 0 — no domain tags found) |
| parsed_at | TEXT | Parse timestamp | Engine | Complete |
| parse_version | TEXT | Parser version | Engine | Complete (all same version) |
| parse_warnings | TEXT | Warnings generated during parse | Engine | Functional (74% — NULL means no warnings) |

**Relations:** FK to `wa_term_inventory.id`. Parent to `wa_meaning_sense`, `wa_meaning_stem`.

**Assessment:** Complete for all terms that have meaning text. The `strongs_number` field appears to have a data anomaly (only 3 distinct values) — may be storing language codes rather than actual Strong's numbers. `has_domain_tags` is all 0, suggesting domain tagging is not being captured by the parser.

---

### wa_meaning_sense (15,981 rows)

**Purpose:** Individual sense entries parsed from meaning text. Hierarchical — senses can have sub-senses via parent_level_code.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| parsed_meaning_id | INTEGER FK | Links to wa_meaning_parsed.id | Engine | Complete |
| level_code | TEXT | Hierarchical sense code (e.g. "1", "1a", "1a.i") | Engine (parsed) | Complete |
| level_depth | INTEGER | Nesting depth (1, 2, 3...) | Engine (parsed) | Complete |
| parent_level_code | TEXT | Parent sense code | Engine (parsed) | Functional — NULL for top-level senses |
| sense_text | TEXT | The sense description | Engine (parsed) | Functional |
| is_stem_label | INTEGER | Whether this row is a stem heading (not a sense) | Engine (parsed) | Complete |
| stem_label | TEXT | Stem name (Qal, Piel, Hiphil, etc.) | Engine (parsed) | Functional — only for stem-labelled rows |
| domain_tag | TEXT | Domain classification | Engine (parsed) | Functional |
| sort_order | INTEGER | Display ordering | Engine | Complete |

**Relations:** FK to `wa_meaning_parsed.id`.

**Assessment:** Complete and well-structured. Actively used for sense-level analysis.

---

### wa_meaning_stem (13 rows)

**Purpose:** Summary of Hebrew stems found in meaning text. Aggregates stem information across senses.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| parsed_meaning_id | INTEGER FK | Links to wa_meaning_parsed.id | Engine | Complete |
| stem_name | TEXT | Stem name (Qal, Niphal, Piel, etc.) | Engine (parsed) | Complete |
| stem_type | TEXT | Classification of stem type | Engine (parsed) | Functional |
| sense_count | INTEGER | Number of senses under this stem | Engine (parsed) | Complete |
| top_sense_text | TEXT | Primary sense text for this stem | Engine (parsed) | Functional |

**Relations:** FK to `wa_meaning_parsed.id`.

**Assessment:** Only 13 rows — stems are only present for Hebrew terms with explicit stem-structured meaning text. This is expected. Functional.

---

### wa_lsj_parsed (2 rows)

**Purpose:** Structured parse of Liddell-Scott-Jones lexicon entries for Greek terms. Captures classical Greek lexicographic detail.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| term_inv_id | INTEGER FK | Links to wa_term_inventory.id | Engine | Complete |
| raw_lsj | TEXT | Raw LSJ entry text | STEP API | Complete |
| lsj_gloss | TEXT | LSJ gloss | Parsed | Complete |
| lsj_domains | TEXT | Semantic domains from LSJ | Parsed | Sparse (50%) |
| lsj_philosophical_note | TEXT | Philosophical usage notes | Parsed | **ALL NULL** |
| lsj_etymology_note | TEXT | Etymology notes | Parsed | **ALL NULL** |
| lsj_cognate_forms | TEXT | Related cognate forms | Parsed | **ALL NULL** |
| parsed_at | TEXT | Parse timestamp | Engine | Complete |
| parse_version | TEXT | Parser version | Engine | Complete |

**Relations:** FK to `wa_term_inventory.id`.

**Assessment:** **Near-unused** — only 2 rows populated. The LSJ parsing pipeline was prototyped but never scaled. Three fields are all NULL. Not blocking but represents unrealised potential for Greek term analysis.

---

## 8. Flags

### phase2_flag_types (25 rows)

**Purpose:** Reference table defining all Phase 2 / Session B analytical flag codes. Used by both `wa_term_phase2_flags` (per-inventory) and `mti_term_flags` (per-MTI-term).

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Migration seed / patches | Complete |
| flag_code | TEXT | Machine-readable code (e.g. GOD_AS_SUBJECT, SOMATIC_INNER_LINK) | Migration seed / patches | Complete (25 unique) |
| description | TEXT | Human-readable description | Migration seed / patches | Functional |

**Relations:** Referenced by `wa_term_phase2_flags.flag_id`, `mti_term_flags.flag_id`.

**Assessment:** Complete reference table.

---

### wa_term_phase2_flags (1,580 rows)

**Purpose:** Analytical flags assigned to individual term inventory records by Claude AI during Session B. Not touched by the engine.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| term_inv_id | INTEGER PK | Links to wa_term_inventory.id (composite PK) | Claude AI (patches) | Complete |
| flag_id | INTEGER PK | Links to phase2_flag_types.id (composite PK) | Claude AI (patches) | Complete |
| description | TEXT | Flag-specific description | Claude AI | Sparse (1%) — rarely provided |
| source | TEXT | Who raised the flag | Claude AI | Functional (71%) — backfilled for newer flags |
| raised_date | TEXT | When the flag was raised | Claude AI | Functional (71%) — matches source |

**Relations:** FK to `wa_term_inventory.id`, `phase2_flag_types.id`.

**Assessment:** Functional. The 29% NULL on `source`/`raised_date` is from early flags before those fields were added (M14). The `description` sparseness is by design — most flags are self-explanatory from the flag_code.

---

### wa_quality_flag_types (29 rows) — extended 2026-04-15

**Purpose:** Reference table defining engine-derived quality flag codes (DATA_COVERAGE group) and session-scoped flag codes used across `wa_data_quality_flags` and `wa_session_research_flags`.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Migration seed / DIR-20260415-002 | Complete |
| flag_group | TEXT | Legacy group classification (DATA_COVERAGE / SESSION_B / SESSION_D) | Migration seed | Complete |
| flag_code | TEXT | Machine-readable code | Migration seed / DIR-20260415-002 | Complete (29 unique) |
| description | TEXT | Human-readable description | Migration seed / DIR-20260415-002 | Complete |
| deprecated | INTEGER | 1 = deprecated, 0 = active (added 2026-04-15 via DIR-20260415-001) | DIR-20260415-001 | Complete (3 deprecated) |
| deprecation_note | TEXT | Reason for deprecation (added 2026-04-15) | DIR-20260415-001 | Functional (populated on deprecated rows only) |
| category | TEXT | Classifier: DATA_QUALITY / SESSION_D_POINTER / STUDY_REQUIRED / RESEARCHER_DECISION (added 2026-04-15) | DIR-20260415-002 | Sparse (15/29) — populated on new rows only |

**Relations:** Referenced by `wa_data_quality_flags.flag_id` and (via string match) `wa_session_research_flags.flag_code`.

**Assessment:** Extended 2026-04-15. 14 pre-existing rows (category NULL) + 15 new rows (category populated) + 3 deprecated rows. The 15 new rows provide reference entries for the flag codes used in `wa_session_research_flags` (previously orphaned). The loose string match between `wa_session_research_flags.flag_code` and `wa_quality_flag_types.flag_code` remains — no FK constraint was added.

---

### wa_data_quality_flags (22,129 rows)

**Purpose:** Engine-derived quality indicators per term. Reset and re-derived on every audit_word run (DATA_COVERAGE group only). Non-derivable flags are preserved.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| file_id | INTEGER FK | Links to wa_file_index.id | Engine (flag_engine) | Complete |
| term_id | TEXT | Strong's number | Engine | Complete |
| flag_id | INTEGER FK | Links to wa_quality_flag_types.id | Engine (flag_engine) | Complete |
| description | TEXT | Flag-specific description with context | Engine (flag_engine) | Complete |
| last_changed | TEXT | Row modification timestamp | Engine | Sparse (2%) — most rows lack timestamp |

**Relations:** FK to `wa_file_index.id`, `wa_quality_flag_types.id`.

**Assessment:** Well-populated. The `last_changed` sparseness is an oversight in flag_engine.py — it does not set the timestamp on most inserts. Not blocking but inconsistent with other tables.

---

## 9. Verse Context

### verse_context_group (3,550 rows)

**Purpose:** Contextual meaning groups — clusters of verses that share a common inner-being characteristic. One group per term per contextual meaning. The grouping unit for Session B analysis.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key (used as FK by verse_context) | Auto-generated | Complete |
| mti_term_id | INTEGER FK | Links to mti_terms.id — programme-wide term identity | Claude Code (from patch) | Complete (2,238 unique terms) |
| group_code | TEXT | Unique group identifier (e.g. "H7965-G1") | Claude AI (via patch) | Complete (3,550 unique) |
| context_description | TEXT | Characteristic-perspective description of what this group of verses is about | Claude AI (via patch) | Complete (3,520 unique) |
| notes | TEXT | Additional group notes | Claude AI (via patch) | Sparse (9%) — only where needed |
| delete_flagged | INTEGER | Soft delete flag | Engine | Complete |
| vertical_pass_flag | INTEGER | Marks groups for future vertical pass analysis | Claude AI | Complete (all 0 — not yet used) |

**Relations:** FK to `mti_terms.id`. Parent to `verse_context`, `wa_dimension_index`.

**Assessment:** Complete and well-structured. Every group has a description and a unique code. The `vertical_pass_flag` is provisioned but not yet activated.

---

### verse_context (63,028 rows)

**Purpose:** Per-verse classification record. Records whether each verse is relevant to the inner being through its associated term, which group it belongs to, and whether it is an anchor or related verse.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| verse_record_id | INTEGER FK | Links to wa_verse_records.id | Claude Code (from patch) | Complete |
| mti_term_id | INTEGER FK | Links to mti_terms.id — enables cross-registry sharing | Claude Code (from patch) | Complete |
| group_id | INTEGER FK | Links to verse_context_group.id (NULL for set-aside verses) | Claude Code (from patch) | Functional (57%) — 27,230 NULL are set-aside (is_relevant=0) verses |
| is_anchor | INTEGER | Whether this verse is an anchor for its group (1/0) | Claude AI (via patch) | Complete |
| is_relevant | INTEGER | Whether this verse engages the inner being through this term (1/0) | Claude AI (via patch) | Complete |
| is_related | INTEGER | Whether this verse is a related (supporting) verse in the group (1/0) | Claude AI (via patch) | Complete |
| notes | TEXT | Classification notes | Claude AI (via patch) | Sparse (10%) — only where noteworthy |
| delete_flagged | INTEGER | Soft delete flag | Engine | Complete |
| vertical_pass_flag | INTEGER | Marks verse for future vertical pass analysis | Claude AI | Complete (all 0 — not yet used) |
| set_aside_reason | TEXT | Why a verse was set aside (no_inner_being, physical_only, spatial_only, wrong_face, other) | Claude AI (via patch, from v2.5) | Sparse (0.8%) — only populated from VCB-032 onward when v2.5 added the field |

**Relations:** FK to `wa_verse_records.id`, `mti_terms.id`, `verse_context_group.id`.

**Assessment:** Second-largest active data table. Classification fields (is_anchor, is_relevant, is_related) are fully populated and well-structured. The `group_id` NULL rate (43%) is entirely explained by set-aside verses (is_relevant=0) which correctly have no group. The `set_aside_reason` extreme sparseness (0.8%) is because it was only added in v2.5 (VCB-032 onward) — earlier batches (VCB-001 through VCB-031) did not have this field. Retroactive backfill would require re-reading each verse, which is not planned.

---

## 10. Dimension Review

### wa_dimension_index (3,500 rows)

**Purpose:** Dimension assignments per verse_context_group. Maps each group to an emergent inner-being dimension, tracks confidence level, and records the dominant subject. The bridge between Verse Context grouping and Session B analysis.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| verse_context_group_id | INTEGER FK | Links to verse_context_group.id (1:1) | Claude Code (from patch) | Complete |
| mti_term_id | INTEGER FK | Links to mti_terms.id | Claude Code (from patch) | Complete |
| strongs_number | TEXT | Strong's number (denormalised for query convenience) | Claude Code | Complete |
| transliteration | TEXT | Romanised form (denormalised) | Claude Code | Complete |
| gloss | TEXT | English gloss (denormalised) | Claude Code | Complete |
| language | TEXT | Hebrew or Greek (denormalised) | Claude Code | Complete |
| owning_registry_no | INTEGER | Registry number (denormalised) | Claude Code | Complete |
| owning_registry_word | TEXT | English word (denormalised) | Claude Code | Complete |
| cluster_assignment | TEXT | Cluster code C01–C22 (denormalised) | Claude Code | Complete |
| group_code | TEXT | Group code from verse_context_group (denormalised) | Claude Code | Complete |
| context_description | TEXT | Group description (denormalised) | Claude Code | Complete |
| dimension | TEXT | Emergent dimension label (e.g. "emotional_distress", "divine_encounter") | Claude AI (via patch) | Functional (93%) — 250 NULL from groups not yet reviewed |
| anchor_count | INTEGER | Number of anchor verses in the group | Computed | Complete |
| related_count | INTEGER | Number of related verses in the group | Computed | Complete |
| set_aside_count | INTEGER | Number of set-aside verses | Computed | Complete |
| total_verse_count | INTEGER | Total verses in the group | Computed | Complete |
| delete_flagged | INTEGER | Soft delete flag | Engine | Complete |
| dimension_confidence | TEXT | Confidence level: AUTOMATED, CLAUDE_AI, RESEARCHER, etc. | Claude AI / Researcher | Complete |
| manual_override | INTEGER | Whether dimension is locked by researcher confirmation | Researcher (via patch) | Complete |
| notes | TEXT | Notes on dimension assignment | Claude AI (via patch) | Sparse (40%) — only where analytical notes exist |
| last_modified | TEXT | Row modification timestamp | Claude Code | Complete |
| dominant_subject | TEXT | What the group is primarily about | Claude AI (via patch) | Sparse (27%) — only populated for Dimension Review completed registries |

**Relations:** FK to `verse_context_group.id`, `mti_terms.id`.

**Assessment:** Well-structured denormalised view. The 7% NULL on `dimension` and 73% NULL on `dominant_subject` reflect the current Dimension Review progress — 5 clusters completed (C01, C06, C17, C18, C20) out of 22. Both fields will fill as reviews progress. The denormalisation is intentional for query performance.

---

### wa_dim_review_cluster_log (5 rows)

**Purpose:** Completion record per cluster. One row per completed Dimension Review. The gate check for Session B DataPrep.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| cluster | TEXT | Cluster code (C01, C06, etc.) | Claude Code (from patch) | Complete |
| completed_date | TEXT | Completion date | Claude Code | Complete |
| instruction_version | TEXT | Instruction version used | Claude Code | Complete |
| registry_count | INTEGER | Number of registries in the cluster | Claude Code | Complete |
| group_count | INTEGER | Number of groups reviewed | Claude Code | Complete |
| anchored_count | INTEGER | Number of anchored groups | Claude Code | Complete |
| notes | TEXT | Completion notes | Claude Code | Functional |
| last_modified | TEXT | Row modification timestamp | Auto (default) | Complete |

**Relations:** None (standalone log).

**Assessment:** Complete for the 5 clusters reviewed. Will grow to 22 as all clusters are processed. Functions as the DataPrep gate.

---

## 11. Cross-Registry Links

### wa_crosslink_type (11 rows)

**Purpose:** Reference table defining cross-registry connection types (semantic overlap, root shared, antonym, etc.).

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Manual seed | Complete |
| type_code | TEXT | Machine-readable code | Manual seed | Complete (11 types) |
| description | TEXT | Human-readable description | Manual seed | Complete |

**Relations:** Referenced by `wa_cross_registry_links.connection_type_id`.

**Assessment:** Complete reference table.

---

### wa_cross_registry_links (158 rows)

**Purpose:** Explicit semantic connections between registries, created during Session A analysis. Records which words are connected, how, and through which term.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| file_id | INTEGER FK | Links to wa_file_index.id | Engine (import) | Complete |
| linked_word | TEXT | Word label of the linked registry | Engine | Complete |
| linked_registry_id | INTEGER FK | Links to word_registry.id | Engine | Functional (96%) — 7 NULL from unresolved links |
| connection_type_id | INTEGER FK | Links to wa_crosslink_type.id | Engine | Complete (all 11 types used) |
| connecting_term | TEXT | The Strong's number that creates the connection | Engine | Functional (96%) |
| note | TEXT | Description of the connection | Engine | Complete |
| last_changed | TEXT | Row modification timestamp | Engine | Functional (92%) |

**Relations:** FK to `wa_file_index.id`, `word_registry.id`, `wa_crosslink_type.id`.

**Assessment:** Functional. The 158 rows represent Session A-era connections. Session B and D will add significantly more connections through the correlation and SD pointer systems.

---

## 12. Session B Structured

### wa_session_b_dimensions (2 rows)

**Purpose:** Dimensional profile per registry — records which inner-being dimensions are engaged and how. Originally designed for Session B v1-v2 instruction; largely superseded by `wa_dimension_index`.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| registry_id | INTEGER FK | Links to word_registry.id | Claude AI (patch) | Complete |
| file_id | INTEGER FK | Links to wa_file_index.id | Claude AI (patch) | Complete |
| relational_environment | INTEGER | Whether the word operates in relational contexts (1/0) | Claude AI | Complete |
| relational_environment_note | TEXT | Reasoning | Claude AI | Complete |
| spirit_soul_body | INTEGER | Whether the word engages spirit-soul-body dimensions (1/0) | Claude AI | Complete |
| spirit_soul_body_note | TEXT | Reasoning | Claude AI | Complete |
| inner_operations | INTEGER | Whether the word describes inner operations (1/0) | Claude AI | Complete |
| inner_operations_note | TEXT | Reasoning | Claude AI | Complete |
| being | INTEGER | Whether the word touches being/existence (1/0) | Claude AI | Complete |
| being_note | TEXT | Reasoning | Claude AI | Complete |
| raised_date | TEXT | Date raised | Claude AI | Complete |
| session_b_instruction | TEXT | Instruction version used | Claude AI | Complete |

**Relations:** FK to `word_registry.id`.

**Assessment:** **Near-unused** — only 2 rows from early Session B pilot. The dimensional profiling function has moved to `wa_dimension_index` which provides group-level granularity rather than registry-level. This table may be retired or repurposed.

---

### wa_session_b_findings (171 rows) — extended 2026-04-15

**Purpose:** Key analytical findings from Session B analysis and Dimension Review, captured as structured records. Extended 2026-04-15 with lifecycle fields supporting confirm/correct/deepen/set-aside/supersede workflows.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| finding_id | TEXT | Unique finding identifier | Claude AI (patch) | Complete (171 unique) |
| registry_id | INTEGER FK | Links to word_registry.id | Claude AI (patch) | Complete (109 registries covered) |
| file_id | INTEGER FK | Links to wa_file_index.id | Claude AI (patch) | Sparse (12%) — not always linked |
| finding_type | TEXT | UPPER_SNAKE_CASE classification (controlled vocab — see below) | Claude AI (patch) | Complete (7 types in use post-normalisation) |
| finding | TEXT | The finding text | Claude AI (patch) | Complete |
| anchor_verses | TEXT | Supporting verse references | Claude AI (patch) | Sparse (35%) — not all findings need verse anchors |
| raised_date | TEXT | Date raised | Claude AI (patch) | Complete |
| session_b_instruction | TEXT | Instruction version | Claude AI (patch) | Complete (9 versions) |
| pass_ref | TEXT | Phase/pass attribution (e.g. 'Session B Pass 3', 'Dimension Review Phase C C17') | Claude AI (patch) | Unused (all NULL — pending use) |
| study_segment | TEXT | Rendering target (controlled vocab from obs schema §14) | Claude AI (patch) | Unused |
| delete_flag | INTEGER | 0 = active; 1 = set aside/superseded | Claude AI / Claude Code | Complete (all 0) |
| obsolete_reason | TEXT | Required when delete_flag = 1 | Claude AI / Claude Code | Unused |
| obsolete_date | TEXT | Date marked obsolete | Claude AI / Claude Code | Unused |
| superseded_by_id | INTEGER FK | Self-ref FK — points to replacement finding | Claude AI / Claude Code | Unused |
| related_finding_id | INTEGER | Link to pointer resolved, prior finding superseded, or related | Claude AI / Claude Code | Unused |
| resolution_note | TEXT | Review outcome note for confirmed/deepened findings | Claude AI | Unused |
| thin_evidence | INTEGER | 1 = supported by thin evidence; must resolve before session close | Claude AI | Complete (all 0) |

**Controlled vocabulary for `finding_type`** (post 2026-04-15 normalisation):
MEANING_OBSERVATION, VERSE_PATTERN, VERSE_ANNOTATION, THEOLOGICAL_NOTE, SOMATIC_EVIDENCE, SPIRIT_SOUL_BODY, ETYMOLOGY, ROOT_FINDING, DIMENSION_REVIEW, DIMENSION_PATTERN, GROUP_INTEGRITY, CROSS_REGISTRY, TERM_BEHAVIOUR, SESSION_C_CORRECTION, OPEN_ITEM.

**Current distribution:** DIMENSION_REVIEW (146), THEOLOGICAL_NOTE (8), VERSE_PATTERN (6), TERM_BEHAVIOUR (4), GROUP_INTEGRITY (3), ETYMOLOGY (2), DIMENSION_PATTERN (2).

**Relations:** FK to `word_registry.id`. Self-ref FK on `superseded_by_id`. Parent to `wa_finding_entity_links.finding_id`.

**Assessment:** Structurally ready for the finding lifecycle workflow. All 9 new fields are at initial state — they will populate as Session B v5.0 and subsequent passes exercise the confirm/correct/deepen/set-aside workflow. 171 existing findings have been preserved intact; only `finding_type` was normalised.

---

### wa_finding_entity_links (0 rows) — created 2026-04-15

**Purpose:** Junction table linking analytical findings to the specific entities they describe (terms, verses, groups, dimensions, root families, cross-registry connections). Created 2026-04-15 via DIR-20260415-005 to enable querying findings by entity type/id — a capability that did not exist before.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| finding_id | INTEGER FK | Links to wa_session_b_findings.id | Claude AI / Claude Code | New — empty |
| entity_type | TEXT | Controlled: term / verse / group / dimension / registry / root_family / cross_registry | Claude AI | New — empty |
| entity_id | INTEGER | Polymorphic id in the entity's own table; FK integrity enforced by CC at write time | Claude AI / Claude Code | New — empty |
| entity_strongs | TEXT | Denormalised Strong's number for term links | Claude AI | New — empty |
| raised_date | TEXT | Date the link was created | Claude AI / Claude Code | New — empty |

**Indexes:**
- `idx_wfel_finding_id` on `(finding_id)` — for lookups from a finding to its entities
- `idx_wfel_entity` on `(entity_type, entity_id)` — for reverse lookup from an entity to its findings

**Relations:** FK to `wa_session_b_findings.id` (SQL-enforced). `entity_id` is polymorphic — no SQL FK; Claude Code must validate at write time.

**Assessment:** **Empty — schema ready, workflow pending.** Will be populated as Session B v5.0 writes findings that reference specific entities. Enables: "find all findings about term X", "find all findings referencing verse Y", "find all findings in dimension Z".

---

## 13. Session Research Flags

### wa_session_research_flags (327 rows) — updated 2026-04-15

**Purpose:** Research flags raised during Session B, Dimension Review, and Verse Context work. Includes SD_POINTER (Session D pointers), PH2_* flags, and others. **Updated 2026-04-15** (DIR-20260415-003): 19 rows with `flag_code = 'VOLUME_LIMITATION'` consolidated to canonical `'PH2_VOLUME_LIMITATION'` (count now 52). Total distinct flag codes: 15 (was 16).

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Internal primary key | Auto-generated | Complete |
| registry_id | INTEGER FK | Links to word_registry.id | Claude AI (patch) | Complete (72 registries) |
| file_id | INTEGER FK | Links to wa_file_index.id | Claude AI (patch) | Sparse (38%) — not always applicable |
| flag_code | TEXT | Flag type code (SD_POINTER, SB_FINDING, etc.) | Claude AI (patch) | Complete (16 distinct codes) |
| flag_label | TEXT | Human-readable label | Claude AI (patch) | Complete (all unique) |
| strongs_reference | TEXT | Associated Strong's number | Claude AI (patch) | Functional (49%) — not all flags are term-specific |
| cross_registry_id | INTEGER FK | Target registry for cross-registry flags | Claude AI (patch) | Functional (46%) — only for cross-registry flags |
| priority | TEXT | HIGH, MEDIUM, LOW | Claude AI (patch) | Complete |
| session_target | TEXT | Which session will resolve: D, B | Claude AI (patch) | Complete |
| description | TEXT | Detailed flag description | Claude AI (patch) | Complete (all unique) |
| session_raised | TEXT | Session identifier | Claude AI (patch) | Complete |
| raised_date | TEXT | Date raised | Claude AI (patch) | Complete |
| resolved | INTEGER | Whether the flag has been resolved (1/0) | Claude Code | Complete (all 0 — none resolved yet) |
| resolved_date | TEXT | When resolved | — | **ALL NULL** — no flags resolved yet |
| resolved_note | TEXT | Resolution details | — | **ALL NULL** — no flags resolved yet |

**Relations:** FK to `word_registry.id`, `wa_file_index.id`.

**Assessment:** Actively growing. 327 flags across 72 registries (primarily SD_POINTERs from Session B completed words). The `resolved` / `resolved_date` / `resolved_note` fields are all in initial state — flag resolution is a Session D activity. The `file_id` sparseness is by design — many flags are registry-level, not file-level.

---

## 14. Session D

### session_d_runs (0 rows)
### session_d_verse_links (0 rows)
### session_d_term_links (0 rows)
### session_d_observations (0 rows)

**Purpose:** Cross-registry synthesis capture tables. Designed to record Session D analytical sessions, shared verse intersections, shared term divergences, and cross-registry observations.

**session_d_runs:**
| Field | Type | Purpose |
|-------|------|---------|
| id | INTEGER PK | Primary key |
| run_id | TEXT | Session D run identifier |
| run_date | TEXT | Session date |
| cluster_ref | TEXT | Cluster being analysed |
| registries_in_scope | TEXT | Which registries are included |
| registries_completed_at_run | INTEGER | How many registries were Session B Complete at time of run |
| session_b_sources | TEXT | Source data references |
| run_summary | TEXT | Summary of findings |
| json_filename | TEXT | Output file reference |

**session_d_verse_links:**
| Field | Type | Purpose |
|-------|------|---------|
| id | INTEGER PK | Primary key |
| run_id | TEXT | Session D run reference |
| verse_ref | TEXT | Verse reference |
| registry_ids | TEXT | Which registries share this verse |
| terms_involved | TEXT | Strong's numbers present |
| overlap_count | INTEGER | Number of registries at this verse |
| threshold_met | INTEGER | Whether significance threshold met |
| gate | TEXT | Session D gate classification |
| raised_date | TEXT | When identified |

**session_d_term_links:**
| Field | Type | Purpose |
|-------|------|---------|
| id | INTEGER PK | Primary key |
| run_id | TEXT | Session D run reference |
| strongs_id | TEXT | Strong's number |
| transliteration | TEXT | Romanised form |
| registry_data | TEXT | Cross-registry data |
| status_divergence | INTEGER | Whether term status differs across registries |
| gate | TEXT | Session D gate classification |
| raised_date | TEXT | When identified |

**session_d_observations:**
| Field | Type | Purpose |
|-------|------|---------|
| id | INTEGER PK | Primary key |
| run_id | TEXT | Session D run reference |
| observation_id | TEXT | Unique observation identifier |
| observation_type | TEXT | Observation classification |
| registries_implicated | TEXT | Which registries are involved |
| terms_implicated | TEXT | Which terms are involved |
| structural_note | TEXT | Structural details |
| source_refs | TEXT | Supporting references |
| gate | TEXT | Session D gate classification |
| researcher_flag | INTEGER | Whether flagged for researcher attention |
| raised_date | TEXT | When raised |

**Assessment:** **All four tables empty.** Session D has not started — it requires Session B completion across enough registries to enable cross-word synthesis. The SD_POINTER flags in `wa_session_research_flags` are the precursors that will feed into these tables. The schema is ready.

---

## 15. Engine Control

### engine_run_log (617 rows)

**Purpose:** Full audit trail for every engine execution. Records mode, timing, counts, and outcome for each run.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | Auto-generated | Complete |
| run_id | TEXT | Unique run identifier (RUN-YYYYMMDD_HHMMss-MODE) | Engine | Complete |
| mode | TEXT | Engine mode (audit_word, new_word, gap_fill, etc.) | Engine | Complete |
| target_registry_ids | TEXT | Which registries were targeted | Engine | Functional |
| started_at | TEXT | Run start timestamp | Engine | Complete |
| completed_at | TEXT | Run completion timestamp | Engine | Functional — NULL for aborted runs |
| outcome | TEXT | PASS, REVIEW, STOP, or error | Engine | Functional |
| words_attempted | INTEGER | Number of words targeted | Engine | Complete |
| words_complete | INTEGER | Number of words completed | Engine | Complete |
| words_stopped | INTEGER | Number of words stopped | Engine | Complete |
| total_terms_new | INTEGER | New terms inserted | Engine | Complete |
| total_terms_xref | INTEGER | XREF terms identified | Engine | Complete |
| total_verses_inserted | INTEGER | Verses inserted | Engine | Complete |
| total_verses_filtered | INTEGER | Verses filtered by span check | Engine | Complete |
| total_meanings_parsed | INTEGER | Meanings parsed | Engine | Complete |
| error_detail | TEXT | Error message if failed | Engine | Functional — NULL when no error |
| resume_from | TEXT | Checkpoint for resumption | Engine | Functional |

**Relations:** Parent to `engine_stream_checkpoint`, `term_fetch_log`, `word_run_state`.

**Assessment:** Complete operational log. 617 runs recorded.

---

### engine_stream_checkpoint (1,169 rows)

**Purpose:** Per-stream progress tracking within engine runs. Enables resumption after interruption.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | Auto-generated | Complete |
| run_id | TEXT FK | Links to engine_run_log.run_id | Engine | Complete |
| stream_name | TEXT | Which processing stream (terms, verses, related, etc.) | Engine | Complete |
| status | TEXT | pending, running, complete, error | Engine | Complete |
| last_registry_id | TEXT | Last registry processed | Engine | Functional |
| last_strong | TEXT | Last Strong's number processed | Engine | Functional |
| rows_written | INTEGER | Rows written in this stream | Engine | Complete |
| rows_filtered | INTEGER | Rows filtered out | Engine | Complete |
| error_detail | TEXT | Error message if failed | Engine | Functional |
| started_at | TEXT | Stream start | Engine | Functional |
| completed_at | TEXT | Stream completion | Engine | Functional |

**Relations:** FK to `engine_run_log.run_id`.

**Assessment:** Complete operational checkpoint data.

---

### term_fetch_log (2,317 rows)

**Purpose:** Per-term STEP API fetch log. Records what was fetched, resolved, stored, and filtered for each Strong's number in each run.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | Auto-generated | Complete |
| run_id | TEXT FK | Links to engine_run_log.run_id | Engine | Complete |
| registry_id | TEXT | Registry being processed | Engine | Complete |
| strongs_input | TEXT | Strong's number requested | Engine | Complete |
| strongs_resolved | TEXT | Strong's number after suffix resolution | Engine | Functional |
| suffix_resolution | INTEGER | Whether suffix was resolved | Engine | Complete |
| vocab_status | TEXT | Vocabulary fetch outcome | Engine | Functional |
| verse_status | TEXT | Verse fetch outcome | Engine | Functional |
| verse_count_fetched | INTEGER | Verses received from STEP | Engine | Complete |
| verse_count_stored | INTEGER | Verses stored in DB | Engine | Complete |
| verse_count_filtered | INTEGER | Verses filtered out | Engine | Complete |
| span_conflict | INTEGER | Whether span conflicts were detected | Engine | Complete |
| api_warnings | TEXT | API-level warnings | Engine | Functional |
| fetched_at | TEXT | Fetch timestamp | Engine | Functional |

**Relations:** FK to `engine_run_log.run_id`.

**Assessment:** Complete fetch audit trail.

---

### word_run_state (437 rows)

**Purpose:** Per-word outcome from each engine run. Records audit result, approval status, and stop reasons.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | Auto-generated | Complete |
| run_id | TEXT FK | Links to engine_run_log.run_id | Engine | Complete |
| registry_id | TEXT | Registry number | Engine | Complete |
| word | TEXT | English word | Engine | Complete |
| phase_reached | TEXT | Furthest step reached (A1-A11) | Engine | Functional |
| audit_result | TEXT | PASS, REVIEW, or STOP | Engine | Functional |
| audit_detail | TEXT | Detailed audit results (JSON) | Engine | Functional |
| stop_reason | TEXT | Why the run stopped (if stopped) | Engine | Functional |
| researcher_approved | INTEGER | Whether researcher has signed off | Engine | Complete |
| approved_by | TEXT | Who approved (PROVISIONAL for engine) | Engine | Functional |
| approved_at | TEXT | Approval timestamp | Engine | Functional |

**Relations:** FK to `engine_run_log.run_id`.

**Assessment:** Complete operational state tracking.

---

## 16. Schema Metadata

### schema_version (3 rows)

**Purpose:** Records schema version and full migration history. The engine checks this at startup to ensure compatibility.

| Field | Type | Purpose | Source | Readiness |
|-------|------|---------|--------|-----------|
| id | INTEGER PK | Primary key | Auto-generated | Complete |
| version_code | TEXT | Schema version (currently "3.8.0") | Engine (migrate.py) | Complete |
| applied_at | TEXT | When this version was applied | Engine | Complete |
| migration_history | TEXT | Full JSON history of all migrations (M01–M18) | Engine | Complete |
| engine_min_version | TEXT | Minimum engine version required | Engine | Functional (NULL — not enforced) |

**Relations:** None.

**Assessment:** Complete. 3 rows representing major schema milestones (initial, 3.0.0, 3.8.0).

---

## Summary: Tables by Readiness

### Fully Active and Well-Populated
| Table | Rows | Assessment |
|-------|------|-----------|
| word_registry | 214 | Core anchor table |
| wa_term_inventory | 7,550 | Core term data |
| mti_terms | 7,571 | Programme-wide term index |
| wa_verse_records | 229,778 | Core verse data |
| wa_verse_term_links | 226,791 | Verse-term associations |
| verse_context | 63,028 | Verse classification |
| verse_context_group | 3,550 | Contextual meaning groups |
| wa_dimension_index | 3,500 | Dimension assignments |
| wa_data_quality_flags | 22,129 | Engine-derived quality flags |
| wa_term_related_words | 101,970 | Lexical relatives |
| wa_meaning_parsed | 7,449 | Structured meaning parse |
| wa_meaning_sense | 15,981 | Sense-level parse |
| wa_session_research_flags | 327 | Research flags (growing). 2026-04-15: 19 VOLUME_LIMITATION → PH2_VOLUME_LIMITATION |
| wa_session_b_findings | 171 | Analytical findings (growing). 2026-04-15: +9 lifecycle fields; finding_type normalised |

### Functional but Sparse
| Table | Rows | Reason |
|-------|------|--------|
| wa_term_root_family | 2,861 | 22% gap from pre-backfill era |
| wa_term_phase2_flags | 1,580 | Growing as Session B progresses |
| wa_finding_entity_links | 0 | Created 2026-04-15; will populate as Session B v5.0 writes linked findings |
| wa_cross_registry_links | 158 | Session A era; will grow |
| mti_term_cross_refs | 464 | Functional for sharing analysis |
| mti_term_flags | 54 | Early — growing with Session B |
| wa_dim_review_cluster_log | 5 | 5 of 22 clusters reviewed |
| wa_meaning_stem | 13 | Only Hebrew stem-structured terms |

### Unused or Near-Unused
| Table | Rows | Assessment |
|-------|------|-----------|
| themes | 0 | Never used — superseded by cluster_assignment |
| sources | 0 | Never used — Zotero integration not operationalised |
| wa_lsj_parsed | 2 | Prototyped, not scaled |
| wa_session_b_dimensions | 2 | Superseded by wa_dimension_index |
| session_d_runs | 0 | Session D not yet started |
| session_d_verse_links | 0 | Session D not yet started |
| session_d_term_links | 0 | Session D not yet started |
| session_d_observations | 0 | Session D not yet started |

### Completely Unused Fields (across active tables)
| Table | Field | Note |
|-------|-------|------|
| wa_verse_records | note | ALL NULL — never used |
| wa_verse_records | claude_output | ALL NULL — superseded by verse_context |
| wa_term_inventory | god_as_subject | Superseded by mti_term_flags |
| wa_term_inventory | somatic_link | Superseded by mti_term_flags |
| wa_term_inventory | status_note | NULL across nearly all records |
| wa_term_inventory | meaning | Superseded by wa_meaning_parsed |
| wa_term_inventory | meaning_numbered | Superseded by wa_meaning_parsed |
