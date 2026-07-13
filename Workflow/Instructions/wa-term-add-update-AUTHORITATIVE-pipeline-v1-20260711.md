# Adding / updating a term — AUTHORITATIVE pipeline (v1)

> *Entry point for **adding/updating a term** in the authoritative pipeline set — spine: `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` (§7C(a)); validations: `wa-db-integrity-definition-authoritative-v1`.*
>
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
- **Shortcut:** `audit_word --fetch-step [--anchors …]` auto-runs this extract, folding STEP 2 into STEP 3.

### ⚠ EXTRACTION MUST BE MORPHOLOGY-ANCHORED, FULL-VARIANT (researcher direction 2026-07-13)
STEP splits some Strong's across **lettered sub-codes** (e.g. *ruach* H7307 → H7307**G/H/J**; base H7307 = 0), and single-code resolution (`_resolved_strong` → `vocabInfos[0]`) **silently drops the sibling codes' verses** — including whole books (the cause of missing verse-records). The extraction **must**:
1. **Identify the variant(s) through the morphology** — the STEP codes the master (`verse_span_index`) actually tags for that Strong's (the double-control: morphology finds the variants, the verse-check finds what's missing);
2. **do a full STEP pull for the Strong's across all those variants** (union, dedup by `osisId`), with morphology;
3. **diff against what the DB already has** → the previously-missed verses; **bring them through** (via `audit_word`).

This is a **root fix in the extractor** (`word_study_extract.fetch_verses` unions the morphology-attested variants), **not** a per-term patch — see the root-fix rule in Governance. `get_verse_records_with_html` preserves an exact variant code, so the union is a loop over the master's variant codes.

### ⚠ TRIAGE GATE (mandatory before the live audit) — do not skip
The extract's `include_codes` carry **STEP related-number noise** — STEP pulls homonyms/relatedNos that are NOT the intended term (e.g. onboarding `perek` H6531 also pulled the `H6532` "curtain" homonym). **Curate the extract's terms array down to the intended Strong's BEFORE the live write**, or `audit_word` onboards junk. Curate the `terms` ARRAY (memory `project_engine_onboard_curate_terms_array`). Dry-run first; run the integrity snapshot/compare gate.

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
- **ROOT FIX, NOT ONE-OFF (researcher direction 2026-07-13).** Fix the *cause*, not the instance. A one-off / per-term / per-book patch is **rarely appropriate, and NEVER appropriate when the problem may recur** — a class of bug (e.g. the STEP multi-variant drop) is fixed in the shared extractor so **every** future term/book is correct, not remediated case-by-case. If you find yourself hand-patching one term's data, stop and fix the mechanism.
- **Integrity-gated:** `audit_word` runs its own pre/post backup in live mode. Do not disable.
- **Per word / per registry.** No cross-book, no cross-word bulk hand-edits.
- **A term without a registry home cannot be onboarded** — decide its registry word first (Step 1), then Steps 2–3.

*Filed 2026-07-11. Authoritative for term add/update. If the engine changes, update THIS file the same day (version bump) — it is the single place this is documented.*

---

## AMENDMENT 2026-07-12 (researcher direction) — the REGISTRY PATH + registry-selection rule

**Registry path (architecture decision, standing).** Every characteristic word **MUST be a registered term** — the term-backbone (`word_registry → mti_terms → wa_verse_records → verse_span_index`) is authoritative and must match the reading. We do **not** relax the registry requirement for emergent / seed-missed characteristics: a candidate whose word is unregistered, or which lacks a verse-record, is **onboarded via this pipeline before the read** (this closes the I2 gate; the cycle's Stage-3 step-d). This is the answer to the register-vs-relax question — **register**.

**Registry-selection rule (mandatory, Step 1).** When choosing a term's registry home:
1. **First, associate it with a RELEVANT EXISTING registry** — an existing `word_registry` word whose sense the term belongs to. This is the default and by far the common case.
2. **Only rarely — where no existing registry fits — create a NEW registry** (your choice; note the justification).
3. **A term not substantive enough to be its own study-word is folded into the best-fit existing registry**, never made a new registry. (E.g. Proverbs *marpe/riphuth* "healing" → folded into the existing `peace` registry on a best-fit basis, not made a new word.)

The seed's `char_candidate_tag` (`"Reg N word"`) already names the intended existing registry for most candidates — use it; supply the association only where the tag is `IB:*` or absent.

---

## AMENDMENT 2026-07-12 (researcher direction) — `audit_word` is the ONLY method for term & verse additions

**Mandatory, no exceptions.** Every addition of a **term** (`mti_terms`, `wa_term_inventory`) or a **verse-record** (`wa_verse_records`) is processed **only** through the integrated engine method **`audit_word`** (STEP 3). There is **no other sanctioned path to create these rows**:

- **No** direct `INSERT` into `mti_terms` / `wa_term_inventory` / `wa_verse_records` — by hand, ad-hoc script, or raw SQL.
- **No** patch (`apply_session_patch`) that mints term/verse rows.
- A batch onboarder or repair tool is compliant **only if it invokes `audit_word`** — e.g. `_run_gate1_onboard_batch_v1` shells `python -m engine.engine --mode=audit_word --registry=N --extract-file=… --add-terms`. A script that writes those tables itself is **not** compliant, whatever its intent.

**Why:** `audit_word` is the single pass that writes every field **and both master links** (`verse_id`, `verse_span_id`) **+ VTL + related-words + run-state**, under an integrity-gated pre/post backup. Hand-written inserts miss fields/links and silently break I1/I2/I3.

**The compliant tools:** the 3-command pipeline above (`--register` → `word_study_extract` → `audit_word`) for a whole word; **`_run_gate1_onboard_batch_v1`** (audit_word path) for onboarding orphan strongs to registries.

**The term↔registry allocation is scaffolding only — ignored downstream (researcher direction 2026-07-12).** A term's registry home exists for **one reason**: to give the term a hook so it can be onboarded (registered + its verses added). The specific allocation is **highly debatable and has NO analytical value in the study** — after the term/verse are added it is **ignored throughout**. Therefore:
- **The only check is that a term HAS a registry (any).** Never re-home, reconcile, merge, move, or debate which registry a term sits under. A "wrong-looking" home (e.g. *ruach*→anger, *palas*→envy) is **not a defect** — it needs no fix.
- Do **not** build tooling or steps that reconcile term↔registry allocation. (Verified 2026-07-13: `audit_word` does **not** re-home — it never rewrites `owning_registry_fk` on an existing term; `--add-terms` is isolated to the new terms. So this rule is already honoured by the engine; keep it that way.)
- Onboarding still uses the seed's `char_candidate_tag` registry as the default hook, but its *correctness* is immaterial — pick any relevant existing registry and move on.

**Prohibited / retired — they hand-write the term/verse tables, bypassing `audit_word`:**
- **`_apply_gate1_term_onboard_v1`** (`INSERT INTO mti_terms`) — **RETIRED, do not use.** Use `_run_gate1_onboard_batch_v1` instead. (Runtime-guarded off 2026-07-12.)
- `_apply_master_index_backfill_v1`, `_apply_psalms_gate1_completeness_v1`, `_apply_psalms_gate1_reactivate_v1`, `_repair_07_wa_verse_records` — may only ever touch **existing** rows (FK backfill / soft-delete reactivation), **never mint a new term or verse-record**. New identities go through `audit_word`, full stop.
