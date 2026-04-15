# WA Global — Observations Schema

**Filename:** wa-global-obs-schema-v2_1-20260414.md
**Date:** 2026-04-14
**Version:** 2.1
**Previous output ref:** wa-global-obs-schema-v2-20260414.md
**Status:** Active — supersedes v2.0.

## Change note

v2.1 (2026-04-14): Three substantive additions addressing gaps in v2.0. (1) Verse Context and Dimension Review analytical finding types expanded: both phases produce category (b) findings that are not captured in their primary outputs (verse classification or dimension assignment). These are now specified with examples of what to look for and record. (2) Session D dependency made explicit throughout: Session D synthesis depends entirely on the quality, type, and entity-linkage of what Session B, Dimension Review, and Verse Context record. The connection is stated at each observation type where it is relevant. (3) Root and cross-registry entity types restored from v1.0 and mapped to the existing schema — both were absent from v2.0 despite being named as first-class entities in v1.0.

---

## 1. Purpose and Scope

This document governs the recording of analytical observations across the full programme pipeline. It specifies — for each type of observation produced by any programme phase — when the need arises, what must be recorded, how it must be recorded, where it goes in the current database, what is missing, and what is still unclear.

The four phases that produce observations requiring database storage are:

| Phase | Primary output | Also produces |
|-------|---------------|---------------|
| **Verse Context** | Verse relevance classifications and group descriptions | Analytical findings: observations about what verses reveal beyond what a group description captures — cross-registry signals, term-level insights, interpretation questions |
| **Dimension Review** | Dimension assignments and dominant subject designations | Analytical findings: cross-group patterns, root family connections, cluster-level observations, Session B/D pointers arising from group reading |
| **Session B** | Term-level analysis: meaning, somatic evidence, spirit-soul-body classification, verse annotations, connection characterisations | Forward pointers (SD_POINTERs) and data quality flags |
| **Session C** | Word study prose | Correction flags: statements contradicted by Session B data; pointers prematurely treated as settled |

**Session D dependency.** Session D is the cross-registry synthesis phase. It begins not with words but with questions about the inner life that emerge when the full body of word-study data is laid alongside itself. Session D's ability to do this work depends entirely on what was recorded during Verse Context, Dimension Review, and Session B. The SD_POINTER flags are the structural bridge (wa_session_research_flags); the analytical findings are the substantive bridge (wa_session_b_findings). If either is thin, Session D works with incomplete material. The observation types in this document — especially OT-4 (analytical finding) and the root and cross-registry entity types — are the direct feedstock for Session D's investigation work.

---

## 2. Observation Type Catalogue

Eight types of analytical output require database storage. They are distinct in nature, origin, and data shape.

| Type | Produced by | Session D relevance |
|------|------------|---------------------|
| **OT-1** Verse relevance decision | Verse Context | Indirect — determines which verses are in scope for all analysis |
| **OT-2** Group classification | Verse Context | Medium — group descriptions are the primary lens Session D uses to read verse evidence |
| **OT-3** Dimension assignment | Dimension Review | High — dimension overlap across registries is a core Session D signal |
| **OT-4** Analytical finding | All phases | **Primary** — findings are the substantive content Session D synthesises |
| **OT-5** Verse annotation | Session B Pass 3 | High — anchor verse readings surface cross-registry relationships |
| **OT-6** Forward pointer (SD) | All phases, continuous | **Primary input** — the structural bridge to Session D |
| **OT-7** Data quality flag | Verse Context, Session B Stage 1 | Low — remediation record, not analytical content |
| **OT-8** Session C correction | Session B Stage 3, Session C | Medium — corrects the published word study |

---

## 3. OT-1 — Verse Relevance Decision

### When is there a need?

Every verse in a term's corpus is evaluated for inner-being relevance during Verse Context. The decision (anchor / relevant / related / set-aside) and the reason for any set-aside must be recorded. All subsequent analysis depends on this filter.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Registry and term | Which word, which Strong's number |
| Verse | Which verse |
| Decision | anchor / relevant / related / set-aside |
| Set-aside reason | If set-aside: no_inner_being / physical_only / spatial_only / wrong_face / other |
| Notes | Only where the decision requires explanation |
| Instruction version | Under which instruction classified |

### Where is it recorded?

**`verse_context`** (63,028 rows) — correct home. All primary fields present.

### What is missing?

`classified_by_instruction` (TEXT, NULL) and `classified_date` (TEXT, NULL) are absent. These are needed for audit when a classification is revisited: knowing which instruction version applied at the time determines whether a change is a correction or an instruction upgrade.

### What is unclear?

The `wrong_face` set-aside value (Verse Context v2.5) marks verses analytically significant from a different registry's perspective. The instruction describes a rediscovery mechanism — reading all `wrong_face` records for a target registry before Session B. It is not yet clear whether a formal FK from a `wrong_face` row to the target registry is needed in the schema, or whether the notes field is sufficient.

---

## 4. OT-2 — Group Classification

### When is there a need?

During Verse Context, relevant verses are grouped by the inner-being characteristic the verse cluster is primarily about. The group description and code are the primary analytical input for both Dimension Review and Session B.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Registry and term | Which word, which Strong's |
| Group code | Unique identifier (e.g. 2310-001) |
| Group description | Characteristic-perspective statement of what this verse cluster is about |
| Instruction version | Under which instruction this group was created |

### Where is it recorded?

**`verse_context_group`** (3,550 rows) — correct home. Primary fields present.

### What is missing?

`classified_by_instruction` (TEXT, NULL) — absent from this table, same gap as OT-1.

---

## 5. OT-3 — Dimension Assignment

### When is there a need?

Dimension Review assigns each verse context group to an emergent inner-being dimension. The assignment, confidence level, dominant subject characterisation, and reasoning must all be recorded. This is the bridge between grouped verse evidence and Session B analysis.

Dimension assignments are also a primary Session D signal: `dimension_overlap` (the correlation signal showing which registries share confirmed dimensions) is built from this table. The quality and granularity of dimension assignments directly determines how productive that Session D signal is.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Group | Which verse context group |
| Dimension | The assigned dimension label |
| Dominant subject | GOD / HUMAN / OTHER_HUMAN / UNSEEN / NONE |
| Confidence level | AUTOMATED / CLAUDE_AI / RESEARCHER |
| Manual override | Whether researcher has locked this |
| Assignment reasoning | Why this dimension fits — analytical rationale |
| Instruction version | Under which Dimension Review instruction this was assigned |
| Date | Captured via `last_modified` auto-timestamp |

### Where is it recorded?

**`wa_dimension_index`** (3,500 rows) — correct home. Most fields present.

### What is missing?

`dim_review_instruction` (TEXT, NULL) — absent at individual group row level. The `wa_dim_review_cluster_log` records instruction version at cluster level, but a group revised during Session B (e.g. a dimension corrected after new verse evidence) has no row-level record of which instruction applied at revision time.

---

## 6. OT-4 — Analytical Finding

### When is there a need?

This is the most important observation type in the programme. An analytical finding is a substantive analytical observation grounded in specific evidence — a verse, a term, a group, a dimension pattern, a root connection, a cross-registry relationship — that names something which was not visible before the analysis was conducted.

**Analytical findings arise in all four phases.** The distinction that matters is this: a group description records *what a verse cluster is about*; a dimension assignment records *which inner-being dimension it engages*. An analytical finding records *what was observed that those two fields cannot hold* — the insight, the pattern, the question, the connection.

#### What Verse Context produces as analytical findings

Verse Context is primarily a classification phase, but verse reading regularly surfaces material that goes beyond the classification decision. This material has no home in `verse_context` or `verse_context_group`. It must be written as an analytical finding in `wa_session_b_findings` at the time of discovery — not deferred to Session B.

**What to look for and record during Verse Context:**

| Signal | Example | Why it matters |
|--------|---------|---------------|
| A verse implying a structural inner-being relationship not captured by its group | Reading H2347 *chus* (to withhold pity) and noticing that Ezek 9:10 places the withdrawal of divine pity in direct causal relationship with human injustice — this is not captured in a group description of "divine withholding of compassion" | These structural relationships are Session D's primary investigation material |
| A term behaving differently from its gloss in a specific verse | A term glossed "comfort" appearing in a context that is grammatically a refusal, making it carry a meaning closer to "resignation" | Term-behaviour observations inform Session B Pass 1 meaning analysis |
| A verse that appears to connect two registries through a shared theological mechanism | A verse where H5162 *na.cham* (relent/comfort) functions as the pivot between divine anger and divine compassion — linking repentance and mercy registries | Cross-registry connections surface here before any correlation signal fires |
| An unexpected set-aside reason that reveals something analytically significant | A `wrong_face` set-aside where the inner-being content clearly belongs to a different registry — identifying which registry and why is itself a finding | Enables vertical pass discovery and feeds Session D |
| A term whose classification raises a question about the inner-being model itself | Classifying H3820A *lev* (heart) in a verse where it clearly operates at the level of both cognition and volition simultaneously — challenging the dimension system's ability to separate these | These are the observations that generate new dimension proposals or Session D structural questions |

The Verse Context instruction provides the Session B flags document (`wa-vcb-{batch_id}-sessionB-flags-v{n}-{date}.md`) as a handoff channel for such findings. The schema must ensure these findings are also written to the database, not only to the markdown file.

#### What Dimension Review produces as analytical findings

Dimension Review is also primarily a classification phase, but group reading surfaces observations that belong in the programme's analytical record beyond the dimension assignment itself. The Dimension Review instruction (Section 5.4) explicitly requires capturing these as Session B findings and Session D pointers.

**What to look for and record during Dimension Review:**

| Signal | Example | Why it matters |
|--------|---------|---------------|
| An anchor verse revealing inner-being content not captured by its group description | Reading the anchor verse for group 1613-001 and noticing that the verse also encodes a conditional structure (covenant obedience → divine favour) not named in the group description | This conditional structure may be significant for multiple registries and for Session D |
| Cross-group pattern within a cluster | Three registries in C17 all show a GOD-dominant group in the Relational Disposition dimension — the consistency of the divine-initiative pattern is a cluster-level finding | This pattern is exactly what Session D investigates — it cannot be seen from any single word study |
| Convergence or divergence between registries | Two registries share what appears to be the same inner-being state (e.g. deep seated compassion) but one assigns it to Relational Disposition and one to Emotion — this divergence is a finding about the dimension system's adequacy | Session D needs to know where the dimension vocabulary breaks down |
| Root family connection revealed by the root family extract | The root family extract shows that H7355 *racham* and H7358 *rechem* share the same womb-root across Compassion and Love registries — this is a finding about the biological metaphor underlying the vocabulary | Root-level connections are a dedicated Session D signal type |
| A dimension that appears in an unexpected cluster | A Transformation dimension group appearing in a cluster dominated by Relational Disposition words — the tension between transformation and relational disposition is analytically significant | These unexpected placements are productive Session D questions |
| A group that fits no existing dimension | Reading a group that clearly describes something like "the inner stillness that precedes divine receptivity" — which is not Emotion, not Cognition, not Volition, not Relational Disposition | Vocabulary gaps are findings about the programme's emergent framework |
| A property-term group that serves different characteristics across the cluster | H8085 *sha.ma* (hear) appearing in contexts of heart-obedience in one group and cognitive reception in another — the same term serving two different inner-being characteristics | This is a Session B finding about term behaviour that feeds Pass 1 analysis |

All of these are written to `wa_session_b_findings` via the Dimension Review patch. They are not dimension assignments — they are the observations that arise *while* assigning dimensions.

### What must be recorded for every analytical finding?

| Data point | Notes |
|-----------|-------|
| Finding text | The substantive analytical content — free prose |
| Finding type | What kind of finding (see controlled vocabulary below) |
| Registry | Which word this finding belongs to |
| Phase / pass of origin | Which phase and pass produced this: e.g. "Verse Context VCB-031", "Dimension Review Phase C C17", "Session B Pass 1" |
| Entity links | Which specific entities this finding is about — must link to the term, verse, group, dimension, root, or cross-registry entity it describes |
| Rendering target | Which section of the word study or brief this finding will be used in |
| Instruction version | Under which instruction this was produced |
| Date | When raised |
| Obsolete flag | Whether this finding has been superseded |
| Obsolete reason and date | If superseded |
| Superseded by | Link to replacement finding |
| Resolution link | If this finding resolves a forward pointer, link to the pointer record |

### Finding type controlled vocabulary

| Type | Produced by | Example |
|------|------------|---------|
| `MEANING_OBSERVATION` | Session B Pass 1 | Sense structure, semantic range, boundary condition |
| `VERSE_PATTERN` | Session B Pass 3, Verse Context | A pattern visible across a verse group or individual verse |
| `VERSE_ANNOTATION` | Session B Pass 3 | Per-anchor-verse 3–6 sentence analytical annotation |
| `THEOLOGICAL_NOTE` | Session B Pass 2 | Divine involvement pattern, eschatological dimension |
| `SOMATIC_EVIDENCE` | Session B Pass 4 | Body-part vocabulary, somatic classification |
| `SPIRIT_SOUL_BODY` | Session B Pass 4 | Provisional spirit-soul-body classification with reasoning |
| `ETYMOLOGY` | Session B | Root etymology or historical semantic observation |
| `ROOT_FINDING` | Session B Pass 1, Dimension Review | Observation about a root family, its scope, or its cross-registry significance |
| `DIMENSION_REVIEW` | Dimension Review | Group quality assessment, dimension discernment observation, cluster pattern |
| `GROUP_INTEGRITY` | Dimension Review, Verse Context | Group structural concern — anchor quality, verse assignment issue |
| `CROSS_REGISTRY` | All phases | Observation about a relationship between two registries, not yet a full SD_POINTER |
| `TERM_BEHAVIOUR` | Verse Context, Session B | Observation about how a specific term behaves in its verse corpus |
| `SESSION_C_CORRECTION` | Session B Stage 3, Session C | A word study statement that must be corrected, deepened, or reopened |
| `OPEN_ITEM` | Any phase | A question that cannot be resolved from current data — not yet a Session D pointer |

### Where is it recorded?

**`wa_session_b_findings`** — correct home. This table receives analytical findings from **all four phases**, not only from Session B. The table name is a legacy of its original scope; its actual role is the programme-wide analytical finding store.

Current field coverage:

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Finding text | `finding` | Present |
| Finding type | `finding_type` | Present — naming inconsistent (UPPER_SNAKE vs lower_snake; "C22" used as type) |
| Registry | `registry_id` FK | Present |
| Phase/pass of origin | Partially in `session_b_instruction` | Partial — instruction version only; phase and pass absent |
| Entity links | Not present | **Missing** |
| Rendering target | Not present | **Missing** |
| Instruction version | `session_b_instruction` | Present |
| Date | `raised_date` | Present |
| Obsolete flag | Not present | **Missing** |
| Obsolete reason/date | Not present | **Missing** |
| Superseded by | Not present | **Missing** |
| Resolution link | Not present | **Missing** |

### What is missing?

**Missing fields on `wa_session_b_findings`:**

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `pass_ref` | TEXT | NULL | Phase and pass attribution: e.g. "Verse Context VCB-031", "Dimension Review Phase C C17", "Session B Pass 3" |
| `study_segment` | TEXT | NULL | Rendering-target declaration per GR-OBS-006. Controlled vocabulary in Section 12 |
| `delete_flag` | INTEGER | 0 | Obsolescence marker. 0 = active; 1 = obsolete. Named `delete_flag` not `delete` to avoid reserved word conflict |
| `obsolete_reason` | TEXT | NULL | Required when `delete_flag` = 1 |
| `obsolete_date` | TEXT | NULL | Date marked obsolete |
| `superseded_by_id` | INTEGER | NULL | FK to `wa_session_b_findings.id` of replacement. Self-referential |
| `related_finding_id` | INTEGER | NULL | Multi-purpose link: (i) the `wa_session_research_flags.id` this finding resolves; (ii) the prior finding this supersedes; (iii) a related finding this builds on |

**Missing table — entity links:**

No FK path exists from a finding to the specific entity it describes. Without entity links:
- Session C cannot query "all findings with study_segment = word_study_s4_racham for registry 23"
- Session D cannot query "all findings about root family RACHAM across all registries"
- "All findings about group 2310-001" cannot be answered programmatically

A new junction table is needed: **`wa_finding_entity_links`**

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER PK | Stable identifier |
| `finding_id` | INTEGER FK | References `wa_session_b_findings.id` |
| `entity_type` | TEXT NOT NULL | Controlled vocabulary — see Section 7 below |
| `entity_id` | INTEGER | The id of the entity in its table. Polymorphic — entity_type determines which table |
| `entity_strongs` | TEXT nullable | Denormalised Strong's number for term links |
| `raised_date` | TEXT | Date this link was created |

---

## 7. Entity Types — The Six Entities a Finding Can Be Linked To

An analytical finding is about one or more of six entity types. Each is a distinct class of programme object. The entity type determines which table `entity_id` points into.

| Entity type | `entity_type` value | Points to table | Notes |
|------------|---------------------|----------------|-------|
| **Term** | `term` | `wa_term_inventory.id` | A finding about a specific Strong's number in a specific registry. The most granular entity level. |
| **Verse** | `verse` | `verse_context.id` | A finding about a specific verse classification record — i.e. this verse as it appears in this term's corpus. Not the same as the verse record itself. |
| **Group** | `group` | `verse_context_group.id` | A finding about a contextual meaning group — its description, its verse composition, its characteristic. |
| **Dimension** | `dimension` | `wa_dimension_index.id` | A finding about a dimension assignment — why this dimension was assigned, what its confidence level implies, or where it is analytically uncertain. |
| **Root family** | `root_family` | `wa_term_root_family.id` | A finding about a root family — its scope, its etymology, its cross-registry reach. Root is a first-class entity per researcher direction (2026-04-13). |
| **Cross-registry** | `cross_registry` | `wa_session_research_flags.id` | A finding about a cross-registry relationship — the analytical content that accompanies or resolves an SD_POINTER. This is how a Session D resolution writes back: a new finding linked to the pointer it resolves. |

**Registry-level findings** (findings about a whole word rather than any specific entity within it) use `entity_type = registry` pointing to `word_registry.id`. These are the "four-root-family structure of the compassion vocabulary" type findings — registry-level characterisations. `registry_id` on `wa_session_b_findings` already captures this, so `wa_finding_entity_links` is not strictly required for registry-level findings — but writing a registry link row provides consistency.

**Multi-entity findings.** A finding about the connection between Compassion and Mercy through the ELE root writes one row in `wa_session_b_findings` and two rows in `wa_finding_entity_links` — one with `entity_type = root_family` pointing to the ELE root record, and one with `entity_type = cross_registry` pointing to the SD_POINTER that names the Compassion↔Mercy connection. The two index rows share the same `finding_id`.

### Root family entity — current schema state

Root families currently live in `wa_term_root_family` (2,861 rows, 22% gap from pre-backfill era). Each row has a stable `id`. Root-level findings can be linked via `entity_type = root_family` pointing to this table. **No new table is needed for root.** The 22% gap means some root-level findings will point to root records that do not yet exist — these require a root family record to be created before the finding link can be inserted.

Root families are also visible in `correlations.root_families` (a derived view from the extract). A finding about a root family that spans multiple registries must link to the root record, not to the correlation view (which has no stable id). If the root record does not exist in `wa_term_root_family` for a cross-registry root, that is itself a data gap requiring a CC directive.

### Cross-registry entity — current schema state

Cross-registry relationships are held in two places:
- `wa_session_research_flags` (SD_POINTER rows) — the active, growing store for Session B–onward cross-registry observations
- `wa_cross_registry_links` — the Session A–era store (158 rows, connecting_term not joinable, being superseded)

For findings about cross-registry relationships, `entity_type = cross_registry` should point to `wa_session_research_flags.id` when the relationship is captured there. For Session A–era links, pointing to `wa_cross_registry_links.id` is permissible but lower priority.

The v1.0 proposal to promote cross-registry relationships to a dedicated first-class `xref` table is deferred. The SD_POINTER mechanism in `wa_session_research_flags` is the current operational store, and it is adequate for linking.

---

## 8. OT-5 — Verse Annotation

### When is there a need?

Session B Pass 3 produces a structured annotation for every anchor verse — a 3–6 sentence analytical comment that names what the verse contributes that a plain summary cannot carry. These annotations are the primary input for Session C Section 3. They are also a productive source of cross-registry observations (Pass 3 is explicitly identified in the Session B instruction as "the primary pass for cross-registry observation").

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Verse and term | Which verse, which Strong's |
| Group | Which verse context group this anchor belongs to |
| Registry | Which word |
| Annotation text | 3–6 sentence analytical comment |
| Anchor type | anchor or supplementary |
| Session C flag | confirm / correct / deepen / add — which word study statement this addresses |
| Cross-registry observation | If the annotation surfaces a cross-registry connection — link to a new SD_POINTER |

### Where is it recorded?

Verse annotations are **not stored in the database**. They exist only in the Session B observations log markdown. No table receives them.

### What is missing?

Verse annotations have no database home. Three options:

| Option | Description | Consequence |
|--------|-------------|-------------|
| **A — OT-4 finding** | Write each annotation as an analytical finding in `wa_session_b_findings` with `finding_type = VERSE_ANNOTATION` and entity links to the verse and group | Consistent approach; fully queryable; Session C can retrieve all annotations for a registry with a single query |
| **B — Field on verse_context** | Add `annotation_text` field to `verse_context` | Simpler; keeps verse data together; conflates classification record with analytical content |
| **C — Defer** | Annotations remain in markdown; Session C rendering works from the markdown log | Simplest operationally; annotations are not queryable or reusable across sessions |

**Researcher decision needed.** Option A is the most consistent with the programme's data architecture — verse annotations are findings, not classification records.

### What is unclear?

The Session B instruction (Pass 3) states: "Tag each anchor verse record with annotation status. Add `VERSE_ANNOTATION_COMPLETE` flag when all anchors are annotated." No `VERSE_ANNOTATION_COMPLETE` flag type exists in `phase2_flag_types` and no mechanism on `verse_context` supports annotation status. This instruction step has no database implementation.

---

## 9. OT-6 — Forward Pointer (Session D)

### When is there a need?

Session D pointers are raised continuously throughout all phases — not only in Session B Pass 6. The Session B instruction (SB-11) makes this explicit: "Session D pointers must be raised at the moment of discovery during any pass." The Dimension Review instruction (Section 5.4) requires the same during Phase C. The Verse Context instruction provides the Session B flags document as the handoff channel for observations arising during classification.

An SD_POINTER says: "when investigating this question at Session D, look at the connection between registry X and registry Y through this specific verse, term, or root." It is a structural observation and a question — not a conclusion. Session D is where the question is investigated.

**Every observation type that cannot be resolved within a single registry's data is a candidate for an SD_POINTER.** The distinction between an OT-4 finding and an OT-6 pointer is:
- OT-4: an observation grounded in this registry's data — what it reveals about this word
- OT-6: an observation that requires cross-registry data to resolve — what it raises as a question for Session D

### What must be recorded?

Per `wa_session_research_flags` SD_POINTER field specification (from Session D Orientation v3.0 Section 5.2):

| Data point | Field |
|-----------|-------|
| Source registry | `registry_id` |
| Target registry | `cross_registry_id` |
| Flag code | `flag_code = 'SD_POINTER'` |
| Unique label | `flag_label` (DIM-[nnn]-SD[nnn]) |
| Priority | `priority` (HIGH / MEDIUM / LOW) |
| Full analytical description | `description` |
| Session and pass raised | `session_raised` |
| Date | `raised_date` |
| Resolved | `resolved` (0 / 1) |
| Resolution note | `resolved_note` |

### Where is it recorded?

**`wa_session_research_flags`** (327 rows, 70% SD_POINTER) — correct and well-designed home. All required fields present.

### What is missing?

No structural gaps. Two data quality issues:

1. `flag_code` naming duplication: `PH2_VOLUME_LIMITATION` (33 rows) and `VOLUME_LIMITATION` (19 rows) — same concept, two codes. Consolidate to `PH2_VOLUME_LIMITATION`.

2. `session_raised` format is inconsistent (34 distinct formats). Enforce a standard going forward: `[instruction-version] [phase] [pass-ref]` (e.g. "WA-SessionB-Instruction-v4.7 Pass 3"). Historical rows cannot be retrospectively corrected.

### What is unclear?

When Session D resolves a pointer, it marks `resolved = 1` and writes `resolved_note`. The resolution should also produce an OT-4 finding in `wa_session_b_findings` recording the synthesis observation. The link from the resolution note (free text) to the finding that produced it does not yet exist structurally. Whether this matters depends on Session D's design — flagged for the Session D instruction design phase.

---

## 10. OT-7 — Data Quality Flag

### When is there a need?

Data quality issues surface during Verse Context processing and Session B Stage 1 data audit: incorrect field values, homonym contamination, extraction anomalies, missing root family records, volume limitations, terms requiring splitting.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Flag code | PH2_DATA_ERROR / PH2_VOLUME_LIMITATION / PH2_DATA_QUALITY / etc. |
| Registry and term | Source and term-level where applicable |
| Priority | HIGH / MEDIUM / LOW |
| Session target | B (fix before Stage 2) or D (acceptable for now) |
| Description | What the issue is, specifically |
| Date | When raised |
| Resolved | 0 / 1 |

### Where is it recorded?

**`wa_session_research_flags`** — non-SD_POINTER rows. The 80 data quality and volume flag rows cover this function adequately. No structural changes needed.

---

## 11. OT-8 — Session C Correction Flag

### When is there a need?

Session B Stage 3 reviews the word study against the completed analysis. Where a word study statement is factually incorrect, incomplete, or contradicted by data, it must be flagged and corrected. Where a statement prematurely treated an SD_POINTER as settled, it must be reopened.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Word study section | Which section contains the error |
| The incorrect statement | What it says |
| The correction | What it should say |
| Evidence | What data establishes the correction |
| Action required | correct / deepen / reopen / add |
| Related finding or pointer | Link to the OT-4 finding or OT-6 pointer that generates this correction |

### Where is it recorded?

Session C corrections are a subset of OT-4 findings: they use `finding_type = SESSION_C_CORRECTION` and `study_segment` pointing to the affected section. The missing fields on `wa_session_b_findings` (particularly `study_segment` and `related_finding_id`) are what makes correction findings queryable and trackable. No separate table is needed.

---

## 12. Implementation Plan

### Step 1 — Data quality cleanup (CC directive, no schema migration)

| Action | Table | Rows affected |
|--------|-------|--------------|
| Normalise `finding_type` to UPPER_SNAKE_CASE | `wa_session_b_findings` | All 171 — map: `theological_note` → `THEOLOGICAL_NOTE`, `verse_pattern` → `VERSE_PATTERN`, `term_behaviour` → `TERM_BEHAVIOUR`, `etymology` → `ETYMOLOGY`. Confirm `C22` normalisation with researcher before executing. |
| Consolidate `flag_code` | `wa_session_research_flags` | 19 rows — update `VOLUME_LIMITATION` → `PH2_VOLUME_LIMITATION` |

### Step 2 — Add fields to existing tables (schema migration, minor)

**On `wa_session_b_findings`:**

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `pass_ref` | TEXT | NULL | Phase and pass attribution |
| `study_segment` | TEXT | NULL | Rendering-target declaration per Section 13 |
| `delete_flag` | INTEGER | 0 | Obsolescence marker |
| `obsolete_reason` | TEXT | NULL | Required when `delete_flag` = 1 |
| `obsolete_date` | TEXT | NULL | Date marked obsolete |
| `superseded_by_id` | INTEGER | NULL | FK to this table's `id` — self-referential |
| `related_finding_id` | INTEGER | NULL | Link to resolved pointer or superseded finding |

**On `verse_context`:**

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `classified_by_instruction` | TEXT | NULL | Instruction version at time of classification |
| `classified_date` | TEXT | NULL | Date classified |

**On `verse_context_group`:**

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `classified_by_instruction` | TEXT | NULL | Instruction version at time of group creation |

**On `wa_dimension_index`:**

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `dim_review_instruction` | TEXT | NULL | Instruction version at time of dimension assignment |

### Step 3 — Create new table (schema migration)

Create `wa_finding_entity_links` as specified in Section 6. Add indexes on `finding_id` and on `(entity_type, entity_id)`.

### Step 4 — Verify write path

Test patch inserting one finding with entity links (a term link, a group link, and a root_family link). Verify chain: finding inserted → entity links inserted → query retrieves finding with all entity links. Confirm root family record exists before test (to exercise the pre-existence check requirement).

### Step 5 — Activate write protocols

Update Session B, Dimension Review, and Verse Context instructions to declare that all OT-4 analytical findings are written to `wa_session_b_findings` at pass close (or at end-of-batch for Verse Context), with `pass_ref`, `study_segment`, and entity links populated. The observations log becomes a session narrative; the database holds the analytical content.

### Researcher decisions required before Step 2

1. **Verse annotations (OT-5):** Option A (OT-4 finding), Option B (field on `verse_context`), or Option C (defer)?
2. **`wa_session_b_dimensions` table:** Retire or retain? The spirit-soul-body classification at registry level currently sits on `word_registry.sb_classification`. Is that sufficient, or should this table be populated going forward?
3. **`wrong_face` target registry link:** Should a `wrong_face` set-aside carry a FK to the target registry?
4. **`finding_type` for "C22" row:** Correct normalisation — `DIMENSION_REVIEW` or other?

---

## 13. `study_segment` Controlled Vocabulary

### Word study sections (reader-facing)

| Value | Maps to |
|-------|---------|
| `word_study_s1_characteristic` | Section 1: The Characteristic |
| `word_study_s2_how_it_works` | Section 2: How It Works |
| `word_study_s3_verses` | Section 3: The Verses |
| `word_study_s4_vocabulary` | Section 4: The Vocabulary |
| `word_study_s4_[root_code]` | Section 4 sub-segment per root family (e.g. `word_study_s4_racham`) |
| `word_study_s5_connections` | Section 5: Connections and Research Pointers |
| `word_study_s5_reg_[n]_[word]` | Section 5 sub-segment per named connection |

### Analytical brief sections (internal)

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
| `unassigned` | Not yet allocated — temporary during pass work |
| `cross_segment` | Applies to multiple sections; used in rendering in more than one place |

---

## 14. Gap Summary

| # | Gap | Severity | Table | Resolution |
|---|-----|----------|-------|------------|
| G-1 | No attribution fields on `verse_context` | Low | OT-1 | Add `classified_by_instruction`, `classified_date` |
| G-2 | No attribution field on `verse_context_group` | Low | OT-2 | Add `classified_by_instruction` |
| G-3 | No instruction version field at row level on `wa_dimension_index` | Low | OT-3 | Add `dim_review_instruction` |
| G-4 | `wa_session_b_findings` missing 7 fields | **High** | OT-4, OT-8 | Add fields per Section 12 Step 2 |
| G-5 | No entity-level linkage from findings to terms/verses/groups/dimensions/roots/cross-registry | **High** | OT-4 | New table `wa_finding_entity_links` |
| G-6 | `finding_type` naming inconsistency | Medium | OT-4 | Normalise per Section 12 Step 1 |
| G-7 | Verse annotations have no database home | Medium | OT-5 | Researcher decision needed |
| G-8 | `VERSE_ANNOTATION_COMPLETE` flag has no database implementation | Low | OT-5 | Depends on G-7 decision |
| G-9 | `flag_code` naming duplication (VOLUME_LIMITATION variants) | Low | OT-6/7 | Consolidate per Section 12 Step 1 |
| G-10 | `strongs_reference` multi-value entries (7 rows) | Low | OT-6/7 | Review and split at query time |
| G-11 | `session_raised` format inconsistency | Low | OT-6/7 | Enforce standard going forward |
| G-12 | No FK from resolved pointer to resolving finding | Low | OT-6 | Deferred to Session D instruction design |
| G-13 | Root family records missing for ~22% of root-coded terms | Medium | OT-4 (root) | CC directive to fill gaps before root entity links are activated |

---

*Produced under GR-OBS-002, GR-OBS-005, GR-OBS-006, GR-PASS-002. For researcher review before implementation begins.*
