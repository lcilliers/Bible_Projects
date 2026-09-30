#!/usr/bin/env python
"""Claude Code UserPromptSubmit hook: records the id of the FIRST user prompt seen since the
last session-boundary event, so gate_developer_mode_entry.py can tell "this /developer-mode
invocation IS the first thing in this session" apart from "this session already had other
activity" (escalation #1380). Part of the same three-file mechanism as
session_boundary_track.py and gate_developer_mode_entry.py -- read that file's docstring for the
full design rationale, including the schema-uncertainty handling.

Never blocks (UserPromptSubmit CAN block per the docs, but this hook's only job is recording --
the actual refusal happens in gate_developer_mode_entry.py). Fires on every user turn, no
matcher filter.

Deliberately uses prompt_id EQUALITY rather than a turn counter: whether or not this hook and
UserPromptExpansion both fire for the same slash-command turn (undocumented, and in which order)
does not matter -- either way, the first prompt_id recorded after a fresh session-boundary event
is the one the gate compares against, and if nothing has been recorded yet the gate treats that
as "nothing came before this" rather than failing closed on an implementation detail it can't
control.
"""
import json
import os
import sys
from datetime import datetime, timezone


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    project_dir = (
        payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    )
    claude_dir = os.path.join(project_dir, ".claude")
    state_path = os.path.join(claude_dir, ".session-boundary-state.json")
    debug_path = os.path.join(claude_dir, ".session-boundary-debug.jsonl")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    try:
        with open(debug_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"hook": "UserPromptSubmit", "at": now, "raw": payload}) + "\n")
    except Exception:
        pass

    try:
        with open(state_path, "r", encoding="utf-8") as fh:
            state = json.load(fh)
    except Exception:
        # No SessionStart record yet -- nothing safe to do; let gate_developer_mode_entry.py's
        # own fail-closed handling of a missing/unreadable state file be the one place that
        # decides what "no record" means.
        print(json.dumps({}))
        return

    session_id = payload.get("session_id")
    prompt_id = payload.get("prompt_id")

    if state.get("session_id") == session_id and state.get("first_prompt_id") is None and prompt_id:
        state["first_prompt_id"] = prompt_id
        try:
            with open(state_path, "w", encoding="utf-8") as fh:
                json.dump(state, fh, indent=2)
        except Exception:
            pass

    # Per-session record (escalation #1894): same update, on this session's own file, which
    # gate_developer_mode_entry.py reads. Not affected by other sessions starting later.
    if session_id and prompt_id:
        per_session_path = os.path.join(claude_dir, "session-boundary", f"{session_id}.json")
        try:
            with open(per_session_path, "r", encoding="utf-8") as fh:
                per_state = json.load(fh)
            if per_state.get("first_prompt_id") is None:
                per_state["first_prompt_id"] = prompt_id
                with open(per_session_path, "w", encoding="utf-8") as fh:
                    json.dump(per_state, fh, indent=2)
        except Exception:
            pass

    print(json.dumps({}))


if __name__ == "__main__":
    main()
