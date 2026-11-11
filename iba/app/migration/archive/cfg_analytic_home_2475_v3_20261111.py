"""cfg_analytic_home_2475_v3_20261111.py -- escalation #2475: rule B:128 points to the existing rule for per-cluster output instead of standing beside it.

  rule  B:128 analytic-reports-and-extracts-in-analytics: the text says that output relating to one cluster stays in that cluster's folder under _analytics/Clusters, as
        cfg_setting report.cluster_folder_naming_convention already says (#2328), and that B:128 covers the other analytic output; it also says where the one-off report default points
  utility  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_analytic_home_2475_v3_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2475-ANALYTIC-HOME-V3-20261111"
MODULE = "cfg_analytic_home_2475_v3_20261111"
RULE_ID = 128
ADD = (" Output that relates to one cluster stays in that cluster's folder under _analytics/Clusters, as cfg_setting report.cluster_folder_naming_convention already says; "
       "this rule covers the analytic output that is not per cluster. governance.oneoff_report_dir (outputs/) is the default of lib/reportkit.oneoff_path for operational and "
       "escalation-tied one-off reports (filing.tool-report-path-vs-deliverable-document), not for a tool's analytic output.")
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2475: B:128 points to the existing per-cluster output rule; run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    text = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=?", (RULE_ID,)).fetchone()[0]
    if ADD.strip() not in text:
        ops.append(("cfg_behaviour_rule", "update", {"id": RULE_ID}, {"rule_text": text.rstrip() + ADD}))
    module, path, inactive, purpose, exempt, reason = MIGRATION_ROW
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone() is None:
        ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                  "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2475-analytic-home-v3', named=True)}")
    try:
        conn.execute("SAVEPOINT analytic_home3")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE analytic_home3")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO analytic_home3")
        conn.execute("RELEASE analytic_home3")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
