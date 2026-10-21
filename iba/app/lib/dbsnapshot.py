"""dbsnapshot.py -- database copies: the pre-run rollback snapshot and test copies (#2193).

Every copy is made with SQLite's online backup API (`copy_db`), never a file copy: a file copy of
a WAL-mode database misses writes still in the -wal file, and a checkpoint before it can fail
silently while another connection is busy.

  - `copy_db(dest, src)` -- a consistent copy of `src` (default iba.db) at `dest`. Developer Mode
    tests run against such a copy (cfg_behaviour_rule developer-mode-scope-and-conduct).
  - `snapshot(reason)` -- copies iba.db to iba/app/db/snapshots/iba-<UTC timestamp>-<reason>.db,
    then prunes to `retention.snapshot_keep_count`. Called once per new run (`run.py:_ensure_run`).
    Skipped when IBA_NO_SNAPSHOT=1 (for tight loops, e.g. a book-by-book sweep).

    python -m iba.app.lib.dbsnapshot --reason manual-test    # take a snapshot now
    python -m iba.app.lib.dbsnapshot --list                  # show what's kept
    python -m iba.app.lib.dbsnapshot --copy-to PATH          # a test copy of iba.db at PATH
"""

from __future__ import annotations

import argparse
import datetime
import re
import sqlite3
import sys
from pathlib import Path

from .cfg import DB_PATH

SNAPSHOT_DIR = DB_PATH.parent / "snapshots"


def _slug(reason: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", reason or "run").strip("-").lower()
    return s[:40] or "run"


def copy_db(dest: Path | str, src: Path | str = DB_PATH) -> Path:
    """Copy `src` to `dest` with the SQLite backup API; returns `dest`. Refuses to overwrite."""
    dest = Path(dest)
    if dest.exists():
        raise FileExistsError(f"{dest} already exists")
    dest.parent.mkdir(parents=True, exist_ok=True)
    source = sqlite3.connect(f"file:{Path(src).as_posix()}?mode=ro", uri=True, timeout=30.0)
    target = sqlite3.connect(dest)
    try:
        source.backup(target)
    finally:
        target.close()
        source.close()
    return dest


def snapshot(reason: str = "run", keep: int | None = None) -> Path | None:
    """Copy iba.db to a timestamped snapshot, then prune. Returns the new path, or None if
    IBA_NO_SNAPSHOT=1 (the loop escape hatch) or the DB doesn't exist yet."""
    import os
    if os.environ.get("IBA_NO_SNAPSHOT") == "1":
        return None
    if not DB_PATH.exists():
        return None

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = copy_db(SNAPSHOT_DIR / f"iba-{ts}-{_slug(reason)}.db")
    prune(keep)
    return dest


def prune(keep: int | None = None) -> int:
    """Delete the oldest snapshots beyond `keep` (config-driven default if not passed
    explicitly — read lazily here, not at import time, so this module has no hard Cfg
    dependency for callers that just want a quick snapshot)."""
    if keep is None:
        try:
            from .cfg import Cfg
            c = Cfg()
            keep = int(c.setting("retention.snapshot_keep_count", 20))
            c.close()
        except Exception:
            keep = 20
    if not SNAPSHOT_DIR.exists():
        return 0
    files = sorted(SNAPSHOT_DIR.glob("iba-*.db"), key=lambda p: p.stat().st_mtime, reverse=True)
    removed = 0
    for f in files[keep:]:
        f.unlink()
        removed += 1
    return removed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reason", default="manual")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--copy-to", help="write a test copy of iba.db to this path")
    a = ap.parse_args()

    if a.copy_to:
        print(f"copy: {copy_db(a.copy_to)}")
        return 0

    if a.list:
        if not SNAPSHOT_DIR.exists():
            print("no snapshots yet")
            return 0
        for f in sorted(SNAPSHOT_DIR.glob("iba-*.db")):
            print(f"  {f.name}  ({f.stat().st_size / 1_000_000:.1f} MB)")
        return 0

    path = snapshot(a.reason)
    if path is None:
        print("snapshot skipped (IBA_NO_SNAPSHOT=1, or no DB yet)")
        return 0
    print(f"snapshot: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
