# Dimension Vocabulary - Extract and Clustering

| Field | Value |
| --- | --- |
| Source table | `wa_dimension_index` |
| Filter | `delete_flagged = 0` |
| Extract date | 2026-04-19 |
| Purpose | Answer coverage question; enumerate dimension labels; surface vocabulary drift |

---

## 1. Coverage Answer

**Answer: No - coverage is partial.**

| Population | Count |
| --- | --- |
| Non-excluded registries (`carry_forward = 1`) | 213 |
| With `dim_review_status = 'Complete'` | 34 |
| With ANY rows in `wa_dimension_index` | 173 |
| With at least one non-NULL `dimension` label | 172 |
| Non-excluded registries with ZERO dimension data | 40 |

**Interpretation:**

- Only 34 registries have `dim_review_status = 'Complete'`. This flag has lagged the actual data state.
- 173 registries have dimension_index rows - this is the real coverage number.
- 40 non-excluded words have zero dimension data. These are gaps that will need to be filled.

**Dimension group counts by confidence (active rows):**

| `dimension_confidence` | Count | Reviewed? |
| --- | --- | --- |
| KEYWORD_WEAK | 1547 | no - automated or unreviewed |
| CLAUDE_AI | 1255 | YES |
| KEYWORD_STRONG | 320 | no - automated or unreviewed |
| UNCLASSIFIED | 250 | no - automated or unreviewed |
| ROOT_INFERRED | 126 | no - automated or unreviewed |

Only CLAUDE_AI (and RESEARCHER) confidence constitutes a reviewed assignment. KEYWORD_STRONG, KEYWORD_WEAK, ROOT_INFERRED, and UNCLASSIFIED are all pre-review states.

---

## 2. All Distinct Dimension Labels

**24 distinct dimension labels** across the corpus.

| # | Dimension | Total uses | CLAUDE_AI (reviewed) | KW_strong | KW_weak | Root_inf | Words covering |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Moral Character | 592 | 208 | 50 | 298 | 36 | 119 |
| 2 | Emotion — Negative | 473 | 78 | 63 | 321 | 11 | 87 |
| 3 | Relational Disposition | 368 | 207 | 19 | 129 | 13 | 92 |
| 4 | Volition | 314 | 68 | 31 | 194 | 21 | 89 |
| 5 | Cognition | 263 | 63 | 17 | 172 | 11 | 83 |
| 6 | Divine-Human Correspondence | 255 | 37 | 77 | 131 | 10 | 88 |
| 7 | Agency / Power | 158 | 76 | 10 | 69 | 3 | 48 |
| 8 | Dependence / Creatureliness | 149 | 78 | 1 | 67 | 3 | 49 |
| 9 | Emotion — Positive | 141 | 28 | 17 | 90 | 6 | 40 |
| 10 | Transformation | 115 | 55 | 34 | 22 | 4 | 56 |
| 11 | Vitality / Existence | 94 | 32 | 1 | 54 | 7 | 39 |
| 12 | Theological/Divine-Human | 64 | 64 | 0 | 0 | 0 | 14 |
| 13 | Moral/Conscience | 60 | 60 | 0 | 0 | 0 | 9 |
| 14 | Affective/Emotional | 47 | 47 | 0 | 0 | 0 | 9 |
| 15 | Spiritual/God-ward | 32 | 32 | 0 | 0 | 0 | 8 |
| 16 | Cognitive/Mind | 30 | 30 | 0 | 0 | 0 | 8 |
| 17 | Relational/Social | 22 | 22 | 0 | 0 | 0 | 7 |
| 18 | Volitional/Will | 19 | 18 | 0 | 0 | 1 | 5 |
| 19 | Character/Disposition | 17 | 17 | 0 | 0 | 0 | 6 |
| 20 | Identity/Selfhood | 9 | 9 | 0 | 0 | 0 | 4 |
| 21 | Identity / Selfhood | 8 | 8 | 0 | 0 | 0 | 3 |
| 22 | Volitional/Capacity | 7 | 7 | 0 | 0 | 0 | 3 |
| 23 | Somatic/Embodied | 6 | 6 | 0 | 0 | 0 | 2 |
| 24 | Theological / Divine-Human | 5 | 5 | 0 | 0 | 0 | 2 |

---

## 3. Clustered by Semantic Category (vocabulary drift surfaced)

The 24 labels fall into **two parallel vocabularies**. Most clusters (C02-C22) use a newer vocabulary (no slashes). C01 predominantly uses an older vocabulary (slash-style). A few near-duplicates exist from formatting inconsistency. This is a data-readiness finding that the DB-wide review should address.

### Moral / Ethical / Character

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Moral Character | new | 592 | 208 |
| Moral/Conscience | legacy | 60 | 60 |
| Character/Disposition | legacy | 17 | 17 |

### Cognition / Mind / Awareness

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Cognition | new | 263 | 63 |
| Cognitive/Mind | legacy | 30 | 30 |

### Volition / Will / Choice

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Volition | new | 314 | 68 |
| Volitional/Will | legacy | 19 | 18 |
| Volitional/Capacity | legacy | 7 | 7 |

### Relational / Social

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Relational Disposition | new | 368 | 207 |
| Relational/Social | legacy | 22 | 22 |

### Emotion - Negative

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Emotion — Negative | new | 473 | 78 |

### Emotion - Positive

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Emotion — Positive | new | 141 | 28 |

### Emotion / Affect (legacy, unsplit)

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Affective/Emotional | legacy | 47 | 47 |

### Divine-Human / Theological

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Divine-Human Correspondence | new | 255 | 37 |
| Theological/Divine-Human | legacy | 64 | 64 |
| Theological / Divine-Human | legacy-variant | 5 | 5 |
| Spiritual/God-ward | legacy | 32 | 32 |

### Agency / Power

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Agency / Power | new | 158 | 76 |

### Dependence / Creatureliness

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Dependence / Creatureliness | new | 149 | 78 |

### Transformation

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Transformation | new | 115 | 55 |

### Vitality / Existence / Life

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Vitality / Existence | new | 94 | 32 |

### Identity / Selfhood

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Identity/Selfhood | legacy | 9 | 9 |
| Identity / Selfhood | legacy-variant | 8 | 8 |

### Somatic / Embodied

| Label | Vocabulary | Total uses | CLAUDE_AI reviewed |
| --- | --- | ---: | ---: |
| Somatic/Embodied | legacy | 6 | 6 |

---

## 4. Dimension Distribution per Cluster Assignment (`cluster_assignment`)

For each cluster code (C01-C22), the dimensions used. Useful to see which clusters hold legacy vocabulary.

**C01** (274 groups - **legacy-dominant**)

| Dimension | n |
| --- | ---: |
| Moral/Conscience | 57 |
| Theological/Divine-Human | 55 |
| Affective/Emotional | 37 |
| Spiritual/God-ward | 25 |
| Cognitive/Mind | 23 |
| Character/Disposition | 17 |
| Volitional/Will | 15 |
| Relational/Social | 14 |
| Identity/Selfhood | 9 |
| Volitional/Capacity | 7 |
| Somatic/Embodied | 6 |
| Moral Character | 4 |
| Cognition | 2 |
| Volition | 1 |
| Relational Disposition | 1 |
| Emotion — Positive | 1 |

**C02** (211 groups - mixed)

| Dimension | n |
| --- | ---: |
| Cognition | 95 |
| Volition | 28 |
| Emotion — Negative | 18 |
| Divine-Human Correspondence | 18 |
| Relational Disposition | 13 |
| Moral Character | 10 |
| Cognitive/Mind | 7 |
| Transformation | 5 |
| Theological/Divine-Human | 4 |
| Agency / Power | 4 |
| Moral/Conscience | 3 |
| Volitional/Will | 2 |
| Dependence / Creatureliness | 2 |
| Spiritual/God-ward | 1 |
| Emotion — Positive | 1 |

**C03** (114 groups)

| Dimension | n |
| --- | ---: |
| Emotion — Positive | 67 |
| Emotion — Negative | 11 |
| Divine-Human Correspondence | 11 |
| Relational Disposition | 9 |
| Moral Character | 6 |
| Volition | 5 |
| Cognition | 3 |
| Agency / Power | 2 |

**C04** (157 groups - mixed)

| Dimension | n |
| --- | ---: |
| Volition | 70 |
| Emotion — Negative | 14 |
| Divine-Human Correspondence | 14 |
| Emotion — Positive | 11 |
| Dependence / Creatureliness | 10 |
| Cognition | 10 |
| Relational Disposition | 9 |
| Moral Character | 5 |
| Vitality / Existence | 4 |
| Agency / Power | 4 |
| Transformation | 3 |
| Volitional/Will | 2 |
| Theological/Divine-Human | 1 |

**C05** (227 groups - mixed)

| Dimension | n |
| --- | ---: |
| Emotion — Negative | 119 |
| Moral Character | 28 |
| Volition | 14 |
| Affective/Emotional | 10 |
| Relational/Social | 8 |
| Vitality / Existence | 7 |
| Emotion — Positive | 7 |
| Divine-Human Correspondence | 7 |
| Spiritual/God-ward | 6 |
| Relational Disposition | 5 |
| Dependence / Creatureliness | 5 |
| Transformation | 4 |
| Theological/Divine-Human | 3 |
| Cognition | 2 |
| Agency / Power | 2 |

**C06** (177 groups)

| Dimension | n |
| --- | ---: |
| Emotion — Negative | 110 |
| Divine-Human Correspondence | 18 |
| Relational Disposition | 14 |
| Moral Character | 14 |
| Dependence / Creatureliness | 8 |
| Volition | 4 |
| Cognition | 3 |
| Agency / Power | 3 |
| Vitality / Existence | 1 |
| Transformation | 1 |
| Emotion — Positive | 1 |

**C07** (109 groups)

| Dimension | n |
| --- | ---: |
| Emotion — Negative | 47 |
| Divine-Human Correspondence | 28 |
| Relational Disposition | 8 |
| Moral Character | 7 |
| Volition | 6 |
| Cognition | 4 |
| Dependence / Creatureliness | 3 |
| Agency / Power | 3 |
| Vitality / Existence | 1 |
| Transformation | 1 |
| Emotion — Positive | 1 |

**C08** (95 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 16 |
| Divine-Human Correspondence | 16 |
| Agency / Power | 12 |
| Volition | 11 |
| Emotion — Negative | 11 |
| Dependence / Creatureliness | 10 |
| Relational Disposition | 8 |
| Cognition | 6 |
| Vitality / Existence | 2 |
| Transformation | 2 |
| Emotion — Positive | 1 |

**C09** (103 groups)

| Dimension | n |
| --- | ---: |
| Divine-Human Correspondence | 22 |
| Volition | 18 |
| Moral Character | 18 |
| Relational Disposition | 12 |
| Agency / Power | 12 |
| Emotion — Negative | 10 |
| Cognition | 6 |
| Vitality / Existence | 2 |
| Transformation | 2 |
| Dependence / Creatureliness | 1 |

**C10** (106 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 50 |
| Transformation | 11 |
| Cognition | 10 |
| Divine-Human Correspondence | 8 |
| Relational Disposition | 7 |
| Emotion — Negative | 6 |
| Vitality / Existence | 5 |
| Volition | 4 |
| Emotion — Positive | 4 |
| Agency / Power | 1 |

**C11** (143 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 76 |
| Volition | 14 |
| Emotion — Negative | 13 |
| Cognition | 10 |
| Vitality / Existence | 9 |
| Divine-Human Correspondence | 7 |
| Relational Disposition | 5 |
| Transformation | 3 |
| Emotion — Positive | 3 |
| Dependence / Creatureliness | 2 |
| Agency / Power | 1 |

**C12** (88 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 32 |
| Volition | 15 |
| Relational Disposition | 10 |
| Transformation | 9 |
| Emotion — Negative | 7 |
| Divine-Human Correspondence | 5 |
| Cognition | 5 |
| Emotion — Positive | 3 |
| Vitality / Existence | 1 |
| Agency / Power | 1 |

**C13** (144 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 52 |
| Cognition | 15 |
| Divine-Human Correspondence | 14 |
| Dependence / Creatureliness | 14 |
| Transformation | 10 |
| Relational Disposition | 10 |
| Emotion — Negative | 9 |
| Volition | 8 |
| Agency / Power | 7 |
| Emotion — Positive | 4 |
| Vitality / Existence | 1 |

**C14** (123 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 24 |
| Volition | 20 |
| Relational Disposition | 13 |
| Divine-Human Correspondence | 13 |
| Dependence / Creatureliness | 12 |
| Emotion — Negative | 10 |
| Agency / Power | 10 |
| Emotion — Positive | 7 |
| Transformation | 6 |
| Vitality / Existence | 4 |
| Cognition | 4 |

**C15** (144 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 40 |
| Relational Disposition | 19 |
| Cognition | 19 |
| Volition | 14 |
| Divine-Human Correspondence | 12 |
| Dependence / Creatureliness | 12 |
| Vitality / Existence | 11 |
| Emotion — Negative | 7 |
| Agency / Power | 7 |
| Transformation | 3 |

**C16** (116 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 31 |
| Divine-Human Correspondence | 17 |
| Vitality / Existence | 12 |
| Cognition | 12 |
| Volition | 11 |
| Relational Disposition | 10 |
| Agency / Power | 10 |
| Emotion — Positive | 4 |
| Transformation | 3 |
| Emotion — Negative | 3 |
| Dependence / Creatureliness | 3 |

**C17** (299 groups - mixed)

| Dimension | n |
| --- | ---: |
| Relational Disposition | 123 |
| Moral Character | 69 |
| Dependence / Creatureliness | 24 |
| Emotion — Positive | 20 |
| Volition | 17 |
| Emotion — Negative | 15 |
| Transformation | 11 |
| Divine-Human Correspondence | 10 |
| Cognition | 8 |
| Vitality / Existence | 1 |
| Theological/Divine-Human | 1 |

**C18** (37 groups)

| Dimension | n |
| --- | ---: |
| Relational Disposition | 12 |
| Volition | 7 |
| Moral Character | 4 |
| Emotion — Negative | 4 |
| Divine-Human Correspondence | 3 |
| Emotion — Positive | 2 |
| Cognition | 2 |
| Agency / Power | 2 |
| Dependence / Creatureliness | 1 |

**C19** (80 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 19 |
| Divine-Human Correspondence | 19 |
| Agency / Power | 8 |
| Transformation | 7 |
| Cognition | 7 |
| Relational Disposition | 6 |
| Emotion — Negative | 5 |
| Volition | 4 |
| Vitality / Existence | 3 |
| Dependence / Creatureliness | 2 |

**C20** (370 groups)

| Dimension | n |
| --- | ---: |
| Moral Character | 70 |
| Agency / Power | 62 |
| Relational Disposition | 60 |
| Volition | 36 |
| Emotion — Negative | 36 |
| Dependence / Creatureliness | 32 |
| Cognition | 21 |
| Transformation | 19 |
| Vitality / Existence | 17 |
| Divine-Human Correspondence | 13 |
| Emotion — Positive | 4 |

**C21** (46 groups)

| Dimension | n |
| --- | ---: |
| Vitality / Existence | 11 |
| Transformation | 9 |
| Cognition | 7 |
| Emotion — Negative | 5 |
| Volition | 4 |
| Moral Character | 4 |
| Identity / Selfhood | 2 |
| Dependence / Creatureliness | 2 |
| Relational Disposition | 1 |
| Agency / Power | 1 |

**C22** (85 groups)

| Dimension | n |
| --- | ---: |
| Relational Disposition | 13 |
| Moral Character | 13 |
| Emotion — Negative | 13 |
| Cognition | 12 |
| Transformation | 6 |
| Identity / Selfhood | 6 |
| Dependence / Creatureliness | 6 |
| Agency / Power | 6 |
| Theological / Divine-Human | 5 |
| Volition | 3 |
| Vitality / Existence | 2 |

---

## 5. Non-Excluded Words With Zero Dimension Data

**41 non-excluded words have zero `wa_dimension_index` rows.**

These are the words that have NOT been through any dimension process.

| no | word | verse_context_status | cluster |
| ---: | --- | --- | --- |
| 9 | assent | - | C22 |
| 10 | awareness | - | C22 |
| 12 | betrayal | - | C18 |
| 14 | blamelessness | - | C10 |
| 21 | commitment | - | C14 |
| 22 | communion | - | C17 |
| 25 | conformity | - | C14 |
| 27 | consciousness | Complete | C22 |
| 36 | cowardice | - | C09 |
| 37 | darkening | - | C21 |
| 38 | deadness | - | C21 |
| 45 | determination | - | C14 |
| 48 | diligence | Complete | C08 |
| 54 | emotion | - | C22 |
| 79 | hopelessness | - | C06 |
| 82 | identity | - | C19 |
| 84 | image of God | - | C19 |
| 88 | ingratitude | - | C22 |
| 95 | intuition | - | C22 |
| 101 | laziness | - | C09 |
| 104 | loyalty | Complete | C18 |
| 106 | manipulation | - | C18 |
| 109 | meekness | Complete | C08 |
| 118 | personality | - | C22 |
| 119 | personhood | - | C19 |
| 129 | recognition | Complete | C22 |
| 133 | reliability | - | C09 |
| 136 | resentment | - | C07 |
| 137 | resolve | Complete | C14 |
| 138 | reverence | Complete | C15 |
| 141 | self-awareness | - | C19 |
| 143 | sensitivity | - | C22 |
| 144 | sensuality | Complete | C12 |
| 145 | sexuality | - | C22 |
| 154 | stupor | - | C21 |
| 161 | transformation | - | C21 |
| 169 | vulnerability | - | C22 |
| 195 | spiritual powers | - | C20 |
| 200 | energy | Complete | C20 |
| 205 | resentment | Complete | C07 |
| 214 | suffering | In Progress | C05 |

**Pattern:** most are VC-None, suggesting they have not even completed Verse Context - dimension review correctly did not run. A few are VC-Complete but dim-gap - those are genuine gaps to fill.

---

## 6. Implications for Readiness Sweep and DB-Wide Review

### Vocabulary normalisation is a DB-review task

The 24 distinct labels collapse to ~14 conceptual dimensions. The DB-wide review should:

1. Decide canonical vocabulary (recommend the newer slash-less style used in C02-C22).
2. Normalise legacy values (C01 and stragglers) to canonical form.
3. Handle near-duplicates (`Identity/Selfhood` vs `Identity / Selfhood`; `Theological/Divine-Human` vs `Theological / Divine-Human`).
4. Consider whether some legacy labels (e.g. `Affective/Emotional`) should split into Positive/Negative to match the newer taxonomy.
5. Consider introducing a dimension dictionary table (`dimension_vocabulary` with `code`, `label`, `parent_code`) to prevent future drift.

### Readiness sweep Phase R.E impact

The sweep's Phase R.E (dimension assignments) should flag:
- Groups with `dimension_confidence IN ('KEYWORD_STRONG','KEYWORD_WEAK','ROOT_INFERRED','UNCLASSIFIED')` - not yet reviewed. Count across corpus: 2243/3498 = 64%.
- Groups using legacy vocabulary (contain `/` without spaces).
- Duplicate labels differing only in whitespace.

### Relation to prose store seed

Dimensions are NOT chapter-equivalent (they describe group semantic content, not word-level chapter structure). They do not map to `prose_section_type`. The question catalogue extract (see `wa-obs-question-catalogue-extract-20260419.md`) is the right source for chapter structure.

Dimensions DO link to prose through the optional `prose_section_dimension_link` table - prose sections can cite which dimensions they discuss. After vocabulary normalisation, that linkage becomes reliable.

---

*Generated 2026-04-19 from live `bible_research.db`. 24 distinct dimension labels across 172 registries. 2243 of 3498 groups not yet at CLAUDE_AI confidence.*
