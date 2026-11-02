"""add_config_modules_2354_v1_20261102.py -- escalation #2354. The settings added by
surface_pair_verdict_2354_v1_20261102.py name two modules, ollama and surface_judge, that enum.config_module does not
list, so configmaint.validate reports 9 coherence errors (8 settings and the value-quality check). This adds the two
values to the enum, after the existing ones. cfg_* writes through configmaint.apply_logged(); registers itself
(inactive, at its archive path). Idempotent. One transaction.

Usage:
    python iba/app/migration/add_config_modules_2354_v1_20261102.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-CONFIG-MODULES-20261102"
MODULE = "add_config_modules_2354_v1_20261102"
ENUM = "config_module"
VALUES = ["ollama", "surface_judge"]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    nxt = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (ENUM,)).fetchone()[0]
    for v in VALUES:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", ENUM, v):
            ops.append(("cfg_enum", "insert", {}, {"name": ENUM, "value": v, "ordinal": nxt, "inactive": 0}))
            nxt += 1
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: modules ollama and surface_judge in enum "
                       f"{ENUM}; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=?", (ENUM,)).fetchone():
        print(f"REFUSED, nothing written: enum not found: {ENUM}")
        return 2
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {set_.get('value') or set_.get('module')} ordinal={set_.get('ordinal', '')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT config_modules")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE config_modules")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO config_modules")
        conn.execute("RELEASE config_modules")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
