"""verse_scope_2228_v1_20261022.py -- escalation #2228, tool 1: the scope resolver as config
(design outputs/escalation/2228-scope-resolver-design-v1-20261022.md, approved 2026-10-22).

- work package verse-scope (iba/app/ps/Verse-Scope.ps1) and its one step verse_scope.resolve, with its
  'refused' route; no write grant (it writes no table).
- the output folder setting verse_scope.output_dir, and its module verse_scope in cfg_enum config_module
  (missed on the first apply: configmaint.validate found it, escalation #2234).
- the three new files registered in cfg_utility.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/verse_scope_2228_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2228-VERSE-SCOPE-20261022"
MODULE = "verse_scope_2228_v1_20261022"
WP = "verse-scope"
STEP = "verse_scope.resolve"
DOES = ("the scope resolver: any request (cluster, subgroup, strand, word, strong -- a bare code decomposed to its "
        "derivatives -- verse references, narrative chapter or block, claim, observation, thread item or thread, "
        "request file) -> the collection of verses as JSON, each verse with its routes, everything not resolved "
        "listed; -OnlyStrong narrows it (read-only) -- see lib/versescope.py (escalation #2228)")
EXEMPT = ("pure SQL resolver over verse_lexical, the grouping tables, the narrative register and the thread items: "
          "no value in it is a setting; its one setting (verse_scope.output_dir) is read by the handler (same class "
          "as lexicalscope, #2207 decision 1a)")
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
UTILITIES = [
    ("versescope", "iba/app/lib/versescope.py", "versescope.py -- the scope resolver (escalation #2228): any "
     "request -> the collection of verses with the route that brought each in; bare Strong's codes decomposed to "
     "their derivatives (cfg_behaviour_rule bare-strong-decomposed-to-derivatives). Read-only.", 1, EXEMPT),
    ("handlers_versescope", "iba/app/handlers/versescope.py", "handlers/versescope.py -- the run.py handler for "
     "work package verse-scope (Verse-Scope.ps1); merges -File with the command line and writes the JSON under "
     "verse_scope.output_dir; the logic is in lib/versescope.py (escalation #2228).", 0, None),
    ("Verse-Scope.ps1", "iba/app/ps/Verse-Scope.ps1", "PS entry point for the scope resolver (escalation #2228); "
     "dispatches through run.py, work package verse-scope.", 1,
     "thin wrapper; config is read by the handler through run.py"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Verse-Scope.ps1",
                                                       "runs_over": "none", "chained": 0, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step=?", STEP):
        ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": 0, "step": STEP,
                                               "handler": "iba.app.handlers.versescope:resolve", "scope": "none",
                                               "does": DOES, "inactive": 0, "kind": "utility"}))
    if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", STEP):
        ops.append(("cfg_on_fail", "insert", {}, {"step": STEP, "condition": "refused", "path": "report-continue",
                                                  "resolver": None, "message": REFUSED, "route": "terminal",
                                                  "inactive": 0}))
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='verse_scope'"):
        n = conn.execute("SELECT coalesce(max(ordinal), 0) + 1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "verse_scope", "ordinal": n,
                                               "inactive": 0}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='verse_scope.output_dir'"):
        ops.append(("cfg_setting", "insert", {}, {
            "key": "verse_scope.output_dir", "value": '"outputs/verse-scope"', "module": "verse_scope",
            "inactive": 0, "use": "where Verse-Scope.ps1 writes each verse collection as <label>-<YYYYMMDD>.json, "
                                  "versioned and archived by lib/filingkit (escalation #2228)"}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    if has("SELECT 1 FROM cfg_utility WHERE module='versescope' AND config_exempt=0"):   # first apply wrote 0
        ops.append(("cfg_utility", "update", {"module": "versescope"}, {"config_exempt": 1,
                                                                        "config_exempt_reason": EXEMPT}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2228: work package verse-scope, its step, route and "
                       f"setting, the three new files; run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
