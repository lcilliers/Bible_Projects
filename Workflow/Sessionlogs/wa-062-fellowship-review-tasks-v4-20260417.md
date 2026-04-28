# WA — Fellowship Analysis Output Review — Task Log
**Registry 062 (fellowship) — Review of Session B Analysis Output prototype run, with rewrite programme for Analysis Output instruction**

| Field | Value |
|---|---|
| Filename | wa-062-fellowship-review-tasks-v4-20260417.md |
| Date opened | 2026-04-17 |
| Version | 4.0 |
| Status | Open — instance tasks held; rewrite programme (Tasks 7–12) defined and ready for execution across multiple sessions |
| Supersedes | wa-062-fellowship-review-tasks-v3-20260417.md |
| Prior output | Supersedes v3. Instance tasks (1–6) carried forward unchanged. Rewrite programme (Tasks 7–12) added in this version following researcher direction that (a) methodology stands as conceptually sound and does not need redesign; (b) the failure was in delivery, cross-checking, safeguarding, memory management, and procedural compliance; (c) AI freedom of choice in procedural matters is the root cause and must be removed while analytical freedom is preserved and expanded; (d) the programme's 214-word horizon over approximately a year requires mechanical cross-word consistency; (e) the rewrite must be executable section by section across multiple sessions, which means this task log must carry complete context. Companion file: wa-062-fellowship-review-sessionlog-v1-20260417.md (deliberation record). |

---

## Change log

**v4.0 (20260417):** Major restructure. Task log reorganised into three strata:
- **Part A — Foundation**: diagnosis, governing principle (Task 7), analytical/procedural glossary, inherit list, rewrite list, worked examples, how to use this log.
- **Part B — Application principles**: Tasks 8–11 (completeness, coverage, safeguarding, memory), each stated as a principle that applies across multiple sections of the instruction.
- **Part C — Per-section rewrite sub-tasks**: Task 12 expanded into one sub-task per section of Analysis Output v1.1. Each sub-task is bounded, executable in one session, and carries its own self-check.

Tasks 1–6 (instance failures and prevention proposals from v3) are carried forward in Part D unchanged. The rewrite programme (Tasks 7–12) is the major addition. Context captured separately in the companion session log (wa-062-fellowship-review-sessionlog-v1-20260417.md) so that a future session picking up a single sub-task has both the prescriptive artefact (this log) and the reasoning record (session log).

**v3.0 (20260417):** Tasks 4, 5, 6 added covering discrepancies surfaced during Q&A three-way comparison.

**v2.0 (20260417):** Task 1 amended. Tasks 2, 3 added (re-export failure; sub-stage verification and download discipline).

**v1.0 (20260417):** New task log opened. Task 1 added (Units 7/8/9 missing from observations log).

---

## How to use this task log

This log is designed to be used across multiple sessions without requiring the conversation that produced it to be reconstructed. It is the prescriptive artefact. The companion session log (wa-062-fellowship-review-sessionlog-v1-20260417.md) is the reasoning record — read it if you need to understand why a task is worded as it is.

**To execute a single rewrite sub-task:**
1. Read Part A (Foundation) in full — once. It establishes the principle and the distinctions the rewrite must honour.
2. Read Part B (Application principles) in full — once. It explains how the principle applies to the four delivery themes.
3. Pick one sub-task from Part C. Read that sub-task only, plus the Analysis Output v1.1 section it governs.
4. Rewrite that section. Apply the self-check that ships with the sub-task. Produce the rewrite as a standalone artefact that can later be composed into the full instruction.
5. At session close, record what was completed, what is outstanding, and what the next session should attach.

**To plan the overall rewrite:**
Read Parts A, B, and the sub-task summary table at the start of Part C. The summary table shows what each sub-task produces and which sub-tasks are prerequisites for which.

**To audit a rewritten section:**
Read Part A to establish the test. Read the sub-task that governed the rewrite. Apply the self-check from the sub-task. If any self-check item fails, the rewrite is not complete.

---

# Part A — Foundation

## A.1 Diagnosis: why the fellowship run failed and why the instruction must be rewritten

The fellowship Session B Analysis Output run produced outputs that failed on nine distinct grounds, enumerated in Tasks 1–6 (Part D). A complete listing is:

1. Stage 2a Units 7, 8, 9 declared complete in the Progress Record but not written to the observations log.
2. A re-export asked to verify completeness did not catch the gap and added Stage 2B Q&A content citing the missing Unit 7 as evidence.
3. Session log summary numbers (28 Q&A pairs processed, 17/4/7 distribution) do not match the observations log (20 Q&A pairs, 15/2/2/1 distribution).
4. Q&A partitioning cherry-picked Q001–Q015, Q017, Q020, Q026, Q051, Q076 from the 194-question catalogue instead of walking sequentially.
5. Type (b) patch did not produce `wa_finding_catalogue_links` insert operations for any finding.
6. Type (b) patch did not produce `wa_finding_entity_links` insert operations for any finding.
7. No SPIRIT_SOUL_BODY finding produced (Closure Domain B requires count = 1).
8. No MEANING_OBSERVATION finding produced (Closure Domain B requires count > 0).
9. Stage 2a proceeded without a Stage 1 Completion Record, under a self-declared "prototype exception" that has no basis in the instruction — which explicitly states "If not present: stop."

These nine failures are not independent. They share a single mechanism: the session made procedural decisions in the moment — to skip writing, to accept a re-export without verifying, to summarise from memory, to select questions from the catalogue, to omit link inserts, to declare a prototype exception. The instruction said something else in each case. The session decided otherwise.

The conceptual plan for Analysis Output was developed over days of prior work and is sound. The failures are not conceptual. They are operational: delivery, cross-checking, safeguarding, memory management, and doing what the instruction requires.

**Why this matters beyond fellowship.** The programme has 214 words to process over approximately one year. Five prior words have already been processed under the earlier Session B instruction; each was sound in its own right but the set was inconsistent — different approaches, different coverage, different emphasis. The set of 5 was unfit to bundle. A set of 214 cannot be re-run to fix inconsistency. Consistency must be produced on the first pass, and it must be produced mechanically because no discipline applied across months of sessions by multiple session instances will otherwise hold.

The upstream infrastructure already enforces input consistency: Analysis-Readiness is a strict data-validation step; the single database prepares data identically for every word; the catalogue tests every word against the same completeness standard. The final step where consistency can still be lost is Analysis Output. Fellowship has shown that it is.

The rewrite's purpose is to close that gap — to make Analysis Output produce artefacts of identical shape and complete coverage across all 214 words, regardless of session, word complexity, or session instance.

---

## A.2 Task 7 — Governing principle for the rewrite (three claims)

The rewrite is governed by three claims, each equal in weight. No rule drafted in the rewrite may contradict any of them. No section is complete until it has been tested against all three.

### Claim 1 — Analytical depth is unrationed and maximal

The session uses the full validated data to produce the deepest analysis the data supports. Observations, narratives, stitched connections, cross-registry patterns, dimensional characterisations, spirit-soul-body classifications — all are produced at the depth the data supports, not at a depth rationed by catalogue length, session budget, or procedural convenience.

The catalogue does not cap analytical depth. The catalogue is a completeness validator applied to a completed analysis. A word like love, with 120+ catalogue questions and multi-page analytical material, receives an analysis of corresponding depth — not a truncation of that depth to fit 120 Q&A slots. Where the data supports more than one finding of a given type, more than one is produced. Where the data supports a cross-registry connection not yet named in existing SD pointers, the session names it. Minimum-count rules in the closure checklist ("at least one MEANING_OBSERVATION") are floors, not caps.

This claim exists because the programme uses AI specifically for analytical judgement on validated data. A rewrite that constrains this destroys the programme's value. The purpose of the rewrite is to protect and expand analytical freedom by eliminating the procedural drift that currently distracts from it.

### Claim 2 — Procedural choice is removed

Every procedural step in the rewritten instruction is mechanical. No procedural decision may be made by the session in the moment.

"Mechanical" means: a named read from a named file, a named write to a named file, a named count of items in a named file, a named check against a named literal. Every procedural statement in the rewrite takes one of these forms. Wording such as "determine", "assess", "use judgement", "as appropriate", "if relevant" — which in v1.1 appear in procedural contexts — are converted to prescriptive form: "read", "count", "write", "compare".

The session does not decide: which question to process next (the catalogue walks in file order); whether a sub-stage is complete (the sub-stage sign-off artefact makes the answer literal); whether the summary numbers are right (they are derived by a re-read of the source file); whether a required artefact can be skipped (the coverage check enumerates every required artefact and requires each to exist); whether an exception applies (there are no session-declared exceptions — only researcher-decided exceptions recorded per GR-RD-001 through GR-RD-006).

This claim is specifically aimed at the failure pattern diagnosed in A.1. Every one of the nine failures was a procedural decision. The rewrite makes them mechanically impossible rather than discouraged.

### Claim 3 — Produced artefacts are identical in shape across all 214 words

The rewrite produces artefacts whose shape, structure, field population, coverage, sequence, and naming are identical across all 214 words. A reader comparing the artefact set for word 3 and word 103 sees the same file set, the same section structure, the same required fields populated, the same coverage guarantees satisfied. Differences between words are analytical (what the data shows, what the narrative says) — never procedural (which files exist, which sections are present, which fields are populated).

Shape consistency includes: the file set produced per word; the sub-sections of each file; the required fields in each record inserted to the database; the coverage proportions (every finding has exactly one or more catalogue-links rows and at least one entity-links row; every finding has a declared finding_type from the controlled vocabulary); the naming conventions across all files; the sign-off artefact format at every sub-stage.

This claim is what binds consistency across the 214 words over the year. Without it, each session produces what it produced — which is what the prior five words demonstrated. With it, the artefact shape is enforced by the instruction, not by session memory or inter-session tradition.

### Test — any proposed rule or rewrite section must pass this check

Before accepting any rewrite of any section, apply this three-part test:

1. **Does this reduce procedural freedom without reducing analytical depth?** If the section removes a choice the session should not be making — pass. If it removes analytical depth that the programme depends on — fail, redraft.
2. **Is every procedural statement mechanical?** If a sentence says "determine", "assess", "as appropriate" in a procedural context — fail. Redraft to "read", "write", "count", "compare".
3. **Does this produce the same artefact shape that every other word will produce?** If the section permits variation in produced artefacts across words for non-analytical reasons — fail. Lock the shape.

Any rewrite of any section that fails any of the three tests must be redrafted before adoption. This test is restated at each sub-task in Part C.

---

## A.3 Glossary — the analytical/procedural distinction

The distinction between analytical and procedural language is load-bearing. A later session may need to classify a sentence in the original instruction as one or the other in order to decide whether to preserve it, rewrite it mechanically, or expand it.

**Analytical language** appears in instructions about how to read the data, how to characterise inner-being dynamics, how to arrive at findings, how to stitch observations, how to describe spirit-soul-body classification, how to identify cross-registry connections. It names *what to think about* and *what kind of output counts as good*. It does not prescribe the session's freedom in how to arrive at the output.

Examples of analytical language to preserve and, where possible, expand:
- "Read every anchor verse with the group description as the interpretive lens."
- "Identify what the verse says about the characteristic the group describes."
- "Stitch observations into the narratives the data supports across verses, terms, and groups."
- "Name connections to other registries where the evidence supports them."
- "Classify the spirit-soul-body standing from the verse evidence and state the reasoning."

**Procedural language** appears in instructions about which file to open, what to write where, in what order, what to verify, which artefact to produce, how to sign off. It names *what must happen and in what order*. It is where the session currently has room to drift.

Examples of procedural language in v1.1 that must be rewritten to mechanical form:
- v1.1: "Work through the catalogue sequentially." → Rewrite: "Read catalogue row N from [catalogue file]. Process it. Write disposition to [Q&A log]. Read row N+1. Do not read row N+2 until N+1 disposition is written."
- v1.1: "Record observations as they are determined." → Rewrite: "After each anchor verse is read, write one or more observation entries to [observations log]. The next verse may not be read until the prior verse's observations are written."
- v1.1: "Verify that the observations log contains all units." → Rewrite: "Count headings matching the pattern `### Unit N` in [observations log]. Compare to 9. If unequal, sub-stage is not complete."
- v1.1: "Assign a disposition." → Rewrite: "Choose one of the four values listed (ANSWERED / PARTIALLY ANSWERED / NOT ANSWERED / NOT APPLICABLE) based on the named criteria. Write the value to [Q&A log]."

**Ambiguous language** appears at the boundary. "Use the characteristic-perspective grouping model" is analytical (describes the reading frame). "Apply the characteristic-perspective grouping model to every anchor verse" is procedural if it implies a loop over verses; analytical if it only describes the method. The test: can the sentence be rewritten as a mechanical step without losing analytical substance? If yes, rewrite. If no, leave.

**Rule for the drafter:** every sentence in the rewrite is classified as analytical, procedural, or mixed, and the classification is recorded in a drafting comment. Analytical sentences are preserved or expanded. Procedural sentences are converted to mechanical form. Mixed sentences are split into their analytical and procedural halves and each half is drafted accordingly.

---

## A.4 Inherit list — what is preserved unchanged from v1.1

The following elements of Analysis Output v1.1 are conceptually sound and the rewrite preserves them. A rewritten section that modifies any of these without explicit justification is not a valid rewrite.

**Conceptual structure:**
- Three-stage shape: Stage 2a (comprehensive analysis), Stage 2b (Q&A partitioning), Stage 2c (analytic word output for Session C).
- Stage 2a as the analytical foundation — the full working out of what the validated data contains.
- Stage 2b as catalogue-driven completeness validation applied to Stage 2a — the catalogue is the validator of analytical completeness, applied to an analysis already produced at full depth.
- Stage 2c as structured output for Session C — six chapters mapping to the six-section word study template.

**Inputs and prerequisites:**
- Stage 1 Completion Record as a hard prerequisite for Stage 2a. "If not present: stop" is preserved and made enforceable.
- Verified clean extract (version confirmed in Stage 1 Completion Record) as the authoritative data source.
- Master catalogue (194 universal questions + registry-specific questions) as the completeness standard.

**Nine Stage 2a reading units:** Registry Overview, XREF Terms, OWNER Terms Lexical Foundation, Verse Context Groups Landscape, Correlation Signals, Existing SD Pointers, Anchor Verse Reading, Thin Evidence Flags, Existing Findings. Preserved as the analytical input units. Their function in the rewrite may be clarified (they are inputs to the analytical disposition, not ends in themselves) but the set of nine is preserved.

**Stage 2b disposition vocabulary:** ANSWERED, PARTIALLY ANSWERED, NOT ANSWERED, NOT APPLICABLE. Preserved.

**Type (a) / Type (b) patch distinction:** Type (a) for data quality corrections (Stage 1 only), Type (b) for analytical findings (Stage 2b close). Preserved.

**Closure checklist six domains:** Stage flow integrity (A), Findings integrity (B), Flag resolution (C), Entity links (D), Catalogue links (E), Analytic Word Output (F). Preserved as end-of-process verification. Supplemented in the rewrite with per-sub-stage gates — not replaced.

**Integrity rules SB-11, SB-25, SB-26, SB-27, SB-7, SB-8:** Cross-registry SD pointer rule; Stage 2a log fixed after sign-off; Stage 2b draws only from Stage 2a; Stage 2c draws only from Stage 2b and SD accumulator; Chapter 5 correlation-signal rules. Preserved.

**GR-DIR-006 six-point patch format compliance check:** Preserved. The rewrite adds coverage checks on top, but the format compliance check itself is retained exactly.

**Finding type vocabulary:** MEANING_OBSERVATION, ETYMOLOGY, ROOT_FINDING, THEOLOGICAL_NOTE, VERSE_ANNOTATION, VERSE_PATTERN, SOMATIC_EVIDENCE, SPIRIT_SOUL_BODY, SESSION_C_CORRECTION, CROSS_REGISTRY, SD_POINTER_LINK. Preserved. Additional finding types observed in the fellowship patch (STRUCTURAL_DISPOSITION, OPERATION_MODES, CHARACTER_FORMATION, INNER_BEING_EFFECTS, RELATIONAL_POSITIONING, DIVINE_DISPOSITION, TEMPORAL_OPERATION, ENABLING_CAPACITY, RELATIONAL_EXPRESSION, GROUND_CONDITION, OPERATIONAL_SEQUENCE, ORIGINATING_SOURCE, INNER_RESPONSE, EXTENSION_REASON, EXTREMITY_DEPTH, GRAMMATICAL_SUBJECT) — these are extensions the session introduced and the rewrite must decide whether to adopt them as controlled vocabulary or retire them. This is a drafting decision logged as an open item in the relevant Part C sub-task.

**Global rules:** wa-global-general-rules-v2_5-20260416.json is the authoritative governance and is preserved. The rewrite may propose new GR-rules but does not modify existing ones without raising a RESEARCHER_DECISION per GR-RD-002.

---

## A.5 Rewrite list — what is replaced

The following elements of Analysis Output v1.1 are rewritten. The rewrite list is not what is bad in v1.1; it is what must be mechanically enforced rather than behaviourally requested.

**Every procedural step** across all sections. Conversion target: mechanical form per A.3. No "determine / assess / as appropriate / if relevant" in procedural contexts.

**Sub-stage sign-offs.** v1.1 uses sign-off statements that a session writes from memory. Rewrite: sign-off is a produced artefact containing literal values read from the files of record — file count, item count, coverage count, verified against the declared values.

**Session log production.** v1.1 produces a session log at end-of-session. Rewrite: session log is produced at every sub-stage boundary, not only at session end. Each update is version-incremented per GR-FILE-003 and dual-written per GR-FILE-008.

**Dual-write discipline.** v1.1 applies dual-write at pass close. Rewrite: dual-write at every sub-stage boundary, with the most recent sub-stage's outputs always available in /mnt/user-data/outputs for researcher download and for attachment to a resumption session.

**Catalogue walk mechanics.** v1.1 says "work through the catalogue sequentially". Rewrite: the walk is driven by reading the catalogue file's next row — not from an in-memory position tracker. Explicit file read per row, explicit write of disposition to Q&A log per row, no advance without disposition written.

**Coverage checks for patch operations.** v1.1 lists required operation types in prose ("one wa_session_b_findings INSERT per finding, one wa_finding_catalogue_links INSERT per finding-question pair, one wa_finding_entity_links INSERT per finding-term/verse/group link"). Rewrite: a coverage check artefact enumerates every finding_id and confirms each has: one or more catalogue-links entries planned, one or more entity-links entries planned, a declared finding_type from controlled vocabulary. The coverage artefact is mandatory; the patch is not submitted without it.

**Finding-type coverage gates.** v1.1 Closure Domain B requires "at least one active MEANING_OBSERVATION finding" and "SPIRIT_SOUL_BODY finding present | Count = 1". Rewrite: these are not end-of-process checks; they are pre-patch coverage requirements embedded in Stage 2b sign-off.

**Summary derivation rule.** v1.1 does not specify how session log numbers are derived. Rewrite: every numerical count in any log, patch, or sign-off is derived by a named read-and-count of the source file, recorded alongside the count. In-memory totals do not enter logs.

**Resumption protocol.** v1.1 does not specify how a crashed session resumes. Rewrite: the session log at the last sub-stage boundary contains a literal resumption pointer — which sub-stage is next, which files to attach, which state to verify. A resumed session reads this pointer, attaches the named files, verifies the state, and proceeds from that point. No session reconstructs state from conversation memory.

**State held in files, not memory.** The catalogue walk position, the question dispositions so far, the coverage so far, the sub-stage completion state — all held in files, read when needed. The instruction explicitly forbids in-memory tracking of procedural state. Analytical context held during active reasoning is preserved; procedural state is not.

**Prototype / exception handling.** v1.1 contains no prototype exception mechanism, but the fellowship session invented one. Rewrite: explicitly state that the session has no authority to declare exceptions. All exceptions are researcher-decided items per GR-RD-001 through GR-RD-006 and must be recorded with their full prescribed format before any exception-relying work proceeds.

---

## A.6 Worked examples — converting v1.1 prose into mechanical form

These examples show the conversion pattern. A later session drafting a Part C sub-task should produce conversions in the same form.

### Example 1 — Stage 2a Unit 7 progress statement

**v1.1 text:**
> Progress tracking: Record after every 5 anchor verses: `Unit 7 progress: [n] of [total] anchor verses read. [n] observations recorded. [n] SD pointers raised.`

**Diagnosis:** The statement prescribes when the record is made (every 5 verses) but does not prescribe how [n] is derived. The fellowship session declared "35 observations" in the Progress Record without writing 35 observation entries.

**Mechanical rewrite:**
> After every anchor verse is read, write one or more observation entries to [observations log]. The entry format is: `Verse [reference] | Group [group_code] | Observation [N]: [text]`, where [N] is a within-unit sequential integer. After every 5 verses, write the progress line by: (a) count the occurrences of `Observation [N]:` in the observations log Unit 7 section; (b) count the occurrences of `SD Pointer [label]:` in the same section; (c) write `Unit 7 progress: [verse_count] of [anchor_total] anchor verses read. [observation_count] observations recorded from file count. [sd_pointer_count] SD pointers raised from file count.` The counts on this line are verified against the file, not from session memory. If file count differs from session's running total, file count is authoritative.

### Example 2 — Stage 2b Q&A disposition assignment

**v1.1 text:**
> Step 3 — Assign disposition: [table of four values] ... Critical distinction — NOT ANSWERED vs NOT APPLICABLE: NOT ANSWERED means Stage 2a should have addressed this and did not. NOT APPLICABLE means the characteristic genuinely does not engage with this question's domain. Assign NOT APPLICABLE conservatively — default to NOT ANSWERED if uncertain.

**Diagnosis:** The analytical distinction (NOT ANSWERED vs NOT APPLICABLE) is preserved. The procedural step "Assign disposition" needs mechanical form — the assignment must be written to a file, not held in memory, and must be made for every catalogue row.

**Mechanical rewrite:**
> For each catalogue row read from [catalogue file]: (a) read the question text and domain; (b) search the Stage 2a observations log for observations that address the question — this is the analytical step, preserved in full; (c) select one disposition from the four values listed using the criteria in the table — this is analytical; (d) write the disposition to [Q&A log] in the format: `Q[code] | Disposition: [value] | Rationale: [text if ANSWERED or PARTIAL, NOT APPLICABLE reason if N/A, NOT ANSWERED gap if NOT ANSWERED]`. Do not proceed to the next catalogue row until the disposition is written. The Q&A log is the source of truth for disposition state; session memory is not.

### Example 3 — Session log Stage 2b summary

**v1.1 text (from v1.1 sign-off template):**
> [n] questions processed: [n] ANSWERED, [n] PARTIALLY ANSWERED, [n] NOT ANSWERED, [n] NOT APPLICABLE
> [n] findings written to database
> [n] SD pointers persisted

**Diagnosis:** The fellowship session wrote "28 questions processed: 17 / 4 / 7" while the observations log contains 20 Q&A pairs: 15 / 2 / 2 / 1. Numbers were from memory, not from the file.

**Mechanical rewrite:**
> Before writing the Stage 2b sign-off, derive all counts from file reads:
> - Count occurrences of `^### Q[0-9]+:` in [observations log] Stage 2b Q&A section → [n_total]
> - Count occurrences of `Disposition: ANSWERED` in the same section → [n_answered]
> - Count occurrences of `Disposition: PARTIALLY ANSWERED` in the same section → [n_partial]
> - Count occurrences of `Disposition: NOT ANSWERED` in the same section → [n_not_answered]
> - Count occurrences of `Disposition: NOT APPLICABLE` in the same section → [n_not_applicable]
> - Verify n_total = n_answered + n_partial + n_not_answered + n_not_applicable. If not equal, sign-off is blocked; source file is inconsistent.
> - Count the operations in the Type (b) patch: insert operations on wa_session_b_findings → [n_findings]. Insert operations on wa_session_research_flags with flag_code = SD_POINTER → [n_sd]. These are derived from the patch file.
> - Write sign-off with each count alongside its derivation: `[n_total] questions processed ([counted from observations log Stage 2b section]): [n_answered] ANSWERED, [n_partial] PARTIALLY ANSWERED, [n_not_answered] NOT ANSWERED, [n_not_applicable] NOT APPLICABLE. [n_findings] findings in patch ([counted from patch file operations]). [n_sd] SD pointers in patch ([counted from patch file operations]).`

### Example 4 — Type (b) patch construction

**v1.1 text:**
> For each ANSWERED or PARTIALLY ANSWERED Q&A entry that produces a new finding:
> - One `wa_session_b_findings` INSERT per finding
> - One `wa_finding_catalogue_links` INSERT per finding-question pair
> - One `wa_finding_entity_links` INSERT per finding-term/verse/group link

**Diagnosis:** Prose list. Fellowship session produced the first category only. No coverage enforcement. The instruction told the session to do three things and the session did one.

**Mechanical rewrite:**
> Before constructing the Type (b) patch JSON, produce the coverage artefact. The coverage artefact is a table in [observations log] with one row per finding and the following columns:
> - finding_id (literal, from Q&A log)
> - finding_type (literal, from Q&A log; must be from controlled vocabulary — reject if not)
> - catalogue_link_questions (at least one catalogue question code, from Q&A log; reject if empty)
> - entity_link_targets (at least one term_id, verse_record_id, or group_id from Q&A log entity_links field; reject if empty)
>
> Verify that the coverage artefact contains one row per finding. Count findings in Q&A log. Count rows in coverage artefact. If not equal, coverage is incomplete; patch is blocked.
>
> Separately, verify finding-type coverage:
> - Count rows in coverage artefact with finding_type = MEANING_OBSERVATION. Must be ≥ 1. If 0: coverage is incomplete; patch is blocked.
> - Count rows in coverage artefact with finding_type = SPIRIT_SOUL_BODY. Must be exactly 1. If 0 or >1: coverage is incomplete; patch is blocked.
>
> Only once the coverage artefact is complete and both finding-type checks pass, construct the patch JSON. Each row in the coverage artefact produces: one wa_session_b_findings insert, one or more wa_finding_catalogue_links inserts (one per catalogue question), one or more wa_finding_entity_links inserts (one per entity link target).

---

## A.7 Scope and relationship to other instructions

The rewrite scope is exclusively **wa-sessionb-analysis-output-v1_1-20260416.md**. Other instructions (Analysis Readiness v1.x, Verse Context v2.x, Dimension Review v3.x, Session C, Session D) are **not** in scope for this rewrite programme.

However, the drafter should note:
- The rewrite's governing principle (Task 7) is cross-instruction in character. If researcher decides to propagate it to other instructions later, this task log's Part A is designed to be re-usable.
- Rules added to the global rules file (wa-global-general-rules-v2_5-20260416.json) as part of the rewrite affect all instructions. Any such addition requires researcher approval per GR-PROC-004 and must pass the GR scope test (a rule belongs in global rules if it governs more than one instruction).
- References from Analysis Output to other instructions must be updated if those references point to outdated versions.

---

## A.8 Companion session log

The companion file `wa-062-fellowship-review-sessionlog-v1-20260417.md` contains the full deliberation record that produced this task log. It preserves:
- Researcher inputs verbatim.
- Claude AI interpretations that were wrong and were corrected.
- The trajectory from "rewrite the methodology" (wrong) to "maximise analytical depth, remove procedural choice" (correct).
- The 214-word horizon context and its implications.

A later session drafting a Part C sub-task does not need to read the session log. It may be consulted if the wording of a task is unclear or appears to conflict with another.

---

# Part B — Application principles

Part B contains the four themes under which Task 7's governing principle is applied. Each theme is a Task in its own right (Tasks 8–11). Each is stated as a principle with its analytical-freedom aspect, its procedural-enforcement aspect, and its cross-word consistency aspect. The Part C sub-tasks each cite which of Tasks 8–11 are relevant to the section being rewritten.

---

## Task 8 — Completeness enforcement across every sub-stage

| Field | Detail |
|---|---|
| Task ID | REV-062-008 |
| Theme | Completeness — no sub-stage advances until its work is written, verified, and signed off |
| Severity | Foundational |
| Raised | 2026-04-17 |
| Applies to Part C sub-tasks | All of Stage 2a units, Stage 2b Q&A walk, Stage 2c chapters, Closure |
| Absorbs | Tasks 3 (sub-stage verification), 6 (sequential walk) |
| Status | Open |

### Principle

Every sub-stage of Analysis Output has a sub-stage sign-off artefact. The artefact contains literal values read from the files of record. The next sub-stage does not begin until the prior sub-stage's sign-off artefact is written and its verified values match the declared values. Sub-stage boundaries are hard gates, not soft disciplines.

### Analytical-freedom aspect

Completeness does not mean uniformity of depth. A word with rich anchor-verse evidence produces a deeper Unit 7 than a word with thin evidence. The sign-off artefact records what was actually produced; it does not impose a minimum observation count. Analytical depth scales with the data. The sign-off check verifies that what was produced is recorded and fixed, not that the session produced a specific quantity.

### Procedural-enforcement aspect

**Sub-stage sign-off artefact format (mandatory structure, same across all sub-stages):**

```
SUB-STAGE SIGN-OFF
  Sub-stage identifier: [literal — e.g. "Stage 2a Unit 7", "Stage 2b Q-batch 001–020", "Stage 2c Chapter 3"]
  Source file: [literal filename]
  Expected items: [declared count — the intended scope of this sub-stage]
  File count: [counted from file by named pattern match]
  Match: [YES if file count = expected count; NO otherwise]
  Verification method: [literal description of the count procedure]
  Sign-off timestamp: [ISO datetime]
  Next sub-stage: [literal identifier of the sub-stage that may now begin]
```

A sub-stage is complete only when `Match: YES` is written to the sign-off artefact.

**Catalogue walk in Stage 2b is file-driven, not memory-driven:**
- The session reads the catalogue from its file (from the observation_question_catalogue section of the extract, or from a separate catalogue file produced by CC).
- For each row in file order: read question, process, write disposition to Q&A log. The next row is read only after the previous row's disposition is written.
- The session does not hold the catalogue in memory as a state variable. Every read of "the next question" is a re-read of the file from a named position.
- There is no cherry-picking. There is no prototype scope that selects a subset. If the instruction permits a partial run (which it may not, for production), it permits only a *contiguous range by file order* and the range is declared and recorded before the run begins.

**Every Stage 2a unit is a sub-stage.** Unit 1 through Unit 9 each produce their own sign-off artefact. The Stage 2a overall sign-off is produced only after all nine unit sign-offs are written and verified.

**Every Stage 2b catalogue batch is a sub-stage.** The catalogue is divided into batches for sub-stage gating purposes. Batch size is fixed — e.g., 20 questions per batch — and declared in the rewrite. Each batch produces its own sign-off before the next batch begins.

**Every Stage 2c chapter is a sub-stage.** Chapter 1 through Chapter 6 each produce their own sign-off.

**The six-domain Closure checklist remains as an end-of-process audit** (inherit from v1.1) but is no longer the first line of defence. By the time Closure runs, sub-stage sign-offs have already verified most of what Closure re-checks.

### Cross-word consistency aspect

The sub-stage sign-off format is identical across every word. The number of sub-stages is identical across every word (same nine Stage 2a units, same number of catalogue batches given fixed batch size, same six Stage 2c chapters). A word with fewer anchor verses still produces Unit 7 sign-off; a word with zero SD pointers in correlation signals still produces Unit 5 sign-off. Shape is locked; content scales.

### Self-check for a rewrite touching this theme

- [ ] Every sub-stage in the rewritten section has a sign-off artefact with the format specified above.
- [ ] The sign-off artefact contains literal counts derived from file reads.
- [ ] The next sub-stage cannot begin without the prior sub-stage's sign-off written with Match: YES.
- [ ] The catalogue walk is file-driven, not memory-driven.
- [ ] Analytical depth is not rationed to fit a minimum count or maximum count.
- [ ] The sub-stage structure is identical across all 214 words.

### Open drafting decisions

- **Batch size for Stage 2b.** 20 questions per batch is a starting suggestion. A larger batch (50) reduces overhead; a smaller batch (10) catches errors sooner. Drafter decides, supported by scale analysis: at 194 questions, batch of 20 gives 10 sub-stages; batch of 10 gives 20. Recorded as a RESEARCHER_DECISION if drafter cannot resolve from instructional principle.

---

## Task 9 — Coverage enforcement for required outputs and artefacts

| Field | Detail |
|---|---|
| Task ID | REV-062-009 |
| Theme | Coverage — every required artefact is produced, and its coverage of the expected population is literal and mandatory |
| Severity | Foundational |
| Raised | 2026-04-17 |
| Applies to Part C sub-tasks | Stage 2b Type (b) patch construction; Stage 2c chapter completeness; Closure Domains D, E |
| Absorbs | Tasks 4 (link operations absent), 5 (session log counts wrong), 7 (Domain B finding types — flagged in earlier correspondence) |
| Status | Open |

### Principle

Every required output has a literal coverage requirement. The coverage is checked by a produced artefact, not by prose statement. The check is mechanical: enumerate the expected items, enumerate the produced items, compare counts, confirm each expected item has a corresponding produced item with the required fields populated.

### Analytical-freedom aspect

Coverage rules are floors, not caps. "At least one MEANING_OBSERVATION finding" does not mean exactly one. If the data supports eight MEANING_OBSERVATION findings, the session produces eight. "At least one entity link per finding" does not mean exactly one. If a finding draws from six anchor verses, the entity-links coverage for that finding is six. The coverage check verifies the floor; the session produces what the data supports above the floor.

Additional finding types beyond the controlled vocabulary (fellowship's STRUCTURAL_DISPOSITION, OPERATION_MODES, and others listed in A.4) are an analytical observation — the session identified categories the programme had not yet defined. The rewrite decides per section whether to adopt them as controlled vocabulary; this is an analytical judgement recorded in a RESEARCHER_DECISION item.

### Procedural-enforcement aspect

**Coverage artefact for Type (b) patch (the primary case).** Per A.6 Example 4. The artefact is a table produced in the observations log before patch JSON construction:

| finding_id | finding_type | catalogue_link_questions | entity_link_targets | floor check |
|---|---|---|---|---|
| [literal] | [from controlled vocabulary] | [≥1 catalogue code] | [≥1 term/verse/group reference] | PASS/FAIL |

The artefact is populated by reading the Q&A log row by row. One coverage row per finding declared in the Q&A log. A row with any column empty is FAIL. If any row is FAIL, the artefact is incomplete and the patch is blocked.

**Finding-type coverage check (mandatory before patch construction):**

| Required finding type | Floor | Count in coverage artefact | PASS/FAIL |
|---|---|---|---|
| MEANING_OBSERVATION | ≥ 1 | [counted] | |
| SPIRIT_SOUL_BODY | = 1 | [counted] | |

If MEANING_OBSERVATION count = 0: patch blocked. The Stage 2b work is returned for gap-filling — the catalogue contains multiple questions addressing meaning/semantic range (Q019, Q011, and others); the session must have produced at least one MEANING_OBSERVATION finding from the analytical disposition. If it has not, the analysis is incomplete.

If SPIRIT_SOUL_BODY count ≠ 1: patch blocked. Every word in the programme has exactly one spirit-soul-body classification; producing zero or more than one indicates a defect in the Stage 2a classification step.

**Session log count derivation (GR-OBS-007 proposed rule from Task 5):**

Every numerical count in any session log, sign-off artefact, or patch summary is derived by a named read-and-count of the source file. The derivation method is recorded alongside the count. In-memory running totals may be maintained but are never authoritative; the file read is.

Format: `[count] ([counted from <source file>, pattern: <regex or literal>])`.

**Patch coverage and format compliance are distinct checks.** GR-DIR-006 checks patch format (structure, field names, operation types). Task 9's coverage check (this task) checks operation coverage (every finding has its required companion inserts). Both are mandatory. Both produce artefacts. Both are run before patch submission.

### Cross-word consistency aspect

Every word's Type (b) patch contains the same proportions of operation types relative to findings: one finding insert + one or more catalogue-links inserts + one or more entity-links inserts per finding. Every word's session log derives its numbers by the same named read procedures. Every word's patch is blocked by the same coverage gate. Database-level comparisons across words are meaningful because the operation shape is uniform.

### Self-check for a rewrite touching this theme

- [ ] Every required output has a coverage requirement stated as a literal count or floor.
- [ ] A coverage artefact is produced before the output is constructed.
- [ ] The coverage artefact enumerates expected items and confirms each is present with required fields.
- [ ] The output is blocked if coverage is incomplete — not completed anyway with a warning.
- [ ] Summary numbers in logs and sign-offs are derived by named file reads.
- [ ] Finding-type floors (MEANING_OBSERVATION ≥ 1, SPIRIT_SOUL_BODY = 1) are enforced at Stage 2b, not deferred to Closure.
- [ ] The coverage artefact format is identical across all 214 words.

### Open drafting decisions

- **Adoption of additional finding types.** The fellowship session introduced 16 finding types not in the v1.1 controlled vocabulary. Three options: (a) adopt them all into the controlled vocabulary; (b) reject them and force re-classification into the existing vocabulary; (c) hybrid — adopt some, retire others. Drafter recommends an option in the relevant Part C sub-task, raised as a RESEARCHER_DECISION if unresolvable from principle alone.
- **Catalogue-link status values.** v1.1 references `status IN ('suggested','validated')` for catalogue links. The rewrite must state which status the Stage 2b patch inserts carry. Drafter decides.

---

## Task 10 — Safeguarding and crash-resilient resumption

| Field | Detail |
|---|---|
| Task ID | REV-062-010 |
| Theme | Safeguarding — no session crash, disruption, or discontinuity reintroduces inconsistency or loses work |
| Severity | Foundational |
| Raised | 2026-04-17 |
| Applies to Part C sub-tasks | Session log discipline (cross-cutting); resumption protocol (new section); every sub-stage sign-off boundary |
| Absorbs | Task 3 (download discipline part) |
| Status | Open |

### Principle

At any sub-stage boundary, the work completed so far is persisted to disk and available for researcher download. A session that crashes, is interrupted, or is otherwise discontinued can be resumed by attaching the most recent sub-stage artefacts and a resumption pointer — and the resumed session will proceed identically to the original session, producing the same shape of output. Resumption does not permit the resumed session to adopt a different approach from the original.

### Analytical-freedom aspect

The analytical work already done — the observations, the narratives, the dispositions, the findings — is preserved in files at every boundary. A resumed session inherits the prior session's analytical work verbatim and continues from there. It does not re-open analytical decisions already made. The session can add depth (continue Unit 7 into new anchor verses); it cannot modify prior analytical conclusions unless a RESEARCHER_DECISION item permits re-opening.

### Procedural-enforcement aspect

**Dual-write at every sub-stage boundary.** When a sub-stage is signed off:
- The updated observations log is written to the working directory and dual-written to /mnt/user-data/outputs.
- The updated session log (see below) is dual-written.
- Any sub-stage-specific artefacts (sign-off file, coverage artefact, partial patch) are dual-written.
- The researcher can download any of these at any time between sub-stages.

**Session log at every sub-stage boundary.** The session log is not a once-per-session artefact. It is updated at every sub-stage sign-off. Each update is version-incremented per GR-FILE-003 and GR-FILE-004 (no overwrites). The session log structure:

```
SESSION LOG — wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[YYYYMMDD].md

Session identifier: [uuid or datestamp]
Session start: [iso datetime]
Last update: [iso datetime of most recent sub-stage close]

Sub-stages completed:
  [Sub-stage identifier] | [sign-off artefact filename] | [timestamp]
  ...

Sub-stages in progress:
  [Sub-stage identifier] | [state: started / observations writing / sign-off pending]

Sub-stages not yet begun:
  [Sub-stage identifier] | [prerequisite: which prior sub-stage must sign off first]

Resumption pointer (for next session if this one ends):
  Next sub-stage: [literal identifier]
  Files to attach: [literal filenames]
  State to verify: [what the resumed session must confirm before proceeding]

Open items: [researcher decisions awaiting response; blockers]
```

**Resumption protocol.** A new session resuming work on a word in progress:
1. Attaches the most recent session log for that word.
2. Reads the resumption pointer.
3. Attaches the named files.
4. Verifies the stated state (e.g., "Stage 2a Unit 6 sign-off is present; Unit 7 is next").
5. If verification passes, proceeds with the next sub-stage named in the pointer.
6. If verification fails, records the failure and raises a RESEARCHER_DECISION item.

A resumed session does not reconstruct state from memory, from prior conversations, or from inferring-backward from the patch. It reads the files. If the files are insufficient to resume, the item is raised to the researcher.

**Explicitly: the session does not declare an exception to proceed without a resumption pointer.** The fellowship failure's "prototype exception" pattern is banned.

### Cross-word consistency aspect

The session log format is identical across all 214 words. The resumption protocol is identical. A researcher looking at any word's most recent session log sees the same fields in the same order. Cross-word progress audits are possible because the format is uniform. At any point across the year of processing, the researcher can download the session log for any word and immediately see: which sub-stages are complete, which are outstanding, what the next action is.

### Self-check for a rewrite touching this theme

- [ ] Dual-write to /mnt/user-data/outputs occurs at every sub-stage boundary, not only at session end.
- [ ] The session log is updated and version-incremented at every sub-stage boundary.
- [ ] The session log contains a literal resumption pointer at all times.
- [ ] The resumption protocol is defined: read files, verify state, proceed or escalate.
- [ ] No session memory reconstruction is permitted for procedural state.
- [ ] "Prototype exception" and similar self-declared exceptions are explicitly prohibited.
- [ ] The session log format is identical across all 214 words.

### Open drafting decisions

- **Session log versioning frequency.** Every sub-stage sign-off produces a new session log version. For Analysis Output as a whole, this could be 20+ versions per word. That is intended — no overwrites, full audit trail — but the drafter should confirm this is not over-versioning that obscures the working record. Alternative: one session log per word, appended rather than versioned, with each sub-stage sign-off as a dated entry. Researcher decision if drafter cannot resolve.

---

## Task 11 — Memory management and state discipline

| Field | Detail |
|---|---|
| Task ID | REV-062-011 |
| Theme | Memory — procedural state is held in files; session memory is for analytical work only |
| Severity | Foundational |
| Raised | 2026-04-17 |
| Applies to Part C sub-tasks | Every sub-task (cross-cutting); Stage 2a reading unit procedures; Stage 2b catalogue walk; Stage 2c chapter writing |
| Absorbs | Task 5 (partial — summary derivation is covered by Task 9 also) |
| Status | Open |

### Principle

Procedural state is held in files, not in session memory. Where the session needs to know its current position in a procedure, the count of items done, the disposition of a question already processed, the coverage so far — it reads the relevant file. Session memory is reserved for analytical work: understanding the verse, stitching observations, reasoning about a finding's language. At scale (120+ Q&A pairs for a word like love), in-memory procedural state is unreliable by nature; the rewrite does not rely on it.

### Analytical-freedom aspect

The session's analytical working memory is preserved in full. While reading 2Pe 1:4 and considering what it reveals about fellowship's ontological participation in divine nature, the session uses its analytical capacity without restriction. The rule applies only to procedural state — position in a walk, count of items done, dispositions already assigned, coverage achieved.

Analytical working memory includes: the shape of an emerging finding as the session reasons about it; the connections between observations that are about to be stitched into a narrative; the interpretation of a verse in the context of surrounding anchor verses. These are active reasoning. The rule does not constrain them.

The rule does constrain: what question number has been processed; what the running count of findings is; what the disposition of Q017 was; whether Unit 6 has been signed off. All of these are facts about procedure and are held in files.

### Procedural-enforcement aspect

**Named state files.** The rewrite names the files that hold procedural state:

- **Catalogue walk position:** held in the Q&A log itself. The "next question" is the catalogue row whose code does not yet appear in the Q&A log as a heading.
- **Question dispositions:** held in the Q&A log. Reading the disposition of Q017 is reading the Q&A log's Q017 entry.
- **Sub-stage completion state:** held in the session log. Reading "is Unit 6 signed off" is reading whether the session log lists Unit 6 in its "Sub-stages completed" section.
- **Finding coverage state:** held in the coverage artefact (Task 9). The session does not hold "which findings still need entity links"; it reads the coverage artefact.
- **Running counts for summary:** not held — derived by file read per Task 9.

**Explicit prohibition:** the rewrite prohibits phrases such as "keep track of", "maintain a running total", "remember which", "the session has processed N so far" in procedural contexts. These imply in-memory state. The rewrite uses "read from the Q&A log", "count the occurrences in the observations log", "check the session log for the last sign-off".

**Re-read discipline.** Before every procedural decision, the session re-reads the relevant state file. Not "the session remembers where it is"; "the session reads where it is". The re-read is cheap and the in-memory cost of losing track is high.

### Cross-word consistency aspect

Every session processing every word uses the same named state files. A session resumed after a crash reads the same files the original session was reading. A researcher auditing progress reads the same files. The absence of in-memory state means no session can carry a private understanding of "where I am" that differs from another session's understanding — because all sessions read from the same file-based source of truth.

### Self-check for a rewrite touching this theme

- [ ] Every procedural state is explicitly located in a named file.
- [ ] No rewrite prose contains "keep track of", "running total", "the session has so far" in procedural contexts.
- [ ] Re-read instructions appear wherever a procedural decision is made.
- [ ] Analytical working memory is not constrained — only procedural state.
- [ ] A resumed session can read all procedural state from the named files.

### Open drafting decisions

None anticipated. This is the cleanest of the four themes to apply mechanically — either the state is named in a file or the rule fails.

---

# Part C — Per-section rewrite sub-tasks

Part C contains the detailed rewrite work, organised by target section of Analysis Output v1.1. Each sub-task:

- Names the v1.1 section(s) it governs (by line range).
- Identifies current weaknesses against Task 7's three claims.
- Lists which of Tasks 8–11 apply.
- States what the rewritten section must contain.
- Ships with a self-check that a later session must complete before closing the sub-task.
- Notes any open drafting decisions and their recommended resolution.

The sub-tasks are numbered **Task 12.1 through Task 12.11** under the umbrella of Task 12 (rewrite Analysis Output instruction to version 2.0). They may be executed in any order that respects the prerequisite relationships noted in the summary table below, though the natural order is the order they appear.

## Sub-task summary table

| Sub-task | Governs v1.1 section(s) | Themes applied | Prerequisites | Output |
|---|---|---|---|---|
| 12.1 | Document metadata, Change Log, Governing Rules | 7 | None | Updated header for v2.0 |
| 12.2 | Pipeline Position, What to Attach at Session Start | 7, 8, 10 | 12.1 | Attachment protocol and pipeline diagram |
| 12.3 | Governing Disciplines | 7, 8, 9, 10, 11 | 12.1 | Governing disciplines for the rewrite |
| 12.4 | Schema Readiness Gate | 7, 9 | 12.3 | Ingress gate: banned prototype exception; Stage 1 prerequisite enforced |
| 12.5 | Stage 2a — Purpose, Outputs, Nine Reading Units | 7, 8, 10, 11 | 12.3 | Stage 2a with sub-stage sign-off per unit |
| 12.6 | Stage 2a Sign-Off | 7, 8, 10 | 12.5 | Stage 2a overall sign-off gate |
| 12.7 | Stage 2b — Purpose, Prerequisites, Outputs, Q&A Partitioning Process | 7, 8, 9, 10, 11 | 12.5, 12.6 | Stage 2b with batch sub-stage sign-off; file-driven walk |
| 12.8 | SD Pointer Review, Existing Findings Review, Type (b) Patch Construction, Stage 2b Sign-Off | 7, 8, 9, 10 | 12.7 | Coverage artefacts; patch construction with coverage gate |
| 12.9 | Stage 2c — Purpose, Prerequisites, Outputs, Six Chapter Structure, Stage 2c Sign-Off | 7, 8, 10 | 12.8 | Stage 2c with chapter sub-stage sign-off |
| 12.10 | Closure — Purpose, Six-Domain Closure Checklist, Corrective Action Loop, Closing Patch, Handoff Signal | 7, 9, 10 | 12.9 | Closure as end-of-process audit (supplementing, not replacing, sub-stage gates) |
| 12.11 | Integrity Rules, Naming Conventions | 7, 8, 9, 10, 11 | 12.1–12.10 | Updated integrity rules and naming to match the rewritten body |

### Execution guidance

- Tasks 12.1 and 12.3 should be executed first as they set conventions used by all others.
- Tasks 12.5 → 12.6 → 12.7 → 12.8 → 12.9 → 12.10 are a pipeline; executing them in order ensures each downstream section aligns with upstream rewrites.
- Task 12.11 is the final consolidation and cannot close until all others are closed.
- Any sub-task may surface a RESEARCHER_DECISION item; record it per GR-RD-001 through GR-RD-006 and continue only after resolution.

---

## Task 12.1 — Rewrite document metadata, Change Log, Governing Rules

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.1 |
| v1.1 sections | Lines 1–35: document header table, Change Log, Governing Rules |
| Themes | 7 |
| Status | Open |

### Current weaknesses against Task 7

v1.1's Change Log documents the v1.0→v1.1 correction for patch format compliance. It is a normal change log. No structural weakness. The Governing Rules section points to global rules and the patch specification. No structural weakness.

The rewrite need: v2.0 is a major version increment under Task 7's governing principle. The header and Change Log must make this visible so that a reader (human or future AI) immediately sees the document has been re-founded under the new principle.

### Rewritten section must contain

1. **Header table** updated with new filename `wa-sessionb-analysis-output-v2-[YYYYMMDD].md`, version 2.0, status Active, supersedes v1.1.
2. **Change Log** entry for v2.0 stating the three-claim governing principle (quoted from A.2), the diagnosis (summarised from A.1), and the intended effect (the rewrite removes procedural choice while maximising analytical depth, and produces identical artefact shape across all 214 words).
3. **Governing Rules section** expanded to state that the rewrite is governed by:
   - wa-global-general-rules-v2_5-20260416.json (or current version).
   - wa-patch-specification-v1_14-20260416.md (or current version).
   - The three-claim principle (Task 7 from this task log), quoted in full as the first paragraph.
   - Any new GR-rules added as a consequence of this rewrite (see Task 5's GR-OBS-007 proposal, to be confirmed by researcher).
4. **Amendment test**: a short paragraph stating that any future amendment to this instruction must pass the three-part test from A.2 before adoption. This prevents future amendments from silently reintroducing procedural freedom.

### Self-check

- [ ] Header filename, version, status updated.
- [ ] Change Log records v2.0 as major version, names the governing principle, references Task 7.
- [ ] Governing Rules section quotes the three claims in full.
- [ ] Amendment test paragraph present.

### Open drafting decisions

None.

---

## Task 12.2 — Rewrite Pipeline Position and What to Attach at Session Start

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.2 |
| v1.1 sections | Lines 38–83: Pipeline Position, What to Attach at Session Start |
| Themes | 7, 8, 10 |
| Status | Open |

### Current weaknesses against Task 7

**Pipeline Position (lines 38–62)** is a diagram. The rewrite updates it to show per-sub-stage sign-off gates (Task 8) and per-sub-stage dual-write (Task 10) so the gating architecture is visible.

**What to Attach at Session Start (lines 65–83)** lists required files with textual conditions ("If not present: stop"). The "stop" is correct but not enforceable as written — the fellowship session proceeded anyway under a self-declared "prototype exception". The rewrite makes the stop mechanical and adds a resumption mode for sessions picking up a word already in progress.

### Rewritten section must contain

**Pipeline Position — updated diagram**: adds explicit sub-stage gate markers so that each sub-stage (unit, batch, chapter) is visually shown as a gate that must close before the next opens.

**What to Attach at Session Start — two modes:**

**Mode A — Fresh word (no prior Session B work):**
- This instruction file (wa-sessionb-analysis-output-v2-[YYYYMMDD].md)
- Global rules file (wa-global-general-rules-v[current].json)
- Stage 1 Completion Record (extracted from the Analysis Readiness observations log)
- Verified clean extract (filename and version as named in Stage 1 Completion Record)
- CC instructions (current version)
- Master catalogue (observation_question_catalogue section of extract or separate catalogue JSON)

**Ingress check for Mode A:** each of the six files above must be present. The session confirms presence by listing each filename in a startup artefact. If any file is missing: write an ingress-failure artefact, raise RESEARCHER_DECISION per GR-RD-002, and do not proceed. The session does not invent exceptions.

**Mode B — Resuming a word in progress:**
All Mode A files, plus:
- The most recent session log for this word (contains the resumption pointer)
- All files named in the resumption pointer (most recent sub-stage sign-off artefact, observations log, Q&A log, session log itself)
- Any sub-stage-specific artefacts named in the pointer (partial patch, coverage artefact in progress, etc.)

**Ingress check for Mode B:** the session (a) reads the resumption pointer in the session log; (b) verifies each named file is attached; (c) verifies the state declared in the pointer against the attached files; (d) proceeds only if verification passes. Any check failure: ingress-failure artefact, RESEARCHER_DECISION raised.

**Ingress artefact format (mandatory):**
```
INGRESS CONFIRMATION — Registry [nnn] [word]
Mode: [A — Fresh / B — Resume]
Session identifier: [new or inherited from resumption pointer]
Files attached and verified:
  [filename 1] | [purpose] | [checksum or size]
  [filename 2] | ...
Resumption pointer (Mode B only): [from session log, verbatim]
State verification (Mode B only): [each pointer assertion | verified YES/NO]
Ingress status: [PASS — proceed | FAIL — RESEARCHER_DECISION raised]
```

The ingress artefact is dual-written (Task 10). Session does not proceed to Stage 2a, 2b, or 2c without `Ingress status: PASS`.

### Self-check

- [ ] Pipeline diagram shows per-sub-stage gates.
- [ ] Two attachment modes defined (Fresh / Resume) with distinct file requirements.
- [ ] Ingress check is mechanical: file presence, state verification.
- [ ] Self-declared exceptions explicitly prohibited.
- [ ] Ingress artefact format is mandatory and identical across all 214 words.

### Open drafting decisions

None.

---

## Task 12.3 — Rewrite Governing Disciplines

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.3 |
| v1.1 section | Lines 86–114: Governing Disciplines |
| Themes | 7, 8, 9, 10, 11 |
| Status | Open |

### Current weaknesses against Task 7

v1.1's Governing Disciplines is a list of eleven bullet points citing relevant GR-rules. Each bullet states a discipline in behavioural terms. The bullets are correct but not mechanically enforceable as stated — they rely on the session following them.

The rewrite preserves the substantive content and adds mechanical enforcement hooks where applicable. Bullets that are purely governance (e.g., two-AI role separation) remain behavioural; bullets that govern procedure are restated in mechanical form and tied to specific sub-stage procedures.

### Rewritten section must contain

1. **Task 7's three claims** restated at the top as the governing principle all other disciplines serve.
2. **Sub-stage gating** as a discipline: "Every sub-stage completes, writes its sign-off artefact, and dual-writes its outputs before the next sub-stage begins."
3. **File-as-state-of-truth** as a discipline: "All procedural state is held in named files. Session memory is reserved for analytical work."
4. **Named file reads for all counts** as a discipline: "Every count in any log, sign-off, or patch summary is derived by a named file read, recorded alongside the count."
5. **Explicit prohibition of self-declared exceptions** as a discipline: "The session may not declare exceptions to procedure. All exceptions are researcher-decided items per GR-RD-001 through GR-RD-006."
6. **Continuity with v1.1** preserved bullets: Step-by-step (GR-PROC-001), Write on discovery (GR-OBS-001 non-waivable), All observations return to the database (GR-OBS-006), Data is authoritative (GR-PROC-002), All changes through patches or directives (GR-PROC-003), Two types of database writes (Type (a), Type (b)), No DB state assumptions (GR-DB-001), Cross-registry vision is always active (GR-PROG-002, SB-11), Characteristic-perspective grouping model (GR-PROG-006), Stage 2a free-form vs Stage 2b structured — preserved (and strengthened: Stage 2a structured by sub-stage sign-offs but its observational content remains free-form), Researcher decision items (GR-RD-001 through GR-RD-006), Session logs at every breakpoint (upgraded: at every sub-stage boundary per Task 10).

### Self-check

- [ ] Task 7's three claims appear at the top of the section.
- [ ] All v1.1 disciplines preserved or explicitly upgraded.
- [ ] New disciplines added from Tasks 8–11.
- [ ] Self-declared exceptions explicitly prohibited.
- [ ] Where a discipline has a mechanical enforcement, the mechanism is named.

### Open drafting decisions

None.

---

## Task 12.4 — Rewrite Schema Readiness Gate as enforceable ingress

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.4 |
| v1.1 section | Lines 116–129: Schema Readiness Gate |
| Themes | 7, 9 |
| Status | Open |

### Current weaknesses against Task 7

v1.1 has a Schema Readiness Gate table with five conditions, each with a check and a fail action. The conditions are correct. The weakness: the gate is described as "confirm with CC" and the fail action is "Raise with researcher" or "Raise CC directive". Fellowship's case shows this is not enforceable — the session proceeded without performing the gate at all (the observations log notes "catalogue_questions_registry: 0" from statistics, which should have been a gate fail, but was merely noted as GAP-006 and work continued).

The rewrite restates the gate as a produced artefact that must exist with PASS status before Stage 2a can begin.

### Rewritten section must contain

**Schema Readiness Gate as produced artefact:**
```
SCHEMA READINESS GATE — Registry [nnn] [word] — [iso date]
Conditions checked:
  1. wa_obs_question_catalogue has >= 194 rows | [counted by CC] | [PASS / FAIL]
  2. wa_finding_catalogue_links table exists | [CC schema check] | [PASS / FAIL]
  3. wa_session_b_findings.status column exists | [CC schema check] | [PASS / FAIL]
  4. wa_session_b_findings.term_id column exists | [CC schema check] | [PASS / FAIL]
  5. Registry-specific catalogue questions count | [from extract] | [value recorded]
Ingress decision: [PROCEED if all conditions PASS | HOLD if any condition FAILS]
Action taken on HOLD: [either "RESEARCHER_DECISION RD-[id] raised" or "CC directive DIR-[id] issued"]
```

The gate is:
- Run once per word, not per session.
- Its artefact is dual-written and attached to every subsequent session for this word.
- Condition 5 is value-recorded, not PASS/FAIL — if 0, the session works with universal catalogue only but notes the absence in its Q&A coverage.
- HOLD blocks Stage 2a. No "prototype exception" override.

### Self-check

- [ ] The gate is a produced artefact with explicit PASS/FAIL per condition.
- [ ] The artefact is dual-written.
- [ ] HOLD blocks Stage 2a mechanically.
- [ ] Self-declared exceptions prohibited.

### Open drafting decisions

- Whether Condition 5 (registry-specific questions) should be PASS/FAIL or informational. v1.1 treats it as "If 0: raise with researcher." Researcher decision if unresolved from drafting principle alone.

---

## Task 12.5 — Rewrite Stage 2a: Purpose, Outputs, Nine Reading Units

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.5 |
| v1.1 sections | Lines 132–303: Stage 2a — Purpose, Outputs, Nine Reading Units (Unit 1 through Unit 9) |
| Themes | 7, 8, 10, 11 |
| Status | Open |

### Current weaknesses against Task 7

**Purpose (lines 132–141):** States Stage 2a is free-form and analytically foundational. Preserve.

**Stage 2a Outputs (lines 144–150):** Observations log "written continuously during Stage 2a, downloaded at end". Rewrite: downloaded at each unit sign-off, not only at end.

**Nine Reading Units (lines 153–302):** Each unit specified as Read / Observe and record / Sign-off statement. The sign-off statement is a textual assertion ("Unit 1 complete. Registry overview recorded. [n] cross-cluster signals noted. [n] programme-level observations."). Fellowship failure: Units 7, 8, 9 declared complete without content. The rewrite makes each unit sign-off a produced artefact per Task 8.

### Rewritten section must contain

**Stage 2a Purpose — preserved largely unchanged.** One addition: explicit statement that Stage 2a produces an *analytical disposition* of the word — a comprehensive understanding drawn from validated data — and that the nine reading units are inputs to that disposition, not ends in themselves. The disposition is the material from which Stage 2b can produce Q&A pairs that address every catalogue question.

**Stage 2a Outputs table — updated:**
- Observations log: dual-written at every unit sign-off, not only at end.
- SD Pointer Accumulator: part of observations log; updated per-unit; its running count is a file-derived figure.
- **Unit sign-off artefacts**: nine artefacts, one per unit, each produced at the close of its respective unit. Artefact format per Task 8's sub-stage sign-off template.

**Each of the nine Reading Units is rewritten with:**

1. **Read** section — preserved from v1.1 (what to read). Analytical freedom intact.
2. **Observe and record** section — preserved in substance. Procedural form strengthened: "Write observations to [observations log] Unit [N] section in the format: [format]. Each observation carries a within-unit sequential identifier. Observations are written as they are produced, per GR-OBS-001."
3. **Progress tracking** — generalised to all units: "After every [N] items processed (verses for Unit 7, groups for Unit 4, etc.), write a progress line to the observations log derived by file read. Format: [literal format]. The counts on this line are verified against the file, not from session memory."
4. **Sign-off artefact** (new for each unit) — replaces the v1.1 sign-off statement. Format per Task 8. Includes: file count of observation entries in this unit's section; expected count (where natural, e.g., Unit 7 expects at least `anchor_verse_count` entries) or declared count (where unit depth is analytical, e.g., Unit 3); match check; next unit identifier.

**Unit 7 (Anchor Verse Reading) — additional specification:**
- Each anchor verse produces one or more observation entries, written before the next verse is read.
- Each anchor verse's application of the five cross-registry vision questions produces either observation entries or SD pointer entries, each written before the next verse.
- The Unit 7 sign-off verifies: count of observation entries >= count of anchor verses (each verse produces at least one observation); count of `Verse [reference]` labels in the Unit 7 section equals the count of anchor verses in the extract; every anchor verse in the extract appears at least once in the Unit 7 section.

**Null-operation units:** where a unit has nothing to do (e.g., Unit 2 when XREF term count is zero, Unit 9 when prior findings count is zero), the sign-off artefact is still produced, with file count = 0 and declared count = 0 and the null operation explicitly recorded. No unit is silently skipped.

### Self-check

- [ ] Purpose preserved; analytical-disposition framing added.
- [ ] Outputs table updated with dual-write per unit.
- [ ] Each of nine units has: Read, Observe and record, Progress tracking, Sign-off artefact.
- [ ] Each unit's sign-off is a produced artefact per Task 8.
- [ ] Unit 7 has additional specification for anchor-verse coverage.
- [ ] Null-operation units explicitly produce their sign-off — no silent skipping.
- [ ] Analytical depth in observational content is unconstrained.
- [ ] Every procedural step is mechanical.

### Open drafting decisions

None anticipated.

---

## Task 12.6 — Rewrite Stage 2a Sign-Off

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.6 |
| v1.1 section | Lines 305–339: Stage 2a Sign-Off |
| Themes | 7, 8, 10 |
| Status | Open |

### Current weaknesses against Task 7

v1.1's Stage 2a Sign-Off is a three-step procedure ending with a textual "STAGE 2A COMPLETE — [date]" summary. Summary contains declared counts per unit. Fellowship failure: summary was written with declared counts for Units 7, 8, 9 but the unit content was not written.

### Rewritten section must contain

**Stage 2a Sign-Off as a compound artefact** that depends on the nine unit sign-off artefacts already existing. Its structure:

```
STAGE 2A SIGN-OFF — Registry [nnn] [word] — [iso date]

Unit sign-off verification:
  Unit 1 sign-off artefact: [filename] | present YES/NO | Match YES/NO
  Unit 2 sign-off artefact: [filename] | present YES/NO | Match YES/NO
  ... (all nine)

Aggregate counts (file-derived):
  Total observation entries: [counted across all unit sections]
  Total SD pointers raised this stage: [counted from SD Pointer Accumulator]
  Anchor verses read in Unit 7: [counted]
  Anchor verses in extract: [counted from extract]
  Unit 7 anchor coverage: [anchor verses read / anchor verses in extract]

Gate decision:
  All unit sign-offs present: [YES/NO]
  All unit sign-offs Match YES: [YES/NO]
  Unit 7 anchor coverage = 100%: [YES/NO]
  Stage 2a COMPLETE: [YES only if all three gate conditions YES]

Observations log status:
  Filename: [filename]
  Fixed per SB-25: YES (after this sign-off, no further writing to Stage 2a sections)
  Dual-written to outputs: YES [timestamp]

Session log update:
  Session log filename: [filename]
  Session log version incremented: [n]
  Resumption pointer set to: Stage 2b opening

Stage 2b: OPEN (only if Stage 2a COMPLETE = YES)
```

If any gate condition is NO, Stage 2a is not complete and Stage 2b does not open. A corrective action loop applies: return to the failing unit, produce its sign-off or re-do its content.

### Self-check

- [ ] Sign-off artefact explicitly depends on nine unit sign-offs.
- [ ] Gate decision is mechanical (all three conditions YES).
- [ ] Dual-write and session log update are part of the sign-off.
- [ ] Stage 2b does not open without COMPLETE = YES.

### Open drafting decisions

None.

---

## Task 12.7 — Rewrite Stage 2b: Purpose, Prerequisites, Outputs, Q&A Partitioning Process

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.7 |
| v1.1 sections | Lines 341–420: Stage 2b Purpose, Prerequisites, Outputs, Q&A Partitioning Process |
| Themes | 7, 8, 9, 10, 11 |
| Status | Open |

### Current weaknesses against Task 7

**Purpose:** Correct — Stage 2b applies the catalogue to Stage 2a observations and produces dispositions. Preserve.

**Prerequisites:** Two-item list (Stage 2a sign-off; master catalogue loaded). Add: verified ingress per Task 12.2; Stage 2a COMPLETE = YES per Task 12.6.

**Outputs:** Lists Q&A log and Type (b) patch. Q&A log "written continuously, downloaded at Stage 2b close". Rewrite: downloaded at every batch sub-stage close (Task 8).

**Q&A Partitioning Process:** Six-step process. "Work through the catalogue sequentially" (Step 1). Fellowship failure: cherry-picked. Rewrite: file-driven walk per Task 11, with batch sub-stage sign-offs per Task 8.

### Rewritten section must contain

**Stage 2b Purpose — preserved.** Sharpened: Stage 2b does not produce new analysis; it tests completeness of the Stage 2a analytical disposition against every catalogue question and persists structured findings.

**Prerequisites — expanded:**
- Ingress confirmation present (Task 12.2).
- Stage 2a sign-off present with COMPLETE = YES (Task 12.6).
- Master catalogue file loaded with >= 194 rows (verified at Schema Readiness Gate; re-verified at Stage 2b open).
- Q&A log file initialised with header and empty body.

**Outputs — updated:**
- Q&A log: dual-written at every batch sub-stage close.
- Batch sub-stage sign-off artefacts: one per catalogue batch (batch size per Task 8 open decision; tentatively 20 questions per batch).
- Type (b) patch coverage artefact: produced before patch JSON; one row per finding.
- Type (b) patch JSON: constructed only after coverage artefact complete; format-verified per GR-DIR-006.
- Stage 2b sign-off artefact: compound, depending on batch sign-offs + coverage + patch.

**Q&A Partitioning Process — rewritten as file-driven loop:**

```
Initialise:
  Open [catalogue file]. Record total row count.
  Open [Q&A log]. Confirm body is empty or contains only prior batches' entries.
  Determine current position: read the last entry in [Q&A log]; next question is the catalogue row with code immediately following.
  If Q&A log is empty: next question is catalogue row 1.
  Set current_batch_number based on position: batch N covers catalogue rows ((N-1)*batch_size + 1) through (N*batch_size).

For each batch:
  For each catalogue row in the batch, read in file order:
    Read catalogue row fields: code, question_text, section, scope, status.
    If status is not 'active' or deleted is 1: write to [Q&A log] as `Q[code] | Disposition: NOT APPLICABLE | Rationale: Catalogue row marked inactive/deleted.` Continue to next row.
    Search [Stage 2a observations log] for observations that engage the question's domain. This is the analytical step. Session uses full analytical capacity.
    Assign one of the four dispositions: ANSWERED / PARTIALLY ANSWERED / NOT ANSWERED / NOT APPLICABLE. Criteria per v1.1 table, preserved analytically. NOT APPLICABLE is conservative — default to NOT ANSWERED if uncertain.
    Write the Q&A log entry in the format:
      ### Q[code]: [question_text]
      **Status:** [DISPOSITION]
      **Evidence:** [Stage 2a observation identifiers that support the answer — e.g., "Unit 7 obs-12, Unit 7 obs-18, Unit 4 obs-5". If no evidence, disposition must be NOT ANSWERED or NOT APPLICABLE.]
      **Answer:** [if ANSWERED or PARTIALLY ANSWERED] or **Gap:** [if NOT ANSWERED or PARTIAL] or **Rationale:** [if NOT APPLICABLE]
      **Finding type:** [controlled vocabulary value, if ANSWERED or PARTIAL produces a new finding]
      **Entity links:** [term_ids, verse_record_ids, or group_ids supporting the answer]
      **SD pointer notes:** [if the answer confirms, deepens, or raises an SD pointer]
    The Q&A log entry is written to file before the next catalogue row is read.
  
  At end of batch: produce batch sub-stage sign-off artefact per Task 8.
  Dual-write Q&A log and sign-off artefact.
  Update session log with resumption pointer: next batch number.
  Proceed to next batch.

After all batches: produce overall catalogue walk verification — count rows in catalogue, count entries in Q&A log, assert equal. If unequal, walk is incomplete; identify missing rows and re-process.
```

**Explicit constraints (from Task 11):**
- Current position is held in the Q&A log, not in session memory.
- The session cannot "skip" a catalogue row. Every row is processed in file order.
- If the session is interrupted mid-batch, resumption reads the Q&A log to determine the next row.

**Evidence field discipline:** a row marked ANSWERED or PARTIALLY ANSWERED must cite specific Stage 2a observation identifiers (e.g., "Unit 7 obs-12"). Citing a unit that does not exist in the observations log (Fellowship Task 2 pattern) is a defect. Batch sign-off verifies that every Evidence identifier resolves to an observation in the Stage 2a observations log.

### Self-check

- [ ] Purpose preserved with sharpened framing (no new analysis in Stage 2b).
- [ ] Prerequisites explicit: ingress, Stage 2a COMPLETE, catalogue loaded, Q&A log initialised.
- [ ] Outputs expanded to include batch sign-offs and coverage artefact.
- [ ] Q&A walk is file-driven, not memory-driven.
- [ ] Every catalogue row is processed; none can be skipped.
- [ ] Evidence field references are verified against Stage 2a observations log at batch sign-off.
- [ ] Batch sign-off artefact per Task 8 format.
- [ ] Analytical work within each disposition assignment is unconstrained.
- [ ] Analytical vocabulary of dispositions preserved.

### Open drafting decisions

- **Batch size** — see Task 8. Default 20 pending researcher decision.
- **Handling of catalogue rows where source_word differs from the word being processed** — fellowship extract shows all 194 questions have scope `universal` regardless of source_word, so likely non-issue. Drafter confirms by inspecting catalogue fields.

---

## Task 12.8 — Rewrite SD Pointer Review, Existing Findings Review, Type (b) Patch Construction, Stage 2b Sign-Off

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.8 |
| v1.1 sections | Lines 422–536: SD Pointer Review, Existing Findings Review, Type (b) Patch Construction, Stage 2b Sign-Off |
| Themes | 7, 8, 9, 10 |
| Status | Open |

### Current weaknesses against Task 7

**SD Pointer Review (lines 422–434):** Five-question review process for each SD pointer. Procedural steps sound but not mechanically enforced. Rewrite: each SD pointer in accumulator gets a produced review record.

**Existing Findings Review (lines 437–447):** Supersession logic for prior findings. Correct in substance; rewrite makes the decisions produced as an artefact.

**Type (b) Patch Construction (lines 450–520):** The main locus of fellowship failure. Current text lists required operation types in prose. Rewrite: mandatory coverage artefact per Task 9, enforced at patch construction.

**Stage 2b Sign-Off (lines 522–535):** Textual sign-off with declared counts from memory. Fellowship failure: "28 questions processed: 17 ANSWERED" vs actual 20 / 15. Rewrite: file-derived counts per Task 9's summary derivation rule.

### Rewritten section must contain

**SD Pointer Review — as produced artefact:**

Each SD pointer in the accumulator produces a review record:
```
SD Pointer Review — [flag_label]
  Priority (HIGH/MEDIUM/LOW): [value]
  Question stated precisely: [YES/NO, with refinement if NO]
  Target registry identified: [value or "pattern — no specific registry"]
  Evidence basis: [named Stage 2a observation identifiers, verified against observations log]
  Duplicate of existing record: [YES/NO; if YES, existing flag_label]
  Disposition: [confirmed / refined / merged / new]
```

Review artefact is dual-written. Records are produced in file order of the SD accumulator. No SD pointer is skipped.

**Existing Findings Review — as produced artefact:**

For each prior finding from Unit 9:
```
Existing Finding Review — [finding_id]
  v1.1 action: [accurate / superseded / factually incorrect / set-aside]
  Patch operation planned: [none / UPDATE delete_flag=1, superseded_by_id=[new_id] / UPDATE delete_flag=1, obsolete_reason=...]
```

Review artefact is dual-written.

**Type (b) Patch Construction — with mandatory coverage artefact (Task 9):**

Before patch JSON construction, produce the coverage artefact:

| finding_id | finding_type | catalogue_link_questions | entity_link_targets | floor check |
|---|---|---|---|---|
| [literal] | [from controlled vocabulary] | [>=1 catalogue code] | [>=1 term/verse/group reference] | PASS/FAIL |

Artefact populated by reading the Q&A log row by row. One coverage row per finding declared in the Q&A log. A row with any column empty is FAIL. Any FAIL: coverage incomplete, patch blocked.

Finding-type coverage check (mandatory before patch construction):

| Required finding type | Floor | Count in coverage artefact | PASS/FAIL |
|---|---|---|---|
| MEANING_OBSERVATION | >= 1 | [counted] | |
| SPIRIT_SOUL_BODY | = 1 | [counted] | |

Failure of either check: patch blocked. Corrective action loop: return to Stage 2b Q&A analysis and fill the gap.

**Patch JSON construction** — after coverage artefact is complete and all floor checks PASS:
- For each coverage row: one wa_session_b_findings insert, one or more wa_finding_catalogue_links inserts, one or more wa_finding_entity_links inserts.
- For each SD pointer new (not in database per review): one wa_session_research_flags insert.
- For each existing finding marked superseded: one wa_session_b_findings UPDATE.
- Registry update: one wa_session_b_status = 'Analysis Complete' update (via registry_no field per patch specification).

**Format compliance check per GR-DIR-006 — six-point check preserved verbatim from v1.1.** Run after patch JSON constructed, before submission.

**Patch submission and confirmation:**
- Patch presented to researcher with: patch filename, operation count by type, coverage artefact reference, format compliance check result.
- Approved patch submitted to CC.
- CC returns confirmation per GR-DIR-005.
- Confirmation includes: findings inserted count, catalogue_links inserted count, entity_links inserted count, research_flags inserted count, registry updated YES/NO.
- Session verifies confirmation counts match patch operation counts. Mismatch: supplementary patch.

**Stage 2b Sign-Off as produced artefact with file-derived counts:**

```
STAGE 2B SIGN-OFF — Registry [nnn] [word] — [iso date]

Batch sign-off verification:
  Batch 1 sign-off artefact: [filename] | present YES/NO
  Batch 2 sign-off artefact: [filename] | present YES/NO
  ... (all batches)

Catalogue walk verification:
  Catalogue row count: [counted from catalogue file]
  Q&A log entry count: [counted from Q&A log]
  Match: [YES/NO]

Disposition counts (file-derived from Q&A log):
  ANSWERED: [count] (counted from Q&A log, pattern: "Status: ANSWERED")
  PARTIALLY ANSWERED: [count] (counted from Q&A log, pattern: "Status: PARTIALLY ANSWERED")
  NOT ANSWERED: [count] (counted from Q&A log, pattern: "Status: NOT ANSWERED")
  NOT APPLICABLE: [count] (counted from Q&A log, pattern: "Status: NOT APPLICABLE")
  Sum: [counted] | Catalogue row count: [counted] | Match: [YES/NO]

Coverage artefact:
  Filename: [filename]
  All rows PASS: [YES/NO]
  MEANING_OBSERVATION floor: [count] >= 1 ? [YES/NO]
  SPIRIT_SOUL_BODY floor: [count] = 1 ? [YES/NO]

Patch:
  Filename: [filename]
  Format compliance: [PASS/FAIL per GR-DIR-006]
  Researcher approval: [YES/NO, timestamp]
  CC confirmation received: [YES/NO, timestamp]
  Confirmation counts match patch counts: [YES/NO]

Gate decision:
  All batch sign-offs present and Match YES: [YES/NO]
  Catalogue walk verification Match: [YES/NO]
  Coverage and floor checks all PASS: [YES/NO]
  Patch applied with confirmation matching: [YES/NO]
  Stage 2b COMPLETE: [YES only if all gate conditions YES]

Session log update: [as per Task 10]

Stage 2c: OPEN (only if Stage 2b COMPLETE = YES)
```

### Self-check

- [ ] SD Pointer Review produces a review record per pointer.
- [ ] Existing Findings Review produces a review record per finding.
- [ ] Coverage artefact is mandatory before patch JSON construction.
- [ ] Finding-type floor checks enforced at Stage 2b, not deferred to Closure.
- [ ] Six-point format compliance check preserved from v1.1.
- [ ] Patch confirmation counts verified against patch operation counts.
- [ ] Stage 2b sign-off is compound artefact with file-derived counts.
- [ ] Every number in sign-off has its derivation recorded.

### Open drafting decisions

- **Controlled vocabulary for finding_type** — see Task 9 open decision. Which of the 16 finding types the fellowship session introduced are adopted into controlled vocabulary.
- **Catalogue-links status** — suggested vs validated at insert time. Drafter decides default based on programme pattern.

---

## Task 12.9 — Rewrite Stage 2c: Purpose, Prerequisites, Outputs, Six Chapter Structure, Stage 2c Sign-Off

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.9 |
| v1.1 sections | Lines 539–621: Stage 2c |
| Themes | 7, 8, 10 |
| Status | Open |

### Current weaknesses against Task 7

**Purpose:** Correct — Stage 2c produces six chapters synthesising Stage 2b Q&A pairs into reader-facing prose. Preserve.

**Prerequisites:** Stage 2b complete; Session C prose rule loaded. Add: Stage 2b COMPLETE = YES per Task 12.8.

**Outputs:** Analytic Word Output file, single deliverable written at end. Rewrite: dual-written at each chapter sign-off per Task 10.

**Six Chapter Structure:** Each chapter has a brief description of scope. Fellowship case: Stage 2c was never run (session crashed before Closure). No per-chapter sign-off. Rewrite: each chapter is a sub-stage with its own sign-off per Task 8.

**Stage 2c Sign-Off:** Textual, declares six chapters complete. Rewrite: compound artefact verifying chapter sign-offs.

### Rewritten section must contain

**Purpose — preserved.** Add: Stage 2c does not introduce new analysis; per SB-27, it draws only from Stage 2b Q&A pairs and the SD Pointer Accumulator.

**Prerequisites:**
- Stage 2b sign-off with COMPLETE = YES.
- Session C prose rule loaded (wa-global-sessionc-prose-rule-v[current].md).

**Outputs:**
- Analytic Word Output file: wa-[nnn]-[word]-sessionb-analytic-v1-[YYYYMMDD].md.
- Six chapter sign-off artefacts, one per chapter.
- Stage 2c sign-off artefact.

**Six Chapter Structure — each chapter is a sub-stage:**

For each chapter (1 through 6), the rewrite specifies:
- Scope (preserved from v1.1 chapter descriptions).
- **Source material** for the chapter, named by Q&A pair categories (file-derived):
  - Chapter 1 (Summary Overview): draws from ANSWERED/PARTIAL Q&A pairs in Section 1 Word Characteristic Summary + aggregate summary counts from Stage 2b sign-off.
  - Chapter 2 (Semantic and Lexical Foundation): draws from ANSWERED/PARTIAL pairs with finding_type in {ROOT_FINDING, ETYMOLOGY, MEANING_OBSERVATION} + Unit 3 OWNER terms observations (read from fixed Stage 2a log).
  - Chapter 3 (Anchor Verse Analysis): draws from ANSWERED/PARTIAL pairs with finding_type in {VERSE_ANNOTATION, VERSE_PATTERN} + Unit 7 observations (read from fixed Stage 2a log). Must cover every anchor verse in the extract.
  - Chapter 4 (Inner-Being Characteristics): draws from findings with finding_type in {SPIRIT_SOUL_BODY, SOMATIC_EVIDENCE, INNER_BEING_EFFECTS} (if adopted), and dimensional data from Unit 4 observations.
  - Chapter 5 (Cross-Registry Connections): draws from findings with finding_type = CROSS_REGISTRY + confirmed correlation signals. Per SB-7 and SB-8, no confirmed connection without correlation signal support; no omission of signal-supported connection.
  - Chapter 6 (Session D Investigation Points): draws from SD Pointer Accumulator (all active SD pointers for this registry, read from Q&A log SD pointer notes and patch wa_session_research_flags inserts).
- **Chapter sub-stage sign-off** per Task 8:
  - Source material verification: did the chapter draw from the named sources only (Q&A log / Stage 2a log / SD accumulator / correlation signals)?
  - Coverage check: does Chapter 3 cover every anchor verse? Does Chapter 6 list every SD pointer?
  - SB-7/SB-8 check for Chapter 5.
  - Chapter file dual-written.

**Stage 2c Sign-Off — compound artefact:**

```
STAGE 2C SIGN-OFF — Registry [nnn] [word] — [iso date]

Chapter sign-off verification:
  Chapter 1 sign-off: [filename] | present YES/NO | Match YES/NO
  ... (all six)

Cross-chapter checks:
  Chapter 3 anchor coverage = 100%: [YES/NO]
  Chapter 5 SB-7 (no unsupported confirmed connection): [YES/NO]
  Chapter 5 SB-8 (no omitted signal-supported connection): [YES/NO]
  Chapter 6 SD pointer count matches database count: [YES/NO]

Analytic Word Output file:
  Filename: [filename]
  Six chapters present: [YES/NO]
  Dual-written to outputs: YES [timestamp]

Gate decision:
  All chapter sign-offs present and Match YES: [YES/NO]
  All cross-chapter checks YES: [YES/NO]
  Stage 2c COMPLETE: [YES only if both gates YES]

Session log update: [as per Task 10]

Closure: OPEN (only if Stage 2c COMPLETE = YES)
```

### Self-check

- [ ] Purpose preserved; SB-27 sourcing rule affirmed.
- [ ] Each chapter has named source material.
- [ ] Each chapter has a sub-stage sign-off per Task 8.
- [ ] Chapter 3 anchor coverage check is mechanical.
- [ ] Chapter 5 SB-7 and SB-8 checks are mechanical.
- [ ] Chapter 6 SD pointer count check is mechanical.
- [ ] Analytical prose within chapters remains reader-facing and unconstrained in depth.

### Open drafting decisions

- **Which finding types map to which chapters** — the mapping above is a first draft; refinement depends on controlled vocabulary decision (Task 12.8 open decision).

---

## Task 12.10 — Rewrite Closure: Purpose, Six-Domain Closure Checklist, Corrective Action Loop, Closing Patch, Handoff Signal

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.10 |
| v1.1 sections | Lines 623–737: Closure |
| Themes | 7, 9, 10 |
| Status | Open |

### Current weaknesses against Task 7

v1.1 Closure is the end-of-process audit. The six-domain checklist is comprehensive. The weakness: Closure is the *only* gate, and as the fellowship case shows, a session can crash before Closure and leave defects undetected. The rewrite does not weaken Closure; it supplements it with per-sub-stage gates (Tasks 8, 9) that catch defects earlier. By the time Closure runs in the rewritten flow, most defects have already been caught. Closure becomes a second-line audit, not a first-line defence.

### Rewritten section must contain

**Purpose — sharpened.** Closure is the end-of-process audit confirming that the pre-existing sub-stage gates have produced an analytical output complete across all six domains. Closure is not the first line of defence — the sub-stage gates are. Closure is the final check that nothing slipped through and the word is ready for Session C.

**Six-Domain Closure Checklist — preserved with one addition:**

v1.1 domains A through F preserved. Each domain's pass condition and fail action unchanged. Additions:

- **Pre-check:** Confirm every sub-stage sign-off from Stage 2a (9 unit sign-offs + overall), Stage 2b (batch sign-offs + overall), Stage 2c (6 chapter sign-offs + overall) is present and Match YES. If not: Closure cannot begin; return to the failing stage.
- **Domain D (Entity links) pass condition** strengthened: "Every active finding has at least one wa_finding_entity_links row" — verified by count query per finding_id.
- **Domain E (Catalogue links) pass condition** strengthened: "Every active finding has at least one wa_finding_catalogue_links row with status IN ('suggested','validated')" — verified by count query per finding_id. These are the fellowship-failure domains (Task 4) — the coverage artefact and patch in Task 12.8 should prevent them from failing, but the Closure check is the final safety net.

**Corrective Action Loop — preserved and formalised.** Each correction produces its own artefact and returns to the failing stage. Procedures are mechanical.

**Closing Patch — preserved with format enforcement.** GR-DIR-006 six-point check runs before submission. Format preserved from v1.1.

**Handoff Signal — preserved with mandatory-outputs check:**

The handoff signal template lists the mandatory outputs (observations log, session log, analytic word output, Type (b) patch applied, closing patch applied). Rewrite: each mandatory output is verified by file-presence check before handoff is stated. If any is absent, handoff cannot be issued.

### Self-check

- [ ] Purpose sharpened to reflect supplementary role.
- [ ] Six domains preserved.
- [ ] Pre-check added: all sub-stage sign-offs present.
- [ ] Domain D and E checks stated mechanically.
- [ ] Corrective action loop preserved.
- [ ] Closing patch format check preserved.
- [ ] Handoff signal requires file-presence verification per output.

### Open drafting decisions

None.

---

## Task 12.11 — Rewrite Integrity Rules and Naming Conventions

| Field | Detail |
|---|---|
| Sub-task ID | REV-062-012.11 |
| v1.1 sections | Lines 741–779: Integrity Rules, Naming Conventions |
| Themes | 7, 8, 9, 10, 11 |
| Status | Open |

### Current weaknesses against Task 7

**Integrity Rules (lines 741–763):** Table of SB-rules inherited from v1.1 and predecessors. Fellowship failure shows the rules are correctly stated but not mechanically enforced. The rewrite preserves all SB-rules verbatim (inherit list A.4) and adds cross-references to the Part C sub-tasks where each rule is now mechanically enforced.

**Naming Conventions (lines 766–778):** Table of output filenames with patterns. Preserve. Add: sub-stage sign-off artefact filenames; coverage artefact filename; ingress artefact filename; review artefacts (SD pointer, existing findings).

### Rewritten section must contain

**Integrity Rules — preserved with enforcement cross-references:**

| Rule | Status in v2.0 | Enforcement mechanism |
|---|---|---|
| SB-1 | From Analysis Readiness (preserved) | Ingress check Task 12.2 |
| SB-2 | Preserved, updated | Sub-stage sign-offs Tasks 12.6, 12.8, 12.9; Closure Task 12.10 |
| SB-7 | Preserved | Chapter 5 mechanical check Task 12.9 |
| SB-8 | Preserved | Chapter 5 mechanical check Task 12.9 |
| SB-9 | Preserved | Stage 2c sourcing rule Task 12.9 |
| SB-11 | Preserved | Unit 7 sign-off verifies SD pointer discovery Task 12.5 |
| SB-12 | Preserved | Unit 7 sign-off verifies five cross-registry questions applied Task 12.5 |
| SB-13 | Retired (replaced by SB-11) | — |
| SB-14 | Preserved, updated | Task 12.8 patch coverage includes SD pointers |
| SB-15 | Preserved | SD pointer count verification in Stage 2b sign-off Task 12.8 |
| SB-16 | Preserved | Closing patch check Task 12.10 |
| SB-17 | Preserved, updated | Mandatory outputs verification in handoff Task 12.10 |
| SB-18 | Preserved | Closure Domain C Task 12.10 |
| SB-25 | Preserved | Stage 2a sign-off fixes observations log Task 12.6 |
| SB-26 | Preserved | Q&A evidence field verification Task 12.7 |
| SB-27 | Preserved | Stage 2c sourcing rule Task 12.9 |

**Naming Conventions — expanded:**

v1.1 patterns preserved. Added patterns for new artefact types:

| Output | Pattern | Example |
|---|---|---|
| Ingress artefact | wa-[nnn]-[word]-ingress-v[n]-[YYYYMMDD].md | wa-062-fellowship-ingress-v1-20260417.md |
| Schema Readiness Gate artefact | wa-[nnn]-[word]-schemagate-v[n]-[YYYYMMDD].md | wa-062-fellowship-schemagate-v1-20260417.md |
| Unit sign-off artefact | wa-[nnn]-[word]-2a-unit[N]-signoff-v[n]-[YYYYMMDD].md | wa-062-fellowship-2a-unit7-signoff-v1-20260417.md |
| Stage 2a sign-off | wa-[nnn]-[word]-2a-signoff-v[n]-[YYYYMMDD].md | wa-062-fellowship-2a-signoff-v1-20260417.md |
| Batch sign-off artefact | wa-[nnn]-[word]-2b-batch[NN]-signoff-v[n]-[YYYYMMDD].md | wa-062-fellowship-2b-batch01-signoff-v1-20260417.md |
| Coverage artefact | wa-[nnn]-[word]-2b-coverage-v[n]-[YYYYMMDD].md | wa-062-fellowship-2b-coverage-v1-20260417.md |
| Stage 2b sign-off | wa-[nnn]-[word]-2b-signoff-v[n]-[YYYYMMDD].md | |
| Chapter sign-off | wa-[nnn]-[word]-2c-ch[N]-signoff-v[n]-[YYYYMMDD].md | |
| Stage 2c sign-off | wa-[nnn]-[word]-2c-signoff-v[n]-[YYYYMMDD].md | |
| SD Pointer Review | wa-[nnn]-[word]-2b-sdreview-v[n]-[YYYYMMDD].md | |
| Existing Findings Review | wa-[nnn]-[word]-2b-findingsreview-v[n]-[YYYYMMDD].md | |
| Session log | wa-[nnn]-[word]-sessionb-sessionlog-v[n]-[YYYYMMDD].md | |

All patterns follow GR-FILE-001/007/009. All artefacts dual-written at production per Task 10.

### Self-check

- [ ] All SB-rules preserved (inherit list A.4).
- [ ] Each SB-rule has a cross-reference to its enforcement sub-task.
- [ ] Naming patterns for all new artefacts defined.
- [ ] Patterns follow GR-FILE conventions.

### Open drafting decisions

None.

---

# Part D — Instance tasks (carried forward from v3.0 unchanged)

Part D contains the instance-level findings from the fellowship run. These tasks identify what went wrong in the specific fellowship session. Per researcher direction, fellowship will be re-run after the rewrite (Part C) is complete; no remediation of the fellowship database state is planned in this task log.

These tasks are **inputs to the rewrite**: their failure patterns must be impossible to repeat under the rewritten instruction, and the self-checks in Part C sub-tasks include verification against the specific failures documented here.

Tasks 1 through 6 are reproduced below exactly as they appeared in v3.0 so that a drafter working Part C can cross-reference a specific failure and confirm the rewrite blocks it.

---

## Context update — prior working session lost

The working session in which the fellowship Session B Analysis Output run was originally executed has since crashed and is no longer available. The only surviving record of that run is the set of files produced during it. This changes the remediation landscape materially:

- The analytical context (reasoning, intermediate observations held in session memory) cannot be recovered by returning to that session.
- Reconstruction of the missing Unit 7/8/9 observations from the session's original analytical trail is not possible — the trail exists only as its written outputs, and those outputs are incomplete.
- Option A in Task 1 (reconstruct from session context) and Option B (re-run with prior context held under review) are both now materially weakened — Option A relied on the session being available to reconstruct from, and Option B on the prior analytical work being recoverable.

This context is why Task 3 is added as a systemic, forward-looking task: the current instruction set contains no sub-stage verification or download gate that would have forced the incomplete observations log into view while the session was still running. If such a gate had existed, the two failures in Tasks 1 and 2 would have been caught at the first sub-stage boundary after the gap formed — not after the session was lost.

---

## Tasks

### Task 1 — Units 7, 8, 9 missing from Stage 2a observations log

| Field | Detail |
|---|---|
| Task ID | REV-062-001 |
| Severity | **Major failure** |
| Raised | 2026-04-17 |
| Raised by | Researcher directive |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-observations-v1-20260416.md |

**What was observed**
The observations log's Progress Record (lines 79–95) declares three reading units complete with specific entry counts:

- Unit 7 (Anchor Verse Reading) — 2026-04-16 — "20 anchor verses, 19 groups, 9 terms; 35 observations; 9 SD pointers raised"
- Unit 8 (Thin-evidence Flags) — 2026-04-16 — "1 entry"
- Unit 9 (Existing Findings) — 2026-04-16 — "1 entry"

However, the narrative body of the same log contains no Unit 7, Unit 8, or Unit 9 section. The detailed content stops partway through Unit 6 at line 417 ("Unit 6 COMPLETE: 2 existing SD pointers reviewed..."), followed by a blank separator, then jumps directly to the Stage 2B header at line 423. The 35 Unit 7 observation entries, 1 Unit 8 entry, and 1 Unit 9 entry declared in the Progress Record are not present in the file. This was verified again after the re-export (see Task 2) — the gap persists.

**Why this is a major failure**
The missing content is not a trivial omission. Unit 7 is the major analytical unit of Stage 2a — anchor-verse reading under the characteristic-perspective grouping model — and is the evidentiary basis for everything downstream. All 16 findings in the Type (b) patch, all 9 new SD pointers (062-SD002 through 062-SD010), and every verse citation in the session log (2Pe 1:4, Phili 3:10, 1Jo 1:3, Psa 119:63, Isa 1:23, Eze 37:19, Pro 20:30, Isa 53:5, Hos 4:17, Mat 23:30, Ecc 9:4, Ecc 4:10, Mal 2:14, 2Cor 6:14, Job 34:8, Job 16:4) trace back to analytical observations that are asserted to exist (per the Progress Record) but are not written in the log.

**Rules violated**

- **GR-OBS-001 (non-waivable):** "Every finding, decision, gap, patch consequence, flag, and open question is written to the observations log at the moment it is determined. Nothing is accumulated in memory for later transcription. This is non-waivable. An analytical decision that exists only in memory is not recorded." The Unit 7/8/9 analysis that was declared complete but not written is precisely the pattern this rule exists to prevent.
- **GR-OBS-006 (all observations return to the database):** "Every analytical observation produced during any phase must be persisted to the database before the session closes." The observations log is the working paper that feeds the Type (b) patch. A log missing its three final units cannot be audited as the source of the findings that made it to the database.
- **GR-PROC-002 (data is authoritative, findings traceable to source):** "Every analytical finding must be traceable to a specific verse record, term entry, lexical source, correlation signal, or extract field in the current working data." The 16 findings in the patch are presented as deriving from Stage 2a observations, but those observations are not on paper. Traceability is broken at the observations log layer.
- **SB-25 (Stage 2a observations log fixed after sign-off):** "Stage 2a observations log is fixed after Stage 2a sign-off. No further writing to the Stage 2a sections is permitted after sign-off." The log was signed off (Progress Record records "STAGE 2A COMPLETE: 2026-04-16") before the Unit 7/8/9 narrative was written. Because SB-25 prohibits further writing to Stage 2a sections after sign-off, and the narrative is not present, there is no compliant path to restore the missing content to this specific log — any reconstruction is itself a new write, which SB-25 forbids against the fixed log.
- **SB-26 (Stage 2b draws only from Stage 2a):** "A Q&A answer that cannot be grounded in a named Stage 2a observation is not a valid Stage 2b answer." The Stage 2b Q&A work (28 questions processed per the session log) purportedly drew from Stage 2a observations — but the Unit 7 observations that would ground the cross-verse pattern findings and the SD pointers are not named in the Stage 2a log. Task 2 confirms this is now explicit in the re-exported log (Q&A answers cite Unit 7 as evidence but Unit 7 does not exist in the file).
- **Integrity rule SB-11:** "SD pointers are raised throughout Stage 2a at the moment of discovery per GR-OBS-001 — not accumulated for a final stage." The 9 new SD pointers are declared as Unit 7-raised in the patch metadata (`session_raised: "Analysis Output Stage 2a Unit 7"`) but the log does not show them being raised at the moment of discovery in a Unit 7 narrative — they appear only in the patch.

**Consequences**

1. The fellowship observations log cannot be used as the authoritative Stage 2a record for Session C or Session D — it does not contain the anchor-verse analysis that those sessions would need to read back to.
2. The 16 findings in `wa_session_b_findings` (already applied to the database) cannot be audited against the Stage 2a analytical trail because that trail is missing in the written record.
3. The 9 SD pointers in `wa_session_research_flags` (already applied) cannot be audited against their stated Stage 2a origin.
4. The observations log cannot be presented as a model for subsequent Session B runs — it fails GR-OBS-001, the single most-emphasised discipline in the instruction set.
5. Because Stage 2b was declared complete and the Type (b) patch was applied to the database, the defect has propagated past the point at which it could be caught by the instruction's own closure checklist. Domain A of the six-domain closure checklist ("Stage 2a observations log fixed and downloadable — File exists and contains all nine units") would have caught this; either it was not run or it was run and the failure was not noted.
6. **Added in v2.0:** The working session that produced the log has crashed and is no longer available. The analytical context that would have been needed to reconstruct Unit 7/8/9 cannot be recovered. Remediation Option A (reconstruction from session context) and Option B (re-run with prior context held) are therefore materially weakened — see the Remediation Options below, updated accordingly.

**Remediation options (for researcher decision — not applied without approval; revised in v2.0 to reflect the loss of the working session)**

| Option | Action | Effect on database state | Compliance posture |
|---|---|---|---|
| A | Reconstruct Unit 7/8/9 narrative from the patch + session log + extract, write to a v2 of the observations log with an explicit reconstruction notice | No DB change | **Weakened further in v2.0.** The reconstruction can now only derive from the written artefacts, not from the original session's reasoning. What the log would contain is inference from the patch output backwards, not a record of the analysis that produced it. This is a narrative reconstruction of what the analysis *must have concluded*, not what it *actually considered and discarded along the way*. SB-25 still prohibits this being treated as the original log. |
| B | Re-run Stage 2a Units 7–9 from scratch against the clean extract and write the observations live, with the prior patch held under review | Hold `session_b_status = "Analysis Complete"` under review; do not mark findings obsolete yet | Restores compliance with GR-OBS-001 but invalidates the prototype claim that Stage 2b was complete. In v2.0: still viable; the original session's loss does not prevent a fresh run. This may now be the strongest option. |
| C | Accept the prototype as non-compliant and retire its outputs; mark findings and SD pointers as prototype-origin in the database pending a production run | DB flagging required; patch to mark 16 findings + 9 SD pointers with a `prototype_origin` disposition | Clean position but requires researcher decision on how the database carries prototype artefacts. |
| D | Do nothing; accept the log as-is | No change | Non-compliant. Not recommended. |

**Recommendation for later discussion (not a decision now)**
With the working session now lost, Option A is significantly weakened — a reconstruction based only on the downstream artefacts cannot fairly be described as a Stage 2a log. Option B or C remains the more defensible path. Final decision held until the review is complete.

**Next action**
Hold. Remediation will be decided after the full review is complete and all tasks are accumulated in this log.

---

### Task 2 — Re-export did not close the gap; Stage 2B Q&A material was added over a missing Stage 2A

| Field | Detail |
|---|---|
| Task ID | REV-062-002 |
| Severity | **Major failure** |
| Raised | 2026-04-17 |
| Raised by | Researcher requested re-export; review confirmed gap persists |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-observations-v1-20260416.md (re-exported version) |

**What was observed**
Researcher returned to the prior working session, requested a re-export, and asked that session to confirm the output was complete. A new zip was supplied. Comparison of the two observations logs:

| File | Original zip | Re-exported zip | Delta |
|---|---|---|---|
| Observations log size | 23,017 bytes | 38,365 bytes | +15,348 bytes (+67%) |
| Line count | 448 | 629 | +181 lines |
| Unit 1–6 bodies | Present | Present (unchanged) | — |
| Unit 7/8/9 bodies | **Absent** | **Still absent** | No change |
| Stage 2B Q&A section | Absent | **Newly present** (lines 447–624, 28 questions) | Added |

The three other files in the zip (session log, patch v2, patch compliance update log, analysis output instruction) are byte-identical between the two zips (same MD5s).

**Why this is a separate failure from Task 1, not a duplicate**
Task 1 is the original omission: Unit 7/8/9 analysis was never written. Task 2 is a verification failure: when asked to confirm the file was complete, the prior session re-exported the file, added more content *on top of* the same gap, and declared it complete. The new content — Stage 2B Q&A pairs — explicitly references the missing Unit 7 as its evidence base. For example, line 453 of the re-exported log states:

> Q001: What is [word]'s structural disposition?
> **Evidence:** Unit 1 registry overview, Unit 4 group landscape, **Unit 7 anchor verse analysis**

The Unit 7 anchor verse analysis named as evidence does not exist in the file. This is SB-26 written out verbatim as a live failure — a Q&A answer cites a Stage 2a observation that is not named in the log — and it was added *after* the researcher asked the session to verify completeness.

**Rules violated (on top of those in Task 1)**

- **GR-PROG-009 (inferential is not confirmed — label accurately):** "Where a connection, claim, or classification is theologically plausible or analytically reasonable but is not directly supported by data in the current extract, it is labelled inferential." The prior session declared the file complete without opening it and verifying every claimed Unit against its declared entry count. Declaration without verification is an unconfirmed claim presented as confirmed.
- **GR-PROC-001 (step-by-step, complete each step before proceeding):** "Each step must be fully complete before the next begins. No step is skipped, abbreviated, or deferred." Stage 2a was not complete (Unit 7/8/9 unwritten), yet Stage 2B proceeded, and Stage 2B Q&A material was added to the log.
- **SB-25 (Stage 2a observations log fixed after sign-off):** The re-export added content to the log after Stage 2a was declared complete. Whether this content is Stage 2B Q&A (technically a new section) or Stage 2A reconstruction, the question of whether the log was ever in a "fixed" state has become ambiguous. If the log was fixed at the first "STAGE 2A COMPLETE" declaration on 2026-04-16, then adding Stage 2B content to it in the re-export is adding to the file that was supposed to be the fixed Stage 2A record. If the log was never fixed, then SB-25 was never operationally applied.
- **SB-26 (Stage 2b draws only from Stage 2a, via a named observation):** Explicitly violated at line 453 and throughout the Q&A section — multiple Q&A answers cite "Unit 7 anchor verse analysis" as evidence when no Unit 7 section exists in the file.

**Consequences**

1. A verification request produced an extended defect, not a resolution. The file is now larger, contains more claims, and has more SB-26 violations than before, while the original gap remains.
2. The researcher's ability to trust prior-session self-reports of completeness is now negative evidence. A session asked to confirm completeness can produce output that claims completeness while extending the non-compliance.
3. Because the prior working session has now crashed and is no longer available, the researcher cannot go back a third time and ask for the missing Unit 7/8/9 content directly from that context. The window for recovering from that specific session has closed.
4. The combined effect of Tasks 1 and 2 is a test-case failure of the current instruction's verification architecture: the closure checklist exists only at the very end of Analysis Output, and nothing earlier in the flow would have forced the Unit 7/8/9 gap into view.

**Next action**
Hold with Task 1. Task 3 below is the systemic response.

---

### Task 3 — Sub-stage verification and per-sub-stage download discipline required

| Field | Detail |
|---|---|
| Task ID | REV-062-003 |
| Severity | Process gap — systemic |
| Raised | 2026-04-17 |
| Raised by | Researcher directive, following loss of prior working session and confirmation that Tasks 1 and 2 cannot be caught by the existing rule set |
| Status | Open |
| Target artefacts | wa-sessionb-analysis-output-v1_1-20260416.md (primary); wa-global-general-rules-v2_5-20260416.json (secondary, if rules need elevation to global status); any other processing instruction with multi-step sub-stages |

**What the researcher directed**

Two disciplines to be added:

1. **Verify completeness during each sub-stage** — not only at end-of-stage closure — so that a gap in one sub-stage is caught before the next sub-stage begins.
2. **Download all outputs at every sub-stage** — not only at stage close — so that if a working session crashes mid-stream, the researcher holds the files up to the last completed sub-stage rather than depending on the session's final export.

**Why this is now necessary**

The fellowship Session B run has demonstrated, through Tasks 1 and 2, that:

- Unit 7, Unit 8, and Unit 9 of Stage 2a were all declared "COMPLETE" in the Progress Record without any of the three being written to the log (Task 1).
- A second export, requested to verify completeness, did not catch the same gap — and in fact extended the file with Stage 2B Q&A content that cites the missing Unit 7 as evidence (Task 2).
- The working session that produced both of these outputs has since crashed and is no longer available. There is no third attempt possible against that context.

The existing instruction set contains completeness gates, but they sit at the wrong layer:

- GR-OBS-001 (write-on-discovery) is non-waivable but is a *behavioural* rule, not a *verification* gate. It can be violated by a session that simply fails to comply.
- GR-PROC-001 (step-by-step) is a *discipline* rule and is similarly behavioural.
- GR-FILE-008 (dual-write) and GR-PASS-001 (download at pass close) operate at *pass* granularity, which for Analysis Output Stage 2a means one download for all nine units combined — not one per unit.
- The six-domain closure checklist in Analysis Output v1.1 runs at the very end of Stage 2c. In the fellowship case, the session crashed before closure was reached, so this checklist never ran.

The gap in the rule set is between GR-OBS-001 (write as you go) and the closure checklist (check at the end). In between — during the nine Stage 2a units, during the batches of Stage 2b Q&A, during the six Stage 2c chapters — there is no per-sub-stage verification-and-download gate. The fellowship failure sits squarely in this gap.

**Rules and instructions affected**

This task is a specification task — to design and embed the sub-stage gates in the right documents. The work will likely touch:

- **Analysis Output instruction** (wa-sessionb-analysis-output-v1_1-20260416.md) — Section "Stage 2a — Comprehensive Analysis" (unit-level sign-offs), Section "Stage 2b — Q&A Partitioning" (Q&A batch boundaries), Section "Stage 2c — Analytic Word Output" (chapter boundaries). This is the immediate target because the fellowship failure occurred here, but the same pattern likely applies elsewhere.
- **Global rules** — possibly a new GR-PASS or GR-OBS rule codifying the sub-stage verify-and-download discipline, if the discipline is cross-instruction rather than specific to Analysis Output. The scope test in the global rules file (document header) states: *"A rule belongs in this file if it governs the programme's mechanics, conventions, processes, or data artefacts across more than one instruction or phase."* Sub-stage verification likely passes this test, since Session D, Dimension Review, and other instructions also have sub-stages. To be confirmed in the design step.
- **Other processing instructions** with sub-stages — Dimension Review, Verse Context, Session D Orientation — to be audited for the same gap after the discipline is designed.

**Proposed design elements (for researcher decision — not applied without approval)**

The following are the elements the new discipline should likely contain. These are starting points for design, not the final rule text.

1. **Per-sub-stage sign-off with written-content verification.** At the end of every sub-stage (Stage 2a unit, Stage 2b batch, Stage 2c chapter), the session must verify that the observations-log or deliverable actually contains the content declared in its progress statement. The verification is not "I have written it"; it is a re-read of the file contents against the declared entry count, with the result recorded in the log. Proposed form: `Sub-stage [identifier] verification: file contains [n] entries. Progress Record declares [n] entries. Match: YES / NO.`

2. **Per-sub-stage file download to outputs directory.** The observations log and any other sub-stage deliverable is written to /mnt/user-data/outputs at the end of every sub-stage — not only at end-of-stage. The filename does not change (same working file, overwrite permitted in outputs since GR-FILE-004's no-overwrite rule applies to versioned deliverables, not to in-flight working files). If the rule conflicts with GR-FILE-004 as written, the design step must clarify or amend.

3. **Hard gate on the next sub-stage.** The next sub-stage does not begin until (1) the previous sub-stage's content verification has passed and been recorded, and (2) the file has been successfully written to the outputs directory and confirmed. This is a hard gate, not a soft discipline.

4. **Crash-resumption clause.** If a session crashes, the researcher attaches the most recent sub-stage download and the session resumes from the sub-stage boundary. The resumed session reads the attached file as the authoritative record of work done up to that point and continues from the next sub-stage.

5. **Applicability to all multi-sub-stage instructions.** The discipline is written generically (at global rules level if confirmed cross-instruction) and each instruction identifies its own sub-stage boundaries.

**Consequences of adopting this discipline**

- **Positive — primary purpose:** Tasks 1 and 2 become operationally impossible in future runs. A missing Unit 7 would be caught at the Unit 7 verification gate before Unit 8 could begin, not at final closure. A session crashing after Unit 6 would leave the researcher with Units 1–6 in the outputs directory, and the next session would resume from Unit 7.
- **Cost — session overhead:** Each sub-stage adds a verification step and a file-write step. For Analysis Output, this is nine additional verifications in Stage 2a, some number in Stage 2b (depending on batch design), and six in Stage 2c. Modest but real overhead.
- **Cost — rule-surface expansion:** One new rule (or small cluster of related rules) added to the global rules or to Analysis Output. Each rule that goes into the global file must justify itself against the cross-instruction scope test.
- **Interaction with SB-25 (Stage 2a fixed after sign-off):** The per-sub-stage download does not conflict with SB-25 as long as the sign-off point remains at Stage 2a close, not at individual unit close. Units are "written and verified" but not "fixed" until Stage 2a overall is signed off. To be confirmed in the design step.
- **Interaction with existing closure checklist:** The closure checklist remains as-is; it becomes the final audit rather than the first line of defence. The sub-stage gates are the first line; closure is the safety net.

**Next action**
Hold. This task feeds the design of a specification update once the full review is complete. The design step will produce: (1) a proposal for the new rule(s) in global rules or in Analysis Output; (2) an audit of other instructions for the same gap; (3) an updated instruction document with the gate embedded at each sub-stage boundary.

---

### Task 4 — Required Type (b) link operations absent from patch; Closure Domains D and E both silently failed

| Field | Detail |
|---|---|
| Task ID | REV-062-004 |
| Severity | Major failure — patch coverage defect |
| Raised | 2026-04-17 |
| Raised by | Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md) Observation 1 |
| Status | Open |
| Target artefacts | wa-062-fellowship-patch-sessionb-v2-20260416.json (fellowship-specific evidence); Analysis Output instruction v1.1 (for prevention mechanism); possibly wa-patch-specification-v1_14-20260416.md |

**What was observed**

The Type (b) patch contains 26 operations: 16 `wa_session_b_findings` inserts, 9 `wa_session_research_flags` inserts, and 1 `word_registry` update. **It contains zero `wa_finding_catalogue_links` inserts and zero `wa_finding_entity_links` inserts.** The database extract confirms both link tables are empty for registry 62 — `finding_catalogue_links: 0 items`, `finding_entity_links: 0 items`.

The Analysis Output instruction v1.1, Section "Type (b) Patch Construction — Step 1: Compile patch operations from Q&A Log", explicitly lists three insert operations per finding:

> For each ANSWERED or PARTIALLY ANSWERED Q&A entry that produces a new finding:
> - One `wa_session_b_findings` INSERT per finding
> - One `wa_finding_catalogue_links` INSERT per finding-question pair
> - One `wa_finding_entity_links` INSERT per finding-term/verse/group link

Two of the three were not produced.

The closure checklist has two distinct domain gates that test for these operations:

- **Domain D — Entity links:** "Every active finding in `wa_session_b_findings` has at least one `wa_finding_entity_links` row — No orphan findings — Fail action: Add entity links via supplementary patch"
- **Domain E — Catalogue links:** "Every active finding has a `wa_finding_catalogue_links` row with `status IN ('suggested','validated')` — No findings without catalogue link — Fail action: Return to Stage 2b; assign links"

Both gates would fail for fellowship. Neither was caught. The fellowship session crashed before final closure could run, but even setting that aside: the patch was produced, presented for approval, applied to the database, and declared complete — with two required table coverages missing.

**Why this is a separate task, not a sub-item of something earlier**

Tasks 1 and 2 are about the Stage 2A observations log. Task 3 is about sub-stage verification. Task 4 is about the patch: what operations the Type (b) patch must contain versus what it actually contains. A session that wrote a clean observations log could still produce this defect — the patch is a separate artefact with its own integrity requirements. Preventing Task 1/2 does not prevent Task 4.

Further, Task 4 has a wider scope than Task 1/2. The observations-log gap affects only fellowship. This patch-coverage gap **will repeat on every Session B run** unless a prevention control is added, because there is currently no artefact-level requirement in the patch construction step that forces the session to enumerate every finding and confirm one catalogue-links row and at least one entity-links row exists for each before the patch is submitted. The current instruction lists the required operations as prose; it does not enforce a coverage check.

**Rules and instructions violated**

- **Analysis Output v1.1, "Type (b) Patch Construction — Step 1":** The required three operations per finding were not produced. Two of three were silently omitted.
- **Analysis Output v1.1, Closure Domain D (entity links):** No entity-links rows exist. Would fail the gate.
- **Analysis Output v1.1, Closure Domain E (catalogue links):** No catalogue-links rows exist with appropriate status. Would fail the gate.
- **GR-PROC-001 (step-by-step — complete each step before proceeding):** Step 1 of Type (b) Patch Construction enumerates three operation types per finding. Only one of three was executed.
- **GR-OBS-006 (all observations return to the database):** The Q&A log's entity links (the `**Entity links:**` field under each ANSWERED Q&A row, for example "Terms G2844 (koinōnos), G2842 (koinōnia), H2270 (cha.ver), H2266 (cha.var)") were written into markdown but never persisted to `wa_finding_entity_links`. Per GR-OBS-006, observations that exist only in markdown have not been recorded for the programme.

**Consequences**

1. The 16 findings in the database are orphaned from the evidence that supposedly supports them. Session C cannot programmatically retrieve "the findings for Q001" because there is no link table row to join through.
2. Session D cannot use the catalogue as an index to cross-registry synthesis work — the linkage that would make this possible does not exist.
3. Closure Domain D and E would have caught the defect, but only if closure had run. In fellowship's case it did not (the session crashed first), but even in a clean future session the patch is presented *before* closure runs — so the defect is currently invisible until closure, by which point the patch has already been applied. This is the same late-catch problem Task 3 identifies in a different form.
4. This defect was also *claimed as validated* in the session log, which stated: "Findings properly linked to evidence verses and catalogue questions — validated." The claim is false against the written artefact. This is a second instance of the pattern named in Task 2 (session self-reports contradicting the evidence).

**Prevention proposed (for researcher decision — not applied without approval)**

Add a **patch coverage check** to Analysis Output Stage 2b, between Step 2 (list all operations in observations log) and Step 3 (construct the patch). The check is a three-column table produced in the observations log before the patch JSON is written:

| finding_id | catalogue-links rows planned | entity-links rows planned |
|---|---|---|

Each of the 16 findings gets a row. Each row must have ≥1 catalogue-links entry (the Q-code from the Q&A partitioning) and ≥1 entity-links entry (the terms/verses/groups named in the Q&A pair's Entity links field). The row is blank only if the finding is genuinely orphan — which the instruction does not currently permit.

The coverage check is recorded in the observations log. Proposed entry form: `Patch coverage check: [n] findings × [n] catalogue links × [n] entity links. All findings covered. Proceed to Step 3.`

If the coverage check is not present in the observations log, the patch is not submitted. This is a hard gate.

This complements the six-point format compliance check already added in Analysis Output v1.1 (which only checks JSON structure, not table coverage). The six-point check was the remedy for the v1→v2 patch correction recorded in wa-patch-compliance-updates-sessionlog-v1-20260416.md. A coverage check is the missing second dimension.

**Next action**
Hold. Design the coverage check during the spec-update step with Task 3. The two remedies are naturally paired: sub-stage verification (Task 3) + artefact coverage check (Task 4) together close the gap between "the work was not written" and "the work was written but not persisted".

---

### Task 5 — Session log counts and status distribution do not match the observations log they summarise

| Field | Detail |
|---|---|
| Task ID | REV-062-005 |
| Severity | Major — self-verification failure (same class as Task 2) |
| Raised | 2026-04-17 |
| Raised by | Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md) Observation 2 |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-complete-sessionlog-v1-20260416.md |

**What was observed**

The session log summarises the Stage 2B Q&A work with these figures:

> STAGE 2B COMPLETE: Q&A partitioning and Type (b) patch construction
> - 28 questions processed from 194-question universal catalogue
> - 17 answered, 4 partially answered, 7 not answered
> - 16 structured findings derived from Q&A analysis

The observations log — the source document — actually contains:

| Metric | Session log claim | Observations log reality | Match |
|---|---:|---:|---|
| Q&A pairs written | 28 | 20 | ✗ |
| ANSWERED | 17 | 15 | ✗ |
| PARTIALLY ANSWERED | 4 | 2 | ✗ |
| NOT ANSWERED | 7 | 2 | ✗ |
| NOT APPLICABLE | 0 (not mentioned) | 1 | ✗ |
| Findings (the one figure that does agree) | 16 | 16 findings in DB | ✓ |

Every count except the findings count is wrong. The session log total of 28 (17+4+7) does not sum internally either — 17+4+7=28 but also fails to account for NOT APPLICABLE dispositions that the instruction's catalogue requires.

**Why this is a separate task, not a sub-item of Task 2**

Task 2 covers one specific instance of the same pattern: a session that was asked to verify completeness and did not. Task 5 covers a structurally adjacent instance: a session log written at the end of Stage 2B that summarises work the session itself had just done, using numbers that do not match the file the session itself had just written. The mechanism is the same — numbers from session memory, not from the artefact — but the remedy is different. Task 2's remedy is about cross-session verification after a crash; Task 5's remedy is about in-session verification when summarising your own work.

**Rules violated**

- **GR-PROG-009 (inferential is not confirmed — label accurately):** The session log presents summary counts as confirmed facts. They are not. They appear to be approximations from session memory, which per GR-PROG-009 must be labelled inferential until verified against the source document.
- **GR-OBS-003 (session log is the handoff record):** "The session log is the handoff record — what was accomplished, what is confirmed, where the next session picks up." A handoff record with numbers that contradict the underlying working file breaks the handoff. The next session resumes with wrong information about what was done.
- **GR-PROC-002 (data is authoritative, findings traceable to source):** "Every analytical finding must be traceable to a specific verse record, term entry, lexical source, correlation signal, or extract field in the current working data." The session log's counts must be traceable to the observations log. They are not.
- **GR-PROC-005 (observations log governs — not memory):** "The observations log is the authoritative record of what has been done in a session... Claude AI does not rely on memory for the current state of work — it reads the observations log." The session log appears to have been written from memory, not from a read of the observations log. This is the exact failure mode GR-PROC-005 exists to prevent.

**Consequences**

1. The session log cannot be trusted as the handoff record. If this session log had been the only survivor (which, given that the working session has now crashed, it nearly is), the next researcher or Claude instance would believe 28 questions were processed across 17/4/7 when only 20 were processed across 15/2/2/1.
2. The finding count of 16 accidentally agreed — which is worse than disagreeing, because it creates false confidence that the other counts were also produced by the same verification process. They were not; they agreed by chance with the patch operation count.
3. This is the second instance of a session summarising its own work without reading its own file. Task 2 is the first (re-export asked to verify completeness, did not). A third would establish this as a systemic pattern that prevention rules must address head-on.

**Prevention proposed (for researcher decision — not applied without approval)**

Add a **summary derivation rule** to GR-OBS or GR-PROC: every summary number in a session log must be derived by a verifiable read of the source artefact, not from session memory. For counts of written items, the verification is mechanical: count the occurrences of the heading pattern in the source file, record the count, and compare against any running total held in memory. If they disagree, the session memory is wrong.

Proposed rule text (draft — to be refined in the spec-update step):

> **GR-OBS-007 (proposed) — Session log summary counts must be derived from source read.** Every numerical count in a session log (findings written, Q&A pairs produced, SD pointers raised, observations entered, etc.) must be derived by reading the current contents of the source artefact at the time the session log is written — not from running totals held in session memory. The derivation method is recorded alongside the count. If a running total in memory disagrees with the artefact count, the artefact count is authoritative.

This is a separate rule from Task 3's sub-stage verification because Task 3 gates *progression* (cannot start Unit 8 until Unit 7 is verified), while this rule gates *reporting* (cannot close a session log with unverified numbers). They are complementary.

**Relation to Task 3**
Task 3's per-sub-stage verification step (`file contains [n] entries. Progress Record declares [n] entries. Match: YES / NO.`) is essentially the in-flight version of this rule. Task 5's rule is the end-of-session version. If Task 3 is adopted, Task 5's rule may be a natural extension of the same mechanism rather than a separate rule — design step to decide whether this is one rule or two.

**Next action**
Hold. Bundle with Task 3 and Task 4 for the spec-update step.

---

### Task 6 — Q&A partitioning did not walk the catalogue sequentially as the instruction requires

| Field | Detail |
|---|---|
| Task ID | REV-062-006 |
| Severity | Instruction non-compliance |
| Raised | 2026-04-17 |
| Raised by | Q&A three-way comparison (wa-062-fellowship-qa-catalogue-comparison-v1_1-20260417.md) Observation 3 |
| Status | Open |
| Target artefact | wa-062-fellowship-sessionb-observations-v1-20260416.md (fellowship-specific evidence); Analysis Output instruction v1.1 Stage 2B (for prevention mechanism) |

**What was observed**

The 20 Q&A pairs written in the observations log carry these question codes, in the order they appear in the file:

> Q001, Q002, Q003, Q004, Q005, Q006, Q007, Q008, Q009, Q010, Q011, Q012, Q013, Q014, Q015, Q017, Q020, Q026, Q051, Q076

Codes missing or skipped: Q016, Q018, Q019, Q021–Q025, Q027–Q050, Q052–Q075, Q077–Q194. Of 194 catalogue questions, 174 are untouched; the 20 that were processed cover Q001–Q015 contiguously and then jump — Q017, Q020, Q026, Q051, Q076 — with no declared reason for the jumps.

The Analysis Output instruction v1.1, Section "Q&A Partitioning Process", Step 1, states:

> Work through the catalogue sequentially. For each question: [Step 1] Read the question and domain. [Step 2] Search Stage 2a observations. [Step 3] Assign disposition. ...

The instruction is explicit. The catalogue is to be walked in order. The session did not do this.

I want to be careful here. The session log states the run was "prototype scope: 28 of 194 questions (14.4% of catalogue)". A prototype scope that processes fewer than all 194 questions is not by itself an instruction violation — the instruction does not say "all 194 must be processed in one sitting", and nothing prohibits a prototype. But the order in which the prototype processed questions does violate the sequential-walk rule. A prototype that covers Q001–Q028 contiguously is different from a prototype that cherry-picks Q017, Q020, Q026, Q051, Q076 from across the catalogue.

**Why this matters beyond the prototype**

The sequential-walk rule is not a stylistic preference — it is a methodological control. The catalogue is organised by section (Section 1 — Word Characteristic Summary, Section 2 — Word Impact Description, etc.), and the sections have a sequence that reflects how the analysis is meant to build. Section 3 (Annotated Verse Evidence, 44 questions) comes after Section 1 and 2 because verse-level evidence is meant to be framed by the word-characteristic and word-impact questions first. Jumping from Q017 (Section 1) to Q076 (partway through Section 3) skips the intervening framing, and any Q076 answer produced without the preceding questions is producing evidence-level answers without the characteristic framing that was meant to shape them.

In the fellowship case specifically: the skip from Q015 to Q051, Q076 means Sections 1 and 2 are largely unaddressed (Section 1: 15 of 20 addressed; Section 2: 1 of 21 addressed), but Section 3 was not systematically worked either (only Q051 and Q076, out of 44 Section 3 questions). This is not a prototype — it is a sampling pattern, and a sampling pattern that bypasses the instruction's intended analytical build.

**Rules violated**

- **Analysis Output v1.1, "Q&A Partitioning Process" Step 1:** "Work through the catalogue sequentially." Direct non-compliance.
- **GR-PROC-001 (step-by-step — complete each step before proceeding):** Each catalogue question is a step in Stage 2B. Skipping from Q015 to Q017, then to Q020, then to Q026 etc., skips steps. The intervening questions are not declared not-applicable or not-answered — they are simply absent.
- **GR-PROG-003 (dimensions are data-derived):** Related indirectly — sampling bypasses the evidentiary build that the sequential walk enforces. A finding derived from Q076 without the preceding questions having been considered is not benefiting from the catalogue's framing sequence.

**Consequences**

1. The 16 findings in the database are derived from a non-sequential sample of the catalogue. The evidential standing of each finding is not the same as it would be if the full catalogue were walked — not because the findings are wrong in themselves, but because the questions that would have contextualised and possibly contradicted them were not asked.
2. A prototype scope limit is legitimate. Cherry-picking from within that scope is not legitimate under the current instruction. The session log labels its work a "prototype" but the prototype itself is internally inconsistent — Q001–Q015 sequential, then cherry-picked.
3. If other Session B runs follow the same pattern (cherry-pick from the catalogue under a prototype label), the programme's analytical outputs become a set of findings that sample the catalogue differently per word. Cross-word comparison in Session D then compares apples from different orchards.

**Prevention proposed (for researcher decision — not applied without approval)**

Add an **ordered-processing enforcement** to Analysis Output Stage 2B. Two candidate designs, either of which addresses the issue:

**Design A — Strict sequentiality.** The session must process Q001, Q002, Q003, …, in order. A question may not be started until the prior question has a disposition (ANSWERED / PARTIALLY ANSWERED / NOT ANSWERED / NOT APPLICABLE). A prototype scope of "first N questions" is permitted; a prototype scope of "selected questions" is not.

**Design B — Declared partition.** The session may process a *contiguous range* or a *named section* at a time (Section 1 in full, then Section 2 in full, etc.). The range or section is declared at the start. Partial coverage of a section is permitted only if declared and labelled, so the gap is visible rather than implicit.

My preference (for researcher discussion, not a decision) is Design B with one amendment: the six catalogue sections the extract names (Section 1–5 + the four "Extensions" sections) are natural partitions. The session declares which sections are in scope for the run and works each declared section sequentially. Unfinished sections are flagged in the session log with the question codes still to be processed.

Either design is a tightening of the current instruction text. The current text says "sequentially" but does not define what sequential means or how it is enforced. The fellowship case shows that "sequentially" alone is not operationally sufficient.

**Relation to Task 3**
Task 3's sub-stage verification gate applies naturally at *catalogue section* boundaries as well. A "Stage 2B sub-stage" could be defined as "one catalogue section fully worked" — at which point the session verifies all questions in that section have a disposition and the coverage matches the section's question count. This would bind Tasks 3, 4, 5, and 6 into a single unified gate at the section boundary. Design step to decide.

**Next action**
Hold. Bundle with Tasks 3, 4, 5 for the spec-update step. Tasks 3–6 together define a single integrated prevention architecture for Analysis Output Stage 2B going forward.

---
---

## Final summary of all tasks

| ID | Title | Class | Part | Status |
|---|---|---|---|---|
| REV-062-001 | Units 7, 8, 9 missing from Stage 2a observations log | Instance failure | D | Open — held pending rewrite |
| REV-062-002 | Re-export did not close the gap; Stage 2B Q&A material added over missing Stage 2A | Instance failure | D | Open — held pending rewrite |
| REV-062-003 | Sub-stage verification and per-sub-stage download discipline required | Prevention proposal | D | Absorbed into Tasks 8, 10; held |
| REV-062-004 | Required Type (b) link operations absent from patch; Closure Domains D and E failed | Instance failure | D | Open — held; rewrite prevents via Task 9 |
| REV-062-005 | Session log counts and status distribution do not match observations log | Instance failure | D | Open — held; rewrite prevents via Task 9 |
| REV-062-006 | Q&A partitioning did not walk catalogue sequentially | Instance failure | D | Open — held; rewrite prevents via Task 8 |
| REV-062-007 | Governing principle for the rewrite (three claims) | Rewrite foundation | A (Part A.2) | Open — applied in every rewrite sub-task |
| REV-062-008 | Completeness enforcement across every sub-stage | Rewrite principle | B | Open — applied in Tasks 12.5, 12.6, 12.7, 12.9 |
| REV-062-009 | Coverage enforcement for required outputs and artefacts | Rewrite principle | B | Open — applied in Tasks 12.4, 12.7, 12.8 |
| REV-062-010 | Safeguarding and crash-resilient resumption | Rewrite principle | B | Open — applied across all 12.x sub-tasks |
| REV-062-011 | Memory management and state discipline | Rewrite principle | B | Open — applied across all 12.x sub-tasks |
| REV-062-012 | Produce the rewritten Analysis Output instruction v2.0 | Rewrite drafting umbrella | C | Open — 11 sub-tasks (12.1–12.11) |
| REV-062-012.1 | Metadata, Change Log, Governing Rules | Rewrite drafting | C | Open |
| REV-062-012.2 | Pipeline Position, What to Attach | Rewrite drafting | C | Open |
| REV-062-012.3 | Governing Disciplines | Rewrite drafting | C | Open |
| REV-062-012.4 | Schema Readiness Gate as enforceable ingress | Rewrite drafting | C | Open |
| REV-062-012.5 | Stage 2a Purpose, Outputs, Nine Reading Units | Rewrite drafting | C | Open |
| REV-062-012.6 | Stage 2a Sign-Off | Rewrite drafting | C | Open |
| REV-062-012.7 | Stage 2b Q&A Partitioning Process | Rewrite drafting | C | Open |
| REV-062-012.8 | SD Pointer Review, Existing Findings Review, Type (b) Patch, Stage 2b Sign-Off | Rewrite drafting | C | Open |
| REV-062-012.9 | Stage 2c Six Chapters, Stage 2c Sign-Off | Rewrite drafting | C | Open |
| REV-062-012.10 | Closure | Rewrite drafting | C | Open |
| REV-062-012.11 | Integrity Rules, Naming Conventions | Rewrite drafting | C | Open |

---

## Closing notes

**Task count.** 12 top-level tasks, with Task 12 broken into 11 drafting sub-tasks for a total of 22 numbered items. This is deliberately granular so that each rewrite session can execute one clearly scoped piece of work.

**Relation to researcher decisions.** Three open drafting decisions are noted in Part B and Part C:
1. Batch size for Stage 2b (Task 8).
2. Adoption of additional finding types (Task 9).
3. Session log versioning frequency (Task 10).

These are resolvable at drafting time with researcher input. None blocks the start of the drafting work. Each should be raised as RESEARCHER_DECISION per GR-RD-002 at the point the relevant Part C sub-task is executed, if not earlier.

**Expected duration.** Eleven drafting sub-tasks at one per session (researcher preference as stated: rewrite in multiple sessions is expected). Actual duration depends on sub-task complexity; Tasks 12.5, 12.7, 12.8 are substantial (Stage 2a nine units; Stage 2b walk; Stage 2b patch) and may require dedicated full sessions each.

**Success criterion.** The rewritten instruction (v2.0) is adopted when all 11 Part C sub-tasks are closed and their self-checks passed, all open drafting decisions are resolved, and the integrated document is reviewed against Task 7's three-part test at the whole-document level.

**Companion session log.** Full deliberation record is in `wa-062-fellowship-review-sessionlog-v1-20260417.md`. Read it if the wording of a task is unclear or if a drafting decision appears to conflict with another.

---

*wa-062-fellowship-review-tasks-v4-20260417.md*
*Version 4.0, 2026-04-17 — Fellowship Analysis Output Review with rewrite programme*
*Supersedes wa-062-fellowship-review-tasks-v3-20260417.md*
