"""engagement_2406_v3_review_close_20261109.py -- escalation #2406 (ruling B of #2411): registers the review step of the engagement work package.

  steps      engagement.review, engagement.close (Engagement.ps1 -Action Review / Close), each with its 'refused' condition
  grants     engagement.close writes ib_observation, ib_node, ib_observation_change
  utilities  the purposes of lib/engagement.py, handlers/engagement.py and Engagement.ps1 brought up to date; this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/engagement_2406_v3_review_close_20261109.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2406-ENGAGEMENT-REVIEW-20261109"
MODULE = "engagement_2406_v3_review_close_20261109"
WP = "engagement"
H = "iba.app.handlers.engagement"
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
STEPS = [
    (5, "engagement.review", "review", "write the review file of -Collection: the verses where every member surface was assessed with no bearing, the items still to be read again (ruling B of #2411) -- see lib/engagement.py (escalation #2406)"),
    (6, "engagement.close", "close", "check the decisions on a review file with -File (-Check previews) and write them in one transaction: confirm no bearing (kept in ib_observation_change), or reopen with a role (the no-bearing node deleted, a new observation node written) -- see lib/engagement.py (escalation #2406)"),
]
GRANTS = [("engagement.close", "ib_observation"), ("engagement.close", "ib_node"), ("engagement.close", "ib_observation_change")]
PURPOSES = {
    "engagement": "engagement.py -- the step before narration: what each surface of a collection does for the inner being: the pull, the check and write of the assessment, the group rule, the review of the no-bearing verses, the report (escalation #2406).",
    "handlers_engagement": "handlers for work package engagement: pull, record, group, review, close, check (escalation #2406).",
    "Engagement.ps1": "PS entry point for the engagement step (escalation #2406): Pull, Record, Group, Review, Close, Check; dispatches through run.py, work package engagement.",
}


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for ordinal, step, fn, does in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": ordinal, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": "operations"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    for writer, table in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", writer, table):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": writer, "table_name": table, "database": "iba", "inactive": 0}))
    for module, purpose in PURPOSES.items():
        if not has("SELECT 1 FROM cfg_utility WHERE module=? AND purpose=?", module, purpose):
            ops.append(("cfg_utility", "update", {"module": module}, {"purpose": purpose}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose":
                    f"ONE-OFF migration -- escalation #2406: registers the engagement review and close steps; run_id {RUN_ID}.", "inactive": 1, "config_exempt": 1,
                    "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                    "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2406-review', named=True)}")
    try:
        conn.execute("SAVEPOINT engagement_review")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE engagement_review")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO engagement_review")
        conn.execute("RELEASE engagement_review")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
