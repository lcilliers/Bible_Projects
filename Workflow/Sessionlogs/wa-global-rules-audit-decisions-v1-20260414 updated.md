# WA Global Rules Audit — Decision Register

**File:** wa-global-rules-audit-decisions-v1-20260414.md
**Date:** 20260414 | **Version:** 1.0
**Previous:** wa-global-rules-audit-session-log-v1-20260414.md
**Purpose:** Interactive decision register. Each item is a concrete action requiring your confirmation (Y/N/MODIFY). Once confirmed, I produce the updated file immediately before moving to the next item.

\---

## HOW TO USE THIS DOCUMENT

Each item shows:

* **What:** what change is proposed
* **Where:** which file is affected
* **Why:** the reason
* **Options:** what you can confirm

Reply with the item number and your decision. Example: `D-01: Y` or `D-03: MODIFY — \[your instruction]`.

I will complete each confirmed item fully (update the file, present for download) before moving to the next.

\---

## SECTION A — Global Rules File Updates (already done in v2)

These changes are already in `wa-global-general-rules-v2-20260414.json`. Review and confirm or reject each.

|#|Change made|Rule ID|Your call|
|-|-|-|-|
|A-01|GR-LOAD-001 added: mandatory load at session start, hard gate, states Claude forgets between sessions|GR-LOAD-001|Confirm |
|A-02|GR-FILE-007 added: all filenames lowercase|GR-FILE-007|Confirm |
|A-03|GR-FILE-008 added: dual-write to /home/claude/ and /mnt/user-data/outputs/|GR-FILE-008|Confirm |
|A-04|GR-FILE-009 added: compact date YYYYMMDD in filenames, ISO date permitted in prose|GR-FILE-009|Confirm |
|A-05|GR-OBS-005 subject updated to "Records flagged not deleted — audit trail preserved"; rule text unchanged from v1|GR-OBS-005|Confirm |
|A-06|GR-PROC-001 through GR-PROC-007 added (step-by-step, data authoritative, all changes through patches, no patch without review, observations log governs, session logs at breakpoints, fix-or-stop)|GR-PROC-001–007|Confirm |
|A-07|GR-PROG-007 added: filter at term level not verse level|GR-PROG-007|I do not know what this means or will be applied|
|A-08|GR-PROG-008 added: emergence principle applies to all classifications, not only dimensions|GR-PROG-008|Confirm|
|A-09|GR-PROG-009 added: inferential is not confirmed; inferential label is accurate, not a failure|GR-PROG-009|Confirm |
|A-10|GR-DATA-005 updated: added note that citations of WA-Reference Section 13.3 should be updated to cite GR-DATA-005|GR-DATA-005|Confirm |
|A-11|GR-DATA-008 added: engine-derived Phase 1 fields not updated by later pipeline|GR-DATA-008|Confirm |
|A-12|GR-FILE-001 example date updated to compact format (20260411 not 2026-04-11)|GR-FILE-001|Confirm |

\---

## SECTION B — Project Setup Info Conflicts

These are stale or conflicting references in the project memory/context that need correction. **These require your action in the project settings**, not in the instruction files.

|#|Location|Stale/wrong value|Correct value|Action needed|
|-|-|-|-|-|
|B-01|userMemories — governing instruction versions|`WA-VerseContext-Instruction v2.4`|v2.5|Update memory|
|B-02|userMemories — governing instruction versions|`WA-DimensionReview-Instruction v2.1`|v1.9 (v2.1 does not exist)|Update memory|
|B-03|userMemories — governing instruction versions|`patch\_specification v1.7`|v1.10|Update memory|
|B-04|userMemories — filename examples (session logs etc.)|Hyphenated dates e.g. `2026-04-11`|Compact dates e.g. `20260411` (after GR-FILE-009 confirmed)|Update memory after A-04 confirmed|
|B-05|userMemories — "Observations logs are version-incremented at named boundaries, not per-write or per-session"|Conflicts with Dimension Review Section 6.2: "version-increment on every new write session for the same cluster"|Correct behaviour: version-increment at named analytical boundaries (start of new cluster, new registry, or new session day) — not on every file save. Needs researcher decision to settle|**DECISION NEEDED** — see D-01 below<br /><br />D-01A|

\---

## SECTION C — Instruction File Changes Required

Each item below is a change needed in an instruction file. I will produce each updated file only after you confirm the item.

**Working method:** I confirm item → produce updated file → present for download → move to next item.

### C-01 through C-06: Remove duplicate rule text, replace with GR reference

These are cosmetic but reduce maintenance risk. Each instruction currently restates a global rule in full prose. The instruction should instead say: "Per \[GR-XXX-NNN]." The operational procedure detail stays; only the principle statement is replaced.

|#|File|Current inline text|Replace with|Depends on|
|-|-|-|-|-|
|C-01|Session B v4.7 — Governing Disciplines|Full write-on-discovery paragraph|"Write on discovery — per GR-OBS-001 (non-waivable)."|A-03 confirmed|
|C-02|Session B v4.7 — Pass 4 somatic\_link note|"Do NOT update wa\_term\_inventory.somatic\_link — this is a redundant field per WA-Reference Section 13.3"|"Do NOT update wa\_term\_inventory.somatic\_link — redundant per GR-DATA-005."|A-10 confirmed|
|C-03|Dimension Review v1.9 — Foundational principles|Write-on-discovery paragraph (Section 0)|"Per GR-OBS-001 (non-waivable)."|A-03 confirmed|
|C-04|Dimension Review v1.9 — Section 1.3 and 1.1|"No dimension category is assumed correct before group content has been read; automated labels are a starting map not a conclusion"|"Per GR-PROG-002."|A-08 confirmed|
|C-05|Verse Context v2.5 — Section 3.3|Borderline retention paragraph|"Per GR-PROG-004."|—|
|C-06|Verse Context v2.5 — Section 6.2 Step 2 all-verses-fail|"individual inspection is mandatory and non-waivable regardless of corpus size" principle statement|"Per GR-PROG-005 (non-waivable). Operational procedure below." Keep the procedure detail.|—|

### C-07: Add global rules reference header to each instruction

Each instruction should open with:

```
## Governing rules
This instruction is governed by wa-global-general-rules-v\[n]-\[date].json.
Claude AI must confirm the global rules file has been loaded before beginning any work in this session.
Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.
```

|#|File|Action|
|-|-|-|
|C-07a|Session B v4.7|Add global rules header immediately after document header table|
|C-07b|Verse Context v2.5|Add global rules header|
|C-07c|Dimension Review v1.9|Add global rules header|

### C-08: Correct stale companion document reference in Dimension Review

|#|File|Current|Correct|
|-|-|-|-|
|C-08|Dimension Review v1.9 — companion documents table|WA-SessionB-Analysis-Instruction-v5.7|WA-SessionB-Instruction-v4.7|

\---

## SECTION D — Decisions needed before any instruction changes

These items cannot be resolved without your input. I need your answer before I can update the relevant files.

### D-01: Observations log versioning rule

**Conflict:** Project memory says "version-incremented at named boundaries, not per-write or per-session." Dimension Review instruction says "version-increment on every new write session for the same cluster."

**Why it matters:** This affects every session that produces an observations log. If the rule is "every new write session", then a session that pauses and resumes the next day produces v1.1, v1.2, etc. If the rule is "named boundaries only", then the version only changes at a defined milestone (new cluster, new stage, new registry).

**My assessment:** Named boundaries is the more practical rule — it avoids proliferating micro-versions for the same body of work. "Write session" in the DR instruction likely meant "when you open a new session to continue the same cluster" not "every time you save the file." But I cannot confirm this without your decision.

**Options:**

* D-01A: Named boundaries is correct. Update memory. Update DR instruction to say "version-increment when resuming a cluster in a new session."
* D-01B: Every write session is correct. Update memory to match DR instruction.
* D-01C: Clarify the distinction. A new session-day working on the same cluster increments minor (e.g. v1.1 → v1.2). A new cluster or stage increments major (v1 → v2).

### D-02: Session C instruction — does it exist as a project file?

**Observation:** The project files include `wa-global-sessionC-prose-rule-v1-2026-04-13.md` and `wa-word-study-template-v2-2026-04-13.md` but no full Session C instruction document. The pass-close procedure and prose rule both say "for incorporation into the Session C instruction at its next revision."

**Question:** Is there a Session C instruction document that I have not yet read? If yes, please confirm its filename and I will read and audit it. If no, the `wa-global-sessionC-prose-rule` is the current governing document for Session C.

### D-03: Session B — five or six passes?

**Observation:** The Session B instruction (v4.7) repeatedly refers to "five passes" in its overview and some section headers, but the instruction body defines six passes (Pass 1 through Pass 6, with Pass 6 being Correlation Audit). The session close confirmation template (line 934) references "six mandatory outputs" — but the pass count language is inconsistent in several places.

**Question:** Is this a known inconsistency, or should I flag it for correction when updating Session B?

\---

## SECTION E — Items confirmed as instruction-specific (no global rule needed)

These rules were assessed in the session log. Confirmed here as correctly staying in their instruction — no promotion to global rules needed. Listed for completeness.

|Rule|Instruction|Reason it stays local|
|-|-|-|
|Cross-registry vision discipline (Section 2.0a)|Session B|Only relevant during Session B Stage 2 analytical passes|
|"Session C documents are not sacred"|Session B|Stage-specific motivational principle|
|Correlation signals confirm, they do not explain|Session B|Pass 6-specific|
|Somatic evidence is observational not interpretive|Session B|Pass 4-specific|
|Phase 2 flags are recommendations not conclusions|Session B|Pass-specific|
|Anchor verse selection criteria (1-2 per group)|Verse Context|Stage-specific procedure|
|Group description QA flag vocabulary|Dimension Review|Stage-specific|
|Wrong-face set-aside procedure|Verse Context|Stage-specific|
|Deferred flag protocol|Verse Context|Stage-specific procedure|
|SD pointer patch mandatory before Stage 3 (SB-14/15)|Session B|Stage gate, not a general rule|

\---

## CURRENT STATUS

|Section|Status|
|-|-|
|A — Global rules v2|DRAFT — awaiting your confirmation|
|B — Project setup conflicts|IDENTIFIED — some require your action|
|C — Instruction changes|QUEUED — awaiting Section A confirmations and D decisions|
|D — Pending decisions|OPEN — D-01, D-02, D-03|
|E — Instruction-specific rules|CONFIRMED as local|

**Suggested sequence:**

1. Confirm or modify Section A items (global rules v2) — this unlocks Section C
2. Resolve D-01, D-02, D-03 — these determine scope of instruction changes:  

   1. D-01A should be applied globally
   2. D-02 Session C instruction now uploaded
   3. D-03 The document defines 6 passes.  Session B instructions  must be updated.
3. I work through C-01 to C-08 one file at a time, presenting each for download before moving on
4. You handle B-01 to B-04 in project settings; I will note B-05 resolution after D-01

