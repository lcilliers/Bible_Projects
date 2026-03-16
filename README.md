# Bible_Projects

> **Repository:** [lcilliers/Bible_Projects](https://github.com/lcilliers/Bible_projects)
> **File Server:** Google Drive (`G:\My Drive\Bible_study_projects`)

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
| **Obsidian** | Writing and note-taking (value still being evaluated) |
| **Google Docs** | Project file management |
| **PowerShell** | File handling and environment scripting |
| **Python** | Analytics and data processing |
| **SQLite / Structured JSON** | Data management (TBD — see [`data/`](data/)) |
| **Git + GitHub** | Source control (`lcilliers/Bible_projects`) |

---

## Repository Structure

```
Bible_Projects/
├── README.md                  # This file — project overview
├── .gitignore                 # Files and folders excluded from source control
│
├── research/                  # Research notes, source summaries, working documents
│
├── docs/                      # Project documentation and setup guides
│   └── zotero_setup.md        # Zotero API integration guide
│
├── data/                      # Structured data files (JSON, CSV, SQLite)
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
    └── bible_analytics.py     # Main analytics entry point
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

---

## Contributing

This is leRoux's personal research project. Contributions are made through the defined toolchain above. All outputs are reviewed and approved by leRoux as the ultimate authority on scope, methodology, and quality.
