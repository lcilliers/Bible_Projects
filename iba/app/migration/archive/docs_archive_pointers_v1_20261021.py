"""docs_archive_pointers_v1_20261021.py -- escalation #2191 (element of the IBA app reset, #2177):
the 36 old docs/ files are archived to docs/archive/, prose-store-architecture.md included (the
researcher: superseded in the configs). Three cfg texts pointed at it: rules 52 and 53's source
(origin: repointed at the archived copy) and the cfg_utility purpose of the prose-extract CLI
(a live description: rewritten to the current state).

Registers itself in cfg_utility in the same transaction. Written through
configmaint.apply_logged(). Idempotent: a value already changed is skipped. One transaction.

Usage:
    python iba/app/migration/docs_archive_pointers_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2191-DOCS-ARCHIVE-20261021"
OLD = "docs/prose-store-architecture.md"
NEW = "docs/archive/prose-store-architecture.md"
MODULE = "docs_archive_pointers_v1_20261021"

# (table, key column, key, column, new value or None to repoint OLD -> NEW)
CHANGES = [
    ("cfg_behaviour_rule", "id", 52, "source", None),
    ("cfg_behaviour_rule", "id", 53, "source", None),
    ("cfg_utility", "module", "scripts_build_programme_prose_extract", "purpose",
     "CLI entry point for the programme-prose extract; the logic is iba/app/lib/prosestore.py, "
     "also run as prose.extract (Prose.ps1 -Step Extract)."),
]
UTILITY = {
    "module": MODULE,
    "file_path": f"iba/app/migration/{MODULE}.py",
    "purpose": "ONE-OFF migration -- escalation #2191: repoints the cfg texts naming "
               f"{OLD} after docs/ was archived, through configmaint.apply_logged under run_id "
               f"{RUN_ID}. inactive=1 once applied.",
    "inactive": 1,
    "config_exempt": 1,
    "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
                            "configmaint.apply_logged, same class as the other Developer Mode "
                            "migrations",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    todo = []
    for table, kcol, key, col, value in CHANGES:
        row = conn.execute(f'SELECT "{col}" FROM "{table}" WHERE "{kcol}"=?', (key,)).fetchone()
        if row is None:
            print(f"{table} {key} not found -- nothing done")
            return 1
        if OLD not in (row[0] or ""):
            continue
        todo.append((table, kcol, key, col, value if value else row[0].replace(OLD, NEW)))
    registered = conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone()
    if not todo and registered:
        print("already applied -- skipped")
        return 0
    if a.dry_run:
        for t in todo:
            print(f"DRY RUN -- {t[0]} {t[2]}.{t[3]} -> {t[4]}")
        return 0
    with conn:
        for table, kcol, key, col, value in todo:
            apply_logged(conn, RUN_ID, table, "update", {kcol: key}, {col: value})
        if not registered:
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, UTILITY)
    print(f"{len(todo)} text(s) repointed (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
