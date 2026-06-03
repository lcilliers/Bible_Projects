"""Normalize stale status on now-clustered/T2 live terms.

After the span-rescue + FLAG triage, 35 live terms sit in a real M-cluster or T2
but still read status delete/excluded/candidate_delete (leftover from when they
were wrongly deleted). A live clustered term cannot be 'deleted'. Set status =
'extracted' (base live status) for these. delete_flagged is already 0.

DEFAULT IS DRY-RUN. Pass --apply. Single transaction, rowcount reported.
"""
import argparse
import sqlite3

DB = "database/bible_research.db"
WHERE = "(cluster_code LIKE 'M%' OR cluster_code='T2') AND COALESCE(delete_flagged,0)=0 AND status IN ('delete','excluded','candidate_delete')"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=20); cur = c.cursor()
    n = cur.execute(f"SELECT COUNT(*) FROM mti_terms WHERE {WHERE}").fetchone()[0]
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: rows to set status='extracted': {n}")
    if not a.apply:
        c.close(); return
    cur.execute("BEGIN")
    try:
        cur.execute(f"UPDATE mti_terms SET status='extracted', last_changed=datetime('now') WHERE {WHERE}")
        upd = cur.rowcount
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: {upd} rows set status='extracted'.")
    c.close()


if __name__ == "__main__":
    main()
