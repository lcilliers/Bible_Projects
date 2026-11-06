"""surface_group_2361_v1_20261106.py -- escalation #2361, stage 2: registers the group repoint of module 1 of 5, surface-group.

  config_module  new value `group`
  settings       group.repoint_apply_kinds ["inflection"], group.repoint_auto_base_groups ["other"]
                 (the values that reproduced the recorded repoint of 2026-11-04: 56 bases changed, 52 pairs held; see lib/surfacegroup.py)
  work package   surface-group, entry Surface-Group.ps1, steps group.status, group.repoint, their 'refused' conditions, the write grants of
                 group.repoint on surface_term, surface_event and surface_flag, the utility rows
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.
Writes no surface row: the recorded corrections are already in the tables (stage 1b); a Repoint run on them proposes nothing new.

Usage:
    python iba/app/migration/surface_group_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2361-SURFACE-GROUP-20261106"
MODULE = "surface_group_2361_v1_20261106"
WP = "surface-group"
H = "iba.app.handlers.surfacegroup"
SETTINGS = [
    ("group.repoint_apply_kinds", ["inflection"], "the kinds of structure hit (cfg_base_construct.result_kind) that may change the group of a base (module 1 of 5, "
     "group, #2361): only an inflection (plural, tense, participle, comparative) keeps the word class, so the group of the derived words carries to the base; any "
     "other kind is held for the researcher. [\"inflection\"] reproduced the recorded repoint of 2026-11-04"),
    ("group.repoint_auto_base_groups", ["other"], "the groups a base may be in for the repoint to correct it without the researcher naming it (#2361): a base judged "
     "other was judged without the sense its derived words show; a base judged being is proposed and corrected only when named with -Base. [\"other\"] reproduced "
     "the recorded repoint (the 3 bases judged being were applied on the researcher's instruction)"),
]
STEPS = [
    ("group.status", "status", "utility", "what the group repoint rule would do with the surfaces of collection a (read-only) -- see lib/surfacegroup.py (escalation #2361)"),
    ("group.repoint", "repoint", "operations", "correct the group of a base from its derived words when they agree and are inflections, hold the other pairs as "
     "held_pair flags; -Check previews; -Base names proposed bases to accept -- see lib/surfacegroup.py (escalation #2361)"),
]
REFUSED = "refused, nothing written -- a setting is missing or -Base names a base the rule does not propose (a usage outcome, not recorded as an escalation)"
GRANTS = ["surface_term", "surface_event", "surface_flag"]
UTILITIES = [
    ("surfacegroup", "iba/app/lib/surfacegroup.py", 0, "surfacegroup.py -- module 1 of 5 of the surface cycle: the group repoint rule, rebuilt from the recorded "
     "repoint of 2026-11-04 and reproducing it (escalation #2361).", 0, None),
    ("handlers_surfacegroup", "iba/app/handlers/surfacegroup.py", 0, "handlers/surfacegroup.py -- the run.py handlers for work package surface-group "
     "(Surface-Group.ps1, escalation #2361).", 0, None),
    ("Surface-Group.ps1", "iba/app/ps/Surface-Group.ps1", 0, "PS entry point for module 1 of 5 of the surface cycle (escalation #2361): Status, Repoint; dispatches "
     "through run.py, work package surface-group.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 2: registers the group repoint, its settings; "
     f"run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='group'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "group", "ordinal": nxt, "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": "group", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Surface-Group.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, fn, kind, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    for t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer='group.repoint' AND table_name=? AND database='iba'", t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": "group.repoint", "table_name": t, "database": "iba", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
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
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-group', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_group")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE surface_group")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_group")
        conn.execute("RELEASE surface_group")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
