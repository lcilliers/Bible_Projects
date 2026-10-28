"""analysis_phase_1_2323_v4_20261027.py -- escalation #2323: the wording of an observation, not its stage, decides.

Researcher, chat 2026-10-27 (verbatim): "stages in the past were inconsistenly used, and is not an indication of the real nature of the
observation. unfortunately it cannot be relied on. it should not be used for filtering. the only filtering that can be used is the
actual wording of the observation."

Undoes analysis_phase_1_2323_v3 (cfg_setting reading.verse_loop `own_stages` removed) and adds the existing-observation action `leave`:
the reading, reading the wording of an observation on the verse, finds it is not verse understanding (for example a characteristic
claim answer) and leaves it exactly as it is, with its reason. A left observation is not changed, deleted or merged, needs no kind or
subgroup, does not count for a surface and is not in the Observe gate. cfg_method_rule RS-04 restated.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2323_v4_20261027.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2323-WORDING-NOT-STAGE-20261027"
MODULE = "analysis_phase_1_2323_v4_20261027"
RS04 = ("When a verse is worked, every existing observation and node on it, of any stage, is checked against the verse by its "
        "wording. The stage is not an indication of the nature of an observation and is never used to filter. Each observation is "
        "accepted, modified (changed in place; the old value, the new value and the reason are kept in ib_observation_change), soft "
        "deleted (the `deleted` column, with the reason), merged (a duplicate description, into the observation that is kept) or, when "
        "its wording shows it is not verse understanding, left exactly as it is with the reason. The check's fixes are part of it and "
        "need no separate approval. Nothing is physically deleted.")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    loop = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.verse_loop'")[0])
    changed = "own_stages" in loop or "leave" not in loop["existing_actions"]
    loop.pop("own_stages", None)
    if "leave" not in loop["existing_actions"]:
        loop["existing_actions"] = list(loop["existing_actions"]) + ["leave"]
    if changed:
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
