# Word Study Pipeline — Full Design Review

Prepared: 2026-03-23  
Scope: All words (soul is the first to drive the logic)  
Status: For researcher review. No code changes made yet.

---

## How to read this document

Each pipeline stage is described in three sections:
- **What it does now** — the actual behaviour of the current scripts
- **What is missing or wrong** — confirmed gaps found by reading the code and the soul output
- **What it should do** — the clean design rule for ALL future words

A set of questions follows that require your decision before coding begins.

---

## Stage 1 — Pull from STEP

**Script:** `scripts/_discover_word_terms.py`  
**Command:** `python scripts/_discover_word_terms.py --english soul`  
**Outputs:**  
- `data/discovery/soul_term_map_20260323.json` — full machine-readable term data  
- `data/discovery/soul_triage_20260323.md` — researcher decision table

### What it does now

1. Runs an English text search against STEP to find the primary Strong's codes associated with the word (e.g. H5315G, G5590G for "soul").
2. For each primary code, calls STEP's `get_related_term_cluster()` API, which returns:
   - Sub-glosses — translational variants of the same lemma (H5315G through H5315N, G5590G through G5590K)
   - Related terms — terms STEP lists as semantically connected (H5314, H5317, G5591, G1634, etc.)
3. Writes the term_map JSON with all this data.
4. Writes the triage.md — a Markdown table showing every discovered term with columns including `include?` and `notes`. Non-proper-noun terms default to `yes`, proper nouns to `no`.

### What is missing or wrong

**Gap 1 — No mechanism for terms outside the STEP cluster.**  
STEP's relatedNos does not include every analytically relevant term. For soul, H4578 (me'eh, belly/inward parts, 30 verses) and H5397 (neshamah, breath of life, 24 verses) are not returned by STEP's cluster for H5315G. Both existed in the old Session A word study (confirmed in the MTI index). Both have full verse sets in STEP (confirmed by direct API call). The current script has no way to include them. If `_discover_word_terms.py` is re-run for any reason, these terms will never appear.

**Gap 2 — No root-consonant check in the triage output.**  
H5317 (nophet, honey) shares no root consonants with H5315 (nephesh, npsh root). It was listed in STEP's relatedNos for H5315G and came through as a review candidate (G2r). In a prior session it was promoted to `include` in the decisions JSON. Nothing in the triage flagged the root mismatch as a reason for caution. The triage should provide a `root_match` indicator so a researcher reviewing the table can see immediately whether a related term shares the root consonants of the anchor word.

**Gap 3 — The triage.md is a display document only, not an input document.**  
The researcher can fill in `include?` and `notes` in the triage.md. But this fills have no effect on anything. The decisions in the next stage are computed independently from the term_map JSON using algorithmic filters. If a researcher edits the triage.md to change a decision, nothing picks that up. The triage.md is documentation, not a decision input. This is not obvious from the column headings.

### What it should do

- Accept an optional `--supplemental-codes` argument: a comma-separated list of Strong's codes that should be added to the discovery output regardless of STEP cluster membership. Each supplemental code is fetched individually via `get_vocab_info()`, assigned `step_section_type = supplemental`, and placed in its own section in the triage table. Default `include?` = `yes`.
- Add a `root_match` column to the triage table. For related terms (not sub-glosses), compare the consonantal skeleton of the term's transliteration against the anchor's root. Flag mismatches with `⚠` so they stand out during review.
- Clarify the triage.md header to state explicitly that the `include?` column feeds into the decisions step only if the researcher uses `_apply_term_decisions.py --triage` (see Stage 2 below).

---

## Stage 2 — Researcher Triage → Decisions

**Script:** `scripts/_apply_term_decisions.py`  
**Command:** `python scripts/_apply_term_decisions.py --input data/discovery/soul_term_map_20260323.json`  
**Outputs:**  
- `data/discovery/soul_term_decisions_20260323.json` — machine-readable term decisions  
- `data/discovery/soul_term_decisions_20260323.md` — decisions with assigned groups and reasons

### What it does now

Reads the term_map JSON and applies five programmatic filters:
- F1: proper noun → exclude (G3)
- F2: vocab_count above 1000 → exclude (G4, grammatical particle)
- F3: primary code of a non-soul cluster → exclude (G4)
- F4: sub-gloss under a soul anchor → **include** (G1)
- F5: related term under a soul anchor → check root-family confirmation:
  - Greek term with ψ in script → include (G2)
  - Hebrew H5314 (confirmed NPŠ root) → include (G2)
  - All others → **review** (G2r), requires researcher decision

The output JSON lists every term with `action = include | review | exclude` and `decision_group`.

### What is missing or wrong

**Critical gap — Researcher edits to triage.md are not read.**  
The script reads `soul_term_map_{date}.json`, not `soul_triage_{date}.md`. The researcher's edits in the triage (any overrides to `include?`, any notes added) are completely ignored. The decisions JSON is built fresh from the algorithm alone. Any researcher override must then be made by hand-editing the decisions JSON — which is a raw JSON file, not a researcher-friendly format. This is how H5317 came to be included without a status_note: the researcher made a manual edit to the JSON without a mechanism to enforce that an explanatory note must accompany it.

**Gap — G2r (review) terms have no structured resolution step.**  
Review codes need a researcher to decide include/exclude. Nothing in the pipeline forces this decision to be made before Phase 2 runs. The extraction script (`_extract_word_terms.py`) accepts the decisions JSON and runs — it will simply skip any term with `action = review`. There is no warning that unresolved review terms were silently skipped, no summary in the output saying "H5317 was in review and was not extracted."

**Gap — Supplemental codes (added in Stage 1) need to pass through to Stage 2.**  
Once Stage 1 supports `--supplemental-codes`, Stage 2 needs to include those codes in the decisions output with `action = include` and skip the filter logic (they have already been confirmed by the researcher's explicit specification at discovery time).

### What it should do

- Accept a `--triage` argument that reads the researcher's decisions directly from an edited triage.md (parsed from the `include?` column of the Markdown table). The algorithm-derived decisions serve as defaults; any row where the researcher has changed `include?` to `yes`, `no`, or `review` overrides the default.
- Enforce that any G2r term promoted to `include` must have a non-empty `notes` value in the triage table. If the notes column is blank on a promoted term, the script should stop with a clear error: "Term H5317 promoted to include with no explanatory note — add a note before proceeding."
- Write a human-readable summary of review terms that were not resolved: "1 review code (H5317) was not extracted because action=review. Re-run _apply_term_decisions.py with a decision."

---

## Stage 3 — Audit-Mode Update (Extraction)

**Script:** `scripts/_extract_word_terms.py`  
**Command:** `python scripts/_extract_word_terms.py --decisions data/discovery/soul_term_decisions_20260323.json`  
**Outputs:** All writes go directly to `data/bible_research.db`

### What it does now

Reads the decisions JSON and performs a full CRUD sync in 9 steps:

0. Ensure `wa_verse_term_links` table exists  
1. Resolve `file_id` via `word_registry` → `wa_file_index`  
2. Purge excluded terms (cascade: junction links → meaning chain → related words → root family → term inventory)  
3. For each include term: call STEP vocab API → upsert `wa_term_inventory` → replace `wa_term_related_words` → replace `wa_term_root_family` → run meaning parser  
4. Fetch verse records from STEP per term  
5. Clear all junction links for this file  
6. Upsert `wa_verse_records` (keyed on file_id + book_id + chapter + verse_num)  
7. Insert `wa_verse_term_links`  
8. Delete orphaned verse records (no remaining junction links)  
9. Commit  

Researcher-owned fields (`word_analysis_gloss`, `god_as_subject`, `somatic_link`, `status_note`) are preserved on update. `wa_term_phase2_flags` is never touched.

### What is missing or wrong

**Missing — Purge of superseded base entries.**  
The old `audit_word.py` engine inserted G5590 (bare lemma, no sub-gloss suffix) into `wa_term_inventory` before sub-glosses existed. Phase 2 inserted G5590G–K. Nothing removed G5590. It now sits in the DB with 825 `occurrence_count` and 0 verses, which triggers:
- WR-08 (low verse/occurrence ratio)
- WR-19 (parse warnings without NOTE flag)

The purge step (Step 2) only removes terms that appear in the decisions JSON with `action ≠ include`. G5590 does not appear in the decisions JSON at all (it was not discovered by the current script), so it is never purged. The extraction script needs logic to detect and remove any old bare-lemma entries that have been superseded by their sub-glosses.

**Missing — Metadata updates after commit.**  
After the commit, the following fields are NOT updated:
- `wa_file_index.testament_coverage`: still says `OT_only` even after NT terms are inserted
- `word_registry.phase1_term_count`: still says 11
- `word_registry.phase1_verse_count`: still says 694
- `word_registry.notes`: still says "4 terms (4 extracted)"

These updates live in `audit_word.py` steps A8 and A9. But `audit_word.py` is fundamentally incompatible with the Phase 2 pipeline (see the note on audit_word.py below) and must not be run after Phase 2 extraction. There is therefore no mechanism to update these fields.

**Missing — Quality flag refresh after commit.**  
`_extract_word_terms.py` does not call the flag engine after completion. Quality flags are the mechanism used by WR-07, WR-08, WR-17, and WR-19 audit checks. Without a flag engine run after extraction, quality flags from the previous pipeline run remain stale.

**Missing — Anchor verses.**  
`word_registry.anchor_verses` is never written by any automated script. There is also no audit check that flags its absence. For soul it is `NULL`.

**Missing — Review term summary.**  
The extraction script prints no warning when terms with `action = review` in the decisions JSON are silently skipped. The researcher does not know that H5317 was not extracted.

### What it should do

After the existing 9-step commit, add:

**Step 10 — Purge superseded base entries.**  
For each include term that has a sub-gloss suffix (e.g. G5590G), derive its base code (G5590). If the base code exists in `wa_term_inventory` for this `file_id` and is NOT in the include list, cascade-delete it. This handles all cases where an old engine run inserted a bare lemma that the Phase 2 sub-gloss architecture has now superseded.

**Step 11 — Metadata update.**  
After commit:
- Compute testament distribution from the inserted verse records → `UPDATE wa_file_index SET testament_coverage = ?`
- Count terms and verses from the DB (not from the decisions JSON, which is pre-dedup) → `UPDATE word_registry SET phase1_term_count = ?, phase1_verse_count = ?, last_automation_run = ?`
- Update `word_registry.notes` to reflect the actual term count

**Step 12 — Flag engine refresh.**  
Call `run_flag_engine(conn, file_id)` so that quality flags are regenerated against the updated DB state, including SPAN_RESOLUTION_CONFLICT flags for terms with low verse/occurrence ratios.

**Additional: Review term warning.**  
Before returning, print a clearly visible warning listing any terms from the decisions JSON that had `action = review` and were therefore skipped, with their verse counts.

---

## Note on audit_word.py

`audit_word.py` was designed for the old 1-term-per-verse model. Its apply phase (A3/A4) fetches verses per `term_inv_id` and reconciles using `WHERE term_inv_id = ?`. The Phase 2 model uses a shared verse pool with junction links. Running A4 after Phase 2 extraction would:
- Find zero existing verses for sub-gloss terms (H5315H–N, G5590H–K) because those verses are stored under H5315G's or G5590G's `term_inv_id`
- Attempt to INSERT them as new rows → integrity errors or duplicates
- Delete `wa_verse_term_links` rows as "obsolete" verses → destroy the junction table
- Never rebuild `wa_verse_term_links` (it doesn't know the table exists)

**Rule for ALL Phase 2 words: `audit_word.py` A3/A4 must never be run after `_extract_word_terms.py` has committed.** The metadata steps that audit_word.py provides (A8, A9) must instead be performed inside `_extract_word_terms.py` (Stage 3, Steps 11 above). The audit checks (A7 = WR-01 through WR-20) are read-only and safe to run at any time.

---

## Stage 4 — Export

**Script:** `analytics/word_export.py` (called by `scripts/export_word_json.py`)  
**Command:** `python scripts/export_word_json.py --registry=182 --pretty --out=data/exports`  
**Output:** `data/exports/Soul_182_full_{date}.json`

### What it does now

Exports all DB data for a registry to a structured JSON:
- Registry header, file index, run history
- Per-term: vocab data, meaning (senses + stems), LSJ entry, quality flags, phase2 flags, related words, root family, MTI cross-refs, verses
- Each verse includes a `term_links` array from `wa_verse_term_links`
- Statistics block

### What is missing or wrong

**Export gap — Verses are bucketed by primary `term_inv_id`, not by junction membership.**  
The export queries `wa_verse_records WHERE term_inv_id IN (all_ti_ids)` and groups the results by `term_inv_id`. In Phase 2, a verse's `term_inv_id` is set to whichever include term first encountered it during extraction (in the include list order). For shared verses between sub-glosses, H5315G (first in the list) is set as primary. In the export, H5315H's `verses` array therefore contains only the verses unique to H5315H — not the full 180 that it genuinely covers, which includes all the shared verses.  

The full junction-based membership is available through the `term_links` array on each verse, but it requires reading the data at verse level, not term level. A researcher building a Session B analysis expects to see all nephesh:life verses under the nephesh:life term.

**Missing — MTI cross-references for Phase 2 terms.**  
24 of 27 soul terms have no MTI cross-reference entries. The old engine populated `mti_terms` for the 4 terms it knew about (H5315, H4578, H5397, G5590). The 23 new Phase 2 terms were never registered. The MTI rebuild is a separate pass and is out of scope for this fix batch, but the export currently shows `"mti": null` for the majority of terms with no explanation.

### What it should do

The verse-bucketing issue can be resolved by changing the query that builds `vr_by_ti`. Instead of bucketing verses by `wa_verse_records.term_inv_id`, the export should bucket verses by `wa_verse_term_links.term_inv_id` — i.e., for each term, find all verses linked to it via the junction table, not just the verses it "owns" in the flat records table.

This means every H5315 sub-gloss will show all its junction-linked verses. The same verse may appear in multiple terms' `verses` arrays (for the 9 multi-term verses). This reflects the reality of the data.

**Open question:** Do you want the `verses` array under each term to show the full junction-linked set (each verse may appear under multiple terms), or the unique set only (each verse under exactly one term, the junction table available as secondary lookup)? The multi-term architecture makes this a design choice about how Session B works.

---

## Complete Pipeline — Clean Design

```
Stage 1   _discover_word_terms.py  --english <word>
                                   [--supplemental-codes H4578,H5397]
          ↓
          {word}_term_map_{date}.json           (machine data, not edited)
          {word}_triage_{date}.md               (researcher fills in include? and notes)

Stage 2   _apply_term_decisions.py --triage {word}_triage_{date}.md
          ↓
          {word}_term_decisions_{date}.json      (machine decisions, drives extraction)
          {word}_term_decisions_{date}.md        (human-readable decisions summary)

          Rules enforced at Stage 2:
          • G2r term promoted without a notes entry → STOP with error
          • Unresolved review terms → printed as WARNING in summary

Stage 3   _extract_word_terms.py  --decisions {word}_term_decisions_{date}.json
          ↓
          DB fully synced (CRUD, including purge of superseded base entries)
          testament_coverage updated
          word_registry counts updated
          Quality flags refreshed
          Review terms that were skipped → printed as WARNING

Stage 4   export_word_json.py --registry=<no> --out=data/exports
          ↓
          {Word}_{no}_full_{date}.json
          Verses bucketed by junction membership (all linked verses per term)
```

`audit_word.py` read-only audit checks (WR-01 through WR-20) can be run at any point
after Stage 3 as a validation pass. A3/A4 (write operations) must never be run after
Stage 3 has completed.

---

## Questions requiring your decision before coding begins

**Q1 — Researcher decision mechanism in Stage 2**  
Currently `_apply_term_decisions.py` reads the term_map JSON and re-computes decisions algorithmically, ignoring anything in the triage.md. The proposed design changes it to read the researcher's `include?` and `notes` columns from the triage.md to produce the decisions JSON.

Should the researcher's decisions travel in the triage.md (as edited markdown), or in a separate overrides JSON file (more robust to formatting errors but less user-friendly)?

**Q2 — Supplemental codes: where are they specified?**  
For words where relevant terms are not in the STEP cluster (like H4578 and H5397 for soul), should supplemental codes be:  
(a) Specified on the command line when running Stage 1 (`--supplemental-codes H4578,H5397`)  
(b) Written by hand into the triage.md before running Stage 2  
(c) A separate per-word config entry in the database (`word_registry` table)

Option (a) is simplest and most explicit. Option (c) would survive re-discovery runs.

**Q3 — Export verse bucketing**  
When a verse is associated with multiple terms (e.g. Lev 17:11 linked to both H5315G and H5315H), should the `verses` array under each term in the export show:  
(a) All verses linked to that term via the junction table (verse appears under every term it belongs to)  
(b) Only the verses where that term is the primary `term_inv_id` (current behaviour, each verse under exactly one term)

Option (a) is more useful for Session B analysis but causes the same verse text to appear under multiple terms in the JSON.

**Q4 — H5317 (honey) disposition**  
H5317 is currently in the DB as an include term with 4 verses. It should be excluded based on root mismatch (nophet root ≠ nephesh root). Do you confirm this is to be removed, and are you comfortable removing it from the soul study entirely?

**Q5 — anchor_verses**  
The proposed anchor verses for soul are:  
`Gen 2:7; Lev 17:11; Isa 53:10-11; 1 Cor 15:44-46; Matt 10:28`

Do you confirm these five, or would you like to add, remove, or amend any?

**Q6 — audit_word.py post-Phase-2 rule**  
For any word that has been through Phase 2 extraction, `audit_word.py` A3/A4 must never run again. Should this be enforced by:  
(a) A flag in `wa_file_index` (e.g. `phase2_extracted = 1`) that `audit_word.py` checks and stops on  
(b) Documentation only (relying on workflow discipline)

**Q7 — MTI cross-references**  
24 of 27 soul terms have no MTI entries. Is the MTI rebuild (adding all Phase 2 terms to `mti_terms` and computing cross-registry links) something to include in the Phase 3 extraction script as a standard step for all words, or is it a separate project to be done when the corpus of extracted words is larger?
