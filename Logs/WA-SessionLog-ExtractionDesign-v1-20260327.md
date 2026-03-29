# WA-SessionLog-ExtractionDesign-v1-20260327.md
Date: 2026-03-27
Status: IN PROGRESS — session ended at natural breakpoint. Resume from this log.

---

## 1. Session Scope

This session covered:
- Reading and confirming all Session B instruction documents (v5.1)
- Schema verification and Task 8 implementation gap identification
- Schema upgrade confirmation (v3.6.0 → v3.7.0)
- Completed extraction for Registry 112 — mind
- Design debate for two new post-patch output files
- Decisions on field structures for both new outputs
- Pending: write updated specification documents, then apply to remaining 5 words in cluster

---

## 2. Files in Project (confirmed readable)

| File | Status |
|---|---|
| WA-SessionB-Extraction-Instruction-v5_1-20260327.docx | Read — governing instruction for this session |
| WA-SessionB-DataPrep-Instruction-v5_1-20260327.docx | Read — reference |
| WA-SessionB-Analysis-Instruction-v5_1-20260327.docx | Not yet read in this session — not required for extraction |
| WA-Reference-v5-20260327.docx | Read — controlled vocabulary and schema reference |
| WA-SessionD-Orientation-v2-20260327.docx | Not yet read in this session |
| WA-Implementation-Instruction-v5-20260327.docx | Read (uploaded separately — not in project files) |
| database_schema_20260327.json | Updated schema v3.7.0 confirmed |
| word_registry.json | Read — 35 registries at Analysis Complete status |

---

## 3. Schema Status — Confirmed v3.7.0

All Task 8 fields confirmed present after Claude Code upgrade:

| Field / Table | Status |
|---|---|
| word_registry.cluster_assignment | ✅ |
| word_registry.sb_classification | ✅ |
| word_registry.sb_classification_reasoning | ✅ |
| word_registry.carry_forward | ✅ |
| wa_term_inventory.evidential_status | ✅ |
| wa_term_inventory.retention_note | ✅ |
| wa_session_b_dimensions | ✅ 13 columns |
| wa_session_b_findings | ✅ 9 columns |
| session_d_runs | ✅ |
| session_d_verse_links | ✅ |
| session_d_term_links | ✅ |
| session_d_observations | ✅ |

Interim mappings from Extraction Instruction Section 5 are **superseded**. Definitive mappings (Implementation Instruction Task 8.6) apply.

---

## 4. Extraction Batch — This Session

**Cluster: C01 — Cognitive/Mind**
Six registries selected for this extraction run:

| Registry | Word | Status |
|---|---|---|
| 112 | mind | ✅ COMPLETE — outputs produced |
| 182 | Soul | ⏳ Pending — files not yet uploaded |
| 183 | heart | ⏳ Pending |
| 184 | spirit | ⏳ Pending |
| 185 | flesh | ⏳ Pending |
| 211 | being | ⏳ Pending |

---

## 5. Registry 112 — Mind — Extraction Complete

**Outputs produced:**
- `wa-112-mind-json-20260327.json` — Session B JSON
- `wa-112-mind-patch-20260327.json` — Analysis completion patch

**Patch summary:**
- 78 × update_evidential_status on wa_term_inventory
- 1 × insert wa_session_b_dimensions (all 4 dimensions active)
- 1 × update_registry sb_classification = confirmed_characteristic
- 10 × insert wa_session_b_findings
- 10 × insert SD_POINTER flags on wa_session_research_flags
- 1 × update_registry session_b_status = Analysis Complete (final op)
- Total: 101 operations

**Key extraction notes:**
- Prior patch PATCH-20260327-112-SESSIONB-V1 had set session_b_status using interim mapping. New patch populates dedicated v3.7.0 fields.
- No extraction flags raised. Narrative complete and unambiguous.
- No session_b_revision_candidates identified.
- 52 confirmed / 23 plausible / 3 uncertain terms
- All 4 dimensions active: relational_environment, spirit_soul_body, inner_operations, being
- sb_classification: confirmed_characteristic

**Handoff to Claude Code — PENDING:**
Patch file wa-112-mind-patch-20260327.json submitted. Awaiting confirmation of application before Session D pointer and final extract outputs are produced (new output format not yet specified — see Section 7 below).

---

## 6. New Output Files — Design Decision in Progress

Two new post-patch outputs agreed in principle during this session. Specifications not yet written. These will be added to Reference v5.1 and Extraction Instruction v5.2 before the remaining five words are processed.

**Output 1: Final Registry Extract**
Filename pattern: `wa-{nnn}-{word}-final-{date}.json`
New scope token: `final`
Purpose: Self-contained cross-table extract of completed registry. Serves both Session D synthesis and future categorisation run.

**Output 2: Session D Pointers**
Filename pattern: `wa-{nnn}-{word}-sdpointers-{date}.json`
New scope token: `sdpointers`
Purpose: Evaluated, elaborated pointer file per registry. Aggregated at cluster level for Session D run. Not a pure data repeat — evaluative and analytical.

---

## 7. Confirmed Design Decisions

### 7.1 source_category field — repurposed
`word_registry.source_category` repurposed as `dimensions`.
- Multi-value, comma-delimited
- Derived from Session B dimensional analysis, not pre-assigned
- Replaces single-bucket classification
- Rationale: words are multi-dimensional; hard categorisation creates false boundaries that Session D has to fight against

### 7.2 Dimensional weight vocabulary
Three values only: **PRIMARY / SECONDARY / PERIPHERAL**
Applied to each of the four Framework B dimensions in the final registry extract.

### 7.3 synthesis_question — required field per pointer
- Each pointer in the sdpointers file carries one or more `synthesis_questions`
- Each is a single concise question Session D is asked to investigate
- Required — not optional
- Multiple questions per pointer are allowed

### 7.4 also_in_registries — pair format
Format: `[{registry_id, word}]` pairs
- Not registry_id alone
- Resolved at extraction time from word_registry.json
- Rationale: numbers alone are not reviewable or digestable

### 7.5 Session B revision candidates
- Formal field `session_b_revision_candidates` in final registry extract
- Empty array if none — explicit confirmation of no divergence
- Populated if extraction surfaces anything warranting narrative review
- Traceable record, not informal

### 7.6 Data quality flags in pointers
- Only carried into sdpointers if analytically relevant to Session D
- Pure data corrections with no cross-registry significance excluded
- Carried as pointer_type: data_quality_impact with same structure as other pointers
- Must include synthesis_question — why does this quality issue matter for cross-registry work

---

## 8. Proposed Field Structures — DRAFT (not yet in specification documents)

### Output 1 — Final Registry Extract

```
meta
  json_template_version
  json_filename
  registry_id
  word
  cluster_assignment
  produced_date
  session_b_instruction_version
  extraction_instruction_version

registry_summary
  word_label
  dimensions                    ← comma-delimited, multi-value
  cluster_assignment
  phase1_term_count
  phase1_verse_count
  active_term_count
  confirmed_count
  plausible_count
  uncertain_count
  session_b_status
  sb_classification
  carry_forward
  dimensional_profile {}
    relational_environment      ← weight: PRIMARY/SECONDARY/PERIPHERAL
    spirit_soul_body              + note
    inner_operations
    being
  evidential_weight {}
    confirmed_verse_count
    plausible_verse_count
    uncertain_verse_count       ← always 0, explicit
    dominant_terms []           ← top 5 by verse count with status

terms []
  strongs_id, transliteration, language
  mti_status, verse_count
  evidential_status, retention_note

dimensions {}                   ← full with notes (from Session B JSON)

inner_being_standing {}
  classification, reasoning, carry_forward

key_findings []
  finding_id, finding_type, finding, anchor_verses

session_b_revision_candidates []
  candidate_id, observation, recommended_action
```

### Output 2 — Session D Pointers

```
meta
  json_template_version
  json_filename
  registry_id
  word
  cluster_assignment
  produced_date
  extraction_instruction_version

registry_context {}
  sb_classification
  dimensions                    ← comma-delimited
  confirmed_count, plausible_count
  dominant_terms []             ← top 5

pointers []
  pointer_id
  pointer_type
    term_co_occurrence / verse_overlap / evidential_uncertainty /
    scope_boundary / data_quality_impact / structural_observation
  pointer_subtype
    term_co_occurrence:   shared_root / shared_gloss /
                          shared_domain / divergent_usage
    verse_overlap:        shared_verse / thematic_proximity
    evidential_uncertainty: thin_corpus / boundary_term /
                            cross_registry_dependency
    scope_boundary:       registry_border / cluster_border
    data_quality_impact:  affects_cross_registry / volume_concern /
                          classification_risk
    structural_observation: testament_shift / divine_human_parallel /
                            conceptual_gap
  significance              ← HIGH / MEDIUM / LOW
  strongs_id                ← null if word-level pointer
  also_in_registries []     ← [{registry_id, word}] pairs
  synthesis_questions []    ← REQUIRED, one or more
  research_depth_required   ← SURFACE / STANDARD / DEEP
  prose_note
  session_b_source_ref      ← e.g. "Section 10", "Section 7"

dimensional_summary {}      ← booleans only
  relational_environment, spirit_soul_body
  inner_operations, being

pointer_summary {}
  total_pointers
  by_type {}
  by_significance {}
  registries_implicated []  ← all {registry_id, word} pairs across file
  open_synthesis_questions  ← total count
```

---

## 9. Specification Documents — To Be Written (Next Session)

The following documents need to be produced before the remaining five words are processed:

| Document | Change | Version |
|---|---|---|
| WA-Reference-v5-20260327.docx | Add `final` and `sdpointers` scope tokens to Section 1.1. Repurpose source_category as dimensions field (Section 4). Add dimensional weight vocabulary. | v5.1 |
| WA-SessionB-Extraction-Instruction-v5_1-20260327.docx | Add Section on post-patch outputs (Output 1 and Output 2). Add field definitions. Add session_b_revision_candidates step. Add also_in_registries resolution instruction. | v5.2 |

---

## 10. Pending Items — Next Session

In order:

1. **Write WA-Reference-v5.1** — updated specification document
2. **Write WA-SessionB-Extraction-Instruction-v5.2** — updated specification document
3. **Upload narrative and JSON export for Registry 182 — Soul**
4. **Produce all three outputs for Soul:** Session B JSON, patch, final extract, sdpointers
   *(Note: mind final extract and sdpointers also to be produced once spec is confirmed)*
5. Continue through 183 heart, 184 spirit, 185 flesh, 211 being
6. **Prototype Session D run across all six words in the cluster**
7. Evaluate data volumes and completeness across the cluster outputs
8. Confirm or revise field structures based on prototype findings
9. Finalise specification documents

---

## 11. Open Questions — Carry Forward

- Should Claude Code or the extraction session resolve `also_in_registries` word labels? **Decision: extraction session resolves from word_registry.json**
- Bible study guide request: researcher has asked for simple digestable bible study guides based on single word narratives. To be actioned separately — not part of extraction workflow. Registry 112 mind narrative is a candidate.
- Future categorisation run: dimensional profiling approach confirmed as preferred over bucketing. Design of categorisation criteria deferred until Session D prototype is evaluated.

---

*WA-SessionLog-ExtractionDesign-v1-20260327.md | In progress | Continues next session*
