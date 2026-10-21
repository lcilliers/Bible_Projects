# Pipeline Design Decisions — Researcher Answers Synthesised

Prepared: 2026-03-23  
Based on: Researcher answers to Q1–Q4  
Status: Design confirmed. Three questions remain before coding begins (bottom of this document).

---

## Answer to Q2 — Supplemental codes: what did the system already know?

The old Session A pipeline (pre-Phase 2) registered H4578 and H5397 against the soul
registry. They are confirmed in the database right now:

| mti_terms.id | strongs_number | gloss         | owning_registry |
|-------------|----------------|---------------|----------------|
| 515         | H4578          | belly         | 182 (soul)     |
| 516         | H5397          | breath        | 182 (soul)     |

These codes are not returned by STEP's cluster for H5315G. They fell through the discovery
gap because the new pipeline did not look at the MTI index before declaring discovery complete.

**Decision:** The pipeline should, after running STEP cluster discovery, query
`mti_terms WHERE owning_registry_fk = ?` to find any codes that were registered in
prior work but absent from the STEP cluster. These are treated as Group G2 include terms
(semantically confirmed by prior researcher work) and extracted alongside cluster-discovered
terms. No command-line argument required — this is automatic for any word with prior MTI data.

Classification for H4578 and H5397:
- H4578 (me'eh, belly/inward parts) — G2, include. Provides somatic grounding for
  inner-being concept. Not etymologically related to NPŠ but part of the soul
  semantic field by researcher confirmation in Session A.
- H5397 (neshamah, breath) — G2, include. Hebrew breath-of-life term (Gen 2:7).
  Connected to the soul concept through the life/breath domain.

---

## Answer to Q1 — Single process, minimal intervention

**What is confirmed:**
- The three scripts (`_discover_word_terms.py`, `_apply_term_decisions.py`,
  `_extract_word_terms.py`) collapse into **one script**.
- The triage document is produced as an **output artifact** for debugging and
  backtracking — not as a gate that must be reviewed before extraction runs.
- Terms that are problematic (root unverified, low verse count, etc.) are
  **imported into the database** and communicated through **data quality flags**,
  not held out of the database.
- Intervention is only required when something goes wrong — the triage output
  shows what decisions were taken so the researcher can inspect and re-run with
  corrections if needed.

**What this means for the three exclusion groups:**

| Group | Current behaviour | New behaviour |
|-------|------------------|---------------|
| G1 — Soul sub-glosses | Include | Include (unchanged) |
| G2 — Confirmed root-family | Include | Include + check MTI index for additional G2 terms |
| G2r — Root unverified | Skip | **Include + ROOT_UNVERIFIED quality flag** |
| G3 — Proper nouns | Exclude | Exclude (unchanged) |
| G4 — Grammatical particles | Exclude | Exclude (unchanged) |
| G5 — Lexically distant noise | Exclude | Exclude (unchanged) |

G2r is the only group that changes. The flag used is `NOTE_ON_ROOT_FAMILY` (existing flag,
group: NOTE, description: "Annotation pertaining to root family relationships").

The flag detail text for a G2r term will be:
`Root consonants of {code} ({transliteration}, {root_note}) differ from the NPŠ root
of {anchor_code} ({anchor_translit}). Included via STEP relatedNos; analytical
relevance requires researcher verification.`

**The single-process script design:**

One command covers everything:
```
python scripts/word_study_extract.py --word soul [--dry-run]
```

Internally this script runs six phases in sequence:

1. **DISCOVER**: Call STEP cluster for anchor codes → collect G1/G2/G2r/G3/G4/G5 candidates.
   Then query `mti_terms WHERE owning_registry_fk = registry_id` → add any codes not already
   in the cluster as G2-MTI terms.

2. **DECIDE**: Apply filters. G3/G4/G5 → excluded. G1/G2/G2-MTI/G2r → include.
   Build the decisions data structure (replaces what `_apply_term_decisions.py` produced).

3. **WRITE TRIAGE**: Write `{word}_triage_{date}.md` to `research/discovery/`. This is a
   complete record of every term considered, the group it was assigned to, the action taken,
   and whether any quality flags will be raised. Produced before DB writes so the researcher
   can inspect it even if the subsequent DB write fails.
   If `--dry-run` is specified, stop here.

4. **EXTRACT**: Full CRUD sync to DB:
   - Purge excluded G3/G4/G5 terms (cascade: junction links → meaning chain → related → root family → inventory)
   - Purge superseded base entries (e.g. G5590 bare lemma superseded by G5590G–K)
   - For each include term: STEP vocab → upsert wa_term_inventory → related words → root family → meaning parser
   - Fetch verse records per code → build deduped verse pool → upsert wa_verse_records → rebuild wa_verse_term_links → delete orphans

5. **METADATA**: After commit:
   - Compute testament distribution from verse records → UPDATE wa_file_index.testament_coverage
   - Count terms and verses from DB → UPDATE word_registry (phase1_term_count, phase1_verse_count, notes, last_automation_run)

6. **FLAGS**: Call run_flag_engine(conn, file_id) to regenerate all derivable quality flags.
   This also creates NOTE_ON_ROOT_FAMILY flags for any G2r terms that were included.

---

## Answer to Q4 — H5317 (honey/nophet)

**Confirmed: import with data quality flag, do not exclude.**

H5317 is included in the database as a G2r term with a `NOTE_ON_ROOT_FAMILY` quality flag.

Flag detail: `Root consonants of H5317 (no.phet, נֹ֫פֶת, dripping/flowing root) differ
from the NPŠ root of H5315G (ne.phesh). Included because STEP relatedNos lists H5317 as
related to H5315G. Analytical connection to the soul concept is not confirmed by etymology.
Researcher should verify whether the 4 honey-dripping verses (Ps 19:10, Prov 5:3, 24:13,
Song 4:11) have relevance to the word study before using them in Session B analysis.`

H5317 remains in the database with its 4 verses. Phase 2 flags will carry the explanation.

---

## Answer to Q3 — Export verse structure

**Confirmed: flat verse list with term association columns.**

The `terms` array in the export no longer contains nested `verses`. Instead, the export
contains a top-level `verses` array — one entry per unique verse record — with:

```json
{
  "_export": {...},
  "registry": {...},
  "terms": [
    {
      "strongs_number": "H5315G",
      "gloss": "soul",
      ...all vocab/meaning/flag data...,
      "verse_count": 230    ← count only, no list
    }
  ],
  "verses": [
    {
      "id": 123,
      "reference": "Gen 1:20",
      "verse_text": "...",
      "testament": "OT",
      "book_id": 1,
      "chapter": 1,
      "verse_num": 20,
      "term_links": [
        { "strongs_number": "H5315G", "step_subgloss_code": "H5315G", "step_subgloss_label": "soul", "span_strong_match": 1 }
      ]
    }
  ]
}
```

Every verse appears exactly once. Its `term_links` array lists every term it belongs to.
A verse that belongs to both H5315G and H5315H will have two entries in `term_links`.
The `statistics` block will include a per-term verse count derived from junction counts,
not from the flat records table.

---

## Revised audit.py (WR checks) — aligned to new design

The following WR checks need updating to match the new single-process design:

**WR-05** (ID gap check):
Change: if exactly one gap and both sub-sequences are themselves contiguous → downgrade
message to "Phase 2 batch insert gap detected (expected)" instead of generic flag.

**WR-07** (terms with zero verses):
Currently flags terms with zero verses that lack an explanatory quality flag.
With G2r terms now included, any G2r term that has zero verses (like G5590K with 1
occurrence) must have a `NOTE_ON_ROOT_FAMILY` or `THIN_DATA` flag. The flag engine
will set this, but WR-07 must recognise `NOTE_ON_ROOT_FAMILY` as a valid explanation
alongside the existing `NO_VERSES` and `SPAN_RESOLUTION_CONFLICT` flags.

**New check** (anchor_verses):
Query `word_registry.anchor_verses WHERE no = ?`. If NULL → REVIEW:
"anchor_verses not set — no anchor texts designated for Session B."

---

## Summary of script changes required

| Script | Change type | What changes |
|--------|------------|------|
| `_discover_word_terms.py` | Replace | Merged into new `word_study_extract.py` Phase 1 |
| `_apply_term_decisions.py` | Replace | Merged into new `word_study_extract.py` Phase 2 |
| `_extract_word_terms.py` | Replace | Merged into new `word_study_extract.py` Phases 4–6 |
| `engine/audit.py` | Edit | WR-05 gap message, WR-07 flag recognition, new anchor_verses check |
| `analytics/word_export.py` | Edit | Flat verse list with term_links; terms show counts only |
| `scripts/export_word_json.py` | No change | Unchanged |

The three old scripts remain in place (archive) but are no longer the canonical pipeline.

---

## Three remaining questions

**RQ-A — Dry-run and triage-only use**

The `--dry-run` flag stops after Phase 3 (triage written, nothing written to DB).
This means the researcher can run:
```
python scripts/word_study_extract.py --word soul --dry-run
```
to see the full triage before committing. If they find an error, they fix the source
data (supplemental codes in MTI, filter thresholds, etc.) and re-run.

Is this sufficient, or do you also need a `--stop-after-extract` option that runs
Phases 1–4 (writes to DB) but stops before metadata and flags? This would be useful
if you want to inspect the DB state before the flag engine marks it as complete.

**RQ-B — New words with no prior MTI history**

The supplemental-code mechanism queries `mti_terms WHERE owning_registry_fk = ?`.
For a brand new word (no prior Session A history), `mti_terms` will be empty → no
supplemental codes → this is correct.

But what if a researcher identifies during the dry-run that a term is missing and wants
to add it before the live run? The options are:
(a) Insert the missing code into `mti_terms` manually before re-running
(b) Pass additional codes via a command-line argument: `--add-codes H4578,H5397`

Option (a) requires knowing the DB. Option (b) is self-documenting in the command.
Which do you prefer?

**RQ-C — audit_word.py guard**

For words that have gone through the new single-process pipeline, running `audit_word.py`
A3/A4 afterwards would corrupt the junction table. Should this be enforced by:
(a) A flag `wa_file_index.phase2_extracted = 1` that `audit_word.py` checks and stops on,
    printing "This word has been extracted via the Phase 2 pipeline. A3/A4 skipped."
    (then continues with A7 read-only audit checks only)
(b) Documentation only

Option (a) makes the system self-protecting. Option (b) relies on the operator knowing
the rule. Given that this is a multi-session project, option (a) is recommended.
