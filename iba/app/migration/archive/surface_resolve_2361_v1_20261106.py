"""surface_resolve_2361_v1_20261106.py -- escalation #2361, stage 3: registers module 4 of 5, surface-resolve.

  config_module  new value `resolve`
  settings       resolve.order ["structure","sibling","ollama","own"], resolve.ai_module "ai_base", resolve.ai_step "base",
                 resolve.protected_states ["confirmed","resolved"] (the values that reproduced the recorded combined base; see lib/surfaceresolve.py)
  work package   surface-resolve, entry Surface-Resolve.ps1, steps resolve.status, resolve.run, resolve.show, their 'refused' conditions, the write
                 grants of resolve.run (surface_term, surface_derivation, surface_event), the utility rows
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.
Writes no surface row: the first Run does (and, because the stage 1b load matches the rule, changes nothing).

Usage:
    python iba/app/migration/surface_resolve_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2361-SURFACE-RESOLVE-20261106"
MODULE = "surface_resolve_2361_v1_20261106"
WP = "surface-resolve"
H = "iba.app.handlers.surfaceresolve"
SETTINGS = [
    ("resolve.order", ["structure", "sibling", "ollama", "own"], "the order in which the evidence for a surface's base is taken (module 4 of 5, resolve, #2361): the "
     "first method that offers a base wins. Structure (the shape of the word) first, a sibling group second, the AI base third, the word itself last. "
     "Reproduced the recorded combined base of 2026-11-04"),
    ("resolve.ai_module", "ai_base", "the ai_call.module of the AI base step whose answers the resolve module reads (#2361)"),
    ("resolve.ai_step", "base", "the ai_call.step of the AI base step whose answers the resolve module reads (#2361)"),
    ("resolve.protected_states", ["confirmed", "resolved"], "the base states the resolve module never changes (#2361): a base the researcher confirmed or "
     "resolved by hand"),
]
STEPS = [
    ("resolve.status", "status", "utility", "how far the stored bases of the surfaces of collection a are from what the evidence decides (read-only) -- see "
     "lib/surfaceresolve.py (escalation #2361)"),
    ("resolve.run", "run", "operations", "decide the base of every surface of collection a from the evidence and write the difference: base fields, accepted "
     "flags, missing own and Ollama evidence rows, computed terms, events; -Check previews -- see lib/surfaceresolve.py (escalation #2361)"),
    ("resolve.show", "show", "utility", "one surface: stored state, the decision and its evidence rows, with -Surface (read-only) -- see lib/surfaceresolve.py "
     "(escalation #2361)"),
]
REFUSED = "refused, nothing written -- a setting is missing, or -Surface is not a live surface (a usage outcome, not recorded as an escalation)"
GRANTS = ["surface_term", "surface_derivation", "surface_event"]
UTILITIES = [
    ("surfaceresolve", "iba/app/lib/surfaceresolve.py", 0, "surfaceresolve.py -- module 4 of 5 of the surface cycle: the base of every surface chosen from the "
     "evidence, reproducing the recorded combined base of 2026-11-04 (escalation #2361).", 0, None),
    ("handlers_surfaceresolve", "iba/app/handlers/surfaceresolve.py", 0, "handlers/surfaceresolve.py -- the run.py handlers for work package surface-resolve "
     "(Surface-Resolve.ps1, escalation #2361).", 1, "thin adapter: every setting is read in lib/surfaceresolve.py (read_settings, through Cfg.setting)"),
    ("Surface-Resolve.ps1", "iba/app/ps/Surface-Resolve.ps1", 0, "PS entry point for module 4 of 5 of the surface cycle (escalation #2361): Status, Run, Show; "
     "dispatches through run.py, work package surface-resolve.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 3: registers module surface-resolve and its settings; "
     f"run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='resolve'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "resolve", "ordinal": nxt, "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": "resolve", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Surface-Resolve.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, fn, kind, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    for t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer='resolve.run' AND table_name=? AND database='iba'", t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": "resolve.run", "table_name": t, "database": "iba", "inactive": 0}))
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-resolve', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_resolve")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE surface_resolve")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_resolve")
        conn.execute("RELEASE surface_resolve")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
