"""encode_2637_cycle_v1_20261126.py -- escalation #2637, plan v3 X6 and X7 (outputs/escalation/2637-build-plan-v3-20261126.md), and B:138 amended.

Researcher 2026-11-26 (Developer Mode), verbatim: "All approved, proceed with 2637" -- approving, with the fixes of #2628 and #2621, the
proposal of #2637 v15: the B:138 run of a routine may be the live standard-session reading of an unread unit, its failures kept in
read_failure and audited, instead of a copy run followed by a live reading.
  cfg_setting      layer.cycle: report_name and package_patterns (the names of the files the package commands write)
  cfg_step         collection.cycle (handlers/collectionbuild.py cycle), its refused routing; it writes only its report
  cfg_behaviour_rule 138: the run on a copy in the building session, or the live reading of the unit, audited by Collection-Build.ps1 -Action Cycle
  cfg_utility      lib/cycleview.py and this migration
Through configmaint.apply_logged; archived after the live apply. Idempotent.
Usage: python iba/app/migration/encode_2637_cycle_v1_20261126.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2637-CYCLE-20261126"
MODULE = "encode_2637_cycle_v1_20261126"
STEP = "collection.cycle"
CYCLE = {"report_name": "collection-cycle",
         "package_patterns": [r"^group-{c}-\d{8}\.json$", r"^layer-{c}-[0-9.]+-\d{8}\.json$",
                              r"^read(words|senses|enrichment|structure|sweep|evidence|elements)-{c}-.+-\d{8}t\d{6}(-part-\d+)?\.(json|md)$",
                              r"^readbehaviours-{c}-\d{8}t\d{6}(-part-\d+)?\.(json|md)$"]}
CYCLE_USE = ("#2637 X6, X7: the cycle view and B:138 audit (Collection-Build.ps1 -Action Cycle, lib/cycleview.py): report_name, the stem of its "
             "report under surfaces.exports_root (versioned); package_patterns, the names of the files the package commands write in "
             "layer.working_dir ({c} the collection's slug); any other file of the collection there fails the audit.")
OLD = "on a database copy made with dbsnapshot.copy_db, in the session that built the change."
NEW = ("either on a database copy made with dbsnapshot.copy_db, in the session that built the change, or as the live reading of that unit in a "
       "standard session, its refusals and crashes kept in read_failure and the run audited by Collection-Build.ps1 -Action Cycle -Since <its start>.")
MESSAGE = "refused, nothing written -- the reason follows (a usage outcome kept in read_failure for learning, not recorded as an escalation; #2637)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key='layer.cycle'").fetchone():
        ops.append(("cfg_setting", "insert", {}, {"key": "layer.cycle", "value": json.dumps(CYCLE), "use": CYCLE_USE, "module": "layer", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (STEP,)).fetchone():
        ordinal = conn.execute("SELECT coalesce(max(ordinal),0)+1 FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
        ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": ordinal, "step": STEP, "handler": "iba.app.handlers.collectionbuild:cycle",
                                               "scope": "none", "does": "the reading cycle of a collection or subgroup (steps, ledger, packages, refusals) and the B:138 audit of a run, as a versioned report -- see lib/cycleview.py (escalation #2637 X6, X7)",
                                               "inactive": 0, "kind": "operations"}))
    if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", (STEP,)).fetchone():
        ops.append(("cfg_on_fail", "insert", {}, {"step": STEP, "condition": "refused", "path": "report-continue", "resolver": None, "message": MESSAGE, "route": "terminal", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name='read_failure'", (STEP,)).fetchone():
        ops.append(("cfg_write_grant", "insert", {}, {"writer": STEP, "table_name": "read_failure", "database": "iba", "inactive": 0}))
    text = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=138").fetchone()[0]
    if OLD in text:
        ops.append(("cfg_behaviour_rule", "update", {"id": 138}, {"rule_text": text.replace(OLD, NEW)}))
    for mod, path, purpose, inactive, ex, why in [
            ("cycleview", "iba/app/lib/cycleview.py", "#2637 X6, X7: the reading cycle view and the B:138 audit of a run", 0, 0, None),
            (MODULE, f"iba/app/migration/{MODULE}.py", "migration of #2637 X6/X7 and the B:138 amendment", 1, 1, "a one-off migration; its values are the config it writes")]:
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (mod,)).fetchone():
            ops.append(("cfg_utility", "insert", {}, {"module": mod, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": ex,
                                                      "config_exempt_reason": why, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        return 0
    for t, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t, op, where, set_)
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    if pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve():
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
