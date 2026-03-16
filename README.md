# Bible_Projects

> **Repository:** [lcilliers/Bible_Projects](https://github.com/lcilliers/Bible_projects)
> **File Server (Google Drive):** `G:\My Drive\Bible_study_projects` — see [`docs/file_organization.md`](docs/file_organization.md) for the full two-tier storage structure

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
