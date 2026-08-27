# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 39,40,41,42,43,44,54,55,47,67,68,50,51 -->

<!-- PROSE_SECTION_ID: 39 -->
<!-- PROSE_SECTION_TYPE: prog_instr_global_rules -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Global rules -->
<!-- PROSE_SORT_ORDER: 111 -->
<!-- PROSE_VERSION: 1194 -->

## Global rules

The programme's binding rules live in two places today, working at different levels. `CLAUDE.md`, at the project root, is the compact reference loaded into every session — file map, schema orientation, script conventions, and the standing pointers to where authoritative detail actually lives; it explicitly states that it can lag the written record and that the live config or schema wins whenever the two disagree. `iba/app/GOVERNANCE.md` is the mechanism document for `iba.db`'s rule store: how a `cfg_*` row is changed, what is enforced versus still a convention, and — from §9 onward — a dated history of every increment.

The rules themselves are `cfg_setting` (scalar rules, always attributed to a `module`), `cfg_enum` (controlled vocabularies), `cfg_behaviour_rule` paired with `cfg_behaviour_class` (six classes at present — chat, terminal, sqlite, documentation, llm_output, and development — each with its own rules for how operational behaviour in that class is expected to run), and the other `cfg_*` tables described in Chapter 5. Rules are typed, module-attributed rows, each readable and changeable through exactly one path (`Config-Maintenance.ps1 -Step Propose`, Chapter 5), and each enforced by code that reads it.

`governance.rules_must_be_config_driven` is the rule that binds every other rule: no operational or process rule may exist only in prose or in memory, without a `cfg_*` row as the evidence that it is actually governing something.

---

<!-- PROSE_SECTION_ID: 40 -->
<!-- PROSE_SECTION_TYPE: prog_instr_reference -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Reference -->
<!-- PROSE_SORT_ORDER: 112 -->
<!-- PROSE_VERSION: 1195 -->

## Reference

The programme's live reference layer is `iba.db`'s own: `cfg_enum` holds every controlled vocabulary project-wide, `cfg_column` holds every field's definition, and `iba/app/config/CONFIG-REPORT.md` is the auto-regenerated snapshot of every value in the config store — settings by module, STEP API routes, every work package's steps, the write-grant table, the schema, the enums, book order, and the change log. The report is never hand-edited; it is regenerated from the database.

Any controlled-vocabulary question is answered by pointing at this live reference rather than by restating a value inline — the concentration this achieves is what keeps a vocabulary change from requiring a document-by-document update.

---

<!-- PROSE_SECTION_ID: 41 -->
<!-- PROSE_SECTION_TYPE: prog_instr_patches -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Patches -->
<!-- PROSE_SORT_ORDER: 113 -->
<!-- PROSE_VERSION: 1196 -->

## Patches

The patch mechanism is live for `bible_research.db`: a JSON object with a `_patch_meta` header, an `operations` array of typed operations against named tables, and a `_patch_summary` footer; `scripts/apply_session_patch.py` is the applicator, run with `--dry-run` before every live application. `wa-patch-instruction-v2_11-20260507.md` is the authoritative reference document for the format.

The actively-used operation type today is `PROSE` (`insert`/`supersede`/`set_status` against `prose_section`) — the mechanism used to produce every revision in this chapter. `REPAIR` operations, for cascading resets, remain part of the format.

Patches are authored, reviewed, and applied through a three-role division — authored by the party producing the content, reviewed by the researcher, applied by the operational agent. `_patch_meta.researcher_approval` tracks the approval state on every patch, `PENDING` until it is actually reviewed. No patch reaches `bible_research.db` without passing through this format and its dry-run gate.

---

<!-- PROSE_SECTION_ID: 42 -->
<!-- PROSE_SECTION_TYPE: prog_instr_directives -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Directives -->
<!-- PROSE_SORT_ORDER: 114 -->
<!-- PROSE_VERSION: 1197 -->

## Directives

The directive mechanism is live for `bible_research.db`: a plain-language instruction with five required elements — title and identifier, what is to be done and why, the operations asked for, the expected outcome, and the confirmation to be returned — used where a change cannot be captured as a declarative patch, most often schema preparation ahead of a patch that depends on it. `wa-directive-instruction-v1_4-20260506.md` is the authoritative reference. `iba.db`'s own schema changes happen through the app's own migration scripts under `iba/app/migration/`, each recorded in `BUILD.md` in the same unit of work per `governance.build_md_on_code_change`.

Directives and patches are equal peers within their shared scope: together they are the exhaustive set of ways `bible_research.db` changes, and a directive, like a patch, does not reach the database without review.

---

<!-- PROSE_SECTION_ID: 43 -->
<!-- PROSE_SECTION_TYPE: prog_instr_claudecode -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Claude Code operating guide -->
<!-- PROSE_SORT_ORDER: 115 -->
<!-- PROSE_VERSION: 1198 -->

## Claude Code operating guide

The live operational guidance for how Claude Code works is split across a document set matched to the two-database architecture: `iba/app/GOVERNANCE.md` and `iba/app/BUILD.md` for how the base-data and process-control layer in `iba.db` runs, `iba/app/USER-GUIDE.md` as the entry point for using the app, and this chapter's own sub-sections for the patch and directive mechanisms and the prose-store operations that remain live on the `bible_research.db` side.

There is no single document today that plays a unifying role across the whole pipeline — the pipeline itself does not run as one unified thing; it is split between the two databases and their two distinct governance mechanisms.

---

<!-- PROSE_SECTION_ID: 44 -->
<!-- PROSE_SECTION_TYPE: prog_instr_registry_guide -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Registry management guide -->
<!-- PROSE_SORT_ORDER: 116 -->
<!-- PROSE_VERSION: 1199 -->

## Registry management guide

`iba.db`'s live `word_registry` is a deliberately thin table (`word`, `source`, `status`, and timestamps only), described in full in Chapter 4. It has not needed a dedicated reference guide, because it does not carry the depth of state that would call for one.

There is, at present, no live registry-management guide. This is named here as an honest gap rather than papered over: if the live registry accretes more fields as the current method matures, a guide will need writing at that point.

---

<!-- PROSE_SECTION_ID: 54 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_a -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session A — extraction -->
<!-- PROSE_SORT_ORDER: 117 -->
<!-- PROSE_VERSION: 1200 -->

## Session A — extraction and the Phase 1 data layer

The live mechanism for getting Hebrew, Greek, and Aramaic term data from STEP into a structured, addressable form is `iba.db`'s base-data layer, described in full in Chapter 4. The onboarding entry point is `iba\app\ps\New-Word.ps1`, governed by `cfg_step`/`cfg_work_package` rather than by a standalone instruction document. No single document today plays the role of a Session A instruction — the operational detail lives in the config the app reads at each step, per the mechanism Chapter 5 describes, rather than in a written procedure a reader follows by hand.

---

<!-- PROSE_SECTION_ID: 55 -->
<!-- PROSE_SECTION_TYPE: prog_instr_verse_context -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Verse Context -->
<!-- PROSE_SORT_ORDER: 118 -->
<!-- PROSE_VERSION: 1201 -->

## Verse Context

The live analytical reading of the verse corpus is the book-by-book debate pipeline described in Chapter 4: `hib`, `phenomenon`, `operation`, and `passage`'s own `debate_status` field, working at the level of a Human Inner Being within a book and a passage. Its current reach is 49 of 18,558 passages, across six books. It is governed by `cfg_step`/`cfg_setting` rows rather than by an instruction document of its own.

---

<!-- PROSE_SECTION_ID: 47 -->
<!-- PROSE_SECTION_TYPE: prog_instr_dimension_review -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Dimension Review -->
<!-- PROSE_SORT_ORDER: 119 -->
<!-- PROSE_VERSION: 1202 -->

## Dimension Review

The live analytical grouping mechanism is the cluster/characteristic model described in Chapter 4, which allocates a Strong's code directly to a cluster (`cluster_strong`) rather than assigning a label to a verse-level grouping. There is not yet an instruction document governing this allocation with the depth a dedicated method instruction would give it. The one standing rule on record is the researcher's 2026-08-13 correction that allocation must be grounded in verse-context analysis, not bulk keyword-crossmatch. Whether a fuller method instruction is written, and where, is open — named here rather than assumed.

---

<!-- PROSE_SECTION_ID: 67 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_b_readiness -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session B — Analysis Readiness -->
<!-- PROSE_SORT_ORDER: 120 -->
<!-- PROSE_VERSION: 1203 -->

## Session B — Analysis Readiness

No live process currently plays this stage's role — preparing a structured, deterministic readiness artefact ahead of an analytical session. The escalation table's own `next_action`/`resolution_kind` mechanism (Chapter 5) covers the adjacent but distinct need of tracking an open item to closure; it does not generate a per-word data-readiness report.

---

<!-- PROSE_SECTION_ID: 68 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_b_output -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session B — Analysis Output -->
<!-- PROSE_SORT_ORDER: 121 -->
<!-- PROSE_VERSION: 1204 -->

## Session B — Analysis Output

The live capture mechanisms for analytical and programme content are described in full in Chapter 4's closing sub-section: the `Prose.ps1` round trip for prose, `debate_change_detail` for the book-by-book debate writers, and the `escalation` table for judgement calls. No registry is currently progressing through a per-word analytical output stage of the kind this section's heading names.

---

<!-- PROSE_SECTION_ID: 50 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_c -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session C -->
<!-- PROSE_SORT_ORDER: 122 -->
<!-- PROSE_VERSION: 1205 -->

## Session C

The live reader-facing narrative mechanism is not word-driven: the book-by-book debate pipeline's `passage.story_summary` field, populated for the passages that have reached `filled`/`complete` debate status across the six books named in Chapter 4, is a book-driven narrative account. The programme currently has no mechanism producing a per-word reader-facing document; whether that need is picked up again, and in what form, is unresolved.

---

<!-- PROSE_SECTION_ID: 51 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_d -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session D -->
<!-- PROSE_SORT_ORDER: 123 -->
<!-- PROSE_VERSION: 1206 -->

## Session D

Cross-registry synthesis has never executed as its own run: the relevant run/observation tables hold zero rows, exactly as Chapter 4's synthesis-bridge sub-section records. The material that would feed such a run — the SD pointer accumulation described in Chapter 4 — continues to build. Whether a dedicated synthesis run executes as originally designed, or whether the cluster/characteristic model comes to do this work in a different shape entirely, is the open question Chapter 4 leaves unresolved and this section does not re-litigate.

---
