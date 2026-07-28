---
name: feedback_iba_data_judgment_calls_must_escalate_not_silent_report
description: "Any IBA app check that finds something needing a researcher JUDGMENT CALL (not a hard structural violation) must route through the escalation mechanism (pause-continue, researcher answers, run resumes) — never a silent advisory list in Outcome.counts, which is a fourth, unsanctioned pattern."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7608c281-70c1-41bb-8181-d9ebf468771f
  modified: 2026-07-21T15:23:04.868Z
---

Researcher's correction (2026-07-21), on a proposed `span_candidate` rule I framed as "report-only,
advisory": *"the rule is not a hard blocking - it should go through the escalation routine. it seems
that you are not familiar with escalation and that make we question how many other rules do we have
that is linked to escalation."*

**Audited on the spot — the real numbers:** across the whole app, only **3 of 15** defined
`cfg_on_fail` conditions actually escalate (`pause-continue`): `raw.discover`/zero-strongs,
`registry.create`/needs-approval, `configmaint.propose`/needs-approval. Everything else is
`report-stop` (hard block, no question) or `report-continue` (proceed silently, logged). Worse: the
`configmaint.validate` checks built earlier the same day (step-duplication, orphan-configs,
settings-needing-justification) don't fit that taxonomy at all — they're returned as plain
`Outcome.counts` data with `condition="ok"`, never interrupting anything, invisible unless someone
reads the JSON or `CONFIG-REPORT.md` by hand. That's a **fourth, unsanctioned pattern** I introduced
without noticing it broke from the app's own established three-shape model.

**Why:** the app has exactly one sanctioned way to say "this needs a human decision, not a code
decision" — `escalate()` → `cfg_on_fail(path=pause-continue)` → the `escalation` table → the run
pauses → the researcher answers → the run resumes and acts on the answer. A silent advisory list is
not oversight; it's data nobody is asked to look at. Anything a check finds that constitutes a genuine
judgment call (not a hard structural break) belongs behind that gate, not in a `counts` dict.

**The real complication, and why it's not just "always escalate":** some checks find a SMALL number
of things (a handful of orphan configs) — one escalation per run, listing everything found, works
fine. Others find a LARGE number (e.g. 15,541 of 87,922 `span_candidate` rows with a null tag; 46,003
with no matching `strong` row) — escalating per-row would be absurd at that scale. The right shape is
still ONE escalation per run/invocation, with a representative sample + total count as the payload
(matching the standing "representative payload" rule), letting the researcher's single decision apply
to the whole batch found in that run — not one escalation per violating row, and not silence either.

**How to apply:** before building or extending ANY check in this app, ask explicitly: does a violation
here need a human decision (route to escalation, batched at the run level if the count could be large)
or is it a genuine hard structural break (report-stop is fine) or is it truly pure information with no
decision attached (rare — a report/snapshot like CONFIG-REPORT.md is fine as-is)? Do not invent a
fourth resting place. Audit existing checks against this the same way, not just new ones. Related:
[[feedback_iba_config_changes_require_researcher_approval_never_silent]],
[[feedback_iba_validation_approval_must_be_representative_and_three_way]].
