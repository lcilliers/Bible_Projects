# WA Patch Type Registry — 2026-04-20

_Schema 3.13.0 · source: `wa_patch_type_registry`._

---

## Summary

**Patch types:** 15  ·  **session_b_status required:** 2  ·  **exempt:** 13

## Patch types

| Type | Req sb_status | Governing | Schema affected | Description |
|---|:---:|---|---|---|
| `CATALOGUE_POPULATION` | — | wa-reference / wa-patch-instruction | wa_obs_question_catalogue | Observation question catalogue population patch |
| `CLUSTERING` | — | wa-registry-management-guide [current] | word_registry | Cluster assignment patch |
| `DIMREVIEW` | — | wa-dimensionreview-instruction [current] | wa_dimension_index, verse_context_group, wa_session_b_findings, wa_session_research_fla... | Dimension Review per-registry patch — dimension + dominant_subject + optional Phase B revisions + registry stamp |
| `DIMREVIEW-GRPDESC` | — | wa-dimensionreview-instruction [current] | verse_context_group, wa_dimension_index | Dimension Review group-description correction patch |
| `PREANALYSIS` | required | wa-patch-instruction [current] | wa_term_inventory, word_registry | Session B Stage 1 Pre-Analysis patch — evidential status + dimensions + pre-analysis findings |
| `PROSE` | — | wa-patch-instruction [current]; prose-store-design-v1 | prose_section, prose_section_dimension_link, prose_section_finding_link | Prose section insert/supersede/approve (narrative Session A/B/C/D output + programme-stage content) |
| `READINESSSWEEP` | — | wa-global-readiness-sweep-instruction [current] | wa_data_quality_flags, mti_terms | Readiness sweep mechanical remediation patch (Path 1 items) |
| `REPAIR` | — | wa-patch-instruction [current] | varies (recovery-specific) | REPAIR patch — recovery from failed apply or data-state corrections |
| `SDPOINTERS` | — | wa-sessiond-orientation [current] | wa_session_research_flags | Session D pointer cluster patch — batches of SD pointers |
| `SESSIONB` | required | wa-patch-instruction [current] | wa_session_b_findings, wa_session_b_dimensions, wa_session_research_flags, word_registry | Session B Stage 2 analysis-complete patch — findings + dimensions + SD pointers + registry stamps |
| `SESSIONB_FINDINGS` | — | wa-patch-instruction [current] | wa_session_b_findings, wa_finding_entity_links | Session B Stage 2b findings-only patch (finer-grained than SESSIONB) |
| `SESSIOND` | — | wa-sessiond-orientation [current] | session_d_observations, session_d_runs, session_d_verse_links, session_d_term_links | Session D cross-registry synthesis patch |
| `VCGROUP` | — | wa-versecontext-instruction [current] | verse_context_group | Verse Context per-group patch |
| `VCVERSE` | — | wa-versecontext-instruction [current] | verse_context | Verse Context per-verse patch |
| `VERSECONTEXT` | — | wa-versecontext-instruction [current] | verse_context, verse_context_group | Verse Context patch — batch-level classification of verse-context groups |

---
*Generated 2026-04-20T16:45:01Z.*