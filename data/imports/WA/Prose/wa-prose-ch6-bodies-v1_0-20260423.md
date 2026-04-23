# Chapter 6 — Instruction Corpus — Prose Bodies

**File:** wa-prose-ch6-bodies-v1_0-20260423.md
**Date:** 2026-04-23
**Previous output:** wa-prose-ch6-section-proposal-v1_0-20260423.md
**Status:** Draft bodies for 13 Ch6 slots. For researcher review before patches are applied.

---

## Chapter note on grouping

The thirteen sections that follow describe the instruction documents the programme uses as formal inputs. They fall into four groups: the global rules and reference that every session loads; the database-and-coding method instructions that govern how changes reach the database; the registry guide that holds the terminology for the word registry; and the pipeline-stage instructions that govern the analytic process from extraction through to cross-registry synthesis. The grouping is implicit in the ordering — no dedicated group-header sections are used. The rules that govern the instruction corpus — referencing, versioning, authority, override — are not described here; those belong to Chapter 3 and Chapter 5. This chapter describes the instructions as objects. The earlier chapters govern how those objects behave.

---

## sort_order 110 — prog_instr_global_rules — Global rules

The global rules document is the single file of programme-wide binding rules. It carries every rule that applies across sessions, phases, and instructions — file naming, cadence discipline, observations-log conduct, cross-document referencing, the two-AI division of responsibility, help-forward bounds, data-discipline requirements, and the rules governing session startup itself. Rules are identified by stable codes (GR-LOAD-001, GR-REF-001, GR-OBS-001, and so on) and are cited by code throughout the rest of the instruction corpus rather than restated.

The rules are held in the database in `wa_rule_registry`, with companion guidance in `wa_addendum_registry`. The working form is a JSON extract — `wa-global-rules-extract-{YYYYMMDD}.json` — regenerated from the database whenever rules change. A parallel markdown view is produced alongside the JSON for reading. Neither extract is itself the rules: the database is canonical.

The document is read in full at the start of every session before any other instruction, extract, or data file. This is the load gate that opens every piece of work the programme does; it is described in the rules themselves and not expanded on here. The rules extract is also the compliance reference point during work: any instruction's behaviour that conflicts with a rule resolves to the rule.

The global rules are the only document in the corpus that binds every other instruction; every other document in this chapter is governed by it.

---

## sort_order 111 — prog_instr_reference — Reference

The reference is the programme's dictionary. It holds the controlled vocabularies that the database and the instructions use — dimension labels, confidence tiers, status values, resolution paths, patch types, classification outcomes — together with the schema field definitions, file-naming rule extensions, and cross-cutting lookups that the rest of the corpus points to when a vocabulary question arises.

The content lives in the database: vocabulary in `wa_vocab_set` and `wa_vocab_member`; schema definitions in the schema tables themselves; naming extensions alongside the file-naming rules. The working form is a JSON snapshot — `wa-reference-snapshot-{YYYYMMDD}.json` — regenerated when any of the underlying tables change. As with the rules, the database is canonical and the snapshot is the live read.

Any controlled-vocabulary value, any field definition, any file-naming clarification that an instruction needs is pointed at the reference rather than restated in the referring instruction. This concentration keeps vocabulary drift impossible: when a dimension label is revised, the change happens in one place and every instruction that uses the label resolves to the revised value without any document-by-document update.

The reference is loaded at session start after the rules. Together, the rules and the reference are the two documents that define what the programme's instructions mean; the rest of the corpus is written on the assumption that both are available and current.

---

## sort_order 112 — prog_instr_patches — Patches

The patches instruction is the method instruction for one of the programme's two mechanisms for changing the database. A patch is a structured JSON object with a defined shape: a `_patch_meta` header carrying identity and provenance, an `operations` array of typed operations against named tables, and a `_patch_summary` footer recording operation counts. The instruction is the authoritative reference for the shape, the allowed operation types, the filename and patch-id conventions, the self-check Claude AI runs before submission, and the completion confirmation Claude Code returns on apply.

A patch is used when the change is fully specified in data terms: the affected fields are known, the foreign keys to match on are known, and the table structure accepts the operation as written. The patch captures everything the applicator needs to execute without further interpretation.

Operations cover the full range of analytical writes: verse-context classification, pre-analysis and analysis-complete updates for Session B, dimension assignments, catalogue population, prose section inserts and supersedes, rules and addenda updates, and the REPAIR operations for cascading resets. The instruction also covers failure-patch mechanics, the supersede-only discipline on narrative prose, and the physical-delete prohibition.

Patches are authored by Claude AI, reviewed by the researcher, and applied by Claude Code. No patch reaches the database without explicit researcher approval. The patches instruction sits alongside the directive instruction as the second of the two formal change channels.

---

## sort_order 113 — prog_instr_directives — Directives

The directives instruction is the method instruction for the second mechanism for changing the database. A directive is a plain-language instruction with five required elements: a title and identifier, a statement of what is to be done and why, a specification of the operations the directive asks Claude Code to perform, a definition of the expected outcome, and the confirmation Claude Code is to return. The instruction covers the five-element format, the filename convention, the self-check before submission, and the completion confirmation protocol.

A directive is used when the change cannot be captured adequately in a JSON patch — typically because it requires reasoning, script execution, or schema preparation that a declarative operation list cannot express. Schema enablement sits here exclusively: before a class of patches can apply against a constraint the current schema does not permit (such as the `registry_id NOT NULL` relaxation that programme-wide prose required), a directive prepares the schema and a patch then carries the data.

The directives instruction and the patches instruction are equal peers: between them, they cover every database-change operation the programme uses. Either document is authoritative within its own scope; together they are the exhaustive set. Directives, like patches, are authored by Claude AI, reviewed by the researcher, and executed by Claude Code — no directive reaches the database without approval.

---

## sort_order 114 — prog_instr_claudecode — Claude Code operating guide

The Claude Code operating guide is the method instruction for Claude Code itself. It describes CC's role — executor of patches and directives, operator of the database, producer of extracts, runner of the engine and supporting scripts — and the operational routines CC performs across the pipeline.

The guide covers the data-foundation pipeline: the registration of new words, the extraction of STEP Bible data, the `audit_word` reconciliation step, and the JSON export workflow that produces the complete word data files Session B works from. It covers schema and implementation tasks, programme-state queries from CC's side, engine and script status reporting, Verse Context operations from CC's perspective including batch construction and anchor integrity, and the re-run mechanisms the programme uses when upstream data changes (the STALE_TERM mechanism and its companions). It also carries the running record of recurring anomaly resolutions.

Where the patches and directives instructions define what Claude AI asks CC to do, this guide defines what CC does with what it receives — how it validates, how it executes, how it reports back. The three documents together cover the CAI-to-CC interaction completely: patches and directives for the ask, this guide for the execution.

The guide does not restate the patch or directive format; it points to those documents. Its own authority is confined to CC's operational behaviour.

---

## sort_order 115 — prog_instr_registry_guide — Registry management guide

The registry management guide is the programme's reference document for the word registry — the central catalogue of the Hebrew and Greek terms the research investigates. The guide defines every field on `word_registry`, the status lifecycle values (`session_b_status`, `verse_context_status`), the OWNER and XREF term distinction and the pure-XREF registry pattern, the cluster assignments and the cluster processing sequence, and the registry-level audit-integrity rules and verse-accounting queries used to confirm that the registry is internally consistent.

The guide is explicitly self-described as a reference guide, not an operational instruction. It tells the reader what a field means or what a status value represents; it does not direct the reader to perform an operation. Transactional work on the registry — classification, status transitions, patch production — lives in the pipeline-stage instructions and the method instructions, not here.

The guide is the authority for registry terminology. Where an instruction needs to refer to a field meaning, a status value, or a cluster concept, the pointer comes to this document. It completes the reference layer alongside the programme's rules and the controlled-vocabulary reference: the rules say what may be done, the reference says what the vocabulary means, and this guide says what the registry itself is composed of.

---

## sort_order 116 — prog_instr_session_a — Session A — extraction

Session A is the pipeline-stage instruction for the first analytic stage. It governs the mechanical extraction of Hebrew and Greek term data from STEP Bible into the database, the reconciliation against the `audit_word` process, the assembly of the complete word data export that downstream stages work from, and the handoff to Verse Context.

The stage is mechanical in character — it runs primarily through Claude Code operations against STEP data, produces the structured per-word records that populate `wa_term_inventory`, `mti_terms`, and the supporting tables, and assembles the complete JSON export the rest of the pipeline consumes. Interpretive judgement enters only at the margins of the stage; the heavy analytical work is Session B's.

The instruction currently exists in a Word document form (version 8). This is historical — the stage predates the move to markdown for the rest of the corpus — and the document remains the authoritative reference for the stage until it is migrated. Conceptually it sits alongside the other pipeline-stage instructions; operationally the format difference reflects only the age of the document, not a difference in the stage's role.

Session A is the entry point of the analytical pipeline. Every word the programme investigates passes through this stage before any interpretive work begins; the complete data export that Session A produces is the substrate every later stage reads.

---

## sort_order 117 — prog_instr_verse_context — Verse Context

The Verse Context instruction governs the stage between Session A and Dimension Review. It covers the full cycle for a batch of words: the construction of the batch JSON from the Session A exports, the reading of every verse for every active OWNER term in the batch, the term-level relevance filter that decides which verses engage the inner being through the term, the contextual grouping that organises the relevant verses by characteristic, the anchor designation that names the primary verse for each group, and the patch production that populates the `verse_context_group` and `verse_context` tables.

The instruction distinguishes clearly between what Verse Context does and what it does not. It classifies verses and groups them; it does not analyse the meaning of the terms at depth — that is Session B's work. It produces the anchor citations Session B will use; it does not draw conclusions from them.

The stage operates in batches — typically tens of registries at a time — with each batch producing its own observations log, flags register, session log, and verse-context patch. At batch completion, Claude Code applies the patch, advances `verse_context_status` to Complete for every registry in the batch, and re-exports the full word JSON for each completed registry. This re-export is the trigger for Dimension Review.

---

## sort_order 118 — prog_instr_dimension_review — Dimension Review

The Dimension Review instruction governs the cluster-level analytical stage between Verse Context completion and Session B. It covers cluster coherence validation (confirming that registry assignments into the cluster make analytical sense), the quality assessment of every group's context description with correction where needed, the verification of anchor verse data, the discernment of dimensions that actually emerge from the groups in the cluster, the assignment of a dominant subject for every active group, the confidence progression from automated hypothesis toward researcher-confirmed anchor, the locking of confirmed dimensions via the `manual_override` flag, and the capture of Session B and Session D observations as structured pointers for later stages to resolve.

The stage is the first analytic stage where cross-registry reading begins: groups from different registries sit alongside one another in the cluster, and dimensions become visible that no single registry could surface. The instruction is careful about what this stage may and may not do — it works with what the cluster's data actually contains, it does not impose pre-formed dimension categories, and it does not reach cross-cluster conclusions, which belong to Session D.

On completion, every registry and cluster is stamped with the governing instruction version, and the cluster is ready for Session B Analysis Readiness to open for every word in it.

---

## sort_order 119 — prog_instr_session_b_readiness — Session B — Analysis Readiness

The Session B Analysis Readiness instruction governs Stage 1 of Session B. Session B is the programme's central analytical stage — the pass where each word is read in depth against the full accumulated data — and Stage 1 is the readiness pass that prepares the word for that analysis.

The instruction covers the full Stage 1 sequence: the audit of the complete word data export for completeness and internal consistency, the assignment of one of four resolution paths to every anomaly surfaced (Type (a) patch, process re-run directive, Stage 2a verification note, or researcher decision), the accumulation of the Type (a) patch that carries the mechanical corrections, the directives raised for anything needing CC re-run, and the confirmation sequence that produces the Stage 1 Completion Record. A fresh clean extract is re-produced by Claude Code after corrections apply, and the Stage 2 Readiness Declaration is the formal handoff to the Analysis Output stage.

Analysis Readiness is a discipline: it is the stage that ensures Session B's analytical work starts from data that has been audited, validated, and confirmed. It does not itself produce analytical output — no findings, no dimensions, no prose — it only produces the readiness state.

---

## sort_order 120 — prog_instr_session_b_output — Session B — Analysis Output

The Session B Analysis Output instruction governs Stage 2 of Session B, which opens on receipt of the Stage 2 Readiness Declaration from Analysis Readiness. It is the analytical production stage where the word is read in depth and the programme's principal analytical output is written.

Stage 2 has three sub-stages. Stage 2a is the comprehensive reading — every verse in the registry read against the full verse context and the dimensional profile the Dimension Review established, with observations captured to the Session B observations log as they arise. Stage 2b is the Q&A partitioning — findings from the reading are absorbed into the observation question catalogue (becoming answers against existing universal questions, or producing new word-specific questions, or closed as obsolete). Stage 2c is the analytic word output — the six analytic chapters of per-registry Session B prose that summarise what the reading has established.

The stage also produces Session D pointers for every cross-registry observation that arises during the reading — these are the SD pointers Session D will later resolve. Closure is via a closing patch that moves the registry to Analysis Complete and triggers the Session C open and the Session D notification.

Analysis Output is the other half of Session B: where Readiness prepares, Output produces. Together they are the pair.

---

## sort_order 121 — prog_instr_session_c — Session C

The Session C instruction governs the word publication layer. For each word the programme investigates, Session C produces a single reader-facing publication document — a complete, accessible description of the word as a characteristic of the human inner life, written for an intelligent non-specialist reader.

The document is drawn directly from the word's Session A complete data export and from the verse annotations and language annotations Session B produces. It does not summarise the technical analysis; it articulates what the word means, how it works, and where it connects, using the biblical evidence as its foundation.

The document is a living document. It is written in its initial form (v1) from the Session A data as soon as that export is available. It is updated to its annotated form (v2) when Session B's verse and language annotations are incorporated. It is updated again (v3) when Session D establishes cross-word connections and those findings are fed back in. Each version carries a distinct audience posture: v1 from the data, v2 from the analysis, v3 from the synthesis.

Session C is the primary articulation layer — the one place in the programme where the word is described in plain language as a finished account for a reader. The analytical work in Session B and Session D deepens and corrects it; Session C does not replace that work, it renders it for reading.

---

## sort_order 122 — prog_instr_session_d — Session D

The Session D orientation is the instruction for the cross-registry synthesis stage. Session D works in the opposite direction from Sessions A, B, and C: where those stages are word-driven — entering through a Hebrew or Greek term and following the corpus outward — Session D begins with questions about the inner life that the programme as a whole is trying to answer, and asks what the full accumulated body of word-study data reveals in the aggregate.

The stage's material is the accumulated data: every registry's Session B output, every SD pointer raised across the programme, every cluster's dimensional profile, every cross-reference and dimension link the prose store has captured. The instruction covers the synthesis run itself — how Session D groups related SD pointers across registries, how it tests hypotheses against the pooled data, how it produces the synthesis documents that will later feed the final programme-level account.

The instruction is described by its own frontmatter as a governing document rather than a complete instruction — sufficient for conducting Session D runs against accumulated pointer data, but not yet a full specification for the final synthesis pass the programme will make when the registries are complete.

Session D is the interpretive, synthetic, and constructive phase of the programme. It is where the research becomes a framework rather than a catalogue.

---

## End — all thirteen bodies drafted
