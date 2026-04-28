# Readiness Sweep Pilot — r068 grace

**Pilot run:** 2026-04-19T20:30:28.013956+00:00
**Mode:** read-only (no patches applied)
**Schema version:** 3.10.0 (post-DBR)
**Script:** scripts/readiness_sweep_pilot.py
**Instruction:** wa-global-readiness-sweep-instruction-v1_0-20260419.md (Active)

---

## Registry Summary

| Field | Value |
| --- | --- |
| registry_id | 68 |
| file_id_count | 1 |
| word | grace |
| cluster_assignment | C17 |
| session_b_status | Verse Context Reset |
| verse_context_status | In Progress |
| dim_review_status | Complete |
| carry_forward | 1 |
| owner_terms | 5 |
| xref_terms | 8 |
| god_flagged_terms | 4 |
| somatic_flagged_terms | 4 |
| active_verse_records | 226 |
| active_groups | 11 |
| active_dimension_rows | 11 |
| null_dimension | 0 |
| automated_confidence | 0 |
| legacy_vocab_labels | 0 |
| findings_active | 1 |
| research_flags_B_unresolved | 0 |
| research_flags_D_unresolved | 55 |
| phase2_flags_live | 4 |
| catalogue_extensions | 147 |
| owner_with_meaning | 5 |
| owner_missing_meaning | 0 |
| cross_registry_links | 0 |
| prose_section_count | 0 |
| session_a_sections | 0 |

---

## Findings by Path

| Path | Count | Description |
| --- | --- | --- |
| 3 | 1 | Deferred to per-word Stage 1 (Path 3) |
| 4 | 4 | RESEARCHER_DECISION (Path 4) |
| 5 | 1 | Outstanding task — beyond CC skill (Path 5) |

**Total findings:** 6

---

## Findings by Phase

### Phase R.A — 2 finding(s)

- **Path 4** · `word_registry.no=68` — verse_context_status='In Progress' → Hard gate — VC must be Complete before Session B proceeds
- **Path 3** · `word_registry.word_synopsis` — NULL → Deferred — researcher authors per Session A advice Q7

### Phase R.B — 3 finding(s)

- **Path 4** · `wa_term_inventory.id=5590` — XREF term has no canonical mti_terms row (broken pointer) → RD: either restore canonical row, remove the XREF, or reclassify — see OT-DBR-009 mti_terms dedup context
- **Path 4** · `wa_term_inventory.id=5591` — XREF term has no canonical mti_terms row (broken pointer) → RD: either restore canonical row, remove the XREF, or reclassify — see OT-DBR-009 mti_terms dedup context
- **Path 4** · `wa_term_inventory.id=5593` — XREF term has no canonical mti_terms row (broken pointer) → RD: either restore canonical row, remove the XREF, or reclassify — see OT-DBR-009 mti_terms dedup context

### Phase R.H — 1 finding(s)

- **Path 5** · `prose_section (Session A)` — No Session A sections generated for this registry → Path 5 (outstanding): generate_session_a_extract.py not yet built


---

## Next Actions

- **Path 1 (0):** build remediation patch with 0 operations.
- **Path 2 (0):** produce 0 sub-process directive(s). Execution may be blocked by OT-DBR-001 (audit_word.py rewrite) if re-extraction involved.
- **Path 3 (1):** record in outstanding tasks with DEFER_STAGE1 tag; resolved during per-word Stage 1 (v1.6).
- **Path 4 (4):** present as RESEARCHER_DECISION block; await resolution.
- **Path 5 (1):** append to outstanding tasks with capability statement.

---

*End of pilot report*