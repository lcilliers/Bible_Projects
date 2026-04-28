# Schema Impact Review — Active Scripts

**Date:** 2026-04-15
**Scope:** Impact of 2026-04-15 schema changes on 18 active Python files.
**Schema changes:** `wa_quality_flag_types` (+3 cols, +15 rows, 3 deprecated); `wa_session_b_findings` (+9 cols, finding_type normalised to UPPER_SNAKE_CASE); `wa_session_research_flags` (VOLUME_LIMITATION -> PH2_VOLUME_LIMITATION); new `wa_finding_entity_links` table.

---

## Summary

| Impact category | Count | Files |
|---|---|---|
| Breaking | 2 | `scripts/apply_session_patch.py`, `scripts/_apply_phase2_flags_patch.py` |
| Functional | 4 | `engine/migrate.py`, `analytics/word_export.py`, `scripts/build_complete_extract.py`, `scripts/_produce_final_extract.py` |
| Cosmetic | 6 | `engine/audit.py`, `engine/flag_engine.py`, `engine/audit_word.py`, `engine/report.py`, `scripts/_generate_programme_report.py`, `scripts/_realign_quality_flags.py` |
| None | 6 | `analytics/db_client.py`, `scripts/extract_term_data.py`, `scripts/inspect_db_only_terms.py`, `scripts/query_h2734.py`, `scripts/word_full_extract.py`, `scripts/build_dimension_extract.py` |

**Top 3 urgent:**
1. `scripts/apply_session_patch.py` — SESSIONB findings INSERT omits 9 new columns (incl. `pass_ref`, `study_segment`, `delete_flag`) and hard-codes legacy fallback `flag_code = 'SB_FINDING'` (deprecated id 145) and defaults `finding_type` to `"DIMENSION_REVIEW"`. Also inserts into the retained `anchor_verses` column — verify column still exists post-M17.
2. `scripts/_apply_phase2_flags_patch.py` — Inserts new flag codes into `wa_quality_flag_types` but no longer supplies `category`, and may collide with the 15 new rows (319-333) just added (duplicate flag_code insertion will raise or silently skip).
3. `engine/migrate.py` — Schema bootstrap code does not know about the new columns (`deprecated`, `deprecation_note`, `category` on `wa_quality_flag_types`; 9 new cols on `wa_session_b_findings`; new `wa_finding_entity_links` table). A fresh DB built from migrations will diverge from the live schema — requires a new migration (M19) committing the 2026-04-15 changes.

**Archive candidates:**
- `scripts/_apply_phase2_flags_patch.py` — One-off patch applicator that pre-inserted the old `SB_FINDING`/`SB_DIMENSION`/`SB_INNER_BEING` phase-2 rows now deprecated. Appears superseded by the 2026-04-15 flag remediation. Recommend moving to `archive/scripts/`.
- `scripts/query_h2734.py` — Diagnostic throwaway keyed to a single Strong's number; not part of any pipeline.

---

## Per-file table

| File | Tables touched | R/W | Impact | Concern | Action |
|---|---|---|---|---|---|
| `scripts/apply_session_patch.py` | `wa_session_b_findings`, `wa_session_research_flags` | Write | Breaking | SESSIONB `INSERT` column list is fixed at 8 cols — new `pass_ref`/`study_segment`/`delete_flag`/`obsolete_*`/`superseded_by_id`/`related_finding_id`/`resolution_note`/`thin_evidence` cannot be populated from incoming patches; research-flag insert hard-codes fallback `flag_code='SB_FINDING'` (deprecated) and never writes to new `wa_finding_entity_links`. | Extend INSERT to include new columns; replace fallback with `PH2_*` codes; add dispatch for entity-link inserts. |
| `scripts/_apply_phase2_flags_patch.py` | `wa_quality_flag_types`, `wa_data_quality_flags` | Write | Breaking | Inserts rows into `wa_quality_flag_types` without populating new `category` column and may clash with the 15 newly-added ids (319-333). Script was bound to the legacy TERM_ANALYSIS Phase-2 group which is now superseded. | Archive — this is a one-off historical patch applicator; confirm with researcher then move to `archive/scripts/`. |
| `engine/migrate.py` | `wa_quality_flag_types`, `wa_session_research_flags` (M13 DDL) | Write (DDL) | Functional | Migration ledger does not record the 2026-04-15 changes; fresh-DB rebuild would lack `deprecated`, `deprecation_note`, `category`, the 15 new flag codes, the 9 new findings columns, the VOLUME_LIMITATION rename, and `wa_finding_entity_links`. | Author a new migration (e.g. M19) capturing all six directives so schema is reproducible. |
| `analytics/word_export.py` | `wa_session_research_flags`, `wa_session_b_findings`, Phase 2 flags | Read | Functional | Export omits the new findings columns (`pass_ref`, `study_segment`, `delete_flag`, etc.) and new `wa_finding_entity_links`; downstream Claude AI payloads will not see these fields. Still uses `SELECT *` on findings so schema additions surface, but calling code does not project them; VOLUME_LIMITATION label still appears as historical string. | Add explicit projection and include entity links; verify downstream consumers handle renamed flag_code. |
| `scripts/build_complete_extract.py` | `wa_session_b_findings`, `wa_session_research_flags`, quality flags | Read | Functional | `SELECT * FROM wa_session_b_findings` will surface new fields with no downstream handling; filter `flag_code == 'SD_POINTER'` unaffected, but VOLUME_LIMITATION consumers (if any) are now stale; no join to `wa_finding_entity_links`. | Decide whether new finding columns should be emitted; add entity-link join to expose cross-term links. |
| `scripts/_produce_final_extract.py` | `wa_session_b_findings` | Read | Functional | Query hard-codes `SELECT finding_id, finding_type, finding, anchor_verses` — does not read the 9 new columns; downstream Session D pointer file therefore loses pass/segment/supersession context. Relies on `anchor_verses` column which is deprecated per RMG v5.8. | Extend select list; plan removal of `anchor_verses` once verified. |
| `engine/audit.py` | `wa_quality_flag_types` | Read | Cosmetic | WR-checks filter on fixed flag_code literals (`NO_VERSES`, `NO_WORD_ANALYSIS`, `SPAN_RESOLUTION_CONFLICT`, `PROSE_ONLY_MEANING`). Deprecated ids 145-147 are not in this list so behaviour is unchanged; new PH2_* codes are not referenced. | No action — confirm that no new quality-group codes should also trigger REVIEW states. |
| `engine/flag_engine.py` | `wa_quality_flag_types` | Write | Cosmetic | `INSERT OR IGNORE` into `wa_quality_flag_types` only writes `(flag_group, flag_code, description)` — new `category` column stays NULL. Acceptable because column is nullable, but inconsistent with remediated rows. | Add `category` arg to `_ensure_flag_type` (low priority). |
| `engine/audit_word.py` | `wa_quality_flag_types`, `wa_session_research_flags` (mention) | Read | Cosmetic | References only the reference table for id lookup; no dependency on new columns or deprecated rows. Header comment states `wa_session_research_flags` is "NOT touched by any step" which remains true. | None. |
| `engine/report.py` | `wa_quality_flag_types` | Read | Cosmetic | Joins for flag listings; surfaces all codes including now-deprecated ones without distinguishing. | Optional filter on `deprecated=0` in display. |
| `scripts/_generate_programme_report.py` | `wa_quality_flag_types` | Read | Cosmetic | Group-by flag_code report will still include deprecated codes 145-147 in counts. | Optional filter on `deprecated=0`. |
| `scripts/_realign_quality_flags.py` | `wa_quality_flag_types`, `wa_data_quality_flags` | Write | Cosmetic | Realigns DATA_COVERAGE flags only (`SPAN_FILTER_APPLIED`); untouched by today's remediation of TERM_ANALYSIS-side codes. | None. |
| `analytics/db_client.py` | `wa_quality_flag_types` (whitelist) | — | None | Table is merely present in export/import whitelist. | None. |
| `scripts/extract_term_data.py` | `wa_quality_flag_types` (via JOIN) | Read | None | Reads flag_group/flag_code only; new columns ignored harmlessly. | None. |
| `scripts/inspect_db_only_terms.py` | `wa_quality_flag_types` | Read | None | Diagnostic query on flag_group/flag_code. | None. |
| `scripts/query_h2734.py` | `wa_quality_flag_types` | Read | None | One-off Strong's diagnostic. | Archive candidate. |
| `scripts/word_full_extract.py` | `wa_quality_flag_types` | Read | None | Denormalised CSV export pulls flag_code only. | None. |
| `scripts/build_dimension_extract.py` | None of the affected tables directly | — | None | Earlier grep hits were false positives (unrelated token matches). | None. |

---

## Notes on specific risks

- **VOLUME_LIMITATION rename:** No active Python script filters on this literal (`Grep` of `VOLUME_LIMITATION` inside the target file list returned zero code matches); rename is safe for scripts but will affect any export JSON produced before 2026-04-15.
- **finding_type normalisation:** `apply_session_patch.py` defaults to uppercase `"DIMENSION_REVIEW"` already, so future inserts stay canonical. Readers (`word_export.py`, `build_complete_extract.py`, `_produce_final_extract.py`) pass the value through verbatim — newly normalised values flow through without code change, but any hard-coded comparisons to `C22`, `theological_note`, `verse_pattern`, `term_behaviour`, `etymology` elsewhere are absent from the reviewed files.
- **`wa_finding_entity_links`:** No active script reads or writes this new table. Patch applicator must grow a new operation handler, and exports (`word_export.py`, `build_complete_extract.py`, `_produce_final_extract.py`) should join it for downstream visibility.
- **Deprecated quality flag rows (145-147):** No active code filters them out. Reports using these rows will show zero-count or stale labels until explicit filters are added.
- **`anchor_verses` column on findings:** `_produce_final_extract.py` and `apply_session_patch.py` still read/write this column. Confirm whether the 2026-04-15 directives retained or removed it — if retained, no action; if removed, both scripts break.
