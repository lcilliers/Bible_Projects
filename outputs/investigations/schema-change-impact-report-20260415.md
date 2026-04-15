# Schema Change Impact Report — 2026-04-15 Flag Remediation

> Consolidated report of all downstream impacts from the six flag remediation directives applied 2026-04-15.
> Companion documents:
> - `Logs/wa-session-log-20260415-flag-remediation.md` — execution log with backup references
> - `outputs/investigations/schema-impact-review-scripts-20260415.md` — detailed per-script review
> - `archive/patches/wa-global-flag-remediation-directives-v1-20260415.md` — the directive set itself

---

## 1. What Changed

Four tables were modified, one new table created:

| Table | Change |
|-------|--------|
| `wa_quality_flag_types` | +3 fields (deprecated, deprecation_note, category); +15 rows; 3 rows deprecated |
| `wa_session_b_findings` | +9 lifecycle fields; 24 rows normalised to UPPER_SNAKE_CASE |
| `wa_session_research_flags` | 19 VOLUME_LIMITATION → PH2_VOLUME_LIMITATION |
| `wa_finding_entity_links` | **NEW** — 6 fields, 2 indexes, FK to findings |

Six pre-write backups in `backups/` (one per directive).

---

## 2. Documentation Updated

| File | Change |
|------|--------|
| `data/schema/create_tables.sql` | `wa_quality_flag_types` + `wa_session_b_findings` definitions updated; `wa_finding_entity_links` CREATE added; section index updated |
| `docs/database-table-analysis.md` | Header notes schema changes; 3 table sections updated; new section added for `wa_finding_entity_links`; summary tables updated |
| `CLAUDE.md` | Group 6 and Group 13 rows updated with 2026-04-15 change notes |
| `docs/assessment-wa-term-phase2-flags.md` | Post-remediation note added (table not modified; core problem unresolved) |
| `docs/assessment-wa-cross-registry-links.md` | Post-remediation note added (table not modified) |
| `docs/assessment-wa-session-b-findings.md` | Post-remediation note added (naming issue resolved; 9 new fields) |
| `docs/assessment-wa-session-research-flags.md` | Post-remediation note added (naming drift resolved; reference coverage complete) |
| `Logs/wa-session-log-20260415-flag-remediation.md` | New session log produced |

---

## 3. Script Impact Summary

From the detailed review in `schema-impact-review-scripts-20260415.md`:

| Impact | Count | Files |
|--------|------:|-------|
| **Breaking** | 2 | `apply_session_patch.py`, `_apply_phase2_flags_patch.py` |
| **Functional** | 4 | `engine/migrate.py`, `word_export.py`, `build_complete_extract.py`, `_produce_final_extract.py` |
| **Cosmetic** | 6 | `engine/audit.py`, `flag_engine.py`, `audit_word.py`, `report.py`, `_generate_programme_report.py`, `_realign_quality_flags.py` |
| **None** | 6 | `db_client.py`, `extract_term_data.py`, `inspect_db_only_terms.py`, `query_h2734.py`, `word_full_extract.py`, `build_dimension_extract.py` |

### 3.1 Breaking (must fix before next write)

**`scripts/apply_session_patch.py`** — The patch applicator.
- SESSIONB findings `INSERT` hard-codes the legacy 8-column list. Incoming patches cannot populate the 9 new lifecycle fields (pass_ref, study_segment, delete_flag, obsolete_*, superseded_by_id, related_finding_id, resolution_note, thin_evidence).
- Research flag insert has a fallback that hard-codes `flag_code='SB_FINDING'` — now a deprecated code.
- No dispatch for `wa_finding_entity_links` inserts.
- **Action:** Extend the INSERT column list; replace deprecated fallback with appropriate PH2_* code; add entity-link operation handler.

**`scripts/_apply_phase2_flags_patch.py`** — One-off patch applicator.
- Pre-inserted the SB_FINDING/SB_DIMENSION/SB_INNER_BEING rows that are now deprecated.
- Collides with the 15 new rows (ids 319–333) — duplicate flag_code inserts will fail.
- **Action:** Archive to `archive/scripts/` — superseded by the remediation.

### 3.2 Functional (should update but not blocking)

**`engine/migrate.py`** — Schema migration ledger.
- No migration record for the 2026-04-15 changes.
- Fresh-DB rebuild from migrations would lack `deprecated`, `deprecation_note`, `category`, the 15 new flag codes, the 9 new findings fields, the VOLUME_LIMITATION rename, and `wa_finding_entity_links`.
- **Action:** Author migration M19 (or equivalent) to capture the directive set. Consider bumping schema version 3.8.0 → 3.9.0.

**`analytics/word_export.py`, `scripts/build_complete_extract.py`, `scripts/_produce_final_extract.py`**
- Read findings without projecting the 9 new columns.
- None join `wa_finding_entity_links`.
- Downstream Claude AI payloads will not see finding lifecycle state.
- **Action:** Add explicit column projection; add entity-link join where relevant.

### 3.3 Cosmetic (optional)

Mostly reports that will include deprecated flag codes in counts until a `deprecated=0` filter is added. Not blocking.

### 3.4 Archive candidates

- `scripts/_apply_phase2_flags_patch.py` — superseded by today's remediation
- `scripts/query_h2734.py` — one-off diagnostic

---

## 4. Outstanding Issues Raised by the Review

### 4.1 `anchor_verses` column question

Both `apply_session_patch.py` and `_produce_final_extract.py` still reference `wa_session_b_findings.anchor_verses`. Confirmed: **the column was retained** by the 2026-04-15 directives — no action needed. (Directive DIR-20260415-004 only ADDED fields; it did not remove any.)

### 4.2 FK constraint for wa_session_research_flags.flag_code

The directive set added 15 reference rows so every in-use code has a match. But the relationship is still a loose string match — no FK constraint was added. New flag codes can still be inserted without a matching reference entry. The researcher may want to consider:
- Option A: Add an FK constraint (requires switch from `flag_code TEXT` to `flag_id INTEGER`)
- Option B: Add application-layer validation in the patch applicator
- Option C: Accept the looseness and rely on periodic audits

### 4.3 `category` field on pre-existing rows

11 pre-existing active rows in `wa_quality_flag_types` have `category = NULL`. These are the DATA_COVERAGE-group engine-derived flags (NO_VERSES, THIN_DATA, etc.) and the SD_POINTER/SD_CLUSTER codes. A follow-on directive could backfill appropriate category values (e.g. DATA_COVERAGE → `DATA_QUALITY`).

### 4.4 Schema version

Current `schema_version.version_code` is `3.8.0`. The 2026-04-15 changes arguably warrant `3.9.0`. Decision deferred to researcher.

---

## 5. Recommended Next Actions

**Priority 1 (before next Session B run):**
1. Fix `scripts/apply_session_patch.py` to write the 9 new finding columns and use valid flag codes in fallback
2. Archive `scripts/_apply_phase2_flags_patch.py`

**Priority 2 (before schema reproducibility is needed):**
3. Author migration M19 and bump schema version to 3.9.0
4. Add explicit field projection in exports (`word_export.py`, `build_complete_extract.py`, `_produce_final_extract.py`)
5. Add `wa_finding_entity_links` join in exports

**Priority 3 (optional hygiene):**
6. Add `deprecated=0` filter in programme reports
7. Add `category` arg to `flag_engine._ensure_flag_type`
8. Backfill `category` for the 11 pre-existing active rows
9. Decide on FK constraint strategy for flag_code (§4.2)

---

## 6. Files Not Affected

The database changes have no impact on:
- Verse data (`wa_verse_records`, `wa_verse_term_links`, 229k + 227k rows)
- Verse context (`verse_context`, `verse_context_group`)
- Dimension review (`wa_dimension_index`, `wa_dim_review_cluster_log`)
- Term inventory and MTI (`wa_term_inventory`, `mti_terms`, `mti_term_flags`)
- Meaning parse tables
- Engine control tables
- Session D tables (still empty, unchanged)

The remediation was surgical — only the flag table governance was affected.

---

*Report produced 2026-04-15 as follow-up to the six-directive flag remediation session.*
