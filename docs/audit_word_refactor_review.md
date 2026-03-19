# AUDIT_WORD Refactor — Framework Review
**Status: AWAITING RESEARCHER APPROVAL**
**Instructions:** Add your comments / answers in the `> RESPONSE:` blocks below each section.
Do not delete any headings. Save the file when done. The agent will read this before writing code.

---

## 1. Root Architectural Problems (Confirmed in Code)

Three problems exist before any field-level fix makes sense:

1. **API calls and DB writes are interleaved.** Spec requires all network I/O to complete and be held in memory BEFORE the database transaction opens.
2. **No researcher gate.** Spec has A4 (gap report) + A5 (researcher approves what to fill). Current code writes everything unconditionally.
3. **Step numbering is wrong.** Current A1–A10 do different actions than spec A1–A10, in the wrong order.

> RESPONSE:
The program logging tables is not shown, we need to include the entries in engine_run_log, engine_stream_checkpoint, word_run_state, term_fetch_log
There is no cater for handling deletions, on all levels.  I think we should use  methodology of flagging for deletion, but using actual deletion as a separate archive run.  This may mean that we need to new field on each table that can be used to flag a delete state.
---

## 2. Proposed Step Sequence

| Step | Label | What happens | Tables read | Tables written | STOP/REVIEW |
|---|---|---|---|---|---|
| **Pre-A1** | **Lock sentinel** | Set `word_registry.last_automation_run = 'IN_PROGRESS'` before any API call (same as N6 in NEW_WORD). Stale lock → STOP. | `word_registry` | `word_registry` | Lock already set → STOP |
| **A1** | **Explicit invocation** | Require typed `"CONFIRM"`. Confirm registry row exists and has prior data. | `word_registry`, `wa_file_index` | — | No CONFIRM → abort. No `wa_file_index` rows → redirect to NEW_WORD |
| **A2** | **Load existing records** | Read all existing terms, verses, mti_terms, flags into memory. Schema version check here. | `wa_term_inventory`, `wa_verse_records`, `mti_terms`, `wa_data_quality_flags` | — | Schema mismatch → STOP. No existing records → redirect NEW_WORD |
| **A3** | **Re-fetch ALL from STEP** | `get_vocab_info()` + `get_verse_records()` per all existing terms. All API calls complete before any write. Span filter applied in memory. `term_fetch_log` written per term. | — | `term_fetch_log` | All failed → STOP (clear lock). Partial → REVIEW |
| **A3a** | **Span back-population** | For every existing `wa_verse_records` row (regardless of current `span_strong_match`): compare against STEP response. Set 1 (confirmed) or 0 (sibling-only). Derive `target_word`. Write `SPAN_FILTER_APPLIED` (id=24) if any → 0. Write `SPAN_BACK_POPULATED` (id=25) unconditionally. | `wa_verse_records` | `wa_verse_records`, `wa_data_quality_flags` | Partial → REVIEW |
| **A4** | **Produce gap report** | Compare STEP memory vs DB. Categorise every discrepancy. Print full report. **No DB writes.** Categories: `MISSING`, `STALE`, `NEW_TERM`, `ORPHAN`, `API_ONLY` | All content tables (read-only) | — | Always show before A5 |
| **A5** | **Researcher review gate** | Present gap report. Researcher approves which categories to fill. None approved → clean exit. | — | — | None → exit |
| **A6** | **Fill approved gaps** | Atomic per-word transaction. Only fills approved categories: COALESCE UPDATE `wa_term_inventory`, INSERT missing verses (`span_strong_match=1`), INSERT missing `mti_terms` for NEW_TERMs, INSERT missing `wa_term_related_words`, re-derive `wa_term_inventory.testament` per term, update `wa_file_index.testament_coverage`. Never DELETE. | — | `wa_term_inventory`, `wa_verse_records`, `mti_terms`, `wa_term_related_words`, `wa_file_index` | Failure → STOP + rollback step only |
| **A7** | **Run meaning parser** | Re-parse all terms. INSERT/UPDATE `wa_meaning_*` tables. UPDATE `parsed_meaning_id`. Show diff if output changed. | `wa_term_inventory` | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed`, `wa_term_inventory` | Mismatch → REVIEW with diff |
| **A8** | **Field-fill** | Interactive: present null `also_spelled` (Hebrew) and null `occurrence_count_qualifier` (all). Accept input or confirm null. | `wa_term_inventory` | `wa_term_inventory` | Cannot fail |
| **A9** | **Run audit + flag engine** | Flag engine: write `wa_data_quality_flags` + `wa_term_phase2_flags` (derivable flags). Then WR-01–WR-20. Write `word_run_state`. | All content tables | `wa_data_quality_flags`, `wa_term_phase2_flags`, `word_run_state` | STOP result → researcher approval before A10 |
| **A10** | **Update word_registry** | Set `phase1_status`, clear lock sentinel, update `last_automation_run`, `automation_run_id`, `notes`, `phase1_term_count`, `phase1_verse_count`. | — | `word_registry` | Should not fail |

> RESPONSE:
A1 - show registry entry with all fields in terminal to confirm to continueA1-check the notes of the word
A2 - the table read list is incomplete. I suggest we build a join statement that will show all the tables for a word. This would become the Word Extract Report. the following tables can all be affected. 
in the following related streams
- Terms - required: inventory,  root, phase 2 flags, mti terms
- terms - not always present: related words, meaning,, quality flags, term flags, term cross refences
- Verses: verse records

--   Section 2  — Registry:               word_registry
--   Section 3  — WA file index:          wa_file_index
--   Section 4  — WA term data:           wa_term_inventory, wa_term_related_words, wa_term_root_family
phase2_flag_types, wa_term_phase2_flags
--   Section 6  — WA quality flags:       wa_quality_flag_types, wa_data_quality_flags
--   Section 7  — WA cross-registry:      wa_crosslink_type, wa_cross_registry_links
--   Section 8  — WA verse records:       wa_verse_records
--   Section 9  — MTI tables:             mti_terms, mti_term_flags, mti_term_cross_refs
--   Section 11 — Meaning parsing:        wa_meaning_parsed, wa_meaning_sense, wa_meaning_stem, wa_lsj_parsed
A2 - the stop should be effected if any of the following is missing data. Sections 3,4,8,9 (mti_terms) and Words NOT marked COVERED / REPLACED / SPECIAL HANDLING . The action for the STOP is to show full registry record and perform a full word extract report.
A2,A3, A3a, A4.A5,A6  this design must be fundamentally reconsidered.  In need to start with STEP search.  I imagine we have a number of different extracts from STEP. Each extract affects specific tables. So we first need to get a collection of all the parsed data from STEP together, and then compare it against the tables with full INSSERT / UPDATE / SET DELETE FLAG
Can we have an interactive debate around the design of A2,A3, A3a, A4.A5,A6 

A7. Handling of meaning is involved.  There are approx 33 records that have meaning in a couple of different fields, and the rest should have meaning in separate tables. meaning should in principle be handled in section A2,3,4 and land in the tables. When one of the 33 records are selected then meaning should just be updated in the tables, and the data in the meaning fields on the term should be removed.
A8 and A9  I want to look deeper into the definition of setting these flags.
A10. missing the update of strongs_list, notes (write any anomalies, error report or success on word level)
---

## 3. Tables Touched — Full Comparison

| Table | Currently touched | Proposed |
|---|---|---|
| `word_registry` | A10 only (no lock sentinel) | Pre-A1 (set lock), A10 (status + clear lock) |
| `wa_file_index` | A9 (testament_coverage) | A6 (testament_coverage post gap-fill) |
| `wa_term_inventory` | A4 (COALESCE update) | A6 (fill approved gaps), A8 (field-fill) |
| `wa_term_related_words` | **never** | A6 (INSERT for NEW_TERMs) |
| `mti_terms` | **never** | A6 (INSERT NEW_TERMs when approved) |
| `wa_verse_records` | A3a | A3a (span back-pop), A6 (INSERT missing) |
| `wa_data_quality_flags` | A8 only (SPAN_BACK_POPULATED) | A3a + A9 (full flag engine) |
| `wa_term_phase2_flags` | **never** | A9 (derivable flags) |
| `wa_meaning_parsed` + sense tables | A5 (partial, no diff) | A7 (full re-parse with diff) |
| `term_fetch_log` | **never** | A3 (one row per term fetch) |
| `word_run_state` | A7 | A9 (after audit WR checks) |
| `engine_run_log` | open/close | unchanged |

> RESPONSE:


---

## 4. Questions Requiring Your Decision

### Q1 — Review Gate (A4/A5)
The spec requires a gap report followed by researcher approval of which categories to fill.

**Option A — CLI interactive prompt (default)**
The terminal prints the gap report and asks:
```
Fill MISSING fields?      [y/n]:
Fill STALE fields?        [y/n]:
Insert NEW_TERM records?  [y/n]:
Mark ORPHAN verses?       [y/n]:
```

**Option B — Command-line flag to bypass gate for scripted runs**
```
engine.py --mode=audit --registry=72 --auto-approve=missing,new_term
engine.py --mode=audit --registry=72 --auto-approve=all
```
Interactive prompt is the default; flag overrides it.

> RESPONSE (choose A, B, or both):


---

### Q2 — STALE Field Handling
A `STALE` gap means the DB already has a value but STEP now returns something different
(e.g. gloss or occurrence count changed upstream).

**Option A — Report only, never overwrite.**
STALE values are shown in the gap report but A6 never touches them.
Researcher edits manually after reviewing the diff.

**Option B — Offer as an approve/skip choice at A5.**
STALE is treated the same as MISSING — researcher can approve or skip.

> RESPONSE (choose A or B):


---

### Q3 — NEW_TERM Handling
A `NEW_TERM` is a Strong's number returned by STEP for this word that has no existing
`mti_terms` / `wa_term_inventory` row (e.g. STEP API vocabulary clusters have expanded).

**Option A — INSERT within AUDIT_WORD (A6) once researcher approves.**
Follows the same INSERT logic as NEW_WORD N10–N11 (mti_terms, wa_term_inventory,
wa_term_related_words, verse records). Stays within the audit run.

**Option B — Redirect to NEW_WORD.**
A NEW_TERM always triggers a message: "New term detected — run NEW_WORD mode to add it."
AUDIT_WORD does not INSERT new terms; it only refreshes existing ones.

> RESPONSE (choose A or B):


---

## 5. Anything Else to Change?

Use this space for any other requirements, constraints, or corrections to the framework above
before implementation begins.

> RESPONSE:


---
*When you have filled in all RESPONSE blocks, save this file. The agent will read it and proceed.*
