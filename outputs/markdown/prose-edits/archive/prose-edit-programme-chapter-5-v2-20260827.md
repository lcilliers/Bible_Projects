# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 32,33,34,35,36,37,38 -->

<!-- PROSE_SECTION_ID: 32 -->
<!-- PROSE_SECTION_TYPE: prog_validation_standard -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Document Validation Standard -->
<!-- PROSE_SORT_ORDER: 104 -->
<!-- PROSE_VERSION: 1187 -->

## Document validation and quality-flag architecture

The programme's validation architecture is `iba.db`'s own, and it operates continuously rather than at fixed phase boundaries: `configmaint.validate` is the standing check that sweeps the entire `cfg_*` config store and the data it governs, and it is what a session runs to know whether the app's own rules are internally coherent.

`configmaint.validate` covers a growing list of concerns, each added as a real gap was found live rather than designed in advance: enum violations (a value that should be drawn from a `cfg_enum` list but isn't), orphan-config detection (a `cfg_*` row that nothing reads), inactive-reference coherence (something still pointing at a row marked `inactive`), write-grant completeness (every writer that touches a table actually holds a grant for it), stale `filled_by` claims, report-path persistence (every quality-check step must write its output somewhere config says it should, not just print to the terminal), and doc-currency checks tying `GOVERNANCE.md`/`BUILD.md` claims back to the config they describe.

For the book-by-book debate pipeline specifically, the inflection point is `passage.debate_status`: a passage moves from having no debate status, to `filled` (the debate content has been authored), to `complete`. `passage.debate_sync` is the registered step that checks an already-written debate file against its fill-in-placeholder marker and advances the status accordingly — a config-driven check, not something inferred from reading how a prior book's debate happened to reach `complete`.

Gap status generally is expressed as a controlled vocabulary wherever the schema has one — `cfg_enum` names every allowed value for every enumerated column, project-wide, and `configmaint.validate`'s enum check is what catches a value that has drifted outside its declared set.

**Quality flags.** `wa_quality_flag_types` and `wa_data_quality_flags` serve the prose store: a `PROSE_QUALITY` flag names a concern about the prose corpus generally — a stale terminology reference, a superseded claim — without being tied to one `prose_section` row at raise time, because the section a flag concerns is found by search at fix time (`Prose.ps1 -Step FlagFixPropose`), not stored from when the flag was raised.

Quality flags are distinct from findings and from escalations: a flag names that attention is due, not an analytical conclusion, and it does not block anything from proceeding on its own. Where a flag concerns a genuine judgement call rather than a mechanical fix, it is raised as an escalation instead — the mechanism described in the sub-section on instruction override, which names a state that needs resolution, tracks it to closure, and leaves a permanent record of what was decided and why.

---

<!-- PROSE_SECTION_ID: 33 -->
<!-- PROSE_SECTION_TYPE: prog_delete_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Soft-Delete Discipline -->
<!-- PROSE_SORT_ORDER: 105 -->
<!-- PROSE_VERSION: 1188 -->

## Soft-delete discipline

The programme does not physically delete rows as a matter of course, and the discipline spans both databases. `iba.db`'s base-data and process-control tables carry a uniform `deleted` column; `bible_research.db`'s analytical tables carry `delete_flagged` (or, on some tables, `delete_flag`). Both are the same convention under different names: the row stays in the database, queryable for audit, excluded from active queries by a filter on the flag.

A table-level form of the same discipline sits above the row-level one. `cfg_table.inactive` marks a whole table as superseded, not just individual rows within it — the mechanism by which the project's own governance record can state precisely which of a database's tables are the live source of truth and which are not, without deleting or hiding either.

The prose store's own lifecycle mechanism is Model A: system-versioned temporal tables (escalation #836, 2026-08-24). A revision mutates the row in place under SQLite's own system-versioned mechanism rather than inserting a new row and chaining it by hand; nothing is silently lost, the full history is queryable, and the guarantee now comes from the database engine itself rather than application bookkeeping.

The discipline is not absolute. A hard delete is reserved for content that genuinely has no future reader and has no live consumer to preserve continuity for — a decision made deliberately when it happens, not a default falling-through. Soft-delete is the default because the programme revisits its own work and needs the trail that decision-making left behind.

Soft-delete is not the same as set-aside: a row marked not-relevant to the current analytical scope is a different fact from a row marked removed from scope entirely. The purpose of the whole discipline is continuity under revision — the programme revisits words, re-derives readings, and rebuilds mechanisms; a database that deleted rows as its understanding changed would lose the very trail that makes its current state defensible.

---

<!-- PROSE_SECTION_ID: 34 -->
<!-- PROSE_SECTION_TYPE: prog_field_authority -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Record consistency with sources -->
<!-- PROSE_SORT_ORDER: 106 -->
<!-- PROSE_VERSION: 1189 -->

## Record consistency with sources

The programme's research record is a derived record, resting on STEP Bible for lexical and verse data and on the researcher's own judgement for classification and analysis. Three disciplines keep the record consistent with those sources.

**Field authority.** The mechanism for declaring which field wins when two hold the same information is `cfg_column`: every column in every table, in both databases, is required to be listed with a `use` text, and — where relevant — a `source`, an `expectation`, and a `filled_by`. `expectation` is enforced at write time (value-quality plus `enum.*` checks, part of `configmaint.validate`); `source`/`filled_by` are recorded but only checked for non-emptiness today — a named, open gap, not a silent one. `use` remains documentation only. Where the schema itself carries the same fact in two places across the two databases, the `inactive` flag on the `cfg_table` row for each copy is the authority declaration: the active copy is the one that wins.

**Finding-reference consistency.** `finding` carries `superseded_by_id` when a row is superseded by a revised finding, and `obsolete_reason`/`obsolete_date` when a row is obsoleted; both rows remain in the database, linked through the chain. A reference into `finding` is a reference to the finding's identity, not to its state at the moment of reference — its meaning is read by following the chain rather than assumed fixed.

**STEP data provenance.** STEP Bible remains the primary source for every Strong's number, gloss, meaning parse, and verse reference in the corpus. The live provenance record for `iba.db`'s base-data layer is the `run` table (1,871 rows) together with `cfg_connection`/`cfg_api`, which record what STEP route was called, under what configuration, and what came back.

The governing principle is unchanged across all three: the record is derived, not primary, and its integrity depends on the chain from source to stored row staying traceable across every revision.

---

<!-- PROSE_SECTION_ID: 35 -->
<!-- PROSE_SECTION_TYPE: prog_backup_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Backup and schema migration discipline -->
<!-- PROSE_SORT_ORDER: 107 -->
<!-- PROSE_VERSION: 1190 -->

## Backup and schema migration discipline

Each of the programme's two databases carries its own backup and versioning discipline, governed by the same underlying principle: every state-changing operation is recoverable, and every schema or configuration change is traceable to a specific, dated event.

**`bible_research.db`.** `schema_version` carries the schema's own migration history — sixteen recorded migrations at time of writing, the schema currently at `3.40.0`, each entry an M-number with a description and an applied timestamp. `apply_session_patch.py` takes a backup of the whole database before every live write, automatically, as a normal part of applying a patch. Off-repository durability is handled outside the patch mechanism: a daily NAS backup of the database file, a daily full-project mirror, both alerting on failure.

**`iba.db`.** Configuration versioning is `cfg_meta.config_version` rather than a `schema_version` table, and every whole-reload event is logged to `cfg_change_log`; every row-level change made through `configmaint.propose` is logged to `cfg_change_detail` — table, operation, the `where`/`set` clauses, the before-state, and when it was applied. `run.py` takes a pre-run database snapshot before every new run, wired in after a 2026-07-22 incident in which a bug corrupted candidate-seed data with no fine-grained rollback point available; `retention.snapshot_keep_count` (currently 5) governs how many of these snapshots are kept before the oldest is pruned. A routine that would otherwise take a snapshot on every iteration of a large batch can suppress it deliberately (`--no-backup`) where the cost is disproportionate to the risk.

The principle that unifies both databases' disciplines: a change without a recoverable prior state is a risk the programme does not accept, and a change without a record of what changed and when is a change the programme cannot later account for.

---

<!-- PROSE_SECTION_ID: 36 -->
<!-- PROSE_SECTION_TYPE: prog_patch_failure_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Patch and directive failure protocol -->
<!-- PROSE_SORT_ORDER: 108 -->
<!-- PROSE_VERSION: 1191 -->

## Patch and directive failure protocol

Patches and directives remain the two channels by which changes reach `bible_research.db`. `apply_session_patch.py`'s dry-run mode, used before every live apply, is the standing rejection check: a patch that violates a schema constraint or a controlled-vocabulary rule is caught before it ever reaches the live database.

`iba.db` runs a parallel failure protocol, built around `cfg_on_fail` rather than around patch review. Every step in the app's run sequence has a registered `(step, condition) → path` entry: `report-stop` halts the run and surfaces the failure; `pause-continue` and `report-continue` let the run proceed past a non-fatal condition while still surfacing it; `self-heal` lets a step correct a known, narrow condition on its own. Changing how a specific failure is handled is itself a config change — moving `cfg_on_fail` for a given `(step, condition)` from one path to another through `Config-Maintenance.ps1 -Step Propose` changes the app's behaviour with no code touched.

Where a failure — on either side of the split — cannot be resolved by a mechanical retry or a rejected patch, it is raised as an escalation. An escalation carries a `resolution_kind`: `decision_required` for a genuine judgement call that must go to the researcher and stops there, or `self_correctable` for a condition Claude can fix and record, with the fix itself named in the resolution.

The protocol's governing principle: no failure is allowed to leave either database in an inconsistent, unrecorded state. The mechanism enforcing it is split along the same line as the databases themselves — patch review for `bible_research.db`'s analytical content, `cfg_on_fail` routing and escalation resolution for `iba.db`'s process-control and base-data operations.

---

<!-- PROSE_SECTION_ID: 37 -->
<!-- PROSE_SECTION_TYPE: prog_instruction_override_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Instruction override and cross-document reference discipline -->
<!-- PROSE_SORT_ORDER: 109 -->
<!-- PROSE_VERSION: 1192 -->

## Instruction override and cross-document reference discipline

**Instruction override.** The researcher's in-session direction is authoritative, and it does not wait on document revision to take effect. The path it travels is `iba\app\ps\Config-Maintenance.ps1 -Step Propose`, the one sanctioned route to changing any `cfg_*` row. A proposed change names the table, the operation, the `where`/`set` clauses, and a question stating why the change is wanted and what it affects; the command runs a coherence check before it ever reaches the researcher, then pauses and prints a run id. The researcher answers through `Escalation.ps1 -Action Update`, moving the raised escalation through `ready_for_approval` to `approved` (or `reject`/`revise`), each with a `resolution`; only then does the same Propose command, re-run against the same run id, commit the write, logged row-by-row to `cfg_change_detail`. An override that is approved this way is, from that point on, no longer an override — it is the rule the config holds, and every part of the app that reads that setting sees the new value immediately, with no code edit required.

For anything that is not a `cfg_*` value — a genuine open question, a discovered anomaly, a clarification needed, a piece of work assigned across a session boundary — the `escalation` table is the single project-wide mechanism: "all open items, discovery of anomalies, clarifications and other forms of escalation must be recorded in escalation using escalation rules" (`governance.escalation.scope`), covering the whole project. An escalation carries a `type`, a `state` that moves through `raised` → (`re-assigned` / `on-hold` / `in-progress`) → a terminal state, a `next_action`, and a `resolution_kind` (`decision_required` / `self_correctable`). `Escalation.ps1 -Action Raise|Update|History|List|Correction|ResolveSelfCorrectable|EscalateToDecision` is the operational front door.

**The `[current]` convention, retained.** The instruction corpus under `Workflow/Instructions/` still uses the `[current]` token for operational cross-references, resolving to the highest-numbered version present at read time, with specific version strings reserved for provenance. This convention is defined directly in `CLAUDE.md` §10.

The two disciplines together describe a cleanly split system: a `cfg_*` rule change is proposed, coherence-checked, approved by explicit decision, and committed with a full audit trail — `Config-Maintenance.ps1` end to end. A genuine open question or anomaly, anywhere in the project, is raised, tracked, and resolved through `escalation` — `Escalation.ps1` end to end.

---

<!-- PROSE_SECTION_ID: 38 -->
<!-- PROSE_SECTION_TYPE: prog_doc_impl_alignment -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Documentation–implementation alignment -->
<!-- PROSE_SORT_ORDER: 110 -->
<!-- PROSE_VERSION: 1193 -->

## Documentation–implementation alignment

The programme's rules, its database schema, its instruction documents, and the prose that describes the work are four surfaces that must stay in alignment for the record to be trustworthy — the alignment is not a state the programme can declare once and rely on thereafter, and this principle is itself now a config-governed rule, not only a value this chapter asserts.

`governance.rules_must_be_config_driven` (`cfg_setting`, module `governance`) states it directly: no operational or process rule may exist only in `GOVERNANCE.md`, `BUILD.md`, `USER-GUIDE.md`, or memory, without a referenced `cfg_*` row recording it as the evidence that the configuration control is actually in operation; any deviation found requires an escalation. `governance.governance_md_on_rule_change` pairs it on the documentation side: a governance or process rule change must be set in `cfg_*` first, via `configmaint.propose`, and `GOVERNANCE.md` updated to reflect it in the same unit of work. `governance.build_md_on_code_change` runs the equivalent check for code: any change under `iba/app/**` must update `BUILD.md`'s build record in the same unit of work.

A fourth rule closes the loop the other three depend on: `governance.past_precedent_investigation_signals_missing_config`. If running an already-registered instruction requires first reconstructing how it was done in the past — reading `BUILD.md` history, diffing archived output files, inferring a missing step from precedent — rather than a live `cfg_step`/`cfg_setting` row saying directly what to run, that investigation is itself the signal that a required config or mechanism is missing, and the correct response is to stop and close the gap, not to proceed on the reconstructed precedent and present it as the standard process.

Where a mismatch between surfaces is detected, the response the four rules above prescribe is consistent in shape: the mismatch is named, an escalation is raised if it isn't self-evidently a mechanical fix, and the resolution updates whichever surface was wrong, in the same unit of work, with the change recorded in `cfg_change_detail` or `BUILD.md`'s history as appropriate. A mismatch is not left open on the assumption that documentation will eventually catch up to practice, or practice will eventually catch up to documentation.

---
