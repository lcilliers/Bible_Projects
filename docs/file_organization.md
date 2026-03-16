# File Organisation Guide

This document is the single source of truth for **how research materials are organised** across both storage tiers in the Bible_Projects ecosystem.

---

## A note on access

> **GitHub Copilot operates only within the cloned GitHub repository.**
> It cannot read your local disk or Google Drive directly.
> To get the most from this guide, paste relevant file listings or document contents into a Claude or Copilot conversation so the AI can analyse them and make tailored suggestions.

---

## Two-Tier Storage Model

Bible_Projects uses two complementary stores. Understanding the boundary between them removes all ambiguity about where a file belongs.

| Tier | Location | What lives here | Backed up by |
|------|----------|-----------------|-------------|
| **Git / GitHub** | `lcilliers/Bible_Projects` | Code, schemas, scripts, docs, small structured data, templates, working notes ≤ a few KB | GitHub |
| **Google Drive** | `G:\My Drive\Bible_study_projects` | PDFs, `.docx` outputs, large exports, raw Claude conversation archives, images, Zotero attachment copies | Google Sync |

### The golden rule

> **If it is a file you would run, version, or share as code or documentation → Git.**
> **If it is a research artefact, large file, or binary → Google Drive.**

---

## Google Drive: Recommended Folder Structure

The folder below is the canonical Google Drive tree for this project. If you have an existing `Claude_Research` folder with unorganised materials, use Section 4 (Migration) to move them here.

```
G:\My Drive\Bible_study_projects\
│
├── 00_Admin\                      ← Project admin, checklists, meeting notes
│   ├── project_log.md             ← Running log of decisions and milestones
│   └── toolchain_notes.md         ← Notes on tools, versions, issues
│
├── 01_Primary_Sources\            ← Bible texts, interlinears, lexicons, grammars
│   ├── Bible_texts\               ← Downloaded Bible editions (ESV, NIV, NA28, BHS…)
│   ├── Lexicons\                  ← BDAG, BDB, Thayer, LSJ PDFs
│   └── Grammars\                  ← Hebrew / Greek grammar reference PDFs
│
├── 02_Secondary_Sources\          ← Commentaries, academic papers, books
│   ├── Commentaries\
│   ├── Journal_Articles\
│   └── Books\
│
├── 03_Research_Projects\          ← One sub-folder per active research project
│   ├── PROJECT_TEMPLATE\          ← Copy this for each new project (see below)
│   │   ├── brief.md               ← Project brief (use template)
│   │   ├── notes\                 ← Working notes for this project
│   │   ├── claude_sessions\       ← Exported / saved Claude conversations
│   │   └── outputs\               ← Final outputs for this project
│   └── [your active projects]\
│
├── 04_Claude_Research\            ← Organised home for all Claude outputs
│   ├── _inbox\                    ← Drop raw Claude outputs here before filing
│   ├── sessions\                  ← Named, dated Claude session logs
│   │   └── YYYY-MM-DD_topic.md    ← Naming convention (see below)
│   ├── analyses\                  ← Completed analytical outputs from Claude
│   └── data_inputs\               ← JSON batches ready for --import-json
│
├── 05_Zotero_Attachments\         ← Mirror of Zotero local attachments
│   └── (managed by Zotero)
│
├── 06_Outputs\                    ← All final and near-final research outputs
│   ├── markdown\                  ← .md versions
│   ├── docx\                      ← .docx versions (for sharing)
│   └── pdf\                       ← .pdf versions (final products)
│
└── 07_Reference\                  ← Maps, charts, timelines, reference sheets
    ├── biblical_timelines\
    ├── maps\
    └── concordances\
```

> **Note on `04_Claude_Research`:** This folder replaces and organises your current `G:\My Drive\Claude_Research` folder. See Section 4 for how to migrate.

---

## Git Repository: Folder Structure

```
Bible_Projects/ (GitHub)
│
├── research/                      ← Versioned research notes (text only, small)
│   ├── projects/                  ← One .md summary per project
│   ├── notes/                     ← Short working notes, cross-references
│   └── templates/                 ← Reusable templates (research, Claude sessions)
│       ├── research_note_template.md
│       ├── claude_session_template.md
│       └── project_brief_template.md
│
├── data/                          ← Structured data (SQLite + supporting files)
│   ├── bible_research.db          ← SQLite DB (Git-excluded — stays on disk/Drive)
│   ├── schema/                    ← SQL schema definitions (versioned)
│   ├── imports/                   ← JSON from Claude staged for --import-json
│   └── exports/                   ← JSON exports for Claude to read
│
├── docs/                          ← Project documentation
│   ├── file_organization.md       ← This file
│   ├── data_setup.md              ← SQLite platform guide
│   ├── zotero_setup.md            ← Zotero API guide
│   └── step_setup.md              ← STEP Bible API guide
│
├── outputs/                       ← Output files (Git tracks .md; .docx/.pdf excluded)
│   ├── markdown/
│   ├── docx/
│   └── pdf/
│
├── analytics/                     ← Python code (always in Git)
│   ├── bible_analytics.py
│   ├── db_client.py
│   ├── zotero_client.py
│   ├── step_client.py
│   └── requirements.txt
│
└── scripts/                       ← PowerShell utilities
    └── env_setup.ps1
```

---

## What Goes Where — Quick Reference

| File type | Example | Git? | Google Drive? |
|-----------|---------|------|---------------|
| Python scripts | `db_client.py` | ✅ | — |
| SQL schema | `create_tables.sql` | ✅ | — |
| Setup documentation | `data_setup.md` | ✅ | — |
| Research note (short, text) | `notes/John_3_16.md` | ✅ | — |
| Project brief (text) | `projects/gospel_of_john.md` | ✅ | — |
| Templates | `templates/*.md` | ✅ | — |
| Claude JSON import batch | `data/imports/batch_01.json` | ⚠️ temporary | ✅ archive in `04_Claude_Research/data_inputs/` |
| SQLite database file | `bible_research.db` | ❌ | ✅ |
| Large PDF | Any commentary / paper | ❌ | ✅ `01_Primary_Sources/` or `02_Secondary_Sources/` |
| Word document output | `essay.docx` | ❌ | ✅ `06_Outputs/docx/` |
| PDF output | `essay.pdf` | ❌ | ✅ `06_Outputs/pdf/` |
| Raw Claude conversation export | `claude_session.html` | ❌ | ✅ `04_Claude_Research/sessions/` |
| Zotero attachments | Any PDF managed by Zotero | ❌ | ✅ `05_Zotero_Attachments/` |
| `.env` credentials file | `.env` | ❌ never | ✅ keep locally |

---

## Naming Conventions

Consistent naming makes files findable without search tools.

### General rules

- Use underscores (`_`) as separators — not spaces, not hyphens
- Use lowercase for everything except proper nouns (book names, author names)
- Prefix dated files with `YYYY-MM-DD`
- Prefix versioned documents with `v01`, `v02`, etc.

### Claude session files

```
YYYY-MM-DD_[topic]_[session_number].md

Examples:
  2026-03-15_John_3_16_exegesis_01.md
  2026-03-16_Pauline_theology_grace_01.md
  2026-03-20_Daniel_7_comparative_01.md
```

### Research notes

```
[book_or_topic]_[subtopic]_[type].md

Examples:
  John_3_16_exegesis_note.md
  Pauline_soteriology_overview_note.md
  Genesis_1_creation_narrative_note.md
```

### Project briefs

```
[short_project_name]_brief.md

Examples:
  gospel_of_john_brief.md
  pauline_letters_brief.md
```

### Data import JSON files

```
[table]_[topic]_[YYYY-MM-DD]_[batch_number].json

Examples:
  verse_notes_John_2026-03-15_01.json
  verse_notes_Psalms_2026-03-20_01.json
```

---

## Section 4 — Migrating from `Claude_Research`

Your `G:\My Drive\Claude_Research` folder contains existing unorganised materials. Use this workflow to move them into the new structure without losing anything.

### Step 1 — Take stock (do this in Claude)

Copy this prompt into a Claude session:

```
I have a folder of unorganised research files from my Bible study work.
I'll paste a file listing below. For each file, suggest:
1. Which category it belongs to (primary source, secondary source,
   research note, Claude session, data input, output, reference)
2. A new filename following these conventions:
   - Dated files: YYYY-MM-DD_topic_number.md
   - Notes: topic_subtopic_note.md
   - Data: table_topic_YYYY-MM-DD_batch.json

[PASTE YOUR FILE LISTING HERE — you can get it by running:
 dir /s /b "G:\My Drive\Claude_Research" > file_list.txt
 in a Windows command prompt]
```

### Step 2 — Sort into holding folders

In Google Drive, create:
```
G:\My Drive\Claude_Research\_sorted\
    _primary_sources\
    _secondary_sources\
    _claude_sessions\
    _data_inputs\
    _outputs\
    _unclear\          ← anything you're not sure about
```

Move each file into its holding category.

### Step 3 — Move to final locations

Once sorted, move each holding folder's contents to the permanent location:

| Holding folder | Final location |
|---------------|----------------|
| `_primary_sources\` | `Bible_study_projects\01_Primary_Sources\` |
| `_secondary_sources\` | `Bible_study_projects\02_Secondary_Sources\` |
| `_claude_sessions\` | `Bible_study_projects\04_Claude_Research\sessions\` |
| `_data_inputs\` | `Bible_study_projects\04_Claude_Research\data_inputs\` |
| `_outputs\` | `Bible_study_projects\06_Outputs\` |
| `_unclear\` | Review with Claude before moving |

### Step 4 — Convert key Claude sessions to research notes

For any Claude session that contains valuable analysis worth keeping:

1. Open the session file
2. Create a new research note in `research/notes/` in the Git repo using the template in `research/templates/research_note_template.md`
3. Summarise the key insights in the note (keep it concise — the full session stays on Google Drive)
4. If the session produced JSON data records, move the JSON to `data/imports/` and run the import

---

## Section 5 — Sharing Materials with AI Tools

### With Claude (claude.ai)

Claude can read attached files directly in the chat interface. For best results:

1. **For text analysis** — paste content directly or attach `.md`, `.txt`, `.pdf` files
2. **For data** — export from SQLite first: `python analytics/bible_analytics.py --export-json verse_notes`, then attach the JSON
3. **For large datasets** — Claude can comfortably read ~300–500 rows of JSON at a time; paginate larger exports
4. **For session continuity** — save each Claude session using the template in `research/templates/claude_session_template.md`; reference previous session notes in the next session

### With GitHub Copilot

Copilot works within the Git repository. To share context:

1. Keep research notes in `research/notes/` and `research/projects/` — Copilot can read these
2. Reference the schema in `data/schema/create_tables.sql` when asking Copilot to write data queries
3. Keep documentation in `docs/` up to date — Copilot uses these as context

---

## Section 6 — Ongoing Workflow

```
New research topic
        ↓
Create project brief in research/projects/ (use template)
        ↓
Run Claude sessions → save to Google Drive 04_Claude_Research/sessions/
        ↓
Extract key insights → create research note in research/notes/
        ↓
If Claude produces data records → save JSON to data/imports/
        ↓
Import into SQLite: python analytics/bible_analytics.py --import-json ... --table verse_notes
        ↓
When analysis complete → write output to outputs/markdown/
        ↓
Convert to .docx or .pdf as needed → copy to Google Drive 06_Outputs/
```

---

## Useful Resources

- [Google Drive web interface](https://drive.google.com)
- [Zotero collection structure](zotero_setup.md#zotero-collection-structure-recommended)
- [SQLite data platform](data_setup.md)
- [STEP Bible integration](step_setup.md)
