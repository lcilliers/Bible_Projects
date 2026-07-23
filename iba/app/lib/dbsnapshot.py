"""dbsnapshot.py — pre-write DB snapshots. THE GAP FOUND 2026-07-22: this app had no rollback
mechanism at all — a bug in `candidate.load`'s revalidation pass wrote `decision='exception'`
over 1029 of 1806 `candidate_seed` rows, and the only recovery path was a stale 3-day-old manual
`.bak` file plus a lucky same-morning CSV export via `Export-Tables.ps1`. The researcher's
verdict: this should have existed "from the word go," the way the legacy Bible-study engine
snapshots before its `_apply_*` scripts run. This is that mechanism for the IBA app.

Design, deliberately simple (a file copy, not a real backup system):
  - `snapshot(reason)` copies iba.db to iba/app/db/snapshots/iba-<UTC timestamp>-<reason-slug>.db,
    then prunes down to `retention.snapshot_keep_count` (config-driven, oldest deleted first).
  - Called once per NEW run (`run.py:_ensure_run`, only when the run is first created — a resumed
    paused run does not re-snapshot on every retry) — every run gets a pre-state to revert to,
    not just data-writing ones, since a run's own bug is exactly what a snapshot protects against.
  - Skippable via `IBA_NO_SNAPSHOT=1`, matching the legacy engine's `--no-backup` escape hatch for
    tight loops (e.g. a book-by-book Set-Candidates.ps1 sweep across 66 books) — a snapshot on
    every iteration of a loop is the "back up scripts run in a loop" problem the engine's own
    memory entry already names.
  - A plain file copy, not `VACUUM INTO` or a hot-backup API — iba.db is ~110MB and this runs
    synchronously before work starts, so simplicity over cleverness; WAL mode means the
    connection isn't holding an exclusive lock at rest, so a copy of the base file plus checkpoint
    first is safe (see `_checkpoint_wal`).

    python -m iba.app.lib.dbsnapshot --reason manual-test    # take one now, from the CLI
    python -m iba.app.lib.dbsnapshot --list                  # show what's kept
"""

from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sqlite3
import sys
from pathlib import Path

from .cfg import DB_PATH

SNAPSHOT_DIR = DB_PATH.parent / "snapshots"


def _slug(reason: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", reason or "run").strip("-").lower()
    return s[:40] or "run"


def _checkpoint_wal(db_path: Path) -> None:
    """Flush the WAL into the main db file first, so a plain file copy is a consistent snapshot
    (WAL mode means recent writes may still be sitting in iba.db-wal, not the base file)."""
    try:
        conn = sqlite3.connect(db_path, timeout=5.0)
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        conn.close()
    except sqlite3.Error:
        pass


def snapshot(reason: str = "run", keep: int | None = None) -> Path | None:
    """Copy iba.db to a timestamped snapshot, then prune. Returns the new path, or None if
    IBA_NO_SNAPSHOT=1 (the loop escape hatch) or the DB doesn't exist yet."""
    import os
    if os.environ.get("IBA_NO_SNAPSHOT") == "1":
        return None
    if not DB_PATH.exists():
        return None

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    _checkpoint_wal(DB_PATH)
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = SNAPSHOT_DIR / f"iba-{ts}-{_slug(reason)}.db"
    shutil.copy2(DB_PATH, dest)
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
    a = ap.parse_args()

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
