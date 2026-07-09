"""_apply_m26_status_complete_v1_20260511.py — DB-modifying.

Advance cluster.status for M26 from 'Analysis - In Progress' to
'Analysis Completed' (matching M05/M06 precedent), and update
last_updated_date.

Usage:
  python scripts/_apply_m26_status_complete_v1_20260511.py --dry-run
  python scripts/_apply_m26_status_complete_v1_20260511.py --live
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
TARGET_STATUS = "Analysis Completed"
EXPECTED_PRIOR = "Analysis - In Progress"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2

    print(f"Advance M26 cluster.status → {TARGET_STATUS!r}  "
          f"({'DRY-RUN' if args.dry_run else 'LIVE'})")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    r = cur.execute(
        "SELECT cluster_code, status, last_updated_date FROM cluster "
        "WHERE cluster_code = 'M26'"
    ).fetchone()
    if not r:
        print("[ERR] no cluster row for M26")
        return 1
    print(f"  Pre:  status={r['status']!r}  last_updated={r['last_updated_date']}")

    if r["status"] != EXPECTED_PRIOR:
        print(f"  [WARN] expected prior status {EXPECTED_PRIOR!r}; "
              f"got {r['status']!r} — proceeding anyway")

    if args.live:
        b = take_backup("m26_status_complete")
        print(f"  Backup: {b}")

    ts = now_iso()
    cur.execute(
        "UPDATE cluster SET status = ?, last_updated_date = ? "
        "WHERE cluster_code = 'M26'",
        (TARGET_STATUS, ts),
    )
    print(f"  Updated rows: {cur.rowcount}")

    r2 = cur.execute(
        "SELECT cluster_code, status, last_updated_date FROM cluster "
        "WHERE cluster_code = 'M26'"
    ).fetchone()
    print(f"  Post: status={r2['status']!r}  last_updated={r2['last_updated_date']}")

    if args.dry_run:
        conn.rollback()
        print("  DRY-RUN: rolled back.")
    else:
        conn.commit()
        print("  LIVE: COMMIT successful.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
