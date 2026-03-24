# Soul Phase 2 — Root Cause Analysis & Repeatability Fix Plan

Generated: 2026-03-23  
Status: Plan — pending researcher approval before execution

---

## Status of Previous Plan

The plan presented in the previous message was **not yet executed** — it was pending approval.
That plan contained mostly one-off DB patches and did NOT address why each issue arose,
nor would it have prevented recurrence. This document supersedes it.

---

## Key Structural Finding (Blocking)

**`audit_word.py` A3/A4 is architecturally incompatible with the Phase 2 pipeline.**

`audit_word.py` was designed for the old 1-term-to-many-verses model:
- A3 fetches verses per `term_inv_id` (one term owns its verses exclusively)
- A4 reconciles using `WHERE term_inv_id = ?`

Phase 2 uses a many-to-many model:
- All verses for a word study share a single pool keyed to a *primary* `term_inv_id`
- The full term membership travels via `wa_verse_term_links`

**Consequence**: If `audit_word.py` is run after Phase 2 extraction, A4 will:
- Find 0 existing verses for every non-primary sub-gloss (H5315H–N, G5590H–K etc.)
  because those verses are stored under the primary term's `term_inv_id`
- Attempt to INSERT them as new verse records → duplicate rows (or integrity errors)
- Cascade-delete `wa_verse_term_links` rows when it deletes "obsolete" verses
- Never rebuild `wa_verse_term_links` (it doesn't know the junction table exists)

**This means two things for the pipeline design:**
1. `audit_word.py` must NOT be run (A3/A4) for any word that has gone through Phase 2 extraction.
2. The metadata updates that `audit_word.py` performs in A8 and A9 (testament_coverage,
   phase1_term_count, phase1_verse_count) must instead be performed by `_extract_word_terms.py`
   directly, so the pipeline is complete without audit_word.py.

---

## Root Cause Analysis — All 8 Issues

### Issue 1 — H4578 (me'eh) and H5397 (neshamah) have zero verses

**Root cause:**
`_discover_word_terms.py` discovers terms exclusively via STEP's `get_related_term_cluster()`
API call on the primary anchor codes. H4578 and H5397 are semantically related to soul but are
NOT returned by STEP's cluster for H5315G or G5590G. They existed in the old Session A word study
(confirmed: `mti_terms` rows 515 and 516, owning_registry=182) but were absent from STEP's
relatedNos, so the Phase 1 discovery script never encountered them.

There is no mechanism in `_discover_word_terms.py` to specify additional codes outside the STEP
cluster traversal.

**Pipeline fix required:**  
Add `--supplemental-codes` to `_discover_word_terms.py`. Codes listed here bypass the STEP
cluster and are fetched directly, with `step_section_type = "supplemental"` and a default triage
of `include? = yes`. These codes must be carried through the decisions JSON's `meta` block so
`_extract_word_terms.py` can process them alongside cluster-derived terms.

**One-off fix for soul:**  
Add H4578 and H5397 directly to `soul_term_decisions_20260323.json` as include terms in G2.

---

### Issue 2 — G5590G covers only 6% of its occurrences

**Root cause:**
The STEP span filter rejects the majority of G5590G verses because the ESV_th tagging
for psuchē verses does not consistently match the span-filter criteria applied by
`filter_verse_records()` in `analytics/step_client.py`. This is not a new problem unique
to Phase 2 — it existed in the pre-Phase-2 pipeline too.

**Pipeline fix required:**
None at the extraction layer. This is the correct behaviour of the span filter — it
avoids false positives. The Phase 2 process should auto-insert a `SPAN_RESOLUTION_CONFLICT`
quality flag for G5590G with a note directing independent NT corpus research.
The flag engine currently derives this flag only if certain span conflicts are detected.
We need `_extract_word_terms.py` to call `run_flag_engine()` post-commit so the flag is
regenerated on the corrected DB state.

**No one-off fix needed** — this is an acknowledged coverage limitation.

---

### Issue 3 — H5317 (honey, nophet) in registry with no justification

**Root cause:**
H5317 was initially placed in group G2r (review) by `_apply_term_decisions.py` because
it appeared in STEP's relatedNos for H5315G. It was then manually promoted to `action=include`
in the decisions JSON in a prior session, without a `status_note` being written to explain the
inclusion. The triage process does not enforce a root-consonant check before promotion.

H5317 (נֹ֫פֶת, npt) does not share the root consonants of H5315G (נֶ֫פֶשׁ, npsh).

**Pipeline fix required:**
`_discover_word_terms.py` should add a root-consonant comparison to the triage output.
Any related term whose consonant skeleton differs from the anchor's by more than 1 position
should be flagged with a `consonant_mismatch: true` column in the triage table and default
to `G2r` (review) — not silently included. This uses the existing `is_proper_noun` logic
as a template.

**One-off fix for soul:**
Change H5317 `action` to `exclude` in `soul_term_decisions_20260323.json`.
The re-run of `_extract_word_terms.py` will cascade-delete it from the DB.

---

### Issue 4 — testament_coverage still OT_only / Issue 5 — Registry notes stale

**Root cause (same for both):**
`audit_word.py` contains the logic to update both fields (step A8 and A9) and was run before
Phase 2 extraction, not after. Even if it had been run after Phase 2 extraction, A4's
incompatibility (see structural finding above) would have corrupted the data before A8/A9 ran.

The intended metadata update never executed against the Phase 2 data.

**Pipeline fix required:**
Add the following to `_extract_word_terms.py` in a new post-commit step:
- `UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?`  
  (derived from DISTINCT testament values in the inserted verse records)
- `UPDATE word_registry SET phase1_term_count = ?, phase1_verse_count = ?, last_automation_run = ?`  
  (counts queried from DB after commit)

These are direct copies of audit_word.py A8/A9 logic, ensuring the extraction script is
self-contained and does not require a subsequent audit_word.py run.

**No separate one-off fix needed** — once `_extract_word_terms.py` is updated and re-run,
both fields will be set correctly as part of the run.

---

### Issue 6 — anchor_verses = None

**Root cause:**
No script in the pipeline writes `word_registry.anchor_verses`. This is a researcher-curated
field intended to be set manually. No WR audit check exists to flag its absence as a
REVIEW item, so it has been silently null across all runs.

**Pipeline fix required:**
Add WR check to `engine/audit.py`:
- Query `word_registry.anchor_verses WHERE no = registry_id`
- If NULL → REVIEW: "anchor_verses not set — no anchor texts designated for Session B"

**One-off fix for soul:**
Directly update `word_registry` row 182 via SQL:
```sql
UPDATE word_registry
SET anchor_verses = 'Gen 2:7; Lev 17:11; Isa 53:10-11; 1 Cor 15:44-46; Matt 10:28'
WHERE no = 182;
```

---

### Issue 7a — researcher_approved = 0 / audit_result = REVIEW

**Root cause:**
`researcher_approved` is a manual gate that the researcher must set when satisfied with the
word's data quality. It was never set because the word has not been cleared of all REVIEW items.
The REVIEW items are: WR-05, WR-08, WR-19. Each has its own root cause below.

`phase1_status` remains "In Progress" because `audit_result` was not "PASS" in the most
recent run — again, because of outstanding REVIEW items.

**Not a pipeline bug** — `researcher_approved` is deliberately manual. Once all REVIEW items
are resolved, the researcher sets this manually.

---

### Issue 7b — WR-05: ID gap in wa_term_inventory

**Root cause:**
`_wr05()` in `engine/audit.py` checks that the set of `wa_term_inventory.id` values for
this word study forms a contiguous sequence. The gap from ID 493 (old audit_word.py engine
inserts) to 1530 (Phase 2 batch inserts starting from MAX(id)+1 of the entire table) is 1037
positions — a legitimate Phase 2 batch insert, not evidence of partially-written data.

The check was designed prior to Phase 2. It does not distinguish "gap from term deletion"
(suspicious) from "gap from batch insertion at a different sequence point" (normal).

**Pipeline fix required:**
In `_wr05()`: check whether all gaps are single-step removals or whether they represent
a single large forward jump (> 10 IDs). A single large forward jump after a contiguous block
is classified as "Phase 2 batch insert — expected" and returns REVIEW rather than STOP.
Specifically: if there is exactly one gap, and both sub-sequences are themselves internally
contiguous, downgrade to REVIEW with an explanatory message.

---

### Issue 7c — WR-08: G5590 base entry (0 verses, 825 occurrences)

**Root cause:**
The old `audit_word.py` engine inserted G5590 (base lemma, no sub-gloss suffix) into
`wa_term_inventory` before the Phase 2 sub-gloss architecture existed. Phase 2 inserted
G5590G–K as the actual include terms. Nothing removed G5590. It now sits in the DB as
an orphan with 825 `occurrence_count` and 0 verses, triggering WR-08 and WR-19.

**Pipeline fix required:**
In `_extract_word_terms.py`, in the purge phase (Step 2), add logic:
- For each include sub-gloss code (e.g., G5590G), derive its base code (G5590)
- If the base code exists in `wa_term_inventory` for this file_id AND all of the
  base code's sub-glosses are among the include terms → purge the bare base entry

This ensures that if G5590G–K are all included, the superseded G5590 base
is automatically removed.

**One-off fix for soul:**
Manual cascade delete of G5590 from `wa_term_inventory` for file_id=36.

---

### Issue 7d — WR-19: Parse warnings on G5590 without NOTE flag

**Root cause:**
G5590 base entry has a `wa_meaning_parsed.parse_warnings` value, which triggers WR-19
(parse warnings not reflected in a NOTE quality flag). This is a symptom of Issue 7c —
once G5590 is purged, WR-19 will pass automatically.

**No separate fix needed** — resolved by Issue 7c fix.

---

### Issue 8 — MTI cross-references missing for 24 of 27 terms

**Root cause:**
`_extract_word_terms.py` does not write to `mti_terms` or `mti_term_cross_refs`.
The old `audit_word.py` engine populated `mti_terms` for the terms it processed (H5315,
H4578, H5397, G5590 — the 4 original terms). The 23 new Phase 2 terms (H5315G–N, G5590G–K,
H5314, G5591, etc.) were never registered in `mti_terms` by the Phase 2 script.
Cross-registry links require a separate pass that queries every other registry to find
overlapping Strong's numbers.

**Status:** Out of scope for this fix batch. Requires a dedicated MTI rebuild pass.
Flagged for a future session.

---

## Execution Plan

### Changes to scripts (pipeline repeatability)

#### A. `scripts/_discover_word_terms.py`
- Add `--supplemental-codes` CLI argument (comma-separated Strong's codes)
- Supplemental codes: fetched via `get_vocab_info()`, added to triage with
  `step_section_type = "supplemental"`, group G2, default `include? = yes`
- Note in triage: "Supplemental code — manually specified, not from STEP cluster"
- `meta.supplemental_codes` added to output JSON

#### B. `scripts/_extract_word_terms.py`
- **Purge superseded base entries**: after processing include terms, if any base lemma
  (code without suffix) exists in the DB but all its sub-glosses are included, purge the base entry
- **Post-commit metadata update** (new Step 10):
  - Compute testament distribution from inserted verse records
  - `UPDATE wa_file_index SET testament_coverage = ?`
  - Count terms and verses
  - `UPDATE word_registry SET phase1_term_count = ?, phase1_verse_count = ?, notes = ?, last_automation_run = ?`
- **Post-commit flag engine** (new Step 11):
  - Call `run_flag_engine(conn, file_id)` to regenerate quality flags on the updated data

#### C. `engine/audit.py`
- **`_wr05()`**: if exactly one gap exists and both sub-sequences are contiguous, return
  REVIEW with "Phase 2 batch gap detected (IDs X–Y contiguous, Z–W contiguous) — expected"
  instead of generic REVIEW  
- **Add `_wr_anchor_verses()`** (new check): query `word_registry.anchor_verses WHERE no=?`;
  if NULL → REVIEW "anchor_verses not set"
- Register the new check in `_CHECKS` list

### One-off DB corrections (soul only)

1. Edit `soul_term_decisions_20260323.json`:
   - Add H4578 (group G2, action=include) with STEP vocab data
   - Add H5397 (group G2, action=include) with STEP vocab data
   - H5317: change action from `include` to `exclude`
   - Update summary counts

2. Run `_extract_word_terms.py` (will also execute new Step 10 and Step 11 after the fixes above):
   - Purges H5317 and its verses
   - Purges G5590 base entry (new purge logic)
   - Inserts H4578 (30 verses) and H5397 (24 verses) as new terms
   - Updates testament_coverage → `both`
   - Updates phase1_term_count and phase1_verse_count

3. Update `word_registry` anchor_verses directly:
   ```sql
   UPDATE word_registry
   SET anchor_verses = 'Gen 2:7; Lev 17:11; Isa 53:10-11; 1 Cor 15:44-46; Matt 10:28'
   WHERE no = 182;
   ```
   This is a researcher judgement call and is not automated.

4. Re-export JSON.

### Out of scope
- MTI cross-reference rebuild (Issue 8)
- `researcher_approved` — manual researcher gate only

---

## Summary: What Makes This Repeatable

| Script | Before | After |
|--------|--------|-------|
| `_discover_word_terms.py` | Only discovers STEP-cluster terms; no way to add H4578/H5397-type terms | `--supplemental-codes` allows researcher to inject codes outside cluster at discovery time |
| `_extract_word_terms.py` | Does not update `testament_coverage` or registry counts; does not purge superseded base entries; does not run flag engine | Fully self-contained: purges base entries, updates all metadata, runs flag engine |
| `engine/audit.py` WR-05 | Flags Phase 2 batch gaps as generic REVIEW | Correctly classifies single contiguous-block gaps as "Phase 2 batch insert — expected" |
| `engine/audit.py` | No anchor_verses check | New check flags missing anchor_verses |
| `audit_word.py` | Designed for 1-term-per-verse model; A3/A4 corrupts Phase 2 junction data | Documented as incompatible with Phase 2 words — A8/A9 logic moved to extraction script |

After these script changes, the complete pipeline for any word is:
```
_discover_word_terms.py --english <word> [--supplemental-codes H1234,G5678]
  → triage.md (researcher fills in)
_apply_term_decisions.py --triage <triage.md>
  → decisions JSON
_extract_word_terms.py --decisions <decisions.json>
  → DB fully synced; metadata updated; flags refreshed
engine.run_audit()   (read-only validation, safe to run any time)
export_word_json.py  → final JSON
```

No `audit_word.py` run required or permitted for words that have gone through Phase 2 extraction.
