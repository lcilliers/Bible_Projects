"""ib_observation_use_2231_v1_20261023.py -- escalation #2231: the iba.db cfg_table row for ib_observation
names only the cluster-reading writers and has no grain; it is rewritten to what the table holds now (every
stage and the steps that write it, from cfg_write_grant). The '81 observations' text first reported on
#2231 belongs to the inactive bible_research.db row of the same name and is left as it is (inactive rows are
history, rule 61).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/ib_observation_use_2231_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2231-IB-OBSERVATION-USE-20261023"
MODULE = "ib_observation_use_2231_v1_20261023"
GRAIN = "one row per observation"
USE = ("One observation: a typed finding from a reading, with its text, meaning, implication, basis, parties and "
       "status (draft or withdrawn), grounded on verses, strongs, subgroups, clusters or other observations through "
       "ib_node. Written by stage: verse-reading (lexical.meaning, lexical.relational), char-reading, char-answers "
       "and char-subgroup (cluster.reading, cluster.answer, cluster.subgroup), strand-reading (strand_reading.record, "
       "strand_reading.derive), and enhanced by observation_enhancer.apply. A differently-shaped legacy table of the "
       "same name in bible_research.db is inactive.")


def plan(conn) -> list[tuple]:
    ops = []
    row = conn.execute("SELECT grain, use FROM cfg_table WHERE database='iba' AND name='ib_observation'").fetchone()
    if row and (row[0], row[1]) != (GRAIN, USE):
        ops.append(("cfg_table", "update", {"database": "iba", "name": "ib_observation"}, {"grain": GRAIN, "use": USE}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2231: cfg_table ib_observation (iba) grain and use; "
                       f"run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
