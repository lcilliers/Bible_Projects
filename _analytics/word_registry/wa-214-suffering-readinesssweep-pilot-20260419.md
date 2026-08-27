# Readiness Sweep Pilot — r214 suffering

**Pilot run:** 2026-04-19T16:35:04.454269+00:00
**Mode:** read-only (no patches applied)
**Schema version:** 3.10.0 (post-DBR)
**Script:** scripts/readiness_sweep_pilot.py
**Instruction:** wa-global-readiness-sweep-instruction-v1_0-20260419.md (Active)

---

## Registry Summary

| Field | Value |
| --- | --- |
| registry_id | 214 |
| file_id_count | 1 |
| word | suffering |
| cluster_assignment | C05 |
| session_b_status | Ready for Analysis |
| verse_context_status | In Progress |
| dim_review_status | None |
| carry_forward | 1 |
| owner_terms | 0 |
| xref_terms | 0 |
| god_flagged_terms | 0 |
| somatic_flagged_terms | 0 |
| active_verse_records | 907 |
| active_groups | 12 |
| active_dimension_rows | 0 |
| null_dimension | 0 |
| automated_confidence | 0 |
| legacy_vocab_labels | 0 |
| findings_active | 0 |
| research_flags_B_unresolved | 0 |
| research_flags_D_unresolved | 0 |
| phase2_flags_live | 0 |
| catalogue_extensions | 0 |
| owner_with_meaning | 0 |
| owner_missing_meaning | 0 |
| cross_registry_links | 0 |
| prose_section_count | 0 |
| session_a_sections | 0 |

---

## Findings by Path

| Path | Count | Description |
| --- | --- | --- |
| 3 | 1 | Deferred to per-word Stage 1 (Path 3) |
| 4 | 15 | RESEARCHER_DECISION (Path 4) |
| 5 | 1 | Outstanding task — beyond CC skill (Path 5) |

**Total findings:** 17

---

## Findings by Phase

### Phase R.A — 4 finding(s)

- **Path 4** · `word_registry.no=214` — verse_context_status='In Progress' → Hard gate — VC must be Complete before Session B proceeds
- **Path 4** · `word_registry.no=214` — dim_review_status=None → Hard gate — Dimension Review must complete
- **Path 3** · `word_registry.word_synopsis` — NULL → Deferred — researcher authors per Session A advice Q7
- **Path 4** · `word_registry.dimensions` — NULL/empty → RD: Dimension Review may not have written registry-level dimension list

### Phase R.D — 12 finding(s)

- **Path 4** · `verse_context_group.id=3508` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3501` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3515` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3516` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3517` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3514` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3502` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3513` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3518` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3482` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3483` — dominant_subject=NULL → RD: requires verse reading to set
- **Path 4** · `verse_context_group.id=3484` — dominant_subject=NULL → RD: requires verse reading to set

### Phase R.H — 1 finding(s)

- **Path 5** · `prose_section (Session A)` — No Session A sections generated for this registry → Path 5 (outstanding): generate_session_a_extract.py not yet built


---

## Next Actions

- **Path 1 (0):** build remediation patch with 0 operations.
- **Path 2 (0):** produce 0 sub-process directive(s). Execution may be blocked by OT-DBR-001 (audit_word.py rewrite) if re-extraction involved.
- **Path 3 (1):** record in outstanding tasks with DEFER_STAGE1 tag; resolved during per-word Stage 1 (v1.6).
- **Path 4 (15):** present as RESEARCHER_DECISION block; await resolution.
- **Path 5 (1):** append to outstanding tasks with capability statement.

---

*End of pilot report*