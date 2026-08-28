# Readiness Sweep Pilot — r182 Soul

**Pilot run:** 2026-04-19T16:50:42.014449+00:00
**Mode:** read-only (no patches applied)
**Schema version:** 3.10.0 (post-DBR)
**Script:** scripts/readiness_sweep_pilot.py
**Instruction:** wa-global-readiness-sweep-instruction-v1_0-20260419.md (Active)

---

## Registry Summary

| Field | Value |
| --- | --- |
| registry_id | 182 |
| file_id_count | 1 |
| word | Soul |
| cluster_assignment | C01 |
| session_b_status | Verse Context Reset |
| verse_context_status | Complete |
| dim_review_status | Complete |
| carry_forward | 1 |
| owner_terms | 20 |
| xref_terms | 17 |
| god_flagged_terms | 8 |
| somatic_flagged_terms | 8 |
| active_verse_records | 752 |
| active_groups | 61 |
| active_dimension_rows | 61 |
| null_dimension | 0 |
| automated_confidence | 0 |
| legacy_vocab_labels | 61 |
| findings_active | 13 |
| research_flags_B_unresolved | 0 |
| research_flags_D_unresolved | 14 |
| phase2_flags_live | 0 |
| catalogue_extensions | 0 |
| owner_with_meaning | 20 |
| owner_missing_meaning | 0 |
| cross_registry_links | 9 |
| prose_section_count | 0 |
| session_a_sections | 0 |

---

## Findings by Path

| Path | Count | Description |
| --- | --- | --- |
| 1 | 1 | Mechanical patch (Path 1) |
| 2 | 1 | Sub-process directive (Path 2) |
| 3 | 1 | Deferred to per-word Stage 1 (Path 3) |
| 4 | 67 | RESEARCHER_DECISION (Path 4) |
| 5 | 2 | Outstanding task — beyond CC skill (Path 5) |

**Total findings:** 72

---

## Findings by Phase

### Phase R.A — 1 finding(s)

- **Path 3** · `word_registry.word_synopsis` — NULL → Deferred — researcher authors per Session A advice Q7

### Phase R.B — 8 finding(s)

- **Path 4** · `mti_terms.id=1389` — OWNER term has status='phase2_enrichment' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `mti_terms.id=1395` — OWNER term has status='delete' → RD: expected extracted/extracted_thin for live OWNER
- **Path 4** · `wa_term_inventory.id=1547` — XREF term has mti_terms.status='extracted' → RD: unexpected status on XREF
- **Path 4** · `wa_term_inventory.id=1550` — XREF term has mti_terms.status='extracted_thin' → RD: unexpected status on XREF
- **Path 4** · `wa_term_inventory.id=1551` — XREF term has mti_terms.status='extracted_thin' → RD: unexpected status on XREF
- **Path 4** · `wa_term_inventory.id=1553` — XREF term has mti_terms.status='extracted_thin' → RD: unexpected status on XREF
- **Path 1** · `wa_data_quality_flags (term G5590G)` — small verse sample: active=46, occ=825 → Path 1: INSERT SMALL_VERSE_SAMPLE quality flag
- **Path 2** · `wa_term_inventory.id=1544 (G5590K)` — zero extraction (occ=1, no verse records) → Path 2 directive: re-extract + audit_word re-run (BLOCKED: OT-DBR-001)

### Phase R.D — 61 finding(s)

- **Path 4** · `verse_context_group.id=2680` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2681` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2682` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2683` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2684` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2685` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2686` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2687` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2688` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2689` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2690` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2691` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2692` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2693` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2694` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2695` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2696` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2697` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2698` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2699` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2700` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2701` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2702` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2703` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2704` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2705` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2706` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2707` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2708` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2709` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2710` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2711` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2712` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2713` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2714` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2660` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2661` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2662` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2663` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2664` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2665` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2666` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2667` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2668` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2669` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2670` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2671` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2672` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2673` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2674` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2675` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2676` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2677` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2678` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2679` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2658` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2659` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2656` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2654` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2655` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=2657` — dominant_subject=NULL → RD: requires verse reading to set

### Phase R.E — 1 finding(s)

- **Path 5** · `wa_dimension_index` — 61 rows use legacy slash-style dimension labels → Path 5 (outstanding): programme-wide vocabulary normalisation

### Phase R.H — 1 finding(s)

- **Path 5** · `prose_section (Session A)` — No Session A sections generated for this registry → Path 5 (outstanding): generate_session_a_extract.py not yet built


---

## Next Actions

- **Path 1 (1):** build remediation patch with 1 operations.
- **Path 2 (1):** produce 1 sub-process directive(s). Execution may be blocked by OT-DBR-001 (audit_word.py rewrite) if re-extraction involved.
- **Path 3 (1):** record in outstanding tasks with DEFER_STAGE1 tag; resolved during per-word Stage 1 (v1.6).
- **Path 4 (67):** present as RESEARCHER_DECISION block; await resolution.
- **Path 5 (2):** append to outstanding tasks with capability statement.

---

*End of pilot report*