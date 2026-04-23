# wa-prose-draft-033-patch-failure-v1-20260421

> Framework B Soul Word Analysis Programme — Draft Prose Body
> Target section_type_id: 33 (`prog_patch_failure_protocol`)
> Target label: Programme — Patch Failure / REPAIR Protocol
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-draft-029-validation-standard-v1-20260421
> Governed by: wa-directive-instruction-v1_2-20260421 §10.4; wa-patch-instruction-v2_3-20260421 §3, §9

---

## Change Control — v1

| Change | Section |
|---|---|
| New document. First-pass draft of the `prog_patch_failure_protocol` prose body, authored from memory per researcher direction in message 4 of session `prose`. Confidence markers applied inline. | All |

---

## Drafting notes — read first

This draft is authored **from memory**. Confidence markers: **[M]** confident; **[M?]** partially reconstructed; **[GAP]** source needed.

The draft is the proposed body text. Heading and PROSE patch envelope in the final sections.

---

## Proposed heading

`Patch Failure and REPAIR Protocol`

---

## Proposed body (draft v1 — memory-first)

### What this protocol governs

Patches are the programme's primary mechanism for mutating the database (wa-patch-instruction [current] §1.1). They are designed to be idempotent, auditable, and safe to re-apply. But patches fail — through malformation, through applicator errors, through mismatched database state, through partial application in a multi-patch pool. When they fail, the programme needs a protocol that preserves two things: the integrity of the database and the integrity of the audit trail. This record specifies that protocol. **[M]**

Patch failure is not a category of shame; it is a normal operational occurrence. The discipline is that failures are recorded, diagnosed, and recovered from in structured ways — not swept under the rug or silently re-run until they appear to succeed. **[M]**

### Where patches fail

A patch can fail at three distinct points, each with a different failure signature and recovery path.

**1. Receipt validation failure.** The patch is rejected before execution begins. CC receipt validation (filename pattern, `_patch_meta` completeness, `patch_type` in vocabulary, `session_b_status` conformance, `total_operations` matching `operations.length`) rejects malformed patches. No DB change occurs; the failure is detected before any mutation. Recovery: Claude AI corrects the patch, increments the version, and resubmits. **[M]**

**2. Applicator execution failure.** The patch passes receipt validation but fails during apply. Common causes: a CHECK constraint violation (e.g. `status` value not in the allowed enum), a FK mismatch (e.g. `section_type_id` references a non-existent row), a NOT NULL violation (e.g. programme-wide prose against the unrelaxed `registry_id` — the exact scenario that produced wa-directive-instruction-v1_2 §10), a UNIQUE constraint violation (e.g. duplicate `patch_id`). The applicator runs each patch in a transaction; a failed operation mid-patch triggers rollback, so the DB state is preserved. CC reports the specific operation that failed, the error, and the rolled-back state. **[M]**

**3. Confirmation mismatch.** The patch applies without error; the completion confirmation queries return values that do not match what was expected. This is not an applicator failure — the applicator did what the patch said. It is an analytical failure: the patch did not implement what Claude AI intended. Recovery is analytical, not mechanical: Claude AI diagnoses the gap between the applied state and the intended state, and issues a correcting patch or directive. **[M]**

### The failure patch

When a patch fails at any of the three points, the failure itself is recorded as an artefact. **[M]**

The failure record captures: the failing `patch_id`; the failure point (receipt / applicator / confirmation); the error reported by CC (verbatim); the DB state at the moment of failure (the rollback target); the diagnosis produced by Claude AI; the remediation taken (corrected patch, REPAIR patch, directive, or close-without-recovery). **[M?]**

*[M? — I am confident the failure record exists as a discipline. I am less confident about its exact storage location. Two possibilities I can recall: (a) an entry appended to the observations log for the session in which the failure occurred; (b) a dedicated table (possibly `wa_patch_failure_log` or similar). Source verification needed — I can see this being either a process discipline or a schema-backed record.]*

*[GAP — specific schema/location for the failure record, if any.]*

### The REPAIR patch

REPAIR is a named patch type (wa-patch-instruction [current] §3.3, §9) used for recovery operations. A REPAIR patch is distinct from a correction patch in one crucial respect: correction patches are normal patches that happen to follow a failure; REPAIR patches are pre-specified cascade reset operations, drawn from a catalogue. **[M]**

The REPAIR catalogue contains cascade reset types — each type knows which fields to reset, which statuses to revert, which delete flags to clear or set. A REPAIR patch invokes a type from the catalogue for a specific scope (a registry, a verse context batch, a cluster). Because the cascade types are pre-specified, REPAIR patches are auditable in a way that ad-hoc correction patches are not: the catalogue is versioned, the reset logic is reviewable outside the context of any particular failure, and the effect of the patch is predictable. **[M]**

Common REPAIR types (from memory — exact names may vary): **[M?]**
- **VC-rerun reset** — revert a registry's verse_context state to pre-classification so the VCB pass can be re-run cleanly.
- **Dimension-review reset** — revert dimension assignments to their KEYWORD_WEAK/KEYWORD_STRONG starting state so review can begin again.
- **Session-B-status revert** — undo a premature session_b_status advancement. **[M?]**

*[GAP — exact catalogue of REPAIR types. wa-patch-instruction §9 is the canonical source; I recall the concept and representative examples, not the full catalogue.]*

A REPAIR patch is the preferred recovery mechanism when the failure affects data state that fits a catalogued reset. When it does not, a correction patch (normal SESSIONB, PREANALYSIS, VERSECONTEXT etc. with corrective operations) is used instead. **[M]**

### Mid-pool recovery

Verse Context processing, Dimension Review, Session B readiness sweeps, and other high-volume activities apply patches in pools — sequences of related patches applied across registries or batches. When a patch fails partway through a pool, the recovery question is: where in the pool did the failure occur, what is the DB state now, and how does the remainder of the pool proceed? **[M]**

The discipline has three parts:

1. **Halt.** CC stops the pool at the failure point. Subsequent patches in the pool are not applied. Nothing runs past the halt point until the failure is diagnosed. **[M]**

2. **Inventory.** CC reports which patches applied successfully, which failed, and which have not yet been attempted. The researcher and Claude AI know the exact pool state. No partial state is invisible. **[M]**

3. **Resume or replay.** After diagnosis: (a) resume from the next unapplied patch if the failure is isolated and the prior applies are sound; (b) roll back the applied patches via REPAIR and replay the full pool if the failure implies the applied patches also have the flaw; (c) redesign the pool if the failure reveals a systemic problem. **[M]**

The pool as a unit has a status — running, halted, resumed, complete, abandoned. The status is recorded in the observations log; it is not inferred from the individual patch outcomes. **[M?]**

*[M? — the named pool statuses are my reconstruction. The principle that the pool has a status distinct from the patches is confident; the exact labels are less so.]*

### Why the protocol matters

The protocol exists because patch failure, unmanaged, produces the programme's worst failure mode: a database that has been partially mutated with no clear record of which parts are current and which are stale. A verse_context batch that half-applied, a Session B status advanced for some registries and not others, a dimension review half-reset — each would silently corrupt downstream analysis. **[M]**

The protocol's purpose is to make every failure visible, recorded, and recoverable — so that failures become events the programme works through, not invisible holes the programme works around. **[M]**

---

## Body word count (approximate)

Approximately 830 words excluding headings. `word_count` to be validated at patch time.

---

## Confidence summary for researcher

| Marker | Count | Note |
|---|---|---|
| [M] | 16 sentences/clauses | Confident from memory |
| [M?] | 3 sentences/clauses | Partially reconstructed — verification recommended |
| [GAP] | 2 substantive gaps | Source needed to close |

The two [GAP] items are:
1. Storage location of the failure record (observations log vs. dedicated table).
2. Exact REPAIR catalogue — the full list of reset types with their scopes.

Both can be closed by access to wa-patch-instruction-v2_3 §9 (I have parts of this in the loaded instruction — I can do a second pass against it if desired).

---

## Patch record envelope (for PROSE patch construction — after body approval)

| Field | Value |
|---|---|
| `table` | `prose_section` |
| `operation` | `insert` |
| `registry_id` | `null` |
| `section_type_id` | `33` (from extract; `prog_patch_failure_protocol`) |
| `heading` | `Patch Failure and REPAIR Protocol` |
| `body` | (approved body text) |
| `word_count` | (calculated) |
| `status` | `draft` |
| `version` | `1` |
| `author` | `claude_ai` |
| `source_file` | `wa-prose-draft-033-patch-failure-v1-20260421.md` |

---

## What the researcher needs to decide

1. **Body approved as-is / with edits / rejected.**
2. **Close [GAP] 1** — is the failure record stored in the obslog, or in a dedicated table? If a table, what is its name?
3. **Close [GAP] 2** — confirm the REPAIR catalogue. I can read wa-patch-instruction-v2_3 §9 (already loaded) as a self-serve second pass if you'd prefer — just say the word.
4. **Confirm the [M?] reconstructions** — "Accepted as-is" label, REPAIR type names, pool status labels.

---

## Authorship flag on item 7's structure

Item 7 was a candidate for splitting into two records (protocol vs. REPAIR catalogue; see obslog). This draft merges both into one record because the REPAIR catalogue reads better as a component of the protocol than as a standalone reference. If on review you find the catalogue section (currently "The REPAIR patch") should live in its own prose record, the split is clean — that section would become a new record against a new `prose_section_type` (e.g. `prog_repair_catalogue`), and the remaining content of this record would stand without it.

---

*wa-prose-draft-033-patch-failure-v1-20260421 | First draft, memory-first per session `prose` message 4*
