# wa-prose-framework-review-v1-20260421

> Framework B Soul Word Analysis Programme — Review of Programme-Prose Structure Design
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-draft-033-patch-failure-v1-20260421; wa-prose-obslog-v1-20260421
> Subject of review: `programme-prose-structure-design-v1-20260421.md` (researcher's first draft, rev 2)
> Governed by: wa-global-general-rules [current]; GR-HF-001 (this is review-on-ask — extensive analytical content is appropriate)

---

## Purpose of this document

Researcher has requested Claude AI's review of a structural framework for programme-wide prose. The task, per researcher: "describe the program as a whole, and the key guiding principles governing it" — with three specific prompts: (a) thoughts on the document; (b) should it be structured differently; (c) are there glaring missing areas.

This review is organised strictly per session protocol: observation → interpretation → reflection, separately, followed by structural concerns, missing-area flags, and direction questions. No restructuring is proposed as a decision — proposals are presented as options.

---

## 1. Observation — what the framework actually is

The draft proposes a two-level architecture for programme-stage prose in `prose_section`:

- **6 macro areas** (chapter-level anchors), each with its own `prose_section_type` row with `chapter_no` set.
- **46 sub-sections** distributed across the 6 areas (7+7+10+9+6+7).
- **Total: 52 `prose_section_type` rows** to seed via a CATALOGUE_POPULATION or PROSE-type patch.

The 6 macro areas are:
1. Programme purpose
2. Research methodology
3. Research approach
4. Data architecture
5. Data integrity & governance
6. Instruction corpus

Each macro area has:
- An intent statement (1–2 sentences stating what content the area holds).
- A named primary-source list (which rules, documents, code files feed the content).
- A proposed sub-section table with code (draft), label, and short description (stub).
- A researcher-notes slot for inline annotation.

Seven of the eight M34 seeds are relocated by rename (codes change from `prog_*` flat pattern to `prog_{area}_*` pattern); one (`prog_field_authority`) is held for decision.

A seeding plan and five open questions close the document.

---

## 2. Interpretation — what the framework is doing

**The framework solves two real problems.** The M34 seeds are a flat list of 8 disciplines. A flat list at the size the programme requires (potentially 50+ records) becomes hard to navigate, hard to assign authorship for gaps, and hard to present as a coherent reader-facing artefact. The two-level structure gives the records an outline. It also does double duty: the macro areas supply the table of contents for a future "programme as a whole" document, while the sub-sections supply the individual prose rows the extract will hold.

**The framework extends scope deliberately.** M34's 8 seeds covered disciplines and protocols — operational content. The framework adds whole categories the M34 seeds did not attempt: the programme's purpose and governing question (Area 1), the research methodology as a pipeline narrative (Area 2), the data-architecture story (Area 4), the instruction corpus as a self-describing system (Area 6). This is the shift from "capture the programme's disciplines" to "describe the programme as a whole". The researcher's framing message confirms this is intended.

**The framework is reader-oriented, not just operator-oriented.** The M34 seeds read like an operator's reference — things a working Claude AI needs to stay in compliance. The framework's Area 1 and parts of Areas 2 and 4 read like introductory content for a reader new to the programme. Both audiences matter; the framework serves both by keeping them in separate areas.

**Three areas are new terrain; three are consolidations.** Areas 1, 2, and 4 are mostly new content — most sub-sections have no existing authoritative home. Areas 5 and 6 largely consolidate content that already exists in rules, instructions, and (now retired) wa-reference. Area 3 is mixed. The drafting effort per area varies substantially with this.

**The M34 rename is clean with one exception.** Six of the seven renamed codes land cleanly in their new areas — same content, better address. `prog_field_authority` has no natural home and is held for decision. This is handled correctly: the framework does not force-fit it.

---

## 3. Reflection — what I notice about the framework's construction

**The framework is substantially well-conceived.** The two-level structure is the right instinct; the area divisions are defensible and I can reconstruct the logic behind each boundary; the primary-source lists are specific enough to make drafting tractable; the seeding plan is operationally coherent. This is not a document that needs rescoping — it needs refinement.

**The strongest areas are 1, 4, and 5.** Area 1 (Purpose) has a clear reader-facing intent and sub-sections that naturally decompose it. Area 4 (Architecture) mirrors the database's own structure (registry → terms → ownership → groups → anchors → dimensions → questions → relationships), which is how the data naturally tells its story. Area 5 (Governance) is a clean consolidation of operational disciplines into a unified area.

**Area 2 and Area 3 have boundary tension.** The draft names it directly ("Area 2 is *what we do*; Area 3 is *how we think*") and locates memory management in Area 3, not Area 2. This is a considered choice — but the distinction is genuinely hard to sustain. Examples:
   - `prog_meth_key_principles` is in Area 2, but "verse as primary unit" and "two-AI discipline" are thinking-disciplines not pipeline-stages — they belong to Area 3's genre.
   - `prog_meth_science_in_action` (Area 2) and `prog_app_evidential_principles` (Area 3) will be hard to keep from duplicating content.
   - `prog_meth_key_constraints` (Area 2) — "what we deliberately do not do" — is a principle of approach, not a methodology step.

   The boundary is not wrong, but it is fuzzy enough that the AI writing each area will need explicit disambiguation to keep bodies from bleeding into each other's territory.

**Area 6 is the weakest in my reading — too close to mirroring the rules.** Six of the seven proposed sub-sections (`prog_ic_global_rules`, `prog_ic_referencing`, `prog_ic_authority`, `prog_ic_instruction_versioning`, `prog_ic_update_flow`, `prog_ic_directive_vs_patch`) are prose narratives *about* rules and instructions that already exist as first-class records in `wa_rule_registry` and as standalone instruction documents. The risk: these prose records drift out of sync with the rules they describe, becoming stale mirrors. The authoritative-memory principle depends on prose being the home, not the mirror — but for content that already has an authoritative home elsewhere, a prose narrative is a mirror by definition.

   Two ways to resolve this:
   - Keep Area 6 but explicitly frame its content as *meta-narrative* — not "what GR-REF-002 says" but "why the programme has a `[current]` token at all and what discipline it enforces". This makes the prose genuinely additive rather than duplicative.
   - Trim Area 6 to the genuinely un-housed items: the override protocol (already an M34 seed because it had no home), the authority hierarchy (partially housed), and the update flow (partially housed). Drop the rest as adequately covered by the rules registry and instruction documents they describe.

**The primary-source lists are a hidden strength.** Every area specifies where its content comes from. This is exactly what memory-first drafting needs. The researcher has effectively pre-solved half the problem of "where does Claude AI look when memory runs out" by naming the sources.

**The seeding plan hits one operational ordering issue.** Step 2 produces the CATALOGUE_POPULATION patch; step 4 executes the schema enablement directive; step 5 writes bodies. But step 2 also inserts into `prose_section_type`, which is independent of the `prose_section.registry_id` NOT NULL — the catalogue patch does not need the schema enablement directive first. Only the body-writing patches need it. This is actually fine as drafted, but the plan reads as if they are sequenced; worth clarifying that steps 2 and 4 are independent gates on different tables.

---

## 4. Structural concerns — specific items to consider

### 4.1 Area 3 name and scope

"Research approach" is functional but weak. It is structurally a basket — thinking disciplines, tools, memory management, evidential principles, filter. The grouping works, but the area has less narrative unity than the other five. Two options:

- **Rename** to signal the basket nature explicitly — "Operational disciplines" or "Working principles". Less elegant but more honest about the content.
- **Split** — move tools (2 sub-sections) into Area 4 (they are architecture-adjacent); move memory management into Area 5 (it is governance-adjacent); keep Area 3 as evidential-and-filter principles only. Reduces Area 3 to a tighter 5–6 sub-sections.

Either option is defensible. The current naming hides the basket, which produces the boundary tension I noted in §3.

### 4.2 Macro-section bodies (open question 1 in the framework)

The framework asks whether macro sections carry prose bodies. My view: **yes, short framing paragraphs**. The reasons:

- The extract is a navigational artefact for future Claude AI sessions. A macro row with only a stub description gives a bare header; a short framing paragraph orients the reader to what the area is for.
- The framing paragraph is also where area-level principles live — the "what area X is and is not" content that prevents boundary bleed between adjacent areas. For Areas 2/3 where the boundary is fuzzy, macro bodies are where the disambiguation gets stated.
- Cost is low (6 short bodies, ~150 words each).

One caveat: **macro bodies should be written last**, after the sub-sections. Writing the framing before the detail risks framing that the content then does not match. The sequence: seed all 52 types; draft sub-section bodies; then draft macro bodies with the actual content in view.

### 4.3 `prog_field_authority` — the held M34 seed

The framework offers three options: drop, fold, relocate. My view:

- **Relocate to Area 5** (Governance). Field authority is a field-level consistency discipline — "which field wins when two sources disagree" — which is fundamentally a governance question. It sits naturally alongside delete-discipline, validation, and patch-failure.
- Drop is wrong — the content is operationally important (GR-DATA-003, GR-DATA-005 exist because field authority is not obvious).
- Fold into `prog_app_data_management` or `prog_arch_database` would sink the content into a larger sub-section and reduce its visibility. Field authority is cross-cutting enough to deserve its own record.

Proposed Area 5 placement: between `prog_gov_validation` and `prog_gov_backup`, as `prog_gov_field_authority` (renames M34 `prog_field_authority` → `prog_gov_field_authority`).

### 4.4 Code-naming convention (open question 3 in the framework)

My view: **keep the area-prefixed codes**. `prog_arch_database` is longer than `prog_database` but unambiguously locates the record in its area. With 46 sub-sections the flat namespace becomes unreadable — `prog_database` could be architecture or a data management discipline, and the code alone doesn't tell you. The tradeoff is about one additional word of code length vs. navigability; navigability wins at this scale.

### 4.5 Granularity — programme flow (open question 4 in the framework)

`prog_meth_programme_flow` covers six pipeline stages in one record. Two options:

- **One record** covering all six stages as a narrative of the pipeline. Reader gets the whole flow; record is longer (~1500 words).
- **Six records** — one per pipeline stage, plus one framing record that shows how they connect.

My view depends on audience. For a reader new to the programme, the single-record narrative is more useful. For an operational reference where a Claude AI session is trying to orient to a specific stage, the per-stage records are more useful. Given that Session A / VCB / Dimension Review / Session B / C / D instructions already exist as first-class documents providing per-stage operational detail, the prose store does not need to replicate that granularity. **Recommend: one record**, with references out to the per-stage instructions.

### 4.6 Area ordering (open question 5 in the framework)

Current: Purpose → Methodology → Approach → Architecture → Governance → Instructions.

The framework notes Approach-before-Methodology is arguable. My view: **keep the current order but reconsider if Area 3 is renamed**. The current order works if Area 2 (Methodology) is read as "the pipeline" and Area 3 (Approach) is read as "how we run the pipeline". Rename Area 3 to something basket-honest and the order becomes: Purpose → Pipeline → Disciplines → Data → Governance → Rules. That reads well.

---

## 5. Glaring missing areas — check

Researcher asked specifically whether there are **glaring missing areas**. Searching for them systematically:

**5.1 Collaboration / roles beyond the two-AI split.** The framework covers CA + CC in Area 3 (`prog_app_two_ai_division`). It does not surface the researcher's role explicitly — as decision authority, as approver, as source of direction, as reviewer of drafts. GR-PROC-004 (researcher approval), GR-RD-007 (researcher feedback process), GR-HF-001 (researcher as direction-setter, Claude AI as authorship-within-direction) exist because the researcher is the third role and it is non-trivial. Proposed addition: a sub-section under Area 3 or Area 6 on the researcher's role and the authority hierarchy — **`prog_app_researcher_role`** or **`prog_ic_authority_hierarchy`** (latter overlaps with existing `prog_ic_authority` but could absorb it).

**5.2 Session lifecycle — not the pipeline, the unit.** Area 2 covers the pipeline (the whole programme's data flow). Nothing explicitly covers *a session* — what a session is, how it starts (GR-LOAD-001 three-step gate), how it carries the obslog, what closes it (session log), what persists between sessions (DB, CLAUDE.md, memory) and what does not (context, reasoning). This is a foundational concept that `prog_app_memory_management` touches but does not own. Proposed addition: **`prog_app_session_lifecycle`** under Area 3.

**5.3 Flags and flag resolution.** The programme uses flags (legacy FLAG-nnn, research_flag table, finding-flag links) as a key mechanism for deferring classification decisions and surfacing review items. This gets no sub-section. It could live in Area 3 (approach — how the programme defers decisions) or Area 4 (architecture — the flag table is an entity). Proposed addition: **`prog_app_flag_discipline`** or **`prog_arch_flags`**.

**5.4 Findings — the Session B output as a first-class entity.** Area 4 covers architecture from registry through to inter-word relationships but does not surface `wa_session_b_findings` explicitly. Findings are the programme's primary analytical output — they carry evidential status, dimension links, question links, SD pointers. They deserve their own architectural record. Proposed addition: **`prog_arch_findings`** under Area 4.

**5.5 The observations question catalogue architecture is in Area 4 but the relationship to flags is not.** `prog_arch_questions` covers the catalogue but the flag-type-question link (`wa_flag_type_question_link`) is a key integration point — questions surface as flags, flags route to questions. Not a missing area, but worth noting the current sub-section should integrate this relationship or it will be missed.

**5.6 Clusters.** `wa_cluster_assignments` and the C01–C22 cluster organisation is a processing discipline (registries are grouped into clusters for phased processing) but is not surfaced. It could fit in Area 2 (methodology — how processing is sequenced) or Area 4 (architecture — cluster as an entity). Proposed addition: **`prog_meth_cluster_architecture`** under Area 2 or **`prog_arch_clusters`** under Area 4.

**5.7 The STEP data boundary.** Area 3 has `prog_app_step_foundation` and Area 5 has `prog_gov_step_data_provenance`. These will need very careful scoping to not overlap. Area 3 is "what STEP is and why we rely on it"; Area 5 is "how we track that reliance over time and what we re-derive vs cache". Reasonable split, but needs the framing to be explicit in both intent statements.

**5.8 Publishing lifecycle is thin.** `prog_meth_publishing` under Area 2 is one sub-section for the Session C word study lifecycle plus Session D synthesis plus target audiences plus format conventions — that is a lot in one record. At minimum: target audience and format conventions are worth splitting into a separate `prog_meth_publishing_standards` sub-section.

---

## 6. Direction questions (my authorship questions to researcher)

1. **Area 3 rename?** Current "Research approach" is a basket. Two options: keep but make macro framing explicit that it is the disciplines/tools area; or rename to "Operational disciplines" / "Working principles". Either is fine; preference?

2. **`prog_field_authority` placement?** My recommendation: relocate to Area 5 as `prog_gov_field_authority`. Confirm or redirect.

3. **Macro-section bodies — yes or no?** My recommendation: yes, short framing paragraphs, written last. Confirm or redirect.

4. **Additions (§5 above)?** Seven candidate additions — researcher-role record, session-lifecycle, flag-discipline, findings, clusters, publishing-standards split. Accept/reject each. At a minimum I would recommend accepting: researcher-role (5.1), session-lifecycle (5.2), findings (5.4). The others are valuable but could live as sections within existing sub-section bodies if scope is to be contained.

5. **Granularity — programme flow split?** My recommendation: keep as one record; per-stage detail lives in the per-stage instruction documents. Confirm or redirect.

6. **Area 6 trim or reframe?** My recommendation: reframe the intent to meta-narrative (why these rules/disciplines exist, not what they say) rather than trimming. If that cannot be held cleanly in drafting, trim to the genuinely un-housed items (override protocol, authority hierarchy, update flow). Which approach?

7. **Commitment to 52 types (or more after decisions above) is a substantial up-front seed.** Once seeded, reorganisation means renames with cascade effects (patches referencing codes). Should we seed in phases (start with one or two areas, adapt the structure if needed, seed the rest later), or seed the full structure in one patch?

---

## 7. Reflection on consequences and impact

**Impact on the programme.** The framework promotes the prose store from "a place for disciplines we want captured" to "the programme's self-description in narrative form". This is a significant elevation. Once populated, the prose store becomes a reading path into the programme for any new participant (human or AI) — parallel to how the rules registry is the binding path and the schema is the structural path. Three authoritative layers: rules (what you must do), schema (what the data looks like), prose (what the programme is). The framework is the architecture of the third layer.

**Impact on maintenance burden.** 52+ prose records are a substantial maintenance surface. Each is versioned, each can go stale, each needs a claimed author and a review cycle. Rules and schema already have robust maintenance disciplines (RULES patches, migrations, self-check). Prose does not yet have a parallel discipline for keeping narrative content in sync with the rules and schema it describes. Flagging: a **prose maintenance discipline** will be needed, probably as its own rule or sub-section — how prose records are reviewed when cited rules change, who authors the update, how supersedence chains (`supersedes_id` / `superseded_by_id`) are used. This is a programme-level consequence worth surfacing now, before 52 records exist.

**Cultural impact.** A well-populated programme-prose store changes who can engage with the programme. Currently, engaging with the programme requires reading the rules (binding), one or more instructions (procedural), and the schema (structural) — a steep ramp. A prose store with 52 narrative records provides a gentler ramp, especially Area 1 (Purpose). This matters for: future Claude AI sessions bootstrapping; a researcher returning to the work after a gap; potential future collaborators. The framework is investing in that ramp.

**No cultural impact on the research itself.** The prose store is descriptive, not prescriptive. Nothing about its content changes how verses are analysed, how dimensions are assigned, or how findings are produced. This is description work, not research work. Separation preserved.

**Impact on different interest groups:**
- *Future Claude AI sessions* — major benefit. 52 narrative anchors reduce the "reconstruct from fragments" pattern that produces drift.
- *The researcher* — moderate benefit, moderate burden. Benefit: a self-describing programme. Burden: review and annotation of 52 records, plus ongoing maintenance.
- *A future reader or collaborator* — major benefit (the ramp). This is the audience Area 1 is really for.
- *The research output (Session C / D publications)* — no direct benefit; these consume rules and schema, not prose. Indirect benefit through clearer programme conception.

---

## 8. What I propose to do next

This is a review, not a decision. Next actions are in the researcher's hands.

My recommended sequence:
1. Researcher reviews this review; makes decisions on the 7 direction questions (§6).
2. I revise the framework to reflect decisions — producing `programme-prose-structure-design-v2-20260421.md` (or an agreed revised version string).
3. After framework agreement: the CATALOGUE_POPULATION / PROSE-type patch seeds all agreed `prose_section_type` rows. This requires researcher approval per GR-PROC-004.
4. Schema enablement directive (independent of content; can run in parallel).
5. Draft sub-section bodies, starting with the easiest area (Area 5 Governance has most existing content to consolidate; my items 3 and 7 drafts would be absorbed here).
6. Draft macro-section bodies last.

The items 3 and 7 drafts produced earlier in this session remain on disk; if the framework is adopted, they need re-addressing against the renamed codes (`prog_gov_validation` and `prog_gov_patch_failure`) and the revised area intent. Minor work.

---

## 9. Cadence and safety flags

- This review is long — ~2800 words. Per GR-HF-001, "extensive help-forward is produced when the researcher explicitly asks for it"; this review was explicitly asked for, so the length is warranted. No apology needed.
- Nothing has been written to the database in this session. All session work is in draft files in `/mnt/user-data/outputs/` per GR-FILE-008.
- No patches or directives have been constructed in this session yet. The schema enablement directive is still to come.

---

*wa-prose-framework-review-v1-20260421 | Review of programme-prose-structure-design-v1-20260421 (researcher draft, rev 2) | Written per GR-HF-001 extensive help-forward on explicit ask*
