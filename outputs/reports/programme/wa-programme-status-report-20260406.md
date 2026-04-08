# Programme Status Report

> Generated: 2026-04-06
> Stage: Verse Context complete — Session B DataPrep gate open

---

# 1. Programme Overview

| Metric | Value |
|--------|-------|
| Total registries | 212 |
| Active (non-excluded) | 181 |
| Excluded (Phase 1) | 31 |
| Active terms (OWNER) | 3647 |
| Active terms (XREF) | 3341 |
| Active verses | 85,115 |

---

# 2. Verse Context — Stage 1 Complete

| verse_context_status | Count |
|---------------------|-------|
| Complete | 181 |
| In Progress | 0 |
| NULL (excluded) | 31 |

### Verse Context Data

| Metric | Value |
|--------|-------|
| Contextual meaning groups | 3,401 |
| Total verse classifications | 60,879 |
| Relevant (inner-being) | 34,212 |
| Set aside | 26,667 |
| Anchor verses | 4,561 |
| Related verses | 29,650 |

**Relevance rate:** 56.2% of classified verses engage the inner being.

**Batches applied:** 31 (VCB-001 through VCB-029)

---

# 3. Dimension Index

Theological dimension classification of all contextual meaning groups.

| Status | Count | % |
|--------|------:|---:|
| Classified | 1856 | 55% |
| Unclassified | 1545 | 45% |
| **Total** | **3401** | |

### Dimension Distribution

| Dimension | Groups | % of classified |
|-----------|-------:|---:|
| UNCLASSIFIED | 1545 | 45.4% |
| Moral/Conscience | 439 | 12.9% |
| Spiritual/God-ward | 416 | 12.2% |
| Cognitive/Mind | 181 | 5.3% |
| Character/Disposition | 163 | 4.8% |
| Relational/Social | 137 | 4.0% |
| Affective/Emotional | 121 | 3.6% |
| Volitional/Will | 115 | 3.4% |
| Theological/Divine-Human | 114 | 3.4% |
| Volitional/Capacity | 75 | 2.2% |
| Identity/Selfhood | 54 | 1.6% |
| Sin & Vice | 21 | 0.6% |
| Somatic/Embodied | 20 | 0.6% |

### Classification Confidence

| Confidence | Count |
|-----------|------:|
| UNCLASSIFIED | 1545 |
| KEYWORD_WEAK | 1165 |
| KEYWORD_STRONG | 691 |

---

# 4. Session B Pipeline Status

| session_b_status | Count |
|-----------------|------:|
| NULL | 31 |
| Verse Context Reset | 181 |

**Registries with DataPrep gate open:** 181

---

# 5. Cluster Readiness for Session B

All clusters have verse_context_status = Complete. Ready for pool-based Session B.

| Cluster | Total | Active | Not-shared | Words |
|---------|------:|-------:|-----------:|-------|
| C01 | 6 | 6 | 0 | mind, Soul, heart, spirit, flesh, being |
| C02 | 13 | 13 | 0 | counsel, discernment, imagination, insight, intention, kn... |
| C03 | 9 | 9 | 1 | awe, contentment, delight, gratitude, joy, rejoicing, won... |
| C04 | 7 | 7 | 0 | appetite, desire, hope, longing, passion, yearning, craving |
| C05 | 9 | 9 | 0 | agony, anguish, brokenness, distress, grief, groaning, mo... |
| C06 | 8 | 7 | 0 | anxiety, despair, dread, fear, shame, terror, contempt |
| C07 | 10 | 9 | 0 | anger, bitterness, envy, hatred, indignation, jealousy, w... |
| C08 | 11 | 11 | 0 | boldness, courage, devotion, diligence, endurance, genero... |
| C09 | 10 | 7 | 0 | boastfulness, hardness, pride, rebellion, stubbornness, w... |
| C10 | 11 | 10 | 2 | faithfulness, goodness, honesty, innocence, integrity, pu... |
| C11 | 10 | 10 | 2 | corruption, deceit, evil, hypocrisy, iniquity, perversene... |
| C12 | 10 | 10 | 1 | abomination, debauchery, defilement, impurity, lust, sens... |
| C13 | 9 | 8 | 0 | condemnation, conscience, covetousness, disobedience, gre... |
| C14 | 10 | 7 | 3 | bondage, obedience, resolve, submission, surrender, will,... |
| C15 | 9 | 9 | 0 | faith, intercession, praise, prayer, reverence, seeking, ... |
| C16 | 10 | 10 | 1 | anointing, consecration, holiness, idolatry, prophecy, so... |
| C17 | 11 | 10 | 3 | compassion, covenant, fellowship, forgiveness, grace, kin... |
| C18 | 7 | 5 | 2 | division, loyalty, rejection, strife, unity |
| C19 | 11 | 7 | 0 | calling, dignity, meaning, worth, image, name, likeness |
| C20 | 7 | 6 | 0 | strength, power, authority, might, dominion, energy |
| C21 | 8 | 4 | 1 | renewal, transformation, blindness (spiritual), deadness |
| C22 | 16 | 7 | 1 | ambition, character, consciousness, experience, foolishne... |

---

# 6. Term Inventory

## 6.1 MTI Status Distribution

| mti_terms.status | Count |
|-----------------|------:|
| delete | 2565 |
| NULL | 2268 |
| extracted | 2240 |
| extracted_thin | 302 |
| candidate_delete | 71 |
| extracted_theological_anchor | 17 |
| excluded | 9 |
| phase2_enrichment | 5 |
| xref_distress | 3 |
| xref_anger | 2 |
| xref_desire | 2 |
| xref_sorrow | 2 |
| xref_wisdom | 1 |

## 6.2 Term Sharing

| Sharing Ratio | Registries |
|--------------|----------:|
| 0% (all unique) | 17 |
| 1-49% shared | 30 |
| 50-79% shared | 54 |
| 80%+ shared | 80 |

## 6.3 Quality Flags

| Quality Flag | Count |
|-------------|------:|
| NO_WORD_ANALYSIS | 7297 |
| PROSE_ONLY_MEANING | 5491 |
| THIN_DATA | 4778 |
| SMALL_VERSE_SAMPLE | 2885 |
| NO_VERSES | 511 |
| CONCRETE_PHYSICAL | 315 |
| HIGH_FREQUENCY_ANCHOR | 274 |

---

# 7. Data Integrity

### Verse Context Integrity (R1-R3)

| Rule | Violations |
|------|----------:|
| R1: set-aside clean | 0 |
| R2: anchor clean | 0 |
| R3: related-anchor linkage | 0 |

**Status:** ALL CLEAN

**Phantom mti_terms duplicates:** 0

**Unparsed meanings:** 71 terms

---

# 8. Next Steps

1. **Dimension classification** — 1,545 UNCLASSIFIED + 1,165 KEYWORD_WEAK groups need Claude AI assessment
2. **Session B DataPrep** — all 181 registries have VC Complete, DataPrep gate open
3. **Pool assembly** — per WA-Registry-Management-Guide v5.6, not-shared words first, then pools by cluster
