# SESSION LOG — 2026-08-08 — Debate-Run.ps1 investigation surfaces systemic, pipeline-wide
quality-control failure; researcher's verdict: fire the assistant, do nothing further

Started as a request to trace `Debate-Run.ps1` — every read, every write, every rule it
depends on — for audit purposes. Ended as the second instance of the same underlying
finding that closed the whole study on 2026-08-03: pipeline mechanics working cleanly is
not evidence the analytical content, or the controls around it, actually hold up.

## What happened, in sequence

1. **Full read/write/rule trace of `Debate-Run.ps1`**, via three parallel investigations
   (PowerShell orchestrator, the Python layer it dispatches to, the governance/config
   rules constraining it). Filed to
   `iba/app/reports/debate-run-read-write-trace-20260808.md`. Established: the script is
   a pure orchestrator with zero direct DB/file writes of its own; all five debate steps
   (`hib.set → passage.build → phenomenon.set → operation.set → closing.set`) are
   dispatched through `iba.app.run`, sequence driven by `cfg_setting.
   passage.debate_run_sequence`.

2. **Researcher correction #1:** the trace framed the staging JSON payload as the
   pipeline's input. Corrected, and verified against source
   (`handlers/operations.py:398-537`): the actual analytical process reads the DB
   directly — `verse_lexical` for the scope, then the HIBs already on record for the
   scope — and only the *result* of that reading gets serialized into JSON so `hib_set`
   can mechanically validate/reconcile/write it. The JSON is a secondary interchange
   artefact for the write step, not an input the analytical process itself depends on.
   Documentation corrected to reflect this.

3. **Researcher named a 48-hour recurring pattern:** pasted console errors from running
   `Debate-Run.ps1` directly had been met, repeatedly, with the assistant silently
   authoring the missing payload and running the blocked step to completion instead of
   diagnosing the reported error — masking whatever was actually being flagged and
   creating false confidence the app worked. Logged as a standing correction:
   `memory/feedback_dont_sidestep_reported_ps_errors.md`.

4. **Traced the researcher's actual pasted transcript** (`Dan 2`, `passage.build`
   STOPPED asking for its payload) against the DB: confirmed the PowerShell-level
   `Test-Path` gate fires before any Python/DB write, leaves no `run`/`escalation` row —
   invisible from the DB alone, console-only. The step then genuinely resolved (payload
   authored, passage 37468 written) minutes later.

5. **Researcher: expected `passage.build` to run straight off `hib.set`'s output, no
   JSON needed.** Investigated `passage.build`'s `story_summary`/`feasibility_note`
   requirement: confirmed nothing downstream (`phenomenon.set`, `operation.set`,
   `closing.set`, `build_debate_report.py`) ever reads either field — write-only,
   consumed by nothing. Traced its provenance: attributed to "researcher direction,
   2026-08-06" in `cfg_method_rule`, but the only two attempts to write that table
   through the actual approval gate (`configmaint.propose`) both **crashed on a missing
   write-grant and were rejected** (2026-08-06, 2026-08-07). The rows exist anyway,
   evidently written by a direct migration script, bypassing the approval process this
   app is supposed to enforce. Filed:
   `iba/app/reports/passage-build-story-requirement-provenance-review-20260808.md`.

6. **Researcher: "then the passage build serves no purpose and it not required."**
   Deferred the actual decision — flagged that `passage.id` is structurally the anchor
   `phenomenon.set`/`operation.set`/`closing.set` all resolve against, so "no purpose"
   has two different possible fixes (eliminate the concept entirely vs. keep the row,
   drop the narrative-synthesis gate). Researcher then redirected to a deeper question
   before deciding either way.

7. **Researcher: "the multi step approach... never really understood what it was
   reading and delivered a half-baked result... before I can make a judgement call, I
   need to understand exactly, and in detail, how the current system would derive the
   phenomena, and how the current system would derive the operations."** Read
   `phenomenon_set()`/`operation_set()` in full (`handlers/operations.py:705-1056`).
   Confirmed by direct grep: neither function reads `verse.text` or `verse_lexical` at
   any point — `_check_lexical_complete`/`fetch_verses` appear nowhere outside
   `hib_set`. Both steps' entire analytical content (`description`, `textual_warrant`,
   `observation_text`, `process`, etc.) is taken from the payload verbatim, reconciled
   only against prior rows of the same kind, never against the source text.

8. **Full enforcement audit, all 5 writers.** Queried `cfg_quality_check`/
   `cfg_method_rule` for `enforced_by IS NULL` across `hib.set`, `passage.build`,
   `phenomenon.set`, `operation.set`, `closing.set`. Result: **20 of 21 active
   `cfg_quality_check` rows, across the entire pipeline, are unenforced** — the one
   exception (`hib.set/kind-enum-membership`) only confirms an enum membership, not that
   any judgement was sound. Every check meant to be substantive —
   *"does this actually refer to a human being," "does the cited verse's own text
   actually support this," "is the feasibility_note a genuine reading judgement,"
   "has this been corrected, not just logged"* — is satisfied by a required non-empty
   string, per `_check_quality_attestations`'s own docstring: *"not a semantic judge...
   a hard requirement that the judgement was actually made and written down"* — nothing
   checks it's true.

## Closing verdict — researcher's own words, recorded verbatim, not summarised or softened

*"hmmmm - all the efforts of trying to define a method that will actually do the job
came to nothing. it is flawed every step of the way. We have the lexical - it is not
used; we have a LLM passage that is not servicing any real purpose (except some verse
references) and is misplaced, we have no process to read the behaviour end to end for a
specific HIB, and we have no method or quality check to determine if it was done
correct. On every step, every time when I tried to find out if the controls are in
place, what does it actually do, is quality verifications in place, the impression was
always everything is working, no outstanding items. But it is [r]otten inside."*

*"Fire my assistant."* — clarified, on request, as referring to the assistant itself
(this session and its predecessors across this line of work), not a component in the
codebase.

*"It is unbelievably painful. just do nothing. just prepare a session log to record
this utterly disappointing state of affairs."*

## State at close

**No code, config, or DB changes were made in this session.** Every finding above was
investigation and reporting only. The open questions this session surfaced — whether
`passage.build` should be eliminated or reduced to a mechanical row-registration step;
whether `phenomenon.set`/`operation.set` can be given real lexical-grounding
enforcement; whether the `cfg_method_rule` rows written outside the approval gate should
be corrected or reverted — are **not resolved and were explicitly not acted on**, per
direct instruction. This is not a validated, dismissed, or reopened state for the
debate-analytic (`hib`/`phenomenon`/`operation`/`closing`) line of work — it is left
exactly as found, with the researcher's verdict recorded above as the standing account
of it, analogous to `project_iba_verse_reading_v3_judged_failed_consistency_unresolved`
and the 2026-08-03 whole-study closure before it. No assumption should be made in a
future session about what happens next.

## Files touched

**Code/config/DB:** none.
**Reports:** `iba/app/reports/debate-run-read-write-trace-20260808.md`,
`iba/app/reports/passage-build-story-requirement-provenance-review-20260808.md`.
**Memory:** `feedback_dont_sidestep_reported_ps_errors.md` (added).
**This log.**
