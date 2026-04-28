# WA — Session B Instruction: Stage 1 Opening Section
## Tracking Documents, Session Management, and Fallback Protocol
**Filename:** wa-global-sessionb-stage1-opening-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Inserts:** Before Step 1.1 in Stage 1; replaces/extends the existing Stage 1 Purpose and outputs sections
**Previous output refs:**
- wa-global-sessionb-stage1-draft-v1-20260416.md (T-02A)
- wa-global-sessionb-step1-2-v2-20260416.md (T-02C)
- wa-global-sessionb-stage1-completion-v1-20260416.md (T-02D)
- wa-global-sessionb-update-tasklist-v1_14-20260416.md (governing task list)

---

## Stage 1 — Data Audit and Remediation

### Purpose

Stage 1 makes the data complete, correct, and ready for analysis before Stage 2 begins. No step in Stage 2 begins until Stage 1 is fully complete, all corrections are verified in a fresh extract, and the Stage 2 Readiness Declaration has been made. This is a hard gate — per integrity rule SB-1.

**Stage 1 role:** Data validation and preparation only. Stage 1 confirms the data is sound, classifies existing findings and flags, and ensures all pre-conditions for analysis are met. Stage 1 does not perform analysis, draw analytical conclusions, or build narrative. That is Stage 2.

Stage 1 has six sequential steps:

```
Step 1.1 — Confirm extract version
Step 1.2 — Read and audit the complete JSON
Step 1.3 — Prepare existing records
        Step 1.3a — wa_term_phase2_flags: assess all advisory term flags
        Step 1.3b — wa_session_b_findings: prepare existing findings for Stage 2
        Step 1.3c — wa_session_research_flags: clear all B-target flags (hard gate)
Step 1.4 — Type (a) patch construction and application
Step 1.5 — Sub-process execution and fresh extract
Step 1.6 — Stage 1 completion verification and handoff
```

---

### Stage 1 Outputs

Stage 1 produces the following outputs. All are initiated at the start of Stage 1 — before Step 1.1 begins. Do not begin Step 1.1 until all tracking documents are open and the session start protocol is complete.

| Output | Filename pattern | When produced | Purpose |
|--------|-----------------|---------------|---------|
| Observations log | `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md` | Initiated at Stage 1 start; written continuously throughout | Primary working record and recovery instrument. Contains all findings, path assignments, sign-off statements, patch accumulator, RD accumulator, Path 3 notes, and Stage 1 Completion Record. |
| Session log | `wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md` | Produced at each natural breakpoint and session end | Handoff document. Records current position, what was accomplished, open items, and exact resume instructions. Not the analytical record — that is the observations log. |
| Type (a) patch | `PATCH-[YYYYMMDD]-[nnn]-PREANALYSIS-V[n].json` | Constructed at Step 1.4 | Data correction patch. Compiled from the patch accumulator section of the observations log. |
| CC directives | `wa-[nnn]-[word]-dir-[date]-[seq]-[desc]-v[n]-[date].md` | Produced as needed for Path 2 sub-process triggers | Plain-language directives to CC for process re-runs. Each directive produced before researcher approval and CC execution. |

---

### Tracking Document Structure

The observations log has a defined structure. All four named sections are created at Stage 1 start — before any data is read. They are updated at the steps specified below.

**Open the observations log immediately and create these four sections:**

```
## Type (a) Patch Accumulator
[Empty at start — populated during Steps 1.2, 1.3a, 1.3b, 1.3c, and RD resolutions]

## RESEARCHER_DECISION Accumulator
[Empty at start — populated when Path 4 items are identified in any step]

## Path 3 — Stage 2a Verification Notes
[Empty at start — populated when Path 3 items are identified in any step]

## Stage 1 Progress Record
[Updated at each step sign-off — this is the position marker register]
```

**When each section is updated:**

| Section | Updated when | Updated by whom |
|---------|-------------|-----------------|
| Type (a) Patch Accumulator | Any time a Path 1 item is identified in Steps 1.2, 1.3a, 1.3b, 1.3c, or RD resolutions | Claude AI — immediately on identification per GR-OBS-001 |
| RESEARCHER_DECISION Accumulator | Any time a Path 4 item is identified in any step | Claude AI — immediately on identification |
| Path 3 Verification Notes | Any time a Path 3 item is identified in any step | Claude AI — immediately on identification |
| Stage 1 Progress Record | At each step and sub-step sign-off | Claude AI — immediately on step completion |

**Patch Accumulator format — each entry:**
```
PATCH ITEM [seq]: [date and time]
  Source: [Step 1.2 / Step 1.3a / Step 1.3b / Step 1.3c / RD-S1-xxx]
  Table: [table name]
  Operation: [insert / update]
  Identifies: [row identifier — strongs_number, group_code, flag_label, finding_id, etc.]
  Field: [field name]
  Current value: [value]
  Corrected value: [value]
  Reason: [one sentence]
```

**RESEARCHER_DECISION Accumulator format — each entry:**
```
RD ITEM [RD-S1-xxx]: [date and time]
  Source step: [step]
  What was checked: [specific item]
  Why unresolvable: Path 1 ruled out — [reason]. Path 2 ruled out — [reason]. Path 3 ruled out — [reason].
  Question: [precisely stated]
  Options: A — [option and consequence]. B — [option and consequence].
  Recommendation: [option with reasoning]
  Status: OPEN / RESOLVED — [resolution if known]
```

**Path 3 Notes format — each entry:**
```
PATH 3 NOTE [seq]: [date and time]
  Source: [Step and section]
  Table.field: [reference]
  Term/group/item: [identifier]
  Current value: [value]
  What to verify in Stage 2a: [specific question]
```

**Stage 1 Progress Record format — each entry:**
```
[Step identifier] COMPLETE: [date and time]
  [Sign-off statement verbatim]
  Patch accumulator items added this step: [n]
  RD items added this step: [n]
  Path 3 notes added this step: [n]
```

---

### Session Start Protocol

Apply this protocol at the **start of every session** that works within Stage 1 — whether it is the first session or a resumption after an interruption.

**Step S1 — Confirm global rules loaded:**
State: `Global rules wa-global-general-rules-v[current].json loaded.`
Do not proceed without this confirmation.

**Step S2 — Establish current position from observations log:**
Read the observations log in full. Locate the last entry in the `Stage 1 Progress Record` section. This is the last completed step.

| If the last progress record shows | Resume from |
|-----------------------------------|-------------|
| No entries (blank) | Step 1.1 — Stage 1 has not started |
| Step 1.1 COMPLETE | Step 1.2 |
| Step 1.2 COMPLETE | Step 1.3a |
| Step 1.3a COMPLETE | Step 1.3b |
| Step 1.3b COMPLETE | Step 1.3c |
| Step 1.3c COMPLETE | RESEARCHER_DECISION block |
| RD block COMPLETE | Step 1.4 |
| Step 1.4 COMPLETE | Step 1.5 |
| Step 1.5 COMPLETE | Step 1.6 |
| Step 1.6 COMPLETE | Stage 1 is complete — proceed to Stage 2 |

If the progress record shows a step was started but not signed off — that step was interrupted. Resume from the beginning of that step, using the observations log to understand what was already done within it. Do not repeat work that has a confirmed written record; continue from the last recorded action within the step.

**Step S3 — Confirm extract version is still current:**
Per GR-DB-001 — never assume database state.
Request from CC: confirm the current version of the extract for registry [nnn].
Compare against the extract version recorded at Step 1.1 in the observations log.

| Condition | Action |
|-----------|--------|
| Versions match | PASS — proceed |
| CC returns a newer version than recorded | A patch has been applied since this session started. Read the patch history to understand what changed. Request the fresh extract before resuming. |
| No version recorded in observations log | Step 1.1 was not completed — resume from Step 1.1 |

**Step S4 — Confirm patch accumulator state:**
Read the `Type (a) Patch Accumulator` section of the observations log.
Check whether Step 1.4 has been signed off in the progress record.

| Condition | Action |
|-----------|--------|
| Step 1.4 signed off AND patch confirmed | Patch is complete — items in accumulator have been applied |
| Step 1.4 NOT signed off AND accumulator has items | Patch not yet constructed or not yet applied — these items are outstanding; resume at Step 1.4 |
| Step 1.4 NOT signed off AND accumulator is empty | Stage 1 has not reached Step 1.4 yet — resume at the correct earlier step per Step S2 |

**Step S5 — Confirm CC directive state (if any directives were produced):**
If the observations log records any Path 2 directives (sub-process triggers), confirm with CC whether each directive has been executed and what its outcome was.

| Condition | Action |
|-----------|--------|
| Directive confirmed complete by CC | PASS — verify outcome in fresh extract at Step 1.5 |
| Directive not yet submitted to CC | Submit for researcher approval before proceeding |
| Directive submitted but CC confirmation not received | Request confirmation from CC before proceeding |
| Directive partially executed | Do not attempt to continue a partial execution — raise a corrective directive |

**Step S6 — State resumption position:**
After completing S1–S5, record in the observations log:
```
SESSION RESUMED: [date and time]
  Resuming from: [step identifier]
  Extract version confirmed: [version]
  Patch accumulator state: [n items outstanding / patch complete]
  Open directives: [none / list]
  Open RD items: [none / n items — RD-IDs]
  Open Path 3 notes: [n notes]
```

Proceed to the identified resumption step.

---

### Fallback Protocol

A fallback position is defined for each potential failure mode in Stage 1. The fallback is always a known, clean state — not a partial state.

**Failure: session interrupted mid-step**
Fallback: the beginning of the interrupted step. Use the observations log to understand what was accomplished within the step before the interruption. Do not re-run work that has a confirmed written record. Continue from the last recorded action.

**Failure: patch partially applied (some operations succeeded, some failed)**
Fallback: the pre-patch state plus successful operations. Do not attempt to retry the failed operations by re-applying the full patch — this risks double-applying successful operations. Instead:
1. Request from CC: confirm the exact state of each operation from the patch (which succeeded, which failed).
2. Produce a targeted corrective patch covering only the failed operations.
3. Apply the corrective patch. Confirm.
4. Verify the full expected patch state before proceeding.
Record in observations log: `PATCH PARTIAL FAILURE: [date]. Operations [list] failed. Corrective patch [PATCH-ref] applied and confirmed.`

**Failure: sub-process interrupted before completion**
Fallback: the pre-sub-process state. The sub-process has a record in the observations log of what was triggered and what was expected. Request from CC: confirm the current state of the affected terms/groups. If the sub-process left data in a partial state, the sub-process instruction governs how to recover. Do not proceed in Stage 1 until the sub-process is confirmed complete and its own patch is applied.

**Failure: extract version stale (patches applied since extract was loaded)**
Fallback: request fresh extract. Read the patch history to understand what changed. Re-run only the affected checklist sections in Step 1.2 for fields that were patched — not the full audit. Record: `EXTRACT REFRESHED: [date]. Reason: [patches applied since last extract]. Re-checked: [list of affected sections].`

**Failure: RESEARCHER_DECISION item unresolvable within session**
Fallback: the step that raised the RD item, with the item formally recorded in the RD accumulator. Stage 1 pauses at the step that requires the RD resolution. The session log records the open item and exact resume instructions. Session may end cleanly — the RD item is not lost, it is in the accumulator awaiting the next session.

**Failure: Path 2 directive not confirmed by CC within session**
Fallback: Step 1.5 remains open. The directive is recorded in the observations log. The session log records the directive reference and states that Stage 1 resumes at Step 1.5 when CC confirmation is received. Session may end cleanly — the directive status is tracked; Stage 1 does not advance past Step 1.5 until it is confirmed.

---

### Session Close Protocol

Apply this protocol whenever a session ends within Stage 1 — whether at a natural breakpoint or due to interruption.

**Step C1 — Complete the current step or reach a clean stopping point:**
Do not end a session mid-step if it can be avoided. Complete the current step's sign-off statement before ending. If interruption is unavoidable, record the exact point within the step where work stopped — which item was being processed, what was determined, and what remains.

**Step C2 — Verify the observations log is complete:**
Confirm that all four named sections reflect the current state:
- Patch accumulator: all Path 1 items identified so far are listed
- RD accumulator: all Path 4 items identified so far are listed with status
- Path 3 notes: all Path 3 items identified so far are listed
- Progress record: last completed step is signed off

**Step C3 — Produce the session log:**
Per GR-PROC-006. The session log records:
- What was accomplished this session (steps completed, sign-offs achieved)
- Current position (last step completed; current step if mid-step)
- Open items (outstanding Path 4 RD items by RD-ID; outstanding Path 2 directives by directive reference; outstanding patch operations if patch not yet applied)
- Exact resume instructions (which step to resume from; what to load; what to confirm with CC first)

**Step C4 — Produce downloads:**
Per GR-PASS-001. At every session close: make the observations log and session log available for download.

Record in the observations log:
```
SESSION CLOSED: [date and time]
  Last completed step: [identifier]
  Session log produced: [filename]
  Downloads confirmed: observations log, session log
  Resume from: [step identifier]
```

---

*End of wa-global-sessionb-stage1-opening-v1-20260416.md*
*For insertion before Step 1.1 in the Stage 1 instruction*
*Replaces: Stage 1 Purpose block and outputs section from wa-global-sessionb-instruction-v5_0-20260415.md*
