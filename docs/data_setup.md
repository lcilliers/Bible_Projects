# Structured Data Platform: SQLite

This document explains the data platform decision for Bible_Projects, covers the schema design approach, and describes the JSON → SQLite import workflow that enables Claude to feed new research records directly into the database.

---

## Decision: SQLite

After evaluating the options — full SQL (PostgreSQL/MySQL), SQLite, and pure JSON — **SQLite** was chosen as the structured data platform. The table below summarises the evaluation:

| Criterion | SQLite ✅ | PostgreSQL / MySQL ❌ | Pure JSON ❌ |
|-----------|-----------|----------------------|-------------|
| Multi-table, relational | ✓ | ✓ | Partial |
| ~20 000 rows (main table) | Trivially fast | Overkill | Slow at scale |
| No server / no install | ✓ — single `.db` file | ✗ — requires server | ✓ |
| Works on Google Drive / local | ✓ | ✗ | ✓ |
| Python built-in support | ✓ — `sqlite3` stdlib | Needs driver | ✓ — `json` stdlib |
| Claude can read/export data | ✓ — JSON export in one step | ✓ | ✓ |
| JSON import workflow | ✓ — trivial with pandas | ✓ | N/A |
| GUI browser available | ✓ — DB Browser for SQLite | ✓ | ✗ |
| Suitable for leRoux's scale | ✓ | Overkill | ✗ |

SQLite stores the entire database in a single cross-platform file (`data/bible_research.db`) that travels with the project — on disk, on Google Drive, or in the repository (the `.db` file is excluded from Git by `.gitignore`).

---

## Prerequisites

- Python 3.10+ — `sqlite3` is part of the standard library; **no extra install needed**
- `pandas` — already in `analytics/requirements.txt` (used for bulk DataFrame → SQLite inserts)
- **Optional GUI:** [DB Browser for SQLite](https://sqlitebrowser.org/) (free, cross-platform) — recommended for visually exploring and editing the database

---

## Directory Structure

```
data/
├── bible_research.db      # Primary SQLite database (excluded from Git)
├── schema/
│   └── create_tables.sql  # SQL schema definitions — versioned in Git
├── imports/               # JSON files from Claude staged for import
│   └── .gitkeep
└── exports/               # JSON / CSV exports produced for Claude to read
    └── .gitkeep
```

> The `.db` file itself is excluded from Git (large binary, contains research data).
> The **schema** SQL files **are** versioned so the database can always be recreated.

---

## Step 1 – Initialise the Database

Run the environment setup script (creates `.env` template and directory tree):

```powershell
.\scripts\env_setup.ps1
```

Then initialise the database schema from Python:

```bash
python analytics/bible_analytics.py --init-db
```

Or directly in Python:

```python
from db_client import get_connection, init_schema_from_file

conn = get_connection()          # uses DB_PATH from .env, default: data/bible_research.db
init_schema_from_file(conn)      # executes data/schema/create_tables.sql
conn.close()
```

---

## Step 2 – Core Schema Design

The schema follows these conventions:

- Every table has an `id INTEGER PRIMARY KEY AUTOINCREMENT`.
- Lookup/reference tables (books, categories, tags) are small and stable.
- The **main research table** (`verse_notes`) is the high-volume table (~20 000 rows).
- Foreign keys are enforced with `PRAGMA foreign_keys = ON` (set in `db_client.py`).

The reference schema is in [`data/schema/create_tables.sql`](../data/schema/create_tables.sql).

### Key Tables

| Table | Purpose | Expected rows |
|-------|---------|---------------|
| `books` | Bible books (66 rows, static) | 66 |
| `verse_notes` | Main research table — one row per annotated verse | ~20 000 |
| `themes` | Research themes / topic tags | Hundreds |
| `verse_theme_map` | Many-to-many: verses ↔ themes | Tens of thousands |
| `sources` | Reference sources (Zotero items, commentaries) | Hundreds |
| `verse_source_map` | Many-to-many: verses ↔ sources | Thousands |

---

## Step 3 – JSON Import Workflow (Claude → SQLite)

The primary data-entry workflow is:

```
Claude analyses / generates research
       ↓
Claude outputs structured JSON (list of records)
       ↓
JSON file saved to  data/imports/
       ↓
Python import script validates + inserts into SQLite
       ↓
Data available for analytics queries
```

### JSON Record Format

Claude should output records as a **JSON array of objects** where each key matches a column name in the target table. Example for `verse_notes`:

```json
[
  {
    "book_id": 43,
    "chapter": 3,
    "verse": 16,
    "translation": "ESV",
    "note": "Central statement of the gospel — God's love expressed through the gift of his Son.",
    "theme_tags": ["love", "salvation", "gospel"],
    "source_refs": ["Zotero:ABC123"]
  }
]
```

### Import Command

```bash
# Import a JSON file produced by Claude
python analytics/bible_analytics.py --import-json data/imports/verse_notes_batch_01.json --table verse_notes
```

Or directly in Python:

```python
import json
from db_client import get_connection, import_json_records

with open("data/imports/verse_notes_batch_01.json") as f:
    records = json.load(f)

conn = get_connection()
imported = import_json_records(conn, "verse_notes", records)
print(f"Imported {imported} records.")
conn.close()
```

---

## Step 4 – Exporting Data for Claude

Export a table or query result to JSON so Claude can read and reason about the data:

```bash
# Export entire verse_notes table to JSON
python analytics/bible_analytics.py --export-json verse_notes
```

Or in Python:

```python
from db_client import get_connection, query_to_json

conn = get_connection()
rows = query_to_json(conn, "SELECT * FROM verse_notes WHERE book_id = 43 LIMIT 100")
conn.close()

import json
print(json.dumps(rows[:3], indent=2))
```

Claude can comfortably ingest JSON exports of up to a few hundred rows at a time. For larger datasets, filter or paginate the export.

---

## Step 5 – Verify the Setup

```bash
python analytics/bible_analytics.py --test-db
```

Expected output:

```
SUCCESS: Connected to SQLite database at data/bible_research.db
  Tables: books, verse_notes, themes, verse_theme_map, sources, verse_source_map
  verse_notes row count: 0
```

---

## Configuration (`.env`)

```dotenv
# ── SQLite Database ──────────────────────────────────────────────────────────
# Path to the SQLite database file (relative to project root)
DB_PATH=data/bible_research.db
```

---

## DB Browser for SQLite (Recommended GUI)

[DB Browser for SQLite](https://sqlitebrowser.org/) provides a free, point-and-click interface for:

- Browsing table contents
- Running ad-hoc SQL queries
- Importing/exporting CSV
- Viewing schema

Download: <https://sqlitebrowser.org/dl/>

---

## Useful Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python `sqlite3` module](https://docs.python.org/3/library/sqlite3.html)
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [pandas `to_sql` / `read_sql` docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
