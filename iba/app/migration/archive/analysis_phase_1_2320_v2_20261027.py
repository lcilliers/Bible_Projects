"""analysis_phase_1_2320_v2_20261027.py -- escalation #2320, follow-up to analysis_phase_1_2320_v1_20261027.py: retiring the step
reading.gather left its cfg_on_fail row and its cfg_write_grant rows pointing at a step that is no longer active, which
Config-Maintenance.ps1 -Step Validate reports as 2 coherence errors. They are retired with the step (inactive=1).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2320_v2_20261027.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2320-ANALYSIS-PHASE-1-GATHER-RETIRED-20261027"
MODULE = "analysis_phase_1_2320_v2_20261027"


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    for step, cond in conn.execute("SELECT step, condition FROM cfg_on_fail WHERE step='reading.gather' AND inactive=0").fetchall():
        ops.append(("cfg_on_fail", "update", {"step": step, "condition": cond}, {"inactive": 1}))
    for w, t, db in conn.execute("SELECT writer, table_name, database FROM cfg_write_grant WHERE writer='reading.gather' "
                                 "AND inactive=0").fetchall():
        ops.append(("cfg_write_grant", "update", {"writer": w, "table_name": t, "database": db}, {"inactive": 1}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2320: the rows of the retired step reading.gather retired; run_id "
                       f"{RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    ops = plan(conn)
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
