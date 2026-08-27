# Session C — Writing Style and Structure Analysis Report
**File:** wa-sessionC-analysis-report-v1-2026-04-13.md  
**Date:** 2026-04-13  
**Purpose:** Assess five final word study documents and their corresponding database extracts against the intended purpose of the programme, as described by the researcher.  
**Documents reviewed:** grace (v4), mercy (v2), compassion (v3), love (v3), forgiveness (v3)  
**Database extracts reviewed:** grace, mercy, compassion, love, forgiveness (incomplete)

---

## 1. The Intended Architecture (as stated)

Before assessment, the governing principles stated by the researcher:

- The **database is the single source of truth**. Every analytical finding must be a database record. The prose document is a rendering of the database, not an independent artefact. It must be possible to re-read the database in six months and regenerate the same prose.
- **Session C** tells the story of a single word for a general reader. It is a first draft.
- **Session B** validates and enriches the database — structured records, not prose. The prose is updated to reflect what is now in the database.
- **Session D** works across words using the database. Its quality depends entirely on what Session B has left behind.
- The intended six-section structure:
  1. Synopsis — short entry point
  2. What the characteristic is — full description
  3. What it does / how it works — the dynamic
  4. How it operates in the Bible — verse evidence
  5. The original language vocabulary
  6. Connections and interrelationships — placeholder pending Session D

---

## 2. Section Structure — Observation

The five final documents show three different section naming conventions and two different conceptual structures.

**Grace, mercy, forgiveness (and fellowship):** Sections 1–5 follow the original Session C instruction numbering — Section 1 Word Characteristic Summary, Section 2 Word Impact Description, Section 3 Annotated Verse Evidence, Section 4 Original Language Vocabulary, Section 5 Connections.

**Compassion:** Sections renamed to plain language — Section 1 The Characteristic, Section 2 How It Works, Section 3 The Verses, Section 4 The Vocabulary, Section 5 Connections. No version label in the header. No Session 6 completion note visible in the final document.

**Love and forgiveness (final versions):** The section *names* in the instruction (Word Characteristic Summary, Word Impact Description, etc.) have been dropped. Love uses sub-headings within Section 3. Forgiveness abandons the section numbering entirely — the sections are titled What Forgiveness Is, How Forgiveness Works, The Biblical Evidence, The Language of Forgiveness, Connections and Open Questions.

**Observation:** The section names in the instruction do not match the intended use as described by the researcher. The researcher described: (1) synopsis, (2) full description, (3) what it does/how it works, (4) verse evidence, (5) vocabulary, (6) connections. The instruction maps these differently — Section 2 is Word *Impact* Description, Section 3 is Verse Evidence, Section 4 is Vocabulary. Compassion's plain-language headings (The Characteristic, How It Works, The Verses, The Vocabulary) are closer to the researcher's description than the instruction's headings, but the section order differs from what the researcher described. Forgiveness's approach (abandoning numbers entirely) produces the most readable document but is the least replicable.

---

## 3. Writing Style — Observation

**Grace (v4):** The most complete document in analytical terms. Sections 1 and 2 are well-written reader-facing prose with genuine insight. Section 3 is extensive and intellectually rich. Section 5 is the most developed connections section in the set. However, sections 1 and 2 carry substantial analytical content — four-form taxonomy, detailed structural observations — that belongs in the database rather than in a synopsis. The prose reads more like a research summary than a story.

**Mercy (v2):** Sections 1 and 2 are strong reader-facing prose — the best balance in the set. Section 3 is very long (sub-headed thematically) and contains explicit programme-internal references ("XREF term anchor verses... belonging to terms owned by registries 23-compassion..."). Section 4 is detailed and technical. The word "registry" appears in the closing line of Section 3 — visible to a reader. Section 6 header is present.

**Compassion (v3):** The most complete and polished document in writing quality. Sections 1 and 2 read as genuine prose essays — flowing, accessible, substantive without being technical. Section 3 uses term-by-term sub-headings which differ from the instruction but works effectively for a reader. Section 4 (The Vocabulary) is the best vocabulary section in the set — genuinely informative without being a glossary. **This is the closest to the intended general reader standard.** However, compassion uses section names that differ from all other documents.

**Love (v3):** Sections 1 and 2 are good. Section 3 has a placeholder note ("requires Pass 2 detailed read of anchor verses") left in the document — a process artefact that was never removed. The duplicate Section 3 heading was identified earlier and remains in the final version. Section 5 is the most systematically structured connections section. Technical notation is well-controlled.

**Forgiveness (v3):** The most radical departure from the instruction format, but arguably the most successfully reader-facing document. The section titles (What Forgiveness Is, How Forgiveness Works, The Biblical Evidence, The Language of Forgiveness, Connections and Open Questions) are intuitive and serve a general reader well. There is no programme-internal language visible to a reader. This document would read naturally as a book chapter. It is the best evidence of what the prose should eventually become.

---

## 4. The Section Intent — Gap Analysis

Mapping the researcher's stated intent to what the documents actually contain:

| Intended section | Researcher's description | What the documents contain |
|---|---|---|
| Section 1 | Synopsis — short entry point | Grace/mercy: 300–400 words of analysis. Compassion: ~400 words but reads as a genuine synopsis. Forgiveness: ~400 words but flows as an introduction. No document is truly synopsis-length. |
| Section 2 | What the characteristic is — full description | Grace: structural taxonomy (four forms). Mercy: good full description. Compassion: this becomes Section 2 (How It Works) — the *what it is* is in Section 1. Love: good. Forgiveness: absorbed into Section 1. |
| Section 3 | What it does / how it works | Most documents place verse evidence here, not the working dynamic. Compassion places the working dynamic in Section 2. Forgiveness places it in Section 2 (How Forgiveness Works). |
| Section 4 | How it operates in the Bible — verse evidence | Grace/mercy/love place verse evidence in Section 3 (matching the instruction), not Section 4. |
| Section 5 | Original language vocabulary | All documents place vocabulary in Section 4, not Section 5. |
| Section 6 | Connections | All documents place connections in Section 5, not Section 6. |

**Finding:** The researcher's stated section structure (1 synopsis, 2 full description, 3 how it works, 4 verse evidence, 5 vocabulary, 6 connections) does not match the current instruction's section structure (1 summary, 2 impact, 3 verse evidence, 4 vocabulary, 5 connections, 6 internal note). They are offset by one section in the middle and have different conceptual intent. The forgiveness and compassion documents have implicitly moved toward the researcher's intended structure without it being formally stated in the instruction.

---

## 5. The Database — Observation

This is the most critical finding in the analysis.

**What is in the database for all five words:**
- `session_b_status`: Analysis Complete ✓
- `sb_classification`: Assigned for all five ✓
- `sb_classification_reasoning`: Assigned for all five ✓
- `dim_review_status`: Complete for all five ✓
- SD pointers: Present — grace 50, compassion 29, love 28, forgiveness 22, mercy 15 ✓

**What is NOT in the database:**

`session_b.findings`: Each word has only 1–2 findings, all of type DIMENSION_REVIEW. These contain short analytical notes about specific dimension review observations. They do not capture the analytical content of the word studies.

`mti_term_flags`: **Zero** for mercy, compassion. Six for grace, eleven for love, not checked for forgiveness. The prose documents contain rich somatic analysis, god-as-subject identifications, and other analytical observations — but the flag mechanism that should record these as structured database records is largely empty.

`god_as_subject`: Mercy has 0 terms flagged despite the prose document being full of God-as-subject analysis. Compassion has 0 despite extensive divine compassion content. The flag mechanism exists but has not been written to.

`somatic_link`: Mercy has 0, compassion has 0. Both documents contain detailed somatic analysis (womb imagery, bowel-movement vocabulary, prostration). Not in the database.

`evidential_status`: Not set on any term across any word. This field is described in programme notes as the one Session B output that materially gates programme-wide Session D synthesis quality.

`session_b.dimensions`: Null for all five words. The dimension analysis is complete (dim_review_status = Complete) but the Session B dimensions field is empty.

**The core problem stated plainly:** The prose documents contain extensive analytical content — somatic observations, divine-subject patterns, semantic structure analysis, causal chains, structural arguments. None of this analytical content exists as structured database records. It exists only in prose. If the prose were deleted, Session D would have the SD pointers and the sb_classification — and nothing else. The database cannot regenerate the prose. The prose and the database have diverged.

---

## 6. What Happened — Interpretation

Session B was designed to enrich the database and update the prose to reflect the database. What actually happened is the reverse: Session B enriched the prose and did not write the analysis to the database. The session_b.findings table, the mti_term_flags mechanism, the god_as_subject flags, the somatic_link flags, the evidential_status field — all exist in the schema for exactly this purpose, and all are largely empty after five completed Session B runs.

The SD pointers are present and well-populated — this is the one database output that Session B reliably produced. The sb_classification and reasoning are recorded. But these are the outputs that the closing patch and SD pointer patch mandated. The analytical content that was not mandated by a specific patch step was written to prose and not to the database.

This is not a writing quality problem. It is a process architecture problem: the instruction does not have a mandatory step that requires every analytical finding — somatic observation, divine-subject identification, semantic structure note, causal chain — to be written as a structured database record before it appears in prose. The prose was the path of least resistance; the database write-back was the harder, slower path with no hard gate requiring it.

---

## 7. Writing Style Drift — Observation

The researcher noted that writing style has drifted toward AI language and away from the general reader. The evidence:

**Specific examples of internal language remaining in final documents:**

- Mercy Section 3 closing: *"XREF term anchor verses (belonging to terms owned by registries 23-compassion, 103-love, 68-grace...)"* — programme-internal vocabulary in a reader-facing document.
- Love Section 3: *"[Section 3 follows — requires Pass 2 detailed read of anchor verses. See observations log for progress.]"* — a process placeholder left in the final document.
- Grace Section 1 uses "four forms" taxonomy which reads as a classification scheme rather than a description. Words like "spirit level," "inner-being condition," and "relational domain" appear in what should be plain reader prose.
- Mercy Section 4 uses vocabulary like "phase 2 flags confirm" and "SEMANTIC_RANGE_BREADTH flag" in the prose — not fully removed.
- Multiple documents reference "the research" or "the data" as the authority — which reads as programme-internal framing.

**The writing quality in the best sections** (compassion Sections 1, 2, 4; forgiveness throughout; mercy Section 1) demonstrates that the intended general reader standard is achievable. The problem is not that the programme cannot produce good prose — it is that the clean-up discipline (removing all internal programme language) was not consistently applied, and the analytical tendency to classify and taxonomise ran ahead of the storytelling tendency.

---

## 8. Summary of Issues for Researcher Decision

**Issue 1 — Section structure mismatch.** The instruction's section structure does not match the researcher's stated intent. A decision is needed on whether to update the instruction to reflect the intended six-section structure, or to clarify that the current structure is correct and the researcher's description was informal.

**Issue 2 — Section naming inconsistency.** Five documents use four different section naming conventions. A single standard is needed and should be written into the instruction.

**Issue 3 — Word count specification.** The 230–270 word target for Sections 1 and 2 has never been met. The actual standard established in practice for well-written documents is approximately 350–500 words for a synopsis-level section and 400–600 words for a full description section. The spec should reflect practice or be enforced.

**Issue 4 — Database write-back gap.** The analytical content of Session B lives almost entirely in prose. The database is largely empty of structured analytical findings beyond SD pointers and sb_classification. This is the most significant technical issue in the programme. Without a mandatory database write-back discipline, Session D will work from correlation signals and SD pointers only — missing the analytical substance of the Session B work.

**Issue 5 — Internal language in final documents.** Stage 3b (Publication Review — stripping all internal programme language) was not applied consistently. Several final documents contain programme references visible to a reader. A clean final editorial pass is needed on grace, mercy, and love.

**Issue 6 — Process artefacts in final documents.** Love contains a placeholder note ("requires Pass 2 detailed read"). This must be removed.

**Issue 7 — Compassion section names.** Compassion uses plain-language section names that differ from all other documents. Either standardise to compassion's approach (which is closer to the researcher's intent) or standardise to the instruction's approach.

**Issue 8 — General tone.** The best documents (compassion, forgiveness) demonstrate the intended tone. The others, particularly grace (v4), are more analytical and taxonomic than narrative. The distinction is not about depth of content but about voice: the reader should be drawn into the story of the word, not presented with a classification of it.

---

## 9. What Is Working Well

This is not only a list of problems. Several things are working well and should not be lost:

- The **analytical quality** of the best sections (compassion, forgiveness) is genuinely excellent — substantive, grounded, accessible.
- The **SD pointer discipline** is well-established — all five words have meaningful Session D flags in the database.
- The **sb_classification** is assigned and reasoned for all five words.
- The **forgiveness document** is very close to the intended final form — it could serve as the new reference model for the prose register.
- The **compassion vocabulary section** (Section 4 / The Vocabulary) is the programme's best example of how vocabulary analysis should read.
- The **connection questions** across all five documents are genuinely analytical — they are asking the right questions for Session D.

