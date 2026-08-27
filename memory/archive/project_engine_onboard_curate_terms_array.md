---
name: project_engine_onboard_curate_terms_array
description: "Onboarding an orphan term via the engine — curate the extract's `terms` ARRAY (not include_codes); --fetch-step ingests immediately, so relatedNos cascade in"
metadata: 
  node_type: memory
  type: project
  originSessionId: ace57f3e-b52e-4cc7-adda-ef61148f91e0
---

When onboarding a new/orphan term via `engine audit_word`, the contamination gate is the extract's **`terms` array**, not `meta.include_codes`.

- **`audit_word` onboards every entry in the extract's `terms` array.** `meta.include_codes` only steers the gap report — it does **not** restrict insertion. (Verified 2026-06-29: include_codes=['H6121A'] still onboarded all 6 family terms.)
- **`--fetch-step` fetches STEP *and* ingests in one pass** — no curation pause. STEP returns the anchor + its `relatedNos`, so the whole etymological family onboards immediately (a.qov H6121 pulled H6117-H6122: heel/footprint/consequence/steep/cunning).
- **Correct, validated gate:** `python scripts/word_study_extract.py --word X --anchors <code>` → **trim `terms` to the wanted code(s)** in the JSON → `audit_word --registry=N --extract-file=<curated.json>` (NOT `--fetch-step`).
- **Onboarding is NOT complete at term+verses.** The engine creates `mti_terms`+`wa_verse_records` but NOT `verse_context` or `ve_lexical`. Full recipe: term+verses → **`_apply_create_vc_for_onboarded.py --registries N`** (creates verse_context) → **`_apply_generate_ve_lexical_v2.py --live --vcids @file`** (reset ve-lexical). The generator scopes to `cluster_code IS NOT NULL`, so a cluster-deferred term (e.g. `arar`) gets no ve-lexical until its cluster is set — don't create its verse_context prematurely.
- **The integrity controls now test completeness, not just orphans** (2026-06-29): hygiene `mti/inv_delete_flag_null` (=0) + surfaced `active_term_verses_no_vc` / `vc_active_no_velex`. Orphan-only checks let the onboarded-but-incomplete terms pass clean — that was the hole.
- **Always run the integrity gate:** backup DB → `_check_integrity_controls.py --snapshot` pre → write → snapshot post → `--compare` (expect exactly +N term/+verses/+reg/cluster+1, **no new invariant breach**; baseline breach `dup_owner_strong=1` G0150 is pre-existing). On unexpected deltas, restore the backup and redo. This caught + rolled back the a.qov cascade twice.
- **Finishing fields** (engine leaves NULL): `mti_terms.cluster_code`, `mti_terms.status='extracted'`, **`mti_terms.delete_flagged=0`** (engine leaves it NULL — and queries filtering `delete_flagged=0` then silently exclude the term; e.g. the raw-data puller missed a.qov until set), `wa_term_inventory.term_owner_type='OWNER'`, and `wa_file_index.testament_coverage` (WR-09 REVIEW).
- Sub-entry senses split: onboard the IB sense only (a.qov H6121**A** "insidious" = IB → M14; H6121**B** "steep" = physical, excluded). See [[feedback_term_coverage_cascade_is_index_not_census]], [[project_new_word_retirement_blocked]].
