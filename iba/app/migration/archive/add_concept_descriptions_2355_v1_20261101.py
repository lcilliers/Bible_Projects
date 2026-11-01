"""add_concept_descriptions_2355_v1_20261101.py -- escalation #2355 (researcher, chat 2026-11-01: "Add a
description column to table domain, concept, and concept-subgroup", then "only add descriptions to concept and
domain, not the link table").

Adds a nullable `description TEXT` column to concept_domain and to concept (not to concept_subgroup, which is the
link table). The column is added last in each table, so its cfg_column ordinal equals its physical position. Both
columns are registered in cfg_column through configmaint.apply_logged(), with the inactive cfg_utility row of this
script (at its archive path). No row is given a description: the columns are NULL until written. Idempotent. One
transaction.

Usage:
    python iba/app/migration/add_concept_descriptions_2355_v1_20261101.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2355-CONCEPT-DESCRIPTIONS-20261101"
MODULE = "add_concept_descriptions_2355_v1_20261101"
SOURCE = "escalation #2355 (researcher, chat 2026-11-01: description on concept_domain and concept, not the link table)"
FILLED = f"iba/app/migration/archive/{MODULE}.py adds the column; no step writes it yet"
USE = {
    "concept_domain": "what the domain is about, in the researcher's intended narrative; free text; NULL until written",
    "concept": "what the concept is about, in the researcher's intended narrative; free text; NULL until written",
}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for t, use in USE.items():
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name='description'", t):
            ordinal = conn.execute("SELECT COUNT(*) FROM cfg_column WHERE database='iba' AND table_name=?",
                                   (t,)).fetchone()[0]
            ops.append(("cfg_column", "insert", {}, {
                "database": "iba", "table_name": t, "name": "description", "ordinal": ordinal, "type": "TEXT",
                "is_pk": 0, "notnull": 0, "is_unique": 0, "dflt": None, "fk": None, "use": use,
                "expectation": None, "source": SOURCE, "filled_by": FILLED, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2355: description column on {', '.join(USE)}; "
                       f"run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    missing = [t for t in USE if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
                                                  (t,)).fetchone()]
    if missing:
        print(f"REFUSED, nothing written: table(s) not found: {missing}")
        return 2
    to_add = [t for t in USE if "description" not in {r[1] for r in conn.execute(f"PRAGMA table_info({t})")}]
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: ALTER TABLE ADD COLUMN on {to_add}; {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {set_.get('table_name', '')} {set_.get('name') or set_.get('module')}"
                  f" ordinal={set_.get('ordinal', '')}")
        return 0
    if not to_add and not ops:
        print("already applied: both columns and their config exist; nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT concept_desc")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for t in to_add:
            conn.execute(f"ALTER TABLE {t} ADD COLUMN description TEXT")
        conn.execute("RELEASE concept_desc")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO concept_desc")
        conn.execute("RELEASE concept_desc")
        raise
    print(f"applied (run {RUN_ID}): description added to {to_add}; {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
