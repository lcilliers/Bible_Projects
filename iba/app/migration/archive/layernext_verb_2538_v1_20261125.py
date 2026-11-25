"""layernext_verb_2538_v1_20261125.py -- escalation #2538 (researcher, 2026-11-25: "the moment I close the chat then you will have no clue what to do").

Registers the verb that holds the loop of the layered reading in code: `Collection-Build.ps1 -Action LayerNext -Collection <name>` (handler collection.layer_next, lib/layerloop.py). It reads the ledger and says
which subgroup is in flight, which step is next, its state and the verbs to run; and the opening of a step for a subgroup is refused while another subgroup is further through its loop and not finished.

Config only (one cfg_step row; the handler, the PowerShell action and lib/layerloop.py are code). Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/layernext_verb_2538_v1_20261125.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-LAYERNEXT-20261125"
STEP = "collection.layer_next"
DOES = ("say what to do next in the layered reading of a collection, from the ledger alone (-Collection): the subgroup in flight, the step, its state and the verbs to run; the loop is for one subgroup at a time, "
        "B1 to C1, and the opening of a step for a subgroup is refused while another subgroup is further through its loop and not finished -- see lib/layerloop.py (escalation #2538)")


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (STEP,)).fetchone():
        top = conn.execute("SELECT coalesce(max(ordinal), 0) FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
        ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": top + 1, "step": STEP, "handler": "iba.app.handlers.collectionbuild:layer_next", "scope": "none",
                                                "does": DOES, "inactive": 0, "kind": "utility"}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module='layerloop'").fetchone():      # the module the verb runs on (governance: every file is registered)
        ops.append(("cfg_utility", "insert", {}, {"module": "layerloop", "file_path": "iba/app/lib/layerloop.py",
                                                  "purpose": "layerloop.py -- the loop of the layered reading held in code (escalation #2538): the progress of each subgroup from the ledger, the next action, and the order gate (one subgroup at a time, B1 to C1).",
                                                  "inactive": 0, "config_exempt": 1, "config_exempt_reason": "the steps, their order and their descriptions are read from cfg_setting layer.reading; the code holds no tunable value",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where)
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-layernext-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT ln")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE ln")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO ln")
        conn.execute("RELEASE ln")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
