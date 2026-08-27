# Prose Edit — Programme — Chapter 4

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 66 -->
<!-- PROSE_SECTION_TYPE: prog_data_obslog_pipeline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 4 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Obslog-to-DB capture pipeline -->
<!-- PROSE_SORT_ORDER: 32 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: programme-prose-v2-recommendations-v1-20260427.md -->

## Programme — Obslog-to-DB capture pipeline

Architecture v2 introduces a structured pipeline by which Session B analytical work is captured into the database. Where the patch flow moved discrete database changes from AI to CC, the obslog flow moves analytical content — observations, Q&A pairs, chapters, SD pointers, anchor-verse readings, new questions, review notes — from a comprehensive obslog `.md` to its DB target tables in a single transactional pass.

The pipeline runs in three phases. Phase 1 is parsing: Claude Code reads the obslog and produces a structured manifest in JSON, validated for completeness against declared counts. Phase 2 is writing: each manifest category is dispatched to its target table — observations become `wa_session_b_findings` rows, Q&A pairs become `wa_finding_catalogue_links` rows with entity links to verses and groups and dimensions, chapters become `prose_section` rows under section_type codes `sb_s2c_ch1` through `sb_s2c_ch5`, anchor-verse analytical readings update `verse_context.analysis_note`, new questions enter `wa_obs_question_catalogue`, review notes append to existing catalogue rows, and SD pointers and status updates land in their respective tables. Phase 3 is validation and anomaly raising: post-write, Claude Code verifies row counts, foreign-key integrity, and the catalogue-link coherence; data inconsistencies surface as `DATA_ANOMALY_*` findings at `status='open'`, carried into the next analytical session for AI to address.

Idempotency is structural. The writer's per-category logic checks for existing rows before inserting — re-running on the same obslog produces no duplicates. The pipeline is transactional: pre-write backup, single-transaction commit, all-or-nothing on failure. The schema supports this with M40 through M43, the four migrations that landed the architecture: a `verse_context.analysis_note` column for anchor-verse commentary, a `wa_prose_section_citations` table for the chapter-to-evidence audit trail, a `wa_obs_question_catalogue.review_note` column for catalogue maintenance, and a `wa_finding_catalogue_links.finding_id` nullability change to support the no-finding and not-applicable coverage states.

A revision session adds one further discipline: every chapter affected by the revision is superseded under v2.7 / v2.CC9, with citation-disciplined prose covering the newly-resolved findings. Claude Code's writer detects `SUPERSEDE: sb_s2c_ch{n}` blocks in the obslog, retires the prior `prose_section` row via the `superseded_by_id` chain, writes the new row at incremented version, and extracts inline citations into `wa_prose_section_citations` with FK resolution to findings, SD pointers, and Q&A links. A four-check coherence audit at session close verifies that every revision-resolved finding is cited, that every chapter that should be superseded has been, that citation FK resolution clears a 90% threshold per chapter, and that every anchor verse appears in at least one current chapter prose body. Failures surface as `DATA_ANOMALY_*` findings for the next session.

Two further artefacts complete the pipeline. The readiness `.md` and `.json`, generated before the analytical session, present every data field in the registry's current state with a clear destination and a prompt for the analyst — the field-level destination audit guarantees that nothing the readiness presents is silently passed over. The analytic status `.md`, generated for revision sessions, captures the prior analytical state — lifecycle summary, resolved Q&A pairs, resolved SD pointers, prior chapters, anchor analyses, open items — so that revision work has both the current data and the prior analysis in view. Together the readiness output, the obslog, and the analytic status form a closed loop: data state in, analytical work, capture to DB, anomalies surfaced for next session, revision input ready.

---
