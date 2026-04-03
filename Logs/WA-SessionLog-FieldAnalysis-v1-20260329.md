# WA-SessionLog-FieldAnalysis-v1-20260329

**Project:** Framework B — Soul Word Analysis Programme
**Session date:** 2026-03-29
**Session type:** Analytical review — instruction gaps, inflection point status, and systematic field analysis of word_registry and wa_term_inventory
**Continues from:** WA-SessionLog-InflectionPointFixes-v2-20260329.md
**Produced by:** Claude AI

---

## 1. Session Objective

This session had two declared tasks from the previous session log:
1. Produce WA-InstructionGaps-v2 — mark resolved gaps, confirm open items
2. Produce WA-InflectionPointReview-v2 — re-assess all 15 inflection points

The session did not reach document production. Instead it identified a significant body of analytical work required before those documents can be produced accurately. That work is now substantially complete and documented in this log. Document production is the next session's first task.

---

## 2. Documents Available This Session

| Document | Version | Source |
|---|---|---|
| WA-SessionLog-InflectionPointFixes-v2 | v2 | In context |
| WA-InstructionGaps-v1 | v1 | Uploaded |
| WA-InflectionPointReview-v1 | v1 | Uploaded |
| WA-SessionB-DataPrep-Instruction | v5.4 | Uploaded |
| WA-SessionB-Analysis-Instruction | v5.3 | Uploaded |
| WA-SessionB-Extraction-Instruction | v5.4 | Uploaded |
| WA-VerseContext-Instruction | v1.2 | Uploaded |
| WA-SessionB-ClaudeCode-Instructions | v3 | Uploaded |
| WA-Registry-Management-Guide | v5.5 | Uploaded |
| patch_specification | v1.4 | Uploaded |
| WA-Reference | v5.3 | Project file |
| database_schema | 2026-03-29 | Project file |
| wa-registry-overview | 2026-03-29 | Project file |
| Session-A-Instruction | v8-final | Project file |
| WA-SessionD-Orientation | v2.1 | Project file |

---

## 3. Decisions Made This Session

All decisions are the researcher's. Recorded here for instruction update accuracy.

### 3.1 IP-12 / G15 / G26 — bulk_update operation

**Decision:** Remove `bulk_update` from the Analysis closing patch. The operation does not exist in the patch specification and its definition is premature. Replace Section 12 with a researcher checkpoint rule: when a situation arises requiring bulk updates for which no standard patch operation is defined, Claude AI must surface a field-level proposal to the researcher (describing all fields to be updated, proposed values, and operation count) before constructing any patch. This prevents partial updates and data errors.

**Consequence:** The Analysis closing patch contains only `registry_note` and `update_registry` for `session_b_status = Analysis Complete`. No bulk status_note write to `mti_terms`. The `mti_terms.status_note` write is removed from the Analysis session entirely.

**Documents to update:** WA-SessionB-Analysis-Instruction v5.3 → v5.4 (Section 12)

### 3.2 G16 — evidential_status table and field

**Decision confirmed:** `mti_terms.status` and `mti_terms.status_note` are DataPrep classification fields. They have no relationship to evidential status.

`wa_term_inventory.evidential_status` is the sole formal record of analytical classification. It is written by the Extraction session only, via the `update_evidential_status` operation. Analysis determines evidential status and records it in the narrative; Extraction writes it to the database.

**OWNER-only rule confirmed:** `update_evidential_status` operations target `term_owner_type = 'OWNER'` records only. XREF terms inherit evidential status from their OWNER registry. This rule must be explicitly stated in the Extraction Instruction.

**Same term, different words:** The same term may carry different `evidential_status` values on different word registries, because `wa_term_inventory` records are word-specific. This confirms `wa_term_inventory` (not `mti_terms`) as the correct table.

**Documents to update:** WA-SessionB-Extraction-Instruction v5.4 → v5.5 (Section 6, Annexure B — add OWNER-only rule)

### 3.3 G09 / G20 — intra_pool column

**Decision:** Do not add `intra_pool` column to `wa_session_b_findings`. Use `finding_type = 'pool_observation'` as the discriminator. Already implemented in v5.4. Gap closed.

### 3.4 file_id handling

**Decision:** No change. Current v5.4 approach (use `files[0].id` with `phase = 'Phase 1'`) stands. `wa_file_index` remains as-is — architectural improvement deferred.

### 3.5 Field-by-field analysis — Group 1 (engine-derived fields)

Fields: `phase1_term_count`, `phase1_verse_count`, `unique_term_count`, `shared_term_count`, `term_sharing_ratio`, `strongs_list`

**Decision:** These fields are owned by the data extraction engine only. They reflect the Phase 1 extraction state and are not updated by the pipeline. Any count of active terms or verses post-DataPrep must be derived from live queries against `mti_terms` and `wa_term_inventory`, not from these registry summary fields.

**Action:** Document this constraint in Reference and Registry Management Guide. No patch operations needed. GAP-E, F, G, H, I, J closed by documentation note.

### 3.6 Field-by-field analysis — Group 2 (analytical fields requiring Session B re-evaluation)

**Decision:** Any Phase 1 value that could change because of analysis must be re-evaluated and confirmed by Session B.

Fields and specific decisions:

| Field | Table | Decision |
|---|---|---|
| `dimensions` | `word_registry` | Session B Extraction writes Session B multi-value dimensional result via `update_registry`. Replaces Phase 1 category_hint value. |
| `description` | `word_registry` | Session B Extraction writes a Session B confirmed description via `update_registry`. Replaces Phase 1 preliminary description. |
| `god_as_subject` | `wa_term_inventory` | **Redundant** — fully duplicated by `mti_term_flags` flag_id 1 (GOD_AS_SUBJECT). Mark as redundant in instructions. No Session B update needed. |
| `somatic_link` | `wa_term_inventory` | **Redundant** — fully duplicated by `mti_term_flags` flag_id 3 (SOMATIC_INNER_LINK) and flag_id 4 (BODY_INNER_EXPRESSION). Mark as redundant in instructions. No Session B update needed. |

GAP-A (`dimensions`) and GAP-D (`description`) require new `update_registry` operations in the Extraction patch. GAP-K (`god_as_subject`) and GAP-L (`somatic_link`) closed as redundant.

### 3.7 Field-by-field analysis — Group 3 (undefined fields)

| Field | Table | Decision |
|---|---|---|
| `inference_note` | `word_registry` | **Redundant** — mark as redundant in instructions. No pipeline stage writes to it. Note: field contains pre-existing content in live data for conceptual gap words. This content was researcher-set at programme intake and is not lost by marking the field redundant in instructions — it remains in the database. No pipeline operation should update it. |
| `status_note` | `wa_term_inventory` | **Redundant** — NULL across all records. No documented purpose. Mark as redundant in instructions. Leave NULL. |

### 3.8 Minor gaps — deferred

| Gap | Field | Decision |
|---|---|---|
| GAP-M | `occurrence_count` (`wa_term_inventory`) | Minor — DataPrep flags contamination but no correction path. Document that correction requires researcher decision and manual patch. No instruction change to pipeline flow. |
| GAP-N | `testament` (`wa_term_inventory`) | Minor — may change after DataPrep verse reassignment. Note as engine responsibility for re-derivation. |

---

## 4. Relational Structure Findings — Recorded for Completeness

A systematic review of the database foreign key structure was conducted. Key findings:

1. `wa_term_inventory` has no direct FK to `word_registry`. The join path is: `wa_term_inventory.file_id → wa_file_index.id → wa_file_index.word_registry_fk → word_registry.id`

2. `wa_session_b_findings` and `wa_session_b_dimensions` have no declared FK constraints. They reference `word_registry` via `registry_id` by convention only.

3. `file_id` on findings and dimensions tables serves a legitimate join path back to `wa_term_inventory` — it is not redundant despite appearing so. Without it, findings cannot be joined to specific term inventory records.

4. An architectural opportunity to add a direct FK from `wa_term_inventory` to `word_registry` was identified. **Decision:** deferred — not required for the dry run and would require a schema migration touching 8 tables and 224,529+ rows.

---

## 5. Gap Status Update — Preliminary (for InstructionGaps-v2)

This is a working assessment. WA-InstructionGaps-v2 must be produced in the next session to formalise these statuses.

| Gap | Original severity | Status | Resolution |
|---|---|---|---|
| G01 | BLOCKING | **Still open** | Batch construction SQL not specified |
| G02 | AMBIGUOUS | **Still open** | term_classification_complete for partial state |
| G03 | AMBIGUOUS | **Still open** | term_classification_complete = true handling |
| G04 | MISSING | **Still open** | Group count guidance |
| G05 | BLOCKING | **Still open** | All verses fail relevance filter |
| G06 | INCONSISTENT | **Still open** | Ready for Analysis status not in VC Instruction |
| G07 | MISSING | **Still open** | Progress reporting across registries |
| G08 | BLOCKING | **Still open** | Batch JSON construction queries |
| G09 | BLOCKING | **Closed** | intra_pool → finding_type = pool_observation (v5.4) |
| G10 | BLOCKING | **Still open** | Pool membership not in database |
| G11 | AMBIGUOUS | **Closed** | FIX-R5 — pool_id controlled vocabulary in RMG v5.5 |
| G12 | BLOCKING | **Closed** | FIX-R1 — mandatory minimal patch always produced |
| G13 | MISSING | **Still open** | mti_terms vs wa_term_inventory identifier |
| G14 | BLOCKING | **Still open** | Simultaneous threshold undefined |
| G15 | BLOCKING | **Decision made** | bulk_update removed; researcher checkpoint rule replaces it. Requires Analysis Instruction update → v5.4 |
| G16 | AMBIGUOUS | **Decision made** | wa_term_inventory.evidential_status is sole formal record; OWNER-only rule added. Requires Extraction Instruction update → v5.5 |
| G17 | MISSING | **Still open** | Quality flag handling in analysis |
| G18 | AMBIGUOUS | **Still open** | Root data absent from pool dataset |
| G19 | MISSING | **Closed** | FIX-R5 — pool_id format documented |
| G20 | BLOCKING | **Closed** | Aligned with G09 — finding_type = pool_observation (v5.4) |
| G21 | AMBIGUOUS | **Still open** | pool_observations not in database |
| G22 | MISSING | **Still open** | Broken cross-reference to Reference Section 4.3 — needs verification |
| G23 | MISSING | **Closed** | Resolved in Extraction v5.4 |
| G24 | AMBIGUOUS | **Closed** | Resolved in Extraction v5.4 — files[0].id with phase=Phase 1 |
| G25 | INCONSISTENT | **Closed** | Resolved in Analysis v5.3 — ANALYSIS infix on patch name |
| G26 | BLOCKING | **Decision made** | bulk_update removed entirely. Requires Analysis Instruction update → v5.4 |
| G27 | MISSING | **Closed** | Resolved in Extraction v5.4 — Section 9 Session B Complete patch |
| G28 | AMBIGUOUS | **Still open** | strongs_number matching ambiguity |
| G29 | MISSING | **Decision made** | dimensions update via update_registry in Extraction patch. Requires Extraction Instruction update → v5.5 |
| G30 | MISSING | **Still open** | extracted_theological_anchor handling in DataPrep |
| GAP-A | NEW-MISSING | **Decision made** | dimensions update — same as G29 |
| GAP-B | NEW-AMBIGUOUS | **Closed** | inference_note — redundant. Mark in instructions. |
| GAP-C | NEW-AMBIGUOUS | **Closed** | wa_term_inventory.status_note — redundant. Mark in instructions. |
| GAP-D | NEW-MISSING | **Decision made** | description update via update_registry in Extraction patch |
| GAP-E/F/G/H/I/J | NEW-MISSING | **Closed** | Engine-derived fields — document as Phase 1 counts, not pipeline-updated |
| GAP-K | NEW-MISSING | **Closed** | god_as_subject redundant — duplicated by mti_term_flags flag_id 1 |
| GAP-L | NEW-MISSING | **Closed** | somatic_link redundant — duplicated by mti_term_flags flag_id 3/4 |
| GAP-M | NEW-MINOR | **Deferred** | occurrence_count — researcher patch decision |
| GAP-N | NEW-MINOR | **Deferred** | testament — engine re-derivation responsibility |

---

## 6. Inflection Point Status Update — Preliminary (for InflectionPointReview-v2)

Working assessment. InflectionPointReview-v2 must be produced in the next session.

| IP | Previous verdict | Current status |
|---|---|---|
| IP-01 | Partially specified | Unchanged — still needs one clarifying sentence on DB vs export |
| IP-02 | Substantially specified | **Improved** — FIX-R3 added source tables |
| IP-03 | Fully specified | Unchanged — still fully specified |
| IP-04 | JSON specified, queries missing | **Improved** — FIX-R3 added source tables |
| IP-05 | Fully specified | Unchanged |
| IP-06 | JSON specified, tables missing | **Improved** — FIX-R3 added source tables |
| IP-07 | Fully specified | Unchanged |
| IP-08 | Process specified, JSON undocumented | **Improved** — FIX-R4 added Annexure C |
| IP-09 | Patch specified; status gap | **Resolved** — FIX-R1 mandatory patch always produced |
| IP-10 | Process specified, JSON undocumented | **Improved** — FIX-R4 covers this |
| IP-11 | JSON specified; CC placeholder stale | **Resolved** — FIX-R2 updated ClaudeCode Instructions Section 14.8 |
| IP-12 | **BLOCKING** — bulk_update missing | **Decision made** — bulk_update removed; Analysis Instruction update pending → v5.4 |
| IP-13 | Inputs listed; word_registry.json undefined | **Resolved** — Extraction v5.4 defines word_registry.json |
| IP-14 | Substantially specified; intra_pool blocking | **Substantially resolved** — intra_pool closed (v5.4); new update_registry operations for description and dimensions pending Extraction v5.5 |
| IP-15 | Adequately specified | Unchanged |

**BLOCKING items remaining after this session:**
- IP-12 — still requires Analysis Instruction v5.4 to be produced
- G01, G05, G08, G10, G14 — batch construction, all-verses-fail, pool membership, simultaneous threshold

---

## 7. Document Changes Required — Next Session Work Order

The following document updates are required. They must be produced in order due to cross-references.

### Priority 1 — Apply decisions from this session

| Document | Current version | New version | Changes required |
|---|---|---|---|
| WA-SessionB-Analysis-Instruction | v5.3 | **v5.4** | Section 12: remove bulk_update and mti_terms.status_note write; replace with researcher checkpoint rule; simplify patch to registry_note + update_registry only; update patch template and _patch_summary |
| WA-SessionB-Extraction-Instruction | v5.4 | **v5.5** | Section 6: add OWNER-only rule for update_evidential_status; add update_registry operations for `description` and `dimensions` to analysis completion patch; Section 8.1: update description and dimensions field guidance; Annexure B: add description and dimensions update_registry ops to patch template; mark god_as_subject and somatic_link as redundant (duplicated by flags) |
| WA-Reference | v5.3 | **v5.4** | Section 13.1: mark inference_note, wa_term_inventory.status_note, god_as_subject, somatic_link as redundant fields; add note that Group 1 engine fields reflect Phase 1 state only |
| WA-Registry-Management-Guide | v5.5 | **v5.6** | Add note on engine-derived fields (Group 1) — Phase 1 state only, not pipeline-updated |

### Priority 2 — Produce updated review documents

| Document | Current version | New version | Changes required |
|---|---|---|---|
| WA-InstructionGaps | v1 | **v2** | Update all gap statuses per Section 5 of this session log; add new GAPs; mark closed items with resolution note |
| WA-InflectionPointReview | v1 | **v2** | Re-assess all 15 IPs against updated document suite; confirm blocking status |

### Priority 3 — Dry run gate assessment

Once InstructionGaps-v2 is complete, assess whether remaining BLOCKING gaps prevent the gratitude dry run. Current assessment: **G01, G05, G08, G10, G14 remain BLOCKING** and must be resolved or explicitly accepted by researcher before dry run begins.

---

## 8. Still-Open Questions Requiring Researcher Decision

These were not resolved in this session and must be addressed before the relevant document updates:

| # | Question | Impacts |
|---|---|---|
| Q-A | G22: does Reference v5.3 Section 4.3 now exist (was a broken cross-reference in Extraction)? Needs a quick verification read. | Extraction Instruction v5.5 |
| Q-B | G14: what is the threshold for simultaneous vs word-by-word analysis? A number must be specified. | Analysis Instruction v5.4 |
| Q-C | G01/G08: are batch construction SQL queries Claude Code's responsibility (derive from schema) or must they be specified in instructions? Researcher previously indicated queries are CC's responsibility — confirm this applies here. | VerseContext Instruction v1.3 |
| Q-D | G05: what should Claude AI do when ALL verses for a term fail the relevance filter? Options: (a) flag to researcher and stop, (b) mark term as no inner-being engagement, (c) designate least-irrelevant verse as anchor with note. | VerseContext Instruction v1.3 |
| Q-E | G10: pool membership must be queryable from the database for the pool readiness check. Currently only defined in RMG prose. Should a `pool_id` column be added to `word_registry`, or is the RMG Section 7a table sufficient for Claude Code to derive pool membership? | DataPrep Instruction; possibly schema |

---

## 9. Key Observations — For Researcher Reflection

These are observations, not decisions. Recorded for the researcher's consideration.

1. **The field analysis revealed more surface area than expected.** The `description` and `dimensions` gaps (GAP-A, GAP-D) mean that every completed Session B word analysis to date has not updated these registry fields. For the six C01 words already completed, these fields are stale. A backfill approach will be needed.

2. **The redundancy findings (god_as_subject, somatic_link, inference_note, wa_term_inventory.status_note) are genuinely redundant** — not just unused. The flag mechanism is the authoritative record. Documenting this reduces confusion for future sessions.

3. **BLOCKING gaps G01, G08, G10** concern Claude Code's ability to construct batch JSONs and check pool readiness without SQL queries in the instructions. The researcher's prior direction was that queries are CC's responsibility. If this is confirmed for these gaps, they close immediately — reducing the BLOCKING count significantly before the dry run.

4. **The dry run gate is closer than the raw gap count suggests.** Many of the 30 original gaps have been closed or are closable by confirming existing decisions. The genuine blockers for the gratitude dry run are: G14 (threshold number needed), G05 (all-verses-fail behaviour), and G10 (pool membership queryability). These are three researcher decisions, not three document rewrites.

---

## 10. Session Log — End State

| Item | State |
|---|---|
| Decisions made | 9 substantive decisions — all recorded in Section 3 |
| Document changes pending | 4 instruction updates + 2 review documents |
| BLOCKING gaps closed this session | G09, G12, G15, G20, G26 (decision made; documents pending) |
| BLOCKING gaps still open | G01, G05, G08, G10, G14 |
| New gaps identified and closed | GAP-B, C, E, F, G, H, I, J, K, L |
| New gaps requiring document updates | GAP-A, D (→ Extraction v5.5) |
| Dry run gate status | Not yet clear — 3 researcher decisions needed (see Section 8, Q-B, Q-D, Q-E) |

---

*WA-SessionLog-FieldAnalysis-v1-20260329 | Systematic field analysis complete | 9 decisions made | 4 documents pending update | Next session: produce document updates then InstructionGaps-v2 and InflectionPointReview-v2*
