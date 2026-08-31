# Design proposal: an "approved but not yet done" flag on `escalation`

**Trigger:** #1059/#1060/#1061/#1062 all reached `state=completed` the moment you set
`next_action=approved` — before the actual config write had happened. You correctly diagnosed this
as a recurring pattern, not a one-off, and asked for a flag that routes the item back to Claude
after approval when real follow-up work remains.

## Root cause, traced exactly (not inferred)

`iba/app/lib/escalation.py`, `update()` → `_evaluate_transition()` reads `cfg_escalation_transition`
in priority order, first match wins. The live row that fires here:

| priority | shape | next_action | condition_key | resulting status |
|---|---|---|---|---|
| 1 | manual | approved | `has_resolution` | `completed` |

`has_resolution` only checks *does a resolution string exist* — nothing checks *is the thing the
resolution describes actually finished*. For a config-change proposal specifically, "approved" and
"applied" are two genuinely separate events (`configmaint.propose` only applies on a **second**,
separate invocation with `-RunId`, after approval) — the state machine has no way to represent that
gap today.

## Proposed fix

**New column**, `escalation.needs_claude_followup` (INTEGER, default 0, NOT NULL) — set by Claude
at `Raise` or at the `ready_for_approval` `Update`, whenever finishing the item requires a further
action from Claude after the researcher approves it (a config apply, a build step, anything not
already done by the time approval happens). Default 0 — most escalations need nothing further, this
only opts in the ones that do.

**New condition_key**, `needs_followup`, added to `_condition_true()` — reads that column off the
current row.

**New `cfg_escalation_transition` row**, checked *ahead of* the existing `has_resolution` rule:

| priority | shape | next_action | condition_key | resulting status |
|---|---|---|---|---|
| 1 (existing rule renumbered to 2) | manual | approved | `needs_followup` | `re-assigned` (assignee → Claude) |
| 2 | manual | approved | `has_resolution` | `completed` (unchanged) |

So: `approved` + flag set → the item lands on `re-assigned`, reassigned to Claude, *not* `completed`
— exactly the routing-back you asked for. `approved` + flag NOT set → unchanged, still goes straight
to `completed`.

**Closing it out:** once Claude actually finishes the follow-up (the real apply, in this example),
Claude runs a further `Update -NextAction noted` — the existing "acknowledged, done" vocabulary —
which resolves to `closed` (a genuinely terminal state, distinct from `completed` but equally final;
`completed`'s own `cfg_status_flow` text specifically means "approved+resolution present," so reusing
it here would blur a meaning that's already load-bearing elsewhere).

**Surface, so it's actually usable:** a new `Escalation.ps1` switch, `-NeedsFollowup`, on both
`-Action Raise` and `-Action Update` — wired through to `raise_new()`/`update()`. Per
`governance.ps_worksheet_sync_on_change`, this means the `ps tools worksheet.xlsx` Escalation tab
(a pointer, not real headers — skipped by the drift check) and, this time for real, `escalation
actions worksheet.xlsx` (your own hand-built model sheet) both need this new flag added as a column
— I'll warn before touching that file, per standing instruction.

## Why this isn't just built already

This is the one state machine every escalation in the project — 1,000+ rows so far — passes
through. A mistake here doesn't stay local to one item. Per the standing rule that design/build
work on shared mechanisms is never self-correctable, even off a clear suggestion: this needs your
sign-off on the shape above (column name, reused `closed` vs a new terminal status, the exact
renumbering) before I touch `cfg_escalation_transition`/`escalation.py`/the two worksheets.

## Scope check — does this also explain past incompletions?

You said you've noticed this "many times" and suspect it explains other unfinished work. Worth a
follow-up pass, separate from building the fix itself: query every escalation that ever reached
`next_action=approved` (or `completed` generally) whose `at_step`/`context` names a
`configmaint.propose`-shaped change, and check whether the matching `cfg_change_detail` row actually
exists — the same live-vs-recorded check I just ran by hand for #1059–1062, done once, systematically,
across history. That would turn "likely" into a real count.
