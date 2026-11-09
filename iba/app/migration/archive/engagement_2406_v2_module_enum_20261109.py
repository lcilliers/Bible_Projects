"""engagement_2406_v2_module_enum_20261109.py -- escalation #2406: the module name `engagement` was used by the 8 settings of v1 but is not a value of
cfg_enum config_module (configmaint.validate: 9 coherence errors, #2410). Adds the value, and registers this migration as a utility.
All cfg_* writes through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/engagement_2406_v2_module_enum_20261109.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2406-ENGAGEMENT-MODULE-ENUM-20261109"
MODULE = "engagement_2406_v2_module_enum_20261109"


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='engagement'").fetchone():
        top = conn.execute("SELECT max(ordinal) FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "engagement", "ordinal": top + 1, "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose":
                    f"ONE-OFF migration -- escalation #2406: adds `engagement` to cfg_enum config_module; run_id {RUN_ID}.", "inactive": 1, "config_exempt": 1,
                    "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                    "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
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
    try:
        conn.execute("SAVEPOINT engagement_enum")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE engagement_enum")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO engagement_enum")
        conn.execute("RELEASE engagement_enum")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
