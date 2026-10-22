"""fix_not_count_2207_v1_20261022.py -- escalation #2207 (researcher approval 2026-10-22), backlog
fixes that need config:
- wa_obs_question_catalogue.scope/status/tier: their cfg_enum groups described the columns but no
  cfg_column.expectation named them, so validate called them orphans. The live data conforms; the
  iba column rows now carry expectation enum.<group>.
- cfg_utility scripts_apply_session_patch: set inactive, as the researcher's 2026-08-18 ruling (#729)
  said; the file moves to scripts/archive/ in the same unit of work.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/fix_not_count_2207_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2207-FIX-NOT-COUNT-20261022"
MODULE = "fix_not_count_2207_v1_20261022"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    for col in ("scope", "status", "tier"):
        exp = f"enum.wa_obs_question_catalogue.{col}"
        row = conn.execute("SELECT expectation FROM cfg_column WHERE database='iba' AND "
                           "table_name='wa_obs_question_catalogue' AND name=?", (col,)).fetchone()
        if row and row[0] != exp:
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": "wa_obs_question_catalogue",
                                                 "name": col}, {"expectation": exp}))
    row = conn.execute("SELECT inactive FROM cfg_utility WHERE module='scripts_apply_session_patch'").fetchone()
    if row and row[0] == 0:
        ops.append(("cfg_utility", "update", {"module": "scripts_apply_session_patch"},
                    {"inactive": 1, "file_path": "scripts/archive/apply_session_patch.py"}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2207: wires 3 enum expectations and retires "
                       f"apply_session_patch, through configmaint.apply_logged under run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
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
