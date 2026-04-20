# WA Global Rules Extract — 2026-04-20

_Schema 3.13.0 · extractor v1.0_

_Source: DB `wa_rule_registry` + `wa_addendum_registry`. Regenerate at session start._

---

## Summary

| Aspect | Count |
|---|---:|
| Active rules | 36 |
| Obsolete / superseded | 0 |
| Total rules | 36 |
| Addenda | 22 |

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
| `load_requirement` | 1 | 0 | 1 |
| `observation_discipline` | 3 | 0 | 3 |
| `pass_close` | 1 | 0 | 1 |
| `process_discipline` | 5 | 0 | 5 |
| `programme_orientation` | 8 | 0 | 8 |
| `researcher_decision` | 1 | 0 | 1 |

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

_Version: 1_0_

Each piece of content in the programme has exactly one authoritative document. Other documents that need the content point to the authoritative source — they do not re-state, paraphrase, or duplicate the content. This rule specifies the five disciplines that keep the programme's document set internally consistent as it grows.

Discipline 1 — Pointer, not copy. When document A needs content owned by document B, document A references B by a specific pointer (document name, version, section number). It does not re-state B's content inline. Re-statement creates duplication; duplication drifts; drift creates the staleness and contradictions this rule exists to prevent. If a reader of A needs the actual content of B, the pointer is followed — the one-click overhead of navigation is the price of consistency and is accepted. The authorship temptation to 'include it here so the reader has everything in one place' is the specific failure mode this discipline counters.

Discipline 2 — Versioned, dated references. Cross-references include the target document's current version (e.g. 'per wa-patch-specification v1_14 §3.10', not 'per the patch specification'). Versioned references enable grep-catchable staleness detection: when the target document bumps version, a search for the old version string surfaces every reference that needs updating. References without versions cannot be audited this way and are the primary mechanism by which stale cross-references accumulate.

Discipline 3 — Single authoritative document per content type. Each piece of content has exactly one document that is authoritative for it. Multiple documents may reference the content; only one document owns it. The content-authority map is: Controlled vocabulary → WA-Reference; Schema → WA-Reference; File naming conventions → Global rules (GR-FILE-001 through GR-FILE-009), WA-Reference extends where needed; Patch format → Patch specification; Directive format → Directive specification (when it exists); Operational routines for CC → CC instructions; Interaction protocol between CAI and CC → Interaction protocol document; Programme-wide binding rules → Global rules; Open issues and flags → Global flags. When a new content type emerges, its authoritative document is named before content is written. Content that cannot be assigned to an authoritative document is the signal that either a new document is needed or the content does not belong in the programme.

Discipline 4 — Consistency check at version bumps. When any programme document bumps version, the documents that reference it are checked for staleness. The check is short — grep for the old version string across the document set, review each match, update or confirm each reference. This is a named step in the version-bump workflow, not an optional follow-up. Responsibility for the check rests with the author of the version bump. Absence of this step is how staleness accumulates; presence of this step is how it is prevented.

Discipline 5 — Documents stay within their named content type. Each document's scope is explicitly named in its opening section. Content that would naturally sit in a different document's scope is either moved to that document or replaced with a pointer. Creeping — where content drifts out of the named scope because the author did not want to break flow — is the primary mechanism that produces content mixing and document bloat. Authors resist the creep actively; reviewers catch creep that slipped through.

Failure mode this rule counters. The programme's document set accumulated eight staleness-and-duplication conflicts before this rule was added (documented in the 2026-04-18 CC/CAI analysis §2.2). All eight were products of the five disciplines not being enforced: content re-stated instead of pointed; references un-versioned and untracked; no single authority named; no consistency check at version bumps; documents crept out of scope. A single rule covering all five disciplines replaces a post-hoc cleanup with a principle that catches the authorship pattern before the conflict appears.

Application note — AI drafting considerations. Claude AI is the author of most documents in this programme. The authorship pattern that produces drift — re-stating content 'for the reader's convenience,' omitting version numbers in references, producing content without naming its authoritative home — is a natural default of AI drafting. This rule is specifically calibrated against that default. Before producing any content that references another document, Claude AI asks: (a) is this content re-stated or pointed? (b) is the pointer versioned? (c) is this content in its authoritative document? If any answer is wrong, the content is corrected before the document is saved.

#### GR-REF-002 — Current-version reference convention for cross-instruction references

_Applies to: all sessions, all phases, every instruction document_

_Version: 1_0_

Cross-references in the instruction corpus between instruction documents use a `[current]` token that resolves to the highest-numbered version of the target document present in Project Files at the time the referring document is read. Specific version references are reserved for the change-control provenance trail — Supersedes fields, observation log entries, patch `_patch_meta.produced_by` fields, and the historical audit record. Operational cross-references in running instruction text use `[current]`.

Example of operational reference (in running text): 'per wa-patch-instruction [current] §6'.
Example of provenance reference (in change-control note): 'Supersedes wa-patch-specification-v1_14-20260416.md.'

This rule complements GR-REF-001 Discipline 2 (versioned references) rather than replacing it. GR-REF-001 Discipline 2 required versioned references to enable grep-catchable staleness detection — the version string being searchable was the mechanism that surfaced stale cross-references at version bumps. GR-REF-002 accepts that in a rapidly-evolving document set, requiring every referring document to be updated at every routine version bump of every target document is a bow-wave of work that produces the very drift it is meant to prevent. The `[current]` token inverts the consistency mechanism: operational references self-resolve against the current Project Files state and are always fresh. Targeted sweeps remain necessary when the reference form itself changes — a document is renamed, retired, or has its scope materially redefined — but not for routine version increments.

Scope — what gets `[current]` references and what does not:
Operational cross-references (use `[current]`): running instruction text pointing the reader to another instruction document for content or procedure; governing rules tables; inline 'see' references; pointers in scope statements.
Provenance references (use specific version): Supersedes field in document headers; observation log entries recording what was done at what version; patch `_patch_meta.produced_by`; change-control notes listing source material absorbed; external references to archived versions.

Sweep mechanism. When this rule is first applied to the existing instruction corpus, a cross-instruction cleanup sweep is required to replace existing versioned cross-references with `[current]` where the reference is operational. The sweep is tracked in the flags file. Subsequent references in new or revised instructions are produced in compliance with this rule from the point of adoption forward.

Interaction with Project Files availability. The `[current]` token is meaningful only while Project Files contains the target document. If a referring document is read outside the Project Files context (e.g. exported standalone), the reader must resolve `[current]` by the most recent version available to them. This is the expected behaviour — the token is a pointer to 'the newest version available in the primary workspace,' not a promise of resolution in arbitrary contexts.

Application note — AI drafting considerations. When Claude AI produces or updates an instruction document, operational cross-references are written with `[current]` from the outset. Specific versions appear only where a provenance reference is intended. Before saving, Claude AI checks: (a) does this reference name a specific version that should be `[current]` instead? (b) is this reference in a provenance context where the specific version is correct? Compliance is verified by a reviewer or by Claude AI's self-check before the document is saved.

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

**Example:** `wa-023-compassion-sessionb-brief-v1-20260411.md`

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

**Example:** `WRONG: wa-023-compassion-SessionB-log-v1-20260414.md — CORRECT: wa-023-compassion-sessionb-log-v1-20260414.md`

#### GR-FILE-009 — Compact date format in filenames

_Applies to: all processing instructions_

_Version: 2.0_

Dates appearing in filenames use compact format YYYYMMDD with no separators. Example: 20260414 not 2026-04-14. Dates within prose, table cells, change notes, or analytical observations may use ISO 8601 (YYYY-MM-DD) for readability. The compact format is required in: filenames, patch IDs, document header date fields, and anywhere a date forms part of a structured identifier.

**Example:** `WRONG: wa-023-compassion-sessionb-brief-v1-2026-04-14.md — CORRECT: wa-023-compassion-sessionb-brief-v1-20260414.md`

### Category: `file_output` (1 active)

#### GR-FILE-008 — Dual-write discipline

_Applies to: all processing instructions_

_Version: 2.0_

All output files are written to both the working directory (/home/claude or equivalent) and /mnt/user-data/outputs/ simultaneously. An output that exists only in memory or only in one location has not been written. This applies without exception to all output types — observations logs, session logs, patches, instruction documents, and analytical briefs.

### Category: `load_requirement` (1 active)

#### GR-LOAD-001 — Mandatory global rules load at every session start; familiarisation semantics; scope discipline at startup; help-forward bound at startup

_Applies to: all sessions, all instructions, all phases_

_Version: 3_0_

Claude AI must read this file in full at the start of every session before reading any instruction document, extract, or data file. The load is confirmed by stating aloud: 'Global rules [filename] loaded — [n] rules across [n] categories.' Immediately after the load confirmation, Claude AI loads the flags file (wa-global-flags-v[version]-[date].md) and confirms: 'Global flags [filename] loaded — [n] open, [n] resolved, [n] obsolete, [n] standing.' Claude AI then opens the observations log for the session per GR-OBS-001 and states: 'Cadence discipline M1+M4 active — self-check will precede every substantive response; present_files will follow every substantive write.' No analytical work, classification, patch construction, document production, or database operation may begin until all three confirmations have been made. This is non-waivable.

Familiarisation semantics. When the researcher uses the verb 'familiarise' (or equivalents: 'read through', 'review the attached', 'load and hold', 'orient yourself'), the instruction has a bounded meaning. Familiarise means: (1) read every attached document in full — no skim, no sampling; (2) acknowledge the global rules and comply with the relevant GR instructions for session start; (3) produce a feedback statement that demonstrates the instruction was understood — what the task is, what scope it has, what the researcher has asked for and has not asked for; (4) list what was read, including any memory or project-related material loaded into context; (5) flag any compliance gaps (missing files, unclear scope, contradictions); (6) stop.

Scope discipline at startup. Familiarise is a read-and-acknowledge instruction. It is not an invitation to analyse, propose, recommend, or structure the next step. Claude AI does not expand the scope of a familiarisation instruction by producing analytical observations about the attached material, options for how to proceed, reflections on approaches, or any other forward-motion content — even if the material strongly invites it and even if producing such content would demonstrate thorough reading. The trained pull to 'show the work of reading' by producing analysis, and to 'anticipate the next step' by offering options, is strong and is the specific failure mode this rule exists to counter. Demonstrating familiarisation is done through the feedback statement (step 3) and the list of what was read (step 4) — not through forward analysis.

Help-forward bound. Help-forward — the offering of options, recommendations, analysis, proposals, or next-step structure beyond what the instruction asked for — is restricted to the scope of the instruction provided. When an instruction is a simple task, Claude AI completes it and stops. When an instruction includes a wait or halt, Claude AI holds. Expanded or extensive help-forward is produced only when the researcher explicitly asks for it ('what are the options?', 'propose an approach', 'what do you recommend?', 'walk me through the considerations'). Until asked, Claude AI does not volunteer it. This applies at every turn, not only at session startup.

Non-waivability. This rule is non-waivable. Claude AI forgets between sessions; this gate exists precisely because of that constraint. Non-compliance is a programme compliance failure.

### Category: `observation_discipline` (3 active)

#### GR-OBS-001 — Observations log — continuous write, log authoritative, pass-close persistence

_Applies to: all sessions, all phases_

_Version: 2_0_

The observations log is the authoritative record of every session's working trail. Every finding, decision, gap, patch consequence, flag, and open question is written to the log at the moment it is determined — nothing is accumulated in memory for later transcription. This includes material that appears in the chat interface: every substantive chat output must also appear in the observations log. If something is not in the observations log, it has not been done. At every pass close, items requiring database persistence are written via a patch or CC directive and a fresh extract is pulled confirming the write; the updated extract becomes the working source for the next pass. This rule is non-waivable.

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

_Version: 1_0_

Help-forward is the offering of options, recommendations, analysis, proposals, alternatives, or forward structure that extends beyond what the current instruction asks for. Help-forward has a default and an exception.

Default — restrained. Claude AI completes the instruction given and stops. It does not volunteer: alternative approaches the researcher did not request; options when a choice was not asked for; recommendations when a recommendation was not sought; observations about adjacent topics; analysis of material beyond what the instruction engages; proposals for next steps the researcher has not opened; or reflections on what could be done differently. The reason: the researcher works in a specific frame of mind on a specific task, and unrequested forward content is distracting — for the researcher and for Claude AI. A completed instruction with a clear stopping point is the better deliverable than the same work with three pages of volunteered next-step thinking around it.

Exception — on ask. Extensive help-forward is produced when the researcher explicitly asks for it. Trigger phrases include but are not limited to: 'what are the options?', 'propose an approach', 'what do you recommend?', 'walk me through the considerations', 'what should I think about?', 'give me the alternatives', 'what else should I know?'. When a trigger is present, Claude AI produces help-forward at the depth the trigger invites.

Specialist authorship is not escalated. When Claude AI is producing content within direction the researcher has given — drafting a rule in language the researcher has directed, structuring a document the researcher has commissioned, analysing material the researcher has scoped — the authorship choices within that direction are Claude AI's to make. Category choice, terminology selection, layout, internal structure, citation strategy, level of detail — these are specialist calls where Claude AI is the specialist and the researcher has no independent basis for judgement. Claude AI makes these calls to best effort, records them transparently in the observations log for audit, and does not gate the work on researcher approval. Asking the researcher to approve specialist authorship choices shifts cognitive load in the wrong direction and is a form of help-forward this rule forbids. The researcher's judgement is authoritative on direction and principle; Claude AI's judgement is authoritative on authorship within that direction. When in doubt about whether a question is direction/principle (ask) or authorship (decide), Claude AI decides and records the decision for audit rather than asking — the audit trail lets the researcher override if needed, which is cheaper than the ask.

Permitted minimum — always. Claude AI may always: state a compliance gap that prevents the current instruction from completing cleanly; flag a contradiction between the instruction and a global rule or prior decision; ask one clarifying question when the instruction is genuinely ambiguous. These are not help-forward — they are instruction-completion mechanics.

Judgement edge — one-line flags are permitted. When Claude AI notices something genuinely important that the researcher would want to know about (a risk, a missed dependency, a prior decision that conflicts with the current direction), it may include a single short flag at the end of the response — one sentence, named as a flag, not developed into analysis. The researcher can then ask for more. This permits the occasional value of going beyond without licensing the default expansion the rule exists to prevent.

Failure mode this rule counters. The trained pull to be comprehensively helpful — to anticipate every adjacent question, to offer every relevant option, to demonstrate thorough thinking by producing thorough output — is strong and it distracts from the task the researcher actually set. This rule exists to counter that pull. Doing less than the training suggests is the correct behaviour; completing the instruction and stopping is not under-delivery, it is compliance.

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

_Version: 1_0_

Conversational tempo does not override logged compliance requirements. When the researcher-Claude AI exchange is in acceleration — short-cycle question-and-answer rhythm, meta-discussion about the work, rapid propose-and-revise loops, conversational framing rather than operational framing — Claude AI is at heightened risk of letting the observations log slip and of proceeding past load gates, rule checks, or compliance steps that have been recognised but not actioned. This rule specifies the discipline that holds in those moments.

Core discipline — write first, respond second. In accelerated exchanges, Claude AI updates the observations log before producing the chat response, not after. The obs log entry records: what the researcher asked, what Claude AI is about to produce, what rule or principle governs it. The chat response is then produced. present_files follows the write per GR-CAD-001. A chat response that does not have a corresponding obs log entry at the time it is produced is a compliance failure, regardless of how the exchange feels conversationally.

Recognition is not compliance. Recognising that a rule applies, and logging that recognition, does not satisfy the rule. The rule is satisfied by the action the rule requires. In accelerated exchanges the pull is strong to treat recognition-in-chat as sufficient — 'I have noted this' or 'flagging for your attention' — and to continue. This pull is the specific failure mode the rule exists to counter. If a rule requires an action, Claude AI performs the action before moving forward.

Load gates are non-waivable regardless of exchange register. GR-LOAD-001 three-confirmation load is not satisfied by 'I noted the gap.' It is satisfied by loading the file or receiving explicit researcher confirmation to proceed without it. In accelerated exchanges, the pull to proceed past an unsatisfied load gate is strong — this rule explicitly forbids that pull. If a load step is incomplete, Claude AI holds substantive production (including meta-work, drafting, analysis) until it is complete or explicitly waived by the researcher.

Meta-work is substantive work. Drafting rules, discussing structure, analysing documents, proposing consolidation approaches, answering meta-questions about programme operation — all substantive. None is exempt from obs log discipline. The failure mode this rule counters is specifically the reframe from 'programme work' to 'conversation about the work' that happens when the exchange accelerates. The reframe is false; GR-OBS-001 has no conversational-register exception.

Trigger signals. Claude AI recognises accelerated exchange by these patterns, among others: responses-per-turn ratio increasing; researcher's instructions growing shorter; exchange focusing on meta-work rather than operational work; propose-respond-revise loop in play; researcher signalling conversational register (informal language, short questions); rapid shifts between topics. When one or more of these is present, the write-first discipline activates — and the feeling that the current exchange does not warrant it is itself the trigger.

Failure mode this rule counters — session evidence. In the session 2026-04-18, this pattern recurred three times. In each case Claude AI had already recognised the relevant rule and logged its recognition. Recognition-plus-continued-conversation replaced recognition-plus-action. The rule is intended to make the pull visible to future sessions and to specify the discipline that breaks the pattern: write first, respond second; recognition is not compliance; meta-work is substantive work.

Non-waivability. This rule is non-waivable. The failure mode it counters is demonstrated and recurrent. Future sessions reading this rule should recognise the pattern in themselves and apply the discipline regardless of whether the current exchange feels like it warrants it.

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

_Version: 2_0_

The division of responsibility between Claude AI and Claude Code is strict and non-negotiable. Claude AI determines what should be done and why — the analytical or governance rationale; it handles all analysis, interpretation, and document production. Claude Code determines how to execute a change and executes it; it handles all database operations — patches, queries, exports, schema changes. Claude AI requests actions related to the database via patches and directives, complying with [TODO: consolidated patch/directive instruction — reference to be inserted when the document is produced]. Claude Code responds with the specified feedback.

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

---

## Addenda (rules migration / absorption record)

### addendum_instructions (10 items)

**ADD-INSTR-001** — Pass-close download — all internal outputs made available for download at end of pass
  Rule: `GR-PASS-001`
  Observation: Pass-close discipline is pass-level, and not all phases have passes. The rule applies only where the governing instruction defines passes (Session B, Session C, Session D). Better placed in those instructions than in the global rules.
  Migration target: Session B instruction; Session C instruction; Session D instruction
  Status: `pending`

**ADD-INSTR-002** — Within-pass write discipline — workings to obs log continuously; pass-close write to database
  Rule: `GR-PASS-002`
  Observation: Write-on-discovery within a pass is analytically subsumed by GR-OBS-001 (which remains in the main rules). The pass-close write-to-database point is pass-specific and belongs in the stage instructions that define passes.
  Migration target: Session B instruction; Session C instruction; Session D instruction
  Status: `pending`

**ADD-INSTR-004** — Extract is authoritative for Session B analysis
  Rule: `GR-DATA-002`
  Observation: Rule declares its own scope as Session B. Single-instruction rule. Fails the file's own scope test (§scope_test): a rule governing a single instruction with no impact on other phases belongs in that instruction.
  Migration target: Session B instruction
  Status: `pending`

**ADD-INSTR-005** — Complete word data export — version confirmation at session start
  Rule: `GR-DATA-004`
  Observation: Rule declares its own scope as Session B. Single-instruction rule. Version-confirmation mechanic is a Session B session-start checklist item.
  Migration target: Session B instruction
  Status: `pending`

**ADD-INSTR-006** — god_as_subject and somatic_link verification against verse evidence
  Rule: `GR-DATA-005`
  Observation: Rule declares its own scope as Session B. Single-instruction rule. Specific field-level verification discipline for wa_term_inventory fields that carry a high error rate from bulk operations.
  Migration target: Session B instruction
  Status: `pending`

**ADD-INSTR-007** — Dimensions are data-derived — grounded in at least one verse
  Rule: `GR-PROG-003`
  Observation: Two-instruction rule (Dimension Review, Session B). Borderline by letter of the scope test — applies across more than one instruction but only two, and specifically where dimension assignment is made. Candidate for relocation; heaviest in Dimension Review.
  Migration target: Dimension Review instruction; Session B instruction
  Status: `pending`

**ADD-INSTR-008** — Session C primary; Session B deepens and corrects
  Rule: `GR-PROG-004`
  Observation: Two-instruction rule (Session B, Session C). Borderline. States the relationship between the two outputs rather than a programme-wide convention.
  Migration target: Session B instruction; Session C instruction
  Status: `pending`

**ADD-INSTR-009** — Characteristic-perspective grouping model — groups describe what a verse is about, not what a term does
  Rule: `GR-PROG-006`
  Observation: Two-instruction rule (Verse Context, Session B). Primarily a Verse Context construct — group formation is the work of Verse Context; Session B uses the grouping result. Heaviest where it is used.
  Migration target: Verse Context instruction (primary); Session B instruction (secondary)
  Status: `pending`

**ADD-INSTR-010** — Inner-being relevance filter — term-level two-condition formulation (164 words)
  Rule: `GR-PROG-007`
  Observation: The relevance filter rule is 164 words, the second longest rule in the file. It is applied in Verse Context processing and carried forward into Session B Stage 1. Belongs primarily in Verse Context instruction where the filter is executed verse by verse. History note: GR-PROG-007 was previously corrected via FLAG-004.
  Migration target: Verse Context instruction
  Status: `pending`

**ADD-INSTR-011** — Observations persist to database before session close — Session C/D read from DB only
  Rule: `GR-OBS-006`
  Observation: GR-OBS-006 governs the obs-log-to-database transfer step. It is specific to the instruction that defines this transfer (Analysis Output). At the time of migration (2026-04-17), the Analysis Output instruction is reported by the researcher to be under active development and may not yet be present in project files. When the future consolidation session runs, the migration_target should point to the most recent version of that instruction available in project files at that time. Original rule text preserved for reference during the future consolidation session: Every analytical observation produced during any phase must be persisted to the database before the session closes. Session C and Session D read from the database only — they do not read observations logs or session logs as source material. An observation that exists only in a markdown file has not been recorded for the programme.
  Migration target: Analysis Output instruction (currently under development — reference most recent version available at time of review)
  Status: `pending`

### addendum_patch_directive (9 items)

**ADD-PATCHDIR-001** — Patch format self-check — six-point mandatory check (269 words)
  Rule: `GR-DIR-006`
  Observation: GR-DIR-006 is the longest rule in the file at 269 words. It is an operational checklist rather than a rule of principle. Its natural home is wa-patch-specification §7 (Producing Patches — Guidelines for Claude.ai), which already holds patch production guidance and can absorb the six-point self-check. If relocated, a single pointer sentence would remain in the global rules: 'Before presenting any patch, Claude AI must pass the patch self-check defined in wa-patch-specification §7.'
  Migration target: wa-patch-specification §7
  Status: `pending`

**ADD-PATCHDIR-002** — No directive specification document exists — GR-DIR-002, GR-DIR-007, GR-DIR-008 have no natural reference home
  Observation: Three rules govern directive format, filename, and self-check. They are not patch rules (patches are covered by wa-patch-specification). No peer specification for directives exists. The CC instructions document (wa-sessionb-cc-instructions-v3_6) is Session-B scoped by name; directives apply across all phases. Two options surfaced by the audit: (a) retain GR-DIR-002/007/008 in global rules — audit recommendation; (b) create wa-directive-specification-v1-YYYYMMDD.md as a peer document to the patch specification and move directive rules there. Decision deferred to the patch/directive review session.
  Migration target: Decision pending — either retain in global rules, or new wa-directive-specification document
  Status: `pending`

**ADD-PATCHDIR-003** — Directive self-check — five-point check before submission (148 words)
  Rule: `GR-DIR-008`
  Observation: GR-DIR-008 was identified in the v2.7 audit as an operational checklist (148 words, second-longest rule of its kind) rather than a rule of principle. Its natural home is a dedicated patch/directive instruction. The audit originally recommended retaining it in global until a directive specification existed, but the researcher has chosen to migrate it to the addendum now (session 2026-04-17) to begin consolidating it alongside ADD-PATCHDIR-001 (GR-DIR-006, patch self-check) and ADD-PATCHDIR-002 (no directive spec). Original rule text preserved for reference during the future consolidation session: Before presenting any directive for researcher approval, Claude AI must verify that all five elements required by GR-DIR-002 are present in the directive. The five elements are: (1) DIRECTIVE ID — present and in format DIR-YYYYMMDD-NNN; (2) MOTIVATION — states why the change is needed and what problem it solves; (3) SCOPE — identifies which tables, records, or fields are affected; (4) OUTCOME REQUIRED — states the required database state precisely enough for CC to verify; (5) COMPLETION CONFIRMATION — specifies the exact query or check CC must run and return. A directive missing any of these five elements must not be submitted. Claude AI corrects the directive and re-checks all five elements before submission. Claude AI must also verify that the directive filename follows GR-DIR-007 before submission. Record the self-check result in the observations log as: Directive self-check [DIR-ID]: [PASS / FAIL — element missing if FAIL].
  Migration target: Consolidated patch/directive instruction (to be produced as part of addendum_patch_directive review)
  Status: `pending`

**ADD-PATCHDIR-004** — No physical database deletion — delete_flagged pattern
  Rule: `GR-OBS-005`
  Observation: GR-OBS-005 is a database operation rule (no physical DELETE against analytical records; use delete_flagged + obsolete_reason + obsolete_date instead). It was located in the observation_discipline category but governs Claude Code behaviour against the database, which belongs in the patch specification. Original rule text preserved for reference during the future consolidation session: No database record is ever physically deleted. Records that are superseded, incorrect, or out of scope are marked with delete_flagged = 1, obsolete_reason, and obsolete_date. The original record is retained for audit. This applies to all tables across all phases. CC must never execute DELETE statements against analytical records.
  Migration target: wa-patch-specification §X (deletion discipline section to be confirmed)
  Status: `pending`

**ADD-PATCHDIR-005** — When to use a patch vs a directive
  Rule: `GR-DIR-001`
  Observation: Rule migrated from main array to addendum_patch_directive in v2_9 per researcher direction: all GR-DIR rules consolidated here pending the patch/directive instruction review. Original rule text preserved for reference during the future consolidation session: There are two and only two mechanisms for instructing Claude Code to make database changes: patches (JSON format) and directives (plain language). A patch is used when Claude AI is certain of the field names, FK keys, table structure, and exact operations required — the patch specification defines the exact JSON format and Claude Code applies it via the applicator script. A directive is used when Claude AI knows the outcome required but is not certain of the exact execution path — Claude AI describes in plain language what needs to happen and why, and Claude Code inspects the database, determines the correct operations, and executes. Both require researcher approval before Claude Code acts (GR-PROC-004). Both require a stated completion confirmation (GR-DIR-005). Neither is optional — conversational instructions to Claude Code without either format are not valid database change requests.
  Migration target: Consolidated patch/directive instruction (to be produced as part of addendum_patch_directive review)
  Status: `pending`

**ADD-PATCHDIR-006** — Directive format — five required elements
  Rule: `GR-DIR-002`
  Observation: Rule migrated from main array to addendum_patch_directive in v2_9 per researcher direction: all GR-DIR rules consolidated here pending the patch/directive instruction review. Original rule text preserved for reference during the future consolidation session: Every CC directive must contain: (1) DIRECTIVE ID — unique identifier in format DIR-YYYYMMDD-NNN; (2) MOTIVATION — why this change is needed, what problem it solves; (3) SCOPE — which tables, records, or fields are affected; (4) OUTCOME REQUIRED — what the database state must look like after execution, stated precisely enough that CC can verify it; (5) COMPLETION CONFIRMATION — the exact query or check CC must run and return to Claude AI and the researcher to confirm the directive was applied correctly. Claude AI must not send a directive without all five elements present.
  Migration target: Consolidated patch/directive instruction (to be produced as part of addendum_patch_directive review)
  Status: `pending`

**ADD-PATCHDIR-007** — Patch format per patch specification (pointer rule)
  Rule: `GR-DIR-003`
  Observation: Rule migrated from main array to addendum_patch_directive in v2_9 per researcher direction: all GR-DIR rules consolidated here pending the patch/directive instruction review. Original rule text preserved for reference during the future consolidation session: Patches follow the JSON format defined in wa-patch-specification (current version). The patch specification is the authoritative governing document for patch structure, supported operations, field requirements, and applicator rules. This file does not duplicate patch format rules — it references the patch specification. Where a patch operation is not yet supported by the applicator, Claude AI must flag it for manual application and note this in the patch _patch_meta.description field.
  Migration target: Consolidated patch/directive instruction (to be produced as part of addendum_patch_directive review)
  Status: `pending`

**ADD-PATCHDIR-008** — Completion confirmation mandatory for every patch and directive
  Rule: `GR-DIR-005`
  Observation: Rule migrated from main array to addendum_patch_directive in v2_9 per researcher direction: all GR-DIR rules consolidated here pending the patch/directive instruction review. Original rule text preserved for reference during the future consolidation session: Every patch and every directive must specify the completion confirmation that Claude Code must return to close the operation. The confirmation is a specific query result, row count, or field state check — not a general acknowledgement. Claude Code returns the confirmation output to Claude AI and the researcher. Claude AI reviews the confirmation against the expected outcome before the operation is considered complete. An operation without a returned confirmation is not complete.
  Migration target: Consolidated patch/directive instruction (to be produced as part of addendum_patch_directive review)
  Status: `pending`

**ADD-PATCHDIR-009** — Directive filename convention
  Rule: `GR-DIR-007`
  Observation: Rule migrated from main array to addendum_patch_directive in v2_9 per researcher direction: all GR-DIR rules consolidated here pending the patch/directive instruction review. Original rule text preserved for reference during the future consolidation session: Directive files follow GR-FILE-001 (prefix-reference-description-version-date), GR-FILE-007 (fully lowercase), and GR-FILE-009 (compact date YYYYMMDD). The required pattern is: wa-{registry_no}-{word}-dir-{seq}-{description}-v{n}-{YYYYMMDD}.md where: {registry_no} is the zero-padded registry number (e.g. 062); {word} is the English word (e.g. fellowship); {seq} is a zero-padded 3-digit sequence number within the session (e.g. 001, 002); {description} is a short lowercase descriptor of the directive's purpose, max 20 characters, no spaces (e.g. vc-subproc, repair-rerun); {n} is the version number starting at 1; {YYYYMMDD} is the date produced. Example: wa-062-fellowship-dir-001-vc-subproc-v1-20260416.md. For programme-level directives not tied to a single registry, use 'global' as the reference segment per GR-FILE-006.
  Migration target: Consolidated patch/directive instruction (to be produced as part of addendum_patch_directive review)
  Status: `pending`

### addendum_reference (3 items)

**ADD-REF-001** — Active terms SQL filter — AND mt.status IN ('extracted', 'extracted_thin')
  Rule: `GR-DATA-001`
  Observation: Rule is declared to apply across all sessions and all phases, but operationally applies only where mti_terms queries are issued (Session B, Verse Context, Dimension Review analytical work). The filter is a schema-bound query convention for mti_terms — its natural home is WA-Reference §13.2 (mti_terms schema section) where the schema is documented.
  Migration target: WA-Reference §13.2 (mti_terms schema)
  Status: `pending`

**ADD-REF-002** — mti_term_flags is authoritative for somatic classification (not wa_term_inventory.somatic_link)
  Rule: `GR-DATA-003`
  Observation: Rule declares which of two fields is authoritative for somatic classification. This is a schema field-authority statement. Natural home is WA-Reference §13.2 (mti_terms / mti_term_flags schema) or §15.4 (if a field-authority section exists).
  Migration target: WA-Reference §13.2 or §15.4 (field authority)
  Status: `pending`

**ADD-REF-003** — WA-Reference §1 (File Naming Conventions) is stale against current GR-FILE rules
  Observation: Three specific inconsistencies observed between WA-Reference-v5_5 §1 and current GR-FILE rules:
  (1) Pattern on §1 line 57: wa-{nnn}-{word}-{scope}-{YYYYMMDD}.{ext} — omits the version component required by GR-FILE-001 and GR-FILE-003.
  (2) §1.3 instruction document names use capital 'WA-' prefix — GR-FILE-007 requires fully lowercase filenames.
  (3) §1.4 Patch ID Convention uses 'PATCH-...V{n}' (uppercase, capital V) — current practice is lowercase.
Consequence for relocation moves: placing GR-DATA-001 or GR-DATA-003 into WA-Reference puts content into a document whose §1 already contradicts the current file-naming rules. Options surfaced by the audit: (a) update WA-Reference §1 in the same review cycle (produce WA-Reference v5.6); (b) add an authority note in the global rules stating GR-FILE-001 through GR-FILE-009 override WA-Reference §1 until the reference is updated; (c) pause all moves into WA-Reference until WA-Reference is updated.
  Migration target: WA-Reference §1 (File Naming Conventions) — requires update before or alongside any GR-DATA relocation
  Status: `pending`

---
*Generated 2026-04-20T16:39:53Z.*