#!/usr/bin/env python
"""Claude Code Stop hook: surfaces the IBA escalation backlog assigned to Claude before a turn ends,
so an open item cannot simply be forgotten.

Blocks the stop ONCE per turn (Claude Code sets `stop_hook_active: true` on the retry after a block,
checked below, so it never traps a turn); a non-blocking note would arrive after the response is
already generated.

Not filtered by age: genuine multi-session work also sits at next_action_assigned_to='Claude', so the
message asks for a triage (acknowledge, or do the cycle), not a full resolution of every item.
Threads at on-hold are left out (they rest there by design; only an in-progress thread counts as work
first, cfg_escalation 4 / T5); every other type counts.

Never blocks on its own failure: a DB lock, a missing file or a query error allows the stop, so a
broken check never becomes a way to get stuck."""
import json
import os
import sqlite3
import sys


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    if payload.get("stop_hook_active"):
        print(json.dumps({}))
        return

    project_dir = (
        payload.get("cwd")
        or os.environ.get("CLAUDE_PROJECT_DIR")
        or os.getcwd()
    )
    db_path = os.path.join(project_dir, "iba", "app", "db", "iba.db")

    try:
        if not os.path.isfile(db_path):
            print(json.dumps({}))
            return
        conn = sqlite3.connect(db_path, timeout=2)
        conn.row_factory = sqlite3.Row
        # #2173 G1: the not-yet-closed states (open + parked) come from cfg_enum, not a literal list
        live = [r[0] for r in conn.execute(
            "SELECT value FROM cfg_enum WHERE name IN ('escalation_state_open', "
            "'escalation_state_parked') AND inactive=0")] or \
            ["raised", "in-progress", "re-assigned", "on-hold"]
        rows = conn.execute(
            "SELECT id, type, state, next_action, short_description FROM escalation "
            "WHERE next_action_assigned_to='Claude' "
            f"AND state IN ({','.join('?' * len(live))}) "
            "AND NOT (type='thread' AND state!='in-progress') "   # #2000, cfg_escalation 4 / T5
            "ORDER BY id", live
        ).fetchall()
        conn.close()
    except Exception:
        # The check itself breaking must never become a new reason to get stuck.
        print(json.dumps({}))
        return

    if not rows:
        print(json.dumps({}))
        return

    lines = [
        f"#{r['id']} ({r['type']}, {r['state']}/{r['next_action']}): {r['short_description']}"
        for r in rows
    ]
    reason = (
        f"Escalation backlog check (automatic, not a memory rule): {len(rows)} open item(s) "
        f"currently assigned to Claude (next_action_assigned_to='Claude') in iba.db:\n"
        + "\n".join(lines)
        + "\n\nBefore finishing this turn, for each one: either (1) it's genuinely ongoing "
        "multi-session work already in motion and just needs a one-line acknowledgement of why "
        "it's untouched this turn -- fine to leave as-is -- or (2) if it's actually actionable "
        "right now, DO the cycle (cfg_behaviour_rule 'claude-held-item-must-progress-or-bounce-"
        "back'), don't just mention it: complete the work and move it forward (ready_for_approval), "
        "or write a comment and reassign it to the Researcher. Merely naming an item as 'open' "
        "without doing one of those two things is not enough -- that already happened once "
        "(2026-08-31) and produced no actual progress."
        "\n\nBefore handing any item to the Researcher for approval (escalation #2178, rule 63): "
        "ask (a) what exactly is the researcher to approve, (b) is it ready for approval -- "
        "finished work or a decision with its options, not work the researcher told Claude to "
        "carry -- and (c) does the resolution state plainly what approval is sought. If not, do "
        "not hand it over: clearing this check is never a reason to. For an interim approval "
        "whose result needs a further action by Claude, pass -NeedsFollowup 1 in the same call, "
        "so `approved` routes it back to Claude and does not close a step in progress."
    )
    print(json.dumps({"decision": "block", "reason": reason}))


if __name__ == "__main__":
    main()
