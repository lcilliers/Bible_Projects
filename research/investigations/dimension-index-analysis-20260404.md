# Dimension Index — Exploration and Analysis

**Date:** 2026-04-04
**Status:** Exploratory — data-driven findings from wa_dimension_index population
**Builds on:** [characteristic-layer-concept-20260403.md](characteristic-layer-concept-20260403.md)
**Scripts:** `scripts/populate_dimension_index.py`, `scripts/extract_term_data.py`

---

## 1. Origin and Purpose

On 2026-04-03, during term exploration using `extract_term_data.py`, the researcher observed that the `verse_context_group.context_description` field — written by Claude AI for every classified term — contains a proto-taxonomy of inner-being functions. These descriptions don't just classify verses; they name what each term *does* to or in the inner being.

This observation was documented in [characteristic-layer-concept-20260403.md](characteristic-layer-concept-20260403.md) as a potential Layer 2 between Verse Context and Session B Analysis. The core idea: if we could cluster the 2,933 context descriptions programme-wide, characteristic families would emerge from the data — families that cut across registries and could pre-structure Session B's analytical work.

On 2026-04-04, with Stage 1 at 81.2% complete (147/181 registries), we built the infrastructure to test this idea.

---

## 2. The Dimension Index Table

**Table:** `wa_dimension_index` — a denormalised cross-reference joining every verse_context_group to its term, registry, and cluster, with a dimension classification and confidence flag.

**Schema:**

| Field | Source | Purpose |
|-------|--------|---------|
| verse_context_group_id | verse_context_group.id | The group being classified |
| mti_term_id | mti_terms.id | Programme-wide term identifier |
| strongs_number | mti_terms.strongs_number | Term reference |
| transliteration, gloss, language | mti_terms | Term identity |
| owning_registry_no, owning_registry_word | word_registry | Which word owns this term |
| cluster_assignment | word_registry | Cluster for pool processing |
| group_code | verse_context_group | Human-readable group reference |
| context_description | verse_context_group | Claude AI's inner-being description |
| **dimension** | Mechanical + Claude AI | Dimension family assignment (from WA-Reference v5.5 Section 4.3 vocabulary) |
| **dimension_confidence** | Script logic / Claude AI | Quality flag: KEYWORD_STRONG, KEYWORD_WEAK, UNCLASSIFIED, or MANUAL |
| **manual_override** | Researcher / Claude AI | 0 = mechanical classification can overwrite; 1 = protected from mechanical rerun |
| **notes** | Researcher / Claude AI | Annotation on the classification — reasoning, uncertainty, cross-dimension notes |
| **last_modified** | Auto-set | Date of last insert or update |
| anchor_count, related_count | verse_context | Group verse counts |
| set_aside_count | verse_context | Set-aside verses for this term |
| total_verse_count | verse_context | Total verses in this group |
| delete_flagged | Soft delete | 0 = active; 1 = excluded |

### How columns are populated

**On mechanical run** (`populate_dimension_index.py`):
- All cross-reference fields (strongs, gloss, registry, cluster, counts) are refreshed from the source tables
- `dimension` is set by keyword matching against the context_description
- `dimension_confidence` is set to KEYWORD_STRONG, KEYWORD_WEAK, or UNCLASSIFIED based on match specificity
- `manual_override` defaults to 0 on new inserts
- `last_modified` is set to today's date
- Rows with `manual_override = 1` are **never touched** — dimension, confidence, notes all preserved

**On Claude AI review:**
- `dimension` is set or corrected to the appropriate vocabulary value
- `dimension_confidence` is set to MANUAL
- `manual_override` is set to 1 — protecting this row from future mechanical runs
- `notes` records the reasoning or any cross-dimension observations
- `last_modified` is updated

**On researcher override:**
- Same as Claude AI review — `manual_override = 1` protects the decision
- `notes` should record the basis for the override

**On `--clear` rerun:**
- Only rows with `manual_override = 0` are deleted
- All manually overridden rows are preserved
- New groups from recent Verse Context batches are inserted
- Existing non-manual rows are updated with fresh mechanical classification

**Population script:** `scripts/populate_dimension_index.py`

```bash
python scripts/populate_dimension_index.py              # first run or incremental
python scripts/populate_dimension_index.py --clear      # clear non-manual rows and repopulate
python scripts/populate_dimension_index.py --dry-run    # show counts without writing
```

---

## 3. Current State

| Metric | Count |
|--------|-------|
| Total groups indexed | 2,933 |
| Unique terms | 1,842 |
| Unique registries | 148 |
| KEYWORD_STRONG | 632 (21.5%) |
| KEYWORD_WEAK | 1,048 (35.7%) |
| UNCLASSIFIED | 1,253 (42.7%) |
| Dimensions used | 12 of 14 |

---

## 4. Dimension Distribution

| Dimension | Groups | Registries | Confidence |
|-----------|--------|-----------|------------|
| Spiritual/God-ward | 381 | 102 | 107 strong, 274 weak |
| Moral/Conscience | 393 | 93 | 100 strong, 293 weak |
| Cognitive/Mind | 164 | 63 | 10 strong, 154 weak |
| Character/Disposition | 154 | 62 | 154 strong, 0 weak |
| Relational/Social | 124 | 51 | 0 strong, 124 weak |
| Theological/Divine-Human | 108 | 50 | 108 strong, 0 weak |
| Volitional/Will | 114 | 47 | 23 strong, 91 weak |
| Affective/Emotional | 114 | 46 | 66 strong, 48 weak |
| Identity/Selfhood | 43 | 28 | 43 strong, 0 weak |
| Volitional/Capacity | 49 | 22 | 0 strong, 49 weak |
| Sin & Vice | 21 | 17 | 6 strong, 15 weak |
| Somatic/Embodied | 15 | 10 | 15 strong, 0 weak |
| UNCLASSIFIED | 1,253 | — | — |

**Observation:** Spiritual/God-ward and Moral/Conscience are the most pervasive — touching 102 and 93 registries respectively. These two dimensions account for 774 groups (26% of all groups) across more than half the programme. This confirms the researcher's intuition that the moral and spiritual dimensions of the inner being are the programme's most cross-cutting characteristics.

**Unused dimensions:** Anthropological/Structural and Inner Life have no mechanical matches. They may emerge from Claude AI's review of the unclassified 42.7%.

---

## 5. Dimensional Analysis — Registries

### Most dimensionally diverse registries

| Reg | Word | Dimensions | Groups |
|-----|------|-----------|--------|
| 4 | anger | 9 | 38 |
| 61 | fear | 9 | 55 |
| 112 | mind | 9 | 75 |
| 117 | peace | 9 | 33 |
| 33 | courage | 8 | 13 |
| 43 | desire | 8 | 48 |
| 52 | division | 8 | 13 |
| 57 | evil | 8 | 31 |
| 99 | kindness | 8 | 38 |
| 103 | love | 8 | 38 |
| 128 | rebellion | 8 | 25 |
| 173 | will | 8 | 21 |

**Observation:** anger, fear, mind, and peace each span 9 of 12 active dimensions. These are not single-dimension words — they are programme-wide integrators. Session B Analysis for these words must address nearly the full dimensional spectrum. This has implications for pool processing order: these registries should be among the last processed, after the dimensional taxonomy is well-established from simpler words.

### Most dimensionally focused registries

Words that operate in 1-2 dimensions are the clearest candidates for early Session B processing — they contribute precision to the dimensional taxonomy without requiring cross-dimensional integration.

---

## 6. Dimensional Analysis — Terms

### Terms spanning most dimensions

| Strong | Gloss | Registry | Dims | Which |
|--------|-------|----------|------|-------|
| H5315G | soul | Soul | 5 | Affective, Volitional/Capacity, Theological, Moral, Spiritual |
| H1245 | to seek | desire | 4 | Spiritual, Volitional/Will, Moral, Relational |
| H2896A | pleasant | goodness | 4 | Theological, Moral, Spiritual, Cognitive |
| H0120G | man | kindness | 4 | Moral, Spiritual, Volitional/Will, Character |
| H4672 | to find | seeking | 4 | Relational, Cognitive, Moral, Affective |

**Observation:** H5315G (nephesh/soul) spans 5 dimensions — more than any other term. This single Hebrew word operates as affective centre, volitional capacity, moral agent, spiritual being, and theological subject. This is exactly the kind of insight the characteristic layer was designed to surface: a term's dimensional span is not visible from its gloss or its registry. It only becomes visible when the verse-level classifications are aggregated.

---

## 7. Dimensional Analysis — Clusters

Each cluster has a primary dimensional profile derivable from its member registries' groups:

| Cluster | Primary dimension | Secondary | Tertiary |
|---------|------------------|-----------|----------|
| C01 (soul/heart/spirit/flesh/mind/being) | Moral/Conscience (38) | Spiritual/God-ward (24) | Volitional/Capacity (22) |
| C02 (counsel/knowledge/wisdom/thought) | Cognitive/Mind (65) | Moral/Conscience (17) | Spiritual/God-ward (15) |
| C03 (joy/delight/gratitude/gladness) | Affective/Emotional (21) | Spiritual/God-ward (15) | Theological (6) |
| C04 (desire/appetite/hope/longing) | Spiritual/God-ward (28) | Volitional/Will (16) | Theological (9) |
| C05 (agony/grief/sorrow/weeping) | Moral/Conscience (23) | Affective/Emotional (22) | Spiritual/God-ward (13) |
| C07 (anger/wrath/envy/hatred) | Theological/Divine-Human (22) | Character/Disposition (10) | Moral/Conscience (8) |
| C10 (faithfulness/righteousness/integrity) | Moral/Conscience (31) | Spiritual/God-ward (27) | Cognitive/Mind (6) |
| C11 (corruption/evil/sin/wickedness) | Moral/Conscience (47) | Sin & Vice (10) | Spiritual/God-ward (9) |
| C15 (faith/prayer/worship/trust) | Spiritual/God-ward (64) | Moral/Conscience (20) | Cognitive/Mind (7) |
| C17 (compassion/love/mercy/peace) | Spiritual/God-ward (36) | Relational/Social (31) | Moral/Conscience (30) |

**Observation:** The cluster dimensional profiles confirm what you'd expect intuitively — C02 is cognitively dominated, C03 is affectively dominated, C15 is spiritually dominated. But the secondary and tertiary dimensions reveal the interconnections: C07 (anger cluster) is primarily Theological/Divine-Human, not Affective/Emotional as English intuition might suggest. The data shows anger in Scripture is primarily about the divine-human encounter, not about human feelings.

---

## 8. What This Enables

The dimension index creates three new analytical capabilities:

### 8.1 Pre-structured Session B input
Instead of Session B discovering the dimensional profile from scratch, the profile is already visible. Session B validates and deepens rather than discovers.

### 8.2 Cross-registry characteristic mapping
The many-to-many relationship between dimensions and registries is now queryable. You can ask: "Which registries share the Volitional/Will dimension?" and get the full list — enabling pool assembly based on dimensional overlap, not just term sharing.

### 8.3 Claude AI classification task
The 1,253 unclassified groups (42.7%) are a well-defined task for Claude AI: read the context_description, assign a dimension from the controlled vocabulary. The data fits in a single session (~119k tokens in compact format). Claude AI reviews the KEYWORD_WEAK assignments simultaneously.

---

## 9. Next Steps

1. **Complete Stage 1** — approximately 5 more batches. Repopulate the index after completion.
2. **Claude AI review session** — provide all 2,933 groups with current classifications for validation and completion of the 42.7% unclassified.
3. **Schema formalisation** — add `dimension_id` to `verse_context_group` once the vocabulary is stable. The index table becomes a view rather than a materialized table.
4. **Session B integration** — include the dimensional profile in pool analysis datasets.

---

## 10. Relationship to Existing Architecture

This work connects to:
- **`word_registry.dimensions`** — currently a comma-delimited field set by Session B. With the dimension index, this becomes derivable: aggregate the dimensions of all groups belonging to terms owned by that registry.
- **WA-Reference v5.5 Section 4.3** — the dimension vocabulary is already controlled. The index uses the same values.
- **Pool processing sequence** — currently based on term sharing (RMG v5.6 Section 5.2). Dimensional overlap offers a complementary criterion.
- **Session D synthesis** — the dimension index is effectively a Session D pre-computation. Cross-registry patterns that would normally require Session D's cross-programme view are already visible.

---

*Produced 2026-04-04 by Claude Code. Builds on characteristic-layer-concept-20260403.md.*
*Scripts: populate_dimension_index.py, extract_term_data.py*
*Table: wa_dimension_index (2,933 rows, 12/14 dimensions active)*
