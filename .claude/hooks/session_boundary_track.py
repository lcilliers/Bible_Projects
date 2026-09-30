#!/usr/bin/env python
"""Claude Code SessionStart hook: records how the current session began, so a later hook
(gate_developer_mode_entry.py) can refuse to enter Developer Mode unless this session is
genuinely fresh (escalation #1380, researcher instruction 2026-09-02: "developer-mode setup
controls check that when this mode is entered, that it does not start up unless it is a new
session").

Fires on EVERY SessionStart matcher (startup / resume / clear / compact / fork -- no matcher
filter in settings.json) so the state file always reflects the most recent session-boundary
event. Deliberately does not itself judge anything -- it only records. The refusal logic lives
entirely in gate_developer_mode_entry.py, which is the one that can actually block.

Schema note (2026-09-02): Claude Code's public hooks docs do not confirm the exact stdin field
name that carries "which matcher fired" for SessionStart, or whether `session_id` changes across
/clear, /resume, /compact, /fork. Rather than guess a single field name and risk silently
tracking nothing, this script (a) tries several plausible field names, (b) falls back to scanning
all string values in the payload for a literal match against the known matcher vocabulary, and
(c) always appends the FULL raw payload to a debug log so the real shape can be read back and
this script corrected if the guess is wrong. First real fresh-session firing should be checked
against the debug log to confirm.
"""
import json
import os
import sys
from datetime import datetime, timezone

KNOWN_SOURCES = {"startup", "resume", "clear", "compact", "fork"}
CANDIDATE_FIELDS = ("source", "matcher", "trigger", "start_source", "session_start_source", "reason")


def _guess_start_source(payload: dict) -> str | None:
    for field in CANDIDATE_FIELDS:
        val = payload.get(field)
        if isinstance(val, str) and val in KNOWN_SOURCES:
            return val
    # Fallback: scan every string value in the payload for a literal match.
    for val in payload.values():
        if isinstance(val, str) and val in KNOWN_SOURCES:
            return val
    return None


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

    # Debug trail first -- must survive even if the rest of this hook fails.
    try:
        with open(debug_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"hook": "SessionStart", "at": now, "raw": payload}) + "\n")
    except Exception:
        pass

    start_source = _guess_start_source(payload)
    session_id = payload.get("session_id")
    state = {
        "session_id": session_id,
        "start_source": start_source,
        "at": now,
        "first_prompt_id": None,  # reset every session-boundary event; set by track_prompt_submit.py
        "raw_keys_seen": sorted(payload.keys()),
    }
    try:
        os.makedirs(claude_dir, exist_ok=True)
        with open(state_path, "w", encoding="utf-8") as fh:
            json.dump(state, fh, indent=2)
    except Exception:
        pass  # never block session start on this hook's own failure

    # Per-session record (escalation #1894, option A, 2026-09-30). The shared file above is
    # overwritten by whichever session in this folder started or resumed last, so it cannot
    # tell sessions apart. This copy is keyed by session_id and is what session.close and
    # gate_developer_mode_entry.py read. `first_seen_at` keeps the earliest boundary event
    # for this session_id (the start of the whole session, across resumes).
    if session_id:
        per_session_dir = os.path.join(claude_dir, "session-boundary")
        per_session_path = os.path.join(per_session_dir, f"{session_id}.json")
        first_seen_at = now
        try:
            with open(per_session_path, "r", encoding="utf-8") as fh:
                first_seen_at = json.load(fh).get("first_seen_at") or now
        except Exception:
            pass
        try:
            os.makedirs(per_session_dir, exist_ok=True)
            with open(per_session_path, "w", encoding="utf-8") as fh:
                json.dump({**state, "first_seen_at": first_seen_at}, fh, indent=2)
        except Exception:
            pass

    print(json.dumps({}))


if __name__ == "__main__":
    main()
