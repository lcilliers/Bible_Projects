"""record_retire_onfail_2172_v1_20261022.py -- escalation #2172 (and #2214): the cascade missed when
narrative_register.record was retired (strand_reading_schema_2172_v1_20261022): its cfg_on_fail row
still named the step, and configmaint.validate reported "on_fail step 'narrative_register.record' is
not a step in any work package". The row is set inactive. Registers itself (inactive, at its own
archive path) in the same transaction; cfg_* writes through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/record_retire_onfail_2172_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2172-RECORD-ONFAIL-20261022"
MODULE = "record_retire_onfail_2172_v1_20261022"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = [("cfg_on_fail", "update", {"step": "narrative_register.record", "condition": cond}, {"inactive": 1})
           for (cond,) in conn.execute("SELECT condition FROM cfg_on_fail WHERE step='narrative_register.record' "
                                       "AND inactive=0")]
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2172/#2214: the retired narrative_register.record's "
                       f"cfg_on_fail row set inactive, run_id {RUN_ID}. inactive=1 once applied."}))
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
