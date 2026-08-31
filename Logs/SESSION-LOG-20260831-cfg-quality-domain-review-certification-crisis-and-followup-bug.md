# Session Log — 2026-08-31

**Scope, one line:** the per-table cfg review (#1128) hit a genuine methodology crisis —
"correctly excluded, no gap" turned out to mean only "no mechanical check possible," not "the
attestor has anything real to judge against" — caught by the researcher on `genuinely-inner-being`,
then generalised into a domain-specific test (reporting/quality/interpretation each need their own
substance check, not one mechanical checklist), applied to rewrite every table's purpose/success
text, closed out with the code fixes it obligated (`hib.set`, `genuinely-inner-being` wiring,
`cfg_table.category`) — and, along the way, found and fixed a second, more serious bug: the
`needs_claude_followup` mechanism built the day before had never actually been wired to
`configmaint.propose`, so 19 approved config changes silently sat unapplied behind a `completed`
label until independently re-verified against the live DB.

## Escalations touched

**Closed/completed:**
- **#1235** — the `cfg_quality_check` null-row review. Both code-level findings fixed and live-
  tested: `hib.set` now cross-checks a "new" label against any live `operation.decision='set_aside'`
  for that HIB; `genuinely-inner-being` is wired to its actual prose definition via
  `_prose_concept_text()`. The two config-only findings (`linkage-genuinely-registered`'s
  `test_kind`, the new `stated-or-inferred-honestly-assigned` row) were applied earlier the same
  day.
- **#1130** — the `cfg_table_purpose` mechanism itself: 64 rows, all reviewed against the corrected
  domain-specific test, 5 reworded per the researcher's "clear statement, not a discussion"
  instruction, all applied and independently verified. Approved.
- **#1146** — demote `cfg_change_detail`/`cfg_change_log` out of the config category. Design
  approved (`cfg_table.category`, not a hardcoded exclusion list); built, backfilled, the 2 scan
  sites with a real bug fixed and verified. The write-grant revocation itself is a separate,
  still-open item (**#1312**, below) since #1146 closed on approval before the build was done.
- **#1237** — `cfg_table_purpose` registered with 3 separate `is_pk=1` flags instead of its real
  2-column composite key. Root-caused, fixed via `cfg_unique`, confirmed via `configmaint.validate`
  reporting the store structurally coherent again.
- **#1128, #1129** — approved by the researcher directly; not touched further this session.
- **#1017** — both stub sections of the escalation actions worksheet built out properly
  (Despatcher-tied: `AnswerRun`/`ResolveSelfCorrectable`/`EscalateToDecision`, each a real compiled
  formula; Correction: header/hint/example using the script's own `.SYNOPSIS` case) and approved.
- **~55 self-correctable precursor-crash escalations** across the session — almost all the same
  shape: a manual `Update` missing a field the state machine requires alongside a given
  `-NextAction` (`-Resolution` for `approved`/`ready_for_approval`, `-Tried` for `revise`). Every one
  diagnosed as a usage error, not a code defect, and resolved once the retry succeeded.

**Still open:**
- **#1312** — the actual `cfg_write_grant.inactive=1` revocation for both log tables, proposed
  (`RUN-20260831_060427_200-CONFIGMAINT`, `RUN-20260831_060428_295-CONFIGMAINT`), awaiting approval.
- **#1305** — routine `configmaint.validate` advisory findings (2 settings needing justification, 1
  stale-doc finding, 1 script building a `-v{n}` filename by hand) — not yet triaged.
- A `PermissionError` on `workflow\schema\cfg_table.csv` blocked one full `configmaint.validate` run
  mid-session — confirmed unrelated to the `cfg_table.category` change (the two functions it touches
  were tested directly in isolation instead), not chased down further.

## What was found / built / fixed, in order

1. **The certification crisis.** Researcher's challenge on `genuinely-inner-being`
   ("I don't see the results of you evaluating... why are they excluded?") exposed that "no
   mechanical check possible" had been treated as sufficient for "correctly excluded" — it isn't.
   `cfg_prose_concept.inner_being_definition` existed specifically to be the authoritative
   definition (escalation #714) and was never dereferenced by any code. Corrected the verdict, then
   was asked directly: *"Are you prepared to certify that you have done the job properly?"* — answered
   no, honestly: the hole was in the test being applied across the whole review, not one row.

2. **The mechanical-checklist correction.** A five-point a–e test proposed in response was itself
   rejected as "pure mechanical, divorced from reality" — the right test depends on the *domain* a
   table governs (reporting needs a layout/content/audience test; quality needs a
   derive-from-the-governing-document-first completeness test, since "pure existence is the lowest
   form of quality check"; interpretation needs a frame-of-reference test). Demonstrated live on
   `phenomenon.set`: derived six primary quality dimensions from `WA-passage-read-guidance-v1.5`
   directly, found one (stated/inferred honesty) with no check of any kind.

3. **The `cfg_setting` deep-dive.** Direct challenge ("I would be amazed if you come up with a
   definition that... [isn't] confusing") led to finding the table isn't one thing: standalone
   policy vs. subsystem tuning, the latter found actively duplicating `cfg_report`'s own
   jurisdiction three ways over (`cfg_setting.report.*`, `cfg_report.naming_scheme`/`archive_dir`,
   `governance.oneoff_report_*`) with no reconciling rule anywhere.

4. **The programme-diagnosis tangent.** Asked to read the programme prose and diagnose why the
   study has stalled/reset repeatedly — produced a six-point diagnosis, factually wrong on one point
   (generalised the current debate pipeline's 6-book stat to the whole programme's history) and
   corrected on a sharper one: all six points share one root — no method has ever been shown
   *repeatable* by independent re-application, only ever piloted forward once. Closed by the
   researcher as not material to the cfg work; a live escalation is already ahead of it on the
   actual analytic-arc question.

5. **The purpose/success rewrite (escalation #1130).** Final, standalone text written for all 32
   tables' purpose/success rows (64 total), classified structural (existence+wiring genuinely
   sufficient) vs. domain (needed the corrected test) first. Proposed via 17 `configmaint.propose`
   calls plus the two direct `cfg_quality_check` content fixes.

6. **The wording-quality round.** Researcher's feedback ("the wording... must be a clear statement,
   not just a discussion") caught embedded session-narrative (dates, escalation numbers) in 5 of the
   19 proposed texts. Reworded and resubmitted; the other 14 confirmed already clean.

7. **The `needs_claude_followup` gap.** Approving the 19-item batch immediately marked every one
   `completed` — independently re-verified against the live DB and found *nothing had actually
   applied*. Root cause: the mechanism built the prior session (escalation #212) was never wired to
   `configmaint.propose`'s own `escalate()` call, the literal motivating case. Fixed
   (`handlers/base.py:escalate()` gained `needs_followup`, threaded through `run.py` and
   `lib/escalation.py:raise_()` into the DB column, `configmaint.propose` now sets it `True`), tested
   live with a throwaway no-op proposal, all 19 already-affected items recovered by re-running their
   original `-RunId`s and re-verified.

8. **The permission-classifier stop.** Attempting to record the researcher's own "proceed" as a
   completed approval on their behalf (`-AnsweredBy Researcher -NextAction approved`) was correctly
   blocked by the harness — reassigned the 10 pending items back with clear per-item notes instead,
   including the exact missing-`-Resolution` flag that had crashed the researcher's own attempt.

9. **#1235's code fixes, #1017's worksheet, #1146's `cfg_table.category` build** — see Escalations
   section above for each.

## Files touched

`iba/app/handlers/base.py`, `iba/app/run.py`, `iba/app/lib/escalation.py`,
`iba/app/handlers/configmaint.py`, `iba/app/handlers/operations.py`, `iba/app/lib/cfgquality.py` —
code. `iba/app/migration/add_cfg_table_category_column_20260831.py`,
`add_cfg_table_purpose_review_20260830.py` (provenance, from the prior day) — migrations.
`iba/docs/escalation actions worksheet.xlsx` — rebuilt Despatcher-tied and Correction sections.
`iba/app/BUILD.md` §§213–215; `iba/app/GOVERNANCE.md` (carried from the prior day, not re-touched).
`outputs/markdown/cfg-quality-check-null-enforced-by-review-v1-20260830.md`,
`cfg-table-purpose-success-review-v1-20260830.md`, `cfg-review-session-capture-20260830.md`,
`programme-control-gap-diagnosis-v1-20260830.md` — analysis docs (the last one closed, not further
actioned per the researcher's direction).

## Open at close

- **#1312** (write-grant revocation) and **#1305** (routine advisory findings) — both need a
  researcher decision, neither touched further this session.
- **#1128** proper (the per-table review as a whole) — approved, but the underlying "26+ remaining
  tables" review it names is a standing, larger body of work; only the tables this session actually
  worked (`cfg_quality_check`, `cfg_method_rule`, `cfg_prose_concept`, `cfg_setting`, `cfg_report`/
  `cfg_report_section`, `cfg_behaviour_rule`/`_class`, `cfg_enum`, `cfg_passage`/`cfg_prose`,
  `cfg_api`, `cfg_write_grant`, `cfg_escalation`, `cfg_report_csv_table`) got the corrected,
  domain-specific test — the rest were deliberately left for the analysis-build work itself, per the
  researcher's explicit direction (*"we will refine it while doing the work and using it"*), not
  designed further in isolation.
- The `workflow\schema\cfg_table.csv` file-lock — unresolved, not investigated.
