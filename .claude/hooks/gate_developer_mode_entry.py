#!/usr/bin/env python
"""Claude Code UserPromptExpansion hook (matcher: "developer-mode"): refuses to expand the
/developer-mode command unless this session (a) began via a fresh SessionStart ("startup" or
"clear", not "resume", "compact" or "fork") and (b) has had no prior user prompt since -- i.e.
/developer-mode is the first thing typed (#1380). It runs in the harness before Claude sees the
prompt, so it cannot be argued past the way an in-context rule can.

Fails CLOSED on any uncertainty (missing state file, session_id mismatch, unrecognised start_source):
a false block is visible and fixable; a false allow is not. The command's own markdown carries a
redundant fallback check.
"""
import json
import os
import sys
from datetime import datetime, timezone

FRESH_SOURCES = {"startup", "clear"}


def _block(reason: str) -> None:
    print(json.dumps({
        "decision": "block",
        "reason": reason,
        "hookSpecificOutput": {
            "hookEventName": "UserPromptExpansion",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        },
    }))


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
            fh.write(json.dumps({"hook": "UserPromptExpansion", "at": now, "raw": payload}) + "\n")
    except Exception:
        pass

    # this session's own record (#1894), not the shared .session-boundary-state.json, which another
    # session resuming later would overwrite
    session_id = payload.get("session_id")
    if session_id:
        state_path = os.path.join(claude_dir, "session-boundary", f"{session_id}.json")
    try:
        with open(state_path, "r", encoding="utf-8") as fh:
            state = json.load(fh)
    except Exception:
        _block(
            "Developer Mode entry refused: no session-boundary state record found "
            f"(expected {state_path}). This mechanism (escalation #1380) fails closed when it "
            "cannot confirm freshness -- if this session genuinely just started, the "
            "session_boundary_track.py SessionStart hook may not have fired or may not be wired "
            "correctly in .claude/settings.json. Check .claude/.session-boundary-debug.jsonl."
        )
        return

    if state.get("session_id") != session_id:
        _block(
            "Developer Mode entry refused: the recorded session-boundary state belongs to a "
            f"different session_id ({state.get('session_id')!r}) than this request "
            f"({session_id!r}). Cannot confirm this session is fresh -- refusing rather than "
            "guessing."
        )
        return

    start_source = state.get("start_source")
    if start_source not in FRESH_SOURCES:
        _block(
            f"Developer Mode entry refused: this session began via {start_source!r}, not a "
            "fresh 'startup' or 'clear'. Developer Mode may only be entered at the start of a "
            "new or cleared session -- a resumed, compacted, or forked session is a continuation "
            "of prior work, not a fresh session boundary (escalation #1380)."
        )
        return

    first_prompt_id = state.get("first_prompt_id")
    current_prompt_id = payload.get("prompt_id")
    if first_prompt_id is not None and current_prompt_id is not None and first_prompt_id != current_prompt_id:
        _block(
            "Developer Mode entry refused: this session already had at least one prior prompt "
            f"(first recorded prompt_id={first_prompt_id!r}) before this /developer-mode "
            f"invocation (prompt_id={current_prompt_id!r}). Developer Mode must be the first "
            "thing typed in a fresh session, not invoked mid-conversation (escalation #1380)."
        )
        return

    # Fresh session boundary + no recorded prior prompt -- allow the expansion through.
    print(json.dumps({}))


if __name__ == "__main__":
    main()
