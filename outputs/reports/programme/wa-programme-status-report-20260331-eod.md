# Programme Status Report — 2026-03-31 (end of day)

> Schema v3.8.0 | VCB-001 through VCB-005 applied

## 1. Programme Overview

| Metric | Count |
|--------|-------|
| Total registries | 212 |
| Active | 179 |
| Excluded | 31 |
| Other | 2 |

## 2. Pipeline Status

| session_b_status | verse_context_status | Count |
|-----------------|---------------------|-------|
| Verse Context Reset | In Progress | 147 |
| Verse Context Reset | Complete | 34 |
| NULL | NULL | 31 |

## 3. Verse Context — Stage 1 Progress

| Metric | Count |
|--------|-------|
| Registries Complete | **34** / 181 (18.8%) |
| Registries In Progress | 147 |
| Batches processed | 5 (VCB-001 through VCB-005) |
| verse_context_group records | 716 |
| verse_context records | 12,331 |
| --- Anchors | 787 |
| --- Related | 4378 |
| --- Set aside | 7,166 |

### 3.1 Completed Registries

| Reg | Word | Cluster | Batch |
|-----|------|---------|-------|
| 1 | abomination | C12 | VCB-001 |
| 2 | agony | C05 | VCB-001 |
| 3 | ambition | C22 | VCB-001 |
| 4 | anger | C07 | VCB-001 |
| 5 | anguish | C05 | VCB-001 |
| 6 | anointing | C16 | VCB-002 |
| 7 | anxiety | C06 | VCB-002 |
| 8 | appetite | C04 | VCB-002 |
| 11 | awe | C03 | VCB-002 |
| 13 | bitterness | C07 | VCB-002 |
| 16 | boldness | C08 | VCB-002 |
| 17 | bondage | C14 | VCB-002 |
| 18 | brokenness | C05 | VCB-002 |
| 19 | calling | C19 | VCB-003 |
| 20 | character | C22 | VCB-003 |
| 23 | compassion | C17 | VCB-003 |
| 24 | condemnation | C13 | VCB-003 |
| 26 | conscience | C13 | VCB-004 |
| 28 | consecration | C16 | VCB-003 |
| 29 | contentment | C03 | VCB-003 |
| 31 | corruption | C11 | VCB-003 |
| 33 | courage | C08 | VCB-004 |
| 34 | covenant | C17 | VCB-004 |
| 35 | covetousness | C13 | VCB-004 |
| 39 | debauchery | C12 | VCB-004 |
| 40 | deceit | C11 | VCB-004 |
| 41 | defilement | C12 | VCB-004 |
| 42 | delight | C03 | VCB-004 |
| 44 | despair | C06 | VCB-005 |
| 46 | devotion | C08 | VCB-005 |
| 47 | dignity | C19 | VCB-005 |
| 48 | diligence | C08 | VCB-005 |
| 49 | discernment | C02 | VCB-005 |
| 50 | disobedience | C13 | VCB-005 |

### 3.2 Remaining Work

| Metric | Count |
|--------|-------|
| Terms unclassified | 1,917 |
| Verses to classify | 45,663 |
| Estimated batches remaining | ~20 |

### 3.3 Partial Registries

| Reg | Word | Classified | Total | Remaining |
|-----|------|-----------|-------|-----------|
| 32 | counsel | 11 | 12 | 1 |
| 43 | desire | 45 | 47 | 2 |
| 51 | distress | 4 | 73 | 69 |

## 4. Data Health

| Check | Value | Status |
|-------|-------|--------|
| Active mti_terms (1 per Strong) | 3807 | CLEAN |
| Multi-OWNER strongs | 0 | CLEAN |
| OWNER ti | 3647 | |
| XREF ti | 3341 | |
| Active verses | 85,116 | |

## 5. Cluster Progress

| Cluster | Words | VC Complete | In Progress | Excluded |
|---------|-------|-------------|-------------|----------|
| C01 | 6 | 0 | 6 | 0 |
| C02 | 13 | 1 | 12 | 0 |
| C03 | 9 | 3 | 6 | 0 |
| C04 | 7 | 1 | 6 | 0 |
| C05 | 9 | 3 | 6 | 0 |
| C06 | 8 | 2 | 5 | 1 |
| C07 | 10 | 2 | 7 | 1 |
| C08 | 11 | 4 | 7 | 0 |
| C09 | 10 | 0 | 7 | 3 |
| C10 | 11 | 0 | 10 | 1 |
| C11 | 10 | 2 | 8 | 0 |
| C12 | 10 | 3 | 7 | 0 |
| C13 | 9 | 4 | 4 | 1 |
| C14 | 10 | 1 | 6 | 3 |
| C15 | 9 | 0 | 9 | 0 |
| C16 | 10 | 2 | 8 | 0 |
| C17 | 11 | 2 | 8 | 1 |
| C18 | 7 | 0 | 5 | 2 |
| C19 | 11 | 2 | 5 | 4 |
| C20 | 7 | 0 | 6 | 1 |
| C21 | 8 | 0 | 4 | 4 |
| C22 | 16 | 2 | 5 | 9 |

## 6. Session Summary (2026-03-30 to 2026-03-31)

### Data fixes (2026-03-30)
- mti_terms deduplicated: 3,616 duplicates + 64 orphans flagged
- OWNER/XREF fixed: 1,871 excess OWNERs flipped, 48,237 XREF verses flagged
- All required fields backfilled; audit_word.py guarded against future duplicates
- delete_flagged column added to mti_terms
- apply_session_patch.py: verse_context insert/update operations added
- File organisation rules published; project files reorganised

### Verse Context batches

| Batch | Terms | Verses | Registries completed |
|-------|-------|--------|---------------------|
| VCB-001 | 178 | 2,470 | abomination, agony, ambition, anger, anguish (5) |
| VCB-002 | 65 | 2,485 | anointing, anxiety, appetite, awe, bitterness, boldness, bondage, brokenness (8) |
| VCB-003 | 112 | 2,490 | calling, character, compassion, condemnation, consecration, contentment, corruption (7) |
| VCB-004 | 119 | 2,496 | conscience, courage, covenant, covetousness, debauchery, deceit, defilement, delight (8) |
| VCB-005 | 81 | 2,495 | despair, devotion, dignity, diligence, discernment, disobedience (6) |
| **Total** | **555** | **12,436** | **34 registries** |

---
*Produced 2026-03-31 by Claude Code. Schema v3.8.0.*