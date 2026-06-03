"""Move category-F live unclustered terms into the FLAG holding grouping.

Researcher direction 2026-06-01: "F live should all be added to the cluster
flagged. We will then process the cluster flagged as a separate exercise."

F = cluster_code IS NULL, delete_flagged=0, status NOT IN
('delete','excluded','candidate_delete'). Pure cluster_code reassignment
(NULL -> 'FLAG'); NO verse_context / verse records touched, nothing deleted.
FLAG is a registered grouping in the `cluster` table (status 'Not started').

DEFAULT IS DRY-RUN. Pass --apply to write.
  python scripts/_repair_flag_f_live_v1_20260601.py
  python scripts/_repair_flag_f_live_v1_20260601.py --apply
"""
import argparse
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")

WHERE = """
  cluster_code IS NULL
  AND COALESCE(delete_flagged,0) = 0
  AND COALESCE(status,'') NOT IN ('delete','excluded','candidate_delete')
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=15)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    ids = [r["id"] for r in cur.execute(f"SELECT id FROM mti_terms WHERE {WHERE}")]
    # sanity: FLAG must exist as a registered grouping
    flag_ok = cur.execute("SELECT COUNT(1) FROM cluster WHERE cluster_code='FLAG'").fetchone()[0]

    print(f"FLAG grouping registered: {bool(flag_ok)}")
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: F-live terms to move NULL -> 'FLAG': {len(ids)}")

    if not a.apply:
        conn.close()
        return
    if not flag_ok:
        raise SystemExit("ABORT: FLAG grouping not registered in cluster table.")

    cur.execute("BEGIN")
    try:
        cur.execute(f"UPDATE mti_terms SET cluster_code='FLAG', last_changed=datetime('now') WHERE {WHERE}")
        n = cur.rowcount
        if n != len(ids):
            conn.rollback()
            raise SystemExit(f"ABORT: UPDATE affected {n}, expected {len(ids)} — rolled back.")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    print(f"APPLIED: moved {n} F-live terms to cluster_code='FLAG'. No evidence rows touched.")
    conn.close()


if __name__ == "__main__":
    main()
