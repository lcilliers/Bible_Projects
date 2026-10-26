"""node_resolve_config_2308_v1_20261026.py -- escalation #2308 (researcher, chat 2026-10-26: the sub_group codes missing
on nodes are to be looked up through the strong and the verse, for the migrated nodes and the earlier clusters' nodes).

1. Work package node-resolve (iba/app/ps/Node-Resolve.ps1) with steps node_resolve.plan (read-only) and
   node_resolve.apply (handlers/noderesolve.py), the routed condition 'refused' and apply's write grant on ib_node.
2. Setting node_resolve.output_dir, enum config_module node_resolve.
3. Method rules NR-01 to NR-06 on node_resolve.apply.
4. cfg_utility for lib/noderesolve.py, handlers/noderesolve.py, Node-Resolve.ps1 and this script.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.
One transaction.

Usage:
    python iba/app/migration/node_resolve_config_2308_v1_20261026.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2308-NODE-RESOLVE-CONFIG-20261026"
MODULE = "node_resolve_config_2308_v1_20261026"
WP = "node-resolve"
SEE = "see lib/noderesolve.py (escalation #2308)"
STEPS = [  # step, ordinal, kind, does, grants
    ("node_resolve.plan", 0, "utility", "what the sweep would fill on ib_node (occurrence, morph code, sub_group code, looked "
     "up through the strong and the verse) and what it cannot fill, with the reason; writes the plan JSON and a report "
     "(read-only)", []),
    ("node_resolve.apply", 1, "operations", "the plan written to ib_node, node by node, only into null columns and only "
     "where the node still holds what the plan saw", ["ib_node"]),
]
ON_FAIL = {"refused": ("report-continue", "refused, nothing written -- the reason follows (a usage outcome, not "
                       "recorded as an escalation)")}
SETTINGS = [("node_resolve.output_dir", json.dumps("outputs/node-resolve"),
             "#2308: where the sweep's plan JSON files and reports are written (versioned per day by lib/filingkit)")]
RULES = [
    ("NR-01 resolve-from-the-tables", "A node that names a strong and a verse is resolved from the tables, never from a "
     "document: the occurrences of the strong in the verse (verse_lexical), and the sub_group of the occurrence's surface "
     "in the node's cluster (surface_subgroup, cluster_subgroup)."),
    ("NR-02 one-occurrence-fills-the-occurrence", "Where the strong occurs once in the verse, the node takes that "
     "occurrence's verse_lexical_id and, if it has none, its morph_code."),
    ("NR-03 several-occurrences-need-the-surface", "Where the strong occurs more than once in the verse, the node takes an "
     "occurrence only if its own surface matches exactly one of them; otherwise it has no verse_lexical_id and is listed."),
    ("NR-04 subgroup-only-where-the-occurrences-agree", "The node takes the sub_group of its occurrence's surface. Where "
     "the occurrence is not unique, the node takes the sub_group only if every candidate occurrence gives the same one; "
     "where they differ, or no sub_group is defined for the strong in the cluster or for the surface, the node is left and "
     "listed with the reason."),
    ("NR-05 never-overwrite", "A value already on a node is never overwritten: the sweep fills null columns only."),
    ("NR-06 plan-then-apply", "The sweep is planned first (a file holding each node's values before and after) and the plan "
     "is applied whole; a node that no longer holds what the plan saw is skipped and listed."),
]
UTILITIES = [
    ("noderesolve", "iba/app/lib/noderesolve.py", "noderesolve.py -- the sweep that resolves the occurrence, morph code and "
     "sub_group of ib_node rows through the strong and the verse: plan, apply, report (#2308, rules NR-01 to NR-06)", 0, None),
    ("handlers_noderesolve", "iba/app/handlers/noderesolve.py", "noderesolve handler -- work package node-resolve: steps "
     "node_resolve.plan and node_resolve.apply (#2308)", 0, None),
    ("Node-Resolve.ps1", "iba/app/ps/Node-Resolve.ps1", "PS entry point of work package node-resolve (#2308): "
     "-Step Plan|Apply -File <plan JSON>", 1, "PS entry point: dispatches through run.py; its settings are the steps' own"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    base = conn.execute("SELECT COALESCE(MAX(ordinal)+1, 0) FROM cfg_enum WHERE name='config_module'").fetchone()[0]
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='node_resolve'"):
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "node_resolve", "ordinal": base, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {
            "name": WP, "ps_script": "iba/app/ps/Node-Resolve.ps1", "runs_over": "none", "chained": 0,
            "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for step, o, kind, does, grants in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {
                "work_package": WP, "ordinal": o, "step": step,
                "handler": f"iba.app.handlers.noderesolve:{step.split('.', 1)[1]}", "scope": "none",
                "does": f"{does} -- {SEE}", "inactive": 0, "kind": kind}))
        for cond, (path, msg) in ON_FAIL.items():
            if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
                ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": path, "resolver": None,
                                                          "message": msg, "route": "terminal", "inactive": 0}))
        for table in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", step, table):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": table, "database": "iba",
                                                              "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": value, "use": use, "module": "node_resolve",
                                                      "inactive": 0}))
    for i, (key, text) in enumerate(RULES):
        if not has("SELECT 1 FROM cfg_method_rule WHERE step='node_resolve.apply' AND rule_key=?", key):
            ops.append(("cfg_method_rule", "insert", {}, {
                "step": "node_resolve.apply", "rule_key": key, "rule_text": text,
                "source_doc": "#2308 and the researcher's instruction 2026-10-26",
                "enforced_by": "iba/app/lib/noderesolve.py", "ordinal": i, "active": 1}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": 0,
                                                      "config_exempt": exempt, "config_exempt_reason": reason,
                                                      "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same "
                                    "class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2308: work package node-resolve, its steps, grant, setting and "
                       f"method rules NR-01 to NR-06; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    print(f"{len(ops)} cfg write(s)")
    if a.dry_run:
        for t, op, where, set_ in ops:
            what = (set_.get("name") or set_.get("value") or set_.get("module") or set_.get("rule_key") or set_.get("step")
                    or set_.get("key") or json.dumps(where))
            print(f"  {op:6} {t:18} {what}")
        return 0
    try:
        conn.execute("SAVEPOINT node_resolve_config")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE node_resolve_config")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO node_resolve_config")
        conn.execute("RELEASE node_resolve_config")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
