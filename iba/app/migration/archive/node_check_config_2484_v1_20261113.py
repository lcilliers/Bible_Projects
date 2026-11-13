"""node_check_config_2484_v1_20261113.py -- escalation #2484: the node and observation checker, registered.

1. Work package node-check (iba/app/ps/Node-Check.ps1) with step node_check.report (utility, read-only: no write grant; handlers/nodecheck.py).
2. Setting node_check.output_dir (_analytics/reading-tools/node-check, behaviour rule B:128) and enum config_module node_check.
3. Method rules NC-01 to NC-04 on node_check.report.
4. cfg_utility for lib/nodecheck.py, handlers/nodecheck.py, Node-Check.ps1 and this script.
The folder is registered in folder_purpose with FolderPurpose.ps1 -Action Set (type results) in the same unit of work, after this run.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Refuses to run twice. One transaction.
Usage: python -m iba.app.migration.node_check_config_2484_v1_20261113 [--db PATH] [--dry-run]"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2484-NODE-CHECK-CONFIG-20261113"
MODULE = "node_check_config_2484_v1_20261113"
WP = "node-check"
STEP = "node_check.report"
SEE = "see lib/nodecheck.py (escalation #2484)"
RULES = [
    ("NC-01 reads-only", "The checker reads the live tables and writes nothing to any table: its step has no write grant. Its output is a Markdown report and a "
     "workbook, one sheet for each check, filed in node_check.output_dir."),
    ("NC-02 findings-state-what-is-wrong-not-what-to-do", "A finding states what is wrong or missing, from the stored rows. A candidate that needs a reading (an "
     "observation repeating the verse text) is marked 'to be read' and is not judged."),
    ("NC-03 member-surfaces-by-the-shared-reader", "The member surfaces of the live collections are read by the shared reader (collectionexport._memberships: a "
     "surface's own link, else its base), so the checker, the exports and the node column agree. A verse is in scope when it holds an occurrence of a member surface."),
    ("NC-04 every-check-is-a-part-of-a-rule", "Each check is a part of behaviour rule B:130 (nodes) or B:131 (observations) and is named with its rule; a part of a rule "
     "that is not yet checked is added here, never judged by hand."),
]
UTILITIES = [
    ("nodecheck", "iba/app/lib/nodecheck.py", "nodecheck.py -- the node and observation checker: every live node and observation against behaviour rules B:130 and "
     "B:131, by check, read-only (#2484, rules NC-01 to NC-04)", 0, None),
    ("handlers_nodecheck", "iba/app/handlers/nodecheck.py", "nodecheck handler -- work package node-check: step node_check.report (#2484)", 0, None),
    ("Node-Check.ps1", "iba/app/ps/Node-Check.ps1", "PS entry point of work package node-check (#2484): -Step Report", 1,
     "PS entry point: dispatches through run.py; its settings are the step's own"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    base = conn.execute("SELECT COALESCE(MAX(ordinal)+1, 0) FROM cfg_enum WHERE name='config_module'").fetchone()[0]
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='node_check'"):
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "node_check", "ordinal": base, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Node-Check.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step=?", STEP):
        ops.append(("cfg_step", "insert", {}, {
            "work_package": WP, "ordinal": 0, "step": STEP, "handler": "iba.app.handlers.nodecheck:report", "scope": "none",
            "does": f"every live node and observation against behaviour rules B:130 and B:131, listed by check; writes a report and a workbook (read-only) -- {SEE}",
            "inactive": 0, "kind": "utility"}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='node_check.output_dir'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "node_check.output_dir", "value": json.dumps("_analytics/reading-tools/node-check"),
                                                  "use": "#2484: where the node checker's report and workbook are written (versioned per day by lib/filingkit; rule B:128)",
                                                  "module": "node_check", "inactive": 0}))
    for i, (key, text) in enumerate(RULES):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", STEP, key):
            ops.append(("cfg_method_rule", "insert", {}, {"step": STEP, "rule_key": key, "rule_text": text, "source_doc": "#2484 and the researcher's instruction 2026-11-13",
                                                          "enforced_by": "iba/app/lib/nodecheck.py", "ordinal": i, "active": 1}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2484: work package node-check, its step, setting and method rules NC-01 to NC-04; run_id {RUN_ID}."}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID})")
        return 0
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
