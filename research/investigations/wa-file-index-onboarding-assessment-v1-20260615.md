# wa_file_index, the FK-bypass, and the new-word onboarding ordeal — assessment

> Prompted by the researcher (2026-06-15): *"wa_file_index is largely legacy, probably incomplete; I tried to build FK references to bypass it — not sure it rolled out; and recent new-word additions were an ordeal with many manual fixes."* Investigated. Both recollections are accurate; one surprise.

## Facts

**1. `wa_file_index` is legacy — but COMPLETE, not incomplete (the surprise).**
- 207 rows · **0 non-excluded registries missing a file_index row** · **0 verses with an orphan file_id**. It is fully populated and internally consistent for active registries.
- So the audit_word A1 dependency on it isn't broken by *incompleteness* — file_index works. The pain is in *creating* a row for a new word, not in the table being patchy.

**2. The FK-bypass was built — but only HALF rolled out.**
- ✅ `wa_file_index.word_registry_fk` — populated **207/207**, consistent with the legacy TEXT `registry_id` 207/207.
- ✅ `mti_terms.owning_registry_fk` — populated **2,539/2,619** (80 gaps).
- ❌ `wa_verse_records` and `wa_term_inventory` — **no registry FK at all; only `file_id`**. They still route to the registry *through* `wa_file_index`.
- So there are **two parallel registry-linkage mechanisms, half-migrated**: the FK exists at the file_index + term level, but the bulk verse/term-inventory tables were never given it. The bypass stalled before the tables that would actually retire file_index.

**3. The onboarding ordeal is real and explained.**
- `new_word` (the only automated file_index creator besides `gap_fill` + a repair script) is stale — no H4 link/morph, divergent rules.
- `audit_word` can't create file_index, so a new word needs new_word/gap_fill *or* manual `_repair_03_wa_file_index.py` + manual term registration + (until now) manual linking + manual morph.
- Recent words' file_index rows carry **old/empty schema_version** (R213 `3.8.0`, R215/R211 `None`) — fingerprints of an old/manual creation path, not a clean automated one.

## What this means for the live model
The **live finding/cluster analytics key on `mti_terms.owning_registry_fk`** (which IS built) — not on file_index. So file_index's remaining real job is narrow: the **onboarding/audit gate** (A1) and a few file-centric reads. That makes the legacy table *mostly* bypassable already.

## Two paths (researcher to choose)
- **B — audit_word owns onboarding (small, low-risk, recommended near-term).** Give `audit_word`'s first-time-population path the ability to create the `wa_file_index` row (+ `word_registry_fk`) and register terms, so a new word goes registry → extract → `audit_word` with **no manual steps** and H4 link/morph at insert. Then `new_word`/`gap_fill` can be archived. Keeps file_index, but onboarding stops being an ordeal.
- **A — finish the FK-bypass, then retire file_index (larger, deliberate).** Add a registry FK to `wa_verse_records` + `wa_term_inventory`, backfill from file_index, repoint the file_id→registry reads, then drop file_index. Kills the legacy double-linkage. This is a real migration (200k+ verses, every file_id read path) — worth doing, but as its own scoped project, not bundled with retirement.

## Recommendation
Do **B** to fix onboarding + unblock the new_word/gap_fill retirement now; schedule **A** as a separate migration to finish the bypass the researcher started and finally retire file_index. The 80 missing `mti_terms.owning_registry_fk` should be backfilled either way (small).
