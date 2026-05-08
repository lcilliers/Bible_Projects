# wa-directive-instruction-v1_4-20260506

> Framework B Soul Word Analysis Programme — Directive Preparation and Execution
> Version: v1_4 | Date: 20260506
> Supersedes: wa-directive-instruction-v1_3-20260422.md (v1_0 consolidated addenda; v1_1 applied GR-REF-002 sweep; v1_2 added §10 Schema enablement directives; v1_3 tightened the directive-vs-patch boundary for prose lifecycle operations; v1_4 adds §11 Cluster-process directives — registry is no longer the dominant analytical scope; directives now operate primarily at cluster / sub-group / cluster_finding scope; cluster-level filename pattern added at §2.3; §1.1 typical scenarios extended; §3.3 SCOPE example extended with a cluster pattern)
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

## Change Control — v1_4

| Change | Section |
|---|---|
| New §11 — **Cluster-process directives**: pattern for directives operating on `cluster`, `cluster_subgroup`, `cluster_finding`, and on `verse_context_group` rows scoped to a cluster's terms. Registry is no longer the dominant analytical scope; cluster has become the primary analytical axis (per the term-anchor reset of 2026-05-04 and the M06 cluster pass of 2026-05-06). The new section makes cluster-process directives a first-class pattern alongside §10 schema enablement. | §11 (new) |
| §11 includes worked patterns from DIR-20260506-001 (sub-group assignment + cluster reassignment) and DIR-20260506-002 (cluster findings recording). The five-element format is unchanged; what changes is the typical scope, table set, and outcome verifications. | §11 |
| §1.1 typical directive scenarios — added "Cluster process change — assigning sub-groups, reassigning terms across clusters, recording cluster findings, repairing cluster-internal inconsistencies." Cluster-process directives are the most common form going forward; registry-scope directives remain valid for word-level work but are no longer the default. | §1.1 |
| §2 Filename Convention — new §2.3 cluster-level pattern: `wa-cluster-{cluster_code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md`. Existing §2.1 registry pattern is now legacy / for word-level work; existing §2.2 programme pattern is unchanged. Renumber: previous §2.3 (Directive ID) becomes §2.4. | §2.3 (new), §2.4 |
| §3.3 SCOPE element — second worked example added showing a cluster-scope directive (sub-group reassignment) alongside the registry-scope orphan-verse example. The two examples make explicit that scope can be registry, cluster, sub-group, or programme-wide. | §3.3 |
| §11 (Relationship to Patches) renumbered to §12; cluster-process row added to its worked-examples table. | §12 |
| Footer updated. | footer |

### Prior change control — v1_3

| Change | Section |
|---|---|
| §1.1 typical directive scenarios — "Schema enablement" entry expanded with a hard boundary: schema enablement directives are the ONLY prose-lifecycle operation that goes through a directive; all other prose work (handle creation, content insert, supersede, approve, delete) goes through patches per wa-patch-instruction [current] §14. Routing table added to make the decision explicit. | §1.1, §1.5 (new) |
| New §1.5 — Prose-lifecycle routing table, with explicit DO / DO NOT entries | §1.5 |
| §10 tightened — §10.2 worked pattern for `registry_id NOT NULL` relaxation retained; §10.5 "when this pattern recurs" enumerated with concrete examples for future prose-adjacent schema changes; §10.7 (new) — "What a directive MUST NOT do for prose" stating the hard exclusions (handle content, body revisions, status transitions, soft-deletes, approvals) | §10.5, §10.7 |
| §11 "Relationship to Patches" — prose lifecycle row added to the worked examples table pointing to wa-patch-instruction [current] §14 | §11 |

### Prior change control — v1_2

| Change | Section |
|---|---|
| New §10 — Schema enablement directives: the pattern for directives that prepare the schema for a class of patches that cannot apply against the current schema; programme-wide prose worked pattern included (resolves the registry_id NOT NULL blocker) | §10 |
| §10 adds §10.1 background, §10.2 programme-wide prose enablement directive (five-element worked content), §10.3 the DDL approach for SQLite NOT NULL removal (CREATE-copy-RENAME + FTS rebuild), §10.4 post-directive PROSE patch pattern, §10.5 when this pattern recurs | §10 |
| §10 renumbered from v1_1 (Relationship to Patches) becomes §11; footer updated | §11, footer |
| §1.1 typical directive scenarios — added "schema enablement — preparing the DB for a class of patches that the current schema cannot accept (see §10)" | §1.1 |
| GR-REF-002 operational cross-references retained | Throughout |

### Prior change control — v1_1

Operational cross-references migrated to `[current]` token per GR-REF-002 — frontmatter, §1, §6, §7, §8-equivalent areas. Inline references updated: `wa-patch-instruction v2_0` (4 occurrences in §1, §6, §7, §8) → `[current]`; rule-version reference `global rules v2_11` in §1 → `[current]`. Provenance preserved: footer consolidation line; `Produced by` field illustration in §4 template. v1_0 Change Control retained below for provenance.

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

- **Cluster-process change** — assigning sub-groups within a cluster, reassigning terms across clusters, recording cluster-level findings, repairing cluster-internal inconsistencies, applying group/verse mappings produced by the catalogue analysis. This is the most common directive form going forward (see §11). Cluster-process directives operate on `cluster`, `cluster_subgroup`, `cluster_finding`, and on `verse_context_group`/`verse_context` rows scoped to a cluster's terms.
- Investigating a data anomaly where the fix is obvious but the affected rows must be discovered first
- Cleaning up orphaned records where the selection criteria are clear but the exact IDs are not known
- Running a maintenance operation whose scope depends on current DB state
- Producing a report that requires CC to compose queries across multiple tables
- One-off remediation where a structured patch would be disproportionate overhead
- **Schema enablement** — preparing the DB for a class of patches that the current schema cannot accept (see §10). This is the only prose-related scenario where a directive is correct. Every other prose operation is a patch — see §1.5.

> **Note on registry scope.** Prior to the term-anchor reset of 2026-05-04, registry was the dominant analytical scope for directives. From v1_4 onward, **cluster** is the primary analytical scope; the registry-scope filename pattern (§2.1) and registry-scope examples in this document remain valid for word-level work (Session B/C/D for individual words) but are no longer the default. New cluster-process directives use the §2.3 pattern.

### 1.2 When a patch is the right tool

Use a patch (wa-patch-instruction [current] §1.1) when Claude AI is certain of the field names, FK keys, table structure, and exact operations. Patches are machine-readable, idempotent, and auditable.

### 1.3 Choice in borderline cases

When a task could be done either way, the default is patch if the scope is well-bounded and the operations are known. Directive if the scope requires DB inspection to resolve.

Where in doubt, Claude AI raises the choice to the researcher as a direction/principle question (GR-HF-001 permitted minimum — one clarifying question).

### 1.4 Common rules (both methods)

- Researcher approval before Claude Code acts — per GR-PROC-004
- Stated completion confirmation — per §6 below for directives; wa-patch-instruction §6 for patches
- No conversational bypass — instructions outside patch or directive format are not valid

### 1.5 Prose-lifecycle routing — do this / do not do this

The prose store (`prose_section_type`, `prose_section`, `prose_section_fts`, `prose_section_dimension_link`, `prose_section_finding_link`) has three distinct change surfaces, routed to three distinct methods. The routing is **fixed and unambiguous** — it is not a judgement call, and AI must not improvise by choosing a different method.

| Change | Method | Authoritative document | Rationale |
|---|---|---|---|
| Add a column to `prose_section` or `prose_section_type` | **Directive** (schema enablement) | This document §10 | DDL; the applicator does not do DDL. |
| Relax / tighten a constraint on a prose table | **Directive** (schema enablement) | This document §10 | DDL. |
| Create a new prose-adjacent table | **Directive** (schema enablement) | This document §10 | DDL. |
| Add a new section-type handle (`prose_section_type` row) | **CATALOGUE_POPULATION patch** | wa-patch-instruction [current] §14.2.1 | Data insert. |
| Edit a section-type handle (label / description / chapter_no / sort_order / lifecycle) | **CATALOGUE_POPULATION patch** | wa-patch-instruction [current] §14.2.2 | Data update. |
| Add a new prose body (`prose_section` row) | **PROSE patch** | wa-patch-instruction [current] §14.3 | Data insert. |
| Revise an existing prose body | **PROSE patch** (`supersede`) | wa-patch-instruction [current] §14.4 | Data insert + update chain. |
| Move prose to a different handle | **PROSE patch** (`supersede` with explicit `section_type_id` in `record`) | wa-patch-instruction [current] §14.6 | Data insert + update chain. |
| Approve a draft (single or batch) | **PROSE patch** (`approve`) | wa-patch-instruction [current] §14.5.1 | Status transition. |
| Retire prose | **PROSE patch** (`delete`, soft) | wa-patch-instruction [current] §14.5.2 | Soft-delete flag. |

**DO NOT do any of the following:**

- ❌ Produce a directive to insert prose content — even one prose body. Use a PROSE patch.
- ❌ Produce a directive to fix a typo or revise a prose body. Use a PROSE patch with `supersede`.
- ❌ Produce a directive to approve, mass-approve, or retire prose. Use a PROSE patch.
- ❌ Produce a directive to add or rename a section-type handle. Use a CATALOGUE_POPULATION patch.
- ❌ Mix schema enablement and data changes into a single directive. Schema enablement directives are scoped narrowly; data changes follow in one or more patches afterwards.
- ❌ Mix handle changes and content changes in a single patch. A CATALOGUE_POPULATION patch contains only `prose_section_type` operations; a PROSE patch contains only `prose_section` operations.

**If a prose-lifecycle task does not appear in the table above,** the default is a PROSE patch, and Claude AI raises one clarifying question to the researcher (GR-HF-001) before producing either a directive or a patch. The scenarios in the table are exhaustive for the programme's current prose architecture.

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

For directives not tied to a single registry **or** a single cluster (e.g. schema enablement that affects multiple tables, or cross-cluster remediation), use `global` as the reference segment per GR-FILE-006:

```
wa-global-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md
```

Example: `wa-global-dir-001-schema-cleanup-v1-20260418.md`

### 2.3 Cluster-level directives (new in v1_4)

For directives whose scope is a single cluster (`cluster_code` matches one row in `cluster`) — assigning sub-groups, reassigning terms, applying group/verse mappings, recording cluster findings, repairing cluster-internal state:

```
wa-cluster-{cluster_code}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md
```

| Component | Content |
|---|---|
| `{cluster_code}` | Cluster identifier (e.g. `M06`, `M28`, `T2`, `FLAG`) |
| `dir` | Fixed token |
| `{seq}` | Zero-padded 3-digit sequence within the session for that cluster (`001`, `002`, …) |
| `{description}` | Short lowercase descriptor of purpose, max 20 characters, no spaces |

Examples:

- `wa-cluster-M06-dir-001-subgroup-assign-v1-20260506.md`
- `wa-cluster-M06-dir-002-findings-record-v1-20260506.md`
- `wa-cluster-M06-dir-003-mapping-apply-v1-20260506.md`
- `wa-cluster-M28-dir-001-term-rebind-v1-20260507.md`

The cluster-level pattern is **preferred** for cluster-process directives. The `wa-global-dir-...` pattern with the cluster code embedded in the description (e.g. `wa-global-dir-001-m06-subgroup-assign-...`) was used in early M06 work and remains valid as legacy, but new directives should use §2.3.

When a directive spans multiple clusters (e.g. a cross-cluster term migration), use the §2.2 `global` pattern with a description that names the affected clusters.

### 2.4 Directive ID

Independent of filename. Used as internal reference in observations logs and completion confirmations:

```
DIR-{YYYYMMDD}-{NNN}
```

Where `NNN` is a 3-digit sequence within the date. Example: `DIR-20260418-001`. Uppercase retained by convention (parallel to `patch_id`).

---

## 3. Directive Format — Five Required Elements

Every directive contains exactly these five elements. A directive missing any element is malformed — see §7 for self-check and §8 for CC rejection behaviour.

### 3.1 Element 1 — DIRECTIVE ID

Unique identifier in format `DIR-YYYYMMDD-NNN` per §2.4.

### 3.2 Element 2 — MOTIVATION

Why this change is needed and what problem it solves. Specific. Not "general cleanup"; name the actual issue, the evidence that it exists, and why it must be addressed now.

Example:
> *Eleven verse records are orphaned — their `term_inv_id` points to a `wa_term_inventory` row that was delete_flagged when the term was reclassified as bleed. The orphan records are being returned by the verse-count query and inflating the reported verse count for registry 097. The registry's session_b_status cannot advance to Ready for Analysis while the verse count is wrong.*

### 3.3 Element 3 — SCOPE

Which tables, records, or fields are affected. Specific enough that CC can determine the query to run — not exhaustive enough to require CC analytical judgement.

Scope can be at registry, cluster, sub-group, or programme-wide level. Both worked examples are valid forms — pick the one that matches the task.

**Example A — registry-scope (legacy / word-level work):**
> *Table: `wa_verse_records`.*
> *Criterion: `term_inv_id` pointing to a row in `wa_term_inventory` where `delete_flagged = 1`.*
> *Registry filter: `wa_file_index.word_registry_fk = 97` (registry 097 only).*
> *Expected count: approximately 11 — exact count to be determined by CC.*

**Example B — cluster / sub-group scope (new in v1_4, the dominant pattern):**
> *Tables: `mti_terms` (column `cluster_subgroup_id`), `verse_context_group` (description), `verse_context` (`group_id`, `is_anchor`, `analysis_note`).*
> *Cluster scope: `mti_terms.cluster_code = 'M06'` AND `cluster_subgroup_id` resolved via `cluster_subgroup.subgroup_code = 'M06-A'`.*
> *Term set: 5 Strong's — H8130, H8131, H8135, H4895, H7852 — listed in the directive.*
> *Operation: assign per-(verse, term) entries to the groups named in the source mapping document; create new `verse_context_group` rows where the source designates `M06-A-NEW-XX`; update group descriptions for retained groups; set `is_anchor = 1` on the named anchor verses.*
> *Expected counts: 49 verses retained in group 1601 after migration; 9 + 16 + 17 + 13 verses migrated to four new groups; 10 dual-assignment second rows inserted.*

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

## 10. Schema Enablement Directives (new in v1_2)

A schema enablement directive is a directive whose purpose is to prepare the database schema for a class of patches that the current schema cannot accept. The pattern was established by DIR-20260421-001 (three new columns on `wa_rule_registry` to support the four-field rule structure, which the wordy-restructure RULES patch depended on) and is formalised here for re-use.

### 10.1 When a schema enablement directive is needed

A schema enablement directive is required when:
- Claude AI has drafted (or is about to draft) a patch whose `insert` / `update` values cannot be written into the existing schema — typically because a column is NOT NULL but has no valid value for the new rows, or a column does not yet exist, or a CHECK / FK constraint rejects the values.
- The remedy is a structural change that no patch operation covers (applicator patches touch data, not schema).
- The change is narrow, specific, and reversible (a single-column add, a constraint relaxation, a new index) — not a whole-table redesign.

If the schema change is broad (restructuring multiple tables, introducing new FK relationships, or changing type widths across the DB), the change goes through an engine migration (`engine/migrate.py`), not a directive. Schema enablement directives are for localised preparatory work only.

### 10.2 Worked pattern — programme-wide prose

**Background.** M34 (2026-04-19) seeded eight `prose_section_type` rows with `source_stage = 'programme'` to support programme-wide prose. The schema of `prose_section` was not updated at the same time; the column `registry_id INTEGER NOT NULL REFERENCES word_registry(id)` remains. Programme-wide prose rows have no registry — `NOT NULL` blocks the insert. No reserved `word_registry` row exists as a workaround.

**The gap is structural, not data.** A PROSE patch attempting `registry_id = NULL` will fail on the NOT NULL constraint. Any patch attempting a sentinel value (e.g. `registry_id = 0`) will fail the FK because no such row exists. The remedy is to relax the NOT NULL constraint so that `registry_id IS NULL` signals programme-wide scope — matching how `prose_section_type.source_stage = 'programme'` already signals it at type level.

**Schema enablement directive — five elements for this case.**

| Element | Content |
|---|---|
| DIRECTIVE ID | `DIR-{YYYYMMDD}-{NNN}` — next in sequence |
| MOTIVATION | `prose_section.registry_id` is `NOT NULL`. M34 introduced programme-stage prose section types (`source_stage = 'programme'`, 8 rows, all without a registry). An `insert` on `prose_section` for these types with `registry_id = NULL` fails the NOT NULL constraint; no reserved `word_registry` row exists for programme-wide use. The PROSE patch that will populate the eight programme-stage sections cannot apply against the current schema. |
| SCOPE | Table: `prose_section`. Column: `registry_id`. Change: drop `NOT NULL`; retain FK `REFERENCES word_registry(id)`. No other columns, constraints, or indexes changed. Companion: `prose_section_fts` (FTS5 virtual table) must be rebuilt because it is keyed to `prose_section.rowid`. Rows affected: zero (`prose_section` is empty at directive time). |
| OUTCOME REQUIRED | After execution, `prose_section.registry_id` is nullable TEXT-compatible (nullable INTEGER), FK `REFERENCES word_registry(id)` retained, all other columns and constraints preserved. FTS5 companion rebuilt and re-populated from `prose_section` (0 rows in, 0 rows out, contents preserved). Row count on `prose_section` unchanged. A subsequent `INSERT INTO prose_section (registry_id, section_type_id, body, ...) VALUES (NULL, ?, ?, ...)` succeeds. |
| COMPLETION CONFIRMATION | Three queries: (1) `PRAGMA table_info(prose_section)` — `registry_id` row shows `notnull = 0`. (2) `SELECT sql FROM sqlite_master WHERE name = 'prose_section'` — DDL shows the FK on `registry_id` is preserved and the NOT NULL is removed. (3) `SELECT name FROM sqlite_master WHERE name = 'prose_section_fts'` — FTS5 virtual table still exists. Optional (4): a test insert + immediate rollback to verify `registry_id = NULL` is accepted. |

### 10.3 DDL approach for this directive (SQLite-specific)

SQLite does not support `ALTER TABLE ... DROP NOT NULL`. The standard pattern is:

1. `BEGIN TRANSACTION`
2. Create `prose_section_new` with the relaxed constraint — same columns, same FKs, same CHECK constraints, `registry_id INTEGER REFERENCES word_registry(id)` (no NOT NULL).
3. `INSERT INTO prose_section_new SELECT * FROM prose_section` — preserves any data (0 rows currently).
4. Drop `prose_section` (this also drops triggers that reference it, if any).
5. Rename `prose_section_new` to `prose_section`.
6. Rebuild `prose_section_fts` — drop and recreate the FTS5 virtual table, then populate from `prose_section`. (If `prose_section` has 0 rows at directive time, population is a no-op; still rebuild the virtual table to ensure it is keyed to the new `prose_section.rowid` sequence.)
7. Recreate any indexes or triggers that were attached to the original table.
8. `COMMIT`.

The directive specifies the outcome (§10.2 Outcome Required). CC decides the DDL path — the CREATE-copy-RENAME sequence above is the expected one. If CC discovers the table has non-trivial triggers or dependent views at execution time, CC halts and reports per §6.4.

### 10.4 Post-directive PROSE patch pattern

After the directive is applied and confirmed, the PROSE patch(es) for programme-wide prose use `registry_id = NULL`. Example:

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-PROSE-PROGRAMME-V1",
    "patch_type": "PROSE",
    "session_b_status": null,
    "produced_by": "wa-claudeai-session-programme-prose-{date}",
    "researcher_approval": "PENDING",
    "motivation": "Populate the 8 programme-stage prose sections seeded in M34."
  },
  "operations": [
    {
      "op_id": "OP-001",
      "table": "prose_section",
      "operation": "insert",
      "record": {
        "registry_id": null,
        "section_type_id": {id of prog_anchor_verse},
        "heading": "Anchor Verse Definition",
        "body": "...",
        "word_count": 180,
        "status": "draft",
        "version": 1,
        "author": "claude_ai",
        "source_file": "research/investigations/programme-prose-session-bundle-v1-20260421.md"
      }
    }
    // ... 7 more operations for the other programme-stage section types
  ]
}
```

The patch is structured per wa-patch-instruction [current] §3.3 (RULES/PROSE patch types) and §2.4 (programme-wide filename pattern: `wa-prose-programme-{topic}-v{n}-{YYYYMMDD}.json`).

### 10.5 When the pattern recurs

Schema enablement directives are expected whenever a new class of patch is introduced that the schema does not yet accept. Examples that would use this pattern:

- A new analytical field on `wa_term_inventory` that a Session B extractor will begin populating (add column; then the SESSIONB patch can write it).
- A new section type category in `prose_section_type` that needs a column on `prose_section` it doesn't currently have.
- A CHECK constraint relaxation (e.g. broadening `status` enum) when new status values are introduced.

In each case: one directive, narrow scope, five elements specified per §3. The directive is independent and auditable. The patch class it enables follows in a separate transaction.

### 10.6 What this pattern is NOT

- Not a substitute for an engine migration when the schema change is broad or affects many tables. Migrations are for programme-wide structural work; directives are for localised enablement.
- Not a way to bypass researcher approval of schema changes — a schema enablement directive still requires GR-PROC-004 approval before CC executes.
- Not a way to perform destructive schema changes (dropping a column with data, changing a column type in a way that truncates existing rows). Those need explicit researcher instruction and typically a migration path.

### 10.7 Directives must NOT carry prose data changes

A schema enablement directive for the prose tables **must not** include operations that write, change, or retire prose data. The enablement directive is scoped to DDL only. Data operations follow in subsequent patches, per the routing in §1.5.

Hard exclusions — a directive must NOT:

- ❌ Insert, update, supersede, or delete any `prose_section` row.
- ❌ Insert, update, or soft-retire any `prose_section_type` row.
- ❌ Transition any prose row's status (draft / in_review / approved / archived).
- ❌ Populate `prose_section_dimension_link` or `prose_section_finding_link`.
- ❌ Rebuild `prose_section_fts` beyond what is required to preserve FTS integrity across the DDL change itself (a no-op rebuild when the table is empty; or an explicit re-index only if the DDL broke the FTS companion).

If CC receives a directive that mixes schema enablement with data operations, CC halts per §8.1 and reports the mix back to Claude AI. Claude AI splits the work into:
1. A directive containing only the DDL elements.
2. One or more patches (per wa-patch-instruction [current] §14) containing the data operations, applied after the directive's completion confirmation is returned and reviewed.

This split discipline preserves two guarantees: (a) schema changes are independently auditable without being tangled with content; (b) data operations can be retried, rolled back, or corrected without re-doing the DDL.

---

## 11. Cluster-process Directives (new in v1_4)

A cluster-process directive is a directive whose scope is a single cluster (or a small set of related clusters). The pattern was established by the M06 cluster pass of 2026-05-06 (DIR-20260506-001 sub-group assignment, DIR-20260506-002 findings recording, plus the M06-A group-verse mapping apply) and is formalised here for re-use across all clusters going forward.

### 11.1 Why this is a distinct pattern

Cluster-process work has properties that differ from the legacy registry-scope pattern:

- The unit of analysis is the **characteristic** (the cluster — e.g. M06 Hate, Contempt and Hostility) rather than the individual word. A cluster typically draws terms from many registries.
- The DB tables touched are predominantly `mti_terms.cluster_code` / `cluster_subgroup_id`, `cluster_subgroup`, `cluster_finding`, and `verse_context_group` / `verse_context` rows scoped to the cluster's terms — not the registry-scoped `wa_file_index` / `wa_session_b_findings` tables.
- The analytical artefacts (sub-group mappings, catalogue-prompt findings, anchor-verse designations) are produced by Claude AI's cluster pass and require precise CC operations to land in the database without losing the analytical fidelity.
- Cluster-process directives are now the **most common** directive form. Schema enablement (§10) and registry-scope clean-ups remain valid, but the cluster pattern dominates day-to-day work.

### 11.2 When to use a cluster-process directive

Use this pattern when the change scope is one cluster's analytical state:

- **Sub-group assignment / reassignment** — recording the sub-group structure within a cluster (M06-A through M06-G + BOUNDARY in M06's case), and assigning each term in the cluster to a sub-group via `mti_terms.cluster_subgroup_id`.
- **Cluster reassignment** — moving a term from one cluster to another (e.g. H6887E and H7520 from M06 to M28). Updates `mti_terms.cluster_code`. Companion rows in `cluster_subgroup` and `cluster_finding` may need cleanup.
- **Group-verse mapping apply** — applying a Claude AI mapping document that revises group descriptions, creates new groups, migrates verses between groups, designates anchor verses, and records per-verse observations as `analysis_note`. Touches `verse_context_group` and `verse_context`. (See worked pattern 11.4.)
- **Cluster findings recording** — loading the catalogue-prompt analytical pass into `cluster_finding` (one row per prompt × scope; statuses `finding`, `silent`, `gap`, `cluster_synthesis`). See worked pattern 11.5.
- **Cluster-internal repair** — fixing dual-anchor inconsistencies, orphaned group rows, mis-attributed verses within a cluster.
- **Gap resolution** — running the DB queries needed to resolve `cluster_finding` rows flagged with `finding_status = 'gap'` and updating them to `finding` with the resolved text.

### 11.3 Five-element form for cluster-process directives

The five elements (DIRECTIVE ID / MOTIVATION / SCOPE / OUTCOME REQUIRED / COMPLETION CONFIRMATION) are the same. Cluster-specific guidance for each element:

- **MOTIVATION** — name the cluster, the analytical pass that produced the artefact, the source document(s) Claude AI used, and the observed gap or required change. Cite the obslog session reference (e.g. `wa-obslog-M06-m06-method-v1-20260506`).
- **SCOPE** — name the cluster_code and (if applicable) the sub-group. Identify the tables. Use the cluster-scope example pattern in §3.3 Example B.
- **OUTCOME REQUIRED** — state the expected `cluster_subgroup` row counts, `cluster_finding` row counts, and per-table state. Where verse-context migrations are involved, state the expected verse counts per group post-migration.
- **COMPLETION CONFIRMATION** — queries that count rows by `cluster_code` and by `cluster_subgroup_id`, plus a sample query showing 3–5 representative rows. Where applicable, include a "no inappropriate writes" check (e.g. `wa_session_b_findings` row count unchanged for cluster-process directives).

### 11.4 Worked pattern A — group-verse mapping apply (M06-A precedent)

**Background.** Claude AI produces a mapping document (e.g. `WA-M06-A-group-verse-mapping-v1-20260506.md`) for one sub-group of a cluster, listing for each existing or new `verse_context_group`: the description, the anchor verse, the verses to assign, the per-verse observation text, and any cross-group dual assignments.

**Five-element form (representative content):**

| Element | Content |
|---|---|
| DIRECTIVE ID | `DIR-{YYYYMMDD}-{NNN}` |
| MOTIVATION | The M06-A sub-group has been analytically reviewed against the catalogue and the consolidated mapping document `WA-M06-A-group-verse-mapping-v1-20260506.md`. The mapping (a) revises descriptions of groups 1601, 3590, 1199, 1201, 1602; (b) introduces 4 new conceptual groups (M06-A-NEW-01..04); (c) migrates verses from legacy groups to new groups; (d) records 10 cross-group dual assignments; (e) designates anchor verses. The mapping must land in the database to enable the cluster's findings analysis to proceed. |
| SCOPE | Cluster: `M06`. Sub-group: `M06-A` (5 terms — H8130, H8131, H8135, H4895, H7852). Tables: `verse_context_group` (UPDATE descriptions × 5; INSERT new × 5), `verse_context` (UPSERT primary memberships, INSERT secondary memberships for dual assignments, set `is_anchor=1` on anchors and clear stale anchors first). Set-asides not re-evaluated unless explicitly re-included in the mapping. |
| OUTCOME REQUIRED | 5 existing groups have refreshed descriptions; 5 new `verse_context_group` rows (one per H8130 + one per H8131 for NEW-04 split); per-group verse counts match doc expectations (49 in 1601, 9 in NEW-01, 16 in NEW-02, 17 in NEW-03, 13 in NEW-04, etc.); each group has exactly one `is_anchor=1` row matching the doc-named anchor; 10 dual-assignment second rows present in `verse_context`; legacy 1601 rows for verses migrated to NEW-XX have been soft-deleted; set-aside rows untouched. |
| COMPLETION CONFIRMATION | (1) `SELECT group_code, COUNT(*) FROM verse_context vc JOIN verse_context_group vcg ON vcg.id=vc.group_id WHERE vcg.mti_term_id IN (550, 1663, 902, 903, 5518) GROUP BY group_code` — verse counts per group match expected. (2) Anchor count per group = 1 for each of the named anchors. (3) Cross-group dual count: 10 (vr_id, mti_id) pairs with >1 group_id. (4) Set-aside row count unchanged (sample by mti_term_id). (5) Application report saved to `Sessions/Session_Clusters/M06/WA-M06-A-group-mapping-applied-v1-{date}.md`. |

The directive's source document is the Claude AI mapping (`.md`), not a JSON patch — CC parses the structured markdown, validates against the DB, and applies. Pre-flight checks (every verse reference resolvable, every group_id matches term, etc.) are mandatory; halt-on-error before any write.

### 11.5 Worked pattern B — cluster findings recording (DIR-20260506-002 precedent)

**Background.** Claude AI completes a 189-prompt × 7-sub-group catalogue pass for a cluster (e.g. M06) and produces a consolidated findings document. Each (prompt × scope) cell carries an outcome code (E evidenced / S silent / G gap) and finding text.

**Path A — table exists.** If `cluster_finding` (post-M45) already covers the requirement, CC parses the consolidated findings and UPSERTs rows. One row per (`obs_id`, `cluster_code`, `cluster_subgroup_id`, `version`); `finding_status` ∈ (`finding`, `silent`, `gap`, `cluster_synthesis`); `finding_text` is the verbatim prose paragraph from the source.

**Path B — schema gap.** If the DB lacks a cluster-level findings mechanism, the cluster-process directive **halts** and produces a schema enablement directive (§10) instead. The data-write follows once the schema is enabled.

**Five-element form (representative content):**

| Element | Content |
|---|---|
| DIRECTIVE ID | `DIR-{YYYYMMDD}-{NNN}` |
| MOTIVATION | The {cluster} catalogue pass has produced 189 prompts × 7 sub-groups + cluster-level synthesis findings documented in `WA-{cluster}-consolidated-findings-v{n}-{date}.md`. The findings need to be recorded in `cluster_finding` so they are queryable, linked to `wa_obs_question_catalogue.obs_id`, and available for cross-cluster synthesis. |
| SCOPE | Table: `cluster_finding`. Cluster: `{cluster_code}`. Source files: 4 parts of the consolidated findings document. Operations: UPSERT one row per (prompt × scope), parsing `**T#.#.#** — ...` headers and `**[X]** ...` / `**[CLUSTER]** ...` / `**S — [...]**` / `**G — [...]**` markers. Catalogue prompts identified by `question_code`. Sub-groups identified by `subgroup_code`. |
| OUTCOME REQUIRED | One row in `cluster_finding` per source-document marker. `finding_status` set per marker type. `finding_text` set to verbatim prose. `source_file` set to part-N filename. Cells the source did not separately address remain at `[Sub-group not separately addressed in source ...]` stub with `finding_status='finding'`. No `wa_session_b_findings` rows written (cluster findings live in `cluster_finding`). |
| COMPLETION CONFIRMATION | Row count by status: `SELECT finding_status, COUNT(*) FROM cluster_finding WHERE cluster_code='{cluster}' GROUP BY finding_status`. Sample: 3 representative rows with `question_code` and excerpt. Gap list: every `finding_status='gap'` row with its `question_code`, scope, and excerpt — for follow-up CC query work. Confirmation that `wa_session_b_findings` row count is unchanged. |

### 11.6 Worked pattern C — cluster reassignment

**Background.** A term is in the wrong cluster. The fix moves it to the correct cluster_code, possibly clears its `cluster_subgroup_id`, and may require updating `cluster_subgroup` rows that referenced it.

**Five-element form (compact):**

- **MOTIVATION** — name the term(s), the wrong cluster, the correct cluster, and the analytical reason for the reassignment.
- **SCOPE** — `mti_terms.cluster_code` for the named Strong's; `mti_terms.cluster_subgroup_id` if it was set; any `cluster_subgroup` rows owned by the term that need de-listing or migration.
- **OUTCOME REQUIRED** — post-update `cluster_code` values; cluster row counts before/after; sub-group counts before/after.
- **COMPLETION CONFIRMATION** — `SELECT cluster_code, COUNT(*) FROM mti_terms WHERE strongs_number IN (...)` for the affected terms; cluster-row counts for both source and destination clusters.

### 11.7 What cluster-process directives MUST NOT do

- ❌ Mix cluster-process changes with schema changes. Schema goes through §10. Mixing them violates the audit-separation guarantee.
- ❌ Touch `wa_session_b_findings` to record cluster-level findings. That table is registry-scope; cluster findings live in `cluster_finding`.
- ❌ Re-evaluate set-aside `verse_context` rows unless the source mapping document explicitly re-includes them (per the M06 precedent's decision 4 — set-asides are not re-evaluated absent explicit re-inclusion).
- ❌ Operate at programme scope under the §2.3 cluster pattern. Cross-cluster work uses §2.2 `global` filename.
- ❌ Improvise scope. The cluster_code, sub-group, and term set are stated explicitly in the directive; CC executes against that exact set.

### 11.8 Recurrence — every cluster goes through this pattern

The 47 named-characteristic clusters (M01..M46 plus T2 and FLAG) will each be processed via cluster-process directives over time. Per-cluster directive sequence:

1. Sub-group assignment (one directive per cluster — a single `dir-001`).
2. Group-verse mapping apply (one directive per sub-group — typically `dir-002` upward).
3. Cluster findings recording (one directive per cluster — typically the highest-numbered `dir-NNN`).
4. Gap resolution (may be folded into the findings directive's Notes or run as a follow-up).

Each cluster has its own `wa-cluster-{cluster_code}-dir-{seq}-...` filename sequence, independent of other clusters' sequences. Sequence numbers reset per cluster.

---

## 12. Relationship to Patches

Patches and directives are not competing methods — they complement each other across different task types (§1).

A session may produce both. Pattern:

1. **Directive** to investigate and remediate a one-off condition (e.g. orphan verses), **or** to enable a schema change before a patch class can apply (§10).
2. **Patch** to implement the outcome as a structured, auditable transaction once the scope is known.

For example: a Verse Context re-run scenario uses:
- A **REPAIR patch** (wa-patch-instruction [current] §9.3) to reset status and delete_flag the affected records — structured, all fields known in advance
- A **directive** may follow if the post-repair state reveals an anomaly that needs bespoke remediation

For programme-wide prose (§10.2):

- A **schema enablement directive** to relax the `prose_section.registry_id` NOT NULL constraint
- A **CATALOGUE_POPULATION patch** to insert new section-type handles (wa-patch-instruction [current] §14.2)
- A **PROSE patch** with `registry_id = NULL` to populate the programme-stage sections (wa-patch-instruction [current] §14.3)
- A **PROSE patch** with `approve` (batch `ids: [...]`) once the researcher has reviewed (wa-patch-instruction [current] §14.5.1)

For any subsequent prose-lifecycle change (adding, revising, approving, retiring), **only patches** — no further directive is needed. Schema enablement directives are a one-off per class of change, not a repeat step for each prose revision.

For cluster-process work (§11), the directive form dominates because the operations require DB inspection (resolving Strong's → mti_id, group_code → group_id, parsing structured AI mapping documents) that patches cannot pre-specify. Cluster-process directives are not one-off; each cluster will produce a sequence of them (sub-group assignment → mapping apply → findings recording → gap resolution).

Worked examples — when each method applies:

| Task | Method | Pattern |
|---|---|---|
| Orphan-record cleanup (registry-scope) | Directive | §3 base form |
| Schema column add / constraint relax | Directive | §10 schema enablement |
| Cluster sub-group assignment | Directive | §11.4 / §11.6 |
| Cluster findings recording (catalogue pass) | Directive | §11.5 |
| Cluster gap resolution | Directive (lightweight) | §11.2 |
| Insert / revise / approve a prose body | Patch (PROSE) | §1.5 routing |
| Add / edit a section-type handle | Patch (CATALOGUE_POPULATION) | §1.5 routing |
| Bulk DB write where every value is known | Patch | wa-patch-instruction |

Patches are the primary mechanism for known data writes. Directives are the remediation-and-investigation mechanism, the schema enablement mechanism (§10), **and the cluster-process mechanism (§11)**. When in doubt, prefer patches; directives exist because some tasks genuinely cannot be specified as patches in advance.

---

*wa-directive-instruction-v1_4-20260506 | Supersedes wa-directive-instruction-v1_3-20260422 | Prior (v1_3): §1.5 prose routing + §10.7 hard exclusions | Prior (v1_2): §10 Schema enablement directives | Prior (v1_1): GR-REF-002 sweep | Prior (v1_0): consolidated global rules addenda ADD-PATCHDIR-002, -003, -005, -006, -008, -009 | v1_4 adds §11 Cluster-process directives — registry is no longer the dominant analytical scope; cluster has become the primary axis (per term-anchor reset 2026-05-04 and M06 cluster pass 2026-05-06); cluster-level filename pattern at §2.3; SCOPE example extended in §3.3*
