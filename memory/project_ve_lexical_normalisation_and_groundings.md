---
name: project_ve_lexical_normalisation_and_groundings
description: "GOVERNING (2026-06-15) - analytic layer normalised; VE values live in ve_lexical, finding=real findings only; mti_terms + verse-records grounded; value rerun is next"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

GOVERNING (2026-06-15, major restructure). Schema → **3.33.0**. **All VE/lexical files are filed + indexed at `research/VE-lexical/00-INDEX.md` — start there (the old scattered wa-l1l2-*/wa-ve-lexical-* names were moved + renamed 01–12 on 2026-06-15).**

**The analytic-layer normalisation (researcher-directed):**
- The "14 VE" was a PHANTOM (no real structure) and the `finding` table conflated VE attributes with real findings.
- Now normalised into TWO tables: **`verse_context`** = verse-level (1:1, per term-in-verse) + **`ve_lexical`** (M59) = items-in-verse-level (1:many). `ve_lexical` cols: `verse_context_id · ve_nr · ve_label · related_tier · value · notes · source_provenance`. ONE row per actual value (no delimited lists, no NONE/imputed).
- Migrated 298,096 VE field-value findings → **212,243 `ve_lexical` rows** (82,178 NONE dropped; l2_api wins l2_api/l2_mechanical overlap); source findings soft-deleted. **`finding` is now REAL findings only** (~11k = 2,892 synthesis CLUSTER/GLOBAL + 8,174 `l2_meaning` to be regenerated). See `research/investigations/wa-ve-lexical-migration-complete-v1-20260615.md` + `wa-ve-lexical-data-model-redesign-v1`.
- ve_nr map: 1 sense·2 type·3 compound·4 mode-of-operation·5 location·6 origin·7 faculty·8 attributed-God·9 purpose·10 typology·11 response·12 produces·14 literary·15 name. **Mode (#4 morph) is a COLUMN, not in ve_lexical** ([[project_morph_is_source_of_truth]]).

**The groundings (fix the truth first — [[feedback_no_patch_to_nice_pointintime_result]]):**
- **`mti_terms` (canonical) grounded:** soft-deleted (cascaded) excluded + zero-verse terms → 2,402 active, now UNIQUE per Strong's, status-clean, owned (OT-DBR-009 dedup swept via the 0-verse rule).
- **`wa_verse_records` UNIQUE by `(reference, term_id)`:** 58,966 active (cleared 161 dead-term orphans + 933 XREF dups + 1 double-insert). `verse_context` keys off the unique `verse_record_id`.
- Residue (next): ~1,623 sole-copy XREF verses (owner re-derivation), 8 ownerless T2 terms, ~19k dangling `verse_context.group_id` (legacy VCG), `verse_context.cluster_subgroup_id` = the LIVE grouping.

**NEXT PHASE = value rerun/validation (researcher will do jointly):** sense still carries the uniform gloss for l2_mechanical rows → apply per-occurrence subgloss (two-level: 83% straight-through mono + 17% complex via 70 poly terms; [[project_l1l2_field_reliability_direction]]); sense+type are paired & can be multi; values must be lookup/rule-driven, present-only; then regenerate the meaning as the templated narrative = the single lexical finding.

Cross-refs: [[reference_file_index_legacy_use_bypass_fks]] (don't join file_index), [[project_new_word_retirement_blocked]].
