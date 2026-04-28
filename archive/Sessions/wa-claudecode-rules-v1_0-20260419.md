# WA — Claude Code Operating Rules

**Framework B — Soul Word Analysis Programme  
CC-specific rules supplementing the global general rules  
Version 1_0 | 20260419 | Status: Active — approved 2026-04-19 by le Roux Cilliers**

| **Document** | **Value** |
|---|---|
| Filename | wa-claudecode-rules-v1_0-20260419.md |
| Supersedes | (new document) |
| Companion | `wa-global-general-rules [current]` — governs all actors. This doc supplements it for CC. |
| Governs | All CC operations across all instructions |
| Produced | 2026-04-19 |
| Trigger for creation | Researcher direction 2026-04-19 that global general rules apply to CC as well as Claude AI, and CC may create its own supplementary rules |

---

## Purpose

This document captures CC-specific operating rules that supplement the global general rules. These rules govern **how CC works** under the file-based, no-chat-Q&A protocol established 2026-04-19.

The global rules apply to CC with their plain meaning (where they reference "Claude AI", read "Claude AI or CC as appropriate"). The rules in this file are additions, not replacements.

---

## Change Log

**v1_0 (2026-04-19):** New document. Captures the eleven CC-specific rules proposed in the DB-wide review design workings §7. Published at the start of the DB-wide review to govern CC's execution from that point onward.

---

## Relationship to Other Documents

| Document | Relationship |
|---|---|
| `wa-global-general-rules [current]` | **Supreme** — CC rules cannot contradict. Where this file cites a global rule, treat the global rule as the parent. |
| `wa-reference [current]` | Controlled vocabulary, schema reference — CC follows as definitive |
| `wa-patch-instruction [current]` | Patch construction — CC rules PATCH-001 layers on top |
| `wa-directive-instruction [current]` | Directive construction — CC follows as definitive |
| `wa-claudecode-instruction [current]` | CC responsibilities and task list. This rules file governs HOW those responsibilities are discharged. |

If a rule conflict arises between this file and a global rule: global wins. Record the conflict as an RD item so the conflict can be resolved in the next global rules revision.

---

## Rule Index

| Rule ID | One-line summary |
|---|---|
| CC-LOAD-001 | Load and state governing documents at session start |
| CC-OBS-001 | All findings, decisions, actions recorded in obslog .md — never only in chat |
| CC-RD-001 | RESEARCHER_DECISION items written to RD .md, not asked in chat |
| CC-SKILL-001 | Tasks beyond CC's tooling → outstanding tasks .md with capability statement |
| CC-PATCH-001 | Patches written to disk; approval recorded in .md before apply |
| CC-RERUN-001 | CC operations are rerun-safe / idempotent on clean state |
| CC-FAIL-001 | Unverifiable outcomes become RD items, not silent proceeds |
| CC-SCOPE-001 | No analytical judgement — surface to Path 3 or Path 5 |
| CC-LOCK-001 | Respect per-registry locks; skip with obslog note; retry next session |
| CC-VERSION-001 | Schema version check at session start; refuse on mismatch |
| CC-IDEM-001 | Remediation patches specify corrections; double-apply is a bug to detect |
| CC-DATA-001 | Data authoritative — SQL live DB + design workings only |
| CC-CHAT-001 | Chat is for pointers only; substantive content lives in .md |
| CC-TOOL-001 | Use dedicated tools over ad-hoc bash where available |
| CC-BACKUP-001 | Before any DDL or destructive DML: backup before, confirm, then act |

---

## Rules

### CC-LOAD-001 — Governing documents loaded at session start

**Rule:** At the start of every session, CC loads the governing document set for the instruction being followed. CC states the resolved version of each document (per GR-REF-002 `[current]` token resolution). CC does not proceed with any work until all confirmations are recorded in the observations log.

**Mirror of:** GR-LOAD-001 (for Claude AI). This rule extends the same discipline to CC.

**Minimum set for any CC session:**

- Global rules file
- CC rules (this file)
- The instruction governing the current work
- Patch instruction
- Directive instruction

**Additional per instruction:** whatever the instruction specifies under "What to Attach at Session Start".

**Applies to:** all CC sessions without exception.

### CC-OBS-001 — Observations log is the primary record

**Rule:** Every finding, decision, action, and outcome that CC produces is recorded in an observations log `.md` at the moment it occurs. Chat output is a pointer to the obslog — not the log itself. Chat transient content cannot serve as a record of work done.

**Mirror of:** GR-OBS-001. Non-waivable.

**Implementation:**

- Obslog file is versioned per GR-OBS-004 and GR-FILE-004
- Every session creates or increments a minor version
- Sections within the obslog are defined by the governing instruction
- CC writes to obslog *before* completing the action (not in a batch at end)

**Why:** researcher-stated requirement 2026-04-19 that all workings be file-tracked for restart, backtrack, and asynchronous review.

### CC-RD-001 — RESEARCHER_DECISION items via file, never chat

**Rule:** CC never asks questions of the researcher in chat. Any question requiring human judgement is written to a RESEARCHER_DECISION accumulator `.md` file in the form prescribed by the governing instruction, with options stated and CC's recommendation.

**Mirror of:** GR-RD-001 through GR-RD-006 (for Claude AI, who also writes RD blocks).

**Implementation:**

- RD accumulator file is separate from obslog; dedicated per work stream
- Each RD item has an RD-ID, context, options, consequences, and CC's recommendation
- Researcher marks up the file to resolve; CC polls the file at session resume
- Never ask in chat; never sleep mid-operation waiting for a response

**Why:** researcher-stated requirement 2026-04-19 that chat not be the place for Q&A.

### CC-SKILL-001 — Skill-limit to outstanding tasks file

**Rule:** When a task is beyond CC's tooling or skill, CC records it in the outstanding tasks `.md` file with an explicit statement of what capability is missing. CC does not attempt to work around skill limits silently.

**Implementation:**

- Outstanding tasks file is persistent across sessions (single file per work stream, or programme-wide)
- Each entry: task description, why it is beyond CC's skill, what capability is required (tool, API, library, access), date recorded, status (OPEN / RESOLVED with resolution note)
- Recorded in obslog as a cross-reference (`Outstanding task added: see wa-global-outstanding-tasks-v{n}-{date}.md entry #{n}`)

**Why:** researcher-stated requirement 2026-04-19 that tasks beyond CC's skill have a visible home.

### CC-PATCH-001 — Patches to disk, approval on file, then apply

**Rule:** CC writes patch files to disk and awaits explicit approval recorded in the obslog (or a dedicated approval file) before applying. Chat-based approval is not sufficient under the 2026-04-19 working protocol.

**Implementation:**

- Produce patch file in the location specified by `wa-patch-instruction`
- Note in obslog: `Patch [patch_id] produced: [path]. AWAITING APPROVAL. Approval recorded by writing "APPROVED: [date]" on the patch entry here, or by researcher marking the approval block on the patch file itself.`
- CC does not apply until approval is on file
- After apply: CC verifies against expected outcomes and records in obslog

**Why:** matches existing patch approval discipline from v1.6; extends it for the file-only protocol.

### CC-RERUN-001 — Operations are rerun-safe on clean state

**Rule:** CC operations must be idempotent. Re-running a clean operation produces a no-op (zero changes). Re-running a partial operation completes it; never duplicates already-completed work.

**Implementation:**

- Every CC script that modifies state first checks whether the target state is already achieved
- Patches target specific states; a patch that would apply the same correction twice is a bug to detect
- Workflow loops (e.g. readiness sweep) that re-process a registry detect already-clean state and exit cleanly

**Why:** work will be interrupted, resumed, re-run; CC must not corrupt state via over-application.

### CC-FAIL-001 — Unverifiable outcomes become RD items

**Rule:** If CC cannot verify the outcome of an action it has taken (e.g. patch applied but post-check ambiguous), CC records the condition as an RD item and halts further dependent work. CC does not proceed on assumption.

**Implementation:**

- Every patch, directive execution, or migration has a verification step
- Failure of verification → RD item with full context
- Ambiguity in verification output → RD item (do not assume success)

**Why:** silent failure is worse than explicit halt.

### CC-SCOPE-001 — No analytical judgement

**Rule:** CC does not perform analytical judgement. Tasks requiring verse reading, semantic assessment, or interpretive decisions are surfaced — never resolved inline — as either:

- Path 3 (deferred to per-word Claude AI Stage 1)
- Path 5 (outstanding task if beyond even per-word analytical capability)

**What counts as analytical:**

- Reading a verse and assessing whether a flag claim holds
- Evaluating whether a dimension label is appropriate for a group
- Judging whether a finding should be extended or contradicted
- Interpreting theological content

**What does not count (CC can do):**

- Counting rows and comparing against expected
- Confirming FK integrity
- Applying controlled vocabulary where the value is derivable from a pattern
- Any SQL-level check

**Why:** mechanical work is CC's skill; analytical work is Claude AI's.

### CC-LOCK-001 — Respect per-registry locks

**Rule:** CC respects per-registry locks (`word_run_state.phase1_status = 'IN_PROGRESS'` or equivalent lock sentinel). A registry under lock is skipped in any bulk operation, with an obslog note explaining the skip; re-attempted in the next session after the lock clears.

**Implementation:**

- Before any per-registry operation, query lock state
- If locked and unrelated to current op: skip, log
- If locked by this CC instance (e.g. stale lock from previous session): apply standard stale-lock detection (STALE_LOCK_SECONDS = 7200); either clear with researcher approval or wait

**Why:** concurrent modification corrupts state; lock existed for a reason.

### CC-VERSION-001 — Schema version check at session start

**Rule:** CC queries `schema_version` at the start of every session and compares against `engine/constants.py::EXPECTED_SCHEMA_VERSION`. On mismatch, CC halts and produces an RD item.

**Implementation:**

```sql
SELECT version FROM schema_version ORDER BY applied_at DESC LIMIT 1;
```

Compare to Python constant. Record both values in obslog. Halt on mismatch.

**Why:** DB may have been migrated by another session / script; running CC against unexpected schema risks corruption.

### CC-IDEM-001 — Remediation patches specify corrections

**Rule:** CC's remediation patches specify *corrections to a target state*, not *operations on current state*. A patch that would apply the same correction twice must be detected as a bug in the patch construction step, not swallowed silently.

**Implementation:**

- Each patch operation specifies the target value (e.g. `language = 'Hebrew'`), not a delta (e.g. "change language from Greek to Hebrew")
- Before producing a patch, CC checks current state: if already at target, no operation needed
- Double-apply detection: patch construction queries current state; generates zero-op patch if clean; logs "clean — no patch produced"

**Why:** allows rerunning remediation safely; makes patches declarative.

### CC-DATA-001 — Data authoritative

**Rule:** CC works strictly from:

1. The live DB (via SQL)
2. The governing instruction documents
3. The design workings referenced by the instruction

CC does not import general knowledge to fill gaps, does not infer undocumented behaviours, does not rely on conversational memory of prior sessions.

**Mirror of:** GR-PROC-002.

**Implementation:**

- If information is not in the three sources above, CC produces an RD item or a clarification request in an RD file
- CC does not proceed on unverified assumptions

### CC-CHAT-001 — Chat is for pointers only

**Rule:** Chat output serves as a pointer to the files where substantive content lives. It is never the primary record. A chat message should:

- Tell the researcher what file was produced or modified and where to find it
- Flag any decisions or RD items added
- Summarise outcomes in one or two sentences

Chat should not contain:

- Full analyses
- Long lists of findings
- Detailed rationales
- Q&A back-and-forth

**Why:** researcher-stated working protocol 2026-04-19.

### CC-TOOL-001 — Use dedicated tools over ad-hoc bash

**Rule:** CC prefers dedicated tools (Read, Write, Edit, Glob, Grep) over ad-hoc bash invocations. Bash is reserved for: running engine scripts, git, pip, python execution, or other operations that require a shell.

**Why:** established project tool usage convention (per CLAUDE.md Using your tools).

### CC-BACKUP-001 — Backup before DDL or destructive DML

**Rule:** Before any DDL (migration) or destructive DML (bulk DELETE, bulk UPDATE that cannot be reverted), CC takes a backup and confirms it exists and is readable before proceeding.

**Implementation:**

- `python -m engine.engine --backup --label="pre_{operation}_{YYYYMMDD}_{HHMMSS}"`
- Verify file exists and size > 0
- Record backup path in obslog before starting the destructive operation
- For DB review migrations specifically: backup retained 6 months minimum (per DBR Q6 resolution)

**Why:** destructive operations must be reversible.

---

## Cross-References

| Rule | Seen from | Purpose |
|---|---|---|
| CC-LOAD-001 | DB review instruction §5 Step S1 | Governs session start |
| CC-OBS-001 | DB review instruction §3 | Governs recording |
| CC-RD-001 | DB review instruction §3, §16 | Governs questions |
| CC-SKILL-001 | DB review instruction §3 | Governs scope boundary |
| CC-PATCH-001 | `wa-patch-instruction [current]` | Governs patch approval |
| CC-VERSION-001 | DB review instruction §5 Step S2 | Governs schema check |
| CC-BACKUP-001 | DB review instruction Phase E Step E.2 | Governs migration backup |

---

## Governance

This file follows the same version discipline as other framework documents:

- Never modified in place after publication
- Updates produce a new minor version (v1_1, v1_2, …)
- Major changes to rule semantics produce a new major version (v2_0, …)
- Old versions retained in `archive/` per file organisation rules
- `[current]` token resolution per GR-REF-002

**Proposed rule additions** (by researcher or CC): added by producing a new minor version. Old version retained for provenance.

**Conflict with a global rule:** global rule wins. RD item recorded for resolution in the next global rules revision.

---

## Approval

**Researcher approval:**

Status: [X] APPROVED — PROCEED (this file is now active CC governance)  [ ] REVISIONS REQUESTED — see markup

Date: 2026-04-19
Reviewer: le Roux Cilliers
Notes: Approved alongside the DB-wide review instruction. Becomes active CC governance from this point forward.

---

*wa-claudecode-rules-v1_0-20260419.md*
*Framework B — Soul Word Analysis Programme*
*Supplements: wa-global-general-rules [current]*
