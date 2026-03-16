"""
bible_analytics.py
──────────────────
Main entry point for the Bible_Projects analytics module.

Usage
-----
    python bible_analytics.py               # Run default pipeline
    python bible_analytics.py --test-zotero # Test Zotero API connectivity
"""

import argparse
import os
import sys

from dotenv import load_dotenv

# ── Load environment variables from project-root .env ──────────────────────
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
load_dotenv(os.path.join(ROOT_DIR, ".env"))


def test_zotero() -> None:
    """Verify that the Zotero API credentials are configured and reachable."""
    try:
        from pyzotero import zotero  # type: ignore
    except ImportError:
        print("ERROR: pyzotero is not installed. Run: pip install -r requirements.txt")
        sys.exit(1)

    api_key = os.getenv("ZOTERO_API_KEY")
    user_id = os.getenv("ZOTERO_USER_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "user")

    if not api_key or not user_id:
        print(
            "ERROR: ZOTERO_API_KEY and ZOTERO_USER_ID must be set in your .env file.\n"
            "See docs/zotero_setup.md for setup instructions."
        )
        sys.exit(1)

    zot = zotero.Zotero(user_id, library_type, api_key)
    items = zot.top(limit=5)
    print(f"SUCCESS: Connected to Zotero. Top {len(items)} item(s):")
    for item in items:
        title = item["data"].get("title", "(no title)")
        print(f"  • {title}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bible_Projects analytics entry point."
    )
    parser.add_argument(
        "--test-zotero",
        action="store_true",
        help="Test Zotero API connectivity and exit.",
    )
    args = parser.parse_args()

    if args.test_zotero:
        test_zotero()
        return

    # ── Default pipeline placeholder ───────────────────────────────────────
    print("Bible_Projects analytics pipeline — ready.")
    print("Add your analysis tasks here.")


if __name__ == "__main__":
    main()
