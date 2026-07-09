"""_apply_cluster_short_name_schema_v1_20260512.py — DB-modifying.

Add `short_name TEXT` column to `cluster` table and populate all 47 rows
with researcher-approved short names (≤15 chars) for use in filenames,
reports, and chat references.

Operations (single transaction):
  Phase 0 — Backup
  Phase 1 — ALTER TABLE cluster ADD COLUMN short_name TEXT (if not present)
  Phase 2 — UPDATE cluster SET short_name = ? for each cluster_code
  Phase 3 — Verify all rows populated, all values ≤15 chars
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
DIRECTIVE_ID = "DIR-20260512-003"

# Researcher-approved short names (≤15 chars each)
SHORT_NAMES = {
    "FLAG": "Flag",
    "M01": "Fear", "M02": "Anger", "M03": "Grief", "M04": "Joy",
    "M05": "Love", "M06": "Hate", "M07": "Shame", "M08": "Pride",
    "M09": "Humility", "M10": "Guilt", "M11": "Repentance",
    "M12": "Purity", "M13": "Truth", "M14": "Deceit",
    "M15": "Wisdom", "M16": "Folly", "M17": "Counsel",
    "M18": "Hope", "M19": "Trust", "M20": "Doubt",
    "M21": "Prayer", "M22": "Praise", "M23": "Strength",
    "M24": "Weakness", "M25": "Life", "M26": "Righteousness",
    "M27": "Evil", "M28": "Envy", "M29": "Desire",
    "M30": "Obedience", "M31": "Faith", "M33": "Peace",
    "M34": "Perseverance", "M35": "Testing", "M36": "Service",
    "M37": "Calling", "M38": "Salvation", "M39": "Blessing",
    "M41": "Remembrance", "M42": "Speech", "M43": "Prophecy",
    "M44": "Relational", "M45": "Transformation", "M46": "Abundance",
    "T2": "Supplementary",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR,
                     f"bible_research_pre_{label}_{today_compact()}.db")
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

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply (cluster.short_name schema + populate)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Pre-flight
    print("PRE-FLIGHT")
    print("-" * 72)
    cols = [r["name"] for r in conn.execute("PRAGMA table_info(cluster)")]
    has_short_name = "short_name" in cols
    print(f"  cluster.short_name already exists: {has_short_name}")

    db_codes = {r["cluster_code"] for r in conn.execute(
        "SELECT cluster_code FROM cluster")}
    missing_in_map = sorted(db_codes - set(SHORT_NAMES))
    missing_in_db = sorted(set(SHORT_NAMES) - db_codes)
    print(f"  cluster rows in DB: {len(db_codes)}")
    print(f"  short_name entries: {len(SHORT_NAMES)}")
    if missing_in_map:
        print(f"  [WARN] DB rows without a proposed short_name: {missing_in_map}")
    if missing_in_db:
        print(f"  [WARN] Proposed short_names with no DB row: {missing_in_db}")

    # Length validation
    too_long = [(k, v) for k, v in SHORT_NAMES.items() if len(v) > 15]
    if too_long:
        print(f"  [ERR] short_name >15 chars: {too_long}")
        return 1
    print(f"  [ok] all proposed short_names ≤15 chars")

    print()
    if args.live:
        b = take_backup("cluster_short_name_schema")
        print(f"Backup: {b}")
        print()

    counts: dict[str, int] = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Phase 1 — ALTER TABLE (idempotent)
        if not has_short_name:
            print("Phase 1 — ALTER TABLE cluster ADD COLUMN short_name TEXT")
            print("-" * 72)
            cur.execute("ALTER TABLE cluster ADD COLUMN short_name TEXT")
            counts["phase1_column_added"] = 1
            print("  Column added")
        else:
            counts["phase1_column_added"] = 0
            print("Phase 1 — column already present; skipping ALTER")

        # Phase 2 — Populate
        print()
        print("Phase 2 — Populate short_name for each cluster_code")
        print("-" * 72)
        updated = 0
        for code, short in sorted(SHORT_NAMES.items()):
            if code not in db_codes:
                continue
            rc = cur.execute(
                "UPDATE cluster SET short_name = ?, last_updated_date = ? "
                " WHERE cluster_code = ?",
                (short, ts, code),
            ).rowcount
            updated += rc
        counts["phase2_rows_updated"] = updated
        print(f"  Updated {updated} cluster rows")

        # Phase 3 — Verify
        print()
        print("Phase 3 — Verify")
        print("-" * 72)
        n_null = conn.execute(
            "SELECT COUNT(*) FROM cluster WHERE short_name IS NULL"
        ).fetchone()[0]
        n_long = conn.execute(
            "SELECT COUNT(*) FROM cluster WHERE LENGTH(short_name) > 15"
        ).fetchone()[0]
        print(f"  rows with NULL short_name: {n_null} "
              f"(expected: {len(missing_in_map)})")
        print(f"  rows with short_name >15 chars: {n_long} (expected 0)")
        if n_long > 0:
            raise RuntimeError(f"{n_long} rows have short_name >15 chars")

        # Sample
        print()
        print("Sample (first 10 by cluster_code):")
        for r in conn.execute(
            "SELECT cluster_code, short_name, description FROM cluster "
            " ORDER BY cluster_code LIMIT 10"
        ):
            print(f"  {r['cluster_code']:<6s} {r['short_name'] or '(NULL)':<15s} "
                  f"| {r['description']}")

        if args.dry_run:
            conn.execute("ROLLBACK")
            print()
            print("DRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print()
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:35s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
