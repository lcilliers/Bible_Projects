# v5 Impact Assessment — Engine, Scripts, and Documentation

> Generated 2026-03-27 by Claude Code after full codebase review against v5 document suite.

---

## 1. Schema and Constants

| Component | Current State | v5 Requirement | Action |
|-----------|--------------|----------------|--------|
| constants.py:8 — EXPECTED_SCHEMA_VERSION | `"3.6.0"` | Must bump after Tasks 1-8 | Bump to `"3.7.0"` after migrations |
| create_tables.sql — header | States v3.1.0 (outdated — actual is 3.6.0 via migrations) | Should reflect current state | Update DDL to match post-migration state |

---

## 2. Migrations (migrate.py)

**Current highest:** M15 (line 364)

**New migrations required for v5 Tasks:**

| Migration | v5 Task | DDL |
|-----------|---------|-----|
| M16 | Task 1 | `ALTER TABLE word_registry ADD COLUMN cluster_assignment TEXT DEFAULT 'unassigned'` |
| M16 | Task 8.2 | `ALTER TABLE wa_term_inventory ADD COLUMN evidential_status TEXT DEFAULT NULL` |
| M16 | Task 8.2 | `ALTER TABLE wa_term_inventory ADD COLUMN retention_note TEXT DEFAULT NULL` |
| M16 | Task 8.3 | `ALTER TABLE word_registry ADD COLUMN sb_classification TEXT DEFAULT NULL` |
| M16 | Task 8.3 | `ALTER TABLE word_registry ADD COLUMN sb_classification_reasoning TEXT DEFAULT NULL` |
| M16 | Task 8.3 | `ALTER TABLE word_registry ADD COLUMN carry_forward INTEGER DEFAULT 1` |
| M17 | Task 3 | `CREATE TABLE session_d_verse_links (...)` |
| M17 | Task 3 | `CREATE TABLE session_d_term_links (...)` |
| M17 | Task 3 | `CREATE TABLE session_d_observations (...)` |
| M17 | Task 3 | `CREATE TABLE session_d_runs (...)` |
| M18 | Task 8.4 | `CREATE TABLE wa_session_b_dimensions (...)` |
| M18 | Task 8.5 | `CREATE TABLE wa_session_b_findings (...)` |

**Pattern:** Uses `_add_column_if_missing()` helper and `@_register(ref, description)` decorator. All migrations are idempotent.

---

## 3. Patch Applicator (scripts/apply_session_patch.py)

**Currently supports:** update_mti_status, update_registry, bulk_update_note, bulk_update_mti_status

**v5 requires adding:**

| New Operation | Purpose | v5 Source |
|--------------|---------|-----------|
| insert on wa_session_research_flags | Already partially supported — verify SB_FINDING, SB_DIMENSION, SD_POINTER flag_codes accepted | Task 2 |
| bulk_confirm_candidate_delete | Confirm candidate_delete terms as delete | DataPrep 7.4.3 |
| reassign_verses | Move verse records between term inventories | DataPrep 7.5.1 |
| restore_delete_flagged | Restore incorrectly flagged terms | DataPrep 7.5.2 |
| add_cross_registry_links | Insert cross-registry link records | DataPrep 7.5.3 |
| insert on wa_session_b_dimensions | Dimensional profile records | Task 8.4 |
| insert on wa_session_b_findings | Key findings records | Task 8.5 |
| SESSIONB patch type recognition | Analysis completion patches | Task 6 |
| SESSIOND patch type recognition | Session D discovery patches | Task 6 |
| CLUSTERING patch type recognition | Cluster assignment patches | Task 6 |

---

## 4. Audit Checks (engine/audit.py)

**Current:** WR-01 through WR-20

**Potential new checks for v5:**

| Check | Purpose | Priority |
|-------|---------|----------|
| WR-21 | Evidential status populated for all active terms (after Session B) | Medium |
| WR-22 | Retention note present for non-confirmed evidential terms | Medium |
| WR-23 | sb_classification populated after Session B complete | Low |
| WR-24 | Session D tables integrity (post-Session D) | Future |

**WR-16 may need expansion** if new SB_* flags are treated as derivable (currently only DATA_COVERAGE group).

---

## 5. Flag Engine (engine/flag_engine.py)

**Current derivable flags (line 98-102):** HIGH_FREQUENCY_ANCHOR, THIN_DATA, SMALL_VERSE_SAMPLE, NO_WORD_ANALYSIS, NO_VERSES, SPAN_RESOLUTION_CONFLICT, PROSE_ONLY_MEANING

**v5 impact:** The new SB_FINDING, SB_DIMENSION, SB_INNER_BEING, SD_POINTER, SD_CLUSTER flags are **researcher/Claude AI judgement flags**, not engine-derivable. No change needed to flag_engine.py — these flags are inserted via patches, not computed.

---

## 6. Report (engine/report.py)

**Currently reports:** registry fields, file index, terms, quality flags, audit state, verse summary.

**Missing for v5:** cluster_assignment, sb_classification, evidential_status, carry_forward, Session B dimensions, Session B findings.

**Priority:** Medium — update after schema changes are in place.

---

## 7. Word Export (analytics/word_export.py)

**Current export structure:** registry meta, files, run_history, cross_registry_links, patch_history, session_research_flags, statistics, terms (with nested meaning_parsed, quality_flags, phase2_flags, verses, mti).

**Missing for v5 export:**
- `evidential_status` and `retention_note` on each term
- `sb_classification`, `sb_classification_reasoning`, `carry_forward` on registry
- `cluster_assignment` on registry
- `wa_session_b_dimensions` as new section
- `wa_session_b_findings` as new section

**Priority:** Medium — update after schema changes. The export is what Claude AI reads for analysis.

---

## 8. Documentation Impact

| Document | Current State | Required Update |
|----------|--------------|-----------------|
| CLAUDE.md | References schema v3.6.0, engine modes, table groups | Add v5 document architecture, new tables, new fields, updated task dependency |
| docs/interaction-preferences.md | References "GitHub Copilot (Claude Sonnet)" | Update to Claude Code |
| data/schema/create_tables.sql | States v3.1.0, missing all M04-M15 additions | Full refresh or note that migrations are authoritative |

---

## 9. Archive Candidates

| File/Location | Reason |
|---------------|--------|
| Frameword_B/Session_B/archive/ (existing) | Already contains v4.x docs — correct location |
| docs/interaction-preferences.md | Title references Copilot — update content |
| Framework_A/ | Empty directory — no action needed |

---

## 10. Recommended Execution Sequence

**Phase 1 — Documentation (now):**
1. Create WA-SessionB-ClaudeCode-Instructions.md (DONE)
2. Update docs/interaction-preferences.md
3. Update CLAUDE.md for v5 architecture
4. Archive outdated materials

**Phase 2 — Schema (on researcher approval):**
1. Create migrations M16-M18 (Tasks 1, 3, 8)
2. Bump EXPECTED_SCHEMA_VERSION
3. Apply migrations with --dry-run first

**Phase 3 — Engine updates (after schema):**
1. Update apply_session_patch.py for new operations and patch types
2. Update word_export.py for new fields
3. Update report.py for new fields
4. Optionally add new audit checks

**Phase 4 — Programme operations (after engine):**
1. Task 4 — Registry clustering export
2. Task 5 — Zero-term investigation
3. Task 6 — PATCH_SPEC update
