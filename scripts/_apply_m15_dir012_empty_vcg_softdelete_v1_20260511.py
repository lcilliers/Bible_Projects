"""_apply_m15_dir012_empty_vcg_softdelete_v1_20260511.py — DB-modifying.

Apply DIR-20260511-M15-012: soft-delete empty VCGs in M15.

Scope: VCGs that are:
  - Linked via vcg_term to at least one mti_term with cluster_code='M15'
  - Currently active (delete_flagged=0)
  - Have zero active verse_context rows pointing at them (group_id)

For each such VCG:
  - Set verse_context_group.delete_flagged = 1
  - Set all of its vcg_term rows' delete_flagged = 1

This is reversible: setting delete_flagged back to 0 restores the row.
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
DIRECTIVE_ID = "DIR-20260511-M15-020"  # second wave: after DIR-013..019 applied


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
    print(f"{DIRECTIVE_ID} apply (M15 empty VCG soft-delete)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # Identify target VCGs
    targets = list(conn.execute("""
        SELECT vcg.id, vcg.group_code,
               SUBSTR(vcg.context_description, 1, 80) AS descr
          FROM verse_context_group vcg
         WHERE COALESCE(vcg.delete_flagged,0) = 0
           AND EXISTS (
                 SELECT 1 FROM vcg_term vt
                   JOIN mti_terms mt ON mt.id = vt.mti_term_id
                  WHERE vt.vcg_id = vcg.id
                    AND COALESCE(vt.delete_flagged,0) = 0
                    AND mt.cluster_code = 'M15'
               )
           AND NOT EXISTS (
                 SELECT 1 FROM verse_context vc
                  WHERE vc.group_id = vcg.id
                    AND COALESCE(vc.delete_flagged,0) = 0
               )
         ORDER BY vcg.group_code
    """))
    print(f"Target M15 VCGs (active + linked to M15 terms + empty): {len(targets)}")
    for r in targets:
        print(f"  {r['group_code']:<14s} id={r['id']:>5d}  {r['descr']}")
    print()

    if not targets:
        print("Nothing to do.")
        return 0

    if args.live:
        b = take_backup("m15_dir012_empty_vcg_softdelete")
        print(f"Backup: {b}")
        print()

    counts: dict[str, int] = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()
        vcg_ids = [r["id"] for r in targets]
        placeholders = ",".join("?" * len(vcg_ids))

        # Soft-delete the VCGs
        rc_vcg = cur.execute(
            f"UPDATE verse_context_group "
            f"   SET delete_flagged = 1, "
            f"       notes = COALESCE(notes || ' | ', '') || ? "
            f" WHERE id IN ({placeholders}) "
            f"   AND COALESCE(delete_flagged,0) = 0",
            [f"{DIRECTIVE_ID}: soft-deleted (empty after M15-A/B cleanup)"]
            + vcg_ids,
        ).rowcount
        counts["vcgs_soft_deleted"] = rc_vcg

        # Soft-delete their vcg_term link rows
        rc_vt = cur.execute(
            f"UPDATE vcg_term "
            f"   SET delete_flagged = 1, "
            f"       last_updated_date = ? "
            f" WHERE vcg_id IN ({placeholders}) "
            f"   AND COALESCE(delete_flagged,0) = 0",
            [ts] + vcg_ids,
        ).rowcount
        counts["vcg_term_rows_soft_deleted"] = rc_vt

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}; sample: {fkv[:3]}")
        print("FK check: ok")

        # Verification
        print()
        print("VERIFICATION")
        print("-" * 72)
        n_still_active = conn.execute(f"""
            SELECT COUNT(*) FROM verse_context_group
             WHERE id IN ({placeholders})
               AND COALESCE(delete_flagged,0) = 0
        """, vcg_ids).fetchone()[0]
        print(f"  Target VCGs still active: {n_still_active} (expected 0)")
        # Confirm no active vc row points at any of these
        n_orphan_vc = conn.execute(f"""
            SELECT COUNT(*) FROM verse_context
             WHERE group_id IN ({placeholders})
               AND COALESCE(delete_flagged,0) = 0
        """, vcg_ids).fetchone()[0]
        print(f"  Active vc rows still pointing at soft-deleted VCGs: "
              f"{n_orphan_vc} (expected 0)")

        # Post-state summary per M15 sub-group
        print()
        print("Per-sub-group VCG counts after soft-delete (M15):")
        rows = conn.execute("""
            SELECT cs.subgroup_code,
                   COUNT(DISTINCT vcg.id) AS active_vcgs
              FROM cluster_subgroup cs
              LEFT JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id = cs.id
                                  AND COALESCE(mts.delete_flagged,0) = 0
              LEFT JOIN vcg_term vt ON vt.mti_term_id = mts.mti_term_id
                                  AND COALESCE(vt.delete_flagged,0) = 0
              LEFT JOIN verse_context_group vcg ON vcg.id = vt.vcg_id
                                  AND COALESCE(vcg.delete_flagged,0) = 0
             WHERE cs.cluster_code = 'M15'
               AND COALESCE(cs.delete_flagged,0) = 0
             GROUP BY cs.subgroup_code
             ORDER BY cs.subgroup_code
        """).fetchall()
        for r in rows:
            print(f"  {r['subgroup_code']:<14s}  active VCGs linked to its terms: "
                  f"{r['active_vcgs']}")

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
