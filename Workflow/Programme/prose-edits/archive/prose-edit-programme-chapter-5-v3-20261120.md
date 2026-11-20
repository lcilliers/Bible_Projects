# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 32,33,34,35,36,37,38 -->

<!-- PROSE_SECTION_ID: 32 -->
<!-- PROSE_SECTION_TYPE: prog_validation_standard -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Document Validation Standard -->
<!-- PROSE_SORT_ORDER: 104 -->
<!-- PROSE_VERSION: 1221 -->

## Document validation and quality-flag architecture

The programme's validation architecture is `iba.db`'s own, and it operates continuously and not only at phase boundaries. Five standing checks together tell a session whether the app, the record and the study are coherent.

`configmaint.validate` sweeps the whole `cfg_*` configuration store and the data it governs. It covers enum violations (a value that should be drawn from a `cfg_enum` list but is not), orphan configuration (a `cfg_*` row that nothing reads), inactive-reference coherence (something still pointing at a row marked inactive), write-grant completeness (every writer that touches a table holds a grant for it), stale `filled_by` claims, report-path persistence (every quality-check step writes its output where configuration says), the currency of the glossary against the terms it must define, and documentation-currency checks that tie `GOVERNANCE.md` and `BUILD.md` back to the configuration they describe. Each concern was added when a real gap was found, not designed in advance.

The **compliance check** (`Compliance.ps1`) runs at the start of every session: Claude restates in its own words every general rule in force, with the work in hand, and the check must pass before work begins; evidence for each engaged rule is added as the session produces it, and the close checks it.

The **session-close checks** compare what the session did, decided and left open against the record, and nothing is committed while a finding is open. `Spine-Check.ps1` checks the spine of the project's own records, and the **thread audit** (`Escalation.ps1 -Action ThreadAudit`) checks the threads of open items for handles that do not resolve, items without a note, referred items closed while the thread item is open, and registers out of date.

For the reading, the **layer check** validates every answered row of a step against the tables (its stage, kind, nodes, roles, collection and every Strong's code of an enrichment) and reports what is open, what failed and what the data demands that has no row. The **grouping check** validates a grouping of surfaces and writes a scrutiny report for the researcher. A boundary check keeps the observations of the lexical stages free of what a word does for the inner being.

Gap status is expressed as a controlled vocabulary wherever the schema has one: `cfg_enum` names every allowed value of every enumerated column, and the enum check catches a value that has drifted outside its declared set.

**Quality flags.** `wa_quality_flag_types` and `wa_data_quality_flags` serve the prose store: a `PROSE_QUALITY` flag names a concern about the prose corpus generally, such as a stale terminology reference, without being tied to one section at raise time, because the section is found by search at fix time (`Prose.ps1 -Step FlagFixPropose`). A flag names that attention is due, not an analytical conclusion, and it does not block anything on its own. Where a flag concerns a genuine judgement call and not a mechanical fix, it is raised as an escalation instead, the mechanism described in the section on instruction override.

---

<!-- PROSE_SECTION_ID: 33 -->
<!-- PROSE_SECTION_TYPE: prog_delete_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Soft-Delete Discipline -->
<!-- PROSE_SORT_ORDER: 105 -->
<!-- PROSE_VERSION: 1222 -->

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
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Record consistency with sources -->
<!-- PROSE_SORT_ORDER: 106 -->
<!-- PROSE_VERSION: 1223 -->

## Record consistency with sources

The programme's research record is a derived record, resting on STEP Bible for lexical and verse data and on the researcher's own judgement for the analysis. Three disciplines keep the record consistent with those sources.

**Field authority.** The mechanism for declaring which field wins when two hold the same information is `cfg_column`: every column of every table, in both databases, is listed with a `use` text and, where relevant, a `source`, an `expectation` and a `filled_by`. `expectation` is enforced at write time (value-quality and enum checks, part of `configmaint.validate`); `source` and `filled_by` are recorded and checked for non-emptiness; `use` is documentation. Before a table or column is used for a count, a finding, a claim or a design, its recorded meaning is read in `cfg_table` and `cfg_column`, and a statement about what a column holds is made only from that text or from a test over all its rows. Where the recorded text is missing or thin, that is raised as a finding and the column is not assumed. Where the schema carries the same fact in two places, the `inactive` flag on the `cfg_table` row of each copy declares which copy wins. A column added to an existing data table is registered in `cfg_column` by the stated procedure before it is used.

**Observation-reference consistency.** An observation that is revised or withdrawn is not overwritten or deleted: its change is kept in `ib_observation_change` with the reason, and a replacing observation points to the one it supersedes. A reference to an observation is a reference to its identity, and its meaning is read by following the chain and not assumed fixed.

**STEP data provenance.** STEP Bible remains the primary source for every Strong's number, gloss, meaning parse and verse reference in the corpus. The live provenance record for the base data in `iba.db` is the `run` table together with `cfg_connection` and `cfg_api`, which record what STEP route was called, under what configuration, and what came back.

The governing principle is the same for all three: the record is derived and not primary, and its integrity depends on the chain from source to stored row staying traceable across every revision.

---

<!-- PROSE_SECTION_ID: 35 -->
<!-- PROSE_SECTION_TYPE: prog_backup_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Backup and schema migration discipline -->
<!-- PROSE_SORT_ORDER: 107 -->
<!-- PROSE_VERSION: 1224 -->

## Backup and schema migration discipline

Each of the programme's two databases carries its own backup and versioning discipline, governed by one principle: every state-changing operation is recoverable, and every schema or configuration change is traceable to a specific, dated event.

**`bible_research.db`.** `schema_version` carries the schema's own migration history, each entry a numbered migration with a description and an applied timestamp. `apply_session_patch.py` takes a backup of the whole database before every live write, automatically, as part of applying a patch. Off-repository durability is handled outside the patch mechanism by a daily backup of the database file and a daily mirror of the whole project, each alerting on failure.

**`iba.db`.** Configuration versioning is `cfg_meta.config_version`; every whole-reload event is logged to `cfg_change_log`; and every row-level change to configuration is logged to `cfg_change_detail` with its table, operation, `where` and `set` clauses, the before-state and when it was applied. `run.py` takes a pre-run database snapshot before every new run, and `retention.snapshot_keep_count` governs how many of these are kept before the oldest is pruned. A routine that would take a snapshot on every iteration of a large batch can suppress it deliberately where the cost is disproportionate to the risk. A named snapshot is taken before a change to the collections or to the observations and is kept (`iba/app/db/snapshots/kept/`), so that the change can be rehearsed on a copy, its counts predicted and checked, and, if it fails, undone from a known state.

The principle that unifies both disciplines: a change without a recoverable prior state is a risk the programme does not accept, and a change without a record of what changed and when is a change the programme cannot later account for.

---

<!-- PROSE_SECTION_ID: 36 -->
<!-- PROSE_SECTION_TYPE: prog_patch_failure_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Patch and directive failure protocol -->
<!-- PROSE_SORT_ORDER: 108 -->
<!-- PROSE_VERSION: 1225 -->

## Patch and directive failure protocol

Patches and directives remain the two channels by which changes reach `bible_research.db`. `apply_session_patch.py`'s dry-run mode, used before every live apply, is the standing rejection check: a patch that violates a schema constraint or a controlled-vocabulary rule is caught before it ever reaches the live database.

`iba.db` runs a parallel failure protocol, built around `cfg_on_fail` rather than around patch review. Every step in the app's run sequence has a registered `(step, condition) → path` entry: `report-stop` halts the run and surfaces the failure; `pause-continue` and `report-continue` let the run proceed past a non-fatal condition while still surfacing it; `self-heal` lets a step correct a known, narrow condition on its own. Changing how a specific failure is handled is itself a config change — moving `cfg_on_fail` for a given `(step, condition)` from one path to another through `Config-Maintenance.ps1 -Step Propose` changes the app's behaviour with no code touched.

Where a failure — on either side of the split — cannot be resolved by a mechanical retry or a rejected patch, it is raised as an escalation. An escalation carries a `resolution_kind`: `decision_required` for a genuine judgement call that must go to the researcher and stops there, or `self_correctable` for a condition Claude can fix and record, with the fix itself named in the resolution.

The protocol's governing principle: no failure is allowed to leave either database in an inconsistent, unrecorded state. The mechanism enforcing it is split along the same line as the databases themselves — patch review for `bible_research.db`'s analytical content, `cfg_on_fail` routing and escalation resolution for `iba.db`'s process-control and base-data operations.

---

<!-- PROSE_SECTION_ID: 37 -->
<!-- PROSE_SECTION_TYPE: prog_instruction_override_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Instruction override and cross-document reference discipline -->
<!-- PROSE_SORT_ORDER: 109 -->
<!-- PROSE_VERSION: 1226 -->

## Instruction override and cross-document reference discipline

**Instruction override.** The researcher's in-session direction is authoritative and does not wait on document revision to take effect. The path it travels for a configuration row is `Config-Maintenance.ps1 -Step Propose`, the one sanctioned route in a standard session. A proposed change names the table, the operation, the `where` and `set` clauses, and a question stating why the change is wanted and what it affects; the command runs a coherence check and pauses, printing a run id. The researcher answers through `Escalation.ps1 -Action Update`, moving the raised escalation through `ready_for_approval` to `approved` (or `reject` or `revise`), each with a resolution; only then does the same Propose command, re-run against the same run id, commit the write, logged row by row to `cfg_change_detail`. In a Developer Mode session, which the researcher chooses when the session starts and which is never switched within it, the app is built or fixed without the per-row approval gate, through one idempotent logged migration; every rule still applies. An override approved this way is from then on no longer an override: it is the rule the configuration holds, and every part of the app that reads it sees the new value with no code edit.

For anything that is not a configuration value, such as a genuine open question, a discovered anomaly, a clarification needed or a piece of work assigned across a session boundary, the `escalation` table is the single project-wide mechanism (`governance.escalation.scope`), covering the whole project. An escalation carries a type, a state that moves from `raised` through `re-assigned`, `on-hold` or `in-progress` to a terminal state, a `next_action` and a `resolution_kind` (`decision_required` or `self_correctable`). The researcher's words that bear on an item are recorded on it verbatim in the same turn. `Escalation.ps1` is the operational front door, with the actions Raise, Update, History, List, Correction, ResolveSelfCorrectable and EscalateToDecision. Open items that are pointers from an analysis in hand to related work are registered with their origin and anchor, scoped to specific verses, and cleared at some point.

**Where the rules live.** `CLAUDE.md` is a pointer file: it holds no rules, no state and no history. The rules, settings and procedures of the project are configuration rows, printed at the start of a session or delivered at the first use of the operation they govern, and the control map (`cfg_control_home`) names the home of each kind of content. Where a document and its home disagree, the home wins.

The two disciplines together describe a cleanly split system: a configuration rule is proposed, coherence-checked, approved by explicit decision and committed with a full audit trail; a genuine open question or anomaly, anywhere in the project, is raised, tracked and resolved through the escalation table.

---

<!-- PROSE_SECTION_ID: 38 -->
<!-- PROSE_SECTION_TYPE: prog_doc_impl_alignment -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Data integrity & governance -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_SECTION_TITLE: Programme — Documentation–implementation alignment -->
<!-- PROSE_SORT_ORDER: 110 -->
<!-- PROSE_VERSION: 1227 -->

## Documentation–implementation alignment

The programme's rules, its database schema, its instruction documents and the prose that describes the work are four surfaces that must stay in alignment for the record to be trustworthy. Alignment is not a state the programme can declare once and rely on afterward, and the principle is itself a configuration-governed rule.

`governance.rules_must_be_config_driven` states it directly: no operational or process rule may exist only in `GOVERNANCE.md`, `BUILD.md`, `USER-GUIDE.md` or memory without a referenced `cfg_*` row recording it as the evidence that the configuration control is in operation; any deviation found requires an escalation. On a new instruction, the first thing established is that the rules governing it are fully captured and correctly interpreted in the configuration. `governance.governance_md_on_rule_change` pairs it on the documentation side: a rule change is set in `cfg_*` first and `GOVERNANCE.md` updated in the same unit of work. `governance.build_md_on_code_change` runs the equivalent check for code: any change under `iba/app` updates `BUILD.md` in the same unit of work. The control map `cfg_control_home` states, for each kind of content, its one home: content lives in its kind's home only, and any other document points to it and does not restate it.

A further rule closes the loop: `governance.past_precedent_investigation_signals_missing_config`. If running an already-registered instruction requires first reconstructing how it was done in the past, by reading `BUILD.md` history, diffing archived output files or inferring a missing step from precedent, instead of a live configuration row saying what to run, that investigation is itself the signal that a required mechanism is missing, and the response is to stop and close the gap, not to proceed on the reconstructed precedent. A table or mechanism is added by the stated procedure, and a column added to an existing data table is registered before it is used.

The record is the project's memory. The researcher's earlier instructions and answers are in the escalation record and the session logs, and are read there before a question is put; a question the record answers, or that later work made moot, is not asked.

Where a mismatch between surfaces is detected, the response is consistent in shape: the mismatch is named, an escalation is raised if it is not a mechanical fix, and the resolution updates whichever surface was wrong in the same unit of work, with the change recorded in `cfg_change_detail` or `BUILD.md` as appropriate. A mismatch is not left open on the assumption that documentation will eventually catch up to practice, or practice to documentation.

---

