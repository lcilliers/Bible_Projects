"""escalation_thread_config_corrections_v1_20261012.py -- escalation #2000: config texts left stale
by the thread lifecycle build (BUILD.md s338), found in the #2106 review.

Every write goes through configmaint.apply_logged(), so each is in cfg_change_detail (Developer
Mode removes propose's approval gate, never the audit).

  - cfg_table use: escalation_thread_item ("open/closed") and escalation_thread_item_response (the
    response kinds) did not name withdrawn/superseded.
  - cfg_escalation_transition notes: T3/T5 and T6 said "closed"; an item is now settled by
    closed, withdrawn or superseded.
  - cfg_status_flow on-hold set_by: "items partly closed" -> partly settled (the "thread, T6" key
    the transition row resolves through is kept).
  - cfg_column use: escalation_thread_item.opened_by and escalation_thread_item_response.
    via_escalation can now hold a thread (an item carried over on supersede).
  - cfg_behaviour_rule 74 enforced_by: named neither the transition and requirement rows nor the
    lifecycle mechanisms.

Root fix (same run): new cfg_behaviour_rule (development) devmode-config-writes-are-audited --
every Developer Mode cfg_* write goes through configmaint.apply_logged().

Idempotent: a row already holding the target text is skipped (no log row). One transaction.

Usage:
    python iba/app/migration/escalation_thread_config_corrections_v1_20261012.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2000-CONFIG-CORRECTIONS-20261012"

CHANGES = [
    ("cfg_table", {"database": "iba", "name": "escalation_thread_item"}, {"use": (
        "One row per item of a thread (type='thread' escalation): what a strand or task is matched "
        "against, and the item's current status only: open, or settled as closed (answered), "
        "withdrawn (no longer relevant) or superseded (carried by another item or thread). Every "
        "response, including each settlement, is a row in escalation_thread_item_response. "
        "escalation #2000 (proposal v3 sec3.2, sec3.4; thread lifecycle, BUILD.md s338).")}),
    ("cfg_table", {"database": "iba", "name": "escalation_thread_item_response"}, {"use": (
        "One row per response to a thread item: touched, narrowed, forward, ruling, note, closed, "
        "reopened, withdrawn, superseded. Nothing is overwritten; each response is also written in "
        "full to the thread's history. escalation #2000 (proposal v3 sec3.3, approved round 5; "
        "thread lifecycle, BUILD.md s338).")}),
    ("cfg_escalation_transition", {"shape": "manual",
                                   "condition_key": "thread_items_changed_and_referenced"},
     {"notes": (
        "escalation #2000 T3/T5: a thread whose items change this call (an item added, settled -- "
        "closed, withdrawn or superseded -- or reopened, or the state of the task/issue an "
        "'escalation' item references changed) while an in-progress task or issue references it "
        "moves to in-progress. A reference from a raised or on-hold task waits until that task is "
        "started (round 2: 'in-progress only'). Mutually exclusive with the other priority-0 rows.")}),
    ("cfg_escalation_transition", {"shape": "manual",
                                   "condition_key": "thread_items_changed_partly_closed"},
     {"notes": (
        "escalation #2000 T6: items settled this call (closed, withdrawn or superseded), other "
        "items still open, and no in-progress work references the thread -> on-hold (partial "
        "settlement). When none is left open, thread_items_all_settled completes the thread "
        "instead. Mutually exclusive with the other priority-0 rows.")}),
    ("cfg_status_flow", {"entity": "escalation", "status": "on-hold"}, {"set_by": (
        "either party directly (Update state=on-hold); OR dispatcher-tied answer_for_run "
        "decision=hold; OR system (thread, T6): items partly settled (closed, withdrawn or "
        "superseded) and no in-progress work references the thread (escalation #2000)")}),
    ("cfg_column", {"database": "iba", "table_name": "escalation_thread_item", "name": "opened_by"},
     {"use": (
        "the escalation under which the item was added: a task or issue (e.g. a forward under "
        "#1998), or the superseded thread an item was carried over from; NULL when added with the "
        "thread itself")}),
    ("cfg_column", {"database": "iba", "table_name": "escalation_thread_item_response",
                    "name": "via_escalation"},
     {"use": (
        "the escalation whose work gave the response, e.g. 1998; for a task's own ending, that "
        "task; for an item carried over on supersede, the other thread")}),
    ("cfg_behaviour_rule", {"rule_key": "open-threads-carried-as-escalations"}, {"enforced_by": (
        "Escalation.ps1 (-Type thread; -Action Thread/Match/ThreadCheck/Export; -Item/-AddItem/"
        "-Respond/-ResponseKind/-SupersededBy on Update); lib/escalation.py; cfg_escalation rows "
        "thread_check_before_work/raise_state_choice/thread_completion/resolution_precedence; "
        "cfg_escalation_transition priority-0 thread rows and thread_reassigned; "
        "cfg_escalation_requirement thread_type/thread_superseding rows; cfg_enum thread item "
        "kinds/statuses/response kinds; GOVERNANCE.md s93. Not mechanical: that a strand checks "
        "Match before a unit pull, and that researcher feedback in chat is recorded the same turn.")}),
]


NEW_RULE = {
    "class": "development",
    "rule_key": "devmode-config-writes-are-audited",
    "rule_text": (
        "Developer Mode removes configmaint.propose's per-row approval gate, never the config audit. "
        "Every cfg_* write made in a Developer Mode session (a migration, a one-off script) goes "
        "through iba.app.handlers.configmaint.apply_logged(conn, run_id, table, op, where, set), "
        "the same audited write propose uses after approval, so cfg_change_detail records the "
        "table, op, where, set, the row's prior state and when. The run_id names the session's "
        "work (e.g. DEVMODE-<escalation>-<what>-<date>). Found 2026-10-12 (#2000): three migrations "
        "had written cfg_* directly, leaving 87 changes with no audit row; they were backfilled "
        "from a pre-change copy of iba.db (DEVMODE-2000-BACKFILL-20261012)."),
    "source": ("researcher, 2026-10-12, #2106: 'there are something in the configs that you have "
               "not done properly' -- the unlogged Developer Mode writes, found in that review"),
    "enforced_by": ("configmaint.apply_logged (the shared write); GOVERNANCE.md s69; the "
                    "developer-mode command (step 3). No mechanical check that a direct write did "
                    "not happen."),
    "added_at": "2026-10-12T00:00:00Z",
    "active": 1,
    "enforcement_status": "context_delivered",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    report: list[str] = []
    try:
        conn.execute("BEGIN")
        for table, where, set_ in CHANGES:
            wsql = " AND ".join(f'"{k}"=?' for k in where)
            rows = conn.execute(f'SELECT {",".join(chr(34)+c+chr(34) for c in set_)} FROM "{table}" '
                                f'WHERE {wsql}', list(where.values())).fetchall()
            if len(rows) != 1:
                raise RuntimeError(f"{table} {where}: {len(rows)} row(s), expected 1")
            if list(rows[0]) == list(set_.values()):
                report.append(f"{table} {where}: already current -- skipped")
                continue
            apply_logged(conn, RUN_ID, table, "update", where, set_)
            report.append(f"{table} {where}: updated, logged")
        if conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
                        (NEW_RULE["class"], NEW_RULE["rule_key"])).fetchone():
            report.append(f"cfg_behaviour_rule {NEW_RULE['rule_key']}: present -- skipped")
        else:
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {}, NEW_RULE)
            report.append(f"cfg_behaviour_rule {NEW_RULE['rule_key']}: inserted, logged")
        if args.dry_run:
            conn.rollback()
            report.append("DRY RUN -- rolled back, nothing written")
        else:
            conn.commit()
            report.append(f"committed under {RUN_ID}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
