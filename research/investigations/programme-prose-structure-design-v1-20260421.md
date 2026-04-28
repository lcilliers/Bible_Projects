# Programme-wide Prose — Structure Design (Working Draft)

**Status:** DRAFT — for researcher annotation before we seed the `prose_section_type` catalogue.
**Date:** 2026-04-21 (rev 2 — researcher expansion applied)
**Purpose:** agree the two-level macro / sub-section structure for programme-wide prose, so the AI session that writes the prose has a clear frame to fill rather than a structure to invent.

**How this doc is used:** researcher reads and annotates (inline notes, prompts, additions, deletions, renames). When the structure is settled, we produce a seed patch that adds the macro and sub-section types to `prose_section_type` with `source_stage = 'programme'`, code + label + short description each. The AI session then fleshes each sub-section into a prose body via a PROSE patch (subject to the schema enablement directive per wa-directive-instruction [current] §10).

**M34 note:** Of the 8 items originally seeded in M34, 7 have clean homes in the new structure and will be renamed in place. One — `prog_field_authority` — does not appear in the revised structure; held for researcher decision (see Area 4 notes).

---

## Structure at a glance

| # | Macro area | Sub-sections (proposed) | Count |
|---|---|---|---:|
| 1 | Programme purpose | mission, scope, this inner-being programme, Defining inner being, Science and the bible, the expected outcome | 6 |
| 2 | Research methodology | Research method, Word selection and registry, Program flow: Word data → Verse data → Lexicon data → word analytics → inner being synergies → Reading Chapters, Science in action, Publishing, Key Principles, Key Constraints | 7 |
| 3 | Research approach | Tool selection, STEP foundation, two-AI division, Data Management, Process Instructions, evidential principles, verse data authority, Analytics and Question catalogue, Memory management, inner-being filter | 10 |
| 4 | Data architecture | Database, Registry, Terms, Ownership and XREF, verse groups, anchor verse, dimensions, questions, inter word relationships | 9 |
| 5 | Data integrity & governance | delete-discipline, validation, backup, patch-failure, finding references, STEP data provenance | 6 |
| 6 | Instruction corpus | global rules, referencing, authority, instruction versioning (`[current]`), update flow, directive vs patch, override protocol | 7 |

**Total:** 6 macro + 45 sub = **51 section types** to seed.

> **Researcher:** add / remove / rename any row above. Counts update as sub-section lists change.

---

## 1. Programme purpose

**Intent:** what this research programme is for, stated in its own terms — the governing question, how inner-being is defined, where the programme sits in the wider study, how it relates to scientific method, and what a successful outcome looks like. A reader with no prior context should come away understanding why the programme exists and what would count as a successful answer.

**Primary source material:** GR-PROG-001 (verse as primary unit of evidence); GR-PROG-002 (governing question — what is the inner life of mankind per scripture); CLAUDE.md §1 (project overview); researcher's framing of the wider study; `word_registry.word_synopsis` examples once populated.

### Proposed sub-sections

| Code (draft) | Label | Short description (stub — what the prose will cover) |
|---|---|---|
| `prog_purp_mission` | Mission | One-paragraph statement of what this programme is investigating, why, and what outcome would constitute success. |
| `prog_purp_scope` | Scope | The research boundary — the ~214 English inner-being words and their Hebrew/Greek mappings — and what is outside. Edge-case treatment (proper nouns, particles, lexically distant terms). |
| `prog_purp_this_inner_being_programme` | This inner-being programme | This specific programme's distinct frame: inner-being-of-mankind as research subject; what makes it a separate study; its 214-word scope. Covers the wider-programme context inline where relevant — no separate "wider programme" section is kept. |
| `prog_purp_defining_inner_being` | Defining inner being | How the programme defines "inner being" in its own terms; the distinctions from soul / spirit / body / material referents; the working definition that drives the filter. |
| `prog_purp_science_and_bible` | Science and the Bible | How the programme relates scientific method to scriptural text; the empirical / textual / interpretive layers; epistemological stance; what kind of knowledge the programme claims to produce. |
| `prog_purp_expected_outcome` | Expected outcome | What success looks like: Session C word studies, Session D cross-registry synthesis, publishing, what a reader should take away. |

> **Researcher notes / prompts — Area 1:**
>
> -
> -
> -

---

## 2. Research methodology

**Intent:** the actual pipeline and data flow — from word selection through to publishing — with the principles and constraints that govern execution. This is *what we do*. Area 3 (Research approach) covers *how we think*. Memory management sits in Area 3 (Approach), not here — this area is about the work itself.

**Primary source material:** CLAUDE.md §8 (data flow patterns); Session A / VC / Session B / C / D instructions; GR-PROG-001 through GR-PROG-007; `wa_registry_management_guide`.

### Proposed sub-sections

| Code (draft) | Label | Short description (stub) |
|---|---|---|
| `prog_meth_research_method` | Research method | High-level description of the programme's method: read-evidence-classify-synthesise cycle; iteration and revision; how findings are distinguished from hypotheses. |
| `prog_meth_word_selection_registry` | Word selection and registry | How the ~214 words were chosen; how the registry is governed; how new words are added and excluded; the Phase 1 → VC → Session B lifecycle on `word_registry`. |
| `prog_meth_programme_flow` | Programme flow | The data-flow pipeline: **Word data → Verse data → Lexicon data → Word analytics → Inner-being synergies → Reading chapters**. Each stage, what it produces, what it feeds into. |
| `prog_meth_science_in_action` | Science in action | How scientific discipline shows up in day-to-day work: hypothesis → evidence → finding; falsifiability; revision when evidence contradicts. |
| `prog_meth_publishing` | Publishing | How work product is released: Session C word studies (v1 / v2 / v3 lifecycle), cross-registry synthesis, target audiences, format conventions. |
| `prog_meth_key_principles` | Key principles | The programme's governing principles at a glance: verse as primary unit (GR-PROG-001), inner-being filter (GR-PROG-007), two-AI discipline (GR-PROG-005), evidence-first (GR-PROC-002). |
| `prog_meth_key_constraints` | Key constraints | What the programme deliberately does not do: no theological advocacy, no systematic theology, no comparative religion, no prescriptive counsel. |

> **Researcher notes / prompts — Area 2:**
>
> -
> -
> -

---

## 3. Research approach

**Intent:** the principles, tools, and disciplines the programme operates by. Distinct from Area 2 (Methodology), which is the actual pipeline. This area is *how we think* and *what we rely on*. Memory management lives here because it is a discipline that makes the programme possible across Claude AI's per-session amnesia — not a pipeline step.

**Primary source material:** GR-PROG-005 (two-AI division); GR-DATA-001 (mti_terms evidence discipline); GR-PROC-002 (findings rooted in evidence); GR-LOAD-001 (session startup); GR-REF-002 (`[current]` token); STEP Bible foundation; `wa_obs_question_catalogue`.

### Proposed sub-sections

| Code (draft) | Label | Short description (stub) |
|---|---|---|
| `prog_app_tool_selection` | Tool selection | Why the chosen tools (SQLite, STEP Bible, Python, Claude AI, Claude Code) and not others; trade-offs; what each tool is relied on for. |
| `prog_app_step_foundation` | STEP Bible foundation | What STEP provides (lexical data, verse occurrences, original-language HTML spans); why it is treated as authoritative; what is and isn't taken from it. |
| `prog_app_two_ai_division` | Two-AI division of responsibility | Claude AI as analytical engine; Claude Code as database engine (GR-PROG-005). Why the split exists; what each does; how they interact via patches and directives. |
| `prog_app_data_management` | Data management | How data is managed: DB as canonical long-term memory; extracts for AI session consumption; soft-deletes for audit; per-patch backups; 6-month retention. |
| `prog_app_process_instructions` | Process instructions | How work is driven by instruction documents, not conversational direction (GR-PROG-005, GR-REF-001/002). The instruction corpus as the programme's procedural memory. |
| `prog_app_evidential_principles` | Evidential principles | Verse as primary unit (GR-PROG-001); findings rooted in evidence (GR-PROC-002); evidential-status vocabulary (confirmed / plausible / uncertain / instrumental / relational_only). |
| `prog_app_verse_data_authority` | Verse data authority | Why verse data from STEP is treated as authoritative; how verse-level assertions are grounded; the link from finding to verse to term. |
| `prog_app_analytics_question_catalogue` | Analytics and question catalogue | The role of the 194 + 12 Q-COV catalogue questions (`wa_obs_question_catalogue`); how analytics surface questions into prose; the question-flag routing via `wa_flag_type_question_link`. |
| `prog_app_memory_management` | Memory management | How the programme persists across Claude AI's per-session amnesia. DB as canonical long-term memory; obslog as per-session working memory; CLAUDE.md + instruction docs as durable reference; `memory/` as auto-memory for persona/preferences; `[current]` token (GR-REF-002) for self-resolving cross-references; session-start loading (GR-LOAD-001) as the re-hydration mechanism. |
| `prog_app_inner_being_filter` | Inner-being relevance filter | The term-level filter (GR-PROG-007) that decides which terms carry inner-being meaning; what it rules in and out; how it interacts with OWNER vs XREF classification. |

> **Researcher notes / prompts — Area 3:**
>
> -
> -
> -

---

## 4. Data architecture

**Intent:** the core entities, their relationships, the scale, and the design patterns fundamental to the programme (ownership model, XREF, anchor verses, dimensional profiles, question catalogue). A reader should understand the shape of the database.

**Primary source material:** CLAUDE.md §3 (schema overview — groups 1–18); `database-schema-v3.14.0-20260421.json`; CLAUDE.md XREF Architecture block; `wa-reference` §13 schema section.

### Proposed sub-sections

| Code (draft) | Label | Short description (stub) | Notes |
|---|---|---|---|
| `prog_arch_database` | Database | SQLite 3.50, schema v3.14.0, 61 tables organised into 18 groups; scale (~133k active verses, ~5.5k OWNER terms, 214 registries); WAL mode. | new |
| `prog_arch_registry` | Registry | `word_registry` as the anchor for everything; ~214 words; lifecycle fields (`phase1_status`, `verse_context_status`, `session_b_status`); researcher-authored fields. | new |
| `prog_arch_terms` | Terms | `mti_terms` (programme-wide, one per Strong's) paired with `wa_term_inventory` (per-registry occurrence record); Hebrew / Greek distinction; how terms join the registry. | new |
| `prog_arch_ownership_xref` | Ownership and XREF | OWNER vs XREF term classification (`term_owner_type`); why verse records live on OWNER only; how `verse_context` is shared via `mti_term_id`; current distribution (5,518 OWNER / 1,470 XREF). | **renames M34 `prog_xref_architecture` → `prog_arch_ownership_xref`** |
| `prog_arch_verse_groups` | Verse groups | `verse_context_group`: contextual meaning clusters within a term's verse occurrences; group-code convention; one-anchor-per-group rule. | new |
| `prog_arch_anchor_verse` | Anchor verse | What an anchor verse is; designation (VC instruction); role in extracts and Session B reading; one-per-group discipline. | **renames M34 `prog_anchor_verse` → `prog_arch_anchor_verse`** |
| `prog_arch_dimensions` | Dimensions | The dimensional profile concept (PRIMARY / SECONDARY / PERIPHERAL); `wa_session_b_dimensions`; cluster-level dimensions; how dimensions emerge from evidence. | new |
| `prog_arch_questions` | Questions | `wa_obs_question_catalogue` (194 + 12 Q-COV); question taxonomy; `wa_finding_catalogue_links` junction; question-flag routing (`wa_flag_type_question_link`). | new |
| `prog_arch_inter_word_relationships` | Inter-word relationships | `wa_cross_registry_links` (typed cross-links); correlation signals across registries; pointer structures for Session D synthesis. | new |

> **Researcher notes / prompts — Area 4:**
>
> - Held M34 seed `prog_field_authority` (researcher-authored vs pipeline-derivable fields) is not in the new structure. Options: (a) drop — the content can live under `prog_arch_database` or `prog_app_data_management`; (b) add as a 10th sub-section here; (c) relocate to Area 5 (Data integrity & governance). Awaiting decision.
> -
> -

---

## 5. Data integrity & governance

**Intent:** the disciplines that keep the DB correct over time — how records are retired (not deleted), how quality is validated, how work is recovered from failure, how findings trace back to their evidence, how upstream data provenance is tracked.

**Primary source material:** GR-OBS-005 (no physical deletes — absorbed into patch instruction §5.4); validation standards in wa-reference; `engine/backup.py` + per-patch backup discipline; wa-patch-instruction §9 REPAIR catalogue + §10 failure patch; `wa_finding_entity_links`; STEP Bible as external source.

### Proposed sub-sections

| Code (draft) | Label | Short description (stub) | Notes |
|---|---|---|---|
| `prog_gov_delete_discipline` | Delete discipline | No physical deletes. `delete_flagged = 1` + `obsolete_reason` + `obsolete_date`. Why — audit trail, recoverability, FK integrity. The applicator's rejection of DELETE statements. | **renames M34 `prog_delete_discipline` → `prog_gov_delete_discipline`** |
| `prog_gov_validation` | Validation | The GR-REF-001 five disciplines applied to documents and to analytical findings. Cross-reference versioning via `[current]`. Pre-apply validation the patch applicator performs. | **renames M34 `prog_validation_standard` → `prog_gov_validation`** |
| `prog_gov_backup` | Backup | Rolling pre/post-run backups by `engine/backup.py` (10 retained); per-patch applicator backups named after `patch_id`; 6-month retention; restore protocol via directive. | **renames M34 `prog_backup_discipline` → `prog_gov_backup`** |
| `prog_gov_patch_failure` | Patch failure and REPAIR | What happens when a patch is rejected or fails mid-apply; REPAIR catalogue (STEP-rerun / audit_word-rerun / VC-rerun / analysis-rerun); failure patches; mid-pool recovery. | **renames M34 `prog_patch_failure_protocol` → `prog_gov_patch_failure`** |
| `prog_gov_finding_references` | Finding references | How findings reference their evidence: `wa_finding_entity_links` (finding → verse / term / group); the trace from a Session B / D finding back to raw data; audit-path integrity. | new |
| `prog_gov_step_data_provenance` | STEP data provenance | STEP Bible as authoritative upstream for term metadata and ESV verse occurrences; pagination (60-row canonical splits); re-fetch policy; what is and isn't re-derivable from STEP. | new |

> **Researcher notes / prompts — Area 5:**
>
> -
> -
> -

---

## 6. Instruction corpus

**Intent:** how the programme's rules and instructions are managed — not the rules themselves (those live in `wa_rule_registry`), but the discipline around authoring, versioning, referencing, updating, and overriding them. Authority and hierarchy are covered here rather than as a separate area.

**Primary source material:** GR-REF-001, GR-REF-002 (the `[current]` token); docs/rules-update-protocol.md; wa-patch-instruction §13 (rules patches); wa-directive-instruction §10 (schema enablement); GR-PROC-004 (researcher approval); GR-PROG-005 (authority hierarchy).

### Proposed sub-sections

| Code (draft) | Label | Short description (stub) | Notes |
|---|---|---|---|
| `prog_ic_global_rules` | Global rules | `wa_rule_registry` as canonical post-M33; the 36 active rules; the four-field structure (rule_text / rationale / application_notes / examples) added by DIR-20260421-001; 13 categories. | new |
| `prog_ic_referencing` | Referencing discipline | GR-REF-001 five disciplines: pointer-not-copy; versioned references; single authoritative document per content type; consistency check at version bumps; scope discipline. | new |
| `prog_ic_authority` | Authority hierarchy | Who / what has authority over what: Global rules > instruction docs > conversational direction. Researcher as ultimate authority on scope and methodology. Claude AI authorship within researcher direction (GR-HF-001). | new |
| `prog_ic_instruction_versioning` | Instruction versioning and `[current]` | How programme documents are versioned (e.g. `v2_3-20260421`); operational cross-references use `[current]` (GR-REF-002); provenance references use specific versions. | new |
| `prog_ic_update_flow` | Update flow | How rules and instructions are changed post-M33: conversational → draft RULES patch → self-check → researcher approval → apply → regenerate extract → commit. Cross-ref `docs/rules-update-protocol.md`. | new |
| `prog_ic_directive_vs_patch` | Directive vs patch | Decision logic (wa-patch-instruction §1 + wa-directive-instruction §1). Schema enablement directives (v1_2 §10) as a distinct pattern for patch prerequisites. | new |
| `prog_ic_override_protocol` | Override protocol | How the researcher overrides a rule (new rule, amended rule, directive, patch). What Claude Code refuses even with researcher instruction (physical deletes, `--no-verify`, unauthorised force-push). | **renames M34 `prog_instruction_override_protocol` → `prog_ic_override_protocol`** |

> **Researcher notes / prompts — Area 6:**
>
> -
> -
> -

---

## Seeding plan (once structure is agreed)

1. This document is edited by the researcher; macro areas and sub-section lists reach agreement.
2. Claude Code produces a `CATALOGUE_POPULATION` patch (or sequence of PROSE-type patches) that:
   - **Inserts** the 6 new macro section types (`prog_purp`, `prog_meth`, `prog_app`, `prog_arch`, `prog_gov`, `prog_ic`) as chapter anchors with `source_stage = 'programme'`, `chapter_no = {1..6}`, `sort_order = 0`.
   - **Inserts** 40 new sub-section types with appropriate `chapter_no` and `sort_order`.
   - **Updates** 6 existing M34 seeds in place (rename `code`, update `description`, set `chapter_no` and `sort_order`): `prog_anchor_verse`, `prog_xref_architecture`, `prog_validation_standard`, `prog_delete_discipline`, `prog_backup_discipline`, `prog_patch_failure_protocol`, `prog_instruction_override_protocol`.
   - **Defers** `prog_field_authority` (existing M34 seed not in the new structure) pending researcher decision (Area 4 notes).
3. After the seed patch, the prose extract (`build_programme_prose_extract.py`) shows **51 empty handles** with meaningful descriptions — a structure the AI session can fill rather than invent.
4. The schema enablement directive per wa-directive-instruction v1_2 §10 is then executed (making `prose_section.registry_id` nullable), after which the PROSE patch(es) writing body text can apply.
5. The AI prose-authoring session writes bodies for the sub-sections. Macro sections may receive a short framing paragraph each (see open question 1 below), typically produced by the researcher or by a follow-up AI pass once the sub-sections exist.

---

## Open questions for the researcher

1. **Macro-section bodies.** Should macro sections (`prog_purp`, `prog_meth`, `prog_app`, `prog_arch`, `prog_gov`, `prog_ic`) themselves carry prose bodies, or are they frame-only (heading + stub description) with all real content in the sub-sections? My suggestion: short framing paragraph each, one short paragraph summarising what follows — makes the extract readable on its own and gives the AI a target for consistent area-level framing.
2. **`prog_field_authority`** — the one M34 seed that has no clean home in the new structure. Drop / fold into another section / add as a 10th sub-section under Data architecture? (See Area 4 notes.)
3. **Code-naming convention.** New structure uses area-prefixed codes (`prog_purp_mission`, `prog_arch_database`, `prog_gov_backup`). Acceptable? Alternative: flat codes (`prog_mission`, `prog_database`, `prog_backup`) — shorter but ambiguous once 46 sub-sections exist.
4. **Granularity.** Any sub-section that should be split (e.g. `prog_meth_programme_flow` could become 6 sub-sub-sections, one per pipeline stage), or merged?
5. **Area ordering.** Current order: Purpose → Methodology → Approach → Architecture → Governance → Instructions. Reader could argue Approach before Methodology (how we think before what we do); kept as you set it for now — flag if you want swap.

---

*Draft rev 2 for researcher annotation — not yet a decision.*
