# WA — Session B Instruction: Step 1.2 Corrected Draft
**Filename:** wa-global-sessionb-step1-2-corrected-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Replaces:** Step 1.2 from wa-global-sessionb-stage1-draft-v1-20260416.md
**Previous output refs:**
- wa-global-sessionb-stage1-draft-v1-20260416.md (Step 1.2 — three problems identified)
- wa-global-sessionlog-sessionb-redesign-v2-20260416.md (problem definitions)
- database-schema-20260416.json (schema v3.9.0 — basis for field coverage)

---

## Corrections Applied

**Problem 1 — Phase 2 deferrals:** `god_as_subject` and `somatic_link` are no longer deferred to Phase 2. Step 1.2 now specifies exactly what can be checked in Stage 1 (field presence, value plausibility against term type) and what is noted as provisional for Stage 2a verification. The instruction is internally consistent.

**Problem 2 — Terms of reference:** Every field check now states what the field must contain, what valid values are, what to compare against, and what constitutes an anomaly requiring action.

**Problem 3 — Field coverage:** Step 1.2 is rebuilt against schema v3.9.0. Every table present in the extract has a checklist section. Cross-field and cross-table consistency checks are specified throughout.

---

## Step 1.2 — Read and Audit the Complete JSON

Read the complete word data export in full before beginning any checklist. Do not check fields as you encounter them — read the entire extract first, form an overall picture of the data, then work through each checklist section systematically.

Record every gap, anomaly, or concern in the observations log at the moment it is identified — per GR-OBS-001. Do not accumulate issues in memory for later recording.

The audit has seven sections corresponding to the main data areas in the extract. All seven sections must be completed before proceeding to Step 1.3.

---

### Section A — Registry Record (`word_registry`)

One row per word. These fields describe the word's overall programme state.

**Request from CC if not already in the extract:** Return the `word_registry` row for registry [nnn] with all fields.

| Field | Valid state at Session B entry | Check | Anomaly action |
|-------|-------------------------------|-------|----------------|
| `word` | Matches the word being analysed | Confirm spelling matches session context | Note mismatch — RESEARCHER_DECISION |
| `no` | Matches registry number [nnn] | Confirm | Note mismatch — stop |
| `cluster_assignment` | A valid cluster code (C01–C22) or 'unassigned' | Present and not NULL | Note if NULL — may indicate incomplete registration |
| `session_b_status` | Must be `Pre-Analysis Complete` at Session B entry. Acceptable legacy entry: `Verse Context Reset` | Check against valid values (Appendix A.5 of patch spec) | If `Analysis Complete` or `Session B Complete` — STOP. Session B already run. Confirm with researcher before proceeding. If NULL — raise RESEARCHER_DECISION: word may not have passed through DataPrep. |
| `verse_context_status` | Must be `Complete` | Confirmed against valid values (Appendix A.7 of patch spec) | If not `Complete` — STOP. Session B cannot begin. Verse Context must complete first. |
| `dimensions` | Populated — at least one dimension string present | Not NULL, not empty string | NULL or empty — note as gap; check whether Dimension Review was completed |
| `dim_review_status` | `Complete` or `COMPLETE` | Present and matches expected value | If absent or incomplete — may indicate Dimension Review sub-process is required |
| `dim_review_version` | Populated | Not NULL | NULL — note; not blocking but record |
| `carry_forward` | Default 1 | If 0 — note explicitly | 0 means this registry is flagged for exclusion. Confirm with researcher whether to proceed. |
| `unique_term_count` | > 0 | Cross-check: count OWNER terms in extract and compare | If extract term count ≠ `unique_term_count` — note discrepancy; may indicate stale registry data |
| `shared_term_count` | ≥ 0 | Present | NULL — note |
| `term_sharing_ratio` | Between 0.0 and 1.0 | Plausibility check: `shared_term_count / (unique_term_count + shared_term_count)` should approximate this value | Significant deviation — note; not blocking but record |
| `phase1_term_count` | > 0 | Present | NULL or 0 — note; may indicate incomplete Session A |
| `phase1_verse_count` | > 0 | Present | NULL or 0 — note |
| `description` | May be NULL at this stage | No action required | — |
| `sb_classification` | May be NULL at this stage | Note value if present | — |

**Cross-field check A1:** `verse_context_status = 'Complete'` AND `dim_review_status = 'Complete'` must both be true before Stage 1 can proceed. If either is absent, record as a hard gate failure.

---

### Section B — Term Inventory (`wa_term_inventory` + `mti_terms`)

One row per term per registry in `wa_term_inventory`. Linked to `mti_terms` via the term's Strong's number. Work through each term in the extract.

**Governing rule:** Only terms with `mti_terms.status IN ('extracted', 'extracted_thin')` are active analytical terms per GR-DATA-001. Terms with `status = 'delete'`, `'excluded'`, or `'xref_[word]'` are out of analytical scope for this registry — note their presence but do not analyse them.

**For each active term (`mti_terms.status IN ('extracted', 'extracted_thin')`):**

| Field | Valid state | Check | Anomaly action |
|-------|------------|-------|----------------|
| `strongs_number` | Format: H[0-9]+ for Hebrew, G[0-9]+ for Greek. No embedded spaces. | Verify format with regex pattern | Malformed — add to Type (a) patch: correct the value |
| `language` | 'Hebrew' or 'Greek' — consistent with the Strong's number prefix (H = Hebrew, G = Greek) | Cross-check: H prefix → language = 'Hebrew'; G prefix → language = 'Greek' | Mismatch — add to Type (a) patch: correct the language field |
| `transliteration` | Present and not empty | Not NULL | NULL — note; not blocking |
| `step_search_gloss` | Present for active terms | Not NULL | NULL — note; not critical if `word_analysis_gloss` is present |
| `word_analysis_gloss` | Present for active terms | Not NULL | NULL on both glosses — note as data gap; term may lack STEP data |
| `occurrence_count` | > 0 for active terms | Numeric, > 0 | 0 or NULL — note; cross-check against verse record count |
| `mti_terms.status` | `extracted` or `extracted_thin` for active terms | Confirm value is in controlled vocabulary (Appendix A.4 of patch spec) | Value not in controlled vocabulary — add to Type (a) patch: correct |
| `evidential_status` | May be NULL at Session B entry — will be set during Stage 2 | Note if already populated | If populated: record value — will be verified in Stage 2a |
| `god_as_subject` | Per GR-DATA-005: this field carries a high error rate from bulk operations. Do not treat the current value as confirmed. | Check: (1) is the field populated (0 or 1)? (2) is the value plausible given the term type? A term that is a preposition or particle should have `god_as_subject = 0`. A term with `status = 'delete'` is irrelevant. | If field is NULL — note as gap; set to 0 as default in Type (a) patch pending Stage 2a verification. If value appears implausible (e.g. = 1 on a function word) — note for correction. **Full verification against verse evidence happens in Stage 2a. Do not attempt verse-reading verification here.** |
| `somatic_link` | Per GR-DATA-005 and GR-DATA-003: the authoritative field for somatic classification is `mti_term_flags` (flag_id = 3 = SOMATIC_INNER_LINK or flag_id = 4 = BODY_INNER_EXPRESSION), not `wa_term_inventory.somatic_link`. | Check: (1) is `somatic_link` populated (0 or 1)? (2) does `mti_term_flags` contain flag_id 3 or 4 for this term? If `somatic_link = 1` but no somatic flag in `mti_term_flags` — note inconsistency. | Note any discrepancy between `somatic_link` and `mti_term_flags` somatic flags. **Full verification against verse evidence happens in Stage 2a. Do not attempt verse-reading verification here.** |
| `causative_form_present` | 0 or 1 | Populated | NULL — default to 0; note |
| `delete_flagged` | 0 for active terms | Must be 0 | If 1 — this term should not appear in the active term set; note as data anomaly |
| `term_owner_type` | 'OWNER' for primary terms; 'XREF' for cross-registry terms | Populated for active terms | NULL — note; determine from context whether OWNER or XREF |
| `meaning` | Present for active terms with word analysis data | Not NULL | NULL — note; check `wa_meaning_parsed` for this term |
| `parsed_meaning_id` | FK to `wa_meaning_parsed` where meaning data exists | If populated: verify a row exists in `wa_meaning_parsed` | Dangling FK — note as data integrity gap |

**Cross-field check B1:** For each active OWNER term: `occurrence_count` must be > 0 AND verse record count in `wa_verse_records` must be > 0. A term with `occurrence_count > 0` but zero verse records is a data gap — the verses were not extracted or were lost. Flag for investigation.

**Cross-field check B2:** For each active OWNER term: `term_owner_type = 'OWNER'` must have at least one `verse_context_group` row (checked in Section D). Note any OWNER term that has no verse context groups.

**Cross-field check B3:** `somatic_link` on `wa_term_inventory` vs somatic flags in `mti_term_flags` (flag_id IN (3,4)). List any discrepancies. These are noted for Stage 2a verification — they are not corrected in Stage 1 without verse evidence.

**For XREF terms (`term_owner_type = 'XREF'`):**
Note the target registry from `mti_terms.owning_registry`. Confirm the XREF term's owning registry is registered in the programme. No analytical work is done on XREF terms in this registry — they are read in Stage 2a for cross-registry context only.

**For deleted terms (`mti_terms.status = 'delete'`):**
Note their presence. Confirm `delete_flagged = 1` on the corresponding `wa_term_inventory` row. No further checks required — deleted terms are outside analytical scope.

---

### Section C — Verse Records (`wa_verse_records`)

One row per verse per term. These are the raw verse records before classification.

**Request from CC if not in extract:** Return count of `wa_verse_records` rows per term for this registry where `delete_flagged = 0`, grouped by `mti_term_id`.

| Check | Valid state | Anomaly action |
|-------|------------|----------------|
| Every active OWNER term has at least one verse record | Count > 0 per term | Zero verses for an active OWNER term — flag as data gap; may trigger Verse Context sub-process |
| `verse_text` is populated | Not NULL or empty | NULL verse_text — note; the verse cannot be read without text |
| `reference` is populated and correctly formatted | Format: [Book] [Chapter]:[Verse] (e.g. 'Rom 3:23', 'Gen 1:1') | Malformed reference — note |
| `span_strong_match` is populated | 0 or 1 | NULL — note; span matching may have failed |
| `translation` value | 'ESV' is the programme standard | If not 'ESV' — note; may indicate a data import anomaly |
| `delete_flagged = 0` for active verses | 0 | If 1 — the verse is soft-deleted; it should not appear in the active set; note if present |

**Cross-field check C1:** For each active OWNER term: the verse count in `wa_verse_records` should be ≤ `occurrence_count` in `wa_term_inventory`. A verse count significantly exceeding `occurrence_count` (> 110%) indicates possible over-extraction — note. A verse count that is < 20% of `occurrence_count` should already have a `SMALL_VERSE_SAMPLE` flag in `wa_data_quality_flags` — confirm this flag is present.

**Cross-field check C2:** Terms with `occurrence_count_qualifier = 'HFA'` (High Frequency Anchor) or `occurrence_count > 500` should have a `HIGH_FREQUENCY_ANCHOR` data quality flag. Confirm flag is present.

---

### Section D — Verse Context Groups (`verse_context_group` + `verse_context`)

One group per sense cluster per term. The groups describe what each verse is about in inner-being terms. Groups are the foundational analytical structure — all dimension assignments depend on them.

**For each verse context group in the extract:**

| Field | Valid state | Check | Anomaly action |
|-------|------------|-------|----------------|
| `group_code` | Format: [strongs_id]-[seq] (e.g. '1234-001') | Present, unique, correctly formatted | Duplicate group codes — note; formatting error — note |
| `context_description` | Present, substantive (not a placeholder or empty) | Not NULL, length > 20 characters | NULL or very short — note as a data gap; blank descriptions block analytical grouping |
| `delete_flagged` | 0 for active groups | Must be 0 | If 1 — group is soft-deleted; should not appear in active set |
| `mti_term_id` | FK to an active term in `mti_terms` | Verify term is in the active term set | FK to a deleted term — note as data integrity issue |

**For verse_context rows within each group:**

| Check | Valid state | Anomaly action |
|-------|------------|----------------|
| Each group has at least one `is_anchor = 1` verse | Count of anchor verses > 0 per group | Zero anchor verses in a group — note; this group cannot serve as an analytical reference |
| `is_anchor`, `is_relevant`, `is_related` are mutually consistent | A verse can be anchor (anchor=1, relevant=1); relevant (anchor=0, relevant=1); related (relevant=0, related=1); or set aside (all 0). A verse cannot have both `is_anchor = 1` and `is_related = 1` | Flag any verse with contradictory classifications |
| `delete_flagged = 0` for active verses | 0 | Soft-deleted verses should not appear in the active count |
| Verse count per group matches the group's total in `wa_dimension_index` | `verse_context` count per group should match `wa_dimension_index.total_verse_count` for that group | Discrepancy > 5% — note; counts may be stale |

**Cross-field check D1:** Every active OWNER term must have at least one group. A term with `mti_terms.status IN ('extracted', 'extracted_thin')` and zero groups is a data gap that triggers the Verse Context sub-process.

**Cross-field check D2:** The sum of `anchor_count` + `related_count` + `set_aside_count` on `wa_dimension_index` should approximately equal `total_verse_count` for each group. A significant discrepancy indicates the dimension index counts are stale.

---

### Section E — Dimension Assignments (`wa_dimension_index`)

One row per group per term. The dimension assignment is the key output of Dimension Review and the foundation for all Session B analytical passes.

**For each dimension index row in the extract:**

| Field | Valid state | Check | Anomaly action |
|-------|------------|-------|----------------|
| `dimension` | A valid dimension string. Valid values: 'Volitional/Will', 'Cognitive/Intellectual', 'Affective/Emotional', 'Theological/Divine-Human', 'Somatic/Embodied', 'Moral/Conscience', 'Vitality/Existence', 'Relational/Social', 'Social/Cultural'. | Not NULL; value must be in the valid list | NULL — triggers Dimension Review sub-process. Value not in the list — note; may be a legacy label; check against the Dimension Review instruction's controlled vocabulary |
| `dimension_confidence` | Must be `CLAUDE_AI` or `RESEARCHER` | Not `AUTOMATED` | `AUTOMATED` — triggers Dimension Review sub-process for this group |
| `dominant_subject` | Must be populated. Valid values: 'God', 'Human', 'Mixed', 'Community', 'Other' | Not NULL | NULL — note; required for analytical passes |
| `manual_override` | 0 or 1 | Present | NULL — default to 0; note |
| `delete_flagged` | 0 for active groups | Must be 0 | If 1 — row is soft-deleted; should not be in active set |
| `owning_registry_no` | Must match this registry's `no` field | Cross-check against `word_registry.no` for registry [nnn] | Mismatch — note as data integrity issue; may indicate a cross-registry contamination |

**Cross-field check E1:** Every active group in `verse_context_group` must have exactly one corresponding row in `wa_dimension_index` for this registry. Groups with zero dimension rows — triggers Dimension Review sub-process. Groups with two or more dimension rows — note as duplication anomaly.

**Cross-field check E2:** Where `dimension = 'Somatic/Embodied'`: confirm the corresponding term has `somatic_link = 1` in `wa_term_inventory` or a somatic flag (flag_id IN (3,4)) in `mti_term_flags`. Inconsistency — note for Stage 2a verification.

**Cross-field check E3:** Where `dimension = 'Theological/Divine-Human'`: confirm the corresponding term has `god_as_subject = 1` in `wa_term_inventory` or a GOD_AS_SUBJECT flag (flag_id = 1) in `wa_term_phase2_flags`. Inconsistency — note for Stage 2a verification. Do not correct these values in Stage 1 — they require verse reading to verify.

---

### Section F — Existing Findings and Flags

These are the existing analytical records for this registry. They are noted here for situational awareness only. Detailed review happens in Step 1.3.

**F1 — `wa_session_b_findings`:**
Request from CC: return count of rows for registry [nnn] where `delete_flag = 0`.
Record: `Prior-phase findings for registry [nnn]: [n] active findings. [n] have status = 'pending'. [n] have catalogue links.`

**F2 — `wa_session_research_flags`:**
Request from CC: return count of rows for registry [nnn] by `session_target` and `resolved`.
Record: `Research flags for registry [nnn]: [n] total. Session D target: [n], [n] resolved. Session B target: [n], [n] resolved.`
If any `session_target = 'B'` flags exist with `resolved = 0`: record count — these will be addressed in Step 1.3c.

**F3 — `wa_term_phase2_flags`:**
Request from CC: return count of rows for active terms in registry [nnn] where `delete_flagged = 0`.
Record: `Phase2 flags for registry [nnn]: [n] flags across [n] terms.`

Do not review these flags in this section. Their detailed review is Step 1.3a, 1.3b, and 1.3c respectively.

---

### Section G — Supporting Term Data

These tables carry supporting analytical data for terms. Check for presence and consistency — do not perform analytical review.

**G1 — `wa_meaning_parsed` / `wa_meaning_sense` / `wa_meaning_stem`:**

For each active OWNER term:
- Does `wa_meaning_parsed` contain a row? If `parsed_meaning_id` is set on `wa_term_inventory`, confirm the FK resolves.
- Does `wa_meaning_sense` contain at least one row for this term's `parsed_meaning_id`? A meaning parse with zero senses is an incomplete parse.
- If `wa_meaning_parsed.has_causative_stem = 1`: confirm at least one `wa_meaning_stem` row exists for this term with `stem_type = 'causative'` or similar.
- Note terms with no meaning data — flag code `NO_WORD_ANALYSIS` should be present in `wa_data_quality_flags` for these terms.

**G2 — `wa_term_root_family`:**

For each active OWNER term:
- Are root family records present?
- `root_code` must be populated. `root_language` should match the term's language.
- Terms with no root family record are not anomalous — not all terms have extracted root data. Note the count.

**G3 — `wa_term_related_words`:**

For each active OWNER term:
- Count of related word records. Note if very low (0–1) for a primary term — may indicate limited STEP data.
- No anomaly action required unless count is 0 for a term that is expected to have cognates.

**G4 — `wa_lsj_parsed` (Greek terms only):**

For Greek terms (`language = 'Greek'`) with `parsed_meaning_id` set:
- Is a `wa_lsj_parsed` row present? LSJ data is available for Greek terms only.
- Not all Greek terms will have LSJ data — absence is not an anomaly. Note presence or absence.

**G5 — `wa_cross_registry_links`:**

Request from CC: return count of `wa_cross_registry_links` rows for this registry's file_id.
Record: `Cross-registry links for registry [nnn]: [n] rows.`
These are noted for Stage 2a — no action required in Stage 1.

---

### Section H — Step 1.2 Close

After completing all seven sections, produce a consolidated audit summary in the observations log:

```
Step 1.2 Audit Summary — Registry [nnn] [word]

Registry state: session_b_status=[value], verse_context_status=[value], dim_review_status=[value]
Active terms: [n] OWNER, [n] XREF, [n] deleted
Total verse records: [n] across [n] active OWNER terms
Verse context groups: [n] active groups across [n] terms
Dimension assignments: [n] groups at CLAUDE_AI/RESEARCHER confidence, [n] at AUTOMATED
Existing findings: [n] active, [n] pending link
Research flags: [n] Session D target ([n] unresolved), [n] Session B target ([n] unresolved)
Phase2 flags: [n] flags across [n] terms

Gaps identified: [n total]
  Hard gate failures (must resolve before proceeding): [list]
  Sub-process triggers: [Verse Context / Dimension Review / None]
  Type (a) patch items identified: [n] — detailed in Step 1.3 and 1.4
  Anomalies noted for Stage 2a verification: [list]
```

**Hard gate check before proceeding to Step 1.3:**

The following conditions must all be true. If any is false, stop and resolve before continuing:

| Condition | Required state | Action if not met |
|-----------|---------------|-------------------|
| `verse_context_status` | `Complete` | STOP — Verse Context sub-process must complete first |
| `session_b_status` | `Pre-Analysis Complete` or `Verse Context Reset` | STOP — confirm with researcher |
| All active OWNER terms have ≥ 1 verse record | Yes | STOP — data gap; may require re-extraction |
| `carry_forward` | 1 | STOP — confirm with researcher before proceeding |

If all conditions are met: record `Step 1.2 complete. All hard gate conditions met. Proceeding to Step 1.3.`

---

*End of Step 1.2 corrected draft*
*For incorporation into wa-global-sessionb-stage1-draft-v1-20260416.md replacing the existing Step 1.2 section*
