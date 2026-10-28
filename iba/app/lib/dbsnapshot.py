"""dbsnapshot.py -- database copies: the rollback points and test copies (#2193, #2301).

Every copy is made with SQLite's online backup API (`copy_db`), never a file copy: a file copy of
a WAL-mode database misses writes still in the -wal file, and a checkpoint before it can fail
silently while another connection is busy.

The rollback method is cfg_setting backup.rollback_method (the objective: a rollback can always be
made, without a full copy of the database for every run, which is slow and used up the kept copies
within minutes):
  - a run snapshot is taken before a new run only when the newest one is older than min_interval_minutes;
  - run snapshots are kept as the newest keep_recent plus the newest of each of the last keep_daily calendar days (today included);
  - a named snapshot (`--named`, taken on purpose before a migration or a bulk change) is kept in its own
    folder, never pruned by the run snapshots, the newest keep_named kept.
Between two snapshots the changes are in the change records (cfg_change_detail, ib_observation_change,
escalation_history), the reading files and git; the NAS keeps a daily copy (backup.nas_db_backup_schedule).

  - `copy_db(dest, src)` -- a consistent copy of `src` (default iba.db). Developer Mode tests run against
    such a copy (cfg_behaviour_rule developer-mode-scope-and-conduct).
  - `snapshot(reason, named=False)` -- a run snapshot (or a named one) under iba/app/db/snapshots, then
    pruned. Run snapshots are asked for once per new run (`run.py:_ensure_run`); skipped when
    IBA_NO_SNAPSHOT=1 (for tight loops, e.g. a book-by-book sweep).

    python -m iba.app.lib.dbsnapshot --reason pre-2301 --named   # a named rollback point, before a risky change
    python -m iba.app.lib.dbsnapshot --list                      # show what is kept
    python -m iba.app.lib.dbsnapshot --prune                     # apply the retention now
    python -m iba.app.lib.dbsnapshot --copy-to PATH              # a test copy of iba.db at PATH
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


def _rule() -> dict:
    """cfg_setting backup.rollback_method (governance.rules_must_be_config_driven): read at the moment of use from the database at
    DB_PATH, so this module has no hard Cfg dependency for a caller that only wants a copy."""
    from .cfg import Cfg
    c = Cfg(DB_PATH)
    try:
        return c.required_setting("backup.rollback_method")
    finally:
        c.conn.close()


_TS = re.compile(r"^iba-(\d{8})T(\d{6})Z")


def _when(f: Path) -> datetime.datetime:
    m = _TS.match(f.name)
    if m:
        return datetime.datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S").replace(tzinfo=datetime.timezone.utc)
    return datetime.datetime.fromtimestamp(f.stat().st_mtime, datetime.timezone.utc)


def _files(folder: Path) -> list[Path]:
    """The snapshots in a folder, newest first."""
    return sorted(folder.glob("iba-*.db"), key=_when, reverse=True) if folder.exists() else []


def snapshot(reason: str = "run", named: bool = False) -> Path | None:
    """A rollback point. A run snapshot is made only when the newest is older than min_interval_minutes; a named one always.
    Returns the new path, or None if nothing was made (IBA_NO_SNAPSHOT=1, no DB yet, or a recent snapshot exists)."""
    import os
    if os.environ.get("IBA_NO_SNAPSHOT") == "1" or not DB_PATH.exists():
        return None
    rule = _rule()
    now = datetime.datetime.now(datetime.timezone.utc)
    ts = now.strftime("%Y%m%dT%H%M%SZ")
    if named:
        dest = copy_db(SNAPSHOT_DIR / rule["named_dir"] / f"iba-{ts}-{_slug(reason)}.db", DB_PATH)
    else:
        newest = _files(SNAPSHOT_DIR)
        if newest and (now - _when(newest[0])) < datetime.timedelta(minutes=rule["min_interval_minutes"]):
            return None
        dest = copy_db(SNAPSHOT_DIR / f"iba-{ts}-{_slug(reason)}.db", DB_PATH)
    prune()
    return dest


def prune() -> int:
    """Apply the retention (backup.rollback_method): the run snapshots keep the newest keep_recent and the newest of each of the
    last keep_daily days; the named snapshots keep the newest keep_named. Sidecar files (-wal, -shm, -journal) whose database is
    gone are removed with it. Returns the number of snapshots removed."""
    rule = _rule()
    removed = 0
    if SNAPSHOT_DIR.exists():
        files = _files(SNAPSHOT_DIR)
        keep = set(files[:rule["keep_recent"]])
        days = []                                   # the calendar days that have a kept snapshot, newest first
        for f in files[:rule["keep_recent"]]:
            if _when(f).date() not in days:
                days.append(_when(f).date())
        for f in files[rule["keep_recent"]:]:
            d = _when(f).date()
            if d not in days and len(days) < rule["keep_daily"]:
                days.append(d)
                keep.add(f)
        for f in files:
            if f not in keep:
                f.unlink()
                removed += 1
        named = _files(SNAPSHOT_DIR / rule["named_dir"])
        for f in named[rule["keep_named"]:]:
            f.unlink()
            removed += 1
        for folder in (SNAPSHOT_DIR, SNAPSHOT_DIR / rule["named_dir"]):
            if folder.exists():
                for side in list(folder.glob("iba-*.db-*")):
                    if not Path(str(side).rsplit(".db-", 1)[0] + ".db").exists():
                        side.unlink()
    return removed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reason", default="manual")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--named", action="store_true", help="a named rollback point (kept apart from the run snapshots)")
    ap.add_argument("--prune", action="store_true", help="apply the retention now")
    ap.add_argument("--copy-to", help="write a test copy of iba.db to this path")
    a = ap.parse_args()

    if a.copy_to:
        print(f"copy: {copy_db(a.copy_to)}")
        return 0

    if a.prune:
        print(f"pruned: {prune()} snapshot(s) removed")
        return 0

    if a.list:
        if not SNAPSHOT_DIR.exists():
            print("no snapshots yet")
            return 0
        for label, folder in (("run", SNAPSHOT_DIR), ("named", SNAPSHOT_DIR / _rule()["named_dir"])):
            for f in _files(folder):
                print(f"  {label:5} {f.name}  ({f.stat().st_size / 1_000_000:.1f} MB)")
        return 0

    path = snapshot(a.reason, named=a.named)
    if path is None:
        print("snapshot skipped (IBA_NO_SNAPSHOT=1, no DB yet, or a snapshot newer than min_interval_minutes exists)")
        return 0
    print(f"snapshot: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
