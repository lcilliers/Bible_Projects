"""reading_reopen_2331_v1_20261030.py -- escalation #2331: Reading has no way to put a done verse back in hand.

Approved by the researcher, chat 2026-10-30: 'Approve A' (a re-open action in Reading.ps1 that returns named done verses to waiting
with a logged reason, so Observe and Record redo them by modifying in place, RS-04). Config first
(governance.rules_must_be_config_driven), then the code that reads it:
- cfg_step: reading.reopen (handler iba.app.handlers.reading:reopen);
- cfg_method_rule RS-09 reopen-done-verse-with-reason.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/reading_reopen_2331_v1_20261030.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2331-READING-REOPEN-20261030"
MODULE = "reading_reopen_2331_v1_20261030"
SRC = "#2331 (researcher, chat 2026-10-30: 'Approve A')"

STEP = {"work_package": "reading", "ordinal": 10, "step": "reading.reopen", "handler": "iba.app.handlers.reading:reopen",
        "scope": "none", "kind": "utility", "inactive": 0,
        "does": "done verses of an open reading returned to waiting (-Verse names them, -Note is the reason), so Observe and Record redo "
                "them by modifying their observations in place; the reason and the last result are kept in the scope JSON; no observation "
                "or node is changed -- see lib/reading.py (#2331)"}
RULE = {"step": "reading.reopen", "rule_key": "RS-09 reopen-done-verse-with-reason", "ordinal": 78, "active": 1, "source_doc": SRC,
        "enforced_by": "iba/app/lib/reading.py reopen",
        "rule_text": "A done verse of an open reading goes back to waiting only by Reading.ps1 -Step Reopen, naming the verse and giving "
                     "the reason (at least reading.verse_loop min_reason_chars). Only a done verse is re-opened. The reason, the time and "
                     "the verse's last result are kept with the verse in the scope JSON (`reopened`); no observation or node is changed "
                     "by it. The redo is Observe and Record on the re-opened verse: each existing observation is accepted, modified in "
                     "place or soft deleted with its reason (RS-04, RW-01). The scope JSON is never edited by hand to do this (#2331)."}


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    if not one("SELECT 1 FROM cfg_step WHERE step='reading.reopen'"):
        ops.append(("cfg_step", "insert", {}, STEP))
    if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", RULE["rule_key"]):
        ops.append(("cfg_method_rule", "insert", {}, RULE))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2331: the Reading Reopen step and RS-09; run_id {RUN_ID}. inactive=1 once applied."}))
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
