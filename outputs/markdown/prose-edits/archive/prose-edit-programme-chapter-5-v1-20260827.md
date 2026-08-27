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
<!-- PROSE_VERSION: 119 -->

## Document validation and quality-flag architecture

The programme's validation standard no longer runs on the Session A/B/C/D phase-gate model this section used to describe — that pipeline, and the `phase1_status`/`verse_context_status`/`dim_review_status`/`session_b_status` gates it advanced words through, belongs to the retired registry described in Chapter 4. The live validation architecture is `iba.db`'s own, and it operates continuously rather than at fixed phase boundaries: `configmaint.validate` is the standing check that sweeps the entire `cfg_*` config store and the data it governs, and it is what a session runs to know whether the app's own rules are internally coherent, not just whether one word's data is complete.

`configmaint.validate` covers a growing list of concerns, each added as a real gap was found live rather than designed in advance: enum violations (`find_enum_violations` — a value that should be drawn from a `cfg_enum` list but isn't), orphan-config detection (a `cfg_*` row that nothing reads), inactive-reference coherence (something still pointing at a row marked `inactive`), write-grant completeness (every writer that touches a table actually holds a grant for it), stale `filled_by` claims, report-path persistence (`find_missing_report_paths` — every quality-check step must write its output somewhere config says it should, not just print to the terminal), and doc-currency checks tying `GOVERNANCE.md`/`BUILD.md` claims back to the config they describe. Each of these was added after a concrete violation was found, not as a pre-built checklist — the standard grows by the same discipline it enforces: a gap found live gets closed and registered, not patched over quietly.

For the book-by-book debate pipeline specifically, the inflection point is `passage.debate_status`: a passage moves from having no debate status, to `filled` (the debate content has been authored), to `complete`. `passage.debate_sync` is the registered step that checks an already-written debate file against its fill-in-placeholder marker and advances the status accordingly — built precisely so that this transition is a config-driven check, not something inferred from reading how a prior book's debate happened to reach `complete`.

Gap status generally is expressed as a controlled vocabulary wherever the schema has one — `cfg_enum` names every allowed value for every enumerated column, project-wide, and `configmaint.validate`'s enum check is what catches a value that has drifted outside its declared set. A record whose status does not resolve to a value `cfg_enum` recognises is itself a validation failure, exactly as the old phase-status fields were meant to work, but enforced by a live check against the config rather than by convention.

**Quality flags.** The programme's quality-flag mechanism was rebuilt on 2026-08-23 (escalation #833) around a different purpose than the one this section previously described. `wa_quality_flag_types` and `wa_data_quality_flags` no longer carry term-quality content — the prior 29 flag codes and 19,866 flag rows were hard-deleted outright, with no data carried over, a deliberate exception to the soft-delete discipline described in the next sub-section, made because the old content served a per-word analytical pipeline that no longer runs. The same two tables now serve the prose store: a `PROSE_QUALITY` flag names a concern about the prose corpus generally — a stale terminology reference, a superseded claim — without being tied to one `prose_section` row at raise time, because the section a flag concerns is found by search at fix time (`Prose.ps1 -Step FlagFixPropose`), not stored from when the flag was raised.

Quality flags remain distinct from findings and from escalations in the same way this section previously drew that line: a flag names that attention is due, not an analytical conclusion, and it does not block anything from proceeding on its own. Where a flag concerns a genuine judgement call rather than a mechanical fix, it is raised as an escalation instead — the mechanism described in the sub-section on instruction override, which has itself absorbed most of what the old inflection-point/gap-status apparatus was built to do: name a state that needs resolution, track it to closure, and leave a permanent record of what was decided and why.

---

<!-- PROSE_SECTION_ID: 33 -->
<!-- PROSE_SECTION_TYPE: prog_delete_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Soft-Delete Discipline -->
<!-- PROSE_SORT_ORDER: 105 -->
<!-- PROSE_VERSION: 120 -->

## Soft-delete discipline

The programme still does not physically delete rows as a matter of course, and the discipline now spans two databases rather than one. `iba.db`'s base-data and process-control tables — `word_strong`, `strong`, `strong_related`, `verse`, `span`, `passage`, `hib`, `phenomenon`, `operation`, `cluster_strong`, `candidate_seed`, and the rest — carry a uniform `deleted` column; `bible_research.db`'s retained analytical tables carry `delete_flagged` (or, on `wa_session_b_findings`, `delete_flag`). Both are the same convention under different names: the row stays in the database, queryable for audit, excluded from active queries by a filter on the flag.

A table-level form of the same discipline now sits above the row-level one. `cfg_table.inactive` marks a whole table as superseded, not just individual rows within it — this is how Chapter 4 is able to state, precisely, that `bible_research.db`'s `verse`, `word_registry`, `mti_terms`, `wa_term_inventory`, `wa_verse_records`, `wa_file_index`, `wa_rule_registry`, `wa_addendum_registry`, and `term_fetch_log` are retired while the physical rows remain intact and readable. The table isn't dropped, and its data isn't purged; it is marked, in the config that governs the whole schema, as no longer the place current work reads from or writes to. This is the soft-delete principle applied one level up, to the architecture itself rather than to a record within it.

The prose store's own lifecycle mechanism changed on 2026-08-24 (escalation #836, described fully in Chapter 4's prose-store sub-section): where a revision used to insert a new `prose_section` row and chain it from the old one through `supersedes_id`/`superseded_by_id`, it now mutates the row in place under SQLite's own system-versioned temporal-table mechanism. The effect for an author is unchanged — nothing is silently lost, the full history is queryable — but the mechanism is now the database engine's, not application bookkeeping the programme had to maintain by hand.

The discipline is not absolute, and the one clear exception on record is itself informative: when `wa_quality_flag_types`/`wa_data_quality_flags` were repurposed on 2026-08-23 (escalation #833), their prior term-quality content — 29 flag codes, 19,866 flag rows — was hard-deleted, not soft-deleted, because that content served an analytical pipeline that no longer exists and had no live consumer to preserve continuity for. Soft-delete is the default because the programme revisits its own work and needs the trail that decision-making left behind; a hard delete is reserved for content that genuinely has no future reader, and is a decision made deliberately, not a default falling-through.

Soft-delete is not the same as set-aside, and that distinction still holds wherever the underlying mechanism survives: a row marked not-relevant to the current analytical scope is a different fact from a row marked removed from scope entirely, and a table can in principle carry both markers independently. The purpose of the whole discipline is unchanged across the architecture's evolution — continuity under revision. The programme revisits words, re-derives readings, and rebuilds mechanisms; a database that deleted rows as its understanding changed would lose the very trail that makes its current state defensible.

---

<!-- PROSE_SECTION_ID: 34 -->
<!-- PROSE_SECTION_TYPE: prog_field_authority -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Record consistency with sources -->
<!-- PROSE_SORT_ORDER: 106 -->
<!-- PROSE_VERSION: 121 -->

## Record consistency with sources

The programme's research record is still a derived record, resting on STEP Bible for lexical and verse data and on the researcher's own judgement for classification and analysis. What has changed is the mechanism that keeps the record's many surfaces consistent with those sources: the field-authority rules this section used to name (`mti_term_flags` vs. `wa_term_inventory.somatic_link`, and the `god_as_subject`/`somatic_link` error-rate caveat) named fields on tables — `mti_terms`, `wa_term_inventory` — that are now retired. They are recorded here as history, not restated as live guidance; a field-authority question about those specific columns is a question about the retained record, not about current data entry.

**Field authority, live.** The current mechanism for declaring which field wins when two overlap is `cfg_column`: every column in every table, in both databases, is required to be listed with a `use` text, and — where relevant — a `source`, an `expectation`, and a `filled_by`. `expectation` is enforced at write time (value-quality plus `enum.*` checks, part of `configmaint.validate`); `source`/`filled_by` are recorded but only checked for non-emptiness today (an informational WARN, not yet a check that the value genuinely came from what its declared source claims) — a named, open gap, not a silent one. `use` remains documentation only. Where the schema itself carries the same fact in two places across the two databases — the `cluster`, `passage`, `verse`, and `word_registry` tables each exist in both `iba.db` and `bible_research.db`, as Chapter 4 describes — the `inactive` flag on the `cfg_table` row for each copy is the authority declaration: the active copy is the one that wins, the inactive copy is retained history.

**Finding-reference consistency.** The mechanism this section previously described — `superseded_by_id`, `obsolete_reason`/`obsolete_date`, and catalogue-link preservation on `finding` and its predecessor `wa_session_b_findings` — is unchanged in its shape, but its practical weight has shifted: as Chapter 4 records, roughly 92% of `finding` rows are now soft-deleted, so a reference into this table today is, for the large majority of rows, a reference into retained history rather than into an active analytical corpus. The principle — a reference is to the finding's identity, not to its state at the moment of reference, and its meaning is read by following the chain rather than assumed fixed — still holds for whichever findings remain live.

**STEP data provenance.** STEP Bible remains the primary source for every Strong's number, gloss, meaning parse, and verse reference in the corpus. The extraction-provenance record has moved: `term_fetch_log` (2,377 rows, `bible_research.db`) is now a closed historical log, marked inactive; the live provenance record for `iba.db`'s base-data layer is the `run` table (1,871 rows) together with `cfg_connection`/`cfg_api`, which record what STEP route was called, under what configuration, and what came back — the same kind of chain the old log kept, rebuilt on the new architecture's own audit mechanism rather than a dedicated fetch-log table.

The governing principle is unchanged across all three: the record is derived, not primary, and its integrity depends on the chain from source to stored row staying traceable across every revision — including the revision that moved the mechanism itself from one database to the other.

---

<!-- PROSE_SECTION_ID: 35 -->
<!-- PROSE_SECTION_TYPE: prog_backup_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Backup and schema migration discipline -->
<!-- PROSE_SORT_ORDER: 107 -->
<!-- PROSE_VERSION: 122 -->

## Backup and schema migration discipline

The programme now runs two SQLite files, and each carries its own backup and versioning discipline, both governed by the same underlying principle: every state-changing operation is recoverable, and every schema or configuration change is traceable to a specific, dated event.

**`bible_research.db`.** `schema_version` still carries the schema's own migration history — sixteen recorded migrations at time of writing, the schema currently at `3.40.0`, each entry an M-number with a description and an applied timestamp. `apply_session_patch.py` takes a backup of the whole database before every live write — this chapter's own revision produced one (`bible_research_backup_20260827_045754_PATCH-...`), automatically, as a normal part of applying the PROSE patch, not as a separate manual step. Off-repository durability is handled outside the patch mechanism: a daily NAS backup of the database file, a daily full-project mirror, both alerting on failure.

**`iba.db`.** Configuration versioning is `cfg_meta.config_version` (currently `app-0.1.0`) rather than a `schema_version` table, and every whole-reload event is logged to `cfg_change_log`; every row-level change made through `configmaint.propose` is logged to `cfg_change_detail` — table, operation, the `where`/`set` clauses, the before-state, and when it was applied. `run.py` takes a pre-run database snapshot before every new run, wired in specifically after a 2026-07-22 incident in which a `candidate.load` bug corrupted 1,029 `candidate_seed` rows with no fine-grained rollback point available; `retention.snapshot_keep_count` (currently 5, lowered from 20 on 2026-08-21) governs how many of these snapshots are kept before the oldest is pruned. A routine or a loop that would otherwise take a snapshot on every iteration of a large batch can suppress it deliberately (`--no-backup`) where the cost of a snapshot per iteration is disproportionate to the risk — a documented exception, not a silent one.

The principle that unifies both databases' disciplines is the same one this section stated before the two-database split: a change without a recoverable prior state is a risk the programme does not accept, and a change without a record of what changed and when is a change the programme cannot later account for. What has changed is the mechanism — `apply_session_patch.py`'s pre-write backup and `schema_version`'s migration log for the research database; `run.py`'s pre-run snapshot and `cfg_change_log`/`cfg_change_detail` for the config database — not the standard both mechanisms are held to.

---

<!-- PROSE_SECTION_ID: 36 -->
<!-- PROSE_SECTION_TYPE: prog_patch_failure_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Patch and directive failure protocol -->
<!-- PROSE_SORT_ORDER: 108 -->
<!-- PROSE_VERSION: 123 -->

## Patch and directive failure protocol

Patches and directives remain the two channels by which changes reach `bible_research.db`, and the three failure modes this section named — rejection, mid-pool failure, post-application error — still describe what can go wrong with a patch there. `apply_session_patch.py`'s dry-run mode (used before every live apply, including this chapter's own) is the standing rejection check: a patch that violates a schema constraint or a controlled-vocabulary rule is caught before it ever reaches the live database, exactly as before.

`iba.db` runs a parallel but distinctly different failure protocol, built around `cfg_on_fail` rather than around patch review. Every step in the app's run sequence has a registered `(step, condition) → path` entry: `report-stop` halts the run and surfaces the failure; `pause-continue` and `report-continue` let the run proceed past a non-fatal condition while still surfacing it; `self-heal` lets a step correct a known, narrow condition on its own. Changing how a specific failure is handled is itself a config change — moving `cfg_on_fail` for a given `(step, condition)` from one path to another through `Config-Maintenance.ps1 -Step Propose` changes the app's behaviour with no code touched, and is itself subject to the same propose/approve cycle as any other rule change (see the next sub-section).

Where a failure — on either side of the split — cannot be resolved by a mechanical retry or a rejected patch, it is raised as an escalation rather than left as a comment in an obslog. An escalation raised this way carries a `resolution_kind`: `decision_required` for a genuine judgement call that must go to the researcher and stops there — it is not closed by the AI reasoning its way to an answer — or `self_correctable` for a condition the AI can fix and record, with the fix itself named in the resolution. This distinction (built 2026-08-22, escalations #798/#799) is what replaced the older, softer convention of noting a failure in a narrative log and moving on: a `decision_required` escalation is a terminal state until the researcher actually answers it, not an inline note that a subsequent pass might silently work around.

The protocol's governing principle carries forward unchanged: no failure is allowed to leave either database in an inconsistent, unrecorded state. What differs from the earlier version of this section is that the mechanism enforcing it is now split cleanly along the same line as the databases themselves — patch review and soft-delete/supersede for `bible_research.db`'s analytical content, `cfg_on_fail` routing and escalation resolution for `iba.db`'s process-control and base-data operations.

---

<!-- PROSE_SECTION_ID: 37 -->
<!-- PROSE_SECTION_TYPE: prog_instruction_override_protocol -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Instruction override and cross-document reference discipline -->
<!-- PROSE_SORT_ORDER: 109 -->
<!-- PROSE_VERSION: 124 -->

## Instruction override and cross-document reference discipline

The mechanism this section used to describe — a researcher override captured in an obslog, carried across a session boundary in a session log, and eventually authored into `wa_rule_registry` or `wa_addendum_registry` — is retired along with both of those tables. `wa_rule_registry` (59 rules, all marked obsolete 2026-08-17, superseded by the `cfg_*` system) and `wa_addendum_registry` (22 one-off audit observations from April 2026, entirely historical, all marked obsolete) are retained for provenance; neither is where a current rule change is authored.

**Instruction override, live.** The researcher's in-session direction is still authoritative, and it still does not wait on document revision to take effect — but the path it now travels is `iba\app\ps\Config-Maintenance.ps1 -Step Propose`, the one sanctioned route to changing any `cfg_*` row. A proposed change names the table, the operation, the `where`/`set` clauses, and a question stating why the change is wanted and what it affects; the command runs a coherence check (unknown table or column, a bad enum value, invalid JSON, a required field missing) before it ever reaches the researcher, then pauses and prints a run id. The researcher answers through `Escalation.ps1 -Action AnswerRun` with a genuine decision — `Approve`, `Reject`, `Revise`, `Hold`, or `Noted` — not a bare yes/no; only on `Approve` does the same Propose command, re-run against the same run id, actually commit the write, logged row-by-row to `cfg_change_detail`. An override that is approved this way is, from that point on, no longer an override — it is the rule the config holds, and every part of the app that reads that setting sees the new value immediately, with no code edit required.

For anything that is not a `cfg_*` value — a genuine open question, a discovered anomaly, a clarification needed, a piece of work assigned across a session boundary — the `escalation` table is the single project-wide mechanism, and it is explicit that this scope is not IBA-specific: "all open items, discovery of anomalies, clarifications and other forms of escalation must be recorded in escalation using escalation rules" (`governance.escalation.scope`), covering the whole project, not a subsection of it. An escalation carries a `type`, a `state` that moves through `raised` → (`re-assigned` / `on-hold` / `in-progress`) → a terminal state, a `next_action`, and — since 2026-08-22 — the `resolution_kind` (`decision_required` / `self_correctable`) described in the previous sub-section. `Escalation.ps1 -Action Raise|Update|List|History|AnswerRun` is the operational front door; `escalations_old` (723 rows) is the pre-rebuild table, retained as history after the 2026-08-16 escalation reset widened the vocabulary and made `configmaint.propose` one path among several rather than the default gate for every kind of open item.

**The `[current]` convention, retained.** The instruction corpus under `Workflow/Instructions/` still uses the `[current]` token for operational cross-references, resolving to the highest-numbered version present at read time, with specific version strings reserved for provenance — Supersedes fields, obslog entries, patch metadata. This convention was originally codified as `GR-REF-002` in `wa_rule_registry`; now that table is itself retired, the convention is defined directly in `CLAUDE.md` §10 rather than through a rule-registry row — the convention survived the retirement of the table that used to state it, because the convention was never really about the table, it was about how references resolve.

The two disciplines together now describe a cleanly split system: a `cfg_*` rule change is proposed, coherence-checked, approved by explicit decision, and committed with a full audit trail — `Config-Maintenance.ps1` end to end. A genuine open question or anomaly, anywhere in the project, is raised, tracked, and resolved through `escalation` — `Escalation.ps1` end to end. Neither mechanism defers to an obslog or a session log to carry the state across a boundary; the state lives in the database from the moment it is raised.

---

<!-- PROSE_SECTION_ID: 38 -->
<!-- PROSE_SECTION_TYPE: prog_doc_impl_alignment -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Documentation–implementation alignment -->
<!-- PROSE_SORT_ORDER: 110 -->
<!-- PROSE_VERSION: 125 -->

## Documentation–implementation alignment

The principle this section has always stated — that rules, schema, instruction documents, and prose are surfaces that drift apart unless drift is actively named and resolved, never silently tolerated — is unchanged. What is new is that the principle itself is now a config-governed rule, not only a value this chapter asserts in prose.

`governance.rules_must_be_config_driven` (`cfg_setting`, module `governance`) states it directly: no operational or process rule may exist only in `GOVERNANCE.md`, `BUILD.md`, `USER-GUIDE.md`, or memory, without a referenced `cfg_*` row recording it as the evidence that the configuration control is actually in operation; any deviation found requires an escalation. `governance.governance_md_on_rule_change` pairs it on the documentation side: a governance or process rule change must be set in `cfg_*` first, via `configmaint.propose`, and `GOVERNANCE.md` updated to reflect it in the same unit of work — the document documents the config, it never holds a rule the config does not. `governance.build_md_on_code_change` runs the equivalent check for code: any change under `iba/app/**` must update `BUILD.md`'s build record in the same unit of work.

A fourth rule closes the loop the other three depend on: `governance.past_precedent_investigation_signals_missing_config`. If running an already-registered instruction requires first reconstructing how it was done in the past — reading `BUILD.md` history, diffing archived output files, inferring a missing step from precedent — rather than a live `cfg_step`/`cfg_setting` row saying directly what to run, that investigation is itself the signal that a required config or mechanism is missing, and the correct response is to stop and close the gap, not to proceed on the reconstructed precedent and present it as the standard process. This rule was itself discovered live (an AI session about to reconstruct the Micah debate's completion step from Jonah/Joel/Obadiah's archived output, rather than reading a config row that didn't yet exist) and is the mechanism that would have caught the kind of documentation-instruction drift the earlier version of this section described in the abstract.

The two kinds of mismatch this section previously illustrated — a rule-to-schema audit gap, and documentation-to-documentation drift — still occur, and the response the four rules above prescribe is the same in shape: the mismatch is named, an escalation is raised if it isn't self-evidently a mechanical fix, and the resolution updates whichever surface was wrong, in the same unit of work, with the change recorded in `cfg_change_detail` or `BUILD.md`'s history as appropriate. What no longer happens is a mismatch being left open on the assumption that documentation will eventually catch up to practice, or practice will eventually catch up to documentation — the four governance rules above exist specifically because that assumption was tested and found to produce exactly the accumulated drift this whole chapter has had to correct.

---
