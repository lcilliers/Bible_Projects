# Session Report — Framework B Soul Word Analysis Programme
## Session A v9 Architecture Design and Stage 1 Evaluation

**Session date:** 2026-03-18  
**Session type:** Architecture design, specification iteration, database evaluation, registry analysis  
**Primary outputs:** Session A v9 Architecture Specification (v1 through v4 Final), Stage 1 Evaluation Report, Empty Words Analysis  

---

## 1. Session Overview

This session covered the complete design cycle for the Session A v9 automated pipeline — from initial concept through four specification iterations incorporating technical review, researcher decisions, and a post-implementation evaluation of the first completed stage. The session also included a systematic analysis of 30 word registry entries with no STEP lexical terms.

The central architectural shift driving the session was the transition from the prior manual workflow (Claude-assisted extraction → source .md files → JSON patch files → database import) to a fully automated pipeline in which a Python engine queries the STEP Bible local API directly and writes all data to the SQLite database without intermediate files.

---

## 2. Participants and Inputs

| Input | Description |
|---|---|
| Researcher | Leroux (Framework B programme director) |
| AI assistant | Claude Sonnet 4.6 |
| Technical reviewer | GitHub Copilot (Claude Sonnet 4.6) — pre-implementation review of v2 draft |
| `session-2026-03-17-step-api-exploration.md` | Full transcript of STEP API discovery session including confirmed endpoints, pagination workaround, span parsing, and complete Session A field mapping |
| `bible_research.db` (initial) | Database at v2.2 schema — 32 complete words, 713 terms, 12,877 verse records |
| `bible_research.db` (Stage 1) | Database post-Stage 1 submission — schema migrated to v3.1.0 |
| `Session-A-Instruction-v8-v5.docx` | Prior manual pipeline specification — the baseline being superseded |

---

## 3. Chronological Record of Work

### 3.1 Initial Assessment and Architecture Framing

The session opened with the researcher's assessment of the v9 direction:

- The automation engine would use the STEP API (confirmed working from the prior session) to systematically fetch all data for every term in the registry
- The database — not intermediate files — would be the single destination for all outputs
- The engine would: identify all terms per word, check mti_terms for existing entries (XREF/NEW), populate term data if NEW, and capture all verse records
- The researcher's view was that data collection could be fully automated, leaving only judgment-dependent flags for researcher review

The first architecture document (v1) was produced covering: the phase overview, term routing logic (XREF/NEW), the 20-step execution sequence, target tables and columns, field mapping from STEP API to database, derivable vs judgment-dependent flags, and the word overview report concept.

**Four open decisions** were identified and put to the researcher at this stage.

---

### 3.2 Researcher Decisions (First Round)

The researcher responded to the four initial decisions:

**D1 — Meaning parser placement:** In GAP_FILL mode the parser should be a separate final stream. In NEW_WORD and AUDIT_WORD it should be integrated — both to verify and to insert/update. 

**D2 — Re-processing existing words:** The architecture must support re-introducing a word and conducting a full audit and update. It must also include introducing new words to the registry with safeguards against database corruption.

**D3 — Batch vs word-by-word:** This depends on the mode — word audit, new word introduction, or gap processing are different. The gap process is the most resource-intensive. Recommended approach: run in streams (fetch all terms for all words, create new terms, then work through terms updating meaning data, then create links and relational tables, etc.).

**D4 — Phase 5 review interface:** Judgment flags will be reviewed later — deferred to the next phase. V9 can ignore them.

**Additional requirements added:**
- Design and specify controls for each step, including self-audit processes with predefined STOP, REVIEW, and APPROVE criteria
- Produce a word overview report covering all aspects of a word from all tables, producible at any point
- Consider new tables to parse meaning data (Hebrew numbered tree structure and Greek prose) — currently raw text, needs to be structured and queryable

---

### 3.3 Architecture v2 — Full Expanded Specification

The second architecture document incorporated all decisions and new requirements. Key additions over v1:

**Three execution modes:** NEW_WORD, AUDIT_WORD, GAP_FILL — each with distinct write permissions and risk profiles.

**Five new control tables:** `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log`, `schema_version` — providing run traceability, resume capability, and audit trail.

**Schema additions approved:**
- `wa_term_inventory.short_def_mounce` (Greek Mounce definition)
- `wa_verse_records.target_word` (English rendering of target Strong's per verse)
- Five new `word_registry` tracking columns
- `wa_term_inventory.parsed_meaning_id` (FK to meaning parse tables)

**Eight-stream GAP_FILL architecture:** S1 Term Discovery → S2 Vocab Fetch → S3 Verse Fetch → S4 DB Write → S5 Flag Engine → S6 Audit → S7 Meaning Parser → S8 Field Fill

**19 predefined audit checks (WR-01 through WR-19):** Each classified as STOP (blocking) or REVIEW (non-blocking). Progressive evaluation — all checks run even after first STOP to give researcher complete context.

**Four meaning parsing tables:** `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` — parsing the Hebrew numbered tree (1), 1a), 1a1) outline structure) and the Greek LSJ entries into structured, queryable form.

**Word overview report:** 15 sections covering all database content for one word, producible at any point, in HTML and JSON formats with colour-coded gap highlighting.

**Disaster recovery, backup, and safeguarding section:** 13 mandatory safeguarding rules (SG-01 through SG-13), backup policy (pre-run, post-run, pre-migration, Synology sync, manual), three recovery scenarios with command sequences, and version control guidelines.

**Schema migration (M01–M10):** Complete migration sequence from v2.2 to v3.0, with mandated MIGRATION.md document requirement.

**Five open decisions (D1–D5)** presented for researcher approval.

---

### 3.4 Researcher Decisions (Second Round)

**D1:** Confirmed — parser separate in GAP_FILL (S7), integrated in NEW_WORD/AUDIT_WORD.

**D2:** Full audit/reintroduction must be supported. New word registration must be a controlled subcommand. Safeguards must prevent database corruption.

**D3:** Parallelism specification should provide guidance but implementation must verify API capabilities. Recommended sequential default with configurable concurrency.

**D4:** Field-fill step at end of GAP_FILL (S8). Automatically included in word-based modes.

**D5:** Tool builder mandated to fully document the schema migration process — the spec already documents the schema and can be extended.

**Additional requirements:** Disaster recovery, backup/restore, and overall safeguarding guidelines for the application creator.

---

### 3.5 Architecture v3 — Technical Review Incorporated

GitHub Copilot conducted a pre-implementation review of the v2 draft and identified 14 items (4 critical, 5 important, 5 minor). All 14 were resolved in v3:

**Critical fixes:**

1. **Transaction restructure** — API calls (N8–N9) moved out of the database transaction. Pre-transaction phase handles all network I/O; the atomic write block covers DB inserts only. This eliminates the risk of holding a write lock during a network call.

2. **Multi-part word handling** — Full specification added: split threshold (12+ NEW terms), part invocation syntax (`--part=1 --parts=2`), wa_file_index field mapping, `root_families_in_prior_parts` derivation rule (query existing wa_term_root_family rows for prior parts and write as JSON array).

3. **`wa_term_root_family` ruling** — Explicitly ruled as researcher-deferred (same tier as god_as_subject). Engine never writes to this table. WR-13 updated to exclude root family, god_as_subject, somatic_link, mti_term_flags, and researcher-confirmed nulls from the undocumented-null check.

4. **`also_spelled` duplication removed** — Migration M04 (adding also_spelled to mti_terms) removed. The field already exists in wa_term_inventory with 17 populated rows. Single authoritative location confirmed.

**Important additions:**

5. `--from` flag formally defined (fresh sub-run, not a checkpoint resume)
6. `engine.py --clear-lock` command specified for stale IN_PROGRESS sentinel recovery
7. `occurrence_count_qualifier` added to S8/N19/A8 field-fill steps
8. S1 now sets `phase1_status = In Progress` when writing wa_file_index
9. WR-05 reworded — scoped to contiguous ID range for this word's rows in this run, not global sequential check

**Minor clarifications:**

10. Baseline row counts footnoted as point-in-time reference values only
11. `mti_term_flags` (THEOLOGICAL_ANCHOR) explicitly listed as judgment-deferred in field mapping
12. `wa_file_index.root_families_in_prior_parts` mapped with derivation rule
13. `word_registry.phase1_input_file` — engine writes run_id here, replacing .md filename convention
14. Engine location confirmed: `engine/` package at project root

---

### 3.6 Researcher Decision — Multi-Part Logic Removal

The researcher questioned the continued inclusion of multi-part split logic (step N5) in the NEW_WORD sequence. The rationale was sound: the multi-part mechanism existed entirely because of Claude's context window limits in the manual pipeline. The automation engine processes all terms in a single Python loop with no context constraint.

**Decision:** Multi-part split assessment removed entirely from the v9 engine. The wa_file_index part columns (`part_number`, `total_parts`, `is_split`, `root_families_in_prior_parts`) are retained as legacy read-only — they hold valid data for 14 existing multi-part words but are never written by the v9 engine for new words.

---

### 3.7 Verse Handling — Span Filter Design

The researcher raised the shared-verse problem: terms in the same root family often share a verse set in STEP, making it difficult to determine which verses genuinely contain the specific term under study.

**Analysis conducted:** Database investigation confirmed 15 terms with verse counts exceeding their occurrence counts. The most extreme case: H7442A (run) has 2 confirmed occurrences but 53 verse records — all 51 extra verses belong to sibling forms H7442B and H7444.

**Key finding:** The STEP masterSearch preview HTML already contains the answer. Each verse's `<span strong='...' morph='...'>` attribute identifies exactly which Strong's number is tagged at that word position. This data is available in the existing API response — no additional call needed.

**Two options considered:**

- **Option A:** Fetch all verses, store all, add `span_strong_match` flag (1 = confirmed, 0 = not applicable)
- **Option B:** Filter at fetch time — store only verses where the queried Strong's appears in the span

**Researcher decision:** Option B with the following reasoning — verses are in the database to show the term in operation. A verse where the term is absent from the original-language tagging is not a verse of that term. It will appear under its actual term's verse set when that term is processed. Cross-term relationships are better understood by examining both terms' confirmed verse sets in parallel.

**AUDIT_WORD back-population:** All existing verse records should be re-fetched and span-assessed — not just the inflated-count cases. `span_strong_match` should be set on every verse record.

**Phase 2 context design:** Phase 1 stores only the reference verse. The schema should reserve `context_before` and `context_after` columns (null in Phase 1) for selective Phase 2 enrichment where the researcher identifies a need. The need cannot be anticipated in advance.

---

### 3.8 Architecture v4 — Final Document

The fourth and final architecture specification incorporated:

**New §5 Verse Handling** — dedicated section covering the shared-verse problem, the span filter rule, span resolution conflict handling, verse count display in the overview report, AUDIT_WORD sub-step A3a (back-population of all existing verse records), and the Phase 2 context design forward reference.

**Four new `wa_verse_records` columns:** `target_word`, `span_strong_match`, `context_before`, `context_after`. Migration M05 extended to add all four in one step.

**Three new quality flag rows:** `SPAN_RESOLUTION_CONFLICT` (id=23), `SPAN_FILTER_APPLIED` (id=24), `SPAN_BACK_POPULATED` (id=25) added to `wa_quality_flag_types` as reference data in M02.

**WR-20 added** — audit check for span_strong_match completeness.

**Multi-part legacy note** (§7.3) — explicit explanation of why the part columns exist, that they hold valid data for 14 existing words, and that the v9 engine treats them as read-only.

**engine_run_log extended** — two new columns: `total_verses_filtered` and `total_meanings_parsed`.

The v4 document was marked ready for researcher sign-off with a 15-section approval checklist.

---

### 3.9 Stage 1 Evaluation

The developer submitted the database following Stage 1 implementation. Evaluation was conducted against the v4 specification.

**Schema migration: PASS**

All ten migrations (M01–M10) applied. Schema version 3.1.0 (developer incremented to 3.1.0 rather than 3.0.0 — acceptable). All 28 tables present and correct. All 4 new wa_verse_records columns added. All 2 new wa_term_inventory columns added. All 5 new word_registry columns added. All 3 new quality flag rows added (ids 23–25). 30 custom indexes present. WAL mode active. Integrity check: OK.

**One unspecified addition:** `word_registry.strongs_list` — a JSON array of Strong's numbers and counts pre-populated for 137 of 167 Pending words. Not in the v4 spec but a valid preparation step. Recommended: retain and document as an input-preparation column.

**S1 Term Discovery: PARTIAL**

The engine_run_log records one GAP_FILL run with 167 words_attempted and S1 marked complete with 167 rows_written. However all completion counters show zero (words_complete, total_terms_new, total_verses_inserted). S1 populated `strongs_list` only — it did not insert wa_file_index rows, run mti_terms classification, set phase1_status to In Progress, or write term_fetch_log rows. S2–S8 cannot execute without S1 completing.

**Data preservation: PASS**

All 32 complete words intact. 713 term inventory rows, 12,877 verse records, 698 mti_terms rows, 2,653 related word rows, 461 phase 2 flags, 404 quality flags — all unchanged from pre-migration.

**Pre-existing issues identified (not introduced by Stage 1):**

- 50 wa_term_inventory rows with term_id mismatch (legacy inconsistent format); 7 true orphans with no matching mti_terms row. WR-04 join should use strongs_number, not term_id.
- Peace registry (117): zero verse records — known pre-existing gap from v2 schema rebuild. First priority for AUDIT_WORD.
- All 12,877 verse records have `span_strong_match = null` — correct and expected; resolved by AUDIT_WORD A3a.
- Migration history logged twice in schema_version (M01–M09 each appear twice) — cosmetic issue, no functional impact. One-line code fix.

**Four actions required before S2–S8:**

1. Complete S1 (insert wa_file_index, run mti_terms classification, write term_fetch_log, set phase1_status)
2. Researcher review of 30 words with empty strongs_list
3. Fix migration history deduplication in migration script
4. Update WR-04 join to use strongs_number not term_id

---

### 3.10 Empty strongs_list Word Analysis

A systematic analysis of all 30 words with no STEP terms was conducted, examining each against existing registry entries and the Hebrew/Greek lexicon.

**Results:**

| Verdict | Count | Words |
|---|---|---|
| ✅ Covered | 10 | assent, blamelessness, commitment, contrition, hopelessness, ingratitude, intuition, personality, reliability, self-awareness |
| ⚠️ Partial | 8 | awareness, communion, cowardice, determination, manipulation, sensitivity, sexuality, vulnerability* |
| ❌ Gap | 11 | betrayal, conformity, darkening, deadness, identity, image of God, laziness, personhood, resentment, transformation, vulnerability |
| ℹ️ Special | 2 | emotion (meta-concept — remove), spiritual powers (Session D synthesis only) |

**Highest priority new entries:**

1. **Image** — H6754 (tselem), H1823 (demuth), G1504 (eikōn). Foundational anthropological terms entirely absent from the registry.
2. **Transformation** — G3339 (metamorphoō, including Rom 12:2). One of the most significant inner-being verses in the NT has no registry home.
3. **Treachery** (replacing betrayal) — H0898 (bagad, 51 occurrences).
4. **Name** (replacing identity) — H8034 (shem, 864 occurrences) — name as identity and character.
5. **Resentment** — H7107 (qatsaph, 46 occurrences) — distinct from anger and bitterness in its relational persistence.

**Twelve words recommended for `automation_eligible = 0`:** assent, blamelessness, commitment, contrition, emotion, hopelessness, ingratitude, intuition, personality, reliability, self-awareness, spiritual powers.

---

## 4. Decisions Record

| # | Decision | Outcome |
|---|---|---|
| D1 | Meaning parser placement by mode | GAP_FILL: separate S7 stream. NEW_WORD/AUDIT_WORD: integrated after DB_WRITE |
| D2 | Re-processing existing words | AUDIT_WORD mode after GAP_FILL completes. New word registration via --register subcommand |
| D3 | API parallelism | Configurable --parallel=[N], default sequential. Tool builder confirms safe limit during development |
| D4 | also_spelled / occurrence_count_qualifier | Field-fill step S8 (GAP_FILL), N19 (NEW_WORD), A8 (AUDIT_WORD) |
| D5 | Schema migration tooling | Tool builder mandated to produce MIGRATION.md with complete DDL |
| — | Multi-part split logic | Removed entirely — context-window artefact not applicable to automation engine |
| — | Verse span filtering | Option B: store only span-confirmed verses. All existing verses back-populated by AUDIT_WORD A3a |
| — | Phase 2 context columns | context_before and context_after reserved in schema, null in Phase 1 |
| — | emotion (#54) | Remove as registry entry — meta-concept, not a lexical term |

---

## 5. Documents Produced

| Document | Version | Status |
|---|---|---|
| Session A v9 Architecture Specification | v1 | Superseded |
| Session A v9 Architecture Specification | v2 DRAFT | Superseded |
| Session A v9 Architecture Specification | v3 Final | Superseded |
| Session A v9 Architecture Specification | **v4 Final** | **Current — ready for sign-off** |
| Stage 1 Evaluation Report | v1 | Delivered |
| Empty Words Analysis | v1 | Delivered |

---

## 6. Current State

### Database
- Schema: v3.1.0 (all migrations M01–M10 applied)
- Complete words: 32 (unchanged)
- Pending words: 167 (strongs_list populated for 137)
- New control tables: created and empty (awaiting S1 completion)
- New parsing tables: created and empty (awaiting meaning parser)

### Pending work — immediate
- S1 completion (wa_file_index inserts, mti_terms classification, term_fetch_log writes)
- Developer fix: migration history deduplication
- Developer fix: WR-04 join on strongs_number
- Researcher decision: 30 empty-strongs_list words (12 to automation_eligible=0; 11 new entries; 8 confirm/redirect)

### Pending work — next phase
- S2–S8 execution for 167 Pending words
- AUDIT_WORD for 32 complete words (priority: peace #117 for verse back-population; all 32 for span back-population A3a)
- Researcher judgment flags (god_as_subject, somatic_link, root family, mti_term_flags) — deferred to next phase
- Meaning parser (wa_meaning_* tables) — deferred to after S4 completion
- New registry entries for 11 identified gaps

### Specification status
- Session A v9 Architecture v4 Final: ready for researcher sign-off
- Upon sign-off: this document is the coding specification for S2–S8 implementation

---

## 7. Key Technical Decisions — Reference

### STEP API
- Endpoint: `localhost:8989`
- Vocab: `GET /rest/module/getInfo/ESV_th//{STRONG}//`
- Verses: `GET /rest/search/masterSearch/strong={STRONG}|version=ESV_th`
- Pagination: section-range workaround (5 canonical sections, each < 60 results)
- Span parsing: `<span strong='H8057 H9003'>joy</span>` — strong= attribute identifies which terms appear

### Database
- Engine: SQLite with WAL mode
- Schema version: 3.1.0 (spec target: 3.0.0)
- Location: `bible_research.db`
- Backup: pre-run automatic to `/backups/`, Synology sync in scope

### Engine
- Location: `engine/` package at project root
- Entry point: `engine/engine.py`
- API client: `step_client.py` (existing, from STEP API exploration session)

---

*Session report produced: 2026-03-18*  
*Framework B Soul Word Analysis Programme — Phase 1 STEP Data Assimilation*
