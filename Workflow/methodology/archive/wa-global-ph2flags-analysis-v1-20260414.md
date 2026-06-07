# WA Global — Phase 2 Flags: Role, State, and Programme Treatment

**Filename:** wa-global-ph2flags-analysis-v1-20260414.md
**Date:** 2026-04-14
**Version:** 1.0
**Previous output ref:** assessment-wa-term-phase2-flags.md (2026-04-13)
**Status:** Analysis document for researcher review. Does not replace any governing instruction.

---

## 1. The Question Being Answered

The assessment of `wa_term_phase2_flags` found that 99% of the 1,580 rows in this table are analytically unverifiable. The researcher's question is: what role should these flags play in the programme, and how should they be handled as Session B progresses through each registry?

This document answers that question by examining what the flags were designed to do, how they are currently used in Session B, what the data quality problems mean for that use, and what the correct programme-wide treatment should be.

---

## 2. What the Flags Were Designed to Do

`wa_term_phase2_flags` was designed as a **term-level analytical signal store**. Each row asserts a specific semantic or structural property about a specific term in a specific registry. The 25 flag types cover four broad categories of claim:

### Category A — Analytical properties requiring verse-level validation
These flags assert something about how the term behaves in its verse corpus. They are meaningful only if grounded in verse-by-verse reading.

| Flag | Claim |
|------|-------|
| `GOD_AS_SUBJECT` | God is the subject in at least one verse — verifiable by reading |
| `SOMATIC_INNER_LINK` | Inner state is connected to a bodily organ or physical process |
| `BODY_INNER_EXPRESSION` | Inner state manifests through visible physical behaviour |
| `SOMATIC_EXPRESSION` | Inner state expressed through somatic/body-language patterns |
| `DIVINE_HUMAN_PARALLEL` | God and humans appear as subject in parallel contexts |
| `CAUSATIVE_OF_INNER_STATE` | Term has causative grammatical form (Hiphil/Piel) |
| `VOLITIONAL_COMPONENT` | Carries a dimension of will, choice, or intention |
| `RELATIONAL_DIRECTION` | Inherently directed toward another person, group, or God |
| `METAPHOR_ROOT` | Meaning grounded in concrete physical/sensory metaphor |
| `CROSS_TESTAMENT_SHIFT` | Meaningful semantic shift between OT and NT usage |

### Category B — Corpus distribution properties
These flags make a quantitative or distributional claim about where the term appears. They are verifiable from occurrence data without deep verse reading.

| Flag | Claim |
|------|-------|
| `WISDOM_LITERATURE_CONCENTRATION` | Predominant in Proverbs, Job, or Ecclesiastes |
| `ESCHATOLOGICAL_USAGE` | Predominant in eschatological/apocalyptic passages |
| `HIGH_FREQUENCY_ANCHOR` | 200+ occurrences; primary anchor for semantic field |
| `MULTI_REGISTRY_ANCHOR` | Cross-reference in 3+ registries |
| `SEMANTIC_RANGE_BREADTH` | Term covers 4+ distinct semantic domains |
| `NT_FACULTY_NAMING` | Greek term directly names an inner faculty |
| `ARAMAIC_FORM` | Aramaic form in Daniel/Ezra/post-exilic contexts |

### Category C — Data quality and structural signals
These flags mark data conditions — thinness, structural issues, or programme-state observations. They are partly mechanical.

| Flag | Claim |
|------|-------|
| `THIN_DATA` | Fewer than 5 verse records; dataset too thin |
| `SMALL_VERSE_SAMPLE` | Verse count < 20% of occurrence count |
| `CROSS_PART_ROOT` | Root family spans a split registry part boundary |
| `GENERATION_RESOLUTION_PAIR` | Hebrew-Aramaic or Hebrew-Greek pair resolving to same referent |
| `CONSOLIDATION_CANDIDATE` | Likely to merge with related entry during Session B |
| `DUPLICATE_RESOLVED` | Duplicate entry resolved |
| `NO_WORD_ANALYSIS` | No STEP word analysis data available |

### Category D — Interpretive position flags
These flags assert a programme-level significance about the term that goes beyond its lexical properties.

| Flag | Claim |
|------|-------|
| `THEOLOGICAL_ANCHOR` | Framework A/B intersection term |

---

## 3. How Session B Currently Uses These Flags

Session B's Stage 1 data audit reads `phase2_flags` for every term in the registry block. The instruction says: "List all present." This is the extent of the read — the flags are listed and noted but not interrogated.

Session B Passes 2 and 4 **write** to this table with new flags produced by analytical work:
- Pass 2 (Divine Dimension): writes `FRAMEWORK_SIGNAL` where the divine-human relationship has implications for spirit-soul-body classification
- Pass 4 (Somatic Evidence): writes `SOMATIC_FLAG_RECOMMENDED`, `SPIRIT_SOUL_BOUNDARY`, `BODY_SOUL_BOUNDARY` flags where somatic evidence warrants

Session B also uses this table as one of two mechanisms for recording `GOD_AS_SUBJECT` and somatic properties — the other being `mti_term_flags`. The Reference document notes that `mti_term_flags` is the **authoritative** record for those properties, and that the `wa_term_inventory.god_as_subject` and `wa_term_inventory.somatic_link` fields are redundant and not written by the pipeline.

This creates a three-source situation for the same properties:
1. `wa_term_inventory.god_as_subject` / `somatic_link` — redundant, not written
2. `wa_term_phase2_flags` (GOD_AS_SUBJECT, SOMATIC_INNER_LINK) — written by Session B but also contains unverified bulk data
3. `mti_term_flags` — authoritative, growing as Session B progresses

---

## 4. The Data Quality Problem and Its Consequences

The assessment found that 99% of existing flags have no verifiable analytical provenance. The specific problems and their analytical consequences:

### 4.1 Flags with no reasoning (98.9%)

Without a `description` explaining why a flag was applied, a Session B analyst reading the flag cannot:
- Know whether the claim has been verified against verse data
- Decide whether the flag should inform the current analysis
- Challenge an incorrect flag with analytical evidence
- Know which session made the assertion

A flag without reasoning is indistinguishable from a flag that is wrong.

### 4.2 Bulk import flags (70%)

1,102 flags were applied in a single bulk operation on 2026-03-19 with no per-term justification. This is a pattern recognition operation, not analytical reading. Pattern-matching term glosses and occurrence data can identify candidates for a flag — but it cannot verify that the flag is correct for each term's actual verse corpus. A term with "heart" in its gloss might receive `SOMATIC_INNER_LINK` from a pattern match — but whether the term actually functions that way in its specific verses requires reading those verses.

### 4.3 Flags on deleted and particle terms

341 flags on mti-deleted terms and a handful of flags on grammatical particles (kai, eth, autos, en, al) are straightforwardly wrong. These terms have no inner-being analytical value and their flags corrupt query results.

### 4.4 Internal contradictions (GOD_AS_SUBJECT, CAUSATIVE, SOMATIC)

The PH2 flags and the `wa_term_inventory` fields disagree on properties they both purport to record. Since neither can claim verifiable provenance for most of the data, neither is authoritative — except for the 17 Session B flags and the engine-derived `mti_term_flags` entries.

### 4.5 The compound risk

The greatest analytical risk is not that bad flags exist. It is that **a Session B analyst reading existing flags treats them as established findings, skips re-verification, and builds analysis on unverified assertions**. This risk is active with every pass that reads `phase2_flags` in Stage 1.

---

## 5. The Correct Role of These Flags in the Programme

Having mapped what the flags were designed to do and what state they are in, the correct programme role can now be stated:

**`wa_term_phase2_flags` should function as Session B's term-level analytical signal record — a place where confirmed, verse-grounded properties of terms are recorded for use across the programme. It is not, and should not be, a pre-populated hint system.**

The distinction matters. A hint system says: "this term might have this property — check it." An analytical signal record says: "this term has this property, verified in Session B for this registry, grounded in these verses."

Currently, the table is partially a hint system (the bulk data) and partially an analytical signal record (the 17 Session B flags). These two roles should be separated and the hint material treated appropriately.

---

## 6. Recommended Treatment

### 6.1 Immediate cleanup (CC directive)

The following should be removed without analytical review, as they are unambiguously incorrect:

| Target | Count | Reason |
|--------|------:|--------|
| Flags on `wa_term_inventory.delete_flagged = 1` terms | 159 | Term removed from programme — flag analytically meaningless |
| Flags on `mti_terms.status = delete` terms | 341 | Same — term excluded |
| Flags on confirmed particle/function words (kai, eth, autos, en, al) | ~10 | No inner-being content possible |

This removes approximately 500 rows of demonstrably incorrect data.

### 6.2 Reclassification of bulk and unknown-source rows

The remaining ~1,063 bulk and unknown-source flags should **not** be deleted — but they must be explicitly reclassified from their current implicit-authoritative status to a declared-advisory status. Two mechanisms:

**Option A — Source field update:** Update `source` on all bulk and NULL-source rows to `'ADVISORY_UNVERIFIED'`. This signals to any future session reading these flags that they are unverified hypotheses, not confirmed analytical outputs. No analytical data is lost; the signal is made honest.

**Option B — New column:** Add a `verified` column (INTEGER, default 0) to `wa_term_phase2_flags`. Set `verified = 1` only for the 17 Session B flags. All other rows default to `verified = 0`. Session B's Stage 1 audit then treats `verified = 0` flags as hypotheses to investigate, not properties to accept.

Option B is architecturally cleaner and does not destroy the bulk data. It also enables a clear query: "show me all unverified flags for registry X" as a Session B work list.

**Recommendation:** Option B. The bulk data contains real candidate signals — terms that may genuinely have the properties asserted. The right treatment is not deletion but honest labelling, followed by per-term verification during Session B.

### 6.3 Session B treatment — the verification obligation

Once the data quality is addressed, the correct programme treatment for every existing PH2 flag is as follows:

**During Session B Stage 1 (data audit):**
Read all existing PH2 flags for this registry. For each flag:
- Note the flag code, the term, and whether it is verified (verified = 1) or advisory (verified = 0)
- Verified flags: treat as confirmed. Note them in the observations log. No re-verification required unless the pass analysis contradicts the flag.
- Advisory (unverified) flags: treat as hypotheses. Each one becomes an analytical question for the relevant pass.

The advisory flags effectively become a pre-populated work list for Session B. A `GOD_AS_SUBJECT` advisory flag on a term means: "when reading this term's verses in Pass 2, specifically check whether God is the subject." The flag is not accepted or rejected at Stage 1 — it is noted and deferred to the pass that is competent to evaluate it.

**During the relevant pass:**

| Flag category | Relevant pass | Disposition |
|---------------|--------------|-------------|
| Category A analytical (GOD_AS_SUBJECT, SOMATIC, DIVINE_HUMAN_PARALLEL, CAUSATIVE, VOLITIONAL, RELATIONAL, METAPHOR_ROOT, CROSS_TESTAMENT_SHIFT) | Pass 2 (divine), Pass 4 (somatic), Pass 1 (meaning) | Read the term's verse corpus. Confirm or contradict. Update `verified = 1` and add description if confirmed. If the flag is wrong, set `delete_flagged = 1` on the flag row and write an OT-4 finding explaining the correction. |
| Category B distributional (WISDOM_LITERATURE, ESCHATOLOGICAL, HIGH_FREQUENCY, SEMANTIC_RANGE_BREADTH, etc.) | Pass 1 (meaning), Pass 5 (language) | Verifiable from occurrence data and corpus distribution without deep verse reading. Confirm or correct during the relevant pass. |
| Category C data quality (THIN_DATA, SMALL_VERSE_SAMPLE, CONSOLIDATION_CANDIDATE) | Stage 1 | These are data state observations, not analytical claims. Review against current data. If still accurate, confirm. If stale (e.g. a THIN_DATA flag on a term that now has 20 verses), mark as no longer applicable. |
| Category D interpretive (THEOLOGICAL_ANCHOR) | Pass 1 or Pass 2 | These make programme-level significance claims. Verify analytically before accepting. |

**The closure rule:** Before Session B closes for a registry, every advisory PH2 flag for that registry must have a recorded disposition — confirmed and verified, corrected and flagged for deletion, or explicitly noted as unresolvable within this registry's data (in which case it becomes a candidate for an SD_POINTER if the question it raises has cross-registry implications).

### 6.4 The dual-store problem for GOD_AS_SUBJECT and somatic properties

Currently Session B writes these properties to both `wa_term_phase2_flags` (via Pass 2 and Pass 4 directives) and `mti_term_flags` (the authoritative store per WA-Reference Section 13.3).

This duplication should be resolved. The recommended position:

- `mti_term_flags` is the **authoritative record** for GOD_AS_SUBJECT, SOMATIC_INNER_LINK, and BODY_INNER_EXPRESSION (as already stated in the Reference document)
- `wa_term_phase2_flags` records the **additional analytical properties** that `mti_term_flags` does not cover: FRAMEWORK_SIGNAL, SOMATIC_FLAG_RECOMMENDED, SPIRIT_SOUL_BOUNDARY, BODY_SOUL_BOUNDARY, and the distributional/data quality Category B and C flags
- Session B should write GOD_AS_SUBJECT and somatic flags to `mti_term_flags` only; it should not duplicate them in `wa_term_phase2_flags`

This is consistent with the Reference document's existing position. It resolves the internal contradiction identified in the assessment (Section 5.3 of the assessment) by eliminating the duplication rather than reconciling two unreliable sources.

---

## 7. What Happens to Flags That Cannot Be Verified

Some flags — particularly the Category A analytical flags — can only be verified by reading the term's verse corpus. For registries that have not yet reached Session B, those flags will sit as advisory until their session runs.

This is acceptable. The advisory label makes the status honest. The flags do not corrupt analysis because Session B is instructed not to treat unverified flags as confirmed. They will be verified or corrected as Session B works through the remaining 176 registries.

The `THIN_DATA` flag is a special case. A term flagged as THIN_DATA has fewer than 5 verse records. The thin evidence protocol (obs-schema v2.2 Section 10) applies: if Session B reads this term and the verse corpus is genuinely too thin to support a finding, the finding is flagged, investigated, and either confirmed with supporting evidence or set aside with a recorded investigation note. The `THIN_DATA` PH2 flag is not a reason to skip the term — it is a signal to apply the thin evidence protocol at the outset.

---

## 8. Flags That Reveal a Design Question

Two categories of PH2 flag deserve separate attention because they reveal an unresolved design question about where term-level analytical properties belong in the programme.

### 8.1 The FRAMEWORK_SIGNAL flag

The Session B instruction (Pass 2) directs writing a `FRAMEWORK_SIGNAL` phase2 flag where the divine-human relationship has direct implications for the spirit-soul-body classification. This flag has no equivalent in `mti_term_flags`, no definition in the existing `phase2_flag_types` reference (it is not in the 25 listed codes in the reference document), and no description in any existing flag row. It appears to be a flag type that was added to the instruction but not added to the controlled vocabulary.

This requires resolution: either add `FRAMEWORK_SIGNAL` to `phase2_flag_types` with a proper definition, or retire the instruction step that writes it and use an OT-4 finding in `wa_session_b_findings` instead (which is the richer analytical record).

### 8.2 The SOMATIC_FLAG_RECOMMENDED flag

Similarly, `SOMATIC_FLAG_RECOMMENDED` is written by Pass 4 but does not appear in the `phase2_flag_types` controlled vocabulary in the Reference document. Its purpose is to recommend that a somatic flag be applied in `mti_term_flags` — but this is a workflow note, not an analytical property. If the somatic evidence is confirmed, the `mti_term_flags` record should be written directly. A "recommended" flag that prompts another operation to happen is an intermediate step that belongs in the observations log, not in the database.

---

## 9. Summary of Recommended Actions

| Action | Type | Who | Priority |
|--------|------|-----|----------|
| Delete flags on delete_flagged and mti-deleted terms | CC directive | CC | High |
| Delete flags on confirmed particles (kai, eth, autos, en, al) | CC directive | CC | High |
| Add `verified` column (INTEGER, default 0) to `wa_term_phase2_flags` | Schema migration | CC | High |
| Set `verified = 1` on 17 Session B source flags | CC directive | CC | High |
| Resolve whether `FRAMEWORK_SIGNAL` and `SOMATIC_FLAG_RECOMMENDED` should be added to `phase2_flag_types` or retired in favour of OT-4 findings | Researcher decision | Researcher | Medium |
| Update Session B Stage 1 instruction to treat unverified flags as hypotheses, not confirmed properties | Instruction update | Claude AI | High — before next Session B run |
| Update Session B Stage 1 to include flag verification obligation (confirm, correct, or carry forward) at pass close | Instruction update | Claude AI | High |
| Confirm that GOD_AS_SUBJECT and somatic flags are written only to `mti_term_flags` going forward | Instruction update | Claude AI | Medium |

---

## 10. Open Questions for Researcher

Before implementation, three decisions are needed:

1. **`FRAMEWORK_SIGNAL` and `SOMATIC_FLAG_RECOMMENDED`:** Add to controlled vocabulary in `phase2_flag_types`, or retire and replace with OT-4 findings in `wa_session_b_findings`? The OT-4 findings approach is richer (carries full prose reasoning, entity links, study_segment) but requires the obs-schema schema migration to be in place first.

2. **Advisory flag treatment:** Option B (add `verified` column) is recommended. Confirm before CC implements the schema migration.

3. **Bulk flag scope:** The recommendation is to clean only the demonstrably incorrect rows (deleted terms, particles) and reclassify the rest as advisory rather than delete them. If you prefer a cleaner baseline — deleting all 1,563 bulk and unknown-source flags and rebuilding from Session B alone — that is also a valid position. It means the flags provide no pre-analytical signal at all for the 176 registries not yet in Session B. The trade-off is cleanliness vs. loss of hypothesis material.

---

*For researcher review. No database changes should be made until decisions are confirmed.*
