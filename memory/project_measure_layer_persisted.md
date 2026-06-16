---
name: project_measure_layer_persisted
description: "GOVERNING (2026-06-16): schema 3.34.0 / M60 — the verse is now a first-class canonical entity; full-verse original-language morphology + lexicon persisted in the DB (the measure layer); lexical rules read the DB, not live STEP"
metadata:
  node_type: memory
  type: project
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

GOVERNING (2026-06-16, schema **3.34.0**, migration **M60**). The **verse is now a first-class canonical entity** and its original-language **measure layer** (01b §2) is **persisted in the DB** — so the lexical engine reads morphology from the DB instead of fetching STEP live (faster, consistent, auditable). Tables:
- **`verse`** — canonical, one row per reference/osis (**23,318** rows; this is the first true one-row-per-verse table, above the per-term `wa_verse_records`).
- **`verse_morphology`** — one row per word per verse (**302,394** rows): `surface · strongs · primary_strong · morph_code · language · pos · stem · person`. Every word incl. untagged ones ("seized", "many") — so the predicate-argument items (object/cause/how/experiencer) are deterministic reads. `morph_code` stays source of truth ([[project_morph_is_source_of_truth]]).
- **`lexicon`** — one row per Strong's (**11,623**): original-language **unicode** + transliteration + gloss + **medium_def** (also powers VE1 sense).
- **`verse_morphology_raw`** — raw STEP html per verse (provenance / re-parse).
- **`wa_verse_records.verse_id`** — bypass FK → `verse` (the explicit verses↔morphology path; 213,621 rows linked).

**Key facts:** ingest = `scripts/_apply_ingest_verse_morphology.py` (resumable, per-verse **circuit-breaker** `VE_MAX_SEC`); fetch via STEP **direct passage endpoint** `rest/bible/getBibleText/{ESV_th}/{ref-dotted}` (NOT search — search had a 60-cap → 25% miss; direct = **0 miss**). Scope = the **23,318 active-term verses** (verses containing ≥1 tagged term); the whole Bible is ~31,102 — extending to the full Bible is an open option the researcher may take.

**IMPORTANT distinction (clarified 2026-06-16):** `wa_verse_records` is unique by **(reference, term_id)** (no dup term-in-verse rows), **NOT** by reference — a verse has one row per *distinct term* (avg 2.5; up to 12). So 58,966 active rows = 23,318 distinct verses. **Redundancy finding:** the interim `mechanical_v1` ve_lexical repeats verse/clause-level facts across a verse's terms (~39%: location 62% · compound 60% · attributed 54%; sense only 4%). OPEN DECISION → give each VE item a **scope** (verse-scoped facts stored ONCE on `verse`; term-scoped per `ve_lexical`; compound edge once) — the `verse` table is the enabler. See [[project_ve_proposition_gap]].
