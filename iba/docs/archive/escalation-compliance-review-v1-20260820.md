# Escalation module — governance compliance review (v1, 2026-08-20)

Requested: confirm the rebuilt escalation utility (`iba/app/lib/escalation.py`,
`iba/app/ps/Escalation.ps1`, `cfg_escalation*`, `escalation`/`escalation_history`) complies with
every governance rule and is ready for review, following the researcher's stated standard: one
missing piece of functionality, error, or omission fails the whole design.

**Method:** live code read (`lib/escalation.py`, `ps/Escalation.ps1`), live DB query against
`iba.db` (`cfg_table`, `cfg_escalation*`, `cfg_setting`), a real `configmaint.validate` run against
the live config store, and a direct text search of `GOVERNANCE.md`/`BUILD.md` — not a re-read of
the design doc's own claims about itself.

## Verdict

**Not fully compliant.** One concrete, verified defect in `governance.tables`, plus one gap in
`governance.governance_md_on_rule_change`. The escalation *mechanism itself* — the code, the two
new rule tables' content, the enum split, the no-default-originator enforcement, the two-stage
approval check — is verified correct and matches the design doc exactly. The defect is in
documentation-of-truth, not in behaviour.

## Finding 1 — `cfg_table.use` for `escalation` and `escalation_history` describes the RETIRED design

`governance.tables`: *"each table in the project must be listed in cfg_table with a proper use
text."*

Live query against `iba.db`, table `cfg_table`, rows `escalation` / `escalation_history`:

> **`escalation`.use:** "One row per item, CURRENT STATE ONLY ... **Redundant with the latest
> escalation_history row by construction: every write updates both, in one transaction.**"
>
> **`escalation_history`.use:** "Append-only, **one FULL SNAPSHOT row** per update to an escalation
> item, **every column's value at that version** -- never updated or deleted once written
> (escalation-redesign-plan-v3 §2). ... **`escalation` always mirrors the latest row here by
> construction.**"

Both statements are false under the live design. `escalation-rebuild-design-v1-20260820.md` §1/§3,
`lib/escalation.py`'s own module docstring, and — tellingly — the **column-level** `cfg_column`
descriptions for the very same table (`comment`: *"delta: the raw increment THIS version added,
NULL if this version didn't touch it"*; `context`, `resolution`, `tried`, `source`, `type`,
`short_description`, `raised_at`: all correctly documented as delta/structural, NULL after v1
unless touched) all agree: `escalation_history` is now a **true per-version delta**, most fields
`NULL` on most rows. It does **not** mirror `escalation`, and `escalation` is **not** "redundant"
with it — the whole point of the rebuild (researcher's own words, quoted in the code: *"the
cumulative is only in escalation"*) was to stop it being a redundant full snapshot.

So the table-level description sitting directly above these correct column rows in
`CONFIG-REPORT-v128-20260820.md` (lines 1856–1857, 1879–1880) contradicts them. `BUILD.md` §161
step 4 confirms the schema constraints were fixed and "`cfg_column` descriptions corrected to
match" — but does not mention the table-level `use` text, and it was in fact left unfixed.

**This is the same defect class that caused the original "not ready for production" ruling** — a
config-facing claim describing a mechanism that no longer exists (there, `cfg_escalation` rows
naming a deleted function; here, `cfg_table.use` naming a deleted snapshot design). It reintroduces,
at the table-description level, the exact failure mode the rebuild was meant to eliminate.

**Fix required:** `configmaint.propose` an update to both rows' `use` text so it states the true
delta/current-state split, matching the column-level text and `escalation.py`'s docstring.

## Finding 2 — `GOVERNANCE.md` was not updated for this rebuild

`governance.governance_md_on_rule_change`: *"any governance/process rule change must be set in
cfg_* first ... then GOVERNANCE.md updated to reflect it in the same unit of work — GOVERNANCE.md
documents the config, it never holds a rule the config does not."*

`grep` of `iba/app/GOVERNANCE.md` for `two-stage`, `ready_for_approval`, `cumulative`,
`state-derivation`, `escalation_history`: **zero matches.** The document has no section describing
the manual-shape state-derivation rule engine (`cfg_escalation_transition`), the field-requirement
engine (`cfg_escalation_requirement`), the true-delta/cumulative split, or the two-stage
separation-of-duties check — not from this rebuild, and not from the redesign before it. `BUILD.md`
§161 lists `USER-GUIDE.md` as updated (user-facing usage) but does not list `GOVERNANCE.md`.

**Fix required:** add a `GOVERNANCE.md` section documenting these mechanisms — the same treatment
already given to `configmaint.propose`'s three-way approval (§ "the only sanctioned path...") a few
sections away.

## What was checked and found correct

- `cfg_escalation`'s 7 rules: `enforced_by` claims re-verified against the live code — no dead
  function references remain (the design doc's claimed fix for `#746`/`#755` holds).
- `configmaint.validate` run live: 0 missing report paths, 0 settings-needing-justification, 2
  orphan settings (`database.iba.path`/`database.bible_research.path` — unrelated to escalation).
- `cfg_write_grant` — `escalation → word_registry` and `run → escalation` both confirmed retired
  (inactive), matching design doc §9.
- `escalation_next_action_dispatcher`/`_manual` enum split present and populated correctly (§9).
- `escalation`/`cfg_escalation_transition`/`cfg_escalation_requirement` schema, `cfg_column`
  entries, and code (`_evaluate_transition`, `_check_requirements`, `_check_assignee`'s no-default
  enforcement, `update()`'s two-stage check) all read consistently with the design doc.
- `BUILD.md` §161 present, detailed, honest about what was deferred (§10 of the design doc:
  `reportkit`/`cfg_report` registration for the two reports — explicitly deferred, not silently
  dropped, and not itself a `governance.reports_must_persist` violation since both reports do
  persist to a `cfg_setting`-defined path — confirmed 0 missing-report-paths findings).

## Not yet checked (would need a further pass if this review continues)

- `escalations_old`'s disposition/relationship to the live `escalation` id sequence.
- `cfg_unique` coverage for the two new rule tables' dedup keys (stated in the report, not
  independently re-verified against the live schema's actual unique constraints).
- Whether `cfg_escalation.rule_key='module_blocking'`'s note ("scheduled as a task escalation, see
  the reset's backlog pass") still points anywhere real now that the escalation table was emptied —
  possibly now a dangling reference, not verified.
