# `cfg_table_purpose` — every table's purpose/success, reviewed and corrected

**Date:** 2026-08-30. Escalation: #1130 (the table exists) / #1128 (the per-table review). This
doc is the direct response to: *"I am convinced that you purpose and success description of each
cfg table is far from what it need to be... you may want to revise your own work and really think
about what you are doing."*

**What was wrong with the first pass.** Almost every SUCCESS row I originally wrote reduces to
one shape: *does the config exist, and is it wired to real code.* That is a real and necessary
test, but it is the *lowest* form of a quality test — it was proven insufficient live today, twice
(`genuinely-inner-being`'s orphaned definition; the missing stated/inferred check that no row of
any kind covers). Existence-and-wiring is genuinely the *right* and *sufficient* test for tables
whose entire job is technical/structural correctness (schema mirrors, dispatch registries, state
machines). It is *not* sufficient for tables whose job is to carry domain judgement — quality
standards, interpretive method, report content, behavioural discipline — where the real question
is whether the substance is complete and right, not just present and connected.

Below, every table is first classified, then given a corrected success measure where the
classification demands one. **Unmarked = original stands, genuinely adequate for what the table
is.** **REVISED = rewritten**, with the reasoning for why the original was too shallow.

---

## Structural / technical tables — existence + wiring genuinely IS the right test

These tables' entire job is mechanical correctness. There is no separate "domain substance"
question hiding behind them — a schema mirror is either accurate or it isn't; an index registry
either matches the live index or it doesn't. Original text stands for all of these, with two minor
sharpenings noted.

- **cfg_api** — stands, with one addition: success should also ask whether each row's documented
  *return shape* still matches what STEP actually returns today (STEP's own output can drift
  independent of whether the call is wired), not only that the call fires.
- **cfg_book_order**, **cfg_candidate_rule**, **cfg_column**, **cfg_connection**,
  **cfg_content_index_exclude**, **cfg_content_index_size_override**, **cfg_index**, **cfg_meta**,
  **cfg_on_fail**, **cfg_status_flow**, **cfg_step**, **cfg_table**, **cfg_unique**,
  **cfg_utility**, **cfg_work_package** — stand as originally written.
- **cfg_escalation_requirement**, **cfg_escalation_transition** — stand; these are state-machine
  definitions, and "does every rule genuinely fire" is exactly the substance question for a state
  machine, not a shortcut past one.
- **cfg_write_grant** — REVISED. Original success ("every write matches a grant; an ungranted
  table is unreachable") tests only that the mechanism is wired, not that each grant's *scope* is
  correct. The `cfg_change_detail`/`cfg_change_log` finding (escalation #1146) proved a grant can
  be technically present and functioning while being the wrong grant — `configmaint.propose`
  holding write access to an audit-log table it should never be able to touch.
  **Corrected success:** every write matches a grant, AND every grant's scope is one the writer
  should actually be trusted with — checked against what kind of table it is (rule table vs. data
  table vs. immutable log), not only that the grant exists and technically permits the write.

## Process-control / policy tables — mostly structural, one real content gap found

- **cfg_escalation** — stands, largely, and its existing success text already caught a real gap
  (`module_blocking` claimed active while genuinely commented out) using exactly the right test:
  does every mechanical-enforcement claim actually fire. One addition: for the rules honestly
  labelled *session practice* rather than mechanical, success should also ask whether there is any
  way to confirm they're actually being followed (a review trail), or whether "session practice"
  currently just means "trust it happens" with no way to check — that's a live open question, not
  yet answered either way.
- **cfg_report_csv_table** — stands, largely technical (which tables export to CSV), with one
  addition: does the exported column set actually give complete coverage of what the report body
  claims to discuss, or is something the report's prose depends on missing from its own CSV.

## Domain / content tables — existence-and-wiring was NOT sufficient; revised below

These are the tables where "the config exists and is read" tells you almost nothing about whether
it's doing its actual job. Each needs a substance question specific to what kind of judgement it
carries — exactly the reporting/quality/interpretation distinction you named.

### cfg_quality_check
**Original success:** "Every required check's `enforced_by` mechanism genuinely exists and runs;
every check's `test_kind` matches how it is actually verified." — This is existence-and-wiring
only, and it is the exact gap proven live today: it checks that each row that exists works, and
says nothing about whether the *set* of rows for a step is complete.
**REVISED purpose:** Per-step data-quality questions a handler asks of its own output — read
alongside, and only interpretable against, the actual governing method document for that step
(`WA-passage-read-guidance-v1.5`, `WA-interpretation-questions-v1.4`, etc.), not as a
self-contained list.
**REVISED success:** (a) every row's own mechanism, where claimed, genuinely fires [kept from
original]; AND (b) **the set of checks for each step covers every primary quality dimension the
step's governing method document actually specifies** — derived independently from that document
first, then compared against the live row set, not the other way around. A dimension the method
names with no check of any kind (mechanical or attestation) is a fail under (b) even if every
existing row individually passes (a). [Demonstrated live 2026-08-30 on `phenomenon.set`: 5/6
method-stated dimensions have a row; "whether stated or inferred is recorded honestly" has none.]

### cfg_method_rule
Same shape of correction as `cfg_quality_check`, for the same reason — it is the interpretive
counterpart, and the original success text has the identical existence-only flaw.
**Original success:** "Every active rule is genuinely consulted by its step's real handler code...
source_doc traces to a real authoritative instruction." — again: does each existing row work, not
whether the rule set is complete.
**REVISED success:** every active rule genuinely consulted [kept]; AND the rule set for each step,
checked against its governing method document, has no substantive requirement missing outright —
same derive-independently-first discipline as `cfg_quality_check`. Not yet run against any step
other than the `phenomenon.set` spot-check above.

### cfg_prose_concept
**Original success:** "Every concept_key's chapter/section_hint actually resolves to a real,
current prose_section; the concept is genuinely referenced by that name somewhere, not an orphan
label." — This is the exact wording that let `inner_being_definition` sit unused: "referenced by
that name somewhere" is satisfied by a comment or a docstring, and was never actually verified
against live code before today.
**REVISED success:** the pointer resolves to a real prose section [kept]; AND **the concept is
actually dereferenced at the point of use by the code path that depends on understanding it** —
not merely named in a comment, escalation, or migration docstring. Every row in this table should
be traceable to at least one real call site that reads it, the same standard just applied to
`cfg_prose_concept.inner_being_definition` and found failing.

### cfg_behaviour_rule
**Original success:** "Every rule is a real, distinct, non-duplicated discipline; confirmed clean
2026-08-30 — 61 rows across 7 classes, no duplicate rule_keys, all active." — dedup/existence
only; says nothing about whether the *set* actually covers the project's real failure history.
**REVISED success:** no duplicates, all active [kept]; AND **every documented incident that
produced a corrective lesson (an escalation, a session-log "caught myself" entry, a researcher
correction) has a corresponding rule** — checked against the actual incident record, not asserted
from the rule table's own completeness-feeling. Not yet run; this requires cross-referencing
escalation history and session logs against the 61 rule rows, which hasn't been done.

### cfg_behaviour_class
**Original success:** tests non-overlap between the 7 classes only.
**REVISED success:** no overlap [kept]; AND the 7 classes are actually exhaustive of what the
project needs regulated — checked by testing whether any real behaviour rule (present or
needed) fails to fit cleanly into one of the 7, not assumed from the fact that none currently
does.

### cfg_report / cfg_report_section
**Original success (both):** "the step is real and active; the actual generated report genuinely
matches these settings." — tests that the code obeys its own config, not that the config
specifies a *good* report.
**REVISED success:** code-matches-config [kept]; AND the specified title/TOC/section
order/inclusion set actually gives the report's real reader what they need — right sections
present in a sensible order, nothing structurally important silently excluded, naming/archiving
scheme matched to how the report is actually consumed downstream. This is the direct reporting-
domain test named in your last message (layout, content, headers, location) — not yet run against
any specific report.

**Added, from the `cfg_setting` finding below:** `cfg_report`'s own success can't be judged solely
from its own rows — its declared jurisdiction (`naming_scheme`, `archive_dir`: "how a report should
look and where it lives") is currently fragmented across two other places (`cfg_setting`'s `report`
module, and `governance.oneoff_report_*`) with no rule reconciling them. A table can hold every one
of its own rows correctly and still fail this test if a *second* table is silently doing part of
its job — success for a domain table includes that nothing else in the config store has
overlapping, unreconciled jurisdiction over the same concern.

### cfg_enum
**Original success:** "every group is actually enforced against live data... zero violations
across the whole dataset."
**REVISED success:** zero violations [kept]; AND, for a group backing a substantive taxonomy (e.g.
`hib_kind`'s six-type plurality×specificity scheme), **the scheme itself has a documented
completeness argument** — zero violations observed so far is not proof the taxonomy can't be
broken by a real case not yet encountered; the taxonomy's own derivation should be checked against
the method document that defines it, not only against data seen to date.

### cfg_setting
**Original success (superseded):** "every key is read... every key has a real module attribution —
the governance.* slice (46 rows) already confirmed 100% clean." Superseded 2026-08-30 — checked the
table's actual content (169 rows, 21 `module` values) rather than leave this as a placeholder, per
direct challenge (*"I would even be amazed if you come up with a definition that let it feel as if
settings really fulfill its purpose, and it not confusing"*). It doesn't, as originally written,
because the table is not one thing.

**Corrected purpose — split, not singular.** `cfg_setting` actually holds two different kinds of
content under one shape: (a) genuine standalone project-wide policy with no natural dedicated table
(most of the `governance` module's 48 rows — `rules_must_be_config_driven`, `scope_project`,
`verse_gap_by_design`, `prose_canonical_authority`, etc.); and (b) subsystem-scoped operational
tuning (`report.*`, `lexicon.*`, `narrative.*`, `validation.*`, `notification.*`, `candidate.*`,
`backup.*`, and 15 more), some of which have never been reconciled against a subsystem's own
dedicated config table where one already exists.

**Concrete, live proof this is a real split, not a theoretical one:** `report` (27 rows in
`cfg_setting`) governs the same ground `cfg_report` already has dedicated columns for
(`naming_scheme`, `archive_dir`). `report.word` is a live row in *both* tables at once —
`cfg_report`: `naming_scheme='dated'`; `cfg_setting`: `report.output_dir`/`report.output_pattern` —
with no rule anywhere saying how the two combine or which wins. A *third* layer duplicates the same
concern again: `governance.oneoff_report_dir`/`_naming_pattern`/`_format`/`_archive_dir`, for
reports that bypass `cfg_report`'s step-registration entirely. Three mechanisms, one concern, zero
reconciling rule. Checked whether this recurs for the other subsystems that already have a
dedicated table (`passage`, `prose`): neither appears as a `cfg_setting` module at all, so the
collision looks confined to `report` — but this was checked only for those two, not systematically
against all 21 modules.

**REVISED success:** for slice (a), read-and-attributed is a fair test, as before. For slice (b), a
module only passes if **every key in it has been checked against whether a dedicated table for that
subsystem already exists and, if so, that the two don't silently overlap or conflict** — which
`report` currently fails outright, and which hasn't yet been checked for the other 19 modules.
Until `report`'s three-way split is either merged into `cfg_report`'s own schema or deliberately
kept separate with a documented, enforced boundary, no purpose statement for `cfg_setting` can
honestly read as non-confusing — the confusion is in the live config, not just in how it's
described.

### cfg_passage / cfg_prose
**Original success (both):** module settings are read by the right code; values match where output
currently lands.
**REVISED success:** matches current behaviour [kept]; AND that current behaviour is actually the
*intended* destination/shape, confirmed against the researcher's actual intent — not merely
self-consistent with wherever the code happens to write today, which would pass even if the
current behaviour itself were wrong.

---

## Not yet touched by this correction

Every "stands" verdict above got a re-read, not a fresh independent derivation the way
`phenomenon.set`'s quality-check set just did. The domain-content tables marked REVISED have a
corrected *test* stated now, but most of those tests haven't actually been *run* yet — only
`cfg_quality_check` has one worked example (`phenomenon.set`). The rest of this file is the
standard to apply next, not a completed audit.
