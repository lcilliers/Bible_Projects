# Anger Word Study — Session Log
**Registry:** 4 | **AUDIT_WORD run:** RUN-20260324_070256-AUDIT_WORD  
**Extract file:** `data/discovery/004_anger_step_data_20260323.json`  
**Export file:** `data/exports/anger_4_full_20260324.json`

---

## INV-001 | H2734 — Term Status Investigation

**Question posed:** Is H2734 in the extract? Is it in the report? What is the actual data around this term?

---

### 1. H2734 in the Extract

**File:** `data/discovery/004_anger_step_data_20260323.json`

- H2734 is **NOT** present in `meta.include_codes`
- H2734 is **NOT** present in `meta.exclude_codes`
- H2734 does appear 20+ times in the raw JSON text, but **exclusively** inside verse preview HTML — as a co-occurring `strong='H2734'` morphological tag within the verse span records fetched for H0639G
- H2734 was **never evaluated as a standalone term** by `word_study_extract.py` in this extract run. It entered the extract data only as incidental verse markup.

**Implication:** `word_study_extract.py` did not request, retrieve, or include H2734 as a search target on 2026-03-23. Its presence in the DB at the time of this AUDIT_WORD run was entirely from Session A (2026-03-16).

---

### 2. H2734 in the Export Report

**File:** `data/exports/anger_4_full_20260324.json`

H2734 is present in the export in two locations:

**2a. `registry.strongs_list`**
- Appears with `{"strong": "H2734", "count": 88}`
- This list reflects all terms in the DB for registry 4, including delete_flagged entries

**2b. `terms[]` array (line ~26848)**

| Field | Value |
|---|---|
| `term_id` | H2734 |
| `strongs_number` | H2734 |
| `transliteration` | cha.rah |
| `step_search_gloss` | to be incensed |
| `word_analysis_gloss` | to be incensed |
| `meaning` | **null** |
| `occurrence_count` | 91 (qualifier: "about") |
| `testament` | OT_only |
| `god_as_subject` | 1 |
| `somatic_link` | 1 |
| `causative_form_present` | 1 |
| `delete_flagged` | **1** |
| `last_changed` | 2026-03-16 11:32:38 |

**Quality flags in export:**
- `NO_WORD_ANALYSIS` (DATA_COVERAGE): "meaning field is null for H2734. STEP returned no word analysis block for this term."

**Phase2 flags in export:**
- `CAUSATIVE_OF_INNER_STATE` — explicit causative grammatical form present (Hiphil)
- `GOD_AS_SUBJECT` — God is subject in at least one meaning or verse
- `SOMATIC_INNER_LINK` — connected to a bodily organ or physical process as its seat

**meaning_parsed in export:** Senses ARE present (populated from Session A — source is not STEP word_analysis block):
- 1. to be hot, furious, burn, become angry, be kindled
  - 1a. (Qal) to burn, kindle (anger)
  - 1b. (Niphal) to be angry with, be incensed
  - 1c. (Hiphil) to burn, kindle
  - 1d. (Hithpael) to heat oneself in vexation

**related_words in export (4 rows — all `delete_flagged=0`):**
| transliteration | gloss |
|---|---|
| cha.ron | burning anger |
| cho.ri | burning |
| cha.rar | to scorch |
| ta.cha.rah | to contend |

**root_family in export (1 row — `delete_flagged=1`):**
- `root_code`: CHAR

**Verse records in export:** 88 verse records  
**Verse term links:** `"term_links": []` (empty on all verse records)

---

### 3. DB Actual Data

**Queries run:** `scripts/query_h2734.py`

#### wa_term_inventory (id=41)
```
strongs_number:          H2734
transliteration:         cha.rah
step_search_gloss:       to be incensed
word_analysis_gloss:     to be incensed
occurrence_count:        91 (about)
meaning:                 null
testament:               OT_only
god_as_subject:          1
somatic_link:            1
causative_form_present:  1
delete_flagged:          1
status_note:             null
last_changed:            2026-03-16 11:32:38
```

#### wa_data_quality_flags
- 1 flag: `NO_WORD_ANALYSIS` (group: DATA_COVERAGE)
- Description: "meaning field is null for H2734. STEP returned no word analysis block for this term."

#### wa_verse_records
- **Count: 88** (versus `occurrence_count=91 ("about")` in wa_term_inventory — a discrepancy of 3)

#### wa_meaning_parsed (id=2343)
```
strongs_number:   "" (empty string — should be "H2734")
language:         Hebrew
top_sense_count:  1
stem_count:       0
has_causative_stem: 1
has_domain_tags:  0
parsed_at:        2026-03-24T07:03:16
parse_version:    1.0.0
parse_warnings:   null
```
Note: `strongs_number` field is empty string, not "H2734". The senses data was parsed at 07:03:16 on 2026-03-24 (during the AUDIT_WORD run), but the source `meaning` field is null.

#### wa_term_root_family (id=34)
```
root_code:      CHAR
root_language:  null
root_gloss:     null
note:           null
delete_flagged: 1
```
The root_family entry itself carries `delete_flagged=1` — it was soft-deleted along with the term.

#### wa_term_related_words (4 rows)
All 4 related_words rows have `delete_flagged=0` — they were NOT soft-deleted along with the parent term.

| id | transliteration | gloss | strongs_number | delete_flagged |
|---|---|---|---|---|
| 151 | cha.ron | burning anger | null | 0 |
| 152 | cho.ri | burning | null | 0 |
| 153 | cha.rar | to scorch | null | 0 |
| 154 | ta.cha.rah | to contend | null | 0 |

All 4 related_words have `strongs_number=null` — they have glosses and transliterations but no Strong's references.

#### mti_terms (id=139)
```
strongs_number:       H2734
transliteration:      cha.rah
gloss:                to be incensed
language:             Hebrew
owning_registry:      4
owning_word:          anger
status:               extracted
strongs_reconciled:   0
last_changed:         2026-03-16 10:34:12
```
`status="extracted"` — was extracted in Session A.  
`strongs_reconciled=0` — Strong's number has not been reconciled.

---

### 4. Data Origin Timeline

| Date | Event |
|---|---|
| 2026-03-16 10:34:12 | `mti_terms` row created — H2734 registered in MTI during Session A |
| 2026-03-16 11:32:38 | `wa_term_inventory` row created — H2734 data imported in Session A |
| 2026-03-23 | Extract `004_anger_step_data_20260323.json` generated — H2734 **not included** in `include_codes` |
| 2026-03-24 07:03:16 | AUDIT_WORD run — A4 identifies H2734 as DB_ONLY_TERM; A6 sets `delete_flagged=1`; meaning_parser runs on null meaning (produces senses but `strongs_number` field left empty) |

---

### 5. Observations (factual only — no recommendations)

1. **Extract absence:** H2734 was present in the DB before the extract was made. The extract does not include it. Its presence in the extract JSON is only incidental (verse HTML co-occurrence within H0639G's records).

2. **Soft-delete scope inconsistency:** `wa_term_inventory.delete_flagged=1` and `wa_term_root_family.delete_flagged=1`, but all 4 `wa_term_related_words` rows have `delete_flagged=0`. The soft-delete in A6 did not propagate to the related_words child rows for H2734.

3. **Occurrence count discrepancy:** `wa_term_inventory.occurrence_count=91 ("about")` vs 88 actual verse records in `wa_verse_records`. This is a 3-record gap. The `occurrence_count` was sourced from STEP metadata in Session A; the 88 loaded verses are what was actually stored.

4. **meaning_parsed.strongs_number empty:** The `wa_meaning_parsed` row (id=2343) has `strongs_number=""` (empty string). The meaning was parsed during the AUDIT_WORD run from a null source field (no STEP word analysis block), so senses were populated by the parser but the strongs_number field was written as empty.

5. **Verse term links empty:** In the export, all 88 H2734 verse records show `"term_links": []`. The `wa_verse_term_links` junction table has no entries for H2734's verses.

6. **Phase2 flags retained on delete_flagged term:** The 3 phase2 flags (CAUSATIVE_OF_INNER_STATE, GOD_AS_SUBJECT, SOMATIC_INNER_LINK) are still present and attached to this term despite `delete_flagged=1`.

7. **No STEP word analysis:** The `NO_WORD_ANALYSIS` quality flag indicates STEP did not return a word analysis block for H2734 when it was originally fetched in Session A. The senses in `wa_meaning_parsed` were parsed from BDB or another source available at that time, not from STEP's word analysis block.

---

*End of INV-001*

---

## INV-002 | H2734 — Re-extract Result

**Action taken:** Re-ran `word_study_extract.py --word anger` on 2026-03-24 to produce a fresh extract `004_anger_step_data_20260324.json`.

**Old extract:** `data/discovery/004_anger_step_data_20260323.json` — 164 include / 65 exclude  
**New extract:** `data/discovery/004_anger_step_data_20260324.json` — 164 include / 65 exclude

**H2734 in new `include_codes`:** No  
**H2734 in new `exclude_codes`:** No  
**H2734 evaluated as a term in Phase 4:** No

**Why:** The extract auto-detects anchors via `client.get_strongs_for_word("anger")`. This STEP text search returned 26 codes — H2734 was not among them. H2734 therefore never became an anchor, and it is not present as a `related_term` in any cluster that was evaluated. It is present in verse preview HTML only (as a co-occurring morph tag within H0639G verses), same as in the old extract.

The new extract is otherwise identical in structure and term count to the old extract. No comparison has been run — awaiting researcher approval.

*End of INV-002*
