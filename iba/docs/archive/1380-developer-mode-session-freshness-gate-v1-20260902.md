# Developer Mode — session-freshness entry gate (v1)

**Date:** 2026-09-02
**Escalation:** #1380 ("Developer Mode: session-boundary enforcement flag") — this document covers
the **entry-boundary half only**, per researcher instruction (chat, 2026-09-02): *"first is to
focus on 1380 and ensure that the developer-mode setup controls check that when this mode is
entered, that it does not start up unless it is a new session."* The **exit-boundary half**
(preventing App Mode continuing in the same conversation after `/exit-developer-mode` without an
explicit session-end) is explicitly **out of scope here** and remains open on #1380.

## Problem

`.claude/commands/developer-mode.md` already told Claude, in prose, not to self-invoke Developer
Mode mid-session. That is Claude's own instruction-following, not enforcement — proven live
2026-09-02 (a standard-mode session discussed switching to Developer Mode mid-conversation, and
nothing external stopped the discussion; only Claude choosing to honour the written rule would
have). #1380's own prior-rejected-design note is explicit: avoid a check Claude itself performs
and can talk itself past — lean structural.

## Design

Three small Python hook scripts under `.claude/hooks/`, wired into `.claude/settings.json`,
sharing one gitignored state file `.claude/.session-boundary-state.json`:

1. **`session_boundary_track.py`** — `SessionStart` hook, no matcher filter (fires on every
   `startup` / `resume` / `clear` / `compact` / `fork`). Records `session_id`, a best-guess
   `start_source`, and resets `first_prompt_id` to `null` on every firing.
2. **`track_prompt_submit.py`** — `UserPromptSubmit` hook, no matcher filter (fires on every user
   turn). If the state file's `first_prompt_id` is still `null` for the current `session_id`, sets
   it to the current turn's `prompt_id` — i.e. records "the first prompt seen since the last
   session-boundary event," whatever it turns out to be.
3. **`gate_developer_mode_entry.py`** — `UserPromptExpansion` hook, `matcher: "developer-mode"`
   (fires, per the docs, "when a user-typed command expands into a prompt, before it reaches
   Claude" — i.e. before the `/developer-mode` command's own text is even read). Refuses
   (`{"decision":"block", ...}`) unless:
   - the state file's `session_id` matches this request's `session_id`,
   - `start_source` is `startup` or `clear` (not `resume`/`compact`/`fork`), AND
   - `first_prompt_id` is either unset or equal to this request's own `prompt_id` (i.e. nothing
     came before this turn).

   **Fails closed on every uncertainty** — missing state file, session_id mismatch, unrecognised
   `start_source` — deliberately: a silent false "allow" is the dangerous failure for a gate like
   this (looks like protection, isn't); a false "block" is loud and immediately visible, and gets
   fixed rather than quietly relied upon.

`.claude/commands/developer-mode.md` §"Do not invoke this mid-session" now documents this hook as
the real mechanism, with the existing prose kept only as a non-structural fallback.

## Known limitation — stated plainly, not glossed over

Claude Code's public hooks documentation does **not** confirm two things this design depends on:

- the exact `UserPromptExpansion` matcher-string convention (`"developer-mode"` vs
  `"/developer-mode"` vs something else), or
- whether `UserPromptExpansion` fires for custom `.claude/commands/*.md` commands at all (the
  docs's own example used a generic command name without confirming scope).

Every hook run appends its full raw stdin payload to `.claude/.session-boundary-debug.jsonl`
(gitignored) specifically so this can be checked empirically. **The real test of whether this gate
actually engages is the next genuine fresh-session `/developer-mode` invocation** — check that
debug log for a `"hook": "UserPromptExpansion"` line. If it's absent, the hook never fired (wrong
matcher string or the event doesn't apply to custom commands) and the wiring needs correcting; if
present, confirm the fields matched what the scripts expect (`session_id`, `prompt_id`).

## Test plan and results (per `cfg_behaviour_rule` `test-plan-per-module-utility`)

Unit-level tests, run 2026-09-02 via synthetic stdin JSON directly against each script (real
end-to-end hook firing cannot be exercised from inside the same session that built it — see
limitation above and the standing rule that built work is tested in a separate session):

| # | Scenario | Input | Expected | Result |
|---|---|---|---|---|
| A | Fresh `SessionStart(startup)` | `source:"startup"` | state recorded, `start_source="startup"` | ✅ PASS |
| B | First prompt after A | `prompt_id:"p1"`, same session | `first_prompt_id` set to `"p1"` | ✅ PASS |
| C | Gate check, same turn as B | `prompt_id:"p1"` | **ALLOW** (`{}`) | ✅ PASS |
| D | Gate check, later turn, same session | `prompt_id:"p2"` | **BLOCK** — prior prompt existed | ✅ PASS |
| E | `SessionStart(resume)`, gate on its first prompt | `source:"resume"`, `prompt_id:"q1"` | **BLOCK** — not a fresh source, even though it's the first prompt of that boundary | ✅ PASS |
| F | Gate check with mismatched `session_id` | state says `sess-B`, request says `sess-X` | **BLOCK** — cannot confirm freshness | ✅ PASS |
| G | Gate check with no state file at all | state file deleted | **BLOCK** — fails closed | ✅ PASS |

All seven scenarios produced the expected decision. Test artifacts (`.session-boundary-state.json`,
`.session-boundary-debug.jsonl`) were deleted after each run — none left in the working tree.

One test-construction pitfall found and corrected along the way, worth recording: the first
attempt used a POSIX-style synthetic `cwd` (`/c/Bible_study_projects`, from git-bash `$(pwd)`)
and unescaped backslashes in a Windows-style path, both of which broke path resolution / JSON
parsing in ways that had nothing to do with the scripts' own logic. Corrected by using a forward-
slash Windows path (`C:/Bible_study_projects`) in the synthetic payloads, which Python's
Windows file APIs accept natively. Real Claude Code hook payloads on this platform are expected to
carry native Windows paths already, so this is not expected to recur in production — flagged here
only because it produced a stray `C:\c\Bible_study_projects\...` directory during testing
(cleaned up, not left behind).

## Not yet done (open)

- Empirical confirmation the `UserPromptExpansion` hook actually fires for this custom command
  (see Known limitation above) — first real fresh-session attempt after this build settles it.
- The exit-boundary half of #1380.
- Whether the mode-split rule itself (and this gate) belongs in `cfg_behaviour_rule` — this
  mechanism lives in `.claude/` (Claude Code harness config), not `iba.db`'s `cfg_*` system, so
  `config-updated-same-unit-of-work-as-change` is judged not to apply here; that rule governs
  IBA app schema/operations config, and this is harness-level tooling. Documented here rather than
  silently assumed.
