# Session A v9 — Architecture Specification Review
**Document reviewed:** `Session-A-v9-Architecture-v2-DRAFT-20260318.docx`  
**Review date:** 2026-03-18  
**Reviewer:** GitHub Copilot (Claude Sonnet 4.6)  
**Status:** Pre-implementation review — for researcher sign-off

---

## Summary

The specification is thorough and well-conceived. The stream architecture, transaction design, audit framework, and safeguarding rules are all sound. Four items are critical and should be resolved in the document before coding begins. Five items are important and should be addressed in a brief addendum. Five minor items can be handled as clarifying notes during implementation.

---

## Critical — resolve before coding begins

### 1. API calls inside the N7–N13 transaction (§6.2)

Steps N9 (vocab fetch) and N10 (verse fetch) are both network API calls, but they sit inside the "single atomic transaction" spanning N7–N13. This is architecturally wrong: network I/O must never be executed inside an open database transaction. If an API call takes 20 seconds or hangs, a write lock is held for the full duration. A network timeout or STEP server hiccup would force a full rollback of already-written `wa_file_index` and `mti_terms` rows.

**Recommended fix:** Restructure into two explicit phases:

- **Pre-transaction (N1–N10):** All validation, classification, API calls, and data assembly. No DB writes except the IN_PROGRESS sentinel at N6.
- **Transaction (N11–N13):** Write `wa_file_index`, `mti_terms`, `wa_term_inventory`, `wa_verse_records` atomically in one commit.

This also simplifies the "STOP + full rollback to N7" clauses in N9 and N10 — there is nothing to roll back yet at those steps.

---

### 2. Multi-part word handling not specified

The schema has `part_number`, `total_parts`, `is_split`, and `root_families_in_prior_parts` in `wa_file_index`. Existing words run up to 3 parts (e.g. strength, flesh). The spec describes NEW_WORD mode as writing "one row" to `wa_file_index` with no mention of splits.

Questions requiring explicit rulings:

- Is each part a separate engine invocation (`--part=1`, `--part=2`)? Or does the engine handle splits automatically?
- What is the split threshold, and is it configurable? (Session A v8 used 12+ new terms as the threshold.)
- How is `root_families_in_prior_parts` populated — from the previous part's `wa_term_root_family` rows at runtime?
- In GAP_FILL, how are multi-part words identified and sequenced? A word with three intended parts but only one `wa_file_index` row would be ambiguous at S1.

If multi-part words are initially deferred to manual handling or AUDIT_WORD, the spec must say so explicitly.

---

### 3. `wa_term_root_family` absent from all write streams

This table exists, holds `root_code` per term, and is populated in every existing Phase 2 patch. It is not mentioned in S4, N11, or Section 8's field mapping. The engine must take an explicit position:

- If root family assignment is **fully deferred to researcher** (like `god_as_subject`), it should be listed alongside the other judgment-deferred fields in Section 8, and audit check WR-13 (undocumented nulls) should make clear that missing root data is a documented, expected gap — not an error.
- If root family assignment can be **partially automated** (e.g. by grouping terms via `rawRelatedNumbers`), that logic needs to be specified.

Either way, an explicit ruling is needed. The current silence will likely cause WR-13 to fire for every term.

---

### 4. `also_spelled` appears in both `wa_term_inventory` and `mti_terms` (M04)

`wa_term_inventory.also_spelled` already exists in the live schema and is populated by the current patch workflow. Migration M04 proposes adding `mti_terms.also_spelled` as a new column. Section 8 covers `wa_term_inventory.also_spelled` but has no entry for `mti_terms.also_spelled`.

Questions:
- Are both columns meant to hold the same value? If yes, why duplicate?
- If the values differ, what is the distinction — and which one is authoritative?
- The S8 / N17 / A8 field-fill steps refer to only one. Which table is being written?

**Recommended resolution:** Either remove M04 and keep `also_spelled` solely in `wa_term_inventory`, or define a clear semantic distinction between the two columns in the migration document.

---

## Important — resolve before coding begins

### 5. `--from=[id]` flag undefined

Section 12.4 (recovery procedure) uses `engine.py --mode=gap --from=[registry_id]` but this parameter is never defined in Section 2 (Execution Modes) or Section 5 (GAP_FILL architecture). Needs a formal definition: does it mean "process only words with `no` ≥ this value", or "resume the prior run starting from the next unprocessed word after this registry number"? Should appear in Section 5.3 alongside `--resume` and `--restart`.

---

### 6. No mechanism to clear the IN_PROGRESS sentinel

SG-03 sets `word_registry.last_automation_run = 'IN_PROGRESS'` at N6 and clears it at N18. If the process is killed between those steps, the sentinel persists. On the next invocation, SG-03 correctly detects it and aborts — but there is no specified command to resolve this without manually editing the database.

**Recommended addition:** `engine.py --clear-lock --registry=[id]` — prints the lock value and requires typed confirmation before clearing. Should be listed in Section 6 and Section 12.4 as a standard recovery step.

---

### 7. `occurrence_count_qualifier` absent from S8 / N17 / A8

D4 explicitly resolves: *"occurrence_count_qualifier: same steps plus AUDIT_WORD gap-fill."* But the S8 stream description in Section 5.1 specifies only `wa_term_inventory rows where also_spelled IS NULL AND language = Hebrew`. Steps N17 and A8 in Section 6 also mention only `also_spelled`. The `occurrence_count_qualifier` field-fill must be added to all three descriptions to match the D4 resolution.

---

### 8. No intermediate `phase1_status` during GAP_FILL streaming

`word_registry.phase1_status` has values: `Pending`, `In Progress`, `Complete`. In GAP_FILL mode, S1 writes `wa_file_index` for a word, but S6 is where the status update happens — potentially many words and several minutes later. During that interval, `phase1_status` is still `Pending` even though data is being written, creating a misleading state.

**Recommended addition:** S1 should update `phase1_status = 'In Progress'` when it writes `wa_file_index`. S6 then sets it to `Complete` (PASS) or leaves it at `In Progress` (STOP). This also clarifies which words are mid-flight for the `--resume` logic.

---

### 9. WR-05 ID gap check scope too broad

*"All explicit IDs for this `file_id` are sequential with no gaps."* Since the engine uses explicit `MAX(id)+1` IDs (not `AUTOINCREMENT`), rolled-back transactions do not leave gaps — the next run re-queries `MAX(id)` and reuses the same number. However, a global sequential check would false-alarm whenever two different words are written in the same run (IDs for word A and word B are interleaved from `MAX(id)` queries, not globally sequential).

**Recommended rewording:** *"IDs assigned for this `file_id` form a contiguous range starting from `max_id_at_run_start + 1` with no gaps within the range."* This scopes the check correctly to one word's set of inserted rows.

---

## Minor — can be addressed during implementation

### 10. Section 11.1 baseline row counts are already stale

`wa_verse_records` is listed as 12,877 (it is now 12,878 after the strength import this morning); `mti_terms` is shown as 698 (now 713). The spec should add a note that these figures are point-in-time reference values for orientation only. The migration tooling must query live `MAX(id)` values — never use the spec's numbers.

### 11. `mti_term_flags` (THEOLOGICAL_ANCHOR) omitted from Section 8 mapping

Every existing Phase 2 patch includes a `mti_term_flags_insert` block for `THEOLOGICAL_ANCHOR` terms. This table appears in the §13 schema summary as "unchanged" but is absent from Section 8's field-level mapping. It should be explicitly listed as a judgment-deferred field — the engine never writes it; the researcher sets it in a downstream review phase.

### 12. `wa_file_index.root_families_in_prior_parts` not in Section 8

This column is populated in multi-part patches to maintain root-family consistency across parts and is a key cross-part coherence tool. It should appear in the field mapping. For single-part words the engine can write `null`; for multi-part, the ruling (researcher-provided vs. engine-derived) should be stated.

### 13. `word_registry.phase1_input_file` undefined in the engine context

The live schema has `phase1_input_file` (previously the `.md` source file path). In the automation context there is no `.md` file. The spec should state what value the engine writes here — options include `null`, the `run_id`, or the patch filename equivalent.

### 14. Engine file location not specified

The spec consistently refers to `engine.py` but does not state where it lives. Given the existing project conventions (`scripts/`, `analytics/`), this matters for import resolution of `step_client.py` and `db_client.py`. Suggest stating in Section 2 or Section 11: either `scripts/engine.py` following current conventions, or a new `engine/` package if the implementation splits into sub-modules.

---

## Items the spec handles particularly well

**Transaction design (SG-04 + SG-06):** Query `MAX(id)` live immediately before each INSERT with explicit id assignment, no caching between phases — this is correct for a single-writer SQLite system and idempotency is structural not procedural.

**Stream independence in GAP_FILL:** The eight-stream architecture with independent checkpoints is sound. Separating the API-volatile streams (S2: vocab fetch, S3: verse fetch) from the write-heavy S4 stream correctly isolates network failure from database integrity. A failure in S2 or S3 does not leave partial writes.

**Audit framework (§7):** The 19 audit checks with deterministic STOP / REVIEW / PASS classification, stored in `word_run_state.audit_detail` as structured JSON, is exactly the kind of traceable, reproducible quality gate the pipeline needs. The rule that STOP checks are all evaluated even after the first failure — giving the researcher the complete picture — is the right design.

---

## Recommended next steps

1. Resolve items 1–4 in the specification document (critical).
2. Add items 5–9 as a brief addendum or inline section updates (important).
3. Confirm `wa_term_root_family` write strategy (part of item 3 above — blocks S4 and N11 design).
4. Issue v3 of the spec and obtain researcher sign-off on the approval checklist.
5. Implementation can begin once v3 is signed off.
