# CLAUDE.md — Claude Code Project Reference

> Auto-generated 2026-03-24; updated 2026-03-28 for v5.1/v5.2 document architecture.
> This file is read by Claude Code at the start of every conversation.

---

## 1. What This Project Is

A structured academic Bible research platform centred on **~212 English words** (anger, love, soul, peace, etc.) describing the **inner life of mankind**. Each word maps to Hebrew (OT) and Greek (NT) terms via Strong's numbers. The system captures occurrence data, verse records, parse analysis, semantic flags, and cross-registry links — all in a relational SQLite database processed by a custom Python automation engine.

**Owner:** le Roux Cilliers (leRoux) — sole researcher, ultimate authority on scope and methodology.

**AI roles:**
- **Claude Code** — database engine: patch application, JSON export, schema migrations, validation queries, programme state reporting
- **Claude AI** — analytical engine: term classification, verse analysis, scope judgements, narrative production, JSON extraction

**Governing documents (v5.1/v5.2, March 2026):** Documents in `data/imports/WA/Workflow/Frameword_B/Session_B/` supersede the monolithic v4.4 instruction. Claude Code's consolidated responsibilities are in `WA-SessionB-ClaudeCode-Instructions.md`. Key versions: WA-Reference-v5.1, WA-SessionB-Extraction-Instruction-v5.2, WA-Registry-Management-Guide-v7.

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
│   ├── constants.py               ← Schema version (3.6.0), thresholds, sentinels
│   ├── db.py                      ← Connection factory (WAL mode), query helpers
│   ├── migrate.py                 ← Schema migrations M01–M15 (v2.2 → v3.6.0)
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
│   ├── schema/
│   │   └── create_tables.sql      ← Full DDL (versioned, authoritative)
│   ├── imports/WA/
│   │   ├── Session_A_Data/        ← 44 Claude-produced JSON files (Phase 1 data)
│   │   ├── Patches/               ← Claude-produced JSON patch files
│   │   ├── Word_Data/             ← Source markdown from STEP research
│   │   ├── Session_B_Analysis/    ← Analysis markdown outputs
│   │   ├── Session_C_Synthesis/   ← Cross-part synthesis documents
│   │   └── Workflow/              ← Session instruction templates
│   │       ├── Frameword_B/Session_B/  ← v5 governing documents (active)
│   │       └── Sessionlogs/            ← Historical session logs
│   ├── exports/                   ← JSON exports for Claude (word_export output)
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
│   ├── interaction-preferences.md ← Communication protocols (MUST READ)
│   ├── Session-A-v9-Architecture-*.md ← Engine specification document
│   ├── data_setup.md              ← SQLite platform guide
│   ├── step_setup.md              ← STEP Bible API guide
│   ├── zotero_setup.md            ← Zotero API guide
│   ├── file_organization.md       ← Two-tier storage guide
│   ├── db_remediation_plan.md     ← DB fix history
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

## 3. The Database — Schema v3.7.0

**File:** `data/bible_research.db` (SQLite, ~40 MB, excluded from Git)

### Table Groups

| # | Group | Key Tables | Purpose |
|---|-------|------------|---------|
| 1 | Reference | `books`, `book_code_variants`, `themes`, `sources` | Static: 66 Bible books, code aliases |
| 2 | Registry | `word_registry` | Master list of ~212 words (the anchor for everything) |
| 3 | WA File Index | `wa_file_index` | One row per imported Session A JSON; parent for all WA tables |
| 4 | WA Term Data | `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` | Per-term metadata: glosses, meaning, occurrences, flags |
| 5 | Phase 2 Flags | `phase2_flag_types`, `wa_term_phase2_flags` | Semantic/analytical flags (set by Claude) |
| 6 | Quality Flags | `wa_quality_flag_types`, `wa_data_quality_flags` | DATA_COVERAGE flags (engine-derived) |
| 7 | Cross-Registry | `wa_crosslink_type`, `wa_cross_registry_links` | Semantic links between word registries |
| 7b | Session Research | `wa_session_research_flags` | Session B/C/D research findings (PH2 flags) |
| 8 | Verse Records | `wa_verse_records`, `wa_verse_term_links` | **Core research table**: one row per term-in-verse occurrence |
| 9 | MTI | `mti_terms`, `mti_term_flags`, `mti_term_cross_refs` | Mounce Term Index terms and cross-refs |
| 10 | Engine Control | `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log` | Full audit trail for every engine run |
| 11 | Meaning Parse | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | Structured parse of meaning text |
| 12 | Metadata | `schema_version` | Current schema version and migration history |
| 13 | Session B Structured | `wa_session_b_dimensions`, `wa_session_b_findings` | Dimensional profiles and key findings per registry (v3.7.0) |
| 14 | Session D | `session_d_runs`, `session_d_verse_links`, `session_d_term_links`, `session_d_observations` | Cross-registry synthesis capture (v3.7.0) |

### Key Relationships

```
word_registry (no=registry_id)
    └─ wa_file_index (word_registry_fk → word_registry.id)
        ├─ wa_term_inventory (file_id → wa_file_index.id)
        │   ├─ wa_term_related_words
        │   ├─ wa_term_root_family
        │   ├─ wa_term_phase2_flags
        │   ├─ wa_data_quality_flags (file_id + term_inv_id)
        │   ├─ wa_meaning_parsed → wa_meaning_sense, wa_meaning_stem
        │   ├─ wa_lsj_parsed
        │   └─ wa_verse_records (file_id + term_inv_id)
        │       └─ wa_verse_term_links
        └─ mti_terms (owning_registry_fk → word_registry.id)
            ├─ mti_term_flags
            └─ mti_term_cross_refs
```

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
| MIGRATE | `--migrate [--dry-run]` | Applies pending schema migrations (M01–M12) |
| REGISTER | `--register --word="..." --source="..."` | Adds new word to word_registry |
| REPORT | `--report --registry=N [--format=markdown]` | Prints word overview report |
| EXPORT | `--export-word --registry=N` | Exports all word data to JSON |

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
├── migrate.py (M01–M15 migrations)
├── backup.py (pre/post-run backups)
├── db.py (connection + helpers)
└── constants.py (schema version 3.6.0, thresholds)
```

### Key Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| EXPECTED_SCHEMA_VERSION | `"3.7.0"` | Engine refuses mismatched schema |
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
| `apply_session_patch.py` | Apply Session B/C/D JSON patches | **No** — modifies DB |
| `word_study_extract.py` | STEP data pull (no DB writes) | Yes |
| `word_full_extract.py` | CSV export (read-only) | Yes |
| `export_word_json.py` | JSON export (read-only) | Yes |
| `verify_*.py`, `inspect_*.py` | Post-operation verification | Yes |

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

### Claude.ai → Database
```
Claude.ai produces JSON → data/imports/WA/Patches/*.json
    → python scripts/_apply_*_patch.py
    → Records inserted/updated in bible_research.db
```
**Rule:** Never import raw Claude output directly. Always validate via Python apply script.

### Database → Claude.ai
```
python -m engine.engine --export-word --registry=N
    → data/exports/{word}_{registry}_{scope}_{YYYYMMDD}_v{N}.json
```
Scope is `full` (pre-analysis) or `final` (Analysis Complete / Session B Complete).
Version auto-increments: v1, v2, v3 per day.

### Post-Patch Outputs (v5.2)

After an analysis completion patch is applied, two additional files are produced:
```
Final registry extract: data/exports/{word}_{registry}_final_{YYYYMMDD}_v{N}.json
Session D pointers:     data/exports/session_d/wa-{nnn}-{word}-sessiond-pointers-{YYYYMMDD}.json
```
The final extract is a cross-table view for Session D. The sdpointers file carries
evaluated cross-registry observations with synthesis questions.

### STEP API → Database
```
python -m engine.engine --mode=new_word --registry=N --terms=H1234,G5678
    → STEP API fetch → span filter → DB write (atomic transaction)
```

---

## 9. Interaction Protocols (from docs/interaction-preferences.md)

1. **Instruction Confirmation:** Before non-trivial tasks — summarise understanding, state approach, WAIT for approval.
2. **Output & Workings:** Write analysis/workings to `.md` files, not just chat. Place in `docs/`, `outputs/`, or relevant subfolder.
3. **Factual Discipline:** Work only with explicit facts. Don't guess. Stop and ask if unclear.

---

## 10. v5.1/v5.2 Document Architecture (March 2026)

Documents in `data/imports/WA/Workflow/Frameword_B/Session_B/`:

| Document | Version | Purpose | Primary Audience |
| -------- | ------- | ------- | ---------------- |
| WA-Implementation-Instruction | v5 | Schema changes, new tables, programme operations (Tasks 1-8) | Claude Code |
| WA-Reference | **v5.1** | Controlled vocabulary, naming conventions, schema reference, post-patch output templates | Both systems |
| WA-Registry-Management-Guide | **v7** | Registry structure, status lifecycle, cluster assignments (C01-C22), periodic reviews | Both systems |
| WA-SessionB-DataPrep-Instruction | v5 | Term classification, data preparation, pre-analysis patches | Claude AI |
| WA-SessionB-Analysis-Instruction | v5 | Verse reading, ten-step analysis protocol, narrative production | Claude AI |
| WA-SessionB-Extraction-Instruction | **v5.2** | JSON extraction, analysis patches, **four outputs per registry** | Claude AI |
| **WA-SessionB-ClaudeCode-Instructions.md** | — | **Consolidated Claude Code responsibilities** | **Claude Code** |

### v5.1/v5.2 Key Changes

- **Four outputs per registry** (was two): Session B JSON, analysis patch, final registry extract, Session D pointers file
- **Post-patch outputs**: `final` and `sdpointers` files produced AFTER patch confirmation (not during patch cycle)
- **source_category → dimensions**: Repurposed as comma-delimited multi-value field derived from Session B
- **Dimensional weight vocabulary**: PRIMARY / SECONDARY / PERIPHERAL per dimension
- **sdpointers file is evaluative**: carries synthesis_questions, significance, research_depth_required, prose_notes
- **session_b_revision_candidates**: Required field in final extract (empty array = explicit sync confirmation)
- **Cluster assignments complete**: All 212 words assigned to C01-C22. C01 (mind, Soul, heart, spirit, flesh, being) is complete.

### v5.2 Session B Workflow

```
DataPrep (Claude AI) → pre-analysis patch → Claude Code applies → re-export JSON
    → Analysis (Claude AI) → narrative document
    → Extraction (Claude AI, batch of ~5):
        1. Session B JSON
        2. Analysis completion patch → Claude Code applies → status = Analysis Complete
        3. Final registry extract (post-patch) → wa-{nnn}-{word}-final-{date}.json
        4. Session D pointers file (post-patch) → wa-{nnn}-{word}-sdpointers-{date}.json
```

### Implementation Tasks Status

Tasks 1-8 from WA-Implementation-Instruction-v5: **all complete** (schema v3.7.0, migration M16). Clustering (Task 4) applied. Zero-term investigation (Task 5) documented.

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

# Full integrity check
python scripts/_integrity_full_check.py

# STEP discovery pull
python scripts/word_study_extract.py --word anger --anchors H2734

# DB connection pattern (ad-hoc scripts)
import sqlite3, os
conn = sqlite3.connect(os.path.join('data', 'bible_research.db'))
conn.row_factory = sqlite3.Row
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
