---
name: reference_file_index_legacy_use_bypass_fks
description: GOVERNING (2026-06-15) - wa_file_index is LEGACY (stub only); registry linkage = bypass FKs (word_registry_fk / owning_registry_fk). NEVER join through file_index.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

GOVERNING ARCHITECTURE DECISION (2026-06-15) — registry linkage:

**Do NOT use `wa_file_index` in joins. It is legacy / a stub only.** The registry a row belongs to is carried by **bypass FK columns directly on the tables** — use those:
- `wa_file_index.word_registry_fk` → word_registry.id (populated 207/207, consistent with the old TEXT `registry_id`).
- `mti_terms.owning_registry_fk` → word_registry.id (the term's canonical home; ~2,539/2,619, ~80 to backfill).
- `wa_verse_records.word_registry_fk` and `wa_term_inventory.word_registry_fk` → word_registry.id — **added 2026-06-15** to finish the bypass the researcher started (these tables previously had ONLY `file_id` → file_index, the legacy path).

**Status facts (so we don't re-discover):**
- `wa_file_index` is LEGACY but was COMPLETE (207 rows, 0 registry gaps, 0 orphan file_ids) — its only real remaining job was the audit_word A1 onboarding gate. The live finding/cluster model already keys on `mti_terms.owning_registry_fk`, not file_index.
- The FK-bypass was half-built (file_index + mti had FKs; the bulk verse/term-inventory tables did not) — now completed.

**Onboarding (the new-word "ordeal" fix):** `audit_word` now creates a **file_index STUB** (minimal row + word_registry_fk) if absent in its first-time-population path, AND populates the bypass FKs at insert — so a new word is registry → extract → `audit_word` with no manual steps (+ H4 link/morph at insert). This unblocks retiring [[project_new_word_retirement_blocked]] (new_word/gap_fill — but verify the stub path on a brand-new word before archiving).

**Rule for all NEW code:** registry of a verse/term = its `word_registry_fk` (or via `mti_term_id → mti_terms.owning_registry_fk` for the term's home). Keep `file_id`/`wa_file_index` only as a legacy stub; do not add new joins through it. See [[project_morph_is_source_of_truth]], [[feedback_no_patch_to_nice_pointintime_result]].
