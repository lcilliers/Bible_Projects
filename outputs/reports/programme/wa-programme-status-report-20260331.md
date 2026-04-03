# Programme Status Report — 2026-03-31

> Schema v3.8.0 | Post mti_terms dedup + OWNER/XREF fix | VCB-001 + VCB-002 applied

## 1. Programme Overview

| Metric | Count |
|--------|-------|
| Total registries | 212 |
| Active (Phase 1 Complete, has terms) | 179 |
| Excluded (Phase 1) | 31 |
| Zero-term / other | 2 |

## 2. Pipeline Status

### 2.1 Combined Status Matrix

| session_b_status | verse_context_status | Count |
|-----------------|---------------------|-------|
| Verse Context Reset | In Progress | 168 |
| NULL | NULL | 31 |
| Verse Context Reset | Complete | 13 |

## 3. Verse Context — Stage 1 Progress

| Metric | Count |
|--------|-------|
| Registries Complete | **13** / 181 (7.2%) |
| Registries In Progress | 168 |
| Registries outside scope (NULL) | 31 |
| Batches processed | 2 (VCB-001, VCB-002) |
| verse_context_group records | 298 |
| verse_context records | 4,978 |
| --- Anchor verses | 302 |
| --- Related verses | 948 |
| --- Set aside | 3,728 |
| --- Total relevant | 1250 |

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

### 3.2 Remaining Work

| Metric | Count |
|--------|-------|
| OWNER terms still unclassified | 2,229 |
| Verses to classify | 53,144 |
| Estimated batches remaining | ~23 |

## 4. Data Health

| Check | Value | Status |
|-------|-------|--------|
| Active mti_terms | 3807 | |
| Deleted mti_terms | 3680 | |
| Duplicate strongs | 0 | CLEAN |
| Multi-OWNER strongs | 0 | CLEAN |
| owning_registry_fk NULL | 0 | CLEAN |
| mti status NULL | 0 | CLEAN |
| OWNER ti records | 3647 | |
| XREF ti records | 3341 | |
| Active verses | 85,116 | |

### 4.1 mti_terms Status Distribution

| Status | Count | % |
|--------|-------|---|
| extracted | 2233 | 58.7% |
| delete | 1185 | 31.1% |
| extracted_thin | 305 | 8.0% |
| candidate_delete | 62 | 1.6% |
| extracted_theological_anchor | 15 | 0.4% |
| xref_distress | 2 | 0.1% |
| phase2_enrichment | 1 | 0.0% |
| xref_anger | 1 | 0.0% |
| xref_desire | 1 | 0.0% |
| xref_sorrow | 1 | 0.0% |
| xref_wisdom | 1 | 0.0% |

## 5. Cluster Progress

| Cluster | Words | VC Complete | VC In Progress | Excluded/NULL |
|---------|-------|-------------|----------------|---------------|
| C01 | 6 | 0 | 6 | 0 |
| C02 | 13 | 0 | 13 | 0 |
| C03 | 9 | 1 | 8 | 0 |
| C04 | 7 | 1 | 6 | 0 |
| C05 | 9 | 3 | 6 | 0 |
| C06 | 8 | 1 | 6 | 1 |
| C07 | 10 | 2 | 7 | 1 |
| C08 | 11 | 1 | 10 | 0 |
| C09 | 10 | 0 | 7 | 3 |
| C10 | 11 | 0 | 10 | 1 |
| C11 | 10 | 0 | 10 | 0 |
| C12 | 10 | 1 | 9 | 0 |
| C13 | 9 | 0 | 8 | 1 |
| C14 | 10 | 1 | 6 | 3 |
| C15 | 9 | 0 | 9 | 0 |
| C16 | 10 | 1 | 9 | 0 |
| C17 | 11 | 0 | 10 | 1 |
| C18 | 7 | 0 | 5 | 2 |
| C19 | 11 | 0 | 7 | 4 |
| C20 | 7 | 0 | 6 | 1 |
| C21 | 8 | 0 | 4 | 4 |
| C22 | 16 | 1 | 6 | 9 |

## 6. Next Steps

1. **Continue Stage 1 Verse Context** — ~23 batches remaining (2,229 terms, 53,144 verses)
2. VCB-003 ready for construction
3. 13 registries have DataPrep gate open — DataPrep can begin for these when Verse Context sweep is further along
4. No registries yet at Pre-Analysis Complete

---
*Produced 2026-03-31 by Claude Code. Schema v3.8.0.*