"""Search prose_section across all prose books.

Core logic now lives in `iba/app/lib/prosestore.py` (escalation #784, 2026-08-21 — incorporated
into the IBA app; this file is the thin CLI entry point documented in
`docs/prose-store-architecture.md` §8). `DEFAULT_LIMIT` is no longer hardcoded here — it reads
`prose.search_default_limit` from `cfg_setting` (module='prose'), resolving the NON-COMPLIANT
flag from escalation #648.

Examples:
  python scripts/search_prose.py grace
  python scripts/search_prose.py "inner being" --book Programme
    python scripts/search_prose.py grace --out outputs/markdown/grace-prose-search.md
    python scripts/search_prose.py 'grace OR mercy' --fts

The query uses SQLite FTS5 syntax. Results are limited to active,
non-superseded prose sections and include their hierarchy and provenance.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from iba.app.lib.cfg import Cfg
from iba.app.lib import prosestore


def main() -> int:
    parser = argparse.ArgumentParser(description="Search active prose sections with SQLite FTS5")
    parser.add_argument("query", help="text to search, for example grace or \"inner being\"")
    parser.add_argument("--book", help="limit results to a book_label")
    parser.add_argument("--limit", type=int, default=None,
                        help="default: prose.search_default_limit (cfg_setting)")
    parser.add_argument("--fts", action="store_true",
                        help="interpret query as a raw SQLite FTS5 MATCH expression")
    parser.add_argument("--out", type=Path,
                        help="Markdown report path; defaults to outputs/markdown/prose-search-*.md")
    args = parser.parse_args()

    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")

    cfg = Cfg()
    try:
        result = prosestore.run_search(
            cfg, args.query, book=args.book, limit=args.limit, raw_fts=args.fts, out=args.out)
    finally:
        cfg.close()

    print(f"Report: {result['path']}")
    print(f"Matches: showing {result['shown']} of {result['total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
