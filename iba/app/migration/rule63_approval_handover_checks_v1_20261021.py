"""rule63_approval_handover_checks_v1_20261021.py -- escalation #2178: what a hand-over for
approval must carry.

Found on #2177 (2026-10-21): Claude handed an item to the researcher at ready_for_approval with
nothing to approve, only to clear the Stop-hook backlog check. Researcher, verbatim: "add to your
action to clear the automatic backlog check that assigning something for me to approve means you
asked what I am suppose to approve, and is it ready for approval, and the content clearly state
what approval you are seeking, if you are requesting interim approval for a action that need to
result in a follow up action you must use assign the next action so the approval does not close a
in progress step."

Amends cfg_behaviour_rule 63 (claude-held-item-must-progress-or-bounce-back): rule_text and source
gain the three checks and the interim-approval rule (-NeedsFollowup 1, escalation #1075, so
`approved` routes back to Claude instead of completed). The Stop hook message
(.claude/hooks/stop_check_escalation_backlog.py) is changed in the same unit of work.

Written through configmaint.apply_logged() (Developer Mode removes propose's gate, never the
audit). Idempotent: skipped when the text is already present. One transaction.

Usage:
    python iba/app/migration/rule63_approval_handover_checks_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2178-RULE63-HANDOVER-20261021"
MARK = "Before any hand-over for approval (escalation #2178"

TEXT_ADD = (
    " " + MARK + ", 2026-10-21), Claude checks three things and the "
    "hand-over states them: (1) what exactly the researcher is asked to approve; (2) that it is "
    "ready for approval, i.e. a finished piece of work or a decision with its options, not "
    "something Claude still has to do or work the researcher has told Claude to carry; (3) the "
    "resolution states plainly what approval is sought. If none of the three holds, the item is "
    "not handed over: work already under way stays with Claude with a one-line acknowledgement, "
    "and clearing the Stop-hook backlog check is never a reason to hand over. An interim approval "
    "(approval of one step whose result needs a further action by Claude) is handed over with "
    "-NeedsFollowup 1 in the same call, so the researcher's `approved` routes the item back to "
    "Claude (re-assigned) and does not close a step still in progress (escalation #1075 "
    "mechanism).")
SOURCE_ADD = (
    " | Amended 2026-10-21 (escalation #2178), researcher verbatim after #2177 was handed over "
    "with nothing to approve: \"add to your action to clear the automatic backlog check that "
    "assigning something for me to approve means you asked what I am suppose to approve, and is "
    "it ready for approval, and the content clearly state what approval you are seeking, if you "
    "are requesting interim approval for a action that need to result in a follow up action you "
    "must use assign the next action so the approval does not close a in progress step.\"")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    row = conn.execute("SELECT rule_text, source FROM cfg_behaviour_rule WHERE id=63 AND "
                       "rule_key='claude-held-item-must-progress-or-bounce-back'").fetchone()
    if row is None:
        print("cfg_behaviour_rule 63 not found -- nothing done")
        return 1
    if MARK in row[0]:
        print("rule 63 already amended -- skipped")
        return 0
    new = {"rule_text": row[0] + TEXT_ADD, "source": row[1] + SOURCE_ADD}
    if a.dry_run:
        print("DRY RUN -- would update cfg_behaviour_rule 63:\n" + TEXT_ADD.strip())
        return 0
    with conn:
        apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 63}, new)
    print(f"cfg_behaviour_rule 63 amended (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
