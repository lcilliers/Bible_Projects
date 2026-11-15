"""record_answers_rule_2505_v3_20261115.py -- escalation #2448/#2507 (researcher, 2026-11-15: "all the work we do lives across sessions and chats - so there is no reason for you not to have the
context or the previous answers if you do your side well ... ensure your note taking fits your requirements"): behaviour rule 99 (read-instruction-in-whole-chat-context) states that the record
is the memory: a question the escalation record or the session logs answer is not asked. One cfg_behaviour_rule update through apply_logged. Idempotent.
Usage: python iba/app/migration/record_answers_rule_2505_v3_20261115.py [--db PATH]"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2448-RECORD-ANSWERS-RULE-20261115"
MODULE = "record_answers_rule_2505_v3_20261115"
ADD = (" The record is the memory: the researcher's earlier instructions and answers are in the escalation record and the session logs, and are read there before a question is put; a question "
       "the record answers, or that later work made moot, is not asked.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    r = conn.execute("SELECT id, rule_text FROM cfg_behaviour_rule WHERE rule_key='read-instruction-in-whole-chat-context'").fetchone()
    if r is None or ADD.strip() in r[1]:
        print("already applied: nothing changed")
        return 0
    conn.execute("SAVEPOINT rec_rule")
    apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": r[0]}, {"rule_text": r[1].rstrip() + ADD})
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2448: a rule text restated; run_id {RUN_ID}.", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None})
    conn.execute("RELEASE rec_rule")
    conn.commit()
    print(f"applied (run {RUN_ID}): rule {r[0]} restated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
