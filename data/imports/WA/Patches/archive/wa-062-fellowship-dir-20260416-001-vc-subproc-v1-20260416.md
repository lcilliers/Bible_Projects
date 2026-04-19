# WA — CC Directive: Verse Context Sub-Process
**Registry 062 — fellowship**
Filename: wa-062-fellowship-dir-20260416-001-vc-subproc-v1-20260416.md
Date: 2026-04-16
Issued by: Claude AI — wa-sessionb-analysis-readiness-v1-20260416.md Step 1.5 Trigger 3
Requires researcher approval before execution.
Previous output: PATCH-20260416-062-PREANALYSIS-V1.json (apply that patch first — see sequencing note below)

---

## Purpose

During Session B Stage 1 Analysis Readiness for Registry 062 (fellowship), Step 1.2 Section B Cross-check B2 identified four active OWNER terms that have active verse records in the database but no `verse_context_group` records. These terms have not been through Verse Context classification. Per the Analysis Readiness instruction (Step 1.5 Trigger 3), a targeted Verse Context sub-process is required for these four terms before Stage 2 can proceed.

This directive instructs CC to construct a targeted Verse Context batch JSON for exactly these four terms, enabling Claude AI to perform classification. Claude AI will then produce a VERSECONTEXT patch; CC applies it and confirms.

---

## Sequencing Note

**Apply PATCH-20260416-062-PREANALYSIS-V1.json before executing this directive.**

That patch contains two operations (H2269 delete_flagged correction; G2842 phase2_flag soft-delete). Neither operation affects the four terms in scope here, but the patch must be applied and confirmed before this directive is executed so that the database is in a clean state when the batch JSON is constructed.

---

## Terms in Scope

These are the four active OWNER terms for registry 062 that have verse records but no verse_context_group records:

| strongs_number | transliteration | mti_term_id | occurrence_count | verse_records (active) |
|---|---|---|---|---|
| H2271 | chab.bar | 7572 | 1 | 1 |
| H2279 | cho.ve.ret | 7570 | 4 | 3 |
| H4225 | mach.be.ret | 7571 | 8 | 7 |
| H4226 | me.chab.be.rah | 7426 | 2 | 2 |

**Note on verse record counts:** The verse record counts above are from the export dated 20260416. CC must confirm active verse record counts from the live database before constructing the batch, in case any changes occurred between export and batch construction.

---

## Step 1 — Pre-construction Verification

Before constructing the batch JSON, CC must verify:

1. Confirm that PATCH-20260416-062-PREANALYSIS-V1.json has been applied. Specifically: confirm `wa_term_inventory.delete_flagged = 1` for H2269 (term_inv_id=7733).

2. For each of the four terms — H2271, H2279, H4225, H4226 — confirm:
   - `mti_terms.status IN ('extracted', 'extracted_thin')` for each term
   - `wa_term_inventory.delete_flagged = 0` and `term_owner_type = 'OWNER'` for each term
   - At least one `wa_verse_records` row with `delete_flagged = 0` for each term
   - Zero existing `verse_context_group` records for each `mti_term_id`
   - Zero existing `verse_context` records for each `mti_term_id`

3. Confirm no other active OWNER terms for registry 062 exist without verse_context_group records beyond these four. (These should be the only four — this is a confirmation check.)

Report the results of Step 1 before proceeding to Step 2. If any check fails, halt and report to researcher before continuing.

---

## Step 2 — Batch JSON Construction

Construct a targeted Verse Context batch JSON for the four terms using the format specified in WA-VerseContext-Instruction-v2.7-20260414.md Section 5.3.

**Batch parameters:**
- This is a **targeted sub-process batch** — it covers exactly the four specified terms only. It is not a programme-wide batch accumulation.
- Batch ID: assign the next available VCB batch ID from the programme sequence (query `max(batch_id)` from existing VCB records or the batch log to determine the next ID).
- If a batch ID sequence table or log is not available, use the naming pattern `VCB-062-SUB-001` to distinguish this as a registry-targeted sub-process batch.
- `existing_groups`: for each of the four terms, this array will be **empty** (no prior groups exist).
- Include all active verse records for each term (`wa_verse_records.delete_flagged = 0`).
- Include full verse text in `verse_text` field.
- Include `target_word` (the specific word form in the verse) from `wa_verse_records`.
- Include `span_strong_match` value (may be NULL for some records — include as-is; Claude AI is aware of the NULL span_strong_match gap from Path 3 Note 005).

**Output file:** `wa-vcb-{batch_id}-extract-{date}.json`
Deliver to Claude AI for classification.

---

## Step 3 — Claude AI Classification

Claude AI will receive the batch JSON and classify all verses for the four terms under WA-VerseContext-Instruction-v2.7-20260414.md.

Claude AI will produce:
- A VERSECONTEXT patch file: `wa-vcb-{batch_id}-patch-v1-{date}.json`
- An observations file: `wa-vcb-{batch_id}-term-observations-v1-{date}.md`

This directive does not govern the classification step — that is Claude AI's responsibility under the VC instruction.

---

## Step 4 — Patch Application and Verification

After Claude AI produces the VERSECONTEXT patch:

1. Apply the patch per WA-VerseContext-Instruction-v2.7-20260414.md Section 8 (patch application procedure).

2. After application, verify each of the four terms:
   - At least one `verse_context_group` record exists for each `mti_term_id`
   - At least one `verse_context` record with `is_anchor = 1` exists for each group
   - Group codes follow the format `{mti_term_id}-{serial}`
   - No `verse_context_group` records have `delete_flagged = 1` for these terms (unless explicitly set in the patch)

3. Run the consistency rules check per VC instruction Section 2.3 (R1–R4) for all new records.

4. **Do not** advance `word_registry.verse_context_status` for registry 062 as a result of this sub-process alone. The verse_context_status will be confirmed by Claude AI in Step 1.6 of Analysis Readiness after the fresh export is produced. CC should leave `verse_context_status` at its current value ('Complete') — this sub-process adds groups for previously unclassified terms within an already-Complete registry.

   **Note on verse_context_status:** Registry 062 already has `verse_context_status = 'Complete'`. The four terms were missed in the original VC run. Once their groups are created and the patch is applied, the status remains 'Complete' — the sub-process is a gap-fill, not a reset.

---

## Step 5 — Fresh Export

After the VERSECONTEXT patch is confirmed applied and the four terms are verified as having groups:

1. Re-export the complete word data for registry 062:
   ```
   python -m engine.engine --export --registry=62
   ```
   (or the equivalent export command for the programme's current export script)

2. Record the new export version number and export date.

3. Deliver the fresh export to Claude AI. This export becomes the working extract for Step 1.6 (Stage 1 Completion Verification) and Stage 2.

---

## Step 6 — Confirmation Report

CC must confirm the following to Claude AI before Step 1.6 begins:

```
DIRECTIVE wa-062-fellowship-dir-20260416-001-vc-subproc — EXECUTION REPORT

Pre-construction verification: [PASS / FAIL — detail if FAIL]

Batch constructed: [batch_id] — [n] terms, [n] verse records
Batch JSON file: [filename]

VERSECONTEXT patch applied: [patch filename] — [n] operations
Post-application verification:
  H2271 (mti_id=7572): [n] group(s) created, [n] anchor(s)
  H2279 (mti_id=7570): [n] group(s) created, [n] anchor(s)
  H4225 (mti_id=7567): [n] group(s) created, [n] anchor(s)
  H4226 (mti_id=7571): [n] group(s) created, [n] anchor(s)

Consistency rules R1–R4: [PASS / FAIL per rule]
verse_context_status (registry 062): [value — should remain 'Complete']

Fresh export produced: [filename] — version [n] — exported [date]
```

This confirmation is required before Claude AI proceeds to Step 1.6.

---

## Governing Instructions

- WA-VerseContext-Instruction-v2.7-20260414.md (CC roles: Sections 5, 8, 13, 14)
- wa-sessionb-cc-instructions-v3_3-20260414.md
- wa-global-general-rules-v2_2-20260415.json

**GR-OBS-005:** No physical deletes. All record retirements via `delete_flagged = 1` only.
**GR-DATA-001:** All queries against mti_terms must include `AND mt.status IN ('extracted', 'extracted_thin')`.
**GR-PROC-003/004:** No changes applied without researcher approval. This directive requires researcher sign-off before execution.

---

*wa-062-fellowship-dir-20260416-001-vc-subproc-v1-20260416.md*
*Issued by Claude AI — Analysis Readiness Step 1.5 Trigger 3*
*Status: PENDING researcher approval*
