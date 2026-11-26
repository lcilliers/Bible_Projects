"""guide_2538_v1_20261126.py -- escalation #2538 (researcher 2026-11-26: "then the work for creating the analytic process as a collection of
methods with a clear path of execution clearly described as such is not complete").

Gives the analytic process its home in the user guide as config, so that the guide cannot fall behind the methods:
  cfg_setting  layer.read_types `guide`: the file and section (USER-GUIDE.md 8.20) that describe the path of execution, and the methods
               besides the read commands that must be named there; checked by cfgquality.find_analytic_guide_gaps (a hard error in
               configmaint.validate)
  cfg_utility  this migration's own row
Written through configmaint.apply_logged. Named snapshot before a live apply; after the live apply the file archives itself. Idempotent.
Usage: python iba/app/migration/guide_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2538-GUIDE-20261126"
MODULE = "guide_2538_v1_20261126"
GUIDE = {"file": "iba/app/USER-GUIDE.md", "section": "8.20",
         "also": ["LayerNext", "Index", "IndexCheck", "GroupPull", "GroupRecord", "LayerOpen", "LayerPull", "LayerRecord", "LayerCheck",
                  "ValidatePull", "ValidateRecord", "ValidateCheck", "Subgroup", "NodeGroups", "ReleaseDeadTraces"]}


def plan(conn):
    ops = []
    types = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    if types.get("guide") != GUIDE:
        types["guide"] = GUIDE
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(types, ensure_ascii=False)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2538: layer.read_types guide, the home of the analytic path in USER-GUIDE.md 8.20",
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-guide-apply', named=True)}")
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
