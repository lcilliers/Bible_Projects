# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 39,40,41,42,43,44,54,55,47,67,68,50,51 -->

<!-- PROSE_SECTION_ID: 39 -->
<!-- PROSE_SECTION_TYPE: prog_instr_global_rules -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Global rules -->
<!-- PROSE_SORT_ORDER: 111 -->
<!-- PROSE_VERSION: 1228 -->

## Global rules

The programme's binding rules are rows of the configuration store in `iba.db`, and they live nowhere else. `CLAUDE.md` at the project root is a pointer file: it holds no rules, no state and no history, and where it and a rule's home disagree, the home wins. `iba/app/GOVERNANCE.md` is the mechanism document for the rule store: how a `cfg_*` row is changed, what is enforced and what is still a convention. The control map (`cfg_control_home`) names the one home of each kind of content.

The rules are `cfg_setting` (scalar rules, each attributed to a module), `cfg_enum` (controlled vocabularies), `cfg_behaviour_rule` with `cfg_behaviour_class` (the classes chat, terminal, sqlite, documentation, filing, llm_output, development and study_method, each with its own rules for how operational behaviour in that class is expected to run), the escalation rules, and the other `cfg_*` tables described in Chapter 5. Each rule is a typed row, readable and changeable through exactly one path (`Config-Maintenance.ps1 -Step Propose`, or a logged migration in a Developer Mode session), and enforced by code that reads it.

A session starts with `/start-project`, which prints every general rule and has Claude restate each in the session's compliance file. The other rules reach Claude at the first use of the operation they govern, so that a rule is read when it is needed. `governance.rules_must_be_config_driven` binds every other rule: no operational or process rule may exist only in prose or in memory, without a `cfg_*` row as the evidence that it governs something.

---

<!-- PROSE_SECTION_ID: 40 -->
<!-- PROSE_SECTION_TYPE: prog_instr_reference -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Reference -->
<!-- PROSE_SORT_ORDER: 112 -->
<!-- PROSE_VERSION: 1229 -->

## Reference

The programme's live reference layer is `iba.db`'s own: `cfg_enum` holds every controlled vocabulary project-wide, `cfg_column` holds every field's definition, and `iba/app/config/CONFIG-REPORT.md` is the auto-regenerated snapshot of every value in the config store — settings by module, STEP API routes, every work package's steps, the write-grant table, the schema, the enums, book order, and the change log. The report is never hand-edited; it is regenerated from the database.

Any controlled-vocabulary question is answered by pointing at this live reference rather than by restating a value inline — the concentration this achieves is what keeps a vocabulary change from requiring a document-by-document update.

---

<!-- PROSE_SECTION_ID: 41 -->
<!-- PROSE_SECTION_TYPE: prog_instr_patches -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Patches -->
<!-- PROSE_SORT_ORDER: 113 -->
<!-- PROSE_VERSION: 1230 -->

## Patches

The patch mechanism is live for `bible_research.db`: a JSON object with a `_patch_meta` header, an `operations` array of typed operations against named tables, and a `_patch_summary` footer. `scripts/apply_session_patch.py` is the applicator and is run as a dry run before every live application. The format reference is held in the archived instruction document `Workflow/Instructions/archive/wa-patch-instruction-v2_11-20260507.md`.

The operation type in use is `PROSE` (insert, supersede and set_status against `prose_section`), the mechanism by which every revision of the programme prose and the glossary is made; `Prose.ps1 -Step ApplyPatch` applies a reviewed patch in one transaction or not at all. `REPAIR` operations, for cascading resets, remain part of the format.

Patches are authored, reviewed and applied in distinct steps: authored by Claude, reviewed by the researcher where review is warranted, and applied by the app. `_patch_meta.researcher_approval` tracks the approval state, pending until it is reviewed. No patch reaches `bible_research.db` without passing through this format and its dry-run gate.

---

<!-- PROSE_SECTION_ID: 42 -->
<!-- PROSE_SECTION_TYPE: prog_instr_directives -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Directives -->
<!-- PROSE_SORT_ORDER: 114 -->
<!-- PROSE_VERSION: 1231 -->

## Directives

The directive mechanism is live for `bible_research.db`: a plain-language instruction with five required elements (a title and identifier, what is to be done and why, the operations asked for, the expected outcome, and the confirmation to be returned), used where a change cannot be captured as a declarative patch, most often schema preparation ahead of a patch that depends on it. The format reference is held in the archived instruction document `Workflow/Instructions/archive/wa-directive-instruction-v1_4-20260506.md`. The schema of `iba.db` changes through the app's own migration scripts under `iba/app/migration/`, each recorded in `BUILD.md` in the same unit of work (`governance.build_md_on_code_change`).

Directives and patches are equal peers within their shared scope: together they are the exhaustive set of ways `bible_research.db` changes, and a directive, like a patch, does not reach the database without review.

---

<!-- PROSE_SECTION_ID: 43 -->
<!-- PROSE_SECTION_TYPE: prog_instr_claudecode -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Claude Code operating guide -->
<!-- PROSE_SORT_ORDER: 115 -->
<!-- PROSE_VERSION: 1232 -->

## Claude Code operating guide

The operational guidance for how Claude Code works is held in the application and its documents. `/start-project` and `Start-Iba.ps1` check the configuration, the data and the STEP connection, report how the last session ended, and print the general rules; the point-of-use rules deliver every other rule when an operation is first used; and `/session-close` checks and records the end of a session. `iba/app/USER-GUIDE.md` is the entry point for using each tool of the app, `iba/app/GOVERNANCE.md` explains how configuration governs the code, `iba/app/BUILD.md` records what changed and why and is read only to assess a past state, and `iba/app/CHARTER.md` states what the app is for. This chapter holds the patch and directive mechanisms and the prose-store operations of the `bible_research.db` side.

These do the work of a single operating guide. The rules are not held in a document that can lag: they are configuration rows that print at the start of a session and arrive at the point of use, and the documents point to them.

---

<!-- PROSE_SECTION_ID: 44 -->
<!-- PROSE_SECTION_TYPE: prog_instr_registry_guide -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Registry management guide -->
<!-- PROSE_SORT_ORDER: 116 -->
<!-- PROSE_VERSION: 1233 -->

## Registry management guide

`iba.db`'s `word_registry` is a deliberately thin table (the word, its source, its status and timestamps), described in Chapter 4. It is the entry point for onboarding a new word of the base data and has not needed a dedicated reference guide, because it does not carry the depth of state that would call for one. The scope of the study is held in the surface and collection tables, whose procedures are in the sections that follow and in `iba/app/USER-GUIDE.md`.

There is, at present, no registry-management guide. This is named as a gap and not papered over: if the registry accretes more fields as the method matures, a guide will need writing at that point.

---

<!-- PROSE_SECTION_ID: 54 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_a -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Session A — extraction -->
<!-- PROSE_SORT_ORDER: 117 -->
<!-- PROSE_VERSION: 1234 -->

## Base data

The mechanism for getting Hebrew, Greek and Aramaic word data from STEP into a structured, addressable form is the base-data layer of `iba.db`, described in Chapter 4. The entry point for a new word is `iba\app\ps\New-Word.ps1`, governed by `cfg_step` and `cfg_work_package`, and the mechanical reading of each verse is built by the lexical build of the app. The operational detail lives in the configuration the app reads at each step, per the mechanism Chapter 5 describes, and not in a written procedure a reader follows by hand.

---

<!-- PROSE_SECTION_ID: 55 -->
<!-- PROSE_SECTION_TYPE: prog_instr_verse_context -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Verse Context -->
<!-- PROSE_SORT_ORDER: 118 -->
<!-- PROSE_VERSION: 1273 -->

## The collection reading

The collection is read through the layered reading, run with `Collection-Build.ps1` (`LayerOpen`, `LayerPull`, `LayerRecord` and `LayerCheck`) over the steps and items of `cfg_setting layer.reading`. A step is opened only when the previous one is closed; the lexical analysis of the words (step S1) closes before the grouping of the surfaces is read, and the grouping is finished before the steps that follow. The rows each step demands are the ledger `collection_layer_item`, derived from the data, and each is answered by an observation with its nodes or by a recorded none with its reason. The stages and steps are described in Chapter 2, and the rules that govern them are configuration rows, delivered at the first use of the routine. The evidence on which a collection is read, its member occurrences, its sense and its pairings, is produced by the collection evidence report from the tables.

---

<!-- PROSE_SECTION_ID: 47 -->
<!-- PROSE_SECTION_TYPE: prog_instr_dimension_review -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Dimension Review -->
<!-- PROSE_SORT_ORDER: 119 -->
<!-- PROSE_VERSION: 1274 -->

## The grouping of the surfaces

The grouping of the surfaces of a collection is run with `Collection-Build.ps1`: `Index` fills the index of the member surfaces, `GroupPull` writes the working file with the evidence of each surface (its Strong's codes with their lexicon evidence, its occurrences and its link), `GroupRecord` validates the whole file and writes the groups and placements in one transaction with a scrutiny report for the researcher, and `Subgroup` makes the researcher's corrections, each with its reason. The method rules are in the configuration. The surfaces are first sorted and gathered into collections by the surface cycle of five modules (Chapter 4), whose map is generated into the configuration report. A change to the collections is made class by class, tried on a copy under a named snapshot, with the counts predicted and checked, and with every change kept in `surface_event`. The procedures are in `iba/app/USER-GUIDE.md` and the rules in `GOVERNANCE.md` and the configuration.

---

<!-- PROSE_SECTION_ID: 67 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_b_readiness -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Session B — Analysis Readiness -->
<!-- PROSE_SORT_ORDER: 120 -->
<!-- PROSE_VERSION: 1237 -->

## Readiness of a step

A step of the reading is made ready by its opening: `LayerOpen` refuses until the previous step is closed and the grouping is finished, and then derives from the data the rows the step demands. `LayerPull` writes the working file of the open rows, each with its evidence and an empty place to fill. The escalation table's `next_action` and `resolution_kind` mechanism (Chapter 5) covers the adjacent but distinct need of tracking an open item to closure.

---

<!-- PROSE_SECTION_ID: 68 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_b_output -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Session B — Analysis Output -->
<!-- PROSE_SORT_ORDER: 121 -->
<!-- PROSE_VERSION: 1275 -->

## Recording observations

The reading's output is the observation, written directly to the database and not assembled into a separate document. `LayerRecord` checks the whole file (a problem anywhere refuses all) and writes the observations, their nodes and the ledger answers in one transaction; `LayerCheck` validates each answered row against the tables and writes a versioned report naming the gates, what is open and what failed. Each observation states what the dictionary, the verses and the stored structure show (Chapter 2). The other capture mechanisms are those of the last section of Chapter 4: the `Prose.ps1` round trip for prose, and the `escalation` table for judgement calls.

---

<!-- PROSE_SECTION_ID: 50 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_c -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Session C -->
<!-- PROSE_SORT_ORDER: 122 -->
<!-- PROSE_VERSION: 1239 -->

## The narrative

The reader-facing output is the narrative of the inner being, held in the database as chapters and sections and built by collection (Chapter 4). Claims are told in it, each with its sources. The narrative is exported from the database, and the export is copied to the inbox of the researcher's publishing site by `Copy-NarrativeToLearning4Comfort.ps1`; there is no direct publishing to GitHub. External publication decisions are outside the programme's method. The cross-linking of the existing claims to the collections, and the update of the narrative to follow them, is part of the claim formulation of stage 5.

---

<!-- PROSE_SECTION_ID: 51 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_d -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Instruction corpus -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_SECTION_TITLE: Programme — Session D -->
<!-- PROSE_SORT_ORDER: 123 -->
<!-- PROSE_VERSION: 1276 -->

## Claims and synthesis across collections

Synthesis across collections, the relations between the words and concepts of the inner being as a whole, is found in the observations of the collections and in the claims formulated from them. The inner-being analysis made from the verse-lexical observations (stage 4) and the formulation of claims (stage 5) are still being defined; they are named here as deferred and not built. The study does not carry a separate synthesis process alongside them.

---

