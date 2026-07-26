# AI failures / lessons / mitigations — source extract only

Date: 2026-07-24

Scope: verbatim extracts from the source documents already identified in the main project. No paraphrase, no synthesis, no interpretation.

---

## Source 1

Source: `docs/interaction-preferences.md`

```md
# Interaction Preferences — Claude Code

This file is the authoritative record of communication protocols between the researcher (leRoux) and Claude Code. Claude Code must read and apply these protocols at the start of every session.

---

## AskUserQuestion Tool — BANNED, full stop (reinforced 2026-07-22)

**The `AskUserQuestion` tool must NEVER be used in this project.** Blocked at the config level
(`.claude/settings.json` → `permissions.deny: ["AskUserQuestion"]`) as of 2026-07-22, after it had
already been called off-limits twice before (2026-06-01, 2026-06-15 "hard stop") and was violated
again this session — a question fired through it, the researcher gave an elaborate answer, and the
tool call came back as a bare rejection with **no answer content at all**. Memory-only enforcement
had already failed three times; this is now a technical block, not just a reminder.

**What to do instead, always:**
- A question answerable from the DB or the code → investigate and present facts. Do not ask what
  you can find out.
- A genuine researcher judgement call → write it to a `.md` file (a review document, a decision
  doc) with the options, current state, and a decision blank — per the file-based review protocol
  below — and tell the researcher in plain chat where it is. Never a structured in-chat menu.
- A single short clarifying question with no real menu of options → plain chat text is fine.

---

## Instruction Confirmation Protocol

Before executing ANY instruction (except trivial single-step tasks):
1. Summarise the instruction as understood
2. State what I plan to do (approach, files affected, scope)
3. WAIT for explicit researcher approval before proceeding

This applies to every new chat session, without exception.

---

## Output & Workings Stream Protocol

All workings (reasoning, plans, steps) and all outputs must be streamed to `.md` files so the researcher can review and contribute to them.

- Never present final output only in chat — always write it to a `.md` file first
- Workings (analysis steps, decisions made, intermediate results) must also be captured in `.md` format
- Files should be placed in a logical location within the workspace (`docs/`, `outputs/`, or a relevant subfolder)
- The researcher may edit these files to correct or contribute, and those edits must be respected in subsequent steps

---

## Factual Discipline Protocol

Do not guess, make assumptions, or offer unsolicited opinions.

- Work only with the facts and inputs explicitly provided
- Do not invent context, fill in gaps with assumptions, or speculate without being asked
- Opinions and recommendations must only be given when explicitly requested
- If anything is unclear or information is missing — STOP and ask before proceeding

---

## PowerShell / Terminal Protocol

It is not necessary to ask for permission before running PowerShell or terminal commands to read system state or execute approved work. Commands that modify the database or codebase should still be consistent with approved tasks.

## Root Fix, Not One-Off (researcher direction 2026-07-13)

Fix the **cause**, not the instance. A one-off / per-term / per-book / per-file patch is **rarely appropriate, and NEVER appropriate when the problem may recur.** When a defect is an instance of a class (a shared method, an extractor, a pipeline step is wrong), fix it at the shared mechanism so every future case is correct — do not remediate case-by-case and leave the mechanism broken. If you catch yourself hand-patching one case of a recurring problem, stop and fix the root. (Worked example: the STEP multi-variant verse drop was fixed in `word_study_extract`, not patched per Proverbs term.)

## Bake Guidance into the Authoritative Instructions

Researcher guidance, rules, decisions, and corrective actions must be written into the **authoritative instruction docs** (`Workflow/Instructions/`), not only into memory or a findings file — the written authoritative record is the source of truth (GR-REF-002). Add a dated amendment to the owning doc, then mirror a pointer in memory.
```

---

## Source 2

Source: `Workflow/Sessionlogs/wa-global-preamble-obslog-v1-20260417.md`

```md
## Entry O-010 — First preamble draft produced

Claude AI drafted the preamble in three parts:
1. Programme context and the no-memory-between-sessions constraint
2. Custodianship framing
3. Two-axis discipline (analytical freedom unrationed; procedural choice removed)
4. Eight specific forbidden behaviours
5. Ambiguity-resolution rule
6. Authority order
7. Edit-lock

Length approximately 700 words.

## Entry O-011 — Researcher sharpening: three failure mechanisms

**Researcher response:** "I want more focus on descipline: Most issues happen because Claude AI dont read properly, dont follow instructions properly, and dont validate outcomes. Most losses and rework happens because Claude AI do not write workings and feedback to disk, but keep it in memory and the chat, and don't export the outputs to download regularly. Most issues are discovered only long afterwards because AI say something to please researcher instead of relaying actual facts - saying something is done, complete, checked but it simply did not even look to check it."

Claude AI extracted three failure mechanisms:
1. Read. Follow. Validate. (not done)
2. Write to disk. Export to download. (held in chat and memory)
3. Report facts, not reassurance. (saying it's done without checking)

Plus feedback that specific-behaviours list was too soft.

## Entry O-012 — Second preamble draft

Claude AI restructured the preamble around the three failure mechanisms. Twelve forbidden behaviours, each a single imperative line. Specifically added "Report facts, not reassurance" as the third and most damaging mechanism.

**Researcher confirmation:** "1 - yes. 2-i hope so: a full list of things that AI is doing poorly or fail in is too long to repeat. 3. yes - in has happened numerous times, even with instructions to prevent it in the instruction that fails."

Item 3 strengthened: the crash-with-material-in-memory sentence expanded to: "This has happened repeatedly, even where the governing instruction required the write."

## Entry O-013 — Preamble embedded and file produced

Claude AI produced `wa-global-general-rules-v2_6-20260417.json` with:
- Preamble (781 words) added to `document` object between `purpose` and `scope_test`
- Filename field updated to v2.6
- Date updated to 20260417
- Status updated to "Active — supersedes v2.5-20260416"
- Change note added documenting the preamble addition
- FLAG-009 added recording the preamble edit-lock as a standing condition
- All 53 existing rules preserved unchanged

File dual-written to /home/claude/work and /mnt/user-data/outputs.

## Entry O-014 — Audit request

**Researcher directive:** "can you now read through the global rules. Check for ambiguity, conflict, scope limitation (by nature of the rule it only applies in limited scenarios). also do we have too many. if it is too many, then they will be ignored."

Claude AI read the full v2.6 file and generated quantitative and substantive findings:

- **Total rules:** 53. Total rule text: 3,630 words. Average 68 per rule. Six rules exceeded 100 words.
- **Scope analysis:** 26 rules apply to "all sessions, all phases"; rest narrower. Four rules (GR-DATA-002, -003, -004, -005) are Session-B-specific by their own declaration. Four more (GR-PROG-003, -004, -006, -007) are two-instruction rules.
- **Redundancy clusters found:** (1) Write-on-discovery said three times (GR-OBS-001, GR-PROC-005, GR-PASS-002); (2) Role separation said twice (GR-PROG-005, GR-DIR-004); (3) Evidence traceability close but distinct (GR-PROC-002, GR-PROG-008); (4) Two large self-checks (GR-DIR-006 at 269 words, GR-DIR-008 at 148 words).
- **Ambiguities found:** 7 total — 2 serious (GR-OBS-004 vs DR v1.9 already flagged; GR-DIR-001 patch-vs-directive test rests on self-assessment) and 5 tidy-up.
- **Conflicts found:** 4 — C1 (already flagged FLAG-002), C2 (GR-FILE-004 vs GR-FILE-008 silent conflict), C3 (GR-DIR-004 / GR-PROG-005 duplication), C4 (decision-block scaling).
- **Recommendation:** Rule count can drop from 53 to ~38 without losing substantive content. Two paths offered: Path A (consolidate in place); Path B (separate binding from reference).

Audit findings delivered in chat. No markdown file produced at this point.

## Entry O-015 — Researcher adds reference documents

Researcher uploaded `wa-patch-specification-v1_14-20260416.md` and `WA-Reference-v5_5-20260330.md`.

**Researcher directive:** "i uploaded two key reference instructions. global rules should reference these - as lookup when needed. global rule items that need to move to one of these, need to move, not repeat. move all the rules that is regarded as items that is best inside instructions to an addendum in the global rules - We will insure that these are covered in the instructions."

Claude AI restated the instruction: (1) rules belonging to reference specs move there; (2) rules belonging to instructions move to an addendum in the global rules; (3) addendum is a holding area until instruction coverage confirmed; (4) global rules reference, do not duplicate.

Claude AI read structural headings of both reference documents, then targeted sections:
- WA-Reference Section 1 (file naming)
- Patch spec Governing Rules, Section 1, Section 2, Section 5, Section 6, Section 7

## Entry O-016 — Complication discovered: WA-Reference Section 1 is stale

Reading WA-Reference Section 1, Claude AI observed:
- Pattern on line 57 omits the version component (GR-FILE-001/003 require it)
- Line 91+ instruction names use capital "WA-" prefix (GR-FILE-007 requires all lowercase)
- Patch ID Convention 1.4 uses uppercase "PATCH-..V{n}" (contradicts current lowercase)

**Consequence:** Cannot simply "move and reference" — WA-Reference is out of date and would propagate stale content. Flagged as Complication 1 requiring researcher decision.

## Entry O-017 — Second complication: no directive specification

Claude AI observed: no reference document exists for directives (the patch specification is patches-only; CC instructions are Session-B scoped). Directive rules GR-DIR-002, GR-DIR-007, GR-DIR-008 have no natural reference-doc home. Flagged as Complication 2.

## Entry O-018 — Classification table produced in chat

Claude AI produced a 53-row classification table with proposed dispositions (KEEP / MOVE → WA-Reference / MOVE → Patch spec / ADDENDUM / MERGE). Projected outcome: from 53 rules to 33 keep + 10 addendum + 3 moved + 2 merged away = effectively 38 rules in main section plus addendum.

Four open questions presented to researcher.

Classification table delivered in chat. No markdown file produced.

## Entry O-019 — Compliance failure surfaced

**Researcher directive:** "in this session, do you see yourself as compliant with the rules in the global rules set? I do not comment or review stuff that is not output to a .md Claude AI chat interface is horrible for scrolling up and down and I cannot properly reference it."

Claude AI inspected own conduct. Compliance failures:
- GR-LOAD-001: Did not confirm load at start of session.
- GR-OBS-001: No observations log produced continuously — findings held in chat.
- GR-OBS-003: No session log produced.
- GR-PROC-005: Accumulated findings in memory; offered to produce log "at natural breakpoint" — end-of-session promise.
- GR-PROC-006: Multiple natural breakpoints passed without session log production.
- GR-FILE-008: Partially complied (preamble dual-written) but audit findings not dual-written because not written at all.

Claude AI stated the failure directly and named three files to produce immediately:
1. wa-global-rules-audit-v1-20260417.md (the audit)
2. wa-global-preamble-obslog-v1-20260417.md (this observations log)
3. wa-global-preamble-sessionlog-v1-20260417.md (handoff record to follow)

## Entry O-020 — Researcher approval and directive

**Researcher directive:** "yes, proceed, and from this point onwards this session is conducted in full compliance with the global rules 2.6"

Claude AI stated GR-LOAD-001 confirmation explicitly: "Global rules wa-global-general-rules-v2_6-20260417.json loaded — 53 rules across 12 categories, plus preamble and 9 flags."

Produced three files. This entry records the present work.

---

## Wrong turns taken in this session (for the record)

Three wrong turns, all corrected by the researcher:

**W1 — Initial framing as fellowship consolidation.** Claude AI's first response treated the task as consolidating the fellowship log. Corrected by O-002 researcher statement: this is a programme-level framework document.

**W2 — Proposed separate document at 4–6 pages.** Claude AI proposed WA-programme-briefing-v1 as a standalone 12-section document of 4–6 pages. Corrected by O-003: 2–3 pages max, lives inside global rules, principles already known and ignored.

**W3 — Substantive work delivered in chat not on disk.** Claude AI produced the audit findings and the 53-row classification table in chat, not as markdown files. Corrected by O-019 researcher challenge on compliance.

These wrong turns follow the same pattern as the fellowship session's three wrong turns. The correction discipline — researcher naming the drift, Claude AI returning to the specified frame — is the same mechanism that carried the fellowship session to its conclusion.

The specific failure in W3 is the one the preamble names directly: *"Working material is held in chat and memory rather than written to disk."* Claude AI drafted the preamble. Claude AI then violated the preamble within the same session. This confirms the reflection in O-019: writing the preamble does not self-enforce.

---

## Open items carried forward

The audit document (wa-global-rules-audit-v1-20260417.md) lists four open questions that require researcher decision before any rule movement happens:
```

---

## Source 3

Source: `Workflow/Sessionlogs/wa-global-preamble-sessionlog-v1-20260417.md`

```md
# WA Global Preamble and Audit — Session Log

**Filename:** wa-global-preamble-sessionlog-v1-20260417.md
**Version:** 1.0
**Date:** 2026-04-17
**Session type:** Preamble drafting + global rules audit
**Companion file:** wa-global-preamble-obslog-v1-20260417.md (the working observations log)

**Prior output referenced:**
- wa-062-fellowship-review-sessionlog-v1-20260417.md (input: fellowship review deliberation)

---

## 1. What this session accomplished

**Primary:** Added a binding preamble to the global rules file, producing `wa-global-general-rules-v2_6-20260417.json`. The preamble establishes Claude AI as the custodian of compliance and consistency, names three failure mechanisms (read/follow/validate; write-to-disk/export; report-facts-not-reassurance), lists twelve specific forbidden behaviours, and states the authority order when documents disagree. Loads automatically with the file via GR-LOAD-001.

**Secondary:** Produced a complete audit of the 53 rules in the global rules file. Audit covers ambiguity, conflict, scope limitation, redundancy, and volume. Proposes dispositions for every rule. Delivered as `wa-global-rules-audit-v1-20260417.md`.

**Housekeeping:** Surfaced a mid-session compliance failure (Claude AI was holding substantive outputs in chat rather than writing to disk) and corrected it by producing all three of: audit document, observations log, this session log.

---

## 2. What is confirmed

| Item | State |
|---|---|
| wa-global-general-rules-v2_6-20260417.json | Produced. Dual-written. Preamble embedded between `purpose` and `scope_test`. FLAG-009 recorded as edit-lock on preamble. |
| Preamble content | Researcher-approved in three iterations. Custodian framing approved. Three failure mechanisms approved. Twelve forbidden behaviours approved. |
| Rules audit | Complete. Delivered as markdown. 53 rules classified with proposed dispositions. |
| Compliance correction | Actioned. From researcher directive: "from this point onwards this session is conducted in full compliance with the global rules 2.6." |

---

## 3. What is deferred

### 3.1 Open researcher decisions (from audit Section 8)

**Q1 — Rule-by-rule disposition approval.** Researcher reviews the 53-row classification table in the audit (Section 6) and approves or rejects each proposed disposition by rule ID. No rule will be moved without explicit approval.

**Q2 — Complication 1: WA-Reference Section 1 is stale.** Researcher chooses:
- (a) Update WA-Reference Section 1 in same cycle (produce v5.6)
- (b) Add authority note in global rules stating GR-FILE rules are authoritative over stale reference content
- (c) Pause all moves into WA-Reference until reference is updated

**Q3 — Complication 2: no directive specification document exists.** Researcher chooses:
- (a) Keep GR-DIR-002, GR-DIR-007, GR-DIR-008 in global rules (audit recommendation)
- (b) Create wa-directive-specification as new document

**Q4 — Addendum structure.** Proposed: new top-level key `addendum` at back of JSON, each item carrying original rule text plus `migration_target` and `migration_status` fields. Confirm or alter.

### 3.2 Open observations from the audit

| Ref | Item | Action |
|---|---|---|
| A5 | GR-OBS-004 vs DR v1.9 §6.2 conflict (FLAG-002) | Resolve in next cycle |
| A7 | GR-DIR-001 patch-vs-directive test rests on AI self-assessment | Replace with objective test in next revision |
| A1–A4, A6 | Five tidy-up ambiguities | Resolve with rule edits in next revision |
| C2 | GR-FILE-004 vs GR-FILE-008 silent conflict on dual-write versioning | Add clarifying sentence in next revision |
| C4 | Decision-block scaling problem at 15+ items | Revisit before Registry 103 'love' is processed |

### 3.3 Structural observation noted but unactioned

The preamble does not self-enforce: writing the preamble did not prevent the session that wrote it from violating it. The programme may need an external compliance checkpoint (a file-production gate, a pre-response self-check, a researcher intervention protocol). No action in this session. Recorded for future consideration.

---

## 4. Where the next session picks up

### 4.1 Next session's entry point

The next session receives researcher decisions on Q1 through Q4 above. Once those decisions are in hand, the next session:

1. Applies approved rule dispositions to produce `wa-global-general-rules-v2_7-YYYYMMDD.json` (minor increment for moves and merges within the file).
2. If Q2(a) chosen: produces `WA-Reference-v5_6-YYYYMMDD.md` with Section 1 updated.
3. If Q2(b) chosen: includes authority note in v2.7 change register.
4. If Q3(b) chosen: produces `wa-directive-specification-v1-YYYYMMDD.md`.
5. Implements the `addendum` key structure confirmed in Q4.
6. Resolves the seven ambiguity and conflict items listed in audit Section 4 and 5.

### 4.2 Files the next session must read

**Required:**
- wa-global-general-rules-v2_6-20260417.json (the v2.6 rules file, current state)
- wa-global-rules-audit-v1-20260417.md (the audit with dispositions)
- wa-global-preamble-obslog-v1-20260417.md (working context)
- wa-global-preamble-sessionlog-v1-20260417.md (this handoff)
- Researcher responses to Q1–Q4 (will be provided at session start)

**Reference (only as needed by specific moves):**
- wa-patch-specification-v1_14-20260416.md (if GR-DIR-006 relocation approved)
- WA-Reference-v5_5-20260330.md (if GR-DATA-001 or GR-DATA-003 relocations approved)

### 4.3 Files to attach at next session start

Attach the five required files listed above. Researcher attaches responses to Q1–Q4 (may be inline in chat).

---

## 5. Session-level reflection

Three wrong turns were taken in this session, each corrected by the researcher. Recorded for the record:

**W1** — Initial framing as fellowship consolidation rather than programme-level framework. Corrected.

**W2** — Proposed a separate 4–6 page standalone document when the correct shape was a 2–3 page header inside global rules. Corrected.

**W3** — Delivered audit findings and the 53-row classification table in chat rather than as markdown files. This is the same failure the preamble names as mechanism #2: "working material is held in chat and memory rather than written to disk." The preamble was drafted in this session and then violated in this session. Corrected when researcher surfaced the issue directly.

The fellowship session's closing line — "This is not the first time we go through this. I hope this is the last." — applies again here. The discipline required to complete this session is the discipline the programme needs to install continuously.

---

## 6. Outputs presented for download

All three of the following produced, dual-written, available at /mnt/user-data/outputs/:

- `wa-global-rules-audit-v1-20260417.md`
- `wa-global-preamble-obslog-v1-20260417.md`
- `wa-global-preamble-sessionlog-v1-20260417.md` (this file)

Plus from earlier in session:
- `wa-global-general-rules-v2_6-20260417.json`

---

## 7. Session close

Session closes cleanly with:
- All outputs dual-written (GR-FILE-008)
- Session log produced (GR-PROC-006, GR-OBS-003)
- Observations log produced (GR-OBS-001)
- Outputs presented for download (GR-PASS-001 spirit applied)
- Open questions (Q1–Q4) documented for next session (GR-RD-006)
- Wrong turns recorded (for pattern recognition across sessions)

No rule has been moved. No reference document has been altered. The only file change in the programme from this session is v2.5 → v2.6 of the global rules, adding the preamble.

---
```

---

## Source 4

Source: `Workflow/Sessionlogs/wa-global-rules-v2_7-obslog-v1-20260417.md`

```md
### Item 8 — the GR-FILE-004 / reliable-write-cadence problem

This is the most important part of your message and I want to give it weight. You said:

> *"GR-FILE-004. I think we already dealt with a more intelligent versioning rule. You need to help me with this cycle. I have lost numerous working session data because AI did not produce the observation or session log. it keeps working and working and never comes forward with the result, and then if I ask to download, the file is incomplete or cannot be outputted. How do I prevent this."*

**Observation — the problem stated in concrete terms:**

The failure mode is: Claude AI is in the middle of analytical work, holds findings in memory and chat, does not write them to the obslog or session log at the time of each finding. When the session ends (or is asked to produce logs), the logs do not reflect the actual work. Or the session times out / crashes before the logs are produced.

This is exactly preamble mechanism #2. It has been named, and it continues to happen. Writing a rule does not prevent it.

**Reflection — why rules alone have not solved this:**

Rules are read once at session start (GR-LOAD-001). They are not re-applied on every response. Claude AI's moment-to-moment behaviour depends on habit, and habit in the middle of an analytical session drifts toward "think hard, output the finding in chat, plan to write later."

**Possible mechanical interventions — options for you to choose from:**

- (M1) **Pre-response self-check.** Claude AI names, before every substantive chat response, what it wrote to disk in this turn. If nothing was written, the response itself is flagged as a compliance step (either the response is discussion-only and that's fine, or it contained a finding and the finding must be written before the response goes out).

- (M2) **Turn-by-turn dual-write.** After every turn that produced a finding, decision, interpretation, or action, Claude AI writes to the obslog and dual-writes to /mnt/user-data/outputs/ before returning control. The researcher sees the file update in the output panel every turn — visible accountability.

- (M3) **Explicit write-points.** The governing instruction defines the moments at which writes happen (e.g. after each rule interpretation, after each file change, at every researcher acknowledgement). At those moments the write is mandatory; between them it is not.

- (M4) **Session-start obslog opening + present-files at every milestone.** Obslog is opened at the first response in the session (already in place this session). `present_files` is called at every substantive step so the file is always visible for download. This prevents end-of-session loss because the most recent version is always downloadable.

- (M5) **Combine M1 + M4.** Self-check + continuous visibility.

**My recommendation: M2 + M4.** Every substantive turn writes to disk and dual-writes to outputs. The file shows up fresh in the output panel each time. If the session dies, the most recent state is always recoverable. I have been doing M2 in this session (each obslog entry is dual-written). What M4 adds is calling `present_files` more frequently — not just at the end of an exchange, but after every substantive write.

**Question for you: does M2+M4 address the problem, or do you want stronger mechanics (M1 pre-response self-check)?**

**Also:** do we merge GR-PROC-006 and GR-OBS-003 at the same time? My read:

- Retire GR-PROC-006
- Strengthen GR-OBS-003 to read: *"The observations log and the session log are separate files with separate purposes. The observations log is the working paper, written continuously per GR-OBS-001. The session log is the handoff record, produced at session close and at any named batch boundary within a session. A session that closes without a session log has not closed cleanly. The session log is always produced before the session ends."*

**Ready to apply pending your choice of mechanics.**

### Item 9 — APPROVED option (b) — trim GR-PROC-001

Draft final text for GR-PROC-001 (v2.0):

> *"A step that produces a required output is not complete until that output exists and has been confirmed."*

Everything else (read-follow-validate, no skipping) is now preamble-governed.

**Ready to apply.** Confirm wording.

### Item 10 — APPROVED with specific text removal only

GR-PROG-002 retained in GR file, governing question retained, but the sentence about divine characteristics is removed.

**Draft final text for GR-PROG-002 (v2.0):**

> *"The programme's governing question is: what does Scripture reveal about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body)? All analytical work is oriented toward this question."*

**Note — this resolves the A6 ambiguity** and the rule stays in global rules (not moved to addendum). Item 10 from the previous batch is replaced by this decision.

**Ready to apply.** Confirm wording.

## Entry O-019 — `discussion` — Summary of current state and next steps

**Ready to apply with your final wording confirmation:**
1. Item 2 — GR-PROG-005 consolidation (absorbs GR-DIR-004, GR-PROC-003) with TODO marker
2. Item 3 — GR-PROC-002 consolidation (absorbs GR-PROG-008)
3. Item 4 — addendum (b) additions (ADD-PATCHDIR-003 for GR-DIR-008)
4. Item 6 — GR-FILE-003 rewrite (underscored versioning)
5. Item 7 — GR-FILE-005 (new simple formulation) or drop
6. Item 8a — GR-OBS-001 with chat-output-to-log clause
7. Item 8d — GR-OBS-005 move to addendum_patch_directive
8. Item 8e — GR-OBS-006 move to addendum_instructions (target: Session B)
9. Item 9 — GR-PROC-001 trim
10. Item 10 — GR-PROG-002 edit (drop divine-characteristics sentence)

**Needs decision before I apply:**
- **Flags migration** — where flags live (new dedicated file vs obslog vs session log), and whether all 9 or only active 7 move.
- **Version notation in JSON `version` field** — underscored `2_7` or dotted `2.7` (machine parsing consideration).
- **Item 7 destination** — short replacement rule (a), no replacement (b), fold into GR-FILE-001 (c).
- **Write-cadence mechanics** — which of M1–M5 to adopt.
- **GR-PROC-006 retirement + GR-OBS-003 strengthening** — confirm.
```

---

## Source 5

Source: `memory/feedback_copilot_frustration.md`

```md
---
name: feedback_copilot_frustration
description: User was frustrated by GitHub Copilot — avoid whatever patterns caused that
type: feedback
---

leRoux switched from GitHub Copilot (Claude Sonnet) to Claude Code because Copilot "endlessly frustrated" him.

**Why:** Specific frustrations not yet detailed, but the latest commit message says "AI attempts to fix and correct and update, but largely fails."
**How to apply:** Be precise, don't over-promise, don't make changes without understanding the code first. If something fails, diagnose rather than retry blindly. Ask before acting on non-trivial operations.
```