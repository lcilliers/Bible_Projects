---
description: Enter a Developer Mode session — building/fixing the IBA app itself, exempt from configmaint.propose, per CHARTER.md §4 / GOVERNANCE.md §69
---

# Developer Mode — Session Declaration

Run this once, at the START of a session dedicated to building or fixing the IBA app itself —
code, schema, scripts, or config *structure* — not for operating the app or analysing study data.
This is the Developer Mode half of the two-mode split established in `iba/app/CHARTER.md` §4 and
`iba/app/GOVERNANCE.md` §69 (memory `feedback_developer_mode_vs_app_mode_operating_model`).

**Scope boundary, researcher's own words (2026-08-31):** *"my plan is to only use developer mode
for scenarios where the IBA app controls get in the way or need to be adjusted without the
blockages that the app control enforce. normal work such as reporting, exploring the data,
prototyping solutions that should follow the rules, will all be in standard mode."* This is not
"elevated privileges for whatever comes up." A task can drift into Developer Mode mid-session
without being checked against this (it happened the same day this line was written — a reporting
fix, escalation #1306, got treated as buildable-now before being caught) — check every new task
against this boundary explicitly, don't assume Developer Mode covers it just because the session
is in that mode.

**Do not invoke this mid-session to switch modes.** The mode is a property the researcher chooses
once, at session start — never self-selected by Claude, never switched on the fly because a
particular table or file "feels like" a dev change. If this session did not start this way, stop
and say so instead of running the rest of this command.

**Session-freshness gate (escalation #1380, built 2026-09-02).** This is no longer just this
paragraph's instruction to follow — a structural hook (`.claude/hooks/gate_developer_mode_entry.py`,
wired as a `UserPromptExpansion` hook on this command in `.claude/settings.json`) fires from the
harness itself, BEFORE this command's text is even expanded, and refuses to run this command
unless: (a) this session began via a genuine `SessionStart` "startup" or "clear" event — not
"resume", "compact", or "fork" — and (b) no user prompt has occurred since that event, i.e. this
IS the first thing typed. It fails closed (blocks) on any uncertainty, so a real fresh-session
invocation that gets refused means the mechanism itself needs checking
(`.claude/.session-boundary-debug.jsonl` has the raw hook payloads), not that the researcher did
anything wrong. As a redundant, non-structural fallback ONLY (the hook above is the real
enforcement, not this paragraph): if you ever find yourself running this command's steps despite
the hook — e.g. it fired but its matcher/field guesses turned out wrong for this Claude Code
build — re-check `.claude/.session-boundary-state.json` yourself before proceeding, and refuse
the same way if `start_source` isn't `startup`/`clear`. The exit-boundary half of #1380
(preventing App Mode continuing in the same conversation after `/exit-developer-mode`) is not yet
built — still open on that escalation.

**This command does not bootstrap the IBA app.** It does not run `Start-Iba.ps1` and does not
follow the full `start-project` procedure — Developer Mode sessions are explicitly exempt from
that entry point (researcher instruction, 2026-08-31). If IBA operational bootstrap is actually
needed this session too, that's a separate, explicit ask.

**It DOES do one cheap thing `start-project` also does — check the backlog assigned to Claude.**
Found missing live 2026-08-31: this session skipped `start-project` on request, built a chunk of
Developer Mode work, and only surfaced two stale items (#1312, #1314 — the researcher had said
"proceed" on both that morning; #1312's real work got done but never formally closed, #1314's
never got touched again at all) when the researcher pointed at them directly, several turns later.
Nothing else in this command would ever have surfaced them — skipping the bootstrap is right, but
it silently dropped this one unrelated, cheap check along with it. Run, as part of step 1:

```powershell
.\iba\app\ps\Escalation.ps1 -Action List
```

Note anything with `next_action_assigned_to='Claude'` in the resulting report, however old — say
what's there in the step 4 report below, don't just silently note it and move on.

## 1. State the permission boundary — don't just take the label

Developer Mode is real only if this harness session actually has elevated ("sysadmin")
permissions — this command cannot grant them, only declare intent. **This tool cannot directly
query the harness's own permission mode**, so don't fabricate a check result. Instead:

- State plainly, in chat, what permission mode this session appears to be running under, based on
  what's observable (e.g. `.claude/settings.json` permissive/restrictive config, whether prior
  tool calls this session have already hit or cleared an approval prompt).
- If nothing yet indicates elevated permissions, say so and flag the mismatch — do not proceed as
  though Developer Mode is active on the strength of this command alone. Ask the researcher to
  confirm the session actually has full permissions before treating `configmaint.propose`'s
  per-row gate as bypassed.
- The signal that actually settles it, going forward: a standard-permission session will hit the
  harness's own approval prompt the moment something needs elevation. That refusal (or its
  absence) IS the signal — not a judgement call to make later.

## 2. Load what still applies — full permissions is not licence to skip research

Read live, not from memory (`feedback_iba_session_start_read_live_docs_not_memory`):

- Query `cfg_behaviour_rule` for `class='development'` (`iba/app/db/iba.db`) and hold every active
  row in context for the session — currently 11 rows, e.g. `root-fix-not-one-off`,
  `simple-steps-not-engineered-designs`, `every-active-ps-script-dispatches-through-run-py`,
  `test-plan-per-module-utility`, `open-items-route-through-escalation`,
  `config-updated-same-unit-of-work-as-change`, `user-guide-updated-same-unit-of-work`. Don't
  paraphrase from a prior session's memory of them — pull the current text.
- `iba/app/CHARTER.md` §4 and `iba/app/GOVERNANCE.md` §69 (the mode split itself, and its
  provenance — including that this section's first draft got the mechanism wrong and was
  corrected same-day).

## 3. State the standing constraints for this session

- Developer Mode removes `configmaint.propose`'s per-row research-approval gate. It removes
  **only that** — every rule loaded in step 2, plus every other applicable project rule
  (`CLAUDE.md`, `docs/interaction-preferences.md`, other `cfg_behaviour_rule` classes), still
  applies in full.
- Every development task carried out this session still gets an escalation item as the durable
  record (`iba/app/ps/Escalation.ps1 -Action Raise ...`) — full permissions is not licence to
  leave work untracked.
- Work built this session is never tested in this same session. Testing happens in a fresh,
  standard-permission (App Mode) session, deliberately separate from the one that built it.
- Any `cfg_*` change made this session is still real config content — it still needs its own
  `cfg_table`/`cfg_column`/etc. registration in the same unit of work
  (`config-updated-same-unit-of-work-as-change`), it's just not gated on researcher approval
  before being written.

## 4. Set the visual signal

The researcher cannot see this tool's permission state and has said so directly — the visible
signal has to come from Claude, and it has to be unmissable, because *"the moment you abuse this
power you are gone"* (researcher, 2026-08-31 — see memory
`feedback_developer_mode_trust_is_the_only_constraint`). Two mechanisms, because neither alone is
reliable:

1. **Marker file** — write the current UTC timestamp to `.claude/.developer-mode-active`
   (gitignored, session-local; create the file if absent, overwrite if present). This is what the
   statusline (below) actually reads — it's the durable signal, not the chat banner.
2. **Statusline** — if `.claude/statusline-devmode.ps1` and the `statusLine` entry in
   `.claude/settings.json` exist, they'll now show a persistent "DEVELOPER MODE" indicator at the
   bottom of the terminal for as long as the marker file is present, automatically, with no
   per-message effort required. If they don't exist yet, say so plainly — don't claim a statusline
   indicator is live when it isn't wired up.

## 5. Report and stop

State plainly, in chat:

- The permission-boundary finding from step 1 (elevated / not observably elevated / uncertain).
- Confirmation that the current `class='development'` rules are loaded (name them, don't just say
  "loaded").
- That Developer Mode is now the declared operating basis for this session, and that the marker
  file is set.
- Whether the statusline indicator is actually wired up (step 4.2) — don't overclaim.
- Anything found `next_action_assigned_to='Claude'` in the backlog check (step "one cheap thing"
  above) — by id and short description, however old. Don't silently fold it into later work or
  skip mentioning it because it seems stale.

Then stop and ask what to build or fix this session. Do not start a task on your own initiative.

## 6. Ongoing behaviour for the rest of this session

While `.claude/.developer-mode-active` exists, start every subsequent chat reply this session with
this exact banner line, on its own line, before anything else:

> 🛠️ **DEVELOPER MODE ACTIVE** — `configmaint.propose` gate bypassed; every other rule still
> applies.

This is the one visual signal fully within this tool's control — it cannot change the terminal's
actual color scheme. Stop prefixing replies the moment `/exit-developer-mode` is run (it deletes
the marker file) or the session ends.
