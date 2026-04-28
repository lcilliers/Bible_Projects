"""
zotero_client.py
────────────────
Thin wrapper around pyzotero to provide a single, pre-configured Zotero
library object for use throughout the analytics module.

PS command-line usage (from project root)
-----------------------------------------
    # List attachments for a Zotero item
    .\\analytics\\venv\\Scripts\\python.exe analytics\\bible_analytics.py --list-attachments <ITEM_KEY>

    # Download an attachment file to data/exports/
    .\\analytics\\venv\\Scripts\\python.exe analytics\\bible_analytics.py --download-attachment <ATTACHMENT_KEY>
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


def get_attachments(item_key: str) -> list[dict]:
    """Return a list of attachment metadata dicts for the given parent item key.

    Each dict contains the raw Zotero item data for one attachment child.
    Only items with itemType == 'attachment' are returned.

    Parameters
    ----------
    item_key : str
        The Zotero item key of the parent document (e.g. "AB12CD34").

    Returns
    -------
    list[dict]
        List of attachment item dicts (pyzotero format).
        Each dict has a 'data' key with fields: key, filename, contentType,
        linkMode ('imported_file', 'linked_file', 'imported_url', 'linked_url').

    Notes
    -----
    - 'imported_file' / 'imported_url'  → stored in Zotero cloud; downloadable.
    - 'linked_file'                     → stored locally on your PC only;
                                          the API cannot retrieve the file content.
    """
    library = get_library()
    children = library.children(item_key)
    return [c for c in children if c["data"].get("itemType") == "attachment"]


def download_attachment(attachment_key: str, dest_dir: str | None = None) -> str:
    """Download an attachment file and save it locally.

    Only works for stored attachments (linkMode 'imported_file' or
    'imported_url').  Linked files exist only on the local machine and
    cannot be retrieved via the API.

    Parameters
    ----------
    attachment_key : str
        The Zotero item key of the attachment itself (not the parent).
    dest_dir : str, optional
        Directory to save the file.  Defaults to data/exports/ in the
        project root.

    Returns
    -------
    str
        Absolute path to the saved file.

    Raises
    ------
    ValueError
        If the attachment is a linked file (not stored in Zotero cloud).
    RuntimeError
        If the download fails or the API returns no content.
    """
    library = get_library()

    # Fetch metadata to get filename and linkMode
    meta = library.item(attachment_key)
    data = meta["data"]
    link_mode = data.get("linkMode", "")
    filename = data.get("filename") or data.get("title") or attachment_key

    if link_mode in ("linked_file", "linked_url"):
        raise ValueError(
            f"Attachment '{attachment_key}' is a linked file ({link_mode}). "
            "Linked files are stored on your local machine and cannot be "
            "downloaded via the Zotero API."
        )

    if dest_dir is None:
        dest_dir = os.path.join(ROOT_DIR, "data", "exports")
    os.makedirs(dest_dir, exist_ok=True)

    file_content = library.file(attachment_key)
    if not file_content:
        raise RuntimeError(
            f"Zotero API returned no content for attachment '{attachment_key}'."
        )

    dest_path = os.path.join(dest_dir, filename)
    mode = "wb" if isinstance(file_content, bytes) else "w"
    with open(dest_path, mode) as fh:
        fh.write(file_content)

    return os.path.abspath(dest_path)
