# Adding / updating a term — AUTHORITATIVE pipeline (v1)

> **READ THIS before any term work. It is THE source. Do not reconstruct it from source-file headers, memory, or the retired modules.** Every field below was read from the live engine code (`engine/register.py`, `engine/audit_word.py`, `engine/db.py`) on 2026-07-11. Supersedes any contrary bit in the `audit_word.py` header, CLAUDE.md §4, or older docs.
>
> **RETIRED — do not use, do not reintroduce:** `new_word.py` (deleted 2026-07-11), `gap_fill.py` (superseded). The one and only pipeline is below.

## The whole thing is THREE commands. The engine writes every field. Never hand-write these inserts.

```
STEP 1  register the registry word   (only if the English word is new)
STEP 2  extract its STEP data          (produces the Step 1 JSON; no DB writes)
STEP 3  audit_word                     (the engine creates/links EVERY row in one pass)
```

Adding a term is **never** done on its own — a term is always added **through its registry word**. To add/refresh terms for a word that already exists, do STEP 2 + STEP 3 only.

---

## STEP 1 — register the registry word (skip if it already exists)
```
python -m engine.engine --register --word="<english word>" --source="<source list>"
```
Writes **one `word_registry` row** (`engine/register.py`):

| field | value written |
|---|---|
| `id` | max(id)+1 |
| `no` | max(no)+1 (this is the registry number `N` used everywhere below) |
| `word` | the word |
| `source_list` | `--source` |
| `category_hint` | optional arg (else NULL) |
| `phase1_status` | `'Pending'` |
| `automation_eligible` | `1` |

If the word already exists, **do not re-register** — find its `no` with `SELECT no FROM word_registry WHERE word=…`.

---

## STEP 2 — extract the word's STEP data
```
python scripts/word_study_extract.py --word "<english word>" [--anchors H1234,G5678]
```
- **Writes NOTHING to the DB.** Queries STEP only.
- Produces `research/discovery/{word}_step_data_{YYYYMMDD}.json` — the **Step 1 JSON** (all terms + all verses for the word). `audit_word` reads the latest such file automatically.
- Requires the STEP server up (`http://localhost:8989`).

---

## STEP 3 — audit (the engine does everything)
```
python -m engine.engine --mode=audit_word --registry=N
```
In **one pass** the engine ingests the Step 1 JSON and creates/updates every row. **Every table, every field it writes:**

### a) `wa_file_index` — auto-created stub if none exists (NO manual step)
| registry_id | word_registry_fk | word | filename | phase | schema_version | produced_date | revision_note | last_changed |
|---|---|---|---|---|---|---|---|---|
| str(reg id) | reg id | word | `WA-NNN-word-audit_word_stub-DATE.json` | `'Phase 1 (audit_word stub)'` | EXPECTED_SCHEMA_VERSION | today | "auto-stub … bypass FK authoritative" | now |

### b) `wa_term_inventory` — one row per NEW term
| file_id | language | term_id | strongs_number | transliteration | step_search_gloss | word_analysis_gloss | occurrence_count | meaning | meaning_numbered | lsj_entry | short_def_mounce | word_registry_fk | last_changed |

### c) `mti_terms` — one row per NEW term (unique per Strong's, programme-wide)
| strongs_number | transliteration | gloss | language | owning_registry | owning_word | extraction_date |
- `status` is set afterwards by **A6b classification** (data-driven): `extracted` · `extracted_thin` · `candidate_delete` (F1–F5 filters). Never set by hand.

### d) `wa_verse_records` — one row per term-occurrence-in-a-verse
| file_id | term_inv_id | term_id | mti_term_id | transliteration | book_id | reference | chapter | verse_num | testament | translation | verse_text | target_word | span_strong_match | context_before | context_after | morph_code | stem | word_registry_fk | **verse_id** | **verse_span_id** | created_at |
- `translation` = `'ESV'`.
- **`verse_id` + `verse_span_id` are the master link.** Resolved by `db.resolve_verse_and_span(reference, strong)`: `verse_id` from the `verse` row; `verse_span_id` from `verse_span_index` for that verse where `primary_strong` = the exact strong, **else** the base strong (suffix stripped), first occurrence (lowest `word_index`). *(This is the base-vs-suffix reconciliation — it matches `H3820` to `H3820A` automatically.)*

### e) `wa_verse_term_links` (VTL) — one row per new verse-record
| verse_id (= the new `wa_verse_records.id`) | term_inv_id | step_subgloss_code | step_subgloss_label | span_strong_match | target_word |

### f) `wa_term_related_words` — the term's related words (insert / re-sync)

### g) run-state fields set on completion
- `word_registry.last_automation_run` = `'AUDITED'`
- `word_run_state.approved_by` = `'PROVISIONAL'` (audit ≠ full sign-off)

**The registry linkage is the bypass FK.** `word_registry_fk` (carried on `wa_term_inventory`, `mti_terms` owning, and `wa_verse_records`) is **authoritative**. **Never join through `wa_file_index` for data** — the stub exists only to satisfy a legacy gate.

---

## To ADD terms to a word that ALREADY exists (e.g. the 261 orphan fix)
Just STEP 2 then STEP 3 (`audit_word --registry=N`). The engine's gap report inserts `NEW_TERM` (+ its `mti_terms`, `wa_verse_records`, VTL) and `MISSING_VERSE` for anything in the fresh extract not yet in the DB, and links every span. Nothing else to do, no second pass.

## Verify after STEP 3 (must all hold — cross-ref `wa-db-integrity-definition-authoritative-v1`)
- every `char_candidate` span for the word now has a live `wa_verse_records` (**I2 = 0**);
- `verse_id` + `verse_span_id` populated on the new records (not NULL);
- `mti_terms.status` is not NULL (A6b ran).

## Governance
- **Integrity-gated:** `audit_word` runs its own pre/post backup in live mode. Do not disable.
- **Per word / per registry.** No cross-book, no cross-word bulk hand-edits.
- **A term without a registry home cannot be onboarded** — decide its registry word first (Step 1), then Steps 2–3.

*Filed 2026-07-11. Authoritative for term add/update. If the engine changes, update THIS file the same day (version bump) — it is the single place this is documented.*
