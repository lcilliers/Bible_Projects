---
name: project_ve_lexical_normalisation_and_groundings
description: "GOVERNING (2026-06-15) - analytic layer normalised (ve_lexical); finding=real findings only; mti_terms + verse-records grounded. UPDATE: ve_lexical VALUE LAYER WIPED 2026-06-15 (corrupt/non-01b) - structure kept, rebuild from primary inputs is next"
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

**WIPED 2026-06-15 (researcher decision):** after reviewing raw M01/M23/M46 dumps, the researcher judged the migrated VALUE layer too corrupt / non-compliant with **01b** to repair (two incompatible vocabularies by old provenance l2_api-vs-l2_mechanical; faculty rule_v1 = R2 noise; sense collapses on coarse-subgloss terms; uneven depth). **All 237,397 `ve_lexical` rows HARD-DELETED** (`scripts/_apply_wipe_ve_lexical_v1.py`; pre-delete snapshot `backups/bible_research_pre-ve_lexical-wipe_20260615.db`). **Table STRUCTURE + indexes retained** (empty, ready for rebuild). The 332,175 M59 source findings stay soft-deleted in `finding` as the historical baseline. Migration/sense/faculty rerun scripts are now superseded.

**REBUILD v1 DONE 2026-06-15** (`scripts/_apply_ve_rebuild_mechanical_v1.py`, live). VE **1,2,3,5,6,7,8,13** mechanically derived for all 40,739 active term-in-verse units → **247,899 `ve_lexical` rows** (`source_provenance='mechanical_v1'`), strictly per 01b §1d signal-lists (transcribed verbatim, not improvised). Key design fix vs the failed faculty run: **attachment proxy = the term neighbourhood** (context_before+target_word+context_after) — signal in neighbourhood ⇒ assign; signal only elsewhere in verse ⇒ **UNRESOLVED**; none ⇒ NONE (present-only, no row). Faculty: R1 direct(gloss) / R2 indirect(neighbourhood) / R4 verse-only⇒UNRESOLVED / R5 NONE. Verified: Psa 20:3 da.shen faculty=UNRESOLVED (the prior false `memory` GONE); za.khar=memory(direct gloss). UNRESOLVED counts (the worklist, handled separately, "where in doubt ⇒ UNRESOLVED"): VE6 3,281 · VE7 8,539 · VE8 14,915 (only 835 confident yes) · VE13 14,450. Iteration-1 homograph noise flagged (will/spirit/bare-prepositions) for list-refinement. Review: `research/VE-lexical/wa-ve-rebuild-dryrun-review-20260615.md`.

**TEMPLATED NARRATION built + PERSISTED** (`scripts/_produce_ve_narration_v1.py` = the deterministic-view composer per 01b §1f; `scripts/_apply_persist_narration_finding_v1.py` = persist). Composes sense→type→mode→location→origin→faculty→attributed→compound→relational; **all elements included, multiples as multiples, UNRESOLVED as a `[field: UNRESOLVED]` placeholder, NONE/SILENT omitted**. **Persisted as the single `l2_meaning` FINDING per term-in-verse** (researcher decision: narration = a FINDING, not a ve_lexical row — ve_lexical holds the atomic field-VALUES, finding holds the composed MEANING): **30,571 M-cluster findings** inserted (`provenance='l2_meaning'`, `source_legacy_ref='ve-narration-v1-20260615'`, `supersedes_id`→old where matched); the **8,174 old NARRATED-PROSE l2_meaning soft-deleted** (the un-traceable prose this reform deprecates). T2 excluded from standalone meaning. The finding is regenerable from ve_lexical (deterministic). Outputs: `research/VE-lexical/wa-ve-templated-narration-first-20260615.md`, `wa-raw-dump-with-narration-M01-M23-M46-20260615.md`.

**NEXT:** resolve the UNRESOLVED worklists (separately); refine iter-1 signal-lists (homographs: will/spirit/bare-prepositions); a/an article cosmetic in narration. Still out of scope: VE4 (mode=column), VE9/10/11/12/14 (read/deferred), type sense-supersede, sense coarse-ceiling refinement. T2 got the mechanical lexical facts but stays excluded from standalone analysis.

Cross-refs: [[reference_file_index_legacy_use_bypass_fks]] (don't join file_index), [[project_new_word_retirement_blocked]].
