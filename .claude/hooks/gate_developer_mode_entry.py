#!/usr/bin/env python
"""Claude Code UserPromptExpansion hook (matcher: "developer-mode"): structurally refuses to
expand the /developer-mode command unless this session both (a) began via a genuinely fresh
SessionStart event ("startup" or "clear" -- not "resume", "compact", or "fork"), and (b) has had
no prior user prompt since that event -- i.e. /developer-mode is the FIRST thing typed.

Why this exists (escalation #1380, researcher instruction 2026-09-02): the command's own
markdown text already told Claude not to self-invoke this mid-session, but that is Claude's own
instruction-following, not enforcement -- proven live 2026-09-02 when a standard-mode session
discussed switching to Developer Mode mid-conversation and nothing external stopped the
discussion. This hook fires BEFORE Claude ever sees the expanded prompt, from the harness itself,
so it cannot be rationalised past the way an in-context rule can.

Fails CLOSED (blocks) on every kind of uncertainty -- missing state file, session_id mismatch,
unrecognised start_source -- deliberately, because for a gate like this a silent false "allow" is
the dangerous failure (looks like protection, isn't), whereas a false "block" is loud and
immediately visible to the researcher, who can then have this fixed rather than unknowingly
relying on a gate that was never actually engaging.

Schema caveat, stated plainly rather than assumed away: Claude Code's public docs do not confirm
(a) the exact UserPromptExpansion matcher-string convention ("developer-mode" vs
"/developer-mode" vs something else) or (b) whether this event fires for custom
`.claude/commands/*.md` commands at all. This hook's actual engagement therefore needs a live
verification pass the first time a real fresh-session /developer-mode is attempted after this
was wired in -- check .claude/.session-boundary-debug.jsonl for a "UserPromptExpansion" line to
confirm it fired, and correct the matcher in .claude/settings.json if it did not. The command's
own markdown carries a redundant, non-structural fallback check for exactly this reason -- belt
and suspenders, not a substitute for this hook actually engaging.
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

    session_id = payload.get("session_id")
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
