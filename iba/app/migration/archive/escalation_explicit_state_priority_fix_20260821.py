"""escalation_explicit_state_priority_fix_20260821.py — fixes escalation #762: a caller's explicit
`-State` (on-hold/in-progress/closed/withdraw/supersede) was silently losing to the
`assignee_changed` inference whenever both were supplied in the same `Update` call.

Found live: researcher ran
    Escalation.ps1 -Action Update -Id 737 -NextAction review -AssignedTo Researcher
        -State on-hold -Comment "on hold until analysis phase start"
and got `state='re-assigned'`, not `on-hold`. Root cause: `cfg_escalation_transition` priority 6
(manual, `next_action=None` — matches ANY next_action, same as the catch-all — condition
`assignee_changed`) fired before priority 7's catch-all, the only rule that honours the caller's
own `-State`. `#737`'s `next_action_assigned_to` genuinely changed (`Claude` -> `Researcher`), so
`assignee_changed=True`, and that rule won regardless of the explicit `-State` given.

Fix: a new condition_key `explicit_state_given` (code: `_condition_true()`/`_evaluate_transition()`
in `lib/escalation.py`, this same commit) — a new priority-6 row checks it BEFORE
`assignee_changed`, so an explicit `-State` now always wins over the inferred reassignment result.
`assignee_changed`/catch-all shift to priority 7/8.

    python -m iba.app.migration.escalation_explicit_state_priority_fix_20260821
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    conn.execute("DELETE FROM cfg_escalation_transition WHERE shape='manual'")
    conn.executemany(
        "INSERT INTO cfg_escalation_transition (priority, shape, next_action, condition_key, "
        "resulting_status_key, notes, active) VALUES (?,?,?,?,?,?,1)", [
        (1, "manual", "approved", "has_resolution", "next_action=approved",
         "resolution present (this call or a prior one) -> completed"),
        (2, "manual", "reject", "always", "__explicit__",
         "state comes from the caller's own explicit withdraw|supersede choice, not a lookup"),
        (3, "manual", "revise", "always", "next_action=revise", None),
        (4, "manual", "noted", "always", "next_action=noted", None),
        (5, "manual", "ready_for_approval", "always", "no more specific rule",
         "D27 (register v9): ready_for_approval resolves explicitly regardless of whether the "
         "assignee happened to change this call."),
        (6, "manual", None, "explicit_state_given", "__unchanged__",
         "escalation #762, 2026-08-21: the caller's own explicit -State must outrank an INFERRED "
         "assignee_changed result, not lose to it -- '-AssignedTo X -State on-hold' was silently "
         "landing on re-assigned. Sits ahead of assignee_changed for exactly this. Only 'review' "
         "or no next_action can still reach this priority (approved/reject/revise/noted/"
         "ready_for_approval are all already intercepted by priorities 1-5 above)."),
        (7, "manual", None, "assignee_changed", "no more specific rule",
         "was priority 6 pre-fix -- any bare reassignment not otherwise matched, and with no "
         "explicit -State given"),
        (8, "manual", None, "always", "__unchanged__",
         "was priority 7 pre-fix -- no rule matched, state carries forward (or the caller's "
         "explicit -State, redundant with priority 6 above but kept as the final safety net)"),
    ])
    print("cfg_escalation_transition: manual shape rebuilt, 8 rows (new priority-6 "
         "explicit_state_given row; old 6/7 renumbered to 7/8)")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
