# wa-reference-v5_7-20260420

> Framework B Soul Word Analysis Programme — Reference Guide
> Version: v5_7 | Date: 20260420 | Schema: v3.11.0
> Supersedes: wa-reference-v5_6-20260418.md
> Governed by: wa-global-general-rules-v2_11-20260418.json
> v5_7 changes: §8 rewritten for evidence-flag redesign (M29); §10 reframed (evidential_status repurposed as research need/outcome tracker); new §8a (research-action route vocabulary), §8b (Q-COV catalogue questions), §9.4 (term_introduction_source vocabulary)

---

## Document scope (GR-REF-001 Discipline 5)

This document is the authoritative source for:
- Controlled vocabulary — all enumerated value sets used in the programme
- Database schema — table structures, column definitions, field-authority rules
- File naming conventions — programme-specific application of GR-FILE rules
- Anchor verse definition, XREF architecture, and related programme-wide concepts

This document is NOT the authority for (pointers, not copies):
- Patch format → `wa-patch-instruction-v2_0-20260418.md`
- Directive format → `wa-directive-instruction-v1_0-20260418.md`
- CC operational routines → `wa-claudecode-instruction-v4_0-20260418.md`
- Programme-wide binding rules → `wa-global-general-rules-v2_11-20260418.json`
- Open issues and flags → `wa-global-flags-v1_2-20260418.md`

Per GR-REF-001 Discipline 1 (pointer not copy): content owned by those documents is not re-stated here.

---

## Change Control — v5_6

| Change | Section |
|---|---|
| Scope statement added per GR-REF-001 Discipline 5 | New "Document scope" above |
| §1 File Naming Conventions — brought into compliance with GR-FILE-001/003/007/009. Version component restored; lowercase filenames throughout; patch_id vs filename distinction added | §1 |
| §1.3 Instruction document pattern list updated — replaces stale .docx patterns, capital-WA filenames with current lowercase conventions; retired instruction references removed | §1.3 |
| §1.4 Patch ID distinguished from patch filename — patch_id retains uppercase for applicator compatibility, filename is lowercase | §1.4 |
| §12 Patch Index — governing document references updated to current instructions (wa-patch-instruction v2_0, wa-directive-instruction v1_0) | §12 |
| §13.2 and §13.3 — GR-DATA-001 active-terms filter and GR-DATA-003 mti_term_flags authority absorbed from global rules addendum ADD-REF-001/002 | §13.2, §13.3 |
| §14 post-patch output structures — pointer to wa-patch-instruction §8 (templates no longer inlined) | §14 |
| §18 Document Preparation and Validation Standard retained; sub-section 18.5 Failure and Recovery updated to point to wa-patch-instruction §9 and §10 | §18 |
| Footer updated | — |

Scope reminder (GR-REF-001 Discipline 5): sections that previously drifted into operational-instruction content (e.g. procedural how-to for CC) have been replaced with pointers to the appropriate instruction document.

---

## 1. File Naming Conventions — CANONICAL SOURCE: DB `wa_file_name_pattern` (M35 2026-04-20)

File naming is governed by GR-FILE-001 through GR-FILE-009 in the global rules (now also DB-sourced: `wa_rule_registry` category=`file_naming`). **Authoritative pattern catalogue lives in DB table `wa_file_name_pattern`** — consume via reference snapshot `data/exports/reference/wa-reference-snapshot-{YYYYMMDD}.json`. Inline tables below mirror DB contents for readability; in any divergence, the DB wins.

### 1.1 Word-Level Files

Pattern: `wa-{nnn}-{word}-{scope}-v{n}-{YYYYMMDD}.{ext}`

Where `{nnn}` is the zero-padded registry number, `{word}` is lowercase English word, `{scope}` is one of the tokens below, `{n}` is version (minor increment for updates, major for rewrites — see GR-FILE-003), `{YYYYMMDD}` is compact date per GR-FILE-009.

| Scope token | File type | Example |
|---|---|---|
| analysis | Session B narrative (docx) | `wa-097-joy-analysis-v1-20260327.docx` |
| extract | Word JSON export from database | `wa-097-joy-extract-v1-20260327.json` |
| json | Session B structured JSON | `wa-097-joy-json-v1-20260327.json` |
| patch | Patch file for Claude Code (see §12 and wa-patch-instruction) | `wa-097-joy-patch-sessionb-v1-20260327.json` |
| final | Final cross-table registry extract (post-patch) | `wa-097-joy-final-v1-20260327.json` |
| sdpointers | Session D pointers file (post-patch) | `wa-097-joy-sdpointers-v1-20260327.json` |
| obslog | Observations log for the session | `wa-097-joy-obslog-v1-20260327.md` |

Post-patch `final` and `sdpointers` files are produced only after the analysis completion patch is applied and confirmed — see wa-patch-instruction §8.

### 1.2 Verse Context Batch Files

Pattern: `wa-vcb{nnn}-{scope}-v{n}-{YYYYMMDD}.{ext}`

| Scope token | File type |
|---|---|
| extract | Verse Context batch JSON input |
| patch | Verse Context batch patch output (see wa-patch-instruction §7.3) |

### 1.3 Programme-Level Files

| Pattern | File type |
|---|---|
| `wa-clusters-v{n}-{YYYYMMDD}.json` | Clustering run output |
| `wa-{cluster}-sessiond-v{n}-{YYYYMMDD}.json` | Session D discovery JSON |
| `wa-programme-review-v{n}-{YYYYMMDD}.docx` | Periodic registry review |
| `wa-global-general-rules-v{n}-{YYYYMMDD}.json` | Global rules |
| `wa-global-flags-v{n}-{YYYYMMDD}.md` | Global flags |
| `wa-global-{task}-obslog-v{n}-{YYYYMMDD}.md` | Cross-cutting obs log |

### 1.4 Instruction Documents

| Pattern | Document |
|---|---|
| `wa-reference-v{n}-{YYYYMMDD}.md` | This document |
| `wa-patch-instruction-v{n}-{YYYYMMDD}.md` | Patch preparation and execution |
| `wa-directive-instruction-v{n}-{YYYYMMDD}.md` | Directive preparation and execution |
| `wa-claudecode-instruction-v{n}-{YYYYMMDD}.md` | Claude Code operating guide |
| `wa-versecontext-instruction-v{n}-{YYYYMMDD}.md` | Verse Context stage |
| `wa-dimensionreview-instruction-v{n}-{YYYYMMDD}.md` | Dimension Review stage |
| `wa-sessionb-analysis-readiness-v{n}-{YYYYMMDD}.md` | Session B analysis-readiness (when finalised) |
| `wa-sessionb-analysis-output-v{n}-{YYYYMMDD}.md` | Session B analysis-output (when finalised) |
| `wa-sessionc-instruction-v{n}-{YYYYMMDD}.md` | Session C (when finalised — see FLAG-001) |
| `wa-sessiond-orientation-v{n}-{YYYYMMDD}.md` | Session D orientation |
| `wa-registry-management-guide-v{n}-{YYYYMMDD}.md` | Registry management |

### 1.5 Patch ID vs Patch Filename — two distinct identifiers

The patch format carries an internal `patch_id` field used by the applicator for idempotency. This is distinct from the patch filename on disk.

| Identifier | Format | Purpose | Location |
|---|---|---|---|
| Patch filename | `wa-{nnn}-{word}-patch-{type}-v{n}-{YYYYMMDD}.json` (fully lowercase per GR-FILE-007) | Human-readable file on disk | Filesystem |
| `patch_id` (internal) | `PATCH-{YYYYMMDD}-{registry_no}-{TYPE}-V{n}` (uppercase retained) | Applicator idempotency key | `_patch_meta.patch_id` inside the JSON |

The uppercase `patch_id` is a historical applicator convention and is not changed by GR-FILE-007 (which governs filenames, not internal field values). Full patch naming rules are in wa-patch-instruction §2.

---

## 2. Controlled Vocabulary — `mti_terms.status`

Source: bible_research.db schema v3.8.0. Use exact values, exact case.

| Value | When to use |
|---|---|
| NULL | Unclassified — no decision made yet |
| extracted | Term is genuine vocabulary for this registry — include in analysis |
| extracted_thin | Relevant but data is thin — include with caution note |
| extracted_theological_anchor | Primary theological anchor for this registry |
| delete | Confirmed bleed, peripheral, or non-registry vocabulary |
| candidate_delete | Likely bleed, not yet confirmed — flag for researcher decision |
| excluded | Excluded from programme scope — not the same as delete |
| xref_{word} | Belongs primarily to another registry (e.g. xref_anger, xref_shame) |
| phase2_enrichment | Needs deeper research before classification |

---

## 3. Controlled Vocabulary — `word_registry.session_b_status`

| Value | Meaning |
|---|---|
| NULL | Phase 1 excluded or not yet started |
| Verse Context Reset | Prior Session B work superseded — registry must reprocess through Verse Context |
| Ready for Analysis | Verse Context complete, term inventory clean — ready for Session B DataPrep |
| Pre-Analysis Complete | Pre-analysis patch applied — term classifications in database |
| Analysis Complete | Session B narrative complete — analysis patch applied |
| Session B Complete | Full Session B cycle done — all outputs complete |

`Ready for Analysis` is reachable only after `verse_context_status = Complete`.

---

## 3a. Controlled Vocabulary — `word_registry.verse_context_status`

Tracks Verse Context completion independently of session_b_status. Set by Claude Code based on OWNER term completion.

| Value | Meaning |
|---|---|
| NULL | Phase 1 excluded or zero-term registry — outside Verse Context scope |
| In Progress | Verse Context work has begun or is pending for this registry |
| Complete | All OWNER terms with verses have verse_context records — DataPrep gate open |

---

## 4. Controlled Vocabulary — `word_registry` fields

### 4.1 phase1_status

Complete | Excluded | In Progress

### 4.2 source_list

High Confidence | Low Confidence / Inferred | Missing Inner Being Words | Programme Addition

### 4.3 dimensions — CANONICAL SOURCE: DB `wa_vocab_set.DIMENSION_LABEL` (M32 2026-04-20)

Column renamed from `source_category` in migration M17 (2026-03-29).

`dimensions` is a comma-delimited multi-value field. Derived from Dimension Review per `wa-dimensionreview-instruction [current]` (currently v3_3-20260418).

**Canonical vocabulary — DB-sourced.** The authoritative list of the 11 dimension labels lives in the DB (`wa_vocab_set` set_code = `DIMENSION_LABEL`, seeded via migration M32 on 2026-04-20). AI sessions should consume this via the reference snapshot (`data/exports/reference/wa-reference-snapshot-{YYYYMMDD}.json`), regenerated at session start by `scripts/build_reference_snapshot.py`. The table below mirrors the DB contents; in any divergence, the DB wins (CC validator `apply_session_patch.py::_canonical_dimensions()` enforces this on every patch apply):

| Code | Canonical label | Description (summary — full text in §7.7) |
|---|---|---|
| 01 | `01 — Emotion — Positive` | Inner states of pleasure, joy, delight, satisfaction |
| 02 | `02 — Emotion — Negative` | Inner states of pain, distress, grief, fear, anger, shame, anxiety |
| 03 | `03 — Cognition` | Inner acts of knowing, perceiving, remembering, understanding, discerning |
| 04 | `04 — Volition` | Inner acts of willing, purposing, choosing, desiring, deciding |
| 05 | `05 — Moral Character` | Stable inner qualities of moral nature — goodness, justice, integrity, purity, faithfulness |
| 06 | `06 — Relational Disposition` | Inner orientation toward another — love, compassion, favour, attachment, contempt, hatred |
| 07 | `07 — Vitality / Existence` | Animating life of the inner person — constitution, continuation, fragility, end |
| 08 | `08 — Transformation` | Inner change — renewal, healing, purification, formation, or degradation |
| 09 | `09 — Agency / Power` | Exercise of inner capacity — sovereignty, authority, strength, restraint, self-giving |
| 10 | `10 — Dependence / Creatureliness` | Inner posture of reliance — humility, dependence, trust, security |
| 11 | `11 — Divine-Human Correspondence` | Inner-being characteristics that operate across the God/human boundary |

**Format rules (enforced by `apply_session_patch.py::CANONICAL_DIMENSIONS`):**

- Two-digit zero-padded code prefix (`01`, `02`, ... `11`)
- Em-dash separator between code and name (U+2014, surrounded by single spaces)
- Em-dash separator within compound names (`Emotion — Positive`)
- Slash with surrounding single spaces (`Vitality / Existence`, `Agency / Power`, `Dependence / Creatureliness`)
- No-space hyphen for `Divine-Human`

Patches whose `set.dimension` value does not match this vocabulary are rejected by the pre-apply validator and the producing agent must redo (researcher direction 2026-04-20). Any extension to the vocabulary (e.g. a new Dimension 12) is a researcher decision via DimReview instruction §7.7 revision (DR-13).

**Legacy vocabulary** (Gen 0 — pre-numbering) and **interim Gen 1** (unnumbered current form) are both deprecated. One-off migration on 2026-04-20 converts all existing rows to the canonical form where mechanically possible; see `outputs/investigations/dimension-label-canonicalisation-plan-20260420.md`.

### 4.4 origin

original_list | programme_addition

### 4.5 Dimensional Weight Vocabulary

Used in the `dimensional_profile` block of the final registry extract (see §14 and wa-patch-instruction §8).

| Value | Meaning |
|---|---|
| PRIMARY | Dominant analytical focus of the registry |
| SECONDARY | Substantially present and analytically significant, but not primary |
| PERIPHERAL | Present but limited or incidental corpus engagement |

---

## 5. Controlled Vocabulary — `wa_session_research_flags`

### 5.1 flag_code — valid values

CANDIDATE_REGISTRY_WORD | PH2_BOUNDARY_QUESTION | PH2_CROSS_REF_ENRICHMENT | PH2_CROSS_REGISTRY_REQUIRED | PH2_DATA_ERROR | PH2_DATA_QUALITY | PH2_DATA_SPLIT_REQUIRED | PH2_ESCHATOLOGICAL_STUDY_REQUIRED | PH2_EXEGETICAL_STUDY_REQUIRED | PH2_THEOLOGICAL_DEPTH_REQUIRED | PH2_VOLUME_LIMITATION | VOLUME_LIMITATION | SB_FINDING | SB_DIMENSION | SB_INNER_BEING | SD_POINTER | SD_CLUSTER

See FLAG-007 in wa-global-flags — SB_FINDING, SB_DIMENSION, SB_INNER_BEING are being deprecated in favour of the dedicated tables wa_session_b_findings, wa_session_b_dimensions, and word_registry.sb_classification fields.

### 5.2 priority

HIGH | MEDIUM | LOW (default: MEDIUM)

### 5.3 session_target

B | C | D (default: D)

### 5.4 flag_label convention — CANONICAL SOURCE: DB `wa_label_pattern` (M35 2026-04-20)

`PH2-{registry_no}-{3-digit-sequence}` — e.g. `PH2-097-001`. Must be unique across all records.

Further label patterns (DIM-{nnn}-NNN finding labels, DIM-{nnn}-SD{NNN} pointer labels, group_code patterns, VCB batch ids, Q-COV catalogue codes, directive IDs, patch IDs, FLAG-{NNN}) are catalogued in DB table `wa_label_pattern` — see reference snapshot.

---

## 6. Controlled Vocabulary — `wa_term_phase2_flags.flag_code`

GOD_AS_SUBJECT | CAUSATIVE_OF_INNER_STATE | SOMATIC_INNER_LINK | BODY_INNER_EXPRESSION | NT_FACULTY_NAMING | GENERATION_RESOLUTION_PAIR | CROSS_PART_ROOT | THIN_DATA | SMALL_VERSE_SAMPLE | DUPLICATE_RESOLVED | NO_WORD_ANALYSIS | CONSOLIDATION_CANDIDATE | THEOLOGICAL_ANCHOR | SOMATIC_EXPRESSION | HIGH_FREQUENCY_ANCHOR | SEMANTIC_RANGE_BREADTH | MULTI_REGISTRY_ANCHOR | DIVINE_HUMAN_PARALLEL | ESCHATOLOGICAL_USAGE | WISDOM_LITERATURE_CONCENTRATION | METAPHOR_ROOT | RELATIONAL_DIRECTION | VOLITIONAL_COMPONENT | CROSS_TESTAMENT_SHIFT | ARAMAIC_FORM

---

## 7. Controlled Vocabulary — `wa_crosslink_type.type_code`

SHARED_TERM | SEMANTIC_OVERLAP | SHARED_ROOT | SHARED_VERSE | THEOLOGICAL | CO_OCCURRENCE | SEMANTIC_OPPOSITION | SISTER_REGISTRY | OVERLAPPING_DOMAIN | CAUSATIVE_CHAIN | THEMATIC_LINK

---

## 8. Controlled Vocabulary — `wa_data_quality_flags.flag_code`

Updated 2026-04-20 (M29 evidence-flag redesign). Flags are **informational only** — never used to gate analytical processing. Per GR-EVIDENCE-001/002/003 (to be ratified in global-general-rules v2.12): coverage information informs approach, not exclusion; absence of expected evidence is itself a research signal; every evidence flag declares research-action routes AND catalogue-question links (see §8a + §8b).

### 8.1 Evidence family (informational — triggers research routing)

| Code | Meaning |
|---|---|
| `VERSE_EVIDENCE_MINIMAL` | Minimal biblical evidence exists for this term in the extraction. Does NOT mean the term is irrelevant — triggers research investigation per research_actions. Linked to Q-COV-01..04. |
| `VERSE_EVIDENCE_CONCENTRATED` | Term has fewer than THIN_DATA_THRESHOLD (20) confirmed verse records. Merged semantic: absorbs prior THIN_DATA and SMALL_VERSE_SAMPLE codes. Informational — verse count does not indicate analytical value. Linked to Q-COV-05..07. |
| `VERSE_EVIDENCE_HIGH` | Term has ≥HIGH_FREQ_THRESHOLD (500) occurrences. Verse records are a structured subset per STEP pagination. Linked to Q-COV-08..10. |
| `VERSE_EVIDENCE_BREADTH_NOTE` | Term's active verse count is a subset of total occurrences. Recorded for awareness — does NOT gate synthesis. Lives on `wa_session_research_flags` not `wa_data_quality_flags`. Linked to Q-COV-11..12. |

### 8.2 Structural / diagnostic (unchanged by M29)

| Code | Meaning |
|---|---|
| `NO_WORD_ANALYSIS` | Meaning is NULL for this term — STEP returned no word analysis |
| `PROSE_ONLY_MEANING` | Meaning stored as single prose block (no structured sense numbering) |
| `SPAN_FILTER_APPLIED` | One or more verse records discarded by span filter during fetch |
| `SPAN_RESOLUTION_CONFLICT` | Queried Strong's not found in any verse span — manual STEP UI verification required |
| `CONCRETE_PHYSICAL` | Term denotes a concrete physical object (not an evidence flag) |

### 8.3 Deprecated (post M29)

| Code | Disposition |
|---|---|
| `NO_VERSES` | Renamed to `VERSE_EVIDENCE_MINIMAL` in M29 (2026-04-20) |
| `SMALL_VERSE_SAMPLE` | Renamed to `VERSE_EVIDENCE_CONCENTRATED` in M29; absorbs THIN_DATA |
| `THIN_DATA` | Merged into `VERSE_EVIDENCE_CONCENTRATED` in M29; flag_id=2 marked deprecated |
| `HIGH_FREQUENCY_ANCHOR` | Renamed to `VERSE_EVIDENCE_HIGH` in M29 |
| `PH2_VOLUME_LIMITATION` (research flag) | Renamed to `VERSE_EVIDENCE_BREADTH_NOTE` in M29 |

---

## 8a. Controlled Vocabulary — `wa_quality_flag_types.research_actions`

New column added in M29 (2026-04-20). Semicolon-separated list of route codes declaring what investigation a flag should trigger.

| Code | Route |
|---|---|
| `R_STEP_EXHAUST_CHECK` | Was the STEP search fully exhausted for this term? Re-run discovery with broader criteria. |
| `R_EXTERNAL_BIBLE` | Researcher-driven Bible research outside STEP (other translations, original-language lexica, concordances). |
| `R_AI_WIDER_CONTEXT` | AI explores term usage in wider historical/cultural/linguistic context (modern science, ANE literature, LXX/Targums, early Christian writings). |
| `R_RELEVANCE_REVIEW` | Re-evaluate whether the term is genuinely in scope for inner-being study. May result in registry deprecation, retention with rationale, or escalation. |

Current per-flag assignments:

| Flag | research_actions |
|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT |
| `VERSE_EVIDENCE_HIGH` | R_AI_WIDER_CONTEXT |
| `VERSE_EVIDENCE_BREADTH_NOTE` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT |

---

## 8b. Q-COV Catalogue Questions (evidence-flag-driven investigation)

12 questions added to `wa_obs_question_catalogue` (section `Evidence-Flag Research Questions`) on 2026-04-20 (patch `PATCH-20260420-CATALOGUE-QCOV-V1`). Linked to evidence flags via `wa_flag_type_question_link`. Surface into prose (Session A/B) when a flag is raised; AI-driven answers land as findings.

| Code | Links to flag | Purpose |
|---|---|---|
| Q-COV-01 | VERSE_EVIDENCE_MINIMAL | Alternative-term coverage check |
| Q-COV-02 | VERSE_EVIDENCE_MINIMAL | Modern neologism check |
| Q-COV-03 | VERSE_EVIDENCE_MINIMAL | Absence as analytical signal |
| Q-COV-04 | VERSE_EVIDENCE_MINIMAL | Inner-being relevance / deprecation decision |
| Q-COV-05 | VERSE_EVIDENCE_CONCENTRATED | STEP exhaustion check |
| Q-COV-06 | VERSE_EVIDENCE_CONCENTRATED | Close-reading of few verses |
| Q-COV-07 | VERSE_EVIDENCE_CONCENTRATED | Genre / period / speaker concentration |
| Q-COV-08 | VERSE_EVIDENCE_HIGH | Differential context value |
| Q-COV-09 | VERSE_EVIDENCE_HIGH | OT/NT repetition analytic |
| Q-COV-10 | VERSE_EVIDENCE_HIGH | Frequency-importance correlation |
| Q-COV-11 | VERSE_EVIDENCE_BREADTH_NOTE | Nuance differentiation by context |
| Q-COV-12 | VERSE_EVIDENCE_BREADTH_NOTE | Breadth captured in correlations |

Full question text: see `wa_obs_question_catalogue` rows obs_id 195–206. Linkage rows: `wa_flag_type_question_link` (M31 schema).

---

## 9. Controlled Vocabulary — `wa_term_inventory`

### 9.1 language

Hebrew | Greek

### 9.2 testament

OT | NT

### 9.3 term_owner_type

OWNER — canonical home for this Strong's number. Verses active. Processed by Verse Context.
XREF — cross-reference copy in another registry. Verses delete_flagged. Verse context derived from OWNER classification.

### 9.4 term_introduction_source (new in M30, 2026-04-20)

Records how a term was introduced to the registry. Surfaced on `wa_term_inventory.term_introduction_source`. Populated by `scripts/classify_term_introduction_source.py` (heuristic proposal) + researcher review.

| Code | Meaning |
|---|---|
| `step_keyword` | Surfaced by STEP's English keyword → Strong's search (primary anchor at rank 0 of `word_registry.strongs_list`) |
| `step_association` | STEP's "related terms" cluster for the primary Strong's (rank 1+ of strongs_list) |
| `step_meaning_block` | Extracted from STEP's meaning/definition prose |
| `step_subgloss` | From STEP's sub-gloss expansion |
| `derived_from_meaning` | Term identified from pattern analysis of another term's `meaning` field text in the same registry |
| `researcher_external` | Researcher added from external Bible research (outside STEP) |
| `ai_proposed` | AI-surfaced during analytical session; researcher-approved |
| `registry_elevation` | A term under another registry was promoted to standalone registry status; this row represents the reverse-import as a term back under another registry |
| `legacy_unknown` | Introduction source not recoverable from available signals — last-resort fallback |

Companion fields: `term_introduction_rationale` (free-text explanation), `term_introduction_date` (ISO-8601 UTC).

---

## 10. Evidential Status — Research Need / Outcome Vocabulary

Updated 2026-04-20 (§12.1 of coverage-flags-redesign). `wa_term_inventory.evidential_status` is now the **research-need / research-outcome tracker** for a term — integrates with the `research_actions` routes on flag types (§8a) and catalogue questions (§8b).

Prior vocabulary (`confirmed` / `plausible` / `uncertain` / `instrumental` / `relational_only`) was retired in M29 as it implied graded judgment (principle violation per GR-EVIDENCE-002). Legacy rows were remapped: `confirmed` → `research_not_required`; others → `pending_further_research` with legacy rationale note.

### 10.1 New controlled vocabulary (M29, 2026-04-20)

| Value | Meaning |
|---|---|
| `pending_further_research` | A flag has triggered a research route; investigation queued but not yet performed |
| `research_in_progress` | Investigation is active |
| `research_confirmed_inner_being` | Research complete — term IS in scope for inner-being study |
| `research_excluded_not_applicable` | Research complete — term is not in scope; registry-level action may follow |
| `research_alternative_term_found` | Research complete — another term better covers this meaning |
| `research_no_biblical_substance` | Research complete — modern concept; no biblical antecedent |
| `research_extends_study` | Research complete — new analytical paths opened; recorded for follow-on |
| `research_not_required` | No flag → no research need (default; equivalent to NULL) |

### 10.2 Usage rule

- Default for a term with no evidence flag: NULL (or `research_not_required`)
- When a `VERSE_EVIDENCE_*` flag is raised, `evidential_status` should move to `pending_further_research` until the linked Q-COV questions are answered
- Answers captured in `wa_session_b_findings` + `wa_finding_catalogue_links` → `evidential_status` then transitions to one of the `research_*` outcomes

### 10.3 Legacy mapping (2026-04-20)

| Old value | Count (2026-04-20) | New value |
|---|---:|---|
| `confirmed` | 106 | `research_not_required` |
| `plausible` | 44 | `pending_further_research` |
| `uncertain` | 5 | `pending_further_research` |
| `instrumental` | 0 (never populated) | — |
| `relational_only` | 0 (never populated) | — |

`retention_note` carries a legacy rationale string on each remapped row.

---

## 11. Session D Observation Types

### 11.1 session_d_observations.observation_type

term_co_occurrence | verse_cluster | volume_reliability | scope_boundary

### 11.2 sdpointers pointer_type

term_co_occurrence | verse_overlap | evidential_uncertainty | scope_boundary | data_quality_impact | structural_observation

### 11.3 sdpointers pointer_subtype

shared_root | shared_gloss | shared_domain | divergent_usage | shared_verse | thematic_proximity | thin_corpus | boundary_term | cross_registry_dependency | registry_border | cluster_border | affects_cross_registry | volume_concern | classification_risk | testament_shift | divine_human_parallel | conceptual_gap

### 11.4 sdpointers significance and research_depth

significance: HIGH | MEDIUM | LOW
research_depth_required: SURFACE | STANDARD | DEEP

---

## 12. Patch Index — CANONICAL SOURCE: DB `wa_patch_type_registry` (M35 2026-04-20)

Single navigation point for patch types. **Authoritative catalogue lives in DB** — consume via reference snapshot. Governing document for each type is named; for applicator rules and JSON format, see `wa-patch-instruction [current]`.

Per wa-patch-instruction §3, `session_b_status` is required and non-null in `_patch_meta` for PREANALYSIS, SESSIONB, SESSIOND, CLUSTERING, and REPAIR patches. VERSECONTEXT, VCGROUP, VCVERSE carry `session_b_status: null` — the applicator must not reject these.

| Patch type | Governing instruction | Valid `session_b_status` | Purpose |
|---|---|---|---|
| PREANALYSIS | wa-sessionb-analysis-readiness (when finalised) | Pre-Analysis Complete | Term classification — extracted/delete/xref |
| SESSIONB | wa-sessionb-analysis-output (when finalised) | Analysis Complete / Session B Complete | Evidential status, dimensions, findings, SD pointers |
| VERSECONTEXT | wa-versecontext-instruction v2_7 | null | Full batch verse relevance filter, grouping, anchor designation |
| VCGROUP | wa-versecontext-instruction v2_7 | null | Targeted update to verse_context_group |
| VCVERSE | wa-versecontext-instruction v2_7 | null | Targeted update to verse_context |
| SESSIOND | wa-sessiond-orientation v3_0 | null | Session D discovery and synthesis |
| CLUSTERING | wa-registry-management-guide v5_9 | null | Cluster assignment updates |
| REPAIR | wa-patch-instruction §9 | Current status or reset target | Cascade resets for pipeline re-runs |

See wa-patch-instruction v2_0 for full patch format, supported operation types, and applicator behaviour.

---

## 13. Database Schema Summary

Source: schema v3.8.0 (migrations M01–M18 complete).

### 13.1 word_registry

Core fields: id | no | word | source_list | category_hint | phase1_status | phase1_term_count | phase1_verse_count | session_b_status | verse_context_status | origin | dimensions | notes | cluster_assignment | sb_classification | sb_classification_reasoning | carry_forward | unique_term_count | shared_term_count | term_sharing_ratio | dim_review_status | dim_review_version | word_synopsis

`anchor_verses` removed in M17. `dimensions` renamed from `source_category` in M17. `verse_context_status` added in M18. `dim_review_status` + `dim_review_version` added in earlier DBR cycles for Dimension Review tracking. **`word_synopsis` added in M21 (2026-04-19)** — 1–2 sentence researcher-authored word summary, rendered into Session A Summary section. Pipeline must never overwrite.

**Engine-derived fields (Phase 1 state only):** `phase1_term_count`, `phase1_verse_count`, `unique_term_count`, `shared_term_count`, `term_sharing_ratio`. Populated by the Session A engine; NOT updated by Session B. Live counts must be derived from queries against mti_terms and wa_term_inventory.

**Redundant field — inference_note:** Not written by any pipeline stage. May contain researcher-set content; preserve on update. Never overwrite in pipeline operations.

### 13.2 mti_terms

Fields: id | strongs_number | transliteration | gloss | language | owning_registry | owning_registry_fk | owning_word | status | status_note | exclusion_reason | anchor_note

**Active-terms filter (absorbed from global rules addendum ADD-REF-001).** All SQL queries against `mti_terms` that are intended to return active terms must include `AND mt.status IN ('extracted', 'extracted_thin')`. Queries without this filter return deleted/excluded terms and produce incorrect counts. Non-waivable where "active terms" is the query intent. Per GR-DATA-001 v2.0.

**Field authority — somatic classification (absorbed from global rules addendum ADD-REF-002).** The authoritative field for somatic classification is `mti_term_flags` (flag_id 3 = SOMATIC_INNER_LINK; flag_id 4 = BODY_INNER_EXPRESSION). The `wa_term_inventory.somatic_link` column is redundant and not updated by the Session B pipeline. Per GR-DATA-003 v2.0.

**Field note — status_note:** Written only by the Session A engine (audit_word step A10). The Session B pipeline does not write to this field.

### 13.3 wa_term_inventory

Fields: id | file_id | language | term_id | strongs_number | transliteration | step_search_gloss | word_analysis_gloss | occurrence_count | testament | delete_flagged | status_note | evidential_status | retention_note | term_owner_type

**Redundant fields — not written in Session B pipeline:**
- `god_as_subject` — superseded by mti_term_flags (flag_id 1 = GOD_AS_SUBJECT). Mti_term_flags is authoritative.
- `somatic_link` — superseded by mti_term_flags (see §13.2 authority rule above).
- `status_note` — NULL across active records; retained for historical compatibility.

### 13.4 wa_session_research_flags

Fields: id | registry_id | file_id | flag_code | flag_label | strongs_reference | cross_registry_id | priority | session_target | description | session_raised | raised_date | resolved | resolved_date | resolved_note

### 13.5 wa_file_index

Fields: id | filename | registry_id | word_registry_fk | word | part_number | total_parts | phase | produced_date | source_file | specification | revision_note

### 13.6 wa_verse_records

Fields: id | file_id | term_inv_id | reference | verse_text | testament | translation | book_id | chapter | verse_num | delete_flagged | target_word | span_strong_match | mti_term_id

### 13.7 wa_cross_registry_links

Fields: id | file_id | linked_word | linked_registry_id | connection_type_id | connecting_term | note

### 13.8 wa_session_b_dimensions

Fields: id | registry_id | file_id | relational_environment | relational_environment_note | spirit_soul_body | spirit_soul_body_note | inner_operations | inner_operations_note | being | being_note | raised_date | session_b_instruction

### 13.9 wa_session_b_findings

Fields: id | finding_id | registry_id | file_id | finding_type | finding | anchor_verses | raised_date | session_b_instruction

### 13.10 Session D tables

session_d_runs | session_d_verse_links | session_d_term_links | session_d_observations

### 13.11 verse_context_group (M18)

Fields: id | mti_term_id | group_code | context_description | notes | delete_flagged

One row per contextual meaning group per term. `group_code` format: `{mti_term_id}-{3-digit-serial}`. Integer `id` used for joins; `group_code` is a human-readable label.

### 13.12 verse_context (M18)

Fields: id | verse_record_id | mti_term_id | group_id | is_anchor | is_relevant | is_related | notes | delete_flagged

UNIQUE on (verse_record_id, mti_term_id, group_id). One row per verse per term per group.

### 13.13 Prose store (M20, 2026-04-19) — v3.10.0

DB-canonical prose storage with FTS5 search and markdown round-trip editing via `<!-- PROSE_SECTION -->` markers (design: `wa-prose-store-design-v1-20260419.md`).

#### 13.13.1 `prose_section_type` — section catalogue (26 seeded types)

Fields: id | code | label | source_stage | lifecycle_tag | chapter_no | description | expected_length_min | expected_length_max | sort_order | delete_flagged | created_at

| source_stage | Count | Notes |
|---|---:|---|
| `session_a` | 6 | sa_s1_d1..d6 — Summary, Meaning, Terms, Verses, Pointers, Questions (see §13.13.2) |
| `session_b` | 5 | Stage 2c 5-chapter reader-facing output |
| `session_c` | 5 | Reader-facing word study chapters |
| `session_d` | 10 | Cross-registry synthesis chapters |

**Session A section types** (OT-DBR-014 flags a labelling mismatch on chapters 3/4 — Terms label sits on chapter_no=4 in the seed, Verses label on chapter_no=3; `generate_session_a_extract.py` dispatches by label keyword not chapter_no so output is correct regardless):

| id | code | label | Chapter_no (seed) |
|---:|---|---|---:|
| 1 | `sa_s1_d1` | Session A — Word Summary | 1 |
| 2 | `sa_s1_d2` | Session A — Meaning | 2 |
| 3 | `sa_s1_d3` | Session A — Verses | 3 |
| 4 | `sa_s1_d4` | Session A — Terms | 4 |
| 5 | `sa_s1_d5` | Session A — Pointers | 5 |
| 6 | `sa_s1_d6` | Session A — Questions | 6 |

#### 13.13.2 `prose_section` — the prose rows

Fields: id | registry_id | section_type_id | heading | body | word_count | status | version | supersedes_id | superseded_by_id | author | created_at | approved_at | approved_by | metadata_json | source_file | delete_flagged

`status` values: `draft` | `in_review` | `approved`. `author` values: `claude_ai` | `claude_code` | `researcher`.

**Versioning:** narrative prose uses supersede chain (new row per version; `supersedes_id` links back). Mechanical Session A extracts are exempt — `session_a_replace` operation UPDATES in place per Session A advice Q5.

#### 13.13.3 `prose_section_fts` — FTS5 virtual table

FTS5 full-text search across prose bodies. Synced via explicit INSERT/UPDATE/DELETE triggers on `prose_section`. Search via `prose_section_fts MATCH 'query'`.

#### 13.13.4 `prose_section_dimension_link` — dimensions cited in a prose row

Fields: id | prose_section_id | dimension | created_at

Populated during Session A generation (for `sa_verses` + `sa_terms` sections) and during Session B/C/D narrative authoring. Enables dimension-scoped prose search.

#### 13.13.5 `prose_section_finding_link` — findings referenced in a prose row

Fields: id | prose_section_id | finding_id | created_at

Populated during Session A generation (for `sa_pointers`) and later narrative authoring. Enables finding-to-prose navigation.

### 13.14 wa_flag_type_question_link (M31, 2026-04-20) — v3.11.0

Junction mapping `wa_quality_flag_types.id` → `wa_obs_question_catalogue.obs_id`. Populated 2026-04-20 for the 4 VERSE_EVIDENCE flag types → 12 Q-COV catalogue questions (see §8b).

Fields: id | flag_type_id | question_id | context_note | active | created_at

UNIQUE on (flag_type_id, question_id). Active index: `active=1`.

**Usage pattern:** when a VERSE_EVIDENCE flag surfaces on a term, Session A / Session B prose generators look up linked Q-COV questions via this junction and inline them beneath the flag mention. Answers land in `wa_session_b_findings` + `wa_finding_catalogue_links`.

---

## 14. Post-Patch Output Structures

### 14.1 Final Registry Extract — `wa-{nnn}-{word}-final-v{n}-{YYYYMMDD}.json`

Cross-table registry view produced after analysis completion patch. Produced by Claude AI per the Session B analysis-output instruction (when finalised). See wa-patch-instruction §8 for the JSON template.

### 14.2 Session D Pointers — `wa-{nnn}-{word}-sdpointers-v{n}-{YYYYMMDD}.json`

Auto-generated by apply_session_patch.py from SD_POINTER flags in wa_session_research_flags. See wa-patch-instruction §8 for the JSON template.

---

## 15. Term Ownership and Housekeeping

### 15.1 term_owner_type

OWNER — canonical home for this Strong's number. Verses active. Processed by Verse Context.
XREF — cross-reference copy. Verses delete_flagged. Verse context derived from OWNER.

### 15.2 Term sharing fields on word_registry

- `unique_term_count` — OWNER terms whose Strong's appears only in this registry
- `shared_term_count` — OWNER terms whose Strong's appears in other registries
- `term_sharing_ratio` — shared / (unique + shared). 0.0 = all unique; 1.0 = all shared.

### 15.3 mti_term_id on wa_verse_records

Direct FK to mti_terms.id — one-hop path from verse to master term index.

### 15.4 CONCRETE_PHYSICAL quality flag

Flagged but not excluded. Verse analysis may reveal inner-being usage in context.

### 15.5 Housekeeping rules (delete_flagged)

- Particle terms (ki, asher, al, im, etc.) are delete_flagged across all registries
- `mti_status = delete` is synced to `wa_term_inventory.delete_flagged`
- Verse records under delete_flagged terms are also delete_flagged
- XREF verse records are delete_flagged (OWNER verses only in active set)
- Records with `delete_flagged = 1` are excluded from all standard queries and exports
- No physical deletion. Per GR-OBS-005 (absorbed into wa-patch-instruction §5 for CC behaviour).

---

## 16. Anchor Verse Definition

An anchor verse is the programme's canonical reference verse for a specific contextual meaning group of a term (`verse_context_group`). It is the verse that most clearly and economically demonstrates the inner-being engagement of the term in that group.

**Dual purpose:**
1. **Efficiency instrument** — Session B Analysis reads anchor verses rather than the full verse corpus
2. **Citation instrument** — anchor verses appear in Session B narratives and Session D synthesis as the evidential foundation for claims

**Minimum requirement:** every term must have at least one active anchor (`is_anchor = 1, delete_flagged = 0`) across all its groups before Session B Analysis may proceed.

**Selection criteria:** unambiguous inner-being function; stands alone without requiring surrounding context; 1–2 per group.

---

## 17. XREF Architecture

`mti_terms` holds one record per Strong's number — programme-wide, registry-independent.

`wa_term_inventory` holds one record per Strong's number per registry. Each is classified OWNER or XREF:
- **OWNER** — primary analytical home. Verses active. Verse Context processes OWNER terms only.
- **XREF** — cross-reference copy. Verses delete_flagged. Verse context derived from OWNER — the same term has the same contextual meaning regardless of which registry views it.

**Consequence for Session B:** words sharing XREF terms are analysed in cluster batches. XREF terms' contextual profiles (group descriptions and anchor references from the OWNER registry) are included in the analysis dataset.

**Current scale:** 5,518 OWNER terms, 1,470 XREF terms, 133,353 active verses (OWNER only).

---

## 18. Document Preparation and Validation Standard

Applies to all instruction documents in the programme. Before any instruction is declared ready for use, this standard must be applied.

This standard exists because a pipeline cannot be validated by decisions alone — only by the instruction text that governs execution. A decision recorded in a session log is the beginning of a remediation, not the end of a gap.

### 18.1 Inflection Point Completeness

An inflection point (IP) is any point where data moves between the pipeline and the database — DB read or DB write. Each IP must be assessed against:

| Criterion | What must be present |
|---|---|
| Operation | What is being done — read or write, which table, what action |
| Method | How it is executed — patch operation type, SQL query scope, engine command, or explicit statement that SQL construction is Claude Code's responsibility |
| Fields and values | Which fields, what values, derivation rules for non-obvious values |
| JSON structure | Where JSON is the carrier — structure must be pre-defined or referenced |

A gap exists if any criterion is not met. Instruction is not ready until all IPs are specified.

**SQL policy:** SQL queries and scripts are Claude Code's responsibility to construct. Claude AI instructions provide: field names, table names, join logic, derivation rules, expected outcomes, and a clear handoff statement. Where these are present, the gap is closed regardless of whether explicit SQL is written.

### 18.2 Gap Status Discipline

A gap is closed only when the instruction document itself contains correct and complete information. The following do not close a gap: a researcher decision in a session log; a verbal agreement; a gap-register note saying "decision made"; a prior instruction version that has not been updated.

Gap register distinguishes: OPEN | PENDING UPDATE (decision made; instruction not yet updated) | CLOSED. When an instruction is updated to address a gap, the register entry becomes CLOSED with reference to the specific document version and section.

### 18.3 Instruction Update Verification

After producing an updated instruction:
1. Verify key changes are in the output file via direct inspection. Do not rely on having made the edit — confirm.
2. Check the change note accurately describes what changed.
3. Check the Supersedes reference points to the correct prior version.
4. Check cross-references within the document point to current versions of companion documents (GR-REF-001 Discipline 2).

If verification fails, correct the document before presenting it.

### 18.4 Cross-Document Consistency

Governed by GR-REF-001 v1_0 Discipline 4 (consistency check at version bumps). When any programme document is updated, references in companion documents are checked for staleness.

The patch_specification (wa-patch-instruction v2_0+) is authoritative for operation types and applicator behaviour. This document (wa-reference) is authoritative for controlled vocabulary and schema. No instruction document defines terms or operations that conflict with these authorities. Per GR-REF-001 Discipline 3.

### 18.5 Failure and Recovery Paths

Every instruction that produces a patch must specify what happens when the patch is rejected. Minimum content:

- Condition indicating rejection (applicator returns error, patch_id conflict, validation failure)
- Immediate action (produce failure patch per wa-patch-instruction §10)
- Recovery procedure (diagnose cause, produce corrected patch with new patch_id, await researcher confirmation)

Every pipeline re-run scenario must have a defined REPAIR patch — see wa-patch-instruction §9 for the catalogue.

### 18.6 Dry Run Gate Assessment

Before recommending dry run or live pipeline execution: produce explicit gate assessment. The assessment:
1. Identifies BLOCKING or MISSING gaps for the specific word or batch.
2. For each, confirms CLOSED in instruction text — not just decided.
3. States explicitly which gaps do not apply.
4. Confirms document versions in use match the current suite.

If any BLOCKING gap remains open in instruction text, dry run recommendation is not made.

### 18.7 Version Control

Version control is governed by GR-FILE-003 v3_0 in the global rules. This section adds instruction-document-specific application:

Every instruction update carries:
- Supersedes — exact filename and version of the document replaced
- Change note — specific description of what changed and why, each change listed with the section affected
- Filename — includes version number per GR-FILE-001

Version numbers in the document header, filename, and footer must all be consistent.

### 18.8 Application

Applied in every session where instruction documents are prepared, reviewed, or updated. When asked whether instructions are ready or whether a stage can proceed, the response is grounded in this standard — not in confidence or absence of known problems.

If a prior session declared instructions ready without applying this standard, the declaration is provisional. Re-assess before execution proceeds.

---

*wa-reference-v5_6-20260418 | Supersedes WA-Reference-v5.5-20260330 | §1 brought into GR-FILE compliance; §13.2 and §13.3 absorb GR-DATA-001/003; §12 Patch Index updated; scope statement added per GR-REF-001 Discipline 5.*
