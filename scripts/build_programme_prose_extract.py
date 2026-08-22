"""build_programme_prose_extract.py — Prose-book extract.

Source of truth: `prose_section_type` and the actual `prose_section` content.

Core logic now lives in `iba/app/lib/prosestore.py` (escalation #784, 2026-08-21 — incorporated
into the IBA app; this file is the thin CLI entry point documented in
`docs/prose-store-architecture.md` §8). `EXTRACTOR_VERSION`/`CHAPTER_NAMES`/`BOOK_STAGE_MAP` are no
longer hardcoded here — they read from `cfg_setting` (module='prose'), resolving the
NON-COMPLIANT flag from escalation #648.

Usage:
  python scripts/build_programme_prose_extract.py
  python scripts/build_programme_prose_extract.py --also-markdown
  python scripts/build_programme_prose_extract.py --also-docx       # readable Word doc in outputs/docx/
    python scripts/build_programme_prose_extract.py --include-body    # include full prose body text in JSON
    python scripts/build_programme_prose_extract.py --book Programme  # one book; omit for all books
  python scripts/build_programme_prose_extract.py --all-formats     # JSON + MD + DOCX with bodies

Default outputs:
  Workflow/Programme/programme_prose/wa-programme-prose-extract-{YYYYMMDD}.json
  Workflow/Programme/programme_prose/wa-programme-prose-extract-{YYYYMMDD}.md   (if --also-markdown)
  outputs/docx/wa-programme-prose-extract-{YYYYMMDD}.docx            (if --also-docx)

The `--book` value matches `prose_section_type.book_label`. Omit it to export all books.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from iba.app.lib.cfg import Cfg
from iba.app.lib import prosestore


def main() -> int:
    ap = argparse.ArgumentParser(description="Build programme-stage prose extract from DB")
    ap.add_argument("--out", type=str, default=None)
    ap.add_argument("--also-markdown", action="store_true")
    ap.add_argument("--also-docx", action="store_true",
                    help="also emit a readable .docx view (outputs/docx/)")
    ap.add_argument("--include-body", action="store_true",
                    help="include full prose body text in JSON (default: metadata only)")
    ap.add_argument("--book", type=str, default=None,
                    help="book_label to export; omit to export all books")
    ap.add_argument("--chapter", type=int, default=None,
                    help="chapter number to export; combine with --book")
    ap.add_argument("--all-formats", action="store_true",
                    help="shortcut: equivalent to --also-markdown --also-docx --include-body")
    args = ap.parse_args()

    if args.all_formats:
        args.also_markdown = True
        args.also_docx = True
        args.include_body = True

    cfg = Cfg()
    try:
        result = prosestore.run_extract(
            cfg, include_body=args.include_body, book=args.book, chapter=args.chapter,
            also_markdown=args.also_markdown, also_docx=args.also_docx, out=args.out,
        )
    except ValueError as e:
        ap.error(str(e))
        return 2
    finally:
        cfg.close()

    print(f"Wrote JSON: {result['json']}")
    if result["md"]:
        print(f"Wrote MD:   {result['md']}")
    if args.also_docx:
        if result["docx"]:
            print(f"Wrote DOCX: {result['docx']}")
        else:
            print("[WARN] python-docx not installed; skipping .docx export")
    print(f"Section types: {result['type_count']}  Content sections: {result['section_total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
