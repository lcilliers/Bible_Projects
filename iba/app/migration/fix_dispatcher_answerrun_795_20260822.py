"""fix_dispatcher_answerrun_795_20260822.py — ONE-OFF, idempotent. Escalation #795, items 1-4,
researcher instruction 2026-08-22 (verbatim, item 1-2): "Calling AnswerRun with approve, reject, or
revise all land on the same completed state is still not solved then solve it. it is a bug. that is
not the correct behaviour... the runid should be allowed to use the number". Item 3, researcher
2026-08-22 (verbatim, on the A/B routing question): "I suggest to check and test the answer to the
question in the configs, my expectation is that it should not be possible and that the configs
should now state that." Item 4 found checking item 3, not separately instructed -- the approved
spec already required it and #799 never built it.

Fixes four real defects in the dispatcher-tied (`run_id` set) AnswerRun path, unchanged since the
escalation-module-rebuild-20260820 and untouched by #798/#799's resolution_kind build (that build
added an alternate route via Update for decision_required items; it never closed the AnswerRun
route off for them, and never built the self_correctable refusal its own approved spec required):

  (1) `cfg_escalation_transition` for shape='dispatcher' had one catch-all rule (next_action=None)
      matching approve/reject/revise alike -> 'dispatcher-tied default' -> status 'completed'.
      Replaced with three specific rules, each resolving to the status its own MANUAL-shape
      equivalent already uses: approve -> completed (unchanged outcome), reject -> withdraw
      (matches manual shape's reject default), revise -> in-progress (matches manual shape's
      revise -> in-progress exactly).
  (2) `pending_for_run()` (iba/app/lib/escalation.py) only matched the literal `run_id` column --
      fixed separately, in code (see that function's own docstring). This script only carries the
      config half of the fix (1).
  (3) Checked live before fixing (escalation #820): `answer_for_run()` had NO guard against
      answering a `resolution_kind='decision_required'` item -- confirmed a flat 'approve' silently
      succeeded on one, the same one-line outcome a self_correctable item gets, collapsing the
      record of a genuine judgement call. Fixed in code (`answer_for_run()`, mirrors `update()`'s
      own opposite-direction carve-out).
  (4) Checked live before fixing (escalation #822): the ORIGINAL approved proposal
      (escalation-decision-vs-defect-axis-proposal-v4-20260822.md §6 + its own §11 Stage 2 test)
      already required `self_correctable` items to have no reachable AnswerRun path at all --
      never built, never tested, in #799. Confirmed the same way as (3): a flat 'approve'
      succeeded with no refusal. Fixed in code -- AnswerRun now refuses BOTH resolution_kind
      values, matching what the approved spec specified throughout.

This script adds/updates the single `cfg_behaviour_rule` row that states the combined (3)+(4)
policy, per the researcher's explicit instruction that the configs should say so, not just the
code.

    python -m iba.app.migration.fix_dispatcher_answerrun_795_20260822
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_MIGRATION_FILE = "iba/app/migration/fix_dispatcher_answerrun_795_20260822.py"


def _replace_catch_all(conn, report: list[str]) -> None:
    row = conn.execute(
        "SELECT priority FROM cfg_escalation_transition WHERE shape='dispatcher' AND "
        "next_action IS NULL AND active=1").fetchone()
    if row is None:
        already = conn.execute(
            "SELECT 1 FROM cfg_escalation_transition WHERE shape='dispatcher' AND "
            "next_action='approve' AND resulting_status_key='decision=approve'").fetchone()
        if already:
            report.append("cfg_escalation_transition already split (approve/reject/revise) — no change")
        else:
            report.append("WARNING: no dispatcher catch-all row found, and no split rows either — "
                          "check cfg_escalation_transition by hand")
        return
    conn.execute(
        "DELETE FROM cfg_escalation_transition WHERE shape='dispatcher' AND next_action IS NULL")
    conn.executemany(
        "INSERT INTO cfg_escalation_transition "
        "(priority, shape, next_action, condition_key, resulting_status_key, notes, active) "
        "VALUES (?,?,?,?,?,?,1)",
        [
            (3, "dispatcher", "approve", "always", "decision=approve",
             "escalation #795 fix, 2026-08-22: was the shared catch-all with reject/revise "
             "(collapsed all three into 'completed'). approve keeps that outcome on its own."),
            (4, "dispatcher", "reject", "always", "decision=reject",
             "escalation #795 fix, 2026-08-22: previously collapsed into 'completed' along with "
             "approve/revise. Now resolves to 'withdraw', matching the manual shape's own reject "
             "default (cfg_escalation_transition shape='manual' priority 2)."),
            (5, "dispatcher", "revise", "always", "decision=revise",
             "escalation #795 fix, 2026-08-22: previously collapsed into 'completed' along with "
             "approve/reject. Now resolves to 'in-progress', matching the manual shape's own "
             "revise -> in-progress rule exactly (cfg_escalation_transition shape='manual' "
             "priority 3)."),
        ])
    report.append("cfg_escalation_transition: dispatcher catch-all (priority 3, next_action=NULL) "
                  "replaced with 3 specific rules (approve/reject/revise)")


def _retarget_status_flow(conn, report: list[str]) -> None:
    updates = [
        ("completed",
         "system: manual next_action=approved+resolution present; OR: dispatcher-tied "
         "answer_for_run decision=approve",
         "system: manual next_action=approved+resolution present; OR: dispatcher-tied default "
         "(answer_for_run, decision not hold/noted)"),
        ("withdraw",
         "party's explicit choice at Update: next_action=reject, state=withdraw; OR: "
         "dispatcher-tied answer_for_run decision=reject (escalation #795 fix, 2026-08-22)",
         "party's explicit choice at Update: next_action=reject, state=withdraw"),
        ("in-progress",
         "either party directly (Update state=in-progress); OR system: next_action=revise; OR "
         "dispatcher-tied answer_for_run decision=revise (escalation #795 fix, 2026-08-22)",
         "either party directly (Update state=in-progress); OR system: next_action=revise"),
    ]
    for status, new_text, old_text in updates:
        row = conn.execute(
            "SELECT set_by FROM cfg_status_flow WHERE entity='escalation' AND status=?",
            (status,)).fetchone()
        if row is None:
            report.append(f"WARNING: cfg_status_flow entity=escalation status={status!r} not found")
            continue
        if row[0] == new_text:
            report.append(f"cfg_status_flow escalation/{status}: already updated — no change")
        elif row[0] == old_text:
            conn.execute(
                "UPDATE cfg_status_flow SET set_by=? WHERE entity='escalation' AND status=?",
                (new_text, status))
            report.append(f"cfg_status_flow escalation/{status}: set_by text updated")
        else:
            report.append(f"WARNING: cfg_status_flow escalation/{status}.set_by does not match "
                          f"either the expected old or new text — left untouched, check by hand: "
                          f"{row[0]!r}")


_RULE_TEXT = (
    "AnswerRun's flat approve/reject/revise/hold/noted vocabulary is refused for BOTH "
    "resolution_kind values -- unreachable for any dispatcher-tied escalation raised under the "
    "resolution_kind regime. decision_required must be answered through Update's richer "
    "vocabulary (ready_for_approval -> approved; -State on-hold; next_action=reject/revise/noted) "
    "-- checked and confirmed live before this half existed (escalation #820): AnswerRun silently "
    "accepted a flat 'approve' on a decision_required item, collapsing the record of a genuine "
    "judgement call into the same one-line outcome a self_correctable item gets. self_correctable "
    "must be closed via resolve-self-correctable, or converted via escalate-to-decision -- this "
    "was always the APPROVED spec (escalation-decision-vs-defect-axis-proposal-v4-20260822.md §6: "
    "'No approve/reject/revise/hold/noted vocabulary. AnswerRun is never invoked' -- and its own "
    "§11 Stage 2 test named this exact check), never actually built or tested during #799's Stage "
    "2 -- confirmed live the same way (escalation #822): a flat 'approve' succeeded with no "
    "refusal at all. Net effect: neither kind ever had a genuine use for AnswerRun's original "
    "'answer and resume the same run' semantics -- decision_required runs terminate and never "
    "resume (a fresh run is the test, §5); self_correctable never carried decision vocabulary to "
    "begin with (§6).")

_RULE_SOURCE = (
    "researcher, 2026-08-22, escalation #795, on decision_required: \"I suggest to check and test "
    "the answer to the question in the configs, my expectation is that it should not be possible "
    "and that the configs should now state that.\" The self_correctable half was already in the "
    "approved proposal (v4 §6/§11 Stage 2) but never built or tested in #799 -- found checking the "
    "first half, not separately instructed.")

_RULE_ENFORCED_BY = (
    "iba/app/lib/escalation.py answer_for_run() -- refuses at the top of the function if "
    "esc_row['resolution_kind'] is 'decision_required' OR 'self_correctable' (i.e. always, since "
    "resolution_kind is required at every Raise). The mirror-image guard, update()'s own "
    "dispatcher carve-out (refuses UNLESS resolution_kind='decision_required'), already existed "
    "from #798/#799 and is unchanged.")


def _behaviour_rule(conn, report: list[str]) -> None:
    class_, rule_key = "development", "decision-required-answered-via-update-not-answerrun"
    row = conn.execute(
        "SELECT rule_text FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
        (class_, rule_key)).fetchone()
    if row is None:
        conn.execute(
            "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
            "added_at, active) VALUES (?,?,?,?,?,datetime('now'),1)",
            (class_, rule_key, _RULE_TEXT, _RULE_SOURCE, _RULE_ENFORCED_BY))
        report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) added")
    elif row[0] != _RULE_TEXT:
        conn.execute(
            "UPDATE cfg_behaviour_rule SET rule_text=?, source=?, enforced_by=? WHERE class=? AND "
            "rule_key=?", (_RULE_TEXT, _RULE_SOURCE, _RULE_ENFORCED_BY, class_, rule_key))
        report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) text updated -- widened to cover "
                      f"both resolution_kind halves")
    else:
        report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) already present, text current")


def _utility(conn, report: list[str]) -> None:
    if not conn.execute(
            "SELECT 1 FROM cfg_utility WHERE file_path=?", (_MIGRATION_FILE,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "config_exempt_reason, crash_escalation_reviewed) VALUES (?,?,?,0,1,?,0)",
            ("fix_dispatcher_answerrun_795", _MIGRATION_FILE,
             "Escalation #795: split the dispatcher shape's collapsed approve/reject/revise "
             "transition into 3 distinct rules, and retargeted cfg_status_flow to match.",
             "one-off migration script -- writes directly into cfg_* tables via raw sqlite3, same "
             "class as cfgload.py"))
        report.append(f"cfg_utility {_MIGRATION_FILE!r} registered")
    else:
        report.append(f"cfg_utility {_MIGRATION_FILE!r} already registered")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []
    _replace_catch_all(conn, report)
    _retarget_status_flow(conn, report)
    _behaviour_rule(conn, report)
    _utility(conn, report)
    conn.commit()
    conn.close()
    print("fix_dispatcher_answerrun_795_20260822:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
