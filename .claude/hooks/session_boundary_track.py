#!/usr/bin/env python
"""Claude Code SessionStart hook: records how the current session began, so
gate_developer_mode_entry.py can refuse Developer Mode unless this session is fresh (#1380).

Fires on every SessionStart (startup / resume / clear / compact / fork; no matcher filter) so the
state reflects the latest boundary event. It only records; the refusal is in
gate_developer_mode_entry.py.

The start source is read from the payload's `source` field, with fallbacks to other field names and to
a scan of the payload's string values for the known matcher vocabulary; the full raw payload is
appended to a debug log.
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

    # Per-session record (#1894): keyed by session_id (the shared file above is overwritten by
    # whichever session started last); session.close and gate_developer_mode_entry.py read it.
    # `first_seen_at` keeps the earliest boundary event for this session_id.
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
