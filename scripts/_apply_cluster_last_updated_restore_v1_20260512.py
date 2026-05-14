"""_apply_cluster_last_updated_restore_v1_20260512.py — DB-modifying.

The short_name migration (DIR-003) wrongly bumped last_updated_date on
every cluster row. Restore the original values from the pre-migration
backup, but preserve the 4 completed clusters' real updates.

Operations:
  Phase 0 — Backup current state
  Phase 1 — Read last_updated_date from backup DB for each cluster
  Phase 2 — UPDATE cluster SET last_updated_date = backup_value
             WHERE cluster_code NOT IN (M05, M06, M15, M26)
            (the 4 completed clusters keep their post-DIR-010..025 dates)
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
BACKUP_SRC = os.path.join(BACKUP_DIR, "bible_research_pre_cluster_short_name_schema_20260512.db")
DIRECTIVE_ID = "DIR-20260512-004"
# Known-correct dates for completed clusters (from their actual status-flip
# timestamps). Override regardless of backup value.
COMPLETED_DATES = {
    "M05": "2026-05-08T02:36:46Z",
    "M06": "2026-05-06T19:02:40Z",
    "M15": "2026-05-12T05:24:13Z",
    "M26": "2026-05-11T04:39:03Z",
}


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{today}.db")
    shutil.copy2(DB_PATH, p)
    return p


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: --dry-run or --live required", file=sys.stderr)
        return 2

    print(f"{DIRECTIVE_ID} apply  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print(f"Backup source: {BACKUP_SRC}")
    if not os.path.exists(BACKUP_SRC):
        print(f"[ERR] backup not found")
        return 1

    # Read original dates from backup
    backup_dates: dict[str, str] = {}
    with sqlite3.connect(BACKUP_SRC) as bc:
        bc.row_factory = sqlite3.Row
        for r in bc.execute("SELECT cluster_code, last_updated_date FROM cluster"):
            backup_dates[r["cluster_code"]] = r["last_updated_date"]
    print(f"Loaded {len(backup_dates)} dates from backup")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if args.live:
        b = take_backup("cluster_last_updated_restore")
        print(f"Pre-restore backup: {b}")

    try:
        conn.execute("BEGIN")
        restored = 0
        completed_fixed = 0
        # Restore non-completed clusters from backup
        for code, original_date in backup_dates.items():
            if code in COMPLETED_DATES:
                continue
            rc = cur.execute(
                "UPDATE cluster SET last_updated_date = ? "
                " WHERE cluster_code = ? AND last_updated_date != ?",
                (original_date, code, original_date),
            ).rowcount
            restored += rc
        # Set the 4 completed clusters to their known-correct dates
        for code, correct_date in COMPLETED_DATES.items():
            rc = cur.execute(
                "UPDATE cluster SET last_updated_date = ? "
                " WHERE cluster_code = ? AND last_updated_date != ?",
                (correct_date, code, correct_date),
            ).rowcount
            completed_fixed += rc
        print(f"Restored {restored} non-completed clusters from backup")
        print(f"Set {completed_fixed} completed clusters to known dates")

        # Sample
        for r in conn.execute("""
            SELECT cluster_code, short_name, status, last_updated_date
              FROM cluster
             WHERE cluster_code IN ('M05','M06','M15','M26','M01','M27','FLAG','T2')
             ORDER BY cluster_code
        """):
            print(f"  {r['cluster_code']:<6s} {r['short_name'] or '':<15s} "
                  f"{r['status']:<22s} {r['last_updated_date']}")

        if args.dry_run:
            conn.execute("ROLLBACK")
            print("\nDRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print("\nLIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
