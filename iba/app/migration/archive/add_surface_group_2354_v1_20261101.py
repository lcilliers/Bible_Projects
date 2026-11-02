"""add_surface_group_2354_v1_20261101.py -- escalation #2354 (researcher, chat 2026-11-01: add the surface group
column; a layer column only if it holds information that confirms why a decision was made; the kinds of being are
told apart by concept domains, not by this column).

Adds a nullable `surface_group TEXT` column to surface_subgroup, last in the table so its cfg_column ordinal equals
its physical position. The group of the pair: behaviour, inner_being_state, being, or not_allocated (the pairs held
back for the researcher to inspect). The kinds of being (divine, spirits, people and so on) are NOT values here: they
are concept domains (concept_domain), as feeling is. Registered through configmaint.apply_logged(): the cfg_column
row, the four cfg_enum values (enum surface_subgroup.surface_group) and the inactive cfg_utility row of this script
(at its archive path). No row is given a group: the column is NULL until a step writes it. Idempotent. One
transaction.

Usage:
    python iba/app/migration/add_surface_group_2354_v1_20261101.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-SURFACE-GROUP-20261101"
MODULE = "add_surface_group_2354_v1_20261101"
TABLE = "surface_subgroup"
ENUM = "surface_subgroup.surface_group"
VALUES = ["behaviour", "inner_being_state", "being", "not_allocated"]
SOURCE = ("escalation #2354 (researcher, chat 2026-11-01; outputs/escalation/2354-concepts-retry-plan-v3-20261101.md)")
FILLED = f"iba/app/migration/archive/{MODULE}.py adds the column; no step writes it yet"
USE = ("the group of the pair for the concepts: behaviour, inner_being_state, being, or not_allocated (held back for "
       "the researcher to inspect in detail). The kinds of being are not values here: they are concept domains. "
       "Provisional and inferential (B:4) until the researcher confirms; NULL until a step writes it")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name='surface_group'", TABLE):
        ordinal = conn.execute("SELECT COUNT(*) FROM cfg_column WHERE database='iba' AND table_name=?",
                               (TABLE,)).fetchone()[0]
        ops.append(("cfg_column", "insert", {}, {
            "database": "iba", "table_name": TABLE, "name": "surface_group", "ordinal": ordinal, "type": "TEXT",
            "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None, "fk": None, "use": USE,
            "expectation": f"enum.{ENUM}", "source": SOURCE, "filled_by": FILLED, "inactive": 0}))
    for i, v in enumerate(VALUES):
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", ENUM, v):
            ops.append(("cfg_enum", "insert", {}, {"name": ENUM, "value": v, "ordinal": i, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: surface_group column on {TABLE}; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (TABLE,)).fetchone():
        print(f"REFUSED, nothing written: table not found: {TABLE}")
        return 2
    add_col = "surface_group" not in {r[1] for r in conn.execute(f"PRAGMA table_info({TABLE})")}
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: ALTER TABLE ADD COLUMN on {TABLE}: {add_col}; {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {set_.get('table_name', '')} {set_.get('name') or set_.get('module')}"
                  f" {set_.get('value', '')} ordinal={set_.get('ordinal', '')}")
        return 0
    if not add_col and not ops:
        print("already applied: the column and its config exist; nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT surface_group")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if add_col:
            conn.execute(f"ALTER TABLE {TABLE} ADD COLUMN surface_group TEXT")
        conn.execute("RELEASE surface_group")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_group")
        conn.execute("RELEASE surface_group")
        raise
    print(f"applied (run {RUN_ID}): surface_group added to {TABLE}: {add_col}; {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
