# Engine hardening — soft-delete integrity + mti_term_id maintenance

> Researcher directive (2026-06-15): after D2b-A, *"review engine source and harden the scripts around soft deletes, inconsistent deleted=1 and no soft delete, cascading of soft deletes, missing mti_term_ids."* This is the forward-looking fix so the fragility we just remediated by hand cannot recur. Review findings + located fixes below.

## What the review found (engine delete model today)
The engine soft-deletes in several places but **without a consistent cascade or a status↔flag invariant**:

| # | defect | where | symptom we hit |
|---|---|---|---|
| 1 | **Exclusion does not cascade.** Setting `phase1_status='Excluded'` (`audit_word.py:1937`, `gap_fill.py:405`) leaves all downstream rows active. | audit_word/gap_fill registry-status writes | R214 'suffering' Excluded but 928 active verses + 962 findings (D1 cleaned by hand) |
| 2 | **status markers ≠ `delete_flagged`.** `status='candidate_delete'` / `'delete'` is set (`audit_word.py:1441`) **without** `delete_flagged=1`. | `_apply_negative_filters` (audit A6b) | 8 OT-DBR-009 duplicate rows `status='delete'` but `delete_flagged=0`, still "active" |
| 3 | **Term soft-delete doesn't cascade to verses/findings.** `wa_term_inventory.delete_flagged=1` (`audit_word.py:915`) cascades to root_family/related_words but **not** to the term's `wa_verse_records` → `verse_context` → `finding`. | `_apply_changes` delete stream | T2 terms soft-deleted, their verses left active + unlinked (D2b-A) |
| 4 | **`mti_term_id` never written.** No create-path sets `wa_verse_records.mti_term_id` (`audit_word.py:1043` INSERT omits it); no maintained backfill. | all 4 verse-create paths | 2,673 processed verses unlinked (D2a) |

## The hardening (located, additive)
- **H1 — exclusion cascade.** A shared `cascade_softdelete_registry(conn, registry_id)` (the logic now in `scripts/_apply_excluded_registry_cascade.py`, promoted to an engine util) called wherever `phase1_status` is set to `Excluded`. Idempotent.
- **H2 — status↔flag invariant.** Whenever `status` is set to `candidate_delete`/`delete`, set `delete_flagged` consistently (delete ⇒ 1). Add a guard + a one-time reconcile of existing `status='delete' AND delete_flagged=0` rows that have no active data.
- **H3 — term-delete cascade.** When a term (`wa_term_inventory`/`mti_terms`) is soft-deleted, cascade to its `wa_verse_records` → `verse_context` → `finding` (reuse the orphan-cascade in `_apply_softdelete_orphan_verses.py`). And the inverse on un-delete.
- **H4 — link at insert (+ derivations).** Create-paths populate `mti_term_id` (match `term_id`→`mti_terms.strongs_number`) **and** `morph_code`+`stem` (from `get_verse_records`, per the morph-at-source plan), so verses arrive **linked + morphed + language-correct**. Then `reconcile_language` runs.
- **H5 — a standing integrity check** (`scripts/_integrity_*`): assert no active verse with NULL `mti_term_id` in a non-excluded registry; no `status='delete'` with `delete_flagged=0`; no active downstream under an excluded registry. Run after audits.

## Sequence (researcher-set)
1. **D2b-A** — soft-delete the 343 orphan verses (this plan's companion; runs after the morph cascade frees the DB).
2. **Engine hardening H1–H5** (this doc) — the durable fix.
3. **Morph/mode update** — finish populating morph for all changed/linked rows (the cascade now running covers the 2,673 newly-linked; H4 makes it automatic henceforth).

Implementation note: H1–H4 reuse the three reversible scripts already written this session (excluded-cascade, orphan-cascade, language-reconcile) — promote their core functions into shared engine utils rather than re-implement, so there is one cascade path, not several.
