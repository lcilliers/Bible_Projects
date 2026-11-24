"""surface_relation_register_2548_v1_20261124.py -- escalation #2548, stage 2: the step set Surface-Relation.ps1 registered.

Registers the work package surface-relation, its five steps (relation.status, .load, .groups, .flag, .validate), their refused routes, the write
grants of the three writing steps and the utility rows of the PS entry point, the handler and the library. Every cfg_* write goes through
configmaint.apply_logged(). Idempotent. One transaction. Writes no data row.

Usage:
    python iba/app/migration/archive/surface_relation_register_2548_v1_20261124.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2548-SURFACE-RELATION-REGISTER-20261124"
MODULE = "surface_relation_register_2548_v1_20261124"
WP = "surface-relation"
H = "iba.app.handlers.surfacerelation:"
STEPS = [
    ("relation.status", "status", "utility", "how far the stored surface relations, network groups and no-pair flags are from what WordNet gives the study "
     "surfaces (read-only) -- see lib/surfacerelation.py (escalation #2548)"),
    ("relation.load", "load", "operations", "write the WordNet pairs of the study surfaces into surface_relation: a changed pair or a pair no longer "
     "linked is flipped to deleted; -Check previews -- see lib/surfacerelation.py (escalation #2548)"),
    ("relation.groups", "groups", "operations", "write the connected groups of the live pairs into surface_network_group, the earlier grouping kept as "
     "deleted; -Check previews -- see lib/surfacerelation.py (escalation #2548)"),
    ("relation.flag", "flag", "operations", "one surface_flag (kind wordnet_no_pair) for each surface of a reviewed list; the list must be exactly the "
     "surfaces with no pair; -File, -Escalation, -Check -- see lib/surfacerelation.py (escalation #2548)"),
    ("relation.validate", "validate", "utility", "compare the WordNet same_base pairs and groups with surface_term.base_id and write a report under the "
     "exports folder; nothing is written to base_id -- see lib/surfacerelation.py (escalation #2548)"),
]
GRANTS = {"relation.load": "surface_relation", "relation.groups": "surface_network_group", "relation.flag": "surface_flag"}
REFUSED = ("refused, nothing written -- a setting is missing, WordNet is not at its folder, or the reviewed list does not match the surfaces with no "
           "pair (a usage outcome, not recorded as an escalation)")
UTILITIES = [
    ("surfacerelation", "iba/app/lib/surfacerelation.py", "surfacerelation.py -- the relations between English surfaces linked by WordNet: scope, pairs, "
     "groups, flags and the check against the study bases (escalation #2548).", 0, None),
    ("handlers_surfacerelation", "iba/app/handlers/surfacerelation.py", "handlers/surfacerelation.py -- the run.py handler for work package "
     "surface-relation: Status, Load, Groups, Flag, Validate (Surface-Relation.ps1, escalation #2548).", 1,
     "thin adapter: every setting is read in lib/surfacerelation.py (read_settings, through Cfg.setting)"),
    ("Surface-Relation.ps1", "iba/app/ps/Surface-Relation.ps1", "PS entry point for the relations between the single-word surfaces (escalation "
     "#2548); dispatches through run.py, work package surface-relation.", 1, "thin wrapper; config is read by the handlers through run.py"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Surface-Relation.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, fn, kind, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?", WP, step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": step, "handler": H + fn, "scope": "none", "does": does,
                                                   "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None,
                                                      "message": REFUSED, "route": "terminal", "inactive": 0}))
    for step, table in GRANTS.items():
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", step, table):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": table, "database": "iba", "inactive": 0}))
    for mod, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", mod):
            ops.append(("cfg_utility", "insert", {}, {"module": mod, "file_path": path, "purpose": purpose, "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2548 stage 2: registers the step set Surface-Relation.ps1; run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
            "as the other Developer Mode migrations", "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t in sorted({o[0] for o in ops}):
            print(f"  {t}: {sum(1 for o in ops if o[0] == t)}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT surface_relation_register")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE surface_relation_register")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_relation_register")
        conn.execute("RELEASE surface_relation_register")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
