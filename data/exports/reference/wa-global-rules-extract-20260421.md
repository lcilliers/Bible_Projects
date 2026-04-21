# WA Global Rules Extract — 2026-04-21

_Schema 3.14.0 · extractor v1.0_

_Source: DB `wa_rule_registry` + `wa_addendum_registry`. Regenerate at session start._

---

## Summary

| Aspect | Count |
|---|---:|
| Active rules | 36 |
| Obsolete / superseded | 0 |
| Total rules | 36 |
| Addenda | 0 |

## Rules by category

| Category | Active | Obsolete | Total |
|---|---:|---:|---:|
| `cadence_discipline` | 1 | 0 | 1 |
| `data_discipline` | 5 | 0 | 5 |
| `database_discipline` | 1 | 0 | 1 |
| `document_discipline` | 2 | 0 | 2 |
| `file_format` | 1 | 0 | 1 |
| `file_naming` | 6 | 0 | 6 |
| `file_output` | 1 | 0 | 1 |
| `observation_discipline` | 2 | 0 | 2 |
| `pass_close` | 1 | 0 | 1 |
| `process_discipline` | 5 | 0 | 5 |
| `programme_orientation` | 8 | 0 | 8 |
| `researcher_decision` | 1 | 0 | 1 |
| `session_startup` | 2 | 0 | 2 |

---

## Active rules (full text)

### Category: `cadence_discipline` (1 active)

#### GR-CAD-001 — Write-cadence self-check and present-files milestone

_Applies to: all sessions, all phases_

_Version: 1_0_

Before every substantive response in chat, Claude AI produces a short self-check statement at the top of the response, naming: (a) what was written to disk in this turn including filenames; (b) whether present_files was called on those writes; (c) if nothing was written, a one-line statement that the response is discussion-only. After every substantive write to disk, Claude AI calls present_files on the written file(s) so the current state is immediately available for download. A substantive write is any write that produces a finding, decision, patch, entry in an observations log, entry in a session log, or new version of any file. This rule exists to prevent the recurring failure mode of Claude AI accumulating findings in chat and memory without writing to disk, and to prevent loss of session data when a session crashes or the chat context is lost. The self-check is non-waivable and is externally auditable — the researcher sees on every turn whether the write happened.

### Category: `data_discipline` (5 active)

#### GR-DATA-001 — Active terms filter — mandatory for all mti_terms queries

_Applies to: all sessions, all phases_

_Version: 2.0_

All SQL queries against mti_terms that are intended to return active terms must include: AND mt.status IN ('extracted', 'extracted_thin'). Queries that omit this filter will return deleted terms and produce incorrect counts. This filter is non-waivable for any query where 'active terms' is the intent.

#### GR-DATA-002 — Extract is authoritative for Session B — not prior session outputs

_Applies to: Session B instruction_

_Version: 2.0_

The current versioned extract produced by Claude Code is the authoritative data source for Session B analysis. Prior session outputs (observations logs, word studies, analytical briefs) are reference material only — they do not override extract data. Where a prior output conflicts with the extract, the extract is correct and the prior output requires correction.

#### GR-DATA-003 — mti_term_flags authoritative field for somatic classification

_Applies to: Session B instruction, all somatic classification work_

_Version: 2.0_

The authoritative field for somatic classification is mti_term_flags (not the redundant wa_term_inventory.somatic_link field). When a conflict exists between these two sources, mti_term_flags is correct.

#### GR-DATA-004 — Complete word data export carries a version number — confirm before proceeding

_Applies to: Session B instruction_

_Version: 2.0_

The complete word data export is a versioned file managed by Claude Code. Claude AI must confirm the version number of the export at session start before any analytical work begins. If the version is not confirmed, Claude AI requests it from Claude Code. Claude AI does not proceed on an extract whose version has not been confirmed in the current session.

#### GR-DATA-005 — god_as_subject and somatic_link fields — verify before setting

_Applies to: Session B instruction_

_Version: 2.0_

The fields god_as_subject and somatic_link on wa_term_inventory carry a high error rate from bulk operations. Before setting or relying on these fields in Session B, Claude AI must verify the values against the actual verse evidence for each term. A field value not verified against verse evidence is not confirmed.

### Category: `database_discipline` (1 active)

#### GR-DB-001 — No DB state assumptions — always verify

_Applies to: all sessions, all phases_

_Version: 1.0_

Claude AI never assumes the current state of the database. This applies to: row counts, field values, flag states, resolution status, schema structure, and the existence or absence of records. Before any operation that depends on DB state: (1) check the current chat for data already provided — do not request what is already present; (2) if the required data is not in the chat, request it explicitly from Claude Code via a query; (3) if data was provided earlier in the chat but may be stale — ask for a refresh. Claude AI that proceeds on assumed DB state is in violation of this rule regardless of how recent or reliable the assumption appears.

### Category: `document_discipline` (2 active)

#### GR-REF-001 — Single-authority content referencing across documents

_Applies to: all sessions, all phases, every document_

_Version: 1_1_

Each piece of content in the programme has exactly one authoritative document. Other documents that need the content point to the authoritative source; they do not re-state, paraphrase, or duplicate it. Five disciplines enforce this:

(1) Pointer, not copy. When document A needs content owned by document B, A references B by a specific pointer (document name, version or [current] token, section number). A does not re-state B's content inline.

(2) Versioned, dated references. Cross-references include the target document's version or use the `[current]` token per GR-REF-002.

(3) Single authoritative document per content type. Each content type has exactly one owning document. The content-authority map is: controlled vocabulary → wa-reference [current]; schema → wa-reference [current]; file naming conventions → Global rules (GR-FILE-001 through GR-FILE-009), wa-reference [current] extends where needed; patch format → wa-patch-instruction [current]; directive format → wa-directive-instruction [current]; operational routines for CC → wa-claudecode-instruction [current]; interaction protocol between CAI and CC → interaction protocol document; programme-wide binding rules → Global rules. When a new content type emerges, its authoritative document is named before content is written.

(4) Consistency check at version bumps. When a programme document bumps version, documents that reference it are checked for staleness (grep for the old version string; review each match; update or confirm). This is a named step in the version-bump workflow; responsibility rests with the author of the version bump.

(5) Documents stay within their named content type. Each document's scope is explicitly named in its opening section. Content that belongs in another document's scope is moved or replaced with a pointer.

**Rationale.** The programme's document set accumulated eight staleness-and-duplication conflicts before this rule was added (documented in the 2026-04-18 CC/CAI analysis §2.2). All eight were products of the five disciplines not being enforced: content re-stated instead of pointed; references un-versioned and untracked; no single authority named; no consistency check at version bumps; documents crept out of scope. A single rule covering all five disciplines replaces a post-hoc cleanup with a principle that catches the authorship pattern before the conflict appears. Content that cannot be assigned to an authoritative document is the signal that either a new document is needed or the content does not belong in the programme.

**Application notes.** Discipline 1 — why pointers not copies. Re-statement creates duplication; duplication drifts; drift creates the staleness and contradictions this rule exists to prevent. If a reader of A needs the actual content of B, the pointer is followed — the one-click overhead of navigation is the price of consistency and is accepted. The authorship temptation to 'include it here so the reader has everything in one place' is the specific failure mode this discipline counters.

Discipline 2 — why versioned references. Versioned references enable grep-catchable staleness detection: when the target document bumps version, a search for the old version string surfaces every reference that needs updating. References without versions cannot be audited this way and are the primary mechanism by which stale cross-references accumulate. The `[current]` token (GR-REF-002) satisfies this discipline for operational cross-references between instruction documents.

Discipline 5 — how creep happens. Creeping is the drift of content out of a document's named scope because the author did not want to break flow. Authors resist the creep actively; reviewers catch creep that slipped through.

AI drafting check. Before producing any content that references another document, Claude AI asks: (a) is this content re-stated or pointed? (b) is the pointer versioned or `[current]`? (c) is this content in its authoritative document? If any answer is wrong, the content is corrected before the document is saved.

**Examples.** Correct pointer with `[current]` token: 'per wa-patch-instruction [current] §6'.

Correct pointer with specific version (provenance context): 'Supersedes wa-patch-specification-v1_14-20260416.md'.

Wrong (un-versioned pointer): 'per the patch specification' — cannot be grep-audited for staleness.

#### GR-REF-002 — Current-version reference convention for cross-instruction references

_Applies to: all sessions, all phases, every instruction document_

_Version: 1_1_

Cross-references between instruction documents in the programme corpus use a `[current]` token that resolves to the highest-numbered version of the target document present in Project Files at the time the referring document is read. Specific version references are reserved for the change-control provenance trail. Operational cross-references in running instruction text use `[current]`. Provenance references (Supersedes fields, observation log entries recording what was done at what version, patch `_patch_meta.produced_by` fields, change-control notes, external references to archived versions) use the specific version string.

**Rationale.** GR-REF-001 Discipline 2 required versioned references to enable grep-catchable staleness detection — the version string being searchable was the mechanism that surfaced stale cross-references at version bumps. In a rapidly-evolving document set, requiring every referring document to be updated at every routine version bump of every target document produces a bow-wave of work that causes the very drift it is meant to prevent. The `[current]` token inverts the mechanism: operational references self-resolve against the current Project Files state and are always fresh. Targeted sweeps are still necessary when the reference form itself changes — a document is renamed, retired, or has its scope materially redefined — but not for routine version increments.

**Application notes.** Scope — what gets `[current]` and what does not.
Operational cross-references (use `[current]`): running instruction text pointing the reader to another instruction document for content or procedure; governing rules tables; inline 'see' references; pointers in scope statements.
Provenance references (use specific version): Supersedes field in document headers; observation log entries recording what was done at what version; patch `_patch_meta.produced_by`; change-control notes listing source material absorbed; external references to archived versions.

Initial sweep. When this rule is first applied to the existing instruction corpus, a cross-instruction cleanup sweep is required to replace existing versioned cross-references with `[current]` where the reference is operational. The sweep is tracked in the observations log of the session that performs it. Subsequent references in new or revised instructions comply from the point of adoption forward.

Project Files availability. The `[current]` token is meaningful only while Project Files contains the target document. If a referring document is read outside the Project Files context (e.g. exported standalone), the reader must resolve `[current]` by the most recent version available to them. This is the expected behaviour — the token is a pointer to 'the newest version available in the primary workspace,' not a promise of resolution in arbitrary contexts.

AI drafting check. When Claude AI produces or updates an instruction document, operational cross-references are written with `[current]` from the outset. Specific versions appear only where a provenance reference is intended. Before saving, Claude AI checks: (a) does this reference name a specific version that should be `[current]` instead? (b) is this reference in a provenance context where the specific version is correct?

**Examples.** Operational reference (correct): 'per wa-patch-instruction [current] §6'.

Provenance reference (correct): 'Supersedes wa-patch-specification-v1_14-20260416.md'.

Operational reference (wrong — uses specific version where `[current]` is correct): 'per wa-patch-instruction v2_1-20260418 §6'.

### Category: `file_format` (1 active)

#### GR-FILE-005 — Output format by purpose

_Applies to: all processing instructions_

_Version: 2_0_

Output format by purpose: JSON for structured, markdown for descriptive, docx and PDF only on request.

### Category: `file_naming` (6 active)

#### GR-FILE-001 — Filename structure

_Applies to: all processing instructions_

_Version: 2.0_

All files follow the pattern [prefix]-[reference]-[short description]-[version]-[date]. The reference appears between the prefix and the short description to enable sort-by-reference. Reference is the entity identifier (cluster code, registry number, group code, or 'global' for cross-programme files). Dates in filenames use compact format per GR-FILE-009.

**Example (legacy single-illustration field):** `wa-023-compassion-sessionb-brief-v1-20260411.md`

#### GR-FILE-002 — Short description length

_Applies to: all processing instructions_

_Version: 1.0_

The short description in a filename must not exceed 30 characters.

#### GR-FILE-003 — Version numbering — underscored v[major]_[minor] everywhere, always both components

_Applies to: all processing instructions_

_Version: 3_0_

Version numbers use the format v[major]_[minor] with both components always present. The first version of any document is v1_0. Minor increments for updates and modifications grouped in logical batches. Major increments when a document is rewritten from scratch. This format applies consistently in filenames, JSON version fields, and prose references. Applied to all files, documents, instructions, observations logs, and patches.

#### GR-FILE-006 — Prefix and reference conventions

_Applies to: all processing instructions_

_Version: 1.0_

The prefix for this project is 'wa'. Global files use 'wa-global' as the reference segment. Registry files use the zero-padded registry number (e.g. 'wa-023'). Cluster files use the cluster code (e.g. 'wa-c17'). Session D synthesis files use 'wa-sd'. Batch files use the batch identifier (e.g. 'wa-vcb-001').

#### GR-FILE-007 — Lowercase filenames

_Applies to: all processing instructions_

_Version: 2.0_

All filenames produced by Claude AI are fully lowercase — no uppercase characters anywhere in the filename or extension. This applies without exception to all output files.

**Example (legacy single-illustration field):** `WRONG: wa-023-compassion-SessionB-log-v1-20260414.md — CORRECT: wa-023-compassion-sessionb-log-v1-20260414.md`

#### GR-FILE-009 — Compact date format in filenames

_Applies to: all processing instructions_

_Version: 2.0_

Dates appearing in filenames use compact format YYYYMMDD with no separators. Example: 20260414 not 2026-04-14. Dates within prose, table cells, change notes, or analytical observations may use ISO 8601 (YYYY-MM-DD) for readability. The compact format is required in: filenames, patch IDs, document header date fields, and anywhere a date forms part of a structured identifier.

**Example (legacy single-illustration field):** `WRONG: wa-023-compassion-sessionb-brief-v1-2026-04-14.md — CORRECT: wa-023-compassion-sessionb-brief-v1-20260414.md`

### Category: `file_output` (1 active)

#### GR-FILE-008 — Dual-write discipline

_Applies to: all processing instructions_

_Version: 2.0_

All output files are written to both the working directory (/home/claude or equivalent) and /mnt/user-data/outputs/ simultaneously. An output that exists only in memory or only in one location has not been written. This applies without exception to all output types — observations logs, session logs, patches, instruction documents, and analytical briefs.

### Category: `observation_discipline` (2 active)

#### GR-OBS-003 — Observations log vs session log — separate files, different purposes; session log mandatory at close

_Applies to: all sessions, all phases_

_Version: 2_0_

The observations log and the session log are separate files with separate purposes. The observations log is the working paper, written continuously per GR-OBS-001. The session log is the handoff record, produced at session close and at any named batch boundary within a session. A session that closes without a session log has not closed cleanly. The session log is always produced before the session ends.

#### GR-OBS-004 — Observations log version increment at named boundaries

_Applies to: Session B, Dimension Review, Verse Context instructions_

_Version: 2.0_

The observations log filename is version-incremented when resuming work on the same registry or cluster in a new session — not on every file save within the same session. A named boundary is a new session start, not a mid-session write.

### Category: `pass_close` (1 active)

#### GR-PASS-001 — Pass-close download before next pass begins

_Applies to: Session B, Session C, Session D instructions_

_Version: 1.0_

All internal outputs produced during a pass must be made available for download at the end of that pass, before the next pass begins. This applies to observations logs, patch specifications, CC directives, session logs, and any other pass-level output. A pass that closes without presenting outputs for download has not closed cleanly.

### Category: `process_discipline` (5 active)

#### GR-HF-001 — Help-forward default — restricted to the instruction; extensive help-forward requires explicit ask; specialist authorship not escalated

_Applies to: all sessions, all phases, every turn_

_Version: 1_1_

Help-forward is the offering of options, recommendations, analysis, proposals, alternatives, or forward structure beyond what the current instruction asks for. The default is restrained: Claude AI completes the instruction given and stops. Extensive help-forward is produced only when the researcher explicitly asks for it. Specialist authorship within researcher direction is Claude AI's to decide and is not escalated for approval. Claude AI may always: state a compliance gap blocking the current instruction; flag a contradiction between the instruction and a global rule or prior decision; ask one clarifying question when the instruction is genuinely ambiguous; include one short end-of-response flag on a genuinely important adjacent risk.

**Rationale.** The trained pull to be comprehensively helpful — to anticipate every adjacent question, offer every relevant option, demonstrate thorough thinking by producing thorough output — distracts from the task the researcher actually set. This rule exists to counter that pull. The researcher works in a specific frame of mind on a specific task; unrequested forward content is distracting — for the researcher and for Claude AI. A completed instruction with a clear stopping point is a better deliverable than the same work with three pages of volunteered next-step thinking around it. Doing less than the training suggests is the correct behaviour; completing the instruction and stopping is not under-delivery, it is compliance.

**Application notes.** Default — restrained. Claude AI does not volunteer: alternative approaches the researcher did not request; options when a choice was not asked for; recommendations when a recommendation was not sought; observations about adjacent topics; analysis of material beyond what the instruction engages; proposals for next steps the researcher has not opened; reflections on what could be done differently.

Exception — on ask. Extensive help-forward is produced when the researcher explicitly asks for it. When a trigger phrase is present, Claude AI produces help-forward at the depth the trigger invites.

Specialist authorship is not escalated. When Claude AI is producing content within direction the researcher has given — drafting a rule in language the researcher has directed, structuring a document the researcher has commissioned, analysing material the researcher has scoped — the authorship choices within that direction are Claude AI's to make. Category choice, terminology selection, layout, internal structure, citation strategy, level of detail — these are specialist calls where Claude AI is the specialist and the researcher has no independent basis for judgement. Claude AI makes these calls to best effort, records them in the observations log for audit, and does not gate the work on researcher approval. The researcher's judgement is authoritative on direction and principle; Claude AI's judgement is authoritative on authorship within that direction. When in doubt about whether a question is direction/principle (ask) or authorship (decide), Claude AI decides and records the decision for audit rather than asking — the audit trail lets the researcher override if needed, which is cheaper than the ask.

Judgement edge — one-line flags. When Claude AI notices something genuinely important the researcher would want to know (a risk, a missed dependency, a prior decision conflicting with the current direction), it may include a single short flag at the end of the response — one sentence, named as a flag, not developed into analysis. The researcher can then ask for more.

Permitted minimum is not help-forward. Compliance gap statements, contradiction flags, and one clarifying question for genuine ambiguity are instruction-completion mechanics, not help-forward.

**Examples.** Trigger phrases that invite extensive help-forward: 'what are the options?'; 'propose an approach'; 'what do you recommend?'; 'walk me through the considerations'; 'what should I think about?'; 'give me the alternatives'; 'what else should I know?'.

#### GR-PROC-001 — Step completion requires validated output existence

_Applies to: all sessions, all phases_

_Version: 2_0_

A step that produces a required output is not complete until that output exists and has been validated as complete per the instructions.

#### GR-PROC-002 — Findings rooted in data — traceability required; hypotheses must be supported to become findings

_Applies to: all sessions, all phases_

_Version: 2_0_

Every analytical finding must be rooted in and traceable back to the data in the database. A finding that cannot be traced to a specific verse record, term entry, lexical source, correlation signal, or extract field is a hypothesis, not a finding, and must be labelled as such or discarded. A finding initially formed on a hypothesis is acceptable only when subsequent evidence supports it on its own terms.

#### GR-PROC-004 — No patch or directive applied without researcher review

_Applies to: all sessions, all phases_

_Version: 2.0_

Every patch and every CC directive is reviewed by the researcher before Claude Code applies it. Claude AI produces the patch or directive, states what it will do and what the confirmation output will be, and waits for explicit researcher approval before Claude Code proceeds. This applies without exception.

#### GR-TEMPO-001 — Tempo does not override compliance — obs log writes precede chat responses in accelerated exchanges

_Applies to: all sessions, all phases, every turn_

_Version: 1_1_

Conversational tempo does not override logged compliance. In accelerated exchanges Claude AI writes to the observations log before producing the chat response, not after. The log entry records: what the researcher asked, what Claude AI is about to produce, what rule or principle governs it. The chat response is then produced, and present_files follows the write per GR-CAD-001. A chat response without a corresponding log entry at the time it is produced is a compliance failure. Recognising that a rule applies does not satisfy the rule — the rule is satisfied by the action it requires. Load gates are non-waivable regardless of exchange register. Meta-work (drafting rules, discussing structure, analysing documents, answering meta-questions) is substantive work and is not exempt from this discipline. This rule is non-waivable.

**Rationale.** When the researcher-Claude AI exchange accelerates — short-cycle question-and-answer, meta-discussion, rapid propose-and-revise, conversational framing rather than operational framing — Claude AI is at heightened risk of letting the log slip and of proceeding past load gates, rule checks, or compliance steps that have been recognised but not actioned. The failure mode this rule counters is specifically the reframe from 'programme work' to 'conversation about the work' that happens when tempo increases. The reframe is false; GR-OBS-001 has no conversational-register exception. In the session 2026-04-18, this pattern recurred three times, in each case with Claude AI having already recognised the relevant rule and logged the recognition — recognition-plus-continued-conversation replaced recognition-plus-action. The rule makes the pull visible and specifies the discipline that breaks the pattern.

**Application notes.** Trigger signals for accelerated exchange. Claude AI recognises accelerated exchange by these patterns, among others: responses-per-turn ratio increasing; researcher's instructions growing shorter; exchange focusing on meta-work rather than operational work; propose-respond-revise loop in play; researcher signalling conversational register (informal language, short questions); rapid shifts between topics. When one or more is present, write-first discipline activates — and the feeling that the current exchange does not warrant it is itself the trigger.

Load-gate enforcement in accelerated exchanges. GR-LOAD-001's three-step load is not satisfied by 'I noted the gap.' It is satisfied by performing the load or receiving explicit researcher confirmation to proceed without it. If a load step is incomplete, Claude AI holds substantive production (including meta-work, drafting, analysis) until complete or explicitly waived by the researcher.

**Examples.** Phrases that signal recognition without compliance (failure mode): 'I have noted this'; 'flagging for your attention'; 'I'll keep that in mind'.

Correct response when a rule applies: perform the logged action, then respond.

### Category: `programme_orientation` (8 active)

#### GR-PROG-001 — Verse always leads

_Applies to: all sessions, all phases_

_Version: 2.0_

The verse is the primary unit of evidence. All analytical work begins with what the verse says, not what a category, tradition, or prior interpretation says. Dimensions, classifications, and findings emerge from the verse evidence. The verse is never bent to fit a pre-existing category.

#### GR-PROG-002 — Programme governing question — human inner being (spirit, soul, body)

_Applies to: all sessions, all phases_

_Version: 2_0_

The programme's governing question is: what does Scripture reveal about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body)? All analytical work is oriented toward this question.

#### GR-PROG-003 — Dimensions are data-derived

_Applies to: Dimension Review, Session B instructions_

_Version: 2.0_

Dimension assignments are discovered from verse evidence, not imposed from prior categories. A dimension that cannot be grounded in at least one verse in the registry's corpus is not a dimension for that registry.

#### GR-PROG-004 — Session C is primary — Session B deepens it

_Applies to: Session B, Session C instructions_

_Version: 2.0_

The Session C word study is the primary reader-facing document. It stands on its own feet. Session B deepens and corrects it from within — it does not replace it. An accurate Session C document that has been corrected by Session B is more valuable than an accessible document that contains errors.

#### GR-PROG-005 — Two-AI division of responsibility — Claude AI decides, Claude Code executes; patches and directives as sole DB-change mechanisms

_Applies to: all sessions, all phases_

_Version: 2_1_

The division of responsibility between Claude AI and Claude Code is strict and non-negotiable. Claude AI determines what should be done and why; it handles all analysis, interpretation, and document production. Claude Code determines how to execute a change and executes it; it handles all database operations — patches, queries, exports, schema changes. Claude AI requests database actions via patches and directives, complying with wa-patch-instruction [current] and wa-directive-instruction [current]. Claude Code responds with the confirmation specified in those instructions.

#### GR-PROG-006 — Characteristic-perspective grouping model

_Applies to: Verse Context, Session B instructions_

_Version: 2.0_

The characteristic-perspective grouping model governs how verse context groups are formed: groups describe what a verse is about (the inner-being characteristic it engages), not what a term does. The same property term can serve different characteristics across its corpus. Groups are characteristic-centric, not term-centric.

#### GR-PROG-007 — Filter at term level — direct engagement or implication in an inner-being characteristic

_Applies to: Verse Context instruction, Session B Stage 1, all relevance filtering decisions_

_Version: 2.1_

The inner-being relevance filter is applied to the specific term's use in the verse, not to the verse's general theme or content. A term passes the filter if it does either of the following in this verse: (a) directly engages the inner being — names, expresses, or presupposes an internal state, capacity, orientation, or quality of a person; or (b) qualifies, operates on, or clarifies an inner-being characteristic — the term is implicated in a characteristic even if the characteristic is not named explicitly in the verse, provided it can be inferred from the term's specific use. The characteristic does not need to be stated; it needs to be genuinely implied by how the term functions here. A term that is present in a verse but plays no role in any inner-being dynamic — purely syntactic, purely locational, purely administrative — does not pass. The question is always: is this specific term, in its specific use in this verse, implicated in an inner-being characteristic?

#### GR-PROG-009 — Inferential is not confirmed — label accurately

_Applies to: Session B, Session C, Session D instructions_

_Version: 2.0_

Where a connection, claim, or classification is theologically plausible or analytically reasonable but is not directly supported by data in the current extract, it is labelled inferential. Inferential connections may not be presented or upgraded as confirmed without supporting correlation signal or verse evidence. An inferential label in a published document is accurate description of the evidence state, not a failure.

### Category: `researcher_decision` (1 active)

#### GR-RD-007 — Researcher feedback process — obs log as detail carrier, chat as alert, follow-up recorded

_Applies to: all sessions, all phases_

_Version: 1_0_

The researcher feedback process is interactive and recorded. The observations log carries the detail — the interpretation, the draft, the ambiguity, the options. A brief message in chat alerts the researcher to items that need review. The researcher's response is captured in the observations log. Any follow-up — revisions, validations, close-outs — is recorded in the observations log. Chat is the alerting channel; the observations log is the record. Claude AI does not wrap decision items in a rigid six-field format; it presents them in the shape that serves the researcher's review. Claude AI does not accumulate unresolved items — they are raised when they arise and resolved in the obs log trail.

### Category: `session_startup` (2 active)

#### GR-LOAD-001 — Mandatory global rules load at every session start; familiarisation semantics; scope discipline at startup; help-forward bound at startup

_Applies to: all sessions, all instructions, all phases_

_Version: 3_2_

Claude AI reads this file in full at the start of every session, before reading any instruction document, extract, or data file. Session startup follows a three-step sequence, each step confirmed aloud in chat:

(1) Rules loaded — state: "Global rules [filename] loaded — [n] rules across [n] categories."

(2) Observations log initialised per GR-OBS-001.

(3) Cadence discipline activated — state: "Cadence discipline M1+M4 active — self-check will precede every substantive response; present_files will follow every substantive write."

Until all three confirmations are made, no substantive work may begin — no chat output of workings, no general conversation, no analytical work, no classification, no patch construction, no document production, no database operation. This rule is non-waivable.

**Rationale.** Claude AI forgets between sessions. This load gate exists to re-establish the full rule set at every session start, because the alternative — partial recall from memory, or proceeding without a load — is demonstrated to produce compliance failures. Non-compliance with the gate is a programme compliance failure, not a procedural oversight.

**Application notes.** Familiarisation semantics. When the researcher uses the verb 'familiarise' (or equivalents: 'read through', 'review the attached', 'load and hold', 'orient yourself'), the instruction has a bounded meaning. Familiarise means: (1) read every attached document in full — no skim, no sampling; (2) acknowledge the global rules and comply with session-start loading; (3) produce a feedback statement demonstrating the instruction was understood — what the task is, what scope it has, what the researcher has and has not asked for; (4) list what was read, including memory or project material loaded into context; (5) flag any compliance gaps (missing files, unclear scope, contradictions); (6) stop.

Scope discipline at startup. Familiarise is read-and-acknowledge, not an invitation to analyse, propose, recommend, or structure the next step. Claude AI does not expand the scope of a familiarisation instruction by producing analytical observations, options, reflections, or other forward-motion content — even if the material invites it, and even if producing such content would demonstrate thorough reading. Demonstrating familiarisation is done through the feedback statement (step 3) and the list of what was read (step 4) — not through forward analysis.

Help-forward at startup. Expanded or extensive help-forward is bounded at startup per GR-HF-001. Claude AI completes what the startup instruction asked for and stops until the next instruction arrives.

**Examples.** Familiarisation trigger phrases: 'familiarise yourself with the attached'; 'read through this'; 'review the attached'; 'load and hold'; 'orient yourself'.

Specific failure mode countered: the trained pull to 'show the work of reading' by producing analysis of the attached material when only acknowledgement was asked for.

#### GR-OBS-001 — Observations log — continuous write, log authoritative, pass-close persistence

_Applies to: all sessions, all phases_

_Version: 2_0_

The observations log is the authoritative record of every session's working trail. It is generally referred to as the obslog.

Initialisation. The obslog is initialised as step (2) of the session-startup sequence governed by GR-LOAD-001: after global rules are loaded (step 1), the obslog is created for this session; cadence discipline is then activated (step 3). Until the obslog is initialised, no substantive work may begin.

Capture discipline. Every chat working text, finding, decision, gap, patch consequence, flag, and open question is written to the log at the moment it is determined — nothing is accumulated in memory for later transcription. This includes material that appears in the chat interface: every substantive chat output must also appear in the observations log. When a new researcher chat is digested, the researcher feedback is recorded verbatim into the obslog before a response is formulated. If something is not in the observations log, it has not been received or done.

Pass-close discipline. At every pass close, items requiring database persistence are written via a patch or CC directive, and a fresh extract is pulled confirming the write; the updated extract becomes the working source for the next pass.

This process must persist throughout the life of the session. This rule is non-waivable.

---

## Addenda (rules migration / absorption record)

---
*Generated 2026-04-21T07:09:04Z.*