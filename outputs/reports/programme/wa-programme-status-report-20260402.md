# Programme Status Report — 2026-04-02

> Schema v3.8.0 | VCB-001 through VCB-012 applied (+ VCB-006 diff + VCB-012 H2617A supplemental)

## 1. Programme Overview

| Metric | Count |
|--------|-------|
| Total registries | 212 |
| Active | 179 |
| Excluded | 31 |

## 2. Pipeline Status

| session_b_status | verse_context_status | Count |
|-----------------|---------------------|-------|
| Verse Context Reset | In Progress | 100 |
| Verse Context Reset | Complete | 81 |
| NULL | NULL | 31 |

## 3. Verse Context — Stage 1 Progress

| Metric | Count |
|--------|-------|
| Registries Complete | **81** / 181 (44.8%) |
| Registries In Progress | 100 |
| Batches processed | 12 + 2 supplemental/differential |
| verse_context_group records | 1,642 |
| verse_context records | 29,375 |
| --- Anchors | 2,133 |
| --- Related | 14,560 |
| --- Set aside | 12,682 |

### 3.1 Completed Registries

         1-abomination  |               2-agony  |            3-ambition  |               4-anger
             5-anguish  |           6-anointing  |             7-anxiety  |            8-appetite
                11-awe  |         13-bitterness  |           16-boldness  |            17-bondage
         18-brokenness  |            19-calling  |          20-character  |         23-compassion
       24-condemnation  |         26-conscience  |       28-consecration  |        29-contentment
         31-corruption  |            33-courage  |           34-covenant  |       35-covetousness
         39-debauchery  |             40-deceit  |         41-defilement  |            42-delight
            44-despair  |           46-devotion  |            47-dignity  |          48-diligence
        49-discernment  |       50-disobedience  |           51-distress  |           52-division
              53-dread  |          55-endurance  |               56-envy  |               57-evil
         58-experience  |              59-faith  |       60-faithfulness  |               61-fear
         62-fellowship  |        63-foolishness  |        64-forgiveness  |         65-generosity
         66-gentleness  |           67-goodness  |              68-grace  |          69-gratitude
              70-greed  |              71-grief  |           72-groaning  |           74-hardness
             75-hatred  |           76-holiness  |            77-honesty  |               78-hope
           80-humility  |          81-hypocrisy  |           83-idolatry  |        85-imagination
           86-impurity  |        87-indignation  |           89-iniquity  |          90-innocence
            91-insight  |          92-integrity  |       94-intercession  |           96-jealousy
                97-joy  |            98-justice  |           99-kindness  |         100-knowledge
           102-longing  |              103-love  |              105-lust  |           107-meaning
        108-meditation

### 3.2 Remaining Work

| Metric | Count |
|--------|-------|
| Terms unclassified | 1,261 |
| Verses to classify | 28,960 |
| Estimated batches remaining | ~12 |

### 3.3 Partial Registries

| Reg | Word | Classified | Total | Remaining |
|-----|------|-----------|-------|-----------|
| 32 | counsel | 11 | 12 | 1 |
| 43 | desire | 45 | 47 | 2 |
| 73 | guilt | 21 | 22 | 1 |
| 110 | memory | 1 | 2 | 1 |
| 111 | mercy | 15 | 25 | 10 |

## 4. Data Health

| Check | Value | Status |
|-------|-------|--------|
| Active mti_terms | 3,807 | CLEAN |
| Multi-OWNER strongs | 0 | CLEAN |
| OWNER ti | 3,647 | |
| XREF ti | 3,341 | |
| Active verses | 85,116 | |

## 5. Cluster Progress

| Cluster | Words | VC Complete | In Progress | Excluded |
|---------|-------|-------------|-------------|----------|
| C01 | 6 | 0 | 6 | 0 |
| C02 | 13 | 5 | 8 | 0 |
| C03 | 9 | 5 | 4 | 0 |
| C04 | 7 | 3 | 4 | 0 |
| C05 | 9 | 6 | 3 | 0 |
| C06 | 8 | 4 | 3 | 1 |
| C07 | 10 | 6 | 3 | 1 |
| C08 | 11 | 8 | 3 | 0 |
| C09 | 10 | 1 | 6 | 3 |
| C10 | 11 | 5 | 5 | 1 |
| C11 | 10 | 5 | 5 | 0 |
| C12 | 10 | 5 | 5 | 0 |
| C13 | 9 | 6 | 2 | 1 |
| C14 | 10 | 1 | 6 | 3 |
| C15 | 9 | 2 | 7 | 0 |
| C16 | 10 | 4 | 6 | 0 |
| C17 | 11 | 7 | 3 | 1 |
| C18 | 7 | 1 | 4 | 2 |
| C19 | 11 | 3 | 4 | 4 |
| C20 | 7 | 0 | 6 | 1 |
| C21 | 8 | 0 | 4 | 4 |
| C22 | 16 | 4 | 3 | 9 |

## 6. Batch History

| Batch | Terms | Registries completed | Notes |
|-------|-------|---------------------|-------|
| VCB-001 | 178 | abomination, agony, ambition, anger, anguish (5) | |
| VCB-002 | 65 | anointing, anxiety, appetite, awe, bitterness, boldness, bondage, brokenness (8) | |
| VCB-003 | 112 | calling, character, compassion, condemnation, consecration, contentment, corruption (7) | |
| VCB-004 | 119 | conscience, courage, covenant, covetousness, debauchery, deceit, defilement, delight (8) | 2 errors fixed |
| VCB-005 | 81 | despair, devotion, dignity, diligence, discernment, disobedience (6) | |
| VCB-006 | 135 | distress, division, dread, endurance, envy (5) | + diff correction |
| VCB-007 | 74 | evil, experience, faith, faithfulness (4) | |
| VCB-008 | 112 | fear, fellowship, foolishness, forgiveness, generosity, gentleness, goodness, grace, gratitude, greed, grief, groaning (12) | |
| VCB-009 | 100 | hardness, hatred, holiness, honesty, hope, humility, hypocrisy, idolatry, imagination, impurity, indignation (11) | 1 deferred term |
| VCB-010 | 91 | iniquity, innocence, insight, integrity, intercession, jealousy, joy (7) | |
| VCB-011 | 25 | justice (1) | kindness partial |
| VCB-012 | 120 | kindness, knowledge, longing, love, lust, meaning, meditation (7) | + H2617A supplemental |
| **Total** | **1,212** | **81 registries** | |

---
*Produced 2026-04-02 by Claude Code. Schema v3.8.0.*