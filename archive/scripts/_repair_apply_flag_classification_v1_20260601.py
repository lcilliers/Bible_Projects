"""Apply the validated FLAG classification to mti_terms (guarded).

Per disposition, on all rows of the strongs currently cluster_code='FLAG':
  - cluster   : cluster_code = target M-code (the new home; routing)
  - t2        : cluster_code = 'T2'
  - set_aside : cluster_code = NULL, status='excluded', exclusion_reason = <reason>,
                delete_flagged LEFT = 0 (NOT soft-deleted -> no verse orphaning;
                "excluded with recorded reason", reversible). [researcher-confirmable]

Validated separately (433/433, 0 errors). Invariant after apply: 0 FLAG rows remain.
DEFAULT IS DRY-RUN. Pass --apply to write. Single transaction.
"""
import argparse
import json
import sqlite3
from collections import Counter

DB = "database/bible_research.db"
JSONF = "Workflow/Clusters/wa-flag-cluster-classification-v1_0-20260601.json"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    cur = c.cursor()
    with open(JSONF, encoding="utf-8") as f:
        rows = json.load(f)["classifications"]

    flag_rows_before = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='FLAG'").fetchone()[0]
    disp = Counter(); affected = 0

    def run(sql, params):
        nonlocal affected
        cur.execute(sql, params);
        return cur.rowcount

    if a.apply:
        cur.execute("BEGIN")
    try:
        for r in rows:
            sn, d, tc, reason = r["strongs"], r["disposition"], r.get("target_clusters", []), r.get("reason", "")
            disp[d] += 1
            if not a.apply:
                continue
            if d == "cluster":
                affected += run("UPDATE mti_terms SET cluster_code=? WHERE strongs_number=? AND cluster_code='FLAG'", (tc[0], sn))
            elif d == "t2":
                affected += run("UPDATE mti_terms SET cluster_code='T2' WHERE strongs_number=? AND cluster_code='FLAG'", (sn,))
            elif d == "set_aside":
                affected += run("UPDATE mti_terms SET cluster_code=NULL, status='excluded', exclusion_reason=?, last_changed=datetime('now') WHERE strongs_number=? AND cluster_code='FLAG'", (reason, sn))
            elif d == "boundary":
                # none in this set; if present, route to first candidate + record (placeholder)
                affected += run("UPDATE mti_terms SET cluster_code=? WHERE strongs_number=? AND cluster_code='FLAG'", (tc[0], sn))
        if a.apply:
            remaining = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code='FLAG'").fetchone()[0]
            if remaining != 0:
                c.rollback(); raise SystemExit(f"ABORT: {remaining} FLAG rows remain after apply (expected 0) — rolled back.")
            c.commit()
    except Exception:
        c.rollback(); raise

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: classifications={len(rows)} | dispositions={dict(disp)}")
    print(f"  FLAG rows before: {flag_rows_before}")
    if a.apply:
        print(f"  rows updated: {affected} | FLAG rows remaining: 0 (asserted)")
    else:
        print("  (dry-run: would update all FLAG rows of the 433 classified strongs; invariant target = 0 FLAG remaining)")
    c.close()


if __name__ == "__main__":
    main()
