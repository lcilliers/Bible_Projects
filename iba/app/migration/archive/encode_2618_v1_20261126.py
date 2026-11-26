"""encode_2618_v1_20261126.py -- escalations #2618 and #2576 (researcher 2026-11-26: "you can clear them, but you MUST change the core methods to take
care of the issues discovered. Any action taken outside of the scope of the packages methods MUST be encoded into the packages ...").

Registers in config what the session did by hand, so that it runs from the app across sessions:
  cfg_step          collection.release_dead_traces (Collection-Build -Action ReleaseDeadTraces: every live trace to a deleted observation dropped, logged)
  cfg_write_grant   the tables it writes (ib_node, ib_observation_change)
  cfg_setting       layer.read_types: the 3.1 read keeps B:72 (the meaning of the routes A, B, C of a party finding) beside its method rules
  cfg_method_rule   RG-06 names where the routes are defined (cfg_behaviour_rule 72)
  cfg_behaviour_rule 137 core-methods-absorb-every-intervention: the researcher's instruction of 2026-11-26, with its scope row
  cfg_utility       six rows naming a file that is gone or moved to archive/ (pointed at the archive copy, or deleted when the file is gone);
                    this migration's own row
Written through configmaint.apply_logged. Named snapshot before a live apply; after the live apply the file archives itself
(configmaint.archive_migration). Idempotent.
Usage: python iba/app/migration/encode_2618_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2618-ENCODE-20261126"
MODULE = "encode_2618_v1_20261126"
STEP = ("collection.release_dead_traces", "iba.app.handlers.collectionbuild:release_dead_traces", "operations",
        "every live trace node that points at a deleted observation, in any collection, dropped with its reason and logged on its holder (a "
        "trace to a deleted observation supports nothing); a named snapshot first; -Check counts -- see lib/validationactions.py "
        "release_dead_traces (escalation #2618)")
GRANTS = ["ib_node", "ib_observation_change"]
RG06 = ("Record the parties: who bears the act, who causes it, who is acted on (source, target, impact, purpose), and the route (cfg_enum "
        "observation_route), whose meaning is cfg_behaviour_rule 72 (route-verses-hib-other-beings-data-only): A another being in its own "
        "right, B another being with the human inner being, C no bearing, data only; a verse may take A and B. A non-human being is never "
        "itself a HIB; a collective stays one HIB; an implied party is named as referential, never asserted.")
RULE = {
    "id": 137, "class": "development", "rule_key": "core-methods-absorb-every-intervention",
    "rule_text": ("Every action taken in a session outside the methods of the app's packages is encoded back into those packages before the work "
                  "is called done: a missed rule, a wrong reading of a rule, a row left dangling in any table and not processed, and anything the "
                  "validation turns up become standard repeatable code or config (a step, a check, a recorder rule, a read instruction) that "
                  "runs across sessions and chats over months. A one-off repair is made through that code, not beside it. Claude may change "
                  "the core code in a chat session only to make it such repeatable code."),
    "source": ('researcher, 2026-11-26, #2618, verbatim: "you can clear them, but you MUST change the core methods to take care of the issues '
               'discovered. Any action taken outside of the scope of the packages methods MUST be encoded into the packages. This included any '
               'missed rules, incorrect interpretations of the rules, any items in any tables that is dangling around and not processed. It '
               'includes any discoveries through the validation process. All these events will highlight items that must be flushed back in the '
               'core code. In essense, while you have the liberty to intervene in the core code in a chat mode, it must always be as a result of '
               'standard repeatable code that will run accross sessions and chats over many months"'),
    "enforced_by": ("session-close SC16 (a repeated failure is fixed at the point of use) and SC10 (every changed code file named in BUILD.md); "
                    "configmaint.validate (find_utility_paths_missing, find_unregistered_project_scripts); otherwise by Claude's own conduct"),
    "active": 1, "enforcement_status": "partially_enforced", "deliver_when": "always",
}
UTILITY_FIX = {  # module -> new file_path, or None to delete the row (the file is gone)
    "research_VE_lexical_faculty_map_build_build_batch4": "research/archive/VE-lexical/faculty-map-build/_build_batch4.py",
    "research_VE_lexical_faculty_map_build_classify_batch1": "research/archive/VE-lexical/faculty-map-build/_classify_batch1.py",
    "schema_overview": "iba/app/tools/archive/build_schema_overview_report.py",
    "iba_app_ps_archive_word-audit": None,
    "reading_reopen_2331_v1_20261030": "iba/app/migration/archive/reading_reopen_2331_v1_20261030.py",
    "analysis_phase_1_2329_v3_20261030": "iba/app/migration/archive/analysis_phase_1_2329_v3_20261030.py",
}


def plan(conn):
    ops = []
    step, handler, kind, does = STEP
    if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
        top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0] + 1
        ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top, "step": step, "handler": handler, "scope": "none",
                                              "does": does, "inactive": 0, "kind": kind}))
    for t in GRANTS:
        if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (step, t)).fetchone():
            ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": t, "database": "iba", "inactive": 0}))
    types = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    if "B:72" not in types["elements"]["rules"]:
        types["elements"] = {**types["elements"], "rules": types["elements"]["rules"] + ["B:72"]}
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(types, ensure_ascii=False)}))
    if conn.execute("SELECT rule_text FROM cfg_method_rule WHERE rule_key='RG-06 parties-and-route'").fetchone()[0] != RG06:
        ops.append(("cfg_method_rule", "update", {"rule_key": "RG-06 parties-and-route"}, {"rule_text": RG06}))
    if not conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", (RULE["rule_key"],)).fetchone():
        if conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE id=?", (RULE["id"],)).fetchone():
            raise SystemExit(f"cfg_behaviour_rule id {RULE['id']} is taken by another rule: re-number before applying")
        ops.append(("cfg_behaviour_rule", "insert", {}, {**RULE, "added_at": "2026-11-26T08:00:00Z"}))
    if not conn.execute("SELECT 1 FROM cfg_rule_scope WHERE rule_ref='B:137'").fetchone():
        ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": "B:137", "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    for module, new in UTILITY_FIX.items():
        row = conn.execute("SELECT file_path FROM cfg_utility WHERE module=?", (module,)).fetchone()
        if row is None:
            continue
        if new is None:
            ops.append(("cfg_utility", "delete", {"module": module}, {}))
        elif row[0] != new:
            ops.append(("cfg_utility", "update", {"module": module}, {"file_path": new}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2618/#2576: ReleaseDeadTraces registered, B:72 in the 3.1 read, RG-06 names the routes, rule 137, dangling utility rows",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2618-encode-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    if live:
        new = archive_migration(conn, RUN_ID, __file__)
        conn.commit()
        print(f"archived: {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
