"""renamed_paths_2207_v1_20261022.py -- escalation #2207 (researcher, 2026-10-22: "#2207: option (a),
close this session; I will start a fresh one with /developer-mode"; first in it, the 7 cfg rows that
name the renamed files). Commit 316cfe3d gave two iba/docs plans their escalation-id prefix (863, 971);
seven live rows still named the old paths:
cfg_table folder_purpose.use; cfg_behaviour_class filing.authoritative_doc; cfg_behaviour_rule 56-60
source. Rules 56-59 also cite docs/file-organisation-rules.md, archived under #2177 to
archive/docs/file-organisation-rules-history-to-20261021.md (the cited sections are still there);
the citation is pointed at the archived file. cfg_change_detail is history and is not touched.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/renamed_paths_2207_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2207-RENAMED-PATHS-20261022"
MODULE = "renamed_paths_2207_v1_20261022"
RENAMES = [
    ("iba/docs/file-naming-and-location-governance-plan-v1-20260826.md",
     "iba/docs/863-file-naming-and-location-governance-plan-v1-20260826.md"),
    ("iba/docs/folder-purpose-governance-plan-v5-20260828.md",
     "iba/docs/971-folder-purpose-governance-plan-v5-20260828.md"),
    ("docs/file-organisation-rules.md ",
     "archive/docs/file-organisation-rules-history-to-20261021.md "),
]
# (table, key column, key value, column to fix)
ROWS = [("cfg_table", "name", "folder_purpose", "use"),
        ("cfg_behaviour_class", "class", "filing", "authoritative_doc")] + \
       [("cfg_behaviour_rule", "id", i, "source") for i in (56, 57, 58, 59, 60)]


def _fixed(value: str) -> str:
    for old, new in RENAMES:
        if new not in value:
            value = value.replace(old, new)
    return value


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    for table, key, kval, col in ROWS:
        row = conn.execute(f'SELECT "{col}" FROM "{table}" WHERE "{key}"=?', (kval,)).fetchone()
        if row is None:
            print(f"missing row: {table} {key}={kval}")
            return 1
        new = _fixed(row[0])
        if new != row[0]:
            ops.append((table, "update", {key: kval}, {col: new}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2207: 7 live cfg rows point at the renamed "
                       f"iba/docs plans and the archived file-organisation rules, through "
                       f"configmaint.apply_logged under run_id {RUN_ID}. inactive=1 once applied."}))
    for t, op, where, set_ in ops:
        print(f"  {op} {t} {where} {set_}")
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
