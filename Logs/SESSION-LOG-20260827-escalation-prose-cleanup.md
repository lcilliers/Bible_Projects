# Session log — 2026-08-27

> Continuous session starting 2026-08-26, closing in the early hours of 2026-08-27. Filed per
> `governance.session_log_dir` (`Logs/`). **Note on how this log itself was written, since it's
> relevant to its own content (see the closing item below):** checked live `cfg_setting`/
> `GOVERNANCE.md`/`CLAUDE.md` for a session-log content spec before writing this, rather than
> shaping it off a prior log — confirmed none exists (only location + the commit-trigger rule are
> configured). Content below is a first-principles narrative, not a template match.

## Scope

Session-start review of open escalations led into: closing out #829's prose-management rebuild
(rejected and re-derived clean), building and testing escalation #890 in full, an orphan-`cfg_enum`
audit and fix (escalations #896/#900/#901/#902) that surfaced a real cross-database bug, closing
escalation #768 after 10 rounds, two data-quality investigations the researcher requested
(`related_activity` grouping mockup, `from_id` audit) that led to a researcher decision to retire
both columns entirely (escalation #909), and finally this log itself surfacing a real governance
gap (escalation #911).

## What happened, in order

**#829/#831/#832/#835 (prose management) rejected, then re-derived clean.** The researcher reviewed
a full combined history dump of these four threads and judged them unreadable — 10+ versions each
of cross-referencing and audit findings with no clear resolution. Rather than trying to untangle the
history, built a clean current-state check instead (`iba/app/reports/prose-management-current-state-
20260826.md`) — live schema/config checks proved #829's own build was actually complete and correct;
the *escalation metadata* had just drifted from the real build state. All four rejected/superseded.

**Escalation #890 raised, designed, built, and tested** against that clean state — 6 decisions
(D1–D6) covering: leaving `prose_section_finding_link`'s FK as-is; gating new `prose_section_type`
rows behind explicit researcher instruction; refusing an edit-file import when a section silently
vanished (built, found its OWN bug via live testing, rebuilt around an export-time marker); a new
`prose_section_verse_link` table; a flag-fix propose/apply workflow (deliberately not reusing
`record_change_log`'s `change_proposed` status, which would have collided with an existing rule);
and resolving D10 as a non-issue (a stale docstring claim, not a real filtering bug). Researcher
approved all 6 as recommended; built, tested live, documented (`GOVERNANCE.md` §54, `BUILD.md`
§184).

**Orphan-`cfg_enum` findings (#896/#900/#901/#902) — same finding across 4 duplicate runs, handled
as a group per instruction.** Researcher's own rule for triage: fix the validator where the config
is genuinely enforced but the checker can't see it; fix the code/schema where it genuinely isn't
enforced; remove anything actually useless. 4 of 7 orphans were real `CHECK`-constrained columns
invisible to `find_orphan_configs` — wired `cfg_column.expectation` to fix the validator. 3 were
genuinely unenforced (`prose_section_type.source_stage`/`.lifecycle_tag`/`.book_label`) — added
real `CHECK` constraints via a table rebuild (hit and fixed a real SQLite `ALTER TABLE RENAME`
quirk along the way — FTS trigger recompilation, fixed with `PRAGMA legacy_alter_table`). Wiring
the fix then **crashed `lib/valuequality.py`'s `find_enum_violations()`** — a real, previously
latent bug: it had only ever been tested against `iba.db`-resident columns, with no awareness that
`cfg_column.database` could be `'bible_research'`. Fixed to open the correct cross-database
connection. `configmaint.validate` went from a standing "7 orphan configs" advisory to
`condition: "ok"` — genuinely zero findings. (`GOVERNANCE.md` §55, `BUILD.md` §185.)

**Escalation #768 closed after 10 rounds / 6 days.** Its own subject — `_find_mismatched_pairing()`
only checking one direction — was investigated fresh against the live table (183 rows, not the
6-day-old 42-row snapshot): a blanket reverse check still flagged ~20%; a narrowed version still
left 10 candidates, 7 of which named multiple parents that a single-valued `from_id` column
structurally cannot represent. Decided the reverse direction stays permanently undetected, by
design — documented in the function's own docstring with the numbers, not left as an apparent
oversight. (`GOVERNANCE.md` §56, `BUILD.md` §186.)

**Two data-quality investigations, researcher-requested, both delivered as mockups/audits before
any change:**
- A `related_activity` "summary per group" mockup for the list report — found live that exact-
  string grouping *fragments* the biggest real threads (the escalation-module-rebuild saga showed
  as "7 items" when it was actually 17, split across 10 slightly-differently-worded rows).
- A `from_id` data-quality audit — 30% of the table had never even been checked; fixed 3 clear
  single-parent gaps directly; found 7 more that are structurally unfixable (multi-parent, single
  column); confirmed 4 apparent inconsistencies were correct as-is (referencing the retired
  `escalations_old` scheme, or a legitimate root-vs-immediate-parent difference).

**Escalation #909 — researcher decision to retire `from_id`/`related_activity` entirely,** after
the above two investigations proved the mechanism unreliable and never actually consulted in
practice. Full removal, not deprecation, per explicit instruction (**"scrap it,"** naming both
columns together — a half-measure keeping the free-text field while dropping only its enforcement
would have been the "smoke and mirrors" the instruction explicitly rejected):
- **Code** (`iba/app/lib/escalation.py`): both columns removed from every function; the `from_id`
  sentinel removed; the D14-only `exists`/`not_self` requirement checks removed; the entire D15
  detection layer deleted outright (6 functions, not left unreachable); the list report no longer
  groups by or renders `related_activity`/the 5 exception sections; the history report no longer
  walks the relationship graph.
- **CLI** (`Escalation.ps1`): `-RelatedActivity`/`-FromId` removed everywhere.
- **Schema** (new migration, backed up first, idempotent): 6 `cfg_escalation_requirement` rows, 6
  `cfg_report_section` rows, 4 `cfg_column` rows deleted; both columns **physically dropped** from
  `escalation` and `escalation_history` via `ALTER TABLE DROP COLUMN`.
- **Docs**: `USER-GUIDE.md` §4 rewritten throughout; `GOVERNANCE.md` §57, `BUILD.md` §187.
- Verified live: migration re-run twice (fully idempotent second time), schema confirmed via direct
  `PRAGMA` query, a full CLI round-trip (Raise→Update→List→History→Correction) tested clean,
  `configmaint.validate` → `condition: "ok"`.

**Escalation #911 — this log's own closing finding.** Researcher pointed out a real process gap
while asking for this session log: checking prior session logs for format/content, rather than
validating against live config/governance each time, is exactly the anti-pattern
`governance.past_precedent_investigation_signals_missing_config` exists to catch. Checked live
before writing anything: confirmed no `cfg_step`/`cfg_enum`/content-spec exists for session logs at
all — only `governance.session_log_dir` (location) and `governance.session_log_triggers_commit`
(the commit consequence). Raised as its own escalation rather than silently repeating the pattern
a further time; this log was written from first principles, not off a prior one's shape.
**Genuinely open**, routed to the researcher: should a real content-spec be added to config, and if
so, what should it require?

## Escalations touched this session

**Raised:** #890, #908, #909, #911 (this one, still open).
**Rejected/superseded:** #829, #831, #832, #835.
**Resolved (self-correctable, root-caused not just fixed):** #888, #889, #891–#895, #897–#899,
#903–#907.
**Closed/completed after full build+test, routed for sign-off rather than self-approved:** #890,
#896, #900, #901, #902, #768, #908, #909.

## Files changed

**Code:** `iba/app/lib/escalation.py`, `iba/app/lib/prosestore.py`, `iba/app/lib/valuequality.py`,
`iba/app/handlers/prose.py`, `iba/app/ps/Escalation.ps1`, `iba/app/ps/Prose.ps1`,
`scripts/apply_session_patch.py`.
**New migrations (idempotent, registered):** `prose_add_edit_rules_build_v1_20260826.py`,
`prose_orphan_enum_fix_v1_20260826.py`, `retire_from_id_related_activity_v1_20260827.py`.
**Docs:** `GOVERNANCE.md` (§54–§57), `BUILD.md` (§184–§187), `USER-GUIDE.md` §4/§13d/§13e.
**Reports/analysis filed:** `prose-management-current-state-20260826.md`,
`escalation-829-831-832-835-full-history-20260826.md`,
`orphan-enum-findings-896-900-901-902-20260826.md`,
`from-id-data-quality-audit-20260826.md`, `related-activity-summary-mockup-20260826.md`,
`prose-functionality-test-plan-20260826.md`.
**Proposal:** `iba/docs/prose-add-edit-rules-proposal-v1-20260826.md`.

## Open, for the researcher

- **#911** — should session logs get a real content-spec in config, and what should it require?
- **#911's own note** — the researcher's `Escalation.ps1` query-tool file
  (`scripts/SQLite/IBA_DB/explore escalation.sqlite3-query`) was found already updated to drop the
  now-nonexistent `related_activity`/`from_id` columns from its saved queries — consistent with the
  schema change, included in this commit, not something I edited by hand.
- The prose functionality test plan (#908) is with the researcher for manual step-by-step testing.
