# CC Directives — Flag Table Remediation
## wa-global-flag-remediation-directives-v1-20260415.md
**Date:** 2026-04-15
**Produced by:** Claude AI — flag remediation design session
**Requires researcher approval before any directive is applied**
**Governed by:** wa-global-general-rules-v2.2-20260415.json (GR-DIR-001 through GR-DIR-005, GR-PROC-003, GR-PROC-004)
**Previous document:** wa-global-flagtable-remediation-plan-v1.0-20260414.md

---

## Context

These directives implement the decisions made during the flag remediation design session (2026-04-15). They are all directives rather than patches because they involve reference table governance and schema changes where Claude AI does not have certainty about the exact field names, constraint state, or current values in the database. Claude Code must inspect, confirm, and execute. Each directive states the outcome required and the completion confirmation that must be returned.

Directives are sequenced. DIR-20260415-001 must be confirmed complete before DIR-20260415-002 begins, and so on.

---

## DIR-20260415-001 — Deprecate obsolete Session B outcome codes

**Motivation:** Three flag codes in `wa_quality_flag_types` — `SB_FINDING` (id 145), `SB_DIMENSION` (id 146), and `SB_INNER_BEING` (id 147) — were designed as placeholders before the dedicated Session B output tables existed. The correct destinations for Session B analytical outputs are now: `wa_session_b_findings` (key findings), `wa_session_b_dimensions` (dimensional profile), and `word_registry.sb_classification` + related fields (inner being standing). These three codes have never been used (zero rows in `wa_data_quality_flags` carry them). They must be deprecated to prevent future use and to remove ambiguity.

**Scope:** `wa_quality_flag_types` — rows with id 145, 146, 147.

**Outcome required:**
- Each of the three rows must carry a deprecation marker. If the table has a boolean or status field suitable for this (e.g. `deprecated`, `active`, `obsolete`), use it and set it to the deprecated/inactive value. If no such field exists, add a `deprecated` INTEGER field (default 0) and set it to 1 for these three rows.
- Each deprecated row must carry a `deprecation_note` text field (add if absent) recording: "Superseded — Session B analytical outputs route to wa_session_b_findings, wa_session_b_dimensions, and word_registry.sb_classification. Deprecated 2026-04-15."
- No rows in `wa_data_quality_flags` reference these three flag_ids. This must be confirmed before any change is made.

**Completion confirmation — CC must return:**
1. Confirm: zero rows in `wa_data_quality_flags` where `flag_id IN (145, 146, 147)`
2. Return the updated rows for ids 145, 146, 147 from `wa_quality_flag_types` showing the deprecated status and deprecation note
3. Confirm the current schema of `wa_quality_flag_types` (all column names and types) — this is needed for DIR-20260415-002

---

## DIR-20260415-002 — Add missing reference rows to wa_quality_flag_types

**Motivation:** `wa_session_research_flags` uses `flag_code` as a string field with no FK constraint to `wa_quality_flag_types`. As a result, 15 of the 16 flag codes currently in active use in `wa_session_research_flags` have no reference row in `wa_quality_flag_types`. This means the reference table is not a reliable governance source. All active codes must have reference rows with descriptions and category assignments.

**Depends on:** DIR-20260415-001 confirmation (need current schema before inserting rows).

**Scope:** `wa_quality_flag_types` — insert missing rows for the 15 codes listed below.

**Category field:** If `wa_quality_flag_types` does not have a `category` field, add one (TEXT, nullable) before inserting rows. The four categories are: `SESSION_D_POINTER`, `DATA_QUALITY`, `STUDY_REQUIRED`, `RESEARCHER_DECISION`.

**Rows to insert** (flag_code, category, description):

| flag_code | category | description |
|-----------|----------|-------------|
| PH2_VOLUME_LIMITATION | DATA_QUALITY | Term has low verse coverage relative to total occurrences — synthesis-level conclusions are provisional. Standard threshold: verse count < 20% of occurrence count. |
| PH2_DATA_ERROR | DATA_QUALITY | Data quality error identified during Session B pre-analysis — includes homonyms with shared counts, function word contamination, extraction anomalies. Requires correction before analysis proceeds. |
| PH2_CROSS_REGISTRY_REQUIRED | DATA_QUALITY | Cross-registry analysis is required before synthesis conclusions can be drawn for this term. Cannot be resolved within the source registry alone. |
| PH2_CROSS_REF_ENRICHMENT | SESSION_D_POINTER | Cross-reference enrichment opportunity identified — a formal connection between registries via this term merits Session D investigation. |
| PH2_THEOLOGICAL_DEPTH_REQUIRED | STUDY_REQUIRED | The verse or passage requires dedicated theological study before its contribution to the inner-being picture can be assessed. |
| PH2_DATA_QUALITY | DATA_QUALITY | General data quality concern — includes root bleed, missing verses, and anomalous groupings not covered by more specific codes. |
| PH2_EXEGETICAL_STUDY_REQUIRED | STUDY_REQUIRED | Dedicated exegetical study of the named passage is required — the verse raises an interpretive question that cannot be resolved from the extract alone. |
| PH2_ESCHATOLOGICAL_STUDY_REQUIRED | STUDY_REQUIRED | The term's eschatological or afterlife usage requires dedicated study — the passage is in an eschatological or Sheol context requiring specialist attention. |
| PH2_DATA_SPLIT_REQUIRED | DATA_QUALITY | The term has multiple distinct senses that are currently conflated in a single entry. A data split into separate entries is required before analysis can proceed cleanly. |
| PH2_BOUNDARY_QUESTION | RESEARCHER_DECISION | A scope or boundary question about this term's registry assignment or analytical treatment requires researcher input to resolve. |
| DIMREVIEW_SESSION_D | SESSION_D_POINTER | Observation raised during Dimension Review that requires Session D investigation — a dimensional pattern, cross-registry connection, or structural question identified during cluster-level review. |
| THEMATIC_LINK | SESSION_D_POINTER | Thematic connection between registries identified during Session B analysis. Distinct from SD_POINTER in that it describes a thematic relationship rather than a structural term-level bridge. |
| DATA_INTEGRITY | DATA_QUALITY | Data integrity concern that does not fit a more specific code — includes FK inconsistencies, orphaned records, and cross-table contradictions. |
| CANDIDATE_REGISTRY_WORD | RESEARCHER_DECISION | A word or concept has been identified as a candidate for a new registry entry. Requires researcher decision on whether to add to programme scope. |
| RESEARCHER_DECISION | RESEARCHER_DECISION | An item requiring researcher input to resolve — Claude AI has exhausted its analytical resources and cannot proceed without a decision. Must follow the format specified in GR-RD-002. |

**Note on VOLUME_LIMITATION (19 rows, no PH2_ prefix):** This is the same concept as PH2_VOLUME_LIMITATION. Do NOT insert a separate reference row for VOLUME_LIMITATION. The data cleanup for these 19 rows is handled in DIR-20260415-003.

**Completion confirmation — CC must return:**
1. Count of rows now in `wa_quality_flag_types` (before and after)
2. List of all newly inserted rows confirming flag_code, category, and description are populated
3. Confirm the `category` field exists on the table and is populated for all 15 new rows

---

## DIR-20260415-003 — Consolidate VOLUME_LIMITATION naming drift

**Motivation:** `wa_session_research_flags` contains 19 rows with `flag_code = 'VOLUME_LIMITATION'` and 33 rows with `flag_code = 'PH2_VOLUME_LIMITATION'`. These describe the same concept. The canonical code is `PH2_VOLUME_LIMITATION` (which now has a reference row from DIR-20260415-002). The 19 non-prefixed rows are naming drift from an earlier instruction version and must be updated to use the canonical code.

**Depends on:** DIR-20260415-002 confirmation (canonical reference row must exist before updating data rows).

**Scope:** `wa_session_research_flags` — 19 rows where `flag_code = 'VOLUME_LIMITATION'`.

**Outcome required:**
- All 19 rows updated: `flag_code` set to `'PH2_VOLUME_LIMITATION'`
- No rows remain in `wa_session_research_flags` with `flag_code = 'VOLUME_LIMITATION'`
- Existing `flag_label`, `description`, `registry_id`, `priority`, `session_target`, `resolved`, and all other fields on these rows are unchanged

**Completion confirmation — CC must return:**
1. Count of rows updated
2. Confirm: zero rows in `wa_session_research_flags` where `flag_code = 'VOLUME_LIMITATION'`
3. Confirm: count of rows where `flag_code = 'PH2_VOLUME_LIMITATION'` is now 52 (33 + 19)

---

## DIR-20260415-004 — Add missing fields to wa_session_b_findings

**Motivation:** The obs schema document (wa-global-obs-schema-v2_2-20260414.md, Gap G-4) specifies nine fields required on `wa_session_b_findings` that do not currently exist. These fields are necessary for: the finding lifecycle (confirm, correct, deepen, set aside, supersede), Session C prose validation, thin evidence management, and the resolution of prior-phase findings during Session B. Session B v5.0 cannot be drafted to full precision without these fields in place.

**Scope:** `wa_session_b_findings` — add nine new fields.

**Fields to add** (field name, type, default, purpose):

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| pass_ref | TEXT | NULL | Phase and pass attribution — e.g. 'Session B Pass 3', 'Dimension Review Phase C C17', 'Session C' |
| study_segment | TEXT | NULL | Rendering target — controlled vocabulary from obs schema Section 14 |
| delete_flag | INTEGER | 0 | 0 = active; 1 = set aside or superseded |
| obsolete_reason | TEXT | NULL | Required when delete_flag = 1 — must record outcome of investigation |
| obsolete_date | TEXT | NULL | Date marked obsolete |
| superseded_by_id | INTEGER | NULL | Self-referential FK to this table's id — points to the finding that replaces this one |
| related_finding_id | INTEGER | NULL | Link to: the pointer this finding resolves; the prior finding this supersedes; or a related finding this builds on |
| resolution_note | TEXT | NULL | For confirmed or deepened findings — brief note of the Session B review outcome |
| thin_evidence | INTEGER | 0 | 1 = this finding is supported by thin evidence; must be resolved before session close |

**Outcome required:**
- All nine fields added to `wa_session_b_findings`
- All existing 171 rows have: `delete_flag = 0`, `thin_evidence = 0`, all new text fields = NULL
- No existing data is altered

**Completion confirmation — CC must return:**
1. Full schema of `wa_session_b_findings` after migration (all column names and types)
2. Count of rows where `delete_flag = 0` (must be 171)
3. Count of rows where `thin_evidence = 0` (must be 171)

---

## DIR-20260415-005 — Create wa_finding_entity_links table

**Motivation:** The obs schema document (Gap G-5) specifies a new junction table `wa_finding_entity_links` that links analytical findings to the specific entities they describe — terms, verses, groups, dimensions, root families, and cross-registry connections. Without this table, findings cannot be queried by entity, and Session D cannot efficiently retrieve all findings about a specific term, verse, or cross-registry relationship.

**Scope:** New table creation.

**Table definition:**

```
wa_finding_entity_links
  id              INTEGER PRIMARY KEY
  finding_id      INTEGER NOT NULL     — FK to wa_session_b_findings.id
  entity_type     TEXT NOT NULL        — controlled: term / verse / group / dimension / registry / root_family / cross_registry
  entity_id       INTEGER              — id of the entity in its table; polymorphic, FK integrity enforced by CC at write time
  entity_strongs  TEXT                 — denormalised Strong's number for term links (nullable)
  raised_date     TEXT NOT NULL        — date this link was created
```

**Indexes required:**
- Index on `finding_id`
- Composite index on `(entity_type, entity_id)`

**Outcome required:**
- Table created with all six fields
- Both indexes created
- Zero rows (table starts empty — entity links are populated as Session B progresses)

**Completion confirmation — CC must return:**
1. Schema of `wa_finding_entity_links` (all column names and types)
2. Confirm both indexes exist — names and fields covered
3. Row count (must be 0)

---

## DIR-20260415-006 — Normalise finding_type to UPPER_SNAKE_CASE in wa_session_b_findings

**Motivation:** The obs schema (Gap G-6) identifies that `finding_type` values in `wa_session_b_findings` use two inconsistent naming conventions: `UPPER_SNAKE_CASE` (from Dimension Review work) and `lower_snake_case` (from Session B extraction work). One value — 'C22' — uses a cluster code as a finding type, which does not conform to either convention. All values must be normalised to UPPER_SNAKE_CASE before Session B v5.0 work begins.

**Depends on:** DIR-20260415-004 (fields added — though this operation does not use the new fields, the table should be in its final state before data normalisation).

**Scope:** `wa_session_b_findings` — update `finding_type` values on existing 171 rows.

**Normalisation mapping:**

| Current value | Normalised value |
|---------------|-----------------|
| theological_note | THEOLOGICAL_NOTE |
| verse_pattern | VERSE_PATTERN |
| term_behaviour | TERM_BEHAVIOUR |
| etymology | ETYMOLOGY |
| C22 | DIMENSION_REVIEW |

**Note on C22:** The four rows with `finding_type = 'C22'` are Cluster C22 Dimension Review findings. Mapping them to `DIMENSION_REVIEW` is analytically correct. If CC finds any reason to question this mapping (e.g. the content is materially different from other DIMENSION_REVIEW rows), CC must flag this before executing and not proceed until confirmed.

**Outcome required:**
- Zero rows with `finding_type` values in `lower_snake_case`
- Zero rows with `finding_type = 'C22'`
- All existing rows use a value from the controlled vocabulary: MEANING_OBSERVATION, VERSE_PATTERN, VERSE_ANNOTATION, THEOLOGICAL_NOTE, SOMATIC_EVIDENCE, SPIRIT_SOUL_BODY, ETYMOLOGY, ROOT_FINDING, DIMENSION_REVIEW, GROUP_INTEGRITY, CROSS_REGISTRY, TERM_BEHAVIOUR, SESSION_C_CORRECTION, OPEN_ITEM
- Row count unchanged (171)

**Completion confirmation — CC must return:**
1. Distinct `finding_type` values after normalisation with row counts per value
2. Confirm total row count is still 171
3. If C22 mapping was flagged — report separately before executing that subset

---

## Directive sequence summary

| Directive | Action | Depends on |
|-----------|--------|------------|
| DIR-20260415-001 | Deprecate SB_FINDING, SB_DIMENSION, SB_INNER_BEING codes | None |
| DIR-20260415-002 | Add 15 missing reference rows to wa_quality_flag_types | DIR-001 confirmed |
| DIR-20260415-003 | Consolidate VOLUME_LIMITATION → PH2_VOLUME_LIMITATION (19 rows) | DIR-002 confirmed |
| DIR-20260415-004 | Add 9 missing fields to wa_session_b_findings | None (can run parallel to DIR-001/002/003) |
| DIR-20260415-005 | Create wa_finding_entity_links table | DIR-004 confirmed |
| DIR-20260415-006 | Normalise finding_type to UPPER_SNAKE_CASE | DIR-004 confirmed |

DIR-001 through DIR-003 are reference table governance and may run sequentially as one CC session.
DIR-004 through DIR-006 are schema migration and data normalisation and may run sequentially as a second CC session.
Both tracks can begin simultaneously if CC is comfortable running two independent sequences.

---

*All directives require researcher approval before Claude Code begins. Confirmation outputs must be returned to Claude AI and the researcher for review before the next directive in sequence begins.*
