"""analysis_phase_1_2323_v2_20261027.py -- escalation #2323: the stage of what Analysis_phase_1 writes is Analysis_phase_1 (researcher, chat 2026-10-27: "the source stage should also be Analysis_phase_1"). It is added to cfg_enum ib_observation.stage; the code writes it as ib_observation.stage and ib_node.source_stage of new rows. (Old text: retiring the step

Old rows keep the stage they were written under.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2323_v2_20261027.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2323-STAGE-20261027"
MODULE = "analysis_phase_1_2323_v2_20261027"


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    if not one("SELECT 1 FROM cfg_enum WHERE name='ib_observation.stage' AND value='Analysis_phase_1'"):
        o = one("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name='ib_observation.stage'")[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "ib_observation.stage", "value": "Analysis_phase_1", "ordinal": o, "inactive": 0}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2320: stage value Analysis_phase_1 added; run_id "
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
