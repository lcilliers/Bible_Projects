# Session B Export — Stage 1 Audit Checklist Cross-Reference
## wa-global-sessionb-export-crossref-v1-20260415.md
**Date:** 2026-04-15
**Export analysed:** wa-023-compassion-sessionb-export-v2-20260415.json (123 KB)
**Instruction reference:** wa-global-sessionb-instruction-v5.0-20260415.md — Stage 1 checklist
**Status:** Findings for researcher review — export script decisions and spec refinements required

---

## A. What the export covers well — checklist items that pass

The following Stage 1 checklist items are fully supported by the export as produced:

| Checklist item | Export section | Status |
|----------------|---------------|--------|
| Registry fields present and correct | `registry` | ✅ All fields present including legacy, sparse, and inference_note |
| `verse_context_status = Complete` | `registry.verse_context_status` | ✅ |
| `session_b_status` at expected stage | `registry.session_b_status = "Analysis Complete"` | ✅ |
| `dimensions` populated | `registry.dimensions` | ⚠ NULL — see Finding F-001 |
| All OWNER terms have meaning parse | `statistics.terms_without_meaning_parse = 0` | ✅ |
| All groups have dimension assignment | `statistics.groups_without_dimension = 0` | ✅ |
| All groups at CLAUDE_AI or RESEARCHER confidence | `statistics.groups_at_automated_confidence = 0` | ✅ |
| `dominant_subject` populated on all groups | `statistics.groups_without_dominant_subject = 0` | ✅ |
| `null_owner_type_count = 0` | `statistics.null_owner_type_count = 0` | ✅ |
| `thin_evidence_findings = 0` | `statistics.thin_evidence_findings = 0` | ✅ |
| `root_family_gap_count = 0` | `statistics.root_family_gap_count = 0` | ✅ |
| `session_b_dimensions_rows = 0` | Correct — not applicable to this registry | ✅ |
| Deleted terms visible with phase2 flags | `terms.deleted_terms` — 89 rows present | ✅ |
| Set-aside verses visible | `set_aside_verses` — 49 rows present | ✅ |
| SD pointers present | `session_research_flags.sd_pointers` — 33 rows | ✅ |
| Correlation signals embedded as per-registry slice | `correlation_signals` — 49 connections across 5 signal types | ✅ |
| Patch history present | `patch_history` — 8 engine runs + 1 word_run_state | ✅ |
| Dimension Review completion confirmed | `registry.dim_review_status = "Complete"`, `dim_review_version` present | ✅ |

---

## B. Findings from the export

### F-001 — registry.dimensions is NULL

**Observation:** `registry.dimensions = null` despite `session_b_status = "Analysis Complete"` and Dimension Review complete.

**Assessment:** This is a real data gap. The `dimensions` field on `word_registry` is populated by Session B extraction. Compassion has completed Session B under the old instruction (v4.x) and `session_b_status = Analysis Complete` — but the `dimensions` field was either not written or has been cleared. The description field is populated and contains analytical content that implies dimensions are known (`"Soul-body interface"`, `sb_classification` is populated). This is a Type (a) correction item for Stage 1.

**Stage 1 action:** Flag for correction. Claude AI will populate `dimensions` from the analytical picture during Stage 2 Pass 4 and write it via a Type (a) patch at Stage 1 close or Stage 2 Pass 4 close.

---

### F-002 — god_as_subject inconsistency

**Observation:** `god_as_subject_inventory_count = 0` but `god_as_subject_mti_flag_count = 4`. Four GOD_AS_SUBJECT flags exist in `mti_term_flags` but `wa_term_inventory.god_as_subject = 0` for all terms.

**Assessment:** Confirmed real inconsistency. The `mti_term_flags` are the authoritative source (per GR-DATA-003 and schema analysis). The `wa_term_inventory.god_as_subject` field is superseded and was not updated when the mti flags were written. The correct state is: 4 terms have God as subject, confirmed by `mti_term_flags`. The `wa_term_inventory` field is wrong.

**Stage 1 action:** Type (a) corrective patch — update `wa_term_inventory.god_as_subject = 1` for all 9 terms that have GOD_AS_SUBJECT in `mti_term_flags` (DIR-007 Q3 confirmed 9 inconsistencies, not 4 as the initial export statistic suggested — the export script undercounted due to a join path error, now corrected). Terms: G3627, G4184, G4697, H2551, H2587, H2594, H2617B, H5150, H7358. Note: per spec audit_notes, this field should not be written going forward — this correction is a one-time alignment only.

**Note for spec:** The consistency check worked exactly as designed. This finding would not have surfaced without the statistics block comparison. The undercount in the initial export statistic (4 vs 9) has been identified and the export script fix is scheduled under DIR-008 work.

---

### F-003 — session_b_flags_unresolved = 1

**Observation:** One open flag with `session_target = 'B'` and `resolved = 0`. The export shows this in `session_research_flags.session_b_flags`.

**Assessment:** This is the hard gate item. Stage 2 cannot close until this flag is resolved. The export makes it visible and provides the full description so Session B can assess disposition at Step 1.3. Need to read the flag content to determine whether it is resolvable in Stage 1 or requires a Stage 2 pass.

**Stage 1 action:** Step 1.3 — assess disposition of this flag. Read the description in the export against the available data. Classify as: resolvable in Stage 1, resolvable in specific Stage 2 pass, requires RESEARCHER_DECISION.

---

### F-004 — terms_without_mti_cross_refs = 8 of 9 OWNER terms

**Observation:** Only 1 of 9 active OWNER terms has rows in `mti_term_cross_refs`. 8 of 9 have no cross-references.

**Assessment:** Two possible explanations: (a) compassion's terms genuinely have few cross-references in the MTI dataset — the ELE root family (the primary compassion vocabulary) may simply not be richly cross-referenced in STEP's data; or (b) the cross-reference data was not populated for these terms during Session A. Cannot distinguish without reading the cross-reference data for the one term that does have entries and checking whether similar terms should also have them.

**Stage 1 action:** Note in observations log. During Pass 1, assess whether the one cross-referenced term's cross-references reveal that similar terms should also have them. If the cross-reference gap appears to be a data preparation failure, raise a CC directive. If it reflects genuine data sparseness in the source, note it as a PH2_DATA_QUALITY observation and carry forward.

---

### F-005 — 89 deleted terms — requires Stage 1 critical review

**Observation:** 89 deleted terms versus 9 active terms. Ratio of 90% deleted is striking.

**Assessment:** This ratio reflects the breadth of the STEP extraction for compassion — the `meanings=` API endpoint casts a wide net across related vocabulary (RACHAM, CHESED, SPLANCHN root families and all lexical relatives). Most of the 89 will be correct deletions — function words, grammatical particles, peripherally related vocabulary. However the volume warrants systematic review. The export includes the full deleted_terms list with phase2_flags for audit.

**Stage 1 action:** Step 1.4 — systematic review of deleted terms during the audit pass. Priority: deleted terms that have phase2_flags (the export includes these). For each phase2 flag on a deleted term: note as irrelevant (term is deleted). For the deleted terms themselves: Claude AI confirms the deletion is justified by the term's gloss and available data. If any deletion appears questionable, raise for reassessment.

---

### F-006 — 1 active session_b_finding — pre-v5.0 finding

**Observation:** 1 active finding in `wa_session_b_findings`. This was raised under an earlier instruction version. The 9 new lifecycle fields (`pass_ref`, `study_segment`, `delete_flag`, etc.) are present in the schema but the existing finding has `pass_ref = NULL` and `study_segment = NULL`.

**Assessment:** Expected for pre-v5.0 work. The finding is valid analytical content but lacks v5.0 lifecycle attribution. Stage 1 must disposition this finding — is it correct, does it need deepening, or has it been superseded by the work done in v4.x?

**Stage 1 action:** During Stage 1 audit of prior-phase findings (Step 1.2), note this finding and schedule its review during the relevant Stage 2 pass. Assign `pass_ref` and `study_segment` when reviewed.

---

### F-007 — 33 SD pointers already raised — require Pass 6 review

**Observation:** 33 SD_POINTER flags already exist for this registry from prior Session B work (v4.x).

**Assessment:** These are not new work for Session B v5.0 — they exist and must be reviewed in Pass 6. The Analytical Brief Section 8 will reference these. The count-match gate at Section 2.2 will verify that these 33 are present in the database against the observations log count from Stage 2.

**Stage 1 action:** Record count in observations log at session start: "33 SD pointers already in database for registry 023." Pass 6 reviews each for accuracy and completeness. Net new SD pointers from this run are added to this count.

---

### F-008 — word_run_state has researcher_approved = 0

**Observation:** The word_run_state from the initial BULK_GAP_FILL run shows `researcher_approved = 0` and multiple REVIEW items (WR-08, WR-09, WR-19). WR-08: low verse/occurrence ratio for G3627. WR-09: testament_coverage NULL. WR-19: parse warnings for H7356A, G4697, H5162G, G3627, G4834.

**Assessment:** These REVIEW items from the audit_word run are historic — they were raised in March 2026 and have not been formally signed off. WR-09 (testament_coverage NULL) is a data gap on the file_index. WR-08 and WR-19 should be checked — G3627 has 1 verse record against 28 occurrences (ratio 0.036), which is a genuine volume limitation. The 5 terms with parse warnings may have meaning data quality issues.

**Stage 1 action:** Review WR-08, WR-09, and WR-19 items during Step 1.2 audit. G3627 is a likely PH2_VOLUME_LIMITATION candidate. Parse warning terms should be cross-checked against their meaning parse content. WR-09 can be corrected via a field patch on wa_file_index.

---

### F-009 — VCREPAIR patch had 23 errors

**Observation:** `PATCH-20260412-023-VCREPAIR-V1` shows `"errors": 23` in error_detail alongside `"vc_inserts": 161`.

**Assessment:** 23 verse context inserts failed during the repair patch. This is a known historical issue (the RESOLVE: prefix problem documented in patch spec v1.8). Whether these 23 errors were subsequently corrected is not visible from this export alone.

**Stage 1 action:** CC query needed. Request from CC: are there any verse records for registry 023 OWNER terms that have no corresponding verse_context record (unclassified verses)? If zero — the 23 errors were resolved. If non-zero — this is a Stage 1 data gap requiring a Verse Context sub-process trigger. Per GR-DB-001 — do not assume.

This is a specific CC data request, not a RESEARCHER_DECISION item. Claude AI can request this directly.

---

## C. Export spec refinements required — for `wa-global-sessionb-export-spec-v1_2-20260415.json`

Based on reading the export and verification report, the following spec updates are needed:

| Item | Spec change | Reason |
|------|-------------|--------|
| **Filename pattern** | Adopt `wa-{NNN}-{word}-sessionb-export-v{N}-{YYYYMMDD}.json` | Consistent with all other Session B output filenames. CC recommendation confirmed. |
| **related_verses: add verse_text** | Add `verse_text` field to `related_verses` per group | Small size impact; related verses are occasionally needed for context during Pass 3. Currently reference only — insufficient. |
| **correlation_signals: document confirmed source** | Replace "TBC" with confirmed specification: separate file `data/exports/session_d/wa-correlations-{date}.json`, sliced per-registry at export time, freshness date carried in `_extract_meta.produced_date` | CV-002 confirmed |
| **correlation freshness gate** | Add to spec: if correlation file `produced_date` is more than 14 days before export date, export emits a WARNING flag in the statistics block (`correlation_stale: true`). Export does not refuse — Session B decides whether to proceed or request a refresh. | Correlation data currency affects Pass 6 quality. A warning is preferable to a hard block. |
| **owning_registry_word field error** | The export shows `owning_registry_word: "be gentle"` for G3356 — this appears to be the gloss, not the owning registry's word label. CC should verify the join path for this field. | Potential export script bug — should show "compassion", not the term gloss |
| **meta.export_version auto-increment** | Specify that the export script scans for existing same-day exports and auto-increments. CLI `--version` override remains available. | Current CLI dependency is fragile for automated pipeline use |

---

## D. Questions for CC

Per GR-DB-001 — request these data points before Session B v5.0 first run begins:

| Query | Purpose |
|-------|---------|
| Count of verse records for registry 023 OWNER terms with no verse_context record (unclassified) | Resolves F-009 — determines whether the 23 VCREPAIR errors were corrected |
| The full description of the 1 open session_target=B flag | Resolves F-003 — needed to determine disposition |
| The 4 terms in mti_term_flags with GOD_AS_SUBJECT for registry 023 | Needed for F-002 corrective patch — confirm which strongs_numbers |

---

## E. Export script promotion decision

**Observation:** The exploratory script implements the full v1.1 spec. The production `word_export.py` covers ~40% of the spec. 

**Assessment:** The exploratory script is the correct foundation for the production export. The question is promotion path — extend `word_export.py` or replace it. The verification report notes that `apply_session_patch.py` also needs updating to write back the 9 new finding lifecycle fields and entity-link inserts.

**This is a CC execution decision, not a researcher decision.** The analytical specification (the spec) is settled. CC determines the promotion approach. The only researcher input needed: confirm whether the exploratory script should be promoted to production as the new `word_export.py` (replacing the old one) or maintained as a parallel script until fully tested.

**Recommendation:** Promote to production once the `owning_registry_word` field bug (see spec refinements) is confirmed and fixed. The script has produced a clean 123 KB export covering all 17 sections — it is functionally ready.

---

## F. Summary — what blocks Session B v5.0 first run

| Item | Blocking? | Resolution path |
|------|-----------|----------------|
| Export spec v1.2 needed (6 refinements) | Not blocking for first run — use v1.1 export with known gaps noted | Produce `wa-global-sessionb-export-spec-v1_2-20260415.json` |
| Export script promotion | Not blocking — exploratory script is usable for first run | CC promotion after bug fix |
| F-009 — VCREPAIR 23 errors — unclassified verses? | **Potentially blocking** — if unclassified verses exist, Verse Context sub-process required before Stage 2 | CC query required |
| F-002 — god_as_subject inconsistency | Not blocking — correctable in Stage 1 Type (a) patch | CC query for 4 term ids, then patch |
| F-003 — 1 unresolved B-flag | **Blocking for Stage 2 close** — must be resolved, not for session start | Read flag description, assess disposition |
| apply_session_patch.py lifecycle field support | **Blocking for Stage 2 write** — patch applicator cannot write back 9 new fields yet | CC update required before first pass close write |

The single item that may block session start is F-009. All others are manageable within the session once it begins.
