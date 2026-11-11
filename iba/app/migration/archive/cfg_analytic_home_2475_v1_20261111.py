"""cfg_analytic_home_2475_v1_20261111.py -- escalation #2475: all analytic reports and extracts are filed in _analytics.

  rule      behaviour rule B:128 filing.analytic-reports-and-extracts-in-analytics, with its path scopes; the control map texts of study_output and generated_report say it
  settings  the output folder of each analytic tool points under _analytics (engagement.report_path, cluster.surface_map.output_dir, node_resolve.output_dir,
            prior_capture.output_dir, verse_scope.output_dir, verse_collate.output_dir, open_item.output_dir, reading_index.output_dir)
  utility   this migration
The files are moved by the session (git mv), not here. All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply.
Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_analytic_home_2475_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2475-ANALYTIC-HOME-20261111"
MODULE = "cfg_analytic_home_2475_v1_20261111"
RULE_KEY = "analytic-reports-and-extracts-in-analytics"
RULE_TEXT = ("All analytic reports and extracts are filed under _analytics/, in the folder of their module: the report, check, pairs, plan, extract, export or index that a tool writes "
             "from the study's data (collections, surfaces, engagement, readings, observations, verses) in order to analyse it. The surface cycle and engagement go under "
             "_analytics/surfaces/exports/, the reading-process tools under _analytics/reading-tools/<tool>/. The *.report_path or *.output_dir setting of the tool points there, and the folder "
             "is registered in folder_purpose (type results) in the same unit of work as the tool. outputs/ holds only the app's own operational output (configs, escalations, validations, "
             "the content index, the narrative-register quote checks, cost history, the prose tools). The folder of a report is decided before its first file is written (filing.claude-code-filing-obligations).")
RULE_SOURCE = "researcher, 2026-11-11, escalation #2475, verbatim: 'the instructions should be very clear - all analytic reports and extracts should be filed in analytics'"
RULE_ENF = "not_mechanically_checkable by file path alone; delivered at the path scopes below; the location check of configmaint.validate flags a *_dir/*_path setting that points at a folder that does not exist"
SETTINGS = {
    "engagement.report_path": "_analytics/surfaces/exports",
    "cluster.surface_map.output_dir": "_analytics/surfaces/exports/surface-map",
    "node_resolve.output_dir": "_analytics/reading-tools/node-resolve",
    "prior_capture.output_dir": "_analytics/reading-tools/prior-capture",
    "verse_scope.output_dir": "_analytics/reading-tools/verse-scope",
    "verse_collate.output_dir": "_analytics/reading-tools/verse-collate",
    "open_item.output_dir": "_analytics/reading-tools/open-items",
    "reading_index.output_dir": "_analytics/reading-tools/reading-index",
}
CONTROL = {
    "study_output": ("The study's working files, the narrative chapters as exported from iba.db (governance.narrative_home), and every analytic report and extract of the study's data, "
                     "in the folder of its module (_analytics/surfaces/exports for the surface cycle and engagement, _analytics/reading-tools/<tool> for the reading-process tools): "
                     "rule filing.analytic-reports-and-extracts-in-analytics (B:128)."),
    "generated_report": ("Output a tool writes. Never edited by hand and never a source; regenerated, not maintained. An operational report stays under outputs/; an analytic report or extract "
                         "goes under _analytics/ (B:128)."),
}
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2475: all analytic reports and extracts are filed in _analytics (B:128, eight output settings); run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", RULE_KEY):
        rid = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM cfg_behaviour_rule").fetchone()[0]
        ops.append(("cfg_behaviour_rule", "insert", {}, {"id": rid, "class": "filing", "rule_key": RULE_KEY, "rule_text": RULE_TEXT, "source": RULE_SOURCE, "enforced_by": RULE_ENF,
                                                         "added_at": "2026-11-11T11:45:00Z", "active": 1, "enforcement_status": "context_delivered", "deliver_when": "always"}))
        sid = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM cfg_rule_scope").fetchone()[0]
        for i, glob in enumerate(("outputs/**", "_analytics/**")):
            ops.append(("cfg_rule_scope", "insert", {}, {"id": sid + i, "rule_ref": f"B:{rid}", "scope_kind": "path", "scope_value": glob, "inactive": 0}))
    for key, value in SETTINGS.items():
        cur = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (key,)).fetchone()[0]
        if json.loads(cur) != value:
            ops.append(("cfg_setting", "update", {"key": key}, {"value": json.dumps(value)}))
    for kind, desc in CONTROL.items():
        cur = conn.execute("SELECT description FROM cfg_control_home WHERE kind=?", (kind,)).fetchone()[0]
        if cur != desc:
            ops.append(("cfg_control_home", "update", {"kind": kind}, {"description": desc}))
    module, path, inactive, purpose, exempt, reason = MIGRATION_ROW
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
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
        for t, op, where, set_ in ops:
            print(" ", t, op, where or set_.get("module") or set_.get("rule_key") or set_.get("scope_value"), set_.get("value", ""))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2475-analytic-home', named=True)}")
    try:
        conn.execute("SAVEPOINT analytic_home")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE analytic_home")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO analytic_home")
        conn.execute("RELEASE analytic_home")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
