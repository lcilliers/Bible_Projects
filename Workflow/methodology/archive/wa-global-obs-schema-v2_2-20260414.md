# WA Global — Observations Schema

**Filename:** wa-global-obs-schema-v2_2-20260414.md
**Date:** 2026-04-14
**Version:** 2.2
**Previous output ref:** wa-global-obs-schema-v2_1-20260414.md
**Status:** Active — supersedes v2.1.

## Change note

v2.2 (2026-04-14): Four additions arising from researcher review. (1) **Session B review obligation added (Section 6, new sub-section):** Session B must review all findings raised by Verse Context and Dimension Review for this registry and bring each to a resolution before the word can close. Findings that can be resolved within the word's data must be resolved and closed in Session B. Only findings requiring cross-word data may carry forward — and when they do, they must be converted to SD_POINTERs, not left as open analytical findings. (2) **Session C role clarified (OT-8 section):** Session C prose must derive entirely from database-substantiated findings. Where Session C work surfaces a new finding or improves an existing one, that finding must be written back to the database before the prose that depends on it is finalised. Session C is not permitted to advance claims that do not have a corresponding finding record. (3) **Thin evidence protocol specified (new Section 10):** The concept of thin evidence now has a defined treatment. A thin finding is flagged explicitly, researched before it can be set aside, and recorded with a resolution outcome. An observation with insufficient supporting evidence is set aside — but only after research; it is not discarded without investigation. The flag must record the outcome. (4) **Flag resolution requirement strengthened:** All OT-7 data quality flags must be resolved before Session B is complete. Resolution must be recorded in the database. An open data quality flag at session close is a programme compliance failure equivalent to an unresolved Stage 1 audit item.

---

## 1. Purpose and Scope

This document governs the recording of analytical observations across the full programme pipeline. It specifies — for each type of observation produced by any programme phase — when the need arises, what must be recorded, how it must be recorded, where it goes in the current database, what is missing, and what is still unclear.

The four phases that produce observations requiring database storage are:

| Phase | Primary output | Also produces |
|-------|---------------|---------------|
| **Verse Context** | Verse relevance classifications and group descriptions | Analytical findings: observations about what verses reveal beyond what a group description captures — cross-registry signals, term-level insights, interpretation questions |
| **Dimension Review** | Dimension assignments and dominant subject designations | Analytical findings: cross-group patterns, root family connections, cluster-level observations, Session B/D pointers arising from group reading |
| **Session B** | Term-level analysis: meaning, somatic evidence, spirit-soul-body classification, verse annotations, connection characterisations | Forward pointers (SD_POINTERs) and data quality flags; review and resolution of all prior-phase findings for this registry |
| **Session C** | Word study prose derived entirely from database-substantiated findings | New or improved findings discovered during prose generation — written back to the database before the prose that depends on them is finalised |

**Session D dependency.** Session D is the cross-registry synthesis phase. It begins not with words but with questions about the inner life that emerge when the full body of word-study data is laid alongside itself. Session D's ability to do this work depends entirely on what was recorded during Verse Context, Dimension Review, and Session B. The SD_POINTER flags are the structural bridge (`wa_session_research_flags`); the analytical findings are the substantive bridge (`wa_session_b_findings`). If either is thin, Session D works with incomplete material. Everything that carries forward to Session D must be structured as an SD_POINTER — not an open analytical finding. The observation types in this document, especially OT-4 and the root and cross-registry entity types, are the direct feedstock for Session D's investigation work.

---

## 2. Observation Type Catalogue

Eight types of analytical output require database storage.

| Type | Produced by | Session D relevance |
|------|------------|---------------------|
| **OT-1** Verse relevance decision | Verse Context | Indirect — determines which verses are in scope |
| **OT-2** Group classification | Verse Context | Medium — group descriptions are the primary lens Session D uses to read verse evidence |
| **OT-3** Dimension assignment | Dimension Review | High — dimension overlap across registries is a core Session D signal |
| **OT-4** Analytical finding | All phases | **Primary** — findings are the substantive content Session D synthesises |
| **OT-5** Verse annotation | Session B Pass 3 | High — anchor verse readings surface cross-registry relationships |
| **OT-6** Forward pointer (SD) | All phases, continuous | **Primary structural input** — the formal bridge to Session D |
| **OT-7** Data quality flag | Verse Context, Session B Stage 1 | Indirect — unresolved data quality issues corrupt the material Session D reads |
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

`classified_by_instruction` (TEXT, NULL) and `classified_date` (TEXT, NULL) are absent. These are needed for audit when a classification is revisited: knowing which instruction version applied determines whether a change is a correction or an instruction upgrade.

### What is unclear?

The `wrong_face` set-aside value marks verses analytically significant from a different registry's perspective. The instruction describes a rediscovery mechanism for Session B. It is not yet clear whether a formal FK from a `wrong_face` row to the target registry is needed in the schema, or whether the notes field is sufficient.

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

`dim_review_instruction` (TEXT, NULL) — absent at individual group row level. The `wa_dim_review_cluster_log` records instruction version at cluster level, but a group revised during Session B has no row-level record of which instruction applied at revision time.

---

## 6. OT-4 — Analytical Finding

### When is there a need?

This is the most important observation type in the programme. An analytical finding is a substantive observation grounded in specific evidence — a verse, a term, a group, a dimension pattern, a root connection, a cross-registry relationship — that names something not visible before the analysis was conducted.

**Analytical findings arise in all four phases.** The distinction that matters: a group description records what a verse cluster is about; a dimension assignment records which inner-being dimension it engages. An analytical finding records what was observed that those two fields cannot hold — the insight, the pattern, the question, the connection.

---

### 6.1 What Verse Context produces as analytical findings

Verse Context is primarily a classification phase, but verse reading regularly surfaces material that goes beyond the classification decision. This material has no home in `verse_context` or `verse_context_group`. It must be written as an analytical finding in `wa_session_b_findings` at the time of discovery — not deferred to Session B.

**What to look for and record during Verse Context:**

| Signal | Example | Why it matters |
|--------|---------|---------------|
| A structural inner-being relationship implied by the verse but not capturable in a group description | Ezek 9:10 places the withdrawal of divine pity in direct causal relationship with human injustice — a conditional structure, not a classification | These structural relationships are Session D's primary investigation material |
| A term behaving differently from its gloss in a specific verse | A term glossed "comfort" appearing in a context that is grammatically refusal, carrying a meaning closer to "resignation" | Informs Session B Pass 1 meaning analysis |
| A verse appearing to connect two registries through a shared theological mechanism | A verse where H5162 *na.cham* functions as the pivot between divine anger and compassion — linking repentance and mercy | Cross-registry connections surface here before any correlation signal fires |
| An unexpected set-aside reason that reveals something analytically significant | A `wrong_face` set-aside where the inner-being content clearly belongs to a different registry — identifying which registry and why is itself a finding | Enables vertical pass discovery; feeds Session D |
| A term whose classification raises a question about the inner-being model itself | H3820A *lev* operating simultaneously as cognition and volition — challenging the dimension system's separability | These generate new dimension proposals or Session D structural questions |

---

### 6.2 What Dimension Review produces as analytical findings

Dimension Review is also primarily a classification phase, but group reading surfaces observations that belong in the analytical record beyond the dimension assignment. The Dimension Review instruction (Section 5.4) explicitly requires capturing these as Session B findings and Session D pointers.

**What to look for and record during Dimension Review:**

| Signal | Example | Why it matters |
|--------|---------|---------------|
| An anchor verse revealing inner-being content absent from the group description | An anchor verse encoding a conditional structure (covenant obedience → divine favour) not named in the group description | May be significant for multiple registries; a Session B finding now, a Session D question later |
| Cross-group pattern within a cluster | Three C17 registries showing GOD-dominant groups in Relational Disposition — the consistency of the divine-initiative pattern | This pattern is exactly what Session D investigates |
| Convergence or divergence between registries on the same inner-being state | Two registries appearing to share deep compassion but assigned to different dimensions — this divergence is a finding about the dimension system's adequacy | Session D needs to know where the vocabulary breaks down |
| Root family connection revealed by the root family extract | H7355 *racham* and H7358 *rechem* sharing the womb-root across Compassion and Love | Root-level connections are a dedicated Session D signal |
| A dimension appearing in an unexpected cluster | A Transformation group appearing in a cluster dominated by Relational Disposition — the tension is analytically significant | Productive Session D question |
| A group fitting no existing dimension | A group describing "inner stillness preceding divine receptivity" — not Emotion, Cognition, Volition, or Relational Disposition | Vocabulary gaps are findings about the programme's emergent framework |
| A property-term group serving different characteristics across the cluster | H8085 *sha.ma* appearing in heart-obedience in one group and cognitive reception in another | Session B Pass 1 finding about term behaviour |

---

### 6.3 Session B review obligation — findings from prior phases

When Session B begins for a registry, all analytical findings already in `wa_session_b_findings` for that registry — raised during Verse Context and Dimension Review — must be reviewed. This is not a light pass. Session B has the full analytical data that earlier phases did not have: the complete extract, sense structures, verse texts, somatic evidence, and correlation signals. Earlier findings were raised with partial data; Session B reads the full picture.

**For each prior-phase finding, Session B must do one of the following:**

| Disposition | When to apply | What happens in the database |
|-------------|--------------|------------------------------|
| **Confirm and close** | The finding is supported by the Session B data. No correction needed. | Update `delete_flag = 0`; write confirmation note to `obsolete_reason` field is not appropriate here — a dedicated `resolution_note` field is needed (see gap G-14 below). Mark `pass_ref` with the confirming pass. |
| **Correct and supersede** | The finding is partially right but the full data shows a more precise or different observation. | Write a new finding with the corrected content. Set `delete_flag = 1` on the original; set `superseded_by_id` pointing to the new finding. The original is retained for audit. |
| **Deepen and link** | The finding is correct as far as it goes, but Session B can add substance to it. | Write a new, deeper finding. Link via `related_finding_id` to the original. The original is not obsoleted — both stand, with the newer one building on the earlier. |
| **Convert to SD_POINTER and close** | The finding cannot be resolved within this registry's data — it requires cross-word analysis. | Write a new `SD_POINTER` flag to `wa_session_research_flags`. Set `delete_flag = 1` on the original finding; set `obsolete_reason = 'Converted to SD_POINTER [label]'`. The pointer carries the full analytical question. |
| **Set aside — insufficient evidence** | Research conducted in Session B finds no supporting evidence for the observation. The finding cannot be substantiated. | Apply the thin evidence protocol (Section 10). Do not simply delete. Mark `delete_flag = 1`; write the research outcome to `obsolete_reason`. |

**The closure rule:** No prior-phase finding for this registry may remain in an open, unreviewed state at Session B close. Every finding must have a visible disposition recorded in the database before `session_b_status` advances to Analysis Complete. An unreviewed prior-phase finding at session close is a programme integrity failure.

**The conversion rule:** The only path from an open analytical finding to Session D is conversion to an SD_POINTER. A finding does not carry forward to Session D as a finding. If it requires cross-word data, it becomes a pointer. If it does not, it is resolved within Session B.

---

### 6.4 What Session C produces as analytical findings

Session C generates prose. The constraint is absolute: **Session C prose must not contain any analytical claim that does not have a corresponding finding in `wa_session_b_findings` for this registry, with `delete_flag = 0`.** If Session C cannot point to a finding that supports a claim, that claim may not appear in the prose.

However, the process of writing prose is itself analytical. Two things can happen during Session C that generate new findings:

1. **A new observation emerges** — the act of articulating the word study reveals a connection, a pattern, or a characterisation that was not recorded as a finding. This is not prohibited — it is valuable. But it must be handled correctly: stop, write the finding to `wa_session_b_findings`, confirm it against the extract data, and then write the prose that depends on it. The finding must precede the prose, not follow from it.

2. **An existing finding is improved** — writing reveals that a finding's phrasing is imprecise, its scope is too narrow, or its evidence base needs clarifying. Write a new corrected finding; supersede the original via `superseded_by_id`. Then write the prose from the corrected finding.

In both cases, Session C is not a source of unreferenced observations. It is a source of findings that must be databased before the prose that depends on them is finalised.

---

### 6.5 What must be recorded for every analytical finding?

| Data point | Notes |
|-----------|-------|
| Finding text | Substantive analytical content — free prose |
| Finding type | What kind of finding — controlled vocabulary in Section 6.6 |
| Registry | Which word |
| Phase and pass | "Verse Context VCB-031", "Dimension Review Phase C C17", "Session B Pass 1", "Session C" |
| Entity links | Which specific entities — linked via `wa_finding_entity_links` |
| Rendering target | Which section of the word study or brief — `study_segment` controlled vocabulary in Section 13 |
| Instruction version | Under which instruction |
| Date | When raised |
| Resolution state | `delete_flag` 0/1; `obsolete_reason` if set aside; `superseded_by_id` if replaced |
| Thin flag | Whether this finding is supported by thin evidence — see Section 10 |
| Resolution link | `related_finding_id` — link to the pointer it resolves, or the finding it supersedes or builds on |

---

### 6.6 Finding type controlled vocabulary

| Type | Produced by | Example |
|------|------------|---------|
| `MEANING_OBSERVATION` | Session B Pass 1 | Sense structure, semantic range, boundary condition |
| `VERSE_PATTERN` | Session B Pass 3, Verse Context | A pattern visible across a verse group or individual verse |
| `VERSE_ANNOTATION` | Session B Pass 3 | Per-anchor-verse 3–6 sentence analytical annotation |
| `THEOLOGICAL_NOTE` | Session B Pass 2 | Divine involvement pattern, eschatological dimension |
| `SOMATIC_EVIDENCE` | Session B Pass 4 | Body-part vocabulary, somatic classification |
| `SPIRIT_SOUL_BODY` | Session B Pass 4 | Provisional spirit-soul-body classification with reasoning |
| `ETYMOLOGY` | Session B | Root etymology or historical semantic observation |
| `ROOT_FINDING` | Session B Pass 1, Dimension Review | Observation about a root family — scope, etymology, cross-registry significance |
| `DIMENSION_REVIEW` | Dimension Review | Group quality assessment, dimension discernment, cluster pattern |
| `GROUP_INTEGRITY` | Dimension Review, Verse Context | Group structural concern — anchor quality, verse assignment issue |
| `CROSS_REGISTRY` | All phases | Observation about a relationship between two registries — not yet a full SD_POINTER |
| `TERM_BEHAVIOUR` | Verse Context, Session B | Observation about how a specific term behaves in its corpus |
| `SESSION_C_CORRECTION` | Session B Stage 3, Session C | A word study statement that must be corrected, deepened, or reopened |
| `OPEN_ITEM` | Any phase | A question unresolvable from current data — candidate for SD_POINTER conversion |

---

### 6.7 Where is it recorded?

**`wa_session_b_findings`** — receives analytical findings from all four phases.

Current field coverage:

| Data need | Field | Readiness |
|-----------|-------|-----------|
| Finding text | `finding` | Present |
| Finding type | `finding_type` | Present — naming inconsistent (see G-6) |
| Registry | `registry_id` FK | Present |
| Phase and pass | Partially in `session_b_instruction` | Partial — instruction version only; phase and pass number absent |
| Entity links | Not present | **Missing** |
| Rendering target | Not present | **Missing** |
| Instruction version | `session_b_instruction` | Present |
| Date | `raised_date` | Present |
| Resolution state | Not present | **Missing** |
| Thin flag | Not present | **Missing** |
| Resolution link | Not present | **Missing** |

### Missing fields on `wa_session_b_findings`

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `pass_ref` | TEXT | NULL | Phase and pass attribution |
| `study_segment` | TEXT | NULL | Rendering-target declaration per Section 13 |
| `delete_flag` | INTEGER | 0 | 0 = active; 1 = set aside or superseded |
| `obsolete_reason` | TEXT | NULL | Required when `delete_flag` = 1. Must record the outcome of investigation for thin or set-aside findings |
| `obsolete_date` | TEXT | NULL | Date marked obsolete |
| `superseded_by_id` | INTEGER | NULL | FK to this table's `id` — self-referential |
| `related_finding_id` | INTEGER | NULL | Link to: the pointer this finding resolves; the prior finding this supersedes; or a related finding this builds on |
| `resolution_note` | TEXT | NULL | For confirmed or deepened findings: brief note of the Session B review outcome. Distinct from `obsolete_reason` (which covers set-aside cases) |
| `thin_evidence` | INTEGER | 0 | 1 = this finding is supported by thin evidence and requires investigation before it can be confirmed or set aside — see Section 10 |

---

## 7. Entity Types

An analytical finding is about one or more of six entity types. The entity type determines which table `entity_id` in `wa_finding_entity_links` points into.

| Entity type | `entity_type` value | Points to table | Notes |
|------------|---------------------|----------------|-------|
| **Term** | `term` | `wa_term_inventory.id` | Most granular — a finding about a specific Strong's number in a specific registry |
| **Verse** | `verse` | `verse_context.id` | A finding about a specific verse as it appears in this term's corpus |
| **Group** | `group` | `verse_context_group.id` | A finding about a contextual meaning group |
| **Dimension** | `dimension` | `wa_dimension_index.id` | A finding about a dimension assignment |
| **Root family** | `root_family` | `wa_term_root_family.id` | First-class entity per researcher direction (2026-04-13). No new table needed — links to existing table |
| **Cross-registry** | `cross_registry` | `wa_session_research_flags.id` | A finding about a cross-registry relationship; also how Session D resolution writes back |

**Registry-level findings** use `entity_type = registry` pointing to `word_registry.id`. The `registry_id` field on `wa_session_b_findings` already captures this; an entity link row is optional but provides consistency.

**Multi-entity findings.** A finding about the Compassion↔Mercy connection through the ELE root writes one row in `wa_session_b_findings` and two rows in `wa_finding_entity_links` — one with `entity_type = root_family` (ELE root) and one with `entity_type = cross_registry` (the SD_POINTER naming the Compassion↔Mercy connection). Both link rows carry the same `finding_id`.

### Root family entity — current schema state

Root families exist in `wa_term_root_family` (2,861 rows, 22% gap from pre-backfill era). Each row has a stable `id`. Root-level findings link via `entity_type = root_family` pointing to this table. No new table is needed. The 22% gap means some root-level findings will reference root records that do not yet exist — a CC directive must create the root record before the finding link can be inserted (gap G-13).

### Cross-registry entity — current schema state

Cross-registry relationships are held in `wa_session_research_flags` (SD_POINTER rows, active and growing) and in `wa_cross_registry_links` (Session A–era, 158 rows, being superseded). For findings about cross-registry relationships, `entity_type = cross_registry` points to `wa_session_research_flags.id` as the primary target. The v1.0 proposal to promote xrefs to a dedicated first-class table is deferred.

**New junction table: `wa_finding_entity_links`**

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER PK | Stable identifier |
| `finding_id` | INTEGER FK | References `wa_session_b_findings.id` |
| `entity_type` | TEXT NOT NULL | Controlled: term / verse / group / dimension / registry / root_family / cross_registry |
| `entity_id` | INTEGER | The id of the entity in its table. Polymorphic — FK integrity enforced by Claude Code at write time |
| `entity_strongs` | TEXT nullable | Denormalised Strong's number for term links |
| `raised_date` | TEXT | Date this link was created |

---

## 8. OT-5 — Verse Annotation

### When is there a need?

Session B Pass 3 produces a structured annotation for every anchor verse — a 3–6 sentence analytical comment that names what the verse contributes that a plain summary cannot carry. Pass 3 is also explicitly identified in the Session B instruction as the primary pass for cross-registry observation.

### What must be recorded?

| Data point | Notes |
|-----------|-------|
| Verse and term | Which verse, which Strong's |
| Group | Which verse context group |
| Registry | Which word |
| Annotation text | 3–6 sentence analytical comment |
| Anchor type | anchor or supplementary |
| Session C flag | confirm / correct / deepen / add |
| Cross-registry observation | If the annotation surfaces a cross-registry connection — link to a new SD_POINTER |

### Where is it recorded?

Verse annotations are **not stored in the database**. They exist only in the Session B observations log markdown. Three options:

| Option | Description | Consequence |
|--------|-------------|-------------|
| **A — OT-4 finding** | Write each annotation as a finding in `wa_session_b_findings` with `finding_type = VERSE_ANNOTATION` and entity links to verse and group | Fully consistent; queryable; Session C can retrieve all annotations for a registry in a single query |
| **B — Field on verse_context** | Add `annotation_text` to `verse_context` | Simpler; conflates classification record with analytical content |
| **C — Defer** | Annotations remain in markdown; Session C works from the markdown log | Simplest operationally; not queryable or reusable |

**Researcher decision needed.** Option A is the most consistent with the programme's data architecture.

### What is unclear?

The Session B instruction requires tagging each anchor verse record with `VERSE_ANNOTATION_COMPLETE` when all anchors are annotated. No such flag type exists in `phase2_flag_types` and no mechanism on `verse_context` supports it. This step has no database implementation.

---

## 9. OT-6 — Forward Pointer (Session D)

### When is there a need?

Session D pointers are raised continuously throughout all phases. The Session B instruction (SB-11) is explicit: pointers must be raised at the moment of discovery during any pass. The Dimension Review instruction (Section 5.4) requires the same during Phase C.

An SD_POINTER says: when investigating this question at Session D, look at the connection between registry X and registry Y through this specific evidence. It is a structural observation and a question — not a conclusion. **It is the only channel through which an open analytical question may carry forward past Session B to Session D.** Findings that remain open at Session B close must either be resolved within the word's data, or converted to SD_POINTERs and closed as findings.

The distinction between an OT-4 finding and an OT-6 pointer:
- OT-4: an observation grounded in this registry's data — what it reveals about this word
- OT-6: an observation requiring cross-registry data to resolve — what it raises as a question for Session D

### What must be recorded?

Per `wa_session_research_flags` SD_POINTER field specification:

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

**`wa_session_research_flags`** — correct and well-designed home. All required fields present.

### What is missing?

No structural gaps. Two data quality issues:

1. `flag_code` naming duplication: `PH2_VOLUME_LIMITATION` (33 rows) and `VOLUME_LIMITATION` (19 rows). Consolidate to `PH2_VOLUME_LIMITATION`.
2. `session_raised` format: 34 distinct formats. Enforce going forward: `[instruction-version] [phase] [pass-ref]`.

### What is unclear?

When Session D resolves a pointer, it marks `resolved = 1` and writes `resolved_note`. The resolution should also produce an OT-4 finding in `wa_session_b_findings`. The structural link from the resolution note (free text) to the finding that produced it does not yet exist. Flagged for Session D instruction design.

---

## 10. Thin Evidence Protocol

### What is thin evidence?

A finding is supported by thin evidence when:
- It is based on one or two verses rather than a pattern across the corpus
- It is plausible from the reading but not directly stated in the verse text
- It involves an inferential step not supported by lexical data
- The term's verse count is too low to establish the observation as representative

Thin evidence does not make a finding wrong. It makes it provisional. The finding must be flagged, researched, and brought to a resolution before the registry can close.

### What the thin evidence flag is not

Thin evidence is not a reason to skip recording a finding. An observation that surfaces during verse reading, group review, or dimension assignment — even if only one verse supports it — must be recorded. The flag marks it as requiring investigation, not as ready to discard.

### The resolution requirement

Every finding with `thin_evidence = 1` must be brought to one of the following outcomes before Session B closes for this registry:

| Outcome | Condition | Database action |
|---------|-----------|-----------------|
| **Confirmed** | Further research across the corpus finds additional supporting evidence | Set `thin_evidence = 0`; write confirmation to `resolution_note` with the specific supporting verses or data |
| **Deepened** | Further research clarifies the scope of the observation, making it more precise rather than broader | Write a corrected finding; supersede the original via `superseded_by_id`; write deepening note |
| **Converted to pointer** | The evidence is insufficient within this registry but the observation is analytically significant enough to warrant cross-registry investigation | Convert to SD_POINTER in `wa_session_research_flags`; set `delete_flag = 1` on the finding; write `obsolete_reason = 'Thin evidence; converted to SD_POINTER [label] for cross-registry investigation'` |
| **Set aside** | Research finds no supporting evidence. The finding cannot be substantiated in any direction. | Set `delete_flag = 1`; write `obsolete_reason` recording: what was investigated, what was found, and why the finding is being set aside. The row is retained for audit. **A finding may not be set aside without this investigation record.** |

### The prohibition on unresearched set-aside

An observation may not be set aside simply because its initial evidence is thin. Thin evidence is a trigger for research, not a disposal pathway. If a finding is set aside, the `obsolete_reason` must include:
- What data was examined in the investigation
- What the investigation found
- Why the finding does not survive that examination

An `obsolete_reason` that reads only "insufficient evidence" or "not supported" without naming what was investigated and what it showed is insufficient. This is a programme integrity requirement.

### Data quality flags and thin evidence

The thin evidence concept applies specifically to analytical findings (OT-4). It is distinct from data quality flags (OT-7), which concern the correctness of data in the database, not the strength of analytical observations derived from that data. Data quality flags have their own resolution protocol — see Section 11.

---

## 11. OT-7 — Data Quality Flag

### When is there a need?

Data quality issues surface during Verse Context processing and Session B Stage 1 data audit: incorrect field values, homonym contamination, extraction anomalies, missing root family records, volume limitations, terms requiring splitting.

### Resolution requirement

**All data quality flags targeting Session B must be resolved before Session B is complete.** An open data quality flag with `session_target = B` at session close is a programme integrity failure equivalent to an unresolved Stage 1 audit item. It is not acceptable to advance a registry to Analysis Complete while a known data error remains unaddressed.

Flags with `session_target = D` are carried forward to Session D — they are acknowledged and explicitly deferred, not ignored. The deferral must be recorded: the `resolved_note` field should carry a brief statement of why the flag is deferred and what Session D is expected to do with it.

**Resolution must be recorded in the database:**

| Resolution type | Database action |
|-----------------|-----------------|
| Issue corrected by patch | `resolved = 1`; `resolved_date`; `resolved_note` stating what was corrected and which patch applied it |
| Issue investigated — no error found | `resolved = 1`; `resolved_date`; `resolved_note` stating what was examined and why no correction was needed |
| Issue confirmed but deferred to Session D | `resolved = 0`; `resolved_note` stating the deferred status and the reason |
| Issue converted to a finding (e.g. a data error that reveals an analytical question) | `resolved = 1`; `resolved_note` pointing to the `wa_session_b_findings` id of the resulting finding |

### What must be recorded?

| Data point | Field |
|-----------|-------|
| Flag code | `flag_code` |
| Registry and term | `registry_id`, `strongs_reference` |
| Priority | `priority` |
| Session target | `session_target` |
| Description | `description` |
| Date raised | `raised_date` |
| Resolved | `resolved` |
| Resolution date | `resolved_date` |
| Resolution note | `resolved_note` |

### Where is it recorded?

**`wa_session_research_flags`** — non-SD_POINTER rows. All required fields present. No structural changes needed.

---

## 12. OT-8 — Session C Correction

### When is there a need?

Session B Stage 3 reviews the word study against the completed analysis. Where a word study statement is factually incorrect, incomplete, or contradicted by data, it must be flagged and corrected. Where a statement prematurely treated an SD_POINTER as settled, it must be reopened.

### The Session C prose constraint

Session C prose must derive entirely from findings in `wa_session_b_findings` for this registry with `delete_flag = 0`. No claim may appear in the prose that does not have a corresponding active finding. This constraint is not a stylistic preference — it is the programme's mechanism for ensuring that the published word study is substantiated by analytical work, not by the act of writing.

### What Session C may produce

Session C is an analytical act as well as a prose act. Writing well requires understanding deeply, and understanding can surface observations that analysis did not name. When this happens:

1. Stop writing at the point the new observation arises
2. Write the finding to `wa_session_b_findings` with the correct `finding_type`, `pass_ref = 'Session C'`, and `study_segment`
3. Verify the finding against the extract data
4. If the finding is supported — continue writing prose that depends on it
5. If the finding is thin — apply the thin evidence protocol (Section 10) before proceeding
6. If the finding cannot be verified from the extract — do not write the prose. The observation becomes a candidate for OT-6 conversion

### What must be recorded?

Session C corrections are a subset of OT-4 findings using `finding_type = SESSION_C_CORRECTION`. The fields that make correction findings queryable are `study_segment` (which section) and `related_finding_id` (which prior finding or pointer this corrects). No separate table is needed.

---

## 13. Implementation Plan

### Step 1 — Data quality cleanup (CC directive, no schema migration)

| Action | Table | Rows affected |
|--------|-------|--------------|
| Normalise `finding_type` to UPPER_SNAKE_CASE | `wa_session_b_findings` | All 171. Map: `theological_note` → `THEOLOGICAL_NOTE`, `verse_pattern` → `VERSE_PATTERN`, `term_behaviour` → `TERM_BEHAVIOUR`, `etymology` → `ETYMOLOGY`. Confirm `C22` with researcher before executing. |
| Consolidate `flag_code` | `wa_session_research_flags` | 19 rows — `VOLUME_LIMITATION` → `PH2_VOLUME_LIMITATION` |

### Step 2 — Add fields to existing tables (schema migration, minor)

**On `wa_session_b_findings`** — nine additional fields:

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `pass_ref` | TEXT | NULL | Phase and pass attribution |
| `study_segment` | TEXT | NULL | Rendering-target declaration |
| `delete_flag` | INTEGER | 0 | 0 = active; 1 = set aside or superseded |
| `obsolete_reason` | TEXT | NULL | Required when `delete_flag` = 1; must include investigation record for thin/set-aside findings |
| `obsolete_date` | TEXT | NULL | Date marked obsolete |
| `superseded_by_id` | INTEGER | NULL | FK to this table's `id` — self-referential |
| `related_finding_id` | INTEGER | NULL | Link to resolved pointer, superseded finding, or finding this builds on |
| `resolution_note` | TEXT | NULL | For confirmed or deepened findings: Session B review outcome |
| `thin_evidence` | INTEGER | 0 | 1 = thin evidence; must be investigated and resolved before session close |

**On `verse_context`:**

| Field | Type | Default |
|-------|------|---------|
| `classified_by_instruction` | TEXT | NULL |
| `classified_date` | TEXT | NULL |

**On `verse_context_group`:**

| Field | Type | Default |
|-------|------|---------|
| `classified_by_instruction` | TEXT | NULL |

**On `wa_dimension_index`:**

| Field | Type | Default |
|-------|------|---------|
| `dim_review_instruction` | TEXT | NULL |

### Step 3 — Create new table (schema migration)

Create `wa_finding_entity_links` as specified in Section 7. Add indexes on `finding_id` and on `(entity_type, entity_id)`.

### Step 4 — Verify write path

Test a complete finding lifecycle: insert with entity links → confirm via query → apply thin evidence flag → confirm resolution process → apply supersession. Verify all links resolve correctly.

### Step 5 — Activate write protocols

Update Session B, Dimension Review, and Verse Context instructions to state:
- All OT-4 findings written to `wa_session_b_findings` at pass close with `pass_ref`, `study_segment`, and entity links populated
- Prior-phase findings reviewed and dispositioned at Session B start
- Thin evidence findings flagged at creation and resolved before session close
- Data quality flags (`session_target = B`) resolved before session close
- Session C prose verified against active findings; new findings written back before prose that depends on them is finalised

### Researcher decisions required before Step 2

1. **Verse annotations (OT-5):** Option A (OT-4 finding), Option B (field on `verse_context`), or Option C (defer)?
2. **`wa_session_b_dimensions` table:** Retire or retain?
3. **`wrong_face` target registry FK:** Formal link in schema or notes field sufficient?
4. **`finding_type` for "C22" row:** Confirm normalisation target before Step 1 executes.

---

## 14. `study_segment` Controlled Vocabulary

### Word study sections (reader-facing)

| Value | Maps to |
|-------|---------|
| `word_study_s1_characteristic` | Section 1: The Characteristic |
| `word_study_s2_how_it_works` | Section 2: How It Works |
| `word_study_s3_verses` | Section 3: The Verses |
| `word_study_s4_vocabulary` | Section 4: The Vocabulary |
| `word_study_s4_[root_code]` | Section 4 sub-segment per root family |
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
| `unassigned` | Temporary — not yet allocated to a segment |
| `cross_segment` | Applies to multiple sections |

---

## 15. Gap Summary

| # | Gap | Severity | Table | Resolution |
|---|-----|----------|-------|------------|
| G-1 | No attribution fields on `verse_context` | Low | OT-1 | Add `classified_by_instruction`, `classified_date` |
| G-2 | No attribution field on `verse_context_group` | Low | OT-2 | Add `classified_by_instruction` |
| G-3 | No instruction version field at row level on `wa_dimension_index` | Low | OT-3 | Add `dim_review_instruction` |
| G-4 | `wa_session_b_findings` missing 9 fields | **High** | OT-4, OT-8 | Add fields per Section 13 Step 2 |
| G-5 | No entity-level linkage from findings to terms/verses/groups/dimensions/roots/cross-registry | **High** | OT-4 | New table `wa_finding_entity_links` |
| G-6 | `finding_type` naming inconsistency | Medium | OT-4 | Normalise per Section 13 Step 1 |
| G-7 | Verse annotations have no database home | Medium | OT-5 | Researcher decision needed |
| G-8 | `VERSE_ANNOTATION_COMPLETE` flag has no database implementation | Low | OT-5 | Depends on G-7 decision |
| G-9 | `flag_code` naming duplication (VOLUME_LIMITATION variants) | Low | OT-6/7 | Consolidate per Section 13 Step 1 |
| G-10 | `strongs_reference` multi-value entries (7 rows) | Low | OT-6/7 | Review and split at query time |
| G-11 | `session_raised` format inconsistency | Low | OT-6/7 | Enforce standard format going forward |
| G-12 | No FK from resolved pointer to resolving finding | Low | OT-6 | Deferred to Session D instruction design |
| G-13 | Root family records missing for ~22% of root-coded terms | Medium | OT-4 (root) | CC directive to fill gaps before root entity links are activated |
| G-14 | No `resolution_note` field on `wa_session_b_findings` for confirmed/deepened findings | **High** | OT-4 | Added to Step 2 field list — resolves this gap |

---

*Produced under GR-OBS-002, GR-OBS-005, GR-OBS-006, GR-PASS-002. For researcher review before implementation begins.*
