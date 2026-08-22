"""Turn an edited prose chapter Markdown file into a PROSE supersede patch.

This script validates routing metadata and generates a patch. It does not
modify the database. Apply the reviewed patch with scripts/apply_session_patch.py.

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
    parser = argparse.ArgumentParser(description="Generate a prose supersede patch from an edited chapter")
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--author", default="researcher")
    args = parser.parse_args()

    cfg = Cfg()
    try:
        result = prosestore.run_import_chapter(cfg, args.input, author=args.author, out=args.out)
    except ValueError as e:
        parser.error(str(e))
        return 2
    finally:
        cfg.close()

    print(f"Patch: {result['path']}")
    print(f"Validated sections: {result['sections']}")
    print("No database changes made; review and apply with scripts/apply_session_patch.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
