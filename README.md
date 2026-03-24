# Bible_Projects — Technical Reference Guide

> **Repository:** [lcilliers/Bible_Projects](https://github.com/lcilliers/Bible_projects)
> **File Server (Google Drive):** `G:\My Drive\Bible_study_projects`
> **Schema version:** v3.1.0 · **Engine version:** 1.0.0 · **Python:** 3.14.0

---

## Table of Contents

1. [Project Purpose](#1-project-purpose)
2. [Participants and Roles](#2-participants-and-roles)
3. [Toolchain](#3-toolchain)
4. [Repository and File Structure](#4-repository-and-file-structure)
5. [Environment Setup — New Machine](#5-environment-setup--new-machine)
6. [Database Platform](#6-database-platform)
7. [Schema Reference](#7-schema-reference)
8. [The Automation Engine](#8-the-automation-engine)
9. [Key Scripts and Operations](#9-key-scripts-and-operations)
10. [Data Import / Patch Workflow](#10-data-import--patch-workflow)
11. [External API Integrations](#11-external-api-integrations)
12. [Project Rules and Conventions](#12-project-rules-and-conventions)

---

## 1. Project Purpose

This project supports deep academic Bible research focused on the **inner life of mankind** — words and concepts relating to the soul, emotions, states of being, and theological themes as expressed in the Hebrew Old Testament and Greek New Testament.

The aim is to produce **stunning, insightful, well-grounded, and comprehensive research outputs** — from structured data through to publishable documents.

The research corpus centres on **~211 English words** (e.g. anger, love, sorrow, peace) each of which maps to a set of Hebrew/Greek terms. For each term the project captures: occurrence data, verse records, parse analysis, semantic flags, and cross-registry links — all stored in a relational SQLite database and processed by a custom Python automation engine.

---

## 2. Participants and Roles

| Role | Participant | Responsibility |
|------|-------------|----------------|
| **Researcher** | le Roux Cilliers (leRoux) | Ultimate authority. Sets objectives, working methods, scope, and evaluates all outputs. This is leRoux's research — all other participants support his endeavours. |
| **Coding & Development** | GitHub Copilot (Claude Sonnet) | Primary AI for coding, database operations, engine development, and data patching. |
| **Thinker & Writer** | Claude.ai | Primary AI for analysis, synthesis, meaning extraction, flag assessment, and articulation. |

### Communication protocols for GitHub Copilot

Copilot must read and apply the protocols in [`docs/interaction-preferences.md`](docs/interaction-preferences.md) at the start of every session. This file is the authoritative record of how Copilot communicates with the researcher.

---

## 3. Toolchain

| Tool | Purpose |
|------|---------|
| **VS Code** | Project interface, coding, and development platform |
| **Python 3.14** | Automation engine, analytics, data processing |
| **SQLite** | Structured research database (`data/bible_research.db`) |
| **Git + GitHub** | Source control (`lcilliers/Bible_Projects`) |
| **Google Drive** | Large-file storage and file server (`G:\My Drive\Bible_study_projects`) |
| **PowerShell 7+** | Environment scripting and file management |
| **STEP Bible** | Scripture search, verse retrieval, Strong's/morphological data via API |
| **Zotero** | Reference management and source tracking via API |
| **Obsidian** | Note-taking (value still being evaluated) |

---

## 4. Repository and File Structure

### Two-tier storage model

- **Git repository** (`lcilliers/Bible_Projects`) — code, schema, scripts, documentation, patch files. The `.db` file is excluded from Git.
- **Google Drive** (`G:\My Drive\Bible_study_projects`) — the live working directory. Contains the database, imports, exports, outputs, backups, and all non-code assets.

### Directory layout

```
Bible_study_projects/          ← Google Drive root (working directory)
│
├── README.md                  ← This file
├── .gitignore
│
├── engine/                    ← Automation engine (Python package)
│   ├── __init__.py
│   ├── engine.py              ← CLI entry point
│   ├── constants.py           ← Shared constants and thresholds
│   ├── db.py                  ← Connection factory, schema version check
│   ├── migrate.py             ← Schema migration runner (M01–M11+)
│   ├── backup.py              ← Database backup utilities
│   ├── register.py            ← Word registration and lock management
│   ├── new_word.py            ← NEW_WORD mode — first-time term/verse fetch
│   ├── gap_fill.py            ← GAP_FILL mode — backfill missing data streams
│   ├── audit_word.py          ← AUDIT_WORD mode — data quality checks
│   ├── flag_engine.py         ← DATA_COVERAGE flag computation
│   ├── meaning_parser.py      ← Meaning block parser (wa_meaning_parsed/sense/stem)
│   ├── span_filter.py         ← Verse span-match filter
│   ├── report.py              ← Word overview report printer
│   ├── run_log.py             ← engine_run_log helpers
│   └── audit.py               ← Audit helper functions
│
├── analytics/                 ← Analytics utilities
│   ├── requirements.txt       ← Python dependencies
│   ├── bible_analytics.py     ← Legacy entry point (--init-db, --import-json, etc.)
│   ├── db_client.py           ← SQLite connection and schema init helpers
│   ├── step_client.py         ← STEP Bible API client
│   └── zotero_client.py       ← Zotero API client
│
├── scripts/                   ← Utility and maintenance scripts
│   ├── env_setup.ps1          ← Environment bootstrap (run once on new machine)
│   ├── word_full_extract.py   ← Full word data extract to CSV
│   ├── _apply_stem_patch.py   ← Apply meaning stem extraction patch
│   ├── _apply_phase2_flags_patch.py ← Apply phase-2 flag reassessment patch
│   ├── _assess_meaning_tables.py    ← Read-only meaning table diagnostic
│   ├── _realign_meaning_tables.py   ← Meaning re-alignment (one-off)
│   ├── _realign_quality_flags.py    ← Quality flag full reset and recompute
│   ├── _reset_registry_status.py    ← word_registry status correction
│   └── _integrity_full_check.py     ← Full DB integrity check
│
├── data/
│   ├── bible_research.db      ← SQLite database (NOT in Git)
│   ├── schema/
│   │   └── create_tables.sql  ← Full schema DDL (versioned)
│   ├── imports/
│   │   └── WA/
│   │       └── Patches/       ← Claude-produced JSON patch files
│   ├── exports/               ← Data exports for Claude and reporting
│   └── bible_research.db.bak_* ← Rolling backups (NOT in Git)
│
├── backups/                   ← Engine-managed database backups (NOT in Git)
│
├── docs/                      ← Project documentation and setup guides
│   ├── data_setup.md
│   ├── step_setup.md
│   ├── zotero_setup.md
│   └── file_organization.md
│
├── outputs/                   ← Research outputs
│   ├── markdown/
│   ├── docx/
│   ├── pdf/
│   └── word_reports/
│
├── research/                  ← Research notes, projects, templates
│   ├── projects/
│   ├── notes/
│   └── templates/
│
├── Logs/                      ← Session logs
└── archive/                   ← Archived scripts and docs
```

---

## 5. Environment Setup — New Machine

### Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.10+ (3.14 current) | Must be on PATH |
| PowerShell | 7+ | For env_setup.ps1 |
| Git | Any recent | For source control |
| Google Drive desktop | Current | Mounts the working directory |

### Step-by-step

```powershell
# 1. Clone the repository
git clone https://github.com/lcilliers/Bible_Projects.git
cd Bible_Projects

# 2. Bootstrap the environment (creates venv, installs dependencies, creates .env template)
.\scripts\env_setup.ps1

# 3. Restore the database
#    Copy bible_research.db from a backup or Google Drive into:
#    G:\My Drive\Bible_study_projects\data\bible_research.db

# 4. Verify schema and apply any pending migrations
python -m engine.engine --db-status
python -m engine.engine --migrate

# 5. Verify engine connectivity
python -m engine.engine --check-locks
```

### Python dependencies (analytics/requirements.txt)

```
pyzotero>=1.5.18          # Zotero API
pandas>=2.2.0             # Data manipulation
jsonschema>=4.23.0        # JSON validation
python-dotenv>=1.0.0      # .env file support
markdown>=3.6             # Markdown generation
requests>=2.32.0          # HTTP / API calls
python-docx>=1.1.2        # .docx output
reportlab>=4.2.0          # PDF output
```

Full install (system-wide or after activating the venv):
```powershell
pip install -r analytics\requirements.txt
```

### .env file

The bootstrap script creates `.env` from a template. Populate with:
```
ZOTERO_API_KEY=your_zotero_api_key
ZOTERO_USER_ID=your_zotero_user_id
STEP_BASE_URL=https://www.stepbible.org/api
```

---

## 6. Database Platform

**SQLite** (`data/bible_research.db`) — single-file, no server, full relational schema.

### Key facts

| Property | Value |
|----------|-------|
| Schema version | v3.1.0 |
| Total tables | 28 |
| Primary research table | `wa_verse_records` |
| Registry size | ~211 English words |
| Term inventory | ~1,529 Hebrew/Greek terms |
| Verse records | ~50,000+ rows |

### Database operations

```powershell
# Schema status
python -m engine.engine --db-status

# Apply migrations
python -m engine.engine --migrate

# Manual backup (label is appended to filename)
python -c "import engine.backup as b; b.manual_backup(label='my-label')"

# Integrity check
python scripts/_integrity_full_check.py
```

### Backup strategy

The engine manages backups automatically in `backups/`:
- **Pre-run backup** — taken before every engine run (rolling, keeps last 10)
- **Pre-migration backup** — taken before `--migrate`
- **Manual backup** — on demand via `b.manual_backup(label=...)`

Backup files are named: `bible_research_<type>_<YYYYMMDD>_<HHMMSS>_<label>.db`

---

## 7. Schema Reference

Schema DDL: [data/schema/create_tables.sql](data/schema/create_tables.sql)

### Table groups

| Section | Tables | Purpose |
|---------|--------|---------|
| 1 — Reference | `books`, `book_code_variants`, `themes`, `sources` | Static reference data (66 Bible books, code variants, etc.) |
| 2 — Registry | `word_registry` | Master list of ~211 English words under study |
| 3 — WA File Index | `wa_file_index` | One row per imported Session A JSON file; parent for all WA tables |
| 4 — WA Term Data | `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` | Per-term metadata: glosses, meaning text, occurrence counts, flags, root families |
| 5 — Phase-2 Flags | `phase2_flag_types`, `wa_term_phase2_flags` | Shared analytical flags (Hebrew stem types, semantic categories) |
| 6 — Quality Flags | `wa_quality_flag_types`, `wa_data_quality_flags` | DATA_COVERAGE, TERM_ANALYSIS, IMPORT_STATUS, NOTE flags per file/term |
| 7 — Cross-Registry | `wa_crosslink_type`, `wa_cross_registry_links` | Semantic links between word registry entries |
| 8 — Verse Records | `wa_verse_records` | **Core research table.** One row per term occurrence in a verse |
| 9 — MTI | `mti_terms`, `mti_term_flags`, `mti_term_cross_refs` | Mounce Term Index extracted terms and their flags/cross-refs |
| 10 — Engine Control | `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log` | Full audit trail for every engine run |
| 11 — Meaning Parsing | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | Structured parse of meaning blocks and LSJ lexicon entries |
| 12 — Metadata | `schema_version` | Current schema version and migration history |

### word_registry — status values

| `phase1_status` | Meaning |
|-----------------|---------|
| `Complete` | Session A data loaded; term inventory and verse records present |
| `In Progress` | Partially processed |
| `Excluded` | No usable data — excluded from engine runs |
| `Redundant` | Superseded by another registry entry |

### wa_data_quality_flags — flag groups

| Group | Codes | Purpose |
|-------|-------|---------|
| `DATA_COVERAGE` | THIN_DATA, SMALL_VERSE_SAMPLE, HIGH_FREQUENCY_ANCHOR, NO_VERSES, NO_WORD_ANALYSIS, SPAN_FILTER_APPLIED, SPAN_RESOLUTION_CONFLICT, ARAMAIC_EQUIVALENT | Data completeness and coverage indicators — computed by engine |
| `TERM_ANALYSIS` | SEMANTIC_RANGE_BREADTH, DIVINE_HUMAN_PARALLEL, CAUSATIVE_OF_INNER_STATE, METAPHOR_ROOT, GOD_AS_SUBJECT, VOLITIONAL_COMPONENT, RELATIONAL_DIRECTION, SOMATIC_INNER_LINK, WISDOM_LITERATURE_CONCENTRATION, GENERATION_RESOLUTION_PAIR, ESCHATOLOGICAL_USAGE, SOMATIC_EXPRESSION, BODY_INNER_EXPRESSION, MULTI_REGISTRY_ANCHOR, NT_FACULTY_NAMING, CROSS_TESTAMENT_SHIFT, ARAMAIC_FORM, THEOLOGICAL_ANCHOR | Semantic and analytical characterisation — set by Claude |
| `IMPORT_STATUS` | STRONGS_RECONCILED, OCCURRENCE_COUNT_MISMATCH, FORMAT_ERROR_IN_SOURCE, DUPLICATE_IN_SOURCE, DUPLICATE_RESOLVED, etc. | Import-time data quality notes |
| `NOTE` | NOTE, NOTE_ON_ROOT_FAMILY, ANOMALY_NOTE, SPAN_BACK_POPULATED | Researcher notes and alerts |

### Meaning parsing chain

```
wa_term_inventory.meaning (raw text)
        ↓  engine/meaning_parser.py
wa_meaning_parsed          (1 row per term — parse metadata)
        ├── wa_meaning_sense   (N rows per parsed term — hierarchical sense entries)
        └── wa_meaning_stem    (N rows per parsed term — Hebrew stem type summary)

wa_term_inventory.lsj_entry (Greek only — raw LSJ text)
        ↓  engine/meaning_parser.py
wa_lsj_parsed              (1 row per Greek term — structured LSJ fields)
```

---

## 8. The Automation Engine

The engine is a Python package at `engine/`. It is invoked as a module:

```powershell
python -m engine.engine [options]
```

### Engine modes

| Mode | Command | Purpose |
|------|---------|---------|
| **NEW_WORD** | `--mode=new_word --registry=N --terms=H0001,H0002` | First-time data load for a word: fetches terms and verse records from STEP API, runs span filter, parses meaning, computes quality flags |
| **GAP_FILL** | `--mode=gap_fill [--registry=N] [--streams=S1,S2]` | Backfills missing data streams for existing words (span match, meaning parse, flag compute, etc.) |
| **AUDIT_WORD** | `--mode=audit_word --registry=N` | Runs data quality checks on an existing word; can trigger span backpopulation |
| **MIGRATE** | `--migrate [--dry-run]` | Applies pending schema migrations |
| **REGISTER** | `--register --word="..." --source="..."` | Adds a new word to `word_registry` |
| **REPORT** | `--report --registry=N [--format=markdown]` | Prints a word overview report |

### Engine flags

```powershell
--dry-run          # Preview actions without writing to DB
--force            # Override lock checks
--skip-span-backpop # Skip span backpopulation in AUDIT_WORD
--streams=S1,S3    # Run only specified data streams in GAP_FILL
```

### Engine constants (engine/constants.py)

| Constant | Value | Purpose |
|----------|-------|---------|
| `EXPECTED_SCHEMA_VERSION` | `"3.1.0"` | Engine refuses to run against a mismatched schema |
| `ENGINE_VERSION` | `"1.0.0"` | Written to run logs |
| `PARSER_VERSION` | `"1.0.0"` | Written to `wa_meaning_parsed.parse_version` |
| `HIGH_FREQ_THRESHOLD` | 500 | Occurrence count above which HIGH_FREQUENCY_ANCHOR flag is raised |
| `THIN_DATA_THRESHOLD` | 20 | Occurrence count below which THIN_DATA flag is raised |
| `SMALL_VERSE_SAMPLE_THRESHOLD` | 5 | Confirmed verse count below which SMALL_VERSE_SAMPLE flag is raised |
| `BACKUP_RETENTION` | 10 | Number of pre-run backups to keep |
| `STALE_LOCK_SECONDS` | 7200 | Time after which an IN_PROGRESS lock is considered stale |

### Lock management

The engine uses `word_registry.last_automation_run = 'IN_PROGRESS'` as a run lock.

```powershell
python -m engine.engine --check-locks          # Show all active locks
python -m engine.engine --clear-lock --registry=42  # Clear a specific lock
```

---

## 9. Key Scripts and Operations

### Production scripts (reusable, safe to re-run)

| Script | Purpose | Safe to re-run? |
|--------|---------|-----------------|
| `scripts/_assess_meaning_tables.py` | Read-only diagnostic of all meaning tables — coverage, orphans, gaps | ✅ Yes |
| `scripts/_integrity_full_check.py` | Full DB integrity check — FK orphans, NULL mandatory fields, duplicates | ✅ Yes |
| `scripts/word_full_extract.py` | Export full word data to CSV | ✅ Yes |
| `scripts/_realign_meaning_tables.py` | One-off: re-parse all meaning blocks using engine's `run_parser()` | ⚠️ Modifies DB |
| `scripts/_realign_quality_flags.py` | Full reset of `wa_data_quality_flags`; recomputes DATA_COVERAGE via engine | ⚠️ Destructive — deletes all then recomputes |
| `scripts/_reset_registry_status.py` | Sets `word_registry.phase1_status` to Complete/Excluded based on data presence | ⚠️ Modifies DB |
| `scripts/_apply_stem_patch.py` | Applies a Claude-produced stem extraction JSON patch | ⚠️ Modifies DB |
| `scripts/_apply_phase2_flags_patch.py` | Applies a Claude-produced phase-2 flag reassessment JSON patch | ⚠️ Modifies DB |

### Common ad-hoc queries

```python
# DB connection pattern used in all scripts
import sqlite3, os
conn = sqlite3.connect(os.path.join('data', 'bible_research.db'))
conn.row_factory = sqlite3.Row
cur = conn.cursor()
```

```sql
-- Word registry status summary
SELECT phase1_status, COUNT(*) FROM word_registry GROUP BY phase1_status;

-- Quality flag distribution by group
SELECT qt.flag_group, qt.flag_code, COUNT(*) AS n
FROM wa_data_quality_flags dq
JOIN wa_quality_flag_types qt ON qt.id = dq.flag_id
GROUP BY qt.flag_group, qt.flag_code
ORDER BY qt.flag_group, n DESC;

-- Terms for a word
SELECT ti.strongs_number, ti.transliteration, ti.language, ti.occurrence_count
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
WHERE fi.word = 'peace';

-- Verse count per word
SELECT fi.word, COUNT(vr.id) AS verses
FROM wa_verse_records vr
JOIN wa_file_index fi ON fi.id = vr.file_id
GROUP BY fi.word
ORDER BY verses DESC;
```

---

## 10. Data Import / Patch Workflow

The project uses a **Claude → JSON patch → Python apply script** pattern for all bulk data operations that require AI analysis.

### Standard patch format

Claude produces a JSON file placed in `data/imports/WA/Patches/`. Each patch has:

```json
{
  "patch_id":    "descriptive-name-YYYYMMDD-v1",
  "produced_at": "2026-03-19T17:51:31Z",
  "description": "What this patch does",
  "summary":     { ... counts of changes ... },
  "<section>":   [ { ... row objects ... } ]
}
```

### Naming convention

`data/imports/WA/Patches/<description>-<YYYYMMDD>-v<N>.json`

Examples:
- `stem-extraction-patch-20260319-v1.json`
- `phase2-flag-reassessment-20260319-v1.json`

### Apply pattern

All apply scripts follow this pattern:
1. Load the patch JSON
2. Build DB lookups (IDs, FKs)
3. Execute inserts/updates/deletes
4. Print verification counts
5. `conn.commit()`

Scripts always resolve FKs by **code/name lookups** against the live DB, never by trusting patch-internal integer IDs.

---

## 11. External API Integrations

### STEP Bible API

Used by the engine to fetch verse records and term data.

- **Client:** `analytics/step_client.py`
- **Setup guide:** [`docs/step_setup.md`](docs/step_setup.md)
- **Base URL:** `https://www.stepbible.org/api`
- **Usage:** Called automatically by `engine/new_word.py` during NEW_WORD runs

### Zotero API

Used for reference management and source tracking.

- **Client:** `analytics/zotero_client.py`
- **Setup guide:** [`docs/zotero_setup.md`](docs/zotero_setup.md)
- **Requires:** `ZOTERO_API_KEY` and `ZOTERO_USER_ID` in `.env`

---

## 12. Project Rules and Conventions

### Data conventions

- **Strongs numbers:** `H` prefix = Hebrew, `G` prefix = Greek. Suffix letters (e.g. `H7965H`, `G0026B`) indicate sub-entries. `NO STRONG` = term identified but Strongs not yet confirmed.
- **Language values:** Always `"Hebrew"` or `"Greek"` (full word, capitalised).
- **Dates:** ISO-8601 format: `2026-03-19T18:08:49Z` (UTC, Z suffix).
- **Boolean fields in SQLite:** `INTEGER` columns — `1` = true, `0` = false.
- **term_id vs strongs_number:** `term_id` is the STEP internal code; `strongs_number` is the canonical Strong's reference (may differ for sub-entries). Always use `strongs_number` for cross-table joins.

### Engine rules

- Never run engine modes against a schema version mismatch — always `--migrate` first.
- Always run `--db-status` before a batch engine run.
- Prefer `--dry-run` to preview before committing bulk operations.
- Do not manually edit `wa_verse_records` or `wa_term_inventory` — use engine modes or patch scripts.

### Script conventions

- Diagnostic scripts are prefixed `_assess_` or `_check_` — read-only, safe to run anytime.
- Modification scripts are prefixed `_apply_`, `_fix_`, `_realign_`, or `_reset_` — always review before running.
- All scripts run from the project root (`G:\My Drive\Bible_study_projects`).
- Set `$env:PYTHONUTF8="1"` when running scripts in PowerShell to ensure correct encoding.

### Git conventions

- `data/bible_research.db` is excluded from Git (`.gitignore`).
- `backups/` is excluded from Git.
- Patch JSON files in `data/imports/WA/Patches/` **are** committed (they are the input record).
- Commit message format: `session YYYYMMDD: brief description\n\n- bullet list of changes`

### Working with Claude

Claude.ai is used for:
- Producing Session A JSON files (term and verse data for a word)
- Producing patch files (meaning analysis, flag assessment, stem extraction)
- Analysis, synthesis, and writing

All Claude-produced data must be validated by a Python apply script before entering the DB — never import raw Claude output directly.

---

*Last updated: 2026-03-20 | Schema v3.1.0 | Engine v1.0.0*

## Objective

To serve as the repository for application development and AI interaction to support deep Bible and other research projects centred on the Bible. The aim is to produce **stunning, insightful, well-grounded, and comprehensive research results**.

---

## Roles and Participants

| Role | Participant | Responsibility |
|------|-------------|----------------|
| **Researcher** | le Roux Cilliers (leRoux) | Ultimate authority. Sets objectives, working methods, subject matter, scope, and evaluates outputs. This is leRoux's research — all other participants support his endeavours. |
| **Coding & Development** | GitHub Copilot | Primary AI tool for coding and development assistance. |
| **Thinker & Writer** | Claude.ai | Primary AI tool for analysis, synthesis, and articulation. |

---

## Toolchain

| Tool | Purpose |
|------|---------|
| **Visual Studio** | Project interface, coding and application development platform |
| **Zotero** | File storage and reference management (API setup required — see [`docs/zotero_setup.md`](docs/zotero_setup.md)) |
| **STEP Bible** | Scripture search and cross-referencing for `Bible_verse_analytics` (see [`docs/step_setup.md`](docs/step_setup.md)) |
| **Obsidian** | Writing and note-taking (value still being evaluated) |
| **Google Docs / Google Drive** | Project file management and large-file storage (`G:\My Drive\Bible_study_projects` — see [`docs/file_organization.md`](docs/file_organization.md)) |
| **PowerShell** | File handling and environment scripting |
| **Python** | Analytics and data processing |
| **SQLite** | Structured research data — multi-table, JSON import/export workflow (see [`docs/data_setup.md`](docs/data_setup.md)) |
| **Git + GitHub** | Source control (`lcilliers/Bible_projects`) |

---

## Repository Structure

```
Bible_Projects/
├── README.md                  # This file — project overview
├── .gitignore                 # Files and folders excluded from source control
│
├── research/                  # Research notes, source summaries, working documents
│   ├── projects/              # One .md brief per research project
│   ├── notes/                 # Working notes, cross-references, exegesis
│   └── templates/             # Reusable templates (research note, Claude session, project brief)
│
├── docs/                      # Project documentation and setup guides
│   ├── file_organization.md   # Two-tier storage guide (Git + Google Drive)
│   ├── zotero_setup.md        # Zotero API integration guide
│   ├── step_setup.md          # STEP Bible API integration guide
│   └── data_setup.md          # SQLite data platform guide
│
├── data/                      # Structured data files
│   ├── bible_research.db      # SQLite database (excluded from Git)
│   ├── schema/                # SQL schema definitions (versioned)
│   │   └── create_tables.sql
│   ├── imports/               # JSON files from Claude staged for import
│   └── exports/               # JSON / CSV exports produced for Claude
│
├── outputs/                   # Research outputs by file type
│   ├── markdown/              # General output (.md)
│   ├── docx/                  # External consumption (.docx)
│   └── pdf/                   # Final products (.pdf)
│
├── scripts/                   # PowerShell and utility scripts
│   └── env_setup.ps1          # Environment bootstrap script
│
└── analytics/                 # Python analytics and data processing
    ├── requirements.txt       # Python dependencies
    ├── bible_analytics.py     # Main analytics entry point
    ├── db_client.py           # SQLite database client
    ├── zotero_client.py       # Zotero API client wrapper
    └── step_client.py         # STEP Bible API client wrapper
```

---

## Output File Types

| Type | Format | Purpose |
|------|--------|---------|
| General output | `.md` (Markdown) | Working notes, research summaries, internal documents |
| External consumption | `.docx` | Documents formatted for sharing externally |
| Final products | `.pdf` | Polished, publishable research outputs |
| Interim structured data | `.json` / `.csv` | Data lists, concordances, structured research artefacts |

---

## Getting Started

### Prerequisites

- **Python 3.10+** — for analytics scripts
- **PowerShell 7+** — for environment and file management scripts
- **Git** — for source control

### Environment Setup

```powershell
# Run the environment setup script from the project root
.\scripts\env_setup.ps1
```

### Python Analytics Setup

```bash
cd analytics
pip install -r requirements.txt
python bible_analytics.py
```

### Zotero API

See [`docs/zotero_setup.md`](docs/zotero_setup.md) for step-by-step instructions on configuring the Zotero API for reference management integration.

### STEP Bible API

See [`docs/step_setup.md`](docs/step_setup.md) for step-by-step instructions on configuring access to [STEP Bible](https://www.stepbible.org/) for scripture search and verse analytics.

### SQLite Data Platform

See [`docs/data_setup.md`](docs/data_setup.md) for the data platform decision, schema design, and the JSON → SQLite import workflow used to add new research records from Claude.

### File Organisation

See [`docs/file_organization.md`](docs/file_organization.md) for the complete two-tier storage model (Git vs Google Drive), naming conventions, what-goes-where reference, and how to migrate existing unorganised materials from `Claude_Research` into the structured layout.

---

## Bible_verse_analytics : STEP Integration

The `Bible_verse_analytics` module integrates with **[STEP Bible](https://www.stepbible.org/)** (Scripture Tools for Every Person), a free, open-access Bible study platform developed by Tyndale House, Cambridge. STEP provides:

- Access to a wide range of Bible translations, original language texts (Hebrew, Greek), and interlinears
- Morphological analysis, lexicon lookups, and cross-references
- A public web API for programmatic scripture search and passage retrieval

### What this integration enables

| Capability | Description |
|------------|-------------|
| **Verse lookup** | Retrieve individual verses or passages by reference (e.g. `John 3:16`) |
| **Multi-translation comparison** | Compare verses across translations (ESV, NIV, KJV, NASB, etc.) |
| **Original language access** | Pull Hebrew (OT) and Greek (NT) texts with morphological tagging |
| **Keyword / concordance search** | Search across the entire Bible for words or phrases |
| **Cross-reference retrieval** | Fetch related passages and thematic links |

Retrieved data flows directly into the research pipeline: stored in `data/`, processed via the Python analytics scripts in `analytics/`, and published to `outputs/`.

### Quick start

```bash
# Test STEP Bible API connectivity
python analytics/bible_analytics.py --test-step
```

For full configuration instructions, see **[`docs/step_setup.md`](docs/step_setup.md)**.

---

## Structured Data Platform : SQLite

After evaluating SQL, pure JSON, and SQLite, **SQLite** is the chosen data platform for this project. It requires no server, stores the entire database in a single portable file (`data/bible_research.db`), and handles the expected scale (~20 000 rows in the main `verse_notes` table) with ease.

### Why SQLite

| Requirement | SQLite |
|-------------|--------|
| Multi-table, relational schema | ✓ |
| ~20 000 rows (main table) | ✓ — trivially fast |
| No server / no install required | ✓ — single `.db` file |
| Python built-in support | ✓ — `sqlite3` stdlib |
| JSON import from Claude | ✓ — one-command batch insert |
| JSON export for Claude to read | ✓ — one-command export |

### Claude → SQLite workflow

```
Claude outputs structured JSON (list of records)
            ↓
Save to  data/imports/<batch_name>.json
            ↓
python analytics/bible_analytics.py --import-json data/imports/<batch>.json --table verse_notes
            ↓
Records inserted into bible_research.db
```

### Quick commands

```bash
python analytics/bible_analytics.py --init-db                                         # Create schema
python analytics/bible_analytics.py --test-db                                         # Verify setup
python analytics/bible_analytics.py --import-json data/imports/batch.json --table verse_notes
python analytics/bible_analytics.py --export-json verse_notes                         # Export for Claude
```

See **[`docs/data_setup.md`](docs/data_setup.md)** for full setup, schema reference, and import/export examples.

---

## Contributing

This is leRoux's personal research project. Contributions are made through the defined toolchain above. All outputs are reviewed and approved by leRoux as the ultimate authority on scope, methodology, and quality.
