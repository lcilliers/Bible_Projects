---
name: reference_strongs_zero_padded_4digit_in_db
description: DB Strong's are zero-padded to 4 digits (H0430, G0575); compare with _canon/zfill, never short literals
metadata:
  type: reference
---

REFERENCE (2026-06-17): Strong's numbers are stored **zero-padded to 4 digits** EVERYWHERE in the DB — `verse_morphology.strongs`, `lexicon.strong`, `mti_terms.strongs_number` (e.g. `H0430` Elohim, `H0408` *'al*, `H0853` *'et*, `G0575`). Sub-entry suffix letters are appended (`H3372H`).

**Trap (cost me a Phase-0 cycle):** `_ve_engine_v2.py` seed lists used the SHORT form (`H430`/`H408`/`H853`), so every <4-digit Hebrew lemma **silently never matched** the padded measure layer → divine (Elohim), negation (*'al*), object-marker (*'et*), faculty (H995/H977) detection all broke, and it masqueraded as engine "stub" behaviour. Fixed via `_canon()` (zfill numeric to 4).

**How to apply:** any code comparing a strong to a literal/set MUST canonicalize both sides to 4-digit padded (or strip-zeros both sides) — never compare a hand-typed `H430` against a DB value. Suspect this bug whenever a Strong's-keyed lookup returns surprisingly empty. Related: [[project_morph_is_source_of_truth]], [[reference_file_index_legacy_use_bypass_fks]].
