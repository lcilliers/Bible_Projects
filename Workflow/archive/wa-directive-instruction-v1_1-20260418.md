# wa-directive-instruction-v1_1-20260418

> Framework B Soul Word Analysis Programme — Directive Preparation and Execution
> Version: v1_1 | Date: 20260418
> Supersedes: wa-directive-instruction-v1_0-20260418.md (new document in v1_0; this minor increments for GR-REF-002 sweep)
> Governed by: wa-global-general-rules [current]

---

## Document scope (GR-REF-001 Discipline 5)

This document is the authoritative source for:
- Directive plain-language format — the five required elements
- Directive preparation workflow — how Claude AI constructs a directive
- Directive execution workflow — how Claude Code receives, validates, and executes
- Directive filename convention
- Directive self-check protocol
- Completion confirmation for directives

This document is NOT authoritative for (pointers, not copies):
- Patch format and execution → wa-patch-instruction [current]
- Controlled vocabulary → wa-reference [current]
- CC operational routines outside directive handling → wa-claudecode-instruction [current]
- Programme-wide binding rules → wa-global-general-rules [current]

---

## Change Control — v1_1

| Change | Section |
|---|---|
| Operational cross-references migrated to `[current]` token per GR-REF-002 — frontmatter, §1, §6, §7, §8-equivalent areas | Frontmatter, §1, inline |
| Inline references updated: `wa-patch-instruction v2_0` (4 occurrences in §1, §6, §7, §8) → `[current]`; rule-version reference `global rules v2_11` in §1 → `[current]` | §1, §6, §7, §8 |
| Provenance preserved: footer consolidation line; `Produced by` field illustration in §4 template | — |
| v1_0 Change Control retained below for provenance | — |

### Prior change control — v1_0

New document. Consolidates content previously scattered across:

| Source | Content absorbed |
|---|---|
| global rules addendum ADD-PATCHDIR-005 | When to use directive vs patch (GR-DIR-001) — §1 |
| global rules addendum ADD-PATCHDIR-006 | Directive five required elements (GR-DIR-002) — §3 |
| global rules addendum ADD-PATCHDIR-008 | Completion confirmation mandatory (GR-DIR-005) — §6 |
| global rules addendum ADD-PATCHDIR-009 | Directive filename convention (GR-DIR-007) — §2 |
| global rules addendum ADD-PATCHDIR-003 | Directive self-check (GR-DIR-008) — §7 |

This document resolves addendum ADD-PATCHDIR-002 (the recorded observation that no peer specification for directives exists).

---

## 1. Role and When to Use a Directive

Per GR-PROG-005 in global rules [current], Claude AI determines what should be done and why; Claude Code executes. There are two and only two mechanisms for instructing Claude Code to make database changes — patches (wa-patch-instruction [current]) and directives (this document). Conversational instructions to CC without either format are not valid database change requests.

### 1.1 When a directive is the right tool

Use a directive when Claude AI knows the outcome required but is not certain of the exact execution path. Claude AI describes in plain language what needs to happen and why; Claude Code inspects the database, determines the correct operations, and executes.

Typical directive scenarios:
- Investigating a data anomaly where the fix is obvious but the affected rows must be discovered first
- Cleaning up orphaned records where the selection criteria are clear but the exact IDs are not known
- Running a maintenance operation whose scope depends on current DB state
- Producing a report that requires CC to compose queries across multiple tables
- One-off remediation where a structured patch would be disproportionate overhead

### 1.2 When a patch is the right tool

Use a patch (wa-patch-instruction [current] §1.1) when Claude AI is certain of the field names, FK keys, table structure, and exact operations. Patches are machine-readable, idempotent, and auditable.

### 1.3 Choice in borderline cases

When a task could be done either way, the default is patch if the scope is well-bounded and the operations are known. Directive if the scope requires DB inspection to resolve.

Where in doubt, Claude AI raises the choice to the researcher as a direction/principle question (GR-HF-001 permitted minimum — one clarifying question).

### 1.4 Common rules (both methods)

- Researcher approval before Claude Code acts — per GR-PROC-004
- Stated completion confirmation — per §6 below for directives; wa-patch-instruction §6 for patches
- No conversational bypass — instructions outside patch or directive format are not valid

---

## 2. Directive Filename Convention

Per GR-FILE-001, GR-FILE-007, GR-FILE-009 in global rules v2_11.

### 2.1 Standard pattern

```
wa-{registry_no}-{word}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md
```

| Component | Content |
|---|---|
| `{registry_no}` | Zero-padded registry number (e.g. `062`) |
| `{word}` | English word (e.g. `fellowship`) |
| `dir` | Fixed token marking this as a directive |
| `{seq}` | Zero-padded 3-digit sequence number within the session (`001`, `002`, …) |
| `{description}` | Short lowercase descriptor of purpose, max 20 characters, no spaces |
| `{n}` | Version number starting at 1 |
| `{YYYYMMDD}` | Compact date produced |

Example: `wa-062-fellowship-dir-001-vc-subproc-v1-20260416.md`

### 2.2 Programme-level directives

For directives not tied to a single registry, use `global` as the reference segment per GR-FILE-006:

```
wa-global-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md
```

Example: `wa-global-dir-001-schema-cleanup-v1-20260418.md`

### 2.3 Directive ID

Independent of filename. Used as internal reference in observations logs and completion confirmations:

```
DIR-{YYYYMMDD}-{NNN}
```

Where `NNN` is a 3-digit sequence within the date. Example: `DIR-20260418-001`. Uppercase retained by convention (parallel to `patch_id`).

---

## 3. Directive Format — Five Required Elements

Every directive contains exactly these five elements. A directive missing any element is malformed — see §7 for self-check and §8 for CC rejection behaviour.

### 3.1 Element 1 — DIRECTIVE ID

Unique identifier in format `DIR-YYYYMMDD-NNN` per §2.3.

### 3.2 Element 2 — MOTIVATION

Why this change is needed and what problem it solves. Specific. Not "general cleanup"; name the actual issue, the evidence that it exists, and why it must be addressed now.

Example:
> *Eleven verse records are orphaned — their `term_inv_id` points to a `wa_term_inventory` row that was delete_flagged when the term was reclassified as bleed. The orphan records are being returned by the verse-count query and inflating the reported verse count for registry 097. The registry's session_b_status cannot advance to Ready for Analysis while the verse count is wrong.*

### 3.3 Element 3 — SCOPE

Which tables, records, or fields are affected. Specific enough that CC can determine the query to run — not exhaustive enough to require CC analytical judgement.

Example:
> *Table: `wa_verse_records`.*
> *Criterion: `term_inv_id` pointing to a row in `wa_term_inventory` where `delete_flagged = 1`.*
> *Registry filter: `wa_file_index.word_registry_fk = 97` (registry 097 only).*
> *Expected count: approximately 11 — exact count to be determined by CC.*

### 3.4 Element 4 — OUTCOME REQUIRED

What the database state must look like after execution. Stated precisely enough that CC can verify. Not "the orphans should be cleaned up" — state the exact field values expected post-execution.

Example:
> *For every `wa_verse_records` row meeting the scope criterion: set `delete_flagged = 1`; set `obsolete_reason = 'orphaned verse — parent term delete_flagged'`; set `obsolete_date = today's compact date`.*
> *No physical deletes per wa-patch-instruction [current] §5.4 (deletion discipline).*

### 3.5 Element 5 — COMPLETION CONFIRMATION

The exact query or check Claude Code must run and return to close the directive. See §6 for the confirmation standard.

Example:
> *Return the following two queries and their results:*
> *1. `SELECT COUNT(*) FROM wa_verse_records vr JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id WHERE ti.delete_flagged = 1 AND vr.delete_flagged = 0 AND vr.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = 97);`*
> *   Expected: 0*
> *2. `SELECT COUNT(*) FROM wa_verse_records vr JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id WHERE ti.delete_flagged = 1 AND vr.delete_flagged = 1 AND vr.obsolete_reason = 'orphaned verse — parent term delete_flagged';`*
> *   Expected: 11 (or the count determined by CC in step Scope)*

---

## 4. Directive Structure — Template

Directives are markdown documents. The template below is the canonical structure; the five elements appear in the order specified.

```markdown
# Directive {DIR-YYYYMMDD-NNN} — {short title}

> Produced by: wa-directive-instruction-v1_0-20260418
> Governed by: wa-global-general-rules-v2_11-20260418
> Registry: {registry_no or 'global'}
> Produced date: {YYYY-MM-DD}
> Researcher approval: {PENDING | APPROVED {date}}

---

## Motivation

{Element 2 — why this change is needed, what problem it solves, evidence}

---

## Scope

{Element 3 — tables, records, fields affected; selection criteria}

---

## Outcome required

{Element 4 — exact database state after execution}

---

## Completion confirmation

{Element 5 — queries or checks CC must return, with expected results}

---

## Notes

{Optional — any context CC needs: related patches, dependencies, known anomalies, handoff to subsequent work}
```

---

## 5. Directive Production Workflow

### 5.1 Step 1 — Identify the task

Claude AI determines that a directive (rather than a patch) is the right method per §1.

### 5.2 Step 2 — Draft the five elements

Produce the markdown document per §4 template. Each element must be complete before the next begins — do not write Motivation and defer Scope.

### 5.3 Step 3 — Self-check (§7)

Run the self-check protocol. Record the result in the observations log:
```
Directive self-check DIR-{YYYYMMDD}-{NNN}: [PASS / FAIL — element missing if FAIL]
```

### 5.4 Step 4 — Submit for researcher approval

Present the directive to the researcher with a brief one-line summary. Researcher reviews and approves or returns for revision.

### 5.5 Step 5 — Hand off to Claude Code

After approval, Claude AI states:
```
DIRECTIVE SUBMISSION TO CLAUDE CODE
Directive file: wa-{registry}-{word}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md
Directive ID: DIR-{YYYYMMDD}-{NNN}
Action required: Execute per directive. Return completion confirmation per §5 of the directive.
```

### 5.6 Step 6 — Receive completion confirmation

CC returns the confirmation output per §6. Claude AI reviews against expected outcome. If it matches, the directive is closed. If it does not, the operation is not complete — diagnose and respond.

### 5.7 Step 7 — Record outcome

Observations log entry:
```
DIR-{YYYYMMDD}-{NNN} closed — CC returned {confirmation summary}. Outcome matches expected.
```

Or, if failed:
```
DIR-{YYYYMMDD}-{NNN} failure — CC returned {actual}. Expected {expected}. Diagnosis: {...}. Next step: {...}.
```

---

## 6. Completion Confirmation (absorbed from GR-DIR-005)

Every directive specifies the completion confirmation that Claude Code must return. This parallels wa-patch-instruction [current] §6 for patches; the principle is the same.

### 6.1 What counts as confirmation

A specific query result, row count, or field state check. Not a general acknowledgement. Not "directive executed" — that is activity confirmation, not completion confirmation. Completion confirmation verifies the outcome against what was required.

### 6.2 What Claude Code returns

CC runs the confirmation queries specified in Element 5 of the directive and returns the results verbatim. Example:

```
DIR-20260418-001 executed.
Completion confirmation:

Query 1: SELECT COUNT(*) FROM wa_verse_records vr
         JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
         WHERE ti.delete_flagged = 1 AND vr.delete_flagged = 0
         AND vr.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = 97);
Result: 0

Query 2: SELECT COUNT(*) FROM wa_verse_records vr
         JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
         WHERE ti.delete_flagged = 1 AND vr.delete_flagged = 1
         AND vr.obsolete_reason = 'orphaned verse — parent term delete_flagged';
Result: 11
```

### 6.3 What Claude AI does with it

Reviews against Element 4 (Outcome required). If outcomes match: directive is closed. If not: not complete — diagnose and respond. The researcher is kept in the loop — CC returns the confirmation to both Claude AI and the researcher.

### 6.4 When the directive cannot be executed as stated

If CC inspects the database and determines the directive cannot be executed exactly as stated — because DB state differs from what the motivation assumes, or because a prerequisite has changed — CC does not improvise. CC returns the divergence to Claude AI and the researcher with the evidence, and awaits further instruction.

Example:
```
DIR-20260418-001 halted before execution.
Scope query returned 0 rows, not the expected 11.
The orphaned-verse condition described in the Motivation is not present in the current DB state.
Possible explanations: [1] issue already resolved by prior work; [2] registry number
changed; [3] filter criterion mismatched.
Awaiting Claude AI review.
```

---

## 7. Directive Self-Check (absorbed from GR-DIR-008)

Before presenting any directive for researcher approval, Claude AI verifies all five elements are present and complete. Self-check result is recorded in the observations log.

### 7.1 The five checks

1. **DIRECTIVE ID** — present, in format `DIR-YYYYMMDD-NNN`
2. **MOTIVATION** — states why the change is needed and what problem it solves; specific, not generic
3. **SCOPE** — identifies which tables, records, or fields are affected
4. **OUTCOME REQUIRED** — states the required database state precisely enough for CC to verify
5. **COMPLETION CONFIRMATION** — specifies the exact query or check CC must run and return, with expected results

### 7.2 Filename check

Directive filename follows §2.1 pattern (lowercase, compact date, versioned, within the 20-character description limit).

### 7.3 A directive missing any element must not be submitted

Claude AI corrects the directive and re-checks all five elements. Submitting an incomplete directive is a compliance failure.

### 7.4 Self-check statement format

Record in observations log:
```
Directive self-check DIR-{YYYYMMDD}-{NNN}: [PASS / FAIL — element missing if FAIL]
```

---

## 8. Claude Code Receipt and Execution

Reciprocal to §7 self-check — if CC receives a directive that fails §7 self-check (element missing, malformed), CC reports the missing elements rather than executing.

### 8.1 CC receipt validation

On receiving a directive file, CC validates:
1. Filename pattern per §2.1
2. Five elements present and non-empty
3. Researcher approval confirmed per GR-PROC-004

If any validation fails: CC reports the specific failure and does not execute.

### 8.2 CC execution

If validation passes, CC:
1. Reads the directive in full
2. Inspects the database to determine the exact operations per the Scope and Outcome Required elements
3. Executes the operations — applying the no-physical-deletion rule per wa-patch-instruction [current] §5.4
4. Runs the completion confirmation queries from Element 5
5. Returns the results to Claude AI and the researcher per §6

### 8.3 CC halts before execution if divergence is detected

Per §6.4 — if CC inspection reveals the DB state does not match what Motivation describes, CC halts and reports. Does not improvise.

### 8.4 CC does not make analytical judgements

CC applies the directive. CC does not extend scope, interpret ambiguity, choose between options, or apply judgement about whether the outcome is desirable. Those are Claude AI's responsibilities. A directive that requires analytical judgement by CC is a malformed directive — CC reports the gap back to Claude AI.

---

## 9. Failure Path

When a directive cannot be executed, fails mid-execution, or returns an unexpected confirmation, the following path applies.

### 9.1 Pre-execution failure

CC receipt validation fails (§8.1):
- CC reports which of the five elements is malformed or missing
- Claude AI corrects the directive and resubmits
- No observations log entry of "failure" unless the pattern recurs

### 9.2 Execution halt (divergence detected)

CC inspection reveals DB state does not match the directive's premise (§6.4):
- CC reports the divergence with evidence (queries run, results)
- Claude AI diagnoses and either: (a) produces a revised directive; (b) determines the directive is no longer needed; (c) escalates to the researcher
- Observations log records the divergence and resolution

### 9.3 Mid-execution failure

CC begins execution but encounters an error:
- CC halts. Any transactional changes are rolled back if possible.
- CC reports: stage reached, error encountered, DB state at halt
- Claude AI diagnoses; if the directive caused DB state corruption, produce a REPAIR patch per wa-patch-instruction [current] §9 before proceeding
- Observations log records the failure, the recovery steps, and the outcome

### 9.4 Unexpected confirmation

CC returns completion confirmation but the results do not match the Outcome Required:
- Treat as execution halt per §9.2
- Not a CC failure — CC ran the queries as specified; the mismatch is an analytical issue for Claude AI to resolve

### 9.5 Recovery — same directive or new directive

For trivial corrections (typo in query, wrong table name): revise and resubmit with next version (`v2`) of the same directive filename. The `DIRECTIVE ID` increments to the next sequence.

For substantive corrections (premise wrong, scope wrong): close the current directive with a failure note in the observations log; produce a new directive with a new `DIRECTIVE ID`.

---

## 10. Relationship to Patches

Patches and directives are not competing methods — they complement each other across different task types (§1).

A session may produce both. Pattern:
1. **Directive** to investigate and remediate a one-off condition (e.g. orphan verses)
2. **Patch** to implement the outcome as a structured, auditable transaction once the scope is known

For example: a Verse Context re-run scenario uses:
- A **REPAIR patch** (wa-patch-instruction [current] §9.3) to reset status and delete_flag the affected records — structured, all fields known in advance
- A **directive** may follow if the post-repair state reveals an anomaly that needs bespoke remediation

Patches are the primary mechanism. Directives are the remediation-and-investigation mechanism. When in doubt, prefer patches; directives exist because some tasks genuinely cannot be specified as patches in advance.

---

*wa-directive-instruction-v1_1-20260418 | Supersedes wa-directive-instruction-v1_0-20260418 | Prior (v1_0): consolidated global rules addenda ADD-PATCHDIR-002, -003, -005, -006, -008, -009 | Resolved addendum ADD-PATCHDIR-002 (directive peer specification)*
