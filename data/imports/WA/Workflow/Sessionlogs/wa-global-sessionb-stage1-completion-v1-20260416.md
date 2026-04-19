# WA — Session B Instruction: Stage 1 Completion Gate
**Filename:** wa-global-sessionb-stage1-completion-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Adds:** Step 1.6 — Stage 1 Completion Verification and Handoff. Updates Step 1.5 to include span filter failure and audit_word re-run triggers from Step 1.2 Path 2 items. Updates Stage 1 integrity rules.
**Previous output refs:**
- wa-global-sessionb-stage1-draft-v1-20260416.md (T-02A — Steps 1.3a–1.5)
- wa-global-sessionb-step1-2-v2-20260416.md (T-02C — Step 1.2 with resolution framework)
- wa-global-sessionb-update-tasklist-v1_13-20260416.md (governing task list)

---

## What This Document Covers

Stage 1 completion requires more than confirming that all steps were executed. It requires verifying that the corrections made during Stage 1 are actually present in the data before Stage 2 begins. The current Step 1.5 pulls a fresh extract but only confirms its version number — it does not verify content. This document adds:

1. **Step 1.5 updated** — extended to include the full set of sub-process triggers from the Step 1.2 resolution framework (including span filter failure and audit_word re-run triggers from Path 2)
2. **Step 1.6 (new)** — Stage 1 Completion Verification: a targeted verification pass against the fresh extract, a completion checklist, a formal handoff statement, and the Stage 2 readiness declaration

---

## Step 1.5 — Sub-Process Execution and Fresh Extract (updated)

### Purpose

Step 1.5 executes all process re-run directives (Path 2 items) identified during Step 1.2, waits for each to complete, and then pulls the fresh extract. The fresh extract is the data that Stage 2 will work from — it must reflect all corrections made during Stage 1.

Step 1.5 does not begin until:
- The Type (a) patch from Step 1.4 is confirmed applied
- The B-target flag hard gate is confirmed (zero open B-target flags)
- All RESEARCHER_DECISION items are resolved

### Sub-process triggers

The following triggers are checked in the order listed. Each trigger that fires must be resolved before the next trigger is checked. Where multiple triggers fire independently (e.g. span filter failure on term A AND missing groups on term B), they may be batched into a single CC directive if the processes are compatible — but each must complete and be confirmed before the fresh extract is pulled.

**Trigger 1 — Span filter failure (from Step 1.2 Path 2):**
Applies when: any active OWNER term has `span_match_count > 0` and `total_verse_records = 0` in the verse_records_summary (all extracted records were span-filtered out).

Action:
1. Produce a CC directive specifying: the affected term(s) by strongs_number; re-extraction of verse data for those terms; audit_word re-run (targeted to those terms); followed by Verse Context classification for those terms.
2. Sequence: re-extraction → audit_word targeted re-run → Verse Context sub-process for affected terms.
3. Submit directive for researcher approval. Do not execute without approval.
4. After CC confirms completion: verify the affected terms now have `total_verse_records > 0` in the updated data.
5. Record in observations log: `Trigger 1 (span filter failure): [n] terms. Directive [DIR-ref] executed. Confirmed: [strongs list] now have active verse records.`

**Trigger 2 — Zero-verse extraction gap (from Step 1.2 Path 2):**
Applies when: any active OWNER term has `span_match_count = 0` and `total_verse_records = 0` (no verses were extracted at all).

Action:
1. Distinguish from span filter failure: this term returned no verse spans from STEP, not verses that were filtered post-extraction.
2. Before producing a re-extraction directive: confirm with the term's `occurrence_count` — if occurrence_count = 0, the term genuinely has no Biblical occurrences and zero verses is correct. If occurrence_count > 0: genuine extraction gap.
3. If genuine extraction gap: produce CC directive for re-extraction → audit_word targeted re-run → Verse Context sub-process.
4. If occurrence_count = 0: Path 4 — RESEARCHER_DECISION on whether the term should be retained or deleted.
5. Record outcome per term.

**Trigger 3 — OWNER terms with no verse_context_groups (from Step 1.2 Path 2):**
Applies when: any active OWNER term has verse records but zero groups in `verse_context_groups`.

Action:
1. Load Verse Context instruction (`wa-versecontext-instruction-v[current].md`).
2. Run targeted Verse Context sub-process for the affected term(s).
3. Do not proceed until sub-process is complete and its own patch is confirmed.
4. Record: `Trigger 3 (missing groups): [strongs] — Verse Context sub-process complete. [n] groups created.`

**Trigger 4 — Groups with NULL dimension or AUTOMATED confidence (from Step 1.2 Path 2):**
Applies when: any group has `dimension = NULL` or `dimension_confidence = 'AUTOMATED'`.

Action:
1. Load Dimension Review instruction (`wa-dimensionreview-instruction-v[current].md`).
2. Run targeted Dimension Review sub-process for the affected group(s).
3. Do not proceed until sub-process is complete and its own patch is confirmed.
4. Record: `Trigger 4 (dimension gap): [n] groups — Dimension Review sub-process complete.`

**Trigger 5 — Groups with no anchor verse (from Step 1.2 Path 2):**
Applies when: any active group has zero `is_anchor = 1` verse_context records.

Action:
1. Load Verse Context instruction.
2. Run targeted Verse Context sub-process for the affected group(s) — anchor designation pass only.
3. Do not proceed until sub-process is complete and its own patch is confirmed.
4. Record: `Trigger 5 (no anchor verses): [n] groups — Verse Context anchor pass complete.`

**If no sub-process triggers fired:**
Record: `Step 1.5: no sub-process triggers. All Path 2 items from Step 1.2 were field-level corrections only (resolved in Step 1.4 patch). Proceeding to fresh extract.`

### Fresh extract

After all sub-process triggers are resolved and confirmed:

Request from CC: re-export the complete word data for registry [nnn] and return the new version identifier and export date.

This extract replaces the one used during Stage 1. All subsequent work in Step 1.6 and Stage 2 uses this extract.

Record in observations log: `Fresh extract confirmed: [filename] — version [n] — exported [date].`

Do not proceed to Step 1.6 until the fresh extract is confirmed.

---

## Step 1.6 — Stage 1 Completion Verification and Handoff

### Purpose

Step 1.6 verifies that the fresh extract reflects all corrections made during Stage 1. It is not a re-run of the full Step 1.2 audit — it is a targeted verification of the specific items that were patched, directed, or sub-processed. It produces the Stage 1 Completion Record and declares Stage 2 readiness.

This step has three parts:
1. Targeted verification of corrections against the fresh extract
2. Stage 1 Completion Checklist
3. Stage 1 Completion Record and Stage 2 readiness declaration

### Part 1 — Targeted verification against fresh extract

For each item that was corrected during Stage 1, confirm that the correction is present in the fresh extract. Work from the observations log — the corrections were recorded there as they were applied.

**Verification by correction type:**

**Type (a) patch verifications:**
For each patch operation recorded in Step 1.4:
- Field correction (e.g. `language` mismatch, `delete_flagged`, `somatic_link`): confirm the field now holds the corrected value in the fresh extract.
- Catalogue link insertion: confirm the `wa_finding_catalogue_links` row is present with `status = 'suggested'`.
- Finding status update: confirm `wa_session_b_findings.status` is updated as patched.
- B-target flag resolution: confirm `wa_session_research_flags.resolved = 1` for each closed flag.
- Quality flag additions: confirm the flag is present in `wa_data_quality_flags` for the relevant term.

For each verification: record `[table].[field] on [reference]: expected [value] — confirmed [value]. PASS / FAIL.`

If any verification FAILS: do not proceed. Raise a corrective directive to CC. Re-pull extract section after correction. Re-verify before continuing.

**Path 2 sub-process verifications:**
For each sub-process trigger that fired:
- Span filter failure terms: confirm `total_verse_records > 0` for each affected term.
- Zero-verse extraction terms: confirm verse records now present and `verse_context_groups` exist for each term.
- Missing groups: confirm at least one `verse_context_group` exists for each affected OWNER term.
- Dimension gaps: confirm all groups now have a non-NULL `dimension` with `dimension_confidence = 'CLAUDE_AI'` or `'RESEARCHER'`.
- No-anchor groups: confirm at least one `is_anchor = 1` verse exists for each affected group.

For each verification: record `[trigger type] on [reference]: [outcome]. PASS / FAIL.`

**Path 3 notes verification:**
Path 3 items are not verified here — they are deferred to Stage 2a by design. Confirm the count of Path 3 notes in the observations log matches the count carried forward. Record: `Path 3 notes carried to Stage 2a: [n].`

**Record in observations log:** `Part 1 verification complete. [n] patch verifications: [n] PASS, [n] FAIL. [n] sub-process verifications: [n] PASS, [n] FAIL. [n] Path 3 notes carried forward.`

If any failures: resolve before proceeding to Part 2.

---

### Part 2 — Stage 1 Completion Checklist

Run this checklist against the fresh extract. Every item must pass. Record the result of each check.

**Domain 1 — Registry state**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| `session_b_status` | `Pre-Analysis Complete` or `Verse Context Reset` | STOP — resolve with researcher before Stage 2 |
| `verse_context_status` | `Complete` | STOP — Verse Context must complete |
| `dim_review_status` | `Complete` | STOP — Dimension Review must complete |
| `carry_forward` | 1 | STOP — confirm with researcher |
| `cluster_assignment` | Valid cluster code (C01–C22) | STOP — cluster must be assigned |

**Domain 2 — Term data**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All active OWNER terms have `mti_terms.status IN ('extracted','extracted_thin')` | Zero NULL-status OWNER terms | Raise corrective Path 1 patch |
| All active XREF terms have `mti_terms.status = 'xref_[word]'` | Zero NULL-status XREF terms | Raise corrective Path 1 patch |
| All deleted terms have `delete_flagged = 1` in `wa_term_inventory` | No deleted terms with `delete_flagged = 0` | Raise Path 1 patch |
| All active OWNER terms have `total_verse_records > 0` | Zero span filter failures or extraction gaps | If any remain: Path 2 directive; do not proceed |
| `somatic_link` consistent with `mti_term_flags` for all OWNER terms | Zero discrepancies | Raise corrective Path 1 patch for any remaining |

**Domain 3 — Verse context groups**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All active OWNER terms have at least one `verse_context_group` | Zero OWNER terms without groups | Path 2: Verse Context sub-process if any remain |
| All active groups have at least one `is_anchor = 1` verse | Zero anchor-less groups | Path 2: targeted VC anchor pass |
| All active groups have `delete_flagged = 0` | No soft-deleted groups in active set | Note — investigation required |
| `dominant_subject` set on all active groups | Zero NULL or 'NONE' values | Path 1 patch for any remaining correctable from description; Path 4 for those requiring verse reading |

**Domain 4 — Dimension assignments**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All active groups have `dimension` set (not NULL) | Zero groups with NULL dimension | Path 2: Dimension Review sub-process |
| All active groups have `dimension_confidence` = 'CLAUDE_AI' or 'RESEARCHER' | Zero AUTOMATED groups | Path 2: Dimension Review sub-process |

**Domain 5 — Flags and findings**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| Zero `wa_session_research_flags` rows for this registry with `session_target = 'B'` AND `resolved = 0` | Count = 0 | STOP — hard gate; resolve remaining B-target flags before proceeding |
| All active `wa_session_b_findings` have `status` set (not left at unprocessed state with no disposition) | Zero findings with no recorded disposition | Return to Step 1.3b; disposition each |
| All `wa_term_phase2_flags` with `delete_flagged = 0` have a recorded disposition in the observations log | All flags accounted for | Return to Step 1.3a; complete dispositions |

**Domain 6 — Catalogue readiness**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| `wa_obs_question_catalogue` has 194+ rows | Count ≥ 194 | Path 4 — RESEARCHER_DECISION: catalogue may be stale |
| Every active `wa_session_b_findings` row either (a) has a `wa_finding_catalogue_links` row with `status IN ('suggested','validated')` OR (b) has an observations log entry noting it needs a new question in Stage 2b | Zero unaccounted findings | Return to Step 1.3b |

**Domain 7 — Process history**

| Check | Pass condition | Fail action |
|-------|---------------|------------|
| All `audit_word` REVIEW flags from `word_run_states` with `researcher_approved = 0` have been dispositioned to a resolution path | Zero undispositioned REVIEW flags | Return to Section A.1 of Step 1.2 |
| All Path 2 directives produced during Stage 1 have CC confirmation of completion | Zero outstanding directives | Execute and confirm before proceeding |

**Checklist outcome:**

If all domains pass: proceed to Part 3.

If any domain fails: apply the corrective action specified. Re-run only the failed domain check after the correction is confirmed — do not re-run the full checklist. Repeat until all domains pass.

Record in observations log: `Stage 1 Completion Checklist. Domains checked: 7. Pass: [n]. Fail: [n]. Corrective actions: [list if any]. Final state: ALL PASS.`

---

### Part 3 — Stage 1 Completion Record and Stage 2 Readiness Declaration

When the checklist is clean, produce the Stage 1 Completion Record. This is the formal handoff from Stage 1 to Stage 2.

```
STAGE 1 COMPLETE — Registry [nnn] ([word])
Date: [date]
Fresh extract version: [version] — exported [date]

Step 1.1 COMPLETE — Extract confirmed: [filename] v[n]
Step 1.2 COMPLETE — Audit complete. Path 1: [n] items. Path 2: [n] items. Path 3: [n] notes. Path 4: [n] RD items (all resolved).
Step 1.3a COMPLETE — Phase2 flags: [n] reviewed. Confirmed: [n]. Rejected/irrelevant: [n] patched. Thin: [n] carried to Stage 2a.
Step 1.3b COMPLETE — Findings: [n] reviewed. Linked: [n]. Needing new question (Stage 2b): [n]. Closed invalid: [n].
Step 1.3c COMPLETE — B-target flags: [n] resolved. Hard gate: CONFIRMED (CC count = 0).
RESEARCHER_DECISION block: [n] items raised. [n] resolved. 0 open.
Step 1.4 COMPLETE — Type (a) patch applied and confirmed. [n] operations.
Step 1.5 COMPLETE — Sub-process triggers: [none / list]. Fresh extract confirmed: v[n].
Step 1.6 COMPLETE — Verification pass: [n] checks. All pass. Completion checklist: all 7 domains pass.

Path 3 notes carried to Stage 2a: [n items — brief list]
Catalogue questions indexed for this word: [n] registry-specific questions

DATA STATUS: Sound, complete, and verified.
STAGE 2 READINESS: CONFIRMED.
```

**Stage 2 readiness declaration:**

State the following as the formal readiness declaration before Stage 2 begins:

`Stage 1 is complete. The data for registry [nnn] ([word]) has been validated, corrected, and verified against the fresh extract (version [n]). All hard gates pass. All Path 2 directives are complete. All RESEARCHER_DECISION items are resolved. [n] Path 3 notes are carried to Stage 2a for verse-reading verification. Stage 2 may begin.`

Record the extract version number that Stage 2 will work from. If at any point during Stage 2 a data question arises about the extract version, this record is the authoritative reference.

---

## Updated Integrity Rules

The following rules are added or updated:

| Rule | Status | Text |
|------|--------|------|
| SB-1 | Updated | Stage 2 does not begin until Stage 1 is fully complete: all steps executed; all Path 1/2/4 items resolved; all domains of the Stage 1 Completion Checklist passing; fresh extract confirmed; Stage 2 readiness declaration made. |
| SB-18 | Updated | Zero `wa_session_research_flags` rows for this registry with `session_target = 'B'` and `resolved = 0` — confirmed by CC count query after Step 1.4 patch application and re-confirmed in Step 1.6 Domain 5 checklist. |
| SB-22 (new) | New | Stage 1 does not close without a Stage 1 Completion Record in the observations log. The record must contain the summary for all steps 1.1–1.6, the resolution counts for all four paths, and the Stage 2 readiness declaration. |
| SB-23 (new) | New | Stage 2 works from the fresh extract confirmed in Step 1.5. If any data question arises during Stage 2 about a field value or count, the fresh extract version number recorded in the Stage 1 Completion Record is the authoritative reference. Claude AI requests CC to confirm the current value from the database if the extract value is in doubt — per GR-DB-001. |
| SB-24 (new) | New | A Path 2 process directive (sub-process re-run) is not complete until CC has confirmed execution AND the targeted terms or groups have been verified in the updated extract. The fresh extract is not pulled until all Path 2 confirmations are in hand. |

---

*End of wa-global-sessionb-stage1-completion-v1-20260416.md*
*Adds Step 1.6 and updates Step 1.5 to the Stage 1 instruction*
*For incorporation into wa-global-sessionb-instruction-v5_1-20260416.md*
