# WA-SessionB-Instruction-v5.0-20260414

**Framework B — Soul Word Analysis Programme
Session B Instruction — Data Audit, Remediation, Analysis, and Database Completion
Version 5.0 | 20260414 | Status: Draft — under review**

| **Document** | **Value** |
|---|---|
| Filename | wa-global-sessionb-instruction-v5.0-20260414.md |
| Supersedes | wa-sessionb-instruction-v4.8-20260414.md |
| Companion documents | wa-global-general-rules-v2.1-20260414.json │ wa-dimensionreview-instruction-v3.1-20260414.md │ wa-versecontext-instruction-v2.7-20260414.md │ wa-sessionb-cc-instructions-v3.3-20260414.md │ wa-patch-specification-v1.11-20260414.md │ wa-sessionc-instruction-[current] │ wa-sessiond-orientation-v3.0-20260412.md |
| Inputs | Complete word data export: wa-[nnn]-[word]-complete-[date].json |
| Outputs | See Section 5 — What This Session Produces |
| Claude AI role | Data audit, analytical passes, outcome recording, checklist verification, handoff |
| Claude Code role | Patch application, sub-process execution, extract production, integrity validation |

---

## Governing Rules

This instruction is governed by **wa-global-general-rules-v2.1-20260414.json**.

Claude AI must confirm the global rules file has been loaded before beginning any work in this session. State aloud: *"Global rules wa-global-general-rules-v2.1-20260414.json loaded."*

Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.

---

## Change Log

**v5.0 (20260414):** Complete redesign of the Session B–Session C relationship and closure architecture.

The fundamental change: Session B is now a complete-before-publish gate. The word study (Session C) is generated after Session B is fully closed and the database is verified. Session B no longer validates or updates a word study — it prepares the database so that Session C can write the word study with confidence.

Principal changes from v4.8:

1. **Pipeline corrected.** Session C no longer precedes Session B. The pipeline is now: Session A → Verse Context → Dimension Review → Session B → Session C → Session D.

2. **Stage 3 and Stage 3b removed.** Session C validation, word study updating, and publication review are no longer part of Session B. Session B ends with a handoff signal that opens Session C.

3. **Analytical Brief redefined.** The Analytical Brief is a dual-purpose handoff document: (a) to Session C — confirming that all database components are articulated and updated, enabling Session C to write the word study from the database; (b) to Session D — the structured SD pointer summary for cross-registry synthesis. It is not a mini word study.

4. **All observations return to the database.** The observations log is a working log only. Every finding, decision, and analytical outcome must be persisted to the appropriate database table via a Type (a) or Type (b) patch or directive before Session B closes. Session C and Session D read from the database, not the observations log.

5. **Two types of database writes formalised.** Type (a): data quality patches — making the input data complete, correct, and reliable. Type (b): analytical outcome patches — recording the results of the six analytical passes as structured database records.

6. **Each pass now closes with a confirmed database write.** Every analytical pass ends with a patch or directive to persist its outcomes before the next pass begins. Per GR-PASS-002.

7. **Session B Closure Checklist introduced.** A new mandatory output. A structured checklist run by Claude AI against a fresh database extract, confirming that every required element is present, correctly formed, and signed off. This is Claude AI's accountability instrument. The researcher does spot checks only.

8. **Corrective action loop formalised.** Checklist discrepancies trigger a corrective action process that may range from a field patch to re-running sub-processes to introducing a new word into the registry and re-running Session B in full.

9. **Schema gap register introduced.** Session B v5.0 identifies and resolves all analytical outcome schema requirements before any Session B analytical work proceeds. The gap register is a companion document to this instruction.

*Prior version history (v1.0–v4.8): see wa-sessionb-instruction-v4.8-20260414.md.*

---

## 1. Purpose and Scope

Session B is the analytical quality gate for each word in the programme. It operates on a single word per run. It does not advance until the word is complete in three respects:

**1. Data complete and reliable.** Every field in the registry is correctly populated. Every data gap has been identified, patched, and confirmed. Verse context is sound. Dimension data has reached `CLAUDE_AI` confidence. Correlation signals can fire correctly from the clean data. No analytical work begins on unreliable data.

**2. Analysis complete and recorded.** A rigorous six-pass analysis has been conducted against the clean data. The findings from every pass — meaning synthesis, divine dimension pattern, verse annotations, somatic evidence, language accuracy, and correlation audit — are persisted to the database as structured records. The observations log is a working document only; it has no standing in Session C or Session D.

**3. Database complete and verified.** All analytical outcomes from the six passes are recorded in the appropriate database tables. SD pointers are in the database. All Session B flags are resolved. The Closure Checklist has been run against a fresh extract and passed clean. The Analytical Brief confirms readiness for Session C and Session D.

**What Session B does:**
- Audits the complete word data and identifies all gaps
- Triggers and oversees Verse Context and Dimension Review sub-processes where required
- Conducts six analytical passes against the clean, complete data
- Persists all analytical outcomes to the database via Type (a) and Type (b) patches
- Raises and persists all Session D pointers
- Runs the Closure Checklist against the verified database
- Produces the Analytical Brief as handoff to Session C and Session D
- Advances `session_b_status` to `Analysis Complete`

**What Session B does not do:**
- Write the word study — that is Session C
- Draw cross-registry synthesis conclusions — that is Session D
- Leave analytical findings only in the observations log — all findings must reach the database
- Close until the Closure Checklist is clean

**Session B is multi-session.** A single session may cover only part of one stage. The session log is the continuous record across all sessions for this word.

---

## 2. Pipeline Position

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
Session B  (this instruction — multi-session operation)
     ├── Stage 1: Data audit and remediation
     │     ├── Read complete JSON → identify all gaps
     │     ├── Type (a) patches: field-level corrections
     │     ├── Verse Context sub-process (if triggered)
     │     ├── Dimension Review sub-process (if triggered)
     │     └── Fresh extract: Claude Code re-exports clean JSON
     ├── Stage 2: Analytical passes (six passes against clean data)
     │     ├── Pass 1: Meaning and semantic range
     │     ├── Pass 2: Divine dimension
     │     ├── Pass 3: Verse annotations
     │     ├── Pass 4: Somatic evidence and spirit-soul-body classification
     │     ├── Pass 5: Language accuracy
     │     └── Pass 6: Correlation audit and connection verification
     │     [Each pass closes with confirmed Type (b) database write]
     ├── Section 2.1: Analytical Brief
     ├── Section 2.2: SD Pointer Persistence
     └── Stage 3: Closure
           ├── Fresh extract
           ├── Closure Checklist (all domains verified)
           ├── Corrective action loop (if checklist fails)
           ├── Closing patch → session_b_status = Analysis Complete
           └── Handoff signal → Session C and Session D
     │
     ▼
Session C  (word study production — from database)
     │
     ▼
Session D  (cross-registry synthesis — from database + SD pointers)
```

---

## 3. What to Attach at Session Start

- This instruction file
- Global rules file: `wa-global-general-rules-v2.1-20260414.json`
- The complete word data export: `wa-[nnn]-[word]-complete-[date].json`
- CC instructions: `wa-sessionb-cc-instructions-v3.3-20260414.md`

Sub-process instruction documents are attached only when the sub-process is triggered:
- Verse Context sub-process: `wa-versecontext-instruction-v2.7-20260414.md`
- Dimension Review sub-process: `wa-dimensionreview-instruction-v3.1-20260414.md`

Do not load more data into the working session than the current step requires.

---

## 4. Governing Disciplines

These disciplines apply without exception across all stages, all passes, and all sessions. All are governed by the global rules file.

**Step-by-step.** Per GR-PROC-001 (non-waivable). Each step is completed and confirmed before the next begins. A step that is partially complete is not complete.

**Write on discovery.** Per GR-OBS-001 (non-waivable). Every finding, decision, gap, patch consequence, flag, and open question is written to the observations log at the moment it is determined. Nothing is accumulated in memory.

**All observations return to the database.** The observations log is a working document. Every analytical finding must be persisted to the appropriate database table via a patch or directive before the session closes. Session C and Session D read from the database only.

**Data is authoritative.** Per GR-PROC-002. Work strictly from what is in the JSON. Do not import general knowledge to fill gaps.

**All changes through patches or directives.** Per GR-PROC-003 (non-waivable). Claude AI produces directives and patches. Claude Code executes them. Per GR-DIR-001, directives are in plain language.

**Two types of database writes.** Type (a) patches correct and complete the input data — making it reliable before analysis begins. Type (b) patches record the analytical outcomes of the six passes — the results Session B found. Both types are mandatory. Neither type substitutes for the other.

**Pass-close database write.** Per GR-PASS-002. Every analytical pass ends with a patch or directive to persist its outcomes to the database. A fresh extract is pulled confirming the write. The updated extract is the working source for the next pass.

**Pass-close download.** Per GR-PASS-001. All outputs produced during a pass are made available for download at pass close before the next pass begins.

**Session logs at every breakpoint.** Per GR-PROC-006. Record the current stage, the last completed step, and the next step.

**Cross-registry vision is always active.** Every piece of data read in Stage 2 is read twice: once for what it says about this word, and once for what it says about something beyond this word. Session D flags are raised continuously throughout all passes — not accumulated for Pass 6. Per Section 2.0a.

**Load only what is needed.** Do not load more data into the working session than the current step requires. Large registries are read section by section.

---

## 5. What This Session Produces

Two categories of database write are produced throughout Session B:

| Write type | Purpose | Stage |
|---|---|---|
| Type (a) patch | Data quality — correct, complete, and reliable input data | Stage 1 |
| Type (b) patch / directive | Analytical outcomes — structured records of what Session B found | Stage 2 passes |

The following documents are produced:

| Output | Stage | Type |
|---|---|---|
| Observations log | All stages | Working log — written continuously; all content must be persisted to database |
| Session log | All stages | Breakpoint summary — produced at every pause or end |
| Type (a) field-level patch(es) | Stage 1 | JSON patch(es) for data corrections |
| Claude Code directive(s) | Stage 1 | Plain-language instructions for CC operations |
| Verse Context sub-process outputs | Stage 1 (if triggered) | Per VC instruction |
| Dimension Review sub-process outputs | Stage 1 (if triggered) | Per DR instruction |
| Clean complete JSON | Stage 1 end | Re-exported by Claude Code after all Stage 1 patches confirmed |
| Type (b) pass outcome patches / directives | Stage 2 — per pass | Analytical findings persisted to database at each pass close |
| Analytical Brief | Stage 2 end | Dual handoff: Session C readiness confirmation + Session D SD pointer summary |
| SD pointer patch | Section 2.2 | SD_POINTER records in wa_session_research_flags |
| Closure Checklist | Stage 3 | Verified checklist against fresh extract — all domains signed off |
| Closing patch | Stage 3 | session_b_status → Analysis Complete |
| Handoff signal | Stage 3 end | Opens Session C; notifies Session D queue |

---

*[End of landscape sections — Sections 1–5. Stages, passes, checklist, principles, integrity rules, and naming conventions follow.]*

