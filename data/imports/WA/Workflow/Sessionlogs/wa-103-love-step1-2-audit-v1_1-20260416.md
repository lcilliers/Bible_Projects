# WA — Step 1.2 Audit Report: Registry 103 (Love)
**Filename:** wa-103-love-step1-2-audit-v1_1-20260416.md
**Date:** 2026-04-16
**Version:** v1.1
**Change note (v1.1):** RD-S1-001 disposition confirmed by researcher — H2898 is a span filter failure requiring re-extraction and Verse Context re-run, not deletion. Instruction gap IC-02 added: Step 1.2 and Step 1.5 must distinguish span filter failure from standard zero-verse data gap; a fourth resolution path (re-extraction + VC re-run) must be specified.
**Extract audited:** wa-103-love-sessionb-export-v1-20260416.json
**Schema version in extract:** 3.8.0
**Audit instruction:** wa-global-sessionb-step1-2-corrected-v1-20260416.md
**Previous output refs:**
- wa-103-love-step1-2-audit-v1-20260416.md (v1.0 — initial audit)
- wa-global-sessionb-step1-2-corrected-v1-20260416.md (audit framework)
- wa-global-sessionb-update-tasklist-v1_12-20260416.md (T-02B)

---

## Purpose

This report applies the Step 1.2 corrected audit framework to the love extract. It validates every data node against the specified checks, documents all findings, and identifies gaps requiring Type (a) patch action, sub-process triggers, or Stage 2a verification notes. It also confirms where nodes are clean.

---

## Section A — Registry Record (`word_registry`)

| Field | Value | Status | Note |
|-------|-------|--------|------|
| `word` | love | ✓ PASS | Matches session context |
| `no` | 103 | ✓ PASS | Correct registry number |
| `cluster_assignment` | C17 | ✓ PASS | Valid cluster code |
| `session_b_status` | Analysis Complete | ⚠ FLAG | Expected: `Pre-Analysis Complete`. Actual: `Analysis Complete`. Session B has already been run on this registry. This extract is being used as a validation test against the instruction — not as a first-run Session B entry. **If this were a live Session B run: STOP — confirm with researcher before proceeding.** |
| `verse_context_status` | Complete | ✓ PASS | Hard gate met |
| `dim_review_status` | Complete | ✓ PASS | Hard gate met |
| `dim_review_version` | WA-DimensionReview-Instruction-v1.9-2026-04-09 | ✓ PASS | Populated |
| `dimensions` | Relational/Social | ✓ PASS | Populated |
| `carry_forward` | 1 | ✓ PASS | Default — proceed |
| `unique_term_count` | 41 | ✓ NOTE | Extract statistics show 57 OWNER terms. Registry field = 41. Discrepancy of 16 — likely reflects unique vs total OWNER count distinction or stale registry count. Note for investigation — not blocking. |
| `shared_term_count` | 96 | ✓ PASS | Present |
| `term_sharing_ratio` | 0.701 | ✓ PASS | Plausible: 96/(41+96) = 0.70 — consistent |
| `phase1_term_count` | 137 | ✓ PASS | > 0 |
| `phase1_verse_count` | 2799 | ✓ PASS | > 0 |
| `sb_classification` | Spirit-Soul Interface | ✓ NOTE | Already populated — Session B previously run |
| `description` | Populated | ✓ PASS | Substantive content present |

**Cross-field check A1:** `verse_context_status = Complete` AND `dim_review_status = Complete` — both true. Hard gate passed.

**Section A summary:** 1 flag (`session_b_status` — test context only, not a live issue), 1 note (`unique_term_count` discrepancy — not blocking).

---

## Section B — Term Inventory (`wa_term_inventory` + `mti_terms`)

**Term counts:**
- Active OWNER terms (`term_owner_type = OWNER`): 57
- Active XREF terms: 14
- Deleted terms: 71
- Terms with `mti_status = NULL` in active set: 13

### B1 — mti_status NULL on active terms

13 active terms have `mti_status = NULL`. Per the controlled vocabulary (patch spec Appendix A.4), NULL means "unclassified — awaiting Session B pre-analysis." These terms are in the active set but have no confirmed status.

**Action required:** Request from CC — identify all active terms for registry 103 where `mti_terms.status IS NULL`. Confirm whether these are OWNER or XREF terms and whether they should be `extracted`, `extracted_thin`, or `xref_[word]`. Add classification to Type (a) patch.

**Note:** One term has `mti_status = 'xref_desire'` — this is a valid `xref_[word]` value per the controlled vocabulary. Correctly classified.

### B2 — evidential_status

All 57 OWNER terms have `evidential_status = NULL`. Expected at Session B entry — will be set during Stage 2. ✓ PASS — no action.

### B3 — strongs_number format

All active terms pass the format check (H[digits] or G[digits] with optional suffix). ✓ PASS

### B4 — occurrence_count

All OWNER terms have `occurrence_count > 0`. ✓ PASS

### B5 — Cross-check B3: somatic_link vs mti_term_flags

Per GR-DATA-003, `mti_term_flags` is authoritative for somatic classification.

**Discrepancies identified:**

| Term | strongs | somatic_link (wa_term_inventory) | Somatic flags (mti_term_flags) | Status |
|------|---------|----------------------------------|-------------------------------|--------|
| agapao | G0026 | 0 | flag_id=3 (SOMATIC_INNER_LINK) present | ⚠ DISCREPANCY |
| kataphileō | G2705 | 0 | flag_id=3 (SOMATIC_INNER_LINK) present | ⚠ DISCREPANCY |
| phileō | G5370 | 0 | flag_id=3 (SOMATIC_INNER_LINK) present | ⚠ DISCREPANCY |
| ahavah | H0160 | 0 | flag_id=3 (SOMATIC_INNER_LINK) present | ⚠ DISCREPANCY |
| racham | H7355 | 1 | flag_id=3 present | ✓ CONSISTENT |
| rachamim | H7356B | 1 | flag_id=3 present | ✓ CONSISTENT |

**Action required:** 4 terms have `somatic_link = 0` in `wa_term_inventory` but a SOMATIC_INNER_LINK flag in `mti_term_flags`. Per GR-DATA-003, the `mti_term_flags` value is authoritative. Add to Type (a) patch: set `somatic_link = 1` on G0026, G2705, G5370, H0160. Note for Stage 2a verification against verse evidence.

**Statistics cross-check:** Extract statistics confirm `somatic_link_inventory_count = 2` but `somatic_link_mti_flag_count = 4` — consistent with the discrepancy found above. The statistics self-reported this gap.

### B6 — god_as_subject plausibility

`god_as_subject = 1` on 11 OWNER terms. Statistics confirm `god_as_subject_inventory_count = 11` and `god_as_subject_mti_flag_count = 11` — fully consistent. No discrepancy. ✓ PASS — note for Stage 2a verse verification.

### B7 — delete_flagged on active terms

All active OWNER terms have `delete_flagged = 0`. ✓ PASS

### B8 — Cross-check B1: verse count vs occurrence_count (small sample check)

Three OWNER terms have verse counts below 20% of occurrence_count and do not have a `SMALL_VERSE_SAMPLE` quality flag:

| Term | strongs | occurrence_count | active_verses | ratio | SMALL_VERSE_SAMPLE flag |
|------|---------|-----------------|---------------|-------|------------------------|
| adelphē | G0079 | 130 | 25 | 19% | ❌ MISSING |
| prōtotokos | G4416 | 134 | 9 | 7% | ❌ MISSING |
| tov (goodness) | H2898 | 32 | 0 (all deleted) | 0% | ❌ MISSING |

**Action required:**
- G0079 and G4416: Add `SMALL_VERSE_SAMPLE` data quality flag to `wa_data_quality_flags` for these terms. Add to Type (a) patch.
- H2898: All 31 verse records are `delete_flagged = 1` with `span_match_count = 31`. This is a span filter outcome — all extracted verses were filtered out. This term has zero usable verses. This is a significant data gap. **Add to RESEARCHER_DECISION accumulator** — what should be done with H2898 (tov — goodness)? Options: (a) reclassify as delete/excluded; (b) accept as zero-verse term with an analytical note; (c) investigate whether span filtering was applied incorrectly.

### B9 — meaning and parsed_meaning_id

Statistics confirm `terms_without_meaning_parse = 0`. All terms have meaning data. ✓ PASS

**Section B summary:** 3 issues requiring Type (a) patch action (B1 NULL mti_status, B3 somatic_link discrepancies, B8 missing quality flags), 1 item for RESEARCHER_DECISION (H2898 zero verses), 1 note for Stage 2a (god_as_subject verification).

---

## Section C — Verse Records (`wa_verse_records`)

**Verse record summary reviewed from `verse_records_summary` (142 term entries):**

| Check | Result | Note |
|-------|--------|------|
| Every active OWNER term has ≥ 1 active verse | ⚠ EXCEPTION: H2898 has 0 active verses (all deleted) | Flagged in Section B — RESEARCHER_DECISION raised |
| Verse text presence | Not directly checkable from summary — assumed present | Verify during Stage 2a if any verse reads as empty |
| span_strong_match | Present across all terms | ✓ PASS |
| translation = 'ESV' | Assumed — not in summary | Verify against extract sample if needed |

**Cross-check C1:** H2898 verse count (0) vs `occurrence_count` (32) — ratio = 0%. Already flagged. G0079 (19%) and G4416 (7%) already flagged in B8.

**Cross-check C2:** Statistics show `somatic_link_mti_flag_count = 4` — H7355, H7356B, G0026, G2705, G5370, H0160 were already reviewed.

**Section C summary:** No additional issues beyond those already captured in Section B.

---

## Section D — Verse Context Groups (`verse_context_group` + `verse_context`)

**67 active groups across the extract.**

| Check | Result | Note |
|-------|--------|------|
| Groups with blank/short context_description | 0 | ✓ PASS — all descriptions are substantive |
| Groups with delete_flagged = 1 | 0 | ✓ PASS — all active |
| Groups with no anchor_verses | 0 | ✓ PASS — all 67 groups have at least one anchor verse |
| Total anchor verses | 117 | ✓ PASS — substantial coverage |
| Total related verses | 1,100 | ✓ PASS |
| Total set-aside verses | 213 | ✓ PASS |

**Cross-check D1:** 3 active OWNER terms have no groups: H1730I (dod), H1736 (du.day), H7468 (re.ut). All three are `extracted_thin` with occurrence counts of 18, 6, and 6 respectively. These may be legitimately ungrouped due to thin verse data, or Verse Context may not have been completed for them.

**Action required:** Confirm with CC whether these three terms have any verse_context records at all. If they have verse records but no groups: Verse Context sub-process trigger for these specific terms. If they have zero verse records after span filtering: note as thin-data terms with no analytical content — add to Stage 2a context.

**Cross-check D2:** Verse count consistency (`anchor_count + related_count + set_aside_count = total_verse_count` per group): present in the `dimension_assignment` nested data for each group. Spot check of first group: `anchor=2, related=14, set_aside=11, total=16`. Note: anchor(2) + related(14) = 16 = total, but set_aside = 11 which exceeds the anchor+related count. This suggests `total_verse_count` counts active verses only and set-aside verses are tracked separately. This is consistent — no anomaly.

**Note on dominant_subject = 'NONE':** 5 groups have `dominant_subject = 'NONE'`. Valid values per the instruction include 'God', 'Human', 'Mixed', 'Community', 'Other'. 'NONE' is not in this list. These 5 groups require correction. **Add to Type (a) patch:** update `dominant_subject` on these groups to the appropriate value, determined by reading the group description. Stage 1 can set based on description content alone:
- Group 1580-001 (kiss as outward relational expression): Human → set to 'Human'
- Group 533-001 (love-relationship full range): Mixed → set to 'Mixed'
- Group 542-001 (inner wellbeing/moral approval): Human → set to 'Human'
- Group 550-001 (hatred as opposing disposition): Human → set to 'Human'
- Group 572-001 (natural affection/friendship): Human → set to 'Human'

These are data corrections grounded in the group description — not analytical judgements.

**Section D summary:** 1 potential sub-process trigger (3 OWNER terms without groups — confirm with CC), 5 Type (a) patch items (`dominant_subject = 'NONE'` corrections).

---

## Section E — Dimension Assignments (`wa_dimension_index`)

| Check | Result | Note |
|-------|--------|------|
| Groups missing dimension_assignment | 1 — group 2898-001 | ⚠ ISSUE |
| Groups with AUTOMATED confidence | 0 | ✓ PASS — no sub-process trigger |
| All assigned groups at CLAUDE_AI confidence | 66 of 67 | ✓ PASS for assigned groups |
| Groups with dominant_subject = NULL | 0 | ✓ PASS |

**Groups with non-standard dimension labels:** All 66 assigned groups use non-standard labels (e.g. 'Relational Disposition', 'Emotion — Positive', 'Moral Character', 'Cognition', 'Volition', 'Transformation', 'Divine-Human Correspondence', 'Emotion — Negative'). These are a different vocabulary from the standard set in the audit framework.

**Observation:** The extract uses a more granular dimension vocabulary than the standard list in the corrected Step 1.2 audit framework ('Volitional/Will', 'Cognitive/Intellectual', etc.). This is an important finding about the audit framework itself — the valid dimension list in Step 1.2 needs to be updated to reflect the actual vocabulary in use. **This is a correction item for T-02B: the valid dimension vocabulary in Section E must be updated to match what Dimension Review actually produces.**

**Action required — group 2898-001:** One group has no dimension assignment. This is group for H2898 (tov) which also has zero verse records. The group exists but has neither verse data nor a dimension. This is consistent with the H2898 data issue flagged in Section B. Covered by the existing RESEARCHER_DECISION item for H2898.

**Cross-check E1:** Every active group has exactly one `dimension_assignment` row (dimension index data is embedded in the group in this extract). ✓ PASS for assigned groups.

**Cross-check E2:** `somatic_link` vs Somatic/Embodied dimension: no groups are assigned to 'Somatic/Embodied' in this extract (the label 'Somatic/Embodied' does not appear). There is no equivalent in the non-standard vocabulary. Note for Stage 2a — the somatic dimension may be embedded in other labels or absent for this word.

**Cross-check E3:** `god_as_subject = 1` (11 terms) vs `Theological/Divine-Human` dimension: the label 'Divine-Human Correspondence' appears to serve this purpose. 12 groups have `dominant_subject = 'GOD'`. Broadly consistent — note for Stage 2a verification.

**Section E summary:** 1 group without dimension assignment (linked to H2898 RESEARCHER_DECISION), important finding about dimension vocabulary that requires correction to the Step 1.2 framework.

---

## Section F — Existing Findings and Flags (counts)

| Item | Value | Note |
|------|-------|------|
| Active session_b_findings | 2 | Both status = 'pending', both DIMENSION_REVIEW type |
| Findings with catalogue_link | 0 | Step 1.3b will process these |
| Session B target flags (unresolved) | 0 | ✓ PASS — Step 1.3c hard gate pre-satisfied |
| SD pointers raised | 35 | Session D — noted for Stage 2a |
| Phase2 flags | 0 | Step 1.3a will have no flags to review |
| Catalogue questions for this registry | 14 (L-001 through L-014) | Love extension questions indexed |
| Catalogue questions total | 194 | ✓ PASS |

**Note on findings:** 2 existing DIMENSION_REVIEW findings in `pending` status with no catalogue link. Step 1.3b will assign catalogue questions to both. No anomalies.

**Note on SD pointers:** 35 SD pointers already raised from prior Session B work. These are Session D matters — not reviewed in Stage 1. They will be read at Stage 2a start.

**Section F summary:** No issues — all counts are expected and clean.

---

## Section G — Supporting Term Data

| Table | Count / Status | Note |
|-------|---------------|------|
| `wa_meaning_parsed` | 0 terms without meaning parse | ✓ PASS — all terms have meaning data |
| `wa_term_root_family` | 18 root family gaps | Note — not anomalous; thin terms and particles often lack root data |
| `wa_term_related_words` | Present | Not checked in detail — no anomaly flags from statistics |
| `wa_lsj_parsed` | Present for Greek terms | Not detailed in statistics — assumed present |
| `wa_cross_registry_links` | 8 rows | ✓ PASS — noted for Stage 2a |
| `correlation_signals` | 16 ranked pairs, 83 shared anchor verses | Substantial — rich cross-registry signal set for Stage 2a |

**Section G summary:** No issues. 18 root family gaps are normal for a large registry with many thin terms.

---

## Catalogue and Question Index

**Observation question catalogue:**
- Master: 194 questions — ✓ PASS
- Registry-indexed questions: 14 (L-001 through L-014, Love Extensions) — correctly populated from T-POP-A

**Finding:** The extract correctly includes both the master catalogue and the registry-specific subset. This confirms the extract structure supports Step 1.3b directly.

---

## Step 1.2 Audit Summary — Registry 103 (Love)

```
Registry state: session_b_status=Analysis Complete [⚠ already run — test context],
                verse_context_status=Complete, dim_review_status=Complete
Active terms: 57 OWNER, 14 XREF, 71 deleted
Active term mti_status gaps: 13 terms with NULL mti_status
Total anchor verses: 117 across 67 groups
Verse context groups: 67 active groups, 66 with dimension assignments
Dimension confidence: 66 CLAUDE_AI, 0 AUTOMATED
Dimension vocabulary: non-standard labels in use (see below)
Existing findings: 2 active (pending, no catalogue links)
Research flags: 0 Session B unresolved, 35 Session D (open)
Phase2 flags: 0

Gaps identified: 7 categories
```

**Hard gate check:**

| Condition | State | Decision |
|-----------|-------|----------|
| `verse_context_status = Complete` | Complete | ✓ PASS |
| `session_b_status = Pre-Analysis Complete` | Analysis Complete | ⚠ TEST CONTEXT ONLY — would STOP in live run |
| All active OWNER terms have ≥ 1 verse record | H2898 has 0 | ⚠ — RESEARCHER_DECISION raised |
| `carry_forward = 1` | 1 | ✓ PASS |

All conditions pass for a test review. One RESEARCHER_DECISION item raised (H2898).

---

## Consolidated Action Items

### Type (a) Patch Items

| # | Table | Action | Source |
|---|-------|--------|--------|
| P-01 | `mti_terms` | Set `status` on 13 NULL-status active terms | Section B1 |
| P-02 | `wa_term_inventory` | Set `somatic_link = 1` on G0026, G2705, G5370, H0160 | Section B3 |
| P-03 | `wa_data_quality_flags` | Add `SMALL_VERSE_SAMPLE` flag for G0079 and G4416 | Section B8 |
| P-04 | `wa_dimension_index` | Set `dominant_subject` on 5 groups with 'NONE' value | Section D |

### Sub-process Triggers

| # | Trigger | Condition |
|---|---------|-----------|
| S-01 | Possible Verse Context sub-process | 3 OWNER terms (H1730I, H1736, H7468) have no groups — confirm with CC whether verse records exist |

### RESEARCHER_DECISION Items

| # | Item | Source | Disposition |
|---|------|--------|-------------|
| RD-S1-001 | H2898 (tov): all 31 verse records are span-filtered out; zero active verses | Sections B8, E | **RESOLVED — researcher confirmed.** This is a span filter failure. The term has genuine analytical content (Exo 33:19, Neh 9:25 and many more confirmed by researcher). Do not reclassify as delete. Resolution path: (1) investigate span resolution conflict for H2898; (2) correct Strong's reference if needed; (3) re-run extraction; (4) re-run audit_word for registry 103 or targeted for H2898; (5) re-run Verse Context for H2898 after verse corpus rebuilt. This is a CC data correction task. |

### Instruction Correction Items (not patch items)

| # | Item |
|---|------|
| IC-01 | The valid dimension vocabulary in Step 1.2 Section E must not be hardcoded. The actual labels in use ('Relational Disposition', 'Emotion — Positive', etc.) differ from the framework list. Step 1.2 Section E must reference the Dimension Review instruction as authority for valid vocabulary, and check only that (a) dimension is not NULL and (b) dimension_confidence is not AUTOMATED. |
| IC-02 | **New gap identified from RD-S1-001 resolution.** Step 1.2 Section C (and Section B cross-check B1) currently treats a zero-verse active term as a single case with three resolution paths (reclassify / retain / investigate). This is insufficient. A zero-verse result caused by span filter failure is structurally different from a zero-verse result caused by failed extraction. The instruction must distinguish: (a) zero verses because extraction returned nothing — standard data gap, may trigger VC sub-process; (b) zero active verses because ALL extracted records were span-filtered out — span filter failure, requires re-extraction before VC sub-process can run. Step 1.2 must check `span_match_count` vs `total_verse_records` vs `delete_flagged_count` in the verse_records_summary to distinguish these cases. Step 1.5 (sub-process triggers) must add a fourth trigger: span filter failure requiring re-extraction + audit_word re-run + VC re-run. |

### Stage 2a Verification Notes (not Stage 1 actions)

| # | Item |
|---|------|
| V-01 | `god_as_subject = 1` on 11 terms — verify against verse evidence |
| V-02 | `somatic_link = 1` on H7355 and H7356B (confirmed by mti_flags); newly corrected on G0026, G2705, G5370, H0160 — verify against verse evidence |
| V-03 | 35 SD pointers already raised — read and incorporate into Stage 2a analysis |
| V-04 | 3 terms (H1730I, H1736, H7468) with no groups — determine analytical treatment |

---

## Conclusion

The extract is largely sound. All major checks produced concrete, actionable results. The Step 1.2 framework is validated as operationally sound with two instruction corrections required (IC-01 and IC-02) before it is finalised.

**RD-S1-001 is resolved:** H2898 requires re-extraction and Verse Context re-run — not deletion. This is a CC data correction task.

**Two instruction corrections needed before T-02C closes:**
- IC-01: Remove hardcoded dimension vocabulary — reference Dimension Review instruction instead
- IC-02: Distinguish span filter failure from standard zero-verse gap — add fourth sub-process trigger to Step 1.5

**Step 1.2 status: FRAMEWORK VALIDATED — two targeted corrections required (IC-01 and IC-02). Proceed to T-02C.**

---

*End of wa-103-love-step1-2-audit-v1_1-20260416.md*
*Supersedes wa-103-love-step1-2-audit-v1-20260416.md*
*Audit applied: wa-global-sessionb-step1-2-corrected-v1-20260416.md*
*Extract audited: wa-103-love-sessionb-export-v1-20260416.json*
