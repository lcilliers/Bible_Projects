# #2268 Config inventory: the analytic process, start to finish (v3)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** inventory only, read from the live `cfg_*` tables of `iba/app/db/iba.db` (read-only). Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"I am sorry, but you need to first assemble all the configs that is pertinent to the end to end scope of the analytic process from start to finish"*.


**v3.** Researcher, chat 2026-10-24 (verbatim): *"read my feedback on R1 - R3 in rulings review v1 and take that on board. … after you have adjusted the analytic process and the file changes following from that."* The stages are now the phases of `outputs/escalation/2268-analytic-process-and-reading-plan-v1-20261024.md`: FRAME, 0.B, 0.C, 0.GAP (pre-claims and post-claims), D1, D2, D3, D4 (verses in context, from observations to narration), PUBLISH, with the observation RECORD and the open ITEMS across all, and the RETIRED passage method kept for its rules. v2 is in `outputs/escalation/archive/`.

**How this was made.** A one-off read-only script wrote this file from the tables. The only hand-made part is which stage each step, rule, setting and enum belongs to (section 0). Every text below is the row's own text. For each rule the file states how it is delivered (`cfg_rule_scope`) and whether that delivery reaches the stage's own tools; that column is computed, not judged.

**Contents.** 0 The stages · one section per stage · H Authorities held in documents · I Config tables not included, and why · Appendix 1 Rule texts · Appendix 2 Method rules and quality checks in full · Appendix 3 Field meanings of the tables the stages write

## 0. The stages

| Stage | What it covers | Steps | PS tools |
|---|---|---|---|
| **FRAME** Frame: purpose, governing settings and where things live (not a phase) | What the analysis is for, its state, and where its parts live. | 0 | - |
| **0.B** 0.B Base data: outside the analytic rule set; read only in 0.C and 0.GAP | Verses, spans, Strong's codes, meanings and clusters, built in the Base_data stage. Missing or poor base data is a gap routed to its recovery process (RO4). | 22 | Cluster-Assign.ps1, Cluster-Report.ps1, Lexicon-Parse.ps1, New-Word.ps1, Raw-Backfill.ps1, Spine-Check.ps1, StrongMeaning-Report.ps1, StrongVerse-Report.ps1, VerseLexical.ps1 |
| **0.C** 0.C Scope: a collection of verses for a stated purpose; a cluster segmented, not read whole | The scope of a reading and its purpose; base data read only to assess it. | 4 | Escalation.ps1, Open-Item.ps1, Reading.ps1, Verse-Scope.ps1 |
| **0.GAP** 0.GAP Gap discovery and gap analysis: pre-claims (before D1) and post-claims (inside D4's claim step) | Across all tables for the scope, at quality depth, without verse text: what is there, what should be there, its quality; work already done gathered; gaps written and kept current. | 15 | Cluster-Assign.ps1, Escalation.ps1, Narrative-Register.ps1, Open-Item.ps1, Reading-Index.ps1, Reading.ps1, Spine-Check.ps1, StrongMeaning-Report.ps1, Verse-Collate.ps1, VerseLexical.ps1, VerseMeta.ps1 |
| **D1** D1 Word level: Stage 1 (lexical.meaning, lexical.relational); table data only | Each word's meaning and form in its occurrences, settled once so D4 does not re-derive it. | 2 | VerseLexical.ps1 |
| **D2** D2 Characteristics: clusters, subgroups, characteristics, open items; table data only | The characteristics the scope bears on, and how its words group. | 4 | ClusterSubgroup.ps1, Open-Item.ps1 |
| **D3** D3 Claims and characteristics: the claims already resting on the scope; table data only | What is already claimed, read against the characteristics, so D4 tests it rather than re-claims it. | 2 | Narrative-Register.ps1 |
| **D4** D4 Verses in context: observe, then claims (with 0.GAP post-claims), then narrate | The only phase that reads verse text and passage: each verse read in its passage (the role guide), then observations carried into claims, then the narrative told from the claims. | 11 | Narrative-Register.ps1, Reading.ps1 |
| **PUBLISH** Publish: the touched chapters published; the chapter structure; the programme prose | The narrative published from the database and copied out; chapters kept through the register; the researcher's programme prose. | 12 | Narrative-Register.ps1, Prose.ps1, Reading.ps1 |
| **RECORD** The observation record across D1 to D4 (not a phase): ib_observation, ib_node, the enhancer, the question catalogue | Every phase that writes, grounds, corrects, enhances or disposes of an observation, and what the record holds. | 11 | Catalogue-Report.ps1, Catalogue-Update.ps1, ClusterSubgroup.ps1, Observation-Enhancer.ps1, Reading.ps1, VerseLexical.ps1 |
| **ITEMS** Open items and threads, across every phase | What a reading leaves to be read elsewhere, how it is registered, and when it comes back. | 5 | Open-Item.ps1 |
| **RETIRED** Retired route: the passage method (hib.set to closing.set); its rules to be gathered into D4 | Retired per the R3 feedback; reading passages in context is part of D4. Its method rules and quality checks are listed so that what still holds can be carried over. | 7 | Build-Passages.ps1, Operations-Ingest.ps1, Passage-Quality.ps1, WholeBookRead-Report.ps1 |

Each phase reads only what §4 of the process file assigns it: verse text and passage in D4 only; base data in 0.C and 0.GAP only; D1 to D3 table data only (rules RO1 to RO9 there). No config row yet holds the phases, their order or what each reads (overlay P32).

### 0.1 What reaches each stage (computed)

| Stage | Rules placed | Reach the stage's own tools | Only at session start | Not delivered to the stage | Method rules (never delivered) | Quality checks (never delivered) |
|---|---|---|---|---|---|---|
| FRAME | 7 | 0 | 4 | 3 | 0 | 0 |
| 0.B | 7 | 4 | 0 | 3 | 8 | 0 |
| 0.C | 7 | 3 | 0 | 4 | 0 | 0 |
| 0.GAP | 10 | 4 | 2 | 4 | 2 | 0 |
| D1 | 7 | 4 | 1 | 2 | 23 | 0 |
| D2 | 9 | 2 | 1 | 6 | 32 | 0 |
| D3 | 4 | 2 | 1 | 1 | 0 | 0 |
| D4 | 22 | 5 | 2 | 15 | 0 | 0 |
| PUBLISH | 5 | 5 | 0 | 0 | 0 | 0 |
| RECORD | 8 | 2 | 1 | 5 | 55 | 0 |
| ITEMS | 10 | 1 | 4 | 5 | 0 | 0 |
| RETIRED | 3 | 0 | 1 | 2 | 37 | 18 |

A rule "not delivered" here is scoped only to paths (mostly `_analytics/**`) or commands that the stage's tools never touch. The first stage (A, now FRAME) has no tools of its own. `cfg_rule_scope` holds no reference to any method rule, so none of the method rules or quality checks is delivered to the session at any point. Some are enforced in the code instead; appendix 2 gives each one's `enforced_by`, and marks those with none.

## FRAME. Frame: purpose, governing settings and where things live (not a phase)

What the analysis is for, its state, and where its parts live.

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

**None.** No method rule or quality check is tied to any step of this stage.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:84 | fan-out-progressive-strands | study_active | path:_analytics/** | **no** |
| B:4 | inferential-not-confirmed | always | general:* | only at session start (general) |
| B:19 | factual-discipline-no-guessing | always | general:* | only at session start (general) |
| B:34 | source-of-truth-is-written-record | always | general:* | only at session start (general) |
| B:61 | inactive-tables-never-active-inputs | always | command:sqlite | **no** |
| B:67 | bible-research-db-excluded-from-iba-results | always | command:sqlite | **no** |
| B:83 | authoritative-source-only | always | general:* | only at session start (general) |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `governance.study_status` | "ACTIVE since 2026-10-23. Researcher, verbatim: 'I will be returning to standard mode and restart the study, so you can release the hold on the study, then do a session-close'. Study work (readings, weaves, audits) is done through the reading process: iba/app/ps/Reading.ps1 (Open, Record, Check, Synergy, Apply, Publish, Account; escalation #2228), a reading of one scope through three gates (recorded, synergised, published), with the narrative in iba.db (governance.narrative_home). The strand steps are retired (#2228 D-a)." | Whether the study is active or on hold, and why. Read at session start (module governance). Changed only on the researcher's instruction. Moved from the CLAUDE.md banner 2026-10-21 (escalation #2181). |
| `behaviour.study_state` | "active" | The study's state flag (cfg_enum study_state): 'active' delivers the study_active rules at start; 'on_hold' withholds them. Set only on the researcher's instruction; the ruling and reason are in governance.study_status. Escalation #2185. |
| `governance.programme_stages` | "The research programme has three main stages: Base_data (STEP through lexical); Analysis (deriving understanding of the inner being); Publishing (essays and output for the results). Previously referred to as Session A (base data), Session B/D (analytics), Session C (publishing) -- methodologies and processes have changed materially over time across all three." |  |
| `governance.prose_canonical_authority` | "The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about. cfg_prose_concept points a key project concept (e.g. verse primacy, the inner-being definition) at the prose section that defines it, rather than restating the definition as a separate rule. Chapter-level review status is not tracked in cfg_*: it lives in prose_section.status (cfg_enum prose_section_status), set per section via Prose.ps1 -Step SetStatus, rolled up per chapter via prose_section_type.chapter_no. A methodology/approach change that touches a concept named in cfg_prose_concept should flag whether the prose needs updating (the flagging mechanism is a deferred build; this setting states the principle only)." | entry-point anchor for the prose-as-canonical-authority work -- part (a) of escalation #714 |
| `governance.scope_project` | "the config's scope is the entire project, with all of its parts, not a sub-section of the project" |  |
| `governance.scope_iba_app` | "IBA App is the central process control mechanism for all operations in the entire project" |  |
| `governance.scope_iba_db` | "The iba_db is the home for all project process control and base data, including all related tables from STEP through Strongs, verses, meaning, and lexicals. It is now primary for all processes and base data; a few analysis tables (debate/passage control) are expected to migrate back to research_db." |  |
| `governance.scope_research_db` | "bible_research.db (research_db) is prose-only -- the canonical, foundational authority on the programme's own governing concepts (governance.prose_canonical_authority). Findings/observations are fully owned by iba.db's ib_observation/ib_node pipeline; the old finding/analysis/legacy-cluster tables in bible_research.db are inactive, not a live parallel store." |  |
| `governance.project_databases` | "bible_research.db (aka research_db) lives in database/; iba.db lives in iba/app/db/ -- both paths are project-root-relative" |  |
| `governance.rules_must_be_config_driven` | "no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or memory without a referenced cfg_* row recording it as the evidence that the configuration control is in operation. Any deviation discovered requires escalation. On a new instruction, the first thing to establish is that the rules governing the instruction are fully captured and interpreted correctly in the configs -- if not, it requires escalation." | the researchers 2026-07-26 standard, raised after an unconfigured rule (STEP required) was silently violated |
| `governance.past_precedent_investigation_signals_missing_config` | "If executing an already-registered standard instruction (a cfg_work_package/cfg_step routine) requires FIRST INVESTIGATING HOW IT WAS DONE IN THE PAST -- reading BUILD.md/session-log history, diffing prior/archived output files, or otherwise reverse-engineering a missing step from precedent -- rather than being told directly by a live cfg_step/cfg_setting row what to run and what rules apply, that investigation is itself the signal that a required config/mechanism is MISSING, not a puzzle to solve from precedent. STOP the instruction immediately the moment this is recognised -- do not proceed by reconstructing the missing rule from historical output and presenting it as the standard process. The gap must be closed first: the missing step/setting registered in cfg_* and its code built (governance.build_md_on_code_change/governance.governance_md_on_rule_change both apply), config validated clean, and only then may the original instruction be resubmitted." | researcher ruling 2026-07-30: a live session investigated BUILD.md history and archived output files to infer an undocumented passage.debate_status filled transition (report.passage_debate has no registered mechanism for marking a manually-filled scaffold complete) instead of finding that transition in cfg_step/cfg_setting -- doc/output archaeology substituting for a missing config is exactly the inconsistency pattern blamed for this study lacking repeatable results over its 7-month history |
| `governance.narrative_home` | "The inner-being narrative is kept in iba.db with its claims: each chapter as blocks (narrative_section.block_text, a heading and its text) and each claim told by a block (narrative_claim_telling). The chapter files in narrative.copy_source_dir are exports written from the database; the narrative is written through Reading.ps1 -Step Apply and the block actions of Narrative-Register.ps1, never in a chapter file. bible_research.db prose_section keeps the programme and glossary prose, which stay live." | researcher 2026-10-22 on escalation #2172 (reading process design v2, option B, approved: "sounds good to proceed with the build"; prose_section's programme and glossary prose are not dead) |
| `governance.project_operations` | "A project operation is any activity to perform research, development, exploration, investigation, or running scripts related to achieving the project objectives." |  |
| `governance.project_change_rule` | "Any change of operations, methodologies or approach must channel through the IBA App. Any operation defined in the past that is not in the IBA app must be migrated to the app." |  |
| `governance.primary_responsibility` | "Claude is responsible for the coding of, and maintenance of the integrity to ensure that all project operations are coded, controlled and maintained in the IBA application. This includes back-filling operations currently outside the application." |  |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `study_state` | active, on_hold |
| `behaviour_rule_deliver_when` | always, study_active, developer_mode |

### Governing concepts (`cfg_prose_concept`)

- **verse_primacy** (chapter 1; wa_rule_registry GR-PROG-001; escalation #714): The verse is the primary unit of evidence; findings and dimensions emerge from verse evidence, never bent to fit a pre-existing category. Direct successor of wa_rule_registry GR-PROG-001 (obsolete 2026-08-17) -- this pointer replaces the rule's own restated text.
- **inner_being_definition** (chapter 1; wa_rule_registry GR-PROG-002 (superseded); escalation #714): The programme's governing question: what does Scripture reveal about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body)? Supersedes wa_rule_registry GR-PROG-002 (obsolete 2026-08-17) per researcher decision 2026-08-18 -- GR-PROG-002 is retired as a rule; this pointer to the prose is now the canonical reference, not a restated rule text.

### Where each kind of study content lives (`cfg_control_home`)

| Kind | Home type | Home | Description | Read when | History home |
|---|---|---|---|---|---|
| study_method | folder | Workflow/Instructions/ -- one live file per subject, named by a cfg_setting path | How study work is done (reading, weaving, writing). Rules drawn from a method file live in cfg_behaviour_rule; the file explains, it does not restate. | when_needed | Workflow/Instructions/archive/ |
| study_state | db_table | escalation (strand escalations and type=thread items), narrative_chapter, the narrative claim register tables, the narrative's blocks (narrative_section.block_text; governance.narrative_home), the reading_strand tables | Where the study stands: strands, what is read, woven, held or forwarded, the chapters and their claims. Not held in CLAUDE.md or memory. | when_needed | escalation_history; the register's change records |
| study_output | folder | _analytics/ (cluster folders per report.cluster_folder_naming_convention; the exported narrative chapters in _analytics/essay/spirit_soul_body/inner-being-narrative/); outputs/strand-reading/ (each strand's context, gather and account files) | The study's working files, and the narrative chapters as exported from iba.db (governance.narrative_home). | when_needed | each folder's archive/ |
| researcher_ruling | db_table | escalation_history (the comment on the escalation the ruling answers) | The researcher's decisions, verbatim. A rule that results goes to its cfg row, with the ruling in that row's source. | when_needed | escalation_history is itself history |
| open_item | db_table | escalation | Every open item, task, issue, decision or thread (rule 40). No other task ledger. | session_start | escalation_history |

### What the rows above do not show

- **B:84 is to be retired and replaced by proper configs (R2).** Its content stays listed here until the replacement is designed.

## 0.B. 0.B Base data: outside the analytic rule set; read only in 0.C and 0.GAP

Verses, spans, Strong's codes, meanings and clusters, built in the Base_data stage. Missing or poor base data is a gap routed to its recovery process (RO4).

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `registry.exists` | new-word / New-Word.ps1 | stop if the word already exists (a refresh run handles that) | - | word-exists: terminal |
| `registry.create` | new-word / New-Word.ps1 | create the word, status proposed->approved | word_registry (iba) | needs-approval: terminal; word-rejected: terminal |
| `raw.discover` | new-word / New-Word.ps1 | CALL 1 meanings= -> word_strong (the seed strongs) | - | zero-strongs: terminal; follow-related-not-built: terminal |
| `raw.detail` | new-word / New-Word.ps1 | CALL 2 getInfo per strong -> strong + sense + tree + lexicon (the meaning) | - | no-vocab: terminal |
| `raw.verses` | new-word / New-Word.ps1 | CALL 3 per strong -> strong_verse + verse + span (span parsed from preview) | - | shortfall: terminal |
| `raw.write` | new-word / New-Word.ps1 | commit; mark raw-complete | word_registry (iba) | - |
| `raw.validate` | new-word / New-Word.ps1 | the parse-check: span vs strong_verse must agree | validation_result (iba) | parse-mismatch: terminal |
| `strong.reconcile` | new-word / New-Word.ps1 | Cluster-classify and, where warranted, promote every one of the word's own codes (lib.strongreconcile.reconcile() per code) -- runs last, after raw.validate, so verses/spans are already validated before classification. Point (c), backfill-cluster-triage-plan-v3-20260812.md: new-word must complete through verse_lexical for qualifying strongs. UPDATED 2026-09-15 (escalation #1606): fails (condition='unclassified') if any of the word's own codes got no cluster assignment at all, rather than always returning ok() -- an automatic classification attempt runs on every code either way, but a failed attempt is now surfaced, not silently absorbed. | strong (iba) | unclassified: terminal |
| `raw.backfill_meaning` | raw-backfill / Raw-Backfill.ps1 | for a book (optionally narrowed to one chapter's verse range via -Range C:V-V), find every distinct strong its spans reference that has no strong row yet, and pull ONLY the meaning (STEP getInfo -> strong/strong_sense/strong_meaning_tree/strong_lexicon) -- not verses. Reuses raw.detail_one() unchanged. Progressive, passage-driven DB coverage growth, not a full-Bible bulk pull. Cluster-reconciles every newly-backfilled code inline (the only chain these codes ever pass through). UPDATED 2026-09-15 (escalation #1606): fails (condition='unclassified') if any newly-backfilled code got no cluster assignment at all, rather than always returning ok(). | - | unreachable: terminal; invalid-range: terminal; unclassified: terminal |
| `lexicon.related` | lexicon-parse / Lexicon-Parse.ps1 | strong -> strong_related; one live STEP getInfo call per row (relatedNos) | strong_related (iba) | unreachable: terminal |
| `lexicon.validate` | lexicon-parse / Lexicon-Parse.ps1 | read-only coverage + value-quality check across all 4 tables; persists lexicon.quality_report_path every run; escalates only if findings exist | - | findings-rejected: terminal; needs-review: terminal; needs-revision: terminal |
| `lexical.readiness` | verse-lexical / VerseLexical.ps1 | 3-leg read-only precondition check for the Layer 1 rebuild (#1606): Leg1 every live verse has >=1 live span; Leg2 every live span's strong_variant code resolves to a live strong row (duplicates spine.check's own desync check deliberately -- #1606's own framing is one cohesive 3-leg check); Leg3 every live strong that actually occurs in a live span has >=1 live cluster_strong allocation (the precondition Layer 1's redesigned role column, a JSON array of cluster_strong.cluster_code, depends on directly). Persists a report every run (governance.reports_must_persist), fails on any FATAL finding. | - | - |
| `lexical.build` | verse-lexical / VerseLexical.ps1 | verse : verse_lexical extract — mechanical T1-T3 engine: for every code in a span's (possibly compound) strong_variant, classifies role (content lexical entry vs. grammatical formative), stem/voice-selects the operative sense from strong_meaning_parsed via morph_code (not the whole six-stem/voice paradigm), and flags — never resolves — the sibling/base-fallback ambiguity case versespanmeaningreport.meaning_for_code already detects. Runs independent of T4-T9/passage_debate. Version-aware: soft-deletes the superseded row and inserts fresh on rewrite, same convention every other iba.db table already uses. Replaces report.verse_span_meaning (retired, see BUILD.md).; from this build onward, also denormalizes position/surface/language/testament and computes is_negator/narrative_morph/gloss_consistent_in_verse/party_kind via cfg_lexical_code_class lookups, unconditionally for every row, no selection (method-and-drift-mitigation doc §2 Layer 1). Also applies the H0853 classify_role exception (design doc §4). | verse_lexical (iba) | unreachable: terminal |
| `report.verse_lexical` | verse-lexical / VerseLexical.ps1 | on-demand MD report, generated from verse_lexical (never an independent write) — EV verse text and the resolved lexical reading placed together, per book/passage range. Requires verse_lexical.build to have already run for this exact range. | - | no-readings: terminal |
| `report.lexical_exceptions` | verse-lexical / VerseLexical.ps1 | Per-run exception report — every unresolved/unclassified/checked_empty/UNCLASSIFIED-connective disposition and every genuine judgement call from the most recent lexical.enrich run for this passage, laid out for researcher review. Read-only against verse_lexical/verse_lexical_note, never an independent write. | - | - |
| `report.lexical_extract` | verse-lexical / VerseLexical.ps1 | Multi-filter JSON extract over verse_lexical/verse_lexical_note — passage/verse/surface/strong/lemma filters, each accepting a list or range. Read-only, JSON output, feeds Phase 2 (Stage 2) input assembly. | - | - |
| `cluster.assign` | cluster-assign / Cluster-Assign.ps1 | DB-wide sweep: lib.strongreconcile.reconcile() per strong — mechanical HIGH-precedent classification + backfill-to-word promotion cascade where warranted. No network beyond what a promotion cascade itself needs (a real STEP verse fetch). | cluster_strong (iba) | - |
| `cluster.validate` | cluster-assign / Cluster-Assign.ps1 | Read-only DB-wide coverage + exception report: unclassified strongs, backfill non-T2 not yet promoted, and the two named exception shapes (cluster with no word; backfill with an already-active/clustered sibling). Persists a report every run. UPDATED 2026-09-15 (escalation #1606): escalates if EITHER an unclassified strong exists OR either named exception shape exists -- previously only escalated on the two named exception shapes, leaving a plain unclassified count unescalated indefinitely. UPDATED 2026-09-15 (escalation #1707): before escalating, checks whether the current findings already fall within a PRIOR run's approved baseline (escalation.answered_baseline_for_step, cross-run, not just this run) -- a known, already-signed-off backlog is acknowledged automatically instead of raising a fresh escalation every run; a genuine increase in any count still escalates. | - | needs-review: terminal; findings-rejected: terminal; needs-revision: terminal |
| `spine.check` | spine-check / Spine-Check.ps1 | read-only check of the base-data spine (governance.base_data_spine): span -> strong, verse <-> span, strong -> cluster, and strong -> meaning (strong_sense, strong_meaning_tree, strong_lexicon; each local gap asked of STEP: content in STEP that the table lacks is FATAL, nothing in STEP is a gap by design). Persists a report every run; escalates only on a FATAL finding. Run by session-close (SC2), not at start (#2173 P3). The parse tables stay retired. See handlers/spine.py. | - | spine-fatal-rejected: terminal; spine-fatal-found: terminal; needs-revision: terminal |
| `report.strong_meaning` | strong-meaning-report / StrongMeaning-Report.ps1 | meaning-parse layer coverage — strong/strong_sense/strong_meaning_tree/strong_lexicon gap list, sense-count distribution, lexicon completeness | - | - |
| `report.strong_verse` | strong-verse-report / StrongVerse-Report.ps1 | on-demand verse restatement for one Strongs reference (verse_lexical.strong exact match, whole Bible) in the context of a registry word -- inline-annotated, exact-variant senses only, combined-tag/empty-surface spans and unresolved collisions explicitly handled, never silently guessed | - | word-not-found: terminal; strong-not-linked: terminal |
| `report.cluster` | cluster-report / Cluster-Report.ps1 | evaluate/review the cluster taxonomy and cluster_strong assignment coverage, scoped to strong.origin=word | - | - |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

| Step | Method rules | Quality checks | Delivered to the session |
|---|---|---|---|
| `raw.verses` | 1 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `lexical.readiness` | 1 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `lexical.build` | 5 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `spine.check` | 1 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |

Texts: appendix 2.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:66 | cluster-label-must-track-membership | always | ps:Cluster-Assign.ps1; ps:ClusterSubgroup.ps1 | yes, at Cluster-Assign.ps1 |
| B:70 | cluster-tags-loose-no-retagging | study_active | path:_analytics/**; ps:Cluster-Assign.ps1 | yes, at Cluster-Assign.ps1 |
| B:71 | reuse-extracted-base-data-set-based-mcode | study_active | path:_analytics/**; command:sqlite | **no** |
| B:95 | verse-sets-only-through-raw-layer | study_active | path:_analytics/**; ps:New-Word.ps1 | yes, at New-Word.ps1 |
| B:113 | bare-strong-decomposed-to-derivatives | always | ps:Verse-Scope.ps1; ps:Reading.ps1 | **no** |
| B:13 | dont-assume-which-database | always | command:sqlite | **no** |
| B:68 | stage1-corrections-only-via-real-rerun | always | ps:VerseLexical.ps1 | yes, at VerseLexical.ps1 |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `governance.base_data_spine` | "verse-span-strong-cluster-must-sync: every strong occurring in a live span must resolve, through cluster_strong, to a live cluster -- not merely to a live strong row. A strong with zero live cluster_strong allocation is a spine failure (FATAL), not a lexical-build-specific precondition." | The base-data spine, researcher ruling 2026-09-10 (escalation #1613 audit, iba/docs/1613-meaning-layer-config-inventory-v1-20260909.md section17): verse defines what is INCLUDED in the study; span defines HOW meaning is derived from the verse text; strong defines WHAT the meaning IS -- the operative anchor. These three must be in sync at all times; a discovered desync (e.g. a span-referenced code with no live strong row) is a FATAL ERROR, fixed on discovery, not merely logged. strong is the main operative: extended meaning is pulled from language-specific repositories (Hebrew+Greek: strong_meaning_tree/strong_meaning_parsed; Greek-only: strong_lexicon/strong_lsj_parsed/strong_mounce_parsed) and these must be absolutely in sync by language. Missing extended meaning is an ACCEPTED, non-fatal anomaly ONLY when explained by classification (T2/T3-T15/backfill -- see method rule spine-extended-meaning-accepted-anomaly), pulled on demand as analysis needs it, not proactively for every strong. Parse (strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed) makes extended meaning digestible: every strong with extended meaning pulled MUST have a parse row; a break here is a FATAL ERROR, fixed on discovery. Once the spine is sound, verse-strong-parse is the whole route for meaning-in-context during analysis; if a term becomes significant during analysis and its parse is missing, pull it through on demand. Diagnosis: existing base-data incompleteness/errors trace to mismanagement of this spine, not unrelated bugs. Adjusted 2026-09-10 (escalations #1622-1624): discovery of a missing meaning/parse entry must TRIGGER its update at the point of discovery, not merely be logged for later. |
| `governance.verse_gap_by_design` | "A verse missing from iba.db's verse table (no `verse` row for that osisId) is BY DESIGN, not a data-integrity error. Verse-existence is gated on prior term discovery (concordance-driven per-Strong's onboarding, iba/app/handlers/raw.py:verses) -- do not escalate, flag, or attempt to backfill a missing verse as a bug. Extent measured 2026-07-29: 2,049/31,086 verses (6.59%) missing, concentrated in genealogy/list-heavy books (1Chr 44%, Ezra 40%, Neh 31%, Josh 23%, Num 17%); a sample read of the missing verses judged the risk within tolerance for this study (iba/app/reports/verse-existence-census-20260729.md). The spine check never looks for a missing verse." | researcher ruling 2026-07-29, after measuring the full-Bible extent of the term-discovery verse gap (see project_iba_verse_existence_gated_on_term_discovery memory + iba/app/reports/verse-existence-census-20260729.md) |
| `language.greek_prefix` | "G" | a strong starting with this is Greek; else Hebrew |
| `meaning.head_marker` | ": " | a mediumDef starting with this is a SENSE: head + the lemma's tree. Else the code is its own lemma. |
| `cluster.quality_report_path` | "_analytics/Clusters/cluster-assign.md" | report path for cluster.validate, same convention as lexicon.quality_report_path |
| `lexical.readiness_report_path` | "research/discovery/lexical-readiness.md" | where lexical.readiness persists its findings -- #1606/#1706 Phase A |
| `spine.meaning_lexicon_languages` | ["Greek"] | #2173 P3: languages whose strongs are checked for a strong_lexicon row (lsj, mounce). Evidence 2026-10-20: 25 Hebrew strongs sampled at random from STEP returned no lsjDefs and no shortDefMounce (LSJ and Mounce are Greek lexicons); every Greek strong has a row. |
| `spine.quality_report_path` | "research/discovery/spine-check.md" | where spine.check persists its findings |
| `raw.meaning_tree_clean_pattern` | "^(?:[^<]/<(?!(?i:br\\b))[^>]*>)*$" | a clean strong_meaning_tree.sense_text: any text plus complete <ref>...</ref> spans (STEP's own citation markup, tolerated -- BUILD.md notes Greek mediumDef is prose with <ref> tags); any OTHER leftover markup (<br>, <b>, ...) fails -- the same <br> parser bug as strong_sense.head, one level deeper |
| `raw.strong_base_pattern` | "^([HG]\\d+)([A-Z]?)$" | Strongs-code base/sub-letter split - single home for this fact (2026-07-29), replacing three independent copies (handlers/raw.py, lib/versespanmeaningreport.py, and the retired candidate.lemma_base_pattern) |
| `raw.zero_strongs_action` | "reject" | What discover() does when a word resolves to zero strongs: 'reject' (default, researcher 2026-08-22 -- 'it should not happen', treated as anomalous every time until decided otherwise for a specific case) or 'proceed' (register the word anyway with zero strongs, no escalation). |
| `discovery.follow_related` | false | relatedNos is root-family noise (H2519 -> 'to divide', 'Mount Halak'). Not followed. |
| `discovery.particle_pattern` | "^[HG]9\\d{3}$" | grammar-particle codes; excluded from discovery, flagged on a span |
| `step.cap` | 60 | STEP's hard result cap; > this triggers the forward-walk |
| `step.expect_gloss_contains` | "God" | STEP preflight known-answer probe |
| `step.expect_min_verses` | 1000 | STEP preflight known-answer probe |
| `step.probe_strong` | "H0430" | STEP preflight known-answer probe |
| `step.required_for_runs` | true | STEP is mandatory infra, not optional -- initpys startup preflight and every STEP-dependent tool/handler must refuse rather than degrade when this is true and STEP is down |
| `step.span_html` | "<span(?: var='[^']*')?(?: morph='([^']*)')? strong='([^']*)'>([^<]*)</span>" | how STEP formats an interlinear span in a verse preview: (morph, strong, surface). The forward-walk and the span parse read it. |
| `step.walk_end` | "Rev.22.21" | forward-walk upper bound |
| `step.walk_max_iter` | 400 | forward-walk safety bound |
| `step.walk_start` | "Gen.1.1" | forward-walk lower bound |
| `lexicon.bracket_pairs` | {"(": ")", "[": "]", "{": "}"} | open->close bracket pairs classify_row/strip_bracketed treat as nestable — a gloss that is wholly one bracketed aside (e.g. '(obsolete)') classifies as 'not applicable'. |
| `lexicon.classify_lookup_max_words` | 3 | classify_row: a gloss/description with at most this many space-separated words is 'lookup', more is 'description' — same shape as candidate.tag_max_words's word-count threshold. |
| `lexicon.header_pos_tags` | ["v", "vb", "n", "a", "adj", "adv", "prep", "subst", "conj", "interj", "pron", "num", "part", "n m", "n f", "n c", "nm", "nf", "nc", "n pr m", "n pr f", "n pr loc"] | meaning_tree_rows()/is_header_only_line(): a strong_meaning_tree row with no sense_code of its own, whose entire (tag-stripped) text exact-matches one of these bare part-of-speech abbreviations, is a STEP-source section header for the numbered sense group that follows, not a sense itself — excluded before it ever becomes a strong_meaning_parsed row. Escalation #1668, 2026-09-10. |
| `lexicon.linebreak_pattern` | "[\\r\\n]+" | the only recognised sense-separator in strong_meaning_tree.sense_text/strong_lexicon.lsj/mounce — commas/semicolons/colons are NOT separators (STEP itself displays them as one sense). |
| `lexicon.lsj_level_tags` | ["level1", "level2", "level3", "level4"] | LSJ's own HTML tag names marking an explicit outline-level boundary (<LevelN>). |
| `lexicon.lsj_sublabel_pattern` | "^\\d+[a-z]*$" | LSJ sublabels are a bare number + optional letter (e.g. '2', '2a') — combined with the current top-level Roman numeral into 'I.2a'. |
| `lexicon.lsj_top_level_label_pattern` | "^[IVXLCDM]+$" | LSJ top-level sense labels are Roman numerals (I, II, III, ...) — matched to track the current top-level for building compound sublabels like 'I.2'. |
| `lexicon.non_latin_script_pattern` | "[Ͱ-Ͽἀ-῿֐-׿]" | classify_row: any match forces 'description' regardless of word count — Greek/Hebrew Unicode block ranges STEP's lexicon text uses. |
| `lexicon.outline_code_pattern` | "^(\\d+[a-zA-Z0-9]*\\))\\s*(.*)$" | strong_meaning_tree.sense_text: matches a leading outline code (e.g. '1)', '2a)') when sense_code itself is empty, splitting it from the remaining gloss text. |
| `lexicon.quality_report_path` | "research/discovery/lexicon-parse.md" | where lexicon.validate persists its findings |
| `lexicon.ref_tag_pattern` | "<ref=['\"]([^'\"]*)['\"]>" | matches STEP's <ref='Act.14.17'>display</ref> markup (a nameless '=value' pseudo-attribute HTMLParser can't parse as a real attribute) so it can be rewritten to a well-formed <ref key="..."> before parsing. |
| `cluster.assign.exclude_flag_gloss_from_voting` | true | the cluster-allocation session pitfall: cluster.csv FLAG gloss list is an uncertainty bag, never a positive P2 precedent-match signal |
| `cluster.assign.word_optional_clusters` | ["T2", "T3"] | cluster codes exempt from the needs-a-word_registry-link rule (Q2.4.1 exception 1) -- researcher correction 2026-08-12: a word generates the verse, it does not need to own every strong later found in it; T3 is inherently not word-specific |
| `registry.duplicate_shared_threshold` | 1.0 | fraction of a new words seed strongs an existing word must already hold for registry.create to warn it may be a duplicate/typo (1.0 = must share ALL strongs) |
| `registry.folder_naming_convention` | "_analytics/registry/word_registry per-word subfolders (report.strong_verse_output_dir) must be named {word_registry.id zero-padded 3 digits}_{word, lowercase, spaces as hyphens} -- e.g. 020_compassion. id comes from the LIVE iba.db word_registry table, never bible_research.db's legacy numbering (the two differ)." | the folder-naming rule for per-word registry output, so it stays config-governed rather than a one-off manual cleanup that can silently drift again |
| `registry.strip_ends_pattern` | "[^A-Za-z]" | on entry, strip runs of these from BOTH ends of the word ('[hypocrisy]' -> 'hypocrisy'); internal hyphens/spaces kept. Word matching is case-insensitive. |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `cluster.status` | strong_assignment_in_progress, t_cluster_assignment_completed, ready_for_subgroup_allocation, ready_for_reading, ready_for_observations, ready_for_synthesis, completed, strongs_reassigned |
| `cluster_subgroup.status` | allocated, ready_for_reading, ready_for_answer, answer_complete, completed, re_read_needed |
| `word_status` | proposed, approved, raw-complete, signed-off, rejected |
| `word_status_built` | raw-complete, signed-off |
| `party_kind` | divine, human, non_human |

### Lexical code classes (`cfg_lexical_code_class`)

| Strong's | Class | Evidence |
|---|---|---|
| G1063 | connective_causal | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17) — CONNECTIVE_LEXICON. |
| H3588A | connective_causal | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17) — CONNECTIVE_LEXICON. |
| G1161 | connective_coordinating | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17) — CONNECTIVE_LEXICON. |
| G2532 | connective_coordinating | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17) — CONNECTIVE_LEXICON. |
| H9002 | connective_coordinating | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17) — CONNECTIVE_LEXICON. |
| G2443 | connective_purpose | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17) — CONNECTIVE_LEXICON. |
| G3361 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| G3756 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| G3760 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| G3761 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| H0408 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| H3808 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| H3809 | negator | proven live, method-and-drift-mitigation doc §2 (script run against Gal 5:16-17, unmodified iba.db, read-only) — NEGATOR_LEXICON. |
| G2316 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |
| G2424 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |
| G2962 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |
| G5547 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |
| H0410 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |
| H0430 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |
| H3068 | party_divine | checked live, escalation #1383 v32 — distinguishable from lowercase generic lord/god codes. |

### What the rows above do not show

- **No config routes a missing base datum from a reading to its recovery step** (New-Word, raw.backfill_meaning, the spine). The reading's `meaning_missing` gap is the one route today.

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `cluster_strong` | one row per (strong, cluster_code) assignment | The strong<->cluster link. Cluster membership is a property of the Strong's code itself, independent of word_strong/word_registry — deliberately has no FK/dependency on either. `source` tracks provenance (old-system-migration now; future allocation passes get their own source value, never overwriting a prior row in place). | **none recorded** |
| `strong` | one row per strong — unique, global to the study | L2 — the strong's identity. The meaning is normalised out (O4): it lives in strong_sense / strong_meaning_tree / strong_lexicon. | **none recorded** |
| `strong_related` | one row per (strong, related strong) pair STEP's getInfo returned (fetched 2026-07-25) | L2b — NOT derived from any raw table; fetched live from STEP per full strong code (lib.stepapi.Step.call2_getInfo, vocabInfos[0].relatedNos) since no raw table captures this. related_strong is unconstrained — STEP can name a code this app has never onboarded via raw.detail. | **none recorded** |
| `validation_result` | one row per check a validate step ran | util.validation — the outcome of a check, persisted so it can be inspected and reported. A passed check is a recorded fact, not just an advancing run. | **none recorded** |
| `verse_lexical` | one row per Strong's code within a span (span_id, code_ordinal) — a compound span yields several rows, one per component code | L4b — DERIVED, version-aware. The mechanical T1-T3 reading: role classification + stem/voice-selected sense + named-not-resolved ambiguity, per code. Read by report.verse_lexical and, downstream, by T4-T9 — never by re-deriving from span/strong/strong_meaning_parsed directly. | **none recorded** |
| `word_registry` | one row per English inner-being word | the study's entry point; scope of a new-word run | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## 0.C. 0.C Scope: a collection of verses for a stated purpose; a cluster segmented, not read whole

The scope of a reading and its purpose; base data read only to assess it.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `verse_scope.resolve` | verse-scope / Verse-Scope.ps1 | the scope resolver: any request (cluster, subgroup, strand, word, strong -- a bare code decomposed to its derivatives -- verse references, narrative chapter or block, claim, observation, thread item or thread, request file) -> the collection of verses as JSON, each verse with its routes, everything not resolved listed; -OnlyStrong narrows it (read-only) -- see lib/versescope.py (escalation #2228) | - | refused: terminal |
| `reading.open` | reading / Reading.ps1 | a reading opened on a scope (the selectors of Verse-Scope.ps1; the 2,500 review applies): its verses kept, the scope collated, and the gap JSON written, one section per gap type of the recording phase -- see lib/reading.py (escalation #2228) | reading (iba), reading_verse (iba) | refused: terminal |
| `open_item.due` | open-item / Open-Item.ps1 | the worded items that come back when a cluster is worked (read-only) -- see lib/openitem.py (escalation #2236) | - | refused: terminal |
| `escalation.thread` | escalation-reporting / Escalation.ps1 | open threads (type=thread): alias, id, title, open items; -State in-progress narrows; -Id OT-nn shows one thread's items with their responses -- see lib/escalation.py:write_thread_report | - | bad-parameter: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

**None.** No method rule or quality check is tied to any step of this stage.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:113 | bare-strong-decomposed-to-derivatives | always | ps:Verse-Scope.ps1; ps:Reading.ps1 | yes, at Reading.ps1, Verse-Scope.ps1 |
| B:94 | strand-pull-scans-glosses-across-codes | study_active | path:_analytics/** | **no** |
| B:110 | surface-is-the-sensitivity-lens | study_active | path:_analytics/** | **no** |
| B:111 | filters-are-working-aids | study_active | path:_analytics/** | **no** |
| B:93 | strand-checks-its-m47-verses | study_active | path:_analytics/** | **no** |
| B:116 | read-the-verse-first | study_active | general:general; ps:Reading.ps1 | yes, at Reading.ps1 |
| E:16 | thread_check_before_work | (escalation rule) | ps:Escalation.ps1 | yes, at Escalation.ps1 |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `reading.output_dir` | "outputs/reading" | where Reading.ps1 writes each reading's gap JSON, synergy JSON and account, one folder per reading (escalation #2228) |
| `verse_scope.max_seconds` | 30 | time guard on the scope resolver: a request still resolving after this many seconds is refused, to be reformed (researcher 2026-10-23, #2228) |
| `verse_scope.max_verses` | 2500 | size guard on the scope resolver: a request whose result has more verses is held for review before it proceeds (researcher 2026-10-23, #2228: 'any verse selection above 2500 should be subject to a review before proceeding'). It proceeds only with -Reviewed "<the review>", given after the researcher has reviewed it, and the review is recorded in the answer. Clusters above it: M72 (3,972), M47 (2,841), M65 (2,568) |
| `verse_scope.output_dir` | "outputs/verse-scope" | where Verse-Scope.ps1 writes each verse collection as <label>-<YYYYMMDD>.json, versioned and archived by lib/filingkit (escalation #2228) |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `reading_state` | open, published, recorded, synergised, withdrawn |

### What the rows above do not show

- **No config for a reading's purpose, nor for segmenting a cluster** (R2's `whole_cluster_reading_start`).

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `reading` | one row per reading: the work on one scope | #2228: a reading opened from a scope request and served by the escalation that anchors it; it passes three gates in order (recorded, synergised, published), each checked by Reading.ps1 | **none recorded** |
| `reading_verse` | one row per verse in a reading's scope at opening | #2228: a reading keeps its verses even if the base data moves | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## 0.GAP. 0.GAP Gap discovery and gap analysis: pre-claims (before D1) and post-claims (inside D4's claim step)

Across all tables for the scope, at quality depth, without verse text: what is there, what should be there, its quality; work already done gathered; gaps written and kept current.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `verse_collate.collate` | verse-collate / Verse-Collate.ps1 | what is known and what is missing for a scope: the scope resolved as verse_scope.resolve does (its guard applies), then per verse its text, inner-being words, observations, strand hits, claims and their tellings, citing blocks, matching open items and the cluster-file lines naming it; the lexicon per strong; the gaps per verse (read-only) -- see lib/versecollate.py (escalation #2228) | - | refused: terminal |
| `reading.open` | reading / Reading.ps1 | a reading opened on a scope (the selectors of Verse-Scope.ps1; the 2,500 review applies): its verses kept, the scope collated, and the gap JSON written, one section per gap type of the recording phase -- see lib/reading.py (escalation #2228) | reading (iba), reading_verse (iba) | refused: terminal |
| `reading.check` | reading / Reading.ps1 | the gate the reading is at, checked from the tables: gate 1 (every gap item has an id that exists or a reason; the verses are then marked analysed) or gate 2 (every observation carried or disposed, every claim told or held, every matched open item settled) -- see lib/reading.py (escalation #2228) | reading (iba), verse_meta (iba) | refused: terminal |
| `reading.account` | reading / Reading.ps1 | the reading from the tables: its state, each gate's gaps (read-only) -- see lib/reading.py (escalation #2228) | - | refused: terminal |
| `reading_index.build` | reading-index / Reading-Index.ps1 | index the study files under reading_index.roots: new and changed files read (sha256), removed ones marked; every verse reference with its file, section, line and how it was found; stops between files after reading_index.max_seconds -- see lib/readingindex.py (escalation #2228) | reading_file (iba), reading_ref (iba), reading_section (iba) | refused: terminal |
| `reading_index.report` | reading-index / Reading-Index.ps1 | the coverage report from reading_file/reading_section/reading_ref (read-only) -- see lib/readingindex.py (escalation #2228) | - | refused: terminal |
| `verse_meta.set_status` | verse-meta / VerseMeta.ps1 | sets verse_meta.status (cfg_enum verse_meta_status) for a comma-delimited list of verse references; stamps status_changed_at only on a real change (#1661; #2207: through run.py) | verse_meta (iba) | bad-parameter: terminal; not-found: terminal |
| `spine.check` | spine-check / Spine-Check.ps1 | read-only check of the base-data spine (governance.base_data_spine): span -> strong, verse <-> span, strong -> cluster, and strong -> meaning (strong_sense, strong_meaning_tree, strong_lexicon; each local gap asked of STEP: content in STEP that the table lacks is FATAL, nothing in STEP is a gap by design). Persists a report every run; escalates only on a FATAL finding. Run by session-close (SC2), not at start (#2173 P3). The parse tables stay retired. See handlers/spine.py. | - | spine-fatal-rejected: terminal; spine-fatal-found: terminal; needs-revision: terminal |
| `lexical.readiness` | verse-lexical / VerseLexical.ps1 | 3-leg read-only precondition check for the Layer 1 rebuild (#1606): Leg1 every live verse has >=1 live span; Leg2 every live span's strong_variant code resolves to a live strong row (duplicates spine.check's own desync check deliberately -- #1606's own framing is one cohesive 3-leg check); Leg3 every live strong that actually occurs in a live span has >=1 live cluster_strong allocation (the precondition Layer 1's redesigned role column, a JSON array of cluster_strong.cluster_code, depends on directly). Persists a report every run (governance.reports_must_persist), fails on any FATAL finding. | - | - |
| `cluster.validate` | cluster-assign / Cluster-Assign.ps1 | Read-only DB-wide coverage + exception report: unclassified strongs, backfill non-T2 not yet promoted, and the two named exception shapes (cluster with no word; backfill with an already-active/clustered sibling). Persists a report every run. UPDATED 2026-09-15 (escalation #1606): escalates if EITHER an unclassified strong exists OR either named exception shape exists -- previously only escalated on the two named exception shapes, leaving a plain unclassified count unescalated indefinitely. UPDATED 2026-09-15 (escalation #1707): before escalating, checks whether the current findings already fall within a PRIOR run's approved baseline (escalation.answered_baseline_for_step, cross-run, not just this run) -- a known, already-signed-off backlog is acknowledged automatically instead of raising a fresh escalation every run; a genuine increase in any count still escalates. | - | needs-review: terminal; findings-rejected: terminal; needs-revision: terminal |
| `report.strong_meaning` | strong-meaning-report / StrongMeaning-Report.ps1 | meaning-parse layer coverage — strong/strong_sense/strong_meaning_tree/strong_lexicon gap list, sense-count distribution, lexicon completeness | - | - |
| `open_item.review` | open-item / Open-Item.ps1 | the stragglers report: items not worded, worded items past the review age (read-only) -- see lib/openitem.py (escalation #2236) | - | refused: terminal |
| `escalation.thread_audit` | escalation-reporting / Escalation.ps1 | #2173 P5: thread quality, validity and integrity, T-a to T-g, each finding by thread item -- see lib/threadaudit.py | - | - |
| `narrative_register.find` | narrative-register / Narrative-Register.ps1 | read-only search (-Verse -Chapter -Section -Claim -Text -Escalation -Thread -Verdict -NotInNarrative -ToldInMoreThanOne) -- see lib/narrativeregister.py (escalation #2110) | - | refused: terminal |
| `narrative_register.check` | narrative-register / Narrative-Register.ps1 | read-only: chapters, sections and passage anchors against the files on disk; chapters with no kind or purpose, duplicate reading orders, stray files, direct-edit rows -- see lib/narrativeregister.py (escalation #2110, #2155) | - | refused: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

| Step | Method rules | Quality checks | Delivered to the session |
|---|---|---|---|
| `spine.check` | 1 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `lexical.readiness` | 1 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |

Texts: appendix 2.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:114 | synergise-from-tables-not-memory | study_active | general:general; ps:Reading.ps1 | yes, at Reading.ps1 |
| B:77 | claims-register-keeps-narrative-honest | study_active | path:_analytics/essay/**; ps:Narrative-Register.ps1; ps:Reading.ps1 | yes, at Narrative-Register.ps1, Reading.ps1 |
| B:93 | strand-checks-its-m47-verses | study_active | path:_analytics/** | **no** |
| B:94 | strand-pull-scans-glosses-across-codes | study_active | path:_analytics/** | **no** |
| B:116 | read-the-verse-first | study_active | general:general; ps:Reading.ps1 | yes, at Reading.ps1 |
| B:115 | open-item-has-a-clear-purpose | always | ps:Open-Item.ps1; ps:Escalation.ps1; ps:Reading.ps1 | yes, at Escalation.ps1, Open-Item.ps1, Reading.ps1 |
| B:2 | step-not-done-without-validated-output | always | general:* | only at session start (general) |
| B:24 | show-evidence-dont-smooth-over | always | general:* | only at session start (general) |
| B:107 | enumerate-link-tables-before-orphan-verdict | always | command:sqlite | **no** |
| B:61 | inactive-tables-never-active-inputs | always | command:sqlite | **no** |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `reading.gap_types` | {"not_read": {"phase": "recording", "records_in": ["ib_observation"], "guide": "A verse with no observation and no strand face. Read it in its passage; record what it states about the inner being (a new observation), name an existing observation that already covers it, or give the reason it holds nothing."}, "read_in_files_only": {"phase": "recording", "records_in": ["ib_observation"], "guide": "A verse the cluster files read (their lines are given) with no observation in the tables. Carry the reading into a table: a new observation from what the files say and the verse states, an existing observation, or the reason the files' reading holds nothing."}, "hit_unread": {"phase": "recording", "records_in": ["reading_strand_hit"], "guide": "A strand hit with no face and no reason. Give the hit its face (and the observation it goes into), or the reason it has none."}, "meaning_missing": {"phase": "recording", "records_in": ["strong_meaning_tree", "strong_lexicon"], "guide": "A word in scope with no meaning senses (or, for Greek, no Mounce entry). Pull it through the spine route and name the row, or give the reason it is not needed for this reading."}, "open_item": {"phase": "recording", "records_in": ["ib_observation", "escalation_thread_item_response"], "guide": "An open item that matches the scope: read for what it asks, and record what the reading found (an observation, or a response of kind touched). It is not closed here: closing is decided in synergy (gate 2)."}, "observed_no_claim": {"phase": "synergy", "records_in": ["narrative_claim", "ib_observation"], "guide": "An observation no current claim rests on: carry it by a claim, or dispose of it (held on an item, silent, withdrawn) with a reason. Gate 2's work, from the tables."}, "claim_not_told": {"phase": "synergy", "records_in": ["narrative_claim_telling"], "guide": "A current claim no block tells: tell it in a block, or hold it with a reason. Gate 2's work, from the tables."}} | the reading's gap types (cfg_enum reading_gap_type): each one's phase (recording: in the gap JSON, gate 1; synergy: gate 2), the table(s) it records into and the guide text written into its section; adding a gap type is an enum value and an entry here (escalation #2228, design v2 sec 2) |
| `report.stage1_coverage_validation_pattern` | "outputs/stage1-coverage-validation-{cluster_code}-{run_id}.csv" | Where lexical.meaning's own per-run coverage-validation report (stage1coverage.validate_coverage, BUILD #315) is written, every live call -- {cluster_code}/{run_id} substituted by the caller. Was a hardcoded f-string in iba/app/handlers/lexical.py; governance.reports_must_persist's own "config-defined report path" requirement (matching the established report.batch_progress_path / report.lexical_notes_output_pattern precedent) means it should have been this from the start -- found live 2026-09-22, escalation #1824 governance audit. |
| `open_item.review_age_days` | 60 | Open-Item.ps1 -Action Review lists worded items older than this as stragglers to deal with (#2236 D4) |
| `escalation.worked_strand_escalations` | {"M01": [1962], "M02": [1963], "M25": [1932], "M47": [1911, 2172], "M64": [1978, 1986], "M18": [1993], "M72": [1998], "M09": [2148], "M08": [2156], "M07": [2171]} | #2173 P5 T-d: per cluster, the escalations that carry its strand. A strand counts as worked only when every listed escalation is completed (read from state at audit time, never from memory); M47 lists #2172, so it is not worked while #2172 is open. Add a cluster here when its strand escalation is raised. |
| `escalation.thread_audit_report_path` | "outputs/escalation/escalation-thread-audit.md" | #2173 P5: thread audit report (Escalation.ps1 -Action ThreadAudit; lib/threadaudit.py) |
| `session_close.state_path` | "iba/app/reports/session-close-state.json" | #2173 SC5(c): the register-check findings at the previous session's last close (the baseline that tells a new finding from a standing one) |
| `lexical.readiness_report_path` | "research/discovery/lexical-readiness.md" | where lexical.readiness persists its findings -- #1606/#1706 Phase A |
| `cluster.quality_report_path` | "_analytics/Clusters/cluster-assign.md" | report path for cluster.validate, same convention as lexicon.quality_report_path |
| `reading_index.max_seconds` | 120 | time guard on a build: it stops between files once past this many seconds and the next build carries on (researcher 2026-10-23, #2228: 'the tool does not work for longer than expected') |
| `reading_index.output_dir` | "outputs/reading-index" | where Reading-Index.ps1 -Step Report writes the coverage report (#2228) |
| `reading_index.roots` | ["_analytics/Clusters", "_analytics/cross-cluster-web/origin-of-thought"] | the folders Reading-Index.ps1 indexes (repo-relative; archive/ folders inside are skipped). The cluster readings, by the researcher exclusions of 2026-10-22 (#2228), and the origin-of-thought strand folder, so the verses its October ledger cites come up as read_in_files_only gaps (#2216 option B, researcher 2026-10-23) |
| `spine.meaning_lexicon_languages` | ["Greek"] | #2173 P3: languages whose strongs are checked for a strong_lexicon row (lsj, mounce). Evidence 2026-10-20: 25 Hebrew strongs sampled at random from STEP returned no lsjDefs and no shortDefMounce (LSJ and Mounce are Greek lexicons); every Greek strong has a row. |
| `spine.quality_report_path` | "research/discovery/spine-check.md" | where spine.check persists its findings |
| `verse_collate.max_seconds` | 120 | time guard on collating: past this many seconds the run is refused, to be reformed to a narrower scope (researcher 2026-10-23, #2228) |
| `verse_collate.output_dir` | "outputs/verse-collate" | where Verse-Collate.ps1 writes <label>-<YYYYMMDD>.json (the record) and .md (the summary) (escalation #2228) |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `reading_gap_type` | claim_not_told, hit_unread, meaning_missing, not_read, observed_no_claim, open_item, read_in_files_only |
| `verse_meta_status` | exclude, citated, analysed |
| `reading_state` | open, published, recorded, synergised, withdrawn |
| `cluster.status` | strong_assignment_in_progress, t_cluster_assignment_completed, ready_for_subgroup_allocation, ready_for_reading, ready_for_observations, ready_for_synthesis, completed, strongs_reassigned |
| `cluster_subgroup.status` | allocated, ready_for_reading, ready_for_answer, answer_complete, completed, re_read_needed |
| `reading_ref.found_by` | explicit, follow-on c:v, follow-on v. |
| `reading_ref.kind` | verse, whole chapter |
| `reading_ref.line_kind` | bullet, heading, paragraph, table row |

### What the rows above do not show

- **Measures of "read" in config and code, none related to another by any row:** `versecollate.py` (a verse is read when any `draft` observation or strand face rests on it); `verse_meta.status` `analysed` (set only by a reading's gate 1); `stage1coverage.py` (expected verse, strong and question triples against live `verse-reading` nodes); `clusterstatus.py` (`cluster.status` advances when every member strong has `verse-reading` coverage); method rules 96 and 107 (per-strong traceability, per-question completeness, D2); `reading_index` (a verse named in a study file); `narrative_register.find -NotInNarrative` (B:77's missing reading area); the thread audit T-a to T-g.
- **No gap register.** No table records a gap, its kind, when it was found, or its state; every measure above is recomputed when run. A reading's gaps live in its gap JSON file.
- **No sufficiency measure.** No row says when a verse, a word, a scope or a cluster has been read enough.
- **Post-claims** gap reading has no step of its own today; gate 2's check (`reading.check`) counts presence only.

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `reading` | one row per reading: the work on one scope | #2228: a reading opened from a scope request and served by the escalation that anchors it; it passes three gates in order (recorded, synergised, published), each checked by Reading.ps1 | **none recorded** |
| `reading_file` | one row per indexed study file | #2228 tool 2: a study file under reading_index.roots read by Reading-Index.ps1 -Step Build; re-read only when its sha256 changes | **none recorded** |
| `reading_ref` | one row per verse a study file names, at a line | #2228 tool 2: every verse reference in an indexed file, after range expansion, with how it was found and the line it stands on; a reference that resolves to nothing kept with its reason | **none recorded** |
| `reading_section` | one row per heading section of an indexed file | #2228 tool 2: the sections of a study file (# to #### headings; the opening before the first heading is section 0) | **none recorded** |
| `reading_verse` | one row per verse in a reading's scope at opening | #2228: a reading keeps its verses even if the base data moves | **none recorded** |
| `verse_meta` | one row per verse (1:1 with verse.id) | Verse-level base-data companion to `verse` -- collates language/testament/chapter/verse_num/passage linkage once at the right grain, instead of denormalizing per-code (the old `language` source) or leaving facts homeless (`genre`, `lexical_complete_at`). Auto-synced via 4 triggers on verse/verse_lexical/verse_passage inserts and verse.deleted updates -- never written to directly by application code. Escalation #1608, 2026-09-09. | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## D1. D1 Word level: Stage 1 (lexical.meaning, lexical.relational); table data only

Each word's meaning and form in its occurrences, settled once so D4 does not re-derive it.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `lexical.meaning` | verse-lexical / VerseLexical.ps1 | The verse-reading stage, WORD-LEVEL HALF (#1711 original build; narrowed to word-level-only by the #1860 split, 2026-09-23): per-cluster, pre-subgroup Layer 2. Reads all 3 meaning sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) as complementary evidence for every strong the cluster's role-annotated word list covers (verse_lexical.role, including currently-unwired role-T2/T6/T10-T15 tags, not just the mechanically-wired subset), and answers M0.1 (Name and Naming) and M0.5 (Lexical and Semantic Analysis, incl. M0.5.11) from wa_obs_question_catalogue -- word-level only now; the relational family (M0.6.5/M0.6.6/D7.7.1/M0.7/M0.8.1) moved to the new lexical.relational step, which requires this step's own output as a precondition (readiness gate). Assembles the LLM payload and estimates cost; the live API call and the DB write are separate, explicit steps (cost preview before spend, never silent). | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `lexical.relational` | verse-lexical / VerseLexical.ps1 | The verse-reading stage, RELATIONAL HALF (#1860 split, 2026-09-23 -- researcher, verbatim: 'we must split the word questions and answers and the relational answers into separate processes. the relational process depends on the word work, and doing it in the same session can only result in errors.'). Per-cluster, pre-subgroup Layer 2, run AFTER lexical.meaning has covered the same verses -- a hard readiness gate refuses to run against any verse whose M-code words don't all have a committed word-level (M0.1/M0.5) observation yet. Answers M0.6.5 (relational, single-vantage), M0.6.6 (whole-network synthesis), D7.7.1 (operation-anchored permeability), M0.7.1-16 (verse substantiation), M0.8.1 (T2/T3 elevation flag), cluster-agnostic (every M-code word in the verse, not just this cluster's own home strong(s)). Grounds on the COMMITTED word-level ib_observation rows for each verse+strong (the researcher's own approval, #1860 v3: 'the base data must in any case be included for relational phase to be successful' -- so the raw lexicon (meaning_sources_by_strong) is ALSO sent alongside the committed findings, never one instead of the other). This is the true final stage of verse-reading -- the cluster.status t_cluster_assignment_completed -> ready_for_subgroup_allocation transition check runs here now, not in lexical.meaning. | ib_node (iba), ib_observation (iba), run_batch (iba) | - |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

| Step | Method rules | Quality checks | Delivered to the session |
|---|---|---|---|
| `lexical.meaning` | 10 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `lexical.relational` | 13 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |

Texts: appendix 2.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:4 | inferential-not-confirmed | always | general:* | only at session start (general) |
| B:7 | cost-cap-before-call | always | ps:VerseLexical.ps1 | yes, at VerseLexical.ps1 |
| B:8 | usage-log-required | always | ps:VerseLexical.ps1 | yes, at VerseLexical.ps1 |
| B:9 | sonnet-default-model | always | ps:VerseLexical.ps1 | yes, at VerseLexical.ps1 |
| B:37 | derive-from-instruction-not-prior-unreviewed-output | always | path:_analytics/** | **no** |
| B:68 | stage1-corrections-only-via-real-rerun | always | ps:VerseLexical.ps1 | yes, at VerseLexical.ps1 |
| B:110 | surface-is-the-sensitivity-lens | study_active | path:_analytics/** | **no** |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `lexical.meaning_max_verses_per_batch` | 1 | Cap on verses per lexical.meaning batch -- REACTIVATED 2026-09-22 (escalation #1842), researcher instruction verbatim: "batching based on strongs is inappropriate, the units of operation is verses not strongs." Reverts the 2026-09-21 supersession by lexical.meaning_max_strongs_per_batch (now inactive): that switch was made because a fixed verse count was found unsafe when strong-density varies (M67 5-verse chunks ranged 6-21 strongs) -- but the strong-density approach own failure that triggered this reversal (M49, 2026-09-22) was a 3-verse chunk (union of 8 strongs), not an unusually dense one, so it was not actually delivering the safety its adoption assumed. Value set to 1 (not the old 5): live per-verse M-tagged strong density across M49 own 193-verse scope ranges 1-10 (median 3) -- a single-verse batch bounds each call to one verse own inherent content, isolating any remaining density outlier to one retryable batch instead of an unpredictable multi-verse one. Read by _chunk_verses_fixed_size() (iba/app/handlers/lexical.py). |
| `lexical.relational_max_verses_per_batch` | 1 | Cap on verses per lexical.relational batch (#1860, 2026-09-23 split) -- mirrors lexical.meaning_max_verses_per_batch's own value and rationale (single-verse batches bound each call to one verse's own inherent content). Read by _chunk_verses_fixed_size() via handlers/lexical.py:relational. |
| `report.stage1_coverage_validation_pattern` | "outputs/stage1-coverage-validation-{cluster_code}-{run_id}.csv" | Where lexical.meaning's own per-run coverage-validation report (stage1coverage.validate_coverage, BUILD #315) is written, every live call -- {cluster_code}/{run_id} substituted by the caller. Was a hardcoded f-string in iba/app/handlers/lexical.py; governance.reports_must_persist's own "config-defined report path" requirement (matching the established report.batch_progress_path / report.lexical_notes_output_pattern precedent) means it should have been this from the start -- found live 2026-09-22, escalation #1824 governance audit. |
| `cluster.recording_similarity_threshold` | 0.85 | recordingpass.py record_one_observation: obs_text similarity score (0-1, difflib SequenceMatcher) above which a same-coordinate new observation is treated as a superficial edit of an existing one (align in place) rather than a genuine broaden (new row). Was a hardcoded module constant with no live tuning; promoted to cfg_setting per escalation #1753/#1761 precedent. |
| `lexical.llm_api_url` | "https://api.anthropic.com/v1/messages" |  |
| `lexical.llm_api_version` | "2023-06-01" |  |
| `lexical.llm_chars_per_token` | 4 |  |
| `lexical.llm_max_cost_per_batch` | 1.0 |  |
| `lexical.llm_max_output_tokens` | 40000 |  |
| `lexical.llm_model` | "claude-sonnet-5" |  |
| `lexical.llm_rate_input_per_million` | 3.0 |  |
| `lexical.llm_rate_output_per_million` | 15.0 |  |
| `lexical.llm_usage_log_path` | "_analytics/lexicon/lexical-extracts/lexical-llm-usage.csv" |  |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `ib_observation.stage` | verse-reading, char-subgroup, char-reading, char-answers, char-synergy, strand-reading |
| `ib_observation.tag` | verse-grouping, difference-inference, surface-gloss-divergence, no-human-context, data-error, alternative-meaning, could-not-resolve, answered-no-flag, tightly-related, no-direct-connection, qualifier-for-term, no-impact, not-related-to-meaningful-word, sole-mcode-in-verse, cluster-pole-negative, cluster-pole-positive, attested-pre-nt, nt-coinage, needs_adjacent_verse_context, elevation-candidate, key-statement |
| `ib_observation.status` | resolved, needs-corroboration, open, silent, withdrawn, draft |
| `ib_observation.window` | meaning, action-impact, relational, literary, cognitive, affective, operational, constitutional, origin, scientific, Subgroup, faculty |
| `ib_observation.meaning_source` | strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce, strong_lexicon, verse-text, role-tags, cluster, observations, n/a |
| `ib_observation.basis` | read, stated |
| `wa_obs_question_catalogue.scope` | Word/term (lexical), Verse-context, The verse, Characteristic (HIB behaviour), Characteristic relational, The HIB, Other non-human beings |
| `wa_obs_question_catalogue.status` | active, retired |
| `wa_obs_question_catalogue.tier` | M0, D1, D2, D3, D4, D5, D6, D7, D9, D10, D11, D12, X0, F0, T7 |

### What the rows above do not show

- **The registered steps call the API** (`lexical.meaning`, `lexical.relational`, via `versereadinggenerate.call_api`); who performs D1 is R3c.

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `ib_node` | one row per grounding element an ib_observation cites (strong/verse/subgroup/cluster/question/another observation) | The cluster-reading pack's own grounding table (#1692, design-complete 2026-09-14). Makes 'no way to check a finding's grounding' structurally impossible via the CHECK constraint + the mandatory coverage self-check (#1692 SS2: every strong/verse in a subgroup's membership must be grounded by >=1 ib_node row, checked at LLM generation time and independently re-checked by the recording pass at load time). | **none recorded** |
| `ib_observation` | one row per observation | One observation: a typed finding from a reading, with its text, meaning, implication, basis, parties and status (draft or withdrawn), grounded on verses, strongs, subgroups, clusters or other observations through ib_node. Written by stage: verse-reading (lexical.meaning, lexical.relational), char-reading, char-answers and char-subgroup (cluster.reading, cluster.answer, cluster.subgroup), strand-reading (strand_reading.record, strand_reading.derive), and enhanced by observation_enhancer.apply. A differently-shaped legacy table of the same name in bible_research.db is inactive. | **none recorded** |
| `run_batch` | one row per batch/chunk attempt of a live multi-batch (or single-call) run | The batch/step-level control table (escalation #1756, researcher-approved design 2026-09-18) -- resume/skip (a new run_id skips any batch a PRIOR run_id already committed, via UNIQUE(step, selector_key, batch_content_key)), crash safeguard (a 'running' row with no terminal update proves a dead run), and live progress monitoring (BatchProgress.ps1) for every long-running LLM-calling step. lib/batchcontrol.py is the sole writer. Prompted directly by M49's Stage 1 verse-reading run needing two full from-scratch restarts this session with no way to skip already-paid-for batches. | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## D2. D2 Characteristics: clusters, subgroups, characteristics, open items; table data only

The characteristics the scope bears on, and how its words group.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `cluster.subgroup` | cluster-reading / ClusterSubgroup.ps1 | The char-subgroup stage (#1690/#1693, process b): reads a cluster's full member-strong list -- gloss/surface plus its already-captured verse-reading (Stage 1) observations -- in ONE session (never streamed/batched, rule a requires the whole cluster read before any assignment), and groups strongs into meaning-based subgroups (max 10, FLAG excluded). Writes cluster_subgroup/cluster_subgroup_strong via the recording pass; advances cluster.status from ready_for_subgroup_allocation to ready_for_reading on success. | cluster_subgroup (iba), cluster_subgroup_strong (iba), ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `cluster.reading` | cluster-reading / ClusterSubgroup.ps1 | The char-reading stage (#1682/#1706 Phase F, process c): given one subgroup's member strongs, reads every occurrence corpus-wide (no sampling) plus all meaning sources, using Stage 1 (verse-reading) and Stage 2 (char-subgroup) observations as grounding, and synergises the similar/different contextual meaning of the subgroup's OWN member strongs against each other. Writes ib_observation/ib_node via the recording pass (stage='char-reading'); per-strong completeness is computed by code, not LLM-self-reported; advances cluster_subgroup.status from ready_for_reading to ready_for_answer on success. | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `cluster.answer` | cluster-reading / ClusterSubgroup.ps1 | The char-answers stage (#1682 §4A / #1706 Phase F, process d): given one subgroup's member strongs and Stage 1/2/3's own accumulated observations, answers the catalogue's characteristic-grain question battery (52 live questions, science-extract-dependent and Stage-1-owned D7.7.1 excluded), multiple slants where the evidence genuinely differs. Writes ib_observation/ib_node via the recording pass (stage='char-answers'); per-question completeness is computed by code; advances cluster_subgroup.status from ready_for_answer to answer_complete on success. | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `open_item.due` | open-item / Open-Item.ps1 | the worded items that come back when a cluster is worked (read-only) -- see lib/openitem.py (escalation #2236) | - | refused: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

| Step | Method rules | Quality checks | Delivered to the session |
|---|---|---|---|
| `cluster.subgroup` | 9 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `cluster.reading` | 15 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `cluster.answer` | 8 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |

Texts: appendix 2.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:4 | inferential-not-confirmed | always | general:* | only at session start (general) |
| B:7 | cost-cap-before-call | always | ps:VerseLexical.ps1 | **no** |
| B:8 | usage-log-required | always | ps:VerseLexical.ps1 | **no** |
| B:9 | sonnet-default-model | always | ps:VerseLexical.ps1 | **no** |
| B:37 | derive-from-instruction-not-prior-unreviewed-output | always | path:_analytics/** | **no** |
| B:66 | cluster-label-must-track-membership | always | ps:Cluster-Assign.ps1; ps:ClusterSubgroup.ps1 | yes, at ClusterSubgroup.ps1 |
| B:70 | cluster-tags-loose-no-retagging | study_active | path:_analytics/**; ps:Cluster-Assign.ps1 | **no** |
| B:89 | change-of-character-recorded | study_active | path:_analytics/** | **no** |
| B:115 | open-item-has-a-clear-purpose | always | ps:Open-Item.ps1; ps:Escalation.ps1; ps:Reading.ps1 | yes, at Open-Item.ps1 |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `cluster.recording_similarity_threshold` | 0.85 | recordingpass.py record_one_observation: obs_text similarity score (0-1, difflib SequenceMatcher) above which a same-coordinate new observation is treated as a superficial edit of an existing one (align in place) rather than a genuine broaden (new row). Was a hardcoded module constant with no live tuning; promoted to cfg_setting per escalation #1753/#1761 precedent. |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `cluster_subgroup.status` | allocated, ready_for_reading, ready_for_answer, answer_complete, completed, re_read_needed |
| `ib_observation.stage` | verse-reading, char-subgroup, char-reading, char-answers, char-synergy, strand-reading |
| `ib_observation.tag` | verse-grouping, difference-inference, surface-gloss-divergence, no-human-context, data-error, alternative-meaning, could-not-resolve, answered-no-flag, tightly-related, no-direct-connection, qualifier-for-term, no-impact, not-related-to-meaningful-word, sole-mcode-in-verse, cluster-pole-negative, cluster-pole-positive, attested-pre-nt, nt-coinage, needs_adjacent_verse_context, elevation-candidate, key-statement |

### What the rows above do not show

- **The registered steps call the API** (`iba/app/handlers/cluster.py` lines 224 and 371); who performs D2 is R3c.

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `cluster_subgroup` |  | Cluster-reading subgroup: a curated group of Strong-numbered codes within one cluster (M-code), the unit of per-subgroup reading/answering in the cluster-reading pipeline (Stage 3, cluster.subgroup step). Built 2026-09 for the synergy-build pipeline; a differently-shaped legacy table of the same name predates it in bible_research.db (M-code cluster model) -- same name, different table, different database. | **none recorded** |
| `cluster_subgroup_strong` | one row per strong-to-subgroup placement (membership) | The cluster-reading pack's own subgroup-membership table (#1690, was mti_term_subgroup, renamed 2026-09-13, design-complete). UNIQUE(strong) enforces one strong, one family, structurally. | **none recorded** |
| `ib_node` | one row per grounding element an ib_observation cites (strong/verse/subgroup/cluster/question/another observation) | The cluster-reading pack's own grounding table (#1692, design-complete 2026-09-14). Makes 'no way to check a finding's grounding' structurally impossible via the CHECK constraint + the mandatory coverage self-check (#1692 SS2: every strong/verse in a subgroup's membership must be grounded by >=1 ib_node row, checked at LLM generation time and independently re-checked by the recording pass at load time). | **none recorded** |
| `ib_observation` | one row per observation | One observation: a typed finding from a reading, with its text, meaning, implication, basis, parties and status (draft or withdrawn), grounded on verses, strongs, subgroups, clusters or other observations through ib_node. Written by stage: verse-reading (lexical.meaning, lexical.relational), char-reading, char-answers and char-subgroup (cluster.reading, cluster.answer, cluster.subgroup), strand-reading (strand_reading.record, strand_reading.derive), and enhanced by observation_enhancer.apply. A differently-shaped legacy table of the same name in bible_research.db is inactive. | **none recorded** |
| `run_batch` | one row per batch/chunk attempt of a live multi-batch (or single-call) run | The batch/step-level control table (escalation #1756, researcher-approved design 2026-09-18) -- resume/skip (a new run_id skips any batch a PRIOR run_id already committed, via UNIQUE(step, selector_key, batch_content_key)), crash safeguard (a 'running' row with no terminal update proves a dead run), and live progress monitoring (BatchProgress.ps1) for every long-running LLM-calling step. lib/batchcontrol.py is the sole writer. Prompted directly by M49's Stage 1 verse-reading run needing two full from-scratch restarts this session with no way to skip already-paid-for batches. | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## D3. D3 Claims and characteristics: the claims already resting on the scope; table data only

What is already claimed, read against the characteristics, so D4 tests it rather than re-claims it.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `narrative_register.find` | narrative-register / Narrative-Register.ps1 | read-only search (-Verse -Chapter -Section -Claim -Text -Escalation -Thread -Verdict -NotInNarrative -ToldInMoreThanOne) -- see lib/narrativeregister.py (escalation #2110) | - | refused: terminal |
| `narrative_register.history` | narrative-register / Narrative-Register.ps1 | read-only: every change to a claim and to the passages that tell it -- see lib/narrativeregister.py (escalation #2110) | - | refused: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

**None.** No method rule or quality check is tied to any step of this stage.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:77 | claims-register-keeps-narrative-honest | study_active | path:_analytics/essay/**; ps:Narrative-Register.ps1; ps:Reading.ps1 | yes, at Narrative-Register.ps1 |
| B:112 | narrative-is-story-claims-are-derived | study_active | path:_analytics/essay/** | **no** |
| B:76 | narrative-claim-register-kept-in-iba-db | study_active | ps:Narrative-Register.ps1; path:_analytics/essay/**; ps:Reading.ps1 | yes, at Narrative-Register.ps1 |
| B:114 | synergise-from-tables-not-memory | study_active | general:general; ps:Reading.ps1 | only at session start (general) |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `narrative.claim_register_path` | "_analytics/essay/spirit_soul_body/narrative-claim-register.md" | the published claim register (Narrative-Register.ps1 -Action Export): index notes, chapters with their sections and the claims told there, the original essay claims, the claims not in the narrative, the Tally. One fixed name, outside inner-being-narrative/, so it is never copied to learning4comfort (escalation #2110, spec sec8) |
| `narrative.register_report_dir` | "outputs/narrative-register" | where Narrative-Register.ps1 -Action Find/History/Check write their dated reports (escalation #2110) |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `narrative_claim_status` | current, withdrawn, held |
| `narrative_claim_verdict` | Stands, Widened, Restated, Withdrawn, Held, Added, New, Removed, Corrected |
| `narrative_claim_source_kind` | verse, lexical, science, study file, observation |

### What the rows above do not show

- **No step reads a scope's claims as a phase of its own.** `reading.synergy` reads them inside D4; `narrative_register.find` reads them on demand.

## D4. D4 Verses in context: observe, then claims (with 0.GAP post-claims), then narrate

The only phase that reads verse text and passage: each verse read in its passage (the role guide), then observations carried into claims, then the narrative told from the claims.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `reading.record` | reading / Reading.ps1 | gate 1 work: the gap JSON's records written (new observations grounded and quote-checked, faces on strand hits, responses on open items, new open items through the open-item tool) and the ids written back into the file -- see lib/reading.py (escalation #2228) | escalation_thread_item (iba), escalation_thread_item_verse (iba), ib_node (iba), ib_observation (iba), reading (iba), reading_strand_hit (iba) | refused: terminal |
| `reading.check` | reading / Reading.ps1 | the gate the reading is at, checked from the tables: gate 1 (every gap item has an id that exists or a reason; the verses are then marked analysed) or gate 2 (every observation carried or disposed, every claim told or held, every matched open item settled) -- see lib/reading.py (escalation #2228) | reading (iba), verse_meta (iba) | refused: terminal |
| `reading.synergy` | reading / Reading.ps1 | gate 2 input: the synergy JSON built by reading all the tables for the scope (observations, claims, blocks, matched open items), never memory -- see lib/reading.py (escalation #2228) | reading (iba) | refused: terminal |
| `reading.apply` | reading / Reading.ps1 | gate 2 work: the synergy JSON written -- claims new, edited, withdrawn, each source naming its observation; dispositions; tellings; blocks rewritten whole; open items settled or carried forward -- see lib/reading.py (escalation #2228) | escalation_thread_item (iba), escalation_thread_item_verse (iba), ib_observation (iba), narrative_chapter (iba), narrative_citation (iba), narrative_claim (iba), narrative_claim_change (iba), narrative_claim_source (iba), narrative_claim_telling (iba), narrative_section (iba), narrative_update (iba), narrative_update_ref (iba), reading (iba), verse_meta (iba) | refused: terminal |
| `narrative_register.add_claim` | narrative-register / Narrative-Register.ps1 | a new claim with its sources (-Text -BeyondText -Source) -- see lib/narrativeregister.py (escalation #2110) | narrative_claim (iba), narrative_claim_change (iba), narrative_claim_source (iba) | refused: terminal |
| `narrative_register.edit` | narrative-register / Narrative-Register.ps1 | changes a claim's wording, verdict or sources; the trigger logs it -- see lib/narrativeregister.py (escalation #2110) | narrative_claim (iba), narrative_claim_change (iba), narrative_claim_source (iba) | refused: terminal |
| `narrative_register.withdraw` | narrative-register / Narrative-Register.ps1 | withdraws a claim (the row stays, with its history) -- see lib/narrativeregister.py (escalation #2110) | narrative_claim (iba), narrative_claim_change (iba) | refused: terminal |
| `narrative_register.tell` | narrative-register / Narrative-Register.ps1 | links a claim to the block that tells it (-Chapter -Section <heading>/<Parent > Heading>) -- see lib/narrativeregister.py (escalation #2110, #2172) | narrative_claim (iba), narrative_claim_change (iba), narrative_claim_telling (iba) | refused: terminal |
| `narrative_register.untell` | narrative-register / Narrative-Register.ps1 | removes a claim's telling from a block (status removed; the row stays) -- see lib/narrativeregister.py (escalation #2110, #2172) | narrative_claim (iba), narrative_claim_change (iba), narrative_claim_telling (iba) | refused: terminal |
| `narrative_register.edit_note` | narrative-register / Narrative-Register.ps1 | edits one block of the index text -- see lib/narrativeregister.py (escalation #2110) | narrative_index_note (iba) | refused: terminal |
| `narrative_register.edit_section` | narrative-register / Narrative-Register.ps1 | edits a section row (heading, level, parent, order); a rename keeps the old row and moves its current passages to the new one -- see lib/narrativeregister.py (escalation #2110) | narrative_chapter (iba), narrative_claim_change (iba), narrative_claim_telling (iba), narrative_passage (iba), narrative_section (iba) | refused: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

**None.** No method rule or quality check is tied to any step of this stage.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:116 | read-the-verse-first | study_active | general:general; ps:Reading.ps1 | yes, at Reading.ps1 |
| B:73 | read-verse-by-role-of-each-mcode-word | study_active | path:_analytics/** | **no** |
| B:72 | route-verses-hib-other-beings-data-only | study_active | path:_analytics/** | **no** |
| B:69 | let-scripture-speak-no-imputed-synthesis | study_active | path:_analytics/** | **no** |
| B:109 | read-verses-before-asking | study_active | path:_analytics/** | **no** |
| B:110 | surface-is-the-sensitivity-lens | study_active | path:_analytics/** | **no** |
| B:89 | change-of-character-recorded | study_active | path:_analytics/** | **no** |
| B:79 | reading-file-placement-per-verse | study_active | path:_analytics/** | **no** |
| B:91 | narration-probes-not-restates | study_active | path:_analytics/essay/** | **no** |
| B:92 | no-unnecessary-holding | study_active | path:_analytics/** | **no** |
| B:4 | inferential-not-confirmed | always | general:* | only at session start (general) |
| B:36 | no-unsubstantiated-superlatives | always | general:* | only at session start (general) |
| B:114 | synergise-from-tables-not-memory | study_active | general:general; ps:Reading.ps1 | yes, at Reading.ps1 |
| B:76 | narrative-claim-register-kept-in-iba-db | study_active | ps:Narrative-Register.ps1; path:_analytics/essay/**; ps:Reading.ps1 | yes, at Narrative-Register.ps1, Reading.ps1 |
| B:77 | claims-register-keeps-narrative-honest | study_active | path:_analytics/essay/**; ps:Narrative-Register.ps1; ps:Reading.ps1 | yes, at Narrative-Register.ps1, Reading.ps1 |
| B:112 | narrative-is-story-claims-are-derived | study_active | path:_analytics/essay/** | **no** |
| B:88 | weave-not-fit | study_active | path:_analytics/** | **no** |
| B:90 | weaving-carries-meaning | study_active | path:_analytics/essay/** | **no** |
| B:85 | prose-only-on-instruction | study_active | path:_analytics/essay/**; ps:Prose.ps1 | **no** |
| B:86 | narrative-reset-and-weave-record | study_active | path:_analytics/essay/** | **no** |
| B:87 | narrative-chapter-text-rules | study_active | path:_analytics/essay/** | **no** |
| B:115 | open-item-has-a-clear-purpose | always | ps:Open-Item.ps1; ps:Escalation.ps1; ps:Reading.ps1 | yes, at Reading.ps1 |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `reading.gap_types` | {"not_read": {"phase": "recording", "records_in": ["ib_observation"], "guide": "A verse with no observation and no strand face. Read it in its passage; record what it states about the inner being (a new observation), name an existing observation that already covers it, or give the reason it holds nothing."}, "read_in_files_only": {"phase": "recording", "records_in": ["ib_observation"], "guide": "A verse the cluster files read (their lines are given) with no observation in the tables. Carry the reading into a table: a new observation from what the files say and the verse states, an existing observation, or the reason the files' reading holds nothing."}, "hit_unread": {"phase": "recording", "records_in": ["reading_strand_hit"], "guide": "A strand hit with no face and no reason. Give the hit its face (and the observation it goes into), or the reason it has none."}, "meaning_missing": {"phase": "recording", "records_in": ["strong_meaning_tree", "strong_lexicon"], "guide": "A word in scope with no meaning senses (or, for Greek, no Mounce entry). Pull it through the spine route and name the row, or give the reason it is not needed for this reading."}, "open_item": {"phase": "recording", "records_in": ["ib_observation", "escalation_thread_item_response"], "guide": "An open item that matches the scope: read for what it asks, and record what the reading found (an observation, or a response of kind touched). It is not closed here: closing is decided in synergy (gate 2)."}, "observed_no_claim": {"phase": "synergy", "records_in": ["narrative_claim", "ib_observation"], "guide": "An observation no current claim rests on: carry it by a claim, or dispose of it (held on an item, silent, withdrawn) with a reason. Gate 2's work, from the tables."}, "claim_not_told": {"phase": "synergy", "records_in": ["narrative_claim_telling"], "guide": "A current claim no block tells: tell it in a block, or hold it with a reason. Gate 2's work, from the tables."}} | the reading's gap types (cfg_enum reading_gap_type): each one's phase (recording: in the gap JSON, gate 1; synergy: gate 2), the table(s) it records into and the guide text written into its section; adding a gap type is an enum value and an entry here (escalation #2228, design v2 sec 2) |
| `strand_reading.output_dir` | "outputs/strand-reading" | where Strand-Reading.ps1 writes each strand's context, gather and account files, one folder per strand (escalation #2172) |
| `session_close.reading_scope` | ["_analytics/Clusters/*", "_analytics/cross-cluster-web/*"] | #2173 SC5(d): where reading files live (fnmatch; * crosses folders) |
| `session_close.reading_file_pattern` | "(reading/account/ledger/weave)" | #2173 SC5(d): a changed file in reading_scope whose name matches this is a reading file and needs a placement per verse it names |
| `session_close.placement_kinds` | ["told", "claim", "data", "forward", "held", "parked", "context"] | #2173 SC5(d), Q2: the first word of a verse's placement in a reading file; forward/held name an open OT-nn.n or #nnnn; told is checked against the narrative |
| `narrative.claim_changes_path` | "_analytics/essay/spirit_soul_body/narrative-claim-changes.md" | the published change log, by update, newest first, and the Structure log (Export; escalation #2110, spec sec8) |
| `narrative.book_alias_map` | {"1ch": "1Ch", "1chr": "1Ch", "1chron": "1Ch", "1chronicles": "1Ch", "1co": "1Cor", "1cor": "1Cor", "1corinthians": "1Cor", "1jn": "1Jo", "1jo": "1Jo", "1john": "1Jo", "1kgs": "1Ki", "1ki": "1Ki", "1kin": "1Ki", "1kings": "1Ki", "1pe": "1Pe", "1pet": "1Pe", "1peter": "1Pe", "1sa": "1Sa", "1sam": "1Sa", "1samuel": "1Sa", "1th": "1Th", "1thes": "1Th", "1thess": "1Th", "1thessalonians": "1Th", "1ti": "1Ti", "1tim": "1Ti", "1timothy": "1Ti", "2ch": "2Ch", "2chr": "2Ch", "2chron": "2Ch", "2chronicles": "2Ch", "2co": "2Cor", "2cor": "2Cor", "2corinthians": "2Cor", "2jn": "2Jo", "2jo": "2Jo", "2john": "2Jo", "2kgs": "2Ki", "2ki": "2Ki", "2kin": "2Ki", "2kings": "2Ki", "2pe": "2Pe", "2pet": "2Pe", "2peter": "2Pe", "2sa": "2Sa", "2sam": "2Sa", "2samuel": "2Sa", "2th": "2Th", "2thes": "2Th", "2thess": "2Th", "2thessalonians": "2Th", "2ti": "2Ti", "2tim": "2Ti", "2timothy": "2Ti", "3jn": "3Jo", "3jo": "3Jo", "3john": "3Jo", "act": "Act", "acts": "Act", "amo": "Amo", "amos": "Amo", "canticles": "Song", "col": "Col", "colossians": "Col", "dan": "Dan", "daniel": "Dan", "deu": "Deu", "deut": "Deu", "deuteronomy": "Deu", "dt": "Deu", "ecc": "Ecc", "eccl": "Ecc", "ecclesiastes": "Ecc", "eph": "Eph", "ephesians": "Eph", "est": "Est", "esth": "Est", "esther": "Est", "ex": "Exo", "exo": "Exo", "exod": "Exo", "exodus": "Exo", "eze": "Eze", "ezek": "Eze", "ezekiel": "Eze", "ezk": "Eze", "ezr": "Ezr", "ezra": "Ezr", "gal": "Gal", "galatians": "Gal", "gen": "Gen", "genesis": "Gen", "hab": "Hab", "habakkuk": "Hab", "hag": "Hag", "haggai": "Hag", "heb": "Heb", "hebrews": "Heb", "hos": "Hos", "hosea": "Hos", "isa": "Isa", "isaiah": "Isa", "jam": "Jam", "james": "Jam", "jas": "Jam", "jdg": "Judg", "jdgs": "Judg", "jer": "Jer", "jeremiah": "Jer", "jhn": "Joh", "jn": "Joh", "job": "Job", "joe": "Joe", "joel": "Joe", "joh": "Joh", "john": "Joh", "jol": "Joe", "jon": "Jon", "jonah": "Jon", "jos": "Jos", "josh": "Jos", "joshua": "Jos", "jud": "Jude", "jude": "Jude", "judg": "Judg", "judges": "Judg", "lam": "Lam", "lamentations": "Lam", "lev": "Lev", "leviticus": "Lev", "lk": "Luk", "luk": "Luk", "luke": "Luk", "mal": "Mal", "malachi": "Mal", "mar": "Mar", "mark": "Mar", "mat": "Mat", "matt": "Mat", "matthew": "Mat", "mic": "Mic", "micah": "Mic", "mk": "Mar", "mrk": "Mar", "mt": "Mat", "nah": "Nah", "nahum": "Nah", "neh": "Neh", "nehemiah": "Neh", "num": "Num", "numbers": "Num", "oba": "Obd", "obad": "Obd", "obadiah": "Obd", "obd": "Obd", "phi": "Phili", "phil": "Phili", "phile": "Phile", "philemon": "Phile", "phili": "Phili", "philippians": "Phili", "phlm": "Phile", "phm": "Phile", "php": "Phili", "pro": "Pro", "prov": "Pro", "proverbs": "Pro", "prv": "Pro", "ps": "Psa", "psa": "Psa", "psalm": "Psa", "psalms": "Psa", "pss": "Psa", "qoh": "Ecc", "rev": "Rev", "revelation": "Rev", "rom": "Rom", "romans": "Rom", "rut": "Rut", "ruth": "Rut", "rv": "Rev", "sng": "Song", "song": "Song", "songofsolomon": "Song", "songofsongs": "Song", "sos": "Song", "tit": "Tit", "titus": "Tit", "zec": "Zec", "zech": "Zec", "zechariah": "Zec", "zep": "Zep", "zeph": "Zep", "zephaniah": "Zep"} | book name or abbreviation -> the book code iba.db verse.reference uses. Keys are lower case with spaces and dots removed (lib/narrativeregister.py parse_refs normalises the same way). The chapters write full names (2 Corinthians), the register short codes (2Co), verse uses its own (2Cor) -- escalation #2110, spec sec1, sec3.8 |
| `narrative.inner_being_style_guide_path` | "Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md" | Authoritative style, format and evidence guide for all IBA-line reader-facing narrative (inner-being narrative chapters, strand write-ups, book narratives). Consolidates the 2026-04..07 prose/essay/narrative guides with the researcher rulings to 2026-10-01: first-person voice, weave not fit, change of character, let Scripture speak for itself, prose supported by bullets, titles name the subject only, external parties dealt with per phenomenon (#1921, #1924). Read before writing or revising any narrative text. |
| `narrative.quote_min_words` | 2 | #2173 G14: quoted parts shorter than this many words are not quote-checked |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `ib_observation.stage` | verse-reading, char-subgroup, char-reading, char-answers, char-synergy, strand-reading |
| `ib_observation.tag` | verse-grouping, difference-inference, surface-gloss-divergence, no-human-context, data-error, alternative-meaning, could-not-resolve, answered-no-flag, tightly-related, no-direct-connection, qualifier-for-term, no-impact, not-related-to-meaningful-word, sole-mcode-in-verse, cluster-pole-negative, cluster-pole-positive, attested-pre-nt, nt-coinage, needs_adjacent_verse_context, elevation-candidate, key-statement |
| `ib_observation.basis` | read, stated |
| `ib_observation.status` | resolved, needs-corroboration, open, silent, withdrawn, draft |
| `reading_strand_item_source` | matched, raised |
| `reading_strand_state` | closed, open, withdrawn, superseded |
| `narrative_claim_change_kind` | claim created, claim restated, verdict changed, claim withdrawn, telling added, telling changed, telling removed, passage moved, renumbered, edited |
| `narrative_claim_origin` | original essay, narrative |
| `narrative_claim_status` | current, withdrawn, held |
| `narrative_claim_verdict` | Stands, Widened, Restated, Withdrawn, Held, Added, New, Removed, Corrected |
| `narrative_change_basis` | recorded, reconstructed, direct edit |
| `narrative_update_ref_kind` | escalation, thread, thread item |
| `narrative_telling_kind` | in full, in part, pointer |
| `narrative_telling_status` | current, removed, superseded |

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `escalation_thread_item` | one row per thread item | One row per item of a thread (type='thread' escalation): what a strand or task is matched against, and the item's current status only: open, or settled as closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread). Every response, including each settlement, is a row in escalation_thread_item_response. escalation #2000 (proposal v3 sec3.2, sec3.4; thread lifecycle, BUILD.md s338). | **none recorded** |
| `escalation_thread_item_verse` | one row per verse of an open item's target | #2236: the verses an open item is about, so it matches a scope on these verses and never on a whole cluster | **none recorded** |
| `ib_node` | one row per grounding element an ib_observation cites (strong/verse/subgroup/cluster/question/another observation) | The cluster-reading pack's own grounding table (#1692, design-complete 2026-09-14). Makes 'no way to check a finding's grounding' structurally impossible via the CHECK constraint + the mandatory coverage self-check (#1692 SS2: every strong/verse in a subgroup's membership must be grounded by >=1 ib_node row, checked at LLM generation time and independently re-checked by the recording pass at load time). | **none recorded** |
| `ib_observation` | one row per observation | One observation: a typed finding from a reading, with its text, meaning, implication, basis, parties and status (draft or withdrawn), grounded on verses, strongs, subgroups, clusters or other observations through ib_node. Written by stage: verse-reading (lexical.meaning, lexical.relational), char-reading, char-answers and char-subgroup (cluster.reading, cluster.answer, cluster.subgroup), strand-reading (strand_reading.record, strand_reading.derive), and enhanced by observation_enhancer.apply. A differently-shaped legacy table of the same name in bible_research.db is inactive. | **none recorded** |
| `narrative_chapter` | one row per chapter or sub-chapter | One row per chapter or sub-chapter of the inner-being narrative, and the authority for which chapters exist, their reading order and what each is for (kind, purpose, purpose_ref). Changed only through Narrative-Register.ps1 (AddChapter, EditChapter); every structural change is logged in the Structure log. A renumbering changes chapter_no on the row; every record keeps its link to the chapter, so the history follows the chapter, not the number. The copy to learning4comfort publishes the active chapters' current files. escalation #2110 spec sec3.1; #2155 | **none recorded** |
| `narrative_citation` | one row per verse cited in a passage of the story | The citation index: every verse cited anywhere in the story, by passage. With narrative_claim_source it answers, for any verse, where it is cited and which claims rest on it. A reference that cannot be resolved is kept with verse_id NULL, never dropped. escalation #2110, spec sec3.8 | **none recorded** |
| `narrative_claim` | one row per claim | The register: one row per claim. A claim is a statement derived from sources (verses, later science) that goes beyond their mere text, held in its own plain wording. A quotation is not a claim. escalation #2110, spec sec3.3 (researcher, round 3) | **none recorded** |
| `narrative_claim_change` | one row per change to a claim or to a passage that tells it | The change log, many rows per claim: every change to a claim, and to each passage that tells it, with enough before and after to review the impact without opening another file (Q-F). A change to one passage that tells three claims writes three rows. escalation #2110, spec sec3.7 | **none recorded** |
| `narrative_claim_source` | one row per source of a claim | What a claim rests on: a verse (one row per verse; ranges and lists expanded), a lexical source, science (later), or a study file. escalation #2110, spec sec3.4 | **none recorded** |
| `narrative_claim_telling` | one row per claim told in a block (passage rows before #2172 are history) | The link between a claim and the block (narrative_section) that tells it, many to many. escalation #2110, spec sec3.5; per block since #2172 | **none recorded** |
| `narrative_index_note` | one row per block of index text | The parts of the old narrative index that are text, not tables (researcher direction, theme and frame, rules applied, how later work updates the narrative, source files, verse check), one row per block, editable. escalation #2110, spec sec3.9 | **none recorded** |
| `narrative_passage` | one row per passage that tells at least one claim | History since #2172: the paragraphs that told claims before the narrative was held as blocks (narrative_section.block_text). No longer written; a claim is told by a block (narrative_claim_telling.section_id). escalation #2110, spec sec3.2 | **none recorded** |
| `narrative_section` | one row per section heading in a chapter | One row per section heading in a chapter, current or past. A chapter's opening, before any heading, has its own row (level 0). escalation #2110, spec sec3.2 | **none recorded** |
| `narrative_update` | one row per weave or recorded pass | One row per weave or recorded pass on the narrative, with its instruction, sources, notes and quote check. Imported updates keep the register version that added them. escalation #2110, spec sec3.6 | **none recorded** |
| `narrative_update_ref` | one row per escalation or thread an update names | The escalations, threads and thread items an update names. escalation #2110, spec sec3.6 | **none recorded** |
| `reading` | one row per reading: the work on one scope | #2228: a reading opened from a scope request and served by the escalation that anchors it; it passes three gates in order (recorded, synergised, published), each checked by Reading.ps1 | **none recorded** |
| `reading_strand_hit` | one row per hit: a strand strong in a verse | #2172 safeguard 1: every hit has a face, or a stated reason it has none, before the strand can close; the observation the hit went into | **none recorded** |
| `verse_meta` | one row per verse (1:1 with verse.id) | Verse-level base-data companion to `verse` -- collates language/testament/chapter/verse_num/passage linkage once at the right grain, instead of denormalizing per-code (the old `language` source) or leaving facts homeless (`genre`, `lexical_complete_at`). Auto-synced via 4 triggers on verse/verse_lexical/verse_passage inserts and verse.deleted updates -- never written to directly by application code. Escalation #1608, 2026-09-09. | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## PUBLISH. Publish: the touched chapters published; the chapter structure; the programme prose

The narrative published from the database and copied out; chapters kept through the register; the researcher's programme prose.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `reading.publish` | reading / Reading.ps1 | gate 3: the chapters the reading touched published from the database, copied to the learning4comfort inbox and checked byte-identical -- see lib/reading.py (escalation #2228) | narrative_chapter (iba), reading (iba) | refused: terminal |
| `reading.account` | reading / Reading.ps1 | the reading from the tables: its state, each gate's gaps (read-only) -- see lib/reading.py (escalation #2228) | - | refused: terminal |
| `narrative_register.add_chapter` | narrative-register / Narrative-Register.ps1 | adds a chapter row (-Chapter -Title -Kind -Purpose -PurposeRef -After/-ReadingOrder -CurrentFile), moves the later chapters down, writes its section rows from the file and a Structure log entry -- see lib/narrativeregister.py (escalation #2155) | narrative_chapter (iba), narrative_claim_change (iba), narrative_section (iba), narrative_update (iba) | refused: terminal |
| `narrative_register.edit_chapter` | narrative-register / Narrative-Register.ps1 | edits a chapter row (number, title, kind, purpose, ruling, state, current file, place); a structural change is logged in the Structure log -- see lib/narrativeregister.py (escalation #2110, #2155) | narrative_chapter (iba), narrative_claim_change (iba), narrative_update (iba) | refused: terminal |
| `narrative_register.check` | narrative-register / Narrative-Register.ps1 | read-only: chapters, sections and passage anchors against the files on disk; chapters with no kind or purpose, duplicate reading orders, stray files, direct-edit rows -- see lib/narrativeregister.py (escalation #2110, #2155) | - | refused: terminal |
| `narrative_register.export` | narrative-register / Narrative-Register.ps1 | regenerates the three published files (spec sec8), the register opening with the Chapters table -- see lib/narrativeregister.py (escalation #2110, #2155) | - | refused: terminal |
| `narrative_register.quote_check` | narrative-register / Narrative-Register.ps1 | #2173 G14: every quotation in -File (or in the lines it added against -Against) must be in the ESV text -- see lib/quotecheck.py | - | quotes-failing: terminal; refused: terminal |
| `prose.extract` | prose / Prose.ps1 | Programme-prose extract (JSON/MD/DOCX) | - | - |
| `prose.search` | prose / Prose.ps1 | FTS/plain search over prose_section | - | - |
| `prose.export_chapter` | prose / Prose.ps1 | Export a chapter to editable .md | - | - |
| `prose.import_chapter` | prose / Prose.ps1 | Turn an edited .md into a patch file (writes no DB row itself) | - | - |
| `prose.apply_patch` | prose / Prose.ps1 | Apply a reviewed PROSE patch (from import_chapter, flag_fix_apply or set_status) to bible_research.db in one transaction, each write logged in record_change_log; -DryRun applies and rolls back (escalation #2212, option A) | - | - |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

**None.** No method rule or quality check is tied to any step of this stage.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:78 | narrative-chapters-change-only-through-the-register | study_active | ps:Narrative-Register.ps1; path:_analytics/essay/**; ps:Reading.ps1 | yes, at Narrative-Register.ps1, Reading.ps1 |
| B:85 | prose-only-on-instruction | study_active | path:_analytics/essay/**; ps:Prose.ps1 | yes, at Prose.ps1 |
| B:52 | prose-section-session-a-replace-author-gate | always | ps:Prose.ps1 | yes, at Prose.ps1 |
| B:53 | prose-section-two-patch-ordering | always | ps:Prose.ps1 | yes, at Prose.ps1 |
| B:55 | prose-section-type-creation-requires-researcher-instruction | always | ps:Prose.ps1 | yes, at Prose.ps1 |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `narrative.chapter_kinds_without_file` | ["part heading", "deferred"] | Escalation #2155: the narrative_chapter kinds that have no chapter file of their own (a part heading, a deferred placeholder). Narrative-Register.ps1 AddChapter accepts these with no -CurrentFile; every other kind needs a file on disk. |
| `narrative.citation_index_path` | "_analytics/essay/spirit_soul_body/narrative-citation-index.md" | the published citation index: every verse cited in the narrative, in canonical order, with where it is cited and which claims rest on it (Export; escalation #2110, spec sec8) |
| `narrative.copy_source_dir` | "_analytics/essay/spirit_soul_body/inner-being-narrative" | Escalation #1941 (researcher, 2026-10-04): the folder whose current top-level .md files Copy-NarrativeToLearning4Comfort.ps1 copies to the learning4comfort inbox. archive/ is never copied. |
| `narrative.learning4comfort_inbox_dir` | "C:/learning4comfort/publication-inbox/the_inner_being" | Escalation #1941 (researcher, 2026-10-04: folder the_inner_being): where Copy-NarrativeToLearning4Comfort.ps1 copies the current narrative files. Local-only staging owned by the learning4comfort repo, which prepares, reviews and publishes. |
| `governance.no_direct_github_publish` | "Bible_study_projects never publishes to GitHub itself (no Actions workflow, no push to a site repo). Narrative files reach learning4comfort only by Copy-NarrativeToLearning4Comfort.ps1, run on completion of a section of work, on request, and at /session-close when a chapter changed in the session (SC12)." | Escalation #1941, researcher verbatim 2026-10-04: "A) this project (bible_study_projects) does not publish directly to github b) on completion of a section of work or on request, the current ...inner-being-narrative files are copied to C:\\learning4comfort\\publication-inbox\\... c) session-close trigger the copy in b)". See CLAUDE.md section 12 and GOVERNANCE.md. |
| `report.cluster_folder_naming_convention` | "_analytics/Clusters holds one subfolder for EVERY row of cluster (deleted=0) -- M-, T- and FLAG codes alike; a folder is created whenever a cluster row is added. ALL output relating to a cluster (analysis, readings, handoffs, inputs/extract CSVs, decisions) is filed in that cluster's subfolder, prior versions in its archive/ subfolder. Name = {cluster.cluster_code} - {cluster.short_name lowercased, & and all other punctuation dropped, spaces as single hyphens} -- e.g. M02 - anger-wrath, M47 - inner-seat, M81 - memory-act, T7 - party-divine. Cross-cluster/all-cluster files (report.cluster_path, cluster.quality_report_path) stay at the _analytics/Clusters root. Single-cluster verse analysis -- including a fan-out strand, unit ledgers, cross-ledger overviews and proposals that read one cluster's vocabulary -- is filed in that cluster's subfolder, never in _analytics/cross-cluster-web/. Only TRUE multi-cluster work (a strand whose subject spans clusters, such as origin-of-thought, or the cross-cluster analyses) is filed in _analytics/cross-cluster-web/." | the filing rule for all per-cluster output: one subfolder per cluster under _analytics/Clusters, keyed to cluster.cluster_code, so cluster work never drifts into outputs/ or research/ |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `narrative_chapter_kind` | front matter, chapter, part heading, opening, activity, key characteristic, other beings, deferred |
| `narrative_chapter_state` | draft, draft + held, empty, deferred |
| `prose_section_status` | draft, in_review, approved, archived |
| `prose_section_author` | claude_ai, claude_code, researcher |

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `narrative_chapter` | one row per chapter or sub-chapter | One row per chapter or sub-chapter of the inner-being narrative, and the authority for which chapters exist, their reading order and what each is for (kind, purpose, purpose_ref). Changed only through Narrative-Register.ps1 (AddChapter, EditChapter); every structural change is logged in the Structure log. A renumbering changes chapter_no on the row; every record keeps its link to the chapter, so the history follows the chapter, not the number. The copy to learning4comfort publishes the active chapters' current files. escalation #2110 spec sec3.1; #2155 | **none recorded** |
| `narrative_claim_change` | one row per change to a claim or to a passage that tells it | The change log, many rows per claim: every change to a claim, and to each passage that tells it, with enough before and after to review the impact without opening another file (Q-F). A change to one passage that tells three claims writes three rows. escalation #2110, spec sec3.7 | **none recorded** |
| `narrative_section` | one row per section heading in a chapter | One row per section heading in a chapter, current or past. A chapter's opening, before any heading, has its own row (level 0). escalation #2110, spec sec3.2 | **none recorded** |
| `narrative_update` | one row per weave or recorded pass | One row per weave or recorded pass on the narrative, with its instruction, sources, notes and quote check. Imported updates keep the register version that added them. escalation #2110, spec sec3.6 | **none recorded** |
| `reading` | one row per reading: the work on one scope | #2228: a reading opened from a scope request and served by the escalation that anchors it; it passes three gates in order (recorded, synergised, published), each checked by Reading.ps1 | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## RECORD. The observation record across D1 to D4 (not a phase): ib_observation, ib_node, the enhancer, the question catalogue

Every phase that writes, grounds, corrects, enhances or disposes of an observation, and what the record holds.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `lexical.meaning` | verse-lexical / VerseLexical.ps1 | The verse-reading stage, WORD-LEVEL HALF (#1711 original build; narrowed to word-level-only by the #1860 split, 2026-09-23): per-cluster, pre-subgroup Layer 2. Reads all 3 meaning sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) as complementary evidence for every strong the cluster's role-annotated word list covers (verse_lexical.role, including currently-unwired role-T2/T6/T10-T15 tags, not just the mechanically-wired subset), and answers M0.1 (Name and Naming) and M0.5 (Lexical and Semantic Analysis, incl. M0.5.11) from wa_obs_question_catalogue -- word-level only now; the relational family (M0.6.5/M0.6.6/D7.7.1/M0.7/M0.8.1) moved to the new lexical.relational step, which requires this step's own output as a precondition (readiness gate). Assembles the LLM payload and estimates cost; the live API call and the DB write are separate, explicit steps (cost preview before spend, never silent). | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `lexical.relational` | verse-lexical / VerseLexical.ps1 | The verse-reading stage, RELATIONAL HALF (#1860 split, 2026-09-23 -- researcher, verbatim: 'we must split the word questions and answers and the relational answers into separate processes. the relational process depends on the word work, and doing it in the same session can only result in errors.'). Per-cluster, pre-subgroup Layer 2, run AFTER lexical.meaning has covered the same verses -- a hard readiness gate refuses to run against any verse whose M-code words don't all have a committed word-level (M0.1/M0.5) observation yet. Answers M0.6.5 (relational, single-vantage), M0.6.6 (whole-network synthesis), D7.7.1 (operation-anchored permeability), M0.7.1-16 (verse substantiation), M0.8.1 (T2/T3 elevation flag), cluster-agnostic (every M-code word in the verse, not just this cluster's own home strong(s)). Grounds on the COMMITTED word-level ib_observation rows for each verse+strong (the researcher's own approval, #1860 v3: 'the base data must in any case be included for relational phase to be successful' -- so the raw lexicon (meaning_sources_by_strong) is ALSO sent alongside the committed findings, never one instead of the other). This is the true final stage of verse-reading -- the cluster.status t_cluster_assignment_completed -> ready_for_subgroup_allocation transition check runs here now, not in lexical.meaning. | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `cluster.subgroup` | cluster-reading / ClusterSubgroup.ps1 | The char-subgroup stage (#1690/#1693, process b): reads a cluster's full member-strong list -- gloss/surface plus its already-captured verse-reading (Stage 1) observations -- in ONE session (never streamed/batched, rule a requires the whole cluster read before any assignment), and groups strongs into meaning-based subgroups (max 10, FLAG excluded). Writes cluster_subgroup/cluster_subgroup_strong via the recording pass; advances cluster.status from ready_for_subgroup_allocation to ready_for_reading on success. | cluster_subgroup (iba), cluster_subgroup_strong (iba), ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `cluster.reading` | cluster-reading / ClusterSubgroup.ps1 | The char-reading stage (#1682/#1706 Phase F, process c): given one subgroup's member strongs, reads every occurrence corpus-wide (no sampling) plus all meaning sources, using Stage 1 (verse-reading) and Stage 2 (char-subgroup) observations as grounding, and synergises the similar/different contextual meaning of the subgroup's OWN member strongs against each other. Writes ib_observation/ib_node via the recording pass (stage='char-reading'); per-strong completeness is computed by code, not LLM-self-reported; advances cluster_subgroup.status from ready_for_reading to ready_for_answer on success. | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `cluster.answer` | cluster-reading / ClusterSubgroup.ps1 | The char-answers stage (#1682 §4A / #1706 Phase F, process d): given one subgroup's member strongs and Stage 1/2/3's own accumulated observations, answers the catalogue's characteristic-grain question battery (52 live questions, science-extract-dependent and Stage-1-owned D7.7.1 excluded), multiple slants where the evidence genuinely differs. Writes ib_observation/ib_node via the recording pass (stage='char-answers'); per-question completeness is computed by code; advances cluster_subgroup.status from ready_for_answer to answer_complete on success. | ib_node (iba), ib_observation (iba), run_batch (iba) | - |
| `reading.record` | reading / Reading.ps1 | gate 1 work: the gap JSON's records written (new observations grounded and quote-checked, faces on strand hits, responses on open items, new open items through the open-item tool) and the ids written back into the file -- see lib/reading.py (escalation #2228) | escalation_thread_item (iba), escalation_thread_item_verse (iba), ib_node (iba), ib_observation (iba), reading (iba), reading_strand_hit (iba) | refused: terminal |
| `reading.apply` | reading / Reading.ps1 | gate 2 work: the synergy JSON written -- claims new, edited, withdrawn, each source naming its observation; dispositions; tellings; blocks rewritten whole; open items settled or carried forward -- see lib/reading.py (escalation #2228) | escalation_thread_item (iba), escalation_thread_item_verse (iba), ib_observation (iba), narrative_chapter (iba), narrative_citation (iba), narrative_claim (iba), narrative_claim_change (iba), narrative_claim_source (iba), narrative_claim_telling (iba), narrative_section (iba), narrative_update (iba), narrative_update_ref (iba), reading (iba), verse_meta (iba) | refused: terminal |
| `observation_enhancer.preview` | observation-enhancer / Observation-Enhancer.ps1 | Read-only. Given -RuleKey, runs that rule's selector_sql against live ib_observation and returns the match count plus a sample of matched rows (id/cluster_code/stage/tag/strong/status/obs_text, up to 10) and the update_json that would be applied. Any rule status -- does not require confirmed. No write. | - | - |
| `observation_enhancer.apply` | observation-enhancer / Observation-Enhancer.ps1 | Given -RuleKey, refuses unless the rule's status is confirmed/active (the researcher's own per-rule confirmation gate, escalation #1778 -- run -Action Preview and confirm via configmaint.propose first). Runs selector_sql, applies update_json to every matched row via UPDATE, logs each (observation, field) change to ib_observation_enhancer_log, and promotes a first-time confirmed rule to active. | cfg_observation_enhancer_rule (iba), ib_observation (iba), ib_observation_enhancer_log (iba) | - |
| `report.obs_catalogue` | catalogue-report / Catalogue-Report.ps1 | structural review of wa_obs_question_catalogue (bible_research.db) on its own -- no join to finding/finding_question_link -- status/deleted lifecycle conflicts, section/tier/question_code/catalogue_version/date_added naming inconsistencies, the live tiered question set for review, and untiered integration candidates | - | - |
| `obs_catalogue.update` | catalogue-update / Catalogue-Update.ps1 | Partial UPDATE of one wa_obs_question_catalogue row (bible_research.db), keyed by obs_id. Every column except obs_id is settable; columns not named in -Set are left untouched. Auto-fills last_modified (now, UTC) and catalogue_version (v2-<today>) when the caller doesn't supply them explicitly -- either is still overridable by naming it in -Set. No history/audit table -- researcher's own call, escalation #1007: 'I dont think there is any history control on this table and I don't think it is necessary.' | wa_obs_question_catalogue (bible_research) | - |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

| Step | Method rules | Quality checks | Delivered to the session |
|---|---|---|---|
| `lexical.meaning` | 10 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `lexical.relational` | 13 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `cluster.subgroup` | 9 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `cluster.reading` | 15 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `cluster.answer` | 8 | 0 | **no** (`cfg_rule_scope` holds no method-rule reference) |

Texts: appendix 2.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:68 | stage1-corrections-only-via-real-rerun | always | ps:VerseLexical.ps1 | yes, at VerseLexical.ps1 |
| B:4 | inferential-not-confirmed | always | general:* | only at session start (general) |
| B:37 | derive-from-instruction-not-prior-unreviewed-output | always | path:_analytics/** | **no** |
| B:67 | bible-research-db-excluded-from-iba-results | always | command:sqlite | **no** |
| B:61 | inactive-tables-never-active-inputs | always | command:sqlite | **no** |
| B:73 | read-verse-by-role-of-each-mcode-word | study_active | path:_analytics/** | **no** |
| B:89 | change-of-character-recorded | study_active | path:_analytics/** | **no** |
| B:114 | synergise-from-tables-not-memory | study_active | general:general; ps:Reading.ps1 | yes, at Reading.ps1 |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `cluster.recording_similarity_threshold` | 0.85 | recordingpass.py record_one_observation: obs_text similarity score (0-1, difflib SequenceMatcher) above which a same-coordinate new observation is treated as a superficial edit of an existing one (align in place) rather than a genuine broaden (new row). Was a hardcoded module constant with no live tuning; promoted to cfg_setting per escalation #1753/#1761 precedent. |
| `report.obs_catalogue_path` | "Workflow/Catalogue/obs-catalogue.md" | where report.obs_catalogue persists its output |
| `ib_observation.meaning_source_aliases` | {"char_reading_observations": "observations", "char_subgroup_observations": "observations", "cluster.cluster_code": "cluster", "cluster_codes": "cluster", "context": "verse-text", "lexicon": "strong_lexicon", "lexicon.lsj": "strong_lexicon.lsj", "lexicon.mounce": "strong_lexicon.mounce", "lsj": "strong_lexicon.lsj", "lsj cross-reference": "strong_lexicon.lsj", "m0.5": "cluster", "morph data": "verse-text", "mounce": "strong_lexicon.mounce", "role list": "role-tags", "role tags": "role-tags", "role-context": "role-tags", "role-tag context": "role-tags", "role-tag reading": "role-tags", "roles_in_verse": "role-tags", "text": "verse-text", "verse": "verse-text", "verse_reading_observations": "observations"} | #2207: each spelling the model has used for a meaning source, mapped to its value in cfg_enum ib_observation.meaning_source; lib/recordingpass.normalise_meaning_source applies it to every new observation |
| `ib_observation.tag_guidance` | {"qualifier-for-term": "the word functions as a MODIFIER (manner, intensifier, or other state/measure/intensity enhancer) of another word's action or quality, rather than naming a disposition/operation/quality in its own right -- e.g. an adverb qualifying HOW an operation is performed, or an adjective qualifying another M-code noun (\"godly\" qualifying \"grief\").", "no-impact": "the occurrence's surface form/stepGloss carries no distinguishing nuance beyond the term's base sense -- a real 'no divergence' finding, not an absence of an answer. Contrast `alternative-meaning` (a real divergence IS found) and `surface-gloss-divergence` (the surface FORM itself, not just the sense, diverges from the dictionary gloss).", "not-related-to-meaningful-word": "the sub-question's target item (a contrast, a related word-form, a co-occurring item the question asks you to identify) genuinely does not exist or apply for this term/verse -- a real negative finding, not a shrug.", "sole-mcode-in-verse": "no other M-code characteristic co-occurs in this verse at all -- distinct from `no-direct-connection`, which means other M-codes ARE present but unrelated to this one.", "tightly-related": "this term's own role connects SUBSTANTIVELY to another M-code term present in the same scope -- a real causal/enabling/response/tension link, or the two share the same acting party -- not just topical co-presence in the same list or catalogue.", "no-direct-connection": "other M-code term(s) ARE present in this scope, but this term's own role does not meaningfully connect to them (no causal link, no shared party, no real interaction) -- distinct from `sole-mcode-in-verse`, where nothing else is present to connect to at all.", "cluster-pole-negative": "this term occupies the negative/negligent pole of a dual-natured cluster (e.g. idleness within a sloth-vs-diligence cluster).", "cluster-pole-positive": "this term occupies the positive/virtuous pole of a dual-natured cluster (e.g. diligence/zeal within a sloth-vs-diligence cluster).", "attested-pre-nt": "the term is attested in classical/pre-NT Greek or Hebrew usage, not coined in the NT period.", "nt-coinage": "the term (or this specific sense of it) has no attestation before the NT -- a NT-period coinage or semantic innovation.", "alternative-meaning": "this SPECIFIC occurrence genuinely supports MORE THAN ONE plausible reading/sense, and the data does not clearly settle which -- real ambiguity, not just a divergence from the usual sense (that's `surface-gloss-divergence` when it's the FORM, or a plain substantive answer when the sense is clear but simply different from elsewhere). State both/all candidate readings in `obs_text`, not just one.", "surface-gloss-divergence": "this occurrence's actual surface form (`span.surface`, the inflected text as it appears) diverges from its `stepGloss` dictionary-standard rendering in a way worth noting -- a form-level fact (e.g. an idiomatic rendering, a metaphorical extension the standard gloss doesn't capture), not a claim of multiple valid readings (`alternative-meaning`).", "no-human-context": "this strong is exclusively a homonym or proper name with no meaningful context for a human reader to analyse -- earmark it as such and stop; do not force an analysis where none is genuinely available (cfg_method_rule 'homonym-no-context-earmarked-and-left').", "data-error": "a data-quality issue noticed while reading (wrong cluster/subgroup membership, a broken span/verse link, a corrupted meaning source) -- flag it here, in its own section; never chase it down or fix it as part of this task (cfg_method_rule 'data-errors-flagged-separately').", "verse-grouping": "several of THIS strong's own occurrences, across different verses, share one genuinely alike reading -- group them under one finding rather than repeating the same point per verse. Requires visibility across a strong's full occurrence set; not meaningful at a single-verse grain.", "difference-inference": "a specific inference or distinction drawn from comparing THIS strong's own occurrences against EACH OTHER (morph-driven distinctions included -- e.g. whether a stem/voice variation across occurrences is meaning-relevant). Requires visibility across a strong's full occurrence set; not meaningful at a single-verse grain.", "could-not-resolve": "a genuine 'couldn't resolve' case -- state in `obs_text` what signal suggests it should be resolvable with further analysis, never a bare flag with no reason.", "needs_adjacent_verse_context": "this verse's own content is insufficient and an adjacent/surrounding verse would help -- state explicitly in `obs_text` what's outstanding and what the follow-up cross-check needs to establish. Resolution happens in a later analytic pass, never fetched ad hoc here.", "elevation-candidate": "this T2/T3-tagged (non-M-code) word's role in THIS verse suggests it names a distinct inner-being characteristic in its own right, not just a supporting role -- state the reason in `obs_text` (M0.8.1 only; escalation #1836). A later, separate process reviews elevation candidates for actual cluster promotion -- this tag only surfaces the candidate, it does not itself change any cluster/role assignment.", "answered-no-flag": "a genuinely plain, substantive answer that matches none of the other tags and has nothing else worth categorising (e.g. a straightforward root-meaning or primary-term identification) -- a LAST RESORT, not a default. Check every observation against the other tags above before reaching for this one."} | #2207: the definition of each ib_observation.tag value, given to the model by every LLM-calling generator stage (lib/taggingguidance.guidance_block). A tag in cfg_enum ib_observation.tag with no definition here is not offered to any stage. |
| `ib_observation.tag_stage_excluded` | {"verse-reading": ["difference-inference", "verse-grouping"], "char-subgroup": [], "char-reading": [], "char-answers": []} | #2207: per generator stage, the tags it may not offer (lib/taggingguidance.tags_for_stage). verse-reading sees one verse at a time, so the cross-occurrence tags are excluded there. |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `ib_observation.stage` | verse-reading, char-subgroup, char-reading, char-answers, char-synergy, strand-reading |
| `ib_observation.tag` | verse-grouping, difference-inference, surface-gloss-divergence, no-human-context, data-error, alternative-meaning, could-not-resolve, answered-no-flag, tightly-related, no-direct-connection, qualifier-for-term, no-impact, not-related-to-meaningful-word, sole-mcode-in-verse, cluster-pole-negative, cluster-pole-positive, attested-pre-nt, nt-coinage, needs_adjacent_verse_context, elevation-candidate, key-statement |
| `ib_observation.status` | resolved, needs-corroboration, open, silent, withdrawn, draft |
| `ib_observation.window` | meaning, action-impact, relational, literary, cognitive, affective, operational, constitutional, origin, scientific, Subgroup, faculty |
| `ib_observation.meaning_source` | strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce, strong_lexicon, verse-text, role-tags, cluster, observations, n/a |
| `ib_observation.basis` | read, stated |
| `wa_obs_question_catalogue.scope` | Word/term (lexical), Verse-context, The verse, Characteristic (HIB behaviour), Characteristic relational, The HIB, Other non-human beings |
| `wa_obs_question_catalogue.tier` | M0, D1, D2, D3, D4, D5, D6, D7, D9, D10, D11, D12, X0, F0, T7 |
| `wa_obs_question_catalogue.status` | active, retired |
| `cfg_observation_enhancer_rule.status` | draft, confirmed, active, retired |

### Observation enhancer rules (`cfg_observation_enhancer_rule`)

| Rule | Status | Selects | Sets | Description |
|---|---|---|---|---|
| 1782-bulk-reset-to-draft | active | `SELECT id FROM ib_observation` | `{"status": "draft"}` | One-time bulk reset (escalation #1782, researcher instruction 2026-09-20): every existing ib_observation row was written under the old resolved-by-default regime, before the status lifecycle was wired up. Reset all of them to draft so they enter the new lifecycle for review, matching what new inserts/edits now do. |
| subgroup-window-for-non-question-observations | active | `SELECT id FROM ib_observation WHERE window IS NULL` | `{"window": "Subgroup"}` | Researcher instruction 2026-09-20: subgroup-level observations not tied to a specific catalogue question (question_code IS NULL) get window=Subgroup instead of NULL. Matches the 137 live rows found during window-value exploration (char-reading 118, char-subgroup 19). |

### What the rows above do not show

- **Writers.** `ib_observation`: lexical.meaning, lexical.relational, cluster.subgroup, cluster.reading, cluster.answer, reading.record, reading.apply, observation_enhancer.apply (`cfg_write_grant`). Two write paths in `recordingpass.py`: `record_one_observation` (D1, D2: same / broaden / new decided by the recording pass) and `record_strand_observations` (D4: Claude's observation as given, `supersedes` withdrawing an earlier row); `set_disposition` changes status in D4's claim step.
- **No status flow** for `ib_observation.status` in `cfg_status_flow`.
- **No change history**: no `cfg_trigger` on `ib_observation` or `ib_node`.
- **The observation rules are a document** (`iba/docs/ib-observation-governing-rules-checklist-v1-20260916.md`); its section 0 is not in config except in part (B:67; tag `could-not-resolve`; method rules 74, 104, 116).

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `cfg_observation_enhancer_rule` | one row per researcher-authored rule | Rule storage for the observation_enhancer utility (escalation #1778) -- pairs a selector_sql (SELECT returning ib_observation.id) with an update_json (column->value) applied via direct UPDATE. Added/edited via configmaint.propose like any other cfg_* row -- NOT a bespoke add/confirm mechanism. status is the researcher's own per-rule confirmation gate (draft -> confirmed, after reviewing a real -Action Preview run -> active, set automatically on first successful apply -> retired). | **none recorded** |
| `cluster_subgroup` |  | Cluster-reading subgroup: a curated group of Strong-numbered codes within one cluster (M-code), the unit of per-subgroup reading/answering in the cluster-reading pipeline (Stage 3, cluster.subgroup step). Built 2026-09 for the synergy-build pipeline; a differently-shaped legacy table of the same name predates it in bible_research.db (M-code cluster model) -- same name, different table, different database. | **none recorded** |
| `cluster_subgroup_strong` | one row per strong-to-subgroup placement (membership) | The cluster-reading pack's own subgroup-membership table (#1690, was mti_term_subgroup, renamed 2026-09-13, design-complete). UNIQUE(strong) enforces one strong, one family, structurally. | **none recorded** |
| `escalation_thread_item` | one row per thread item | One row per item of a thread (type='thread' escalation): what a strand or task is matched against, and the item's current status only: open, or settled as closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread). Every response, including each settlement, is a row in escalation_thread_item_response. escalation #2000 (proposal v3 sec3.2, sec3.4; thread lifecycle, BUILD.md s338). | **none recorded** |
| `escalation_thread_item_verse` | one row per verse of an open item's target | #2236: the verses an open item is about, so it matches a scope on these verses and never on a whole cluster | **none recorded** |
| `ib_node` | one row per grounding element an ib_observation cites (strong/verse/subgroup/cluster/question/another observation) | The cluster-reading pack's own grounding table (#1692, design-complete 2026-09-14). Makes 'no way to check a finding's grounding' structurally impossible via the CHECK constraint + the mandatory coverage self-check (#1692 SS2: every strong/verse in a subgroup's membership must be grounded by >=1 ib_node row, checked at LLM generation time and independently re-checked by the recording pass at load time). | **none recorded** |
| `ib_observation` | one row per observation | One observation: a typed finding from a reading, with its text, meaning, implication, basis, parties and status (draft or withdrawn), grounded on verses, strongs, subgroups, clusters or other observations through ib_node. Written by stage: verse-reading (lexical.meaning, lexical.relational), char-reading, char-answers and char-subgroup (cluster.reading, cluster.answer, cluster.subgroup), strand-reading (strand_reading.record, strand_reading.derive), and enhanced by observation_enhancer.apply. A differently-shaped legacy table of the same name in bible_research.db is inactive. | **none recorded** |
| `ib_observation_enhancer_log` | one row per (observation, field) actually changed by a rule application | Audit trail for the observation_enhancer utility (escalation #1778) -- answers 'which rule touched this row, and what did it change' months later, the same kind of traceability ib_node's own traced_observation_id/source_stage already gives the write-time pipeline. Written only by handlers/observationenhancer.py:apply. | **none recorded** |
| `narrative_chapter` | one row per chapter or sub-chapter | One row per chapter or sub-chapter of the inner-being narrative, and the authority for which chapters exist, their reading order and what each is for (kind, purpose, purpose_ref). Changed only through Narrative-Register.ps1 (AddChapter, EditChapter); every structural change is logged in the Structure log. A renumbering changes chapter_no on the row; every record keeps its link to the chapter, so the history follows the chapter, not the number. The copy to learning4comfort publishes the active chapters' current files. escalation #2110 spec sec3.1; #2155 | **none recorded** |
| `narrative_citation` | one row per verse cited in a passage of the story | The citation index: every verse cited anywhere in the story, by passage. With narrative_claim_source it answers, for any verse, where it is cited and which claims rest on it. A reference that cannot be resolved is kept with verse_id NULL, never dropped. escalation #2110, spec sec3.8 | **none recorded** |
| `narrative_claim` | one row per claim | The register: one row per claim. A claim is a statement derived from sources (verses, later science) that goes beyond their mere text, held in its own plain wording. A quotation is not a claim. escalation #2110, spec sec3.3 (researcher, round 3) | **none recorded** |
| `narrative_claim_change` | one row per change to a claim or to a passage that tells it | The change log, many rows per claim: every change to a claim, and to each passage that tells it, with enough before and after to review the impact without opening another file (Q-F). A change to one passage that tells three claims writes three rows. escalation #2110, spec sec3.7 | **none recorded** |
| `narrative_claim_source` | one row per source of a claim | What a claim rests on: a verse (one row per verse; ranges and lists expanded), a lexical source, science (later), or a study file. escalation #2110, spec sec3.4 | **none recorded** |
| `narrative_claim_telling` | one row per claim told in a block (passage rows before #2172 are history) | The link between a claim and the block (narrative_section) that tells it, many to many. escalation #2110, spec sec3.5; per block since #2172 | **none recorded** |
| `narrative_section` | one row per section heading in a chapter | One row per section heading in a chapter, current or past. A chapter's opening, before any heading, has its own row (level 0). escalation #2110, spec sec3.2 | **none recorded** |
| `narrative_update` | one row per weave or recorded pass | One row per weave or recorded pass on the narrative, with its instruction, sources, notes and quote check. Imported updates keep the register version that added them. escalation #2110, spec sec3.6 | **none recorded** |
| `narrative_update_ref` | one row per escalation or thread an update names | The escalations, threads and thread items an update names. escalation #2110, spec sec3.6 | **none recorded** |
| `reading` | one row per reading: the work on one scope | #2228: a reading opened from a scope request and served by the escalation that anchors it; it passes three gates in order (recorded, synergised, published), each checked by Reading.ps1 | **none recorded** |
| `reading_strand_hit` | one row per hit: a strand strong in a verse | #2172 safeguard 1: every hit has a face, or a stated reason it has none, before the strand can close; the observation the hit went into | **none recorded** |
| `run_batch` | one row per batch/chunk attempt of a live multi-batch (or single-call) run | The batch/step-level control table (escalation #1756, researcher-approved design 2026-09-18) -- resume/skip (a new run_id skips any batch a PRIOR run_id already committed, via UNIQUE(step, selector_key, batch_content_key)), crash safeguard (a 'running' row with no terminal update proves a dead run), and live progress monitoring (BatchProgress.ps1) for every long-running LLM-calling step. lib/batchcontrol.py is the sole writer. Prompted directly by M49's Stage 1 verse-reading run needing two full from-scratch restarts this session with no way to skip already-paid-for batches. | **none recorded** |
| `verse_meta` | one row per verse (1:1 with verse.id) | Verse-level base-data companion to `verse` -- collates language/testament/chapter/verse_num/passage linkage once at the right grain, instead of denormalizing per-code (the old `language` source) or leaving facts homeless (`genre`, `lexical_complete_at`). Auto-synced via 4 triggers on verse/verse_lexical/verse_passage inserts and verse.deleted updates -- never written to directly by application code. Escalation #1608, 2026-09-09. | **none recorded** |
| `wa_obs_question_catalogue` | one row per catalogue question, the analytic-event question bank for the cluster-reading pipeline | Migrated from bible_research.db 2026-09-16 (#1696, #1706 Phase D item 19) -- 92 rows (98 source - 8 dropped per Phase 5 content review + 2 new T2.11 rows). ib_observation.question_code/ib_node.question_code both intend a real FK here once their tables' write paths are built (Phase F) -- not enforced yet, SQLite FKs are declare-at-create-time only. | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## ITEMS. Open items and threads, across every phase

What a reading leaves to be read elsewhere, how it is registered, and when it comes back.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `open_item.add` | open-item / Open-Item.ps1 | an item registered to a clear purpose: origin and anchor, a target scoped to verses, read for, why, comes back when -- see lib/openitem.py (escalation #2236) | escalation_thread_item (iba), escalation_thread_item_verse (iba) | refused: terminal |
| `open_item.reword` | open-item / Open-Item.ps1 | an existing item reworded to the same rules; the earlier wording to its history -- see lib/openitem.py (escalation #2236) | escalation_thread_item (iba), escalation_thread_item_verse (iba) | refused: terminal |
| `open_item.split` | open-item / Open-Item.ps1 | one wide item replaced by several, one purpose each; the old one superseded by them -- see lib/openitem.py (escalation #2236) | escalation_thread_item (iba), escalation_thread_item_verse (iba) | refused: terminal |
| `open_item.due` | open-item / Open-Item.ps1 | the worded items that come back when a cluster is worked (read-only) -- see lib/openitem.py (escalation #2236) | - | refused: terminal |
| `open_item.review` | open-item / Open-Item.ps1 | the stragglers report: items not worded, worded items past the review age (read-only) -- see lib/openitem.py (escalation #2236) | - | refused: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

**None.** No method rule or quality check is tied to any step of this stage.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:115 | open-item-has-a-clear-purpose | always | ps:Open-Item.ps1; ps:Escalation.ps1; ps:Reading.ps1 | yes, at Open-Item.ps1 |
| B:74 | open-threads-carried-as-escalations | study_active | ps:Escalation.ps1 -Action Thread; path:_analytics/** | **no** |
| B:92 | no-unnecessary-holding | study_active | path:_analytics/** | **no** |
| B:80 | open-items-lines-carry-a-handle | always | path:**/*.md | **no** |
| B:21 | chat-items-become-escalations | always | general:* | only at session start (general) |
| B:40 | open-items-route-through-escalation | always | general:* | only at session start (general) |
| E:4 | resolution_precedence | (escalation rule) | general:* | only at session start (general) |
| E:5 | chat_routing | (escalation rule) | general:* | only at session start (general) |
| E:16 | thread_check_before_work | (escalation rule) | ps:Escalation.ps1 | **no** |
| E:18 | thread_completion | (escalation rule) | ps:Escalation.ps1 | **no** |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `escalation.thread_register_path` | "_analytics/cross-cluster-web/open-threads-register.md" | the generated open threads register (Escalation.ps1 -Action Export -Type thread; regenerated at session-close) -- same path as the hand-kept register it replaces (escalation #2000, decision 3) |
| `escalation.thread_report_path` | "outputs/escalation/escalation-threads.md" | where Escalation.ps1 -Action Thread writes the open threads report (escalation #2000) |
| `escalation.thread_audit_report_path` | "outputs/escalation/escalation-thread-audit.md" | #2173 P5: thread audit report (Escalation.ps1 -Action ThreadAudit; lib/threadaudit.py) |
| `escalation.worked_strand_escalations` | {"M01": [1962], "M02": [1963], "M25": [1932], "M47": [1911, 2172], "M64": [1978, 1986], "M18": [1993], "M72": [1998], "M09": [2148], "M08": [2156], "M07": [2171]} | #2173 P5 T-d: per cluster, the escalations that carry its strand. A strand counts as worked only when every listed escalation is completed (read from state at audit time, never from memory); M47 lists #2172, so it is not worked while #2172 is open. Add a cluster here when its strand escalation is raised. |
| `open_item.max_verses` | 200 | an open item's target holds at most this many verses; a wider one is refused, to be split into separate items, one purpose each (researcher 2026-10-23, #2236 D3) |
| `open_item.output_dir` | "outputs/open-items" | where Open-Item.ps1 -Action Review writes the stragglers report (#2236) |
| `open_item.review_age_days` | 60 | Open-Item.ps1 -Action Review lists worded items older than this as stragglers to deal with (#2236 D4) |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `escalation_thread_item_kind` | cluster, strong, verse, strand, chapter, event, researcher, escalation, scope |
| `escalation_thread_item_response_kind` | touched, narrowed, forward, ruling, note, closed, reopened, withdrawn, superseded |
| `escalation_thread_item_status` | open, closed, withdrawn, superseded |
| `escalation_type` | task, run_error, issue, notice, config, note, thread |

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `escalation_thread_item` | one row per thread item | One row per item of a thread (type='thread' escalation): what a strand or task is matched against, and the item's current status only: open, or settled as closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread). Every response, including each settlement, is a row in escalation_thread_item_response. escalation #2000 (proposal v3 sec3.2, sec3.4; thread lifecycle, BUILD.md s338). | **none recorded** |
| `escalation_thread_item_verse` | one row per verse of an open item's target | #2236: the verses an open item is about, so it matches a scope on these verses and never on a whole cluster | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## RETIRED. Retired route: the passage method (hib.set to closing.set); its rules to be gathered into D4

Retired per the R3 feedback; reading passages in context is part of D4. Its method rules and quality checks are listed so that what still holds can be carried over.

### Steps (`cfg_step`, `cfg_work_package`)

| Step | Work package / PS tool | What it does | Writes (`cfg_write_grant`) | On fail (`cfg_on_fail`) |
|---|---|---|---|---|
| `hib.set` | operations-ingest / Operations-Ingest.ps1 | Step 1's HIB register for a whole book -- writes hib/hib_referent_option/verse_hib from a JSON payload (-PayloadPath). Clean re-derivation per book (soft-delete existing, insert fresh), same convention passage.build uses for passage. Fails cleanly (unknown-verse/bad-payload) rather than partially writing. | debate_change_detail (iba), hib (iba), hib_referent_option (iba), verse_hib (iba) | - |
| `passage.build` | build-passages / Build-Passages.ps1 | recompute the book's passages from verse_hib (hib-continuity/maximal); flag >review_over as needs_review. Redefined 2026-08-05 (B4) from the retired candidate-stamp/char-continuity rule -- see debate-analytic-process-digest-20260805.md Step 2. | debate_change_detail (iba), passage (iba), verse_passage (iba) | - |
| `phenomenon.set` | operations-ingest / Operations-Ingest.ps1 | Step 3's phenomena register for one already-tracked passage (needs -Chapters/-Range), from a JSON payload. Clean re-derivation per passage. Sets passage.phenomena_complete_at itself once the register is complete against verse_hib -- the phase gate operation.set checks. Fails cleanly (no-passage/unresolved-reference/bad-payload). | debate_change_detail (iba), passage (iba), phenomenon (iba) | - |
| `operation.set` | operations-ingest / Operations-Ingest.ps1 | Step 4-5's operations + parties for the same passage, from a JSON payload. REFUSES (phenomena-incomplete) if passage.phenomena_complete_at is still NULL -- the actual code enforcement of WA-interpretation-questions Part B.12 / the debate digest's Step 3 phase gate. Clean re-derivation per phenomenon set. Fails cleanly on any unresolved reference. | debate_change_detail (iba), operation (iba), operation_party (iba) | - |
| `closing.set` | operations-ingest / Operations-Ingest.ps1 | Step 7 (digest) / WA-interpretation-questions-v1.4 Part C sections 4-8 for one already-tracked hib-continuity passage -- writes passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note + passage.open_decisions_note from a JSON payload. Refuses (operations-incomplete) until every live phenomenon in the passage has a live operation. Reconciliation-gated per list (BUILD.md ??64 pattern), same as hib.set/phenomenon.set/operation.set. | debate_change_detail (iba), passage (iba), passage_emergent_question (iba), passage_insufficiency (iba), passage_linkage (iba), passage_validation_note (iba) | - |
| `passage.validate` | passage-quality / Passage-Quality.ps1 | read-only quality check: passage verse_count distribution — one escalation per invocation, standalone (not part of build-passages) | - | needs-review: terminal; findings-rejected: terminal; needs-revision: terminal |
| `report.whole_book_read` | whole-book-read / WholeBookRead-Report.ps1 | whole-book-read gathering report — for a book whose passage debates are (wholly or partly) filled, pulls every debate_status='filled' passage row in reading order, reads each debate file, extracts its Emergent-questions and Passage-level-linkages sections (tolerant heading match, explicit NOT-FOUND if a file's headings don't match), and lays them out per-passage with an empty Resolution slot for the researcher/AI to fill in; does not decide how any emergent question actually resolves itself | - | no-debates-found: terminal |

### Method rules (`cfg_method_rule`) and quality checks (`cfg_quality_check`)

| Step | Method rules | Quality checks | Delivered to the session |
|---|---|---|---|
| `hib.set` | 7 | 4 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `passage.build` | 6 | 1 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `phenomenon.set` | 9 | 6 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `operation.set` | 9 | 3 | **no** (`cfg_rule_scope` holds no method-rule reference) |
| `closing.set` | 6 | 4 | **no** (`cfg_rule_scope` holds no method-rule reference) |

Texts: appendix 2.

### Behaviour and escalation rules

| Rule | Key | Delivered when | Delivered where (`cfg_rule_scope`) | Reaches this stage's tools |
|---|---|---|---|---|
| B:4 | inferential-not-confirmed | always | general:* | only at session start (general) |
| B:69 | let-scripture-speak-no-imputed-synthesis | study_active | path:_analytics/** | **no** |
| B:72 | route-verses-hib-other-beings-data-only | study_active | path:_analytics/** | **no** |

Texts: appendix 1.

### Settings (`cfg_setting`)

| Key | Value | Use |
|---|---|---|
| `report.passage_debate_naming_pattern` | "WA-{book}-{range}-debate.md" | filename pattern for report.passage_debate ({book}/{range} substituted); stable scheme — reportkit archives the prior version on regenerate, no -vN-/date in the name itself |
| `report.whole_book_read_naming_pattern` | "WA-{book}-whole-book-read.md" | filename pattern for report.whole_book_read ({book} substituted); stable scheme — reportkit archives the prior version on regenerate, same convention report.passage_debate_naming_pattern already uses |
| `report.verse_gap_note` | "**Verse gap -- by design.** `{ref}` has no verse row in iba.db (no onboarded term's concordance search ever surfaced it -- see governance.verse_gap_by_design). Not an error; continuing with the next available verse." | inline note both report.verse_span_meaning and report.passage_debate insert into their output wherever a verse is structurally known to be missing from iba.db within the rendered range (lib.versespanmeaningreport.detect_verse_gaps) -- {ref} substituted |
| `method.interpretation_questions_path` | "workflow/instructions/WA-interpretation-questions-v1.4-2026-08-02.md" | current version of the Q1-Q10 interrogative + Part B guidance of interpretation — the passage-debate scaffold and any AI applying it must follow this exact file |
| `method.passage_read_guidance_path` | "workflow/instructions/WA-passage-read-guidance-v1.5-2026-08-02.md" | current version of the passage read guidance (steps 1-5 + notes, incl. step 2 note (f)) — the passage-debate scaffold and any AI applying it must follow this exact file; bump this setting (not the debates' memory) when the guidance revises |

### Allowed values (`cfg_enum`)

| Enum | Values |
|---|---|
| `hib_kind` | named_individual, unnamed_individual, named_collection, unnamed_collection, implicit_individual, implicit_collection |
| `operation_decision` | retain, set_aside, retain_referential, recorded_silence |
| `party_kind` | divine, human, non_human |
| `passage_debate_status` | scaffold, filled, empty, in-progress, complete |

### Passage settings (`cfg_passage`)

| Key | Value | Use |
|---|---|---|
| `passage.quality_report_path` | "iba/app/reports/passage-quality.md" | where passage.validate persists its findings |
| `passage.debate_session_chapter_guideline` | 3 | Advisory session-scope guideline (not hard-enforced) for report.passage_debate fill-in work: recommended max chapters per Claude Code session before clearing context and starting a fresh one. |
| `passage.debate_run_sequence` | [{"work_package": "operations-ingest", "step": "hib.set"}, {"work_package": "build-passages", "step": "passage.build"}, {"work_package": "operations-ingest", "step": "phenomenon.set"}, {"work_package": "operations-ingest", "step": "operation.set"}, {"work_package": "operations-ingest", "step": "closing.set"}] | Ordered step sequence Debate-Run.ps1 walks for one debate scope -- work_package+step pairs against the EXISTING active registrations. |
| `passage.debate_staging_path_pattern` | "iba/app/staging/operations/{book_lower}-{scope}-{step}.json" | Predictable path Debate-Run.ps1 checks for each step payload JSON before pausing. |
| `passage.max_single_verse_pct` | 20 | Per-book threshold: passage.validate escalates only if a book's (single-verse passage count / total verses in that book) exceeds this percentage. Below it, the book's distribution is accepted automatically -- no researcher decision needed for an already-in-bounds result. Researcher, 2026-08-22. |
| `passage.max_avg_verses_per_passage` | 30 | Per-book threshold: passage.validate escalates only if a book's average verses-per-passage exceeds this. Below it, accepted automatically. Researcher, 2026-08-22. |
| `passage.max_verses` | 20 | hard ceiling decided #1379 v7 — a passage/reading-block payload exceeding this many verses is refused before any write (too-many-verses), never silently truncated or auto-split. Read via required_module_setting('cfg_passage', 'passage.max_verses'), same call shape as every other cfg_passage row. |

### What the rows above do not show

- **Still registered as live:** the work packages `operations-ingest`, `build-passages`, `passage-quality` and `whole-book-read` are active in `cfg_work_package`.

### Tables this stage writes (`cfg_table`), and what counts as success (`cfg_table_purpose`)

| Table | Grain | Use | Success measure |
|---|---|---|---|
| `debate_change_detail` | hib_change_detail | one row per hib/hib_referent_option/verse_hib/passage/verse_passage/phenomenon/operation/operation_party/passage_linkage/passage_insufficiency/passage_emergent_question/passage_validation_note row inserted, updated, or soft-deleted by hib.set/passage.build/phenomenon.set/operation.set/closing.set -- the per-run CRUD audit trail shared by every debate writer (researcher direction 2026-08-08). | **none recorded** |
| `hib` | hib | one row per Human Inner Being identified in a scope (debate digest Step 1) -- scope-wide, not passage-scoped: the same HIB recurs across many passages of a book. | **none recorded** |
| `hib_referent_option` | hib_referent_option | one row per grammatically-live referent-crux reading (T4), child of hib. | **none recorded** |
| `operation` | operation | the operation for a registered phenomenon (Step 4-5 output) -- phenomenon_id NOT NULL enforces Part B.12 at the DB level. | **none recorded** |
| `operation_party` | operation_party | one row per source/target of an operation (plural-capable, v1.5 step1 note a), child of operation. | **none recorded** |
| `passage` | one row per passage — a reading frame (global, per book) | extends a characteristic's context to adjacent verses for assessing movement/process/qualifying spans; NOT a thematic unit | **none recorded** |
| `passage_emergent_question` | passage_emergent_question | Part C section 6 (Q10/B.9/B.12) -- interpretive forks and genuine literary/structural observations, tracked per passage, never merged across passages. | **none recorded** |
| `passage_insufficiency` | passage_insufficiency | Part C section 5 (Q9/B.7) -- data the base extract does not carry, named not filled. | **none recorded** |
| `passage_linkage` | passage_linkage | Part C section 4 (Q7) -- linkages between two specific, already-registered operations in the same passage, and surfaced non-linkages. | **none recorded** |
| `passage_validation_note` | passage_validation_note | Part C section 7 (Phase 3) -- the closing re-examination of the passage's own phenomena/operations, corrected before the debate is considered filled. | **none recorded** |
| `phenomenon` | phenomenon | the phenomena register (Step 3 output) -- one row per HIB per verse per passage. | **none recorded** |
| `verse_hib` | verse_hib | one row per HIB present/a presumptive candidate in a given verse (Step 1's per-verse sweep) -- the input B4's future HIB-continuity passage-boundary rule reads from. | **none recorded** |
| `verse_passage` | one row per verse-in-a-passage — passage membership (L4b), keeps the raw verse pristine | which passage a verse belongs to; a verse is in at most one passage | **none recorded** |

`cfg_table_purpose` (purpose and success) is filled only for the `cfg_*` tables; no data table has a success measure recorded.

Field meanings: appendix 3.

## H. Authorities held in documents, not config

Config rows that name a file as the authority for how analytic work is done.

| Config row | Names |
|---|---|
| B:73 read-verse-by-role-of-each-mcode-word | Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md |
| B:74 open-threads-carried-as-escalations | open-threads-register.md |
| B:88 weave-not-fit | _analytics/essay/spirit_soul_body/wa-essay-narrative-weave-method-and-ch10-structure-* |
| setting `governance.prose_canonical_authority` | "The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about. cfg_prose_concept points a key project concept (e.g. verse primacy, the inner-being definition) at the prose section that defines it, rather than restating the definition as a separate rule. Chapter-level review status is not tracked in cfg_*: it lives in prose_section.status (cfg_enum prose_section_status), set per section via Prose.ps1 -Step SetStatus, rolled up per chapter via prose_section_type.chapter_no. A methodology/approach change that touches a concept named in cfg_prose_concept should flag whether the prose needs updating (the flagging mechanism is a deferred build; this setting states the principle only)." |
| setting `method.interpretation_questions_path` | "workflow/instructions/WA-interpretation-questions-v1.4-2026-08-02.md" |
| setting `method.passage_read_guidance_path` | "workflow/instructions/WA-passage-read-guidance-v1.5-2026-08-02.md" |
| setting `narrative.inner_being_style_guide_path` | "Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md" |
| setting `report.obs_catalogue_path` | "Workflow/Catalogue/obs-catalogue.md" |
| behaviour class `sqlite` (authoritative_doc) | Workflow/SQLite/sqlite-extension-best-practice-v1-20260815.md |
| behaviour class `documentation` (authoritative_doc) | iba/app/GOVERNANCE.md |
| behaviour class `llm_output` (authoritative_doc) | Workflow/Claude_API/claude-api-usage-guide-v1-20260815.md |
| behaviour class `filing` (authoritative_doc) | iba/docs/863-file-naming-and-location-governance-plan-v1-20260826.md |
| `cfg_control_home` study_method | Workflow/Instructions/ -- one live file per subject, named by a cfg_setting path |

Source documents named by the method rules of these stages (`cfg_method_rule.source_doc`), with the number of rules drawn from each:

- #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) (14)
- #1690 (2026-09-13), #1706 (this build, 2026-09-17) (9)
- #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) (7)
- researcher direction, 2026-08-07 (6)
- (none given) (4)
- researcher direction, 2026-08-06 (3)
- #1706 SS4A, 2026-09-16 (2)
- #1706 role-data-presentation doc SS6, 2026-09-17 (2)
- #1711 v11, 2026-09-16 (2)
- ib-observation-governing-rules-checklist rule 5a/5a-i/5b (2)
- established project-wide convention, lexicalenrichgenerate.py precedent (2)
- escalation #1697 v5 (design) + #1706 (this build, 2026-09-17) -- iba/app/lib/clusterstatus.py (2)
- researcher 2026-06-15 review, restored via escalation #1836 (2026-09-22) (2)
- chat 2026-09-23, follow-on to escalation #1849/#1852 (2)
- WA-interpretation-questions-v1.4-2026-08-02.md Part A Q7 / Part B.12 / Part C item 4 (1)
- WA-interpretation-questions-v1.4-2026-08-02.md Part B.7 / Part C item 5 (1)
- WA-interpretation-questions-v1.4-2026-08-02.md Part A Q10 / Part B.8-B.9 / Part C item 6 (1)
- WA-interpretation-questions-v1.4-2026-08-02.md Part C item 7 (1)
- WA-interpretation-questions-v1.4-2026-08-02.md Part C item 8 (1)
- WA-passage-read-guidance-v1.5 step 6 note b (1)
- WA-passage-read-guidance-v1.5 step 2 note f (1)
- WA-passage-read-guidance-v1.5 step 2 notes b, d (1)
- WA-passage-read-guidance-v1.5 step 2 note c (1)
- WA-passage-read-guidance-v1.5 step 2 note e (1)
- debate-analytic-process-digest-20260805.md Step 1 (T4 folded in) (1)
- nahum-1-inner-being-training-20260803.md (researcher's own training pass) (1)
- design doc §5.1/§3.E (1)
- design doc §4 (1)
- catalogue-finishing doc §4; governance.rules_must_be_config_driven (1)
- method-and-drift-mitigation doc §1-2 (1)
- design doc §3.G (1)
- #1711 v11 + #1712 catalogue realignment, 2026-09-17 (1)
- escalation #1606; #1706 Phase A item 1; #1711 build (1)
- #1860, 2026-09-23 word-level/relational split (1)
- escalation #1697 (design) + #1706 (this build, 2026-09-17) -- iba/app/lib/clusterstatus.py (1)
- #1860 v3 researcher approval, 2026-09-23 (1)
- #1860 v1 context, 2026-09-23 (1)
- WA-interpretation-questions-v1.4 Part B.12 (1)
- WA-passage-read-guidance-v1.5 step 1 note a (1)
- WA-interpretation-questions-v1.4 Q4 / Part B.5 (1)
- WA-interpretation-questions-v1.4 Q11 / Part B.10 (1)
- WA-interpretation-questions-v1.4 Q12 / Part B.11 (1)
- WA-interpretation-questions-v1.4 Part C section 3 (1)
- researcher direct correction, same session as dan8-debate-run-failure-review-20260806.md (1)
- researcher direction, 2026-08-06, following the HIB-distribution visualization (1)
- app convention (DB-enforced: verse_passage.verse_id unique) (1)
- researcher direction, 2026-08-05/06 (1)
- WA-passage-read-guidance-v1.5 Phase 1/Phase 2 structure + its own 2026-08-02 change-control note (the direct fix for the Amos 1-3 drift) (1)
- WA-passage-read-guidance-v1.5 step 3 note e (1)
- WA-passage-read-guidance-v1.5 step 3b (1)
- WA-interpretation-questions-v1.4 Part B.12; WA-passage-read-guidance-v1.5 step 6 note c (1)
- debate-analytic-process-digest-20260805.md Step 3 'how this gets controlled'; b3-b5-operations-schema-design-20260805.md (1)
- WA-interpretation-questions-v1.4 Part B.4; WA-passage-read-guidance-v1.5 step 2 note f (1)
- iba/docs/1613-meaning-layer-config-inventory-v1-20260909.md section17.1; escalation #1613, researcher ruling 2026-09-10 (1)
- outputs/markdown/session-routines-start-project-change-proposal-v1-20261020.md (P3, Q1) (1)

## I. Config tables not included, and why

| Table | Rows | Why not included |
|---|---|---|
| `cfg_api` | 3 | the app's API routes |
| `cfg_behaviour_class` | 8 | class descriptions (authoritative documents listed in H) |
| `cfg_book_order` | 66 | book ordering (base data mechanics) |
| `cfg_candidate_rule` | 289 | accept-list of the retired candidate stage |
| `cfg_change_detail` | 3274 | history of cfg changes |
| `cfg_change_log` | 12 | history of config loads |
| `cfg_column` | 2251 | only the analytic tables' columns are included (appendix 3) |
| `cfg_connection` | 3 | connection settings |
| `cfg_content_index_exclude` | 1 | file content index |
| `cfg_content_index_size_override` | 0 | file content index |
| `cfg_escalation_requirement` | 25 | escalation mechanics |
| `cfg_escalation_transition` | 19 | escalation mechanics |
| `cfg_index` | 126 | schema indexes |
| `cfg_meta` | 2 | app metadata |
| `cfg_prose` | 9 | programme-prose tool paths (prose is the researcher's, B:85) |
| `cfg_report` | 50 | report layout |
| `cfg_report_csv_table` | 41 | report layout |
| `cfg_report_section` | 135 | report layout |
| `cfg_status_flow` | 17 | escalation, prose and word status flows (word flow is base data) |
| `cfg_table` | 226 | table registry: only the tables the stages write are included, with their grain and use, in each stage |
| `cfg_table_purpose` | 68 | purpose and success are recorded only for cfg_* tables; none for any data table |
| `cfg_trigger` | 31 | schema triggers |
| `cfg_unique` | 111 | schema constraints |
| `cfg_utility` | 982 | module registry |

**Behaviour rules not placed in a stage (57).** These govern any work (chat, filing, terminal, development, escalation handling, the API) rather than the analysis itself; each still applies through its own delivery: B:1 verify-before-acting, B:3 single-authority-pointer-not-copy, B:5 sdk-dependency-decision, B:6 no-hardcoded-call-params, B:10 never-expose-api-key, B:11 readonly-by-default, B:14 query-file-conventions, B:16 askuserquestion-banned, B:17 confirm-before-nontrivial-work, B:18 output-to-file-not-chat-only, B:20 cost-awareness-flag-cheaper-path, B:22 proceed-autonomously-once-rules-are-stable, B:23 close-the-loop-not-just-report, B:25 readonly-commands-no-permission-needed, B:26 git-commit-and-push-together, B:27 heredoc-powershell-only, B:28 diagnose-reported-errors-dont-route-around, B:29 verify-fix-against-synthetic-and-real-case, B:31 guidance-baked-into-authoritative-record, B:32 no-hedge-in-complete-records, B:33 single-living-register-update-in-place, B:38 root-fix-not-one-off, B:39 simple-steps-not-engineered-designs, B:41 every-interactive-module-needs-ps-script, B:42 user-guide-updated-same-unit-of-work, B:43 every-active-ps-script-dispatches-through-run-py, B:44 decision-points-are-terminal-not-inline, B:45 decision-required-answered-via-update-not-answerrun, B:46 test-plan-per-module-utility, B:48 record-change-log-choke-point, B:49 record-change-log-version-is-pointer, B:50 record-change-log-payload-is-prior-state, B:51 one-time-hard-delete-exception, B:56 naming-shape, B:57 snapshot-vs-living-document, B:58 archiving-trigger, B:59 claude-code-filing-obligations, B:60 tool-report-path-vs-deliverable-document, B:62 config-updated-same-unit-of-work-as-change, B:63 claude-held-item-must-progress-or-bounce-back, B:64 escalation-file-carries-escalation-id-prefix, B:65 audit-deliverable-cross-check-before-presenting, B:75 devmode-config-writes-are-audited, B:81 session-compliance-restated-and-proved, B:82 session-close-blocks-commit-on-open-findings, B:96 replaced-history-out-of-read-path, B:97 developer-mode-scope-and-conduct, B:98 fix-standard-violations-dont-ask, B:99 read-instruction-in-whole-chat-context, B:100 names-not-bare-codes, B:101 ready-to-run-commands, B:102 status-reports-checked-facts-only, B:103 match-established-convention-when-extending, B:104 check-new-rules-against-existing-first, B:105 diagnosis-is-not-licence-to-build, B:106 no-per-item-approval-steps-in-designs, B:108 tool-layer-escaping-checks.

**Live steps not placed in a stage (38):** `behaviour.list`, `compliance.check_start`, `compliance.template`, `configmaint.propose`, `configmaint.report`, `configmaint.validate`, `content_index.search`, `content_index.size_profile`, `escalation.context`, `escalation.history`, `escalation.list`, `escalation.thread_export`, `folderpurpose.autoassess`, `folderpurpose.crosscheck`, `folderpurpose.list`, `folderpurpose.seed`, `folderpurpose.set`, `folderpurpose.show`, `manifest.rebuild`, `manifest.search`, `pathaudit.scan`, `prose.flag`, `prose.flag_fix_apply`, `prose.flag_fix_propose`, `prose.set_status`, `purge.audit`, `purge.execute`, `purge.retire_database`, `report.registry`, `report.schema_overview`, `report.schema_overview_bible_research`, `report.span_analysis`, `report.word`, `retention.report`, `session.close`, `table.export`, `validation.book`, `validation.word`.

**Retired work packages (inactive), not included:** batch-progress-report, book-narrative, book-narrative-generate, book-narrative-validate, candidate-curation, candidate-quality, chapter-generate, content-index-rebuild, passage-debate-report, passage-debate-sync, seed-candidate-report, set-candidates, strand-reading, verse-analysis-report, word-audit, word-registry-span-report.

## Appendix 1. Rule texts

**B:2 step-not-done-without-validated-output** · class terminal · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> A step expected to produce an output (a file, a database write, a report) is not complete until that output has been confirmed to exist and matches what the step was supposed to produce. Reporting a step as done on the strength of the command appearing to succeed, without that confirmation, is a violation.

**B:4 inferential-not-confirmed** · class llm_output · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> Any claim, classification, or connection produced via an LLM or API call -- including Claude's own output, a subagent's report, or an automated classification pass -- that is not directly grounded in verifiable source data must be labelled inferential, not confirmed. An inferential label may not be silently upgraded to confirmed without new, citable supporting evidence.

**B:7 cost-cap-before-call** · class llm_output · enforced by: VERIFIED against the one live call site (iba/app/handlers/narrative.py:generate(), lines ~156-161) 2026-09-03: max_cost read from narrative.generate_max_cost, est_cost_usd checked against it BEFORE call_api() is ever reached -- fail('cost-cap-exceeded') with no call and no spend if over. Confirmed by reading the actual branch, not inferred from the docstring.

> A live Claude-API call is preceded by a pre-call cost estimate and a hard cost-cap check: hard-refuse over the cap (no call, no escalation, nothing spent); escalate for approval below the cap. No live call happens before this two-step gate.

**B:8 usage-log-required** · class llm_output · enforced by: VERIFIED against the one live call site (lib/narrativegenerate.py:log_usage()) 2026-09-03: every call_api() success path writes run_id/book/model/input_tokens/output_tokens/cost_usd/path to an append-only CSV via log_usage() -- read the actual write, not assumed.

> Every live Claude-API call's real `usage` block (not the pre-call estimate) is logged to an append-only CSV usage log. Skipping this write leaves the project's cost ledger with no record the call ever happened.

**B:9 sonnet-default-model** · class llm_output · enforced by: VERIFIED live 2026-09-03: cfg_setting narrative.generate_model = 'claude-sonnet-5', the one live call site's only model source (no hardcoded override found).

> Claude Sonnet 5 is the default model for high-volume structured analytic-phase work. Using a more expensive model (Opus) requires a specific stated reason, not a default choice.

**B:13 dont-assume-which-database** · class sqlite · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> Don't assume which database a table lives in. bible_research.db (prose + analytic findings) and iba.db (process control + the entire base data layer) have a defined split; a 'no such table' error usually means the wrong database was opened, not a typo.

**B:19 factual-discipline-no-guessing** · class chat · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> Work proceeds only from explicit, verified facts. Guessing, unstated assumptions, and filling gaps with speculation are not permitted; when information is missing or unclear, work stops and a real question is asked (never via AskUserQuestion) before proceeding. Distinct from `llm_output.inferential-not-confirmed`, which labels content already produced — this rule governs not proceeding at all without the facts.

**B:21 chat-items-become-escalations** · class chat · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> A genuine open item, discovered anomaly, or judgement call raised or surfaced in chat conversation is recorded as an escalation in the same turn it's identified, not left standing only in chat prose. Full rule (including the closed-decision exemption) and its mechanical enforcement live at `cfg_escalation.chat_routing` — this row is a pointer into that table, not a restatement, per `documentation.single-authority-pointer-not-copy`.

**B:24 show-evidence-dont-smooth-over** · class chat · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> When reporting database state or investigation results, the actual query/sample data is shown, not a rounded-off or smoothed summary that hides messiness or uncertainty. A structural check passing (FK/not-null/enum) is a different claim from the values being fit for purpose, and reporting must not conflate the two.

**B:34 source-of-truth-is-written-record** · class documentation · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> A claim about project state, history, or a prior decision is grounded in the written record (files, database, manifest) and cited, not asserted from memory or recollection.

**B:36 no-unsubstantiated-superlatives** · class llm_output · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> A superlative claim ('most', 'clearest', 'strongest', and similar) is not written unless every candidate was actually checked against it — an unverified superlative is exactly the kind of unearned-confidence claim `inferential-not-confirmed` already forbids, made concrete.

**B:37 derive-from-instruction-not-prior-unreviewed-output** · class llm_output · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> New analytical work is derived from the authoritative instruction document, never from a prior run's unreviewed output file used as an implicit template — an unreviewed pass may itself be wrong, and copying its shape propagates the error silently.

**B:40 open-items-route-through-escalation** · class development · enforced by: DETERMINED (not deferred), 2026-09-03 audit, escalation #1384: this rule governs Claude's real-time conversational/tool-use conduct within a turn -- there is no durable code or DB artifact a configmaint.validate scan could check after the fact to confirm or refute compliance. Mechanical enforcement does not apply to this class of rule; the realistic enforcement path is direct researcher review of transcripts/sessions, not automation. If this determination is wrong for this specific rule, flag it -- not left open as a default.

> Every open item discovered anywhere in the project's work -- a code review finding, a validation run's output, a documentation sweep, a data-quality check -- is recorded in the escalation table (`governance.escalation.scope`), not left as a silent fix, a code comment, or a mention buried in a report with no tracked row. `chat.chat-items-become-escalations` is this same principle's chat-conversation-timing instance (same turn it's raised in conversation); this rule is the general case, for anywhere else an open item surfaces.

**B:52 prose-section-session-a-replace-author-gate** · class sqlite · enforced by: apply_session_patch.py's UPDATE ... WHERE id=? AND author='claude_code' clause

> The session_a_replace operation updates a prose_section row in place. Code-gated on author='claude_code'; permitted only for Session A mechanical extracts, because they are reproducible from structured data rather than analytical judgement. Under Model A (escalation #836) every write is in-place, so this is one of several in-place write paths, distinguished by its author-gate, not by being uniquely non-supersede.

**B:53 prose-section-two-patch-ordering** · class sqlite · enforced by: apply_session_patch.py's section_type_id_lookup resolution

> A new prose chapter reaches the database in two ordered patches: CATALOGUE_POPULATION first (creates prose_section_type handles), then PROSE (content, referencing handles by section_type_id_lookup: {code}). Applying PROSE before its CATALOGUE_POPULATION fails at the code lookup, by design.

**B:55 prose-section-type-creation-requires-researcher-instruction** · class sqlite · enforced by: Not mechanically enforced -- a discipline rule, made real and queryable via cfg_behaviour_rule, matching the prose-quality-flag-on-upstream-change precedent (escalation #829).

> A new prose_section_type row may only be inserted on explicit researcher instruction naming the new code and its book_label/source_stage placement -- it is controlled vocabulary (prose_section_type's own cfg_table.use text: 'the only real enforcement behind prose_section.section_type_id'), not Claude-originated content, the same standard already applied project-wide to cfg_enum and other controlled-vocabulary tables. Governs WHO may trigger the first half of the existing two-patch (CATALOGUE_POPULATION then PROSE) creation pattern -- that pattern's own ORDERING is unchanged, governed separately by cfg_behaviour_rule 'prose-section-two-patch-ordering'.

**B:61 inactive-tables-never-active-inputs** · class sqlite · enforced by: DETERMINED, 2026-09-03: this is Claude's own behavioural discipline (what to investigate/include), not a code-checkable fact after the fact -- the failure mode the researcher caught live this session was Claude choosing to dig into inactive/historical state unprompted, not a code defect a scan would catch.

> If a table, column, or row is marked inactive in the configs (cfg_table.inactive / cfg_column.inactive / an active=0/inactive=1/delete_flagged=1 row), it is never included in any report, analysis, or result -- unless the request explicitly asks to explore historical/inactive data. Going back over inactive/historical data to rebuild or reconcile it, unprompted, is itself a violation of this rule's intent, not a form of thoroughness -- it wastes time and produces confusing results. Default to ignoring inactive state entirely; only engage with it on an explicit historical-exploration ask.

**B:66 cluster-label-must-track-membership** · class development · enforced by: buildable_not_built, 2026-09-07 -- a mechanical check is plausible (flag any cluster_code whose cluster_strong membership changed since cluster.last_updated_date/description was last touched) but not built this pass; until built, enforcement is manual discipline at merge/reassignment time.

> The cluster table's short_name and description are maintained labels, not immutable identifiers -- cluster_code is the stable key, the label is not. Whenever a cluster's live cluster_strong membership changes (a strong added, removed, or moved to/from that cluster_code -- including a merge or split, e.g. escalation #1525's M-code merges), the cluster's short_name/description must be reconsidered against the new membership and updated if it no longer accurately describes it. A frozen label that no longer matches its cluster's actual Strong's content is not acceptable -- these labels are read and relied on repeatedly downstream (reports, prose, researcher review) and must stay accurate, not just stable.

**B:67 bible-research-db-excluded-from-iba-results** · class sqlite · enforced by: context_delivered, 2026-10-13 (#2108) -- a rule about what goes into analysis results, the same class as the other sqlite rules marked context_delivered; delivered by memory project_bible_research_db_prose_only_20260924, feedback_dont_assume_which_database.

> bible_research.db (research_db) is never included in any IBA-line ANALYSIS result -- report, escalation finding, cross-check, or answer to the researcher drawing conclusions about the study's content -- EXCEPT the prose tables (prose_section, prose_section_type, and cfg_prose_concept's referenced content), the canonical, foundational authority on the programme's own governing concepts (governance.prose_canonical_authority), explicitly exempt from this exclusion, AND EXCEPT registered DB-hygiene/maintenance utilities (e.g. purge.audit/purge.execute) whose job is administrative housekeeping across the whole app -- soft-delete counts, dependency checks, row removal -- rather than analytical investigation: these may query, report on, and write to bible_research.db tables as their registered function requires. All other current base-data/lexical/cluster investigation and reporting is scoped to iba.db only. If a question or discrepancy seems to require bible_research.db data OUTSIDE the prose tables or a registered maintenance utility's own scope, stop and flag it rather than querying or citing that database.

**B:68 stage1-corrections-only-via-real-rerun** · class sqlite · enforced by: iba/app/lib/recordingpass.py:record_one_observation (no automated check exists yet that a future script complies -- structurally known, not mechanically enforced)

> Every correction to ib_observation (update, withdraw, consolidate) happens ONLY as a byproduct of record_one_observation() (iba/app/lib/recordingpass.py) processing a real, fresh LLM answer for the exact occurrence in question -- never a standalone script that edits or derives content for existing rows without a genuine new answer behind it. Reconciliation is therefore inherently incremental: a verse's stale/duplicate data only gets cleaned up when that verse is genuinely reprocessed (lexical.meaning -Force) -- there is no batch-cleanup lever and none should be built.

**B:69 let-scripture-speak-no-imputed-synthesis** · class llm_output · enforced by: Not mechanically enforced -- the guide §8.2 let-Scripture-speak pass before any narrative commit; audit record _analytics/essay/spirit_soul_body/wa-essay-narrative-imputed-readings-audit-v1-20261001.md; delivered by CLAUDE.md (rule 69 cited) and memory feedback_let_scripture_speak_no_imputed_synthesis. [2026-10-21, #2181: CLAUDE.md no longer carries rule text; delivery is the start routine -- Start-Iba.ps1 prints every active rule, restated in the compliance file (rule 81).]

> Narrative, ledger and finding text states what a cited verse or passage says, and may set related verses side by side. It never joins verses into a pattern, mechanism, division of labour or "what this shows" that no verse states, and never uses an uncounted most/often/always. A new insight found while writing goes to the strand ledger first, not into prose. A researcher "not in the way you portrayed it" means withdraw the portrayal. When in doubt: quote, and stop. Full standard: cfg_setting narrative.inner_being_style_guide_path (guide §1, §2, §8.2).

**B:70 cluster-tags-loose-no-retagging** · class llm_output · enforced by: Not mechanically enforced -- applied when writing strand and unit ledgers (section F); memory feedback_interaction_over_reallocation

> Cluster allocation (cluster_strong) is a loose association for the purposes of analysis. A strand or unit that finds a word associated with another cluster records that association in its ledger, for cross-cluster analysis. It never proposes, raises or applies a re-tag or re-allocation of a single word, and never builds option tables for one. Exception: re-tagging takes place only in exceptional circumstances, where a group of words turns out to be wrongly clustered (example: #2163, the body words and the flesh word's own T-codes moved to M47 on the researcher's instruction).

**B:71 reuse-extracted-base-data-set-based-mcode** · class sqlite · enforced by: Not mechanically enforced -- applied when preparing any strand/unit query; companion to rule 20 cost-awareness-flag-cheaper-path; memory feedback_reuse_extracted_base_data

> Before any query in a strand or unit, use what is already extracted. (1) The strand folder's existing pulls come first: their columns (other_m_words, narrative_refs, hit_words, group) are aggregated from the file, not re-queried. (2) The verse to M-code link is verse_lexical.strong joined to cluster_strong (cluster_code LIKE 'M%', deleted=0). For any verse set it is read with ONE set-based query over that set. Never a per-verse query loop, and never a pass over every cluster to find which apply. (3) Results already produced in this or another strand (ledgers, face-combination CSVs, crossrefs, reading placements) are reused, not re-derived. (4) A query that does not return within seconds is a signal the approach is wrong: stop and re-plan, do not wait it out.

**B:72 route-verses-hib-other-beings-data-only** · class llm_output · enforced by: Not mechanically enforced -- applied when writing strand ledgers and narrative; GOVERNANCE.md s90; memory project_god_character_routing_20261007

> The study's primary focus is the human inner being (HIB). Each verse in a strand is routed by what it shows, and the route is recorded in the ledger. (A) Other beings in their own right: a word used of God, angels, other spirits or nature (non-HIB) is routed to Ch 13 "Other beings" (13.1 Divine, 13.2 Angels, 13.3 Other spirits, 13.4 Nature), analysed for what the verses say that being is and does; for God, also how his character passed to the HIB through creation in his image, held open (not deep-dived now, #1984). (B) Another being interacting with the HIB is fully in HIB scope and follows the HIB analytic pattern. A verse may take A and B, described from different angles. (C) A verse with no inner-being and no other-being bearing is still properly assessed in the analysis and recorded in the ledger, but does not enter the narrative. Existing analysis and narrative sections are NOT corrected in a dedicated pass: each is reset only on the researcher's individual instruction. Routing a strand's verses into the narrative waits for the researcher's direction.

**B:73 read-verse-by-role-of-each-mcode-word** · class llm_output · enforced by: Not mechanically enforced -- applied when reading strand verses and weaving, per the guide Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md; memory feedback_entry_word_is_not_the_main_operation

> A strand pulls verses by its M-code, but an M-code tag does not make a word the verse's characteristic: cluster allocation is a loose association (rule 70) and a word's role -- characteristic, qualifier / process-element, or standalone -- is decided per occurrence (verse-analysis method s13-14; glossary 'role'). Each verse is read in its passage and genre; every M-coded word (rule 71, set-based) is given its role against the verse's main IB operation; only then is the strand's own word read, in the role it has there. A strand word in the qualifier role is carried as a qualifier of that characteristic (no own account from that verse, method s13b), recorded as an interrelationship and a face (rule 89), and the verse's home follows the characteristic. The M-code words are read in relation to each other (relational observation), pointers outside the verse kept separate, parties and route recorded (rule 72), following the confirmed role-driven sequence and progressive reading across strands. Collections are grouped by main operation, not entry word. Existing narrative is not audited in a dedicated pass; placements are corrected in each strand's read-back as the verse's characteristic M-code comes into focus. Reading also: (1) goes outward from the verse, not inward from the item's question -- first write down everything the verse carries, each with where it bears (chapter, thread, signpost), and answer the item's question last; (2) for every word that names an inner or bodily act, looks at the original -- the root's range (strong_meaning_tree and the ESV renderings across its verses) and whether the English adds or hides something; (3) never closes an item or verse on 'not X' -- the close records what the verse is instead. A role label is never a verdict. Full guide: Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md.

**B:74 open-threads-carried-as-escalations** · class chat · enforced by: Escalation.ps1 (-Type thread; -Action Thread/Match/ThreadCheck/Export; -Item/-AddItem/-Respond/-ResponseKind/-SupersededBy on Update); lib/escalation.py; cfg_escalation rows thread_check_before_work/raise_state_choice/thread_completion/resolution_precedence; cfg_escalation_transition priority-0 thread rows and thread_reassigned; cfg_escalation_requirement thread_type/thread_superseding rows; cfg_enum thread item kinds/statuses/response kinds; GOVERNANCE.md s93. Not mechanical: that a strand checks Match before a unit pull, and that researcher feedback in chat is recorded the same turn.

> The open threads register is carried in the escalation table as type='thread' (alias OT-nn), not edited as a markdown file. A thread is not worked as a task: it moves only when a strand reaches it (focused capture, rule 84). Its items (escalation_thread_item) are registered and reworded through Open-Item.ps1, each to one read purpose (rule B:115: a face or perspective, its target scoped to the verses and strongs of that purpose, what to read for, why it is open, when it comes back); items of the older kinds (cluster, Strong's, verse, strand, chapter, event, researcher, escalation) are reworded to that form. Items are what a strand, task or reading is matched against (Escalation.ps1 -Action Match; a worded item on its target verses). Claude manages each thread's lifecycle; the researcher gives feedback in chat, which Claude records verbatim the same turn, and there is no approval step, for a thread or for any item. Every response to an item -- touched, narrowed, forward, ruling, note, closed, reopened, withdrawn, superseded -- is an escalation_thread_item_response row, recorded through Escalation.ps1 -Action Update -Id OT-nn -Item ... -ResponseKind ... -Respond ..., and written in full to the thread's history. A thread completes when its last open item is settled; a thread is withdrawn or superseded (-SupersededBy OT-nn) with its open items settled in the same call. Notes and comments on a thread are Updates, never edits to the register file. The file _analytics/cross-cluster-web/open-threads-register.md is generated (Escalation.ps1 -Action Export -Type thread) and regenerated at session-close when a thread row changed in the session (SC12). Its quality, validity and integrity are audited at every start (Escalation.ps1 -Action ThreadAudit). Before every unit pull of a strand, the threads that bear on it are matched (Escalation.ps1 -Action Match -Cluster .. -Strong .. -Verse ..; -For nnnn records the match); held items and researcher questions are raised as threads at every ledger approval (Escalation.ps1 -Action Raise -Type thread).

**B:76 narrative-claim-register-kept-in-iba-db** · class chat · enforced by: Narrative-Register.ps1 (work package narrative-register); history triggers on narrative_claim, narrative_claim_telling, narrative_passage and narrative_chapter (cfg_trigger); -Action Export regenerates the three published files

> The narrative claim register is kept in iba.db. It is edited there, through `Narrative-Register.ps1` and `Reading.ps1` (the narrative itself: -Step Apply) or directly, and every change keeps its before and after. The register file is the published copy, regenerated from the database after each change; an edit made only in that file is not kept.

**B:77 claims-register-keeps-narrative-honest** · class llm_output · enforced by: Not mechanically enforced -- delivered by CLAUDE.md (The claims register keeps the narrative honest), GOVERNANCE.md section 94 and memory feedback_claims_register_keeps_narrative_honest; Narrative-Register.ps1 Record lists changed passages and other tellings to read; life-death-claim-register-crosscheck-v2-20261013.py finds verses in neither narrative nor register. [2026-10-21, #2181: CLAUDE.md no longer carries rule text; delivery is the start routine -- Start-Iba.ps1 prints every active rule, restated in the compliance file (rule 81).]

> Every narrative statement that goes beyond its verses has a narrative claim register entry with verse sources, or it is removed from the narrative (it may return later in another form). The interpretation of verses in context sets the narrative; verses that sit against a narrative line change the narrative and get their own claim, never trimmed, set aside or left out. Readings of the words in focus check the full verse set: a verse in neither the narrative nor the register is a missing reading area. The register anchors what verses say from different readings and focal points; the narrative tells the story from the claims; the register keeps the narrative honest. When an update touches a chapter, the existing passages on the concept being updated and its related concepts (not the whole chapter) are read against the register under this rule in the same pass, and that concept's current claims that no passage tells are linked, restated or withdrawn.

**B:78 narrative-chapters-change-only-through-the-register** · class sqlite · enforced by: Partially enforced: AddChapter/EditChapter refuse an unknown kind or state, a number in use and a missing file, and log every structural change in the Structure log; Narrative-Register.ps1 Check reports a chapter with no kind or purpose, a duplicate reading order, a .md file in the narrative folder that is no chapter's current file, and every row whose created_by is 'direct edit'; narrativecopy.py copies only the active chapters' current files. A direct SQL insert cannot be stopped, only reported. GOVERNANCE.md section 95.

> Every chapter of the inner-being narrative is added, moved, renamed, renumbered, split, merged or retired through Narrative-Register.ps1 (AddChapter, EditChapter), never by a direct insert or update of narrative_chapter. The chapter table is the authority for which chapters exist, their reading order and what each is for (kind, purpose, purpose_ref); a new chapter carries its purpose and the ruling that set it up. The copy to learning4comfort publishes exactly the active chapters' current files.

**B:79 reading-file-placement-per-verse** · class documentation · enforced by: session-close SC5(d) (handlers/session_close.py _sc5d) on every reading file changed in the session; settings session_close.reading_scope / reading_file_pattern / placement_kinds.

> Every reading, account, ledger or weave file of a strand carries one placement for every verse it names: in a `## Placements` table (/ verse / placement /) for a .md file, or a `placement` column beside `reference` for a .csv. The placement's first word is one of session_close.placement_kinds: told (a current chapter tells it), claim (a register claim source), data, forward OT-nn.n, held #nnnn, parked, or context (named only as the setting of another verse). A verse named with no placement, or placed 'told' when no chapter tells it, is a finding at session-close.

**B:80 open-items-lines-carry-a-handle** · class documentation · enforced by: session-close SC4(a) (handlers/session_close.py _sc4a) on every .md file changed in the session.

> Every line of an `Open items` section in a project file names the register item that carries it: an OT-nn.n or OT-nn thread item, or an escalation #nnnn, that exists and is still open. A line with no handle, or a handle that is closed or does not exist, is a finding at session-close: raise the item (rule 21) or close the line.

**B:83 authoritative-source-only** · class filing · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> C:\Bible_study_projects is the only authoritative source for the project. Every other copy is ignored by default: G:\My Drive\Bible_study_projects (an old copy, to be archived), G:\My Drive\Claude_Research (a working folder for other platforms; what duplicates this project or Zotero is to be archived), and study documents in %USERPROFILE%\Zotero\storage, Documents, Desktop and elsewhere on G:\My Drive. A file from those places is used only when the researcher names it; even then Claude says it is outside the authoritative source and brings it into the project, with the researcher's approval, before relying on it.

**B:84 fan-out-progressive-strands** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> Analysis is fan-out / progressive-stream, not cluster by cluster: no cluster reading is started as such. The inner being is a web of interrelated activity; a strand is one strand of that web, with no start and no finish, taken in turn and explored; the fan-out follows as the picture develops; a strand may be diverted, and a 'distraction' may deserve a deeper look; all strands merge into one whole. Open items are parked focus areas. Cluster codes are anchor points, not goals. Capture is focused: nodes and observations are written per topic or strand as that strand is explored, with no generic whole-scope task and no backfill of earlier work. The ib_node principle (verse, surface, strong, subgroup = association, question = stream) is the central linkage.

**B:85 prose-only-on-instruction** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> Prose is the researcher's: it is built up by the researcher as each area of focus develops. Claude writes no prose (the DB prose store, or a narrative chapter file) without a specific instruction. The inner-being narrative's chapter files are drafts written on the researcher's specific instruction; they are files, not the DB prose store.

**B:86 narrative-reset-and-weave-record** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> The narrative is Inner Being in Operation, in chapter files under _analytics/essay/spirit_soul_body/inner-being-narrative/, written to the style guide (narrative.inner_being_style_guide_path). The original adjusts to the new, not the reverse; each unfounded claim is checked and restated; each later stream of work adds to it. Each strand updates the chapter files it touches (version bump, prior version archived) and records the weave in the narrative claim register in the same pass (Narrative-Register.ps1 -Action Record -File <the weave's update JSON> -By Claude). A chapter's purpose is read in narrative_chapter before material is placed in it (rule 78). The researcher's own pictures (e.g. 'umbrella') are not narrative terms: the verses' own phrases are used.

**B:87 narrative-chapter-text-rules** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> In the chapter text: unchecked original material stays in marked Held sections; quote wording is checked against the ESV text in iba.db verse; science chapters come later; the Holy Spirit study is separate, except that for 13.1 (the divine) the Spirit is part of it -- a verse about the Spirit's own acts is placed in 13.1, not set aside; Jesus is part of the divine and gets attention in Ch 13 -- his own acts get their 13.1 face, and Ch 10 keeps the human side.

**B:88 weave-not-fit** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> A new item is woven into the narrative, knowing there is more to come; it is never fitted to where it supports the current narrative. Every observation from a strand gets a recorded placement; 'does not fit' is never one -- it means the narrative's structure must change. Each strand re-reads the sections it touches, and they adjust to it. Ch 10 is designed to grow. A strand is woven by activity and never given a file or chapter of its own, except that a key characteristic gets its full account as its own Ch 10 sub-chapter (as 10.12 Fear, 10.13 Anger, 10.14 Humility, 10.15 Pride), with its angles also woven into the chapters they belong to, in context. Method: _analytics/essay/spirit_soul_body/wa-essay-narrative-weave-method-and-ch10-structure-*.

**B:89 change-of-character-recorded** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> How the meaning or application of the same word or concept changes in different circumstances is a key discovery and is built upon, never set aside. Every strand records each word's or concept's faces, the circumstances that differ, and why. A word's meaning is never taken from its cluster tag, since a tag shows one face only. Ch 11 section 4 ('What changes the character') is the cross-cutting account every strand adds to; the ledger is _analytics/cross-cluster-web/origin-of-thought/origin-of-thought-change-of-character-*.

**B:90 weaving-carries-meaning** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> Weaving applies the appropriate parts of the ledger work into other sections with interpretation; it is not a list of quotes or a mechanical mix and match. Rule 69 forbids joining verses into patterns no verse states; it does not forbid saying what a verse means in its own setting -- that interpretation is required. A phenomenon gets one coherent account answering what Scripture says it is, its forms from the words themselves, and why they differ. Other sections carry only the parts that belong to their activity, rewritten as prose with chosen verses, pointing back to the account; full verse lists stay in the ledger. A verse that says nothing about the inner being or the word stays in the data. Readings beyond what a verse states are marked 'I read'.

**B:91 narration-probes-not-restates** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> Narration is done from the perspective of the inner being's workings: restating a verse is not narration. Each item is thought about with probing questions -- compare; why different; what lies behind it; whether the relationships make a difference -- and figurative speech is explored, not restated. Each verse is read in its whole passage, with no reading framework laid over it; the account grows from the readings. A gap often sits in the neighbouring verses of a marked verse, so the whole passage is read.

**B:92 no-unnecessary-holding** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> Items are not held unnecessarily: verses or items that bear on the work in hand are read while the strand is busy with them, and accumulating outstanding items are completed, not parked behind another step.

**B:93 strand-checks-its-m47-verses** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> For each strand as it is taken up, its M47 (inner seat) verses are checked for dropped placements, by word and not by citation (a narrative citation is verse-level, not word coverage), as was done for M64 (#1989). The record is on OT-09.

**B:94 strand-pull-scans-glosses-across-codes** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> Before a theme is read, the glosses are scanned across all cluster codes, M and T alike: words for the theme may sit in T-codes that no strand ever pulled (e.g. the dead/die words, G3498 nekros and 16 others, found only when the researcher asked).

**B:95 verse-sets-only-through-raw-layer** · class study_method · enforced by: Context-delivered: printed in full at session start (Start-Iba.ps1) and restated in the session compliance file (rule 81).

> A strand's verse sets come only through the app's raw layer (New-Word, strong.reconcile), never through an inline STEP call.

**B:107 enumerate-link-tables-before-orphan-verdict** · class sqlite · enforced by: Context-delivered at session start (rule 81).

> Before a record is called unlinked, orphaned or unmapped, every junction or link table that references it is enumerated: linkage often lives in a subsidiary table.

**B:109 read-verses-before-asking** · class study_method · enforced by: Context-delivered at session start (rule 81).

> A question a verse reading could answer (e.g. whether a word belongs in a strand) is answered by reading the verses, never passed to the researcher.

**B:110 surface-is-the-sensitivity-lens** · class study_method · enforced by: Context-delivered at session start (rule 81).

> In any strand or word pull, verse_lexical.surface is analysed per Strong's first: the surface shows the different interpretations of the root that the gloss or suffix alone can miss.

**B:111 filters-are-working-aids** · class study_method · enforced by: Context-delivered at session start (rule 81).

> A pre-reading filter (e.g. buckets that split verses before reading) is a working aid the readings absorb; it is never raised as a standing decision item for the researcher.

**B:112 narrative-is-story-claims-are-derived** · class study_method · enforced by: Context-delivered at session start (rule 81).

> The narrative is the story and is never cut into claims. A claim is a statement derived from sources beyond the mere text of a verse; quoting a verse is not a claim (rule 77).

**B:113 bare-strong-decomposed-to-derivatives** · class study_method · enforced by: iba/app/lib/versescope.py (Resolver.decompose): every Strong's code a request names, the scope resolver

> Study work never works with a bare Strong's code. A bare code that is referenced (H0430) is always decomposed to its derivatives: every lettered code of that base that occurs in verse_lexical (H0430G, H0430H, ...). A bare code that occurs itself has no derivatives and is taken as it is, as is a suffixed code. The collection of verses taken into analysis may then be focused on a subset of the derivatives.

**B:114 synergise-from-tables-not-memory** · class study_method · enforced by: Context-delivered at session start while the study is active (rule 81); the tools of #2228 give the tables for a scope

> Study work runs in order: the scope is resolved (Verse-Scope.ps1), what is already known is collated for it, the gaps are recorded into the tables, and only then are claims finalised and the narrative written. That last step, synergising, is done only from the tables (observations, strand faces, claims and their sources, read through the app for the scope in hand), never from memory or recollection of earlier readings or of the conversation. The recording is finished first; a session may break between the end of recording and the start of synergising.

**B:115 open-item-has-a-clear-purpose** · class study_method · enforced by: iba/app/lib/openitem.py (Add/Reword/Split refuse an item with no target, read-for, why or comes-back-when, or over open_item.max_verses); Open-Item.ps1 -Action Review

> An open item is a pointer from the analysis in hand to related work, made so as not to interrupt that analysis: a record of related analysis to do, always cleared at some point, and always related to the core analysis that raised it. It is registered through Open-Item.ps1 with its origin and anchor, a target scoped to specific verses (a cluster item reads the target cluster's related term against the source analysis's strong, never the cluster as a whole), what to read for, why it is open, and when it comes back. One purpose per item: a wider target is split into separate items. An item without a clear purpose is not raised; open items are reviewed for stragglers (Open-Item.ps1 -Action Review).

**B:116 read-the-verse-first** · class study_method · enforced by: Context-delivered at session start while the study is active (rule 81), and at the first use of Reading.ps1 (cfg_rule_scope); the gap guides of cfg_setting reading.gap_types

> Study work starts by reading each verse in its passage and letting it say what it says. Reading is never itself a decision and is never held back. The rules on decisions (B:44), the written record (B:34), routing rulings, open items and gates act on what the reading found, and do not decide whether a verse is read. What the record says about a verse (a file's status, an item's wording, a ruling's summary) is not a reading of it.

**E:4 resolution_precedence** · enforced by: session practice (Claude Code) -- not mechanically enforced. The thread half is fed by Escalation.ps1 -Action ThreadCheck at session start (.claude/commands/start-project.md step 4B).

> Escalation resolution takes precedence over any other activity; open items with next_action_assigned_to='Claude' must be addressed before other work. For type='thread' (escalation #2000, rule T5): only threads at state 'in-progress' count -- a thread is in-progress only while an in-progress task or issue references it (an open 'escalation' item). An on-hold thread is never 'work first'.

**E:5 chat_routing** · enforced by: session practice (Claude Code) -- not mechanically enforced (nothing can reliably scan this session's own prose for 'looks like a deferred item'). Researcher caught a real violation live, 2026-08-16: 3 'deliberately not touched' items reported in one chat response, only 1 of which (a genuine judgement call, GOVERNANCE.md sec6) should have been escalated and wasn't until asked -- see escalation MANUAL-20260816_191254_734775.

> Chat discussions must be actioned through escalations -- the next action to work on arrives from an escalation, and the actions/steps identified are recorded in escalations, optionally by reference to a planning document that carries a whole package of tasks. Extended 2026-08-16: any judgement call reported only in chat prose (a 'left as-is', 'deliberately not touched', 'deferred' statement, or similar) that represents an actual open question or unfinished work -- not a closed decision with no further action possible -- must get its own escalation in the SAME turn it's mentioned, not after being asked. A closed, fully-reasoned decision (e.g. 'this historical record is correctly left unedited, nothing further to do') does not need one -- only genuine open items and judgement calls do. Extended 2026-08-20 (researcher direct instruction, this session): the rule applies symmetrically -- not only Claude's self-reported judgement calls, but any comment, correction, or feedback the RESEARCHER gives in chat that relates to an existing escalation, or that itself constitutes a genuine open item or judgement call, must be captured as part of an escalation (a new item, or an update to the item it relates to) by Claude in the same turn it is given, not left to live only in the chat transcript. The same closed-decision exemption above still applies -- a purely closed acknowledgement needs none. Extended 2026-08-21: content captured under this rule is recorded with the operative instruction or correction quoted VERBATIM -- the researcher's or Claude's own exact words for the substantive instruction/finding, not a paraphrase. Claude's own connective framing may surround it, clearly distinguishable from the quoted part.

**E:16 thread_check_before_work** · enforced by: Escalation.ps1 -Action Match -For nnnn [-Cluster ..] [-Strong ..] [-Verse ..] (lib/escalation.py match_threads); running the match is session practice.

> T1 (escalation #2000; researcher, round 1: 'open threads must be read before commencing with a task or issue, to determine if any threads relate to the task or issue escalation'). When a task or issue is raised, and before it is started (moved to in-progress), its clusters, Strong's numbers and verses are matched against the items of every thread not completed. Each match adds an 'escalation' item #nnnn to the thread. This is rule 4 redirected.

**E:18 thread_completion** · enforced by: cfg_escalation_requirement check_kind no_open_thread_items (update, resolve_self_correctable); cfg_escalation_transition (shape manual, priority 0); lib/escalation.py _sync_threads_for.

> T6 as amended by the thread lifecycle (escalation #2000; researcher 2026-10-12: 'I will give you feedback in the chat, the rest you need to control and the code must make it possible to manage the thread. all interaction must go to history'). Claude manages a thread's lifecycle; there is no approval step. An item is settled when it is closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread, named in the response). When an item change leaves no item open, the thread is completed in the same call, with a resolution generated from the closures; while items stay open, a partial settlement returns the thread to on-hold. A thread reaches completed or closed only when every item is settled. When a task or issue reaches a terminal state, its 'escalation' item on each thread takes the same ending: closed for completed/closed, withdrawn for withdraw, superseded for supersede. Withdrawing a thread withdraws its open items; superseding a thread names its successor (-SupersededBy OT-nn), and each open item moves to the successor and is recorded superseded. Every item response is written, in full, to the thread's history.

## Appendix 2. Method rules and quality checks in full

### `raw.verses` (stage 0.B)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 68 | spine-verse-span-strong-sync-fatal | verse, span, strong and cluster are the study's spine and must stay in sync: every live span belongs to a live verse and every live verse has live spans (a verse with no verse row at all is a gap by design, governance.verse_gap_by_design); every Strong's code a live span names (span.strong_variant) resolves to a live strong row; every such strong resolves through cluster_strong to a live cluster (governance.base_data_spine, extended 2026-09-21). A discovered desync is a FATAL ERROR, fixed on discovery, not merely logged or deferred -- researcher ruling 2026-09-10. handlers/spine.py checks all four; restated 2026-10-20 (#2173 G8): the check had covered span -> strong only. History: 409 span-referenced codes had no strong row on 2026-09-09 (#1613); 0 on 2026-10-20. | iba/docs/1613-meaning-layer-config-inventory-v1-20260909.md section17.1; escalation #1613, researcher ruling 2026-09-10 | handlers/spine.py compute(): all four checks (#2173 P3) |

### `lexical.readiness` (stage 0.B, also 0.GAP)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 69 | lexical-readiness-3leg-fatal | Before any Layer 1 (verse_lexical) rebuild scope runs, the base data must pass a 3-leg readiness check: every verse in scope has >=1 live span (Leg1); every span's strong code resolves to a live strong row (Leg2); every occurring strong has >=1 live cluster_strong allocation (Leg3). A FATAL finding on any leg blocks the run -- fixed on discovery, not deferred. Researcher ruling, escalation #1606, 2026-09-15: 'lexical readiness is a precursor for the lexical reading stage, which is a precursor for the sub group.' | escalation #1606; #1706 Phase A item 1; #1711 build | lexical.readiness (handlers/lexical.py:readiness) -- registered and live 2026-09-16, run before every Layer 1 build/rebuild |

### `lexical.build` (stage 0.B)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 44 | language-testament-derivation | language and testament are denormalized onto verse_lexical unconditionally, at build time — language = strong.language (verbatim copy); testament = 'OT' if cfg_book_order.ordinal<=38 else 'NT'. Both mechanical, no judgement, run on every row. | design doc §5.1/§3.E | **not enforced** |
| 45 | h0853-function-word-exception | H0853 (the Hebrew direct-object marker, stepGloss='[Obj.]') is classified role='function' — classify_role's H9xxx regex gets an explicit, evidence-commented exception set (starting with H0853), not a widened range. | design doc §4 | **not enforced** |
| 46 | lexical-code-class-lookup-not-hardcoded | Every code-classification lexicon (negator, connective-type, party_kind's divine/human/angelic classes) is a queried row in cfg_lexical_code_class, never a hardcoded list/dict in a handler. A code absent from the table is reported UNCLASSIFIED/NULL — never guessed, never silently defaulted. | catalogue-finishing doc §4; governance.rules_must_be_config_driven | **not enforced** |
| 47 | mechanical-columns-run-on-every-code-no-selection | position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/party_kind are computed for every verse_lexical row, unconditionally — none is selectively computed based on whether a code 'looks interesting.' Direct structural fix for the selective-attention drift found live 2026-09-03 (Gal 5:16-17, the G1063/G1937-G1939 misses). | method-and-drift-mitigation doc §1-2 | **not enforced** |
| 48 | narrative-morph-hebrew-only | narrative_morph is derived only for language='Hebrew' rows; Greek rows get NULL unconditionally — no guessed Greek chain-test equivalent exists yet. | design doc §3.G | **not enforced** |

### `spine.check` (stage 0.B, also 0.GAP)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 126 | spine-meaning-complete-against-step | Every live strong has its meaning in the three core meaning tables, which are the extracts from STEP: strong_sense (head), strong_meaning_tree (the range, by the exact code) and strong_lexicon (lsj and mounce, for the languages in spine.meaning_lexicon_languages). Complete means: matches what STEP holds for that Strong's, not what a table or a classification would lead one to expect. A local gap (no live row, or empty text) is asked of STEP for that code: STEP holding content the table lacks is a FATAL spine finding, fixed on discovery by pulling it into the table; STEP holding nothing is the only gap by design, and is listed as such. The parse tables stay retired and are not read. Researcher, 2026-10-20 (#2173 Q1), verbatim: "you need to check that each strong have its meaning, the three tables are the extracts from STEP, so it is not about which table, it depend on what the STRONG has in step. parsed table stay retired. the check is done directly to the three core meaning tables." | outputs/markdown/session-routines-start-project-change-proposal-v1-20261020.md (P3, Q1) | handlers/spine.py compute() (strong -> meaning), run by Spine-Check.ps1 and session-close SC2 |

### `lexical.meaning` (stage D1, also RECORD)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 70 | read-3-sources-complementary | Every strong's meaning is read from all 3 sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) as complementary evidence, never picking one and dropping the others. Researcher, verbatim, 2026-09-16: "the important take away is to read meaning from all three tables because they are complementary, rather than replacing each other." Inherited directly from process (c)'s own rule 2, not a new principle for this stage. | #1706 SS4A, 2026-09-16 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 71 | role-list-includes-unwired-tags | The role-annotated word list given to the LLM includes every live role-cluster tag (cluster.cluster_code T2-T15) on a strong, not only the mechanically-wired subset (role-T4/T5/T7/T8/T9). Researcher's own registry-construction principle applies: "the cost of over-inclusion is visible and recoverable; the cost of silent omission is invisible and not recoverable." Excluding the currently-unwired tags would silently reproduce the exact gap #1704's five-phase investigation diagnosed. | #1706 role-data-presentation doc SS6, 2026-09-17 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 72 | per-cluster-scope-not-subgroup | This stage runs per-cluster (all strongs the cluster's role list covers), anchored to the cluster as "home" -- not per-subgroup, since subgroups do not exist yet at this pre-subgroup stage. Confirmed scope grain, #1711 v11. | #1711 v11, 2026-09-16 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 73 | answers-M0.1-M0.5-D7.7 | This step's catalogue linkage (narrowed by the #1860 split, 2026-09-23): M0.1 (Name and Naming) derived from the strong's surface + its meaning in context; M0.5 (Lexical and Semantic Analysis) derived from the 3 meaning sources jointly -- both span-grounded, answered for every M-code strong's every occurrence (2026-09-23 correction, not once-ever per strong). The relational family (D7.7.1/M0.6.5/M0.6.6/M0.7/M0.8.1) moved to the new lexical.relational step, catalogue-linked there instead -- this step no longer answers them. | #1711 v11 + #1712 catalogue realignment, 2026-09-17 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 74 | needs-adjacent-verse-context-applies-here | needs_adjacent_verse_context applies at this stage too, not only char-reading -- the checklist's own cross-cutting rule 5a already governs every flag-shaped observation the pipeline raises. When raised, obs_text must state explicitly what's outstanding and what the follow-up cross-check needs to establish. | ib-observation-governing-rules-checklist rule 5a/5a-i/5b | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 75 | cost-bounded-small-batches | Never a full-cluster-corpus push in one call. Batches capped the same way lexical.enrich's own write path already enforces (passage.max_verses-sized chunks), cost estimated and shown before any live API call, per project_api_reads_budget_bounded_small_batches. | established project-wide convention, lexicalenrichgenerate.py precedent | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 77 | strongs-reassigned-detection | Any routine that changes cluster_strong membership for a cluster already past ordinal 2 (ready_for_subgroup_allocation or later) must call clusterstatus.flag_if_reassigned, which sets cluster.status=strongs_reassigned and raises a real decision_required escalation naming the cluster and the reason -- manual control only, no automatic resubmission of process (b), per the researchers own explicit instruction (#1697 v5). Found live 2026-09-17: no DB trigger or application hook implemented this at all despite the design requiring it -- confirmed by checking sqlite_master for triggers (none exist) and by the fact escalation #1714s own cluster_strong changes (to M59/M60/M67/M05) raised no such warning. | escalation #1697 v5 (design) + #1706 (this build, 2026-09-17) -- iba/app/lib/clusterstatus.py | lib/clusterstatus.py:flag_if_reassigned -- NOT YET WIRED into every cluster_strong-writing routine, only built and available to call |
| 108 | concise-and-verse-specific-obs-text | obs_text must be concise and tied to THIS specific verse/occurrence's own content -- state the finding directly, grounded in what this verse actually shows, not a free-standing restatement of the word's general/dictionary sense in your own varying prose. Two occurrences that genuinely show the same finding should produce recognisably similar, terse text (so the same/broaden/new duplicate check can actually recognise them as the same observation); padding, scene-setting, or restating background already given elsewhere in the payload adds nothing and actively defeats that check. Escalation #1824, 2026-09-21: confirmed live that generic, variably-worded obs_text caused the duplicate-detection mechanism to never once recognise two answers to the same question about the same strong as the same finding (0 of 378 real pairwise comparisons ever matched), even when they were restating the identical underlying fact. | - | **not enforced** |
| 111 | translit-never-without-gloss | A Greek or Hebrew transliteration or script term is never rendered in obs_text without its own gloss alongside it (e.g. spoude "earnestness" not bare spoude) -- the gloss is what carries the sense for a reader without Greek/Hebrew literacy, the bare form alone is unreadable. Restores a real, previously-decided rule (researcher, 2026-06-15, pre-IBA ve_lexical narration review) that never carried forward into this pipeline when it was rebuilt under IBA -- escalation #1836. | researcher 2026-06-15 review, restored via escalation #1836 (2026-09-22) | **not enforced** |
| 112 | span-grounded-not-generic | Every word-observation answer (any question code, any stage that answers about a specific M-code word) must be resolvable ONLY by consulting that occurrences own verse text, span, and morph_code -- if a question can be answered correctly without looking at any specific verse/span/morph (a pure lemma/strong-level lookup), the answer is generic and invalid for this pipeline. Sharing one canonical observation across multiple occurrences is permitted ONLY as a storage consolidation after independently-grounded per-occurrence answers are found to match exactly -- never assumed up front, never skipped because a strong already has an answer elsewhere. Researcher, verbatim, 2026-09-23: this has been the intent since approximately May 2026 (first flagged as wrong-values-for-word-analysis); it was never enforced in governance, config, catalogue wording, or code, and collapsed under its own weight as a result. | chat 2026-09-23, follow-on to escalation #1849/#1852 | versereadinggenerate.py/recordingpass.py/stage1coverage.py word-level path, rebuilt 2026-09-23 (escalations #1852/#1853) |

### `lexical.relational` (stage D1, also RECORD)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 113 | read-3-sources-complementary | Every strong's meaning is read from all 3 sources (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) as complementary evidence, never picking one and dropping the others. Researcher, verbatim, 2026-09-16: "the important take away is to read meaning from all three tables because they are complementary, rather than replacing each other." Inherited directly from process (c)'s own rule 2, not a new principle for this stage. | #1706 SS4A, 2026-09-16 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 114 | role-list-includes-unwired-tags | The role-annotated word list given to the LLM includes every live role-cluster tag (cluster.cluster_code T2-T15) on a strong, not only the mechanically-wired subset (role-T4/T5/T7/T8/T9). Researcher's own registry-construction principle applies: "the cost of over-inclusion is visible and recoverable; the cost of silent omission is invisible and not recoverable." Excluding the currently-unwired tags would silently reproduce the exact gap #1704's five-phase investigation diagnosed. | #1706 role-data-presentation doc SS6, 2026-09-17 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 115 | per-cluster-scope-not-subgroup | This stage runs per-cluster (all strongs the cluster's role list covers), anchored to the cluster as "home" -- not per-subgroup, since subgroups do not exist yet at this pre-subgroup stage. Confirmed scope grain, #1711 v11. | #1711 v11, 2026-09-16 | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 116 | needs-adjacent-verse-context-applies-here | needs_adjacent_verse_context applies at this stage too, not only char-reading -- the checklist's own cross-cutting rule 5a already governs every flag-shaped observation the pipeline raises. When raised, obs_text must state explicitly what's outstanding and what the follow-up cross-check needs to establish. | ib-observation-governing-rules-checklist rule 5a/5a-i/5b | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 117 | cost-bounded-small-batches | Never a full-cluster-corpus push in one call. Batches capped the same way lexical.enrich's own write path already enforces (passage.max_verses-sized chunks), cost estimated and shown before any live API call, per project_api_reads_budget_bounded_small_batches. | established project-wide convention, lexicalenrichgenerate.py precedent | lexical.meaning (handlers/lexical.py:meaning) -- registered 2026-09-17 |
| 118 | strongs-reassigned-detection | Any routine that changes cluster_strong membership for a cluster already past ordinal 2 (ready_for_subgroup_allocation or later) must call clusterstatus.flag_if_reassigned, which sets cluster.status=strongs_reassigned and raises a real decision_required escalation naming the cluster and the reason -- manual control only, no automatic resubmission of process (b), per the researchers own explicit instruction (#1697 v5). Found live 2026-09-17: no DB trigger or application hook implemented this at all despite the design requiring it -- confirmed by checking sqlite_master for triggers (none exist) and by the fact escalation #1714s own cluster_strong changes (to M59/M60/M67/M05) raised no such warning. | escalation #1697 v5 (design) + #1706 (this build, 2026-09-17) -- iba/app/lib/clusterstatus.py | lib/clusterstatus.py:flag_if_reassigned -- NOT YET WIRED into every cluster_strong-writing routine, only built and available to call |
| 119 | concise-and-verse-specific-obs-text | obs_text must be concise and tied to THIS specific verse/occurrence's own content -- state the finding directly, grounded in what this verse actually shows, not a free-standing restatement of the word's general/dictionary sense in your own varying prose. Two occurrences that genuinely show the same finding should produce recognisably similar, terse text (so the same/broaden/new duplicate check can actually recognise them as the same observation); padding, scene-setting, or restating background already given elsewhere in the payload adds nothing and actively defeats that check. Escalation #1824, 2026-09-21: confirmed live that generic, variably-worded obs_text caused the duplicate-detection mechanism to never once recognise two answers to the same question about the same strong as the same finding (0 of 378 real pairwise comparisons ever matched), even when they were restating the identical underlying fact. | - | **not enforced** |
| 120 | translit-never-without-gloss | A Greek or Hebrew transliteration or script term is never rendered in obs_text without its own gloss alongside it (e.g. spoude "earnestness" not bare spoude) -- the gloss is what carries the sense for a reader without Greek/Hebrew literacy, the bare form alone is unreadable. Restores a real, previously-decided rule (researcher, 2026-06-15, pre-IBA ve_lexical narration review) that never carried forward into this pipeline when it was rebuilt under IBA -- escalation #1836. | researcher 2026-06-15 review, restored via escalation #1836 (2026-09-22) | **not enforced** |
| 121 | span-grounded-not-generic | Every word-observation answer (any question code, any stage that answers about a specific M-code word) must be resolvable ONLY by consulting that occurrences own verse text, span, and morph_code -- if a question can be answered correctly without looking at any specific verse/span/morph (a pure lemma/strong-level lookup), the answer is generic and invalid for this pipeline. Sharing one canonical observation across multiple occurrences is permitted ONLY as a storage consolidation after independently-grounded per-occurrence answers are found to match exactly -- never assumed up front, never skipped because a strong already has an answer elsewhere. Researcher, verbatim, 2026-09-23: this has been the intent since approximately May 2026 (first flagged as wrong-values-for-word-analysis); it was never enforced in governance, config, catalogue wording, or code, and collapsed under its own weight as a result. | chat 2026-09-23, follow-on to escalation #1849/#1852 | versereadinggenerate.py/recordingpass.py/stage1coverage.py word-level path, rebuilt 2026-09-23 (escalations #1852/#1853) |
| 122 | answers-relational-family | This step's catalogue linkage (#1860 split, 2026-09-23): D7.7.1 (operation-anchored permeability, role-T3), M0.6.5 (relational, single-vantage), M0.6.6 (whole-network synthesis), M0.7.1-16 (verse substantiation), M0.8.1 (T2/T3 elevation flag) -- all answered for EVERY M-code strong present in roles_in_verse, cluster-agnostic (escalation #1824 v14/v15). Fed progressively via each question's own prior-context stream (M0.6.5/M0.6.6, per-verse not globally-once) so a later pass builds on, not duplicates, what's already there; does not even attempt an already-fully-covered verse (whole-verse batch exclusion). Requires lexical.meaning to have already committed M0.1/M0.5 for every M-code word in scope (readiness gate) -- moved out of the combined lexical.meaning rule this step inherits from (id 73, pre-split). | #1860, 2026-09-23 word-level/relational split | lexical.relational (handlers/lexical.py:relational) |
| 123 | cluster-status-2to3-transition-verse-reading-complete | cluster.status advances from t_cluster_assignment_completed (ordinal 2) to ready_for_subgroup_allocation (ordinal 3) automatically, only when every one of the clusters live member strongs has at least one verse-reading-stage ib_observation row. Checked and advanced at the end of every live (non-preview) lexical.meaning run against the clusters full resolved verse list. Found live 2026-09-17: this transition was designed (escalation #1697) but never built -- confirmed all 80 live clusters stuck at ordinal 2 with no code anywhere that ever advanced one. | escalation #1697 (design) + #1706 (this build, 2026-09-17) -- iba/app/lib/clusterstatus.py | lib/clusterstatus.py:advance_if_verse_reading_complete, called from handlers/lexical.py:relational (moved from lexical.meaning, #1860 2026-09-23) |
| 124 | grounds-on-committed-word-level-observations | Relational reading's primary grounding is the COMMITTED word-level (M0.1/M0.5) ib_observation rows for the exact verse+strong being reasoned about (versereadinggenerate._word_level_findings), not the raw lexicon alone. Researcher, verbatim, escalation #1860 v3 approval, 2026-09-23: 'the base data must in any case be included for relational phase to be successful' -- corrects Claude's own original v1 draft, which had proposed committed findings INSTEAD OF raw meaning_sources_by_strong; both are sent together, the committed findings as primary grounding, the raw lexicon as the same complementary evidence every other stage already reads (read-3-sources-complementary). | #1860 v3 researcher approval, 2026-09-23 | versereadinggenerate._word_level_findings, called from assemble_relational_batch_package |
| 125 | relational-readiness-gate | lexical.relational refuses to run (hard stop, same shape as lexical.build's stale-role check and lexical.readiness's FATAL stop -- not a silent per-verse skip) against any verse whose M-code words don't ALL already have a committed (non-withdrawn) word-level (M0.1/M0.5) ib_observation. stage1coverage.missing_word_level_coverage() computes the gap; -Force does NOT bypass this gate (unlike the whole-verse-exclusion optimisation) -- it is a correctness precondition, not a reconciliation-skip mechanism. Researcher instruction, verbatim, #1860 v1 context: 'the relational process depends on the word work, and doing it in the same session can only result in errors.' | #1860 v1 context, 2026-09-23 | stage1coverage.missing_word_level_coverage, called from handlers/lexical.py:relational |

### `cluster.subgroup` (stage D2, also RECORD)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 78 | full-cluster-read-before-assignment | All gloss and surface values for every strong in the cluster must be read FIRST, before subgroup assignment begins for any of them -- not a streaming process that assigns strongs one at a time as they're read. #1690 §2(a), researcher's own instruction, 2026-09-13. | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 79 | meaning-based-not-surface-similar | Subgroups are grouped on actual shared meaning, not on strongs whose glosses merely look alike or share superficial wording. #1690 §2(b). | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 80 | max-10-subgroups-flag-excluded | A cluster's real (non-FLAG) subgroups top out at 10 -- FLAG is a signpost bucket, not a subgroup competing for that budget, and is excluded from this cap. #1690 §2(c). | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 81 | label-true-to-essence-not-wordlist | label must be true to the subgroup's essence, not an enumeration of its member glosses -- a label that names what the subgroup actually IS. #1690 §2(d). | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 82 | singleton-subgroup-valid | A subgroup may legitimately hold exactly one strong, if that strong's meaning is genuinely unique and doesn't fit any other subgroup -- a singleton is a valid outcome, not a sign of mis-grouping needing correction. #1690 §2(e). | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 83 | flag-conditions-and-reason-required | A strong is assigned to FLAG when it (i) has no inner-being implication, (ii) actually belongs to another cluster, or (iii) has some other anomaly preventing assignment -- always with the reason recorded in placement_note (REQUIRED for FLAG placements). #1690 §2(f)/§3 item 3. FLAG is a signpost, not a resolution in itself -- corrective action is to re-allocate the strong or resolve the underlying issue elsewhere, never decided by this stage. | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 84 | placement-note-captures-any-observation | placement_note is not FLAG-only -- any observation arising from a subgroup assignment is captured there, optional but available for any ordinary placement too. #1690 §2(g). | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 85 | anchor-verse-llm-selected | For each real subgroup, select the one verse from its own membership that best describes/represents the subgroup's shared characteristic -- a judgement call made in this same pass, not a separate metric (word count, verse length, frequency). #1690 §2(h)/§2A. FLAG has no anchor verse (it is not a real subgroup). | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |
| 86 | one-strong-one-subgroup | Every strong is placed in exactly one subgroup (including FLAG) -- structurally enforced by cluster_subgroup_strong's UNIQUE(strong) constraint downstream, but the LLM's own output must already respect it: a strong never appears under two subgroup_codes. #1690 §2 item 2. | #1690 (2026-09-13), #1706 (this build, 2026-09-17) | cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17 |

### `cluster.reading` (stage D2, also RECORD)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 87 | per-subgroup-never-whole-cluster | Always run per subgroup -- never the whole cluster in one pass. #1682 §2 rule 1. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 88 | read-3-sources-complementary-reading | Read all three meaning sources in full for every strong, every time -- never dump raw text unread, never skip a source. Inherited directly from lexical.meaning's own rule of the same substance, applied here at subgroup grain. #1682 §2 rule 2. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 89 | scan-every-occurrence-no-sampling | Scan every verse occurrence of every subgroup member strong, corpus-wide -- no sampling, regardless of strong or subgroup size. A high occurrence count is never a reason to sample or silently drop instances; it is a reason to raise the occurrence cap or split the subgroup, never to sample quietly. #1682 §2 rule 3. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 90 | grouping-never-excuses-skipping | Similar verses may be grouped where their meaning is genuinely alike, but grouping does not excuse skipping any instance -- every occurrence is still accounted for individually in the trace. #1682 §2 rule 4. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 91 | every-instance-states-what-it-is | Every instance states what it is -- a positive reading, not only a contrast with other instances. #1682 §2 rule 5. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 92 | not-a-single-distilled-meaning | The aim is not a single distilled meaning -- show what a verse's or strong's meaning could be or is likely to be, including alternative candidate readings where the data supports more than one. #1682 §2 rule 6. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 93 | difference-is-its-own-observation | A difference or a specific inference is recorded as its own, separate observation -- never folded silently into the main per-instance reading. #1682 §2 rule 7. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 94 | cross-strong-comparison-is-this-stages-own-task | This stage's own distinct value beyond Stage 1: synergise the similar and different contextual meaning of THIS SUBGROUP'S member strongs against each other -- where they genuinely share meaning and where they diverge, given their full occurrence lists and Stage 1/2's own prior observations as grounding. Do not re-derive or duplicate Stage 1's own per-occurrence M0.1/M0.5 findings. #1682 §2 (objective), this build's own scoping. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 95 | morph-actively-read-not-merely-carried | span.morph must be actively read, not merely carried -- where occurrences of the same strong show different stems/voices, check whether the variation is meaning-relevant (does the subject DO the action, HAVE it done to them, or CAUSE another to do it); record a real distinction as its own difference-inference, and record a genuine no-distinction-found result too, not silence. #1682 §2 rule 9. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 96 | per-strong-traceability-verified-by-code | Per-strong traceability is verified before that strong's reading counts as done -- every occurrence from its full corpus-wide list must be cited in >=1 observation's occurrences for it. Computed by CODE after the write (recordingpass has already written the observations), never trusted from an LLM self-report -- an improvement on the original 2026-09-11 spec's self-reported strong_checks, consistent with question_code/tag/obs_text never being trusted from the model either. #1682 §2 rule 10, this build's own architecture correction. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 97 | homonym-no-context-earmarked-and-left | A strong that is exclusively a homonym/name with no meaningful context for a human reader is earmarked as such (tag no-human-context) and left there -- no further analysis attempted. #1682 §2 rule 11. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 98 | data-errors-flagged-separately | Data-quality issues found while reading (wrong cluster/subgroup membership, a broken span/verse link, a corrupted meaning source) are flagged as tag data-error, in their own section, never chased down or fixed as part of this process. #1682 §2 rule 13. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 99 | reread-includes-existing-rows | If this is a re-read of a subgroup already in the database, the input includes that subgroup's existing char-reading ib_observation rows, so the model sees prior findings rather than starting blind. #1682/checklist §2 rule 17. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 100 | role-driven-walk-not-forced | The role-driven-walk is NOT a structural gate at this stage -- checklist rule 14's own 'structurally forced' framing was superseded 2026-09-17 (researcher: 'no further mechanical role work necessary... the question is expanded to explore the impact of the roles'), confirmed closed 2026-09-18 against three stale docs still citing it as pending (#1706 v34). Recorded here explicitly so this stage's own build doesn't reintroduce the retired framing. | #1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §2, #1706 (this build, 2026-09-18) | cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18 |
| 109 | concise-and-verse-specific-obs-text | obs_text must be concise and tied to THIS specific verse/occurrence's own content -- state the finding directly, grounded in what this verse actually shows, not a free-standing restatement of the word's general/dictionary sense in your own varying prose. Two occurrences that genuinely show the same finding should produce recognisably similar, terse text (so the same/broaden/new duplicate check can actually recognise them as the same observation); padding, scene-setting, or restating background already given elsewhere in the payload adds nothing and actively defeats that check. Escalation #1824, 2026-09-21: confirmed live that generic, variably-worded obs_text caused the duplicate-detection mechanism to never once recognise two answers to the same question about the same strong as the same finding (0 of 378 real pairwise comparisons ever matched), even when they were restating the identical underlying fact. | - | **not enforced** |

### `cluster.answer` (stage D2, also RECORD)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 101 | per-subgroup-answer-never-whole-cluster | Always run per subgroup -- same discipline as reading, never the whole cluster in one pass. #1682 §4A / checklist §3 rule 1. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 102 | multiple-slants-not-one-distilled-answer | Where a subgroup's own strongs or evidence genuinely point to different answers to the same catalogue question, every distinct slant is its own observation, all under the same question_code, each with its own evidence trail -- never flattened into one 'the characteristic means X' answer. A single slant is correct only when the evidence actually is uniform, not a default. #1682 §4A / checklist §3 rule 2. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 103 | scope-level-governs-evidence-trail | A slant grounded in one specific member strong sets `strong` to that code and cites its own occurrences. A slant grounded in the subgroup as a whole leaves `strong` null on the observation but requires every occurrence to carry its own `strong` field -- an occurrence with no strong of its own cannot be resolved. #1682 §4A / checklist §3 rule 3. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 104 | adjacent-context-flagged-not-fetched-answer | Where answering a question properly would need surrounding verses beyond what this subgroup's own evidence carries, flag needs_adjacent_verse_context with the reason stated explicitly in obs_text -- never fetched ad hoc mid-run. Resolution happens in a later analytic run (expected to be the synergy stage), not chased down here. #1682 §4A / checklist §0 rule 5a / §3 rule 4. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 105 | cross-family-flagging-out-of-scope-this-build | Cross-family/cross-cluster relevance is explicitly OUT OF SCOPE for this stage's current build -- do not attempt it. Its own tag value is not yet chosen (checklist's own still-open-items list); inventing one here would bake a design decision into a code build rather than apply one already made. #1682 §4A / checklist §3 rule 5, deliberately deferred. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 106 | battery-scope-excludes-verse-reading-and-science-extract | This stage answers the catalogue's characteristic-grain battery only (scope in Characteristic (HIB behaviour)/Characteristic relational/The HIB/Other non-human beings), excluding D7.7.1 (already Stage 1's own territory, per-verse) and every question whose text depends on the cluster's science-extract file (deferred to the science stage: science chapters come later, per CLAUDE.md). Queried live from wa_obs_question_catalogue at call time, never hardcoded, so a catalogue change is picked up automatically. This build's own scoping, 2026-09-18. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 107 | per-question-completeness-verified-by-code | Per-question completeness (did every battery question_code get answered for this subgroup) is computed by CODE after the write, via ib_node's own strong citations against this subgroup's member strongs -- never trusted from an LLM self-report, same discipline as Stage 3's per-strong traceability check. This build's own architecture, 2026-09-18. | #1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-20260916.md §3, #1706 (this build, 2026-09-18) | cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18 |
| 110 | concise-and-verse-specific-obs-text | obs_text must be concise and tied to THIS specific verse/occurrence's own content -- state the finding directly, grounded in what this verse actually shows, not a free-standing restatement of the word's general/dictionary sense in your own varying prose. Two occurrences that genuinely show the same finding should produce recognisably similar, terse text (so the same/broaden/new duplicate check can actually recognise them as the same observation); padding, scene-setting, or restating background already given elsewhere in the payload adds nothing and actively defeats that check. Escalation #1824, 2026-09-21: confirmed live that generic, variably-worded obs_text caused the duplicate-detection mechanism to never once recognise two answers to the same question about the same strong as the same finding (0 of 378 real pairwise comparisons ever matched), even when they were restating the identical underlying fact. | - | **not enforced** |

### `hib.set` (stage RETIRED)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 1 | presumptive-candidate | Every human mentioned -- named or collective, major or minor, however briefly -- is a presumptive candidate: anyone who acts, undergoes an act, thinks, speaks, refrains from acting, or is simply named as present. This holds even where the act looks purely outward, administrative, locational, or incidental -- the inner-being content may be hidden behind the act, with only the act stated in the text. | WA-passage-read-guidance-v1.5 step 2 note f | **not enforced** |
| 2 | non-human-scope | HIB = Human Inner Being. A non-human being can NEVER itself be registered as a HIB, by definition -- not conditionally, not when related to a human. A non-human being (an animal in a symbolic vision, an angel, a voice or other physical medium) may only appear as a source/target/related-object PARTY within a human HIB's own operation (operation_party.kind='non_human') -- never as its own hib row, phenomenon, or operation. Where a vision depicts a human king/kingdom in animal or symbolic form and the text itself resolves that image (e.g. Dan 8:20-23), the HIB is the resolved HUMAN referent, registered from its first (symbolic) appearance onward -- not the animal/image itself as a separate entity. Superseded 2026-08-06 (same day as the first wording): the original text still allowed a non-human being 'in scope' as its own HIB when related to a human (e.g. an angel) -- corrected directly by the researcher: 'a non human by definition cannot be a HIB.' | WA-passage-read-guidance-v1.5 step 2 notes b, d | **not enforced** |
| 3 | collective-stays-collective | A tribe, nation, 'youths', 'gentiles' etc. is recorded as ONE HIB representing the collection -- not decomposed into individuals; any later operation involving it is a movement to/from a collection, not an individual. | WA-passage-read-guidance-v1.5 step 2 note c | **not enforced** |
| 4 | referential-named-not-skipped | Where a party is unnamed but implied by the verse or wider passage, name it as a referential HIB; never assert an inferred identity as settled fact. | WA-passage-read-guidance-v1.5 step 2 note e | **not enforced** |
| 5 | referent-crux-resolution | Where a pronoun or unnamed party is genuinely ambiguous (several readings all grammatically live), enumerate every live reading, give the textual grounds for each, adopt one explicitly (stating whether this is a directed/researcher call or this pass's own default), and keep the rejected alternatives on record. | debate-analytic-process-digest-20260805.md Step 1 (T4 folded in) | schema: hib_referent_option |
| 6 | six-type-scheme | Every HIB is typed along two axes: plurality (individual / collection) x specificity (named / unnamed / implicit) = six types: named_individual, unnamed_individual, named_collection, unnamed_collection, implicit_individual, implicit_collection. | nahum-1-inner-being-training-20260803.md (researcher's own training pass) | cfg_enum 'hib_kind' + operations.py:_valid_hib_kinds |
| 7 | db-compare-adjudicate | Read the verses in scope; compare the fresh reading against what's already in the DB; validate the list against the DB; where the fresh reading differs, adjudicate and correct the DB -- not blind re-derivation. | researcher direction, 2026-08-06 | operations.py:_reconcile |

| Check | Question | Kind | Required | Enforced by |
|---|---|---|---|---|
| kind-enum-membership | Is hib.kind one of the six live enum.hib_kind values (not free text)? | existence | 1 | cfg_enum 'hib_kind' + operations.py:_valid_hib_kinds |
| is-genuinely-human | Does this candidate actually refer to a human being as Step 1 defines it -- not a non-human being whose state happens to be described in human-like terms, and not a place, object, or abstraction personified only grammatically? | reasonableness | 1 | **not enforced** |
| not-already-excluded | Has this exact referent already been recorded as out-of-scope for this book/passage (e.g. explicitly set aside per step 2 note d), and is this entry silently reintroducing it without new textual grounds? | non_existence | 1 | **not enforced** |
| verse-actually-supports-it | Does the cited verse's own text (lexical row-level data, not the paraphrased English gloss) actually support this HIB being present, or is the entry drifting from what the verse itself states? | reasonableness | 1 | **not enforced** |

### `passage.build` (stage RETIRED)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 28 | story-organized-by-hib | The story synthesis is told through the passage's own cast, not as a generic plot summary -- the dominant HIB's own arc as the spine, others introduced as they bear on it. A story that reads identically with the HIB list deleted has not done this step's job. | researcher direction, 2026-08-07 | **not enforced** |
| 31 | input-scope-is-the-passage | A passage is the debate's own input scope, registered verbatim -- never sub-divided by algorithm. | researcher direction, 2026-08-06, following the HIB-distribution visualization | passage.py:build |
| 32 | story-synthesis-required | Step 2's real output is a high-level story synthesis for the scope, read in light of the identified HIBs -- not a derived boundary. | researcher direction, 2026-08-06 | schema: passage.story_summary |
| 33 | feasibility-self-assessment | Before registering a passage, self-assess whether the scope can be read as a whole without quality loss; if not, the debate is skipped with a message to revise the input scope, not silently sub-divided. | researcher direction, 2026-08-06 | passage.py:build (scope-too-complex refusal) |
| 34 | one-passage-per-verse | A verse belongs to at most one live passage at a time. | app convention (DB-enforced: verse_passage.verse_id unique) | schema: verse_passage unique constraint + passage.py:build's overlap check |
| 35 | legacy-superseded-unconditionally | A legacy (pre-redefinition) passage overlapping a newly-registered scope is superseded wholesale -- "not reconciling the old with the new." | researcher direction, 2026-08-05/06 | passage.py:build |

| Check | Question | Kind | Required | Enforced by |
|---|---|---|---|---|
| boundary-not-arbitrary | Is the feasibility_note a genuine, specific reading judgement about THIS scope -- not a reflexive "yes it is fine" answer given without actually working through the HIB relationships in it? Would a second, independent read of this scope plausibly reach the same feasible/infeasible call for the same reasons? | reasonableness | 1 | **not enforced** |

### `phenomenon.set` (stage RETIRED)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 13 | phase-separation | The phenomena register (Phase 1) must be completed for the WHOLE passage before any operation (Phase 2) is written for ANY verse in it -- not interleaved verse-by-verse. Running Phase 2 immediately after Phase 1 verse-by-verse reopens the same drift, since operation-writing momentum can bleed back into how the next verse's phenomenon gets identified. | WA-passage-read-guidance-v1.5 Phase 1/Phase 2 structure + its own 2026-08-02 change-control note (the direct fix for the Amos 1-3 drift) | operations.py:phenomenon_set (passage.phenomena_complete_at gate) + operations.py:operation_set (refuses while NULL) |
| 14 | hidden-behind-act | A phenomenon may be hidden behind a stated act or a refrained-from act, with only the act recorded in the text -- naming what the act is taken to evidence is exactly this step's job. | WA-passage-read-guidance-v1.5 step 3 note e | **not enforced** |
| 15 | warrant-required | For every phenomenon isolated, record the specific textual warrant that grounds it (the verb, clause, or stated silence) and whether it is stated or inferred -- its own register entry, written before and independently of any operation. | WA-passage-read-guidance-v1.5 step 3b | schema: phenomenon.textual_warrant/status |
| 16 | not-literary-pattern | A genuine literary/structural/genre observation is not a phenomenon -- log it once as an emergent question (Step 7) instead, never built into the phenomena register. | WA-interpretation-questions-v1.4 Part B.12; WA-passage-read-guidance-v1.5 step 6 note c | **not enforced** |
| 17 | control-total | Every HIB crossed with every verse it appears in, in this passage, equals the exact number of phenomena-register entries (including explicit 'silent' entries) Step 3 must produce before it can be considered done -- known in advance, not dependent on trusting the pass to remember to cover everything. | debate-analytic-process-digest-20260805.md Step 3 'how this gets controlled'; b3-b5-operations-schema-design-20260805.md | operations.py:phenomenon_set (verse_hib pair-set vs live phenomenon pair-set comparison) |
| 18 | silence-is-a-finding | 'No phenomenon found, silent' is a valid RESULT of running the phenomenon check on a human-bearing clause, not an omission -- and not a valid substitute for running the check. | WA-interpretation-questions-v1.4 Part B.4; WA-passage-read-guidance-v1.5 step 2 note f | schema: phenomenon.status='silent' |
| 29 | hib-first-traversal | Work HIB-by-HIB, not verse-by-verse: start with the passage's most dominant HIB (highest verse-count cross-checked against the story's own throughline), read every verse that HIB appears in against its own verse_lexical row (full range, not the story or the printed gloss), complete that HIB's full phenomena list, then move to the next HIB. Stay inside phenomenon-only territory throughout -- no reasoning yet about source/target or cross-HIB movement (see operation.set's hib-fanout-dimensions rule). | researcher direction, 2026-08-07 | **not enforced** |
| 41 | hib-still-warranted | Once a HIB's phenomena list is complete across the whole passage, review whether it still genuinely warrants being a HIB at all -- if there is no inner-being role or effect anywhere, and no reasonable basis to infer one, go back and correct hib.set (remove, with reason) before treating this HIB's phenomena as final. Distinct from silence-is-a-finding: a HIB with some or all silent entries is not automatically suspect -- silence is a legitimate result. This rule is for a HIB that, on full review, was never a genuine candidate in the first place. | researcher direction, 2026-08-07 | **not enforced** |
| 42 | full-lexical-weight-in-description | A phenomenon's description must draw on the word's actual full lexical range (the whole meaning_tree entry for its governing Strong's code, per T2) -- not a brief, generic, or stereotyped label. The specific sense operative in THIS context, in its own fullness, is where the phenomenon's real content resides; flattening it into a stock gloss compromises that content. Context-specific, every time -- never a reusable stock phrase. | researcher direction, 2026-08-07 | **not enforced** |

| Check | Question | Kind | Required | Enforced by |
|---|---|---|---|---|
| genuinely-inner-being | Is this phenomenon actually a state, disposition, or characteristic of the HIB's inner life -- not a purely outward/administrative fact restated without any interior content identified? | reasonableness | 1 | **not enforced** |
| not-a-literary-pattern | Is this entry a genuine per-verse, per-HIB phenomenon -- not a textual/structural pattern (recurring formula, book-wide thesis) smuggled in as if it were one (Part B.12)? | non_existence | 1 | **not enforced** |
| warrant-is-specific | Does textual_warrant name an actual verb/clause/stated silence in this verse, not a vague restatement of the description field? | existence | 1 | **not enforced** |
| hib-still-warranted | Having completed this HIB's full phenomena list for the passage, does it still genuinely warrant being a HIB -- or has the review revealed hib.set needs correcting (and has that correction already been submitted)? | reasonableness | 1 | **not enforced** |
| description-uses-full-lexical-range | Does this description draw on the governing word's full lexical range and its specific contextual sense here -- not a brief, generic, or stereotyped label that could apply to any similar-sounding phenomenon regardless of context? | reasonableness | 1 | **not enforced** |
| stated-or-inferred-honestly-assigned | Having recorded whether this phenomenon is stated or inferred (step 3b), is that classification itself honest -- not a stated status quietly assigned to what the textual_warrant actually shows is inferred, or vice versa? | reasonableness | 1 | **not enforced** |

### `operation.set` (stage RETIRED)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 19 | operation-from-phenomenon-only | An operation may only originate from an already-registered phenomenon -- never identify a fresh phenomenon while writing one. If writing an operation reveals no genuine phenomenon underlies it, the Step 3 entry was mis-identified -- go back and correct it; do not paper over the mismatch. | WA-interpretation-questions-v1.4 Part B.12 | schema: operation.phenomenon_id NOT NULL + operations.py:operation_set |
| 20 | four-parts | Every operation has: process (a state/status, or a movement -- come from / go to / impact on / emerge / go away / become evident); source; target; and an action-type label. Source and target may be singular, multiple, mixed, or non-existent. | WA-passage-read-guidance-v1.5 step 1 note a | schema: operation + operation_party |
| 21 | source-vs-enablement | Keep source of the interior state and source of enablement to act distinct -- a non-human being may be the stated source of an outcome or an enablement without the text sourcing the actor's own disposition; extending sourcing from outcome to interior is an interpretive step to flag, never to assume. | WA-interpretation-questions-v1.4 Q4 / Part B.5 | schema: operation_party.enablement_only |
| 22 | action-type-is-a-label | The action-type is a short, natural, verb-based tag (e.g. 'gave', 'summoned/complied', 'worshiped') -- a label for cross-passage/cross-book comparison, not a taxonomy; no controlled vocabulary is being built. | WA-interpretation-questions-v1.4 Q11 / Part B.10 | schema: operation.action_type (free text) |
| 23 | divine-mirroring-anchored | Record a human/divine operation comparison (juxtaposition, difference, inversion) only where the text's own juxtaposition or wording anchors it -- a merely plausible resemblance is logged as an emergent question, never asserted or theologically elaborated. | WA-interpretation-questions-v1.4 Q12 / Part B.11 | **not enforced** |
| 24 | decision-enum | decision = retain / set_aside / retain_referential / recorded_silence. | WA-interpretation-questions-v1.4 Part C section 3 | schema: operation.decision (free text, not yet enum-enforced -- see cfg_enum follow-up) |
| 27 | hib-can-be-party-in-another-hibs-operation | A HIB can be a party within another HIB's own operation (e.g. a king acting against Daniel) -- operation_party.kind='human', with an optional hib_label naming the other HIB (resolved to operation_party.hib_id, a real structural link) alongside the existing free-text detail. Corrected 2026-08-07 (debate-schema-traceability-gap-findings-20260807.md, Finding 2): detail alone was NOT sufficient traceability -- only 3 of 42 live detail values matched a hib.label even as text; hib_id is now the real link, detail stays as a human-readable gloss alongside it, not a replacement for it. Distinct from a non-human party (kind='non_human'), which never gets its own hib/phenomenon/operation rows at all (see non-human-scope). | researcher direct correction, same session as dan8-debate-run-failure-review-20260806.md | schema: operation_party.hib_id (FK -> hib.id) + operations.py:operation_set hib_label resolution |
| 30 | hib-fanout-dimensions | Fanning out from the focused HIB to the rest of the passage's cast has three distinct dimensions: (A) another HIB as source/target within the focused HIB's own operation; (B) the mirror once focus switches to that other HIB, checked for consistency, not re-derived; (C) movement/process BETWEEN two different HIBs' already-registered phenomena/operations, which belongs to closing.set's passage_linkage (Q7), not to operation.set itself. Only (A) and (B) are this step's job. | researcher direction, 2026-08-07 | **not enforced** |
| 43 | full-lexical-weight-in-observation | The same discipline as phenomenon.set's full-lexical-weight-in-description rule, applied to an operation's observation_text/description_text: draw on the governing word's full lexical range, in this exact context, not a brief generic label. Distinct from action_type (a short label, deliberately -- action-type-is-a-label) -- observation/description text is where the full weight belongs. | researcher direction, 2026-08-07 | **not enforced** |

| Check | Question | Kind | Required | Enforced by |
|---|---|---|---|---|
| phenomenon-actually-underlies-it | Having written this operation, does a genuine phenomenon actually underlie it -- or has writing the operation revealed the Step 3 entry was mis-identified and needs correcting (Part B.12)? | reasonableness | 1 | **not enforced** |
| source-target-not-invented | Are the source/target parties actually named or clearly identifiable in the verse/passage, not invented to complete the operation's shape? | non_existence | 1 | **not enforced** |
| observation-uses-full-lexical-range | Does observation_text/description_text draw on the governing word's full lexical range and its specific contextual sense here -- not a brief, generic, or stereotyped label? | reasonableness | 1 | **not enforced** |

### `closing.set` (stage RETIRED)

| id | Rule | Text | Source document | Enforced by |
|---|---|---|---|---|
| 36 | linkages-q7 | What linkages run to other operations in the passage? Where a linkage is absent, surface the absence; do not pass over it silently. A Q7 linkage connects two specific, already-registered phenomena/operations to each other -- it is not licence to narrate a pattern across a whole chapter range. | WA-interpretation-questions-v1.4-2026-08-02.md Part A Q7 / Part B.12 / Part C item 4 | schema: passage_linkage |
| 37 | insufficiencies-register | Where required data (e.g. name etymologies) is absent from the base extract, name it as an insufficiency; do not substitute remembered or external knowledge. | WA-interpretation-questions-v1.4-2026-08-02.md Part B.7 / Part C item 5 | schema: passage_insufficiency |
| 38 | emergent-questions-log | Interpretive forks and genuine literary/structural observations are carried forward here. An interpretive fork is NOT a researcher decision awaiting a ruling -- it is named where it bites, weighed against each new data point as the corpus grows, and answered (or left open) by what the accumulating evidence actually shows, not settled in the abstract before the evidence is in. "The researcher should decide" is reserved for genuine resourcing/data-curation choices this instrument cannot make for itself, not for interpretive questions the study itself exists to answer. Not merged with other passages' logs. | WA-interpretation-questions-v1.4-2026-08-02.md Part A Q10 / Part B.8-B.9 / Part C item 6 | schema: passage_emergent_question |
| 39 | debate-quality-validation | Once the phenomena register and operations are assembled: a re-examination, for each phenomenon or a representative sample spanning the range, of whether it is genuinely an inner-being phenomenon (not a textual/structural pattern mislabeled as one), whether its Phase 1 justification actually warrants it, and whether its Phase 2 operation tracks faithfully back to it. CORRECT ANY FAILURE FOUND before the debate is considered filled, rather than only noting it for later. | WA-interpretation-questions-v1.4-2026-08-02.md Part C item 7 | schema: passage_validation_note (corrected flag) |
| 40 | open-decisions | Next steps / open decisions the passage's own analysis surfaces, recorded as a single evolving summary field, not a repeating structured list. | WA-interpretation-questions-v1.4-2026-08-02.md Part C item 8 | schema: passage.open_decisions_note |
| 25 | multi-chapter-vigilance | Where a debate document spans multiple chapters, Phase 3 validation should pay particular attention to phenomena/justifications that read as though they are describing the passage's own literary architecture rather than a specific inner being's own state -- this is the exact failure mode phase-separation (phenomenon.set) exists to prevent, and this validation pass is the last check that it did not recur. | WA-passage-read-guidance-v1.5 step 6 note b | **not enforced** |

| Check | Question | Kind | Required | Enforced by |
|---|---|---|---|---|
| linkage-genuinely-registered | Do both the from/to sides of this linkage reference already-registered phenomena/operations -- not licence to narrate a pattern across the whole passage as if it were a linkage? | reasonableness | 1 | **not enforced** |
| insufficiency-genuinely-absent | Is this data genuinely absent from the base extract/lexical, not substituted from remembered or external knowledge? | non_existence | 1 | **not enforced** |
| emergent-question-not-resolvable-now | Is this a genuine interpretive fork or literary/structural observation that could not be resolved within the phenomena/operations themselves -- not something that should have been settled there directly? | reasonableness | 1 | **not enforced** |
| validation-finding-corrected-not-just-logged | If this finding identifies a real failure in an existing phenomenon/operation, has it actually been corrected (corrected=true, and the correction submitted) rather than merely logged for later? | existence | 1 | **not enforced** |

## Appendix 3. Field meanings of the tables the stages write (`cfg_column`, iba.db)

### `cluster_strong` (written in stage 0.B)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate key | - | - |
| strong | TEXT | the full Strong's code this assignment is for | - | - |
| cluster_code | TEXT | the assigned cluster | - | - |
| source | TEXT | provenance: 'old-system-migration' / (future) an LLM-allocation pass identifier | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | soft delete | - | - |
| confidence | TEXT | 'high' / 'medium' / 'low' -- an allocation pass's own confidence in this assignment; NULL for old-system-migration rows (no equivalent signal). | - | - |
| operation | INTEGER | 1 if the code denotes a human operation/movement (a T3 'Operations' candidate), 0/NULL otherwise. | - | - |
| alt_clusters | TEXT | JSON list of alternate cluster_code candidates an allocation pass considered besides the one it picked. | - | - |
| review_flag | INTEGER | 1 if this specific assignment needs researcher review before being trusted as final. | - | - |
| rationale | TEXT | free-text reasoning for the assignment, as given by whatever process produced it. | - | - |

### `cluster_subgroup` (written in stage D2, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK, assigned by the recording pass (#1693) | - | - |
| cluster_code | TEXT | required, singular -- a family is structurally one-cluster-only by construction | - | - |
| subgroup_code | TEXT | the family's stable code, unique per (cluster_code, subgroup_code) -- expected to repeat as 'FLAG' across clusters, never otherwise | - | - |
| label | TEXT | short human title | - | - |
| core_description | TEXT | one sentence on the family's shared commonality | - | - |
| anchor_verse_reference | TEXT | ADDED 2026-09-16 (#1526). One representative verse per subgroup, selected by process (b)'s own LLM session as the verse that best describes the subgroup's shared characteristic (researcher, verbatim). Resolved fresh against iba.db.verse.osisId (CORRECTED 2026-09-22, escalation #1824 -- previously said verse.reference, the same wrong claim ib_node.verse_reference carried, inherited via this text's own 'same convention as' reference; confirmed live: 0 of 13 non-null values fail to join against verse.osisId), same convention as ib_node.verse_reference; written in the SAME DB update as the rest of the subgroup row (#1693's recording pass), never a separate pass or left null-then-backfilled. | - | - |
| sort_order | INTEGER | display order | - | - |
| status | TEXT | subgroup-level lifecycle, cfg_enum-governed (cluster_subgroup.status, #1690 SS3a). Distinct from cluster.status (#1697) -- coarser grain, separate enum. NULL for the FLAG subgroup (never enters this lifecycle). | - | - |
| version | TEXT | reused as-is from the legacy table convention | - | - |
| source | TEXT | descriptive provenance text, not an invented code | - | - |
| notes | TEXT | free text | - | - |
| delete_flagged | INTEGER | soft-delete | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| last_updated_date | TEXT | ISO-8601 UTC | - | - |

### `cluster_subgroup_strong` (written in stage D2, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK, assigned by the recording pass (#1693) | - | - |
| strong | TEXT | the Strong's code, resolved to strong.strongNumber (was mti_term_id/mti_terms.id pre-DB-fork). UNIQUE -- one strong, one family, structurally enforced | - | - |
| cluster_subgroup_id | INTEGER | which subgroup this strong belongs to | - | - |
| placement_note | TEXT | free text -- REQUIRED for FLAG placements (the signpost's rationale); optional but available for any ordinary placement, captures whatever observation the LLM made while assigning that strong | - | - |
| delete_flagged | INTEGER | soft-delete | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| last_updated_date | TEXT | ISO-8601 UTC | - | - |

### `debate_change_detail` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| run_id | TEXT | which run made this change -- same fk convention as escalation.run_id/validation_result.run_id | - | - |
| table_name | TEXT | 'hib' / 'hib_referent_option' / 'verse_hib' -- which table this row's change touched | - | - |
| op | TEXT | 'insert' / 'update' / 'delete' -- free text, matching cfg_change_detail.op's own precedent | - | - |
| where_json | TEXT | identifies the row touched, e.g. {"id": 47} | - | - |
| set_json | TEXT | the new values written (insert/update only) | - | - |
| before_json | TEXT | prior row state (update/delete only), NULL on insert | - | - |
| applied_at | TEXT | ISO-8601 UTC | - | - |
| writer | TEXT | which step made this change -- 'hib.set' / 'passage.build' / 'phenomenon.set' / 'operation.set' / 'closing.set' | - | migration/add_debate_change_detail_writer_column_20260808.py |

### `escalation_thread_item` (written in stage D4, RECORD, ITEMS)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| escalation_id | INTEGER | the thread | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| item_no | INTEGER | the item's place in its thread; the reference is {alias}.{item_no}, e.g. OT-16.1. Never renumbered; a new item takes the next number (proposal sec3.4) | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| kind | TEXT | cfg_enum escalation_thread_item_kind: cluster, strong, verse, strand, chapter, event, researcher, escalation | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| value | TEXT | e.g. M72, M10c, H5782, Rom 7:15-21, 10.13, #1993 (kind escalation: the task or issue that references the thread) | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| status | TEXT | cfg_enum escalation_thread_item_status: open, closed (answered), withdrawn (no longer relevant) or superseded (carried by another item or thread) -- current state only; every change is a response row | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| note | TEXT | what this item asks for, e.g. '7 verses' | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| opened_at | TEXT | when the item was added (ISO-8601 UTC) | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| opened_by | INTEGER | the escalation under which the item was added: a task or issue (e.g. a forward under #1998), or the superseded thread an item was carried over from; NULL when added with the thread itself | - | iba/app/migration/escalation_open_threads_v1_20261012.py; escalation.raise_new/update |
| origin_escalation_id | INTEGER | the task or issue of the analysis that raised the item | - | iba/app/lib/openitem.py (add, reword, split) |
| anchor | TEXT | where in that analysis: strong:, verse:, observation:, claim: or block:<chapter / heading> | - | iba/app/lib/openitem.py (add, reword, split) |
| source_terms | TEXT | the source analysis's strong(s), comma-separated, for a cluster item | - | iba/app/lib/openitem.py (add, reword, split) |
| target_cluster | TEXT | the cluster the further work reads (the item's home: it comes back when that cluster is worked) | - | iba/app/lib/openitem.py (add, reword, split) |
| target_terms | TEXT | the related term(s) in the target cluster, comma-separated | - | iba/app/lib/openitem.py (add, reword, split) |
| read_for | TEXT | what the further reading is to look for | - | iba/app/lib/openitem.py (add, reword, split) |
| why | TEXT | why it is an open item: what the origin found that leaves it open | - | iba/app/lib/openitem.py (add, reword, split) |
| comes_back_when | TEXT | the trigger that brings the item back | - | iba/app/lib/openitem.py (add, reword, split) |
| target_verses | INTEGER | how many verses the target holds (escalation_thread_item_verse); at most open_item.max_verses | - | iba/app/lib/openitem.py (add, reword, split) |
| worded_at | TEXT | when the item was worded to the #2236 rules (kind 'scope'); NULL: not yet worded | - | iba/app/lib/openitem.py (add, reword, split) |

### `escalation_thread_item_verse` (written in stage D4, RECORD, ITEMS)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/openitem.py (add, reword, split) |
| item_id | INTEGER | the open item | - | iba/app/lib/openitem.py (add, reword, split) |
| verse_id | INTEGER | a verse of its target | - | iba/app/lib/openitem.py (add, reword, split) |
| deleted | INTEGER | 1 once the item is reworded (the earlier target kept as history) | - | iba/app/lib/openitem.py (add, reword, split) |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/openitem.py (add, reword, split) |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' | - | iba/app/lib/openitem.py (add, reword, split) |

### `hib` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| book | TEXT | OSIS book code, same convention as verse.osisId's book segment | - | - |
| label | TEXT | e.g. 'Daniel', 'the four youths', 'King Belshazzar' | - | - |
| kind | TEXT | named_individual / unnamed_individual / named_collection / unnamed_collection / implicit_individual / implicit_collection -- six types, two orthogonal axes: plurality (individual/collection) x specificity (named/unnamed/implicit). Researcher training pass nahum-1-inner-being-training-20260803.md; debate digest Step 1 (presumptive-candidate / collective / referential rules). | enum.hib_kind | - |
| first_verse_id | INTEGER | anchor -- where this HIB was first identified | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete, standard convention | - | - |

### `hib_referent_option` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| hib_id | INTEGER | the HIB this referent-crux reading belongs to | - | - |
| reading_text | TEXT | one grammatically-live candidate reading (T4) -- e.g. one option for 'we' in Obad 1 | - | - |
| textual_grounds | TEXT | why this reading is live | - | - |
| adopted | INTEGER | exactly one row per hib_id should be 1 -- the explicit choice (T4: 'adopt one explicitly') | - | - |
| ordinal | INTEGER | **no use recorded** | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `ib_node` (written in stage D1, D2, D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK, assigned by the recording pass | - | - |
| observation_id | INTEGER | which observation this grounding element belongs to | - | - |
| cluster_code | TEXT | a VALUE, not necessarily a copy of the parent observation's own cluster -- THE cluster this row references. One row per cluster when an observation touches multiple clusters. | - | - |
| cluster_subgroup_code | TEXT | was family_key -- THE subgroup this row references (usually the observation's own, but can differ) | - | - |
| strong | TEXT | denormalized copy | - | - |
| verse_reference | TEXT | resolved FRESH against iba.db.verse.osisId at load time (recordingpass.py:resolve_occurrence returns v.osisId, never v.reference), never trusted from the LLM's JSON directly (#1693's own fix). CORRECTED 2026-09-22 (escalation #1824) -- this text previously said 'verse.reference', which was factually wrong (verse.reference is a different, space-separated STEP-abbreviated format, e.g. 'Mar 6:25', vs. osisId's dotted 'Mark.6.25'; confirmed live: 0 of 10,115 non-null ib_node.verse_reference values fail to join against verse.osisId) and is the likely cause of a real hand-written query bug this same session that joined against verse.reference expecting the dotted format. | - | - |
| surface | TEXT | was span_surface -- matches span.surface | - | - |
| morph_code | TEXT | was span_morph -- matches span.morph_code | - | - |
| question_code | TEXT | catalogue-question grounding -- not yet an enforced FK, restore once #1696 lands the catalogue into iba.db | - | - |
| traced_observation_id | INTEGER | set when grounded in ANOTHER observation instead of a verse | - | - |
| source_stage | TEXT | reading / answer / synthesis | - | - |
| seq | INTEGER | a plain per-observation ordinal -- ties together every ib_node row sharing one observation_id, in reading order when meaningful. UNIQUE(observation_id, seq) is the real natural key. | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |

### `ib_observation` (written in stage D1, D2, D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| meaning_keywords | TEXT | JSON array of short key terms/concepts the LLM extracts alongside obs_text, used by recordingpass.py's structured-key same/broaden/new matching (surface+morph+keywords) -- escalation #1824, 2026-09-21. NULL for stages/questions not yet using this path (everything except the new M0.7 family so far); the existing text-similarity path remains the fallback wherever this is NULL. | - | - |
| id | INTEGER | surrogate PK, assigned by the recording pass, never the LLM session | - | - |
| cluster_code | TEXT | NULL for stage=synthesis (cross-cluster; the actual cluster(s) are recorded via ib_node rows instead) AND for word-level (M0.1.x/M0.5.x) questions in stage=verse-reading (2026-09-23: cluster has no role in these -- the observation is a fact about the strong+span alone, keyed on strong and verse, never a cluster). Required for every other stage/question type. | - | - |
| cluster_subgroup_id | INTEGER | NULL for stage=synthesis and process (b)'s own cluster-level observations (both above single-subgroup scope) | - | - |
| stage | TEXT | cfg_enum-governed (ib_observation.stage): verse-reading (pre-subgroup Layer 2, #1711) / char-subgroup (subgroup/family formation, process b) / char-reading (process c) / char-answers (process d) / char-synergy (process e, cross-cluster). Renamed 2026-09-17, escalation #1706, completing the naming scheme -- every value now names an activity at a grain (verse vs. characteristic), subgroup formation included. | - | - |
| tag | TEXT | enum, cfg_enum-governed (ib_observation.tag) -- shared across all stages, not partitioned per stage; most tags apply wherever the relevant condition arises (e.g. data-error, cross-cluster-significance, could-not-resolve are not reading-exclusive). Corrected 2026-09-17, escalation #1706: previously read 'stage-specific enum', which the researcher identified as the wrong model -- ib_observation is one unified record set populated across stages, not fragmented enum groups per stage. | - | - |
| strong | TEXT | the strong this claim is grounded in | - | - |
| question_code | TEXT | answer/verse_meaning stages -- not yet an enforced FK; restore once the catalogue migration (#1696) lands wa_obs_question_catalogue into iba.db | - | - |
| window | TEXT | The analytical angle this row looks through -- meaning / action-impact / relational (cfg_enum ib_observation.window). Populated FROM wa_obs_question_catalogue.window at write time (recordingpass.py), never invented ad hoc. Redefined #1723, 2026-09-17 -- was a 4-value pipeline-stage enum (#1691) that duplicated `stage`. | - | - |
| obs_text | TEXT | self-standing claim text, no join required | - | - |
| meaning_source | TEXT | which of the 3 meaning tables/columns (strong_meaning_tree, strong_lexicon.lsj, strong_lexicon.mounce) an observation drew its data from -- any meaning-reading stage (verse_meaning and reading both read all 3 as complementary evidence), not reading-only. Corrected 2026-09-17, escalation #1706: previously read 'reading stage only', the same stage-scoping mistake corrected for `tag`. | - | - |
| status | TEXT | Where the observation stands (6-value lifecycle, researcher-defined 2026-09-20, escalation #1782): draft (just written or edited by the pipeline, not yet looked at by the observation_enhancer or a human -- the write-time default as of this round) / needs-corroboration (observation detail is incomplete or needs revision) / open (not yet confirmed -- NOTE: no current writer sets this since draft was introduced; kept live pending the researchers call on whether to retire it) / silent (captured but not included in any subsequent analysis) / withdrawn (observation is incorrect or not useful) / resolved (set only once the observation is cleared for inclusion in analysis). | - | - |
| supersedes_observation_id | INTEGER | synthesis stage only, self-referencing, the append-only supersedes chain | - | - |
| stable_key | TEXT | the generating JSON file's own name; for a strand-reading observation imported from a ledger (#2172 catch-up), '<strand>:<ledger ID>' | - | - |
| revisit_note | TEXT | synthesis stage; for a strand-reading observation, its disposition note (#2172): the October disposition and the row's touches until step C sets the status, then the claim, item or reason | - | - |
| source_json_serial | INTEGER | the LLM session's own local numbering within its JSON, distinct from id | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| updated_at | TEXT | set whenever obs_text is broadened in place | - | - |
| setting | TEXT | the key statement's setting: who speaks, the verses around it, the genre (October ledger part) | - | iba/app/lib/recordingpass.py (record_strand_observations) |
| meaning | TEXT | what the statement means in its setting (October ledger part) | - | iba/app/lib/recordingpass.py (record_strand_observations) |
| implication | TEXT | what it implies for the inner being (October ledger part) | - | iba/app/lib/recordingpass.py (record_strand_observations) |
| chain | TEXT | the link the verse itself states to another act or state; NULL where the verse states none | - | iba/app/lib/recordingpass.py (record_strand_observations) |
| basis | TEXT | cfg_enum ib_observation.basis: stated (the verse states it) or read (Claude's reading, 'I read') | enum.ib_observation.basis | iba/app/lib/recordingpass.py (record_strand_observations) |
| parties | TEXT | who acts, toward whom, and who else is named | - | iba/app/lib/recordingpass.py (record_strand_observations) |
| run_id | TEXT | the Strand-Reading run that wrote or last changed the row | - | iba/app/lib/recordingpass.py (record_strand_observations) |

### `ib_observation_enhancer_log` (written in stage RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| rule_id | INTEGER | which rule made this change | - | - |
| rule_key | TEXT | denormalised copy of the rule's own key at apply time -- readable even if the rule row is later retired/edited | - | - |
| observation_id | INTEGER | which observation was changed | - | - |
| field_changed | TEXT | the ib_observation column that was updated | - | - |
| before_value | TEXT | the field's value immediately before this change (stringified) | - | - |
| after_value | TEXT | the value written (stringified) | - | - |
| applied_at | TEXT | ISO-8601 UTC | - | - |
| run_id | TEXT | the run.run_id of the -Action Apply call that made this change | - | - |

### `narrative_chapter` (written in stage D4, PUBLISH, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_no | TEXT | 02, 10.7, 13.1 | unique among active rows (trigger trg_narrative_chapter_no_bi/_bu) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| title | TEXT | the chapter heading, e.g. Choosing and setting direction | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| reading_order | INTEGER | order in the book | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| file_stem | TEXT | e.g. 10-07-choosing-and-setting-direction | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| current_version | INTEGER | the current chapter file's version, e.g. 27 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| current_file | TEXT | the current chapter file name | matches a file on disk (Check) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| state | TEXT | cfg_enum narrative_chapter_state | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| replaces_original | TEXT | the index column 'Replaces or absorbs (original)' | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| built_from | TEXT | the index column 'Built from' | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| inactive | INTEGER | 1 for a retired chapter number (old Ch 13 Under God's anger) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL; 'direct edit' means the row was inserted outside the tool, which Check reports (#2155) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| kind | TEXT | cfg_enum narrative_chapter_kind: what sort of chapter this is (front matter, activity, key characteristic, ...) | set on every active chapter (Check) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_chapter_table_config_v1_20261018.py |
| purpose | TEXT | what the chapter holds, what belongs in it and what goes elsewhere, in plain words | set on every active chapter (Check); changed only through EditChapter, logged in the Structure log | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_chapter_table_config_v1_20261018.py |
| purpose_ref | TEXT | the rulings that set the purpose: escalation numbers and dates | may say 'No recorded ruling' where the purpose is read from the chapter itself | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_chapter_table_config_v1_20261018.py |

### `narrative_citation` (written in stage D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_id | INTEGER | where it is cited | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| section_id | INTEGER | where it is cited | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| passage_id | INTEGER | NULL if the passage tells no claim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| verse_id | INTEGER | NULL where the verse has no row | a non-NULL value must name a verse row (trigger trg_narrative_citation_verse_bi/_bu) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ref_as_written | TEXT | as written in the chapter | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ref_normalised | TEXT | in verse.reference form | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| quoted | INTEGER | 1 when the verse's words are quoted, 0 when it is only referred to | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| first_version | INTEGER | the first chapter version that cites it | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| last_version | INTEGER | the last chapter version that cites it; NULL while current | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_claim` (written in stage D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_ref | TEXT | original claims keep the register's id (I-1, 2-5, K-2); new claims are C-{id}, set by trigger trg_narrative_claim_ref_ai when left empty | unique | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| origin | TEXT | cfg_enum narrative_claim_origin | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_text | TEXT | the claim in its own plain wording, apart from how the narrative tells it | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| beyond_text | TEXT | what the claim adds to its sources: why it is a claim and not a quotation | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| i_read | INTEGER | 1 when the narrative marks it as the narrator's reading ('I read') | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| verdict | TEXT | cfg_enum narrative_claim_verdict, the register's own words | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| part_verdict | TEXT | the second verdict of a split verdict, e.g. Held in 9-1 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| part_scope | TEXT | what each part of a split verdict covers | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| original_chapter | TEXT | for original claims: the essay chapter heading | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| original_wording | TEXT | for original claims: the claim as the essay made it | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| main_chapter_id | INTEGER | the chapter that tells the claim most fully | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| main_section_id | INTEGER | the section that tells it most fully | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| in_narrative | INTEGER | 1 if at least one current passage tells the claim (a pointer does not count); 0 if none. The filter for claims not included | kept by the telling and passage triggers | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| status | TEXT | cfg_enum narrative_claim_status | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_claim_change` (written in stage D4, PUBLISH, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_id | INTEGER | the claim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| passage_id | INTEGER | the passage, for a change in how the claim is told | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| update_id | INTEGER | the update that made it; NULL for a direct edit | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| change_date | TEXT | ISO date | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| change_kind | TEXT | cfg_enum narrative_claim_change_kind | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_before | TEXT | the claim's wording before | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_after | TEXT | the claim's wording after | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| verdict_before | TEXT | the verdict before | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| verdict_after | TEXT | the verdict after | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| passage_before | TEXT | the full passage before, as it read in the chapter | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| passage_after | TEXT | the full passage after | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_id | INTEGER | where | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| section_id | INTEGER | where | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| section_before_id | INTEGER | where from, for a move | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_version_from | INTEGER | e.g. 7 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_version_to | INTEGER | e.g. 8 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| file_before | TEXT | the chapter file before | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| file_after | TEXT | the chapter file after | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| note | TEXT | the verdict cell verbatim, or any remark | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| basis | TEXT | cfg_enum narrative_change_basis: recorded, reconstructed, direct edit | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| provenance | TEXT | the file(s) the row came from, or the trigger that wrote it | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_claim_source` (written in stage D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_id | INTEGER | the claim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| source_kind | TEXT | cfg_enum narrative_claim_source_kind | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| verse_id | INTEGER | for kind verse; NULL where the verse has no row | a non-NULL value must name a verse row (trigger trg_narrative_claim_source_verse_bi/_bu) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ref_as_written | TEXT | the reference as written, e.g. 1 Samuel 24:5 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ref_normalised | TEXT | in verse.reference form, e.g. 1Sa 24:5 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| source_text | TEXT | for the other kinds: the word with its gloss, the science reference, or the file path | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| note | TEXT | how the source bears on the claim, where it is not plain | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| observation_id | INTEGER | the observation the claim rests on, when source_kind is 'observation' (#2172 design decision 4) | - | iba/app/lib/narrativeregister.py; iba/app/lib/strandreading.py |

### `narrative_claim_telling` (written in stage D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claim_id | INTEGER | the claim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| section_id | INTEGER | the block (narrative_section) that tells the claim; one current telling per claim and block (#2172) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py; iba/app/migration/archive/strand_reading_schema_2172_v1_20261022.py |
| passage_id | INTEGER | the passage that told the claim before #2172 (history, status superseded); NULL on a block telling | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py; iba/app/migration/archive/strand_reading_schema_2172_v1_20261022.py |
| kind | TEXT | cfg_enum narrative_telling_kind: in full, in part, pointer | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| part_told | TEXT | which part of the claim this passage tells | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| status | TEXT | cfg_enum narrative_telling_status: current, removed, superseded (a passage telling carried by its block's telling, #2172) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_index_note` (written in stage D4)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| heading | TEXT | the block heading | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| text | TEXT | the block text (markdown) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ordinal | INTEGER | order in the published register | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_passage` (written in stage D4)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_id | INTEGER | the chapter | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| section_id | INTEGER | the section | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ordinal | INTEGER | its place in the section | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| anchor_text | TEXT | its opening words, so the tool can find it in the file | found in the current chapter file (Check) | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| passage_text | TEXT | the passage as it now reads | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| first_version | INTEGER | the first chapter version that holds it | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| last_version | INTEGER | the last chapter version that holds it; NULL while current | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_section` (written in stage D4, PUBLISH, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| chapter_id | INTEGER | the chapter | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| heading | TEXT | the heading text as written; '(opening)' for the opening | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| level | INTEGER | heading level 2-4; 0 for the opening | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| parent_section_id | INTEGER | the section it sits in | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| ordinal | INTEGER | order in the chapter | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| first_version | INTEGER | the first chapter version that has the heading | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| last_version | INTEGER | the last chapter version that has it; NULL while current | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| renamed_from_id | INTEGER | when a heading is renamed, the old row | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| block_text | TEXT | the section's block of the chapter, verbatim: its heading line and every line up to the next heading (the opening row: the title line and the opening). The chapters render from these blocks in ordinal order (narrativeregister.render_chapter); NULL on a row that is no longer current | - | iba/app/lib/narrativeregister.py (_sync_bodies, from Record and AddChapter); iba/app/migration/archive/narrative_blocks_2172_v1_20261022.py |

### `narrative_update` (written in stage D4, PUBLISH, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| update_date | TEXT | ISO date of the update | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| title | TEXT | the update's heading | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| strand | TEXT | e.g. anger (M02) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| researcher_instruction | TEXT | verbatim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| method | TEXT | method or rule named (e.g. rule 73) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| source_files | TEXT | one path per line | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| scripts | TEXT | one path per line | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| claims_changed_note | TEXT | 'Original claims changed', verbatim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| not_woven_note | TEXT | 'Not woven' / 'Kept out', verbatim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| structure_change | TEXT | filled when the book's shape changed (the Structure log) | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| structure_reason | TEXT | the reason for the structure change | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| quote_parts | INTEGER | the quote check: parts checked | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| quote_failures | INTEGER | the quote check: failures | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| quote_note | TEXT | the quote check note, verbatim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| notes | TEXT | any other paragraph, verbatim | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| legacy_register_version | INTEGER | for imported updates, the register version that added it | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `narrative_update_ref` (written in stage D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | assigned by SQLite | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| update_id | INTEGER | the update | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| kind | TEXT | cfg_enum narrative_update_ref_kind | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| value | TEXT | 1998, OT-29, OT-29.1 | - | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | historical date for imported rows; now for new rows | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, trigger, or 'direct edit' (the default, for a row inserted outside the tool) | never NULL | iba/app/lib/narrativeregister.py; iba/app/migration/narrative_claim_register_config_v1_20261013.py |

### `operation` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| phenomenon_id | INTEGER | NOT NULL by design -- the DB-level enforcement of WA-interpretation-questions Part B.12: an operation may only originate from an already-registered phenomenon | - | - |
| process | TEXT | state/status, or a movement (come from/go to/impact on/emerge/go away/become evident) -- v1.4 Q6 | - | - |
| action_type | TEXT | short verb-based label (Q11) -- a label, not a controlled vocabulary (Part B.10) | - | - |
| decision | TEXT | 'retain' / 'set_aside' / 'retain_referential' / 'recorded_silence' | enum.operation_decision | - |
| observation_text | TEXT | what the text/span-data states, Strong's codes cited | - | - |
| description_text | TEXT | debate digest Step 5's descriptive write-up | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `operation_party` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| operation_id | INTEGER | **no use recorded** | - | - |
| role | TEXT | 'source' / 'target' | - | - |
| kind | TEXT | 'self' / 'human' / 'non_human' / 'object_situation' / 'none' | - | - |
| detail | TEXT | which human/object, if named | - | - |
| enablement_only | INTEGER | role='source' rows only -- Part B.5's source-of-state vs source-of-enablement distinction, kept structurally separate rather than folded into kind | - | - |
| ordinal | INTEGER | a phenomenon's operation can have multiple sources/targets (v1.5 step1 note a) | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| hib_id | INTEGER | which registered HIB this source/target party IS, when it is one -- nullable: self/non_human/object_situation/none parties genuinely have no HIB to link. Added 2026-08-07 (Finding 2, debate-schema-traceability-gap-findings-20260807.md): 'detail' alone gave no structural traceability back to the hib register. | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `passage` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| feasibility_note | TEXT | Step 2's own self-assessment record: why this scope was judged readable as a whole without quality loss (or, if the call was refused, why not -- though a refused call writes no passage row at all, so a live row's feasibility_note is always the 'yes, and here's why' case). | - | passage.build |
| open_decisions_note | TEXT | Part C section 8 -- short free-text summary of open decisions/next steps for this passage. Stays a single field, not its own table (design doc: normally short prose, not a repeating structured list, unlike sections 4-7). | - | - |
| phenomena_complete_at | TEXT | NULL until the debate digest Step 3 phase gate is confirmed complete for the whole passage (every verse_hib pair for this passage has a matching phenomenon row); set only by an explicit control check, never by trust. operation writes are blocked in code while this is NULL (schema built, gate-enforcing writer not yet built -- see b3-b5-operations-schema-design-20260805.md). | - | - |
| story_summary | TEXT | Step 2's high-level story synthesis for this passage's scope, read in light of the identified HIBs -- the researcher's own 2026-08-06 redefinition of what Step 2 actually produces. Written once per passage registration, updated only via reconciliation. | - | passage.build |
| id | INTEGER | surrogate key | - | - |
| book | TEXT | OSIS book code | - | - |
| anchor_verse_id | INTEGER | first verse of the run — the anchor | - | - |
| start_chapter | INTEGER | range start chapter - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| start_verse | INTEGER | range start verse - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| end_chapter | INTEGER | range end chapter - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| end_verse | INTEGER | range end verse - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| ref | TEXT | human range - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| verse_count | INTEGER | count of verses in the range - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| rule | TEXT | char-continuity / maximal - DORMANT since passage.build retired 2026-07-26; NULL on every live row; no active mechanism populates this column | hardcoded literal "input-scope" (set by passage.py:build itself, never analyst-supplied) for a live row; NULL/legacy value for a pre-2026-08-06 row never rebuilt under the new model. No longer enum-validated -- the passage_rule enum was retired 2026-08-06 (BUILD.md sec68) since nothing ever validates an incoming choice against it any more. | - |
| source | TEXT | passage-build / single-verse-emergent - DORMANT since passage.build retired 2026-07-26; NULL on every live row; no active mechanism populates this column | enum.passage_source | - |
| needs_review | INTEGER | 1 when verse_count > passage.review_over (passage.build only) - DORMANT since passage.build retired 2026-07-26; NULL on every live row; passage.validate reports the live distribution directly instead | - | - |
| created_at | TEXT | when this passage row was created - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| deleted | INTEGER | soft delete | - | - |
| book_label | TEXT | human-facing subfolder name (e.g. 'Daniel') used by the verse-analysis report writers; defaults to `book` if the caller never supplied one | - | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| verse_span_meaning_path | TEXT | path to this range's report.verse_span_meaning output, written by that step on success | - | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| verse_span_meaning_written_at | TEXT | UTC timestamp of the last report.verse_span_meaning write for this range | - | DORMANT -- report.verse_span_meaning retired (superseded by report.verse_lexical / lexical.build, BUILD.md §56-59); not carried into the input-scope passage model (BUILD.md §67) -- no live writer as of 2026-08-06 (confirmed against handlers/passage.py:build directly, researcher-approved dormant per CONFIG-REPORT-v34) |
| debate_path | TEXT | path to this range's report.passage_debate output (scaffold or filled — see debate_status), written by that step on success | - | report.passage_debate (legacy, passage.rule IS NULL) or report.debate (new-model, passage.rule='input-scope' -- tools/build_debate_report.py) |
| debate_written_at | TEXT | UTC timestamp of the last report.passage_debate write for this range | - | report.passage_debate (legacy, passage.rule IS NULL) or report.debate (new-model, passage.rule='input-scope' -- tools/build_debate_report.py) |
| debate_status | TEXT | 'scaffold' (auto-generated, still has unreplaced <!-- fill in --> placeholders) or 'filled' (none remain) — a coarse, mechanically-derived completion signal only; NOT a digestion of the debate's analytical content, which is a separate, not-yet-designed question | enum.passage_debate_status | report.passage_debate (legacy, passage.rule IS NULL: scaffold/filled) or report.debate (new-model, passage.rule='input-scope': empty/in-progress/complete) -- tools/build_debate_report.py |

### `passage_emergent_question` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| passage_id | INTEGER | **no use recorded** | - | - |
| verse_id | INTEGER | nullable -- an emergent question can span the whole passage | - | - |
| question_text | TEXT | Part C section 6 / Q10 -- interpretive forks (Part B.9) and genuine literary/structural observations (Part B.12, T5) both land here, never in the phenomena register or an operation | - | - |
| kind | TEXT | 'interpretive_fork' / 'literary_structural' / 'other' | - | - |
| ordinal | INTEGER | natural key within passage_id for the reconciliation writer | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `passage_insufficiency` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| passage_id | INTEGER | **no use recorded** | - | - |
| verse_id | INTEGER | nullable -- an insufficiency can be passage-wide, not always tied to one verse | - | - |
| note | TEXT | Part C section 5 / Q9 / Part B.7 -- data the base extract does not carry, named not filled from outside knowledge | - | - |
| ordinal | INTEGER | natural key within passage_id for the reconciliation writer | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `passage_linkage` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| passage_id | INTEGER | **no use recorded** | - | - |
| from_operation_id | INTEGER | Part C section 4 / Q7 -- a linkage connects two SPECIFIC, already-registered operations in the same passage, never a pattern across a range | - | - |
| to_operation_id | INTEGER | **no use recorded** | - | - |
| note | TEXT | what the linkage is -- also where a Q7 SURFACED ABSENCE gets recorded (row with from=to=the same operation, note explains the absence) rather than passed over silently | - | - |
| ordinal | INTEGER | natural key within passage_id for the reconciliation writer | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `passage_validation_note` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| passage_id | INTEGER | **no use recorded** | - | - |
| phenomenon_id | INTEGER | nullable -- a validation finding can be about the passage's debate generally, not always one phenomenon | - | - |
| finding_text | TEXT | Part C section 7 / Phase 3 step 6 -- is this genuinely an inner-being phenomenon, does its Phase 1 justification warrant it, does its Phase 2 operation track faithfully back to it | - | - |
| corrected | INTEGER | WA-passage-read-guidance v1.5 step 6: a failure found here is corrected before the debate is considered filled, not merely logged for later -- this flag records that the correction actually happened, not just that a finding was noted | - | - |
| ordinal | INTEGER | natural key within passage_id for the reconciliation writer | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `phenomenon` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| passage_id | INTEGER | **no use recorded** | - | - |
| verse_id | INTEGER | **no use recorded** | - | - |
| hib_id | INTEGER | **no use recorded** | - | - |
| description | TEXT | the phenomenon: a state, disposition, or characteristic of this HIB's inner life (debate digest Step 3) | - | - |
| textual_warrant | TEXT | the verb/clause/stated-silence that grounds it (WA-passage-read-guidance step 3b) | - | - |
| status | TEXT | 'stated' / 'inferred' / 'silent' -- 'no phenomenon found, silent' is itself a valid row (WA-interpretation-questions Part B.4), never an omitted one | - | - |
| ordinal | INTEGER | allows more than one phenomenon for the same HIB in the same verse (v1.5 step3 note c) | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `reading` (written in stage 0.C, 0.GAP, D4, PUBLISH, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/reading.py |
| label | TEXT | the reading's short name, lowercase-hyphenated (e.g. anger-bosom); unique | - | iba/app/lib/reading.py |
| escalation_id | INTEGER | the task or issue that anchors the reading; it cannot close while the reading is not published or withdrawn (check kind readings_published) | - | iba/app/lib/reading.py |
| home_cluster | TEXT | the cluster its new observations are grounded under (ib_node) | - | iba/app/lib/reading.py |
| request | TEXT | the scope request as resolved at opening (JSON, versescope) | - | iba/app/lib/reading.py |
| state | TEXT | cfg_enum reading_state | enum.reading_state | iba/app/lib/reading.py |
| gap_file | TEXT | the gap JSON written at Open (gate 1's record) | - | iba/app/lib/reading.py |
| synergy_file | TEXT | the synergy JSON written at Synergy (gate 2's record) | - | iba/app/lib/reading.py |
| synergy_built_at | TEXT | when the synergy JSON was built from the tables; Apply refuses a file that does not carry it | - | iba/app/lib/reading.py |
| recorded_at | TEXT | when gate 1 passed | - | iba/app/lib/reading.py |
| synergised_at | TEXT | when gate 2 passed | - | iba/app/lib/reading.py |
| published_at | TEXT | when gate 3 passed | - | iba/app/lib/reading.py |
| chapters | TEXT | the chapters the reading touched (JSON list of chapter numbers), filled at Apply | - | iba/app/lib/reading.py |
| note | TEXT | free note | - | iba/app/lib/reading.py |
| run_id | TEXT | the Reading run that last changed the row | - | iba/app/lib/reading.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/reading.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | - | iba/app/lib/reading.py |

### `reading_file` (written in stage 0.GAP)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/readingindex.py (build) |
| path | TEXT | the file, repo-relative posix path | - | iba/app/lib/readingindex.py (build) |
| cluster | TEXT | the cluster folder it sits in (M02 for 'M02 - anger-wrath'); NULL at a root | - | iba/app/lib/readingindex.py (build) |
| size_bytes | INTEGER | size when indexed | - | iba/app/lib/readingindex.py (build) |
| sha256 | TEXT | content hash when indexed; a different hash means the file is read again | - | iba/app/lib/readingindex.py (build) |
| indexed_at | TEXT | when the file was last indexed or marked removed (ISO-8601 UTC) | - | iba/app/lib/readingindex.py (build) |
| sections | INTEGER | heading sections found (the opening counts as one) | - | iba/app/lib/readingindex.py (build) |
| refs | INTEGER | verse references found, one per verse after range expansion | - | iba/app/lib/readingindex.py (build) |
| imported_observations | INTEGER | ib_observation rows whose revisit_note names this file: its rows are also in the tables (#2228 D2) | - | iba/app/lib/readingindex.py (build) |
| removed | INTEGER | 1 when the file is gone or archived; its rows are then marked deleted | - | iba/app/lib/readingindex.py (build) |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/readingindex.py (build) |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | - | iba/app/lib/readingindex.py (build) |

### `reading_ref` (written in stage 0.GAP)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/readingindex.py (build) |
| file_id | INTEGER | the file | - | iba/app/lib/readingindex.py (build) |
| section_id | INTEGER | the heading section | - | iba/app/lib/readingindex.py (build) |
| verse_id | INTEGER | the verse; NULL for a whole chapter or a reference that resolves to nothing | - | iba/app/lib/readingindex.py (build) |
| book | TEXT | the verse.reference book code (Psa) | - | iba/app/lib/readingindex.py (build) |
| chapter | INTEGER | the chapter, for a whole-chapter reference | - | iba/app/lib/readingindex.py (build) |
| ref_as_written | TEXT | the reference as the file writes it | - | iba/app/lib/readingindex.py (build) |
| ref_normalised | TEXT | verse.reference form (Psa 10:2, or Psa 51 for a chapter) | - | iba/app/lib/readingindex.py (build) |
| kind | TEXT | cfg_enum reading_ref.kind: verse or whole chapter | enum.reading_ref.kind | iba/app/lib/readingindex.py (build) |
| found_by | TEXT | cfg_enum reading_ref.found_by: explicit (a book named), follow-on c:v, follow-on v. | enum.reading_ref.found_by | iba/app/lib/readingindex.py (build) |
| line_no | INTEGER | the line it stands on (1-based) | - | iba/app/lib/readingindex.py (build) |
| line_kind | TEXT | cfg_enum reading_ref.line_kind: heading, table row, bullet, paragraph | enum.reading_ref.line_kind | iba/app/lib/readingindex.py (build) |
| reason | TEXT | why it resolves to nothing; NULL when it resolves | - | iba/app/lib/readingindex.py (build) |
| deleted | INTEGER | 1 once the file is re-read or removed | - | iba/app/lib/readingindex.py (build) |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/readingindex.py (build) |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | - | iba/app/lib/readingindex.py (build) |

### `reading_section` (written in stage 0.GAP)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/readingindex.py (build) |
| file_id | INTEGER | the file | - | iba/app/lib/readingindex.py (build) |
| ordinal | INTEGER | order in the file, 0 for the opening | - | iba/app/lib/readingindex.py (build) |
| level | INTEGER | heading level 1-4, 0 for the opening | - | iba/app/lib/readingindex.py (build) |
| heading | TEXT | the heading text | - | iba/app/lib/readingindex.py (build) |
| path | TEXT | the parent headings, joined with ' > ' | - | iba/app/lib/readingindex.py (build) |
| line_start | INTEGER | first line (1-based) | - | iba/app/lib/readingindex.py (build) |
| line_end | INTEGER | last line | - | iba/app/lib/readingindex.py (build) |
| deleted | INTEGER | 1 once the file is re-read or removed (an earlier reading kept as history) | - | iba/app/lib/readingindex.py (build) |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/readingindex.py (build) |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | - | iba/app/lib/readingindex.py (build) |

### `reading_strand_hit` (written in stage D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/strandreading.py |
| strand_id | INTEGER | the strand | - | iba/app/lib/strandreading.py |
| verse_id | INTEGER | the verse | - | iba/app/lib/strandreading.py |
| strong | TEXT | the strong as in verse_lexical | - | iba/app/lib/strandreading.py |
| surface | TEXT | the English surface of the hit (verse_lexical) | - | iba/app/lib/strandreading.py |
| face | TEXT | the face the reading gives the hit: its label and words (e.g. 'A. With his people as a whole'); NULL until read | - | iba/app/lib/strandreading.py |
| parties | TEXT | who acts in the hit, toward whom | - | iba/app/lib/strandreading.py |
| reason | TEXT | why the hit has no face (e.g. another sense of the word); a read hit has a face or a reason | - | iba/app/lib/strandreading.py |
| observation_id | INTEGER | the observation the hit went into, if any | - | iba/app/lib/strandreading.py |
| run_id | TEXT | the Strand-Reading run that read the hit | - | iba/app/lib/strandreading.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/strandreading.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | - | iba/app/lib/strandreading.py |

### `reading_verse` (written in stage 0.C, 0.GAP)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | iba/app/lib/reading.py |
| reading_id | INTEGER | the reading | - | iba/app/lib/reading.py |
| verse_id | INTEGER | the verse | - | iba/app/lib/reading.py |
| routes | TEXT | how the scope reached the verse (JSON, versescope routes) | - | iba/app/lib/reading.py |
| created_at | TEXT | when the row was written (ISO-8601 UTC) | - | iba/app/lib/reading.py |
| created_by | TEXT | who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool) | - | iba/app/lib/reading.py |

### `run_batch` (written in stage D1, D2, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| run_id | TEXT | the run.run_id that attempted this batch (informational/audit -- NOT part of the resume/skip key, deliberately, so a later run_id can still see an earlier run_id's committed work) | - | - |
| work_package | TEXT | e.g. verse-lexical, cluster-reading | - | - |
| step | TEXT | e.g. lexical.meaning, cluster.subgroup -- part of the resume/skip key | - | - |
| selector_key | TEXT | what this run was scoped to -- cluster_code alone, or cluster_code/subgroup_code for a subgroup-scoped step. Part of the resume/skip key. | - | - |
| batch_ordinal | INTEGER | this batch's 1-based position within its own run -- display/ordering only, NOT part of the resume/skip key (batch_content_key is, since ordinal position can drift between runs if the selector's own item list changes) | - | - |
| batch_content_key | TEXT | stable hash (batchcontrol.content_key) of the batch's own actual item list (verse ids, or member strongs) -- content-keyed, not position-keyed, so resume is correct even if the underlying item list shifts between runs. Indexed together with step/selector_key for lookup performance, but NOT unique -- the resume/skip guarantee lives in batchcontrol.already_committed()'s own WHERE status='committed' check, consulted before start_batch() runs, not in a schema constraint (a UNIQUE constraint here was tried first and found live, #1758, to incorrectly block a legitimate retry after a failed attempt at the same content). | - | - |
| status | TEXT | cfg_enum-governed (run_batch.status): running (written before the API call) / committed (written after record_batch's own commit succeeds) / failed (written in an exception handler before re-raising -- the crash safeguard). A 'running' row with no later committed/failed row for the same id is live proof of a dead run. | - | - |
| started_at | TEXT | ISO-8601 UTC, set when status='running' is written | - | - |
| ended_at | TEXT | ISO-8601 UTC, set when status becomes committed/failed | - | - |
| error_message | TEXT | set only when status='failed' | - | - |
| cost_usd | REAL | set only when status='committed', the real spent cost | - | - |

### `strong` (written in stage 0.B)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| strongNumber | TEXT | the resolved Strong's code — the key | - | - |
| accentedUnicode | TEXT | the actual Hebrew/Greek word | - | - |
| stepGloss | TEXT | short English sense | - | - |
| stepTransliteration | TEXT | romanised form; never shown without the gloss | - | - |
| language | TEXT | Hebrew/Greek from the code prefix | - | - |
| count | INTEGER | STEP token frequency — NOT a verse count, may be capped | - | - |
| freqList | TEXT | raw frequency distribution | - | - |
| created_at | TEXT | when first fetched | - | raw.detail |
| deleted | INTEGER | soft delete | - | - |
| origin | TEXT | 'word' = deliberately onboarded for a registry word (raw.discover -> word_strong -> raw.detail); must carry the full raw-data-integrity chain. 'backfill' = onboarded by raw.backfill_meaning's book-scoped completeness sweep, independent of any word; not in scope for cluster/meaning-relevance mapping, used only to support lexical resolution. Sticky: an upgrade backfill->word can happen (a later word legitimately claims the code); never downgraded. | - | raw.detail_one |

### `strong_related` (written in stage 0.B)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate key | - | - |
| strong | TEXT | the full code of the SOURCE term STEP was asked about | - | lexicon.related |
| related_strong | TEXT | the full code of the RELATED term — may have no strong row of its own yet | - | lexicon.related |
| related_form | TEXT | the related term's native-script form | - | lexicon.related |
| related_transliteration | TEXT | the related term's transliteration | - | lexicon.related |
| related_gloss | TEXT | the related term's own short gloss | - | lexicon.related |
| deleted | INTEGER | soft delete | - | - |

### `validation_result` (written in stage 0.B)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate key | - | - |
| run_id | TEXT | the run that ran the check | - | - |
| word | TEXT | the word the check was over | - | validate |
| step | TEXT | the step that ran it | - | validate |
| check_name | TEXT | which check | - | validate |
| result | TEXT | pass / fail | - | validate |
| detail | TEXT | the specifics — counts, what failed | - | validate |
| ran_at | TEXT | when | - | validate |
| deleted | INTEGER | soft delete | - | - |

### `verse_hib` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | - |
| verse_id | INTEGER | **no use recorded** | - | - |
| hib_id | INTEGER | this HIB is present/a presumptive candidate in this verse (debate digest Step 1) -- also the table B4's future HIB-continuity passage-boundary rule reads from | - | - |
| created_at | TEXT | ISO-8601 UTC | - | - |
| deleted | INTEGER | version-aware soft-delete | - | - |

### `verse_lexical` (written in stage 0.B)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | migration/bootstrap_span_reading.py |
| span_id | INTEGER | which span this reading is for — a span may carry several code_ordinal rows here (one per code in its compound strong_variant) | - | migration/bootstrap_span_reading.py |
| verse_id | INTEGER | denormalized from span, matches verse_passage's own precedent — query without joining through span | - | migration/bootstrap_span_reading.py |
| code_ordinal | INTEGER | position of this code within the span's space-joined strong_variant, 0-based | - | migration/bootstrap_span_reading.py |
| strong | TEXT | the single code this row resolves — may be NULL only if strong_variant itself is empty (should not occur in practice) | - | migration/bootstrap_span_reading.py |
| morph_code | TEXT | this code's own morph slice (space-split from span.morph_code in the same order) | - | migration/bootstrap_span_reading.py |
| role | TEXT | REDESIGNED 2026-09-16 (#1706 Phase B item 3, #1607 D1/D4) — bare JSON array of every live cluster_strong.cluster_code for this strong (T-codes AND M-codes, e.g. '["T5","M12"]'), not an array of objects. Replaces the old content/function morph-tag classifier (escalation #1590's bug — Greek article tag 'T' misclassified content instead of function — is retired-by-design, not patched: the whole classify_role() mechanism is deleted, not fixed). Also the base-data readiness signal itself (#1606 D1): an empty array means zero cluster_strong allocation, the exact FATAL condition `lexical.readiness` Leg 3 and the pre-run unready_codes_in_scope() validator both check for. | - | migration/bootstrap_span_reading.py |
| status | TEXT | 'resolved' (strong row found, sense pulled -- content or function role alike) or 'unregistered' (no strong row yet -- a genuine coverage gap, regardless of role). | - | migration/bootstrap_span_reading.py |
| created_at | TEXT | ISO-8601 UTC | - | migration/bootstrap_span_reading.py |
| deleted | INTEGER | version-aware soft-delete — rewriting a (span_id, code_ordinal) inserts a fresh row and flips the superseded row's deleted to 1, same convention as verse/span/strong | - | migration/bootstrap_span_reading.py |
| position | INTEGER | span.position, denormalized — mechanical, no judgement | - | lexical.build |
| surface | TEXT | span.surface, denormalized — the literal text at this span, independent of sense (never confused with resolved_sense) | - | lexical.build |
| testament | TEXT | derived: 'OT' if cfg_book_order.ordinal<=38 else 'NT' (Mal=38/Matt=39 boundary) — pure ordinal derivation, no reference table | - | lexical.build |
| is_negator | INTEGER | 1 if strong is in cluster_strong WHERE cluster_code='T5' AND deleted=0, else NULL (never 0 -- NULL means 'not in the T5 lexicon'). cfg_lexical_code_class is dead code, never read by load_code_classes() -- corrected, escalation #1607/CA-5, 2026-09-10. | - | lexical.build |
| narrative_morph | TEXT | Hebrew wayyiqtol / az+imperfect flag, derived from morph_code pattern — NULL unconditionally for language != 'Hebrew' | - | lexical.build |
| gloss_consistent_in_verse | INTEGER | 1 unless this (strong, morph_code) pair carries >1 distinct SURFACE value among this verse's own rows — mechanical data-quality check. CORRECTED 2026-09-16 (#1706 Phase B migration): this row previously said 'resolved_sense', stale since escalation #1527 (2026-09-06) rekeyed the actual check to `surface` — resolved_sense is a pure function of (strong, morph_code) with no per-occurrence signal, so a same-code-different-sense check against it could never fire; `surface` (the aligned translation word) genuinely does vary by occurrence. | - | lexical.build |
| party_kind | TEXT | 'divine'/'human'/'non_human' -- set ONLY when this code IS ITSELF a name in cluster_strong WHERE cluster_code IN ('T4','T7','T8','T9') AND deleted=0 (T4=adversarial->non_human, T7=divine, T8=human, T9=angelic->non_human); a pronoun's own party_kind is NOT stored here, it derives via its entity_link note's target_verse_lexical_id (two-hop join, Window 2's own future join). cfg_lexical_code_class is dead code, never read by load_code_classes(); the previous text also omitted T4/party_adversarial from its source list -- both corrected, escalation #1607/CA-6, 2026-09-10. | - | lexical.build |
| updated_at | TEXT | Timestamp of the row's last real content correction (post-insert), set by write_readings_for_span whenever a live row's content actually changes -- INSERT never populates it (CA-7, escalation #1607/#1605: 20/21 live columns were registered, this one never was, since the #1520 identity-stable-write redesign added it). 113,684/544,572 (20.9%) live rows are currently non-NULL, matching 'only rows corrected since #1520 get it set' exactly. | - | lexical.build |

### `verse_meta` (written in stage 0.GAP, D4, RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate PK | - | verse_meta triggers |
| verse_id | INTEGER | the verse this row is about -- unique, one row per verse | - | verse_meta triggers |
| testament | TEXT | 'OT'/'NT', derived from cfg_book_order.ordinal<=38 -- pure function of the verse's own book, no dependency on any other table. Set by verse_meta_on_verse_insert, immutable thereafter (a verse never changes book). | - | verse_meta triggers |
| language | TEXT | 'Hebrew'/'Greek' in practice (domain also allows 'Aramaic' for forward-compatibility, but strong.language never carries it corpus-wide -- checked live 2026-09-09, even H0762 'Aramaic' itself is tagged Hebrew, so this column CANNOT distinguish genuine Aramaic portions). Majority vote across the verse's own live verse_lexical rows (verse_meta_on_lexical_change), testament-based default when none exist yet. Real value: surfaces a per-code language OUTLIER as a data-quality signal (e.g. John.1.18/H5207, a mistagged code) that a testament-only guess would never catch, not language diversity. | - | verse_meta triggers |
| chapter | INTEGER | parsed once from osisId (Book.NN.NN) | - | verse_meta triggers |
| verse_num | INTEGER | parsed once from osisId (Book.NN.NN) | - | verse_meta triggers |
| passage_id | INTEGER | via the verse_passage junction (verse_id unique, one passage per verse) -- NULL if this verse isn't in a passage yet. Synced by verse_meta_on_passage_change. | - | verse_meta triggers |
| is_passage_anchor | INTEGER | via the same verse_passage junction, same trigger as passage_id | - | verse_meta triggers |
| lexical_complete_at | TEXT | NOT populated as of #1608 -- home for CA-12 (`passage.lexical_complete_at`, orphaned by #1451's verse-scoped redesign). Giving it a verse-level home is #1608's job; the completeness-CHECK logic that would populate it is separate, future work. | - | verse_meta triggers |
| created_at | TEXT | ISO-8601 UTC, set once at row creation | - | verse_meta triggers |
| updated_at | TEXT | ISO-8601 UTC, set by any of the 3 refresh triggers (deleted/language/passage_id change) -- NULL means never refreshed since creation | - | verse_meta triggers |
| deleted | INTEGER | soft delete, kept in sync with verse.deleted via verse_meta_on_verse_deleted | - | verse_meta triggers |
| status | TEXT | Researcher-set verse status, one of cfg_enum verse_meta_status (exclude/citated/analysed). NULL = not yet set. Deliberately excludes 'anchor' -- that's already verse_meta.is_passage_anchor, per the researcher's own instruction. Written only by VerseMeta.ps1 -Step SetStatus, never by application code. | - | VerseMeta.ps1 -Step SetStatus (step verse_meta.set_status, lib/versemeta.py) |
| status_changed_at | TEXT | ISO-8601 UTC, set ONLY when `status` actually changes value (not touched on every write) -- the researcher's own 'stamped if the status change' requirement. NULL means status has never been set. | - | VerseMeta.ps1 -Step SetStatus (step verse_meta.set_status, lib/versemeta.py) |

### `verse_passage` (written in stage RETIRED)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate key | - | - |
| passage_id | INTEGER | the passage | - | - |
| verse_id | INTEGER | the verse (unique — one passage per verse) | - | - |
| is_anchor | INTEGER | 1 on the anchor verse - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| created_at | TEXT | when this link was created - now populated by the verse-fanout tracking mechanism, not passage.build | - | report.verse_span_meaning / report.passage_debate (via lib/passagetrack.py) |
| deleted | INTEGER | soft delete | - | - |

### `wa_obs_question_catalogue` (written in stage RECORD)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| data_mechanism | TEXT | What data actually answers this question, checked live against the DB, not asserted: a role-cluster tag (cluster.cluster_code T2-T15), a specific table/cluster (e.g. M47), an existing reading-stage tag (e.g. surface-gloss-divergence), a per-cluster science-extract file (Workflow/Sciences/science_files/), or direct LLM reading of base verse/lexical text with no special tag needed. | - | - |
| dimension | TEXT | One of the 12 goal-derived dimensions (D1-D12, escalation #1712) this question serves, or M0 (lexical/textual evidence, feeds the 12 but is not itself one), X0 (cross-characteristic synthesis, synergy-stage), or a plus-joined list (e.g. D1+D2+D3+D4) for a deliberately consolidated question. Derived from the programme prose definition (Ch.1), independently cross-checked via a blind second derivation, 2026-09-17. | - | - |
| window | None | 11-window analytical-angle taxonomy tag for this catalogue question (e.g. relational, action-impact, origin, meaning, operational, constitutional, literary, faculty, cognitive, affective) -- applied catalogue-wide 2026-09-18. | - | - |
| obs_id | INTEGER | surrogate PK, fresh sequence (not copied from source) | - | - |
| question_code | TEXT | e.g. T1.1.1 -- unique, the catalogue's own stable key | - | - |
| section | TEXT | SUPERSEDED 2026-09-21, escalation #1818 -- redundant with `dimension` (#1712, 2026-09-17). Carries the OLD pre-realignment T0-T7 scheme label for 92 of 103 live rows; `dimension` already carries the live D1-D12/M0/X0/F0 classification for every row, confirmed clean. Checked live before deciding this: no stage-generator module (verse-reading/char-subgroup/char-reading/char-answers) ever reads `section` -- its only live reader is cataloguereport.py, which treats it purely as a documented data-quality finding ('two competing section-naming schemes'), not a working classification. Same verdict already applied in this table to `pattern_type`/`source_word`/`source_registry_no` -- kept for historical/audit value, not read as authoritative by any live code. Use `dimension` for the live classification instead. | - | - |
| question_text | TEXT | the actual catalogue question text | - | - |
| scope | TEXT | The stage-selection bucket a question answers at -- checked live against every stage-generator module's own selection query, 2026-09-21 (escalation #1806 coverage audit): 'Characteristic (HIB behaviour)'/'Characteristic relational'/'The HIB'/'Other non-human beings' select Stage 4 (char-answers); 'Word/term (lexical)'/'Verse-context'/'The verse' are NOT selected by any live stage's query at all (escalation #1806's own still-open ask -- 27 of 103 questions are structurally unreachable on this basis, tracked there, not a defect in this column itself). Registered as cfg_enum wa_obs_question_catalogue.scope, 2026-09-21. | enum.wa_obs_question_catalogue.scope | - |
| status | TEXT | Lifecycle state: 'active' (live, presented to a stage per its scope/mechanism) or 'retired' (superseded, `deleted` should also be 1 -- checked live 2026-09-21, escalation #1818: found and fixed 4 rows, the T7.3.x family, that had deleted=1 but status still 'active', the exact status/deleted-disagreement defect class this table's own migration history already flagged as a known risk). Registered as cfg_enum wa_obs_question_catalogue.status, 2026-09-21. | enum.wa_obs_question_catalogue.status | - |
| deleted | INTEGER | soft-delete | - | - |
| date_added | TEXT | ISO-8601 UTC, set at migration/insert time | - | - |
| catalogue_version | TEXT | e.g. v2-2026-09-16 | - | - |
| review_note | TEXT | free text | - | - |
| tier | TEXT | The live analytical bucket a question belongs to, post-#1712 realignment (2026-09-17): M0 (word-level battery), D1-D12 (the 12 goal-derived dimensions), X0 (cross-characteristic synergy-stage synthesis), F0 (faculty engagement), or T7 (legacy, retired-only -- the 4 deleted T7.3.x rows, never migrated since they're superseded, not live). Registered as cfg_enum wa_obs_question_catalogue.tier, 2026-09-21. | enum.wa_obs_question_catalogue.tier | - |
| component_code | TEXT | e.g. T2.11 | - | - |
| component_title | TEXT | e.g. Faculty Engagement | - | - |
| prompt_seq | INTEGER | Display-ordering only within (tier, component_code) -- confirmed live consumer: cataloguereport.py's own tiered listing (`ORDER BY tier, component_code, prompt_seq, obs_id`). NOT read by any of the 4 live LLM-calling stages (verse-reading/char-subgroup/char-reading/char-answers select question_code/question_text/scope only, never prompt_seq) -- it has zero effect on which questions get asked or in what order the LLM actually sees them within a stage's own prompt; it only affects this one human-facing report's display order. NULL sorts first in SQLite ASC order, so a NULL row displays out of its intended sequence, not absent -- checked and fixed for all 9 rows that had it (2026-09-21, escalation #1818). | - | - |
| source | TEXT | descriptive provenance, not an invented code | - | - |
| last_modified | TEXT | ISO-8601 UTC | - | - |

### `word_registry` (written in stage 0.B)

| Column | Type | Use | Expectation | Filled by |
|---|---|---|---|---|
| id | INTEGER | surrogate key | - | - |
| word | TEXT | the English word | pattern:candidate.tag_clean_pattern | - |
| source | TEXT | why it was registered — the growth trigger | - | - |
| status | TEXT | registry processing stage | enum.word_status | registry+raw+signoff |
| created_at | TEXT | when registered | - | registry.create |
| deleted | INTEGER | soft delete | - | - |

