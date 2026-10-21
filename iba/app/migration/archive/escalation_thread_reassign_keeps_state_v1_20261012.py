"""escalation_thread_reassign_keeps_state_v1_20261012.py -- escalation #2000, defect D1.

Found in the #2000 test run (test plan v2, 2026-10-12): `Update -AssignedTo` alone on a thread fell
through to cfg_escalation_transition priority 7 (assignee_changed) and set state 're-assigned',
which is outside the thread open states (on-hold, in-progress), so the thread dropped out of
Thread/Match/ThreadCheck. Researcher, verbatim (chat 2026-10-12): "go with option a" -- a
reassignment keeps a thread's state.

Writes one cfg_escalation_transition row (shape manual, priority 6, next_action NULL, condition
thread_reassigned -> __unchanged__), ahead of priority 7 assignee_changed and behind the approval
rows. The condition itself is lib/escalation.py _condition_true 'thread_reassigned'. No schema
change, so no cfg_table/cfg_column change.

Idempotent: the insert is guarded on (shape, condition_key). One transaction.

Usage:
    python iba/app/migration/escalation_thread_reassign_keeps_state_v1_20261012.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

ROW = (6, "manual", None, "thread_reassigned", "__unchanged__",
       "escalation #2000 D1 (researcher, 2026-10-12: 'go with option a'): reassigning a thread "
       "keeps its state. Without this, a bare -AssignedTo on a thread fell to priority 7 "
       "(assignee_changed) and landed on re-assigned, outside the thread open states, so the "
       "thread dropped out of Thread/Match/ThreadCheck. Ahead of priority 7, behind the approval "
       "rows (priorities 1-5). Shares priority 6 with explicit_state_given; both resolve to "
       "__unchanged__, so their order does not matter.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        prio, shape, na, cond, key, notes = ROW
        if cur.execute("SELECT 1 FROM cfg_escalation_transition WHERE shape=? AND condition_key=?",
                       (shape, cond)).fetchone():
            cur.execute("UPDATE cfg_escalation_transition SET priority=?, resulting_status_key=?, "
                        "notes=? WHERE shape=? AND condition_key=?", (prio, key, notes, shape, cond))
            report.append(f"cfg_escalation_transition {cond} already present -- refreshed")
        else:
            cur.execute("INSERT INTO cfg_escalation_transition (priority, shape, next_action, "
                        "condition_key, resulting_status_key, notes, active) VALUES (?,?,?,?,?,?,1)",
                        (prio, shape, na, cond, key, notes))
            report.append(f"cfg_escalation_transition {cond} inserted (priority {prio})")
        if args.dry_run:
            conn.rollback()
            report.append("DRY RUN -- rolled back, nothing written")
        else:
            conn.commit()
            report.append("committed")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
