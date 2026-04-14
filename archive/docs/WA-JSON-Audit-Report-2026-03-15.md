# Session A JSON Audit Report
**Date:** 2026-03-15  
**Files audited:** 8  
**Standard applied:** Session A Instruction v7 / Schema v2.3

---

## Summary Table

| File | Word | Reg | Schema | Spec | Structure | Issues |
|------|------|-----|--------|------|-----------|--------|
| WA-004-anger-data-2026-03-06__1_.json | anger | 4 | none | none | v1.x — non-standard | 15 |
| WA-072-grief-data-2026-03-05__1_.json | grief | 72 | 1.0 | WA-Phase1-Spec V2 | v1.x — non-standard | 15 |
| WA-051-Distress-data-2026-03-07.json | distress | 051 | none | none | v1.x — non-standard | 15 |
| WA-006-anointing-data-2026-03-08.json | anointing | 006 | 2.2 | v4 | v2.x — current family | 4 |
| WA-071-grief-data-part2-2026-03-08-updated.json | grief | 071 | 2.3 | v5 | v2.x — current family | 3 |
| WA-146-shame-data-part2-2026-03-12.json | shame | 146 | 2.3 | v6 | v2.x — current family | 0 |
| WA-117-peace-data-part1-2026-03-13.json | peace | 117 | none | v7 | custom flat — non-standard | 15 |
| WA-043-desire-data-part2-2026-03-14.json | desire | 043 | 2.3 | v7 | v2.x — current family | 29 |

**Clean (0 issues):** 1 file (shame part 2)  
**Minor issues:** 2 files (anointing, grief part 2)  
**Significant issues:** 2 files (desire part 2)  
**Non-standard schema — not comparable to v7:** 4 files (anger, grief v1, distress, peace part 1)

---

## Schema Generations Present

Three distinct schema generations are in this set of 8 files:

**Generation 1 — v1.x (pre-v4 spec, March 2026-03-05 to 2026-03-07)**  
Files: anger, grief_v1, distress  
Structure: `word_identity` + `term_inventory` (list) + `verse_classification` (dict or list). No `meta` block. No `term_inventory_hebrew` / `term_inventory_greek` split. No `verse_records` array. Verses stored in a separate classification structure keyed by transliteration.

**Generation 2 — v2.x (v4–v7 spec, from 2026-03-08)**  
Files: anointing, grief part 2, shame part 2, desire part 2  
Structure: `meta` + `term_inventory_hebrew` + `term_inventory_greek` + `verse_records`. This is the current target structure.

**Generation 3 — peace custom (v7 spec but non-standard structure, 2026-03-13)**  
Files: peace part 1  
Structure: flat top-level keys (`registry`, `word`, `part`, `terms`). Terms have verses embedded within them. No `meta` block using the v7 schema. Uses v7 spec but is structurally incompatible with every other file.

---

## Detailed Issues by File

### anger / grief_v1 / distress (v1.x schema)

All three share the same structural issues against the v7 standard:

**Structural (applies to all three):**
- No `meta` block — word, registry_id, schema_version, specification, testament_coverage, is_split, part_number, root_families_in_prior_parts all absent at top level
- Registry IDs not zero-padded (anger=`4`, grief=`72` vs current standard `004`, `071`)
- No `term_inventory_hebrew` / `term_inventory_greek` split — single flat list
- No `verse_records` array — verses in `verse_classification` keyed by transliteration

**Term-level fields absent (all three):**
- `term_id` — absent; terms not individually addressable by ID
- `step_search_gloss` — absent; anchor_gloss used instead
- `step_search_flag` — absent
- `word_analysis_gloss` — absent
- `meaning` — absent; `meaning_summary` used instead (different name)
- `meaning_numbered` — absent
- `occurrence_count_qualifier` — absent
- `related_words` — absent
- `also_spelled` — absent
- `root_family` — absent
- `testament` — absent
- `god_as_subject` — absent; `divine_subject_possible` used instead (different name, different boolean intent)
- `somatic_link` — absent; `somatic_dimension` used instead (different name)
- `causative_form_present` — absent; `causative_stem_present` used instead (different name)
- `phase2_flags` — absent

**Additional fields present in v1.x not in v7:**
- `anchor_grammatical_form`, `anchor_stem`, `full_stem_range`, `word_type`, `note`

**Cross-registry links (grief_v1):**
- `linked_registry_id` values are unpadded integers (80, 4) not 3-digit strings; one is null

**Note on data volume:**
- anger: 34 terms, 297 verse records (in verse_classification)
- grief_v1: 26 terms, 64 verse records
- distress: 56 terms, 274 verse records

These are not lost — the data exists. But the structure is incompatible with v7 and cannot be used alongside v2.x files without transformation.

---

### anointing (schema 2.2, spec v4)

**Meta block issues (4 fields missing vs v7):**
- `part_number` — absent (single-part word, should be null)
- `total_parts` — absent (should be null)
- `is_split` — absent (should be false)
- `root_families_in_prior_parts` — absent (should be empty array)

**Term-level:** All 22 terms have all v7 fields present. No issues.  
**Verse records:** 181 records, all fields present.  
**Assessment:** Minor meta-block gap only. Data content is sound.

---

### grief part 2 (schema 2.3, spec v5)

**Cross-registry links (5 issues):**
- All 5 links have `linked_registry_id: "unknown"` — the registry IDs were not resolved at time of production
- 2 links use `connection_type: "co-occurrence"` — not a valid value in the current controlled vocabulary (valid: shared_term, shared_root, shared_verse, semantic_overlap)
- 1 link uses `connection_type: "theological"` — also not in the controlled vocabulary

**Term-level:** All 10 terms have all v7 fields present. No issues.  
**Verse records:** 94 records, all fields present.  
**Assessment:** Data content is sound. Cross-registry links are incomplete and two have invalid type values.

---

### shame part 2 (schema 2.3, spec v6)

**No issues found.** All meta fields, term fields, verse records, and cross-registry links pass audit against v7 standard. This is the only fully clean file in the set.

---

### peace part 1 (custom flat schema, spec v7)

**Structural:**
- Entirely custom flat structure — incompatible with every other file including other v7 files
- No `meta` block in v7 format; top-level fields used directly (`registry`, `word`, `part`, `source_list`, `produced_date`)
- `specification_version` field name used instead of `specification`
- Verses embedded within term objects (field `verses`) rather than in a separate `verse_records` array

**Term-level fields absent vs v7 (all 20 terms):**
- `term_id`, `step_search_gloss`, `step_search_flag`, `word_analysis_gloss`, `meaning`, `meaning_numbered`, `occurrence_count_qualifier`, `related_words`, `also_spelled`, `root_family`, `testament`, `god_as_subject`, `somatic_link`, `causative_form_present`, `phase2_flags`

**Extra fields present not in v7:**
- `gloss`, `gloss_sub`, `hebrew`, `script`, `word_analysis`, `is_consolidated_parent`, `is_sub_gloss`, `sub_gloss_entries`, `parent_entry`, `verse_extraction_note`, `check_c_exception`, `data_quality_note`

**Note on data volume:** 20 terms, 304 verse records (embedded in terms). Data exists but is structurally isolated.

---

### desire part 2 (schema 2.3, spec v7)

**Term-level — missing fields (25 terms × 2 fields = 50 individual absences):**
- `also_spelled` — absent on all 25 Greek terms (Greek terms legitimately do not use this field, but the field should be present and set to null per v7 schema for consistency)
- `meaning_numbered` — absent on all 25 Greek terms (same issue — Greek terms use lsj_entry instead but the field should still be present as null)

**PENDING Strong's numbers (2 terms):**
- `PENDING-043-epithumetos` (gloss: desirable) — Strong's unresolved
- `PENDING-043-epithumema` (gloss: desire) — Strong's unresolved
- Additionally `PENDING-043-oregō` uses a non-standard term_id format and Strong's G3713 is populated but term_id still shows PENDING prefix

**Extra field present:**
- `status_note` — appears on some terms; not in v7 schema. Contains useful data but is not a recognised field.

**Assessment:** The field absences are a schema drift issue — Greek term handling in v6/v7 did not enforce `also_spelled: null` and `meaning_numbered: null` on Greek terms. The 3 PENDING Strong's numbers were unresolved at production time and remain so.

---

## Cross-File Consistency Issues

**Registry ID format:** Inconsistent across files:
- v1.x files: unpadded integers (`4`, `72`) or unpadded string (`051`)
- v2.x files: zero-padded 3-digit strings (`006`, `071`, `043`)
- grief_p2 cross-registry links: `"unknown"` string

**Somatic field naming:**
- v1.x files: `somatic_dimension` (string or boolean, varies)
- v2.x files: `somatic_link` (boolean)
- These cannot be queried together without transformation

**Divine subject field naming:**
- v1.x files: `divine_subject_possible` (boolean)
- v2.x files: `god_as_subject` (boolean)
- Different names, different intent (possible vs confirmed)

**Causative field naming:**
- v1.x files: `causative_stem_present` (boolean)
- v2.x files: `causative_form_present` (boolean)
- Same concept, different field names

**connection_type controlled vocabulary:** Values in use across files:
- Valid: `shared_term`, `shared_root`, `shared_verse`, `semantic_overlap`
- Invalid found: `co-occurrence` (grief_p2), `theological` (grief_p2)

---

## What This Means for Cross-Registry Analysis

Of the 8 files audited:
- **1 file** is fully clean against v7 (shame part 2)
- **3 files** are clean on content but have minor structural gaps (anointing: 4 meta fields; grief part 2: cross-registry links only; desire part 2: 50 field absences + 3 pending strongs)
- **4 files** use incompatible schemas (anger, grief_v1, distress, peace part 1) — their data cannot be queried alongside v2.x files without transformation

Any analysis that queries across somatic_link, god_as_subject, or causative_form_present will silently exclude the v1.x files because those fields do not exist under those names. Any analysis that queries root_family, testament, or term_id will exclude v1.x and peace entirely.

---

## Recommendations (for your decision)

1. **Define a single canonical format** for `also_used_in` in the MTI and `linked_registry_id` in JSON files — one format, one decision
2. **Define whether Greek terms require `also_spelled: null` and `meaning_numbered: null`** — this removes the desire-type drift
3. **Decide what to do with v1.x files** — they hold real data but are structurally incompatible. Options: transform to v2.3, leave as legacy and exclude from cross-registry queries, or document as a known gap
4. **Peace part 1 is the most isolated file** — produced under v7 spec but with an entirely custom structure. This needs to be understood before peace is used in any analysis

