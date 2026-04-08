# File Organisation Rules — Framework B

> Governs where Claude Code and the researcher place files.
> Created 2026-03-30. Read by Claude Code at session start via CLAUDE.md reference.

---

## 1. Principle

Every file has one correct location determined by its **type** and **lifecycle stage**. Files must not accumulate in folder roots when a subfolder exists for their type. Old versions are archived, not left alongside current versions.

---

## 2. Folder Rules

### `data/exports/`

Programme data exported from the database for consumption by Claude AI or the researcher.

| Subfolder | What goes here | Naming pattern |
|-----------|---------------|----------------|
| `data/exports/` (root) | Only subfolders — no files in root |  |
| `data/exports/STEP Extracts/` | Full word JSON exports from engine | `{word}_{reg}_full_{date}_v{n}.json` |
| `data/exports/verse_context/` | Verse Context batch extracts | `wa-vcb-{nnn}-extract-{date}.json` |
| `data/exports/dimension_review/` | Dimension Review extracts (cluster, group verification, existing pointers) | `wa-dim-extract-{cluster}-{date}.json`, `wa-dim-grpverify-{group_code}-{date}.json`, `wa-dim-existing-pointers-{cluster}-{date}.json` |
| `data/exports/dimension_review/directives/` | Pending CC directives from Claude AI. Processed directives move to `directives/archive/`. | `wa-dim-cc-directive-{scope}-v{n}-{date}.md` |
| `data/exports/dimension_review/directives/archive/` | Processed directives (moved after execution) | |
| `data/exports/vertical_pass/` | Vertical Pass experiment and analysis extracts | `wa-verticalpass-{scope}-{date}.json` |
| `data/exports/vertical_pass/directives/` | Pending CC directives. Processed directives move to `directives/archive/`. | `WA-VerticalPass-{scope}-v{n}-{date}.md` |
| `data/exports/vertical_pass/directives/archive/` | Processed directives (moved after execution) | |
| `data/exports/session_d/` | Session D pointers files | `wa-{nnn}-{word}-sdpointers-{date}.json` |
| `data/exports/pool_analysis/` | Pool analysis datasets | `wa-pool-{pool_id}-analysis-{date}.json` |

**Archiving:** When a new version of an export is produced on the same day (v2, v3), prior versions are retained (auto-versioned). When a new day's export supersedes a prior day's, the prior day's file is moved to `data/exports/archive/`.

### `data/imports/WA/Patches/`

All patch files received from Claude AI. Applied patches are moved to `archive/patches/` by the applicator.

| What goes here | Naming pattern |
|---------------|----------------|
| Pending patches | `wa-{nnn}-{word}-patch-{date}.json`, `wa-vcb-{nnn}-patch-{date}.json`, `wa-dim-patch-{cluster}-v{n}-{date}.json`, `wa-dim-grpdesc-patch-{reg}-v{n}-{date}.json` |

### `data/imports/WA/Session_B_Dimension_Review/`

Claude AI session outputs from Dimension Review work.

| What goes here | Naming pattern |
|---------------|----------------|
| Cluster review assessments | `wa-dim-cluster-review-{cluster}-v{n}-{date}.md` |
| Dimension refinement logs | `wa-dim-refinement-log-v{n}-{date}.md` |
| Session logs | `wa-dim-session-log-{scope}-v{n}-{date}.md` |

### `data/imports/WA/vertical_pass/`

Claude AI session outputs from Vertical Pass work.

| What goes here | Naming pattern |
|---------------|----------------|
| Session logs | `wa-verticalpass-session-log-{scope}-v{n}-{date}.md` |
| Patches | `wa-verticalpass-patch-{scope}-v{n}-{date}.json` |
| Analysis outputs | `wa-verticalpass-{scope}-v{n}-{date}.md` |

### `data/imports/WA/Workflow/Frameword_B/Session_B/`

Governing instruction documents. Only the **current version** lives here. Superseded versions go to the `archive/` subfolder within Session_B.

### `data/discovery/`

STEP API discovery output. Paired JSON + markdown files per word. No archiving needed — these are source data.

### `data/schema/`

Authoritative DDL. Only `create_tables.sql` (kept current with schema).

---

### `outputs/`

All analysis outputs, reports, and investigation artefacts produced by Claude Code or the researcher.

| Subfolder | What goes here | Naming pattern |
|-----------|---------------|----------------|
| `outputs/reports/programme/` | Programme status reports, periodic reviews, database schema reports, registry overviews, word registry exports | `wa-programme-status-report-{date}.md`, `database_schema_{date}.json`, `wa-registry-overview-{date}.json`, `word_registry.json` |
| `outputs/reports/words/` | Per-word reports — Verse Context reports, engine run reports, word extracts | `vc-report-{nnn}-{word}-{date}.docx`, `{word}_{reg}_report_{date}.md` |
| `outputs/investigations/` | Ad-hoc data investigations, CSV dumps, dedup plans, instruction gap analyses | `{topic}-{date}.csv`, `{topic}-{date}.md` |
| `outputs/docx/` | Word documents for external consumption | `{WORD}-full-extract-{date}.docx` |
| `outputs/pdf/` | Final publishable products | |
| `outputs/word_reports/` | Per-word engine reports and run logs | `{word}_{reg}_report_{date}.md` |
| `outputs/archive/` | Superseded outputs (audit diffs, old reports) | moved here when superseded |

**Rule:** Nothing goes in `outputs/` root. Every file goes in the appropriate subfolder.

---

### `docs/`

Project documentation — architecture specs, setup guides, design decisions. These are **reference documents**, not session outputs.

| What goes here | Examples |
|---------------|---------|
| Architecture specifications | `Session-A-v9-Architecture-*.md` |
| Setup guides | `data_setup.md`, `step_setup.md`, `zotero_setup.md` |
| Design decisions | `pipeline_design_review_*.md`, `pipeline_decisions_*.md` |
| Data flow mapping | `field-data-flow-mapping.md` |
| Interaction preferences | `interaction-preferences.md` |
| File organisation rules | This file |

**Not here:** Session logs, status reports, investigation outputs, instruction documents.

---

### `Logs/`

Session logs — timestamped records of what happened in each working session.

| What goes here | Naming pattern |
|---------------|----------------|
| Session logs | `WA-SessionLog-{topic}-v{n}-{date}.md` |
| Pipeline status reviews | `WA-PipelineStatusReview-v{n}-{date}.md` |

**Archiving:** Old session logs stay here (they are historical records). Only move to `archive/Logs/` if explicitly superseded.

---

### `scripts/`

Utility and maintenance scripts. Active scripts only.

| What goes here | Naming convention |
|---------------|-------------------|
| Active utility scripts | `_assess_*.py`, `_check_*.py`, `_apply_*.py`, `_repair_*.py`, etc. |
| Batch construction | `_build_vc_batch.py` |
| Report generation | `_generate_programme_report.py` |
| One-off applicators | `apply_session_patch.py` |

**Rule:** `_tmp_*.py` scripts must be deleted or moved to `archive/scripts/` at end of session. They must not accumulate in `scripts/` root.

---

### `archive/`

Superseded and retired artefacts. Organised by type.

| Subfolder | What goes here |
|-----------|---------------|
| `archive/scripts/` | Retired `_tmp_*` and old utility scripts |
| `archive/patches/` | Applied patch files (moved by applicator) |
| `archive/Logs/` | Old session logs if superseded |
| `archive/docs/` | Old documentation versions |

---

### `backups/`

Engine-managed database backups. Not in Git. Rolling retention of 10 pre-run backups (managed by `engine/backup.py`).

---

### `engine/`

Core Python automation engine. Only engine module files. No outputs, no data, no reports.

### `analytics/`

Python library: API clients and DB utilities. No outputs.

### `research/`

Research notes and templates. Currently placeholder — available for researcher use.

---

## 3. Archiving Rules

| Trigger | Action |
|---------|--------|
| New version of a report produced | Move prior version to `outputs/archive/` |
| New version of an instruction document | Move prior version to the `archive/` subfolder within the instruction's directory |
| Patch applied successfully | Applicator moves patch to `archive/patches/` |
| `_tmp_*.py` script no longer needed | Move to `archive/scripts/` or delete |
| New day's word export produced | Prior day's export to `data/exports/archive/` (same-day versions kept) |

---

## 4. Cleanup Actions Required (2026-03-30)

The following files need to be moved to comply with these rules:

### From `outputs/` root to `outputs/reports/`:
- `wa-programme-status-report-20260328.md`
- `wa-programme-status-report-20260330.md`

### From `outputs/` root to `outputs/investigations/`:
- `mti_dedup_plan_20260330.csv`
- `mti_orphans_20260330.csv`
- `mti_terms_full_20260330.csv`
- `multi_owner_terms_20260330.csv`
- `wa_term_inventory_full_20260330.csv`
- `sense-sampling-walkthrough-20260328.md`
- `v5-impact-assessment-20260327.md`
- `task5-zero-term-investigation-20260327.md`
- `cross_registry_term_analysis_20260328.png`
- `cross_registry_root_analysis_20260328.png`
- `term_sharing_network_20260328.png`

### From `outputs/` root to `outputs/markdown/`:
- `WA-InstructionGaps-v2-20260330_1 researcher comments.md`
- `WA-InstructionGaps-v2_2-20260330.md`

### From `outputs/markdown/` to `outputs/investigations/`:
- `mti-dedup-investigation-20260330.md`

### From `scripts/` root — archive or delete:
- `_tmp_apply_fixes.py` → `archive/scripts/`
- `_tmp_status_report.py` → `archive/scripts/`

---

## 5. Claude Code Obligations

1. **Before writing any file:** determine the correct subfolder from this document.
2. **After completing an investigation:** move `_tmp_*.py` scripts to `archive/scripts/`.
3. **After producing a new report version:** move the prior version to `outputs/archive/`.
4. **Never place files in a folder root** when a subfolder exists for that file type.
5. **Reference this document** when uncertain about file placement.

---

*Created 2026-03-30. Referenced from CLAUDE.md Section 2.*
