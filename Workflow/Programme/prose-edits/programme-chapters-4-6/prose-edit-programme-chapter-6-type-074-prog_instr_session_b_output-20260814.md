# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 68 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_b_output -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session B — Analysis Output -->
<!-- PROSE_SORT_ORDER: 121 -->
<!-- PROSE_VERSION: 2 -->
<!-- PROSE_SOURCE_FILE: programme-prose-v2-recommendations-v1-20260427.md -->

## Session B — Analysis Output

The Session B Analysis Output instruction governs the analytical production stage of Session B — where a word is read in depth and the programme's principal analytical output is written. Under Architecture v2 (effective 2026-04-27), this stage takes the readiness `.md` (and, for revision sessions, also the analytic status `.md`) as input and produces a single comprehensive obslog `.md` as output. There are no AI-submitted patches.

The stage retains its three sub-stages. Stage 2a is the comprehensive reading — every verse in the registry read against the full verse context and the dimensional profile, with observations captured to the obslog as they arise. Stage 2b is the Q&A partitioning — findings from the reading are linked to catalogue questions, producing answers against existing universal questions, raising new GAP questions where the catalogue does not yet cover the surfaced pattern, and marking questions as not-applicable where the word's evidence does not engage the question's domain. Stage 2c is the analytic word output — five chapters of analytical prose (Word Characteristic Summary, Word Impact Description, Annotated Verse Evidence, Original Language Vocabulary, Connections and Research Pointers) plus a sixth section (Open Items) that compiles SD pointers for Session D.

Two disciplines are mandatory under v2. The first is citation discipline: every Stage 2b answer must cite its source observation as an OBS-NNN reference inline; every Stage 2c chapter substantive claim must cite at least one source — an OBS-NNN, a Q&A code, an SD pointer code, or an existing finding ID. Without these citations, CC's parser cannot link the answer to its evidence and the audit trail breaks. The second is the §N open-item discipline: every open Session B finding carried forward into the session — visible in §N of the readiness `.md` — must reach a resolution outcome before session close. The obslog records the chosen outcome path (Q&A, new GAP question, SD pointer, not-relevant) for each open item; CC's parser reads these closures and updates the lifecycle state. When an analytic revision is performed on a previously analysed registry, the same disciplines apply to revisited prose: chapters whose content is affected by the revision must be superseded with citation-disciplined versions covering the newly-resolved findings, ensuring the prose-versus-findings audit trail remains complete.

The obslog is the canonical artefact. Claude Code parses it into the database after the session: chapters write to the prose store, Q&A pairs populate the catalogue-link table, observations land as new findings, SD pointers and dimension references become flag and entity-link rows, anchor-verse analytical readings return to the verse_context table, new catalogue questions enter the question store, and review notes append to existing catalogue rows. Every category of analytical content has a defined target table; nothing the obslog records is silently dropped.

Closure is the writer's status_update operation, advancing `word_registry.session_b_status` to Analysis Complete. Session C opens on the chapter prose; Session D is notified of the SD pointers. Where Readiness prepares, Output produces — together they remain the pair, but under v2 their delivery mechanism is the obslog-to-DB capture pipeline, not the patch flow.

---
