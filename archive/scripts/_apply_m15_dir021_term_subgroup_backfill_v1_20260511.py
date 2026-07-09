"""_apply_m15_dir021_term_subgroup_backfill_v1_20260511.py — DB-modifying.

Apply DIR-20260511-M15-021: backfill mti_term_subgroup links.

After DIR-010..019, some terms have active verse_context rows in
sub-groups they are not linked to via mti_term_subgroup. M15-H is the
most visible (G3056 logos verses are in M15-H but the term is not linked
to M15-H), but similar gaps may exist where DIR-014..017 moved verses
across sub-groups.

This directive:
  - Identifies every (mti_term_id, cluster_subgroup_id) pair within M15
    that has at least one active verse_context row
  - Inserts a mti_term_subgroup row for any such pair that does not
    already have one (delete_flagged=0)

It does NOT remove orphan mti_term_subgroup rows (terms that no longer
have verses in a sub-group). That's a separate cleanup if needed.
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
DIRECTIVE_ID = "DIR-20260511-M15-021"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR,
                     f"bible_research_pre_{label}_{today_compact()}.db")
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
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply (M15 mti_term_subgroup backfill)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # Find missing (term, sub-group) pairs
    missing = list(conn.execute("""
        SELECT DISTINCT vc.mti_term_id, vc.cluster_subgroup_id,
               mt.strongs_number, mt.transliteration,
               cs.subgroup_code
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
         WHERE mt.cluster_code = 'M15'
           AND COALESCE(vc.delete_flagged,0) = 0
           AND vc.cluster_subgroup_id IS NOT NULL
           AND NOT EXISTS (
                 SELECT 1 FROM mti_term_subgroup mts
                  WHERE mts.mti_term_id = vc.mti_term_id
                    AND mts.cluster_subgroup_id = vc.cluster_subgroup_id
                    AND COALESCE(mts.delete_flagged,0) = 0
           )
         ORDER BY cs.subgroup_code, mt.strongs_number
    """))
    print(f"Missing (term, sub-group) pairs: {len(missing)}")
    for r in missing:
        print(f"  {r['strongs_number']:>8s} {r['transliteration']:<20s} "
              f"→ {r['subgroup_code']}")
    print()
    if not missing:
        print("Nothing to do.")
        return 0

    if args.live:
        b = take_backup("m15_dir021_term_subgroup_backfill")
        print(f"Backup: {b}")
        print()

    counts = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()
        inserts = 0
        for r in missing:
            cur.execute(
                "INSERT INTO mti_term_subgroup "
                "  (mti_term_id, cluster_subgroup_id, placement_note, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (r["mti_term_id"], r["cluster_subgroup_id"],
                 f"{DIRECTIVE_ID}: backfill — verses present without "
                 f"term-membership", ts, ts),
            )
            inserts += 1
        counts["mti_term_subgroup_inserts"] = inserts
        print(f"Inserted {inserts} mti_term_subgroup rows")

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}; sample: {fkv[:3]}")
        print("FK check: ok")

        # Verify no gaps remain
        remaining = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
             WHERE mt.cluster_code = 'M15'
               AND COALESCE(vc.delete_flagged,0) = 0
               AND vc.cluster_subgroup_id IS NOT NULL
               AND NOT EXISTS (
                     SELECT 1 FROM mti_term_subgroup mts
                      WHERE mts.mti_term_id = vc.mti_term_id
                        AND mts.cluster_subgroup_id = vc.cluster_subgroup_id
                        AND COALESCE(mts.delete_flagged,0) = 0
               )
        """).fetchone()[0]
        print(f"\nVerification: remaining vc rows with missing term-link: "
              f"{remaining} (expected 0)")

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

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:35s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
