# STEP Bible API Setup

This document describes how to configure access to the **STEP Bible** API for use within the `Bible_verse_analytics` module of Bible_Projects.

---

## Overview

[STEP Bible](https://www.stepbible.org/) (Scripture Tools for Every Person) is a free, open-access Bible study platform developed by [Tyndale House, Cambridge](https://www.tyndale.cam.ac.uk/). It provides:

- Dozens of Bible translations (ESV, NIV, KJV, NASB, NET, and more)
- Original Hebrew and Greek texts with morphological analysis
- Strong's concordance, lexicons, and interlinear views
- Cross-references and thematic links
- A public HTTP API for programmatic scripture access

The STEP Bible API is **publicly accessible without requiring an account or API key** for read-only queries, so you can start making API calls immediately.

> **Important:** Please review the [STEP Bible terms of use](https://www.stepbible.org/terms.jsp) before building any application on top of it. Use the API responsibly — reasonable request rates, local caching where possible, and proper attribution of scripture sources.

---

## API Access

### Base URL

```
https://www.stepbible.org/api/
```

### Official Resources

| Resource | URL |
|----------|-----|
| STEP Bible website | <https://www.stepbible.org/> |
| STEP Bible API | <https://www.stepbible.org/api/> |
| STEP Bible on GitHub (open source) | <https://github.com/STEPBible/step> |
| Tyndale House (project host) | <https://www.tyndale.cam.ac.uk/> |
| Terms of use | <https://www.stepbible.org/terms.jsp> |

### Authentication

The public API **does not require an API key** for standard lookups. All requests are anonymous HTTP GET calls. If you require extended or bulk access, contact the STEP Bible team via their [website](https://www.stepbible.org/).

---

## Prerequisites

- Python 3.10+
- `requests` library (already in `analytics/requirements.txt`)
- `python-dotenv` library (already in `analytics/requirements.txt`)

---

## Step 1 – Verify API Reachability

No registration needed. Confirm the API is accessible:

```bash
curl "https://www.stepbible.org/api/bible/passage/ESV/John.3.16"
```

Or with Python:

```python
import requests

response = requests.get(
    "https://www.stepbible.org/api/bible/passage/ESV/John.3.16",
    timeout=10,
)
print(response.status_code)   # 200 if reachable
print(response.json())
```

---

## Step 2 – Configure the `.env` File

Store API configuration in your `.env` file at the project root so it can be changed without touching code. **Never commit this file** (the `.gitignore` already excludes `.env`).

Add the following entries to `.env`:

```dotenv
# ── STEP Bible ──────────────────────────────────────────────────────────────
# Base URL for the STEP Bible public API
STEP_API_BASE_URL=https://www.stepbible.org/api

# Default Bible translation to use (e.g. ESV, NIV, KJV, NASB, NET)
STEP_DEFAULT_VERSION=ESV

# Optional: API key placeholder — leave blank unless STEP issues a key
# STEP_API_KEY=

# Optional: HTTP request timeout in seconds
STEP_REQUEST_TIMEOUT=10
```

The environment setup script (`scripts/env_setup.ps1`) will generate a `.env` template automatically if one does not yet exist. You can then add the STEP entries above.

---

## Step 3 – Install Python Dependencies

The `requests` and `python-dotenv` packages are already in `analytics/requirements.txt`. Install all dependencies with:

```bash
cd analytics
pip install -r requirements.txt
```

Or run the PowerShell bootstrap from the project root:

```powershell
.\scripts\env_setup.ps1
```

---

## Step 4 – Verify the Integration

Run the built-in connectivity check from the **project root**:

```bash
python analytics/bible_analytics.py --test-step
```

A successful result looks like:

```
SUCCESS: Connected to STEP Bible API (https://www.stepbible.org/api).
  John 3:16 (ESV): "For God so loved the world, that he gave his only Son..."
```

---

## Step 5 – Using the STEP Client in Code

The `analytics/step_client.py` module provides a thin wrapper around the STEP Bible API:

```python
from step_client import StepClient

client = StepClient()

# Retrieve a passage
passage = client.get_passage("John.3.16", version="ESV")
print(passage.get("text"))

# Search for a keyword across the Bible
results = client.search("grace", version="ESV")
for verse in results:
    print(f"{verse.get('ref')}: {verse.get('text')}")
```

---

## Common API Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `/bible/passage/{version}/{ref}` | Retrieve a verse or passage | `/bible/passage/ESV/John.3.16` |
| `/bible/search/{version}/{query}` | Search for a word or phrase | `/bible/search/ESV/grace` |
| `/bible/versions` | List available Bible versions | `/bible/versions` |

> These endpoint patterns are based on the STEP Bible public API. Confirm exact routes and response schemas in the [official API docs](https://www.stepbible.org/api/).

---

## Recommended Data Structure

Retrieved STEP Bible data is stored under `data/` in the project:

```
data/
└── step/
    ├── passages/              # Raw passage JSON responses
    ├── searches/              # Search result JSON responses
    └── cache/                 # Optional local cache to reduce API calls
```

---

## Troubleshooting

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| `ConnectionError` | No internet / wrong URL | Check network; verify `STEP_API_BASE_URL` in `.env` |
| `HTTP 429 Too Many Requests` | Rate limit exceeded | Add delays between requests; cache results in `data/step/cache/` |
| `HTTP 404 Not Found` | Wrong reference format | Use dot notation: `John.3.16` (not `John 3:16`) in URLs |
| `KeyError` in response JSON | API response schema changed | Check [STEP API docs](https://www.stepbible.org/api/) for updates |

---

## Useful Resources

- [STEP Bible](https://www.stepbible.org/)
- [STEP Bible API](https://www.stepbible.org/api/)
- [STEP Bible on GitHub (open source)](https://github.com/STEPBible/step)
- [Tyndale House Cambridge](https://www.tyndale.cam.ac.uk/)
- [STEP Bible Terms of Use](https://www.stepbible.org/terms.jsp)
