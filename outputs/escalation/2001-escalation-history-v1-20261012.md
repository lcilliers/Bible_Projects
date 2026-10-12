# Escalation deep history

## #2001 — Developer-mode gate bypassed by Skill tool invocation
type=task source=researcher

**v1** (2026-10-12T11:04:28Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Developer-mode gate bypassed by Skill tool invocation
> **comment (set this version):** Found 2026-10-12 (#2000 session). Claude invoked the developer-mode skill mid-session through the Skill tool. The session-freshness gate (.claude/hooks/gate_developer_mode_entry.py, wired as a UserPromptExpansion hook in .claude/settings.json) only fires when the researcher types the command, so it never ran; .claude/.session-boundary-state.json already held a first_prompt_id, so a typed invocation would have been refused. The skill text itself says to stop if the session did not start this way, and Claude stopped before any build. Also found: .claude/.developer-mode-active exists, dated 2026-09-30 13:44 (stale from an earlier session), so the statusline may show DEVELOPER MODE when it is not active. Needs: a design decision on closing the Skill-tool path (e.g. a PreToolUse hook on Skill for developer-mode, or disable-model-invocation on the skill), and clearing the stale marker. No change made.
