# WA — Session B Instruction: Step 1.2 Full Rewrite
**Filename:** wa-global-sessionb-step1-2-v2-20260416.md
**Date:** 2026-04-16
**Version:** v2.0
**Change note (v2.0):** Full clean rewrite. Incorporates IC-01 through IC-07 and structural weaknesses W1–W3 identified during love extract validation test. Primary change: resolution classification framework added as governing structure — all checks now reference one of four named resolution paths. Section A.0 (statistics pre-read) and Section A.1 (audit_word history) added. Section B restructured by term_owner_type. Span filter failure detection added (IC-02). Deleted terms cross-table check added (IC-04). Dimension vocabulary hardcoding removed (IC-01). Set-aside NULL reason check added (IC-06). Section H hard gate extended with three additional stopping conditions (W3). Every anomaly action now specifies path, table/field/value or process sequence, and recording requirement.
**Supersedes:** wa-global-sessionb-step1-2-corrected-v1-20260416.md (v1.0)
**Previous output refs:**
- wa-global-sessionb-step1-2-corrected-v1-20260416.md (v1.0 — superseded)
- wa-103-love-step1-2-audit-v1_1-20260416.md (validation test — identified all corrections)
- wa-global-sessionb-update-tasklist-v1_13-20260416.md (T-02C — governing task)

---

## Step 1.2 — Read and Audit the Complete JSON

### Governing principle

Step 1.2 validates that the data is complete, correct, and internally consistent before any analytical work begins. It does not perform analysis. Every check either confirms the data is sound or assigns the anomaly to one of four resolution paths.

Read the complete word data export in full before beginning any checklist section. Do not check fields as you encounter them — read the entire extract first, form an overall picture of the data, then work through each section systematically.

Record every gap, anomaly, and resolution assignment in the observations log at the moment it is identified — per GR-OBS-001. Do not accumulate in memory.

---

### Resolution Classification Framework

Every anomaly identified in Step 1.2 is assigned to exactly one of the four resolution paths below. The path determines the action. No anomaly is recorded without a path assignment. No anomaly is left with only "note" — every note either has a path or is not an anomaly.

**Path 1 — Type (a) patch (Claude AI fixes)**
*Applies when:* The correct value is determinable from the extract data alone, without verse reading or researcher judgement. Claude AI can construct the fix.
*Method:* Record in observations log: `PATH 1 — [table].[field]: current value = [x], correct value = [y]. Add to Type (a) patch accumulator.` State the exact table, field, and corrected value. These are compiled into the Type (a) patch at Step 1.4.
*Examples:* `language` mismatch with Strong's prefix; `delete_flagged=0` on a deleted term; `dominant_subject='NONE'` correctable from group description; missing `SMALL_VERSE_SAMPLE` quality flag; `mti_status` NULL on an XREF term (correct value: `xref_[owning_word]`); `somatic_link` inconsistent with `mti_term_flags` (where `mti_term_flags` is authoritative per GR-DATA-003).

**Path 2 — Process re-run directive (CC executes)**
*Applies when:* The data structure requires a process to be rebuilt — field patching alone cannot correct it. The verse corpus, the verse context classification, or the dimension assignments need to be re-generated.
*Method:* Record in observations log: `PATH 2 — Process re-run required: [process name]. Scope: [full registry / targeted: term [strongs]]. Sequence: [steps in order]. Session B is PAUSED at Step 1.2 until this directive is complete and confirmed by CC.` Identify the correct process and scope:
- **Span filter failure** (term has `span_match_count > 0` but `total_verse_records = 0`): re-extraction → audit_word re-run → Verse Context classification. Scope: targeted to the affected term(s).
- **Genuine zero-verse extraction** (term has `span_match_count = 0` and `total_verse_records = 0`): re-extraction → audit_word re-run. Scope: targeted.
- **OWNER term with no verse_context_groups** but verse records exist: Verse Context sub-process. Scope: targeted to the affected term(s).
- **Group with AUTOMATED dimension confidence**: Dimension Review sub-process. Scope: targeted to the affected group(s).
- **Group with NULL dimension**: Dimension Review sub-process. Scope: targeted.
Process re-run directives are produced as plain-language directives to CC per GR-DIR-001 and submitted for researcher approval before CC executes. Session B does not proceed past Step 1.2 until all Path 2 items are resolved and a fresh extract is confirmed.

**Path 3 — Stage 2a verification note (deferred, non-blocking)**
*Applies when:* The field value may be wrong but cannot be confirmed or corrected without reading verses. Stage 1 cannot make a determination. Stage 2a will make the determination when verses are read.
*Method:* Record in observations log: `PATH 3 — [table].[field] on [strongs]: current value = [x]. Cannot verify in Stage 1 — requires verse reading. Note for Stage 2a verification.` Do not patch. Do not block. The Stage 2a observations log will address these.
*Examples:* `god_as_subject` plausibility (cannot verify without verse reading); `somatic_link` value where `mti_term_flags` and `wa_term_inventory` agree but verse evidence may contradict; dimension assignment where confidence is CLAUDE_AI but the label appears inconsistent with the group description.

**Path 4 — RESEARCHER_DECISION (human decision required)**
*Applies when:* The anomaly cannot be resolved analytically, cannot be corrected by Claude AI alone, is not a process re-run case, and requires a human decision on direction. Apply Path 4 only after confirming Paths 1–3 do not apply and stating why.
*Method:* Record in observations log: `PATH 4 — RESEARCHER_DECISION accumulator: [RD-ID]. What was checked: [specific field/table/value]. Why unresolvable: [Path 1 ruled out: reason. Path 2 ruled out: reason. Path 3 ruled out: reason]. Question: [precisely stated]. Options: [option A — consequence; option B — consequence]. Claude AI recommendation: [one option with reasoning].` These are collected and presented as the formal RD block after Step 1.3c is complete. Session B does not proceed past Step 1.4 until all RD items are resolved.
*Examples:* `session_b_status = Analysis Complete` when Session B appears already run; `carry_forward = 0`; `word` field mismatch; term with genuine zero-verse extraction where reason is unclear; any situation where options have meaningfully different programme consequences.

**Resolution path decision rule:**
1. Can the correct value be determined from the extract data alone, without verse reading? → Path 1
2. Does the data structure require a process to be re-run? → Path 2
3. Does confirmation require reading verses? → Path 3
4. None of the above apply and human judgement is needed? → Path 4

---

### Section A.0 — Statistics Pre-Read

Before running any section-by-section checks, read the `statistics` section of the extract. This section provides self-reported counts that serve as a first-pass orientation signal.

**Record in observations log:** All statistics values. Then check the following internal consistency pairs:

| Pair to compare | Expected relationship | If inconsistent |
|-----------------|----------------------|-----------------|
| `active_owner_term_count` vs count of OWNER terms in `terms.active_terms` | Should match | Path 1 if extract count differs from statistics count — note discrepancy; stale registry data |
| `somatic_link_inventory_count` vs `somatic_link_mti_flag_count` | Should match | Path 3 — note discrepancy; cross-check B3 will detail which terms are affected |
| `god_as_subject_inventory_count` vs god_as_subject count in `terms.active_terms` | Should match | Path 3 — note discrepancy; cross-check B in detail |
| `active_group_count` vs count of groups in `verse_context_groups` | Should match | Note discrepancy — check for soft-deleted groups in the count |
| `groups_without_dimension` | Should be 0 | Path 2 (Dimension Review sub-process) if > 0 |
| `groups_at_automated_confidence` | Should be 0 | Path 2 (Dimension Review sub-process) if > 0 |
| `session_b_flags_unresolved` | Should be 0 | Note count — these will be Step 1.3c items |
| `catalogue_questions_master` | Should be 194 or more | Path 4 if < 194 — catalogue may be stale |
| `catalogue_links_total` vs `findings_by_status` counts | Informational — note both | Record for Step 1.3b context |

**Record in observations log:** `Section A.0 complete. Statistics read. Internal consistency: [pass / [n] discrepancies noted]. Discrepancies: [list]. Proceeding to Section A.1.`

---

### Section A.1 — Audit_word History and Unresolved REVIEW Flags

Read the `patch_history.word_run_states` section of the extract. This records every prior audit_word run and its outcome. Unresolved REVIEW flags from prior runs are open items that Session B inherits.

**For each `word_run_state` row:**

1. Note the `run_id`, `audit_result`, and `audit_detail`.
2. If `audit_result = 'PASS'`: record and proceed. No action.
3. If `audit_result = 'REVIEW'` and `researcher_approved = 1`: record as previously reviewed. No action unless the current extract shows the issue persists.
4. If `audit_result = 'REVIEW'` and `researcher_approved = 0`: this is an **inherited open item**. For each REVIEW flag in `audit_detail`:

| Flag code | Meaning | Resolution path |
|-----------|---------|----------------|
| WR-05 (ID gaps in wa_term_inventory) | Sequence gaps in term IDs — may indicate missing records | Path 3 — note; not analytically blocking but record for awareness |
| WR-08 (Low verse/occurrence ratio) | Specific terms have verse counts < 20% of occurrence count | Cross-check against Section C — if not already flagged, assign Path 1 (missing SMALL_VERSE_SAMPLE flag) or Path 2 (span filter failure) as appropriate |
| WR-20 (NULL span_strong_match on verse records) | Back-population step may not have completed for pre-v9 records | Path 3 — note count; these verses have unvalidated span matching; flag for Stage 2a awareness |
| Other WR codes | Read the description | Apply resolution path decision rule above |

**Persistent flags** (same flag appearing across multiple `audit_result = 'REVIEW'` runs with `researcher_approved = 0`): these are higher priority — they have not been resolved across multiple sessions. Record as persistent and note for RESEARCHER_DECISION accumulator if they cannot be assigned Path 1, 2, or 3.

**Record in observations log:** `Section A.1 complete. [n] audit runs reviewed. [n] REVIEW flags inherited, [n] previously approved, [n] open and dispositioned as follows: [list of flag → path assignments].`

---

### Section A — Registry Record (`word_registry`)

One row per word. These fields describe the word's overall programme state.

| Field | Valid state | Check | Path | Action |
|-------|------------|-------|------|--------|
| `word` | Matches the word being analysed | Confirm spelling matches session context | 4 | Mismatch — RESEARCHER_DECISION: confirm correct registry before proceeding |
| `no` | Matches registry number [nnn] | Confirm | 4 | Mismatch — STOP immediately; confirm with researcher |
| `cluster_assignment` | A valid cluster code (C01–C22) | Present, not NULL, not 'unassigned' | 4 | NULL or 'unassigned' — RESEARCHER_DECISION: confirm cluster assignment before proceeding |
| `session_b_status` | `Pre-Analysis Complete` (required) or `Verse Context Reset` (legacy acceptable) | Check against valid values — Appendix A.5 of patch spec | 4 | `Analysis Complete` or `Session B Complete` — RESEARCHER_DECISION: Session B may already have run; confirm before proceeding. `NULL` — RESEARCHER_DECISION: word may not have completed DataPrep. |
| `verse_context_status` | `Complete` | Confirmed against Appendix A.7 of patch spec | Hard gate | Not `Complete` — STOP. Verse Context must complete first. This is a hard gate — record and halt. |
| `dim_review_status` | `Complete` | Present and matches | Hard gate | Absent or incomplete — STOP. Dimension Review must complete first. Hard gate. |
| `dim_review_version` | Populated | Not NULL | 3 | NULL — note for Stage 2a; not blocking |
| `dimensions` | Populated — at least one value | Not NULL or empty | 4 | NULL or empty — RESEARCHER_DECISION: Dimension Review may not have written output to registry |
| `carry_forward` | 1 | If 0 — note explicitly | 4 | 0 — RESEARCHER_DECISION: this registry is flagged for exclusion; confirm whether to proceed |
| `unique_term_count` | Should approximate OWNER term count in extract | Cross-check: count OWNER terms in `terms.active_terms`; compare | 1 | Discrepancy > 10% — Path 1: note; update `unique_term_count` in patch if extract count is verifiably more current |
| `shared_term_count` | ≥ 0 | Present | 1 | NULL — Path 1: set to 0 |
| `term_sharing_ratio` | 0.0–1.0; consistent with `shared / (unique + shared)` | Plausibility check | 3 | Significant deviation — Path 3: note; not analytically blocking |
| `phase1_term_count` | > 0 | Present | 3 | NULL or 0 — Path 3: note; may indicate incomplete Session A |
| `phase1_verse_count` | > 0 | Present | 3 | NULL or 0 — Path 3: note |

**Cross-field check A1 (hard gates):** `verse_context_status = 'Complete'` AND `dim_review_status = 'Complete'` must BOTH be true. If either fails: STOP. Do not proceed to any further section.

**Record in observations log:** `Section A complete. Hard gates: [PASS/FAIL]. Path 1 items: [n]. Path 4 items: [n]. Anomalies: [list].`

---

### Section B — Term Inventory

The extract contains three distinct term populations. Each has different validity expectations and different checks. Work through each population separately.

#### B1 — Active OWNER terms (`term_owner_type = 'OWNER'`, `mti_terms.status IN ('extracted','extracted_thin')`)

These are the primary analytical terms for this registry. Every field must be sound.

| Field | Valid state | Check | Path | Action |
|-------|------------|-------|------|--------|
| `strongs_number` | Format H[digits][suffix] or G[digits][suffix]; no spaces | Regex check: `^[HG]\d+[A-Z]?$` | 1 | Malformed — Path 1: correct in `wa_term_inventory.strongs_number` |
| `language` | 'Hebrew' for H prefix; 'Greek' for G prefix | Cross-check prefix vs language field | 1 | Mismatch — Path 1: correct `wa_term_inventory.language` |
| `transliteration` | Present | Not NULL | 3 | NULL — Path 3: note; not analytically blocking |
| `step_search_gloss` OR `word_analysis_gloss` | At least one present | Not both NULL | 3 | Both NULL — Path 3: note; term may lack STEP data |
| `occurrence_count` | > 0 | Numeric, > 0 | 3 | 0 or NULL — Path 3: note; cross-check against verse records in Section C |
| `mti_terms.status` | `extracted` or `extracted_thin` | Confirm value in Appendix A.4 of patch spec | 1 | Value not in controlled vocabulary — Path 1: correct `mti_terms.status` |
| `evidential_status` | NULL at Session B entry (will be set in Stage 2) | Note if already populated | 3 | If populated: record value; confirm in Stage 2a |
| `god_as_subject` | 0 or 1; plausible for term type | Populated; if 1 on a function word or particle — implausible | 3 | NULL — Path 1: set to 0 as safe default. Implausible value — Path 3: note for Stage 2a verification. Do not attempt correction without verse reading. |
| `somatic_link` | Must be consistent with `mti_term_flags` (flag_id IN (3,4)) per GR-DATA-003 | Compare `somatic_link` on `wa_term_inventory` against presence of flag_id 3 or 4 in `mti_term_flags` for this term | 1 | `somatic_link=0` but somatic mti_flag present: Path 1 — set `somatic_link=1` (mti_term_flags is authoritative). `somatic_link=1` but no somatic mti_flag: Path 3 — note for Stage 2a verification; do not remove without verse evidence. |
| `causative_form_present` | 0 or 1 | Populated | 1 | NULL — Path 1: set to 0 |
| `delete_flagged` | 0 for active terms | Must be 0 | 4 | If 1 — this term is soft-deleted but appearing in active set. RESEARCHER_DECISION: investigate why deleted term is in active population. |
| `term_owner_type` | 'OWNER' | Confirmed | 1 | NULL — Path 1: set to 'OWNER' based on context |
| `parsed_meaning_id` | FK resolves in `wa_meaning_parsed` if populated | Verify FK if not NULL | 1 | Dangling FK — Path 1: set to NULL (broken reference is worse than absent) |

**Cross-check B1 — occurrence count vs verse records:**
For each OWNER term, retrieve from `verse_records_summary`: `span_match_count`, `total_verse_records`, `delete_flagged_count`.

Apply the following diagnostic:

| Condition | Diagnosis | Path | Action |
|-----------|-----------|------|--------|
| `span=0, active=0, deleted=0` | No verses extracted at all | 2 | Re-extraction → audit_word re-run. Note: targeted to this term. Session B paused until complete. |
| `span>0, active=0, deleted=span` | Span filter failure — all verses filtered out | 2 | Re-extraction → audit_word re-run → Verse Context re-classification. Note: targeted. Session B paused. Record: `[strongs] span filter failure. [n] records extracted, all deleted by span filter. Genuine verse content confirmed exists (term has [occ] occurrences). Path 2: re-extraction required.` |
| `span>0, active>0` | Normal — verses present | Continue | Check ratios below |
| `active > occ * 1.1` | Possible over-extraction | 4 | RESEARCHER_DECISION: verse count exceeds occurrence count by > 10%. Possible duplicate records or incorrect span matching. |
| `active < occ * 0.2` AND `occ > 20` | Small verse sample | 1 | Check `wa_data_quality_flags` for this term. If no `SMALL_VERSE_SAMPLE` flag: Path 1 — add quality flag. If flag exists: PASS. |

**Cross-check B2 — OWNER terms with no verse_context_groups:**
For each OWNER term: check whether at least one group exists in `verse_context_groups` for this `mti_term_id`.

| Condition | Path | Action |
|-----------|------|--------|
| Term has verse records AND at least one group | PASS | Continue |
| Term has verse records but zero groups | 2 | Verse Context sub-process — targeted to this term |
| Term has zero active verse records (caught in B1) | Already handled in B1 | Do not duplicate |

**Cross-check B3 — god_as_subject consistency with statistics:**
Compare `statistics.god_as_subject_inventory_count` against count of OWNER terms in the extract with `god_as_subject = 1`. If these match the statistics pre-read: PASS. If they differ: Path 3 — note discrepancy; the statistics field reflects the database state at export time.

#### B2 — XREF terms (`term_owner_type = 'XREF'`)

Cross-registry terms — primary analysis in another registry. Lighter checks.

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `mti_terms.status` | Should be `xref_[owning_word]` per Appendix A.4 | 1 | NULL or wrong value — Path 1: set to `xref_[owning_word]` where owning_word is from `mti_terms.owning_word` or `owning_registry_word` in the extract |
| `owning_registry_no` | Must reference a valid, registered word in the programme | Confirm registry exists in extract context | 4 | Owning registry not recognised — RESEARCHER_DECISION: XREF term points to an unregistered word |
| Verse records | May have zero active verses — this is acceptable for XREF terms | Note count | 3 | Zero active verses — Path 3: note; XREF terms are not primary analytical subjects; absence is not a data gap |
| `delete_flagged` | 0 | Must be 0 in active XREF set | 4 | If 1 — soft-deleted XREF in active set; RESEARCHER_DECISION |

Record in observations log: `XREF terms: [n] reviewed. [n] with NULL mti_status corrected to xref_[word] (Path 1). [n] with valid owning registry. [n] path 3 notes.`

#### B3 — Deleted terms (`mti_terms.status = 'delete'`)

Deleted terms are outside analytical scope. One cross-table consistency check only.

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `wa_term_inventory.delete_flagged` | Should be 1 for deleted terms | For each deleted term: confirm `delete_flagged = 1` on its `wa_term_inventory` row | 1 | `delete_flagged = 0` on a deleted term — Path 1: set `delete_flagged = 1`. This is a data consistency correction. Note count: `[n] deleted terms had delete_flagged=0; corrected in Type (a) patch.` |

Record in observations log: `Section B complete. OWNER terms: [n] reviewed. Path 1 items: [n]. Path 2 items: [n] (span filter failure: [n]; zero extraction: [n]; no groups: [n]). Path 3 notes: [n]. Path 4 items: [n]. XREF terms: [n] reviewed. [n] mti_status corrected. Deleted terms: [n], [n] delete_flagged corrections.`

---

### Section C — Verse Records (`wa_verse_records`)

The three-number diagnostic for each term was applied in Section B cross-check B1. Section C supplements this with checks on verse record quality.

For each term in `verse_records_summary` where `total_verse_records > 0`:

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `verse_text` populated | Not NULL or empty string | 3 | NULL verse text — Path 3: note; verse cannot be read in Stage 2a; record reference |
| `reference` format | [Book] [Chapter]:[Verse] e.g. 'Rom 3:23' | Plausibility check | 1 | Malformed reference — Path 1: correct if pattern is clear; otherwise Path 3 note |
| `span_strong_match` | 0 or 1 | Populated | 3 | NULL span_strong_match — Path 3: note count; back-population (WR-20) may not have completed for pre-v9 records; these verses have unvalidated span matching |
| `translation` | 'ESV' (programme standard) | Confirm | 4 | Non-ESV translation — RESEARCHER_DECISION: confirm whether this is intentional or an import anomaly |
| `delete_flagged` | 0 for active verse records | Must be 0 in active set | 4 | If 1 — soft-deleted verse in active count; RESEARCHER_DECISION |

**NULL span_strong_match count:** If WR-20 was flagged in Section A.1, the count of NULL span_strong_match records should be consistent with the audit_word detail. If the count has grown since the last audit run: Path 4 — RESEARCHER_DECISION.

Record in observations log: `Section C complete. Verse records checked. NULL verse_text: [n]. NULL span_strong_match: [n] (consistent with WR-20: [yes/no]). Path items: [n].`

---

### Section D — Verse Context Groups (`verse_context_group` + `verse_context`)

#### D1 — Groups

| Field | Valid state | Path | Action |
|-------|------------|------|--------|
| `group_code` | Format: [mti_term_id]-[seq] e.g. '1234-001' | Present, unique, correctly formatted | 1 | Malformed — Path 1: correct format. Duplicate code — Path 4: RESEARCHER_DECISION |
| `context_description` | Present, substantive (> 20 characters) | Not NULL, not a placeholder | 4 | NULL or < 20 chars — RESEARCHER_DECISION: blank descriptions block analytical grouping; Verse Context re-run may be required |
| `delete_flagged` | 0 for active groups | Must be 0 | 4 | If 1 — soft-deleted group in active set; RESEARCHER_DECISION |
| `mti_term_id` | FK to a term in the active or XREF term set | Verify term is in the extract | 1 | FK to a deleted term — Path 1: note as data integrity gap; the group references a term outside scope |

#### D2 — Anchor verses within groups

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| Each group has ≥ 1 `is_anchor = 1` verse | Count of anchor verses > 0 per group | 2 | Zero anchor verses in a group — Path 2: targeted Verse Context re-run for this group |
| `is_anchor` and `is_related` not both 1 on same verse | Mutually exclusive | 1 | Contradiction — Path 1: correct `is_related = 0` where `is_anchor = 1` |
| `delete_flagged = 0` for active verses | 0 | 4 | Soft-deleted verse in active count — RESEARCHER_DECISION |

#### D3 — Set-aside verses

| Check | Valid state | Path | Action |
|-------|------------|------|--------|
| `set_aside_reason` populated | Should have a reason | 3 | NULL reason — Path 3: count NULL-reason set-asides. If > 20% of total set-aside: note as unverifiable set-aside; Stage 2a should examine a sample. Not blocking. |

**Cross-check D1 — dominant_subject:**
For each active group, check `dimension_assignment.dominant_subject`. Valid values: 'God', 'Human', 'Mixed', 'Community', 'Other'.

| Condition | Path | Action |
|-----------|------|--------|
| `dominant_subject` is NULL | 4 | RESEARCHER_DECISION: cannot be set without reading the group's verses |
| `dominant_subject` = 'NONE' (string) | 1 | Path 1: determine correct value from group description alone. If group description clearly indicates human activity → 'Human'. Divine activity → 'God'. Mixed → 'Mixed'. If unclear from description alone → Path 4 |
| `dominant_subject` is a valid value | PASS | Continue |

**Cross-check D2 — verse counts vs dimension index:**
For each group with a `dimension_assignment`: compare `anchor_count + related_count` in the dimension_assignment data against the actual count of `is_anchor` and `is_relevant` verse_context rows for that group.

| Condition | Path | Action |
|-----------|------|--------|
| Counts match within 5% | PASS | Continue |
| Counts differ by > 5% | 3 | Path 3: note as stale dimension index counts; not blocking; Stage 2a will use live verse data |

Record in observations log: `Section D complete. Groups: [n] active. Anchor check: [n] groups with no anchors (Path 2). Dominant subject: [n] NULL (Path 4), [n] 'NONE' corrected (Path 1). Set-aside NULL reason: [n] of [total] ([%]).`

---

### Section E — Dimension Assignments (`wa_dimension_index`)

For each group in the extract, check its `dimension_assignment` sub-object.

| Field | Valid state | Path | Action |
|-------|------------|------|--------|
| `dimension` | Not NULL | Any non-NULL value from Dimension Review is acceptable. The Dimension Review instruction governs valid vocabulary — do not validate vocabulary here. | 2 | NULL dimension — Path 2: Dimension Review sub-process for this group |
| `dimension_confidence` | `CLAUDE_AI` or `RESEARCHER` | Not `AUTOMATED` | 2 | `AUTOMATED` — Path 2: Dimension Review sub-process for this group |
| `dominant_subject` | See Section D cross-check D1 | Already checked in Section D | — | Handled in Section D |
| `manual_override` | 0 or 1 | Populated | 1 | NULL — Path 1: set to 0 |
| `delete_flagged` | 0 for active rows | Must be 0 | 4 | If 1 — soft-deleted dimension row in active set; RESEARCHER_DECISION |
| `owning_registry_no` | Must match this registry's `no` | Cross-check | 4 | Mismatch — RESEARCHER_DECISION: dimension row may belong to another registry |

**Cross-check E1 — every active group has exactly one dimension assignment:**
For each group in `verse_context_groups`: confirm exactly one `dimension_assignment` sub-object is present.

| Condition | Path | Action |
|-----------|------|--------|
| 0 dimension rows | 2 | Dimension Review sub-process |
| 1 dimension row | PASS | Continue |
| > 1 dimension rows | 4 | RESEARCHER_DECISION: duplicate dimension assignments for same group |

**Cross-check E2 — Somatic/Embodied dimension vs somatic term flags:**
Note: dimension vocabulary varies by programme version. Do not test for a specific dimension label. Instead: for groups where the dimension label contains 'Somatic' or 'Embod' (case-insensitive): confirm the corresponding term has `somatic_link = 1` in `wa_term_inventory` or a somatic flag in `mti_term_flags`. If inconsistent: Path 3 — note for Stage 2a verification.

**Cross-check E3 — Theological/Divine-Human dimension vs god_as_subject:**
For groups where the dimension label contains 'Theolog' or 'Divine' or 'God' (case-insensitive): confirm the corresponding term has `god_as_subject = 1` or a GOD_AS_SUBJECT flag in `mti_term_flags`. If inconsistent: Path 3 — note for Stage 2a verification.

Record in observations log: `Section E complete. [n] groups with dimension assignments. NULL dimension: [n] (Path 2). AUTOMATED confidence: [n] (Path 2). Somatic/Divine consistency notes: [n] (Path 3).`

---

### Section F — Existing Findings and Flags (counts and orientation)

Section F is situational awareness only. Detailed review happens in Step 1.3. Do not action items here.

**F1 — `wa_session_b_findings`:**
From extract or from CC: count rows for registry [nnn] where `delete_flag = 0`. Note: total active, count by status (`pending` / `in_review` / `complete`), count with catalogue links.
Record: `Findings for registry [nnn]: [n] active. Status: pending=[n], in_review=[n], complete=[n]. Catalogue links: [n]. Step 1.3b will process these.`

**F2 — `wa_session_research_flags`:**
Count rows by `session_target` and `resolved`.
Record: `Research flags for registry [nnn]: Session D: [n] total, [n] unresolved. Session B: [n] total, [n] unresolved.`
B-target unresolved count: if > 0, record: `[n] B-target flags will be addressed in Step 1.3c.`

**F3 — `wa_term_phase2_flags`:**
Count rows for active terms where `delete_flagged = 0`.
Record: `Phase2 flags: [n] across [n] terms. Step 1.3a will assess these.`

**F4 — `wa_obs_question_catalogue`:**
Confirm master catalogue count from extract statistics: should be 194 or more.
Confirm registry-specific questions count: these are the questions already indexed for this word.
Record: `Catalogue: master=[n], registry-indexed=[n].`

**F5 — `correlation_signals`:**
Note: ranked pairs, xref sharing pairs, shared anchor verse count.
Record: `Correlation signals: [n] ranked pairs, [n] shared anchors. Stage 2a will read these.`

---

### Section G — Supporting Term Data

Check for presence and basic consistency. Do not perform analytical review.

**G1 — Meaning data (`wa_meaning_parsed` / `wa_meaning_sense` / `wa_meaning_stem`):**
For each active OWNER term:
- `parsed_meaning_id` populated → confirm FK resolves. If dangling: Path 1 — set to NULL.
- `wa_meaning_parsed` row present → confirm `wa_meaning_sense` has at least one row. Zero senses on a populated parse: Path 3 — note as incomplete parse.
- `has_causative_stem = 1` → confirm at least one `wa_meaning_stem` row. Absent: Path 3 — note.
- No meaning data at all → confirm `NO_WORD_ANALYSIS` quality flag is present. Absent: Path 1 — add quality flag.

**G2 — Root families (`wa_term_root_family`):**
For each active OWNER term:
- Note whether root family records are present.
- `root_code` must be populated if row exists: Path 1 if NULL.
- `root_language` should match term's language: Path 1 if mismatch.
- Zero root family records: not anomalous — note count only.

**G3 — Related words (`wa_term_related_words`):**
For each active OWNER term:
- Note count of related word records.
- Zero related words for a primary term with high occurrence count: Path 3 — note; may indicate limited STEP data.

**G4 — LSJ data (`wa_lsj_parsed`, Greek terms only):**
For Greek OWNER terms:
- Note whether `wa_lsj_parsed` row is present.
- Absence is not anomalous — note count only.

**G5 — Cross-registry links (`wa_cross_registry_links`):**
Note count of rows for this registry.
Record: `Cross-registry links: [n]. Stage 2a will read these.`

Record in observations log: `Section G complete. Meaning data: [n] terms with parse, [n] without. Root family gaps: [n]. Path 1 items from G: [n].`

---

### Section H — Step 1.2 Close and Hard Gate Check

After completing all sections, produce the consolidated audit summary:

```
Step 1.2 Audit Summary — Registry [nnn] [word]
Date: [date]
Extract version: [version]

Registry state:
  session_b_status = [value]
  verse_context_status = [value]
  dim_review_status = [value]
  carry_forward = [value]

Term populations:
  OWNER terms (extracted/extracted_thin): [n]
  XREF terms: [n]
  Deleted terms: [n]

Verse coverage:
  Total active verse records (OWNER terms): [n]
  Terms with span filter failure: [n] — [strongs list]
  Terms with zero active verses (genuine extraction gap): [n] — [strongs list]

Verse context groups:
  Active groups: [n]
  Groups with NULL dimension (Path 2): [n]
  Groups with AUTOMATED confidence (Path 2): [n]
  Groups with no anchor verse (Path 2): [n]
  Groups with dominant_subject issue (Path 1/4): [n]

Audit history:
  audit_word REVIEW flags inherited: [n] — [WR codes]

Resolution summary:
  Path 1 (Type (a) patch items): [n total] — [brief list]
  Path 2 (Process re-run directives): [n total] — [process: scope per item]
  Path 3 (Stage 2a verification notes): [n total] — [brief list]
  Path 4 (RESEARCHER_DECISION items): [n total] — [RD-IDs]
```

**Hard gate check — all conditions must be true before proceeding to Step 1.3:**

| Condition | Required state | If not met |
|-----------|---------------|-----------|
| `verse_context_status` | `Complete` | STOP — hard gate failure. Record and halt. |
| `session_b_status` | `Pre-Analysis Complete` or `Verse Context Reset` | STOP — confirm with researcher |
| `dim_review_status` | `Complete` | STOP — Dimension Review must complete first |
| All hard gate conditions from Section A | PASS | STOP — resolve before proceeding |
| No active OWNER term has `mti_terms.status = NULL` | 0 NULL-status OWNER terms | STOP — Path 1 patch must be confirmed before Step 1.3 |
| No active OWNER term has span filter failure (Path 2) | 0 span filter failures | STOP — Path 2 directive must be complete, re-run confirmed, fresh extract pulled |
| Unresolved `audit_word` REVIEW flags with `researcher_approved = 0` | All dispositioned to a path | If any PATH 4 items from audit history — include in RESEARCHER_DECISION block; gate holds until resolved |
| `carry_forward` | 1 | STOP — confirm with researcher |

**If all conditions are met:** Record `Step 1.2 complete. All hard gate conditions met. Path 2 directives: [none / [n] confirmed complete]. Path 4 items accumulated for RD block: [n]. Proceeding to Step 1.3.`

**If any Path 2 items remain outstanding:** Step 1.2 is not complete until the Path 2 directives have been executed by CC and a fresh extract confirming the corrected data has been pulled. Re-run Section B and Section C checks for the affected terms after the fresh extract is available.

---

*End of wa-global-sessionb-step1-2-v2-20260416.md*
*Supersedes wa-global-sessionb-step1-2-corrected-v1-20260416.md*
*For incorporation into wa-global-sessionb-instruction-v5_1-20260416.md, replacing Step 1.2*
