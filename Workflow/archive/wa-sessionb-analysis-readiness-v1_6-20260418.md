# WA — Session B: Analysis Readiness Instruction
**Framework B — Soul Word Analysis Programme
Analysis Readiness Instruction — Data Validation, Preparation, and Stage 2 Handoff
Version 1_6 | 20260418 | Status: Active**

| **Document** | **Value** |
|---|---|
| Filename | wa-sessionb-analysis-readiness-v1_6-20260418.md |
| Supersedes | wa-sessionb-analysis-readiness-v1_5-20260416.md |
| Companion documents | wa-global-general-rules [current] │ wa-reference [current] │ wa-dimensionreview-instruction [current] │ wa-versecontext-instruction [current] │ wa-claudecode-instruction [current] │ wa-patch-instruction [current] │ wa-directive-instruction [current] |
| Inputs | Complete word data export: wa-[nnn]-[word]-complete-[date].json |
| Outputs | Observations log; session log; Type (a) patch; CC directives; Stage 1 Completion Record; Stage 2 Readiness Declaration |
| Claude AI role | Data audit; resolution path assignment; patch accumulation; directive production; completion verification; handoff |
| Claude Code role | Patch application; sub-process execution; extract production; field confirmation |
| Handoff to | wa-sessionb-analysis-output-v[current].md — Stage 2 begins after Stage 2 Readiness Declaration |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules [current]**.

Claude AI must confirm the global rules file has been loaded before beginning any work per GR-LOAD-001.

Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.

---

## Change Log

**v1_6 (2026-04-18):** GR-REF-002 sweep. (1) Header table: filename/supersedes refreshed; Companion documents row updated — retired `wa-sessionb-cc-instructions` replaced with `wa-claudecode-instruction`; `wa-patch-specification` replaced with `wa-patch-instruction`; added `wa-reference` and `wa-directive-instruction` to current corpus; all references use `[current]` token. (2) Governing Rules section: stale `wa-global-general-rules-v2_5-20260416.json` → `[current]`. (3) §What to Attach at Session Start: stale `wa-global-general-rules-v2_2-20260415.json` → `[current]`; retired `wa-sessionb-cc-instructions` → `wa-claudecode-instruction [current]`. (4) §Step 1.4 patch construction: retired `wa-patch-specification` → `wa-patch-instruction [current]`. (5) Footer version/supersedes refreshed. Prior v1_5 change note retained below for provenance.

**v1.5 (20260416):** Observations log version control made explicit. Step S0 added to Session Start Protocol: first action in every session is to open the observations log (first session) or increment its minor version and create a new versioned file (resumption). Session Close Protocol Step C4 updated: save the observations log as a new incremented version before producing downloads. Session log template in Step C3 updated: observations log version is now a required field. Outputs table updated: versioning note added to observations log row. Per GR-OBS-004 (version-increment at session boundary) and GR-FILE-004 (no overwrites).

**v1.4 (20260416):** Global rules architecture alignment. Step 1.4 format compliance table removed — it duplicated GR-DIR-006 content. Replaced with a single citation: "Per GR-DIR-006 — run self-check before submission." Governing rules reference updated to v2.5.

**v1.3 (20260416):** Patch filename updated to wa-[nnn]-[word]-patch-preanalysis-v[n]-[YYYYMMDD].json — fixed "patch" type token in position 4, word in position 3, per revised convention. Governing rules reference updated to v2.5.

**v1.2 (20260416):** Output table filenames corrected for GR-FILE-001/007/009 compliance: Type (a) patch filename changed from uppercase PATCH-... to lowercase wa-[nnn]-preanalysis-v[n]-[YYYYMMDD].json; CC directive filename pattern corrected from double-date pattern to single-date GR-DIR-007 compliant pattern wa-[nnn]-[word]-dir-[seq]-[desc]-v[n]-[YYYYMMDD].md. Governing rules reference updated to v2.4. Companion docs updated to v2.4.

**v1.1 (20260416):** Patch format compliance gate added to Step 1.4. New subsection "Format compliance check" inserted before patch presentation step, requiring Claude AI to verify all six structural compliance points (per GR-DIR-006) before presenting any patch for researcher approval. Governing rules reference updated from v2.2 to v2.3. Document status changed from Draft to Active.

**v1.0 (20260416):** New document. Principal changes from v5.0 Stage 1:

1. **Instruction split.** Session B now governed by two separate instructions: Analysis Readiness (this document — Stage 1) and Analysis Output (Stage 2). The Stage 1 Completion Record is the formal handoff between them.
2. **Resolution Classification Framework introduced.** Four named resolution paths (Type (a) patch / Process re-run directive / Stage 2a verification note / RESEARCHER_DECISION) applied consistently to every check in Step 1.2. No anomaly left without a path and a specific action.
3. **Step 1.2 fully rebuilt.** Against schema v3.9.0. Nine sections (A.0, A.1, A–H). Statistics pre-read (A.0) and audit_word history review (A.1) added. Section B restructured by term type. Three-number verse diagnostic for span filter failure. Every check specifies path, table/field/value or process sequence, observations log record.
4. **Step 1.3 restructured.** Old Steps 1.3 and 1.4 replaced by three sub-steps (1.3a — phase2 flags; 1.3b — findings preparation; 1.3c — B-target flags). All flag-related preparation grouped together.
5. **Step 1.5 extended.** Five explicit sub-process trigger types with sequences. Span filter failure distinguished from missing-groups trigger.
6. **Step 1.6 added.** Stage 1 Completion Verification and Handoff: targeted verification of corrections in fresh extract; 7-domain completion checklist; formal Stage 1 Completion Record and Stage 2 Readiness Declaration.
7. **Tracking document structure specified.** Four named sections in observations log (Patch Accumulator; RD Accumulator; Path 3 Notes; Progress Record) with formats and update triggers. Initiated before Step 1.1.
8. **Session start and close protocols specified.** Deterministic resumption from position markers. Six failure modes with defined clean fallback states.
9. **Integrity rules updated.** SB-1, SB-18 updated; SB-20 through SB-24 added.

*Prior version history: see wa-global-sessionb-instruction-v5_0-20260415.md.*

---

## Pipeline Position

```
Session A  (term extraction → complete JSON)
     │
     ▼
Verse Context  (verse relevance filtering, grouping, anchor designation)
     │
     ▼
Dimension Review  (dimension assignment → CLAUDE_AI confidence on all groups)
     │
     ▼
Analysis Readiness  (this instruction)
     ├── Step 1.1: Confirm extract version
     ├── Step 1.2: Audit complete JSON (resolution paths assigned)
     ├── Step 1.3: Prepare existing records
     │       ├── Step 1.3a: wa_term_phase2_flags
     │       ├── Step 1.3b: wa_session_b_findings
     │       └── Step 1.3c: wa_session_research_flags B-target (hard gate)
     ├── Step 1.4: Type (a) patch construction and application
     ├── Step 1.5: Sub-process execution and fresh extract
     └── Step 1.6: Completion verification and handoff
          └── Stage 1 Completion Record → Stage 2 Readiness Declaration
     │
     ▼
Analysis Output  (wa-sessionb-analysis-output-v[current].md)
     ├── Stage 2a: Comprehensive analysis → Observations log
     ├── Stage 2b: Q&A partitioning → Q&A log + patches
     └── Stage 2c: Structured output → Analytic word output
     │
     ▼
Session C  (word study production)
     │
     ▼
Session D  (cross-registry synthesis)
```

---

## What to Attach at Session Start

- This instruction file
- Global rules file: `wa-global-general-rules [current]`
- The complete word data export: `wa-[nnn]-[word]-complete-[date].json`
- CC instructions: `wa-claudecode-instruction [current]`

Sub-process instruction documents are attached only when a trigger fires:
- Verse Context sub-process: `wa-versecontext-instruction-v[current].md`
- Dimension Review sub-process: `wa-dimensionreview-instruction-v[current].md`

Do not load more data into the working session than the current step requires.

---

## Governing Disciplines

These disciplines apply without exception across all steps and all sessions.

**Step-by-step.** Per GR-PROC-001. Each step is completed and confirmed before the next begins.

**Write on discovery.** Per GR-OBS-001 (non-waivable). Every finding, path assignment, patch item, flag, and open question is written to the observations log at the moment it is determined. Nothing is accumulated in memory.

**Data is authoritative.** Per GR-PROC-002. Work strictly from what is in the JSON. Do not import general knowledge to fill gaps.

**All changes through patches or directives.** Per GR-PROC-003 and GR-DIR-001 through GR-DIR-005. Patches when field names, FK keys, and operations are certain. Directives when the outcome is known but execution path requires CC inspection. Both require researcher approval (GR-PROC-004).

**No DB state assumptions.** Per GR-DB-001. Claude AI never assumes the current state of the database. Check the extract; request from CC if not present; request a refresh if currency is in doubt.

**Researcher decision items.** Per GR-RD-001 through GR-RD-006. A RESEARCHER_DECISION item is raised only after Claude AI has exhausted its own analytical resources. It is presented in a discrete numbered block — never embedded in analysis.

**Session logs at every breakpoint.** Per GR-PROC-006.

**Analysis Readiness does not perform analysis.** Any step that requires analytical judgement — assessing the significance of a finding, drawing a conclusion about a word's meaning — must be deferred to Analysis Output. Record what was deferred and why. Per integrity rule SB-21.

---

---

## Stage 1 — Data Audit and Remediation

### Stage 1 Outputs

Stage 1 produces the following outputs. All are initiated at the start of Stage 1 — before Step 1.1 begins. Do not begin Step 1.1 until all tracking documents are open and the session start protocol is complete.

| Output | Filename pattern | When produced | Purpose |
|--------|-----------------|---------------|---------|
| Observations log | `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md` | Initiated at Stage 1 start; written continuously throughout; minor version incremented at each session boundary per GR-OBS-004 and GR-FILE-004 | Primary working record and recovery instrument. Contains all findings, path assignments, sign-off statements, patch accumulator, RD accumulator, Path 3 notes, and Stage 1 Completion Record. Version history: v1 = first session; v1.1 = second session; v1.2 = third session, etc. The session log always records which observations log version it corresponds to. |
| Session log | `wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[date].md` | Produced at each natural breakpoint and session end | Handoff document. Records current position, what was accomplished, open items, and exact resume instructions. Not the analytical record — that is the observations log. |
| Type (a) patch | `wa-[nnn]-[word]-patch-preanalysis-v[n]-[YYYYMMDD].json` | Constructed at Step 1.4 | Data correction patch. Compiled from the patch accumulator section of the observations log. Filename per GR-FILE-001/007/009; internal `patch_id` field retains `PATCH-[YYYYMMDD]-[nnn]-PREANALYSIS-V[n]` for applicator compatibility. |
| CC directives | `wa-[nnn]-[word]-dir-[seq]-[desc]-v[n]-[YYYYMMDD].md` | Produced as needed for Path 2 sub-process triggers | Plain-language directives to CC for process re-runs. Filename per GR-DIR-007 and GR-FILE-001/007/009. Each directive produced before researcher approval and CC execution. |

---

### Tracking Document Structure

The observations log has a defined structure. All four named sections are created at Stage 1 start — before any data is read. They are updated at the steps specified below.

**Open the observations log immediately and create these four sections:**

```
#### Type (a) Patch Accumulator
[Empty at start — populated during Steps 1.2, 1.3a, 1.3b, 1.3c, and RD resolutions]

#### RESEARCHER_DECISION Accumulator
[Empty at start — populated when Path 4 items are identified in any step]

#### Path 3 — Stage 2a Verification Notes
[Empty at start — populated when Path 3 items are identified in any step]

#### Stage 1 Progress Record
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

**Step S0 — Open or version-increment the observations log:**
Per GR-OBS-004 and GR-FILE-004. This is the first action of every session — before global rules confirmation, before reading any data.

| Condition | Action |
|-----------|--------|
| First session for this registry | Create observations log: `wa-[nnn]-[word]-sessionb-observations-v1-[YYYYMMDD].md`. Write the four empty named sections. Record: `SESSION STARTED: [date]. Observations log v1 created.` |
| Resumption — prior session ended cleanly | Increment minor version: read the current filename, increment `v[n]` to `v[n.1]` (e.g. v1 → v1.1, v1.2 → v1.3). Create the new versioned file as a copy of the prior version. Record: `SESSION RESUMED: [date]. Observations log incremented to v[n.1] from v[n].` All subsequent writes in this session go to the new file. |
| Resumption — prior session interrupted | Same as clean resumption: increment the version and create a new file. The prior version is preserved as the last confirmed state. |

State aloud the observations log version before proceeding: *"Observations log: wa-[nnn]-[word]-sessionb-observations-v[n]-[YYYYMMDD].md — this session writes to this file."*

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
  Observations log version: [wa-{nnn}-{word}-sessionb-observations-v{n}-{YYYYMMDD}.md]
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
- **Observations log version** — the exact filename and version of the observations log at the time the session log is produced (e.g. `wa-062-fellowship-sessionb-observations-v1.2-20260416.md`). This creates a recoverable link between the session log and the observations log state it describes.
- What was accomplished this session (steps completed, sign-offs achieved)
- Current position (last step completed; current step if mid-step)
- Open items (outstanding Path 4 RD items by RD-ID; outstanding Path 2 directives by directive reference; outstanding patch operations if patch not yet applied)
- Exact resume instructions (which step to resume from; what to load; what to confirm with CC first)

**Step C4 — Save the observations log as a new versioned file and produce downloads:**
Per GR-OBS-004, GR-FILE-004, and GR-PASS-001.

Before producing downloads:
1. Write the SESSION CLOSED record to the current observations log (see below).
2. Save the observations log under its current version filename — do not overwrite the prior version. The file written at session close is the recovery instrument for the next session start.
3. The session log must state the observations log filename and version at the time of writing.

Record in the observations log before saving:
```
SESSION CLOSED: [date and time]
  Observations log version at close: [wa-{nnn}-{word}-sessionb-observations-v{n}-{YYYYMMDD}.md]
  Last completed step: [identifier]
  Session log produced: [filename]
  Downloads confirmed: observations log v[n], session log
  Next session: resume from [step identifier]; increment observations log to v[n.1] at session start
```

Make both files available for download per GR-PASS-001.

---

### Step 1.1 — Confirm Extract Version

Per GR-DB-001 and GR-DATA-004. Before reading any data:

1. State the filename of the complete word data export attached to this session.
2. Request from CC: confirm this is the current version of the extract for registry [nnn] and return the version identifier and export date.
3. Wait for CC confirmation. If CC returns a different version as current — stop. The attached extract is stale. Request the current version before proceeding.
4. Record in observations log: `Extract confirmed: [filename] — version [n] — exported [date].`

Do not proceed until extract version is confirmed.

---

---

### Resolution Classification Framework

Every anomaly identified in Step 1.2 is assigned to exactly one of the four resolution paths below. The path determines the action. No anomaly is recorded without a path assignment. No anomaly is left with only "note" — every note either has a path or is not an anomaly.

**Path 1 — Type (a) patch (Claude AI fixes)**
*Applies when:* The correct value is determinable from the extract data alone, without verse reading or researcher judgement. Claude AI can construct the fix.
*Method:* Record in observations log: `PATH 1 — [table].[field]: current value = [x], correct value = [y]. Add to Type (a) patch accumulator.` State the exact table, field, and corrected value. These are compiled into the Type (a) patch at Step 1.4.
*Examples:* `language` mismatch with Strong's prefix; `delete_flagged=0` on a deleted term; `dominant_subject='NONE'` correctable from group description; missing `SMALL_VERSE_SAMPLE` quality flag; `mti_status` NULL on an XREF term (correct value: `xref_[owning_word]`); `somatic_link` inconsistent with `mti_term_flags` (where `mti_term_flags` is authoritative per GR-DATA-003).

**Path 2 — Process re-run directive (CC executes)**
*Applies when:* The data structure requires a process to be rebuilt — field patching alone cannot correct it. The verse corpus, the verse context classification, or the dimension assignments need to be re-generated.
*Method:* Record in observations log: `PATH 2 — Process re-run required: [process name]. Scope: [full registry / targeted: term [strongs]]. Sequence: [steps in order]. Session B is PAUSED at Step 1.2 until this directive is complete and confirmed by CC.` Identify the correct process and scope:
- **Span filter failure** (term has `span_match_count > 0` but `total_verse_records = 0`): re-extraction → audit_word re-run → Verse Context classification. Scope: targeted to the affected term(s).
- **Genuine zero-verse extraction** (term has `span_match_count = 0` and `total_verse_records = 0`): re-extraction → audit_word re-run. Scope: targeted.
- **OWNER term with no verse_context_groups** but verse records exist: Verse Context sub-process. Scope: targeted to the affected term(s).
- **Group with AUTOMATED dimension confidence**: Dimension Review sub-process. Scope: targeted to the affected group(s).
- **Group with NULL dimension**: Dimension Review sub-process. Scope: targeted.
Process re-run directives are produced as plain-language directives to CC per GR-DIR-001 and submitted for researcher approval before CC executes. Session B does not proceed past Step 1.2 until all Path 2 items are resolved and a fresh extract is confirmed.

**Path 3 — Stage 2a verification note (deferred, non-blocking)**
*Applies when:* The field value may be wrong but cannot be confirmed or corrected without reading verses. Stage 1 cannot make a determination. Stage 2a will make the determination when verses are read.
*Method:* Record in observations log: `PATH 3 — [table].[field] on [strongs]: current value = [x]. Cannot verify in Stage 1 — requires verse reading. Note for Stage 2a verification.` Do not patch. Do not block. The Stage 2a observations log will address these.
*Examples:* `god_as_subject` plausibility (cannot verify without verse reading); `somatic_link` value where `mti_term_flags` and `wa_term_inventory` agree but verse evidence may contradict; dimension assignment where confidence is CLAUDE_AI but the label appears inconsistent with the group description.

**Path 4 — RESEARCHER_DECISION (human decision required)**
*Applies when:* The anomaly cannot be resolved analytically, cannot be corrected by Claude AI alone, is not a process re-run case, and requires a human decision on direction. Apply Path 4 only after confirming Paths 1–3 do not apply and stating why.
*Method:* Record in observations log: `PATH 4 — RESEARCHER_DECISION accumulator: [RD-ID]. What was checked: [specific field/table/value]. Why unresolvable: [Path 1 ruled out: reason. Path 2 ruled out: reason. Path 3 ruled out: reason]. Question: [precisely stated]. Options: [option A — consequence; option B — consequence]. Claude AI recommendation: [one option with reasoning].` These are collected and presented as the formal RD block after Step 1.3c is complete. Session B does not proceed past Step 1.4 until all RD items are resolved.
*Examples:* `session_b_status = Analysis Complete` when Session B appears already run; `carry_forward = 0`; `word` field mismatch; term with genuine zero-verse extraction where reason is unclear; any situation where options have meaningfully different programme consequences.

**Resolution path decision rule:**
1. Can the correct value be determined from the extract data alone, without verse reading? → Path 1
2. Does the data structure require a process to be re-run? → Path 2
3. Does confirmation require reading verses? → Path 3
4. None of the above apply and human judgement is needed? → Path 4

---

### Section A.0 — Statistics Pre-Read

Before running any section-by-section checks, read the `statistics` section of the extract. This section provides self-reported counts that serve as a first-pass orientation signal.

**Record in observations log:** All statistics values. Then check the following internal consistency pairs:

| Pair to compare | Expected relationship | If inconsistent |
|-----------------|----------------------|-----------------|
| `active_owner_term_count` vs count of OWNER terms in `terms.active_terms` | Should match | Path 1 if extract count differs from statistics count — note discrepancy; stale registry data |
| `somatic_link_inventory_count` vs `somatic_link_mti_flag_count` | Should match | Path 3 — note discrepancy; cross-check B3 will detail which terms are affected |
| `god_as_subject_inventory_count` vs god_as_subject count in `terms.active_terms` | Should match | Path 3 — note discrepancy; cross-check B in detail |
| `active_group_count` vs count of groups in `verse_context_groups` | Should match | Note discrepancy — check for soft-deleted groups in the count |
| `groups_without_dimension` | Should be 0 | Path 2 (Dimension Review sub-process) if > 0 |
| `groups_at_automated_confidence` | Should be 0 | Path 2 (Dimension Review sub-process) if > 0 |
| `session_b_flags_unresolved` | Should be 0 | Note count — these will be Step 1.3c items |
| `catalogue_questions_master` | Should be 194 or more | Path 4 if < 194 — catalogue may be stale |
| `catalogue_links_total` vs `findings_by_status` counts | Informational — note both | Record for Step 1.3b context |

**Record in observations log:** `Section A.0 complete. Statistics read. Internal consistency: [pass / [n] discrepancies noted]. Discrepancies: [list]. Proceeding to Section A.1.`

---

### Section A.1 — Audit_word History and Unresolved REVIEW Flags

Read the `patch_history.word_run_states` section of the extract. This records every prior audit_word run and its outcome. Unresolved REVIEW flags from prior runs are open items that Session B inherits.

**For each `word_run_state` row:**

1. Note the `run_id`, `audit_result`, and `audit_detail`.
2. If `audit_result = 'PASS'`: record and proceed. No action.
3. If `audit_result = 'REVIEW'` and `researcher_approved = 1`: record as previously reviewed. No action unless the current extract shows the issue persists.
4. If `audit_result = 'REVIEW'` and `researcher_approved = 0`: this is an **inherited open item**. For each REVIEW flag in `audit_detail`:

| Flag code | Meaning | Resolution path |
|-----------|---------|----------------|
| WR-05 (ID gaps in wa_term_inventory) | Sequence gaps in term IDs — may indicate missing records | Path 3 — note; not analytically blocking but record for awareness |
| WR-08 (Low verse/occurrence ratio) | Specific terms have verse counts < 20% of occurrence count | Cross-check against Section C — if not already flagged, assign Path 1 (missing SMALL_VERSE_SAMPLE flag) or Path 2 (span filter failure) as appropriate |
| WR-20 (NULL span_strong_match on verse records) | Back-population step may not have completed for pre-v9 records | Path 3 — note count; these verses have unvalidated span matching; flag for Stage 2a awareness |
| Other WR codes | Read the description | Apply resolution path decision rule above |

**Persistent flags** (same flag appearing across multiple `audit_result = 'REVIEW'` runs with `researcher_approved = 0`): these are higher priority — they have not been resolved across multiple sessions. Record as persistent and note for RESEARCHER_DECISION accumulator if they cannot be assigned Path 1, 2, or 3.

**Record in observations log:** `Section A.1 complete. [n] audit runs reviewed. [n] REVIEW flags inherited, [n] previously approved, [n] open and dispositioned as follows: [list of flag → path assignments].`

---

### Section A — Registry Record (`word_registry`)

One row per word. These fields describe the word's overall programme state.

| Field | Valid state | Check | Path | Action |
|-------|------------|-------|------|--------|
| `word` | Matches the word being analysed | Confirm spelling matches session context | 4 | Mismatch — RESEARCHER_DECISION: confirm correct registry before proceeding |
| `no` | Matches registry number [nnn] | Confirm | 4 | Mismatch — STOP immediately; confirm with researcher |
| `cluster_assignment` | A valid cluster code (C01–C22) | Present, not NULL, not 'unassigned' | 4 | NULL or 'unassigned' — RESEARCHER_DECISION: confirm cluster assignment before proceeding |
| `session_b_status` | `Pre-Analysis Complete` (required) or `Verse Context Reset` (legacy acceptable) | Check against valid values — Appendix A.5 of patch spec | 4 | `Analysis Complete` or `Session B Complete` — RESEARCHER_DECISION: Session B may already have run; confirm before proceeding. `NULL` — RESEARCHER_DECISION: word may not have completed DataPrep. |
| `verse_context_status` | `Complete` | Confirmed against Appendix A.7 of patch spec | Hard gate | Not `Complete` — STOP. Verse Context must complete first. This is a hard gate — record and halt. |
| `dim_review_status` | `Complete` | Present and matches | Hard gate | Absent or incomplete — STOP. Dimension Review must complete first. Hard gate. |
| `dim_review_version` | Populated | Not NULL | 3 | NULL — note for Stage 2a; not blocking |
| `dimensions` | Populated — at least one value | Not NULL or empty | 4 | NULL or empty — RESEARCHER_DECISION: Dimension Review may not have written output to registry |
| `carry_forward` | 1 | If 0 — note explicitly | 4 | 0 — RESEARCHER_DECISION: this registry is flagged for exclusion; confirm whether to proceed |
| `unique_term_count` | Should approximate OWNER term count in extract | Cross-check: count OWNER terms in `terms.active_terms`; compare | 1 | Discrepancy > 10% — Path 1: note; update `unique_term_count` in patch if extract count is verifiably more current |
| `shared_term_count` | ≥ 0 | Present | 1 | NULL — Path 1: set to 0 |
| `term_sharing_ratio` | 0.0–1.0; consistent with `shared / (unique + shared)` | Plausibility check | 3 | Significant deviation — Path 3: note; not analytically blocking |
| `phase1_term_count` | > 0 | Present | 3 | NULL or 0 — Path 3: note; may indicate incomplete Session A |
| `phase1_verse_count` | > 0 | Present | 3 | NULL or 0 — Path 3: note |

**Cross-field check A1 (hard gates):** `verse_context_status = 'Complete'` AND `dim_review_status = 'Complete'` must BOTH be true. If either fails: STOP. Do not proceed to any further section.

**Record in observations log:** `Section A complete. Hard gates: [PASS/FAIL]. Path 1 items: [n]. Path 4 items: [n]. Anomalies: [list].`

---

### Section B — Term Inventory

The extract contains three distinct term populations. Each has different validity expectations and different checks. Work through each population separately.

#### B1 — Active OWNER terms (`term_owner_type = 'OWNER'`, `mti_terms.status IN ('extracted','extracted_thin')`)

These are the primary analytical terms for this registry. Every field must be sound.

| Field | Valid state | Check | Path | Action |
|-------|------------|-------|------|--------|
| `strongs_number` | Format H[digits][suffix] or G[digits][suffix]; no spaces | Regex check: `^[HG]\d+[A-Z]?$` | 1 | Malformed — Path 1: correct in `wa_term_inventory.strongs_number` |
| `language` | 'Hebrew' for H prefix; 'Greek' for G prefix | Cross-check prefix vs language field | 1 | Mismatch — Path 1: correct `wa_term_inventory.language` |
| `transliteration` | Present | Not NULL | 3 | NULL — Path 3: note; not analytically blocking |
| `step_search_gloss` OR `word_analysis_gloss` | At least one present | Not both NULL | 3 | Both NULL — Path 3: note; term may lack STEP data |
| `occurrence_count` | > 0 | Numeric, > 0 | 3 | 0 or NULL — Path 3: note; cross-check against verse records in Section C |
| `mti_terms.status` | `extracted` or `extracted_thin` | Confirm value in Appendix A.4 of patch spec | 1 | Value not in controlled vocabulary — Path 1: correct `mti_terms.status` |
| `evidential_status` | NULL at Session B entry (will be set in Stage 2) | Note if already populated | 3 | If populated: record value; confirm in Stage 2a |
| `god_as_subject` | 0 or 1; plausible for term type | Populated; if 1 on a function word or particle — implausible | 3 | NULL — Path 1: set to 0 as safe default. Implausible value — Path 3: note for Stage 2a verification. Do not attempt correction without verse reading. |
| `somatic_link` | Must be consistent with `mti_term_flags` (flag_id IN (3,4)) per GR-DATA-003 | Compare `somatic_link` on `wa_term_inventory` against presence of flag_id 3 or 4 in `mti_term_flags` for this term | 1 | `somatic_link=0` but somatic mti_flag present: Path 1 — set `somatic_link=1` (mti_term_flags is authoritative). `somatic_link=1` but no somatic mti_flag: Path 3 — note for Stage 2a verification; do not remove without verse evidence. |
| `causative_form_present` | 0 or 1 | Populated | 1 | NULL — Path 1: set to 0 |
| `delete_flagged` | 0 for active terms | Must be 0 | 4 | If 1 — this term is soft-deleted but appearing in active set. RESEARCHER_DECISION: investigate why deleted term is in active population. |
| `term_owner_type` | 'OWNER' | Confirmed | 1 | NULL — Path 1: set to 'OWNER' based on context |
| `parsed_meaning_id` | FK resolves in `wa_meaning_parsed` if populated | Verify FK if not NULL | 1 | Dangling FK — Path 1: set to NULL (broken reference is worse than absent) |

**Cross-check B1 — occurrence count vs verse records:**
For each OWNER term, retrieve from `verse_records_summary`: `span_match_count`, `total_verse_records`, `delete_flagged_count`.

Apply the following diagnostic:

| Condition | Diagnosis | Path | Action |
|-----------|-----------|------|--------|
| `span=0, active=0, deleted=0` | No verses extracted at all | 2 | Re-extraction → audit_word re-run. Note: targeted to this term. Session B paused until complete. |
| `span>0, active=0, deleted=span` | Span filter failure — all verses filtered out | 2 | Re-extraction → audit_word re-run → Verse Context re-classification. Note: targeted. Session B paused. Record: `[strongs] span filter failure. [n] records extracted, all deleted by span filter. Genuine verse content confirmed exists (term has [occ] occurrences). Path 2: re-extraction required.` |
| `span>0, active>0` | Normal — verses present | Continue | Check ratios below |
| `active > occ * 1.1` | Possible over-extraction | 4 | RESEARCHER_DECISION: verse count exceeds occurrence count by > 10%. Possible duplicate records or incorrect span matching. |
| `active < occ * 0.2` AND `occ > 20` | Small verse sample | 1 | Check `wa_data_quality_flags` for this term. If no `SMALL_VERSE_SAMPLE` flag: Path 1 — add quality flag. If flag exists: PASS. |

**Cross-check B2 — OWNER terms with no verse_context_groups:**
For each OWNER term: check whether at least one group exists in `verse_context_groups` for this `mti_term_id`.

| Condition | Path | Action |
|-----------|------|--------|
| Term has verse records AND at least one group | PASS | Continue |
| Term has verse records but zero groups | 2 | Verse Context sub-process — targeted to this term |
| Term has zero active verse records (caught in B1) | Already handled in B1 | Do not duplicate |

**Cross-check B3 — god_as_subject consistency with statistics:**
Compare `statistics.god_as_subject_inventory_count` against count of OWNER terms in the extract with `god_as_subject = 1`. If these match the statistics pre-read: PASS. If they differ: Path 3 — note discrepancy; the statistics field reflects the database state at export time.

#### B2 — XREF terms (`term_owner_type = 'XREF'`)

Cross-registry terms — primary analysis in another registry. Lighter checks.

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `mti_terms.status` | Should be `xref_[owning_word]` per Appendix A.4 | 1 | NULL or wrong value — Path 1: set to `xref_[owning_word]` where owning_word is from `mti_terms.owning_word` or `owning_registry_word` in the extract |
| `owning_registry_no` | Must reference a valid, registered word in the programme | Confirm registry exists in extract context | 4 | Owning registry not recognised — RESEARCHER_DECISION: XREF term points to an unregistered word |
| Verse records | May have zero active verses — this is acceptable for XREF terms | Note count | 3 | Zero active verses — Path 3: note; XREF terms are not primary analytical subjects; absence is not a data gap |
| `delete_flagged` | 0 | Must be 0 in active XREF set | 4 | If 1 — soft-deleted XREF in active set; RESEARCHER_DECISION |

Record in observations log: `XREF terms: [n] reviewed. [n] with NULL mti_status corrected to xref_[word] (Path 1). [n] with valid owning registry. [n] path 3 notes.`

#### B3 — Deleted terms (`mti_terms.status = 'delete'`)

Deleted terms are outside analytical scope. One cross-table consistency check only.

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `wa_term_inventory.delete_flagged` | Should be 1 for deleted terms | For each deleted term: confirm `delete_flagged = 1` on its `wa_term_inventory` row | 1 | `delete_flagged = 0` on a deleted term — Path 1: set `delete_flagged = 1`. This is a data consistency correction. Note count: `[n] deleted terms had delete_flagged=0; corrected in Type (a) patch.` |

Record in observations log: `Section B complete. OWNER terms: [n] reviewed. Path 1 items: [n]. Path 2 items: [n] (span filter failure: [n]; zero extraction: [n]; no groups: [n]). Path 3 notes: [n]. Path 4 items: [n]. XREF terms: [n] reviewed. [n] mti_status corrected. Deleted terms: [n], [n] delete_flagged corrections.`

---

### Section C — Verse Records (`wa_verse_records`)

The three-number diagnostic for each term was applied in Section B cross-check B1. Section C supplements this with checks on verse record quality.

For each term in `verse_records_summary` where `total_verse_records > 0`:

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `verse_text` populated | Not NULL or empty string | 3 | NULL verse text — Path 3: note; verse cannot be read in Stage 2a; record reference |
| `reference` format | [Book] [Chapter]:[Verse] e.g. 'Rom 3:23' | Plausibility check | 1 | Malformed reference — Path 1: correct if pattern is clear; otherwise Path 3 note |
| `span_strong_match` | 0 or 1 | Populated | 3 | NULL span_strong_match — Path 3: note count; back-population (WR-20) may not have completed for pre-v9 records; these verses have unvalidated span matching |
| `translation` | 'ESV' (programme standard) | Confirm | 4 | Non-ESV translation — RESEARCHER_DECISION: confirm whether this is intentional or an import anomaly |
| `delete_flagged` | 0 for active verse records | Must be 0 in active set | 4 | If 1 — soft-deleted verse in active count; RESEARCHER_DECISION |

**NULL span_strong_match count:** If WR-20 was flagged in Section A.1, the count of NULL span_strong_match records should be consistent with the audit_word detail. If the count has grown since the last audit run: Path 4 — RESEARCHER_DECISION.

Record in observations log: `Section C complete. Verse records checked. NULL verse_text: [n]. NULL span_strong_match: [n] (consistent with WR-20: [yes/no]). Path items: [n].`

---

### Section D — Verse Context Groups (`verse_context_group` + `verse_context`)

#### D1 — Groups

| Field | Valid state | Path | Action |
|-------|------------|------|--------|
| `group_code` | Format: [mti_term_id]-[seq] e.g. '1234-001' | Present, unique, correctly formatted | 1 | Malformed — Path 1: correct format. Duplicate code — Path 4: RESEARCHER_DECISION |
| `context_description` | Present, substantive (> 20 characters) | Not NULL, not a placeholder | 4 | NULL or < 20 chars — RESEARCHER_DECISION: blank descriptions block analytical grouping; Verse Context re-run may be required |
| `delete_flagged` | 0 for active groups | Must be 0 | 4 | If 1 — soft-deleted group in active set; RESEARCHER_DECISION |
| `mti_term_id` | FK to a term in the active or XREF term set | Verify term is in the extract | 1 | FK to a deleted term — Path 1: note as data integrity gap; the group references a term outside scope |

#### D2 — Anchor verses within groups

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| Each group has ≥ 1 `is_anchor = 1` verse | Count of anchor verses > 0 per group | 2 | Zero anchor verses in a group — Path 2: targeted Verse Context re-run for this group |
| `is_anchor` and `is_related` not both 1 on same verse | Mutually exclusive | 1 | Contradiction — Path 1: correct `is_related = 0` where `is_anchor = 1` |
| `delete_flagged = 0` for active verses | 0 | 4 | Soft-deleted verse in active count — RESEARCHER_DECISION |

#### D3 — Set-aside verses

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `set_aside_reason` populated | Should have a reason | 3 | NULL reason — Path 3: count NULL-reason set-asides. If > 20% of total set-aside: note as unverifiable set-aside; Stage 2a should examine a sample. Not blocking. |

**Cross-check D1 — dominant_subject:**
For each active group, check `dimension_assignment.dominant_subject`. Valid values: 'God', 'Human', 'Mixed', 'Community', 'Other'.

| Condition | Path | Action |
|-----------|------|--------|
| `dominant_subject` is NULL | 4 | RESEARCHER_DECISION: cannot be set without reading the group's verses |
| `dominant_subject` = 'NONE' (string) | 1 | Path 1: determine correct value from group description alone. If group description clearly indicates human activity → 'Human'. Divine activity → 'God'. Mixed → 'Mixed'. If unclear from description alone → Path 4 |
| `dominant_subject` is a valid value | PASS | Continue |

**Cross-check D2 — verse counts vs dimension index:**
For each group with a `dimension_assignment`: compare `anchor_count + related_count` in the dimension_assignment data against the actual count of `is_anchor` and `is_relevant` verse_context rows for that group.

| Condition | Path | Action |
|-----------|------|--------|
| Counts match within 5% | PASS | Continue |
| Counts differ by > 5% | 3 | Path 3: note as stale dimension index counts; not blocking; Stage 2a will use live verse data |

Record in observations log: `Section D complete. Groups: [n] active. Anchor check: [n] groups with no anchors (Path 2). Dominant subject: [n] NULL (Path 4), [n] 'NONE' corrected (Path 1). Set-aside NULL reason: [n] of [total] ([%]).`

---

### Section E — Dimension Assignments (`wa_dimension_index`)

For each group in the extract, check its `dimension_assignment` sub-object.

| Field | Valid state | Path | Action |
|-------|------------|------|--------|
| `dimension` | Not NULL | Any non-NULL value from Dimension Review is acceptable. The Dimension Review instruction governs valid vocabulary — do not validate vocabulary here. | 2 | NULL dimension — Path 2: Dimension Review sub-process for this group |
| `dimension_confidence` | `CLAUDE_AI` or `RESEARCHER` | Not `AUTOMATED` | 2 | `AUTOMATED` — Path 2: Dimension Review sub-process for this group |
| `dominant_subject` | See Section D cross-check D1 | Already checked in Section D | — | Handled in Section D |
| `manual_override` | 0 or 1 | Populated | 1 | NULL — Path 1: set to 0 |
| `delete_flagged` | 0 for active rows | Must be 0 | 4 | If 1 — soft-deleted dimension row in active set; RESEARCHER_DECISION |
| `owning_registry_no` | Must match this registry's `no` | Cross-check | 4 | Mismatch — RESEARCHER_DECISION: dimension row may belong to another registry |

**Cross-check E1 — every active group has exactly one dimension assignment:**
For each group in `verse_context_groups`: confirm exactly one `dimension_assignment` sub-object is present.

| Condition | Path | Action |
|-----------|------|--------|
| 0 dimension rows | 2 | Dimension Review sub-process |
| 1 dimension row | PASS | Continue |
| > 1 dimension rows | 4 | RESEARCHER_DECISION: duplicate dimension assignments for same group |

**Cross-check E2 — Somatic/Embodied dimension vs somatic term flags:**
Note: dimension vocabulary varies by programme version. Do not test for a specific dimension label. Instead: for groups where the dimension label contains 'Somatic' or 'Embod' (case-insensitive): confirm the corresponding term has `somatic_link = 1` in `wa_term_inventory` or a somatic flag in `mti_term_flags`. If inconsistent: Path 3 — note for Stage 2a verification.

**Cross-check E3 — Theological/Divine-Human dimension vs god_as_subject:**
For groups where the dimension label contains 'Theolog' or 'Divine' or 'God' (case-insensitive): confirm the corresponding term has `god_as_subject = 1` or a GOD_AS_SUBJECT flag in `mti_term_flags`. If inconsistent: Path 3 — note for Stage 2a verification.

Record in observations log: `Section E complete. [n] groups with dimension assignments. NULL dimension: [n] (Path 2). AUTOMATED confidence: [n] (Path 2). Somatic/Divine consistency notes: [n] (Path 3).`

---

### Section F — Existing Findings and Flags (counts and orientation)

Section F is situational awareness only. Detailed review happens in Step 1.3. Do not action items here.

**F1 — `wa_session_b_findings`:**
From extract or from CC: count rows for registry [nnn] where `delete_flag = 0`. Note: total active, count by status (`pending` / `in_review` / `complete`), count with catalogue links.
Record: `Findings for registry [nnn]: [n] active. Status: pending=[n], in_review=[n], complete=[n]. Catalogue links: [n]. Step 1.3b will process these.`

**F2 — `wa_session_research_flags`:**
Count rows by `session_target` and `resolved`.
Record: `Research flags for registry [nnn]: Session D: [n] total, [n] unresolved. Session B: [n] total, [n] unresolved.`
B-target unresolved count: if > 0, record: `[n] B-target flags will be addressed in Step 1.3c.`

**F3 — `wa_term_phase2_flags`:**
Count rows for active terms where `delete_flagged = 0`.
Record: `Phase2 flags: [n] across [n] terms. Step 1.3a will assess these.`

**F4 — `wa_obs_question_catalogue`:**
Confirm master catalogue count from extract statistics: should be 194 or more.
Confirm registry-specific questions count: these are the questions already indexed for this word.
Record: `Catalogue: master=[n], registry-indexed=[n].`

**F5 — `correlation_signals`:**
Note: ranked pairs, xref sharing pairs, shared anchor verse count.
Record: `Correlation signals: [n] ranked pairs, [n] shared anchors. Stage 2a will read these.`

---

### Section G — Supporting Term Data

Check for presence and basic consistency. Do not perform analytical review.

**G1 — Meaning data (`wa_meaning_parsed` / `wa_meaning_sense` / `wa_meaning_stem`):**
For each active OWNER term:
- `parsed_meaning_id` populated → confirm FK resolves. If dangling: Path 1 — set to NULL.
- `wa_meaning_parsed` row present → confirm `wa_meaning_sense` has at least one row. Zero senses on a populated parse: Path 3 — note as incomplete parse.
- `has_causative_stem = 1` → confirm at least one `wa_meaning_stem` row. Absent: Path 3 — note.
- No meaning data at all → confirm `NO_WORD_ANALYSIS` quality flag is present. Absent: Path 1 — add quality flag.

**G2 — Root families (`wa_term_root_family`):**
For each active OWNER term:
- Note whether root family records are present.
- `root_code` must be populated if row exists: Path 1 if NULL.
- `root_language` should match term's language: Path 1 if mismatch.
- Zero root family records: not anomalous — note count only.

**G3 — Related words (`wa_term_related_words`):**
For each active OWNER term:
- Note count of related word records.
- Zero related words for a primary term with high occurrence count: Path 3 — note; may indicate limited STEP data.

**G4 — LSJ data (`wa_lsj_parsed`, Greek terms only):**
For Greek OWNER terms:
- Note whether `wa_lsj_parsed` row is present.
- Absence is not anomalous — note count only.

**G5 — Cross-registry links (`wa_cross_registry_links`):**
Note count of rows for this registry.
Record: `Cross-registry links: [n]. Stage 2a will read these.`

Record in observations log: `Section G complete. Meaning data: [n] terms with parse, [n] without. Root family gaps: [n]. Path 1 items from G: [n].`

---

### Section H — Step 1.2 Close and Hard Gate Check

After completing all sections, produce the consolidated audit summary:

```
Step 1.2 Audit Summary — Registry [nnn] [word]
Date: [date]
Extract version: [version]

Registry state:
  session_b_status = [value]
  verse_context_status = [value]
  dim_review_status = [value]
  carry_forward = [value]

Term populations:
  OWNER terms (extracted/extracted_thin): [n]
  XREF terms: [n]
  Deleted terms: [n]

Verse coverage:
  Total active verse records (OWNER terms): [n]
  Terms with span filter failure: [n] — [strongs list]
  Terms with zero active verses (genuine extraction gap): [n] — [strongs list]

Verse context groups:
  Active groups: [n]
  Groups with NULL dimension (Path 2): [n]
  Groups with AUTOMATED confidence (Path 2): [n]
  Groups with no anchor verse (Path 2): [n]
  Groups with dominant_subject issue (Path 1/4): [n]

Audit history:
  audit_word REVIEW flags inherited: [n] — [WR codes]

Resolution summary:
  Path 1 (Type (a) patch items): [n total] — [brief list]
  Path 2 (Process re-run directives): [n total] — [process: scope per item]
  Path 3 (Stage 2a verification notes): [n total] — [brief list]
  Path 4 (RESEARCHER_DECISION items): [n total] — [RD-IDs]
```

**Hard gate check — all conditions must be true before proceeding to Step 1.3:**

| Condition | Required state | If not met |
|-----------|---------------|-----------|
| `verse_context_status` | `Complete` | STOP — hard gate failure. Record and halt. |
| `session_b_status` | `Pre-Analysis Complete` or `Verse Context Reset` | STOP — confirm with researcher |
| `dim_review_status` | `Complete` | STOP — Dimension Review must complete first |
| All hard gate conditions from Section A | PASS | STOP — resolve before proceeding |
| No active OWNER term has `mti_terms.status = NULL` | 0 NULL-status OWNER terms | STOP — Path 1 patch must be confirmed before Step 1.3 |
| No active OWNER term has span filter failure (Path 2) | 0 span filter failures | STOP — Path 2 directive must be complete, re-run confirmed, fresh extract pulled |
| Unresolved `audit_word` REVIEW flags with `researcher_approved = 0` | All dispositioned to a path | If any PATH 4 items from audit history — include in RESEARCHER_DECISION block; gate holds until resolved |
| `carry_forward` | 1 | STOP — confirm with researcher |

**If all conditions are met:** Record `Step 1.2 complete. All hard gate conditions met. Path 2 directives: [none / [n] confirmed complete]. Path 4 items accumulated for RD block: [n]. Proceeding to Step 1.3.`

**If any Path 2 items remain outstanding:** Step 1.2 is not complete until the Path 2 directives have been executed by CC and a fresh extract confirming the corrected data has been pulled. Re-run Section B and Section C checks for the affected terms after the fresh extract is available.

---

### Step 1.3 — Prepare Existing Records

Step 1.3 has three sequential sub-steps. All three must be complete before proceeding to the RESEARCHER_DECISION block. Each sub-step has its own sign-off record in the observations log.

**Governing principle for Step 1.3:** This step prepares existing data for Stage 2. It does not perform analysis. Specifically:
- It assesses flags against verse evidence to determine data validity — not analytical significance.
- It links existing findings to catalogue questions to confirm they are ready for Stage 2 — not to answer those questions.
- It resolves data quality issues that must be cleared before Session B can proceed — not to explore their analytical implications.

If at any point in Step 1.3 a decision appears to require analytical judgement rather than a data call, stop. Record the item as requiring Stage 2 work and proceed. Do not perform analysis in Stage 1.

---

#### Step 1.3a — `wa_term_phase2_flags`: Assess All Advisory Term Flags

**Purpose:** Review all phase2 analytical flags on this registry's active terms. These flags are advisory — prior-session hypotheses about terms. They are not confirmed analytical facts. Each flag is assessed against the verse evidence and given a disposition. Rejected and irrelevant flags are soft-deleted. Thin-evidence flags are noted for Stage 2.

**Action 1 — Request data from CC:**

Request from CC: return all rows from `wa_term_phase2_flags` where `term_inv_id` is in the active term set for registry [nnn] AND `delete_flagged = 0`. Join to `wa_term_inventory` to include: `term_inv_id`, `strongs_number`, `transliteration`, `flag_code`, `description` (if any), `wa_term_inventory.status`.

Also join to `mti_terms` to confirm each term's current `status` in `mti_terms`.

**Action 2 — If zero rows returned:**

Record in observations log: `Step 1.3a: wa_term_phase2_flags — 0 flags for this registry. Step 1.3a complete.`

Proceed to Step 1.3b.

**Action 3 — If rows returned, assess each flag:**

Work through each flag one at a time. For each flag:

**Step 1:** Check `mti_terms.status` for this term.
- If `status = 'delete'` — the term is outside analytical scope. Record: `[flag_code] on [strongs] — irrelevant, mti_terms status = delete. No patch needed.` Move to next flag.
- If `status` is not `delete` — proceed to Step 2.

**Step 2:** Identify the term type from the extract.
- If the term is a particle, preposition, conjunction, article, or pronoun with no inner-being content — record: `[flag_code] on [strongs] — irrelevant, function word. Add to Type (a) patch: delete_flagged = 1, obsolete_reason = 'Function word — no inner-being analytical content.'` Move to next flag.
- Otherwise — proceed to Step 3.

**Step 3:** Count the verses available for this term in the extract.
- If verse count is 0 or 1 — record: `[flag_code] on [strongs] — thin evidence. [n] verses available. Carrying forward to Stage 2 for assessment.` No patch. Move to next flag.
- If verse count is 2–4 — note as thin evidence but proceed to Step 4 with caution. Record: `[flag_code] on [strongs] — thin evidence ([n] verses). Attempting assessment.`
- If verse count is 5 or more — proceed to Step 4.

**Step 4:** Read the verses for this term in the extract. For each verse, ask: does this verse support the flag claim?

Do not use general knowledge. Work only from what the verses say.

- If the verse evidence supports the flag: record `[flag_code] on [strongs] — confirmed by [verse reference(s)].` Flag stands — no patch needed.
- If the verse evidence does not support the flag: record `[flag_code] on [strongs] — rejected. Reason: [specific reason grounded in verse evidence].` Add to Type (a) patch: `delete_flagged = 1`, `obsolete_reason = '[reason]'`.
- If the evidence is present but insufficient to confirm or reject: record `[flag_code] on [strongs] — thin evidence. [n] verses available. Cannot confirm or reject from this data. Carrying forward to Stage 2.` No patch.

**Note on NULL descriptions:** Where `description` is NULL — which is the case for the majority of bulk-imported flags — the assessment is made entirely from the verse evidence. The absence of prior reasoning does not block assessment. The verses carry the full evidential weight.

**Action 4 — Record sign-off in observations log:**

`Step 1.3a complete. Flags reviewed: [total]. Confirmed: [n]. Rejected: [n] — added to Type (a) patch. Irrelevant (term deleted): [n]. Irrelevant (function word): [n] — added to Type (a) patch. Thin — carried to Stage 2: [n].`

Proceed to Step 1.3b.

---

#### Step 1.3b — `wa_session_b_findings`: Prepare Existing Findings for Stage 2

**Purpose:** Review all active findings for this registry. For each finding, confirm it has a linked catalogue question in `wa_finding_catalogue_links`. Where no link exists, find the best matching question in `wa_obs_question_catalogue` and create a suggested link. Where no matching question exists in the catalogue, note the finding as requiring a new question — that question will be formulated in Stage 2b. Where a finding is demonstrably no longer valid as a data matter (not an analytical judgement), soft-delete it.

This step does not answer catalogue questions. It does not reframe findings analytically. It does not make analytical conclusions. It prepares findings so that Stage 2 can work with them.

**Action 1 — Load the catalogue:**

The catalogue JSON extract (`wa_obs_question_catalogue`) must be available in this session. If it is not loaded, request from CC: return all rows from `wa_obs_question_catalogue` where `deleted = 0`, ordered by `obs_id`. Confirm 194 or more rows are returned before proceeding.

**Action 2 — Request findings data from CC:**

Request from CC: return all rows from `wa_session_b_findings` where `registry_id = [nnn]` AND `delete_flag = 0`. Include all fields. Also return all rows from `wa_finding_catalogue_links` where `finding_id` is in the returned finding set AND `delete_flagged = 0`.

**Action 3 — If zero findings returned:**

Record in observations log: `Step 1.3b: wa_session_b_findings — 0 active findings for registry [nnn]. Step 1.3b complete.`

Proceed to Step 1.3c.

**Action 4 — If findings returned, process each finding:**

Work through each finding one at a time. For each finding:

**Step 1:** Check whether this finding already has a catalogue link.

From the `wa_finding_catalogue_links` data returned: does a row exist for this `finding_id` with `delete_flagged = 0`?

- **Yes — link exists:** Record in observations log: `[finding_code] — catalogue link exists ([question_code], status=[link_status]). No action needed.` Move to next finding.
- **No — no link:** Proceed to Step 2.

**Step 2:** Assess whether this finding is still valid.

Read the finding text and finding_type. Ask: is there a concrete data reason why this finding cannot be valid — for example, the term it describes has since been deleted, the group it references has been soft-deleted, or the finding duplicates another finding in identical wording?

- **Finding is invalid for a data reason:** Record in observations log: `[finding_code] — invalid, reason: [specific data reason]. Add to Type (a) patch: delete_flag = 1, obsolete_reason = '[reason]', status = 'complete'.` Move to next finding.
- **Finding appears valid — proceed to Step 3.** Do not discard a finding because it seems analytically weak or incomplete. Only discard for concrete data reasons. Analytical assessment belongs to Stage 2.

**Step 3:** Search the catalogue for a matching question.

Read the finding text and finding_type. Search `wa_obs_question_catalogue` for a question whose `question_text` most directly addresses the analytical territory of this finding.

Use this decision sequence:

a. Is there a question that specifically addresses what this finding observes? If yes — that is the candidate. Note it and proceed to Step 4.

b. Is there a question that addresses the same general analytical territory, though not the specific observation? If yes — that is the candidate at PARTIAL coverage. Note it and proceed to Step 4.

c. Is there no question that addresses this territory at all? Record in observations log: `[finding_code] — no matching catalogue question found. Needs new question in Stage 2b. Set finding status = 'pending' (unchanged).` Move to next finding. Do not formulate a new question here.

**Step 4:** Create the catalogue link.

Record in observations log: `[finding_code] — linking to [question_code] ([question_text truncated to 60 chars]). Coverage: [FULL/PARTIAL]. Add to Type (a) patch: insert wa_finding_catalogue_links row.`

Set finding `status = 'in_review'` in the Type (a) patch.

**Link record fields:**
- `finding_id` = this finding's `id`
- `question_id` = matched question's `obs_id`
- `coverage` = FULL or PARTIAL
- `status` = 'suggested'
- `mapped_date` = today's date
- `validated_by` = 'Session B Stage 1 Step 1.3b'
- `session_b_note` = one sentence stating why this question matches this finding

**Action 5 — Record sign-off in observations log:**

`Step 1.3b complete. Findings reviewed: [total]. Already linked: [n]. Linked in this step: [n]. Needing new question (Stage 2b): [n]. Closed as invalid: [n]. All active findings have status set.`

**Integrity check before proceeding:** Every active finding (delete_flag = 0) must now have either (a) a catalogue link with status = 'suggested' or 'validated', or (b) an observations log entry stating it needs a new question in Stage 2b. No finding may be left in status = 'pending' with no recorded disposition. If any finding has no link and no Stage 2b note, return to that finding and complete its assessment before proceeding.

Proceed to Step 1.3c.

---

#### Step 1.3c — `wa_session_research_flags`: Clear All B-Target Flags

**Purpose:** Identify all `wa_session_research_flags` rows for this registry that require resolution before Session B can close. These are flags with `session_target = 'B'` and `resolved = 0`. Each must reach a confirmed resolution in this step. Zero open B-target flags is the hard gate for Stage 1 completion.

**Session D flags** (`session_target = 'D'`) require no action in Step 1.3c. They are noted in Stage 2a as part of reading all data. They are not reviewed or resolved here.

**Action 1 — Request data from CC:**

Request from CC: return all rows from `wa_session_research_flags` where `registry_id = [nnn]` AND `session_target = 'B'` AND `resolved = 0`. Include all fields.

**Action 2 — If zero rows returned:**

Record in observations log: `Step 1.3c: wa_session_research_flags — 0 B-target flags for registry [nnn]. Hard gate: PASS.`

Proceed to RESEARCHER_DECISION block.

**Action 3 — If rows returned, resolve each flag:**

Work through each flag one at a time. For each flag:

**Step 1:** Record the flag in the observations log: `Flag [flag_label] — code: [flag_code], priority: [priority]. Description: [description].`

**Step 2:** Identify the resolution type. Apply exactly one of the four resolution types below. Do not leave a flag without a resolution type.

---

**Resolution type A — Data correction.**

Applies when: the flag identifies a specific data error that can be corrected from the extract — a term misclassified, a field incorrect, an extraction anomaly confirmed by the data.

Action:
1. Confirm the error is present in the current extract. State specifically: what is wrong, what the correct value is, and where in the data it is confirmed.
2. Add the correction to the Type (a) patch.
3. Record in observations log: `[flag_label] — Resolution type A (data correction). Correction: [specific correction]. Added to Type (a) patch. Mark resolved = 1, resolved_note = 'Data corrected: [summary]'.`
4. Add to Type (a) patch: `resolved = 1`, `resolved_date = [today]`, `resolved_note = 'Data corrected: [summary]'` on this flag row.

---

**Resolution type B — Research completed.**

Applies when: the flag asked a question that the current extract data now answers. The question is answerable from the data without further analytical work beyond reading what is in the extract.

Action:
1. State the answer drawn from the extract data. Be specific — cite the term, group, or verse that provides the answer.
2. Record in observations log: `[flag_label] — Resolution type B (research completed). Answer: [specific answer from extract data]. Mark resolved = 1, resolved_note = '[answer]'.`
3. Add to Type (a) patch: `resolved = 1`, `resolved_date = [today]`, `resolved_note = '[answer]'` on this flag row.

---

**Resolution type C — Convert to Session D pointer.**

Applies when: the flag describes a cross-registry question or connection that cannot be resolved within this registry — it requires Session D synthesis. This type also applies when the flag was incorrectly assigned `session_target = 'B'` and is more properly a Session D matter.

Action:
1. Confirm this flag's content is genuinely cross-registry or post-word-study in nature.
2. Check whether an SD_POINTER already exists in `wa_session_research_flags` for this registry that covers the same content. If one exists, do not create a duplicate — simply close the B-target flag with a reference to the existing SD_POINTER.
3. If no equivalent SD_POINTER exists: note in observations log that a new SD_POINTER will be created in Stage 2b when SD pointer patching occurs. Do not create it here.
4. Record in observations log: `[flag_label] — Resolution type C (convert to Session D). [Either: existing SD_POINTER [label] covers this content] or [New SD_POINTER to be created in Stage 2b]. Mark resolved = 1, resolved_note = 'Session D matter: [summary]. [Covered by SD_POINTER [label]] or [SD_POINTER to be created in Stage 2b]'.`
5. Add to Type (a) patch: `resolved = 1`, `resolved_date = [today]`, `resolved_note = '[note]'` on this flag row.

---

**Resolution type D — RESEARCHER_DECISION required.**

Applies when: the flag describes a genuine decision that cannot be resolved by reading the extract, is not a cross-registry matter, and requires researcher input. This is a last resort. Before applying resolution type D, confirm that types A, B, and C have been genuinely considered and ruled out with stated reasons.

Action:
1. Record in observations log: `[flag_label] — cannot resolve in Stage 1. Type A ruled out: [reason]. Type B ruled out: [reason]. Type C ruled out: [reason]. Adding to RESEARCHER_DECISION block.`
2. Add to the RESEARCHER_DECISION accumulator — the item will be presented in the RD block after Step 1.3c.
3. Do not mark the flag resolved yet. It will be resolved after the researcher decision is received.

---

**Action 4 — Verify all flags are resolved.**

After working through all rows, count: how many flags were processed, how many reached resolution types A, B, or C, how many are in the RESEARCHER_DECISION accumulator.

Flags in the RESEARCHER_DECISION accumulator are NOT yet resolved — they will be resolved after researcher decisions are received. This is acceptable at this stage. The hard gate (zero open B-target flags) applies at Step 1.4 patch application — after all RD items are resolved.

**Action 5 — Record sign-off in observations log:**

`Step 1.3c complete. B-target flags reviewed: [total]. Resolved type A (data correction): [n]. Resolved type B (research completed): [n]. Resolved type C (Session D): [n]. Awaiting researcher decision (type D): [n].`

If type D count is zero: `Hard gate: PASS — [n] B-target flags resolved. Zero remaining.`

If type D count is greater than zero: `Hard gate: PENDING — [n] flags awaiting researcher decision. Gate will be confirmed after RD block is resolved.`

Proceed to RESEARCHER_DECISION block.

---

### RESEARCHER_DECISION Block — Stage 1

Collect all items that could not be resolved analytically across Steps 1.3a, 1.3b, and 1.3c. Present as a discrete numbered block before proceeding to patch construction.

Format per GR-RD-002. Each item must contain:
- **RD-ID** — sequential number (RD-S1-001, RD-S1-002, etc.)
- **Source step** — which sub-step generated this item
- **What was checked** — the specific flag, finding, or field examined
- **Why resolution was not possible** — what was tried and why it did not resolve
- **The question** — stated precisely and unambiguously
- **Options with consequences** — at least two options, each with its specific outcome
- **Claude AI's recommendation** — one option, stated with reasoning

**If zero items:** Record `No RESEARCHER_DECISION items from Stage 1.` Proceed to Step 1.4.

**If items present:** Present the block. Do not begin Step 1.4 until every item is resolved. The researcher responds by RD-ID. Each response produces a concrete outcome: a correction noted for the patch, a patch item added, a direction confirmed, or a flag marked for resolution type C. Record each response and its outcome in the observations log.

When all RD items are resolved, confirm in observations log: `All Stage 1 RESEARCHER_DECISION items resolved. Proceeding to Step 1.4.`

---

### Step 1.4 — Type (a) Patch Construction and Application

Compile all data quality corrections identified across Steps 1.2, 1.3a, 1.3b, and 1.3c into a single Type (a) patch. These are data corrections — not analytical findings.

**Items that generate Type (a) patch operations:**

| Source | Operation |
|--------|-----------|
| Step 1.2 gaps | Missing or incorrect field values on `word_registry`, `wa_term_inventory`, or `mti_terms` |
| Step 1.2 gaps | Verse context or dimension gaps correctable by a field patch (not requiring a sub-process) |
| Step 1.3a rejected flags | `wa_term_phase2_flags`: `delete_flagged = 1`, `obsolete_reason` for each rejected or irrelevant flag |
| Step 1.3b finding status updates | `wa_session_b_findings`: `status = 'in_review'` for findings linked to a catalogue question |
| Step 1.3b invalid findings | `wa_session_b_findings`: `delete_flag = 1`, `obsolete_reason`, `status = 'complete'` for invalid findings |
| Step 1.3b catalogue links | `wa_finding_catalogue_links`: new INSERT rows for each new finding-question link |
| Step 1.3c resolved flags | `wa_session_research_flags`: `resolved = 1`, `resolved_date`, `resolved_note` for each resolved B-target flag |
| Stage 1 RD items resolved | Any correction or field update arising from researcher decisions |

**Construction rules:**

1. List all patch operations in the observations log before constructing the patch JSON. State each operation: table, field(s), value(s), and the step that generated it.
2. Construct the patch per the patch instruction (`wa-patch-instruction [current]`).
3. Name the patch file: `wa-[nnn]-[word]-patch-preanalysis-v1-[YYYYMMDD].json` (per GR-FILE-001/007/009). The internal `patch_id` in `_patch_meta` follows the format `PATCH-[YYYYMMDD]-[nnn]-PREANALYSIS-V1` for applicator compatibility — do not confuse filename with patch_id.
4. State patch contents in the observations log: `Stage 1 Type (a) patch constructed. [n] operations covering: [brief list of operation types].`

**Format compliance check — mandatory before submission:**

Per GR-DIR-006: run the six-point self-check against the patch specification before presenting the patch for researcher approval. Record the result in the observations log as `Patch format compliance check: [PASS / FAIL — detail if FAIL]`. Do not submit a patch that fails any point.

**Submission and confirmation:**

Present the patch to the researcher for approval. Do not submit to CC without explicit researcher approval.

After researcher approval: submit to CC for application. Wait for CC confirmation.

Review the confirmation against the expected outcomes. For each operation, confirm the expected field value is now present. If any operation failed or produced an unexpected result, raise a corrective directive before proceeding — do not proceed with a partially applied patch.

Record in observations log: `Stage 1 Type (a) patch applied and confirmed. [n] operations. Confirmation reviewed — [outcome: all expected values confirmed / anomalies noted as: (detail)].`

**B-target flag hard gate verification:**

After the patch is confirmed, request from CC: return count of `wa_session_research_flags` rows for registry [nnn] where `session_target = 'B'` AND `resolved = 0`.

- Count = 0: Record `B-target flag hard gate: CONFIRMED. Zero open B-target flags.` Proceed.
- Count > 0: STOP. One or more B-target flags remain unresolved. Identify which flags were not closed by the patch and resolve them before proceeding. Do not proceed to Step 1.5 until this count is zero.


---

### Step 1.5 — Sub-Process Execution and Fresh Extract

#### Purpose

Step 1.5 executes all process re-run directives (Path 2 items) identified during Step 1.2, waits for each to complete, and then pulls the fresh extract. The fresh extract is the data that Stage 2 will work from — it must reflect all corrections made during Stage 1.

Step 1.5 does not begin until:
- The Type (a) patch from Step 1.4 is confirmed applied
- The B-target flag hard gate is confirmed (zero open B-target flags)
- All RESEARCHER_DECISION items are resolved

#### Sub-process triggers

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

#### Fresh extract

After all sub-process triggers are resolved and confirmed:

Request from CC: re-export the complete word data for registry [nnn] and return the new version identifier and export date.

This extract replaces the one used during Stage 1. All subsequent work in Step 1.6 and Stage 2 uses this extract.

Record in observations log: `Fresh extract confirmed: [filename] — version [n] — exported [date].`

Do not proceed to Step 1.6 until the fresh extract is confirmed.

---

### Step 1.6 — Stage 1 Completion Verification and Handoff

#### Purpose

Step 1.6 verifies that the fresh extract reflects all corrections made during Stage 1. It is not a re-run of the full Step 1.2 audit — it is a targeted verification of the specific items that were patched, directed, or sub-processed. It produces the Stage 1 Completion Record and declares Stage 2 readiness.

This step has three parts:
1. Targeted verification of corrections against the fresh extract
2. Stage 1 Completion Checklist
3. Stage 1 Completion Record and Stage 2 readiness declaration

#### Part 1 — Targeted verification against fresh extract

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

#### Part 2 — Stage 1 Completion Checklist

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

#### Part 3 — Stage 1 Completion Record and Stage 2 Readiness Declaration

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

---

## Integrity Rules

The following integrity rules govern Analysis Readiness. Rules SB-18 through SB-24 supersede the corresponding rules in v5.0.

| Rule | Status | Text |
|------|--------|------|
| SB-1 | Updated | Stage 2 does not begin until Stage 1 is fully complete: all steps executed; all Path 1/2/4 items resolved; all 7 domains of the Stage 1 Completion Checklist passing; fresh extract confirmed; Stage 2 Readiness Declaration made. |
| SB-18 | Updated | Zero `wa_session_research_flags` rows for this registry with `session_target = 'B'` and `resolved = 0` — confirmed by CC count query after Step 1.4 patch application and re-confirmed in Step 1.6 Domain 5 checklist. |
| SB-19 | Unchanged | No RESEARCHER_DECISION item may be raised without evidence that GR-RD-001 steps 1–6 have been completed. |
| SB-20 | New | Every active `wa_session_b_findings` row for this registry must have either (a) a `wa_finding_catalogue_links` row with `status` in ('suggested', 'validated') or (b) an observations log entry confirming it needs a new question in Stage 2b — before Step 1.4 patch construction begins. |
| SB-21 | New | Analysis Readiness does not perform analysis. Any step that requires analytical judgement must be deferred to Analysis Output. Record what was deferred and why in the observations log. |
| SB-22 | New | Stage 1 does not close without a Stage 1 Completion Record in the observations log. The record must contain the summary for all steps 1.1–1.6, resolution counts for all four paths, and the Stage 2 Readiness Declaration. |
| SB-23 | New | Analysis Output works from the fresh extract confirmed in Step 1.5. If any data question arises during Analysis Output about a field value or count, the extract version in the Stage 1 Completion Record is the authoritative reference. |
| SB-24 | New | A Path 2 process directive is not complete until CC has confirmed execution AND the targeted terms or groups have been verified in the updated extract. The fresh extract is not pulled until all Path 2 confirmations are in hand. |

---

*wa-sessionb-analysis-readiness-v1_6-20260418.md*
*Framework B — Soul Word Analysis Programme*
*Supersedes wa-global-sessionb-instruction-v5_0-20260415.md (Stage 1)*
*Paired with wa-sessionb-analysis-output-v1-[date].md (Stage 2)*
