# WA-SessionLog-InstructionUpdates-v1-20260330

**Project:** Framework B — Soul Word Analysis Programme
**Session date:** 2026-03-30
**Session type:** Gap analysis update and instruction document updates
**Continues from:** WA-SessionLog-FieldAnalysis-v1-20260329.md
**Produced by:** Claude AI

---

## 1. Session Objective

Two declared tasks:
1. Produce WA-InstructionGaps-v2 — fresh IP-based gap register from instruction documents
2. Apply all pending instruction updates from previous session decisions

A third task emerged mid-session: apply researcher decisions from uploaded comments on the gap report.

---

## 2. Documents Available This Session

| Document | Version | Source |
|---|---|---|
| WA-SessionLog-FieldAnalysis-v1 | v1 | Uploaded (session continuation) |
| WA-InstructionGaps-v1 | v1 | Uploaded |
| WA-SessionLog-InflectionPointFixes-v1 | v1 | Uploaded |
| WA-SessionB-Analysis-Instruction | v5.3 | Uploaded |
| WA-SessionB-Extraction-Instruction | v5.4 | Uploaded |
| WA-Registry-Management-Guide | v5.5 | Uploaded (zip) |
| WA-SessionB-DataPrep-Instruction | v5.4 | Uploaded (zip) |
| WA-VerseContext-Instruction | v1.2 | Uploaded (zip) |
| WA-SessionB-ClaudeCode-Instructions | v3 | Uploaded (zip) |
| patch_specification | v1.4 | Uploaded (zip) |
| WA-Reference | v5.3 | Uploaded |
| WA-InstructionGaps-v2-researcher-comments | — | Uploaded (researcher annotations) |

---

## 3. Work Completed This Session

### 3.1 Gap register — fresh IP-based analysis

All instruction documents were read in full. Inflection points were identified from scratch by locating every DB read and DB write in the pipeline. 27 IPs identified; 34 gaps assessed.

**Cross-gap consistency corrections applied before document updates:**
- G22 closed — Reference v5.3 Section 4.3 confirmed to exist with dimensions vocabulary
- G25/IP-XP-01 closed — patch_specification Section 6 confirms overwrite behaviour; idempotency not an issue
- G15/G26 description corrected — bulk_update IS in patch_specification v1.4 Section 3.10a; the gap is that the operation should be removed from the Analysis patch, not that it is undefined
- G06 clarified — Ready for Analysis is set by audit_word (COALESCE), not by VerseContext; DataPrep gates on verse_context_status only

### 3.2 Researcher decisions received and applied (from uploaded comments)

| Decision | Resolution |
|---|---|
| SQL policy | SQL queries and scripts are Claude Code's responsibility. Claude AI instructions need only provide field names, table names, derivation rules, and expected outcomes plus a clear handoff. Where these are present, the gap closes. Closes G01, G08, G07, G10 by policy. |
| G05 — all-verses-fail | This scenario should never happen. If it occurs, it is an error condition. Claude AI must stop and flag to researcher with term details and reasons. |
| G02 — partial completion | Partial completion (term_classification_complete = false with existing records) is an error — not a continue-from-prior scenario. Must be flagged to researcher; batch fixed and resubmitted. |
| G03 — revision criterion | When revision is clearly warranted, Claude AI must document reasons in notes field and report to researcher in per-term summary. Not a silent reclassification. |
| G04 — grouping criterion | New group warranted when context is materially different — meaning an analysis would arrive at a differential conclusion about how the inner-being characteristic operates. Criteria: different way the term serves the inner being; different verse context; variation changes or enhances how the characteristic operates (parties, function, influences, other characteristics). |
| G06 escalation | Pipeline status lifecycle is a holistic gap requiring a dedicated review. Not resolvable by a single note. New gap G06-NEW raised. |
| G13 | Closed per yesterday's session decisions — clarification note applied in DataPrep v5.5. |
| G14 — threshold | Approximately 9 words. Subject to empirical revision. Recorded as working threshold. |
| G10 | RMG Section 7a is confirmed sufficient for pool membership without schema change. |
| Q-F (G30) | extracted_theological_anchor treated as extracted — no reclassification needed. Applied in DataPrep v5.5. |

### 3.3 Document updates produced

**First wave (pending decisions from 2026-03-29 session):**

| Document | Version | Key changes |
|---|---|---|
| WA-SessionB-Analysis-Instruction | v5.4 | Section 12: bulk_update removed; 2-operation patch template; researcher checkpoint rule |
| WA-SessionB-Extraction-Instruction | v5.5 | OWNER-only rule; Group F (dimensions + description); Section 8.1 derivation rules; Annexure B updated; pool_observations file-only note |
| WA-Reference | v5.4 | Engine-derived fields note; redundant fields documented |
| WA-Registry-Management-Guide | v5.6 | Section 2: engine-derived fields note |
| WA-VerseContext-Instruction | v1.3 | Section 13.3: Ready for Analysis clarification; Section 13.4: batch completion summary; Section 6.2: partial classification guidance, revision criterion, grouping discipline |
| WA-SessionB-DataPrep-Instruction | v5.5 | Section 6: extracted_theological_anchor; Section 7.4: XREF rule + G13 note; Section 9.1: pool membership from RMG 7a |

**Second wave (researcher decisions from uploaded comments):**

| Document | Version | Key changes |
|---|---|---|
| WA-VerseContext-Instruction | v1.4 | Section 5.2: SQL policy statement; Section 6.1: partial completion error rule; Section 6.2: all-verses-fail error rule; revision documentation rule; grouping criterion (researcher-specified) |
| WA-SessionB-Analysis-Instruction | v5.5 | Section 4.2: approx. 9 word threshold; Section 7: quality flag handling table; Section 7 Step 4: root data absence rule |
| WA-SessionB-ClaudeCode-Instructions | v3.1 | Section 14.1: SQL policy statement; Section 14.8: pre-construction check mandatory; pool membership from RMG 7a |

**Gap register updates:**

| Document | Version | Key changes |
|---|---|---|
| WA-InstructionGaps | v2 | Complete IP-based rebuild; 34 gaps; cross-gap consistency verified |
| WA-InstructionGaps | v2.1 | Researcher decisions applied; 37 gaps; 27 closed; all BLOCKING gaps resolved |

---

## 4. Decisions Made This Session

All decisions are the researcher's. Recorded here for instruction update accuracy.

### 4.1 SQL policy (applies programme-wide)

**Decision:** SQL queries and scripts are Claude Code's responsibility. Claude AI instructions must provide field names, table names, derivation rules, and expected outcomes, plus a clear handoff statement to Claude Code. Where these are present, gaps that previously required explicit SQL are closed. This policy closes G01, G08, G07, G10, IP-PA-01a (partially) by policy acknowledgement rather than SQL specification.

**Documents updated:** VerseContext Instruction v1.4 Section 5.2; CC Instructions v3.1 Section 14.1.

### 4.2 All-verses-fail error rule (G05)

**Decision:** If all verses for a term fail the relevance filter, this is an error condition — it should never happen for a correctly classified term. Claude AI must stop immediately, flag to researcher with term details and per-verse reasons, and await instruction.

**Documents updated:** VerseContext Instruction v1.4 Section 6.2.

### 4.3 Partial completion error rule (G02)

**Decision:** Partial completion (term_classification_complete = false with existing records in a new batch) is an error condition. Claude AI must flag to researcher with details and await instruction. The batch must be fixed and resubmitted — not continued from where it left off.

**Documents updated:** VerseContext Instruction v1.4 Section 6.1.

### 4.4 Revision documentation rule (G03)

**Decision:** When a revision to a prior classification is clearly warranted, Claude AI must document the reasons in the verse_context notes field and report the change to the researcher in the per-term classification summary. Not a silent reclassification.

**Documents updated:** VerseContext Instruction v1.4 Section 6.2.

### 4.5 Grouping criterion (G04)

**Decision:** A new group is warranted when the contextual meaning is materially different — meaning an analysis of the verses would arrive at a differential conclusion about how the inner-being characteristic operates. Material difference is assessed against: different way the term serves the inner being; different verse context; variation that changes or enhances how the characteristic operates — including different parties involved, different function, different influences, or involvement of other characteristics.

**Documents updated:** VerseContext Instruction v1.4 Section 6.2 Step 3.

### 4.6 Pipeline status lifecycle (G06 escalation)

**Decision:** The pipeline status transition rules are not fully documented as a coherent whole. This is a holistic gap requiring a dedicated review work item (G06-NEW). Individual note fixes are insufficient. The full review must trace every status value, every transition trigger, failure scenarios, and recovery paths.

**New gap raised:** G06-NEW. Not resolved this session — requires dedicated work item.

### 4.7 Simultaneous analysis threshold (G14)

**Decision:** Working threshold is approximately 9 words. Subject to empirical revision as pool analyses proceed. Not yet a firm limit — will be tested.

**Documents updated:** Analysis Instruction v5.5 Section 4.2.

### 4.8 extracted_theological_anchor (G30/Q-F)

**Decision:** Treat as equivalent to extracted. No reclassification needed. Leave status unchanged.

**Documents updated:** DataPrep Instruction v5.5 Section 6 (applied in first wave).

---

## 5. Gap Register — Final State This Session

| Status | Count |
|---|---|
| CLOSED | 27 |
| OPEN — instruction update needed | 9 |
| NEW GAP (G06-NEW) | 1 |
| **Total** | **37** |

**All BLOCKING gaps resolved.** The gratitude dry run may proceed once VerseContext v1.4 and Analysis v5.5 updates are in place (both produced this session).

**Remaining open gaps (instruction updates still needed):**

| Gap | Document | Change needed |
|---|---|---|
| G01/G08 | VerseContext v1.4 | SQL policy note — APPLIED this session |
| G02 | VerseContext v1.4 | Partial completion error rule — APPLIED |
| G03 | VerseContext v1.4 | Revision documentation rule — APPLIED |
| G04 | VerseContext v1.4 | Grouping criterion — APPLIED |
| G05 | VerseContext v1.4 | All-verses-fail error rule — APPLIED |
| G14 | Analysis v5.5 | Threshold — APPLIED |
| G17 | Analysis v5.5 | Quality flag handling — APPLIED |
| G18 | Analysis v5.5 | Root data absence rule — APPLIED |
| IP-PA-01a | CC Instructions v3.1 | Pre-construction check — APPLIED |
| G06-NEW | Dedicated review | Pipeline status lifecycle — NOT YET RESOLVED |
| G21 | Extraction v5.5 | Verify pool_observations note applied correctly |

---

## 6. Document Version Registry — End of Session

| Document | Latest version | Status |
|---|---|---|
| WA-InstructionGaps | v2.1 | Current |
| WA-VerseContext-Instruction | v1.4 | Current |
| WA-SessionB-DataPrep-Instruction | v5.5 | Current |
| WA-SessionB-Analysis-Instruction | v5.5 | Current |
| WA-SessionB-Extraction-Instruction | v5.5 | Current |
| WA-SessionB-ClaudeCode-Instructions | v3.1 | Current |
| WA-Reference | v5.4 | Current |
| WA-Registry-Management-Guide | v5.6 | Current |
| patch_specification | v1.4 | Unchanged |

---

## 7. Next Session Work Order

1. **G06-NEW — Pipeline status lifecycle review.** Trace every session_b_status and verse_context_status transition across all pipeline stages. Document what sets each value, failure scenarios, and recovery paths. Update all affected instructions.

2. **G21 verification.** Confirm pool_observations file-only note is correctly applied in Extraction v5.5 Section 8.1.

3. **Gratitude dry run.** All BLOCKING gaps resolved. Documents are in place. Proceed with the gratitude word analysis as a dry run to validate the pipeline.

4. **Empirical threshold review.** After the gratitude dry run, assess whether the approximately 9 word simultaneous threshold is accurate and update Analysis Instruction v5.5 if needed.

---

*WA-SessionLog-InstructionUpdates-v1-20260330 | Continues from WA-SessionLog-FieldAnalysis-v1-20260329 | 37 gaps in register; 27 closed; 9 applied this session; 1 new gap (G06-NEW); all BLOCKING gaps resolved; dry run gate clear*
