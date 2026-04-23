# Chapter 6 — Instruction Corpus — Section-List Proposal

**File:** wa-prose-ch6-section-proposal-v1_0-20260423.md
**Date:** 2026-04-23
**Previous output:** wa-prose-ch6-obslog-v1_0-20260423.md
**Status:** Proposal for researcher review. No slot inserts, no prose bodies, no patches authored.

---

## Purpose

Chapter 6 is a brief description of each instruction that is used as a formal input to the programme. It does not restate governance principles (those live in Ch3 and Ch5) and it does not go into operational detail of the instructions themselves. Each section is a short portrait — what the document is, what it governs, what it is not.

Order follows researcher direction: global rules → references → all others → patches and directives (including CC operating guide as a method instruction).

Length range per slot: 150–300 words — brief-description register, matching the shortest Ch1 slots rather than the expository Ch3/Ch5 slots.

---

## Proposed sections

| sort_order | code | label | description | length |
|---|---|---|---|---|
| 110 | prog_instr_global_rules | Global rules | The single file of programme-wide binding rules — what it is, its current JSON form held in `wa_rule_registry` and exported as the session-start extract, and its role as the file read before any other instruction at every session start. Points to GR-LOAD-001 for the load gate without restating it. | 150–300 |
| 111 | prog_instr_reference | Reference | The single reference document holding controlled vocabularies, schema field definitions, and file-naming extensions — what it is, its current JSON form held in `wa_vocab_set` + `wa_vocab_member` + schema tables and exported as the reference snapshot, and its role as the authoritative lookup for any vocabulary, schema, or naming question. | 150–300 |
| 112 | prog_instr_registry_guide | Registry management guide | The reference guide for registry terminology, structure, status lifecycle, the OWNER/XREF distinction, cluster assignments, and registry-level integrity queries — what it is, what it covers, and the deliberate self-description as "reference guide, not an operational instruction". | 150–300 |
| 113 | prog_instr_session_a | Session A — extraction | The pipeline-stage instruction for the first stage: mechanical extraction of Hebrew/Greek term data from STEP Bible into the database, assembly of the complete word data export, and handoff to Verse Context. What the stage produces; the docx form it currently sits in. | 150–300 |
| 114 | prog_instr_verse_context | Verse Context | The pipeline-stage instruction governing the stage between Session A and Dimension Review: batch construction, relevance filtering at the term-in-verse level, contextual grouping, anchor designation, patch production, and the VCB-per-batch outputs. | 150–300 |
| 115 | prog_instr_dimension_review | Dimension Review | The pipeline-stage instruction for the cluster-level analytical stage between Verse Context and Session B: cluster coherence validation, group description quality, anchor-verse verification, dimension and dominant-subject assignment, and the Session B / Session D pointer capture that arises during review. | 150–300 |
| 116 | prog_instr_session_b | Session B — readiness and analysis | The two-instruction pair that governs Session B. Readiness covers Stage 1 — data audit, resolution-path assignment, patch accumulation, and the Stage 1 Completion Record that opens Stage 2. Analysis Output covers Stage 2 — comprehensive analysis, Q&A partitioning, analytic word output, and closure. One Session B concept split across two instructions; described as a pair. | 200–350 |
| 117 | prog_instr_session_c | Session C | The pipeline-stage instruction for the word publication layer: a single reader-facing publication document per word, written in accessible language, drawn from Session A's data export, and updated through Session B's verse/language annotations and Session D's cross-word findings. The primary articulation layer of the programme. | 150–300 |
| 118 | prog_instr_session_d | Session D | The pipeline-stage instruction for cross-registry synthesis: the phase that begins with questions about the inner life and asks what the accumulated word-study data reveals in the aggregate. Starts from the SD pointers Session B raises; produces synthesis documents at named Session D runs. | 150–300 |
| 119 | prog_instr_patches | Patches | The method instruction for one of the two DB-change mechanisms: formal JSON patches with defined operation types, filename conventions, self-check protocol, and completion confirmation. Used when field names, FK keys, and table structure are certain. Authored by Claude AI, reviewed by researcher, applied by Claude Code. | 150–300 |
| 120 | prog_instr_directives | Directives | The method instruction for the equal-peer DB-change mechanism: plain-language directives with five required elements, for changes that need reasoning beyond what a JSON patch can express — schema enablement, re-run triggers, and other operations where the form is prose-and-steps. Routing between patch and directive is defined at the boundary between the two instructions. | 150–300 |
| 121 | prog_instr_claudecode | Claude Code operating guide | The method instruction for Claude Code itself: CC's role and boundary, the data-foundation pipeline, schema and implementation tasks, JSON export workflow, Verse Context operations from CC's perspective, and the re-run mechanisms that handle upstream changes. Governs what CC does with what it receives from CAI and from the researcher. | 150–300 |

---

## Notes on the proposal

**Overlap with earlier chapters is deliberately avoided.** The rules that govern these documents (GR-REF-001, GR-REF-002, GR-FILE-001 to GR-FILE-009, GR-LOAD-001, GR-PROG-005) are not restated in Ch6. Ch5 sort=108 holds the cross-document reference discipline and the instruction override protocol; Ch3 sort=16 holds the CAI/CC authority division; Ch3 sort=18 holds the tools context. Ch6 describes *what the instructions are*; the earlier chapters describe *how they are governed*.

**Pairing.** Only the Session B pair is combined into a single slot (117). Patches and directives are kept as separate slots because they are separate documents with separate scopes; the decision logic between them is already held within each document and does not need a bridge slot.

**Retired documents.** The researcher confirmed `wa-global-flags` is retired. No slot is proposed for it. FLAG-CORP-01 is held open in the obslog for a downstream reference-sweep of documents still carrying `wa-global-flags [current]` references (registry management guide at minimum).

**Slot count.** 12 slots total (110–121). Chapter 5 has 7; Chapter 3 has 6; Chapter 4 has 10. Ch6 at 12 is consistent with the fuller chapters. If a shorter chapter is preferred, the candidates for consolidation are: (a) Session A + Verse Context + Dimension Review into a single "pipeline stages — up to Session B" slot; (b) patches + directives + claudecode into a single "method instructions" slot. Both consolidations would cost the portrait-per-document register the researcher asked for, so I default to the expanded form above.

---

## What researcher review decides

1. Does the 12-slot structure fit, or should it consolidate (e.g. Session A/VC/DR into one slot; or method instructions into one slot)?
2. Are the slot codes acceptable in the `prog_instr_*` namespace, or should they follow a different pattern?
3. Is the 150–300 word length range right, or should it expand/contract?
4. Are the sort_order numbers (110–121) acceptable, or should they sit elsewhere?
5. On approval — proceed to author prose bodies and then the two patches (CATALOGUE_POPULATION for slot inserts; PROSE for bodies).

---
