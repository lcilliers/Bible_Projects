"""backup_db_to_nas.py — consistent off-Drive backup of bible_research.db to the NAS.

Why this exists: the engine's `backups/` folder lives inside the Google-Drive-synced
tree, so a single Drive sync failure can take out the database AND its backups together
(this happened 2026-06-03 — see outputs/markdown/wa-db-loss-incident-20260603.md).
This script writes an INDEPENDENT copy to the NAS, in a different failure domain.

What it does (safe by construction):
  1. Opens the source DB read-only and verifies PRAGMA integrity_check.
     -> If the source is 0 bytes / corrupt, it ABORTS and prunes NOTHING
        (so a broken DB can never overwrite or prune away good backups).
  2. Uses SQLite's online backup API to write a consistent snapshot to a local
     temp file (works even if the DB is mid-write), then integrity-checks the copy.
  3. Moves the verified copy to the NAS with a UTC-timestamped name.
  4. Prunes the NAS folder with a grandfather-father-son retention policy.
  5. Appends a line to a log file on the NAS.

Read-only with respect to the database. Writes only to the NAS target.

Usage:
  python scripts/backup_db_to_nas.py                      # back up the live DB
  python scripts/backup_db_to_nas.py --source PATH        # back up a specific DB
  python scripts/backup_db_to_nas.py --dry-run            # show what would happen
  python scripts/backup_db_to_nas.py --label pre_restore  # tag the filename
"""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# --- Defaults ---------------------------------------------------------------
_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = _ROOT / "database" / "bible_research.db"
DEFAULT_TARGET = Path(r"\\LSUK-SYNRACK\HomeMedia\bible_study_projects\db_backups")
LOG_NAME = "backup_log.txt"

# Retention (grandfather-father-son): a backup is KEPT if it satisfies ANY tier.
KEEP_RECENT = 24   # the N most-recent backups, always
KEEP_DAILY = 30    # newest backup of each of the last D calendar days (UTC)
KEEP_WEEKLY = 26   # newest backup of each of the last W ISO weeks

MIN_PLAUSIBLE_BYTES = 50 * 1024 * 1024  # a real DB is >> 50 MB; guard against stubs

# Local (off-NAS) status + alert. The normal backup_log.txt lives ON the NAS, so when
# the NAS is down the failure leaves no local trace — this writes one and raises alerts.
_STATUS_DIR = Path(r"C:\Users\lerouxc\nas_mirror_logs")
_RC_DETAIL = {
    0: "OK",
    2: "source DB not found",
    3: "source DB implausibly small (possible corruption) — backup refused",
    4: "source DB failed integrity_check — backup refused",
    5: "NAS target unreachable",
    6: "snapshot failed integrity_check",
    7: "NAS copy hash mismatch",
}


def _notify(rc: int) -> None:
    """Write a LOCAL status file and (on failure) raise the rich alert channels."""
    status = "OK" if rc == 0 else "FAIL"
    detail = _RC_DETAIL.get(rc, f"unknown failure rc={rc}")
    try:
        _STATUS_DIR.mkdir(parents=True, exist_ok=True)
        (_STATUS_DIR / "status_dbbackup.txt").write_text(
            f"{status}|{datetime.now().astimezone().isoformat()}|{detail}", encoding="utf-8")
    except OSError:
        pass
    helper = _ROOT / "scripts" / "notify_backup_alert.ps1"
    try:
        subprocess.run(["pwsh", "-NoProfile", "-File", str(helper),
                        "-Job", "dbbackup", "-Status", status, "-Detail", detail],
                       capture_output=True, timeout=120)
    except Exception:
        pass


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _log(target: Path, msg: str, dry: bool) -> None:
    line = f"{datetime.now(timezone.utc).isoformat()}  {msg}"
    print(line)
    if dry:
        return
    try:
        with open(target / LOG_NAME, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError as e:
        print(f"  (warning: could not write log: {e})")


def _integrity_ok(db_path: Path) -> tuple[bool, str]:
    try:
        con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        try:
            row = con.execute("PRAGMA integrity_check").fetchone()
        finally:
            con.close()
        result = (row[0] if row else "").strip()
        return result.lower() == "ok", result
    except sqlite3.Error as e:
        return False, f"sqlite error: {e}"


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _parse_ts(name: str) -> datetime | None:
    # bible_research_YYYYMMDDTHHMMSSZ[...].db
    stem = name[len("bible_research_"):] if name.startswith("bible_research_") else name
    token = stem[:16]  # YYYYMMDDTHHMMSS + 'Z'
    try:
        return datetime.strptime(token, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _select_to_keep(backups: list[tuple[Path, datetime]]) -> set[Path]:
    """Return the set of paths to KEEP under the GFS policy."""
    keep: set[Path] = set()
    ordered = sorted(backups, key=lambda b: b[1], reverse=True)
    # recent
    for p, _ in ordered[:KEEP_RECENT]:
        keep.add(p)
    # daily: newest per UTC date
    seen_days: dict[str, Path] = {}
    for p, dt in ordered:
        key = dt.strftime("%Y-%m-%d")
        if key not in seen_days:
            seen_days[key] = p
    for key in sorted(seen_days, reverse=True)[:KEEP_DAILY]:
        keep.add(seen_days[key])
    # weekly: newest per ISO week
    seen_weeks: dict[str, Path] = {}
    for p, dt in ordered:
        iso = dt.isocalendar()
        key = f"{iso[0]}-W{iso[1]:02d}"
        if key not in seen_weeks:
            seen_weeks[key] = p
    for key in sorted(seen_weeks, reverse=True)[:KEEP_WEEKLY]:
        keep.add(seen_weeks[key])
    return keep


def prune(target: Path, dry: bool) -> None:
    backups: list[tuple[Path, datetime]] = []
    for p in target.glob("bible_research_*.db"):
        dt = _parse_ts(p.name)
        if dt:
            backups.append((p, dt))
    if len(backups) <= KEEP_RECENT:
        return
    keep = _select_to_keep(backups)
    for p, _ in backups:
        if p not in keep:
            _log(target, f"PRUNE {p.name}", dry)
            if not dry:
                try:
                    p.unlink()
                except OSError as e:
                    _log(target, f"  prune failed: {e}", dry)


def main() -> int:
    ap = argparse.ArgumentParser(description="Consistent off-Drive DB backup to the NAS.")
    ap.add_argument("--source", default=str(DEFAULT_SOURCE), help="DB to back up")
    ap.add_argument("--target", default=str(DEFAULT_TARGET), help="NAS backup folder")
    ap.add_argument("--label", default="", help="optional tag added to the filename")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    source = Path(args.source)
    target = Path(args.target)

    if not source.exists():
        print(f"ABORT: source not found: {source}")
        return 2
    size = source.stat().st_size
    if size < MIN_PLAUSIBLE_BYTES:
        print(f"ABORT: source is implausibly small ({size} bytes) — refusing to back up "
              f"a possibly-corrupt/empty DB. Pruning skipped.")
        return 3
    ok, detail = _integrity_ok(source)
    if not ok:
        print(f"ABORT: source failed integrity_check ({detail}). Pruning skipped.")
        return 4
    if not target.exists():
        print(f"ABORT: NAS target unreachable: {target}")
        return 5

    suffix = f"_{args.label}" if args.label else ""
    dest_name = f"bible_research_{_ts()}{suffix}.db"
    dest = target / dest_name

    _log(target, f"START backup of {source} ({size/1024/1024:.1f} MB) -> {dest_name}", args.dry_run)
    if args.dry_run:
        _log(target, "DRY-RUN: would snapshot, verify, move, prune.", args.dry_run)
        prune(target, dry=True)
        return 0

    # 1) consistent snapshot to local temp
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".db", prefix="bibledb_bak_")
    os.close(tmp_fd)
    tmp = Path(tmp_path)
    try:
        src = sqlite3.connect(f"file:{source}?mode=ro", uri=True)
        bak = sqlite3.connect(str(tmp))
        with bak:
            src.backup(bak)
        bak.close()
        src.close()

        # 2) verify the snapshot
        ok, detail = _integrity_ok(tmp)
        if not ok:
            _log(target, f"ABORT: snapshot failed integrity_check ({detail}). No prune.", False)
            return 6

        # 3) move verified snapshot to NAS
        shutil.copy2(tmp, dest)
        # verify the network copy byte-for-byte
        if _sha256(tmp) != _sha256(dest):
            _log(target, "ABORT: NAS copy hash mismatch — removing bad copy. No prune.", False)
            try:
                dest.unlink()
            except OSError:
                pass
            return 7
        _log(target, f"OK backup verified on NAS: {dest_name} ({dest.stat().st_size/1024/1024:.1f} MB)", False)
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass

    # 4) prune
    prune(target, dry=False)
    _log(target, "DONE", False)
    return 0


if __name__ == "__main__":
    rc = main()
    if "--dry-run" not in sys.argv:   # don't let a dry-run overwrite the real status
        _notify(rc)
    sys.exit(rc)
