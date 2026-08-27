---
name: project_ib_characteristic_meaning_keyed
description: "ib_characteristic is keyed on MEANING-IN-CONTEXT (lemma+ESV rendering), not the bare lemma."
metadata: 
  node_type: memory
  type: project
  originSessionId: e78eb6e5-dae6-487a-a98b-121f066465fc
---

★ LIVE (2026-07-11). The `ib_characteristic` normalised index is keyed on **meaning-in-context**, not the base lemma. v2 keyed on base Strong's and **merged distinct meanings of one word** (halal → praise+boast+deride under one record; gur → sojourn+strife).

**What carries the true meaning of a Hebrew word in context** (established by DB investigation, not assumption):
- the **lemma** (base Strong's) is only an identifier — it merges meanings;
- **`stem`** (morphology, in `wa_verse_records.morph_code`/`stem`) helps but is insufficient — one form can carry two senses (Piel halal = praise *and* deride); and for gur the Qal covers both sojourn *and* strife;
- the **read-sense field `ve_lexical` ve_nr 101** is often a *contextual phrase* ("he restores my soul"), not the word's meaning → keying on it over-splits;
- **the ESV rendering (`wa_verse_records.target_word`) carries the true meaning-in-context** — it even splits homographs stem cannot. Cross-checked by stem/morph/attested-gloss.

**v3 model:** identity = `(base-lemma, normalised-ESV-rendering)`; `char_key="{lemma}:{norm_esv}"`, `name`=modal raw ESV. Evidence columns (so grouping is auditable, no bad merge hidden): `stems`, `morph_codes`, `esv_words`, `lexical_gloss` (attested inventory from `mti_terms`), `read_sense_variants` (read phrases preserved). Psalms: 502→877 records, 2168 spans linked, I7=0. Errs to **over-split (safe)**; known residue = irregular inflections (keep/kept) + multi-word ESV targets, mergeable in a later canonicalisation pass. `family` still NULL (the cross-characteristic grouping is the pending next layer).

Builder: `scripts/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py` (per-book, `--book N --live`, reversible — exports v2 first). Authoritative spec: cycle doc §7D v3. Integrity link = [[project_lexical_cycle_finalised_and_integrity_invariant]] (I7). Runs at book close for every book. See also [[project_morph_is_source_of_truth]], [[project_candidate_characteristic_seed_and_role_model]].
