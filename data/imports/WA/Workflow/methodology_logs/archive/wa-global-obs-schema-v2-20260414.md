# WA Global — Observations Schema

**Filename:** wa-global-obs-schema-v2-20260414.md
**Date:** 2026-04-14
**Version:** 2.0
**Previous output ref:** wa-global-obs-schema-v1-2026-04-13.md
**Status:** Active — supersedes v1.0. Rewrites the approach: maps observation types first, then data needs, then existing coverage, then gaps.

## Change note

v2.0 (2026-04-14): Complete rewrite. v1.0 proposed new tables (`Proj_observations` and entity index tables) without first auditing the existing schema. v2.0 takes the correct approach: identify every type of observation that needs a home, specify what data each type needs, map each against the existing database (schema v3.8.0), and flag only what is genuinely missing. The goal is to make the existing schema work, not to add tables unnecessarily.

---

## 1. Scope of this Document

Four programme phases produce analytical observations, findings, flags, and commentary that need to be captured in the database:

| Phase | Produces |
|-------|---------|
| **Verse Context** | Relevance decisions, group assignments, anchor designations, classification rationale, deferred flags, Session B handoff flags |
| **Dimension Review** | Dimension assignments per group, dimension confidence, group characterisation, cluster-level patterns |
| **Session B** | Term-level meaning findings, verse annotations, somatic evidence, spirit-soul-body classification, cross-registry pointers, data quality flags, connection characterisations |
| **Session C** | Prose articulation, correction flags where word study contradicts data, open items preserved for Session D |

Session D is out of scope for this document — it is governed by the Session D Orientation document.

The question this document answers is: **for every type of observation produced by these phases, when is it needed, what does it record, how must it be recorded, where does it go, what is missing, and what is still unclear?**

---

## 2. Observation Types — Catalogue

The programme produces eight distinct types of analytical output that require database storage. They are different in nature and require different data shapes.

| Type | Produced by | Primary consumer |
|------|------------|-----------------|
| **OT-1 Verse relevance decision** | Verse Context | Session B Stage 1 |
| **OT-2 Group classification** | Verse Context | Session B analysis, Dimension Review |
| **OT-3 Dimension assignment** | Dimension Review | Session B analysis |
| **OT-4 Analytical finding** | Session B passes, Dimension Review | Session C, Session D |
| **OT-5 Verse annotation** | Session B Pass 3 | Session C Section 3 |
| **OT-6 Forward pointer (Session D)** | Session B all passes | Session D |
| **OT-7 Data quality flag** | Session B Stage 1, Verse Context | Claude Code remediation |
| **OT-8 Session C correction flag** | Session B Stage 3, Session C | Word study update |

Each type is examined in turn below: what it captures, what data fields it needs, where the current schema stores it, what is missing.

---

## 3. OT-1 — Verse Relevance Decision

### When is there a need?

During Verse Context classification, every verse in a term's corpus is evaluated for inner-being relevance. The decision — relevant, set-aside, or related — and the reason for it must be recorded. This record is the basis for all subsequent analysis: Session B only analyses verses that passed this filter. The filter reasoning must be auditable.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Registry (word) | Which word this classification belongs to |
| Term (Strong's) | Which term within the word |
| Verse reference | Book, chapter, verse |
| Decision | Anchor / relevant / related / set-aside |
| Set-aside reason | If set-aside: no_inner_being / physical_only / spatial_only / wrong_face / other |
| Classification notes | Only where noteworthy — not required for every row |
| Instruction version | Under which instruction the classification was made |
| Date | When classified |

### Where is it recorded currently?

**`verse_context`** (63,028 rows) — this is the correct home. Fields map as follows:

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Registry | via `mti_term_id` → `wa_term_inventory.registry_id` | Present (join required) |
| Term | `mti_term_id` FK | Present |
| Verse | `verse_record_id` FK | Present |
| Decision | `is_anchor`, `is_relevant`, `is_related` | Present |
| Set-aside reason | `set_aside_reason` | Present — but sparse: only populated from VCB-032 onward; earlier batches have no value |
| Classification notes | `notes` | Present — sparse (10%) by design |
| Instruction version | Not present | **Missing** |
| Date | Not present | **Missing** |

### What is missing?

Two attribution fields are absent from `verse_context`:
- `classified_by_instruction` — instruction version under which this row was created
- `classified_date` — date of classification

These matter for audit: when a classification is revisited, knowing which instruction version applied at the time is essential for deciding whether a change is a correction or an instruction upgrade.

The `set_aside_reason` sparseness (pre-VCB-032 rows all NULL) is a known data state, not a schema gap. No retroactive backfill is planned.

### What is unclear?

The `wrong_face` set-aside value (added in v2.5) is intended to enable future vertical pass discovery — verses that are analytically significant from a different registry's perspective but set aside for this one. The rediscovery mechanism (reading all `wrong_face` records for a target registry before Session B) is described in the Verse Context instruction but has not yet been operationalised. It is unclear whether a formal link from a `wrong_face` record to the target registry is needed in the schema, or whether the notes field is sufficient.

---

## 4. OT-2 — Group Classification

### When is there a need?

Also during Verse Context, relevant verses are grouped by the inner-being characteristic the verse cluster is primarily about. Each group gets a description and a code. This grouping is the semantic structure that Session B reads — the groups are the unit of analysis.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Registry | Which word |
| Term | Which Strong's number |
| Group code | Unique identifier (e.g. 2310-001) |
| Group description | Characteristic-perspective description of what this verse cluster is about |
| Anchor count | How many anchor verses in this group |
| Related count | How many related verses |
| Set-aside count | How many set-aside verses |
| Instruction version | When this group was created or last revised |

### Where is it recorded currently?

**`verse_context_group`** (3,550 rows) — correct home.

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Registry | via `mti_term_id` → registry | Present (join required) |
| Term | `mti_term_id` FK | Present |
| Group code | `group_code` | Present |
| Group description | `context_description` | Present |
| Anchor / related / set-aside counts | Not directly on this table | Computed from `verse_context` counts — no stored counts here |
| Instruction version | Not present | **Missing** |

### What is missing?

- `classified_by_instruction` — instruction version
- Stored verse counts would avoid repeated computation but are not strictly necessary — they can always be derived from `verse_context`

---

## 5. OT-3 — Dimension Assignment

### When is there a need?

Dimension Review assigns each verse context group to an emergent inner-being dimension. The assignment, its confidence level, the dominant subject characterisation, and the reasoning must all be recorded. This is the bridge between raw verse groupings and Session B analytical work.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Group | Which verse context group |
| Dimension | The assigned dimension label |
| Dominant subject | What the group is primarily about (characteristic-perspective) |
| Confidence level | AUTOMATED / CLAUDE_AI / RESEARCHER |
| Manual override | Whether researcher has locked this |
| Assignment reasoning | Why this dimension fits (analytical rationale) |
| Instruction version | Under which Dimension Review instruction this was assigned |
| Date | When assigned |

### Where is it recorded currently?

**`wa_dimension_index`** (3,500 rows) — correct home.

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Group | `verse_context_group_id` FK | Present |
| Dimension | `dimension` | Present (93% populated — 7% still at KEYWORD_WEAK or unreviewed) |
| Dominant subject | `dominant_subject` | Present but sparse (27%) — only populated where Dimension Review completed |
| Confidence level | `dimension_confidence` | Present |
| Manual override | `manual_override` | Present |
| Assignment reasoning | `notes` | Present but sparse (40%) — only where analytical notes exist |
| Instruction version | Not present | **Missing** |
| Date | `last_modified` | Present (auto-updated timestamp) |

### What is missing?

- `dim_review_instruction` — instruction version under which the dimension was assigned. Currently not recorded at row level. The `wa_dim_review_cluster_log` table records instruction version at cluster level, but there is no field at the individual group level. For groups revisited under a later instruction version (e.g. a correction during Session B), the revision is invisible.

---

## 6. OT-4 — Analytical Finding

### When is there a need?

Session B's six passes, and Dimension Review's group-by-group review, produce substantive analytical findings: meaning observations about a term, a pattern visible across a group's verses, a theological dimension that the word study must account for, an etymology insight, a dimension pattern across the registry. These are the primary analytical outputs of the programme — the content that Session C renders into prose, and that Session D draws on for synthesis.

An analytical finding:
- Is grounded in specific verse evidence, term data, or group structure
- Names something that was not visible before the analysis was conducted
- Can be linked to the entity (term, verse, group, dimension, or registry) it describes
- May confirm, correct, or deepen something in the Session C word study
- Is the category (b) entity-linked observation from the GR-OBS-002 model

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Finding text | The substantive analytical content — free prose |
| Finding type | What kind of finding this is (meaning observation, verse pattern, theological note, somatic evidence, etymology, dimension pattern, group integrity) |
| Registry | Which word this finding belongs to |
| Entity links | Which specific entities this finding is about (term, verse, group, dimension) |
| Rendering target | Which section of the word study or brief this finding contributes to |
| Origin pass | Which Session B pass or Dimension Review phase produced this |
| Instruction version | Under which instruction |
| Date | When raised |
| Obsolete flag | Whether this finding has been superseded |
| Obsolete reason | Why it was superseded, if applicable |
| Superseded by | Link to the replacement finding, if applicable |
| Resolution link | If this finding resolves a forward pointer or supersedes an earlier finding, the link |

### Where is it recorded currently?

**`wa_session_b_findings`** (171 rows) — this table is the correct home but is currently populated primarily with Dimension Review outputs only, and lacks several required fields.

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Finding text | `finding` | Present |
| Finding type | `finding_type` | Present — but naming is inconsistent (UPPER_SNAKE vs lower_snake; "C22" raw cluster code used once) |
| Registry | `registry_id` FK | Present |
| Entity links | Not present | **Missing** — no FK to term, verse, group, or dimension |
| Rendering target | Not present | **Missing** — `study_segment` not present |
| Origin pass | Partially in `session_b_instruction` | Partial — instruction version only; pass number absent |
| Instruction version | `session_b_instruction` | Present |
| Date | `raised_date` | Present |
| Obsolete flag | Not present | **Missing** |
| Obsolete reason | Not present | **Missing** |
| Superseded by | Not present | **Missing** |
| Resolution link | Not present | **Missing** |

**Coverage gap:** The table currently holds 83% Dimension Review findings and 17% Session B extraction findings. It does not yet receive Verse Context findings (none written to it), and the write protocol for Session B analytical pass findings is not formalised. The table needs to become the home for all analytical findings across all four phases.

### What is missing?

**Missing fields on `wa_session_b_findings`:**

| Field | Type | Purpose |
|-------|------|---------|
| `pass_ref` | TEXT nullable | Pass-level attribution: e.g. "Session B Pass 3", "Dimension Review Phase C", "Verse Context VCB-031". Complements the existing instruction version field. |
| `study_segment` | TEXT nullable | Rendering-target declaration per GR-OBS-006. Controlled vocabulary in Section 9. Declares which section of the word study or analytical brief this finding contributes to. |
| `delete_flag` | INTEGER default 0 | Obsolescence marker per GR-OBS-005. 0 = active; 1 = obsolete. Named `delete_flag` not `delete` to avoid reserved word conflict. |
| `obsolete_reason` | TEXT nullable | If `delete_flag` = 1: why this finding is obsolete. Required when `delete_flag` is set. |
| `obsolete_date` | TEXT nullable | Date marked obsolete. |
| `superseded_by_id` | INTEGER FK nullable | If obsoleted and a replacement exists: the `id` of the replacement finding in this table. Self-referential FK. |
| `related_finding_id` | INTEGER FK nullable | Multi-purpose link: (i) the `wa_session_research_flags.id` that this finding resolves; (ii) the prior `wa_session_b_findings.id` that this supersedes; (iii) a related finding this builds on. |

**Missing table — entity links:**

The existing `file_id` on `wa_session_b_findings` gives file-level linkage only. There is no FK path from a finding to the specific term, verse, group, or dimension it describes. Without entity links:
- "Show me all findings about group 2310-001" cannot be answered
- "Show me all findings about H2617B across all registries" cannot be answered
- Session C cannot query "all findings with study_segment = word_study_section_4_racham for registry 23"

A new junction table is needed: **`wa_finding_entity_links`**

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER PK | Stable identifier |
| `finding_id` | INTEGER FK | References `wa_session_b_findings.id` |
| `entity_type` | TEXT | Controlled: `term` / `verse` / `group` / `dimension` / `registry` / `root_family` / `research_flag` |
| `entity_id` | INTEGER | The id of the entity in its table. Polymorphic — entity_type determines which table this id belongs to |
| `entity_strongs` | TEXT nullable | Denormalised Strong's number for term links, enabling common queries without a join |
| `raised_date` | TEXT | Date this link was created |

This is a single polymorphic table rather than seven separate tables. The trade-off is that `entity_id` cannot be enforced by a DB-level FK — integrity is maintained by requiring Claude Code to verify entity existence at write time.

### What is unclear?

The `wa_session_b_dimensions` table (2 rows, near-unused) records a registry-level spirit-soul-body dimensional profile. This is an OT-4 finding at registry level. It is unclear whether this table should be: (a) retired and its function absorbed by `wa_session_b_findings` with `finding_type = SPIRIT_SOUL_BODY_CLASSIFICATION`; or (b) retained and populated as the authoritative per-registry classification record. The current instruction writes the spirit-soul-body classification to the analytical brief and to the `sb_classification` field on `word_registry`, not to this table.

---

## 7. OT-5 — Verse Annotation

### When is there a need?

Session B Pass 3 produces a structured annotation for every anchor verse — a 3–6 sentence analytical comment that names what the verse does that a plain summary cannot carry, drawn from specific language, grammar, or context. These annotations are the primary input for Session C Section 3 (The Verses). They are the most verse-specific analytical outputs in the programme.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Verse reference | Specific book/chapter/verse |
| Term | Which Strong's number produced the anchor classification |
| Group | Which verse context group this anchor belongs to |
| Annotation text | 3–6 sentence analytical comment |
| Anchor type | anchor / supplementary |
| Session C flag | confirm / correct / deepen / add — which statement this addresses |
| Registry | Which word |
| Pass | Session B Pass 3 |
| Date | When annotated |

### Where is it recorded currently?

Verse annotations are **not stored in the database**. They exist only in the Session B observations log markdown file. No table in the current schema receives them.

The closest existing storage is `verse_context.notes` (sparse, 10%) — but this field is for classification notes, not analytical annotations. Using it for annotations would conflate two distinct purposes.

### What is missing?

Verse annotations have no database home. This is the most significant gap in the current schema for Session B outputs.

Three options exist:
- **Option A:** Add the annotation text as a new `annotation_text` field on `verse_context`. Simple, keeps verse data together, but conflates classification records with analytical content.
- **Option B:** Write verse annotations as OT-4 findings in `wa_session_b_findings` with `finding_type = VERSE_ANNOTATION` and an entity link to the verse via `wa_finding_entity_links`. Consistent with the unified finding store, fully queryable. Slightly less direct than a dedicated field.
- **Option C:** Defer — annotations remain in the observations log until Session C rendering, at which point the rendering process decides what to incorporate. No database write-back. Simplest operationally but loses the structured queryability.

**Researcher decision needed.** The choice affects both the `wa_session_b_findings` schema and the Session B Pass 3 write-back protocol.

### What is unclear?

The Session B instruction (Pass 3) says: "Tag each anchor verse record with annotation status. Add `VERSE_ANNOTATION_COMPLETE` flag when all anchors are annotated." It is unclear which table and field this flag targets — the current schema has no `VERSE_ANNOTATION_COMPLETE` flag type in `phase2_flag_types` and no mechanism on `verse_context` for annotation status. This instruction step has no database implementation.

---

## 8. OT-6 — Forward Pointer (Session D)

### When is there a need?

Throughout all six passes of Session B (and continuously, per SB-11), observations about cross-registry connections are raised as Session D pointers. These say: "when analysing this word in Session D, look at the connection to registry Y through this specific evidence." They are analytical directives, not conclusions. They are also raised during Dimension Review and Verse Context (where a classification decision surfaces an inter-registry observation).

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Flag code | SD_POINTER |
| Unique label | DIM-[nnn]-SD[nnn] format |
| Source registry | Which word raised this pointer |
| Target registry | Which word(s) it points to |
| Strong's reference | Primary term involved, if any |
| Priority | HIGH / MEDIUM / LOW |
| Description | Full analytical text — the observation, the registries, the question, why it cannot be answered within this registry |
| Session raised | Instruction and pass reference |
| Date raised | |
| Resolved | 0 / 1 |
| Resolved date | When resolved |
| Resolved note | How resolved |

### Where is it recorded currently?

**`wa_session_research_flags`** (327 rows, 70% SD_POINTER) — this is the correct and well-designed home. The field structure is well-matched to the requirement.

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Flag code | `flag_code` | Present |
| Unique label | `flag_label` | Present |
| Source registry | `registry_id` FK | Present |
| Target registry | `cross_registry_id` FK | Present (54% NULL — by design; some pointers have no specific target) |
| Strong's reference | `strongs_reference` | Present (51% NULL — by design; some pointers are registry-level) |
| Priority | `priority` | Present |
| Description | `description` | Present (100% populated, avg 524 chars) |
| Session raised | `session_raised` | Present — but format is inconsistent across 34 distinct formats |
| Date raised | `raised_date` | Present |
| Resolved | `resolved` | Present (all 0 — Session D has not started) |
| Resolved date | `resolved_date` | Present (all NULL — pending Session D) |
| Resolved note | `resolved_note` | Present (all NULL — pending Session D) |

### What is missing?

No structural gaps. The table is well-designed for this purpose.

**Data quality issues (not schema gaps):**

1. `session_raised` format is inconsistent — 34 distinct formats, not programmatically parseable. Going forward, a standardised format (`[instruction-version] [pass-ref]`) should be enforced. Historical rows cannot be retrospectively corrected without risk.

2. `flag_code` naming duplication: `PH2_VOLUME_LIMITATION` (33 rows) and `VOLUME_LIMITATION` (19 rows) describe the same concept. These should be consolidated to `PH2_VOLUME_LIMITATION`.

3. `strongs_reference` multi-value entries: 7 rows contain multiple Strong's numbers as a comma or semicolon-separated string. These cannot join to `mti_terms`. These rows should be reviewed when term-level queries are needed and split into separate rows if the analytical reasoning supports it.

### What is unclear?

When a Session D pointer is resolved by a Session D analysis, the resolution writes `resolved = 1`, `resolved_date`, and `resolved_note` on this table — and should also write an OT-4 finding to `wa_session_b_findings` recording the synthesis observation. The link between a resolution note and the finding that resolved it does not yet exist: the `resolved_note` field is free text, not a FK. Whether this matters depends on how Session D is designed — this is flagged for the Session D instruction design phase.

---

## 9. OT-7 — Data Quality Flag

### When is there a need?

Session B Stage 1 (data audit) and Verse Context processing both surface data quality issues: incorrect field values, homonym contamination, extraction anomalies, missing root family records, volume limitations, terms that need splitting. These must be recorded as actionable flags that direct Claude Code remediation.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Flag code | Specific type (PH2_DATA_ERROR, PH2_VOLUME_LIMITATION, etc.) |
| Registry | Which word |
| Term | Which Strong's number, if term-specific |
| Priority | HIGH / MEDIUM / LOW |
| Session target | B (fix before Stage 2) or D (acceptable for now) |
| Description | What the issue is, specifically |
| Date raised | |
| Resolved | 0 / 1 |

### Where is it recorded currently?

**`wa_session_research_flags`** (same table as OT-6) — the non-SD_POINTER rows serve this purpose. The 80 data quality and volume flag rows (PH2_*, VOLUME_LIMITATION, PH2_DATA_ERROR, etc.) capture data quality observations at the same level of detail as Session D pointers.

The mapping is adequate. No structural gaps.

---

## 10. OT-8 — Session C Correction Flag

### When is there a need?

Session B Stage 3 reviews the existing Session C word study against the completed analysis. Where the word study contains a statement that is factually incorrect, incomplete, or contradicted by data, that must be flagged and corrected. Where a statement was premature (a Session D question treated as settled), it must be reopened. These correction flags drive the word study update.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Word study section | Which section the error appears in |
| The incorrect statement | What it says |
| The correction | What it should say |
| Evidence | What data establishes the correction |
| Action required | Correct / deepen / reopen / add |
| Related finding | Link to the OT-4 finding or OT-6 pointer that generates this correction |

### Where is it recorded currently?

Session C correction flags live in two places:

1. **The Session B observations log** — the markdown file records corrections as they are identified during Stage 3 review. This is the working record.

2. **`wa_session_b_findings`** with `finding_type = DIMENSION_REVIEW` or similar — some correction observations are written as findings but without a `study_segment` or correction-specific structure.

There is no dedicated correction record structure in the database. Corrections are prose observations embedded in findings, not structured records.

### What is missing?

No separate table is needed. Session C corrections are a subset of OT-4 findings: they are findings with `finding_type = SESSION_C_CORRECTION` and `study_segment` pointing to the affected word study section. The missing fields on `wa_session_b_findings` (particularly `study_segment` and `related_finding_id`) are what would make correction findings queryable and trackable. The field additions in Section 6 above are therefore sufficient to cover OT-8 as well.

---

## 11. Implementation Plan

The gaps identified above resolve into three categories of change:

### Category 1 — Data quality cleanup (CC directive, no schema migration)

These should be completed before any schema migration begins:

| Action | Table | Detail |
|--------|-------|--------|
| Normalise `finding_type` | `wa_session_b_findings` | Standardise to UPPER_SNAKE_CASE throughout. Map: `theological_note` → `THEOLOGICAL_NOTE`, `verse_pattern` → `VERSE_PATTERN`, `term_behaviour` → `TERM_BEHAVIOUR`, `etymology` → `ETYMOLOGY`, `C22` → `DIMENSION_REVIEW` (confirm with researcher). |
| Consolidate `flag_code` | `wa_session_research_flags` | Update all 19 `VOLUME_LIMITATION` rows to `PH2_VOLUME_LIMITATION`. |

### Category 2 — Add fields to existing table (schema migration, minor)

Add the following fields to `wa_session_b_findings`. All nullable except `delete_flag` (default 0). Increment schema version.

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `pass_ref` | TEXT | NULL | Pass-level attribution (e.g. "Session B Pass 3", "Dimension Review Phase C") |
| `study_segment` | TEXT | NULL | Rendering-target declaration. Controlled vocabulary in Section 12. |
| `delete_flag` | INTEGER | 0 | Obsolescence marker. 0 = active; 1 = obsolete. |
| `obsolete_reason` | TEXT | NULL | Required when `delete_flag` = 1. |
| `obsolete_date` | TEXT | NULL | Date marked obsolete. |
| `superseded_by_id` | INTEGER | NULL | FK to `wa_session_b_findings.id` of replacement. Self-referential. |
| `related_finding_id` | INTEGER | NULL | FK to `wa_session_research_flags.id` (pointer resolved) or `wa_session_b_findings.id` (finding superseded or built on). |

Add `classified_by_instruction` (TEXT, NULL) to both `verse_context` and `verse_context_group` for OT-1 and OT-2 attribution.

Add `dim_review_instruction` (TEXT, NULL) to `wa_dimension_index` for OT-3 attribution.

### Category 3 — New table (schema migration, new)

Create `wa_finding_entity_links` as specified in Section 6 above. Add indexes on `finding_id` and on `(entity_type, entity_id)`.

### Researcher decisions required before implementation

1. **Verse annotations (OT-5):** Which option — store as OT-4 findings (Option B), add a field to `verse_context` (Option A), or defer (Option C)? This determines whether an additional finding_type is needed and whether Pass 3 produces a database patch.

2. **`wa_session_b_dimensions` table:** Retire or retain? If retained, should it be populated going forward? If retired, the spirit-soul-body classification at registry level sits only on `word_registry.sb_classification` — is that sufficient?

3. **`wrong_face` target registry link:** Should a `wrong_face` set-aside record carry a FK to the target registry it belongs to? Or is the notes field sufficient for rediscovery?

4. **`finding_type` for "C22" row:** Is `DIMENSION_REVIEW` the correct normalisation, or was the C22 cluster code significant and deserving a different type?

---

## 12. `study_segment` Controlled Vocabulary

When `study_segment` is added to `wa_session_b_findings`, it must draw from a controlled vocabulary. The vocabulary maps a finding to the section of the Session C word study or Session B analytical brief where it will be rendered.

### Word study sections

| Value | Maps to |
|-------|---------|
| `word_study_s1_characteristic` | Section 1: The Characteristic |
| `word_study_s2_how_it_works` | Section 2: How It Works |
| `word_study_s3_verses` | Section 3: The Verses |
| `word_study_s4_vocabulary` | Section 4: The Vocabulary (whole section) |
| `word_study_s4_[root_code]` | Section 4 sub-segment per root family (e.g. `word_study_s4_racham`) |
| `word_study_s5_connections` | Section 5: Connections and Research Pointers (whole section) |
| `word_study_s5_reg_[n]_[word]` | Section 5 sub-segment per named connection |

### Analytical brief sections

| Value | Maps to |
|-------|---------|
| `brief_s2_meaning_findings` | Brief Section 2: Meaning Findings |
| `brief_s3_divine_dimension` | Brief Section 3: Divine Dimension |
| `brief_s4_somatic_signature` | Brief Section 4: Somatic Signature |
| `brief_s5_spirit_soul_body` | Brief Section 5: Spirit-Soul-Body Classification |
| `brief_s6_sessionc_corrections` | Brief Section 6: Session C Corrections |
| `brief_s7_correlation_connections` | Brief Section 7: Correlation Connections |
| `brief_s8_cross_word_questions` | Brief Section 8: Cross-Word Questions |
| `brief_s9_open_items` | Brief Section 9: Open Items |

### Other

| Value | Use |
|-------|-----|
| `unassigned` | Not yet allocated — temporary state during pass work |
| `cross_segment` | Applies to multiple sections; used in more than one place |

---

## 13. Summary of Gaps

| # | Gap | Severity | Location | Resolution |
|---|-----|----------|----------|------------|
| G-1 | No attribution fields on `verse_context` | Low | OT-1 | Add `classified_by_instruction`, `classified_date` |
| G-2 | No attribution field on `verse_context_group` | Low | OT-2 | Add `classified_by_instruction` |
| G-3 | No instruction field on `wa_dimension_index` | Low | OT-3 | Add `dim_review_instruction` |
| G-4 | `wa_session_b_findings` missing 7 fields | High | OT-4, OT-8 | Add fields per Section 11 Category 2 |
| G-5 | No entity-level FK from findings to terms/verses/groups/dimensions | High | OT-4 | New table `wa_finding_entity_links` |
| G-6 | `finding_type` naming inconsistency | Medium | OT-4 | Normalise per Section 11 Category 1 |
| G-7 | Verse annotations have no database home | Medium | OT-5 | Researcher decision needed (Section 11) |
| G-8 | `VERSE_ANNOTATION_COMPLETE` flag has no implementation | Low | OT-5 | Depends on G-7 decision |
| G-9 | `flag_code` naming duplication | Low | OT-6/7 | Consolidate `VOLUME_LIMITATION` → `PH2_VOLUME_LIMITATION` |
| G-10 | `strongs_reference` multi-value entries (7 rows) | Low | OT-6/7 | Review and split when term-level queries needed |
| G-11 | `session_raised` format inconsistency | Low | OT-6/7 | Enforce standard format going forward; historical rows as-is |
| G-12 | No FK between resolved pointer and resolving finding | Low | OT-6 | Deferred to Session D instruction design |

---

*Produced under GR-OBS-002, GR-OBS-005, GR-OBS-006, GR-PASS-002. For researcher review before implementation begins.*
