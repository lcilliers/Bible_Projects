---
name: feedback_deliberately_sparse_instructions_to_probe_defaults
description: "In training/exploratory IBA sessions, the researcher deliberately under-specifies instructions to observe Claude's default work patterns as diagnostic signal, not oversight"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a8221a07-e7e7-4200-bed6-5478ddbb6f3b
  modified: 2026-08-03T05:31:24.133Z
---

In training/exploratory sessions (e.g. the 2026-08-03 "teach you to read a passage and identify
inner beings" session), the researcher deliberately withholds detailed instructions on purpose —
to see what Claude's unprompted "go-to" pattern of work is. Stated directly: "I deliberately do not
provide more comprehensive instructions to be able to identify your go-to patterns of work — it has
good and bad built in, and navigating through it is part of my job. Your go-to position in most
cases is only indicative, rather than definitive."

**Why:** the default behavior itself is the data he's after — e.g. this session's default was to
reach for the DB pipeline/report scripts immediately (rejected), and later to classify beings from
English surface text/pattern-matching rather than grounded morph/Strong's data (self-diagnosed
after he asked whether regex-style matching was used — see
[[feedback_source_of_truth_is_written_record]] and the Obadiah grep-pattern-matching precedent,
commit 6ed3c46b). Both were useful precisely *because* they were unprompted defaults he could then
correct against.

**How to apply:** in these sessions, don't over-ask for clarification up front trying to guess the
"right" scope before starting — let the natural default surface, then treat correction as expected
data collection, not a failure to route around. Don't get defensive or over-hedge when a default is
called out; name plainly what the default actually was and why it produced the result it did (as
with the regex-reflection above). Do not infer from a single un-corrected default that it's
endorsed — silence on a given task isn't approval, since he's watching many things across a session,
not exhaustively vetting each one. This complements
[[feedback_review_via_files_not_chat]] and [[feedback_close_the_loop_not_just_investigate_and_report]]
— the review still happens, it's just happening by letting the default run first rather than asking
before every step.
