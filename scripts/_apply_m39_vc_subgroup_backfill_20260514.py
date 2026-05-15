"""M39 — backfill verse_context.cluster_subgroup_id from mti_term_subgroup placement.

Follow-up to dir-002/003 application: the apply script only set verse_context.group_id,
leaving cluster_subgroup_id NULL. The validator C1 check requires
verse_context.cluster_subgroup_id to be populated. This script derives it
deterministically from the term's mti_term_subgroup placement.

Not an analytical change. CC-level data integrity fix.
"""
import sqlite3, sys, os, shutil
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = os.path.join("database", "bible_research.db")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Find verse_context rows for M39 terms where cluster_subgroup_id is NULL
    # but the term has an mti_term_subgroup placement
    rows = list(conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, mts.cluster_subgroup_id AS target_sg
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                                     AND COALESCE(mts.delete_flagged,0)=0
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
         WHERE cs.cluster_code = 'M39'
           AND COALESCE(vc.delete_flagged,0)=0
           AND vc.cluster_subgroup_id IS NULL
    """))
    print(f"Rows needing backfill: {len(rows)}")
    by_sg = {}
    for r in rows:
        by_sg[r["target_sg"]] = by_sg.get(r["target_sg"], 0) + 1
    for sg_id, n in sorted(by_sg.items()):
        sg = conn.execute("SELECT subgroup_code FROM cluster_subgroup WHERE id=?", (sg_id,)).fetchone()
        print(f"  -> sg_id={sg_id} ({sg['subgroup_code']}): {n}")

    if not args.live:
        print("\n[DRY-RUN]")
        return 0

    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    bp = os.path.join(backup_dir,
                      f"bible_research_pre_m39_vc_subgroup_backfill_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    conn.execute("BEGIN")
    cur = conn.cursor()
    cur.executemany(
        "UPDATE verse_context SET cluster_subgroup_id=? WHERE id=?",
        [(r["target_sg"], r["vc_id"]) for r in rows]
    )
    conn.commit()
    print(f"Updated {cur.rowcount} verse_context rows.")
    conn.close()


if __name__ == "__main__":
    sys.exit(main())
