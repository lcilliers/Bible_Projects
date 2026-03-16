"""
bible_analytics.py
──────────────────
Main entry point for the Bible_Projects analytics module.

Usage
-----
    python bible_analytics.py                                        # Run default pipeline
    python bible_analytics.py --test-zotero                         # Test Zotero API connectivity
    python bible_analytics.py --test-step                            # Test STEP Bible API connectivity
    python bible_analytics.py --init-db                              # Initialise SQLite schema
    python bible_analytics.py --test-db                              # Verify SQLite connectivity
    python bible_analytics.py --import-json FILE --table TABLE       # Import JSON records into SQLite
    python bible_analytics.py --export-json TABLE                    # Export table to JSON
    python bible_analytics.py --list-attachments ITEM_KEY            # List attachments for a Zotero item
    python bible_analytics.py --download-attachment ATTACHMENT_KEY   # Download a Zotero attachment
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


def test_step() -> None:
    """Verify that the STEP Bible API is reachable and returns a verse."""
    from step_client import StepClient  # type: ignore

    client = StepClient()
    version = os.getenv("STEP_DEFAULT_VERSION", "ESV")

    result = client.get_passage("John.3.16", version=version)
    if result:
        text = result.get("text", "(no text returned)")
        print(f"SUCCESS: Connected to STEP Bible API ({client.base_url}).")
        print(f"  John 3:16 ({version}): {text!r}")
    else:
        print(
            "WARNING: STEP Bible API responded but returned no text for John 3:16.\n"
            "See docs/step_setup.md for troubleshooting."
        )


def init_db() -> None:
    """Initialise the SQLite database schema (creates tables if absent)."""
    from db_client import get_connection, init_schema_from_file  # type: ignore

    conn = get_connection()
    init_schema_from_file(conn)
    conn.close()
    db_path = os.getenv("DB_PATH", os.path.join(ROOT_DIR, "data", "bible_research.db"))
    print(f"SUCCESS: Database schema initialised at {db_path}")


def test_db() -> None:
    """Verify that the SQLite database is reachable and the schema is present."""
    from db_client import get_connection, list_tables, row_count  # type: ignore

    conn = get_connection()
    tables = list_tables(conn)
    db_path = os.getenv("DB_PATH", os.path.join(ROOT_DIR, "data", "bible_research.db"))

    if not tables:
        print(
            "WARNING: Database exists but contains no tables.\n"
            "Run: python bible_analytics.py --init-db"
        )
        conn.close()
        return

    print(f"SUCCESS: Connected to SQLite database at {db_path}")
    print(f"  Tables: {', '.join(tables)}")
    if "verse_notes" in tables:
        n = row_count(conn, "verse_notes")
        print(f"  verse_notes row count: {n}")
    conn.close()


def import_json(json_path: str, table: str) -> None:
    """Import a JSON file of records into the named SQLite table."""
    from db_client import get_connection, import_json_file  # type: ignore

    if not os.path.isfile(json_path):
        print(f"ERROR: File not found: {json_path}")
        sys.exit(1)

    conn = get_connection()
    count = import_json_file(conn, json_path, table)
    conn.close()
    print(f"SUCCESS: Imported {count} record(s) from {json_path!r} into '{table}'.")


def export_json(table: str) -> None:
    """Export the named SQLite table to a JSON file in data/exports/."""
    import json as _json

    from db_client import export_table_to_json, get_connection  # type: ignore

    conn = get_connection()
    output_path = os.path.join(ROOT_DIR, "data", "exports", f"{table}.json")
    rows = export_table_to_json(conn, table, output_path=output_path)
    conn.close()
    print(f"SUCCESS: Exported {len(rows)} row(s) from '{table}' to {output_path!r}.")


def list_attachments(item_key: str) -> None:
    """List all attachments for a Zotero item and print their metadata."""
    from zotero_client import get_attachments  # type: ignore

    attachments = get_attachments(item_key)
    if not attachments:
        print(f"No attachments found for item '{item_key}'.")
        return

    print(f"Attachments for item '{item_key}' ({len(attachments)} found):")
    for att in attachments:
        d = att["data"]
        key = d.get("key", "?")
        filename = d.get("filename") or d.get("title") or "(no filename)"
        content_type = d.get("contentType", "(unknown type)")
        link_mode = d.get("linkMode", "?")
        downloadable = "✓ downloadable" if link_mode in ("imported_file", "imported_url") else "✗ linked (local only)"
        print(f"  [{key}]  {filename}  |  {content_type}  |  {link_mode}  |  {downloadable}")


def download_attachment(attachment_key: str) -> None:
    """Download a Zotero stored attachment to data/exports/."""
    from zotero_client import download_attachment as _download  # type: ignore

    try:
        dest = _download(attachment_key)
        print(f"SUCCESS: Attachment '{attachment_key}' saved to {dest!r}.")
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except RuntimeError as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bible_Projects analytics entry point."
    )
    parser.add_argument(
        "--test-zotero",
        action="store_true",
        help="Test Zotero API connectivity and exit.",
    )
    parser.add_argument(
        "--test-step",
        action="store_true",
        help="Test STEP Bible API connectivity and exit.",
    )
    parser.add_argument(
        "--init-db",
        action="store_true",
        help="Initialise the SQLite database schema and exit.",
    )
    parser.add_argument(
        "--test-db",
        action="store_true",
        help="Verify SQLite database connectivity and schema, then exit.",
    )
    parser.add_argument(
        "--import-json",
        metavar="FILE",
        help="Path to a JSON file of records to import. Requires --table.",
    )
    parser.add_argument(
        "--table",
        metavar="TABLE",
        help="Target table name for --import-json or source table for --export-json.",
    )
    parser.add_argument(
        "--export-json",
        metavar="TABLE",
        help="Export the named table to data/exports/<TABLE>.json and exit.",
    )
    parser.add_argument(
        "--list-attachments",
        metavar="ITEM_KEY",
        help="List all attachments for the given Zotero item key and exit.",
    )
    parser.add_argument(
        "--download-attachment",
        metavar="ATTACHMENT_KEY",
        help="Download a stored Zotero attachment to data/exports/ and exit.",
    )
    args = parser.parse_args()

    if args.test_zotero:
        test_zotero()
        return

    if args.test_step:
        test_step()
        return

    if args.init_db:
        init_db()
        return

    if args.test_db:
        test_db()
        return

    if args.import_json:
        if not args.table:
            print("ERROR: --import-json requires --table <TABLE_NAME>.")
            sys.exit(1)
        import_json(args.import_json, args.table)
        return

    if args.export_json:
        export_json(args.export_json)
        return

    if args.list_attachments:
        list_attachments(args.list_attachments)
        return

    if args.download_attachment:
        download_attachment(args.download_attachment)
        return

    # ── Default pipeline placeholder ───────────────────────────────────────
    print("Bible_Projects analytics pipeline — ready.")
    print("Add your analysis tasks here.")


if __name__ == "__main__":
    main()
