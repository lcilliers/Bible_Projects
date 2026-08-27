# WA Session Log — Session B Instruction Redesign: Session Close
**Filename:** wa-global-sessionlog-sessionb-redesign-v2-20260416.md
**Date:** 2026-04-16
**Version:** v2.0
**Previous output refs:**
- wa-global-sessionlog-sessionb-redesign-v1-20260416.md (prior session log — Phase 2 architecture decisions)
- wa-global-sessionb-update-tasklist-v1_9-20260416.md (current task list)
- wa-global-sessionb-stage1-draft-v1-20260416.md (T-02 output — Stage 1 draft, under review)

---

## 1. Session Summary

This session completed the following work since the prior session log:

- T-POP confirmed COMPLETE: `wa_obs_question_catalogue` populated with 194 rows, `source_registry_no` correct for all five source words. No pre-population of `wa_finding_catalogue_links` or `wa_session_research_flags` corrections — researcher decision to let the Session B process per word determine relevance.
- T-02 COMPLETE (draft): Full Stage 1 replacement text produced (`wa-global-sessionb-stage1-draft-v1-20260416.md`). Awaiting researcher review.
- Session parked at Step 1.2 review — three structural problems identified by researcher.

---

## 2. Step 1.2 Correction Items — Formal Record

The researcher identified three problems with Step 1.2 as drafted in v5.0 (which was retained unchanged in the T-02 draft). These must be corrected before Step 1.2 can be considered sound. They are recorded here as the primary work item for the next session.

### Problem 1 — Incoherent reference to Phase 2

**Location:** Step 1.2 audit checklist — terms section. Fields `god_as_subject` and `somatic_link` are flagged with: "Per GR-DATA-005: do not trust — verify against verses in Stage 2."

**Problem:** Deferring verification of a field to Stage 2 is incoherent in a step whose purpose is to confirm the data is correct before Stage 2 begins. If the field value cannot be trusted, that is a data quality gap — Stage 1 must deal with it, not defer it. The instruction cannot tell Stage 1 to check a field and simultaneously say the check only happens in Stage 2.

**Correction required:** For fields that cannot be verified by reading the extract alone (e.g. `god_as_subject`, `somatic_link` — which require verse reading to verify), the Step 1.2 instruction must either:
- Specify a reasonability check that can be done in Stage 1 (e.g. flag the field value as provisional, note it for verification in Stage 2a), or
- Specify what "correct" means in Stage 1 terms — not "trust the value" but "confirm the field is populated and that the value is plausible given the term's type."

The note "do not trust — verify in Stage 2" must be replaced with a concrete action that Stage 1 can complete.

### Problem 2 — No terms of reference for "correct"

**Location:** Step 1.2 audit checklists throughout — registry fields, terms, verse context groups, dimension assignments.

**Problem:** The instruction says to check each field but does not state what "correct" means for each field. Without terms of reference, the check cannot be performed reliably. An AI cannot determine whether a field value is correct without knowing what it should be checked against, what the valid value range is, and what constitutes an anomaly.

**Correction required:** Every field check in Step 1.2 must include:
- What the field should contain (the valid value, range, or format)
- What to compare it against (the extract's own internal data, a controlled vocabulary, a schema rule, or a cross-field consistency check)
- What constitutes a gap or anomaly requiring action

This is not a matter of adding explanatory notes — it is a matter of specifying the check precisely enough that there is no room for interpretation.

### Problem 3 — Incomplete field coverage

**Location:** Step 1.2 audit checklists — the full set of fields checked does not cover all data present in the extract.

**Problem:** The current checklist covers selected fields from `word_registry`, `wa_term_inventory`, verse context groups, and dimension assignments. It does not systematically cover all tables present in the extract, and it does not include cross-field consistency checks or cross-table correlation checks.

**Correction required:** Step 1.2 must be rebuilt against the database schema. The governing rule is: ALL data for the word must be validated. This means:
- Every table present in the extract has a field-level check
- Every field that can be validated has a reasonability check
- Cross-field consistency checks are specified (e.g. a term with `status = 'extracted'` should have verse count > 0; a group with `is_anchor = 1` on any verse should have `anchor_count > 0` on its dimension index row)
- Cross-table correlation checks are specified (e.g. a term with `somatic_link = 1` should have at least one verse context group assigned to the Somatic/Embodied dimension)

**Action required for next session:** Read Step 1.2 against the full schema (v3.9.0) and identify every table and field that should be present in the extract. For each, specify the check, the terms of reference, and the action if the check fails. This is a significant rewrite of Step 1.2 — not an incremental correction.

---

## 3. Implication for T-02 Status

T-02 produced a draft of Stage 1. Steps 1.3a, 1.3b, 1.3c, 1.4, and 1.5 are considered sound pending researcher review. Step 1.2 requires a substantive rewrite before T-02 can be marked fully confirmed.

The T-02 draft is therefore split into two parts for review purposes:
- **Part A** (Steps 1.3a, 1.3b, 1.3c, 1.4, 1.5): ready for researcher review
- **Part B** (Step 1.2): requires correction — the three problems above must be resolved first

T-2A (Stage 2a drafting) should not begin until both parts of T-02 are confirmed.

---

## 4. Outputs Produced This Session (since prior log)

| File | Content | Status |
|---|---|---|
| PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json | T-POP-A — 194 catalogue rows | Applied and confirmed |
| wa-global-dir-20260416-002-popbc-extracts-v1-20260416.md | T-POP-B/C extraction directives | Extracts received; no patches applied |
| wa-global-sessionb-stage1-draft-v1-20260416.md | Stage 1 replacement text (T-02) | Draft — Part B (Step 1.2) requires correction |
| wa-global-sessionb-update-tasklist-v1_0 through v1_9 | Task list — 10 iterations | v1.9 active |
| wa-global-sessionlog-sessionb-redesign-v1-20260416.md | Phase 2 architecture decisions | Active |
| wa-global-sessionlog-sessionb-redesign-v2-20260416.md | This session log | Active |

---

## 5. Open Items Entering Next Session

| Item | Priority | Action needed |
|---|---|---|
| Step 1.2 Problem 1 | HIGH | Correct incoherent Phase 2 deferrals — specify Stage 1 actions for fields that require verse reading to verify |
| Step 1.2 Problem 2 | HIGH | Add terms of reference to every field check — what is correct, what to compare against, what constitutes an anomaly |
| Step 1.2 Problem 3 | HIGH | Rebuild Step 1.2 against schema v3.9.0 — ALL data for the word must be validated; cross-field and cross-table consistency checks required |
| T-02 Part A review | MEDIUM | Researcher reviews Steps 1.3a–1.3c, 1.4, 1.5 and confirms or returns corrections |
| T-08 gap candidates | MEDIUM | Researcher decision on C-1 through C-9 |

---

## 6. Resume Instructions for Next Session

**Load at session start (in order):**
1. `wa-global-general-rules-v2_2-20260415.json`
2. `wa-global-sessionb-update-tasklist-v1_9-20260416.md` (governing task list)
3. `wa-global-sessionlog-sessionb-redesign-v1-20260416.md` (Phase 2 architecture decisions)
4. `wa-global-sessionlog-sessionb-redesign-v2-20260416.md` (this log — Step 1.2 correction items)
5. `wa-global-sessionb-stage1-draft-v1-20260416.md` (T-02 draft — to be corrected)
6. `wa-global-sessionb-instruction-v5_0-20260415.md` (source instruction)
7. `database-schema-20260416.json` (schema v3.9.0 — required for Step 1.2 rebuild)

**First action:** Read Step 1.2 in the T-02 draft against the full schema. For each table in the extract, identify all fields and specify the check, terms of reference, and action. This is the primary work of the next session before any other instruction drafting proceeds.

**Do not begin T-2A until Step 1.2 is corrected and both parts of T-02 are confirmed by the researcher.**

---

*Session parked: 2026-04-16*
*Next session: Step 1.2 correction and rebuild; then T-02 Part A researcher review*
