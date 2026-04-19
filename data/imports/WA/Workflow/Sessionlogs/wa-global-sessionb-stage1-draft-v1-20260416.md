# WA — Session B Instruction: Stage 1 Replacement Text
## For incorporation into wa-global-sessionb-instruction-v5_1-20260416.md
**Filename:** wa-global-sessionb-stage1-draft-v1-20260416.md
**Date:** 2026-04-16
**Version:** v1.0
**Replaces:** Stage 1 Steps 1.3, 1.4, 1.5, 1.6 from wa-global-sessionb-instruction-v5_0-20260415.md
**Retains unchanged:** Stage 1 Purpose block; Step 1.1; Step 1.2
**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_8-20260416.md (T-02)
- wa-global-sessionb-instruction-v5_0-20260415.md (source)
- wa-global-sessionlog-sessionb-redesign-v1-20260416.md (design reasoning)

---

## Change Summary

The following changes are made to Stage 1 from v5.0:

1. **Step structure updated.** Old Steps 1.3 (Inherited Flag Review) and 1.4 (wa_term_phase2_flags Audit) are replaced by three sub-steps: 1.3a, 1.3b, and 1.3c. All flag-related preparation operations are grouped together under Step 1.3.
2. **Step 1.3a** — `wa_term_phase2_flags` audit (was Step 1.4 — moved earlier and made a sub-step).
3. **Step 1.3b** — `wa_session_b_findings` preparation (new — links existing findings to catalogue questions; data preparation only, no analytical work).
4. **Step 1.3c** — `wa_session_research_flags` B-target clearance (replaces old Step 1.3 — now a hard gate with explicit resolution actions).
5. **Step renumbering.** Old Step 1.5 (Type (a) patch) → Step 1.4. Old Step 1.6 (Sub-process triggers and fresh extract) → Step 1.5.
6. **Step 1.2 prior-phase findings check updated.** The findings count and anomaly check in Step 1.2 is retained; the note that findings are "not resolved in Stage 1" is updated to reflect that Step 1.3b prepares them for Stage 2 without performing analysis.
7. **RESEARCHER_DECISION block** now collected after all three sub-steps of Step 1.3 are complete, before patch construction.

Steps 1.1 and 1.2 are otherwise unchanged from v5.0 except for the Step 1.2 findings note (item 6 above).

---

## Full Replacement Text

---

## Stage 1 — Data Audit and Remediation

### Purpose

Stage 1 makes the data complete, correct, and ready for analysis before Stage 2 begins. No step in Stage 2 begins until Stage 1 is fully complete and a fresh extract is confirmed. This is a hard gate — per integrity rule SB-1.

**Stage 1 role:** Data validation and preparation only. Stage 1 confirms the data is sound, classifies existing findings and flags, and ensures all pre-conditions for analysis are met. Stage 1 does not perform analysis, draw analytical conclusions, or build narrative. That is Stage 2.

Stage 1 has five sequential steps:

```
Step 1.1 — Confirm extract version
Step 1.2 — Read and audit the complete JSON
Step 1.3 — Prepare existing records (three sub-steps)
        Step 1.3a — wa_term_phase2_flags: assess all advisory term flags
        Step 1.3b — wa_session_b_findings: prepare existing findings for Stage 2
        Step 1.3c — wa_session_research_flags: clear all B-target flags (hard gate)
Step 1.4 — Type (a) patch construction and application
Step 1.5 — Sub-process triggers and fresh extract
```

RESEARCHER_DECISION items raised during any step are accumulated and presented as a discrete numbered block after Step 1.3c is complete — before patch construction begins. Stage 2 does not begin until all RD items from Stage 1 are resolved.

---

### Step 1.1 — Confirm Extract Version

Per GR-DB-001 and GR-DATA-004. Before reading any data:

1. State the filename of the complete word data export attached to this session.
2. Request from CC: confirm this is the current version of the extract for registry [nnn] and return the version identifier and export date.
3. Wait for CC confirmation. If CC returns a different version as current — stop. The attached extract is stale. Request the current version before proceeding.
4. Record in observations log: `Extract confirmed: [filename] — version [n] — exported [date].`

Do not proceed until extract version is confirmed.

---

### Step 1.2 — Read and Audit the Complete JSON

Read the complete word data export in full. For each section of the JSON, work through the audit checklist below. Record every gap, anomaly, or concern in the observations log at the moment of discovery — per GR-OBS-001.

**Audit checklist — registry fields:**

| Field | Check |
|-------|-------|
| `word`, `registry_no`, `cluster` | Present and correct |
| `session_b_status` | Should be at the expected stage entry point |
| `verse_context_status` | Must be `Complete` before Stage 1 can proceed |
| `dimensions` | Populated — at least one dimension present |
| `sb_classification` | May be NULL at this stage |
| `carry_forward` | Default 1 — note if 0 |

**Audit checklist — terms:**

For each term in the extract:

| Check | Action if gap found |
|-------|-------------------|
| `status` is populated | Note as gap — requires classification decision |
| `evidential_status` is populated | Note as gap — requires Stage 2 work |
| `god_as_subject` value | Per GR-DATA-005: do not trust — verify against verses in Stage 2 |
| `somatic_link` value | Per GR-DATA-005: do not trust — verify against verses in Stage 2 |
| Verse count > 0 for OWNER terms | Zero-verse OWNER term is a data gap — flag |
| `strongs_number` format | Must be clean (no embedded spaces, correct prefix H/G) |

**Audit checklist — verse context groups:**

| Check | Action if gap found |
|-------|-------------------|
| All OWNER terms have at least one group | Missing groups trigger Verse Context sub-process |
| Each group has a description | Blank description is a gap — note |
| Each group has at least one anchor verse | No anchor is a gap — note |
| `dominant_subject` populated on all dimension index rows | Missing triggers Dimension Review sub-process consideration |

**Audit checklist — dimension assignments:**

| Check | Action if gap found |
|-------|-------------------|
| All groups have a dimension assignment | Unassigned group triggers Dimension Review sub-process |
| All assignments at `CLAUDE_AI` or `RESEARCHER` confidence | `AUTOMATED` confidence is a data gap — triggers Dimension Review sub-process |
| No dimension assignment contradicts the group description | Contradiction — note in observations log |

**Audit checklist — existing findings count:**

Request from CC: return count of `wa_session_b_findings` rows for this registry where `delete_flag = 0`.

Record in observations log: `Prior-phase findings for registry [nnn]: [n] active findings.`

This count is for situational awareness only. Findings are not reviewed or dispositioned in Step 1.2. That is Step 1.3b.

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
2. Construct the patch per the patch specification (`wa-patch-specification-v[current]`).
3. Name the patch: `PATCH-[YYYYMMDD]-[nnn]-PREANALYSIS-V1.json`
4. State patch contents in the observations log: `Stage 1 Type (a) patch constructed. [n] operations covering: [brief list of operation types].`

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

### Step 1.5 — Sub-Process Triggers and Fresh Extract

**Sub-process triggers:** If Step 1.2 identified gaps requiring a full Verse Context or Dimension Review sub-process, those sub-processes run now — after the Type (a) patch is confirmed but before the fresh extract is pulled.

- **Verse Context sub-process:** Triggered if any OWNER term has zero verse context records, or if verse context groups are missing or malformed. Load `wa-versecontext-instruction-v[current].md` and run the sub-process. Do not proceed until the sub-process is complete and its own patch is confirmed.
- **Dimension Review sub-process:** Triggered if any group has `AUTOMATED` confidence dimension assignment, or if any group has no dimension assignment. Load `wa-dimensionreview-instruction-v[current].md` and run the sub-process. Do not proceed until the sub-process is complete and its own patch is confirmed.

If no sub-processes are triggered: record `Step 1.5: no sub-process triggers identified. Proceeding to fresh extract.`

**Fresh extract:** After all Stage 1 patches and any sub-processes are confirmed, request from CC: re-export the complete word data for registry [nnn] and return the new version identifier.

Record in observations log: `Fresh extract confirmed: [filename] — version [n] — exported [date]. Stage 1 complete.`

**Stage 2 does not begin until the fresh extract is confirmed.** Per integrity rule SB-1.

---

## Integrity Rules Affected by This Change

The following integrity rules from v5.0 are updated or added:

| Rule | Status | Updated text |
|---|---|---|
| SB-1 | Unchanged | Stage 2 does not begin until Stage 1 is fully complete and the fresh extract is confirmed |
| SB-18 | Updated | Zero open `wa_session_research_flags` rows for this registry with `session_target = 'B'` and `resolved = 0` at Step 1.4 completion — hard gate. Verified by CC count query after patch application. |
| SB-19 | Unchanged | No RESEARCHER_DECISION item may be raised without evidence that GR-RD-001 steps 1–6 have been completed |
| SB-20 (new) | New | Every active `wa_session_b_findings` row for this registry must have either (a) a `wa_finding_catalogue_links` row with `status` in ('suggested', 'validated') or (b) an observations log entry confirming it needs a new question in Stage 2b — before Step 1.4 patch construction begins. Per Step 1.3b integrity check. |
| SB-21 (new) | New | Stage 1 does not perform analysis. Any step in Stage 1 that requires analytical judgement — assessing the significance of a finding, drawing a conclusion about a word's meaning, evaluating a theological claim — must be deferred to Stage 2. A clear record of what was deferred and why must be in the observations log. |

---

*End of wa-global-sessionb-stage1-draft-v1-20260416.md*
*For incorporation into wa-global-sessionb-instruction-v5_1-20260416.md*
*Supersedes Steps 1.3, 1.4, 1.5, 1.6 from wa-global-sessionb-instruction-v5_0-20260415.md*
