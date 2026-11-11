"""collection_evidence_2464_v1_20261111.py -- escalation #2464: registers the collection evidence report as a step of work package collection-build.

  settings   collection.evidence_path (the folder), collection.evidence_name (the file name stem)
  step       collection.evidence (Collection-Build.ps1 -Action Evidence), with its 'refused' condition
  utilities  lib/collectionevidence.py, this migration, and the purpose of Collection-Build.ps1 brought up to date
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/collection_evidence_2464_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2464-COLLECTION-EVIDENCE-20261111"
MODULE = "collection_evidence_2464_v1_20261111"
WP = "collection-build"
H = "iba.app.handlers.collectionbuild"
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
SETTINGS = [
    ("collection.evidence_path", "outputs/reports/collection-evidence",
     "the folder the collection evidence report (Collection-Build.ps1 -Action Evidence, #2464) writes its Markdown file and CSV to", "collection"),
    ("collection.evidence_name", "collection-evidence",
     "the stem of the collection evidence report's file names (#2464); the collection names, the version and the date follow it by the filing rule", "collection"),
]
STEP = (10, "collection.evidence", "evidence",
        "write the evidence report of one collection or a comma list, with -Collection: the table entries stored for every aspect of the members, from the base data "
        "through the observations and claims into the narrative, as a Markdown file and a CSV under collection.evidence_path, versioned by the filing rule, the "
        "previous live versions archived; no evaluation, nothing inferred, nothing written to a table; -Check writes no file -- see lib/collectionevidence.py (escalation #2464)")
UTILITIES = [
    ("collectionevidence", "iba/app/lib/collectionevidence.py", 0, "collectionevidence.py -- the evidence report of one collection or a list: the stored entries from the base "
     "data through observations and claims into the narrative, read-only on the tables (escalation #2464).", 1,
     "the tiers, folder and file name stem are read from cfg_setting by the handler; the code holds no tunable value"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2464: registers the collection evidence report as a step of collection-build; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]
PS_PURPOSE = ("PS entry point for module 5 of 5 of the surface cycle (escalation #2361): Status, Links, Show, Export, ExportMembers, ExportSurfaces, Evidence, Set, Merge, Seed, Ask; "
              "dispatches through run.py, work package collection-build.")


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    ordinal, step, fn, does = STEP
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
        for t, op, where, set_ in ops:
            print(" ", t, op, where or set_.get("key") or set_.get("step") or set_.get("module"))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2464-collection-evidence', named=True)}")
    try:
        conn.execute("SAVEPOINT collection_evidence")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE collection_evidence")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO collection_evidence")
        conn.execute("RELEASE collection_evidence")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
