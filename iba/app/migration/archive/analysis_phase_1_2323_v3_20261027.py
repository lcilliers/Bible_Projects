"""analysis_phase_1_2323_v3_20261027.py -- escalation #2323: the observations Analysis_phase_1 works on.

Researcher, chat 2026-10-27 (verbatim): "you must respect the fact that some observations are not related to analysis_phase_1 work and
should not be updated or removed."

cfg_setting reading.verse_loop gets `own_stages`: the stages of the observations that are the verse understanding Analysis_phase_1
checks (accept, modify, delete, merge): verse-reading, reading, prior-capture and Analysis_phase_1. The observations of every other
stage (char-answers, char-reading, char-subgroup, char-synergy, strand-reading) are shown on the sheet as context, read only: they
are never changed, deleted or merged, and they do not count for a surface. cfg_method_rule RS-04 restated.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2323_v3_20261027.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2323-OWN-STAGES-20261027"
MODULE = "analysis_phase_1_2323_v3_20261027"
RS04 = ("When a verse is worked, every existing observation and node on it that belongs to Analysis_phase_1 (the stages of "
        "cfg_setting reading.verse_loop own_stages) is checked against the verse and accepted, modified (changed in place; the old "
        "value, the new value and the reason are kept in ib_observation_change), soft deleted (the `deleted` column, with the reason) "
        "or, for a duplicate description, merged into the observation that is kept. The check's fixes are part of it and need no "
        "separate approval. Observations of other stages (the characteristic and strand work) are shown for context, never changed, "
        "deleted or merged, and do not count for a surface. Nothing is physically deleted.")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    loop = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.verse_loop'")[0])
    if "own_stages" not in loop:
        loop["own_stages"] = ["verse-reading", "reading", "prior-capture", "Analysis_phase_1"]
        ops.append(("cfg_setting", "update", {"key": "reading.verse_loop"}, {"value": json.dumps(loop)}))
    row = one("SELECT id FROM cfg_method_rule WHERE rule_key LIKE 'RS-04 %' AND active=1")
    if row:
        ops.append(("cfg_method_rule", "update", {"id": row[0]}, {"rule_text": RS04, "source_doc": "#2323 (researcher, chat 2026-10-27)"}))
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
