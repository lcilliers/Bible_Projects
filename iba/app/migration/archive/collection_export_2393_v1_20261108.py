"""collection_export_2393_v1_20261108.py -- escalation #2393: registers the two #2379 CSV exports as steps of work package collection-build.

  settings   collection.export_tiers, surfaces.export_groups (the exports folder is the live surfaces.exports_root)
  steps      collection.export_members, collection.export_surfaces (Collection-Build.ps1 -Action ExportMembers / ExportSurfaces), each with its 'refused' condition
  utilities  lib/collectionexport.py, this migration, and the purpose of Collection-Build.ps1 brought up to date
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/collection_export_2393_v1_20261108.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2393-COLLECTION-EXPORT-20261108"
MODULE = "collection_export_2393_v1_20261108"
WP = "collection-build"
H = "iba.app.handlers.collectionbuild"
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
SETTINGS = [
    ("collection.export_tiers", ["core", "synonym", "opposite"],
     "the tiers of a collection that count as its members in the CSV exports of the surface work (#2393); possible_opposite, associated and set_aside are listed apart and are not members",
     "collection"),
    ("surfaces.export_groups", ["behaviour", "inner_being_state"],
     "the surface groups the surfaces export covers (#2393), with the surfaces that have no group yet (not yet judged); entity and other are outside it",
     "surfaces"),
]
STEPS = [
    (8, "collection.export_members", "export_members", "write a CSV of the member surfaces of the collections to the exports folder, one row for each verse, cluster and tier, with the verse "
     "text, with -Name (a view, never an input; the #2379 members-verses file) -- see lib/collectionexport.py (escalation #2393)"),
    (9, "collection.export_surfaces", "export_surfaces", "write a CSV of the surfaces of the behaviour and inner-being-state groups to the exports folder, one row for each verse and "
     "cluster, with the collection and tier of each membership, with -Name (a view, never an input; the #2379 surfaces file) -- see lib/collectionexport.py (escalation #2393)"),
]
UTILITIES = [
    ("collectionexport", "iba/app/lib/collectionexport.py", 0, "collectionexport.py -- the two #2379 CSV views of the surface work (members with verses; surfaces with collections), "
     "reproducible on demand from the tables (escalation #2393).", 1, "the tiers and groups are read from cfg_setting by the handler; the code holds no tunable value"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2393: registers the two #2379 CSV exports as steps of collection-build; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
PS_PURPOSE = ("PS entry point for module 5 of 5 of the surface cycle (escalation #2361): Status, Links, Show, Export, ExportMembers, ExportSurfaces, Set, Merge, Seed, Ask; "
              "dispatches through run.py, work package collection-build.")


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    for ordinal, step, fn, does in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": ordinal, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module='Collection-Build.ps1' AND purpose=?", PS_PURPOSE):
        ops.append(("cfg_utility", "update", {"module": "Collection-Build.ps1"}, {"purpose": PS_PURPOSE}))
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2393-collection-export', named=True)}")
    try:
        conn.execute("SAVEPOINT collection_export")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE collection_export")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO collection_export")
        conn.execute("RELEASE collection_export")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
