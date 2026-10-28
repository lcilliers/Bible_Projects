"""analysis_phase_1_2320_v3_20261028.py -- escalation #2320: the rules for stating an observation are enforced in the code.

Researcher, chat 2026-10-28 (verbatim): "the test failed. I am going back to the developer mode so you can enforce in the code for the
observation all the rules for stating an observation, I do not yet know how you want to do it, but the result I want to see is that
the observations for each surface comply with the requirement."

Config for the code in iba/app/lib/reading.py and observationrecord.py:
- cfg_setting reading.verse_loop node_set gets `observation_id` (a node moves to the observation of the act, spec 4.1) and
  `reading_id` (the reading that checked and kept it);
- cfg_method_rule RS-08 observation-covers-the-parts: what Record enforces (spec 4.1 and 4.2).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2320_v3_20261028.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2320-OBSERVATION-RULES-ENFORCED-20261028"
MODULE = "analysis_phase_1_2320_v3_20261028"
SRC = "#2320 (researcher, chat 2026-10-28)"
RS08 = ("The observations of a verse state what the verse shows, and Record enforces it: an observation that covers a relevant surface "
        "(a node with a characteristic or qualifier role) holds every part of spec 4.2 (sense, evidence, polarity, content, enactment, "
        "party, circumstance, chain, primary operation, typed flags), each in words or stated absent with the reason (sense, evidence "
        "and circumstance never absent). The words that bear on an act are nodes of the observation of the act, never an observation "
        "of their own. One statement observation names the primary operation; a stated chain has a link observation; a stated party "
        "has a party observation with its route. A verse whose observations do not comply is not recorded.")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    loop = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.verse_loop'")[0])
    add = [c for c in ("observation_id", "reading_id") if c not in loop["node_set"]]
    if add:
        loop["node_set"] = list(loop["node_set"]) + add
        ops.append(("cfg_setting", "update", {"key": "reading.verse_loop"}, {"value": json.dumps(loop)}))
    if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key LIKE 'RS-08 %'"):
        nid = one("SELECT max(id) FROM cfg_method_rule")[0] + 1
        nord = one("SELECT max(ordinal) FROM cfg_method_rule")[0] + 1
        ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": "reading.record", "rule_key": "RS-08 observation-covers-the-parts",
                                                      "rule_text": RS08, "source_doc": SRC, "enforced_by": "iba/app/lib/reading.py _validate_sheet; iba/app/lib/observationrecord.py complete_parts",
                                                      "ordinal": nord, "active": 1}))
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
