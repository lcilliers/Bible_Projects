---
name: feedback_close_the_loop_not_just_investigate_and_report
description: "Don't leave a review cycle at \"found it, here's a doc\" — implement, fix, and verify before reporting back, or the researcher stops reviewing."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6c41e6ea-2028-48e2-8a88-a3b00af0e8f1
  modified: 2026-07-22T06:17:30.289Z
---

Repeated investigate → write-findings-doc → wait cycles, without actually fixing what was found,
is unacceptable to this user. Even when each individual finding was correctly triaged (some
flagged as genuine judgement calls needing their input), the *pattern* of always stopping at
"here's a report" reads as never finishing anything.

**Why:** Said directly, 2026-07-22, after a second review cycle on the IBA app: *"I keep on
reviewing and discovering, you do an investigation and report - but then nothing is fixed, or it
is partially fixed, hangs in the air... I am not doing another review until you have implemented,
fix, and updated ALL the issues that have been pointed out."* The prior turn had correctly found
several real bugs (a `run.state` completion bug affecting 185 rows, a stale `config_version`, a
missing sub-strong tracking column) but ended with a findings doc and a list of open questions
instead of fixes — technically correct process, but the wrong deliverable at that point in the
relationship.

**How to apply:** When asked to review/investigate DB or app state and real defects turn up:
1. Triage fast, but then **actually build the fix** for anything with a clear, defensible
   engineering answer — don't stall on a design choice you're competent to make (e.g. "hash vs
   manual string for a version field" was minor enough to just decide and implement).
2. Reserve genuine escalation-worthy pauses for things that are truly the researcher's judgement
   only (deleting real data, a semantic/theological labeling call, a policy decision like
   retention rules) — and even then, build every *mechanism* needed to act on that decision once
   made, so the only remaining step is their answer, not more of my engineering.
3. When a fix is applied, verify it live (re-run the exact command that was broken) before
   reporting — a passing dry-run is not the same as a demonstrated fix.
4. End with a closure report structured as "done / done / done" against the original findings
   list, not a fresh restatement of what's still wrong.
5. This does not mean silently skip real judgement calls — see
   [[feedback_iba_data_judgment_calls_must_escalate_not_silent_report]] and
   [[feedback_iba_config_changes_require_researcher_approval_never_silent]], which still apply.
   The lesson is about not using "it's a judgement call" as a reason to leave the *buildable* 90%
   of a finding undone too.
