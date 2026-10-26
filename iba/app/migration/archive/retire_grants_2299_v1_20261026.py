"""retire_grants_2299_v1_20261026.py -- escalation #2299 (#2286 U9): the write grants of the retired steps
cluster.subgroup, cluster.reading and cluster.answer made inactive. t_word_and_retire_2297_2299_v1_20261026.py made the
steps inactive and left their 11 grants live, which configmaint.validate reports as coherence errors (a grant whose
writer is not an active step).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.

Usage:
    python iba/app/migration/retire_grants_2299_v1_20261026.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2299-RETIRE-GRANTS-20261026"
MODULE = "retire_grants_2299_v1_20261026"
RETIRED_STEPS = ("cluster.subgroup", "cluster.reading", "cluster.answer")


def plan(conn) -> list[tuple]:
    ops = [("cfg_write_grant", "update", {"writer": w, "table_name": t, "database": d}, {"inactive": 1})
           for w, t, d in conn.execute("SELECT writer, table_name, database FROM cfg_write_grant WHERE writer IN "
                                       "(SELECT value FROM json_each(?)) AND inactive=0", (json.dumps(RETIRED_STEPS),))]
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2299 (#2286 U9): the write grants of the retired "
                       f"cluster.subgroup pipeline made inactive; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, set_ in ops:
            print(f"  {op:6} {t:20} {where or set_.get('module')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
