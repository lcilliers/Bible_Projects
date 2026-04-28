# Readiness Sweep Pilot — r001 abomination

**Pilot run:** 2026-04-19T16:35:04.001656+00:00
**Mode:** read-only (no patches applied)
**Schema version:** 3.10.0 (post-DBR)
**Script:** scripts/readiness_sweep_pilot.py
**Instruction:** wa-global-readiness-sweep-instruction-v1_0-20260419.md (Active)

---

## Registry Summary

| Field | Value |
| --- | --- |
| registry_id | 1 |
| file_id_count | 1 |
| word | abomination |
| cluster_assignment | C12 |
| session_b_status | Verse Context Reset |
| verse_context_status | Complete |
| dim_review_status | None |
| carry_forward | 1 |
| owner_terms | 30 |
| xref_terms | 9 |
| god_flagged_terms | 4 |
| somatic_flagged_terms | 1 |
| active_verse_records | 227 |
| active_groups | 26 |
| active_dimension_rows | 26 |
| null_dimension | 1 |
| automated_confidence | 26 |
| legacy_vocab_labels | 0 |
| findings_active | 1 |
| research_flags_B_unresolved | 0 |
| research_flags_D_unresolved | 1 |
| phase2_flags_live | 17 |
| catalogue_extensions | 0 |
| owner_with_meaning | 30 |
| owner_missing_meaning | 0 |
| cross_registry_links | 6 |
| prose_section_count | 0 |
| session_a_sections | 0 |

---

## Findings by Path

| Path | Count | Description |
| --- | --- | --- |
| 1 | 7 | Mechanical patch (Path 1) |
| 2 | 16 | Sub-process directive (Path 2) |
| 3 | 1 | Deferred to per-word Stage 1 (Path 3) |
| 4 | 44 | RESEARCHER_DECISION (Path 4) |
| 5 | 1 | Outstanding task — beyond CC skill (Path 5) |

**Total findings:** 69

---

## Findings by Phase

### Phase R.A — 2 finding(s)

- **Path 4** · `word_registry.no=1` — dim_review_status=None → Hard gate — Dimension Review must complete
- **Path 3** · `word_registry.word_synopsis` — NULL → Deferred — researcher authors per Session A advice Q7

### Phase R.B — 38 finding(s)

- **Path 4** · `mti_terms.id=4535` — OWNER term has status='candidate_delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=4536` — OWNER term has status='candidate_delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=2046` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=2047` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=2048` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=2050` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=2051` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3279` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3277` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3282` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3283` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3285` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3286` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=3287` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 1** · `wa_term_inventory.id=4658` — XREF term has mti_terms.status=NULL → Path 1: set to xref_[owning_word]
- **Path 1** · `wa_term_inventory.id=4658` — XREF term has mti_terms.status=NULL → Path 1: set to xref_[owning_word]
- **Path 1** · `wa_term_inventory.id=4658` — XREF term has mti_terms.status=NULL → Path 1: set to xref_[owning_word]
- **Path 4** · `wa_term_inventory.id=4658` — XREF term has mti_terms.status='extracted' → RD: unexpected status on XREF
- **Path 1** · `wa_term_inventory.id=4659` — XREF term has mti_terms.status=NULL → Path 1: set to xref_[owning_word]
- **Path 4** · `wa_term_inventory.id=4659` — XREF term has mti_terms.status='extracted' → RD: unexpected status on XREF
- **Path 1** · `wa_term_inventory.id=4665` — XREF term has mti_terms.status=NULL → Path 1: set to xref_[owning_word]
- **Path 4** · `wa_term_inventory.id=4665` — XREF term has mti_terms.status='extracted' → RD: unexpected status on XREF
- **Path 1** · `wa_data_quality_flags (term G0946)` — small verse sample: active=6, occ=117 → Path 1: INSERT SMALL_VERSE_SAMPLE quality flag
- **Path 2** · `wa_term_inventory.id=4656 (G8238)` — zero extraction (occ=2, no verse records) → Path 2 directive: re-extract + audit_word re-run (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4657 (G6662)` — zero extraction (occ=2, no verse records) → Path 2 directive: re-extract + audit_word re-run (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4662 (H0889)` — span filter failure (span=3, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4663 (H0891)` — span filter failure (span=2, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4664 (H0873)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4666 (H0890)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4667 (H0892)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4668 (G5087)` — span filter failure (span=85, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 1** · `wa_data_quality_flags (term G1303)` — small verse sample: active=6, occ=92 → Path 1: INSERT SMALL_VERSE_SAMPLE quality flag
- **Path 2** · `wa_term_inventory.id=4671 (G4934)` — span filter failure (span=3, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4672 (G0394)` — span filter failure (span=2, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4673 (G0475)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4674 (G2652)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4675 (G2653)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)
- **Path 2** · `wa_term_inventory.id=4676 (G4784)` — span filter failure (span=1, all deleted) → Path 2: re-extract + audit + VC (BLOCKED: OT-DBR-001)

### Phase R.D — 26 finding(s)

- **Path 4** · `verse_context_group.id=4` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=5` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=6` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=7` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=49` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=52` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=53` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=105` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=122` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=123` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=124` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=125` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=126` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=127` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=128` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=129` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=130` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=131` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=132` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=133` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=136` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=137` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=138` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=163` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=164` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=165` — dominant_subject=NULL → RD: requires verse reading to set

### Phase R.E — 2 finding(s)

- **Path 2** · `wa_dimension_index` — 1 groups with NULL dimension → Path 2: Dimension Review sub-process
- **Path 2** · `wa_dimension_index` — 26 groups at non-reviewed confidence (KEYWORD_*/ROOT_INFERRED/UNCLASSIFIED) → Path 2: Dimension Review

### Phase R.H — 1 finding(s)

- **Path 5** · `prose_section (Session A)` — No Session A sections generated for this registry → Path 5 (outstanding): generate_session_a_extract.py not yet built


---

## Next Actions

- **Path 1 (7):** build remediation patch with 7 operations.
- **Path 2 (16):** produce 16 sub-process directive(s). Execution may be blocked by OT-DBR-001 (audit_word.py rewrite) if re-extraction involved.
- **Path 3 (1):** record in outstanding tasks with DEFER_STAGE1 tag; resolved during per-word Stage 1 (v1.6).
- **Path 4 (44):** present as RESEARCHER_DECISION block; await resolution.
- **Path 5 (1):** append to outstanding tasks with capability statement.

---

*End of pilot report*