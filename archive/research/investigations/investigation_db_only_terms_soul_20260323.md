# Investigation: DB_ONLY Terms — H4578, H5397, G5590
**Word:** Soul (registry 182) | **Date:** 2026-03-23  
**Status:** Root cause confirmed. Fix required in `scripts/word_study_extract.py`.

---

## 1. What audit_word.py reported

The audit run on 2026-03-23 (RUN-20260323_202200-AUDIT_WORD) classified three terms
as **DB_ONLY_TERM** — meaning they exist in `wa_term_inventory` for file_id=36 but are
not present in the Step 1 JSON `include_codes` list. The audit applied the DB_ONLY logic
and set `delete_flagged=1` on all three.

| Reported | Code | DB_ONLY consequence |
|---|---|---|
| H4578 | meʾeh / belly | `delete_flagged=1` — flagged for archive |
| H5397 | nᵉšāmāh / breath | `delete_flagged=1` — flagged for archive |
| G5590 | psychē / soul (bare lemma) | `delete_flagged=1` — flagged for archive |

---

## 2. What is in the database for these terms

### H4578 — meʾeh (belly / inward parts)

**wa_term_inventory**
| Field | Value |
|---|---|
| id | 490 |
| file_id | 36 (soul) |
| step_search_gloss | belly |
| word_analysis_gloss | belly |
| transliteration | me.eh |
| language | Hebrew |
| occurrence_count | **32** |
| testament | OT |
| delete_flagged | **1** (set by this audit run) |

**wa_verse_term_links:** 0 rows  
**Active linked verses:** 0  
**wa_term_root_family:** 1 row  
**wa_term_related_words:** 3 rows

**mti_terms**
| Field | Value |
|---|---|
| id | 515 |
| gloss | belly |
| owning_registry | 182 |
| owning_registry_fk | 182 |
| extraction_date | NULL |
| status | extracted |

**wa_data_quality_flags** (2 flags)
| Flag | Group | Detail |
|---|---|---|
| NO_VERSES | DATA_COVERAGE | Zero confirmed verse records for H4578. |
| NO_WORD_ANALYSIS | DATA_COVERAGE | meaning field is null for H4578. STEP returned no word analysis block for this term. |

---

### H5397 — nᵉšāmāh (breath / breath of life)

**wa_term_inventory**
| Field | Value |
|---|---|
| id | 491 |
| file_id | 36 (soul) |
| step_search_gloss | breath |
| word_analysis_gloss | breath |
| transliteration | ne.sha.mah |
| language | Hebrew |
| occurrence_count | **24** |
| testament | OT |
| delete_flagged | **1** (set by this audit run) |

**wa_verse_term_links:** 0 rows  
**Active linked verses:** 0  
**wa_term_root_family:** 1 row  
**wa_term_related_words:** 2 rows

**mti_terms**
| Field | Value |
|---|---|
| id | 516 |
| gloss | breath |
| owning_registry | 182 |
| owning_registry_fk | 182 |
| extraction_date | NULL |
| status | extracted |

**wa_data_quality_flags** (2 flags)
| Flag | Group | Detail |
|---|---|---|
| NO_VERSES | DATA_COVERAGE | Zero confirmed verse records for H5397. |
| NO_WORD_ANALYSIS | DATA_COVERAGE | meaning field is null for H5397. STEP returned no word analysis block for this term. |

---

### G5590 — psychē (soul, bare base lemma)

**wa_term_inventory**
| Field | Value |
|---|---|
| id | 493 |
| file_id | 36 (soul) |
| step_search_gloss | soul |
| word_analysis_gloss | soul |
| transliteration | psychē |
| language | Greek |
| occurrence_count | **825** |
| testament | NT |
| delete_flagged | **1** (set by this audit run) |

**wa_verse_term_links:** 0 rows  
**Active linked verses:** 0  
**wa_term_root_family:** 1 row  
**wa_term_related_words:** 0 rows

**mti_terms**
| Field | Value |
|---|---|
| id | 517 |
| gloss | soul |
| owning_registry | 182 |
| owning_registry_fk | 182 |
| extraction_date | NULL |
| status | extracted |

**wa_data_quality_flags** (3 flags)
| Flag | Group | Detail |
|---|---|---|
| HIGH_FREQUENCY_ANCHOR | DATA_COVERAGE | High-frequency term: 825 occurrences. Verse sample represents a subset of all occurrences. |
| NO_VERSES | DATA_COVERAGE | Zero confirmed verse records for G5590. |
| NO_WORD_ANALYSIS | DATA_COVERAGE | meaning field is null for G5590. STEP returned no word analysis block for this term. |

---

## 3. What is in the Step 1 JSON extraction

**File:** `data/discovery/182_soul_step_data_20260323.json`  
**Generated:** 2026-03-23  
**STEP version:** ESV_th  
**Anchors given to extraction:** `H5315G`, `G5590G`  
**Total terms evaluated:** 26  
**Include codes (24):** H5315G, H5315H, H5315I, H5315J, H5315K, H5315L, H5315M, H5315N, H5317, H5314, G5590G, G5590H, G5590I, G5590J, G5590K, G5591, G1634, G1374, G0674, G0895, G2174, G2473, G3642, G4861  
**Exclude codes (2):** H5305, H5320

**Search result for H4578, H5397, G5590 in the `terms[]` array:**

> **RESULT: NOT FOUND — none of these three codes appear anywhere in the `terms[]` array.
> They are not excluded. They are not included. They were never generated.**

Full term list from the JSON:
| Code | Group | Action | Section type | Gloss |
|---|---|---|---|---|
| H5315G | G1 | include | primary | soul |
| H5315H | G1 | include | sub_gloss | soul: life |
| H5315I | G1 | include | sub_gloss | soul: myself |
| H5315J | G1 | include | sub_gloss | soul: person |
| H5315K | G1 | include | sub_gloss | soul: animal |
| H5315L | G1 | include | sub_gloss | soul: appetite |
| H5315M | G1 | include | sub_gloss | soul: dead |
| H5315N | G1 | include | sub_gloss | soul: neck |
| H5317 | G2r | include | related_term | honey |
| H5305 | G3 | exclude | related_term | Naphish |
| H5314 | G2 | include | related_term | be refreshed |
| H5320 | G3 | exclude | related_term | Naphtuhim |
| G5590G | G1 | include | primary | soul |
| G5590H | G1 | include | sub_gloss | soul: life |
| G5590I | G1 | include | sub_gloss | soul: myself |
| G5590J | G1 | include | sub_gloss | soul: person |
| G5590K | G1 | include | sub_gloss | soul: animal |
| G5591 | G2 | include | related_term | natural |
| G1634 | G2 | include | related_term | to expire |
| G1374 | G2 | include | related_term | double-minded |
| G0674 | G2 | include | related_term | to faint |
| G0895 | G2 | include | related_term | lifeless |
| G2174 | G2 | include | related_term | be glad |
| G2473 | G2 | include | related_term | like-minded |
| G3642 | G2 | include | related_term | fainthearted |
| G4861 | G2 | include | related_term | harmonious |

---

## 4. Why these terms were not processed — root cause analysis

### 4a. H4578 and H5397 — not returned by STEP

`word_study_extract.py` discovers terms **exclusively through STEP's `relatedNos` cluster API**.
The script calls `get_related_term_cluster()` for each anchor code. STEP's cluster for H5315G
does **not** include H4578 or H5397 in its `relatedNos` list. Because these codes are never
returned by the cluster, they never enter the script's `seen_codes` set, never get a `terms[]`
record, and never appear in the JSON.

There is **no mechanism in `word_study_extract.py` to consult the database** (the script
docstring states explicitly: "No DB reads. No DB writes."). This means the script has no way
to discover that the researcher registered H4578 and H5397 against the soul registry in the
prior Session A pipeline. These registrations sit in `mti_terms` (rows 515 and 516,
`owning_registry_fk=182`) and are completely ignored during extraction.

`docs/pipeline_design_review_20260323.md` (Stage 1, Gap 1) documented this in full:

> *STEP's relatedNos does not include every analytically relevant term. For soul, H4578
> (me'eh, belly/inward parts, 30 verses) and H5397 (neshamah, breath of life, 24 verses)
> are not returned by STEP's cluster for H5315G. Both existed in the old Session A word
> study (confirmed in the MTI index). Both have full verse sets in STEP (confirmed by direct
> API call). The current script has no way to include them.*

`docs/pipeline_decisions_20260323.md` confirmed the fix design:

> *The pipeline should, after running STEP cluster discovery, query
> `mti_terms WHERE owning_registry_fk = ?` to find any codes that were registered in
> prior work but absent from the STEP cluster. These are treated as Group G2 include terms
> (semantically confirmed by prior researcher work) and extracted alongside cluster-discovered
> terms.*

Neither the fix nor the `--supplemental-codes` workaround was ever coded into
`word_study_extract.py`. The design decision was documented but implementation did not follow.

### 4b. G5590 — superseded base lemma, different problem

G5590 is a different category of problem. It is **not** a missing STEP term — it is a
legacy artefact from the old engine.

The old Session A pipeline registered G5590 (bare *psychē* lemma, 825 occurrences) before
the sub-gloss architecture existed. When Phase 2 was designed, STEP's cluster for G5590G
returned sub-glosses G5590G through G5590K — these become the correct include terms
(`step_section_type=sub_gloss`).

The bare G5590 base lemma was **never purged** from `wa_term_inventory` after the sub-glosses
were created. Nothing in the pipeline design detects or handles this. From the extraction
script's point of view, G5590 is simply another code it never discovers (because the
anchor given was `G5590G`, not the bare `G5590`). From `audit_word.py`'s point of view,
G5590 is a DB row with a code not in `include_codes` — a `DB_ONLY_TERM`.

`docs/pipeline_design_review_20260323.md` (Stage 1, paragraph on G5590) confirmed:

> *G5590 bare lemma — old engine issue. Nothing removed it. It never appears in
> the decisions JSON so it was never purged through the decisions pathway.*

The fix for G5590 is not the same as for H4578/H5397. G5590 should **not** be included
as an active term — the sub-glosses G5590G–K are the correct terms. But it should be
detected as a "superseded base lemma" rather than treated as an unexpected DB_ONLY term
that requires researcher decision about deletion. The deletion of G5590 is correct;
the classification needs to be transparent.

---

## 5. Summary of what is wrong and what needs to be fixed

| Term | Category | Root cause | Correct outcome | Fix location |
|---|---|---|---|---|
| H4578 | Should be a tracked include term | `word_study_extract.py` never queries `mti_terms` — only uses STEP cluster, which does not return H4578 | Include as G2 term; fetch verses from STEP; no deletion | `word_study_extract.py` — add MTI supplemental lookup after STEP cluster discovery |
| H5397 | Should be a tracked include term | Same as H4578 | Include as G2 term; fetch verses from STEP; no deletion | `word_study_extract.py` — same fix |
| G5590 | Superseded base lemma, correct to remove | Old engine registered bare G5590 before sub-gloss architecture; never purged; not wrong to delete, but wrong classification | Classify as `SUPERSEDED_BASE_LEMMA`, delete automatically — not as `DB_ONLY_TERM` requiring researcher decision | `word_study_extract.py` — detect superseded base lemmas; `engine/audit_word.py` — handle new category |

---

## 6. Current DB impact

All three terms currently have `delete_flagged=1` in `wa_term_inventory`.  
H4578 and H5397 have `mti_terms` rows (`owning_registry_fk=182`) confirming they are
registered to this word study and should not be deleted.

**H4578 and H5397 must be unflagged (`delete_flagged=0`) before the next audit run.**
If left flagged and a cleanup pass runs, their `mti_terms` rows, root family rows,
and related word rows will be purged. Once the extraction script is fixed, these
terms need fresh verse records fetched from STEP (they currently have 0 verses because
the old pipeline never fetched them either).

**G5590 deletion is the correct eventual outcome**, but the DB record should be
retained until the fixed extraction script writes `G5590` into a `superseded_codes`
list in the JSON meta and `audit_word.py` handles it as a classified supersession
rather than an unexplained DB_ONLY term.

---

## 7. Required code changes (not yet implemented)

| Script | Change |
|---|---|
| `scripts/word_study_extract.py` | After Phase 2 cluster discovery, query `mti_terms WHERE owning_registry_fk = <registry_id>`. For each code not already in the cluster, call `get_vocab_info()`, build a term entry with `step_section_type="mti_supplemental"`, `decision_group="G2"`, `action="include"`. These enter Phase 5 (verse fetch) as normal. |
| `scripts/word_study_extract.py` | After Phase 4 (filters applied), scan include_codes for sub-gloss suffix pattern (`[HG]\d+[A-Z]$`). Derive base code (e.g. `G5590G` → `G5590`). Query `wa_term_inventory` for that base code under this file_id. If found but NOT in include_codes, write base code to `meta.superseded_codes`. |
| `engine/audit_word.py` | In A4 (DB_ONLY detection), check if a DB_ONLY code appears in `meta.superseded_codes`. If so, classify as `SUPERSEDED_BASE_LEMMA` (auto-approve deletion, no researcher prompt) rather than `DB_ONLY_TERM`. |

**Before these changes are implemented, the urgently required manual action is:**  
Unflag H4578 and H5397 (`delete_flagged=0`) in `wa_term_inventory` to prevent
accidental deletion in any cleanup pass.
