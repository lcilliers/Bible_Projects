# wa-prose-corpus-assembly-v3-20260422

> Framework B Soul Word Analysis Programme — Programme Prose Corpus Assembly
> Version: v3 (reflects approved state through Area 2, with preamble supersede)
> Date: 2026-04-22
> Previous output: wa-prose-corpus-assembly-v2-20260421 (session prose v1 + v2 draft state)
> Governed by: wa-global-general-rules [current]; wa-prose-style-and-approach-v1-20260422

---

## Status summary

| Macro area | Records | Status |
|---|---:|---|
| Chapter 0 — Preamble | 1 | APPROVED; **supersede pending CC execution** (v3 body under PATCH-20260422-PROSE-PREAMBLE-SUPERSEDE-V1) |
| Chapter 1 — Purpose (Mission; Scope; This Inner-Being Programme; Defining Inner Being; Science and the Bible; Expected Outcome) | 6 | APPROVED — in database, session v1 |
| Chapter 2 — Research Methodology (seven sub-sections) | 7 | **APPROVED by researcher 2026-04-22; pending CC execution** (V2 patch pair) |
| Chapter 3 — Disciplines, tools, evidential principles | — | Not yet drafted |
| Chapter 4 — Data architecture | — | Not yet drafted |
| Chapter 5 — Data integrity and governance | — | Not yet drafted |
| Chapter 6 — Instruction corpus and authority | — | Not yet drafted |

**Total prose corpus (approved through this session):** 14 records across chapters 0–2.

**Approved word count after CC applies all patches:** preamble v3 (465) + chapter 1 bodies (exact counts held in database; sum recorded in session v1 log) + chapter 2 bodies (4,109).

---

## Pending CC execution — patch set

In order:

1. **Preamble supersede** — `wa-prose-preamble-supersede-v1-20260422.json` (PATCH-20260422-PROSE-PREAMBLE-SUPERSEDE-V1)
2. **Chapter 2 handles** — `wa-catalogue-prose-programme-ch2-v2-20260422.json` (PATCH-20260422-CATALOGUE-PROSE-PROGRAMME-CH2-V2)
3. **Chapter 2 bodies** — `wa-prose-programme-ch2-v2-20260422.json` (PATCH-20260422-PROSE-PROGRAMME-CH2-V2)

Step 1 is independent of steps 2–3. Step 2 must precede step 3 (handles must exist before bodies reference them via `section_type_id_lookup`).

---

## Reading order

### Chapter 0 — Preamble (pending supersede)


---

## 0.1 Programme Preamble (v3 — supersede pending)

The programme prose describes the research programme — what it is, how it fits together, and how it operates. It is the programme's narrative description, written to stand on its own: a reader encountering the work for the first time can use it to understand what the programme is, what it produces, and the disciplines by which it operates.

The prose is not the place for instructions on how to perform specific tasks. Procedural content — the exact format of a patch, the step sequence for executing a directive, the completeness tests applied at an inflection point — lives in the instruction documents and the global rules. The prose describes the programme; the instructions direct the work.

The corpus covers six areas. **Area 1** is the programme's purpose — the governing question, how inner being is defined, where this study sits within the researcher's wider work, what a successful outcome would look like, and the relationship between Scripture and contemporary science as the two lenses through which the inner being is studied. **Area 2** is the research methodology — the three building blocks of registry, data collation, and analysis; the six-phase pipeline from word selection to publication; the role of science in the work; the methodological principles that govern every phase; and the constraints the programme deliberately accepts. **Area 3** is the disciplines, tools, and evidential principles by which the programme operates — how findings are distinguished from hypotheses, how the two-AI division of responsibility functions, how memory is managed across sessions. **Area 4** describes the data architecture — the registry, the terms, the verse groups, the dimensional profiles, the question catalogue, and the cross-references that hold them together. **Area 5** covers the governance that keeps the data correct over time — the soft-delete discipline, validation standards, backup regime, patch-failure protocol, and field authority rules. **Area 6** describes the instruction corpus itself: how rules and instructions are versioned, referenced, and updated.

Individual prose records within each area describe specific components in enough detail that a reader can understand the component without leaving the corpus. Where a record points outward to a rule, an instruction, or a schema table, the pointer serves the reader reaching the binding source.

**On style.** The programme's prose is direct and factual. Every sentence is either a statement about the programme or carries information the reader needs. The prose avoids framing that introduces rather than states, motive attribution, rhetorical closings, and metaphors layered on facts. Where the researcher has articulated a principle in their own words, those words are used. Factual claims are traceable to source documents — instructions, the database schema, the Science Framework, the registry construction files. This style carries forward through every sub-section of the corpus and is the reference register for all future prose additions and revisions.


---

## 2.1 Research method

The programme investigates what Scripture reveals about the human inner being. The method proceeds corpus-level from the biblical text, word by word, through a disciplined sequence that separates data gathering from analysis and returns to the full body of findings only once every word has been worked through.

The method rests on three building blocks, in a fixed order. **First, the registry** — a list of English words that name inner-being characteristics, each mapped to the Hebrew and Greek terms through which Scripture expresses it. The registry is built against the programme's working definition of the inner being and is completed before any word is studied. It is the scope: which verses are read, which terms are classified, and which findings the programme produces are all defined by what is in it. **Second, data collation** — for every word in the registry, the programme assembles every verse in which the word or any of its related Hebrew or Greek terms occurs, together with the lexicon data for all those terms. A verse qualifies because the original-language term is present in it, not because a particular reading of the verse has been proposed. Collation is completed for the whole registry before analysis begins. **Third, analysis** — once the data is complete, each word is examined in its full corpus. Similar verses are grouped into characteristic-perspective groups; each group is given an anchor verse that represents it; the groups are assigned to dimensions of the inner being; and each word is then worked through a standing catalogue of questions that interrogate the verse evidence and the lexical data. The answers are persisted in the database and become the findings for that word.

The final step is synthesis. Once every word has been analysed, the findings are read across the corpus to identify interrelationships and impacts between words and concepts at the level of the inner being as a whole. Synthesis does not begin until the per-word analysis is complete.

The sequencing between the three blocks is a methodological commitment. Building the registry before collation means the programme's scope is settled before the evidence is gathered. Completing collation before analysis means the analytical frame is not built from the early words and then imposed on the later ones; every word is read against the same completed corpus of data. Persisting analytical findings into the database — with prior findings discarded each time the data is re-read — keeps findings anchored to the evidence that produced them.

Scripture is the primary lens. The analytical work is work on the biblical text. Contemporary scientific literature on the inner life is held as a second lens, engaged at a defined point in the per-word analysis rather than running in parallel. The reasoning and the operational engagement are described in the sub-section on science in action.

Categories are not imposed on the data; they emerge from it. Dimensions of the inner being are identified by reading the verses and asking what the verses engage. A category that cannot be grounded in verse evidence is not a category the programme uses. A finding that cannot be traced back to a specific verse or lexical source is not a finding the programme records.


---

## 2.2 Word selection and the registry

The programme's scope is the registry of inner-being words. Every word it contains is a word the programme will study; every word outside it is outside the programme's scope. The registry is built against the programme's working definition of the inner being, and that definition is the sole admission criterion.

Registry construction proceeded in four stages.

The first stage was **direct extraction** from prior work. The programme drew on the vocabulary of inner-being characteristics already identified in Framework B, retaining those words where a single Hebrew or Greek term carried the English sense in a lexically direct way. Each modern English word mapped to one or more biblical terms through their standard meanings in the primary lexica. This stage produced the High Confidence list — 75 words.

The second stage was **inferential extension**. A set of modern psychological and conceptual terms — emotion, personality, intuition, manipulation, ambition, among others — names territory that Scripture engages but does not lexicalise under a single matching term. Each entry in this stage carries one of three inference flags. *Inferred* indicates that no biblical term directly translates the modern word, but the closest semantic equivalents have been identified. *Partial* indicates that a biblical term covers part of what the modern word means but not all of it. *Absent* indicates that the concept is present in Scripture narratively but has no single lexical expression. This stage produced the Low Confidence list — 21 words, each carrying its inference flag into subsequent work.

The third stage was **systematic gap analysis**. The first two stages had been shaped by Framework B's prior analytical focus — the distinction between soul and spirit. That focus produced a vocabulary weighted toward the soul-spirit question and under-represented adjacent domains: the cognitive and mental vocabulary, the moral and conscience vocabulary, the relational and social vocabulary. The gap analysis applied the inner-being definition to the full semantic range of biblical Hebrew and Greek, working from the primary lexica — Brown-Driver-Briggs, Köhler-Baumgartner, Bauer-Danker-Arndt-Gingrich, Thayer — and from standard treatments of biblical anthropology. It added approximately 85 words across eight domains: cognitive and mental, volitional, affective and emotional, moral and conscience, relational and social, spiritual and God-ward, character and disposition, and identity and selfhood.

The fourth stage runs continuously during data collation. As STEP retrieval assembles the verse and lexicon data for each registry word, it sometimes surfaces related Hebrew or Greek terms that meet the inner-being definition but were not on the list. A term that satisfies the definition — presence in the original-language text of verses that engage the inner being — is added to the registry. Approximately 30 words have been added through this stage to date. The registry is stable in its boundary criterion but open to evidence surfacing during collation.

Every registry entry carries: Hebrew terms with transliteration, gloss, and sample verses; Greek terms in the same shape; a list of conceptual search terms — alternate English glosses and theological synonyms that support cross-checking; and a STEP Bible search suggestion identifying the landmark verses that seed the analysis.

The active registry stands at approximately two hundred words. The total record count is larger because the registry retains entries that have been excluded on considered grounds rather than deleting them, so the reasoning behind exclusion remains visible and reviewable.


---

## 2.3 Programme flow



### Chapter 1 — Programme purpose

*(Six records approved in session v1; bodies live in the database. See `wa-programme-prose-extract-20260421.json` `bodies_by_id` 2–7 for full text, or regenerate the extract after the preamble supersede applies.)*

1. Mission — `prog_purp_mission`
2. Scope — `prog_purp_scope`
3. This Inner-Being Programme — `prog_purp_this_inner_being_programme`
4. Defining Inner Being — `prog_purp_defining_inner_being`
5. Science and the Bible — `prog_purp_science_and_bible`
6. Expected Outcome — `prog_purp_expected_outcome`

**Style note.** Chapter 1 bodies were produced in session prose v1, before the factual-direct style document was in place. A future session should re-read them against `wa-prose-style-and-approach-v1-20260422.md` and produce any necessary supersedes. The style document's publication preserves the record; the Chapter 1 bodies remain valid prose and are not blocked from use pending the audit.

### Chapter 2 — Research methodology

*(Seven records approved in session v2; bodies pending CC execution of the V2 PROSE patch. Full text follows.)*

The programme moves each word through a defined sequence of six phases. Each phase has an input, an output, and an inflection point that must be satisfied before the word advances. The database records the state of each word at each phase, and the state is what entitles the word to enter the next phase.

**Session A — Term extraction.** For each registry word, Session A assembles the source data: the Hebrew and Greek terms that carry the word's meaning, the full set of verses in which those terms occur, and the lexicon data for every term. The source is STEP Bible. Session A runs in two phases within a single working window — a Phase 1 that produces a source file for researcher verification of the STEP data, and a Phase 2 that produces the database import JSON. Its output is the complete per-word dataset. Its inflection point is import into the database.

**Verse Context — Verse reading and grouping.** Once a word's data is in the database, Verse Context reads every verse in which the word's terms occur. Each verse is filtered for relevance — does it engage the inner being through this term, or is the term present in a sense that falls outside the programme's question? Relevant verses are grouped by contextual meaning. Groups describe what a verse is about — the inner-being characteristic it engages — rather than what the term does within the sentence. The same term can therefore serve different characteristics across its corpus. Each group is given an anchor verse — the citation that represents the group and serves as the primary input to subsequent analysis. Its inflection point is completion of classification for every OWNER term: every verse classified, every group anchored, every word re-exported.

**Dimension Review — Dimensional placement.** The groups produced by Verse Context are read across a cluster of related registries, and each group is assigned a dimension of the inner being. The dimension vocabulary is data-derived — it emerged from the corpus and is refined by continued contact with it. A dimension that cannot be grounded in verse evidence is not a dimension the programme uses. Dimension Review also validates that each group's description remains characteristic-centric and corrects groups formed under an earlier, term-centric model. Its inflection point is the cluster's completion: every active registry with every group dimensioned and locked.

**Session B — Word analysis.** Session B runs the deep analytical pass on each word. Structurally it is two instruction documents — a Readiness phase that establishes the state of the data and the analytical frame, and an Output phase that produces the written analysis. The analytical sequence inside those phases proceeds through ten steps. Steps 1–6 are the biblical pass: semantic characterisation, dimensional placement, divine and somatic dimensions, relational and causative analysis, anchor-verse work. Steps 7–8 are the scientific pass. Steps 9–10 are the integrating synthesis. Every finding is substantiated by data in the database, and every answer is persisted there. On re-analysis, prior findings are set aside and the data is read freshly. Its inflection point is a word whose analysis is closed — every standing question answered, every finding traceable to evidence.

**Session C — Publication.** Session C produces the reader-facing written study for each word. It reads from Session B's analytical record and presents the word in a form the reader can work with. Session C is produced one word at a time. A word's publication depends on its analysis being closed.

**Session D — Cross-registry synthesis.** Session B raises SD pointers — structural observations and questions that implicate other registries — and records them in the database. Session D begins from the accumulated SD pointer record. It groups related pointers across registries, formulates specific investigation questions, requests targeted database queries from Claude Code to retrieve evidence, performs cross-registry analysis against that evidence, and produces synthesis findings. Session D is the interpretive, synthetic, and constructive phase of the programme.

The database carries each word's state between phases. A session is a span of work on words that are ready for that phase; work can be taken up at whatever point the database shows it left off.


---

## 2.4 Science in action

The relationship between Scripture and contemporary science is described conceptually in the sub-section on science and the Bible. This sub-section describes the operational consequence: how the scientific lens is engaged within the programme's work, at what point, and through what instrument.

The governing premise is the second-lens position. Scientific literature relevant to the inner being is vast — psychology, neuroscience, physiology, behavioural science, developmental and cognitive psychology, and evolutionary biology each address territory the programme's corpus covers. Treated as a co-equal research programme, the scientific material would demand a second corpus-level effort matching the biblical one in scope and rigour. The programme does not attempt this. It requires representative and reliable coverage of the landmark findings in each relevant field, held alongside the biblical analysis as the second lens through which the same territory is read.

**When science enters the work.** Scientific engagement happens during Session B and is sequenced after the biblical pass is complete. Steps 1–6 of Session B's analytical protocol are the biblical pass — semantic characterisation, dimensional placement, divine and somatic dimensions, relational and causative analysis, anchor-verse work. Steps 7–8 are the scientific pass. Steps 9–10 are the integrating synthesis. The sequencing is a methodological commitment. Running the two passes simultaneously risks the scientific frame distorting the biblical reading before the biblical analysis is complete, particularly for words where the scientific literature is substantial (shame, fear, grief, and comparable affective territory).

**The three-question structure.** The scientific pass proceeds through three questions. First, what is the primary scientific field for this word? Second, what are the landmark findings in that field for this characteristic? These are the settled, well-replicated observations that researchers in the field would cite — not a literature review. Third, where does the scientific finding engage the biblical analysis? One substantive paragraph per word, identifying the specific point of convergence or divergence. The third question is the analytical work of the pass; the first two are preparation for it.

**The six scientific fields.** The programme works with six fields.

- *Neuroscience* — body-soul boundary and somatic dimension. Neural correlates of inner states, the brain-body connection, how emotion is implemented biologically.
- *Clinical and social psychology* — soul operations. Emotion theory, attachment, moral psychology, shame and guilt research, the psychology of will, motivation, and virtue. Most Session B words draw on this field.
- *Physiology and epigenetics* — body circle and generational transmission. Stress physiology, the HPA axis, the bodily expression of grief and joy, the inheritance of patterns across generations.
- *Behavioural science* — relational circle. How inner states express in behaviour and social context, how cooperation and competition shape inner life, the social functions of emotion.
- *Developmental and cognitive psychology* — cognitive circle and the formation of character. How cognitive capacities develop, moral development, conscience, executive function and self-regulation, character formation.
- *Genetics and evolutionary biology* — the created endowment. What is built into the human creature by nature, the heritability of temperament, the evolutionary origins of social emotions, the genetic basis of empathy and conscience.

Most words have a clear primary field; some span two. Field assignment is made at the head of the scientific pass.

**The reference shelf.** The scientific pass uses a curated reference shelf — a set of foundational texts and landmark papers organised by field, chosen for breadth of coverage against the corpus. The shelf is not a reading list to complete before analysis begins; it is consulted during the scientific pass of each word. Where the shelf carries a text of high relevance to the word being analysed, that text is the primary scientific reference for the session. Where a word falls outside the shelf's coverage, a targeted search fills the gap. A recurring gap across multiple words signals that the shelf should be extended.

**The no-database decision.** The programme does not build a structured scientific database to match its biblical database. Three reasons. A parallel scientific database at the depth of the biblical one would constitute a second programme of comparable scale and would defer synthesis. The data types are not structurally equivalent: biblical data is lexical and classifiable, while scientific findings are arguments, observations, and interpretations that require judgement to apply. And the programme does not need it — the second-lens role is served by the reference shelf.

**Convergence and divergence.** The analytical work of the scientific pass is organised by a framework that distinguishes three kinds of convergence and three kinds of divergence. Convergence can be phenomenological — the two accounts describing the same experience from different angles. It can be mechanistic — science describing the mechanism of what Scripture describes as a reality. It can be structural — the architecture of the inner life having the same shape in both accounts. Divergence can be register divergence — the accounts addressing different levels of the same reality and only appearing to conflict. It can be reductive divergence — a scientific account that reduces the inner-being characteristic to its biological substrate and loses dimensions the biblical account treats as primary. It can be genuine divergence — claims in actual tension that cannot be harmonised by reframing. Genuine divergence is flagged for the cross-registry synthesis phase rather than resolved at the word level.

**What the pass produces.** The output of the scientific pass for each word is a concise annotation: the primary field, the two or three landmark findings drawn on, and the paragraph identifying the convergence or divergence with the biblical analysis. The annotation is carried into the word's Session B record and appears in the published word study.


---

## 2.5 Publishing

Publishing is the output side of the pipeline: the production of documents that carry the programme's findings to its audience. The programme produces three orders of published output.

The first order is the **per-word study**. Each word in the registry receives a written study produced at Session C. The study is the reader-facing form of the word's analytical record: what the term means across its Hebrew and Greek originals, how its occurrences distribute across Scripture, what contexts and characteristics the verses reveal, how the term engages the spirit-soul-body continuum, and how the biblical analysis relates to the relevant scientific findings. The per-word study is designed to stand alone: a reader encountering a single study, without having read any of the others, gets a complete treatment of that word.

The second order is the **cross-word synthesis**. Once a cluster of related words has been studied individually, Session D reads across them and produces the synthesis findings that single-word studies cannot carry: interrelationships between words, patterns that run across a group of words, and impacts of one characteristic on another at the level of the inner being as a whole. Syntheses are produced when the per-word studies for their cluster are complete.

The third order is the **programme-level account**. When clusters have been worked through and their syntheses produced, the programme's description of the human inner being becomes assemblable — built from the bottom up, word by word. The present prose corpus is part of this third-order work: the self-description that makes the programme's structure and findings readable as a whole.

Publishing in this sub-section means the production of readable documents that carry the programme's findings. It does not mean commercial publication, external release, or any particular distribution channel. The documents produced at Session C and Session D are the programme's published output regardless of how they are subsequently made available externally. Publication decisions of the external kind are outside the programme's methodological scope.

The analytical record — the per-word findings held in the database — is the research. The published studies are the form in which the research reaches the reader. The database carries the full set of answers to the standing catalogue of questions for every word; the published study is a curated presentation of that record. Where a reader's question is more specific than the published study's treatment, the database supports the deeper look.


---

## 2.6 Key methodological principles

The method rests on nine principles. They govern every phase of the work.

**Registry completeness against the inner-being definition.** The scope of the study is defined by a word list built against the programme's working definition of an inner-being characteristic, and the list is as complete as the evidence permits before any word is studied.

**Data collation is separated from analysis.** The full data for every registry word is collated before analytical work begins on any of them. Every word is read against the same completed body of data.

**Words are not forced into preconceived categories or assumptions.** Dimensions of the inner being are identified from the verse evidence; groups are formed from what the verses engage; findings emerge from the questions applied to the data. A category that cannot be grounded in verse evidence is not a category the programme uses.

**Verses qualify by original-language occurrence, not by interpretation.** A verse is included in a word's corpus because the relevant Hebrew or Greek term is present in it, irrespective of what contribution or meaning the verse may have. This is the same criterion that admits a word to the registry: lexical presence, not interpretive fit.

**Every finding is substantiated by data — no guessing, no assumptions, no made-up results.** A finding is a statement that can be traced back to a specific verse, a specific term, or a specific pattern in the evidence. A statement that cannot be so traced is not a finding the programme records.

**Analysis reads the data as a whole; it does not pick and choose angles.** The analytical work for each word runs through a standing catalogue of questions that every word is worked through in the same way. The catalogue is applied in full. A word's answer to every question is part of its record.

**The database is the analytical memory.** Every answer to every question is persisted in the database, and the database is where the word's findings live. When re-analysis occurs, the prior finding is set aside and the data is read freshly; the new finding replaces the old in the database.

**Biblical lens primary, scientific lens secondary.** Scripture is the primary lens; science is the second lens. The biblical pass is completed before the scientific pass begins, at each word. The operational consequences are described in the sub-section on science in action.

**Synthesis follows analysis — bottom-up, not top-down.** Cross-word synthesis is produced after the per-word analytical work for those words is complete. The programme-level account is produced when the cluster-level syntheses have been completed.

The nine principles are not independent. Building the registry against a definition makes a complete collation meaningful. Completing collation before analysis makes inductive reading possible. Inductive reading makes the catalogue of questions applicable as a uniform instrument. Uniform application makes the database a neutral record of findings. The database supports re-analysis on the same footing as original analysis. Re-analysis on a stable footing makes cross-word synthesis possible.

A word can be revisited at any point by returning to any stage of the pipeline and processing all subsequent stages in sequence. A new Verse Context grouping re-runs Dimension Review, Session B analysis, Session C publication, and feeds Session D synthesis for that word. The database is the final authority of the data and the analysis. Because the data read at re-run is the same data the prior run read, and because the discipline discards the prior finding and reads the data freshly, the re-run arrives at the same result as the prior run. The method is reproducible.


---

## 2.7 Key constraints

The principles described in the preceding sub-section shape how the programme works. The constraints described here shape what the programme does not attempt.

**Scope is bounded by the registry.** The programme studies the words in the registry and does not study other vocabulary. Registry membership is open to evidence surfacing from within the corpus, as described in the sub-section on word selection. It is not open to interpretive expansion from outside it.

**The scientific lens is bounded by the second-lens decision.** The programme does not engage scientific literature at the depth of its biblical engagement. The scope of scientific engagement is set by the three-question structure, the reference shelf, and the per-word annotation, described in the sub-section on science in action. The reasons are practical (the scale of a parallel corpus-level effort), methodological (the data types are not structurally equivalent), and structural (the programme is biblical research, with science as the second lens).

**No structured scientific database.** The programme does not build a structured scientific-literature database alongside its biblical database. Scientific findings are carried in Session B's written record and in the reference shelf. The database holds the biblical research.

**Synthesis does not run ahead of its evidence.** A per-word study is produced when its analytical work is complete. A cross-word synthesis is produced when the studies for its cluster are complete. A programme-level account is assembled when the cluster syntheses are complete. Larger claims are not made before the smaller claims on which they rest.

**The programme is corpus-level, not survey-level.** Each word in the registry receives a full analytical treatment: every verse read, every term classified, every standing question answered. The programme does not treat its subject at survey level.

**No per-word publication before analytical closure.** A word's published study is not produced before its analysis is closed. Prior findings are set aside on re-analysis and replaced with current readings; a published study produced ahead of analytical closure would carry a retraction risk.

**Registry membership is not reopened on interpretive grounds.** Once a word has been admitted to the registry under the inner-being definition, it is not re-examined for admission because a particular interpretive frame would exclude it, or because the analytical work on it has produced findings that conflict with a current reading. A word's membership is a matter of the original-language evidence that admits it. Where analytical findings raise a definition-level question — what the inner being is, where its edges are — that question is handled at the level of the definition, not by editing the registry.



---

## Close-out notes

**Style reference.** The corpus follows the style described in `wa-prose-style-and-approach-v1-20260422.md`. Every future prose addition, supersede, or revision is checked against that document. The preamble v3 (when superseded) carries an explicit style statement as its closing paragraph, so readers of the corpus understand the register from the first page.

**Outstanding for future sessions:**

1. **Chapter 1 style audit.** Chapter 1 bodies were drafted under the earlier Claude AI working style. A style-audit pass (analogous to what was applied to Chapter 2 in this session) should produce supersedes where material padding is found.
2. **Chapter 3 drafting.** Disciplines, tools, evidential principles — the operational disciplines that Chapter 2's "key principles" sub-section does not cover.
3. **Chapter 4 drafting.** Data architecture — registry structure, terms, verse groups, dimensional profiles, cross-references, question catalogue.
4. **Chapter 5 drafting.** Data integrity and governance — soft-delete, validation, backup, patch-failure protocol. The M34 seed records 29 and 33 (validation standard, patch failure protocol) and `prog_field_authority` find their home here.
5. **Chapter 6 drafting.** Instruction corpus and authority — versioning, reference discipline, instruction authority structure.
6. **Macro-area framing paragraphs.** Short bodies at the head of each of chapters 1–6, written after all sub-sections are complete.

The order above is a default, not a binding sequence. The next session may justify a different priority on evidence at session-start.
