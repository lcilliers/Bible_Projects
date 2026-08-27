# Readiness Sweep Pilot — r035 covetousness

**Pilot run:** 2026-04-20T04:19:47.616934+00:00
**Mode:** read-only (no patches applied)
**Schema version:** 3.10.0 (post-DBR)
**Script:** scripts/readiness_sweep_pilot.py
**Instruction:** wa-global-readiness-sweep-instruction-v1_0-20260419.md (Active)

---

## Registry Summary

| Field | Value |
| --- | --- |
| registry_id | 35 |
| file_id_count | 1 |
| word | covetousness |
| cluster_assignment | C13 |
| session_b_status | Verse Context Reset |
| verse_context_status | Complete |
| dim_review_status | Complete |
| carry_forward | 1 |
| owner_terms | 7 |
| xref_terms | 4 |
| god_flagged_terms | 0 |
| somatic_flagged_terms | 0 |
| active_verse_records | 25 |
| active_groups | 10 |
| active_dimension_rows | 10 |
| null_dimension | 0 |
| automated_confidence | 0 |
| legacy_vocab_labels | 0 |
| findings_active | 1 |
| research_flags_B_unresolved | 0 |
| research_flags_D_unresolved | 1 |
| phase2_flags_live | 1 |
| catalogue_extensions | 0 |
| owner_with_meaning | 7 |
| owner_missing_meaning | 0 |
| cross_registry_links | 0 |
| prose_section_count | 0 |
| session_a_sections | 0 |

---

## Findings by Path

| Path | Count | Description |
| --- | --- | --- |
| 3 | 1 | Deferred to per-word Stage 1 (Path 3) |
| 5 | 1 | Outstanding task — beyond CC skill (Path 5) |

**Total findings:** 2

---

## Findings by Phase

### Phase R.A — 1 finding(s)

- **Path 3** · `word_registry.word_synopsis` — NULL → Deferred — researcher authors per Session A advice Q7

### Phase R.H — 1 finding(s)

- **Path 5** · `prose_section (Session A)` — No Session A sections generated for this registry → Path 5 (outstanding): generate_session_a_extract.py not yet built


---

## Next Actions

- **Path 1 (0):** build remediation patch with 0 operations.
- **Path 2 (0):** produce 0 sub-process directive(s). Execution may be blocked by OT-DBR-001 (audit_word.py rewrite) if re-extraction involved.
- **Path 3 (1):** record in outstanding tasks with DEFER_STAGE1 tag; resolved during per-word Stage 1 (v1.6).
- **Path 4 (0):** present as RESEARCHER_DECISION block; await resolution.
- **Path 5 (1):** append to outstanding tasks with capability statement.

---

*End of pilot report*