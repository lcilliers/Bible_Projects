# Flag Table Remediation Plan
## wa-global-flagtable-remediation-plan-v1.0-20260414.md
**Date:** 2026-04-14
**Status:** Draft — for researcher review and approval before work begins
**Raised by:** Session B v5.0 design session — flag table infrastructure finding

---

## Context

During the design of Session B v5.0, a review of the live flag table extract revealed that the flag system has grown organically and is out of governance. This must be resolved before Session B v5.0 drafting continues. The flag tables are the primary mechanism for:
- Recording Session B analytical outcomes (Type b writes)
- Raising researcher decision items
- Storing Session D pointers
- Tracking data quality concerns

Without a governed flag schema, none of the Session B, Session C, or Session D instructions can be written with precision.

---

## Current state summary

### What is clean
- `phase2_flag_types` (25 codes) — well-defined, used by `wa_term_phase2_flags` and `mti_term_flags`
- `wa_crosslink_type` (11 codes) — clean reference table for cross-registry links
- `wa_data_quality_flags` (22,129 rows) — engine-derived, largely automatic; contains three SESSION_B and two SESSION_D reference codes that are not yet actively used

### What needs governance
- `wa_session_research_flags` (327 rows, 16 codes in live use): only 1 of 16 codes has a reference entry. Four distinct purposes mixed without differentiation:
  1. Session D pointers (229 rows — dominant use)
  2. Data quality flags (errors, gaps, concerns)
  3. Study requirement flags (exegetical, theological, eschatological)
  4. Researcher decision items
- Naming drift: VOLUME_LIMITATION and PH2_VOLUME_LIMITATION are the same thing
- SESSION_B outcome codes exist in reference table (SB_FINDING, SB_DIMENSION, SB_INNER_BEING) but are not used and not specified

### Open schema questions
- Does `wa_session_research_flags` have a `resolved_notes` field? (Need CC to confirm)
- What fields does `wa_session_research_flags` have in full? (Need schema extract)
- Is a RESEARCHER_DECISION flag code sufficient, or does the table need additional fields?
- Should the four purposes currently in `wa_session_research_flags` be separated, or governed within the same table using flag codes?

---

## Proposed remediation steps

### Step 1 — Full schema extract (CC task)
Before any design decisions, obtain the full schema for all flag-related tables:
- `wa_session_research_flags` — all columns, types, constraints
- `wa_data_quality_flags` — all columns, types, constraints
- `wa_term_phase2_flags` — all columns, types, constraints
- `mti_term_flags` — all columns, types, constraints
- `wa_quality_flag_types` — all columns (already have reference data)
- `phase2_flag_types` — all columns (already have reference data)

**Output:** Schema extract JSON for researcher and Claude AI review.
**Decision gate:** No design decisions until schema is confirmed.

### Step 2 — Clarify the four purposes
Examine each of the 16 live flag codes in `wa_session_research_flags` and classify each by purpose:
1. Session D pointer — cross-registry observation for synthesis
2. Data quality — error, gap, or concern requiring correction
3. Study requirement — passage needing dedicated study
4. Researcher decision — item requiring researcher input to resolve

**Question for researcher:** Should these four purposes live in the same table (governed by flag code category) or in separate tables? Arguments:
- Same table: simpler, fewer joins, existing data does not move
- Separate tables: cleaner boundaries, easier to query by purpose, prevents future drift

**Output:** Design decision confirmed by researcher.
**Decision gate:** Researcher confirms table architecture before proceeding.

### Step 3 — Govern the reference table
Once architecture is decided:
- Add all 15 missing ad-hoc codes to `wa_quality_flag_types` with proper descriptions
- Introduce category field to `wa_quality_flag_types` if same-table architecture chosen (SESSION_D / DATA_QUALITY / STUDY_REQUIRED / RESEARCHER_DECISION)
- Resolve naming drift: pick one canonical code for VOLUME_LIMITATION and deprecate the other (flag existing records, do not delete)
- Introduce RESEARCHER_DECISION code

**Output:** CC directive to update reference table. Researcher approves before CC executes.

### Step 4 — Define RESEARCHER_DECISION flag fields
Specify what a researcher decision flag must carry:
- The question or decision required
- Sufficient context for the researcher to decide without re-reading the raw data
- The researcher's response
- CC query result (where applicable)

Confirm whether existing fields support this or whether schema extension is needed.

**Output:** Field specification. Schema gap raised if extension needed. Researcher approves.

### Step 5 — Specify Session B outcome codes
Define exactly what SB_FINDING, SB_DIMENSION, SB_INNER_BEING store:
- Which table do they live in? (`wa_data_quality_flags` or `wa_session_research_flags`?)
- What fields carry the analytical content?
- One record per finding? Per pass? Per term?
- How does Session C and Session D query these records?

This is the Type (b) analytical outcome design. It directly governs every pass in Session B v5.0.

**Output:** Outcome code specifications. Schema gaps raised for any missing fields. Researcher approves before Session B drafting resumes.

### Step 6 — Specify complete word data export to include flag records
The current complete word data export does not include flag records as input to Session B. Define:
- Which flag tables and which records to include in the export
- How records are scoped to the registry (by registry_no, by strongs_reference, etc.)
- Version numbering convention for the export file (CC to implement)

**Output:** CC directive for updated export format.

### Step 7 — Clean up existing data
Once schema and governance are confirmed:
- Update existing records to use canonical flag codes (fix naming drift)
- Add missing reference rows for all existing ad-hoc codes
- Flag (do not delete) deprecated duplicates

**Output:** CC patch for data cleanup. Researcher approves before CC executes.

### Step 8 — Update all instruction documents
Once schema is confirmed and data is clean:
- Update Session B v5.0 with precise flag table references per pass
- Update Verse Context instruction flag references
- Update Dimension Review instruction flag references
- Update global rules if new database patterns emerge
- Update CC instructions

**Output:** Updated instruction documents. Researcher reviews before active.

---

## Sequencing and dependencies

```
Step 1 (schema extract — CC)
    │
    ▼
Step 2 (architecture decision — researcher)
    │
    ▼
Step 3 (govern reference table — CC + researcher approval)
    │
    ├── Step 4 (RESEARCHER_DECISION fields — Claude AI + researcher)
    │
    └── Step 5 (SESSION_B outcome codes — Claude AI + researcher)
          │
          ▼
    Step 6 (export format — CC + researcher)
          │
          ▼
    Step 7 (data cleanup — CC + researcher approval)
          │
          ▼
    Step 8 (instruction updates — Claude AI)
          │
          ▼
    Resume Session B v5.0 Stage 1 drafting
```

---

## Questions requiring researcher decision before work begins

**Q1:** Confirm that this plan is approved and the sequence is correct before Step 1 begins.

**Q2:** Step 2 architecture question — same table or separate tables for the four purposes? If you have an initial preference, state it and Step 2 can confirm rather than design from scratch.

**Q3:** Are there any other flag-related tables or codes not in the extract that should be included in Step 1?

---

## Notes

- No existing data is deleted at any step — per GR-OBS-005, records are flagged not deleted
- All CC directives produced in Steps 3, 6, and 7 require researcher approval before execution
- Steps 1–7 must be complete before Session B v5.0 Stage 1 drafting resumes
- This plan itself may need revision after Step 1 reveals the full schema

