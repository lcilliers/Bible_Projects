# Session A Extract — Section Type Advice

| Field | Value |
|---|---|
| Filename | session-a-extract-section-types-advice-v1-20260419.md |
| Status | DRAFT — advice; awaiting researcher markup |
| Purpose | Answer the question "am I missing something?" for the proposed Session A extract section types |
| Relates to | `wa-prose-store-design-v1-20260419.md` (prose store — adds new `source_stage = 'session_a'` types) |
| Produced | 2026-04-19 |

---

## 1. Short Answer

**Your list is close, but 4–5 things are genuinely missing.** Your original five proposed groupings (Meaning, Terms, Verses, Pointers, Analytic Questions) cover most of Session B Stage 2's needs — but omitted orientation, the group/dimension structuring framework, supporting lexical context, and existing findings.

**Consolidated total: 6 section types** (after your §3 edits). You have folded the missing pieces into existing groupings rather than adding them as separate sections:

- Added **Summary** (1 new section) — covers orientation / registry state
- Expanded **Terms** — now includes root family + related words (lexical context)
- Expanded **Verses** — now includes verse-context groups and dimensions (analytical framework)
- Expanded **Pointers** — now includes cross-registry links (connections to pursue)

**All seven §8 questions resolved (2026-04-19):**

- Q1: Findings → Section 5 sub-block 5a; Session D pointers → sub-block 5b
- Q2: Correlations → Section 5 sub-block 5d
- Q3: File layout follows prose store §5 round-trip convention (marker-based; any number of sections per file)
- Q4: Status skips to `approved` on generation
- Q5: Simple in-place replace on regeneration (exception to supersede immutability for mechanical extracts)
- Q6: Populate both dimension and finding link tables during generation
- Q7: Word synopsis in Section 1 (Summary); new `word_synopsis` column on `word_registry`

**No remaining open questions.** Ready to produce the instruction artefact when DB-wide review design is approved.


---

## 2. Framing — What Session A Is (for this design)

Based on your description:

- Session A = **mechanical extraction** of data from the live DB into analyst-friendly `.md` files, grouped by topic.
- Purpose: **input to Session B Stage 2** — analysts read these instead of (or alongside) the JSON extract.
- Role: **Claude Code** performs this. No analytical judgement. Pure data rendering.
- Output: one `prose_section` row per (registry, section_type), `source_stage = 'session_a'`, `author = 'claude_code'`, `status = 'approved'` (since mechanical extraction produces authoritative snapshots).

This is a *new* role for prose_section — not narrative authoring, but structured-data rendering. It is valid, because:

- The content is stable TEXT (markdown tables, lists)
- It benefits from versioning (regenerate when DB changes)
- FTS5 on these extracts is useful (cross-word search)
- It sits alongside narrative prose in the same store

**Important:** these are *derived* artefacts. When the DB changes, the Session A extract for that registry should be regenerated. The current version is canonical; older versions are archived.

---

## 3. Consolidated Section Contents — Items, Source Tables, and Fields

**Design principle (applies to every grouping):** each section opens with a **meta block** giving context and the listing of items below. Each item is rendered from the specified source table and fields. Items are NOT concatenated into a single field — they are rendered as distinct sub-blocks inside the section.

### Section 1 — Summary

| Item | Source table | Key fields |
|---|---|---|
| Word identity | `word_registry` | `word`, `no` |
| Word synopsis (1–2 sentences) | `word_registry` | `word_synopsis` — **new column to be added** (per §8 Q7 → answered: belongs in Summary) |
| Programme state | `word_registry` | `carry_forward`, `session_b_status`, `verse_context_status`, `dim_review_status`, `dim_review_version` |
| Term population counts | `word_registry` | `unique_term_count`, `shared_term_count`, `term_sharing_ratio`, `phase1_term_count`, `phase1_verse_count` |
| Registry-level dimension list | `word_registry` | `dimensions` |
| Derived counts (confirmatory) | computed from `wa_verse_records`, `verse_context_group`, `wa_term_inventory` | total active OWNER/XREF term counts; total active verses; group count |

`cluster_assignment` excluded — incidental processing grouping, not analytical content.

---

### Section 2 — Meaning

Rendered per OWNER term that has meaning data. Terms without meaning data are noted (surfaces `NO_WORD_ANALYSIS` data quality flag).

| Item | Source table | Key fields |
|---|---|---|
| Parsed meaning header | `wa_meaning_parsed` | `id`, `term_inv_id`, `raw_meaning_text`, `parse_status` |
| Senses | `wa_meaning_sense` | `sense_text`, `sense_order`, `gloss`, `domain`, `register` |
| Stems (verbal forms) | `wa_meaning_stem` | `stem_label`, `stem_text`, `sense_link` |
| LSJ lexicon (Greek only) | `wa_lsj_parsed` | `lsj_entry`, `short_gloss`, `attested_forms` |

---

### Section 3 — Terms (OWNER + XREF)

Rendered per term, OWNER and XREF combined. OWNER terms first, then XREF. Each term gets a block with the fields below.

| Item | Source table | Key fields |
|---|---|---|
| Term identity | `wa_term_inventory` | `strongs_number`, `transliteration`, `step_search_gloss`, `word_analysis_gloss`, `language`, `term_owner_type` |
| MTI status | `mti_terms` | `status`, `owning_registry_fk`, `owning_word`, `occurrence_count` |
| MTI flags (authoritative for somatic / god_as_subject per GR-DATA-003) | `mti_term_flags` | `flag_id`, `flag_label` |
| Evidential status | `wa_term_inventory` | `evidential_status`, `retention_note` |
| Analytical fields | `wa_term_inventory` | `god_as_subject`, `somatic_link`, `causative_form_present`, `occurrence_count` |
| Data quality flags | `wa_data_quality_flags` | `flag_code`, `description`, `resolved` |
| Term-level dimension (aggregated from groups this term participates in) | derived from `wa_dimension_index` joined to `verse_context_group` via `mti_term_id` | `dimension` (majority label), distinct count of distinct dimensions |
| Root family | `wa_term_root_family` | `root_code`, `root_language`, `root_meaning`, `related_term_count` |
| Related words | `wa_term_related_words` | `related_strongs`, `related_gloss`, `relation_type` |
| Verse record counts | computed from `wa_verse_records` | total, active, delete_flagged; span_match_count |

---

### Section 4 — Verses (Group-First)

Rendered group by group. Each group is a block containing its dimension assignment and the verses inside it.

| Item | Source table | Key fields |
|---|---|---|
| Group identity | `verse_context_group` | `group_code`, `mti_term_id`, `context_description`, `delete_flagged` |
| Group dimension | `wa_dimension_index` | `dimension`, `dimension_confidence`, `manual_override`, `dominant_subject`, `anchor_count`, `related_count`, `set_aside_count`, `notes` |
| Verse record | `wa_verse_records` | `reference`, `verse_text`, `translation`, `span_strong_match` |
| Verse classification within group | `verse_context` | `is_relevant`, `is_anchor`, `is_related`, `set_aside_reason` |

Verses within each group are presented in three sub-groups: anchor → related → set-aside.

---

### Section 5 — Pointers

Three sub-blocks rendered in order.

**5a — Session B Pointers and Findings** (pointers remaining within Session B scope)

| Item | Source table | Key fields |
|---|---|---|
| Structured findings | `wa_session_b_findings` | `finding_code`, `finding_type`, `finding_text`, `status`, `delete_flag` |
| Catalogue linkage per finding | `wa_finding_catalogue_links` | `finding_id`, `question_id`, `coverage`, `status`, `mapped_date` |
| Catalogue question text (joined in for readability) | `wa_obs_question_catalogue` | `question_code`, `question_text`, `section` |
| Session B research flags | `wa_session_research_flags` WHERE `session_target = 'B'` | `flag_code`, `flag_label`, `description`, `priority`, `resolved`, `resolved_note`, `resolved_date` |
| Phase2 term-level advisories | `wa_term_phase2_flags` | `term_inv_id`, `flag_code`, `description`, `delete_flagged` |

**5b — Session D Pointers** (pointers for cross-registry synthesis)

| Item | Source table | Key fields |
|---|---|---|
| Session D research flags | `wa_session_research_flags` WHERE `session_target = 'D'` | `flag_code`, `flag_label`, `description`, `priority`, `resolved` |

**5c — Cross-Registry Links**

| Item | Source table | Key fields |
|---|---|---|
| Cross-registry link | `wa_cross_registry_links` | `target_registry_no`, `target_word`, `link_type_id`, `description`, `strength`, `delete_flagged` |
| Link type label | `wa_crosslink_type` | `link_type_code`, `link_type_label`, `description` |

---

### Section 6 — Analytic Questions

| Item | Source table | Key fields |
|---|---|---|
| Master catalogue questions | `wa_obs_question_catalogue` WHERE `scope = 'universal'` AND `deleted = 0` | `obs_id`, `question_code`, `section`, `question_text` |
| Registry-specific extensions | `wa_obs_question_catalogue` WHERE `source_registry_no = [this]` OR `source_word = [this]` | `obs_id`, `question_code`, `section`, `question_text` |

Questions are grouped by `section` (Sections 1–5 of the catalogue + registry-specific extension groups).

---

---

## 4. Consolidation Rationale — How the 6 Sections Absorb the 10 I'd Proposed

Each of your 6 groupings absorbs what I'd originally split into separate sections. Here is what is folded where and why.

### Into Summary (1 new section)

**What it covers that wasn't in your original 5:** Orientation. Without this block, the analyst has no framing.

**Maps to:** Question Catalogue **Section 1 — Word Characteristic Summary** (20 questions).

**Content:** word, no, session_b_status, verse_context_status, dim_review_status, unique_term_count, shared_term_count, term_sharing_ratio, phase1_term_count, phase1_verse_count, registry-level `dimensions`, carry_forward. `cluster_assignment` excluded (per your note: incidental processing grouping, not analytical content).

**Note:** Summary should also include a 1–2 sentence word synopsis at the top — human-readable framing of what this word means in the inner-being corpus. The synopsis can be derived deterministically from `word_registry.word` + meaning data for the canonical OWNER term(s).

### Into Terms (expanded)

**What is folded here from my originally separate sections:**

- **Quality flags** (was going to be sub-block): `wa_data_quality_flags` (THIN_DATA, SMALL_VERSE_SAMPLE, SPAN_FILTER_APPLIED, NO_WORD_ANALYSIS, CONCRETE_PHYSICAL, etc.) — per term context that qualifies data weight. Stays under Terms as dedicated per-term sub-block.
- **Term-level analytical metadata**: evidential_status, god_as_subject, somatic_link, `mti_term_flags` (authoritative source for somatic / god_as_subject per GR-DATA-003).
- **Term-level dimension**: inherited from the dimensions of groups this term participates in.
- **Lexical context (root family + related words)**: was going to be a separate `sa_lexical_context` section. Folded here because the analyst reading about a term wants its lexical relationships in the same view. Maps to Question Catalogue Section 4 (36 questions).

Structure per term: identity block → analytical metadata → quality flags → meaning (cross-ref to §2) → root family → related words.

### Into Verses (expanded)

**What is folded here:**

- **Verse Context Groups + Dimensions**: was going to be separate `sa_groups`. Folded because group framework and verses are analytically inseparable — the group is the frame, the verses are the content.
- Structure per verse group: group_code + context_description + dominant_subject + dimension + dimension_confidence + counts → verses inside group (anchor / related / set-aside), each with reference + ESV text + span match status.

**Maps to:** Question Catalogue Section 2 (Word Impact Description) and Section 3 (Annotated Verse Evidence) — 21 + 44 = 65 questions.

### Into Pointers (expanded)

**What is folded here:**

- **Research flags** (`wa_session_research_flags`): SB_FINDING, SD_POINTER, phase2_*, etc.
- **Phase2 flags** (`wa_term_phase2_flags`): term-level advisory signals.
- **Cross-registry links** (`wa_cross_registry_links` + `wa_crosslink_type`): was going to be separate `sa_cross_links`. Folded here because all four are "things to pursue" — cross-registry links are structural pointers to connected words.
- **Structured findings** (`wa_session_b_findings` + catalogue links): **See §8 Q1 for decision.** Recommend folding here as "prior research state" — the structured findings share the pointer/connections nature.

**Maps to:** Question Catalogue Section 5 — 26 questions.

### Kept outside — Correlation Signals

**Not included** in the six. Programme-wide correlation data (`build_correlation_extract.py` — ranked pairs, shared anchors) is Session D input; a brief summary line inside Pointers is sufficient at Stage 2. Full correlation reading belongs to Session D.

### Why the consolidation is the right call

- **Reading flow**: 6 sections scan faster than 10 with no loss of content.
- **Analytical cohesion**: lexical context belongs WITH terms; groups belong WITH verses. Separating them fragments the analyst's mental model.
- **File size**: 6 sections per word keeps the `.md` manageable for Obsidian / IDE preview.
- **FTS remains effective**: FTS5 search across 6 section types is as granular as across 10 — the markers still tag each section block.

---

## 5. Consolidated Proposed Section Types

Six section types for Session A. All `source_stage = 'session_a'`, `lifecycle_tag = NULL`, `author = 'claude_code'`.

| # | Code | Label | Primary data sources | Feeds Session B chapter |
|---|---|---|---|---|
| 1 | `sa_summary` | Session A — Summary (Registry Orientation) | `word_registry` + computed counts + registry-level dimension list | Ch 1 |
| 2 | `sa_meaning` | Session A — Meaning (Lexical / Semantic) | `wa_meaning_parsed` + `wa_meaning_sense` + `wa_meaning_stem` + `wa_lsj_parsed` | Ch 4 |
| 3 | `sa_terms` | Session A — Terms (OWNER + XREF) with Analytical Metadata, Root Family, Related Words | `wa_term_inventory` + `mti_terms` + `mti_term_flags` + `wa_data_quality_flags` + `wa_term_root_family` + `wa_term_related_words` | Ch 1, 2, 4 |
| 4 | `sa_verses` | Session A — Verses by Group with Dimensions and Annotations | `verse_context_group` + `wa_dimension_index` + `wa_verse_records` + `verse_context` | Ch 2, 3 |
| 5 | `sa_pointers` | Session A — Research Pointers, Findings, and Cross-Registry Links | `wa_session_research_flags` + `wa_term_phase2_flags` + `wa_session_b_findings` + `wa_finding_catalogue_links` + `wa_cross_registry_links` + `wa_crosslink_type` | Ch 5 |
| 6 | `sa_questions` | Session A — Analytic Questions (Catalogue + Extensions) | `wa_obs_question_catalogue` + registry-specific extensions | Driver for all chapters |

Each section opens with a **meta block** (context + fields-included listing), per the design principle in §3.

---

## 6. Section Ordering Rationale

The order is deliberately **telescoping from general to specific to analytical**:

1. **Summary** — frame the word (what is this?)
2. **Meaning** — what the word means lexically (semantic layer)
3. **Terms** — the atoms that carry the word's Hebrew/Greek realisations, with full lexical + analytical metadata
4. **Verses** — the evidence, structured by verse-context group and dimension
5. **Pointers** — prior research state: findings, research flags, cross-word connections (what is already known or flagged)
6. **Questions** — what still needs to be answered (the analytical task)

An analyst reading top-to-bottom gains: orientation → meaning → the terms and their evidence → prior research state → open analytical tasks. This matches the natural investigative flow for Session B Stage 2.

---

## 7. Integration with Prose Store Design (v1)

### 7.1 prose_section_type seed additions

Add **6 rows** to the `prose_section_type` seed, all `source_stage = 'session_a'`, with codes and labels per §5 above.

### 7.2 Update to wa-prose-store-design-v1 §4

The current §4 seed proposal covers Session B, C, D. It should be extended to include Session A as a fourth `source_stage`. The existing 5-chapter Session B Stage 2c structure (based on question catalogue Sections 1–5, per `wa-obs-question-catalogue-extract-20260419.md`) stays; Session A adds 6 new types.

### 7.3 Authoring and regeneration

Session A extracts are regenerated — not hand-authored. Pattern:

- A new script `scripts/generate_session_a_extract.py` produces all 6 sections for one registry
- Output: one `.md` file per registry (or segmented per section) imported via `import_prose.py`
- On import: any existing current-version Session A rows for that registry are superseded by the new rows (atomic batch)
- Section bodies are markdown tables and lists — deterministic rendering from SQL
- Each section's first line is the PROSE_SECTION marker; second block is the meta-block (context + fields-included listing) per §3 design principle

### 7.4 `author` value

Add `'claude_code'` as author for mechanical extracts. This is already in the proposed CHECK constraint in prose_section design §3.2. No schema change needed.

### 7.5 When does Session A run?

**Proposed trigger points:**

- After DB-wide review completes (establishes canonical schema)
- After per-word readiness sweep completes for a registry (data is ready for Stage 2)
- On demand when any patch affecting the registry is applied
- Pre-regeneration on entry to any Session B Stage 2 working session (per GR-DB-001 — never assume DB state)

### 7.6 Relationship to the JSON `build_complete_extract.py`

The two are **complementary**, not duplicative:

| Aspect | JSON extract (`build_complete_extract.py`) | Session A prose extract (new) |
|---|---|---|
| Format | JSON | Markdown |
| Audience | Programmatic consumers (Claude AI patch generation, applicator, automation) | Human/Claude AI **readers** during Stage 2 analysis |
| Granularity | Every field, every row | Curated, formatted for reading |
| Volume | Large (may be MB per word) | Smaller, scannable |
| Search | None native | FTS5 across all Session A sections |
| Update frequency | On-demand per script run | Versioned, stored, searchable |

Session B Stage 2 attaches BOTH: JSON for reference lookup, Session A markdown for reading.

---

## 8. Open Questions

### Q1 — Placement of `wa_session_b_findings` — **RESOLVED**

**Researcher decision (2026-04-19):** Session B findings are pointers belonging to Section 5. Listed as a distinct sub-block (5a — Session B Pointers and Findings) separate from Session D pointers (5b). Reflected in §3 Section 5 structure.

---

### Q2 — Correlations — include or defer? — **RESOLVED**

**Researcher decision (2026-04-19):** Correlations are **included in Pointers** (Section 5). Added as a fourth sub-block (5d — Correlation Signals) alongside 5a (SB findings/pointers), 5b (SD pointers), and 5c (cross-registry links). Reflects the unified "prior research state / connections to pursue" theme.

---

### Q3 — Per-word output: one file with all 6 sections, or 6 files? — **RESOLVED**

**Researcher decision (2026-04-19):** Refer to `wa-prose-store-design-v1-20260419.md` §4 Section Type Catalogue — section types themselves are the semantic unit. File layout follows the round-trip marker convention (§5 of prose store): any number of sections can live in a single file or be split across files. Export tool supports both layouts via flags.

---

### Q4 — Status handling — **RESOLVED**

**Researcher decision (2026-04-19):** Session A extracts go directly to `approved` on generation. No draft/in_review chain. If the researcher wants to annotate an extract, that creates a NEW derivative (narrative) section rather than a new version of the mechanical extract.

---

### Q5 — Supersede semantics for regeneration — **RESOLVED**

**Researcher decision (2026-04-19):** On regeneration, existing Session A rows are **simply replaced** — no supersede chain. Explicit exception to the immutability rule: for rows with `author = 'claude_code'` AND `source_stage = 'session_a'`, regeneration UPDATEs the existing row in place rather than INSERTing a new version.

**Implementation implication:**

- `body`, `word_count`, `heading`, `metadata_json`, `source_file` refreshed
- `created_at` retained; optional `regenerated_at` field OR simple refresh of `created_at`
- No new row; no supersede linkage
- FTS triggers fire on UPDATE — search index stays current
- History of old extracts is recoverable only by re-running the generator against a historical DB backup (acceptable for mechanical derivations)

This keeps the DB lean and reflects that mechanical extracts don't need preservation the way narrative versions do.

---

### Q6 — Metadata linkage — **RESOLVED**

**Researcher decision (2026-04-19):** Yes — populate `prose_section_dimension_link` and `prose_section_finding_link` during Session A generation.

Specifically:

- `sa_verses` (chapter 3) gets dimension links (one per distinct dimension referenced in the section's groups)
- `sa_pointers` (chapter 5) gets finding links (one per finding listed in sub-block 5a)
- `sa_terms` (chapter 4) gets dimension links (one per distinct term-level dimension) — for completeness

On regeneration (per Q5 simple-replace semantics): DELETE existing links for the row, then INSERT fresh links in the same transaction as the row UPDATE.

---

### Q7 — Word synopsis in Summary — **RESOLVED**

**Researcher decision (2026-04-19):** Word synopsis belongs in Section 1 (Summary). Implies adopting option (c) — a new `word_synopsis` column on `word_registry`, researcher-authored once per word, pulled into every Summary regeneration. Reflected in §3 Section 1 field list and in DB-wide review scope (new column migration).

---

## 9. Summary

**What you originally proposed:** 5 section types (Meaning, Terms, Verses, Pointers, Analytic Questions).

**What I originally recommended:** 10 section types — your 5 plus Orientation, Groups+Dimensions, Root Family+Related, Findings, Cross-Links.

**What your §3 edits consolidated to:** **6 section types** — Summary, Meaning, Terms, Verses, Pointers, Analytic Questions — absorbing the additions into expanded groupings rather than new sections.

**Reason the 6 works:** each analytical concept I had separated is absorbed naturally:
- Orientation → new Summary
- Lexical context (root family + related) → expanded Terms (where it belongs analytically)
- Groups + Dimensions → expanded Verses (where the structure supports the evidence)
- Cross-links → expanded Pointers (as "connections to pursue")
- Findings → proposed into expanded Pointers (§8 Q1)

**Design principle:** each section opens with a meta block (context + fields included).

**Integration:** adds 6 rows to `prose_section_type` seed, `source_stage = 'session_a'`. New generation script `generate_session_a_extract.py`. Imports via existing `import_prose.py`. FTS5 coverage inherited automatically.

**All seven §8 questions resolved 2026-04-19.** Key design points now settled:

- **Pointers (Section 5)** has four sub-blocks: 5a SB findings+pointers, 5b SD pointers, 5c cross-registry links, 5d correlations
- **File layout**: follows prose store §5 marker convention (per-word or per-section layouts both supported)
- **Status**: mechanical extracts go straight to `approved`
- **Regeneration**: simple in-place replace (exception to supersede rule for `source_stage='session_a'` + `author='claude_code'`)
- **Link tables**: populated during generation for `sa_verses`, `sa_terms`, `sa_pointers`
- **Word synopsis**: new `word_synopsis` column on `word_registry`

**Downstream impact propagated:**

- DB-wide review M_P7: `ALTER TABLE word_registry ADD COLUMN word_synopsis TEXT`
- Prose store schema: immutability-exception rule for Session A rows (amend §3.2 design notes)
- Patch instruction: PROSE patch type gains `session_a_replace` operation (in-place UPDATE for Session A rows)

---

## 10. Approval

**Researcher approval — write below:**

Status: [ ] APPROVED — PROCEED (adopt 6 sections as consolidated)  [ ] APPROVED WITH MODS — see markup  [ ] REVISIONS REQUESTED

Date:  
Reviewer: le Roux Cilliers
Notes:  

---

*End of advice v1 — 2026-04-19 (updated after researcher edits 2026-04-19 PM)*
