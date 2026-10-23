"""study_active_2228_v1_20261023.py -- the study re-opened on the researcher's instruction, 2026-10-23, after the
reading process was built and accepted (#2228): "I will be returning to standard mode and restart the study, so
you can release the hold on the study, then do a session-close".

- cfg_setting behaviour.study_state: on_hold -> active (the study_active rules are delivered at start again).
- cfg_setting governance.study_status: ACTIVE, with the instruction verbatim and the process study work goes
  through now (Reading.ps1).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path) in the same
transaction. Idempotent.

Usage:
    python iba/app/migration/study_active_2228_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2228-STUDY-ACTIVE-20261023"
MODULE = "study_active_2228_v1_20261023"
STATUS = ("ACTIVE since 2026-10-23. Researcher, verbatim: 'I will be returning to standard mode and restart the study, "
          "so you can release the hold on the study, then do a session-close'. Study work (readings, weaves, audits) is "
          "done through the reading process: iba/app/ps/Reading.ps1 (Open, Record, Check, Synergy, Apply, Publish, "
          "Account; escalation #2228), a reading of one scope through three gates (recorded, synergised, published), "
          "with the narrative in iba.db (governance.narrative_home). The strand steps are retired (#2228 D-a).")


def plan(conn) -> list[tuple]:
    ops = []
    if conn.execute("SELECT value FROM cfg_setting WHERE key='behaviour.study_state'").fetchone()[0] != json.dumps("active"):
        ops.append(("cfg_setting", "update", {"key": "behaviour.study_state"}, {"value": json.dumps("active")}))
    if conn.execute("SELECT value FROM cfg_setting WHERE key='governance.study_status'").fetchone()[0] != json.dumps(STATUS):
        ops.append(("cfg_setting", "update", {"key": "governance.study_status"}, {"value": json.dumps(STATUS)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- the study re-opened on the researcher's instruction (2026-10-23, "
                       f"after #2228): behaviour.study_state active, governance.study_status; run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
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
