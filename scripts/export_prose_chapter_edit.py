"""Export one current prose chapter or section as a temporary editable Markdown file.

The markers are immutable routing metadata. Edit only the body below each
chapter heading; the importer rejects structural marker changes.

Core logic now lives in `iba/app/lib/prosestore.py` (escalation #784, 2026-08-21 — incorporated
into the IBA app; this file is the thin CLI entry point documented in
`docs/prose-store-architecture.md` §8).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from iba.app.lib.cfg import Cfg
from iba.app.lib import prosestore


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a prose chapter for editing")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--type-id", type=int, help="single prose_section_type.id")
    group.add_argument("--book", help="book_label, for example Programme")
    parser.add_argument("--chapter", type=int, help="chapter number; required with --book")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    if args.book is not None and args.chapter is None:
        parser.error("--chapter is required with --book")

    cfg = Cfg()
    try:
        result = prosestore.run_export_chapter(
            cfg, type_id=args.type_id, book=args.book, chapter=args.chapter, out=args.out)
    except ValueError as e:
        parser.error(str(e))
        return 2
    finally:
        cfg.close()

    print(f"Exported {result['sections']} prose section(s): {result['path']}")
    print("Edit prose bodies only; preserve all PROSE_* markers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
