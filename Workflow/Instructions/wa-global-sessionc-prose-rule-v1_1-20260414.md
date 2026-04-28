# WA Global — Session C Prose Rule

Version: v1_1

**Filename:** wa-global-sessionc-prose-rule-v1_1-20260414.md
**Date:** 20260414 | **Version:** v1_1
**Previous output ref:** wa-global-general-rules-v2-20260414.json
**Status:** Draft rule for incorporation into the Session C instruction document at its next revision.

## Change note
v1.1 (20260414): Filename and header dates updated to compact format per GR-FILE-009. Filename corrected to lowercase per GR-FILE-007. Previous output ref updated to global rules v2. No substantive content changes. FLAG-001 in global rules file notes that the full Session C instruction is missing from project files — this prose rule remains the primary Session C governance document until FLAG-001 is resolved.

---

## 1. Purpose

This document specifies the discipline under which Session C produces reader-facing word studies from the observations database. The rule exists because of a pattern identified during the compassion word study audit (2026-04-13): literary framings and interpretive claims were introduced at the Session C writing stage without audit trail in Session B's observations. When audited against the JSON and the observations log, these framings had no source. Some were defensible; some were factually wrong; all broke the chain of evidence.

The rule's goal is to make the word study reproducible from the database alone. Under this rule, a clean instance of Claude AI with access only to the database and the Session C instruction must be able to produce an equivalent word study — the same claims, the same structure, the same evidence — for any registry.

---

## 2. The core rule

**Session C reader-facing prose must derive from (b) observations in the database. It must not introduce new analytical claims at the writing stage.**

Concretely:

1. Every analytical claim in the word study must correspond to at least one (b) observation in `observation_description` keyed to the registry or to an entity the registry owns.
2. The writer declares which observations support a section via the `study_segment` field on each observation.
3. During rendering, the writer reads observations whose `study_segment` matches the section being written (plus any `cross_segment` observations that apply).
4. The writer selects order, emphasis, linking language, and metaphor — these are presentation choices, not analytical additions.
5. The writer may not assert any analytical claim that is not traceable to a declared observation.

---

## 3. The gap-detection corollary

The rule creates one structural consequence: while writing, the writer will sometimes identify a gap — something the prose should say but which is not supported by any existing observation. The corollary handles this case.

**When a gap is identified, writing pauses. The writer produces a patch or directive that adds the missing observation(s) to the database, applies the patch, pulls a fresh extract, and resumes writing against the updated database.**

This makes Session C a discovery-plus-rendering stage, not a generation stage. Gaps are a normal and expected outcome of writing — they indicate that Session B did not produce a complete set of observations for a given section. The correct response is to close the gap via the database, not to bridge it via unsourced prose.

The gap-filling patch follows the same discipline as any other observation patch:

1. The new observation has an evidential source (a verse text, a lexical entry, a correlation record, a dimension assignment, or another observation it builds on).
2. The observation is keyed to the relevant entity.
3. The `study_segment` is declared.
4. The patch is applied and a fresh extract is pulled before writing resumes.

---

## 4. The insight caveat

Per researcher direction (2026-04-13): "Too much structure too early blocks creative thinking. Something valuable may lie outside the declared boundaries."

The rule is not a cage. Writers are expected to discover insights while writing — connections between observations, emergent patterns, structural features that become visible only in the rendering process. These insights are welcome and the rule accommodates them, but with a constraint:

**Insights that lie outside the declared observation set become new observations, not new prose.**

The writer pauses, records the insight as a new (b) observation, applies it to the database, and resumes writing with the insight now part of the declared set. The insight is preserved (in the database, where it can be audited and reused by Session D), and the prose is still traceable.

This is the same mechanism as the gap corollary (Section 3) — but the gap corollary handles *missing* observations that should have been produced by Session B, while the insight caveat handles *new* observations that arise specifically from the writing process. Both flow through the patch mechanism; both result in database updates; both preserve the derive-from-observations rule.

---

## 5. What the rule prohibits

The rule prohibits the following patterns, all of which were identified in the compassion audit:

### 5.1 Literary framings without source

A sentence like "Lam 3:22 is not optimistic sentiment but defiant confession in the face of catastrophe" is a literary framing. The "defiant confession" language is an author choice. The rule requires that this framing be grounded in an observation — either a specific (b) observation that uses or licenses the "defiant" framing, or a more neutral observation that the writer then renders with this framing.

If the framing has no source, the writer cannot use it. Either the writer adds a (b) observation that supports it (and the observation itself must have evidential grounding — e.g., the Lamentations genre context, the counterfactual force of the declaration against its setting), or the writer renders the substance without the framing.

### 5.2 Superlatives without programme-wide data

A sentence like "Mercy shares 38 terms with compassion — the largest term-sharing recorded in this research" contains a superlative ("largest in this research"). Per GR-PROG-006, superlatives are only permissible if supported by programme-wide data. Registry-local maxima are not programme-wide superlatives.

Under the rule, the writer either (i) omits the superlative and states the fact neutrally, or (ii) produces a programme-wide (b) observation that verifies the superlative and declares its scope. Option (ii) requires the programme-wide correlation extract, not just the registry's own extract.

### 5.3 Comparative claims without evidence

A sentence like "The New Testament introduces a dimension of compassion that the Old Testament vocabulary does not develop at the same depth" is a comparative claim. The observation that the sym- compounds are a NT-concentrated development is supported; the comparative "does not develop at the same depth" in the OT is an interpretive addition.

Under the rule, the writer either (i) omits the comparative half, or (ii) adds a (b) observation that supports the comparative — which in this case would require a parallel examination of OT participatory-compassion vocabulary, which is Session D work, not Session C work.

### 5.4 Premature closure of forward pointers

A sentence like "Isaiah 54:8 settles the question of which impulse is more fundamental" closes a Session D pointer (SD-019) by writing it as settled. Per GR-OBS-002, forward pointers are resolved in their designated session — Session B resolves Session B pointers, Session D resolves Session D pointers. Session C does not resolve pointers.

Under the rule, the writer renders the verse's evidence as evidence, not as resolution. The pointer remains open. The word study can note that a particular verse speaks to an open question without claiming to close it.

### 5.5 Factual claims that conflict with the underlying data

This was the most serious class of error in the compassion audit — claims about which verses and which vocabulary are shared with which partner registries that did not match the correlation data. These errors usually originated in the analytical brief, not in the word study, but they propagated through the word study because the writer did not verify against the JSON.

Under the rule, the writer verifies every factual claim against the observation it derives from. If the observation itself is wrong (because the brief was wrong), the writer cannot render the wrong claim — the writer instead triggers a correction patch against the brief's observation and resumes writing after the correction.

---

## 6. Rendering-verification procedure

A rendered section is verified against its declared observations by the following procedure:

1. **Identify the section's observation set.** Retrieve all observations with `study_segment` matching the section (plus `cross_segment` observations that apply).
2. **Extract the section's claims.** Read the section prose and list every analytical claim it makes.
3. **Match each claim to an observation.** For each claim, find the supporting observation(s) in the declared set.
4. **Flag unmatched claims.** Any claim that cannot be matched to a declared observation is a violation — either the writer introduced an unsourced claim (violation of the core rule) or the writer forgot to declare a relevant observation (correctable by updating the observation's `study_segment`).
5. **Flag unused observations.** Any observation in the declared set that is not rendered in the prose is noted. This is not a violation — the writer may legitimately choose not to render every observation — but it is a signal that either the observation is not needed for this section, or the writer missed it.

The procedure can be run manually by the writer (self-verification at section close) or automated (once the schema is implemented and a rendering tool is available). Per PRD-05 in the session actions register, this choice is pending researcher decision.

---

## 7. Section-level linking via `study_segment`

The `study_segment` field on each observation declares which section of the word study the observation belongs to. See Artefact 2 Section 7 for the proposed initial vocabulary.

Writers use the field in two directions:

1. **When rendering a section:** read observations whose `study_segment` matches the section, and render from them.
2. **When adding a new observation (via gap-filling or insight capture):** declare the `study_segment` at observation-creation time.

The field is not exclusive — an observation can belong to multiple segments via the `cross_segment` value, or the segment vocabulary can be extended by the writer when a new segment type is needed. Per the insight caveat, segment vocabulary extension is a legitimate outcome of writing.

---

## 8. Workflow shape

The new Session C workflow under this rule is:

1. **Open the registry.** Read the registry record from `word_registry`.
2. **Retrieve observations.** Read all (b) observations keyed to the registry or to entities owned by the registry (terms, verses, groups, dimensions, roots), with `delete = 0`.
3. **Read the instruction.** Session C instruction specifies the word study's section structure.
4. **Render section by section.** For each section:
   a. Read observations with matching `study_segment`.
   b. Render the section prose from the observations.
   c. Run the rendering-verification procedure (Section 6) against the section.
   d. If gaps are found, pause and run the gap-filling corollary (Section 3).
   e. If insights arise, pause and run the insight caveat (Section 4).
   f. When the section is verified, close it.
5. **Close the word study.** When all sections are verified, produce the word study file (markdown), run the final verification pass (all sections verified, no unclosed gaps, no unclosed insights), and deliver.

The workflow is stepped and verifiable. At each point the writer knows exactly what observations the section is drawing on, what gaps exist, and what corrections have been made.

---

## 9. Relationship to the previous Session C workflow

The previous workflow (under which the compassion word study v3 was produced) allowed the writer to synthesise freely from the analytical brief and the observations log. This produced readable prose but broke the chain of evidence — some claims in the word study had no source, and some claims that did have source were misattributed.

The new workflow constrains writing to the database and makes rendering the core activity. This is a significant change in what Session C does:

- **Old Session C:** synthesise, frame, interpret, render.
- **New Session C:** render from declared observations, detect gaps, fill gaps via patches, capture insights as new observations.

The synthesis and framing work moves upstream to Session B (where it can be audited at each pass close) and the writing work becomes a rendering task with discovery support.

Literary quality is not sacrificed — the writer still chooses order, emphasis, and language. But the analytical content is no longer generated at the writing stage.

---

## 10. Open items for incorporation into the Session C instruction

The next revision of the Session C instruction should incorporate:

1. A reference to GR-OBS-006 for the core rule.
2. A reference to the general rules file (Artefact 1) and the removal of duplicated rules from the inline instruction text.
3. The workflow shape in Section 8 of this document, replacing the current synthesis-based workflow.
4. The rendering-verification procedure in Section 6.
5. The three corollaries — gap-detection (Section 3), insight caveat (Section 4), and the explicit prohibitions (Section 5).
6. A reference to the `study_segment` controlled vocabulary (once the schema is implemented and the vocabulary is finalised).
7. A note that the rule applies when the observations schema is live; pre-implementation, Session C operates in a degraded mode that still enforces the core rule against the markdown observations log as the best available source.

---

*Produced under GR-OBS-006. For incorporation into the Session C instruction at its next revision.*
