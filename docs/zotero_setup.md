# Zotero API Setup

This document describes how to configure the Zotero API for use within the Bible_Projects research environment.

---

## Overview

[Zotero](https://www.zotero.org/) is used as the primary reference and file storage manager for this project. The Zotero Web API allows Python scripts and other tools to programmatically read, write, and organise library items.

---

## Prerequisites

- A Zotero account at [zotero.org](https://www.zotero.org/user/register)
- Zotero desktop application installed
- Python 3.10+ (for API integration scripts)

---

## Step 1 – Obtain Your Zotero API Key

1. Log in to [zotero.org](https://www.zotero.org/).
2. Navigate to **Settings → Feeds/API**.
3. Under **Private Keys**, click **Create new private key**.
4. Give the key a descriptive name (e.g., `Bible_Projects`).
5. Grant the following permissions:
   - **Personal Library** – Read/Write
   - **Groups** – Read/Write (if using group libraries)
6. Click **Save Key** and copy the generated key.

---

## Step 2 – Find Your Zotero User ID

Your User ID appears on the same **Feeds/API** settings page, directly below your username, e.g.:

```
Your userID for use in API calls is 1234567
```

---

## Step 3 – Store Credentials Securely

Create a `.env` file in the project root (**never commit this file**):

```dotenv
ZOTERO_API_KEY=your_api_key_here
ZOTERO_USER_ID=your_user_id_here
ZOTERO_LIBRARY_TYPE=user   # or "group" for a shared group library
```

The `.gitignore` is already configured to exclude `.env` files.

---

## Step 4 – Install the Python Client

```bash
cd analytics
pip install -r requirements.txt
```

The `pyzotero` package is included in `requirements.txt`.

---

## Step 5 – Verify the Connection

```python
# Quick connectivity test (run from the analytics/ directory)
from zotero_client import get_library

library = get_library()
items = library.top(limit=5)
for item in items:
    print(item['data'].get('title', '(no title)'))
```

Or run the analytics entry point:

```bash
python bible_analytics.py --test-zotero
```

---

## Zotero Collection Structure (Recommended)

```
My Library/
├── Bible_Projects/
│   ├── Primary Sources/       # Bible texts, commentaries, lexicons
│   ├── Secondary Sources/     # Academic papers, books
│   ├── Reference/             # Dictionaries, encyclopaedias
│   └── Working Documents/     # Notes, drafts, interim outputs
```

---

## Useful Resources

- [Zotero Web API Documentation](https://www.zotero.org/support/dev/web_api/v3/start)
- [pyzotero Documentation](https://pyzotero.readthedocs.io/)
