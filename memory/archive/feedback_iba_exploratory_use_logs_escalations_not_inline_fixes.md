---
name: feedback_iba_exploratory_use_logs_escalations_not_inline_fixes
description: "When the researcher is exploratorily using the IBA app and spots an error/omission, log it as an escalation (Escalation.ps1 -Action Raise) — do NOT fix on the spot. Only work the backlog when a new session explicitly says to start clearing escalations."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 369238a5-4a30-4a96-85b6-138d1738a129
  modified: 2026-07-23T05:48:20.285Z
---

Set 2026-07-23, start of an app-usage session: *"as I spot errors, omissions, I want you to create
escalation updates for your action, I do not want each error to be fixed on the spot, unless I
start a new session and instruct you to start clearing the escalation."*

**Why:** exploratory use-the-app sessions are for surfacing issues, not context-switching into
fixes mid-flow. Batching via the app's own `escalation` table keeps a durable, reviewable backlog
(the same mechanism GOVERNANCE.md §10 built for researcher-initiated flags) rather than scattering
ad-hoc fixes across a session.

**How to apply:** during a session explicitly framed this way — the researcher is using the app and
reporting things they notice — raise `iba\app\ps\Escalation.ps1 -Action Raise -Question "<the
researcher's own wording, verbatim>"` for each item, then keep going. **Use the wording the
researcher supplies, as supplied — do not investigate first, do not fold in root-cause analysis or
a proposed fix, do not rewrite/expand their wording.** Do not fix, do not propose a
`configmaint.propose`, do not edit code or DB rows, do not touch the paused/rejected state of any
run, even for a trivial/obvious case — the escalation insert is the ONLY action taken.

**Corrected same session (2026-07-23), after a real miss:** the researcher's first item ("the
report attached is in the wrong folder... check the config, fix, then archive... produce it in the
right folder") was misread as a command to execute now; I investigated, found the root cause,
raised an escalation with my OWN analysis folded into the question text, then proposed a config fix
via `configmaint.propose` — all before any approval. The researcher's correction: *"I do not want
you to investigate, or fix the issue now. You just need to properly record it using the escalation
method... with the wording I supply."* Descriptive/imperative phrasing in what the researcher tells
you to escalate (e.g. "check the config, fix...") is the CONTENT they want captured, addressed to
whoever later clears the backlog — not an instruction to you to act immediately. When genuinely
ambiguous whether a researcher message is dictating escalation wording vs. issuing a direct command,
this workflow's default is escalate-only; a real live change (even pausing a `configmaint.propose`
for later approval) is still an action taken now and violates the rule, not just applying it.

This is a **deliberate, scoped override** of
[[feedback_close_the_loop_not_just_investigate_and_report]] and
[[feedback_fix_standard_violations_dont_ask]] for this specific workflow only — those defaults
resume once the researcher says (in a session) to start clearing the escalation backlog.
