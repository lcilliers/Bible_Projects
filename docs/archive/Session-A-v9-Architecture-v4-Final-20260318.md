
Framework B  ·  Soul Word Analysis Programme
Session A  v9
Automation Architecture Specification  —  v4 Final

Phase 1 — STEP Data Assimilation  |  2026-03-18  |  Supersedes: v3


| Status | READY FOR RESEARCHER SIGN-OFF |
|---|---|
| v3→v4 changes | (A) Multi-part logic removed — context-window artefact not applicable to automation engine. (B) Span-based verse filtering added — only verses where the queried Strong's is confirmed in the original-language span are stored. (C) Three new wa_verse_records columns: span_strong_match, context_before, context_after. (D) Two new quality flags: SPAN_RESOLUTION_CONFLICT, SPAN_FILTER_APPLIED. (E) AUDIT_WORD sub-step A3a added for span back-population across all existing verse records. |


# 1.  Governing Principles
These six principles govern every design decision. All implementation choices must be traceable to at least one of them.

1.1  Database is the single source of truth.  The engine reads from and writes to the database. No intermediate files. word_registry is the master driver.
1.2  The registry is the anchor.  Every run begins and ends with a confirmed word_registry row. No work begins without one. No word is marked complete without a passing audit.
1.3  Idempotency by design.  Every write is safe to re-run. Duplicate prevention is structural (UNIQUE constraints, conflict_action IGNORE), not procedural.
1.4  Audit at every boundary.  Every phase transition includes a structured self-audit with predefined STOP, REVIEW, and PASS criteria. No phase proceeds past a STOP without researcher sign-off.
1.5  Automation handles data; judgment stays with the researcher.  The engine populates everything the STEP API supplies without interpretation. Fields and flags requiring semantic or theological judgment are deferred to the next phase.
1.6  Modes are distinct code paths.  NEW_WORD, AUDIT_WORD, and GAP_FILL are separate execution paths with different entry conditions, write permissions, and audit gates. They share library functions but never share state.

# 2.  Execution Modes
Three modes plus a registration subcommand. The researcher specifies the mode at invocation. The engine confirms mode, target, and pre-conditions before writing anything.


| Mode | Invocation | Write scope | Meaning parser | Risk |
|---|---|---|---|---|
| NEW_WORD | engine.py --mode=new --registry=[id] | All content tables for this word. Pre-transaction API assembly then single atomic write. | Integrated: after DB_WRITE, before audit. | Low |
| AUDIT_WORD | engine.py --mode=audit --registry=[id] | Read + compare. Write only researcher-approved gaps. Includes span back-population of all verse records. Never DELETEs. | Integrated: re-parses and updates wa_meaning_* tables. | Medium |
| GAP_FILL | engine.py --mode=gap [--from=[id]] | All content tables across all Pending words. Stream-based with checkpointing. | Separate stream S7 after all data writes and audits. | High |
| REGISTER | engine.py --register --word=[w] --source=[s] | word_registry INSERT only. | N/A | Minimal |


◆  D2 RESOLVED: The 32 already-complete words are processed in AUDIT_WORD mode after GAP_FILL finishes for all Pending words. A key step of that AUDIT_WORD run is span back-population (sub-step A3a) — see Section 6.5.


# 3.  Automation Control Tables
Five new tables form the safeguard and audit layer. They hold no biblical data, are never deleted, and are written exclusively by the engine.


| Table | Written by | Purpose |
|---|---|---|
| engine_run_log | Engine (every invocation) | One row per engine run. Records mode, target, outcome, counts, errors. Append-only. |
| engine_stream_checkpoint | Engine (GAP_FILL only) | One row per stream per run. Tracks status and last-processed position. Enables resume. |
| word_run_state | Engine + researcher | One row per word per run. Audit result, STOP/REVIEW/PASS, researcher approval. |
| term_fetch_log | Engine (every fetch) | One row per term per fetch attempt. API outcome, verse count, warnings. |
| schema_version | Migration scripts | Single row: current schema version and migration history JSON. |


## 3.1  engine_run_log

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| run_id | TEXT | UNIQUE | RUN-YYYYMMDD-HHMMss-[MODE] |
| mode | TEXT |  | NEW_WORD / AUDIT_WORD / GAP_FILL |
| target_registry_ids | TEXT |  | Comma-separated registry_id values |
| started_at | TEXT |  | ISO datetime |
| completed_at | TEXT |  | ISO datetime; null if incomplete |
| outcome | TEXT |  | COMPLETE / PARTIAL / FAILED / STOPPED |
| words_attempted | INTEGER |  | Words targeted |
| words_complete | INTEGER |  | Words reaching PASS audit state |
| words_stopped | INTEGER |  | Words halted at STOP condition |
| total_terms_new | INTEGER |  | NEW mti_terms rows inserted |
| total_terms_xref | INTEGER |  | mti_term_cross_refs rows inserted |
| total_verses_inserted | INTEGER |  | wa_verse_records rows inserted (span-confirmed only) |
| total_verses_filtered | INTEGER |  | Verse records discarded by span filter (not stored) |
| total_meanings_parsed | INTEGER |  | wa_meaning_parsed rows written |
| error_detail | TEXT |  | JSON array of error objects; null if none |
| resume_from | TEXT |  | run_id of prior run if this is a resume; null otherwise |


## 3.2  engine_stream_checkpoint

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| run_id | TEXT | FK | References engine_run_log.run_id |
| stream_name | TEXT |  | S1_TERM_DISCOVERY … S7_MEANING_PARSER / S8_FIELD_FILL |
| status | TEXT |  | pending / running / complete / failed |
| last_registry_id | TEXT |  | Last registry_id fully processed |
| last_strong | TEXT |  | Last Strong's number processed within stream |
| rows_written | INTEGER |  | Cumulative DB rows written in stream |
| rows_filtered | INTEGER |  | Verse rows discarded by span filter in this stream (S3/S4) |
| error_detail | TEXT |  | JSON error if status = failed |
| started_at | TEXT |  | ISO datetime |
| completed_at | TEXT |  | ISO datetime; null if not finished |


## 3.3  word_run_state

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| run_id | TEXT | FK | References engine_run_log.run_id |
| registry_id | TEXT |  | Zero-padded three-digit registry number |
| word | TEXT |  | English word label |
| phase_reached | TEXT |  | DISCOVERY / FETCH / WRITE / FLAGS / AUDIT / MEANING_PARSE / COMPLETE |
| audit_result | TEXT |  | PASS / REVIEW / STOP / null |
| audit_detail | TEXT |  | JSON: per-check result for every WR-xx check |
| stop_reason | TEXT |  | Human-readable description if STOP |
| researcher_approved | INTEGER |  | 0 = not approved; 1 = approved — required to unblock STOP words |
| approved_by | TEXT |  | Approver identifier |
| approved_at | TEXT |  | ISO datetime of approval |


## 3.4  term_fetch_log

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| run_id | TEXT | FK | References engine_run_log.run_id |
| registry_id | TEXT |  | Registry this term belongs to |
| strongs_input | TEXT |  | Strong's as provided to engine |
| strongs_resolved | TEXT |  | Resolved form after _resolved_strong() call |
| suffix_resolution | INTEGER |  | 1 if resolved ≠ input; 0 otherwise |
| vocab_status | TEXT |  | ok / failed / partial |
| verse_status | TEXT |  | ok / failed / partial / zero_results |
| verse_count_fetched | INTEGER |  | Verse records returned by STEP API (pre-filter) |
| verse_count_stored | INTEGER |  | Verse records stored after span filter (span_strong_match = 1 only) |
| verse_count_filtered | INTEGER |  | Verse records discarded by span filter |
| span_conflict | INTEGER |  | 1 if all fetched verses were filtered (SPAN_RESOLUTION_CONFLICT); 0 otherwise |
| api_warnings | TEXT |  | JSON array of step_client warnings; null if none |
| fetched_at | TEXT |  | ISO datetime of fetch |


## 3.5  schema_version

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Always 1 — single row |
| version_code | TEXT |  | Semantic version: "3.0.0" |
| applied_at | TEXT |  | ISO datetime of most recent migration |
| migration_history | TEXT |  | JSON array: {version, description, applied_at, sql_summary} |
| engine_min_version | TEXT |  | Minimum engine build compatible with this schema |


⚠  The engine reads schema_version at startup. A version mismatch halts the run with a message to run engine.py --migrate first.


# 4.  Schema Additions and Amendments
✔  v4 CHANGE: Migration M04 (mti_terms.also_spelled) remains removed. v4 adds three new columns to wa_verse_records: span_strong_match, context_before, context_after. These replace the single target_word addition in prior drafts — target_word is still added, and the three verse-handling columns are added in the same migration step M05.


| Table | Column / Object | Type | Rationale |
|---|---|---|---|
| wa_term_inventory | short_def_mounce | TEXT | NEW. Mounce short definition. Greek only; null for Hebrew. |
| wa_verse_records | target_word | TEXT | NEW. English rendering of target Strong's per verse, from span. Nullable. |
| wa_verse_records | span_strong_match | INTEGER | NEW. 1 = queried Strong's confirmed in span strong= attribute. 0 = only related form in span. Null = pre-v9 record not yet back-populated. See Section 5.5. |
| wa_verse_records | context_before | TEXT | NEW. Reserved for Phase 2. One or more preceding verses for context, where researcher identifies the need. Null for all Phase 1 records. See Section 5.6. |
| wa_verse_records | context_after | TEXT | NEW. Reserved for Phase 2. One or more following verses for context. Null for all Phase 1 records. See Section 5.6. |
| wa_term_inventory | parsed_meaning_id | INTEGER | NEW. FK to wa_meaning_parsed.id. Null until parser runs. |
| word_registry | automation_eligible | INTEGER | NEW. 1 = automatable; 0 = manual handling required. Default 1. |
| word_registry | last_automation_run | TEXT | NEW. ISO datetime of most recent run. |
| word_registry | automation_run_id | TEXT | NEW. FK to engine_run_log.run_id. |
| word_registry | phase1_term_count | INTEGER | NEW. Count of NEW terms written. |
| word_registry | phase1_verse_count | INTEGER | NEW. Total verse records stored (span-confirmed). |
| wa_quality_flag_types | SPAN_RESOLUTION_CONFLICT (id=23) | — | NEW ROW. DATA_COVERAGE group. The queried Strong's did not appear in any verse span after suffix resolution. Verse set may be empty or assigned to a sibling form. Manual STEP UI verification required. |
| wa_quality_flag_types | SPAN_FILTER_APPLIED (id=24) | — | NEW ROW. DATA_COVERAGE group. One or more verse records were discarded by span filter during fetch or AUDIT back-population. verse_count_filtered in term_fetch_log records the count. |
| wa_quality_flag_types | SPAN_BACK_POPULATED (id=25) | — | NEW ROW. NOTE group. AUDIT_WORD sub-step A3a has been run for this term — all verse records now have span_strong_match set. Records that received span_strong_match = 0 are retained but marked as non-applicable to this term. |
| engine_run_log | (new table) | — | Control. Section 3.1. |
| engine_stream_checkpoint | (new table) | — | Control. Section 3.2. |
| word_run_state | (new table) | — | Control. Section 3.3. |
| term_fetch_log | (new table) | — | Control. Section 3.4. |
| schema_version | (new table) | — | Control. Section 3.5. |
| wa_meaning_parsed | (new table) | — | Meaning parsing. Section 9.1. |
| wa_meaning_sense | (new table) | — | Meaning parsing. Section 9.2. |
| wa_meaning_stem | (new table) | — | Meaning parsing. Section 9.3. |
| wa_lsj_parsed | (new table) | — | Meaning parsing. Section 9.4. |



# 5.  Verse Handling — Span Filtering and Context Design
This section defines the complete verse handling model: how verses are fetched, how the span filter determines which verses are stored, how the AUDIT_WORD back-population works, and how the schema supports Phase 2 context enrichment.

## 5.1  The Shared-Verse Problem
When STEP's masterSearch is queried for a Strong's number (e.g. H7442A), STEP's search index returns every verse where any member of the same root family appears. In the H7442 family this returns 53 verses — but H7442A has only 2 confirmed occurrences; the other 51 are tagged H7442B or H7444 in the original-language span.
Storing all 53 verses under H7442A would make that term appear to have 51 verses it does not own. When a researcher examines verses to understand how H7442A operates as an inner being term, non-applicable verses produce noise, not insight.
The correct verses for each sibling term will appear under that term's own verse set when it is processed — so no analytical value is lost by filtering. A verse that contains both H7442A and H7442B in the same passage will appear in both terms' verse sets, and the relationship between those terms operating together will be visible when the researcher examines them in parallel.

## 5.2  The Span Filter
The STEP masterSearch preview HTML for each verse contains inline span tags:
<span morph='HVqp3ms' strong='H7442B H9001'>sang</span>
The strong= attribute lists every Strong's number tagged to that word token, including grammatical prefix codes (H9001, H9002, H9003 etc.). The filter rule is:


| Condition | Result |
|---|---|
| The queried Strong's number appears in the strong= attribute of the target-word span | STORE the verse. Set span_strong_match = 1. Set target_word from the span text. |
| The strong= attribute contains only sibling forms or prefix codes, not the queried Strong's | DISCARD the verse. Do not insert a row. Increment verse_count_filtered in term_fetch_log. |
| All verses fetched for a term are discarded (zero stored after filter) | Store zero verse records. Set span_conflict = 1 in term_fetch_log. Write SPAN_RESOLUTION_CONFLICT quality flag. See Section 5.3. |


ℹ  The filter is applied during S3 (VERSE_FETCH) in GAP_FILL mode and during step N9 in NEW_WORD mode. The raw HTML is parsed once per verse; both target_word and span_strong_match are extracted in the same pass. There is no additional API call.

## 5.3  Span Resolution Conflict
A span resolution conflict occurs when suffix resolution has remapped the queried Strong's to a canonical form that differs from the input. For example, querying H7442A may cause STEP to search on H7442B internally, returning verses where H7442B appears in the span but H7442A does not. After filtering, zero verses are stored.
When this occurs the engine:
• Stores zero verse records for the term.
• Sets span_conflict = 1 in term_fetch_log.
• Writes SPAN_RESOLUTION_CONFLICT quality flag (id=23) to wa_data_quality_flags with description: "Queried Strong's [H7442A] not found in any verse span after suffix resolution to [H7442B]. Verse set is empty. Manual STEP UI verification required."
• Sets verse_status = "zero_results" in term_fetch_log.
• Does NOT trigger a STOP — this is a REVIEW condition. The term record is written with all lexical data; only verses are absent.

## 5.4  Verse Counts in the Word Overview Report
The word overview report displays two verse counts per term:

| Count | Definition |
|---|---|
| Confirmed verses | COUNT(wa_verse_records WHERE term_inv_id = id AND span_strong_match = 1). This is the working verse set — verses where the term is present in the original language. |
| Filtered verses | COUNT(wa_verse_records WHERE term_inv_id = id AND span_strong_match = 0). These exist only for pre-v9 records back-populated by AUDIT_WORD. Displayed with strikethrough or grey styling. Label: "not applicable to this term." |
| Pre-v9 unassessed | COUNT(wa_verse_records WHERE term_inv_id = id AND span_strong_match IS NULL). Existing records not yet back-populated. Shown with amber styling. Label: "span not verified." |


## 5.5  AUDIT_WORD Span Back-Population (Sub-Step A3a)
When AUDIT_WORD is run for a word that has existing verse records (pre-v9 data), sub-step A3a re-fetches the STEP preview HTML for every stored verse and applies the span filter retroactively. This applies to all verse records for the word — not just those where verse_count exceeded occurrence_count.


| Sub-step | Action | Detail |
|---|---|---|
| A3a.1 | Re-fetch all verse spans | For each wa_verse_records row for this registry: re-call masterSearch for the term's Strong's and retrieve the preview HTML. Match stored verse references against the fetched results. |
| A3a.2 | Parse each span | Extract the strong= attribute from the target-word span. Compare against the term's strongs_number (both input and resolved form). |
| A3a.3 | Update span_strong_match | UPDATE wa_verse_records SET span_strong_match = 1 where confirmed; span_strong_match = 0 where only sibling/prefix forms found. |
| A3a.4 | Update target_word | UPDATE wa_verse_records SET target_word from the span text for all rows where span_strong_match = 1 and target_word IS NULL. |
| A3a.5 | Write quality flags | If any rows received span_strong_match = 0: write SPAN_FILTER_APPLIED quality flag (id=24). Write SPAN_BACK_POPULATED note flag (id=25) unconditionally — records that A3a has been run for this term. |
| A3a.6 | Update term_fetch_log | INSERT a new term_fetch_log row for this AUDIT_WORD run with verse_count_stored = confirmed count and verse_count_filtered = non-applicable count. |


⚠  A3a does NOT delete verse records. Rows with span_strong_match = 0 are retained as a documented audit trail of what STEP originally returned. They are excluded from all analytical counts and from the working verse set, but they remain visible in the report with clear non-applicable labelling.

## 5.6  Phase 2 Context Design — Forward Reference
Phase 1 stores the reference verse only. The wa_verse_records schema includes two columns reserved for Phase 2:

| Column | Design intent |
|---|---|
| context_before TEXT | One or more verses immediately preceding the reference verse, where the researcher identifies a need for contextual reading. Null for all Phase 1 records. |
| context_after TEXT | One or more verses immediately following the reference verse. Null for all Phase 1 records. |


These columns are populated selectively in Phase 2 by researcher judgment — they cannot be anticipated in advance and apply only to specific verses where surrounding context is needed for meaningful analysis. The need arises from the research, not from the data structure. No Phase 2 tooling for populating these columns is specified in this document.
ℹ  The note and claude_output columns already present in wa_verse_records are also reserved for Phase 2 use. note can hold researcher annotations at the verse level. claude_output can hold AI-assisted analysis output for a specific verse. Both are null for all Phase 1 records and are not written by the v9 engine.
Together, context_before, context_after, note, and claude_output give Phase 2 full per-verse enrichment capability without any schema change.


# 6.  GAP_FILL Mode — Stream Architecture
GAP_FILL processes all Pending words in eight sequential streams. Each stream is a complete pass over its input set before the next begins. Streams are independent — a failure in one does not cascade into another.

✔  v4 CHANGE: S3 (VERSE_FETCH) now includes the span filter. Verse records are filtered at fetch time — only span-confirmed verses are passed to S4 for DB_WRITE. Filtered verse counts are recorded in term_fetch_log and in the engine_stream_checkpoint rows_filtered column.

## 6.1  Stream Definitions

| Stream | Name | Input | Writes | Checkpoint |
|---|---|---|---|---|
| S1 | TERM_DISCOVERY | word_registry WHERE phase1_status = Pending AND automation_eligible = 1 | wa_file_index (1 row/word); mti_term_cross_refs (XREF terms); term_fetch_log (classification). Sets phase1_status = In Progress per word. | Per word |
| S2 | VOCAB_FETCH | NEW terms from S1 | term_fetch_log: vocab_status, strongs_resolved, api_warnings per term | Per term |
| S3 | VERSE_FETCH + SPAN FILTER | NEW terms where S2 vocab_status = ok | term_fetch_log: verse_status, verse_count_fetched, verse_count_stored, verse_count_filtered, span_conflict per term. Span-confirmed verse data held in memory for S4. | Per term |
| S4 | DB_WRITE | NEW terms where S2=ok AND S3≠failed | mti_terms; wa_term_inventory; wa_term_related_words; wa_verse_records (span_strong_match=1 rows only). One transaction per word — full rollback on failure. | Per word (transactional) |
| S5 | FLAG_ENGINE | Terms written in S4 | wa_term_phase2_flags (derivable flags); wa_data_quality_flags including SPAN_RESOLUTION_CONFLICT where applicable | Per word |
| S6 | AUDIT | Words where S4–S5 complete | word_run_state (PASS/REVIEW/STOP); word_registry.phase1_status update | Per word |
| S7 | MEANING_PARSER | Words with PASS or REVIEW in S6 | wa_meaning_parsed; wa_meaning_sense; wa_meaning_stem; wa_lsj_parsed; wa_term_inventory.parsed_meaning_id | Per word |
| S8 | FIELD_FILL | Rows where also_spelled IS NULL (Hebrew) OR occurrence_count_qualifier IS NULL | wa_term_inventory: also_spelled, occurrence_count_qualifier. Interactive — researcher provides values or confirms null. | Per term (interactive, resumable) |


## 6.2  Stream Dependencies

| Stream | Depends on | Detail |
|---|---|---|
| S1 | word_registry | Reads phase1_status = Pending. Reads mti_terms for XREF classification. |
| S2 | S1 complete | Reads term_fetch_log for NEW term list. |
| S3 | S2 complete | Reads strongs_resolved from S2 rows. Applies span filter during fetch. Holds span-confirmed verse data in memory. |
| S4 | S2 + S3 complete | Words where S2 or S3 failed are skipped (flagged). Writes only span-confirmed verse records from S3 memory. |
| S5 | S4 complete for word | Can run per-word as soon as S4 commits for that word. |
| S6 | S5 complete for word | Reads all content tables. Requires flag engine to have run. |
| S7 | S6 complete for all words | Single pass after full S6. STOP words excluded unless researcher_approved = 1. |
| S8 | S7 complete | Final interactive step. Runs if any null field-fill values remain. |


## 6.3  Run Control Flags
engine.py --mode=gap                       # full run, all Pending words
engine.py --mode=gap --from=[registry_id]  # fresh sub-run from this word onward
engine.py --mode=gap --resume=[run_id]     # resume a prior interrupted run
engine.py --mode=gap --restart             # discard all checkpoints; fresh full run
engine.py --mode=gap --parallel=[N]        # enable concurrent API calls (S2/S3), N=1–8


| Flag | Definition |
|---|---|
| --from=[registry_id] | Filter: process only words where word_registry.no >= registry_id. Fresh sub-run — new run_id and new checkpoints. Does NOT resume a prior run. |
| --resume=[run_id] | Resume: continues from the last engine_stream_checkpoint position of the specified run. Requires that run to have status PARTIAL or FAILED. |
| --restart | Fresh start: ignores all prior checkpoints. New run_id. Safe — S1's duplicate check prevents double-writing. |
| --parallel=[N] | Concurrent API calls in S2 and S3 with N workers (1–8). Default: 1 (sequential). Enable only after confirming STEP API concurrency tolerance. See Section 6.4. |


## 6.4  API Parallelism Guidance

| Parameter | Guidance |
|---|---|
| Default | Sequential (--parallel=1). ~55 min estimated for 167 words at 1 call/second. |
| Concurrent | N=4 estimated ~15 min if STEP tolerates it. |
| Rate limit handling | On HTTP 429/503: pause all workers; exponential backoff 2s doubling to 60s max; resume at N-1. |
| Pre-run test | 10-call test sequence before any concurrent run. If mean response > 3s or any 429: disable concurrency for this run. |
| Tool builder mandate | Document confirmed safe concurrency limit in step_setup.md during development. |



# 7.  NEW_WORD and AUDIT_WORD Mode Sequences
✔  v4 CHANGE: Multi-part split assessment (step N5 in v3) has been removed entirely. The multi-part mechanism was a context-window artefact of the manual pipeline — it does not apply to the automation engine. See Section 7.3 for the legacy data note. Step numbering has been updated accordingly.

## 7.1  New Word Registration
engine.py --register --word=[word] --source=[source_list] --category=[hint]
• Validates: no duplicate word label; lowercase and hyphens only; source_list non-empty.
• Queries MAX(no) FROM word_registry — live, never from memory.
• Inserts word_registry row: no = MAX+1, phase1_status = Pending, automation_eligible = 1.

## 7.2  NEW_WORD Mode — Step Sequence

| Step | Action | Detail | STOP / REVIEW condition |
|---|---|---|---|
| N1 | Registry confirmation | Query word_registry WHERE no = [registry_id]. Confirm row, word, automation_eligible = 1. | No row → STOP. phase1_status ≠ Pending → STOP. automation_eligible = 0 → STOP. |
| N2 | Duplicate check | Query wa_file_index WHERE registry_id = [id]. | Existing rows → STOP unless --force set (requires typed "OVERWRITE"). |
| N3 | Term list validation | Validate Strong's format; check internal duplicates; confirm non-empty. | Empty list → STOP. Malformed Strong's → STOP. Duplicates → STOP. |
| N4 | MTI classification | _resolved_strong() per term. Query mti_terms. Classify NEW/XREF. Report to researcher. | PENDING terms → REVIEW gate. Researcher approves before N5. |
| N5 | Schema version check | Confirm schema_version matches engine expected_version. | Mismatch → STOP. Run --migrate first. |
| N6 | Pre-write lock | SET word_registry.last_automation_run = "IN_PROGRESS". | Sentinel already set → STOP. Resolve with --clear-lock. |
| — PRE-TRANSACTION — | API assembly (N7–N8) | All network I/O completes before the database transaction opens. Results held in memory. | — |
| N7 | Fetch vocab | get_vocab_info() per NEW term. Log to term_fetch_log. | All failed → STOP (clear sentinel). Partial → REVIEW. |
| N8 | Fetch verses + span filter | get_verse_records() per NEW term. Apply span filter: retain only span_strong_match = 1 verses. Log counts to term_fetch_log. | Total failure + no meanings → STOP (clear sentinel). Partial → REVIEW. All filtered (span conflict) → REVIEW + SPAN_RESOLUTION_CONFLICT flag queued. |
| — OPEN TRANSACTION — | DB writes (N9–N15) | All inserts are a single atomic SQLite transaction. Full rollback on any failure. | — |
| N9 | Write wa_file_index | INSERT one row. id = MAX(id)+1. testament_coverage = null. | Failure → STOP + rollback. |
| N10 | Write mti_terms | INSERT per NEW term. status = extracted. word_data_reference = wa_file_index.id. | Failure → STOP + rollback. |
| N11 | Write term inventory + related words | INSERT wa_term_inventory, wa_term_related_words per NEW term. | Failure → STOP + rollback. |
| N12 | Write verse records | INSERT wa_verse_records per NEW term — span_strong_match = 1 rows only. Set span_strong_match = 1, target_word, context_before = null, context_after = null. | Failure → STOP + rollback. |
| N13 | Write XREF cross-refs | INSERT mti_term_cross_refs per XREF term. conflict_action IGNORE. | Non-IGNORE failure → STOP + rollback. |
| — COMMIT TRANSACTION — |  | On rollback: IN_PROGRESS sentinel persists for diagnostic clarity; cleared at N19. | — |
| N14 | Derive testament_coverage | Derive OT/NT/both from stored verse records. UPDATE wa_file_index. | No confirmed verses for all terms → REVIEW. |
| N15 | Run meaning parser | Parse meaning per NEW term. INSERT wa_meaning_* tables. SET parsed_meaning_id. | Parser failure → REVIEW. Data load not rolled back. |
| N16 | Run flag engine | Evaluate derivable flags. INSERT wa_term_phase2_flags, wa_data_quality_flags (including SPAN_RESOLUTION_CONFLICT for any span-conflict terms). | Flag errors → REVIEW. |
| N17 | Run audit | Execute all WR-xx checks. Write word_run_state. | STOP result → researcher approval before N18. |
| N18 | Field-fill | Present null also_spelled (Hebrew) and null occurrence_count_qualifier (all) terms. Accept input or confirm null. | Interactive. Cannot fail. |
| N19 | Update word_registry | SET phase1_status, counts, last_automation_run, automation_run_id. Clear IN_PROGRESS sentinel. | REVIEW if fails. |


## 7.3  Multi-Part Legacy Note
§  The wa_file_index table contains part_number, total_parts, is_split, and root_families_in_prior_parts columns. These were populated by the manual v4–v8 pipeline for 14 words that were split across 2–3 parts due to Claude context-window limits. In the automation engine these columns have no operational purpose — the engine processes all terms for a word in a single run and writes a single wa_file_index row with is_split = 0 and part_number / total_parts / root_families_in_prior_parts = null. The columns are retained in the schema and remain read-only — AUDIT_WORD mode reads them for context but never updates them. The word overview report displays multi-part information for existing split words.

## 7.4  Lock Management
engine.py --clear-lock --registry=[id]
→ Prints lock value and timestamp. Requires typed "CLEAR".
→ Sets word_registry.last_automation_run = NULL.
→ Logs clear in engine_run_log with mode = LOCK_CLEAR.
⚠  If the IN_PROGRESS sentinel has been set for more than 2 hours, the engine warns on the next invocation: "Lock may be stale — use --clear-lock if no run is active."

## 7.5  AUDIT_WORD Mode — Step Sequence

| Step | Action | Detail | STOP / REVIEW condition |
|---|---|---|---|
| A1 | Explicit invocation | engine.py --mode=audit --registry=[id]. Requires typed "CONFIRM". | No confirmation → abort. |
| A2 | Load existing records | Read all rows from content tables for this registry_id. | No existing records → redirect to NEW_WORD. |
| A3 | Re-fetch from STEP | Re-call get_vocab_info() and get_verse_records() per existing term. All API calls complete before any DB write. | API unavailable → STOP. |
| A3a | Span back-population | Re-fetch preview HTML for ALL existing verse records for this registry regardless of prior span_strong_match value. Parse each span. UPDATE span_strong_match (1 or 0) and target_word. Write SPAN_FILTER_APPLIED (id=24) if any rows receive 0. Write SPAN_BACK_POPULATED (id=25) unconditionally. See Section 5.5. | Partial fetch failure → REVIEW (update rows that were successfully re-fetched; log unresolved rows). |
| A4 | Produce gap report | Categorise: MISSING / STALE / NEW_TERM / ORPHAN / API_ONLY. | Present to researcher before writes. |
| A5 | Researcher review gate | Researcher approves gap categories to fill. | None → exit cleanly. Partial → fill only approved. |
| A6 | Fill gaps | UPDATE null fields; INSERT missing verses (with span filter applied); INSERT missing NEW_TERMs. Never DELETE. | Failure → STOP + rollback this step only. |
| A7 | Run meaning parser | Re-parse all terms. UPDATE wa_meaning_* tables. | Mismatch → REVIEW with diff. |
| A8 | Field-fill | Present null also_spelled and occurrence_count_qualifier. Accept input or confirm null. | Interactive. Cannot fail. |
| A9 | Run audit | Execute WR-xx checks. Write word_run_state. | STOP → researcher approval. |
| A10 | Update word_registry | Update last_automation_run, automation_run_id, notes. | Should not fail. |



# 8.  Audit Framework
Every mode runs the same predefined audit after all writes complete. Results are deterministic — the same database state always produces the same result.

## 8.1  Audit Checks

| Check | Class | Condition | Action if failed |
|---|---|---|---|
| WR-01  wa_file_index present | STOP | COUNT(wa_file_index WHERE registry_id = [id]) >= 1 | STOP — no anchor row. |
| WR-02  wa_file_index single row | STOP | COUNT = exactly 1 for v9 words (is_split = 0). Legacy split words exempt from this check. | STOP — duplicate anchor rows for a non-split word. |
| WR-03  Term count non-zero | REVIEW | COUNT(wa_term_inventory WHERE file_id = [id]) > 0 | REVIEW — all terms may be XREF. |
| WR-04  All term_ids in mti_terms | STOP | Every term_id in wa_term_inventory has mti_terms row with status = extracted | STOP — orphaned inventory rows. |
| WR-05  No ID gaps within word's rows | STOP | IDs for this word's wa_term_inventory rows form a contiguous range from max_id_at_run_start+1 with no gaps within that range. | STOP — indicates partial write. |
| WR-06  Confirmed verse records present | REVIEW | COUNT(wa_verse_records WHERE file_id = [id] AND (span_strong_match = 1 OR span_strong_match IS NULL)) > 0 | REVIEW — zero confirmed verses for entire word. Check for span conflict across all terms. |
| WR-07  All terms have verses or quality flag | REVIEW | Each wa_term_inventory row: COUNT(verses WHERE span_strong_match = 1) > 0 OR wa_data_quality_flags has NO_VERSES or SPAN_RESOLUTION_CONFLICT | REVIEW — unexpected zero confirmed verses. |
| WR-08  Verse/occurrence ratio | REVIEW | For terms with occurrence_count >= 20: (confirmed_verse_count / occurrence_count) >= 0.15 | REVIEW — possible incomplete fetch or heavy span filtering. |
| WR-09  testament_coverage set | REVIEW | wa_file_index.testament_coverage IS NOT NULL | REVIEW — N14/S4 did not complete or zero confirmed verses. |
| WR-10  Meaning populated or flagged | REVIEW | Each wa_term_inventory row: meaning IS NOT NULL OR wa_data_quality_flags has NO_WORD_ANALYSIS | REVIEW — unexpected null meaning. |
| WR-11  Transliteration populated | STOP | All wa_term_inventory rows have non-null transliteration | STOP — required for downstream analysis. |
| WR-12  Language populated | STOP | All wa_term_inventory rows have language IN (Hebrew, Greek) | STOP — unknown language breaks flag engine. |
| WR-13  Undocumented nulls (API-derivable fields only) | REVIEW | Nullable API-derivable fields that are null have a wa_data_quality_flags row. Excludes: god_as_subject, somatic_link, wa_term_root_family.root_code, mti_term_flags, also_spelled (confirmed null), occurrence_count_qualifier (confirmed null), context_before, context_after (Phase 2 reserved). | REVIEW — undocumented null in API-derivable field. |
| WR-14  XREF terms cross-referenced | REVIEW | All XREF terms have mti_term_cross_refs row for this registry | REVIEW — missing cross-refs. |
| WR-15  No duplicate mti_terms | STOP | mti_terms has exactly one row per strongs_number for owning_registry | STOP — duplicate MTI rows. |
| WR-16  Derivable flags assessed | REVIEW | HIGH_FREQUENCY_ANCHOR, THIN_DATA, SMALL_VERSE_SAMPLE, NO_WORD_ANALYSIS, SPAN_RESOLUTION_CONFLICT candidates all evaluated | REVIEW — flag engine may have failed. |
| WR-17  Fetch warnings reflected | REVIEW | All term_fetch_log warnings for this run have wa_data_quality_flags rows | REVIEW — fetch warnings not reflected. |
| WR-18  Meaning parsed | REVIEW | All NEW terms have wa_meaning_parsed row (parsed_meaning_id IS NOT NULL) | REVIEW — parser did not run or failed. |
| WR-19  Parse warnings documented | REVIEW | wa_meaning_parsed rows with parse_warnings have NOTE quality flag | REVIEW — undocumented parse anomalies. |
| WR-20  Span back-population status | REVIEW | For AUDIT_WORD runs: all wa_verse_records for this word have span_strong_match IS NOT NULL (back-population complete). For NEW_WORD / GAP_FILL: all rows have span_strong_match = 1 (filter applied at fetch time). | REVIEW — some verse records have null span_strong_match. A3a may not have completed. |


## 8.2  Classification Criteria

| Result | Condition | word_registry update | Proceed? |
|---|---|---|---|
| PASS | All STOP checks pass; zero REVIEW checks fail | phase1_status = Complete | Yes |
| REVIEW | All STOP checks pass; ≥1 REVIEW check fails | phase1_status = In Progress | Yes — word usable; researcher notified |
| STOP | ≥1 STOP check fails | phase1_status unchanged | No — researcher must inspect and approve |


## 8.3  Progressive Evaluation
• STOP checks evaluated first. If any fail, all remaining checks still run to give complete context.
• In GAP_FILL mode, STOP words are skipped and counted in words_stopped. The stream continues.
• Audit re-runs after every gap-fill operation and after researcher-approved re-writes.
ℹ  audit_detail in word_run_state records every check ID, its result, and the specific values that caused a failure. Complete picture without querying content tables.


# 9.  Field-Level Mapping

| Table · Column | API / DB source | Default / rule | Notes |
|---|---|---|---|
| wa_term_root_family · root_code | Researcher judgment | null until assigned | DEFERRED. Not written by engine. Expected null for all automation terms. Not flagged by WR-13. |
| mti_term_flags · flag_id | Researcher judgment | Not written by engine | DEFERRED. THEOLOGICAL_ANCHOR only. WR-13 excludes. |
| wa_term_inventory · god_as_subject | Default | 0 | DEFERRED. Next-phase review. |
| wa_term_inventory · somatic_link | Default | 0 | DEFERRED. Next-phase review. |
| wa_term_inventory · also_spelled | Field-fill N18/A8/S8 | null until filled | DEFERRED-INTERACTIVE. wa_term_inventory only — not duplicated in mti_terms. |
| wa_term_inventory · occurrence_count_qualifier | Field-fill N18/A8/S8 | null until filled | DEFERRED-INTERACTIVE. Not available from API. |
| wa_file_index · specification | — | Session A v9 Automation | Constant. |
| wa_file_index · testament_coverage | Derived post-verse write | null | OT/NT/both set after confirmed verse insert (N14/S4 end). |
| wa_file_index · part_number | — | null | Legacy column. Not written by v9 engine. |
| wa_file_index · total_parts | — | null | Legacy column. Not written by v9 engine. |
| wa_file_index · is_split | — | 0 | Written as 0 for all v9 words. |
| wa_file_index · root_families_in_prior_parts | — | null | Legacy column. Not written by v9 engine. |
| word_registry · phase1_input_file | Constant: run_id | run_id value | Engine writes the run_id here. Replaces .md filename convention from prior spec versions. |
| wa_term_inventory · strongs_number | vocab.strong_number | — | Resolved form. H2428 → H2428A. |
| wa_term_inventory · transliteration | vocab.transliteration | STOP if null | Required. WR-11. |
| wa_term_inventory · language | Derived | STOP if null | H-prefix → Hebrew; G-prefix → Greek. WR-12. |
| wa_term_inventory · step_search_gloss | vocab.gloss | — | From vocabInfos[0].stepGloss. |
| wa_term_inventory · word_analysis_gloss | vocab.gloss | — | Same at write. Researcher may update in review. |
| wa_term_inventory · occurrence_count | vocab.occurrence_count | null + DATA_GAP flag | Token count. |
| wa_term_inventory · meaning | vocab.medium_def | null + NO_WORD_ANALYSIS flag | HTML-stripped; newlines preserved. |
| wa_term_inventory · meaning_numbered | Derived | null for Greek | True if medium_def contains 1), 1a) pattern. Hebrew only. |
| wa_term_inventory · lsj_entry | vocab.lsj_entry | null for Hebrew | Greek only. |
| wa_term_inventory · short_def_mounce | vocab.short_def_mounce | null for Hebrew | New column. Greek only. |
| wa_term_inventory · testament | Derived from confirmed verses | null if 0 confirmed verses | OT/NT/both from span_strong_match = 1 rows only. |
| wa_term_inventory · causative_form_present | Derived | 0 | True if medium_def contains Hiphil or Piel. |
| wa_term_inventory · status_note | data.notes | null | step_client warnings for this term. |
| wa_term_inventory · parsed_meaning_id | Meaning parser | null until parser runs | FK to wa_meaning_parsed.id. |
| wa_verse_records · reference | verse_records[i].ref | — | "Gen 31:27" |
| wa_verse_records · verse_text | verse_records[i].esv_text | — | HTML-stripped. |
| wa_verse_records · target_word | Span parse | null if extraction fails | English rendering of target Strong's from span text. |
| wa_verse_records · span_strong_match | Span parse | 1 at write time; null for pre-v9 | 1 = confirmed. 0 = sibling form only (AUDIT back-population). Null = pre-v9 not yet assessed. |
| wa_verse_records · context_before | Phase 2 reserved | null | Not written in Phase 1. See Section 5.6. |
| wa_verse_records · context_after | Phase 2 reserved | null | Not written in Phase 1. See Section 5.6. |
| wa_verse_records · note | Phase 2 reserved | null | Not written in Phase 1. Available for researcher annotation. |
| wa_verse_records · claude_output | Phase 2 reserved | null | Not written in Phase 1. Available for AI-assisted verse analysis. |
| wa_verse_records · testament | verse_records[i].testament | — | From book_code vs NT_BOOKS. |
| wa_verse_records · book_id | DB lookup | STOP if not found | SELECT book_id FROM book_code_variants WHERE code = book_code. |
| wa_verse_records · chapter | verse_records[i].chapter | — | Integer. Single-chapter books: always 1. |
| wa_verse_records · verse_num | verse_records[i].verse_num | — | Integer. |
| wa_verse_records · translation | — | ESV | Constant. |
| mti_terms · status | — | extracted | Always. |
| mti_terms · word_data_reference | wa_file_index.id | — | Pre-assigned integer. |
| mti_terms · extraction_date | Run date | — | ISO date. |
| mti_terms · strongs_reconciled | Logic | 0 | 1 if resolved strongs_number differs from input. |


Colour coding: white/grey = standard engine fields; blue = Phase 2 reserved columns (null in Phase 1); purple = legacy part columns (retained read-only, not written by engine); amber default cell = field not available from API.


# 10.  Meaning Parsing Schema
Four new tables parse wa_term_inventory.meaning and lsj_entry into structured, queryable form. The parser is version-tagged and runs independently of the main data load.

## 10.1  wa_meaning_parsed — Root Parse Record

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| term_inv_id | INTEGER | FK | References wa_term_inventory.id — 1:1 |
| strongs_number | TEXT |  | Denormalised for query performance |
| language | TEXT |  | Hebrew or Greek |
| top_sense_count | INTEGER |  | Count of top-level numbered senses |
| stem_count | INTEGER |  | Count of distinct Hebrew stem labels. 0 for Greek or prose-only. |
| has_causative_stem | INTEGER |  | 1 if Hiphil or Piel present. |
| has_domain_tags | INTEGER |  | 1 if any sense node has domain_tag assigned. |
| parsed_at | TEXT |  | ISO datetime. |
| parse_version | TEXT |  | Parser version string. |
| parse_warnings | TEXT |  | JSON array of warnings; null if clean. |


## 10.2  wa_meaning_sense — Sense Tree Nodes

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| parsed_meaning_id | INTEGER | FK | References wa_meaning_parsed.id |
| level_code | TEXT |  | Outline prefix: 1, 1a, 1a1, 1a1f1. |
| level_depth | INTEGER |  | Depth. Derived: strip digits from level_code, count remaining chars + 1. |
| parent_level_code | TEXT |  | Derived by truncating last alphanumeric segment. Null for depth 1. |
| sense_text | TEXT |  | Text stripped of level prefix and stem label. |
| is_stem_label | INTEGER |  | 1 if node is purely a stem label: (Qal), (Hiphil) etc. |
| stem_label | TEXT |  | Stem name if is_stem_label = 1. |
| domain_tag | TEXT |  | Researcher-assigned domain tag. Null by default. |
| sort_order | INTEGER |  | Position in original text order. |


## 10.3  wa_meaning_stem — Hebrew Stem Records

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| parsed_meaning_id | INTEGER | FK | References wa_meaning_parsed.id |
| stem_name | TEXT |  | Qal/Niphal/Piel/Pual/Hiphil/Hophal/Hitpael/Polel/Pulal |
| stem_type | TEXT |  | simple/causative/reflexive/passive/other |
| sense_count | INTEGER |  | Count of wa_meaning_sense rows under this stem. |
| top_sense_text | TEXT |  | Primary gloss for this stem. |


## 10.4  wa_lsj_parsed — Structured LSJ Entry (Greek)

| Column | Type | Key | Purpose |
|---|---|---|---|
| id | INTEGER | PK | Auto-assigned |
| term_inv_id | INTEGER | FK | References wa_term_inventory.id |
| raw_lsj | TEXT |  | Full LSJ text (denormalised) |
| lsj_gloss | TEXT |  | Primary gloss. |
| lsj_domains | TEXT |  | JSON array: LXX, NT, 1st c.AD etc. |
| lsj_philosophical_note | TEXT |  | Plato, Aristotle etc. Null if absent. |
| lsj_etymology_note | TEXT |  | Null if absent. |
| lsj_cognate_forms | TEXT |  | JSON array. |
| parsed_at | TEXT |  | ISO datetime. |
| parse_version | TEXT |  | Parser version. |


## 10.5  Parsing Logic
Hebrew numbered: Regex per line. level_code = token before ")". Parent = algorithmic truncation. Stem labels detected against canonical list.
Hebrew prose: Single sense node at level_code = "1". parse_warnings = ["PROSE_ONLY"].
Greek prose: Semicolon-split. Each clause = one top-level node.
LSJ: First segment = lsj_gloss. Bracketed abbreviations → domains. Philosopher names → philosophical_note. Etymology keywords → etymology_note.
ℹ  Re-parse: engine.py --reparse-meanings [--registry=[id] | --all]. Only touches parsing tables and parsed_meaning_id — no content data affected.


# 11.  Word Overview Report
engine.py --report --registry=[id] [--format=html|json]


| Section | Source tables | Content |
|---|---|---|
| Word header | word_registry, engine_run_log | Registry number, word, source list, phase1_status, last run, term count, confirmed verse count. |
| Run history | engine_run_log, word_run_state | All runs: mode, date, outcome, terms/verses written, verses filtered, audit result. |
| Term inventory | wa_term_inventory, wa_file_index | One row per term: Strong's, transliteration, language, gloss, occurrence count, confirmed verse count, filtered verse count, testament. XREF = blue; STOP flags = red. |
| XREF summary | mti_term_cross_refs, mti_terms | XREF terms with owning registry and word. |
| Verse counts | wa_verse_records | Per term: confirmed (span_strong_match=1), filtered (span_strong_match=0), unassessed (null). Span conflict terms highlighted. |
| Phase 2 flags | wa_term_phase2_flags, phase2_flag_types | Matrix: derivable flags set vs judgment flags (greyed — deferred). |
| Quality flags | wa_data_quality_flags, wa_quality_flag_types | All flags grouped by flag_group. SPAN_RESOLUTION_CONFLICT and SPAN_FILTER_APPLIED highlighted. |
| Root families | wa_term_root_family | Root family per term. Null shown as grey (expected gap — deferred). |
| Gaps section | wa_term_inventory, wa_data_quality_flags | Null fields per term. Red = undocumented. Amber = documented. Grey = intentionally deferred. Blue = Phase 2 reserved (context_before, context_after, note, claude_output). |
| Audit status | word_run_state | Most recent audit result with per-check detail. |
| Meaning summary | wa_meaning_parsed, wa_meaning_sense, wa_meaning_stem | Sense count, stem count, causative stem. Collapsible Hebrew tree. Greek LSJ domains. |
| Verse coverage | wa_verse_records, books | Confirmed verse count by testament and book. Full verse table with target_word. Filtered/unassessed verses shown with strikethrough or amber styling. |
| Related words | wa_term_related_words | Per term. |
| Cross-registry links | wa_cross_registry_links, word_registry, wa_crosslink_type | Linked words with type and note. |
| MTI status | mti_terms, mti_term_flags | Status, word_data_reference, THEOLOGICAL_ANCHOR if set. |
| Field-fill status | wa_term_inventory | also_spelled and occurrence_count_qualifier: set / confirmed null / pending. |
| Multi-part note | wa_file_index | For legacy split words: part count, part_number, root_families_in_prior_parts per part. Not shown for v9 single-part words. |
| Phase 2 context slots | wa_verse_records | Table of verses where context_before or context_after is populated. Empty in Phase 1. Shown as "reserved — no Phase 2 context added yet." |


## 11.1  Gap Colour Coding

| Colour | Meaning |
|---|---|
| Red | Null AND no quality flag. Unacknowledged gap. |
| Amber | Null AND quality flag documents it. |
| Grey | Intentionally deferred: root family, god_as_subject, somatic_link, mti_term_flags, confirmed nulls. |
| Blue | Phase 2 reserved: context_before, context_after, note, claude_output. Not a gap. |
| Strikethrough / light grey text | Verse record with span_strong_match = 0. Not applicable to this term. |
| Green | All STOP checks pass; no unexplained nulls. |



# 12.  Schema Migration
✔  v4 CHANGE: Migration M05 now adds four wa_verse_records columns (target_word, span_strong_match, context_before, context_after) in one step. The migration sequence is M01–M10 (ten steps, unchanged count — M05 now covers four columns instead of one). Three new wa_quality_flag_types rows (ids 23–25) are added in M02 as reference data inserts.

## 12.1  Current Schema Baseline (v2.2 — reference values only)
⚠  Row counts below are point-in-time reference values for orientation only. Migration tooling must always query live MAX(id) values — never use these figures in code.

| Table | Rows (approx.) | Description |
|---|---|---|
| book_code_variants | (ref) | OSIS and abbreviation variants → books.id |
| books | 66 | Canon books |
| mti_term_cross_refs | (data) | XREF cross-references |
| mti_term_flags | (data) | Junction: mti_terms ↔ THEOLOGICAL_ANCHOR |
| mti_terms | ~700 | Master Term Index |
| phase2_flag_types | 25 | Analytical flag definitions |
| sources | (ref) | Bibliographic sources |
| themes | (ref) | Theme taxonomy |
| wa_cross_registry_links | (data) | Cross-word relationships |
| wa_crosslink_type | 7 | Link type definitions |
| wa_data_quality_flags | (data) | Per-term quality issues |
| wa_file_index | 54 | Per-word anchor rows |
| wa_quality_flag_types | 22 → 25 after M02 | Quality flag type definitions (3 new rows added in M02) |
| wa_term_inventory | ~715 | Core term records |
| wa_term_phase2_flags | (data) | Junction: terms ↔ phase 2 flags |
| wa_term_related_words | (data) | Related word entries |
| wa_term_root_family | ~640 | Root family assignments |
| wa_verse_records | ~12,900 | Verse records per term |
| word_registry | 200 | Master word registry |


## 12.2  Migration Sequence (v2.2 → v3.0)

| Ref | Migration | SQL summary |
|---|---|---|
| M01 | Create schema_version | CREATE TABLE schema_version. INSERT one row: version_code = "2.2.0". |
| M02 | Create control tables + reference data | CREATE TABLE engine_run_log; engine_stream_checkpoint; word_run_state; term_fetch_log. INSERT INTO wa_quality_flag_types: SPAN_RESOLUTION_CONFLICT (id=23, DATA_COVERAGE); SPAN_FILTER_APPLIED (id=24, DATA_COVERAGE); SPAN_BACK_POPULATED (id=25, NOTE). |
| M03 | Extend word_registry | ALTER TABLE word_registry ADD COLUMN automation_eligible INTEGER DEFAULT 1; last_automation_run TEXT; automation_run_id TEXT; phase1_term_count INTEGER; phase1_verse_count INTEGER. |
| M04 | Extend wa_term_inventory | ALTER TABLE wa_term_inventory ADD COLUMN short_def_mounce TEXT; parsed_meaning_id INTEGER. |
| M05 | Extend wa_verse_records | ALTER TABLE wa_verse_records ADD COLUMN target_word TEXT; span_strong_match INTEGER; context_before TEXT; context_after TEXT. |
| M06 | Create wa_meaning_parsed | CREATE TABLE wa_meaning_parsed. CREATE INDEX idx_meaning_parsed_term_inv. |
| M07 | Create wa_meaning_sense | CREATE TABLE wa_meaning_sense. CREATE INDEX idx_meaning_sense_parsed; idx_meaning_sense_level. |
| M08 | Create wa_meaning_stem | CREATE TABLE wa_meaning_stem. CREATE INDEX idx_meaning_stem_parsed. |
| M09 | Create wa_lsj_parsed | CREATE TABLE wa_lsj_parsed. CREATE INDEX idx_lsj_parsed_term. |
| M10 | Update schema_version | UPDATE schema_version SET version_code = "3.0.0", applied_at = [now], migration_history = [full JSON array]. |


## 12.3  Migration Tool Requirements
engine.py --migrate              # apply all pending migrations
engine.py --migrate --dry-run    # show SQL without executing
engine.py --migrate --to=M05     # apply up to M05 only
engine.py --db-status            # show current version and pending migrations
• Each migration runs inside a SQLite transaction — fully committed or fully rolled back.
• Each migration is idempotent — checks for column/table existence before ALTER/CREATE.
• Updates migration_history JSON on success.
⚠  Tool builder mandate: MIGRATION.md must contain complete CREATE TABLE DDL for all 28 tables in v3.0, all ALTER TABLE statements, all indexes, all M02 reference data INSERTs, and rollback procedures per migration. Commit to git.


# 13.  Disaster Recovery, Backup, and Safeguarding
## 13.1  Database Risk Profile

| Characteristic | Detail |
|---|---|
| Current size | ~5.4 MB (baseline). Projected at completion: ~30 MB. |
| Growth rate | ~170 KB per word average. |
| Data uniqueness | Irreplaceable. STEP data re-fetchable; MTI classifications, quality flags, researcher annotations, audit history, root family assignments cannot be recovered from external sources. |
| Criticality | HIGH. Loss without backup requires re-running all completed words from scratch. |
| SQLite safety | WAL mode provides crash safety. Partial transactions roll back automatically on restart. |


## 13.2  Backup Requirements

| Type | Frequency | Requirements |
|---|---|---|
| Pre-run | Every invocation | Engine copies database to backups/bible_research_backup_YYYYMMDD_HHMMss_[run_id].db before any writes. Run aborts if backup fails. |
| Post-run | COMPLETE or PARTIAL outcome | Copy final state to backups/bible_research_YYYYMMDD_[run_id]_post.db. |
| Pre-migration | Before any --migrate | Permanent. backups/bible_research_pre_migration_v[version].db. |
| Synology sync | Ongoing | The /backups/ directory is within the researcher's Synology sync scope. |
| Manual checkpoint | Researcher-initiated | engine.py --backup [--label=[description]]. |

• Pre-run backups: keep 10 most recent. Auto-delete older.
• Post-run: rolling 30-day.
• Pre-migration and manual: permanent.
• /backups/ in .gitignore. Never commit backup files.

## 13.3  Recovery Procedures
Stale lock: engine.py --clear-lock --registry=[id]
Interrupted run: engine.py --mode=gap --resume=[run_id]. For NEW_WORD: --clear-lock then re-run.
Corrupt database:
sqlite3 bible_research.db "PRAGMA integrity_check;"
cp backups/bible_research_backup_[timestamp].db bible_research.db
engine.py --mode=gap --from=[last_good_registry_id]
Failed migration: Transaction rolls back automatically. Restore from pre-migration backup. Fix script. Re-run --migrate.

## 13.4  Safeguarding Rules

| Ref | Safeguard | Requirement |
|---|---|---|
| SG-01 | Pre-run backup | Engine creates backup before any write. Run aborts if backup fails. |
| SG-02 | Schema version check | Engine reads schema_version at startup. Aborts on mismatch. |
| SG-03 | Concurrent run detection | IN_PROGRESS sentinel. Stale lock (>2 hours) triggers warning. Resolved by --clear-lock. |
| SG-04 | Transaction isolation | All inserts for one word in single SQLite transaction. Automatic rollback on failure. |
| SG-05 | No DELETE in engine code | Engine source must not contain DELETE FROM on content tables. |
| SG-06 | No hardcoded IDs | Engine queries MAX(id) live immediately before every explicit-id INSERT. |
| SG-07 | No hardcoded registry numbers | Always read from word_registry via live query. |
| SG-08 | AUDIT_WORD confirmation | Requires typed "CONFIRM" before any writes. |
| SG-09 | --force / --overwrite gating | Requires typed "OVERWRITE". Logged in engine_run_log. |
| SG-10 | Read-only mode | engine.py --mode=readonly produces report with no write lock. |
| SG-11 | Dry-run mode | All write commands accept --dry-run. No DB writes; all logic including API calls executes. |
| SG-12 | WAL mode | Engine enables PRAGMA journal_mode=WAL at startup. |
| SG-13 | Integrity check on restore | Engine runs PRAGMA integrity_check after any backup restore. Aborts if check fails. |


## 13.5  Version Control
• Engine source under git from first commit.
• bible_research.db and /backups/ in .gitignore.
• MIGRATION.md committed and kept in sync.
• step_setup.md (STEP API, confirmed concurrency limits) committed and maintained.
• Git tags at schema boundaries: git tag schema-v3.0.0.
• Engine location: engine/ package at project root. Entry point engine/engine.py.


# 14.  Complete Schema Summary (v3.0)
28 tables. White/grey = unchanged; amber = amended; blue = new; purple = legacy read-only (part columns in wa_file_index).


| Table | Category | Mode | Status |
|---|---|---|---|
| book_code_variants | Reference | — | Unchanged |
| books | Reference | — | Unchanged |
| mti_term_cross_refs | Content | All modes | Unchanged |
| mti_term_flags | Content | Researcher (deferred) | Unchanged — written by researcher in next phase only |
| mti_terms | Content | All modes | Unchanged (M04 also_spelled removal confirmed in v3; no further change) |
| phase2_flag_types | Reference | — | Unchanged |
| sources | Reference | — | Unchanged |
| themes | Reference | — | Unchanged |
| wa_cross_registry_links | Content | Researcher | Unchanged |
| wa_crosslink_type | Reference | — | Unchanged |
| wa_data_quality_flags | Content | Engine | Unchanged structure; 3 new reference rows in wa_quality_flag_types |
| wa_file_index | Content | All modes | Unchanged structure; part columns are legacy read-only for v9 engine |
| wa_quality_flag_types | Reference | — | AMENDED — 3 new rows: SPAN_RESOLUTION_CONFLICT (23), SPAN_FILTER_APPLIED (24), SPAN_BACK_POPULATED (25) |
| wa_term_inventory | Content | All modes | AMENDED — 2 new columns: short_def_mounce, parsed_meaning_id |
| wa_term_phase2_flags | Content | Engine (derivable) | Unchanged |
| wa_term_related_words | Content | Engine | Unchanged |
| wa_term_root_family | Content | Researcher (deferred) | Unchanged — populated by researcher, not engine |
| wa_verse_records | Content | Engine | AMENDED — 4 new columns: target_word, span_strong_match, context_before, context_after |
| word_registry | Content | All modes | AMENDED — 5 new columns: automation_eligible, last_automation_run, automation_run_id, phase1_term_count, phase1_verse_count |
| engine_run_log | Control | All modes | NEW — Section 3.1 |
| engine_stream_checkpoint | Control | GAP_FILL | NEW — Section 3.2 |
| word_run_state | Control | All modes | NEW — Section 3.3 |
| term_fetch_log | Control | All modes | NEW — Section 3.4 |
| schema_version | Control | Migration | NEW — Section 3.5 |
| wa_meaning_parsed | Parsing | Meaning parser | NEW — Section 10.1 |
| wa_meaning_sense | Parsing | Meaning parser | NEW — Section 10.2 |
| wa_meaning_stem | Parsing | Meaning parser | NEW — Section 10.3 |
| wa_lsj_parsed | Parsing | Meaning parser | NEW — Section 10.4 |



# 15.  Approval Checklist — v4 Final

## 15.1  v3 → v4 Changes — Confirm Resolution

| Ref | Change | Confirmation required |
|---|---|---|
| v4-A | Multi-part removed | Step N5 (split assessment) removed from NEW_WORD. Multi-part mechanism confirmed as context-window artefact not applicable to automation engine. wa_file_index part columns retained as legacy read-only. Section 7.3. |
| v4-B | Span filter added | Option B confirmed: only span-confirmed verses stored. span_strong_match = 1 at write time. Verses where queried Strong's absent from span are discarded, not stored. Section 5.2. |
| v4-C | AUDIT back-population | Sub-step A3a added to AUDIT_WORD: re-fetches preview HTML for ALL existing verse records (not just inflated-count terms), sets span_strong_match, does not delete rows. Section 5.5. |
| v4-D | Phase 2 context columns | context_before and context_after added to wa_verse_records as Phase 2 reserved columns. Null in all Phase 1 records. note and claude_output also documented as Phase 2 reserved. Section 5.6. |
| v4-E | New quality flags | SPAN_RESOLUTION_CONFLICT (id=23), SPAN_FILTER_APPLIED (id=24), SPAN_BACK_POPULATED (id=25) added to wa_quality_flag_types in M02. Section 4. |
| v4-F | WR-20 added | New audit check: span_strong_match completeness — all verse records have non-null span_strong_match after fetch (v9) or back-population (AUDIT). Section 8.1. |
| v4-G | M05 extended | wa_verse_records migration now adds four columns in one step: target_word, span_strong_match, context_before, context_after. Section 12.2. |


## 15.2  All Prior Items — Carried Forward Confirmed
□  All 14 v2→v3 review items remain resolved (see v3 checklist §14.1).
□  Section 8 audit checks WR-01 through WR-20 confirmed.
□  Migration sequence M01–M10 confirmed.
□  Safeguarding rules SG-01 through SG-13 confirmed as mandatory.
□  Judgment-deferred fields confirmed: wa_term_root_family, god_as_subject, somatic_link, mti_term_flags, all 25 phase2_flag_types judgment flags.
□  STEP server confirmed at localhost:8989. step_client.py confirmed as API base.
□  Engine package confirmed at engine/ project root.


| Document status | v4 FINAL — ready for researcher sign-off. Upon sign-off this document is the coding specification. |
|---|---|

