"""add_surface_group_qualifier_2354_v1_20261102.py -- escalation #2354 (researcher, chat 2026-11-02: "Yes, add
qualifier").

Adds the value `qualifier` to the enum surface_subgroup.surface_group (a word that describes something rather than
being a behaviour, a state or a being: "within" says where). The use that makes the word a qualifier (a place, a
time, a quantity, a quality) is kept in the name of the qualifier subgroup the pair sits in
(cluster_subgroup.kind = 'qualifier'), as the five existing qualifier subgroups already do; there is no marker for
which group it supports. The `use` text of the cfg_column row of surface_group is brought to the five values. Both
writes go through configmaint.apply_logged(). No surface_subgroup row is touched. Idempotent. One transaction.

Usage:
    python iba/app/migration/add_surface_group_qualifier_2354_v1_20261102.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-SURFACE-GROUP-QUALIFIER-20261102"
MODULE = "add_surface_group_qualifier_2354_v1_20261102"
ENUM = "surface_subgroup.surface_group"
USE = ("the group of the pair for the concepts: behaviour, inner_being_state, being, qualifier (a word that "
       "describes something and is not itself a behaviour, state or being: it says where, when, how much or what "
       "kind; the use is named by the qualifier subgroup the pair sits in), or not_allocated (held back for the "
       "researcher to inspect in detail). The kinds of being are not values here: they are concept domains. "
       "Provisional and inferential (B:4) until the researcher confirms; NULL until a step writes it")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value='qualifier'", ENUM):
        # qualifier takes ordinal 3; not_allocated moves from 3 to 4 so the held-back value stays last
        ops.append(("cfg_enum", "update", {"name": ENUM, "value": "not_allocated"}, {"ordinal": 4}))
        ops.append(("cfg_enum", "insert", {}, {"name": ENUM, "value": "qualifier", "ordinal": 3, "inactive": 0}))
    row = conn.execute("SELECT use FROM cfg_column WHERE database='iba' AND table_name='surface_subgroup' "
                       "AND name='surface_group'").fetchone()
    if row is not None and row[0] != USE:
        ops.append(("cfg_column", "update", {"database": "iba", "table_name": "surface_subgroup",
                                             "name": "surface_group"}, {"use": USE}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: qualifier value of surface_group; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    if not conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='surface_subgroup' "
                        "AND name='surface_group'").fetchone():
        print("REFUSED, nothing written: the surface_group column is not registered (run the #2354 column "
              "migration first)")
        return 2
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {where or ''} {set_.get('value') or set_.get('module') or list(set_)}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT sg_qualifier")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE sg_qualifier")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sg_qualifier")
        conn.execute("RELEASE sg_qualifier")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
