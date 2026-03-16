"""
zotero_client.py
────────────────
Thin wrapper around pyzotero to provide a single, pre-configured Zotero
library object for use throughout the analytics module.
"""

import os
import sys

from dotenv import load_dotenv

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
load_dotenv(os.path.join(ROOT_DIR, ".env"))


def get_library():
    """Return an authenticated pyzotero Zotero library instance.

    Reads credentials from environment variables:
      - ZOTERO_API_KEY
      - ZOTERO_USER_ID
      - ZOTERO_LIBRARY_TYPE  (default: "user")

    Raises
    ------
    EnvironmentError
        If ZOTERO_API_KEY or ZOTERO_USER_ID are not set.
    ImportError
        If pyzotero is not installed.
    """
    try:
        from pyzotero import zotero  # type: ignore
    except ImportError as exc:
        raise ImportError(
            "pyzotero is not installed. Run: pip install -r requirements.txt"
        ) from exc

    api_key = os.getenv("ZOTERO_API_KEY")
    user_id = os.getenv("ZOTERO_USER_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "user")

    if not api_key or not user_id:
        raise EnvironmentError(
            "ZOTERO_API_KEY and ZOTERO_USER_ID must be set in your .env file.\n"
            "See docs/zotero_setup.md for setup instructions."
        )

    return zotero.Zotero(user_id, library_type, api_key)
