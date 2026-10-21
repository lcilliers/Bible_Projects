"""escalation_thread_lifecycle_v1_20261012.py -- escalation #2000, the thread lifecycle (config).

Review: `iba/docs/2000-thread-lifecycle-review-v1-20261012.md` (round 2). Researcher, verbatim
(chat 2026-10-12): "We decided I will give you feedback in the chat, the rest you need to control
and the code must make it possible to manage the thread. all interaction must go to history." and
"proceed with the build". Claude manages a thread's lifecycle; there is no approval step.

Config written (the code is lib/escalation.py, same unit of work):
  1  cfg_enum escalation_thread_item_status += withdrawn, superseded;
     escalation_thread_item_response_kind += withdrawn, superseded                       (G1)
  3  cfg_escalation_transition: shape manual, priority 0, condition thread_items_all_settled ->
     completed (no open item left after this call's item change; never on reject). cfg_status_flow
     'completed' set_by gains its key.                                                     (G3)
  4  cfg_escalation_requirement: superseding a thread names its successor (-SupersededBy).   (G4)
  -  cfg_escalation thread_completion restated; the T6 requirement messages say 'settled'.
  -  cfg_behaviour_rule open-threads-carried-as-escalations restated (lifecycle, history).
  -  cfg_column use text for escalation_thread_item.status and escalation_thread_item_response.kind.
  (G2 and G5 are code only.)

No schema change. Idempotent: guarded inserts, updates set the target text. One transaction.

Usage:
    python iba/app/migration/escalation_thread_lifecycle_v1_20261012.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

ENUMS = [
    ("escalation_thread_item_status", "withdrawn", 2),
    ("escalation_thread_item_status", "superseded", 3),
    ("escalation_thread_item_response_kind", "withdrawn", 7),
    ("escalation_thread_item_response_kind", "superseded", 8),
]

SETTLED_KEY = "thread: every item settled"
TRANSITION = (0, "manual", None, "thread_items_all_settled", SETTLED_KEY,
              "escalation #2000 lifecycle (researcher 2026-10-12: 'the rest you need to control'): "
              "when this call's item change leaves no item open (each closed, withdrawn or "
              "superseded), the thread is completed in the same call, with a resolution generated "
              "from the item closures. Replaces T6's separate 'approved' step. Never fires on "
              "next_action=reject (a thread withdrawn or superseded settles its items itself). "
              "Mutually exclusive with the other priority-0 rows, which need an open item.")
STATUS_FLOW_ADD = ("; OR system (thread: every item settled -- closed, withdrawn or superseded -- "
                   "after an item change; escalation #2000 lifecycle)")

THREAD_COMPLETION = (
    "T6 as amended by the thread lifecycle (escalation #2000; researcher 2026-10-12: 'I will give "
    "you feedback in the chat, the rest you need to control and the code must make it possible to "
    "manage the thread. all interaction must go to history'). Claude manages a thread's lifecycle; "
    "there is no approval step. An item is settled when it is closed (answered), withdrawn (no "
    "longer relevant) or superseded (carried by another item or thread, named in the response). "
    "When an item change leaves no item open, the thread is completed in the same call, with a "
    "resolution generated from the closures; while items stay open, a partial settlement returns "
    "the thread to on-hold. A thread reaches completed or closed only when every item is settled. "
    "When a task or issue reaches a terminal state, its 'escalation' item on each thread takes the "
    "same ending: closed for completed/closed, withdrawn for withdraw, superseded for supersede. "
    "Withdrawing a thread withdraws its open items; superseding a thread names its successor "
    "(-SupersededBy OT-nn), and each open item moves to the successor and is recorded superseded. "
    "Every item response is written, in full, to the thread's history.")

REQ_SUCCESSOR = ("reject", "superseded_by", "thread_superseding",
                 "superseding a thread names its successor: -SupersededBy OT-nn (the open items move "
                 "to it) -- escalation #2000 lifecycle", "field_required")
T6_MESSAGES = {
    "update": "a thread reaches completed or closed only when every item is settled (closed, "
              "withdrawn or superseded) -- rule T6, escalation #2000. Settle the open items "
              "(-Item ... -ResponseKind closed|withdrawn|superseded) first.",
    "resolve_self_correctable": "a thread reaches completed only when every item is settled "
                                "(closed, withdrawn or superseded) -- rule T6, escalation #2000.",
}

COLUMN_USE = {
    ("escalation_thread_item", "status"):
        "cfg_enum escalation_thread_item_status: open, closed (answered), withdrawn (no longer "
        "relevant) or superseded (carried by another item or thread) -- current state only; every "
        "change is a response row",
    ("escalation_thread_item_response", "kind"):
        "cfg_enum escalation_thread_item_response_kind. 'closed', 'withdrawn' and 'superseded' "
        "settle an open item (status = kind; 'superseded' names its successor OT-nn[.n] or #nnnn in "
        "the text), 'reopened' opens a settled item again, 'forward' comes with at least one new "
        "item on the same thread",
}

RULE_TEXT = (
    "The open threads register is carried in the escalation table as type='thread' (alias OT-nn), "
    "not edited as a markdown file. A thread is not worked as a task: it moves only when a strand "
    "reaches it (focused capture, #1900). Its items (escalation_thread_item; cluster, Strong's, "
    "verse, strand, chapter, event, researcher, escalation) are what a strand or task is matched "
    "against (Escalation.ps1 -Action Match). Claude manages each thread's lifecycle; the "
    "researcher gives feedback in chat, which Claude records verbatim the same turn, and there is "
    "no approval step (researcher 2026-10-12: 'the rest you need to control'). Every response to "
    "an item -- touched, narrowed, forward, ruling, note, closed, reopened, withdrawn, superseded "
    "-- is an escalation_thread_item_response row, recorded through Escalation.ps1 -Action Update "
    "-Id OT-nn -Item ... -ResponseKind ... -Respond ..., and written in full to the thread's "
    "history ('all interaction must go to history'). A thread completes when its last open item "
    "is settled; a thread is withdrawn or superseded (-SupersededBy OT-nn) with its open items "
    "settled in the same call. Notes and comments on a thread are Updates, never edits to the "
    "register file (rule T8). New held items and researcher questions are raised as threads at "
    "ledger approval. The file _analytics/cross-cluster-web/open-threads-register.md is generated "
    "(Escalation.ps1 -Action Export -Type thread) and regenerated at session-close.")


def config(cur, report: list[str]) -> None:
    for name, value, ordinal in ENUMS:
        if cur.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
            report.append(f"cfg_enum {name}={value} already present -- skipped")
        else:
            cur.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                        (name, value, ordinal))
            report.append(f"cfg_enum {name}={value} inserted")

    prio, shape, na, cond, key, notes = TRANSITION
    if cur.execute("SELECT 1 FROM cfg_escalation_transition WHERE shape=? AND condition_key=?",
                   (shape, cond)).fetchone():
        cur.execute("UPDATE cfg_escalation_transition SET priority=?, resulting_status_key=?, "
                    "notes=? WHERE shape=? AND condition_key=?", (prio, key, notes, shape, cond))
        report.append(f"cfg_escalation_transition {cond} already present -- refreshed")
    else:
        cur.execute("INSERT INTO cfg_escalation_transition (priority, shape, next_action, "
                    "condition_key, resulting_status_key, notes, active) VALUES (?,?,?,?,?,?,1)",
                    (prio, shape, na, cond, key, notes))
        report.append(f"cfg_escalation_transition {cond} inserted")

    row = cur.execute("SELECT set_by FROM cfg_status_flow WHERE entity='escalation' AND "
                      "status='completed'").fetchone()
    if SETTLED_KEY in row[0]:
        report.append("cfg_status_flow completed already carries the settled key -- skipped")
    else:
        cur.execute("UPDATE cfg_status_flow SET set_by=? WHERE entity='escalation' AND "
                    "status='completed'", (row[0] + STATUS_FLOW_ADD,))
        report.append("cfg_status_flow completed set_by extended")

    cur.execute("UPDATE cfg_escalation SET rule_text=? WHERE rule_key='thread_completion'",
                (THREAD_COMPLETION,))
    report.append(f"cfg_escalation thread_completion restated: {cur.rowcount} row")

    action, field, ckey, msg, kind = REQ_SUCCESSOR
    if cur.execute("SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND field=? AND "
                   "condition_key=? AND check_kind=?", (action, field, ckey, kind)).fetchone():
        cur.execute("UPDATE cfg_escalation_requirement SET message=? WHERE action=? AND field=? "
                    "AND condition_key=? AND check_kind=?", (msg, action, field, ckey, kind))
        report.append("cfg_escalation_requirement superseded_by already present -- refreshed")
    else:
        cur.execute("INSERT INTO cfg_escalation_requirement (action, field, condition_key, "
                    "message, active, check_kind) VALUES (?,?,?,?,1,?)",
                    (action, field, ckey, msg, kind))
        report.append("cfg_escalation_requirement superseded_by inserted")
    for act, m in T6_MESSAGES.items():
        cur.execute("UPDATE cfg_escalation_requirement SET message=? WHERE action=? AND "
                    "check_kind='no_open_thread_items'", (m, act))
        report.append(f"cfg_escalation_requirement no_open_thread_items ({act}) message: "
                      f"{cur.rowcount} row")

    for (table, col), use in COLUMN_USE.items():
        cur.execute("UPDATE cfg_column SET use=? WHERE database='iba' AND table_name=? AND name=?",
                    (use, table, col))
        report.append(f"cfg_column {table}.{col} use: {cur.rowcount} row")

    cur.execute("UPDATE cfg_behaviour_rule SET rule_text=? WHERE "
                "rule_key='open-threads-carried-as-escalations'", (RULE_TEXT,))
    report.append(f"cfg_behaviour_rule open-threads-carried-as-escalations restated: "
                  f"{cur.rowcount} row")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        config(cur, report)
        if args.dry_run:
            conn.rollback()
            report.append("DRY RUN -- rolled back, nothing written")
        else:
            conn.commit()
            report.append("committed")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
