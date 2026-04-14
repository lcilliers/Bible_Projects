# CLAUDE.md — Claude Code Project Reference

> Auto-generated 2026-03-24; updated 2026-04-12 for v4.7/v5.8/v1.10 instruction refresh + Session B progress.
> This file is read by Claude Code at the start of every conversation.

---

## 1. What This Project Is

A structured academic Bible research platform centred on **~214 English words** (anger, love, soul, peace, etc.) describing the **inner life of mankind**. Each word maps to Hebrew (OT) and Greek (NT) terms via Strong's numbers. The system captures occurrence data, verse records, parse analysis, semantic flags, and cross-registry links — all in a relational SQLite database processed by a custom Python automation engine.

**Owner:** le Roux Cilliers (leRoux) — sole researcher, ultimate authority on scope and methodology.

**AI roles:**
- **Claude Code** — database engine: patch application, JSON export, schema migrations, validation queries, programme state reporting, Verse Context batch construction, pool analysis dataset assembly
- **Claude AI** — analytical engine: term classification, verse analysis, scope judgements, narrative production, JSON extraction, Verse Context classification

**Governing documents (April 2026):** Documents in `data/imports/WA/Workflow/Framework_B/Session_B/` supersede all prior versions. Claude Code's consolidated responsibilities are in `WA-SessionB-ClaudeCode-Instructions-v3.2`. Key versions: WA-SessionB-Instruction-v4.7, WA-Registry-Management-Guide-v5.8, patch_specification-v1.10, WA-DimensionReview-Instruction-v2.2, WA-VerseContext-Instruction-v2.5, WA-Reference-v5.5.

---

## 2. Directory Map — Where Everything Lives

```
Bible_study_projects/              ← Google Drive root = working directory
│
├── CLAUDE.md                      ← THIS FILE (Claude Code project context)
├── README.md                      ← Human-facing project overview
├── .gitignore                     ← Tracks code+docs; excludes .db, exports, binaries
│
├── engine/                        ← Python automation engine (the core application)
│   ├── engine.py                  ← CLI entry point (python -m engine.engine)
│   ├── constants.py               ← Schema version (3.8.0), thresholds, sentinels
│   ├── db.py                      ← Connection factory (WAL mode), query helpers
│   ├── migrate.py                 ← Schema migrations M01–M18 (v2.2 → v3.8.0)
│   ├── backup.py                  ← Pre/post-run + manual backups (rolling 10)
│   ├── register.py                ← REGISTER mode + lock management
│   ├── new_word.py                ← NEW_WORD mode (N1–N19): first-time STEP fetch
│   ├── gap_fill.py                ← GAP_FILL mode (S1–S8): backfill missing streams
│   ├── audit_word.py              ← AUDIT_WORD mode (A1–A11): ingest Step 1 JSON, full sync
│   ├── flag_engine.py             ← Derivable quality flag computation (DATA_COVERAGE group)
│   ├── meaning_parser.py          ← Parse meaning text → wa_meaning_parsed/sense/stem/lsj
│   ├── span_filter.py             ← STEP HTML span matching (Strong's confirmation)
│   ├── audit.py                   ← WR-01–WR-20 post-write validation checks
│   ├── report.py                  ← --report: word overview (text/markdown)
│   └── run_log.py                 ← Run ID generation, engine_run_log/checkpoint/fetch helpers
│
├── analytics/                     ← Python library: API clients + DB utilities
│   ├── bible_analytics.py         ← CLI entry: --init-db, --test-step, --import-json, etc.
│   ├── db_client.py               ← SQLite connection, JSON import/export, table whitelist
│   ├── step_client.py             ← STEP Bible API client (localhost:8989)
│   ├── zotero_client.py           ← Zotero API wrapper
│   ├── word_export.py             ← export_word(): full word → nested dict → JSON
│   └── requirements.txt           ← pyzotero, pandas, jsonschema, python-docx, etc.
│
├── scripts/                       ← Utility and maintenance scripts
│   ├── env_setup.ps1              ← Environment bootstrap (venv, deps, .env template)
│   ├── word_study_extract.py      ← STEP data pull → discovery JSON + summary MD
│   ├── word_full_extract.py       ← Denormalized flat CSV export
│   ├── export_word_json.py        ← CLI wrapper for word_export.export_word()
│   ├── _discover_word_terms.py    ← Phase 1: term discovery from English anchor
│   ├── _apply_term_decisions.py   ← Phase 2: programmatic include/exclude filters
│   ├── _extract_word_terms.py     ← Phase 3: full DB CRUD sync from decisions
│   ├── _apply_*_patch.py          ← One-off patch applicators (stems, flags, descriptions, metadata)
│   ├── _repair_*.py               ← DB structural fixes (zero-padding, FK recreation)
│   ├── _assess_*.py / _check_*.py ← Read-only diagnostics and consistency checks
│   ├── _realign_*.py              ← Re-parse / re-compute operations (modify DB)
│   ├── _reset_registry_status.py  ← Bulk phase1_status correction
│   ├── _delete_empty_fi.py        ← Remove orphan wa_file_index rows
│   ├── verify_soul.py             ← Post-audit verification for Soul (registry 182)
│   ├── inspect_db_only_terms.py   ← Detail query for DB_ONLY terms
│   ├── list_tables.py             ← Quick table listing
│   ├── query_h2734.py             ← Inspect specific Strong's across tables
│   └── _tmp_*.py                  ← Throwaway ad-hoc scripts (temporary)
│
├── data/
│   ├── bible_research.db          ← SQLite database (NOT in Git, ~40 MB)
│   ├── file_manifest.json          ← Machine-readable file index (generated by build_file_manifest.py)
│   ├── schema/
│   │   └── create_tables.sql      ← Full DDL (versioned, authoritative)
│   ├── imports/WA/
│   │   ├── Session_A_Data/        ← 44 Claude-produced JSON files (Phase 1 data)
│   │   ├── Patches/               ← Claude-produced JSON patch files
│   │   ├── Word_Data/             ← Source markdown from STEP research
│   │   ├── Session_B_Analysis/    ← Analysis markdown outputs
│   │   ├── Session_C_Synthesis/   ← Cross-part synthesis documents
│   │   └── Workflow/              ← Session instruction templates
│   │       ├── Framework_B/Session_B/  ← v5 governing documents (active)
│   │       └── Sessionlogs/            ← Historical session logs
│   ├── exports/                   ← JSON exports for Claude (word_export output)
│   │   └── verse_context/         ← Verse Context batch exports (wa-vcb-*.json)
│   └── discovery/                 ← STEP discovery output (word_study_extract.py)
│
├── outputs/                       ← Research outputs and session reports
│   ├── markdown/                  ← General markdown outputs
│   ├── docx/                      ← .docx for external consumption
│   ├── pdf/                       ← Final publishable products
│   ├── word_reports/              ← CSV exports from automation runs
│   ├── audit_diff_*.md            ← Detailed word audit diff reports
│   └── session-*.md               ← Session findings and plans
│
├── docs/                          ← Project documentation
│   ├── file-organisation-rules.md ← File placement rules (MUST READ before writing files)
│   ├── interaction-preferences.md ← Communication protocols (MUST READ)
│   ├── Session-A-v9-Architecture-*.md ← Engine specification document
│   ├── data_setup.md              ← SQLite platform guide
│   ├── step_setup.md              ← STEP Bible API guide
│   ├── zotero_setup.md            ← Zotero API guide
│   ├── field-data-flow-mapping.md  ← Data flow mapping
│   └── pipeline_design_review*.md ← Architecture decisions
│
├── research/                      ← Research notes and templates
│   ├── notes/                     ← Working notes
│   ├── projects/                  ← Project briefs
│   └── templates/                 ← claude_session, project_brief, research_note templates
│
├── Logs/                          ← Historical session logs (timestamped markdown)
├── backups/                       ← Engine-managed DB backups (NOT in Git)
└── archive/                       ← Retired scripts and old exports
    ├── scripts/                   ← 50+ legacy migration/inspection scripts
    └── docs/                      ← Archived JSON exports, architecture docs
```

---

## 3. The Database — Schema v3.8.0

**File:** `data/bible_research.db` (SQLite, ~40 MB, excluded from Git)

### Table Groups

| # | Group | Key Tables | Purpose |
|---|-------|------------|---------|
| 1 | Reference | `books`, `book_code_variants`, `themes`, `sources` | Static: 66 Bible books, code aliases |
| 2 | Registry | `word_registry` | Master list of ~212 words (the anchor for everything) |
| 3 | WA File Index | `wa_file_index` | One row per imported Session A JSON; parent for all WA tables |
| 4 | WA Term Data | `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` | Per-term metadata: glosses, meaning, occurrences, flags. `term_owner_type` (OWNER/XREF) classifies each term. |
| 5 | Phase 2 Flags | `phase2_flag_types`, `wa_term_phase2_flags` | Semantic/analytical flags (set by Claude) |
| 6 | Quality Flags | `wa_quality_flag_types`, `wa_data_quality_flags` | DATA_COVERAGE flags (engine-derived). Includes CONCRETE_PHYSICAL. |
| 7 | Cross-Registry | `wa_crosslink_type`, `wa_cross_registry_links` | Semantic links between word registries |
| 7b | Session Research | `wa_session_research_flags` | Session B/C/D research findings (PH2, SB_FINDING, SB_DIMENSION, SD_POINTER flags) |
| 8 | Verse Records | `wa_verse_records`, `wa_verse_term_links` | **Core research table**: one row per term-in-verse occurrence. `mti_term_id` FK for direct term lookup. |
| 9 | MTI | `mti_terms`, `mti_term_flags`, `mti_term_cross_refs` | Mounce Term Index terms and cross-refs |
| 10 | Engine Control | `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log` | Full audit trail for every engine run |
| 11 | Meaning Parse | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | Structured parse of meaning text |
| 12 | Metadata | `schema_version` | Current schema version and migration history |
| 13 | Session B Structured | `wa_session_b_dimensions`, `wa_session_b_findings` | Dimensional profiles and key findings per registry |
| 14 | Session D | `session_d_runs`, `session_d_verse_links`, `session_d_term_links`, `session_d_observations` | Cross-registry synthesis capture |
| 15 | Verse Context | `verse_context_group`, `verse_context` | Contextual meaning groups and per-verse classification (v3.8.0, M18) |

### Key Relationships

```
word_registry (no=registry_id)
    ├─ wa_file_index (word_registry_fk → word_registry.id)
    │   ├─ wa_term_inventory (file_id → wa_file_index.id)
    │   │   ├─ wa_term_related_words
    │   │   ├─ wa_term_root_family
    │   │   ├─ wa_term_phase2_flags
    │   │   ├─ wa_data_quality_flags (file_id + term_inv_id)
    │   │   ├─ wa_meaning_parsed → wa_meaning_sense, wa_meaning_stem
    │   │   ├─ wa_lsj_parsed
    │   │   └─ wa_verse_records (file_id + term_inv_id)
    │   │       ├─ wa_verse_term_links
    │   │       └─ verse_context (verse_record_id → wa_verse_records.id)
    │   └─ mti_terms (owning_registry_fk → word_registry.id)
    │       ├─ mti_term_flags
    │       ├─ mti_term_cross_refs
    │       └─ verse_context_group (mti_term_id → mti_terms.id)
    │           └─ verse_context (group_id → verse_context_group.id)
    └─ [verse_context_status, session_b_status — dual status tracks on word_registry]
```

### XREF Architecture

- `mti_terms`: one record per Strong's number, programme-wide
- `wa_term_inventory.term_owner_type`: **OWNER** (canonical home, verses active, Verse Context processes) or **XREF** (cross-reference copy, verses delete_flagged, verse context derived from OWNER)
- `verse_context` uses `mti_term_id` — OWNER and XREF registries see the same records
- Current scale: 5,518 OWNER terms, 1,470 XREF terms, 133,353 active verses (OWNER only)

### Data Conventions

- **Strong's numbers:** `H` = Hebrew, `G` = Greek. Suffix letters (e.g. `H7965H`) = sub-entries
- **Language values:** Always `"Hebrew"` or `"Greek"` (capitalised)
- **Dates:** ISO-8601 UTC: `2026-03-19T18:08:49Z`
- **Booleans:** INTEGER — `1` = true, `0` = false
- **Soft deletes:** `delete_flagged=1` (no physical deletes in automated flows)

---

## 4. The Engine — How It Works

**Invocation:** `python -m engine.engine [options]`

### Engine Modes

| Mode | Command | What It Does |
|------|---------|-------------|
| NEW_WORD | `--mode=new_word` | **Superseded** — retained for reference. Use AUDIT_WORD for all words. |
| GAP_FILL | `--mode=gap_fill` | **Superseded** — retained for reference. Use AUDIT_WORD for all words. |
| AUDIT_WORD | `--mode=audit_word --registry=N` | Unified pipeline: ingests Step 1 JSON, inserts terms + verses in single pass, syncs DB, resets flags, runs audit. Works for both new and existing words. |
| MIGRATE | `--migrate [--dry-run]` | Applies pending schema migrations (M01–M18) |
| REGISTER | `--register --word="..." --source="..."` | Adds new word to word_registry |
| REPORT | `--report --registry=N [--format=markdown]` | Prints word overview report |
| EXPORT | `--export-word --registry=N` | Exports all word data to JSON |
| EXPORT_REGISTRY | `--export-registry` | Exports full word_registry to JSON (for Extraction sessions) |

### Key Flags

```
--dry-run              Preview without writing
--force                Override lock checks
--interactive          Enable confirmation prompts (AUDIT_WORD)
--skip-span-backpop    Skip span backpopulation
--streams=S1,S3        Run only specified streams (GAP_FILL)
--extract-file=PATH    Override auto-discovery of Step 1 JSON (AUDIT_WORD)
```

### Engine Architecture

```
engine.py (CLI dispatcher)
├── new_word.py (N1–N19) ──┐
├── gap_fill.py (S1–S8) ───┤── All three call:
├── audit_word.py (A1–A11) ─┘   audit.py (WR-01–WR-20)
│                                flag_engine.py (derivable flags)
│                                meaning_parser.py (sense/stem parse)
│                                span_filter.py (HTML span matching)
│                                run_log.py (run tracking)
├── register.py (word registration + locks)
├── report.py (word overview)
├── migrate.py (M01–M18 migrations)
├── backup.py (pre/post-run backups)
├── db.py (connection + helpers)
└── constants.py (schema version 3.8.0, thresholds)
```

### Key Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| EXPECTED_SCHEMA_VERSION | `"3.8.0"` | Engine refuses mismatched schema |
| LOCK_SENTINEL | `"IN_PROGRESS"` | Prevents concurrent runs |
| AUDITED_SENTINEL | `"AUDITED"` | Marks successful audit completion |
| HIGH_FREQ_THRESHOLD | 500 | Above → HIGH_FREQUENCY_ANCHOR flag |
| THIN_DATA_THRESHOLD | 20 | Below → THIN_DATA flag |
| SMALL_VERSE_SAMPLE_THRESHOLD | 5 | Below → SMALL_VERSE_SAMPLE flag |
| BACKUP_RETENTION | 10 | Rolling pre-run backup count |
| STALE_LOCK_SECONDS | 7200 | 2 hours → lock considered stale |

### Audit Checks (WR-01 through WR-20)

Three-state outcome: **PASS** (all good), **REVIEW** (non-critical issues), **STOP** (critical failures).

Key checks: file_index exists (WR-01), terms present (WR-03), all strongs in mti_terms (WR-04), verses present (WR-06), verse/occurrence ratio ≥ 0.15 (WR-08), meaning populated (WR-10), transliteration present (WR-11, STOP), language valid (WR-12, STOP), derivable flags assessed (WR-16), span back-population complete (WR-20).

---

## 5. The STEP Bible API Client

**File:** `analytics/step_client.py`
**Target:** Local STEP Bible server at `http://localhost:8989` (Tomcat embedded)

### Key Methods

| Method | Returns | Used For |
|--------|---------|----------|
| `get_vocab_info(strong)` | Lexical data dict (gloss, meaning, related words, etc.) | Term metadata |
| `get_verse_records(strong)` | All ESV verse occurrences for a Strong's number | Verse population |
| `get_verse_records_with_html(strong)` | Same + raw STEP HTML per verse (for span filtering) | Span confirmation |
| `get_strongs_for_word(english)` | All Strong's tagging an English word in ESV | Term discovery |
| `get_related_term_cluster(strong)` | Full term cluster (sub-glosses + related terms) | Phase 1 mapping |
| `extract_word_data(strong)` | Comprehensive data package (vocab + verses + notes) | Word study |

### Pagination

STEP API caps results at 60. The client uses two-layer canonical section splits (Torah/History/Poetry/Prophets/NT, each halved if needed) to get complete coverage.

---

## 6. Script Naming Conventions

| Prefix | Meaning | Safe? |
|--------|---------|-------|
| `_assess_*`, `_check_*` | Read-only diagnostics | Yes |
| `_apply_*` | Apply a JSON patch to DB | **No** — modifies DB |
| `_repair_*` | Structural DB fixes (FK, columns) | **No** — DDL changes |
| `_realign_*`, `_reset_*` | Re-compute / bulk update | **No** — modifies DB |
| `_delete_*` | Remove rows | **No** — destructive |
| `_discover_*`, `_explore_*`, `_probe_*` | API exploration, read-only | Yes |
| `_extract_*` | DB sync from decisions | **No** — modifies DB |
| `_tmp_*` | Throwaway ad-hoc scripts | Varies |
| `apply_session_patch.py` | Apply Session B/C/D/VerseContext/REPAIR JSON patches | **No** — modifies DB |
| `word_study_extract.py` | STEP data pull (no DB writes) | Yes |
| `word_full_extract.py` | CSV export (read-only) | Yes |
| `export_word_json.py` | JSON export (read-only) | Yes |
| `verify_*.py`, `inspect_*.py` | Post-operation verification | Yes |
| `_batch_extract.py` | Subprocess-isolated batch STEP extraction + audit_word | **No** — modifies DB |
| `_produce_final_extract.py` | Final registry extract from database | Yes (read-only) |
| `_generate_programme_report.py` | Comprehensive programme status report | Yes (read-only) |
| `_update_reference_doc.py` | Reference document update utility | Varies |
| `build_complete_extract.py` | Comprehensive per-word extract (9 layers incl. correlations) | Yes (read-only) |
| `build_correlation_extract.py` | Programme-wide inter-word correlation (5 signals) | Yes (read-only) |
| `build_dimension_extract.py` | Dimension review cluster/group/rootfamily extracts | Yes (read-only) |
| `generate_registry_overview.py` | Full registry overview JSON (all 214 registries) | Yes (read-only) |
| `build_file_manifest.py` | Project file manifest (indexes all files incl. archive) | Yes (read-only) |

---

## 7. Word Study Pipeline (3 Phases)

### Phase 1 — Term Discovery
```
scripts/_discover_word_terms.py --english <word>
    → data/discovery/{word}_term_map_{YYYYMMDD}.json
    → data/discovery/{word}_triage_{YYYYMMDD}.md
```
English text search → primary Strong's codes → cluster expansion → triage table.

### Phase 2 — Term Decisions
```
scripts/_apply_term_decisions.py --input <term_map.json>
    → data/discovery/{word}_term_decisions_{YYYYMMDD}.json
```
Programmatic filters: proper nouns (exclude), particles (exclude), lexically distant (exclude), sub-glosses (include), root-family (include/review).

### Phase 3 — Database Sync
```
scripts/_extract_word_terms.py --decisions <decisions.json> [--dry-run]
```
INCLUDE → upsert terms/verses/meanings. EXCLUDE → cascade delete. Rebuilds verse_term_links.

### Alternative: Single-Pass Extraction
```
scripts/word_study_extract.py --word <word> [--anchors H1234,G5678]
    → data/discovery/{word}_step_data_{YYYYMMDD}.json
    → data/discovery/{word}_step_data_{YYYYMMDD}.md
```
Replaces the 3-script pipeline for quick STEP data pulls.

---

## 8. Data Flow Patterns

### Full Pipeline (v5.6)

```
Phase 1: Register → STEP Extract → audit_word → Export JSON
    │
    ▼
Verse Context (Stage 1):
    Claude Code constructs batch JSON (2,000–2,500 verses)
    → Claude AI classifies verses (relevance, grouping, anchors)
    → Claude Code applies VERSECONTEXT patch
    → Claude Code validates (R1–R4, anchor integrity, XREF coverage)
    → Claude Code advances verse_context_status to Complete per registry
    → Claude Code re-exports full word JSON (opens DataPrep gate)
    → Loop until all 181 registries complete
    │
    ▼
Session B (Stage 2 — pool-based):
    DataPrep: Claude AI classifies terms → PREANALYSIS patch → Claude Code applies → re-export
    → Claude Code monitors pool readiness (all words at Pre-Analysis Complete)
    → Claude Code assembles pool analysis dataset
    Analysis: Claude AI reads pool dataset → narrative per word → ANALYSIS patch → Claude Code applies
    Extraction: Claude AI extracts structured data → SESSIONB patch → Claude Code applies
    → Post-patch: final registry extract + Session D pointers
    → SESSIONB-COMPLETE patch → Session B Complete
```

### Claude.ai → Database
```
Claude.ai produces JSON patch → wa-{nnn}-{word}-patch-{date}.json
    → python scripts/apply_session_patch.py
    → Records inserted/updated in bible_research.db
```
**Rule:** Never import raw Claude output directly. Always validate via Python apply script.

**Patch types:** PREANALYSIS, SESSIONB, VERSECONTEXT, VCGROUP, VCVERSE, REPAIR, SESSIOND, CLUSTERING

### Database → Claude.ai
```
# Engine export (STEP format)
python -m engine.engine --export-word --registry=N
    → data/exports/STEP Extracts/{word}_{registry}_{scope}_{YYYYMMDD}_v{N}.json

# Complete extract (Session B format — preferred for Claude AI)
python scripts/build_complete_extract.py --registry=N [--complete-only|--owner-only]
    → data/exports/Session C/wa-{NNN}-{word}-{scope}-{YYYYMMDD}.json
    (9 layers: registry, terms, verses, verse_context, dimensions, Session B/D, cross-links, correlations, statistics)
```
Scope is `full` (pre-analysis) or `final` (Analysis Complete / Session B Complete).
Version auto-increments: v1, v2, v3 per day.

### Verse Context Batch Flow
```
Claude Code queries DB → data/exports/verse_context/wa-vcb-{batch_id}-extract-{date}.json
    → Claude AI classifies → wa-vcb-{batch_id}-patch-{date}.json
    → Claude Code applies patch (resolves group_code → integer id)
    → Claude Code validates consistency rules + advances registry status
```

### Pool Analysis Dataset Flow
```
Claude Code assembles → data/exports/wa-pool-{pool_id}-analysis-{date}.json
    → Claude AI reads for Session B Analysis
```

### Post-Patch Outputs (v5.6)

After an analysis completion patch is applied, two additional files are produced:
```
Final registry extract: data/exports/{word}_{registry}_final_{YYYYMMDD}_v{N}.json
Session D pointers:     data/exports/session_d/wa-{nnn}-{word}-sdpointers-{YYYYMMDD}.json
```
The final extract is a cross-table view for Session D. The sdpointers file carries
evaluated cross-registry observations with synthesis questions.

### STEP API → Database
```
python -m engine.engine --mode=audit_word --registry=N
    → STEP API fetch → span filter → DB write (atomic transaction)
```

---

## 9. Interaction Protocols (from docs/interaction-preferences.md)

1. **Instruction Confirmation:** Before non-trivial tasks — summarise understanding, state approach, WAIT for approval.
2. **Output & Workings:** Write analysis/workings to `.md` files, not just chat. Place in `docs/`, `outputs/`, or relevant subfolder.
3. **Factual Discipline:** Work only with explicit facts. Don't guess. Stop and ask if unclear.
4. **File Organisation:** Follow `docs/file-organisation-rules.md` for all file placement and naming. Archive superseded versions promptly.
5. **Manifest Maintenance:** Run `python scripts/build_file_manifest.py` after processing a session log or after any batch of file moves/archiving. The manifest indexes all files including archived ones.

---

## 10. v5.5/v5.6 Document Architecture (March 2026)

Documents in `data/imports/WA/Workflow/Framework_B/Session_B/`:

| Document | Version | Purpose | Primary Audience |
| -------- | ------- | ------- | ---------------- |
| WA-Implementation-Instruction | v5 | Schema changes, new tables, programme operations (Tasks 1-8) | Claude Code |
| WA-Reference | **v5.5** | Controlled vocabulary, naming conventions, schema reference (v3.8.0), document validation standard | Both systems |
| WA-Registry-Management-Guide | **v5.8** | Registry structure, dual status lifecycle, cluster assignments (C01-C22), pool IDs, periodic reviews | Both systems |
| **WA-SessionB-Instruction** | **v4.7** | **Unified Session B instruction: 6-pass analytical process, directive delivery (D1/D2), CC coordination** | **Both systems** |
| **WA-SessionB-ClaudeCode-Instructions** | **v3.2** | **Consolidated Claude Code responsibilities, REPAIR catalogue, failure patches** | **Claude Code** |
| **WA-DimensionReview-Instruction** | **v2.2** | **Dimension review stage — cluster-level review, group classification, dominant_subject** | **Both systems** |
| **WA-VerseContext-Instruction** | **v2.5** | **Verse Context stage — batch construction, classification, patch application** | **Both systems** |
| **patch_specification** | **v1.10** | **Authoritative patch applicator rules, all operation types, status workflow** | **Claude Code** |

### Key Changes (v5.8/v4.7/v1.10 from earlier versions)

- **Verse Context stage added**: New pipeline stage between Phase 1 and DataPrep — classifies all 133,353 active verses by inner-being relevance, groups by contextual meaning, designates anchor verses
- **Dual status tracks**: `session_b_status` + `verse_context_status` on word_registry
- **Pool-based Session B**: Analysis runs per pool (not per individual word). Pool analysis datasets assembled by Claude Code.
- **Verse Context Reset**: New session_b_status value — prior Session B work superseded
- **Ready for Analysis**: Now legacy — only set by audit_word COALESCE on NULL status (new words only)
- **REPAIR patch catalogue**: Four cascade reset types (STEP re-run, audit_word re-run, VC re-run, Analysis re-run)
- **Failure patch protocol**: Mandatory on any patch rejection — record failure before retry
- **Schema v3.8.0**: M17 (dimensions rename, anchor_verses removal) + M18 (verse_context tables, verse_context_status field)
- **XREF architecture**: OWNER/XREF term ownership, shared verse_context via mti_term_id
- **Mid-pool interruption**: System failure detection — mixed pool states trigger recovery patches
- **Four outputs per registry** (unchanged): Session B JSON, analysis patch, final registry extract, Session D pointers file
- **source_category → dimensions** (M17): Comma-delimited multi-value field. anchor_verses field removed.
- **Cluster assignments complete**: All 212 words assigned to C01-C22.

### Session B Workflow (v4.7 — per-registry, 6-pass)

```
Verse Context (Stage 1):
    Claude Code batch → Claude AI classifies → VERSECONTEXT patch → verse_context_status = Complete
    │
    ▼
Session B (Stage 2 — per registry, 6 passes):
    Claude Code produces complete extract (build_complete_extract.py)
    │
    Pass 1: Data audit + remediation → PREANALYSIS patch (D1 delivery)
    Pass 2: GOD_AS_SUBJECT, somatic flags, FRAMEWORK_SIGNAL
    Pass 3: Root family, correlation analysis → D1 delivery to CC
    │  CC applies D1 directives → fresh extract R2
    │
    Pass 4: Somatic scan (SOMATIC_INNER_LINK, BODY_INNER_EXPRESSION)
    Pass 5: sb_classification determination
    Pass 6: Session D pointers (SD_POINTER flags) → D2 delivery to CC
    │  CC applies D2 directives → fresh extract R3
    │
    ▼
Session C (Stage 3): Word study production + Session C notes
    │
    ▼
Status close: session_b_status → Analysis Complete
```

### Implementation Tasks Status

Tasks 1-8 from WA-Implementation-Instruction-v5: **all complete** (schema v3.8.0, migrations M01–M18). Clustering (Task 4) applied. Zero-term investigation (Task 5) resolved.

### Current Programme State (2026-04-12)

- 214 total registries (213 listen + 214 suffering added since March)
- 182 registries VC Complete, 1 In Progress (grace — pending XREF VC from regs 23/73), 31 NULL (excluded)
- C17 Dimension Review complete (cluster stamp set), C01-C16/C18-C22 previously completed
- 3 registries at Session B Analysis Complete: grace (68), mercy (111), compassion (23)
- SD pointers enriched across all three: grace=50, mercy=16, compassion=31
- Love (103) Session B extract prepared, pending analytical work
- Suffering (214): C05, 72 terms, 907 verses, VCB-034 batch prepared, VC/dim review pending
- Session B uses unified 6-pass instruction (v4.7) with D1/D2 directive delivery points

---

## 11. Common Operations Quick Reference

```bash
# Schema status
python -m engine.engine --db-status

# Apply pending migrations
python -m engine.engine --migrate

# Check for stale locks
python -m engine.engine --check-locks

# Clear a stuck lock
python -m engine.engine --clear-lock --registry=42

# Run audit on a word
python -m engine.engine --mode=audit_word --registry=4

# Word report
python -m engine.engine --report --registry=4

# Export word to JSON
python -m engine.engine --export-word --registry=4

# Export full word registry (for Extraction sessions)
python -m engine.engine --export-registry

# Apply a session patch (PREANALYSIS, SESSIONB, VERSECONTEXT, REPAIR, etc.)
python scripts/apply_session_patch.py --patch-file <path_to_patch.json>

# Full integrity check
python scripts/_integrity_full_check.py

# STEP discovery pull
python scripts/word_study_extract.py --word anger --anchors H2734

# Programme status report
python scripts/_generate_programme_report.py

# Registry overview JSON (all registries, for Claude AI)
python scripts/generate_registry_overview.py

# Complete word extract (Session B format, 9 layers incl. correlations)
python scripts/build_complete_extract.py --registry=N --complete-only

# Dimension review batch (3 files per cluster)
python scripts/build_dimension_extract.py --cluster C17
python scripts/build_dimension_extract.py --pointers C17
python scripts/build_dimension_extract.py --rootfamily C17

# Programme-wide correlations
python scripts/build_correlation_extract.py

# File manifest — rebuild after session log or file moves
python scripts/build_file_manifest.py

# File manifest — search
python scripts/build_file_manifest.py --search "grace"
python scripts/build_file_manifest.py --search "registry:068"
python scripts/build_file_manifest.py --search "type:observations"

# DB connection pattern (ad-hoc scripts)
import sqlite3, os
conn = sqlite3.connect(os.path.join('data', 'bible_research.db'))
conn.row_factory = sqlite3.Row
```

### Programme State Queries

```sql
-- Session B progress by status
SELECT session_b_status, COUNT(*) as count
FROM word_registry GROUP BY session_b_status ORDER BY session_b_status;

-- Verse Context progress
SELECT verse_context_status, COUNT(*) as count
FROM word_registry GROUP BY verse_context_status;

-- Registries where VC complete and DataPrep gate open
SELECT no, word, cluster_assignment
FROM word_registry
WHERE verse_context_status = 'Complete'
  AND session_b_status NOT IN ('Ready for Analysis','Pre-Analysis Complete','Analysis Complete','Session B Complete')
ORDER BY no;

-- OWNER terms still needing Verse Context classification
SELECT mt.strongs_number, mt.gloss, mt.owning_word, COUNT(vr.id) as verse_count
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
  AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE mt.status IN ('extracted','extracted_thin')
  AND NOT EXISTS (SELECT 1 FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0)
GROUP BY mt.id ORDER BY mt.owning_registry_fk, mt.strongs_number;

-- Pool processing readiness (not-shared words ready for independent Session B)
SELECT no, word, cluster_assignment, verse_context_status
FROM word_registry
WHERE term_sharing_ratio = 0.0 AND phase1_status = 'Complete'
  AND phase1_term_count > 0 AND verse_context_status = 'Complete'
ORDER BY no;

-- Cluster progress
SELECT cluster_assignment, COUNT(*) as total,
  SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete
FROM word_registry GROUP BY cluster_assignment;

-- Ownership distribution
SELECT term_owner_type, COUNT(*) as terms
FROM wa_term_inventory WHERE delete_flagged = 0
GROUP BY term_owner_type;
```

---

## 12. Git Conventions

- `data/bible_research.db` — **excluded** from Git
- `backups/` — **excluded** from Git
- `data/imports/WA/Patches/*.json` — **committed** (input record)
- Commit message format: `session YYYYMMDD: brief description`
- Branch: `main` (single branch workflow)
- Remote: `origin` → `github.com/lcilliers/Bible_Projects`

---

## 13. Environment

- **Platform:** Windows 11, Google Drive mount at `G:\My Drive\Bible_study_projects`
- **Python:** 3.14.0
- **Shell:** PowerShell 7+ (set `$env:PYTHONUTF8="1"` for encoding)
- **STEP Bible:** Local server at `http://localhost:8989`
- **Secrets:** `.env` file (ZOTERO_API_KEY, ZOTERO_USER_ID, STEP_BASE_URL)

---

## 14. Verse Context — Claude Code Operations

The Verse Context stage sits between Phase 1 and Session B DataPrep. It classifies all 133,353 active OWNER term verses by inner-being relevance, groups them by contextual meaning, and designates anchor verses. Governed by `WA-VerseContext-Instruction-v1.7`.

### 14.1 Batch Construction

Claude Code builds batch JSONs from the database for Claude AI to classify:

- **OWNER terms only** (`term_owner_type = 'OWNER'`, `mti_terms.status IN ('extracted', 'extracted_thin')`)
- **Target:** 2,000–2,500 unclassified verses per batch (never split a term)
- **Priority:** unclassified terms first, ordered by `owning_registry_fk` ascending
- **Batch ID:** sequential VCB-001, VCB-002, etc.
- **Output:** `data/exports/verse_context/wa-vcb-{batch_id}-extract-{date}.json`
- **SQL construction:** Claude Code's responsibility based on criteria in VC-Instruction Section 5.2

### 14.2 Patch Application

Three Verse Context patch types — all carry `session_b_status: null` (applicator must not reject):

| Type | Naming | Purpose |
|------|--------|---------|
| VERSECONTEXT | `PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1` | Full batch — all terms in batch |
| VCGROUP | `PATCH-{YYYYMMDD}-VCGROUP{group_id}-V1` | Targeted group update |
| VCVERSE | `PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V1` | Targeted verse update |

**group_code resolution:** After each `verse_context_group` insert, capture `last_insert_rowid()` and map `group_code → integer id` for subsequent `verse_context` inserts in the same patch.

### 14.3 Post-Patch Validation

Run after every Verse Context patch:

```sql
-- R1: set-aside rows clean (is_relevant=0 must have no group/anchor/related)
SELECT COUNT(*) FROM verse_context
WHERE is_relevant=0 AND (group_id IS NOT NULL OR is_anchor=1 OR is_related=1);

-- R2: anchor rows clean (is_anchor=1 must be relevant, not related, has group)
SELECT COUNT(*) FROM verse_context
WHERE is_anchor=1 AND (is_relevant=0 OR is_related=1 OR group_id IS NULL);

-- R3: related rows have an active anchor in their group
SELECT COUNT(*) FROM verse_context vc
WHERE is_related=1 AND NOT EXISTS (
  SELECT 1 FROM verse_context a
  WHERE a.group_id=vc.group_id AND a.is_anchor=1 AND a.delete_flagged=0);

-- Integrity: no active verse_context for deleted/excluded terms
SELECT mt.strongs_number, mt.status, COUNT(vc.id) as active_vc_rows
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.status IN ('delete','excluded') AND vc.delete_flagged = 0
GROUP BY mt.id;
```

All expected: 0. Any violation → report to researcher, do not advance status.

### 14.4 Registry Completion Check

After each VERSECONTEXT patch, for each affected registry:
1. **OWNER check:** Count unclassified OWNER terms (terms with no verse_context record)
2. **XREF check:** Count XREF terms whose OWNER has no verse_context records
3. **Double-check:** After writing `Complete`, re-verify both checks; reverse if inconsistent
4. If both = 0: `UPDATE word_registry SET verse_context_status = 'Complete' WHERE no = {N}`
5. Re-export: `python -m engine.engine --export-word --registry={N}` (opens DataPrep gate)

### 14.5 Re-extraction Trigger

After any `audit_word` re-run, detect new verses missing verse_context:
- Set owning registry `verse_context_status = 'In Progress'`
- Cascade delete_flag: `UPDATE verse_context SET delete_flagged = 1 WHERE verse_record_id IN (SELECT id FROM wa_verse_records WHERE delete_flagged = 1) AND delete_flagged = 0`

---

## 15. Patch System — Comprehensive Reference

**Authoritative document:** `patch_specification_v1_10-20260412.md`
**Applicator:** `scripts/apply_session_patch.py`

### 15.1 Patch Types

| Type | Naming | session_b_status | Governing Document |
|------|--------|-----------------|-------------------|
| PREANALYSIS | `PATCH-{date}-{nnn}-PREANALYSIS-V1` | Pre-Analysis Complete | DataPrep v5.6 |
| SESSIONB | `PATCH-{date}-{nnn}-SESSIONB-V1` | Analysis Complete | Extraction v5.6 |
| SESSIONB-COMPLETE | `PATCH-{date}-{nnn}-SESSIONB-COMPLETE-V1` | Session B Complete | Extraction v5.6 |
| ANALYSIS | `PATCH-{date}-{nnn}-ANALYSIS-V1` | Analysis Complete | Analysis v5.6 |
| VERSECONTEXT | `PATCH-{date}-VCB{nnn}-VERSECONTEXT-V1` | null | VC-Instruction v1.5 |
| VCGROUP | `PATCH-{date}-VCGROUP{id}-V1` | null | VC-Instruction v1.5 |
| VCVERSE | `PATCH-{date}-VCVERSE{id}-V1` | null | VC-Instruction v1.5 |
| REPAIR | `PATCH-{date}-{nnn}-REPAIR-{scenario}-V1` | varies | CC-Instructions v3.2 §15 |
| SESSIOND | `PATCH-{date}-SESSIOND-V1` | null | SessionD Orientation |
| CLUSTERING | `PATCH-{date}-CLUSTERS-V1` | null | Implementation v5 |

### 15.2 Supported Operation Types (automated)

| Operation | Table | Purpose |
|-----------|-------|---------|
| `update_mti_status` | mti_terms | Set status on single term |
| `bulk_update_mti_status` | mti_terms | Multiple terms to same status |
| `bulk_confirm_candidate_delete` | mti_terms | candidate_delete → delete |
| `bulk_update_none_to_delete` | mti_terms | NULL status → delete |
| `bulk_confirm_delete_flagged` | mti_terms | delete_flagged=1 + NULL → delete |
| `bulk_update_note` | mti_terms | Filter-based or strongs-list update |
| `bulk_update` | mti_terms | Nested match/set or flat format |
| `update_evidential_status` | wa_term_inventory | Set evidential_status + retention_note per term |
| `update_registry` | word_registry | Update fields on word_registry |
| `insert` | wa_session_research_flags | Insert research flags (PH2, SB_FINDING, SD_POINTER) |
| `insert` | verse_context_group | New contextual meaning group |
| `update` | verse_context_group | Revise/dissolve group |
| `insert` | verse_context | New verse classification record |
| `update` | verse_context | Revise existing classification |
| `registry_note` | — | Documentation only, no DB action |

### 15.3 Manual Operation Types (require Claude Code intervention)

`reassign_verses`, `restore_delete_flagged`, `add_cross_registry_links`, `add_quality_flag`, `populate_vtl`, `schema_investigation_note`

### 15.4 REPAIR Patch Catalogue

Four cascade reset types — all require researcher approval before application:

| Scenario | Patch naming | Target session_b_status | What is reset |
|----------|-------------|------------------------|---------------|
| STEP extraction re-run | `REPAIR-STEP-RERUN` | NULL | Everything — full pipeline restart |
| audit_word re-run | `REPAIR-AUDITWORD-RERUN` | Verse Context Reset | verse_context*, analytical outputs. wa_term_inventory NOT flagged (STALE_TERM handles) |
| Verse Context re-run | `REPAIR-VC-RERUN` | Verse Context Reset | verse_context*, analytical outputs. mti_terms.status NOT reset. |
| Analysis re-run | `REPAIR-ANALYSIS-RERUN` | Pre-Analysis Complete | Analytical outputs only. VC and DataPrep preserved. |

### 15.5 Failure Patch Protocol

When **any** patch is rejected by the applicator:
1. Produce REPAIR failure patch immediately: `PATCH-{date}-{nnn}-REPAIR-FAILURE-V1`
2. Contains one `registry_note` recording what failed
3. `session_b_status` carries current (unchanged) value
4. Apply the failure patch (records failure in patch history)
5. Report to researcher with: failure patch_id, rejected patch, rejection reason
6. Await researcher instruction before producing corrected patch

### 15.6 audit_word Re-run Requirements

When audit_word detects re-run for existing registry:
1. **REPAIR gate:** Check patch history for `REPAIR-AUDITWORD-RERUN` on this registry. If not found → halt.
2. **STALE_TERM:** Authoritative path for wa_term_inventory updates. No delete/re-insert.
3. **Post-run:** Check for `mti_terms.status = NULL` terms — report to researcher for DataPrep re-classification.

### 15.7 Mid-Pool Interruption

If mixed pool states detected (some words at Pre-Analysis Complete, some at Analysis Complete):
- **System failure** — stop immediately
- Produce REPAIR mid-pool recovery patch per affected word: `REPAIR-MIDPOOL-V1`
- Reset to Pre-Analysis Complete
- Report to researcher

---

## 16. Pool-Based Processing

### 16.1 Pool Analysis Dataset

**Trigger:** All words in a pool reach Pre-Analysis Complete.

**Pre-construction check (mandatory):**
1. Determine all registry_no values in pool (from `cluster_assignment` or RMG v5.6 Section 7a)
2. Verify `verse_context_status = 'Complete'` for all pool registries
3. If any not Complete → halt, report to researcher

**File naming:** `wa-pool-{pool_id}-analysis-{date}.json`
**Structure:** Defined in Analysis Instruction v5.6 Annexure B
**Contents:** Per-word registry meta, OWNER terms with contextual groups and anchor verse text, XREF term profiles with group descriptions and anchor references, cross-word map

### 16.2 Pool IDs

Defined in WA-Registry-Management-Guide v5.6 Section 7a. Key pools:

| pool_id | Words | Notes |
|---------|-------|-------|
| not-shared | 17 words (term_sharing_ratio = 0) | Independent, any order |
| unconnected | 47 words (below 15-term threshold) | Group by cluster |
| pool2-suffering | 11 suffering/fear words | Single batch |
| pool3-zeal through pool8-holiness | 2-3 word pairs | Single sessions |
| pool1-anger-pair through pool1-isolates | Pool 1 sub-pools | Most complex last |

### 16.3 Pool Readiness Monitoring

After every DataPrep patch, Claude Code checks if all words in the same pool are at Pre-Analysis Complete. If ready → report to researcher (pool assembly is not automatic).

---

## 17. Controlled Vocabulary Quick Reference

### 17.1 session_b_status

| Value | Meaning |
|-------|---------|
| NULL | Phase 1 excluded or not yet audited |
| Verse Context Reset | Prior Session B work superseded — reprocess through VC and pool-based Session B |
| Ready for Analysis | **Legacy** — only set by audit_word COALESCE on NULL status (new words only) |
| Pre-Analysis Complete | Pre-analysis patch applied |
| Analysis Complete | Session B narrative complete, analysis patch applied |
| Session B Complete | Full Session B cycle done |

### 17.2 verse_context_status

| Value | Meaning |
|-------|---------|
| NULL | Phase 1 excluded or zero-term — outside Verse Context scope |
| In Progress | Verse Context work pending or underway |
| Complete | All OWNER terms classified — registry may proceed to DataPrep |

### 17.3 Key Flag Codes

**wa_session_research_flags.flag_code:** PH2_* (various), SB_FINDING, SB_DIMENSION, SB_INNER_BEING, SD_POINTER, SD_CLUSTER, CANDIDATE_REGISTRY_WORD, VOLUME_LIMITATION

**wa_data_quality_flags.flag_code:** HIGH_FREQUENCY_ANCHOR, NO_VERSES, NO_WORD_ANALYSIS, PROSE_ONLY_MEANING, SMALL_VERSE_SAMPLE, SPAN_FILTER_APPLIED, SPAN_RESOLUTION_CONFLICT, THIN_DATA, CONCRETE_PHYSICAL

### 17.4 Evidential Status (wa_term_inventory.evidential_status)

confirmed | plausible | uncertain | instrumental | relational_only

### 17.5 Dimensional Weight

PRIMARY | SECONDARY | PERIPHERAL — used in final registry extract dimensional_profile

### 17.6 Redundant Fields — Do Not Write

| Field | Table | Note |
|-------|-------|------|
| god_as_subject | wa_term_inventory | Superseded by mti_term_flags |
| somatic_link | wa_term_inventory | Superseded by mti_term_flags |
| status_note | wa_term_inventory | NULL across all records, no pipeline purpose |
| inference_note | word_registry | Researcher-set only — pipeline must never overwrite |
| status_note | mti_terms | Written by audit_word A10 only, not by Session B |
