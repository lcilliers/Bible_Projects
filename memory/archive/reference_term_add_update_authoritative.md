---
name: reference_term_add_update_authoritative
description: "The single authoritative doc for adding/updating a term — read it, do not re-derive from engine source headers."
metadata: 
  node_type: memory
  type: reference
  originSessionId: e78eb6e5-dae6-487a-a98b-121f066465fc
---

**Adding or updating a term = read `Workflow/Instructions/wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md` FIRST.** It enumerates every field written to every table, in single steps. Do not reconstruct the flow from `audit_word.py` headers, memory, or the retired modules — that is what has burned hours repeatedly.

The whole flow is **3 commands**:
1. `python -m engine.engine --register --word="X" --source="…"` (only if the English registry word is new) → writes `word_registry`.
2. `python scripts/word_study_extract.py --word X [--anchors …]` → Step 1 JSON, no DB writes. (Or `audit_word --fetch-step` folds this in.)
3. `python -m engine.engine --mode=audit_word --registry=N` → the engine, in ONE pass, auto-creates the `wa_file_index` stub and inserts + span-links `wa_term_inventory` / `mti_terms` / `wa_verse_records` / `wa_verse_term_links` / `wa_term_related_words`. `verse_id`+`verse_span_id` resolve from the master index by reference+strong (exact strong then base — this is the H3820↔H3820A base/suffix reconciliation).

**`audit_word` is the ONLY method for term & verse-record additions (mandatory, 2026-07-12).** No direct `INSERT` into `mti_terms`/`wa_term_inventory`/`wa_verse_records`, no ad-hoc `_apply_*` script, no patch — a batch/repair tool is compliant only if it invokes `audit_word` (`_run_gate1_onboard_batch_v1` does; use it for orphan-strong onboarding). **RETIRED (runtime-guarded off):** `_apply_gate1_term_onboard_v1` (hand-wrote `mti_terms`). Registry-selection: existing-registry-first, new rarely, non-substantive folds to best-fit (term-add doc 2026-07-12 amendment). A term is **always** added through its **registry word** (never on its own). To add terms to an existing word: steps 2–3 only. **⚠ Triage gate:** curate the extract's `terms` array to the intended Strong's before the live write (STEP pulls homonym/relatedNo noise) — see [[project_engine_onboard_curate_terms_array]]. **`new_word.py` is DELETED (2026-07-11); `gap_fill.py` superseded — do not use.** Verify after: I2=0 (every char_candidate span has a verse-record), `verse_span_id` populated, `mti_terms.status` not NULL. Related: [[project_new_word_retirement_blocked]], [[reference_file_index_legacy_use_bypass_fks]], integrity model `wa-db-integrity-definition-authoritative-v1`.
