# File Organisation Rules — Framework B

> Governs where Claude Code and the researcher place files.
> Created 2026-03-30. Updated 2026-04-14: naming conventions (Section 2), manifest system (Section 6), stale doc policy (Section 3.2).
> Read by Claude Code at session start via CLAUDE.md reference.

---

## 1. Principle

Every file has one correct location determined by its **type** and **lifecycle stage**. Files must not accumulate in folder roots when a subfolder exists for their type. Old versions are archived, not left alongside current versions.

---

## 2. Naming Conventions

### 2.1 Core Rules

All non-code files produced by or for the programme follow these rules:

| Rule | Standard | Example |
|------|----------|---------|
| **Case** | All lowercase | `wa-068-grace-sessionb-observations-v5-20260410.md` |
| **Separators** | Hyphens (`-`) between tokens | `wa-dim-c17-session-log-v1-20260413.md` |
| **Date format** | Compact `YYYYMMDD` | `20260414` (not `2026-04-14`) |
| **Version** | `-v{n}` suffix before date, integer, no leading zero | `-v1-`, `-v12-` |
| **Registry number** | Zero-padded to 3 digits | `023`, `068`, `214` |
| **No spaces** | Never in filenames | Use hyphens |

### 2.2 Standard Naming Patterns

Files are named to sort naturally by registry number within a folder, making it easy to find all files for a given word.

#### Session B Analysis

```
wa-{NNN}-{word}-sessionb-{type}-v{n}-{YYYYMMDD}.{ext}

Types: observations, brief, log, cc-directive
Examples:
  wa-068-grace-sessionb-observations-v5-20260410.md
  wa-068-grace-sessionb-log-v2-20260410.md
  wa-068-grace-sessionb-cc-directive-v1-20260410.md
  wa-068-grace-sessionb-brief-v1-20260410.md
```

#### Session C Word Studies

```
wa-{NNN}-{word}-sessionc-{type}-v{n}-{YYYYMMDD}.{ext}

Types: word-study, log, note, analysis-report
Examples:
  wa-064-forgiveness-sessionc-word-study-v3-20260412.md
  wa-103-love-sessionc-log-v1-20260412.md
```

#### Session D Synthesis

```
wa-{NNN}-{word}-sessiond-{type}-v{n}-{YYYYMMDD}.{ext}

Types: pointers, synthesis, note
```

#### Verse Context

```
wa-vcb-{NNN}-{type}-v{n}-{YYYYMMDD}.{ext}

Types: term-observations, session-log, sessionb-flags, patch-log
Examples:
  wa-vcb-034-term-observations-v1-20260412.md
  wa-vcb-034-session-log-v1-20260412.md
```

#### Dimension Review

```
wa-dim-{cluster}-{type}-v{n}-{YYYYMMDD}.{ext}
wa-dim-{cluster}-{scope}-{type}-v{n}-{YYYYMMDD}.{ext}

Types: observations, session-log, patch (for JSON)
Scope (optional): reg{NNN} for registry-specific files
Examples:
  wa-dim-c17-observations-v1-20260413.md
  wa-dim-c17-session-log-v1-20260413.md
  wa-dim-c17-reg068-patch-v1-20260410.json
```

#### Patches (JSON)

```
patch-{YYYYMMDD}-{NNN}-{type}-v{n}.json

Types: preanalysis, analysis, sessionb, sessionb-complete, versecontext,
       vcgroup, vcverse, repair-{scenario}, sessiond, clustering,
       sdenrich, sdpointers, dimcorrect, dimreview
Examples:
  patch-20260412-068-sdenrich-v1.json
  patch-20260412-103-analysis-v1.json
  patch-20260413-vcb037-versecontext-v1.json
  patch-20260413-dimreview-c17-reg062-v1.json
```

#### Directives (Markdown — unstructured AI instructions)

```
cc-directive-{NNN}-{seq}-{YYYYMMDD}.md

Examples:
  cc-directive-062-001-20260413.md
  cc-directive-062-002-20260413.md
```

#### Exports

```
# STEP Extracts (engine export)
{word}_{reg}_{scope}_{YYYYMMDD}_v{n}.json
  contrition_30_full_20260413_v1.json

# Session C complete extracts
wa-{NNN}-{word}-{scope}-{YYYYMMDD}-v{n}.json
  wa-068-grace-complete-20260413-v1.json
  wa-068-grace-owner_only-20260413-v1.json

# Verse Context batch extracts
wa-vcb-{NNN}-extract-{YYYYMMDD}.json

# Dimension review extracts
wa-dim-{cluster}-{type}-{YYYYMMDD}.json
  wa-dim-c17-extract-20260413.json
  wa-dim-c17-rootfamily-20260413.json
  wa-dim-c17-existing-pointers-20260413.json

# Session D pointers
wa-{NNN}-{word}-sdpointers-{YYYYMMDD}.json

# Pool analysis
wa-pool-{pool_id}-analysis-{YYYYMMDD}.json
```

#### Discovery

```
{NNN}_{word}_step_data_{YYYYMMDD}.{json|md}
  030_contrition_step_data_20260413.json
```

#### Programme Reports

```
wa-programme-{type}-{YYYYMMDD}.{ext}
  wa-programme-status-report-20260414.md
  wa-programme-registry-overview-20260414.json

database-schema-{YYYYMMDD}.json
```

#### Workflow / Governing Documents

```
WA-{DocumentName}-v{major}_{minor}-{YYYYMMDD}.md

Current versions live in the Session_B/ folder. Superseded versions go to Session_B/archive/.
Examples:
  WA-SessionB-Instruction-v4_7-20260412.md
  WA-Registry-Management-Guide-v5_8-20260412.md
```

> **Note:** Governing documents retain their established `WA-` uppercase prefix for continuity. All other files use lowercase `wa-`.

#### Session Logs (Workflow)

```
wa-session-log-{YYYYMMDD}-{topic}.md
  wa-session-log-20260412-programme-docs-update.md
```

### 2.3 Version Control via Filename

Date-stamping and version numbering serve as the version control mechanism for non-code files:

- **Same-day revisions:** Increment the version number: `v1`, `v2`, `v3`
- **New-day revision:** New date, version resets to `v1`
- **Archiving:** Only the **latest version** of a file remains in its active folder. All prior versions (whether by date or version number) move to the `archive/` subfolder within that directory. Git history preserves the full lineage.
- **No duplicates:** Two files that differ only by date or version number are the same logical document. Treat them identically for archiving purposes.

### 2.4 Sort-Friendly Design

The naming patterns above are designed so that `ls` or file explorer sorting groups related files together:

- **By registry:** `wa-023-*`, `wa-064-*`, `wa-068-*` — zero-padded 3-digit registry sorts numerically
- **By batch:** `wa-vcb-034-*`, `wa-vcb-035-*` — sequential batch numbers
- **By cluster:** `wa-dim-c13-*`, `wa-dim-c17-*` — cluster codes sort together
- **By type within a word:** `wa-068-grace-sessionb-brief-*`, `wa-068-grace-sessionb-log-*`, `wa-068-grace-sessionb-observations-*`

---

## 3. Folder Rules

### 3.1 `data/exports/`

Programme data exported from the database for consumption by Claude AI or the researcher.

| Subfolder | What goes here | Naming pattern |
|-----------|---------------|----------------|
| `data/exports/` (root) | Only subfolders — no files in root |  |
| `Sessions/Session_A/STEP Extracts/` | Full word JSON exports from engine | `{word}_{reg}_{scope}_{YYYYMMDD}_v{n}.json` |
| `Sessions/Session_B/01_Verse_Context_Process_input/` | Verse Context batch extracts | `wa-vcb-{NNN}-extract-{YYYYMMDD}.json` |
| `Sessions/Session_B/04_dimension_review_process input/` | Dimension Review extracts (cluster, root family, group verification, existing pointers) | `wa-dim-{cluster}-{type}-{YYYYMMDD}.json` |
| `Sessions/Session_B/04_dimension_review_process input/directives/` | Pending CC directives from Claude AI. Processed directives move to `directives/archive/`. | `wa-dim-{ref}-cc-directive-{scope}-v{n}-{YYYYMMDD}.md` |
| `Sessions/Session_B/04_dimension_review_process input/directives/archive/` | Processed directives (moved after execution) | |
| `data/exports/vertical_pass/` | Vertical Pass experiment and analysis extracts | `wa-verticalpass-{scope}-{YYYYMMDD}.json` |
| `data/exports/Session C/` | Comprehensive word extracts (complete and owner-only) | `wa-{NNN}-{word}-{scope}-{YYYYMMDD}-v{n}.json` |
| `Sessions/Session_D/session_d/` | Session D pointers files | `wa-{NNN}-{word}-sdpointers-{YYYYMMDD}.json` |
| `data/exports/pool_analysis/` | Pool analysis datasets | `wa-pool-{pool_id}-analysis-{YYYYMMDD}.json` |

**Archiving:** When a new version of an export is produced on the same day (v2, v3), prior versions are retained (auto-versioned). When a new day's export supersedes a prior day's, the prior day's file is moved to `data/exports/archive/`.

### 3.2 `Sessions/Patches/`

All patch files received from Claude AI. Two categories:

| Type | Description | Format |
|------|-------------|--------|
| **Patches** | Structured JSON instructions for the applicator | `patch-{YYYYMMDD}-{NNN}-{type}-v{n}.json` |
| **Directives** | Unstructured markdown instructions for Claude Code | `cc-directive-{NNN}-{seq}-{YYYYMMDD}.md` |

Applied patches and executed directives are moved to `archive/patches/` by the applicator or Claude Code.

### 3.3 `Sessions/Session_B/09_Analysis_output_logs/`

Claude AI session outputs from Session B analytical work.

| What goes here | Naming pattern |
|---------------|----------------|
| Observations | `wa-{NNN}-{word}-sessionb-observations-v{n}-{YYYYMMDD}.md` |
| Session briefs | `wa-{NNN}-{word}-sessionb-brief-v{n}-{YYYYMMDD}.md` |
| Session logs | `wa-{NNN}-{word}-sessionb-log-v{n}-{YYYYMMDD}.md` |
| CC directives | `wa-{NNN}-{word}-sessionb-cc-directive-v{n}-{YYYYMMDD}.md` |

**Not here:** Session C notes (→ `Session_C_Words/`), dimension review files (→ `Session_B_Dimension_Review/`).

### 3.4 `Sessions/Session_B/02_Verse_Context_logs/`

Claude AI session outputs from Verse Context classification work.

| What goes here | Naming pattern |
|---------------|----------------|
| Term observations | `wa-vcb-{NNN}-term-observations-v{n}-{YYYYMMDD}.md` |
| Session logs | `wa-vcb-{NNN}-session-log-v{n}-{YYYYMMDD}.md` |
| Session B flags | `wa-vcb-{NNN}-sessionb-flags-v{n}-{YYYYMMDD}.md` |
| Patch logs | `wa-vcb-{NNN}-patch-log-v{n}-{YYYYMMDD}.md` |

**Not here:** Dimension review files (→ `Session_B_Dimension_Review/`).

### 3.5 `Sessions/Session_B/05_Dimension_Review_logs/`

Claude AI session outputs from Dimension Review work.

| What goes here | Naming pattern |
|---------------|----------------|
| Cluster observations | `wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md` |
| Session logs | `wa-dim-{cluster}-session-log-v{n}-{YYYYMMDD}.md` |
| Registry-specific patches | `wa-dim-{cluster}-reg{NNN}-patch-v{n}-{YYYYMMDD}.json` |

### 3.6 `Sessions/Session_C/Session_C_Words/`

Claude AI Session C word study outputs.

| What goes here | Naming pattern |
|---------------|----------------|
| Word studies | `wa-{NNN}-{word}-sessionc-word-study-v{n}-{YYYYMMDD}.md` |
| Session logs | `wa-{NNN}-{word}-sessionc-log-v{n}-{YYYYMMDD}.md` |
| Session C notes | `wa-{NNN}-{word}-sessionc-note-v{n}-{YYYYMMDD}.md` |
| Analysis reports | `wa-sessionc-analysis-report-v{n}-{YYYYMMDD}.md` |

### 3.7 `data/imports/WA/Workflow/Framework_B/Session_B/`

Governing instruction documents. Only the **current version** lives here. Superseded versions go to the `archive/` subfolder within Session_B.

### 3.8 `research/discovery/`

STEP API discovery output. Paired JSON + markdown files per word. No archiving needed — these are source data.

### 3.9 `data/schema/`

Authoritative DDL and schema-related reports.

| What goes here | Naming pattern |
|---------------|----------------|
| DDL | `create_tables.sql` |
| Schema snapshots | `database-schema-{YYYYMMDD}.json` |

---

### 3.10 `outputs/`

All analysis outputs, reports, and investigation artefacts produced by Claude Code or the researcher.

| Subfolder | What goes here | Naming pattern |
|-----------|---------------|----------------|
| `Workflow/Programme/Program_reports/` | Programme status reports, periodic reviews, registry overviews, word registry exports | `wa-programme-status-report-{YYYYMMDD}.md`, `wa-programme-registry-overview-{YYYYMMDD}.json`, `word_registry.json` |
| `Sessions/Session_B/09_Analysis_output_logs/words/` | Per-word reports — Verse Context reports, engine run reports, word extracts | `vc-report-{NNN}-{word}-{YYYYMMDD}.docx`, `{word}_{reg}_report_{YYYYMMDD}.md` |
| `research/investigations/` | Ad-hoc data investigations, CSV dumps, dedup plans, instruction gap analyses, assessments | `{topic}-{YYYYMMDD}.{ext}` |
| `outputs/docx/` | Word documents for external consumption | `{WORD}-full-extract-{YYYYMMDD}.docx` |
| `outputs/pdf/` | Final publishable products | |
| `outputs/archive/` | Superseded outputs (audit diffs, old reports) | Moved here when superseded |

**Rule:** Nothing goes in `outputs/` root. Every file goes in the appropriate subfolder.

---

### 3.11 `docs/`

Project documentation — architecture specs, setup guides, design decisions. These are **reference documents**, not session outputs.

| What goes here | Examples |
|---------------|---------|
| Architecture specifications | `Session-A-v9-Architecture-*.md` |
| Setup guides | `data_setup.md`, `step_setup.md`, `zotero_setup.md` |
| Design decisions | `pipeline_design_review_*.md`, `pipeline_decisions_*.md` |
| Data flow mapping | `field-data-flow-mapping.md` |
| Interaction preferences | `interaction-preferences.md` |
| File organisation rules | This file |

**Not here:** Session logs, status reports, investigation outputs, instruction documents, one-off audit results.

---

### 3.12 `Logs/`

Session logs — timestamped records of what happened in each working session. Logs are **topic-related** and crucial for maintaining topical information access.

| What goes here | Naming pattern |
|---------------|----------------|
| Programme session logs | `wa-session-log-{YYYYMMDD}-{topic}.md` |
| Pipeline status reviews | `wa-pipeline-status-review-v{n}-{YYYYMMDD}.md` |

**Filing:** Logs should be filed to the appropriate topical folder where possible:
- VC batch logs → `Session_B_Verse_Context/`
- Session B analysis logs → `Session_B_Analysis/`
- Dimension review logs → `Session_B_Dimension_Review/`
- Programme-level logs → `Logs/` or `Workflow/Sessionlogs/`

**Archiving:** Old session logs stay in their folder (they are historical records). Only move to `archive/Logs/` if explicitly superseded or no longer topically relevant.

---

### 3.13 `scripts/`

Utility and maintenance scripts. Active scripts only.

| What goes here | Naming convention |
|---------------|-------------------|
| Active utility scripts | `_assess_*.py`, `_check_*.py`, `_apply_*.py`, `_repair_*.py`, etc. |
| Batch construction | `_build_vc_batch.py` |
| Report generation | `_generate_programme_report.py` |
| One-off applicators | `apply_session_patch.py` |

**Rule:** `_tmp_*.py` scripts must be deleted or moved to `archive/scripts/` at end of session. One-off investigation scripts (`_check_*`, `_probe_*`) that have served their purpose should be archived promptly.

---

### 3.14 `archive/`

Superseded and retired artefacts. Organised by type. **Archive is not dead** — these files remain accessible and indexed in the file manifest.

| Subfolder | What goes here |
|-----------|---------------|
| `archive/scripts/` | Retired `_tmp_*`, one-off `_check_*`/`_probe_*`, and old utility scripts |
| `archive/patches/` | Applied patch files and executed directives (moved after processing) |
| `archive/Logs/` | Old session logs if superseded or no longer topically relevant |
| `archive/docs/` | Old documentation versions, superseded reference docs |

---

### 3.15 Other directories

| Directory | Purpose | Rules |
|-----------|---------|-------|
| `backups/` | Engine-managed database backups. Not in Git. Rolling 10. | Managed by `engine/backup.py` |
| `engine/` | Core Python automation engine modules only | No outputs, no data |
| `analytics/` | Python library: API clients and DB utilities | No outputs |
| `research/` | Research notes and templates (placeholder) | Available for researcher use |

---

## 4. Archiving Rules

| Trigger | Action |
|---------|--------|
| New version of a file produced (same day) | Move prior version to `archive/` subfolder within the file's directory |
| New day's version of a file produced | Move prior day's version to `archive/` subfolder (same-day versions already archived) |
| New version of an instruction document | Move prior version to the `archive/` subfolder within the instruction's directory |
| Patch applied successfully | Applicator moves patch to `archive/patches/` |
| Directive executed | Claude Code moves directive to `archive/patches/` |
| `_tmp_*.py` script no longer needed | Move to `archive/scripts/` or delete |
| One-off `_check_*`/`_probe_*` investigation complete | Move to `archive/scripts/` |
| New day's word export produced | Prior day's export to `data/exports/archive/` |
| Document identified as stale | Move to `archive/docs/`. Can be reinstated via manifest lookup. |

### 4.1 Stale Document Policy

Documents that are outdated but contain valuable content are archived, not deleted. The file manifest indexes all archived files, making them discoverable. If a stale document needs to be renewed:

1. Locate it via the manifest (`python scripts/build_file_manifest.py --search "topic"`)
2. Move it back to its active location
3. Update its content and version
4. Re-run the manifest

---

## 5. Claude Code Obligations

1. **Before writing any file:** determine the correct subfolder from this document.
2. **After completing an investigation:** move `_tmp_*.py` scripts to `archive/scripts/`.
3. **After producing a new report version:** move the prior version to `outputs/archive/`.
4. **Never place files in a folder root** when a subfolder exists for that file type.
5. **Reference this document** when uncertain about file placement.
6. **Maintain the file manifest** — run `python scripts/build_file_manifest.py` after processing a session log or when files are created/moved/archived.
7. **Archive superseded versions** — when producing a new version, move the prior version(s) to the appropriate archive subfolder.

---

## 6. File Manifest

The project maintains a machine-readable file manifest at `database/file_manifest.json`. This indexes every non-code file in the project (including archived files) with structured metadata.

### 6.1 Purpose

- **Programmatic lookup:** Find the latest version of any file by word, registry, or type
- **Stale file detection:** Identify superseded files that haven't been archived
- **Cross-reference:** All files related to a registry, cluster, or batch
- **Archive access:** Archived files are indexed and discoverable, not lost

### 6.2 Generation

```bash
# Full rebuild (on demand)
python scripts/build_file_manifest.py

# Search the manifest
python scripts/build_file_manifest.py --search "grace"
python scripts/build_file_manifest.py --search "registry:068"
python scripts/build_file_manifest.py --search "type:observations"
```

### 6.3 When to Update

- After processing a session log
- After any batch of file moves or archiving
- On demand when needed for lookup
- At session end as part of cleanup

### 6.4 Manifest Structure

Each entry contains:

| Field | Description |
|-------|-------------|
| `path` | Relative path from project root |
| `category` | Top-level category (import, export, patch, directive, report, investigation, log, doc, script, discovery) |
| `type` | Specific file type (observations, session-log, word-study, patch, extract, etc.) |
| `registry` | Registry number if applicable (null otherwise) |
| `word` | Word name if applicable |
| `cluster` | Cluster code if applicable |
| `batch` | VCB batch number if applicable |
| `version` | Version number extracted from filename |
| `date` | Date extracted from filename (YYYY-MM-DD normalised) |
| `ext` | File extension |
| `archived` | Boolean — whether the file is in an archive location |
| `size_bytes` | File size |
| `modified` | Last modified timestamp |

---

*Created 2026-03-30. Updated 2026-04-14 with naming conventions, manifest system, stale doc policy.*
